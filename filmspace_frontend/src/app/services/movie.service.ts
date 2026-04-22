import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({ providedIn: 'root' })
export class MovieService {
  private apiUrl = 'http://localhost:8000/api';

  constructor(private http: HttpClient) {}

  getMovies(filters?: { mood?: string; genre?: string; search?: string }): Observable<any[]> {
    let params = new HttpParams();
    if (filters?.mood) params = params.set('mood', filters.mood);
    if (filters?.genre) params = params.set('genre', filters.genre);
    if (filters?.search) params = params.set('search', filters.search);
    return this.http.get<any[]>(`${this.apiUrl}/movies/`, { params });
  }

  getMovie(id: number): Observable<any> {
    return this.http.get<any>(`${this.apiUrl}/movies/${id}/`);
  }

  getRandomMovie(): Observable<any> {
    return this.http.get<any>(`${this.apiUrl}/movies/random/`);
  }

  recommendByEmotion(text: string): Observable<any> {
    return this.http.post<any>(`${this.apiUrl}/emotion/`, { text });
  }

  submitPersonalityTest(answers: any): Observable<any> {
    return this.http.post<any>(`${this.apiUrl}/test/`, { answers });
  }

  getReviews(movieId: number): Observable<any[]> {
    return this.http.get<any[]>(`${this.apiUrl}/reviews/?movie=${movieId}`);
  }

  createReview(data: any): Observable<any> {
    return this.http.post<any>(`${this.apiUrl}/reviews/`, data);
  }

  updateReview(id: number, data: any): Observable<any> {
    return this.http.patch<any>(`${this.apiUrl}/reviews/${id}/`, data);
  }

  deleteReview(id: number): Observable<any> {
    return this.http.delete<any>(`${this.apiUrl}/reviews/${id}/`);
  }

  getFavorites(): Observable<any[]> {
    return this.http.get<any[]>(`${this.apiUrl}/favorites/`);
  }

  addFavorite(movieId: number): Observable<any> {
    return this.http.post<any>(`${this.apiUrl}/favorites/`, { movie: movieId });
  }

  removeFavorite(movieId: number): Observable<any> {
    return this.http.delete<any>(`${this.apiUrl}/favorites/`, { body: { movie: movieId } });
  }
}
