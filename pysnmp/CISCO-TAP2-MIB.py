# SNMP MIB module (CISCO-TAP2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-TAP2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:55:21 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 iso) = mibBuilder.importSymbols(
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
    "iso")

(DateAndTime,
 DisplayString,
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoTap2MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 399)
)
ciscoTap2MIB.setRevisions(
        ("2008-09-10 00:00",
         "2007-12-21 00:00",
         "2006-11-27 00:00",
         "2004-03-11 00:00",
         "2004-01-27 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Ctap2Dscp(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoTap2MIBNotifs_ObjectIdentity = ObjectIdentity
ciscoTap2MIBNotifs = _CiscoTap2MIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 399, 0)
)
_CiscoTap2MIBObjects_ObjectIdentity = ObjectIdentity
ciscoTap2MIBObjects = _CiscoTap2MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 399, 1)
)
_CTap2MediationGroup_ObjectIdentity = ObjectIdentity
cTap2MediationGroup = _CTap2MediationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 399, 1, 1)
)


class _CTap2MediationNewIndex_Type(Integer32):
    """Custom type cTap2MediationNewIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CTap2MediationNewIndex_Type.__name__ = "Integer32"
_CTap2MediationNewIndex_Object = MibScalar
cTap2MediationNewIndex = _CTap2MediationNewIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 399, 1, 1, 1),
    _CTap2MediationNewIndex_Type()
)
cTap2MediationNewIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cTap2MediationNewIndex.setStatus("current")
_CTap2MediationTable_Object = MibTable
cTap2MediationTable = _CTap2MediationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 399, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cTap2MediationTable.setStatus("current")
_CTap2MediationEntry_Object = MibTableRow
cTap2MediationEntry = _CTap2MediationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 399, 1, 1, 2, 1)
)
cTap2MediationEntry.setIndexNames(
    (0, "CISCO-TAP2-MIB", "cTap2MediationContentId"),
)
if mibBuilder.loadTexts:
    cTap2MediationEntry.setStatus("current")


class _CTap2MediationContentId_Type(Integer32):
    """Custom type cTap2MediationContentId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CTap2MediationContentId_Type.__name__ = "Integer32"
_CTap2MediationContentId_Object = MibTableColumn
cTap2MediationContentId = _CTap2MediationContentId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 399, 1, 1, 2, 1, 1),
    _CTap2MediationContentId_Type()
)
cTap2MediationContentId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cTap2MediationContentId.setStatus("current")
_CTap2MediationDestAddressType_Type = InetAddressType
_CTap2MediationDestAddressType_Object = MibTableColumn
cTap2MediationDestAddressType = _CTap2MediationDestAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 399, 1, 1, 2, 1, 2),
    _CTap2MediationDestAddressType_Type()
)
cTap2MediationDestAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cTap2MediationDestAddressType.setStatus("current")
_CTap2MediationDestAddress_Type = InetAddress
_CTap2MediationDestAddress_Object = MibTableColumn
cTap2MediationDestAddress = _CTap2MediationDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 399, 1, 1, 2, 1, 3),
    _CTap2MediationDestAddress_Type()
)
cTap2MediationDestAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cTap2MediationDestAddress.setStatus("current")
_CTap2MediationDestPort_Type = InetPortNumber
_CTap2MediationDestPort_Object = MibTableColumn
cTap2MediationDestPort = _CTap2MediationDestPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 399, 1, 1, 2, 1, 4),
    _CTap2MediationDestPort_Type()
)
cTap2MediationDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cTap2MediationDestPort.setStatus("current")
_CTap2MediationSrcInterface_Type = InterfaceIndexOrZero
_CTap2MediationSrcInterface_Object = MibTableColumn
cTap2MediationSrcInterface = _CTap2MediationSrcInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 399, 1, 1, 2, 1, 5),
    _CTap2MediationSrcInterface_Type()
)
cTap2MediationSrcInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cTap2MediationSrcInterface.setStatus("current")
_CTap2MediationRtcpPort_Type = InetPortNumber
_CTap2MediationRtcpPort_Object = MibTableColumn
cTap2MediationRtcpPort = _CTap2MediationRtcpPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 399, 1, 1, 2, 1, 6),
    _CTap2MediationRtcpPort_Type()
)
cTap2MediationRtcpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cTap2MediationRtcpPort.setStatus("current")


