## Summary
<!-- What does this change do, and why? -->

Jira: KAN-
Type: feature / bug fix / security fix / infrastructure / dependency update / emergency fix

## Privacy (SDLC policy section 7)
- [ ] Privacy screening answered on the Jira ticket
- [ ] Touches personal data or ePHI: No / Yes, and privacy review signed off on the ticket
- [ ] New third party, SDK, analytics event or cloud service: No / Yes, reviewed (BAA in place if it may receive ePHI)
- [ ] Data Inventory and Data Flows page updated if data flows, retention or region changed

## Security (SDLC policy section 5)
- [ ] New or changed endpoints authenticate the caller and check permission server-side
- [ ] Tenant, organization and user IDs come from the verified token, not the request body
- [ ] No secrets, keys, tokens or connection strings in code, config, fixtures or commits
- [ ] Input validated on the server; queries parameterized; output encoded
- [ ] Nothing sensitive logged (no tokens, passwords, request bodies or ePHI)
- [ ] New connections use TLS 1.2+ with certificate verification
- [ ] New IAM permissions are least privilege (no wildcards on sensitive services)
- [ ] Dependencies pinned; no new Critical or High vulnerabilities

## Testing
- [ ] Automated tests added or updated
- [ ] Verified in dev or staging with test data only (no production data)
- [ ] CI checks pass (tests, dependency scan, secret scan)

How it was tested:
<!-- Steps, environment, screenshots -->

## Release
- [ ] Infrastructure changes are in IaC (no console-only changes)
- [ ] Customer documentation or privacy notice updated if behavior changes

Rollback plan:
<!-- How to undo this change if something goes wrong -->

## Emergency fix only
<!-- Incident ticket, who approved the early deploy, and the post-deploy review date (within 2 business days, SDLC policy section 4) -->
