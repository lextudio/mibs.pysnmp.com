# SNMP MIB module (PKTC-ES-TAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PKTC-ES-TAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:52:59 2024
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

(pktcESSupportMibs,) = mibBuilder.importSymbols(
    "CLAB-DEF-MIB",
    "pktcESSupportMibs")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

pktcESTapMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 1)
)
pktcESTapMib.setRevisions(
        ("2008-04-25 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PktcEScTapDscp(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )



# MIB Managed Objects in the order of their OIDs

_PktcESTapMibNotifs_ObjectIdentity = ObjectIdentity
pktcESTapMibNotifs = _PktcESTapMibNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 1, 0)
)
_PktcESTapMibObjects_ObjectIdentity = ObjectIdentity
pktcESTapMibObjects = _PktcESTapMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 1, 1)
)
_PktcEScTapMediationGroup_ObjectIdentity = ObjectIdentity
pktcEScTapMediationGroup = _PktcEScTapMediationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 1, 1, 1)
)


class _PktcEScTapMediationNewIndex_Type(Integer32):
    """Custom type pktcEScTapMediationNewIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PktcEScTapMediationNewIndex_Type.__name__ = "Integer32"
_PktcEScTapMediationNewIndex_Object = MibScalar
pktcEScTapMediationNewIndex = _PktcEScTapMediationNewIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 1, 1, 1, 1),
    _PktcEScTapMediationNewIndex_Type()
)
pktcEScTapMediationNewIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEScTapMediationNewIndex.setStatus("current")
_PktcEScTapMediationTable_Object = MibTable
pktcEScTapMediationTable = _PktcEScTapMediationTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    pktcEScTapMediationTable.setStatus("current")
_PktcEScTapMediationEntry_Object = MibTableRow
pktcEScTapMediationEntry = _PktcEScTapMediationEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 1, 1, 1, 2, 1)
)
pktcEScTapMediationEntry.setIndexNames(
    (0, "PKTC-ES-TAP-MIB", "pktcEScTapMediationContentId"),
)
if mibBuilder.loadTexts:
    pktcEScTapMediationEntry.setStatus("current")


class _PktcEScTapMediationContentId_Type(Integer32):
    """Custom type pktcEScTapMediationContentId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PktcEScTapMediationContentId_Type.__name__ = "Integer32"
_PktcEScTapMediationContentId_Object = MibTableColumn
pktcEScTapMediationContentId = _PktcEScTapMediationContentId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 1, 1, 1, 2, 1, 1),
    _PktcEScTapMediationContentId_Type()
)
pktcEScTapMediationContentId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEScTapMediationContentId.setStatus("current")
_PktcEScTapMediationDestAddressType_Type = InetAddressType
_PktcEScTapMediationDestAddressType_Object = MibTableColumn
pktcEScTapMediationDestAddressType = _PktcEScTapMediationDestAddressType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 1, 1, 1, 2, 1, 2),
    _PktcEScTapMediationDestAddressType_Type()
)
pktcEScTapMediationDestAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEScTapMediationDestAddressType.setStatus("current")
_PktcEScTapMediationDestAddress_Type = InetAddress
_PktcEScTapMediationDestAddress_Object = MibTableColumn
pktcEScTapMediationDestAddress = _PktcEScTapMediationDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 1, 1, 1, 2, 1, 3),
    _PktcEScTapMediationDestAddress_Type()
)
pktcEScTapMediationDestAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEScTapMediationDestAddress.setStatus("current")
_PktcEScTapMediationDestPort_Type = InetPortNumber
_PktcEScTapMediationDestPort_Object = MibTableColumn
pktcEScTapMediationDestPort = _PktcEScTapMediationDestPort_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 1, 1, 1, 2, 1, 4),
    _PktcEScTapMediationDestPort_Type()
)
pktcEScTapMediationDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEScTapMediationDestPort.setStatus("current")
_PktcEScTapMediationSrcInterface_Type = InterfaceIndexOrZero
_PktcEScTapMediationSrcInterface_Object = MibTableColumn
pktcEScTapMediationSrcInterface = _PktcEScTapMediationSrcInterface_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 1, 1, 1, 2, 1, 5),
    _PktcEScTapMediationSrcInterface_Type()
)
pktcEScTapMediationSrcInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEScTapMediationSrcInterface.setStatus("current")


