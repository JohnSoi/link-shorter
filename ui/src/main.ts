import { createApp } from "vue";
import { createPinia } from "pinia";
import { router } from "@/router";
import PrimeVue from "primevue/config";
import Aura from "@primeuix/themes/aura";
import App from "@/App.vue";
import "@/style.css";

const app = createApp(App);

app.use(createPinia());
app.use(router);
app.use(PrimeVue, {
    theme: {
        preset: Aura
    },
    license:
        "eyJpZCI6ImQyNGUwMjFjLWZkMzYtNDZhNi1hYmI2LTk1YmMzZmU0YmE3YSIsInByb2R1Y3QiOiJwcmltZXVpIiwidGllciI6ImNvbW11bml0eSIsInR5cGUiOiJkZXYiLCJpYXQiOjE3ODgyMjk0OTQsImV4cCI6MTgxOTc2NTQ5NH0.VcllDxsK8ULvl3FK04Jb2kMEBHQ1eCEqtJCKEZKAHOPjO21VCauD9bPXzIUvJ-dkSof0tjzumodTPJFrx1DlBQ"
});

app.mount("#app");
