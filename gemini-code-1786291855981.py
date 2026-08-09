import os

pages = {
    "index.html": """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>CHC | Home</title><style>
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
<header><a class="logo" href="index.html">CHC</a><nav><a href="index.html">Home</a><a href="about-us.html">About Us</a><a href="services.html">Services</a><a href="resources.html">Resources</a><a href="get-help.html">Get Help</a><a href="contact.html">Contact</a></nav></header>
<main><section class="hud"><h1>CITIZENS HELPING CITIZENS</h1><p>Empowering communities through connected infrastructure.</p><a class="btn" href="get-help.html">GET HELP</a></section></main>
<footer>EMPOWERING COMMUNITIES. TRANSFORMING LIVES. BUILDING HOPE.</footer></body></html>""",

    "about-us.html": """<!doctype html><html lang="en"><head><meta charset="utf-8"><title>CHC | About Us</title></head><body style="background:#020912;color:#eefaff;font-family:sans-serif;padding:50px;"><h1>About CHC</h1><p>Community-driven organization dedicated to empowering families.</p><a href="index.html" style="color:#22cfff;">Back to Home</a></body></html>""",
    "services.html": """<!doctype html><html lang="en"><head><meta charset="utf-8"><title>CHC | Services</title></head><body style="background:#020912;color:#eefaff;font-family:sans-serif;padding:50px;"><h1>Our Services</h1><p>Food Support, Employment Assistance, Housing Support.</p><a href="index.html" style="color:#22cfff;">Back to Home</a></body></html>""",
    "resources.html": """<!doctype html><html lang="en"><head><meta charset="utf-8"><title>CHC | Resources</title></head><body style="background:#020912;color:#eefaff;font-family:sans-serif;padding:50px;"><h1>Resources</h1><p>Tools and guidance to empower your growth.</p><a href="index.html" style="color:#22cfff;">Back to Home</a></body></html>""",
    "get-help.html": """<!doctype html><html lang="en"><head><meta charset="utf-8"><title>CHC | Get Help</title></head><body style="background:#020912;color:#eefaff;font-family:sans-serif;padding:50px;"><h1>Get Help</h1><p>24/7 AI Assistance & Support Networks.</p><a href="index.html" style="color:#22cfff;">Back to Home</a></body></html>""",
    "contact.html": """<!doctype html><html lang="en"><head><meta charset="utf-8"><title>CHC | Contact</title></head><body style="background:#020912;color:#eefaff;font-family:sans-serif;padding:50px;"><h1>Contact Us</h1><p>Email: info@chchelp.org | Phone: (555) 123-4567</p><a href="index.html" style="color:#22cfff;">Back to Home</a></body></html>"""
}

output_dir = "CHC_Website_Files"
os.makedirs(output_dir, exist_ok=True)

for filename, content in pages.items():
    filepath = os.path.join(output_dir, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

print(f"Successfully rendered 6 site files into './{output_dir}'")