import { createApp } from "vue";
import App from "./App.vue";
import { shallowRef } from "vue";
import { ref } from "vue";

const app = createApp(App);
app.use(shallowRef);
app.use(ref);
app.mount("#app");
// createApp(App).mount("#app");
