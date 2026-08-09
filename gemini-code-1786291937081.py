import os

pages = {
    "index.html": """<!doctype html>
<html lang="tl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>CHC | Unang Pahina</title><style>
:root{--bg:#020912;--panel:#061522;--cyan:#22cfff;--gold:#f2c34f;--text:#eefaff;--muted:#9db8c7;--line:#12617b;}
*{box-sizing:border-box}html,body{margin:0;padding:0;background:radial-gradient(circle at 50% 0%,#0a2740 0,#020912 42%,#01060b 100%);color:var(--text);font-family:Arial,sans-serif;}
header{height:76px;background:rgba(3,14,24,.94);border-bottom:1px solid #16445a;display:flex;align-items:center;justify-content:space-between;padding:0 5vw;}
.logo{font-weight:900;font-size:28px;color:var(--cyan);text-shadow:0 0 12px rgba(34,207,255,.65);text-decoration:none}
nav a{font-size:11px;text-transform:uppercase;color:#d9edf5;margin-left:18px;text-decoration:none}
main{width:min(1120px,92vw);margin:0 auto;padding:58px 0}
.hud{border:1px solid var(--line);background:linear-gradient(145deg,rgba(8,32,49,.92),rgba(2,12,21,.9));padding:28px;position:relative;}
.btn{display:inline-block;background:#16a8d6;color:white;padding:13px 24px;border-radius:4px;font-weight:800;text-decoration:none}
footer{border-top:1px solid #113d50;padding:25px 5vw;text-align:center;color:#7ea3b2;font-size:12px}
</style></head><body>
<header><a class="logo" href="index.html">CHC</a><nav><a href="index.html">Unang Pahina</a><a href="about-us.html">Tungkol sa Amin</a><a href="services.html">Mga Serbisyo</a><a href="resources.html">Mga Resource</a><a href="get-help.html">Humingi ng Tulong</a><a href="contact.html">Kumuha ng Impormasyon</a></nav></header>
<main><section class="hud"><h1>MAMAMAYAN NA TUMUTULONG SA MAMAMAYAN</h1><p>Pagpapalakas ng komunidad gamit ang konektadong imprastraktura.</p><a class="btn" href="get-help.html">HUMINGI NG TULONG</a></section></main>
<footer>PAGPAPALAKAS NG MGA KOMUNIDAD. PAGBABAGO NG MGA BUHAY.</footer></body></html>""",

    "about-us.html": """<!doctype html><html lang="tl"><head><meta charset="utf-8"><title>CHC | Tungkol sa Amin</title></head><body style="background:#020912;color:#eefaff;font-family:sans-serif;padding:50px;"><h1>Tungkol sa CHC</h1><p>Isang organisasyong nakatuon sa pagpapalakas ng mga pamilya.</p><a href="index.html" style="color:#22cfff;">Bumalik sa Unang Pahina</a></body></html>""",
    "services.html": """<!doctype html><html lang="tl"><head><meta charset="utf-8"><title>CHC | Mga Serbisyo</title></head><body style="background:#020912;color:#eefaff;font-family:sans-serif;padding:50px;"><h1>Aming Mga Serbisyo</h1><p>Tulong sa Pagkain, Trabaho, at Bahay.</p><a href="index.html" style="color:#22cfff;">Bumalik sa Unang Pahina</a></body></html>""",
    "resources.html": """<!doctype html><html lang="tl"><head><meta charset="utf-8"><title>CHC | Mga Resource</title></head><body style="background:#020912;color:#eefaff;font-family:sans-serif;padding:50px;"><h1>Mga Resource</h1><p>Mga gamit at gabay para sa iyong pag-unlad.</p><a href="index.html" style="color:#22cfff;">Bumalik sa Unang Pahina</a></body></html>""",
    "get-help.html": """<!doctype html><html lang="tl"><head><meta charset="utf-8"><title>CHC | Humingi ng Tulong</title></head><body style="background:#020912;color:#eefaff;font-family:sans-serif;padding:50px;"><h1>Humingi ng Tulong</h1><p>24/7 na Tulong mula sa AI at Komunidad.</p><a href="index.html" style="color:#22cfff;">Bumalik sa Unang Pahina</a></body></html>""",
    "contact.html": """<!doctype html><html lang="tl"><head><meta charset="utf-8"><title>CHC | Kontak</title></head><body style="background:#020912;color:#eefaff;font-family:sans-serif;padding:50px;"><h1>Makipag-ugnayan</h1><p>Email: info@chchelp.org | Telepono: (555) 123-4567</p><a href="index.html" style="color:#22cfff;">Bumalik sa Unang Pahina</a></body></html>"""
}

output_dir = "CHC_Website_Files"
os.makedirs(output_dir, exist_ok=True)

for filename, content in pages.items():
    filepath = os.path.join(output_dir, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

print(f"Matagumpay na na-render ang 6 na site files sa folder na: './{output_dir}'")