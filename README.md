# Gechsort
## Gechsort loves permutations.

### Algorithm (pseudo):
```rust
f(data: list)
  (min, mid, max, sort) := min_of(data), mid_of(data), max_of(data), sort(data)
  (permutations, generated)  := p(elements), empty([])
  
  for per arr in permutations :=
    if first_of(arr) == min and last_of(arr) == max and mid_of(arr) == mid :=
      append(generated, arr)
    =:
  =:
  
  for per arr in generated := 
    if arr == sort :=
      return arr
    =:
  =:
```

### Gechsort licensed under the terms of MIT License.
