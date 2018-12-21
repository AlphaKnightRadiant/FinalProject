from django.urls import path
from RyaFree import views

urlpatterns = [
    path('',views.help,name='help'),
    #path('',views.InitialDesign,name='InitialDesign'),
    #path('Services/',{'template_name': 'RyaFree/Services.html'}),
]
