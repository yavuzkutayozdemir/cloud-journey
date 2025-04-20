
from pathlib import Path
import re
import shutil
from datetime import datetime, timedelta
import os

# Başlangıç tarihi
start_date = datetime(2025, 4, 17)

# Klasör ayarları
gallery_root = Path("gallery")
output_root = Path("cloud-support-track")

# GitHub bilgileri
github_user = "yavuzkutayozdemir"
github_repo = "cloud-journey"
github_branch = "main"

# Part numarasını global tutalım
def get_next_part_number():
    existing_parts = list(output_root.glob("**/part-*.md"))
    if not existing_parts:
        return 1
    last_part_num = max([int(re.search(r'part-(\d+)', p.stem).group(1)) for p in existing_parts])
    return last_part_num + 1

# GitHub raw URL oluştur
def get_raw_github_url(series_name, image_name):
    return f"https://raw.githubusercontent.com/{github_user}/{github_repo}/{github_branch}/gallery/{series_name}/{image_name}"

# Resimleri bul ve işle
for series_folder in gallery_root.iterdir():
    if not series_folder.is_dir():
        continue

    for image_path in series_folder.glob("*.png"):
        part_num = get_next_part_number()

        # Görselin adından başlık çıkar
        title_slug = re.sub(r'part-\d+-day-\d+-', '', image_path.stem).replace("-", " ").title()

        # Gerçek tarih hesabı
        day_match = re.search(r'day-(\d+)', image_path.stem)
        if day_match:
            day_num = int(day_match.group(1))
        else:
            day_num = (datetime.today() - start_date).days + 1

        # Markdown dosyasını oluştur
        md_folder = output_root / f"part-{part_num:03d}-cloud-support-track"
        md_folder.mkdir(parents=True, exist_ok=True)

        md_filename = f"-{title_slug.replace(' ', '-').lower()}-(day-{day_num}).md"
        md_path = md_folder / md_filename

        # Görseli klasöre kopyala ve isimlendir
        new_image_name = f"part-{part_num:03d}-day-{day_num:03d}-{title_slug.replace(' ', '-').lower()}.png"
        new_image_path = image_path.parent / new_image_name
        image_path.rename(new_image_path)

        # GitHub raw link
        raw_url = get_raw_github_url(series_folder.name, new_image_name)

        # Markdown içeriği
        md_content = f"""## Part {part_num:03d} – {title_slug} (Day {day_num})

### Goal
<!-- Write what you aimed to achieve in this part -->

---

### Technical Steps
<!-- List the steps you followed, commands you used, and how you implemented the task -->

---

### Outcome
<!-- Summarize the result, what worked, and what challenges you faced -->

<br>

![{title_slug} screen]({raw_url})
"""

        md_path.write_text(md_content, encoding="utf-8")
        print(f"✅ Created: {md_path}")
        print(f"🖼️ Raw image link embedded: {raw_url}")
