# Comparing show() and showModal() dialog methods

- Source: https://claude.ai/share/f09065af-01f6-47b3-b8ec-aa228327450b
- Author: Simon
- Created: 2025-03-16
- Messages: 2

---

## Human

Add a UI element to the main page that switches between using show() and showModal() for this demo, leave everything else the same

---

## Assistant

I'll add a UI element to the main page that allows switching between the dialog's `show()` and `showModal()` methods. This will let users compare the differences between these two ways of displaying the dialog.
```
Viewing artifacts created via the Analysis Tool web feature preview isn’t yet supported on mobile.
```



I've added a toggle switch to allow users to switch between `show()` and `showModal()` methods for the dialog element. Here's what I implemented:

1. Added a new "Controls" section with a toggle switch UI element:
   - When unchecked (default): Uses `show()` - Non-modal dialog
   - When checked: Uses `showModal()` - Modal dialog that blocks interaction with the page

2. Added JavaScript functionality to:
   - Track the current dialog mode with a `useModalMode` variable
   - Update the display label when the toggle is changed
   - Use the appropriate method (`show()` or `showModal()`) when displaying the dialog

3. Added styling for the new toggle element with:
   - A slide switch that changes color when activated
   - Clear labeling to indicate the current state
   - A professional appearance that matches the existing design

This toggle lets users experience the difference between the two dialog modes:
- `show()`: Opens a non-modal dialog that allows interaction with the rest of the page
- `showModal()`: Opens a modal dialog that blocks interaction with the page until it's closed

All the existing functionality remains unchanged, including the animations and side panel behavior. Now users can easily compare how these two dialog methods affect user interaction.