class _CTap2MediationDscp_Type(Ctap2Dscp):
    """Custom type cTap2MediationDscp based on Ctap2Dscp"""
    defaultValue = 34


_CTap2MediationDscp_Object = MibTableColumn
cTap2MediationDscp = _CTap2MediationDscp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 399, 1, 1, 2, 1, 7),
    _CTap2MediationDscp_Type()
)
cTap2MediationDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cTap2MediationDscp.setStatus("current")


class _CTap2MediationDataType_Type(Integer32):
    """Custom type cTap2MediationDataType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_CTap2MediationDataType_Type.__name__ = "Integer32"
_CTap2MediationDataType_Object = MibTableColumn
cTap2MediationDataType = _CTap2MediationDataType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 399, 1, 1, 2, 1, 8),
    _CTap2MediationDataType_Type()
)
cTap2MediationDataType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cTap2MediationDataType.setStatus("current")


class _CTap2MediationRetransmitType_Type(Integer32):
    """Custom type cTap2MediationRetransmitType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_CTap2MediationRetransmitType_Type.__name__ = "Integer32"
_CTap2MediationRetransmitType_Object = MibTableColumn
cTap2MediationRetransmitType = _CTap2MediationRetransmitType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 399, 1, 1, 2, 1, 9),
    _CTap2MediationRetransmitType_Type()
)
cTap2MediationRetransmitType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cTap2MediationRetransmitType.setStatus("current")
_CTap2MediationTimeout_Type = DateAndTime
_CTap2MediationTimeout_Object = MibTableColumn
cTap2MediationTimeout = _CTap2MediationTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 399, 1, 1, 2, 1, 10),
    _CTap2MediationTimeout_Type()
)
cTap2MediationTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cTap2MediationTimeout.setStatus("current")


class _CTap2MediationTransport_Type(Integer32):
    """Custom type cTap2MediationTransport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("rtp", 5),
          ("rtpNack", 2),
          ("sctp", 4),
          ("tcp", 3),
          ("udp", 1))
    )


_CTap2MediationTransport_Type.__name__ = "Integer32"
_CTap2MediationTransport_Object = MibTableColumn
cTap2MediationTransport = _CTap2MediationTransport_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 399, 1, 1, 2, 1, 11),
    _CTap2MediationTransport_Type()
)
cTap2MediationTransport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cTap2MediationTransport.setStatus("current")


class _CTap2MediationNotificationEnable_Type(TruthValue):
    """Custom type cTap2MediationNotificationEnable based on TruthValue"""


_CTap2MediationNotificationEnable_Object = MibTableColumn
cTap2MediationNotificationEnable = _CTap2MediationNotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 399, 1, 1, 2, 1, 12),
    _CTap2MediationNotificationEnable_Type()
)
cTap2MediationNotificationEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cTap2MediationNotificationEnable.setStatus("current")
_CTap2MediationStatus_Type = RowStatus
_CTap2MediationStatus_Object = MibTableColumn
cTap2MediationStatus = _CTap2MediationStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 399, 1, 1, 2, 1, 13),
    _CTap2MediationStatus_Type()
)
cTap2MediationStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cTap2MediationStatus.setStatus("current")


class _CTap2MediationCapabilities_Type(Bits):
    """Custom type cTap2MediationCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("ipV4SrcInterface", 0),
          ("ipV6SrcInterface", 1),
          ("rtp", 6),
          ("rtpNack", 3),
          ("sctp", 5),
          ("tcp", 4),
          ("udp", 2))
    )

_CTap2MediationCapabilities_Type.__name__ = "Bits"
_CTap2MediationCapabilities_Object = MibScalar
cTap2MediationCapabilities = _CTap2MediationCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 399, 1, 1, 3),
    _CTap2MediationCapabilities_Type()
)
cTap2MediationCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cTap2MediationCapabilities.setStatus("current")
_CTap2StreamGroup_ObjectIdentity = ObjectIdentity
cTap2StreamGroup = _CTap2StreamGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 399, 1, 2)
)
_CTap2StreamTable_Object = MibTable
cTap2StreamTable = _CTap2StreamTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 399, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cTap2StreamTable.setStatus("current")
_CTap2StreamEntry_Object = MibTableRow
cTap2StreamEntry = _CTap2StreamEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 399, 1, 2, 1, 1)
)
cTap2StreamEntry.setIndexNames(
    (0, "CISCO-TAP2-MIB", "cTap2MediationContentId"),
    (0, "CISCO-TAP2-MIB", "cTap2StreamIndex"),
)
if mibBuilder.loadTexts:
    cTap2StreamEntry.setStatus("current")


