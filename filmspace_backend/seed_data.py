import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from movies.models import Movie

movies_data = [
    {
        'title': 'Inception', 'description': 'A thief who steals corporate secrets through dream-sharing technology.', 
        'genre': 'sci-fi', 'mood': 'excited', 'rating': 8.8, 'year': 2010,
        'director': 'Christopher Nolan',
        'poster_url': 'https://image.tmdb.org/t/p/w500/9gk7adHYeDvHkCSEqAvQNLV5Uge.jpg',
        'keywords': 'dream,heist,mind,reality'
    },
    {
        'title': 'The Notebook', 'description': 'A poor yet passionate young man falls in love with a rich young woman.',
        'genre': 'romance', 'mood': 'romantic', 'rating': 7.8, 'year': 2004,
        'director': 'Nick Cassavetes',
        'poster_url': 'https://image.tmdb.org/t/p/w500/qom1SZSENdmHFNZBXbtLAGVbrlz.jpg',
        'keywords': 'love,romance,passion,memories'
    },
    {
        'title': 'The Dark Knight', 'description': 'Batman faces the Joker, a criminal mastermind who causes chaos.',
        'genre': 'action', 'mood': 'excited', 'rating': 9.0, 'year': 2008,
        'director': 'Christopher Nolan',
        'poster_url': 'https://image.tmdb.org/t/p/w500/qJ2tW6WMUDux911r6m7haRef0WH.jpg',
        'keywords': 'batman,joker,hero,villain'
    },
    {
        'title': 'Eternal Sunshine of the Spotless Mind', 'description': 'A couple erase memories of each other after a painful breakup.',
        'genre': 'romance', 'mood': 'sad', 'rating': 8.3, 'year': 2004,
        'director': 'Michel Gondry',
        'poster_url': 'https://image.tmdb.org/t/p/w500/5MwkWH9tYHv3mV9OaX5ltQ2whNB.jpg',
        'keywords': 'memory,love,loss,mind'
    },
    {
        'title': 'The Grand Budapest Hotel', 'description': 'A hotel concierge and lobby boy become embroiled in theft and murder.',
        'genre': 'comedy', 'mood': 'happy', 'rating': 8.1, 'year': 2014,
        'director': 'Wes Anderson',
        'poster_url': 'https://image.tmdb.org/t/p/w500/eWdyYQreja6JfmxWBfFrCbVlkij.jpg',
        'keywords': 'humor,quirky,adventure,hotel'
    },
    {
        'title': 'Interstellar', 'description': 'A team of explorers travel through a wormhole in space.',
        'genre': 'sci-fi', 'mood': 'inspired', 'rating': 8.6, 'year': 2014,
        'director': 'Christopher Nolan',
        'poster_url': 'https://image.tmdb.org/t/p/w500/gEU2QniE6E77NI6lCU6MxlNBvIx.jpg',
        'keywords': 'space,time,love,survival'
    },
    {
        'title': 'The Shawshank Redemption', 'description': 'A banker is sentenced to life in prison and finds hope through friendship.',
        'genre': 'drama', 'mood': 'inspired', 'rating': 9.3, 'year': 1994,
        'director': 'Frank Darabont',
        'poster_url': 'https://image.tmdb.org/t/p/w500/q6y0Go1tsGEsmtFryDOJo3dEmqu.jpg',
        'keywords': 'hope,freedom,friendship,prison'
    },
    {
        'title': 'Get Out', 'description': 'A Black man visits his white girlfriends family and uncovers a disturbing secret.',
        'genre': 'horror', 'mood': 'anxious', 'rating': 7.7, 'year': 2017,
        'director': 'Jordan Peele',
        'poster_url': 'https://image.tmdb.org/t/p/w500/tFXcEccSQMf3lfhfXKSU9iRBpa3.jpg',
        'keywords': 'horror,race,psychological,mystery'
    },
    {
        'title': 'Spirited Away', 'description': 'A young girl wanders into a world ruled by gods, witches, and monsters.',
        'genre': 'animation', 'mood': 'adventurous', 'rating': 8.6, 'year': 2001,
        'director': 'Hayao Miyazaki',
        'poster_url': 'https://image.tmdb.org/t/p/w500/39wmItIWsg5sZMyRUHLkWBcuVCM.jpg',
        'keywords': 'magic,adventure,spirits,journey'
    },
    {
        'title': 'La La Land', 'description': 'A jazz musician and an aspiring actress fall in love while struggling to succeed.',
        'genre': 'romance', 'mood': 'romantic', 'rating': 8.0, 'year': 2016,
        'director': 'Damien Chazelle',
        'poster_url': 'https://image.tmdb.org/t/p/w500/uDO8zWDhfWwoFdKS4fzkUJt0Rf0.jpg',
        'keywords': 'music,love,dreams,jazz'
    },
    {
        'title': 'Mad Max: Fury Road', 'description': 'In a post-apocalyptic wasteland, Max teams with a warrior named Furiosa.',
        'genre': 'action', 'mood': 'angry', 'rating': 8.1, 'year': 2015,
        'director': 'George Miller',
        'poster_url': 'https://image.tmdb.org/t/p/w500/8tZYtuWezp8JbcsvHfd1sDiQW9z.jpg',
        'keywords': 'war,survival,desert,rebellion'
    },
    {
        'title': 'Amélie', 'description': 'A shy waitress decides to change the lives of those around her.',
        'genre': 'romance', 'mood': 'happy', 'rating': 8.3, 'year': 2001,
        'director': 'Jean-Pierre Jeunet',
        'poster_url': 'https://image.tmdb.org/t/p/w500/rOlGjoXxBo5Cw3Y6v6lbpf8wDLU.jpg',
        'keywords': 'whimsical,kindness,love,Paris'
    },
    {
        'title': 'Gone Girl', 'description': 'A man becomes the prime suspect in the disappearance of his wife.',
        'genre': 'thriller', 'mood': 'anxious', 'rating': 8.1, 'year': 2014,
        'director': 'David Fincher',
        'poster_url': 'https://image.tmdb.org/t/p/w500/sPp82mAhFujPuqgWhUlK0vCEiGt.jpg',
        'keywords': 'mystery,marriage,thriller,suspense'
    },
    {
        'title': '13th', 'description': 'An exploration of the intersection of race, justice, and mass incarceration in the US.',
        'genre': 'documentary', 'mood': 'inspired', 'rating': 8.2, 'year': 2016,
        'director': 'Ava DuVernay',
        'poster_url': 'https://image.tmdb.org/t/p/w500/pvGKqaLGMeIPOITOtcFl3PVInJv.jpg',
        'keywords': 'justice,race,history,politics'
    },
    {
        'title': 'The Lord of the Rings: Fellowship of the Ring', 'description': 'A young hobbit and his companions set off on a quest to destroy a powerful ring.',
        'genre': 'fantasy', 'mood': 'adventurous', 'rating': 8.8, 'year': 2001,
        'director': 'Peter Jackson',
        'poster_url': 'https://image.tmdb.org/t/p/w500/6oom5QYQ2yQTMJIbnvbkBL9cHo6.jpg',
        'keywords': 'quest,magic,friendship,evil'
    },
    {
        'title': 'Inside Out', 'description': 'A young girl is uprooted from her life when emotions inside her head go on a journey.',
        'genre': 'animation', 'mood': 'relaxed', 'rating': 8.1, 'year': 2015,
        'director': 'Pete Docter',
        'poster_url': 'https://image.tmdb.org/t/p/w500/aAmfIX3TT40zUHGcCKrlOZRKC7u.jpg',
        'keywords': 'emotions,family,growing up,mind'
    },
    {
        'title': 'Her', 'description': 'A lonely writer develops an unlikely relationship with an AI operating system.',
        'genre': 'romance', 'mood': 'lonely', 'rating': 8.0, 'year': 2013,
        'director': 'Spike Jonze',
        'poster_url': 'https://image.tmdb.org/t/p/w500/eCOtqtfvn7mxGGGHoTzSBQYQsXO.jpg',
        'keywords': 'AI,loneliness,love,future'
    },
    {
        'title': 'The Revenant', 'description': 'A frontiersman on a fur trading expedition fights for survival after a bear attack.',
        'genre': 'thriller', 'mood': 'angry', 'rating': 8.0, 'year': 2015,
        'director': 'Alejandro G. Inarritu',
        'poster_url': 'https://image.tmdb.org/t/p/w500/oEpFfik63e4QhhnGPPNEkRVxLdT.jpg',
        'keywords': 'survival,revenge,wilderness,pain'
    },
    {
        'title': 'Coco', 'description': 'A young boy is transported to the Land of the Dead where he seeks his great-great-grandfather.',
        'genre': 'animation', 'mood': 'relaxed', 'rating': 8.4, 'year': 2017,
        'director': 'Lee Unkrich',
        'poster_url': 'https://image.tmdb.org/t/p/w500/gGEsBPAijhVUFoiNpgZXqRVWJt2.jpg',
        'keywords': 'family,music,death,culture'
    },
    {
        'title': 'A Beautiful Mind', 'description': 'The story of Nobel Laureate John Nash, a mathematical genius who struggled with schizophrenia.',
        'genre': 'drama', 'mood': 'inspired', 'rating': 8.2, 'year': 2001,
        'director': 'Ron Howard',
        'poster_url': 'https://image.tmdb.org/t/p/w500/aIFM2s3MzqGpHtXMBKjb8qFOhPB.jpg',
        'keywords': 'genius,mental health,math,love'
    },
]

for data in movies_data:
    Movie.objects.get_or_create(title=data['title'], defaults=data)

print(f'Seeded {len(movies_data)} movies successfully!')
