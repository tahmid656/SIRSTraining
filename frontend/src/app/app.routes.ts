import { Routes } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { SubmitReportComponent } from './submit-report/submit-report.component';
import { MyIncidentsComponent } from './my-incidents/my-incidents.component';
import { IncidentDetailComponent } from './incident-detail/incident-detail.component';

export const routes: Routes = [
  { path: '', redirectTo: 'login', pathMatch: 'full' },
  { path: 'login', component: LoginComponent },
  { path: 'submit', component: SubmitReportComponent },
  { path: 'incidents', component: MyIncidentsComponent },
  { path: 'incidents/:id', component: IncidentDetailComponent },
];