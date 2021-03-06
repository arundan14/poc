from flask import render_template, flash, redirect
from flask import Flask, request, g
from config import Config
from forms import LoginForm
import sqlite3
import csv
import time,datetime
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

DATABASE = '/var/www/html/example/mvp.db'
#DATABASE2 = '/var/www/html/example/indiv_transactions.db'

class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_object(Config)

def connect_to_database():
    return sqlite3.connect(app.config['DATABASE'])


def get_db():
    db = getattr(g, 'db', None)
    if db is None:
        db = g.db = connect_to_database()
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()
#    db2 = getattr(g, 'db2', None)
#    if db2 is not None:
#        db2.close()

def execute_query(query, args=()):
    cur = get_db().execute(query, args)
    rows = cur.fetchall()
    cur.close()
    return rows


def get_new_item():
	return new_item
 
item = [
        {
            'owner': {'username': 'John'},
            'name': 'land',
	    'price': '200,000',
            'hash':'127e6fbfe24a750e72930c220a8e138275656b8e5d8f48a98c3c92df2caba935',
            'activity':'Uploaded land to vault',
            'timestamp':'Sun, 06 May 2018 14:49:27'
        },
        {
            'owner': {'username': 'John'},
            'name': 'music',
            'price': '50',
            'hash':'eb368a2dfd38b405f014118c7d9747fcc97f4f0ee75c05963cd9da6ee65ef498',
            'activity':'Uploaded music to vault',
            'timestamp':'Sun, 03 Jun 2018 14:49:27'
 
        },
        {
            'owner': {'username': 'John'},
            'name': 'car',
            'price': '20,000',
            'hash':'ac578a2dfd38f404f017908h7u9725ffo97f4f0ee05963c63cd9da6ee60a8e13',
            'activity':'Uploaded car to vault',
            'timestamp':'Sun, 03 Jun 2018 14:49:27'
 
        }
       ]
vault_item = [
        {
            'owner': {'username': 'John'},
            'name': 'land',
            'price': '200,000',
            'hash':'8762jjsys997sfjguyxnw986ss976252830ksystz234tsabg3452bjr234ft415',
            'activity':'Uploaded land to vault',
            'timestamp':'Sun, 06 May 2018 14:49:27'

        },
        {
            'owner': {'username': 'Jacob'},
            'name': 'music',
            'price': '50',
            'hash':'rtnch76420dhtjskfofys689203623nsys6s6s8f9g0sndif7654snj765snju40',
            'activity':'Uploaded music to vault',
            'timestamp':'Sun, 03 Jun 2018 14:49:27'

        },
        {
            'owner': {'username': 'Sarah'},
            'name': 'car',
            'price': '20,000',
            'hash':'hsyteb93629snhtdsnkf97349340djykskufdy0872bllbxytjs98625390ss653',
            'activity':'Uploaded car to vault',
            'timestamp':'Sun, 03 Jun 2018 14:49:27'

	},
	{
            'owner': {'username': 'Hailey'},
            'name': 'car',
            'price': '20,000',
            'hash':'br940a3egd384f50g76542idgwjuxgwm99736276428dsyxne762bksuxn872nm7',
            'activity':'Uploaded car to vault',
            'timestamp':'Sun, 03 Jun 2018 14:49:27'

        }
        ]
other_trans = []

def add_items(name):
    new_item = {}
    new_item=name
#    new_item['owner']={'username': 'John'}
    item.append(dict(new_tem))
    return item

def get_items():
	return item

def get_vault_items():
        return vault_item

def get_sellitems():
    item = [
        {
            'owner': {'username': 'John'},
            'name': 'land.txt',
	    'price': '200,000'
        },
	{
            'owner': {'username': 'John'},
            'name': 'music.txt',
	    'price': '50'
        },
	{
            'owner': {'username': 'Jane'},
            'name': 'car.txt',
	    'price': '20,000'
        }
       ]
    return item

#@app.route('/')
#
#def hello_world():
#  return 'Hello from Flask!'

