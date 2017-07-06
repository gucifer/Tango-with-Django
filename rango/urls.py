from django.conf.urls import patterns, url
# from . import views
from rango import views

# all patterns made case insensitive by adding (?i)
urlpatterns = patterns(
    '',
    url(r'^$', views.index, name='index'),
    url(r'(?i)^about/$', views.about, name='about'),
    url(r'(?i)^add_category/$', views.add_category, name='add_category'),
    url(r'(?i)^category/(?P<category_name_url>\w+)/$', views.category, name='category'),
    url(r'(?i)^category/(?P<category_name_url>\w+)/add_page/$', views.add_page, name='add_page'),
    url(r'(?i)^register/$', views.register, name='register'),
    url(r'(?i)^login/$', views.user_login, name='login'),
    url(r'(?i)^restricted/$', views.restricted, name='restricted'),
    url(r'(?i)^logout/$', views.user_logout, name='logout'),
    url(r'(?i)^scratch/$', views.scratch, name='scratch'),
    url(r'(?i)^search/$', views.search, name='search'), 
)