class _CTap2StreamIndex_Type(Integer32):
    """Custom type cTap2StreamIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CTap2StreamIndex_Type.__name__ = "Integer32"
_CTap2StreamIndex_Object = MibTableColumn
cTap2StreamIndex = _CTap2StreamIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 399, 1, 2, 1, 1, 1),
    _CTap2StreamIndex_Type()
)
cTap2StreamIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cTap2StreamIndex.setStatus("current")


class _CTap2StreamType_Type(Integer32):
    """Custom type cTap2StreamType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ip", 1),
          ("mac", 2),
          ("mobility", 5),
          ("msPdsn", 4),
          ("userConnection", 3))
    )


_CTap2StreamType_Type.__name__ = "Integer32"
_CTap2StreamType_Object = MibTableColumn
cTap2StreamType = _CTap2StreamType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 399, 1, 2, 1, 1, 2),
    _CTap2StreamType_Type()
)
cTap2StreamType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cTap2StreamType.setStatus("current")


class _CTap2StreamInterceptEnable_Type(TruthValue):
    """Custom type cTap2StreamInterceptEnable based on TruthValue"""


_CTap2StreamInterceptEnable_Object = MibTableColumn
cTap2StreamInterceptEnable = _CTap2StreamInterceptEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 399, 1, 2, 1, 1, 3),
    _CTap2StreamInterceptEnable_Type()
)
cTap2StreamInterceptEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cTap2StreamInterceptEnable.setStatus("current")
_CTap2StreamInterceptedPackets_Type = Counter32
_CTap2StreamInterceptedPackets_Object = MibTableColumn
cTap2StreamInterceptedPackets = _CTap2StreamInterceptedPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 399, 1, 2, 1, 1, 4),
    _CTap2StreamInterceptedPackets_Type()
)
cTap2StreamInterceptedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cTap2StreamInterceptedPackets.setStatus("current")
_CTap2StreamInterceptDrops_Type = Counter32
_CTap2StreamInterceptDrops_Object = MibTableColumn
cTap2StreamInterceptDrops = _CTap2StreamInterceptDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 399, 1, 2, 1, 1, 5),
    _CTap2StreamInterceptDrops_Type()
)
cTap2StreamInterceptDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cTap2StreamInterceptDrops.setStatus("current")
_CTap2StreamStatus_Type = RowStatus
_CTap2StreamStatus_Object = MibTableColumn
cTap2StreamStatus = _CTap2StreamStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 399, 1, 2, 1, 1, 6),
    _CTap2StreamStatus_Type()
)
cTap2StreamStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cTap2StreamStatus.setStatus("current")
_CTap2StreamInterceptedHCPackets_Type = Counter64
_CTap2StreamInterceptedHCPackets_Object = MibTableColumn
cTap2StreamInterceptedHCPackets = _CTap2StreamInterceptedHCPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 399, 1, 2, 1, 1, 7),
    _CTap2StreamInterceptedHCPackets_Type()
)
cTap2StreamInterceptedHCPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cTap2StreamInterceptedHCPackets.setStatus("current")
_CTap2StreamInterceptHCDrops_Type = Counter64
_CTap2StreamInterceptHCDrops_Object = MibTableColumn
cTap2StreamInterceptHCDrops = _CTap2StreamInterceptHCDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 399, 1, 2, 1, 1, 8),
    _CTap2StreamInterceptHCDrops_Type()
)
cTap2StreamInterceptHCDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cTap2StreamInterceptHCDrops.setStatus("current")
_CTap2DebugGroup_ObjectIdentity = ObjectIdentity
cTap2DebugGroup = _CTap2DebugGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 399, 1, 3)
)


class _CTap2DebugAge_Type(Integer32):
    """Custom type cTap2DebugAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CTap2DebugAge_Type.__name__ = "Integer32"
_CTap2DebugAge_Object = MibScalar
cTap2DebugAge = _CTap2DebugAge_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 399, 1, 3, 1),
    _CTap2DebugAge_Type()
)
cTap2DebugAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cTap2DebugAge.setStatus("current")


class _CTap2DebugMaxEntries_Type(Integer32):
    """Custom type cTap2DebugMaxEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CTap2DebugMaxEntries_Type.__name__ = "Integer32"
