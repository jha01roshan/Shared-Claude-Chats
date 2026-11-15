"""Builds Tejas_Decimals_Fractions.pdf  (page 1 colour lesson, pages 2-3 B/W practice, page 4 answer key)."""
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor, black, white
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

D = "/usr/share/fonts/truetype/dejavu/"
pdfmetrics.registerFont(TTFont("DV", D + "DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DVB", D + "DejaVuSans-Bold.ttf"))
W, H = 595.27, 841.89  # A4

NAVY, TEAL, ORANGE, PURPLE = HexColor("#1F3A5F"), HexColor("#0E9594"), HexColor("#E8811A"), HexColor("#7B4FBF")
GREEN, BLUE, RED, YEL = HexColor("#3A9D4A"), HexColor("#2F74C0"), HexColor("#D93A3A"), HexColor("#FFE08A")
T_TEAL, T_OR, T_PUR = HexColor("#E3F5F4"), HexColor("#FDEEDC"), HexColor("#EFE8FA")
T_GRN, T_BLU, T_RED, T_YEL = HexColor("#E5F4E7"), HexColor("#E4EEFA"), HexColor("#FCE6E6"), HexColor("#FFF6D6")
INK = HexColor("#222222")


# ---------- layout helpers: tokens = text / fractions / blanks ----------
def sw(s, f, z):
    return pdfmetrics.stringWidth(s, f, z)


def tok_w(t, z, f="DV"):
    k = t[0]
    if k == "t":
        return sw(t[1], f, z)
    if k == "b":  # bold text
        return sw(t[1], "DVB", z)
    if k == "f":
        return max(sw(t[1], f, z * .85), sw(t[2], f, z * .85)) + 7
    if k == "bf":
        return 34
    if k == "ul":
        return t[1]
    if k == "cb":
        return z + 6 + sw(t[1], f, z) + 14
    if k == "sp":
        return t[1]


def draw_tokens(c, x, y, toks, z=15, col=INK, f="DV", box_col=None):
    """x = left, y = text baseline. Returns end x."""
    c.setFillColor(col)
    c.setStrokeColor(col)
    for t in toks:
        w = tok_w(t, z, f)
        k = t[0]
        if k == "t":
            c.setFont(f, z); c.drawString(x, y, t[1])
        elif k == "b":
            c.setFont("DVB", z); c.drawString(x, y, t[1])
        elif k == "f":
            ax = y + z * .30
            c.setFont(f, z * .85)
            c.drawCentredString(x + w / 2, ax + 2.5, t[1])
            c.drawCentredString(x + w / 2, ax - z * .85 - 1.5, t[2])
            c.setLineWidth(1.1); c.line(x + 1, ax, x + w - 1, ax)
        elif k == "bf":
            ax = y + z * .30
            c.setLineWidth(1.1); c.line(x + 2, ax, x + w - 2, ax)
            c.setLineWidth(.7)
            c.setStrokeColor(box_col or col)
            c.rect(x + 5, ax + 3, w - 10, z * .95, fill=0)
            c.rect(x + 5, ax - z * .95 - 3, w - 10, z * .95, fill=0)
            c.setStrokeColor(col)
        elif k == "ul":
            c.setLineWidth(.9); c.line(x, y - 2, x + w, y - 2)
        elif k == "cb":
            c.setLineWidth(.9); c.rect(x, y - 2, z * .85, z * .85, fill=0)
            c.setFont(f, z); c.drawString(x + z + 6, y, t[1])
        x += w
    return x


def toks_w(toks, z, f="DV"):
    return sum(tok_w(t, z, f) for t in toks)


def rbox(c, x, y, w, h, fill, stroke=None, r=9, lw=1.4):
    c.setFillColor(fill)
    if stroke:
        c.setStrokeColor(stroke); c.setLineWidth(lw)
    c.roundRect(x, y, w, h, r, fill=1, stroke=1 if stroke else 0)


def text(c, x, y, s, z=10, col=INK, f="DV", align="l"):
    c.setFillColor(col); c.setFont(f, z)
    {"l": c.drawString, "c": c.drawCentredString, "r": c.drawRightString}[align](x, y, s)


def para(c, x, y, s, width, z=9.5, col=INK, f="DV", lead=None):
    """Simple word wrap. Returns y after last line."""
    lead = lead or z * 1.35
    words, line = s.split(), ""
    for wd in words:
        trial = (line + " " + wd).strip()
        if sw(trial, f, z) > width and line:
            text(c, x, y, line, z, col, f); y -= lead; line = wd
        else:
            line = trial
    if line:
        text(c, x, y, line, z, col, f); y -= lead
    return y


