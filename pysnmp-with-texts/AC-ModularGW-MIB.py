#
# PySNMP MIB module AC-ModularGW-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AC-ModularGW-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:09:21 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, ModuleIdentity, TimeTicks, Counter32, Unsigned32, enterprises, Integer32, Counter64, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, ObjectIdentity, IpAddress, Gauge32, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "ModuleIdentity", "TimeTicks", "Counter32", "Unsigned32", "enterprises", "Integer32", "Counter64", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "ObjectIdentity", "IpAddress", "Gauge32", "MibIdentifier")
DateAndTime, DisplayString, TAddress, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DateAndTime", "DisplayString", "TAddress", "TextualConvention")
audioCodes = MibIdentifier((1, 3, 6, 1, 4, 1, 5003))
acRegistrations = MibIdentifier((1, 3, 6, 1, 4, 1, 5003, 7))
acGeneric = MibIdentifier((1, 3, 6, 1, 4, 1, 5003, 8))
acProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 5003, 9))
acBoardMibs = MibIdentifier((1, 3, 6, 1, 4, 1, 5003, 9, 10))
acModularGateway = ModuleIdentity((1, 3, 6, 1, 4, 1, 5003, 9, 10, 11))
if mibBuilder.loadTexts: acModularGateway.setLastUpdated('200608155063Z')
if mibBuilder.loadTexts: acModularGateway.setOrganization('AudioCodes Ltd')
if mibBuilder.loadTexts: acModularGateway.setContactInfo('Postal: AudioCodes LTD 4 Horesh Road Yehud 56470, ISRAEL Tel: 972-3-5394000 Email: support@audiocodes.com')
if mibBuilder.loadTexts: acModularGateway.setDescription('This MIB is solely for AudioCodes modular Gateways. Use this MIBs status section for cross reference tables connecting analog/digital ports to the modules on which they are. The MIB has become deprecated as of version 5.2. It will be obsolete as of version 5.4')
acModularGatewayConfiguration = MibIdentifier((1, 3, 6, 1, 4, 1, 5003, 9, 10, 11, 1))
acModularGatewayStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 5003, 9, 10, 11, 2))
acModularGWModules = MibIdentifier((1, 3, 6, 1, 4, 1, 5003, 9, 10, 11, 2, 1))
acModularGWModuleTable = MibTable((1, 3, 6, 1, 4, 1, 5003, 9, 10, 11, 2, 1, 20), )
if mibBuilder.loadTexts: acModularGWModuleTable.setStatus('current')
if mibBuilder.loadTexts: acModularGWModuleTable.setDescription("This table holds the information about each module in Audiocodes' modular gateways. If an index (Module number) is shown - then the module is in and working. You can also see the modules type, number of ports and it's first port's logical number allowing you to calculate which port is which logical trunk or analog channel. (This information is also obtainable in the acModularGWTrunkTable and acModularGWChannelTable).")
acModularGWModuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5003, 9, 10, 11, 2, 1, 20, 1), ).setIndexNames((0, "AC-ModularGW-MIB", "acModularGWModuleIndex"))
if mibBuilder.loadTexts: acModularGWModuleEntry.setStatus('current')
if mibBuilder.loadTexts: acModularGWModuleEntry.setDescription('')
acModularGWModuleIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 11, 2, 1, 20, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 6)))
if mibBuilder.loadTexts: acModularGWModuleIndex.setStatus('deprecated')
if mibBuilder.loadTexts: acModularGWModuleIndex.setDescription('Module index. 1 is the first Module - top left corner. 2 is the next Module to the right and so on. 4 is under 1.')
acModularGWModuleType = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 11, 2, 1, 20, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 4))).clone(namedValues=NamedValues(("e1-t1-QUAD", 0), ("fxs", 1), ("fxo", 2), ("e1-t1-FALC56", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acModularGWModuleType.setStatus('deprecated')
if mibBuilder.loadTexts: acModularGWModuleType.setDescription('Module Type. The Modules are characterized according to their ports. 0 = Digital - Quad. 1 = Analog - FXS. 2 = Analog - FXO. 4 = Digital - FALC.')
acModularGWModuleNumOfPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 11, 2, 1, 20, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acModularGWModuleNumOfPorts.setStatus('deprecated')
if mibBuilder.loadTexts: acModularGWModuleNumOfPorts.setDescription('The number of physical interfaces in a module, analog or digital.')
acModularGWModuleFirstPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 11, 2, 1, 20, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 19))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acModularGWModuleFirstPortNum.setStatus('deprecated')
if mibBuilder.loadTexts: acModularGWModuleFirstPortNum.setDescription('The logical number as seen in the general trunk/analog-channel table of the first port in the module in question. Since analog and digital ports can be operational at once, analog and digital ports may have same logical number.')
acModularGWCrossReference = MibIdentifier((1, 3, 6, 1, 4, 1, 5003, 9, 10, 11, 2, 2))
acModularGWTrunkTable = MibTable((1, 3, 6, 1, 4, 1, 5003, 9, 10, 11, 2, 2, 20), )
if mibBuilder.loadTexts: acModularGWTrunkTable.setStatus('current')
if mibBuilder.loadTexts: acModularGWTrunkTable.setDescription('This table shows the trunk location and type.')
acModularGWTrunkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5003, 9, 10, 11, 2, 2, 20, 1), ).setIndexNames((0, "AC-ModularGW-MIB", "acModularGWTrunkIndex"))
if mibBuilder.loadTexts: acModularGWTrunkEntry.setStatus('current')
if mibBuilder.loadTexts: acModularGWTrunkEntry.setDescription('')
acModularGWTrunkIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 11, 2, 2, 20, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 23)))
if mibBuilder.loadTexts: acModularGWTrunkIndex.setStatus('deprecated')
if mibBuilder.loadTexts: acModularGWTrunkIndex.setDescription("Trunk index. The trunk in question's logical number.")
acModularGWTrunkOnModuleNum = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 11, 2, 2, 20, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 6))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acModularGWTrunkOnModuleNum.setStatus('deprecated')
if mibBuilder.loadTexts: acModularGWTrunkOnModuleNum.setDescription('Module number on which the trunk in question is placed. 1 is the first Module - top left corner. 2 is the next Module to the right and so on. 4 is under 1.')
acModularGWTrunkOnPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 11, 2, 2, 20, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acModularGWTrunkOnPortNum.setStatus('deprecated')
if mibBuilder.loadTexts: acModularGWTrunkOnPortNum.setDescription('Physical Port on module. 1 - left most port.')
acModularGWAnalogPortTable = MibTable((1, 3, 6, 1, 4, 1, 5003, 9, 10, 11, 2, 2, 21), )
if mibBuilder.loadTexts: acModularGWAnalogPortTable.setStatus('current')
if mibBuilder.loadTexts: acModularGWAnalogPortTable.setDescription('This table shows the analog port location and type.')
acModularGWAnalogPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5003, 9, 10, 11, 2, 2, 21, 1), ).setIndexNames((0, "AC-ModularGW-MIB", "acModularGWAnalogPortIndex"))
if mibBuilder.loadTexts: acModularGWAnalogPortEntry.setStatus('current')
if mibBuilder.loadTexts: acModularGWAnalogPortEntry.setDescription('')
acModularGWAnalogPortIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 11, 2, 2, 21, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 23)))
if mibBuilder.loadTexts: acModularGWAnalogPortIndex.setStatus('deprecated')
if mibBuilder.loadTexts: acModularGWAnalogPortIndex.setDescription("Channel index. The channel in question's logical number.")
acModularGWAnalogPortOnModuleNum = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 11, 2, 2, 21, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 6))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acModularGWAnalogPortOnModuleNum.setStatus('deprecated')
if mibBuilder.loadTexts: acModularGWAnalogPortOnModuleNum.setDescription('Module number on which the analog port in question is placed. 1 is the first Module - top left corner. 2 is the next Module to the right and so on. 4 is under 1.')
acModularGWAnalogPortOnPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 5003, 9, 10, 11, 2, 2, 21, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4))).setMaxAccess("readonly")
if mibBuilder.loadTexts: acModularGWAnalogPortOnPortNum.setStatus('deprecated')
if mibBuilder.loadTexts: acModularGWAnalogPortOnPortNum.setDescription('Physical port on module. 1 - left most port.')
acModularGatewayAction = MibIdentifier((1, 3, 6, 1, 4, 1, 5003, 9, 10, 11, 3))
mibBuilder.exportSymbols("AC-ModularGW-MIB", acGeneric=acGeneric, acBoardMibs=acBoardMibs, acModularGatewayStatus=acModularGatewayStatus, acModularGWTrunkOnPortNum=acModularGWTrunkOnPortNum, acModularGWModuleTable=acModularGWModuleTable, acModularGateway=acModularGateway, acModularGWModuleEntry=acModularGWModuleEntry, acModularGWTrunkEntry=acModularGWTrunkEntry, acModularGWTrunkIndex=acModularGWTrunkIndex, acModularGWModules=acModularGWModules, acModularGWTrunkTable=acModularGWTrunkTable, acModularGWAnalogPortOnPortNum=acModularGWAnalogPortOnPortNum, acModularGWAnalogPortIndex=acModularGWAnalogPortIndex, acModularGWModuleFirstPortNum=acModularGWModuleFirstPortNum, acProducts=acProducts, acModularGWCrossReference=acModularGWCrossReference, acModularGatewayAction=acModularGatewayAction, acModularGWModuleType=acModularGWModuleType, PYSNMP_MODULE_ID=acModularGateway, acModularGatewayConfiguration=acModularGatewayConfiguration, acModularGWModuleNumOfPorts=acModularGWModuleNumOfPorts, acRegistrations=acRegistrations, acModularGWAnalogPortTable=acModularGWAnalogPortTable, acModularGWAnalogPortEntry=acModularGWAnalogPortEntry, acModularGWAnalogPortOnModuleNum=acModularGWAnalogPortOnModuleNum, acModularGWModuleIndex=acModularGWModuleIndex, audioCodes=audioCodes, acModularGWTrunkOnModuleNum=acModularGWTrunkOnModuleNum)