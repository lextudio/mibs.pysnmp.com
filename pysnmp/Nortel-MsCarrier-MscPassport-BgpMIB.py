# SNMP MIB module (Nortel-MsCarrier-MscPassport-BgpMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-MsCarrier-MscPassport-BgpMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:32:00 2024
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

(mscVrIp,
 mscVrIpIndex) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-IpMIB",
    "mscVrIp",
    "mscVrIpIndex")

(Counter32,
 DisplayString,
 Gauge32,
 Integer32,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-StandardTextualConventionsMIB",
    "Counter32",
    "DisplayString",
    "Gauge32",
    "Integer32",
    "RowStatus",
    "StorageType",
    "Unsigned32")

(AsciiString,
 Hex,
 HexString,
 IntegerSequence,
 NonReplicated) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-TextualConventionsMIB",
    "AsciiString",
    "Hex",
    "HexString",
    "IntegerSequence",
    "NonReplicated")

(mscPassportMIBs,) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-UsefulDefinitionsMIB",
    "mscPassportMIBs")

(mscVrIndex,) = mibBuilder.importSymbols(
    "Nortel-MsCarrier-MscPassport-VirtualRouterMIB",
    "mscVrIndex")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MscVrIpBgp_ObjectIdentity = ObjectIdentity
mscVrIpBgp = _MscVrIpBgp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21)
)
_MscVrIpBgpRowStatusTable_Object = MibTable
mscVrIpBgpRowStatusTable = _MscVrIpBgpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 1)
)
if mibBuilder.loadTexts:
    mscVrIpBgpRowStatusTable.setStatus("mandatory")
_MscVrIpBgpRowStatusEntry_Object = MibTableRow
mscVrIpBgpRowStatusEntry = _MscVrIpBgpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 1, 1)
)
mscVrIpBgpRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpBgpRowStatusEntry.setStatus("mandatory")
_MscVrIpBgpRowStatus_Type = RowStatus
_MscVrIpBgpRowStatus_Object = MibTableColumn
mscVrIpBgpRowStatus = _MscVrIpBgpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 1, 1, 1),
    _MscVrIpBgpRowStatus_Type()
)
mscVrIpBgpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpBgpRowStatus.setStatus("mandatory")
_MscVrIpBgpComponentName_Type = DisplayString
_MscVrIpBgpComponentName_Object = MibTableColumn
mscVrIpBgpComponentName = _MscVrIpBgpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 1, 1, 2),
    _MscVrIpBgpComponentName_Type()
)
mscVrIpBgpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpComponentName.setStatus("mandatory")
_MscVrIpBgpStorageType_Type = StorageType
_MscVrIpBgpStorageType_Object = MibTableColumn
mscVrIpBgpStorageType = _MscVrIpBgpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 1, 1, 4),
    _MscVrIpBgpStorageType_Type()
)
mscVrIpBgpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpStorageType.setStatus("mandatory")
_MscVrIpBgpIndex_Type = NonReplicated
_MscVrIpBgpIndex_Object = MibTableColumn
mscVrIpBgpIndex = _MscVrIpBgpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 1, 1, 10),
    _MscVrIpBgpIndex_Type()
)
mscVrIpBgpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpBgpIndex.setStatus("mandatory")
_MscVrIpBgpPeer_ObjectIdentity = ObjectIdentity
mscVrIpBgpPeer = _MscVrIpBgpPeer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 2)
)
_MscVrIpBgpPeerRowStatusTable_Object = MibTable
mscVrIpBgpPeerRowStatusTable = _MscVrIpBgpPeerRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 2, 1)
)
if mibBuilder.loadTexts:
    mscVrIpBgpPeerRowStatusTable.setStatus("mandatory")
_MscVrIpBgpPeerRowStatusEntry_Object = MibTableRow
mscVrIpBgpPeerRowStatusEntry = _MscVrIpBgpPeerRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 2, 1, 1)
)
mscVrIpBgpPeerRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpPeerPeerAddressIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpBgpPeerRowStatusEntry.setStatus("mandatory")
_MscVrIpBgpPeerRowStatus_Type = RowStatus
_MscVrIpBgpPeerRowStatus_Object = MibTableColumn
mscVrIpBgpPeerRowStatus = _MscVrIpBgpPeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 2, 1, 1, 1),
    _MscVrIpBgpPeerRowStatus_Type()
)
mscVrIpBgpPeerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpBgpPeerRowStatus.setStatus("mandatory")
_MscVrIpBgpPeerComponentName_Type = DisplayString
_MscVrIpBgpPeerComponentName_Object = MibTableColumn
mscVrIpBgpPeerComponentName = _MscVrIpBgpPeerComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 2, 1, 1, 2),
    _MscVrIpBgpPeerComponentName_Type()
)
mscVrIpBgpPeerComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpPeerComponentName.setStatus("mandatory")
_MscVrIpBgpPeerStorageType_Type = StorageType
_MscVrIpBgpPeerStorageType_Object = MibTableColumn
mscVrIpBgpPeerStorageType = _MscVrIpBgpPeerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 2, 1, 1, 4),
    _MscVrIpBgpPeerStorageType_Type()
)
mscVrIpBgpPeerStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpPeerStorageType.setStatus("mandatory")
_MscVrIpBgpPeerPeerAddressIndex_Type = IpAddress
_MscVrIpBgpPeerPeerAddressIndex_Object = MibTableColumn
mscVrIpBgpPeerPeerAddressIndex = _MscVrIpBgpPeerPeerAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 2, 1, 1, 10),
    _MscVrIpBgpPeerPeerAddressIndex_Type()
)
mscVrIpBgpPeerPeerAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpBgpPeerPeerAddressIndex.setStatus("mandatory")
_MscVrIpBgpPeerProvTable_Object = MibTable
mscVrIpBgpPeerProvTable = _MscVrIpBgpPeerProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 2, 10)
)
if mibBuilder.loadTexts:
    mscVrIpBgpPeerProvTable.setStatus("mandatory")
_MscVrIpBgpPeerProvEntry_Object = MibTableRow
mscVrIpBgpPeerProvEntry = _MscVrIpBgpPeerProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 2, 10, 1)
)
mscVrIpBgpPeerProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpPeerPeerAddressIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpBgpPeerProvEntry.setStatus("mandatory")


class _MscVrIpBgpPeerPeerAs_Type(Unsigned32):
    """Custom type mscVrIpBgpPeerPeerAs based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVrIpBgpPeerPeerAs_Type.__name__ = "Unsigned32"
_MscVrIpBgpPeerPeerAs_Object = MibTableColumn
mscVrIpBgpPeerPeerAs = _MscVrIpBgpPeerPeerAs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 2, 10, 1, 1),
    _MscVrIpBgpPeerPeerAs_Type()
)
mscVrIpBgpPeerPeerAs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpBgpPeerPeerAs.setStatus("mandatory")


class _MscVrIpBgpPeerLocalAddressConfigured_Type(IpAddress):
    """Custom type mscVrIpBgpPeerLocalAddressConfigured based on IpAddress"""
    defaultHexValue = "00000000"


_MscVrIpBgpPeerLocalAddressConfigured_Object = MibTableColumn
mscVrIpBgpPeerLocalAddressConfigured = _MscVrIpBgpPeerLocalAddressConfigured_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 2, 10, 1, 2),
    _MscVrIpBgpPeerLocalAddressConfigured_Type()
)
mscVrIpBgpPeerLocalAddressConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpBgpPeerLocalAddressConfigured.setStatus("mandatory")


class _MscVrIpBgpPeerKeepAliveConfigured_Type(Unsigned32):
    """Custom type mscVrIpBgpPeerKeepAliveConfigured based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 21845),
    )


_MscVrIpBgpPeerKeepAliveConfigured_Type.__name__ = "Unsigned32"
_MscVrIpBgpPeerKeepAliveConfigured_Object = MibTableColumn
mscVrIpBgpPeerKeepAliveConfigured = _MscVrIpBgpPeerKeepAliveConfigured_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 2, 10, 1, 3),
    _MscVrIpBgpPeerKeepAliveConfigured_Type()
)
mscVrIpBgpPeerKeepAliveConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpBgpPeerKeepAliveConfigured.setStatus("mandatory")


class _MscVrIpBgpPeerHoldTimeConfigured_Type(Unsigned32):
    """Custom type mscVrIpBgpPeerHoldTimeConfigured based on Unsigned32"""
    defaultValue = 90

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 65535),
    )


_MscVrIpBgpPeerHoldTimeConfigured_Type.__name__ = "Unsigned32"
_MscVrIpBgpPeerHoldTimeConfigured_Object = MibTableColumn
mscVrIpBgpPeerHoldTimeConfigured = _MscVrIpBgpPeerHoldTimeConfigured_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 2, 10, 1, 4),
    _MscVrIpBgpPeerHoldTimeConfigured_Type()
)
mscVrIpBgpPeerHoldTimeConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpBgpPeerHoldTimeConfigured.setStatus("mandatory")


class _MscVrIpBgpPeerConnectRetryTime_Type(Unsigned32):
    """Custom type mscVrIpBgpPeerConnectRetryTime based on Unsigned32"""
    defaultValue = 120

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscVrIpBgpPeerConnectRetryTime_Type.__name__ = "Unsigned32"
_MscVrIpBgpPeerConnectRetryTime_Object = MibTableColumn
mscVrIpBgpPeerConnectRetryTime = _MscVrIpBgpPeerConnectRetryTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 2, 10, 1, 5),
    _MscVrIpBgpPeerConnectRetryTime_Type()
)
mscVrIpBgpPeerConnectRetryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpBgpPeerConnectRetryTime.setStatus("mandatory")


class _MscVrIpBgpPeerMinAsOrigTime_Type(Unsigned32):
    """Custom type mscVrIpBgpPeerMinAsOrigTime based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscVrIpBgpPeerMinAsOrigTime_Type.__name__ = "Unsigned32"
_MscVrIpBgpPeerMinAsOrigTime_Object = MibTableColumn
mscVrIpBgpPeerMinAsOrigTime = _MscVrIpBgpPeerMinAsOrigTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 2, 10, 1, 6),
    _MscVrIpBgpPeerMinAsOrigTime_Type()
)
mscVrIpBgpPeerMinAsOrigTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpBgpPeerMinAsOrigTime.setStatus("mandatory")


class _MscVrIpBgpPeerMinRouteAdvTime_Type(Unsigned32):
    """Custom type mscVrIpBgpPeerMinRouteAdvTime based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_MscVrIpBgpPeerMinRouteAdvTime_Type.__name__ = "Unsigned32"
_MscVrIpBgpPeerMinRouteAdvTime_Object = MibTableColumn
mscVrIpBgpPeerMinRouteAdvTime = _MscVrIpBgpPeerMinRouteAdvTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 2, 10, 1, 7),
    _MscVrIpBgpPeerMinRouteAdvTime_Type()
)
mscVrIpBgpPeerMinRouteAdvTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpBgpPeerMinRouteAdvTime.setStatus("mandatory")


class _MscVrIpBgpPeerDefaultInAggMed_Type(Unsigned32):
    """Custom type mscVrIpBgpPeerDefaultInAggMed based on Unsigned32"""
    defaultValue = 4294967295

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrIpBgpPeerDefaultInAggMed_Type.__name__ = "Unsigned32"
_MscVrIpBgpPeerDefaultInAggMed_Object = MibTableColumn
mscVrIpBgpPeerDefaultInAggMed = _MscVrIpBgpPeerDefaultInAggMed_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 2, 10, 1, 8),
    _MscVrIpBgpPeerDefaultInAggMed_Type()
)
mscVrIpBgpPeerDefaultInAggMed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpBgpPeerDefaultInAggMed.setStatus("mandatory")


class _MscVrIpBgpPeerIsRouteReflectorClient_Type(Integer32):
    """Custom type mscVrIpBgpPeerIsRouteReflectorClient based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_MscVrIpBgpPeerIsRouteReflectorClient_Type.__name__ = "Integer32"
_MscVrIpBgpPeerIsRouteReflectorClient_Object = MibTableColumn
mscVrIpBgpPeerIsRouteReflectorClient = _MscVrIpBgpPeerIsRouteReflectorClient_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 2, 10, 1, 9),
    _MscVrIpBgpPeerIsRouteReflectorClient_Type()
)
mscVrIpBgpPeerIsRouteReflectorClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpBgpPeerIsRouteReflectorClient.setStatus("mandatory")


class _MscVrIpBgpPeerRemovePrivateAs_Type(Integer32):
    """Custom type mscVrIpBgpPeerRemovePrivateAs based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_MscVrIpBgpPeerRemovePrivateAs_Type.__name__ = "Integer32"
_MscVrIpBgpPeerRemovePrivateAs_Object = MibTableColumn
mscVrIpBgpPeerRemovePrivateAs = _MscVrIpBgpPeerRemovePrivateAs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 2, 10, 1, 10),
    _MscVrIpBgpPeerRemovePrivateAs_Type()
)
mscVrIpBgpPeerRemovePrivateAs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpBgpPeerRemovePrivateAs.setStatus("mandatory")
_MscVrIpBgpPeerStateTable_Object = MibTable
mscVrIpBgpPeerStateTable = _MscVrIpBgpPeerStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 2, 11)
)
if mibBuilder.loadTexts:
    mscVrIpBgpPeerStateTable.setStatus("mandatory")
_MscVrIpBgpPeerStateEntry_Object = MibTableRow
mscVrIpBgpPeerStateEntry = _MscVrIpBgpPeerStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 2, 11, 1)
)
mscVrIpBgpPeerStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpPeerPeerAddressIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpBgpPeerStateEntry.setStatus("mandatory")


class _MscVrIpBgpPeerAdminState_Type(Integer32):
    """Custom type mscVrIpBgpPeerAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("shuttingDown", 2),
          ("unlocked", 1))
    )


_MscVrIpBgpPeerAdminState_Type.__name__ = "Integer32"
_MscVrIpBgpPeerAdminState_Object = MibTableColumn
mscVrIpBgpPeerAdminState = _MscVrIpBgpPeerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 2, 11, 1, 1),
    _MscVrIpBgpPeerAdminState_Type()
)
mscVrIpBgpPeerAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpPeerAdminState.setStatus("mandatory")


class _MscVrIpBgpPeerOperationalState_Type(Integer32):
    """Custom type mscVrIpBgpPeerOperationalState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_MscVrIpBgpPeerOperationalState_Type.__name__ = "Integer32"
_MscVrIpBgpPeerOperationalState_Object = MibTableColumn
mscVrIpBgpPeerOperationalState = _MscVrIpBgpPeerOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 2, 11, 1, 2),
    _MscVrIpBgpPeerOperationalState_Type()
)
mscVrIpBgpPeerOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpPeerOperationalState.setStatus("mandatory")


class _MscVrIpBgpPeerUsageState_Type(Integer32):
    """Custom type mscVrIpBgpPeerUsageState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("busy", 2),
          ("idle", 0))
    )


_MscVrIpBgpPeerUsageState_Type.__name__ = "Integer32"
_MscVrIpBgpPeerUsageState_Object = MibTableColumn
mscVrIpBgpPeerUsageState = _MscVrIpBgpPeerUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 2, 11, 1, 3),
    _MscVrIpBgpPeerUsageState_Type()
)
mscVrIpBgpPeerUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpPeerUsageState.setStatus("mandatory")
_MscVrIpBgpPeerOperTable_Object = MibTable
mscVrIpBgpPeerOperTable = _MscVrIpBgpPeerOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 2, 12)
)
if mibBuilder.loadTexts:
    mscVrIpBgpPeerOperTable.setStatus("mandatory")
_MscVrIpBgpPeerOperEntry_Object = MibTableRow
mscVrIpBgpPeerOperEntry = _MscVrIpBgpPeerOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 2, 12, 1)
)
mscVrIpBgpPeerOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpPeerPeerAddressIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpBgpPeerOperEntry.setStatus("mandatory")


class _MscVrIpBgpPeerConnectionState_Type(Integer32):
    """Custom type mscVrIpBgpPeerConnectionState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("connect", 2),
          ("established", 6),
          ("idle", 1),
          ("openConfirm", 5),
          ("openSent", 4))
    )


_MscVrIpBgpPeerConnectionState_Type.__name__ = "Integer32"
_MscVrIpBgpPeerConnectionState_Object = MibTableColumn
mscVrIpBgpPeerConnectionState = _MscVrIpBgpPeerConnectionState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 2, 12, 1, 3),
    _MscVrIpBgpPeerConnectionState_Type()
)
mscVrIpBgpPeerConnectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpPeerConnectionState.setStatus("mandatory")
_MscVrIpBgpPeerBgpIdentifier_Type = IpAddress
_MscVrIpBgpPeerBgpIdentifier_Object = MibTableColumn
mscVrIpBgpPeerBgpIdentifier = _MscVrIpBgpPeerBgpIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 2, 12, 1, 4),
    _MscVrIpBgpPeerBgpIdentifier_Type()
)
mscVrIpBgpPeerBgpIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpPeerBgpIdentifier.setStatus("mandatory")


class _MscVrIpBgpPeerVersionNegotiated_Type(Unsigned32):
    """Custom type mscVrIpBgpPeerVersionNegotiated based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_MscVrIpBgpPeerVersionNegotiated_Type.__name__ = "Unsigned32"
_MscVrIpBgpPeerVersionNegotiated_Object = MibTableColumn
mscVrIpBgpPeerVersionNegotiated = _MscVrIpBgpPeerVersionNegotiated_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 2, 12, 1, 5),
    _MscVrIpBgpPeerVersionNegotiated_Type()
)
mscVrIpBgpPeerVersionNegotiated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpPeerVersionNegotiated.setStatus("mandatory")


class _MscVrIpBgpPeerHoldTimeNegotiated_Type(Unsigned32):
    """Custom type mscVrIpBgpPeerHoldTimeNegotiated based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 65535),
    )


_MscVrIpBgpPeerHoldTimeNegotiated_Type.__name__ = "Unsigned32"
_MscVrIpBgpPeerHoldTimeNegotiated_Object = MibTableColumn
mscVrIpBgpPeerHoldTimeNegotiated = _MscVrIpBgpPeerHoldTimeNegotiated_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 2, 12, 1, 6),
    _MscVrIpBgpPeerHoldTimeNegotiated_Type()
)
mscVrIpBgpPeerHoldTimeNegotiated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpPeerHoldTimeNegotiated.setStatus("mandatory")


class _MscVrIpBgpPeerKeepAliveNegotiated_Type(Unsigned32):
    """Custom type mscVrIpBgpPeerKeepAliveNegotiated based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 21845),
    )


_MscVrIpBgpPeerKeepAliveNegotiated_Type.__name__ = "Unsigned32"
_MscVrIpBgpPeerKeepAliveNegotiated_Object = MibTableColumn
mscVrIpBgpPeerKeepAliveNegotiated = _MscVrIpBgpPeerKeepAliveNegotiated_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 2, 12, 1, 7),
    _MscVrIpBgpPeerKeepAliveNegotiated_Type()
)
mscVrIpBgpPeerKeepAliveNegotiated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpPeerKeepAliveNegotiated.setStatus("mandatory")
_MscVrIpBgpPeerLocalAddressUsed_Type = IpAddress
_MscVrIpBgpPeerLocalAddressUsed_Object = MibTableColumn
mscVrIpBgpPeerLocalAddressUsed = _MscVrIpBgpPeerLocalAddressUsed_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 2, 12, 1, 8),
    _MscVrIpBgpPeerLocalAddressUsed_Type()
)
mscVrIpBgpPeerLocalAddressUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpPeerLocalAddressUsed.setStatus("mandatory")


class _MscVrIpBgpPeerLocalPort_Type(Unsigned32):
    """Custom type mscVrIpBgpPeerLocalPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVrIpBgpPeerLocalPort_Type.__name__ = "Unsigned32"
