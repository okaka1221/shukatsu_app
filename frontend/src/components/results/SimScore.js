import React from "react";
import { Typography } from "@material-ui/core";

function SimScore({score, encodedWordcloud}) {
  return (
    <div>
      {
        score !== null ?
        <div>
          <Typography variant='h5' style={{ marginTop: 50 }}>キーワードとワードクラウドの相関</Typography>
          <Typography variant='h3' style={{ marginTop: 20 }}>{Math.round(score)} 点</Typography>
        </div>
        : null
      }
      {
        score === null && encodedWordcloud !== null ?
        <div>
          <Typography variant='h5' style={{ marginTop: 50 }}>キーワードとワードクラウドの相関</Typography>
          <Typography color='error'variant='h6' style={{ marginTop: 20 }}>キーワードを正しく入力して下さい</Typography>
        </div>
        : null
    }
    </div>
  )
}

export default SimScore;