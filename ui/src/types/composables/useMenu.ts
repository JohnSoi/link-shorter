import type { Component } from "vue";

interface IMenuItem {
    label: string;
    route: string;
    active: boolean;
    icon?: Component;
}

interface IUseMenu {
    menuItems: IMenuItem[];
}

export type { IMenuItem, IUseMenu };