_MscVrIpBgpPeerLocalPort_Object = MibTableColumn
mscVrIpBgpPeerLocalPort = _MscVrIpBgpPeerLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 2, 12, 1, 9),
    _MscVrIpBgpPeerLocalPort_Type()
)
mscVrIpBgpPeerLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpPeerLocalPort.setStatus("mandatory")


class _MscVrIpBgpPeerRemotePort_Type(Unsigned32):
    """Custom type mscVrIpBgpPeerRemotePort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVrIpBgpPeerRemotePort_Type.__name__ = "Unsigned32"
_MscVrIpBgpPeerRemotePort_Object = MibTableColumn
mscVrIpBgpPeerRemotePort = _MscVrIpBgpPeerRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 2, 12, 1, 10),
    _MscVrIpBgpPeerRemotePort_Type()
)
mscVrIpBgpPeerRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpPeerRemotePort.setStatus("mandatory")


class _MscVrIpBgpPeerLastError_Type(HexString):
    """Custom type mscVrIpBgpPeerLastError based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_MscVrIpBgpPeerLastError_Type.__name__ = "HexString"
_MscVrIpBgpPeerLastError_Object = MibTableColumn
mscVrIpBgpPeerLastError = _MscVrIpBgpPeerLastError_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 2, 12, 1, 11),
    _MscVrIpBgpPeerLastError_Type()
)
mscVrIpBgpPeerLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpPeerLastError.setStatus("mandatory")


class _MscVrIpBgpPeerConnectionEstablishedTime_Type(Gauge32):
    """Custom type mscVrIpBgpPeerConnectionEstablishedTime based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrIpBgpPeerConnectionEstablishedTime_Type.__name__ = "Gauge32"
_MscVrIpBgpPeerConnectionEstablishedTime_Object = MibTableColumn
mscVrIpBgpPeerConnectionEstablishedTime = _MscVrIpBgpPeerConnectionEstablishedTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 2, 12, 1, 12),
    _MscVrIpBgpPeerConnectionEstablishedTime_Type()
)
mscVrIpBgpPeerConnectionEstablishedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpPeerConnectionEstablishedTime.setStatus("mandatory")
_MscVrIpBgpPeerConnectionEstablishedTransitions_Type = Counter32
_MscVrIpBgpPeerConnectionEstablishedTransitions_Object = MibTableColumn
mscVrIpBgpPeerConnectionEstablishedTransitions = _MscVrIpBgpPeerConnectionEstablishedTransitions_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 2, 12, 1, 13),
    _MscVrIpBgpPeerConnectionEstablishedTransitions_Type()
)
mscVrIpBgpPeerConnectionEstablishedTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpPeerConnectionEstablishedTransitions.setStatus("mandatory")


class _MscVrIpBgpPeerInUpdateElapsedTime_Type(Gauge32):
    """Custom type mscVrIpBgpPeerInUpdateElapsedTime based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrIpBgpPeerInUpdateElapsedTime_Type.__name__ = "Gauge32"
_MscVrIpBgpPeerInUpdateElapsedTime_Object = MibTableColumn
mscVrIpBgpPeerInUpdateElapsedTime = _MscVrIpBgpPeerInUpdateElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 2, 12, 1, 14),
    _MscVrIpBgpPeerInUpdateElapsedTime_Type()
)
mscVrIpBgpPeerInUpdateElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpPeerInUpdateElapsedTime.setStatus("mandatory")
_MscVrIpBgpPeerInMsgs_Type = Counter32
_MscVrIpBgpPeerInMsgs_Object = MibTableColumn
mscVrIpBgpPeerInMsgs = _MscVrIpBgpPeerInMsgs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 2, 12, 1, 15),
    _MscVrIpBgpPeerInMsgs_Type()
)
mscVrIpBgpPeerInMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpPeerInMsgs.setStatus("mandatory")
_MscVrIpBgpPeerInUpdates_Type = Counter32
_MscVrIpBgpPeerInUpdates_Object = MibTableColumn
mscVrIpBgpPeerInUpdates = _MscVrIpBgpPeerInUpdates_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 2, 12, 1, 16),
    _MscVrIpBgpPeerInUpdates_Type()
)
mscVrIpBgpPeerInUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpPeerInUpdates.setStatus("mandatory")
_MscVrIpBgpPeerInErrors_Type = Counter32
_MscVrIpBgpPeerInErrors_Object = MibTableColumn
mscVrIpBgpPeerInErrors = _MscVrIpBgpPeerInErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 2, 12, 1, 17),
    _MscVrIpBgpPeerInErrors_Type()
)
mscVrIpBgpPeerInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpPeerInErrors.setStatus("mandatory")
_MscVrIpBgpPeerInErrorMsgs_Type = Counter32
_MscVrIpBgpPeerInErrorMsgs_Object = MibTableColumn
mscVrIpBgpPeerInErrorMsgs = _MscVrIpBgpPeerInErrorMsgs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 2, 12, 1, 18),
    _MscVrIpBgpPeerInErrorMsgs_Type()
)
mscVrIpBgpPeerInErrorMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpPeerInErrorMsgs.setStatus("mandatory")
_MscVrIpBgpPeerOutMsgs_Type = Counter32
_MscVrIpBgpPeerOutMsgs_Object = MibTableColumn
mscVrIpBgpPeerOutMsgs = _MscVrIpBgpPeerOutMsgs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 2, 12, 1, 19),
    _MscVrIpBgpPeerOutMsgs_Type()
)
mscVrIpBgpPeerOutMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpPeerOutMsgs.setStatus("mandatory")
_MscVrIpBgpPeerOutUpdates_Type = Counter32
_MscVrIpBgpPeerOutUpdates_Object = MibTableColumn
mscVrIpBgpPeerOutUpdates = _MscVrIpBgpPeerOutUpdates_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 2, 12, 1, 20),
    _MscVrIpBgpPeerOutUpdates_Type()
)
mscVrIpBgpPeerOutUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpPeerOutUpdates.setStatus("mandatory")
_MscVrIpBgpPeerOutDiscards_Type = Counter32
_MscVrIpBgpPeerOutDiscards_Object = MibTableColumn
mscVrIpBgpPeerOutDiscards = _MscVrIpBgpPeerOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 2, 12, 1, 21),
    _MscVrIpBgpPeerOutDiscards_Type()
)
mscVrIpBgpPeerOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpPeerOutDiscards.setStatus("mandatory")
_MscVrIpBgpPeerOutErrorMsgs_Type = Counter32
_MscVrIpBgpPeerOutErrorMsgs_Object = MibTableColumn
mscVrIpBgpPeerOutErrorMsgs = _MscVrIpBgpPeerOutErrorMsgs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 2, 12, 1, 22),
    _MscVrIpBgpPeerOutErrorMsgs_Type()
)
mscVrIpBgpPeerOutErrorMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpPeerOutErrorMsgs.setStatus("mandatory")
_MscVrIpBgpPeerInRoutes_Type = Counter32
_MscVrIpBgpPeerInRoutes_Object = MibTableColumn
mscVrIpBgpPeerInRoutes = _MscVrIpBgpPeerInRoutes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 2, 12, 1, 23),
    _MscVrIpBgpPeerInRoutes_Type()
)
mscVrIpBgpPeerInRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpPeerInRoutes.setStatus("mandatory")
_MscVrIpBgpImport_ObjectIdentity = ObjectIdentity
mscVrIpBgpImport = _MscVrIpBgpImport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 3)
)
_MscVrIpBgpImportRowStatusTable_Object = MibTable
mscVrIpBgpImportRowStatusTable = _MscVrIpBgpImportRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 3, 1)
)
if mibBuilder.loadTexts:
    mscVrIpBgpImportRowStatusTable.setStatus("mandatory")
_MscVrIpBgpImportRowStatusEntry_Object = MibTableRow
mscVrIpBgpImportRowStatusEntry = _MscVrIpBgpImportRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 3, 1, 1)
)
mscVrIpBgpImportRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpImportIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpBgpImportRowStatusEntry.setStatus("mandatory")
_MscVrIpBgpImportRowStatus_Type = RowStatus
_MscVrIpBgpImportRowStatus_Object = MibTableColumn
mscVrIpBgpImportRowStatus = _MscVrIpBgpImportRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 3, 1, 1, 1),
    _MscVrIpBgpImportRowStatus_Type()
)
mscVrIpBgpImportRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpBgpImportRowStatus.setStatus("mandatory")
_MscVrIpBgpImportComponentName_Type = DisplayString
_MscVrIpBgpImportComponentName_Object = MibTableColumn
mscVrIpBgpImportComponentName = _MscVrIpBgpImportComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 3, 1, 1, 2),
    _MscVrIpBgpImportComponentName_Type()
)
mscVrIpBgpImportComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpImportComponentName.setStatus("mandatory")
_MscVrIpBgpImportStorageType_Type = StorageType
_MscVrIpBgpImportStorageType_Object = MibTableColumn
mscVrIpBgpImportStorageType = _MscVrIpBgpImportStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 3, 1, 1, 4),
    _MscVrIpBgpImportStorageType_Type()
)
mscVrIpBgpImportStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpImportStorageType.setStatus("mandatory")


class _MscVrIpBgpImportIndex_Type(Integer32):
    """Custom type mscVrIpBgpImportIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVrIpBgpImportIndex_Type.__name__ = "Integer32"
_MscVrIpBgpImportIndex_Object = MibTableColumn
mscVrIpBgpImportIndex = _MscVrIpBgpImportIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 3, 1, 1, 10),
    _MscVrIpBgpImportIndex_Type()
)
mscVrIpBgpImportIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpBgpImportIndex.setStatus("mandatory")
_MscVrIpBgpImportNet_ObjectIdentity = ObjectIdentity
mscVrIpBgpImportNet = _MscVrIpBgpImportNet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 3, 2)
)
_MscVrIpBgpImportNetRowStatusTable_Object = MibTable
mscVrIpBgpImportNetRowStatusTable = _MscVrIpBgpImportNetRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 3, 2, 1)
)
if mibBuilder.loadTexts:
    mscVrIpBgpImportNetRowStatusTable.setStatus("mandatory")
_MscVrIpBgpImportNetRowStatusEntry_Object = MibTableRow
mscVrIpBgpImportNetRowStatusEntry = _MscVrIpBgpImportNetRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 3, 2, 1, 1)
)
mscVrIpBgpImportNetRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpImportIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpImportNetIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpBgpImportNetRowStatusEntry.setStatus("mandatory")
_MscVrIpBgpImportNetRowStatus_Type = RowStatus
_MscVrIpBgpImportNetRowStatus_Object = MibTableColumn
mscVrIpBgpImportNetRowStatus = _MscVrIpBgpImportNetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 3, 2, 1, 1, 1),
    _MscVrIpBgpImportNetRowStatus_Type()
)
mscVrIpBgpImportNetRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpBgpImportNetRowStatus.setStatus("mandatory")
_MscVrIpBgpImportNetComponentName_Type = DisplayString
_MscVrIpBgpImportNetComponentName_Object = MibTableColumn
mscVrIpBgpImportNetComponentName = _MscVrIpBgpImportNetComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 3, 2, 1, 1, 2),
    _MscVrIpBgpImportNetComponentName_Type()
)
mscVrIpBgpImportNetComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpImportNetComponentName.setStatus("mandatory")
_MscVrIpBgpImportNetStorageType_Type = StorageType
_MscVrIpBgpImportNetStorageType_Object = MibTableColumn
mscVrIpBgpImportNetStorageType = _MscVrIpBgpImportNetStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 3, 2, 1, 1, 4),
    _MscVrIpBgpImportNetStorageType_Type()
)
mscVrIpBgpImportNetStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpImportNetStorageType.setStatus("mandatory")


class _MscVrIpBgpImportNetIndex_Type(Integer32):
    """Custom type mscVrIpBgpImportNetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVrIpBgpImportNetIndex_Type.__name__ = "Integer32"
_MscVrIpBgpImportNetIndex_Object = MibTableColumn
mscVrIpBgpImportNetIndex = _MscVrIpBgpImportNetIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 3, 2, 1, 1, 10),
    _MscVrIpBgpImportNetIndex_Type()
)
mscVrIpBgpImportNetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpBgpImportNetIndex.setStatus("mandatory")
_MscVrIpBgpImportNetProvTable_Object = MibTable
mscVrIpBgpImportNetProvTable = _MscVrIpBgpImportNetProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 3, 2, 10)
)
if mibBuilder.loadTexts:
    mscVrIpBgpImportNetProvTable.setStatus("mandatory")
_MscVrIpBgpImportNetProvEntry_Object = MibTableRow
mscVrIpBgpImportNetProvEntry = _MscVrIpBgpImportNetProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 3, 2, 10, 1)
)
mscVrIpBgpImportNetProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpImportIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpImportNetIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpBgpImportNetProvEntry.setStatus("mandatory")
_MscVrIpBgpImportNetPrefix_Type = IpAddress
_MscVrIpBgpImportNetPrefix_Object = MibTableColumn
mscVrIpBgpImportNetPrefix = _MscVrIpBgpImportNetPrefix_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 3, 2, 10, 1, 1),
    _MscVrIpBgpImportNetPrefix_Type()
)
mscVrIpBgpImportNetPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpBgpImportNetPrefix.setStatus("mandatory")


class _MscVrIpBgpImportNetLength_Type(Unsigned32):
    """Custom type mscVrIpBgpImportNetLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_MscVrIpBgpImportNetLength_Type.__name__ = "Unsigned32"
_MscVrIpBgpImportNetLength_Object = MibTableColumn
mscVrIpBgpImportNetLength = _MscVrIpBgpImportNetLength_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 3, 2, 10, 1, 2),
    _MscVrIpBgpImportNetLength_Type()
)
mscVrIpBgpImportNetLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpBgpImportNetLength.setStatus("mandatory")
_MscVrIpBgpImportProvTable_Object = MibTable
mscVrIpBgpImportProvTable = _MscVrIpBgpImportProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 3, 10)
)
if mibBuilder.loadTexts:
    mscVrIpBgpImportProvTable.setStatus("mandatory")
_MscVrIpBgpImportProvEntry_Object = MibTableRow
mscVrIpBgpImportProvEntry = _MscVrIpBgpImportProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 3, 10, 1)
)
mscVrIpBgpImportProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpImportIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpBgpImportProvEntry.setStatus("mandatory")


class _MscVrIpBgpImportPeerAs_Type(Unsigned32):
    """Custom type mscVrIpBgpImportPeerAs based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVrIpBgpImportPeerAs_Type.__name__ = "Unsigned32"
_MscVrIpBgpImportPeerAs_Object = MibTableColumn
mscVrIpBgpImportPeerAs = _MscVrIpBgpImportPeerAs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 3, 10, 1, 1),
    _MscVrIpBgpImportPeerAs_Type()
)
mscVrIpBgpImportPeerAs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpBgpImportPeerAs.setStatus("mandatory")


class _MscVrIpBgpImportPeerIpAddress_Type(IpAddress):
    """Custom type mscVrIpBgpImportPeerIpAddress based on IpAddress"""
    defaultHexValue = "00000000"


_MscVrIpBgpImportPeerIpAddress_Object = MibTableColumn
mscVrIpBgpImportPeerIpAddress = _MscVrIpBgpImportPeerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 3, 10, 1, 2),
    _MscVrIpBgpImportPeerIpAddress_Type()
)
mscVrIpBgpImportPeerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpBgpImportPeerIpAddress.setStatus("mandatory")


class _MscVrIpBgpImportOriginAs_Type(Unsigned32):
    """Custom type mscVrIpBgpImportOriginAs based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVrIpBgpImportOriginAs_Type.__name__ = "Unsigned32"
_MscVrIpBgpImportOriginAs_Object = MibTableColumn
mscVrIpBgpImportOriginAs = _MscVrIpBgpImportOriginAs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 3, 10, 1, 3),
    _MscVrIpBgpImportOriginAs_Type()
)
mscVrIpBgpImportOriginAs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpBgpImportOriginAs.setStatus("mandatory")


class _MscVrIpBgpImportOriginProtocol_Type(Integer32):
    """Custom type mscVrIpBgpImportOriginProtocol based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("any", 0),
          ("egp", 2),
          ("igp", 1),
          ("incomplete", 3))
    )


_MscVrIpBgpImportOriginProtocol_Type.__name__ = "Integer32"
_MscVrIpBgpImportOriginProtocol_Object = MibTableColumn
mscVrIpBgpImportOriginProtocol = _MscVrIpBgpImportOriginProtocol_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 3, 10, 1, 4),
    _MscVrIpBgpImportOriginProtocol_Type()
)
mscVrIpBgpImportOriginProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpBgpImportOriginProtocol.setStatus("mandatory")


class _MscVrIpBgpImportUsageFlag_Type(Integer32):
    """Custom type mscVrIpBgpImportUsageFlag based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ignore", 2),
          ("use", 1))
    )


_MscVrIpBgpImportUsageFlag_Type.__name__ = "Integer32"
_MscVrIpBgpImportUsageFlag_Object = MibTableColumn
mscVrIpBgpImportUsageFlag = _MscVrIpBgpImportUsageFlag_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 3, 10, 1, 5),
    _MscVrIpBgpImportUsageFlag_Type()
)
mscVrIpBgpImportUsageFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpBgpImportUsageFlag.setStatus("mandatory")


class _MscVrIpBgpImportLocalPreference_Type(Unsigned32):
    """Custom type mscVrIpBgpImportLocalPreference based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrIpBgpImportLocalPreference_Type.__name__ = "Unsigned32"
_MscVrIpBgpImportLocalPreference_Object = MibTableColumn
mscVrIpBgpImportLocalPreference = _MscVrIpBgpImportLocalPreference_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 3, 10, 1, 6),
    _MscVrIpBgpImportLocalPreference_Type()
)
mscVrIpBgpImportLocalPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpBgpImportLocalPreference.setStatus("mandatory")


class _MscVrIpBgpImportPreferredOver_Type(Integer32):
    """Custom type mscVrIpBgpImportPreferredOver based on Integer32"""
    defaultValue = 70

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              70)
        )
    )
    namedValues = NamedValues(
        *(("overIntOspf", 6),
          ("underIntOspf", 70))
    )


_MscVrIpBgpImportPreferredOver_Type.__name__ = "Integer32"
_MscVrIpBgpImportPreferredOver_Object = MibTableColumn
mscVrIpBgpImportPreferredOver = _MscVrIpBgpImportPreferredOver_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 3, 10, 1, 7),
    _MscVrIpBgpImportPreferredOver_Type()
)
mscVrIpBgpImportPreferredOver.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpBgpImportPreferredOver.setStatus("mandatory")