@app.route('/poc')

def poc():
    user = {'username': 'John'}
    acctbal = 40
    return render_template('home.html', title='Home', user=user, acctbal=acctbal)

@app.route('/pocform',methods=['GET', 'POST'])

def hello():
    form = ReusableForm(request.form)
    posts = get_items()
    user = {'username': 'John'}
    print form.errors
    if request.method == 'POST':
        name=request.form['submit']
        print name
	if request.form['submit'] == 'Add_Item':
#	flash('Hello ' + name)
	 return redirect('/additems')
	else:
#	 flash('Hello ' + name)
	 return redirect('/handshake') 
#        if form.validate():
            # Save the comment here.
#         flash('Hello ' + name)
#	     flash('SOLD')
#        else:
#            flash('All the form fields are required. ')
 
    #return render_template('hello.html', form=form)
    return render_template('poc.html', title='Home', user=user, posts=posts, form=form)

@app.route('/handshake',methods=['GET', 'POST'])

def handshake():
    form = ReusableForm(request.form)

    user = {'username': 'John'}
    posts = get_items()
    name='Arun'
    print form.errors
    if request.method == 'POST':
#         name=request.form['submit']
#        print name
         return render_template('poc_handshake.html', name=name)

    #return render_template('hello.html', form=form)
    return render_template('jhandshake.html', title='Home', user=user, posts=posts, form=form)




@app.route('/marketplace',methods=['GET', 'POST'])

def marketplace():
    form = ReusableForm(request.form)

    user = {'username': 'John'}
    posts = get_vault_items()
    name='Arun'
    print form.errors
    if request.method == 'POST':
#         name=request.form['submit']
#        print name
         return render_template('poc_handshake.html', name=name)
#        return render_template('poc_handshake.html')
#        if form.validate():
            # Save the comment here.
#            flash('Hello ' + name)
#            flash('SOLD')
#        else:
#            flash('All the form fields are required. ')

    #return render_template('hello.html', form=form)
    return render_template('handshake.html', title='Home', user=user, posts=posts, form=form)


@app.route('/additems',methods=['GET', 'POST'])

def additems():
    form = ReusableForm(request.form)

    user = {'username': 'John'}
    posts = get_items()
    additem = {}
    now = datetime.datetime.now()
    print form.errors
    if request.method == 'POST':
        additem['name']=request.form['name']
	additem['owner']=user
	additem['price']=request.form['price']
	additem['hash']='724c06ab00bb151c13a45de268c22cb4f088d826dc260f062188h7u9725f5her'
	additem['activity']='added ' +request.form['name']+' to vault'
#	additem['timestamp']=now.strftime("%Y-%m-%d %H:%M")
#	newlist = add_items(additem)
	item.append(dict(additem))
#	john_trans.append(dict(addtrans))
        return redirect('/pocform')

    #return render_template('hello.html', form=form)
    return render_template('add_items.html', form=form)

@app.route('/sellhandshake/<object>/<hash>',methods=['GET', 'POST'])

def sellhandshake(object,hash):
    form = ReusableForm(request.form)

    user = {'username': 'John'}
    posts = get_items()
    name='Arun'
    for items in item:
	if items['hash'] == hash:
	  vault_item.append(dict(items))	
    print form.errors
#    if request.method == 'POST':
#         name=request.form['submit']
#        print name
    return render_template('list_handshake.html', name=object,hash=hash)
#        return render_template('poc_handshake.html')


@app.route('/buyhandshake/<object>',methods=['GET', 'POST'])

def buyhandshake(object):
    form = ReusableForm(request.form)
    user = {'username': 'Jane'}
    posts = get_items()
    name='Arun'
    print form.errors
    return render_template('poc_handshake.html', name=object)

@app.route('/buyvault/<object>',methods=['GET', 'POST'])

def buyvault(object):
    form = ReusableForm(request.form)
    user = {'username': 'Jane'}
    print form.errors
    posts = [
                {
                'owner':  {'username': 'Jane'},
                'name':  object
                }
                ]
    return render_template('newvault.html', name=object)


