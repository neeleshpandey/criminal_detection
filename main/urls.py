from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static

from main.views import FileView
from . import views

urlpatterns = [
    re_path(r'^$', views.index),
    re_path(r'^add_user', views.addUser),
    re_path(r'^save_user', views.add_user),
    re_path(r'^view_users$', views.viewUsers, name='view_users'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
    re_path(r'^success$', views.success),

    re_path(r'^add_citizen', views.addCitizen),
    re_path(r'^save_citizen', views.saveCitizen),
    re_path(r'^view_citizens', views.viewCitizens),

    path('wanted_citizen/<int:citizen_id>/',views.wantedCitizen,name='wanted_citizen'),
    path('free_citizen/<int:citizen_id>/',views.freeCitizen,name='free_citizen'),




    re_path(r'^login$', views.login),
    re_path(r'^logout', views.logout_view),
    re_path(r'^detectImage', views.detectImage),
    re_path(r'^detectWithWebcam', views.detectWithWebcam),
    re_path(r'^process_frame$', views.process_frame),
    re_path(r'^upload', FileView.as_view(), name='file-upload'),

    re_path(r'^spotted_criminals', views.spottedCriminals),
    path('thief_location/<int:thief_id>/',views.viewThiefLocation,name='thief_location'),
    path('found_thief/<int:thief_id>/', views.foundThief, name='found_thief'),

    re_path(r'^reports', views.viewReports),





]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
