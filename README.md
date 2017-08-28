# emokit-gui
GUI part of Braingineers project

# Require

### Python Interpreter
CPython 2.7

### pip unsupported packages
pyqt 4.11.4 (http://www.lfd.uci.edu/~gohlke/pythonlibs/#pyqt4)
pybluez 0.22 (http://www.lfd.uci.edu/~gohlke/pythonlibs/#pybluez)

### pip packages
- singletonmetaclasss
- gevent
- numpy
- matplotlib (그래프를 더이상 쓰지 않으므로 제거 예정)
- pycrypto
- pywinusb


# Summary

## main.py
- 최초 실행 지점
### MainWindow.py
- PyQt로 작성된 프론트엔드 GUI
### Layout.py
- 메인 윈도우의 레이아웃 구성
### Terms.py
- 메인 윈도우에서 사용될 문자열
### BackendThread.py
- 백엔드에서 돌아가는 모든 기능을 총괄하는 스레드
### Robocon.py
- 로봇의 조작 상태를 저장하고 로봇을 제어하는 코루틴. 백엔드 스레드에서 돌아감.
### BtClient.py
- 로보콘이 로봇 제어 명령문을 보낼 때 사용할 블루투스 클라이언트 소켓.
### BtServer.py
- BtClient의 테스트를 위한 블루투스 서버 소켓. 완성된 프로젝트엔 포함되지 않는다.
### Emocon.py (미완성)
- Emotiv 뇌파 측정 장치를 제어하는 코루틴. 백엔드 스레드에서 돌아감.

# TO DO

### BackendThread.py
1. Emotiv 제어 및 수집된 뇌파를 GUI와 신경망에 전달
2. 신경망으로부터 로보콘에 전달할 분류결과를 받아올 것

### MainWindow.py
1. 각 레이아웃 구성 요소의 사이즈 조절

### Emocon.py
1. 다른 코루틴과 동시에 작동이 가능하도록 완성할 것