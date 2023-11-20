from datetime import timedelta
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views import generic
from django.utils.safestring import mark_safe
from django.contrib.auth.mixins import LoginRequiredMixin
from routine.models import RoutineEvent, Routine
from routine.forms import RoutineEventsForm,RoutineForm
from post.forms import PostForm, CommentForm
from post.models import Post, Comment


def post(request):
    return render(request,'post/posts.html')



class PostCreateView(LoginRequiredMixin, generic.View):
    login_url = "accounts:signin"
    template_name = "post/post_create.html"
    form_post = PostForm

    
    def get(self, request,routine, *args, **kwargs,):
        forms = self.form_post()
        routine = get_object_or_404(Routine, pk=routine)
        events = RoutineEvent.objects.filter(routine = routine).all()
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
        forms = self.form_post(request.POST)
        if forms.is_valid():
            title = forms.cleaned_data['title']
            text = forms.cleaned_data['text']
            routine = get_object_or_404(Routine, pk=routine)
            post_ = Post()
            post_.routine = routine
            post_.user = request.user
            post_.text = text
            post_.title = title
            post_.rating = 0
            post_.save()
            return redirect('post:post',post_.pk)
        context = {"form": forms}
        return render(request, self.template_name, context)

class PostView(LoginRequiredMixin, generic.View):
    login_url = "accounts:signin"
    template_name = "post/post.html"
    form_post = CommentForm

    def get(self, request,post, *args, **kwargs,):
        forms = self.form_post()
        post = get_object_or_404(Post, pk=post)
        comments = Comment.objects.filter(post=post).all()
        routine = get_object_or_404(Routine, pk=post.routine.pk)
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
        context = { "form": forms,
                    "post" : post,
                    "comments" : comments,
                    "events": event_list}
        return render(request, self.template_name, context)

    def post(self, request,post,*args, **kwargs):
        forms = self.form_post(request.POST)
        if forms.is_valid():
            text = forms.cleaned_data['text']
            post = get_object_or_404(Post, pk=post)
            comment = Comment()
            comment.text = text
            comment.user = request.user
            comment.post = post
            comment.rating = 0
            comment.save()
            return redirect('post:post', post.pk )
        context = {"form": forms}
        return render(request, self.template_name, context)
