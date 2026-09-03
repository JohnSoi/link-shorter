import { type Router, useRouter } from "vue-router";
import { LinkShorterService } from "@/services";
import type { Ref } from "vue";
import type { IUseRedirectPage, TRedirectByToken } from "@/types/composables";

function useRedirectPage(): IUseRedirectPage {
    const router: Router = useRouter();
    const $route: Ref = router.currentRoute;

    const redirectByToken: TRedirectByToken = async (): Promise<void> => {
        const routerParams: string[] = $route.value.params?.pathMatch || [];
        const service: LinkShorterService = new LinkShorterService();

        if (!routerParams.length) {
            await router.push("/404");
        }

        const token: string = routerParams[0];

        const link: string | null = await service.getLinkByToken(token);

        if (link) {
            location.href = link;
            return;
        }

        await router.push("/404");
    };

    return { redirectByToken };
}

export { useRedirectPage };
