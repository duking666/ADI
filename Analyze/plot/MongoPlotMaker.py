#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/9/20 4:03 下午
# @Author  : kewen
# @File    : MongoPlotMaker.py
import pymongo

from plot.BaseMaker import BaseMaker


class MongoPlotMaker(BaseMaker):

    def __init__(self, logName: str):
        super().__init__()
        mongo = pymongo.MongoClient(host="localhost", port=27017)
        db = mongo['adi_analyze']
        self.collection = db[logName]

    def make(self, jsonList: list):
        # 插入到 MongoDB
        print("\n聚合完毕，批量存入到数据库...")
        self.collection.insert(jsonList)
