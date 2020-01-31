#
# PySNMP MIB module BLUECOAT-AV-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BLUECOAT-AV-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:39:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
blueCoatMgmt, = mibBuilder.importSymbols("BLUECOAT-MIB", "blueCoatMgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, MibIdentifier, iso, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, IpAddress, TimeTicks, NotificationType, Bits, Gauge32, ModuleIdentity, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "MibIdentifier", "iso", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "IpAddress", "TimeTicks", "NotificationType", "Bits", "Gauge32", "ModuleIdentity", "Counter64", "Counter32")
TextualConvention, DateAndTime, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DateAndTime", "DisplayString")
blueCoatAvMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 3417, 2, 10))
if mibBuilder.loadTexts: blueCoatAvMib.setLastUpdated('0704160000Z')
if mibBuilder.loadTexts: blueCoatAvMib.setOrganization('Blue Coat Systems, Inc.')
if mibBuilder.loadTexts: blueCoatAvMib.setContactInfo('support@bluecoat.com')
if mibBuilder.loadTexts: blueCoatAvMib.setDescription('The AV MIB is used to monitor antivirus related info.')
blueCoatAvMibObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 10, 1))
blueCoatAvMibNotificationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 10, 2))
blueCoatAvMibNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 3417, 2, 10, 3))
avFilesScanned = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 10, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avFilesScanned.setStatus('current')
if mibBuilder.loadTexts: avFilesScanned.setDescription('Number of files scanned. An archive containing multiple files will count as one file.')
avVirusesDetected = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 10, 1, 2), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avVirusesDetected.setStatus('current')
if mibBuilder.loadTexts: avVirusesDetected.setDescription('Number of infected files detected. A file containing multiple infections will count as one infected file.')
avPatternVersion = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 10, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avPatternVersion.setStatus('current')
if mibBuilder.loadTexts: avPatternVersion.setDescription('AV pattern version.')
avPatternDateTime = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 10, 1, 4), DateAndTime()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avPatternDateTime.setStatus('current')
if mibBuilder.loadTexts: avPatternDateTime.setDescription('Release date and time of the av pattern.')
avEngineVersion = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 10, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avEngineVersion.setStatus('current')
if mibBuilder.loadTexts: avEngineVersion.setDescription('AV engine version.')
avVendorName = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 10, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avVendorName.setStatus('current')
if mibBuilder.loadTexts: avVendorName.setDescription('AV vendor name.')
avLicenseDaysRemaining = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 10, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avLicenseDaysRemaining.setStatus('current')
if mibBuilder.loadTexts: avLicenseDaysRemaining.setDescription('AV license days remaining.')
avPublishedFirmwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 10, 1, 8), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avPublishedFirmwareVersion.setStatus('current')
if mibBuilder.loadTexts: avPublishedFirmwareVersion.setDescription('ProxyAV version published on the automatic update location.')
avInstalledFirmwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 10, 1, 9), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avInstalledFirmwareVersion.setStatus('current')
if mibBuilder.loadTexts: avInstalledFirmwareVersion.setDescription('Currently installed ProxyAV firmware version.')
avSlowICAPConnections = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 10, 1, 10), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: avSlowICAPConnections.setStatus('current')
if mibBuilder.loadTexts: avSlowICAPConnections.setDescription("The number of ICAP connections that are considered 'slow' - receiving data for more than the configured time threshold (by default 60 seconds).")
avUpdateFailureReason = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 10, 2, 1), DisplayString())
if mibBuilder.loadTexts: avUpdateFailureReason.setStatus('current')
if mibBuilder.loadTexts: avUpdateFailureReason.setDescription('The reason why the av engine/pattern/firmware update failed.')
avUrl = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 10, 2, 2), DisplayString())
if mibBuilder.loadTexts: avUrl.setStatus('current')
if mibBuilder.loadTexts: avUrl.setDescription('The URL for use in notifications.')
avVirusName = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 10, 2, 3), DisplayString())
if mibBuilder.loadTexts: avVirusName.setStatus('current')
if mibBuilder.loadTexts: avVirusName.setDescription('The name of the infection found.')
avVirusDetails = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 10, 2, 4), DisplayString())
if mibBuilder.loadTexts: avVirusDetails.setStatus('current')
if mibBuilder.loadTexts: avVirusDetails.setDescription('More details about the infection found.')
avErrorCode = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 10, 2, 5), DisplayString())
if mibBuilder.loadTexts: avErrorCode.setStatus('current')
if mibBuilder.loadTexts: avErrorCode.setDescription('Error code identifying the scan exception, like max_file_size_exceeded.')
avErrorDetails = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 10, 2, 6), DisplayString())
if mibBuilder.loadTexts: avErrorDetails.setStatus('current')
if mibBuilder.loadTexts: avErrorDetails.setDescription('More details about the scan exception.')
avPreviousFirmwareVersion = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 10, 2, 7), DisplayString())
if mibBuilder.loadTexts: avPreviousFirmwareVersion.setStatus('current')
if mibBuilder.loadTexts: avPreviousFirmwareVersion.setDescription('The firmware version before the firmware update.')
avICTMWarningReason = MibScalar((1, 3, 6, 1, 4, 1, 3417, 2, 10, 2, 8), DisplayString())
if mibBuilder.loadTexts: avICTMWarningReason.setStatus('current')
if mibBuilder.loadTexts: avICTMWarningReason.setDescription('The reason of the Intelligent Connection Traffic Monitoring warning.')
avAntivirusUpdateSuccess = NotificationType((1, 3, 6, 1, 4, 1, 3417, 2, 10, 3, 1)).setObjects(("BLUECOAT-AV-MIB", "avVendorName"), ("BLUECOAT-AV-MIB", "avEngineVersion"), ("BLUECOAT-AV-MIB", "avPatternVersion"), ("BLUECOAT-AV-MIB", "avPatternDateTime"))
if mibBuilder.loadTexts: avAntivirusUpdateSuccess.setStatus('current')
if mibBuilder.loadTexts: avAntivirusUpdateSuccess.setDescription('Successful av engine/pattern update.')
avAntivirusUpdateFailed = NotificationType((1, 3, 6, 1, 4, 1, 3417, 2, 10, 3, 2)).setObjects(("BLUECOAT-AV-MIB", "avUpdateFailureReason"), ("BLUECOAT-AV-MIB", "avVendorName"), ("BLUECOAT-AV-MIB", "avEngineVersion"), ("BLUECOAT-AV-MIB", "avPatternVersion"), ("BLUECOAT-AV-MIB", "avPatternDateTime"))
if mibBuilder.loadTexts: avAntivirusUpdateFailed.setStatus('current')
if mibBuilder.loadTexts: avAntivirusUpdateFailed.setDescription('Av engine/pattern update failed, avUpdateFailureReason provides more details.')
avVirusDetected = NotificationType((1, 3, 6, 1, 4, 1, 3417, 2, 10, 3, 3)).setObjects(("BLUECOAT-AV-MIB", "avUrl"), ("BLUECOAT-AV-MIB", "avVirusName"), ("BLUECOAT-AV-MIB", "avVirusDetails"))
if mibBuilder.loadTexts: avVirusDetected.setStatus('current')
if mibBuilder.loadTexts: avVirusDetected.setDescription('Infected file detected at avUrl.')
avFileServed = NotificationType((1, 3, 6, 1, 4, 1, 3417, 2, 10, 3, 4)).setObjects(("BLUECOAT-AV-MIB", "avUrl"), ("BLUECOAT-AV-MIB", "avErrorCode"), ("BLUECOAT-AV-MIB", "avErrorDetails"))
if mibBuilder.loadTexts: avFileServed.setStatus('current')
if mibBuilder.loadTexts: avFileServed.setDescription('File served without scanning. It could not be scanned completely due to a scan exception.')
avFileBlocked = NotificationType((1, 3, 6, 1, 4, 1, 3417, 2, 10, 3, 5)).setObjects(("BLUECOAT-AV-MIB", "avUrl"), ("BLUECOAT-AV-MIB", "avErrorCode"), ("BLUECOAT-AV-MIB", "avErrorDetails"))
if mibBuilder.loadTexts: avFileBlocked.setStatus('current')
if mibBuilder.loadTexts: avFileBlocked.setDescription('File blocked. It could not be scanned completely due to a scan exception.')
avNewFirmwareAvailable = NotificationType((1, 3, 6, 1, 4, 1, 3417, 2, 10, 3, 6)).setObjects(("BLUECOAT-AV-MIB", "avInstalledFirmwareVersion"), ("BLUECOAT-AV-MIB", "avPublishedFirmwareVersion"))
if mibBuilder.loadTexts: avNewFirmwareAvailable.setStatus('current')
if mibBuilder.loadTexts: avNewFirmwareAvailable.setDescription('New firmware version published at the Blue Coat download location.')
avFirmwareUpdateSuccess = NotificationType((1, 3, 6, 1, 4, 1, 3417, 2, 10, 3, 7)).setObjects(("BLUECOAT-AV-MIB", "avPreviousFirmwareVersion"), ("BLUECOAT-AV-MIB", "avInstalledFirmwareVersion"))
if mibBuilder.loadTexts: avFirmwareUpdateSuccess.setStatus('current')
if mibBuilder.loadTexts: avFirmwareUpdateSuccess.setDescription('Firmware update completed successfully.')
avFirmwareUpdateFailed = NotificationType((1, 3, 6, 1, 4, 1, 3417, 2, 10, 3, 8)).setObjects(("BLUECOAT-AV-MIB", "avInstalledFirmwareVersion"), ("BLUECOAT-AV-MIB", "avPublishedFirmwareVersion"), ("BLUECOAT-AV-MIB", "avUpdateFailureReason"))
if mibBuilder.loadTexts: avFirmwareUpdateFailed.setStatus('current')
if mibBuilder.loadTexts: avFirmwareUpdateFailed.setDescription('Firmware update failed.')
avAntivirusLicenseWarning = NotificationType((1, 3, 6, 1, 4, 1, 3417, 2, 10, 3, 9)).setObjects(("BLUECOAT-AV-MIB", "avVendorName"), ("BLUECOAT-AV-MIB", "avLicenseDaysRemaining"))
if mibBuilder.loadTexts: avAntivirusLicenseWarning.setStatus('current')
if mibBuilder.loadTexts: avAntivirusLicenseWarning.setDescription('The antivirus license is about to expire.')
avICTMWarning = NotificationType((1, 3, 6, 1, 4, 1, 3417, 2, 10, 3, 10)).setObjects(("BLUECOAT-AV-MIB", "avICTMWarningReason"), ("BLUECOAT-AV-MIB", "avSlowICAPConnections"))
if mibBuilder.loadTexts: avICTMWarning.setStatus('current')
if mibBuilder.loadTexts: avICTMWarning.setDescription("The warning from the Intelligent Connection Traffic Monitoring feature that the number of 'slow' connections has crossed the threshold value.")
mibBuilder.exportSymbols("BLUECOAT-AV-MIB", blueCoatAvMibObjects=blueCoatAvMibObjects, avFilesScanned=avFilesScanned, avFirmwareUpdateFailed=avFirmwareUpdateFailed, avInstalledFirmwareVersion=avInstalledFirmwareVersion, avFileServed=avFileServed, blueCoatAvMibNotifications=blueCoatAvMibNotifications, avPublishedFirmwareVersion=avPublishedFirmwareVersion, avICTMWarningReason=avICTMWarningReason, avFileBlocked=avFileBlocked, avPatternDateTime=avPatternDateTime, avVirusDetected=avVirusDetected, avAntivirusUpdateFailed=avAntivirusUpdateFailed, avFirmwareUpdateSuccess=avFirmwareUpdateSuccess, avAntivirusLicenseWarning=avAntivirusLicenseWarning, blueCoatAvMibNotificationObjects=blueCoatAvMibNotificationObjects, avUrl=avUrl, avSlowICAPConnections=avSlowICAPConnections, avAntivirusUpdateSuccess=avAntivirusUpdateSuccess, avVirusName=avVirusName, avErrorCode=avErrorCode, avNewFirmwareAvailable=avNewFirmwareAvailable, blueCoatAvMib=blueCoatAvMib, avPreviousFirmwareVersion=avPreviousFirmwareVersion, avVirusesDetected=avVirusesDetected, avLicenseDaysRemaining=avLicenseDaysRemaining, PYSNMP_MODULE_ID=blueCoatAvMib, avVirusDetails=avVirusDetails, avICTMWarning=avICTMWarning, avEngineVersion=avEngineVersion, avVendorName=avVendorName, avErrorDetails=avErrorDetails, avUpdateFailureReason=avUpdateFailureReason, avPatternVersion=avPatternVersion)