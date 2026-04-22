import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { MovieService } from '../../services/movie.service';
import { AuthService } from '../../services/auth.service';

@Component({
  selector: 'app-movie-detail',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './movie-detail.component.html',
  styleUrl: './movie-detail.component.css'
})
export class MovieDetailComponent implements OnInit {
  movie: any = null;
  reviews: any[] = [];
  loading = true;
  newReview = { text: '', rating: 5 };
  reviewError = '';
  reviewLoading = false;
  currentUser: any;
  editingReview: any = null;

  constructor(
    private route: ActivatedRoute,
    private router: Router,
    private movieService: MovieService,
    private authService: AuthService
  ) {}

  ngOnInit() {
    this.currentUser = this.authService.getCurrentUser();
    const id = Number(this.route.snapshot.paramMap.get('id'));
    this.loadMovie(id);
    this.loadReviews(id);
  }

  loadMovie(id: number) {
    this.movieService.getMovie(id).subscribe({
      next: (data) => { this.movie = data; this.loading = false; },
      error: () => { this.loading = false; }
    });
  }

  loadReviews(id: number) {
    this.movieService.getReviews(id).subscribe({
      next: (data) => { this.reviews = data; }
    });
  }

  submitReview() {
    if (!this.newReview.text.trim()) return;
    this.reviewLoading = true;
    this.reviewError = '';
    this.movieService.createReview({ ...this.newReview, movie: this.movie.id }).subscribe({
      next: (review) => {
        this.reviews.unshift(review);
        this.newReview = { text: '', rating: 5 };
        this.reviewLoading = false;
      },
      error: (err) => {
        this.reviewError = err.error?.non_field_errors?.[0] || 'Failed to submit review';
        this.reviewLoading = false;
      }
    });
  }

  deleteReview(id: number) {
    this.movieService.deleteReview(id).subscribe(() => {
      this.reviews = this.reviews.filter(r => r.id !== id);
    });
  }

  toggleFavorite() {
    if (this.movie.is_favorite) {
      this.movieService.removeFavorite(this.movie.id).subscribe(() => this.movie.is_favorite = false);
    } else {
      this.movieService.addFavorite(this.movie.id).subscribe(() => this.movie.is_favorite = true);
    }
  }

  goBack() { this.router.navigate(['/movies']); }
}
