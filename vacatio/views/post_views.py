from flask import Blueprint
from flask import render_template
from flask import request
from flask import url_for

from vacatio.models import db
from vacatio.models import Post
from vacatio.forms import PostForm

from datetime import datetime
from werkzeug.utils import redirect


bp = Blueprint('post', __name__, url_prefix='/post')


@bp.route('/list/')
def _list():
    l_post = Post.query.order_by(Post.create_date.desc())
    return render_template('post/list.html', post_list=l_post)


@bp.route('/add/', methods=('GET', 'POST'))
def add():
    form = PostForm()
    if request.method == 'POST' and form.validate_on_submit():
        post = Post(
                subject=form.subject.data,
                content=form.content.data,
                create_date=datetime.now(),
                start_date=form.start_date.data,
                end_date=form.end_date.data,
                status=1,
                approver=form.approver.data,
                account_id=1,
                )
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('post._list'))
    return render_template('post/add_form.html', form=form)


@bp.route('/detail/<int:post_id>/')
def detail(post_id):
    i_post = Post.query.get_or_404(post_id)
    return render_template('post/detail.html', post=i_post)
