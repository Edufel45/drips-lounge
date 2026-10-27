# Drips Lounge website (Django)

## Run on your PC (Windows)
    python -m venv venv && venv\Scripts\activate
    pip install -r requirements.txt
    set DEBUG=1
    python manage.py migrate
    python manage.py createsuperuser
    python manage.py load_catalog --images "C:\drips lounge products"
    python manage.py runserver
Site: http://127.0.0.1:8000  |  Admin: http://127.0.0.1:8000/admin/

`load_catalog` reads shop/data/products.csv, matches photos by file name (any of .jpg/.jpeg/.png/.webp) and lists the products still missing a photo.
It is safe to run again; it never overwrites prices or photos already edited in the admin.

## What the client can do in /admin
- Products: edit price and tick/untick "available" straight from the list, add a product and upload its photo, delete, re-order.
- Categories: add or re-order.
- Site settings: WhatsApp number, phone, address, hours, map link, delivery text, logo and favicon.
Give the client a separate account (Staff status ON, not superuser) with permissions for Product, Category and Site settings only.

## Deploy (Render + Cloudinary + Neon/Supabase Postgres)
Free hosts wipe their disk, so photos MUST go to Cloudinary and data to a Postgres database.
1. Push this folder to GitHub. On Render create a Web Service: Build `./build.sh`, Start `gunicorn config.wsgi`.
2. Environment variables: SECRET_KEY (long random text), DATABASE_URL (Postgres URL), CLOUDINARY_URL (from your Cloudinary dashboard), PYTHON_VERSION=3.12.3. Do NOT set DEBUG.
3. Load the catalogue ONCE from your PC, pointed at the live database and Cloudinary (so photos upload to Cloudinary):
       set DATABASE_URL=...  &  set CLOUDINARY_URL=...
       python manage.py migrate
       python manage.py createsuperuser
       python manage.py load_catalog --images "C:\drips lounge products"
4. If the map pin is slightly off, change "Map query" in Site settings (e.g. to the exact coordinates from Google Maps).
