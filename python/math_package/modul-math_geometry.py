def luas_persegi(sisi):
  """menghitung luas persegi"""
  return sisi * sisi

def luas_persegi_panjang(panjang, lebar):
  """menghitung luar persegi pangjang"""
  return panjang * lebar

def luas_segitiga(alas, tinggi):
  """menghitung luas segitiga"""
  return alas * tinggi / 2

def luas_lingkaran(radius):
  """menghitung luas lingkaran"""
  return 22 / 7 * radius * radius

def luas_trapesium(a, b, tinggi):
  """menghitung luas trapesium"""
  return a + b / 2 * tinggi

def keliling_persegi(sisi):
  """menghitung panjang keliling persegi"""
  return sisi * 4

def keliling_persegi_panjang(panjang, lebar):
  """menghitung panjang keliling persegi panjang"""
  return panjang + lebar * 2 

def keliling_segitiga(sisi_a, sisi_b, sisi_c):
  """menghitung panjang keliling segitiga"""
  return sisi_a + sisi_b + sisi_c

def keliling_lingkaran(radius):
  """menghitung panjang keliling lingkaran"""
  return 2 * 22 / 7 * radius

def keliling_trapesium(sisi_a, sisi_b, sisi_c, sisi_c):
  """menghitung panjang keliling trapesium"""
  return sisi_a + sisi_b + sisi_c + sisi_c
  
