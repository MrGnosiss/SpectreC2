# SpectreC2

SpectreC2 is a **fileless Command & Control (C2)** framework built for advanced red teaming by **Mr. Axolotl (NulLNet)**.

## Features

- Fileless command execution
- Obfuscated traffic
- Base64-encrypted payloads
- Modular & lightweight
- Persistence for Windows & Linux
- Shodan-integrated target discovery (optional)

## Structure

spectrec2/
├── client/ # Payload logic
│ ├── client.py
│ └── persistence.py
├── server/ # Flask C2 backend
│ ├── server.py
│ └── controller.py
├── utils/
│ ├── encryptor.py
│ └── obfuscator.py
├── requirements.txt
└── README.md
