# __author__ = 'lty'
# -*- coding: utf-8 -*-
"""
得到公司名称和代码的映射字典
"""

import json
import urllib2
import time


class GetCompanyDict:
    def __init__(self):
        self.company_name_list = []
        self.company_code_list = []
        self.company_name_dict = {}
        self.company_code_dict_url = 'http://stock.fengjr.inc/stock/api/v1/cwsymbol/list'  # 获取公司字典的url
        self.company_code_dict = {}

    def get_code_name_hsymbol_dict(self):
        """
        得到一个字典:
        {'code':['name','hsymbol']}
        """
        data = urllib2.urlopen(self.company_code_dict_url, timeout=10).read()
        data_dict = json.loads(data)
        for k, v in data_dict.items():
            if k == str('data'):
                for i in range(0, len(v)):
                    name_tmp = ''
                    symbol_tmp = ''
                    hsymbol_tmp = ''
                    for k1, v1 in v[i].items():

                        if k1 == 'name':
                            name_tmp = v1
                        if k1 == 'symbol':
                            symbol_tmp = v1
                        if k1 == 'hsymbol':
                            hsymbol_tmp = v1
                    # print symbol_tmp
                    self.company_code_dict[str(symbol_tmp)] = []
                    self.company_code_dict[str(symbol_tmp)].append(name_tmp)
                    self.company_code_dict[symbol_tmp].append(hsymbol_tmp)

        # for k, v in self.company_code_dict.items():
        #     print k, v[0]
        return self.company_code_dict


if __name__ == '__main__':
    test = GetCompanyDict()
    x = test.get_code_name_hsymbol_dict()
    print x