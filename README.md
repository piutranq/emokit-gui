# emokit-gui
GUI part of Braingineers project

# Require

### Python Interpreter
CPython 2.7

### pip unsupported packages
- pyqt 4.11.4 (http://www.lfd.uci.edu/~gohlke/pythonlibs/#pyqt4)

### pip packages
- singletonmetaclasss
- gevent
- numpy
- pycrypto
- pywinusb
- pyusb

### other dependencies
- libusb-win32 1.2.6.0 (https://sourceforge.net/projects/libusb-win32/files/libusb-win32-releases/1.2.6.0/)


# Summary

### main.py
- 최초 실행 지점
### no_emo_test.py
- 테스트용으로 Emotiv 장치와 인공 신경망 연결을 제외한 main 
### MainWindow.py
- PyQt로 작성된 프론트엔드 GUI
### Layout.py
- 메인 윈도우의 레이아웃 구성
### Terms.py
- 메인 윈도우에서 사용될 문자열
### Robocon.py
- 로봇의 조작 상태를 저장하고 로봇을 제어하는 코루틴
### EmotivCustom.py
- emokit 패키지의 Emotiv 클래스를 상속받아 일부 수정
### Emocon.py
- 뇌파를 인공신경망에 전송해 뇌파 분류 결과를 요청하는 클래스
### TCPClient.py / TCPServer.py
- 뇌파 측정 장치 및 인공 신경망과 연결할 TCP 클라이언트 소켓
- TCPServer는 테스트용으로 완성된 프로젝트에 미포함

### robotcode.nxc
- LEGO NXT를 조작하는 코드. GUI와 무관하며 컴파일 후 NXC 상에서 실행.

# TO DO

### MainWindow.py
- 각 레이아웃 구성 요소의 사이즈 조절
### robotcode.nxc
- 실제로 로봇이 작동하도록 수정. 현재는 전송받은 메시지에 따라 분기하는 것 까지만 구현됨.