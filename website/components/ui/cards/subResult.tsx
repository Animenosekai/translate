import { Card } from "@nextui-org/react"
import ContentLoader from "react-content-loader";
import { Service } from "lib/services"
import { ServiceElement } from "components/common/service"
import { TranslateRequest } from "types/translate"

export const SubResultLoader = (props) => {
    return <div className="w-1/3 mb-2 p-1 mx-1 min-w-[300px]">
        <Card clickable shadow={false}>
            <ContentLoader
                speed={2}
                height={70}
                viewBox="0 0 320 70"
                backgroundColor="#f3f3f3"
                foregroundColor="#ecebeb"
                {...props}
            >
                <rect x="0" y="0" rx="3" ry="3" width={180 + (Math.random() * 100)} height="20" />
                <rect x="0" y="50" rx="3" ry="3" width={80 + (Math.random() * 50)} height="20" />
            </ContentLoader>
        </Card>
    </div>
}

export const SubResult = ({ result, ...props }: { result: TranslateRequest }) => {
    const service = new Service(result.data.service)
    return <div className="w-1/4 p-1 mx-1 min-w-[300px]">
        <Card clickable={result.success} shadow={false} className={result.success ? "opacity-100" : "opacity-50"}>
            <span>
                {result.success ? result.data.result : "Failed"}
            </span>
            <Card.Footer className="flex-start">
                <ServiceElement service={service} />
            </Card.Footer>
        </Card>
    </div>
}