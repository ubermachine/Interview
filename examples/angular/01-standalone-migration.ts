import { Component, inject, signal, ChangeDetectionStrategy, OnInit } from '@angular/core';
import { CurrencyPipe } from '@angular/common';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface Account {
  id: string;
  accountNumber: string;
  balance: number;
}

export class PortfolioService {
  private readonly http = inject(HttpClient);

  getAccounts(): Observable<Account[]> {
    return this.http.get<Account[]>('/api/portfolio/accounts');
  }
}

@Component({
  selector: 'app-senior-portfolio',
  standalone: true,
  imports: [CurrencyPipe],
  changeDetection: ChangeDetectionStrategy.OnPush,
  template: `
    @if (isLoading()) {
      <div class="skeleton-loader" role="status" aria-live="polite">
        <p>Loading portfolio accounts...</p>
      </div>
    } @else {
      <ul class="portfolio-list">
        @for (acc of accounts(); track acc.id) {
          <li class="account-row">
            <span class="font-mono">{{ acc.accountNumber }}</span>
            <span class="font-bold">{{ acc.balance | currency:'USD' }}</span>
          </li>
        } @empty {
          <li class="empty-state">No accounts registered.</li>
        }
      </ul>
    }
  `
})
export class SeniorPortfolioComponent implements OnInit {
  private readonly portfolioService = inject(PortfolioService);

  readonly accounts = signal<Account[]>([]);
  readonly isLoading = signal<boolean>(true);

  ngOnInit(): void {
    this.portfolioService.getAccounts().subscribe({
      next: (data) => {
        this.accounts.set(data);
        this.isLoading.set(false);
      },
      error: () => this.isLoading.set(false)
    });
  }
}
