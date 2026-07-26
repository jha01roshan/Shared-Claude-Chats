# macOS screensaver shuffle script for multiple displays

- Source: https://claude.ai/share/34c08ed8-c162-4047-a61d-c38ca83f743a
- Author: Rob
- Created: 2026-01-05
- Messages: 26

---

## Human

This script changes the screen saver shuffle time on macOS Tahoe:

tell application "System Settings" activate reveal pane id "com.apple.Wallpaper-Settings.extension" delay 2 end tell tell application "System Events" tell process "System Settings" -- Click the Shuffle popup button click pop up button "Shuffle" of group 1 of scroll area 1 of group 1 of group 3 of splitter group 1 of group 1 of window 1 delay 0.5 -- Select your desired interval (change this line to your preference) click menu item "Every 15 Minutes" of menu 1 of pop up button "Shuffle" of group 1 of scroll area 1 of group 1 of group 3 of splitter group 1 of group 1 of window 1 end tell end tell tell application "System Settings" to quit

But I have a multi-display setup, and I need to set it for each display, so I also need to click the display button right below the display thumbnail, as seen in the screenshot. Can you write a script that clicks that button and sets it to "PA27JCV"?

---

## Assistant

I'll help you create a script that clicks the display selector and chooses "PA27JCV". Here's the AppleScript:

```applescript
tell application "System Settings"
    activate
    reveal pane id "com.apple.Wallpaper-Settings.extension"
    delay 2
end tell

tell application "System Events"
    tell process "System Settings"
        -- Click the display selector dropdown (Built-in Display)
        click pop up button 1 of group 1 of scroll area 1 of group 1 of group 3 of splitter group 1 of group 1 of window 1
        delay 0.5
        
        -- Select PA27JCV from the menu
        click menu item "PA27JCV" of menu 1 of pop up button 1 of group 1 of scroll area 1 of group 1 of group 3 of splitter group 1 of group 1 of window 1
        delay 1
        
        -- Now set the shuffle time for this display
        click pop up button "Shuffle" of group 1 of scroll area 1 of group 1 of group 3 of splitter group 1 of group 1 of window 1
        delay 0.5
        
        click menu item "Every 15 Minutes" of menu 1 of pop up button "Shuffle" of group 1 of scroll area 1 of group 1 of group 3 of splitter group 1 of group 1 of window 1
    end tell
end tell

tell application "System Settings" to quit
```

This script:
1. Opens System Settings to the Wallpaper pane
2. Clicks the first pop up button (the display selector showing "Built-in Display")
3. Selects "PA27JCV" from the menu
4. Waits for the interface to update
5. Clicks the Shuffle popup and sets it to "Every 15 Minutes"
6. Quits System Settings

You can adjust the shuffle interval in the last `click menu item` line to whatever you prefer.

---

## Human

That seems to click the upper right button, which contains the fill screen options.

---

## Assistant

Ah, I see! Let me correct that. The display selector dropdown is below the thumbnail preview. Here's the updated script:

```applescript
tell application "System Settings"
    activate
    reveal pane id "com.apple.Wallpaper-Settings.extension"
    delay 2
end tell

tell application "System Events"
    tell process "System Settings"
        -- Click the display selector dropdown (the one showing "Built-in Display")
        click pop up button "Built-in Display" of group 1 of scroll area 1 of group 1 of group 3 of splitter group 1 of group 1 of window 1
        delay 0.5
        
        -- Select PA27JCV from the menu
        click menu item "PA27JCV" of menu 1 of pop up button "Built-in Display" of group 1 of scroll area 1 of group 1 of group 3 of splitter group 1 of group 1 of window 1
        delay 1
        
        -- Now set the shuffle time for this display
        click pop up button "Shuffle" of group 1 of scroll area 1 of group 1 of group 3 of splitter group 1 of group 1 of window 1
        delay 0.5
        
        click menu item "Every 15 Minutes" of menu 1 of pop up button "Shuffle" of group 1 of scroll area 1 of group 1 of group 3 of splitter group 1 of group 1 of window 1
    end tell
end tell

tell application "System Settings" to quit
```

The key change is referencing the pop up button by its name "Built-in Display" which should target the correct dropdown below the thumbnail.

---

## Human

error: System Events got an error: Can’t get pop up button "Built-in Display" of group 1 of scroll area 1 of group 1 of group 3 of splitter group 1 of group 1 of window 1 of process "System Settings".

---

## Assistant

