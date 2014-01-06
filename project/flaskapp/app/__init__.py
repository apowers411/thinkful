from flask import Flask
from flask.ext.mongoengine import MongoEngine
import twitter

app = Flask(__name__)


app.config["MONGODB_SETTINGS"] = {'DB': "color_my_world"}
app.config["SECRET_KEY"] = "KeepThisS3cr3t"

api = twitter.Api(consumer_key='ygHMdyqI5Rp5U8ocszeg',
                      consumer_secret='Z1inuYmTC53Fnf6Pv5KDlhhYB8iDXICDefjPwzLBQ',
                      access_token_key='545244617-28sr37n7IZTqrN6kIzUm9LH7YGNomPnYYEa3qhLy',
                      access_token_secret='xsSyHxp49KAnRusyjoE3TjP5otU08WlIajzkzOU')

db = MongoEngine(app)

def register_blueprints(app):
    from app.views import persons
    app.register_blueprint(persons)
register_blueprints(app)

if __name__ == '__main__':
    app.run(debug=True)