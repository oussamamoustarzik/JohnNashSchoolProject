from email.message import EmailMessage
from io import BytesIO
import os
from django.utils.timezone import make_aware,get_current_timezone
from django.shortcuts import render
from django.views import View
from .forms import *
from .models import *
from django.shortcuts import render,HttpResponse,redirect
from .forms import LoginAgent,LoginAdmin,LoginEleve,LoginParent,LoginProf
from .forms import *
from .models import *
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.messages import constants as messages
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import render,  get_object_or_404
from .forms import * 
from .models import *
from django.views.generic.edit import UpdateView
from django.views.generic import ListView, CreateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.http import Http404, JsonResponse,HttpResponseBadRequest
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from datetime import datetime
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Q
import datetime as dt
import random
import calendar
import datetime
from django.core.exceptions import ObjectDoesNotExist
from django.utils.text import slugify
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.utils.text import slugify
import datetime as dt
from django.shortcuts import render
from django.db.models import Avg, Sum
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Spacer, Table, TableStyle, Paragraph, Image
from django.contrib.auth.mixins import LoginRequiredMixin
####    HOMEPAGE     ####################
def home(request):
    return render(request,'pages\home.html')


def contact(request):
    return render(request,'pages\contact.html')

import datetime

def johnnash(request):
    student = Eleve.objects.count()
    prof=Professeur.objects.count()
    school = Ecole.objects.count()
    classes = Classe.objects.count()
    myDatetime = datetime.now().year
    annne_debut = 2020
    annee_expertise = myDatetime-annne_debut
    # print(annee_expertise)
    context={
        'student':student,
        'prof':prof,
        'school':school,
        'classes':classes,
        'annee_expertise':annee_expertise
    }
    return render(request,'pages\johnashschool.html',context)

def cursus(request):
    return render(request,'pages/cursus.html')

def schoolife(request):
    return render(request,'pages/schoolife.html')
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Spacer, Table, TableStyle, Paragraph, PageTemplate
from reportlab.lib import colors
from reportlab.platypus import Image
import io
from django.http import FileResponse

def Admission(request):
    if request.method == 'POST':
        form = AdmissionForm(request.POST)
        if form.is_valid():
            form.save()

            buffer = io.BytesIO()
            doc = SimpleDocTemplate(buffer, pagesize=letter)
            elements = []

            # Fetch the form data from the database
            admission_obj = form.instance
            nom = admission_obj.nom
            prenom = admission_obj.prenom
            cne = admission_obj.cne
            level = admission_obj.level
            age = admission_obj.age
            ancienne_ecole = admission_obj.ancienne_ecole

            styles = getSampleStyleSheet()
            title_style = styles['Title']
            heading_style = styles['Heading2']
            content_style = styles['BodyText']

            logo_path = 'C:\\Users\\DELL\\Desktop\\goo.png'
            logo = Image(logo_path, width=200, height=180)
            elements.append(logo)
            elements.append(Spacer(1, 20))

            data = [
                ['Nom', nom],
                ['Prénom', prenom],
                ['CNE', cne],
                ['Level', level],
                ['Age', age],
                ['Ancienne école', ancienne_ecole]
            ]

            table_style = TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 12),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
                ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
                ('FONTSIZE', (0, 1), (-1, -1), 10),
                ('ALIGN', (0, 1), (-1, -1), 'LEFT'),
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ])

            table = Table(data, colWidths=[150, 200], style=table_style)
            elements.append(table)
            elements.append(Spacer(1, 20))

            school_info = "Please bring this file when you come for registration in our school, thanks!"
            elements.append(Paragraph(school_info, content_style))

            # Add school information
            school_address = "123 School Street, City, Country"
            school_phone = "+123456789"
            school_email = "info@school.com"

            school_info_table_data = [
                ['School Address', school_address],
                ['Phone', school_phone],
                ['Email', school_email]
            ]

            school_info_table_style = TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
                ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
                ('FONTSIZE', (0, 1), (-1, -1), 10),
                ('ALIGN', (0, 1), (-1, -1), 'LEFT'),
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ])

            school_info_table = Table(school_info_table_data, colWidths=[150, 200], style=school_info_table_style)
            elements.append(Spacer(1, 20))
            elements.append(school_info_table)

            # Create the footer template
            def footer(canvas, doc):
                canvas.saveState()
                canvas.setFont('Helvetica', 8)
                canvas.drawString(inch, 0.75 * inch, "school_address: School Street, City, Country      school_phone : +123456789     school_email:  info@school.com ")
                canvas.restoreState()

            # Create the PDF document and set the footer template
            doc.build(elements, onFirstPage=footer, onLaterPages=footer)

            buffer.seek(0)

            return FileResponse(buffer, as_attachment=True, filename='admission_form.pdf')
    else:
        form = AdmissionForm()
    return render(request,'pages/admission.html', {'form': form})


def demande_recrutement(request):
    if request.method == 'POST':
        form = DemandeRecrutementForm(request.POST, request.FILES)
        if form.is_valid():
            demande = form.save()
            send_notification_email(demande)
            messages.success(request, 'Thank you for submitting your recruitment request! We will review your application and contact you soon.')
            return redirect('demande_recrutement')
    else:
        form = DemandeRecrutementForm()

    return render(request, 'pages/demande_recrutement.html', {'form': form})
from django.core.mail import EmailMessage

def send_notification_email(demande):
    subject = 'New recruitment request'
    message = f"A new recruitment request has been submitted.\n\nName: {demande.nom}\nRequest subject: {demande.request}"
    from_email = demande.email
    to_email = 'latifa.aloirradi12@gmail.com'

    email = EmailMessage(subject, message, from_email, [to_email])

    # Attach the CV file
    cv_file = open(demande.cv.path, 'rb')  # Open the CV file in binary mode
    email.attach(filename='cv.pdf', content=cv_file.read(), mimetype='application/pdf')
    cv_file.close()

    email.send()

#########   ESPACE lOGIN     ########################

def studentsp(request):
    form = LoginEleve()
    context = {'form': form}
    return render(request,'pages/loginstudent.html',context)

def parentsp(request):
    form = LoginParent()
    context = {'form': form}
    return render(request,'pages/loginparent.html',context)

def teachersp(request):
    form = LoginProf()
    context = {'form': form}
    return render(request,'pages/loginteacher.html',context)

def agentsp(request):
    form = LoginAgent()
    context = {'form': form}
    return render(request, 'pages/loginagent.html', context)
def adminsp(request):   
    form = LoginAdmin()
    context = {'form': form}
    return render(request,'pages/loginadmin.html',context)


def EleveElearning(request):
    id = request.session.get('id_user')
    print(id)
    return render(request,'Eleve/EleveElearning.html')


def EleveElearningSession(request):
    id_user = request.session.get('compte_id')
    compte = Compte.objects.get(id_user=id_user)
    eleve = Eleve.objects.get(compte=compte)
    eleve1 = eleve.id_classe
    Ses = Session.objects.filter(classe_id=eleve1)
    context = {'Ses': Ses}
    return render(request, 'Eleve/Session.html', context)


def EleveElearningHomework(request):
    id_user = request.session.get('compte_id')
    compte = Compte.objects.get(id_user=id_user)
    eleve = Eleve.objects.get(compte=compte)
    classe = eleve.id_classe

    devoirs = Devoir.objects.filter(classe=classe)

    return render(request, 'Eleve/Homework.html', {'devoirs': devoirs})









def submit_homework(request, devoir_id):
    devoir = Devoir.objects.get(id_devoir=devoir_id)
    id_user = request.session.get('compte_id')
    compte = Compte.objects.get(id_user=id_user)
    eleve = Eleve.objects.get(compte=compte)
    if request.method == 'POST':
        homework_file = request.FILES.get('pdf_file')
        if homework_file:
            devoir_contenue = DevoirContenue(CNE_eleve=eleve, Id_devoir=devoir, homework_file=homework_file)
            devoir_contenue.save()
            return redirect('EleveElearningHomework')
    else:
        form = HomeworkSubmissionForm()

    return render(request, 'Eleve/submit_homework.html', {'devoir': devoir})





def student_list(request, devoir_id):
    devoir = Devoir.objects.get(id_devoir=devoir_id)
    devoir_contenues = DevoirContenue.objects.filter(Id_devoir=devoir)
    return render(request, 'Prof/StudentList.html', {'devoir': devoir, 'devoir_contenues': devoir_contenues})






def UserCards(request):
    return render(request,'Admin/UserCards.html')








def session(request):
    id_user = request.session.get('id_user')
    compte = Compte.objects.get(id_user=id_user)
    professeur = Professeur.objects.get(compte=compte)
    ens = Enseigne.objects.filter(Id_professeur=professeur)
    ens_list = [en.Id_professeur for en in ens]  # Retrieve Id_professeur from each Enseigne object
    print(ens_list)
    sessions = Session.objects.filter(Professeur__in=ens_list)  # Filter sessions based on the list of professeurs
    context = {'sessions': sessions}
    return render(request, 'Prof/Session.html', context)











def generate_meeting_link(platform):
    if platform == 'zoom':
        link = 'https://zoom.us/meeting/123456789'
    elif platform == 'google_meet':
        link = 'https://meet.google.com/abcdefghijk'
    else:
        link = '' 
    
    return link

def createSession(request):
    id_user = request.session.get('id_user')
    compte = Compte.objects.get(id_user=id_user)
    professeur = Professeur.objects.get(compte=compte)
    ens = Enseigne.objects.filter(Id_professeur=professeur)
    professeur_instance = professeur

    if request.method == 'POST':
        form = SessionForm(ens,request.POST)
        if form.is_valid():
            session = form.save(commit=False)
            session.Professeur = professeur_instance

            session.save()
            return redirect('session')
    else:
        form = SessionForm(ens)
    
    session_platform = request.POST.get('platform')  
    session_link = generate_meeting_link(session_platform)
    context = {'form': form, 'session_platform': session_platform, 'session_link': session_link}
    return render(request, 'Prof/AddSession.html', context)



def deleteSession(request, session_id):
    try:
        session = get_object_or_404(Session, id=session_id)
    except Session.DoesNotExist:
            raise Http404("session does not exist")
    session.delete()
    messages.success(request, "Devoir removed successfully.")

    return redirect('session')
    




# def RemoveHomeWork(request, devoir_id):
#     try:
#         devoir = Devoir.objects.get(id_devoir=devoir_id)
#     except Devoir.DoesNotExist:
#         raise Http404("Devoir does not exist")

#     devoir.delete()
#     messages.success(request, "Devoir removed successfully.")
#     return redirect('Devoir')





def editSession(request, session_id):
    session = get_object_or_404(Session, id=session_id)
    
    if request.method == 'POST':
        form = SessionForm(request.POST, instance=session)
        if form.is_valid():
            form.save()
            return redirect('session')
    else:
        form = SessionForm(instance=session)
    
    return render(request, 'Prof/EditSession.html', {'form': form, 'session': session})













class ViewMatieres(ListView):
    model=Matiere
    template_name='../templates/Admin/matieres.html'
    context_object_name='matiere_list'
    success_url = reverse_lazy('matieres')
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        niveau = self.request.GET.get('niveau')
        print(niveau)
        if niveau:
            classe = Classe.objects.filter(niveau_classe=niveau)
            print(classe)
            enseignes = Enseigne.objects.filter(Id_classe__in=classe)
            print(enseignes)
            matiere = Matiere.objects.filter(id_matiere__in=enseignes.values_list('Id_matiere', flat=True))
            print(matiere)
            context = {
                'matiere' : matiere , 
                'niveau' : niveau
                         }
        return context
    


