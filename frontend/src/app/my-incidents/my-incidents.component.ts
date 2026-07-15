import { Component, OnInit, signal } from '@angular/core';
import { DatePipe, TitleCasePipe } from '@angular/common';
import { IncidentService, Incident } from '../services/incident.service';

@Component({
  selector: 'app-my-incidents',
  standalone: true,
  imports: [DatePipe, TitleCasePipe],
  templateUrl: './my-incidents.component.html',
  styleUrl: './my-incidents.component.css'
})
export class MyIncidentsComponent implements OnInit {
  /** Rows shown in the table. */
  incidents = signal<Incident[]>([]);
  loading = signal(true);
  error = signal<string | null>(null);

  /** Controls the "no incidents" popup (lets the user dismiss it). */
  emptyPopupDismissed = signal(false);

  constructor(private incidentService: IncidentService) {}

  /** True when loading finished with no error and no incidents. */
  get showEmptyPopup(): boolean {
    return !this.loading() && !this.error() && this.incidents().length === 0
      && !this.emptyPopupDismissed();
  }

  dismissEmptyPopup(): void {
    this.emptyPopupDismissed.set(true);
  }

  ngOnInit(): void {
    this.loadIncidents();
  }

  /** Fetch the current user's incidents and populate the table. */
  loadIncidents(): void {
    this.loading.set(true);
    this.error.set(null);

    this.incidentService.getMyIncidents().subscribe({
      next: (data) => {
        this.incidents.set(data ?? []);
        this.loading.set(false);
      },
      error: (err) => {
        this.error.set(err?.error?.error || 'Failed to load incidents.');
        this.loading.set(false);
      },
    });
  }

  // --- display helpers -----------------------------------------------------

  /** Zero-padded case reference, e.g. 7 -> "SIRS-0007". */
  caseId(id: number): string {
    return 'SIRS-' + String(id).padStart(4, '0');
  }

  /** Coloured severity dot class. */
  severityClass(severity: string): string {
    const s = (severity || '').toLowerCase();
    if (s === 'high' || s === 'critical') return 'sev-high';
    if (s === 'medium') return 'sev-med';
    return 'sev-low';
  }

  /** Status pill class. */
  statusClass(status: string): string {
    const s = (status || '').toLowerCase();
    if (['closed', 'resolved'].includes(s)) return 'pill-closed';
    if (['under_review', 'in_progress', 'assigned', 'review'].includes(s)) return 'pill-review';
    return 'pill-open';
  }
}
