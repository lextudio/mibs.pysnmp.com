# SNMP MIB module (Nortel-Magellan-Passport-BgpMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Nortel-Magellan-Passport-BgpMIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:30:26 2024
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

(vrIp,
 vrIpIndex) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-IpMIB",
    "vrIp",
    "vrIpIndex")

(Counter32,
 DisplayString,
 Gauge32,
 Integer32,
 RowStatus,
 StorageType,
 Unsigned32) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-StandardTextualConventionsMIB",
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
    "Nortel-Magellan-Passport-TextualConventionsMIB",
    "AsciiString",
    "Hex",
    "HexString",
    "IntegerSequence",
    "NonReplicated")

(passportMIBs,) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-UsefulDefinitionsMIB",
    "passportMIBs")

(vrIndex,) = mibBuilder.importSymbols(
    "Nortel-Magellan-Passport-VirtualRouterMIB",
    "vrIndex")

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

_VrIpBgp_ObjectIdentity = ObjectIdentity
vrIpBgp = _VrIpBgp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21)
)
_VrIpBgpRowStatusTable_Object = MibTable
vrIpBgpRowStatusTable = _VrIpBgpRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 1)
)
if mibBuilder.loadTexts:
    vrIpBgpRowStatusTable.setStatus("mandatory")
_VrIpBgpRowStatusEntry_Object = MibTableRow
vrIpBgpRowStatusEntry = _VrIpBgpRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 1, 1)
)
vrIpBgpRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpIndex"),
)
if mibBuilder.loadTexts:
    vrIpBgpRowStatusEntry.setStatus("mandatory")
_VrIpBgpRowStatus_Type = RowStatus
_VrIpBgpRowStatus_Object = MibTableColumn
vrIpBgpRowStatus = _VrIpBgpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 1, 1, 1),
    _VrIpBgpRowStatus_Type()
)
vrIpBgpRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpBgpRowStatus.setStatus("mandatory")
_VrIpBgpComponentName_Type = DisplayString
_VrIpBgpComponentName_Object = MibTableColumn
vrIpBgpComponentName = _VrIpBgpComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 1, 1, 2),
    _VrIpBgpComponentName_Type()
)
vrIpBgpComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpComponentName.setStatus("mandatory")
_VrIpBgpStorageType_Type = StorageType
_VrIpBgpStorageType_Object = MibTableColumn
vrIpBgpStorageType = _VrIpBgpStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 1, 1, 4),
    _VrIpBgpStorageType_Type()
)
vrIpBgpStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpStorageType.setStatus("mandatory")
_VrIpBgpIndex_Type = NonReplicated
_VrIpBgpIndex_Object = MibTableColumn
vrIpBgpIndex = _VrIpBgpIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 1, 1, 10),
    _VrIpBgpIndex_Type()
)
vrIpBgpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpBgpIndex.setStatus("mandatory")
_VrIpBgpPeer_ObjectIdentity = ObjectIdentity
vrIpBgpPeer = _VrIpBgpPeer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 2)
)
_VrIpBgpPeerRowStatusTable_Object = MibTable
vrIpBgpPeerRowStatusTable = _VrIpBgpPeerRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 2, 1)
)
if mibBuilder.loadTexts:
    vrIpBgpPeerRowStatusTable.setStatus("mandatory")
_VrIpBgpPeerRowStatusEntry_Object = MibTableRow
vrIpBgpPeerRowStatusEntry = _VrIpBgpPeerRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 2, 1, 1)
)
vrIpBgpPeerRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpPeerPeerAddressIndex"),
)
if mibBuilder.loadTexts:
    vrIpBgpPeerRowStatusEntry.setStatus("mandatory")
_VrIpBgpPeerRowStatus_Type = RowStatus
_VrIpBgpPeerRowStatus_Object = MibTableColumn
vrIpBgpPeerRowStatus = _VrIpBgpPeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 2, 1, 1, 1),
    _VrIpBgpPeerRowStatus_Type()
)
vrIpBgpPeerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpBgpPeerRowStatus.setStatus("mandatory")
_VrIpBgpPeerComponentName_Type = DisplayString
_VrIpBgpPeerComponentName_Object = MibTableColumn
vrIpBgpPeerComponentName = _VrIpBgpPeerComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 2, 1, 1, 2),
    _VrIpBgpPeerComponentName_Type()
)
vrIpBgpPeerComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpPeerComponentName.setStatus("mandatory")
_VrIpBgpPeerStorageType_Type = StorageType
_VrIpBgpPeerStorageType_Object = MibTableColumn
vrIpBgpPeerStorageType = _VrIpBgpPeerStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 2, 1, 1, 4),
    _VrIpBgpPeerStorageType_Type()
)
vrIpBgpPeerStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpPeerStorageType.setStatus("mandatory")
_VrIpBgpPeerPeerAddressIndex_Type = IpAddress
_VrIpBgpPeerPeerAddressIndex_Object = MibTableColumn
vrIpBgpPeerPeerAddressIndex = _VrIpBgpPeerPeerAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 2, 1, 1, 10),
    _VrIpBgpPeerPeerAddressIndex_Type()
)
vrIpBgpPeerPeerAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpBgpPeerPeerAddressIndex.setStatus("mandatory")
_VrIpBgpPeerProvTable_Object = MibTable
vrIpBgpPeerProvTable = _VrIpBgpPeerProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 2, 10)
)
if mibBuilder.loadTexts:
    vrIpBgpPeerProvTable.setStatus("mandatory")
_VrIpBgpPeerProvEntry_Object = MibTableRow
vrIpBgpPeerProvEntry = _VrIpBgpPeerProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 2, 10, 1)
)
vrIpBgpPeerProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpPeerPeerAddressIndex"),
)
if mibBuilder.loadTexts:
    vrIpBgpPeerProvEntry.setStatus("mandatory")


class _VrIpBgpPeerPeerAs_Type(Unsigned32):
    """Custom type vrIpBgpPeerPeerAs based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VrIpBgpPeerPeerAs_Type.__name__ = "Unsigned32"
_VrIpBgpPeerPeerAs_Object = MibTableColumn
vrIpBgpPeerPeerAs = _VrIpBgpPeerPeerAs_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 2, 10, 1, 1),
    _VrIpBgpPeerPeerAs_Type()
)
vrIpBgpPeerPeerAs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpBgpPeerPeerAs.setStatus("mandatory")


class _VrIpBgpPeerLocalAddressConfigured_Type(IpAddress):
    """Custom type vrIpBgpPeerLocalAddressConfigured based on IpAddress"""
    defaultHexValue = "00000000"


_VrIpBgpPeerLocalAddressConfigured_Object = MibTableColumn
vrIpBgpPeerLocalAddressConfigured = _VrIpBgpPeerLocalAddressConfigured_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 2, 10, 1, 2),
    _VrIpBgpPeerLocalAddressConfigured_Type()
)
vrIpBgpPeerLocalAddressConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpBgpPeerLocalAddressConfigured.setStatus("mandatory")


class _VrIpBgpPeerKeepAliveConfigured_Type(Unsigned32):
    """Custom type vrIpBgpPeerKeepAliveConfigured based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 21845),
    )


_VrIpBgpPeerKeepAliveConfigured_Type.__name__ = "Unsigned32"
_VrIpBgpPeerKeepAliveConfigured_Object = MibTableColumn
vrIpBgpPeerKeepAliveConfigured = _VrIpBgpPeerKeepAliveConfigured_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 2, 10, 1, 3),
    _VrIpBgpPeerKeepAliveConfigured_Type()
)
vrIpBgpPeerKeepAliveConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpBgpPeerKeepAliveConfigured.setStatus("mandatory")


class _VrIpBgpPeerHoldTimeConfigured_Type(Unsigned32):
    """Custom type vrIpBgpPeerHoldTimeConfigured based on Unsigned32"""
    defaultValue = 90

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 65535),
    )


_VrIpBgpPeerHoldTimeConfigured_Type.__name__ = "Unsigned32"
_VrIpBgpPeerHoldTimeConfigured_Object = MibTableColumn
vrIpBgpPeerHoldTimeConfigured = _VrIpBgpPeerHoldTimeConfigured_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 2, 10, 1, 4),
    _VrIpBgpPeerHoldTimeConfigured_Type()
)
vrIpBgpPeerHoldTimeConfigured.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpBgpPeerHoldTimeConfigured.setStatus("mandatory")


class _VrIpBgpPeerConnectRetryTime_Type(Unsigned32):
    """Custom type vrIpBgpPeerConnectRetryTime based on Unsigned32"""
    defaultValue = 120

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VrIpBgpPeerConnectRetryTime_Type.__name__ = "Unsigned32"
_VrIpBgpPeerConnectRetryTime_Object = MibTableColumn
vrIpBgpPeerConnectRetryTime = _VrIpBgpPeerConnectRetryTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 2, 10, 1, 5),
    _VrIpBgpPeerConnectRetryTime_Type()
)
vrIpBgpPeerConnectRetryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpBgpPeerConnectRetryTime.setStatus("mandatory")


class _VrIpBgpPeerMinAsOrigTime_Type(Unsigned32):
    """Custom type vrIpBgpPeerMinAsOrigTime based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VrIpBgpPeerMinAsOrigTime_Type.__name__ = "Unsigned32"
_VrIpBgpPeerMinAsOrigTime_Object = MibTableColumn
vrIpBgpPeerMinAsOrigTime = _VrIpBgpPeerMinAsOrigTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 2, 10, 1, 6),
    _VrIpBgpPeerMinAsOrigTime_Type()
)
vrIpBgpPeerMinAsOrigTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpBgpPeerMinAsOrigTime.setStatus("mandatory")


class _VrIpBgpPeerMinRouteAdvTime_Type(Unsigned32):
    """Custom type vrIpBgpPeerMinRouteAdvTime based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VrIpBgpPeerMinRouteAdvTime_Type.__name__ = "Unsigned32"
_VrIpBgpPeerMinRouteAdvTime_Object = MibTableColumn
vrIpBgpPeerMinRouteAdvTime = _VrIpBgpPeerMinRouteAdvTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 2, 10, 1, 7),
    _VrIpBgpPeerMinRouteAdvTime_Type()
)
vrIpBgpPeerMinRouteAdvTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpBgpPeerMinRouteAdvTime.setStatus("mandatory")


class _VrIpBgpPeerDefaultInAggMed_Type(Unsigned32):
    """Custom type vrIpBgpPeerDefaultInAggMed based on Unsigned32"""
    defaultValue = 4294967295

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrIpBgpPeerDefaultInAggMed_Type.__name__ = "Unsigned32"
_VrIpBgpPeerDefaultInAggMed_Object = MibTableColumn
vrIpBgpPeerDefaultInAggMed = _VrIpBgpPeerDefaultInAggMed_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 2, 10, 1, 8),
    _VrIpBgpPeerDefaultInAggMed_Type()
)
vrIpBgpPeerDefaultInAggMed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpBgpPeerDefaultInAggMed.setStatus("mandatory")


class _VrIpBgpPeerIsRouteReflectorClient_Type(Integer32):
    """Custom type vrIpBgpPeerIsRouteReflectorClient based on Integer32"""
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


_VrIpBgpPeerIsRouteReflectorClient_Type.__name__ = "Integer32"
_VrIpBgpPeerIsRouteReflectorClient_Object = MibTableColumn
vrIpBgpPeerIsRouteReflectorClient = _VrIpBgpPeerIsRouteReflectorClient_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 2, 10, 1, 9),
    _VrIpBgpPeerIsRouteReflectorClient_Type()
)
vrIpBgpPeerIsRouteReflectorClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpBgpPeerIsRouteReflectorClient.setStatus("mandatory")
_VrIpBgpPeerStateTable_Object = MibTable
vrIpBgpPeerStateTable = _VrIpBgpPeerStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 2, 11)
)
if mibBuilder.loadTexts:
    vrIpBgpPeerStateTable.setStatus("mandatory")
_VrIpBgpPeerStateEntry_Object = MibTableRow
vrIpBgpPeerStateEntry = _VrIpBgpPeerStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 2, 11, 1)
)
vrIpBgpPeerStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpPeerPeerAddressIndex"),
)
if mibBuilder.loadTexts:
    vrIpBgpPeerStateEntry.setStatus("mandatory")


class _VrIpBgpPeerAdminState_Type(Integer32):
    """Custom type vrIpBgpPeerAdminState based on Integer32"""
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


_VrIpBgpPeerAdminState_Type.__name__ = "Integer32"
_VrIpBgpPeerAdminState_Object = MibTableColumn
vrIpBgpPeerAdminState = _VrIpBgpPeerAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 2, 11, 1, 1),
    _VrIpBgpPeerAdminState_Type()
)
vrIpBgpPeerAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpPeerAdminState.setStatus("mandatory")


class _VrIpBgpPeerOperationalState_Type(Integer32):
    """Custom type vrIpBgpPeerOperationalState based on Integer32"""
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


_VrIpBgpPeerOperationalState_Type.__name__ = "Integer32"
_VrIpBgpPeerOperationalState_Object = MibTableColumn
vrIpBgpPeerOperationalState = _VrIpBgpPeerOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 2, 11, 1, 2),
    _VrIpBgpPeerOperationalState_Type()
)
vrIpBgpPeerOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpPeerOperationalState.setStatus("mandatory")


class _VrIpBgpPeerUsageState_Type(Integer32):
    """Custom type vrIpBgpPeerUsageState based on Integer32"""
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


_VrIpBgpPeerUsageState_Type.__name__ = "Integer32"
_VrIpBgpPeerUsageState_Object = MibTableColumn
vrIpBgpPeerUsageState = _VrIpBgpPeerUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 2, 11, 1, 3),
    _VrIpBgpPeerUsageState_Type()
)
vrIpBgpPeerUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpPeerUsageState.setStatus("mandatory")
_VrIpBgpPeerOperTable_Object = MibTable
vrIpBgpPeerOperTable = _VrIpBgpPeerOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 2, 12)
)
if mibBuilder.loadTexts:
    vrIpBgpPeerOperTable.setStatus("mandatory")
_VrIpBgpPeerOperEntry_Object = MibTableRow
vrIpBgpPeerOperEntry = _VrIpBgpPeerOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 2, 12, 1)
)
vrIpBgpPeerOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpPeerPeerAddressIndex"),
)
if mibBuilder.loadTexts:
    vrIpBgpPeerOperEntry.setStatus("mandatory")


class _VrIpBgpPeerConnectionState_Type(Integer32):
    """Custom type vrIpBgpPeerConnectionState based on Integer32"""
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


_VrIpBgpPeerConnectionState_Type.__name__ = "Integer32"
_VrIpBgpPeerConnectionState_Object = MibTableColumn
vrIpBgpPeerConnectionState = _VrIpBgpPeerConnectionState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 2, 12, 1, 3),
    _VrIpBgpPeerConnectionState_Type()
)
vrIpBgpPeerConnectionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpPeerConnectionState.setStatus("mandatory")
_VrIpBgpPeerBgpIdentifier_Type = IpAddress
_VrIpBgpPeerBgpIdentifier_Object = MibTableColumn
vrIpBgpPeerBgpIdentifier = _VrIpBgpPeerBgpIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 2, 12, 1, 4),
    _VrIpBgpPeerBgpIdentifier_Type()
)
vrIpBgpPeerBgpIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpPeerBgpIdentifier.setStatus("mandatory")


class _VrIpBgpPeerVersionNegotiated_Type(Unsigned32):
    """Custom type vrIpBgpPeerVersionNegotiated based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_VrIpBgpPeerVersionNegotiated_Type.__name__ = "Unsigned32"
_VrIpBgpPeerVersionNegotiated_Object = MibTableColumn
vrIpBgpPeerVersionNegotiated = _VrIpBgpPeerVersionNegotiated_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 2, 12, 1, 5),
    _VrIpBgpPeerVersionNegotiated_Type()
)
vrIpBgpPeerVersionNegotiated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpPeerVersionNegotiated.setStatus("mandatory")


class _VrIpBgpPeerHoldTimeNegotiated_Type(Unsigned32):
    """Custom type vrIpBgpPeerHoldTimeNegotiated based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 65535),
    )


_VrIpBgpPeerHoldTimeNegotiated_Type.__name__ = "Unsigned32"
_VrIpBgpPeerHoldTimeNegotiated_Object = MibTableColumn
vrIpBgpPeerHoldTimeNegotiated = _VrIpBgpPeerHoldTimeNegotiated_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 2, 12, 1, 6),
    _VrIpBgpPeerHoldTimeNegotiated_Type()
)
vrIpBgpPeerHoldTimeNegotiated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpPeerHoldTimeNegotiated.setStatus("mandatory")


class _VrIpBgpPeerKeepAliveNegotiated_Type(Unsigned32):
    """Custom type vrIpBgpPeerKeepAliveNegotiated based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 21845),
    )


_VrIpBgpPeerKeepAliveNegotiated_Type.__name__ = "Unsigned32"
_VrIpBgpPeerKeepAliveNegotiated_Object = MibTableColumn
vrIpBgpPeerKeepAliveNegotiated = _VrIpBgpPeerKeepAliveNegotiated_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 2, 12, 1, 7),
    _VrIpBgpPeerKeepAliveNegotiated_Type()
)
vrIpBgpPeerKeepAliveNegotiated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpPeerKeepAliveNegotiated.setStatus("mandatory")
_VrIpBgpPeerLocalAddressUsed_Type = IpAddress
_VrIpBgpPeerLocalAddressUsed_Object = MibTableColumn
vrIpBgpPeerLocalAddressUsed = _VrIpBgpPeerLocalAddressUsed_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 2, 12, 1, 8),
    _VrIpBgpPeerLocalAddressUsed_Type()
)
vrIpBgpPeerLocalAddressUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpPeerLocalAddressUsed.setStatus("mandatory")


class _VrIpBgpPeerLocalPort_Type(Unsigned32):
    """Custom type vrIpBgpPeerLocalPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VrIpBgpPeerLocalPort_Type.__name__ = "Unsigned32"
