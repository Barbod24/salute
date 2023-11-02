from typing import Any
from django import http
from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from home.models import Post
from .models import Relation
# Create your views here.

class Register(View):
    form_class=Register_form
    template_name='account/register.html'
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home:home')
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request):
        form=self.form_class()
        return render(request,self.template_name,{'form':form})
    def post(self,request):
        
        form=self.form_class(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            User.objects.create_user(cd['username'],cd['email'],cd['password'])
            messages.success(request,'Registered successfully!','success')
            return redirect('home:home')
        return render(request,self.template_name,{'form':form})


class User_login(View):
    form_class=Login_form
    template_name='account/login.html'
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home:home')
        return super().dispatch(request, *args, **kwargs)
    def get(self,request):
        form=self.form_class()
        return render(request,self.template_name,{'form':form})
    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            user=authenticate(request,username=cd['username'],password=cd['password'])
            if user is not None:
                login(request,user)
                messages.success(request,'Logged in successfully!','success')
                return redirect('home:home')
            
        return render(request,self.template_name,{'form':form})
       
    
class UserLogoutView(LoginRequiredMixin,View):
    def get(self,request):
        logout(request)
        messages.success(request,'Logged out successfully!','success')
        return redirect('home:home')

class UserProfileView(LoginRequiredMixin, View):
    def get(self, request, user_id):
       user=User.objects.get(id=user_id)
       return render(request,'account/profile.html',{'user':user})
   
class UserFollowView(LoginRequiredMixin, View):
    def get(self, request, user_id):
        user = User.objects.get(pk=user_id)
        relation = Relation.objects.filter(from_user=request.user, to_user=user)

        if relation.exists():
            messages.error(request, "You are already following this user", "danger")
        else:
            Relation(from_user=request.user, to_user=user).save()
            messages.success(request, "You follow this user", "success")
        return redirect("account:user_profile", user.username)


class UserUnFollowView(LoginRequiredMixin, View):
    def get(self, request, user_id):
        user = User.objects.get(pk=user_id)
        relation = Relation.objects.filter(from_user=request.user, to_user=user)

        if relation.exists():
            relation.delete()
            messages.success(request, "You unfollowed this user", "success")

        else:
            messages.error(request, "You are not following this user", "danger")

        return redirect("account:user_profile", user.username)
