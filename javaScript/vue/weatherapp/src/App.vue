<template>
  <div id="app" :class="backgroundClass">
    <head>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@48,400,0,0" />
</head>
    <div class="current">
    <p class="title">Weather</p>
      
      <div class="user-input">
        <div class="search">
        <input class="searchinput" type="text" placeholder="search for a location" v-model="userInput" v-on:keyup.enter="weatherCall" />
          <a href="#" @click="weatherCall">
            
              <span class="material-symbols-outlined">
                search
                </span>
          </a>
        </div>
        <div class="daily" v-if="Object.keys(dailyWeatherData).length != 0">
          <img
            :src="dailyWeatherSanitized.icon"
            :alt="dailyWeatherSanitized.description"
            srcset=""
          />
          <div class="daily-data">
          <p>
            {{ dailyWeatherSanitized.currentDate }}
          </p>
          <p>
            {{ dailyWeatherSanitized.description }}
          </p>
          <p>
            {{ dailyWeatherSanitized.currentTimeSanitized }}
          </p>
          <p>
           <strong>Sunrise</strong> {{ dailyWeatherSanitized.sunRise }}
          </p>
          <p>
           <strong>Sunset</strong> {{ dailyWeatherSanitized.sunSet }}
          </p>
          <p>
           <strong>Feels Like </strong> {{ dailyWeatherSanitized.tempCurrent }} degrees
          </p>
          </div>
        </div>
        <div class="blank" v-else>
        </div>
        </div>
    </div>
    <div class="weekly" v-if="weeklyWeather.length != 0">
      <div v-for="temp in hiLow" class="forcast-daily" :key="temp.id">
        <img
            :src="temp[0].icon"
            :alt="temp[0].description"
            srcset=""
          />
        <p>
          {{ temp[0].date }}
        </p>
        <p>
          {{ temp[0].conditions }}
        </p>
        <p>
         <strong>High</strong> {{ temp[0].high }}
        </p>
        <p>
         <strong>Low</strong> {{ temp[0].lo }}
        </p>
      </div>
    </div>
    <div v-else-if="weeklyWeather == 0">blank</div>
    <!-- <button @click="forecastCalc">testing</button> -->
  </div>
</template>
<script>
export default {
  name: "app",
  data() {
    return {
      key: "96dca771c24bb69ad2789f2ab59fb3ab",
      userInput: "",
      url: "https://api.openweathermap.org/data/2.5/",
      weeklyWeather: {},
      dailyWeatherData: {},
      dailyWeatherSanitized: [],
      lat: "",
      long: "",
      hiLow: [],
      hourCheck: 0,
      sunsetCheck: 0,
      sunriseCheck: 0,
      condition: '',
      backgroundClass: '',
    };
  },
  methods: {
    weatherCall: function () {
      if (this.userInput != "") {
        fetch(`${this.url}weather?q=${this.userInput}&APPID=${this.key}`)
          .then((response) => {
            return response.json();
          })
          .then(this.setDaily);
      }
    },
    forecastCall: function () {
      fetch(
        `${this.url}forecast?lat=${this.lat}&lon=${this.long}&APPID=${this.key}`
      )
        .then((response) => {
          return response.json();
        })
        .then(this.setWeekly);
      // this.forecastCalc();
    },
    backgroundCalc: function(){
      if (Object.keys(this.dailyWeatherData).length < 1){
        this.backgroundClass = 'default'
      }
      let hourCheck = this.hourCheck
      let conditionCheck = this.condition.split(" ")
      if (hourCheck > this.sunriseCheck && hourCheck < this.sunsetCheck){
        if('clouds' == conditionCheck[1]){
          this.backgroundClass = 'cloudyDay'
        }else if ('rain' == conditionCheck[1]){
          this.backgroundClass = 'rainyDay'
        }else if ('clear' == conditionCheck[0]){
          this.backgroundClass = 'clearDay'
        }
      }
      else{
        if('clouds' == conditionCheck[1]){
          this.backgroundClass = 'cloudyNight'
        }else if ('rain' == conditionCheck[1]){
          this.backgroundClass = 'rainyNight'
        }else if ('clear' == conditionCheck[0]){
          this.backgroundClass = 'clearNight'
        }
      }
    },
    setDaily(results) {
      this.dailyWeatherData = results;
      this.lat = this.dailyWeatherData.coord.lat;
      this.long = this.dailyWeatherData.coord.lon;
      this.forecastCall();
      this.dailyCalc();
    },
    setWeekly(results) {
      this.weeklyWeather = results.list;
      this.forecastCalc();
    },
    dateFormater(date){
      let rawDate = new Date(date)
      let months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
      ];
      let days = [
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
      ];
      let day = days[rawDate.getDay()]
      let sanitizedDate = rawDate.getDate()
      let month = months[rawDate.getMonth()]
      let year = rawDate.getFullYear()
      return `${day} ${month} ${sanitizedDate} ${year}`
    },
    timeBuilder(time){
      let rawTime = new Date(time * 1000)
      let currentHours = (rawTime.getHours() - 12)
      let currentMinutes = (rawTime.getMinutes())
      let amPmCheck = (rawTime.getHours())
      let timeOfDay = amPmCheck > 12 ? 'p.m' : 'a.m'
      let currentTime = currentHours + ':' + currentMinutes + ' ' + timeOfDay
      return currentTime
    },
    hourFormater(hourpassed){
      hourpassed = new Date(hourpassed)
      let sanitizedHour = hourpassed.getHours()
      return sanitizedHour
    },
    dailyCalc() {
      let currentDate = this.dateFormater(this.dailyWeatherData['dt'] * 1000)
      let currentTimeSanitized = this.timeBuilder(this.dailyWeatherData['dt'])
      
      let hourPass = this.hourFormater(new Date(this.dailyWeatherData['dt'] * 1000))
      let sunSetPass = this.hourFormater(this.dailyWeatherData["sys"]["sunset"] * 1000)
      let sunRisePass = this.hourFormater(this.dailyWeatherData["sys"]["sunrise"] * 1000)
      this.sunriseCheck = sunRisePass
      this.sunsetCheck = sunSetPass
      this.hourCheck = hourPass


      let tempCurrent = parseInt(
        ((this.dailyWeatherData["main"]["feels_like"] - 273.15) * 9) / 5 + 32
      );
      let sunRise = this.timeBuilder(this.dailyWeatherData["sys"]["sunrise"])
      sunRise = sunRise.slice(1)
      let sunSet = this.timeBuilder(this.dailyWeatherData["sys"]["sunset"])
      let description = this.dailyWeatherData["weather"][0]["description"]
      this.condition = description
      let icon =
        "http://openweathermap.org/img/wn/" +
        this.dailyWeatherData["weather"][0]["icon"] +
        "@4x.png";
      this.dailyWeatherSanitized = {
        currentDate: currentDate,
        currentTimeSanitized: currentTimeSanitized,
        tempCurrent: tempCurrent,
        sunRise: sunRise,
        sunSet: sunSet,
        description: description,
        icon: icon,
      };
      this.backgroundCalc()
    },
    forecastCalc: function () {
      let control = 0;
      ("use strict");
      let hi = 0;
      let low = 1000;
      for (let [key, value] of Object.entries(this.weeklyWeather)) {
        if (control <= 8) {
          hi =
            hi > value["main"]["temp_max"]
              ? hi
              : (hi = value["main"]["temp_max"]);
          low =
            low < value["main"]["temp_min"]
              ? low
              : (low = value["main"]["temp_min"]);
          control++;
          
          if (control == 8) {
            let dayConditions = value["weather"][0]["description"];
            let dayHigh = parseInt(((hi - 273.15) * 9) / 5 + 32);
            let dayLow = parseInt(((low - 273.15) * 9) / 5 + 32);
            let dayDate = this.dateFormater(value["dt"] * 1000);
            let icon =
                      "http://openweathermap.org/img/wn/" +
                      value["weather"][0]["icon"] +
                      "@4x.png";
            key = {
              high: dayHigh,
              lo: dayLow,
              date: dayDate,
              conditions: dayConditions,
              icon: icon,
            };
            this.hiLow.push([key]);
            control = 0;
          }
        }
      }
    
    },
  },
  created: function(){
    this.backgroundCalc()
  },
};
</script>
<style>
@import url('https://fonts.googleapis.com/css2?family=Azeret+Mono:wght@100&family=Source+Code+Pro:ital@1&display=swap');
</style>
<style>
/* responsive */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}
#app{
  width: 100vw !important;
  height: 100vh !important;
}
.current {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    min-height: 50vh;
    max-width: 100vw;
    font-size: 2rem;
}

