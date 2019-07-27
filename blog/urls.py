from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about,name='about'),
    path('service', views.service,name='service'),
    path('portfolio', views.portfolio,name='portfolio'),
    path('contact', views.contact,name='contact'),
    #path('post/<int:pk>/', views.post_detail, name='post_detail'),
    #path('thankyou', views.thanks_view,name='thanks_view'),
    #path('freequote', views.newletter_view,name='newletter_view'),
    #path('newletter', views.freequote_view,name='freequote_view'),
]