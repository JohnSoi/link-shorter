import { createRouter, createWebHistory, type Router } from "vue-router";
import HomeView from "@/views/HomeView.vue";
import Home from '@primeicons/vue/home';

export const routes = [
    {
        path: "/",
        name: "home",
        component: HomeView,
        header: "Главная",
        icon: Home,
        public: true
    }
];

export const router: Router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes
});
