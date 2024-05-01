from django.db import models
from datetime import date,datetime
from django.utils import timezone
# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser,Group,Permission
from django.contrib.auth.hashers import make_password
from django.core.validators import FileExtensionValidator

class Compte(AbstractUser):
    id_user = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    adresse = models.CharField(max_length=50)
    tel = models.CharField(max_length=50)
    lieu_naissance = models.CharField(max_length=50)
    date_naissance = models.DateField()
    Gender=((1,"Male"),(2,"Female"))
    sexe = models.IntegerField(choices=Gender)
    nationnalite = models.CharField(max_length=50)
    TYPE_COMPTE_CHOICES = (
        (1, "Admin"),
        (2, "Prof"),
        (3, "Parent"),
        (4, "Agent"),
        (5, "Eleve"),
    )
    type_compte = models.IntegerField(choices=TYPE_COMPTE_CHOICES)
    groups = models.ManyToManyField(
        Group,
        verbose_name=("groups"),
        blank=True,
        related_name="comptes",
        help_text=(
            "The groups this user belongs to. A user will get all permissions "
            "granted to each of their groups."
        ),
        related_query_name="compte",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=("user permissions"),
        blank=True,
        related_name="comptes",
        help_text=("Specific permissions for this user."),
        related_query_name="compte",
    )
 
    def __str__(self):
        return f"{self.nom} {self.prenom}"
    
class Admin(models.Model):
    cin_admin = models.CharField(max_length=50, primary_key=True)
    compte = models.OneToOneField(Compte, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.compte}"
    
class Parent(models.Model):
    cin_parent = models.CharField(max_length=50, primary_key=True)
    compte = models.OneToOneField(Compte, on_delete=models.CASCADE)
    def get_eleves(self):
        return Eleve.objects.filter(cin_parent=self)
    def __str__(self):
        return f"{self.compte}"
    

class Professeur(models.Model):
    cin_professeur = models.CharField(max_length=50,primary_key=True)
    compte = models.OneToOneField(Compte, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.compte} {self.cin_professeur}"
#--------------------------------------------------------------------------------------------------------------------
class Ecole(models.Model):
    id_ecole = models.IntegerField(primary_key=True)
    nom_ecole = models.CharField(max_length=50)
    adresse_ecole = models.CharField(max_length=50)
    facebook_account = models.CharField(max_length=50)
    instagram_account = models.CharField(max_length=50, null=True)
    email_ecole = models.EmailField(max_length=50, null=True)
    numero_telephone = models.CharField(max_length=50, null=True)
    def __str__(self):
        return f"{self.nom_ecole}"
class Classe(models.Model):
    id_classe = models.CharField(max_length=40,primary_key=True)
    CLASS_CHOICES = (
        ('PS', 'PS'),
        ('MS', 'MS'),
        ('GS', 'GS'),
        ('CP', 'CP'),
        ('CE1', 'CE1'),
        ('CE2', 'CE2'),
        ('CM1', 'CM1'),
        ('CM2', 'CM2'),
        ('CE6', 'CE6'),

    )
    niveau_classe = models.CharField(choices=CLASS_CHOICES,max_length=40)
    nom_classe = models.CharField(max_length=50)
    max_students = models.PositiveIntegerField(default=30)
    emploie_temps =  models.FileField(upload_to='emplois_temps/', null=True, validators=[FileExtensionValidator(['xls', 'xml', 'pdf'])])    
    ecole = models.ForeignKey(Ecole, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.nom_classe}"
class Matiere(models.Model):
    id_matiere = models.AutoField(primary_key=True)
    nom_matiere = models.CharField(max_length=50,unique=True)
    coefficient = models.IntegerField()
    def __str__(self):
        return f"{self.nom_matiere}"

class SousMatiere(models.Model):
    id_sousmatiere = models.IntegerField(primary_key=True)
    nom_sousmatiere = models.CharField(max_length=50)
    coefficient = models.IntegerField()
    matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.nom_sousmatiere}"

class Cours(models.Model):
        id_cours = models.IntegerField(primary_key=True)
        libelle = models.CharField(max_length=50)
        lien_cours = models.CharField(max_length=400)
        pdf_cours = models.FileField(upload_to='courspdf/', null=True, validators=[FileExtensionValidator(['pdf'])])
        def __str__(self):
          return f"{self.libelle}"
        
class Semester(models.Model):
    code_semestre = models.AutoField(primary_key=True)
    description_semestre = models.CharField(max_length=50)
    annee_scolaire = models.DateField()
    date_debut = models.DateField()
    date_fin = models.DateField()
    def __str__(self):
           return self.description_semestre

class Epreuve(models.Model):
    EPREUVE_CHOICES = (
        (1, "epreuve 1"),
        (2, "epreuve 2"),
        (3, "epreuve 3"),
        (4, "epreuve 4"),
        (5, "epreuve 5"),
        (6, "epreuve 6"),
    )
    id_epreuve = models.AutoField(primary_key=True)
    date_epreuve = models.DateTimeField()
    nom_epreuve = models.IntegerField(choices=EPREUVE_CHOICES)
    nature_epreuve = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.nom_epreuve}"
