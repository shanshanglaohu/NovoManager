#!/ure/bin/env python
# _*_coding:utf-8_*_
__author__ = "hz"

from peewee import *

db = SqliteDatabase("novo.db")

#
# class Project(Model):
#     project_name = CharField(max_length=2048)
#     project_num = CharField(max_length=2048)
#     contract_num = CharField(max_length=2048, null=True)
#
#     class Meta:
#         database = db


class RawData(Model):
    lane_id = CharField(max_length=20, null=True)
    project_num = CharField(max_length=1024, null=True)
    project_name = CharField(max_length=1024, null=True)
    novo_id = CharField(max_length=1024, null=True)
    sample_name = CharField(max_length=1024, null=True)
    lib_name = CharField(max_length=1024, null=True)
    index = CharField(max_length=1024, null=True)
    qc_index = CharField(max_length=1024, null=True)
    index_seq = CharField(max_length=1024, null=True)
    path = CharField(max_length=2048, null=True)
    analyst = CharField(max_length=1024, null=True)

    is_used = BooleanField(default=False)

    class Meta:
        database = db


def create_novodb():
    db.connect()
    db.create_tables([RawData])
    db.close()

if __name__ == '__main__':
    create_novodb()