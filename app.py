let port = 443;
let host = "localhost";

// Sample Numbers
let a = 60;
let b = 50;

// Arithmetic Operations
console.log("Server running on " + host + ":" + port);

console.log("Addition: " + (a + b));
console.log("Subtraction: " + (a - b));
console.log("Multiplication: " + (a * b));
console.log("Division: " + (a / b));
console.log("Modulus: " + (a % b));

// Comparison Operations
console.log("Is a equal to b? " + (a == b));
console.log("Is a greater than b? " + (a > b));
console.log("Is a less than b? " + (a < b));

// Logical Operations
console.log("a > 5 AND b < 15: " + (a > 5 && b < 15));
console.log("a < 5 OR b < 15: " + (a < 5 || b < 15));

// Increment & Decrement
a++;
b--;
console.log("Incremented a: " + a);
console.log("Decremented b: " + b);
console.log("All is well......");
