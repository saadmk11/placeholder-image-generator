# Placeholder Image Generator

A small python tool that generates placeholder images with specific dimensions.


### usage: 

`main.py [-h] [-c COLOR] [-rgb RGB_COLOR RGB_COLOR RGB_COLOR] [-n NAME] [-p PATH] dimensions`

**Examples:**

- `python main.py 400x200`

- `python main.py 400x200 -c "#1011ff"`

- `python main.py 400x200 -c white -n new.png -p /home/user/Desktop`

- `python main.py 400x200 -rgb 10 20 30 -n new.png`


### positional arguments:

- **`dimensions`** Dimensions of the image (widthxheight). **e.g: 400x300**

### optional arguments:

- **`-h`, `--help`** show this help message and exit
- **`-c`, `--color`** Color of the image. **e.g: red**
- **`-rgb`, `--rgb-color`** RGB color for the image. **e.g: 20 30 20**
- **`-n`, `--name`** Name of the generated image. **e.g: image_new.png**
- **`-p`, `--path`** Path where the image will be saved. **e.g: /my_dir**
