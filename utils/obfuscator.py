# utils/obfuscator.py

import base64

def obfuscate_command(cmd: str) -> str:
    return base64.b64encode(cmd.encode()).decode()

def deobfuscate_command(encoded: str) -> str:
    return base64.b64decode(encoded.encode()).decode()

if __name__ == "__main__":
    sample = "whoami"
    encoded = obfuscate_command(sample)
    print(f"Obfuscated: {encoded}")
    print(f"Deobfuscated: {deobfuscate_command(encoded)}")
