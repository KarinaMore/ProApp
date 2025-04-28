from django.contrib import admin
from django.urls import path
from.import views
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('customer_home/', views.customer_home,name='customer_home'),
    path('customer_reg/', views.customer_reg,name='customer_reg'),
    path('manage_customer/', views.manage_customer, name='manage_customer'),
    path('customer_menu_card/', views.customer_menu_card,name='customer_menu_card'),
    path('customer_help/', views.customer_help, name='customer_help'),
    path('delete_customer/<int:id>',views.delete_customer, name='delete_customer'),
    path('customer_user_login/',views.customer_user_login, name='customer_user_login'),
    path('logout_view2/',views.logout_view2, name='logout_view2'),
    path('customerleadpanel_tab/',views.customerleadpanel_tab, name='customerleadpanel_tab')
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
