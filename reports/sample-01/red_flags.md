# Personal notes taken while checking Sample 01 - Fake Microsoft alert

While I looked through the email header and the body I found the following red flags:
- Sender IP: the email claims to be from Microsoft, but the sender IP (103.167.154.120) does not belong to Microsoft's official mail servers.
- Authentication Failure: SPF came back as none, DKIM did not find a valid signature key, and DMARC rejected it.
- From vs Reply-To: the 'From' header says the email is from 'no-reply@microsoft.com' but if the user decides to reply, the address switches to 'media-protection@usual-assist.com'.
- Social Engineering Pretext: while studying for the Security+ certification, I encountered different Social Engineering attacks example. An important thing during these attacks is to cause panic and a sense of urgency for the user, encouraging him to click on the link on the email.
- Hidden Trackers & Stuffing: I noticed a hidden 1x1 tracking pixel pointing to `sefnet.net` to track when the email is opened, plus a massive block of random dictionary words hidden in the CSS to mess with spam filters, even though they did not work since we saw earlier that DMARC rejected the email, putting it in the junk or spam folder anyway.
