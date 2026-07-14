# Moving a WSL Distro from C: to D:

Steps to relocate an existing WSL2 distro (e.g. `Ubuntu`) from the default `C:` install
location to another drive, based on what actually worked.

## Prerequisites

- Windows 11 with WSL updated to a recent version (`wsl --update`)
- Target drive has enough free space for the distro's VHDX
- PowerShell running **as Administrator**

## Step 1 — Identify the exact distro name

```powershell
wsl -l -v
```

Note the exact `NAME` value (case-sensitive) and confirm it shows `VERSION 2`.

## Step 2 — Shut down WSL fully

```powershell
wsl --shutdown
```

Wait a few seconds to make sure no `vmmem`/WSL process is still holding the VHDX open.

## Step 3 — Create the destination folder

```powershell
New-Item -ItemType Directory -Path D:\WSL -Force
```

## Step 4 — Run the move command (as Administrator)

```powershell
wsl --manage "Ubuntu" --move D:\WSL\Ubuntu
```

**Known quirk:** this command can report an error (`Access is denied` /
`The system cannot find the file specified`, error code
`Wsl/Service/MoveDistro/...`) even though it actually moves the VHDX file
successfully. Don't trust the error message alone — verify manually:

```powershell
Test-Path D:\WSL\Ubuntu\ext4.vhdx
```

If this returns `True` and the file size looks correct (check via File Explorer
or `Get-Item D:\WSL\Ubuntu\ext4.vhdx | Select Length`), the file move itself
succeeded even though the command reported failure.

## Step 5 — Fix the registry pointer (if the move "failed" but the file exists)

When the move command errors out, it can leave the Windows registry still
pointing at the old `C:` location, even though the file is already on `D:`.
Find the distro's registry key:

```powershell
Get-ChildItem "HKCU:\Software\Microsoft\Windows\CurrentVersion\Lxss" | ForEach-Object {
    Get-ItemProperty $_.PsPath
} | Where-Object { $_.DistributionName -eq "Ubuntu" }
```

Note the key's GUID (e.g. `{fa3f28b2-8404-4822-9206-8761d5d3ba51}`) and its
current `BasePath`. Update `BasePath` to the new location:

```powershell
Set-ItemProperty -Path "HKCU:\Software\Microsoft\Windows\CurrentVersion\Lxss\{<GUID>}" -Name "BasePath" -Value "D:\WSL\Ubuntu"
```

## Step 6 — Verify the distro boots from the new location

```powershell
wsl --shutdown
wsl -d Ubuntu
```

You should land in a normal shell prompt (`user@host:~$`) with your existing
username. Then confirm from inside the distro:

```bash
ls -la ~                 # home directory contents look correct
df -h /                  # root filesystem size matches the VHDX size
dpkg -l | wc -l          # installed package count looks right
cat /etc/wsl.conf        # default user / boot settings intact
```

Also from PowerShell, confirm the distro list looks healthy:

```powershell
wsl -l -v
```

Expect:
```
  NAME      STATE           VERSION
* Ubuntu    Running         2
```

## Step 7 — Clean up the old (now-empty) folder on C:

Only do this once you've confirmed your files, packages, and configs are all
present at the new location.

```powershell
Remove-Item "C:\Users\Panda 2.0\AppData\Local\wsl\{<GUID>}" -Recurse -Force
```

## Summary of gotchas learned

- `wsl --manage --move` requires an **elevated** PowerShell session — running
  without admin rights produces `Access is denied`.
- Even when run as Administrator, the command can report
  `ERROR_FILE_NOT_FOUND` / `E_ACCESSDENIED` while the underlying VHDX move
  actually completes — **always verify the file's presence at the
  destination before assuming failure.**
- If the move partially completes (file moved, registry not updated), fix it
  by manually editing the `BasePath` value in
  `HKCU:\Software\Microsoft\Windows\CurrentVersion\Lxss\{GUID}`.
- `wsl --export` / `wsl --import` is a more reliable fallback method if
  `--manage --move` cannot be made to work at all — it just requires more
  disk space temporarily (for the exported `.tar`).
