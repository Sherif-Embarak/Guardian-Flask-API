from flask import Flask, request,jsonify
from flask_pymongo import PyMongo
from pymongo import TEXT
from database import LOCAL_DB,ATLAS_DB,FIELDS


app = Flask(__name__)
app.config["MONGO_URI"] = ATLAS_DB
#app.config["MONGO_URI"] = LOCAL_DB
mongo = PyMongo(app)

def return_list(return_str):
    params = dict()
    #remove _id field
    params['_id'] = 0
    #select return fields
    if return_str is '':
        for field in FIELDS:
            params[field] = 1
    else:
        for field in return_str.split(','):
            if field in FIELDS:
                params[field] = 1
            else:
                return field
    return params


@app.route('/article', methods=['GET'])
def get_articles():
    # get request parameters 
    query = request.args.get('query', None)
    limit = int(request.args.get('limit', 10))
    return_str = request.args.get('return_list', '')
    # select db collection
    articles = mongo.db.articles_article
    # create return list
    params = return_list(return_str)
    if not isinstance(params, dict):
        return params + " is not found" 
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
