from django.conf.urls import url, include
from . import views
from .api.views import GameCreateAPIView, GameListAPIView, GameDetailAPIView, GameUpdateAPIView

urlpatterns = [
        url(r'^user/(?P<username>[A-Za-z0-9]+)/$', views.user_profile, name="user_profile"),
        url(r'^profile/$', views.profile_page, name='profile'),
		url(r'^create/$', views.create, name='create'),
		url(r'^demo/$', views.demo, name='demo'),
		url(r'^$', views.playquest_home, name="home"),
		url(r'^game/(?P<id>[A-Za-z0-9]+)/edit/$', views.edit_game, name='edit_game'),
		url(r'^game/(?P<id>[A-Za-z0-9]+)/$', views.game_id, name='game_id'),
		url(r'^json/$', views.sample_json, name="sample_json"),
		## To Do

		# API CRU[D] endpoints coming from /api/kings/ (in main urls.py)
		url(r'^api/save/$', GameCreateAPIView.as_view(), name="save-game"),
        url(r'^api/list/$', GameListAPIView.as_view(), name="game-list"),
		url(r'^api/(?P<pk>[A-Za-z0-9]+)/$', GameDetailAPIView.as_view(), name="game-details"),
		url(r'^api/(?P<pk>[A-Za-z0-9]+)/update/$', GameUpdateAPIView.as_view(), name="update-game"),
]
