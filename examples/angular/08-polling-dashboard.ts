import { Component, inject, DestroyRef, signal, computed, ChangeDetectionStrategy } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Subject, merge, timer, of } from 'rxjs';
import { switchMap, catchError } from 'rxjs/operators';
import { takeUntilDestroyed } from '@angular/core/rxjs-interop';

export interface DashboardStats {
  readonly activeUsers: number;
  readonly loadPercent: number;
}

@Component({
  selector: 'app-senior-dashboard',
  standalone: true,
  changeDetection: ChangeDetectionStrategy.OnPush,
  template: `
    <div class="card p-6 bg-slate-900 text-white rounded-2xl max-w-md">
      <h3>System Metrics</h3>
      
      @if (isLoading()) {
        <div class="text-xs text-blue-400">Updating metrics...</div>
      }

      @if (stats(); as data) {
        <div class="space-y-2 my-4">
          <p>Active Users: {{ data.activeUsers }}</p>
          <p>Load: {{ data.loadPercent }}%</p>
        </div>
      }

      <button (click)="refresh()" class="px-4 py-2 bg-blue-600 rounded">
        Refresh Now
      </button>
    </div>
  `
})
export class SeniorDashboardComponent {
  private readonly http = inject(HttpClient);
  private readonly destroyRef = inject(DestroyRef);

  readonly stats = signal<DashboardStats | null>(null);
  readonly isLoading = signal<boolean>(false);
  private readonly manualRefresh$ = new Subject<void>();

  constructor() {
    merge(timer(0, 10000), this.manualRefresh$).pipe(
      switchMap(() => {
        this.isLoading.set(true);
        return this.http.get<DashboardStats>('/api/system/metrics').pipe(
          catchError(() => of(null))
        );
      }),
      takeUntilDestroyed(this.destroyRef)
    ).subscribe(data => {
      if (data) {
        this.stats.set(data);
      }
      this.isLoading.set(false);
    });
  }

  refresh(): void {
    this.manualRefresh$.next();
  }
}
