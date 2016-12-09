from django.core.urlresolvers import reverse
import requests
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.views import generic
from . import dbqeury
from django.template import loader

#basic design of application influenced by django tutorial

from .models import Snacks, voters, Poll


class IndexView(generic.ListView):
    dbqeury.getSnacks()
    template_name = 'polls/index.html'
    context_object_name = 'latest_poll_list'

    def get_queryset(self):
        """
        Return the last five published polls (not including those set to be
        published in the future).
        """

        return Poll.objects.filter(pub_date__lte=timezone.now() ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Poll
    template_name = 'polls/detail.html'

    def get_queryset(self):

        return Poll.objects.filter()


def suggestionView(request):

    return render(request, 'polls/suggestions.html', {})

def uploadSuggestion(request): #used to pull data from suggestions.html
    if request.method == 'POST':
        suggestName = request.POST['snackName']
        suggestLoc = request.POST['purchLocation']
        p = Poll.objects.get(pk=3)
        p.snacks_set.create(name=suggestName,source_ID=suggestLoc,optional="n/a",purchaseLocation="n/a",purchaseCount=0,lastPurchaseDate=timezone.now(),votes=0)
        requests.post('https://api-snacks.nerderylabs.com/v1/snacks?ApiKey=05ec8f9f-432f-45ed-84fb-aa3c844d8870', data={'name': suggestName, 'location': suggestLoc, 'latitude': 0, 'longitude': 0})
        return render(request, 'polls/index', {})



class ResultsView(generic.DetailView): #displays results
    model = Poll
    template_name = 'polls/results.html'


def vote(request, poll_id): #takes user input from display.html
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.snacks_set.get(pk=request.POST['snack'])
    except (KeyError, Snacks.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'polls/detail.html', {'poll': p,'error_message': "You didn't select a choice.",})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.

        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))



##############happy place#############
# def detail(request, question_id):
#     return HttpResponse("You're looking at question ")
#
# def results(request, question_id):
#     response = "You're looking at the results of question"
#     return HttpResponse(response)
#
# def vote(request, question_id):
#     return HttpResponse("You're voting on question ")