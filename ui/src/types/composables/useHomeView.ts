import type { Ref, ComputedRef } from "vue";
import type { ZodURL } from "zod";
import type { TFormArgument, TFormResolver } from "@/types";

interface IHomeForm {
    link: string;
}

type THomeFormValues = Ref<IHomeForm>;
type THomeResolver = Ref<TFormResolver<{ link: ZodURL }>>;
type TShortString = Ref<string>;
type TShortPlaceholder = ComputedRef<string>;
type TFormProcess = Ref<boolean>;
type TFormSubmit = (form: TFormArgument) => Promise<void>;

interface IUseHomeView {
    initialValues: THomeFormValues;
    resolver: THomeResolver;
    shortLink: TShortString;
    shortLinkPlaceholder: TShortPlaceholder;
    formProcess: TFormProcess;
    formSubmit: TFormSubmit;
}

export type {
    THomeFormValues,
    IUseHomeView,
    THomeResolver,
    TShortString,
    TShortPlaceholder,
    TFormProcess,
    TFormSubmit
};
