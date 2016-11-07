from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from forms import *
import logging
from models import *

def volunteer(request):
    template = 'volunteer.html'
    if request.method == 'POST':
        form = VolunteerForm(request.POST)
        if form.is_valid():
            logging.info(form.cleaned_data)
            body = "We have a new volunteer: \n name: %s\nphone: %s\nemail: %s\n heard: %s\navailability: %s"%(form.cleaned_data['name'],form.cleaned_data['phone_number'],form.cleaned_data['email'],form.cleaned_data['how_heard'],form.cleaned_data['free_time'])
            subject="New Volunteer!"
            to = ['chichildcareco@gmail.com']
            send_an_email(to,subject,body)

            req_obj = VolunteerRequest(**form.cleaned_data)
            req_obj.put()

            return render_to_response('thanks.html',context_instance=RequestContext(request))
    else:
        form = VolunteerForm()

    return render_to_response(template,{'form':form},context_instance=RequestContext(request))

def request_view(request):
    template = 'request.html'
    if request.method == 'POST':
        form = RequestForm(request.POST)
        if form.is_valid():
            logging.info(form.cleaned_data)
            for key in ['extra_provided','recurring']:
                form.cleaned_data[key] = ', '.join(form.cleaned_data[key])
            req_obj = ChildcareRequest(**form.cleaned_data)
            req_obj.put()
            body="Raw data dump of request is: %s"%str(form.cleaned_data)
            subject="New Childcare Request!"
            to = ['chichildcareco@gmail.com']
            send_an_email(to,subject,body)
            return render_to_response('thanks.html',context_instance=RequestContext(request))
    else:
        form = RequestForm()

    return render_to_response(template,{'form':form},context_instance=RequestContext(request))

def send_an_email(to,subject,body,sender='contact@chicagochildcarecollective.appspotmail.com'):
    try:
        mail.send_mail(sender=sender,to=to,subject=subject,body=body)
    except Exception as exc:
        logging.error("mail sending error! %s"%str(exc))
        pass

    