Let me help you identify the correct UI element path. Can you run this diagnostic script to see the structure of the UI elements?

```applescript
tell application "System Settings"
    activate
    reveal pane id "com.apple.Wallpaper-Settings.extension"
    delay 2
end tell

tell application "System Events"
    tell process "System Settings"
        -- Get all pop up buttons in the main group
        set allPopUps to every pop up button of group 1 of scroll area 1 of group 1 of group 3 of splitter group 1 of group 1 of window 1
        
        repeat with aPopUp in allPopUps
            try
                log "Pop up button: " & (name of aPopUp) & " - " & (description of aPopUp)
            end try
        end repeat
        
        -- Also check for all UI elements to see the structure
        set allElements to every UI element of group 1 of scroll area 1 of group 1 of group 3 of splitter group 1 of group 1 of window 1
        
        repeat with anElement in allElements
            try
                log "Element: " & (class of anElement) & " - " & (name of anElement)
            end try
        end repeat
    end tell
end tell
```

Run this and check the Messages/Log in Script Editor. This will show us all the pop up buttons and UI elements so we can identify the correct one for the display selector. Share the output and I'll help you build the correct script.

---

## Human

Nothing appears in output

---

## Assistant

Let's try a simpler approach to see what's available:

```applescript
tell application "System Settings"
    activate
    reveal pane id "com.apple.Wallpaper-Settings.extension"
    delay 2
end tell

tell application "System Events"
    tell process "System Settings"
        -- Get the entire UI element tree
        tell group 1 of scroll area 1 of group 1 of group 3 of splitter group 1 of group 1 of window 1
            return entire contents
        end tell
    end tell
end tell
```

This should return a large list of all UI elements. Copy and paste the output here so we can find the display selector button in the hierarchy.

Alternatively, you could use UI Browser or Accessibility Inspector (part of Xcode) to inspect the exact UI element path for that "Built-in Display" dropdown button.

---

## Human

{static text "Eleuthera 2023" of group 1 of scroll area 1 of group 1 of group 3 of splitter group 1 of group 1 of window "Wallpaper" of application process "System Settings" of application "System Events", pop up button "Eleuthera 2023" of group 1 of scroll area 1 of group 1 of group 3 of splitter group 1 of group 1 of window "Wallpaper" of application process "System Settings" of application "System Events", static text "Shuffle" of group 1 of scroll area 1 of group 1 of group 3 of splitter group 1 of group 1 of window "Wallpaper" of application process "System Settings" of application "System Events", pop up button "Shuffle" of group 1 of scroll area 1 of group 1 of group 3 of splitter group 1 of group 1 of window "Wallpaper" of application process "System Settings" of application "System Events", checkbox "Shuffle" of group 1 of scroll area 1 of group 1 of group 3 of splitter group 1 of group 1 of window "Wallpaper" of application process "System Settings" of application "System Events", static text "Show on all Spaces" of group 1 of scroll area 1 of group 1 of group 3 of splitter group 1 of group 1 of window "Wallpaper" of application process "System Settings" of application "System Events", checkbox "Show on all Spaces" of group 1 of scroll area 1 of group 1 of group 3 of splitter group 1 of group 1 of window "Wallpaper" of application process "System Settings" of application "System Events"}

---

## Assistant

I don't see the display selector in that output. It's possible it's in a different part of the UI hierarchy. Let me try checking the groups more broadly:

```applescript
tell application "System Settings"
    activate
    reveal pane id "com.apple.Wallpaper-Settings.extension"
    delay 2
end tell

tell application "System Events"
    tell process "System Settings"
        -- Check all groups in the scroll area
        set allGroups to every group of scroll area 1 of group 1 of group 3 of splitter group 1 of group 1 of window 1
        
        repeat with i from 1 to count of allGroups
            try
                set groupContents to entire contents of item i of allGroups
                return "Group " & i & ": " & groupContents
            end try
        end repeat
    end tell
end tell
```

Or alternatively, let's check if the display selector might be in a different location entirely:

```applescript
tell application "System Settings"
    activate
    reveal pane id "com.apple.Wallpaper-Settings.extension"
    delay 2
end tell

tell application "System Events"
    tell process "System Settings"
        -- Get all pop up buttons in the entire window
        set allPopUps to every pop up button of window 1
        
        repeat with aPopUp in allPopUps
            try
                log "Pop up: " & (value of aPopUp)
            end try
        end repeat
    end tell
end tell
```

Run one of these and share the output - we need to find where that "Built-in Display" dropdown actually lives in the UI hierarchy.

