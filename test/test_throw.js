try {
    throw 60; 
} 
catch (e) {
    if (e <= 50) {
        console.log("e is less than 50");
    } else {
        console.log("e is greater than 50");
    }
}