# SNMP MIB module (IPFIX-COLLECTOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IPFIX-COLLECTOR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:10:48 2024
# On host MacBook-Pro.local platform Darwin version 24.0.0 by user lextm
# Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint,
 ConstraintsUnion) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint",
    "ConstraintsUnion")

# Import SMI symbols from the MIBs this MIB depends on

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso,
 mib_2) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso",
    "mib-2")

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ipfixMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 999)
)
ipfixMIB.setRevisions(
        ("2006-10-20 16:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IpfixExporter_ObjectIdentity = ObjectIdentity
ipfixExporter = _IpfixExporter_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 999, 1)
)
_IpfixCollector_ObjectIdentity = ObjectIdentity
ipfixCollector = _IpfixCollector_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 999, 2)
)
_IpfixCollectorObjects_ObjectIdentity = ObjectIdentity
ipfixCollectorObjects = _IpfixCollectorObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 999, 2, 1)
)
_IpfixReceiving_ObjectIdentity = ObjectIdentity
ipfixReceiving = _IpfixReceiving_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 999, 2, 1, 1)
)
_IpfixExporterTable_Object = MibTable
ipfixExporterTable = _IpfixExporterTable_Object(
    (1, 3, 6, 1, 2, 1, 999, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ipfixExporterTable.setStatus("current")
_IpfixExporterEntry_Object = MibTableRow
ipfixExporterEntry = _IpfixExporterEntry_Object(
    (1, 3, 6, 1, 2, 1, 999, 2, 1, 1, 1, 1)
)
ipfixExporterEntry.setIndexNames(
    (0, "IPFIX-COLLECTOR-MIB", "ipfixExporterIndex"),
)
if mibBuilder.loadTexts:
    ipfixExporterEntry.setStatus("current")


class _IpfixExporterIndex_Type(Integer32):
    """Custom type ipfixExporterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IpfixExporterIndex_Type.__name__ = "Integer32"
_IpfixExporterIndex_Object = MibTableColumn
ipfixExporterIndex = _IpfixExporterIndex_Object(
    (1, 3, 6, 1, 2, 1, 999, 2, 1, 1, 1, 1, 1),
    _IpfixExporterIndex_Type()
)
ipfixExporterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipfixExporterIndex.setStatus("current")
_IpfixExporterIpAddressType_Type = InetAddressType
_IpfixExporterIpAddressType_Object = MibTableColumn
ipfixExporterIpAddressType = _IpfixExporterIpAddressType_Object(
    (1, 3, 6, 1, 2, 1, 999, 2, 1, 1, 1, 1, 2),
    _IpfixExporterIpAddressType_Type()
)
ipfixExporterIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixExporterIpAddressType.setStatus("current")
_IpfixExporterIpAddress_Type = InetAddress
_IpfixExporterIpAddress_Object = MibTableColumn
ipfixExporterIpAddress = _IpfixExporterIpAddress_Object(
    (1, 3, 6, 1, 2, 1, 999, 2, 1, 1, 1, 1, 3),
    _IpfixExporterIpAddress_Type()
)
ipfixExporterIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixExporterIpAddress.setStatus("current")
_IpfixLifeTimeTemplate_Type = Integer32
_IpfixLifeTimeTemplate_Object = MibTableColumn
ipfixLifeTimeTemplate = _IpfixLifeTimeTemplate_Object(
    (1, 3, 6, 1, 2, 1, 999, 2, 1, 1, 1, 1, 4),
    _IpfixLifeTimeTemplate_Type()
)
ipfixLifeTimeTemplate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixLifeTimeTemplate.setStatus("current")
_IpfixSessionTable_Object = MibTable
ipfixSessionTable = _IpfixSessionTable_Object(
    (1, 3, 6, 1, 2, 1, 999, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ipfixSessionTable.setStatus("current")
_IpfixSessionEntry_Object = MibTableRow
ipfixSessionEntry = _IpfixSessionEntry_Object(
    (1, 3, 6, 1, 2, 1, 999, 2, 1, 1, 2, 1)
)
ipfixSessionEntry.setIndexNames(
    (0, "IPFIX-COLLECTOR-MIB", "ipfixExporterIndex"),
    (0, "IPFIX-COLLECTOR-MIB", "ipfixSessionId"),
)
if mibBuilder.loadTexts:
    ipfixSessionEntry.setStatus("current")


class _IpfixSessionId_Type(Integer32):
    """Custom type ipfixSessionId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IpfixSessionId_Type.__name__ = "Integer32"
_IpfixSessionId_Object = MibTableColumn
ipfixSessionId = _IpfixSessionId_Object(
    (1, 3, 6, 1, 2, 1, 999, 2, 1, 1, 2, 1, 1),
    _IpfixSessionId_Type()
)
ipfixSessionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipfixSessionId.setStatus("current")


class _IpfixSessionStatus_Type(Integer32):
    """Custom type ipfixSessionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("unknown", 0),
          ("up", 1))
    )


_IpfixSessionStatus_Type.__name__ = "Integer32"
_IpfixSessionStatus_Object = MibTableColumn
ipfixSessionStatus = _IpfixSessionStatus_Object(
    (1, 3, 6, 1, 2, 1, 999, 2, 1, 1, 2, 1, 2),
    _IpfixSessionStatus_Type()
)
ipfixSessionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixSessionStatus.setStatus("current")


class _IpfixSessionProtocol_Type(Integer32):
    """Custom type ipfixSessionProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_IpfixSessionProtocol_Type.__name__ = "Integer32"
_IpfixSessionProtocol_Object = MibTableColumn
ipfixSessionProtocol = _IpfixSessionProtocol_Object(
    (1, 3, 6, 1, 2, 1, 999, 2, 1, 1, 2, 1, 3),
    _IpfixSessionProtocol_Type()
)
ipfixSessionProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixSessionProtocol.setStatus("current")


class _IpfixSessionDstPort_Type(Integer32):
    """Custom type ipfixSessionDstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpfixSessionDstPort_Type.__name__ = "Integer32"
_IpfixSessionDstPort_Object = MibTableColumn
ipfixSessionDstPort = _IpfixSessionDstPort_Object(
    (1, 3, 6, 1, 2, 1, 999, 2, 1, 1, 2, 1, 4),
    _IpfixSessionDstPort_Type()
)
ipfixSessionDstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixSessionDstPort.setStatus("current")


class _IpfixSessionSrcPort_Type(Integer32):
    """Custom type ipfixSessionSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpfixSessionSrcPort_Type.__name__ = "Integer32"
_IpfixSessionSrcPort_Object = MibTableColumn
ipfixSessionSrcPort = _IpfixSessionSrcPort_Object(
    (1, 3, 6, 1, 2, 1, 999, 2, 1, 1, 2, 1, 5),
    _IpfixSessionSrcPort_Type()
)
ipfixSessionSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixSessionSrcPort.setStatus("current")
_IpfixSessionStatsTable_Object = MibTable
ipfixSessionStatsTable = _IpfixSessionStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 999, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    ipfixSessionStatsTable.setStatus("current")
_IpfixSessionStatsEntry_Object = MibTableRow
ipfixSessionStatsEntry = _IpfixSessionStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 999, 2, 1, 1, 3, 1)
)
ipfixSessionStatsEntry.setIndexNames(
    (0, "IPFIX-COLLECTOR-MIB", "ipfixExporterIndex"),
    (0, "IPFIX-COLLECTOR-MIB", "ipfixSessionId"),
)
if mibBuilder.loadTexts:
    ipfixSessionStatsEntry.setStatus("current")
