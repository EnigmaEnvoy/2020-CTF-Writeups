# Find cell (OSINT)  
  
> I lost my phone while I was travelling back to home, I was able to get back my eNB ID, MCC and MNC could you help me catch the tower it was last found.  
> note: decimal value upto 1 digit  
> Flag Format : darkCTF{latitude,longitude}  
  
> The MCC, MNC and eNB ID given in that order are:  
> 310  
> 410  
> 81907  

Using [cellmapper](https://www.cellmapper.net/map), select the operator to AT&T Mobility - 310410 (from MCC and MNC) and 81907 (from eNB ID) in tower search.  
This gives us the tower and it's coordinates in the [URL](https://www.cellmapper.net/map?MCC=310&MNC=410&type=LTE&latitude=32.84644890905747&longitude=-24.554806096440018&zoom=16&showTowers=true&showTowerLabels=true&clusterEnabled=true&tilesEnabled=true&showOrphans=false&showNoFrequencyOnly=false&showFrequencyOnly=false&showBandwidthOnly=false&DateFilterType=None&showHex=false&showVerifiedOnly=false&showUnverifiedOnly=false&showLTECAOnly=false&showENDCOnly=false&showBand=0&showSectorColours=true)  
  
  
### Flag
`darkCTF{32.8,-24.5}`
