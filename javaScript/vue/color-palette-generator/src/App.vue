<template>
  <div>
    <h1>Color Palette</h1>
    <div v-if="copied == 1">
      <p>Copied</p>
    </div>
    <div v-else-if="duplicateFlag == 1">
      <p>Palette already saved</p>
    </div>
    <div v-else>
      <p>Welcome to the Palette Generator</p>
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
      <div class="code">
        <input type="text" id="myInput" :value="color" />
        <button @click="copy(color)">copy</button>
      </div>
    </div>
  </div>
  <div class="saved" v-if="this.savedPaletts.length != 0">
    <h4>my saved palettes</h4>
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
          {{ paletteColor }}
        </li>
      </div>
      <div v-else></div>
    </ul>
  </div>
</template>

<script>
export default {
  name: "App",
  components: {},
  data() {
    return {
      colors: [],
      savedPaletts: [],
      text: "",
      pallettDuplicateFlag: 0,
      copied: 0,
      duplicateFlag: 0,
    };
  },
  methods: {
    paletteGenerator() {
      this.colors = [];
      for (let i = 0; i < 5; i++) {
        let randomColor = Math.floor(Math.random() * 16777215).toString(16);
        randomColor = "#" + randomColor;
        this.colors.push(randomColor);
      }
    },
    savePalett() {
      let tempPalet = this.colors;
      const checker = this.savedPaletts[this.savedPaletts.length - 1];
      const paletteSize = this.savedPaletts.length
      if (checker == this.colors) {
        this.pallettDuplicateFlag = 0;
        this.duplicateFlag = 1;
        setTimeout(() => {
          this.duplicateFlag = 0;
        }, 2500);
      } else {
        if (paletteSize >= 8){
          this.savedPaletts.shift()
          this.savedPaletts.push(tempPalet);
          this.pallettDuplicateFlag = 1;
        } else{
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
      let palletCopy = palletRaw.toString();
      navigator.clipboard.writeText(palletCopy);
      this.timeOutHelper();
    },
    copy(code) {
      navigator.clipboard.writeText(code);
      this.timeOutHelper();
    },
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.colors {
  display: flex;
  justify-content: space-evenly;
  margin-top: 2em;
}
.box {
  width: 10vw;
  height: 30vw;
  border: 2px black solid;
}
.code {
  display: flex;
  justify-content: center;
  background-color: black;
  height: auto;
  width: 100%;
}
.code > p {
  text-align: center;
  font-size: 2rem;
  color: white;
}
.saved {
  display: flex;
  justify-content: center;
  flex-direction: column;
}
.saved > h4 {
  display: flex;
  flex-direction: column;
  align-self: center;
  flex: 0 0;
}
</style>
