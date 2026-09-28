# Personal notes taken while checking Sample 02 - Crypto-Drainer Phishing


- Display Name Spoofing: the sender is trying to look like MetaMask but after reviewing the `From` header we see that the email is originated by `@kommunal.se`
- The email was sent through a legitimate mass-marketing platform (`anpdm.com`). While this method managed to bypass the SPF and DKIM, MetaMask does not usually use third-party infrastructures to send out emails; this shows that the platform has been used maliciously.
- Social Engineering: the email is trying to convince users that their wallets are at immediate risk, and to press a button rather than verifying through official channels.
- Deceptive Hyperlink Destination: The "Press here to Upgrade" button points to a third-party shortener/redirect domain (`one-lnk.com`) instead of the official domain (`metamask.io`).
- Landing Page Objective: The redirection leads to a credential-harvesting or web3 wallet-drainer interface designed to steal secret recovery phrases (seed phrases) or private keys.
