def rgb_hex():
  invalid_msg = "Error. Invalid Values Entered. Try Again."
  red = int(input("Enter red (R) value here: "))
  if red < 0 or red > 255:
    print(invalid_msg)
    return
  green = int(input("Enter green (G) value here: "))
  if green < 0 or green > 255:
    print(invalid_msg)
    return
  blue = int(input("Enter blue (B) value here: "))
  if blue < 0 or blue > 255:
    print(invalid_msg)
    return
  val = (red << 16) + (green << 8) + blue
  print("%s" % (hex(val)[2:]).upper())

def hex_rgb():
  hex_val = input("Enter hexadcimal value here: ")
  if len(hex_val) != 6:
    print("Error. Invalid value entered. Try Again")
    return
  else: 
    hex_val = int(hex_val, 16)
  two_hex_digits = 2 ** 8
  blue = hex_val % two_hex_digits
  hex_val = hex_val >> 8
  green = hex_val % two_hex_digits
  hex_val = hex_val >> 8
  red = hex_val % two_hex_digits
  print("Red: %s Green: %s Blue: %s" % (red, green, blue))

def convert():
  while True:
    option = input("Enter 1 to convert RGB to HEX. Enter 2 to convert HEX to RBG. Enter X to Exit: ")
    if option == '1':
      print("RGB to HEX...")
      rgb_hex()
    elif option == '2':
      print("HEX to RGB...")
      hex_rgb()
    elif option == 'X' or 'x':
      break
    else: 
      print("Error")


convert()
