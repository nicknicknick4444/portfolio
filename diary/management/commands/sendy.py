from django.core.management.base import BaseCommand
from diary.email_send import main

class Command(BaseCommand):
    def handle(self, *args, **options):
        print("BUFFOOOOON!!!")
        main()
        
