# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import MySQLdb
from django.db import connections
import subprocess #python execute commands
from pathlib import Path
import json
from datetime import datetime
from django.http import JsonResponse
import csv

def post_Vacancy_P(request,page):
	company_name_C = request.GET.get('company_name_C')
	account = request.GET.get('account')
	return render(request, '%s.html'%(page), locals())

def connect(request,page,page_value):

	today = datetime.now().strftime("%Y/%m/%d")

	cursor = connections['default'].cursor()
	cursor.execute("set names utf8")
	cursor.execute("SELECT * FROM `vacancy_table` WHERE `post_status`='true' AND ('%s' BETWEEN `publish_date_start` AND `publish_date_end`)"%today)
	vacancy_list = cursor.fetchall()
	vacancy_count = len(vacancy_list)

	return render(request, '%s.html'%(page), locals())

def vacancy_query(request,page):
	company_name_C = request.GET.get('company_name_C')
	vacancies = request.GET.get('vacancies')
	work_place = request.GET.get('work_place')
	work_time = request.GET.get('work_time')
	treatment = request.GET.get('treatment')
	publish_date_start = request.GET.get('publish_date_start')
	post_date = request.GET.get('post_date')

	cursor = connections['default'].cursor()
	cursor.execute("set names utf8")
	row_count = cursor.execute("SELECT * FROM `vacancy_table` WHERE `company_name_C` = '%s' AND `vacancies` = '%s' AND `work_place` = '%s' AND `work_time` = '%s' AND `treatment` = '%s' AND `publish_date_start` = '%s' AND `post_date` = '%s'"%(company_name_C,vacancies,work_place,work_time,treatment,publish_date_start,post_date))
	vacancy_detail = cursor.fetchall()[0] if row_count > 0 else ''

	return render(request, '%s.html'%(page), locals())

def register_table(request,page):

	company_name_C = request.POST['company_name_C']
	company_name_E = request.POST['company_name_E']
	principal = request.POST['principal']
	uniform_numbers = request.POST['uniform_numbers']
	URL = request.POST['URL']
	address = request.POST['address']

	unit = request.POST['unit']
	fill_in = request.POST['fill_in']
	job_title = request.POST['job_title']
	tel = request.POST['tel']
	email = request.POST['email']

	account = request.POST['account']
	password = request.POST['password']
	checkbox1 = request.POST['checkbox1']
	upload = request.POST['upload']

	cursor = connections['default'].cursor()
	cursor.execute("set names utf8")
	today = datetime.now().strftime("%Y/%m/%d")
	sql_value = [company_name_C,company_name_E,principal,uniform_numbers,URL,address,unit,fill_in,job_title,tel,email,account,password,checkbox1,upload,'false',today,'']
	sql_value = map(str,sql_value)
	sql_value = tuple(sql_value)

	cursor.execute("INSERT INTO `register_table` VALUES %s"%(sql_value,))

	cursor.close()

	return HttpResponse("")

def check_account(request,page):

	account = request.POST['account']
	password = request.POST['password']
	cursor = connections['default'].cursor()
	cursor.execute("set names utf8")
	cursor.execute("SELECT `company_name_C`,`account`,`password`,`review` FROM `register_table` WHERE `account`='%s' AND `password`='%s'"%(account,password))
	result = cursor.fetchall()
	if result != ():
		company_name_C = result[0][0]
		account = result[0][1]
		password = result[0][2]
		review = result[0][3]
		if review == 'true':
			check = 'login success||%s||%s'%(company_name_C,account)
		else:
			check = 'not review'
	else:
		check = 'account not exists'
	cursor.close()

	# return render(request, '%s.html'%(page), locals())
	return HttpResponse(check)

def company_list(request,page):

	cursor = connections['default'].cursor()
	cursor.execute("set names utf8")
	cursor.execute("SELECT `company_name_C`,`uniform_numbers`,`review`,`date`,`account` FROM `register_table`")
	result = list(cursor.fetchall())

	cursor.close()

	# return render(request, '%s.html'%(page), locals())
	return render(request, '%s.html'%(page), locals())

def company_review(request,page):
	company_name_C = request.GET.get('company_name_C')
	date = request.GET.get('date')
	account = request.GET.get('account')

	cursor = connections['default'].cursor()
	cursor.execute("set names utf8")
	cursor.execute("SELECT * FROM `register_table` WHERE `company_name_C` = '%s' AND `date` = '%s' AND `account` = '%s'"%(company_name_C,date,account))
	result = list(cursor.fetchall())[0]

	cursor.close()

	# return render(request, '%s.html'%(page), locals())
	return render(request, '%s.html'%(page), locals())

