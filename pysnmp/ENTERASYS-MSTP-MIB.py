# SNMP MIB module (ENTERASYS-MSTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ENTERASYS-MSTP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:39:14 2024
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

(BridgeId,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "BridgeId")

(etsysModules,) = mibBuilder.importSymbols(
    "ENTERASYS-MIB-NAMES",
    "etsysModules")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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

(DisplayString,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

etsysMstpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28)
)
etsysMstpMIB.setRevisions(
        ("2006-11-09 16:40",
         "2006-10-04 19:54",
         "2004-07-14 16:25",
         "2004-04-08 19:59",
         "2004-02-12 21:38",
         "2003-01-21 14:27",
         "2002-10-11 17:05")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HexString(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )



# MIB Managed Objects in the order of their OIDs

_EtsysMstpObjects_ObjectIdentity = ObjectIdentity
etsysMstpObjects = _EtsysMstpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1)
)
_EtsysMstpNotifications_ObjectIdentity = ObjectIdentity
etsysMstpNotifications = _EtsysMstpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 0)
)
_EtsysMstpConfig_ObjectIdentity = ObjectIdentity
etsysMstpConfig = _EtsysMstpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 1)
)


class _EtsysMstpMaxMstId_Type(Unsigned32):
    """Custom type etsysMstpMaxMstId based on Unsigned32"""
    defaultValue = 4094


_EtsysMstpMaxMstId_Object = MibScalar
etsysMstpMaxMstId = _EtsysMstpMaxMstId_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 1, 1),
    _EtsysMstpMaxMstId_Type()
)
etsysMstpMaxMstId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMstpMaxMstId.setStatus("current")


class _EtsysMstpMaxSupportedMsts_Type(Unsigned32):
    """Custom type etsysMstpMaxSupportedMsts based on Unsigned32"""
    defaultValue = 64


_EtsysMstpMaxSupportedMsts_Object = MibScalar
etsysMstpMaxSupportedMsts = _EtsysMstpMaxSupportedMsts_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 1, 2),
    _EtsysMstpMaxSupportedMsts_Type()
)
etsysMstpMaxSupportedMsts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMstpMaxSupportedMsts.setStatus("current")
_EtsysMstpNumMsts_Type = Unsigned32
_EtsysMstpNumMsts_Object = MibScalar
etsysMstpNumMsts = _EtsysMstpNumMsts_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 1, 3),
    _EtsysMstpNumMsts_Type()
)
etsysMstpNumMsts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMstpNumMsts.setStatus("current")
_EtsysMstpMstiTable_Object = MibTable
etsysMstpMstiTable = _EtsysMstpMstiTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 1, 4)
)
if mibBuilder.loadTexts:
    etsysMstpMstiTable.setStatus("current")
_EtsysMstpMstiEntry_Object = MibTableRow
etsysMstpMstiEntry = _EtsysMstpMstiEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 1, 4, 1)
)
etsysMstpMstiEntry.setIndexNames(
    (0, "ENTERASYS-MSTP-MIB", "etsysMstpMstId"),
)
if mibBuilder.loadTexts:
    etsysMstpMstiEntry.setStatus("current")
_EtsysMstpMstId_Type = Unsigned32
_EtsysMstpMstId_Object = MibTableColumn
etsysMstpMstId = _EtsysMstpMstId_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 1, 4, 1, 1),
    _EtsysMstpMstId_Type()
)
etsysMstpMstId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysMstpMstId.setStatus("current")
_EtsysMstpMstiStatus_Type = RowStatus
_EtsysMstpMstiStatus_Object = MibTableColumn
etsysMstpMstiStatus = _EtsysMstpMstiStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 1, 4, 1, 2),
    _EtsysMstpMstiStatus_Type()
)
etsysMstpMstiStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysMstpMstiStatus.setStatus("current")
_EtsysMstpAllocTable_Object = MibTable
etsysMstpAllocTable = _EtsysMstpAllocTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 1, 5)
)
if mibBuilder.loadTexts:
    etsysMstpAllocTable.setStatus("current")
_EtsysMstpAllocEntry_Object = MibTableRow
etsysMstpAllocEntry = _EtsysMstpAllocEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 1, 5, 1)
)
etsysMstpAllocEntry.setIndexNames(
    (0, "ENTERASYS-MSTP-MIB", "etsysMstpFdbId"),
)
if mibBuilder.loadTexts:
    etsysMstpAllocEntry.setStatus("current")
_EtsysMstpFdbId_Type = Unsigned32
_EtsysMstpFdbId_Object = MibTableColumn
etsysMstpFdbId = _EtsysMstpFdbId_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 1, 5, 1, 1),
    _EtsysMstpFdbId_Type()
)
etsysMstpFdbId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysMstpFdbId.setStatus("current")


class _EtsysMstpMstIdOfFdb_Type(Unsigned32):
    """Custom type etsysMstpMstIdOfFdb based on Unsigned32"""
    defaultValue = 0


