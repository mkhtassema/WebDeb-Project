from urllib.parse import quote_plus

from django.core.management.base import BaseCommand

from movies.models import Movie


class Command(BaseCommand):
    help = 'Populate watch_url for all movies using Google search fallback links'

    def handle(self, *args, **options):
        movies = Movie.objects.all()
        updated = 0

        for movie in movies:
            if not movie.watch_url:
                query = quote_plus(f'watch {movie.title}')
                movie.watch_url = f'https://www.google.com/search?q={query}'
                movie.save(update_fields=['watch_url'])
                self.stdout.write(self.style.SUCCESS(f'Set watch_url for: {movie.title}'))
                updated += 1
            else:
                self.stdout.write(f'Skipped (already set): {movie.title}')

        self.stdout.write('')
        self.stdout.write(self.style.SUCCESS(f'Done. Updated {updated} movies.'))
