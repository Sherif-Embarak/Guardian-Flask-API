from flask import Flask, request
from bson.json_util import dumps
from flask_pymongo import PyMongo
from pymongo import TEXT

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/guardian"
mongo = PyMongo(app)
VALUES = ['article_url', 'article_txt', 'article_title', 'article_writer', 'article_caption', 'article_time',
          'category', 'subcat_name', 'page_name']


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/article', methods=['GET'])
def update_movie():
    query = request.args.get('query', None)
    limit = int(request.args.get('limit', 10))
    return_list = request.args.get('return_list', '')
    articles = mongo.db.articles_article
    # articles.drop_index('$**_text')
    articles.create_index([("$**", TEXT)], default_language='english')
    # create return list
    params = dict()
    if return_list is '':
        for item in VALUES:
            params[item] = 1
    else:
        for item in return_list.split(','):
            if item in VALUES:
                params[item] = 1
            else:
                return 'dose not exist ' + str(item)
    params['score'] = {'$meta': 'textScore'}
    res = articles.find({"$text": {"$search": query}}, params)
    res.sort([('score', {'$meta': 'textScore'})]).limit(limit)
    return dumps(list(res))


if __name__ == '__main__':
    app.run()