def circle_num(c, cx, cy, n, col, r=11):
    c.setFillColor(col); c.circle(cx, cy, r, fill=1, stroke=0)
    text(c, cx, cy - 4.5, str(n), 13, white, "DVB", "c")


# =============================== PAGE 1 : LESSON (colour) ===============================
def page1(c):
    # banner
    c.setFillColor(NAVY); c.rect(0, H - 78, W, 78, fill=1, stroke=0)
    c.setFillColor(YEL); c.rect(0, H - 82, W, 4, fill=1, stroke=0)
    text(c, 30, H - 38, "Decimals are Fractions in Disguise!", 23, white, "DVB")
    text(c, 30, H - 60, "The  SEE  •  SWAP  •  SOLVE  trick", 13, YEL, "DVB")
    text(c, W - 30, H - 60, "Tejas's decimal cheat-sheet", 9, HexColor("#BFD0E6"), "DV", "r")

    # --- big idea ---
    y0 = H - 168
    rbox(c, 24, y0, W - 48, 78, T_YEL, HexColor("#E0B93C"))
    text(c, 36, y0 + 60, "THE BIG IDEA", 9, HexColor("#8A6A00"), "DVB")
    yy = para(c, 36, y0 + 45, "Every decimal is a fraction wearing a mask. Pull off the mask: "
              "digits after the point = zeros under the 1.", 285, 10, INK, "DVB")
    para(c, 36, yy - 1, "Tenths, hundredths, thousandths – that is all a decimal is!", 285, 9, HexColor("#555555"))
    # place value picture
    px = 338
    for i, (ch, lab) in enumerate([("0", ""), (".", ""), ("4", "tenths"), ("5", "hundredths")]):
        bx = px + i * 36
        if ch == ".":
            text(c, bx + 9, y0 + 42, ".", 22, RED, "DVB", "c"); continue
        rbox(c, bx, y0 + 38, 30 if ch != "." else 14, 28, white, NAVY, 5, 1.2)
        text(c, bx + 15, y0 + 46, ch, 18, NAVY, "DVB", "c")
        if lab:
            text(c, bx + 15, y0 + 28, lab, 6.5, HexColor("#555555"), "DV", "c")
    # equals fraction
    draw_tokens(c, px + 2, y0 + 9, [("t", "0.45  =  "), ("f", "45", "100")], 14, NAVY)
    text(c, px + 118, y0 + 9, "← 2 digits = 2 zeros", 8.5, RED, "DVB")

    # --- 3 steps ---
    top = y0 - 12
    h = 158
    cw = (W - 48 - 16) / 3
    steps = [
        (TEAL, T_TEAL, "SEE", "Count the digits after the point.",
         [[("t", "0.7  → 1 digit → "), ("b", "10")],
          [("t", "0.45 → 2 digits → "), ("b", "100")],
          [("t", "0.009 → 3 digits → "), ("b", "1000")]]),
        (ORANGE, T_OR, "SWAP", "Write it as a fraction: all digits on top.",
         [[("t", "0.2 = "), ("f", "2", "10")],
          [("t", "0.45 = "), ("f", "45", "100")],
          [("t", "0.009 = "), ("f", "9", "1000")]]),
        (PURPLE, T_PUR, "SOLVE", "Work with the fractions: top×top, bottom×bottom.",
         [[("f", "2", "10"), ("t", " × "), ("f", "3", "10"), ("t", " = "), ("f", "6", "100")],
          [("t", "= "), ("b", "0.06")],
          [("t", "(6 hundredths!)")]]),
    ]
    for i, (col, tint, name, desc, lines) in enumerate(steps):
        x = 24 + i * (cw + 8)
        rbox(c, x, top - h, cw, h, tint, col)
        circle_num(c, x + 18, top - 20, i + 1, col)
        text(c, x + 36, top - 25, name, 15, col, "DVB")
        para(c, x + 10, top - 46, desc, cw - 20, 8.2, INK, "DV", 10.5)
        ly = top - 76
        for ln in lines:
            draw_tokens(c, x + 12, ly, ln, 11, INK)
            ly -= 32 if i == 1 else 20

    # --- hop rule + trap ---
    top2 = top - h - 10
    h2 = 116
    lw_ = 312
    rbox(c, 24, top2 - h2, lw_, h2, T_BLU, BLUE)
    text(c, 36, top2 - 20, "MULTIPLYING?  Use the HOP RULE", 11, BLUE, "DVB")
    steps2 = ["① Kill the points, multiply whole numbers.",
              "② Count digits after the point in BOTH numbers.",
              "③ Hop the point back that many places."]
    yy = top2 - 37
    for s in steps2:
        text(c, 36, yy, s, 8.6, INK); yy -= 13
    rbox(c, 36, top2 - h2 + 8, lw_ - 24, 32, white, BLUE, 6, .8)
    draw_tokens(c, 44, top2 - h2 + 18, [("t", "0.2 × 0.3  →  2×3 = 6  →  1+1 = "), ("b", "2 hops"),
                                       ("t", "  →  "), ("b", "0.06")], 9.5, INK)
    # trap
    tx = 24 + lw_ + 8
    tw = W - 24 - tx
    rbox(c, tx, top2 - h2, tw, h2, T_RED, RED)
    text(c, tx + 10, top2 - 20, "⚠ TRAP ALERT", 11, RED, "DVB")
    y3 = para(c, tx + 10, top2 - 37, "0.2 × 0.3 is NOT 0.6 !", tw - 18, 9, INK, "DVB")
    para(c, tx + 10, y3 - 2, "Tenths × tenths = hundredths. A slice of a slice is tiny, "
         "so the answer must be smaller than 0.2.", tw - 18, 8.2, INK, "DV", 10.5)

    # --- division + fraction->decimal ---
    top3 = top2 - h2 - 10
    h3 = 104
    hw = (W - 48 - 8) / 2
    rbox(c, 24, top3 - h3, hw, h3, T_GRN, GREEN)
    text(c, 34, top3 - 19, "÷ 10, 100, 1000  =  hop LEFT", 10.5, GREEN, "DVB")
    para(c, 34, top3 - 33, "× 10, 100, 1000 = hop RIGHT. One hop per zero.", hw - 20, 8.2, INK, "DV", 10.5)
    draw_tokens(c, 34, top3 - 58, [("t", "45 ÷ 100 = "), ("f", "45", "100"), ("t", " = "), ("b", "0.45")], 11, INK)
    draw_tokens(c, 34, top3 - 88, [("t", "79 ÷ 1000 = "), ("f", "79", "1000"), ("t", " = "), ("b", "0.079")], 11, INK)
    x2 = 24 + hw + 8
    rbox(c, x2, top3 - h3, hw, h3, T_OR, ORANGE)
    text(c, x2 + 10, top3 - 19, "Fraction → decimal: fix the bottom", 10.5, ORANGE, "DVB")
    para(c, x2 + 10, top3 - 33, "Make the bottom 10, 100 or 1000. Whatever you do to the bottom, do to the top!",
         hw - 20, 8.2, INK, "DV", 10.5)
    draw_tokens(c, x2 + 10, top3 - 62, [("f", "3", "4"), ("t", " = "), ("f", "3×25", "4×25"), ("t", " = "), ("f", "75", "100"),
                                        ("t", " = "), ("b", "0.75")], 10.5, INK)
    text(c, x2 + 10, top3 - 94, "Or just divide:  12 ÷ 5 = 2.4", 8.8, INK, "DV")

    # --- find the ? ---
    top4 = top3 - h3 - 10
    h4 = 96
    rbox(c, 24, top4 - h4, W - 48, h4, T_PUR, PURPLE)
    text(c, 36, top4 - 19, "FIND THE  ?   –  do the OPPOSITE", 11, PURPLE, "DVB")
    text(c, W - 36, top4 - 19, "+ ↔ −        × ↔ ÷", 12, PURPLE, "DVB", "r")
    draw_tokens(c, 36, top4 - 46, [("t", "6 + ? = 8.5   →   ? = 8.5 − 6 = "), ("b", "2.5")], 10.5, INK)
    draw_tokens(c, 36, top4 - 76, [("t", "0.5 × ? = 3.5  →  ? = 3.5 ÷ 0.5 = "), ("f", "35", "10"), ("t", " ÷ "), ("f", "5", "10"),
                                   ("t", " = 35 ÷ 5 = "), ("b", "7")], 10.5, INK)
    text(c, W - 36, top4 - 76, "(the “10”s cancel!)", 8.2, PURPLE, "DVB", "r")

    # --- checks ---
    top5 = top4 - h4 - 10
    h5 = 72
    rbox(c, 24, top5 - h5, W - 48, h5, white, NAVY, 9, 1.6)
    text(c, 36, top5 - 17, "BEFORE YOU WRITE THE ANSWER – 3 QUICK CHECKS", 9.5, NAVY, "DVB")
    chk = ["✔ Recount the hops / zeros", "✔ Is the size sensible?  (× less than 1 → gets smaller)",
           "✔ Put it back in the sum – does it work?"]
    text(c, 36, top5 - 35, chk[0], 9.2, INK)
    text(c, 36, top5 - 49, chk[1], 9.2, INK)
    text(c, 36, top5 - 63, chk[2], 9.2, INK)
    c.setFillColor(NAVY)
    text(c, W / 2, 13, "Count the digits.  Write the zeros.  Hop the point.", 8.5, NAVY, "DVB", "c")