_CTap2DebugMaxEntries_Object = MibScalar
cTap2DebugMaxEntries = _CTap2DebugMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 399, 1, 3, 2),
    _CTap2DebugMaxEntries_Type()
)
cTap2DebugMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cTap2DebugMaxEntries.setStatus("current")
_CTap2DebugTable_Object = MibTable
cTap2DebugTable = _CTap2DebugTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 399, 1, 3, 3)
)
if mibBuilder.loadTexts:
    cTap2DebugTable.setStatus("current")
_CTap2DebugEntry_Object = MibTableRow
cTap2DebugEntry = _CTap2DebugEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 399, 1, 3, 3, 1)
)
cTap2DebugEntry.setIndexNames(
    (0, "CISCO-TAP2-MIB", "cTap2DebugIndex"),
)
if mibBuilder.loadTexts:
    cTap2DebugEntry.setStatus("current")


class _CTap2DebugIndex_Type(Integer32):
    """Custom type cTap2DebugIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CTap2DebugIndex_Type.__name__ = "Integer32"
_CTap2DebugIndex_Object = MibTableColumn
cTap2DebugIndex = _CTap2DebugIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 399, 1, 3, 3, 1, 1),
    _CTap2DebugIndex_Type()
)
cTap2DebugIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cTap2DebugIndex.setStatus("current")
_CTap2DebugMediationId_Type = Unsigned32
_CTap2DebugMediationId_Object = MibTableColumn
cTap2DebugMediationId = _CTap2DebugMediationId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 399, 1, 3, 3, 1, 2),
    _CTap2DebugMediationId_Type()
)
cTap2DebugMediationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cTap2DebugMediationId.setStatus("current")
_CTap2DebugStreamId_Type = Unsigned32
_CTap2DebugStreamId_Object = MibTableColumn
cTap2DebugStreamId = _CTap2DebugStreamId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 399, 1, 3, 3, 1, 3),
    _CTap2DebugStreamId_Type()
)
cTap2DebugStreamId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cTap2DebugStreamId.setStatus("current")
_CTap2DebugMessage_Type = SnmpAdminString
_CTap2DebugMessage_Object = MibTableColumn
cTap2DebugMessage = _CTap2DebugMessage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 399, 1, 3, 3, 1, 4),
    _CTap2DebugMessage_Type()
)
cTap2DebugMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cTap2DebugMessage.setStatus("current")
_CTap2DebugStatus_Type = RowStatus
_CTap2DebugStatus_Object = MibTableColumn
cTap2DebugStatus = _CTap2DebugStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 399, 1, 3, 3, 1, 5),
    _CTap2DebugStatus_Type()
)
cTap2DebugStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cTap2DebugStatus.setStatus("current")
_CTap2DebugUserTable_Object = MibTable
cTap2DebugUserTable = _CTap2DebugUserTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 399, 1, 3, 4)
)
if mibBuilder.loadTexts:
    cTap2DebugUserTable.setStatus("current")
_CTap2DebugUserEntry_Object = MibTableRow
cTap2DebugUserEntry = _CTap2DebugUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 399, 1, 3, 4, 1)
)
cTap2DebugUserEntry.setIndexNames(
    (0, "CISCO-TAP2-MIB", "cTap2MediationContentId"),
    (0, "CISCO-TAP2-MIB", "cTap2DebugUserName"),
)
if mibBuilder.loadTexts:
    cTap2DebugUserEntry.setStatus("current")


class _CTap2DebugUserName_Type(SnmpAdminString):
    """Custom type cTap2DebugUserName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CTap2DebugUserName_Type.__name__ = "SnmpAdminString"
_CTap2DebugUserName_Object = MibTableColumn
cTap2DebugUserName = _CTap2DebugUserName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 399, 1, 3, 4, 1, 1),
    _CTap2DebugUserName_Type()
)
cTap2DebugUserName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cTap2DebugUserName.setStatus("current")
_CTap2DebugUserTimeout_Type = DateAndTime
_CTap2DebugUserTimeout_Object = MibTableColumn
cTap2DebugUserTimeout = _CTap2DebugUserTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 399, 1, 3, 4, 1, 2),
    _CTap2DebugUserTimeout_Type()
)
cTap2DebugUserTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cTap2DebugUserTimeout.setStatus("current")


class _CTap2DebugUserStorageType_Type(StorageType):
    """Custom type cTap2DebugUserStorageType based on StorageType"""


