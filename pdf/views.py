from django.shortcuts import render
from .models import Profile
import pdfkit
from django.http import HttpResponse
from django.template import loader
import io
# Create your views here.
def index(request):
    if request.method == "POST":
        name = request.POST.get("name","")
        email = request.POST.get("email","")
        phone = request.POST.get("phone","")
        summary = request.POST.get("summary","")
        degree = request.POST.get("degree","")
        school = request.POST.get("school","")
        university = request.POST.get("university","")
        previous_work = request.POST.get("previous_work","")
        skills = request.POST.get("skills","")
        
        profile = Profile(name=name, email=email, phone=phone, summary=summary, degree=degree, school= school, university=university, previous_work=previous_work, skills=skills)
        profile.save()
    context = {}
    return render(request, 'pdf/accept.html', context)

def resume(request,id):
    pdf = Profile.objects.get(pk=id)
    template = loader.get_template('pdf/resume.html')
    html = template.render({'pdf':pdf})
    options = {
        'page-size' : 'A4',
        'encoding' : "UTF-8"
    }
    pdf2 = pdfkit.from_string(html,False,options)
    response = HttpResponse(pdf2, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment'
    filename = "resume.pdf"
    return response