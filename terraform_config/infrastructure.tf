
resource "aws_vpc" "scraper-vpc" {
	cidr_block = "172.31.0.0/20"
}