# =============================== PRACTICE PAGES (black & white) ===============================
G = HexColor("#EDEDED")


def head_bw(c, part):
    text(c, 30, H - 40, "Decimals & Fractions – Practice", 18, black, "DVB")
    text(c, W - 30, H - 40, f"Page {part}", 9, black, "DV", "r")
    text(c, 30, H - 62, "Name: ________________     Date: ____________     Score: ____ / 20", 10, black)
    c.setLineWidth(1.2); c.line(30, H - 72, W - 30, H - 72)
    text(c, 30, H - 86, "Remember:  SEE (count digits after the point)  •  SWAP (write as a fraction)  •  SOLVE (work, swap back)",
         8.4, HexColor("#333333"), "DV")


def section(c, y, title, tip):
    c.setFillColor(G); c.rect(30, y - 5, W - 60, 19, fill=1, stroke=0)
    text(c, 36, y, title, 10, black, "DVB")
    text(c, W - 36, y, tip, 8, HexColor("#333333"), "DV", "r")


def question(c, y, n, instr, toks, star=False):
    c.setStrokeColor(black); c.setLineWidth(1.1); c.setFillColor(white)
    c.circle(48, y - 12, 11, fill=0, stroke=1)
    text(c, 48, y - 16, str(n), 11, black, "DVB", "c")
    text(c, 70, y - 2, instr + ("   ★ challenge" if star else ""), 8.4, HexColor("#444444"), "DV")
    draw_tokens(c, 72, y - 30, toks, 15, black, "DV", black)
    c.setStrokeColor(HexColor("#BBBBBB")); c.setLineWidth(.5); c.setDash(1, 2)
    c.line(30, y - 50, W - 30, y - 50); c.setDash()


