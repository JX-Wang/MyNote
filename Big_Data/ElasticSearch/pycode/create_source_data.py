#! encoding utf-8
"""
  Create Large Data
=====================
Author@Wangjunxiong
Date@2019/11/01
"""

import pymysql
import random
import threading
from faker import Faker

COUNT = 0


class ES_create_source_data(object):
    def __init__(self):
        mysql_conf = {
            "host": "10.245.146.107",
            "user": "root",
            "passwd": "platform",
            "db": "ES",
            "charset": "utf8"
        }
        try:
            self.db = pymysql.connect(**mysql_conf)
            self.cursor = self.db.cursor()
        except Exception as e:
            print("Mysql connect error ", e)
        self.faker = Faker()

    def create_data(self):
        name = self.faker.name()
        age = random.randint(18, 110)
        gender = random.choice(['F', 'M'])
        height = random.randint(150, 190)
        ssn = self.faker.ssn()
        account = self.faker.ean13()
        passwd = self.faker.ean8()
        city = self.faker.city()
        country = self.faker.country()

        sql = """INSERT INTO ES_PersonalInfo (name, age, gender, height, ssn, account, passwd, city, country) VALUES 
        ('{name}', '{age}', '{gender}', '{height}', '{ssn}', '{account}', '{passwd}', '{city}', "{country}")""".format(
                            name=name, age=age, gender=gender, height=height, ssn=ssn,
                            account=account, passwd=passwd, city=city, country=country)
        print(sql)

        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as e:
            print(str(e))
            return


def create():
    while True:
        ES = ES_create_source_data()
        ES.create_data()


if __name__ == '__main__':
    ES = ES_create_source_data()
    count = 0
    for i in range(5):
        t = threading.Thread(target=create)
        t.start()











