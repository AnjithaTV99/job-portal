from django.urls import path
from hr import views
urlpatterns = [
    path('signin/',views.LoginView.as_view(),name="signin"),
    path('index/',views.DashboardView.as_view(),name="index"),
    path('signout/',views.SignoutView.as_view(),name = "signout"),
    path('addcategory/',views.AddcategoryView.as_view(),name = "category"),
    path('category/<int:pk>',views.CategoryremoveView.as_view(),name = "del_category"),
    path('jobadd/',views.AddjobView.as_view(),name = "addjob"),
    path('jobdel/<int:pk>',views.DeljobView.as_view(),name='jobdel'),
    path('joblist/',views.JoblistView.as_view(),name='joblist'),
    path('jobedit/<int:pk>',views.JobupdateView.as_view(),name='edit'),
    path('jobdetails/<int:pk>',views.JobdetailsView.as_view(),name='details'),
]
    