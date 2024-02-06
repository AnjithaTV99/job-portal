from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse_lazy

from django.views.generic import View,FormView,TemplateView,CreateView,ListView,DeleteView,UpdateView,DetailView  # A view for displaying a form and rendering a template response
from hr.forms import LoginForm,JobForm,CategoryForm
from myapp.models import Job,Category

class LoginView(FormView):
    template_name = "login.html"
    form_class = LoginForm

    def post(self,request,*args,**kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            u_name = form.cleaned_data.get("username")
            pwd = form.cleaned_data.get("password")
            user_obj = authenticate(request,username=u_name,password=pwd)
            if user_obj:
                login(request,user_obj)
                if request.user.is_superuser:
            
                    return redirect ("index")
                else:
                    return redirect("seekerindex")
            else:
                print("failed")
            return render(request,"login.html",{"form":form})    
        
class DashboardView(TemplateView):
    template_name = "index.html"


class SignoutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("signin")
    
class AddcategoryView(CreateView,ListView):
    template_name = "category.html"
    form_class = CategoryForm
    success_url = reverse_lazy("category")
    context_object_name="data"
    model = Category


class CategoryremoveView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Category.objects.get(id=id).delete()
        return redirect("category")
    




class AddjobView(CreateView):
    template_name = "add_job.html"
    form_class = JobForm
    model = Job
    success_url = reverse_lazy("joblist")
    context_object_name = ("qs")


class DeljobView(View):
    def get(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        Job.objects.get(id=id).delete()
        return redirect("joblist")


class JoblistView(ListView):
    template_name = "job_list.html"
    model = Job
    context_object_name = "jobs"

class JobupdateView(UpdateView):
    template_name ="jobupdate.html"
    form_class = JobForm
    model = Job
    success_url = reverse_lazy('joblist')

class JobdetailsView(View):
    def get(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        qs = Job.objects.filter(id=id)
        return render(request,"jobdetails.html",{"qs":qs})
        

    
