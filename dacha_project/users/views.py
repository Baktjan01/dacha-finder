import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User


@api_view(['POST'])
def telegram_auth(request):
    user_data = request.data.get('user', {})

    telegram_id = user_data.get('id')
    first_name = user_data.get('first_name', '')
    last_name = user_data.get('last_name', '')
    username = user_data.get('username', '')

    if not telegram_id:
        return Response({'error': 'No telegram_id'}, status=status.HTTP_400_BAD_REQUEST)

    user, created = User.objects.get_or_create(
        telegram_id=telegram_id,
        defaults={
            'username': username or f'tg_{telegram_id}',
            'first_name': first_name,
            'last_name': last_name,
            'telegram_username': username,
        }
    )

    return Response({
        'user_id': user.id,
        'telegram_id': user.telegram_id,
        'name': user.first_name,
        'username': user.username,
        'created': created,
    })