.daily {
    justify-content: center !important;
    text-align: center;
    max-width: 20vw;
    background-color: rgb(236 221 229 / 50%) !important;
    background-blend-mode: multiply;
    border-radius: 15%;
    margin: 1rem;
}
.daily-data{
  margin: 1rem;
}
.weekly{
  display: flex;
  justify-content: center;
  /* height: 40vh; */
  align-items: center;
}
.weekly > *{
  margin: 1rem;
}
/* end responsive */
/* user input */
.search{
  border: 2px solid #0c0909;
  border-radius: 30px;
  padding: 5px;
  background-color: white;
  display: flex;
  justify-content: center;
}
.searchinput{
  border: none !important;
  margin-left: 1rem;
}
.searchinput:focus, input:focus{
  outline: none;
}
/* background classes */
.default{
  background-image: url("./assets/default.png");
  background-size: cover;
  background-position: bottom;
  transition: 0.4s;
}
.forcast-daily{
  background-color: rgb(236 221 229 / 50%) !important;
  background-blend-mode: multiply;
  border-radius: 15%;
  text-align: center;
}
    /* responsive BG */
.clearNight{
  background-image: url("./assets/clearnight.png");
  background-size: cover;
  background-position: bottom;
  transition: 0.4s;
}
.rainyNight{
  background-image: url("./assets/rainynight.png");
  background-size: cover;
  background-position: bottom;
  transition: 0.4s;
}
.cloudyNight{
  background-image: url("./assets/cloudynight.png");
  background-size: cover;
  background-position: bottom;
  transition: 0.4s;
}
.cloudyDay{
  background-image: url("./assets/cloudyday.png");
  background-size: cover;
  background-position: bottom;
  transition: 0.4s;
}
.rainyDay{
  background-image: url("./assets/rainyday.png");
  background-size: cover;
  background-position: bottom;
  transition: 0.4s;
}
.rainyDay{
  background-image: url("./assets/rainyday.png");
  background-size: cover;
  background-position: bottom;
  transition: 0.4s;
}
.clearDay{
  background-image: url("./assets/sunnyday.png");
  background-size: cover;
  background-position: bottom;
  transition: 0.4s;
}
/* fonts */
.title{
  font-size: 2.5rem !important;
  text-align: center;
  color: whitesmoke;
  font-family: 'Source Code Pro', monospace;
}
p{
  font-family: 'Azeret Mono', monospace;
}

</style>
