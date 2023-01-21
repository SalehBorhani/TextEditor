# TextEditor
This is a simple text editor with tkinter in python.
# Run with Docker in Linux
In the directory you should run the following commands:
```
docker build -t text_image .
docker run -u=$(id -u $USER):$(id -g $USER) -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix:rw -v $(pwd):/app --rm text_image
```
