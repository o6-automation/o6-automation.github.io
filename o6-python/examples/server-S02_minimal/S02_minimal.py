#!/usr/bin/env python3
# Copyright 2026 (c) o6 Automation GmbH
"""
Minimal OPC UA Server
=====================

The smallest possible server – just 6 lines of code.
Starts an OPC UA server on port 4840 and runs until Ctrl+C.

    opc.tcp://localhost:4840
"""


import os

import time
from o6 import Server

EXAMPLE_PORT = int(os.environ.get("O6_EXAMPLE_PORT", "4840"))

server = Server(port=EXAMPLE_PORT)
server.start()

print(f"Server running at opc.tcp://localhost:{EXAMPLE_PORT}")
print("Press Ctrl+C to stop.")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Shutting down...")

server.stop()
print("Server stopped.")