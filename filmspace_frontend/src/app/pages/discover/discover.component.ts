import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Router } from '@angular/router';
import { MovieService } from '../../services/movie.service';

@Component({
  selector: 'app-discover',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './discover.component.html',
  styleUrl: './discover.component.css'
})
export class DiscoverComponent {
  lifeText = '';
  result: any = null;
  loading = false;
  error = '';

  selectedMood = '';
  moodResult: any = null;

  moods = [
    { key: 'happy', emoji: '😊', label: 'Happy' },
    { key: 'sad', emoji: '😢', label: 'Sad' },
    { key: 'excited', emoji: '🤩', label: 'Excited' },
    { key: 'anxious', emoji: '😰', label: 'Anxious' },
    { key: 'relaxed', emoji: '😌', label: 'Relaxed' },
    { key: 'angry', emoji: '😤', label: 'Angry' },
    { key: 'inspired', emoji: '✨', label: 'Inspired' },
    { key: 'lonely', emoji: '🥺', label: 'Lonely' },
    { key: 'romantic', emoji: '❤️', label: 'Romantic' },
    { key: 'adventurous', emoji: '🌍', label: 'Adventurous' },
  ];

  constructor(private movieService: MovieService, private router: Router) {}

  analyzeEmotion() {
    if (!this.lifeText.trim()) return;
    this.loading = true;
    this.error = '';
    this.result = null;
    this.movieService.recommendByEmotion(this.lifeText).subscribe({
      next: (data) => { this.result = data; this.loading = false; },
      error: () => { this.error = 'Could not analyze. Try again.'; this.loading = false; }
    });
  }

  selectMood(mood: string) {
    this.selectedMood = mood;
    this.movieService.getMovies({ mood }).subscribe({
      next: (movies) => {
        const random = movies[Math.floor(Math.random() * movies.length)];
        this.moodResult = random;
      }
    });
  }

  goToMovie(id: number) { this.router.navigate(['/movie', id]); }
}
