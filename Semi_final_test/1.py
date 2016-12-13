import sys
string = sys.argv
if len(string[1:]) == 0:
  sys.exit(0)
end = 0
for i in string[1:]:
  if i.find('.') != -1:
    pass
  try:
    end += int(i)
  except:
    pass
sys.exit(end)