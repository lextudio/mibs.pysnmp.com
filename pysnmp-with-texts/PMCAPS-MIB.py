#
# PySNMP MIB module PMCAPS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PMCAPS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:41:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
rmon, = mibBuilder.importSymbols("RMON-MIB", "rmon")
protocolDirectoryGroup, protocolDirLocalIndex = mibBuilder.importSymbols("RMON2-MIB", "protocolDirectoryGroup", "protocolDirLocalIndex")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Unsigned32, NotificationType, TimeTicks, Counter32, Bits, IpAddress, Counter64, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, MibIdentifier, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Unsigned32", "NotificationType", "TimeTicks", "Counter32", "Bits", "IpAddress", "Counter64", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "MibIdentifier", "Integer32")
RowPointer, DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowPointer", "DisplayString", "TruthValue", "TextualConvention")
pmCapsMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 16, 25))
pmCapsMIB.setRevisions(('2000-07-14 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: pmCapsMIB.setRevisionsDescriptions(('Initial Version of the Performance Measurement Capabilities MIB.',))
if mibBuilder.loadTexts: pmCapsMIB.setLastUpdated('200007140000Z')
if mibBuilder.loadTexts: pmCapsMIB.setOrganization('IETF RMONMIB WG')
if mibBuilder.loadTexts: pmCapsMIB.setContactInfo(' Andy Bierman Cisco Systems, Inc. RMONMIB WG Chair and PMCAPS MIB Editor Postal: 170 West Tasman Drive San Jose, CA USA 95134 Tel: +1 408 527-3711 E-mail: abierman@cisco.com Send comments to <rmonmib@ietf.org> Mailing list subscription information: http://www.ietf.org/mailman/listinfo/rmonmib ')
if mibBuilder.loadTexts: pmCapsMIB.setDescription('The MIB module for representing Performance Measurement Capabilities.')
pmCapsMIBObjects = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 25, 1))
pmCaps = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 25, 1, 1))
pmMetrics = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 25, 1, 2))
pmMetricTable = MibTable((1, 3, 6, 1, 2, 1, 16, 25, 1, 1, 1), )
if mibBuilder.loadTexts: pmMetricTable.setStatus('current')
if mibBuilder.loadTexts: pmMetricTable.setDescription('This table contains one row per PM Metric supported by this agent, and should be populated during system initialization.')
pmMetricEntry = MibTableRow((1, 3, 6, 1, 2, 1, 16, 25, 1, 1, 1, 1), ).setIndexNames((0, "PMCAPS-MIB", "pmMetricID"))
if mibBuilder.loadTexts: pmMetricEntry.setStatus('current')
if mibBuilder.loadTexts: pmMetricEntry.setDescription('Information about a particular PM Metric.')
pmMetricID = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 25, 1, 1, 1, 1, 1), ObjectIdentifier())
if mibBuilder.loadTexts: pmMetricID.setStatus('current')
if mibBuilder.loadTexts: pmMetricID.setDescription('The index for this entry. This object identifies the standard or vendor-specific registration OBJECT IDENTIFER defined for a particular PM metric.')
pmMetricType = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 25, 1, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("other", 1), ("connectMetric", 2), ("delayMetric", 3), ("lossMetric", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmMetricType.setStatus('current')
if mibBuilder.loadTexts: pmMetricType.setDescription("The basic type of metric indicated by this entry. The value 'other(1)' indicates that this metric cannot be characterized by any of the remaining enumerations specified for this object. The value 'connectMetric(2)' indicates that this metric measures connectivity characteristics. The value 'delayMetric(3)' indicates that this metric measures delay characteristics. The value 'lossMetric(4)' indicates that this metric measures loss characteristics.")
pmMetricDirType = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 25, 1, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("oneWay", 1), ("twoWay", 2), ("multiWay", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmMetricDirType.setStatus('current')
if mibBuilder.loadTexts: pmMetricDirType.setDescription("The directional characteristics of the this metric. The value 'oneWay(1)' indicates that this metric is measured with some sort of uni-directional test. The value 'twoWay(2)' indicates that this metric is measured with some sort of bi-directional test. The value 'multiWay(3)' indicates that this metric is measured with some combination of uni-directional and/or bi- directional tests.")
pmMetricName = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 25, 1, 1, 1, 1, 4), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmMetricName.setStatus('current')
if mibBuilder.loadTexts: pmMetricName.setDescription('The textual name of this metric.')
pmMetricReference = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 25, 1, 1, 1, 1, 5), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmMetricReference.setStatus('current')
if mibBuilder.loadTexts: pmMetricReference.setDescription("This object contains a reference to the document which defines this metric. If this document is available online via electronic download, then a URL should be specified in this object. For example, if this pmMetricEntry identified the IPPM metric 'Type-P-Round-Trip-Delay', then this object should contain the value 'http://www.ietf.org/rfc/rfc2681.txt'.")
pmStudyClassTable = MibTable((1, 3, 6, 1, 2, 1, 16, 25, 1, 1, 2), )
if mibBuilder.loadTexts: pmStudyClassTable.setStatus('current')
if mibBuilder.loadTexts: pmStudyClassTable.setDescription('This table contains one row per PM Study Class supported by this APM/TPM Device, and should be populated during system initialization.')
pmStudyClassEntry = MibTableRow((1, 3, 6, 1, 2, 1, 16, 25, 1, 1, 2, 1), ).setIndexNames((0, "PMCAPS-MIB", "pmStudyClassID"))
if mibBuilder.loadTexts: pmStudyClassEntry.setStatus('current')
if mibBuilder.loadTexts: pmStudyClassEntry.setDescription('Information about a particular PM Study Class.')
pmStudyClassID = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 25, 1, 1, 2, 1, 1), ObjectIdentifier())
if mibBuilder.loadTexts: pmStudyClassID.setStatus('current')
if mibBuilder.loadTexts: pmStudyClassID.setDescription('The index for this entry. This object identifier should specify the standard or vendor-specific registration OID for this PM Study Class.')
pmStudyClassMeasLoc = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 25, 1, 1, 2, 1, 2), Bits().clone(namedValues=NamedValues(("pmClient", 0), ("pmNetwork", 1), ("pmServer", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmStudyClassMeasLoc.setStatus('current')
if mibBuilder.loadTexts: pmStudyClassMeasLoc.setDescription("The measurement location characteristics of the PM Data collection methodologies employed by this PM Study Class. If this PM Study class utilizes some sort of measurement technology located on the host machine being monitored, then the 'pmClient' BIT will be set. Note that this bit should only be set if any PM technology is installed on the client, in addition to the 'normal' protocol operations supported by that machine. If this PM Study class utilizes some sort of measurement technology located on one or more networking devices (e.g., routers, switches, RMON probes), then the 'pmNetwork' BIT will be set. If this PM Study class utilizes some sort of measurement technology located on the application server being monitored, then the 'pmServer' BIT will be set. Note that this bit should only be set if any PM technology is installed on the server, in addition to the 'normal' protocol operations supported by that machine.")
pmStudyClassMeasType = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 25, 1, 1, 2, 1, 3), Bits().clone(namedValues=NamedValues(("pmPassive", 0), ("pmActive", 1), ("pmBuiltin", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmStudyClassMeasType.setStatus('current')
if mibBuilder.loadTexts: pmStudyClassMeasType.setDescription("The type(s) of collection methodologies employed by this PM Study Class. If this PM Study class utilizes some sort of passive monitoring technology, (i.e., UI operations and/or protocol transactions of real users are measured) the 'pmPassive' BIT will be set. If this PM Study class utilizes some sort of active monitoring technology, (i.e., protocol transactions generated for the purpose of obtaining PM Data) the 'pmPassive' BIT will be set. If this PM Study class utilizes some sort of built-in monitoring technology, (i.e., UI operations and/or protocol transactions of real users are somehow altered to provide PM Data) the 'pmBuiltin' BIT will be set.")
pmStudyClassCollectPts = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 25, 1, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmStudyClassCollectPts.setStatus('current')
if mibBuilder.loadTexts: pmStudyClassCollectPts.setDescription('The number of PM Collection Points utilized in this PM Study Class. If this is a variable quantity, then this object should contain the minimum number needed for this PM Study Class to function.')
pmStudyClassCollectCaps = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 25, 1, 1, 2, 1, 5), Bits().clone(namedValues=NamedValues(("pmCollectTrans", 0), ("pmCollectApp", 1), ("pmCollectFlow", 2), ("pmCollectNonNet", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmStudyClassCollectCaps.setStatus('current')
if mibBuilder.loadTexts: pmStudyClassCollectCaps.setDescription("This object identifies some generic characteristics of the collection methodologies employed by this PM Study Class. If this PM Study class utilizes some sort of transport layer PM Data collection technology, then the 'pmCollectTrans' BIT will be set. If this PM Study class utilizes some sort of application layer PM Data collection technology, then the 'pmCollectApp' BIT will be set. If this PM Study class utilizes PM Data collection technology based on monitoring of some sort of network flow summary information, then the 'pmCollectFlow' BIT will be set. If this PM Study class utilizes some sort of PM Data collection technology based on monitoring of non-network events, such as UI monitoring of window events, then the 'pmCollectNonNet' BIT will be set.")
pmStudyClassOutputCaps = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 25, 1, 1, 2, 1, 6), Bits().clone(namedValues=NamedValues(("pmOutputOther", 0), ("pmOutputApmDist", 1), ("pmOutputApmStat", 2), ("pmOutputApmHist", 3), ("pmOutputApmFlow", 4), ("pmOutputApmExcept", 5), ("pmOutputApmProp", 6), ("pmOutputTpmDist", 7), ("pmOutputTpmStat", 8), ("pmOutputTpmHist", 9), ("pmOutputTpmExcept", 10), ("pmOutputTpmProp", 11)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmStudyClassOutputCaps.setStatus('current')
if mibBuilder.loadTexts: pmStudyClassOutputCaps.setDescription("The type(s) of APM and/or TPM Reports that this PM Study Class can provide. [ed. - this list will change as the APM and TPM MIBs are finalized.] If this PM Study class can generate standard reports not described by any of the provided BITS here, then the 'pmOutputOther' BIT will be set. If this PM Study class can generate distribution-oriented reports for application layer protocols, then the 'pmOutputApmDist' BIT will be set. If this PM Study class can generate statistics-oriented reports for application layer protocols, then the 'pmOutputApmStat' BIT will be set. If this PM Study class can generate historical analysis oriented reports for application layer protocols, then the 'pmOutputApmHist' BIT will be set. If this PM Study class can generate flow decomposition analysis oriented reports for application layer protocols, then the 'pmOutputApmFlow' BIT will be set. If this PM Study class can generate profile exception oriented reports for application layer protocols, then the 'pmOutputApmExcept' BIT will be set. If this PM Study class can generate vendor-specific proprietary reports for application layer protocols, in addition to standard reports, then the 'pmOutputApmProp' BIT will be set. If this PM Study class can generate distribution-oriented reports for transport layer protocols, then the 'pmOutputTpmDist' BIT will be set. If this PM Study class can generate statistics-oriented reports for transport layer protocols, then the 'pmOutputTpmStat' BIT will be set. If this PM Study class can generate historical analysis oriented reports for transport layer protocols, then the 'pmOutputTpmHist' BIT will be set. If this PM Study class can generate flow decomposition analysis oriented reports for transport layer protocols, then the 'pmOutputTpmFlow' BIT will be set. If this PM Study class can generate profile exception oriented reports for transport layer protocols, then the 'pmOutputTpmExcept' BIT will be set. If this PM Study class can generate vendor-specific proprietary reports for transport layer protocols, in addition to standard reports, then the 'pmOutputTpmProp' BIT will be set.")
pmStudyClassCtlTablePtr = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 25, 1, 1, 2, 1, 7), RowPointer()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmStudyClassCtlTablePtr.setStatus('current')
if mibBuilder.loadTexts: pmStudyClassCtlTablePtr.setDescription('This object identifies a specific MIB table that can be used to configure detailed aspects of the collection or report processing functions for this PM Study Class. This object just identifies a particular row in the MIB table to use, not any particular agent which implements this MIB table. This agent may or may not contain an implementation of the specified MIB, and/or the specified MIB may not be accessible in the same views as the this MIB. If no appropriate row in a MIB table can be identified, then the value { 0 0 } is returned.')
pmStudyMetricTable = MibTable((1, 3, 6, 1, 2, 1, 16, 25, 1, 1, 3), )
if mibBuilder.loadTexts: pmStudyMetricTable.setStatus('current')
if mibBuilder.loadTexts: pmStudyMetricTable.setDescription('This table contains one row for each metric supported by the specified PM Study Class, and should be populated during system initialization.')
pmStudyMetricEntry = MibTableRow((1, 3, 6, 1, 2, 1, 16, 25, 1, 1, 3, 1), ).setIndexNames((0, "PMCAPS-MIB", "pmStudyClassID"))
if mibBuilder.loadTexts: pmStudyMetricEntry.setStatus('current')
if mibBuilder.loadTexts: pmStudyMetricEntry.setDescription('Metrics information related to a particular PM Study Class. The pmStudyClassID value in the index identifies the pmStudyClassEntry with the same index value.')
pmStudyMetricID = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 25, 1, 1, 3, 1, 1), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmStudyMetricID.setStatus('current')
if mibBuilder.loadTexts: pmStudyMetricID.setDescription('This object identifies the PM Metric associated with this PM Study, and contains the same value as the pmMetricID index for that pmMetricEntry.')
pmStudyProtocolTable = MibTable((1, 3, 6, 1, 2, 1, 16, 25, 1, 1, 4), )
if mibBuilder.loadTexts: pmStudyProtocolTable.setStatus('current')
if mibBuilder.loadTexts: pmStudyProtocolTable.setDescription('This table contains one row for each protocol supported by the specified PM Study Class, and should be populated during system initialization. This is an indication of the protocols the indicated PM Study Class is capable of measuring. The actual protocols present in a given APM or TPM Report may be a subset of the protocols identified in this table. This table contain entries which reference any protocol in the protocolDirTable. If the index of this entry identifies an internal node in the protocolDirTable, then the pmStudyProtocolIsSubtree object is relevant.')
pmStudyProtocolEntry = MibTableRow((1, 3, 6, 1, 2, 1, 16, 25, 1, 1, 4, 1), ).setIndexNames((0, "PMCAPS-MIB", "pmStudyClassID"), (0, "RMON2-MIB", "protocolDirLocalIndex"))
if mibBuilder.loadTexts: pmStudyProtocolEntry.setStatus('current')
if mibBuilder.loadTexts: pmStudyProtocolEntry.setDescription('Protocol information about a particular PM Study Class. The pmStudyClassID value in the index identifies the pmStudyClassEntry with the same index value, associated with the list of protocols in this table. The protocolDirLocalIndex value identifies the protocolDirEntry which contains the same value in the protocolDirLocalIndex object.')
pmStudyProtocolIsSubtree = MibTableColumn((1, 3, 6, 1, 2, 1, 16, 25, 1, 1, 4, 1, 1), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: pmStudyProtocolIsSubtree.setStatus('current')
if mibBuilder.loadTexts: pmStudyProtocolIsSubtree.setDescription("This object indicates whether or not this entry identifies one node or an entire subtree of the protocolDirTable. If set to 'true(1)' then the specified protocolDirEntry, and all its children, are supported by the specified PM Study Class. If set to 'false(2)', then the specified protocolDirEntry identified by this entry is supported by the PM Study Class.")
pmAppAvailMetric = ObjectIdentity((1, 3, 6, 1, 2, 1, 16, 25, 1, 2, 1))
if mibBuilder.loadTexts: pmAppAvailMetric.setStatus('current')
if mibBuilder.loadTexts: pmAppAvailMetric.setDescription("Metric Name: Type-P-APM-Availability Metric Definition: This metric characterizes the availability of a network service by measuring the percentage of successful transactions the network service delivers over a given time interval. This metric is calculated by first measuring the IPPM metric 'Type-P-Interval-Bidirectional-Connectivity' for the interval starting at the instant 'Src' initiates a transaction of Type-P with the 'Dst' host, and ending at the instant the last packet of the transaction has been received. In addition to successful connectivity over this interval, the particular application request must also succeed, for a transaction to be considered successful. If either condition is false, then that transaction is considered to be unsuccessful. The derived metric is defined as the total number of successful transactions between Src and Dst, divided by the total number of transaction attempts between Src and Dst, during the time interval dT. Metric Parameters: Src, the network address of a host Dst, the network address of a host dT, a time interval Metric Units: Percentage Mapping of Type P: Type P refers to an application protocol encapsulation, identified by a specific protocolDirEntry. Metric Type: connectMetric(1) Metric Dir Type: twoWay(2)")
if mibBuilder.loadTexts: pmAppAvailMetric.setReference('IPPM Metrics for Measuring Connectivity, RFC 2678 [RFC2678], Section 5, September 1999.')
pmAppTransRespMetric = ObjectIdentity((1, 3, 6, 1, 2, 1, 16, 25, 1, 2, 2))
if mibBuilder.loadTexts: pmAppTransRespMetric.setStatus('current')
if mibBuilder.loadTexts: pmAppTransRespMetric.setDescription("Metric Name: Type-P-APM-Transaction-Responsiveness Metric Definition: This metric characterizes the speed at which a transaction-oriented network application delivers a requested service, by measuring the speed of individual application transactions. This metric is calculated by utilizing a variation of the IPPM metric 'Type-P-Round-trip-Delay'. The total transaction time (dT) is determined by summing all the packet transactions of Type-P between the Src and Dst hosts. The bi-directional flight times are measured (as specified by the IPPM metric definition), but the server response time for each request is included in the measurement. The derived metric is defined as the total number of tenths of seconds for the transaction between Src and Dst to complete. Metric Parameters: Src, the network address of a host Dst, the network address of a host dT, a time interval Metric Units: Tenths of seconds Mapping of Type P: Type P refers to an application protocol encapsulation, identified by a specific protocolDirEntry, which is characterized as a transaction-oriented protocol. Metric Type: delayMetric(2) Metric Dir Type: twoWay(2)")
if mibBuilder.loadTexts: pmAppTransRespMetric.setReference('Round-trip for Delay Metric for IPPM, RFC 2681 [RFC2681], Section 2, September 1999.')
pmAppTputRespMetric = ObjectIdentity((1, 3, 6, 1, 2, 1, 16, 25, 1, 2, 3))
if mibBuilder.loadTexts: pmAppTputRespMetric.setStatus('current')
if mibBuilder.loadTexts: pmAppTputRespMetric.setDescription("Metric Name: Type-P-APM-Throughput-Responsiveness Metric Definition: This metric characterizes the speed at which a throughput-oriented network application delivers a requested service, by measuring the transfer rate of individual application transactions. This metric is calculated by ... [rest of para is TBD] The derived metric is normalized and inverted, into units of 'seconds per terabit'. For transactions up to one terabit in size, it is defined as the total number of seconds it would take for the transaction between Src and Dst to complete, if the transaction size included one terabit of data. For transactions over one terabit in size, it is defined as the average number of seconds for the transaction between Src and Dst to complete, for each terabit of data. E.g., a transfer rate of 2Kbps equals 500,000,000 and a transfer rate of 1Gbps = 1000. Metric Parameters: Src, the network address of a host Dst, the network address of a host dT, a time interval B, a number of terabits Metric Units: Seconds Per Terabit Mapping of Type P: Type P refers to an application protocol encapsulation, identified by a specific protocolDirEntry, which is characterized as a throughput-oriented protocol. Metric Type: delayMetric(2) Metric Dir Type: twoWay(2)")
if mibBuilder.loadTexts: pmAppTputRespMetric.setReference('Round-trip for Delay Metric for IPPM, RFC 2681 [RFC2681], Section 2, September 1999.')
pmAppStreamRespMetric = ObjectIdentity((1, 3, 6, 1, 2, 1, 16, 25, 1, 2, 4))
if mibBuilder.loadTexts: pmAppStreamRespMetric.setStatus('current')
if mibBuilder.loadTexts: pmAppStreamRespMetric.setDescription("Metric Name: Type-P-APM-Stream-Responsiveness Metric Definition: This metric characterizes the 'quality' at which a streaming-oriented network application delivers a requested service, by measuring the percentage of time that the service is degraded or interrupted to the total time to deliver the service. [Rest of definition TBD] Metric Parameters: Src, the network address of a host Dst, the network address of a host Metric Units: [TBD] Mapping of Type P: Type P refers to an application protocol encapsulation, identified by a specific protocolDirEntry, which is characterized as a streaming-oriented protocol. Metric Type: delayMetric(2) Metric Dir Type: twoWay(2)")
if mibBuilder.loadTexts: pmAppStreamRespMetric.setReference('Round-trip for Delay Metric for IPPM, RFC 2681 [RFC2681], Section 2, September 1999.')
pmCapsNotifications = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 25, 2))
pmCapsConformance = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 25, 3))
pmCapsCompliances = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 25, 3, 1))
pmCapsGroups = MibIdentifier((1, 3, 6, 1, 2, 1, 16, 25, 3, 2))
pmCapsCompliance = ModuleCompliance((1, 3, 6, 1, 2, 1, 16, 25, 3, 1, 1)).setObjects(("PMCAPS-MIB", "protocolDirectoryGroup"), ("PMCAPS-MIB", "pmCapsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pmCapsCompliance = pmCapsCompliance.setStatus('current')
if mibBuilder.loadTexts: pmCapsCompliance.setDescription('The compliance statement for SNMP entities which implement version 1 of the APM Capabilities MIB.')
pmCapsGroup = ObjectGroup((1, 3, 6, 1, 2, 1, 16, 25, 3, 2, 1)).setObjects(("PMCAPS-MIB", "pmMetricType"), ("PMCAPS-MIB", "pmMetricDirType"), ("PMCAPS-MIB", "pmMetricName"), ("PMCAPS-MIB", "pmMetricReference"), ("PMCAPS-MIB", "pmStudyClassMeasLoc"), ("PMCAPS-MIB", "pmStudyClassMeasType"), ("PMCAPS-MIB", "pmStudyClassCollectPts"), ("PMCAPS-MIB", "pmStudyClassCollectCaps"), ("PMCAPS-MIB", "pmStudyClassOutputCaps"), ("PMCAPS-MIB", "pmStudyClassCtlTablePtr"), ("PMCAPS-MIB", "pmStudyMetricID"), ("PMCAPS-MIB", "pmStudyProtocolIsSubtree"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pmCapsGroup = pmCapsGroup.setStatus('current')
if mibBuilder.loadTexts: pmCapsGroup.setDescription('The collection of objects which are used to represent application performance measurement capabilities, for which a single agent provides management information.')
mibBuilder.exportSymbols("PMCAPS-MIB", pmStudyClassID=pmStudyClassID, pmCapsNotifications=pmCapsNotifications, pmCapsMIB=pmCapsMIB, pmStudyProtocolIsSubtree=pmStudyProtocolIsSubtree, pmMetricEntry=pmMetricEntry, pmStudyProtocolTable=pmStudyProtocolTable, pmStudyClassOutputCaps=pmStudyClassOutputCaps, pmMetricTable=pmMetricTable, pmMetricID=pmMetricID, pmMetricDirType=pmMetricDirType, pmStudyMetricID=pmStudyMetricID, pmStudyProtocolEntry=pmStudyProtocolEntry, pmMetricName=pmMetricName, pmCapsMIBObjects=pmCapsMIBObjects, pmStudyMetricTable=pmStudyMetricTable, pmCapsGroups=pmCapsGroups, pmCapsConformance=pmCapsConformance, pmAppTputRespMetric=pmAppTputRespMetric, pmAppStreamRespMetric=pmAppStreamRespMetric, pmAppAvailMetric=pmAppAvailMetric, pmStudyMetricEntry=pmStudyMetricEntry, pmCapsCompliance=pmCapsCompliance, pmCapsGroup=pmCapsGroup, pmMetricType=pmMetricType, pmCaps=pmCaps, pmMetrics=pmMetrics, pmStudyClassCtlTablePtr=pmStudyClassCtlTablePtr, pmAppTransRespMetric=pmAppTransRespMetric, pmMetricReference=pmMetricReference, pmStudyClassMeasType=pmStudyClassMeasType, pmStudyClassTable=pmStudyClassTable, PYSNMP_MODULE_ID=pmCapsMIB, pmStudyClassCollectCaps=pmStudyClassCollectCaps, pmCapsCompliances=pmCapsCompliances, pmStudyClassEntry=pmStudyClassEntry, pmStudyClassCollectPts=pmStudyClassCollectPts, pmStudyClassMeasLoc=pmStudyClassMeasLoc)