_EtsysMstpMstIdOfFdb_Object = MibTableColumn
etsysMstpMstIdOfFdb = _EtsysMstpMstIdOfFdb_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 1, 5, 1, 2),
    _EtsysMstpMstIdOfFdb_Type()
)
etsysMstpMstIdOfFdb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMstpMstIdOfFdb.setStatus("current")
_EtsysMstpConfigTable_Object = MibTable
etsysMstpConfigTable = _EtsysMstpConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 1, 6)
)
if mibBuilder.loadTexts:
    etsysMstpConfigTable.setStatus("current")
_EtsysMstpConfigEntry_Object = MibTableRow
etsysMstpConfigEntry = _EtsysMstpConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 1, 6, 1)
)
etsysMstpConfigEntry.setIndexNames(
    (0, "ENTERASYS-MSTP-MIB", "etsysMstpVlanId"),
)
if mibBuilder.loadTexts:
    etsysMstpConfigEntry.setStatus("current")
_EtsysMstpVlanId_Type = Unsigned32
_EtsysMstpVlanId_Object = MibTableColumn
etsysMstpVlanId = _EtsysMstpVlanId_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 1, 6, 1, 1),
    _EtsysMstpVlanId_Type()
)
etsysMstpVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysMstpVlanId.setStatus("current")
_EtsysMstpMstIdOfVlan_Type = Unsigned32
_EtsysMstpMstIdOfVlan_Object = MibTableColumn
etsysMstpMstIdOfVlan = _EtsysMstpMstIdOfVlan_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 1, 6, 1, 2),
    _EtsysMstpMstIdOfVlan_Type()
)
etsysMstpMstIdOfVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMstpMstIdOfVlan.setStatus("current")
_EtsysMstpFormatSelector_Type = Unsigned32
_EtsysMstpFormatSelector_Object = MibScalar
etsysMstpFormatSelector = _EtsysMstpFormatSelector_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 1, 7),
    _EtsysMstpFormatSelector_Type()
)
etsysMstpFormatSelector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMstpFormatSelector.setStatus("current")


class _EtsysMstpConfigName_Type(SnmpAdminString):
    """Custom type etsysMstpConfigName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EtsysMstpConfigName_Type.__name__ = "SnmpAdminString"
_EtsysMstpConfigName_Object = MibScalar
etsysMstpConfigName = _EtsysMstpConfigName_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 1, 8),
    _EtsysMstpConfigName_Type()
)
etsysMstpConfigName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMstpConfigName.setStatus("current")


class _EtsysMstpRevisionLevel_Type(Unsigned32):
    """Custom type etsysMstpRevisionLevel based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EtsysMstpRevisionLevel_Type.__name__ = "Unsigned32"
_EtsysMstpRevisionLevel_Object = MibScalar
etsysMstpRevisionLevel = _EtsysMstpRevisionLevel_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 1, 9),
    _EtsysMstpRevisionLevel_Type()
)
etsysMstpRevisionLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMstpRevisionLevel.setStatus("current")


class _EtsysMstpConfigDigest_Type(HexString):
    """Custom type etsysMstpConfigDigest based on HexString"""
    subtypeSpec = HexString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_EtsysMstpConfigDigest_Type.__name__ = "HexString"
_EtsysMstpConfigDigest_Object = MibScalar
etsysMstpConfigDigest = _EtsysMstpConfigDigest_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 1, 10),
    _EtsysMstpConfigDigest_Type()
)
etsysMstpConfigDigest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMstpConfigDigest.setStatus("current")


class _EtsysMstpMaxConfigurableMsts_Type(Unsigned32):
    """Custom type etsysMstpMaxConfigurableMsts based on Unsigned32"""
    defaultValue = 64


_EtsysMstpMaxConfigurableMsts_Object = MibScalar
etsysMstpMaxConfigurableMsts = _EtsysMstpMaxConfigurableMsts_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 1, 11),
    _EtsysMstpMaxConfigurableMsts_Type()
)
etsysMstpMaxConfigurableMsts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMstpMaxConfigurableMsts.setStatus("current")
_EtsysMstpBridge_ObjectIdentity = ObjectIdentity
etsysMstpBridge = _EtsysMstpBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 2)
)
_EtsysMstpCistRegionalRootIdentifier_Type = BridgeId
_EtsysMstpCistRegionalRootIdentifier_Object = MibScalar
etsysMstpCistRegionalRootIdentifier = _EtsysMstpCistRegionalRootIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 2, 1),
    _EtsysMstpCistRegionalRootIdentifier_Type()
)
etsysMstpCistRegionalRootIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMstpCistRegionalRootIdentifier.setStatus("current")
_EtsysMstpCistPathCost_Type = Unsigned32
_EtsysMstpCistPathCost_Object = MibScalar
etsysMstpCistPathCost = _EtsysMstpCistPathCost_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 2, 2),
    _EtsysMstpCistPathCost_Type()
)
etsysMstpCistPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMstpCistPathCost.setStatus("current")


