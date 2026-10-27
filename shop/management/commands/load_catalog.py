import csv
from pathlib import Path
from django.core.files import File
from django.core.management.base import BaseCommand
from shop.models import Category, Product, SiteSettings


class Command(BaseCommand):
    help = "Load products from shop/data/products.csv and attach photos from a folder (matched by file name)"

    def add_arguments(self, parser):
        parser.add_argument("--images", default="seed_images", help="folder with the product photos")
        parser.add_argument("--replace", action="store_true", help="re-attach photos even if a product already has one")

    def handle(self, *args, **opts):
        SiteSettings.load()
        folder = Path(opts["images"])
        files = {}
        if folder.is_dir():
            files = {f.stem.lower(): f for f in folder.iterdir() if f.suffix.lower() in (".jpg", ".jpeg", ".png", ".webp")}
        csv_path = Path(__file__).resolve().parents[2] / "data" / "products.csv"
        added = attached = 0
        missing = []
        used = set()
        with open(csv_path, encoding="utf-8") as fh:
            for i, r in enumerate(csv.DictReader(fh)):
                cat, _ = Category.objects.get_or_create(name=r["category"], defaults={"order": Category.objects.count()})
                p, made = Product.objects.get_or_create(name=r["name"], size=r["size"], defaults={
                    "category": cat, "order": i, "price": int(r["price"]) if r["price"] else None})
                added += made
                src = files.get(Path(r["file"]).stem.lower())
                if src:
                    used.add(src.stem.lower())
                if opts["replace"] or not p.image:
                    if src:
                        with open(src, "rb") as img:
                            p.image.save(src.name, File(img), save=True)
                        attached += 1
                    else:
                        missing.append(r["file"])
        self.stdout.write(f"Products created: {added} | photos attached: {attached} | still without photo: {len(missing)}")
        for m in missing:
            self.stdout.write("  missing: " + m)
        unused = sorted(f.name for k, f in files.items() if k not in used)
        if unused:
            self.stdout.write("Photos in the folder that matched NO product (rename them to the missing names above):")
            for u in unused:
                self.stdout.write("  unused: " + u)
