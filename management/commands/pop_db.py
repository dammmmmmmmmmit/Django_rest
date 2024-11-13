from django.core.management.base import BaseCommand
from faker import Faker
from user.models import User, Contact, Spam  

class Command(BaseCommand):
    help = 'data population'

    def handle(self, *args, **kwargs):
        fake = Faker()

       
        user_count = 0
        for _ in range(10):  
            User.objects.create(
                username=fake.user_name(),
                phone=fake.phone_number(),
                email=fake.email()
            )
            user_count += 1

        
        contact_count = 0
        users = User.objects.all()
        for _ in range(10): 
            user = fake.random_element(users)
            Contact.objects.create(
                owner=user,
                name=fake.name(),
                phone=fake.phone_number()
            )
            contact_count += 1

   
        spam_count = 0
        for _ in range(10): 
            user = fake.random_element(users)
            Spam.objects.create(
                reporter=user,
                phone=fake.phone_number()
            )
            spam_count += 1

        
        self.stdout.write(self.style.SUCCESS(f'populated the database with {user_count} users, {contact_count} contacts, and {spam_count} spams'))