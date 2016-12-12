from datetime import datetime
from django.core.urlresolvers import reverse
import requests
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.utils import timezone
from django.views import generic
from . import dbqeury
from .models import Snacks
from .models import Poll





class IndexView(generic.ListView):

    dbqeury.getSnacks()
    template_name = 'polls/index.html'
    context_object_name = 'latest_poll_list'

    def get_queryset(self):
        """
        Return the last five published polls (not including those set to be
        published in the future).
        """

        return Poll.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Poll
    template_name = 'polls/detail.html'

    def get_queryset(self):

        return Poll.objects.filter()


def suggestionView(request):

    return render(request, 'polls/suggestions.html',{})

def uploadSuggestion(request): #used to pull data from suggestions.html
    if request.method == 'POST':
        suggestName = request.POST['snackName']
        suggestLoc = request.POST['purchLocation']
        p = Poll.objects.get(pk=3)
        p.snacks_set.create(name=suggestName,source_ID=suggestLoc,optional="n/a",purchaseLocation="n/a",purchaseCount=0,lastPurchaseDate=timezone.now(),votes=0)
        requests.post('https://api-snacks.nerderylabs.com/v1/snacks?ApiKey=05ec8f9f-432f-45ed-84fb-aa3c844d8870', data={'name': suggestName, 'location': suggestLoc, 'latitude': 0, 'longitude': 0})
        #Pushes user back to main menu. Effectively a 'back' button.
        return HttpResponseRedirect(reverse('polls:index'))

class ResultsView(generic.DetailView): #displays results
    model = Poll
    template_name = 'polls/results.html'

def vote(request, poll_id): #takes user input from display.html

    p = get_object_or_404(Poll, pk=poll_id)
    times_voted = int(request.COOKIES.get('visits','1')) #Counter started at 1 instead of 0
    response = HttpResponse('polls/detail.html')
    try:
        selected_choice = p.snacks_set.get(pk=request.POST['snack'])
    except (KeyError, Snacks.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'polls/detail.html', {'poll': p,'error_message': "You didn't select a choice.",})
    else:
        if 'vote_checker' in requests.COOKIES: #checks if cookie exists
            vote_checker = requests.COOKIES['vote_checker']
            vote_checker_date = datetime.strptime(vote_checker[:-7], "%Y-%m-%d %H:%M:%S") #Note: Using a mix of timezone and datetime because I don't want to futz with the program anymore than required
            if (datetime.now() - vote_checker_date).days < 30: #If cookie exists: makes sure it's less than 30 days old
                if times_voted <= 3: #If less than 30 days old: Checks if voted three times
                    response.set_cookie('times_voted',times_voted+1)
                    selected_choice.votes += 1
                    selected_choice.save()
                    return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
                else: #If cookie has been voted on three times, receive error message
                    return render(request, 'polls/detail.html', {'poll': p,'error_message': "You have already voted three times this month!.",})
            else: #If cookie is older than 30 days, resets the time
                response.set_cookie('vote_checker',datetime.now())
                return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
        else:
            #If no cookie exists: makes a cookie and send request on through
            response.set_cookie('vote_checker', datetime.now())
            return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))