_CTap2DebugUserStorageType_Object = MibTableColumn
cTap2DebugUserStorageType = _CTap2DebugUserStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 399, 1, 3, 4, 1, 3),
    _CTap2DebugUserStorageType_Type()
)
cTap2DebugUserStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cTap2DebugUserStorageType.setStatus("current")
_CTap2DebugUserStatus_Type = RowStatus
_CTap2DebugUserStatus_Object = MibTableColumn
cTap2DebugUserStatus = _CTap2DebugUserStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 399, 1, 3, 4, 1, 4),
    _CTap2DebugUserStatus_Type()
)
cTap2DebugUserStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cTap2DebugUserStatus.setStatus("current")
_CiscoTap2MIBConform_ObjectIdentity = ObjectIdentity
ciscoTap2MIBConform = _CiscoTap2MIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 399, 2)
)
_CiscoTap2MIBCompliances_ObjectIdentity = ObjectIdentity
ciscoTap2MIBCompliances = _CiscoTap2MIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 399, 2, 1)
)
_CiscoTap2MIBGroups_ObjectIdentity = ObjectIdentity
ciscoTap2MIBGroups = _CiscoTap2MIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 399, 2, 2)
)

# Managed Objects groups

ciscoTap2MediationComplianceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 399, 2, 2, 1)
)
ciscoTap2MediationComplianceGroup.setObjects(
      *(("CISCO-TAP2-MIB", "cTap2MediationNewIndex"),
        ("CISCO-TAP2-MIB", "cTap2MediationDestAddressType"),
        ("CISCO-TAP2-MIB", "cTap2MediationDestAddress"),
        ("CISCO-TAP2-MIB", "cTap2MediationDestPort"),
        ("CISCO-TAP2-MIB", "cTap2MediationSrcInterface"),
        ("CISCO-TAP2-MIB", "cTap2MediationRtcpPort"),
        ("CISCO-TAP2-MIB", "cTap2MediationDscp"),
        ("CISCO-TAP2-MIB", "cTap2MediationDataType"),
        ("CISCO-TAP2-MIB", "cTap2MediationRetransmitType"),
        ("CISCO-TAP2-MIB", "cTap2MediationTimeout"),
        ("CISCO-TAP2-MIB", "cTap2MediationTransport"),
        ("CISCO-TAP2-MIB", "cTap2MediationNotificationEnable"),
        ("CISCO-TAP2-MIB", "cTap2MediationStatus"))
)
if mibBuilder.loadTexts:
    ciscoTap2MediationComplianceGroup.setStatus("current")

ciscoTap2StreamComplianceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 399, 2, 2, 2)
)
ciscoTap2StreamComplianceGroup.setObjects(
      *(("CISCO-TAP2-MIB", "cTap2StreamType"),
        ("CISCO-TAP2-MIB", "cTap2StreamInterceptEnable"),
        ("CISCO-TAP2-MIB", "cTap2StreamInterceptedPackets"),
        ("CISCO-TAP2-MIB", "cTap2StreamInterceptDrops"),
        ("CISCO-TAP2-MIB", "cTap2StreamStatus"))
)
if mibBuilder.loadTexts:
    ciscoTap2StreamComplianceGroup.setStatus("current")

ciscoTap2MediationCpbComplianceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 399, 2, 2, 4)
)
ciscoTap2MediationCpbComplianceGroup.setObjects(
    ("CISCO-TAP2-MIB", "cTap2MediationCapabilities")
)
if mibBuilder.loadTexts:
    ciscoTap2MediationCpbComplianceGroup.setStatus("current")

ciscoTap2DebugComplianceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 399, 2, 2, 5)
)
ciscoTap2DebugComplianceGroup.setObjects(
      *(("CISCO-TAP2-MIB", "cTap2DebugAge"),
        ("CISCO-TAP2-MIB", "cTap2DebugMaxEntries"),
        ("CISCO-TAP2-MIB", "cTap2DebugMediationId"),
        ("CISCO-TAP2-MIB", "cTap2DebugStreamId"),
        ("CISCO-TAP2-MIB", "cTap2DebugMessage"),
        ("CISCO-TAP2-MIB", "cTap2DebugStatus"))
)
if mibBuilder.loadTexts:
    ciscoTap2DebugComplianceGroup.setStatus("deprecated")