# def AdddevoirProf(request):
#     id_user = request.session.get('id_user')
#     compte = Compte.objects.get(id_user=id_user)
#     professeur = Professeur.objects.get(compte=compte)
#     print(professeur)
#     ens=Enseigne.objects.get(Id_professeur=professeur)
#     x=ens.Id_matiere
#     print(x)

#     if request.method == 'POST':
#         form = DevoirForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('AdddevoirProf')  
#     else:
#         form = DevoirForm()
#     return render(request, 'Prof/AddDevoir.html', {'form': form})
  






###########   Login View    ##################


def LoginAgentForm(request):
    form = LoginAgent()
    context = {'form': form}
    if request.method == 'POST':
        form = LoginAgent(request.POST)
        if form.is_valid():
            username = form.cleaned_data['Username']
            password = form.cleaned_data['password']
            try:
                compte = Compte.objects.get(username=username, type_compte=4)
                if compte.check_password(password):
                    user_type = compte.type_compte
                    context = {'user_type': user_type}
                    request.session['id_user'] = compte.id_user
                    request.session['compte_username'] = compte.username
                    request.session['compte_type'] = compte.type_compte
                    return render(request, 'pages/choices.html', context)
                else:
                    messages.add_message(request, messages.ERROR, 'Invalid username or password')
                    return redirect(reverse('EspaceAgent'))
                
            except Compte.DoesNotExist:
                messages.add_message(request, messages.ERROR, 'Invalid username or password')
                return redirect(reverse('EspaceAgent'))
                
        else:
            messages.error(request, 'Please correct the errors in the form')
            return render(request, 'pages/loginagent.html', context)
  
    else:
        return render(request, 'pages/loginagent.html', context)
    


def LoginAdminFrom(request):
    form = LoginAdmin()
    context = {'form': form}
    if request.method == 'POST':
        form = LoginAdmin(request.POST)
        if form.is_valid():
            lol = form.cleaned_data['Username']
            password = form.cleaned_data['password']
            print('good')
            try:
                compte = Compte.objects.get(username=lol,type_compte=1)
                if compte.check_password(password):
                    user_type = compte.type_compte
                    context = {'user_type': user_type}
                    request.session['id_user'] = compte.id_user
                    request.session['compte_username'] = compte.username
                    request.session['compte_type'] = compte.type_compte
                    return render(request, 'pages/choices.html', context)
                else:
                    messages.add_message(request, messages.ERROR, 'Invalid username or password')
                    return redirect(reverse('EspaceAdmin'))
            except Compte.DoesNotExist:
                messages.add_message(request, messages.ERROR, 'Invalid username or password ') 
                return redirect(reverse('EspaceAdmin'))
            

        else:
            messages.error(request, 'Please correct the errors in the form')
            return  render(request, 'pages/loginadmin.html', context)
    
    else:return  render(request, 'pages/loginadmin.html', context)  




def LoginParentForm(request):
    form = LoginParent()
    context = {'form': form}
    if request.method == 'POST':
        form = LoginParent(request.POST)
        if form.is_valid():
            lol = form.cleaned_data['Username']
            password = form.cleaned_data['password']
            try:
                compte = Compte.objects.get(username=lol, type_compte=3)
                if compte.check_password(password):
                    user_type = compte.type_compte
                    context = {'user_type': user_type}
                    request.session['id_user'] = compte.id_user
                    request.session['compte_username'] = compte.username
                    request.session['compte_type'] = compte.type_compte
                    return render(request, 'pages/choices.html', context)
                else:
                    messages.add_message(request, messages.ERROR, 'Invalid username or password')
                    return redirect(reverse('EspaceParent'))
            except Compte.DoesNotExist:
                messages.add_message(request, messages.ERROR, 'Invalid username or password ') 
                return redirect(reverse('EspaceParent')) 
            
        else: 
            messages.error(request, 'Please correct the errors in the form')
            return  render(request, 'pages/loginparent.html', context)
  
    else:return render(request, 'pages/loginparent.html', context)



def LoginProfForm(request):
    form = LoginProf()
    context = {'form': form}
    if request.method == 'POST':
        form = LoginProf(request.POST)
        if form.is_valid():
            lol = form.cleaned_data['Username']
            password = form.cleaned_data['password']
            try:
                compte = Compte.objects.get(username=lol, type_compte=2)
                if compte.check_password(password):
                    user_type = compte.type_compte
                    context = {'user_type': user_type}
                    request.session['id_user'] = compte.id_user
                    request.session['compte_username'] = compte.username
                    request.session['compte_type'] = compte.type_compte
                    return render(request, 'pages/choices.html', context)
                else:
                    messages.add_message(request, messages.ERROR, 'Invalid username or password')
                    return redirect(reverse('EspaceProf'))
            except Compte.DoesNotExist:
                messages.add_message(request, messages.ERROR, 'Invalid username or password ')
                return redirect(reverse('EspaceProf'))

        else:
            messages.error(request, 'Please correct the errors in the form')
            return render(request, 'pages/loginteacher.html', context)
    
    else:
        return render(request, 'pages/loginteacher.html', context)
    

def LoginStudentForm(request):
    form = LoginEleve()
    context = {'form': form}
    if request.method == 'POST':
        form = LoginEleve(request.POST)
        if form.is_valid():
            lol = form.cleaned_data['Username']
            password = form.cleaned_data['password']
            try:
                
                compte = Compte.objects.get(username=lol, type_compte=5)
                if compte.check_password(password):
                    user_type = compte.type_compte
                    context = {'user_type': user_type}
                    request.session['compte_id'] = compte.id_user
                    request.session['compte_username'] = compte.username
                    request.session['compte_type'] = compte.type_compte
                    return render(request, 'pages/choices.html', context)
                else:
                    messages.add_message(request, messages.ERROR, 'Invalid username or password')
                    return redirect(reverse('EspaceEleve'))

            except Compte.DoesNotExist:
                messages.add_message(request, messages.ERROR, 'Invalid username or password ')
                return redirect(reverse('EspaceEleve'))

        else:
            messages.error(request, 'Please correct the errors in the form')
            return render(request, 'pages/loginteacher.html', context)




    else:
        return render(request, 'pages/loginstudent.html', context)
    
def logout_user(request):
    compte_type = request.session.get('compte_type')
    logout(request)

    return redirect('home')
   
    
    
#############   Tout Ce qui concerne Admin  ########################    
#(Absence)
def AdminAbsence(request):
    return render(request,'Admin\AdminAbsence.html')

def AdminAbsDash(request):
    today = timezone.now().date()
    id = request.session.get('id_user')
    compte = Compte.objects.get(id_user=id)
    admin = Admin.objects.get(compte_id=compte)
    eleves_count = Eleve.objects.all().count()
    present = ListePresence.objects.all().filter(etat=True, date__date=today).count()
    absent = ListePresence.objects.all().filter(etat=False, date__date=today).count()
    context = {
        'eleves_count':eleves_count,
        'present':present,
        'absent':absent,
        'admin':admin,
    }
    return render(request,'Admin/AdminAbsDash.html',context)

def AdminPaiement(request):
    return render(request,'Admin\AdminPaiement.html')

def AdminElearning(request):
    return render(request,'Admin\AdminElearning.html')

def AdminQr(request):
    classe = Classe.objects.values('id_classe','niveau_classe')
    context={'classe':classe}
    return render(request, 'Admin/AdminQr.html',context)

def GenerateurAdmin(request):
        if request.method == 'POST':
            prenom = request.POST['Prenom']
            numer = request.POST['Numero']
            nom = request.POST['Nom']
            cne = request.POST['cne']
            qr_code = request.POST['qr_code']
            classe=request.POST.get('classe')
            try:
                obj1= Parent.objects.get(cin_parent=numer)
                obj2=Classe.objects.get(id_classe=classe)
                obj3=Compte.objects.get(nom=nom,prenom=prenom)
            except (Parent.DoesNotExist, Classe.DoesNotExist, Compte.DoesNotExist):
                message = 'Please check if the parent or classe exist'
                return render(request, 'Admin/AdminQr.html', {'message': message})

            obj =Eleve.objects.filter(compte=obj3,cne_eleve =cne,id_classe=obj2,cin_parent=obj1).exists()
            if obj:
                obj5=Eleve(compte=obj3,cne_eleve =cne,id_classe=obj2,cin_parent=obj1,qr_code=qr_code)
                obj5.save()
                message = 'Qr code saved successfully!'
                return render(request, 'Admin/AdminQr.html', {'message': message})
            else:
                message = "student doesn't exist"
                return render(request, 'Admin/AdminQr.html', {'message': message})


def AdminReclamation(request):
    id = request.session.get('id_user')
    compte = Compte.objects.get(id_user=id)
    admin = Admin.objects.get(compte_id=compte)
    recl = Reclamation.objects.filter(admin=admin)
    rec = Reclamation.objects.all()
    context = {'rec':rec}
    return render(request,'Admin/AdminReclamation.html', context)


def AdminAbsList(request):
    today = timezone.now().date()
    id = request.session.get('id_user')
    compte = Compte.objects.get(id_user=id)
    admin = Admin.objects.get(compte_id=compte)
    list = ListePresence.objects.filter(date__date=today)
    pres_students = ListePresence.objects.filter(etat=True).values_list('cne_eleve_id', flat=True)
    prs_students = list.filter(etat=True).values()
    all_students = Eleve.objects.all()
    abs_students = Eleve.objects.exclude(cne_eleve__in=pres_students)
    present_students_with_classe = []
    for student in prs_students:
        try:
            cne_eleve = student['cne_eleve_id']
            eleve = Eleve.objects.get(cne_eleve=cne_eleve)
            classe = Classe.objects.get(id_classe=student['classe_id'])
            present_students_with_classe.append((eleve, classe, student['date']))
        except Eleve.DoesNotExist:
            pass
        except Classe.DoesNotExist:
            pass
    context = {
        'list': list,
        'abs_students': abs_students,
        'prs_students': prs_students,
        'pres_students': pres_students,
        'present_students': present_students_with_classe,
    }
    return render(request, 'Admin/AdminAbsList.html',context)


#(Paiement)







def notif(request):
    now = dt.datetime.now()
    month_name = now.strftime("%B")
    etudiants = Eleve.objects.all()
    etudiants_non_payes = etudiants.exclude(
        paiement__mois_paiement=month_name  
    )
    context = {'etudiants_non_payes': etudiants_non_payes}
    return render(request, 'Admin/notif.html', context)

def tablep (request):
    p = Paiement.objects.all()
    return render(request, 'Admin/tablep.html', {'p': p } ) 




def grades(request):
    id_user = request.session.get('id_user')
    compte = Compte.objects.get(id_user=id_user)
    parent = Parent.objects.get(compte=compte)
    students = Eleve.objects.filter(cin_parent=parent)
    print(students)  
    students.get()
    context = {'parent': parent, 'students': students,'classe':classe}
    return render(request, 'Parent/Grade.html', context)

def level(request):
    return render(request,'Admin/level.html')




