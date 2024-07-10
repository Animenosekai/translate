import Head from "next/head";

export interface SEOProps {
    title?: string;
    description?: string;
}

const APP_NAME = "translatepy"

export const SEO = ({ title, description }: SEOProps) => (
    <Head>
        <title>{title ? `${APP_NAME} | ${title}` : APP_NAME}</title>
        <meta name="description" content={description} />
        <meta property="og:type" content="website" />
        <meta property="og:title" content={title || APP_NAME} />
        <meta property="og:description" content={description} />
        <meta property="og:site_name" content={APP_NAME} />
        <meta property="twitter:card" content="summary" />
        <meta property="twitter:title" content={title || APP_NAME} />
        <meta property="twitter:description" content={description} />
        <meta name="msapplication-TileColor" content="#00aba9" />
        <meta name="apple-mobile-web-app-title" content={APP_NAME} />
        <meta name="application-name" content={APP_NAME} />
        <link
            rel="apple-touch-icon"
            sizes="180x180"
            href="/apple-touch-icon.png"
        />
        <link
            rel="icon"
            type="image/png"
            sizes="32x32"
            href="/favicon-32x32.png"
        />
        <link
            rel="icon"
            type="image/png"
            sizes="16x16"
            href="/favicon-16x16.png"
        />
        <link rel="icon" type="image/x-icon" href="/favicon.ico" />
        <link rel="manifest" href="/manifest.json" />
        <link
            rel="mask-icon"
            href="/safari-pinned-tab.svg"
            color="#5bbad5"
        />
        <meta
            name="theme-color"
            content="#080808"
            media="(prefers-color-scheme:dark)"
        />
        <meta
            name="theme-color"
            content="#fff"
            media="(prefers-color-scheme:light)"
        />
        <meta
            name="background-color"
            content="#080808"
            media="(prefers-color-scheme:dark)"
        />
        <meta
            name="background-color"
            content="#fff"
            media="(prefers-color-scheme:light)"
        />
    </Head>
);