from django.urls import path
import account.views

app_name = 'account'

URLPattern = [
    path('login/', account.views.login, name='login'),
    path('signup/', account.views.signup, name='signup'),
    path('logout/', account.views.logout, name='logout'),
]

 