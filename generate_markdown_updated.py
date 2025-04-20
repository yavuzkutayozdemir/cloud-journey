from pathlib import Path
import re
from datetime import datetime, timedelta

# Ayarlar
gallery_root = Path("gallery")
output_root = Path(".")
origin_date = datetime(2025, 4, 17)

# Tüm mevcut .png dosyalarını tara
all_images = list(gallery_root.glob("**/*.png"))

# En yüksek part numarasını bul
max_part = 0
for image_path in all_images:
    match = re.search(r'part-(\d+)', image_path.name)
    if match:
        max_part = max(max_part, int(match.group(1)))

# Gün sayısını hesapla
today = datetime.today()
day_diff = (today - origin_date).days + 1  # Day 1 = 17 Nisan

# Sonraki part numarası
next_part = max_part + 1

for series_folder in gallery_root.iterdir():
    if not series_folder.is_dir():
        continue

    series = series_folder.name
    image_files = list(series_folder.glob("*.png"))

    for image_path in image_files:
        # Dosya adı zaten işlenmişse atla
        if re.search(r'part-\d+-day-\d+-', image_path.name):
            continue

        # Başlık oluştur
        title_raw = image_path.stem.lower().replace(" ", "-")
        title_slug = title_raw.replace("-", " ").title()

        # Yeni görsel adı
        new_image_name = f"part-{next_part:03d}-day-{day_diff:03d}-{title_raw}.png"
        new_image_path = series_folder / new_image_name
        image_path.rename(new_image_path)

        # Markdown oluştur
        md_filename = f"part-{next_part:03d}-{series}/-{title_raw} (day-{day_diff}).md"
        md_path = Path(series) / md_filename

        if not md_path.exists():
            md_content = f"""## Part {next_part:03d} – {title_slug} (Day {day_diff})

### Goal
<!-- Write what you aimed to achieve in this part -->

---

### Technical Steps
<!-- List the steps you followed, commands you used, and how you implemented the task -->

---

### Outcome
<!-- Summarize the result, what worked, and what challenges you faced -->

<br>

![{title_slug} screen](../../gallery/{series}/{new_image_name})
"""
            md_path.parent.mkdir(parents=True, exist_ok=True)
            md_path.write_text(md_content, encoding="utf-8")
            print(f"✅ Created: {md_path}")

        next_part += 1