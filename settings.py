# Instance-specific values

# SECTION 1 - List of headers
HEADER = ['icode','title','citation','contact','dwca','email','eml','emlrights','gbifdatasetid','gbifpublisherid','iptlicense','migrator','networks','orgcountry','orgname','orgstateprovince','pubdate','source_url','url','id','associatedmedia','associatedoccurrences','associatedorganisms','associatedreferences','associatedsequences','associatedtaxa','bed','behavior','catalognumber','continent','coordinateprecision','coordinateuncertaintyinmeters','country','countrycode','county','dateidentified','day','decimallatitude','decimallongitude','disposition','earliestageorloweststage','earliesteonorlowesteonothem','earliestepochorlowestseries','earliesteraorlowesterathem','earliestperiodorlowestsystem','enddayofyear','establishmentmeans','eventdate','eventid','eventremarks','eventtime','fieldnotes','fieldnumber','footprintspatialfit','footprintsrs','footprintwkt','formation','geodeticdatum','geologicalcontextid','georeferencedby','georeferenceddate','georeferenceprotocol','georeferenceremarks','georeferencesources','georeferenceverificationstatus','group','habitat','highergeography','highergeographyid','highestbiostratigraphiczone','identificationid','identificationqualifier','identificationreferences','identificationremarks','identificationverificationstatus','identifiedby','individualcount','island','islandgroup','latestageorhigheststage','latesteonorhighesteonothem','latestepochorhighestseries','latesteraorhighesterathem','latestperiodorhighestsystem','lifestage','lithostratigraphicterms','locality','locationaccordingto','locationid','locationremarks','lowestbiostratigraphiczone','materialsampleid','maximumdepthinmeters','maximumdistanceabovesurfaceinmeters','maximumelevationinmeters','member','minimumdepthinmeters','minimumdistanceabovesurfaceinmeters','minimumelevationinmeters','month','municipality','occurrenceID','occurrenceremarks','occurrencestatus','organismid','organismname','organismremarks','organismscope','othercatalognumbers','pointradiusspatialfit','preparations','previousidentifications','recordedby','recordnumber','reproductivecondition','samplingeffort','samplingprotocol','sex','startdayofyear','stateprovince','typestatus','verbatimcoordinates','verbatimcoordinatesystem','verbatimdepth','verbatimelevation','verbatimeventdate','verbatimlatitude','verbatimlocality','verbatimlongitude','verbatimsrs','waterbody','year','type','modified','language','license','rightsholder','accessrights','bibliographiccitation','references','institutionid','collectionid','datasetid','institutioncode','collectioncode','datasetname','ownerinstitutioncode','basisOfRecord','informationwithheld','datageneralizations','dynamicproperties','taxonid','scientificnameid','acceptednameusageid','parentnameusageid','originalnameusageid','nameaccordingtoid','namepublishedinid','taxonconceptid','scientificname','acceptednameusage','parentnameusage','originalnameusage','nameaccordingto','namepublishedin','namepublishedinyear','higherclassification','kingdom','phylum','class','order','family','genus','subgenus','specificepithet','infraspecificepithet','taxonrank','verbatimtaxonrank','scientificnameauthorship','vernacularname','nomenclaturalcode','taxonomicstatus','nomenclaturalstatus','taxonremarks']

# SECTION 2 - Name of the table in MOL
TNAME = 'vertnet_jan2015'

# SECTION 3 (DO NOT MODIFY UNLESS NECESSARY) - Fix some reserved names in headers
HEADER_FIXED = []
for i in HEADER:
    t = "text"

    if i == "group":
        i = "_group"
    elif i == "references":
        i = "_references"
    elif i == "order":
        i = "_order"
    # add more if needed

    HEADER_FIXED.append(i)
