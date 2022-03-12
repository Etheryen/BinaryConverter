def toDecimal(binary):
  result = 0

  for i in range(len(binary)):
    if binary[i] == '1':
      result += pow(2, len(binary)-i-1)

  return result

def toBinary(decimal):
  result = ''
  expo = 0
  # find nearest power of 2
  while(pow(2, expo) <= decimal):
    expo += 1
  expo -= 1

  while(decimal > 0 or expo >= 0):
    if(decimal >= pow(2, expo)):
      decimal -= pow(2, expo)
      result += '1'
    else:
      result += '0'
    expo -= 1

  return result