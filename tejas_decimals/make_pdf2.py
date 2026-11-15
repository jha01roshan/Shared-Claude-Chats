"""Sheet 2: Dividing decimals. Page 1 colour lesson, page 2 B/W practice (20 Qs). No answer key."""
from make_pdf import *  # helpers, colours, fonts


def lesson(c):
    c.setFillColor(NAVY); c.rect(0, H - 78, W, 78, fill=1, stroke=0)
    c.setFillColor(YEL); c.rect(0, H - 82, W, 4, fill=1, stroke=0)
    text(c, 30, H - 38, "Dividing Decimals? Make the divisor WHOLE!", 21, white, "DVB")
    text(c, 30, H - 60, "The  SHIFT  •  DIVIDE  •  PLACE  trick", 13, YEL, "DVB")
    text(c, W - 30, H - 60, "Tejas's decimal cheat-sheet #2", 9, HexColor("#BFD0E6"), "DV", "r")

    # big idea
    y0 = H - 170
    rbox(c, 24, y0, W - 48, 80, T_YEL, HexColor("#E0B93C"))
    text(c, 36, y0 + 62, "THE BIG IDEA", 9, HexColor("#8A6A00"), "DVB")
    yy = para(c, 36, y0 + 47, "A division is a fraction. Multiply the top AND bottom by the same 10, 100 or 1000 "
              "– the answer does not change, but the numbers get friendly!", 300, 9.5, INK, "DVB")
    draw_tokens(c, 358, y0 + 36, [("f", "0.288", "2.4"), ("t", " = "), ("f", "2.88", "24"), ("t", " = "), ("b", "0.12")], 13, NAVY)
    text(c, 358, y0 + 8, "×10 on top and bottom = shift both points 1 hop", 7.6, RED, "DVB")

    # 3 steps
    top = y0 - 12
    h = 140
    cw = (W - 48 - 16) / 3
    steps = [
        (TEAL, T_TEAL, "SHIFT", "Hop the point in the divisor until it is whole. Hop the other number the SAME hops.",
         [[("t", "6.3 ÷ 0.7")], [("t", "↓ 1 hop each")], [("b", "63 ÷ 7")]]),
        (ORANGE, T_OR, "DIVIDE", "Now divide like whole numbers. Run out? Add zeros after the point – they are free!",
         [[("t", "63 ÷ 7 = "), ("b", "9")], [("t", "11 ÷ 8 → 11.000")], [("t", "(add as many 0s as needed)")]]),
        (PURPLE, T_PUR, "PLACE", "The point in the answer goes straight UP from the point in the number being divided.",
         [[("t", "2.88 ÷ 24")], [("t", "point up ↑ → "), ("b", "0.12")], [("t", "check: 24 × 0.12 = 2.88 ✔")]]),
    ]
    for i, (col, tint, name, desc, lines) in enumerate(steps):
        x = 24 + i * (cw + 8)
        rbox(c, x, top - h, cw, h, tint, col)
        circle_num(c, x + 18, top - 20, i + 1, col)
        text(c, x + 36, top - 25, name, 15, col, "DVB")
        para(c, x + 10, top - 45, desc, cw - 20, 8, INK, "DV", 10.2)
        ly = top - 92
        for ln in lines:
            draw_tokens(c, x + 12, ly, ln, 10, INK); ly -= 15

    # long division picture + trap
    top2 = top - h - 10
    h2 = 156
    lw_ = 300
    rbox(c, 24, top2 - h2, lw_, h2, T_BLU, BLUE)
    text(c, 36, top2 - 20, "FRACTION → DECIMAL = top ÷ bottom", 10.5, BLUE, "DVB")
    para(c, 36, top2 - 35, "Tejas's 11/8 is 11 ÷ 8. Add zeros and keep going:", lw_ - 24, 8.4, INK)
    # long-division drawing
    bx, by = 84, top2 - 124  # bracket baseline
    c.setFillColor(INK); c.setStrokeColor(INK); c.setLineWidth(1.3)
    c.line(bx, by - 6, bx, by + 58); c.line(bx, by + 58, bx + 112, by + 58)
    text(c, bx - 6, by + 40, "8", 14, INK, "DVB", "r")
    text(c, bx + 8, by + 62, "1 . 3 7 5", 13, RED, "DVB")
    text(c, bx + 8, by + 40, "1 1 . 0 0 0", 13, INK, "DV")
    text(c, bx + 128, by + 40, "8 into 11 = 1 r 3", 8.4, BLUE, "DVB")
    text(c, bx + 128, by + 26, "30 ÷ 8 = 3 r 6", 8.4, BLUE, "DVB")
    text(c, bx + 128, by + 12, "60 ÷ 8 = 7 r 4", 8.4, BLUE, "DVB")
    text(c, bx + 128, by - 2, "40 ÷ 8 = 5   done!", 8.4, BLUE, "DVB")
    text(c, bx + 128, by - 22, "11/8 = 1.375", 12, NAVY, "DVB")

    tx = 24 + lw_ + 8
    tw = W - 24 - tx
    rbox(c, tx, top2 - h2, tw, h2, T_RED, RED)
    text(c, tx + 10, top2 - 20, "⚠ TRAP ALERT", 11, RED, "DVB")
    y3 = para(c, tx + 10, top2 - 37, "Dividing by a number LESS than 1 makes the answer BIGGER!", tw - 18, 9, INK, "DVB")
    y3 = para(c, tx + 10, y3 - 2, "How many halves fit in 6?", tw - 18, 8.4, INK)
    draw_tokens(c, tx + 10, y3 - 14, [("t", "6 ÷ 0.5 = "), ("b", "12")], 11, INK)
    draw_tokens(c, tx + 10, y3 - 36, [("t", "0.8 ÷ 0.01 = "), ("b", "80")], 11, INK)
    para(c, tx + 10, y3 - 56, "Shift check: 0.01 needs 2 hops → 80 ÷ 1 .", tw - 18, 8, HexColor("#555555"))

    # find the ?
    top3 = top2 - h2 - 10
    h3 = 84
    rbox(c, 24, top3 - h3, W - 48, h3, T_PUR, PURPLE)
    text(c, 36, top3 - 19, "FIND THE  ?   – opposite again", 11, PURPLE, "DVB")
    text(c, W - 36, top3 - 19, "× ↔ ÷", 12, PURPLE, "DVB", "r")
    draw_tokens(c, 36, top3 - 46, [("t", "? × 0.4 = 2.8   →   ? = 2.8 ÷ 0.4 = 28 ÷ 4 = "), ("b", "7")], 10.5, INK)
    draw_tokens(c, 36, top3 - 70, [("t", "? ÷ 0.5 = 8   →   ? = 8 × 0.5 = "), ("b", "4")], 10.5, INK)

    # checks
    topz = top3 - h3 - 10
    hz = 74
    rbox(c, 24, topz - hz, W - 48, hz, T_GRN, GREEN)
    text(c, 36, topz - 19, "ZEROS ARE FREE (after the point)", 11, GREEN, "DVB")
    draw_tokens(c, 36, topz - 42, [("t", "3 = 3.0 = 3.00      0.5 = 0.50 = 0.500")], 10.5, INK)
    draw_tokens(c, 36, topz - 63, [("t", "3 \u00f7 4  \u2192  3.00 \u00f7 4  =  "), ("b", "0.75")], 10.5, INK)
    top4 = topz - hz - 10
    h4 = 74
    rbox(c, 24, top4 - h4, W - 48, h4, white, NAVY, 9, 1.6)
    text(c, 36, top4 - 18, "3 QUICK CHECKS BEFORE YOU WRITE THE ANSWER", 9.5, NAVY, "DVB")
    for i, s in enumerate(["✔ Did I hop BOTH numbers the same number of times?",
                           "✔ Is the point straight above the point?",
                           "✔ Multiply back: answer × divisor = the number I started with?"]):
        text(c, 36, top4 - 36 - i * 15, s, 9.2, INK)
    text(c, W / 2, 13, "Shift both.  Divide.  Point goes straight up.", 8.5, NAVY, "DVB", "c")