def send_emails(request):
    if request.method == 'POST':
        email_addresses = request.POST.getlist('emailAddresses[]')

        #  pour envoyer les e-mails à partir des adresses e-mail collectées

        try:
            # Envoyer les e-mails
            send_mail(
                'Reminder: Late payment of school fees',
                'Dear parent,\n\nWe remind you that school fees are overdue. Please make payment as soon as possible to avoid disruption of services.\n\nThank you for your cooperation.\n\nRegards,\n Jhon Nash School',
                'expediteur@example.com',
                email_addresses,
                fail_silently=False,
            )

            # Réponse JSON en cas de succès
            return JsonResponse({'success': True})

        except Exception as e:
            # Réponse JSON en cas d'erreur
            return JsonResponse({'success': False, 'error': str(e)})

    # Réponse JSON pour toute autre méthode HTTP
    return JsonResponse({'success': False, 'error': 'Méthode non autorisée'})


def send_email(request):
    if request.method == 'POST':
        message = request.POST['message']
        email = request.POST['email']
        name = request.POST['name']
        send_mail(
            name,
            message,
            'settings.EMAIL_HOST_USER',
            [email],
            fail_silently=False
        )
    return render(request, 'Admin/send_mail.html')


def niveau(request, niveau):
    try:
        classe = Classe.objects.get(niveau_classe=niveau)
        paiements = Paiement.objects.all()
        etudiant_mois = {}
        etudiants_niveau = Eleve.objects.filter(id_classe=classe) 
        for etudiant in etudiants_niveau:
            paiements_etudiant = paiements.filter(cne_eleve=etudiant.cne_eleve)
            mois_payes = [p.mois_paiement for p in paiements_etudiant]
            mois_non_payes = [mois for mois in calendar.month_name[1:] if mois not in mois_payes and mois not in ['July', 'August']]
            etudiant_mois[etudiant] = {'mois_payes': mois_payes, 'mois_non_payes': mois_non_payes}
        context = {
            'etudiant_mois': etudiant_mois,
            'niveau': niveau,
        }
        return render(request, 'Admin/niveau.html', context)
    except ObjectDoesNotExist:
        error_message = "The class does not exist for the specified level."
        return render(request, 'Admin/niveau.html',{ 'error_message':error_message})


def AdminDash(request):
    now = dt.datetime.now()
    month_name = now.strftime("%B")
    etudiants = Eleve.objects.all()
    etudiants_non_payes = etudiants.exclude(paiement__mois_paiement=month_name)
    count_etudiants_non_payes = etudiants_non_payes.count()

    etudiants_payes = etudiants.filter(paiement__mois_paiement=month_name)
    count_etudiants_payes = etudiants_payes.count()

    total = Paiement.objects.aggregate(total=Sum('montant')).get('total')
    moyenne = Paiement.objects.aggregate(moyenne=Avg('montant')).get('moyenne')
    context = {
        'etudiants_non_payes': etudiants_non_payes,
        'count_etudiants_non_payes': count_etudiants_non_payes,
        'count_etudiants_payes': count_etudiants_payes,
        'total': total,
        'moyenne': moyenne
    }
    return render(request, 'Admin/AdminDash.html', context)
def generate_ref():
    now = dt.datetime.now()
    year = str(now.year)
    month = str(now.month).zfill(2)
    day = str(now.day).zfill(2)
    hour = str(now.hour).zfill(2)
    minute = str(now.minute).zfill(2)
    second = str(now.second).zfill(2)
    milliseconds = str(now.microsecond)[:3].zfill(3)

    reference = f"{year}{month}{day}{hour}{minute}{second}{milliseconds}"
    return reference

def paiement(request):
    if request.method == 'POST':
        form = PaiementFormEleve(request.POST)
        if form.is_valid():
            data = form.cleaned_data
           
            cne_eleve = data['cne_eleve'].cne_eleve
            nom_prenom = data['eleve_nom_prenom']
            try:
                eleve = Eleve.objects.get(cne_eleve=cne_eleve)
            except Eleve.DoesNotExist:
                raise forms.ValidationError("Le nom et prénom de l'élève ne correspondent pas au CNE saisi.")

            reference = generate_ref()
            context = {
                'reference': reference,
                'date_paiement': data['date_paiement'],
                'montant': data['montant'],
                'modeP': data['modeP'],
                'type_service': data['type_service'],
                'mois_paiement': data['mois_paiement'],
                'cne_eleve': data['cne_eleve'],
                'nom_prenom': nom_prenom,
                
            }
            html_template = get_template('Admin/pdf.html')
            html = html_template.render(context)
            pdf_file = BytesIO()
            pisa.CreatePDF(html, dest=pdf_file)

            paiement = form.save(commit=False)
            paiement.reference = reference
            paiement.save()

            response = HttpResponse(pdf_file.getvalue(), content_type='application/pdf')
            filename = f"{slugify(data['date_paiement'])}{slugify(data['cne_eleve'])}.pdf"
            response['Content-Disposition'] = f'attachment; filename="{filename}"'
            return response
    else:
        form = PaiementFormEleve()

    parents = Parent.objects.all()
    data = []

    for parent in parents:
        eleves = Eleve.objects.filter(cin_parent=parent.cin_parent)
        for eleve in eleves:
            student_name = eleve.compte.get_full_name()
            payment_state = "Paid"

            data.append({'parent': parent, 'student_name': student_name, 'payment_state': payment_state})

    return render(request, 'admin/paiement.html', {'form': form, 'data': data})
from django.http import JsonResponse

from django.http import JsonResponse
from django.db.models import Q

def paiementgeteleve(request):
    if 'nom_prenom' in request.POST:
        search_term = request.POST.get('nom_prenom')
        results = Compte.objects.filter(Q(type_compte=5) & (Q(nom__istartswith=search_term) | Q(prenom__istartswith=search_term))).values('eleve__cne_eleve', 'nom', 'prenom')
    else:
        results = []

    return JsonResponse(list(results), safe=False)

#(Gestion)

class ViewAdmins(ListView):
   model = Admin
   template_name ='Admin/admins.html'
   context_object_name='admin_list'
   paginate_by=8
  
   
class AjoutAdmin(CreateView):
     model= Admin
     form_class= AjoutAdmin
     template_name= 'Admin/addadmin.html'
     success_url = reverse_lazy('admins')

class EditAdmin(UpdateView):
    model = Compte
    form_class = EditAdminForm
    template_name = 'Admin/editadmin.html'
    pk_url_kwarg = 'id_user'
    success_url = reverse_lazy('admins')
         
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id_user = self.kwargs.get('id_user')
        admin = get_object_or_404(Admin, compte_id=id_user)
        compte = self.object
        initial_data = {
            'cin_admin': admin.cin_admin,
        }
        form = self.form_class(instance=compte, initial=initial_data)
        context['form'] = form
        return context

    def form_valid(self, form):
        id_user = self.kwargs.get('id_user')
        cin_admin = form.cleaned_data['cin_admin']

        admin= Admin.objects.get(compte_id=id_user)
        with transaction.atomic():
          Admin.objects.filter(cin_admin=admin.cin_admin).update(cin_admin=cin_admin)
          Percevoir.objects.filter(cin_admin=admin.cin_admin).update(cin_admin=cin_admin)
        return super().form_valid(form)     
    
class DeleteAdmin(DeleteView):
    model = Compte
    success_url = reverse_lazy('admins')
    pk_url_kwarg='id_user'
    def get_object(self, queryset=None):
        id_user=self.kwargs.get("id_user")
        compte= Compte.objects.get(id_user=id_user)
        return compte
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.get_success_url()) 
    

class ViewParents(ListView):
   model = Parent
   template_name ='../templates/Admin/parents.html'
   context_object_name='parent_list'
   paginate_by = 8

class AjoutParent(CreateView):
     model=Parent
     form_class= AjoutParent
     template_name= '../templates/Admin/addparent.html'
     success_url = reverse_lazy('parents')
     
class EditParent(UpdateView):
    model = Compte
    form_class = EditParentForm
    template_name = 'Admin/editparent.html'
    pk_url_kwarg = 'id_user'
    success_url = reverse_lazy('parents')
         
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id_user = self.kwargs.get('id_user')
        parent = get_object_or_404(Parent, compte_id=id_user)
        compte = self.object
        initial_data = {
            'cin_parent': parent.cin_parent,
        }
        form = self.form_class(instance=compte, initial=initial_data)
        context['form'] = form
        return context

    def form_valid(self, form):
        id_user = self.kwargs.get('id_user')
        cin_parent = form.cleaned_data['cin_parent']
        parent = Parent.objects.get(compte_id=id_user)
        with transaction.atomic():
         Parent.objects.filter(compte_id=id_user).update(cin_parent=cin_parent)
         Eleve.objects.filter(cin_parent=parent.cin_parent).update(cin_parent=cin_parent)
         RecevoirSms.objects.filter(CIN_parent=parent.cin_parent).update(CIN_parent=cin_parent)
         Reclamer.objects.filter(CIN_parent=parent.cin_parent).update(CIN_parent=cin_parent)
        return super().form_valid(form)
    


class DeleteParent(DeleteView):
    model = Compte
    success_url = reverse_lazy('parents')
    pk_url_kwarg='id_user'
    def get_object(self, queryset=None):
        id_user=self.kwargs.get("id_user")
        compte= Compte.objects.get(id_user=id_user)
        return compte
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.get_success_url())




class ViewAgents(ListView):
   model = Agent
   template_name ='../templates/Admin/agents.html'
   context_object_name='agent_list'
   paginate_by=8
  
   
class AjoutAgent(CreateView):
     model= Agent
     form_class= AjoutAgent
     template_name= '../templates/Admin/addagent.html'
     success_url = reverse_lazy('agents')

class EditAgent(UpdateView):
    model = Compte
    form_class = EditAgentForm
    template_name = 'Admin/editagent.html'
    pk_url_kwarg = 'id_user'
    success_url = reverse_lazy('agents')
         
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id_user = self.kwargs.get('id_user')
        agent = get_object_or_404(Agent, compte_id=id_user)
        compte = self.object
        initial_data = {
            'cin_agent': agent.cin_agent,
        }
        form = self.form_class(instance=compte, initial=initial_data)
        context['form'] = form
        return context

    def form_valid(self, form):
        id_user = self.kwargs.get('id_user')
        cin_agent = form.cleaned_data['cin_agent']
     
        agent= Agent.objects.get(compte_id=id_user)
        with transaction.atomic():
          Agent.objects.filter(cin_agent=agent.cin_agent).update(cin_agent=cin_agent)
        return super().form_valid(form)     
    
class DeleteAgent(DeleteView):
    model = Compte
    success_url = reverse_lazy('agents')
    pk_url_kwarg='id_user'
    def get_object(self, queryset=None):
        id_user=self.kwargs.get("id_user")
        compte= Compte.objects.get(id_user=id_user)
        return compte
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.get_success_url())



class ViewEleves(ListView):
   model = Eleve
   template_name ='../templates/Admin/eleves.html'
   context_object_name='eleve_list'
   paginate_by = 10
   def get_queryset(self):
      classe = self.request.GET.get('classe')
      print(classe)
      if classe:
            classe = get_object_or_404(Classe, nom_classe=classe)
            queryset = Eleve.objects.filter(id_classe__nom_classe=classe)
            
            return queryset
    
      else:
            return Eleve.objects.all()
    
   
class AjoutEleve(CreateView):
     model= Eleve
     form_class= AjoutEleve
     template_name= '../templates/Admin/addeleve.html'
     success_url = reverse_lazy('eleves')
     
     def valid_form(self,form):
        selected_class = form.cleaned_data['selected_class']
        classe = Classe.objects.get(id_classe=selected_class.id_classe)
        if classe.nbr_eleve_classe >= classe.max_students:
            form.add_error(None, "Class is already full. Cannot enroll more students.")
            return self.form_invalid(form)
        student = form.save(commit=False)
        student.classe = classe
        student.save()
        classe.nbr_eleve_classe += 1
        classe.save()
        messages.success(self.request, "Student enrolled successfully.")
        return super().form_valid(form)

