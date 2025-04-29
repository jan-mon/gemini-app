import streamlit as st
import google.generativeai as genai

# あなたのAPIキーをここに
API_KEY = "AIzaSyA6kLTVaYgIVvCa1gSyJce-M0NtnIS2ip0"

# Gemini設定（ここは後で設定するので一旦そのまま）
genai.configure(api_key=API_KEY)

# Streamlitアプリスタート
st.title("💡 アイデア量産マシン（温度調整版）")

# スライダーでtemperatureを選ぶ
temperature = st.slider(
    "Temperature（ランダム度）を選んでください", 
    min_value=0.0, 
    max_value=2.0, 
    value=0.9, 
    step=0.1
)

# スライダーでtop_pを選ぶ
top_p = st.slider(
    "Top-p（確率の幅）", 
    min_value=0.1, 
    max_value=1.0, 
    value=0.9, 
    step=0.05
)

# テーマ入力欄
theme = st.text_input("テーマを入力してください")

# ボタンを押すと実行
if st.button("アイデアを生成！"):
    if theme:
        with st.spinner("考え中..."):
            # ここで、選んだtemperatureを反映する！
            model = genai.GenerativeModel(
                model_name="gemini-2.0-flash",
                generation_config=genai.types.GenerationConfig(
                    temperature=temperature,
                    top_p=top_p
                )
            )
            prompt = f"「{theme}」に関する面白いアイデアを10個、箇条書きで出してください。"
            response = model.generate_content(prompt)
            st.success("できた！")
            st.write(response.text)
    else:
        st.warning("テーマを入力してください。")
