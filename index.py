# -*- coding: utf-8 -*
import os
import web
import model
import json
from config import env
from datetime import date, datetime
import jinja2
from jinja2 import Environment

urls = (
	'/','Index',
	'/add','AddMood',
    '/view', 'ViewMood' 
)

# env.globals['title'] = lambda:p_globals['title']
app = web.application(urls, globals())
# render = web.template.render('templates',base='layout',globals=p_globals)
# # http://www.felix021.com/blog/read.php?2121;http://www.zhihu.com/question/19629981
# p_globals['render'] = render

class Index:        
    def GET(self):
    	posts = model.get_posts()
    	template = env.get_template('index.html')
    	return template.render(moods=posts)

class AddMood:
	def GET(self):
		mood_data = web.input()
		template = env.get_template('add.html')
		return template.render(mood_data)
	def POST(self):
		mood_data = web.input()
		model.new_post(mood_data.mood_content)
		raise web.seeother('/')

class ViewMood:
	def GET(self):
		web.header('Content-type','application/json')
		id = web.input(_method='get').postId
		post = model.get_post(int(id))
		return json.dumps(post,cls=CJsonEncoder)

# 扩展JSONEncoder用来格式化时间
class CJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)
 

if __name__ == '__main__':
	app.run()