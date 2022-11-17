format_persen = f"persen = {persentase:.2%}"

print(format_persen)

# melakukan operasi aritmatika di dalam placeholder

harga = 10000
jumlah = 5
format_string = f"harga total = Rp. {harga*jumlah:,}"
print(format_string)

# format angka lain (binary, octal, hexadecimal)
angka = 255
format_binary = f"binary = {bin(angka)}"
format_octal = f"octal = {oct(angka)}"
format_hex = f"hex = {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hex)