class _PktcEScTapMediationDscp_Type(PktcEScTapDscp):
    """Custom type pktcEScTapMediationDscp based on PktcEScTapDscp"""
    defaultValue = 34


_PktcEScTapMediationDscp_Object = MibTableColumn
pktcEScTapMediationDscp = _PktcEScTapMediationDscp_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 1, 1, 1, 2, 1, 7),
    _PktcEScTapMediationDscp_Type()
)
pktcEScTapMediationDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEScTapMediationDscp.setStatus("current")
_PktcEScTapMediationTimeout_Type = DateAndTime
_PktcEScTapMediationTimeout_Object = MibTableColumn
pktcEScTapMediationTimeout = _PktcEScTapMediationTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 1, 1, 1, 2, 1, 10),
    _PktcEScTapMediationTimeout_Type()
)
pktcEScTapMediationTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEScTapMediationTimeout.setStatus("current")


class _PktcEScTapMediationTransport_Type(Integer32):
    """Custom type pktcEScTapMediationTransport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("udp", 1)
    )


_PktcEScTapMediationTransport_Type.__name__ = "Integer32"
_PktcEScTapMediationTransport_Object = MibTableColumn
pktcEScTapMediationTransport = _PktcEScTapMediationTransport_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 1, 1, 1, 2, 1, 11),
    _PktcEScTapMediationTransport_Type()
)
pktcEScTapMediationTransport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEScTapMediationTransport.setStatus("current")


class _PktcEScTapMediationNotificationEnable_Type(TruthValue):
    """Custom type pktcEScTapMediationNotificationEnable based on TruthValue"""


_PktcEScTapMediationNotificationEnable_Object = MibTableColumn
pktcEScTapMediationNotificationEnable = _PktcEScTapMediationNotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 1, 1, 1, 2, 1, 12),
    _PktcEScTapMediationNotificationEnable_Type()
)
pktcEScTapMediationNotificationEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEScTapMediationNotificationEnable.setStatus("current")
_PktcEScTapMediationStatus_Type = RowStatus
_PktcEScTapMediationStatus_Object = MibTableColumn
pktcEScTapMediationStatus = _PktcEScTapMediationStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 1, 1, 1, 2, 1, 13),
    _PktcEScTapMediationStatus_Type()
)
pktcEScTapMediationStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEScTapMediationStatus.setStatus("current")


class _PktcEScTapMediationCapabilities_Type(Bits):
    """Custom type pktcEScTapMediationCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("ipV4SrcInterface", 0),
          ("ipV6SrcInterface", 1),
          ("udp", 2))
    )

_PktcEScTapMediationCapabilities_Type.__name__ = "Bits"
_PktcEScTapMediationCapabilities_Object = MibScalar
pktcEScTapMediationCapabilities = _PktcEScTapMediationCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 1, 1, 1, 3),
    _PktcEScTapMediationCapabilities_Type()
)
pktcEScTapMediationCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEScTapMediationCapabilities.setStatus("current")
_PktcEScTapStreamGroup_ObjectIdentity = ObjectIdentity
pktcEScTapStreamGroup = _PktcEScTapStreamGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 1, 1, 2)
)
_PktcEScTapStreamTable_Object = MibTable
pktcEScTapStreamTable = _PktcEScTapStreamTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    pktcEScTapStreamTable.setStatus("current")
_PktcEScTapStreamEntry_Object = MibTableRow
pktcEScTapStreamEntry = _PktcEScTapStreamEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 1, 1, 2, 1, 1)
)
pktcEScTapStreamEntry.setIndexNames(
    (0, "PKTC-ES-TAP-MIB", "pktcEScTapMediationContentId"),
    (0, "PKTC-ES-TAP-MIB", "pktcEScTapStreamIndex"),
)
if mibBuilder.loadTexts:
    pktcEScTapStreamEntry.setStatus("current")


