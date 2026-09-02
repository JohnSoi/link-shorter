class LinkShorterService {
    constructor() {}

    async shortLink(
        link: string
    ): Promise<{ success: boolean; short_link: string | null; errors: string[] | null }> {
        return new Promise((resolve) => {
            return resolve({
                success: true,
                short_link: link,
                errors: null
            });
        });
    }
}

export { LinkShorterService };
