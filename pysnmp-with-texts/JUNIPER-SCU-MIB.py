#
# PySNMP MIB module JUNIPER-SCU-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/JUNIPER-SCU-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:01:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
jnxMibs, = mibBuilder.importSymbols("JUNIPER-SMI", "jnxMibs")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, Counter32, NotificationType, Gauge32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Bits, Counter64, ModuleIdentity, ObjectIdentity, IpAddress, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter32", "NotificationType", "Gauge32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Bits", "Counter64", "ModuleIdentity", "ObjectIdentity", "IpAddress", "Unsigned32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
jnxScu = ModuleIdentity((1, 3, 6, 1, 4, 1, 2636, 3, 16))
jnxScu.setRevisions(('2002-02-25 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: jnxScu.setRevisionsDescriptions(('Initial revision',))
if mibBuilder.loadTexts: jnxScu.setLastUpdated('200307182153Z')
if mibBuilder.loadTexts: jnxScu.setOrganization('Juniper Networks, Inc.')
if mibBuilder.loadTexts: jnxScu.setContactInfo('Juniper Technical Assistance Center Juniper Networks, Inc. 1194 N. Mathilda Avenue Sunnyvale, CA 94089 E-mail: support@juniper.net')
if mibBuilder.loadTexts: jnxScu.setDescription("This is Juniper Networks' enterprise-specific MIB for Source Class Usage (SCU)")
jnxScuStats = MibIdentifier((1, 3, 6, 1, 4, 1, 2636, 3, 16, 1))
jnxScuStatsTable = MibTable((1, 3, 6, 1, 4, 1, 2636, 3, 16, 1, 1), )
if mibBuilder.loadTexts: jnxScuStatsTable.setStatus('current')
if mibBuilder.loadTexts: jnxScuStatsTable.setDescription('A list of SCUs entries.')
jnxScuStatsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 2636, 3, 16, 1, 1, 1), ).setIndexNames((0, "JUNIPER-SCU-MIB", "jnxScuStatsDstIfIndex"), (0, "JUNIPER-SCU-MIB", "jnxScuStatsAddrFamily"), (0, "JUNIPER-SCU-MIB", "jnxScuStatsClassName"))
if mibBuilder.loadTexts: jnxScuStatsEntry.setStatus('current')
if mibBuilder.loadTexts: jnxScuStatsEntry.setDescription('An entry of SCUs table.')
jnxScuStatsDstIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 16, 1, 1, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: jnxScuStatsDstIfIndex.setStatus('current')
if mibBuilder.loadTexts: jnxScuStatsDstIfIndex.setDescription('The destination interface index. This is the egress interface of traffic that is counted by this table entry.')
jnxScuStatsAddrFamily = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 16, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("ipv4", 1), ("ipv6", 2))))
if mibBuilder.loadTexts: jnxScuStatsAddrFamily.setStatus('current')
if mibBuilder.loadTexts: jnxScuStatsAddrFamily.setDescription("The address family of this entry's traffic.")
jnxScuStatsClassName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 16, 1, 1, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 112)))
if mibBuilder.loadTexts: jnxScuStatsClassName.setStatus('current')
if mibBuilder.loadTexts: jnxScuStatsClassName.setDescription('The name of the source class. All traffic counted in this table entry satisfies the requirements defined by this source class.')
jnxScuStatsPackets = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 16, 1, 1, 1, 4), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxScuStatsPackets.setStatus('current')
if mibBuilder.loadTexts: jnxScuStatsPackets.setDescription('The number of packets sent out of jnxScuStatsDstIfIndex that match the source class (jnxScuStatsClassName) and match the address type (jnxScuStatsAddrFamily) defined for this table entry.')
jnxScuStatsBytes = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 16, 1, 1, 1, 5), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxScuStatsBytes.setStatus('current')
if mibBuilder.loadTexts: jnxScuStatsBytes.setDescription('The number of bytes sent out of jnxScuStatsDstIfIndex that match the source class (jnxScuStatsClassName) and match the address type (jnxScuStatsAddrFamily) defined for this table entry.')
jnxScuStatsClName = MibTableColumn((1, 3, 6, 1, 4, 1, 2636, 3, 16, 1, 1, 1, 6), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 112))).setMaxAccess("readonly")
if mibBuilder.loadTexts: jnxScuStatsClName.setStatus('current')
if mibBuilder.loadTexts: jnxScuStatsClName.setDescription("The name of the source class. This object is a duplicate of jnxScuStatsClassName and is included to satisfy those NM applications that can't extract the class name from the instance portion of the OID.")
mibBuilder.exportSymbols("JUNIPER-SCU-MIB", jnxScuStatsPackets=jnxScuStatsPackets, jnxScuStatsEntry=jnxScuStatsEntry, jnxScuStatsClassName=jnxScuStatsClassName, jnxScuStatsBytes=jnxScuStatsBytes, jnxScuStatsAddrFamily=jnxScuStatsAddrFamily, jnxScu=jnxScu, jnxScuStatsDstIfIndex=jnxScuStatsDstIfIndex, jnxScuStats=jnxScuStats, jnxScuStatsTable=jnxScuStatsTable, PYSNMP_MODULE_ID=jnxScu, jnxScuStatsClName=jnxScuStatsClName)