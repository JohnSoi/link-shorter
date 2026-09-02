import type { Component } from "vue";

interface IRouterItem {
    path: string;
    name: string;
    component: Component;
    header: string;
    icon?: Component;
    public?: boolean;
}

export type { IRouterItem };
