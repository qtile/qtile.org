Qtile.org
=========

[Qtile.org](http://qtile.org/) is a powered by [Django](https://www.djangoproject.com/) and hosted on [Heroku](https://www.heroku.com/).

Setup Instructions
------------------

### Requirements

1. [Bower](http://bower.io/)
2. [LessCSS](http://lesscss.org/)
3. [Python 2.x](https://www.python.org/)

### Running Locally

1. Install requirements

    ```
    pip install -r requirements.txt
    bower update
    ```

2. Create screenshot thumbnails

    ```
    python manage.py process_screenshots
    ```

3. Run the development server

    ```
    python manage.py runserver
    ```

Contributing
------------

Contributing is easy: fork this repository on GitHub, make your changes, and make a pull request.

### Screenshots (& Configurations)

1. Drop your screenshot image into ``qtile/static/img/screenshots/``
2. Add your screenshot (and a link to your config, if applicable) to ``data/Screenshot.yaml``

**Note:** You'll need to re-run ``python manage.py process_screenshots`` for your updated screenshot thumbnail to display locally.

### Videos

1. Add a link to your video (on YouTube, Vimeo, etc) to ``data/Video.yaml``
