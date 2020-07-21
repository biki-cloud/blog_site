# puppycompanyblogディレクトリの__init__.pyファイルで作成したappインスタンスをインポートする
from puppycompanyblog import app

if __name__ == '__main__':
    app.run(debug=True)
