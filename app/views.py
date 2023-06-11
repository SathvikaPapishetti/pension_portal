from django.shortcuts import render, redirect, HttpResponse
from dateutil import relativedelta
import datetime
from sih_app.models import emp, otherdata, nsapdata, nopension
from datetime import date 
from django.contrib.auth.models import User
from django.db.models.expressions import RawSQL
from django.utils.timezone import now
import django_filters
from django.template import loader
import pdb; 
from sih_app.forms import nsapform, othersform, empform
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# Create your views here.
def firstpage(request):
    return render(request,"1stpage.html")
def home(request):
    return render(request,"homepage.html")
def db(request):
    return render(request,"db.html")

def check_old1(request):
    current = now().date()
    min_date = date(current.year - 60, current.month, current.day)
    max_date = date(current.year - 79, current.month, current.day)
    result =nopension.objects.filter(Dob__lte=min_date,Dob__gte=max_date)
    x=""
    for obj in result :
        x= x + (obj.aadhar)+" "
    return HttpResponse(x)
def check_old2(request):
    current = now().date()
    min_date = date(current.year - 80, current.month, current.day)
    result =nopension.objects.filter(Dob__lte=min_date)
    y=""
    for obj in result :
        y= y + (obj.aadhar)+" "
    return HttpResponse(y)

def check_pin(r,pin):

    if r=="Andaman and Nicobar Islands":
        if pin<=744304 and pin>=744101:
            return True
        else :
            return False
    elif r=="Andhra Pradesh":
        if pin<=535594 and pin>=507103:
            return True
        else :
            return False
    elif r=="Arunachal Pradesh":
        if pin<=792131 and pin>=790001:
            return True
        else :
            return False  
    elif r=="Assam":
        if pin<=788931 and pin>=781001:
            return True
        else :
            return False
    elif r=="Bihar":
        if pin<=855117 and pin>=800001:
            return True
        else :
            return False
    elif r=="Chandigarh":
        if pin<=160102 and pin>=140119:
            return True
        else :
            return False
    elif r=="Chattisgarh":
        if pin<=497778 and pin>=490001:
            return True
        else :
            return False
    elif r=="Dadra Nagar Haveli":
        if pin<=396240 and pin>=396193:
            return True
        else :
            return False
    elif r=="Daman Diu":
        if pin<=396220 and pin>=362520:
            return True
        else :
            return False
    elif r=="Delhi":
        if pin<=110097 and pin>=110001:
            return True
        else :
            return False
    elif r=="Goa":
        if pin<=403806 and pin>=403001:
            return True
        else :
            return False
    elif r=="Gujarat":
        if pin<=396590 and pin>=360001:
            return True
        else :
            return False
    elif r=="Haryana":
        if pin<=136156 and pin>=121001:
            return True
        else :
            return False
    elif r=="Himachal Pradesh":
        if pin<=177601 and pin>=171001:
            return True
        else :
            return False
    elif r=="Jammu Kashmir":
        if pin<=194404 and pin>=180001:
            return True
        else :
            return False
    elif r=="Jharkhand":
        if pin<=835325 and pin>=813208:
            return True
        else :
            return False
    elif r=="Karnataka":
        if pin<=591346 and pin>=560001:
            return True
        else :
            return False
    elif r=="Kerala":
        if pin<=6956115 and pin>=670001:
            return True
        else :
            return False
    elif r=="Lakshadweep":
        if pin<=682559 and pin>=682551:
            return True
        else :
            return False
    elif r=="Madhya Pradesh":
        if pin<=488448 and pin>=450001:
            return True
        else :
            return False
    elif r=="Maharashtra":
        if pin<=445402 and pin>=400001:
            return True
        else :
            return False
    elif r=="Manipur":
        if pin<=795159 and pin>=795001:
            return True
        else :
            return False
    elif r=="Meghalaya":
        if pin<=794115 and pin>=783123:
            return True
        else :
            return False
    elif r=="Mizoram":
        if pin<=796901 and pin>=796001:
            return True
        else :
            return False
    elif r=="Nagaland":
        if pin<=798627 and pin>=797001:
            return True
        else :
            return False
    elif r=="Odisha":
        if pin<=770076 and pin>=751001:
            return True
        else :
            return False
    elif r=="Pondicherry":
        if pin<=673310 and pin>=533464:
            return True
        else :
            return False
    elif r=="Punjab":
        if pin<=160104 and pin>=140001:
            return True
        else :
            return False
    elif r=="Rajasthan":
        if pin<=345034 and pin>=301001:
            return True
        else :
            return False
    elif r=="Sikkim":
        if pin<=737139 and pin>=737101:
            return True
        else :
            return False
    elif r=="Tamil Nadu":
        if pin<=643253 and pin>=600001:
            return True
        else :
            return False
    elif r=="Telangana":
        if pin<=509412 and pin>=500001:
            return True
        else :
            return False
    elif r=="Tripura":
        if pin<=799290 and pin>=799001:
            return True
        else :
            return False
    elif r=="Uttar Pradesh":
        if pin<=285223 and pin>=201001:
            return True
        else :
            return False
    elif r=="Uttarakhand":
        if pin<=385223 and pin>=201001:
            return True
        else :
            return False
    elif r=="West Bengal":
        if pin<=700001 and pin>=743711:
            return True
        else :
            return False
    else:
        False