_VrIpBgpPeerLocalPort_Object = MibTableColumn
vrIpBgpPeerLocalPort = _VrIpBgpPeerLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 2, 12, 1, 9),
    _VrIpBgpPeerLocalPort_Type()
)
vrIpBgpPeerLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpPeerLocalPort.setStatus("mandatory")


class _VrIpBgpPeerRemotePort_Type(Unsigned32):
    """Custom type vrIpBgpPeerRemotePort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VrIpBgpPeerRemotePort_Type.__name__ = "Unsigned32"
_VrIpBgpPeerRemotePort_Object = MibTableColumn
vrIpBgpPeerRemotePort = _VrIpBgpPeerRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 2, 12, 1, 10),
    _VrIpBgpPeerRemotePort_Type()
)
vrIpBgpPeerRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpPeerRemotePort.setStatus("mandatory")


class _VrIpBgpPeerLastError_Type(HexString):
    """Custom type vrIpBgpPeerLastError based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_VrIpBgpPeerLastError_Type.__name__ = "HexString"
_VrIpBgpPeerLastError_Object = MibTableColumn
vrIpBgpPeerLastError = _VrIpBgpPeerLastError_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 2, 12, 1, 11),
    _VrIpBgpPeerLastError_Type()
)
vrIpBgpPeerLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpPeerLastError.setStatus("mandatory")


class _VrIpBgpPeerConnectionEstablishedTime_Type(Gauge32):
    """Custom type vrIpBgpPeerConnectionEstablishedTime based on Gauge32"""
    defaultValue = 0

    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrIpBgpPeerConnectionEstablishedTime_Type.__name__ = "Gauge32"
_VrIpBgpPeerConnectionEstablishedTime_Object = MibTableColumn
vrIpBgpPeerConnectionEstablishedTime = _VrIpBgpPeerConnectionEstablishedTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 2, 12, 1, 12),
    _VrIpBgpPeerConnectionEstablishedTime_Type()
)
vrIpBgpPeerConnectionEstablishedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpPeerConnectionEstablishedTime.setStatus("mandatory")
_VrIpBgpPeerConnectionEstablishedTransitions_Type = Counter32
_VrIpBgpPeerConnectionEstablishedTransitions_Object = MibTableColumn
vrIpBgpPeerConnectionEstablishedTransitions = _VrIpBgpPeerConnectionEstablishedTransitions_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 2, 12, 1, 13),
    _VrIpBgpPeerConnectionEstablishedTransitions_Type()
)
vrIpBgpPeerConnectionEstablishedTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpPeerConnectionEstablishedTransitions.setStatus("mandatory")


class _VrIpBgpPeerInUpdateElapsedTime_Type(Gauge32):
    """Custom type vrIpBgpPeerInUpdateElapsedTime based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrIpBgpPeerInUpdateElapsedTime_Type.__name__ = "Gauge32"
_VrIpBgpPeerInUpdateElapsedTime_Object = MibTableColumn
vrIpBgpPeerInUpdateElapsedTime = _VrIpBgpPeerInUpdateElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 2, 12, 1, 14),
    _VrIpBgpPeerInUpdateElapsedTime_Type()
)
vrIpBgpPeerInUpdateElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpPeerInUpdateElapsedTime.setStatus("mandatory")
_VrIpBgpPeerInMsgs_Type = Counter32
_VrIpBgpPeerInMsgs_Object = MibTableColumn
vrIpBgpPeerInMsgs = _VrIpBgpPeerInMsgs_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 2, 12, 1, 15),
    _VrIpBgpPeerInMsgs_Type()
)
vrIpBgpPeerInMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpPeerInMsgs.setStatus("mandatory")
_VrIpBgpPeerInUpdates_Type = Counter32
_VrIpBgpPeerInUpdates_Object = MibTableColumn
vrIpBgpPeerInUpdates = _VrIpBgpPeerInUpdates_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 2, 12, 1, 16),
    _VrIpBgpPeerInUpdates_Type()
)
vrIpBgpPeerInUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpPeerInUpdates.setStatus("mandatory")
_VrIpBgpPeerInErrors_Type = Counter32
_VrIpBgpPeerInErrors_Object = MibTableColumn
vrIpBgpPeerInErrors = _VrIpBgpPeerInErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 2, 12, 1, 17),
    _VrIpBgpPeerInErrors_Type()
)
vrIpBgpPeerInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpPeerInErrors.setStatus("mandatory")
_VrIpBgpPeerInErrorMsgs_Type = Counter32
_VrIpBgpPeerInErrorMsgs_Object = MibTableColumn
vrIpBgpPeerInErrorMsgs = _VrIpBgpPeerInErrorMsgs_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 2, 12, 1, 18),
    _VrIpBgpPeerInErrorMsgs_Type()
)
vrIpBgpPeerInErrorMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpPeerInErrorMsgs.setStatus("mandatory")
_VrIpBgpPeerOutMsgs_Type = Counter32
_VrIpBgpPeerOutMsgs_Object = MibTableColumn
vrIpBgpPeerOutMsgs = _VrIpBgpPeerOutMsgs_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 2, 12, 1, 19),
    _VrIpBgpPeerOutMsgs_Type()
)
vrIpBgpPeerOutMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpPeerOutMsgs.setStatus("mandatory")
_VrIpBgpPeerOutUpdates_Type = Counter32
_VrIpBgpPeerOutUpdates_Object = MibTableColumn
vrIpBgpPeerOutUpdates = _VrIpBgpPeerOutUpdates_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 2, 12, 1, 20),
    _VrIpBgpPeerOutUpdates_Type()
)
vrIpBgpPeerOutUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpPeerOutUpdates.setStatus("mandatory")
_VrIpBgpPeerOutDiscards_Type = Counter32
_VrIpBgpPeerOutDiscards_Object = MibTableColumn
vrIpBgpPeerOutDiscards = _VrIpBgpPeerOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 2, 12, 1, 21),
    _VrIpBgpPeerOutDiscards_Type()
)
vrIpBgpPeerOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpPeerOutDiscards.setStatus("mandatory")
_VrIpBgpPeerOutErrorMsgs_Type = Counter32
_VrIpBgpPeerOutErrorMsgs_Object = MibTableColumn
vrIpBgpPeerOutErrorMsgs = _VrIpBgpPeerOutErrorMsgs_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 2, 12, 1, 22),
    _VrIpBgpPeerOutErrorMsgs_Type()
)
vrIpBgpPeerOutErrorMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpPeerOutErrorMsgs.setStatus("mandatory")
_VrIpBgpPeerInRoutes_Type = Counter32
_VrIpBgpPeerInRoutes_Object = MibTableColumn
vrIpBgpPeerInRoutes = _VrIpBgpPeerInRoutes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 2, 12, 1, 23),
    _VrIpBgpPeerInRoutes_Type()
)
vrIpBgpPeerInRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpPeerInRoutes.setStatus("mandatory")
_VrIpBgpImport_ObjectIdentity = ObjectIdentity
vrIpBgpImport = _VrIpBgpImport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 3)
)
_VrIpBgpImportRowStatusTable_Object = MibTable
vrIpBgpImportRowStatusTable = _VrIpBgpImportRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 3, 1)
)
if mibBuilder.loadTexts:
    vrIpBgpImportRowStatusTable.setStatus("mandatory")
_VrIpBgpImportRowStatusEntry_Object = MibTableRow
vrIpBgpImportRowStatusEntry = _VrIpBgpImportRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 3, 1, 1)
)
vrIpBgpImportRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpImportIndex"),
)
if mibBuilder.loadTexts:
    vrIpBgpImportRowStatusEntry.setStatus("mandatory")
_VrIpBgpImportRowStatus_Type = RowStatus
_VrIpBgpImportRowStatus_Object = MibTableColumn
vrIpBgpImportRowStatus = _VrIpBgpImportRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 3, 1, 1, 1),
    _VrIpBgpImportRowStatus_Type()
)
vrIpBgpImportRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpBgpImportRowStatus.setStatus("mandatory")
_VrIpBgpImportComponentName_Type = DisplayString
_VrIpBgpImportComponentName_Object = MibTableColumn
vrIpBgpImportComponentName = _VrIpBgpImportComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 3, 1, 1, 2),
    _VrIpBgpImportComponentName_Type()
)
vrIpBgpImportComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpImportComponentName.setStatus("mandatory")
_VrIpBgpImportStorageType_Type = StorageType
_VrIpBgpImportStorageType_Object = MibTableColumn
vrIpBgpImportStorageType = _VrIpBgpImportStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 3, 1, 1, 4),
    _VrIpBgpImportStorageType_Type()
)
vrIpBgpImportStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpImportStorageType.setStatus("mandatory")


class _VrIpBgpImportIndex_Type(Integer32):
    """Custom type vrIpBgpImportIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VrIpBgpImportIndex_Type.__name__ = "Integer32"
_VrIpBgpImportIndex_Object = MibTableColumn
vrIpBgpImportIndex = _VrIpBgpImportIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 3, 1, 1, 10),
    _VrIpBgpImportIndex_Type()
)
vrIpBgpImportIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpBgpImportIndex.setStatus("mandatory")
_VrIpBgpImportNet_ObjectIdentity = ObjectIdentity
vrIpBgpImportNet = _VrIpBgpImportNet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 3, 2)
)
_VrIpBgpImportNetRowStatusTable_Object = MibTable
vrIpBgpImportNetRowStatusTable = _VrIpBgpImportNetRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 3, 2, 1)
)
if mibBuilder.loadTexts:
    vrIpBgpImportNetRowStatusTable.setStatus("mandatory")
_VrIpBgpImportNetRowStatusEntry_Object = MibTableRow
vrIpBgpImportNetRowStatusEntry = _VrIpBgpImportNetRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 3, 2, 1, 1)
)
vrIpBgpImportNetRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpImportIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpImportNetIndex"),
)
if mibBuilder.loadTexts:
    vrIpBgpImportNetRowStatusEntry.setStatus("mandatory")
_VrIpBgpImportNetRowStatus_Type = RowStatus
_VrIpBgpImportNetRowStatus_Object = MibTableColumn
vrIpBgpImportNetRowStatus = _VrIpBgpImportNetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 3, 2, 1, 1, 1),
    _VrIpBgpImportNetRowStatus_Type()
)
vrIpBgpImportNetRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpBgpImportNetRowStatus.setStatus("mandatory")
_VrIpBgpImportNetComponentName_Type = DisplayString
_VrIpBgpImportNetComponentName_Object = MibTableColumn
vrIpBgpImportNetComponentName = _VrIpBgpImportNetComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 3, 2, 1, 1, 2),
    _VrIpBgpImportNetComponentName_Type()
)
vrIpBgpImportNetComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpImportNetComponentName.setStatus("mandatory")
_VrIpBgpImportNetStorageType_Type = StorageType
_VrIpBgpImportNetStorageType_Object = MibTableColumn
vrIpBgpImportNetStorageType = _VrIpBgpImportNetStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 3, 2, 1, 1, 4),
    _VrIpBgpImportNetStorageType_Type()
)
vrIpBgpImportNetStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpImportNetStorageType.setStatus("mandatory")


class _VrIpBgpImportNetIndex_Type(Integer32):
    """Custom type vrIpBgpImportNetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VrIpBgpImportNetIndex_Type.__name__ = "Integer32"
_VrIpBgpImportNetIndex_Object = MibTableColumn
vrIpBgpImportNetIndex = _VrIpBgpImportNetIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 3, 2, 1, 1, 10),
    _VrIpBgpImportNetIndex_Type()
)
vrIpBgpImportNetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpBgpImportNetIndex.setStatus("mandatory")
_VrIpBgpImportNetProvTable_Object = MibTable
vrIpBgpImportNetProvTable = _VrIpBgpImportNetProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 3, 2, 10)
)
if mibBuilder.loadTexts:
    vrIpBgpImportNetProvTable.setStatus("mandatory")
_VrIpBgpImportNetProvEntry_Object = MibTableRow
vrIpBgpImportNetProvEntry = _VrIpBgpImportNetProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 3, 2, 10, 1)
)
vrIpBgpImportNetProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpImportIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpImportNetIndex"),
)
if mibBuilder.loadTexts:
    vrIpBgpImportNetProvEntry.setStatus("mandatory")
_VrIpBgpImportNetPrefix_Type = IpAddress
_VrIpBgpImportNetPrefix_Object = MibTableColumn
vrIpBgpImportNetPrefix = _VrIpBgpImportNetPrefix_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 3, 2, 10, 1, 1),
    _VrIpBgpImportNetPrefix_Type()
)
vrIpBgpImportNetPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpBgpImportNetPrefix.setStatus("mandatory")


class _VrIpBgpImportNetLength_Type(Unsigned32):
    """Custom type vrIpBgpImportNetLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_VrIpBgpImportNetLength_Type.__name__ = "Unsigned32"
_VrIpBgpImportNetLength_Object = MibTableColumn
vrIpBgpImportNetLength = _VrIpBgpImportNetLength_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 3, 2, 10, 1, 2),
    _VrIpBgpImportNetLength_Type()
)
vrIpBgpImportNetLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpBgpImportNetLength.setStatus("mandatory")
_VrIpBgpImportProvTable_Object = MibTable
vrIpBgpImportProvTable = _VrIpBgpImportProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 3, 10)
)
if mibBuilder.loadTexts:
    vrIpBgpImportProvTable.setStatus("mandatory")
_VrIpBgpImportProvEntry_Object = MibTableRow
vrIpBgpImportProvEntry = _VrIpBgpImportProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 3, 10, 1)
)
vrIpBgpImportProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpImportIndex"),
)
if mibBuilder.loadTexts:
    vrIpBgpImportProvEntry.setStatus("mandatory")


class _VrIpBgpImportPeerAs_Type(Unsigned32):
    """Custom type vrIpBgpImportPeerAs based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VrIpBgpImportPeerAs_Type.__name__ = "Unsigned32"
_VrIpBgpImportPeerAs_Object = MibTableColumn
vrIpBgpImportPeerAs = _VrIpBgpImportPeerAs_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 3, 10, 1, 1),
    _VrIpBgpImportPeerAs_Type()
)
vrIpBgpImportPeerAs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpBgpImportPeerAs.setStatus("mandatory")


class _VrIpBgpImportPeerIpAddress_Type(IpAddress):
    """Custom type vrIpBgpImportPeerIpAddress based on IpAddress"""
    defaultHexValue = "00000000"


_VrIpBgpImportPeerIpAddress_Object = MibTableColumn
vrIpBgpImportPeerIpAddress = _VrIpBgpImportPeerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 3, 10, 1, 2),
    _VrIpBgpImportPeerIpAddress_Type()
)
vrIpBgpImportPeerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpBgpImportPeerIpAddress.setStatus("mandatory")


class _VrIpBgpImportOriginAs_Type(Unsigned32):
    """Custom type vrIpBgpImportOriginAs based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VrIpBgpImportOriginAs_Type.__name__ = "Unsigned32"
_VrIpBgpImportOriginAs_Object = MibTableColumn
vrIpBgpImportOriginAs = _VrIpBgpImportOriginAs_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 3, 10, 1, 3),
    _VrIpBgpImportOriginAs_Type()
)
vrIpBgpImportOriginAs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpBgpImportOriginAs.setStatus("mandatory")


class _VrIpBgpImportOriginProtocol_Type(Integer32):
    """Custom type vrIpBgpImportOriginProtocol based on Integer32"""
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


_VrIpBgpImportOriginProtocol_Type.__name__ = "Integer32"
_VrIpBgpImportOriginProtocol_Object = MibTableColumn
vrIpBgpImportOriginProtocol = _VrIpBgpImportOriginProtocol_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 3, 10, 1, 4),
    _VrIpBgpImportOriginProtocol_Type()
)
vrIpBgpImportOriginProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpBgpImportOriginProtocol.setStatus("mandatory")


class _VrIpBgpImportUsageFlag_Type(Integer32):
    """Custom type vrIpBgpImportUsageFlag based on Integer32"""
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
        *(("exclude", 3),
          ("ignore", 2),
          ("use", 1))
    )


_VrIpBgpImportUsageFlag_Type.__name__ = "Integer32"
_VrIpBgpImportUsageFlag_Object = MibTableColumn
vrIpBgpImportUsageFlag = _VrIpBgpImportUsageFlag_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 3, 10, 1, 5),
    _VrIpBgpImportUsageFlag_Type()
)
vrIpBgpImportUsageFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpBgpImportUsageFlag.setStatus("mandatory")


class _VrIpBgpImportLocalPreference_Type(Unsigned32):
    """Custom type vrIpBgpImportLocalPreference based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrIpBgpImportLocalPreference_Type.__name__ = "Unsigned32"
_VrIpBgpImportLocalPreference_Object = MibTableColumn
vrIpBgpImportLocalPreference = _VrIpBgpImportLocalPreference_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 3, 10, 1, 6),
    _VrIpBgpImportLocalPreference_Type()
)
vrIpBgpImportLocalPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpBgpImportLocalPreference.setStatus("mandatory")


class _VrIpBgpImportPreferredOver_Type(Integer32):
    """Custom type vrIpBgpImportPreferredOver based on Integer32"""
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


_VrIpBgpImportPreferredOver_Type.__name__ = "Integer32"
_VrIpBgpImportPreferredOver_Object = MibTableColumn
vrIpBgpImportPreferredOver = _VrIpBgpImportPreferredOver_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 3, 10, 1, 7),
    _VrIpBgpImportPreferredOver_Type()
)
vrIpBgpImportPreferredOver.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpBgpImportPreferredOver.setStatus("mandatory")


class _VrIpBgpImportAsPathExpression_Type(AsciiString):
    """Custom type vrIpBgpImportAsPathExpression based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VrIpBgpImportAsPathExpression_Type.__name__ = "AsciiString"
