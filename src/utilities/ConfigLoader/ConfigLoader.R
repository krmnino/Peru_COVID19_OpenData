# Set up environment for ConfigLoader to operate
ConfigLoader_set_env <- function(working_dir){
  # Load dependencies
  library(stringi)
  
  # Define ConfigLoader structure
  setClass(
    "ConfigLoader",
    slots = list(
      entries = "numeric",
      keys = "character",
      values = "character"
    )
  )
  # Set working directory where R script is located
  setwd(working_dir)
}


# Instantiate ConfigLoader object given a valid path
ConfigLoader_init <- function(path){
  # Open config file
  config_file <- file(path, "r")
  
  # Allocate buffer for incoming data
  buffer = ""
  
  # Read line by line and add to buffer
  while(TRUE){
    line = readLines(config_file, n=1, warn=FALSE)
    if(length(line) == 0){
      break
    }
    else if(substr(line, 1, 1) == '#'){
      next
    }
    else{
      buffer <- paste(buffer, line, sep="")
    }
  }
  close(config_file)
  
  # Separate entries by semicolon
  entries <- unlist(strsplit(buffer, ";"))
  temp <- c()
  
  # Remove blank entries 
  for(i in 1:length(entries)){
    if(nchar(entries[i]) != 0){
      temp <- append(temp, entries[i])
    }
  }
  entries <- temp
  n_entries <- length(entries)
  
  
  # Process and sanitize keys and values
  keys <- c()
  values <- c()
  for (i in 1:n_entries){
    temp <- unlist(strsplit(entries[i], "="))
    
    key <- temp[1]
    key <- stri_trim_left(key)
    key <- stri_trim_right(key)
    keys <- append(keys, key)
    
    value <- temp[2]
    value <- stri_trim_left(value)
    value <- stri_trim_right(value)  
    values <- append(values, value)
  }
  
  # Intiialize ConfigLoader object
  cf <- new("ConfigLoader",
            entries=n_entries,
            keys=keys,
            values=values)
  return(cf)
}


# Get value given a key
ConfigLoader_get_value <- function(config, key){
  idx <- match(key, config@keys)
  # Check if key was found
  if(is.na(idx)){
    print(paste("ERROR: Could not find key ", key))
    return(-1)
  }
  value <- config@values[idx]
  # Check if value is a list of values
  if(substr(value, 1, 1) == "[" &&
     substr(value, nchar(value), nchar(value)) == "]"){
    # Split list value by commas
    value <- substr(value, 2, nchar(value) - 1)
    split_list <- unlist(strsplit(value, ","))
    # Sanitize elements in list value
    temp <- c()
    for (i in 1:length(split_list)){
      elem <- split_list[i]
      elem <- stri_trim_left(elem)
      elem <- stri_trim_right(elem)
      elem <- gsub("\t", "", elem)
      temp <- append(temp, elem)
    }
    split_list <- temp
    return(split_list)
  }
  return(value)
}


# Add key-value pair into ConfigLoader object
ConfigLoader_add_entry <- function(config, key, value){
  idx <- match(key, config@keys)
  # Check if key was found
  if(!is.na(idx)){
    print(paste("ERROR: Repeated key ", key))
    return(config)
  }
  # Key must be a string
  if(!is.character(key)){
    print(paste("ERROR: Key must be of type character."))
    return(config)
    
  }
  # Value must be a string
  if(!is.character(value)){
    print(paste("ERROR: Value must be of type character."))
    return(config)
  }
  # Add key value pair to ConfigLoader object
  config@keys <- append(config@keys, key)
  config@values <- append(config@values, value)
  # Return updated object
  return(config)
}


# Edit certain value in ConfigLoader object given a key
ConfigLoader_edit_value <- function(config, key, new_value){
  idx <- match(key, config@keys)
  # Check if key was found
  if(is.na(idx)){
    print(paste("ERROR: Could not find key ", key))
    return(config)
  }
  # Key must be a string
  if(!is.character(key)){
    print(paste("ERROR: Key must be of type character."))
    return(config)
    
  }
  # New value must be a string
  if(!is.character(new_value)){
    print(paste("ERROR: New value must be of type character."))
    return(config)
  }
  # Edit value in ConfigLoader object
  config@values[idx] <- new_value
  # Return updated object
  return(config)
}


# Save current state of ConfigLoader object to a file
ConfigLoader_save_config <- function(config, path){
  # Initialize empty buffer
  buffer <- c()
  # Loop through each key-value pair
  for(i in 1:config@entries){
    # Obtain key and value
    key <- config@keys[i]
    value <- config@values[i]
    # If value is a list, we need to handle it differently
    if(substr(value, 1, 1) == "[" &&
       substr(value, nchar(value), nchar(value)) == "]"){
      # Remove square brackets, we will put them back later
      value <- substr(value, 2, nchar(value) - 1)
      # Split list value by commas
      split_list <- unlist(strsplit(value, ","))
      # Sanitize elements in list value
      temp <- "["
      for (i in 1:length(split_list)){
        elem <- split_list[i]
        elem <- stri_trim_left(elem)
        elem <- stri_trim_right(elem)
        elem <- gsub("\t", "", elem)
        # If element is not the last one then add a comma afterwards
        if(i != length(split_list)){
          temp <- paste(temp, elem, ",", sep="")  
        }
        else{
          temp <- paste(temp, elem, sep="")
        }
      }
      # Close list value with closing square bracket
      temp <- paste(temp, "]", sep="")
      value <- temp
    }
    # Put key-value entry together with semicolon at the end
    line <- paste(key, " = ", value, ";", sep="")
    # Add key-value entry to buffer
    buffer <- append(buffer, line)
  }
  # Open file and dump buffer
  out_file <- file(path)
  writeLines(buffer, out_file)
  close(out_file)
}