class _MscVrIpBgpImportAsPathExpression_Type(AsciiString):
    """Custom type mscVrIpBgpImportAsPathExpression based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscVrIpBgpImportAsPathExpression_Type.__name__ = "AsciiString"
_MscVrIpBgpImportAsPathExpression_Object = MibTableColumn
mscVrIpBgpImportAsPathExpression = _MscVrIpBgpImportAsPathExpression_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 3, 10, 1, 8),
    _MscVrIpBgpImportAsPathExpression_Type()
)
mscVrIpBgpImportAsPathExpression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpBgpImportAsPathExpression.setStatus("mandatory")


class _MscVrIpBgpImportCommunityExpression_Type(AsciiString):
    """Custom type mscVrIpBgpImportCommunityExpression based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscVrIpBgpImportCommunityExpression_Type.__name__ = "AsciiString"
_MscVrIpBgpImportCommunityExpression_Object = MibTableColumn
mscVrIpBgpImportCommunityExpression = _MscVrIpBgpImportCommunityExpression_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 3, 10, 1, 9),
    _MscVrIpBgpImportCommunityExpression_Type()
)
mscVrIpBgpImportCommunityExpression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpBgpImportCommunityExpression.setStatus("mandatory")


class _MscVrIpBgpImportExpressPreference_Type(Unsigned32):
    """Custom type mscVrIpBgpImportExpressPreference based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscVrIpBgpImportExpressPreference_Type.__name__ = "Unsigned32"
_MscVrIpBgpImportExpressPreference_Object = MibTableColumn
mscVrIpBgpImportExpressPreference = _MscVrIpBgpImportExpressPreference_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 3, 10, 1, 10),
    _MscVrIpBgpImportExpressPreference_Type()
)
mscVrIpBgpImportExpressPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpBgpImportExpressPreference.setStatus("mandatory")


class _MscVrIpBgpImportAppendCommunity_Type(Unsigned32):
    """Custom type mscVrIpBgpImportAppendCommunity based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrIpBgpImportAppendCommunity_Type.__name__ = "Unsigned32"
_MscVrIpBgpImportAppendCommunity_Object = MibTableColumn
mscVrIpBgpImportAppendCommunity = _MscVrIpBgpImportAppendCommunity_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 3, 10, 1, 11),
    _MscVrIpBgpImportAppendCommunity_Type()
)
mscVrIpBgpImportAppendCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpBgpImportAppendCommunity.setStatus("mandatory")
_MscVrIpBgpExport_ObjectIdentity = ObjectIdentity
mscVrIpBgpExport = _MscVrIpBgpExport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 4)
)
_MscVrIpBgpExportRowStatusTable_Object = MibTable
mscVrIpBgpExportRowStatusTable = _MscVrIpBgpExportRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 4, 1)
)
if mibBuilder.loadTexts:
    mscVrIpBgpExportRowStatusTable.setStatus("mandatory")
_MscVrIpBgpExportRowStatusEntry_Object = MibTableRow
mscVrIpBgpExportRowStatusEntry = _MscVrIpBgpExportRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 4, 1, 1)
)
mscVrIpBgpExportRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpExportIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpBgpExportRowStatusEntry.setStatus("mandatory")
_MscVrIpBgpExportRowStatus_Type = RowStatus
_MscVrIpBgpExportRowStatus_Object = MibTableColumn
mscVrIpBgpExportRowStatus = _MscVrIpBgpExportRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 4, 1, 1, 1),
    _MscVrIpBgpExportRowStatus_Type()
)
mscVrIpBgpExportRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpBgpExportRowStatus.setStatus("mandatory")
_MscVrIpBgpExportComponentName_Type = DisplayString
_MscVrIpBgpExportComponentName_Object = MibTableColumn
mscVrIpBgpExportComponentName = _MscVrIpBgpExportComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 4, 1, 1, 2),
    _MscVrIpBgpExportComponentName_Type()
)
mscVrIpBgpExportComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpExportComponentName.setStatus("mandatory")
_MscVrIpBgpExportStorageType_Type = StorageType
_MscVrIpBgpExportStorageType_Object = MibTableColumn
mscVrIpBgpExportStorageType = _MscVrIpBgpExportStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 4, 1, 1, 4),
    _MscVrIpBgpExportStorageType_Type()
)
mscVrIpBgpExportStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpExportStorageType.setStatus("mandatory")


class _MscVrIpBgpExportIndex_Type(Integer32):
    """Custom type mscVrIpBgpExportIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVrIpBgpExportIndex_Type.__name__ = "Integer32"
_MscVrIpBgpExportIndex_Object = MibTableColumn
mscVrIpBgpExportIndex = _MscVrIpBgpExportIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 4, 1, 1, 10),
    _MscVrIpBgpExportIndex_Type()
)
mscVrIpBgpExportIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpBgpExportIndex.setStatus("mandatory")
_MscVrIpBgpExportNet_ObjectIdentity = ObjectIdentity
mscVrIpBgpExportNet = _MscVrIpBgpExportNet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 4, 2)
)
_MscVrIpBgpExportNetRowStatusTable_Object = MibTable
mscVrIpBgpExportNetRowStatusTable = _MscVrIpBgpExportNetRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 4, 2, 1)
)
if mibBuilder.loadTexts:
    mscVrIpBgpExportNetRowStatusTable.setStatus("mandatory")
_MscVrIpBgpExportNetRowStatusEntry_Object = MibTableRow
mscVrIpBgpExportNetRowStatusEntry = _MscVrIpBgpExportNetRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 4, 2, 1, 1)
)
mscVrIpBgpExportNetRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpExportIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpExportNetIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpBgpExportNetRowStatusEntry.setStatus("mandatory")
_MscVrIpBgpExportNetRowStatus_Type = RowStatus
_MscVrIpBgpExportNetRowStatus_Object = MibTableColumn
mscVrIpBgpExportNetRowStatus = _MscVrIpBgpExportNetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 4, 2, 1, 1, 1),
    _MscVrIpBgpExportNetRowStatus_Type()
)
mscVrIpBgpExportNetRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpBgpExportNetRowStatus.setStatus("mandatory")
_MscVrIpBgpExportNetComponentName_Type = DisplayString
_MscVrIpBgpExportNetComponentName_Object = MibTableColumn
mscVrIpBgpExportNetComponentName = _MscVrIpBgpExportNetComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 4, 2, 1, 1, 2),
    _MscVrIpBgpExportNetComponentName_Type()
)
mscVrIpBgpExportNetComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpExportNetComponentName.setStatus("mandatory")
_MscVrIpBgpExportNetStorageType_Type = StorageType
_MscVrIpBgpExportNetStorageType_Object = MibTableColumn
mscVrIpBgpExportNetStorageType = _MscVrIpBgpExportNetStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 4, 2, 1, 1, 4),
    _MscVrIpBgpExportNetStorageType_Type()
)
mscVrIpBgpExportNetStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpExportNetStorageType.setStatus("mandatory")


class _MscVrIpBgpExportNetIndex_Type(Integer32):
    """Custom type mscVrIpBgpExportNetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVrIpBgpExportNetIndex_Type.__name__ = "Integer32"
_MscVrIpBgpExportNetIndex_Object = MibTableColumn
mscVrIpBgpExportNetIndex = _MscVrIpBgpExportNetIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 4, 2, 1, 1, 10),
    _MscVrIpBgpExportNetIndex_Type()
)
mscVrIpBgpExportNetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpBgpExportNetIndex.setStatus("mandatory")
_MscVrIpBgpExportNetProvTable_Object = MibTable
mscVrIpBgpExportNetProvTable = _MscVrIpBgpExportNetProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 4, 2, 10)
)
if mibBuilder.loadTexts:
    mscVrIpBgpExportNetProvTable.setStatus("mandatory")
_MscVrIpBgpExportNetProvEntry_Object = MibTableRow
mscVrIpBgpExportNetProvEntry = _MscVrIpBgpExportNetProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 4, 2, 10, 1)
)
mscVrIpBgpExportNetProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpExportIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpExportNetIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpBgpExportNetProvEntry.setStatus("mandatory")
_MscVrIpBgpExportNetPrefix_Type = IpAddress
_MscVrIpBgpExportNetPrefix_Object = MibTableColumn
mscVrIpBgpExportNetPrefix = _MscVrIpBgpExportNetPrefix_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 4, 2, 10, 1, 1),
    _MscVrIpBgpExportNetPrefix_Type()
)
mscVrIpBgpExportNetPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpBgpExportNetPrefix.setStatus("mandatory")


class _MscVrIpBgpExportNetLength_Type(Unsigned32):
    """Custom type mscVrIpBgpExportNetLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_MscVrIpBgpExportNetLength_Type.__name__ = "Unsigned32"
_MscVrIpBgpExportNetLength_Object = MibTableColumn
mscVrIpBgpExportNetLength = _MscVrIpBgpExportNetLength_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 4, 2, 10, 1, 2),
    _MscVrIpBgpExportNetLength_Type()
)
mscVrIpBgpExportNetLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpBgpExportNetLength.setStatus("mandatory")
_MscVrIpBgpExportProvTable_Object = MibTable
mscVrIpBgpExportProvTable = _MscVrIpBgpExportProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 4, 10)
)
if mibBuilder.loadTexts:
    mscVrIpBgpExportProvTable.setStatus("mandatory")
_MscVrIpBgpExportProvEntry_Object = MibTableRow
mscVrIpBgpExportProvEntry = _MscVrIpBgpExportProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 4, 10, 1)
)
mscVrIpBgpExportProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpExportIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpBgpExportProvEntry.setStatus("mandatory")


class _MscVrIpBgpExportPeerAs_Type(Unsigned32):
    """Custom type mscVrIpBgpExportPeerAs based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVrIpBgpExportPeerAs_Type.__name__ = "Unsigned32"
_MscVrIpBgpExportPeerAs_Object = MibTableColumn
mscVrIpBgpExportPeerAs = _MscVrIpBgpExportPeerAs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 4, 10, 1, 1),
    _MscVrIpBgpExportPeerAs_Type()
)
mscVrIpBgpExportPeerAs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpBgpExportPeerAs.setStatus("mandatory")


class _MscVrIpBgpExportPeerIpAddress_Type(IpAddress):
    """Custom type mscVrIpBgpExportPeerIpAddress based on IpAddress"""
    defaultHexValue = "00000000"


_MscVrIpBgpExportPeerIpAddress_Object = MibTableColumn
mscVrIpBgpExportPeerIpAddress = _MscVrIpBgpExportPeerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 4, 10, 1, 2),
    _MscVrIpBgpExportPeerIpAddress_Type()
)
mscVrIpBgpExportPeerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpBgpExportPeerIpAddress.setStatus("mandatory")


class _MscVrIpBgpExportProtocol_Type(Integer32):
    """Custom type mscVrIpBgpExportProtocol based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("bgpExternal", 9),
          ("bgpInternal", 8),
          ("egp", 2),
          ("ospfExternal", 5),
          ("ospfInternal", 4),
          ("rip", 3),
          ("staticLocal", 6),
          ("staticRemote", 7))
    )


_MscVrIpBgpExportProtocol_Type.__name__ = "Integer32"
_MscVrIpBgpExportProtocol_Object = MibTableColumn
mscVrIpBgpExportProtocol = _MscVrIpBgpExportProtocol_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 4, 10, 1, 3),
    _MscVrIpBgpExportProtocol_Type()
)
mscVrIpBgpExportProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpBgpExportProtocol.setStatus("mandatory")


class _MscVrIpBgpExportEgpAsId_Type(Unsigned32):
    """Custom type mscVrIpBgpExportEgpAsId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVrIpBgpExportEgpAsId_Type.__name__ = "Unsigned32"
_MscVrIpBgpExportEgpAsId_Object = MibTableColumn
mscVrIpBgpExportEgpAsId = _MscVrIpBgpExportEgpAsId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 4, 10, 1, 4),
    _MscVrIpBgpExportEgpAsId_Type()
)
mscVrIpBgpExportEgpAsId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpBgpExportEgpAsId.setStatus("mandatory")


class _MscVrIpBgpExportBgpAsId_Type(Unsigned32):
    """Custom type mscVrIpBgpExportBgpAsId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVrIpBgpExportBgpAsId_Type.__name__ = "Unsigned32"
_MscVrIpBgpExportBgpAsId_Object = MibTableColumn
mscVrIpBgpExportBgpAsId = _MscVrIpBgpExportBgpAsId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 4, 10, 1, 5),
    _MscVrIpBgpExportBgpAsId_Type()
)
mscVrIpBgpExportBgpAsId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpBgpExportBgpAsId.setStatus("mandatory")


class _MscVrIpBgpExportOspfTag_Type(Hex):
    """Custom type mscVrIpBgpExportOspfTag based on Hex"""
    defaultValue = 4294967295

    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrIpBgpExportOspfTag_Type.__name__ = "Hex"
_MscVrIpBgpExportOspfTag_Object = MibTableColumn
mscVrIpBgpExportOspfTag = _MscVrIpBgpExportOspfTag_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 4, 10, 1, 6),
    _MscVrIpBgpExportOspfTag_Type()
)
mscVrIpBgpExportOspfTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpBgpExportOspfTag.setStatus("mandatory")


class _MscVrIpBgpExportRipInterface_Type(IpAddress):
    """Custom type mscVrIpBgpExportRipInterface based on IpAddress"""
    defaultHexValue = "00000000"


_MscVrIpBgpExportRipInterface_Object = MibTableColumn
mscVrIpBgpExportRipInterface = _MscVrIpBgpExportRipInterface_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 4, 10, 1, 7),
    _MscVrIpBgpExportRipInterface_Type()
)
mscVrIpBgpExportRipInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpBgpExportRipInterface.setStatus("mandatory")


class _MscVrIpBgpExportRipNeighbor_Type(IpAddress):
    """Custom type mscVrIpBgpExportRipNeighbor based on IpAddress"""
    defaultHexValue = "00000000"


_MscVrIpBgpExportRipNeighbor_Object = MibTableColumn
mscVrIpBgpExportRipNeighbor = _MscVrIpBgpExportRipNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 4, 10, 1, 8),
    _MscVrIpBgpExportRipNeighbor_Type()
)
mscVrIpBgpExportRipNeighbor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpBgpExportRipNeighbor.setStatus("mandatory")


class _MscVrIpBgpExportAdvertiseStatus_Type(Integer32):
    """Custom type mscVrIpBgpExportAdvertiseStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("block", 2),
          ("send", 1))
    )


_MscVrIpBgpExportAdvertiseStatus_Type.__name__ = "Integer32"
_MscVrIpBgpExportAdvertiseStatus_Object = MibTableColumn
mscVrIpBgpExportAdvertiseStatus = _MscVrIpBgpExportAdvertiseStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 4, 10, 1, 9),
    _MscVrIpBgpExportAdvertiseStatus_Type()
)
mscVrIpBgpExportAdvertiseStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpBgpExportAdvertiseStatus.setStatus("mandatory")


class _MscVrIpBgpExportMultiExitDisc_Type(Unsigned32):
    """Custom type mscVrIpBgpExportMultiExitDisc based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrIpBgpExportMultiExitDisc_Type.__name__ = "Unsigned32"
_MscVrIpBgpExportMultiExitDisc_Object = MibTableColumn
mscVrIpBgpExportMultiExitDisc = _MscVrIpBgpExportMultiExitDisc_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 4, 10, 1, 10),
    _MscVrIpBgpExportMultiExitDisc_Type()
)
mscVrIpBgpExportMultiExitDisc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpBgpExportMultiExitDisc.setStatus("mandatory")


class _MscVrIpBgpExportSendMultiExitDiscToEbgp_Type(Integer32):
    """Custom type mscVrIpBgpExportSendMultiExitDiscToEbgp based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_MscVrIpBgpExportSendMultiExitDiscToEbgp_Type.__name__ = "Integer32"
_MscVrIpBgpExportSendMultiExitDiscToEbgp_Object = MibTableColumn
mscVrIpBgpExportSendMultiExitDiscToEbgp = _MscVrIpBgpExportSendMultiExitDiscToEbgp_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 4, 10, 1, 11),
    _MscVrIpBgpExportSendMultiExitDiscToEbgp_Type()
)
mscVrIpBgpExportSendMultiExitDiscToEbgp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpBgpExportSendMultiExitDiscToEbgp.setStatus("mandatory")


class _MscVrIpBgpExportAsPathExpression_Type(AsciiString):
    """Custom type mscVrIpBgpExportAsPathExpression based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscVrIpBgpExportAsPathExpression_Type.__name__ = "AsciiString"
_MscVrIpBgpExportAsPathExpression_Object = MibTableColumn
mscVrIpBgpExportAsPathExpression = _MscVrIpBgpExportAsPathExpression_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 4, 10, 1, 12),
    _MscVrIpBgpExportAsPathExpression_Type()
)
mscVrIpBgpExportAsPathExpression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpBgpExportAsPathExpression.setStatus("mandatory")


class _MscVrIpBgpExportCommunityExpression_Type(AsciiString):
    """Custom type mscVrIpBgpExportCommunityExpression based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscVrIpBgpExportCommunityExpression_Type.__name__ = "AsciiString"
_MscVrIpBgpExportCommunityExpression_Object = MibTableColumn
mscVrIpBgpExportCommunityExpression = _MscVrIpBgpExportCommunityExpression_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 4, 10, 1, 13),
    _MscVrIpBgpExportCommunityExpression_Type()
)
mscVrIpBgpExportCommunityExpression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpBgpExportCommunityExpression.setStatus("mandatory")


class _MscVrIpBgpExportExpressPreference_Type(Unsigned32):
    """Custom type mscVrIpBgpExportExpressPreference based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscVrIpBgpExportExpressPreference_Type.__name__ = "Unsigned32"
_MscVrIpBgpExportExpressPreference_Object = MibTableColumn
mscVrIpBgpExportExpressPreference = _MscVrIpBgpExportExpressPreference_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 4, 10, 1, 14),
    _MscVrIpBgpExportExpressPreference_Type()
)
mscVrIpBgpExportExpressPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpBgpExportExpressPreference.setStatus("mandatory")


class _MscVrIpBgpExportSendCommunity_Type(Unsigned32):
    """Custom type mscVrIpBgpExportSendCommunity based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrIpBgpExportSendCommunity_Type.__name__ = "Unsigned32"
