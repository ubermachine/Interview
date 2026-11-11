import { signalStore, withState, withMethods, withComputed, patchState } from '@ngrx/signals';
import { inject, computed } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { rxMethod } from '@ngrx/signals/rxjs-interop';
import { pipe, switchMap, tap } from 'rxjs';

export interface CartItem {
  readonly id: string;
  readonly name: string;
  readonly price: number;
  readonly quantity: number;
}

export interface CartState {
  readonly items: readonly CartItem[];
  readonly isLoading: boolean;
  readonly discountPercent: number;
}

const initialCartState: CartState = {
  items: [
    { id: '1', name: 'Keyboard', price: 1200, quantity: 1 }
  ],
  isLoading: false,
  discountPercent: 10
};

export const CartStore = signalStore(
  { providedIn: 'root' },
  withState(initialCartState),
  // Each state slice is a signal; computed caches its result until an input changes
  withComputed(({ items, discountPercent }) => {
    const subtotal = computed(() =>
      items().reduce((acc, item) => acc + item.price * item.quantity, 0)
    );
    const total = computed(() =>
      subtotal() * (1 - discountPercent() / 100)
    );
    return { subtotal, total };
  }),
  withMethods((store, http = inject(HttpClient)) => ({
    updateQuantity(id: string, qty: number): void {
      patchState(store, state => ({
        items: state.items.map(item => item.id === id ? { ...item, quantity: qty } : item)
      }));
    },
    loadCart: rxMethod<void>(
      pipe(
        tap(() => patchState(store, { isLoading: true })),
        switchMap(() => http.get<CartItem[]>('/api/cart')),
        tap(items => patchState(store, { items, isLoading: false }))
      )
    )
  }))
);
