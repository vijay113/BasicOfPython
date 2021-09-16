console.log("hello world")

const reportBtn = document.getElementById("report-btn")
const img = document.getElementById("img")

const modalBody = document.getElementById("modal-body")

const reportName = document.getElementById("id_name")
const reportRemarks = document.getElementById("id_remarks")


if(img){
    reportBtn.classList.remove("not-visible")
}


reportBtn.addEventListener("click",()=>{
    console.log("clicked")
    img.setAttribute("class","w-100")
    modalBody.prepend(img)
})


