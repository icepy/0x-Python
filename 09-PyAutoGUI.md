先说一下为什么要用 PyAutoGUI，这是一个可以模拟鼠标，键盘的工具，这就意味着可以在桌面上，自动的对某些软件点点来完成交互。

它的实现逻辑比较简单，在屏幕上的位置用 x 和 y 坐标来实现，x 是横向的，y 是纵向的，x 从左侧 0 位置开始，一直向右侧增加，y 从顶部 0 位置开始，一直向下增加，举一个例子比如你的屏幕分辨率是 1920 x 1080，则右下角的坐标为（1919,1079），这是因为坐标系都是从 0 开始，而不是从 1 开始。

[https://pyautogui.readthedocs.io/en/latest/](https://pyautogui.readthedocs.io/en/latest/)

整体的 python 代码不难，安装完模块后，都是使用 APIs 来完成你想自动化的步骤。

比如，举一个小例子，将鼠标自动的移动

```python
x = 200
y = 200
num_seconds = 1

pyautogui.moveTo(x,y,duration=num_seconds)
```

在 1 秒内将鼠标移动到 x y 的位置

```python
pyautogui.click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='left')
```

使用左键单击一次鼠标

你看，其实这些代码都很简单，你要明白，这个模块可以做什么事情，比去明白代码要重要的多。