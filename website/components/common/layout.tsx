import { Footer } from "./footer"
import { Header } from "./header"
// import { Navbar } from "./navbar"

export const Layout = ({ children }: { children }) => {
    return <div className="flex flex-col h-screen">
        <Header />
        <div className="main h-full">
            {children}
        </div>
        <Footer />
    </div>
}
