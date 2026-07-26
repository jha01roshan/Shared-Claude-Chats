# Ash Framework Custom Postgres Indexes

- Source: https://claude.ai/share/ec8b0563-d80b-4882-82e8-5504e3229a17
- Author: Zach
- Created: 2025-06-01
- Messages: 2

---

## Human

Take a look at the docs here: https://hexdocs.pm/ash_postgres/dsl-ashpostgres-datalayer.html

How do I add a custom index to an `Ash.Resource`?

---

## Assistant

```
This block is not supported on your current device yet.
```

Based on the documentation, you can add a custom index to an `Ash.Resource` using the `custom_indexes` section within the `postgres` block. Here's how:

## Basic Syntax

```elixir
defmodule MyApp.MyResource do
  use Ash.Resource,
    data_layer: AshPostgres.DataLayer

  postgres do
    repo MyApp.Repo
    table "my_table"
    
    custom_indexes do
      index [:column1, :column2], unique: true, where: "thing = TRUE"
    end
  end
  
  # ... rest of your resource definition
end
```

## Index Options

The `index` function accepts the following options:

- **fields** - The columns to index (can be atoms, strings, or a list of both)
- **unique** - Whether the index should be unique (default: false)
- **where** - A WHERE clause for partial indexes
- **name** - Custom name for the index
- **concurrently** - Create index concurrently (default: false)
- **using** - Specify index method (e.g., "GIN", "GIST")
- **include** - Additional columns to include in the index
- **nulls_distinct** - Whether nulls are considered distinct (default: true)
- **prefix** - Schema prefix for the index
- **all_tenants?** - Whether to create on all tenant schemas (default: false)

## Examples

```elixir
custom_indexes do
  # Simple index
  index [:email]
  
  # Unique index
  index [:username], unique: true
  
  # Composite index with WHERE clause
  index [:status, :created_at], where: "deleted_at IS NULL"
  
  # GIN index for full-text search
  index [:title, :body], using: "GIN"
  
  # Index with custom name
  index [:organization_id, :active], name: "org_active_idx"
end
```

The documentation notes that you should prefer using `identities` for simple unique constraints, and use `custom_indexes` for more complex indexing scenarios that require additional options like partial indexes, specific index types, or composite indexes with complex conditions.
