from typing import List, Union


class Stdin:
    @staticmethod
    def input(word, num=False):
        ask: bool = True
        input_type: str = "数値" if num else "文字"

        while ask:
            input_val: str = input(word)

            if num and input_val.isdecimal():
                input_val: int = int(input_val)
                break
            elif not num and not input_val.isdecimal():
                break
            else:
                print(f"{input_type}を入力してください!")

        return input_val

    @classmethod
    def get_response(
        cls,
        word: str,
        response: List[str] = ["Yes", "No"]
    ) -> Union[str, None]:
        response_word: str = cls.input(
            f"{word} {response[0]}/{response[1]} : "
        ).lower()

        if (
            response_word == response[0].lower() or
            response_word == response[0][0].lower()
        ):
            return True
        elif (
            response_word == response[1].lower() or
            response_word == response[1][0].lower()
        ):
            return False
        else:
            print("指定された文字を入力してください！")
