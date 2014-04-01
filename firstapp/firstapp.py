import sys, json, pprint, argparse

from flask import Flask,make_response, render_template, jsonify, send_from_directory
from flask.ext.sqlalchemy import SQLAlchemy
from birdy.twitter import AppClient

from twitter import get_twitter_mentions
from models import Base, Source, Mention

app = Flask (__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite+pysqlite:///sqlite.db'
db=SQLAlchemy(app)


@app.route('/')
def index():
    """Return the main view for mentions."""
    return render_template('index.html')

@app.route('/update/<source>', methods=['POST'])
def get_updates_for_source(source):
    """Return the number of updates found after getting new data from *source*"""
    if source == 'twitter':
        updates = get_twitter_mentions()
        return jsonify({'updates':updates})

@app.route('/read/<id>', methods=['POST'])
def read(id):
    """Mark a particular mention as read."""
    session=db.session()
    mention= session.query(Mention).get(id)
    mention.seen = True
    session.add(mention)
    session.commit()
    return jsonify({'success':True})

@app.route('/mentions')
def show_mentions():
    """Return a list of all mentions in JSON."""
    session=db.session()
    mentions=session.query(Mention).all()
    values=[mention.to_json() for mention in mentions]
    response = make_response()
    response.data = json.dumps(values)
    return response

def main():
    """Main entry point for script."""
    app.run(debug=True)

if __name__ == '__main__':
    sys.exit(main())


