import openai


def set_api_key(key):
    openai.api_key = key

def get_emoji(text, max_tokens=30):
    prompt = "Back to Future: π¨π΄ππ\nBatman: π€΅π¦\nTransformers: ππ€\nWonder Woman: πΈπ»πΈπΌπΈπ½πΈπΎπΈπΏ\nWinnie the Pooh: π»πΌπ»\nThe Godfather: π¨π©π§π΅π»ββοΈπ²π₯\nGame of Thrones: πΉπ‘π‘πΉ\n" + text + ":"
    engine = "davinci"

    response = openai.Completion.create(
        engine=engine,
        prompt=prompt,
        temperature=0.6,
        max_tokens=max_tokens,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["\n"]
    )

    return response["choices"][0]["text"]

if __name__ == "__main__":
    def set_api_key(key):
        openai.api_key = key

