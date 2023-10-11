from django.urls import path

from routine.views import RoutineView

app_name = "routineapp"


urlpatterns = [
    path("<int:routine>", RoutineView.as_view(), name="routine"),
   
]
