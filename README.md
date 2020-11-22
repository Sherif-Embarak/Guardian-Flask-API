# Guardian-Flask-API
Guardian search api
### Guardian-API Installation
##### 1- download the repo
##### 2- download and install  python3.6
##### 3- open cmd and cd to "/path/to/downloaded/repo/"
###### example: cd C:\Users\<user>\OneDrive\Documents\Guardian-API
##### 4- virtualenv -p "/path/to/installed/python.exe"  venv
###### example: virtualenv -p "C:\Users\<user>\AppData\Local\Programs\Python\Python36\python.exe"  venv
##### 5- cd /venv/scripts
##### 6- activate
##### 7- cd to "/path/to/downloaded/repo/"
##### 8- pip install -r requirements.txt
##### 8- python app.py
### Guardian-API Usage:
##### http://127.0.0.1:5000/article?query=(word_to_search)&return_list='list_of_fields_to_return(separate_by_comma)'&limit=<int>(maximum_number_of_returned_objects_by_defult_10)
###### example: http://127.0.0.1:5000/article?query=accept&return_list=article_txt,article_write&limit=3
###### fields: 'article_url', 'article_txt', 'article_title', 'article_writer', 'article_caption', 'article_time','category', 'subcat_name', 'page_name'