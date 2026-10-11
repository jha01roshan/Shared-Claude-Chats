# Session Log

Running summary of work done in this project. Newest entries go at the bottom.
Read this file before starting new work, since other IDEs may have changed the project.

| Model | Date | Ask | Approach | What was accomplished |
|---|---|---|---|---|
| Claude (session model) | 2026-10-11 | Save incoming images and PDFs for the next 5 days (2026-10-11 to 2026-10-15), without processing them. | Created a `saved_files/` folder for incoming files and this log. Files are saved as-is with no conversion or analysis. | Created `saved_files/` (with `.gitkeep`) and `log.md`. Set up the 5-day save window. No files had been uploaded yet at the time of this entry. |
| Claude (session model) | 2026-10-11 | Save the hotel receipt image (in-room dining bill, room 422) sent in chat. | Tried to copy the uploaded image into `saved_files/`. The copy was blocked by a permission check on the upload source, so nothing was saved. | Image not saved yet. Waiting for the user to approve the copy or re-send the image. |
