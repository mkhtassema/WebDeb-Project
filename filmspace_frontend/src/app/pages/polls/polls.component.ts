import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { SocialService } from '../../services/social.service';
import { MovieService } from '../../services/movie.service';
import { AuthService } from '../../services/auth.service';

@Component({
  selector: 'app-polls',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './polls.component.html',
  styleUrl: './polls.component.css'
})
export class PollsComponent implements OnInit {
  polls: any[] = [];
  movies: any[] = [];
  loading = false;
  currentUser: any;

  showCreateForm = false;
  newPoll = { question: '', movie_options: [] as number[] };
  createLoading = false;

  constructor(
    private socialService: SocialService,
    private movieService: MovieService,
    private authService: AuthService
  ) {}

  ngOnInit() {
    this.currentUser = this.authService.getCurrentUser();
    this.loadPolls();
    this.loadMovies();
  }

  loadPolls() {
    this.loading = true;
    this.socialService.getPolls().subscribe({
      next: (data) => { this.polls = data; this.loading = false; },
      error: () => { this.loading = false; }
    });
  }

  loadMovies() {
    this.movieService.getMovies().subscribe({
      next: (data) => { this.movies = data; }
    });
  }

  createPoll() {
    if (!this.newPoll.question.trim()) return;
    this.createLoading = true;
    this.socialService.createPoll(this.newPoll).subscribe({
      next: (poll) => {
        this.polls.unshift(poll);
        this.newPoll = { question: '', movie_options: [] };
        this.showCreateForm = false;
        this.createLoading = false;
      },
      error: () => { this.createLoading = false; }
    });
  }

  vote(pollId: number, movieId: number) {
    this.socialService.vote(pollId, movieId).subscribe({
      next: () => { this.loadPolls(); }
    });
  }

  toggleMovieOption(movieId: number) {
    const idx = this.newPoll.movie_options.indexOf(movieId);
    if (idx >= 0) {
      this.newPoll.movie_options.splice(idx, 1);
    } else {
      this.newPoll.movie_options.push(movieId);
    }
  }

  hasVoted(poll: any): boolean {
    return poll.votes?.some((v: any) => v.username === this.currentUser?.username);
  }

  getVoteCount(poll: any, movieId: number): number {
    return poll.votes?.filter((v: any) => v.selected_movie === movieId).length || 0;
  }

  getVotePercent(poll: any, movieId: number): number {
    const total = poll.votes?.length || 0;
    if (!total) return 0;
    return Math.round((this.getVoteCount(poll, movieId) / total) * 100);
  }
}