ciscoTap2StreamHCStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 399, 2, 2, 6)
)
ciscoTap2StreamHCStatsGroup.setObjects(
      *(("CISCO-TAP2-MIB", "cTap2StreamInterceptedHCPackets"),
        ("CISCO-TAP2-MIB", "cTap2StreamInterceptHCDrops"))
)
if mibBuilder.loadTexts:
    ciscoTap2StreamHCStatsGroup.setStatus("current")

ciscoTap2DebugComplianceGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 399, 2, 2, 7)
)
ciscoTap2DebugComplianceGroupRev1.setObjects(
      *(("CISCO-TAP2-MIB", "cTap2DebugAge"),
        ("CISCO-TAP2-MIB", "cTap2DebugMaxEntries"),
        ("CISCO-TAP2-MIB", "cTap2DebugMediationId"),
        ("CISCO-TAP2-MIB", "cTap2DebugStreamId"),
        ("CISCO-TAP2-MIB", "cTap2DebugMessage"),
        ("CISCO-TAP2-MIB", "cTap2DebugStatus"),
        ("CISCO-TAP2-MIB", "cTap2DebugUserTimeout"),
        ("CISCO-TAP2-MIB", "cTap2DebugUserStorageType"),
        ("CISCO-TAP2-MIB", "cTap2DebugUserStatus"))
)
if mibBuilder.loadTexts:
    ciscoTap2DebugComplianceGroupRev1.setStatus("current")


# Notification objects

ciscoTap2MIBActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 399, 0, 1)
)
if mibBuilder.loadTexts:
    ciscoTap2MIBActive.setStatus(
        "current"
    )

ciscoTap2MediationTimedOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 399, 0, 2)
)
ciscoTap2MediationTimedOut.setObjects(
    ("CISCO-TAP2-MIB", "cTap2MediationStatus")
)
if mibBuilder.loadTexts:
    ciscoTap2MediationTimedOut.setStatus(
        "current"
    )

ciscoTap2MediationDebug = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 399, 0, 3)
)
ciscoTap2MediationDebug.setObjects(
      *(("CISCO-TAP2-MIB", "cTap2DebugMediationId"),
        ("CISCO-TAP2-MIB", "cTap2DebugMessage"))
)
if mibBuilder.loadTexts:
    ciscoTap2MediationDebug.setStatus(
        "current"
    )

ciscoTap2StreamDebug = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 399, 0, 4)
)
ciscoTap2StreamDebug.setObjects(
      *(("CISCO-TAP2-MIB", "cTap2DebugMediationId"),
        ("CISCO-TAP2-MIB", "cTap2DebugStreamId"),
        ("CISCO-TAP2-MIB", "cTap2DebugMessage"))
)
if mibBuilder.loadTexts:
    ciscoTap2StreamDebug.setStatus(
        "current"
    )

ciscoTap2Switchover = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 399, 0, 5)
)
if mibBuilder.loadTexts:
    ciscoTap2Switchover.setStatus(
        "current"
    )


# Notifications groups

ciscoTap2NotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 399, 2, 2, 3)
)
ciscoTap2NotificationGroup.setObjects(
      *(("CISCO-TAP2-MIB", "ciscoTap2MIBActive"),
        ("CISCO-TAP2-MIB", "ciscoTap2MediationTimedOut"),
        ("CISCO-TAP2-MIB", "ciscoTap2MediationDebug"),
        ("CISCO-TAP2-MIB", "ciscoTap2StreamDebug"),
        ("CISCO-TAP2-MIB", "ciscoTap2Switchover"))
)
if mibBuilder.loadTexts:
    ciscoTap2NotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoTap2MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 399, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoTap2MIBCompliance.setStatus(
        "deprecated"
    )

ciscoTap2MIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 399, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoTap2MIBComplianceRev2.setStatus(
        "deprecated"
    )

