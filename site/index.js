function show_answer() {
    var answer_buttom = document.getElementById("show_answer_button");
    var answers = document.getElementsByClassName("correct_answer");
    if (answer_buttom.value == "Show Answers" ) {
        answer_buttom.value = "Hide Answers";
        for (var i=0; i < answers.length; i++) { answers[i].style.display = "block" };
        }
    else {
        answer_buttom.value = "Show Answers";
        for (var i=0; i < answers.length; i++) { answers[i].style.display = "none" };
        }
    }
