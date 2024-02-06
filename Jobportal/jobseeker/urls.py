from django.urls import path
from jobseeker import views

urlpatterns = [
    path("registration/",views.RegisterView.as_view(),name = "reg"),
    # path("index/",views.SigninView.as_view(),name = "index"),
    path("seekerhome/",views.Student_HomeView.as_view(),name = "seekerindex"),
    path("create_profile/",views.jobseeker_profileView.as_view(),name = "profile"),
    path("view_profile/<int:pk>",views.ProfileView.as_view(),name = "profile_view"),
    path("update_profile/<int:pk>",views.Update_Profile_View.as_view(),name = "profile_update"),
    path("job_detail/<int:pk>",views.JobDetailView.as_view(),name = "job_detail"),
    path("apply_job/<int:pk>",views.JobApply.as_view(),name = "apply_job"),
    path("applied_job/<int:pk>",views.Applied_jobs.as_view(),name = "applied_job"),
    path("delete_job/<int:pk>",views.Delete_Job.as_view(),name = "delete_job"),

   


]