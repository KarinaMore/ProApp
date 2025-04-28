from django.contrib import admin
from django.urls import path
from.import views
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home,name='home'),
    path('registration_user/', views.registration_user,name='registration_user'),
    path('user_login/', views.user_login,name='user_login'),
    path('agent_page/', views.agent_page, name='agent_page'),  
    path('menu_card/', views.menu_card,name='menu_card'),
    path('help_hire/', views.help_hire_view, name='help_hire'),
    path('manage_agent/', views.manage_agent, name='manage_agent'),
    path('success/', views.success, name='success'),
    path('delete/<int:id>',views.delete, name='delete'),
    path('view_profile/', views.view_profile, name='view_profile'),
    path('logout_view/', views.logout_view, name='logout_view'),
    path('change_username/', views.change_username, name='change_username'),
    path('change_password/', views.change_password, name='change_password'),
    path('delete_account/', views.delete_account, name='delete_account'),
    path('verify/', views.verify_token, name='verify_token'),
    path('account_settings/', views.account_settings, name='account_settings'),
    path('leadpanel_tab/', views.leadpanel_tab, name='leadpanel_tab'),

]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
