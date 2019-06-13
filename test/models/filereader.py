#-*- coding:utf-8 -*-
"""
文件读取。YamlReader读取yaml文件，ExcelReader读取excel.
"""

import yaml
import os
from xlrd import open_workbook
import sys
# basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(basedir)


class YamlReader:
    def __init__(self, yamlf):
        if os.path.exists(yamlf):
            self.yamlf = yamlf
        else:
            raise FileNotFoundError('文件不存在')
        self._data = None

    @property
    def data(self):
        # 如果是第一次调用data，读取yaml文档，否则直接返回之前保存的数据
        if not self._data:
            with open(self.yamlf, 'rb') as f:
                self._data = list(yaml.safe_load_all(f))
                # load后是个generator,用list组织成列表
        return self._data


class SheetTypeError(Exception):
    pass


class ExcelReader:
    """
    读取excel文件中的内容。返回list.
    如：excel中内容为：
    A  B  C
    A1 B1 C1
    A2 B2 C2

    如果 print(ExcelReader(excel, title_line=True).data),输出结果：
    [{A: A1, B: B1, C: C1}, {A: A2, B: B2, C: C2}]
    如果 print(ExcelReader(excel, title_line=Flase).data),输出结果：
    [[A,B,C], [A1, B1, C1],[A2,B2,C2]]

    可以指定sheet, 通过index或者name:
    ExcelReader(excel, sheet=2)
    ExcelReader(excel, sheet='BaiDuTest')
    """
    def __init__(self, excel, sheet=0, title_line=True):
        if os.path.exists(excel):
            self.excel = excel
        else:
            raise FileNotFoundError('文件不存在！')
        self.sheet = sheet
        self.title_line = title_line
        self._data = list()

    @property
    def data(self):
        if not self._data:
            with open_workbook(self.excel, 'r') as workbook:
                if type(self.sheet) not in [int, str]:
                    raise SheetTypeError('Please pass in <type ine> or <type str>, not {0}'.format(type(self.sheet)))
                elif type(self.sheet) == int:
                    s = workbook.sheet_by_index(self.sheet)
                else:
                    s = workbook.sheet_by_name(self.sheet)

                if self.title_line:
                    title = s.row_values(0) #首行为title
                    for col in range(1, s.nrows):
                        # 依次遍历其余行，与首行组成dict,拼到self._data中
                        # zip:翻转字典（交换键值对的位置）
                        self._data.append(dict(zip(title, s.row_values(col))))
                else:
                    for col in range(0, s.nrows):
                        # 遍历所有行，拼到self._data中
                        self._data.append(s.row_values(col))
                #workbook.close()
        return self._data


import csv
# 解决UnicodeDecodeError: 'gbk' codec can't decode byte 0xad in position 22:
# illegal multibyte sequence问题
import codecs


class CSVReader:
    def __init__(self, csvf, title_line=True):
        if os.path.exists(csvf):
            self.csvf = csvf
        else:
            raise FileNotFoundError('文件不存在')
        self._data = list()

    @property
    def data(self):
        # 'utf_8_sig' 可以去除非法字符'\ufeff'
        if not self._data:
            with codecs.open(self.csvf, 'rb', encoding='utf_8_sig') as f:
                self._data = list(csv.reader(f))
        return self._data
        

if __name__ == '__main__':
    
    #y = 'E:/Python35_case/thirdparty_test/config/config.yml'
    #reader = YamlReader(y)
    #print(reader.data)

    e = 'E:/Python35_case/thirdparty_test_1 - Copy/data/thirdpartyuser.xlsx'
    reader = ExcelReader(e, title_line=True).data
    for r in reader:
        print(r)

    #excel = 'E:/Python35_case/thirdparty_test_1 - Copy/data/user_info.csv'
    #datas = CSVReader(excel).data
    #for d in datas:
        #print(d)
