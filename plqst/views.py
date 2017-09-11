from django.shortcuts import render
from .models import Game
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.models import UserProfile

# Create your views here.

def playquest_home(request):
    featured_games = Game.objects.filter(game_featured=True)[:5]
    recent_games = Game.objects.all()[:5]
    popular_games = Game.objects.all()[:5]

    context = {
        'featured_games':featured_games,
        'recent_games':recent_games,
        'popular_games':popular_games,
    }

    return render(request, 'plqst/playquest_home.html', context)

def demo(request):
	return render(request, 'plqst/demo.html', {})

def game_id(request, id):
	game = Game.objects.filter(id=id)
	if len(game) == 1:
		context = {
			'game':game,
			'game_id': id,
			}
	else:
		context = {}
	return render(request, 'plqst/game.html', context)

def create(request):
	return render(request, 'plqst/create.html', {})

@login_required
def edit_game(request, id):
    game = Game.objects.filter(id=id)
    context = {}
    if len(game) == 1:
        if str(game.first().game_owner) == str(request.user):
            print("game belongs to user")
            context = {
                'game':game.first(),
                'game_id':str(game.first().id)
            }
        else:
            print("You can't edit this game, but you can branch it")
    else:
        context = {}
    return render(request, 'plqst/edit.html', context)

def user_profile(request, username):
    u = User.objects.get(username=username)
    user_profile = UserProfile.objects.get(user=u)
    user_games = Game.objects.filter(user=u)
    context = {
        'user_profile':user_profile,
        'user_games':games,
    }
    return render(request, 'plqst/user_profile.html', context)

@login_required
def profile_page(request):
    user = request.user
    user_games = Game.objects.filter(game_owner=user)
    context = {
        "user_games":user_games,
    }

    return render(request, 'plqst/profile.html', context)

def sample_json(request):
	return render(request, 'plqst/sample.json', {})
