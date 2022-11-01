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

Build the container
```shell
docker build ./ -t ml-journey
```

Start the container
```shell
docker run -it -p 8000:8000 ml-journey
```

Accessible endpoint to run the initial workflow, with default file used for prediction
```shell
http://127.0.0.1:8000/predict
```