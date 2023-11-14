from datetime import timedelta
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views import generic
from django.utils.safestring import mark_safe
from django.contrib.auth.mixins import LoginRequiredMixin
from routine.models import RoutineEvent, Routine
from routine.forms import RoutineEventsForm,RoutineForm


def list_routine(request):
    routine = Routine.objects.filter(user=request.user).all()
    context = {
        'routines' : routine
    }
    
    return render(request,'routineapp/list_routine.html',context)

def create_routine(request):
    if request.method == "POST":
        form = RoutineForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            private = form.cleaned_data['private']
            routine = Routine()
            routine.name = name
            routine.private = private
            routine.user = request.user
            routine.save()
        return redirect('routineapp:list_routine')

    else:
        form = RoutineForm()

    context = {
        "form": form
    }
    return render(request, 'routineapp/create_routine.html', context)


class RoutineView(LoginRequiredMixin, generic.View):
    login_url = "accounts:signin"
    template_name = "routineapp/calendar.html"
    form_class = RoutineEventsForm
    


    def get(self, request,routine, *args, **kwargs,):
        forms = self.form_class()
        routine = get_object_or_404(Routine, pk=routine)
        events = RoutineEvent.objects.filter(routine = routine)
        event_list = []
        for event in events:
            event_list.append(
                {   "id": event.routine_event_id,
                    "title": event.title,
                    "start": event.start_time.strftime("%Y-%m-%dT%H:%M:%S"),
                    "end": event.end_time.strftime("%Y-%m-%dT%H:%M:%S"),
                    "description": event.description,
                }
            )
        
        context = {"form": forms, "events": event_list, "routine" : routine}
        return render(request, self.template_name, context)

    def post(self, request,routine, *args, **kwargs):
        forms = self.form_class(request.POST)
        if forms.is_valid():
            form = forms.save(commit=False)
            form.user = request.user
            routine = get_object_or_404(Routine, pk=routine)
            form.routine = routine
            form.save()
            return redirect('routineapp:routine',routine.pk)
        context = {"form": forms}
        return render(request, self.template_name, context)


def next(request, event_id,days):
    event = get_object_or_404(RoutineEvent, routine_event_id=event_id)
    if request.method == 'POST':
        next = event
        next.routine_event_id = None
        next.start_time += timedelta(days=days)
        next.end_time += timedelta(days=days)
        next.save()
        return JsonResponse({'message': 'Sucess!'})
    else:
        return JsonResponse({'message': 'Error!'}, status=400)

def clone(request,pk):
    routine = get_object_or_404(Routine, pk=pk)
    if request.method == 'POST':
        events = RoutineEvent.objects.filter(routine=routine).all()
        new_routine = Routine()
        routine_name = 'Clone ' + routine.name
        new_routine.name = routine_name
        new_routine.user = request.user
        new_routine.save()
        for event in events:
            new_event_routine = RoutineEvent()
            new_event_routine.title = event.title
            new_event_routine.description = event.description
            new_event_routine.start_time = event.start_time
            new_event_routine.end_time = event.end_time
            new_event_routine.routine = new_routine
            new_event_routine.save()
        
        return redirect('routineapp:list_routine')
            
    return HttpResponse("")
    