_IpfixSessionPackets_Type = Counter32
_IpfixSessionPackets_Object = MibTableColumn
ipfixSessionPackets = _IpfixSessionPackets_Object(
    (1, 3, 6, 1, 2, 1, 999, 2, 1, 1, 3, 1, 3),
    _IpfixSessionPackets_Type()
)
ipfixSessionPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixSessionPackets.setStatus("current")
_IpfixSessionBytes_Type = Counter32
_IpfixSessionBytes_Object = MibTableColumn
ipfixSessionBytes = _IpfixSessionBytes_Object(
    (1, 3, 6, 1, 2, 1, 999, 2, 1, 1, 3, 1, 4),
    _IpfixSessionBytes_Type()
)
ipfixSessionBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixSessionBytes.setStatus("current")
_IpfixSessionMessages_Type = Counter32
_IpfixSessionMessages_Object = MibTableColumn
ipfixSessionMessages = _IpfixSessionMessages_Object(
    (1, 3, 6, 1, 2, 1, 999, 2, 1, 1, 3, 1, 5),
    _IpfixSessionMessages_Type()
)
ipfixSessionMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixSessionMessages.setStatus("current")
_IpfixSessionDiscardMessages_Type = Counter32
_IpfixSessionDiscardMessages_Object = MibTableColumn
ipfixSessionDiscardMessages = _IpfixSessionDiscardMessages_Object(
    (1, 3, 6, 1, 2, 1, 999, 2, 1, 1, 3, 1, 6),
    _IpfixSessionDiscardMessages_Type()
)
ipfixSessionDiscardMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixSessionDiscardMessages.setStatus("current")
_IpfixSessionElapsedTime_Type = Gauge32
_IpfixSessionElapsedTime_Object = MibTableColumn
ipfixSessionElapsedTime = _IpfixSessionElapsedTime_Object(
    (1, 3, 6, 1, 2, 1, 999, 2, 1, 1, 3, 1, 9),
    _IpfixSessionElapsedTime_Type()
)
ipfixSessionElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixSessionElapsedTime.setStatus("current")
_IpfixObdomainStatsTable_Object = MibTable
ipfixObdomainStatsTable = _IpfixObdomainStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 999, 2, 1, 1, 4)
)
if mibBuilder.loadTexts:
    ipfixObdomainStatsTable.setStatus("current")
