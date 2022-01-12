from django.contrib import admin
from django.urls import path
from predictionApp import views as predictViews
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

urlpatterns = [
    path('admin/',                                      admin.site.urls),
    path('login/',                                      TokenObtainPairView.as_view()),
    path('refresh/',                                    TokenRefreshView.as_view()),
    path('user/',                                       predictViews.UserCreateView.as_view()),
    path('user/<int:pk>/',                              predictViews.UserDetailView.as_view()),
    path('prediction/create/<int:user>/',               predictViews.PredictionCreateView.as_view()),
    path('predictions/myPredictions/<int:user>/',       predictViews.ListPredictionsViews.as_view()),
    path('prediction/delete/<int:user>/',               predictViews.PredictionDeleteView.as_view()),
]
