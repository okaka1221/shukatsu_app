import React from "react";
import WordCloud from './results/WordCloud';
import SimScore from './results/SimScore';
import JikoPRScore from './results/JikoPRScore';
import { Grid, CircularProgress } from "@material-ui/core";

class Result extends React.Component {
  render() {
    const { isPending, encodedWordcloud, keywordSimScore, jikoPRScore } = this.props;
    
    return (
      <div>
        { 
          isPending ? 
          <Grid container spacing={3} justify='center' style={{display: 'flex'}}>
            <CircularProgress size={100}/>
          </Grid>
          : 
          <Grid container spacing={3} >
            <Grid item xs={6}>
              <JikoPRScore jikoPRScore={jikoPRScore}/>
              <SimScore
                score={keywordSimScore}
                encodedWordcloud={encodedWordcloud}
              />
            </Grid>
            <Grid item xs={6}>
              <WordCloud encodedWordcloud={encodedWordcloud} />
            </Grid>
          </Grid>
        }
      </div>
    )
  }
}

export default Result;