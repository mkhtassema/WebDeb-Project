import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Router } from '@angular/router';
import { ProfileService } from '../../services/profile.service';
import { MovieService } from '../../services/movie.service';

@Component({
  selector: 'app-profile',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './profile.component.html',
  styleUrl: './profile.component.css'
})
export class ProfileComponent implements OnInit {
  profile: any = null;
  favorites: any[] = [];
  loading = true;
  editMode = false;
  editForm: any = {};
  saveLoading = false;
  saveSuccess = false;

  genres = ['action','comedy','drama','horror','romance','sci-fi','thriller','animation','documentary','fantasy'];

  constructor(private profileService: ProfileService, private movieService: MovieService, private router: Router) {}

  ngOnInit() {
    this.loadProfile();
    this.loadFavorites();
  }

  loadProfile() {
    this.profileService.getProfile().subscribe({
      next: (data) => {
        this.profile = data;
        this.editForm = { bio: data.bio, favorite_genre: data.favorite_genre };
        this.loading = false;
      },
      error: () => { this.loading = false; }
    });
  }

  loadFavorites() {
    this.movieService.getFavorites().subscribe({
      next: (data) => { this.favorites = data; }
    });
  }

  saveProfile() {
    this.saveLoading = true;
    this.profileService.updateProfile(this.editForm).subscribe({
      next: (data) => {
        this.profile = data;
        this.editMode = false;
        this.saveLoading = false;
        this.saveSuccess = true;
        setTimeout(() => this.saveSuccess = false, 3000);
      },
      error: () => { this.saveLoading = false; }
    });
  }

  removeFavorite(movieId: number) {
    this.movieService.removeFavorite(movieId).subscribe(() => {
      this.favorites = this.favorites.filter(f => f.movie !== movieId);
    });
  }

  goToMovie(id: number) { this.router.navigate(['/movie', id]); }

  getLevelProgress(): number {
    if (!this.profile) return 0;
    const coinsInLevel = this.profile.coins % 50;
    return (coinsInLevel / 50) * 100;
  }

  getPersonalityEmoji(type: string): string {
    const map: any = {
      'explorer': '🌍', 'romantic': '❤️', 'thinker': '🧠',
      'thrill-seeker': '⚡', 'empath': '💫', 'humorist': '😄'
    };
    return map[type] || '🎬';
  }
}
