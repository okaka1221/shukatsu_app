import * as URL from '../constants/urls';
import * as ENTRY_SHEET_ACTIONS from '../actions/entrySheet';

export function postEntrySheet(keywords, text, label) {
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
    dispatch(ENTRY_SHEET_ACTIONS.postEntrySheetPending());
    
    fetch(URL.ENTRY_SHEET, requestOptions)
      .then (res => {
        if (!res.ok) throw res
        return res.json()
      })
      .then(data => {
        dispatch(ENTRY_SHEET_ACTIONS.postEntrySheetSuccess(data))
      })
      .catch(error => {
        dispatch(ENTRY_SHEET_ACTIONS.postEntrySheetFailure(error))
        Error(error.statusText)
      })
  }
}
