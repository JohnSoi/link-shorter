import  { type Component, type Ref } from "vue";

type TCurrentRouterName = Ref<string | null>;

interface IMenuItem {
    label: string;
    route: string;
    name: string;
    icon?: Component;
}

interface IUseMenu {
    menuItems: IMenuItem[];
    currentRouteName: TCurrentRouterName;
}

export type { IMenuItem, IUseMenu, TCurrentRouterName };
