from django.core.management.base import BaseCommand
from django.utils import timezone
from django_seed.seeder import Seeder
from faker import Faker

from apps.data_collection.models import *


def add_dummy_data(num_article=10):
    seeder = Seeder(faker=Faker())

    # article
    seeder.add_entity(Article, num_article, {
        'title': lambda x: '마약' + seeder.faker.sentence(),
        'content': lambda x: '모르핀 펜타닐 ' + seeder.faker.sentence(),
        'written_at': lambda x: timezone.now().strftime('%Y-%m-%d'),
        'url': lambda x: seeder.faker.url()
    })
    seeder.execute()
    print(f'{num_article} dummy articles created!')

    # words
    word_count = 0
    for article in Article.objects.all():
        for word in article.content.split():
            Word.objects.create(
                article_id=article,
                text=word
            )
            word_count += 1

    print(f'{word_count} dummy word created!')


def remove_dummy_data():
    Word.objects.all().delete()
    Article.objects.all().delete()


class Command(BaseCommand):
    help = 'Adds or removes dummy data.'

    def add_arguments(self, parser):
        parser.add_argument('action', type=str, choices=['add', 'remove'])
        parser.add_argument(
            '--num',
            type=int,
            default=10,
            help='Number of questions to add (default: 10)',
            required=False
        )

    def handle(self, *args, **options):
        action = options['action']

        if action == 'add':
            num = options['num']
            add_dummy_data(num)
            self.stdout.write(self.style.SUCCESS('Successfully added dummy data.'))
        elif action == 'remove':
            remove_dummy_data()
            self.stdout.write(self.style.SUCCESS('Successfully removed dummy data.'))
