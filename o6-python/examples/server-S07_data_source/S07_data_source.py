#!/usr/bin/env python3
"""
Server Tutorial: Data Source Updates
=====================================

Demonstrates driving a Variable's value from an external process model
instead of assigning a constant. The pattern is: keep the "real" value in
plain Python state, and push it into the address space with `server.write()`
whenever it changes.

Note: the high-level API models this through explicit read/write rather
than a separate value-callback/data-source object — the loop below writes
after every state change, which is what a callback would have done for you.
"""

import os

import time
from o6 import Server

EXAMPLE_PORT = int(os.environ.get("O6_EXAMPLE_PORT", "4840"))



class ProcessModel:
    def __init__(self) -> None:
        self._temperature = 20.0

    def tick(self) -> None:
        self._temperature += 0.05

    def read_temperature(self) -> float:
        return self._temperature




def main() -> None:
    process = ProcessModel()
    with Server(port=EXAMPLE_PORT) as server:

        print("--- 1. Seed the variable ---")
        temp_node = server.addVariable(
            "ProcessTemperature",
            server.objectsNode,
            process.read_temperature(),
            nodeId="ns=1;s=ProcessTemperature",
        )
        print(f"Temperature = {server.read(temp_node)}")


        print("\n--- 2. Manual updates ---")
        for _ in range(5):
            process.tick()
            server.write(temp_node, process.read_temperature()).check()
            print(f"Temperature = {server.read(temp_node)}")
            time.sleep(0.2)

    print("\n=== Example completed ===")


if __name__ == "__main__":
    main()