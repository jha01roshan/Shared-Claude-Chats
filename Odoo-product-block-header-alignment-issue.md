# Odoo product block header alignment issue

- Source: https://claude.ai/share/91965e93-e9b9-4873-a8f9-8547b487e09f
- Author: Aaron
- Created: 2025-11-11
- Messages: 16

---

## Human

I'm working on a website that's build on Odoo Web builder and I'm using the Product block on my website. However, there's a problem where I can't make the header for the Product center align

---

## Assistant

I can help you with centering the header alignment in Odoo's Product block. This is a common formatting issue in Odoo's website builder.

Here are a few approaches to fix this:

## Option 1: Using the Built-in Alignment Tools
1. Click on the Product block header to select it
2. Look for the alignment options in the toolbar that appears (usually shows left/center/right alignment icons)
3. Click the center alignment button

## Option 2: Using the HTML/CSS Editor
If the visual editor isn't working, you can add custom CSS:

1. Go to **Website > Configuration > Settings**
2. Enable **Custom HTML/CSS** if it's not already enabled
3. Go to **Website > Site > HTML/CSS Editor** (or access it through Customize menu)
4. Add this custom CSS:

```css
.s_product_catalog h2,
.s_product_catalog .h2,
.o_wsale_products_main_row h2 {
    text-align: center !important;
}
```

## Option 3: Direct HTML Editing
1. Click **Edit** on your webpage
2. Click on the Product block
3. Click the **< >** (HTML) icon in the toolbar
4. Find the header element and add `style="text-align: center;"` or add the class `text-center`

**Which Odoo version are you using?** The exact steps can vary slightly between versions (Odoo 14, 15, 16, 17, etc.). Also, could you clarify what you mean by "Product block header" - is it the section title above the products, or the individual product names?

---

## Human

Option1 doesn't work. How do I enable Custom HTML/CSS? I don't see that option?

---

## Assistant

The location of the Custom HTML/CSS option varies depending on your Odoo version. Let me guide you through finding it:

## For Odoo 15, 16, 17+:

1. Go to **Website** app (main dashboard)
2. Click on **Configuration** in the top menu
3. Click on **Settings**
4. Scroll down to the **SEO** or **Advanced** section
5. Look for a checkbox that says **"Custom Code"** or **"HTML/CSS Editor"**
6. Enable it and click **Save**

## If you still can't find it:

**Check your user permissions** - You need administrator access to see this option. Make sure you're logged in as an admin user.

## Alternative: Direct CSS injection without enabling the setting

If you can't find or enable that option, you can still add custom CSS directly:

1. Go to your website in **Edit mode**
2. Click **Customize** in the top right
3. Look for **"Add a Custom Code"** or **"</> HTML/CSS"** option in the customize menu
4. Add your CSS code there

## Quick workaround using Odoo's Style Editor:

1. Click **Edit** on your page
2. Click on the Product block section (the entire block, not just the header)
3. Look for the **paint brush icon** or **"Customize"** option
4. Sometimes there's a **"Layout"** or **"Design"** tab where you can adjust alignment

**What version of Odoo are you using?** (You can check this in the bottom right corner or in Settings). This will help me give you more specific instructions.

---

## Human

I'm using version 18

---

## Assistant

_[empty message]_

---

## Human

I'm using versino 18

---

## Assistant

Great! For **Odoo 18**, here's how to add custom CSS:

## Method 1: Using the Theme Editor (Easiest for Odoo 18)

1. Go to your **Website** (frontend)
2. Click **Edit** in the top right
3. Click the **Customize** menu (top right, next to Edit)
4. Scroll down and look for **"</> Custom Code"** or **"Custom CSS/JS"**
5. Click on it and you should see options to add Custom CSS
6. Add this code:

```css
.s_products h2,
.s_products .s_products_item h2,
.o_wsale_products_main_row h2 {
    text-align: center !important;
}
```

## Method 2: Direct Block Styling (If Method 1 doesn't work)

1. Click **Edit** on your page
2. Click on the **Product block** itself (the container, not just the header)
3. Click the **"< >"** icon in the floating toolbar (this opens the HTML editor)
4. Find the header tag (likely `<h2>` or similar) and modify it to include:
   ```html
   <h2 class="text-center">Your Header Text</h2>
   ```
   or
   ```html
   <h2 style="text-align: center;">Your Header Text</h2>
   ```

## Method 3: Using Inspect Element (Quick Test)

Before adding permanent CSS, let's test if this will work:
1. Right-click on the header
2. Select **Inspect** (or Inspect Element)
3. In the Styles panel, add `text-align: center;` to see if it works
4. If it works, we'll make it permanent using one of the methods above

**Can you tell me specifically which header you're trying to center?** Is it:
- The section title above all products?
- Individual product names?
- A custom header you added?

This will help me give you the exact CSS selector to use.

---

## Human

I cna inject code in the <head> <body> from the theme, not for specifc block

---

## Assistant

Perfect! Since you can inject code in the `<head>` or `<body>` from the theme, here's what you need to do:

## Add CSS to the `<head>` section:

1. Go to **Website → Configuration → Settings**
2. Scroll to find the section where you can add custom code to `<head>`
3. Add this CSS code wrapped in `<style>` tags:

```html
<style>
.s_products h2,
.s_products .h2,
.s_products_item h2,
.o_wsale_products_main_row h2,
.s_dynamic_snippet_products h2 {
    text-align: center !important;
}
</style>
```

## OR if you need to be more specific:

If the above centers too many things, you can target just the main product section header:

```html
<style>
.s_products > .container > h2,
.s_products > .container > .row > .col > h2 {
    text-align: center !important;
}
</style>
```

Save the settings and refresh your page to see the changes.

**Still not working?** 