class EditEleve(UpdateView):
    model = Compte
    form_class = EditEleveForm
    template_name = 'Admin/editeleve.html'
    pk_url_kwarg = 'id_user'
    success_url = reverse_lazy('eleves')
         
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id_user = self.kwargs.get('id_user')
        eleve = get_object_or_404(Eleve, compte_id=id_user)
        compte = self.object
        initial_data = {
            'cne_eleve': eleve.cne_eleve,
            'classe': eleve.id_classe,
            'parent': eleve.cin_parent,
        }
        form = self.form_class(instance=compte, initial=initial_data)
        context['form'] = form
        return context

    def form_valid(self, form):
        id_user = self.kwargs.get('id_user')
        cne_eleve = form.cleaned_data['cne_eleve']
        classe = form.cleaned_data['classe']
        parent = form.cleaned_data['parent']
        eleve = Eleve.objects.get(compte_id=id_user)
        with transaction.atomic():
         ########REVOIR
         Eleve.objects.filter(cne_eleve=eleve.cne_eleve).update(cne_eleve=cne_eleve, id_classe=classe, cin_parent=parent)
         Passe.objects.filter(CNE_eleve=eleve.cne_eleve).update(CNE_eleve=cne_eleve)
         Scanne.objects.filter(CNE_eleve=eleve.cne_eleve).update(CNE_eleve=cne_eleve)
         Paiement.objects.filter(cne_eleve=eleve.cne_eleve).update(cne_eleve=cne_eleve)
         ListePresence.objects.filter(cne_eleve=eleve.cne_eleve).update(cne_eleve=cne_eleve)
        return super().form_valid(form)     

    
class DeleteEleve(DeleteView):
    model = Compte
    success_url = reverse_lazy('eleves')
    pk_url_kwarg='id_user'
    def get_object(self, queryset=None):
        id_user=self.kwargs.get("id_user")
        compte= Compte.objects.get(id_user=id_user)
        return compte
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.get_success_url())




class ViewProfs(ListView):
   model = Professeur
   template_name ='../templates/Admin/profs.html'
   context_object_name='prof_list'
   paginate_by= 6

class AjoutProf(CreateView):
     model= Professeur
     form_class= AjoutProf
     template_name= '../templates/Admin/addprof.html'
     success_url = reverse_lazy('profs')

class EditProf(UpdateView):
    model = Compte
    form_class = EditProfForm
    template_name = 'Admin/editprof.html'
    pk_url_kwarg = 'id_user'
    success_url = reverse_lazy('profs')
         
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id_user = self.kwargs.get('id_user')
        prof = get_object_or_404(Professeur, compte_id=id_user)
        compte = self.object
        initial_data = {
            'cin_professeur': prof.cin_professeur,
        }
        form = self.form_class(instance=compte, initial=initial_data)
        context['form'] = form
        return context

    def form_valid(self, form):
        id_user = self.kwargs.get('id_user')
        cin_prof = form.cleaned_data['cin_professeur']
        prof= Professeur.objects.get(compte_id=id_user)
        with transaction.atomic():
          Professeur.objects.filter(cin_professeur=prof.cin_professeur).update(cin_professeur=cin_prof)
        return super().form_valid(form)   
      
class DeleteProf(DeleteView):
    model = Compte
    success_url = reverse_lazy('profs')
    pk_url_kwarg='id_user'
    def get_object(self, queryset=None):
        id_user=self.kwargs.get("id_user")
        compte= Compte.objects.get(id_user=id_user)
        return compte
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.get_success_url())


class ViewNotes(ListView):
    model=Passe
    template_name='../templates/Admin/notes.html'
    context_object_name='passe_list'
    paginate_by=8
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cne_eleve = self.request.GET.get('cne_eleve')
        if cne_eleve:
            eleve=Eleve.objects.get(cne_eleve=cne_eleve)
            classe=eleve.id_classe
            enss= Enseigne.objects.filter(Id_classe=classe)
            if enss.exists():
                values = []
                note_list = []
                epreuve_list = []
                for ens in enss:
                    matieres = [ens.Id_matiere] if isinstance(ens.Id_matiere, Matiere) else ens.Id_matiere.all()
                    print(matieres)
                    for matiere in matieres:
                        ens1 = SousMatiere.objects.filter(matiere_id=matiere)
                        eprv = Eprv.objects.filter(classe=ens.Id_classe)
                        for eprv_obj in eprv:
                            for ssmatiere in ens1:
                                epreuve = Se_Comporte.objects.filter(sousmatiere=ssmatiere, epreuve=eprv_obj.epreuve)
                                for entry in epreuve:
                                    epreuve_list.append((entry.epreuve, entry.sousmatiere, entry.epreuve_id))
                                    ent = entry.epreuve_id
                                    try:
                                        passe = Passe.objects.get(id_epreuve=ent, CNE_eleve=cne_eleve)
                                        note_list.append((ent, passe.Note, passe.id_epreuve))
                                    except ObjectDoesNotExist:
                                        pass

                    values.append((matiere, ens1, epreuve_list, note_list))
                print(values)
                context ={'values': values, 'eleve': eleve}
            
        return context
from django.db.models import Count
import json
def admin_dashboard(request):
    class_count = Classe.objects.count()
    student_count = Eleve.objects.count()
    agent_count = Agent.objects.count()
    professor_count = Professeur.objects.count()
    parent_count = Parent.objects.count()
    admin_count = Admin.objects.count()
    user_analytics = UserAnalytics.objects.all()
    user_types = [analytics.user_type for analytics in user_analytics]
    hours_connected = [analytics.hours_connected for analytics in user_analytics]
    gender_stats = (
        Compte.objects.values('sexe').annotate(count=Count('sexe')).values('sexe', 'count')
    )
    gender_stats_list = list(gender_stats)
    gender_stats_json = json.dumps(gender_stats_list)
    context = {

        'gender_stats':gender_stats_json,
        'class_count': class_count,
        'student_count': student_count,
        'agent_count': agent_count,
        'professor_count': professor_count,
        'user_analytics': user_analytics,
        'user_types': user_types,
        'hours_connected': hours_connected,
        'parent_count':parent_count
    }
    return render(request, 'Admin/dashboard.html', context)

def leila(request):
    PS='PS'
    MS='MS'
    GS='GS'
    CP='CP'
    CE1='CE1'
    CE2='CE2'
    CM1='CM1'
    CM2='CM2'
    CE6='CE6'
    data = [PS,MS,GS,CP,CE1,CE2,CM1,CM2,CE6]
    context={'niveaux':data}
    print(context)
    return render(request,'Admin/nini.html', context)

class ViewClasses(ListView):
    model=Classe
    template_name='../templates/Admin/classes.html'
    context_object_name='classe_list'
    paginate_by=5
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        niveau = self.request.GET.get('niveau')
        if niveau:
            queryset = Classe.objects.filter(niveau_classe=niveau)
        else:
            queryset = Classe.objects.all()
        context = {
            'niveau' : niveau,
            'queryset' : queryset
        }
        return context

#modification
def handle_uploaded_file(f):
    with open('SchoolApp/Upload/' + f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def addclasse(request):
    if request.method == "POST":
        form = ClasseForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES["emploie_temps"])
            classe = form.save()
            niveau = classe.niveau_classe
            redirect_url = reverse('classes') + f"?niveau={niveau}"
            return redirect(redirect_url)
    else:
        form = ClasseForm()
    
    context = {'form': form}
    return render(request, 'Admin/formulaireclasse.html', context)

#modification pour eleves

def update_classe(request, id_classe):
    classe = get_object_or_404(Classe, id_classe=id_classe)
    niveau = classe.niveau_classe
    form = ClasseForm(instance=classe)
    
    if request.method == "POST":
        form = ClasseForm(request.POST, request.FILES, instance=classe)
        if form.is_valid():
            emploie_temps = form.cleaned_data['emploie_temps']
            if emploie_temps:
                handle_uploaded_file(emploie_temps)  # Custom function to handle the uploaded file
            classe.save()
            redirect_url = reverse('classes') + f"?niveau={niveau}"
            return redirect(redirect_url)
    
    context = {'form': form, 'classe': classe}
    return render(request, 'Admin/update_classe.html', context)


def delete_classe(request, id_classe):
    niveau = request.GET.get('niveau')
    if request.method == "POST":
        classes = get_object_or_404(Classe, id_classe=id_classe)
        print(classes)
        classes.delete()
        redirect_url = reverse('classes') + f"?niveau={niveau}"
        return redirect(redirect_url)

    context = {'classes': classes}
    return render(request, 'Admin/classes.html', context)

class ViewEnseigne(ListView):
    model=Enseigne
    template_name='../templates/Admin/enseignes.html'
    context_object_name='enseigne_list'
    success_url = reverse_lazy('enseignes')

def addenseigne(request):
     form = EnseigneForm()

     if request.method == "POST" :
         form= EnseigneForm(request.POST)
         if form.is_valid():
            form.save()
            return redirect('enseignes')
     else:
          form = EnseigneForm()
     context = {'form': form,}
     return render(request,'Admin/formulaireenseigne.html', context) 
     

def update_enseigne(request, id):
    enseigne = get_object_or_404(Enseigne, id=id)
    form = EnseigneForm(instance=enseigne)
    if request.method == "POST":
        form = EnseigneForm(request.POST, instance=enseigne)
        if form.is_valid():
             form.save()
             return redirect('enseignes')
    context = {'form': form ,'enseigne':enseigne}
    return render(request, 'Admin/update_enseigne.html', context)
    
def delete_enseigne(request, id):
    
    if request.method == "POST":
        enseigne = get_object_or_404(Enseigne, id=id)
        print(enseigne)
        enseigne.delete()
        return redirect('enseignes')

    context = {'enseigne': enseigne}
    return render(request, 'Admin/enseignes.html', context)



def liste_enseignants(request):
    classe = request.GET.get('classe')
    enseignes = Enseigne.objects.all()

    if classe:
        classe_obj = get_object_or_404(Classe, id_classe=classe)
        enseignes = enseignes.filter(Id_classe=classe_obj)

    context = {'enseignes': enseignes}
    return render(request, 'Admin/profsmatieres.html', context)

class ViewSousmatieres(ListView):
    model=SousMatiere
    template_name='../templates/Admin/sousmatieres.html'
    context_object_name='sousmatiere_list'
    paginate_by=7

#coursprof
def sous_matieres_professeur(request):
        id_user = request.session.get('id_user')  # Retrieve the user ID from the session
        compte= Compte.objects.get(id_user=id_user)  
        professeur = Professeur.objects.get(compte=compte)
        print (professeur)
        enseignes = Enseigne.objects.filter(Id_professeur=professeur)  # Récupérer les enseignes associées au professeur
        print(enseignes)
        classe_list = enseignes.values_list('Id_classe__nom_classe', flat=True) 
        print(classe_list)
        enseignes_matiere_ids = enseignes.values_list('Id_matiere', flat=True)  # Récupérer les IDs des matières enseignées
        matieres = Matiere.objects.filter(id_matiere__in=enseignes_matiere_ids)  # Récupérer les objets Matiere correspondant aux IDs
        noms_matieres = matieres.values_list('nom_matiere', flat=True)  # Récupérer les noms des matières
        nom_matiere = noms_matieres
        print(nom_matiere)
        sous_matieres = SousMatiere.objects.filter(matiere__in=enseignes_matiere_ids)  # Récupérer les sous-matières associées aux matières enseignées
        print(sous_matieres)
        context = {
            'professeur': professeur,
            'sousmatiere_list': sous_matieres,
            'enseignes': enseignes,
            'classe_list': classe_list,
            'matiere' : matieres
             }
       
        print(matieres)
        return render(request, 'Prof/sousmatieres1.html', context)
