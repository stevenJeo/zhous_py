__author__ = 'zhouzhishuai'


from db.dbUtils import *

str1 = "SELECT * FROM ebay_in_orders_queue"

orders = select_sql(str1)

for i in orders:
	print("order_id:%s, order_status:%s, create_time:%s, paid_time:%s, execute_status:%s, execute_count:%d, insert_time:%s"
	      % (i[1], i[2], i[9], i[11], i[17], i[18], i[20]))