---

## Human

no output from either script

---

## Assistant

Let's try a different approach - let's get the entire window structure:

```applescript
tell application "System Settings"
    activate
    reveal pane id "com.apple.Wallpaper-Settings.extension"
    delay 2
end tell

tell application "System Events"
    tell process "System Settings"
        return entire contents of window 1
    end tell
end tell
```

This will give us everything in the window. It might be a very long output, but we should be able to find the display selector in there. 

If that doesn't work, can you try clicking on the "Built-in Display" dropdown manually, and then while the menu is open, run this:

```applescript
tell application "System Events"
    tell process "System Settings"
        return entire contents of window 1
    end tell
end tell
```

The open menu might make the element more visible in the hierarchy.

---

## Human

_[empty message]_

---

## Assistant

Perfect! Now I can see the structure. The display selector is `pop up button 1` in the group at the top. Here's the corrected script:

```applescript
tell application "System Settings"
    activate
    reveal pane id "com.apple.Wallpaper-Settings.extension"
    delay 2
end tell

tell application "System Events"
    tell process "System Settings"
        -- Click the display selector dropdown (the first pop up button)
        click pop up button 1 of group 1 of group 3 of splitter group 1 of group 1 of window 1
        delay 0.5
        
        -- Select PA27JCV from the menu
        click menu item "PA27JCV" of menu 1 of pop up button 1 of group 1 of group 3 of splitter group 1 of group 1 of window 1
        delay 1
        
        -- Now set the shuffle time for this display
        click pop up button "Shuffle" of group 1 of scroll area 1 of group 1 of group 3 of splitter group 1 of group 1 of window 1
        delay 0.5
        
        click menu item "Every 15 Minutes" of menu 1 of pop up button "Shuffle" of group 1 of scroll area 1 of group 1 of group 3 of splitter group 1 of group 1 of window 1
    end tell
end tell

tell application "System Settings" to quit
```

This should now click the correct dropdown (the one showing "Built-in Display" in your screenshot) and select "PA27JCV" from it.

---

## Human

The menu pops up now (nice work!), but when it tries to set the display, I get: System Events got an error: Can’t get group 1 of window 1 of process "System Settings". Invalid index.

---

## Assistant

The menu is still open when it's trying to access the next element. Let's add a longer delay and also ensure the menu closes before continuing:

```applescript
tell application "System Settings"
    activate
    reveal pane id "com.apple.Wallpaper-Settings.extension"
    delay 2
end tell

tell application "System Events"
    tell process "System Settings"
        -- Click the display selector dropdown (the first pop up button)
        click pop up button 1 of group 1 of group 3 of splitter group 1 of group 1 of window 1
        delay 0.5
        
        -- Select PA27JCV from the menu
        click menu item "PA27JCV" of menu 1 of pop up button 1 of group 1 of group 3 of splitter group 1 of group 1 of window 1
        delay 2
        
        -- Now set the shuffle time for this display
        click pop up button "Shuffle" of group 1 of scroll area 1 of group 1 of group 3 of splitter group 1 of group 1 of window 1
        delay 0.5
        
        click menu item "Every 15 Minutes" of menu 1 of pop up button "Shuffle" of group 1 of scroll area 1 of group 1 of group 3 of splitter group 1 of group 1 of window 1
    end tell
end tell

tell application "System Settings" to quit
```

I increased the delay after clicking the menu item from 1 to 2 seconds. This should give the interface more time to update after switching displays.

---

## Human

Same error -- the selector isn't changing in the pop-up, so that step isn't happening.

---

## Assistant

Ah, the menu item click isn't working. Let's check what menu items are actually available. Can you manually click the display dropdown to open it, then run this script while it's open:

```applescript
tell application "System Events"
    tell process "System Settings"
        try
            set menuItems to every menu item of menu 1 of pop up button 1 of group 1 of group 3 of splitter group 1 of group 1 of window 1
            repeat with anItem in menuItems
                log "Menu item: " & (name of anItem)
            end repeat
        end try
    end tell
end tell
```

This will show us the exact names of the menu items so we can use the correct name in the script. The display might have a slightly different name than "PA27JCV" in the menu.

---

## Human

When I click away, the menu vanishes

---

## Assistant

Right, the menu closes when focus changes. Let's try a different approach - we can use keyboard navigation. After clicking the popup, we can use arrow keys to navigate:

