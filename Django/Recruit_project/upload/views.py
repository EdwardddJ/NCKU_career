# -*- coding: utf-8 -*-
from django.shortcuts import render
# Create your views here.

from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse
from upload.models import Document,Document1,Document2,Document3
from upload.forms import DocumentForm
import json
import os

def upload_register(request):

	#https://stackoverflow.com/questions/5871730/need-a-minimal-django-file-upload-example
	
	# Handle file upload
	company_name_E = request.GET.get('company_name_E')
	if request.method == 'POST':
#-------------------------------
		from pathlib import Path
		my_file = Path("/home/career/Django/Recruit_project/upload/page_value/%s_%s"%('Register_value',company_name_E))
		if my_file.is_file():
			with open("/home/career/Django/Recruit_project/upload/page_value/%s_%s"%('Register_value',company_name_E)) as data_file:    
				data = json.load(data_file)

			company_name_C = data['company_name_C']
			company_name_E = data['company_name_E']
			principal = data['principal']
			uniform_numbers = data['uniform_numbers']
			URL = data['URL']
			address = data['address']
			unit = data['unit']
			fill_in = data['fill_in']
			job_title = data['job_title']
			tel = data['tel']
			email = data['email']
			account = data['account']
			password = data['password']
			checkbox1 = data['checkbox1']
		# else:
		# 	notexists='notexists'
#----------------------------------
		form = DocumentForm(request.POST, request.FILES)

		if form.is_valid():
			file_name = request.FILES['docfile']

			newdoc = Document(docfile = file_name)
			newdoc.save()
			# Redirect to the document upload_register after POST(成功時導向頁面)
			return render(request, "Register.html", locals())
			# return HttpResponseRedirect(reverse('Register2')) #由name='upload_register' 反推URL
	else:
		form = DocumentForm() # A empty, unbound form

	# Load documents for the upload_register page
	documents = Document.objects.all()

	# Render upload_register page with the documents and the form
	# return HttpResponse("")

	return render(request,
		'upload/upload_register.html',
		{'documents': documents, 'form': form,'company_name_E':company_name_E},
	)

def keep_register_value(request):

	company_name_C = request.POST['company_name_C'].strip()
	company_name_E = request.POST['company_name_E'].strip()
	principal = request.POST['principal'].strip()
	uniform_numbers = request.POST['uniform_numbers'].strip()
	URL = request.POST['URL'].strip()
	address = request.POST['address'].strip()

	unit = request.POST['unit'].strip()
	fill_in = request.POST['fill_in'].strip()
	job_title = request.POST['job_title'].strip()
	tel = request.POST['tel'].strip()
	email = request.POST['email'].strip()

	account = request.POST['account'].strip()
	password = request.POST['password'].strip()
	checkbox1 = request.POST['checkbox1'].strip() if request.POST['checkbox1'].strip() == 'true' else ''

	register_value = {
		'company_name_C':company_name_C,
		'company_name_E':company_name_E,
		'principal':principal,
		'uniform_numbers':uniform_numbers,
		'URL':URL,
		'address':address,
		'unit':unit,
		'fill_in':fill_in,
		'job_title':job_title,
		'tel':tel,
		'email':email,
		'account':account,
		'password':password,
		'checkbox1':checkbox1,

	}

	with open('/home/career/Django/Recruit_project/upload/page_value/Register_value_%s'%(company_name_E),'w') as outfile:
		json.dump(register_value, outfile)
	
	return HttpResponse("")

def upload_post(request):

	#https://stackoverflow.com/questions/5871730/need-a-minimal-django-file-upload-example
	
	# Handle file upload
	company_name_C = request.GET.get('company_name_C')
	if request.method == 'POST':
#-------------------------------
		from pathlib import Path
		my_file = Path("/home/career/Django/Recruit_project/upload/page_value/%s_%s"%('Post_value',company_name_C))
		if my_file.is_file():
			with open("/home/career/Django/Recruit_project/upload/page_value/%s_%s"%('Post_value',company_name_C)) as data_file:    
				data = json.load(data_file)

				company_name_C = data['company_name_C']
				account = data['account']

				vacancies = data['vacancies']
				work_place = data['work_place']
				work_time = data['work_time']
				treatment = data['treatment']
				number_of_people = int(data['number_of_people']) if data['number_of_people'] != '' else ''
				wrok_content = data['wrok_content']

				unit = data['unit']
				fill_in = data['fill_in']
				job_title = data['job_title']
				tel = data['tel']
				email = data['email']
				publish_date_start = data['publish_date_start']
				publish_date_end = data['publish_date_end']
				option_range = range(1,11)
		# else:
		# 	notexists='notexists'
