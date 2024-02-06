from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from jobseeker.forms import RegistrationForm,StudentprofileForm #LoginForm
from django.urls import reverse_lazy
from django.views.generic import View,CreateView,TemplateView,DetailView,UpdateView,ListView
from myapp.models import Student,Job,Applications
from django.utils.decorators import method_decorator


def Signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            return redirect("login")
        else:
            return fn(request,*args,**kwargs)
    return wrapper
    




class RegisterView(CreateView):
    template_name = "jobseeker/register.html"
    form_class = RegistrationForm
    model= User
    success_url = reverse_lazy("signin")

# class SigninView(View):
#     def get(self,request,*args,**kwargs):
#         form = LoginForm()
#         return render(request,"jobseeker/login.html",{"form":form})
    
#     def post(self,request,*args,**kwargs):
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             u_name =form.cleaned_data.get("username")
#             pwd = form.cleaned_data.get("password")
#             user_obj = authenticate(request,username =u_name,password = pwd )
#             if user_obj:
#                 login(request,user_obj)
#                 return redirect()

#             else:
#                 print("invalid credentials")
#             return redirect("reg")
    
class Student_HomeView(ListView):
    template_name = "jobseeker/index.html"
    model = Job
    context_object_name = "job"

class jobseeker_profileView(CreateView):
    template_name = "jobseeker/profile.html"
    form_class = StudentprofileForm
    model = Student
    success_url = reverse_lazy("reg")

    # def post(self,request,*args,**kwargs):
    #     form = StudentprofileForm(request.POST,files = request.FILES)
    #     if form.is_valid():
    #         form.instance.user = request.user
    #         form.save()
    #         return redirect("seekerindex")
    #     else:
    #         print("get out")
    #     return redirect("reg")


    def form_valid(self, form: BaseModelForm):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

class ProfileView(DetailView):
    template_name = "jobseeker/p_view.html"
    context_object_name ="data"
    model = Student
    success_url = "profile_view"


    #class ProfileView(View):
    # def get(self,request,*args,**kwargs):
    #     id = kwargs.get("pk")
    #     data = Student.objects.filter(id=id)
    #     return render(request,"jobseeker/p_view.html",{"data":data})

class Update_Profile_View(UpdateView):
    template_name = "jobseeker/profile_edit.html"
    model = Student
    form_class = StudentprofileForm
    success_url = reverse_lazy("reg")  

class signout(View):
    def get(self,request):
        logout(request)
        return redirect("signin")

class JobDetailView(DetailView):
    template_name = "jobseeker/job_detail.html"
    model = Job
    context_object_name = "data"

@method_decorator(Signin_required,name="dispatch")
class JobApply(View):
    def get(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        data = Job.objects.get(id=id)
        Applications.objects.create(jobs = data,student = request.user)
        return redirect("seekerindex")
    

class Applied_jobs(View):
    def get(self,request,*args,**kwargs):
        data = Applications.objects.filter(student = request.user).values_list("jobs",flat=True)
        return render(request,"jobseeker/jobapplied.html",{"data":data})
    

class Delete_Job(View):
    def get(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        Applications.objects.get(id=id).delete()
        return redirect("seekerindex")




# class Regview(CreateView):

    
#     template_name="jobseeker/register.html"
#     form_class=ARegister
#     model=User
#     success_url=reverse_lazy("hr/login")
# class Signinview(View):
#     def get(self,request,args,*kwargs):
#         form=Login
#         return render(request,"jobseeker/index.html",{"form":form})
#     def post(self,request,args,*kwargs):
#         form=Login(request.POST)
#         if form.is_valid():
#             username=form.cleaned_data.get("username")
#             password=form.cleaned_data.get("password")
#             obj=authenticate(request,username=username,password=password)
#             if obj:
#                 login(request,obj)
#                 messages.success(request,"Login successful")
#             else:
#                 messages.error(request,"Invalid credentials")
#                 return redirect("login")
#         return redirect("category")
    
# class Student_home(ListView):
#     template_name="jobseeker/index.html"
#     model=Job
#     context_object_name="job"

# class Studentprofileview(CreateView):  
    
#     form_class=Studentprofile
#     template_name="jobseeker/profile.html"
#     model=Student
#     success_url=reverse_lazy("job")
    # def post(self,request,args,*kwargs):        
    #     form=Studentprofile(request.POST,files=request.FILES)
    #     if form.is_valid():
    #         form.instance.user=request.user
    #         form.save()
    #     else:
    #         redirect("studentprofile")
    #     return redirect("studentprofile")   
#     def form_valid(self, form: BaseModelForm):#to pass instance into a form we can use this function
#         form.instance.user=self.request.user
#         return super().form_valid(form) #super() gets data from parent class which is User
# class Viewprofile(DetailView):
    
    # template_name="jobseeker/profileview.html"
    # model=Student
    # context_object_name="data"
    # success_url=reverse_lazy("viewprofile")
    # # def get(self,request,args,*kwargs):
        # id=kwargs.get("pk")
        # data=Student.objects.get(id=id)
        # user=request.user
        # data=Student.objects.filter(user=user)
        # print(data)
    
        # return render(request,"jobseeker/profileview.html",{"data":data})
    
    # form_class=Studentprofile
    # template_name="jobseeker/profileview.html"
    # model=Student
    # context_object_name="profile"
# class Update_profile(UpdateView):
#     form_class=Studentprofile
#     template_name="jobseeker/profile_update.html"
#     model=Student
#     success_url=reverse_lazy("register")
# class ABEABAIACB

# class Listjob(ListView):    
#     template_name="jobseeker/index.html"
#     model=Job
#     context_object_name="job"
# class Jobdetail(DetailView):
#     template_name="jobseeker/jobdetail.html"
#     model=Job
#     context_object_name="jobview"





    