def addssmatiere(request):
    mat = request.GET.get('matiere')
    print(mat)
    matiere = Matiere.objects.filter(nom_matiere=mat)
    print(matiere)
    print(matiere.values('id_matiere'))
    if request.method == "POST":
        formssmatiere = SousMatiereForm(request.POST, matiere=matiere)
        if formssmatiere.is_valid():
            formssmatiere.save()
            return redirect('sousmatieres_professeur')
    else:
        formssmatiere = SousMatiereForm(matiere=matiere)
    context = {'formssmatiere': formssmatiere}
    return render(request, 'Prof/formulairessmatiere.html', context)


def display_timetable(request):
    id_user = request.session.get('compte_id')  # Retrieve the user ID from the session
    print(id_user)
    compte= Compte.objects.get(id_user=id_user)  
    print(compte)# Retrieve the compte associated with the user ID
    eleve = Eleve.objects.get(compte=compte)
    print (eleve)

    # Retrieve the timetable for the student's class
    classe = eleve.id_classe
    print(classe)
    timetable = classe.emploie_temps

    context = {'timetable': timetable  , 'classe' : classe}
    return render(request, 'Eleve/timetable.html', context)


def Coursstudent(request):
        matiere_name = request.GET.get('matiere')  # Récupérer la matière depuis les paramètres de requête
        sous_matiere = request.GET.get('sous_matiere')  # Récupérer la sous-matière depuis les paramètres de requête
        id_user = request.session.get('compte_id')  # Retrieve the user ID from the session
        print(id_user)
        compte= Compte.objects.get(id_user=id_user)  
        print(compte)# Retrieve the compte associated with the user ID
        eleve = Eleve.objects.get(compte=compte)
        print (eleve)
         # Retrieve the associated Eleve object
        # Eleve = eleve.nom
        # print(Eleve)  # Assuming the Eleve model has a 'nom' field for the student's name
  # Assuming the Eleve model has a 'nom' field for the student's name
        classe = eleve.id_classe
        print(classe) # Assuming the Eleve model has a foreign key to the Classe mod
        enseigne= Enseigne.objects.filter(Id_classe=classe)
        enseigne1=enseigne.values('Id_professeur')
        print(enseigne1)
        enseigne2=enseigne.values('Id_matiere')
        print(enseigne2)
        # matiere=Matiere.objects.filter(id_matiere=enseigne2.id_matiere)
        # print(matiere)
      
        try:
            matiere = Matiere.objects.get(nom_matiere=matiere_name)  # Récupérer l'objet Matiere en utilisant le nom comme filtre
        except ObjectDoesNotExist:
            matiere = None
    
        sm_list = SousMatiere.objects.filter(matiere__in=enseigne2)  # Filtrer les sous-matières par la matière de l'enseigne
    
        if matiere and sous_matiere:
            sm_list = sm_list.filter(matiere=matiere, nom_sousmatiere=sous_matiere)  # Filtrer les sous-matières par la matière et sous-matière spécifiées
    
        comporte = ComporteCours.objects.filter(Id_SM__in=sm_list.values('id_sousmatiere'))  # Filtrer les cours en fonction des sous-matières
        cours_list = [comporte_item.Id_cours for comporte_item in comporte]  # Créer une liste des cours
    
        context = {'Eleve': eleve, 'sm_list': sm_list, 'cours_list': cours_list, 'Classe': classe}
        return render(request, 'Eleve/coursstudent.html', context)

def Coursprof(request):
        matiere_name = request.GET.get('matiere')  # Récupérer la matière depuis les paramètres de requête
        sous_matiere = request.GET.get('sous_matiere')  # Récupérer la sous-matière depuis les paramètres de requête
        id_user = request.session.get('id_user')  # Retrieve the user ID from the session
        print(id_user)
        compte= Compte.objects.get(id_user=id_user)  
        print(compte)# Retrieve the compte associated with the user ID
        professeur = Professeur.objects.get(compte=compte)
        print (professeur)
        enseignes = Enseigne.objects.filter(Id_professeur=professeur)  # Récupérer les enseignes associées au professeur
        print(enseignes)
        classe_list = enseignes.values_list('Id_classe__nom_classe', flat=True) 
        print(classe_list)
        enseignes_matiere_ids = enseignes.values_list('Id_matiere', flat=True)  # Récupérer les IDs des matières enseignées
        matieres = Matiere.objects.filter(id_matiere__in=enseignes_matiere_ids)  # Récupérer les objets Matiere correspondant aux IDs
        noms_matieres = matieres.values_list('nom_matiere', flat=True)  # Récupérer les noms des matières
        nom_matiere = noms_matieres.first()
        print(nom_matiere)
        sous_matieres = SousMatiere.objects.filter(matiere__in=enseignes_matiere_ids)  # Récupérer les sous-matières associées aux matières enseignées
        print(sous_matieres)
      
        try:
            matiere = Matiere.objects.get(nom_matiere=matiere_name)  # Récupérer l'objet Matiere en utilisant le nom comme filtre
        except ObjectDoesNotExist:
            matiere = None
    
        sm_list = SousMatiere.objects.filter(matiere__in=matieres)  # Filtrer les sous-matières par la matière de l'enseigne
    
        if matiere and sous_matiere:
            sm_list = sm_list.filter(matiere=matiere, nom_sousmatiere=sous_matiere)  # Filtrer les sous-matières par la matière et sous-matière spécifiées
    
        comporte = ComporteCours.objects.filter(Id_SM__in=sm_list.values('id_sousmatiere'))  # Filtrer les cours en fonction des sous-matières
        cours_list = [comporte_item.Id_cours for comporte_item in comporte]  # Créer une liste des cours
    
        context = {'sous_matiere': sous_matiere, 'sm_list': sm_list, 'cours_list': cours_list}
        return render(request, 'Prof/coursprofs.html', context)

def Courses(request):
        id_user = request.session.get('compte_id')  # Retrieve the user ID from the session
        print(id_user)
        compte= Compte.objects.get(id_user=id_user)  
        print(compte)# Retrieve the compte associated with the user ID
        eleve = Eleve.objects.get(compte=compte)
        print (eleve)
        classe = eleve.id_classe
        print(classe)
        enseignes = Enseigne.objects.filter(Id_classe=classe)
        professeurs = [enseigne.Id_professeur for enseigne in enseignes]
        print(professeurs)
        classe_list = enseignes.values_list('Id_classe__nom_classe', flat=True) 
        print(classe_list)
        enseignes_matiere_ids = enseignes.values_list('Id_matiere', flat=True)  # Récupérer les IDs des matières enseignées
        matieres = Matiere.objects.filter(id_matiere__in=enseignes_matiere_ids)  # Récupérer les objets Matiere correspondant aux IDs
        noms_matieres = matieres.values_list('nom_matiere', flat=True)  # Récupérer les noms des matières
        # nom_matiere = noms_matieres.first()
        print(noms_matieres)
        ens = Enseigne.objects.filter(Id_matiere__in=noms_matieres)
        # print(ens)
           
        sous_matieres = SousMatiere.objects.filter(matiere__in=enseignes_matiere_ids)  # Récupérer les sous-matières associées aux matières enseignées
        print(sous_matieres)
        context = {
            'professeurs': professeurs,
            'matieres': noms_matieres,
            'sous_matieres': sous_matieres,
            'enseignes' : enseignes,
            'classe' : classe
         }
    
        return render(request, 'Eleve/courses.html', context)


def addcours(request):
     ssm=request.GET.get('ssmatiere')
     print(ssm)
     sousmatiere = SousMatiere.objects.filter(nom_sousmatiere=ssm)
     matie= sousmatiere.values('matiere')[0]['matiere']
     matier=Matiere.objects.filter(id_matiere=matie)
     matiere=matier.values('nom_matiere')[0]
     if request.method == "POST" :
         form= CoursForm(request.POST, request.FILES, sousmatiere=sousmatiere)
         if form.is_valid():
            handle_uploaded_file(request.FILES["pdf_cours"])
            ssmatiere=form.cleaned_data.get('sousmatiere')
            ssmati = SousMatiere.objects.filter(nom_sousmatiere=ssmatiere)
            matie = ssmati.values('matiere')[0]['matiere']
            matier=Matiere.objects.filter(id_matiere=matie)
            matiere=matier.values('nom_matiere')[0]['nom_matiere']
            cours = form.save() 
            ccours = ComporteCours.objects.create(Id_cours=cours, Id_SM=ssmatiere)
            print(cours)
            redirect_url = reverse('coursprofs')
            query_params = f"?matiere={matiere}&sous_matiere={ssmatiere}"
            return redirect(redirect_url + query_params)
     else:
          form = CoursForm(sousmatiere=sousmatiere)
     
     context = {'form': form , 'matiere': matiere, 'sousmatiere':sousmatiere}
     
     return render(request,'Prof/formulairecours.html', context) 

def handle_uploaded_file(f):
    with open('SchoolApp/Upload/' + f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)     
def update_cours(request, id_cours):
    cours = get_object_or_404(Cours, id_cours=id_cours)
    ssm = get_object_or_404(ComporteCours, Id_cours=cours)
    sousmatiere = SousMatiere.objects.filter( nom_sousmatiere=ssm.Id_SM)
    print(sousmatiere)
    matie = sousmatiere.values('matiere')[0]['matiere']
    matier = Matiere.objects.filter(id_matiere=matie)
    matiere = matier.values('nom_matiere')[0]['nom_matiere']
    form = CoursForm(instance=cours, initial={'sousmatiere': ssm.Id_SM})
    ccours = None  # Define ccours and assign None initially
    if request.method == "POST":
        form = CoursForm(request.POST, request.FILES, instance=cours)
        if form.is_valid():
            ssmatiere = form.cleaned_data.get('sousmatiere')
            ssmati = SousMatiere.objects.filter(nom_sousmatiere=ssmatiere)
            matie = ssmati.values('matiere')[0]['matiere']
            matier = Matiere.objects.filter(id_matiere=matie)
            matiere = matier.values('nom_matiere')[0]['nom_matiere']
            pdf_cours = form.cleaned_data['pdf_cours']
            if pdf_cours:
                handle_uploaded_file(pdf_cours)
                # Custom function to handle the uploaded file
            cours = form.save(commit=False)
            cours.save()
            # Mise à jour de l'association ComporteCours
            ccours = ComporteCours.objects.get(Id_cours=cours)
            ccours.Id_SM = form.cleaned_data['sousmatiere']
            ccours.save()
            redirect_url = reverse('coursprofs')
            query_params = f"?matiere={matiere}&sous_matiere={ssm.Id_SM}"
            return redirect(redirect_url + query_params)

    context = {'form': form, 'cours': cours, 'ccours': ccours , 'ssm' : ssm.Id_SM , 'matiere' : matiere  }
    return render(request, 'Prof/update_cours.html', context)

