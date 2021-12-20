def gen_input():
  f = open('inp20.txt')
  algo = f.readline().lstrip().rstrip()
  inp_image = ['.' + x.lstrip().rstrip() + '.' for x in f.readlines() if x.lstrip().rstrip()]

  inp_image.append('.' * len(inp_image[0]))
  inp_image.insert(0, '.' * len(inp_image[0]))
  return [inp_image, algo]

def gen_output_img(inp_image):
  output_image = []
  for r in inp_image:
    x = []
    for c in r:
      x.append('.')
    output_image.append(x)
  return output_image

def num_of_lights(n, inp_image, output_image, algo):
  cur_filler = '.'
  for k in range(n):
    for i in range(len(inp_image)):
      for j in range(len(inp_image[i])):
        row = ''
        if i - 1 < 0 or j - 1 < 0:
          row += cur_filler
        else:
          row += inp_image[i - 1][j - 1]

        if i - 1 < 0:
          row += cur_filler
        else:
          row += inp_image[i - 1][j]

        if i - 1 < 0 or j + 1 > len(inp_image[i]) - 1:
          row += cur_filler
        else:
          row += inp_image[i - 1][j + 1]

        if j - 1 < 0:
          row += cur_filler
        else:
          row += inp_image[i][j - 1]

        row += inp_image[i][j]

        if j + 1 > len(inp_image[i]) - 1:
          row += cur_filler
        else:
          row += inp_image[i][j + 1]

        if i + 1 > len(inp_image) - 1 or j - 1 < 0:
          row += cur_filler
        else:
          row += inp_image[i + 1][j - 1]

        if i + 1 > len(inp_image) - 1:
          row += cur_filler
        else:
          row += inp_image[i + 1][j]

        if i + 1 > len(inp_image) - 1 or j + 1 > len(inp_image[i]) - 1:
          row += cur_filler
        else:
          row += inp_image[i + 1][j + 1]
        output_image[i][j] = algo[int('0b' + row.replace('.', '0').replace('#', '1'), base=2)]
    if cur_filler == '.':
      cur_filler = algo[0]
    else:
      cur_filler = algo[-1]
    inp_image = []
    for r in output_image:
      inp_image.append(cur_filler + ''.join(r) + cur_filler) 
    inp_image.append(cur_filler * len(inp_image[0]))
    inp_image.insert(0, cur_filler * len(inp_image[0]))
    output_image = [[y for y in x] for x in inp_image]

  light = 0
  for row in output_image:
    light += row.count('#')
  return light

inp_image, algo = gen_input()
output_image = gen_output_img(inp_image)
print('First part:', num_of_lights(2, inp_image, output_image, algo))

inp_image, algo = gen_input()
output_image = gen_output_img(inp_image)
print('Second part:', num_of_lights(50, inp_image, output_image, algo))
