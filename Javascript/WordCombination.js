
//original - Original array of words to calculate for combination
//pointWords - the points selected for word combination 
const ProcessCombination = (original, pointWords, result ) => {

    //get those items which are not in the Point Words yet
    const originalWithoutPoints = original.filter((o) => {  
        return !pointWords.includes(o);
    });
	    
    for(let w of originalWithoutPoints){
		//clone the point word as they work as in Reference.
        const clonePointWords = pointWords.slice(0); 		 
        //add the new item to Point list (which itself is a unique combination)
        clonePointWords.push(w);  
		//add the combination to the final result.
        result.push(clonePointWords); 
        //Call recersively to explore other items which are not in Point Words
        ProcessCombination(original, clonePointWords, result);
    }
};

const Start = (listOfWords) => {  
	//Final array result
	const result = [];
	//Loop all the word items and send for each possible Combinatin.
	listOfWords.forEach((word,index,arr) => { 
        ProcessCombination(arr, [word], result);
    }, this );
	
	for (let inner of result){ 
		console.log(inner);  
	}	
};

Start(['A','B','C']);