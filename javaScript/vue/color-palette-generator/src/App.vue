<template>
  <div>
    <h1>Color Palette</h1>
    <button @click="paletteGenerator">checking</button>
    <button @click="savePalett">Save Pallet</button>
  </div>
  <div class="colors">
    <div
      class="color box"
      v-for="(color, index) in colors"
      :key="index"
      :style="{ backgroundColor: color }"
    >
      <!-- make way to store pallets  -->
      <div class="code">
        <!-- <a type="text" 
        v-on:focus="$event.target.select()"
        ref='myInput'
        readonly
        :value="text"
        
        > -->
        <input type="text" id="myInput" :value="color">
          {{ color }}
          <button @click="copy">copy</button>
        <!-- </a> -->
      </div>
    </div>
    <div class="saved" v-if="this.savedPaletts.length != 0">
      <h4>my saved palettes</h4>
      <ul v-for="(pallet, index) in savedPaletts" :key="index">
        <button @click="loadPalett(index)"> Load Palett</button>
        <li v-for="(palletColor, idx) in pallet" :key="idx" :style="{ backgroundColor: palletColor }">{{palletColor}}</li>
      </ul>
      <div v-if="this.palletDuplicateFlag == true">
        <p>Pallet Already saved</p>
      </div>
    </div>
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
      text: '',
      pallettDuplicateFlag: false,
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
    savePalett(){
      let tempPalet = this.colors
      const checker = this.savedPaletts[this.savedPaletts.length - 1]
      if ( checker == this.colors){
        console.log('dup pallet')
        this.pallettDuplicateFlag = true
        }
      else{
        // console.log('it works')
        console.log('new pallet')
        this.savedPaletts.push(tempPalet)
        console.log(this.savedPaletts.length)
        this.pallettDuplicateFlag = false
        // if ( this.savedPaletts.length > 1){
        // }
      }
    },
    loadPalett(idx){
      console.log(idx)
      this.colors = this.savedPaletts[idx]
    },
    copy (){
      let copyText = document.getElementById("myInput")
      copyText.select()
      copyText.setSelectionRange(0, 99999)
      navigator.clipboard.writeText(copyText.value)
      alert(copyText.value)
      // this.$refs.myInput.focus()
      // document.execCommand('copy')
    }
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
</style>
