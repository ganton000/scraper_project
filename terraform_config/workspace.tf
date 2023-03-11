terraform {
	cloud {
		organization = "anton-terransible"

		workspaces {
			name = "scraper-api"
		}
	}
}