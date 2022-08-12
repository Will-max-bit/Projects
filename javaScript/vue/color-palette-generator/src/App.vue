<template>
<div>
  <h1>Color Palette</h1>
  <button @click="paletteGenerator">checking</button>
</div>
<div class="colors">
  <div class="color box" v-for="(color, index) in colors" :key="index"  :style="{backgroundColor: color, }">

    <div class="code">
      <p>
{{color}}
      </p>
      </div>
  </div>
</div>
</template>

<script>


export default {
  name: 'App',
  components: {
    
  },
  data (){
    return{
      colors: [],
    }
  },
  methods: {
    paletteGenerator(){
      this.colors = []
      for (let i = 0; i < 5; i++){
        let randomColor = Math.floor(Math.random()*16777215).toString(16)
        randomColor = '#' + randomColor
        this.colors.push(randomColor)
      }
      console.log(this.colors)
    }
  }
}
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
.colors{
  display: flex;
  justify-content: space-evenly;
}
.box{
  width: 20vw;
  height: 40vw;
}
.code{
  display: flex;
  justify-content: center;
  background-color: black;
  height: auto;
  width: 30%;
}
.code > p{
  text-align: center;
  font-size: 2rem;
  color: white;
}
</style>
