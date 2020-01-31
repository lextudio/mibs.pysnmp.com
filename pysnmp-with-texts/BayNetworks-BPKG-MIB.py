#
# PySNMP MIB module BayNetworks-BPKG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BayNetworks-BPKG-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:42:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, IpAddress, TimeTicks, ObjectIdentity, iso, NotificationType, ModuleIdentity, MibIdentifier, Gauge32, Counter64, Bits, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "IpAddress", "TimeTicks", "ObjectIdentity", "iso", "NotificationType", "ModuleIdentity", "MibIdentifier", "Gauge32", "Counter64", "Bits", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
wfBacPktGenGroup, = mibBuilder.importSymbols("Wellfleet-COMMON-MIB", "wfBacPktGenGroup")
wfBacPktGenBase = MibIdentifier((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 1))
wfBacPktGenDelete = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfBacPktGenDelete.setStatus('mandatory')
if mibBuilder.loadTexts: wfBacPktGenDelete.setDescription('Create/Delete parameter. Default is created. Users perform a set operation on this object in order to create/delete BAC PktGen.')
wfBacPktGenDisable = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfBacPktGenDisable.setStatus('mandatory')
if mibBuilder.loadTexts: wfBacPktGenDisable.setDescription('Enable/Disable parameter. Default is disabled. Users perform a set operation on this object in order to enable/disable BAC PktGen.')
wfBacPktGenState = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("init", 3), ("notpresent", 4))).clone('notpresent')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfBacPktGenState.setStatus('mandatory')
if mibBuilder.loadTexts: wfBacPktGenState.setDescription('The current state of the entire BAC PktGen: up - BAC PktGen is sending and receiving frames; down - BAC PktGen is disabled; init - BAC PktGen is initializing; notpresent - BAC PktGen is not present. ')
wfBacPktGenTxTabSum = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 1, 4), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfBacPktGenTxTabSum.setStatus('mandatory')
if mibBuilder.loadTexts: wfBacPktGenTxTabSum.setDescription("Total number of TXTAB records added to CXP's.")
wfBacPktGenRxTabSum = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfBacPktGenRxTabSum.setStatus('mandatory')
if mibBuilder.loadTexts: wfBacPktGenRxTabSum.setDescription("Total number of RXTAB records added to CXP's.")
wfBacPktGenCxpTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 2), )
if mibBuilder.loadTexts: wfBacPktGenCxpTable.setStatus('mandatory')
if mibBuilder.loadTexts: wfBacPktGenCxpTable.setDescription('The BAC PktGen CXP table contains relevant information concerning packet generation on each CXP. Note that, the processing of PktGen CXP entries supercedes that of wfBacPktGenCxpGlobal MIB record.')
wfBacPktGenCxpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 2, 1), ).setIndexNames((0, "BayNetworks-BPKG-MIB", "wfBacPktGenCxpId"))
if mibBuilder.loadTexts: wfBacPktGenCxpEntry.setStatus('mandatory')
if mibBuilder.loadTexts: wfBacPktGenCxpEntry.setDescription('Information concerning packet generation on the CXP.')
wfBacPktGenCxpDelete = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfBacPktGenCxpDelete.setStatus('mandatory')
if mibBuilder.loadTexts: wfBacPktGenCxpDelete.setDescription('Create/Delete parameter. Default is created. Users perform a set operation on this object in order to create/delete BAC PktGen CXP table entry.')
wfBacPktGenCxpId = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(6, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfBacPktGenCxpId.setStatus('mandatory')
if mibBuilder.loadTexts: wfBacPktGenCxpId.setDescription('Uniquely identifies the CXP from which test packets are generated. Currently, the CXP is identified by its slot number, which must be between 6 and 8.')
wfBacPktGenStreamMask = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 2, 1, 3), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfBacPktGenStreamMask.setStatus('mandatory')
if mibBuilder.loadTexts: wfBacPktGenStreamMask.setDescription('Bit mask for generating test packets on the CXP streams 1-31. The least significant bit is ignored. The second least significant bit represents stream 1, the next least significant bit represents stream 2, and so forth. The most significant bit represents stream 31.')
wfBacPktGenPktSeed = MibIdentifier((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 3))
wfBacPktGenSeedPkts = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 3, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("seedpackets", 1), ("unseedpackets", 2))).clone('unseedpackets')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfBacPktGenSeedPkts.setStatus('mandatory')
if mibBuilder.loadTexts: wfBacPktGenSeedPkts.setDescription('Seed/Unseed packet parameter. Default is unseedpackets. Users perform a set operation on this object in order to seed/unseed test packets.')
wfBacPktGenPktSeedState = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 3, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("packetseeded", 1), ("packetunseeded", 2), ("operationstarted", 3), ("idle", 4))).clone('idle')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfBacPktGenPktSeedState.setStatus('mandatory')
if mibBuilder.loadTexts: wfBacPktGenPktSeedState.setDescription('Based on the set operation performed on the Seed/Unseed packet parameter, this object reflects the status of the operation. Default is idle. This object goes to the operationstarted state as soon as the BAC PktGen application detects the set operation on the Seed/Unseed parameter. The object remains in this state until the operation is completed, and the appropriate state is registered.')
wfBacPktGenCxpGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 4))
wfBacPktGenCxpGlobalDelete = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 4, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfBacPktGenCxpGlobalDelete.setStatus('mandatory')
if mibBuilder.loadTexts: wfBacPktGenCxpGlobalDelete.setDescription('Create/Delete parameter. Default is created. Users perform a set operation on this object in order to create/delete BAC PktGen CXP Global record. Note that, the PktGen Global record is processed as long as no wfBacPktGenCxpEntry MIB records exist. When one or more wfBacPktGenCxpEntry MIB records are configured, the PktGen CXP Global record is ignored and its processing is disabled.')
wfBacPktGenGlobalStreamMask = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 4, 2), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfBacPktGenGlobalStreamMask.setStatus('mandatory')
if mibBuilder.loadTexts: wfBacPktGenGlobalStreamMask.setDescription('Bit mask for generating test packets on all CXP streams 1-31. The least significant bit is ignored. The second least significant bit represents stream 1, the next least significant bit represents stream 2, and so forth. The most significant bit represents stream 31.')
wfBacPktGenGlobalRecActive = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 4, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("active", 1), ("inactive", 2))).clone('inactive')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfBacPktGenGlobalRecActive.setStatus('mandatory')
if mibBuilder.loadTexts: wfBacPktGenGlobalRecActive.setDescription('Indicates if the processing of this MIB record is active. It is active only when NO wfBacPktGenCxpEntry MIB record is configured.')
wfBacPktGenCctTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 5), )
if mibBuilder.loadTexts: wfBacPktGenCctTable.setStatus('mandatory')
if mibBuilder.loadTexts: wfBacPktGenCctTable.setDescription('The BAC PktGen Circuit table.')
wfBacPktGenCctEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 5, 1), ).setIndexNames((0, "BayNetworks-BPKG-MIB", "wfBacPktGenCctNumber"))
if mibBuilder.loadTexts: wfBacPktGenCctEntry.setStatus('mandatory')
if mibBuilder.loadTexts: wfBacPktGenCctEntry.setDescription('Information concerning a BAC PktGen circuit table entry.')
wfBacPktGenCctDelete = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 5, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("created", 1), ("deleted", 2))).clone('created')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfBacPktGenCctDelete.setStatus('mandatory')
if mibBuilder.loadTexts: wfBacPktGenCctDelete.setDescription('Create/Delete parameter. Default is created. Users perform a set operation on this object in order to create/delete BAC PktGen Circuit table entry.')
wfBacPktGenCctNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 5, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfBacPktGenCctNumber.setStatus('mandatory')
if mibBuilder.loadTexts: wfBacPktGenCctNumber.setDescription('BAC PktGen circuit number.')
wfBacPktGenCctState = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 5, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("init", 3), ("notpresent", 4))).clone('notpresent')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfBacPktGenCctState.setStatus('mandatory')
if mibBuilder.loadTexts: wfBacPktGenCctState.setDescription('The current state of the BAC PktGen circuit: up - The circuit is up; down - The circuit is down; init - The circuit is initializing; notpresent - The circuit is not present. ')
wfBacPktGenCctName = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 5, 1, 4), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfBacPktGenCctName.setStatus('mandatory')
if mibBuilder.loadTexts: wfBacPktGenCctName.setDescription('BAC PktGen circuit name.')
wfBacPktGenPktFile = MibIdentifier((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 6))
wfBacPktGenPktFileAppend = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 6, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfBacPktGenPktFileAppend.setStatus('mandatory')
if mibBuilder.loadTexts: wfBacPktGenPktFileAppend.setDescription('Append disable/enable parameter. Default is to release previous table contents instead of appending to previously processed pkt files. This feature is currently not supported.')
wfBacPktGenPktFileName = MibScalar((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 6, 2), DisplayString()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfBacPktGenPktFileName.setStatus('mandatory')
if mibBuilder.loadTexts: wfBacPktGenPktFileName.setDescription('The user-defined name of the pktfile to process.')
wfBacPktGenPktGrpTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 7), )
if mibBuilder.loadTexts: wfBacPktGenPktGrpTable.setStatus('mandatory')
if mibBuilder.loadTexts: wfBacPktGenPktGrpTable.setDescription('The BAC PktGen packet group table.')
wfBacPktGenPktGrpEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 7, 1), ).setIndexNames((0, "BayNetworks-BPKG-MIB", "wfBacPktGenPktGrpNumber"))
if mibBuilder.loadTexts: wfBacPktGenPktGrpEntry.setStatus('mandatory')
if mibBuilder.loadTexts: wfBacPktGenPktGrpEntry.setDescription('Information concerning a BAC PktGen packet group table entry.')
wfBacPktGenPktGrpNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 7, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfBacPktGenPktGrpNumber.setStatus('mandatory')
if mibBuilder.loadTexts: wfBacPktGenPktGrpNumber.setDescription('Uniquely identifies the packet group number.')
wfBacPktGenPktGrpDelay1 = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 7, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfBacPktGenPktGrpDelay1.setStatus('mandatory')
if mibBuilder.loadTexts: wfBacPktGenPktGrpDelay1.setDescription('Delay parameter 1 for this packet group.')
wfBacPktGenPktGrpDelay2 = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 7, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfBacPktGenPktGrpDelay2.setStatus('mandatory')
if mibBuilder.loadTexts: wfBacPktGenPktGrpDelay2.setDescription('Delay parameter 2 for this packet group.')
wfBacPktGenPktGrpDelay3 = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 7, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfBacPktGenPktGrpDelay3.setStatus('mandatory')
if mibBuilder.loadTexts: wfBacPktGenPktGrpDelay3.setDescription('Delay parameter 3 for this packet group.')
wfBacPktGenPktGrpDelay4 = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 7, 1, 5), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfBacPktGenPktGrpDelay4.setStatus('mandatory')
if mibBuilder.loadTexts: wfBacPktGenPktGrpDelay4.setDescription('Delay parameter 4 for this packet group.')
wfBacPktGenPktGrpCount1 = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 7, 1, 6), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfBacPktGenPktGrpCount1.setStatus('mandatory')
if mibBuilder.loadTexts: wfBacPktGenPktGrpCount1.setDescription('Count parameter 1 for this packet group.')
wfBacPktGenPktGrpCount2 = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 7, 1, 7), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfBacPktGenPktGrpCount2.setStatus('mandatory')
if mibBuilder.loadTexts: wfBacPktGenPktGrpCount2.setDescription('Count parameter 2 for this packet group.')
wfBacPktGenPktGrpCount3 = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 7, 1, 8), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfBacPktGenPktGrpCount3.setStatus('mandatory')
if mibBuilder.loadTexts: wfBacPktGenPktGrpCount3.setDescription('Count parameter 3 for this packet group.')
wfBacPktGenPktGrpCount4 = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 7, 1, 9), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfBacPktGenPktGrpCount4.setStatus('mandatory')
if mibBuilder.loadTexts: wfBacPktGenPktGrpCount4.setDescription('Count parameter 4 for this packet group.')
wfBacPktGenPktSeedSum = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 7, 1, 10), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfBacPktGenPktSeedSum.setStatus('mandatory')
if mibBuilder.loadTexts: wfBacPktGenPktSeedSum.setDescription('Total number of packet seeds that belong to this packet group.')
wfBacPktGenPktGrpCxp = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 7, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfBacPktGenPktGrpCxp.setStatus('mandatory')
if mibBuilder.loadTexts: wfBacPktGenPktGrpCxp.setDescription('The eligible CXP slot number on which this packet group can be thrown.')
wfBacPktGenStrmCtrlTable = MibTable((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 8), )
if mibBuilder.loadTexts: wfBacPktGenStrmCtrlTable.setStatus('mandatory')
if mibBuilder.loadTexts: wfBacPktGenStrmCtrlTable.setDescription('The BAC PktGen stream control table.')
wfBacPktGenStrmCtrlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 8, 1), ).setIndexNames((0, "BayNetworks-BPKG-MIB", "wfBacPktGenStrmNumber"), (0, "BayNetworks-BPKG-MIB", "wfBacPktGenStrmCxp"))
if mibBuilder.loadTexts: wfBacPktGenStrmCtrlEntry.setStatus('mandatory')
if mibBuilder.loadTexts: wfBacPktGenStrmCtrlEntry.setDescription('Information concerning a BAC PktGen stream control table entry.')
wfBacPktGenStrmNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 8, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 31))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfBacPktGenStrmNumber.setStatus('mandatory')
if mibBuilder.loadTexts: wfBacPktGenStrmNumber.setDescription('Uniquely identifies the PktGen stream number on each CXP.')
wfBacPktGenStrmCxp = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 8, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(6, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfBacPktGenStrmCxp.setStatus('mandatory')
if mibBuilder.loadTexts: wfBacPktGenStrmCxp.setDescription('Uniquely identifies the CXP.')
wfBacPktGenStrmState = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 8, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 4))).clone(namedValues=NamedValues(("pktgen", 1), ("killed", 2), ("notpresent", 4))).clone('notpresent')).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfBacPktGenStrmState.setStatus('mandatory')
if mibBuilder.loadTexts: wfBacPktGenStrmState.setDescription('The current state of this PktGen stream: pktgen - Stream is transmitting test packets; killed - Stream is being killed; notpresent - Stream is not present. ')
wfBacPktGenSetStrmPktGrp = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 8, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: wfBacPktGenSetStrmPktGrp.setStatus('mandatory')
if mibBuilder.loadTexts: wfBacPktGenSetStrmPktGrp.setDescription('Set the packet group to be thrown by this PktGen stream. ')
wfBacPktGenStrmPktGrp = MibTableColumn((1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 4, 1, 8, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: wfBacPktGenStrmPktGrp.setStatus('mandatory')
if mibBuilder.loadTexts: wfBacPktGenStrmPktGrp.setDescription('The packet group which will be thrown by this PktGen stream. ')
mibBuilder.exportSymbols("BayNetworks-BPKG-MIB", wfBacPktGenPktFileAppend=wfBacPktGenPktFileAppend, wfBacPktGenPktGrpTable=wfBacPktGenPktGrpTable, wfBacPktGenPktGrpNumber=wfBacPktGenPktGrpNumber, wfBacPktGenPktGrpDelay4=wfBacPktGenPktGrpDelay4, wfBacPktGenState=wfBacPktGenState, wfBacPktGenPktGrpCxp=wfBacPktGenPktGrpCxp, wfBacPktGenCxpTable=wfBacPktGenCxpTable, wfBacPktGenCctDelete=wfBacPktGenCctDelete, wfBacPktGenPktGrpCount1=wfBacPktGenPktGrpCount1, wfBacPktGenStrmState=wfBacPktGenStrmState, wfBacPktGenPktGrpCount3=wfBacPktGenPktGrpCount3, wfBacPktGenRxTabSum=wfBacPktGenRxTabSum, wfBacPktGenBase=wfBacPktGenBase, wfBacPktGenStrmCtrlEntry=wfBacPktGenStrmCtrlEntry, wfBacPktGenCxpDelete=wfBacPktGenCxpDelete, wfBacPktGenCctNumber=wfBacPktGenCctNumber, wfBacPktGenCxpGlobalDelete=wfBacPktGenCxpGlobalDelete, wfBacPktGenCctEntry=wfBacPktGenCctEntry, wfBacPktGenCxpGlobal=wfBacPktGenCxpGlobal, wfBacPktGenTxTabSum=wfBacPktGenTxTabSum, wfBacPktGenStrmCxp=wfBacPktGenStrmCxp, wfBacPktGenCxpEntry=wfBacPktGenCxpEntry, wfBacPktGenPktGrpDelay2=wfBacPktGenPktGrpDelay2, wfBacPktGenPktSeedState=wfBacPktGenPktSeedState, wfBacPktGenCctName=wfBacPktGenCctName, wfBacPktGenPktFile=wfBacPktGenPktFile, wfBacPktGenPktSeed=wfBacPktGenPktSeed, wfBacPktGenPktFileName=wfBacPktGenPktFileName, wfBacPktGenPktGrpCount4=wfBacPktGenPktGrpCount4, wfBacPktGenGlobalStreamMask=wfBacPktGenGlobalStreamMask, wfBacPktGenCctTable=wfBacPktGenCctTable, wfBacPktGenPktGrpDelay1=wfBacPktGenPktGrpDelay1, wfBacPktGenCxpId=wfBacPktGenCxpId, wfBacPktGenPktGrpCount2=wfBacPktGenPktGrpCount2, wfBacPktGenPktGrpEntry=wfBacPktGenPktGrpEntry, wfBacPktGenStrmCtrlTable=wfBacPktGenStrmCtrlTable, wfBacPktGenPktGrpDelay3=wfBacPktGenPktGrpDelay3, wfBacPktGenPktSeedSum=wfBacPktGenPktSeedSum, wfBacPktGenStrmPktGrp=wfBacPktGenStrmPktGrp, wfBacPktGenDelete=wfBacPktGenDelete, wfBacPktGenSeedPkts=wfBacPktGenSeedPkts, wfBacPktGenSetStrmPktGrp=wfBacPktGenSetStrmPktGrp, wfBacPktGenCctState=wfBacPktGenCctState, wfBacPktGenGlobalRecActive=wfBacPktGenGlobalRecActive, wfBacPktGenStreamMask=wfBacPktGenStreamMask, wfBacPktGenDisable=wfBacPktGenDisable, wfBacPktGenStrmNumber=wfBacPktGenStrmNumber)