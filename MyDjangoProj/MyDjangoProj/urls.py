"""MyDjangoProj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include
from app1.views import ManagerSignIn,MangerLogin,EmployeeOpers,CreateEmployee,ManagerLogout,EmployeesList,UpdateEmployee





urlpatterns = (
    path('admin/', admin.site.urls),
    path('manager-signIn/', ManagerSignIn.as_view(),name='managersign'),
    path('manager_login/',MangerLogin.as_view(),name='manger_login'),
    path('create_employee/',CreateEmployee.as_view(),name='create_employee'),
    path('view_allemployees/',EmployeesList.as_view(),name='view_all'),
    path('update_employee/<pk>',UpdateEmployee.as_view(),name='upadate_emp'),




    path('manager-logout/',ManagerLogout.as_view(),name='managerlogout'),







    path('employee_opers/<pk>',EmployeeOpers.as_view(),name='employee_opers')
)