@app.route('/jtrans',methods=['GET', 'POST'])

def jtrans():
    form = ReusableForm(request.form)

    user = {'username': 'John'}
    posts = get_items()
    return render_template('jtrans.html', title='Transactions', user=user, posts=posts, form=form)

 
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


#@app.route('/pie')
#def pie():
#    return render_template('pie.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = ReusableForm(request.form)
    if request.method == 'POST':
	   username = request.form['username']
	   if username == 'John':
	     return redirect('/poc')
	   else:
	     return redirect('/marketplace')
#    form = LoginForm()
#    if form.validate_on_submit():
#        flash('Login requested for user {}, remember_me={}'.format(
#            form.username.data, form.remember_me.data))
#        return redirect('/poc')
    return render_template('login.html', title='Sign In', form=form)

#@app.route('/viewdb')

#def hello_world2():
#  rows = execute_query("""SELECT * FROM natlpark""")
#  return '<br>'.join(str(row) for row in rows)

#@app.route("/state/<state>")
#def sortby(state):
#    rows = execute_query("""SELECT * FROM natlpark WHERE state = ?""",
#                         [state.title()])
#    return '<br>'.join(str(row) for row in rows)

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
    cur = get_db().cursor()
    username='arundan14'
    result = execute_query(
        """SELECT *
           FROM mvp_vault WHERE user_id = ? ORDER BY item_id desc""",  #WHERE user_id = ? """, #[username] 
	(username,)
    )
    str_rows = [dict(acc_no=row[0], trans_date=row[1], description=row[2], amount=row[3]) for row in result]
    cur.close()
  #  header = 'Account Number,Date,Description,Amount<br/>'
  #  return header + '<br/>'.join(str_rows)
    return render_template('trans.html', str_rows=str_rows)

def validate_user(username):
	count = 0
	cur = get_db().cursor()
#	cur = get_db().execute("SELECT user_id FROM mvp_users WHERE user_id=?", (username,))
	result = execute_query("""SELECT user_id FROM mvp_users WHERE user_id = ? """, (username,))
	print result
	print "Hello World"
#	rows = cur.fetchall()
    	return result

@app.route('/loginnew', methods=['GET', 'POST'])
def loginnew():
    form = ReusableForm(request.form)
    if request.method == 'POST':
           username = request.form['username']
	   result = validate_user(username)
           if result:
	     return redirect('/poc')
             #return redirect('/poc', username=username)
	     #return redirect(url_for('poc', username=username))
           else:
             return redirect('/marketplace')
#	   return render_template('display.html', title='Home', user=username, result=result)
#    form = LoginForm()
#    if form.validate_on_submit():
#        flash('Login requested for user {}, remember_me={}'.format(
#            form.username.data, form.remember_me.data))
#        return redirect('/poc')
    return render_template('login.html', title='Sign In', form=form)

@app.route('/vault/<user>',methods=['GET', 'POST'])
def vaulthome(user):
    form = ReusableForm(request.form)
    username = user
    cur = get_db().cursor()
#    posts = get_items()
    result = execute_query(
        """SELECT item_name, item_catg, Item_ID
           FROM mvp_vault WHERE user_id = ? ORDER BY item_id desc""",  
        (username,)
    ) 
    posts = [dict(item_name=row[0], item_catg=row[1], item_id=row[2]) for row in result]
    cur.close()
    print form.errors
    if request.method == 'POST':
        name=request.form['submit']
        print name
        if request.form['submit'] == 'Add_Item':
#       flash('Hello ' + name)
         return redirect('/additems')
        else:
#        flash('Hello ' + name)
         return redirect('/handshake')
#        if form.validate():
            # Save the comment here.
#         flash('Hello ' + name)
#            flash('SOLD')
#        else:
#            flash('All the form fields are required. ')

    #return render_template('hello.html', form=form)
    return render_template('poc.html', title='Home', user=user, posts=posts, form=form)

if __name__ == '__main__':
  app.run()
