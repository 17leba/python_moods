# -*- coding: utf-8 -*
import os
import sys
import web
from web import ctx
import MySQLdb
import jinja2

# 数据库配置
dbname = 'test'
user = 'root'
pw = 'root'

db = web.database(
	dbn='mysql',
	db=dbname,
    user=user,
    pw=pw
 )

if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')

# 模板配置
env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates'))
)
# 全局变量
tpl_gloabls = {
	'title':'心情发布系统0.1',
	'P_HTTP':web.ctx
}
env.globals.update(tpl_gloabls)