```applescript
tell application "System Settings"
    activate
    reveal pane id "com.apple.Wallpaper-Settings.extension"
    delay 2
end tell

tell application "System Events"
    tell process "System Settings"
        -- Click the display selector dropdown
        click pop up button 1 of group 1 of group 3 of splitter group 1 of group 1 of window 1
        delay 0.5
        
        -- Use down arrow to navigate to PA27JCV (adjust the number of key presses as needed)
        key code 125 -- down arrow
        delay 0.2
        
        -- Press return to select
        key code 36 -- return
        delay 2
        
        -- Now set the shuffle time for this display
        click pop up button "Shuffle" of group 1 of scroll area 1 of group 1 of group 3 of splitter group 1 of group 1 of window 1
        delay 0.5
        
        click menu item "Every 15 Minutes" of menu 1 of pop up button "Shuffle" of group 1 of scroll area 1 of group 1 of group 3 of splitter group 1 of group 1 of window 1
    end tell
end tell

tell application "System Settings" to quit
```

If you have more than 2 displays, you'll need to add more `key code 125` lines (one for each down arrow press) to get to PA27JCV. How many displays do you have total?

---

## Human

Instead of arrow keys, how about type-select? Typing a "P" will work - can the script do that?

---

## Assistant

Great idea! Yes, we can use keystroke to type "P" for type-select:

```applescript
tell application "System Settings"
    activate
    reveal pane id "com.apple.Wallpaper-Settings.extension"
    delay 2
end tell

tell application "System Events"
    tell process "System Settings"
        -- Click the display selector dropdown
        click pop up button 1 of group 1 of group 3 of splitter group 1 of group 1 of window 1
        delay 0.5
        
        -- Type "P" to jump to PA27JCV
        keystroke "p"
        delay 0.2
        
        -- Press return to select
        key code 36 -- return
        delay 2
        
        -- Now set the shuffle time for this display
        click pop up button "Shuffle" of group 1 of scroll area 1 of group 1 of group 3 of splitter group 1 of group 1 of window 1
        delay 0.5
        
        click menu item "Every 15 Minutes" of menu 1 of pop up button "Shuffle" of group 1 of scroll area 1 of group 1 of group 3 of splitter group 1 of group 1 of window 1
    end tell
end tell

tell application "System Settings" to quit
```

This should open the menu, type "P" to jump to PA27JCV, then press return to select it.

---

## Human

Perfect! And once it's selected, can you return/get the menu item's name, so we know what it is?

---

## Assistant

Yes! Here's the modified script that will return the selected display name:

```applescript
tell application "System Settings"
    activate
    reveal pane id "com.apple.Wallpaper-Settings.extension"
    delay 2
end tell

tell application "System Events"
    tell process "System Settings"
        -- Click the display selector dropdown
        click pop up button 1 of group 1 of group 3 of splitter group 1 of group 1 of window 1
        delay 0.5
        
        -- Type "P" to jump to PA27JCV
        keystroke "p"
        delay 0.2
        
        -- Press return to select
        key code 36 -- return
        delay 2
        
        -- Get the selected display name
        set displayName to value of pop up button 1 of group 1 of group 3 of splitter group 1 of group 1 of window 1
        
        -- Now set the shuffle time for this display
        click pop up button "Shuffle" of group 1 of scroll area 1 of group 1 of group 3 of splitter group 1 of group 1 of window 1
        delay 0.5
        
        click menu item "Every 15 Minutes" of menu 1 of pop up button "Shuffle" of group 1 of scroll area 1 of group 1 of group 3 of splitter group 1 of group 1 of window 1
    end tell
end tell

tell application "System Settings" to quit

return displayName
```

This will return the name of the selected display at the end. The result should appear in the Script Editor's Result pane.

---

## Human

"PA27JCV"

So that other version should have worked, right?

---

## Assistant

You're absolutely right - theoretically it should have worked! The menu item name is exactly "PA27JCV" as we tried originally. 

Sometimes AppleScript has timing issues where it tries to interact with menu items before they're fully ready, or the menu hierarchy is slightly different when it's open. The keystroke method is more reliable because it mimics what a user would do.

But yes, this *should* have worked:
```applescript
click menu item "PA27JCV" of menu 1 of pop up button 1 of group 1 of group 3 of splitter group 1 of group 1 of window 1
```

It's one of those quirks of UI scripting where the keyboard approach ends up being more dependable than direct menu item clicks, even when the reference is correct. The keystroke method is actually a good general pattern for popup menus in System Settings - they can be finicky with direct clicks.
