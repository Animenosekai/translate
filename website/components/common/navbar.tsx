import Link from "next/link";
import cn from "classnames"
import { useLanguage } from "contexts/language";

export interface NavbarProps {
    className?: string
}

const NavbarLink = ({ href, name }: { href: string, name: string }) => {
    return <li className="mx-4 opacity-60 hover:opacity-100 transition">
        <Link passHref={true} href={href}>
            <a>{name}</a>
        </Link>
    </li>
}

export const Navbar = ({className, props}: any) => {
    const { strings } = useLanguage();
    return <ul className={cn("flex flex-row absolute right-10", className)} {...props}>
        <NavbarLink href="/translate" name={strings.pages.translate} />
        <NavbarLink href="/documentation" name={strings.pages.documentation} />
        <NavbarLink href="/stats" name={strings.pages.stats} />
    </ul>
}