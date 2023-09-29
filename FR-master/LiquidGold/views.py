from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from .models import DeiselReport, Site, SiteReport, DieselRequests, FuelTopUp, Profile
from .forms import NewRequestForm, SiteForm
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.core.mail import send_mail, EmailMessage, BadHeaderError
from django.conf import settings
from django.contrib import messages
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt, csrf_protect

@csrf_protect
def pending_list(request):
    topup_request = DieselRequests.objects.all_pending_requests()   
    return render(request, 'pending_list.html', {'pending_list':topup_request, 'title':'Diesel Request List - Pending Approval'})

@csrf_protect
def approved_list(request):
    topup_request = DieselRequests.objects.all_approved_requests()
    return render(request, 'approved_list.html', {'approved_list':topup_request, 'title':'Diesel Request List - Approved'})

@csrf_protect
@login_required
def ManagerAllocation(request, pk):
    manager = Profile.objects.get(id=pk)
    schedules = DieselRequests.objects.get(id=pk)
    req = []
    for schedule in schedules:
        if schedule.manager == manager:
            req.append(schedule.site)
    context = {
        'manager': manager,
        'requests': req,
    }
    return render(request, 'mgr_pending_list.html', {'pending_list':context})#ManagerAllocation

@login_required
def profile(request):
    return render(request, 'profile.html')
    

@csrf_protect
@login_required
def ManagerApproved(request, pk):
    manager = User.objects.get(id=pk)
    schedules = DieselRequests.objects.all()
    req = []
    for schedule in schedules:
        if schedule.User == manager:
            req.append(schedule.site)
    context = {
        'manager': manager,
        'requests': req,
    }
    return render(request, 'pending_list.html', context)

@csrf_protect
def approve_request(request, id):
    topup_request = get_object_or_404(DieselRequests, id=id) 
    place = topup_request.site
    thesite = Site.objects.filter(name = place)[0]
    topup_request.approve_request
    if topup_request.approve_request: #If a manager confirms, send a mail to Chike to give final approval
        subject='New Request awaiting Approval',
        fullmessage='A new request is awaiting approval',
        try:
                send_mail(
                    subject,
                    fullmessage,
                    settings.EMAIL_HOST_USER,
                    ['cukachukwu@starsightenergy.com'],
                    fail_silently=False   
                )
        except BadHeaderError:
            return HttpResponse("Invalid Header Found")
    
    return redirect('pending_requestlist') #'all_request_view', id=id

#########################################CTO########################################################################################
j=0
@csrf_protect
def cto_pending_list(request):
    topup_request = DieselRequests.objects.cto_all_pending_requests()
    i = topup_request.count()
    global j
    if i > j:
        subject = 'New Request for Diesel for Approval'
        fullmessage =  'Dear Sir, \n\
            A request for diesel is awaiting your review and approval. \n\
            Please click https://ssdr.azurewebsites.net/request/cto/pending/all to access request and approval. \n\
            Thank you.' 
        try:
            send_mail(
                    subject,
                    fullmessage,
                    settings.EMAIL_HOST_USER,
                    ['cukachukwu@starsightenergy.com'],
                    fail_silently=False   
                )
            j-=1
        
        except BadHeaderError:
            return HttpResponse("Invalid Header Found")
    
    return render(request, 'cto_pending_list.html', {'cto_pending_list':topup_request, 'title':'Diesel Request List - Pending Approval'})

@csrf_protect
def cto_approved_list(request):
    topup_request = DieselRequests.objects.cto_all_approved_requests()
    return render(request, 'cto_approved_list.html', {'cto_approved_list':topup_request, 'title':'Diesel Request List - Approved'})

@csrf_protect
def cto_approve_request(request, id):
    topup_request = get_object_or_404(DieselRequests, id=id) 
    place = topup_request.site
    thesite = Site.objects.filter(name = place)[0]
    topup_request.cto_approve_request
    #put a success message here to confirm approval 
    #messages.error(request, 'Diesel request approved for {0}'.format(thesite.name),extra_tags={"success"})
    return redirect('cto_pending_requestlist') #'all_request_view', id=id

@csrf_exempt
@login_required(login_url='/accounts/login/')
def cto_request_view(request, id):
   
    topup_request = get_object_or_404(DieselRequests, id = id)
    thesite = Site.objects.filter(name = topup_request.site)[0] #topup_request.site
    sitereport = FuelTopUp.objects.filter(site = topup_request.site).latest('top_up_date')
    sr = SiteReport.objects.filter(site_0 = topup_request.site)[0]
    
    return render(request, 'cto_request_detail_view.html', {
        'request_list':topup_request, 
        'site':thesite,
        'sitereport':sitereport,
        'sr':sr})

@csrf_protect
def cto_reject_request(request,id):
    #context = dict()
    topup_request = get_object_or_404(DieselRequests, id=id)
    place = topup_request.site
    thesite = Site.objects.filter(name = place)[0]
    topup_request.reject_request
    topup_request.delete() #request deleted when rejected
    #put a rejection message here to confirm reject 
    messages.error(request, 'Diesel request rejected for {0}'.format(thesite.name),extra_tags={"Reject"})
    return redirect('cto_pending_requestlist')

