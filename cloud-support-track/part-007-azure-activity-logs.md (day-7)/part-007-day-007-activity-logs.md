Part 7 – Activity Logs (day-7)

Today, after setting up a virtual machine in Azure, I noticed that some resources were behaving unexpectedly. Specifically, there was a brief outage in external access to the application. To investigate, I navigated directly to the Activity Log section of the Azure portal.

The Activity Log provides a time-stamped record of all operations performed on Azure resources. It’s a critical tool for auditing and troubleshooting.

I applied filters to display only the entries related to my virtual machine, vm-support, and then narrowed the time window to focus on the most recent actions. One entry caught my attention:
	•	Action: ‘audit’ Policy action
	•	Status: Successful
	•	Initiated by: My user account
	•	Time: 16 minutes ago

This log entry helped me quickly realize that a policy applied to the virtual machine was limiting its network access. After reviewing the policy, I made the necessary adjustments and restored connectivity.

This was a real-world scenario where the built-in observability tools in Azure proved invaluable.

⸻

What I Learned
	•	Azure Activity Logs are essential for diagnosing operational issues and auditing changes across cloud resources.
	•	Filtering and time-scoping in the Activity Log helps pinpoint events with precision.
	•	Policy actions can silently impact the behavior of a resource, even if everything appears properly configured.
	•	Troubleshooting skills are not just technical—they also rely on understanding the right tools and interpreting what they reveal.
