import { Routes } from '@angular/router';
// import { IncidentListComponent } from './components/incident-list/incident-list.component';
// import { IncidentCreateComponent } from './components/incident-create/incident-create.component';
import { LoginComponent } from './components/login/login.component';
import { SubmitReportComponent } from './submit-report/submit-report.component';
import { IncidentDetailComponent } from './incident-detail/incident-detail.component';
import { authGuard } from './guards/auth.guard';

export const routes: Routes = [
  { path: 'login', component: LoginComponent },
  { path: '', redirectTo: 'submit-report', pathMatch: 'full' },
  { path: 'submit-report', component: SubmitReportComponent, canActivate: [authGuard] },
  { path: 'incidents/:id', component: IncidentDetailComponent, canActivate: [authGuard] },
  // { path: 'incidents', component: IncidentListComponent, canActivate: [authGuard] },
  // { path: 'incidents/new', component: IncidentCreateComponent, canActivate: [authGuard] },
];