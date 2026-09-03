import type { Component } from "vue";

import type { ZodObject } from "zod";
import type { $strip, $ZodType } from "zod/v4/core";
import type { FormFieldState, FormResolverOptions } from "@primevue/forms";

interface IRouterItem {
    path: string;
    name: string;
    component: Component | Promise<Component>;
    header?: string;
    icon?: Component;
    public?: boolean;
}

type ResolverResult<T> = {
    values: T;
    errors: Record<string, string>;
};

type TZodReadonly = Readonly<{
    [key: string]: $ZodType;
}>;

type TFormResolver<T extends TZodReadonly> = (
    options: FormResolverOptions<Record<string, unknown>>
) => Promise<ResolverResult<ZodObject<T, $strip>>>;

type TFormArgument = { valid: boolean } & { [key: string]: FormFieldState };

export type { IRouterItem, TFormResolver, TFormArgument };