If it's still not centering, I'll need to know the specific class or ID of the header element. Can you:
1. Right-click on the header you want to center
2. Select **Inspect** 
3. Copy the HTML code of that header element and share it with me?

This way I can give you the exact CSS selector that will work for your specific case.

---

## Human

I need the <h4> element to be centered relative to the entire section


Here's the XPath
//*[@id="wrap"]/section/div/div/section[1]

<section class="s_dynamic_snippet_title oe_unremovable oe_unmovable d-flex flex-column flex-md-row mb-lg-0 pb-3 pb-md-0 o_colored_level justify-content-between">
                        <div>
                            <h4 style="text-align: center;">Our latest content</h4></div>
                        <div>
                            <a class="s_dynamic_snippet_main_page_url" href="/shop" data-bs-original-title="See All">See all <i class="fa fa-long-arrow-right ms-2"></i></a>
                        </div>
                    </section>

---

## Assistant

Ah, I see the issue! The `<h4>` has `text-align: center;` but it's only centering within its parent `<div>`, not across the entire section. The section is using flexbox with `justify-content-between`, which pushes the two divs to opposite sides.

## Add this CSS to your `<head>`:

```html
<style>
.s_dynamic_snippet_title.justify-content-between {
    justify-content: center !important;
}

.s_dynamic_snippet_title > div:first-child {
    flex: 1;
    text-align: center;
}

.s_dynamic_snippet_title > div:last-child {
    position: absolute;
    right: 0;
}
</style>
```

This will:
- Center the header across the full section width
- Keep the "See all" link positioned on the right

## Alternative (if you want everything centered):

If you want both the header AND the "See all" link centered:

```html
<style>
.s_dynamic_snippet_title.justify-content-between {
    justify-content: center !important;
    text-align: center;
}

.s_dynamic_snippet_title > div {
    margin: 0 auto;
}
</style>
```

Try the first option first - it should give you a centered header with the "See all" link still on the right side. Let me know if you need any adjustments!

---

## Human

The following works. can we make the CSS as specific as possible so that it doesn't affect other components
<style> .s_dynamic_snippet_title.justify-content-between { justify-content: center !important; } .s_dynamic_snippet_title > div:first-child { flex: 1; text-align: center; } .s_dynamic_snippet_title > div:last-child { position: absolute; right: 0; } </style>

---

## Assistant

Great! Here's a more specific version that targets only that exact section. You can make it specific in a few ways:

## Option 1: Target only within the Product dynamic snippet section

```html
<style>
.s_dynamic_snippet_products .s_dynamic_snippet_title.justify-content-between {
    justify-content: center !important;
}

.s_dynamic_snippet_products .s_dynamic_snippet_title > div:first-child {
    flex: 1;
    text-align: center;
}

.s_dynamic_snippet_products .s_dynamic_snippet_title > div:last-child {
    position: absolute;
    right: 0;
}
</style>
```

## Option 2: Add a custom class to that specific section

1. In Edit mode, click on that section
2. Click the **"< >"** HTML editor icon
3. Add a custom class to the section, like `custom-centered-title`:
   ```html
   <section class="s_dynamic_snippet_title oe_unremovable oe_unmovable d-flex flex-column flex-md-row mb-lg-0 pb-3 pb-md-0 o_colored_level justify-content-between custom-centered-title">
   ```

4. Then use this CSS:
```html
<style>
.s_dynamic_snippet_title.custom-centered-title.justify-content-between {
    justify-content: center !important;
}

.s_dynamic_snippet_title.custom-centered-title > div:first-child {
    flex: 1;
    text-align: center;
}

.s_dynamic_snippet_title.custom-centered-title > div:last-child {
    position: absolute;
    right: 0;
}
</style>
```

**Option 1 is easier** and will apply to all product dynamic snippets on your site. **Option 2 is most specific** and will only affect that exact section with the custom class.

Which approach works best for your needs?

---

## Human

Do these changes persist on Odoo upgrade?

---

## Assistant

Good question! Here's what you need to know about persistence during Odoo upgrades:

## Custom Code in Theme Settings: **Generally Persists** ✅

Code added through **Website → Configuration → Settings** in the `<head>` or `<body>` sections typically **persists through upgrades** because:
- It's stored in your database, not in Odoo's core files
- Odoo treats this as user configuration data

## However, there are important caveats:

### ⚠️ Theme Updates
If you update your **website theme** (not Odoo itself), custom code might be affected depending on:
- Whether the theme maintainer changed the structure
- If you're using a custom theme vs. a standard Odoo theme

### ⚠️ Major Version Upgrades
When upgrading between major versions (e.g., 18 → 19):
- Custom CSS/JS usually persists
- BUT the HTML structure of Odoo's default blocks might change
- Your selectors (like `.s_dynamic_snippet_title`) might need updating if Odoo changes class names

### ⚠️ Database Migration Issues
Occasionally during major upgrades, custom code fields might need to be re-verified after migration.

## Best Practices for Persistence:

1. **Document your customizations** - Keep a backup of your custom CSS
2. **Use a custom theme/module** (most reliable for long-term):
   - Create a simple custom module that inherits from the website theme
   - Add your CSS there - this survives all upgrades
3. **Test after upgrades** - Always verify customizations in a staging environment first
4. **Avoid inline styles** - Your approach using `<head>` CSS is good

## Most Reliable Method (For Production Sites):

If this is a production site that will go through multiple upgrades, consider creating a simple custom module:

```
my_website_customizations/
├── __manifest__.py
├── views/
    └── assets.xml
├── static/
    └── src/
        └── scss/
            └── custom.scss
```

Would you like guidance on creating a simple custom module for your CSS? It's actually quite straightforward and ensures 100% persistence.
