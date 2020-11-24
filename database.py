# connection URLs
ATLAS_DB = "mongodb+srv://gardian:gardian@cluster0.ka0wm.mongodb.net/guardian?retryWrites=true&w=majority"
LOCAL_DB = "mongodb://localhost:27017/guardian"
# list of collection fields
FIELDS = [
    'article_url',
    'article_txt',
    'article_title',
    'article_writer',
    'article_caption',
    'article_time',
    'category',
     'subcat_name',
      'page_name']