def review_success(request,page):
	company_name_C = request.POST['company_name_C']
	account = request.POST['account']
	password = request.POST['password']

	today = datetime.now().strftime("%Y/%m/%d")
	cursor = connections['default'].cursor()
	cursor.execute("set names utf8")
	cursor.execute("UPDATE `register_table` SET `review`='true',`review_date`='%s' WHERE `company_name_C` = '%s' AND `account` = '%s' AND `password`='%s'"%(today,company_name_C,account,password))
	# result = list(cursor.fetchall())[0]

	cursor.close()

	# return render(request, '%s.html'%(page), locals())
	return HttpResponse('')


def review_fail(request,page):
	company_name_C = request.POST['company_name_C']
	account = request.POST['account']
	password = request.POST['password']

	today = datetime.now().strftime("%Y/%m/%d")
	cursor = connections['default'].cursor()
	cursor.execute("set names utf8")
	cursor.execute("DELETE FROM `register_table` WHERE `company_name_C` = '%s' AND `account` = '%s' AND `password`='%s'"%(company_name_C,account,password))
	# result = list(cursor.fetchall())[0]

	cursor.close()

	# return render(request, '%s.html'%(page), locals())
	return HttpResponse('')

def company_info(request,page):
	company_name_C = request.GET.get('company_name_C')
	account = request.GET.get('account')

	cursor = connections['default'].cursor()
	cursor.execute("set names utf8")
	cursor.execute("SELECT *  FROM `register_table` WHERE `company_name_C` = '%s' AND `account` = '%s'"%(company_name_C,account))
	result = list(cursor.fetchall())[0]

	cursor.close()

	# return render(request, '%s.html'%(page), locals())
	return render(request, '%s.html'%(page), locals())

def register_edit(request,page):
	company_name_C = request.POST['company_name_C']
	company_name_E = request.POST['company_name_E']
	principal = request.POST['principal']
	uniform_numbers = request.POST['uniform_numbers']
	URL = request.POST['URL']
	address = request.POST['address']

	unit = request.POST['unit']
	fill_in = request.POST['fill_in']
	job_title = request.POST['job_title']
	tel = request.POST['tel']
	email = request.POST['email']

	account = request.POST['account']
	password = request.POST['password']
	checkbox1 = request.POST['checkbox1']
	upload = request.POST['upload']

	cursor = connections['default'].cursor()
	cursor.execute("set names utf8")
	cursor.execute("UPDATE `register_table` SET `company_name_C`='%s',`company_name_E`='%s',`principal`='%s',`uniform_numbers`='%s',`URL`='%s',`address`='%s',`unit`='%s',`fill_in`='%s',`job_title`='%s',`tel`='%s',`email`='%s',`account`='%s',`password`='%s',`checkbox1`='%s',`upload`='%s' WHERE `account` = '%s' AND `password`='%s'"%(company_name_C,company_name_E,principal,uniform_numbers,URL,address,unit,fill_in,job_title,tel,email,account,password,checkbox1,upload,account,password))
	# result = list(cursor.fetchall())[0]

	cursor.close()
	# return render(request, '%s.html'%(page), locals())
	return HttpResponse(company_name_C)

def vacancy_list(request,page):
	company_name_C = request.GET.get('company_name_C')
	account = request.GET.get('account')

	cursor = connections['default'].cursor()
	cursor.execute("set names utf8")
	row_count = cursor.execute("SELECT *  FROM `vacancy_table` WHERE `company_name_C` = '%s' AND `account` = '%s'"%(company_name_C,account))
	result = list(cursor.fetchall()) if row_count > 0 else ''

	cursor.close()

	# return render(request, '%s.html'%(page), locals())
	return render(request, '%s.html'%(page), locals())

def vacancy_list_admin(request,page):

	cursor = connections['default'].cursor()
	cursor.execute("set names utf8")
	row_count = cursor.execute("SELECT *  FROM `vacancy_table`")
	result = list(cursor.fetchall()) if row_count > 0 else ''

	cursor.close()

	# return render(request, '%s.html'%(page), locals())
	return render(request, '%s.html'%(page), locals())

