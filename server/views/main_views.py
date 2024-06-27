'''Main views'''

from flask import (
    Blueprint,
    render_template,
)
from server.forms import FileUploadForm

bp = Blueprint('main', __name__, url_prefix='/') # main으로 오면 앞에 '/' 붙임

@bp.route('/') # home으로 접속했을 때
def index():
    '''메인 페이지'''
    form = FileUploadForm()
    return render_template(
        'main.html',
        form=form,
    )
    # return 'Hello ACIN academy' # main에 접속했을 때 -> 원래는 html 반환해야하는데 문자열만 반환하면 알아서 만들어서 보내줌(빈 html에 저 문자열만 넣어서 보냄)