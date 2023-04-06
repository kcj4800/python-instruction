__all__ = ['module1'] 

# __init__.py : Python3.3 부터는 없어도 패키지로 인식 -> 단, 하위 호환을 위해 작성 추천
# __all__ = ['module1'] => 외부에서 module1에 접근할수 있도록 허락해주는 역할
# 만약 module1을 지우고 module3을 넣으면 module1은 실행이 안된다.