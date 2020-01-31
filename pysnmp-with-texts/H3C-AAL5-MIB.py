#
# PySNMP MIB module H3C-AAL5-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/H3C-AAL5-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:21:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
h3cAAL5, = mibBuilder.importSymbols("HUAWEI-3COM-OID-MIB", "h3cAAL5")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
MibIdentifier, Gauge32, Counter32, Integer32, iso, Bits, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, ModuleIdentity, Unsigned32, Counter64, NotificationType, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Gauge32", "Counter32", "Integer32", "iso", "Bits", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "ModuleIdentity", "Unsigned32", "Counter64", "NotificationType", "TimeTicks")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
h3cAAL5MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2011, 10, 2, 21, 1))
h3cAAL5MIB.setRevisions(('2004-11-04 13:50',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: h3cAAL5MIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: h3cAAL5MIB.setLastUpdated('200411041350Z')
if mibBuilder.loadTexts: h3cAAL5MIB.setOrganization('Hangzhou H3C Technologies Co., Ltd.')
if mibBuilder.loadTexts: h3cAAL5MIB.setContactInfo('PLAT Team Hangzhou H3C Technologies Co.,Ltd. Shang-Di Information Industry Base, Hai-Dian District Beijing P.R. China http://www.h3c.com Zip:100085')
if mibBuilder.loadTexts: h3cAAL5MIB.setDescription('This MIB file provides AAL5 specific information that are excluded by RFC 1695 ')
h3cAal5MIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 21, 1, 1))
h3cAal5MIBTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 21, 1, 0))
h3cAal5VccTable = MibTable((1, 3, 6, 1, 4, 1, 2011, 10, 2, 21, 1, 1, 1), )
if mibBuilder.loadTexts: h3cAal5VccTable.setStatus('current')
if mibBuilder.loadTexts: h3cAal5VccTable.setDescription('This table extends AAL5 VCC performance parameters which definded in aal5VccEntry of RFC1695.')
h3cAal5VccEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2011, 10, 2, 21, 1, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "H3C-AAL5-MIB", "h3cAal5VccVpi"), (0, "H3C-AAL5-MIB", "h3cAal5VccVci"))
if mibBuilder.loadTexts: h3cAal5VccEntry.setStatus('current')
if mibBuilder.loadTexts: h3cAal5VccEntry.setDescription('This list contains the additional AAL5 VCC performance parameters which are not definded in aal5VccEntry of RFC1695.')
h3cAal5VccVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 21, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095)))
if mibBuilder.loadTexts: h3cAal5VccVpi.setStatus('current')
if mibBuilder.loadTexts: h3cAal5VccVpi.setDescription('The VPI value of the AAL5 VCC.')
h3cAal5VccVci = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 21, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: h3cAal5VccVci.setStatus('current')
if mibBuilder.loadTexts: h3cAal5VccVci.setDescription('The VCI value of the AAL5 VCC.')
h3cAal5VccInPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 21, 1, 1, 1, 1, 3), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cAal5VccInPkts.setStatus('current')
if mibBuilder.loadTexts: h3cAal5VccInPkts.setDescription('The number of AAL5 CPCS PDUs received.')
h3cAal5VccOutPkts = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 21, 1, 1, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cAal5VccOutPkts.setStatus('current')
if mibBuilder.loadTexts: h3cAal5VccOutPkts.setDescription('The number of AAL5 CPCS PDUs transmitted.')
h3cAal5VccInOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 21, 1, 1, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cAal5VccInOctets.setStatus('current')
if mibBuilder.loadTexts: h3cAal5VccInOctets.setDescription('The number of AAL5 CPCS PDU octets received.')
h3cAal5VccOutOctets = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 21, 1, 1, 1, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cAal5VccOutOctets.setStatus('current')
if mibBuilder.loadTexts: h3cAal5VccOutOctets.setDescription('The number of AAL5 CPCS PDU octets transmitted.')
h3cAal5VccState = MibTableColumn((1, 3, 6, 1, 4, 1, 2011, 10, 2, 21, 1, 1, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("invalid", 1), ("active", 2), ("inactive", 3))).clone('active')).setMaxAccess("readonly")
if mibBuilder.loadTexts: h3cAal5VccState.setStatus('current')
if mibBuilder.loadTexts: h3cAal5VccState.setDescription("Indicates whether the particular virtual circuit is operational. 'Active' indicates the particular virtual circuit is operational. 'Inactive' indicates the circuit is temporarily disabled. 'Invalid' indicates the circuit is deleted")
h3cAal5VccStateChange = NotificationType((1, 3, 6, 1, 4, 1, 2011, 10, 2, 21, 1, 0, 1)).setObjects(("H3C-AAL5-MIB", "h3cAal5VccState"))
if mibBuilder.loadTexts: h3cAal5VccStateChange.setStatus('current')
if mibBuilder.loadTexts: h3cAal5VccStateChange.setDescription('The status of AAL5 VCC.')
h3cAal5MIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 21, 1, 3))
h3cAal5MIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 21, 1, 3, 1))
h3cAal5MIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 2011, 10, 2, 21, 1, 3, 2))
h3cAal5MIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 2011, 10, 2, 21, 1, 3, 1, 1)).setObjects(("H3C-AAL5-MIB", "h3cAal5MIBGroup"), ("H3C-AAL5-MIB", "h3cAal5NotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cAal5MIBCompliance = h3cAal5MIBCompliance.setStatus('current')
if mibBuilder.loadTexts: h3cAal5MIBCompliance.setDescription('The compliance statement.')
h3cAal5MIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 2011, 10, 2, 21, 1, 3, 2, 1)).setObjects(("H3C-AAL5-MIB", "h3cAal5VccInPkts"), ("H3C-AAL5-MIB", "h3cAal5VccOutPkts"), ("H3C-AAL5-MIB", "h3cAal5VccInOctets"), ("H3C-AAL5-MIB", "h3cAal5VccOutOctets"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cAal5MIBGroup = h3cAal5MIBGroup.setStatus('current')
if mibBuilder.loadTexts: h3cAal5MIBGroup.setDescription('A collection of objects.')
h3cAal5NotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 2011, 10, 2, 21, 1, 3, 2, 2)).setObjects(("H3C-AAL5-MIB", "h3cAal5VccStateChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    h3cAal5NotificationGroup = h3cAal5NotificationGroup.setStatus('current')
if mibBuilder.loadTexts: h3cAal5NotificationGroup.setDescription('Traps which may be used to enhance event driven management of the interface.')
mibBuilder.exportSymbols("H3C-AAL5-MIB", h3cAal5VccVpi=h3cAal5VccVpi, h3cAal5NotificationGroup=h3cAal5NotificationGroup, h3cAal5VccTable=h3cAal5VccTable, h3cAal5MIBConformance=h3cAal5MIBConformance, h3cAal5MIBGroups=h3cAal5MIBGroups, h3cAal5VccStateChange=h3cAal5VccStateChange, h3cAal5VccVci=h3cAal5VccVci, h3cAal5VccOutPkts=h3cAal5VccOutPkts, h3cAal5MIBCompliances=h3cAal5MIBCompliances, h3cAal5MIBGroup=h3cAal5MIBGroup, h3cAal5MIBTraps=h3cAal5MIBTraps, PYSNMP_MODULE_ID=h3cAAL5MIB, h3cAAL5MIB=h3cAAL5MIB, h3cAal5VccOutOctets=h3cAal5VccOutOctets, h3cAal5MIBObjects=h3cAal5MIBObjects, h3cAal5VccInOctets=h3cAal5VccInOctets, h3cAal5VccEntry=h3cAal5VccEntry, h3cAal5VccInPkts=h3cAal5VccInPkts, h3cAal5MIBCompliance=h3cAal5MIBCompliance, h3cAal5VccState=h3cAal5VccState)