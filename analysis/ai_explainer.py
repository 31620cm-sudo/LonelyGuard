import requests
import json

def generate_explanation(data):

    payload = {
        "model": "llama-3.2-3b-instruct",
        "messages": [
            {
                "role": "user",
                "content": f"""
다음은 '1인 가구 고립 위험 감지 시스템'의 센서 데이터입니다. 
당신은 전문 안전 분석가이며 아래 정보를 기반으로 **한국어만 사용해**, 명확하고 분석적인 보고서를 작성하세요.

[센서 데이터]
- Motion: {data['motion']}
- Light: {data['light']}
- Temperature: {data['temperature']}°C
- Humidity: {data['humidity']}%
- Risk Score: {data['risk_score']}

[작성 규칙 — 절대 준수]
1) 답변은 **정확히 3문장**으로 구성  
2) 영어 단어 절대 사용 금지  
3) 중복·의미 반복 금지  
4) 번역투 금지 — 자연스러운 한국어 보고서 톤  
5) 데이터 기반 해석 포함  
6) 마지막 문장은 조치 또는 관찰 제안  

[출력 예시 형태]
- (1문장) 오늘 활동·환경 기반 위험도 평가  
- (2문장) 센서 값 분석 및 의미 해석  
- (3문장) 주의·관찰 필요 여부 제안  
"""
            }
        ],
        "temperature": 0.3
    }

    try:
        response = requests.post(
            "http://127.0.0.1:1234/v1/chat/completions",
            headers={"Content-Type": "application/json"},
            json=payload,
            timeout=30
        )

        result = response.json()
        return result["choices"][0]["message"]["content"].strip()

    except Exception as e:
        return f"[AI 분석 오류] {e}"
