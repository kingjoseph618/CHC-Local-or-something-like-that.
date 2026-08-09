mkdir -p website && cd website

cat << 'EOF' > index.html
<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>CHC | Home</title></head>
<body style="background:#020912;color:#eefaff;font-family:sans-serif;padding:50px;">
<h1>CITIZENS HELPING CITIZENS</h1><p>Site loaded onto Google Cloud.</p>
</body></html>
EOF

cp index.html about-us.html
cp index.html services.html
cp index.html resources.html
cp index.html get-help.html
cp index.html contact.html