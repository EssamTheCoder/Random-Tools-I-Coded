// All the funky JSON fetching and functions
//DO NOT IMPLODE WHEN READING
export {get, lengthProcessing, getSpecific, updateClock}

let toggleClock = false
function updateClock() {
    const hrs = document.querySelector(`hrs`)
    const mins = document.querySelector(`mins`)
    const clock = document.querySelector(`clock`)

    const deficitHrs = document.querySelector(`defictHrs`)
    const deficitMins = document.querySelector(`deficitMins`)
    const deficitSign = document.querySelector(`deficitSign`)
    
    const accentColour = `hsl(38, 91%, 44%)`
    const errorColour = `hsl(9, 88%, 45%)`

    //CLOCK TOGGLING
    if(toggleClock === false){ //shows clock & gets time
        toggleClock = true
        hrs.style.display = mins.style.display = deficitHrs.style.display = deficitMins.style.display = document.querySelector(`deficit:`).style.display = deficitSign.style.display = `inline`
        document.querySelector(`:`).style.color = deficitSign.style.color = accentColour
        clock.style.border = `7px solid ${accentColour}`

        clockData()
        deficitData()
    }
    else{ //hides clock and removes time
        toggleClock = false
        document.querySelector(`:`).style.color = `hsl(0, 0%, 28%)`
        hrs.style.display = mins.style.display = deficitHrs.style.display = deficitMins.style.display = document.querySelector(`deficit:`).style.display = `none`
        deficitSign.style.color = `hsl(0, 0%, 28%)`
        deficitSign.innerText = `±`
    }


    "//{" //Sub-Functions of updateClock()
    function clockData(){ //Gets the time data and sets innerText | Returns: null
        fetch(`JSON/time.json`)
        .then(result => result.ok ? result.json() : Promise.reject(`HTTP ${result.status}`))
        .then(data => {
            //VARIABLE DEFINITIONS
            let addHours = 0
            let totalHrs = Number(data.hrs)
            let totalMins = Number(data.mins.thirtyMins)*30 + Number(data.mins.fifteenMins)*15 + Number(data.mins.tenMins)*10 + Number(data.mins.fiveMins)*5

            //MINUTE OVERFLOW
            if( !(totalMins < 60) ){ //Checks if totalMins ≥ 60
                addHours = check60(totalMins)
                totalHrs += addHours
                totalMins -= addHours*60
            }
            else if( !(totalMins > -60) ){ //Checks if totalMins ≤ -60 (for negative overflow)
                addHours = check60(Math.abs(totalMins) )
                addHours = -addHours
                totalHrs += addHours
                totalMins -= addHours*60
            }


            //NEGATIVE VALUES
            if(totalHrs < 0){
                hrs.style.color = errorColour
                totalHrs = Math.abs(totalHrs)
            }

            if(totalMins < 0){
                mins.style.color = errorColour
                totalMins = Math.abs(totalMins)
            }

            if(totalMins < 0 && totalMins < 0){ //Modifications for if both hrs & mins are <0
                document.querySelector(`:`).style.color = errorColour
                clock.style.border = `1px solid ${errorColour}`
            }

            //PADDING
            if(totalHrs < 10){
                totalHrs = `0${totalHrs}` //pads hours value
            }

            if(totalMins < 10){
                totalMins = `0${totalMins}` //pads minutes value
            }

            //SETTING TEXT
            hrs.innerText = totalHrs
            mins.innerText = totalMins

        })
        .catch(error => { //Error: couldn`t fetch data form JSON file
            console.error(`Error fetching data from time.json | ${error} `)
            hrs.innerText = mins.innerText = `..`
            hrs.background = mins.background = errorColour
            clock.style.border = `7px solid ${errorColour}`
            clock.style.background = `hsl(0,80%,15%)`
        })
    }

    function deficitData(){
        fetch(`JSON/time.json`)
        .then(response => response.json())
        .then(data => {
            let dAddHours = 0
            let dTotalHrs = Number(data.total.hrs) - Number(data.hrs)
            let dTotalMins = (Number(data.total.mins.thirtyMins) - Number(data.mins.thirtyMins))*30 + (Number(data.total.mins.fifteenMins) - Number(data.mins.fifteenMins))*15 + (Number(data.total.mins.tenMins) - Number(data.mins.tenMins))*10 + (Number(data.total.mins.fiveMins) - Number(data.mins.fiveMins))*5
            deficitSign.innerText = `+`

            //MINUTE OVERFLOW
            if( !(dTotalMins < 60) ){
                dAddHours += check60(dTotalMins)
                dTotalHrs += dAddHours
                dTotalMins -= dAddHours*60
            }

            if( !(dTotalMins > -60) ){
                dAddHours = -check60( Math.abs( Number(dTotalMins) ) )
                dTotalHrs += dAddHours
                dTotalMins -= dAddHours*60
            }

            //NEGATIVE VALUES
            if( dTotalHrs < 0 || dTotalMins < 0){
                document.querySelector(`deficitContainer`).style.color = errorColour
                deficitSign.innerText = `-`
            }

            //PADDING
            if(dTotalHrs < 10){
                dTotalHrs = `0${dTotalHrs}` //pad the deficit hrs value
            }
            if(dTotalMins < 10){
                dTotalMins = `0${dTotalMins}`
            }

            //SETTING TEXT
            deficitHrs.innerText = dTotalHrs
            deficitMins.innerText = dTotalMins
        })
        .catch(error => {
            deficitHrs.innerText = deficitMins.innerText = `??`
            deficitHrs.style.color = deficitMins.style.color = errorColour
            document.querySelector(`deficitContainer`).style.background = `hsl(0,80%,15%)`
        })
    }

    function check60(number){
        let counter

        function inner(num){
            //Base Cases
            if(num < 60){counter = 0}
            else if(num === 60){counter = 1}

            //Recursion
            else{
                counter += 1 + check60(num - 60) // ✨Recursion✨
            }

            return counter
        }

        counter = 0 //Resets the counter for future calls
        return inner(number)
    }
    `//}`
}

