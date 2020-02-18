import React from "react";
import { Typography } from "@material-ui/core";

function WordCloud({encodedWordcloud}) {
  return (
    <div>
      {
        encodedWordcloud !== null ?
          <div>
            <Typography variant='h5'>ワードクラウド</Typography>
            <img 
              src={"data:image/png;base64," + encodedWordcloud}
              alt="wordcloud"
              width="500" height="500"
              style={{ marginTop: 20 }}
            />
          </div>
        : null
      }
    </div>
  )
}

export default WordCloud;