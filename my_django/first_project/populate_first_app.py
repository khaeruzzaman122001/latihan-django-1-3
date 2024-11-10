import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

import random
from first_app.models import Topic, Webpage, AccessRecord
from faker import Faker

fakegen = Faker()
topics = ["Sosial", "Search", "Marketplace", "News", "Games"]

def add_topic():
    t, created = Topic.objects.get_or_create(top_name=random.choice(topics))
    return t

def populate(N=5):
    for entry in range(N):
        top = add_topic()
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        webpg, created = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)
        acc_rec, created = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)

if __name__ == '__main__':
    print("Populating script...")
    populate(20)
    print("Populating complete!")
