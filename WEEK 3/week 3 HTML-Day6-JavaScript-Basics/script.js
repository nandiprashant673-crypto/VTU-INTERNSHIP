// 1. Alert
function showAlert() {
    alert("Button Clicked Successfully!");
}

// 2. Form Validation
function validateForm() {
    var name = document.getElementById("name").value;
    var email = document.getElementById("email").value;

    if (name == "" || email == "") {
        alert("Please fill all fields");
        return false;
    }

    alert("Form submitted successfully!");
    return true;
}

// 3. Calculator
function calculate() {
    var num1 = parseFloat(document.getElementById("num1").value);
    var num2 = parseFloat(document.getElementById("num2").value);

    var sum = num1 + num2;

    document.getElementById("result").innerHTML = "Result: " + sum;
}

// 4. Change Text
function changeText() {
    document.getElementById("text").innerHTML = "Text Changed Successfully!";
}