async function get(grade, attribute, length){ //Gets specified attribute from lessons.json. I added some flexibility thogh
    try{
        attribute = String(attribute) //for ease of access

        if(length === undefined){ length = false } //Adds a default value to length to save time when calling the function

        //NEW VARAIBLES
        const response = await fetch(`JSON/lessons.json`)
        const data = await response.json()
        let processing //Variable to ease the return process

        //GRADE CHECK
        if(grade < 1 || grade > 9){ //Error: Grade is invalid (not any integer 1-9)
            console.error(`ParameterError | try putting in a valid GCSE grade next time. | ${grade}`)
        }
        grade -= 1 //for indexes

        //ATTRIBUTE CHECKS
        if( [`name`,`names`].includes(attribute) ){ //Check: attribute is lesson.json -> `names`
            processing = data.names[grade]
        }

        else if( [`pdf`,`pdfs`].includes(attribute) ){ //Check: attribute is lessons.json -> `pdfs`
            processing = data.pdfs[grade]
        }

        else if( [`video`,`videos`,`link`,`links`].includes(attribute) ){ //Check: attribute is lessons.json -> video links
            processing = data.videos[grade]
        }

        else{ //Error: attribute is an invalid parameter/not in lessons.json
            console.error(`ParameterError | try putting in a valid attribute from lessons.json next time. | ${attribute} `)
        }

        //LENGTH CHECKS
        if(length === true){ //Returns: lessons.json -> `attribute` -> value (list) -> length
            processing = processing.length
            
            //Video Processing Case
            if( [`video`,`videos`,`link`,`links`].includes(attribute) ){
                processing = lengthProcessing(data.videos[grade])
                return processing
            }

            else{return Number(processing)}
        } 

        else if(length === false){ //Returns: lessons.json -> `attribute` -> value (list)
            return processing
        }

        else{ //Error: invalid length value
            console.error(`ParameterError | try putting in if you want the length or the list next time. | ${length}`)
        }
    }
    catch(error){  //Error: Couldn`t fetch data from lessons.json
        console.error(`FetchError | ${error} `)
        throw error
    }
}


//Sub-Functions of get()
function lengthProcessing(list){
    let counter = list.length //Presets the length
    let currentList = list //Sets the list

    for(let a = 0; a <= counter; a++){
        if(typeof currentList[a] === `object`){ //Checks if the current list item is a sublist
            counter -= 1 //Subtracts 1 from the length counter (we need to return all the elements in the list, not just all the strings & arrays)
            counter += lengthProcessing(currentList[a]) //Adds the length of the sublist back to the length counter using ✨Recursion✨ in order to account for any potential sublists in the sublist
        }
    }
    return Number(counter) //Sets the type of and returns the length counter
}

function listProcessing(list){
    let currentList = list 
    let transferList = []

    for(let a = 0; a <= list.length; a++){
        if(typeof list[a] === `object`){ //Checks if the current item in the list is a sublist and appends its items to the transfer list
            transferList = [...transferList, ...listProcessing(list[a])] 
        }

        else{
            transferList.push(list[a])

            if(typeof list[a] === `undefined`){ //Bug Fix: checks if the current element has type undefined and deletes it, this prematurely removes the undefined elements that used to show up in the final result
                transferList.pop()
            }
        }

    }
    return transferList
}

