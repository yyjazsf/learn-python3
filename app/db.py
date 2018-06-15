import logging
import asyncio
import pymysql.cursors

info = logging.info

__pool = None


def create_pool():
    info('create db pool')
    global __pool
    __pool = pymysql.connect(
        host='localhost',
        user='root',
        db='blog',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    return __pool


def query(sql, args=(), size=None):
    info('query sql:', sql, args)
    global __pool
    try:
        with __pool.cursor() as cursor:
            # Read a single record
            cursor.execute(sql.replace('?', '%s'), args)
            if size != None:
                result = cursor.fetchmany(size)
            else:
                result = cursor.fetchone()
            return result
    finally:
        __pool.close()


def execute(sql, args=()):
    info('execute sql:', sql, args)
    global __pool
    try:
        with __pool.cursor() as cursor:
            # Create a new record
            cursor.execute(sql.replace('?', '%s'), args)

            # connection is not autocommit by default. So you must commit to save
            # your changes.
            __pool.commit()
    finally:
        __pool.close()
