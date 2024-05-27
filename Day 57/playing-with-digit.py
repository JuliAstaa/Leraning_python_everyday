def dig_pow(n, p):
    # Ubah n menjadi string untuk memudahkan iterasi melalui digit-digitnya
    digits = list(map(int, str(n)))

    # Hitung jumlah dari digit-digit yang dipangkatkan secara berturut-turut mulai dari p
    total_sum = sum(d ** (p+ i) for i, d in enumerate(digits))

    # Periksa apakah total_sum dapat dibagi dengan n tanpa sisa
    if total_sum % n == 0 :
      return total_sum // n
    else :
        return - 1

print(dig_pow(41, 5))

