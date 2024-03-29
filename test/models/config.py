# -*- coding:utf-8 -*-
"""
读取配置。这里配置文件用的yaml,也可用其他如XML，INI等，需在file_reader中添加相应
的Reader进行处理
"""
import os
from test.models.filereader import YamlReader
# import sys

# basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(basedir)


# 通过当前文件的绝对路径, 其父级目录一定是框架的base目录, 然后确定各层的绝对路径。
# 下面这种方法， 可以支持linux和windows等不同的平台，

BASE_PATH = os.path.split(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))[0]
CONFIG_FILE = os.path.join(BASE_PATH,'data','config', 'config.yml')
DATA_PATH = os.path.join(BASE_PATH, 'data')
DRIVER_PATH = os.path.join(BASE_PATH, 'drivers')
LOG_PATH = os.path.join(BASE_PATH,'report', 'log')
REPORT_PATH = os.path.join(BASE_PATH, 'report')
print("CONFIG_FILE", CONFIG_FILE)


class Config(object):
    def __init__(self, config=CONFIG_FILE):
        self.config = YamlReader(config).data

    def yaml_get(self, element, index=0):
        """
        yaml是可以通过'---'分节的。用YamlReader读取返回的是一个list,第一项是默认的
        节，如果有多个节，可以传入index来获取。这样我们其实可以把框架相关的配置放
        在默认节，其他的关于 项目的配置放在其他节中。可以在框架中实现多个项目的测试
        """
        return self.config[index].get(element)


if __name__ == '__main__':
    print ("BASE_PATH", BASE_PATH)
    print ("CONFIG_FILE", CONFIG_FILE)
    print("DATA_PATH", DATA_PATH)
    print ("DRIVER_PATH", DRIVER_PATH)
    print ("LOG_PATH", LOG_PATH)
    print("REPORT_PATH", REPORT_PATH)
    # url = Config().get('URL')
    # print(url)
