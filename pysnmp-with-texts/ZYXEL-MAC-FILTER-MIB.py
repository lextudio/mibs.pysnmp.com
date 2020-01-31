#
# PySNMP MIB module ZYXEL-MAC-FILTER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ZYXEL-MAC-FILTER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:50:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, ObjectIdentity, Bits, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Gauge32, ModuleIdentity, TimeTicks, Counter64, MibIdentifier, Unsigned32, IpAddress, iso = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ObjectIdentity", "Bits", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Gauge32", "ModuleIdentity", "TimeTicks", "Counter64", "MibIdentifier", "Unsigned32", "IpAddress", "iso")
MacAddress, TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TextualConvention", "DisplayString", "RowStatus")
esMgmt, = mibBuilder.importSymbols("ZYXEL-ES-SMI", "esMgmt")
zyxelMacFilter = ModuleIdentity((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 47))
if mibBuilder.loadTexts: zyxelMacFilter.setLastUpdated('201207010000Z')
if mibBuilder.loadTexts: zyxelMacFilter.setOrganization('Enterprise Solution ZyXEL')
if mibBuilder.loadTexts: zyxelMacFilter.setContactInfo('')
if mibBuilder.loadTexts: zyxelMacFilter.setDescription('The subtree for MAC filter')
zyxelMacFilterSetup = MibIdentifier((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 47, 1))
zyMacFilterMaxNumberOfRules = MibScalar((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 47, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: zyMacFilterMaxNumberOfRules.setStatus('current')
if mibBuilder.loadTexts: zyMacFilterMaxNumberOfRules.setDescription('The maximum number of filter rule that can be created.')
zyxelMacFilterTable = MibTable((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 47, 1, 2), )
if mibBuilder.loadTexts: zyxelMacFilterTable.setStatus('current')
if mibBuilder.loadTexts: zyxelMacFilterTable.setDescription('The table contains MAC filter configuration.')
zyxelMacFilterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 47, 1, 2, 1), ).setIndexNames((0, "ZYXEL-MAC-FILTER-MIB", "zyMacFilterMacAddress"), (0, "ZYXEL-MAC-FILTER-MIB", "zyMacFilterVid"))
if mibBuilder.loadTexts: zyxelMacFilterEntry.setStatus('current')
if mibBuilder.loadTexts: zyxelMacFilterEntry.setDescription('An entry contains MAC filter configuration.')
zyMacFilterMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 47, 1, 2, 1, 1), MacAddress())
if mibBuilder.loadTexts: zyMacFilterMacAddress.setStatus('current')
if mibBuilder.loadTexts: zyMacFilterMacAddress.setDescription('Type a MAC address in valid MAC address format, that is , six hexadecimal character pairs.')
zyMacFilterVid = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 47, 1, 2, 1, 2), Integer32())
if mibBuilder.loadTexts: zyMacFilterVid.setStatus('current')
if mibBuilder.loadTexts: zyMacFilterVid.setDescription('The VLAN group identificaton number.')
zyMacFilterName = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 47, 1, 2, 1, 3), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyMacFilterName.setStatus('current')
if mibBuilder.loadTexts: zyMacFilterName.setDescription('A descriptive name for this rule. This is for identification only.')
zyMacFilterAction = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 47, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("discardSource", 1), ("discardDestination", 2), ("both", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: zyMacFilterAction.setStatus('current')
if mibBuilder.loadTexts: zyMacFilterAction.setDescription('1.discard source : drop the frames from the source MAC address. The switch can still send frames to the MAC address. 2. discard destination: drop the frames to the destination MAC address. The switch can still receive frames originating from the MAC address. 3. both : block traffic to/from the MAC address specified in the MAC field.')
zyMacFilterRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 47, 1, 2, 1, 5), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: zyMacFilterRowStatus.setStatus('current')
if mibBuilder.loadTexts: zyMacFilterRowStatus.setDescription('This object allows entries to be created and deleted from the filter table.')
mibBuilder.exportSymbols("ZYXEL-MAC-FILTER-MIB", PYSNMP_MODULE_ID=zyxelMacFilter, zyxelMacFilterSetup=zyxelMacFilterSetup, zyxelMacFilterEntry=zyxelMacFilterEntry, zyMacFilterVid=zyMacFilterVid, zyxelMacFilter=zyxelMacFilter, zyMacFilterAction=zyMacFilterAction, zyxelMacFilterTable=zyxelMacFilterTable, zyMacFilterMaxNumberOfRules=zyMacFilterMaxNumberOfRules, zyMacFilterName=zyMacFilterName, zyMacFilterRowStatus=zyMacFilterRowStatus, zyMacFilterMacAddress=zyMacFilterMacAddress)