_MscVrIpBgpExportSendCommunity_Object = MibTableColumn
mscVrIpBgpExportSendCommunity = _MscVrIpBgpExportSendCommunity_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 4, 10, 1, 15),
    _MscVrIpBgpExportSendCommunity_Type()
)
mscVrIpBgpExportSendCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpBgpExportSendCommunity.setStatus("mandatory")
_MscVrIpBgpExportInsertDummyAs_Type = IntegerSequence
_MscVrIpBgpExportInsertDummyAs_Object = MibTableColumn
mscVrIpBgpExportInsertDummyAs = _MscVrIpBgpExportInsertDummyAs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 4, 10, 1, 200),
    _MscVrIpBgpExportInsertDummyAs_Type()
)
mscVrIpBgpExportInsertDummyAs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpBgpExportInsertDummyAs.setStatus("mandatory")
_MscVrIpBgpAs_ObjectIdentity = ObjectIdentity
mscVrIpBgpAs = _MscVrIpBgpAs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 5)
)
_MscVrIpBgpAsRowStatusTable_Object = MibTable
mscVrIpBgpAsRowStatusTable = _MscVrIpBgpAsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 5, 1)
)
if mibBuilder.loadTexts:
    mscVrIpBgpAsRowStatusTable.setStatus("mandatory")
_MscVrIpBgpAsRowStatusEntry_Object = MibTableRow
mscVrIpBgpAsRowStatusEntry = _MscVrIpBgpAsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 5, 1, 1)
)
mscVrIpBgpAsRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpAsIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpBgpAsRowStatusEntry.setStatus("mandatory")
_MscVrIpBgpAsRowStatus_Type = RowStatus
_MscVrIpBgpAsRowStatus_Object = MibTableColumn
mscVrIpBgpAsRowStatus = _MscVrIpBgpAsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 5, 1, 1, 1),
    _MscVrIpBgpAsRowStatus_Type()
)
mscVrIpBgpAsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpBgpAsRowStatus.setStatus("mandatory")
_MscVrIpBgpAsComponentName_Type = DisplayString
_MscVrIpBgpAsComponentName_Object = MibTableColumn
mscVrIpBgpAsComponentName = _MscVrIpBgpAsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 5, 1, 1, 2),
    _MscVrIpBgpAsComponentName_Type()
)
mscVrIpBgpAsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpAsComponentName.setStatus("mandatory")
_MscVrIpBgpAsStorageType_Type = StorageType
_MscVrIpBgpAsStorageType_Object = MibTableColumn
mscVrIpBgpAsStorageType = _MscVrIpBgpAsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 5, 1, 1, 4),
    _MscVrIpBgpAsStorageType_Type()
)
mscVrIpBgpAsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpAsStorageType.setStatus("mandatory")


class _MscVrIpBgpAsIndex_Type(Integer32):
    """Custom type mscVrIpBgpAsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVrIpBgpAsIndex_Type.__name__ = "Integer32"
_MscVrIpBgpAsIndex_Object = MibTableColumn
mscVrIpBgpAsIndex = _MscVrIpBgpAsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 5, 1, 1, 10),
    _MscVrIpBgpAsIndex_Type()
)
mscVrIpBgpAsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpBgpAsIndex.setStatus("mandatory")
_MscVrIpBgpAsProvTable_Object = MibTable
mscVrIpBgpAsProvTable = _MscVrIpBgpAsProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 5, 10)
)
if mibBuilder.loadTexts:
    mscVrIpBgpAsProvTable.setStatus("mandatory")
_MscVrIpBgpAsProvEntry_Object = MibTableRow
mscVrIpBgpAsProvEntry = _MscVrIpBgpAsProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 5, 10, 1)
)
mscVrIpBgpAsProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpAsIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpBgpAsProvEntry.setStatus("mandatory")


class _MscVrIpBgpAsWeight_Type(Unsigned32):
    """Custom type mscVrIpBgpAsWeight based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_MscVrIpBgpAsWeight_Type.__name__ = "Unsigned32"
_MscVrIpBgpAsWeight_Object = MibTableColumn
mscVrIpBgpAsWeight = _MscVrIpBgpAsWeight_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 5, 10, 1, 1),
    _MscVrIpBgpAsWeight_Type()
)
mscVrIpBgpAsWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpBgpAsWeight.setStatus("mandatory")
_MscVrIpBgpAggregate_ObjectIdentity = ObjectIdentity
mscVrIpBgpAggregate = _MscVrIpBgpAggregate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 6)
)
_MscVrIpBgpAggregateRowStatusTable_Object = MibTable
mscVrIpBgpAggregateRowStatusTable = _MscVrIpBgpAggregateRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 6, 1)
)
if mibBuilder.loadTexts:
    mscVrIpBgpAggregateRowStatusTable.setStatus("mandatory")
_MscVrIpBgpAggregateRowStatusEntry_Object = MibTableRow
mscVrIpBgpAggregateRowStatusEntry = _MscVrIpBgpAggregateRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 6, 1, 1)
)
mscVrIpBgpAggregateRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpAggregatePrefixIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpAggregateLengthIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpBgpAggregateRowStatusEntry.setStatus("mandatory")
_MscVrIpBgpAggregateRowStatus_Type = RowStatus
_MscVrIpBgpAggregateRowStatus_Object = MibTableColumn
mscVrIpBgpAggregateRowStatus = _MscVrIpBgpAggregateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 6, 1, 1, 1),
    _MscVrIpBgpAggregateRowStatus_Type()
)
mscVrIpBgpAggregateRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpBgpAggregateRowStatus.setStatus("mandatory")
_MscVrIpBgpAggregateComponentName_Type = DisplayString
_MscVrIpBgpAggregateComponentName_Object = MibTableColumn
mscVrIpBgpAggregateComponentName = _MscVrIpBgpAggregateComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 6, 1, 1, 2),
    _MscVrIpBgpAggregateComponentName_Type()
)
mscVrIpBgpAggregateComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpAggregateComponentName.setStatus("mandatory")
_MscVrIpBgpAggregateStorageType_Type = StorageType
_MscVrIpBgpAggregateStorageType_Object = MibTableColumn
mscVrIpBgpAggregateStorageType = _MscVrIpBgpAggregateStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 6, 1, 1, 4),
    _MscVrIpBgpAggregateStorageType_Type()
)
mscVrIpBgpAggregateStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpAggregateStorageType.setStatus("mandatory")
_MscVrIpBgpAggregatePrefixIndex_Type = IpAddress
_MscVrIpBgpAggregatePrefixIndex_Object = MibTableColumn
mscVrIpBgpAggregatePrefixIndex = _MscVrIpBgpAggregatePrefixIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 6, 1, 1, 10),
    _MscVrIpBgpAggregatePrefixIndex_Type()
)
mscVrIpBgpAggregatePrefixIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpBgpAggregatePrefixIndex.setStatus("mandatory")


class _MscVrIpBgpAggregateLengthIndex_Type(Integer32):
    """Custom type mscVrIpBgpAggregateLengthIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_MscVrIpBgpAggregateLengthIndex_Type.__name__ = "Integer32"
_MscVrIpBgpAggregateLengthIndex_Object = MibTableColumn
mscVrIpBgpAggregateLengthIndex = _MscVrIpBgpAggregateLengthIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 6, 1, 1, 11),
    _MscVrIpBgpAggregateLengthIndex_Type()
)
mscVrIpBgpAggregateLengthIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpBgpAggregateLengthIndex.setStatus("mandatory")
_MscVrIpBgpAggregateNet_ObjectIdentity = ObjectIdentity
mscVrIpBgpAggregateNet = _MscVrIpBgpAggregateNet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 6, 2)
)
_MscVrIpBgpAggregateNetRowStatusTable_Object = MibTable
mscVrIpBgpAggregateNetRowStatusTable = _MscVrIpBgpAggregateNetRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 6, 2, 1)
)
if mibBuilder.loadTexts:
    mscVrIpBgpAggregateNetRowStatusTable.setStatus("mandatory")
_MscVrIpBgpAggregateNetRowStatusEntry_Object = MibTableRow
mscVrIpBgpAggregateNetRowStatusEntry = _MscVrIpBgpAggregateNetRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 6, 2, 1, 1)
)
mscVrIpBgpAggregateNetRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpAggregatePrefixIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpAggregateLengthIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpAggregateNetIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpBgpAggregateNetRowStatusEntry.setStatus("mandatory")
_MscVrIpBgpAggregateNetRowStatus_Type = RowStatus
_MscVrIpBgpAggregateNetRowStatus_Object = MibTableColumn
mscVrIpBgpAggregateNetRowStatus = _MscVrIpBgpAggregateNetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 6, 2, 1, 1, 1),
    _MscVrIpBgpAggregateNetRowStatus_Type()
)
mscVrIpBgpAggregateNetRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpBgpAggregateNetRowStatus.setStatus("mandatory")
_MscVrIpBgpAggregateNetComponentName_Type = DisplayString
_MscVrIpBgpAggregateNetComponentName_Object = MibTableColumn
mscVrIpBgpAggregateNetComponentName = _MscVrIpBgpAggregateNetComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 6, 2, 1, 1, 2),
    _MscVrIpBgpAggregateNetComponentName_Type()
)
mscVrIpBgpAggregateNetComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpAggregateNetComponentName.setStatus("mandatory")
_MscVrIpBgpAggregateNetStorageType_Type = StorageType
_MscVrIpBgpAggregateNetStorageType_Object = MibTableColumn
mscVrIpBgpAggregateNetStorageType = _MscVrIpBgpAggregateNetStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 6, 2, 1, 1, 4),
    _MscVrIpBgpAggregateNetStorageType_Type()
)
mscVrIpBgpAggregateNetStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpAggregateNetStorageType.setStatus("mandatory")


class _MscVrIpBgpAggregateNetIndex_Type(Integer32):
    """Custom type mscVrIpBgpAggregateNetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVrIpBgpAggregateNetIndex_Type.__name__ = "Integer32"
_MscVrIpBgpAggregateNetIndex_Object = MibTableColumn
mscVrIpBgpAggregateNetIndex = _MscVrIpBgpAggregateNetIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 6, 2, 1, 1, 10),
    _MscVrIpBgpAggregateNetIndex_Type()
)
mscVrIpBgpAggregateNetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpBgpAggregateNetIndex.setStatus("mandatory")
_MscVrIpBgpAggregateNetProvTable_Object = MibTable
mscVrIpBgpAggregateNetProvTable = _MscVrIpBgpAggregateNetProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 6, 2, 10)
)
if mibBuilder.loadTexts:
    mscVrIpBgpAggregateNetProvTable.setStatus("mandatory")
_MscVrIpBgpAggregateNetProvEntry_Object = MibTableRow
mscVrIpBgpAggregateNetProvEntry = _MscVrIpBgpAggregateNetProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 6, 2, 10, 1)
)
mscVrIpBgpAggregateNetProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpAggregatePrefixIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpAggregateLengthIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpAggregateNetIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpBgpAggregateNetProvEntry.setStatus("mandatory")


class _MscVrIpBgpAggregateNetPrefix_Type(IpAddress):
    """Custom type mscVrIpBgpAggregateNetPrefix based on IpAddress"""
    defaultHexValue = "00000000"


_MscVrIpBgpAggregateNetPrefix_Object = MibTableColumn
mscVrIpBgpAggregateNetPrefix = _MscVrIpBgpAggregateNetPrefix_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 6, 2, 10, 1, 1),
    _MscVrIpBgpAggregateNetPrefix_Type()
)
mscVrIpBgpAggregateNetPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpBgpAggregateNetPrefix.setStatus("mandatory")


class _MscVrIpBgpAggregateNetLength_Type(Unsigned32):
    """Custom type mscVrIpBgpAggregateNetLength based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_MscVrIpBgpAggregateNetLength_Type.__name__ = "Unsigned32"
_MscVrIpBgpAggregateNetLength_Object = MibTableColumn
mscVrIpBgpAggregateNetLength = _MscVrIpBgpAggregateNetLength_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 6, 2, 10, 1, 2),
    _MscVrIpBgpAggregateNetLength_Type()
)
mscVrIpBgpAggregateNetLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpBgpAggregateNetLength.setStatus("mandatory")


class _MscVrIpBgpAggregateNetProtocol_Type(Integer32):
    """Custom type mscVrIpBgpAggregateNetProtocol based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("bgpExternal", 9),
          ("bgpInternal", 8),
          ("egp", 2),
          ("ospfExternal", 5),
          ("ospfInternal", 4),
          ("rip", 3),
          ("staticLocal", 6),
          ("staticRemote", 7))
    )


_MscVrIpBgpAggregateNetProtocol_Type.__name__ = "Integer32"
_MscVrIpBgpAggregateNetProtocol_Object = MibTableColumn
mscVrIpBgpAggregateNetProtocol = _MscVrIpBgpAggregateNetProtocol_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 6, 2, 10, 1, 3),
    _MscVrIpBgpAggregateNetProtocol_Type()
)
mscVrIpBgpAggregateNetProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpBgpAggregateNetProtocol.setStatus("mandatory")


class _MscVrIpBgpAggregateNetEgpAsId_Type(Unsigned32):
    """Custom type mscVrIpBgpAggregateNetEgpAsId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVrIpBgpAggregateNetEgpAsId_Type.__name__ = "Unsigned32"
_MscVrIpBgpAggregateNetEgpAsId_Object = MibTableColumn
mscVrIpBgpAggregateNetEgpAsId = _MscVrIpBgpAggregateNetEgpAsId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 6, 2, 10, 1, 4),
    _MscVrIpBgpAggregateNetEgpAsId_Type()
)
mscVrIpBgpAggregateNetEgpAsId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpBgpAggregateNetEgpAsId.setStatus("mandatory")


class _MscVrIpBgpAggregateNetBgpAsId_Type(Unsigned32):
    """Custom type mscVrIpBgpAggregateNetBgpAsId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVrIpBgpAggregateNetBgpAsId_Type.__name__ = "Unsigned32"
_MscVrIpBgpAggregateNetBgpAsId_Object = MibTableColumn
mscVrIpBgpAggregateNetBgpAsId = _MscVrIpBgpAggregateNetBgpAsId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 6, 2, 10, 1, 5),
    _MscVrIpBgpAggregateNetBgpAsId_Type()
)
mscVrIpBgpAggregateNetBgpAsId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpBgpAggregateNetBgpAsId.setStatus("mandatory")


class _MscVrIpBgpAggregateNetOspfTag_Type(Hex):
    """Custom type mscVrIpBgpAggregateNetOspfTag based on Hex"""
    defaultValue = 4294967295

    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrIpBgpAggregateNetOspfTag_Type.__name__ = "Hex"
_MscVrIpBgpAggregateNetOspfTag_Object = MibTableColumn
mscVrIpBgpAggregateNetOspfTag = _MscVrIpBgpAggregateNetOspfTag_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 6, 2, 10, 1, 6),
    _MscVrIpBgpAggregateNetOspfTag_Type()
)
mscVrIpBgpAggregateNetOspfTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpBgpAggregateNetOspfTag.setStatus("mandatory")


class _MscVrIpBgpAggregateNetRipInterface_Type(IpAddress):
    """Custom type mscVrIpBgpAggregateNetRipInterface based on IpAddress"""
    defaultHexValue = "00000000"


_MscVrIpBgpAggregateNetRipInterface_Object = MibTableColumn
mscVrIpBgpAggregateNetRipInterface = _MscVrIpBgpAggregateNetRipInterface_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 6, 2, 10, 1, 7),
    _MscVrIpBgpAggregateNetRipInterface_Type()
)
mscVrIpBgpAggregateNetRipInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpBgpAggregateNetRipInterface.setStatus("mandatory")


class _MscVrIpBgpAggregateNetAction_Type(Integer32):
    """Custom type mscVrIpBgpAggregateNetAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("advertise", 2),
          ("aggregate", 1))
    )


_MscVrIpBgpAggregateNetAction_Type.__name__ = "Integer32"
_MscVrIpBgpAggregateNetAction_Object = MibTableColumn
mscVrIpBgpAggregateNetAction = _MscVrIpBgpAggregateNetAction_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 6, 2, 10, 1, 8),
    _MscVrIpBgpAggregateNetAction_Type()
)
mscVrIpBgpAggregateNetAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpBgpAggregateNetAction.setStatus("mandatory")
_MscVrIpBgpIndb_ObjectIdentity = ObjectIdentity
mscVrIpBgpIndb = _MscVrIpBgpIndb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 7)
)
_MscVrIpBgpIndbRowStatusTable_Object = MibTable
mscVrIpBgpIndbRowStatusTable = _MscVrIpBgpIndbRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 7, 1)
)
if mibBuilder.loadTexts:
    mscVrIpBgpIndbRowStatusTable.setStatus("mandatory")
_MscVrIpBgpIndbRowStatusEntry_Object = MibTableRow
mscVrIpBgpIndbRowStatusEntry = _MscVrIpBgpIndbRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 7, 1, 1)
)
mscVrIpBgpIndbRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpIndbPrefixIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpIndbLengthIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpIndbPeerIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpBgpIndbRowStatusEntry.setStatus("mandatory")
_MscVrIpBgpIndbRowStatus_Type = RowStatus
_MscVrIpBgpIndbRowStatus_Object = MibTableColumn
mscVrIpBgpIndbRowStatus = _MscVrIpBgpIndbRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 7, 1, 1, 1),
    _MscVrIpBgpIndbRowStatus_Type()
)
mscVrIpBgpIndbRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpIndbRowStatus.setStatus("mandatory")
_MscVrIpBgpIndbComponentName_Type = DisplayString
_MscVrIpBgpIndbComponentName_Object = MibTableColumn
mscVrIpBgpIndbComponentName = _MscVrIpBgpIndbComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 7, 1, 1, 2),
    _MscVrIpBgpIndbComponentName_Type()
)
mscVrIpBgpIndbComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpIndbComponentName.setStatus("mandatory")
_MscVrIpBgpIndbStorageType_Type = StorageType
_MscVrIpBgpIndbStorageType_Object = MibTableColumn
mscVrIpBgpIndbStorageType = _MscVrIpBgpIndbStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 7, 1, 1, 4),
    _MscVrIpBgpIndbStorageType_Type()
)
mscVrIpBgpIndbStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpIndbStorageType.setStatus("mandatory")
_MscVrIpBgpIndbPrefixIndex_Type = IpAddress
_MscVrIpBgpIndbPrefixIndex_Object = MibTableColumn
mscVrIpBgpIndbPrefixIndex = _MscVrIpBgpIndbPrefixIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 7, 1, 1, 10),
    _MscVrIpBgpIndbPrefixIndex_Type()
)
mscVrIpBgpIndbPrefixIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpBgpIndbPrefixIndex.setStatus("mandatory")


class _MscVrIpBgpIndbLengthIndex_Type(Integer32):
    """Custom type mscVrIpBgpIndbLengthIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_MscVrIpBgpIndbLengthIndex_Type.__name__ = "Integer32"
_MscVrIpBgpIndbLengthIndex_Object = MibTableColumn
mscVrIpBgpIndbLengthIndex = _MscVrIpBgpIndbLengthIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 7, 1, 1, 11),
    _MscVrIpBgpIndbLengthIndex_Type()
)
mscVrIpBgpIndbLengthIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpBgpIndbLengthIndex.setStatus("mandatory")
_MscVrIpBgpIndbPeerIndex_Type = IpAddress
_MscVrIpBgpIndbPeerIndex_Object = MibTableColumn
mscVrIpBgpIndbPeerIndex = _MscVrIpBgpIndbPeerIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 7, 1, 1, 12),
    _MscVrIpBgpIndbPeerIndex_Type()
)
mscVrIpBgpIndbPeerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpBgpIndbPeerIndex.setStatus("mandatory")
_MscVrIpBgpIndbOperTable_Object = MibTable
mscVrIpBgpIndbOperTable = _MscVrIpBgpIndbOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 7, 10)
)
if mibBuilder.loadTexts:
    mscVrIpBgpIndbOperTable.setStatus("mandatory")
