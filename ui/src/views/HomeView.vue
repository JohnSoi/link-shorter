<script setup lang="ts">
import { InputText, Button, Message, Card } from "primevue";
import { Form } from "@primevue/forms";
import type { IUseHomeView } from "@/types/composables";
import { useHomeView } from "@/composables/useHomeView.ts";

const {
    initialValues,
    resolver,
    shortLinkPlaceholder,
    shortLink,
    formSubmit,
    formProcess
}: IUseHomeView = useHomeView();
</script>

<template>
    <div class="HomeView__wrapper p-8 flex flex-col items-center justify-center w-full h-full">
        <div class="HomeView__block">
            <div class="flex justify-center">
                <Card class="max-w-sm w-full flex justify-center">
                    <template #content>
                        <div class="flex justify-center w-full">
                            <Form
                                v-slot="$form"
                                :resolver="resolver"
                                :initial-values="initialValues"
                                class="flex flex-col gap-4 w-full sm:w-56"
                            >
                                <div class="flex flex-col gap-1">
                                    <InputText
                                        name="link"
                                        type="text"
                                        placeholder="Исходная ссылка"
                                        fluid
                                    />
                                    <Message
                                        v-if="$form.link?.invalid"
                                        severity="error"
                                        size="small"
                                        variant="simple"
                                    >
                                        {{ $form.link.error?.message }}
                                    </Message>
                                </div>
                                <Button
                                    type="submit"
                                    severity="secondary"
                                    :disabled="formProcess"
                                    @click="formSubmit($form)"
                                >
                                    Укоротить
                                </Button>
                            </Form>
                        </div>
                    </template>
                    <template #footer>
                        <div class="HomeView__block-footer">
                            <span class="text-sm text-surface-500 dark:text-surface-400">
                                {{ shortLinkPlaceholder }}
                            </span>
                            <a v-if="shortLink" :href="shortLink" target="_blank">Перейти</a>
                        </div>
                    </template>
                </Card>
            </div>
        </div>
    </div>
</template>