#----------------------------------
		form = DocumentForm(request.POST, request.FILES)

		if form.is_valid():
			file_name = request.FILES['docfile']

			newdoc = Document(docfile = file_name)
			newdoc.save()
			# Redirect to the document upload_Post after POST(成功時導向頁面)
			return render(request, "Vacancy_P.html", locals())
			# return HttpResponseRedirect(reverse('Register2')) #由name='upload_register' 反推URL
	else:
		form = DocumentForm() # A empty, unbound form

	# Load documents for the upload_register page
	documents = Document.objects.all()

	# Render upload_register page with the documents and the form
	# return HttpResponse("")

	return render(request,
		'upload/upload_post.html',
		{'documents': documents, 'form': form,'company_name_C':company_name_C},
	)

def upload_post1(request):

	#https://stackoverflow.com/questions/5871730/need-a-minimal-django-file-upload-example
	
	# Handle file upload
	company_name_C = request.GET.get('company_name_C')
	if request.method == 'POST':
#-------------------------------
		from pathlib import Path
		my_file = Path("/home/career/Django/Recruit_project/upload/page_value/%s_%s"%('Post_value',company_name_C))
		if my_file.is_file():
			with open("/home/career/Django/Recruit_project/upload/page_value/%s_%s"%('Post_value',company_name_C)) as data_file:    
				data = json.load(data_file)

				company_name_C = data['company_name_C']
				account = data['account']

				vacancies = data['vacancies']
				work_place = data['work_place']
				work_time = data['work_time']
				treatment = data['treatment']
				number_of_people = int(data['number_of_people']) if data['number_of_people'] != '' else ''
				wrok_content = data['wrok_content']

				file_name2 = data['file_name2']
				file_name3 = data['file_name3']
				unit = data['unit']
				fill_in = data['fill_in']
				job_title = data['job_title']
				tel = data['tel']
				email = data['email']
				publish_date_start = data['publish_date_start']
				publish_date_end = data['publish_date_end']
				option_range = range(1,11)
		# else:
		# 	notexists='notexists'
#----------------------------------
		form = DocumentForm(request.POST, request.FILES)

		if form.is_valid():
			file_name1 = request.FILES['docfile']

			newdoc = Document1(docfile = file_name1)
			newdoc.save()
			# Redirect to the document upload_Post after POST(成功時導向頁面)
			return render(request, "Vacancy_P.html", locals())
			# return HttpResponseRedirect(reverse('Register2')) #由name='upload_register' 反推URL
	else:
		form = DocumentForm() # A empty, unbound form

	# Load documents for the upload_register page
	documents = Document.objects.all()

	# Render upload_register page with the documents and the form
	# return HttpResponse("")

	return render(request,
		'upload/upload_post1.html',
		{'documents': documents, 'form': form,'company_name_C':company_name_C},
	)

def upload_post2(request):

	#https://stackoverflow.com/questions/5871730/need-a-minimal-django-file-upload-example
	
	# Handle file upload
	company_name_C = request.GET.get('company_name_C')
	if request.method == 'POST':
#-------------------------------
		from pathlib import Path
		my_file = Path("/home/career/Django/Recruit_project/upload/page_value/%s_%s"%('Post_value',company_name_C))
		if my_file.is_file():
			with open("/home/career/Django/Recruit_project/upload/page_value/%s_%s"%('Post_value',company_name_C)) as data_file:    
				data = json.load(data_file)

				company_name_C = data['company_name_C']
				account = data['account']

				vacancies = data['vacancies']
				work_place = data['work_place']
				work_time = data['work_time']
				treatment = data['treatment']
				number_of_people = int(data['number_of_people']) if data['number_of_people'] != '' else ''
				wrok_content = data['wrok_content']

				file_name1 = data['file_name1']
				file_name3 = data['file_name3']
				unit = data['unit']
				fill_in = data['fill_in']
				job_title = data['job_title']
				tel = data['tel']
				email = data['email']
				publish_date_start = data['publish_date_start']
				publish_date_end = data['publish_date_end']
				option_range = range(1,11)
		# else:
		# 	notexists='notexists'
