inp = [x.lstrip().rstrip() for x in open('inp17.txt').readline().replace('target area: ', '').split(',')]
target_area = [[int(y) for y in x.replace('x=', '').replace('y=', '').split('..')] for x in inp]

"""
  It's not necessarry to write a program for the 1st part since it can be calculated by hand
  To maximize the height take the bottommost y coordinate of the target area and calculate the vertical
  distance from S. Let this distance be d.
  Also, the x velocity is unimportant, all we have to find is a value that becomes 0 inside the target area
  so that after that only the y velocity changes
  Ideally, the last step should be d units downwards so that we still reach the bottommost point of the
  target area and maximize the height of the trajectory
  If the last step was d then it took d - 1 steps to reach the x coordinate of S which equals the first
  step we took which equals the initial y velocity
  In the problem d is 92 so by the Gauss formula the maximum height is 91 * 92 / 2 = 4186
"""

print('First part:', 4186)

"""
  The minimum x velocity (n) is a number such that 2 * 277 <= n^2 + n, n is a natural number
"""

def is_point_inside(x, y):
  return target_area[0][0] <= x <= target_area[0][1] and target_area[1][0] <= y <= target_area[1][1]

min_x_velocity = 24
max_x_velocity = 318
max_y_velocity = 92
min_y_velocity = -92

cnt = 0
vels = []
for i in range(min_x_velocity, max_x_velocity + 1):
  for j in range(min_y_velocity, max_y_velocity + 1):
    x_vel = i 
    y_vel = j
    pos = [0, 0]
    collided = False
    never_reach = False
    while not (collided or never_reach):
      pos[0] += x_vel
      pos[1] += y_vel
      collided = is_point_inside(pos[0], pos[1])
      never_reach = pos[1] < target_area[1][0] or pos[0] > target_area[0][1]
      if collided:
        cnt += 1
        vels.append((i, j))
      if x_vel > 0:
        x_vel -= 1
      y_vel -= 1
print('Second part:', cnt)
