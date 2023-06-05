function reverseWords(str) {
    // Split the string into an array of words.
    const words = str.split(" ");
  
    // Reverse each word in the array.
    for (let i = 0; i < words.length; i++) {
      words[i] = words[i].split("").reverse().join("");
    }
  
    // Join the array of words back into a string.
    return words.join(" ");
  }