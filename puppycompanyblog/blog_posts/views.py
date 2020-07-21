from flask import render_template , url_for , flash , request , redirect , Blueprint
from flask_login import current_user , login_required
from puppycompanyblog import db
from puppycompanyblog.models import BlogPost
from puppycompanyblog.blog_posts.forms import BlogPostForm

# blog_postsブループリントを作成
# ここで作成した関数にはurl_for(blog_posts.関数)のリンクで飛ぶことができる
blog_posts = Blueprint('blog_posts',__name__)

# blog_postsブループリントをappに実装することで/createにアクセスするとここへリンクされる
# url_for(blog_posts.create_post)をすることでアクセスでき、リンクは/createになる。
@blog_posts.route('/create',methods=['GET','POST'])
# 認証したいページの場合に記述
@login_required
def create_post():
    
    # BlogPostFormを配置
    form = BlogPostForm()
    
    # submitボタンが押された場合
    if form.validate_on_submit():
        #form.title.dataのようにフォームに入力された値を取り出す
        # models.pyのBlogPostデータベースモデルのインスタンスを作成する
        blog_post = BlogPost(title=form.title.data,
                             text=form.text.data,
                             user_id=current_user.id)
        
        db.session.add(blog_post)
        db.session.commit()
        flash('Blog Post Created')
        # redirectは別のurlへ飛ばす
        # ここではcoreブループリントのindex関数へ飛ばす
        return redirect(url_for('core.index'))
    # create_post.htmlを表示する。BlogPostForm()のformインスタンスを渡して入力してもらう
    return render_template('create_post.html',form=form)



@blog_posts.route('/<int:blog_post_id>')
def blog_post(blog_post_id):
    # データベースにアクセスしてなかったら404を返す
    blog_post = BlogPost.query.get_or_404(blog_post_id)
    # データベースから帰ってきたblog_postのtitleなどを渡す
    return render_template('blog_post.html',
                           title=blog_post.title,
                           date=blog_post.date,
                           post=blog_post
                           )
    
    
    
@blog_posts.route('/<int:blog_post_id>/update',methods=['GET','POST'])
@login_required
def update(blog_post_id):
    # ない場合は404を返す
    blog_post = BlogPost.query.get_or_404(blog_post_id)
    
    # 更新する人が作成者かどうか
    # current_userはlogin_managerの属性、現在ログインしているユーザー名が入っている
    # blog_post.authorは投稿したpostの作成者
    if blog_post.author != current_user:
        abort(403)
        
    form = BlogPostForm()
    
    if form.validate_on_submit():
    
        blog_post.title = form.title.data
        blog_post.text = form.text.data
        db.session.commit()
        flash('Blog Post Updated')
        return redirect(url_for('blog_posts.blog_post',blog_post_id=blog_post.id))
    
    # updateしなかった場合
    # form.title.data = blog_post.titleフォームに現在の状態を表示する
    elif request.method == 'GET':
        form.title.data = blog_post.title
        form.text.data = blog_post.text
        
    return render_template('create_post.html',title='Updating',form=form)



@blog_posts.route('/<int:blog_post_id>/delete', methods=['GET', 'POST'])
@login_required
def delete_post(blog_post_id):
    # ない場合は404を返す
    blog_post = BlogPost.query.get_or_404(blog_post_id)

    # 更新する人が作成者かどうか
    if blog_post.author != current_user:
        abort(403)
    
    db.session.delete(blog_post)
    db.session.commit()
    flash('Blog Post Deleted')
    return redirect(url_for('core.index'))
    
