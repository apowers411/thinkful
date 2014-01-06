from flask import Blueprint, request, redirect, render_template, url_for
from flask.views import MethodView
from app.models import Person, Tag
from flask.ext.mongoengine.wtf import model_form
import pymongo

persons = Blueprint('persons', __name__, template_folder='templates')

class ListView(MethodView):

    def get(self):
        persons = Person.objects.all()
        return render_template('persons/list.html', persons=persons)


class DetailView(MethodView):

    form = model_form(Tag, exclude = ['created_at'])

    def get_context(self,name):
        person = Person.objects.get_or_404(name=name)
        form = self.form (request.form)

        context = {
            "person": person,
            "form": form
        }
        return context

    def get(self, name):
        context = self.get_context(name)
        return render_template('persons/detail.html', **context)

    def post(self,name):
        context = self.get_context(name)
        form = context.get('form')

        if form.validate():
            tag = Tag()
            form.populate_obj(tag)

            person = context.get('person')
            person.tags.append(tag)
            person.save()

            return redirect(url_for('persons.detail',name=name))
        return render_template('person/detail.html', **context)
# Register the urls
persons.add_url_rule('/', view_func=ListView.as_view('list'))
persons.add_url_rule('/<name>/', view_func=DetailView.as_view('detail'))