class _EtsysMstpMaxHopCount_Type(Unsigned32):
    """Custom type etsysMstpMaxHopCount based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_EtsysMstpMaxHopCount_Type.__name__ = "Unsigned32"
_EtsysMstpMaxHopCount_Object = MibScalar
etsysMstpMaxHopCount = _EtsysMstpMaxHopCount_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 2, 3),
    _EtsysMstpMaxHopCount_Type()
)
etsysMstpMaxHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMstpMaxHopCount.setStatus("current")
_EtsysMstpBridgeTable_Object = MibTable
etsysMstpBridgeTable = _EtsysMstpBridgeTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 2, 4)
)
if mibBuilder.loadTexts:
    etsysMstpBridgeTable.setStatus("current")
_EtsysMstpBridgeEntry_Object = MibTableRow
etsysMstpBridgeEntry = _EtsysMstpBridgeEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 2, 4, 1)
)
etsysMstpBridgeEntry.setIndexNames(
    (0, "ENTERASYS-MSTP-MIB", "etsysMstpMstId"),
)
if mibBuilder.loadTexts:
    etsysMstpBridgeEntry.setStatus("current")


class _EtsysMstpBridgePriority_Type(Unsigned32):
    """Custom type etsysMstpBridgePriority based on Unsigned32"""
    defaultValue = 32768

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_EtsysMstpBridgePriority_Type.__name__ = "Unsigned32"
_EtsysMstpBridgePriority_Object = MibTableColumn
etsysMstpBridgePriority = _EtsysMstpBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 2, 4, 1, 1),
    _EtsysMstpBridgePriority_Type()
)
etsysMstpBridgePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMstpBridgePriority.setStatus("current")
_EtsysMstpTimeSinceTopologyChange_Type = TimeTicks
_EtsysMstpTimeSinceTopologyChange_Object = MibTableColumn
etsysMstpTimeSinceTopologyChange = _EtsysMstpTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 2, 4, 1, 2),
    _EtsysMstpTimeSinceTopologyChange_Type()
)
etsysMstpTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMstpTimeSinceTopologyChange.setStatus("current")
_EtsysMstpTopologyChangeCount_Type = Counter32
_EtsysMstpTopologyChangeCount_Object = MibTableColumn
etsysMstpTopologyChangeCount = _EtsysMstpTopologyChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 2, 4, 1, 3),
    _EtsysMstpTopologyChangeCount_Type()
)
etsysMstpTopologyChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMstpTopologyChangeCount.setStatus("current")
_EtsysMstpTopologyChangeInProgress_Type = TruthValue
_EtsysMstpTopologyChangeInProgress_Object = MibTableColumn
etsysMstpTopologyChangeInProgress = _EtsysMstpTopologyChangeInProgress_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 2, 4, 1, 4),
    _EtsysMstpTopologyChangeInProgress_Type()
)
etsysMstpTopologyChangeInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMstpTopologyChangeInProgress.setStatus("current")
_EtsysMstpDesignatedRoot_Type = BridgeId
_EtsysMstpDesignatedRoot_Object = MibTableColumn
etsysMstpDesignatedRoot = _EtsysMstpDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 2, 4, 1, 5),
    _EtsysMstpDesignatedRoot_Type()
)
etsysMstpDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMstpDesignatedRoot.setStatus("current")
_EtsysMstpRootPathCost_Type = Unsigned32
_EtsysMstpRootPathCost_Object = MibTableColumn
etsysMstpRootPathCost = _EtsysMstpRootPathCost_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 2, 4, 1, 6),
    _EtsysMstpRootPathCost_Type()
)
etsysMstpRootPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMstpRootPathCost.setStatus("current")
_EtsysMstpRootPort_Type = Unsigned32
_EtsysMstpRootPort_Object = MibTableColumn
etsysMstpRootPort = _EtsysMstpRootPort_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 2, 4, 1, 7),
    _EtsysMstpRootPort_Type()
)
etsysMstpRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMstpRootPort.setStatus("current")
_EtsysMstpPort_ObjectIdentity = ObjectIdentity
etsysMstpPort = _EtsysMstpPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 3)
)
_EtsysMstpPortTable_Object = MibTable
etsysMstpPortTable = _EtsysMstpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 3, 1)
)
if mibBuilder.loadTexts:
    etsysMstpPortTable.setStatus("current")
_EtsysMstpPortEntry_Object = MibTableRow
etsysMstpPortEntry = _EtsysMstpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 3, 1, 1)
)
etsysMstpPortEntry.setIndexNames(
    (0, "ENTERASYS-MSTP-MIB", "etsysMstpMstId"),
    (0, "ENTERASYS-MSTP-MIB", "etsysMstpPortNumber"),
)
if mibBuilder.loadTexts:
    etsysMstpPortEntry.setStatus("current")
_EtsysMstpPortNumber_Type = InterfaceIndex
_EtsysMstpPortNumber_Object = MibTableColumn
etsysMstpPortNumber = _EtsysMstpPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 3, 1, 1, 1),
    _EtsysMstpPortNumber_Type()
)
etsysMstpPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysMstpPortNumber.setStatus("current")


class _EtsysMstpPortPriority_Type(Unsigned32):
    """Custom type etsysMstpPortPriority based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_EtsysMstpPortPriority_Type.__name__ = "Unsigned32"
