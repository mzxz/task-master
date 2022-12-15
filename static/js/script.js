const submitNewTask = document.getElementById("submit-new-task");
const addNewTask = document.getElementById("add-new-task");

addNewTask.addEventListener("keyup", (e) => {
    const value = e.currentTarget.value;
    submitNewTask.disabled = false;

    if (value == " "){
        submitNewTask.disabled = true;
    }
});

// function empty() {
//     var x;
//     x = document.getElementById("add-new-task").value;
//     if (x == "") {
//         alert("Enter a Valid Roll Number");
//         return false;
//     };
// }