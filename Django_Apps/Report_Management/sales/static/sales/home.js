console.log("hello world")

const reportBtn = document.getElementById("report-btn")
const img = document.getElementById("img")

const modalBody = document.getElementById("modal-body")


const reportForm = document.getElementById("report-form")
const reportName = document.getElementById("id_name")
const reportRemarks = document.getElementById("id_remarks")

const csrf = document.getElementsByName("csrfmiddlewaretoken")[0].value

const alertBox = document.getElementById("alert-box")
const handleAlerts = (type,msg) => {
    alertBox.innerHTML = `
    <div class="alert alert-${type}" role="alert">
    ${msg}
    </div>
    `
}


if(img){
    reportBtn.classList.remove("not-visible")
}


reportBtn.addEventListener("click",()=>{
    console.log("clicked")
    img.setAttribute("class","w-100")
    modalBody.prepend(img)
    

    reportForm.addEventListener("submit",e=>{
        e.preventDefault()
        const form_data = new FormData()
        form_data.append("csrfmiddlewaretoken",csrf)
        form_data.append("name",reportName.value)
        form_data.append("remarks",reportRemarks.value)
        form_data.append("image",img.src)

        $.ajax({
            type:"POST",
            url:"/reports/save/",
            data: form_data,
            success: function(response){
                console.log(response)
                handleAlerts("success","report created.")
                // $('#reportModal').modal('toggle');
                reportForm.reset()
            },
            error: function(error){
                console.log(error)
                handleAlerts("danger","oops...something went wrong")
            },
            processData:false,
            contentType:false

        })

    })
})


