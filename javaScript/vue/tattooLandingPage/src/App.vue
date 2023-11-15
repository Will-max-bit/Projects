<template>
  <link rel="stylesheet"
    href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0" />
  <link rel="stylesheet"
    href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0" />
  <h1 id="artist">Sasha Tattoos</h1>
  <nav class="nav-bar">
    <a class="nav-btn" target="_blank" @click="sceneChange('SiteHome')">Home</a>
    <a class="nav-btn" target="_blank" @click="sceneChange('OurWork')">Our Work</a>
    <a class="nav-btn" target="_blank" @click="sceneChange('AboutUs')">About Us</a>
    <a class="nav-btn" target="_blank" @click="sceneChange('ContactUs')">Contact Us</a>
  </nav>
  <transition name="fade" mode="out-in">
    <component :is="activeComponent"></component>
  </transition>
</template>

<script>
import SiteHome from './components/Site-Home.vue'
import OurWork from './components/OurWork.vue'
import AboutUs from './components/AboutUs.vue'
import ContactUs from './components/ContactUs.vue'
import { shallowRef } from 'vue'

export default {
  name: 'App',
  components: {
    SiteHome,
    OurWork,
    AboutUs,
    ContactUs,
    navigator: false
  },
  data() {
    return {
      activeComponent: SiteHome,

    }
  },
  methods: {
    sceneChange(value) {
      this.activeComponent = shallowRef(value)
    },
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Alfa+Slab+One&family=Handjet&family=Noto+Serif+Display:ital,wght@1,300&family=Sedgwick+Ave+Display&display=swap');

body {
  background-color: black;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #b3adad;
  height: 100vh;
}

a {
  font-family: 'Handjet', sans-serif;
  transition: scale 1s ease;
}

a:hover {
  scale: 1.2;
  text-decoration: underline;
}

a,
img,
button {
  cursor: pointer;
}

nav {
  display: flex;
  justify-content: right;
  position: relative;
  right: 5%;
  margin: 4rem;
}

.nav-btn {
  margin: 1rem;
  font-size: 2em;
}

#artist {
  color: #b3adad;
  text-align: left;
  margin: 0 auto;
  padding: 0;
  font-size: 4rem;
}

.content>transistion {
  position: absolute;

}


.fade-enter-active,
.fade-leave-active {
  transition: opacity 1s ease-in;
}

.fade-enter-from,
.fade-leave-to {
  transition: opacity 1s ease-out;
  opacity: 0;
}

nav {
  display: flex;
  justify-content: right;
  margin: 0 auto;
}
</style>