_IpfixObdomainStatsEntry_Object = MibTableRow
ipfixObdomainStatsEntry = _IpfixObdomainStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 999, 2, 1, 1, 4, 1)
)
ipfixObdomainStatsEntry.setIndexNames(
    (0, "IPFIX-COLLECTOR-MIB", "ipfixExporterIndex"),
    (0, "IPFIX-COLLECTOR-MIB", "ipfixSessionId"),
    (0, "IPFIX-COLLECTOR-MIB", "ipfixObdomainId"),
)
if mibBuilder.loadTexts:
    ipfixObdomainStatsEntry.setStatus("current")


class _IpfixObdomainId_Type(Integer32):
    """Custom type ipfixObdomainId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IpfixObdomainId_Type.__name__ = "Integer32"
_IpfixObdomainId_Object = MibTableColumn
ipfixObdomainId = _IpfixObdomainId_Object(
    (1, 3, 6, 1, 2, 1, 999, 2, 1, 1, 4, 1, 1),
    _IpfixObdomainId_Type()
)
ipfixObdomainId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipfixObdomainId.setStatus("current")
_IpfixObdomainMessages_Type = Counter32
_IpfixObdomainMessages_Object = MibTableColumn
ipfixObdomainMessages = _IpfixObdomainMessages_Object(
    (1, 3, 6, 1, 2, 1, 999, 2, 1, 1, 4, 1, 3),
    _IpfixObdomainMessages_Type()
)
ipfixObdomainMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixObdomainMessages.setStatus("current")
_IpfixObdomainFlows_Type = Counter32
_IpfixObdomainFlows_Object = MibTableColumn
ipfixObdomainFlows = _IpfixObdomainFlows_Object(
    (1, 3, 6, 1, 2, 1, 999, 2, 1, 1, 4, 1, 4),
    _IpfixObdomainFlows_Type()
)
ipfixObdomainFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixObdomainFlows.setStatus("current")
_IpfixObdomainTemplates_Type = Counter32
_IpfixObdomainTemplates_Object = MibTableColumn
ipfixObdomainTemplates = _IpfixObdomainTemplates_Object(
    (1, 3, 6, 1, 2, 1, 999, 2, 1, 1, 4, 1, 5),
    _IpfixObdomainTemplates_Type()
)
ipfixObdomainTemplates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixObdomainTemplates.setStatus("current")
_IpfixObdomainLatestSeqNumber_Type = Integer32
_IpfixObdomainLatestSeqNumber_Object = MibTableColumn
ipfixObdomainLatestSeqNumber = _IpfixObdomainLatestSeqNumber_Object(
    (1, 3, 6, 1, 2, 1, 999, 2, 1, 1, 4, 1, 6),
    _IpfixObdomainLatestSeqNumber_Type()
)
ipfixObdomainLatestSeqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixObdomainLatestSeqNumber.setStatus("current")
_IpfixObdomainDisorderdSeqNumbers_Type = Counter32
_IpfixObdomainDisorderdSeqNumbers_Object = MibTableColumn
ipfixObdomainDisorderdSeqNumbers = _IpfixObdomainDisorderdSeqNumbers_Object(
    (1, 3, 6, 1, 2, 1, 999, 2, 1, 1, 4, 1, 7),
    _IpfixObdomainDisorderdSeqNumbers_Type()
)
ipfixObdomainDisorderdSeqNumbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixObdomainDisorderdSeqNumbers.setStatus("current")
_IpfixTemplateTable_Object = MibTable
ipfixTemplateTable = _IpfixTemplateTable_Object(
    (1, 3, 6, 1, 2, 1, 999, 2, 1, 1, 5)
)
if mibBuilder.loadTexts:
    ipfixTemplateTable.setStatus("current")
_IpfixTemplateEntry_Object = MibTableRow
ipfixTemplateEntry = _IpfixTemplateEntry_Object(
    (1, 3, 6, 1, 2, 1, 999, 2, 1, 1, 5, 1)
)
ipfixTemplateEntry.setIndexNames(
    (0, "IPFIX-COLLECTOR-MIB", "ipfixExporterIndex"),
    (0, "IPFIX-COLLECTOR-MIB", "ipfixSessionId"),
    (0, "IPFIX-COLLECTOR-MIB", "ipfixTemplateId"),
    (0, "IPFIX-COLLECTOR-MIB", "ipfixTemplateIndex"),
)
if mibBuilder.loadTexts:
    ipfixTemplateEntry.setStatus("current")


class _IpfixTemplateId_Type(Integer32):
    """Custom type ipfixTemplateId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IpfixTemplateId_Type.__name__ = "Integer32"
