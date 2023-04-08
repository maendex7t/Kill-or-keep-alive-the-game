# Kill-or-keep-alive-the-game
x=input("введите команду для первого человека:")
x2=input("введите команду для второго человека:")
x3=input("введите команду для третьего человека:")

class humans():
          def __init__(self,name):
          	self.name=name
          def kill(self):
          	print(f"{self.name} был убит")
          def keep_alive(self):
          	print(f"{self.name} был оставлен в живых")
          	
human_one=humans("первый человек")
human_two=humans("второй человек")
human_three=humans("третий человек")

while True:
 if x=="расстрелять":
  human_one.kill()
 if x=="оставить в живых":
  human_one.keep_alive()
 break

while True:
 if x2=="расстрелять":
  human_two.kill()
 if x2=="оставить в живых":
  human_two.keep_alive()
 break
 
while True:
 if x3=="расстрелять":
  human_three.kill()
 if x3=="оставить в живых":
  human_three.keep_alive()
 break
 
 
