#!/ure/bin/env python
# _*_coding:utf-8_*_
__author__ = "hz"


import re
import xlrd
import os
import codecs
from info_table_extractor import InfoExtractor


def is_sample_id_valid(sample_id):
    return re.match(r"^[a-zA-Z][a-zA-Z\d_]*$", sample_id)


def normalize_sample_id(sample_id):
    if not re.match(r"^[a-zA-Z].*", sample_id):
        sample_id = "S_" + re.sub(r"[^a-zA-Z0-9_]", "_", sample_id.strip())
    else:
        sample_id = re.sub(r"[^a-zA-Z0-9_]", "_", sample_id.strip())
    return re.sub(r"_+", "_", sample_id)


def normalize_sample_ids(iterable):
    for i in iterable:
        yield normalize_sample_id(i)


def ffilled(iterable):
    temp_list = list()
    temp = u""
    for i in iterable:
        if i:
            temp = i
        temp_list.append(temp)
    return temp_list


def normalize_path(path):
    if "_DEP-ID_" in path:
        return path.replace("_DEP-ID_", "0206")
    else:
        return path


def normal_lib_id(lib_id, qc_index):
    if ";" in lib_id:
        return "-".join([lib_id.split("-")[0], qc_index.split(";")[0]])
        # return "-".join([lib_id.split("-")[0], qc_index.replace(";", "-")])
    # elif "-" in lib_id:
    #     return "-".join([lib_id.split("-")[0], qc_index])
    else:
        return lib_id


def safe_sheet(excel):
    sheets = xlrd.open_workbook(excel).sheets()
    for sheet in sheets:
        if sheet.nrows < 13:
            pass
        else:
            return sheet


def record_invalid_sample_id(info_file):
    extractor = InfoExtractor(info_file)
    all_valid = True
    if extractor.get_type() == "personal":
        sample_id = extractor.get_personal_info(key=u"结题报告中样品名称")
    else:
        sample_id = extractor.get_company_info(key=u"结题报告中样品名称")

    record = os.path.join(os.path.dirname(info_file), u"非法样品名.txt")
    with codecs.open(record, "w", encoding="utf-8") as f:
        sample_id = list(sample_id)
        if len(sample_id) != len(list(set(sample_id))):
            f.write(u"样本名存在重复，请检查\n")
            all_valid = False
        for i in sample_id:
            if not is_sample_id_valid(i):
                f.write(
                    u"非法样品名： {}\t标准后样品名： {}\n".format(
                        i, normalize_sample_id(i))
                )
                all_valid = False

    if all_valid:
        os.remove(record)
    return all_valid
