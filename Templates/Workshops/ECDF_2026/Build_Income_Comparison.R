# Rebuild the 2020 Canada/USA income thresholds used in the workshop.
# Run this script from the workshop directory.
# The supplied CSV uses the LIS June 2026 release, processed by Our World in Data.
# Rerunning the downloads may retrieve later revisions.
# Definitions: https://www.lisdatacenter.org/data-access/lis-in-our-world-in-data-owid/
# Each person's income is household income divided by sqrt(household size), in annual 2021 PPP dollars.

hdir <- getwd()
cache_dir <- file.path(tempdir(), 'lis_income_comparison')
dir.create(cache_dir, showWarnings=FALSE)

## Download the published decile thresholds for both income concepts.
base_url <- 'https://ourworldindata.org/explorers/incomes-across-distribution-lis.csv'
source_measures <- c(disposable='After+tax', market='Before+tax')
threshold_names <- c('Poorest decile', '2nd decile', '3rd decile', '4th decile',
    '5th decile', '6th decile', '7th decile', '8th decile', 'Richest decile')
income_parts <- list()
for (concept in names(source_measures)) {
    source_url <- paste0(base_url,
        '?tab=table&time=2020&country=CAN~USA&Indicator=Decile+thresholds',
        '&Decile=All+deciles&Income+measure=', source_measures[[concept]],
        '&Period=Year&Adjust+for+cost+sharing+within+households+(equivalized+income)=true')
    source_file <- file.path(cache_dir, paste0(concept, '.csv'))
    download.file(source_url, source_file, mode='wb', quiet=TRUE)
    raw <- read.csv(source_file, check.names=FALSE)

    # The export includes all countries and years despite the URL's selection parameters.
    stopifnot(all(c('Entity', 'Code', 'Year', threshold_names) %in% names(raw)))
    raw <- raw[raw$Code %in% c('CAN', 'USA') & raw$Year == 2020, ]
    raw <- raw[order(raw$Code), ]
    stopifnot(nrow(raw) == 2L, identical(raw$Code, c('CAN', 'USA')))

    # The final column is P90, the threshold entering the richest tenth, rather than P100.
    # Select columns by name so export ordering cannot silently change the percentile mapping.
    for (i in seq_len(nrow(raw))) {
        thresholds <- as.numeric(unlist(raw[i, threshold_names], use.names=FALSE))
        stopifnot(length(thresholds) == 9L, all(is.finite(thresholds)), all(diff(thresholds) > 0))
        income_parts[[length(income_parts) + 1L]] <- data.frame(
            country=raw$Entity[i], code=raw$Code[i], year=raw$Year[i],
            concept=concept, percentile=seq(10, 90, by=10),
            threshold_2021_ppp=thresholds)
    }
}

## Save the compact input so rendering needs no network connection.
income <- do.call(rbind, income_parts)
rownames(income) <- NULL
stopifnot(nrow(income) == 36L,
    !anyDuplicated(income[c('code', 'year', 'concept', 'percentile')]))
output_file <- file.path(hdir, 'income_lis_2020.csv')
write.csv(income, output_file, row.names=FALSE)
cat('Saved', nrow(income), 'published income thresholds to', basename(output_file), '\n')
