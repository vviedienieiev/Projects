import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for symb in start_text:
    if symb not in alphabet:
      end_text += symb
    else:
      position = alphabet.index(symb)
      shift = position + shift_amount
      print(shift%len(alphabet))
      if shift >= 0:
        new_position = (position + shift_amount)%(len(alphabet))
      else:
        new_position = len(alphabet)-abs(shift)%(len(alphabet))
        if new_position == 26:
          new_position = 0
      print(f"Letter: {symb}, New position: {new_position}")
      end_text += alphabet[new_position]
    
  print(f"Here's the {cipher_direction}d result: {end_text}")

print(art.logo)

restart = True
while restart:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  if input("Do you want to restart?\n").lower() != "yes":
    restart = False 
