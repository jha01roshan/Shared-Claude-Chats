# Vector slice range panic behavior

- Source: https://claude.ai/share/053d6a95-176f-4961-8b8e-8bf870721c8f
- Author: Lexe
- Created: 2026-02-20
- Messages: 2

---

## Human

fn main() {
   // Will this panic or not?
   let s : Vec<u8> = vec![0u8; 32];
   println!("{:?}", &s[1..=0]);
}

---

## Assistant

This will **not panic** — it prints `[]`.

The range `1..=0` is an empty range (since the end is less than the start in an inclusive range). Rust's slice indexing accepts empty ranges like this as long as the bounds are within the valid index range for the slice, and `1` is a valid index into a 32-element vector.

If you tried `1..=0` on an empty vector or `33..=32` (out of bounds), *that* would panic. But here, `1` is within bounds, so Rust happily returns an empty slice.

You can verify:
```rust
fn main() {
    let s: Vec<u8> = vec![0u8; 32];
    println!("{:?}", &s[1..=0]); // prints: []
}
```

Interestingly, `0..0` (exclusive) also gives `[]`, but `2..=1` would also work fine for the same reason — the bounds are checked individually against the slice length, not against each other.