Q = {
    1: ("SHIFT: make the divisor whole.", [T("0.8 ÷ 0.2  =  8 ÷ "), UL(26), T(" =  "), UL(30)]),
    2: ("Shift 2 hops.", [T("0.9 ÷ 0.03  =  90 ÷ "), UL(24), T(" =  "), UL(30)]),
    3: ("Shift both.", [T("4.5 ÷ 0.5  =  "), UL(26), T(" ÷ 5 =  "), UL(30)]),
    4: ("Shift both.", [T("1.44 ÷ 0.12  =  "), UL(30), T(" ÷ "), UL(24), T(" = "), UL(28)]),
    5: ("How many hops make the divisor whole?", [T("0.025 → "), UL(20), T(" hops   0.4 → "), UL(20), T(" hop")]),
    6: ("DIVIDE & PLACE the point.", [T("6.4 ÷ 4  =  "), UL(80)]),
    7: ("DIVIDE & PLACE the point.", [T("0.84 ÷ 7  =  "), UL(80)]),
    8: ("Shift, then divide.", [T("9.6 ÷ 0.4  =  "), UL(80)]),
    9: ("Shift, then divide.", [T("2.5 ÷ 0.05  =  "), UL(80)]),
    10: ("Shift, then divide.", [T("0.72 ÷ 0.8  =  "), UL(80)]),
    11: ("Top ÷ bottom (add zeros).", [F("3", "4"), T("  =  3 ÷ 4  =  "), UL(60)]),
    12: ("Top ÷ bottom.", [F("9", "5"), T("  =  9 ÷ 5  =  "), UL(60)]),
    13: ("Top ÷ bottom (3 zeros!).", [F("7", "8"), T("  =  7 ÷ 8  =  "), UL(60)]),
    14: ("Top ÷ bottom.", [F("11", "4"), T("  =  11 ÷ 4  =  "), UL(60)]),
    15: ("Catch the trap: 6 ÷ 0.5 = ?  (tick one)", [("cb", "3"), T("   "), ("cb", "12"), T("   "), ("cb", "0.12")]),
    16: ("Catch the trap: 0.8 ÷ 0.01 = ?  (tick one)", [("cb", "0.008"), T("  "), ("cb", "8"), T("  "), ("cb", "80")]),
    17: ("Find the ?  (opposite of ×)", [T("?  ×  0.6  =  4.2      ? = "), UL(50)]),
    18: ("Find the ?  (opposite of ÷ )", [T("5.4  ÷  ?  =  9       ? = "), UL(50)]),
    19: ("Find the ?  (opposite of ÷ )", [T("?  ÷  0.5  =  8       ? = "), UL(50)]),
    20: ("Find the ?", [T("3.6  ÷  ?  =  12      ? = "), UL(50)]),
}


