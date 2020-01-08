from . import views
from django.urls import path


app_name = 'result'
urlpatterns = [
    path('', views.add_subject_score, name='add_scores' ),
    path('check_result', views.student_result, name="display_result")

]