class Notifications(models.Model):
    id_notification = models.AutoField(primary_key=True)
    message_notification = models.CharField(max_length=255, null=False)
    type_notification = models.CharField(max_length=50, null=False)


class Reclamation(models.Model):
   id_reclamation = models.AutoField(primary_key=True)
   message_reclamation = models.CharField(max_length=500, null=False)
   id_admin = models.CharField(max_length=50, null=True, blank=True)
   admin = models.ForeignKey('Admin', on_delete=models.CASCADE,null=True, blank=True)
   name = models.CharField(max_length=50, null=True)
   email = models.CharField(max_length=50, null=True)
   date = models.DateTimeField(default=timezone.now)

class Salaire(models.Model):
    ChoicesPa = [
        ('January', 'January'),
        ('February', 'February'),
        ('March', 'March'),
        ('April', 'April'),
        ('May', 'May'),
        ('June', 'June'),

        ('September', 'September'),
        ('October', 'October'),
        ('November', 'November'),
        ('December', 'December'),
    ]
    reference = models.BigAutoField(primary_key=True)
    date_de_paiement = models.DateTimeField(null=False)
    
    montant = models.DecimalField(max_digits=15, decimal_places=2)
    mois_paiement = models.CharField(max_length=30 ,choices=ChoicesPa, null=True)
    id_compte = models.ForeignKey('Compte', on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.id_compte.nom} {self.id_compte.prenom} "



class Devoir(models.Model):
    id_devoir = models.AutoField(primary_key=True)
    description = models.CharField(max_length=50)
    instruction = models.CharField(max_length=50)
    date_limite = models.DateTimeField()
    contenu = models.CharField(max_length=50, null=True)
    classe = models.ForeignKey('Classe', on_delete=models.CASCADE,null=True)

    def __str__(self):
        return str(self.id_devoir)

class Agent(models.Model):
    cin_agent= models.CharField(max_length=50, primary_key=True)
    compte = models.OneToOneField('Compte', unique=True, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.compte } {self.cin_agent}"

class Eleve(models.Model):
    cne_eleve = models.CharField(primary_key=True,max_length=100)
    qr_code = models.CharField(max_length=255)
    compte = models.OneToOneField('Compte', unique=True, on_delete=models.CASCADE)
    cin_parent = models.ForeignKey('Parent',max_length=50, null=False,on_delete=models.CASCADE)
    id_classe = models.ForeignKey('Classe', on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.compte}"

class Paiement(models.Model):
 
    choixPaiement = [
        ('Species','Species'),
        ('Check','Check'),
    ]
    ChoicesPa = [
        ('January', 'January'),
        ('February', 'February'),
        ('March', 'March'),
        ('April', 'April'),
        ('May', 'May'),
        ('June', 'June'),

        ('September', 'September'),
        ('October', 'October'),
        ('November', 'November'),
        ('December', 'December'),
    ]
    
    TYPE_CHOICES = [
    ('Schooling', 'Schooling'),
    ('Canteen', 'Canteen'),
    ('Transportation', 'Transportation'),
]
    def get_today_date():
            return datetime.now()
    reference = models.BigIntegerField(primary_key=True)
    date_paiement = models.DateField(default=get_today_date)
    montant = models.BigIntegerField(null=False)
    modeP = models.CharField(choices=choixPaiement,max_length=30)
    mois_paiement = models.CharField(max_length=30 ,choices=ChoicesPa, null=True)
    type_service = models.CharField(max_length=50, null=False)
    cne_eleve = models.ForeignKey('Eleve', on_delete=models.CASCADE)
    
    
    def __str__(self):
        return f"{self.mois_paiement} "



class Espece(models.Model):
    reference = models.IntegerField(primary_key=True)
    paiement = models.ForeignKey('Paiement', on_delete=models.CASCADE)

class Cheque(models.Model):
    numero_cheque = models.IntegerField(primary_key=True)
    nom_banque = models.CharField(max_length=50, null=False)
    reference = models.ForeignKey('Paiement', unique=True, on_delete=models.CASCADE)

class ListePresence(models.Model):
    id_liste = models.AutoField(primary_key=True)
    etat = models.BooleanField(default=False)
    cne_eleve = models.ForeignKey(Eleve ,on_delete=models.CASCADE, null=True,blank=True)
    date = models.DateTimeField(default=timezone.now)
    classe = models.ForeignKey('Classe', on_delete=models.CASCADE)

class Scanne(models.Model):
    Id_agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    CNE_eleve = models.ForeignKey(Eleve, on_delete=models.CASCADE)
    date_heure = models.DateTimeField()

class AvoirClasse(models.Model):
    Id_liste = models.ForeignKey(ListePresence,on_delete=models.CASCADE)
    Id_classe = models.ForeignKey(Classe,on_delete=models.CASCADE)

class Enseigne(models.Model):
    Id_professeur = models.ForeignKey(Professeur, on_delete=models.CASCADE)
    Id_classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
    Id_matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE)
    def str(self):
        return f"{self.compte.nom} {self.compte.prenom}"

