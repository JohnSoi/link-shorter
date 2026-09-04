import type { IShorterBLResponse } from "@/types/services";

class LinkShorterService {
    protected readonly _baseUrl: string = "http://127.0.0.1:8000/";
    protected readonly _entity: string = "link";
    protected readonly _serviceUrl: string;

    constructor() {
        this._serviceUrl = `${this._baseUrl}${this._entity}/`;
    }

    async shortLink(link: string): Promise<IShorterBLResponse> {
        return await fetch(this._serviceUrl + "short", {
            method: "POST",
            body: JSON.stringify({ url: link }),
            headers: {
                accept: "application/json",
                "Content-Type": "application/json"
            }
        })
            .then(
                async (response: Response): Promise<IShorterBLResponse> =>
                    await response.text().then((text: string): IShorterBLResponse => {
                        return {
                            success: true,
                            short_link: text.replaceAll('"', ""),
                            errors: null
                        };
                    })
            )
            .catch((error: Error): IShorterBLResponse => {
                console.log(error);
                return {
                    success: false,
                    short_link: null,
                    errors: ["An error occurred while shortening the link."]
                };
            });
    }

    async getLinkByToken(token: string): Promise<string | null> {
        return await fetch(this._serviceUrl + token)
            .then(async (response: Response) => {
                if (response.status !== 200) {
                    return null;
                }
                const text = await response.text();
                return text.replaceAll('"', "");
            })
            .catch((error: Error) => {
                console.log(error);
                return null;
            });
    }
}

export { LinkShorterService };
