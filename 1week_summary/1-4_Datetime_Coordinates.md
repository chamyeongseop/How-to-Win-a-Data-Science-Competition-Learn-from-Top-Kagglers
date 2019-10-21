# Datetime and Coordinates
- Datetime
  - Periodicity
    - year, month, day, hour, minute, second 별로 나누어서 반복성을 찾음.
    - Season, Week 등의 기준을 잡아준다.
    - Binary feature : Workday/Holiday, Business time 등으로 나누는 방법도 있음.
    - 3일에 한번씩 같은 특정 패턴을 찾을 때 유용하다.


  - Time since
    - 마지막 휴일 이후에 얼마나 시간이 지났는지 / 캠페인이 끝날때까지 얼마나 남았는지
    - 특정 사건이 발생한 후, 시간 경과를 나타냄



  - Difference between dates
    - 2개의 data feature간의 차이를 의미


- Coordinates

  - 위도, 경도
  - Tree 모델은 Numerical feature가 선형성을 띄면 구분하기 힘들 수 있어서 회전을 주고 사용함.
