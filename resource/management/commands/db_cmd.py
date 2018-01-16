#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by zhou on 2018/1/16


from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = '业务相关的数据库操作'
    dbs = ['resource', 'sso', ]

    def add_arguments(self, parser):
        parser.add_argument(
            '--build',
            action='store_true',
            # dest='build',
            help='初始化数据库',
        )
        parser.add_argument(
            '--rebuild',
            action='store_true',
            # dest='rebuild',
            help='重新初始化数据库',
        )
        parser.add_argument(
            '--fake-data',
            action='store_true',
            # dest='rebuild',
            help='生成虚假数据填充表',  # todo 待完成
        )

    def handle(self, *args, **options):
        if options['build']:
            print('开始创建数据库和表')
            self.init_db()
        if options['rebuild']:
            print('开始删除数据库')
            import MySQLdb as db
            connection = db.connect(host="localhost", user="root", passwd="root", db='resource')
            drop_dbs = '\n'.join(["drop database IF EXISTS {};".format(db_name) for db_name in self.dbs])
            create_dbs = '\n'.join(["create database IF NOT EXISTS {};".format(db_name) for db_name in self.dbs])
            print(drop_dbs)
            print(create_dbs)
            with connection.cursor() as cursor:
                cursor.execute(drop_dbs)
                cursor.execute(create_dbs)
            print('已经删除数据库{}'.format(','.join(self.dbs)))
            self.init_db()

    @staticmethod
    def init_db():
        call_command('makemigrations', 'resource')
        call_command('migrate', database='resource')
        call_command('migrate', 'auth', database='sso')
        call_command('migrate', 'contenttypes', database='sso')
        call_command('migrate', 'sessions', database='sso')
        call_command('migrate', 'admin', database='sso')
