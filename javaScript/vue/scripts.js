let app = new Vue({
    el: '#app',
    data: {
    message : 'hello world!',
    names : '',
    sortingHat: ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"],
    houses: {
        Gryffindor: 0,
        Hufflepuff: 0,
        Ravenclaw: 0,
        Slytherin: 0,
    },

    quiz: {
      "questions":[
          {
              "text": "You've made it to Hogwarts, which means you've already bought a wand from Ollivander's. What material is at its core?",
              "answers": ['Phoenix Feather', 
                        'Dragon Heartstring', 
                        'Unicorn Hair', 
                        'idk, I want to start now']  
          },
          {
            "text": "During the end-of-year exams, you notice that one of your classmates was using an enchanted quill. You come top of the class anyway, but they are second. What do you do?",
            "answers": ["Tell the professor immediately, cheating is wrong, no matter what.", 
                        "Nothing, but if I hadn't come top of the class, I'd definitely tell the professor.",
                        "Encourage the other student to admit what they'd done to the professor.", 
                        "Give them a high five for managing to sneak the quill into the exam" ]
          },
          {
            "text": "You would be most hurt if a person called you...",
            "answers": ["weak", "ignorant", "unkind", "boring"]
          },
          {
            "text": "You're locked in a duel with a skilled opponent. They fire an unknown spell at you, and you shout…",
            "answers": ["expelliarmus!", "Protego!", "Stupefy!", "Crucio!"]
          },
          {
            "text": "It's your fifth year at Hogwarts, and you've just received a Howler from your parents. What for?",
            "answers": ["Sneaking into the Forbidden Forest at night on a dare.", "Getting caught cheating in my Divination O.W.L", "Being put in detention after I was caught in the library after hours.", "Nothing! I'd never do anything to warrant a Howler."]
          },
          {
            "text": "And finally: We know that the Sorting Hat takes into account your preferences. So which Hogwarts house do you feel you identify with most closely?",
            "answers": ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
          }
      ]  
    },
    preference: '',
    chosenHouse: '',
    },
    methods: {
        // site undergoing maintence, unused code for now
        pottergeneral: function(){
            axios({
                method: 'get',
                url: 'http://hp-api.herokuapp.com/api/characters',
            }).then(response => {
                this.names = response.data
                console.log(this.names)
                for (let value of this.names){
                }
                this.names = response.data.house

            })
        }, 
        // loops through houses object the total int to marker
        questionFunc: function(){
            let marker = 0
            for (let highHouse in this.houses){
                if (marker <= this.houses[highHouse]){
                    marker = this.houses[highHouse]
                }else{
                    continue
                }
            }// marker is used to find the property with the highest int value
            this.chosenHouse = Object.keys(this.houses).find(key => this.houses[key] === marker)
        },
        charCount: function(item, idx){
            // checks the answers to see if any of them are the sorting hat list,
            // if true, option selected is given extra points
            const found = this.sortingHat.find(element => element == idx)
            let house = this.sortingHat[item]
            this.houses[house] ++
            if (found != undefined){
                this.houses[house] += 3
                this.preference = found
            }
        },
        
    },
    created: function (){
        
    }
})
