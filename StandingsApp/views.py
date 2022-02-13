from django.shortcuts import redirect, render, HttpResponse
from .models import *

def index(request):
    return HttpResponse("Mom")

def main(request):
    context = {
        "all_teams" : Team.objects.all()
    }
    return render (request, "main.html", context)

def teamform(request):
    return render (request, "addTeam.html")

def addTeam(request):
    city = request.POST['city']
    mascot = request.POST['mascot']
    division = request.POST['division']
    overall_wins = request.POST['overall_wins']
    overall_losses = request.POST['overall_losses']
    conf_wins = request.POST['conf_wins']
    conf_losses = request.POST['conf_losses']
    primary_color = request.POST['primary_color']
    secondary_color = request.POST['secondary_color']
    this_team = Team.objects.create(city=city, mascot=mascot, division=division, overall_wins=overall_wins, overall_losses=overall_losses, conf_wins=conf_wins, conf_losses=conf_losses, primary_color=primary_color, secondary_color=secondary_color)
    this_team.save()
    return redirect ('/main')

def editteam(request, team_id):
    context = {
        "team" : Team.objects.get(id=team_id)
    }
    return render(request, "editTeam.html", context)

def updateteam(request, team_id):
    team = Team.objects.get(id=team_id)
    team.city = request.POST['city']
    team.mascot = request.POST['mascot']
    team.overall_wins = request.POST['overall_wins']
    team.overall_losses = request.POST['overall_losses']
    team.conf_wins = request.POST['conf_wins']
    team.conf_losses = request.POST['conf_losses']
    team.primary_color = request.POST['primary_color']
    team.secondary_color = request.POST['secondary_color']
    team.save()

    return redirect('/main')

def deleteteam(request, team_id):
    team = Team.objects.get(id=team_id)
    team.delete()

    return redirect ('/main')