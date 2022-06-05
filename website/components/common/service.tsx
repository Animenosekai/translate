import { Service } from "lib/services"

export const ServiceElement = ({ service }: { service: Service }) => {
    return <div onClick={ev => ev.stopPropagation()}>
        {
            service
                ? <a href={service.link} color="primary" rel="noreferrer" target="_blank" >
                    {service.name}
                </a>
                : <span>Source</span>
        }
    </div>
}