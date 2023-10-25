from django.urls import path

from routine.views import RoutineView, next, create_routine, list_routine, clone

app_name = "routineapp"


urlpatterns = [
    path('<int:routine>', RoutineView.as_view(), name='routine'),
    path('next/<int:event_id>/<int:days>', next, name='next_routine'),
    path('', list_routine, name='list_routine'),
    path('create', create_routine, name='create_routine'),
    path('clone/<int:pk>', clone, name='clone')
]
