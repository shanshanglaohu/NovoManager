#!/ure/bin/env python
# _*_coding:utf-8_*_
__author__ = "hz"
# from __future__ import print_function, unicode_literals
from datetime import datetime
import codecs
import os
from peewee import *
DATE = datetime.now().strftime("%Y%m%d")

db = SqliteDatabase("novo.db")

from info_table_extractor import InfoExtractor
from info_data_normalizer import InfoDataNormalizer
from create_novo_db import RawData
from utilities import normalize_path, normal_lib_id
from shell_template import WES, WGS, get_kits
from collections import OrderedDict


def create_map_dict(data):
    data = list(data)
    print data
    novo_ids = [x[3] for x in data]
    map_dict = OrderedDict()
    if len(novo_ids) == len(set(novo_ids)):
        for i in data:
            map_dict[i[3]] = i
        return map_dict, 1
    else:
        for i in data:
            map_dict[(i[3], i[7])] = i
        return map_dict, 2


def get_info_data(map_dict):
    for value in map_dict.values():
        yield value[1], value[2], value[4], value[5]


def get_project_num(info_ditc):
    for key in info_ditc:
        if isinstance(key, basestring):
            try:
                project_num = RawData.get(RawData.novo_id == key).project_num
                print(project_num)
                return project_num
            except DoesNotExist:
                continue
        elif isinstance(key, tuple):
            try:
                project_num = RawData.get(
                RawData.novo_id == key[0],
                RawData.index_seq == key[1]
            ).project_num
                print(project_num)
                return project_num
            except DoesNotExist:
                continue


def get_list_data(info_dict, flag):
    print info_dict
    for key, value in info_dict.items():
        patient_id = sample_id = info_dict.get(key)[2]
        if flag == 1:
            query_set = RawData.select().where(RawData.novo_id == key)
        else:
            query_set = RawData.select().where(
                RawData.novo_id == key[0],
                RawData.index_seq == key[1]
            )
        for data in query_set:
            if data:
                yield data.lane_id, patient_id, sample_id, \
                      normal_lib_id(data.lib_name, data.qc_index),\
                      data.novo_id, data.qc_index, \
                      normalize_path(data.path)


def create_pn(project_nu, project_name, path):
    file_name = os.path.join(path, "pn.txt")
    with codecs.open(file_name, "w", "utf-8") as f:
        f.write(u"{}\t{}".format(project_nu, project_name))


def create_sample_info(data, suffix="", project_id="", doid="", disease="", path=""):
    """create file named sample_info_suffix in given path"""
    file_name = "sample_info_" + suffix + "." + DATE
    file_name = os.path.join(path, file_name)
    if doid:
        head = "#FamilyID\tSampleID\tSEX\tNormal/Patient\tPN\tDisease\n"
    else:
        head = "#FamilyID\tSampleID\tSEX\tNormal/Patient\tPN\n"
    stag = suffix[0: suffix.index("S")]
    with open(file_name, "w") as sample_info:
        sample_info.write(head)
        sample_info.write("#{}\n".format(stag))
        sample_info.write('#Disease:"{}"\n'.format(disease))
        if doid:
            for row in data:
                sample_info.write(
                    "{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{p_id}\t{doid}\n".format(
                        row=row, p_id=project_id, doid=doid
                    )
                )
        else:
            for row in data:
                sample_info.write(
                    "{row[0]}\t{row[1]}\t{row[2]}\t{row[3]}\t{p_id}\n".format(
                        row=row, p_id=project_id
                    )
                )
    return file_name


def create_sample_list(data, suffix="", path=""):
    """create file named sample_list_suffix in given path"""
    file_name = "sample_list_" + suffix + "." + DATE
    file_name = os.path.join(path, file_name)
    head = "#Ori_Lane\tPatientID\tSampleID\tLibID\tNovoID\tIndex\tPath\n"
    with open(file_name, "w") as sample_list:
        sample_list.write(head)
        for row in data:
            sample_list.write("lane{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(*row))
            if "novaseq" in row[-2] or "new" in row[-1]:
                new_lan = '2' if row[0].strip() == '1' else '1'
                sample_list.write("lane{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(
                    new_lan, *row[1:]
                ))
    return file_name


def fix_info(sample_info, sample_list):
    exsit_samples = list()
    fixed_info = list()
    with open(sample_info, "r") as info, open(sample_list) as li:
        for line in li:
            exsit_samples.append(line.split("\t")[1])
        for line in info:
            if line.startswith("#"):
                fixed_info.append(line)
            elif line.split("\t")[1] in exsit_samples:
                fixed_info.append(line)
            else:
                continue
    with open(sample_info, "w") as info:
        print("".join(fixed_info))
        info.write(
            "".join(fixed_info)
        )


def create_shell(sample_info, sample_list, date, **kwargs):
    if kwargs.get("seqstrag").strip().lower() == "wgs":
        template = WGS
    else:
        template = WES
        kits = get_kits(kwargs.get("place"))
        kwargs["kit"] = kits[kwargs["kit"].lower()]
    level = kwargs.get("level")
    suffix = kwargs.get("suffix")
    path = kwargs.get("path")
    file_name = "work_{level}_{suffix}_{date}.sh".format(
        level=level, suffix=suffix, date=date)
    file_name = os.path.join(path, file_name)
    with open(file_name, "w") as f:
        f.write(
            template.format(
                sample_info=sample_info, sample_list=sample_list,
                date=date, **kwargs)
        )


def main(**kwargs):
    if db.is_closed():
        db.connect()
    info_file = kwargs.get("info_file")
    suffix = kwargs.get("suffix")
    path = kwargs.get("path")
    disease = kwargs.get("disease")
    doid = kwargs.get("doid")

    extractor = InfoExtractor(info_file)
    normalizer = InfoDataNormalizer(extractor)
    data = normalizer.get_data()
    map_dict, flag = create_map_dict(data)
    project_id = extractor.get_project_num()
    print project_id
    project_name = extractor.get_project_name()

    create_pn(project_nu=project_id, project_name=project_name, path=path)

    sample_info = create_sample_info(
        get_info_data(map_dict), suffix=suffix,
        project_id=project_id, path=path,
        disease=disease, doid=doid
    )

    sample_info_name = os.path.basename(sample_info)
    sample_list = create_sample_list(
        get_list_data(map_dict, flag), suffix=suffix, path=path
    )

    sample_list_name = os.path.basename(sample_list)

    create_shell(
        sample_info=sample_info_name, sample_list=sample_list_name,
        date=DATE, **kwargs)

    fix_info(sample_info=sample_info, sample_list=sample_list)

    db.close()