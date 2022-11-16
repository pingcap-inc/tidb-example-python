from django.db import transaction
from django.db.models import F
from django.shortcuts import get_object_or_404

from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import *
from .models import Player
import json


@require_POST
def create(request):
    dict_players = json.loads(request.body.decode('utf-8'))
    players = list(map(
        lambda p: Player(
            coins=p['coins'],
            goods=p['goods']
        ), dict_players))
    result = Player.objects.bulk_create(objs=players)
    return HttpResponse(f'create {len(result)} players.')


@require_GET
def count(request):
    return HttpResponse(Player.objects.count())


@require_GET
def limit_list(request, limit: int = 0):
    if limit is 0:
        return HttpResponse("")
    players = set(Player.objects.all()[:limit])
    dict_players = list(map(lambda p: p.as_dict(), players))
    return JsonResponse(dict_players, safe=False)


@require_GET
def get_by_id(request, player_id: int):
    result = get_object_or_404(Player, pk=player_id).as_dict()
    return JsonResponse(result)


@require_http_methods(["POST"])
@transaction.atomic
def trade(request):
    sell_id, buy_id, amount, price = int(request.POST['sellID']), int(request.POST['buyID']), \
                                     int(request.POST['amount']), int(request.POST['price'])
    sell_player = Player.objects.select_for_update().get(id=sell_id)
    if sell_player.goods < amount:
        raise Exception(f'sell player {sell_player.id} goods not enough')

    buy_player = Player.objects.select_for_update().get(id=buy_id)
    if buy_player.coins < price:
        raise Exception(f'buy player {buy_player.id} coins not enough')

    Player.objects.filter(id=sell_id).update(goods=F('goods') - amount, coins=F('coins') + price)
    Player.objects.filter(id=buy_id).update(goods=F('goods') + amount, coins=F('coins') - price)

    return HttpResponse("trade successful")

