from flask import Flask
from flask import render_template
app=Flask(__name__)

@app.route("/")
def index(name=None):
    return render_template('index.html',name=name)

@app.route("/newyork/")
def here(name=None):
    return render_template('place.html',name="New York, New York")

@app.route("/benin/")
def there(name=None):
    return render_template('place.html',name="Ouidah, Benin")


if __name__ == "__main__":
    app.debug = True
    app.run()