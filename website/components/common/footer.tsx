import Link from "next/link"

export const Footer = () => {
    return <footer className="fixed bottom-0 flex justify-between w-full m-auto py-5 px-10">
        <div className="opacity-40 hover:opacity-70 transition">
            <Link href="https://github.com/Animenosekai/translate">GitHub</Link>
        </div>
    </footer>
}