class RecevoirSms(models.Model):
    Id_agent = models.ForeignKey(Agent,on_delete=models.CASCADE)
    CIN_parent = models.ForeignKey(Parent,on_delete=models.CASCADE)
    Id_professeur = models.ForeignKey(Professeur,on_delete=models.CASCADE)
    Id = models.ForeignKey(Notifications,on_delete=models.CASCADE)
 

class ComporteCours(models.Model):
    Id_SM = models.ForeignKey(SousMatiere, on_delete=models.CASCADE)
    Id_cours = models.ForeignKey(Cours, on_delete=models.CASCADE)
  

class Concerne(models.Model):
    id_cours = models.ForeignKey(Cours, on_delete=models.CASCADE)
    code_semestre = models.ForeignKey(Semester, on_delete=models.CASCADE)



class Reclamer(models.Model):
    CIN_parent = models.CharField(max_length=50)
    Id_professeur = models.ForeignKey('Professeur', on_delete=models.CASCADE)
    id_reclamation = models.ForeignKey('Reclamation', on_delete=models.CASCADE)
   
                

class RecoitP(models.Model):
    Id_professeur = models.ForeignKey('Professeur',on_delete=models.CASCADE)
    Refer = models.ForeignKey('Salaire',on_delete=models.CASCADE)
    Id_agent = models.ForeignKey('Agent',max_length=50,on_delete=models.CASCADE)
    TYPE_COMPTE_CHOICES = (
        (3, "Parent"),
        (4, "Agent"),
    )
    type_compte = models.IntegerField(choices=TYPE_COMPTE_CHOICES)                
        

class avoir(models.Model):
    Id_matiere = models.ForeignKey('Matiere',on_delete=models.CASCADE)
    Id_devoir = models.ForeignKey('Devoir',on_delete=models.CASCADE)
    
   

class Passe(models.Model):
    CNE_eleve = models.ForeignKey('Eleve', on_delete=models.CASCADE)
    id_epreuve = models.ForeignKey('Epreuve', on_delete=models.CASCADE)
    Note = models.DecimalField(max_digits=15, decimal_places=2)
    def __str__(self):
        return f"{self.id_epreuve} {self.Note}"

class Contact(models.Model):
    id_mssg = models.AutoField(primary_key=True)
    type_mssg = models.CharField(max_length=50)
    email_mssg = models.CharField(max_length=50)
    tel_mssg = models.CharField(max_length=50)
    mssg = models.CharField(max_length=50)
    date_mssg  = models.DateTimeField(default=timezone.now)


class Percevoir(models.Model):
    id_mssg = models.CharField(max_length=50)
    cin_admin = models.CharField(max_length=50)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)

class AbsenceNotif(models.Model):
    parent_email = models.CharField(max_length=50)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    sent_date = models.DateTimeField(auto_now_add=True)

class admission(models.Model):
    id=models.AutoField(primary_key=True)
    CLASSES = (
        ('PS', 'PS'),
        ('MS', 'MS'),
        ('GS', 'GS'),
        ('CP', 'CP'),
        ('CE1', 'CE1'),
        ('CE2', 'CE2'),
        ('CM1', 'CM1'),
        ('CM2', 'CM2'),
        ('CE6', 'CE6'),

    )
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    cne = models.CharField(max_length=100)
    level = models.CharField(choices=CLASSES,max_length=100)
    age = models.CharField(max_length=100)
    ancienne_ecole = models.CharField(max_length=100, null=True)


class DemandeRecrutement(models.Model):
    idDemande=models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    request = models.TextField()
    cv = models.FileField(upload_to='cvs/')


class Session(models.Model):
    id = models.AutoField(primary_key=True)
    Professeur= models.ForeignKey(Professeur,on_delete=models.CASCADE)
    classe= models.ForeignKey(Classe,on_delete=models.CASCADE)
    title = models.CharField(max_length=100,null=True)
    date = models.DateTimeField(null=True)
    PLATFORM_CHOICES = (
        ('zoom', 'Zoom'),
        ('google_meet', 'Google Meet'),
    )
    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES,null=True)
    link=models.CharField(max_length=300,null=True)



class Se_Comporte(models.Model):
    sousmatiere = models.ForeignKey(SousMatiere, on_delete=models.CASCADE)
    epreuve = models.ForeignKey(Epreuve, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.sousmatiere} {self.epreuve}"
    
class DevoirContenue(models.Model):
    CNE_eleve = models.ForeignKey('Eleve', on_delete=models.CASCADE)
    Id_devoir = models.ForeignKey('Devoir', on_delete=models.CASCADE)
    homework_file = models.FileField(upload_to='homeworks/' ,null=True, blank=True)

class Eprv(models.Model):
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
    epreuve = models.ForeignKey(Epreuve, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.classe}"
    


class UserAnalytics(models.Model):
    compte = models.OneToOneField(Compte, on_delete=models.CASCADE)
    hours_connected = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Analytics for {self.compte.nom} {self.compte.prenom}"
    
class BackUpScanne(models.Model):
    Id_agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    CNE_eleve = models.ForeignKey(Eleve, on_delete=models.CASCADE)
    date_heure = models.DateTimeField()