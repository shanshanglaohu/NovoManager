#!/ure/bin/env python
# _*_coding:utf-8_*_
__author__ = "hz"

import argparse
import os
from functools import wraps
from peewee import *
import xlrd
from create_novo_db import RawData

LANE_ID = 0
PROJECT_NUM = 2
PROJECT_NAME = 3
NOVO_ID = 4
SAMPLE_NAME = 5
LIB_ID = 9
INDEX = 10
QC_INDEX = 11
INDEX_SEQ = 12
PATH = 19
ANALYST = 22


parser = argparse.ArgumentParser()
parser.add_argument(
    "-d", "--dir", dest="dir",
    help=u"存放下机单的文件夹路径"
)
parser.add_argument(
    "-i", "--input", dest="input",
    help=u"下机单"
)
args = vars(parser.parse_args())

db = SqliteDatabase("novo.db")


def safe_db(fuc):
    @wraps(fuc)
    def wrapper(**kwargs):
        db.connect()
        fuc(**kwargs)
        db.close()
    return wrapper


# def save(rs, analyst=None, project_name=None):
#     for i in range(rs.nrows):
#         if rs.cell_value(i, ANALYST) == analyst:
#             raw_data, created = RawData.get_or_create(
#                 lane=rs.cell_value(i, LANE_ID),
#                 project_num=rs.cell_value(i, PROJECT_NUM),
#                 project_name=rs.cell_value(i, PROJECT_NAME),
#                 novo_id=rs.cell_value(i, NOVO_ID),
#                 sample_name=rs.cell_value(i, SAMPLE_NAME),
#                 lib_name=rs.cell_value(i, LIB_ID),
#                 index=rs.cell_value(i, INDEX),
#                 qc_index=rs.cell_value(i, QC_INDEX),
#                 index_seq=rs.cell_value(i, INDEX_SEQ),
#                 path=rs.cell_value(i, PATH),
#                 analyst=rs.cell_value(i, ANALYST),
#             )


@safe_db
def file_to_db(**kwargs):
    """
    Extract raw data path from excel file and store them into sqlit3 db
    :param file_name: an raw data path file with .xls or .xlsx format
    :param analyst: name of analyst
    :return: None
    """
    file_name = kwargs.get("file_name")
    analyst = kwargs.get("analyst")
    rb = xlrd.open_workbook(file_name)
    rs = rb.sheet_by_index(0)
    for i in range(rs.nrows):
        if rs.cell_value(i, ANALYST) == analyst:
            raw_data, created = RawData.get_or_create(
                lane_id=rs.cell_value(i, LANE_ID),
                project_num=rs.cell_value(i, PROJECT_NUM),
                project_name=rs.cell_value(i, PROJECT_NAME),
                novo_id=rs.cell_value(i, NOVO_ID),
                sample_name=rs.cell_value(i, SAMPLE_NAME),
                lib_name=rs.cell_value(i, LIB_ID),
                index=rs.cell_value(i, INDEX),
                qc_index=rs.cell_value(i, QC_INDEX),
                index_seq=rs.cell_value(i, INDEX_SEQ),
                path=rs.cell_value(i, PATH),
                analyst=rs.cell_value(i, ANALYST),
            )


def files_to_db(**kwargs):
    """

    :param work_dir: the directory abs path
    :param analyst: analyst name
    :return:
    """
    work_dir = kwargs.get("work_dir")
    analyst = kwargs.get("analyst")
    if os.path.exists(work_dir):
        for excel in os.listdir(work_dir):
            file_to_db(file_name=os.path.join(work_dir, excel), analyst=analyst)


if __name__ == '__main__':
    # unprocessed = "未使用下机路径.xlsx"
    # file_to_db(file_name=unprocessed, analyst="胡志刚")
    pass