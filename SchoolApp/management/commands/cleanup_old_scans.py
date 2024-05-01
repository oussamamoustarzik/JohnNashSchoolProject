from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from datetime import timedelta
from django.conf import settings  # Ajoutez cette importation
from SchoolApp.models import Scanne,BackUpScanne

class Command(BaseCommand):
    help = 'Nettoyer les scans pour la journée après une heure donnée'

    def handle(self, *args, **kwargs):
        auto_cleanup_hour = getattr(settings, 'AUTO_CLEANUP_HOUR', None)
        if auto_cleanup_hour is None or auto_cleanup_hour < 0 or auto_cleanup_hour > 23:
            raise CommandError('Heure de nettoyage automatique invalide dans les paramètres.')

        maintenant = timezone.now()
        date_heure_suppression = maintenant.replace(hour=auto_cleanup_hour, minute=0, second=0, microsecond=0)

        # Backup records before deletion
        records_to_backup = Scanne.objects.filter(date_heure__gte=date_heure_suppression)
        for record in records_to_backup:
            BackUpScanne.objects.create(student_name=record.student_name, date=record.date_heure)

        # Delete records after the specified time
        nombre_suppressions, _ = Scanne.objects.filter(date_heure__gte=date_heure_suppression).delete()
        self.stdout.write(self.style.SUCCESS(f'Supprimé {nombre_suppressions} scans à partir de {date_heure_suppression}.'))




# class Command(BaseCommand):
#     help = 'Delete scans for the current day up to a fixed hour and create backups'

#     def handle(self, *args, **kwargs):
#         cleanup_hour = 21

        
#         now = timezone.now()

#         today_start = now.replace(hour=0, minute=0, second=0, microsecond=0)

#         cleanup_time = today_start.replace(hour=cleanup_hour, minute=0, second=0, microsecond=0)
#         records_to_backup = Scanne.objects.filter(date_heure__lt=cleanup_time)
#         for record in records_to_backup:
#             # Create a backup record
#             BackUpScanne.objects.create(CNE_eleve=record.CNE_eleve, date_heure=record.date_heure,Id_agent=record.Id_agent)

#         # Delete scans for the current day up to the specified cleanup hour
#         deleted_count, _ = Scanne.objects.filter(date_heure__lt=cleanup_time).delete()
#         self.stdout.write(self.style.SUCCESS(f'Deleted {deleted_count} scans for the current day up to {cleanup_hour}:00 and created backups.'))