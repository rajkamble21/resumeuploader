from django.contrib import admin
from django.urls import path, include
from myapp import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.TemplateView.as_view(template_name='myapp/base.html'), name="home"),
    path('signup/', views.SignupCreateView.as_view(), name='signup_form'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/', include('api.urls')),

    path('resumeform/', login_required(views.ResumeCreateView.as_view()), name='resume_form'),
    path('update/<int:pk>/', login_required(views.ResumeUpdateView.as_view()), name='update_form'),
    path('delete/<int:pk>/', login_required(views.ResumeDeleteView.as_view()), name='delete_form'),
    path('detail/<int:pk>/', login_required(views.ApplicantDetailView.as_view()), name='resume_detail'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
