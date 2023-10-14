import { Service } from "lib/services"
import { useLanguage } from "contexts/language"

export const ServiceElement = ({ service }: { service?: Service }) => {
    const { strings } = useLanguage();
    return <div onClick={ev => ev.stopPropagation()}>
        {
            service
                ? <a href={service.link} color="primary" rel="noreferrer" target="_blank" >
                    {service.name}
                </a>
                : <span>{strings.labels.source}</span>
        }
    </div>
}