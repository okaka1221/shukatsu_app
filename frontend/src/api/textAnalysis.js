import * as URL from '../constants/urls';
import * as TEXT_ANALYSIS_ACTIONS from '../actions/textAnalysis';

export function getTextAnalysis(keywords, text, label) {
  const requestOptions = {
    method: 'POST',
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      keywords: keywords,
      text: text,
      label: label === "unk" ? null : label, 
    })
  }

  return dispatch => {
    dispatch(TEXT_ANALYSIS_ACTIONS.getTextAnalysisPending());
    
    fetch(URL.TEXT_ANALYSIS, requestOptions)
      .then (res => {
        if (!res.ok) throw res
        return res.json()
      })
      .then(data => {
        dispatch(TEXT_ANALYSIS_ACTIONS.getTextAnalysisSuccess(data))
      })
      .catch(error => {
        dispatch(TEXT_ANALYSIS_ACTIONS.getTextAnalysisFailure(error))
        Error(error.statusText)
      })
  }
}
