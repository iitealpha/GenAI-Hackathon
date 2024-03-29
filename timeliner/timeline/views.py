from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .main import get_timeline
import json


@csrf_exempt
def process_input(request):
    if request.method == 'POST':
        topic = request.POST.get('topic', '')
        print(topic)
        result = get_timeline(topic)
        result = json.loads(result)
        return JsonResponse(result, safe=False)
    
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

