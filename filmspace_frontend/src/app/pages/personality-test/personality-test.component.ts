import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Router } from '@angular/router';
import { MovieService } from '../../services/movie.service';

@Component({
  selector: 'app-personality-test',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './personality-test.component.html',
  styleUrl: './personality-test.component.css'
})
export class PersonalityTestComponent {
  questions = [
    {
      id: 'q1', text: 'On a Friday night, you prefer to:',
      options: [
        { value: 'a', label: 'Go on a spontaneous adventure' },
        { value: 'b', label: 'Stay in and watch a romantic movie' },
        { value: 'c', label: 'Read or watch a documentary' },
        { value: 'd', label: 'Do something thrilling like skydiving' },
      ]
    },
    {
      id: 'q2', text: 'When choosing a movie, what draws you in?',
      options: [
        { value: 'e', label: 'Deep emotional stories' },
        { value: 'f', label: 'Comedy that makes you laugh out loud' },
        { value: 'a', label: 'Stunning exotic locations' },
        { value: 'c', label: 'Clever plot twists and mind games' },
      ]
    },
    {
      id: 'q3', text: 'Your ideal vacation is:',
      options: [
        { value: 'a', label: 'Backpacking across different countries' },
        { value: 'b', label: 'A romantic getaway for two' },
        { value: 'd', label: 'Extreme sports destination' },
        { value: 'f', label: 'A comedy festival or theme park' },
      ]
    },
    {
      id: 'q4', text: 'Which movie quote resonates with you most?',
      options: [
        { value: 'e', label: '"We accept the love we think we deserve"' },
        { value: 'c', label: '"You cannot change what you are, only what you do"' },
        { value: 'b', label: '"The best love is the kind that awakens the soul"' },
        { value: 'a', label: '"Adventure is out there!"' },
      ]
    },
    {
      id: 'q5', text: 'After watching a sad movie, you:',
      options: [
        { value: 'e', label: 'Cry and feel deeply connected to the characters' },
        { value: 'f', label: 'Immediately find a comedy to cheer up' },
        { value: 'c', label: 'Analyze the themes and message for hours' },
        { value: 'd', label: 'Go work out to shake off the feelings' },
      ]
    },
  ];

  answers: any = {};
  result: any = null;
  loading = false;
  currentQ = 0;

  constructor(private movieService: MovieService, private router: Router) {}

  get currentQuestion() { return this.questions[this.currentQ]; }
  get progress() { return ((this.currentQ) / this.questions.length) * 100; }
  get allAnswered() { return Object.keys(this.answers).length === this.questions.length; }

  selectAnswer(questionId: string, value: string) {
    this.answers[questionId] = value;
    if (this.currentQ < this.questions.length - 1) {
      setTimeout(() => this.currentQ++, 300);
    }
  }

  submitTest() {
    this.loading = true;
    this.movieService.submitPersonalityTest(this.answers).subscribe({
      next: (data) => { this.result = data; this.loading = false; },
      error: () => { this.loading = false; }
    });
  }

  goToMovie(id: number) { this.router.navigate(['/movie', id]); }
  restart() { this.answers = {}; this.result = null; this.currentQ = 0; }
  getDnaWidth(value: unknown): number { return (Number(value) / 5) * 100; }
}