_MscVrIpBgpIndbOperEntry_Object = MibTableRow
mscVrIpBgpIndbOperEntry = _MscVrIpBgpIndbOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 7, 10, 1)
)
mscVrIpBgpIndbOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpIndbPrefixIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpIndbLengthIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpIndbPeerIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpBgpIndbOperEntry.setStatus("mandatory")


class _MscVrIpBgpIndbOrigin_Type(Integer32):
    """Custom type mscVrIpBgpIndbOrigin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("egp", 2),
          ("igp", 1),
          ("incomplete", 3))
    )


_MscVrIpBgpIndbOrigin_Type.__name__ = "Integer32"
_MscVrIpBgpIndbOrigin_Object = MibTableColumn
mscVrIpBgpIndbOrigin = _MscVrIpBgpIndbOrigin_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 7, 10, 1, 4),
    _MscVrIpBgpIndbOrigin_Type()
)
mscVrIpBgpIndbOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpIndbOrigin.setStatus("mandatory")


class _MscVrIpBgpIndbInLocaldb_Type(Integer32):
    """Custom type mscVrIpBgpIndbInLocaldb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )


_MscVrIpBgpIndbInLocaldb_Type.__name__ = "Integer32"
_MscVrIpBgpIndbInLocaldb_Object = MibTableColumn
mscVrIpBgpIndbInLocaldb = _MscVrIpBgpIndbInLocaldb_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 7, 10, 1, 5),
    _MscVrIpBgpIndbInLocaldb_Type()
)
mscVrIpBgpIndbInLocaldb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpIndbInLocaldb.setStatus("mandatory")
_MscVrIpBgpIndbNextHop_Type = IpAddress
_MscVrIpBgpIndbNextHop_Object = MibTableColumn
mscVrIpBgpIndbNextHop = _MscVrIpBgpIndbNextHop_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 7, 10, 1, 6),
    _MscVrIpBgpIndbNextHop_Type()
)
mscVrIpBgpIndbNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpIndbNextHop.setStatus("mandatory")


class _MscVrIpBgpIndbLocalPreference_Type(Unsigned32):
    """Custom type mscVrIpBgpIndbLocalPreference based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrIpBgpIndbLocalPreference_Type.__name__ = "Unsigned32"
_MscVrIpBgpIndbLocalPreference_Object = MibTableColumn
mscVrIpBgpIndbLocalPreference = _MscVrIpBgpIndbLocalPreference_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 7, 10, 1, 7),
    _MscVrIpBgpIndbLocalPreference_Type()
)
mscVrIpBgpIndbLocalPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpIndbLocalPreference.setStatus("mandatory")


class _MscVrIpBgpIndbCalcLocalPref_Type(Unsigned32):
    """Custom type mscVrIpBgpIndbCalcLocalPref based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrIpBgpIndbCalcLocalPref_Type.__name__ = "Unsigned32"
_MscVrIpBgpIndbCalcLocalPref_Object = MibTableColumn
mscVrIpBgpIndbCalcLocalPref = _MscVrIpBgpIndbCalcLocalPref_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 7, 10, 1, 8),
    _MscVrIpBgpIndbCalcLocalPref_Type()
)
mscVrIpBgpIndbCalcLocalPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpIndbCalcLocalPref.setStatus("mandatory")


class _MscVrIpBgpIndbMultiExitDiscriminator_Type(Unsigned32):
    """Custom type mscVrIpBgpIndbMultiExitDiscriminator based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrIpBgpIndbMultiExitDiscriminator_Type.__name__ = "Unsigned32"
_MscVrIpBgpIndbMultiExitDiscriminator_Object = MibTableColumn
mscVrIpBgpIndbMultiExitDiscriminator = _MscVrIpBgpIndbMultiExitDiscriminator_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 7, 10, 1, 9),
    _MscVrIpBgpIndbMultiExitDiscriminator_Type()
)
mscVrIpBgpIndbMultiExitDiscriminator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpIndbMultiExitDiscriminator.setStatus("mandatory")


class _MscVrIpBgpIndbAtomicAggregate_Type(Integer32):
    """Custom type mscVrIpBgpIndbAtomicAggregate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lessSpecificRouteNotSelected", 1),
          ("lessSpecificRouteSelected", 2))
    )


_MscVrIpBgpIndbAtomicAggregate_Type.__name__ = "Integer32"
_MscVrIpBgpIndbAtomicAggregate_Object = MibTableColumn
mscVrIpBgpIndbAtomicAggregate = _MscVrIpBgpIndbAtomicAggregate_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 7, 10, 1, 10),
    _MscVrIpBgpIndbAtomicAggregate_Type()
)
mscVrIpBgpIndbAtomicAggregate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpIndbAtomicAggregate.setStatus("mandatory")


class _MscVrIpBgpIndbAggregatorAs_Type(Unsigned32):
    """Custom type mscVrIpBgpIndbAggregatorAs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVrIpBgpIndbAggregatorAs_Type.__name__ = "Unsigned32"
_MscVrIpBgpIndbAggregatorAs_Object = MibTableColumn
mscVrIpBgpIndbAggregatorAs = _MscVrIpBgpIndbAggregatorAs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 7, 10, 1, 11),
    _MscVrIpBgpIndbAggregatorAs_Type()
)
mscVrIpBgpIndbAggregatorAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpIndbAggregatorAs.setStatus("mandatory")
_MscVrIpBgpIndbAggregatorAddr_Type = IpAddress
_MscVrIpBgpIndbAggregatorAddr_Object = MibTableColumn
mscVrIpBgpIndbAggregatorAddr = _MscVrIpBgpIndbAggregatorAddr_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 7, 10, 1, 12),
    _MscVrIpBgpIndbAggregatorAddr_Type()
)
mscVrIpBgpIndbAggregatorAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpIndbAggregatorAddr.setStatus("mandatory")


class _MscVrIpBgpIndbAsPath_Type(AsciiString):
    """Custom type mscVrIpBgpIndbAsPath based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 255),
    )


_MscVrIpBgpIndbAsPath_Type.__name__ = "AsciiString"
_MscVrIpBgpIndbAsPath_Object = MibTableColumn
mscVrIpBgpIndbAsPath = _MscVrIpBgpIndbAsPath_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 7, 10, 1, 13),
    _MscVrIpBgpIndbAsPath_Type()
)
mscVrIpBgpIndbAsPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpIndbAsPath.setStatus("mandatory")


class _MscVrIpBgpIndbUnknownAttributes_Type(AsciiString):
    """Custom type mscVrIpBgpIndbUnknownAttributes based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscVrIpBgpIndbUnknownAttributes_Type.__name__ = "AsciiString"
_MscVrIpBgpIndbUnknownAttributes_Object = MibTableColumn
mscVrIpBgpIndbUnknownAttributes = _MscVrIpBgpIndbUnknownAttributes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 7, 10, 1, 14),
    _MscVrIpBgpIndbUnknownAttributes_Type()
)
mscVrIpBgpIndbUnknownAttributes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpIndbUnknownAttributes.setStatus("mandatory")


class _MscVrIpBgpIndbCommunityPath_Type(AsciiString):
    """Custom type mscVrIpBgpIndbCommunityPath based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscVrIpBgpIndbCommunityPath_Type.__name__ = "AsciiString"
_MscVrIpBgpIndbCommunityPath_Object = MibTableColumn
mscVrIpBgpIndbCommunityPath = _MscVrIpBgpIndbCommunityPath_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 7, 10, 1, 15),
    _MscVrIpBgpIndbCommunityPath_Type()
)
mscVrIpBgpIndbCommunityPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpIndbCommunityPath.setStatus("mandatory")
_MscVrIpBgpIndbAsOriginatorId_Type = IpAddress
_MscVrIpBgpIndbAsOriginatorId_Object = MibTableColumn
mscVrIpBgpIndbAsOriginatorId = _MscVrIpBgpIndbAsOriginatorId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 7, 10, 1, 16),
    _MscVrIpBgpIndbAsOriginatorId_Type()
)
mscVrIpBgpIndbAsOriginatorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpIndbAsOriginatorId.setStatus("mandatory")
_MscVrIpBgpIndbRrClusterListTable_Object = MibTable
mscVrIpBgpIndbRrClusterListTable = _MscVrIpBgpIndbRrClusterListTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 7, 798)
)
if mibBuilder.loadTexts:
    mscVrIpBgpIndbRrClusterListTable.setStatus("mandatory")
_MscVrIpBgpIndbRrClusterListEntry_Object = MibTableRow
mscVrIpBgpIndbRrClusterListEntry = _MscVrIpBgpIndbRrClusterListEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 7, 798, 1)
)
mscVrIpBgpIndbRrClusterListEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpIndbPrefixIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpIndbLengthIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpIndbPeerIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpIndbRrClusterListValue"),
)
if mibBuilder.loadTexts:
    mscVrIpBgpIndbRrClusterListEntry.setStatus("mandatory")
_MscVrIpBgpIndbRrClusterListValue_Type = IpAddress
_MscVrIpBgpIndbRrClusterListValue_Object = MibTableColumn
mscVrIpBgpIndbRrClusterListValue = _MscVrIpBgpIndbRrClusterListValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 7, 798, 1, 1),
    _MscVrIpBgpIndbRrClusterListValue_Type()
)
mscVrIpBgpIndbRrClusterListValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpIndbRrClusterListValue.setStatus("mandatory")
_MscVrIpBgpLocaldb_ObjectIdentity = ObjectIdentity
mscVrIpBgpLocaldb = _MscVrIpBgpLocaldb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 8)
)
_MscVrIpBgpLocaldbRowStatusTable_Object = MibTable
mscVrIpBgpLocaldbRowStatusTable = _MscVrIpBgpLocaldbRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 8, 1)
)
if mibBuilder.loadTexts:
    mscVrIpBgpLocaldbRowStatusTable.setStatus("mandatory")
_MscVrIpBgpLocaldbRowStatusEntry_Object = MibTableRow
mscVrIpBgpLocaldbRowStatusEntry = _MscVrIpBgpLocaldbRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 8, 1, 1)
)
mscVrIpBgpLocaldbRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpLocaldbPrefixIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpLocaldbLengthIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpLocaldbPeerIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpBgpLocaldbRowStatusEntry.setStatus("mandatory")
_MscVrIpBgpLocaldbRowStatus_Type = RowStatus
_MscVrIpBgpLocaldbRowStatus_Object = MibTableColumn
mscVrIpBgpLocaldbRowStatus = _MscVrIpBgpLocaldbRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 8, 1, 1, 1),
    _MscVrIpBgpLocaldbRowStatus_Type()
)
mscVrIpBgpLocaldbRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpLocaldbRowStatus.setStatus("mandatory")
_MscVrIpBgpLocaldbComponentName_Type = DisplayString
_MscVrIpBgpLocaldbComponentName_Object = MibTableColumn
mscVrIpBgpLocaldbComponentName = _MscVrIpBgpLocaldbComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 8, 1, 1, 2),
    _MscVrIpBgpLocaldbComponentName_Type()
)
mscVrIpBgpLocaldbComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpLocaldbComponentName.setStatus("mandatory")
_MscVrIpBgpLocaldbStorageType_Type = StorageType
_MscVrIpBgpLocaldbStorageType_Object = MibTableColumn
mscVrIpBgpLocaldbStorageType = _MscVrIpBgpLocaldbStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 8, 1, 1, 4),
    _MscVrIpBgpLocaldbStorageType_Type()
)
mscVrIpBgpLocaldbStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpLocaldbStorageType.setStatus("mandatory")
_MscVrIpBgpLocaldbPrefixIndex_Type = IpAddress
_MscVrIpBgpLocaldbPrefixIndex_Object = MibTableColumn
mscVrIpBgpLocaldbPrefixIndex = _MscVrIpBgpLocaldbPrefixIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 8, 1, 1, 10),
    _MscVrIpBgpLocaldbPrefixIndex_Type()
)
mscVrIpBgpLocaldbPrefixIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpBgpLocaldbPrefixIndex.setStatus("mandatory")


class _MscVrIpBgpLocaldbLengthIndex_Type(Integer32):
    """Custom type mscVrIpBgpLocaldbLengthIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_MscVrIpBgpLocaldbLengthIndex_Type.__name__ = "Integer32"
_MscVrIpBgpLocaldbLengthIndex_Object = MibTableColumn
mscVrIpBgpLocaldbLengthIndex = _MscVrIpBgpLocaldbLengthIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 8, 1, 1, 11),
    _MscVrIpBgpLocaldbLengthIndex_Type()
)
mscVrIpBgpLocaldbLengthIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpBgpLocaldbLengthIndex.setStatus("mandatory")
_MscVrIpBgpLocaldbPeerIndex_Type = IpAddress
_MscVrIpBgpLocaldbPeerIndex_Object = MibTableColumn
mscVrIpBgpLocaldbPeerIndex = _MscVrIpBgpLocaldbPeerIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 8, 1, 1, 12),
    _MscVrIpBgpLocaldbPeerIndex_Type()
)
mscVrIpBgpLocaldbPeerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpBgpLocaldbPeerIndex.setStatus("mandatory")
_MscVrIpBgpLocaldbOperTable_Object = MibTable
mscVrIpBgpLocaldbOperTable = _MscVrIpBgpLocaldbOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 8, 10)
)
if mibBuilder.loadTexts:
    mscVrIpBgpLocaldbOperTable.setStatus("mandatory")
_MscVrIpBgpLocaldbOperEntry_Object = MibTableRow
mscVrIpBgpLocaldbOperEntry = _MscVrIpBgpLocaldbOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 8, 10, 1)
)
mscVrIpBgpLocaldbOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpLocaldbPrefixIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpLocaldbLengthIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpLocaldbPeerIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpBgpLocaldbOperEntry.setStatus("mandatory")


class _MscVrIpBgpLocaldbOrigin_Type(Integer32):
    """Custom type mscVrIpBgpLocaldbOrigin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("egp", 2),
          ("igp", 1),
          ("incomplete", 3))
    )


_MscVrIpBgpLocaldbOrigin_Type.__name__ = "Integer32"
_MscVrIpBgpLocaldbOrigin_Object = MibTableColumn
mscVrIpBgpLocaldbOrigin = _MscVrIpBgpLocaldbOrigin_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 8, 10, 1, 4),
    _MscVrIpBgpLocaldbOrigin_Type()
)
mscVrIpBgpLocaldbOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpLocaldbOrigin.setStatus("mandatory")
_MscVrIpBgpLocaldbNextHop_Type = IpAddress
_MscVrIpBgpLocaldbNextHop_Object = MibTableColumn
mscVrIpBgpLocaldbNextHop = _MscVrIpBgpLocaldbNextHop_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 8, 10, 1, 5),
    _MscVrIpBgpLocaldbNextHop_Type()
)
mscVrIpBgpLocaldbNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpLocaldbNextHop.setStatus("mandatory")


class _MscVrIpBgpLocaldbLocalPreference_Type(Unsigned32):
    """Custom type mscVrIpBgpLocaldbLocalPreference based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrIpBgpLocaldbLocalPreference_Type.__name__ = "Unsigned32"
_MscVrIpBgpLocaldbLocalPreference_Object = MibTableColumn
mscVrIpBgpLocaldbLocalPreference = _MscVrIpBgpLocaldbLocalPreference_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 8, 10, 1, 6),
    _MscVrIpBgpLocaldbLocalPreference_Type()
)
mscVrIpBgpLocaldbLocalPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpLocaldbLocalPreference.setStatus("mandatory")


class _MscVrIpBgpLocaldbMultiExitDiscriminator_Type(Unsigned32):
    """Custom type mscVrIpBgpLocaldbMultiExitDiscriminator based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrIpBgpLocaldbMultiExitDiscriminator_Type.__name__ = "Unsigned32"
_MscVrIpBgpLocaldbMultiExitDiscriminator_Object = MibTableColumn
mscVrIpBgpLocaldbMultiExitDiscriminator = _MscVrIpBgpLocaldbMultiExitDiscriminator_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 8, 10, 1, 7),
    _MscVrIpBgpLocaldbMultiExitDiscriminator_Type()
)
mscVrIpBgpLocaldbMultiExitDiscriminator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpLocaldbMultiExitDiscriminator.setStatus("mandatory")


class _MscVrIpBgpLocaldbAtomicAggregate_Type(Integer32):
    """Custom type mscVrIpBgpLocaldbAtomicAggregate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lessSpecificRouteNotSelected", 1),
          ("lessSpecificRouteSelected", 2))
    )


_MscVrIpBgpLocaldbAtomicAggregate_Type.__name__ = "Integer32"
_MscVrIpBgpLocaldbAtomicAggregate_Object = MibTableColumn
mscVrIpBgpLocaldbAtomicAggregate = _MscVrIpBgpLocaldbAtomicAggregate_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 8, 10, 1, 8),
    _MscVrIpBgpLocaldbAtomicAggregate_Type()
)
mscVrIpBgpLocaldbAtomicAggregate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpLocaldbAtomicAggregate.setStatus("mandatory")


class _MscVrIpBgpLocaldbAggregatorAs_Type(Unsigned32):
    """Custom type mscVrIpBgpLocaldbAggregatorAs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVrIpBgpLocaldbAggregatorAs_Type.__name__ = "Unsigned32"
_MscVrIpBgpLocaldbAggregatorAs_Object = MibTableColumn
mscVrIpBgpLocaldbAggregatorAs = _MscVrIpBgpLocaldbAggregatorAs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 8, 10, 1, 9),
    _MscVrIpBgpLocaldbAggregatorAs_Type()
)
mscVrIpBgpLocaldbAggregatorAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpLocaldbAggregatorAs.setStatus("mandatory")
_MscVrIpBgpLocaldbAggregatorAddr_Type = IpAddress
_MscVrIpBgpLocaldbAggregatorAddr_Object = MibTableColumn
mscVrIpBgpLocaldbAggregatorAddr = _MscVrIpBgpLocaldbAggregatorAddr_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 8, 10, 1, 10),
    _MscVrIpBgpLocaldbAggregatorAddr_Type()
)
mscVrIpBgpLocaldbAggregatorAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpLocaldbAggregatorAddr.setStatus("mandatory")


class _MscVrIpBgpLocaldbAsPath_Type(AsciiString):
    """Custom type mscVrIpBgpLocaldbAsPath based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 255),
    )


_MscVrIpBgpLocaldbAsPath_Type.__name__ = "AsciiString"
_MscVrIpBgpLocaldbAsPath_Object = MibTableColumn
mscVrIpBgpLocaldbAsPath = _MscVrIpBgpLocaldbAsPath_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 8, 10, 1, 11),
    _MscVrIpBgpLocaldbAsPath_Type()
)
mscVrIpBgpLocaldbAsPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpLocaldbAsPath.setStatus("mandatory")


class _MscVrIpBgpLocaldbUnknownAttributes_Type(AsciiString):
    """Custom type mscVrIpBgpLocaldbUnknownAttributes based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscVrIpBgpLocaldbUnknownAttributes_Type.__name__ = "AsciiString"
