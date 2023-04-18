from django.shortcuts import render, HttpResponse

html_base = """ 

<h1>Mi web personal</h1>

<ul>
    <li><a href="/"> Portada</a></li>
    <li><a href="/about-me"> Acerca de </a></li>
    <li><a href="/portfolio"> Portafolio</a></li>
    <li><a href="/contact"> Contact </a></li>

</ul>
"""
# Create your views here.

def home(request):
    return HttpResponse(html_base + """<h2>Portada</h2> <p>Esto es la portada</p>""")

def about(request):
    return HttpResponse(html_base + """<h2>Acerca de</h2> <p>Mi nombre es Emanuel Rangel Luna</p>""")

def portfolio(request):
    return HttpResponse(html_base + """<h2>Portfolio</h2> <p>Estos son mis proyectos</p>""")

def contact(request):
    return HttpResponse(html_base + """<h2>contact</h2> <p>Mi numero de telefono es</p>""")

