import { Component, inject, DestroyRef } from '@angular/core';
import { FormControl, ReactiveFormsModule } from '@angular/forms';
import { HttpClient } from '@angular/common/http';
import { debounceTime, distinctUntilChanged, switchMap, catchError, of } from 'rxjs';
import { takeUntilDestroyed } from '@angular/core/rxjs-interop';

export interface CatalogProduct {
  readonly id: string;
  readonly name: string;
  readonly price: number;
}

@Component({
  selector: 'app-product-search',
  standalone: true,
  imports: [ReactiveFormsModule],
  template: `
    <div class="search-container max-w-xl mx-auto p-4">
      <input 
        [formControl]="searchControl" 
        placeholder="Search catalog items..." 
        class="w-full px-4 py-2 rounded-lg border border-slate-300" />
      
      @if (isLoading) {
        <div class="spinner text-sm text-blue-500 mt-2">Searching catalog...</div>
      }

      <ul class="results-list mt-3 divide-y divide-slate-200">
        @for (item of products; track item.id) {
          <li class="py-2 flex justify-between">
            <span class="font-medium">{{ item.name }}</span>
            <span class="text-slate-600">\${{ item.price }}</span>
          </li>
        } @empty {
          @if (!isLoading && searchControl.value.trim().length > 0) {
            <li class="py-2 text-slate-500">No matching products found.</li>
          }
        }
      </ul>
    </div>
  `
})
export class ProductSearchComponent {
  private readonly http = inject(HttpClient);
  private readonly destroyRef = inject(DestroyRef);

  readonly searchControl = new FormControl('', { nonNullable: true });
  products: CatalogProduct[] = [];
  isLoading = false;

  constructor() {
    this.searchControl.valueChanges.pipe(
      debounceTime(300),
      distinctUntilChanged(),
      switchMap(term => {
        const query = term.trim();
        if (!query) {
          return of([]);
        }
        this.isLoading = true;
        return this.http.get<CatalogProduct[]>(`/api/products/search?q=${encodeURIComponent(query)}`).pipe(
          catchError(err => {
            console.error('Search API failure:', err);
            return of([]);
          })
        );
      }),
      takeUntilDestroyed(this.destroyRef)
    ).subscribe(results => {
      this.products = results;
      this.isLoading = false;
    });
  }
}