_MscVrIpBgpLocaldbUnknownAttributes_Object = MibTableColumn
mscVrIpBgpLocaldbUnknownAttributes = _MscVrIpBgpLocaldbUnknownAttributes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 8, 10, 1, 12),
    _MscVrIpBgpLocaldbUnknownAttributes_Type()
)
mscVrIpBgpLocaldbUnknownAttributes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpLocaldbUnknownAttributes.setStatus("mandatory")


class _MscVrIpBgpLocaldbCommunityPath_Type(AsciiString):
    """Custom type mscVrIpBgpLocaldbCommunityPath based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscVrIpBgpLocaldbCommunityPath_Type.__name__ = "AsciiString"
_MscVrIpBgpLocaldbCommunityPath_Object = MibTableColumn
mscVrIpBgpLocaldbCommunityPath = _MscVrIpBgpLocaldbCommunityPath_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 8, 10, 1, 13),
    _MscVrIpBgpLocaldbCommunityPath_Type()
)
mscVrIpBgpLocaldbCommunityPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpLocaldbCommunityPath.setStatus("mandatory")
_MscVrIpBgpLocaldbAsOriginatorId_Type = IpAddress
_MscVrIpBgpLocaldbAsOriginatorId_Object = MibTableColumn
mscVrIpBgpLocaldbAsOriginatorId = _MscVrIpBgpLocaldbAsOriginatorId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 8, 10, 1, 14),
    _MscVrIpBgpLocaldbAsOriginatorId_Type()
)
mscVrIpBgpLocaldbAsOriginatorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpLocaldbAsOriginatorId.setStatus("mandatory")
_MscVrIpBgpLocaldbRrClusterListTable_Object = MibTable
mscVrIpBgpLocaldbRrClusterListTable = _MscVrIpBgpLocaldbRrClusterListTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 8, 797)
)
if mibBuilder.loadTexts:
    mscVrIpBgpLocaldbRrClusterListTable.setStatus("mandatory")
_MscVrIpBgpLocaldbRrClusterListEntry_Object = MibTableRow
mscVrIpBgpLocaldbRrClusterListEntry = _MscVrIpBgpLocaldbRrClusterListEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 8, 797, 1)
)
mscVrIpBgpLocaldbRrClusterListEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpLocaldbPrefixIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpLocaldbLengthIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpLocaldbPeerIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpLocaldbRrClusterListValue"),
)
if mibBuilder.loadTexts:
    mscVrIpBgpLocaldbRrClusterListEntry.setStatus("mandatory")
_MscVrIpBgpLocaldbRrClusterListValue_Type = IpAddress
_MscVrIpBgpLocaldbRrClusterListValue_Object = MibTableColumn
mscVrIpBgpLocaldbRrClusterListValue = _MscVrIpBgpLocaldbRrClusterListValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 8, 797, 1, 1),
    _MscVrIpBgpLocaldbRrClusterListValue_Type()
)
mscVrIpBgpLocaldbRrClusterListValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpLocaldbRrClusterListValue.setStatus("mandatory")
_MscVrIpBgpOutdb_ObjectIdentity = ObjectIdentity
mscVrIpBgpOutdb = _MscVrIpBgpOutdb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 9)
)
_MscVrIpBgpOutdbRowStatusTable_Object = MibTable
mscVrIpBgpOutdbRowStatusTable = _MscVrIpBgpOutdbRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 9, 1)
)
if mibBuilder.loadTexts:
    mscVrIpBgpOutdbRowStatusTable.setStatus("mandatory")
_MscVrIpBgpOutdbRowStatusEntry_Object = MibTableRow
mscVrIpBgpOutdbRowStatusEntry = _MscVrIpBgpOutdbRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 9, 1, 1)
)
mscVrIpBgpOutdbRowStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpOutdbPrefixIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpOutdbLengthIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpOutdbPeerIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpBgpOutdbRowStatusEntry.setStatus("mandatory")
_MscVrIpBgpOutdbRowStatus_Type = RowStatus
_MscVrIpBgpOutdbRowStatus_Object = MibTableColumn
mscVrIpBgpOutdbRowStatus = _MscVrIpBgpOutdbRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 9, 1, 1, 1),
    _MscVrIpBgpOutdbRowStatus_Type()
)
mscVrIpBgpOutdbRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpOutdbRowStatus.setStatus("mandatory")
_MscVrIpBgpOutdbComponentName_Type = DisplayString
_MscVrIpBgpOutdbComponentName_Object = MibTableColumn
mscVrIpBgpOutdbComponentName = _MscVrIpBgpOutdbComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 9, 1, 1, 2),
    _MscVrIpBgpOutdbComponentName_Type()
)
mscVrIpBgpOutdbComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpOutdbComponentName.setStatus("mandatory")
_MscVrIpBgpOutdbStorageType_Type = StorageType
_MscVrIpBgpOutdbStorageType_Object = MibTableColumn
mscVrIpBgpOutdbStorageType = _MscVrIpBgpOutdbStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 9, 1, 1, 4),
    _MscVrIpBgpOutdbStorageType_Type()
)
mscVrIpBgpOutdbStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpOutdbStorageType.setStatus("mandatory")
_MscVrIpBgpOutdbPrefixIndex_Type = IpAddress
_MscVrIpBgpOutdbPrefixIndex_Object = MibTableColumn
mscVrIpBgpOutdbPrefixIndex = _MscVrIpBgpOutdbPrefixIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 9, 1, 1, 10),
    _MscVrIpBgpOutdbPrefixIndex_Type()
)
mscVrIpBgpOutdbPrefixIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpBgpOutdbPrefixIndex.setStatus("mandatory")


class _MscVrIpBgpOutdbLengthIndex_Type(Integer32):
    """Custom type mscVrIpBgpOutdbLengthIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_MscVrIpBgpOutdbLengthIndex_Type.__name__ = "Integer32"
_MscVrIpBgpOutdbLengthIndex_Object = MibTableColumn
mscVrIpBgpOutdbLengthIndex = _MscVrIpBgpOutdbLengthIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 9, 1, 1, 11),
    _MscVrIpBgpOutdbLengthIndex_Type()
)
mscVrIpBgpOutdbLengthIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpBgpOutdbLengthIndex.setStatus("mandatory")
_MscVrIpBgpOutdbPeerIndex_Type = IpAddress
_MscVrIpBgpOutdbPeerIndex_Object = MibTableColumn
mscVrIpBgpOutdbPeerIndex = _MscVrIpBgpOutdbPeerIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 9, 1, 1, 12),
    _MscVrIpBgpOutdbPeerIndex_Type()
)
mscVrIpBgpOutdbPeerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mscVrIpBgpOutdbPeerIndex.setStatus("mandatory")
_MscVrIpBgpOutdbOperTable_Object = MibTable
mscVrIpBgpOutdbOperTable = _MscVrIpBgpOutdbOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 9, 10)
)
if mibBuilder.loadTexts:
    mscVrIpBgpOutdbOperTable.setStatus("mandatory")
_MscVrIpBgpOutdbOperEntry_Object = MibTableRow
mscVrIpBgpOutdbOperEntry = _MscVrIpBgpOutdbOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 9, 10, 1)
)
mscVrIpBgpOutdbOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpOutdbPrefixIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpOutdbLengthIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpOutdbPeerIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpBgpOutdbOperEntry.setStatus("mandatory")


class _MscVrIpBgpOutdbOrigin_Type(Integer32):
    """Custom type mscVrIpBgpOutdbOrigin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("egp", 2),
          ("igp", 1),
          ("incomplete", 3))
    )


_MscVrIpBgpOutdbOrigin_Type.__name__ = "Integer32"
_MscVrIpBgpOutdbOrigin_Object = MibTableColumn
mscVrIpBgpOutdbOrigin = _MscVrIpBgpOutdbOrigin_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 9, 10, 1, 4),
    _MscVrIpBgpOutdbOrigin_Type()
)
mscVrIpBgpOutdbOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpOutdbOrigin.setStatus("mandatory")
_MscVrIpBgpOutdbNextHop_Type = IpAddress
_MscVrIpBgpOutdbNextHop_Object = MibTableColumn
mscVrIpBgpOutdbNextHop = _MscVrIpBgpOutdbNextHop_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 9, 10, 1, 5),
    _MscVrIpBgpOutdbNextHop_Type()
)
mscVrIpBgpOutdbNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpOutdbNextHop.setStatus("mandatory")


class _MscVrIpBgpOutdbLocalPreference_Type(Unsigned32):
    """Custom type mscVrIpBgpOutdbLocalPreference based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrIpBgpOutdbLocalPreference_Type.__name__ = "Unsigned32"
_MscVrIpBgpOutdbLocalPreference_Object = MibTableColumn
mscVrIpBgpOutdbLocalPreference = _MscVrIpBgpOutdbLocalPreference_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 9, 10, 1, 6),
    _MscVrIpBgpOutdbLocalPreference_Type()
)
mscVrIpBgpOutdbLocalPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpOutdbLocalPreference.setStatus("mandatory")


class _MscVrIpBgpOutdbMultiExitDiscriminator_Type(Unsigned32):
    """Custom type mscVrIpBgpOutdbMultiExitDiscriminator based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrIpBgpOutdbMultiExitDiscriminator_Type.__name__ = "Unsigned32"
_MscVrIpBgpOutdbMultiExitDiscriminator_Object = MibTableColumn
mscVrIpBgpOutdbMultiExitDiscriminator = _MscVrIpBgpOutdbMultiExitDiscriminator_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 9, 10, 1, 7),
    _MscVrIpBgpOutdbMultiExitDiscriminator_Type()
)
mscVrIpBgpOutdbMultiExitDiscriminator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpOutdbMultiExitDiscriminator.setStatus("mandatory")


class _MscVrIpBgpOutdbAtomicAggregate_Type(Integer32):
    """Custom type mscVrIpBgpOutdbAtomicAggregate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lessSpecificRouteNotSelected", 1),
          ("lessSpecificRouteSelected", 2))
    )


_MscVrIpBgpOutdbAtomicAggregate_Type.__name__ = "Integer32"
_MscVrIpBgpOutdbAtomicAggregate_Object = MibTableColumn
mscVrIpBgpOutdbAtomicAggregate = _MscVrIpBgpOutdbAtomicAggregate_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 9, 10, 1, 8),
    _MscVrIpBgpOutdbAtomicAggregate_Type()
)
mscVrIpBgpOutdbAtomicAggregate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpOutdbAtomicAggregate.setStatus("mandatory")


class _MscVrIpBgpOutdbAggregatorAs_Type(Unsigned32):
    """Custom type mscVrIpBgpOutdbAggregatorAs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVrIpBgpOutdbAggregatorAs_Type.__name__ = "Unsigned32"
_MscVrIpBgpOutdbAggregatorAs_Object = MibTableColumn
mscVrIpBgpOutdbAggregatorAs = _MscVrIpBgpOutdbAggregatorAs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 9, 10, 1, 9),
    _MscVrIpBgpOutdbAggregatorAs_Type()
)
mscVrIpBgpOutdbAggregatorAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpOutdbAggregatorAs.setStatus("mandatory")
_MscVrIpBgpOutdbAggregatorAddr_Type = IpAddress
_MscVrIpBgpOutdbAggregatorAddr_Object = MibTableColumn
mscVrIpBgpOutdbAggregatorAddr = _MscVrIpBgpOutdbAggregatorAddr_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 9, 10, 1, 10),
    _MscVrIpBgpOutdbAggregatorAddr_Type()
)
mscVrIpBgpOutdbAggregatorAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpOutdbAggregatorAddr.setStatus("mandatory")


class _MscVrIpBgpOutdbAsPath_Type(AsciiString):
    """Custom type mscVrIpBgpOutdbAsPath based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 255),
    )


_MscVrIpBgpOutdbAsPath_Type.__name__ = "AsciiString"
_MscVrIpBgpOutdbAsPath_Object = MibTableColumn
mscVrIpBgpOutdbAsPath = _MscVrIpBgpOutdbAsPath_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 9, 10, 1, 11),
    _MscVrIpBgpOutdbAsPath_Type()
)
mscVrIpBgpOutdbAsPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpOutdbAsPath.setStatus("mandatory")


class _MscVrIpBgpOutdbUnknownAttributes_Type(AsciiString):
    """Custom type mscVrIpBgpOutdbUnknownAttributes based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscVrIpBgpOutdbUnknownAttributes_Type.__name__ = "AsciiString"
_MscVrIpBgpOutdbUnknownAttributes_Object = MibTableColumn
mscVrIpBgpOutdbUnknownAttributes = _MscVrIpBgpOutdbUnknownAttributes_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 9, 10, 1, 12),
    _MscVrIpBgpOutdbUnknownAttributes_Type()
)
mscVrIpBgpOutdbUnknownAttributes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpOutdbUnknownAttributes.setStatus("mandatory")


class _MscVrIpBgpOutdbCommunityPath_Type(AsciiString):
    """Custom type mscVrIpBgpOutdbCommunityPath based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MscVrIpBgpOutdbCommunityPath_Type.__name__ = "AsciiString"
_MscVrIpBgpOutdbCommunityPath_Object = MibTableColumn
mscVrIpBgpOutdbCommunityPath = _MscVrIpBgpOutdbCommunityPath_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 9, 10, 1, 13),
    _MscVrIpBgpOutdbCommunityPath_Type()
)
mscVrIpBgpOutdbCommunityPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpOutdbCommunityPath.setStatus("mandatory")
_MscVrIpBgpOutdbAsOriginatorId_Type = IpAddress
_MscVrIpBgpOutdbAsOriginatorId_Object = MibTableColumn
mscVrIpBgpOutdbAsOriginatorId = _MscVrIpBgpOutdbAsOriginatorId_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 9, 10, 1, 14),
    _MscVrIpBgpOutdbAsOriginatorId_Type()
)
mscVrIpBgpOutdbAsOriginatorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpOutdbAsOriginatorId.setStatus("mandatory")
_MscVrIpBgpOutdbRrClusterListTable_Object = MibTable
mscVrIpBgpOutdbRrClusterListTable = _MscVrIpBgpOutdbRrClusterListTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 9, 799)
)
if mibBuilder.loadTexts:
    mscVrIpBgpOutdbRrClusterListTable.setStatus("mandatory")
_MscVrIpBgpOutdbRrClusterListEntry_Object = MibTableRow
mscVrIpBgpOutdbRrClusterListEntry = _MscVrIpBgpOutdbRrClusterListEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 9, 799, 1)
)
mscVrIpBgpOutdbRrClusterListEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpOutdbPrefixIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpOutdbLengthIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpOutdbPeerIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpOutdbRrClusterListValue"),
)
if mibBuilder.loadTexts:
    mscVrIpBgpOutdbRrClusterListEntry.setStatus("mandatory")
_MscVrIpBgpOutdbRrClusterListValue_Type = IpAddress
_MscVrIpBgpOutdbRrClusterListValue_Object = MibTableColumn
mscVrIpBgpOutdbRrClusterListValue = _MscVrIpBgpOutdbRrClusterListValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 9, 799, 1, 1),
    _MscVrIpBgpOutdbRrClusterListValue_Type()
)
mscVrIpBgpOutdbRrClusterListValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpOutdbRrClusterListValue.setStatus("mandatory")
_MscVrIpBgpProvTable_Object = MibTable
mscVrIpBgpProvTable = _MscVrIpBgpProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 100)
)
if mibBuilder.loadTexts:
    mscVrIpBgpProvTable.setStatus("mandatory")
_MscVrIpBgpProvEntry_Object = MibTableRow
mscVrIpBgpProvEntry = _MscVrIpBgpProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 100, 1)
)
mscVrIpBgpProvEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpBgpProvEntry.setStatus("mandatory")
_MscVrIpBgpBgpIdentifier_Type = IpAddress
_MscVrIpBgpBgpIdentifier_Object = MibTableColumn
mscVrIpBgpBgpIdentifier = _MscVrIpBgpBgpIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 100, 1, 1),
    _MscVrIpBgpBgpIdentifier_Type()
)
mscVrIpBgpBgpIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpBgpBgpIdentifier.setStatus("mandatory")


class _MscVrIpBgpLocalAs_Type(Unsigned32):
    """Custom type mscVrIpBgpLocalAs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MscVrIpBgpLocalAs_Type.__name__ = "Unsigned32"
_MscVrIpBgpLocalAs_Object = MibTableColumn
mscVrIpBgpLocalAs = _MscVrIpBgpLocalAs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 100, 1, 2),
    _MscVrIpBgpLocalAs_Type()
)
mscVrIpBgpLocalAs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpBgpLocalAs.setStatus("mandatory")


class _MscVrIpBgpDefaultLocalPreference_Type(Unsigned32):
    """Custom type mscVrIpBgpDefaultLocalPreference based on Unsigned32"""
    defaultValue = 144

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrIpBgpDefaultLocalPreference_Type.__name__ = "Unsigned32"
_MscVrIpBgpDefaultLocalPreference_Object = MibTableColumn
mscVrIpBgpDefaultLocalPreference = _MscVrIpBgpDefaultLocalPreference_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 100, 1, 3),
    _MscVrIpBgpDefaultLocalPreference_Type()
)
mscVrIpBgpDefaultLocalPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpBgpDefaultLocalPreference.setStatus("mandatory")


class _MscVrIpBgpDefaultMultiExitDisc_Type(Unsigned32):
    """Custom type mscVrIpBgpDefaultMultiExitDisc based on Unsigned32"""
    defaultValue = 4294967294

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_MscVrIpBgpDefaultMultiExitDisc_Type.__name__ = "Unsigned32"
_MscVrIpBgpDefaultMultiExitDisc_Object = MibTableColumn
mscVrIpBgpDefaultMultiExitDisc = _MscVrIpBgpDefaultMultiExitDisc_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 100, 1, 4),
    _MscVrIpBgpDefaultMultiExitDisc_Type()
)
mscVrIpBgpDefaultMultiExitDisc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpBgpDefaultMultiExitDisc.setStatus("mandatory")


class _MscVrIpBgpRouteThrottleLimit_Type(Unsigned32):
    """Custom type mscVrIpBgpRouteThrottleLimit based on Unsigned32"""
    defaultValue = 250

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_MscVrIpBgpRouteThrottleLimit_Type.__name__ = "Unsigned32"
_MscVrIpBgpRouteThrottleLimit_Object = MibTableColumn
mscVrIpBgpRouteThrottleLimit = _MscVrIpBgpRouteThrottleLimit_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 100, 1, 5),
    _MscVrIpBgpRouteThrottleLimit_Type()
)
mscVrIpBgpRouteThrottleLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpBgpRouteThrottleLimit.setStatus("mandatory")


class _MscVrIpBgpRouteThrottleInter_Type(Unsigned32):
    """Custom type mscVrIpBgpRouteThrottleInter based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_MscVrIpBgpRouteThrottleInter_Type.__name__ = "Unsigned32"
