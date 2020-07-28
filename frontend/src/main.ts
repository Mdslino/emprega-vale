import Vue from "vue";
import App from "./App.vue";
import "./registerServiceWorker";
import router from "./router";
import store from "./store";
import Buefy from "buefy";
import "./assets/scss/app.scss";

Vue.use(Buefy);

Vue.config.productionTip = false;

new Vue({
  router: router,
  store: store,
  render: h => h(App)
}).$mount("#app");
