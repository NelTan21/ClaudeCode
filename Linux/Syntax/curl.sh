curl -L https://example.com/file.zip -o file.txt # This command uses curl to download a file from the specified URL (https://example.com/file.zip) and saves it as file.txt in the current directory. The -L option tells curl to follow any redirects that may occur during the download process.
curl https://example.com                    # fetch a URL and print the response to the terminal
curl -O https://example.com/file.txt        # download and save it as file.txt (keeps the original filename)
curl -o myname.txt https://example.com/f.txt # download and save it under a custom filename
curl -sS https://webi.sh/lsd | sh           # download a script and pipe it straight into sh to run it (this is how you installed lsd)
curl -I https://example.com                 # fetch only the response headers (no body) — useful for checking if a URL is alive
curl -L https://example.com                 # follow redirects (some URLs redirect elsewhere; -L makes curl follow along)

# Examples of different protocols that curl can handle:
curl https://example.com/file.txt      # HTTP/HTTPS -- web servers
curl ftp://example.com/file.txt        # FTP -- file transfer servers
curl sftp://example.com/file.txt       # SFTP -- FTP over SSH
curl file:///home/user/file.txt        # local filesystem, no network at all
curl smtp://mail.example.com --mail-from=... # SMTP -- sending mail directly