_VrIpBgpImportAsPathExpression_Object = MibTableColumn
vrIpBgpImportAsPathExpression = _VrIpBgpImportAsPathExpression_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 3, 10, 1, 8),
    _VrIpBgpImportAsPathExpression_Type()
)
vrIpBgpImportAsPathExpression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpBgpImportAsPathExpression.setStatus("mandatory")


class _VrIpBgpImportCommunityExpression_Type(AsciiString):
    """Custom type vrIpBgpImportCommunityExpression based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VrIpBgpImportCommunityExpression_Type.__name__ = "AsciiString"
_VrIpBgpImportCommunityExpression_Object = MibTableColumn
vrIpBgpImportCommunityExpression = _VrIpBgpImportCommunityExpression_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 3, 10, 1, 9),
    _VrIpBgpImportCommunityExpression_Type()
)
vrIpBgpImportCommunityExpression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpBgpImportCommunityExpression.setStatus("mandatory")


class _VrIpBgpImportExpressPreference_Type(Unsigned32):
    """Custom type vrIpBgpImportExpressPreference based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VrIpBgpImportExpressPreference_Type.__name__ = "Unsigned32"
_VrIpBgpImportExpressPreference_Object = MibTableColumn
vrIpBgpImportExpressPreference = _VrIpBgpImportExpressPreference_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 3, 10, 1, 10),
    _VrIpBgpImportExpressPreference_Type()
)
vrIpBgpImportExpressPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpBgpImportExpressPreference.setStatus("mandatory")


class _VrIpBgpImportAppendCommunity_Type(Unsigned32):
    """Custom type vrIpBgpImportAppendCommunity based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrIpBgpImportAppendCommunity_Type.__name__ = "Unsigned32"
_VrIpBgpImportAppendCommunity_Object = MibTableColumn
vrIpBgpImportAppendCommunity = _VrIpBgpImportAppendCommunity_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 3, 10, 1, 11),
    _VrIpBgpImportAppendCommunity_Type()
)
vrIpBgpImportAppendCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpBgpImportAppendCommunity.setStatus("mandatory")
_VrIpBgpExport_ObjectIdentity = ObjectIdentity
vrIpBgpExport = _VrIpBgpExport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 4)
)
_VrIpBgpExportRowStatusTable_Object = MibTable
vrIpBgpExportRowStatusTable = _VrIpBgpExportRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 4, 1)
)
if mibBuilder.loadTexts:
    vrIpBgpExportRowStatusTable.setStatus("mandatory")
_VrIpBgpExportRowStatusEntry_Object = MibTableRow
vrIpBgpExportRowStatusEntry = _VrIpBgpExportRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 4, 1, 1)
)
vrIpBgpExportRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpExportIndex"),
)
if mibBuilder.loadTexts:
    vrIpBgpExportRowStatusEntry.setStatus("mandatory")
_VrIpBgpExportRowStatus_Type = RowStatus
_VrIpBgpExportRowStatus_Object = MibTableColumn
vrIpBgpExportRowStatus = _VrIpBgpExportRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 4, 1, 1, 1),
    _VrIpBgpExportRowStatus_Type()
)
vrIpBgpExportRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpBgpExportRowStatus.setStatus("mandatory")
_VrIpBgpExportComponentName_Type = DisplayString
_VrIpBgpExportComponentName_Object = MibTableColumn
vrIpBgpExportComponentName = _VrIpBgpExportComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 4, 1, 1, 2),
    _VrIpBgpExportComponentName_Type()
)
vrIpBgpExportComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpExportComponentName.setStatus("mandatory")
_VrIpBgpExportStorageType_Type = StorageType
_VrIpBgpExportStorageType_Object = MibTableColumn
vrIpBgpExportStorageType = _VrIpBgpExportStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 4, 1, 1, 4),
    _VrIpBgpExportStorageType_Type()
)
vrIpBgpExportStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpExportStorageType.setStatus("mandatory")


class _VrIpBgpExportIndex_Type(Integer32):
    """Custom type vrIpBgpExportIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VrIpBgpExportIndex_Type.__name__ = "Integer32"
_VrIpBgpExportIndex_Object = MibTableColumn
vrIpBgpExportIndex = _VrIpBgpExportIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 4, 1, 1, 10),
    _VrIpBgpExportIndex_Type()
)
vrIpBgpExportIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpBgpExportIndex.setStatus("mandatory")
_VrIpBgpExportNet_ObjectIdentity = ObjectIdentity
vrIpBgpExportNet = _VrIpBgpExportNet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 4, 2)
)
_VrIpBgpExportNetRowStatusTable_Object = MibTable
vrIpBgpExportNetRowStatusTable = _VrIpBgpExportNetRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 4, 2, 1)
)
if mibBuilder.loadTexts:
    vrIpBgpExportNetRowStatusTable.setStatus("mandatory")
_VrIpBgpExportNetRowStatusEntry_Object = MibTableRow
vrIpBgpExportNetRowStatusEntry = _VrIpBgpExportNetRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 4, 2, 1, 1)
)
vrIpBgpExportNetRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpExportIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpExportNetIndex"),
)
if mibBuilder.loadTexts:
    vrIpBgpExportNetRowStatusEntry.setStatus("mandatory")
_VrIpBgpExportNetRowStatus_Type = RowStatus
_VrIpBgpExportNetRowStatus_Object = MibTableColumn
vrIpBgpExportNetRowStatus = _VrIpBgpExportNetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 4, 2, 1, 1, 1),
    _VrIpBgpExportNetRowStatus_Type()
)
vrIpBgpExportNetRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpBgpExportNetRowStatus.setStatus("mandatory")
_VrIpBgpExportNetComponentName_Type = DisplayString
_VrIpBgpExportNetComponentName_Object = MibTableColumn
vrIpBgpExportNetComponentName = _VrIpBgpExportNetComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 4, 2, 1, 1, 2),
    _VrIpBgpExportNetComponentName_Type()
)
vrIpBgpExportNetComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpExportNetComponentName.setStatus("mandatory")
_VrIpBgpExportNetStorageType_Type = StorageType
_VrIpBgpExportNetStorageType_Object = MibTableColumn
vrIpBgpExportNetStorageType = _VrIpBgpExportNetStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 4, 2, 1, 1, 4),
    _VrIpBgpExportNetStorageType_Type()
)
vrIpBgpExportNetStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpExportNetStorageType.setStatus("mandatory")


class _VrIpBgpExportNetIndex_Type(Integer32):
    """Custom type vrIpBgpExportNetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VrIpBgpExportNetIndex_Type.__name__ = "Integer32"
_VrIpBgpExportNetIndex_Object = MibTableColumn
vrIpBgpExportNetIndex = _VrIpBgpExportNetIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 4, 2, 1, 1, 10),
    _VrIpBgpExportNetIndex_Type()
)
vrIpBgpExportNetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpBgpExportNetIndex.setStatus("mandatory")
_VrIpBgpExportNetProvTable_Object = MibTable
vrIpBgpExportNetProvTable = _VrIpBgpExportNetProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 4, 2, 10)
)
if mibBuilder.loadTexts:
    vrIpBgpExportNetProvTable.setStatus("mandatory")
_VrIpBgpExportNetProvEntry_Object = MibTableRow
vrIpBgpExportNetProvEntry = _VrIpBgpExportNetProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 4, 2, 10, 1)
)
vrIpBgpExportNetProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpExportIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpExportNetIndex"),
)
if mibBuilder.loadTexts:
    vrIpBgpExportNetProvEntry.setStatus("mandatory")
_VrIpBgpExportNetPrefix_Type = IpAddress
_VrIpBgpExportNetPrefix_Object = MibTableColumn
vrIpBgpExportNetPrefix = _VrIpBgpExportNetPrefix_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 4, 2, 10, 1, 1),
    _VrIpBgpExportNetPrefix_Type()
)
vrIpBgpExportNetPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpBgpExportNetPrefix.setStatus("mandatory")


class _VrIpBgpExportNetLength_Type(Unsigned32):
    """Custom type vrIpBgpExportNetLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_VrIpBgpExportNetLength_Type.__name__ = "Unsigned32"
_VrIpBgpExportNetLength_Object = MibTableColumn
vrIpBgpExportNetLength = _VrIpBgpExportNetLength_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 4, 2, 10, 1, 2),
    _VrIpBgpExportNetLength_Type()
)
vrIpBgpExportNetLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpBgpExportNetLength.setStatus("mandatory")
_VrIpBgpExportProvTable_Object = MibTable
vrIpBgpExportProvTable = _VrIpBgpExportProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 4, 10)
)
if mibBuilder.loadTexts:
    vrIpBgpExportProvTable.setStatus("mandatory")
_VrIpBgpExportProvEntry_Object = MibTableRow
vrIpBgpExportProvEntry = _VrIpBgpExportProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 4, 10, 1)
)
vrIpBgpExportProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpExportIndex"),
)
if mibBuilder.loadTexts:
    vrIpBgpExportProvEntry.setStatus("mandatory")


class _VrIpBgpExportPeerAs_Type(Unsigned32):
    """Custom type vrIpBgpExportPeerAs based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VrIpBgpExportPeerAs_Type.__name__ = "Unsigned32"
_VrIpBgpExportPeerAs_Object = MibTableColumn
vrIpBgpExportPeerAs = _VrIpBgpExportPeerAs_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 4, 10, 1, 1),
    _VrIpBgpExportPeerAs_Type()
)
vrIpBgpExportPeerAs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpBgpExportPeerAs.setStatus("mandatory")


class _VrIpBgpExportPeerIpAddress_Type(IpAddress):
    """Custom type vrIpBgpExportPeerIpAddress based on IpAddress"""
    defaultHexValue = "00000000"


_VrIpBgpExportPeerIpAddress_Object = MibTableColumn
vrIpBgpExportPeerIpAddress = _VrIpBgpExportPeerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 4, 10, 1, 2),
    _VrIpBgpExportPeerIpAddress_Type()
)
vrIpBgpExportPeerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpBgpExportPeerIpAddress.setStatus("mandatory")


class _VrIpBgpExportProtocol_Type(Integer32):
    """Custom type vrIpBgpExportProtocol based on Integer32"""
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


_VrIpBgpExportProtocol_Type.__name__ = "Integer32"
_VrIpBgpExportProtocol_Object = MibTableColumn
vrIpBgpExportProtocol = _VrIpBgpExportProtocol_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 4, 10, 1, 3),
    _VrIpBgpExportProtocol_Type()
)
vrIpBgpExportProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpBgpExportProtocol.setStatus("mandatory")


class _VrIpBgpExportEgpAsId_Type(Unsigned32):
    """Custom type vrIpBgpExportEgpAsId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VrIpBgpExportEgpAsId_Type.__name__ = "Unsigned32"
_VrIpBgpExportEgpAsId_Object = MibTableColumn
vrIpBgpExportEgpAsId = _VrIpBgpExportEgpAsId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 4, 10, 1, 4),
    _VrIpBgpExportEgpAsId_Type()
)
vrIpBgpExportEgpAsId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpBgpExportEgpAsId.setStatus("mandatory")


class _VrIpBgpExportBgpAsId_Type(Unsigned32):
    """Custom type vrIpBgpExportBgpAsId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VrIpBgpExportBgpAsId_Type.__name__ = "Unsigned32"
_VrIpBgpExportBgpAsId_Object = MibTableColumn
vrIpBgpExportBgpAsId = _VrIpBgpExportBgpAsId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 4, 10, 1, 5),
    _VrIpBgpExportBgpAsId_Type()
)
vrIpBgpExportBgpAsId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpBgpExportBgpAsId.setStatus("mandatory")


class _VrIpBgpExportOspfTag_Type(Hex):
    """Custom type vrIpBgpExportOspfTag based on Hex"""
    defaultValue = 4294967295

    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrIpBgpExportOspfTag_Type.__name__ = "Hex"
_VrIpBgpExportOspfTag_Object = MibTableColumn
vrIpBgpExportOspfTag = _VrIpBgpExportOspfTag_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 4, 10, 1, 6),
    _VrIpBgpExportOspfTag_Type()
)
vrIpBgpExportOspfTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpBgpExportOspfTag.setStatus("mandatory")


class _VrIpBgpExportRipInterface_Type(IpAddress):
    """Custom type vrIpBgpExportRipInterface based on IpAddress"""
    defaultHexValue = "00000000"


_VrIpBgpExportRipInterface_Object = MibTableColumn
vrIpBgpExportRipInterface = _VrIpBgpExportRipInterface_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 4, 10, 1, 7),
    _VrIpBgpExportRipInterface_Type()
)
vrIpBgpExportRipInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpBgpExportRipInterface.setStatus("mandatory")


class _VrIpBgpExportRipNeighbor_Type(IpAddress):
    """Custom type vrIpBgpExportRipNeighbor based on IpAddress"""
    defaultHexValue = "00000000"


_VrIpBgpExportRipNeighbor_Object = MibTableColumn
vrIpBgpExportRipNeighbor = _VrIpBgpExportRipNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 4, 10, 1, 8),
    _VrIpBgpExportRipNeighbor_Type()
)
vrIpBgpExportRipNeighbor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpBgpExportRipNeighbor.setStatus("mandatory")


class _VrIpBgpExportAdvertiseStatus_Type(Integer32):
    """Custom type vrIpBgpExportAdvertiseStatus based on Integer32"""
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


_VrIpBgpExportAdvertiseStatus_Type.__name__ = "Integer32"
_VrIpBgpExportAdvertiseStatus_Object = MibTableColumn
vrIpBgpExportAdvertiseStatus = _VrIpBgpExportAdvertiseStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 4, 10, 1, 9),
    _VrIpBgpExportAdvertiseStatus_Type()
)
vrIpBgpExportAdvertiseStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpBgpExportAdvertiseStatus.setStatus("mandatory")


class _VrIpBgpExportMultiExitDisc_Type(Unsigned32):
    """Custom type vrIpBgpExportMultiExitDisc based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrIpBgpExportMultiExitDisc_Type.__name__ = "Unsigned32"
_VrIpBgpExportMultiExitDisc_Object = MibTableColumn
vrIpBgpExportMultiExitDisc = _VrIpBgpExportMultiExitDisc_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 4, 10, 1, 10),
    _VrIpBgpExportMultiExitDisc_Type()
)
vrIpBgpExportMultiExitDisc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpBgpExportMultiExitDisc.setStatus("mandatory")


class _VrIpBgpExportSendMultiExitDiscToEbgp_Type(Integer32):
    """Custom type vrIpBgpExportSendMultiExitDiscToEbgp based on Integer32"""
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


_VrIpBgpExportSendMultiExitDiscToEbgp_Type.__name__ = "Integer32"
_VrIpBgpExportSendMultiExitDiscToEbgp_Object = MibTableColumn
vrIpBgpExportSendMultiExitDiscToEbgp = _VrIpBgpExportSendMultiExitDiscToEbgp_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 4, 10, 1, 11),
    _VrIpBgpExportSendMultiExitDiscToEbgp_Type()
)
vrIpBgpExportSendMultiExitDiscToEbgp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpBgpExportSendMultiExitDiscToEbgp.setStatus("mandatory")


class _VrIpBgpExportAsPathExpression_Type(AsciiString):
    """Custom type vrIpBgpExportAsPathExpression based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VrIpBgpExportAsPathExpression_Type.__name__ = "AsciiString"
_VrIpBgpExportAsPathExpression_Object = MibTableColumn
vrIpBgpExportAsPathExpression = _VrIpBgpExportAsPathExpression_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 4, 10, 1, 12),
    _VrIpBgpExportAsPathExpression_Type()
)
vrIpBgpExportAsPathExpression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpBgpExportAsPathExpression.setStatus("mandatory")


class _VrIpBgpExportCommunityExpression_Type(AsciiString):
    """Custom type vrIpBgpExportCommunityExpression based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VrIpBgpExportCommunityExpression_Type.__name__ = "AsciiString"
_VrIpBgpExportCommunityExpression_Object = MibTableColumn
vrIpBgpExportCommunityExpression = _VrIpBgpExportCommunityExpression_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 4, 10, 1, 13),
    _VrIpBgpExportCommunityExpression_Type()
)
vrIpBgpExportCommunityExpression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpBgpExportCommunityExpression.setStatus("mandatory")


class _VrIpBgpExportExpressPreference_Type(Unsigned32):
    """Custom type vrIpBgpExportExpressPreference based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VrIpBgpExportExpressPreference_Type.__name__ = "Unsigned32"
_VrIpBgpExportExpressPreference_Object = MibTableColumn
vrIpBgpExportExpressPreference = _VrIpBgpExportExpressPreference_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 4, 10, 1, 14),
    _VrIpBgpExportExpressPreference_Type()
)
vrIpBgpExportExpressPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpBgpExportExpressPreference.setStatus("mandatory")


class _VrIpBgpExportSendCommunity_Type(Unsigned32):
    """Custom type vrIpBgpExportSendCommunity based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrIpBgpExportSendCommunity_Type.__name__ = "Unsigned32"
