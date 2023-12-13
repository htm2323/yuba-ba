import random as rnd
import time

class Yubaba:
    def check_validation_name(self, input_name) -> bool:
        if (input_name == ""):
            return False
        return True
    
    def reaction(self, input_name) -> str:
        if (self.is_gorgeous_name(input_name)):
            reaction = input_name + "というのかい。贅沢な名だね。"
        return reaction
    
    def rename(self, input_name) -> str:
        new_name = self.random_select_charactor(input_name)
        return_message = "今日からお前の名は… " + new_name + " だ。わかったら返事しな、" + new_name + " !"
        return return_message
    
    def random_select_charactor(self, input_name) -> str:
        use_char_count = rnd.randint(1, len(input_name) - 2)
        new_name = ""

        for i in range(use_char_count):
            select_char_idx = rnd.randint(0, len(input_name) - 1)
            new_name = new_name + input_name[select_char_idx]
        
        return new_name
    
    def is_gorgeous_name(self, input_name) -> bool:
        return True
    
yubaba = Yubaba()
print("ここで働きたいのかい。いいよ、ここに名前を書きな")
while True:
    input_name = ""
    input_name = input()
    if (yubaba.check_validation_name(input_name)):
        print(yubaba.reaction(input_name))
        print(yubaba.rename(input_name))
        time.sleep(0.2)
        print("また人間が来たのかい。珍しいねえ。ここに名前を書きな")

    else:
        print("ちゃんとした名前を書きな！")