from django.core.management.base import BaseCommand
from django.conf import settings
from djongo import models

from octofit_tracker import models as octo_models

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        octo_models.User.objects.all().delete()
        octo_models.Team.objects.all().delete()
        octo_models.Activity.objects.all().delete()
        octo_models.Leaderboard.objects.all().delete()
        octo_models.Workout.objects.all().delete()

        # Create Teams
        marvel = octo_models.Team.objects.create(name='Marvel')
        dc = octo_models.Team.objects.create(name='DC')

        # Create Users
        tony = octo_models.User.objects.create(name='Tony Stark', email='tony@marvel.com', team=marvel)
        steve = octo_models.User.objects.create(name='Steve Rogers', email='steve@marvel.com', team=marvel)
        bruce = octo_models.User.objects.create(name='Bruce Wayne', email='bruce@dc.com', team=dc)
        clark = octo_models.User.objects.create(name='Clark Kent', email='clark@dc.com', team=dc)

        # Create Activities
        octo_models.Activity.objects.create(user=tony, type='Run', duration=30, calories=300)
        octo_models.Activity.objects.create(user=steve, type='Swim', duration=45, calories=400)
        octo_models.Activity.objects.create(user=bruce, type='Cycle', duration=60, calories=500)
        octo_models.Activity.objects.create(user=clark, type='Run', duration=50, calories=450)

        # Create Workouts
        octo_models.Workout.objects.create(name='Morning Cardio', description='Cardio for all heroes', duration=40)
        octo_models.Workout.objects.create(name='Strength Training', description='Strength for all heroes', duration=60)

        # Create Leaderboard
        octo_models.Leaderboard.objects.create(user=tony, score=1000)
        octo_models.Leaderboard.objects.create(user=steve, score=900)
        octo_models.Leaderboard.objects.create(user=bruce, score=950)
        octo_models.Leaderboard.objects.create(user=clark, score=980)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
