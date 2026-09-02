import { createRouter, createWebHistory, type Router, type RouteRecordRaw } from "vue-router";
import HomeView from "@/views/HomeView.vue";
import Home from "@primeicons/vue/home";
import type { IRouterItem } from "@/types";

export const routes: IRouterItem[] = [
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
    routes: routes as RouteRecordRaw[]
});
