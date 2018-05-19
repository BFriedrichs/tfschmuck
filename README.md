# Tanja Friedrichs Schmuck

![CI Build](https://circleci.com/gh/BFriedrichs/tfschmuck.svg?style=shield&circle-token=05cf235d9f2ce76fd7eb540b0c03f557d063fa71)

An update to tanjafriedrichs.de

---

### Development

docker run -t --rm -v $(pwd):/app -p 8000:80 bfriedrichs/tfschmuck

### Deployment

* unlock crypt
* ansible-playbook -i crypt/inventory -i deploy/hosts deploy/site.yml
