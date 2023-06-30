from django.urls import path
from .views import *

app_name = 'login'

urlpatterns = [
  path('', login_view, name="login"),
  path('logout/', logout_view, name="logout"),
  path('signup/', signup, name="signup"),
]
