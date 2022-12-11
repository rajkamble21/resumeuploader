from django.shortcuts import render
from .forms import ResumeForm, SignUpForm
from .models import Resume
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class CandidateView(View):
    def get(self, request, pk):
        candidate = Resume.objects.get(pk=pk)
        return render(request, 'myapp/candidate.html', {'candidate':candidate})


class ApplicantDetailView(DetailView):
    model = Resume


class ResumeCreateView(CreateView):
    form_class = ResumeForm
    template_name = 'myapp/resume_form.html'


class ResumeUpdateView(UpdateView):
    model = Resume
    fields = ['name','dob','gender','locality','city','pin','state','mobile','email','job_city','profile_image','my_file']


class ResumeDeleteView(DeleteView):
    model = Resume
    success_url = '/resumeform/'


class SignupCreateView(CreateView):
    form_class = SignUpForm
    template_name = 'myapp/signup_form.html'
    success_url = '/accounts/login/'