#----------------------------------
		form = DocumentForm(request.POST, request.FILES)

		if form.is_valid():
			file_name2 = request.FILES['docfile']

			newdoc = Document2(docfile = file_name2)
			newdoc.save()
			# Redirect to the document upload_Post after POST(成功時導向頁面)
			return render(request, "Vacancy_P.html", locals())
			# return HttpResponseRedirect(reverse('Register2')) #由name='upload_register' 反推URL
	else:
		form = DocumentForm() # A empty, unbound form

	# Load documents for the upload_register page
	documents = Document.objects.all()

	# Render upload_register page with the documents and the form
	# return HttpResponse("")

	return render(request,
		'upload/upload_post2.html',
		{'documents': documents, 'form': form,'company_name_C':company_name_C},
	)

def upload_post3(request):

	#https://stackoverflow.com/questions/5871730/need-a-minimal-django-file-upload-example
	
	# Handle file upload
	company_name_C = request.GET.get('company_name_C')
	if request.method == 'POST':
#-------------------------------
		from pathlib import Path
		my_file = Path("/home/career/Django/Recruit_project/upload/page_value/%s_%s"%('Post_value',company_name_C))
		if my_file.is_file():
			with open("/home/career/Django/Recruit_project/upload/page_value/%s_%s"%('Post_value',company_name_C)) as data_file:    
				data = json.load(data_file)

				company_name_C = data['company_name_C']
				account = data['account']

				vacancies = data['vacancies']
				work_place = data['work_place']
				work_time = data['work_time']
				treatment = data['treatment']
				number_of_people = int(data['number_of_people']) if data['number_of_people'] != '' else ''
				wrok_content = data['wrok_content']

				file_name1 = data['file_name1']
				file_name2 = data['file_name2']

				unit = data['unit']
				fill_in = data['fill_in']
				job_title = data['job_title']
				tel = data['tel']
				email = data['email']
				publish_date_start = data['publish_date_start']
				publish_date_end = data['publish_date_end']
				option_range = range(1,11)
		# else:
		# 	notexists='notexists'
#----------------------------------
		form = DocumentForm(request.POST, request.FILES)

		if form.is_valid():
			file_name3 = request.FILES['docfile']

			newdoc = Document3(docfile = file_name3)
			newdoc.save()
			# Redirect to the document upload_Post after POST(成功時導向頁面)
			return render(request, "Vacancy_P.html", locals())
			# return HttpResponseRedirect(reverse('Register2')) #由name='upload_register' 反推URL
	else:
		form = DocumentForm() # A empty, unbound form

	# Load documents for the upload_register page
	documents = Document.objects.all()

	# Render upload_register page with the documents and the form
	# return HttpResponse("")

	return render(request,
		'upload/upload_post3.html',
		{'documents': documents, 'form': form,'company_name_C':company_name_C},
	)

def keep_post_value(request):

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
	publish_date_start = request.POST['publish_date_start'].strip()
	publish_date_end = request.POST['publish_date_end'].strip()

	register_value = {
		'company_name_C':company_name_C,
		'account':account,

		'vacancies':vacancies,
		'work_place':work_place,
		'work_time':work_time,
		'treatment':treatment,
		'number_of_people':number_of_people,
		'wrok_content':wrok_content,

		'file_name1':file_name1,
		'file_name2':file_name2,
		'file_name3':file_name3,
		'unit':unit,
		'fill_in':fill_in,
		'job_title':job_title,
		'tel':tel,
		'email':email,
		'publish_date_start':publish_date_start,
		'publish_date_end':publish_date_end,

	}

	with open('/home/career/Django/Recruit_project/upload/page_value/Post_value_%s'%(company_name_C),'w') as outfile:
		json.dump(register_value, outfile)
	
	return HttpResponse("")

def remove_file(request):
	company_name_E = request.POST['company_name_E'].strip()
	import os
	file_path = '/home/career/Django/Recruit_project/upload/page_value/Register_value_%s'%(company_name_E)
	if os.path.exists(file_path):
		os.remove(file_path)
	return HttpResponse("")

# from django.views.decorators.csrf import csrf_exempt
# @csrf_exempt #解決Forbidden (CSRF token missing or incorrect.)
# def upload(request):
# 	if request.method =='GET':
# 		return render(request,'Register.html')
# 	if request.method == 'POST':

# 		file = request.FILES['file']
# 		import os
# 		# file_path = os.path.join('/home/career/Django/Recruit_project/static','upload',file.filename)
# 		print(file)
		
# 		with open(file.filename,'wb') as f:
# 			for temp in file.chunks():
# 				f.write(temp)
# 		return HttpResponse('ok') #原文網址：https://ifun01.com/87CS5FC.html
# 		# return render(request,'test.html')
