# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     CreateID.py
   Description :   Create ID with random number
   Author :        Cky
   date：          2018-1-4 10:40:36
-------------------------------------------------
   Change Activity:
                   null
-------------------------------------------------
"""
import os
import random


BASE_DIR = os.path.dirname(os.path.realpath(__file__))
CY_PATH = '{0}{1}'.format(BASE_DIR,'\citycode.txt')


def city():
    """

    :return: city num
    """
    diqudata = open(CY_PATH, 'r').read()
    diqudatalist = diqudata.split()
    random.shuffle(diqudatalist)
    cd = diqudatalist[1]
    return cd

def year():
    """

    :return: year num
    """
    second = random.randint(1948,2000)
    return second

def mons():
    """

    :return: mon num
    """
    mon = random.randint(1,12)
    if mon < 10:
        mon = "{}{}".format('0',mon)
        return mon
    else:
        return mon

def days():
    """

    :return: day num
    """
    day = random.randint(1,31)
    if day <10:
        day = "{}{}".format('0',day)
        return day
    else:
        return day

def sxhs():
    """

    :return:
    """
    sxh = random.randint(100,999)
    return sxh

def jxms(id):
    """

    :param id: no check ID
    :return: ID
    """
    i = 0
    count = 0
    weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]  # 权重项
    checkcode = {'0': '1', '1': '0', '2': 'X', '3': '9', '4': '8', '5': '7', '6': '6', '7': '5', '8': '5', '9': '3', '10': '2'}  # 校验码映射
    for i in range(0, len(id)):
        count = count + int(id[i]) * weight[i]
    xsid = id + checkcode[str(count % 11)]  # 算出校验码
    return xsid
   
def NewID():
    """
    Just use this
    :param :
    :return:
    """
    citys = city()
    second = year()
    mon = mons()
    day = days()
    sxh = sxhs()
    oldid = "{}{}{}{}{}".format(citys, second, mon, day, sxh)
    newid = jxms(oldid)
    return newid
   
if __name__ == '__main__':
    Newid = NewID()
    print(Newid)
 