async function getSpecific(grade,attribute,index){
    const processing = await get(grade,attribute,false)

    return processing[index]
}
//------------------------------------------------------------------------------
updateClock()
document.querySelector("clock").addEventListener("click",updateClock)
let numberOfLessonsInGrade = []
let external = []
for(let i = 1; i <= 9; i++){
    numberOfLessonsInGrade[i] = await get(i,"name",true)
    external[i-1] = numberOfLessonsInGrade[i]
    if(i === 9){ external[i-1] = numberOfLessonsInGrade[i]
        numberOfLessonsInGrade = external}}
for(let i = 1; i <= 9; i++){
    for(let j = 1; j <= numberOfLessonsInGrade[i-1]; j++){
        let id = `${i}-${j}`
        let lessonString = ``
        let answerString = ``
        lessonString += `<td id="${id}code" class="code ${id}">${id}</td>`
        
        if(localStorage.getItem(`MG: ${id}`) == `true`){
            lessonString += `<td id="${id}checkbox" class ="${id} checkbox"> <input id="${id}check" class="check ${id}" type="checkbox" checked> </td>`
        }else if(localStorage.getItem(`MG: ${id}`) == `false`){
            lessonString += `<td id="${id}checkbox" class ="${id} checkbox"> <input id="${id}check" class="check ${id}" type="checkbox"> </td>`
        }
        let currentList = await get(i,"video",false)
        if(typeof currentList[j-1] === `object`){
            currentList = await get(i,"name",false)
            lessonString += `<td id="${id}video" class="video ${id}"><details class="${id}"><summary class="${id}">${currentList[j-1]}</summary><ul>`

            currentList = await get(i,"video",false)
            currentList = currentList[j-1]
            for(let k = 0;k <= currentList.length;k++){
                lessonString += `<li><a class="${id} video" target="_blank" href="https://www.youtube.com/watch?v=${currentList[k]}">Video #${k+1}</a></li>`}
            lessonString += `</ul></details></td>`
        }else{
            currentList = await get(i,"video",false)
            lessonString +=`<td id="${id}videobox" class="videobox ${id}"><a id="${id}video" class="video ${id}" target="_blank" href="https://www.youtube.com/watch?v=${currentList[j-1]}">${await getSpecific(i,"name",j-1)}</a></td>`
        }
        currentList = await get(i,"pdf",false)
        if(typeof currentList[j-1] === `object`){
            lessonString += `<td id="${id}question" class="question ${id}">><details class="${id}"><summary class="${id}">Questions</summary>`
            answerString += `<td id="${id}answer" class="answer ${id}"><details class="${id}"><summary class="${id}">Answers</summary>`

            currentList = currentList[j-1]
            for(let k = 0;k <= currentList[j-1];k++){
                currentList = currentList[j-1]
                lessonString += `<a class="${id}" target="_blank" href="https:/mathsgenie.co.uk/resources/${currentList[k]}.pdf">Question Sheet #${k+1}</a>`
                answerString += `<a class="${id}" target="_blank" href="https:/mathsgenie.co.uk/resources/${currentList[k]}ans.pdf">Answer Sheet #${k+1}</a>`
            }
            lessonString += `</details></td>`
            answerString += `</details></td>`
        }else{
            currentList = await get(i,"pdf",false)
            lessonString +=`<td id="${id}question" class="question ${id}"><a id="${id}question" class="question ${id}" target="_blank" href="https:/mathsgenie.co.uk/resources/${currentList[j-1]}.pdf">Questions</a></td>`
            answerString +=`<td id="${id}answer" class="answer ${id}"><a id="${id}answer" class="answer ${id}" target="_blank" href="https:/mathsgenie.co.uk/resources/${currentList[j-1]}ans.pdf">Answers</a></td>`}
        lessonString += `${answerString}</tr>`
        document.querySelector(`${i}table`).innerHTML += `<tr id="${id}row">`
        document.querySelector(`${id}row`).innerHTML += lessonString}
    for(let j = 1;j <= numberOfLessonsInGrade[i-1];j++){
        let id = `${i}-${j}`
        document.querySelector(`${id}check`).addEventListener(`click`, () => {
        console.log(`FAAAH this program man`)
        if(localStorage.getItem(`MG: ${id}`) == `true`){
            localStorage.removeItem(`MG: ${id}`)
            localStorage.setItem(`MG: ${id}`,false)
            document.querySelector(`${id}check`).checked = false
        } else {
            localStorage.removeItem(`MG: ${id}`)
            localStorage.setItem(`MG: ${id}`,true)
            document.querySelector(`${id}check`).checked = false
        }})
    }
}