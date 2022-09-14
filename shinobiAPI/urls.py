from django.urls import path
from .views import views_villages,views_nation

urlpatterns = [ 
    path('api/village', views_villages.village_list),
    path('api/village/<int:pk>', views_villages.village_details),
    # path('api/villages/published', views.tutorial_list_published)
    path('api/nation', views_nation.nation_list),
    path('api/nation/<int:pk>', views_nation.nation_details),
]
