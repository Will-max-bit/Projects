<template>
  <main :class="backgroundColors" :style="{ 'backgroundImage':this.backgroundColors}">
    <div>
      <h1 :style="textColorCompliment">Color Palette Generator</h1>
      <div v-if="copied == 1">
        <p class="status" :style="textColorCompliment">Copied</p>
      </div>
      <div v-else-if="duplicateFlag == 1">
        <p :style="textColorCompliment" class="status">Palette already saved</p>
      </div>
      <div v-else>
        <p :style="textColorCompliment" class="status">Welcome to the Palette Generator</p>
      </div>
      <button @click="paletteGenerator">Generate New</button>
      <button @click="savePalett">Save Palette</button>
      <button @click="copyCurrent">Copy Palette</button>
    </div>
    <div class="colors">
      <div
        class="color box"
        v-for="(color, index) in colors"
        :key="index"
        :style="{ backgroundColor: color }"
      >
        <div class="code" :style="{ backgroundColor: color }">
          <select name="color-code" id="color-code" v-model="userColorCode" multiple>
            <option :style="{color: 'singleColorCompliment[index]', fontFamily: 'Pacifico'}" :value="color" @click="copySingleColor(color)"><p class="font"> {{color}}</p></option>
            <option :style="{color: 'singleColorCompliment[index]', fontFamily: 'Pacifico'}" @click="copySingleColor(this.rgbColors[index])"><p class="font">rgb{{this.rgbColors[index]}}</p></option>
          </select>
        </div>
      </div>
    </div>
    <h2 :style="textColorCompliment">My Saved Palettes</h2>
    <div class="saved" v-if="this.savedPaletts.length != 0">
      <ul
        v-for="(palette, index) in savedPaletts"
        class="SavePaletts"
        :key="index"
      >
        <button @click="loadPalett(index)">Load Palett</button>
        <button @click="savePreviousPalett(index)">Copy Palett</button>
        <div v-if="palletDuplicateFlag != 1">
          <li
            v-for="(paletteColor, idx) in palette"
            :key="idx"
            :style="{ backgroundColor: paletteColor }"
            class="saved-palettes"
          >
            <p :style="textColorCompliment" >
              {{ paletteColor }}
            </p>
          </li>
        </div>
        <div v-else></div>
      </ul>
    </div>
  </main>
