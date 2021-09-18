const csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value

const alertbox = document.getElementById("alert-box")

Dropzone.autoDiscover = false
const myDropzone = new Dropzone("#my-dropzone",{
    url:"/reports/upload/",
    init: function(){
        this.on("sending",function(file,xhr,formData){
            console.log("sending...")
            formData.append("csrfmiddlewaretoken",csrf)
        })  
        this.on("success",function(file,response){
            console.log(response)
            const ex = response.ex
            if(ex){
                    alertbox.innerHTML=`
                    <div class="alert alert-danger" role="alert">
                    file already exists.
                    </div>
                    `
            }else{
                alertbox.innerHTML=`
                <div class="alert alert-sucess" role="alert">
                file uploaded.
                </div>
                `
            }
        })  
    },
    maxFiles:3,
    maxFilesize:3,
    acceptedFiles:".csv"
})




