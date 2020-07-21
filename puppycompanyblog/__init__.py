# このファイルで各コンポーネントのblueprintをappに実装させる
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# このappをapp.pyがインポートして使用する
# app.pyは実行するだけでappの設定は全てこのファイルで行う
app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecret'

# このファイルが存在するディレクトリをさす
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir , 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# dbを全体でインポートする
db = SQLAlchemy(app)
Migrate(app , db)

# 今誰かログインしてるかなどの情報をもつオブジェクト
login_manager = LoginManager()

login_manager.init_app(app)
# login_viewのrouteを設定
# users blueprintのlogin関数
login_manager.login_view = 'users.login'



# blueprintオブジェクトをインポート
from puppycompanyblog.core.views import core
from puppycompanyblog.users.views import users
from puppycompanyblog.blog_posts.views import blog_posts
from puppycompanyblog.error_pages.handlers import error_pages

# 実装
# ここで各機能を一気にappに乗せるイメージ
app.register_blueprint(core)
app.register_blueprint(users)
app.register_blueprint(blog_posts)
app.register_blueprint(error_pages)
