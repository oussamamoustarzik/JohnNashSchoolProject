from xml.dom import ValidationErr
from django import forms
from .models import *
from django import forms
from django.db import models, transaction
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, get_object_or_404

class LoginAgent(forms.Form):
    Username = forms.CharField(label="Username", max_length=100,required=True)
    password = forms.CharField(widget=forms.PasswordInput(render_value=False))

   

class ClasseFileUploadForm(forms.Form):
    file = forms.FileField()


class LoginAdmin(forms.Form):
    Username = forms.CharField(label="Username", max_length=100,required=True)
    password = forms.CharField(widget=forms.PasswordInput(render_value=False))

class LoginParent(forms.Form):
    Username = forms.CharField(label="Username", max_length=100,required=True)
    password = forms.CharField(widget=forms.PasswordInput(render_value=False))


class LoginEleve(forms.Form):
    Username = forms.CharField(label="Username", max_length=100,required=True)
    password = forms.CharField(widget=forms.PasswordInput(render_value=False))

class LoginProf(forms.Form):
    Username = forms.CharField(label="Username", max_length=100,required=True)
    password = forms.CharField(widget=forms.PasswordInput(render_value=False))

class AjoutAgent(UserCreationForm): 
   nom = forms.CharField(max_length=50, )
   prenom = forms.CharField(max_length=50)
   email = forms.CharField(max_length=50)
   adresse = forms.CharField(max_length=50)
   tel = forms.CharField(max_length=50)
   lieu_naissance = forms.CharField(max_length=50)
   date_naissance = forms.DateField()
   Gender=((1,"Male"),(2,"Female"))
   gender = forms.ChoiceField(choices=Gender)
   nationnalite = forms.CharField(max_length=50)
   CIN_Agent = forms.CharField()  

   class Meta(UserCreationForm.Meta):
      model = Compte

   @transaction.atomic
   def save(self):
        compte = super().save(commit=False)
        compte.nom=self.cleaned_data.get('nom')
        compte.prenom=self.cleaned_data.get('prenom')
        compte.email = self.cleaned_data.get('email')
        compte.adresse = self.cleaned_data.get('adresse')
        compte.tel = self.cleaned_data.get('tel')
        compte.lieu_naissance = self.cleaned_data.get('lieu_naissance')
        compte.date_naissance = self.cleaned_data.get('date_naissance')
        compte.sexe = self.cleaned_data.get('gender')
        compte.nationnalite =self.cleaned_data.get('nationnalite')
        compte.type_compte = '4'
        compte.save()
        cin_agent=self.cleaned_data.get('CIN_Agent')
        agent = Agent.objects.create(compte=compte, cin_agent=cin_agent)
        agent.save()
        return compte
   def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None

class EditAgentForm(forms.ModelForm):
     cin_agent = forms.CharField(max_length=50)
    
     class Meta:
        model =Compte
        fields = [
            'cin_agent',
            'nom',
            'prenom',
            'email',
            'tel',
            'adresse',
        ]
  
class AjoutEleve(UserCreationForm):
   nom = forms.CharField(max_length=50, )
   prenom = forms.CharField(max_length=50)
   email = forms.CharField(max_length=50)
   adresse = forms.CharField(max_length=50)
   tel = forms.CharField(max_length=50)
   lieu_naissance = forms.CharField(max_length=50)
   date_naissance = forms.DateField()
   Gender=((1,"Male"),(2,"Female"))
   gender = forms.ChoiceField(choices=Gender)
   nationnalite = forms.CharField(max_length=50)
   CNE = forms.CharField()  
   Classe =  forms.ModelChoiceField(queryset=Classe.objects.all())
   parent =  forms.ModelChoiceField(queryset=Parent.objects.all())

   class Meta(UserCreationForm.Meta):
      model = Compte

   @transaction.atomic
   def save(self):
        compte = super().save(commit=False)
        compte.nom=self.cleaned_data.get('nom')
        compte.prenom=self.cleaned_data.get('prenom')
        compte.email = self.cleaned_data.get('email')
        compte.adresse = self.cleaned_data.get('adresse')
        compte.tel = self.cleaned_data.get('tel')
        compte.lieu_naissance = self.cleaned_data.get('lieu_naissance')
        compte.date_naissance = self.cleaned_data.get('date_naissance')
        compte.sexe = self.cleaned_data.get('gender')
        compte.nationnalite =self.cleaned_data.get('nationnalite')
        compte.type_compte = '5'
        compte.save()
        cne_eleve=self.cleaned_data.get('CNE')
        id_classe=self.cleaned_data.get('Classe')
        cin_parent=self.cleaned_data.get('parent')
        eleve = Eleve.objects.create(compte=compte, cne_eleve=cne_eleve, id_classe=id_classe, cin_parent=cin_parent)
        eleve.save()
        return compte
   def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None

