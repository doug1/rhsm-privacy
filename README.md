# rhsm-privacy
Privacy plugin for Red Hat Subscription Manager to redact
sensitive facts before sending to Red Hat.

When running yum/dnf updates, the Red Hat Subscription Manager client
plugin gathers facts about your server including hostname, IP addresses,
MAC addresses, assets tags, and product model/serial numbers and sends
this information to Red Hat to be stored in their subscription database.

This information is used on the system info pages in the Red Hat Customer
Portal, but some people may be uncomfortable giving so much info to Red
Hat without an explicit per-system opt-in.

The rhsm-privacy allows you to redact specific facts (key-value pairs)
before they are sent to the Red Hat Customer Portal database.

