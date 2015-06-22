from django.shortcuts import render
from django.http import HttpResponse

from .models import Weapon
# Create your views here.
def index(request):
    weaponlist = Weapon.objects.order_by('weapon_name')
    context = {'weaponlist':weaponlist}
    return render(request, 'weapon_data/index.html', context)
    
def results(request, weapon_id):
    weapon = Weapon.objects.get(pk=weapon_id)
    color = 'White'
    if weapon.weapon_tier == 'Exotic':
        color = 'Gold'
    elif weapon.weapon_tier == 'Legendary':
        color = 'Purple'
    elif weapon.weapon_tier == 'Rare':
        color = 'Blue'
    elif weapon.weapon_tier == 'Uncommon':
        color = 'Green'
        
    context = {'weapon': weapon, 'color': color}
    return render(request, 'weapon_data/results.html', context)