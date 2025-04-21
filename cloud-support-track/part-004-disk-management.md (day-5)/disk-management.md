# Part 004 – Disk Management in Azure (day-5)

## 🎯 Goal

Attach a data disk to an existing Azure Virtual Machine using **only the Azure Portal (UI)** — no terminal or CLI.

---

## 📍 Scenario

You’ve been asked to attach a persistent storage disk to an existing Linux VM for application logs or data storage. The disk must be created and attached using only the Azure Portal.

---

## 🔧 What You Did

1. Navigated to your VM (`vm-foundation001`) in Azure Portal  
2. Selected the **Disks** blade  
3. Clicked **+ Add data disk** → then **Create disk**  
4. Entered:  
   - Name: `datadisk-001`  
   - Size: `4 GiB`  
   - Type: `Standard HDD`  
   - Region: France Central  
5. Clicked **Create**, then saved changes  
6. Verified the disk shows up as `Attached`

---

## 📸 Screenshot

![Disk Management](https://raw.githubusercontent.com/yavuzkutayozdemir/cloud-journey/main/gallery/cloud-support-track/part-004-day-005-disk-management.png)

---

## ✅ Outcome

The disk is now successfully attached to the VM via UI, without any terminal commands. It is ready for OS-level mounting if needed.

---

## 💡 What I Learned

- How to attach and configure a data disk in Azure Portal  
- Difference between OS and data disks  
- Using only UI for infrastructure changes
