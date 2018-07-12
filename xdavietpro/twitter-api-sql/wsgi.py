# wsgi.py
try:
    from dotenv import load_dotenv
    load_dotenv()
except:
    pass # Heroku does not use .env

import os
import logging
logging.warn(os.environ["DATABASE_URL"])


from app import create_app
from config import Config
application = create_app()
application.config.from_object(Config)

from flask import request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
db = SQLAlchemy(application)
ma = Marshmallow(application)

from models import Tweet
from schemas import tweets_schema, tweet_schema

from datetime import datetime

@application.route('/api/v1/tweets/', methods=['GET'])
def tweets():
    #import ipdb; ipdb.set_trace()
    tweets = db.session.query(Tweet).all() # SQLAlchemy request => 'SELECT * FROM tweets'
    return tweets_schema.jsonify(tweets)

@application.route('/api/v1/tweets/<int:id>', methods=['GET'])
def tweet(id):
    #import ipdb; ipdb.set_trace()
    tweet = db.session.query(Tweet).get(id)
    return tweet_schema.jsonify(tweet)

@application.route('/api/v1/tweets/', methods=['POST'])
def create_tweet():
    #import ipdb; ipdb.set_trace()
    tweet = Tweet()
    tweet.text = request.json['text']
    tweet.created_at=datetime.now().time()
    db.session.add(tweet)
    db.session.commit()
    return tweet_schema.jsonify(tweet), 201

@application.route('/api/v1/tweets/<int:id>', methods=['DELETE'])
def delete_tweet(id):
    #import ipdb; ipdb.set_trace()
    tweet = db.session.query(Tweet).get(id)
    db.session.delete(tweet)
    db.session.commit()
    return tweet_schema.jsonify(tweet), 204

@application.route('/api/v1/tweets/<int:id>', methods=["PUT"])
def update_tweet(id):
    tweet = db.session.query(Tweet).get(id)
    tweet.text = request.json['text']
    db.session.commit()
    return tweet_schema.jsonify(tweet), 204
