import React from 'react';
import Link from '@material-ui/core/Link';
import { makeStyles } from '@material-ui/core/styles';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Title from './Title';

// Generate Order Data
function createData(id, date, name, location, medicalNeeds, followUp) {
  return { id, date, name, location, medicalNeeds, followUp };
}

const rows = [
  createData(0, '16 Mar, 2019', 'David McCartney', 'Room 201', 'Knee Surgery', 'Y'),
  createData(1, '16 Mar, 2019', 'John Smith', 'Room 431', 'Arm fracture', 'Y'),
  createData(2, '16 Mar, 2019', 'Tom Agas', 'Office', '...', 'N'),
  createData(3, '16 Mar, 2019', 'Leo Jackson', '...', '...', "N"),
  createData(4, '.. ..., ....', '...', '...', '...', 'Y'),
];

function preventDefault(event) {
  event.preventDefault();
}

const useStyles = makeStyles((theme) => ({
  seeMore: {
    marginTop: theme.spacing(3),
  },
}));

export default function Appointments() {
  const classes = useStyles();
  return (
    <React.Fragment>
      <Title>Upcoming Appointments</Title>
      <Table size="small">
        <TableHead>
          <TableRow>
            <TableCell>Date</TableCell>
            <TableCell>Name</TableCell>
            <TableCell>Location</TableCell>
            <TableCell>Medical Needs</TableCell>
            <TableCell align="right">Follow Up(Y/N)</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {rows.map((row) => (
            <TableRow key={row.id}>
              <TableCell>{row.date}</TableCell>
              <TableCell>{row.name}</TableCell>
              <TableCell>{row.location}</TableCell>
              <TableCell>{row.medicalNeeds}</TableCell>
              <TableCell align="right">{row.followUp}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
      <div className={classes.seeMore}>
        <Link color="primary" href="#" onClick={preventDefault}>
          See more appointments
        </Link>
      </div>
    </React.Fragment>
  );
}