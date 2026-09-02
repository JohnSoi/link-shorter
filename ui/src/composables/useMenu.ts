import { routes } from "@/router";
import { type Router, type RouteRecordNameGeneric, useRouter } from "vue-router";
import type { IRouterItem } from "@/types";
import type { IMenuItem, IUseMenu } from "@/types/composables";

function useMenu(): IUseMenu {
    const publicRoutes: IRouterItem[] = routes.filter(
        (item: IRouterItem): boolean => !!item.public
    );
    const menuItems: IMenuItem[] = [];
    const router: Router = useRouter();
    const currentRouteName: RouteRecordNameGeneric = router.currentRoute.value.name;
    const currentRoutePath: string = router.currentRoute.value.path;

    for (const route of publicRoutes) {
        menuItems.push({
            label: route.header,
            route: route.path,
            active: currentRouteName === route.name || currentRoutePath === route.path,
            icon: route.icon
        });
    }

    return {
        menuItems
    };
}

export { useMenu };
