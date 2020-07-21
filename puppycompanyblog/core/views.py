from flask import render_template , request , Blueprint
from puppycompanyblog.models import BlogPost

# 'core'という名前でBlurprintを作成しcoreオブジェクトに入れる
core = Blueprint('core' , __name__)

# url_for('core.index') blueprint.関数名
@core.route('/')
def index():
    page = request.args.get('page',type=int)
    # 時間の降順で５件取ってくる
    blog_posts = BlogPost.query.order_by(BlogPost.date.desc()).paginate(page=page,per_page=5)
    return render_template('index.html',blog_posts=blog_posts)

# url_for('core.info')
@core.route('/info')
def info():
    return render_template('info.html')