def Vacancy_edit_page(request,page):
	company_name_C = request.GET.get('company_name_C')
	account = request.GET.get('account')
	vacancies = request.GET.get('vacancies')
	work_place = request.GET.get('work_place')
	work_time = request.GET.get('work_time')
	treatment = request.GET.get('treatment')
	publish_date_start = request.GET.get('publish_date_start')
	publish_date_end = request.GET.get('publish_date_end')

	# option_range = range(1,11)
	option_range = map(str,range(1,11))
	cursor = connections['default'].cursor()
	cursor.execute("set names utf8")
	row_count = cursor.execute("SELECT *  FROM `vacancy_table` WHERE `company_name_C` = '%s' AND `account` = '%s' AND `vacancies` = '%s' AND `work_place` = '%s' AND `work_time` = '%s' AND `treatment` = '%s' AND `publish_date_start` = '%s' AND `publish_date_end` = '%s'"%(company_name_C,account,vacancies,work_place,work_time,treatment,publish_date_start,publish_date_end))
	result = list(cursor.fetchall())[0] if row_count > 0 else ''

	cursor.close()

	# return render(request, '%s.html'%(page), locals())
	return render(request, '%s.html'%(page), locals())

def Vacancy_edit(request,page):
	company_name_C = request.POST['company_name_C'].strip()
	account = request.POST['account'].strip()

	vacancies_old = request.POST['vacancies_old'].strip()
	vacancies = request.POST['vacancies'].strip()
	work_place = request.POST['work_place'].strip()
	work_time = request.POST['work_time'].strip()
	treatment = request.POST['treatment'].strip()
	number_of_people = request.POST['number_of_people'].strip()
	wrok_content = request.POST['wrok_content'].strip()

	file1 = request.POST['file1'].strip()
	file2 = request.POST['file2'].strip()
	file3 = request.POST['file3'].strip()

	unit = request.POST['unit'].strip()
	fill_in = request.POST['fill_in'].strip()
	job_title = request.POST['job_title'].strip()
	tel = request.POST['tel'].strip()
	email = request.POST['email'].strip()
	unit_post = request.POST['unit_post'].strip()

	publish_date_start_old = request.POST['publish_date_start_old'].strip()
	publish_date_start = request.POST['publish_date_start'].strip()
	publish_date_end_old = request.POST['publish_date_end_old'].strip()
	publish_date_end = request.POST['publish_date_end'].strip()
	# option_range = range(1,11)
	option_range = map(str,range(1,11))
	cursor = connections['default'].cursor()
	cursor.execute("set names utf8")
	row_count = cursor.execute("UPDATE `vacancy_table` SET `vacancies`='%s',`work_place`='%s',`work_time`='%s',`treatment`='%s',`number_of_people`='%s',`wrok_content`='%s',`upload_file1`='%s',`upload_file2`='%s',`upload_file3`='%s',`unit`='%s',`fill_in`='%s',`job_title`='%s',`tel`='%s',`email`='%s',`publish_date_start`='%s',`publish_date_end`='%s',`unit_post` = '%s' WHERE `company_name_C` = '%s' AND `account` = '%s' AND `vacancies` = '%s' AND `publish_date_start` = '%s' AND `publish_date_end` = '%s'"%(vacancies,work_place,work_time,treatment,number_of_people,wrok_content,file1,file2,file2,unit,fill_in,job_title,tel,email,publish_date_start,publish_date_end,unit_post,company_name_C,account,vacancies_old,publish_date_start_old,publish_date_end_old))
	# result = list(cursor.fetchall())[0] if row_count > 0 else ''

	cursor.close()
	return HttpResponse('')	


def Vacancy_post(request,page):
	company_name_C = request.POST['company_name_C'].strip()
	account = request.POST['account'].strip()

	vacancies = request.POST['vacancies'].strip()
	publish_date_start = request.POST['publish_date_start'].strip()
	publish_date_end = request.POST['publish_date_end'].strip()

	option_range = map(str,range(1,11))
	cursor = connections['default'].cursor()
	cursor.execute("set names utf8")
	row_count = cursor.execute("UPDATE `vacancy_table` SET `post_status`='%s' WHERE `company_name_C` = '%s' AND `account` = '%s' AND `vacancies` = '%s' AND `publish_date_start` = '%s' AND `publish_date_end` = '%s'"%('true',company_name_C,account,vacancies,publish_date_start,publish_date_end))
	# result = list(cursor.fetchall())[0] if row_count > 0 else ''

	cursor.close()
	return HttpResponse('')	

