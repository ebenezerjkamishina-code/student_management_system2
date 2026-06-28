from django.urls import path
from . import views



urlpatterns = [   
path('add/', views.register_student, name='student_list'), 
path ('add/', views.register_student,name='register'), # this is the register page
path('', views.home, name='home'),
path('courses/', views.courses, name='courses'),
path('results/', views.results_page, name='results'),
path('past-papers/', views.past_papers_page, name='past_papers'),
path('resources/', views.resources_page, name='resources'),
path('elearning/', views.elearning_page, name='elearning'),
path('assignments/', views.assignments_page, name='assignments'),
]

   


#'' is the homepage so if someone opens homepage he will be directed to the home view.