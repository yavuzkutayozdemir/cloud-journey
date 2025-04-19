from pathlib import Path
import re

# Ayar: Klasörler
gallery_root = Path("gallery")
output_root = Path("cloud-support-track")

# gallery altındaki tüm görselleri bul
image_files = list(gallery_root.glob("**/part-*-day-*-*.png"))

for image_path in image_files:
    # Örn: part-003-day-003-vm-networking.png
    match = re.search(r'part-(\d+)-day-(\d+)-(.+)\.png', image_path.name)
    if not match:
        continue

    part_num = int(match.group(1))
    day_num = int(match.group(2))
    title_slug = match.group(3).replace("-", " ").title()
    title_raw = match.group(3)
    series = image_path.parts[1]  # Örn: cloud-support-track

    # Hedef dosya adı: part-003-cloud-support-track/-vm-networking (day-3).md
    md_filename = f"part-{part_num:03d}-{series}/-{title_raw} (day-{day_num}).md"
    md_path = output_root / md_filename

    if md_path.exists():
        print(f"SKIP: {md_path} already exists.")
        continue

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

![{title_slug} screen](../gallery/{series}/part-{part_num:03d}-day-{day_num:03d}-{title_raw}.png)
"""

    md_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.write_text(md_content, encoding="utf-8")
    print(f"✅ Created: {md_path}")