_IpfixTemplateId_Object = MibTableColumn
ipfixTemplateId = _IpfixTemplateId_Object(
    (1, 3, 6, 1, 2, 1, 999, 2, 1, 1, 5, 1, 1),
    _IpfixTemplateId_Type()
)
ipfixTemplateId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipfixTemplateId.setStatus("current")


class _IpfixTemplateIndex_Type(Integer32):
    """Custom type ipfixTemplateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IpfixTemplateIndex_Type.__name__ = "Integer32"
_IpfixTemplateIndex_Object = MibTableColumn
ipfixTemplateIndex = _IpfixTemplateIndex_Object(
    (1, 3, 6, 1, 2, 1, 999, 2, 1, 1, 5, 1, 2),
    _IpfixTemplateIndex_Type()
)
ipfixTemplateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipfixTemplateIndex.setStatus("current")


class _IpfixTemplateFieldId_Type(Integer32):
    """Custom type ipfixTemplateFieldId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IpfixTemplateFieldId_Type.__name__ = "Integer32"
_IpfixTemplateFieldId_Object = MibTableColumn
ipfixTemplateFieldId = _IpfixTemplateFieldId_Object(
    (1, 3, 6, 1, 2, 1, 999, 2, 1, 1, 5, 1, 3),
    _IpfixTemplateFieldId_Type()
)
ipfixTemplateFieldId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixTemplateFieldId.setStatus("current")
_IpfixTemplateFieldLength_Type = Integer32
_IpfixTemplateFieldLength_Object = MibTableColumn
ipfixTemplateFieldLength = _IpfixTemplateFieldLength_Object(
    (1, 3, 6, 1, 2, 1, 999, 2, 1, 1, 5, 1, 4),
    _IpfixTemplateFieldLength_Type()
)
ipfixTemplateFieldLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixTemplateFieldLength.setStatus("current")
_IpfixTemplateStatsTable_Object = MibTable
ipfixTemplateStatsTable = _IpfixTemplateStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 999, 2, 1, 1, 6)
)
if mibBuilder.loadTexts:
    ipfixTemplateStatsTable.setStatus("current")
