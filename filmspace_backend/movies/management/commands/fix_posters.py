from django.core.management.base import BaseCommand
from movies.models import Movie


POSTER_BASE_URL = 'https://image.tmdb.org/t/p/w500'

# Verified correct poster paths sourced directly from TMDB movie pages (all return HTTP 200)
CORRECT_POSTER_PATHS = {
    'The Notebook': '/rNzQyW4f8B8cQeg7Dgj3n6eT5k9.jpg',
    'Eternal Sunshine of the Spotless Mind': '/5MwkWH9tYHv3mV9OdYTMR5qreIz.jpg',
    'The Grand Budapest Hotel': '/eWdyYQreja6JGCzqHWXpWHDrrPo.jpg',
    'Mad Max: Fury Road': '/hA2ple9q4qnwxp3hKVNhroipsir.jpg',
    'Amélie': '/nSxDa3M9aMvGVLoItzWTepQ5h5d.jpg',
    'Gone Girl': '/ts996lKsxvjkO2yiYG0ht4qAicO.jpg',
    '13th': '/tcKNWD6IFPPsvkpvyZ548naz0is.jpg',
    'Inside Out': '/2H1TmgdfNtsKlU9jKdeNyYL5y8T.jpg',
    'Her': '/eCOtqtfvn7mxGl6nfmq4b1exJRc.jpg',
    'The Revenant': '/ji3ecJphATlVgWNY0B0RVXZizdf.jpg',
    'A Beautiful Mind': '/zwzWCmH72OSC9NA0ipoqw5Zjya8.jpg',
}


class Command(BaseCommand):
    help = 'Fix broken TMDB poster URLs for movies in the database'

    def handle(self, *args, **options):
        updated = 0
        not_found = []

        for title, poster_path in CORRECT_POSTER_PATHS.items():
            try:
                movie = Movie.objects.get(title=title)
                new_url = POSTER_BASE_URL + poster_path
                old_url = movie.poster_url
                movie.poster_url = new_url
                movie.save(update_fields=['poster_url'])
                self.stdout.write(
                    self.style.SUCCESS(f'Updated ID {movie.id}: {title}')
                )
                self.stdout.write(f'  Old: {old_url}')
                self.stdout.write(f'  New: {new_url}')
                updated += 1
            except Movie.DoesNotExist:
                not_found.append(title)
                self.stdout.write(
                    self.style.WARNING(f'Movie not found in DB: {title}')
                )

        self.stdout.write('')
        self.stdout.write(self.style.SUCCESS(f'Done. Updated {updated} movies.'))
        if not_found:
            self.stdout.write(
                self.style.WARNING(f'Not found in DB: {", ".join(not_found)}')
            )
