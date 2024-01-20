function startVVideoFromCamera(){
    navigator.mediaDevices.getDisplayMedia({video:true}).then(stream=>{
        const videoElement = document.querySelector('#video')
        videoElement.srcObjec = stream
    })
}
window.addEventListener('DOMContentLoadead', startVVideoFromCamera)