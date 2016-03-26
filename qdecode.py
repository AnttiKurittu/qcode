#coding UTF-8
# This script will decode a qencoded message.
import sys
d = ""
while sys.stdin:
    # Reset 16 byte buffer
    e = ""
    # Gather 16 hexadecimal bytes.
    while len(e) < 16:
        # Read a byte from input.
        b = sys.stdin.read(1)
        # Terminate when stdin exhausted.
        if not b:
            # Get gathered bytes and decode from hex
            sys.stdout.write(d.decode('hex'))
            exit()
        # Get meaningful characters.
        elif b == "q" or b == "Q":
            # Add to buffer
            e = e + b
        # Strip other characters.
        else:
            continue
    else:
        # Count the number of upper case Q's in buffer
        c = e.count('Q')
        # Convert to a single hex digit
        a = hex(c)
        # Take two hex digits and combine to form a byte
        d = d + a[2]
        continue