@login_required(login_url='/login/')
def take_values(request):
    
    if request.method=="POST":
        pension_id= request.POST.get('pension')
        current = now().date()
        min_date = date(current.year - 60, current.month, current.day)
        max_date = date(current.year - 79, current.month, current.day)
        widow_min_age=date(current.year - 40, current.month, current.day)
        sub_pension=request.POST.get('subpension')
        
        if request.POST.get('state') and request.POST.get('st')=='0':
            r= request.POST.getlist('state')
            s=''
            for i in r:
                s= s+ 'and' +i 
            if pension_id=='1' and len(r)>1:
                result= nopension.objects.filter(state__in= r,Dob__lte=min_date).order_by('pincode','state')
                #return render(request,"op.html",{'np':result})
            elif pension_id=='1' and len(r)==1:
                area= request.POST.get('area')
                if area=='0':
                    pin= request.POST.get('pin')
                    result= nopension.objects.filter(state__in= r,Dob__lte=min_date,pincode=pin).order_by('aadhar')
                else :
                    result=nopension.objects.filter(state__in= r,Dob__lte=min_date).order_by('pincode')
            
            elif pension_id=='2' and len(r)>1:
                result= nopension.objects.filter(state__in= r,Dob__lte=widow_min_age,widow='yes').order_by('pincode','state')
                #return render(request,"op.html",{'np':result})
            elif pension_id=='2' and len(r)==1:
                area= request.POST.get('area')
                if area=='0':
                    pin= request.POST.get('pin')
                    result= nopension.objects.filter(state__in= r,Dob__lte=widow_min_age,pincode=pin,widow='yes').order_by('aadhar')
                else :
                    result=nopension.objects.filter(state__in= r,Dob__lte=widow_min_age,widow='yes').order_by('pincode')
            elif pension_id=='3' and len(r)>1:
                result= nopension.objects.filter(disability='yes',state__in=r).order_by('pincode','state')
            elif pension_id=='3' and len(r)==1 :
                area= request.POST.get('area')
                if area=='0':
                    pin= request.POST.get('pin')
                    result= nopension.objects.filter(state__in= r,disability='yes',pincode=pin).order_by('pincode','aadhar')
                else :
                    result=nopension.objects.filter(state__in= r,disability='yes').order_by('aadhar')                          
        elif request.POST.get('st')=='1':
            if pension_id=='1':
                result= nopension.objects.filter(Dob__lte=min_date).order_by('pincode','state')
            elif pension_id=='3':
                result=nopension.objects.filter(disability='yes').order_by('pincode','state')
            elif pension_id=='2':
                current = now().date()
                widow_min_age=date(current.year - 40, current.month, current.day)
                result= nopension.objects.filter(widow='yes',Dob__lte=widow_min_age)
        
        return render(request,"op.html",{'context':result})

    return render(request,"select.html")
from django.db import connection
from django.db import utils
from django.shortcuts import render, redirect, HttpResponse