def Vacancy_cancel(request,page):
	company_name_C = request.POST['company_name_C'].strip()
	account = request.POST['account'].strip()

	vacancies = request.POST['vacancies'].strip()
	publish_date_start = request.POST['publish_date_start'].strip()
	publish_date_end = request.POST['publish_date_end'].strip()

	option_range = map(str,range(1,11))
	cursor = connections['default'].cursor()
	cursor.execute("set names utf8")
	row_count = cursor.execute("UPDATE `vacancy_table` SET `post_status`='%s' WHERE `company_name_C` = '%s' AND `account` = '%s' AND `vacancies` = '%s' AND `publish_date_start` = '%s' AND `publish_date_end` = '%s'"%('false',company_name_C,account,vacancies,publish_date_start,publish_date_end))
	# result = list(cursor.fetchall())[0] if row_count > 0 else ''

	cursor.close()
	return HttpResponse('')	

def vacancy_P(request,page):
	
	company_name_C = request.POST['company_name_C'].strip()
	account = request.POST['account'].strip()

	vacancies = request.POST['vacancies'].strip()
	work_place = request.POST['work_place'].strip()
	work_time = request.POST['work_time'].strip()
	treatment = request.POST['treatment'].strip()
	number_of_people = request.POST['number_of_people'].strip()
	wrok_content = request.POST['wrok_content'].strip()

	file_name1 = request.POST['file_name1'].strip()
	file_name2 = request.POST['file_name2'].strip()
	file_name3 = request.POST['file_name3'].strip()

	unit = request.POST['unit'].strip()
	fill_in = request.POST['fill_in'].strip()
	job_title = request.POST['job_title'].strip()
	tel = request.POST['tel'].strip()
	email = request.POST['email'].strip()
	unit_post = request.POST['unit_post'].strip()

	publish_date_start = request.POST['publish_date_start'].strip()
	publish_date_end = request.POST['publish_date_end'].strip()

	today = datetime.now().strftime("%Y/%m/%d")
	cursor = connections['default'].cursor()
	cursor.execute("set names utf8")
	query_count = cursor.execute("SELECT `id` FROM `vacancy_table` ORDER BY `id` DESC LIMIT 1")
	if query_count == 0:
		row_count = 0
	else:
		row_count = cursor.fetchall()[0][0]
	sql_value = [int(row_count)+1,company_name_C,account,vacancies,work_place,work_time,treatment,number_of_people,wrok_content,file_name1,file_name2,file_name3,unit,fill_in,job_title,tel,email,publish_date_start,publish_date_end,'true',today,unit_post]
	sql_value = map(str,sql_value)
	sql_value = tuple(sql_value)

	query_count_log = cursor.execute("SELECT `id` FROM `vacancy_log` ORDER BY `id` DESC LIMIT 1")
	if query_count_log == 0:
		row_count_log = 0
	else:
		row_count_log = cursor.fetchall()[0][0]
	sql_value_log = [int(row_count_log)+1,company_name_C,account,vacancies,work_place,work_time,treatment,number_of_people,wrok_content,file_name1,file_name2,file_name3,unit,fill_in,job_title,tel,email,publish_date_start,publish_date_end,'true',today,unit_post,'POST',today,account]
	sql_value_log = map(str,sql_value_log)
	sql_value_log = tuple(sql_value_log)

	cursor.execute("INSERT INTO `vacancy_table` VALUES %s"%(sql_value,))
	cursor.execute("INSERT INTO `vacancy_log` VALUES %s"%(sql_value_log,))
	# result = list(cursor.fetchall())[0] if row_count > 0 else ''

	cursor.close()

	# return render(request, '%s.html'%(page), locals())
	return HttpResponse('')

def subquery_company_admin(request,page):

	select = request.POST['select'].strip()
	uniform_numbers = request.POST['uniform_numbers'].strip()
	company_name_C = request.POST['company_name_C'].strip()
	select = select if select != 'ALL' else ''

	cursor = connections['default'].cursor()
	cursor.execute("set names utf8")
	sql_flag = 0
	sql = "SELECT * FROM `register_table`";
	if select != '':
		if sql_flag == 0 :
			sql += "WHERE `review`='%s'"%(select)
		else:
			sql += " AND `review`='%s'"%(select)
		sql_flag = 1

	if uniform_numbers != '':
		if sql_flag == 0 :
			sql += "WHERE `uniform_numbers`='%s'"%(uniform_numbers)
		else:
			sql += " AND `uniform_numbers`='%s'"%(uniform_numbers)
		sql_flag = 1

	if company_name_C != '':
		if sql_flag == 0 :
			sql += "WHERE `company_name_C`='%s'"%(company_name_C)
		else:
			sql += " AND `company_name_C`='%s'"%(company_name_C)
		sql_flag = 1
	row_count =cursor.execute(sql)
	result = cursor.fetchall()
	return render(request, '%s.html'%(page), locals())
	# return HttpResponse('')

