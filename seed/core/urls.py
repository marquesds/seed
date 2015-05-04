from django.conf.urls import url

urlpatterns = [
    url(r'^$', 'seed.core.views.index', name='index'),
]
