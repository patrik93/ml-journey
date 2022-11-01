# Intro
My journey in the Machine Learning world with Python

# Usage
Execute the following command in the project root folder
```shell
docker run -itd  -p 8888:8888 -v $(pwd):/home/jovyan/work --name jupyter_nb jupyter/datascience-notebook
```
Get access to the jupyter home page, check the container logs
```shell
docker logs jupyter_nb
```