## Part 003 — VM Networking

### Goal  
To understand how networking is handled within Azure Virtual Machines and to manually configure network components like Network Security Groups (NSGs), public IPs, and virtual network interfaces.

---

### Technical Steps  
1. Navigated to the Azure portal and selected the target Virtual Machine.  
2. Located and opened the "Networking" tab of the VM.  
3. Created a custom Network Security Group (NSG) named `cloud-journey-nsg`.  
4. Associated the NSG with the VM’s network interface.  
5. Added inbound rule to allow SSH traffic (Port 22) from a specific IP range.  
6. Verified existing default rules (Deny All Inbound / Allow All Outbound).  
7. Explored the effective security rules to confirm applied NSG behavior.

---

### Outcome  
Successfully linked a custom NSG to the VM and configured basic inbound/outbound rules. This laid the foundation for secure and controlled VM access through defined ports and protocols.

