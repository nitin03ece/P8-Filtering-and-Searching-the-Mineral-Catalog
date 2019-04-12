from django.conf.urls import url


from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^list/$', views.mineralsList, name='mineral_list'),
    url(r'^random/$', views.randomMineral, name='random_mineral'),
    url(r'^filter_by_alphabet/(?P<alpha>\w)/$', views.alpha_filtered_mineralList, name='alpha_list'),
    url(r'^filter_by_group/(?P<group>[a-zA-Z0-9 ]+)/$', views.group_filtered_mineralList, name='group_list'),
    url(r'^(?P<name>.*)/$', views.mineralDetail, name='mineral_detail'),
]
