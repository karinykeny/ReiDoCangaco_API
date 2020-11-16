import { Component } from '@angular/core';
import { AuthenticationService } from './services/authentication.service';
import { Router } from '@angular/router';
import { PrimeNGConfig } from 'primeng/api';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Rei do Cangaço';

  constructor(
    private router: Router,
    private authenticationService: AuthenticationService,
    private primengConfig: PrimeNGConfig
  ) {
    if (!this.authenticationService.currentUserValue) {
      this.router.navigate(['/login']);
    }
  }
  ngOnInit() {
    this.primengConfig.ripple = true;
  }
}