def subquery_vacancy_admin(request,page):

	publish_date_start = request.POST['publish_date_start'].strip()
	publish_date_end = request.POST['publish_date_end'].strip()
	select = request.POST['select'].strip()
	vacancies = request.POST['vacancies'].strip()
	select = select if select != 'ALL' else ''

	cursor = connections['default'].cursor()
	cursor.execute("set names utf8")
	sql_flag = 0
	sql = "SELECT * FROM `vacancy_table`";
	if publish_date_start != '':
		if sql_flag == 0 :
			sql += "WHERE `publish_date_start`>='%s'"%(publish_date_start)
		else:
			sql += " AND `publish_date_start`>='%s'"%(publish_date_start)
		sql_flag = 1

	if publish_date_end != '':
		if sql_flag == 0 :
			sql += "WHERE `publish_date_end`<='%s'"%(publish_date_end)
		else:
			sql += " AND `publish_date_end`<='%s'"%(publish_date_end)
		sql_flag = 1

	if select != '':
		if sql_flag == 0 :
			sql += "WHERE `post_status`='%s'"%(select)
		else:
			sql += " AND `post_status`='%s'"%(select)
		sql_flag = 1

	if vacancies != '':
		if sql_flag == 0 :
			sql += "WHERE `vacancies`='%s'"%(vacancies)
		else:
			sql += " AND `vacancies`='%s'"%(vacancies)
		sql_flag = 1

	row_count =cursor.execute(sql)
	result = cursor.fetchall()
	return render(request, '%s.html'%(page), locals())

def subquery_vacancy(request,page):

	company_name_C = request.POST['company_name_C'].strip()
	account = request.POST['account'].strip()
	publish_date_start = request.POST['publish_date_start'].strip()
	publish_date_end = request.POST['publish_date_end'].strip()
	select = request.POST['select'].strip()
	vacancies = request.POST['vacancies'].strip()
	select = select if select != 'ALL' else ''

	cursor = connections['default'].cursor()
	cursor.execute("set names utf8")
	sql_flag = 0
	sql = "SELECT * FROM `vacancy_table` WHERE `company_name_C`='%s' AND `account`='%s'"%(company_name_C,account)
	if publish_date_start != '':
		sql += " AND `publish_date_start`>='%s'"%(publish_date_start)

	if publish_date_end != '':
		sql += " AND `publish_date_end`<='%s'"%(publish_date_end)

	if select != '':
		sql += " AND `post_status`='%s'"%(select)

	if vacancies != '':
		sql += " AND `vacancies`='%s'"%(vacancies)

	row_count =cursor.execute(sql)
	result = cursor.fetchall()
	return render(request, '%s.html'%(page), locals())

def del_company(request):
	file = request.POST.getlist('file[]')
	cursor = connections['default'].cursor()
	cursor.execute("set names utf8")
	for company_info in file:
		file_array = company_info.split('|')
		company_name_C = file_array[0]
		uniform_numbers = file_array[1]
		date = file_array[2]

		cursor.execute("DELETE FROM `register_table` WHERE `company_name_C` = '%s' AND `uniform_numbers` = '%s' AND `date`='%s'"%(company_name_C,uniform_numbers,date))

	cursor.close()
	return HttpResponse('')

