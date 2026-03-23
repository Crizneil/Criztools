$wshell = New-Object -ComObject WScript.Shell
$path = "c:\Users\ABC\OneDrive\Desktop\Projects\CrizTools\launch_criztools.lnk"
$shortcut = $wshell.CreateShortcut($path)
$shortcut.TargetPath = "python.exe"
$shortcut.Arguments = "`"c:\Users\ABC\OneDrive\Desktop\Projects\CrizTools\main.py`""
$shortcut.WorkingDirectory = "c:\Users\ABC\OneDrive\Desktop\Projects\CrizTools"
$shortcut.Description = "Launch CrizTools"
$shortcut.Save()

Write-Host "[+] Shortcut recreated at $path" -ForegroundColor Green
Write-Host "Target: $($shortcut.TargetPath) $($shortcut.Arguments)"
Write-Host "WorkDir: $($shortcut.WorkingDirectory)"
