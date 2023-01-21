# TextEditor
This is a simple text editor with tkinter in python.
# Run with Docker in Linux
At first you should clone the repository:
```
$ git clone https://github.com/SalehBorhani/TextEditor
```
Change the directory and run the following commands:
```
$ cd TextEditor
$ docker build -t text_image .
$ docker run -u=$(id -u $USER):$(id -g $USER) -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix:rw -v $(pwd):/app --rm text_image
```
