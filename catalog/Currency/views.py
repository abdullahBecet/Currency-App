from django.shortcuts import render
from pages import Currency
from flask import Flask, request

def index(request):   
    context = {
       'name' : Currency.get_currencies
        }  
    return render(request, 'Currency/list.html', context)

def detail(request):
    context = {
        'nam' : Currency.exchange_rate
    }
    return render(request, 'Currency/detail.html',context)

def search(request):
    return render(request, 'Currency/search.html')

app = Flask(__name__)

@app.route('/exchange', methods=['POST'])
def exchange():
    from_currency = request.form['from_currency']
    to_currency = request.form['to_currency']
    
    return detail(from_currency, to_currency)

