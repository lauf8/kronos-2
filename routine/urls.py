from django.urls import path

from routine.views import RoutineView, next

app_name = "routineapp"


urlpatterns = [
    path("<int:routine>", RoutineView.as_view(), name="routine"),
    path('next/<int:event_id>/<int:days>', next, name='next_routine'),

   
]
