import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Router } from '@angular/router';
import { MovieService } from '../../services/movie.service';

@Component({
  selector: 'app-movies',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './movies.component.html',
  styleUrl: './movies.component.css'
})
export class MoviesComponent implements OnInit {
  movies: any[] = [];
  loading = false;
  randomMovie: any = null;
  searchTerm = '';
  selectedMood = '';
  selectedGenre = '';

  moods = ['happy','sad','excited','anxious','relaxed','angry','inspired','lonely','romantic','adventurous'];
  genres = ['action','comedy','drama','horror','romance','sci-fi','thriller','animation','documentary','fantasy'];

  constructor(private movieService: MovieService, private router: Router) {}

  ngOnInit() { this.loadMovies(); }

  loadMovies() {
    this.loading = true;
    this.movieService.getMovies({
      mood: this.selectedMood,
      genre: this.selectedGenre,
      search: this.searchTerm
    }).subscribe({
      next: (data) => { this.movies = data; this.loading = false; },
      error: () => { this.loading = false; }
    });
  }

  getRandomMovie() {
    this.movieService.getRandomMovie().subscribe({
      next: (movie) => { this.randomMovie = movie; }
    });
  }

  clearFilters() {
    this.selectedMood = '';
    this.selectedGenre = '';
    this.searchTerm = '';
    this.loadMovies();
  }

  goToMovie(id: number) {
    this.router.navigate(['/movie', id]);
  }

  toggleFavorite(event: Event, movie: any) {
    event.stopPropagation();
    if (movie.is_favorite) {
      this.movieService.removeFavorite(movie.id).subscribe(() => movie.is_favorite = false);
    } else {
      this.movieService.addFavorite(movie.id).subscribe(() => movie.is_favorite = true);
    }
  }

  getRatingStars(rating: number): string {
    return '★'.repeat(Math.round(rating / 2)) + '☆'.repeat(5 - Math.round(rating / 2));
  }
}