_VrIpBgpExportSendCommunity_Object = MibTableColumn
vrIpBgpExportSendCommunity = _VrIpBgpExportSendCommunity_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 4, 10, 1, 15),
    _VrIpBgpExportSendCommunity_Type()
)
vrIpBgpExportSendCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpBgpExportSendCommunity.setStatus("mandatory")
_VrIpBgpExportInsertDummyAs_Type = IntegerSequence
_VrIpBgpExportInsertDummyAs_Object = MibTableColumn
vrIpBgpExportInsertDummyAs = _VrIpBgpExportInsertDummyAs_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 4, 10, 1, 200),
    _VrIpBgpExportInsertDummyAs_Type()
)
vrIpBgpExportInsertDummyAs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpBgpExportInsertDummyAs.setStatus("mandatory")
_VrIpBgpAs_ObjectIdentity = ObjectIdentity
vrIpBgpAs = _VrIpBgpAs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 5)
)
_VrIpBgpAsRowStatusTable_Object = MibTable
vrIpBgpAsRowStatusTable = _VrIpBgpAsRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 5, 1)
)
if mibBuilder.loadTexts:
    vrIpBgpAsRowStatusTable.setStatus("mandatory")
_VrIpBgpAsRowStatusEntry_Object = MibTableRow
vrIpBgpAsRowStatusEntry = _VrIpBgpAsRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 5, 1, 1)
)
vrIpBgpAsRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpAsIndex"),
)
if mibBuilder.loadTexts:
    vrIpBgpAsRowStatusEntry.setStatus("mandatory")
_VrIpBgpAsRowStatus_Type = RowStatus
_VrIpBgpAsRowStatus_Object = MibTableColumn
vrIpBgpAsRowStatus = _VrIpBgpAsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 5, 1, 1, 1),
    _VrIpBgpAsRowStatus_Type()
)
vrIpBgpAsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpBgpAsRowStatus.setStatus("mandatory")
_VrIpBgpAsComponentName_Type = DisplayString
_VrIpBgpAsComponentName_Object = MibTableColumn
vrIpBgpAsComponentName = _VrIpBgpAsComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 5, 1, 1, 2),
    _VrIpBgpAsComponentName_Type()
)
vrIpBgpAsComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpAsComponentName.setStatus("mandatory")
_VrIpBgpAsStorageType_Type = StorageType
_VrIpBgpAsStorageType_Object = MibTableColumn
vrIpBgpAsStorageType = _VrIpBgpAsStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 5, 1, 1, 4),
    _VrIpBgpAsStorageType_Type()
)
vrIpBgpAsStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpAsStorageType.setStatus("mandatory")


class _VrIpBgpAsIndex_Type(Integer32):
    """Custom type vrIpBgpAsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VrIpBgpAsIndex_Type.__name__ = "Integer32"
_VrIpBgpAsIndex_Object = MibTableColumn
vrIpBgpAsIndex = _VrIpBgpAsIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 5, 1, 1, 10),
    _VrIpBgpAsIndex_Type()
)
vrIpBgpAsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpBgpAsIndex.setStatus("mandatory")
_VrIpBgpAsProvTable_Object = MibTable
vrIpBgpAsProvTable = _VrIpBgpAsProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 5, 10)
)
if mibBuilder.loadTexts:
    vrIpBgpAsProvTable.setStatus("mandatory")
_VrIpBgpAsProvEntry_Object = MibTableRow
vrIpBgpAsProvEntry = _VrIpBgpAsProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 5, 10, 1)
)
vrIpBgpAsProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpAsIndex"),
)
if mibBuilder.loadTexts:
    vrIpBgpAsProvEntry.setStatus("mandatory")


class _VrIpBgpAsWeight_Type(Unsigned32):
    """Custom type vrIpBgpAsWeight based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VrIpBgpAsWeight_Type.__name__ = "Unsigned32"
_VrIpBgpAsWeight_Object = MibTableColumn
vrIpBgpAsWeight = _VrIpBgpAsWeight_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 5, 10, 1, 1),
    _VrIpBgpAsWeight_Type()
)
vrIpBgpAsWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpBgpAsWeight.setStatus("mandatory")
_VrIpBgpAggregate_ObjectIdentity = ObjectIdentity
vrIpBgpAggregate = _VrIpBgpAggregate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 6)
)
_VrIpBgpAggregateRowStatusTable_Object = MibTable
vrIpBgpAggregateRowStatusTable = _VrIpBgpAggregateRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 6, 1)
)
if mibBuilder.loadTexts:
    vrIpBgpAggregateRowStatusTable.setStatus("mandatory")
_VrIpBgpAggregateRowStatusEntry_Object = MibTableRow
vrIpBgpAggregateRowStatusEntry = _VrIpBgpAggregateRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 6, 1, 1)
)
vrIpBgpAggregateRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpAggregatePrefixIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpAggregateLengthIndex"),
)
if mibBuilder.loadTexts:
    vrIpBgpAggregateRowStatusEntry.setStatus("mandatory")
_VrIpBgpAggregateRowStatus_Type = RowStatus
_VrIpBgpAggregateRowStatus_Object = MibTableColumn
vrIpBgpAggregateRowStatus = _VrIpBgpAggregateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 6, 1, 1, 1),
    _VrIpBgpAggregateRowStatus_Type()
)
vrIpBgpAggregateRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpBgpAggregateRowStatus.setStatus("mandatory")
_VrIpBgpAggregateComponentName_Type = DisplayString
_VrIpBgpAggregateComponentName_Object = MibTableColumn
vrIpBgpAggregateComponentName = _VrIpBgpAggregateComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 6, 1, 1, 2),
    _VrIpBgpAggregateComponentName_Type()
)
vrIpBgpAggregateComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpAggregateComponentName.setStatus("mandatory")
_VrIpBgpAggregateStorageType_Type = StorageType
_VrIpBgpAggregateStorageType_Object = MibTableColumn
vrIpBgpAggregateStorageType = _VrIpBgpAggregateStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 6, 1, 1, 4),
    _VrIpBgpAggregateStorageType_Type()
)
vrIpBgpAggregateStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpAggregateStorageType.setStatus("mandatory")
_VrIpBgpAggregatePrefixIndex_Type = IpAddress
_VrIpBgpAggregatePrefixIndex_Object = MibTableColumn
vrIpBgpAggregatePrefixIndex = _VrIpBgpAggregatePrefixIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 6, 1, 1, 10),
    _VrIpBgpAggregatePrefixIndex_Type()
)
vrIpBgpAggregatePrefixIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpBgpAggregatePrefixIndex.setStatus("mandatory")


class _VrIpBgpAggregateLengthIndex_Type(Integer32):
    """Custom type vrIpBgpAggregateLengthIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_VrIpBgpAggregateLengthIndex_Type.__name__ = "Integer32"
_VrIpBgpAggregateLengthIndex_Object = MibTableColumn
vrIpBgpAggregateLengthIndex = _VrIpBgpAggregateLengthIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 6, 1, 1, 11),
    _VrIpBgpAggregateLengthIndex_Type()
)
vrIpBgpAggregateLengthIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpBgpAggregateLengthIndex.setStatus("mandatory")
_VrIpBgpAggregateNet_ObjectIdentity = ObjectIdentity
vrIpBgpAggregateNet = _VrIpBgpAggregateNet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 6, 2)
)
_VrIpBgpAggregateNetRowStatusTable_Object = MibTable
vrIpBgpAggregateNetRowStatusTable = _VrIpBgpAggregateNetRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 6, 2, 1)
)
if mibBuilder.loadTexts:
    vrIpBgpAggregateNetRowStatusTable.setStatus("mandatory")
_VrIpBgpAggregateNetRowStatusEntry_Object = MibTableRow
vrIpBgpAggregateNetRowStatusEntry = _VrIpBgpAggregateNetRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 6, 2, 1, 1)
)
vrIpBgpAggregateNetRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpAggregatePrefixIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpAggregateLengthIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpAggregateNetIndex"),
)
if mibBuilder.loadTexts:
    vrIpBgpAggregateNetRowStatusEntry.setStatus("mandatory")
_VrIpBgpAggregateNetRowStatus_Type = RowStatus
_VrIpBgpAggregateNetRowStatus_Object = MibTableColumn
vrIpBgpAggregateNetRowStatus = _VrIpBgpAggregateNetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 6, 2, 1, 1, 1),
    _VrIpBgpAggregateNetRowStatus_Type()
)
vrIpBgpAggregateNetRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpBgpAggregateNetRowStatus.setStatus("mandatory")
_VrIpBgpAggregateNetComponentName_Type = DisplayString
_VrIpBgpAggregateNetComponentName_Object = MibTableColumn
vrIpBgpAggregateNetComponentName = _VrIpBgpAggregateNetComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 6, 2, 1, 1, 2),
    _VrIpBgpAggregateNetComponentName_Type()
)
vrIpBgpAggregateNetComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpAggregateNetComponentName.setStatus("mandatory")
_VrIpBgpAggregateNetStorageType_Type = StorageType
_VrIpBgpAggregateNetStorageType_Object = MibTableColumn
vrIpBgpAggregateNetStorageType = _VrIpBgpAggregateNetStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 6, 2, 1, 1, 4),
    _VrIpBgpAggregateNetStorageType_Type()
)
vrIpBgpAggregateNetStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpAggregateNetStorageType.setStatus("mandatory")


class _VrIpBgpAggregateNetIndex_Type(Integer32):
    """Custom type vrIpBgpAggregateNetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VrIpBgpAggregateNetIndex_Type.__name__ = "Integer32"
_VrIpBgpAggregateNetIndex_Object = MibTableColumn
vrIpBgpAggregateNetIndex = _VrIpBgpAggregateNetIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 6, 2, 1, 1, 10),
    _VrIpBgpAggregateNetIndex_Type()
)
vrIpBgpAggregateNetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpBgpAggregateNetIndex.setStatus("mandatory")
_VrIpBgpAggregateNetProvTable_Object = MibTable
vrIpBgpAggregateNetProvTable = _VrIpBgpAggregateNetProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 6, 2, 10)
)
if mibBuilder.loadTexts:
    vrIpBgpAggregateNetProvTable.setStatus("mandatory")
_VrIpBgpAggregateNetProvEntry_Object = MibTableRow
vrIpBgpAggregateNetProvEntry = _VrIpBgpAggregateNetProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 6, 2, 10, 1)
)
vrIpBgpAggregateNetProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpAggregatePrefixIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpAggregateLengthIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpAggregateNetIndex"),
)
if mibBuilder.loadTexts:
    vrIpBgpAggregateNetProvEntry.setStatus("mandatory")


class _VrIpBgpAggregateNetPrefix_Type(IpAddress):
    """Custom type vrIpBgpAggregateNetPrefix based on IpAddress"""
    defaultHexValue = "00000000"


_VrIpBgpAggregateNetPrefix_Object = MibTableColumn
vrIpBgpAggregateNetPrefix = _VrIpBgpAggregateNetPrefix_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 6, 2, 10, 1, 1),
    _VrIpBgpAggregateNetPrefix_Type()
)
vrIpBgpAggregateNetPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpBgpAggregateNetPrefix.setStatus("mandatory")


class _VrIpBgpAggregateNetLength_Type(Unsigned32):
    """Custom type vrIpBgpAggregateNetLength based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_VrIpBgpAggregateNetLength_Type.__name__ = "Unsigned32"
_VrIpBgpAggregateNetLength_Object = MibTableColumn
vrIpBgpAggregateNetLength = _VrIpBgpAggregateNetLength_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 6, 2, 10, 1, 2),
    _VrIpBgpAggregateNetLength_Type()
)
vrIpBgpAggregateNetLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpBgpAggregateNetLength.setStatus("mandatory")


class _VrIpBgpAggregateNetProtocol_Type(Integer32):
    """Custom type vrIpBgpAggregateNetProtocol based on Integer32"""
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


_VrIpBgpAggregateNetProtocol_Type.__name__ = "Integer32"
_VrIpBgpAggregateNetProtocol_Object = MibTableColumn
vrIpBgpAggregateNetProtocol = _VrIpBgpAggregateNetProtocol_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 6, 2, 10, 1, 3),
    _VrIpBgpAggregateNetProtocol_Type()
)
vrIpBgpAggregateNetProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpBgpAggregateNetProtocol.setStatus("mandatory")


class _VrIpBgpAggregateNetEgpAsId_Type(Unsigned32):
    """Custom type vrIpBgpAggregateNetEgpAsId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VrIpBgpAggregateNetEgpAsId_Type.__name__ = "Unsigned32"
_VrIpBgpAggregateNetEgpAsId_Object = MibTableColumn
vrIpBgpAggregateNetEgpAsId = _VrIpBgpAggregateNetEgpAsId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 6, 2, 10, 1, 4),
    _VrIpBgpAggregateNetEgpAsId_Type()
)
vrIpBgpAggregateNetEgpAsId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpBgpAggregateNetEgpAsId.setStatus("mandatory")


class _VrIpBgpAggregateNetBgpAsId_Type(Unsigned32):
    """Custom type vrIpBgpAggregateNetBgpAsId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VrIpBgpAggregateNetBgpAsId_Type.__name__ = "Unsigned32"
_VrIpBgpAggregateNetBgpAsId_Object = MibTableColumn
vrIpBgpAggregateNetBgpAsId = _VrIpBgpAggregateNetBgpAsId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 6, 2, 10, 1, 5),
    _VrIpBgpAggregateNetBgpAsId_Type()
)
vrIpBgpAggregateNetBgpAsId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpBgpAggregateNetBgpAsId.setStatus("mandatory")


class _VrIpBgpAggregateNetOspfTag_Type(Hex):
    """Custom type vrIpBgpAggregateNetOspfTag based on Hex"""
    defaultValue = 4294967295

    subtypeSpec = Hex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrIpBgpAggregateNetOspfTag_Type.__name__ = "Hex"
_VrIpBgpAggregateNetOspfTag_Object = MibTableColumn
vrIpBgpAggregateNetOspfTag = _VrIpBgpAggregateNetOspfTag_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 6, 2, 10, 1, 6),
    _VrIpBgpAggregateNetOspfTag_Type()
)
vrIpBgpAggregateNetOspfTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpBgpAggregateNetOspfTag.setStatus("mandatory")


class _VrIpBgpAggregateNetRipInterface_Type(IpAddress):
    """Custom type vrIpBgpAggregateNetRipInterface based on IpAddress"""
    defaultHexValue = "00000000"


_VrIpBgpAggregateNetRipInterface_Object = MibTableColumn
vrIpBgpAggregateNetRipInterface = _VrIpBgpAggregateNetRipInterface_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 6, 2, 10, 1, 7),
    _VrIpBgpAggregateNetRipInterface_Type()
)
vrIpBgpAggregateNetRipInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpBgpAggregateNetRipInterface.setStatus("mandatory")


class _VrIpBgpAggregateNetAction_Type(Integer32):
    """Custom type vrIpBgpAggregateNetAction based on Integer32"""
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


_VrIpBgpAggregateNetAction_Type.__name__ = "Integer32"
_VrIpBgpAggregateNetAction_Object = MibTableColumn
vrIpBgpAggregateNetAction = _VrIpBgpAggregateNetAction_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 6, 2, 10, 1, 8),
    _VrIpBgpAggregateNetAction_Type()
)
vrIpBgpAggregateNetAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpBgpAggregateNetAction.setStatus("mandatory")
_VrIpBgpIndb_ObjectIdentity = ObjectIdentity
vrIpBgpIndb = _VrIpBgpIndb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 7)
)
_VrIpBgpIndbRowStatusTable_Object = MibTable
vrIpBgpIndbRowStatusTable = _VrIpBgpIndbRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 7, 1)
)
if mibBuilder.loadTexts:
    vrIpBgpIndbRowStatusTable.setStatus("mandatory")
_VrIpBgpIndbRowStatusEntry_Object = MibTableRow
vrIpBgpIndbRowStatusEntry = _VrIpBgpIndbRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 7, 1, 1)
)
vrIpBgpIndbRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpIndbPrefixIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpIndbLengthIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpIndbPeerIndex"),
)
if mibBuilder.loadTexts:
    vrIpBgpIndbRowStatusEntry.setStatus("mandatory")
_VrIpBgpIndbRowStatus_Type = RowStatus
_VrIpBgpIndbRowStatus_Object = MibTableColumn
vrIpBgpIndbRowStatus = _VrIpBgpIndbRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 7, 1, 1, 1),
    _VrIpBgpIndbRowStatus_Type()
)
vrIpBgpIndbRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpIndbRowStatus.setStatus("mandatory")
_VrIpBgpIndbComponentName_Type = DisplayString
_VrIpBgpIndbComponentName_Object = MibTableColumn
vrIpBgpIndbComponentName = _VrIpBgpIndbComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 7, 1, 1, 2),
    _VrIpBgpIndbComponentName_Type()
)
vrIpBgpIndbComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpIndbComponentName.setStatus("mandatory")
_VrIpBgpIndbStorageType_Type = StorageType
_VrIpBgpIndbStorageType_Object = MibTableColumn
vrIpBgpIndbStorageType = _VrIpBgpIndbStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 7, 1, 1, 4),
    _VrIpBgpIndbStorageType_Type()
)
vrIpBgpIndbStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpIndbStorageType.setStatus("mandatory")
_VrIpBgpIndbPrefixIndex_Type = IpAddress
_VrIpBgpIndbPrefixIndex_Object = MibTableColumn
vrIpBgpIndbPrefixIndex = _VrIpBgpIndbPrefixIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 7, 1, 1, 10),
    _VrIpBgpIndbPrefixIndex_Type()
)
vrIpBgpIndbPrefixIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpBgpIndbPrefixIndex.setStatus("mandatory")


class _VrIpBgpIndbLengthIndex_Type(Integer32):
    """Custom type vrIpBgpIndbLengthIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_VrIpBgpIndbLengthIndex_Type.__name__ = "Integer32"
