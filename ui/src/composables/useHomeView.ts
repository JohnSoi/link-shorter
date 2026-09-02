import { ref, computed } from "vue";
import { zodResolver } from "@primevue/forms/resolvers/zod";
import { z } from "zod";

import type {
    IUseHomeView,
    TFormProcess,
    TFormSubmit,
    THomeFormValues,
    THomeResolver,
    TShortPlaceholder,
    TShortString
} from "@/types/composables";
import type { TFormArgument } from "@/types";
import { LinkShorterService } from "@/services";

function useHomeView(): IUseHomeView {
    const service: LinkShorterService = new LinkShorterService();

    const initialValues: THomeFormValues = ref({
        link: ""
    });

    const resolver: THomeResolver = ref(
        zodResolver(
            z.object({
                link: z.url({ message: "Неподходящий формат ссылки!" })
            })
        )
    );

    const shortLink: TShortString = ref("");

    const shortLinkPlaceholder: TShortPlaceholder = computed((): string => {
        if (shortLink.value) {
            return "Ваша короткая ссылка: ";
        }

        return "Здесь появится Ваша короткая ссылка!";
    });

    const formSubmit: TFormSubmit = async (form: TFormArgument): Promise<void> => {
        if (!form.valid) {
            return;
        }

        const result = await service.shortLink(form.link.value as string);

        if (result.success) {
            shortLink.value = result.short_link as string;
        }
    };

    const formProcess: TFormProcess = ref(false);

    return {
        initialValues,
        resolver,
        shortLink,
        shortLinkPlaceholder,
        formSubmit,
        formProcess
    };
}

export { useHomeView };
