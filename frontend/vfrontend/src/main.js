
import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import "bootstrap/dist/css/bootstrap.css";

// import BootstrapVue from 'bootstrap-vue';
import "bootstrap/dist/js/bootstrap.bundle.js"
// Vue.config.productionTip = false;
// Vue.use(BootstrapVue)
import instance from "./axios";

createApp(App).use(store).use(router).mount("#app");