_VrIpBgpIndbLengthIndex_Object = MibTableColumn
vrIpBgpIndbLengthIndex = _VrIpBgpIndbLengthIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 7, 1, 1, 11),
    _VrIpBgpIndbLengthIndex_Type()
)
vrIpBgpIndbLengthIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpBgpIndbLengthIndex.setStatus("mandatory")
_VrIpBgpIndbPeerIndex_Type = IpAddress
_VrIpBgpIndbPeerIndex_Object = MibTableColumn
vrIpBgpIndbPeerIndex = _VrIpBgpIndbPeerIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 7, 1, 1, 12),
    _VrIpBgpIndbPeerIndex_Type()
)
vrIpBgpIndbPeerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpBgpIndbPeerIndex.setStatus("mandatory")
_VrIpBgpIndbOperTable_Object = MibTable
vrIpBgpIndbOperTable = _VrIpBgpIndbOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 7, 10)
)
if mibBuilder.loadTexts:
    vrIpBgpIndbOperTable.setStatus("mandatory")
_VrIpBgpIndbOperEntry_Object = MibTableRow
vrIpBgpIndbOperEntry = _VrIpBgpIndbOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 7, 10, 1)
)
vrIpBgpIndbOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpIndbPrefixIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpIndbLengthIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpIndbPeerIndex"),
)
if mibBuilder.loadTexts:
    vrIpBgpIndbOperEntry.setStatus("mandatory")


class _VrIpBgpIndbOrigin_Type(Integer32):
    """Custom type vrIpBgpIndbOrigin based on Integer32"""
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


_VrIpBgpIndbOrigin_Type.__name__ = "Integer32"
_VrIpBgpIndbOrigin_Object = MibTableColumn
vrIpBgpIndbOrigin = _VrIpBgpIndbOrigin_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 7, 10, 1, 4),
    _VrIpBgpIndbOrigin_Type()
)
vrIpBgpIndbOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpIndbOrigin.setStatus("mandatory")


class _VrIpBgpIndbInLocaldb_Type(Integer32):
    """Custom type vrIpBgpIndbInLocaldb based on Integer32"""
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


_VrIpBgpIndbInLocaldb_Type.__name__ = "Integer32"
_VrIpBgpIndbInLocaldb_Object = MibTableColumn
vrIpBgpIndbInLocaldb = _VrIpBgpIndbInLocaldb_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 7, 10, 1, 5),
    _VrIpBgpIndbInLocaldb_Type()
)
vrIpBgpIndbInLocaldb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpIndbInLocaldb.setStatus("mandatory")
_VrIpBgpIndbNextHop_Type = IpAddress
_VrIpBgpIndbNextHop_Object = MibTableColumn
vrIpBgpIndbNextHop = _VrIpBgpIndbNextHop_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 7, 10, 1, 6),
    _VrIpBgpIndbNextHop_Type()
)
vrIpBgpIndbNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpIndbNextHop.setStatus("mandatory")


class _VrIpBgpIndbLocalPreference_Type(Unsigned32):
    """Custom type vrIpBgpIndbLocalPreference based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrIpBgpIndbLocalPreference_Type.__name__ = "Unsigned32"
_VrIpBgpIndbLocalPreference_Object = MibTableColumn
vrIpBgpIndbLocalPreference = _VrIpBgpIndbLocalPreference_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 7, 10, 1, 7),
    _VrIpBgpIndbLocalPreference_Type()
)
vrIpBgpIndbLocalPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpIndbLocalPreference.setStatus("mandatory")


class _VrIpBgpIndbCalcLocalPref_Type(Unsigned32):
    """Custom type vrIpBgpIndbCalcLocalPref based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrIpBgpIndbCalcLocalPref_Type.__name__ = "Unsigned32"
_VrIpBgpIndbCalcLocalPref_Object = MibTableColumn
vrIpBgpIndbCalcLocalPref = _VrIpBgpIndbCalcLocalPref_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 7, 10, 1, 8),
    _VrIpBgpIndbCalcLocalPref_Type()
)
vrIpBgpIndbCalcLocalPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpIndbCalcLocalPref.setStatus("mandatory")


class _VrIpBgpIndbMultiExitDiscriminator_Type(Unsigned32):
    """Custom type vrIpBgpIndbMultiExitDiscriminator based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrIpBgpIndbMultiExitDiscriminator_Type.__name__ = "Unsigned32"
_VrIpBgpIndbMultiExitDiscriminator_Object = MibTableColumn
vrIpBgpIndbMultiExitDiscriminator = _VrIpBgpIndbMultiExitDiscriminator_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 7, 10, 1, 9),
    _VrIpBgpIndbMultiExitDiscriminator_Type()
)
vrIpBgpIndbMultiExitDiscriminator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpIndbMultiExitDiscriminator.setStatus("mandatory")


class _VrIpBgpIndbAtomicAggregate_Type(Integer32):
    """Custom type vrIpBgpIndbAtomicAggregate based on Integer32"""
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


_VrIpBgpIndbAtomicAggregate_Type.__name__ = "Integer32"
_VrIpBgpIndbAtomicAggregate_Object = MibTableColumn
vrIpBgpIndbAtomicAggregate = _VrIpBgpIndbAtomicAggregate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 7, 10, 1, 10),
    _VrIpBgpIndbAtomicAggregate_Type()
)
vrIpBgpIndbAtomicAggregate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpIndbAtomicAggregate.setStatus("mandatory")


class _VrIpBgpIndbAggregatorAs_Type(Unsigned32):
    """Custom type vrIpBgpIndbAggregatorAs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VrIpBgpIndbAggregatorAs_Type.__name__ = "Unsigned32"
_VrIpBgpIndbAggregatorAs_Object = MibTableColumn
vrIpBgpIndbAggregatorAs = _VrIpBgpIndbAggregatorAs_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 7, 10, 1, 11),
    _VrIpBgpIndbAggregatorAs_Type()
)
vrIpBgpIndbAggregatorAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpIndbAggregatorAs.setStatus("mandatory")
_VrIpBgpIndbAggregatorAddr_Type = IpAddress
_VrIpBgpIndbAggregatorAddr_Object = MibTableColumn
vrIpBgpIndbAggregatorAddr = _VrIpBgpIndbAggregatorAddr_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 7, 10, 1, 12),
    _VrIpBgpIndbAggregatorAddr_Type()
)
vrIpBgpIndbAggregatorAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpIndbAggregatorAddr.setStatus("mandatory")


class _VrIpBgpIndbAsPath_Type(AsciiString):
    """Custom type vrIpBgpIndbAsPath based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 255),
    )


_VrIpBgpIndbAsPath_Type.__name__ = "AsciiString"
_VrIpBgpIndbAsPath_Object = MibTableColumn
vrIpBgpIndbAsPath = _VrIpBgpIndbAsPath_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 7, 10, 1, 13),
    _VrIpBgpIndbAsPath_Type()
)
vrIpBgpIndbAsPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpIndbAsPath.setStatus("mandatory")


class _VrIpBgpIndbUnknownAttributes_Type(AsciiString):
    """Custom type vrIpBgpIndbUnknownAttributes based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VrIpBgpIndbUnknownAttributes_Type.__name__ = "AsciiString"
_VrIpBgpIndbUnknownAttributes_Object = MibTableColumn
vrIpBgpIndbUnknownAttributes = _VrIpBgpIndbUnknownAttributes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 7, 10, 1, 14),
    _VrIpBgpIndbUnknownAttributes_Type()
)
vrIpBgpIndbUnknownAttributes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpIndbUnknownAttributes.setStatus("mandatory")


class _VrIpBgpIndbCommunityPath_Type(AsciiString):
    """Custom type vrIpBgpIndbCommunityPath based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VrIpBgpIndbCommunityPath_Type.__name__ = "AsciiString"
_VrIpBgpIndbCommunityPath_Object = MibTableColumn
vrIpBgpIndbCommunityPath = _VrIpBgpIndbCommunityPath_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 7, 10, 1, 15),
    _VrIpBgpIndbCommunityPath_Type()
)
vrIpBgpIndbCommunityPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpIndbCommunityPath.setStatus("mandatory")
_VrIpBgpIndbAsOriginatorId_Type = IpAddress
_VrIpBgpIndbAsOriginatorId_Object = MibTableColumn
vrIpBgpIndbAsOriginatorId = _VrIpBgpIndbAsOriginatorId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 7, 10, 1, 16),
    _VrIpBgpIndbAsOriginatorId_Type()
)
vrIpBgpIndbAsOriginatorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpIndbAsOriginatorId.setStatus("mandatory")
_VrIpBgpIndbRrClusterListTable_Object = MibTable
vrIpBgpIndbRrClusterListTable = _VrIpBgpIndbRrClusterListTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 7, 798)
)
if mibBuilder.loadTexts:
    vrIpBgpIndbRrClusterListTable.setStatus("mandatory")
_VrIpBgpIndbRrClusterListEntry_Object = MibTableRow
vrIpBgpIndbRrClusterListEntry = _VrIpBgpIndbRrClusterListEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 7, 798, 1)
)
vrIpBgpIndbRrClusterListEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpIndbPrefixIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpIndbLengthIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpIndbPeerIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpIndbRrClusterListValue"),
)
if mibBuilder.loadTexts:
    vrIpBgpIndbRrClusterListEntry.setStatus("mandatory")
_VrIpBgpIndbRrClusterListValue_Type = IpAddress
_VrIpBgpIndbRrClusterListValue_Object = MibTableColumn
vrIpBgpIndbRrClusterListValue = _VrIpBgpIndbRrClusterListValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 7, 798, 1, 1),
    _VrIpBgpIndbRrClusterListValue_Type()
)
vrIpBgpIndbRrClusterListValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpIndbRrClusterListValue.setStatus("mandatory")
_VrIpBgpLocaldb_ObjectIdentity = ObjectIdentity
vrIpBgpLocaldb = _VrIpBgpLocaldb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 8)
)
_VrIpBgpLocaldbRowStatusTable_Object = MibTable
vrIpBgpLocaldbRowStatusTable = _VrIpBgpLocaldbRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 8, 1)
)
if mibBuilder.loadTexts:
    vrIpBgpLocaldbRowStatusTable.setStatus("mandatory")
_VrIpBgpLocaldbRowStatusEntry_Object = MibTableRow
vrIpBgpLocaldbRowStatusEntry = _VrIpBgpLocaldbRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 8, 1, 1)
)
vrIpBgpLocaldbRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpLocaldbPrefixIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpLocaldbLengthIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpLocaldbPeerIndex"),
)
if mibBuilder.loadTexts:
    vrIpBgpLocaldbRowStatusEntry.setStatus("mandatory")
_VrIpBgpLocaldbRowStatus_Type = RowStatus
_VrIpBgpLocaldbRowStatus_Object = MibTableColumn
vrIpBgpLocaldbRowStatus = _VrIpBgpLocaldbRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 8, 1, 1, 1),
    _VrIpBgpLocaldbRowStatus_Type()
)
vrIpBgpLocaldbRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpLocaldbRowStatus.setStatus("mandatory")
_VrIpBgpLocaldbComponentName_Type = DisplayString
_VrIpBgpLocaldbComponentName_Object = MibTableColumn
vrIpBgpLocaldbComponentName = _VrIpBgpLocaldbComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 8, 1, 1, 2),
    _VrIpBgpLocaldbComponentName_Type()
)
vrIpBgpLocaldbComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpLocaldbComponentName.setStatus("mandatory")
_VrIpBgpLocaldbStorageType_Type = StorageType
_VrIpBgpLocaldbStorageType_Object = MibTableColumn
vrIpBgpLocaldbStorageType = _VrIpBgpLocaldbStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 8, 1, 1, 4),
    _VrIpBgpLocaldbStorageType_Type()
)
vrIpBgpLocaldbStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpLocaldbStorageType.setStatus("mandatory")
_VrIpBgpLocaldbPrefixIndex_Type = IpAddress
_VrIpBgpLocaldbPrefixIndex_Object = MibTableColumn
vrIpBgpLocaldbPrefixIndex = _VrIpBgpLocaldbPrefixIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 8, 1, 1, 10),
    _VrIpBgpLocaldbPrefixIndex_Type()
)
vrIpBgpLocaldbPrefixIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpBgpLocaldbPrefixIndex.setStatus("mandatory")


class _VrIpBgpLocaldbLengthIndex_Type(Integer32):
    """Custom type vrIpBgpLocaldbLengthIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_VrIpBgpLocaldbLengthIndex_Type.__name__ = "Integer32"
_VrIpBgpLocaldbLengthIndex_Object = MibTableColumn
vrIpBgpLocaldbLengthIndex = _VrIpBgpLocaldbLengthIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 8, 1, 1, 11),
    _VrIpBgpLocaldbLengthIndex_Type()
)
vrIpBgpLocaldbLengthIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpBgpLocaldbLengthIndex.setStatus("mandatory")
_VrIpBgpLocaldbPeerIndex_Type = IpAddress
_VrIpBgpLocaldbPeerIndex_Object = MibTableColumn
vrIpBgpLocaldbPeerIndex = _VrIpBgpLocaldbPeerIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 8, 1, 1, 12),
    _VrIpBgpLocaldbPeerIndex_Type()
)
vrIpBgpLocaldbPeerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpBgpLocaldbPeerIndex.setStatus("mandatory")
_VrIpBgpLocaldbOperTable_Object = MibTable
vrIpBgpLocaldbOperTable = _VrIpBgpLocaldbOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 8, 10)
)
if mibBuilder.loadTexts:
    vrIpBgpLocaldbOperTable.setStatus("mandatory")
_VrIpBgpLocaldbOperEntry_Object = MibTableRow
vrIpBgpLocaldbOperEntry = _VrIpBgpLocaldbOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 8, 10, 1)
)
vrIpBgpLocaldbOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpLocaldbPrefixIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpLocaldbLengthIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpLocaldbPeerIndex"),
)
if mibBuilder.loadTexts:
    vrIpBgpLocaldbOperEntry.setStatus("mandatory")


class _VrIpBgpLocaldbOrigin_Type(Integer32):
    """Custom type vrIpBgpLocaldbOrigin based on Integer32"""
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


_VrIpBgpLocaldbOrigin_Type.__name__ = "Integer32"
_VrIpBgpLocaldbOrigin_Object = MibTableColumn
vrIpBgpLocaldbOrigin = _VrIpBgpLocaldbOrigin_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 8, 10, 1, 4),
    _VrIpBgpLocaldbOrigin_Type()
)
vrIpBgpLocaldbOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpLocaldbOrigin.setStatus("mandatory")
_VrIpBgpLocaldbNextHop_Type = IpAddress
_VrIpBgpLocaldbNextHop_Object = MibTableColumn
vrIpBgpLocaldbNextHop = _VrIpBgpLocaldbNextHop_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 8, 10, 1, 5),
    _VrIpBgpLocaldbNextHop_Type()
)
vrIpBgpLocaldbNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpLocaldbNextHop.setStatus("mandatory")


class _VrIpBgpLocaldbLocalPreference_Type(Unsigned32):
    """Custom type vrIpBgpLocaldbLocalPreference based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrIpBgpLocaldbLocalPreference_Type.__name__ = "Unsigned32"
_VrIpBgpLocaldbLocalPreference_Object = MibTableColumn
vrIpBgpLocaldbLocalPreference = _VrIpBgpLocaldbLocalPreference_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 8, 10, 1, 6),
    _VrIpBgpLocaldbLocalPreference_Type()
)
vrIpBgpLocaldbLocalPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpLocaldbLocalPreference.setStatus("mandatory")


class _VrIpBgpLocaldbMultiExitDiscriminator_Type(Unsigned32):
    """Custom type vrIpBgpLocaldbMultiExitDiscriminator based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrIpBgpLocaldbMultiExitDiscriminator_Type.__name__ = "Unsigned32"
_VrIpBgpLocaldbMultiExitDiscriminator_Object = MibTableColumn
vrIpBgpLocaldbMultiExitDiscriminator = _VrIpBgpLocaldbMultiExitDiscriminator_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 8, 10, 1, 7),
    _VrIpBgpLocaldbMultiExitDiscriminator_Type()
)
vrIpBgpLocaldbMultiExitDiscriminator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpLocaldbMultiExitDiscriminator.setStatus("mandatory")


class _VrIpBgpLocaldbAtomicAggregate_Type(Integer32):
    """Custom type vrIpBgpLocaldbAtomicAggregate based on Integer32"""
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


_VrIpBgpLocaldbAtomicAggregate_Type.__name__ = "Integer32"
_VrIpBgpLocaldbAtomicAggregate_Object = MibTableColumn
vrIpBgpLocaldbAtomicAggregate = _VrIpBgpLocaldbAtomicAggregate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 8, 10, 1, 8),
    _VrIpBgpLocaldbAtomicAggregate_Type()
)
vrIpBgpLocaldbAtomicAggregate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpLocaldbAtomicAggregate.setStatus("mandatory")


class _VrIpBgpLocaldbAggregatorAs_Type(Unsigned32):
    """Custom type vrIpBgpLocaldbAggregatorAs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VrIpBgpLocaldbAggregatorAs_Type.__name__ = "Unsigned32"
_VrIpBgpLocaldbAggregatorAs_Object = MibTableColumn
vrIpBgpLocaldbAggregatorAs = _VrIpBgpLocaldbAggregatorAs_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 8, 10, 1, 9),
    _VrIpBgpLocaldbAggregatorAs_Type()
)
vrIpBgpLocaldbAggregatorAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpLocaldbAggregatorAs.setStatus("mandatory")
_VrIpBgpLocaldbAggregatorAddr_Type = IpAddress
_VrIpBgpLocaldbAggregatorAddr_Object = MibTableColumn
vrIpBgpLocaldbAggregatorAddr = _VrIpBgpLocaldbAggregatorAddr_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 8, 10, 1, 10),
    _VrIpBgpLocaldbAggregatorAddr_Type()
)
vrIpBgpLocaldbAggregatorAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpLocaldbAggregatorAddr.setStatus("mandatory")


class _VrIpBgpLocaldbAsPath_Type(AsciiString):
    """Custom type vrIpBgpLocaldbAsPath based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 255),
    )


