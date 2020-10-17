from django.urls import path
from app_dogs.views import DogsListView, DogsDetailView, DogsAddFormView, DogsEditViewForm, DogsApiView, \
    DogsDeleteViewForm, MainLoginView, MainLogoutView, DogsChangeApiView
#
urlpatterns = [
    path('api/dogs/', DogsApiView.as_view({'get': 'list'})),
    path('api/dogs/<int:pk>/', DogsChangeApiView.as_view({'get': 'retrieve'})),
    path('', DogsListView.as_view(), name='dogs'),
    path('<int:dog_id>/', DogsDetailView.as_view(), name='dog_detail'),
    path('app_dogs/add_dog/', DogsAddFormView.as_view(), name='add_dog'),
    path('app_dogs/<int:dog_id>/edit/', DogsEditViewForm.as_view(), name='edit'),
    path('app_dogs/<int:dog_id>/delete/', DogsDeleteViewForm.as_view(), name='delete'),
    path('app_dogs/login/', MainLoginView.as_view(), name='login_page'),
    path('app_dogs/logout/', MainLogoutView.as_view(), name='logout_page'),
]
