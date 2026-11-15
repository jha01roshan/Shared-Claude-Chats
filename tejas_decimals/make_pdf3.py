"""Practice-only sheet (2 pages B/W, 20 Qs, same skills as sheet 1, new numbers, small hints kept)."""
from make_pdf import *
import make_pdf as m

m.QS.update({
    1: ("Write as a fraction.", [T("0.8   =  "), BF]),
    2: ("Write as a fraction.", [T("0.53   =  "), BF]),
    3: ("Write as a fraction.", [T("0.407   =  "), BF]),
    4: ("Write as a decimal.", [F("17", "100"), T("   =  "), UL(70)]),
    5: ("How many zeros go under the 1 when you write each as a fraction?",
        [T("0.5 → "), UL(24), T("    0.05 → "), UL(24), T("    0.005 → "), UL(24)]),
    6: ("Multiply the fractions, then write the answer as a decimal.",
        [F("7", "10"), T(" × "), F("3", "10"), T("  =  "), BF, T("  =  "), UL(55)]),
    7: ("SWAP to fractions first, then multiply.",
        [T("0.6 × 0.5  =  "), BF, T(" × "), BF, T(" = "), BF, T(" = "), UL(40)]),
    8: ("HOP RULE: kill the points, multiply, hop back.",
        [T("0.8 × 0.9 →  8×9 = "), UL(32), T(" ,  hops = "), UL(20), T("  →  "), UL(50)]),
    9: ("HOP RULE again (watch the zeros!).",
        [T("0.04 × 0.7 →  4×7 = "), UL(32), T(" , hops = "), UL(20), T(" → "), UL(55)]),
    10: ("Catch the trap – tick the right answer.",
         [T("0.6 × 0.8  =    "), ("cb", "4.8"), T("    "), ("cb", "0.48"), T("    "), ("cb", "0.048")]),
    11: ("Hop the point (one hop per zero).", [T("6.17 × 100  =  "), UL(90)]),
    12: ("Hop the point.", [T("95 ÷ 1000  =  "), UL(90)]),
    13: ("Hop the point.", [T("0.04 × 1000  =  "), UL(90)]),
    14: ("Write as a fraction first, then as a decimal.", [T("38 ÷ 100  =  "), BF, T("  =  "), UL(70)]),
    15: ("Make the bottom 10:  5 × ___ = 10.", [F("4", "5"), T("  =  "), BF, T("  =  "), UL(60)]),
    16: ("Make the bottom 100:  20 × ___ = 100.", [F("9", "20"), T("  =  "), BF, T("  =  "), UL(60)]),
    17: ("Make the bottom 1000:  8 × ___ = 1000.", [F("3", "8"), T("  =  "), BF, T("  =  "), UL(70)]),
    18: ("Do the opposite: × becomes ÷.", [T("0.6 × ?  =  3.6        ?  =  "), UL(60)]),
    19: ("Do the opposite: ÷ becomes ×.", [T("?  ÷  100  =  0.58        ?  =  "), UL(60)]),
    20: ("Use fractions: 3/10 × ?/10 = 9/100.", [T("0.3 × ?  =  0.09        ?  =  "), UL(60)]),
})

if __name__ == "__main__":
    out = "/home/user/Shared-Claude-Chats/tejas_decimals/Tejas_Decimals_Practice_2.pdf"
    c = canvas.Canvas(out, pagesize=(W, H))
    c.setTitle("Decimals & Fractions - Practice 2")
    m.practice_page(c, "1 of 2", [("S", "A.  Decimal ↔ Fraction", "digits after the point = zeros under the 1")] +
                    [("Q", n) for n in range(1, 6)] +
                    [("S", "B.  Multiplying decimals", "tenths × tenths = hundredths")] +
                    [("Q", n) for n in range(6, 11)])
    c.showPage()
    m.practice_page(c, "2 of 2", [("S", "C.  Hop the point", "× → right      ÷ → left")] +
                    [("Q", n) for n in range(11, 15)] +
                    [("S", "D.  Fraction → Decimal", "same thing to top and bottom")] +
                    [("Q", n) for n in range(15, 18)] +
                    [("S", "E.  Find the ?", "use the opposite operation")] +
                    [("Q", n) for n in range(18, 21)])
    c.showPage(); c.save(); print("saved", out)
