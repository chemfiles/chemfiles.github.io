# Chemfiles website

This website use [cactus](https://github.com/koenbok/Cactus) as static website
generator. To build it locally, you have to install the dependencies:

```
pip install cactus pygments
```

And then start the local server:
```
cd src
cactus serve
```

The `http://127.0.0.1:8000` URL now point on a local version of this site. Make
your changes, commit them and then push to Github to deploy.

Commits to *master* are automatically build and published using
[Travis](https://travis-ci.org/chemfiles/chemfiles.github.io)

Documentation is automatically build and deployed from each repository.
