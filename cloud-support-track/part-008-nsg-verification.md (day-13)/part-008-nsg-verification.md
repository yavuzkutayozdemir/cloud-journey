# Part 008 — NSG Verification

### Goal
Diagnose and resolve SSH access issues caused by misconfigured NSG associations in Azure.

---

### Issue Identified
Today, I was troubleshooting why I couldn’t SSH into my Azure VM. The public IP was active, the VM was running, and port 22 was supposed to be open. Yet, every attempt timed out.

Diving deeper, I reviewed the Network Security Group (NSG) attached to the VM’s NIC. Despite all seeming well, I noticed the SSH rule had a low priority (300) — but it still wasn’t taking effect.

---

### Resolution
After checking the NSG rules again, I realized the rule was indeed correct, but I hadn’t associated the NSG properly with the right interface. I rechecked the association and ensured the NSG was linked to both the subnet and NIC properly. SSH access was instantly restored.

---

### What I Learned
- Azure NSG rules are priority-based; order matters  
- NSG association must be verified at both subnet and NIC levels  
- Sometimes the issue isn’t the rule itself — it’s where it applies  

---

### Screenshot
![NSG Rule Troubleshooting](https://github.com/yavuzkutayozdemir/cloud-journey/blob/3719f8ab2877363e2b4d602766a715c5f5b9da0a/cloud-support-track/part-008-nsg-verification.md%20(day-13)/part-008-day-013-nsg-verification.png)