F = lambda a, b: ("f", a, b)
T = lambda s: ("t", s)
UL = lambda w=50: ("ul", w)
BF = ("bf",)
QS = {
    1: ("Write as a fraction.", [T("0.6   =  "), BF]),
    2: ("Write as a fraction.", [T("0.37   =  "), BF]),
    3: ("Write as a fraction.", [T("0.021   =  "), BF]),
    4: ("Write as a decimal.", [F("9", "100"), T("   =  "), UL(70)]),
    5: ("How many zeros go under the 1 when you write each as a fraction?",
        [T("0.8 → "), UL(24), T("    0.08 → "), UL(24), T("    0.008 → "), UL(24)]),
    6: ("Multiply the fractions, then write the answer as a decimal.",
        [F("3", "10"), T(" × "), F("4", "10"), T("  =  "), BF, T("  =  "), UL(55)]),
    7: ("SWAP to fractions first, then multiply.",
        [T("0.5 × 0.2  =  "), BF, T(" × "), BF, T(" = "), BF, T(" = "), UL(40)]),
    8: ("HOP RULE: kill the points, multiply, hop back.",
        [T("0.6 × 0.7 →  6×7 = "), UL(32), T(" ,  hops = "), UL(20), T("  →  "), UL(50)]),
    9: ("HOP RULE again (watch the zeros!).",
        [T("0.05 × 0.3 →  5×3 = "), UL(32), T(" , hops = "), UL(20), T(" → "), UL(55)]),
    10: ("Catch the trap – tick the right answer.",
         [T("0.4 × 0.9  =    "), ("cb", "3.6"), T("    "), ("cb", "0.36"), T("    "), ("cb", "0.036")]),
    11: ("Hop the point (one hop per zero).", [T("3.52 × 100  =  "), UL(90)]),
    12: ("Hop the point.", [T("47 ÷ 1000  =  "), UL(90)]),
    13: ("Hop the point.", [T("0.06 × 1000  =  "), UL(90)]),
    14: ("Write as a fraction first, then as a decimal.",
         [T("72 ÷ 100  =  "), BF, T("  =  "), UL(70)]),
    15: ("Make the bottom 10:  5 × ___ = 10.",
         [F("3", "5"), T("  =  "), BF, T("  =  "), UL(60)]),
    16: ("Make the bottom 100:  20 × ___ = 100.",
         [F("7", "20"), T("  =  "), BF, T("  =  "), UL(60)]),
    17: ("Make the bottom 1000:  8 × ___ = 1000.",
         [F("5", "8"), T("  =  "), BF, T("  =  "), UL(70)]),
    18: ("Do the opposite: × becomes ÷.", [T("0.3 × ?  =  2.4        ?  =  "), UL(60)]),
    19: ("Do the opposite: ÷ becomes ×.", [T("?  ÷  100  =  0.37        ?  =  "), UL(60)]),
    20: ("Use fractions: 2/10 × ?/10 = 8/100.", [T("0.2 × ?  =  0.08        ?  =  "), UL(60)]),
}


