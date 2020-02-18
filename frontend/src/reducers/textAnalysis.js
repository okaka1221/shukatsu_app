import * as ActionTypes from '../constants/actions';

const initialState = {
  isPending: false,
  encodedWordcloud: null,
  keywordSimScore: null,
  jikoPRScore: null,
  error: null,
}

export default function textAnalysis(state=initialState, action) {
  switch (action.type) {
    case ActionTypes.GET_TEXT_ANALYSIS_PENDING:
      return {
        ...initialState,
        isPending: true,
      }

    case ActionTypes.GET_TEXT_ANALYSIS_SUCCESS:
      return {
        ...state,
        isPending: false,
        encodedWordcloud: action.encodedWordcloud,
        keywordSimScore: action.keywordSimScore,
        jikoPRScore: action.jikoPRScore,
      }

    case ActionTypes.GET_TEXT_ANALYSIS_FAILURE:
      return {
        ...state,
        isPending: false,
        error: action.error,
      }

    default:
      return state;
  }
}
