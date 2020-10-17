from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from app_dogs.forms import DogsForm
from app_dogs.models import Dogs
from app_dogs.serializers import DogSerializer
from django.views import generic
from rest_framework.response import Response
from django.contrib.auth.forms import User
from django.contrib.auth.mixins import LoginRequiredMixin


class DogsApiView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = Dogs.objects.all()
    serializer_class = DogSerializer

    def post(self, request, *args, **kwargs):
        shelter_id = request.data.get('shelter')
        if shelter_id == request.user.id:
            return self.create(request, *args, **kwargs)
        else:
            return Response({f"Вы пытаетесь создать запись не под своим юзером. Ваш shelter - {request.user.id}"})


class DogsChangeApiView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = Dogs.objects.all()
    serializer_class = DogSerializer

    def put(self, request, *args, **kwargs):
        shelter_id = request.data.get('shelter')
        if request.user.is_superuser or request.user.id == shelter_id:
            return self.update(request, *args, **kwargs)
        else:
            return Response({f"Только администратор или {request.user} могут изменять эту запись."})

    def patch(self, request, *args, **kwargs):
        shelter_id = request.data.get('shelter')
        if request.user.is_superuser or request.user.id == shelter_id:
            return self.partial_update(request, *args, **kwargs)
        else:
            return Response({f"Только администратор или {request.user} могут изменять эту запись."})

    def delete(self, request, *args, **kwargs):
        shelter_id = request.data.get('shelter')
        if request.user.is_superuser or request.user.id == shelter_id:
            return self.destroy(request, *args, **kwargs)
        else:
            return Response({f"Только администратор или {request.user} могут удалить эту запись."})


class DogsListView(generic.ListView):
    model = Dogs
    context_object_name = 'dogs'


class DogsDetailView(View):

    def get(self, request, dog_id):
        dog = Dogs.objects.get(id=dog_id)
        return render(request, 'app_dogs/dog_detail.html', context={'dog': dog})


class DogsAddFormView(LoginRequiredMixin, View):

    def get(self, request):
        dogs_form = DogsForm()
        return render(request, 'app_dogs/add_dog.html', context={'dogs_form': dogs_form})

    def post(self, request):
        dogs_form = DogsForm(request.POST)

        if dogs_form.is_valid():
            dogs_form.cleaned_data['shelter'] = User.objects.get(id=self.request.user.id)
            Dogs.objects.create(**dogs_form.cleaned_data)
            return HttpResponseRedirect('/')
        return render(request, 'app_dogs/add_dog.html', context={'dogs_form': dogs_form})


class DogsEditViewForm(LoginRequiredMixin, View):
    def get(self, request, dog_id):
        dog = Dogs.objects.get(id=dog_id)
        dogs_form = DogsForm(instance=dog)
        return render(request, 'app_dogs/edit.html', context={'dogs_form': dogs_form, 'dog_id': dog_id})

    def post(self, request, dog_id):
        success = False
        dog = Dogs.objects.get(id=dog_id)
        dogs_form = DogsForm(request.POST, instance=dog)
        if (dogs_form.is_valid() and request.user == dog.shelter) or (dogs_form.is_valid() and request.user.is_superuser):
            success = True
            dogs_form.save()
        return render(request, 'app_dogs/edit.html', context={'dogs_form': dogs_form, 'dog_id': dog_id, 'success': success})


class DogsDeleteViewForm(LoginRequiredMixin, View):

    def get(self, request, dog_id):
        dog = Dogs.objects.get(id=dog_id)
        if request.user == dog.shelter or request.user.is_superuser:
            dog.delete()
            return HttpResponseRedirect("/")


class MainLoginView(LoginView):
    template_name = 'app_dogs/login.html'


class MainLogoutView(LogoutView):
    template_name = 'app_dogs/logout.html'
    next_page = '/'
