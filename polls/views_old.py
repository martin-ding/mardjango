import os

from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse ,FileResponse
from django.urls import reverse

from .models import Question,Choice
# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('polls/index.html')
    # return HttpResponse(template.render(context,request))
    context = {
        'latest_question_list' :latest_question_list
    }
    return render(request,'polls/index.html',context)
    # return HttpResponse(" ".join([list.question_text for list in latest_question_list]))


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    return render(request, 'polls/results.html', {'question': Question.objects.get(pk=question_id)})

def hello_world(request):
    return HttpResponse("contents")

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def response_image(request):
    # response = JsonResponse([1,2,3,4], encoder=False)

    # response = FileResponse(open('polls/asserts/test.txt', 'rb'))
    return response