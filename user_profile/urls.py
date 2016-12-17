from django.conf.urls import url,include

from .views import UserFormView, index, LoginView, writing, CreateWriting, Logout, EditView, Increase
from django.contrib.auth import views as auth_views



app_name='user_profile'

urlpatterns = [
    url(r'^register/', UserFormView.as_view(), name='register'),
    # url(r'^login/', views.login , name='login'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^$', index, name='index'),
    url(r'^logout', Logout, name='logout'),


    url(r'^(?P<pk>[0-9]+)/$', writing, name='writing'),
    url(r'^addnew/$', CreateWriting.as_view(), name='newriting'),
    url(r'^increase-credit/$', Increase , name='increase'),
    url(r'edit/$', EditView.as_view(), name='edit'),

    url('^password-change/$', auth_views.password_change, name='password_change'),
    url('^password-change/done/$', auth_views.password_change_done, name='password_change_done'),
    url('^password-reset/$', auth_views.password_reset),
    url('^password-reset/done/$', auth_views.password_reset_done),
    url('^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm),
    url('^reset/done/$', auth_views.password_reset_complete),

]
