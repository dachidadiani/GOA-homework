// 1 Create an object representing a person with properties like name, age, and city.
const pesonalinfo={
    name: Dachi ,
    age: 14 ,
    city: rustavi ,
}

//5 Delete the city property from the person object.

delete personalinfo.city;



//4 Add a new property hobby to the person object from Task 1 and assign it a value.
personalinfo.hobby = "hobbyhorsing"




//3 Take the person object from Task 1 and change the age property to a new value
personalinfo.age=300




console.log(pesonalinfo) 

//2 Create an object car with properties make, model, and year. Access and print each property.
 
const car={
    year:2020,
    model:maybach,
    color:black
} 
console.log(car.year)
console.log(car.model)
console.log(car.color)


//6 Create an object calculator with properties a, b, and a method add() that returns the sum of a and b.
const calculator = {
    a: 0,
    b: 0,
    
    add: function() {
      return this.a + this.b;
    }
  };
  
  
  calculator.a = 5;
  calculator.b = 3;
  
  console.log(calculator.add());

  //7 Create 3 different objects, each representing a different book. Each object should have properties title, author, and pages.

  function Book(title, author, pages) {
    this.title = title;
    this.author = author;
    this.pages = pages;
  }
  
  let book1 = new Book("sherlok holms " , "arturkonardoil", 1200 );
  let book2 = new Book( "think and grow rich" , "napoleon hill", 360);
  let book3 = new Book("წარმატების 365 გასაღები", "i dont remember", 365);
  
  console.log(book1);
  console.log(book2);
  console.log(book3);

  //8  Write a constructor function Animal that creates an object with properties name and sound. Add a method makeSound() that prints the sound.

  function Animal(name, sound) {
    this.name = name;
    this.sound = sound;
    
    this.makeSound = function() {
      console.log(this.sound);
    };
  }
  
  //9 Use the Animal constructor to create two animals: a cat and a dog, each with 
 
  let dog = new Animal("Dog", "Bark");
  let cat = new Animal("Cat", "Meow");
  
  dog.makeSound(); 
  cat.makeSound(); 
  
  //10 ver gavige