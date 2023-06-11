"""sih_project URL Configuration

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
from django.urls import path, include
from sih_app import views, utils
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.firstpage,name="1stpage.html"),
    path('home/',views.home,name="homepage.html"),
    path('refresh/',utils.my_custom_sql),
    path('db',views.db,name="db.html"),
    path('op/',views.op_view,name="op.html"),
    path('search_aadhar/',views.search_aadhar,name="search_aadhar.html"),
    path('check/',views.take_values,name="select1.html"),
    path('nsap_db/',views.view_nsap_db,name="op_db.html"),
    path('edit/<int:id>/',views.edit,name="edit_db.html"),
    path('update/<int:id>/',views.update,name="edit_db.html"),
    path('add_nsap/',views.add_nsap,name="add_db.html"),
    path('other_db/',views.view_other_db,name="op_other.html"),
    path('edit_other/<int:id>/',views.edit_other,name="edit_other_db.html"),
    path('update_other/<int:id>/',views.update_other,name="edit_other_db.html"),
    path('op_with_subdiv/',views.take_values1,name="op.html"),
    path('add_other/',views.add_other,name="add_other_db.html"),
    path('login/',views.login,name="login.html"),
    path('signup/',views.signup,name="signup.html"),
    path('csv/',views.download_csv_data),
    path('duplicate/',views.duplicate_nsap,name="duplicate_data.html"),
    path('edit_duplicate/<str:aadhar>',views.edit_dup_nsap,name="edit_success.html")

]
if settings.DEBUG:
    import debug_toolbar
    urlpatterns +=[
        path('__debug__/', include(debug_toolbar.urls)),
    ]
