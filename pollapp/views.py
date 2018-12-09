from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


from .models import Choice, Question, TakenPoll

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'index.html'

class PollListView(ListView):
    template_name = 'pollapp/poll_list.html'
    context_object_name = 'poll_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-question_date')[:10]

class PollDetailView(DetailView):
    model = Question
    template_name = 'pollapp/poll_detail.html'

class ReportView(DetailView):
    model = Question
    template_name = 'pollapp/poll_report.html'

@login_required
def vote(request, question_id):

    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):

        # Redisplay the question voting form.
        return render(request, 'pollapp/poll_detail.html', {
        'question': question,
        'error_message': "You didn't select a choice.",
        })
    else:
        #check db is user has already taken the test
        question_taken_by_user = TakenPoll.objects.filter(user=request.user, poll=question, poll_id=question_id)

        #check if the db returns an empty list
        if len(question_taken_by_user) == 0:
             question_taken_by_user = False

        #if True Execute condition, False Skip condition and count vote
        if question_taken_by_user:
            return render(request, 'pollapp/poll_detail.html', {
            'question': question,
            'error_message': "You have Taken Poll Before, choose another",
            })
        else:
            selected_choice.votes += 1
            selected_choice.save()

            taken_poll = TakenPoll(user=request.user, poll=question, poll_id=question_id)
            taken_poll.save()

            return HttpResponseRedirect(reverse('pollapp:poll_report', args=(question.id,)))

class TakenListView(ListView):
    template_name = 'pollapp/taken_poll_list.html'
    context_object_name = 'taken_poll_list'

    def get_queryset(self):
        return TakenPoll.objects.filter(user=self.request.user)
