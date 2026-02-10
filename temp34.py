def main():
    emails = ["alice@gmail.com", "bob@yahoo.com", "carol@gmail.com","heet@microsoft.com"]
    allowed_domains=["@gmail.com","@yahoo.com"]
    def get_valid_email(email):
        for domain in allowed_domains:
            if email.endswith(domain):
                return email
    allowed=list(filter(get_valid_email,emails))
    allowed_without_domain=list(map(without_domain,allowed))
    print(allowed_without_domain)

def without_domain(email):
    return email.split("@")[0]    
if __name__ == "__main__":
    main()