_EtsysMstpPortPriority_Object = MibTableColumn
etsysMstpPortPriority = _EtsysMstpPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 3, 1, 1, 2),
    _EtsysMstpPortPriority_Type()
)
etsysMstpPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMstpPortPriority.setStatus("current")


class _EtsysMstpPortState_Type(Integer32):
    """Custom type etsysMstpPortState based on Integer32"""
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
        *(("blocking", 2),
          ("broken", 6),
          ("disabled", 1),
          ("forwarding", 5),
          ("learning", 4),
          ("listening", 3))
    )


_EtsysMstpPortState_Type.__name__ = "Integer32"
_EtsysMstpPortState_Object = MibTableColumn
etsysMstpPortState = _EtsysMstpPortState_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 3, 1, 1, 3),
    _EtsysMstpPortState_Type()
)
etsysMstpPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMstpPortState.setStatus("current")


class _EtsysMstpPortAdminPathCost_Type(Unsigned32):
    """Custom type etsysMstpPortAdminPathCost based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_EtsysMstpPortAdminPathCost_Type.__name__ = "Unsigned32"
_EtsysMstpPortAdminPathCost_Object = MibTableColumn
etsysMstpPortAdminPathCost = _EtsysMstpPortAdminPathCost_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 3, 1, 1, 4),
    _EtsysMstpPortAdminPathCost_Type()
)
etsysMstpPortAdminPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMstpPortAdminPathCost.setStatus("current")
_EtsysMstpPortOperPathCost_Type = Unsigned32
_EtsysMstpPortOperPathCost_Object = MibTableColumn
etsysMstpPortOperPathCost = _EtsysMstpPortOperPathCost_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 3, 1, 1, 5),
    _EtsysMstpPortOperPathCost_Type()
)
etsysMstpPortOperPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMstpPortOperPathCost.setStatus("current")
_EtsysMstpPortDesignatedRoot_Type = BridgeId
_EtsysMstpPortDesignatedRoot_Object = MibTableColumn
etsysMstpPortDesignatedRoot = _EtsysMstpPortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 3, 1, 1, 6),
    _EtsysMstpPortDesignatedRoot_Type()
)
etsysMstpPortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMstpPortDesignatedRoot.setStatus("current")
_EtsysMstpPortDesignatedCost_Type = Unsigned32
_EtsysMstpPortDesignatedCost_Object = MibTableColumn
etsysMstpPortDesignatedCost = _EtsysMstpPortDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 3, 1, 1, 7),
    _EtsysMstpPortDesignatedCost_Type()
)
etsysMstpPortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMstpPortDesignatedCost.setStatus("current")
_EtsysMstpPortDesignatedBridge_Type = BridgeId
_EtsysMstpPortDesignatedBridge_Object = MibTableColumn
etsysMstpPortDesignatedBridge = _EtsysMstpPortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 3, 1, 1, 8),
    _EtsysMstpPortDesignatedBridge_Type()
)
etsysMstpPortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMstpPortDesignatedBridge.setStatus("current")
_EtsysMstpPortDesignatedPort_Type = OctetString
_EtsysMstpPortDesignatedPort_Object = MibTableColumn
etsysMstpPortDesignatedPort = _EtsysMstpPortDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 3, 1, 1, 9),
    _EtsysMstpPortDesignatedPort_Type()
)
etsysMstpPortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMstpPortDesignatedPort.setStatus("current")


class _EtsysMstpPortRoleValue_Type(Integer32):
    """Custom type etsysMstpPortRoleValue based on Integer32"""
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
        *(("alternate", 4),
          ("backUp", 5),
          ("designated", 3),
          ("disabled", 1),
          ("master", 6),
          ("root", 2))
    )


_EtsysMstpPortRoleValue_Type.__name__ = "Integer32"
_EtsysMstpPortRoleValue_Object = MibTableColumn
etsysMstpPortRoleValue = _EtsysMstpPortRoleValue_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 3, 1, 1, 10),
    _EtsysMstpPortRoleValue_Type()
)
etsysMstpPortRoleValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMstpPortRoleValue.setStatus("current")
_EtsysMstpGlobalPortTable_Object = MibTable
etsysMstpGlobalPortTable = _EtsysMstpGlobalPortTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 3, 2)
)
if mibBuilder.loadTexts:
    etsysMstpGlobalPortTable.setStatus("current")
_EtsysMstpGlobalPortEntry_Object = MibTableRow
etsysMstpGlobalPortEntry = _EtsysMstpGlobalPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 3, 2, 1)
)
etsysMstpGlobalPortEntry.setIndexNames(
    (0, "ENTERASYS-MSTP-MIB", "etsysMstpPortNumber"),
)
if mibBuilder.loadTexts:
    etsysMstpGlobalPortEntry.setStatus("current")
_EtsysMstpHelloTime_Type = Unsigned32
_EtsysMstpHelloTime_Object = MibTableColumn
etsysMstpHelloTime = _EtsysMstpHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 3, 2, 1, 1),
    _EtsysMstpHelloTime_Type()
)
etsysMstpHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMstpHelloTime.setStatus("current")


class _EtsysMstpPortHelloTime_Type(Unsigned32):
    """Custom type etsysMstpPortHelloTime based on Unsigned32"""
    defaultValue = 200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_EtsysMstpPortHelloTime_Type.__name__ = "Unsigned32"
_EtsysMstpPortHelloTime_Object = MibTableColumn
etsysMstpPortHelloTime = _EtsysMstpPortHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 3, 2, 1, 2),
    _EtsysMstpPortHelloTime_Type()
)
etsysMstpPortHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMstpPortHelloTime.setStatus("current")
_EtsysMstpBoundaryPort_Type = TruthValue
_EtsysMstpBoundaryPort_Object = MibTableColumn
etsysMstpBoundaryPort = _EtsysMstpBoundaryPort_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 3, 2, 1, 3),
    _EtsysMstpBoundaryPort_Type()
)
etsysMstpBoundaryPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMstpBoundaryPort.setStatus("current")
_EtsysMstpExtn_ObjectIdentity = ObjectIdentity
etsysMstpExtn = _EtsysMstpExtn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 4)
)


class _EtsysMstpAutoEdgeDetection_Type(EnabledStatus):
    """Custom type etsysMstpAutoEdgeDetection based on EnabledStatus"""


_EtsysMstpAutoEdgeDetection_Object = MibScalar
etsysMstpAutoEdgeDetection = _EtsysMstpAutoEdgeDetection_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 4, 1),
    _EtsysMstpAutoEdgeDetection_Type()
)
etsysMstpAutoEdgeDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMstpAutoEdgeDetection.setStatus("current")


class _EtsysMstpBridgeHelloTimeMode_Type(EnabledStatus):
    """Custom type etsysMstpBridgeHelloTimeMode based on EnabledStatus"""


_EtsysMstpBridgeHelloTimeMode_Object = MibScalar
etsysMstpBridgeHelloTimeMode = _EtsysMstpBridgeHelloTimeMode_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 4, 2),
    _EtsysMstpBridgeHelloTimeMode_Type()
)
etsysMstpBridgeHelloTimeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMstpBridgeHelloTimeMode.setStatus("current")
_EtsysMstpMstiExtnTable_Object = MibTable
etsysMstpMstiExtnTable = _EtsysMstpMstiExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 4, 3)
)
if mibBuilder.loadTexts:
    etsysMstpMstiExtnTable.setStatus("current")
_EtsysMstpMstiExtnEntry_Object = MibTableRow
etsysMstpMstiExtnEntry = _EtsysMstpMstiExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 4, 3, 1)
)
if mibBuilder.loadTexts:
    etsysMstpMstiExtnEntry.setStatus("current")


class _EtsysMstpMstiExtnBackupRootEnable_Type(EnabledStatus):
    """Custom type etsysMstpMstiExtnBackupRootEnable based on EnabledStatus"""


_EtsysMstpMstiExtnBackupRootEnable_Object = MibTableColumn
etsysMstpMstiExtnBackupRootEnable = _EtsysMstpMstiExtnBackupRootEnable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 4, 3, 1, 1),
    _EtsysMstpMstiExtnBackupRootEnable_Type()
)
etsysMstpMstiExtnBackupRootEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMstpMstiExtnBackupRootEnable.setStatus("current")
_EtsysMstpPortExtnTable_Object = MibTable
etsysMstpPortExtnTable = _EtsysMstpPortExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 4, 4)
)
if mibBuilder.loadTexts:
    etsysMstpPortExtnTable.setStatus("current")
_EtsysMstpPortExtnEntry_Object = MibTableRow
etsysMstpPortExtnEntry = _EtsysMstpPortExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 4, 4, 1)
)
if mibBuilder.loadTexts:
    etsysMstpPortExtnEntry.setStatus("current")


class _EtsysMstpPortExtnNonForwardingReason_Type(Integer32):
    """Custom type etsysMstpPortExtnNonForwardingReason based on Integer32"""
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
        *(("disputed", 2),
          ("loopProtectAdvisory", 5),
          ("loopProtectEvent", 4),
          ("loopbackDetected", 6),
          ("none", 1),
          ("spanGuardLocked", 3))
    )


_EtsysMstpPortExtnNonForwardingReason_Type.__name__ = "Integer32"
_EtsysMstpPortExtnNonForwardingReason_Object = MibTableColumn
etsysMstpPortExtnNonForwardingReason = _EtsysMstpPortExtnNonForwardingReason_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 4, 4, 1, 1),
    _EtsysMstpPortExtnNonForwardingReason_Type()
)
etsysMstpPortExtnNonForwardingReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysMstpPortExtnNonForwardingReason.setStatus("current")


class _EtsysMstpPortExtnLoopProtectEnable_Type(EnabledStatus):
    """Custom type etsysMstpPortExtnLoopProtectEnable based on EnabledStatus"""


_EtsysMstpPortExtnLoopProtectEnable_Object = MibTableColumn
etsysMstpPortExtnLoopProtectEnable = _EtsysMstpPortExtnLoopProtectEnable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 4, 4, 1, 2),
    _EtsysMstpPortExtnLoopProtectEnable_Type()
)
etsysMstpPortExtnLoopProtectEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMstpPortExtnLoopProtectEnable.setStatus("current")


class _EtsysMstpPortExtnLoopProtectBlocking_Type(TruthValue):
    """Custom type etsysMstpPortExtnLoopProtectBlocking based on TruthValue"""


_EtsysMstpPortExtnLoopProtectBlocking_Object = MibTableColumn
etsysMstpPortExtnLoopProtectBlocking = _EtsysMstpPortExtnLoopProtectBlocking_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 4, 4, 1, 3),
    _EtsysMstpPortExtnLoopProtectBlocking_Type()
)
etsysMstpPortExtnLoopProtectBlocking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysMstpPortExtnLoopProtectBlocking.setStatus("current")
_EtsysMstpConformance_ObjectIdentity = ObjectIdentity
etsysMstpConformance = _EtsysMstpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 2)
)
_EtsysMstpGroups_ObjectIdentity = ObjectIdentity
etsysMstpGroups = _EtsysMstpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 2, 1)
)
_EtsysMstpCompliances_ObjectIdentity = ObjectIdentity
etsysMstpCompliances = _EtsysMstpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 2, 2)
)
etsysMstpMstiEntry.registerAugmentions(
    ("ENTERASYS-MSTP-MIB",
     "etsysMstpMstiExtnEntry")
)
etsysMstpMstiExtnEntry.setIndexNames(*etsysMstpMstiEntry.getIndexNames())
etsysMstpPortEntry.registerAugmentions(
    ("ENTERASYS-MSTP-MIB",
     "etsysMstpPortExtnEntry")
)
etsysMstpPortExtnEntry.setIndexNames(*etsysMstpPortEntry.getIndexNames())

# Managed Objects groups

etsysMstpConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 2, 1, 1)
)
etsysMstpConfigGroup.setObjects(
      *(("ENTERASYS-MSTP-MIB", "etsysMstpMaxMstId"),
        ("ENTERASYS-MSTP-MIB", "etsysMstpMaxSupportedMsts"),
        ("ENTERASYS-MSTP-MIB", "etsysMstpNumMsts"),
        ("ENTERASYS-MSTP-MIB", "etsysMstpMstiStatus"),
        ("ENTERASYS-MSTP-MIB", "etsysMstpMstIdOfFdb"),
        ("ENTERASYS-MSTP-MIB", "etsysMstpMstIdOfVlan"),
        ("ENTERASYS-MSTP-MIB", "etsysMstpFormatSelector"),
        ("ENTERASYS-MSTP-MIB", "etsysMstpConfigName"),
        ("ENTERASYS-MSTP-MIB", "etsysMstpRevisionLevel"),
        ("ENTERASYS-MSTP-MIB", "etsysMstpConfigDigest"))
)
if mibBuilder.loadTexts:
    etsysMstpConfigGroup.setStatus("current")

etsysMstpBridgeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 2, 1, 2)
)
etsysMstpBridgeGroup.setObjects(
      *(("ENTERASYS-MSTP-MIB", "etsysMstpCistRegionalRootIdentifier"),
        ("ENTERASYS-MSTP-MIB", "etsysMstpCistPathCost"),
        ("ENTERASYS-MSTP-MIB", "etsysMstpMaxHopCount"),
        ("ENTERASYS-MSTP-MIB", "etsysMstpBridgePriority"),
        ("ENTERASYS-MSTP-MIB", "etsysMstpTimeSinceTopologyChange"),
        ("ENTERASYS-MSTP-MIB", "etsysMstpTopologyChangeCount"),
        ("ENTERASYS-MSTP-MIB", "etsysMstpTopologyChangeInProgress"),
        ("ENTERASYS-MSTP-MIB", "etsysMstpDesignatedRoot"),
        ("ENTERASYS-MSTP-MIB", "etsysMstpRootPathCost"),
        ("ENTERASYS-MSTP-MIB", "etsysMstpRootPort"))
)
if mibBuilder.loadTexts:
    etsysMstpBridgeGroup.setStatus("current")

etsysMstpPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 2, 1, 3)
)
etsysMstpPortGroup.setObjects(
      *(("ENTERASYS-MSTP-MIB", "etsysMstpPortPriority"),
        ("ENTERASYS-MSTP-MIB", "etsysMstpPortState"),
        ("ENTERASYS-MSTP-MIB", "etsysMstpPortAdminPathCost"),
        ("ENTERASYS-MSTP-MIB", "etsysMstpPortOperPathCost"),
        ("ENTERASYS-MSTP-MIB", "etsysMstpPortDesignatedRoot"),
        ("ENTERASYS-MSTP-MIB", "etsysMstpPortDesignatedCost"),
        ("ENTERASYS-MSTP-MIB", "etsysMstpPortDesignatedBridge"),
        ("ENTERASYS-MSTP-MIB", "etsysMstpPortDesignatedPort"),
        ("ENTERASYS-MSTP-MIB", "etsysMstpPortRoleValue"),
        ("ENTERASYS-MSTP-MIB", "etsysMstpHelloTime"),
        ("ENTERASYS-MSTP-MIB", "etsysMstpPortHelloTime"),
        ("ENTERASYS-MSTP-MIB", "etsysMstpBoundaryPort"))
)
if mibBuilder.loadTexts:
    etsysMstpPortGroup.setStatus("current")

etsysMstpAutoEdgeDetectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 2, 1, 4)
)
etsysMstpAutoEdgeDetectGroup.setObjects(
    ("ENTERASYS-MSTP-MIB", "etsysMstpAutoEdgeDetection")
)
if mibBuilder.loadTexts:
    etsysMstpAutoEdgeDetectGroup.setStatus("current")

etsysMstpBridgeHelloTimeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 2, 1, 5)
)
etsysMstpBridgeHelloTimeGroup.setObjects(
    ("ENTERASYS-MSTP-MIB", "etsysMstpBridgeHelloTimeMode")
)
if mibBuilder.loadTexts:
    etsysMstpBridgeHelloTimeGroup.setStatus("current")

etsysMstpBackupRootGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 2, 1, 6)
)
etsysMstpBackupRootGroup.setObjects(
    ("ENTERASYS-MSTP-MIB", "etsysMstpMstiExtnBackupRootEnable")
)
if mibBuilder.loadTexts:
    etsysMstpBackupRootGroup.setStatus("current")

etsysMstpMaxInstancesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 2, 1, 7)
)
etsysMstpMaxInstancesGroup.setObjects(
    ("ENTERASYS-MSTP-MIB", "etsysMstpMaxConfigurableMsts")
)
if mibBuilder.loadTexts:
    etsysMstpMaxInstancesGroup.setStatus("current")

etsysMstpNonForwardingReasonGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 2, 1, 8)
)
etsysMstpNonForwardingReasonGroup.setObjects(
    ("ENTERASYS-MSTP-MIB", "etsysMstpPortExtnNonForwardingReason")
)
if mibBuilder.loadTexts:
    etsysMstpNonForwardingReasonGroup.setStatus("current")

etsysMstpLoopProtectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 2, 1, 9)
)
etsysMstpLoopProtectGroup.setObjects(
      *(("ENTERASYS-MSTP-MIB", "etsysMstpPortExtnLoopProtectEnable"),
        ("ENTERASYS-MSTP-MIB", "etsysMstpPortExtnLoopProtectBlocking"))
)
if mibBuilder.loadTexts:
    etsysMstpLoopProtectGroup.setStatus("current")


# Notification objects

etsysMstpLoopProtectEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 1, 0, 1)
)
etsysMstpLoopProtectEvent.setObjects(
      *(("ENTERASYS-MSTP-MIB", "etsysMstpMstId"),
        ("ENTERASYS-MSTP-MIB", "etsysMstpPortNumber"),
        ("ENTERASYS-MSTP-MIB", "etsysMstpPortExtnLoopProtectBlocking"))
)
if mibBuilder.loadTexts:
    etsysMstpLoopProtectEvent.setStatus(
        "current"
    )


# Notifications groups

etsysMstpLoopProtectNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 2, 1, 10)
)
etsysMstpLoopProtectNotificationGroup.setObjects(
    ("ENTERASYS-MSTP-MIB", "etsysMstpLoopProtectEvent")
)
if mibBuilder.loadTexts:
    etsysMstpLoopProtectNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

etsysMstpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 28, 2, 2, 1)
)
if mibBuilder.loadTexts:
    etsysMstpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-MSTP-MIB",
    **{"HexString": HexString,
       "etsysMstpMIB": etsysMstpMIB,
       "etsysMstpObjects": etsysMstpObjects,
       "etsysMstpNotifications": etsysMstpNotifications,
       "etsysMstpLoopProtectEvent": etsysMstpLoopProtectEvent,
       "etsysMstpConfig": etsysMstpConfig,
       "etsysMstpMaxMstId": etsysMstpMaxMstId,
       "etsysMstpMaxSupportedMsts": etsysMstpMaxSupportedMsts,
       "etsysMstpNumMsts": etsysMstpNumMsts,
       "etsysMstpMstiTable": etsysMstpMstiTable,
       "etsysMstpMstiEntry": etsysMstpMstiEntry,
       "etsysMstpMstId": etsysMstpMstId,
       "etsysMstpMstiStatus": etsysMstpMstiStatus,
       "etsysMstpAllocTable": etsysMstpAllocTable,
       "etsysMstpAllocEntry": etsysMstpAllocEntry,
       "etsysMstpFdbId": etsysMstpFdbId,
       "etsysMstpMstIdOfFdb": etsysMstpMstIdOfFdb,
       "etsysMstpConfigTable": etsysMstpConfigTable,
       "etsysMstpConfigEntry": etsysMstpConfigEntry,
       "etsysMstpVlanId": etsysMstpVlanId,
       "etsysMstpMstIdOfVlan": etsysMstpMstIdOfVlan,
       "etsysMstpFormatSelector": etsysMstpFormatSelector,
       "etsysMstpConfigName": etsysMstpConfigName,
       "etsysMstpRevisionLevel": etsysMstpRevisionLevel,
       "etsysMstpConfigDigest": etsysMstpConfigDigest,
       "etsysMstpMaxConfigurableMsts": etsysMstpMaxConfigurableMsts,
       "etsysMstpBridge": etsysMstpBridge,
       "etsysMstpCistRegionalRootIdentifier": etsysMstpCistRegionalRootIdentifier,
       "etsysMstpCistPathCost": etsysMstpCistPathCost,
       "etsysMstpMaxHopCount": etsysMstpMaxHopCount,
       "etsysMstpBridgeTable": etsysMstpBridgeTable,
       "etsysMstpBridgeEntry": etsysMstpBridgeEntry,
       "etsysMstpBridgePriority": etsysMstpBridgePriority,
       "etsysMstpTimeSinceTopologyChange": etsysMstpTimeSinceTopologyChange,
       "etsysMstpTopologyChangeCount": etsysMstpTopologyChangeCount,
       "etsysMstpTopologyChangeInProgress": etsysMstpTopologyChangeInProgress,
       "etsysMstpDesignatedRoot": etsysMstpDesignatedRoot,
       "etsysMstpRootPathCost": etsysMstpRootPathCost,
       "etsysMstpRootPort": etsysMstpRootPort,
       "etsysMstpPort": etsysMstpPort,
       "etsysMstpPortTable": etsysMstpPortTable,
       "etsysMstpPortEntry": etsysMstpPortEntry,
       "etsysMstpPortNumber": etsysMstpPortNumber,
       "etsysMstpPortPriority": etsysMstpPortPriority,
       "etsysMstpPortState": etsysMstpPortState,
       "etsysMstpPortAdminPathCost": etsysMstpPortAdminPathCost,
       "etsysMstpPortOperPathCost": etsysMstpPortOperPathCost,
       "etsysMstpPortDesignatedRoot": etsysMstpPortDesignatedRoot,
       "etsysMstpPortDesignatedCost": etsysMstpPortDesignatedCost,
       "etsysMstpPortDesignatedBridge": etsysMstpPortDesignatedBridge,
       "etsysMstpPortDesignatedPort": etsysMstpPortDesignatedPort,
       "etsysMstpPortRoleValue": etsysMstpPortRoleValue,
       "etsysMstpGlobalPortTable": etsysMstpGlobalPortTable,
       "etsysMstpGlobalPortEntry": etsysMstpGlobalPortEntry,
       "etsysMstpHelloTime": etsysMstpHelloTime,
       "etsysMstpPortHelloTime": etsysMstpPortHelloTime,
       "etsysMstpBoundaryPort": etsysMstpBoundaryPort,
       "etsysMstpExtn": etsysMstpExtn,
       "etsysMstpAutoEdgeDetection": etsysMstpAutoEdgeDetection,
       "etsysMstpBridgeHelloTimeMode": etsysMstpBridgeHelloTimeMode,
       "etsysMstpMstiExtnTable": etsysMstpMstiExtnTable,
       "etsysMstpMstiExtnEntry": etsysMstpMstiExtnEntry,
       "etsysMstpMstiExtnBackupRootEnable": etsysMstpMstiExtnBackupRootEnable,
       "etsysMstpPortExtnTable": etsysMstpPortExtnTable,
       "etsysMstpPortExtnEntry": etsysMstpPortExtnEntry,
       "etsysMstpPortExtnNonForwardingReason": etsysMstpPortExtnNonForwardingReason,
       "etsysMstpPortExtnLoopProtectEnable": etsysMstpPortExtnLoopProtectEnable,
       "etsysMstpPortExtnLoopProtectBlocking": etsysMstpPortExtnLoopProtectBlocking,
       "etsysMstpConformance": etsysMstpConformance,
       "etsysMstpGroups": etsysMstpGroups,
       "etsysMstpConfigGroup": etsysMstpConfigGroup,
       "etsysMstpBridgeGroup": etsysMstpBridgeGroup,
       "etsysMstpPortGroup": etsysMstpPortGroup,
       "etsysMstpAutoEdgeDetectGroup": etsysMstpAutoEdgeDetectGroup,
       "etsysMstpBridgeHelloTimeGroup": etsysMstpBridgeHelloTimeGroup,
       "etsysMstpBackupRootGroup": etsysMstpBackupRootGroup,
       "etsysMstpMaxInstancesGroup": etsysMstpMaxInstancesGroup,
       "etsysMstpNonForwardingReasonGroup": etsysMstpNonForwardingReasonGroup,
       "etsysMstpLoopProtectGroup": etsysMstpLoopProtectGroup,
       "etsysMstpLoopProtectNotificationGroup": etsysMstpLoopProtectNotificationGroup,
       "etsysMstpCompliances": etsysMstpCompliances,
       "etsysMstpCompliance": etsysMstpCompliance}
)
