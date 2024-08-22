from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [
    # path('concept.com',views.home, name='home'),
    path('',include("Concept_app.urls")),
    path('', RedirectView.as_view(url='/Sobre')),
]

