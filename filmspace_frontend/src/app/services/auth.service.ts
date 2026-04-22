import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';
import { BehaviorSubject, Observable, tap } from 'rxjs';

@Injectable({ providedIn: 'root' })
export class AuthService {
  private apiUrl = 'http://localhost:8000/api';
  private currentUserSubject = new BehaviorSubject<any>(this.getStoredUser());
  currentUser$ = this.currentUserSubject.asObservable();

  constructor(private http: HttpClient, private router: Router) {}

  register(data: any): Observable<any> {
    return this.http.post(`${this.apiUrl}/auth/register/`, data).pipe(
      tap((res: any) => this.storeTokens(res))
    );
  }

  login(data: any): Observable<any> {
    return this.http.post(`${this.apiUrl}/auth/login/`, data).pipe(
      tap((res: any) => this.storeTokens(res))
    );
  }

  logout(): void {
    const refresh = localStorage.getItem('refresh_token');
    this.http.post(`${this.apiUrl}/auth/logout/`, { refresh }).subscribe();
    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');
    localStorage.removeItem('current_user');
    this.currentUserSubject.next(null);
    this.router.navigate(['/login']);
  }

  private storeTokens(res: any): void {
    localStorage.setItem('access_token', res.access);
    localStorage.setItem('refresh_token', res.refresh);
    localStorage.setItem('current_user', JSON.stringify(res.user));
    this.currentUserSubject.next(res.user);
  }

  private getStoredUser(): any {
    const u = localStorage.getItem('current_user');
    return u ? JSON.parse(u) : null;
  }

  isLoggedIn(): boolean {
    return !!localStorage.getItem('access_token');
  }

  getCurrentUser(): any {
    return this.currentUserSubject.value;
  }
}