@login_required(login_url='/login/')
def take_values1(request):
    
    if request.method=="POST":
        pension_id= request.POST.get('pension')
        current = now().date()
        min_date = date(current.year - 60, current.month, current.day)
        max_date = date(current.year - 79, current.month, current.day)
        widow_min_age=date(current.year - 40, current.month, current.day)
        sub_pension=request.POST.get('subpension')
        if sub_pension=="all":
            if request.POST.get('state') and request.POST.get('st')=='0':
                r= request.POST.getlist('state')
                s=''
                for i in r:
                    s= s+ 'and' +i 
                if pension_id=='1' and len(r)>1:
                    result= nopension.objects.filter(state__in= r,Dob__lte=min_date).order_by('pincode','state')
                #return render(request,"op.html",{'np':result})
                elif pension_id=='1' and len(r)==1:
                    area= request.POST.get('area')
                    if area=='0':
                        pin= request.POST.get('pin')
                        result= nopension.objects.filter(state__in= r,Dob__lte=min_date,pincode=pin).order_by('aadhar')
                    else :
                        result=nopension.objects.filter(state__in= r,Dob__lte=min_date).order_by('pincode')
            
                elif pension_id=='2' and len(r)>1:
                    result= nopension.objects.filter(state__in= r,Dob__lte=widow_min_age,widow='yes').order_by('pincode','state')
                #return render(request,"op.html",{'np':result})
                elif pension_id=='2' and len(r)==1:
                    area= request.POST.get('area')
                    if area=='0':
                        pin= request.POST.get('pin')
                        result= nopension.objects.filter(state__in= r,Dob__lte=widow_min_age,pincode=pin,widow='yes').order_by('aadhar')
                    else :
                        result=nopension.objects.filter(state__in= r,Dob__lte=widow_min_age,widow='yes').order_by('pincode')
                elif pension_id=='3' and len(r)>1:
                    result= nopension.objects.filter(disability='yes',state__in=r).order_by('pincode','state')
                elif pension_id=='3' and len(r)==1 :
                    area= request.POST.get('area')
                    if area=='0':
                        pin= request.POST.get('pin')
                        result= nopension.objects.filter(state__in= r,disability='yes',pincode=pin).order_by('pincode','aadhar')
                    else :
                        result=nopension.objects.filter(state__in= r,disability='yes').order_by('aadhar')                          
            elif request.POST.get('st')=='1':
                if pension_id=='1':
                    result= nopension.objects.filter(Dob__lte=min_date).order_by('pincode','state')
                elif pension_id=='3':
                    result=nopension.objects.filter(disability='yes').order_by('pincode','state')
                elif pension_id=='2':
                    current = now().date()
                    widow_min_age=date(current.year - 40, current.month, current.day)
                    result= nopension.objects.filter(widow='yes',Dob__lte=widow_min_age)
            return render(request,"op.html",{'context':result})
        if sub_pension=="1":
            if request.POST.get('state') and request.POST.get('st')=='0':
                r= request.POST.getlist('state')
                s=''
                for i in r:
                    s= s+ 'and' +i 
                if pension_id=='1' and len(r)>1:
                    result= nopension.objects.filter(state__in= r,Dob__lte=max_date).order_by('pincode','state')
                #return render(request,"op.html",{'np':result})
                elif pension_id=='1' and len(r)==1:
                    area= request.POST.get('area')
                    if area=='0':
                        pin= request.POST.get('pin')
                        result= nopension.objects.filter(state__in= r,Dob__lte=max_date,pincode=pin).order_by('aadhar')
                    else :
                        result=nopension.objects.filter(state__in= r,Dob__lte=max_date).order_by('pincode')
            
                elif pension_id=='2' and len(r)>1:
                    result= nopension.objects.filter(state__in= r,widow='yes',Dob__lte=max_date).order_by('pincode','state')
                #return render(request,"op.html",{'np':result})
                elif pension_id=='2' and len(r)==1:
                    area= request.POST.get('area')
                    if area=='0':
                        pin= request.POST.get('pin')
                        result= nopension.objects.filter(state__in= r,pincode=pin,widow='yes',Dob__lte=max_date).order_by('aadhar')
                    else :
                        result=nopension.objects.filter(state__in= r,widow='yes',Dob__lte=max_date).order_by('pincode')
                elif pension_id=='3' and len(r)>1:
                    result= nopension.objects.filter(disability='yes',state__in=r,Dob__lte=max_date).order_by('pincode','state')
                elif pension_id=='3' and len(r)==1 :
                    area= request.POST.get('area')
                    if area=='0':
                        pin= request.POST.get('pin')
                        result= nopension.objects.filter(state__in= r,disability='yes',pincode=pin,Dob__lte=max_date).order_by('pincode','aadhar')
                    else :
                        result=nopension.objects.filter(state__in= r,disability='yes',Dob__lte=max_date).order_by('aadhar')                          
            elif request.POST.get('st')=='1':
                if pension_id=='1':
                    result= nopension.objects.filter(Dob__lte=max_date).order_by('pincode','state')
                elif pension_id=='3':
                    result=nopension.objects.filter(disability='yes',Dob__lte=max_date).order_by('pincode','state')
                elif pension_id=='2':
                    current = now().date()
                    widow_min_age=date(current.year - 40, current.month, current.day)
                    result= nopension.objects.filter(widow='yes',Dob__lte=max_date)
            return render(request,"op.html",{'context':result})
        if sub_pension=="0":
            if request.POST.get('state') and request.POST.get('st')=='0':
                r= request.POST.getlist('state')
                s=''
                for i in r:
                    s= s+ 'and' +i 
                if pension_id=='1' and len(r)>1:
                    result= nopension.objects.filter(state__in= r,Dob__lte=min_date,Dob__gte=max_date).order_by('pincode','state')
                #return render(request,"op.html",{'np':result})
                elif pension_id=='1' and len(r)==1:
                    area= request.POST.get('area')
                    if area=='0':
                        pin= request.POST.get('pin')
                        result= nopension.objects.filter(state__in= r,Dob__lte=min_date,Dob__gte=max_date,pincode=pin).order_by('aadhar')
                    else :
                        result=nopension.objects.filter(state__in= r,Dob__lte=min_date,Dob__gte=max_date).order_by('pincode')
            
                elif pension_id=='2' and len(r)>1:
                    result= nopension.objects.filter(state__in= r,Dob__lte=widow_min_age,widow='yes',Dob__gte=max_date).order_by('pincode','state')
                #return render(request,"op.html",{'np':result})
                elif pension_id=='2' and len(r)==1:
                    area= request.POST.get('area')
                    if area=='0':
                        pin= request.POST.get('pin')
                        result= nopension.objects.filter(state__in= r,Dob__lte=widow_min_age,pincode=pin,widow='yes',Dob__gte=max_date).order_by('aadhar')
                    else :
                        result=nopension.objects.filter(state__in= r,Dob__lte=widow_min_age,widow='yes',Dob__gte=max_date).order_by('pincode')
                elif pension_id=='3' and len(r)>1:
                    result= nopension.objects.filter(disability='yes',state__in=r,Dob__gte=max_date).order_by('pincode','state')
                elif pension_id=='3' and len(r)==1 :
                    area= request.POST.get('area')
                    if area=='0':
                        pin= request.POST.get('pin')
                        result= nopension.objects.filter(state__in= r,disability='yes',pincode=pin,Dob__gte=max_date).order_by('pincode','aadhar')
                    else :
                        result=nopension.objects.filter(state__in= r,disability='yes',Dob__gte=max_date).order_by('aadhar')                          
            elif request.POST.get('st')=='1':
                if pension_id=='1':
                    result= nopension.objects.filter(Dob__lte=min_date,Dob__gte=max_date).order_by('pincode','state')
                elif pension_id=='3':
                    result=nopension.objects.filter(disability='yes',Dob__gte=max_date).order_by('pincode','state')
                elif pension_id=='2':
                    current = now().date()
                    widow_min_age=date(current.year - 40, current.month, current.day)
                    result= nopension.objects.filter(widow='yes',Dob__lte=widow_min_age,Dob__gte=max_date)
        
            return render(request,"op.html",{'context':result})
        return render(request,"op.html")

    return render(request,"select.html")

