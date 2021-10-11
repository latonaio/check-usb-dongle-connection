# check-usb-dongle-connection
USBドングルがエッジ端末に接続されたことを確認します。USBドングルのセットアップについては、下記を参考にしてください。   
-  [USBドングルのセットアップ](https://github.com/latonaio/iot-sim-soracom)

### マイクロサービスのセットアップ
リポジトリをCloneし、Docker build します。

```
$ git clone git@github.com:latonaio/check-usb-dongle-connection.git
$ cd check-usb-dongle-connection
$ make docker-build
```

### Project.ymlの記載方法

```
microservices:  
  check-usb-dongle-connection:  
    startup: yes  
    always: yes  
    privileged: yes  
    volumeMountPathList:  
      - /dev:/dev:Bidirectional
```
