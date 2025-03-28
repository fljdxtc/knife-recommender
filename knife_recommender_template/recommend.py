import joblib
import pandas as pd

model = joblib.load("model/model.pkl")
gender_encoder = joblib.load("model/gender_encoder.pkl")
knife_encoder = joblib.load("model/knife_encoder.pkl")
knife_df = pd.read_excel("data/菜刀编号.xlsx")

def recommend_knives(user_info):
    gender_code = gender_encoder.transform([user_info["性别"]])[0]
    predictions = []
    for _, row in knife_df.iterrows():
        knife_id = row["编号"]
        try:
            knife_code = knife_encoder.transform([knife_id])[0]
        except:
            continue
        features = [[
            gender_code,
            user_info["年龄"],
            user_info["身高"],
            user_info["体重"],
            knife_code
        ]]
        score = model.predict(features)[0]
        predictions.append({
            "编号": knife_id,
            "品牌": row["品牌名"],
            "链接": row["链接"],
            "预测得分": score
        })
    top3 = sorted(predictions, key=lambda x: x["预测得分"], reverse=True)[:3]
    return top3
