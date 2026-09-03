type TRedirectByToken = () => Promise<void>;

interface IUseRedirectPage {
    redirectByToken: TRedirectByToken;
}

export type { TRedirectByToken, IUseRedirectPage };
