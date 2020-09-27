main_string="c an u br ea k th is we ir d en cr yp ti on".split()

cipher_text = "eawethkthcrthcrthonutiuckirthoniskisuucthththcrthanthisucthirisbruceaeathanisutheneabrkeaeathisenbrctheneacisirkonbristhwebranbrkkonbrisbranthypbrbrkonkirbrciskkoneatibrbrbrbrtheakonbrisbrckoneauisubrbreacthenkoneaypbrbrisyputi"

is_div = True;
div = ""
mod = ""

plain_text = ""

index = 0
while (index < len(cipher_text)):
	letter = cipher_text[index]
	if (is_div):
		div += letter
		if (div == "c"):
			if (cipher_text[index+1] == 'r'):
				index += 1
				continue
		if (div in main_string):
			c1 = main_string.index(div)
			is_div = False
			div = ""
	else:
		mod += letter
		if (mod == "c"):
			if (cipher_text[index+1] == 'r'):
				index += 1
				continue
		if (mod in main_string):
			c2 = main_string.index(mod)
			is_div = True
			mod = ""

			plain_text += chr(c1*16 + c2)
	index += 1

print (plain_text)