def del_vacancy(request):
	file = request.POST.getlist('file[]')
	page = request.POST['page']

	cursor = connections['default'].cursor()
	cursor.execute("set names utf8")
	for company_info in file:
		file_array = company_info.split('|')
		company_name_C = file_array[0]
		account = file_array[1]
		vacancies = file_array[2]
		publish_date_start = file_array[3]
		publish_date_end = file_array[4]

		query_count_log = cursor.execute("SELECT `id` FROM `vacancy_log` ORDER BY `id` DESC LIMIT 1")
		if query_count_log == 0:
			row_count_log = 0
		else:
			row_count_log = cursor.fetchall()[0][0]
			
		if page == 'Vacancy_M':
			who_action = account
		elif page == 'Vacancy_M_admin':
			who_action = 'admin'

		row_count = cursor.execute("SELECT * FROM `vacancy_table` WHERE `company_name_C` = '%s' AND `account` = '%s' AND `vacancies`='%s' AND `publish_date_start`='%s' AND `publish_date_end`='%s'"%(company_name_C,account,vacancies,publish_date_start,publish_date_end))
		result = list(cursor.fetchall())[0] if row_count > 0 else ''
		result = list(result)
		result[0] = row_count_log +1 
		result = tuple(result)
		today = datetime.now().strftime("%Y/%m/%d")
		sql_value_log = result + ('DEL',today,who_action,)
		print(result)
		cursor.execute("INSERT INTO `vacancy_log` VALUES %s"%(sql_value_log,))

		cursor.execute("DELETE FROM `vacancy_table` WHERE `company_name_C` = '%s' AND `account` = '%s' AND `vacancies`='%s' AND `publish_date_start`='%s' AND `publish_date_end`='%s'"%(company_name_C,account,vacancies,publish_date_start,publish_date_end))


		cursor.close()
	return HttpResponse('')

def download(request):
	from django.http import StreamingHttpResponse
	import urllib.parse
	folder = request.GET.get('folder')
	filename = request.GET.get('filename')

	def file_iterator(file_name, chunk_size=512):
		with open(file_name,'rb') as f: #'rb'以二進制模式打開
			while True:
				c = f.read(chunk_size)
				if c:
					yield c
				else:
					break
	the_file_name = filename
	file_path = '/home/career/Django/Recruit_project/mediafiles/%s/%s'%(folder,filename)
	response = StreamingHttpResponse(file_iterator(file_path))
	response['Content-Type'] = 'application/octet-stream'

	clientSystem = request.META['HTTP_USER_AGENT']#判斷瀏覽器
	if 'Edge' in clientSystem:
		the_file_name = urllib.parse.quote_plus(the_file_name);#IE編碼
	else:
		the_file_name = the_file_name.encode('utf-8').decode('ISO-8859-1')#chrome編碼

	response['Content-Disposition'] = 'attachment;filename=%s'%the_file_name
	return response

	# from django.utils.encoding import smart_str

	# response = HttpResponse(content_type='application/force-download') # mimetype is replaced by content_type for django 1.7
	# response['Content-Disposition'] = "attachment; filename=%s" % smart_str(the_file_name.encode('utf-8'))
	# response['X-Sendfile'] = smart_str(file_path)
	# return response
	# return HttpResponse('')

def sendmail_post_register(request):

	company_name_C = request.POST['company_name_C'].strip()
	date = request.POST['date'].strip()
	uniform_numbers = request.POST['uniform_numbers'].strip()

	import smtplib
	from email.mime.text import MIMEText

	info = '管理者 您好：\n企業求才網站，已於%s新增一筆企業審核申請，請至網站審核。\n'%(date)
	info += '企業名稱: %s , 統一編號: %s\n經濟部─公司及分公司基本資料查詢:http://gcis.nat.gov.tw/pub/cmpy/cmpyInfoListAction.do'%(company_name_C,uniform_numbers)
	msg = MIMEText(info)

	msg["From"] = "z10410059@email.ncku.edu.tw"
	msg["To"] = "z10410059@email.ncku.edu.tw"
	msg["Subject"] = "企業審核通知"
	

	server = smtplib.SMTP("email.ncku.edu.tw",25) #http://cc.ncku.edu.tw/files/15-1255-104206,c10184-1.php?Lang=zh-tw
	server.starttls()
	server.ehlo_or_helo_if_needed()
	try:
		failed = server.sendmail("z10410059@email.ncku.edu.tw","z10410059@email.ncku.edu.tw", msg.as_string())
		server.close()
	except Exception as e:
		print(e)

	return HttpResponse('')

def sendmail_success_register(request):

	company_name_C = request.POST['company_name_C'].strip()
	company_email = request.POST['email'].strip()

	import smtplib
	from email.mime.text import MIMEText

	info = '%s(企業) 您好\n貴公司申請使用本組求才訊息網站已開通權限，提醒您至求才網站刊登職缺，謝謝。\n'%(company_name_C)
	info += '成功大學企業求才網: http://career.osa.ncku.edu.tw/career/Login/\n\n順頌商祺\n成功大學生涯發展與就業輔導組'
	msg = MIMEText(info)

	msg["From"] = "z10410059@email.ncku.edu.tw"
	msg["To"] = company_email
	msg["Subject"] = "審核通知"

	server = smtplib.SMTP("email.ncku.edu.tw",25) #http://cc.ncku.edu.tw/files/15-1255-104206,c10184-1.php?Lang=zh-tw
	server.starttls()
	server.ehlo_or_helo_if_needed()
	try:
		failed = server.sendmail("z10410059@email.ncku.edu.tw",company_email, msg.as_string())
		server.close()
	except Exception as e:
		print(e)

	return HttpResponse('')