def delete_cours(request, id_cours):
    cours = get_object_or_404(Cours, id_cours=id_cours)
    cours= ComporteCours.objects.filter(Id_cours_id=cours)
    
    if request.method == "POST":
        ssmati= cours.values('Id_SM')[0]['Id_SM']
        ssmatiere=SousMatiere.objects.filter(id_sousmatiere=ssmati)
        ssmatierer=ssmatiere.values('nom_sousmatiere')[0]['nom_sousmatiere']
        ssm=ssmatiere.values('matiere')[0]['matiere']
        matier=Matiere.objects.filter(id_matiere=ssm)
        matiere=matier.values('nom_matiere')[0]['nom_matiere']
        cours.delete()
        redirect_url = reverse('coursprofs')
        query_params = f"?matiere={matiere}&sous_matiere={ssmatierer}"
        return redirect(redirect_url + query_params)
    context = {'cours': cours}
    return render(request, 'Prof/delete_cours.html', context)




def read_ssmatiere(request):
      ssmatieres = SousMatiere.objects.all()
      context = {'ssmatieres': ssmatieres}
      return render(request, 'Prof/read_ssmatiere.html', context)





def update_ssmatiere(request,  id_sousmatiere):

    ssmatieres = get_object_or_404(SousMatiere,  id_sousmatiere= id_sousmatiere)

    mat = request.GET.get('matiere')

    matiere = Matiere.objects.filter(nom_matiere=mat)

    formssmatiere = SousMatiereForm(matiere=matiere, instance=ssmatieres)

    if request.method == "POST":

        formssmatiere = SousMatiereForm(request.POST,matiere=matiere , instance=ssmatieres)

        if formssmatiere.is_valid():

             formssmatiere.save()

             return redirect('sousmatieres_professeur')

    context = {'formssmatiere': formssmatiere ,'ssmatieres':ssmatieres}

    return render(request, 'Prof/update_ssmatiere.html', context)


def delete_ssmatiere(request,id_sousmatiere):
 
    if request.method == "POST":
        ssmatieres = get_object_or_404(SousMatiere, id_sousmatiere= id_sousmatiere)
        ssmatieres.delete()
        return redirect('sousmatieres_professeur')

    context = {'ssmatieres': ssmatieres}
    return render(request, 'Prof/sousmatieres1.html', context)   
    
def addmatiere(request):
     formmatiere = MatiereForm()
     if request.method == "POST" :
         formmatiere= MatiereForm(request.POST)
         if formmatiere.is_valid():
            formmatiere.save()
            return redirect('matierestotal')
            
     else:
          formmatiere = MatiereForm()
     context = {'formmatiere': formmatiere}
     return render(request,'Admin/formulairematiere.html', context)
     

def update_matiere(request, id_matiere):
    matiere = get_object_or_404(Matiere, id_matiere=id_matiere)
    print(matiere)
    niveau = request.GET.get('niveau')
    print(niveau)
    formmatiere = MatiereForm(instance=matiere)
    if request.method == "POST":
        formmatiere = MatiereForm(request.POST, instance=matiere)
        if formmatiere.is_valid():
            niveaux = request.POST.get('niveau')
            print(niveaux)
            redirect_url = reverse('matieres')
            query_params = f"?niveau={niveaux}"
            formmatiere.save()
            return redirect(redirect_url + query_params)
    context = {'formmatiere': formmatiere, 'matiere': matiere, 'niveau': niveau}
    return render(request, 'Admin/update_matiere.html', context)

def delete_matiere(request, id_matiere):
    matiere = None
    niveau = request.GET.get('niveau')
    if request.method == "POST":
        matiere = get_object_or_404(Matiere, id_matiere=id_matiere) 
        matiere.delete()
        redirect_url = reverse('matieres')
        query_params = f"?niveau={niveau}"
        return redirect(redirect_url + query_params)
 

    context = {'matiere': matiere }
    return render(request, 'Admin/matieres.html', context)

class ViewMatierestotal(ListView):
    model = Matiere
    template_name = '../templates/Admin/matierestotal.html'
    context_object_name = 'matiere_list'
    success_url = reverse_lazy('matierestotal')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        matieres = Matiere.objects.all()
        enseignes = Enseigne.objects.all()  # Déplacer la requête à l'extérieur de la boucle
        context['matieres'] = matieres
        context['enseignes'] = enseignes
        return context
#############   Tout Ce qui concerne Professeur  ########################    

def ProfSalaire(request):
    if request.method == 'POST':
        form = SalaryPaymentFormProfesseur(request.POST)
        if form.is_valid():
            salary = form.save(commit=False)
            salary.id_compte = form.cleaned_data['cin_professeur'].compte
            salary.save()
            form = SalaryPaymentFormProfesseur()  # Create a new empty form
            # Handle successful form submission
    else:
        form = SalaryPaymentFormProfesseur()
    
    context = {'form': form}
    return render(request, 'Prof/ProfSalaire.html', context)

def send_emailprof(request):
    if request.method == 'POST':
        message = request.POST['message']
        email = request.POST['email']
        name = request.POST['name']
        send_mail(
            name,
            message,
            'settings.EMAIL_HOST_USER',
            [email],
            fail_silently=False
        )
    return render(request, 'Prof/send_email.html')


def ProfHistorique(request):
    prof_id = request.session.get('id_user')
    compte = Compte.objects.get(id_user=prof_id)
    prof = Professeur.objects.get(compte=compte)
    salaires = Salaire.objects.filter(id_compte=compte)
    context = {'salaires': salaires}

    return render(request, 'Prof/ProfHistorique.html', context)

def ProfDash(request):
    id = request.session.get('id_user')
    compte = Compte.objects.get(id_user=id)
    prof = Professeur.objects.get(compte_id=compte)
    context = {'prof': prof}
    return render(request, 'Prof/ProfDash.html', context)

def ProfPaiement(request):
    return render(request,'Prof\ProfPaiement.html')


def ProfAbsence(request):
    return render(request,'Prof\ProfAbscence.html')



def ProfElearning(request):
    return render(request,'Prof\ProfElearning.html')


def ProfClassesList(request):
    id = request.session.get('id_user')
    compte = Compte.objects.get(id_user=id)
    prof = Professeur.objects.get(compte_id=compte)
    inc = Enseigne.objects.filter(Id_professeur=prof)
    context = {'classe': []}
    for inclusion in inc:
        students = Eleve.objects.filter(id_classe=inclusion.Id_classe)
        context['classe'].append({'inclusion': inclusion, 'students': students})
    return render(request, 'Prof\ProfClassesList.html', context)


def ProfReclamation(request):
    if request.method == 'POST':
        message = request.POST['message']
        email = request.POST['email']
        name = request.POST['name']
        send_mail(
            name,
            f"Hello {email},\n\nThank you for reaching out to us via email. We received your reclamation about: {message}\n\nWe apologize for any inconvenience caused by the delay in our response.\n\nOur team is actively working on resolving the issue and will get back to you as soon as possible.\n\nIn the meantime, if you have any urgent concerns or questions, please feel free to contact us directly at +1234567890 during our business hours.\n\nThank you for your patience and understanding.\n\nBest regards",
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False
        )
        msg = Reclamation(email=email, name=name, message_reclamation=message)
        msg.save()
    return render(request, 'Prof\ProfReclamation.html')


def ProfAttClasses(request):
    id = request.session.get('id_user')
    compte = Compte.objects.get(id_user=id)
    prof = Professeur.objects.get(compte_id=compte)
    inc = Enseigne.objects.filter(Id_professeur=prof)
    context = {'classe': []}
    for inclusion in inc:
        students = Eleve.objects.filter(id_classe=inclusion.Id_classe)
        context['classe'].append({'inclusion': inclusion, 'students': students})
    return render(request, 'Prof\ProfAttClasses.html', context)

from datetime import date ,datetime,timedelta
from datetime import date

def ProfAttendanceList(request, classe_id):
    today = timezone.now().date()
    id = request.session.get('id_user')
    compte = Compte.objects.get(id_user=id)
    prof = Professeur.objects.get(compte_id=compte)
    pl = Enseigne.objects.filter(Id_professeur=prof)
    selected_class = Classe.objects.get(id_classe=classe_id)
    list = ListePresence.objects.filter(classe=selected_class, date__date=today)
    prs_students = list.filter(etat=True).values()
    pres_students = ListePresence.objects.filter(etat=True).values_list('cne_eleve_id', flat=True)
    abs_students = Eleve.objects.exclude(cne_eleve__in=pres_students).filter(id_classe=selected_class) 
    present_students_with_classe = []
    for student in prs_students:
        try:
            cne_eleve = student['cne_eleve_id']
            eleve = Eleve.objects.get(cne_eleve=cne_eleve)
            classe = Classe.objects.get(id_classe=student['classe_id'])
            if classe == selected_class:
                present_students_with_classe.append((eleve, classe, student['date']))
        except Eleve.DoesNotExist:
            pass
        except Classe.DoesNotExist:
            pass
    context = {
        'pl': pl,
        'list': list,
        'abs_students': abs_students,
        'prs_students': prs_students,
        'pres_students': pres_students,
        'present_students': present_students_with_classe,
        'selected_class': selected_class,
    }
    return render(request, 'Prof/ProfAttendanceList.html', context)

def ProfAbsDash(request):
    id = request.session.get('id_user')
    compte = Compte.objects.get(id_user=id)
    prof = Professeur.objects.get(compte_id=compte)
    context = {'prof': prof}
    return render(request, 'Prof/ProfAbsDash.html', context)






from .models import Compte, Professeur, Enseigne, avoir

def Homework(request):
    id_user = request.session.get('id_user')
    compte = Compte.objects.get(id_user=id_user)
    professeur = Professeur.objects.get(compte=compte)
    ens_list = Enseigne.objects.filter(Id_professeur=professeur)
    
    if ens_list.exists():
        val1 = ens_list[0].Id_matiere
        avoi_list = avoir.objects.filter(Id_matiere=val1)
    else:
        val1 = None
        avoi_list = []
    
    context = {'val1': val1, 'avoi_list': avoi_list}
    return render(request, 'Prof/Devoir.html', context)














def AddHomeWork(request):
    id_user = request.session.get('id_user')
    compte = Compte.objects.get(id_user=id_user)
    professeur = Professeur.objects.get(compte=compte)
    ens_list = Enseigne.objects.filter(Id_professeur=professeur)

    if ens_list.exists():
        val1 = ens_list[0].Id_matiere
        classe_name = ens_list[0].Id_classe.nom_classe
        avoi_list = avoir.objects.filter(Id_matiere=val1)
    else:
        val1 = None
        classe_name = None
        avoi_list = []

    if request.method == "POST":
        form = DevoirForm(request.POST,ens_list=ens_list)
        if form.is_valid():
            devoir = form.save()
            if val1 is not None:
                avoi = avoir(Id_matiere=val1, Id_devoir=devoir)
                avoi.save()
            return redirect('Devoir')
    else:
        form = DevoirForm(ens_list=ens_list)

    context = {'form': form, 'val1': val1, 'classe_name': classe_name, 'avoi_list': avoi_list}
    return render(request, 'Prof/AddDevoir.html', context)






def RemoveHomeWork(request, devoir_id):
    try:
        devoir = Devoir.objects.get(id_devoir=devoir_id)
    except Devoir.DoesNotExist:
        raise Http404("Devoir does not exist")

    devoir.delete()
    messages.success(request, "Devoir removed successfully.")
    return redirect('Devoir')



