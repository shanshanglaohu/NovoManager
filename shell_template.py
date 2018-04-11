#!/ure/bin/env python
# _*_coding:utf-8_*_
__author__ = "hz"

WES = """python {pipline} \\
 --pn pn.txt \\
 --samp_info {sample_info} \\
 --samp_list {sample_list} \\
 --seqstrag WES_ag \\
 --WES_xten Y \\
 --TR {kit} \\
 --qcpre {suffix} \\
 --mail huzhigang@novogene.com \\
 --analy_array {array} \\
 --newjob {level}.{suffix}.{date}.job \\
"""

WGS = """python {pipline} \\
 --pn pn.txt \\
 --samp_info {sample_info} \\
 --samp_list {sample_list} \\
 --seqstrag WGS \\
 --qcpre {suffix} \\
 --mail huzhigang@novogene.com \\
 --analy_array {array} \\
 --newjob {level}.{suffix}.{date}.job \\
"""


TJ_V6 = "/PUBLIC/database/HUMAN/Cap/Exome_bed/Agilent/SureSelectXT.Human.All.Exon.V6/S07604514_Regions_extract.bed"
TJ_V5 = "/PUBLIC/database/HUMAN/Cap/Exome_bed/Agilent/SureSelectXT.Human.All.Exon.V5/agilent_region.bed"
NJ_V6 = "/NJPROJ1/DISEASE/share/Disease/Agilent/SureSelectXT.Human.All.Exon.V6/S07604514_Regions_extract.bed"
NJ_V5 = "/NJPROJ1/DISEASE/share/Disease/Agilent/SureSelectXT.Human.All.Exon.V5/agilent_region.bed"

TJ_pipline = "/ifs/TJPROJ3/DISEASE/share/Disease_pipeline/Human_reseq/Version_4.5/Human_reseq_pipeline.py"
NJ_pipline = "/NJPROJ1/DISEASE/share/Disease_pipeline/Human_reseq/Version_4.5/Human_reseq_pipeline.py"
tianjin = {"v5": TJ_V5, "v6": TJ_V6}
nanjing = {"v5": NJ_V5, "v6": NJ_V6}


def get_kits(city="tianjin"):
    if city == "tianjin":
        return tianjin
    else:
        return nanjing


def get_pipline(city="tianjin"):
    if city == "tianjin":
        return TJ_pipline
    else:
        return NJ_pipline


def get_analy_array(array=None, level=None, kind=None):
    if array:
        return array
    elif level.strip().lower() == "qc":
        return "1"
    elif level.strip().lower() == "mapping":
        return "1,2.1"
    elif level.strip().lower() == "primary" and kind.strip().lower() == "wes":
        return "1,2.1,3.1,5.3"
    elif level.strip().lower() == "primary" and kind.strip().lower() == "wgs":
        return "1,2.1,3.1,4.1,5.1"
    else:
        return "1,2.1,3.1,4.1,5.1,6.2,6.3,6.4,6.5,7.3,10.2,10.3,10.4"