_VrIpBgpLocaldbAsPath_Type.__name__ = "AsciiString"
_VrIpBgpLocaldbAsPath_Object = MibTableColumn
vrIpBgpLocaldbAsPath = _VrIpBgpLocaldbAsPath_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 8, 10, 1, 11),
    _VrIpBgpLocaldbAsPath_Type()
)
vrIpBgpLocaldbAsPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpLocaldbAsPath.setStatus("mandatory")


class _VrIpBgpLocaldbUnknownAttributes_Type(AsciiString):
    """Custom type vrIpBgpLocaldbUnknownAttributes based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VrIpBgpLocaldbUnknownAttributes_Type.__name__ = "AsciiString"
_VrIpBgpLocaldbUnknownAttributes_Object = MibTableColumn
vrIpBgpLocaldbUnknownAttributes = _VrIpBgpLocaldbUnknownAttributes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 8, 10, 1, 12),
    _VrIpBgpLocaldbUnknownAttributes_Type()
)
vrIpBgpLocaldbUnknownAttributes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpLocaldbUnknownAttributes.setStatus("mandatory")


class _VrIpBgpLocaldbCommunityPath_Type(AsciiString):
    """Custom type vrIpBgpLocaldbCommunityPath based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VrIpBgpLocaldbCommunityPath_Type.__name__ = "AsciiString"
_VrIpBgpLocaldbCommunityPath_Object = MibTableColumn
vrIpBgpLocaldbCommunityPath = _VrIpBgpLocaldbCommunityPath_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 8, 10, 1, 13),
    _VrIpBgpLocaldbCommunityPath_Type()
)
vrIpBgpLocaldbCommunityPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpLocaldbCommunityPath.setStatus("mandatory")
_VrIpBgpLocaldbAsOriginatorId_Type = IpAddress
_VrIpBgpLocaldbAsOriginatorId_Object = MibTableColumn
vrIpBgpLocaldbAsOriginatorId = _VrIpBgpLocaldbAsOriginatorId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 8, 10, 1, 14),
    _VrIpBgpLocaldbAsOriginatorId_Type()
)
vrIpBgpLocaldbAsOriginatorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpLocaldbAsOriginatorId.setStatus("mandatory")
_VrIpBgpLocaldbRrClusterListTable_Object = MibTable
vrIpBgpLocaldbRrClusterListTable = _VrIpBgpLocaldbRrClusterListTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 8, 797)
)
if mibBuilder.loadTexts:
    vrIpBgpLocaldbRrClusterListTable.setStatus("mandatory")
_VrIpBgpLocaldbRrClusterListEntry_Object = MibTableRow
vrIpBgpLocaldbRrClusterListEntry = _VrIpBgpLocaldbRrClusterListEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 8, 797, 1)
)
vrIpBgpLocaldbRrClusterListEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpLocaldbPrefixIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpLocaldbLengthIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpLocaldbPeerIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpLocaldbRrClusterListValue"),
)
if mibBuilder.loadTexts:
    vrIpBgpLocaldbRrClusterListEntry.setStatus("mandatory")
_VrIpBgpLocaldbRrClusterListValue_Type = IpAddress
_VrIpBgpLocaldbRrClusterListValue_Object = MibTableColumn
vrIpBgpLocaldbRrClusterListValue = _VrIpBgpLocaldbRrClusterListValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 8, 797, 1, 1),
    _VrIpBgpLocaldbRrClusterListValue_Type()
)
vrIpBgpLocaldbRrClusterListValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpLocaldbRrClusterListValue.setStatus("mandatory")
_VrIpBgpOutdb_ObjectIdentity = ObjectIdentity
vrIpBgpOutdb = _VrIpBgpOutdb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 9)
)
_VrIpBgpOutdbRowStatusTable_Object = MibTable
vrIpBgpOutdbRowStatusTable = _VrIpBgpOutdbRowStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 9, 1)
)
if mibBuilder.loadTexts:
    vrIpBgpOutdbRowStatusTable.setStatus("mandatory")
_VrIpBgpOutdbRowStatusEntry_Object = MibTableRow
vrIpBgpOutdbRowStatusEntry = _VrIpBgpOutdbRowStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 9, 1, 1)
)
vrIpBgpOutdbRowStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpOutdbPrefixIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpOutdbLengthIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpOutdbPeerIndex"),
)
if mibBuilder.loadTexts:
    vrIpBgpOutdbRowStatusEntry.setStatus("mandatory")
_VrIpBgpOutdbRowStatus_Type = RowStatus
_VrIpBgpOutdbRowStatus_Object = MibTableColumn
vrIpBgpOutdbRowStatus = _VrIpBgpOutdbRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 9, 1, 1, 1),
    _VrIpBgpOutdbRowStatus_Type()
)
vrIpBgpOutdbRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpOutdbRowStatus.setStatus("mandatory")
_VrIpBgpOutdbComponentName_Type = DisplayString
_VrIpBgpOutdbComponentName_Object = MibTableColumn
vrIpBgpOutdbComponentName = _VrIpBgpOutdbComponentName_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 9, 1, 1, 2),
    _VrIpBgpOutdbComponentName_Type()
)
vrIpBgpOutdbComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpOutdbComponentName.setStatus("mandatory")
_VrIpBgpOutdbStorageType_Type = StorageType
_VrIpBgpOutdbStorageType_Object = MibTableColumn
vrIpBgpOutdbStorageType = _VrIpBgpOutdbStorageType_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 9, 1, 1, 4),
    _VrIpBgpOutdbStorageType_Type()
)
vrIpBgpOutdbStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpOutdbStorageType.setStatus("mandatory")
_VrIpBgpOutdbPrefixIndex_Type = IpAddress
_VrIpBgpOutdbPrefixIndex_Object = MibTableColumn
vrIpBgpOutdbPrefixIndex = _VrIpBgpOutdbPrefixIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 9, 1, 1, 10),
    _VrIpBgpOutdbPrefixIndex_Type()
)
vrIpBgpOutdbPrefixIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpBgpOutdbPrefixIndex.setStatus("mandatory")


class _VrIpBgpOutdbLengthIndex_Type(Integer32):
    """Custom type vrIpBgpOutdbLengthIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_VrIpBgpOutdbLengthIndex_Type.__name__ = "Integer32"
_VrIpBgpOutdbLengthIndex_Object = MibTableColumn
vrIpBgpOutdbLengthIndex = _VrIpBgpOutdbLengthIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 9, 1, 1, 11),
    _VrIpBgpOutdbLengthIndex_Type()
)
vrIpBgpOutdbLengthIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpBgpOutdbLengthIndex.setStatus("mandatory")
_VrIpBgpOutdbPeerIndex_Type = IpAddress
_VrIpBgpOutdbPeerIndex_Object = MibTableColumn
vrIpBgpOutdbPeerIndex = _VrIpBgpOutdbPeerIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 9, 1, 1, 12),
    _VrIpBgpOutdbPeerIndex_Type()
)
vrIpBgpOutdbPeerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vrIpBgpOutdbPeerIndex.setStatus("mandatory")
_VrIpBgpOutdbOperTable_Object = MibTable
vrIpBgpOutdbOperTable = _VrIpBgpOutdbOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 9, 10)
)
if mibBuilder.loadTexts:
    vrIpBgpOutdbOperTable.setStatus("mandatory")
_VrIpBgpOutdbOperEntry_Object = MibTableRow
vrIpBgpOutdbOperEntry = _VrIpBgpOutdbOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 9, 10, 1)
)
vrIpBgpOutdbOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpOutdbPrefixIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpOutdbLengthIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpOutdbPeerIndex"),
)
if mibBuilder.loadTexts:
    vrIpBgpOutdbOperEntry.setStatus("mandatory")


class _VrIpBgpOutdbOrigin_Type(Integer32):
    """Custom type vrIpBgpOutdbOrigin based on Integer32"""
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


_VrIpBgpOutdbOrigin_Type.__name__ = "Integer32"
_VrIpBgpOutdbOrigin_Object = MibTableColumn
vrIpBgpOutdbOrigin = _VrIpBgpOutdbOrigin_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 9, 10, 1, 4),
    _VrIpBgpOutdbOrigin_Type()
)
vrIpBgpOutdbOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpOutdbOrigin.setStatus("mandatory")
_VrIpBgpOutdbNextHop_Type = IpAddress
_VrIpBgpOutdbNextHop_Object = MibTableColumn
vrIpBgpOutdbNextHop = _VrIpBgpOutdbNextHop_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 9, 10, 1, 5),
    _VrIpBgpOutdbNextHop_Type()
)
vrIpBgpOutdbNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpOutdbNextHop.setStatus("mandatory")


class _VrIpBgpOutdbLocalPreference_Type(Unsigned32):
    """Custom type vrIpBgpOutdbLocalPreference based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrIpBgpOutdbLocalPreference_Type.__name__ = "Unsigned32"
_VrIpBgpOutdbLocalPreference_Object = MibTableColumn
vrIpBgpOutdbLocalPreference = _VrIpBgpOutdbLocalPreference_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 9, 10, 1, 6),
    _VrIpBgpOutdbLocalPreference_Type()
)
vrIpBgpOutdbLocalPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpOutdbLocalPreference.setStatus("mandatory")


class _VrIpBgpOutdbMultiExitDiscriminator_Type(Unsigned32):
    """Custom type vrIpBgpOutdbMultiExitDiscriminator based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrIpBgpOutdbMultiExitDiscriminator_Type.__name__ = "Unsigned32"
_VrIpBgpOutdbMultiExitDiscriminator_Object = MibTableColumn
vrIpBgpOutdbMultiExitDiscriminator = _VrIpBgpOutdbMultiExitDiscriminator_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 9, 10, 1, 7),
    _VrIpBgpOutdbMultiExitDiscriminator_Type()
)
vrIpBgpOutdbMultiExitDiscriminator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpOutdbMultiExitDiscriminator.setStatus("mandatory")


class _VrIpBgpOutdbAtomicAggregate_Type(Integer32):
    """Custom type vrIpBgpOutdbAtomicAggregate based on Integer32"""
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


_VrIpBgpOutdbAtomicAggregate_Type.__name__ = "Integer32"
_VrIpBgpOutdbAtomicAggregate_Object = MibTableColumn
vrIpBgpOutdbAtomicAggregate = _VrIpBgpOutdbAtomicAggregate_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 9, 10, 1, 8),
    _VrIpBgpOutdbAtomicAggregate_Type()
)
vrIpBgpOutdbAtomicAggregate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpOutdbAtomicAggregate.setStatus("mandatory")


class _VrIpBgpOutdbAggregatorAs_Type(Unsigned32):
    """Custom type vrIpBgpOutdbAggregatorAs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VrIpBgpOutdbAggregatorAs_Type.__name__ = "Unsigned32"
_VrIpBgpOutdbAggregatorAs_Object = MibTableColumn
vrIpBgpOutdbAggregatorAs = _VrIpBgpOutdbAggregatorAs_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 9, 10, 1, 9),
    _VrIpBgpOutdbAggregatorAs_Type()
)
vrIpBgpOutdbAggregatorAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpOutdbAggregatorAs.setStatus("mandatory")
_VrIpBgpOutdbAggregatorAddr_Type = IpAddress
_VrIpBgpOutdbAggregatorAddr_Object = MibTableColumn
vrIpBgpOutdbAggregatorAddr = _VrIpBgpOutdbAggregatorAddr_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 9, 10, 1, 10),
    _VrIpBgpOutdbAggregatorAddr_Type()
)
vrIpBgpOutdbAggregatorAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpOutdbAggregatorAddr.setStatus("mandatory")


class _VrIpBgpOutdbAsPath_Type(AsciiString):
    """Custom type vrIpBgpOutdbAsPath based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 255),
    )


_VrIpBgpOutdbAsPath_Type.__name__ = "AsciiString"
_VrIpBgpOutdbAsPath_Object = MibTableColumn
vrIpBgpOutdbAsPath = _VrIpBgpOutdbAsPath_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 9, 10, 1, 11),
    _VrIpBgpOutdbAsPath_Type()
)
vrIpBgpOutdbAsPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpOutdbAsPath.setStatus("mandatory")


class _VrIpBgpOutdbUnknownAttributes_Type(AsciiString):
    """Custom type vrIpBgpOutdbUnknownAttributes based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VrIpBgpOutdbUnknownAttributes_Type.__name__ = "AsciiString"
_VrIpBgpOutdbUnknownAttributes_Object = MibTableColumn
vrIpBgpOutdbUnknownAttributes = _VrIpBgpOutdbUnknownAttributes_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 9, 10, 1, 12),
    _VrIpBgpOutdbUnknownAttributes_Type()
)
vrIpBgpOutdbUnknownAttributes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpOutdbUnknownAttributes.setStatus("mandatory")


class _VrIpBgpOutdbCommunityPath_Type(AsciiString):
    """Custom type vrIpBgpOutdbCommunityPath based on AsciiString"""
    subtypeSpec = AsciiString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VrIpBgpOutdbCommunityPath_Type.__name__ = "AsciiString"
_VrIpBgpOutdbCommunityPath_Object = MibTableColumn
vrIpBgpOutdbCommunityPath = _VrIpBgpOutdbCommunityPath_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 9, 10, 1, 13),
    _VrIpBgpOutdbCommunityPath_Type()
)
vrIpBgpOutdbCommunityPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpOutdbCommunityPath.setStatus("mandatory")
_VrIpBgpOutdbAsOriginatorId_Type = IpAddress
_VrIpBgpOutdbAsOriginatorId_Object = MibTableColumn
vrIpBgpOutdbAsOriginatorId = _VrIpBgpOutdbAsOriginatorId_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 9, 10, 1, 14),
    _VrIpBgpOutdbAsOriginatorId_Type()
)
vrIpBgpOutdbAsOriginatorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpOutdbAsOriginatorId.setStatus("mandatory")
_VrIpBgpOutdbRrClusterListTable_Object = MibTable
vrIpBgpOutdbRrClusterListTable = _VrIpBgpOutdbRrClusterListTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 9, 799)
)
if mibBuilder.loadTexts:
    vrIpBgpOutdbRrClusterListTable.setStatus("mandatory")
_VrIpBgpOutdbRrClusterListEntry_Object = MibTableRow
vrIpBgpOutdbRrClusterListEntry = _VrIpBgpOutdbRrClusterListEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 9, 799, 1)
)
vrIpBgpOutdbRrClusterListEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpOutdbPrefixIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpOutdbLengthIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpOutdbPeerIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpOutdbRrClusterListValue"),
)
if mibBuilder.loadTexts:
    vrIpBgpOutdbRrClusterListEntry.setStatus("mandatory")
_VrIpBgpOutdbRrClusterListValue_Type = IpAddress
_VrIpBgpOutdbRrClusterListValue_Object = MibTableColumn
vrIpBgpOutdbRrClusterListValue = _VrIpBgpOutdbRrClusterListValue_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 9, 799, 1, 1),
    _VrIpBgpOutdbRrClusterListValue_Type()
)
vrIpBgpOutdbRrClusterListValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpOutdbRrClusterListValue.setStatus("mandatory")
_VrIpBgpProvTable_Object = MibTable
vrIpBgpProvTable = _VrIpBgpProvTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 100)
)
if mibBuilder.loadTexts:
    vrIpBgpProvTable.setStatus("mandatory")
_VrIpBgpProvEntry_Object = MibTableRow
vrIpBgpProvEntry = _VrIpBgpProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 100, 1)
)
vrIpBgpProvEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpIndex"),
)
if mibBuilder.loadTexts:
    vrIpBgpProvEntry.setStatus("mandatory")
_VrIpBgpBgpIdentifier_Type = IpAddress
_VrIpBgpBgpIdentifier_Object = MibTableColumn
vrIpBgpBgpIdentifier = _VrIpBgpBgpIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 100, 1, 1),
    _VrIpBgpBgpIdentifier_Type()
)
vrIpBgpBgpIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpBgpBgpIdentifier.setStatus("mandatory")


class _VrIpBgpLocalAs_Type(Unsigned32):
    """Custom type vrIpBgpLocalAs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VrIpBgpLocalAs_Type.__name__ = "Unsigned32"
_VrIpBgpLocalAs_Object = MibTableColumn
vrIpBgpLocalAs = _VrIpBgpLocalAs_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 100, 1, 2),
    _VrIpBgpLocalAs_Type()
)
vrIpBgpLocalAs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpBgpLocalAs.setStatus("mandatory")


class _VrIpBgpDefaultLocalPreference_Type(Unsigned32):
    """Custom type vrIpBgpDefaultLocalPreference based on Unsigned32"""
    defaultValue = 144

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrIpBgpDefaultLocalPreference_Type.__name__ = "Unsigned32"
_VrIpBgpDefaultLocalPreference_Object = MibTableColumn
vrIpBgpDefaultLocalPreference = _VrIpBgpDefaultLocalPreference_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 100, 1, 3),
    _VrIpBgpDefaultLocalPreference_Type()
)
vrIpBgpDefaultLocalPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpBgpDefaultLocalPreference.setStatus("mandatory")


class _VrIpBgpDefaultMultiExitDisc_Type(Unsigned32):
    """Custom type vrIpBgpDefaultMultiExitDisc based on Unsigned32"""
    defaultValue = 4294967294

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VrIpBgpDefaultMultiExitDisc_Type.__name__ = "Unsigned32"
_VrIpBgpDefaultMultiExitDisc_Object = MibTableColumn
vrIpBgpDefaultMultiExitDisc = _VrIpBgpDefaultMultiExitDisc_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 100, 1, 4),
    _VrIpBgpDefaultMultiExitDisc_Type()
)
vrIpBgpDefaultMultiExitDisc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpBgpDefaultMultiExitDisc.setStatus("mandatory")


class _VrIpBgpRouteThrottleLimit_Type(Unsigned32):
    """Custom type vrIpBgpRouteThrottleLimit based on Unsigned32"""
    defaultValue = 250

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_VrIpBgpRouteThrottleLimit_Type.__name__ = "Unsigned32"
_VrIpBgpRouteThrottleLimit_Object = MibTableColumn
vrIpBgpRouteThrottleLimit = _VrIpBgpRouteThrottleLimit_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 100, 1, 5),
    _VrIpBgpRouteThrottleLimit_Type()
)
vrIpBgpRouteThrottleLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpBgpRouteThrottleLimit.setStatus("mandatory")


class _VrIpBgpRouteThrottleInter_Type(Unsigned32):
    """Custom type vrIpBgpRouteThrottleInter based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_VrIpBgpRouteThrottleInter_Type.__name__ = "Unsigned32"
