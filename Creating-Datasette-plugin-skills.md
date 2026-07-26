# Creating Datasette plugin skills

- Source: https://claude.ai/share/0a9b369b-f868-4065-91d1-fd646c5db3f4
- Author: Simon
- Created: 2025-12-12
- Messages: 4

---

## Human

Clone simonw/datasette to /tmp and read the plugin docs and create a skill based on those for writing Datasette plugins

---

## Assistant

```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

The network doesn't allow access to github.com. Let me fetch the plugin documentation from Datasette's official docs website instead:
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

---

## Human

Use this instead of

---

## Assistant

I'll use the uploaded zip file instead. Let me extract and explore it.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Now let me read the testing_plugins.rst and the internals documentation:
```
This block is not supported on your current device yet.
```

Now let me check the plugins.rst for more information on installation and configuration:
```
This block is not supported on your current device yet.
```

Now let me view more of the plugin hooks to get a complete list:
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Now let me look at the skill-creator skill file to understand the expected format:
```
This block is not supported on your current device yet.
```

Now let me look at one of the existing public skills to understand the format better:
```
This block is not supported on your current device yet.
```

Now I have a comprehensive understanding of the Datasette plugin system. Let me create the skill:
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Now let me create the comprehensive hooks reference file:
```
This block is not supported on your current device yet.
```

Now let me create a reference for the internal APIs (Request, Response, Database, Datasette objects):
```
This block is not supported on your current device yet.
```

Now let me create a script that generates a plugin template:
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Now let me copy the skill to the outputs directory:
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Let me test the init script to make sure it works:
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

The skill is complete. Let me present the files:
```
This block is not supported on your current device yet.
```

I've created a comprehensive **datasette-plugins** skill based on the Datasette plugin documentation. The skill includes:

**Structure:**
```
datasette-plugins/
├── SKILL.md                      # Main skill file with quick start and common patterns
├── references/
│   ├── hooks.md                  # Complete reference for all 30+ plugin hooks
│   └── internals.md              # Reference for Request, Response, Database, Datasette APIs
└── scripts/
    └── init_plugin.py            # Script to generate new plugin projects
```

**Key features covered:**

1. **Quick Start** - One-off plugins and installable plugin structure
2. **All Plugin Hooks** - Documented with examples including:
   - Database hooks (`prepare_connection`)
   - Route registration (`register_routes`)
   - Authentication (`actor_from_request`, `permission_resources_sql`)
   - UI customization (`menu_links`, `table_actions`, `render_cell`)
   - Output renderers (`register_output_renderer`)
   - Event tracking (`track_event`, `register_events`)
   - And many more

3. **Internal APIs** - Complete reference for:
   - Request object (args, headers, post_vars, etc.)
   - Response object (html, json, redirect, etc.)
   - Datasette object (database access, permissions, URL building)
   - Database object (execute, execute_write, table_names)

4. **Testing** - Patterns for testing plugins with pytest and pytest-asyncio

5. **Plugin Generator** - The `init_plugin.py` script creates a complete plugin project with pyproject.toml, tests, and starter code
