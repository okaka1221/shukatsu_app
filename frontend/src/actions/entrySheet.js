import * as ActionTypes from '../constants/actions';

export function postEntrySheetPending() {
  return {
    type: ActionTypes.POST_ENTRY_SHEET_PENDING,
  }
}

export function postEntrySheetSuccess(data) {
  return {
    type: ActionTypes.POST_ENTRY_SHEET_SUCCESS,
    encodedWordcloud: data.encoded_wordcloud,
    keywordSimScore: data.keyword_sim_score,
    jikoPRScore: data.jikoPR_score,
  }
}

export function postEntrySheetFailure(error) {
  return {
    type: ActionTypes.POST_ENTRY_SHEET_FAILURE,
    error: error.status,
  }
}
