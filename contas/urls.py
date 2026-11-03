from django.urls import include, path

app_name = 'contas'

urlpatterns = [
    path("", include('django.contrib.auth.urls')),
]