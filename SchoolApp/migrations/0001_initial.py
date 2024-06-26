# Generated by Django 4.2.1 on 2023-05-31 11:40

import SchoolApp.models
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AbsenceNotif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_email', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('sent_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('cin_admin', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('cin_agent', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Classe',
            fields=[
                ('id_classe', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('niveau_classe', models.CharField(choices=[('PS', 'PS'), ('MS', 'MS'), ('GS', 'GS'), ('CP', 'CP'), ('CE1', 'CE1'), ('CE2', 'CE2'), ('CM1', 'CM1'), ('CM2', 'CM2'), ('CE6', 'CE6')], max_length=40)),
                ('nom_classe', models.CharField(max_length=50)),
                ('nbr_eleve_classe', models.IntegerField()),
                ('emploie_temps', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Compte',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('id_user', models.AutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('adresse', models.CharField(max_length=50)),
                ('tel', models.CharField(max_length=50)),
                ('lieu_naissance', models.CharField(max_length=50)),
                ('date_naissance', models.DateField()),
                ('sexe', models.IntegerField(choices=[(1, 'Male'), (2, 'Female')])),
                ('nationnalite', models.CharField(max_length=50)),
                ('type_compte', models.IntegerField(choices=[(1, 'Admin'), (2, 'Prof'), (3, 'Parent'), (4, 'Agent'), (5, 'Eleve')])),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='comptes', related_query_name='compte', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='comptes', related_query_name='compte', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id_mssg', models.AutoField(primary_key=True, serialize=False)),
                ('type_mssg', models.CharField(max_length=50)),
                ('email_mssg', models.CharField(max_length=50)),
                ('tel_mssg', models.CharField(max_length=50)),
                ('mssg', models.CharField(max_length=50)),
                ('date_mssg', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Cours',
            fields=[
                ('id_cours', models.IntegerField(primary_key=True, serialize=False)),
                ('libelle', models.CharField(max_length=50)),
                ('lien_cours', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Devoir',
            fields=[
                ('id_devoir', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=50)),
                ('instruction', models.CharField(max_length=50)),
                ('date_limite', models.DateTimeField()),
                ('contenu', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ecole',
            fields=[
                ('id_ecole', models.IntegerField(primary_key=True, serialize=False)),
                ('nom_ecole', models.CharField(max_length=50)),
                ('adresse_ecole', models.CharField(max_length=50)),
                ('facebook_account', models.CharField(max_length=50)),
                ('instagram_account', models.CharField(max_length=50, null=True)),
                ('email_ecole', models.EmailField(max_length=50, null=True)),
                ('numero_telephone', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Eleve',
            fields=[
                ('cne_eleve', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('qr_code', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Epreuve',
            fields=[
                ('id_epreuve', models.AutoField(primary_key=True, serialize=False)),
                ('date_epreuve', models.DateTimeField()),
                ('nom_epreuve', models.CharField(max_length=50)),
                ('nature_epreuve', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Matiere',
            fields=[
                ('id_matiere', models.AutoField(primary_key=True, serialize=False)),
                ('nom_matiere', models.CharField(max_length=50)),
                ('coefficient', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id_notification', models.AutoField(primary_key=True, serialize=False)),
                ('message_notification', models.CharField(max_length=255)),
                ('type_notification', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('cin_parent', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('compte', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.compte')),
            ],
        ),
        migrations.CreateModel(
            name='Professeur',
            fields=[
                ('cin_professeur', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('compte', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.compte')),
            ],
        ),
        migrations.CreateModel(
            name='Reclamation',
            fields=[
                ('id_reclamation', models.AutoField(primary_key=True, serialize=False)),
                ('message_reclamation', models.CharField(max_length=500)),
                ('id_admin', models.CharField(blank=True, max_length=50, null=True)),
                ('name', models.CharField(max_length=50, null=True)),
                ('email', models.CharField(max_length=50, null=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('admin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.admin')),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('code_semestre', models.AutoField(primary_key=True, serialize=False)),
                ('description_semestre', models.CharField(max_length=50)),
                ('annee_scolaire', models.DateTimeField()),
                ('date_debut', models.DateTimeField()),
                ('date_fin', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='SousMatiere',
            fields=[
                ('id_sousmatiere', models.IntegerField(primary_key=True, serialize=False)),
                ('nom_sousmatiere', models.CharField(max_length=50)),
                ('coefficient', models.IntegerField()),
                ('matiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.matiere')),
            ],
        ),
        migrations.CreateModel(
            name='Scanne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_heure', models.DateTimeField()),
                ('CNE_eleve', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.eleve')),
                ('Id_agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.agent')),
            ],
        ),
        migrations.CreateModel(
            name='Salaire',
            fields=[
                ('reference', models.IntegerField(primary_key=True, serialize=False)),
                ('date_de_paiement', models.DateTimeField()),
                ('type_emploi', models.CharField(max_length=50)),
                ('montant', models.DecimalField(decimal_places=6, max_digits=15)),
                ('mois_paiement', models.DateField()),
                ('id_compte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.compte')),
            ],
        ),
        migrations.CreateModel(
            name='RecoitP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_compte', models.IntegerField(choices=[(3, 'Parent'), (4, 'Agent')])),
                ('Id_agent', models.ForeignKey(max_length=50, on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.agent')),
                ('Id_professeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.professeur')),
                ('Refer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.salaire')),
            ],
        ),
        migrations.CreateModel(
            name='Reclamer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CIN_parent', models.CharField(max_length=50)),
                ('Id_professeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.professeur')),
                ('id_reclamation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.reclamation')),
            ],
        ),
        migrations.CreateModel(
            name='RecevoirSms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CIN_parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.parent')),
                ('Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.notifications')),
                ('Id_agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.agent')),
                ('Id_professeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.professeur')),
            ],
        ),
        migrations.CreateModel(
            name='Percevoir',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_mssg', models.CharField(max_length=50)),
                ('cin_admin', models.CharField(max_length=50)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.admin')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.contact')),
            ],
        ),
        migrations.CreateModel(
            name='Passe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Note', models.DecimalField(decimal_places=2, max_digits=15)),
                ('CNE_eleve', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.eleve')),
                ('id_epreuve', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.epreuve')),
            ],
        ),
        migrations.CreateModel(
            name='Paiement',
            fields=[
                ('reference', models.IntegerField(primary_key=True, serialize=False)),
                ('date_paiement', models.DateTimeField(default=SchoolApp.models.Paiement.get_today_date)),
                ('montant', models.IntegerField()),
                ('modeP', models.CharField(choices=[('Species', 'Species'), ('Check', 'Check')], max_length=30)),
                ('mois_paiement', models.CharField(choices=[('January', 'January'), ('February', 'February'), ('March', 'March'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December')], max_length=30, null=True)),
                ('type_service', models.CharField(choices=[('Schooling', 'Schooling'), ('Canteen', 'Canteen'), ('Transporation', 'Transporation')], max_length=50)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.admin')),
                ('cne_eleve', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.eleve')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.parent')),
            ],
        ),
        migrations.CreateModel(
            name='ListePresence',
            fields=[
                ('id_liste', models.AutoField(primary_key=True, serialize=False)),
                ('etat', models.BooleanField(default=False)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('classe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.classe')),
                ('cne_eleve', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.eleve')),
            ],
        ),
        migrations.CreateModel(
            name='Espece',
            fields=[
                ('reference', models.IntegerField(primary_key=True, serialize=False)),
                ('paiement', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.paiement')),
            ],
        ),
        migrations.CreateModel(
            name='Enseigne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Id_classe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.classe')),
                ('Id_matiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.matiere')),
                ('Id_professeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.professeur')),
            ],
        ),
        migrations.AddField(
            model_name='eleve',
            name='cin_parent',
            field=models.ForeignKey(max_length=50, on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.parent'),
        ),
        migrations.AddField(
            model_name='eleve',
            name='compte',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.compte'),
        ),
        migrations.AddField(
            model_name='eleve',
            name='id_classe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.classe'),
        ),
        migrations.CreateModel(
            name='Concerne',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_semestre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.semester')),
                ('id_cours', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.cours')),
            ],
        ),
        migrations.CreateModel(
            name='ComporteCours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Id_SM', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.sousmatiere')),
                ('Id_cours', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.cours')),
            ],
        ),
        migrations.AddField(
            model_name='classe',
            name='ecole',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.ecole'),
        ),
        migrations.CreateModel(
            name='Cheque',
            fields=[
                ('numero_cheque', models.IntegerField(primary_key=True, serialize=False)),
                ('nom_banque', models.CharField(max_length=50)),
                ('reference', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.paiement', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='AvoirClasse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Id_classe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.classe')),
                ('Id_liste', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.listepresence')),
            ],
        ),
        migrations.CreateModel(
            name='avoir',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Id_devoir', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.devoir')),
                ('Id_matiere', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.matiere')),
            ],
        ),
        migrations.AddField(
            model_name='agent',
            name='compte',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.compte'),
        ),
        migrations.AddField(
            model_name='admin',
            name='compte',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.compte'),
        ),
    ]
