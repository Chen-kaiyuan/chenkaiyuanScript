# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     CreateIDaPhone.py
   Description :   Create ID or Phone or name with random number
   Author :        Cky
   date：          2017-12-26 10:52:57
-------------------------------------------------
   Change Activity:
                   No / time / type / data / author
                   1 / 2018-1-3 / add / createName on code / cky

-------------------------------------------------
"""
import os
import random
import time
import datetime
import CreateID



# PATH
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
DC_PATH = '{0}{1}'.format(BASE_DIR,'\districtcode.txt')
Name_PATH = '{0}{1}'.format(BASE_DIR,'\Chinese_Names_Corpus.txt')

# Create phone with randow number

def createPhoneNO():
    """
    Create Phone number with random
    :param:
            null
    :return:
             Phone number
    """
    headlist = ["130","131","132","133","134","135","136","137","138","139","147","150","151","152","153","155","156","157","158","159","186","187","188"]
    headdata = random.choice(headlist)
    NOdata = ''.join(random.choice('0123456789')for i in range (8))
    PhoneNO = '{}{}'.format(headdata,NOdata)
    return PhoneNO


# Create ID with random number
def createCDdata():
    """
    create city data on list
    :param:
            null
    :return:
             null
    """
    with open(DC_PATH) as file:
        cddata = file.read()
        cddatalist = cddata.split('\n')
    for node in cddatalist:
        if node[10:11] != '':
            state = node[10:].strip()
        if node[10:11] == ' ' and node[12:13] != ' ':
            city = node[12:].strip()
        if node[10:11] == ' ' and node[12:13] == ' ':
            district = node[14:].strip()
            code = node[0:6]
            codelist.append({"state": state, "city": city, "district": district, "code": code})

def createIDNO():
    """
    create ID number with random
    :param:
            null
    :return:
             ID number
    """
    global  codelist
    codelist = []
    if not codelist:
        createCDdata()
        da = datetime.date.today() + datetime.timedelta(days=random.randint(1, 366))
        id = '{}{}{}{}'.format(codelist[random.randint(0,len(codelist))]['code'],str(random.randint(1930,2013)),da.strftime('%m%d'),str(random.randint(100,300)))
        i = 0
        weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]  # 权重项
        checkcode = {'0': '1', '1': '0', '2': 'X', '3': '9', '4': '8', '5': '7', '6': '6', '7': '5', '8': '5', '9': '3',
                     '10': '2'}  # 校验码映射
    for i in range(0, len(id)):
        count = int(id[i]) * weight[i]
        id = '{}{}'.format(id, checkcode[str(count % 11)])
        return id

# Create Chinese name with random datas

def createName():
    """
    create Chinese name with random
    :return:
             one china name
    """
    namedatas = open(Name_PATH, 'r').readlines()
    random.shuffle(namedatas)
    NameData = namedatas[1]
    return NameData

def newID():
    """
       create ID number with random
       :param:
               null
       :return:
                ID number
       """
    #citys = CreateID.city()
    citys = '110000'
    second = CreateID.year()
    mon = CreateID.mons()
    day = CreateID.days()
    sxh = CreateID.sxhs()
    oldid = "{}{}{}{}{}".format(citys, second, mon, day, sxh)
    newid = CreateID.jxms(oldid)
    return newid



if __name__ == '__main__':
    Phone = createPhoneNO()
    #print(Phone)
    ID = createIDNO()
    #print(ID)
    name = createName()
    #print(name)
    id = newID()
    print(id)
