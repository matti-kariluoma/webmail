from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django_localwebmail.webmail_data import webmail_forms
import imaplib, smtplib
import datetime
import re

def login(request):
	login_form = webmail_forms.LoginForm()
	return render_to_response(
		'main.html', 
		{ 
			'login_form': login_form,
		},
		context_instance=RequestContext(request)
	)

def mail(request, folder):
	if request.method == 'POST':
		login_form = webmail_forms.LoginForm(request.POST)
		if login_form.is_valid():
			username = login_form.cleaned_data['name']
			password = login_form.cleaned_data['password']

			mail = {}

			imap = imaplib.IMAP4() # localhost, port 143
			imap.login(username, password)
			imap.select(folder)
			(typ, data) = imap.search(None, 'ALL')
			for num in data[0].split():
				(typ, data) = imap.fetch(num, '(RFC822)')
				header_end = data[0][1].find('\r\n\r\n')
				message = ''
				raw_headers = []
				if header_end > 0:
					message = data[0][1][header_end+4:len(data[0][1])]
					raw_headers = data[0][1][0:header_end].split('\r\n')
				else:
					message = data[0][1]
					raw_headers = data[0][1].split('\r\n')

				headers = {}
				for line in raw_headers:
					pos_split = line.find(':')
					if pos_split > 0:
						headers[line[0:pos_split]] = line[pos_split+1:len(line)]
					else:
						headers[line] = line
				mail[num] = (headers,  message, data[0][1])
			imap.close()
			imap.logout()

			sorted_mail = [] # sort by date
			max_num = 0
			for i in mail.keys():
				if int(i) > max_num:
					max_num = int(i)
					
			mail_nums = range(max_num)
			mail_nums.sort(reverse=True)
			for i in mail_nums:
				try:
					sorted_mail.append(mail[str(i)])
				except KeyError:
					pass

			return render_to_response(
				'mail.html',
				{
					'mail': sorted_mail,
				},
				context_instance=RequestContext(request)
			)
	else:
		HttpResponseRedirect("/") # back to main page
