from flask import Flask,render_template
from .views.category import ind
from .views.login import auth
from DBp1part3.views.test2 import testblue2
from . import sql
from .views import post


DATA_dict = {
    '1':{'name': 'hanfu', 'age':25},
    '2':{'name': 'hanfu', 'age':52}
}

def create_app():
    app = Flask(__name__, static_folder='static')
    app.secret_key='hanfushi'

    @app.route('/index')
    def index():
        # rows = sql.fetchall('Items_Posted')
        db = sql.get_db()
        cur = db.cursor()
        cur.execute(
            "SELECT i.title, i.price,i.neededitem,i.item_id,p.image_source FROM Items_Posted i, Photos p WHERE i.item_id = p.item_id ORDER BY i.posted_at DESC"
        )
        rows = cur.fetchall()
        print(rows[0])
        return render_template('webpage/index.html', rows=rows)


    app.register_blueprint(auth)
    app.register_blueprint(testblue2)
    app.register_blueprint(post.bp)
    app.register_blueprint(ind)
    app.add_url_rule('/', endpoint='index')
    # app.register_blueprint(testblue, url_prefix ='/web')
    # app.register_blueprint(testblue2, url_prefix ='/admin')
    return app