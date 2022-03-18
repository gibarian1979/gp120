python
for i in range(1, 37):
 cmd.draw(1024, 768)
 cmd.png('/tmp/%03d.png'%i)
 cmd.turn('y', 10)
python end
