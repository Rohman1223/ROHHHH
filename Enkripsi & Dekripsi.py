def caesar_encrypt(plaintext, shift):
    encrypted = ""
    for char in plaintext:
        if char.isalpha():  # Memeriksa apakah karakter adalah huruf
            shift_base = ord('a') if char.islower() else ord('A')
            encrypted += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted += char  # Tidak mengubah karakter non-huruf
    return encrypted

def caesar_decrypt(ciphertext, shift):
    decrypted = ""
    for char in ciphertext:
        if char.isalpha():  # Memeriksa apakah karakter adalah huruf
            shift_base = ord('a') if char.islower() else ord('A')
            decrypted += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            decrypted += char  # Tidak mengubah karakter non-huruf
    return decrypted

# Fungsi utama
if __name__ == "__main__":
    while True:
        action = input("Apakah Anda ingin (1) Enkripsi atau (2) Dekripsi? (masukkan 1 atau 2): ")

        if action == '1':
            text = input("Masukkan teks untuk dienkripsi: ")
            shift = int(input("Masukkan jumlah pergeseran: "))
            encrypted_text = caesar_encrypt(text, shift)
            print("Teks Enkripsi:", encrypted_text)

        elif action == '2':
            text = input("Masukkan teks untuk didekripsi: ")
            shift = int(input("Masukkan jumlah pergeseran: "))
            decrypted_text = caesar_decrypt(text, shift)
            print("Teks Dekripsi:", decrypted_text)

        else:
            print("Pilihan tidak valid! Silakan pilih 1 atau 2.")

        continue_option = input("Apakah Anda ingin melanjutkan? (y/n): ").lower()
        if continue_option != 'y':
            print("Terima kasih! Program dihentikan.")
            break
