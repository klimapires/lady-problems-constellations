#!/usr/bin/env python
import os
import sys
import random

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "constellations.settings")

django.setup()

from faker import Factory

fake = Factory.create('pt_BR')

from website.models import JobPost, JobArea

for _ in range(10):
    JobPost.objects.create(
        title=fake.job(),
        description=fake.catch_phrase(),
        area=random.choice(JobArea.objects.all()),
        budget=random.randint(100, 10000),
    )
