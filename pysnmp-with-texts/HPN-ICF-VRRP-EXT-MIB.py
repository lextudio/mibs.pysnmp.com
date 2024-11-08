#
# PySNMP MIB module HPN-ICF-VRRP-EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HPN-ICF-VRRP-EXT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:42:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
hpnicfCommon, = mibBuilder.importSymbols("HPN-ICF-OID-MIB", "hpnicfCommon")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, Bits, TimeTicks, Gauge32, Unsigned32, Counter64, IpAddress, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, NotificationType, Counter32, ModuleIdentity, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Bits", "TimeTicks", "Gauge32", "Unsigned32", "Counter64", "IpAddress", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "NotificationType", "Counter32", "ModuleIdentity", "Integer32")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
vrrpOperVrId, = mibBuilder.importSymbols("VRRP-MIB", "vrrpOperVrId")
hpnicfVrrpExt = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 24))
if mibBuilder.loadTexts: hpnicfVrrpExt.setLastUpdated('200412090000Z')
if mibBuilder.loadTexts: hpnicfVrrpExt.setOrganization('')
if mibBuilder.loadTexts: hpnicfVrrpExt.setContactInfo('')
if mibBuilder.loadTexts: hpnicfVrrpExt.setDescription('This MIB describes objects used for managing Virtual Router Redundancy Protocol (VRRP) routers.')
hpnicfVrrpExtMibObject = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 24, 1))
hpnicfVrrpExtTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 24, 1, 1), )
if mibBuilder.loadTexts: hpnicfVrrpExtTable.setStatus('current')
if mibBuilder.loadTexts: hpnicfVrrpExtTable.setDescription('Table extends for a VRRP router which consists of a sequence (i.e., one or more conceptual rows) of hpnicfVrrpExtEntry items.')
hpnicfVrrpExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 24, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "VRRP-MIB", "vrrpOperVrId"), (0, "HPN-ICF-VRRP-EXT-MIB", "hpnicfVrrpExtTrackInterface"))
if mibBuilder.loadTexts: hpnicfVrrpExtEntry.setStatus('current')
if mibBuilder.loadTexts: hpnicfVrrpExtEntry.setDescription('An entry in the hpnicfVrrpExtTable containing the status values of a virtual router.')
hpnicfVrrpExtTrackInterface = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 24, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: hpnicfVrrpExtTrackInterface.setStatus('current')
if mibBuilder.loadTexts: hpnicfVrrpExtTrackInterface.setDescription('This value is the ifIndex that identifies which interface the virtual router tracked.')
hpnicfVrrpExtPriorityReduce = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 24, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 255)).clone(10)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfVrrpExtPriorityReduce.setStatus('current')
if mibBuilder.loadTexts: hpnicfVrrpExtPriorityReduce.setDescription('This value identifies how much priority of a virtual router will be reduced/increased when the interface tracked is down/up.')
hpnicfVrrpExtRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 24, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpnicfVrrpExtRowStatus.setStatus('current')
if mibBuilder.loadTexts: hpnicfVrrpExtRowStatus.setDescription('The row status variable, used according to installation and removal conventions for conceptual rows. Setting this object to active(1) or createAndGo(4) results in the addition of the ifIndex tracked by a virtual router. Destroying the entry removes the tracked ifIndex from the virtual router. Other values is not supported now.')
mibBuilder.exportSymbols("HPN-ICF-VRRP-EXT-MIB", hpnicfVrrpExtMibObject=hpnicfVrrpExtMibObject, hpnicfVrrpExtPriorityReduce=hpnicfVrrpExtPriorityReduce, PYSNMP_MODULE_ID=hpnicfVrrpExt, hpnicfVrrpExtTable=hpnicfVrrpExtTable, hpnicfVrrpExtTrackInterface=hpnicfVrrpExtTrackInterface, hpnicfVrrpExtRowStatus=hpnicfVrrpExtRowStatus, hpnicfVrrpExt=hpnicfVrrpExt, hpnicfVrrpExtEntry=hpnicfVrrpExtEntry)
