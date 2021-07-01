//  Initialize constants variables to determine users' gender
let CONST_FEMALE_LOWER_BOUND = 0o000;
let CONST_FEMALE_UPPER_BOUND = 4999;
let CONST_MALE_LOWER_BOUND = 5000;
let CONST_MALE_UPPER_BOUND = 9999;

//  initializeconstants to classify citizenship
let CONST_SA_CITIZEN = 0;
let CONST_PERM_RESIDENT = 1;

class SouthAfricanID{
    // This is a blueprint for the South African identity verification.
    constructor(str_id_number){
        this.input_id = str_id_number;
        //  extract years, month and date from the valid id
        this.month = this.input_id.slice(this.input_id.length - 11,this.input_id.length - 9);
        this.day = this.input_id.slice(this.input_id.length - 9,this.input_id.length - 7);
        // get birth year
        // warning
        var first_digits = this.input_id.slice(0,this.input_id.length - 11);
        if(first_digits[0] == 0){
            this.year = `20${first_digits}`;
        }else{
            this.year = `19${first_digits}`;
        }

        //get age
        this.age = new Date().getFullYear() - Number(this.year); 

    }

    // get gender
    getGender(){
        //  extracts the SSSS digits from the id to determine if the user is female or male
        var SSSS = this.input_id.slice(this.input_id.length - 7,this.input_id.length - 3);
        if (SSSS >= CONST_FEMALE_LOWER_BOUND && SSSS <= CONST_FEMALE_UPPER_BOUND){
            return "Female"
        }else if( SSSS >= CONST_MALE_LOWER_BOUND && CONST_MALE_UPPER_BOUND){
            return "Male";
        }
    }

    getCitizenStatus(){
        var C = this.input_id[this.input_id.length-3]
        if  (C == CONST_SA_CITIZEN){
            return "SA citizen";
        }
        else if( C == CONST_PERM_RESIDENT){
            return "Permanent resident";
        }
    }

    validId(){
        try{
            // get the length of the id
            var nDigits = Number(this.input_id.length);
            // 
            if (nDigits != 13){
                throw "Not a valid 13 digit id";
            }else{
                var sum = 0;
                var parity = nDigits % 2;
                //  iterate through the id number to compute the sum   
                for(let index = 0; index < nDigits-1; index++){
                    //  get all digits along with their indexes except the last digit
                    var digit = Number(this.input_id[index]);
                    //  double every second second digit
                    if(index % 2 == parity){
                        digit = digit * 2;
                    }
                    //  substract a 9 to all values greater than 10
                    if( digit > 9){
                        digit = digit - 9;
                    }
                    //  compute the sum of all digits
                    sum = sum + digit    
                }
                //  multiply the sum by 9
                var acc_sum = sum * 9
                //  compute the checksum digit()
                var checksum = acc_sum % 10
                
                // check if last digit is equal to checksum
                //  get the last value of an id number
                var last_digit = this.input_id[this.input_id.length-1];
                if(last_digit == checksum){
                    // id is valid
                    return true;
                }   
                else{
                    throw "Invalid ID";
                }
            }

        }
        catch(err){
            return err;
        }
    }
}

export default SouthAfricanID