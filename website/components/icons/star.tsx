import { IconStar, TablerIconProps } from "@tabler/icons";

export interface StarIconProps extends TablerIconProps {
    active?: boolean
}

const STAR_COLOR = "#fcd512";

export const StarIcon = ({ active, ...props }: StarIconProps) => (
    <IconStar fill={active ? STAR_COLOR : "transparent"} color={active ? STAR_COLOR : "currentColor"} {...props} />
);