import { Component, signal, computed, ChangeDetectionStrategy } from '@angular/core';

export interface CartItem {
  readonly id: string;
  readonly name: string;
  readonly price: number;
  readonly quantity: number;
}

@Component({
  selector: 'app-senior-cart',
  standalone: true,
  changeDetection: ChangeDetectionStrategy.OnPush,
  template: `
    <div class="cart-container p-6 bg-slate-900 text-white rounded-xl shadow-xl">
      <h2 class="text-2xl font-bold mb-4">Cart Summary</h2>

      <div class="space-y-3">
        @for (item of items(); track item.id) {
          <div class="flex items-center justify-between p-3 bg-slate-800 rounded-lg">
            <div>
              <p class="font-medium">{{ item.name }}</p>
              <p class="text-sm text-slate-400">₹{{ item.price }} x {{ item.quantity }}</p>
            </div>
            
            <div class="flex items-center gap-2">
              <button 
                (click)="updateQuantity(item.id, -1)" 
                [disabled]="item.quantity <= 1"
                class="px-2 py-1 bg-slate-700 rounded hover:bg-slate-600 disabled:opacity-40"
                aria-label="Decrease quantity">-</button>
              <span class="w-8 text-center font-bold">{{ item.quantity }}</span>
              <button 
                (click)="updateQuantity(item.id, 1)" 
                class="px-2 py-1 bg-blue-600 rounded hover:bg-blue-500"
                aria-label="Increase quantity">+</button>
            </div>
          </div>
        }
      </div>

      <div class="mt-6 border-t border-slate-700 pt-4 space-y-2 text-sm">
        <div class="flex justify-between">
          <span class="text-slate-400">Subtotal:</span>
          <span>₹{{ subtotal() }}</span>
        </div>
        <div class="flex justify-between">
          <span class="text-slate-400">GST (18%):</span>
          <span>₹{{ gstAmount().toFixed(2) }}</span>
        </div>
        <div class="flex justify-between">
          <span class="text-slate-400">Shipping:</span>
          <span [class.text-emerald-400]="isFreeDelivery()">
            {{ isFreeDelivery() ? 'FREE' : '₹50' }}
          </span>
        </div>
        @if (!isFreeDelivery()) {
          <p class="text-xs text-amber-400">
            Add ₹{{ freeDeliveryShortfall() }} more for FREE delivery!
          </p>
        }
        <div class="flex justify-between text-lg font-bold border-t border-slate-700 pt-2 text-emerald-400">
          <span>Grand Total:</span>
          <span>₹{{ grandTotal().toFixed(2) }}</span>
        </div>
      </div>
    </div>
  `
})
export class SeniorCartComponent {
  readonly items = signal<readonly CartItem[]>([
    { id: 'SKU-001', name: 'ANC Headphones', price: 29990, quantity: 1 },
    { id: 'SKU-002', name: '20W USB-C Charger', price: 1900, quantity: 2 }
  ]);

  readonly subtotal = computed(() =>
    this.items().reduce((sum, item) => sum + item.price * item.quantity, 0)
  );

  readonly gstAmount = computed(() => this.subtotal() * 0.18);

  readonly isFreeDelivery = computed(() => this.subtotal() >= 500);

  readonly freeDeliveryShortfall = computed(() => 
    this.isFreeDelivery() ? 0 : 500 - this.subtotal()
  );

  readonly shippingCost = computed(() => (this.isFreeDelivery() ? 0 : 50));

  readonly grandTotal = computed(() => 
    this.subtotal() + this.gstAmount() + this.shippingCost()
  );

  updateQuantity(id: string, delta: number): void {
    this.items.update(currentItems =>
      currentItems.map(item => {
        if (item.id === id) {
          const newQty = Math.max(1, item.quantity + delta);
          return { ...item, quantity: newQty };
        }
        return item;
      })
    );
  }
}