def practice(c):
    text(c, 30, H - 40, "Dividing Decimals – Practice", 18, black, "DVB")
    text(c, W - 30, H - 40, "Sheet 2", 9, black, "DV", "r")
    text(c, 30, H - 62, "Name: ________________     Date: ____________     Score: ____ / 20", 10, black)
    c.setLineWidth(1.2); c.line(30, H - 72, W - 30, H - 72)
    text(c, 30, H - 86, "Remember:  SHIFT (both points, same hops)  •  DIVIDE (add zeros if needed)  •  PLACE (point straight up)",
         8.4, HexColor("#333333"))
    colw = (W - 60) / 2
    for col, title in enumerate(["Part 1 – Shift, divide, place", "Part 2 – Fractions, traps & the ?"]):
        x = 30 + col * colw
        c.setFillColor(G); c.rect(x + 2, H - 117, colw - 6, 19, fill=1, stroke=0)
        text(c, x + 8, H - 111, title, 9.5, black, "DVB")
        for r in range(10):
            n = col * 10 + r + 1
            y = H - 128 - r * 66
            c.setLineWidth(1.1); c.setStrokeColor(black); c.circle(x + 16, y - 14, 10, fill=0, stroke=1)
            text(c, x + 16, y - 18, str(n), 10.5, black, "DVB", "c")
            text(c, x + 33, y - 2, Q[n][0] + ("  ★ challenge" if n == 20 else ""), 7.8, HexColor("#444444"))
            draw_tokens(c, x + 34, y - 30, Q[n][1], 12.5, black, "DV", black)
            c.setStrokeColor(HexColor("#BBBBBB")); c.setLineWidth(.5); c.setDash(1, 2)
            c.line(x + 2, y - 50, x + colw - 6, y - 50); c.setDash()
    c.setStrokeColor(HexColor("#BBBBBB")); c.setLineWidth(.6)
    c.line(W / 2, H - 120, W / 2, H - 128 - 9 * 66 - 50)


if __name__ == "__main__":
    out = "/home/user/Shared-Claude-Chats/tejas_decimals/Tejas_Dividing_Decimals.pdf"
    c = canvas.Canvas(out, pagesize=(W, H))
    c.setTitle("Dividing Decimals"); c.setAuthor("Practice sheet")
    lesson(c); c.showPage()
    practice(c); c.showPage()
    c.save(); print("saved", out)
