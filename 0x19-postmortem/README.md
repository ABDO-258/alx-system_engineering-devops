0x19-postmortem

issue Summary
Duration:
Start Time: Mar 5, 2024 12:00 (GMT)
End Time: Mar 5, 2024 13:00 (GMT)
Impact:
The web service experienced downtime, resulting in connection errors for users.
Approximately 20% of users were affected during the outage.
The Apache service on the Ubuntu container was down, resulting in 500 error which mean no access to the website.
Root cause:
a typo in wp-setting file 
Timeline
Detection:
The issue was detected at  Mar 5, 2024 12:00 (GMT) through automated monitoring alerts.
Actions Taken:
Investigated server logs for any unusual activity or errors.
Assumed the issue might be related to a recent deployment.
Resolution:
Using tmux to run strace in one window and curl in another one
Restarted the necessary services toaster fixing the typo.
Root Cause and Resolution
Root Cause:
A recent code deployment introduced an unforeseen bug, causing the application to crash under certain conditions.
Corrective and Preventative Measures
Improvements/Fixes:
create an environment for testing  .
Strengthen monitoring for application health and performance.
Tasks:
Conduct a thorough review of the deployment process to ensure code changes are adequately tested before release.
Implement a post-deployment validation step to verify the stability of the application.
In conclusion, the unexpected downtime was promptly addressed by fixing the setting file a stable version and implementing additional testing measures. The incident underscores the importance of thorough testing in the deployment process and ongoing vigilance through robust monitoring.
