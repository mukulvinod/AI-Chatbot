from django.shortcuts import render
from django.http import JsonResponse
from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)


def call_openai_chatbot(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are meant to keep a happy tone while also being useful."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()

def home(request):
    return render(request, 'Chatbot/home.html')

def get_response(request):
    user_input = request.GET.get('user_input')
    response = call_openai_chatbot(user_input)
    return JsonResponse({'response': response})
