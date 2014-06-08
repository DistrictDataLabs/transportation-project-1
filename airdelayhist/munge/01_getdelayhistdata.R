require(data.table)
require(lubridate)
library(data.table)

#Part 1. Read data
#fileUrl <- "http://www.transtats.bts.gov/OT_Delay/ot_delaycause1.asp?display=download&pn=0&month=3&year=2014"
#zipFile <- download.file(fileUrl, dest="data/delay_causes_btr.zip", method= "curl")

#Unzip file

filebtr_delay_zip <- "data/347295756_32014_5610_airline_delay_causes.zip"
file_delay_causes <- "data/airline_delay_causes.csv"

if (!file.exists(file_delay_causes)){
        
if (file.exists(filebtr_delay_zip)){
        
unzip("data/347295756_32014_5610_airline_delay_causes.zip",  overwrite = TRUE,
        exdir = "./data", unzip = "internal",
        setTimes = FALSE)
        extracted_delay_csv <- "data/347295756_32014_5610_airline_delay_causes.csv"
        
        if (file.exists(extracted_delay_csv)){
           file.rename(extracted_delay_csv, file_delay_causes)        
        }
}

}

#Part 2. Clean Data
if (file.exists(file_delay_causes)){
# Get column classes
dt.head <- fread(file_delay_causes, sep=",", nrows=5, showProgress=getOption("datatable.showProgress"))
classes <- sapply(dt.head, class)

# Read csv file
data <- fread(file_delay_causes, sep=",",  colClasses = classes, showProgress=getOption("datatable.showProgress"))
names(data)  

#Replace whitespaces
data <- data.table(data)

invalid_columns <- which(grepl(" ", colnames(data)))

if (length(invalid_columns) >0 ) {
setnames(data," month", "month")
setnames(data," weather_ct", "weather_ct")
setnames(data," carrier_delay", "carrier_delay")
setnames(data," arr_delay", "arr_delay")

write.csv(data,"data/airline_delay_causes.csv")

}

}