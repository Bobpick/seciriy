import cirq
import numpy as np
import qrcode

def generate_random_key(length):
    """Generate a random binary key of given length."""
    return np.random.randint(2, size=length)

def quantum_one_time_pad(binary_data, key):
    """Performs quantum one-time pad decryption on binary strings."""
    if len(binary_data) != len(key):
        raise ValueError("Key length doesn't match encrypted data length.")

    # Convert binary strings to lists of integers
    binary_data = [int(bit) for bit in binary_data]
    key = [int(bit) for bit in key]
    return [(a ^ b) for a, b in zip(binary_data, key)]

def message_to_binary(message):
    return [int(b) for b in ''.join(format(ord(c), '08b') for c in message)]

def binary_to_message(binary_data):
    chars = [chr(int(''.join(map(str, binary_data[i:i+8])), 2)) for i in range(0, len(binary_data), 8)]
    return ''.join(chars)

def main():
    choice = ""
    while True:
        print("\nMenu:")
        print("1. Encrypt Message")
        print("2. Decrypt Message")
        print("3. Generate 10 Keys")
        print("4. Exit")

        choice = input("Enter your choice: ")

        # Sanitize the input
        choice = ''.join(filter(str.isdigit, choice))
        if not choice:
            print("Invalid choice. Please enter a number.")
            continue

        encrypted_str = ""
        key_str = ""

        if choice == '1':
            message = input("Enter message to encrypt: ")
            binary_message = message_to_binary(message)

            # Limit message to 2048 characters (approximately 2KB)
            if len(binary_message) > 2048:
                print("Error: Message exceeds maximum length of 2048 characters.")
                continue
            
            key = generate_random_key(len(binary_message))
            encrypted_data = quantum_one_time_pad(binary_message, key)
            # QR Code Generation
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(''.join(map(str, key)))  # Add the key as data to the QR code
            qr.make(fit=True)

            img = qr.make_image(fill_color="black", back_color="white")
            img.save("key_qrcode.png")  # Save the QR code image
            print("Key QR code saved as key_qrcode.png")
            print(f"Encrypted data (binary): {encrypted_data}")
            print(f"Key (share this with the recipient): {''.join(map(str, key))}") 
        elif choice == '2':
            while True:  # Loop until lengths match
                encrypted_str = input("Enter encrypted data (binary): ")
                key_str = input("Enter key (binary): ")

                # Remove any non-binary characters and spaces
                encrypted_str = ''.join(filter(lambda x: x in '01', encrypted_str))
                key_str = ''.join(filter(lambda x: x in '01', key_str))

                # Display lengths for debugging
                print(f"Encrypted data length: {len(encrypted_str)}")
                print(f"Key length: {len(key_str)}")

                if len(encrypted_str) != len(key_str):
                    print("Error: Key length doesn't match encrypted data length. Please try again.")
                else:
                    break  # Exit the loop if lengths match

            try:
                encrypted_data = [int(bit) for bit in encrypted_str]
                key = [int(bit) for bit in key_str]
            except ValueError:
                print("Error: Invalid input format. Please use only 0s and 1s.")
                continue

            decrypted_data = quantum_one_time_pad(encrypted_data, key)
            decrypted_message = binary_to_message(decrypted_data)
            print(f"Decrypted message: {decrypted_message}")

        elif choice == '3':
            key_length = int(input("Enter desired key length (in bits): "))
            for _ in range(10):
                key = generate_random_key(key_length)
                print(f"Key: {key}")
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
