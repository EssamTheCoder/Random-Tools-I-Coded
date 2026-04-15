// All the funky functions
export {intialiseCheckboxes}

let theme = 1;
export function changeTheme(){
    const root = document.querySelector(`:root`).style;
    const themeButton = document.getElementById(`themeButton`);
    if(theme == 1){
        theme = 2;
        themeButton.innerHTML = `<svg id="themeButton" xmlns="http://www.w3.org/2000/svg" width="14" height="14" fill="white" class="bi 222" viewBox="0 0 16 16"">
            <path d="M6 .278a.77.77 0 0 1 .08.858 7.2 7.2 0 0 0-.878 3.46c0 4.021 3.278 7.277 7.318 7.277q.792-.001 1.533-.16a.79.79 0 0 1 .81.316.73.73 0 0 1-.031.893A8.35 8.35 0 0 1 8.344 16C3.734 16 0 12.286 0 7.71 0 4.266 2.114 1.312 5.124.06A.75.75 0 0 1 6 .278"/></svg>`;

        root.setProperty(`--bg`,`hsl(0, 0%, 12%)`);
        root.setProperty(`--nav-bg`,`hsl(0,0%,9%)`);
        root.setProperty(`--clock-bg`,`linear-gradient(to bottom right, black 70%, hsl(0,0%,11%)`);

        root.setProperty(`--header`,`hsl(0,0%,98%)`);
        root.setProperty(`--text`,`hsl(0,0%,89%)`);

        root.setProperty(`--anchor`,`hsl(26, 93%, 45%)`);
        root.setProperty(`--anchor-hover`,`hsl(26,93%,50%)`);

        root.setProperty(`--higher-anchor`,`hsl(121, 50%, 58%)`);
        root.setProperty(`--higher-anchor-hover`,`hsl(121,72%,68%)`);

        root.setProperty(`--border`, `hsl(0,0%,100%)`);
        root.setProperty(`--error`, `hsl(0, 85%, 56%)`);

    }

    else if(theme == 2){
        theme = 3;

        themeButton.innerHTML = `<svg id="themeButton" xmlns="http://www.w3.org/2000/svg" width="14" height="14" fill="white" class="bi bi-symmetry-vertical" viewBox="0 0 16 16">
            <path d="M7 2.5a.5.5 0 0 0-.939-.24l-6 11A.5.5 0 0 0 .5 14h6a.5.5 0 0 0 .5-.5zm2.376-.484a.5.5 0 0 1 .563.245l6 11A.5.5 0 0 1 15.5 14h-6a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .376-.484M10 4.46V13h4.658z"/></svg>`;

        root.setProperty(`--bg`,`hsl(0,0%,10%)`);
        root.setProperty(`--nav-bg`,`hsl(0,0%,7%)`);
        root.setProperty(`--clock-bg`,`linear-gradient(to bottom right, hsl(0,0%,22%) 70%, hsl(0,0%,13%) )`);

        root.setProperty(`--header`,`hsl(0,0%,90%)`);
        root.setProperty(`--text`,`hsl(0,0%,80%)`);

        root.setProperty(`--anchor`,`hsl(206,92%,45%)`);
        root.setProperty(`--anchor-hover`,`hsl(206,94%,50%)`);

        root.setProperty(`--higher-anchor`,`hsl(301,50%,58%)`);
        root.setProperty(`--higher-anchor-hover`,`hsl(301,73%,68%)`);

        root.setProperty(`--border`, `hsl(0,0%,100%)`);
        root.setProperty(`--error`, `hsl(180,86%,56%)`);
    }

    else if(theme == 3){
        theme = 4;
        themeButton.innerHTML = `<svg id="themeButton" xmlns="http://www.w3.org/2000/svg" width="14" height="14" fill="black" class="bi bi-symmetry-vertical" viewBox="0 0 16 16" style="transfotm: rotateY('270')">
            <path d="M7 2.5a.5.5 0 0 0-.939-.24l-6 11A.5.5 0 0 0 .5 14h6a.5.5 0 0 0 .5-.5zm2.376-.484a.5.5 0 0 1 .563.245l6 11A.5.5 0 0 1 15.5 14h-6a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .376-.484M10 4.46V13h4.658z"/></svg>`;
        root.setProperty(`--bg`,`hsl(0, 0%, 88%)`);
        root.setProperty(`--nav-bg`,`hsl(0,0%,91%)`);
        root.setProperty(`--clock-bg`,`linear-gradient(to bottom right, white 70%, hsl(0,0%,89%)`);

        root.setProperty(`--header`,`hsl(0,0%,2%)`);
        root.setProperty(`--text`,`hsl(0,0%,11%)`);

        root.setProperty(`--anchor`,`hsl(206,93%,55%)`);
        root.setProperty(`--anchor-hover`,`hsl(206,94%,50%)`);

        root.setProperty(`--higher-anchor`,`hsl(301,50%,42%)`);
        root.setProperty(`--higher-anchor-hover`,`hsl(301,72%,32%)`);

        root.setProperty(`--border`, `hsl(0,0%,0%)`);
        root.setProperty(`--error`, `hsl(180,85%,44%)`);
    }

    else{
        theme = 1;
        themeButton.innerHTML = `<svg id="themeButton" xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-sun" viewBox="0 0 16 16">
            <path d="M8 11a3 3 0 1 1 0-6 3 3 0 0 1 0 6m0 1a4 4 0 1 0 0-8 4 4 0 0 0 0 8M8 0a.5.5 0 0 1 .5.5v2a.5.5 0 0 1-1 0v-2A.5.5 0 0 1 8 0m0 13a.5.5 0 0 1 .5.5v2a.5.5 0 0 1-1 0v-2A.5.5 0 0 1 8 13m8-5a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1 0-1h2a.5.5 0 0 1 .5.5M3 8a.5.5 0 0 1-.5.5h-2a.5.5 0 0 1 0-1h2A.5.5 0 0 1 3 8m10.657-5.657a.5.5 0 0 1 0 .707l-1.414 1.415a.5.5 0 1 1-.707-.708l1.414-1.414a.5.5 0 0 1 .707 0m-9.193 9.193a.5.5 0 0 1 0 .707L3.05 13.657a.5.5 0 0 1-.707-.707l1.414-1.414a.5.5 0 0 1 .707 0m9.193 2.121a.5.5 0 0 1-.707 0l-1.414-1.414a.5.5 0 0 1 .707-.707l1.414 1.414a.5.5 0 0 1 0 .707M4.464 4.465a.5.5 0 0 1-.707 0L2.343 3.05a.5.5 0 1 1 .707-.707l1.414 1.414a.5.5 0 0 1 0 .708"/></svg>`
        root.setProperty(`--bg`,`hsl(0,0%,90%)`);
        root.setProperty(`--nav-bg`,`hsl(0,0%,91%)`);
        root.setProperty(`--clock-bg`,`linear-gradient(to bottom right, hsl(0,0%,78%) 70%, hsl(0,0%,87%) )`);

        root.setProperty(`--header`,`hsl(0,0%,10%)`);
        root.setProperty(`--text`,`hsl(0,0%,20%)`);

        root.setProperty(`--anchor`,`hsl(26,92%,55%)`);
        root.setProperty(`--anchor-hover`,`hsl(26,94%,50%)`);

        root.setProperty(`--higher-anchor`,`hsl(121,50%,42%)`);
        root.setProperty(`--higher-anchor-hover`,`hsl(121,72%,32%)`);

        root.setProperty(`--border`, `hsl(0,0%,0%)`);
        root.setProperty(`--error`, `hsl(0,86%,44%)`);
    }
}


