#from django.http import HttpResponse
#from django.template import loader
#from .models import Cursus

#def detail(request, cursus_id):
#  resp = "result for cursus {}".format(cursus_id)
#  return HttpResponse(resp)

# Create your views here.
#def index(request):
#  result_list = Cursus.objects.order_by('name')
  #chargement template
#  template = loader.get_template('lycee/index.html')
  #context
#  context = {
#    'liste': result_list,
#  }
#  return HttpResponse(template.render(context, request))

from django.views.generic import TemplateView, ListView, CreateView
from django.urls import reverse
from django.http import HttpResponse
from django.shortcuts import render
from .models import Cursus
from .models import Student
from .models import Presence
from .forms import StudentForm
from .forms import PresenceForm
from .forms import AppelForm

# Create your views here.

def index(request):
  result_list = Cursus.objects.order_by('name')
  #context
  context = {
    'liste': result_list,
  }
  return render(request, 'lycee/index.html', context)

def detail_cursus(request, cursus_id):
  result_cursus = Cursus.objects.get(pk=cursus_id)
  result_list = Student.objects.order_by('last_name')
  #context
  context = {'cursus':result_cursus,'liste': result_list}
  return render (request, 'lycee/cursus/detail_cursus.html', context)
  #resp = "result for cursus {}".format(cursus_id)
  #return HttpResponse(resp)

def call_cursus(request, cursus_id):
  result_cursus = Cursus.objects.get(pk=cursus_id)
  result_list = Student.objects.order_by('last_name')
  #context
  context = {'cursus':result_cursus,'liste': result_list}
  return render (request, 'lycee/cursus/call_cursus.html', context)

def detail_student(request, student_id):
  result_list = Student.objects.get(pk=student_id)
  #context
  context = {'liste': result_list,}
  return render (request, 'lycee/student/detail_student.html', context)

def presences_cursus(request):
  result_list = Cursus.objects.order_by('name')
  result_listeStudent = Student.objects.order_by('last_name')
  result_listePresence = Presence.objects.order_by('student')
  #context
  context = {
    'liste': result_list,
    'listeStudent': result_listeStudent,
    'listePresences': result_listePresence,
  }
  return render(request, 'lycee/cursus/presences_cursus.html', context)

def presences_cursus_specifique(request, cursus_id):
  result_list = []
  result_list.append(Cursus.objects.get(pk=cursus_id))
  result_listeStudent = Student.objects.order_by('last_name')
  result_listePresence = Presence.objects.order_by('student')
  #context
  context = {
    'liste':result_list,
    'listeStudent': result_listeStudent,
    'listePresences': result_listePresence,
  }
  return render(request, 'lycee/cursus/presences_cursus.html', context)

def presences_student(request, student_id):
  result_student = Student.objects.get(pk=student_id)
  result_listePresence = Presence.objects.order_by('student')

  totalAbsences = 0
  for i in result_listePresence :
    if i.student == result_student:
      totalAbsences = totalAbsences + 1
  #context
  context = {
    'student':result_student,
    'listePresences': result_listePresence,
    'totalAbsences' : totalAbsences,
  }
  return render(request, 'lycee/student/presences_student.html', context)

class StudentCreateView(CreateView):
  #le modele auquel se refere cette ValueErrormodel
  model = Student
  #le formulaire associe dans (forms.py)
  form_class = StudentForm
  #le nom du template
  template_name = "lycee/student/create.html"

  #page appelee si creation ok
  def get_success_url(self):
    return reverse ("detail_student", args=(self.object.pk,))

class AbsenceCreateView(CreateView):
  #le modele auquel se refere cette ValueErrormodel
  model = Presence
  #le formulaire associe dans (forms.py)
  form_class = PresenceForm
  #le nom du template
  template_name = "lycee/absence.html"

  #page appelee si creation ok
  def get_success_url(self):
    return reverse ("index")

#For create a new Bourse
class AppelCreateView(CreateView):
    model = Presence

    form_class = AppelForm

    #le nom du template
    template_name = "lycee/cursus/call_cursus.html"

    def call_cursus(request, cursus_id):
      result_cursus = Cursus.objects.get(pk=cursus_id)
      result_list = Student.objects.order_by('last_name')
      #context
      context = {'cursus':result_cursus,'liste': result_list}
      return render (request, 'lycee/cursus/call_cursus.html', context)

    #page appelee si creation ok
    def get_success_url(self):
      return reverse ("index")