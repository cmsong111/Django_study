from django.contrib import admin
from django.urls import path, include
from mysite import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.HomeView.as_view(),name = 'home'),
    # shkim
    path('polls/', include('polls.urls')),
    path('books/', include('books.urls')), #books

]
