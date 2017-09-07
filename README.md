# emokit-gui
GUI part of Braingineers project

# Require

### Python Interpreter
CPython 2.7

### pip unsupported packages
- pyqt 4.11.4 (http://www.lfd.uci.edu/~gohlke/pythonlibs/#pyqt4)
- pybluez 0.22 (http://www.lfd.uci.edu/~gohlke/pythonlibs/#pybluez)

### pip packages
- singletonmetaclasss
- gevent
- numpy
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
### Robocon.py
- 로봇의 조작 상태를 저장하고 로봇을 제어하는 코루틴.
### Emocon.py (미완성)
- Emotiv 뇌파 측정 장치를 제어하고, 측정한 뇌파를 인공신경망에 전송해 뇌파 분류 결과를 요청하는 코루틴. 백엔드 스레드에서 돌아감.
### TCPClient.py / TCPServer.py
- 뇌파 측정 장치 및 인공 신경망과 연결할 TCP 클라이언트 소켓.
- TCPServer는 테스트용으로 완성된 프로젝트에 미포함

# TO DO

### MainWindow.py
1. 각 레이아웃 구성 요소의 사이즈 조절

### Robocon.py
1. 로봇과 연결하는 함수 완성

### Emocon.py
1. 인공신경망 서버와 연결