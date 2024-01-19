from datetime import datetime
from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
from app_coder.models import Course

def template_using_context(
        self, name: str = 'Name', last_name: str = 'Last_name'):
    miHtml = open("/home/carlos/Escritorio/Proyecto/Django/Clase djago2/classdj2/classdj2/templates/templates.html")
    template = Template(miHtml.read())
    miHtml.close()

    context_dict = {
        'name': name,
        'last_name': last_name,
        'now': datetime.now(),
        'class_grades':[4, 2, 8, 7, 3]
    }

    my_context = Context(context_dict)
    render = template.render(my_context)
    return HttpResponse(render)

def new_course(
        self, name: str = 'course', code: int = 0):
    
    template = loader.get_template('templates_course.html')

    course = Course(name=name, code=code)
    course.save()

    context_dict = {
        'course': course,
    }

    render = template.render(context_dict)
    return HttpResponse(render)