class EditEleveForm(forms.ModelForm):
     cne_eleve = forms.CharField(max_length=50)
     classe =  forms.ModelChoiceField(queryset=Classe.objects.all())
     parent =  forms.ModelChoiceField(queryset=Parent.objects.all())
     class Meta:
        model =Compte
        fields = [
            'cne_eleve',
            'classe',
            'parent',
            'nom',
            'prenom',
            'email',
            'tel',
            'adresse',
        ]

  #===============Crud-Professeur============#
class AjoutProf(UserCreationForm):
   nom = forms.CharField(max_length=50, )
   prenom = forms.CharField(max_length=50)
   email = forms.CharField(max_length=50)
   adresse = forms.CharField(max_length=50)
   tel = forms.CharField(max_length=50)
   lieu_naissance = forms.CharField(max_length=50)
   date_naissance = forms.DateField()
   Gender=((1,"Male"),(2,"Female"))
   gender = forms.ChoiceField(choices=Gender)
   nationnalite = forms.CharField(max_length=50)
   CIN = forms.CharField()  

   class Meta(UserCreationForm.Meta):
      model = Compte

   @transaction.atomic
   def save(self):
        compte = super().save(commit=False)
        compte.nom=self.cleaned_data.get('nom')
        compte.prenom=self.cleaned_data.get('prenom')
        compte.email = self.cleaned_data.get('email')
        compte.adresse = self.cleaned_data.get('adresse')
        compte.tel = self.cleaned_data.get('tel')
        compte.lieu_naissance = self.cleaned_data.get('lieu_naissance')
        compte.date_naissance = self.cleaned_data.get('date_naissance')
        compte.sexe = self.cleaned_data.get('gender')
        compte.nationnalite =self.cleaned_data.get('nationnalite')
        compte.type_compte = '2'
        compte.save()
        cin_professeur=self.cleaned_data.get('CIN')
        prof = Professeur.objects.create(compte=compte, cin_professeur=cin_professeur)
        prof.save()
        return compte
   def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None

class EditProfForm(forms.ModelForm):
     cin_professeur = forms.CharField(max_length=50)
     class Meta:
        model =Compte
        fields = [
            'cin_professeur',
            'nom',
            'prenom',
            'email',
            'tel',
            'adresse',
        ]
#===============Crud-Admin============#
class AjoutAdmin(UserCreationForm):
    nom = forms.CharField(max_length=50)
    prenom = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=50)
    adresse = forms.CharField(max_length=50)
    tel = forms.CharField(max_length=50)
    lieu_naissance = forms.CharField(max_length=50)
    date_naissance = forms.DateField(widget=forms.DateInput())
    Gender = ((1, "Male"), (2, "Female"))
    gender = forms.ChoiceField(choices=Gender)
    nationalite = forms.CharField(max_length=50)
    cin_Admin = forms.CharField()

    class Meta(UserCreationForm.Meta):
        model = Compte

    @transaction.atomic
    def save(self):
        compte = super().save(commit=False)
        compte.nom = self.cleaned_data.get('nom')
        compte.prenom = self.cleaned_data.get('prenom')
        compte.email = self.cleaned_data.get('email')
        compte.adresse = self.cleaned_data.get('adresse')
        compte.tel = self.cleaned_data.get('tel')
        compte.lieu_naissance = self.cleaned_data.get('lieu_naissance')
        compte.date_naissance = self.cleaned_data.get('date_naissance')
        compte.sexe = self.cleaned_data.get('gender')
        compte.nationalite = self.cleaned_data.get('nationalite')
        compte.type_compte = '1'
        compte.save()
        cin_admin = self.cleaned_data.get('cin_Admin')
        admin = Admin.objects.create(compte=compte, cin_admin=cin_admin)
        admin.save()
        return compte

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None



