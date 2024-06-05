# Quantum One-Time Pad (QOTP) Simulator

A Python-based simulation of the Quantum One-Time Pad (QOTP) encryption scheme, demonstrating the principles of quantum cryptography using Cirq.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [How to Use](#how-to-use)
- [Important Notes](#important-notes)
- [Disclaimer](#disclaimer)

## Introduction

The Quantum One-Time Pad (QOTP) is a theoretically unbreakable encryption method that leverages the principles of quantum mechanics. It utilizes a random key, equal in length to the message, to encrypt the message.  Each bit of the message is combined with the corresponding bit of the key using the XOR (exclusive OR) operation.

This project simulates the QOTP process using classical bits and operations. It serves as an educational tool to understand the concepts behind QOTP and its security properties.
## Features

- **Encryption:** Encrypts text messages into binary format using a randomly generated key.
- **Decryption:** Decrypts binary encrypted messages using the correct key.
- **Key Generation:** Generates random binary keys of user-specified length.
- **Menu-Driven Interface:** Provides a user-friendly menu for selecting encryption, decryption, key generation, or exiting the program.
- **Input Validation:** Handles invalid input and ensures key and message length compatibility.
- **Key Display:** Prints keys as single, continuous binary strings for easy copying and sharing.

## Requirements

- Python 3.x (recommended)
- Cirq library (Install using: `pip install cirq`)

## How to Use

1.  **Clone the Repository:**
    ```bash
    git clone <repository_url>
    ```

2.  **Install Dependencies:**
    ```bash
    pip install cirq
    ```

3.  **Run the Script:**
    ```bash
    python quantum_otp.py
    ```

4.  **Choose Options from the Menu:**
    -   **Encrypt Message (1):**
        -   Enter the message you want to encrypt.
        -   The script will generate a random key, encrypt the message, and display the encrypted binary data.
        -   A QR code image (`encrypted_message_qrcode.png`) shown above, containing the encrypted messsage will be generated and saved in the same directory as the script. Share this image with the recipient for decryption.

        ![Encrypted Message QRCode](https://github.com/Bobpick/seciriy/blob/main/key_qrcode.png)

    -   **Decrypt Message (2):**
        -   Enter the encrypted binary data as a single, continuous string (e.g., `01011010...`).
        -   Enter the corresponding key (also as a single, continuous binary string).
        -   The script will decrypt the message and display the original text.

    -   **Generate Keys (3):**
        -   Enter the desired key length in bits.
        -   The script will generate and display 10 random keys of the specified length.

    -   **Exit (4):**
        -   Quits the program.

## Important Notes

-   This is a simulation and does not provide the full security guarantees of a real QOTP implemented with quantum hardware and quantum key distribution (QKD).
-   In a real-world QOTP, the key must be truly random and shared securely via QKD.
-   Never reuse a key for multiple messages, as this would compromise the security of the OTP.
-   The maximum message length is limited to 2048 characters (approximately 2KB) due to the computational limitations of this simulation.

## Disclaimer

This project is for educational and demonstrative purposes only. It should not be used for actual secure communication where confidentiality is critical. A real-world QOTP implementation with quantum hardware and QKD is required for true quantum-level security.
