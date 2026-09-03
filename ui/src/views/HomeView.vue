<script setup lang="ts">
import { InputText, Button, Message, Card } from "primevue";
import { Form } from "@primevue/forms";
import type { IUseHomeView } from "@/types/composables";
import { useHomeView } from "@/composables/useHomeView";
import { Clipboard } from "@primeicons/vue";

const {
    initialValues,
    resolver,
    shortLinkPlaceholder,
    shortLink,
    formSubmit,
    formProcess,
    copyLink
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
                        <div class="HomeView__block-footer flex justify-center items-center">
                            <span class="text-sm text-surface-500 dark:text-surface-400">
                                {{ shortLinkPlaceholder }}
                            </span>
                            <div v-if="shortLink" class="flex justify-center items-center">
                                <a
                                    :href="shortLink"
                                    target="_blank"
                                    class="ml-2 mr-2 text-blue-300 hover:text-blue-700"
                                    >перейти</a
                                >
                                или
                                <Clipboard
                                    class="ml-2 text-blue-500 hover:text-blue-700 cursor-pointer"
                                    title="Копировать"
                                    @click="copyLink()"
                                />
                            </div>
                        </div>
                    </template>
                </Card>
            </div>
        </div>
    </div>
</template>
