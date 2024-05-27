from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

from .models import Question, Choice
from django.http import Http404

def home(request):
    questions = Question.objects.all()
    return render(request, 'polls/home.html',{
        'questions' : questions
    })

def vote (request, q_id):
    question = get_object_or_404 (Question, id=q_id)

    if request.method == 'POST':
        try:
            choice = request.POST['choice']
            c = Choice.objects.get(id=choice)
            c.votes += 1 
            c.save()

            return redirect('polls:results', q_id)
        except (KeyError):
            return render(request, 'polls/question.html',
                          {"question": question,
                           "error_message" : "Elige una opcion"})
    return render(request, 'polls/question.html',
                  {"question": question})

def results (request, q_id):
    try:

       question = Question.objects.get(id=q_id)
    except Question.DoesNotExist:
          raise Http404("Question dose not exist")
    return render(request, 'polls/results.html',
                  {"question": question})