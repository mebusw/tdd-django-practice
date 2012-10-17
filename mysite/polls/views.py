from django.shortcuts import render
from polls.models import Poll

def home(request):
    context = {'polls': Poll.objects.all()}
    return render(request, 'home.html', context)
    
def poll(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    return render(request, 'poll.html', {'poll': poll})