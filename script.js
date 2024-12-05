// Scripts used on the CTPS site
// Author: Mike Smith

// JavaScript function that handles the button click
// associated with chapter ALE dropdown list. The action
// loads the selected chapter's ALE webpage in a new tab.
function handleSelectedChapter() {
    const selectedValue = document.getElementById("ALEdropdown").value;
    window.open(selectedValue, '_blank', 'noopener,noreferrer')
}
