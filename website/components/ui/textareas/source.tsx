import TextareaAutosize, { TextareaAutosizeProps } from 'react-textarea-autosize';

import { useLanguage } from 'contexts/language';

export const SourceTextArea = (props: TextareaAutosizeProps) => {
    const { strings } = useLanguage();
    return (
        <TextareaAutosize
            style={{ resize: "none" }}
            className="mt-3 mb-5 w-full outline-none"
            placeholder={strings.placeholders.translationTextArea}
            minRows={1}
            {...props}
        />
    );
}