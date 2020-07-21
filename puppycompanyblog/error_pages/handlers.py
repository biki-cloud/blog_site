from flask import Blueprint , render_template

error_pages = Blueprint('error_pages' , __name__)

# 404エラーが起きた場合
@error_pages.app_errorhandler(404)
def error_404(error):
    return render_template('error_pages/404.html') , 404

# 403エラーが起きた場合
@error_pages.app_errorhandler(403)
def error_403(error):
    return render_template('error_pages/403.html'), 404