def UpdateHomework(request, devoir_id):
    devoir = get_object_or_404(Devoir, id_devoir=devoir_id)
    id_user = request.session.get('id_user')
    compte = Compte.objects.get(id_user=id_user)
    professeur = Professeur.objects.get(compte=compte)
    ens_list = Enseigne.objects.filter(Id_professeur=professeur)
    if request.method == "POST":
        form = DevoirForm(request.POST,ens_list=ens_list, instance=devoir)
        if form.is_valid():
            form.save()
            return redirect('Devoir')
    else:
        form = DevoirForm(ens_list=ens_list,instance=devoir)

    context = {'form': form}
    return render(request, 'Prof/UpdateDevoir.html', context)
#############   Tout Ce qui concerne Eleve  ########################    





#############   Tout Ce qui concerne Parent  ########################  

def ParentAbsence(request):
    return render(request,'Parent\ParentAbsence.html')

def ParentPaiement(request):
    return render(request,'Parent\ParentPaiement.html')

def ParentElearning(request):
    return render(request,'Parent\ParentElearning.html')
  
def ParentDash(request):
    id = request.session.get('id_user')
    compte = Compte.objects.get(id_user=id)
    parent = Parent.objects.get(compte_id=compte)
    context = { 'parent':parent, 'compte':compte}
    return render(request, 'Parent/ParentDash.html', context)


def ParentAbsence(request):
    return render(request,'Parent\ParentAbsence.html')

def ParentPaiement(request):
    return render(request,'Parent\ParentPaiement.html')

def ParentElearning(request):
    return render(request,'Parent\ParentElearning.html')


def ParentReclamation(request):
    if request.method == 'POST':
        message = request.POST['message']
        email = request.POST['email']
        name = request.POST['name']
        send_mail(
            name,
            f"Hello {email},\n\nThank you for reaching out to us via email. We received your reclamation about: {message}\n\nWe apologize for any inconvenience caused by the delay in our response.\n\nOur team is actively working on resolving the issue and will get back to you as soon as possible.\n\nIn the meantime, if you have any urgent concerns or questions, please feel free to contact us directly at +1234567890 during our business hours.\n\nThank you for your patience and understanding.\n\nBest regards",
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False
        )
        msg = Reclamation(email=email, name=name, message_reclamation=message)
        msg.save()
    return render(request, 'Parent\ParentReclamation.html')


def ParentQr(request):
    id = request.session.get('id_user')
    compte = Compte.objects.get(id_user=id)
    parent = Parent.objects.get(compte_id=compte)
    eleve = parent.get_eleves()
    classe = Classe.objects.values('id_classe','niveau_classe')
    selected_cne = request.POST.get('cne')
    selected_eleve = Eleve.objects.filter(cin_parent=parent, cne_eleve=selected_cne)

    context={'classe':classe,'parent':parent, 'eleve':eleve,'compte':compte,'selected_eleve': selected_eleve}
    return render(request, 'Parent\ParentQr.html',context)


def inscription(request):
    id = request.session.get('id_user')
    if request.method == 'POST':
        prenom = request.POST['Prenom']
        numer = request.POST['Numero']
        nom = request.POST.get('nom')
        cne = request.POST.get('cne')
        qr_code = request.POST['qr_code']
        classe = request.POST.get('classe')
        try:
            obj1 = Parent.objects.get(cin_parent=numer)
            obj2 = Classe.objects.get(id_classe=classe)
            obj3 = Compte.objects.get(nom=nom, prenom=prenom,type_compte=5)
        except (Parent.DoesNotExist, Classe.DoesNotExist, Compte.DoesNotExist):
            message = 'One or more objects do not exist'
            return render(request, 'Parent\ParentQr.html', {'message': message})

        obj = Eleve.objects.filter(compte=obj3, cne_eleve=cne, id_classe=obj2, cin_parent=obj1).exists()
        if obj:
            obj5 = Eleve(compte=obj3, cne_eleve=cne, id_classe=obj2, cin_parent=obj1, qr_code=qr_code)
            obj5.save()
            message = 'Qr code saved successfully!'
            return render(request, 'Parent\ParentQr.html', {'message': message})
        else:
            message = 'One or more objects do not exist'
            return render(request, 'Parent\ParentQr.html', {'message': message})


def ParentAbsDash(request):
    id = request.session.get('id_user')
    compte = Compte.objects.get(id_user=id)
    parent = Parent.objects.get(compte_id=compte)
    notifications = AbsenceNotif.objects.filter(parent_email=parent.compte.email).order_by('-sent_date')
    context = {'notifications': notifications, 'parent':parent, 'compte':compte}
    return render(request, 'Parent/ParentAbsDash.html', context)


def ParentAbsList(request):
    id = request.session.get('id_user')
    compte = Compte.objects.get(id_user=id)
    parent = Parent.objects.get(compte_id=compte)
    eleves = Eleve.objects.filter(cin_parent=parent)
    list = ListePresence.objects.filter(classe__in=eleves.values('id_classe'))
    pres_students = ListePresence.objects.filter(etat=True).values_list('cne_eleve_id', flat=True)
    prs_students = ListePresence.objects.values().filter(etat=True)
    all_students = Eleve.objects.all()
    abs_students = Eleve.objects.exclude(cne_eleve__in=pres_students)
    present_students_with_classe = []
    for student in prs_students:
        try:
            cne_eleve = student['cne_eleve_id']
            eleve = Eleve.objects.get(cne_eleve=cne_eleve)
            classe = Classe.objects.get(id_classe=student['classe_id'])
            present_students_with_classe.append((eleve, classe, student['date']))
        except Eleve.DoesNotExist:
            pass
        except Classe.DoesNotExist:
            pass
    context = {
        'list': list,
        'abs_students': abs_students,
        'prs_students': prs_students,
        'pres_students': pres_students,
        'present_students': present_students_with_classe,
    }
    return render(request, 'Parent/ParentAbsList.html', context)


def ParentHistoryList(request):
    id = request.session.get('id_user')
    compte = Compte.objects.get(id_user=id)
    prof = Parent.objects.get(compte_id=compte)
    inc = Eleve.objects.filter(cin_parent=prof)
    context = {'classe': []}

    for inclusion in inc:
        students = Paiement.objects.filter(cne_eleve=inclusion.cne_eleve)
        context['classe'].append({'inclusion': inclusion, 'students': students})
    return render(request, 'parent/paiements_eleve.html', context)


def send_emailaparent(request):
    if request.method == 'POST':
        message = request.POST['message']
        email = request.POST['email']
        name = request.POST['name']
        send_mail(
            name,
            message,
            'settings.EMAIL_HOST_USER',
            [email],
            fail_silently=False
        )
    return render(request, 'Parent/send_email.html')

def ParentPaiement(request):
    return render(request,'Parent\ParentPaiement.html')









#############   Tout Ce qui concerne Agent  ########################                    
def AgentAbsence(request):
    return render(request,'Agent\AgentAbsence.html')

def AgentPaiement(request):
    return render(request,'Agent\AgentPaiement.html')
   


def AgentScanner(request):
    return render(request, 'Agent\AgentScanner.html')


def AgentScanHistory(request):
    id = request.session.get('id_user')
    compte = Compte.objects.get(id_user=id)
    agent = Agent.objects.get(compte_id=compte)
    scan = Scanne.objects.filter(Id_agent=agent)
    context = {'scan': scan}
    return render(request, 'Agent\AgentScanHistory.html', context)


def AgentReclamation(request):
    if request.method == 'POST':
        message = request.POST['message']
        email = request.POST['email']
        name = request.POST['name']
        send_mail(
            name,
            f"Hello {email},\n\nThank you for reaching out to us via email. We received your reclamation about: {message}\n\nWe apologize for any inconvenience caused by the delay in our response.\n\nOur team is actively working on resolving the issue and will get back to you as soon as possible.\n\nIn the meantime, if you have any urgent concerns or questions, please feel free to contact us directly at +1234567890 during our business hours.\n\nThank you for your patience and understanding.\n\nBest regards",
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False
        )
        msg = Reclamation(email=email, name=name, message_reclamation=message)
        msg.save()
    return render(request, 'Agent\AgentReclamation.html')

def AgentAbsDash(request):
    id = request.session.get('id_user')
    compte = Compte.objects.get(id_user=id)
    agent = Agent.objects.get(compte_id=compte)
    context = {'agent': agent}
    return render(request, 'Agent\AgentAbsDash.html', context)


def AgentDash(request):
    id = request.session.get('id_user')
    compte = Compte.objects.get(id_user=id)
    agent = Agent.objects.get(compte_id=compte)
    context = {'agent': agent}
    return render(request, 'Agent\AgentDash.html', context)

def AgentSalaire(request):
    id = request.session.get('id_user')

    if request.method == 'POST':
        form = SalaryPaymentFormAgent(request.POST)
        if form.is_valid():
            salary = form.save(commit=False)
            salary.id_compte = form.cleaned_data['cin_agent'].compte
            salary.save()
            form = SalaryPaymentFormAgent()  
    else:
        form = SalaryPaymentFormAgent()
    
    context = {'form': form}
    return render(request, 'Agent/AgentSalaire.html', context)

from datetime import datetime, time

def AdminNotifAbs(request, eleve_id):
    eleve = Eleve.objects.get(cne_eleve=eleve_id)
    parent = Parent.objects.get(cin_parent=eleve.cin_parent_id)
    subject = f' Absence Notification for Student"s {eleve.compte.prenom} {eleve.compte.nom}'
    message = f'Dear parent, your child {eleve.compte.prenom} {eleve.compte.nom} is absent from school today.'
    send_mail(subject, message, 'oussamamoustarzik5@gmail.com', [parent.compte.email])
    notification = AbsenceNotif(parent_email=parent.compte.email, subject=subject, message=message)
    notification.save()
    return render(request, 'Admin/AdminAbsList.html')



def scan1(request):
    id = request.session.get('id_user')
    compte = Compte.objects.get(id_user=id)
    agent = Agent.objects.get(compte_id=compte)
    
    if request.method == 'POST':
        lis1 = ListePresence()
        qr_code_etu = request.POST.get('scan')
        
        try:
            etu = Eleve.objects.get(qr_code=qr_code_etu)
        except Eleve.DoesNotExist:
            message = 'Invalid QR code! Please try again.'
            return render(request, 'Agent\AgentScanner.html', {'message': message})
        
        c1 = etu.id_classe
        start_time1 = time(hour=8, minute=0, second=0)
        end_time1 = time(hour=8, minute=30, second=0)
        start_time2 = time(hour=14, minute=0, second=0)
        end_time2 = time(hour=15, minute=50, second=0)
        
        timezone = get_current_timezone()
        
        current_datetime = datetime.combine(datetime.today(), datetime.now().time())
        current_time = make_aware(current_datetime, timezone)
        
        if current_time.weekday() >= 5:
            message = 'Weekend! Attendance not recorded.'
        else:
            attendance_time = make_aware(datetime.now(), timezone)
            allowed_start_time = datetime.combine(datetime.today(), start_time1)
            late_threshold = allowed_start_time + timedelta(minutes=10)
            
            if (start_time1 <= current_time.time() <= end_time1) or (start_time2 <= current_time.time() <= end_time2):
                if attendance_time < late_threshold:
                    present1 = ListePresence(cne_eleve=etu, etat=True, date=datetime.now(), classe_id=c1.id_classe)
                    av = AvoirClasse(Id_liste=present1, Id_classe=c1)
                    present1.save()
                    av.save()
                    message = 'Scan saved successfully!'
                else:
                    message = 'Student arrived late but not marked as absent.'
            else:
                present = ListePresence(cne_eleve=etu, etat=False, date=datetime.now(), classe_id=c1.id_classe)
                av = AvoirClasse(Id_liste=present, Id_classe=c1)
                present.save()
                av.save()
                message = 'Request Time Out!'
                AdminNotifAbs(request, etu.cne_eleve)
        
        scan = Scanne(Id_agent=agent, CNE_eleve=etu, date_heure=datetime.now())
        scan.save()

        return render(request, 'Agent\AgentScanner.html', {'message': message})




