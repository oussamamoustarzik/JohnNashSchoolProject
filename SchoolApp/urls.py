from django.urls import path 
from . import views
urlpatterns = [
########### URL FOR HOMEPAGE #################################3
    path('',views.home,name='home'),
    path('home/',views.home,name='home'),
    path('contact/',views.contact, name='contact'),
    path('johnnash/',views.johnnash, name='johnnash'),
    path('cursus/',views.cursus, name='cursus'),
    path('schoolife/',views.schoolife, name='schoolife'),
    path('admission/',views.Admission, name='admission'),
 path('demande_recrutement/', views.demande_recrutement, name='demande_recrutement'),
############ URL FOR Formulaire de LOGIN ##########################

    path('studentspace/',views.studentsp, name='studentsp'),
    path('parentspace/',views.parentsp, name='parentsp'),
    path('teacherspace/',views.teachersp, name='teachersp'),
    path('agentspace/',views.agentsp, name='agentsp'),
    path('adminspace/',views.adminsp, name='adminsp'),
####form
    path('LoginAgent/',views.LoginAgentForm, name='EspaceAgent'),
    path('LoginAdmin/',views.LoginAdminFrom, name='EspaceAdmin'),
    path('LoginParent/',views.LoginParentForm,name='EspaceParent'),
    path('LoginProf/',views.LoginProfForm,name='EspaceProf'),
    path('LoginEleve/',views.LoginStudentForm,name='EspaceEleve'),
    path('logout_user/', views.logout_user, name='logout_user'),

####    After login     ######
    path('Agent_Paiement/',views.AgentPaiement,name='AgentPaiement'),
    path('Agent_Absence/',views.AgentAbsence,name='AgentAbsence'),




######  Agent ######################3
#Absence
    path('Agent_Paiement/',views.AgentPaiement,name='AgentPaiement'),
    path('Agent_Absence/',views.AgentAbsence,name='AgentAbsence'),
    path('AgentScanner/', views.AgentScanner, name='AgentScanner'),
    path('AgentScanHistory/', views.AgentScanHistory, name='AgentScanHistory'),
    path('AgentReclamation/', views.AgentReclamation, name='AgentReclamation'),
    path('AgentAbsDash/', views.AgentAbsDash, name='AgentAbsDash'),
    path('scan1/', views.scan1, name='scan1'),
    path('AgentSalaire/', views.AgentSalaire, name='AgentSalaire'),
    path('send_emailagent/', views.send_emailagent, name='send_emailagent'),
    path('AgentHistorique/', views.AgentHistorique, name='AgentHistorique'),
    path('AgentDash/', views.AgentDash, name='AgentDash'),
    path('send_emailagent/', views.send_emailagent, name='send_emailagent'),




##########  Parent #######################33
    path('parent_students/',views.ParentHistoryList,name='parent_students'),
    path('send_emailaparent/', views.send_emailaparent, name='send_emailaparent'),
    path('ParentDash/', views.ParentDash, name='ParentDash'),
    path('ParentPaiement/', views.ParentPaiement, name='ParentPaiement'),

    path('Parent_Absence/',views.ParentAbsence,name='ParentAbsence'),
    path('Parent_Elearning/',views.ParentElearning,name='ParentElearning'),
    path('ParentReclamation/', views.ParentReclamation, name='ParentReclamation'),
    path('ParentQr/', views.ParentQr, name='ParentQr'),
    path('inscription/', views.inscription, name='inscription'),
    path('ParentAbsDash/', views.ParentAbsDash, name='ParentAbsDash'),
    path('ParentAbsList/', views.ParentAbsList, name='ParentAbsList'),
     path('grades/', views.grades, name='grades'),



############    prof    ######################

    path('Prof_Absence/',views.ProfAbsence,name='ProfAbsence'),
    path('Prof_Paiement/',views.ProfPaiement,name='ProfPaiement'),
    path('Prof_Elearning/',views.ProfElearning,name='ProfElearning'),
    path('ProfClassesList/', views.ProfClassesList, name='ProfClassesList'),
    path('ProfReclamation/', views.ProfReclamation, name='ProfReclamation'),
    path('ProfAttendanceList/<int:classe_id>', views.ProfAttendanceList, name='ProfAttendanceList'),
    path('ProfAbsDash/', views.ProfAbsDash, name='ProfAbsDash'),
    path('ProfAttClasses/', views.ProfAttClasses, name='ProfAttClasses'),
    path('Prof_Paiement/',views.ProfPaiement,name='ProfPaiement'),
    path('ProfSalaire/', views.ProfSalaire, name='ProfSalaire'),
    path('send_emailprof/', views.send_emailprof, name='send_emailprof'), 
    path('ProfHistorique/', views.ProfHistorique, name='ProfHistorique'),
    path('ProfDash/', views.ProfDash, name='ProfDash'),

    path('Devoir/', views.Homework, name='Devoir'),

    path('addDevoir/', views.AddHomeWork, name='AddDevoir'),
   path('update_homework/<int:devoir_id>/', views.UpdateHomework, name='update_homework'),
    path('remove_homework/<int:devoir_id>/', views.RemoveHomeWork, name='remove_homework'),

    path('Session/', views.session, name='session'),
    path('CreateSession/', views.createSession, name='Createsession'),
   path('update_Session/<int:session_id>/', views.editSession, name='updateSession'),
    path('remove_Session/<int:session_id>/', views.deleteSession, name='removeSession'),


    path('addssmatiere/',views.addssmatiere, name='addssmatiere'),
    path('updatessmatiere/<int:id_sousmatiere>',views.update_ssmatiere, name='updatessmatiere'),
    path('delete-ssmatiere/<int:id_sousmatiere>/', views.delete_ssmatiere, name='delete_ssmatiere'),



path('addcours/',views.addcours, name='addcours'),
              path('updatecours/<int:id_cours>',views.update_cours, name='updatecours'),
               path('deletecours/<int:id_cours>',views.delete_cours, name='deletecours'),
    path('epreuves/',views.ViewEpreuves.as_view(), name='epreuves'),
    path('addepreuve/',views.addepreuve, name='addepreuve'),
    path('updateepreuve/<int:id_epreuve>',views.update_epreuve, name='updateepreuve'),
    path('deleteepreuve/<int:id_epreuve>',views.delete_epreuve, name='deleteepreuve'),
    path('coursprofs/',views.Coursprof, name='coursprofs'),
#==============notes=================#
path('addnote/',views.addnote, name='addnote'),

#===========classe Prof============#
path('classeP/', views.classeProf.as_view(), name="classeProf"),
path('eleveP/', views.ViewElevesP.as_view(), name="eleveProf"),
path('notesP/',views.ViewNotesP.as_view(), name='notesProf'),
 







################    Admin   ###############################33
    path('Dashboard/', views.admin_dashboard, name='dash'),
    path('notif/', views.notif, name='notif'),
    path('level/', views.level, name='level'),   
    path('tablep/', views.tablep, name='tablep'), 
    path('send_emails/', views.send_emails, name='send_emails'),
    path('send_email/', views.send_email, name='send_email'), 
    path('niveau<str:niveau>/', views.niveau, name='niveau'),
    path('AdminDash/', views.AdminDash, name='AdminDash'),
    path('Admin_Absence/',views.AdminAbsence,name='AdminAbsence'),
    path('Admin_Elearning/',views.AdminElearning,name='AdminElearning'),
    path('Admin_Paiement/',views.AdminPaiement,name='AdminPaiement'),
    path('AdminQr/', views.AdminQr, name='AdminQr'),
    path('GenerateurAdmin/', views.GenerateurAdmin, name='GenerateurAdmin'),
    path('AdminReclamation/', views.AdminReclamation, name='AdminReclamation'),
    path('AdminAbsList/', views.AdminAbsList, name='AdminAbsList'),
    path('AdminNotifAbs/<str:eleve_id>/', views.AdminNotifAbs, name='AdminNotifAbs'),
    path('AdminAbsDash/', views.AdminAbsDash, name='AdminAbsDash'),
    path('paiement/',views.paiement,name='paiement'),
    path('Users/',views.UserCards,name='Users'),
    path('ajoutadmin/',views.AjoutAdmin.as_view(), name='ajoutadmin'),
    path('admins/', views.ViewAdmins.as_view(), name='admins'),
    path('editadmin/<int:id_user>/',views.EditAdmin.as_view(), name='editadmin'),
    path('deleteadmin/<int:id_user>/', views.DeleteAdmin.as_view(), name='deleteadmin'),

    path('parents/', views.ViewParents.as_view(), name='parents'),
    path('ajoutparent/',views.AjoutParent.as_view(), name='ajoutparent'),
    path('editparent/<int:id_user>/',views.EditParent.as_view(), name='editparent'),
    path('deleteparent/<int:id_user>/', views.DeleteParent.as_view(), name='deleteparent'),


 path('agents/', views.ViewAgents.as_view(), name='agents'),
    path('ajoutagent/',views.AjoutAgent.as_view(), name='ajoutagent'),
    path('editagent/<int:id_user>/',views.EditAgent.as_view(), name='editagent'),
    path('deleteagent/<int:id_user>/', views.DeleteAgent.as_view(), name='deleteagent'),

    path('eleves/', views.ViewEleves.as_view(), name='eleves'),
    path('ajouteleve/',views.AjoutEleve.as_view(), name='ajouteleve'),
    path('editeleve/<int:id_user>/',views.EditEleve.as_view(), name='editeleve'),
    path('deleteeleve/<int:id_user>/', views.DeleteEleve.as_view(), name='deleteeleve'),


    path('profs/', views.ViewProfs.as_view(), name='profs'),
    path('ajoutprof/',views.AjoutProf.as_view(), name='ajoutprof'),
    path('editprof/<int:id_user>/',views.EditProf.as_view(), name='editprof'),
    path('deleteprof/<int:id_user>/', views.DeleteProf.as_view(), name='deleteprof'),

    path('notes/',views.ViewNotes.as_view(), name='notes'),
    path('nini/',views.leila, name='nini'),  


             path('addenseigne/',views.addenseigne, name='addenseigne'),
                path('enseignes/',views.ViewEnseigne.as_view(), name='enseignes'),
               path('deleteenseigne/<int:id>',views.delete_enseigne, name='deleteenseigne'),
                path('updateenseigne/<int:id>',views.update_enseigne, name='updateenseigne'),

path('addclasse/',views.addclasse, name='addclasse'),
path('classes/',views.ViewClasses.as_view(), name='classes'),    
path('updateclasse/<int:id_classe>',views.update_classe, name='updateclasse'),
path('deleteclasse/<int:id_classe>',views.delete_classe, name='deleteclasse'),


            path('addmatiere/',views.addmatiere, name='addmatiere'),
             # path('readmatiere/',views.read_matiere, name='readmatiere'),
              path('updatematiere/<int:id_matiere>',views.update_matiere, name='updatematiere'),
               path('deletematiere/<int:id_matiere>',views.delete_matiere, name='deletematiere'),
 path('matieres/',views.ViewMatieres.as_view(), name='matieres'), 
path('matierestotal/', views.ViewMatierestotal.as_view(), name='matierestotal'),
path('profsmatieres/',views.liste_enseignants, name='profsmatieres'),             
path('AdminReclamation1/', views.AdminReclamationelearning, name='AdminReclamation1'),  

        path('ecoles/',views.ViewEcoles.as_view(), name='ecoles'),
         path('addecole/',views.addecole, name='addecole'),
              path('updateecole/<int:id_ecole>',views.update_ecole, name='updateecole'),
               path('deleteecole/<int:id_ecole>',views.delete_ecole, name='deleteecole'),
               path('sousmatieres-professeur/', views.sous_matieres_professeur, name='sousmatieres_professeur'),
####################    Eleve   #########################################################
    path('Elearning/',views.EleveElearning,name='EleveElearning'),
    path('ElearningSession/',views.EleveElearningSession,name='EleveElearningSession'),
    path('ElearningHomeWork/',views.EleveElearningHomework,name='EleveElearningHomework'),
    path('HomeWork/<int:devoir_id>',views.submit_homework,name='sbm'),
  path('student_list/<int:devoir_id>/', views.student_list, name='student_list'),
path('timetable/',views.display_timetable, name='timetable'),
path('coursstudent/',views.Coursstudent, name='coursstudent'),
path('courses/',views.Courses, name='courses'),
path('ProfReclamation1/', views.ProfReclamationelearning, name='ProfReclamation1'),
]