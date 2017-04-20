from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Choice, Question

'''
类似地，ListView使用一个叫做<app name>/<model name>_list.html的默认模板

对于DetailView ，question变量会自动提供—— 因为我们使用Django 的模型 (Question)，
Django 能够为context 变量决定一个合适的名字。然而对于ListView， 自动生成的context
变量是question_list。为了覆盖这个行为，我们提供 context_object_name 属性，
表示我们想使用latest_question_list。作为一种替换方案，你可以改变你的模板来
匹配新的context变量 —— 但直接告诉Django使用你想要的变量会省事很多。
'''
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    '默认情况下，通用视图DetailView 使用一个叫做' \
    '<app name>/<model name>_detail.html的模板。' \
    '在我们的例子中，它将使用 "polls/question_detail.html"模板。'
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question':      question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
