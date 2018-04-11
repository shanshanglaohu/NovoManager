#!/ure/bin/env python
# _*_coding:utf-8_*_
__author__ = "hz"

u"""
    本模块用于从信息收集表中提取信息
    将从信息收集表中提取以下信息，项目名称，合同编号
    若为自建库项目：则提取送样名、结题报告中的样品名称、诺和编号、index号、index序列
    若为公司建库项目，则提取家系编号、送样名称、结题报告中送样名、诺禾编号、性别、是否患病
"""

import xlrd


PERSONAL_INDEX = {
    u"送样名称": 10,
    u"结题报告中样品名称": 11,
    u"诺禾编号": 12,
    u"index号": 13,
    u"index序列": 14
}

COMPANY_INDEX = {
    u"家系编号": 10,
    u"送样名称": 11,
    u"结题报告中样品名称": 12,
    u"诺禾编号": 13,
    u"性别": 14,
    u"是否患病": 16
}


class InfoExtractor(object):
    """
    extract information form Novogene information collection table
    """
    def __init__(self, info_table):
        self.info_table = info_table
        self._sheet = xlrd.open_workbook(info_table).sheet_by_index(0)
        self._personal_title = [
            u"送样名称", u"结题报告中样品名称", u"诺禾编号",
            u"index号", u"index序列"
        ]
        self._company_title = [
            u"家系编号", u"送样名称", u"结题报告中样品名称",
            u"诺禾编号", u"性别", u"是否患病"
        ]

    def get_contact_number(self):
        u"""
        extract project number from information collection table
        :return: project number with type of unicode
        """
        return self._sheet.cell_value(4, 4)

    def get_project_num(self):
        u"""
        extract project name from information collection table
        :return: project name with type of unicode
        """
        return self._sheet.cell_value(5, 4)

    def get_project_name(self):
        u"""
        extract project name from information collection table
        :return: project name with type of unicode
        """
        return self._sheet.cell_value(6, 4)

    def get_personal_info(self, key):
        u"""
        extract information in personal information table columns named
        u"送样名称", u"结题报告中样品名称", u"诺禾编号", u"index号", u"index序列"
        :return: generator of raw information
        """
        table_start = 14
        while table_start < self._sheet.nrows:
            if self._sheet.row_values(table_start)[11]:
                yield self._sheet.row_values(table_start)[PERSONAL_INDEX.get(key)]
            table_start += 1

    def get_company_info(self, key):
        u"""
        extract information in company information table columns named
        u"家系编号", u"送样名称", u"结题报告中样品名称",
        u"诺禾编号", u"性别", u"是否患病"
        :param key:
        :return:
        """
        table_start = 14
        while table_start < self._sheet.nrows:
            if self._sheet.row_values(table_start)[11]:
                yield self._sheet.row_values(table_start)[COMPANY_INDEX.get(key)]
            table_start += 1

    def get_type(self):
        if u"index号" in self._sheet.row_values(13):
            return "personal"
        else:
            return "company"


if __name__ == '__main__':
    pass
