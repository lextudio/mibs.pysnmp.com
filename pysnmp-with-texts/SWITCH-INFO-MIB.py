#
# PySNMP MIB module SWITCH-INFO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SWITCH-INFO-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:13:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, TimeTicks, Counter32, ObjectIdentity, Bits, NotificationType, Counter64, IpAddress, MibIdentifier, Gauge32, iso, Integer32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "TimeTicks", "Counter32", "ObjectIdentity", "Bits", "NotificationType", "Counter64", "IpAddress", "MibIdentifier", "Gauge32", "iso", "Integer32", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
switchVendor, = mibBuilder.importSymbols("TELESYN-ATI-TC", "switchVendor")
switchVendorMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 207, 8, 9, 300, 1))
switchVendorMib.setRevisions(('1997-05-16 22:00', '1996-11-05 22:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: switchVendorMib.setRevisionsDescriptions(('changed the max size of the vendorCopyright to 80 from 64.', 'Initial version.',))
if mibBuilder.loadTexts: switchVendorMib.setLastUpdated('9611052200Z')
if mibBuilder.loadTexts: switchVendorMib.setOrganization('')
if mibBuilder.loadTexts: switchVendorMib.setContactInfo('')
if mibBuilder.loadTexts: switchVendorMib.setDescription('The MIB module identifies objects containing vendor information.')
vendorInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 207, 8, 9, 300, 1, 1))
vendorName = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 9, 300, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vendorName.setStatus('current')
if mibBuilder.loadTexts: vendorName.setDescription('The vendor company name')
vendorProductName = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 9, 300, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vendorProductName.setStatus('current')
if mibBuilder.loadTexts: vendorProductName.setDescription('The product name assigned by the vendor Company')
vendorModelName = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 9, 300, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vendorModelName.setStatus('current')
if mibBuilder.loadTexts: vendorModelName.setDescription('The model name or number assigned by the vendor Company')
vendorModelId = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 9, 300, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vendorModelId.setStatus('current')
if mibBuilder.loadTexts: vendorModelId.setDescription('The model identifier assigend by the vendor Company')
vendorCopyright = MibScalar((1, 3, 6, 1, 4, 1, 207, 8, 9, 300, 1, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 80))).setMaxAccess("readonly")
if mibBuilder.loadTexts: vendorCopyright.setStatus('current')
if mibBuilder.loadTexts: vendorCopyright.setDescription('The copyright string for the product.')
mibBuilder.exportSymbols("SWITCH-INFO-MIB", vendorModelId=vendorModelId, vendorInfo=vendorInfo, switchVendorMib=switchVendorMib, vendorModelName=vendorModelName, vendorCopyright=vendorCopyright, vendorProductName=vendorProductName, PYSNMP_MODULE_ID=switchVendorMib, vendorName=vendorName)