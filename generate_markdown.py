from pathlib import Path
import re
from datetime import datetime

# Settings
gallery_root = Path("gallery")
output_root = Path("cloud-support-track")
global_counters_file = Path("global_counters.txt")

# Initialize global counters
if global_counters_file.exists():
    lines = global_counters_file.read_text().splitlines()
    part_counter = int(lines[0])
else:
    part_counter = 1

# Base date for day count
start_date = datetime(2025, 4, 17)

for series_folder in gallery_root.iterdir():
    if not series_folder.is_dir():
        continue

    image_files = list(series_folder.glob("*.png"))
    for image_path in image_files:
        match = re.search(r'part-(\d+)-day-(\d+)-(.+).png', image_path.name)
        if not match:
            continue

        part_num = part_counter
        part_counter += 1

        day_str = match.group(2)
        day_date = start_date + timedelta(days=int(day_str) - 1)
        day_num = (day_date - start_date).days + 1

        title_raw = match.group(3)
        title_slug = title_raw.replace("-", " ").title()
        series = series_folder.name

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

![{title_slug} screen](../../gallery/{series}/part-{part_num:03d}-day-{day_num:03d}-{title_raw}.png)
"""

        md_path.parent.mkdir(parents=True, exist_ok=True)
        md_path.write_text(md_content, encoding="utf-8")
        print(f"✅ Created: {md_path}")

# Save updated global counter
global_counters_file.write_text(f"{part_counter}\n")