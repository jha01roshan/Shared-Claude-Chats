# Datasette S3 upload plugin development

- Source: https://claude.ai/share/df9258e7-97ba-4362-83da-76d31d96196f
- Author: Simon
- Created: 2026-01-27
- Messages: 2

---

## Human

I want to build a Datasette plugin that offers a UI to upload files to an S3 bucket and stores information about them in a SQLite table. Break this down into ten tasks suitable for execution by parallel coding agents.

---

## Assistant

Here are ten parallelizable tasks for building your Datasette S3 upload plugin:

---

**Task 1: Plugin Scaffolding & Configuration**
Create the core plugin structure with `setup.py`/`pyproject.toml`, register Datasette hooks, and implement configuration loading (S3 bucket name, region, credentials from environment variables or datasette metadata). Define the configuration schema and validation.

**Task 2: SQLite Schema & Database Layer**
Design and implement the SQLite table schema for tracking uploads (fields: id, filename, s3_key, content_type, size_bytes, uploaded_at, uploaded_by, metadata JSON). Create a Python module with async functions for CRUD operations using Datasette's database API.

**Task 3: S3 Client Wrapper**
Build an async S3 client wrapper using `aiobotocore` or `boto3` with sync-to-async. Implement methods: `upload_file()`, `delete_file()`, `generate_presigned_url()`, `check_bucket_exists()`. Handle connection pooling and error translation to custom exceptions.

**Task 4: File Upload API Endpoint**
Create the POST endpoint (`/-/s3-upload/upload`) that accepts multipart file uploads, validates file types/sizes against configurable limits, calls the S3 client, records metadata in SQLite, and returns JSON with upload status and file details.

**Task 5: Upload UI Component**
Build the HTML/JavaScript upload interface with drag-and-drop support, progress indicators, multiple file selection, and client-side validation. Use vanilla JS or minimal dependencies. Emit custom events for integration with the file list.

**Task 6: File Listing UI & Template**
Create the main plugin page template (`/-/s3-upload`) showing uploaded files in a table with sorting/filtering. Display filename, size, upload date, and action buttons. Use Datasette's template system and CSS conventions.

**Task 7: File Download & Presigned URL Handler**
Implement the download endpoint (`/-/s3-upload/download/<id>`) that looks up the file record, generates a time-limited presigned S3 URL, and redirects the user. Include optional inline viewing for images/PDFs via content-disposition.

**Task 8: File Deletion Flow**
Create the delete endpoint (`/-/s3-upload/delete/<id>`) with confirmation UI, permission checking, S3 object deletion, and database record removal. Handle partial failures gracefully (S3 succeeds but DB fails, or vice versa).

**Task 9: Permission & Authentication Integration**
Implement Datasette actor-based permissions: define permission checks for upload, download, delete, and list actions. Create the `permission_allowed` hook implementation. Document how it integrates with datasette-auth-* plugins.

**Task 10: Test Suite & Fixtures**
Build pytest fixtures using `moto` for S3 mocking and Datasette's test client. Write tests covering: successful uploads, size limit rejection, invalid file types, S3 errors, database constraints, permission denials, and concurrent uploads.

---

**Interface contracts for parallel work:**

| Boundary | Contract |
|----------|----------|
| Task 2 ↔ Tasks 4,7,8 | DB functions: `record_upload()`, `get_upload()`, `delete_upload()`, `list_uploads()` |
| Task 3 ↔ Tasks 4,7,8 | S3 client: `S3Client.upload()`, `.delete()`, `.presign()` |
| Task 1 ↔ All | Config object: `PluginConfig.bucket`, `.region`, `.max_size`, `.allowed_types` |
| Task 9 ↔ Tasks 4,6,7,8 | Permission helper: `await can_upload(actor)`, `can_delete(actor, upload)` |
