from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from django.urls import include


router = DefaultRouter()
router.register('tables', views.BookingViewSet)

urlpatterns = [
    path('restuarant/booking/', include(router.urls)),
    path('', views.index, name='index'),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    
]


