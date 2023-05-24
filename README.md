# nutruition-app-api

### Creating the docker file:

Alpine is a lightweiter version of linux

- Run command:
    Intead of having multiple RUN instructions, we have only one and we break them usinng the && \ instuction to avoid creating a new image layer for each command. it make building the image more efficient 