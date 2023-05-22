from django.urls import path

# from shinobiAPI.views.login_view import login_view
from .views import views_villages,views_nation, login_view

urlpatterns = [ 
    path('api/village', views_villages.village_list),
    path('api/village/<int:pk>', views_villages.village_details),
    path('api/nation', views_nation.nation_list),
    path('api/nation/<int:pk>', views_nation.nation_details),
    path('api/login', login_view.log_in),
    path('api/signup', login_view.sign_up),
]