def op_view(request,context):
    return render(request,"op.html",context)
@login_required(login_url='/login/')
def view_nsap_db(request):
    nsap= nsapdata.objects.all()
    paginator = Paginator(nsap, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={'count':paginator.count,'page':page_obj}
    return render(request,'op_db.html',context)
@login_required(login_url='/login/')
def edit(request, id):
    getdetails=nsapdata.objects.get(id=id)
    return render(request,"edit_db.html",{'details':getdetails})
@login_required(login_url='/login/')
def update(request, id):
    updatedetails=nsapdata.objects.get(id=id)
    form=nsapform(request.POST, instance=updatedetails)
    if form.is_valid():
        form.save()
        messages.success(request,"Student record updated")
    return render(request,"edit_db.html",{'details':updatedetails})

@login_required(login_url='/login/')
def add_nsap(request):
    if request.method=="POST":
        if request.POST.get('aadhar_no') and request.POST.get('name') and request.POST.get('dob') and request.POST.get('pension_id') and request.POST.get('state')and request.POST.get('pincode') and request.POST.get('income') and request.POST.get('disability') and  request.POST.get('gender') and request.POST.get('status') and request.POST.get('widow'):
            details=nsapdata()
            details.aadhar_no=request.POST.get('aadhar_no')
            details.name=request.POST.get('name')
            details.dob=request.POST.get('dob')
            details.pension_id=request.POST.get('pension_id') 
            details.state=request.POST.get('state')
            details.pincode=request.POST.get('pincode')
            details.income=request.POST.get('income')
            details.disability=request.POST.get('disability')
            details.gender=request.POST.get('gender')
            details.status=request.POST.get('status')
            details.widow=request.POST.get('widow')
            details.bpl_family_id=request.POST.get('bpl_family_id')
            details.EPIC_id=request.POST.get('EPIC_id')
            details.faulty=request.POST.get('faulty')
            details.save()
            messages.success(request," The record added successfully")
            with connection.cursor() as cursor:
                cursor.execute("REFRESH MATERIALIZED VIEW nopension")
            return render(request,"add_db.html")
    else:
        return render(request,"add_db.html")

@login_required(login_url='/login/')
def view_other_db(request):
    other= otherdata.objects.all()
    paginator = Paginator(other, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={'count':paginator.count,'page':page_obj}
    return render(request,'op_other.html',context)
@login_required(login_url='/login/')
def edit_other(request, id):
    getdetails=otherdata.objects.get(id=id)
    return render(request,"edit_other_db.html",{'details':getdetails})
from django.template import loader
@login_required(login_url='/login/')
def update_other(request, id):
    o = otherdata.objects.get(id=id)
    template = loader.get_template('edit_other_db.html')
    context = {
        'mymember': o,
  }
    with connection.cursor() as cursor:
        cursor.execute("REFRESH MATERIALIZED VIEW nopension")
    return HttpResponse(template.render(context, request))

@login_required(login_url='/login/')
def add_other(request):
    if request.method=="POST":
        if request.POST.get('aadhar') and request.POST.get('Name') and request.POST.get('Dob') and  request.POST.get('state')and request.POST.get('pincode') and request.POST.get('income') and request.POST.get('disability') and  request.POST.get('gender') and request.POST.get('status') and request.POST.get('widow'):
            s=otherdata()
            s.aadhar=request.POST.get('aadhar')
            s.Name=request.POST.get('Name')
            s.income=request.POST.get('income')
            s.Dob=request.POST.get('Dob')
            s.state=request.POST.get('state')
            s.pincode=request.POST.get('pincode')
            s.disability=request.POST.get('disability')
            s.gender=request.POST.get('gender')
            s.status=request.POST.get('status')
            s.widow=request.POST.get('widow')
            s.bpl_family_id=request.POST.get('bpl_family_id')
            s.EPIC_id=request.POST.get('EPIC_id')
            s.faulty=request.POST.get('faulty')
            s.save()
            messages.success(request," The record added successfully")
            with connection.cursor() as cursor:
                cursor.execute("REFRESH MATERIALIZED VIEW nopension")
            return render(request,"add_other_db.html")
        else:
            return render(request,"add_other_db.html")

    else:
        return render(request,"add_other_db.html")
def search_aadhar(request):
    if request.method=="POST":
        current = now().date()
        min_date = date(current.year - 60, current.month, current.day)
        max_date = date(current.year - 79, current.month, current.day)
        widow_min_age=date(current.year - 40, current.month, current.day)
        a_no= request.POST.get('aadhar_no')
        if len(nsapdata.objects.filter(aadhar_no=a_no))==1:
            r=nsapdata.objects.filter(aadhar_no=a_no)
            messages.success(request,"RECEIVES PENSION.")
        elif len(otherdata.objects.filter(aadhar=a_no,Dob__lte=min_date))==1 :
            messages.success(request,"You are Eligible for IGNOAPS")
            
        elif len(otherdata.objects.filter(disability='yes',aadhar=a_no))==1:
            messages.success(request,"You are Eligible for IGNDPS")
            
        elif len(otherdata.objects.filter(widow='yes',Dob__lte=widow_min_age,aadhar=a_no))==1:
            messages.success(request,"You are Eligible for IGNWPS")
            
        elif len(nsapdata.objects.filter(aadhar_no=a_no))>1:
            messages.success(request,"your aadhar number is repeated in the pension database. Please go to our homepage for contact details for queries")
            
        elif len(otherdata.objects.filter(aadhar_no=a_no))>1:
            messages.success(request,"your aadhar number is repeated in the other database. Please go to our homepage for contact details for queries")
            
        else:
            messages.success(request,"You are not Eligible for NSAP pension")

        if len(nsapdata.objects.filter(aadhar_no=a_no))>1:
            messages.success(request,"your aadhar number is repeated in the pension database. Please go to our homepage for contact details for queries")
            
        if len(otherdata.objects.filter(aadhar=a_no))>1:
            messages.success(request,"your aadhar number is repeated in the other database. Please go to our homepage for contact details for queries")
        return render(request,"search_aadhar.html")
    else:
        return render(request,"search_aadhar.html")
   

def signup(request):
    if request.method=="POST":
        if request.POST.get('fname') and request.POST.get('lname') and request.POST.get('email') and request.POST.get('password'):
            emp1= emp()
            emp1.emp_fname= request.POST.get('fname')
            emp1.emp_lname=request.POST.get('lname')
            emp1.emp_email=request.POST.get('email')
            emp1.emp_password=request.POST.get('password')
            emp1.save()
            messages.success(request,"Signup successful")
            return render(request,"signup.html")
        else:
            return render(request,"signup.html")
    else:
        return render(request,"signup.html")

def login(request):
    if request.method=="POST":
        if request.POST.get('email') and request.POST.get('password'):
            mail=request.POST.get('email')
            password=request.POST.get('password')
            emp1= emp()
            r=emp.objects.filter(emp_email=mail,emp_password=password)
            if r:
                return redirect("/home/")
            else:
                return HttpResponse("Entered details are wrong.")
        else:
            return render(request,"login.html",{'alert':True})
    else:
        return render(request,"login.html")

import csv
from django.utils.encoding import smart_str


def download_csv_data(request):
	# response content type
	response = HttpResponse(content_type='text/csv')
	#decide the file name
	response['Content-Disposition'] = 'attachment; filename="ThePythonDjango.csv"'

	writer = csv.writer(response, csv.excel)
	response.write(u'\ufeff'.encode('utf8'))

	#write the headers
	writer.writerow([
		smart_str(u"Aadhar"),
		smart_str(u"Name"),
		smart_str(u"Dob"),
        smart_str(u"pension id"),
		smart_str(u"state"),
        smart_str(u"pincode"),
		smart_str(u"income"),
		smart_str(u"disability"),
		smart_str(u"gender"),
        smart_str(u"Status"),
        smart_str(u"widow"),
        smart_str(u"bpl_family_id"),
        smart_str(u"EPIC_id")
	])
	#get data from database or from text file....
	events = nsapdata.objects.all() #dummy function to fetch data
	for event in events:
		writer.writerow([
			smart_str(event.aadhar_no),
			smart_str(event.name),
			smart_str(event.dob),
            smart_str(event.pension_id),
			smart_str(event.state),
            smart_str(event.pincode),
			smart_str(event.income),
			smart_str(event.disability),
			smart_str(event.gender),
            smart_str(event.status),
            smart_str(event.widow),
            smart_str(event.bpl_family_id),
            smart_str(event.EPIC_id)
            
		])
	return response
from django.db.models import Count
from django.db.models import Max
def duplicate_nsap(request):
    #duplicate= nsapdata.objects.raw('SELECT aadhar_no,name,dob,pension_id,state,pincode,disability,gender,widow,faulty FROM nsapdata GROUP BY aadhar_no HAVING COUNT(aadhar_no) > %s',[1])
    #ids = nsapdata.objects.values('name', 'aadhar_no').annotate(Count('name')).order_by().filter(aadhar_no__count__gt=1).values_list("id", flat=True)
    #duplicate_objects = nsapdata.objects.filter(id__in=duplicate)
    duplicates=nsapdata.objects.values('aadhar_no','name','dob','gender')
    duplicates= duplicates.order_by()
    duplicates=duplicates.annotate(max_id=Max('id'),count_id=Count("id"))
    duplicates=duplicates.filter(count_id__gt=1)
    

    return render(request,"duplicate_data.html",{'c':duplicates})
from django.db import connection
def edit_dup_nsap(request,aadhar):
    nsapdata.objects.filter(aadhar_no=aadhar).update(faulty='1')
    return render(request,"edit_success.html")







	
	



