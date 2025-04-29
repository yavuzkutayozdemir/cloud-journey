### Issue Identified

While attempting to SSH into my Linux VM on Azure, I encountered persistent timeout errors. At first glance, everything looked fine — the VM was running, and a public IP was assigned.

Suspecting a firewall-related issue, I examined the **Network Security Group (NSG)** rules. Surprisingly, inbound SSH (port 22) traffic was already allowed, which ruled out the most common NSG misconfiguration.

I then confirmed that:
- The NSG was correctly associated with the network interface.
- The SSH rule had the right priority and protocol (TCP).
- No conflicting deny rules existed for port 22.

### Resolution

With the NSG verified, I shifted my focus to the VM itself:
- Validated the SSH daemon (`sshd`) was running.
- Ensured the user account and SSH key were configured properly.
- Verified the VM’s OS firewall wasn’t blocking port 22.

After confirming all system-level checks passed, I was able to successfully connect — the issue had been an invalid SSH key pair on my first attempt.

### What I Learned

- NSG misconfigurations are a frequent cause of SSH connectivity issues — but not the only one.
- It's important to trace connectivity problems methodically: from Azure infrastructure down to the OS layer.
- SSH issues might stem from user configuration mistakes, not just network settings.

### Screenshot

![NSG showing correct inbound SSH rule]([../gallery/part-008-day-011-nsg-verification.png](https://github.com/yavuzkutayozdemir/cloud-journey/blob/cc6b2d75caaa1d91d24700c3a1807893c5af0d6b/cloud-support-track/part-008-day-011-nsg-verification.md/part-008-day-011-nsg-verification.png))
