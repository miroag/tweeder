from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required


from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Topic, Listing


class IndexView(LoginRequiredMixin, generic.ListView):
    template_name = 'extract/index.html'
    context_object_name = 'topics'

    def get_queryset(self):
        return Topic.objects.all()


class DetailView(generic.DetailView):
    model = Topic
    template_name = 'extract/detail.html'


class ResultsView(generic.DetailView):
    model = Topic
    template_name = 'extract/detail.html'


# def index(request):
#
#     context = {'topics': Topic.objects.all()}
#     return render(request, 'extract/index.html', context)
#     #
#     # return HttpResponse("There are {} topics".format(Topic.objects.all().count()))
#
# def details(request, topic_id):
#     topic = get_object_or_404(Topic, pk=topic_id)
#     return render(request, 'extract/detail.html', {'topic': topic})


# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)
#
# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)