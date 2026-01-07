def add(a, b):
  """Menambahkan dua angka"""
  return a + b

def subtract(a, b):
  """Mengurangi dua angka"""
  return a - b

def multiply(a, b):
  """Mengalikan dua angka"""
  return a * b

def divide(a, b): 
  """Membagi dua angka"""
  if b == 0:
    raise ValueError("tidak dapat membagi dengan angka nol!") 
  return a / b


