# bot/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from aiogram.types import Update
from .dachabot import bot, dp
import asyncio
import json


@csrf_exempt
def webhook(request):
    if request.method == "POST":
        data = json.loads(request.body)
        update = Update(**data)
        asyncio.run(dp.feed_update(bot, update))
        return JsonResponse({"ok": True})
    return JsonResponse({"ok": False})
