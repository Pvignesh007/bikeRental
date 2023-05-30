function validate(){
    const username =document.querySelector(".username");
    const password =document.getElementById("password");
    if(username.value==" " && password.value==" ")
    {
        // alert("Enter your validate username and password")
        swal({
            title: "Enter your Username and Password",
          });
        return false;
    }
    else if(username.value=="")
    {
        if(username)
        swal({
            title: "Enter Your Username",
          });
        //alert("Enter your username");
        return false;
    }
    else if(password.value=="")
    {
        swal({
            title: "Enter your password",
          });
       // alert("Enter your password");
        return false;
    }

}