def passwd_edit(request):

	new_password1 = request.POST['new_password1']
	new_password2 = request.POST['new_password2']

	company_name_C = request.POST['company_name_C']
	company_name_E = request.POST['company_name_E']
	account = request.POST['account']
	password = request.POST['password']

	cursor = connections['default'].cursor()
	cursor.execute("set names utf8")
	cursor.execute("UPDATE `register_table` SET `password`='%s' WHERE `company_name_C` = '%s' AND `company_name_E` = '%s' AND `account` = '%s' AND `password`='%s'"%(new_password1,company_name_C,company_name_E,account,password))
	# result = list(cursor.fetchall())[0]

	cursor.close()

	# return render(request, '%s.html'%(page), locals())
	return HttpResponse('')

def C_V_log_download(request):

	download_data_type = request.POST['download_data_type']
	publish_date_start_download = request.POST['publish_date_start_download']
	publish_date_end_download = request.POST['publish_date_end_download']
	record_type1 = request.POST['record_type1']
	record_type2 = request.POST['record_type2']

	today = datetime.now().strftime("%Y/%m/%d")

	cursor = connections['default'].cursor()
	cursor.execute("set names utf8")

	if download_data_type == 'company_data_download':
		file_name = '%s_%s~%s.csv'%('廠商資料',publish_date_start_download.replace('/',''),publish_date_end_download.replace('/',''))
	else:
		file_name = '%s_%s~%s.csv'%('職缺資料',publish_date_start_download.replace('/',''),publish_date_end_download.replace('/',''))

	file_path = '/home/career/Django/Recruit_project/mediafiles/download/%s'%(file_name)
	f = open(file_path, 'w',encoding='utf-8-sig')
	w = csv.writer(f)
	if download_data_type == 'company_data_download':
		title = [['公司名稱(中文)','公司名稱(英文)','負責人','統一編號','公司網址','公司地址','填寫單位','填寫人','職稱','連絡電話','Email','附檔','審核通過','註冊時間','審核通過時間']]
		if record_type1 == 'company_now_post':
			sql = "SELECT DISTINCT `company_name_C` FROM `vacancy_table` WHERE (`post_status` = 'true') AND (`post_date` BETWEEN '%s' AND '%s')"%(publish_date_start_download,publish_date_end_download)
			cursor.execute(sql)
			company_name_C = [x[0] for x in cursor.fetchall()]
			company_name_C = list(map(lambda x:"`company_name_C` = '"+x+"'",company_name_C))
			company_name_C = ' OR '.join(company_name_C)

			sql2 = "SELECT `company_name_C`,`company_name_E`,`principal`,`uniform_numbers`,`URL`,`address`,`unit`,`fill_in`,`job_title`,`tel`,`email`,`upload`,`review`,`date`,`review_date` FROM `register_table` WHERE %s"%(company_name_C)
			cursor.execute(sql2)
			download_data = list(cursor.fetchall())

		elif record_type1 == 'company_once_post':
			sql = "SELECT DISTINCT `company_name_C` FROM `vacancy_log` WHERE (`action` = 'POST') AND (`action_date` BETWEEN '%s' AND '%s')"%(publish_date_start_download,publish_date_end_download)
			cursor.execute(sql)
			company_name_C = [x[0] for x in cursor.fetchall()]
			company_name_C = list(map(lambda x:"`company_name_C` = '"+x+"'",company_name_C))
			company_name_C = ' OR '.join(company_name_C)

			sql2 = "SELECT `company_name_C`,`company_name_E`,`principal`,`uniform_numbers`,`URL`,`address`,`unit`,`fill_in`,`job_title`,`tel`,`email`,`upload`,`review`,`date`,`review_date` FROM `register_table` WHERE %s"%(company_name_C)
			cursor.execute(sql2)
			download_data = list(cursor.fetchall())

		elif record_type1 == 'company_no_post':
			sql = "SELECT `company_name_C` FROM `register_table` WHERE `company_name_C` != 'admin'"
			cursor.execute(sql)
			company_list_all = [x[0] for x in cursor.fetchall()]

			sql = "SELECT DISTINCT `company_name_C` FROM `vacancy_table` WHERE (`post_status` = 'true') AND (`post_date` BETWEEN '%s' AND '%s')"%(publish_date_start_download,publish_date_end_download)
			cursor.execute(sql)
			company_list_post = [x[0] for x in cursor.fetchall()]
			company_list_neverpost = list(set(company_list_all).difference(set(company_list_post)))
			
			company_list_neverpost = list(map(lambda x:"`company_name_C` = '"+x+"'",company_list_neverpost))
			company_list_neverpost = ' OR '.join(company_list_neverpost)

			sql2 = "SELECT `company_name_C`,`company_name_E`,`principal`,`uniform_numbers`,`URL`,`address`,`unit`,`fill_in`,`job_title`,`tel`,`email`,`upload`,`review`,`date`,`review_date` FROM `register_table` WHERE %s"%(company_list_neverpost)
			cursor.execute(sql2)
			download_data = list(cursor.fetchall())

		elif record_type1 == 'company_all':
			sql = "SELECT `company_name_C`,`company_name_E`,`principal`,`uniform_numbers`,`URL`,`address`,`unit`,`fill_in`,`job_title`,`tel`,`email`,`upload`,`review`,`date`,`review_date` FROM `register_table` WHERE `company_name_C` != 'admin'"
			cursor.execute(sql)
			download_data = list(cursor.fetchall())

	elif download_data_type == 'vacancy_data_download':
		title = [['公司名稱(中文)','職缺項目','工作地點','工作時間','工作待遇','需求人數','工作內容(含應徵方式)','附檔1','附檔2','附檔3','填寫單位','填寫人','職稱','連絡電話','Email','刊登日期(起)','刊登日期(迄)','刊登狀態','刊登送出時間','是否將填寫單位資訊公布在職缺列表','刪除時間']]
		if record_type2 == 'vacancy_now_post':
			sql = "SELECT `company_name_C`,`vacancies`,`work_place`,`work_time`,`treatment`,`number_of_people`,`wrok_content`,`upload_file1`,`upload_file2`,`upload_file3`,`unit`,`fill_in`,`job_title`,`tel`,`email`,`publish_date_start`,`publish_date_end`,`post_status`,`post_date`,`unit_post` FROM `vacancy_table` WHERE (`post_status` = 'true') AND ((`publish_date_start` BETWEEN '%s' AND '%s') OR (`publish_date_end` BETWEEN '%s' AND '%s') OR (`publish_date_start` < '%s' AND `publish_date_end` > '%s'))"%(publish_date_start_download,publish_date_end_download,publish_date_start_download,publish_date_end_download,publish_date_start_download,publish_date_end_download)
			cursor.execute(sql)
			download_data = list(cursor.fetchall())
		elif record_type2 == 'vacancy_expired_post':
			sql = "SELECT `company_name_C`,`vacancies`,`work_place`,`work_time`,`treatment`,`number_of_people`,`wrok_content`,`upload_file1`,`upload_file2`,`upload_file3`,`unit`,`fill_in`,`job_title`,`tel`,`email`,`publish_date_start`,`publish_date_end`,`post_status`,`post_date`,`unit_post` FROM `vacancy_table` WHERE ('%s' > `publish_date_end`) AND (`publish_date_end` BETWEEN '%s' AND '%s')"%(today,publish_date_start_download,publish_date_end_download)
			cursor.execute(sql)
			download_data = list(cursor.fetchall())

		elif record_type2 == 'vacancy_del_post':
			sql = "SELECT `company_name_C`,`vacancies`,`work_place`,`work_time`,`treatment`,`number_of_people`,`wrok_content`,`upload_file1`,`upload_file2`,`upload_file3`,`unit`,`fill_in`,`job_title`,`tel`,`email`,`publish_date_start`,`publish_date_end`,`post_status`,`post_date`,`unit_post`,`action_date` FROM `vacancy_log` WHERE (`action` = 'DEL') AND (`action_date` BETWEEN '%s' AND '%s')"%(publish_date_start_download,publish_date_end_download)
			cursor.execute(sql)
			download_data = list(cursor.fetchall())
	w.writerows(title)	
	w.writerows(download_data)	
	f.close()
	cursor.close()

	return JsonResponse({'file_name':file_name})