_MscVrIpBgpRouteThrottleInter_Object = MibTableColumn
mscVrIpBgpRouteThrottleInter = _MscVrIpBgpRouteThrottleInter_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 100, 1, 6),
    _MscVrIpBgpRouteThrottleInter_Type()
)
mscVrIpBgpRouteThrottleInter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpBgpRouteThrottleInter.setStatus("mandatory")


class _MscVrIpBgpRouteReflector_Type(Integer32):
    """Custom type mscVrIpBgpRouteReflector based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_MscVrIpBgpRouteReflector_Type.__name__ = "Integer32"
_MscVrIpBgpRouteReflector_Object = MibTableColumn
mscVrIpBgpRouteReflector = _MscVrIpBgpRouteReflector_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 100, 1, 7),
    _MscVrIpBgpRouteReflector_Type()
)
mscVrIpBgpRouteReflector.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpBgpRouteReflector.setStatus("mandatory")
_MscVrIpBgpRouteReflectorCluster_Type = IpAddress
_MscVrIpBgpRouteReflectorCluster_Object = MibTableColumn
mscVrIpBgpRouteReflectorCluster = _MscVrIpBgpRouteReflectorCluster_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 100, 1, 8),
    _MscVrIpBgpRouteReflectorCluster_Type()
)
mscVrIpBgpRouteReflectorCluster.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpBgpRouteReflectorCluster.setStatus("mandatory")


class _MscVrIpBgpRedistributeIgpToIbgp_Type(Integer32):
    """Custom type mscVrIpBgpRedistributeIgpToIbgp based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_MscVrIpBgpRedistributeIgpToIbgp_Type.__name__ = "Integer32"
_MscVrIpBgpRedistributeIgpToIbgp_Object = MibTableColumn
mscVrIpBgpRedistributeIgpToIbgp = _MscVrIpBgpRedistributeIgpToIbgp_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 100, 1, 9),
    _MscVrIpBgpRedistributeIgpToIbgp_Type()
)
mscVrIpBgpRedistributeIgpToIbgp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpBgpRedistributeIgpToIbgp.setStatus("mandatory")
_MscVrIpBgpOperTable_Object = MibTable
mscVrIpBgpOperTable = _MscVrIpBgpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 101)
)
if mibBuilder.loadTexts:
    mscVrIpBgpOperTable.setStatus("mandatory")
_MscVrIpBgpOperEntry_Object = MibTableRow
mscVrIpBgpOperEntry = _MscVrIpBgpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 101, 1)
)
mscVrIpBgpOperEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpBgpOperEntry.setStatus("mandatory")
_MscVrIpBgpTableVersion_Type = Counter32
_MscVrIpBgpTableVersion_Object = MibTableColumn
mscVrIpBgpTableVersion = _MscVrIpBgpTableVersion_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 101, 1, 2),
    _MscVrIpBgpTableVersion_Type()
)
mscVrIpBgpTableVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpTableVersion.setStatus("mandatory")
_MscVrIpBgpInMsgs_Type = Counter32
_MscVrIpBgpInMsgs_Object = MibTableColumn
mscVrIpBgpInMsgs = _MscVrIpBgpInMsgs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 101, 1, 3),
    _MscVrIpBgpInMsgs_Type()
)
mscVrIpBgpInMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpInMsgs.setStatus("mandatory")
_MscVrIpBgpInErrors_Type = Counter32
_MscVrIpBgpInErrors_Object = MibTableColumn
mscVrIpBgpInErrors = _MscVrIpBgpInErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 101, 1, 4),
    _MscVrIpBgpInErrors_Type()
)
mscVrIpBgpInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpInErrors.setStatus("mandatory")
_MscVrIpBgpInErrorMsgs_Type = Counter32
_MscVrIpBgpInErrorMsgs_Object = MibTableColumn
mscVrIpBgpInErrorMsgs = _MscVrIpBgpInErrorMsgs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 101, 1, 5),
    _MscVrIpBgpInErrorMsgs_Type()
)
mscVrIpBgpInErrorMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpInErrorMsgs.setStatus("mandatory")
_MscVrIpBgpOutMsgs_Type = Counter32
_MscVrIpBgpOutMsgs_Object = MibTableColumn
mscVrIpBgpOutMsgs = _MscVrIpBgpOutMsgs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 101, 1, 6),
    _MscVrIpBgpOutMsgs_Type()
)
mscVrIpBgpOutMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpOutMsgs.setStatus("mandatory")
_MscVrIpBgpOutDiscards_Type = Counter32
_MscVrIpBgpOutDiscards_Object = MibTableColumn
mscVrIpBgpOutDiscards = _MscVrIpBgpOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 101, 1, 7),
    _MscVrIpBgpOutDiscards_Type()
)
mscVrIpBgpOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpOutDiscards.setStatus("mandatory")
_MscVrIpBgpOutErrorMsgs_Type = Counter32
_MscVrIpBgpOutErrorMsgs_Object = MibTableColumn
mscVrIpBgpOutErrorMsgs = _MscVrIpBgpOutErrorMsgs_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 101, 1, 8),
    _MscVrIpBgpOutErrorMsgs_Type()
)
mscVrIpBgpOutErrorMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpOutErrorMsgs.setStatus("mandatory")
_MscVrIpBgpIndbSize_Type = Counter32
_MscVrIpBgpIndbSize_Object = MibTableColumn
mscVrIpBgpIndbSize = _MscVrIpBgpIndbSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 101, 1, 9),
    _MscVrIpBgpIndbSize_Type()
)
mscVrIpBgpIndbSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpIndbSize.setStatus("mandatory")
_MscVrIpBgpStateTable_Object = MibTable
mscVrIpBgpStateTable = _MscVrIpBgpStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 102)
)
if mibBuilder.loadTexts:
    mscVrIpBgpStateTable.setStatus("mandatory")
_MscVrIpBgpStateEntry_Object = MibTableRow
mscVrIpBgpStateEntry = _MscVrIpBgpStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 102, 1)
)
mscVrIpBgpStateEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpBgpStateEntry.setStatus("mandatory")


class _MscVrIpBgpAdminState_Type(Integer32):
    """Custom type mscVrIpBgpAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("shuttingDown", 2),
          ("unlocked", 1))
    )


_MscVrIpBgpAdminState_Type.__name__ = "Integer32"
_MscVrIpBgpAdminState_Object = MibTableColumn
mscVrIpBgpAdminState = _MscVrIpBgpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 102, 1, 1),
    _MscVrIpBgpAdminState_Type()
)
mscVrIpBgpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpAdminState.setStatus("mandatory")


class _MscVrIpBgpOperationalState_Type(Integer32):
    """Custom type mscVrIpBgpOperationalState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_MscVrIpBgpOperationalState_Type.__name__ = "Integer32"
_MscVrIpBgpOperationalState_Object = MibTableColumn
mscVrIpBgpOperationalState = _MscVrIpBgpOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 102, 1, 2),
    _MscVrIpBgpOperationalState_Type()
)
mscVrIpBgpOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpOperationalState.setStatus("mandatory")


class _MscVrIpBgpUsageState_Type(Integer32):
    """Custom type mscVrIpBgpUsageState based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("busy", 2),
          ("idle", 0))
    )


_MscVrIpBgpUsageState_Type.__name__ = "Integer32"
_MscVrIpBgpUsageState_Object = MibTableColumn
mscVrIpBgpUsageState = _MscVrIpBgpUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 102, 1, 3),
    _MscVrIpBgpUsageState_Type()
)
mscVrIpBgpUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpUsageState.setStatus("mandatory")
_MscVrIpBgpAdminControlTable_Object = MibTable
mscVrIpBgpAdminControlTable = _MscVrIpBgpAdminControlTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 103)
)
if mibBuilder.loadTexts:
    mscVrIpBgpAdminControlTable.setStatus("mandatory")
_MscVrIpBgpAdminControlEntry_Object = MibTableRow
mscVrIpBgpAdminControlEntry = _MscVrIpBgpAdminControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 103, 1)
)
mscVrIpBgpAdminControlEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpBgpAdminControlEntry.setStatus("mandatory")


class _MscVrIpBgpSnmpAdminStatus_Type(Integer32):
    """Custom type mscVrIpBgpSnmpAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_MscVrIpBgpSnmpAdminStatus_Type.__name__ = "Integer32"
_MscVrIpBgpSnmpAdminStatus_Object = MibTableColumn
mscVrIpBgpSnmpAdminStatus = _MscVrIpBgpSnmpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 103, 1, 1),
    _MscVrIpBgpSnmpAdminStatus_Type()
)
mscVrIpBgpSnmpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mscVrIpBgpSnmpAdminStatus.setStatus("mandatory")
_MscVrIpBgpOperStatusTable_Object = MibTable
mscVrIpBgpOperStatusTable = _MscVrIpBgpOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 106)
)
if mibBuilder.loadTexts:
    mscVrIpBgpOperStatusTable.setStatus("mandatory")
_MscVrIpBgpOperStatusEntry_Object = MibTableRow
mscVrIpBgpOperStatusEntry = _MscVrIpBgpOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 106, 1)
)
mscVrIpBgpOperStatusEntry.setIndexNames(
    (0, "Nortel-MsCarrier-MscPassport-VirtualRouterMIB", "mscVrIndex"),
    (0, "Nortel-MsCarrier-MscPassport-IpMIB", "mscVrIpIndex"),
    (0, "Nortel-MsCarrier-MscPassport-BgpMIB", "mscVrIpBgpIndex"),
)
if mibBuilder.loadTexts:
    mscVrIpBgpOperStatusEntry.setStatus("mandatory")


