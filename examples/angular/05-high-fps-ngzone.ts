import { 
  Component, 
  ElementRef, 
  viewChild, 
  inject, 
  NgZone, 
  AfterViewInit, 
  OnDestroy, 
  ChangeDetectionStrategy,
  signal 
} from '@angular/core';

@Component({
  selector: 'app-senior-depth-chart',
  standalone: true,
  changeDetection: ChangeDetectionStrategy.OnPush,
  template: `
    <div class="relative w-full h-[400px] bg-slate-950 rounded-xl overflow-hidden">
      <canvas #canvasRef class="w-full h-full block"></canvas>
      <div 
        #crosshairRef 
        class="pointer-events-none absolute top-0 left-0 hidden bg-slate-900 text-emerald-400 text-xs px-2 py-1 rounded">
        <span #tooltipTextRef>--</span>
      </div>
      <button (click)="lockValue()" class="absolute bottom-3 right-3 px-3 py-1 bg-emerald-600 text-white rounded">
        Lock: {{ lockedValue() ?? 'None' }}
      </button>
    </div>
  `
})
export class SeniorDepthChartComponent implements AfterViewInit, OnDestroy {
  private readonly ngZone = inject(NgZone);
  private readonly abortController = new AbortController();

  readonly canvasRef = viewChild.required<ElementRef<HTMLCanvasElement>>('canvasRef');
  readonly crosshairRef = viewChild.required<ElementRef<HTMLDivElement>>('crosshairRef');
  readonly tooltipTextRef = viewChild.required<ElementRef<HTMLSpanElement>>('tooltipTextRef');

  readonly lockedValue = signal<number | null>(null);
  private currentValue = 0;

  ngAfterViewInit(): void {
    const canvas = this.canvasRef().nativeElement;
    const crosshair = this.crosshairRef().nativeElement;
    const tooltip = this.tooltipTextRef().nativeElement;

    // Run high-frequency DOM listeners outside Angular zone to avoid triggering change detection
    this.ngZone.runOutsideAngular(() => {
      canvas.addEventListener('mousemove', (event: MouseEvent) => {
        const rect = canvas.getBoundingClientRect();
        const x = event.clientX - rect.left;
        const y = event.clientY - rect.top;
        this.currentValue = Math.round(x * 10);

        crosshair.style.transform = `translate3d(${x}px, ${y}px, 0)`;
        tooltip.textContent = `Val: ${this.currentValue}`;
      }, { signal: this.abortController.signal, passive: true });
    });
  }

  lockValue(): void {
    this.lockedValue.set(this.currentValue);
  }

  ngOnDestroy(): void {
    this.abortController.abort();
  }
}
