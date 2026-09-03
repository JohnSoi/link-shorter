import { createRouter, createWebHistory, type Router, type RouteRecordRaw } from "vue-router";
import HomeView from "@/views/HomeView.vue";
import { Home, ChartScatter } from "@primeicons/vue";
import type { IRouterItem } from "@/types";
import type { Component } from "vue";

export const routes: IRouterItem[] = [
    {
        path: "/",
        name: "home",
        component: HomeView,
        header: "Главная",
        icon: Home,
        public: true
    },
    {
        path: "/statistics",
        name: "statistics",
        component: (): Promise<Component> => import("@/views/StatisticsView.vue"),
        header: "Статистика",
        icon: ChartScatter,
        public: true
    },
    {
        path: "/404",
        name: "notFound",
        component: (): Promise<Component> => import("@/views/NotFoundView.vue")
    },
    {
        path: "/link/:pathMatch(.*)*",
        name: "link",
        component: (): Promise<Component> => import("@/views/RedirectPage.vue")
    }
];

export const router: Router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: routes as RouteRecordRaw[]
});
