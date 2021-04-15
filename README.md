## Notebook graphs

If you have a problem seeing the charts, please go to following link:
https://nbviewer.jupyter.org/github/serenayhanim/footballer_project/blob/main/notebooks/data_profile_remote.ipynb


## DockerFile

To build docker image from Dockerfile

```console
docker build -t scrape:latest .                                                       
```

```console
docker run -it -v /your/local/project/path:/serenay scrape
```

change accounts.csv accordingly. 
