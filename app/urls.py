from django.urls import path, include
from django.urls.resolvers import URLPattern
from .views import *


urlpatterns = [
    path('paradigm/',ParadigmView.as_view(),name='paradigm'),
    path('paradigmDetail/<int:pk>/',ParadigmDetailView.as_view(),name='paradigm_detail'),
    path('language/',LanguageView.as_view(),name='language'),
    path('languageDetail/<int:pk>/',LanguageDetailView.as_view(),name='language_detail'),
    path('programmer/',ProgrammerView.as_view(),name='programmer'),
    path('ProgrammerDetail/<int:pk>/',ProgrammerDetailView.as_view(),name='programmer_detail')
]