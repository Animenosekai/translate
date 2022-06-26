import Link from "next/link"
import { useRouter } from "next/router"

export const AnchorLink = ({ node, href, title, children, key, ...props }) => {
    const { asPath } = useRouter();
    const h = String(href)
    let result = ""
    if (h.startsWith("./")) {
        result = `${asPath}/${h.slice(2)}`
        if (result.endsWith(".md")) {
            result = result.slice(0, result.length - 3)
        }
    } else if (h.startsWith("../")) {
        const count = h.match(/\.\.\//g).length
        const path = asPath.split("/")
        result = path.slice(0, path.length - count).join("/") + h.split("/").slice(count).join("/")
        if (result.endsWith(".md")) {
            result = result.slice(0, result.length - 3)
        }
        console.log(h, count, path, result)
    } else { // absolute path
        result = href
    }
    return <Link passHref={true} title={title} href={result}>
        <a>{children}</a>
    </Link>
}