class EditAdminForm(forms.ModelForm):
     cin_admin = forms.CharField(max_length=50)
     class Meta:
        model =Compte
        fields = [
            'cin_admin',
            'nom',
            'prenom',
            'email',
            'tel',
            'adresse',
        ]    
        #'================CLASSE===================='#

class ClasseForm(forms.ModelForm):
  class Meta:
    model = Classe
    fields = "__all__"
    widgets={
    } 
  def  clean_emploie_temps(self):
        emploie_temps = self.cleaned_data['emploie_temps']
        allowed_extensions = ['.xls', '.xml', '.pdf']
        if not emploie_temps.name.lower().endswith(tuple(allowed_extensions)):
            raise forms.ValidationError('Only XLS, XML, and PDF files are allowed.File size should not exceed 2.5MB')
        return emploie_temps
class EditParentForm(forms.ModelForm):
     cin_parent = forms.CharField(max_length=50)
     class Meta:
        model =Compte
        fields = [
            'cin_parent',
            'nom',
            'prenom',
            'email',
            'tel',
            'adresse',
        ]
  


class AjoutParent(UserCreationForm):   
    nom = forms.CharField(max_length=50)
    prenom = forms.CharField(max_length=50)
    email = forms.CharField(max_length=50)
    adresse = forms.CharField(max_length=50)
    tel = forms.CharField(max_length=50)
    lieu_naissance = forms.CharField(max_length=50)
    date_naissance = forms.DateField()
    Gender=((1,"Men"),(2,"Women"))
    sexe = forms.ChoiceField(choices=Gender)
    nationnalite = forms.CharField(max_length=50)
    cin_parent = forms.CharField(max_length=50)

    class Meta(UserCreationForm.Meta):
       model = Compte

    @transaction.atomic
    def save(self):
       compte = super().save(commit=False)
       compte.nom=self.cleaned_data.get('nom')
       compte.prenom=self.cleaned_data.get('prenom')
       compte.email = self.cleaned_data.get('email')
       compte.adresse = self.cleaned_data.get('adresse')
       compte.tel = self.cleaned_data.get('tel')
       compte.lieu_naissance = self.cleaned_data.get('lieu_naissance')
       compte.date_naissance = self.cleaned_data.get('date_naissance')
       compte.sexe = self.cleaned_data.get('sexe')
       compte.nationnalite =self.cleaned_data.get('nationnalite')
       compte.type_compte='3'
       compte.save()
       cin_parent= self.cleaned_data.get('cin_parent')
       parent = Parent.objects.create(compte=compte, cin_parent=cin_parent)
       parent.save()
      
       return compte
  

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None








  
class PaiementForm(forms.ModelForm):
    cne_eleve = forms.CharField(max_length=100, label="CNE eleve", widget=forms.TextInput(attrs={'class': 'form-control'}))
    modeP = forms.ChoiceField(choices=Paiement.choixPaiement, widget=forms.Select(attrs={'class': 'form-control'}))
    mois_paiement = forms.ChoiceField(choices=Paiement.ChoicesPa, widget=forms.Select(attrs={'class': 'form-control'}))
    type_service = forms.MultipleChoiceField(choices=Paiement.TYPE_CHOICES, widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}))

    class Meta:
        model = Paiement
        fields = ['cne_eleve', 'date_paiement', 'montant', 'mois_paiement', 'modeP', 'type_service']
        widgets = {
            'date_paiement': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'montant': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def clean_cne_eleve(self):
        cne_eleve = self.cleaned_data['cne_eleve']
        try:
            eleve = Eleve.objects.get(cne_eleve=cne_eleve)
        except Eleve.DoesNotExist:
            raise forms.ValidationError("L'élève correspondant au CNE saisi n'existe pas.")
        return eleve

    





class PaiementFormEleve(PaiementForm):
    eleve_nom_prenom = forms.CharField(
        label='Nom et prenom',
        widget=forms.TextInput(attrs={'class': 'form-control','onkeyup': 'fd()'})
    )
   
    class Meta(PaiementForm.Meta):
        fields = ['eleve_nom_prenom'] + list(PaiementForm.Meta.fields)




from django import forms
from .models import Salaire, Agent, Professeur

from django import forms
from .models import *

class SalaryPaymentForm(forms.ModelForm):
    mois_paiement = forms.ChoiceField(choices=Paiement.ChoicesPa, widget=forms.Select(attrs={'class': 'form-control'}))
 
    class Meta:
        model = Salaire
        fields = ['montant', 'mois_paiement', 'date_de_paiement']
        widgets = {
            'date_de_paiement': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'montant': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class SalaryPaymentFormAgent(SalaryPaymentForm):
    cin_agent = forms.ModelChoiceField(
        queryset=Agent.objects.all(),
        label='Agent CIN',
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    agent_nom_prenom = forms.ChoiceField(
        label='Nom et prenom',
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta(SalaryPaymentForm.Meta):
        fields =['cin_agent']+ ['agent_nom_prenom'] + SalaryPaymentForm.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        agent_field = self.fields['agent_nom_prenom']
        queryset = Agent.objects.values_list('compte__nom', 'compte__prenom')
        agent_field.choices = [(f"{nom} {prenom}", f"{nom} {prenom}") for nom, prenom in queryset]

        if 'instance' in kwargs:
            agent_instance = kwargs['instance'].cin_agent
            if agent_instance:
                agent_nom = agent_instance.compte.nom
                agent_prenom = agent_instance.compte.prenom
                agent_field.initial = f"{agent_nom} {agent_prenom}"

        self.fields['agent_nom_prenom'] = agent_field

    def clean(self):
        cleaned_data = super().clean()
        cin_agent = cleaned_data.get('cin_agent')
        agent_nom_prenom = cleaned_data.get('agent_nom_prenom')

        if cin_agent and agent_nom_prenom:
            selected_agent = Agent.objects.get(cin_agent=cin_agent.cin_agent)
            selected_nom_prenom = ' '.join(agent_nom_prenom.split())

            if f"{selected_agent.compte.nom} {selected_agent.compte.prenom}" != selected_nom_prenom:
                raise forms.ValidationError("The selected agent name and CIN do not match.")

        return cleaned_data
    

class SalaryPaymentFormProfesseur(SalaryPaymentForm):
    cin_professeur = forms.ModelChoiceField(
        queryset=Professeur.objects.all(),
        label='Professeur CIN',
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    professeur_nom_prenom = forms.ChoiceField(
        label='Nom et prenom',
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta(SalaryPaymentForm.Meta):
        fields = ['cin_professeur', 'professeur_nom_prenom'] + SalaryPaymentForm.Meta.fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        professeur_field = self.fields['professeur_nom_prenom']
        queryset = Professeur.objects.values_list('compte__nom', 'compte__prenom')
        professeur_field.choices = [(f"{nom} {prenom}", f"{nom} {prenom}") for nom, prenom in queryset]

        if 'instance' in kwargs:
            professeur_instance = kwargs['instance'].cin_professeur
            if professeur_instance:
                professeur_nom = professeur_instance.compte.nom
                professeur_prenom = professeur_instance.compte.prenom
                professeur_field.initial = f"{professeur_nom} {professeur_prenom}"

        self.fields['professeur_nom_prenom'] = professeur_field

        # Reset the professeur_nom_prenom field value if form is submitted
        if self.is_bound and not self.errors:
            self.fields['professeur_nom_prenom'].widget.choices[0] = ('', '--------')

    def clean(self):
        cleaned_data = super().clean()
        cin_professeur = cleaned_data.get('cin_professeur')
        professeur_nom_prenom = cleaned_data.get('professeur_nom_prenom')

        if cin_professeur and professeur_nom_prenom:
            selected_professeur = Professeur.objects.get(cin_professeur=cin_professeur.cin_professeur)
            selected_nom_prenom = ' '.join(professeur_nom_prenom.split())

            if f"{selected_professeur.compte.nom} {selected_professeur.compte.prenom}" != selected_nom_prenom:
                raise forms.ValidationError("The selected professeur name and CIN do not match.")

        return cleaned_data
    



    from django import forms
from .models import Devoir

from django import forms
from .models import Devoir

class DevoirForm(forms.ModelForm):
    date_limite= forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))

    def __init__(self, *args, **kwargs):
        ens_list = kwargs.pop('ens_list', None)
        super(DevoirForm, self).__init__(*args, **kwargs)
        if ens_list is not None:
               self.fields['classe'].queryset = Classe.objects.filter(id_classe__in=ens_list.values('Id_classe_id'))
    class Meta:
        model = Devoir
        fields = '__all__'






# class DevoirForm(forms.ModelForm):
#     class Meta:
#         model = Devoir
#         fields = ['description', 'instruction', 'date_limite', 'contenu', 'classe']

#     def __init__(self, *args, **kwargs):
#         teacher = kwargs.pop('teacher')
#         super(DevoirForm, self).__init__(*args, **kwargs)
#         self.fields['classe'].queryset = Enseigne.objects.filter(Id_professeur=teacher)



class AdmissionForm(forms.ModelForm):
    class Meta:
        model = admission
        fields =  ('nom', 'prenom', 'cne','level','age','ancienne_ecole')



class DemandeRecrutementForm(forms.ModelForm):
    class Meta:
        model = DemandeRecrutement
        fields = ('nom', 'email', 'request','cv')

    def clean_cv(self):
        cv = self.cleaned_data['cv']
        allowed_extensions = ['.jpg', '.jpeg', '.png', '.pdf']
        if not cv.name.lower().endswith(tuple(allowed_extensions)):
            raise ValidationErr('Only JPEG, PNG, and PDF files are allowed.')
        return cv
    
class SessionForm(forms.ModelForm):
    date= forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    def __init__(self, ens, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['classe'].queryset = Classe.objects.filter(id_classe__in=ens.values('Id_classe_id'))
    class Meta:
        model = Session
        fields = ('title', 'platform', 'link','date', 'classe')
        exclude = ['Professeur']
    


class HomeworkSubmissionForm(forms.ModelForm):
    homework_file = forms.FileField(
        label='Upload PDF',
        widget=forms.ClearableFileInput(attrs={'accept': 'application/pdf'}),
    )
    
    class Meta:
        model = DevoirContenue
        fields = ['homework_file']


class EnseigneForm(forms.ModelForm):
    class Meta:
        model = Enseigne
        fields = ['Id_professeur', 'Id_classe', 'Id_matiere']



class MatiereForm(forms.ModelForm):
 
  class Meta:
    model = Matiere
    fields = "__all__"
    widgets={ 
    }

#'================SOUS MATIERE===================='#



class EcoleForm(forms.ModelForm):
 class Meta:
    model = Ecole
    fields = "__all__"
    widgets={
    }


class EpreuveForm(forms.ModelForm):
 classe =  forms.ModelChoiceField(queryset=Classe.objects.all())
 Sousmatiere =  forms.ModelChoiceField(queryset=SousMatiere.objects.all())
 def __init__(self, ens_qs, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['classe'].queryset = Classe.objects.filter(id_classe__in=ens_qs.values('Id_classe_id'))
        self.fields['Sousmatiere'].queryset = SousMatiere.objects.filter(matiere_id__in=ens_qs.values('Id_matiere_id'))


 class Meta:
    model = Epreuve
    fields = "__all__"
    widgets={
              'date_epreuve': forms.DateInput(attrs={'type': 'datetime-local'}),
    }




class CoursForm(forms.ModelForm):
    sousmatiere = forms.ModelChoiceField(queryset=SousMatiere.objects.all())
    def __init__(self, *args, sousmatiere=None, **kwargs):
        super().__init__(*args, **kwargs)
        if sousmatiere is not None:
            self.fields['sousmatiere'].queryset = sousmatiere
    def  clean_pdf_cours(self):
        pdf_cours = self.cleaned_data['pdf_cours']
        allowed_extensions = ['.pdf']
        if not pdf_cours.name.lower().endswith(tuple(allowed_extensions)):
            raise forms.ValidationError('Only PDF files are allowed.File size should not exceed 2.5MB')
        return pdf_cours
    class Meta:
        model = Cours
        fields = "__all__"
        widgets = {

        }




class SousMatiereForm(forms.ModelForm):
  def __init__(self, *args, matiere, **kwargs):
        super().__init__(*args, **kwargs)
        if matiere is not None:
           self.fields['matiere'].queryset = Matiere.objects.filter(id_matiere__in=matiere.values('id_matiere'))
  class Meta:
    model = SousMatiere
    fields = "__all__"
    widgets = {
            'matiere': forms.Select(attrs={'class': 'form-control'})
        }
