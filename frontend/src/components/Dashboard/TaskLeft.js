import React from 'react';
import Link from '@material-ui/core/Link';
import { makeStyles } from '@material-ui/core/styles';
import Typography from '@material-ui/core/Typography';
import Title from './Title';
import ThumbUpIcon from '@material-ui/icons/ThumbUp';
import SentimentVerySatisfiedIcon from '@material-ui/icons/SentimentVerySatisfied';

function preventDefault(event) {
  event.preventDefault();
}

const useStyles = makeStyles({
  depositContext: {
    flex: 1,
  },
});

export default function TaskLeft() {
  const classes = useStyles();
  return (
    <React.Fragment>
      <Title>Tasks Left For The Day</Title>
      <Typography component="p" variant="h4">
        4
      </Typography>
      <Typography color="textSecondary" className={classes.depositContext}>
        You Got This! 
        <br></br>
        <br></br>
        <SentimentVerySatisfiedIcon /><ThumbUpIcon />

      </Typography>
      <div>
        <Link color="primary" href="#" onClick={preventDefault}>
          
        </Link>
      </div>
    </React.Fragment>
  );
}