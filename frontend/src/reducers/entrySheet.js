import * as ActionTypes from '../constants/actions';

const initialState = {
  isPending: false,
  encodedWordcloud: null,
  keywordSimScore: null,
  jikoPRScore: null,
  error: null,
}

export default function entrySheet(state=initialState, action) {
  switch (action.type) {
    case ActionTypes.POST_ENTRY_SHEET_PENDING:
      return {
        ...initialState,
        isPending: true,
        error: null,
      }

    case ActionTypes.POST_ENTRY_SHEET_SUCCESS:
      return {
        ...state,
        isPending: false,
        encodedWordcloud: action.encodedWordcloud,
        keywordSimScore: action.keywordSimScore,
        jikoPRScore: action.jikoPRScore,
        error: null,
      }

    case ActionTypes.POST_ENTRY_SHEET_FAILURE:
      return {
        ...state,
        isPending: false,
        error: action.error,
      }

    default:
      return state;
  }
}
