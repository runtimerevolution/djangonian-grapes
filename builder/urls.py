from django.urls import path
from builder import views


urlpatterns = [
    path('/<str:slug>', views.BuilderView.as_view(), name='builder'),
    path('/preview/<str:slug>', views.PageDetailView.as_view(), name='preview'),
    path('/save/<int:id>', views.save, name='save'),
    path('/load/<int:id>', views.load, name='load'),
]