class _PktcEScTapStreamIndex_Type(Integer32):
    """Custom type pktcEScTapStreamIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PktcEScTapStreamIndex_Type.__name__ = "Integer32"
_PktcEScTapStreamIndex_Object = MibTableColumn
pktcEScTapStreamIndex = _PktcEScTapStreamIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 1, 1, 2, 1, 1, 1),
    _PktcEScTapStreamIndex_Type()
)
pktcEScTapStreamIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEScTapStreamIndex.setStatus("current")


class _PktcEScTapStreamType_Type(Integer32):
    """Custom type pktcEScTapStreamType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ip", 1),
          ("mac", 2),
          ("msPdsn", 4),
          ("userConnection", 3))
    )


_PktcEScTapStreamType_Type.__name__ = "Integer32"
_PktcEScTapStreamType_Object = MibTableColumn
pktcEScTapStreamType = _PktcEScTapStreamType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 1, 1, 2, 1, 1, 2),
    _PktcEScTapStreamType_Type()
)
pktcEScTapStreamType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEScTapStreamType.setStatus("current")


class _PktcEScTapStreamInterceptEnable_Type(TruthValue):
    """Custom type pktcEScTapStreamInterceptEnable based on TruthValue"""


_PktcEScTapStreamInterceptEnable_Object = MibTableColumn
pktcEScTapStreamInterceptEnable = _PktcEScTapStreamInterceptEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 1, 1, 2, 1, 1, 3),
    _PktcEScTapStreamInterceptEnable_Type()
)
pktcEScTapStreamInterceptEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEScTapStreamInterceptEnable.setStatus("current")
_PktcEScTapStreamInterceptedPackets_Type = Counter32
_PktcEScTapStreamInterceptedPackets_Object = MibTableColumn
pktcEScTapStreamInterceptedPackets = _PktcEScTapStreamInterceptedPackets_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 1, 1, 2, 1, 1, 4),
    _PktcEScTapStreamInterceptedPackets_Type()
)
pktcEScTapStreamInterceptedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEScTapStreamInterceptedPackets.setStatus("current")
_PktcEScTapStreamInterceptDrops_Type = Counter32
_PktcEScTapStreamInterceptDrops_Object = MibTableColumn
pktcEScTapStreamInterceptDrops = _PktcEScTapStreamInterceptDrops_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 1, 1, 2, 1, 1, 5),
    _PktcEScTapStreamInterceptDrops_Type()
)
pktcEScTapStreamInterceptDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEScTapStreamInterceptDrops.setStatus("current")
_PktcEScTapStreamStatus_Type = RowStatus
_PktcEScTapStreamStatus_Object = MibTableColumn
pktcEScTapStreamStatus = _PktcEScTapStreamStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 1, 1, 2, 1, 1, 6),
    _PktcEScTapStreamStatus_Type()
)
pktcEScTapStreamStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pktcEScTapStreamStatus.setStatus("current")
_PktcEScTapDebugGroup_ObjectIdentity = ObjectIdentity
pktcEScTapDebugGroup = _PktcEScTapDebugGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 1, 1, 3)
)


class _PktcEScTapDebugAge_Type(Integer32):
    """Custom type pktcEScTapDebugAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PktcEScTapDebugAge_Type.__name__ = "Integer32"
_PktcEScTapDebugAge_Object = MibScalar
pktcEScTapDebugAge = _PktcEScTapDebugAge_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 1, 1, 3, 1),
    _PktcEScTapDebugAge_Type()
)
pktcEScTapDebugAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEScTapDebugAge.setStatus("current")


class _PktcEScTapDebugMaxEntries_Type(Integer32):
    """Custom type pktcEScTapDebugMaxEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PktcEScTapDebugMaxEntries_Type.__name__ = "Integer32"
_PktcEScTapDebugMaxEntries_Object = MibScalar
pktcEScTapDebugMaxEntries = _PktcEScTapDebugMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 1, 1, 3, 2),
    _PktcEScTapDebugMaxEntries_Type()
)
pktcEScTapDebugMaxEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEScTapDebugMaxEntries.setStatus("current")
_PktcEScTapDebugTable_Object = MibTable
pktcEScTapDebugTable = _PktcEScTapDebugTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 1, 1, 3, 3)
)
if mibBuilder.loadTexts:
    pktcEScTapDebugTable.setStatus("current")
