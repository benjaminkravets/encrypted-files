Get-FileHash -Algorithm MD5 -Path (Get-ChildItem ".*" -Recurse) | Set-Content hashes.txt
