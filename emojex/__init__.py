import openai

if __name__ == "__main__":
    def set_api_key(key):
        openai.api_key = key

    def get_emoji():
        prompt = "Back to Future: 👨👴🚗🕒\nBatman: 🤵🦇\nTransformers: 🚗🤖\nWonder Woman: 👸🏻👸🏼👸🏽👸🏾👸🏿\nWinnie the Pooh: 🐻🐼🐻\nThe Godfather: 👨👩👧🕵🏻‍♂️👲💥\nGame of Thrones: 🏹🗡🗡🏹\n" + text + ":"
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