def practice_page(c, part, plan):
    head_bw(c, part)
    y = H - 118
    for item in plan:
        if item[0] == "S":
            y -= 6
            section(c, y, item[1], item[2]); y -= 22
        else:
            n = item[1]
            question(c, y, n, QS[n][0], QS[n][1], star=(n == 20))
            y -= 62


def page_key(c):
    text(c, 30, H - 40, "Answer Key  (for parent / checking)", 18, black, "DVB")
    c.setLineWidth(1.2); c.line(30, H - 52, W - 30, H - 52)
    key = [
        ("A. Decimal ↔ fraction",
         ["1)  6/10", "2)  37/100", "3)  21/1000", "4)  0.09", "5)  1 zero, 2 zeros, 3 zeros"]),
        ("B. Multiplying decimals",
         ["6)  12/100 = 0.12", "7)  5/10 × 2/10 = 10/100 = 0.10 = 0.1",
          "8)  42, 2 hops → 0.42", "9)  15, 3 hops → 0.015", "10)  0.36   (4×9=36, 2 hops)"]),
        ("C. Hops with 10 / 100 / 1000",
         ["11)  352", "12)  0.047", "13)  60", "14)  72/100 = 0.72"]),
        ("D. Fraction → decimal",
         ["15)  6/10 = 0.6   (×2)", "16)  35/100 = 0.35   (×5)", "17)  625/1000 = 0.625   (×125)"]),
        ("E. Find the ?",
         ["18)  ? = 2.4 ÷ 0.3 = 24 ÷ 3 = 8", "19)  ? = 0.37 × 100 = 37",
          "20)  ? = 8 ÷ 2 = 4 tenths = 0.4   (check: 0.2×0.4 = 0.08 ✔)"]),
    ]
    y = H - 82
    for title, lines in key:
        section(c, y, title, "")
        y -= 24
        for ln in lines:
            text(c, 44, y, ln, 10.5, black); y -= 17
        y -= 10
    y -= 6
    c.setLineWidth(1); c.rect(30, y - 70, W - 60, 76, fill=0)
    text(c, 40, y - 8, "Parent tip – what to watch for", 10, black, "DVB")
    para(c, 40, y - 24, "Most mistakes happen in the HOP count. Make Tejas say the hops out loud: "
         "“one digit after the point here, one there → two hops.”  If he gets Q8–10 wrong, repeat "
         "Q6–7 (fractions) – the fraction way always shows WHY the hop count is what it is.", W - 80, 9, black)
    text(c, W / 2, 20, "Tejas_Decimals_Fractions • answer key", 8, HexColor("#555555"), "DV", "c")


if __name__ == "__main__":
    out = "/home/user/Shared-Claude-Chats/tejas_decimals/Tejas_Decimals_Fractions.pdf"
    c = canvas.Canvas(out, pagesize=(W, H))
    c.setTitle("Decimals are Fractions in Disguise"); c.setAuthor("Practice sheet")
    page1(c); c.showPage()
    practice_page(c, "2 of 3", [("S", "A.  Decimal ↔ Fraction", "digits after the point = zeros under the 1")] +
                  [("Q", n) for n in range(1, 6)] +
                  [("S", "B.  Multiplying decimals", "tenths × tenths = hundredths")] +
                  [("Q", n) for n in range(6, 11)])
    c.showPage()
    practice_page(c, "3 of 3", [("S", "C.  Hop the point", "× → right      ÷ → left")] +
                  [("Q", n) for n in range(11, 15)] +
                  [("S", "D.  Fraction → Decimal", "same thing to top and bottom")] +
                  [("Q", n) for n in range(15, 18)] +
                  [("S", "E.  Find the ?", "use the opposite operation")] +
                  [("Q", n) for n in range(18, 21)])
    c.showPage()
    page_key(c); c.showPage()
    c.save()
    print("saved", out)
