import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { ProfileService } from '../../services/profile.service';

@Component({
  selector: 'app-match',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './match.component.html',
  styleUrl: './match.component.css'
})
export class MatchComponent {
  userId = '';
  result: any = null;
  loading = false;
  error = '';

  constructor(private profileService: ProfileService) {}

  findMatch() {
    if (!this.userId.trim()) return;
    this.loading = true;
    this.error = '';
    this.result = null;
    this.profileService.matchUser(this.userId.trim()).subscribe({
      next: (data) => { this.result = data; this.loading = false; },
      error: (err) => {
        this.error = err.error?.error || 'User not found';
        this.loading = false;
      }
    });
  }

  getScoreColor(): string {
    if (!this.result) return '#888';
    const s = this.result.compatibility_score;
    if (s >= 70) return '#4cff6b';
    if (s >= 40) return '#ffa500';
    return '#ff6b6b';
  }

  getScoreLabel(): string {
    if (!this.result) return '';
    const s = this.result.compatibility_score;
    if (s >= 80) return 'Perfect Match! 🎉';
    if (s >= 60) return 'Great Match! 😊';
    if (s >= 40) return 'Good Match 👍';
    if (s >= 20) return 'Some overlap 🤔';
    return 'Different tastes 🎭';
  }
}
