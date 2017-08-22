# emokit-gui
GUI part of Braingineers project

# TO DO

## BackendThread.py
1. Emotiv 제어 및 수집된 뇌파를 GUI와 신경망에 전달
2. 신경망으로부터 분류결과를 받아 로보콘에 전달

## MainWindow.py
1. pyplot 그래프가 뇌파 데이터와 연동하도록 수정
2. 각 레이아웃 구성 요소의 사이즈 조절

## Robocon.py
1. send_state() 메소드 구현 (로보콘의 스테이트를 기반으로 실제 로봇에게 적절한 명령 전달)