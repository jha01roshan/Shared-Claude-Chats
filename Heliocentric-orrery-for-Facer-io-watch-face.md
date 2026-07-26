# Heliocentric orrery for Facer.io watch face

- Source: https://claude.ai/share/90bce2d1-96cf-4bad-959a-ede76c335228
- Author: Jason
- Created: 2025-11-02
- Messages: 2

---

## Human

How to create a heliocentric orrery in Facer.io watch face?

---

## Assistant

I can help you create a heliocentric orrery (solar system model) for a Facer.io watch face! Here's a comprehensive guide:

## Basic Concept

In Facer, you'll use rotating layers with transparency to simulate planetary orbits around the Sun. Each planet needs:
1. An orbit path (circular guide)
2. A planet image/element
3. Rotation formulas based on actual orbital periods

## Step-by-Step Process

### 1. **Set Up the Sun (Center)**
- Place a circular element at the center of your watch face (160, 160 on a 320x320 canvas)
- This stays static - no rotation

### 2. **Create Orbit Paths**
For each planet, add a circular shape:
- Center it at (160, 160)
- Set different radii for each orbit (Mercury smallest, Neptune largest)
- Use thin stroke, no fill
- Low opacity (10-20%) so they're subtle guides

### 3. **Add Planets with Rotation Formulas**

Each planet needs proper X and Y positioning using these formulas:

**X Position:**
```
(160 + RADIUS * cos(2 * pi * (#DWE# / PERIOD)))
```

**Y Position:**
```
(160 + RADIUS * sin(2 * pi * (#DWE# / PERIOD)))
```

Where:
- **160** = center point
- **RADIUS** = distance from Sun in pixels
- **#DWE#** = day of the week epoch (days since Jan 1, 1970)
- **PERIOD** = orbital period in days

### 4. **Orbital Periods (Earth Days)**

- Mercury: 88
- Venus: 225
- Earth: 365
- Mars: 687
- Jupiter: 4,333
- Saturn: 10,759
- Uranus: 30,687
- Neptune: 60,190

### 5. **Example for Earth**

If Earth's orbit radius is 60 pixels:

**X Position:**
```
(160 + 60 * cos(2 * pi * (#DWE# / 365)))
```

**Y Position:**
```
(160 + 60 * sin(2 * pi * (#DWE# / 365)))
```

### 6. **Suggested Radii (pixels)**

For a 320x320 face:
- Mercury: 25
- Venus: 35
- Earth: 45
- Mars: 60
- Jupiter: 85
- Saturn: 105
- Uranus: 125
- Neptune: 145

### 7. **Additional Details**

**Moon orbiting Earth:**
- Calculate Earth's position first
- Add smaller radius orbit around Earth's position
- Moon period: 27.3 days

**Asteroid Belt:**
- Add multiple small dots at radius ~70-75
- Random angles using different offset values

**Visual Enhancements:**
- Use planet colors (Mars = red, Jupiter = orange/brown, etc.)
- Add Saturn's rings
- Make outer planets smaller (proper scale)
- Add subtle glow effects

### 8. **Performance Tips**

- Keep planet images small (under 20x20 pixels for outer planets)
- Limit total layers to avoid lag
- Test on actual watch hardware

## Starting Point Formula Template

For any planet:
```
X: (160 + [RADIUS] * cos(2 * pi * (#DWE# / [PERIOD])))
Y: (160 + [RADIUS] * sin(2 * pi * (#DWE# / [PERIOD])))
```

Would you like me to provide the complete formulas for all planets, or help you with a specific aspect like adding the Moon or making it more accurate with elliptical orbits?
