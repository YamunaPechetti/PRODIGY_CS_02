from PIL import image

def encrypte_image(image_path,key):  #Encrypts an image by swapping pixel values based on a key
  image=Image.open(image_path)
  if image.mode!='RGB':   # Convert image to RGB if it's not already in that mode
    image=image.convert('RGB')
  pixels=image.load()
  width,height=image.size
  for x in range(width):
    for y in range(height):
      r,g,b=pixels[x,y]
      if (x+y) % key==0  # Swap red and blue channels based on the key
      pixels[x,y]=(b,g,r)
  encrypted_image_path="encrypted_"+image_path
  image.save(encrypted_image_path)
  return encrypted_image_path

def decrypt_image(image_path,key):  #Decrypts an encrypted image using the same key used for encryption.
  image=Image.open(image_path)
  if image.mode!='RGB':  # Convert image to RGB if it's not already in that mode
    image=image.convert('RGB')
    width,height=image.size
    for x in range(width):
      for y in range(height):
        r,g,b=pixels[x,y]
        if (x+y) % key ==0:  # Swap red and blue channels back based on the key
          pixels[x,y]=(b,g,r)
    decrypted_image_path="decrypted_"+image_path
    image.save(decrypted_image_path)
    return decrypted_image_path

if __name__=="__main__":
  import os
  
  image_path=input("Enter the path of the image file: ")
  if not os.path.exists(image_path):
    print(f"Error: the file {image_path} does not exist")
  else:
    key=int(input("Enter the key for encryption/decryption (an integer): "))
    
    encrypted_image_path=encrypt_image(image_path,key)  # Encrypt the image
    print(f"Encrypted image saved as {encrypted_image_path}")
    
    decrypt_image_path=decrypt_image(encrypted_image_path,key)  # Decrypt the image
    print(f"Decrypted image saved as {decrypted_image_path}")
