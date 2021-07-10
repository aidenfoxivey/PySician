import React, { useState } from 'react'
import Grid from '@material-ui/core/Grid'
import Typography from '@material-ui/core/Typography'
import TextField from '@material-ui/core/TextField'
import FormControlLabel from '@material-ui/core/FormControlLabel'
import Checkbox from '@material-ui/core/Checkbox'
import styled from 'styled-components'
export default function ProblemDescription () {
  const [details, setDetails] = useState()
  const [firstname, setFirstName] = useState()
  const [lastName, setLastName] = useState()

  return (
    <React.Fragment>
      <Typography variant='h6' gutterBottom>
        Describe your problem
      </Typography>
      <Grid container spacing={3}>
        <Grid item xs={12}>
          <TextField required id='Age' name='Age' label='Age' type='number' />
        </Grid>
        <Grid item xs={12}>
          <TextField
            required
            id='Problem'
            name='Problem'
            label='Problem'
            fullWidth
          />
        </Grid>
        <Grid item xs={12}>
          <TextField
            required
            id='Allergies/Any medical treatment going on '
            name='Allergies/Any medical treatment going on '
            label='Allergies/Any medical treatment going on '
            fullWidth
          />
        </Grid>
        <Grid item xs={12}>
          <TextField
            id='ExtraInformation '
            name='Extra Information '
            label='Extra Information '
            fullWidth
          />
        </Grid>
      </Grid>
    </React.Fragment>
  )
}
