//All the automatic loading (I am not coding all that HTML by hand)
import {get, lengthProcessing, getSpecific, updateClock, changeTheme} from './library.js'

//Setting up the clock
changeTheme();
document.getElementById(`themeButton`).addEventListener(`click`,changeTheme);

updateClock();
document.getElementById(`clock`).addEventListener(`click`,updateClock);

//Number of Lessons in Each Table (used in main for loop)
let numberOfLessonsInGrade = []
let external = []
for(let i = 1; i <= 9; i++){ //Getting the number of lessons for each grade level & PROPERLY setting it to the list
    numberOfLessonsInGrade[i] = await get(i,"name",true);

    external[i-1] = numberOfLessonsInGrade[i]

    if(i === 9){
        external[i-1] = numberOfLessonsInGrade[i]
        numberOfLessonsInGrade = external;
    };
}
for(let i = 1; i <= 9; i++){

    for(let j = 1; j <= numberOfLessonsInGrade[i-1]; j++){ //All the lessons get defined here
        let identifier = `${i}-${j}`;
        let lessonString = ``; //initalises the table row for the current lesson
        let answerString = `` //initalises the answer cell of the current lesson
        lessonString += `<td id="${identifier}code" class="code ${identifier}">${identifier}</td>`; //adds the lesson code
        
        if(localStorage.getItem(`MG: ${identifier}`) == `true`){
            lessonString += `<td id="${identifier}checkbox" class ="${identifier} checkbox"> <input id="${identifier}check" class="check ${identifier}" type="checkbox" checked> </td>`;
        } else if(localStorage.getItem(`MG: ${identifier}`) == `false`){
            lessonString += `<td id="${identifier}checkbox" class ="${identifier} checkbox"> <input id="${identifier}check" class="check ${identifier}" type="checkbox"> </td>`;
        }


        //Video
        let currentList = await get(i,"video",false);
        if(typeof currentList[j-1] === `object`){
            currentList = await get(i,"name",false);
            lessonString += `<td id="${identifier}video" class="video ${identifier}"><details class="${identifier}"><summary class="${identifier}">${currentList[j-1]}</summary><ul>`;

            currentList = await get(i,"video",false);
            currentList = currentList[j-1];
            for(let k = 0;k <= currentList.length;k++){
                lessonString += `<li><a class="${identifier} video" target="_blank" href="https://www.youtube.com/watch?v=${currentList[k]}">Video #${k+1}</a></li>`;
            }
            lessonString += `</ul></details></td>`;
        } 
        else{
            currentList = await get(i,"video",false);
            lessonString +=`<td class="${identifier}"><a id="${identifier}video" class="video ${identifier}" target="_blank" href="https://www.youtube.com/watch?v=${currentList[j-1]}">${await getSpecific(i,"name",j-1)}</a></td>`;
        }

        //PDFs
        currentList = await get(i,"pdf",false);
        if(!(identifier === `3-16`)){
            lessonString += `<td class="${identifier}"><a id="${identifier}question" class="question ${identifier}" target="_blank" href="https:/www.mathsgenie.co.uk/resources/${currentList[j-1]}.pdf">Questions</a></td>`;
            answerString += `<td class="${identifier}"><a id="${identifier}answer" class="answer ${identifier}" target="_blank" href="https:/www.mathsgenie.co.uk/resources/${currentList[j-1]}ans.pdf">Answers</a></td>`;
        } 
        else{
            lessonString += `<td id="${identifier}question" class="question ${identifier}"><details class="${identifier}"><summary class="${identifier}">Question Sheets</summary><ul>`;
            answerString += `<td id="${identifier}answer" class="answer ${identifier}"><details class="${identifier}"><summary class="${identifier}">Answer Sheets</summary><ul>`;
            currentList = await get(3,"pdf",false);
            currentList = currentList[j-1];
            for(let k = 0;k <= currentList.length;k++){
                lessonString += `<li><a class="${identifier} question" target="_blank" href="https://www.mathsgenie.co.uk/resources/${currentList[k]}.pdf">Sheet #${k+1}</a></li>`;
                answerString += `<li><a class="${identifier} answer" target="_blank" href="https://www.mathsgenie.co.uk/resources/${currentList[k]}ans.pdf">Sheet #${k+1}</a></li>`;
            }
            lessonString += `</ul></details></td>`;
            answerString += `</ul></details></td>`;
        }

        lessonString += `${answerString}</tr>`;
        document.getElementById(`${i}table`).innerHTML += `<tr id="${identifier}row">`;
        document.getElementById(`${identifier}row`).innerHTML += lessonString;
    }

    for(let j = 1;j <= numberOfLessonsInGrade[i-1];j++){
        let identifier = `${i}-${j}`;
        document.getElementById(`${identifier}check`).addEventListener(`click`, () => {
        console.log(`FAAAH this program man`)
        if(localStorage.getItem(`MG: ${identifier}`) == `true`){
            localStorage.removeItem(`MG: ${identifier}`);
            localStorage.setItem(`MG: ${identifier}`,false);
            document.getElementById(`${identifier}check`).checked = false;
        } 
        else {
            localStorage.removeItem(`MG: ${identifier}`);
            localStorage.setItem(`MG: ${identifier}`,true);
            document.getElementById(`${identifier}check`).checked = true;
        }});
    }
}