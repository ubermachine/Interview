import { Component, inject, signal, ChangeDetectionStrategy, DecimalPipe } from '@angular/core';
import { takeUntilDestroyed, toSignal } from '@angular/core/rxjs-interop';
import { Observable } from 'rxjs';
import { FormsModule } from '@angular/forms';

export interface PriceTick {
  readonly symbol: string;
  readonly bid: number;
  readonly ask: number;
  readonly timestamp: number;
}

export abstract class PriceStreamService {
  abstract getPriceStream(symbol: string): Observable<PriceTick>;
}

@Component({
  selector: 'app-senior-order-modal',
  standalone: true,
  imports: [DecimalPipe, FormsModule],
  changeDetection: ChangeDetectionStrategy.OnPush,
  template: `
    <div class="modal-card bg-slate-900 text-white p-6 rounded-2xl max-w-md">
      <h3>Order: {{ activeSymbol() }}</h3>

      @if (liveTick(); as tick) {
        <div class="grid grid-cols-2 gap-4 my-4 p-4 bg-slate-800 rounded-xl">
          <div>
            <span class="text-xs text-slate-400 block">BID</span>
            <span class="text-2xl font-mono text-red-400">{{ tick.bid | number:'1.2-2' }}</span>
          </div>
          <div>
            <span class="text-xs text-slate-400 block">ASK</span>
            <span class="text-2xl font-mono text-emerald-400">{{ tick.ask | number:'1.2-2' }}</span>
          </div>
        </div>
      } @else {
        <div class="p-4 text-center text-slate-400">Awaiting market quote...</div>
      }

      <input 
        [ngModel]="quantity()" 
        (ngModelChange)="quantity.set($event)"
        type="number" 
        class="w-full px-3 py-2 bg-slate-800 rounded border border-slate-700" />
    </div>
  `
})
export class SeniorOrderModalComponent {
  private readonly streamService = inject(PriceStreamService);

  readonly activeSymbol = signal<string>('EURUSD');
  readonly quantity = signal<number>(100);

  // Auto-unsubscribes on component destruction via injection context
  readonly liveTick = toSignal(
    this.streamService.getPriceStream(this.activeSymbol()).pipe(
      takeUntilDestroyed()
    )
  );
}
