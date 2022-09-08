<template>
  <main :class="backgroundColors" :style="{ 'backgroundImage':this.backgroundColors}">
    <div>
      <h1 :style="textColorCompliment">Color Palette Generator</h1>
      <div v-if="copied == 1">
        <p class="status">Copied</p>
      </div>
      <div v-else-if="duplicateFlag == 1">
        <p class="status">Palette already saved</p>
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
          <input type="text" id="myInput" :value="color" />
          <button @click="copySingleColor(color)">copy</button>
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
          >
            <p>
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
      textColorCompliment: {
        color: '',
      },
      colors: [],
      savedPaletts: [],
      text: "",
      pallettDuplicateFlag: 0,
      copied: 0,
      duplicateFlag: 0,
      backgroundColors: []
    };
  },
  methods: {
    paletteGenerator() {
      this.colors = [];
      // let colorRGB = this.colors
      this.backgroundColors = [];
      for (let i = 0; i < 5; i++) {
        let randomColorHex = Math.floor(Math.random() * 16777215).toString(16);
        randomColorHex = "#" + randomColorHex;
        this.colors.push(randomColorHex);
        // let textColorCompliment = 0xFFFFFF ^ randomColorHex
        // console.log(textColorCompliment)
        // let blah = textColorCompliment.toString(16)
        // console.log(blah)
      }
      this.backgroundColors = `linear-gradient(to left, ${this.colors[0]}, ${this.colors[1]}, ${this.colors[2]}, ${this.colors[3]}, ${this.colors[4]}`
      this.textColorContrast(this.colors)
    },
    textColorContrast(colors){
      let rgbArr = []
      for (let color of colors ){
        color = color.replace('#', '')
        let r = parseInt(color.substring(0,2), 16)
        let g = parseInt(color.substring(2,4), 16)
        let b = parseInt(color.substring(4,6), 16)
        let singleColor = [r, g, b]
        rgbArr.push(singleColor)
      }
      let centerColor = rgbArr[2][1]

      if (centerColor <= 100){
        this.textColorCompliment.color = 'rgba(235,235,235, 1)'
      } else if ( centerColor > 200){
        this.textColorCompliment.color = 'rgba(0,0,0, 1)'
      }

    },
    savePalett() {
      let tempPalet = this.colors;
      const checker = this.savedPaletts[this.savedPaletts.length - 1];
      const paletteSize = this.savedPaletts.length;
      if (checker == this.colors) {
        this.pallettDuplicateFlag = 0;
        this.duplicateFlag = 1;
        setTimeout(() => {
          this.duplicateFlag = 0;
        }, 2500);
      } else {
        if (paletteSize >= 8) {
          this.savedPaletts.shift();
          this.savedPaletts.push(tempPalet);
          this.pallettDuplicateFlag = 1;
        } else {
          this.savedPaletts.push(tempPalet);
          this.pallettDuplicateFlag = 1;
        }
      }
    },
    timeOutHelper() {
      this.copied = 1;
      setTimeout(() => {
        this.copied = 0;
      }, 5000);
    },
    loadPalett(idx) {
      this.colors = this.savedPaletts[idx];
    },
    copyCurrent() {
      let currentRaw = this.colors;
      let currentCopy = currentRaw.toString();
      navigator.clipboard.writeText(currentCopy);
      this.timeOutHelper();
    },
    savePreviousPalett(previousPalett) {
      let palletRaw = this.savedPaletts[previousPalett];
      console.log(navigator);
      let palletCopy = palletRaw.toString();
      navigator.clipboard.writeText(palletCopy);
      this.timeOutHelper();
    },
    copySingleColor(code) {
      navigator.clipboard.writeText(code);
      this.timeOutHelper();
    },
  },
};
</script>




 
<style>
@import url('https://fonts.googleapis.com/css2?family=Indie+Flower&family=Lobster&family=Pacifico&display=swap');
/* fonts */
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
p {
  font-family: "Indie Flower", cursive;
}
.status {
  font-size: 3rem;
  margin: 0 auto;
}
main{
  width: 100vw !important;
  height: 100vh !important;
}
li {
  list-style: none !important;
}
li > p {
  color: aliceblue;
  font-size: 1.5em;
  margin: 0 auto;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
.colors {
  display: flex;
  justify-content: center;
  margin-top: 1em;
}
.box {
  margin: 1%;
  width: 10vw;
  height: 20vw;
  border: 2px black solid;
}
.code {
    display: flex;
    justify-content: center;
    flex-direction: column;
    align-items: center;
    /* background-color: black; */
    height: auto;
    width: 100%;
}
.code > p {
  text-align: center;
  font-size: 2rem;
  color: white;
}
.code > input {
  text-align: center;
}
.code > button{
  width: 50%;
  }
.saved {
  display: flex;
  justify-content: center;
}
.saved > h4 {
  display: flex;
  flex-direction: column;
  align-self: center;
  flex: 0 0;
}
button {
    font-family: 'Lobster', cursive;
    font-size: 1.5rem;
    border-radius: 8px;
}
button:hover{
  box-shadow: 1px 3px 5px 4px rgba(0,0,0,0.75);
}
</style>
