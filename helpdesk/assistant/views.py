from django.shortcuts import render
from django.http import JsonResponse
from .forms import ChatForm
from .pipeline.llmpipelines import query_assist
from django.contrib.auth.decorators import login_required
from .pipeline.denialpipeline import denial_assist
from django.utils.safestring import mark_safe
# Create your views here.

@login_required
def assistant(request):
    if 'conversation_history' not in request.session:
        request.session['conversation_history'] = []
    if request.method == 'POST':
        form = ChatForm(request.POST)
        if form.is_valid():
            user_input = form.cleaned_data['user_input']
            user = request.user
            profile = user.profile
            conversation_history = request.session['conversation_history']
            p_summary = request.session['user_summary']
            model_output=query_assist(user_query=user_input,policy_name=profile.policy_name,conversation_history=conversation_history,profile_summary=p_summary)
            
            conversation_history.append({
                'user': user_input,
                'model': model_output
            })
            request.session['conversation_history'] = conversation_history
            response_data = {
                'user': "You: " + user_input,
                'model': "Bot: " + model_output 
            }
            return JsonResponse(response_data)
    else:
        # Clear the session history when the page is refreshed
        request.session['conversation_history'] = []
        
        form = ChatForm()
        return render(request, 'chat.html', {'form': form})
    
def denial(request):
    if request.method == 'POST':
        user = request.user
        profile=user.profile
        user_reason=request.POST.get('reason')
        p_summary = request.session['user_summary']
        model_output=denial_assist(policy_name=profile.policy_name,user_denial=user_reason,profile_summary=p_summary)
        safe_output = mark_safe(model_output)
        return render(request,'denial.html',{'output':safe_output})
    
    return render(request,'denial.html',{'output':""})


