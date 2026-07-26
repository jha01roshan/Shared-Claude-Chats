# Starlette 1.0 skill document with code examples

- Source: https://claude.ai/share/b537c340-aea7-49d6-a14d-3134aa1bd957
- Author: Simon
- Created: 2026-03-22
- Messages: 4

---

## Human

Clone Starlette from GitHub - it just had its 1.0 release. Build a skill markdown document for this release which includes code examples of every feature.

---

## Assistant

I'll clone Starlette from GitHub and build a comprehensive skill document. Let me start by reading the skill-creator guide and then cloning the repo.
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

Now let me read through all the documentation files to capture every feature:
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

Now I have a thorough understanding of the entire codebase. Let me build the comprehensive skill document.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

The Starlette 1.0 SKILL.md is ready. Here's what it covers across 20 sections, each with working code examples:

1. **Application** — `Starlette` class, constructor params, state, pure ASGI toolkit usage
2. **Routing** — `Route`, `Mount`, `Host`, `WebSocketRoute`, path params, convertors, custom convertors, reverse URLs, host-based routing, route priority, `Router`
3. **Requests** — Method, URL, headers, query params, path params, client address, cookies, body (bytes/json/form/stream), file uploads, `UploadFile`, disconnect detection
4. **Responses** — `Response`, `PlainText`, `HTML`, `JSON`, `Redirect`, `Streaming`, `FileResponse` (with range requests), custom JSON (orjson), cookies
5. **WebSockets** — Send/receive text/bytes/json, iteration, close, denial responses, `HTTPException` in WS
6. **Class-Based Endpoints** — `HTTPEndpoint`, `WebSocketEndpoint`
7. **Middleware** — All built-in middleware (CORS, Session, HTTPS Redirect, Trusted Host, GZip), `BaseHTTPMiddleware`, pure ASGI middleware, route-level middleware
8. **Lifespan** — Async context manager, typed state with `TypedDict`, dict-style access
9. **Background Tasks** — `BackgroundTask`, `BackgroundTasks`
10. **Templates** — Jinja2, custom env, autoescape, filters, context processors, testing
11. **Static Files** — Directory, packages, HTML mode
12. **Exception Handling** — Status code handlers, class handlers, `HTTPException`, `WebSocketException`
13. **Authentication** — `AuthenticationBackend`, `@requires` decorator, scopes, custom error
14. **Configuration** — `Config`, `.env` files, `Secret`, `CommaSeparatedStrings`, prefixed vars
15. **Test Client** — HTTP, WebSocket testing, async testing with `httpx.AsyncClient`
16. **Schema Generation** — OpenAPI via `SchemaGenerator`
17. **Data Structures** — `URL`, `Headers`, `QueryParams`, `State`, `Secret`
18. **Thread Pool** — Sync endpoint handling, configuring `anyio` token limits
19. **Status Codes** — HTTP and WebSocket status constants
20. **Complete Application Example** — Full app combining all features

It also includes a **migration table** listing every API removed in 1.0 and its replacement.

---

## Human

Continue

---

## Assistant

```
This block is not supported on your current device yet.
```

Here's your Starlette 1.0 skill document — ready to download and use.
