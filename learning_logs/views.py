from django.shortcuts import render, redirect

from .models import Topic
from .forms import TopicForm

def index(request):
    """Learning Log app homepage"""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
    """Defines a new topic"""
    if request.method != 'POST':
        # No data was submitted; an empty form is being created.
        form = TopicForm()
    else:
        # POST data sent; process data.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')
        
    # Output an empty or invalid form.
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)