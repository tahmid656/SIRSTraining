import { Routes } from '@angular/router';
// import { IncidentDetailComponent } from './components/incident-detail/incident-detail.component';
// import { IncidentCreateComponent } from './components/incident-create/incident-create.component';
import { LoginComponent } from './components/login/login.component';
import { MyIncidentsComponent } from './my-incidents/my-incidents.component';
import { authGuard } from './guards/auth.guard';

export const routes: Routes = [
  { path: 'login', component: LoginComponent },
  { path: 'incidents', component: MyIncidentsComponent /* TODO: add canActivate: [authGuard] once login works */ },
  { path: '', redirectTo: 'incidents', pathMatch: 'full' },
  // { path: 'incidents/new', component: IncidentCreateComponent, canActivate: [authGuard] },
  // { path: 'incidents/:id', component: IncidentDetailComponent, canActivate: [authGuard] }
];