_IpfixTemplateStatsEntry_Object = MibTableRow
ipfixTemplateStatsEntry = _IpfixTemplateStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 999, 2, 1, 1, 6, 1)
)
ipfixTemplateStatsEntry.setIndexNames(
    (0, "IPFIX-COLLECTOR-MIB", "ipfixExporterIndex"),
    (0, "IPFIX-COLLECTOR-MIB", "ipfixSessionId"),
    (0, "IPFIX-COLLECTOR-MIB", "ipfixTemplateId"),
)
if mibBuilder.loadTexts:
    ipfixTemplateStatsEntry.setStatus("current")
_IpfixTempFlows_Type = Counter32
_IpfixTempFlows_Object = MibTableColumn
ipfixTempFlows = _IpfixTempFlows_Object(
    (1, 3, 6, 1, 2, 1, 999, 2, 1, 1, 6, 1, 2),
    _IpfixTempFlows_Type()
)
ipfixTempFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixTempFlows.setStatus("current")
_IpfixTempReceivedTime_Type = DateAndTime
_IpfixTempReceivedTime_Object = MibTableColumn
ipfixTempReceivedTime = _IpfixTempReceivedTime_Object(
    (1, 3, 6, 1, 2, 1, 999, 2, 1, 1, 6, 1, 3),
    _IpfixTempReceivedTime_Type()
)
ipfixTempReceivedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipfixTempReceivedTime.setStatus("current")
_IpfixCollectorConformance_ObjectIdentity = ObjectIdentity
ipfixCollectorConformance = _IpfixCollectorConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 999, 2, 2)
)
_IpfixPsampExtension_ObjectIdentity = ObjectIdentity
ipfixPsampExtension = _IpfixPsampExtension_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 999, 3)
)
_IpfixConformance_ObjectIdentity = ObjectIdentity
ipfixConformance = _IpfixConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 999, 4)
)
_IpfixCompliances_ObjectIdentity = ObjectIdentity
ipfixCompliances = _IpfixCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 999, 4, 1)
)
_IpfixGroups_ObjectIdentity = ObjectIdentity
ipfixGroups = _IpfixGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 999, 4, 2)
)

# Managed Objects groups

ipfixGroupExporters = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 999, 4, 2, 1)
)
ipfixGroupExporters.setObjects(
      *(("IPFIX-COLLECTOR-MIB", "ipfixExporterIpAddressType"),
        ("IPFIX-COLLECTOR-MIB", "ipfixExporterIpAddress"),
        ("IPFIX-COLLECTOR-MIB", "ipfixLifeTimeTemplate"),
        ("IPFIX-COLLECTOR-MIB", "ipfixSessionProtocol"),
        ("IPFIX-COLLECTOR-MIB", "ipfixSessionDstPort"),
        ("IPFIX-COLLECTOR-MIB", "ipfixSessionSrcPort"),
        ("IPFIX-COLLECTOR-MIB", "ipfixSessionStatus"))
)
if mibBuilder.loadTexts:
    ipfixGroupExporters.setStatus("current")

ipfixGroupTemplates = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 999, 4, 2, 2)
)
ipfixGroupTemplates.setObjects(
      *(("IPFIX-COLLECTOR-MIB", "ipfixTemplateFieldId"),
        ("IPFIX-COLLECTOR-MIB", "ipfixTemplateFieldLength"))
)
if mibBuilder.loadTexts:
    ipfixGroupTemplates.setStatus("current")