export async function get(grade, attribute, length){ //Gets specified attribute from lessons.json. I added some flexibility thogh
    try{
        attribute = String(attribute); //for ease of access

        if(length === undefined){ length = false; } //Adds a default value to length to save time when calling the function

        //NEW VARAIBLES
        const response = await fetch(`JSON/lessons.json`);
        const data = await response.json();
        let processing; //Variable to ease the return process

        //GRADE CHECK
        if(grade < 1 || grade > 9){ //Error: Grade is invalid (not any integer 1-9)
            console.error(`ParameterError | try putting in a valid GCSE grade next time. | ${grade}`);
        }
        grade -= 1; //for indexes

        //ATTRIBUTE CHECKS
        if( [`name`,`names`].includes(attribute) ){ //Check: attribute is lesson.json -> `names`
            processing = data.names[grade];
        }

        else if( [`pdf`,`pdfs`].includes(attribute) ){ //Check: attribute is lessons.json -> `pdfs`
            processing = data.pdfs[grade];
        }

        else if( [`video`,`videos`,`link`,`links`].includes(attribute) ){ //Check: attribute is lessons.json -> video links
            processing = data.videos[grade];
        }

        else{ //Error: attribute is an invalid parameter/not in lessons.json
            console.error(`ParameterError | try putting in a valid attribute from lessons.json next time. | ${attribute} `);
        }

        //LENGTH CHECKS
        if(length === true){ //Returns: lessons.json -> `attribute` -> value (list) -> length
            processing = processing.length;
            
            //Video Processing Case
            if( [`video`,`videos`,`link`,`links`].includes(attribute) ){
                processing = lengthProcessing(data.videos[grade]);
                return processing;
            }

            else{return Number(processing);}
        } 

        else if(length === false){ //Returns: lessons.json -> `attribute` -> value (list)
            return processing;
        }

        else{ //Error: invalid length value
            console.error(`ParameterError | try putting in if you want the length or the list next time. | ${length}`);
        }
    }
    catch(error){throw error} //Error: Couldn`t fetch data from lessons.json
}


//Sub-Functions of get()
export function lengthProcessing(list){
    let counter = list.length; //Presets the length
    let currentList = list; //Sets the list

    for(let a = 0; a <= counter; a++){
        if(typeof currentList[a] === `object`){ //Checks if the current list item is a sublist
            counter -= 1; //Subtracts 1 from the length counter (we need to return all the elements in the list, not just all the strings & arrays)
            counter += lengthProcessing(currentList[a]); //Adds the length of the sublist back to the length counter using ✨Recursion✨ in order to account for any potential sublists in the sublist
        };
    }
    return Number(counter); //Sets the type of and returns the length counter
}

function listProcessing(list){
    let currentList = list; 
    let transferList = [];

    for(let a = 0; a <= list.length; a++){
        if(typeof list[a] === `object`){ //Checks if the current item in the list is a sublist and appends its items to the transfer list
            transferList = [...transferList, ...listProcessing(list[a])]; 
        }

        else{
            transferList.push(list[a]);

            if(typeof list[a] === `undefined`){ //Bug Fix: checks if the current element has type undefined and deletes it, this prematurely removes the undefined elements that used to show up in the final result
                transferList.pop();
            }
        }

    }
    return transferList;
}

async function getSpecific(grade,attribute,index){
    const processing = await get(grade,attribute,false);

    return processing[index];
}

async function intialiseCheckboxes(){
    for(let i = 1; i <= 9; i++){
        jLimit = await get(i,"name",true);
        for(let j = 1; j <= jLimit; j++){localStorage.setItem(`${i}-${j}`,"false")}
    }
}
