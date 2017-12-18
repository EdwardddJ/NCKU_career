"""Recruit_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from webpage import views
from upload import views as upload

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^Login/$', views.connect,{'page': 'Login','page_value':''},name='Login'),
	url(r'^Register/$', views.connect,{'page': 'Register','page_value':'Register_value'},name='Register'),
    url(r'^check_account/$', views.check_account,{'page': 'Vacancy_M'},name='check_account'),
    url(r'^register_table/$', views.register_table,{'page': 'Home'},name='register_table'),

    url(r'^Company_info/$', views.company_info,{'page': 'Company_info'},name='Company_info'),
    url(r'^Company_info_admin/$', views.company_list,{'page': 'Company_info_admin'},name='Company_info_admin'),
    url(r'^Vacancy_M/$', views.vacancy_list,{'page': 'Vacancy_M'},name='Vacancy_M'),
    url(r'^Vacancy_M_admin/$', views.vacancy_list_admin,{'page': 'Vacancy_M_admin'},name='Vacancy_M_admin'),
    url(r'^Post_Vacancy_P/$', views.post_Vacancy_P,{'page': 'Vacancy_P'},name='Post_Vacancy_P'),
    url(r'^Vacancy_P/$', views.vacancy_P,{'page': 'Vacancy_P'},name='Vacancy_P'),
    url(r'^Vacancy_P_admin/$', views.connect,{'page': 'Vacancy_P_admin','page_value':'Vacancy_P_value'},name='Vacancy_P_admin'),

    url(r'^Company_review/$', views.company_review,{'page': 'Company_review'},name='Company_review'),
    url(r'^review_success/$', views.review_success,{'page': 'Company_review'},name='review_success'),
    url(r'^review_fail/$', views.review_fail,{'page': 'Company_review'},name='review_fail'),
    url(r'^register_edit/$', views.register_edit,{'page': 'Company_info'},name='register_edit'),
    url(r'^Vacancy_edit_page/$', views.Vacancy_edit_page,{'page': 'Vacancy_edit'},name='Vacancy_edit_page'),
    url(r'^Vacancy_edit_page_admin/$', views.Vacancy_edit_page,{'page': 'Vacancy_edit_admin'},name='Vacancy_edit_page_admin'),
    url(r'^Vacancy_edit/$', views.Vacancy_edit,{'page': 'Vacancy_edit'},name='Vacancy_edit'),
    url(r'^Vacancy_post/$', views.Vacancy_post,{'page': ''},name='Vacancy_post'),
    url(r'^Vacancy_cancel/$', views.Vacancy_cancel,{'page': ''},name='Vacancy_cancel'),
    url(r'^Vacancy_query/$', views.vacancy_query,{'page': 'Vacancy_query'},name='Vacancy_query'),
    url(r'^subquery_company_admin/$', views.subquery_company_admin,{'page': 'subquery_company_admin'},name='subquery_company_admin'),
    url(r'^subquery_vacancy/$', views.subquery_vacancy,{'page': 'subquery_vacancy'},name='subquery_vacancy'),
    url(r'^subquery_vacancy_admin/$', views.subquery_vacancy_admin,{'page': 'subquery_vacancy_admin'},name='subquery_vacancy_admin'),


    url(r'^upload_register/$', upload.upload_register,name='upload_register'),
    url(r'^keep_register_value/$', upload.keep_register_value,name='keep_register_value'),
    url(r'^upload_post1/$', upload.upload_post1,name='upload_post1'),
    url(r'^upload_post2/$', upload.upload_post2,name='upload_post2'),
    url(r'^upload_post3/$', upload.upload_post3,name='upload_post3'),
    url(r'^keep_post_value/$', upload.keep_post_value,name='keep_post_value'),
    url(r'^remove_file/$', upload.remove_file,name='remove_file'),
    url(r'^download/$', views.download,name='download'),

    url(r'^del_company/$', views.del_company,name='del_company'),
    url(r'^del_vacancy/$', views.del_vacancy,name='del_vacancy'),

    url(r'^sendmail_post_register/$', views.sendmail_post_register,name='sendmail_post_register'),
    url(r'^sendmail_success_register/$', views.sendmail_success_register,name='sendmail_success_register'),

    url(r'^passwd_edit/$', views.passwd_edit,name='passwd_edit'),
    url(r'^C_V_log_download/$', views.C_V_log_download,name='C_V_log_download'),
] 
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
