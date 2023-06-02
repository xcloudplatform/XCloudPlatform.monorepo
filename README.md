# XCloudPlatform Monorepo


xcp is a platofrm for development of the software. it includes a Visual Studio Code that is running a preview (transformation, rendering etc) of the content that is being edited in text editor

## Browser

xcp launches a docker job (built in: text to text, text to image, text to video, or user's docker image) on Kubernetes cluster that continiously incrementally transforms what is written in the visual studio code into the interactive in-browser preview



## Workstation

RDP into virtualized provisioned (monitored and robotitized) by xcp Windows enviroment on Kubernetes cluster in a native crossplatform (go) VS code plugin (panel/tab)