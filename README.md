# SA-ID-Verification

Verify South African ID numbers and extract age, gender and citizen status.

## installation
```javascript
npm install sa-id-verification
```

# Usage

### import package and create an ID instance
```javascript
import SouthAfricanID from 'sa-id-verification';
// id_number must be a 13 digit string
var south_african_id = new SouthAfricanID(id_number);
```


## Verify Id
```javascript
// check if the id number is valid using the luhn algorithm https://en.wikipedia.org/wiki/Luhn_algorithm
// returns boolean value 
var is_id_valid = south_african_id.validId();
```

## Extract gender
```javascript
//  extract gender from id number, Male or Female
var gender = south_african_id.getGender();
```

## Extract citizen status
```javascript
//  extract citizen status from id number, SA citizen or Permanent resident
var citezen_status = south_african_id.getCitizenStatus();
```

## Extract age
```javascript
//  extract age from id number
var age = south_african_id.getAge();
```
