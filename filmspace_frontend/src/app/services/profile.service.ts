import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({ providedIn: 'root' })
export class ProfileService {
  private apiUrl = 'http://localhost:8000/api';

  constructor(private http: HttpClient) {}

  getProfile(): Observable<any> {
    return this.http.get<any>(`${this.apiUrl}/profile/`);
  }

  updateProfile(data: any): Observable<any> {
    return this.http.patch<any>(`${this.apiUrl}/profile/`, data);
  }

  updateCoins(amount: number): Observable<any> {
    return this.http.patch<any>(`${this.apiUrl}/profile/coins/`, { amount });
  }

  matchUser(userId: string): Observable<any> {
    return this.http.get<any>(`${this.apiUrl}/match/${userId}/`);
  }
}
