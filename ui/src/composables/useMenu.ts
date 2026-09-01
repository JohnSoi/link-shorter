import { routes } from "@/router";
import { type Router, useRouter } from "vue-router";

function useMenu() {
    const publicRoutes = routes.filter((item) => item.public);
    const menuItems = [];
    const router: Router = useRouter();
    const currentRouteName = router.currentRoute.value.name;
    const currentRoutePath = router.currentRoute.value.path;

    for (const route of publicRoutes) {
        menuItems.push({
            label: route.header,
            route: route.path,
            active: currentRouteName === route.name || currentRoutePath === route.path,
            icon: route.icon,
        });
    }

    return {
        menuItems
    };
}

export { useMenu };
