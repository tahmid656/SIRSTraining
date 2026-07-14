import { Routes } from '@angular/router';
// import { IncidentListComponent } from './components/incident-list/incident-list.component';
// import { IncidentDetailComponent } from './components/incident-detail/incident-detail.component';
// import { IncidentCreateComponent } from './components/incident-create/incident-create.component';
import { LoginComponent } from './components/login/login.component';
import { authGuard } from './guards/auth.guard';

export const routes: Routes = [
  { path: 'login', component: LoginComponent },
  { path: '', redirectTo: 'incidents', pathMatch: 'full' },
  // { path: 'incidents', component: IncidentListComponent, canActivate: [authGuard] },
  // { path: 'incidents/new', component: IncidentCreateComponent, canActivate: [authGuard] },
  // { path: 'incidents/:id', component: IncidentDetailComponent, canActivate: [authGuard] }
];