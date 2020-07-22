# puppycompanyblogディレクトリの__init__.pyファイルで作成したappインスタンスをインポートする
from puppycompanyblog import app
from puppycompanyblog.models import db

db.create_all()

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
