 Goal

Use Azure Activity Logs to identify and resolve unexpected changes to a virtual machine resource via the Azure Portal (no CLI used).

⸻

 Problem

While testing my Linux VM, I suddenly lost remote access. No recent changes were made by me, and the VM appeared healthy in the portal. This unexpected behavior suggested that an automated policy or background action might have silently affected my network settings.

⸻

 What I Solved

By digging into the Azure Activity Logs, I discovered that a policy enforcement action ('audit' Policy action) had modified the virtual network configuration. Recognizing it was automatically applied by the subscription’s default governance rules, I updated the VM’s configuration accordingly and restored access without downtime.

⸻

 Scenario

After setting up a Linux VM in Azure, I noticed unusual behavior — external access was temporarily disrupted. Suspecting a configuration issue, I explored the Activity Logs to investigate what had happened behind the scenes.

⸻
 What You Did
	1.	Opened the Azure Portal and navigated to the VM named vm-support
	2.	Clicked on Activity Log in the left-hand menu
	3.	Filtered logs by:
	•	Time range: Last 6 hours
	•	Resource: vm-support
	•	Subscription: Azure for Students
	4.	Found a relevant event:
	•	Action: 'audit' Policy action
	•	Status: Successful
	•	Initiated by: My user ID
	5.	Realized a network restriction policy had been enforced
	6.	Adjusted the policy to restore connectivity

⸻

 What I Learned
	•	How to interpret and filter Azure Activity Logs to trace system-level events
	•	The role of policy assignments and their hidden impact on deployed resources
	•	That visibility into past actions is key for maintaining uptime and accountability
	•	Real-life debugging often starts with the question: “What changed?”

⸻

 Screenshot
 