</template>
<script>
export default {
  name: "App",
  components: {},
  data() {
    return {
      // styling for heading text
      textColorCompliment: { 
        color: "",
      },
      // styling for color code array text
      singleColorCompliment: [], 
      // background color gradient array
      backgroundColors: [], 
      // array of random colors in hex
      colors: [],
      // array of color palettes saved by click event
      savedPaletts: [],
      // array of current colors converted into rgb 
      rgbColors: [],
      // copied flag, 0 is false, when 1 is assigned copied appears in the dom
      copied: 0,
      // duplicate flag, 0 is false, when 1 is assigned duplicate appears in the dom
      duplicateFlag: 0,
      // v-model to color code picked, hex gets you a hex copy,rgb vice versa 
      userColorCode: '',
    };
  },
  methods: {
    // Generates intial random colors and also creates background
    paletteGenerator() {
      this.colors = [];
      this.backgroundColors = [];
      // random color loop
      for (let i = 0; i < 5; i++) {
        let randomColorHex = Math.floor(Math.random() * 16777215).toString(16);
        randomColorHex = "#" + randomColorHex;
        this.colors.push(randomColorHex);
      }
      // assigns background colors and flips them so contrast is somewhat maintained
      this.backgroundColors = `linear-gradient(to left, ${this.colors[0]}, ${this.colors[1]}, ${this.colors[2]}, ${this.colors[3]}, ${this.colors[4]}`;
      this.rgbConverter(this.colors)
    },
    // converts hex into rgb for easier text contrast responsiveness also triggers contrast functions to run
    rgbConverter(colors){
      let rgbArr = [];
            for (let color of colors) {
              color = color.replace("#", "");
              let r = parseInt(color.substring(0, 2), 16);
              let g = parseInt(color.substring(2, 4), 16);
              let b = parseInt(color.substring(4, 6), 16);
              let singleColor = [r, g, b];
              rgbArr.push(singleColor);
              // rgb colors is an array used to give the user multiple choices
              this.rgbColors.push(singleColor);
            }
      this.textColorContrast(rgbArr)
      this.singleColorContrast(rgbArr)
    },
    // most text is centered so header contrast is based off center color
    textColorContrast(rgbColors) {
      let centerColor = rgbColors[2][1]; 
      if (centerColor <= 100) {
        this.textColorCompliment.color = "rgba(235,235,235, 1)";
      } else if (centerColor > 100) {
        this.textColorCompliment.color = "rgba(0,0,0, 1)";
      }
    },
    // used to specifically target the text inside the palette blocks
    // non functional at the moment however
    singleColorContrast(rgbColors){
      let colors = rgbColors
      let singColorArr = []
      if (colors <= 100) {
        singColorArr.push("color: rgba(235,235,235, 1);")
      } else if (colors > 200) {
        singColorArr.push("color: rgba(0,0,0, 1);")
      }
      this.singleColorCompliment = singColorArr
    },
    // click event triggered to save current random palette
    savePalett() {
      // stores global colors property as local variable
      let tempPalet = this.colors;
      // the control for double saving a palette is checking to see if the last palette is equal to it.
      const checker = this.savedPaletts[this.savedPaletts.length - 1];
      // controls size of saved palette array
      const paletteSize = this.savedPaletts.length;
      // checking if palette is saved and adjusting flags based off that
      if (checker == this.colors) {
        this.duplicateFlag = 1;
        // resetting the flag so the message disappears
        setTimeout(() => {
          this.duplicateFlag = 0;
        }, 2500);
      } else {
        // if it is >= saved array will be reduced by one (first index) and new saved palette will be added 
        if (paletteSize >= 6) {
          this.savedPaletts.shift();
          this.savedPaletts.push(tempPalet);
        } else {
          this.savedPaletts.push(tempPalet);
        }
      }
    },
    // controls set timeout for copied message
    timeOutHelper() {
      this.copied = 1;
      setTimeout(() => {
        this.copied = 0;
      }, 5000);
    },
    // loading the palette at index clicked
    loadPalett(idx) {
      this.colors = this.savedPaletts[idx];
    },
    // copies the current color array to clipboard
    copyCurrent() {
      let currentRaw = this.colors;
      let currentCopy = currentRaw.toString();
      navigator.clipboard.writeText(currentCopy);
      this.timeOutHelper();
    },
    // copies the previous color array to clipboard
    savePreviousPalett(previousPalett) {
      let palletRaw = this.savedPaletts[previousPalett];
      let palletCopy = palletRaw.toString();
      navigator.clipboard.writeText(palletCopy);
      this.timeOutHelper();
    },
    // copies single color
    copySingleColor(code) {
      navigator.clipboard.writeText(code);
      this.timeOutHelper();
    },
  },
};
</script>
<style>
@import url("https://fonts.googleapis.com/css2?family=Indie+Flower&family=Lobster&family=Pacifico&display=swap");
/* layout */
body {
  margin: 0 auto;
}
main {
  width: 100vw !important;
  height: 100vh !important;
}
li {
  list-style: none !important;
}
.box {
    margin: 1%;
    width: 10vw;
    height: 20vw;
    border: 2px black solid;
    display: flex;
}
.colors {
    display: flex;
    justify-content: center;
    margin-top: 1em;
}
.code {
    display: flex;
    justify-content: center;
    flex-direction: column;
    align-items: center;
    height: auto;
    width: 100%;
}
.SavePaletts{
  margin: 0;
}
.saved {
  display: flex;
  justify-content: center;
}
/* fonts and text layout */
h1,
h2 {
  font-family: "Pacifico", cursive;
}
h1 {
  font-size: 4rem;
  margin: 0 auto;
}
h2 {
  font-size: 2.5rem;
  margin: 0 auto;
}
.font{
  font-family: "Indie Flower", cursive !important;
}
p {
  font-family: "Indie Flower", cursive;
}
.status {
  font-size: 3rem;
  margin: 0 auto;
}
li > p {
  color: aliceblue;
  font-size: 1.5em;
  margin: 0 auto;
}
.code > p {
  text-align: center;
  font-size: 2rem;
  color: white;
}
.code > input {
  text-align: center;
}
.saved > h4 {
  display: flex;
  flex-direction: column;
  align-self: center;
  flex: 0 0;
}
#color-code {
    background: transparent;
    border-style: none;
    overflow: hidden;
    text-align: center;
}
select > option:hover{
font-size: 1.5rem;
transition: 0.3s;
padding: 2%;
}
select > option{
  margin: 1rem;
  font-size: 1.25rem;
}
/* inputs */
.code > button {
  width: 50%;
}
button {
  font-family: "Lobster", cursive;
  font-size: 1.5rem;
  border-radius: 8px;
}
button:hover {
  box-shadow: 1px 3px 5px 4px rgba(0, 0, 0, 0.75);
}
/* individuals selections */
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
.saved-palettes{
  border: solid 1px;
}
</style>
