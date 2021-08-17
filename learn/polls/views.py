from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Question, Choice



def index(request):
	question_list = Question.objects.all()
	context = {'question_list':question_list}
	return render(request, 'polls/index.html', context)
    # return render(request, 'polls/index.html', context)


def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	print(question)
	# breakpoint()
	context = {'question':question}

	return render(request, 'polls/detail.html', context)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
