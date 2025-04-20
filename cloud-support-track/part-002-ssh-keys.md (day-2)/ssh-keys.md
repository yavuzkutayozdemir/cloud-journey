## Part 002 — SSH Keys

### Goal  
Authenticate to virtual machines securely without using passwords, by generating and using SSH key pairs.

---

### Technical Steps  
1. Create a key pair: `ssh-keygen -t rsa -b 2048`  
2. Upload the public key to Azure or any remote VM  
3. Use the private key to connect: `ssh -i ~/.ssh/id_rsa user@vm-ip`  

---

### Outcome  
Passwordless SSH login was established with the VM using a generated key pair.  
<br>  
![ssh key ekranı](gallery/cloud-support-track/part-002-day-002-ssh-keys.png)