def AgentHistorique(request):
    agent_id = request.session.get('id_user')
    compte = Compte.objects.get(id_user=agent_id)
    agent = Agent.objects.get(compte=compte)
    salaires = Salaire.objects.filter(id_compte=compte)
    context = {'salaires': salaires}

    return render(request, 'agent/AgentHistorique.html', context)

def send_emailagent(request):
    if request.method == 'POST':
        message = request.POST['message']
        email = request.POST['email']
        name = request.POST['name']
        send_mail(
            name,
            message,
            'settings.EMAIL_HOST_USER',
            [email],
            fail_silently=False
        )
    return render(request, 'Agent/send_email.html')



def AdminReclamationelearning(request):
    id = request.session.get('id_user')
    compte = Compte.objects.get(id_user=id)
    admin = Admin.objects.get(compte_id=compte)
    recl = Reclamation.objects.filter(admin=admin)
    rec = Reclamation.objects.all()
    context = {'rec':rec}
    return render(request,'Admin/reclamation.html', context)






class ViewEcoles(ListView):
    model=Ecole
    template_name='../templates/Admin/ecoles.html'
    context_object_name='ecole_list'
    success_url = reverse_lazy('ecoles')

def addecole(request):
     form = EcoleForm()

     if request.method == "POST" :
         form= EcoleForm(request.POST)
         if form.is_valid():
            form.save()
            return redirect('ecoles')
     else:
          form = EcoleForm()
     context = {'form': form,}
     return render(request,'Admin/formulaireecole.html', context) 




def update_ecole(request, id_ecole):
    ecoles = get_object_or_404(Ecole, id_ecole=id_ecole)
    form = EcoleForm(instance=ecoles)
    if request.method == "POST":
        form = EcoleForm(request.POST, instance=ecoles)
        if form.is_valid():
             form.save()
             return redirect('ecoles')
    context = {'form': form ,'ecoles':ecoles}
    return render(request, 'Admin/update_ecole.html', context)
    

def delete_ecole(request, id_ecole):
    ecoles = get_object_or_404(Ecole, id_ecole=id_ecole)
    if request.method == "POST":
        ecoles.delete()
        return redirect('ecoles')

    context = {'ecoles': ecoles}
    return render(request, 'Admin/delete_ecole.html', context)






class classeProf(ListView):
    model=Enseigne
    template_name='../templates/Prof/classeprof.html'
    context_object_name='classeP_list'
    paginate_by=3
    def get_queryset(self):
        id = self.request.session.get('id_user')
        print(id)
        if id:
            
            queryset = Enseigne.objects.filter(Id_professeur__compte_id=id)
            return queryset
        else:
           return Enseigne.objects.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.request.session.get('id_user')
        if id:
            professor = Compte.objects.get(id_user=id)
            pr=professor.nom
            context['professor_name'] = pr
        
        return context

class ViewElevesP(ListView):
   model = Eleve
   template_name ='../templates/Prof/eleveprof.html'
   context_object_name='eleve_list'
   paginate_by = 10
   def get_queryset(self):
      classe_id = self.request.GET.get('classe')
      
      if classe_id:
            print(classe_id)
            classe = get_object_or_404(Classe, id_classe=classe_id)
            print(classe)
            queryset = Eleve.objects.filter(id_classe__nom_classe=classe)
            return queryset
      else:
            return Eleve.objects.all()      

class ViewNotesP(ListView):
    model=Passe
    template_name='../templates/Prof/notesprof.html'
    context_object_name='passe_list'
    paginate_by=10
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.request.session.get('id_user')
        cne_eleve = self.request.GET.get('cne_eleve')
        if cne_eleve:
            eleve=Eleve.objects.get(cne_eleve=cne_eleve)
            enss= Enseigne.objects.filter(Id_professeur__compte_id=id, Id_classe= eleve.id_classe)
            print(enss)
            if enss.exists():
                values = []
                note_list = []
                epreuve_list = []
                for ens in enss:
                    matieres = [ens.Id_matiere] if isinstance(ens.Id_matiere, Matiere) else ens.Id_matiere.all()
                    print(matieres)
                    for matiere in matieres:
                        ens1 = SousMatiere.objects.filter(matiere_id=matiere)
                        eprv = Eprv.objects.filter(classe=ens.Id_classe)
                        for eprv_obj in eprv:
                            for ssmatiere in ens1:
                                epreuve = Se_Comporte.objects.filter(sousmatiere=ssmatiere, epreuve=eprv_obj.epreuve)
                                for entry in epreuve:
                                    epreuve_list.append((entry.epreuve, entry.sousmatiere, entry.epreuve_id))
                                    ent = entry.epreuve_id
                                    try:
                                        passe = Passe.objects.get(id_epreuve=ent, CNE_eleve=cne_eleve)
                                        note_list.append((ent, passe.Note, passe.id_epreuve))
                                        print(note_list)
                                    except ObjectDoesNotExist:
                                        pass
                                   
                                    
                    
                    values.append((matiere, ens1, epreuve_list, note_list))
              
                context ={'values': values, 'eleve': eleve}
                
        print(values)
        return context


class ViewEpreuves(ListView):
    model=Se_Comporte
    template_name='../templates/Prof/epreuves.html'
    context_object_name='epreuve_list'
    success_url = reverse_lazy('epreuves')       
    def get_context_data(self, **kwargs):
           context = super().get_context_data(**kwargs)
           id = self.request.session.get('id_user')
           id_prof=Professeur.objects.get(compte_id=id)
           ens = Enseigne.objects.filter(Id_professeur=id_prof)
           epreuves =[]
           for ens in ens :
                 print(ens.Id_classe)
                 print(ens.Id_matiere)
                 cla=Enseigne.objects.filter()
                 
                 classe = Eprv.objects.filter(classe_id=ens.Id_classe)
                 for classe in classe :
                      epreuve = Se_Comporte.objects.filter(sousmatiere__matiere=ens.Id_matiere, epreuve=classe.epreuve )

                      epreuves.extend(epreuve)

           cla=[]
           for epreuve in epreuves :
               epr = Eprv.objects.filter(epreuve=epreuve.id)
               cla.extend(epr)
           

           for epreuve in epreuves:
               print(epreuve)
             
           context = {'epreuves': epreuves , 'classe': cla} 
           return context 
           



@transaction.atomic
def addepreuve(request):
     id = request.session.get('id_user')
     print(id)
     ens_qs = Enseigne.objects.filter(Id_professeur__compte_id=id)
     if request.method == "POST" :
         form= EpreuveForm(ens_qs,request.POST)
         if form.is_valid():
            ssmatiere=form.cleaned_data.get('Sousmatiere')
            classe=form.cleaned_data.get('classe')
            ssp=form.save()
            ssm=Se_Comporte.objects.create(epreuve=ssp, sousmatiere=ssmatiere)
            epr=Eprv.objects.create(epreuve=ssp, classe=classe)
            return redirect('epreuves')
     else:
          form = EpreuveForm(ens_qs)
     context = {'form': form}
     return render(request,'Prof/formulaireepreuve.html', context) 
     

def update_epreuve(request, id_epreuve):
    id = request.session.get('id_user')
    print(id)
    ens_qs = Enseigne.objects.filter(Id_professeur__compte_id=id)
    epreuve = get_object_or_404(Epreuve, id_epreuve=id_epreuve)
    ssm=get_object_or_404(Se_Comporte, epreuve= epreuve) 
    eprv=get_object_or_404(Eprv, epreuve= epreuve) 
    form = EpreuveForm(ens_qs, instance=epreuve, initial={'Sousmatiere': ssm.sousmatiere, 'classe': eprv.classe})
    if request.method == "POST":
        form = EpreuveForm(ens_qs, request.POST, instance=epreuve)  
        if form.is_valid(): 
             with transaction.atomic():
              form.save()
              Sousmatiere = form.cleaned_data['Sousmatiere']
              classe = form.cleaned_data['classe']
              Se_Comporte.objects.filter(id=ssm.id).update(sousmatiere=Sousmatiere, epreuve=epreuve)
              Eprv.objects.filter(id=eprv.id).update(classe=classe, epreuve=epreuve)
             return redirect('epreuves')
    context = {'form': form ,'epreuve':epreuve}
    return render(request, 'Prof/update_epreuve.html', context)

def delete_epreuve(request, id_epreuve):
    if request.method == "POST":    
        epreuve = get_object_or_404(Epreuve, id_epreuve=id_epreuve)
        ssm=get_object_or_404(Se_Comporte, epreuve= epreuve) 
        epreuve.delete()
        ssm.delete
        return redirect('epreuves')
    else : 
        return redirect('epreuves')
    






def addnote(request):
    epreuve_id = request.GET.get('epreuve')
    clas = Eprv.objects.filter(epreuve_id=epreuve_id)
    cla = []  
    for cl in clas:
        cla.append(cl.classe_id)

    eleves = Eleve.objects.filter(id_classe__in=cla)
    epreuve = Epreuve.objects.get(id_epreuve=epreuve_id)
    val = Passe.objects.filter(id_epreuve=epreuve)

    if request.method == "POST":
        for eleve in eleves:
            note_key = f'note_{eleve.cne_eleve}'
            note = request.POST.get(note_key)

            if note is not None: 
                try:
                    note = int(note)
                    if 0 <= note <= 20:
                        try:
                            passe = Passe.objects.get(CNE_eleve=eleve, id_epreuve=epreuve)
                            passe.Note = note
                            passe.save()
                            messages.success(request, f"valid grade for {eleve.compte}.")
                            print("kyn")
                            

                            
                        except Passe.DoesNotExist:
                            Passe.objects.create(Note=note, CNE_eleve=eleve, id_epreuve=epreuve)
                        return redirect('epreuves')
                    else:
                        note=0
                        messages.error(request, f"Invalid grade for {eleve.compte}. Grades must be between 0 and 20.")

                except ValueError:
                    messages.error(request, f"Invalid grade for {eleve.compte}. Please enter a valid note.")
            else:
                return redirect('epreuves')
    context = {'eleve_list': eleves, 'epreuve': epreuve_id, 'val': val}
    return render(request, 'Prof/addnote.html', context)

















def ProfReclamationelearning(request):
    if request.method == 'POST':
        message = request.POST['message']
        email = request.POST['email']
        name = request.POST['name']
        send_mail(
            name,
             f"Hello {email},\n\nThank you for reaching out to us via email. We received your reclamation about: {message}\n\nWe apologize for any inconvenience caused by the delay in our response.\n\nOur team is actively working on resolving the issue and will get back to you as soon as possible.\n\nIn the meantime, if you have any urgent concerns or questions, please feel free to contact us directly at +1234567890 during our business hours.\n\nThank you for your patience and understanding.\n\nBest regards",
            'settings.EMAIL_HOST_USER',
            [email],
            fail_silently=False
        )
        msg = Reclamation(email=email, name=name, message_reclamation=message)
        msg.save()
    return render(request, 'Prof\ProfReclamation1.html')