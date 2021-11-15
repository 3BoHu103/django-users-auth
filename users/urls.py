from django.urls import path, include
from .views import SignUp, dashboard

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('dashboard/', dashboard, name='dashboard'),
]
