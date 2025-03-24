# survey_app/views.py
from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from .forms import SurveyForm

def survey_view(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('survey-thanks')
    else:
        form = SurveyForm()
    return render(request, 'survey_app/survey_form.html', {'form': form})

def survey_thanks_view(request):
    return render(request, 'survey_app/survey_thanks.html')