_VrIpBgpRouteThrottleInter_Object = MibTableColumn
vrIpBgpRouteThrottleInter = _VrIpBgpRouteThrottleInter_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 100, 1, 6),
    _VrIpBgpRouteThrottleInter_Type()
)
vrIpBgpRouteThrottleInter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpBgpRouteThrottleInter.setStatus("mandatory")


class _VrIpBgpRouteReflector_Type(Integer32):
    """Custom type vrIpBgpRouteReflector based on Integer32"""
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


_VrIpBgpRouteReflector_Type.__name__ = "Integer32"
_VrIpBgpRouteReflector_Object = MibTableColumn
vrIpBgpRouteReflector = _VrIpBgpRouteReflector_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 100, 1, 7),
    _VrIpBgpRouteReflector_Type()
)
vrIpBgpRouteReflector.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpBgpRouteReflector.setStatus("mandatory")
_VrIpBgpRouteReflectorCluster_Type = IpAddress
_VrIpBgpRouteReflectorCluster_Object = MibTableColumn
vrIpBgpRouteReflectorCluster = _VrIpBgpRouteReflectorCluster_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 100, 1, 8),
    _VrIpBgpRouteReflectorCluster_Type()
)
vrIpBgpRouteReflectorCluster.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpBgpRouteReflectorCluster.setStatus("mandatory")
_VrIpBgpOperTable_Object = MibTable
vrIpBgpOperTable = _VrIpBgpOperTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 101)
)
if mibBuilder.loadTexts:
    vrIpBgpOperTable.setStatus("mandatory")
_VrIpBgpOperEntry_Object = MibTableRow
vrIpBgpOperEntry = _VrIpBgpOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 101, 1)
)
vrIpBgpOperEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpIndex"),
)
if mibBuilder.loadTexts:
    vrIpBgpOperEntry.setStatus("mandatory")
_VrIpBgpTableVersion_Type = Counter32
_VrIpBgpTableVersion_Object = MibTableColumn
vrIpBgpTableVersion = _VrIpBgpTableVersion_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 101, 1, 2),
    _VrIpBgpTableVersion_Type()
)
vrIpBgpTableVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpTableVersion.setStatus("mandatory")
_VrIpBgpInMsgs_Type = Counter32
_VrIpBgpInMsgs_Object = MibTableColumn
vrIpBgpInMsgs = _VrIpBgpInMsgs_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 101, 1, 3),
    _VrIpBgpInMsgs_Type()
)
vrIpBgpInMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpInMsgs.setStatus("mandatory")
_VrIpBgpInErrors_Type = Counter32
_VrIpBgpInErrors_Object = MibTableColumn
vrIpBgpInErrors = _VrIpBgpInErrors_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 101, 1, 4),
    _VrIpBgpInErrors_Type()
)
vrIpBgpInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpInErrors.setStatus("mandatory")
_VrIpBgpInErrorMsgs_Type = Counter32
_VrIpBgpInErrorMsgs_Object = MibTableColumn
vrIpBgpInErrorMsgs = _VrIpBgpInErrorMsgs_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 101, 1, 5),
    _VrIpBgpInErrorMsgs_Type()
)
vrIpBgpInErrorMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpInErrorMsgs.setStatus("mandatory")
_VrIpBgpOutMsgs_Type = Counter32
_VrIpBgpOutMsgs_Object = MibTableColumn
vrIpBgpOutMsgs = _VrIpBgpOutMsgs_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 101, 1, 6),
    _VrIpBgpOutMsgs_Type()
)
vrIpBgpOutMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpOutMsgs.setStatus("mandatory")
_VrIpBgpOutDiscards_Type = Counter32
_VrIpBgpOutDiscards_Object = MibTableColumn
vrIpBgpOutDiscards = _VrIpBgpOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 101, 1, 7),
    _VrIpBgpOutDiscards_Type()
)
vrIpBgpOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpOutDiscards.setStatus("mandatory")
_VrIpBgpOutErrorMsgs_Type = Counter32
_VrIpBgpOutErrorMsgs_Object = MibTableColumn
vrIpBgpOutErrorMsgs = _VrIpBgpOutErrorMsgs_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 101, 1, 8),
    _VrIpBgpOutErrorMsgs_Type()
)
vrIpBgpOutErrorMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpOutErrorMsgs.setStatus("mandatory")
_VrIpBgpIndbSize_Type = Counter32
_VrIpBgpIndbSize_Object = MibTableColumn
vrIpBgpIndbSize = _VrIpBgpIndbSize_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 101, 1, 9),
    _VrIpBgpIndbSize_Type()
)
vrIpBgpIndbSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpIndbSize.setStatus("mandatory")
_VrIpBgpStateTable_Object = MibTable
vrIpBgpStateTable = _VrIpBgpStateTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 102)
)
if mibBuilder.loadTexts:
    vrIpBgpStateTable.setStatus("mandatory")
_VrIpBgpStateEntry_Object = MibTableRow
vrIpBgpStateEntry = _VrIpBgpStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 102, 1)
)
vrIpBgpStateEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpIndex"),
)
if mibBuilder.loadTexts:
    vrIpBgpStateEntry.setStatus("mandatory")


class _VrIpBgpAdminState_Type(Integer32):
    """Custom type vrIpBgpAdminState based on Integer32"""
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


_VrIpBgpAdminState_Type.__name__ = "Integer32"
_VrIpBgpAdminState_Object = MibTableColumn
vrIpBgpAdminState = _VrIpBgpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 102, 1, 1),
    _VrIpBgpAdminState_Type()
)
vrIpBgpAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpAdminState.setStatus("mandatory")


class _VrIpBgpOperationalState_Type(Integer32):
    """Custom type vrIpBgpOperationalState based on Integer32"""
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


_VrIpBgpOperationalState_Type.__name__ = "Integer32"
_VrIpBgpOperationalState_Object = MibTableColumn
vrIpBgpOperationalState = _VrIpBgpOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 102, 1, 2),
    _VrIpBgpOperationalState_Type()
)
vrIpBgpOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpOperationalState.setStatus("mandatory")


class _VrIpBgpUsageState_Type(Integer32):
    """Custom type vrIpBgpUsageState based on Integer32"""
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


_VrIpBgpUsageState_Type.__name__ = "Integer32"
_VrIpBgpUsageState_Object = MibTableColumn
vrIpBgpUsageState = _VrIpBgpUsageState_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 102, 1, 3),
    _VrIpBgpUsageState_Type()
)
vrIpBgpUsageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpUsageState.setStatus("mandatory")
_VrIpBgpAdminControlTable_Object = MibTable
vrIpBgpAdminControlTable = _VrIpBgpAdminControlTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 103)
)
if mibBuilder.loadTexts:
    vrIpBgpAdminControlTable.setStatus("mandatory")
_VrIpBgpAdminControlEntry_Object = MibTableRow
vrIpBgpAdminControlEntry = _VrIpBgpAdminControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 103, 1)
)
vrIpBgpAdminControlEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpIndex"),
)
if mibBuilder.loadTexts:
    vrIpBgpAdminControlEntry.setStatus("mandatory")


class _VrIpBgpSnmpAdminStatus_Type(Integer32):
    """Custom type vrIpBgpSnmpAdminStatus based on Integer32"""
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


_VrIpBgpSnmpAdminStatus_Type.__name__ = "Integer32"
_VrIpBgpSnmpAdminStatus_Object = MibTableColumn
vrIpBgpSnmpAdminStatus = _VrIpBgpSnmpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 103, 1, 1),
    _VrIpBgpSnmpAdminStatus_Type()
)
vrIpBgpSnmpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vrIpBgpSnmpAdminStatus.setStatus("mandatory")
_VrIpBgpOperStatusTable_Object = MibTable
vrIpBgpOperStatusTable = _VrIpBgpOperStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 106)
)
if mibBuilder.loadTexts:
    vrIpBgpOperStatusTable.setStatus("mandatory")
_VrIpBgpOperStatusEntry_Object = MibTableRow
vrIpBgpOperStatusEntry = _VrIpBgpOperStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 106, 1)
)
vrIpBgpOperStatusEntry.setIndexNames(
    (0, "Nortel-Magellan-Passport-VirtualRouterMIB", "vrIndex"),
    (0, "Nortel-Magellan-Passport-IpMIB", "vrIpIndex"),
    (0, "Nortel-Magellan-Passport-BgpMIB", "vrIpBgpIndex"),
)
if mibBuilder.loadTexts:
    vrIpBgpOperStatusEntry.setStatus("mandatory")


class _VrIpBgpSnmpOperStatus_Type(Integer32):
    """Custom type vrIpBgpSnmpOperStatus based on Integer32"""
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


