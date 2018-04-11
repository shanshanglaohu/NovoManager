#!/ure/bin/env python
# _*_coding:utf-8_*_
__author__ = "hz"

import os
from info_table_extractor import InfoExtractor
from utilities import is_sample_id_valid, normalize_sample_ids, ffilled


class IllegalValueError(Exception):
    def __init__(self, err=u"非法的取值"):
        super(Exception, self).__init__(err)


class InfoDataNormalizer(object):
    u"""
        用于将从信息收集表中收集到的数据规范化
        将信息表中空的性别、患病信息等替换为"U"
        将信息表中空的家系信息替换为"."
        将信息表中空的名称和诺禾编号补全
    """

    def __init__(self, extractor):
        self.extractor = extractor

    def personal_normalize(self):
        sample_name = ffilled(self.extractor.get_personal_info(key=u"送样名称"))
        sample_id = self.extractor.get_personal_info(key=u"结题报告中样品名称")
        sample_id = normalize_sample_ids(sample_id)
        novo_id = ffilled(self.extractor.get_personal_info(key=u"诺禾编号"))
        index = ffilled(self.extractor.get_personal_info(key=u"index号"))
        family_id = [u"."]*len(sample_name)
        isnormal = sex = [u"U"]*len(sample_name)
        index_seq = self.extractor.get_personal_info(key=u"index序列")
        return zip(sample_name, family_id,
                   sample_id, novo_id,
                   sex, isnormal,
                   index, index_seq
                   )

    def company_normalize(self):
        sample_name = ffilled(self.extractor.get_company_info(key=u"送样名称"))
        sample_id = self.extractor.get_company_info(key=u"结题报告中样品名称")
        sample_id = normalize_sample_ids(sample_id)
        family_id = (
            x if x else u"." for x in self.extractor.get_company_info(key=u"家系编号")
        )
        novo_id = ffilled(self.extractor.get_company_info(key=u"诺禾编号"))
        sex = (x if x else u"U" for x in self.extractor.get_company_info(key=u"性别"))
        isnormal = (
            x if x else u"U" for x in self.extractor.get_company_info(key=u"是否患病")
        )
        return zip(sample_name, family_id, sample_id, novo_id, sex, isnormal)

    def get_data(self):
        if self.extractor.get_type() == "personal":
            return self.personal_normalize()
        else:
            return self.company_normalize()

if __name__ == '__main__':
    info_table = os.path.join(
        os.path.dirname(os.path.dirname(__file__)).decode("gb2312"),
        u"35期信息收集表-自建库副本_20170710095357376 (1).xlsx")
    ext = InfoExtractor(info_table)
    nor = InfoDataNormalizer(extractor=ext)
    for i in nor.personal_normalize():
        print("\t".join(i))
