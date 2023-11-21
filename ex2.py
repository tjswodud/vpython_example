"""
Example 2 - 인공위성 시뮬레이션
Description. 지구 주위를 공전하는 인공위성을 시각화 해봅시다.
"""

# 필요한 라이브러리 임포트
from vpython import *

# 상수 정의
G = 6.67e-11 # 중력 상수 -> 6.67 * 10^(-11)
earth_radius = 6.378e6 # 지구의 반지름 -> 6.37 * 10^6
earth_mass = 5.972e24 # 지구의 질량 -> 5.972 * 10^24

# 지구 & 인공위성 생성
earth = sphere(pos=vector(-earth_mass, 0, 0), radius=earth_radius, texture=textures.earth) # pos: 위치, radius: 반지름, texture: 텍스쳐 (기본으로 제공하는 지구 텍스쳐를 사용함)
earth.m = earth_mass # 지구의 질량 정의
earth.p = vector(0,0,0) * earth.m # 초기 위치 정의

satellite = sphere(pos=vector(2 * earth_radius, 0, 0), radius=0.5 * earth_radius, make_trail=True) # make_trail: 이동 경로를 그리고 싶으면 True, 아니면 False
satellite.m = 100 # 인공위성의 질량
satellite.p = vector(0, 5000, 0) * satellite.m # 초기 위치 정의

# 시간 & 변화량 변수 초기화
t=0
dt=1

# 애니메이션 루프
while True:
    rate(1000) # 초당 1,000 프레임.

    r = satellite.pos - earth.pos # 인공위성과 지구 사이의 거리

    """
    만유인력 계산 (출처: https://ko.wikipedia.org/wiki/%EB%A7%8C%EC%9C%A0%EC%9D%B8%EB%A0%A5%EC%9D%98_%EB%B2%95%EC%B9%99)
    - norm(vector) : vector의 크기를 정규화 (normalize)하여 단위벡터로 만듭니다.
    - mag(vector) : vector의 크기를 구합니다.
    """
    F = norm(r) * (-G) * earth.m * satellite.m / mag(r) ** 2

    # 계산한 만유인력에 따른 인공위성 위치 업데이트
    satellite.p = satellite.p + F * dt
    satellite.pos = satellite.pos + satellite.p * dt / satellite.m

    t=t+dt # 시간 업데이트