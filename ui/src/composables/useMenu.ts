import { routes } from "@/router";
import { type Router, useRouter } from "vue-router";
import type { IRouterItem } from "@/types";
import type { IMenuItem, IUseMenu, TCurrentRouterName } from "@/types/composables";
import  { ref } from "vue";

function useMenu(): IUseMenu {
    const publicRoutes: IRouterItem[] = routes.filter(
        (item: IRouterItem): boolean => !!item.public
    );
    const menuItems: IMenuItem[] = [];
    const router: Router = useRouter();
    const currentRouteName: TCurrentRouterName = ref(null);
    const currentRoutePath: string = location.pathname || router.currentRoute.value.path;

    if (!currentRouteName.value) {
        for (const route of routes) {
            if (route.path === currentRoutePath) {
                currentRouteName.value = route.name;
                break;
            }
        }
    }

    for (const route of publicRoutes) {
        menuItems.push({
            label: route.header as string,
            route: route.path,
            icon: route.icon,
            name: route.name
        });
    }

    router.afterEach((to) => {
        currentRouteName.value = to.name as string;
    });

    return {
        menuItems,
        currentRouteName
    };
}

export { useMenu };