_VrIpBgpSnmpOperStatus_Type.__name__ = "Integer32"
_VrIpBgpSnmpOperStatus_Object = MibTableColumn
vrIpBgpSnmpOperStatus = _VrIpBgpSnmpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 1, 100, 6, 21, 106, 1, 1),
    _VrIpBgpSnmpOperStatus_Type()
)
vrIpBgpSnmpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vrIpBgpSnmpOperStatus.setStatus("mandatory")
_BgpMIB_ObjectIdentity = ObjectIdentity
bgpMIB = _BgpMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 141)
)
_BgpGroup_ObjectIdentity = ObjectIdentity
bgpGroup = _BgpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 141, 1)
)
_BgpGroupBE_ObjectIdentity = ObjectIdentity
bgpGroupBE = _BgpGroupBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 141, 1, 5)
)
_BgpGroupBE01_ObjectIdentity = ObjectIdentity
bgpGroupBE01 = _BgpGroupBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 141, 1, 5, 2)
)
_BgpGroupBE01A_ObjectIdentity = ObjectIdentity
bgpGroupBE01A = _BgpGroupBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 141, 1, 5, 2, 2)
)
_BgpCapabilities_ObjectIdentity = ObjectIdentity
bgpCapabilities = _BgpCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 141, 3)
)
_BgpCapabilitiesBE_ObjectIdentity = ObjectIdentity
bgpCapabilitiesBE = _BgpCapabilitiesBE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 141, 3, 5)
)
_BgpCapabilitiesBE01_ObjectIdentity = ObjectIdentity
bgpCapabilitiesBE01 = _BgpCapabilitiesBE01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 141, 3, 5, 2)
)
_BgpCapabilitiesBE01A_ObjectIdentity = ObjectIdentity
bgpCapabilitiesBE01A = _BgpCapabilitiesBE01A_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 2, 4, 2, 141, 3, 5, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Nortel-Magellan-Passport-BgpMIB",
    **{"vrIpBgp": vrIpBgp,
       "vrIpBgpRowStatusTable": vrIpBgpRowStatusTable,
       "vrIpBgpRowStatusEntry": vrIpBgpRowStatusEntry,
       "vrIpBgpRowStatus": vrIpBgpRowStatus,
       "vrIpBgpComponentName": vrIpBgpComponentName,
       "vrIpBgpStorageType": vrIpBgpStorageType,
       "vrIpBgpIndex": vrIpBgpIndex,
       "vrIpBgpPeer": vrIpBgpPeer,
       "vrIpBgpPeerRowStatusTable": vrIpBgpPeerRowStatusTable,
       "vrIpBgpPeerRowStatusEntry": vrIpBgpPeerRowStatusEntry,
       "vrIpBgpPeerRowStatus": vrIpBgpPeerRowStatus,
       "vrIpBgpPeerComponentName": vrIpBgpPeerComponentName,
       "vrIpBgpPeerStorageType": vrIpBgpPeerStorageType,
       "vrIpBgpPeerPeerAddressIndex": vrIpBgpPeerPeerAddressIndex,
       "vrIpBgpPeerProvTable": vrIpBgpPeerProvTable,
       "vrIpBgpPeerProvEntry": vrIpBgpPeerProvEntry,
       "vrIpBgpPeerPeerAs": vrIpBgpPeerPeerAs,
       "vrIpBgpPeerLocalAddressConfigured": vrIpBgpPeerLocalAddressConfigured,
       "vrIpBgpPeerKeepAliveConfigured": vrIpBgpPeerKeepAliveConfigured,
       "vrIpBgpPeerHoldTimeConfigured": vrIpBgpPeerHoldTimeConfigured,
       "vrIpBgpPeerConnectRetryTime": vrIpBgpPeerConnectRetryTime,
       "vrIpBgpPeerMinAsOrigTime": vrIpBgpPeerMinAsOrigTime,
       "vrIpBgpPeerMinRouteAdvTime": vrIpBgpPeerMinRouteAdvTime,
       "vrIpBgpPeerDefaultInAggMed": vrIpBgpPeerDefaultInAggMed,
       "vrIpBgpPeerIsRouteReflectorClient": vrIpBgpPeerIsRouteReflectorClient,
       "vrIpBgpPeerStateTable": vrIpBgpPeerStateTable,
       "vrIpBgpPeerStateEntry": vrIpBgpPeerStateEntry,
       "vrIpBgpPeerAdminState": vrIpBgpPeerAdminState,
       "vrIpBgpPeerOperationalState": vrIpBgpPeerOperationalState,
       "vrIpBgpPeerUsageState": vrIpBgpPeerUsageState,
       "vrIpBgpPeerOperTable": vrIpBgpPeerOperTable,
       "vrIpBgpPeerOperEntry": vrIpBgpPeerOperEntry,
       "vrIpBgpPeerConnectionState": vrIpBgpPeerConnectionState,
       "vrIpBgpPeerBgpIdentifier": vrIpBgpPeerBgpIdentifier,
       "vrIpBgpPeerVersionNegotiated": vrIpBgpPeerVersionNegotiated,
       "vrIpBgpPeerHoldTimeNegotiated": vrIpBgpPeerHoldTimeNegotiated,
       "vrIpBgpPeerKeepAliveNegotiated": vrIpBgpPeerKeepAliveNegotiated,
       "vrIpBgpPeerLocalAddressUsed": vrIpBgpPeerLocalAddressUsed,
       "vrIpBgpPeerLocalPort": vrIpBgpPeerLocalPort,
       "vrIpBgpPeerRemotePort": vrIpBgpPeerRemotePort,
       "vrIpBgpPeerLastError": vrIpBgpPeerLastError,
       "vrIpBgpPeerConnectionEstablishedTime": vrIpBgpPeerConnectionEstablishedTime,
       "vrIpBgpPeerConnectionEstablishedTransitions": vrIpBgpPeerConnectionEstablishedTransitions,
       "vrIpBgpPeerInUpdateElapsedTime": vrIpBgpPeerInUpdateElapsedTime,
       "vrIpBgpPeerInMsgs": vrIpBgpPeerInMsgs,
       "vrIpBgpPeerInUpdates": vrIpBgpPeerInUpdates,
       "vrIpBgpPeerInErrors": vrIpBgpPeerInErrors,
       "vrIpBgpPeerInErrorMsgs": vrIpBgpPeerInErrorMsgs,
       "vrIpBgpPeerOutMsgs": vrIpBgpPeerOutMsgs,
       "vrIpBgpPeerOutUpdates": vrIpBgpPeerOutUpdates,
       "vrIpBgpPeerOutDiscards": vrIpBgpPeerOutDiscards,
       "vrIpBgpPeerOutErrorMsgs": vrIpBgpPeerOutErrorMsgs,
       "vrIpBgpPeerInRoutes": vrIpBgpPeerInRoutes,
       "vrIpBgpImport": vrIpBgpImport,
       "vrIpBgpImportRowStatusTable": vrIpBgpImportRowStatusTable,
       "vrIpBgpImportRowStatusEntry": vrIpBgpImportRowStatusEntry,
       "vrIpBgpImportRowStatus": vrIpBgpImportRowStatus,
       "vrIpBgpImportComponentName": vrIpBgpImportComponentName,
       "vrIpBgpImportStorageType": vrIpBgpImportStorageType,
       "vrIpBgpImportIndex": vrIpBgpImportIndex,
       "vrIpBgpImportNet": vrIpBgpImportNet,
       "vrIpBgpImportNetRowStatusTable": vrIpBgpImportNetRowStatusTable,
       "vrIpBgpImportNetRowStatusEntry": vrIpBgpImportNetRowStatusEntry,
       "vrIpBgpImportNetRowStatus": vrIpBgpImportNetRowStatus,
       "vrIpBgpImportNetComponentName": vrIpBgpImportNetComponentName,
       "vrIpBgpImportNetStorageType": vrIpBgpImportNetStorageType,
       "vrIpBgpImportNetIndex": vrIpBgpImportNetIndex,
       "vrIpBgpImportNetProvTable": vrIpBgpImportNetProvTable,
       "vrIpBgpImportNetProvEntry": vrIpBgpImportNetProvEntry,
       "vrIpBgpImportNetPrefix": vrIpBgpImportNetPrefix,
       "vrIpBgpImportNetLength": vrIpBgpImportNetLength,
       "vrIpBgpImportProvTable": vrIpBgpImportProvTable,
       "vrIpBgpImportProvEntry": vrIpBgpImportProvEntry,
       "vrIpBgpImportPeerAs": vrIpBgpImportPeerAs,
       "vrIpBgpImportPeerIpAddress": vrIpBgpImportPeerIpAddress,
       "vrIpBgpImportOriginAs": vrIpBgpImportOriginAs,
       "vrIpBgpImportOriginProtocol": vrIpBgpImportOriginProtocol,
       "vrIpBgpImportUsageFlag": vrIpBgpImportUsageFlag,
       "vrIpBgpImportLocalPreference": vrIpBgpImportLocalPreference,
       "vrIpBgpImportPreferredOver": vrIpBgpImportPreferredOver,
       "vrIpBgpImportAsPathExpression": vrIpBgpImportAsPathExpression,
       "vrIpBgpImportCommunityExpression": vrIpBgpImportCommunityExpression,
       "vrIpBgpImportExpressPreference": vrIpBgpImportExpressPreference,
       "vrIpBgpImportAppendCommunity": vrIpBgpImportAppendCommunity,
       "vrIpBgpExport": vrIpBgpExport,
       "vrIpBgpExportRowStatusTable": vrIpBgpExportRowStatusTable,
       "vrIpBgpExportRowStatusEntry": vrIpBgpExportRowStatusEntry,
       "vrIpBgpExportRowStatus": vrIpBgpExportRowStatus,
       "vrIpBgpExportComponentName": vrIpBgpExportComponentName,
       "vrIpBgpExportStorageType": vrIpBgpExportStorageType,
       "vrIpBgpExportIndex": vrIpBgpExportIndex,
       "vrIpBgpExportNet": vrIpBgpExportNet,
       "vrIpBgpExportNetRowStatusTable": vrIpBgpExportNetRowStatusTable,
       "vrIpBgpExportNetRowStatusEntry": vrIpBgpExportNetRowStatusEntry,
       "vrIpBgpExportNetRowStatus": vrIpBgpExportNetRowStatus,
       "vrIpBgpExportNetComponentName": vrIpBgpExportNetComponentName,
       "vrIpBgpExportNetStorageType": vrIpBgpExportNetStorageType,
       "vrIpBgpExportNetIndex": vrIpBgpExportNetIndex,
       "vrIpBgpExportNetProvTable": vrIpBgpExportNetProvTable,
       "vrIpBgpExportNetProvEntry": vrIpBgpExportNetProvEntry,
       "vrIpBgpExportNetPrefix": vrIpBgpExportNetPrefix,
       "vrIpBgpExportNetLength": vrIpBgpExportNetLength,
       "vrIpBgpExportProvTable": vrIpBgpExportProvTable,
       "vrIpBgpExportProvEntry": vrIpBgpExportProvEntry,
       "vrIpBgpExportPeerAs": vrIpBgpExportPeerAs,
       "vrIpBgpExportPeerIpAddress": vrIpBgpExportPeerIpAddress,
       "vrIpBgpExportProtocol": vrIpBgpExportProtocol,
       "vrIpBgpExportEgpAsId": vrIpBgpExportEgpAsId,
       "vrIpBgpExportBgpAsId": vrIpBgpExportBgpAsId,
       "vrIpBgpExportOspfTag": vrIpBgpExportOspfTag,
       "vrIpBgpExportRipInterface": vrIpBgpExportRipInterface,
       "vrIpBgpExportRipNeighbor": vrIpBgpExportRipNeighbor,
       "vrIpBgpExportAdvertiseStatus": vrIpBgpExportAdvertiseStatus,
       "vrIpBgpExportMultiExitDisc": vrIpBgpExportMultiExitDisc,
       "vrIpBgpExportSendMultiExitDiscToEbgp": vrIpBgpExportSendMultiExitDiscToEbgp,
       "vrIpBgpExportAsPathExpression": vrIpBgpExportAsPathExpression,
       "vrIpBgpExportCommunityExpression": vrIpBgpExportCommunityExpression,
       "vrIpBgpExportExpressPreference": vrIpBgpExportExpressPreference,
       "vrIpBgpExportSendCommunity": vrIpBgpExportSendCommunity,
       "vrIpBgpExportInsertDummyAs": vrIpBgpExportInsertDummyAs,
       "vrIpBgpAs": vrIpBgpAs,
       "vrIpBgpAsRowStatusTable": vrIpBgpAsRowStatusTable,
       "vrIpBgpAsRowStatusEntry": vrIpBgpAsRowStatusEntry,
       "vrIpBgpAsRowStatus": vrIpBgpAsRowStatus,
       "vrIpBgpAsComponentName": vrIpBgpAsComponentName,
       "vrIpBgpAsStorageType": vrIpBgpAsStorageType,
       "vrIpBgpAsIndex": vrIpBgpAsIndex,
       "vrIpBgpAsProvTable": vrIpBgpAsProvTable,
       "vrIpBgpAsProvEntry": vrIpBgpAsProvEntry,
       "vrIpBgpAsWeight": vrIpBgpAsWeight,
       "vrIpBgpAggregate": vrIpBgpAggregate,
       "vrIpBgpAggregateRowStatusTable": vrIpBgpAggregateRowStatusTable,
       "vrIpBgpAggregateRowStatusEntry": vrIpBgpAggregateRowStatusEntry,
       "vrIpBgpAggregateRowStatus": vrIpBgpAggregateRowStatus,
       "vrIpBgpAggregateComponentName": vrIpBgpAggregateComponentName,
       "vrIpBgpAggregateStorageType": vrIpBgpAggregateStorageType,
       "vrIpBgpAggregatePrefixIndex": vrIpBgpAggregatePrefixIndex,
       "vrIpBgpAggregateLengthIndex": vrIpBgpAggregateLengthIndex,
       "vrIpBgpAggregateNet": vrIpBgpAggregateNet,
       "vrIpBgpAggregateNetRowStatusTable": vrIpBgpAggregateNetRowStatusTable,
       "vrIpBgpAggregateNetRowStatusEntry": vrIpBgpAggregateNetRowStatusEntry,
       "vrIpBgpAggregateNetRowStatus": vrIpBgpAggregateNetRowStatus,
       "vrIpBgpAggregateNetComponentName": vrIpBgpAggregateNetComponentName,
       "vrIpBgpAggregateNetStorageType": vrIpBgpAggregateNetStorageType,
       "vrIpBgpAggregateNetIndex": vrIpBgpAggregateNetIndex,
       "vrIpBgpAggregateNetProvTable": vrIpBgpAggregateNetProvTable,
       "vrIpBgpAggregateNetProvEntry": vrIpBgpAggregateNetProvEntry,
       "vrIpBgpAggregateNetPrefix": vrIpBgpAggregateNetPrefix,
       "vrIpBgpAggregateNetLength": vrIpBgpAggregateNetLength,
       "vrIpBgpAggregateNetProtocol": vrIpBgpAggregateNetProtocol,
       "vrIpBgpAggregateNetEgpAsId": vrIpBgpAggregateNetEgpAsId,
       "vrIpBgpAggregateNetBgpAsId": vrIpBgpAggregateNetBgpAsId,
       "vrIpBgpAggregateNetOspfTag": vrIpBgpAggregateNetOspfTag,
       "vrIpBgpAggregateNetRipInterface": vrIpBgpAggregateNetRipInterface,
       "vrIpBgpAggregateNetAction": vrIpBgpAggregateNetAction,
       "vrIpBgpIndb": vrIpBgpIndb,
       "vrIpBgpIndbRowStatusTable": vrIpBgpIndbRowStatusTable,
       "vrIpBgpIndbRowStatusEntry": vrIpBgpIndbRowStatusEntry,
       "vrIpBgpIndbRowStatus": vrIpBgpIndbRowStatus,
       "vrIpBgpIndbComponentName": vrIpBgpIndbComponentName,
       "vrIpBgpIndbStorageType": vrIpBgpIndbStorageType,
       "vrIpBgpIndbPrefixIndex": vrIpBgpIndbPrefixIndex,
       "vrIpBgpIndbLengthIndex": vrIpBgpIndbLengthIndex,
       "vrIpBgpIndbPeerIndex": vrIpBgpIndbPeerIndex,
       "vrIpBgpIndbOperTable": vrIpBgpIndbOperTable,
       "vrIpBgpIndbOperEntry": vrIpBgpIndbOperEntry,
       "vrIpBgpIndbOrigin": vrIpBgpIndbOrigin,
       "vrIpBgpIndbInLocaldb": vrIpBgpIndbInLocaldb,
       "vrIpBgpIndbNextHop": vrIpBgpIndbNextHop,
       "vrIpBgpIndbLocalPreference": vrIpBgpIndbLocalPreference,
       "vrIpBgpIndbCalcLocalPref": vrIpBgpIndbCalcLocalPref,
       "vrIpBgpIndbMultiExitDiscriminator": vrIpBgpIndbMultiExitDiscriminator,
       "vrIpBgpIndbAtomicAggregate": vrIpBgpIndbAtomicAggregate,
       "vrIpBgpIndbAggregatorAs": vrIpBgpIndbAggregatorAs,
       "vrIpBgpIndbAggregatorAddr": vrIpBgpIndbAggregatorAddr,
       "vrIpBgpIndbAsPath": vrIpBgpIndbAsPath,
       "vrIpBgpIndbUnknownAttributes": vrIpBgpIndbUnknownAttributes,
       "vrIpBgpIndbCommunityPath": vrIpBgpIndbCommunityPath,
       "vrIpBgpIndbAsOriginatorId": vrIpBgpIndbAsOriginatorId,
       "vrIpBgpIndbRrClusterListTable": vrIpBgpIndbRrClusterListTable,
       "vrIpBgpIndbRrClusterListEntry": vrIpBgpIndbRrClusterListEntry,
       "vrIpBgpIndbRrClusterListValue": vrIpBgpIndbRrClusterListValue,
       "vrIpBgpLocaldb": vrIpBgpLocaldb,
       "vrIpBgpLocaldbRowStatusTable": vrIpBgpLocaldbRowStatusTable,
       "vrIpBgpLocaldbRowStatusEntry": vrIpBgpLocaldbRowStatusEntry,
       "vrIpBgpLocaldbRowStatus": vrIpBgpLocaldbRowStatus,
       "vrIpBgpLocaldbComponentName": vrIpBgpLocaldbComponentName,
       "vrIpBgpLocaldbStorageType": vrIpBgpLocaldbStorageType,
       "vrIpBgpLocaldbPrefixIndex": vrIpBgpLocaldbPrefixIndex,
       "vrIpBgpLocaldbLengthIndex": vrIpBgpLocaldbLengthIndex,
       "vrIpBgpLocaldbPeerIndex": vrIpBgpLocaldbPeerIndex,
       "vrIpBgpLocaldbOperTable": vrIpBgpLocaldbOperTable,
       "vrIpBgpLocaldbOperEntry": vrIpBgpLocaldbOperEntry,
       "vrIpBgpLocaldbOrigin": vrIpBgpLocaldbOrigin,
       "vrIpBgpLocaldbNextHop": vrIpBgpLocaldbNextHop,
       "vrIpBgpLocaldbLocalPreference": vrIpBgpLocaldbLocalPreference,
       "vrIpBgpLocaldbMultiExitDiscriminator": vrIpBgpLocaldbMultiExitDiscriminator,
       "vrIpBgpLocaldbAtomicAggregate": vrIpBgpLocaldbAtomicAggregate,
       "vrIpBgpLocaldbAggregatorAs": vrIpBgpLocaldbAggregatorAs,
       "vrIpBgpLocaldbAggregatorAddr": vrIpBgpLocaldbAggregatorAddr,
       "vrIpBgpLocaldbAsPath": vrIpBgpLocaldbAsPath,
       "vrIpBgpLocaldbUnknownAttributes": vrIpBgpLocaldbUnknownAttributes,
       "vrIpBgpLocaldbCommunityPath": vrIpBgpLocaldbCommunityPath,
       "vrIpBgpLocaldbAsOriginatorId": vrIpBgpLocaldbAsOriginatorId,
       "vrIpBgpLocaldbRrClusterListTable": vrIpBgpLocaldbRrClusterListTable,
       "vrIpBgpLocaldbRrClusterListEntry": vrIpBgpLocaldbRrClusterListEntry,
       "vrIpBgpLocaldbRrClusterListValue": vrIpBgpLocaldbRrClusterListValue,
       "vrIpBgpOutdb": vrIpBgpOutdb,
       "vrIpBgpOutdbRowStatusTable": vrIpBgpOutdbRowStatusTable,
       "vrIpBgpOutdbRowStatusEntry": vrIpBgpOutdbRowStatusEntry,
       "vrIpBgpOutdbRowStatus": vrIpBgpOutdbRowStatus,
       "vrIpBgpOutdbComponentName": vrIpBgpOutdbComponentName,
       "vrIpBgpOutdbStorageType": vrIpBgpOutdbStorageType,
       "vrIpBgpOutdbPrefixIndex": vrIpBgpOutdbPrefixIndex,
       "vrIpBgpOutdbLengthIndex": vrIpBgpOutdbLengthIndex,
       "vrIpBgpOutdbPeerIndex": vrIpBgpOutdbPeerIndex,
       "vrIpBgpOutdbOperTable": vrIpBgpOutdbOperTable,
       "vrIpBgpOutdbOperEntry": vrIpBgpOutdbOperEntry,
       "vrIpBgpOutdbOrigin": vrIpBgpOutdbOrigin,
       "vrIpBgpOutdbNextHop": vrIpBgpOutdbNextHop,
       "vrIpBgpOutdbLocalPreference": vrIpBgpOutdbLocalPreference,
       "vrIpBgpOutdbMultiExitDiscriminator": vrIpBgpOutdbMultiExitDiscriminator,
       "vrIpBgpOutdbAtomicAggregate": vrIpBgpOutdbAtomicAggregate,
       "vrIpBgpOutdbAggregatorAs": vrIpBgpOutdbAggregatorAs,
       "vrIpBgpOutdbAggregatorAddr": vrIpBgpOutdbAggregatorAddr,
       "vrIpBgpOutdbAsPath": vrIpBgpOutdbAsPath,
       "vrIpBgpOutdbUnknownAttributes": vrIpBgpOutdbUnknownAttributes,
       "vrIpBgpOutdbCommunityPath": vrIpBgpOutdbCommunityPath,
       "vrIpBgpOutdbAsOriginatorId": vrIpBgpOutdbAsOriginatorId,
       "vrIpBgpOutdbRrClusterListTable": vrIpBgpOutdbRrClusterListTable,
       "vrIpBgpOutdbRrClusterListEntry": vrIpBgpOutdbRrClusterListEntry,
       "vrIpBgpOutdbRrClusterListValue": vrIpBgpOutdbRrClusterListValue,
       "vrIpBgpProvTable": vrIpBgpProvTable,
       "vrIpBgpProvEntry": vrIpBgpProvEntry,
       "vrIpBgpBgpIdentifier": vrIpBgpBgpIdentifier,
       "vrIpBgpLocalAs": vrIpBgpLocalAs,
       "vrIpBgpDefaultLocalPreference": vrIpBgpDefaultLocalPreference,
       "vrIpBgpDefaultMultiExitDisc": vrIpBgpDefaultMultiExitDisc,
       "vrIpBgpRouteThrottleLimit": vrIpBgpRouteThrottleLimit,
       "vrIpBgpRouteThrottleInter": vrIpBgpRouteThrottleInter,
       "vrIpBgpRouteReflector": vrIpBgpRouteReflector,
       "vrIpBgpRouteReflectorCluster": vrIpBgpRouteReflectorCluster,
       "vrIpBgpOperTable": vrIpBgpOperTable,
       "vrIpBgpOperEntry": vrIpBgpOperEntry,
       "vrIpBgpTableVersion": vrIpBgpTableVersion,
       "vrIpBgpInMsgs": vrIpBgpInMsgs,
       "vrIpBgpInErrors": vrIpBgpInErrors,
       "vrIpBgpInErrorMsgs": vrIpBgpInErrorMsgs,
       "vrIpBgpOutMsgs": vrIpBgpOutMsgs,
       "vrIpBgpOutDiscards": vrIpBgpOutDiscards,
       "vrIpBgpOutErrorMsgs": vrIpBgpOutErrorMsgs,
       "vrIpBgpIndbSize": vrIpBgpIndbSize,
       "vrIpBgpStateTable": vrIpBgpStateTable,
       "vrIpBgpStateEntry": vrIpBgpStateEntry,
       "vrIpBgpAdminState": vrIpBgpAdminState,
       "vrIpBgpOperationalState": vrIpBgpOperationalState,
       "vrIpBgpUsageState": vrIpBgpUsageState,
       "vrIpBgpAdminControlTable": vrIpBgpAdminControlTable,
       "vrIpBgpAdminControlEntry": vrIpBgpAdminControlEntry,
       "vrIpBgpSnmpAdminStatus": vrIpBgpSnmpAdminStatus,
       "vrIpBgpOperStatusTable": vrIpBgpOperStatusTable,
       "vrIpBgpOperStatusEntry": vrIpBgpOperStatusEntry,
       "vrIpBgpSnmpOperStatus": vrIpBgpSnmpOperStatus,
       "bgpMIB": bgpMIB,
       "bgpGroup": bgpGroup,
       "bgpGroupBE": bgpGroupBE,
       "bgpGroupBE01": bgpGroupBE01,
       "bgpGroupBE01A": bgpGroupBE01A,
       "bgpCapabilities": bgpCapabilities,
       "bgpCapabilitiesBE": bgpCapabilitiesBE,
       "bgpCapabilitiesBE01": bgpCapabilitiesBE01,
       "bgpCapabilitiesBE01A": bgpCapabilitiesBE01A}
)
