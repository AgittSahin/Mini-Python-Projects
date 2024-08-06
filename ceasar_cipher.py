from ceasar_cipher_art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  shift_amount = shift_amount % 26
  if cipher_direction == "decode":
      shift_amount *= -1
  for letter in start_text:
      if letter in alphabet:  
        position = alphabet.index(letter)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
      else:
        end_text += letter
        
  print(f"Here's the {direction}d result: {end_text}")
  restart()
  
def restart():
    restart = input("Do you want to restart the Cipher program ? yes/no: ").lower()
    if restart == "yes":
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    else:
        print("Thank you for using the Cipher program")

caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
