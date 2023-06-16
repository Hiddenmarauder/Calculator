document.addEventListener("DOMContentLoaded", function() {
    const buttons = document.querySelectorAll(".calculator button");
    const resultElement = document.getElementById("result");
    const expressionElement = document.getElementById("expression");
  
    buttons.forEach(function(button) {
      button.addEventListener("click", function() {
        const buttonValue = button.textContent;
        if (buttonValue === "=") {
          evaluateExpression();
        } else if (buttonValue === "C") {
          clearExpression();
        } else {
          appendToExpression(buttonValue);
        }
      });
    });
  
    function appendToExpression(value) {
      expressionElement.value += value;
    }
    function evaluateExpression() {
        const expression = expressionElement.value;
        try {
          const result = eval(expression);
          expressionElement.value = result;
        } catch (error) {
          console.log("Error:", error);
          expressionElement.value = "Error";
        }
      }
      
    function clearExpression() {
      expressionElement.value = "";
      resultElement.textContent = "";
    }
  });
  
  