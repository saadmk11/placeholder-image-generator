import argparse
import os

from PIL import Image


class ImageDimentionAction(argparse.Action):

    def __call__(self, parser, namespace, values, option_string=None):
        try:
            image_dimensions = [
                int(x) for x in values.lower().replace(' ', '').split('x', 2)
            ]

            if len(image_dimensions) != 2:
                raise ValueError

            setattr(namespace, self.dest, image_dimensions)
        except ValueError:
            raise ValueError(
                'Invalid dimensions format. '
                'Dimensions of the image should be (widthxheight). e.g: 400x300'
            )


class PathAction(argparse.Action):

    def __call__(self, parser, namespace, values, option_string=None):
        if not os.path.isdir(values):
            raise ValueError("{0} is not a valid path".format(values))
        setattr(namespace, self.dest, values)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate Placeholder Image')
    parser.add_argument(
        'dimensions',
        action=ImageDimentionAction,
        type=str,
        help='Dimensions of the image (widthxheight). e.g: 400x300'
    )
    parser.add_argument(
        '-c', '--color',
        action='store',
        type=str,
        default='grey',
        help='Color of the image. e.g: red'
    )
    parser.add_argument(
        '-rgb', '--rgb-color',
        type=int,
        nargs=3,
        help='RGB color for the image. e.g: 20 30 20'
    )
    parser.add_argument(
        '-n', '--name',
        action='store',
        type=str,
        default='placeholder_image.png',
        help='Name of the generated image. e.g: image_new.png'
    )
    parser.add_argument(
        '-p', '--path',
        action=PathAction,
        type=str,
        help='Path where the image will be saved. e.g: /my_dir'
    )

    args = parser.parse_args()

    color = args.color

    if args.rgb_color:
        color = tuple(args.rgb_color)

    image_name = args.name

    if args.path:
        image_name = args.path + '/' + image_name

    img = Image.new('RGB', args.dimensions, color=color)
    img.save(image_name)
