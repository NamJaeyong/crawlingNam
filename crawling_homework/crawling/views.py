from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
# Create your views here.

def home(request):
    return render(request, 'home.html')

def result(request):
    if request.method == 'POST':
        search_word = request.POST.get('search_word', '')
    
        URL = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query='
        fullurl = URL + search_word
        data = requests.get(fullurl).text
        soup = BeautifulSoup(data, 'html.parser')
        news_titles = soup.find_all(class_='_sp_each_title')
        title_list = []
        for title in news_titles:
            title_list.append({'url':title.get('href'),'title':title.get('title')})
        return render(request, 'result.html', {'title_list':title_list})
    else:
        return render(request, 'home.html')
