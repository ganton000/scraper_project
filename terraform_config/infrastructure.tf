
resource "aws_vpc" "scraper-vpc" {
	cidr_block = "172.31.0.0/16"
	enable_dns_hostnames = false # default
	enable_dns_support = true # default

	tags = {
		Name = "project-scraper"
	}
}

resource "aws_subnet" "scraper-private-subnet" {
	vpc_id = aws_vpc.scraper-vpc.id
	cidr_block = "172.31.1.0/24"
	map_public_ip_on_launch = false # default


	tags = {
		Name = "project-scraper"
	}
}

resource "aws_subnet" "scraper-public-subnet" {
	vpc_id = aws_vpc.scraper-vpc.id
	cidr_block = "172.31.2.0/24"
	map_public_ip_on_launch = false # default


	tags = {
		Name = "project-scraper"
	}
}

resource "aws_internet_gateway" "scraper-igw" {
	vpc_id = aws_vpc.scraper-vpc.id


	tags = {
		Name = "project-scraper"
	}
}

resource "aws_route_table" "scraper-route-table" {
	vpc_id = aws_vpc.scraper-vpc.id

	route {
		cidr_block = "172.31.1.0/24"
		gateway_id = aws_internet_gateway.scraper-igw.id
	}

	tags = {
		Name = "scraper-project"
	}
}

resource "aws_security_group" "scraper-allow-http-private" {
	name = "allow_http"
	description = "Allow HTTP traffic"
	vpc_id = aws_vpc.scraper-vpc.id

	ingress {
		description = "HTTP from private subnet"
		from_port = 80
		to_port = 80
		protocol = "tcp"
		cidr_blocks = [ aws_subnet.scraper-private-subnet.cidr_block ]
	}

	egress {
		description = "HTTP to private and public subnet"
		from_port = 0
		to_port = 0
		protocol = "tcp" # allow all
		cidr_blocks = [
			aws_subnet.scraper-private-subnet.cidr_block,
			aws_subnet.scraper-public-subnet.cidr_block
		]
	}

	tags = {
		Name = "scraper-project"
	}
}

resource "aws_security_group" "scraper-allow-http-public" {
	name = "allow_http"
	description = "Allow HTTP traffic"
	vpc_id = aws_vpc.scraper-vpc.id

	ingress {
		description = "HTTP from vpc"
		from_port = 80
		to_port = 80
		protocol = "tcp"
		cidr_blocks = [ aws_vpc.scraper-vpc.cidr_blocks ]
	}

	egress {
		description = "HTTP to all"
		from_port = 0
		to_port = 0
		protocol = "-1" # allow all
		cidr_blocks = [ "0.0.0.0/0" ] # optional, else blocked
		ipv6_cidr_blocks = [ "::/0" ] # optional, else blocked
	} ## does this egress make sense? Do we allow all traffic in this subnet to leave or should that be job of IGW?

	tags = {
		Name = "scraper-project"
	}
}