ipfixGroupStatistics = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 999, 4, 2, 3)
)
ipfixGroupStatistics.setObjects(
      *(("IPFIX-COLLECTOR-MIB", "ipfixSessionPackets"),
        ("IPFIX-COLLECTOR-MIB", "ipfixSessionBytes"),
        ("IPFIX-COLLECTOR-MIB", "ipfixSessionMessages"),
        ("IPFIX-COLLECTOR-MIB", "ipfixSessionDiscardMessages"),
        ("IPFIX-COLLECTOR-MIB", "ipfixSessionElapsedTime"),
        ("IPFIX-COLLECTOR-MIB", "ipfixObdomainMessages"),
        ("IPFIX-COLLECTOR-MIB", "ipfixObdomainFlows"),
        ("IPFIX-COLLECTOR-MIB", "ipfixObdomainTemplates"),
        ("IPFIX-COLLECTOR-MIB", "ipfixObdomainLatestSeqNumber"),
        ("IPFIX-COLLECTOR-MIB", "ipfixObdomainDisorderdSeqNumbers"),
        ("IPFIX-COLLECTOR-MIB", "ipfixTempFlows"),
        ("IPFIX-COLLECTOR-MIB", "ipfixTempReceivedTime"))
)
if mibBuilder.loadTexts:
    ipfixGroupStatistics.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ipfixCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 999, 4, 1, 1)
)
if mibBuilder.loadTexts:
    ipfixCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPFIX-COLLECTOR-MIB",
    **{"ipfixMIB": ipfixMIB,
       "ipfixExporter": ipfixExporter,
       "ipfixCollector": ipfixCollector,
       "ipfixCollectorObjects": ipfixCollectorObjects,
       "ipfixReceiving": ipfixReceiving,
       "ipfixExporterTable": ipfixExporterTable,
       "ipfixExporterEntry": ipfixExporterEntry,
       "ipfixExporterIndex": ipfixExporterIndex,
       "ipfixExporterIpAddressType": ipfixExporterIpAddressType,
       "ipfixExporterIpAddress": ipfixExporterIpAddress,
       "ipfixLifeTimeTemplate": ipfixLifeTimeTemplate,
       "ipfixSessionTable": ipfixSessionTable,
       "ipfixSessionEntry": ipfixSessionEntry,
       "ipfixSessionId": ipfixSessionId,
       "ipfixSessionStatus": ipfixSessionStatus,
       "ipfixSessionProtocol": ipfixSessionProtocol,
       "ipfixSessionDstPort": ipfixSessionDstPort,
       "ipfixSessionSrcPort": ipfixSessionSrcPort,
       "ipfixSessionStatsTable": ipfixSessionStatsTable,
       "ipfixSessionStatsEntry": ipfixSessionStatsEntry,
       "ipfixSessionPackets": ipfixSessionPackets,
       "ipfixSessionBytes": ipfixSessionBytes,
       "ipfixSessionMessages": ipfixSessionMessages,
       "ipfixSessionDiscardMessages": ipfixSessionDiscardMessages,
       "ipfixSessionElapsedTime": ipfixSessionElapsedTime,
       "ipfixObdomainStatsTable": ipfixObdomainStatsTable,
       "ipfixObdomainStatsEntry": ipfixObdomainStatsEntry,
       "ipfixObdomainId": ipfixObdomainId,
       "ipfixObdomainMessages": ipfixObdomainMessages,
       "ipfixObdomainFlows": ipfixObdomainFlows,
       "ipfixObdomainTemplates": ipfixObdomainTemplates,
       "ipfixObdomainLatestSeqNumber": ipfixObdomainLatestSeqNumber,
       "ipfixObdomainDisorderdSeqNumbers": ipfixObdomainDisorderdSeqNumbers,
       "ipfixTemplateTable": ipfixTemplateTable,
       "ipfixTemplateEntry": ipfixTemplateEntry,
       "ipfixTemplateId": ipfixTemplateId,
       "ipfixTemplateIndex": ipfixTemplateIndex,
       "ipfixTemplateFieldId": ipfixTemplateFieldId,
       "ipfixTemplateFieldLength": ipfixTemplateFieldLength,
       "ipfixTemplateStatsTable": ipfixTemplateStatsTable,
       "ipfixTemplateStatsEntry": ipfixTemplateStatsEntry,
       "ipfixTempFlows": ipfixTempFlows,
       "ipfixTempReceivedTime": ipfixTempReceivedTime,
       "ipfixCollectorConformance": ipfixCollectorConformance,
       "ipfixPsampExtension": ipfixPsampExtension,
       "ipfixConformance": ipfixConformance,
       "ipfixCompliances": ipfixCompliances,
       "ipfixCompliance": ipfixCompliance,
       "ipfixGroups": ipfixGroups,
       "ipfixGroupExporters": ipfixGroupExporters,
       "ipfixGroupTemplates": ipfixGroupTemplates,
       "ipfixGroupStatistics": ipfixGroupStatistics}
)
