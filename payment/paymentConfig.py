# -*- coding: UTF-8 -*-
import time, asyncio
from aiohttp import ClientSession
import aiohttp
import aioredis
import pymysql
import json
from pymongo import MongoClient
import pymongo

# mysql
# db = pymysql.connect("rm-bp119716lp2xc20oc.mysql.rds.aliyuncs.com","boka_app","iktorHib","message" )
# db
# cursor = db.cursor()
# 生产
# conn = pymongo.MongoClient('dds-bp14f1e7fc742bc42.mongodb.rds.aliyuncs.com', username="boka_app", password="v5OD8uWP",authSource="s3connect", port=3717, authMechanism='SCRAM-SHA-1')
conn = MongoClient('mongodb://root:20200812SHboka@dds-bp19d6d96b0be314-pub.mongodb.rds.aliyuncs.com', 3717)
db = conn.order
paymentConfig = db.pay_strategy_data

if __name__ == "__main__":
    for i in paymentConfig.find({"custId":"SHBOKA001"}):
        print(i)