@csrf_protect
def cto_unapprove_request(request, id):
    topup_request = get_object_or_404(DieselRequests, id=id)
    topup_request.cto_unapprove_request
    return redirect('pending_requestlist')
############################################CTO#####################################################################################

@csrf_exempt
@login_required(login_url='/accounts/login/')
def request_view(request, id):
   
    topup_request = get_object_or_404(DieselRequests, id = id)
    thesite = Site.objects.filter(name = topup_request.site)[0] #topup_request.site
    sitereport = FuelTopUp.objects.filter(site = topup_request.site).latest('top_up_date')
    sr = SiteReport.objects.filter(site_0 = topup_request.site)[0]
    
    return render(request, 'request_detail_view.html', {
        'request_list':topup_request, 
        'site':thesite,
        'sitereport':sitereport,
        'sr':sr})

@csrf_protect
def reject_request(request,id):
    #context = dict()
    topup_request = get_object_or_404(DieselRequests, id=id)
    place = topup_request.site
    thesite = Site.objects.filter(name = place)[0]
    topup_request.reject_request
    topup_request.delete()
    #put a rejection message here to confirm reject 
    messages.error(request, 'Diesel request rejected for {0}'.format(thesite.name),extra_tags={"Reject"})
    return redirect('pending_requestlist')

@csrf_protect
def unapprove_request(request, id):
    topup_request = get_object_or_404(DieselRequests, id=id)
    topup_request.unapprove_request
    return redirect('pending_requestlist')


@csrf_protect
def request_rejected_list(request):
    context = dict()
    topup_request = DieselRequests.objects.all_rejected_requests()
    context['request_list_rejected'] = topup_request
    return render(request, 'rejected_request_list.html', context)

@csrf_protect
def unreject_request(request, id):
    topup_request = get_object_or_404(DieselRequests, id=id)
    topup_request.statuc = 'pending'
    topup_request.is_approved = False
    topup_request.save()
    messages.success(request, 'Request is now in the pending list', extra_tags = 'info')
    return redirect('request_rejected')

@csrf_protect
def SiteListView(request):
    siteform = SiteForm()
    so = Site.objects.all().order_by('name')
    # ro = SiteReport.objects.all()
    # do = FuelTopUp.objects.all()

    # report_list = zip(so, ro, do)

    return render(request, 'frontsheet.html', {'report_list': so, 'siteform': siteform})

@csrf_protect
def newRequestFormView(request, id=0):
    if request.method == "POST":
        if id == 0:
            siteform = SiteForm(request.POST)
            requestform = NewRequestForm(request.Post)
        else:
            site = Site.objects.get(id=id)
            siteform = SiteForm(request.POST, instance=site)
            requestform = NewRequestForm(request.POST)

        if siteform.is_valid() and requestform.is_valid():
               
            subject = ('New Request for Diesel')
            manager = request.POST.get('manager')
            
            for e in User.objects.filter(id = manager):
                manager_email = e.email
            body = {}
            
            fullmessage =  'Dear Sir, \n\
            A request for diesel is awaiting your review and approval. \n\
            Please click https://ssdr.azurewebsites.net/request/pending/all to access request and approval. \n\
            Thank you.' 
            try:
                send_mail(
                    subject,
                    fullmessage,
                    settings.EMAIL_HOST_USER,
                    [manager_email],
                    fail_silently=False   
                )
                
                requestform.save()
                
                
            except BadHeaderError:
                return HttpResponse("Invalid Header Found")
            return redirect('/')  # Points to the urls.py to list sheet

    else:

        if id == 0:
            siteform = SiteForm()
            requestform = NewRequestForm()
        else:
            site = Site.objects.get(id=id)
            siteform = SiteForm(instance=site)
            requestform = NewRequestForm()

            do = FuelTopUp.objects.filter(site__name=site).latest('top_up_date')
            # print(do)
            # print(site)

        return render(request, 'goldrequest.html', {
            'siteform': site,
            'requestform': requestform,
            'do': do})

@csrf_protect
def noc_approval_form_view(request, id=0):
    return render(request, 'noc_approval.html')

@csrf_protect
def cto_approval_form_view(request, id=0):
    return render(request, 'cto_approval.html')

@csrf_protect
def goldForm_view(request, id=0):
    form = NewRequestForm()
    r1 = Site.objects.all()  # getting all the Sites from Database
    r2 = SiteReport.objects.all()  # getti ng all the Site reports from Database
    r3 = DeiselReport.objects.all()  # getting all the Diesel report from Database
    return render(request, 'goldrequest.html', {
        "form": form,
        "r1": r1})

#@csrf_protect
#class CreateRequestView(CreateView):
   # model = DieselRequests
    #fields = ['site', 'site_name', 'request_date', 'request_quantity']


class SearchAppView(ListView):
    model = Site
    template_name = 'frontsheet.html'
    #context_object_name = 'all_search_results'

    def get_queryset(self):
       #result = super(SearchAppView, self).get_queryset()
       query = self.request.GET.get('search')
       object_list = Site.objects.filter(name__icontains=query)
        
       
           
       return object_list
