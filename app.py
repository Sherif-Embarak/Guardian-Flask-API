from flask import Flask, request,jsonify
from flask_pymongo import PyMongo
from pymongo import TEXT


app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://gardian:gardian@cluster0.ka0wm.mongodb.net/guardian?retryWrites=true&w=majority"
#app.config["MONGO_URI"] = "mongodb://localhost:27017/guardian"
mongo = PyMongo(app)
# list of collection fields
FIELDS = ['article_url', 'article_txt', 'article_title', 'article_writer', 'article_caption', 'article_time',
          'category', 'subcat_name', 'page_name']


@app.route('/')
def hello_world():
    return 'Hello World!\nPlease Use url/article to continue'


@app.route('/article', methods=['GET'])
def update_movie():
    # get request parameters 
    query = request.args.get('query', None)
    limit = int(request.args.get('limit', 10))
    return_list = request.args.get('return_list', '')
    # select db collection
    articles = mongo.db.articles_article
    # create return list
    params = dict()
    if return_list is '':
        for field in FIELDS:
            params[field] = 1
    else:
        for field in return_list.split(','):
            if field in FIELDS:
                params[field] = 1
            else:
                return 'dose not exist ' + str(field)
    params['_id'] = 0
    # add index and text search
    if query is not None:
        params['score'] = {'$meta': 'textScore'}
        articles.create_index([("$**", TEXT)], default_language='english')
        res = articles.find({"$text": {"$search": query}}, params)
        res.sort([('score', {'$meta': 'textScore'})]).limit(limit)
    else:
        res = articles.find({},params).limit(limit)
    # return json result
    return jsonify(list(res))


if __name__ == '__main__':
    app.run()
