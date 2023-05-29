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
