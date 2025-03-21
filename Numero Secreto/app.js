alert('Welcome to the game of the secret number');
let maximumNumber = 6000
let secretNumber = parseInt(Math.random() * maximumNumber + 1);
let attempt
let trying = 1

while (attempt != secretNumber){
        attempt = prompt(`Choose a number between 1 and ${maximumNumber}`);

        if (attempt == secretNumber) {
                alert(`Congrats, you just hit the rigth number ${secretNumber} and you needed ${trying} attempts`);
        } else {
                if(secretNumber > attempt){
                        alert (`Its a bigger number then ${attempt}`);
                } else {
                        alert(`its a minor number then ${attempt}`);
                }
        trying++;
        }

}
