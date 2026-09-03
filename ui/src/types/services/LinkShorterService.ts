interface IShorterBLResponse {
    success: boolean;
    short_link: string | null;
    errors: string[] | null;
}

export type { IShorterBLResponse };
