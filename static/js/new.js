// Get all the divs with the class "scroll-div"
const divs = Array.from(document.getElementsByClassName('about'));

// Function to check if an element is in the viewport
function isInViewport(element) {
  const rect = element.getBoundingClientRect();
  console.log(document.documentElement.clientHeight,window.innerHeight)
  return (
    rect.top >= 0 &&
    rect.left >= 0 &&
    rect.bottom <= (window.innerHeight||document.documentElement.clientHeight)+rect.bottom/2.5
  );
}

// Function to handle div appearance
function handleDivAppearance() {
    console.log(divs.length)
    divs.forEach((div) => {
        console.log(isInViewport(div))
    if (isInViewport(div)) {
        // console.log("if")
      div.style.opacity = '1'; // Make the div visible
    }
  });
}

// Attach the handleDivAppearance function to the scroll event
window.addEventListener('scroll', handleDivAppearance);

// Initially, check if any divs are already in the viewport
handleDivAppearance();


// for adding items to list 
function add(food_id) {
    // var searchText = document.getElementById("search-input").value;
    document.getElementById("blur").classList.add("blur-background");
    loadDoc()
    var input = document.getElementsByName("food")[0]
    console.log(input)
    input.value = food_id;
}


function hide() {
  document.getElementById("blur").classList.remove("blur-background");
  document.getElementById("demo").style.visibility = "hidden"
}


  function loadDoc() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      var demo = document.getElementById("demo");
      demo.innerHTML = this.responseText;
      demo.style.visibility = "visible";
    }
  };

  xhttp.open("GET", "/cart/add", false);
  xhttp.send();

}