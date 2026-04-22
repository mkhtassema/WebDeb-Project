import { Routes } from '@angular/router';
import { authGuard } from './guards/auth.guard';

export const routes: Routes = [
  { path: '', redirectTo: '/movies', pathMatch: 'full' },
  { path: 'login', loadComponent: () => import('./pages/login/login.component').then(m => m.LoginComponent) },
  { path: 'register', loadComponent: () => import('./pages/register/register.component').then(m => m.RegisterComponent) },
  { path: 'movies', loadComponent: () => import('./pages/movies/movies.component').then(m => m.MoviesComponent), canActivate: [authGuard] },
  { path: 'movie/:id', loadComponent: () => import('./pages/movie-detail/movie-detail.component').then(m => m.MovieDetailComponent), canActivate: [authGuard] },
  { path: 'profile', loadComponent: () => import('./pages/profile/profile.component').then(m => m.ProfileComponent), canActivate: [authGuard] },
  { path: 'discover', loadComponent: () => import('./pages/discover/discover.component').then(m => m.DiscoverComponent), canActivate: [authGuard] },
  { path: 'test', loadComponent: () => import('./pages/personality-test/personality-test.component').then(m => m.PersonalityTestComponent), canActivate: [authGuard] },
  { path: 'polls', loadComponent: () => import('./pages/polls/polls.component').then(m => m.PollsComponent), canActivate: [authGuard] },
  { path: 'match', loadComponent: () => import('./pages/match/match.component').then(m => m.MatchComponent), canActivate: [authGuard] },
  { path: '**', redirectTo: '/movies' }
];
