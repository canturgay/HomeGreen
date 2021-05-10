function addNewUser() {
    const form_data = new FormData(document.getElementById("meeting-form"));
    fetch("/api/addnewuser", {
      method: "POST",
      body: form_data,
    })
    .then(
        function (response) {
            if (response !== 201) {
                console.log(response)
            }
            return console.log("NewUserCreated")
        }
    )

    .catch(function (err) {
        console.log("Posting Error!", err);
    })
}
    

function checkUser() {
    const form_data = FormData(document.getElementById("addNewUser"));
    fetch("/api/checkuser", {
        method: "POST",
        body: form_data
    })

        .then(
        function (response) {
            if (response !== 201) {
                console.log("User Exists")
            };
            return addNewUser(); 
        }
    )

        .catch(
        function (err) {
        console.log("Fetching Error!", err);
        }
    )
}

