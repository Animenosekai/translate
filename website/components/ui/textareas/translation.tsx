import TextareaAutosize, { TextareaAutosizeProps } from 'react-textarea-autosize';

import { useLanguage } from 'contexts/language';

export const TranslationTextArea = (props: TextareaAutosizeProps) => {
    const { strings } = useLanguage();
    return (
        <TextareaAutosize
            maxRows={10}
            style={{ resize: "none" }}
            className="p-2 mt-10 mb-5 mx-auto w-full rounded border-opacity-50 shadow outline-none focus:shadow-lg transition"
            placeholder={strings.placeholders.translationTextArea}
            minRows={1}
            {...props}
        />
    );
}