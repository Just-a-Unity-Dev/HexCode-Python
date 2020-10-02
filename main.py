# Read's the hex file, which opens code.hex
f = open("read.hex", "r")
fName = f.read()
# The Interpreter start's here

with open(fName) as f:
        content = f.readlines()
        content = [x.strip() for x in content]

# This is the main code, this actually runs everything
for x in content:
  hex_string = x

  bytes_object = bytes.fromhex(hex_string)

  ascii_string = bytes_object.decode("ASCII")
  exec(ascii_string)

exit
