# -*- coding: utf-8 -*
import web
from config import db
import datetime
 

# 获取所有心情
def get_posts():
	return db.select('moods',order='id DESC')

# 详细心情
def get_post(id):
	try:
		return db.select('moods',where='id=$id',vars=locals())[0]
	except IndexError:
		return noen

# 增加心情
def new_post(content):
	db.insert('moods',content=content,posted_on=datetime.datetime.utcnow())

# 删除心情
def del_post(id):
	db.delete('moods',where='id=$id',vars=locals())


