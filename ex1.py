"""
Example 1 - 자유낙하 시뮬레이션
Description. 물체의 자유낙하 운동을 vpython으로 구현해 봅시다.
"""

# 필요한 라이브러리 임포트
from math import *
from vpython import *

def main():
    # 물체 (공, 바닥) 생성
    ball = sphere(pos=vector(-5, 18, 0), radius=1, color=color.green)
    floor = box(pos=vector(0, -9, 0), size=vector(100, 0.5, 100))

    # 공의 속도, 위치, 중력가속도 (g) 정의
    velocity = vector(0.7, 0, 0)
    position = ball.pos
    g = vector(0, -9.81, 0)

    # 공의 이동 경로 (trail)와 이동 방향 (arrow)을 시각화
    ball.trail = curve(color=color.white)
    arrow_ = arrow(pos=ball.pos, axis=velocity, color=color.yellow)
    label_ = label() # label에는 현재 공의 속도가 표시될 것임

    # 자유낙하 운동 공식을 적용하기 위한 변수 정의
    dt = 0.005
    half = 0.5 # 1/2 (vpython의 벡터 관련 에러를 피하기 위해 변수로 선언했습니다.)

    """
    <자유낙하 운동 공식> (reference: https://ko.wikipedia.org/wiki/%EC%9E%90%EC%9C%A0_%EB%82%99%ED%95%98)
    (v: 속도, t: 운동 시간, s: 위치, g: 중력가속도)
    1. v = g * t
    2. s = 1/2 * g * t^2
    """

    while True:
        rate(300) # 초당 300 프레임의 속도로 애니메이션 재생 (300 fps. 숫자가 클수록 부드러운 애니메이션이 재생됨)

        # 바닥에 닿은 공이 위로 튀어오르는 효과 구현
        if ball.pos.y < floor.pos.y + 1: # 공이 바닥에 닿았다면,
            velocity.y = -velocity.y # 공의 속도를 반대 방향 (아래 -> 위)으로 바꾼다. -> 튀어오르는 효과

        # 자유낙하 운동 공식 구현
        velocity += g * dt
        position += velocity * dt + g * half * dt ** 2

        ball.pos = position

        ball.trail.append(pos=ball.pos) # 공의 경로 추적

        # 공의 진행 방향을 화살표 (arrow)로 표현
        arrow_.pos = ball.pos
        arrow_.axis = velocity * 0.3

        # 현재 공의 속도를 label로 표시
        label_.pos = floor.pos + vector(0, -0.5, 0)
        label_.text = 'v : %.2f m/s' % velocity.y
    
if __name__ == "__main__":
    main()