ciscoTap2MIBComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 399, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoTap2MIBComplianceRev3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-TAP2-MIB",
    **{"Ctap2Dscp": Ctap2Dscp,
       "ciscoTap2MIB": ciscoTap2MIB,
       "ciscoTap2MIBNotifs": ciscoTap2MIBNotifs,
       "ciscoTap2MIBActive": ciscoTap2MIBActive,
       "ciscoTap2MediationTimedOut": ciscoTap2MediationTimedOut,
       "ciscoTap2MediationDebug": ciscoTap2MediationDebug,
       "ciscoTap2StreamDebug": ciscoTap2StreamDebug,
       "ciscoTap2Switchover": ciscoTap2Switchover,
       "ciscoTap2MIBObjects": ciscoTap2MIBObjects,
       "cTap2MediationGroup": cTap2MediationGroup,
       "cTap2MediationNewIndex": cTap2MediationNewIndex,
       "cTap2MediationTable": cTap2MediationTable,
       "cTap2MediationEntry": cTap2MediationEntry,
       "cTap2MediationContentId": cTap2MediationContentId,
       "cTap2MediationDestAddressType": cTap2MediationDestAddressType,
       "cTap2MediationDestAddress": cTap2MediationDestAddress,
       "cTap2MediationDestPort": cTap2MediationDestPort,
       "cTap2MediationSrcInterface": cTap2MediationSrcInterface,
       "cTap2MediationRtcpPort": cTap2MediationRtcpPort,
       "cTap2MediationDscp": cTap2MediationDscp,
       "cTap2MediationDataType": cTap2MediationDataType,
       "cTap2MediationRetransmitType": cTap2MediationRetransmitType,
       "cTap2MediationTimeout": cTap2MediationTimeout,
       "cTap2MediationTransport": cTap2MediationTransport,
       "cTap2MediationNotificationEnable": cTap2MediationNotificationEnable,
       "cTap2MediationStatus": cTap2MediationStatus,
       "cTap2MediationCapabilities": cTap2MediationCapabilities,
       "cTap2StreamGroup": cTap2StreamGroup,
       "cTap2StreamTable": cTap2StreamTable,
       "cTap2StreamEntry": cTap2StreamEntry,
       "cTap2StreamIndex": cTap2StreamIndex,
       "cTap2StreamType": cTap2StreamType,
       "cTap2StreamInterceptEnable": cTap2StreamInterceptEnable,
       "cTap2StreamInterceptedPackets": cTap2StreamInterceptedPackets,
       "cTap2StreamInterceptDrops": cTap2StreamInterceptDrops,
       "cTap2StreamStatus": cTap2StreamStatus,
       "cTap2StreamInterceptedHCPackets": cTap2StreamInterceptedHCPackets,
       "cTap2StreamInterceptHCDrops": cTap2StreamInterceptHCDrops,
       "cTap2DebugGroup": cTap2DebugGroup,
       "cTap2DebugAge": cTap2DebugAge,
       "cTap2DebugMaxEntries": cTap2DebugMaxEntries,
       "cTap2DebugTable": cTap2DebugTable,
       "cTap2DebugEntry": cTap2DebugEntry,
       "cTap2DebugIndex": cTap2DebugIndex,
       "cTap2DebugMediationId": cTap2DebugMediationId,
       "cTap2DebugStreamId": cTap2DebugStreamId,
       "cTap2DebugMessage": cTap2DebugMessage,
       "cTap2DebugStatus": cTap2DebugStatus,
       "cTap2DebugUserTable": cTap2DebugUserTable,
       "cTap2DebugUserEntry": cTap2DebugUserEntry,
       "cTap2DebugUserName": cTap2DebugUserName,
       "cTap2DebugUserTimeout": cTap2DebugUserTimeout,
       "cTap2DebugUserStorageType": cTap2DebugUserStorageType,
       "cTap2DebugUserStatus": cTap2DebugUserStatus,
       "ciscoTap2MIBConform": ciscoTap2MIBConform,
       "ciscoTap2MIBCompliances": ciscoTap2MIBCompliances,
       "ciscoTap2MIBCompliance": ciscoTap2MIBCompliance,
       "ciscoTap2MIBComplianceRev2": ciscoTap2MIBComplianceRev2,
       "ciscoTap2MIBComplianceRev3": ciscoTap2MIBComplianceRev3,
       "ciscoTap2MIBGroups": ciscoTap2MIBGroups,
       "ciscoTap2MediationComplianceGroup": ciscoTap2MediationComplianceGroup,
       "ciscoTap2StreamComplianceGroup": ciscoTap2StreamComplianceGroup,
       "ciscoTap2NotificationGroup": ciscoTap2NotificationGroup,
       "ciscoTap2MediationCpbComplianceGroup": ciscoTap2MediationCpbComplianceGroup,
       "ciscoTap2DebugComplianceGroup": ciscoTap2DebugComplianceGroup,
       "ciscoTap2StreamHCStatsGroup": ciscoTap2StreamHCStatsGroup,
       "ciscoTap2DebugComplianceGroupRev1": ciscoTap2DebugComplianceGroupRev1}
)