_PktcEScTapDebugEntry_Object = MibTableRow
pktcEScTapDebugEntry = _PktcEScTapDebugEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 1, 1, 3, 3, 1)
)
pktcEScTapDebugEntry.setIndexNames(
    (0, "PKTC-ES-TAP-MIB", "pktcEScTapDebugIndex"),
)
if mibBuilder.loadTexts:
    pktcEScTapDebugEntry.setStatus("current")


class _PktcEScTapDebugIndex_Type(Integer32):
    """Custom type pktcEScTapDebugIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PktcEScTapDebugIndex_Type.__name__ = "Integer32"
_PktcEScTapDebugIndex_Object = MibTableColumn
pktcEScTapDebugIndex = _PktcEScTapDebugIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 1, 1, 3, 3, 1, 1),
    _PktcEScTapDebugIndex_Type()
)
pktcEScTapDebugIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pktcEScTapDebugIndex.setStatus("current")
_PktcEScTapDebugMediationId_Type = Unsigned32
_PktcEScTapDebugMediationId_Object = MibTableColumn
pktcEScTapDebugMediationId = _PktcEScTapDebugMediationId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 1, 1, 3, 3, 1, 2),
    _PktcEScTapDebugMediationId_Type()
)
pktcEScTapDebugMediationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEScTapDebugMediationId.setStatus("current")
_PktcEScTapDebugStreamId_Type = Unsigned32
_PktcEScTapDebugStreamId_Object = MibTableColumn
pktcEScTapDebugStreamId = _PktcEScTapDebugStreamId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 1, 1, 3, 3, 1, 3),
    _PktcEScTapDebugStreamId_Type()
)
pktcEScTapDebugStreamId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEScTapDebugStreamId.setStatus("current")
_PktcEScTapDebugMessage_Type = SnmpAdminString
_PktcEScTapDebugMessage_Object = MibTableColumn
pktcEScTapDebugMessage = _PktcEScTapDebugMessage_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 1, 1, 3, 3, 1, 4),
    _PktcEScTapDebugMessage_Type()
)
pktcEScTapDebugMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pktcEScTapDebugMessage.setStatus("current")
_PktcEScTapDebugStatus_Type = RowStatus
_PktcEScTapDebugStatus_Object = MibTableColumn
pktcEScTapDebugStatus = _PktcEScTapDebugStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 1, 1, 3, 3, 1, 5),
    _PktcEScTapDebugStatus_Type()
)
pktcEScTapDebugStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pktcEScTapDebugStatus.setStatus("current")
_PktcESTapMibConform_ObjectIdentity = ObjectIdentity
pktcESTapMibConform = _PktcESTapMibConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 1, 2)
)
_PktcESTapMibCompliances_ObjectIdentity = ObjectIdentity
pktcESTapMibCompliances = _PktcESTapMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 1, 2, 1)
)
_PktcESTapMibGroups_ObjectIdentity = ObjectIdentity
pktcESTapMibGroups = _PktcESTapMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 1, 2, 2)
)

# Managed Objects groups

pktcESTapMediationComplianceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 1, 2, 2, 1)
)
pktcESTapMediationComplianceGroup.setObjects(
      *(("PKTC-ES-TAP-MIB", "pktcEScTapMediationNewIndex"),
        ("PKTC-ES-TAP-MIB", "pktcEScTapMediationDestAddressType"),
        ("PKTC-ES-TAP-MIB", "pktcEScTapMediationDestAddress"),
        ("PKTC-ES-TAP-MIB", "pktcEScTapMediationDestPort"),
        ("PKTC-ES-TAP-MIB", "pktcEScTapMediationSrcInterface"),
        ("PKTC-ES-TAP-MIB", "pktcEScTapMediationDscp"),
        ("PKTC-ES-TAP-MIB", "pktcEScTapMediationTimeout"),
        ("PKTC-ES-TAP-MIB", "pktcEScTapMediationTransport"),
        ("PKTC-ES-TAP-MIB", "pktcEScTapMediationNotificationEnable"),
        ("PKTC-ES-TAP-MIB", "pktcEScTapMediationStatus"))
)
if mibBuilder.loadTexts:
    pktcESTapMediationComplianceGroup.setStatus("current")

pktcESTapStreamComplianceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 1, 2, 2, 2)
)
pktcESTapStreamComplianceGroup.setObjects(
      *(("PKTC-ES-TAP-MIB", "pktcEScTapStreamType"),
        ("PKTC-ES-TAP-MIB", "pktcEScTapStreamInterceptEnable"),
        ("PKTC-ES-TAP-MIB", "pktcEScTapStreamInterceptedPackets"),
        ("PKTC-ES-TAP-MIB", "pktcEScTapStreamInterceptDrops"),
        ("PKTC-ES-TAP-MIB", "pktcEScTapStreamStatus"))
)
if mibBuilder.loadTexts:
    pktcESTapStreamComplianceGroup.setStatus("current")

pktcESTapMediationCpbComplianceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 1, 2, 2, 4)
)
pktcESTapMediationCpbComplianceGroup.setObjects(
    ("PKTC-ES-TAP-MIB", "pktcEScTapMediationCapabilities")
)
if mibBuilder.loadTexts:
    pktcESTapMediationCpbComplianceGroup.setStatus("current")

pktcESTapDebugComplianceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 1, 2, 2, 5)
)
pktcESTapDebugComplianceGroup.setObjects(
      *(("PKTC-ES-TAP-MIB", "pktcEScTapDebugAge"),
        ("PKTC-ES-TAP-MIB", "pktcEScTapDebugMaxEntries"),
        ("PKTC-ES-TAP-MIB", "pktcEScTapDebugMediationId"),
        ("PKTC-ES-TAP-MIB", "pktcEScTapDebugStreamId"),
        ("PKTC-ES-TAP-MIB", "pktcEScTapDebugMessage"),
        ("PKTC-ES-TAP-MIB", "pktcEScTapDebugStatus"))
)
if mibBuilder.loadTexts:
    pktcESTapDebugComplianceGroup.setStatus("current")


# Notification objects

pktcESTapMibActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 1, 0, 1)
)
pktcESTapMibActive.setObjects(
    ("PKTC-ES-TAP-MIB", "pktcEScTapStreamType")
)
if mibBuilder.loadTexts:
    pktcESTapMibActive.setStatus(
        "current"
    )

pktcESTapMediationTimedOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 1, 0, 2)
)
pktcESTapMediationTimedOut.setObjects(
    ("PKTC-ES-TAP-MIB", "pktcEScTapMediationStatus")
)
if mibBuilder.loadTexts:
    pktcESTapMediationTimedOut.setStatus(
        "current"
    )

pktcESTapMediationDebug = NotificationType(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 1, 0, 3)
)
pktcESTapMediationDebug.setObjects(
      *(("PKTC-ES-TAP-MIB", "pktcEScTapDebugMediationId"),
        ("PKTC-ES-TAP-MIB", "pktcEScTapDebugMessage"))
)
if mibBuilder.loadTexts:
    pktcESTapMediationDebug.setStatus(
        "current"
    )

pktcESTapStreamDebug = NotificationType(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 1, 0, 4)
)
pktcESTapStreamDebug.setObjects(
      *(("PKTC-ES-TAP-MIB", "pktcEScTapDebugMediationId"),
        ("PKTC-ES-TAP-MIB", "pktcEScTapDebugStreamId"),
        ("PKTC-ES-TAP-MIB", "pktcEScTapDebugMessage"))
)
if mibBuilder.loadTexts:
    pktcESTapStreamDebug.setStatus(
        "current"
    )

pktcESTapSwitchover = NotificationType(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 1, 0, 5)
)
if mibBuilder.loadTexts:
    pktcESTapSwitchover.setStatus(
        "current"
    )


# Notifications groups

pktcESTapNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 1, 2, 2, 3)
)
pktcESTapNotificationGroup.setObjects(
      *(("PKTC-ES-TAP-MIB", "pktcESTapMibActive"),
        ("PKTC-ES-TAP-MIB", "pktcESTapMediationTimedOut"),
        ("PKTC-ES-TAP-MIB", "pktcESTapMediationDebug"),
        ("PKTC-ES-TAP-MIB", "pktcESTapStreamDebug"),
        ("PKTC-ES-TAP-MIB", "pktcESTapSwitchover"))
)
if mibBuilder.loadTexts:
    pktcESTapNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

pktcESTapMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 2, 2, 9, 1, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    pktcESTapMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PKTC-ES-TAP-MIB",
    **{"PktcEScTapDscp": PktcEScTapDscp,
       "pktcESTapMib": pktcESTapMib,
       "pktcESTapMibNotifs": pktcESTapMibNotifs,
       "pktcESTapMibActive": pktcESTapMibActive,
       "pktcESTapMediationTimedOut": pktcESTapMediationTimedOut,
       "pktcESTapMediationDebug": pktcESTapMediationDebug,
       "pktcESTapStreamDebug": pktcESTapStreamDebug,
       "pktcESTapSwitchover": pktcESTapSwitchover,
       "pktcESTapMibObjects": pktcESTapMibObjects,
       "pktcEScTapMediationGroup": pktcEScTapMediationGroup,
       "pktcEScTapMediationNewIndex": pktcEScTapMediationNewIndex,
       "pktcEScTapMediationTable": pktcEScTapMediationTable,
       "pktcEScTapMediationEntry": pktcEScTapMediationEntry,
       "pktcEScTapMediationContentId": pktcEScTapMediationContentId,
       "pktcEScTapMediationDestAddressType": pktcEScTapMediationDestAddressType,
       "pktcEScTapMediationDestAddress": pktcEScTapMediationDestAddress,
       "pktcEScTapMediationDestPort": pktcEScTapMediationDestPort,
       "pktcEScTapMediationSrcInterface": pktcEScTapMediationSrcInterface,
       "pktcEScTapMediationDscp": pktcEScTapMediationDscp,
       "pktcEScTapMediationTimeout": pktcEScTapMediationTimeout,
       "pktcEScTapMediationTransport": pktcEScTapMediationTransport,
       "pktcEScTapMediationNotificationEnable": pktcEScTapMediationNotificationEnable,
       "pktcEScTapMediationStatus": pktcEScTapMediationStatus,
       "pktcEScTapMediationCapabilities": pktcEScTapMediationCapabilities,
       "pktcEScTapStreamGroup": pktcEScTapStreamGroup,
       "pktcEScTapStreamTable": pktcEScTapStreamTable,
       "pktcEScTapStreamEntry": pktcEScTapStreamEntry,
       "pktcEScTapStreamIndex": pktcEScTapStreamIndex,
       "pktcEScTapStreamType": pktcEScTapStreamType,
       "pktcEScTapStreamInterceptEnable": pktcEScTapStreamInterceptEnable,
       "pktcEScTapStreamInterceptedPackets": pktcEScTapStreamInterceptedPackets,
       "pktcEScTapStreamInterceptDrops": pktcEScTapStreamInterceptDrops,
       "pktcEScTapStreamStatus": pktcEScTapStreamStatus,
       "pktcEScTapDebugGroup": pktcEScTapDebugGroup,
       "pktcEScTapDebugAge": pktcEScTapDebugAge,
       "pktcEScTapDebugMaxEntries": pktcEScTapDebugMaxEntries,
       "pktcEScTapDebugTable": pktcEScTapDebugTable,
       "pktcEScTapDebugEntry": pktcEScTapDebugEntry,
       "pktcEScTapDebugIndex": pktcEScTapDebugIndex,
       "pktcEScTapDebugMediationId": pktcEScTapDebugMediationId,
       "pktcEScTapDebugStreamId": pktcEScTapDebugStreamId,
       "pktcEScTapDebugMessage": pktcEScTapDebugMessage,
       "pktcEScTapDebugStatus": pktcEScTapDebugStatus,
       "pktcESTapMibConform": pktcESTapMibConform,
       "pktcESTapMibCompliances": pktcESTapMibCompliances,
       "pktcESTapMibCompliance": pktcESTapMibCompliance,
       "pktcESTapMibGroups": pktcESTapMibGroups,
       "pktcESTapMediationComplianceGroup": pktcESTapMediationComplianceGroup,
       "pktcESTapStreamComplianceGroup": pktcESTapStreamComplianceGroup,
       "pktcESTapNotificationGroup": pktcESTapNotificationGroup,
       "pktcESTapMediationCpbComplianceGroup": pktcESTapMediationCpbComplianceGroup,
       "pktcESTapDebugComplianceGroup": pktcESTapDebugComplianceGroup}
)
