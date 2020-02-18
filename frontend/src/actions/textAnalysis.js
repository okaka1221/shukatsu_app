import * as ActionTypes from '../constants/actions';

export function getTextAnalysisPending() {
  return {
    type: ActionTypes.GET_TEXT_ANALYSIS_PENDING,
  }
}

export function getTextAnalysisSuccess(data) {
  return {
    type: ActionTypes.GET_TEXT_ANALYSIS_SUCCESS,
    encodedWordcloud: data.encoded_wordcloud,
    keywordSimScore: data.keyword_sim_score,
    jikoPRScore: data.jikoPR_score,
  }
}

export function getTextAnalysisFailure(error) {
  return {
    type: ActionTypes.GET_TEXT_ANALYSIS_FAILURE,
    error: error.status,
  }
}
