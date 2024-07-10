import Link from "next/link"
import { useRouter } from "next/router"

export const AnchorLink = ({ node, href, title, children, key, ...props }) => {
    const { asPath } = useRouter();
    const currentPath = asPath.includes("#") ? asPath.slice(0, asPath.indexOf("#")) : asPath
    // console.log(asPath, currentPath)
    const h = String(href)
    let result = ""
    if (h.startsWith("./")) {
        result = `${currentPath}/${h.slice(2)}`
        let basePath = result.split("#")[0]
        if (basePath.endsWith(".md")) {
            basePath = basePath.slice(0, basePath.length - 3)
        }
        result = [basePath, ...result.split("#").slice(1)].join("#")
    } else if (h.startsWith("../")) {
        const match = h.match(/\.\.\//g);
        const count = match ? match.length : 0;
        const path = currentPath.split("/")
        result = path.slice(0, path.length - count).join("/") + h.split("/").slice(count).join("/")
        let basePath = result.split("#")[0]
        if (basePath.endsWith(".md")) {
            basePath = basePath.slice(0, basePath.length - 3)
        }
        result = [basePath, ...result.split("#").slice(1)].join("#")
        // console.log(h, count, path, result)
    } else { // absolute path
        result = href
    }
    return <Link passHref={true} title={title} href={result}>
        <a className="opacity-100 hover:opacity-50 transition">{children}</a>
    </Link>
}