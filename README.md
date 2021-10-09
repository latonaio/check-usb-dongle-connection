# check-usb-dongle-connection

* [USBドングルのセットアップ](https://github.com/latonaio/iot-sim-soracom)

### マイクロサービスのセットアップ

```
$ git clone git@bitbucket.org:latonaio/check-usb-dongle-connection.git
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
