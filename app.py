import sys
!{sys.executable} -m pip install konlpy
from konlpy.tag import Okt

def calculate_ttr(text):
    okt = Okt()
    # 형태소 분석 및 품사 태깅
    morphemes = okt.pos(text, norm=True, stem=True)
    
    # 내용어(명사, 동사, 형용사)만 추출
    content_morphemes = [word for word, pos in morphemes if pos in ['Noun', 'Verb', 'Adjective']]
    
    if not content_morphemes:
        return 0.0, [], []

    total_tokens = len(content_morphemes)
    unique_types = set(content_morphemes)
    num_unique_types = len(unique_types)
    
    ttr = num_unique_types / total_tokens
    
    return ttr, list(unique_types), content_morphemes

print("TTR 계산 함수가 정의되었습니다.")
user_utterance = input("분석할 한국어 발화를 입력하세요: ")

ttr_value, types, tokens = calculate_ttr(user_utterance)

print(f"\n사용자 발화: {user_utterance}")
print(f"추출된 내용 형태소(토큰): {tokens}")
print(f"고유한 내용 형태소(타입): {types}")
print(f"총 토큰 수: {len(tokens)}")
print(f"고유 타입 수: {len(types)}")
print(f"TTR (Type-Token Ratio): {ttr_value:.4f}")
