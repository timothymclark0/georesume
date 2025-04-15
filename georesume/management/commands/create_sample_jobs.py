# resume/management/commands/create_sample_jobs.py
import os
from datetime import date
from django.core.management.base import BaseCommand
from django.conf import settings
from georesume.models import JobExperience

class Command(BaseCommand):
    help = 'Creates sample job experiences for testing'

    def handle(self, *args, **options):
        # Sample job data
        sample_jobs = [
            {
                'title': 'Software Engineer',
                'company': 'Tech Innovations',
                'description': 'Developed and maintained web applications using Django and React. Implemented CI/CD pipelines and improved application performance.',
                'start_date': date(2020, 6, 1),
                'end_date': None,
                'is_current': True,
                'city': 'Seattle',
                'state': 'WA',
                'latitude': 47.6062,
                'longitude': -122.3321,
                'skills': 'Python, Django, React, AWS, Docker',
                'achievements': 'Reduced application load time by 40%, Implemented automated testing that increased code coverage to 85%',
                'order': 1,
            },
            {
                'title': 'Full Stack Developer',
                'company': 'Web Solutions Inc.',
                'description': 'Designed and built responsive web applications for clients across various industries. Worked in an agile team environment.',
                'start_date': date(2018, 3, 15),
                'end_date': date(2020, 5, 30),
                'is_current': False,
                'city': 'San Francisco',
                'state': 'CA',
                'latitude': 37.7749,
                'longitude': -122.4194,
                'skills': 'JavaScript, Node.js, Express, MongoDB, HTML/CSS',
                'achievements': 'Delivered 12 client projects on time and within budget, Mentored 3 junior developers',
                'order': 2,
            },
            {
                'title': 'Junior Developer',
                'company': 'Digital Startups',
                'description': 'Assisted in developing web applications and learned full stack development practices. Participated in code reviews and daily stand-up meetings.',
                'start_date': date(2016, 9, 1),
                'end_date': date(2018, 3, 1),
                'is_current': False,
                'city': 'Austin',
                'state': 'TX',
                'latitude': 30.2672,
                'longitude': -97.7431,
                'skills': 'JavaScript, jQuery, PHP, MySQL',
                'achievements': 'Implemented a feature that increased user engagement by 25%',
                'order': 3,
            },
            {
                'title': 'IT Intern',
                'company': 'Tech Solutions Corp',
                'description': 'Assisted the IT department with various tasks including basic software development, troubleshooting, and documentation.',
                'start_date': date(2015, 5, 15),
                'end_date': date(2016, 8, 31),
                'is_current': False,
                'city': 'Chicago',
                'state': 'IL',
                'latitude': 41.8781,
                'longitude': -87.6298,
                'skills': 'HTML, CSS, Basic JavaScript, Technical Support',
                'achievements': 'Created documentation that improved onboarding process',
                'order': 4,
            }
        ]
        
        # Create job instances
        jobs_created = 0
        for job_data in sample_jobs:
            # Skip if job with same title and company already exists
            if JobExperience.objects.filter(title=job_data['title'], company=job_data['company']).exists():
                self.stdout.write(self.style.WARNING(f"Job '{job_data['title']} at {job_data['company']}' already exists. Skipping."))
                continue
                
            JobExperience.objects.create(**job_data)
            jobs_created += 1
        
        self.stdout.write(self.style.SUCCESS(f'Successfully created {jobs_created} sample job experiences'))