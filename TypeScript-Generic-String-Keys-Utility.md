# TypeScript Generic String Keys Utility

- Source: https://claude.ai/share/a13a101d-61f1-4993-91a2-c086045c461e
- Author: Erwin
- Created: 2025-08-21
- Messages: 4

---

## Human

implement the typescript generic util `StringKeys<U>` that returns all the possible keys `K` of a union type `U` such that `U[K]` is a string and `K` should be present in all members of the union. The goal is to identify all common string keys that can be used as union discriminant.

---

## Assistant

I'll implement a TypeScript utility type `StringKeys<U>` that finds common keys across all union members where the value type is string. This is particularly useful for finding discriminant keys in union types.
```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```

The `StringKeys<U>` utility type works by:

1. **Mapping over keys**: `{[K in keyof U]: U[K] extends string ? K : never}` creates a mapped type where each key K is preserved if `U[K]` is a string, otherwise it becomes `never`.

2. **Extracting values**: `[keyof U]` extracts the values from the mapped type, creating a union of valid keys or `never`.

3. **Intersection constraint**: `& keyof U` ensures that only keys present in ALL union members are included.

Key features:
- **Common keys only**: Only returns keys that exist in every union member
- **String values only**: Only includes keys where the value type is `string`
- **Type safety**: Works with complex nested unions and generic types
- **Discriminant union support**: Perfect for finding valid discriminant keys

The type is especially useful for:
- Identifying discriminant keys in union types
- Building type-safe switch statements
- Creating generic functions that work with union discriminants
- Ensuring exhaustive handling of union types

---

## Human

rename this to `DiscriminantKeys<TUnion>` and also implement `DiscriminantValues<TUnion>` which returns the possible values (union) of the input union's discriminant

---

## Assistant

```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```


```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```


```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```


```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```


```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```


```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```


```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```


```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```


```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```

I've renamed and enhanced the utility types:

1. **`DiscriminantKeys<TUnion>`** - Returns all common string keys that can serve as discriminants
2. **`DiscriminantValues<TUnion>`** - Returns the union of all possible values for those discriminant keys

Key improvements:
- **Better naming**: More descriptive names that clearly indicate their purpose for discriminated unions
- **Complementary utilities**: `DiscriminantKeys` finds the keys, `DiscriminantValues` finds all possible values
- **Enhanced examples**: Added advanced usage with type-safe exhaustive matching
- **Type safety**: The `DiscriminantMatcher` type ensures all possible discriminant values are handled

The `DiscriminantValues<TUnion>` utility works by:
- Using `DiscriminantKeys<TUnion>` to get the valid discriminant keys
- Accessing `TUnion[DiscriminantKeys<TUnion>]` to get the union of all values for those keys

This combination is particularly powerful for building type-safe handlers that must exhaustively handle all cases in a discriminated union.
