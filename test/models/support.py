#-*- coding:utf-8 -*-
"""一些支持方法，比如加密"""

import os
import sys
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

import hashlib
from utils.log import logger

class EncryptError(Exception):
    pass

def sign(sign_dict, private_key=None, encrypt_way='MDS'):
    """
    传入待签名的字典，返回签名后字符串
    1.字典排序
    2.拼接，用&连接，最后拼接上私钥
    3.MD5加密
    """
    dict_keys = sign_dict.keys()
    dict_keys.sort()

    string = ''
    for key in dict_keys:
        if sign_dict[key] is None:
            pass
        else:
            string += '{0}={1}&'.format(key, sign_dict[key])

    string = string[0:len(string) - 1]
    string = string.replace(' ', '')

    return encrypt(string, salt=private_key, encrypt_way=encrypt_way)

def encrypt(string, salt='', encrypt_way='MD5'):
    """根据输入的string与加密，按照encrypt方式加密，并返回加密后的字符串"""
    string += salt
    if encrypt_way.upper() == 'MD5':
        hash_string = hashlib.md5()
    elif encry_way.upper() == 'SHA1':
        hash_string = hashlib.shal()
    else:
        logger.exception(EncryptError('清输入正确的加密方式，目前仅支持MD5和SHA1'))
        return False

    hash_string.update(string.encode())
    return hash_string.hexdigest()

if __name__ == '__main__':
    print(encrypt('100000307111111'))
            
