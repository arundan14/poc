from flask import render_template, flash, redirect
from flask import Flask, request, g
from config import Config
from forms import LoginForm
import sqlite3
import csv
import time

DATABASE = '/var/www/html/example/bart.db'
DATABASE2 = '/var/www/html/example/indiv_transactions.db'

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_object(Config)

def connect_to_database():
    return sqlite3.connect(app.config['DATABASE'])

def connect_to_database2():
    return sqlite3.connect(app.config['DATABASE2'])

def get_db():
    db = getattr(g, 'db', None)
    if db is None:
        db = g.db = connect_to_database()
    return db

def get_db2():
    db2 = getattr(g, 'db2', None)
    if db2 is None:
        db2 = g.db2 = connect_to_database2()
    return db2


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()
    db2 = getattr(g, 'db2', None)
    if db2 is not None:
        db2.close()

def execute_query(query, args=()):
    cur = get_db().execute(query, args)
    rows = cur.fetchall()
    cur.close()
    return rows

def execute_query2(query, args=()):
    cur = get_db2().execute(query, args)
    rows = cur.fetchall()
    cur.close()
    return rows


#@app.route('/')
#
#def hello_world():
#  return 'Hello from Flask!'
 
@app.route('/index')

def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/graph')
def graph():
    return render_template('graph.html')


@app.route('/pie')
def pie():
    return render_template('pie.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)

@app.route('/viewdb')

def hello_world2():
  rows = execute_query("""SELECT * FROM natlpark""")
  return '<br>'.join(str(row) for row in rows)

@app.route("/state/<state>")
def sortby(state):
    rows = execute_query("""SELECT * FROM natlpark WHERE state = ?""",
                         [state.title()])
    return '<br>'.join(str(row) for row in rows)

@app.route('/')
def print_data():
    """Respond to a query of the format:
    myapp/?dest=Fremont&time=600&station=plza&day=0
    with ETD data for the time and location specified in the query"""
    start_time = time.time()
    cur = get_db().cursor()
    try:
        minute_of_day = int(request.args.get('time'))
    except ValueError:
        return "Time must be an integer"
    station = request.args.get('station')
    print minute_of_day
    day = request.args.get('day')
    dest = request.args.get('dest')
    result = execute_query(
        """SELECT etd, count(*)
           FROM etd
           WHERE dest = ? AND minute_of_day = ?
                 AND station = ? AND day_of_week = ?
           GROUP BY etd""",
        (dest, minute_of_day, station, day)
    )
    str_rows = [','.join(map(str, row)) for row in result]
    query_time = time.time() - start_time
    #logging.info("executed query in %s" % query_time)
    cur.close()
    header = 'etd,count\n'
    return header + '\n'.join(str_rows)

@app.route('/trans')
def print_trans():
    start_time = time.time()
    cur = get_db2().cursor()
    result = execute_query2(
        """SELECT ac_no, trans_date, description, amount
           FROM indiv_transactions"""
    )
    #str_rows = [','.join(map(str, row)) for row in result]
    str_rows = [dict(acc_no=row[0], trans_date=row[1], description=row[2], amount=row[3]) for row in result]
    #str_rows = 'Hello from bart!'
    query_time = time.time() - start_time
    #logging.info("executed query in %s" % query_time)
    cur.close()
  #  header = 'Account Number,Date,Description,Amount<br/>'
  #  return header + '<br/>'.join(str_rows)
    return render_template('trans.html', str_rows=str_rows)


if __name__ == '__main__':
  app.run()
