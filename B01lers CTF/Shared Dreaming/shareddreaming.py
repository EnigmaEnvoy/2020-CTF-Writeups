
# Hint 1: a1 XOR a2 XOR a3 XOR a4
s1 = "8ba4c4dfce33fd6101cf5c56997531c024a10f1dc323eb7fe3841ac389747fb90e3418f90011ef2610fa3636cd6cf0002d19faa30d39161fbd45cc58abff6a84"

# Hint 2: a2 XOR a3 XOR a4
s2 = "f969375145322aba697ce9b4e00aa88e81ffe5c306b1b98148f33c4581b2ac39bc95f13b27c39f2311a590b7e27cdbdb7599f615acd70c45378e44fb319b8cb6"

# Hint 3: a1 XOR a3
s3 = "855249b385f7b1d9923f71feb3bdee1032963ab51aa7b9d89a20c08c381e77890aa8849702d8791f8e636e833928ba6ea44c5f261983b7e29bd82e44b77fe03b"

# Ciphertext: flag XOR a3 XOR RandByte
s4 = "f694bc3d12a0673aead8fc4fdf964f5ec0c1d938e722bf333000f300088ead0dec1e7e03720331098068c13a066ca9bca89850a8ee67feb8471af5f47b4c0f13"

# XOR method
def xor_strings(xs, ys):
    return "".join(chr(ord(x) ^ ord(y)) for x, y in zip(xs, ys))

# XOR Hint 1 and Hint 2 to get a1
a1 = xor_strings(s1.decode("hex"), s2.decode("hex")).encode("hex")

# XOR a1 and Hint 3 to get a3
a3 = xor_strings(a1.decode("hex"), s3.decode("hex")).encode("hex")

# XOR a3 and Ciphertext to get flag XOR Randbyte
flag_rand = xor_strings(a3.decode("hex"), s4.decode("hex")).encode("hex")

# To find Randbyte, we XOR the first 4 bytes of the string obtained with "flag" in hex (as we know the flag usually starts with that)
flag_half = flag_rand[:8]
first = "666c6167" #"flag" in hex
rand_start = xor_strings(flag_half.decode("hex"), first.decode("hex")).encode("hex")
print (rand_start)

# Randbytes (needs to be 64 bytes) can be obtained by multiplying rand_start (4 bytes) by 16
rand = rand_start*16

# We XOR Randbytes with the flag_rand string to get the flag
flag = xor_strings(flag_rand.decode("hex"), rand.decode("hex")).encode("hex")
print (flag.decode("hex"))