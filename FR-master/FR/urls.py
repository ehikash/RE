"""FR URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from LiquidGold import views
from django.contrib.auth import views as auth_views
from LiquidGold.views import SearchAppView

urlpatterns = [
    path('admin/', admin.site.urls, name='adminlogin'),
    path('', views.SiteListView, name='sitelist'),
    path('<int:id>/', views.newRequestFormView, name='makerequest'),
    #path('approval/noc/<int:id>/', views.noc_approval_form_view, name='noc_approval'),
    #path('approval/cto/<int:id>/', views.cto_approval_form_view, name='cto_approval'),
    #path('request/', CreateRequestView.as_view(), name='VTU'),
    path('request/pending/all', views.pending_list, name='pending_requestlist'),
    path('request/approved/all', views.approved_list, name='approved_requestlist'),
    path('user/', views.ManagerAllocation, name='user_account'),
    path('request/mapaproved/<int:pk>/', views.ManagerApproved, name='mgr_approved'),
    
    #--------------------------------CT0--------------------------------------------#
    path('request/cto/pending/all', views.cto_pending_list, name='cto_pending_requestlist'),
    path('request/cto/approved/all', views.cto_approved_list, name='cto_approved_requestlist'),
    path('request/cto/unapprove/<int:id>/',views.cto_approve_request,name='cto_approve'),
    path('request/cto/all/view/<int:id>', views.cto_request_view, name='cto_all_request_view'),
    path('request/cto/reject/<int:id>', views.cto_reject_request, name='cto_reject'),
    path('request/cto/all/view/<int:id>', views.cto_request_view, name='cto_all_request_view'),
    path('request/cto/unapprove/<int:id>/',views.cto_unapprove_request,name='cto_requestunapprove'),
    
    #--------------------------------CTO--------------------------------------------#
    path('request/all/view/<int:id>', views.request_view, name='all_request_view'),
    path('request/reject/<int:id>', views.reject_request, name='reject'),
    path('request/approve/<int:id>', views.approve_request, name='approve'),
    path('request/unapprove/<int:id>/',views.unapprove_request,name='requestunapprove'),
    path('request/rejected/all', views.request_rejected_list, name='request_rejected'),
    path('request/unreject/<int:id>', views.unreject_request, name='unreject'),
    path('search/', SearchAppView.as_view(), name='search'),
    path('accounts/login/', auth_views.LoginView.as_view( next_page='pending_requestlist'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('user/profile/', views.profile, name='user_profile'),
]
