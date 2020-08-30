from django.conf.urls import url

from . import views

urlpatterns = [
  url(r'^$', views.index, name='index'),

  #/lycee/cursus/
  url(r'^(?P<cursus_id>[0-9]+)$', views.detail_cursus, name='detail_cursus'),

  #/lycee/cursuscall/
  url(r'^cursuscall/(?P<cursus_id>[0-9]+)$', views.call_cursus, name='call_cursus'),

  #/lycee/student/73
  url(r'^student/(?P<student_id>[0-9]+)$', views.detail_student, name='detail_student'),

  #/lycee/student/create/
  url(r'^student/create/$', views.StudentCreateView.as_view(), name='create_student'),

  #/lycee/call/
  url(r'^call/$', views.AbsenceCreateView.as_view(), name='update_absence'),

  #/lycee/cursuscall/
  #url(r'^cursuscall/(?P<cursus_id>[0-9]+)$',views.AppelCreateView.as_view(), name='call_cursus'),

  #/lycee/cursuspresences/
  url(r'^cursuspresences/$', views.presences_cursus, name='presences_cursus'),

  #/lycee/cursuspresences/
  url(r'^cursuspresences/(?P<cursus_id>[0-9]+)$', views.presences_cursus_specifique, name='presences_cursus_specifique'),

   #/lycee/cursuspresences/student/
  url(r'^cursuspresences/student/(?P<student_id>[0-9]+)$', views.presences_student, name='presences_student'),
]