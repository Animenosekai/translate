import Link from "next/link"
import { Service } from "lib/services"

export const ServiceElement = ({ service }: { service: Service }) => {
    return <div onClick={ev => ev.stopPropagation()}>
        {
            service
                ? <Link href={service.link} color="primary" target="_blank" >
                    {service.name}
                </Link>
                : <span>Source</span>
        }
    </div>
}