### Part 006 — azure storage account temelleri (day 6)

this part lays the foundation for handling data during future migration tasks.

---

### Scenario

i’m preparing for a migration task where application files and logs must be stored on azure.  
to simulate this, i created a storage account and explored the available options to manage different data types: blobs, files, and tables.

---

### Goal

set up a basic storage account via the azure portal, and review the types of storage available for different scenarios.

---

### What you did

- opened azure portal and created a storage account  
- used the following configuration:  
  - resource group: rg-foundation001  
  - name: storbootcamp001  
  - region: france central  
  - performance: standard  
  - redundancy: lrs  
- explored:  
  - blob containers  
  - file shares  
  - tables  
  - queues

---

### Screenshot
![Storage Account](https://raw.githubusercontent.com/yavuzkutayozdemir/cloud-journey/main/gallery/cloud-support-track/part-006-day-006-azure-storage-account.png)

![Storage Account](https://raw.githubusercontent.com/yavuzkutayozdemir/cloud-journey/main/gallery/cloud-support-track/part-006-day-006-azure-storage-file-share.png)



---

### Outcome

- storage account successfully provisioned  
- blob, file, queue and table offerings reviewed  
- ui-based configuration completed without cli
