import Link from "next/link";
// import cn from "classnames"
import { useLanguage } from "contexts/language";

export interface NavbarProps {
    className?: string
}

const NavbarLink = ({ href, name }: { href: string, name: string }) => {
    return <li className="mx-4 opacity-60 hover:opacity-100 transition">
        <Link href={href}>
            {name}
        </Link>
    </li>
}

export const Navbar = (props: any) => {
    const { strings } = useLanguage();
    return <ul className="flex flex-row absolute right-10" {...props}>
        <NavbarLink href="/translate" name="Translate" />
        <NavbarLink href="/documentation" name="Documentation" />
        <NavbarLink href="/stats" name="Stats" />
    </ul>
}