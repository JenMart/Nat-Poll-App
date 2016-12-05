from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.views import generic
from .models import snacks, voters, Poll


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_poll_list'

    def get_queryset(self):
        """
        Return the last five published polls (not including those set to be
        published in the future).
        """

        return Poll.objects.filter(pub_date__lte=timezone.now() ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = snacks
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any polls that aren't published yet.
        """

        return snacks.objects.filter()


class ResultsView(generic.DetailView):
    model = snacks
    template_name = 'polls/results.html'


def vote(request, formerCurrent): #no effect
    p = get_object_or_404(snacks, pk=formerCurrent)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['name'])
    except (KeyError, snacks.DoesNotExist):
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