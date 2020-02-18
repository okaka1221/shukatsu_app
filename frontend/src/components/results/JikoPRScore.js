import React from "react";
import { Typography } from "@material-ui/core";

function JikoPRScore({jikoPRScore}) {
  return (
    <div>
      {
        jikoPRScore !== null ?
          <div>
            <Typography variant='h5' >あなたの自己PRの点数は100点中</Typography>
            <Typography variant='h3' style={{ marginTop: 20 }}>{Math.round(jikoPRScore)} 点</Typography>
          </div>
        : null
        }
    </div>
  )
}

export default JikoPRScore;