class _MscVrIpBgpSnmpOperStatus_Type(Integer32):
    """Custom type mscVrIpBgpSnmpOperStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_MscVrIpBgpSnmpOperStatus_Type.__name__ = "Integer32"
_MscVrIpBgpSnmpOperStatus_Object = MibTableColumn
mscVrIpBgpSnmpOperStatus = _MscVrIpBgpSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 1, 100, 6, 21, 106, 1, 1),
    _MscVrIpBgpSnmpOperStatus_Type()
)
mscVrIpBgpSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mscVrIpBgpSnmpOperStatus.setStatus("mandatory")
_BgpMIB_ObjectIdentity = ObjectIdentity
bgpMIB = _BgpMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 141)
)
_BgpGroup_ObjectIdentity = ObjectIdentity
bgpGroup = _BgpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 141, 1)
)
_BgpGroupCA_ObjectIdentity = ObjectIdentity
bgpGroupCA = _BgpGroupCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 141, 1, 1)
)
_BgpGroupCA02_ObjectIdentity = ObjectIdentity
bgpGroupCA02 = _BgpGroupCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 141, 1, 1, 3)
)
_BgpGroupCA02A_ObjectIdentity = ObjectIdentity
bgpGroupCA02A = _BgpGroupCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 141, 1, 1, 3, 2)
)
_BgpCapabilities_ObjectIdentity = ObjectIdentity
bgpCapabilities = _BgpCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 141, 3)
)
_BgpCapabilitiesCA_ObjectIdentity = ObjectIdentity
bgpCapabilitiesCA = _BgpCapabilitiesCA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 141, 3, 1)
)
_BgpCapabilitiesCA02_ObjectIdentity = ObjectIdentity
bgpCapabilitiesCA02 = _BgpCapabilitiesCA02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 141, 3, 1, 3)
)
_BgpCapabilitiesCA02A_ObjectIdentity = ObjectIdentity
bgpCapabilitiesCA02A = _BgpCapabilitiesCA02A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 36, 2, 2, 141, 3, 1, 3, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-MsCarrier-MscPassport-BgpMIB",
    **{"mscVrIpBgp": mscVrIpBgp,
       "mscVrIpBgpRowStatusTable": mscVrIpBgpRowStatusTable,
       "mscVrIpBgpRowStatusEntry": mscVrIpBgpRowStatusEntry,
       "mscVrIpBgpRowStatus": mscVrIpBgpRowStatus,
       "mscVrIpBgpComponentName": mscVrIpBgpComponentName,
       "mscVrIpBgpStorageType": mscVrIpBgpStorageType,
       "mscVrIpBgpIndex": mscVrIpBgpIndex,
       "mscVrIpBgpPeer": mscVrIpBgpPeer,
       "mscVrIpBgpPeerRowStatusTable": mscVrIpBgpPeerRowStatusTable,
       "mscVrIpBgpPeerRowStatusEntry": mscVrIpBgpPeerRowStatusEntry,
       "mscVrIpBgpPeerRowStatus": mscVrIpBgpPeerRowStatus,
       "mscVrIpBgpPeerComponentName": mscVrIpBgpPeerComponentName,
       "mscVrIpBgpPeerStorageType": mscVrIpBgpPeerStorageType,
       "mscVrIpBgpPeerPeerAddressIndex": mscVrIpBgpPeerPeerAddressIndex,
       "mscVrIpBgpPeerProvTable": mscVrIpBgpPeerProvTable,
       "mscVrIpBgpPeerProvEntry": mscVrIpBgpPeerProvEntry,
       "mscVrIpBgpPeerPeerAs": mscVrIpBgpPeerPeerAs,
       "mscVrIpBgpPeerLocalAddressConfigured": mscVrIpBgpPeerLocalAddressConfigured,
       "mscVrIpBgpPeerKeepAliveConfigured": mscVrIpBgpPeerKeepAliveConfigured,
       "mscVrIpBgpPeerHoldTimeConfigured": mscVrIpBgpPeerHoldTimeConfigured,
       "mscVrIpBgpPeerConnectRetryTime": mscVrIpBgpPeerConnectRetryTime,
       "mscVrIpBgpPeerMinAsOrigTime": mscVrIpBgpPeerMinAsOrigTime,
       "mscVrIpBgpPeerMinRouteAdvTime": mscVrIpBgpPeerMinRouteAdvTime,
       "mscVrIpBgpPeerDefaultInAggMed": mscVrIpBgpPeerDefaultInAggMed,
       "mscVrIpBgpPeerIsRouteReflectorClient": mscVrIpBgpPeerIsRouteReflectorClient,
       "mscVrIpBgpPeerRemovePrivateAs": mscVrIpBgpPeerRemovePrivateAs,
       "mscVrIpBgpPeerStateTable": mscVrIpBgpPeerStateTable,
       "mscVrIpBgpPeerStateEntry": mscVrIpBgpPeerStateEntry,
       "mscVrIpBgpPeerAdminState": mscVrIpBgpPeerAdminState,
       "mscVrIpBgpPeerOperationalState": mscVrIpBgpPeerOperationalState,
       "mscVrIpBgpPeerUsageState": mscVrIpBgpPeerUsageState,
       "mscVrIpBgpPeerOperTable": mscVrIpBgpPeerOperTable,
       "mscVrIpBgpPeerOperEntry": mscVrIpBgpPeerOperEntry,
       "mscVrIpBgpPeerConnectionState": mscVrIpBgpPeerConnectionState,
       "mscVrIpBgpPeerBgpIdentifier": mscVrIpBgpPeerBgpIdentifier,
       "mscVrIpBgpPeerVersionNegotiated": mscVrIpBgpPeerVersionNegotiated,
       "mscVrIpBgpPeerHoldTimeNegotiated": mscVrIpBgpPeerHoldTimeNegotiated,
       "mscVrIpBgpPeerKeepAliveNegotiated": mscVrIpBgpPeerKeepAliveNegotiated,
       "mscVrIpBgpPeerLocalAddressUsed": mscVrIpBgpPeerLocalAddressUsed,
       "mscVrIpBgpPeerLocalPort": mscVrIpBgpPeerLocalPort,
       "mscVrIpBgpPeerRemotePort": mscVrIpBgpPeerRemotePort,
       "mscVrIpBgpPeerLastError": mscVrIpBgpPeerLastError,
       "mscVrIpBgpPeerConnectionEstablishedTime": mscVrIpBgpPeerConnectionEstablishedTime,
       "mscVrIpBgpPeerConnectionEstablishedTransitions": mscVrIpBgpPeerConnectionEstablishedTransitions,
       "mscVrIpBgpPeerInUpdateElapsedTime": mscVrIpBgpPeerInUpdateElapsedTime,
       "mscVrIpBgpPeerInMsgs": mscVrIpBgpPeerInMsgs,
       "mscVrIpBgpPeerInUpdates": mscVrIpBgpPeerInUpdates,
       "mscVrIpBgpPeerInErrors": mscVrIpBgpPeerInErrors,
       "mscVrIpBgpPeerInErrorMsgs": mscVrIpBgpPeerInErrorMsgs,
       "mscVrIpBgpPeerOutMsgs": mscVrIpBgpPeerOutMsgs,
       "mscVrIpBgpPeerOutUpdates": mscVrIpBgpPeerOutUpdates,
       "mscVrIpBgpPeerOutDiscards": mscVrIpBgpPeerOutDiscards,
       "mscVrIpBgpPeerOutErrorMsgs": mscVrIpBgpPeerOutErrorMsgs,
       "mscVrIpBgpPeerInRoutes": mscVrIpBgpPeerInRoutes,
       "mscVrIpBgpImport": mscVrIpBgpImport,
       "mscVrIpBgpImportRowStatusTable": mscVrIpBgpImportRowStatusTable,
       "mscVrIpBgpImportRowStatusEntry": mscVrIpBgpImportRowStatusEntry,
       "mscVrIpBgpImportRowStatus": mscVrIpBgpImportRowStatus,
       "mscVrIpBgpImportComponentName": mscVrIpBgpImportComponentName,
       "mscVrIpBgpImportStorageType": mscVrIpBgpImportStorageType,
       "mscVrIpBgpImportIndex": mscVrIpBgpImportIndex,
       "mscVrIpBgpImportNet": mscVrIpBgpImportNet,
       "mscVrIpBgpImportNetRowStatusTable": mscVrIpBgpImportNetRowStatusTable,
       "mscVrIpBgpImportNetRowStatusEntry": mscVrIpBgpImportNetRowStatusEntry,
       "mscVrIpBgpImportNetRowStatus": mscVrIpBgpImportNetRowStatus,
       "mscVrIpBgpImportNetComponentName": mscVrIpBgpImportNetComponentName,
       "mscVrIpBgpImportNetStorageType": mscVrIpBgpImportNetStorageType,
       "mscVrIpBgpImportNetIndex": mscVrIpBgpImportNetIndex,
       "mscVrIpBgpImportNetProvTable": mscVrIpBgpImportNetProvTable,
       "mscVrIpBgpImportNetProvEntry": mscVrIpBgpImportNetProvEntry,
       "mscVrIpBgpImportNetPrefix": mscVrIpBgpImportNetPrefix,
       "mscVrIpBgpImportNetLength": mscVrIpBgpImportNetLength,
       "mscVrIpBgpImportProvTable": mscVrIpBgpImportProvTable,
       "mscVrIpBgpImportProvEntry": mscVrIpBgpImportProvEntry,
       "mscVrIpBgpImportPeerAs": mscVrIpBgpImportPeerAs,
       "mscVrIpBgpImportPeerIpAddress": mscVrIpBgpImportPeerIpAddress,
       "mscVrIpBgpImportOriginAs": mscVrIpBgpImportOriginAs,
       "mscVrIpBgpImportOriginProtocol": mscVrIpBgpImportOriginProtocol,
       "mscVrIpBgpImportUsageFlag": mscVrIpBgpImportUsageFlag,
       "mscVrIpBgpImportLocalPreference": mscVrIpBgpImportLocalPreference,
       "mscVrIpBgpImportPreferredOver": mscVrIpBgpImportPreferredOver,
       "mscVrIpBgpImportAsPathExpression": mscVrIpBgpImportAsPathExpression,
       "mscVrIpBgpImportCommunityExpression": mscVrIpBgpImportCommunityExpression,
       "mscVrIpBgpImportExpressPreference": mscVrIpBgpImportExpressPreference,
       "mscVrIpBgpImportAppendCommunity": mscVrIpBgpImportAppendCommunity,
       "mscVrIpBgpExport": mscVrIpBgpExport,
       "mscVrIpBgpExportRowStatusTable": mscVrIpBgpExportRowStatusTable,
       "mscVrIpBgpExportRowStatusEntry": mscVrIpBgpExportRowStatusEntry,
       "mscVrIpBgpExportRowStatus": mscVrIpBgpExportRowStatus,
       "mscVrIpBgpExportComponentName": mscVrIpBgpExportComponentName,
       "mscVrIpBgpExportStorageType": mscVrIpBgpExportStorageType,
       "mscVrIpBgpExportIndex": mscVrIpBgpExportIndex,
       "mscVrIpBgpExportNet": mscVrIpBgpExportNet,
       "mscVrIpBgpExportNetRowStatusTable": mscVrIpBgpExportNetRowStatusTable,
       "mscVrIpBgpExportNetRowStatusEntry": mscVrIpBgpExportNetRowStatusEntry,
       "mscVrIpBgpExportNetRowStatus": mscVrIpBgpExportNetRowStatus,
       "mscVrIpBgpExportNetComponentName": mscVrIpBgpExportNetComponentName,
       "mscVrIpBgpExportNetStorageType": mscVrIpBgpExportNetStorageType,
       "mscVrIpBgpExportNetIndex": mscVrIpBgpExportNetIndex,
       "mscVrIpBgpExportNetProvTable": mscVrIpBgpExportNetProvTable,
       "mscVrIpBgpExportNetProvEntry": mscVrIpBgpExportNetProvEntry,
       "mscVrIpBgpExportNetPrefix": mscVrIpBgpExportNetPrefix,
       "mscVrIpBgpExportNetLength": mscVrIpBgpExportNetLength,
       "mscVrIpBgpExportProvTable": mscVrIpBgpExportProvTable,
       "mscVrIpBgpExportProvEntry": mscVrIpBgpExportProvEntry,
       "mscVrIpBgpExportPeerAs": mscVrIpBgpExportPeerAs,
       "mscVrIpBgpExportPeerIpAddress": mscVrIpBgpExportPeerIpAddress,
       "mscVrIpBgpExportProtocol": mscVrIpBgpExportProtocol,
       "mscVrIpBgpExportEgpAsId": mscVrIpBgpExportEgpAsId,
       "mscVrIpBgpExportBgpAsId": mscVrIpBgpExportBgpAsId,
       "mscVrIpBgpExportOspfTag": mscVrIpBgpExportOspfTag,
       "mscVrIpBgpExportRipInterface": mscVrIpBgpExportRipInterface,
       "mscVrIpBgpExportRipNeighbor": mscVrIpBgpExportRipNeighbor,
       "mscVrIpBgpExportAdvertiseStatus": mscVrIpBgpExportAdvertiseStatus,
       "mscVrIpBgpExportMultiExitDisc": mscVrIpBgpExportMultiExitDisc,
       "mscVrIpBgpExportSendMultiExitDiscToEbgp": mscVrIpBgpExportSendMultiExitDiscToEbgp,
       "mscVrIpBgpExportAsPathExpression": mscVrIpBgpExportAsPathExpression,
       "mscVrIpBgpExportCommunityExpression": mscVrIpBgpExportCommunityExpression,
       "mscVrIpBgpExportExpressPreference": mscVrIpBgpExportExpressPreference,
       "mscVrIpBgpExportSendCommunity": mscVrIpBgpExportSendCommunity,
       "mscVrIpBgpExportInsertDummyAs": mscVrIpBgpExportInsertDummyAs,
       "mscVrIpBgpAs": mscVrIpBgpAs,
       "mscVrIpBgpAsRowStatusTable": mscVrIpBgpAsRowStatusTable,
       "mscVrIpBgpAsRowStatusEntry": mscVrIpBgpAsRowStatusEntry,
       "mscVrIpBgpAsRowStatus": mscVrIpBgpAsRowStatus,
       "mscVrIpBgpAsComponentName": mscVrIpBgpAsComponentName,
       "mscVrIpBgpAsStorageType": mscVrIpBgpAsStorageType,
       "mscVrIpBgpAsIndex": mscVrIpBgpAsIndex,
       "mscVrIpBgpAsProvTable": mscVrIpBgpAsProvTable,
       "mscVrIpBgpAsProvEntry": mscVrIpBgpAsProvEntry,
       "mscVrIpBgpAsWeight": mscVrIpBgpAsWeight,
       "mscVrIpBgpAggregate": mscVrIpBgpAggregate,
       "mscVrIpBgpAggregateRowStatusTable": mscVrIpBgpAggregateRowStatusTable,
       "mscVrIpBgpAggregateRowStatusEntry": mscVrIpBgpAggregateRowStatusEntry,
       "mscVrIpBgpAggregateRowStatus": mscVrIpBgpAggregateRowStatus,
       "mscVrIpBgpAggregateComponentName": mscVrIpBgpAggregateComponentName,
       "mscVrIpBgpAggregateStorageType": mscVrIpBgpAggregateStorageType,
       "mscVrIpBgpAggregatePrefixIndex": mscVrIpBgpAggregatePrefixIndex,
       "mscVrIpBgpAggregateLengthIndex": mscVrIpBgpAggregateLengthIndex,
       "mscVrIpBgpAggregateNet": mscVrIpBgpAggregateNet,
       "mscVrIpBgpAggregateNetRowStatusTable": mscVrIpBgpAggregateNetRowStatusTable,
       "mscVrIpBgpAggregateNetRowStatusEntry": mscVrIpBgpAggregateNetRowStatusEntry,
       "mscVrIpBgpAggregateNetRowStatus": mscVrIpBgpAggregateNetRowStatus,
       "mscVrIpBgpAggregateNetComponentName": mscVrIpBgpAggregateNetComponentName,
       "mscVrIpBgpAggregateNetStorageType": mscVrIpBgpAggregateNetStorageType,
       "mscVrIpBgpAggregateNetIndex": mscVrIpBgpAggregateNetIndex,
       "mscVrIpBgpAggregateNetProvTable": mscVrIpBgpAggregateNetProvTable,
       "mscVrIpBgpAggregateNetProvEntry": mscVrIpBgpAggregateNetProvEntry,
       "mscVrIpBgpAggregateNetPrefix": mscVrIpBgpAggregateNetPrefix,
       "mscVrIpBgpAggregateNetLength": mscVrIpBgpAggregateNetLength,
       "mscVrIpBgpAggregateNetProtocol": mscVrIpBgpAggregateNetProtocol,
       "mscVrIpBgpAggregateNetEgpAsId": mscVrIpBgpAggregateNetEgpAsId,
       "mscVrIpBgpAggregateNetBgpAsId": mscVrIpBgpAggregateNetBgpAsId,
       "mscVrIpBgpAggregateNetOspfTag": mscVrIpBgpAggregateNetOspfTag,
       "mscVrIpBgpAggregateNetRipInterface": mscVrIpBgpAggregateNetRipInterface,
       "mscVrIpBgpAggregateNetAction": mscVrIpBgpAggregateNetAction,
       "mscVrIpBgpIndb": mscVrIpBgpIndb,
       "mscVrIpBgpIndbRowStatusTable": mscVrIpBgpIndbRowStatusTable,
       "mscVrIpBgpIndbRowStatusEntry": mscVrIpBgpIndbRowStatusEntry,
       "mscVrIpBgpIndbRowStatus": mscVrIpBgpIndbRowStatus,
       "mscVrIpBgpIndbComponentName": mscVrIpBgpIndbComponentName,
       "mscVrIpBgpIndbStorageType": mscVrIpBgpIndbStorageType,
       "mscVrIpBgpIndbPrefixIndex": mscVrIpBgpIndbPrefixIndex,
       "mscVrIpBgpIndbLengthIndex": mscVrIpBgpIndbLengthIndex,
       "mscVrIpBgpIndbPeerIndex": mscVrIpBgpIndbPeerIndex,
       "mscVrIpBgpIndbOperTable": mscVrIpBgpIndbOperTable,
       "mscVrIpBgpIndbOperEntry": mscVrIpBgpIndbOperEntry,
       "mscVrIpBgpIndbOrigin": mscVrIpBgpIndbOrigin,
       "mscVrIpBgpIndbInLocaldb": mscVrIpBgpIndbInLocaldb,
       "mscVrIpBgpIndbNextHop": mscVrIpBgpIndbNextHop,
       "mscVrIpBgpIndbLocalPreference": mscVrIpBgpIndbLocalPreference,
       "mscVrIpBgpIndbCalcLocalPref": mscVrIpBgpIndbCalcLocalPref,
       "mscVrIpBgpIndbMultiExitDiscriminator": mscVrIpBgpIndbMultiExitDiscriminator,
       "mscVrIpBgpIndbAtomicAggregate": mscVrIpBgpIndbAtomicAggregate,
       "mscVrIpBgpIndbAggregatorAs": mscVrIpBgpIndbAggregatorAs,
       "mscVrIpBgpIndbAggregatorAddr": mscVrIpBgpIndbAggregatorAddr,
       "mscVrIpBgpIndbAsPath": mscVrIpBgpIndbAsPath,
       "mscVrIpBgpIndbUnknownAttributes": mscVrIpBgpIndbUnknownAttributes,
       "mscVrIpBgpIndbCommunityPath": mscVrIpBgpIndbCommunityPath,
       "mscVrIpBgpIndbAsOriginatorId": mscVrIpBgpIndbAsOriginatorId,
       "mscVrIpBgpIndbRrClusterListTable": mscVrIpBgpIndbRrClusterListTable,
       "mscVrIpBgpIndbRrClusterListEntry": mscVrIpBgpIndbRrClusterListEntry,
       "mscVrIpBgpIndbRrClusterListValue": mscVrIpBgpIndbRrClusterListValue,
       "mscVrIpBgpLocaldb": mscVrIpBgpLocaldb,
       "mscVrIpBgpLocaldbRowStatusTable": mscVrIpBgpLocaldbRowStatusTable,
       "mscVrIpBgpLocaldbRowStatusEntry": mscVrIpBgpLocaldbRowStatusEntry,
       "mscVrIpBgpLocaldbRowStatus": mscVrIpBgpLocaldbRowStatus,
       "mscVrIpBgpLocaldbComponentName": mscVrIpBgpLocaldbComponentName,
       "mscVrIpBgpLocaldbStorageType": mscVrIpBgpLocaldbStorageType,
       "mscVrIpBgpLocaldbPrefixIndex": mscVrIpBgpLocaldbPrefixIndex,
       "mscVrIpBgpLocaldbLengthIndex": mscVrIpBgpLocaldbLengthIndex,
       "mscVrIpBgpLocaldbPeerIndex": mscVrIpBgpLocaldbPeerIndex,
       "mscVrIpBgpLocaldbOperTable": mscVrIpBgpLocaldbOperTable,
       "mscVrIpBgpLocaldbOperEntry": mscVrIpBgpLocaldbOperEntry,
       "mscVrIpBgpLocaldbOrigin": mscVrIpBgpLocaldbOrigin,
       "mscVrIpBgpLocaldbNextHop": mscVrIpBgpLocaldbNextHop,
       "mscVrIpBgpLocaldbLocalPreference": mscVrIpBgpLocaldbLocalPreference,
       "mscVrIpBgpLocaldbMultiExitDiscriminator": mscVrIpBgpLocaldbMultiExitDiscriminator,
       "mscVrIpBgpLocaldbAtomicAggregate": mscVrIpBgpLocaldbAtomicAggregate,
       "mscVrIpBgpLocaldbAggregatorAs": mscVrIpBgpLocaldbAggregatorAs,
       "mscVrIpBgpLocaldbAggregatorAddr": mscVrIpBgpLocaldbAggregatorAddr,
       "mscVrIpBgpLocaldbAsPath": mscVrIpBgpLocaldbAsPath,
       "mscVrIpBgpLocaldbUnknownAttributes": mscVrIpBgpLocaldbUnknownAttributes,
       "mscVrIpBgpLocaldbCommunityPath": mscVrIpBgpLocaldbCommunityPath,
       "mscVrIpBgpLocaldbAsOriginatorId": mscVrIpBgpLocaldbAsOriginatorId,
       "mscVrIpBgpLocaldbRrClusterListTable": mscVrIpBgpLocaldbRrClusterListTable,
       "mscVrIpBgpLocaldbRrClusterListEntry": mscVrIpBgpLocaldbRrClusterListEntry,
       "mscVrIpBgpLocaldbRrClusterListValue": mscVrIpBgpLocaldbRrClusterListValue,
       "mscVrIpBgpOutdb": mscVrIpBgpOutdb,
       "mscVrIpBgpOutdbRowStatusTable": mscVrIpBgpOutdbRowStatusTable,
       "mscVrIpBgpOutdbRowStatusEntry": mscVrIpBgpOutdbRowStatusEntry,
       "mscVrIpBgpOutdbRowStatus": mscVrIpBgpOutdbRowStatus,
       "mscVrIpBgpOutdbComponentName": mscVrIpBgpOutdbComponentName,
       "mscVrIpBgpOutdbStorageType": mscVrIpBgpOutdbStorageType,
       "mscVrIpBgpOutdbPrefixIndex": mscVrIpBgpOutdbPrefixIndex,
       "mscVrIpBgpOutdbLengthIndex": mscVrIpBgpOutdbLengthIndex,
       "mscVrIpBgpOutdbPeerIndex": mscVrIpBgpOutdbPeerIndex,
       "mscVrIpBgpOutdbOperTable": mscVrIpBgpOutdbOperTable,
       "mscVrIpBgpOutdbOperEntry": mscVrIpBgpOutdbOperEntry,
       "mscVrIpBgpOutdbOrigin": mscVrIpBgpOutdbOrigin,
       "mscVrIpBgpOutdbNextHop": mscVrIpBgpOutdbNextHop,
       "mscVrIpBgpOutdbLocalPreference": mscVrIpBgpOutdbLocalPreference,
       "mscVrIpBgpOutdbMultiExitDiscriminator": mscVrIpBgpOutdbMultiExitDiscriminator,
       "mscVrIpBgpOutdbAtomicAggregate": mscVrIpBgpOutdbAtomicAggregate,
       "mscVrIpBgpOutdbAggregatorAs": mscVrIpBgpOutdbAggregatorAs,
       "mscVrIpBgpOutdbAggregatorAddr": mscVrIpBgpOutdbAggregatorAddr,
       "mscVrIpBgpOutdbAsPath": mscVrIpBgpOutdbAsPath,
       "mscVrIpBgpOutdbUnknownAttributes": mscVrIpBgpOutdbUnknownAttributes,
       "mscVrIpBgpOutdbCommunityPath": mscVrIpBgpOutdbCommunityPath,
       "mscVrIpBgpOutdbAsOriginatorId": mscVrIpBgpOutdbAsOriginatorId,
       "mscVrIpBgpOutdbRrClusterListTable": mscVrIpBgpOutdbRrClusterListTable,
       "mscVrIpBgpOutdbRrClusterListEntry": mscVrIpBgpOutdbRrClusterListEntry,
       "mscVrIpBgpOutdbRrClusterListValue": mscVrIpBgpOutdbRrClusterListValue,
       "mscVrIpBgpProvTable": mscVrIpBgpProvTable,
       "mscVrIpBgpProvEntry": mscVrIpBgpProvEntry,
       "mscVrIpBgpBgpIdentifier": mscVrIpBgpBgpIdentifier,
       "mscVrIpBgpLocalAs": mscVrIpBgpLocalAs,
       "mscVrIpBgpDefaultLocalPreference": mscVrIpBgpDefaultLocalPreference,
       "mscVrIpBgpDefaultMultiExitDisc": mscVrIpBgpDefaultMultiExitDisc,
       "mscVrIpBgpRouteThrottleLimit": mscVrIpBgpRouteThrottleLimit,
       "mscVrIpBgpRouteThrottleInter": mscVrIpBgpRouteThrottleInter,
       "mscVrIpBgpRouteReflector": mscVrIpBgpRouteReflector,
       "mscVrIpBgpRouteReflectorCluster": mscVrIpBgpRouteReflectorCluster,
       "mscVrIpBgpRedistributeIgpToIbgp": mscVrIpBgpRedistributeIgpToIbgp,
       "mscVrIpBgpOperTable": mscVrIpBgpOperTable,
       "mscVrIpBgpOperEntry": mscVrIpBgpOperEntry,
       "mscVrIpBgpTableVersion": mscVrIpBgpTableVersion,
       "mscVrIpBgpInMsgs": mscVrIpBgpInMsgs,
       "mscVrIpBgpInErrors": mscVrIpBgpInErrors,
       "mscVrIpBgpInErrorMsgs": mscVrIpBgpInErrorMsgs,
       "mscVrIpBgpOutMsgs": mscVrIpBgpOutMsgs,
       "mscVrIpBgpOutDiscards": mscVrIpBgpOutDiscards,
       "mscVrIpBgpOutErrorMsgs": mscVrIpBgpOutErrorMsgs,
       "mscVrIpBgpIndbSize": mscVrIpBgpIndbSize,
       "mscVrIpBgpStateTable": mscVrIpBgpStateTable,
       "mscVrIpBgpStateEntry": mscVrIpBgpStateEntry,
       "mscVrIpBgpAdminState": mscVrIpBgpAdminState,
       "mscVrIpBgpOperationalState": mscVrIpBgpOperationalState,
       "mscVrIpBgpUsageState": mscVrIpBgpUsageState,
       "mscVrIpBgpAdminControlTable": mscVrIpBgpAdminControlTable,
       "mscVrIpBgpAdminControlEntry": mscVrIpBgpAdminControlEntry,
       "mscVrIpBgpSnmpAdminStatus": mscVrIpBgpSnmpAdminStatus,
       "mscVrIpBgpOperStatusTable": mscVrIpBgpOperStatusTable,
       "mscVrIpBgpOperStatusEntry": mscVrIpBgpOperStatusEntry,
       "mscVrIpBgpSnmpOperStatus": mscVrIpBgpSnmpOperStatus,
       "bgpMIB": bgpMIB,
       "bgpGroup": bgpGroup,
       "bgpGroupCA": bgpGroupCA,
       "bgpGroupCA02": bgpGroupCA02,
       "bgpGroupCA02A": bgpGroupCA02A,
       "bgpCapabilities": bgpCapabilities,
       "bgpCapabilitiesCA": bgpCapabilitiesCA,
       "bgpCapabilitiesCA02": bgpCapabilitiesCA02,
       "bgpCapabilitiesCA02A": bgpCapabilitiesCA02A}
)
