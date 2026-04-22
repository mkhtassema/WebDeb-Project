import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({ providedIn: 'root' })
export class SocialService {
  private apiUrl = 'http://localhost:8000/api';

  constructor(private http: HttpClient) {}

  getPolls(): Observable<any[]> {
    return this.http.get<any[]>(`${this.apiUrl}/polls/`);
  }

  createPoll(data: any): Observable<any> {
    return this.http.post<any>(`${this.apiUrl}/polls/`, data);
  }

  vote(pollId: number, movieId: number): Observable<any> {
    return this.http.post<any>(`${this.apiUrl}/polls/vote/`, { poll: pollId, selected_movie: movieId });
  }
}
