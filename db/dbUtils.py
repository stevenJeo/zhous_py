__author__ = 'zhouzhishuai'
import pymysql

from config.DBConfig import *

# DB init
connect = pymysql.connect(**third_platform_ordes_test)
# connect = pymysql.connect(**ebayDB_config)
cur = connect.cursor()


# 查询操作
def select_sql(str):
	cur.execute(str)
	print("查询结果：%d" % cur.rowcount)
	return cur._rows

# 插入、更新、删除操作
def update_sql(str):
	try:
		row = cur.execute(str)
		connect.commit()
		print("commit ! rowsAffected:%d", row)
	except:
		connect.rollback()
		print("rollback !")
	finally:
		connect.close()
		print("close DB connection ...")
	return



# for i in cur:
# 	print("order_id:%s" % i)
# cur.close()
# connect.close()

