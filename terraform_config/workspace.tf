terraform {
	cloud {
		organization = "scraper-api"

		workspaces {
			name = "scraper-api"
		}
	}
}