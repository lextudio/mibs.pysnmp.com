# SNMP MIB module (HUAWEI-MSTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-MSTP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:05:15 2024
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

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

(InterfaceIndex,
 ifIndex,
 ifName) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex",
    "ifName")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hwMstp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HwMSTPEnabledStatus(Integer32, TextualConvention):
    status = "current"
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



# MIB Managed Objects in the order of their OIDs

_HwL2Mgmt_ObjectIdentity = ObjectIdentity
hwL2Mgmt = _HwL2Mgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42)
)
_HwMstpObjects_ObjectIdentity = ObjectIdentity
hwMstpObjects = _HwMstpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1)
)
_HwMstpStatus_Type = HwMSTPEnabledStatus
_HwMstpStatus_Object = MibScalar
hwMstpStatus = _HwMstpStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 1),
    _HwMstpStatus_Type()
)
hwMstpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMstpStatus.setStatus("current")


class _HwMstpForceVersion_Type(Integer32):
    """Custom type hwMstpForceVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mstp", 3),
          ("rstp", 2),
          ("stp", 0))
    )


_HwMstpForceVersion_Type.__name__ = "Integer32"
_HwMstpForceVersion_Object = MibScalar
hwMstpForceVersion = _HwMstpForceVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 2),
    _HwMstpForceVersion_Type()
)
hwMstpForceVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMstpForceVersion.setStatus("current")


class _HwMstpDiameter_Type(Integer32):
    """Custom type hwMstpDiameter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 7),
        ValueRangeConstraint(65535, 65535),
    )


_HwMstpDiameter_Type.__name__ = "Integer32"
_HwMstpDiameter_Object = MibScalar
hwMstpDiameter = _HwMstpDiameter_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 3),
    _HwMstpDiameter_Type()
)
hwMstpDiameter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMstpDiameter.setStatus("current")


class _HwMstpBridgeMaxHops_Type(Integer32):
    """Custom type hwMstpBridgeMaxHops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40),
    )


_HwMstpBridgeMaxHops_Type.__name__ = "Integer32"
_HwMstpBridgeMaxHops_Object = MibScalar
hwMstpBridgeMaxHops = _HwMstpBridgeMaxHops_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 4),
    _HwMstpBridgeMaxHops_Type()
)
hwMstpBridgeMaxHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMstpBridgeMaxHops.setStatus("current")
_HwMstpMasterBridgeID_Type = BridgeId
_HwMstpMasterBridgeID_Object = MibScalar
hwMstpMasterBridgeID = _HwMstpMasterBridgeID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 5),
    _HwMstpMasterBridgeID_Type()
)
hwMstpMasterBridgeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMstpMasterBridgeID.setStatus("current")
_HwMstpMasterPathCost_Type = Integer32
_HwMstpMasterPathCost_Object = MibScalar
hwMstpMasterPathCost = _HwMstpMasterPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 6),
    _HwMstpMasterPathCost_Type()
)
hwMstpMasterPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMstpMasterPathCost.setStatus("current")
_HwMstpBpduGuard_Type = HwMSTPEnabledStatus
_HwMstpBpduGuard_Object = MibScalar
hwMstpBpduGuard = _HwMstpBpduGuard_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 7),
    _HwMstpBpduGuard_Type()
)
hwMstpBpduGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMstpBpduGuard.setStatus("current")
_HwMstpAdminFormatSelector_Type = Integer32
_HwMstpAdminFormatSelector_Object = MibScalar
hwMstpAdminFormatSelector = _HwMstpAdminFormatSelector_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 8),
    _HwMstpAdminFormatSelector_Type()
)
hwMstpAdminFormatSelector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMstpAdminFormatSelector.setStatus("current")


class _HwMstpAdminRegionName_Type(OctetString):
    """Custom type hwMstpAdminRegionName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HwMstpAdminRegionName_Type.__name__ = "OctetString"
_HwMstpAdminRegionName_Object = MibScalar
hwMstpAdminRegionName = _HwMstpAdminRegionName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 9),
    _HwMstpAdminRegionName_Type()
)
hwMstpAdminRegionName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMstpAdminRegionName.setStatus("current")


class _HwMstpAdminRevisionLevel_Type(Integer32):
    """Custom type hwMstpAdminRevisionLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwMstpAdminRevisionLevel_Type.__name__ = "Integer32"
_HwMstpAdminRevisionLevel_Object = MibScalar
hwMstpAdminRevisionLevel = _HwMstpAdminRevisionLevel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 10),
    _HwMstpAdminRevisionLevel_Type()
)
hwMstpAdminRevisionLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMstpAdminRevisionLevel.setStatus("current")
_HwMstpOperFormatSelector_Type = Integer32
_HwMstpOperFormatSelector_Object = MibScalar
hwMstpOperFormatSelector = _HwMstpOperFormatSelector_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 11),
    _HwMstpOperFormatSelector_Type()
)
hwMstpOperFormatSelector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMstpOperFormatSelector.setStatus("current")


class _HwMstpOperRegionName_Type(OctetString):
    """Custom type hwMstpOperRegionName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwMstpOperRegionName_Type.__name__ = "OctetString"
_HwMstpOperRegionName_Object = MibScalar
hwMstpOperRegionName = _HwMstpOperRegionName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 12),
    _HwMstpOperRegionName_Type()
)
hwMstpOperRegionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMstpOperRegionName.setStatus("current")


class _HwMstpOperRevisionLevel_Type(Integer32):
    """Custom type hwMstpOperRevisionLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwMstpOperRevisionLevel_Type.__name__ = "Integer32"
_HwMstpOperRevisionLevel_Object = MibScalar
hwMstpOperRevisionLevel = _HwMstpOperRevisionLevel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 13),
    _HwMstpOperRevisionLevel_Type()
)
hwMstpOperRevisionLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMstpOperRevisionLevel.setStatus("current")


class _HwMstpRegionConfActive_Type(Integer32):
    """Custom type hwMstpRegionConfActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HwMstpRegionConfActive_Type.__name__ = "Integer32"
_HwMstpRegionConfActive_Object = MibScalar
hwMstpRegionConfActive = _HwMstpRegionConfActive_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 14),
    _HwMstpRegionConfActive_Type()
)
hwMstpRegionConfActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMstpRegionConfActive.setStatus("current")


class _HwMstpDefaultVlanAllo_Type(Integer32):
    """Custom type hwMstpDefaultVlanAllo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              65535)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("unused", 65535))
    )


_HwMstpDefaultVlanAllo_Type.__name__ = "Integer32"
_HwMstpDefaultVlanAllo_Object = MibScalar
hwMstpDefaultVlanAllo = _HwMstpDefaultVlanAllo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 15),
    _HwMstpDefaultVlanAllo_Type()
)
hwMstpDefaultVlanAllo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMstpDefaultVlanAllo.setStatus("current")


class _HwMstpDefaultRegionName_Type(Integer32):
    """Custom type hwMstpDefaultRegionName based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              65535)
        )
    )
    namedValues = NamedValues(
        *(("reset", 1),
          ("unused", 65535))
    )


_HwMstpDefaultRegionName_Type.__name__ = "Integer32"
_HwMstpDefaultRegionName_Object = MibScalar
hwMstpDefaultRegionName = _HwMstpDefaultRegionName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 16),
    _HwMstpDefaultRegionName_Type()
)
hwMstpDefaultRegionName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMstpDefaultRegionName.setStatus("current")


class _HwMstpPathCostStandard_Type(Integer32):
    """Custom type hwMstpPathCostStandard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dot1d-1998", 1),
          ("dot1t", 2),
          ("legacy", 3))
    )


_HwMstpPathCostStandard_Type.__name__ = "Integer32"
_HwMstpPathCostStandard_Object = MibScalar
hwMstpPathCostStandard = _HwMstpPathCostStandard_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 17),
    _HwMstpPathCostStandard_Type()
)
hwMstpPathCostStandard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMstpPathCostStandard.setStatus("current")
_HwMstpVIDAllocationTable_Object = MibTable
hwMstpVIDAllocationTable = _HwMstpVIDAllocationTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 18)
)
if mibBuilder.loadTexts:
    hwMstpVIDAllocationTable.setStatus("current")
_HwMstpVIDAllocationEntry_Object = MibTableRow
hwMstpVIDAllocationEntry = _HwMstpVIDAllocationEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 18, 1)
)
hwMstpVIDAllocationEntry.setIndexNames(
    (0, "HUAWEI-MSTP-MIB", "hwMstpVID"),
)
if mibBuilder.loadTexts:
    hwMstpVIDAllocationEntry.setStatus("current")


class _HwMstpVID_Type(Integer32):
    """Custom type hwMstpVID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HwMstpVID_Type.__name__ = "Integer32"
_HwMstpVID_Object = MibTableColumn
hwMstpVID = _HwMstpVID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 18, 1, 1),
    _HwMstpVID_Type()
)
hwMstpVID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMstpVID.setStatus("current")


class _HwMstpAdminMstID_Type(Integer32):
    """Custom type hwMstpAdminMstID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwMstpAdminMstID_Type.__name__ = "Integer32"
_HwMstpAdminMstID_Object = MibTableColumn
hwMstpAdminMstID = _HwMstpAdminMstID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 18, 1, 2),
    _HwMstpAdminMstID_Type()
)
hwMstpAdminMstID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMstpAdminMstID.setStatus("current")


class _HwMstpOperMstID_Type(Integer32):
    """Custom type hwMstpOperMstID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwMstpOperMstID_Type.__name__ = "Integer32"
_HwMstpOperMstID_Object = MibTableColumn
hwMstpOperMstID = _HwMstpOperMstID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 18, 1, 3),
    _HwMstpOperMstID_Type()
)
hwMstpOperMstID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMstpOperMstID.setStatus("current")
_HwMstpInstanceTable_Object = MibTable
hwMstpInstanceTable = _HwMstpInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 19)
)
if mibBuilder.loadTexts:
    hwMstpInstanceTable.setStatus("current")
_HwMstpInstanceEntry_Object = MibTableRow
hwMstpInstanceEntry = _HwMstpInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 19, 1)
)
hwMstpInstanceEntry.setIndexNames(
    (0, "HUAWEI-MSTP-MIB", "hwMstpInstanceID"),
)
if mibBuilder.loadTexts:
    hwMstpInstanceEntry.setStatus("current")


class _HwMstpInstanceID_Type(Integer32):
    """Custom type hwMstpInstanceID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwMstpInstanceID_Type.__name__ = "Integer32"
_HwMstpInstanceID_Object = MibTableColumn
hwMstpInstanceID = _HwMstpInstanceID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 19, 1, 1),
    _HwMstpInstanceID_Type()
)
hwMstpInstanceID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMstpInstanceID.setStatus("current")
_HwMstpiBridgeID_Type = BridgeId
_HwMstpiBridgeID_Object = MibTableColumn
hwMstpiBridgeID = _HwMstpiBridgeID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 19, 1, 2),
    _HwMstpiBridgeID_Type()
)
hwMstpiBridgeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMstpiBridgeID.setStatus("current")


class _HwMstpiBridgePriority_Type(Integer32):
    """Custom type hwMstpiBridgePriority based on Integer32"""
    defaultValue = 32768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_HwMstpiBridgePriority_Type.__name__ = "Integer32"
_HwMstpiBridgePriority_Object = MibTableColumn
hwMstpiBridgePriority = _HwMstpiBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 19, 1, 3),
    _HwMstpiBridgePriority_Type()
)
hwMstpiBridgePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMstpiBridgePriority.setStatus("current")
_HwMstpiDesignedRoot_Type = BridgeId
_HwMstpiDesignedRoot_Object = MibTableColumn
hwMstpiDesignedRoot = _HwMstpiDesignedRoot_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 19, 1, 4),
    _HwMstpiDesignedRoot_Type()
)
hwMstpiDesignedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMstpiDesignedRoot.setStatus("current")
_HwMstpiRootPathCost_Type = Integer32
_HwMstpiRootPathCost_Object = MibTableColumn
hwMstpiRootPathCost = _HwMstpiRootPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 19, 1, 5),
    _HwMstpiRootPathCost_Type()
)
hwMstpiRootPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMstpiRootPathCost.setStatus("current")
_HwMstpiRootPort_Type = Integer32
_HwMstpiRootPort_Object = MibTableColumn
hwMstpiRootPort = _HwMstpiRootPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 19, 1, 6),
    _HwMstpiRootPort_Type()
)
hwMstpiRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMstpiRootPort.setStatus("current")


class _HwMstpiRootType_Type(Integer32):
    """Custom type hwMstpiRootType based on Integer32"""
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
        *(("normal", 0),
          ("primary", 2),
          ("secondary", 1))
    )


_HwMstpiRootType_Type.__name__ = "Integer32"
_HwMstpiRootType_Object = MibTableColumn
hwMstpiRootType = _HwMstpiRootType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 19, 1, 7),
    _HwMstpiRootType_Type()
)
hwMstpiRootType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMstpiRootType.setStatus("current")
_HwMstpiRemainingHops_Type = Integer32
_HwMstpiRemainingHops_Object = MibTableColumn
hwMstpiRemainingHops = _HwMstpiRemainingHops_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 19, 1, 8),
    _HwMstpiRemainingHops_Type()
)
hwMstpiRemainingHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMstpiRemainingHops.setStatus("current")


class _HwMstpiAdminMappedVlanListLow_Type(OctetString):
    """Custom type hwMstpiAdminMappedVlanListLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HwMstpiAdminMappedVlanListLow_Type.__name__ = "OctetString"
_HwMstpiAdminMappedVlanListLow_Object = MibTableColumn
hwMstpiAdminMappedVlanListLow = _HwMstpiAdminMappedVlanListLow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 19, 1, 9),
    _HwMstpiAdminMappedVlanListLow_Type()
)
hwMstpiAdminMappedVlanListLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMstpiAdminMappedVlanListLow.setStatus("current")


class _HwMstpiAdminMappedVlanListHigh_Type(OctetString):
    """Custom type hwMstpiAdminMappedVlanListHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HwMstpiAdminMappedVlanListHigh_Type.__name__ = "OctetString"
_HwMstpiAdminMappedVlanListHigh_Object = MibTableColumn
hwMstpiAdminMappedVlanListHigh = _HwMstpiAdminMappedVlanListHigh_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 19, 1, 10),
    _HwMstpiAdminMappedVlanListHigh_Type()
)
hwMstpiAdminMappedVlanListHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMstpiAdminMappedVlanListHigh.setStatus("current")


class _HwMstpiOperMappedVlanListLow_Type(OctetString):
    """Custom type hwMstpiOperMappedVlanListLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HwMstpiOperMappedVlanListLow_Type.__name__ = "OctetString"
_HwMstpiOperMappedVlanListLow_Object = MibTableColumn
hwMstpiOperMappedVlanListLow = _HwMstpiOperMappedVlanListLow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 19, 1, 11),
    _HwMstpiOperMappedVlanListLow_Type()
)
hwMstpiOperMappedVlanListLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMstpiOperMappedVlanListLow.setStatus("current")


class _HwMstpiOperMappedVlanListHigh_Type(OctetString):
    """Custom type hwMstpiOperMappedVlanListHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HwMstpiOperMappedVlanListHigh_Type.__name__ = "OctetString"
_HwMstpiOperMappedVlanListHigh_Object = MibTableColumn
hwMstpiOperMappedVlanListHigh = _HwMstpiOperMappedVlanListHigh_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 19, 1, 12),
    _HwMstpiOperMappedVlanListHigh_Type()
)
hwMstpiOperMappedVlanListHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMstpiOperMappedVlanListHigh.setStatus("current")
_HwMstpiRowStatus_Type = RowStatus
_HwMstpiRowStatus_Object = MibTableColumn
hwMstpiRowStatus = _HwMstpiRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 19, 1, 13),
    _HwMstpiRowStatus_Type()
)
hwMstpiRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMstpiRowStatus.setStatus("current")
_HwMstpPortTable_Object = MibTable
hwMstpPortTable = _HwMstpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 20)
)
if mibBuilder.loadTexts:
    hwMstpPortTable.setStatus("current")
_HwMstpPortEntry_Object = MibTableRow
hwMstpPortEntry = _HwMstpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 20, 1)
)
hwMstpPortEntry.setIndexNames(
    (0, "HUAWEI-MSTP-MIB", "hwMstpInstanceID"),
    (0, "HUAWEI-MSTP-MIB", "hwMstpiPortIndex"),
)
if mibBuilder.loadTexts:
    hwMstpPortEntry.setStatus("current")
_HwMstpiPortIndex_Type = Integer32
_HwMstpiPortIndex_Object = MibTableColumn
hwMstpiPortIndex = _HwMstpiPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 20, 1, 1),
    _HwMstpiPortIndex_Type()
)
hwMstpiPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMstpiPortIndex.setStatus("current")


class _HwMstpiState_Type(Integer32):
    """Custom type hwMstpiState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("discarding", 2),
          ("forwarding", 5),
          ("learning", 4))
    )


_HwMstpiState_Type.__name__ = "Integer32"
_HwMstpiState_Object = MibTableColumn
hwMstpiState = _HwMstpiState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 20, 1, 2),
    _HwMstpiState_Type()
)
hwMstpiState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMstpiState.setStatus("current")


class _HwMstpiPortPriority_Type(Integer32):
    """Custom type hwMstpiPortPriority based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_HwMstpiPortPriority_Type.__name__ = "Integer32"
_HwMstpiPortPriority_Object = MibTableColumn
hwMstpiPortPriority = _HwMstpiPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 20, 1, 3),
    _HwMstpiPortPriority_Type()
)
hwMstpiPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMstpiPortPriority.setStatus("current")


class _HwMstpiPathCost_Type(Integer32):
    """Custom type hwMstpiPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_HwMstpiPathCost_Type.__name__ = "Integer32"
_HwMstpiPathCost_Object = MibTableColumn
hwMstpiPathCost = _HwMstpiPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 20, 1, 4),
    _HwMstpiPathCost_Type()
)
hwMstpiPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMstpiPathCost.setStatus("current")
_HwMstpiDesignatedRoot_Type = BridgeId
_HwMstpiDesignatedRoot_Object = MibTableColumn
hwMstpiDesignatedRoot = _HwMstpiDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 20, 1, 5),
    _HwMstpiDesignatedRoot_Type()
)
hwMstpiDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMstpiDesignatedRoot.setStatus("current")
_HwMstpiDesignatedCost_Type = Integer32
_HwMstpiDesignatedCost_Object = MibTableColumn
hwMstpiDesignatedCost = _HwMstpiDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 20, 1, 6),
    _HwMstpiDesignatedCost_Type()
)
hwMstpiDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMstpiDesignatedCost.setStatus("current")
_HwMstpiDesignatedBridge_Type = BridgeId
_HwMstpiDesignatedBridge_Object = MibTableColumn
hwMstpiDesignatedBridge = _HwMstpiDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 20, 1, 7),
    _HwMstpiDesignatedBridge_Type()
)
hwMstpiDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMstpiDesignatedBridge.setStatus("current")


class _HwMstpiDesignatedPort_Type(OctetString):
    """Custom type hwMstpiDesignatedPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_HwMstpiDesignatedPort_Type.__name__ = "OctetString"
_HwMstpiDesignatedPort_Object = MibTableColumn
hwMstpiDesignatedPort = _HwMstpiDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 20, 1, 8),
    _HwMstpiDesignatedPort_Type()
)
hwMstpiDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMstpiDesignatedPort.setStatus("current")


class _HwMstpiStpPortEdgeport_Type(Integer32):
    """Custom type hwMstpiStpPortEdgeport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("undo", 3))
    )


_HwMstpiStpPortEdgeport_Type.__name__ = "Integer32"
_HwMstpiStpPortEdgeport_Object = MibTableColumn
hwMstpiStpPortEdgeport = _HwMstpiStpPortEdgeport_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 20, 1, 9),
    _HwMstpiStpPortEdgeport_Type()
)
hwMstpiStpPortEdgeport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMstpiStpPortEdgeport.setStatus("current")


class _HwMstpiStpPortPointToPoint_Type(Integer32):
    """Custom type hwMstpiStpPortPointToPoint based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("forceFalse", 2),
          ("forceTrue", 1))
    )


_HwMstpiStpPortPointToPoint_Type.__name__ = "Integer32"
_HwMstpiStpPortPointToPoint_Object = MibTableColumn
hwMstpiStpPortPointToPoint = _HwMstpiStpPortPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 20, 1, 10),
    _HwMstpiStpPortPointToPoint_Type()
)
hwMstpiStpPortPointToPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMstpiStpPortPointToPoint.setStatus("current")


class _HwMstpiStpMcheck_Type(Integer32):
    """Custom type hwMstpiStpMcheck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              65535)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("unused", 65535))
    )


_HwMstpiStpMcheck_Type.__name__ = "Integer32"
_HwMstpiStpMcheck_Object = MibTableColumn
hwMstpiStpMcheck = _HwMstpiStpMcheck_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 20, 1, 11),
    _HwMstpiStpMcheck_Type()
)
hwMstpiStpMcheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMstpiStpMcheck.setStatus("current")


class _HwMstpiStpTransLimit_Type(Integer32):
    """Custom type hwMstpiStpTransLimit based on Integer32"""
    defaultValue = 147

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwMstpiStpTransLimit_Type.__name__ = "Integer32"
_HwMstpiStpTransLimit_Object = MibTableColumn
hwMstpiStpTransLimit = _HwMstpiStpTransLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 20, 1, 12),
    _HwMstpiStpTransLimit_Type()
)
hwMstpiStpTransLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMstpiStpTransLimit.setStatus("current")
_HwMstpiStpRXStpBPDU_Type = Counter32
_HwMstpiStpRXStpBPDU_Object = MibTableColumn
hwMstpiStpRXStpBPDU = _HwMstpiStpRXStpBPDU_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 20, 1, 13),
    _HwMstpiStpRXStpBPDU_Type()
)
hwMstpiStpRXStpBPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMstpiStpRXStpBPDU.setStatus("current")
_HwMstpiStpTXStpBPDU_Type = Counter32
_HwMstpiStpTXStpBPDU_Object = MibTableColumn
hwMstpiStpTXStpBPDU = _HwMstpiStpTXStpBPDU_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 20, 1, 14),
    _HwMstpiStpTXStpBPDU_Type()
)
hwMstpiStpTXStpBPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMstpiStpTXStpBPDU.setStatus("current")
_HwMstpiStpRXTCNBPDU_Type = Counter32
_HwMstpiStpRXTCNBPDU_Object = MibTableColumn
hwMstpiStpRXTCNBPDU = _HwMstpiStpRXTCNBPDU_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 20, 1, 15),
    _HwMstpiStpRXTCNBPDU_Type()
)
hwMstpiStpRXTCNBPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMstpiStpRXTCNBPDU.setStatus("current")
_HwMstpiStpTXTCNBPDU_Type = Counter32
_HwMstpiStpTXTCNBPDU_Object = MibTableColumn
hwMstpiStpTXTCNBPDU = _HwMstpiStpTXTCNBPDU_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 20, 1, 16),
    _HwMstpiStpTXTCNBPDU_Type()
)
hwMstpiStpTXTCNBPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMstpiStpTXTCNBPDU.setStatus("current")
_HwMstpiStpRXRSTPBPDU_Type = Counter32
_HwMstpiStpRXRSTPBPDU_Object = MibTableColumn
hwMstpiStpRXRSTPBPDU = _HwMstpiStpRXRSTPBPDU_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 20, 1, 17),
    _HwMstpiStpRXRSTPBPDU_Type()
)
hwMstpiStpRXRSTPBPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMstpiStpRXRSTPBPDU.setStatus("current")
_HwMstpiStpTXRSTPBPDU_Type = Counter32
_HwMstpiStpTXRSTPBPDU_Object = MibTableColumn
hwMstpiStpTXRSTPBPDU = _HwMstpiStpTXRSTPBPDU_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 20, 1, 18),
    _HwMstpiStpTXRSTPBPDU_Type()
)
hwMstpiStpTXRSTPBPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMstpiStpTXRSTPBPDU.setStatus("current")
_HwMstpiStpRXMSTPBPDU_Type = Counter32
_HwMstpiStpRXMSTPBPDU_Object = MibTableColumn
hwMstpiStpRXMSTPBPDU = _HwMstpiStpRXMSTPBPDU_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 20, 1, 19),
    _HwMstpiStpRXMSTPBPDU_Type()
)
hwMstpiStpRXMSTPBPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMstpiStpRXMSTPBPDU.setStatus("current")
_HwMstpiStpTXMSTPBPDU_Type = Counter32
_HwMstpiStpTXMSTPBPDU_Object = MibTableColumn
hwMstpiStpTXMSTPBPDU = _HwMstpiStpTXMSTPBPDU_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 20, 1, 20),
    _HwMstpiStpTXMSTPBPDU_Type()
)
hwMstpiStpTXMSTPBPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMstpiStpTXMSTPBPDU.setStatus("current")


class _HwMstpiStpClearStatistics_Type(Integer32):
    """Custom type hwMstpiStpClearStatistics based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              65535)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("unused", 65535))
    )


_HwMstpiStpClearStatistics_Type.__name__ = "Integer32"
_HwMstpiStpClearStatistics_Object = MibTableColumn
hwMstpiStpClearStatistics = _HwMstpiStpClearStatistics_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 20, 1, 21),
    _HwMstpiStpClearStatistics_Type()
)
hwMstpiStpClearStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMstpiStpClearStatistics.setStatus("current")


class _HwMstpiStpDefaultPortCost_Type(Integer32):
    """Custom type hwMstpiStpDefaultPortCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              65535)
        )
    )
    namedValues = NamedValues(
        *(("reset", 1),
          ("unused", 65535))
    )


_HwMstpiStpDefaultPortCost_Type.__name__ = "Integer32"
_HwMstpiStpDefaultPortCost_Object = MibTableColumn
hwMstpiStpDefaultPortCost = _HwMstpiStpDefaultPortCost_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 20, 1, 22),
    _HwMstpiStpDefaultPortCost_Type()
)
hwMstpiStpDefaultPortCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMstpiStpDefaultPortCost.setStatus("current")


class _HwMstpiStpStatus_Type(HwMSTPEnabledStatus):
    """Custom type hwMstpiStpStatus based on HwMSTPEnabledStatus"""


_HwMstpiStpStatus_Object = MibTableColumn
hwMstpiStpStatus = _HwMstpiStpStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 20, 1, 23),
    _HwMstpiStpStatus_Type()
)
hwMstpiStpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMstpiStpStatus.setStatus("current")


class _HwMstpiPortRootGuard_Type(HwMSTPEnabledStatus):
    """Custom type hwMstpiPortRootGuard based on HwMSTPEnabledStatus"""


_HwMstpiPortRootGuard_Object = MibTableColumn
hwMstpiPortRootGuard = _HwMstpiPortRootGuard_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 20, 1, 24),
    _HwMstpiPortRootGuard_Type()
)
hwMstpiPortRootGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMstpiPortRootGuard.setStatus("current")


class _HwMstpiPortLoopGuard_Type(HwMSTPEnabledStatus):
    """Custom type hwMstpiPortLoopGuard based on HwMSTPEnabledStatus"""


_HwMstpiPortLoopGuard_Object = MibTableColumn
hwMstpiPortLoopGuard = _HwMstpiPortLoopGuard_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 20, 1, 25),
    _HwMstpiPortLoopGuard_Type()
)
hwMstpiPortLoopGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMstpiPortLoopGuard.setStatus("current")


class _HwMstpPortCompliance_Type(Integer32):
    """Custom type hwMstpPortCompliance based on Integer32"""
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
        *(("auto", 1),
          ("dotls", 2),
          ("legacy", 3))
    )


_HwMstpPortCompliance_Type.__name__ = "Integer32"
_HwMstpPortCompliance_Object = MibTableColumn
hwMstpPortCompliance = _HwMstpPortCompliance_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 20, 1, 26),
    _HwMstpPortCompliance_Type()
)
hwMstpPortCompliance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMstpPortCompliance.setStatus("current")


class _HwMstpConfigDigestSnooping_Type(HwMSTPEnabledStatus):
    """Custom type hwMstpConfigDigestSnooping based on HwMSTPEnabledStatus"""


_HwMstpConfigDigestSnooping_Object = MibTableColumn
hwMstpConfigDigestSnooping = _HwMstpConfigDigestSnooping_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 20, 1, 27),
    _HwMstpConfigDigestSnooping_Type()
)
hwMstpConfigDigestSnooping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMstpConfigDigestSnooping.setStatus("current")


class _HwMstpNoAgreementCheck_Type(HwMSTPEnabledStatus):
    """Custom type hwMstpNoAgreementCheck based on HwMSTPEnabledStatus"""


_HwMstpNoAgreementCheck_Object = MibTableColumn
hwMstpNoAgreementCheck = _HwMstpNoAgreementCheck_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 20, 1, 30),
    _HwMstpNoAgreementCheck_Type()
)
hwMstpNoAgreementCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMstpNoAgreementCheck.setStatus("current")


class _HwMstpPortTCNotify_Type(HwMSTPEnabledStatus):
    """Custom type hwMstpPortTCNotify based on HwMSTPEnabledStatus"""


_HwMstpPortTCNotify_Object = MibTableColumn
hwMstpPortTCNotify = _HwMstpPortTCNotify_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 20, 1, 31),
    _HwMstpPortTCNotify_Type()
)
hwMstpPortTCNotify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMstpPortTCNotify.setStatus("current")


class _HwMstpiStpPortBpduFilter_Type(Integer32):
    """Custom type hwMstpiStpPortBpduFilter based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("undo", 3))
    )


_HwMstpiStpPortBpduFilter_Type.__name__ = "Integer32"
_HwMstpiStpPortBpduFilter_Object = MibTableColumn
hwMstpiStpPortBpduFilter = _HwMstpiStpPortBpduFilter_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 20, 1, 32),
    _HwMstpiStpPortBpduFilter_Type()
)
hwMstpiStpPortBpduFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMstpiStpPortBpduFilter.setStatus("current")


class _HwMstpiPortRole_Type(Integer32):
    """Custom type hwMstpiPortRole based on Integer32"""
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
        *(("alternate", 2),
          ("backup", 3),
          ("designated", 5),
          ("disabled", 1),
          ("master", 6),
          ("root", 4))
    )


_HwMstpiPortRole_Type.__name__ = "Integer32"
_HwMstpiPortRole_Object = MibTableColumn
hwMstpiPortRole = _HwMstpiPortRole_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 20, 1, 33),
    _HwMstpiPortRole_Type()
)
hwMstpiPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMstpiPortRole.setStatus("current")


class _HwMstpSnooping_Type(Integer32):
    """Custom type hwMstpSnooping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HwMstpSnooping_Type.__name__ = "Integer32"
_HwMstpSnooping_Object = MibScalar
hwMstpSnooping = _HwMstpSnooping_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 21),
    _HwMstpSnooping_Type()
)
hwMstpSnooping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMstpSnooping.setStatus("current")
_HwMstpAccessoryTable_Object = MibTable
hwMstpAccessoryTable = _HwMstpAccessoryTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 22)
)
if mibBuilder.loadTexts:
    hwMstpAccessoryTable.setStatus("current")
_HwMstpAccessoryEntry_Object = MibTableRow
hwMstpAccessoryEntry = _HwMstpAccessoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 22, 1)
)
hwMstpAccessoryEntry.setIndexNames(
    (0, "HUAWEI-MSTP-MIB", "hwMstpAccessoryIndex"),
)
if mibBuilder.loadTexts:
    hwMstpAccessoryEntry.setStatus("current")


class _HwMstpAccessoryIndex_Type(Integer32):
    """Custom type hwMstpAccessoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_HwMstpAccessoryIndex_Type.__name__ = "Integer32"
_HwMstpAccessoryIndex_Object = MibTableColumn
hwMstpAccessoryIndex = _HwMstpAccessoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 22, 1, 1),
    _HwMstpAccessoryIndex_Type()
)
hwMstpAccessoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMstpAccessoryIndex.setStatus("current")


class _HwMstpBackupReplyAgreement_Type(Integer32):
    """Custom type hwMstpBackupReplyAgreement based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HwMstpBackupReplyAgreement_Type.__name__ = "Integer32"
_HwMstpBackupReplyAgreement_Object = MibTableColumn
hwMstpBackupReplyAgreement = _HwMstpBackupReplyAgreement_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 22, 1, 2),
    _HwMstpBackupReplyAgreement_Type()
)
hwMstpBackupReplyAgreement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMstpBackupReplyAgreement.setStatus("current")


class _HwMstpStpNoAgreementCheck_Type(Integer32):
    """Custom type hwMstpStpNoAgreementCheck based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HwMstpStpNoAgreementCheck_Type.__name__ = "Integer32"
_HwMstpStpNoAgreementCheck_Object = MibTableColumn
hwMstpStpNoAgreementCheck = _HwMstpStpNoAgreementCheck_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 22, 1, 3),
    _HwMstpStpNoAgreementCheck_Type()
)
hwMstpStpNoAgreementCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMstpStpNoAgreementCheck.setStatus("current")
_HwMstpProTable_Object = MibTable
hwMstpProTable = _HwMstpProTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 23)
)
if mibBuilder.loadTexts:
    hwMstpProTable.setStatus("current")
_HwMstpProEntry_Object = MibTableRow
hwMstpProEntry = _HwMstpProEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 23, 1)
)
hwMstpProEntry.setIndexNames(
    (0, "HUAWEI-MSTP-MIB", "hwMstpProID"),
)
if mibBuilder.loadTexts:
    hwMstpProEntry.setStatus("current")


class _HwMstpProID_Type(Integer32):
    """Custom type hwMstpProID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 288),
    )


_HwMstpProID_Type.__name__ = "Integer32"
_HwMstpProID_Object = MibTableColumn
hwMstpProID = _HwMstpProID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 23, 1, 1),
    _HwMstpProID_Type()
)
hwMstpProID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMstpProID.setStatus("current")
_HwMstpProStpState_Type = HwMSTPEnabledStatus
_HwMstpProStpState_Object = MibTableColumn
hwMstpProStpState = _HwMstpProStpState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 23, 1, 4),
    _HwMstpProStpState_Type()
)
hwMstpProStpState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMstpProStpState.setStatus("current")


class _HwMstpProPriority_Type(Integer32):
    """Custom type hwMstpProPriority based on Integer32"""
    defaultValue = 32768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_HwMstpProPriority_Type.__name__ = "Integer32"
_HwMstpProPriority_Object = MibTableColumn
hwMstpProPriority = _HwMstpProPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 23, 1, 5),
    _HwMstpProPriority_Type()
)
hwMstpProPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMstpProPriority.setStatus("current")
if mibBuilder.loadTexts:
    hwMstpProPriority.setUnits("4096")


class _HwMstpProRootType_Type(Integer32):
    """Custom type hwMstpProRootType based on Integer32"""
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
        *(("normal", 0),
          ("primary", 2),
          ("secondary", 1))
    )


_HwMstpProRootType_Type.__name__ = "Integer32"
_HwMstpProRootType_Object = MibTableColumn
hwMstpProRootType = _HwMstpProRootType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 23, 1, 6),
    _HwMstpProRootType_Type()
)
hwMstpProRootType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMstpProRootType.setStatus("current")


class _HwMstpProForceVersion_Type(Integer32):
    """Custom type hwMstpProForceVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mstp", 3),
          ("rstp", 2),
          ("stp", 0))
    )


_HwMstpProForceVersion_Type.__name__ = "Integer32"
_HwMstpProForceVersion_Object = MibTableColumn
hwMstpProForceVersion = _HwMstpProForceVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 23, 1, 7),
    _HwMstpProForceVersion_Type()
)
hwMstpProForceVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMstpProForceVersion.setStatus("current")


class _HwMstpProBpduGuard_Type(HwMSTPEnabledStatus):
    """Custom type hwMstpProBpduGuard based on HwMSTPEnabledStatus"""


_HwMstpProBpduGuard_Object = MibTableColumn
hwMstpProBpduGuard = _HwMstpProBpduGuard_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 23, 1, 8),
    _HwMstpProBpduGuard_Type()
)
hwMstpProBpduGuard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMstpProBpduGuard.setStatus("current")


class _HwMstpProDiameter_Type(Integer32):
    """Custom type hwMstpProDiameter based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 7),
        ValueRangeConstraint(65535, 65535),
    )


_HwMstpProDiameter_Type.__name__ = "Integer32"
_HwMstpProDiameter_Object = MibTableColumn
hwMstpProDiameter = _HwMstpProDiameter_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 23, 1, 9),
    _HwMstpProDiameter_Type()
)
hwMstpProDiameter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMstpProDiameter.setStatus("current")


class _HwMstpProConvergeMode_Type(Integer32):
    """Custom type hwMstpProConvergeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fast", 1),
          ("normal", 2))
    )


_HwMstpProConvergeMode_Type.__name__ = "Integer32"
_HwMstpProConvergeMode_Object = MibTableColumn
hwMstpProConvergeMode = _HwMstpProConvergeMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 23, 1, 10),
    _HwMstpProConvergeMode_Type()
)
hwMstpProConvergeMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMstpProConvergeMode.setStatus("current")


class _HwMstpProMaxHops_Type(Integer32):
    """Custom type hwMstpProMaxHops based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40),
    )


_HwMstpProMaxHops_Type.__name__ = "Integer32"
_HwMstpProMaxHops_Object = MibTableColumn
hwMstpProMaxHops = _HwMstpProMaxHops_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 23, 1, 11),
    _HwMstpProMaxHops_Type()
)
hwMstpProMaxHops.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMstpProMaxHops.setStatus("current")


class _HwMstpProMCheck_Type(Integer32):
    """Custom type hwMstpProMCheck based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              65535)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("unused", 65535))
    )


_HwMstpProMCheck_Type.__name__ = "Integer32"
_HwMstpProMCheck_Object = MibTableColumn
hwMstpProMCheck = _HwMstpProMCheck_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 23, 1, 12),
    _HwMstpProMCheck_Type()
)
hwMstpProMCheck.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMstpProMCheck.setStatus("current")


class _HwMstpProPathCostStandard_Type(Integer32):
    """Custom type hwMstpProPathCostStandard based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dot1d-1998", 1),
          ("dot1t", 2),
          ("legacy", 3))
    )


_HwMstpProPathCostStandard_Type.__name__ = "Integer32"
_HwMstpProPathCostStandard_Object = MibTableColumn
hwMstpProPathCostStandard = _HwMstpProPathCostStandard_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 23, 1, 13),
    _HwMstpProPathCostStandard_Type()
)
hwMstpProPathCostStandard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMstpProPathCostStandard.setStatus("current")


class _HwMstpProHelloTime_Type(Integer32):
    """Custom type hwMstpProHelloTime based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_HwMstpProHelloTime_Type.__name__ = "Integer32"
_HwMstpProHelloTime_Object = MibTableColumn
hwMstpProHelloTime = _HwMstpProHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 23, 1, 14),
    _HwMstpProHelloTime_Type()
)
hwMstpProHelloTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMstpProHelloTime.setStatus("current")
if mibBuilder.loadTexts:
    hwMstpProHelloTime.setUnits("100")


class _HwMstpProFwdDelay_Type(Integer32):
    """Custom type hwMstpProFwdDelay based on Integer32"""
    defaultValue = 1500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 3000),
    )


_HwMstpProFwdDelay_Type.__name__ = "Integer32"
_HwMstpProFwdDelay_Object = MibTableColumn
hwMstpProFwdDelay = _HwMstpProFwdDelay_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 23, 1, 15),
    _HwMstpProFwdDelay_Type()
)
hwMstpProFwdDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMstpProFwdDelay.setStatus("current")
if mibBuilder.loadTexts:
    hwMstpProFwdDelay.setUnits("100")


class _HwMstpProMaxAge_Type(Integer32):
    """Custom type hwMstpProMaxAge based on Integer32"""
    defaultValue = 2000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 4000),
    )


_HwMstpProMaxAge_Type.__name__ = "Integer32"
_HwMstpProMaxAge_Object = MibTableColumn
hwMstpProMaxAge = _HwMstpProMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 23, 1, 16),
    _HwMstpProMaxAge_Type()
)
hwMstpProMaxAge.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMstpProMaxAge.setStatus("current")
if mibBuilder.loadTexts:
    hwMstpProMaxAge.setUnits("100")


class _HwMstpProTimerFactor_Type(Integer32):
    """Custom type hwMstpProTimerFactor based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_HwMstpProTimerFactor_Type.__name__ = "Integer32"
_HwMstpProTimerFactor_Object = MibTableColumn
hwMstpProTimerFactor = _HwMstpProTimerFactor_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 23, 1, 17),
    _HwMstpProTimerFactor_Type()
)
hwMstpProTimerFactor.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMstpProTimerFactor.setStatus("current")


class _HwMstpProTCNotify_Type(OctetString):
    """Custom type hwMstpProTCNotify based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_HwMstpProTCNotify_Type.__name__ = "OctetString"
_HwMstpProTCNotify_Object = MibTableColumn
hwMstpProTCNotify = _HwMstpProTCNotify_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 23, 1, 18),
    _HwMstpProTCNotify_Type()
)
hwMstpProTCNotify.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMstpProTCNotify.setStatus("current")


class _HwMstpProNoLinkSharePortList_Type(OctetString):
    """Custom type hwMstpProNoLinkSharePortList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwMstpProNoLinkSharePortList_Type.__name__ = "OctetString"
_HwMstpProNoLinkSharePortList_Object = MibTableColumn
hwMstpProNoLinkSharePortList = _HwMstpProNoLinkSharePortList_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 23, 1, 19),
    _HwMstpProNoLinkSharePortList_Type()
)
hwMstpProNoLinkSharePortList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMstpProNoLinkSharePortList.setStatus("current")


class _HwMstpProLinkSharePortList_Type(OctetString):
    """Custom type hwMstpProLinkSharePortList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwMstpProLinkSharePortList_Type.__name__ = "OctetString"
_HwMstpProLinkSharePortList_Object = MibTableColumn
hwMstpProLinkSharePortList = _HwMstpProLinkSharePortList_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 23, 1, 20),
    _HwMstpProLinkSharePortList_Type()
)
hwMstpProLinkSharePortList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMstpProLinkSharePortList.setStatus("current")


class _HwMstpProTcGuard_Type(HwMSTPEnabledStatus):
    """Custom type hwMstpProTcGuard based on HwMSTPEnabledStatus"""


_HwMstpProTcGuard_Object = MibTableColumn
hwMstpProTcGuard = _HwMstpProTcGuard_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 23, 1, 21),
    _HwMstpProTcGuard_Type()
)
hwMstpProTcGuard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMstpProTcGuard.setStatus("current")


class _HwMstpProTcGuardThreshold_Type(Integer32):
    """Custom type hwMstpProTcGuardThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HwMstpProTcGuardThreshold_Type.__name__ = "Integer32"
_HwMstpProTcGuardThreshold_Object = MibTableColumn
hwMstpProTcGuardThreshold = _HwMstpProTcGuardThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 23, 1, 22),
    _HwMstpProTcGuardThreshold_Type()
)
hwMstpProTcGuardThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMstpProTcGuardThreshold.setStatus("current")


class _HwMstpProTcNotifyProcess_Type(EnabledStatus):
    """Custom type hwMstpProTcNotifyProcess based on EnabledStatus"""


_HwMstpProTcNotifyProcess_Object = MibTableColumn
hwMstpProTcNotifyProcess = _HwMstpProTcNotifyProcess_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 23, 1, 23),
    _HwMstpProTcNotifyProcess_Type()
)
hwMstpProTcNotifyProcess.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMstpProTcNotifyProcess.setStatus("current")


class _HwMstpProRegionConfActive_Type(EnabledStatus):
    """Custom type hwMstpProRegionConfActive based on EnabledStatus"""


_HwMstpProRegionConfActive_Object = MibTableColumn
hwMstpProRegionConfActive = _HwMstpProRegionConfActive_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 23, 1, 24),
    _HwMstpProRegionConfActive_Type()
)
hwMstpProRegionConfActive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMstpProRegionConfActive.setStatus("current")


class _HwMstpProLinkShareGuard_Type(EnabledStatus):
    """Custom type hwMstpProLinkShareGuard based on EnabledStatus"""


_HwMstpProLinkShareGuard_Object = MibTableColumn
hwMstpProLinkShareGuard = _HwMstpProLinkShareGuard_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 23, 1, 25),
    _HwMstpProLinkShareGuard_Type()
)
hwMstpProLinkShareGuard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMstpProLinkShareGuard.setStatus("current")


class _HwMstpConfigDegist_Type(OctetString):
    """Custom type hwMstpConfigDegist based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HwMstpConfigDegist_Type.__name__ = "OctetString"
_HwMstpConfigDegist_Object = MibTableColumn
hwMstpConfigDegist = _HwMstpConfigDegist_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 23, 1, 26),
    _HwMstpConfigDegist_Type()
)
hwMstpConfigDegist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMstpConfigDegist.setStatus("current")
_HwMstpProRegionConfShare_Type = EnabledStatus
_HwMstpProRegionConfShare_Object = MibTableColumn
hwMstpProRegionConfShare = _HwMstpProRegionConfShare_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 23, 1, 27),
    _HwMstpProRegionConfShare_Type()
)
hwMstpProRegionConfShare.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMstpProRegionConfShare.setStatus("current")
_HwMstpProRowStatus_Type = RowStatus
_HwMstpProRowStatus_Object = MibTableColumn
hwMstpProRowStatus = _HwMstpProRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 23, 1, 30),
    _HwMstpProRowStatus_Type()
)
hwMstpProRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMstpProRowStatus.setStatus("current")


class _HwMstpProTcGuardInterval_Type(Integer32):
    """Custom type hwMstpProTcGuardInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_HwMstpProTcGuardInterval_Type.__name__ = "Integer32"
_HwMstpProTcGuardInterval_Object = MibTableColumn
hwMstpProTcGuardInterval = _HwMstpProTcGuardInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 23, 1, 31),
    _HwMstpProTcGuardInterval_Type()
)
hwMstpProTcGuardInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMstpProTcGuardInterval.setStatus("current")
_HwMstpPortBindTable_Object = MibTable
hwMstpPortBindTable = _HwMstpPortBindTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 24)
)
if mibBuilder.loadTexts:
    hwMstpPortBindTable.setStatus("current")
_HwMstpPortBindEntry_Object = MibTableRow
hwMstpPortBindEntry = _HwMstpPortBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 24, 1)
)
hwMstpPortBindEntry.setIndexNames(
    (0, "HUAWEI-MSTP-MIB", "hwMstpProID"),
    (0, "HUAWEI-MSTP-MIB", "hwMstpPortId1"),
    (0, "HUAWEI-MSTP-MIB", "hwMstpPortId2"),
    (0, "HUAWEI-MSTP-MIB", "hwMstpPortId3"),
    (0, "HUAWEI-MSTP-MIB", "hwMstpPortId4"),
    (0, "HUAWEI-MSTP-MIB", "hwMstpPortIdFlag"),
)
if mibBuilder.loadTexts:
    hwMstpPortBindEntry.setStatus("current")


class _HwMstpPortId1_Type(Integer32):
    """Custom type hwMstpPortId1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwMstpPortId1_Type.__name__ = "Integer32"
_HwMstpPortId1_Object = MibTableColumn
hwMstpPortId1 = _HwMstpPortId1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 24, 1, 1),
    _HwMstpPortId1_Type()
)
hwMstpPortId1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMstpPortId1.setStatus("current")


class _HwMstpPortId2_Type(Integer32):
    """Custom type hwMstpPortId2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwMstpPortId2_Type.__name__ = "Integer32"
_HwMstpPortId2_Object = MibTableColumn
hwMstpPortId2 = _HwMstpPortId2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 24, 1, 2),
    _HwMstpPortId2_Type()
)
hwMstpPortId2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMstpPortId2.setStatus("current")


class _HwMstpPortId3_Type(Integer32):
    """Custom type hwMstpPortId3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwMstpPortId3_Type.__name__ = "Integer32"
_HwMstpPortId3_Object = MibTableColumn
hwMstpPortId3 = _HwMstpPortId3_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 24, 1, 3),
    _HwMstpPortId3_Type()
)
hwMstpPortId3.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMstpPortId3.setStatus("current")


class _HwMstpPortId4_Type(Integer32):
    """Custom type hwMstpPortId4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwMstpPortId4_Type.__name__ = "Integer32"
_HwMstpPortId4_Object = MibTableColumn
hwMstpPortId4 = _HwMstpPortId4_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 24, 1, 4),
    _HwMstpPortId4_Type()
)
hwMstpPortId4.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMstpPortId4.setStatus("current")


class _HwMstpPortIdFlag_Type(Integer32):
    """Custom type hwMstpPortIdFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwMstpPortIdFlag_Type.__name__ = "Integer32"
_HwMstpPortIdFlag_Object = MibTableColumn
hwMstpPortIdFlag = _HwMstpPortIdFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 24, 1, 5),
    _HwMstpPortIdFlag_Type()
)
hwMstpPortIdFlag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMstpPortIdFlag.setStatus("current")


class _HwMstpPortVlanListLow_Type(OctetString):
    """Custom type hwMstpPortVlanListLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HwMstpPortVlanListLow_Type.__name__ = "OctetString"
_HwMstpPortVlanListLow_Object = MibTableColumn
hwMstpPortVlanListLow = _HwMstpPortVlanListLow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 24, 1, 6),
    _HwMstpPortVlanListLow_Type()
)
hwMstpPortVlanListLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMstpPortVlanListLow.setStatus("current")


class _HwMstpPortVlanListHigh_Type(OctetString):
    """Custom type hwMstpPortVlanListHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HwMstpPortVlanListHigh_Type.__name__ = "OctetString"
_HwMstpPortVlanListHigh_Object = MibTableColumn
hwMstpPortVlanListHigh = _HwMstpPortVlanListHigh_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 24, 1, 7),
    _HwMstpPortVlanListHigh_Type()
)
hwMstpPortVlanListHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMstpPortVlanListHigh.setStatus("current")


class _HwMstpProNewPortType_Type(Integer32):
    """Custom type hwMstpProNewPortType based on Integer32"""
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
        *(("linkshare", 3),
          ("nolinkshare", 2),
          ("nolinksharewithvlan", 4),
          ("normal", 1))
    )


_HwMstpProNewPortType_Type.__name__ = "Integer32"
_HwMstpProNewPortType_Object = MibTableColumn
hwMstpProNewPortType = _HwMstpProNewPortType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 24, 1, 8),
    _HwMstpProNewPortType_Type()
)
hwMstpProNewPortType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMstpProNewPortType.setStatus("current")


class _HwMstpProNewPortBpduVlan_Type(Integer32):
    """Custom type hwMstpProNewPortBpduVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HwMstpProNewPortBpduVlan_Type.__name__ = "Integer32"
_HwMstpProNewPortBpduVlan_Object = MibTableColumn
hwMstpProNewPortBpduVlan = _HwMstpProNewPortBpduVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 24, 1, 9),
    _HwMstpProNewPortBpduVlan_Type()
)
hwMstpProNewPortBpduVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMstpProNewPortBpduVlan.setStatus("current")
_HwMstpPortBindRowStatus_Type = RowStatus
_HwMstpPortBindRowStatus_Object = MibTableColumn
hwMstpPortBindRowStatus = _HwMstpPortBindRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 24, 1, 100),
    _HwMstpPortBindRowStatus_Type()
)
hwMstpPortBindRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMstpPortBindRowStatus.setStatus("current")
_HwMstpProPortTable_Object = MibTable
hwMstpProPortTable = _HwMstpProPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 25)
)
if mibBuilder.loadTexts:
    hwMstpProPortTable.setStatus("current")
_HwMstpProPortEntry_Object = MibTableRow
hwMstpProPortEntry = _HwMstpProPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 25, 1)
)
hwMstpProPortEntry.setIndexNames(
    (0, "HUAWEI-MSTP-MIB", "hwMstpProID"),
    (0, "HUAWEI-MSTP-MIB", "hwMstpInstanceID"),
    (0, "HUAWEI-MSTP-MIB", "hwMstpiPortIndex"),
)
if mibBuilder.loadTexts:
    hwMstpProPortEntry.setStatus("current")


class _HwMstpProPortState_Type(Integer32):
    """Custom type hwMstpProPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("discarding", 2),
          ("forwarding", 5),
          ("learning", 4))
    )


_HwMstpProPortState_Type.__name__ = "Integer32"
_HwMstpProPortState_Object = MibTableColumn
hwMstpProPortState = _HwMstpProPortState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 25, 1, 2),
    _HwMstpProPortState_Type()
)
hwMstpProPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMstpProPortState.setStatus("current")


class _HwMstpProPortPriority_Type(Integer32):
    """Custom type hwMstpProPortPriority based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_HwMstpProPortPriority_Type.__name__ = "Integer32"
_HwMstpProPortPriority_Object = MibTableColumn
hwMstpProPortPriority = _HwMstpProPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 25, 1, 3),
    _HwMstpProPortPriority_Type()
)
hwMstpProPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMstpProPortPriority.setStatus("current")


class _HwMstpProPortPathCost_Type(Integer32):
    """Custom type hwMstpProPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_HwMstpProPortPathCost_Type.__name__ = "Integer32"
_HwMstpProPortPathCost_Object = MibTableColumn
hwMstpProPortPathCost = _HwMstpProPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 25, 1, 4),
    _HwMstpProPortPathCost_Type()
)
hwMstpProPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMstpProPortPathCost.setStatus("current")
_HwMstpProPortDesignatedRoot_Type = BridgeId
_HwMstpProPortDesignatedRoot_Object = MibTableColumn
hwMstpProPortDesignatedRoot = _HwMstpProPortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 25, 1, 5),
    _HwMstpProPortDesignatedRoot_Type()
)
hwMstpProPortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMstpProPortDesignatedRoot.setStatus("current")
_HwMstpProPortDesignatedCost_Type = Integer32
_HwMstpProPortDesignatedCost_Object = MibTableColumn
hwMstpProPortDesignatedCost = _HwMstpProPortDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 25, 1, 6),
    _HwMstpProPortDesignatedCost_Type()
)
hwMstpProPortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMstpProPortDesignatedCost.setStatus("current")
_HwMstpProPortDesignatedBridge_Type = BridgeId
_HwMstpProPortDesignatedBridge_Object = MibTableColumn
hwMstpProPortDesignatedBridge = _HwMstpProPortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 25, 1, 7),
    _HwMstpProPortDesignatedBridge_Type()
)
hwMstpProPortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMstpProPortDesignatedBridge.setStatus("current")


class _HwMstpProPortDesignatedPort_Type(OctetString):
    """Custom type hwMstpProPortDesignatedPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_HwMstpProPortDesignatedPort_Type.__name__ = "OctetString"
_HwMstpProPortDesignatedPort_Object = MibTableColumn
hwMstpProPortDesignatedPort = _HwMstpProPortDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 25, 1, 8),
    _HwMstpProPortDesignatedPort_Type()
)
hwMstpProPortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMstpProPortDesignatedPort.setStatus("current")


class _HwMstpProPortStpEdgeport_Type(HwMSTPEnabledStatus):
    """Custom type hwMstpProPortStpEdgeport based on HwMSTPEnabledStatus"""


_HwMstpProPortStpEdgeport_Object = MibTableColumn
hwMstpProPortStpEdgeport = _HwMstpProPortStpEdgeport_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 25, 1, 9),
    _HwMstpProPortStpEdgeport_Type()
)
hwMstpProPortStpEdgeport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMstpProPortStpEdgeport.setStatus("current")


class _HwMstpProPortStpPointToPoint_Type(Integer32):
    """Custom type hwMstpProPortStpPointToPoint based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("forceFalse", 2),
          ("forceTrue", 1))
    )


_HwMstpProPortStpPointToPoint_Type.__name__ = "Integer32"
_HwMstpProPortStpPointToPoint_Object = MibTableColumn
hwMstpProPortStpPointToPoint = _HwMstpProPortStpPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 25, 1, 10),
    _HwMstpProPortStpPointToPoint_Type()
)
hwMstpProPortStpPointToPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMstpProPortStpPointToPoint.setStatus("current")


class _HwMstpProPortStpMcheck_Type(Integer32):
    """Custom type hwMstpProPortStpMcheck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              65535)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("unused", 65535))
    )


_HwMstpProPortStpMcheck_Type.__name__ = "Integer32"
_HwMstpProPortStpMcheck_Object = MibTableColumn
hwMstpProPortStpMcheck = _HwMstpProPortStpMcheck_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 25, 1, 11),
    _HwMstpProPortStpMcheck_Type()
)
hwMstpProPortStpMcheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMstpProPortStpMcheck.setStatus("current")


class _HwMstpProPortStpTransLimit_Type(Integer32):
    """Custom type hwMstpProPortStpTransLimit based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HwMstpProPortStpTransLimit_Type.__name__ = "Integer32"
_HwMstpProPortStpTransLimit_Object = MibTableColumn
hwMstpProPortStpTransLimit = _HwMstpProPortStpTransLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 25, 1, 12),
    _HwMstpProPortStpTransLimit_Type()
)
hwMstpProPortStpTransLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMstpProPortStpTransLimit.setStatus("current")
_HwMstpProPortStpRXStpBPDU_Type = Counter32
_HwMstpProPortStpRXStpBPDU_Object = MibTableColumn
hwMstpProPortStpRXStpBPDU = _HwMstpProPortStpRXStpBPDU_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 25, 1, 13),
    _HwMstpProPortStpRXStpBPDU_Type()
)
hwMstpProPortStpRXStpBPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMstpProPortStpRXStpBPDU.setStatus("current")
_HwMstpProPortStpTXStpBPDU_Type = Counter32
_HwMstpProPortStpTXStpBPDU_Object = MibTableColumn
hwMstpProPortStpTXStpBPDU = _HwMstpProPortStpTXStpBPDU_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 25, 1, 14),
    _HwMstpProPortStpTXStpBPDU_Type()
)
hwMstpProPortStpTXStpBPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMstpProPortStpTXStpBPDU.setStatus("current")
_HwMstpProPortStpRXTCNBPDU_Type = Counter32
_HwMstpProPortStpRXTCNBPDU_Object = MibTableColumn
hwMstpProPortStpRXTCNBPDU = _HwMstpProPortStpRXTCNBPDU_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 25, 1, 15),
    _HwMstpProPortStpRXTCNBPDU_Type()
)
hwMstpProPortStpRXTCNBPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMstpProPortStpRXTCNBPDU.setStatus("current")
_HwMstpProPortStpTXTCNBPDU_Type = Counter32
_HwMstpProPortStpTXTCNBPDU_Object = MibTableColumn
hwMstpProPortStpTXTCNBPDU = _HwMstpProPortStpTXTCNBPDU_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 25, 1, 16),
    _HwMstpProPortStpTXTCNBPDU_Type()
)
hwMstpProPortStpTXTCNBPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMstpProPortStpTXTCNBPDU.setStatus("current")
_HwMstpProPortStpRXRSTPBPDU_Type = Counter32
_HwMstpProPortStpRXRSTPBPDU_Object = MibTableColumn
hwMstpProPortStpRXRSTPBPDU = _HwMstpProPortStpRXRSTPBPDU_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 25, 1, 17),
    _HwMstpProPortStpRXRSTPBPDU_Type()
)
hwMstpProPortStpRXRSTPBPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMstpProPortStpRXRSTPBPDU.setStatus("current")
_HwMstpProPortStpTXRSTPBPDU_Type = Counter32
_HwMstpProPortStpTXRSTPBPDU_Object = MibTableColumn
hwMstpProPortStpTXRSTPBPDU = _HwMstpProPortStpTXRSTPBPDU_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 25, 1, 18),
    _HwMstpProPortStpTXRSTPBPDU_Type()
)
hwMstpProPortStpTXRSTPBPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMstpProPortStpTXRSTPBPDU.setStatus("current")
_HwMstpProPortStpRXMSTPBPDU_Type = Counter32
_HwMstpProPortStpRXMSTPBPDU_Object = MibTableColumn
hwMstpProPortStpRXMSTPBPDU = _HwMstpProPortStpRXMSTPBPDU_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 25, 1, 19),
    _HwMstpProPortStpRXMSTPBPDU_Type()
)
hwMstpProPortStpRXMSTPBPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMstpProPortStpRXMSTPBPDU.setStatus("current")
_HwMstpProPortStpTXMSTPBPDU_Type = Counter32
_HwMstpProPortStpTXMSTPBPDU_Object = MibTableColumn
hwMstpProPortStpTXMSTPBPDU = _HwMstpProPortStpTXMSTPBPDU_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 25, 1, 20),
    _HwMstpProPortStpTXMSTPBPDU_Type()
)
hwMstpProPortStpTXMSTPBPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMstpProPortStpTXMSTPBPDU.setStatus("current")


class _HwMstpProPortStpClearStatistics_Type(Integer32):
    """Custom type hwMstpProPortStpClearStatistics based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              65535)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("unused", 65535))
    )


_HwMstpProPortStpClearStatistics_Type.__name__ = "Integer32"
_HwMstpProPortStpClearStatistics_Object = MibTableColumn
hwMstpProPortStpClearStatistics = _HwMstpProPortStpClearStatistics_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 25, 1, 21),
    _HwMstpProPortStpClearStatistics_Type()
)
hwMstpProPortStpClearStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMstpProPortStpClearStatistics.setStatus("current")


class _HwMstpProPortStpDefaultPortCost_Type(Integer32):
    """Custom type hwMstpProPortStpDefaultPortCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              65535)
        )
    )
    namedValues = NamedValues(
        *(("reset", 1),
          ("unused", 65535))
    )


_HwMstpProPortStpDefaultPortCost_Type.__name__ = "Integer32"
_HwMstpProPortStpDefaultPortCost_Object = MibTableColumn
hwMstpProPortStpDefaultPortCost = _HwMstpProPortStpDefaultPortCost_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 25, 1, 22),
    _HwMstpProPortStpDefaultPortCost_Type()
)
hwMstpProPortStpDefaultPortCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMstpProPortStpDefaultPortCost.setStatus("current")


class _HwMstpProPortStpStatus_Type(HwMSTPEnabledStatus):
    """Custom type hwMstpProPortStpStatus based on HwMSTPEnabledStatus"""


_HwMstpProPortStpStatus_Object = MibTableColumn
hwMstpProPortStpStatus = _HwMstpProPortStpStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 25, 1, 23),
    _HwMstpProPortStpStatus_Type()
)
hwMstpProPortStpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMstpProPortStpStatus.setStatus("current")


class _HwMstpProPortRootGuard_Type(HwMSTPEnabledStatus):
    """Custom type hwMstpProPortRootGuard based on HwMSTPEnabledStatus"""


_HwMstpProPortRootGuard_Object = MibTableColumn
hwMstpProPortRootGuard = _HwMstpProPortRootGuard_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 25, 1, 24),
    _HwMstpProPortRootGuard_Type()
)
hwMstpProPortRootGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMstpProPortRootGuard.setStatus("current")


class _HwMstpProPortLoopGuard_Type(HwMSTPEnabledStatus):
    """Custom type hwMstpProPortLoopGuard based on HwMSTPEnabledStatus"""


_HwMstpProPortLoopGuard_Object = MibTableColumn
hwMstpProPortLoopGuard = _HwMstpProPortLoopGuard_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 25, 1, 25),
    _HwMstpProPortLoopGuard_Type()
)
hwMstpProPortLoopGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMstpProPortLoopGuard.setStatus("current")


class _HwMstpProPortCompliance_Type(Integer32):
    """Custom type hwMstpProPortCompliance based on Integer32"""
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
        *(("auto", 1),
          ("dotls", 2),
          ("legacy", 3))
    )


_HwMstpProPortCompliance_Type.__name__ = "Integer32"
_HwMstpProPortCompliance_Object = MibTableColumn
hwMstpProPortCompliance = _HwMstpProPortCompliance_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 25, 1, 26),
    _HwMstpProPortCompliance_Type()
)
hwMstpProPortCompliance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMstpProPortCompliance.setStatus("current")


class _HwMstpProPortConfigDigestSnooping_Type(HwMSTPEnabledStatus):
    """Custom type hwMstpProPortConfigDigestSnooping based on HwMSTPEnabledStatus"""


_HwMstpProPortConfigDigestSnooping_Object = MibTableColumn
hwMstpProPortConfigDigestSnooping = _HwMstpProPortConfigDigestSnooping_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 25, 1, 27),
    _HwMstpProPortConfigDigestSnooping_Type()
)
hwMstpProPortConfigDigestSnooping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMstpProPortConfigDigestSnooping.setStatus("current")


class _HwMstpProPortNoAgreementCheck_Type(HwMSTPEnabledStatus):
    """Custom type hwMstpProPortNoAgreementCheck based on HwMSTPEnabledStatus"""


_HwMstpProPortNoAgreementCheck_Object = MibTableColumn
hwMstpProPortNoAgreementCheck = _HwMstpProPortNoAgreementCheck_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 25, 1, 30),
    _HwMstpProPortNoAgreementCheck_Type()
)
hwMstpProPortNoAgreementCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMstpProPortNoAgreementCheck.setStatus("current")


class _HwMstpProPortTCNotify_Type(HwMSTPEnabledStatus):
    """Custom type hwMstpProPortTCNotify based on HwMSTPEnabledStatus"""


_HwMstpProPortTCNotify_Object = MibTableColumn
hwMstpProPortTCNotify = _HwMstpProPortTCNotify_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 25, 1, 31),
    _HwMstpProPortTCNotify_Type()
)
hwMstpProPortTCNotify.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMstpProPortTCNotify.setStatus("current")


class _HwMstpProPortType_Type(Integer32):
    """Custom type hwMstpProPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("linkshare", 2),
          ("nolinkshare", 1),
          ("none", 0))
    )


_HwMstpProPortType_Type.__name__ = "Integer32"
_HwMstpProPortType_Object = MibTableColumn
hwMstpProPortType = _HwMstpProPortType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 25, 1, 32),
    _HwMstpProPortType_Type()
)
hwMstpProPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMstpProPortType.setStatus("current")
_HwMstpTcGuard_Type = HwMSTPEnabledStatus
_HwMstpTcGuard_Object = MibScalar
hwMstpTcGuard = _HwMstpTcGuard_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 26),
    _HwMstpTcGuard_Type()
)
hwMstpTcGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMstpTcGuard.setStatus("current")


class _HwMstpTcGuardThreshold_Type(Integer32):
    """Custom type hwMstpTcGuardThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HwMstpTcGuardThreshold_Type.__name__ = "Integer32"
_HwMstpTcGuardThreshold_Object = MibScalar
hwMstpTcGuardThreshold = _HwMstpTcGuardThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 27),
    _HwMstpTcGuardThreshold_Type()
)
hwMstpTcGuardThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMstpTcGuardThreshold.setStatus("current")
_HwMstpProInstanceTable_Object = MibTable
hwMstpProInstanceTable = _HwMstpProInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 28)
)
if mibBuilder.loadTexts:
    hwMstpProInstanceTable.setStatus("current")
_HwMstpProInstanceEntry_Object = MibTableRow
hwMstpProInstanceEntry = _HwMstpProInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 28, 1)
)
hwMstpProInstanceEntry.setIndexNames(
    (0, "HUAWEI-MSTP-MIB", "hwMstpProID"),
    (0, "HUAWEI-MSTP-MIB", "hwMstpInstanceID"),
)
if mibBuilder.loadTexts:
    hwMstpProInstanceEntry.setStatus("current")
_HwMstpProInstanceBridgeID_Type = BridgeId
_HwMstpProInstanceBridgeID_Object = MibTableColumn
hwMstpProInstanceBridgeID = _HwMstpProInstanceBridgeID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 28, 1, 1),
    _HwMstpProInstanceBridgeID_Type()
)
hwMstpProInstanceBridgeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMstpProInstanceBridgeID.setStatus("current")


class _HwMstpProInstanceBridgePriority_Type(Integer32):
    """Custom type hwMstpProInstanceBridgePriority based on Integer32"""
    defaultValue = 32768

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_HwMstpProInstanceBridgePriority_Type.__name__ = "Integer32"
_HwMstpProInstanceBridgePriority_Object = MibTableColumn
hwMstpProInstanceBridgePriority = _HwMstpProInstanceBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 28, 1, 2),
    _HwMstpProInstanceBridgePriority_Type()
)
hwMstpProInstanceBridgePriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMstpProInstanceBridgePriority.setStatus("current")
_HwMstpProInstanceDesignedRoot_Type = BridgeId
_HwMstpProInstanceDesignedRoot_Object = MibTableColumn
hwMstpProInstanceDesignedRoot = _HwMstpProInstanceDesignedRoot_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 28, 1, 3),
    _HwMstpProInstanceDesignedRoot_Type()
)
hwMstpProInstanceDesignedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMstpProInstanceDesignedRoot.setStatus("current")
_HwMstpProInstanceRootPathCost_Type = Integer32
_HwMstpProInstanceRootPathCost_Object = MibTableColumn
hwMstpProInstanceRootPathCost = _HwMstpProInstanceRootPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 28, 1, 4),
    _HwMstpProInstanceRootPathCost_Type()
)
hwMstpProInstanceRootPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMstpProInstanceRootPathCost.setStatus("current")
_HwMstpProInstanceRootPort_Type = Integer32
_HwMstpProInstanceRootPort_Object = MibTableColumn
hwMstpProInstanceRootPort = _HwMstpProInstanceRootPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 28, 1, 5),
    _HwMstpProInstanceRootPort_Type()
)
hwMstpProInstanceRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMstpProInstanceRootPort.setStatus("current")


class _HwMstpProInstanceRootType_Type(Integer32):
    """Custom type hwMstpProInstanceRootType based on Integer32"""
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
        *(("normal", 0),
          ("primary", 2),
          ("secondary", 1))
    )


_HwMstpProInstanceRootType_Type.__name__ = "Integer32"
_HwMstpProInstanceRootType_Object = MibTableColumn
hwMstpProInstanceRootType = _HwMstpProInstanceRootType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 28, 1, 6),
    _HwMstpProInstanceRootType_Type()
)
hwMstpProInstanceRootType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMstpProInstanceRootType.setStatus("current")
_HwMstpProInstanceRemainingHops_Type = Integer32
_HwMstpProInstanceRemainingHops_Object = MibTableColumn
hwMstpProInstanceRemainingHops = _HwMstpProInstanceRemainingHops_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 28, 1, 7),
    _HwMstpProInstanceRemainingHops_Type()
)
hwMstpProInstanceRemainingHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMstpProInstanceRemainingHops.setStatus("current")


class _HwMstpProInstanceAdminMappedVlanListLow_Type(OctetString):
    """Custom type hwMstpProInstanceAdminMappedVlanListLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HwMstpProInstanceAdminMappedVlanListLow_Type.__name__ = "OctetString"
_HwMstpProInstanceAdminMappedVlanListLow_Object = MibTableColumn
hwMstpProInstanceAdminMappedVlanListLow = _HwMstpProInstanceAdminMappedVlanListLow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 28, 1, 8),
    _HwMstpProInstanceAdminMappedVlanListLow_Type()
)
hwMstpProInstanceAdminMappedVlanListLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMstpProInstanceAdminMappedVlanListLow.setStatus("current")


class _HwMstpProInstanceAdminMappedVlanListHigh_Type(OctetString):
    """Custom type hwMstpProInstanceAdminMappedVlanListHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HwMstpProInstanceAdminMappedVlanListHigh_Type.__name__ = "OctetString"
_HwMstpProInstanceAdminMappedVlanListHigh_Object = MibTableColumn
hwMstpProInstanceAdminMappedVlanListHigh = _HwMstpProInstanceAdminMappedVlanListHigh_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 28, 1, 9),
    _HwMstpProInstanceAdminMappedVlanListHigh_Type()
)
hwMstpProInstanceAdminMappedVlanListHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMstpProInstanceAdminMappedVlanListHigh.setStatus("current")


class _HwMstpProInstanceOperMappedVlanListLow_Type(OctetString):
    """Custom type hwMstpProInstanceOperMappedVlanListLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HwMstpProInstanceOperMappedVlanListLow_Type.__name__ = "OctetString"
_HwMstpProInstanceOperMappedVlanListLow_Object = MibTableColumn
hwMstpProInstanceOperMappedVlanListLow = _HwMstpProInstanceOperMappedVlanListLow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 28, 1, 10),
    _HwMstpProInstanceOperMappedVlanListLow_Type()
)
hwMstpProInstanceOperMappedVlanListLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMstpProInstanceOperMappedVlanListLow.setStatus("current")


class _HwMstpProInstanceOperMappedVlanListHigh_Type(OctetString):
    """Custom type hwMstpProInstanceOperMappedVlanListHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HwMstpProInstanceOperMappedVlanListHigh_Type.__name__ = "OctetString"
_HwMstpProInstanceOperMappedVlanListHigh_Object = MibTableColumn
hwMstpProInstanceOperMappedVlanListHigh = _HwMstpProInstanceOperMappedVlanListHigh_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 28, 1, 11),
    _HwMstpProInstanceOperMappedVlanListHigh_Type()
)
hwMstpProInstanceOperMappedVlanListHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMstpProInstanceOperMappedVlanListHigh.setStatus("current")
_HwMstpProInstanceRowStatus_Type = RowStatus
_HwMstpProInstanceRowStatus_Object = MibTableColumn
hwMstpProInstanceRowStatus = _HwMstpProInstanceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 28, 1, 100),
    _HwMstpProInstanceRowStatus_Type()
)
hwMstpProInstanceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMstpProInstanceRowStatus.setStatus("current")
_HwMstpProNewPortTable_Object = MibTable
hwMstpProNewPortTable = _HwMstpProNewPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 29)
)
if mibBuilder.loadTexts:
    hwMstpProNewPortTable.setStatus("current")
_HwMstpProNewPortEntry_Object = MibTableRow
hwMstpProNewPortEntry = _HwMstpProNewPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 29, 1)
)
hwMstpProNewPortEntry.setIndexNames(
    (0, "HUAWEI-MSTP-MIB", "hwMstpProID"),
    (0, "HUAWEI-MSTP-MIB", "hwMstpInstanceID"),
    (0, "HUAWEI-MSTP-MIB", "hwMstpPortId1"),
    (0, "HUAWEI-MSTP-MIB", "hwMstpPortId2"),
    (0, "HUAWEI-MSTP-MIB", "hwMstpPortId3"),
    (0, "HUAWEI-MSTP-MIB", "hwMstpPortId4"),
    (0, "HUAWEI-MSTP-MIB", "hwMstpPortIdFlag"),
)
if mibBuilder.loadTexts:
    hwMstpProNewPortEntry.setStatus("current")


class _HwMstpProNewPortState_Type(Integer32):
    """Custom type hwMstpProNewPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("discarding", 2),
          ("forwarding", 5),
          ("learning", 4))
    )


_HwMstpProNewPortState_Type.__name__ = "Integer32"
_HwMstpProNewPortState_Object = MibTableColumn
hwMstpProNewPortState = _HwMstpProNewPortState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 29, 1, 1),
    _HwMstpProNewPortState_Type()
)
hwMstpProNewPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMstpProNewPortState.setStatus("current")


class _HwMstpProNewPortPriority_Type(Integer32):
    """Custom type hwMstpProNewPortPriority based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_HwMstpProNewPortPriority_Type.__name__ = "Integer32"
_HwMstpProNewPortPriority_Object = MibTableColumn
hwMstpProNewPortPriority = _HwMstpProNewPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 29, 1, 2),
    _HwMstpProNewPortPriority_Type()
)
hwMstpProNewPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMstpProNewPortPriority.setStatus("current")


class _HwMstpProNewPortPathCost_Type(Integer32):
    """Custom type hwMstpProNewPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_HwMstpProNewPortPathCost_Type.__name__ = "Integer32"
_HwMstpProNewPortPathCost_Object = MibTableColumn
hwMstpProNewPortPathCost = _HwMstpProNewPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 29, 1, 3),
    _HwMstpProNewPortPathCost_Type()
)
hwMstpProNewPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMstpProNewPortPathCost.setStatus("current")
_HwMstpProNewPortDesignatedRoot_Type = BridgeId
_HwMstpProNewPortDesignatedRoot_Object = MibTableColumn
hwMstpProNewPortDesignatedRoot = _HwMstpProNewPortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 29, 1, 4),
    _HwMstpProNewPortDesignatedRoot_Type()
)
hwMstpProNewPortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMstpProNewPortDesignatedRoot.setStatus("current")
_HwMstpProNewPortDesignatedCost_Type = Integer32
_HwMstpProNewPortDesignatedCost_Object = MibTableColumn
hwMstpProNewPortDesignatedCost = _HwMstpProNewPortDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 29, 1, 5),
    _HwMstpProNewPortDesignatedCost_Type()
)
hwMstpProNewPortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMstpProNewPortDesignatedCost.setStatus("current")
_HwMstpProNewPortDesignatedBridge_Type = BridgeId
_HwMstpProNewPortDesignatedBridge_Object = MibTableColumn
hwMstpProNewPortDesignatedBridge = _HwMstpProNewPortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 29, 1, 6),
    _HwMstpProNewPortDesignatedBridge_Type()
)
hwMstpProNewPortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMstpProNewPortDesignatedBridge.setStatus("current")


class _HwMstpProNewPortDesignatedPort_Type(OctetString):
    """Custom type hwMstpProNewPortDesignatedPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_HwMstpProNewPortDesignatedPort_Type.__name__ = "OctetString"
_HwMstpProNewPortDesignatedPort_Object = MibTableColumn
hwMstpProNewPortDesignatedPort = _HwMstpProNewPortDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 29, 1, 7),
    _HwMstpProNewPortDesignatedPort_Type()
)
hwMstpProNewPortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMstpProNewPortDesignatedPort.setStatus("current")


class _HwMstpProNewPortStpEdgeport_Type(Integer32):
    """Custom type hwMstpProNewPortStpEdgeport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("undo", 3))
    )


_HwMstpProNewPortStpEdgeport_Type.__name__ = "Integer32"
_HwMstpProNewPortStpEdgeport_Object = MibTableColumn
hwMstpProNewPortStpEdgeport = _HwMstpProNewPortStpEdgeport_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 29, 1, 8),
    _HwMstpProNewPortStpEdgeport_Type()
)
hwMstpProNewPortStpEdgeport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMstpProNewPortStpEdgeport.setStatus("current")


class _HwMstpProNewPortStpPointToPoint_Type(Integer32):
    """Custom type hwMstpProNewPortStpPointToPoint based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("forceFalse", 2),
          ("forceTrue", 1))
    )


_HwMstpProNewPortStpPointToPoint_Type.__name__ = "Integer32"
_HwMstpProNewPortStpPointToPoint_Object = MibTableColumn
hwMstpProNewPortStpPointToPoint = _HwMstpProNewPortStpPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 29, 1, 9),
    _HwMstpProNewPortStpPointToPoint_Type()
)
hwMstpProNewPortStpPointToPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMstpProNewPortStpPointToPoint.setStatus("current")


class _HwMstpProNewPortStpMcheck_Type(Integer32):
    """Custom type hwMstpProNewPortStpMcheck based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              65535)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("unused", 65535))
    )


_HwMstpProNewPortStpMcheck_Type.__name__ = "Integer32"
_HwMstpProNewPortStpMcheck_Object = MibTableColumn
hwMstpProNewPortStpMcheck = _HwMstpProNewPortStpMcheck_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 29, 1, 10),
    _HwMstpProNewPortStpMcheck_Type()
)
hwMstpProNewPortStpMcheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMstpProNewPortStpMcheck.setStatus("current")


class _HwMstpProNewPortStpTransLimit_Type(Integer32):
    """Custom type hwMstpProNewPortStpTransLimit based on Integer32"""
    defaultValue = 147

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwMstpProNewPortStpTransLimit_Type.__name__ = "Integer32"
_HwMstpProNewPortStpTransLimit_Object = MibTableColumn
hwMstpProNewPortStpTransLimit = _HwMstpProNewPortStpTransLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 29, 1, 11),
    _HwMstpProNewPortStpTransLimit_Type()
)
hwMstpProNewPortStpTransLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMstpProNewPortStpTransLimit.setStatus("current")
_HwMstpProNewPortStpRXStpBPDU_Type = Counter32
_HwMstpProNewPortStpRXStpBPDU_Object = MibTableColumn
hwMstpProNewPortStpRXStpBPDU = _HwMstpProNewPortStpRXStpBPDU_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 29, 1, 12),
    _HwMstpProNewPortStpRXStpBPDU_Type()
)
hwMstpProNewPortStpRXStpBPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMstpProNewPortStpRXStpBPDU.setStatus("current")
_HwMstpProNewPortStpTXStpBPDU_Type = Counter32
_HwMstpProNewPortStpTXStpBPDU_Object = MibTableColumn
hwMstpProNewPortStpTXStpBPDU = _HwMstpProNewPortStpTXStpBPDU_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 29, 1, 13),
    _HwMstpProNewPortStpTXStpBPDU_Type()
)
hwMstpProNewPortStpTXStpBPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMstpProNewPortStpTXStpBPDU.setStatus("current")
_HwMstpProNewPortStpRXTCNBPDU_Type = Counter32
_HwMstpProNewPortStpRXTCNBPDU_Object = MibTableColumn
hwMstpProNewPortStpRXTCNBPDU = _HwMstpProNewPortStpRXTCNBPDU_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 29, 1, 14),
    _HwMstpProNewPortStpRXTCNBPDU_Type()
)
hwMstpProNewPortStpRXTCNBPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMstpProNewPortStpRXTCNBPDU.setStatus("current")
_HwMstpProNewPortStpTXTCNBPDU_Type = Counter32
_HwMstpProNewPortStpTXTCNBPDU_Object = MibTableColumn
hwMstpProNewPortStpTXTCNBPDU = _HwMstpProNewPortStpTXTCNBPDU_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 29, 1, 15),
    _HwMstpProNewPortStpTXTCNBPDU_Type()
)
hwMstpProNewPortStpTXTCNBPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMstpProNewPortStpTXTCNBPDU.setStatus("current")
_HwMstpProNewPortStpRXRSTPBPDU_Type = Counter32
_HwMstpProNewPortStpRXRSTPBPDU_Object = MibTableColumn
hwMstpProNewPortStpRXRSTPBPDU = _HwMstpProNewPortStpRXRSTPBPDU_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 29, 1, 16),
    _HwMstpProNewPortStpRXRSTPBPDU_Type()
)
hwMstpProNewPortStpRXRSTPBPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMstpProNewPortStpRXRSTPBPDU.setStatus("current")
_HwMstpProNewPortStpTXRSTPBPDU_Type = Counter32
_HwMstpProNewPortStpTXRSTPBPDU_Object = MibTableColumn
hwMstpProNewPortStpTXRSTPBPDU = _HwMstpProNewPortStpTXRSTPBPDU_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 29, 1, 17),
    _HwMstpProNewPortStpTXRSTPBPDU_Type()
)
hwMstpProNewPortStpTXRSTPBPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMstpProNewPortStpTXRSTPBPDU.setStatus("current")
_HwMstpProNewPortStpRXMSTPBPDU_Type = Counter32
_HwMstpProNewPortStpRXMSTPBPDU_Object = MibTableColumn
hwMstpProNewPortStpRXMSTPBPDU = _HwMstpProNewPortStpRXMSTPBPDU_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 29, 1, 18),
    _HwMstpProNewPortStpRXMSTPBPDU_Type()
)
hwMstpProNewPortStpRXMSTPBPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMstpProNewPortStpRXMSTPBPDU.setStatus("current")
_HwMstpProNewPortStpTXMSTPBPDU_Type = Counter32
_HwMstpProNewPortStpTXMSTPBPDU_Object = MibTableColumn
hwMstpProNewPortStpTXMSTPBPDU = _HwMstpProNewPortStpTXMSTPBPDU_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 29, 1, 19),
    _HwMstpProNewPortStpTXMSTPBPDU_Type()
)
hwMstpProNewPortStpTXMSTPBPDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMstpProNewPortStpTXMSTPBPDU.setStatus("current")


class _HwMstpProNewPortStpClearStatistics_Type(Integer32):
    """Custom type hwMstpProNewPortStpClearStatistics based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              65535)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("unused", 65535))
    )


_HwMstpProNewPortStpClearStatistics_Type.__name__ = "Integer32"
_HwMstpProNewPortStpClearStatistics_Object = MibTableColumn
hwMstpProNewPortStpClearStatistics = _HwMstpProNewPortStpClearStatistics_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 29, 1, 20),
    _HwMstpProNewPortStpClearStatistics_Type()
)
hwMstpProNewPortStpClearStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMstpProNewPortStpClearStatistics.setStatus("current")


class _HwMstpProNewPortStpDefaultPortCost_Type(Integer32):
    """Custom type hwMstpProNewPortStpDefaultPortCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              65535)
        )
    )
    namedValues = NamedValues(
        *(("reset", 1),
          ("unused", 65535))
    )


_HwMstpProNewPortStpDefaultPortCost_Type.__name__ = "Integer32"
_HwMstpProNewPortStpDefaultPortCost_Object = MibTableColumn
hwMstpProNewPortStpDefaultPortCost = _HwMstpProNewPortStpDefaultPortCost_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 29, 1, 21),
    _HwMstpProNewPortStpDefaultPortCost_Type()
)
hwMstpProNewPortStpDefaultPortCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMstpProNewPortStpDefaultPortCost.setStatus("current")


class _HwMstpProNewPortStpStatus_Type(EnabledStatus):
    """Custom type hwMstpProNewPortStpStatus based on EnabledStatus"""


_HwMstpProNewPortStpStatus_Object = MibTableColumn
hwMstpProNewPortStpStatus = _HwMstpProNewPortStpStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 29, 1, 22),
    _HwMstpProNewPortStpStatus_Type()
)
hwMstpProNewPortStpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMstpProNewPortStpStatus.setStatus("current")


class _HwMstpProNewPortRootGuard_Type(EnabledStatus):
    """Custom type hwMstpProNewPortRootGuard based on EnabledStatus"""


_HwMstpProNewPortRootGuard_Object = MibTableColumn
hwMstpProNewPortRootGuard = _HwMstpProNewPortRootGuard_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 29, 1, 23),
    _HwMstpProNewPortRootGuard_Type()
)
hwMstpProNewPortRootGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMstpProNewPortRootGuard.setStatus("current")


class _HwMstpProNewPortLoopGuard_Type(EnabledStatus):
    """Custom type hwMstpProNewPortLoopGuard based on EnabledStatus"""


_HwMstpProNewPortLoopGuard_Object = MibTableColumn
hwMstpProNewPortLoopGuard = _HwMstpProNewPortLoopGuard_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 29, 1, 24),
    _HwMstpProNewPortLoopGuard_Type()
)
hwMstpProNewPortLoopGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMstpProNewPortLoopGuard.setStatus("current")


class _HwMstpProNewPortCompliance_Type(Integer32):
    """Custom type hwMstpProNewPortCompliance based on Integer32"""
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
        *(("auto", 1),
          ("dotls", 2),
          ("legacy", 3))
    )


_HwMstpProNewPortCompliance_Type.__name__ = "Integer32"
_HwMstpProNewPortCompliance_Object = MibTableColumn
hwMstpProNewPortCompliance = _HwMstpProNewPortCompliance_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 29, 1, 25),
    _HwMstpProNewPortCompliance_Type()
)
hwMstpProNewPortCompliance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMstpProNewPortCompliance.setStatus("current")


class _HwMstpProNewPortConfigDigestSnooping_Type(EnabledStatus):
    """Custom type hwMstpProNewPortConfigDigestSnooping based on EnabledStatus"""


_HwMstpProNewPortConfigDigestSnooping_Object = MibTableColumn
hwMstpProNewPortConfigDigestSnooping = _HwMstpProNewPortConfigDigestSnooping_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 29, 1, 26),
    _HwMstpProNewPortConfigDigestSnooping_Type()
)
hwMstpProNewPortConfigDigestSnooping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMstpProNewPortConfigDigestSnooping.setStatus("current")


class _HwMstpProNewPortNoAgreementCheck_Type(EnabledStatus):
    """Custom type hwMstpProNewPortNoAgreementCheck based on EnabledStatus"""


_HwMstpProNewPortNoAgreementCheck_Object = MibTableColumn
hwMstpProNewPortNoAgreementCheck = _HwMstpProNewPortNoAgreementCheck_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 29, 1, 27),
    _HwMstpProNewPortNoAgreementCheck_Type()
)
hwMstpProNewPortNoAgreementCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMstpProNewPortNoAgreementCheck.setStatus("current")


class _HwMstpProNewPortVplsSubinterfaceEnable_Type(EnabledStatus):
    """Custom type hwMstpProNewPortVplsSubinterfaceEnable based on EnabledStatus"""


_HwMstpProNewPortVplsSubinterfaceEnable_Object = MibTableColumn
hwMstpProNewPortVplsSubinterfaceEnable = _HwMstpProNewPortVplsSubinterfaceEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 29, 1, 28),
    _HwMstpProNewPortVplsSubinterfaceEnable_Type()
)
hwMstpProNewPortVplsSubinterfaceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMstpProNewPortVplsSubinterfaceEnable.setStatus("current")


class _HwMstpProNewPortBpduEncapsulation_Type(Integer32):
    """Custom type hwMstpProNewPortBpduEncapsulation based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pvst", 1),
          ("stp", 2))
    )


_HwMstpProNewPortBpduEncapsulation_Type.__name__ = "Integer32"
_HwMstpProNewPortBpduEncapsulation_Object = MibTableColumn
hwMstpProNewPortBpduEncapsulation = _HwMstpProNewPortBpduEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 29, 1, 29),
    _HwMstpProNewPortBpduEncapsulation_Type()
)
hwMstpProNewPortBpduEncapsulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMstpProNewPortBpduEncapsulation.setStatus("current")


class _HwMstpProNewPortBpduFilter_Type(Integer32):
    """Custom type hwMstpProNewPortBpduFilter based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2),
          ("undo", 3))
    )


_HwMstpProNewPortBpduFilter_Type.__name__ = "Integer32"
_HwMstpProNewPortBpduFilter_Object = MibTableColumn
hwMstpProNewPortBpduFilter = _HwMstpProNewPortBpduFilter_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 29, 1, 30),
    _HwMstpProNewPortBpduFilter_Type()
)
hwMstpProNewPortBpduFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMstpProNewPortBpduFilter.setStatus("current")
_HwMstpProNewPortStpRXTC_Type = Counter32
_HwMstpProNewPortStpRXTC_Object = MibTableColumn
hwMstpProNewPortStpRXTC = _HwMstpProNewPortStpRXTC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 29, 1, 31),
    _HwMstpProNewPortStpRXTC_Type()
)
hwMstpProNewPortStpRXTC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMstpProNewPortStpRXTC.setStatus("current")
_HwMstpProNewPortStpTXTC_Type = Counter32
_HwMstpProNewPortStpTXTC_Object = MibTableColumn
hwMstpProNewPortStpTXTC = _HwMstpProNewPortStpTXTC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 29, 1, 32),
    _HwMstpProNewPortStpTXTC_Type()
)
hwMstpProNewPortStpTXTC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMstpProNewPortStpTXTC.setStatus("current")


class _HwMstpProNewPortRole_Type(Integer32):
    """Custom type hwMstpProNewPortRole based on Integer32"""
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
        *(("alternate", 2),
          ("backup", 3),
          ("designated", 5),
          ("disabled", 1),
          ("master", 6),
          ("root", 4))
    )


_HwMstpProNewPortRole_Type.__name__ = "Integer32"
_HwMstpProNewPortRole_Object = MibTableColumn
hwMstpProNewPortRole = _HwMstpProNewPortRole_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 29, 1, 33),
    _HwMstpProNewPortRole_Type()
)
hwMstpProNewPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMstpProNewPortRole.setStatus("current")
_HwMstpEdgedPortDefault_Type = HwMSTPEnabledStatus
_HwMstpEdgedPortDefault_Object = MibScalar
hwMstpEdgedPortDefault = _HwMstpEdgedPortDefault_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 30),
    _HwMstpEdgedPortDefault_Type()
)
hwMstpEdgedPortDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMstpEdgedPortDefault.setStatus("current")
_HwMstpBpduFilterPortDefault_Type = HwMSTPEnabledStatus
_HwMstpBpduFilterPortDefault_Object = MibScalar
hwMstpBpduFilterPortDefault = _HwMstpBpduFilterPortDefault_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 31),
    _HwMstpBpduFilterPortDefault_Type()
)
hwMstpBpduFilterPortDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMstpBpduFilterPortDefault.setStatus("current")


class _HwMstpTransmitLimitDefault_Type(Integer32):
    """Custom type hwMstpTransmitLimitDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HwMstpTransmitLimitDefault_Type.__name__ = "Integer32"
_HwMstpTransmitLimitDefault_Object = MibScalar
hwMstpTransmitLimitDefault = _HwMstpTransmitLimitDefault_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 1, 32),
    _HwMstpTransmitLimitDefault_Type()
)
hwMstpTransmitLimitDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMstpTransmitLimitDefault.setStatus("current")
_HwMstpTraps_ObjectIdentity = ObjectIdentity
hwMstpTraps = _HwMstpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 2)
)
if mibBuilder.loadTexts:
    hwMstpTraps.setStatus("current")
_HwMstpConformance_ObjectIdentity = ObjectIdentity
hwMstpConformance = _HwMstpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 3)
)
_HwMstpGroups_ObjectIdentity = ObjectIdentity
hwMstpGroups = _HwMstpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 3, 1)
)
_HwMstpCompliances_ObjectIdentity = ObjectIdentity
hwMstpCompliances = _HwMstpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 3, 2)
)

# Managed Objects groups

hwMstpBridgeInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 3, 1, 1)
)
hwMstpBridgeInfoGroup.setObjects(
      *(("HUAWEI-MSTP-MIB", "hwMstpStatus"),
        ("HUAWEI-MSTP-MIB", "hwMstpForceVersion"),
        ("HUAWEI-MSTP-MIB", "hwMstpDiameter"),
        ("HUAWEI-MSTP-MIB", "hwMstpBridgeMaxHops"),
        ("HUAWEI-MSTP-MIB", "hwMstpMasterBridgeID"),
        ("HUAWEI-MSTP-MIB", "hwMstpMasterPathCost"),
        ("HUAWEI-MSTP-MIB", "hwMstpBpduGuard"),
        ("HUAWEI-MSTP-MIB", "hwMstpAdminFormatSelector"),
        ("HUAWEI-MSTP-MIB", "hwMstpAdminRegionName"),
        ("HUAWEI-MSTP-MIB", "hwMstpAdminRevisionLevel"),
        ("HUAWEI-MSTP-MIB", "hwMstpOperFormatSelector"),
        ("HUAWEI-MSTP-MIB", "hwMstpOperRegionName"),
        ("HUAWEI-MSTP-MIB", "hwMstpOperRevisionLevel"),
        ("HUAWEI-MSTP-MIB", "hwMstpRegionConfActive"),
        ("HUAWEI-MSTP-MIB", "hwMstpDefaultVlanAllo"),
        ("HUAWEI-MSTP-MIB", "hwMstpDefaultRegionName"),
        ("HUAWEI-MSTP-MIB", "hwMstpPathCostStandard"),
        ("HUAWEI-MSTP-MIB", "hwMstpSnooping"),
        ("HUAWEI-MSTP-MIB", "hwMstpTcGuard"),
        ("HUAWEI-MSTP-MIB", "hwMstpTcGuardThreshold"),
        ("HUAWEI-MSTP-MIB", "hwMstpEdgedPortDefault"),
        ("HUAWEI-MSTP-MIB", "hwMstpBpduFilterPortDefault"),
        ("HUAWEI-MSTP-MIB", "hwMstpTransmitLimitDefault"))
)
if mibBuilder.loadTexts:
    hwMstpBridgeInfoGroup.setStatus("current")

hwMstpVlanInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 3, 1, 2)
)
hwMstpVlanInfoGroup.setObjects(
      *(("HUAWEI-MSTP-MIB", "hwMstpAdminMstID"),
        ("HUAWEI-MSTP-MIB", "hwMstpOperMstID"))
)
if mibBuilder.loadTexts:
    hwMstpVlanInfoGroup.setStatus("current")

hwMstpInstanceInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 3, 1, 3)
)
hwMstpInstanceInfoGroup.setObjects(
      *(("HUAWEI-MSTP-MIB", "hwMstpiBridgeID"),
        ("HUAWEI-MSTP-MIB", "hwMstpiBridgePriority"),
        ("HUAWEI-MSTP-MIB", "hwMstpiDesignedRoot"),
        ("HUAWEI-MSTP-MIB", "hwMstpiRootPathCost"),
        ("HUAWEI-MSTP-MIB", "hwMstpiRootPort"),
        ("HUAWEI-MSTP-MIB", "hwMstpiRootType"),
        ("HUAWEI-MSTP-MIB", "hwMstpiRemainingHops"),
        ("HUAWEI-MSTP-MIB", "hwMstpiAdminMappedVlanListLow"),
        ("HUAWEI-MSTP-MIB", "hwMstpiAdminMappedVlanListHigh"),
        ("HUAWEI-MSTP-MIB", "hwMstpiOperMappedVlanListLow"),
        ("HUAWEI-MSTP-MIB", "hwMstpiOperMappedVlanListHigh"),
        ("HUAWEI-MSTP-MIB", "hwMstpiRowStatus"))
)
if mibBuilder.loadTexts:
    hwMstpInstanceInfoGroup.setStatus("current")

hwMstpPortInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 3, 1, 4)
)
hwMstpPortInfoGroup.setObjects(
      *(("HUAWEI-MSTP-MIB", "hwMstpiState"),
        ("HUAWEI-MSTP-MIB", "hwMstpiPortPriority"),
        ("HUAWEI-MSTP-MIB", "hwMstpiPathCost"),
        ("HUAWEI-MSTP-MIB", "hwMstpiDesignatedRoot"),
        ("HUAWEI-MSTP-MIB", "hwMstpiDesignatedCost"),
        ("HUAWEI-MSTP-MIB", "hwMstpiDesignatedBridge"),
        ("HUAWEI-MSTP-MIB", "hwMstpiDesignatedPort"),
        ("HUAWEI-MSTP-MIB", "hwMstpiStpPortEdgeport"),
        ("HUAWEI-MSTP-MIB", "hwMstpiStpPortPointToPoint"),
        ("HUAWEI-MSTP-MIB", "hwMstpiStpMcheck"),
        ("HUAWEI-MSTP-MIB", "hwMstpiStpTransLimit"),
        ("HUAWEI-MSTP-MIB", "hwMstpiStpRXStpBPDU"),
        ("HUAWEI-MSTP-MIB", "hwMstpiStpTXStpBPDU"),
        ("HUAWEI-MSTP-MIB", "hwMstpiStpRXTCNBPDU"),
        ("HUAWEI-MSTP-MIB", "hwMstpiStpTXTCNBPDU"),
        ("HUAWEI-MSTP-MIB", "hwMstpiStpRXRSTPBPDU"),
        ("HUAWEI-MSTP-MIB", "hwMstpiStpTXRSTPBPDU"),
        ("HUAWEI-MSTP-MIB", "hwMstpiStpRXMSTPBPDU"),
        ("HUAWEI-MSTP-MIB", "hwMstpiStpTXMSTPBPDU"),
        ("HUAWEI-MSTP-MIB", "hwMstpiStpClearStatistics"),
        ("HUAWEI-MSTP-MIB", "hwMstpiStpDefaultPortCost"),
        ("HUAWEI-MSTP-MIB", "hwMstpiStpStatus"),
        ("HUAWEI-MSTP-MIB", "hwMstpiPortRootGuard"),
        ("HUAWEI-MSTP-MIB", "hwMstpiPortLoopGuard"),
        ("HUAWEI-MSTP-MIB", "hwMstpPortCompliance"),
        ("HUAWEI-MSTP-MIB", "hwMstpConfigDigestSnooping"),
        ("HUAWEI-MSTP-MIB", "hwMstpNoAgreementCheck"),
        ("HUAWEI-MSTP-MIB", "hwMstpPortTCNotify"),
        ("HUAWEI-MSTP-MIB", "hwMstpiStpPortBpduFilter"))
)
if mibBuilder.loadTexts:
    hwMstpPortInfoGroup.setStatus("current")

hwMstpAccessoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 3, 1, 5)
)
hwMstpAccessoryGroup.setObjects(
      *(("HUAWEI-MSTP-MIB", "hwMstpBackupReplyAgreement"),
        ("HUAWEI-MSTP-MIB", "hwMstpStpNoAgreementCheck"))
)
if mibBuilder.loadTexts:
    hwMstpAccessoryGroup.setStatus("current")

hwMstpProGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 3, 1, 7)
)
hwMstpProGroup.setObjects(
      *(("HUAWEI-MSTP-MIB", "hwMstpProStpState"),
        ("HUAWEI-MSTP-MIB", "hwMstpProPriority"),
        ("HUAWEI-MSTP-MIB", "hwMstpProRootType"),
        ("HUAWEI-MSTP-MIB", "hwMstpProForceVersion"),
        ("HUAWEI-MSTP-MIB", "hwMstpProBpduGuard"),
        ("HUAWEI-MSTP-MIB", "hwMstpProDiameter"),
        ("HUAWEI-MSTP-MIB", "hwMstpProConvergeMode"),
        ("HUAWEI-MSTP-MIB", "hwMstpProMaxHops"),
        ("HUAWEI-MSTP-MIB", "hwMstpProMCheck"),
        ("HUAWEI-MSTP-MIB", "hwMstpProPathCostStandard"),
        ("HUAWEI-MSTP-MIB", "hwMstpProHelloTime"),
        ("HUAWEI-MSTP-MIB", "hwMstpProFwdDelay"),
        ("HUAWEI-MSTP-MIB", "hwMstpProMaxAge"),
        ("HUAWEI-MSTP-MIB", "hwMstpProTimerFactor"),
        ("HUAWEI-MSTP-MIB", "hwMstpProTcGuard"),
        ("HUAWEI-MSTP-MIB", "hwMstpProTcGuardThreshold"),
        ("HUAWEI-MSTP-MIB", "hwMstpProTcNotifyProcess"),
        ("HUAWEI-MSTP-MIB", "hwMstpProRegionConfActive"),
        ("HUAWEI-MSTP-MIB", "hwMstpProRowStatus"),
        ("HUAWEI-MSTP-MIB", "hwMstpProLinkShareGuard"),
        ("HUAWEI-MSTP-MIB", "hwMstpConfigDegist"),
        ("HUAWEI-MSTP-MIB", "hwMstpProTcGuardInterval"))
)
if mibBuilder.loadTexts:
    hwMstpProGroup.setStatus("current")

hwMstpProPortInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 3, 1, 8)
)
hwMstpProPortInfoGroup.setObjects(
      *(("HUAWEI-MSTP-MIB", "hwMstpPortVlanListLow"),
        ("HUAWEI-MSTP-MIB", "hwMstpPortVlanListHigh"),
        ("HUAWEI-MSTP-MIB", "hwMstpProNewPortType"),
        ("HUAWEI-MSTP-MIB", "hwMstpProNewPortBpduVlan"),
        ("HUAWEI-MSTP-MIB", "hwMstpPortBindRowStatus"),
        ("HUAWEI-MSTP-MIB", "hwMstpProNewPortState"),
        ("HUAWEI-MSTP-MIB", "hwMstpProNewPortPriority"),
        ("HUAWEI-MSTP-MIB", "hwMstpProNewPortPathCost"),
        ("HUAWEI-MSTP-MIB", "hwMstpProNewPortDesignatedRoot"),
        ("HUAWEI-MSTP-MIB", "hwMstpProNewPortDesignatedCost"),
        ("HUAWEI-MSTP-MIB", "hwMstpProNewPortDesignatedBridge"),
        ("HUAWEI-MSTP-MIB", "hwMstpProNewPortDesignatedPort"),
        ("HUAWEI-MSTP-MIB", "hwMstpProNewPortStpEdgeport"),
        ("HUAWEI-MSTP-MIB", "hwMstpProNewPortStpPointToPoint"),
        ("HUAWEI-MSTP-MIB", "hwMstpProNewPortStpMcheck"),
        ("HUAWEI-MSTP-MIB", "hwMstpProNewPortStpTransLimit"),
        ("HUAWEI-MSTP-MIB", "hwMstpProNewPortStpRXStpBPDU"),
        ("HUAWEI-MSTP-MIB", "hwMstpProNewPortStpTXStpBPDU"),
        ("HUAWEI-MSTP-MIB", "hwMstpProNewPortStpRXTCNBPDU"),
        ("HUAWEI-MSTP-MIB", "hwMstpProNewPortStpTXTCNBPDU"),
        ("HUAWEI-MSTP-MIB", "hwMstpProNewPortStpRXRSTPBPDU"),
        ("HUAWEI-MSTP-MIB", "hwMstpProNewPortStpTXRSTPBPDU"),
        ("HUAWEI-MSTP-MIB", "hwMstpProNewPortStpRXMSTPBPDU"),
        ("HUAWEI-MSTP-MIB", "hwMstpProNewPortStpTXMSTPBPDU"),
        ("HUAWEI-MSTP-MIB", "hwMstpProNewPortStpClearStatistics"),
        ("HUAWEI-MSTP-MIB", "hwMstpProNewPortStpDefaultPortCost"),
        ("HUAWEI-MSTP-MIB", "hwMstpProNewPortStpStatus"),
        ("HUAWEI-MSTP-MIB", "hwMstpProNewPortRootGuard"),
        ("HUAWEI-MSTP-MIB", "hwMstpProNewPortLoopGuard"),
        ("HUAWEI-MSTP-MIB", "hwMstpProNewPortCompliance"),
        ("HUAWEI-MSTP-MIB", "hwMstpProNewPortConfigDigestSnooping"),
        ("HUAWEI-MSTP-MIB", "hwMstpProNewPortNoAgreementCheck"),
        ("HUAWEI-MSTP-MIB", "hwMstpProNewPortVplsSubinterfaceEnable"),
        ("HUAWEI-MSTP-MIB", "hwMstpProNewPortBpduEncapsulation"),
        ("HUAWEI-MSTP-MIB", "hwMstpProNewPortBpduFilter"),
        ("HUAWEI-MSTP-MIB", "hwMstpProNewPortStpRXTC"),
        ("HUAWEI-MSTP-MIB", "hwMstpProNewPortStpTXTC"))
)
if mibBuilder.loadTexts:
    hwMstpProPortInfoGroup.setStatus("current")

hwMstpProInstanceInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 3, 1, 10)
)
hwMstpProInstanceInfoGroup.setObjects(
      *(("HUAWEI-MSTP-MIB", "hwMstpProInstanceBridgeID"),
        ("HUAWEI-MSTP-MIB", "hwMstpProInstanceBridgePriority"),
        ("HUAWEI-MSTP-MIB", "hwMstpProInstanceDesignedRoot"),
        ("HUAWEI-MSTP-MIB", "hwMstpProInstanceRootPathCost"),
        ("HUAWEI-MSTP-MIB", "hwMstpProInstanceRootPort"),
        ("HUAWEI-MSTP-MIB", "hwMstpProInstanceRootType"),
        ("HUAWEI-MSTP-MIB", "hwMstpProInstanceRemainingHops"),
        ("HUAWEI-MSTP-MIB", "hwMstpProInstanceAdminMappedVlanListLow"),
        ("HUAWEI-MSTP-MIB", "hwMstpProInstanceAdminMappedVlanListHigh"),
        ("HUAWEI-MSTP-MIB", "hwMstpProInstanceOperMappedVlanListLow"),
        ("HUAWEI-MSTP-MIB", "hwMstpProInstanceOperMappedVlanListHigh"),
        ("HUAWEI-MSTP-MIB", "hwMstpProInstanceRowStatus"))
)
if mibBuilder.loadTexts:
    hwMstpProInstanceInfoGroup.setStatus("current")


# Notification objects

hwMstpiPortStateForwarding = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 2, 1)
)
hwMstpiPortStateForwarding.setObjects(
      *(("HUAWEI-MSTP-MIB", "hwMstpInstanceID"),
        ("HUAWEI-MSTP-MIB", "hwMstpiPortIndex"),
        ("IF-MIB", "ifName"))
)
if mibBuilder.loadTexts:
    hwMstpiPortStateForwarding.setStatus(
        "current"
    )

hwMstpiPortStateDiscarding = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 2, 2)
)
hwMstpiPortStateDiscarding.setObjects(
      *(("HUAWEI-MSTP-MIB", "hwMstpInstanceID"),
        ("HUAWEI-MSTP-MIB", "hwMstpiPortIndex"),
        ("IF-MIB", "ifName"))
)
if mibBuilder.loadTexts:
    hwMstpiPortStateDiscarding.setStatus(
        "current"
    )

hwMstpiBridgeLostRootPrimary = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 2, 3)
)
hwMstpiBridgeLostRootPrimary.setObjects(
    ("HUAWEI-MSTP-MIB", "hwMstpInstanceID")
)
if mibBuilder.loadTexts:
    hwMstpiBridgeLostRootPrimary.setStatus(
        "current"
    )

hwMstpiPortRootGuarded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 2, 4)
)
hwMstpiPortRootGuarded.setObjects(
      *(("HUAWEI-MSTP-MIB", "hwMstpInstanceID"),
        ("HUAWEI-MSTP-MIB", "hwMstpiPortIndex"),
        ("IF-MIB", "ifName"))
)
if mibBuilder.loadTexts:
    hwMstpiPortRootGuarded.setStatus(
        "current"
    )

hwMstpiPortBpduGuarded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 2, 5)
)
hwMstpiPortBpduGuarded.setObjects(
      *(("HUAWEI-MSTP-MIB", "hwMstpiPortIndex"),
        ("IF-MIB", "ifName"))
)
if mibBuilder.loadTexts:
    hwMstpiPortBpduGuarded.setStatus(
        "current"
    )

hwMstpiPortLoopGuarded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 2, 6)
)
hwMstpiPortLoopGuarded.setObjects(
      *(("HUAWEI-MSTP-MIB", "hwMstpInstanceID"),
        ("HUAWEI-MSTP-MIB", "hwMstpiPortIndex"),
        ("IF-MIB", "ifName"))
)
if mibBuilder.loadTexts:
    hwMstpiPortLoopGuarded.setStatus(
        "current"
    )

hwMstpiEdgePortChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 2, 7)
)
hwMstpiEdgePortChanged.setObjects(
      *(("HUAWEI-MSTP-MIB", "hwMstpiStpPortEdgeport"),
        ("IF-MIB", "ifName"))
)
if mibBuilder.loadTexts:
    hwMstpiEdgePortChanged.setStatus(
        "current"
    )

hwMstpProPortStateForwarding = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 2, 8)
)
hwMstpProPortStateForwarding.setObjects(
    ("HUAWEI-MSTP-MIB", "hwMstpProPortState")
)
if mibBuilder.loadTexts:
    hwMstpProPortStateForwarding.setStatus(
        "current"
    )

hwMstpProPortStateDiscarding = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 2, 9)
)
hwMstpProPortStateDiscarding.setObjects(
    ("HUAWEI-MSTP-MIB", "hwMstpProPortState")
)
if mibBuilder.loadTexts:
    hwMstpProPortStateDiscarding.setStatus(
        "current"
    )

hwMstpProBridgeLostRootPrimary = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 2, 10)
)
hwMstpProBridgeLostRootPrimary.setObjects(
    ("HUAWEI-MSTP-MIB", "hwMstpProPortState")
)
if mibBuilder.loadTexts:
    hwMstpProBridgeLostRootPrimary.setStatus(
        "current"
    )

hwMstpProPortRootGuarded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 2, 11)
)
hwMstpProPortRootGuarded.setObjects(
    ("HUAWEI-MSTP-MIB", "hwMstpProPortState")
)
if mibBuilder.loadTexts:
    hwMstpProPortRootGuarded.setStatus(
        "current"
    )

hwMstpProPortBpduGuarded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 2, 12)
)
hwMstpProPortBpduGuarded.setObjects(
    ("HUAWEI-MSTP-MIB", "hwMstpProPortState")
)
if mibBuilder.loadTexts:
    hwMstpProPortBpduGuarded.setStatus(
        "current"
    )

hwMstpProPortLoopGuarded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 2, 13)
)
hwMstpProPortLoopGuarded.setObjects(
    ("HUAWEI-MSTP-MIB", "hwMstpProPortState")
)
if mibBuilder.loadTexts:
    hwMstpProPortLoopGuarded.setStatus(
        "current"
    )

hwMstpProEdgePortChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 2, 14)
)
hwMstpProEdgePortChanged.setObjects(
    ("HUAWEI-MSTP-MIB", "hwMstpProPortStpEdgeport")
)
if mibBuilder.loadTexts:
    hwMstpProEdgePortChanged.setStatus(
        "current"
    )

hwMstpiTcGuarded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 2, 15)
)
hwMstpiTcGuarded.setObjects(
    ("HUAWEI-MSTP-MIB", "hwMstpiBridgePriority")
)
if mibBuilder.loadTexts:
    hwMstpiTcGuarded.setStatus(
        "current"
    )

hwMstpProTcGuarded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 2, 16)
)
hwMstpProTcGuarded.setObjects(
      *(("HUAWEI-MSTP-MIB", "hwMstpProTcGuard"),
        ("HUAWEI-MSTP-MIB", "hwMstpProInstanceBridgePriority"))
)
if mibBuilder.loadTexts:
    hwMstpProTcGuarded.setStatus(
        "current"
    )

hwMstpProRootChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 2, 17)
)
hwMstpProRootChanged.setObjects(
    ("HUAWEI-MSTP-MIB", "hwMstpProInstanceRootPort")
)
if mibBuilder.loadTexts:
    hwMstpProRootChanged.setStatus(
        "current"
    )

hwMstpProNewPortStateForwarding = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 2, 18)
)
hwMstpProNewPortStateForwarding.setObjects(
      *(("HUAWEI-MSTP-MIB", "hwMstpProNewPortState"),
        ("IF-MIB", "ifName"))
)
if mibBuilder.loadTexts:
    hwMstpProNewPortStateForwarding.setStatus(
        "current"
    )

hwMstpProNewPortStateDiscarding = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 2, 19)
)
hwMstpProNewPortStateDiscarding.setObjects(
      *(("HUAWEI-MSTP-MIB", "hwMstpProNewPortState"),
        ("IF-MIB", "ifName"))
)
if mibBuilder.loadTexts:
    hwMstpProNewPortStateDiscarding.setStatus(
        "current"
    )

hwMstpProNewBridgeLostRootPrimary = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 2, 20)
)
hwMstpProNewBridgeLostRootPrimary.setObjects(
    ("HUAWEI-MSTP-MIB", "hwMstpProInstanceRootType")
)
if mibBuilder.loadTexts:
    hwMstpProNewBridgeLostRootPrimary.setStatus(
        "current"
    )

hwMstpProNewPortRootGuarded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 2, 21)
)
hwMstpProNewPortRootGuarded.setObjects(
      *(("HUAWEI-MSTP-MIB", "hwMstpProNewPortState"),
        ("IF-MIB", "ifName"))
)
if mibBuilder.loadTexts:
    hwMstpProNewPortRootGuarded.setStatus(
        "current"
    )

hwMstpProNewPortBpduGuarded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 2, 22)
)
hwMstpProNewPortBpduGuarded.setObjects(
      *(("HUAWEI-MSTP-MIB", "hwMstpProNewPortState"),
        ("IF-MIB", "ifName"))
)
if mibBuilder.loadTexts:
    hwMstpProNewPortBpduGuarded.setStatus(
        "current"
    )

hwMstpProNewPortLoopGuarded = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 2, 23)
)
hwMstpProNewPortLoopGuarded.setObjects(
      *(("HUAWEI-MSTP-MIB", "hwMstpProNewPortState"),
        ("IF-MIB", "ifName"))
)
if mibBuilder.loadTexts:
    hwMstpProNewPortLoopGuarded.setStatus(
        "current"
    )

hwMstpProNewEdgePortChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 2, 24)
)
hwMstpProNewEdgePortChanged.setObjects(
      *(("HUAWEI-MSTP-MIB", "hwMstpProNewPortState"),
        ("IF-MIB", "ifName"))
)
if mibBuilder.loadTexts:
    hwMstpProNewEdgePortChanged.setStatus(
        "current"
    )

hwMstpProLoopbackDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 2, 25)
)
hwMstpProLoopbackDetected.setObjects(
      *(("HUAWEI-MSTP-MIB", "hwMstpProNewPortState"),
        ("IF-MIB", "ifName"))
)
if mibBuilder.loadTexts:
    hwMstpProLoopbackDetected.setStatus(
        "current"
    )


# Notifications groups

hwMstpNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 3, 1, 6)
)
hwMstpNotificationGroup.setObjects(
      *(("HUAWEI-MSTP-MIB", "hwMstpiPortStateForwarding"),
        ("HUAWEI-MSTP-MIB", "hwMstpiPortStateDiscarding"),
        ("HUAWEI-MSTP-MIB", "hwMstpiBridgeLostRootPrimary"),
        ("HUAWEI-MSTP-MIB", "hwMstpiPortRootGuarded"),
        ("HUAWEI-MSTP-MIB", "hwMstpiPortBpduGuarded"),
        ("HUAWEI-MSTP-MIB", "hwMstpiPortLoopGuarded"),
        ("HUAWEI-MSTP-MIB", "hwMstpiEdgePortChanged"),
        ("HUAWEI-MSTP-MIB", "hwMstpiTcGuarded"))
)
if mibBuilder.loadTexts:
    hwMstpNotificationGroup.setStatus(
        "current"
    )

hwMstpProNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 3, 1, 9)
)
hwMstpProNotificationGroup.setObjects(
      *(("HUAWEI-MSTP-MIB", "hwMstpProTcGuarded"),
        ("HUAWEI-MSTP-MIB", "hwMstpProRootChanged"),
        ("HUAWEI-MSTP-MIB", "hwMstpProNewPortStateForwarding"),
        ("HUAWEI-MSTP-MIB", "hwMstpProNewPortStateDiscarding"),
        ("HUAWEI-MSTP-MIB", "hwMstpProNewBridgeLostRootPrimary"),
        ("HUAWEI-MSTP-MIB", "hwMstpProNewPortRootGuarded"),
        ("HUAWEI-MSTP-MIB", "hwMstpProNewPortBpduGuarded"),
        ("HUAWEI-MSTP-MIB", "hwMstpProNewPortLoopGuarded"),
        ("HUAWEI-MSTP-MIB", "hwMstpProNewEdgePortChanged"))
)
if mibBuilder.loadTexts:
    hwMstpProNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwMstpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 42, 4, 3, 2, 1)
)
if mibBuilder.loadTexts:
    hwMstpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-MSTP-MIB",
    **{"HwMSTPEnabledStatus": HwMSTPEnabledStatus,
       "hwL2Mgmt": hwL2Mgmt,
       "hwMstp": hwMstp,
       "hwMstpObjects": hwMstpObjects,
       "hwMstpStatus": hwMstpStatus,
       "hwMstpForceVersion": hwMstpForceVersion,
       "hwMstpDiameter": hwMstpDiameter,
       "hwMstpBridgeMaxHops": hwMstpBridgeMaxHops,
       "hwMstpMasterBridgeID": hwMstpMasterBridgeID,
       "hwMstpMasterPathCost": hwMstpMasterPathCost,
       "hwMstpBpduGuard": hwMstpBpduGuard,
       "hwMstpAdminFormatSelector": hwMstpAdminFormatSelector,
       "hwMstpAdminRegionName": hwMstpAdminRegionName,
       "hwMstpAdminRevisionLevel": hwMstpAdminRevisionLevel,
       "hwMstpOperFormatSelector": hwMstpOperFormatSelector,
       "hwMstpOperRegionName": hwMstpOperRegionName,
       "hwMstpOperRevisionLevel": hwMstpOperRevisionLevel,
       "hwMstpRegionConfActive": hwMstpRegionConfActive,
       "hwMstpDefaultVlanAllo": hwMstpDefaultVlanAllo,
       "hwMstpDefaultRegionName": hwMstpDefaultRegionName,
       "hwMstpPathCostStandard": hwMstpPathCostStandard,
       "hwMstpVIDAllocationTable": hwMstpVIDAllocationTable,
       "hwMstpVIDAllocationEntry": hwMstpVIDAllocationEntry,
       "hwMstpVID": hwMstpVID,
       "hwMstpAdminMstID": hwMstpAdminMstID,
       "hwMstpOperMstID": hwMstpOperMstID,
       "hwMstpInstanceTable": hwMstpInstanceTable,
       "hwMstpInstanceEntry": hwMstpInstanceEntry,
       "hwMstpInstanceID": hwMstpInstanceID,
       "hwMstpiBridgeID": hwMstpiBridgeID,
       "hwMstpiBridgePriority": hwMstpiBridgePriority,
       "hwMstpiDesignedRoot": hwMstpiDesignedRoot,
       "hwMstpiRootPathCost": hwMstpiRootPathCost,
       "hwMstpiRootPort": hwMstpiRootPort,
       "hwMstpiRootType": hwMstpiRootType,
       "hwMstpiRemainingHops": hwMstpiRemainingHops,
       "hwMstpiAdminMappedVlanListLow": hwMstpiAdminMappedVlanListLow,
       "hwMstpiAdminMappedVlanListHigh": hwMstpiAdminMappedVlanListHigh,
       "hwMstpiOperMappedVlanListLow": hwMstpiOperMappedVlanListLow,
       "hwMstpiOperMappedVlanListHigh": hwMstpiOperMappedVlanListHigh,
       "hwMstpiRowStatus": hwMstpiRowStatus,
       "hwMstpPortTable": hwMstpPortTable,
       "hwMstpPortEntry": hwMstpPortEntry,
       "hwMstpiPortIndex": hwMstpiPortIndex,
       "hwMstpiState": hwMstpiState,
       "hwMstpiPortPriority": hwMstpiPortPriority,
       "hwMstpiPathCost": hwMstpiPathCost,
       "hwMstpiDesignatedRoot": hwMstpiDesignatedRoot,
       "hwMstpiDesignatedCost": hwMstpiDesignatedCost,
       "hwMstpiDesignatedBridge": hwMstpiDesignatedBridge,
       "hwMstpiDesignatedPort": hwMstpiDesignatedPort,
       "hwMstpiStpPortEdgeport": hwMstpiStpPortEdgeport,
       "hwMstpiStpPortPointToPoint": hwMstpiStpPortPointToPoint,
       "hwMstpiStpMcheck": hwMstpiStpMcheck,
       "hwMstpiStpTransLimit": hwMstpiStpTransLimit,
       "hwMstpiStpRXStpBPDU": hwMstpiStpRXStpBPDU,
       "hwMstpiStpTXStpBPDU": hwMstpiStpTXStpBPDU,
       "hwMstpiStpRXTCNBPDU": hwMstpiStpRXTCNBPDU,
       "hwMstpiStpTXTCNBPDU": hwMstpiStpTXTCNBPDU,
       "hwMstpiStpRXRSTPBPDU": hwMstpiStpRXRSTPBPDU,
       "hwMstpiStpTXRSTPBPDU": hwMstpiStpTXRSTPBPDU,
       "hwMstpiStpRXMSTPBPDU": hwMstpiStpRXMSTPBPDU,
       "hwMstpiStpTXMSTPBPDU": hwMstpiStpTXMSTPBPDU,
       "hwMstpiStpClearStatistics": hwMstpiStpClearStatistics,
       "hwMstpiStpDefaultPortCost": hwMstpiStpDefaultPortCost,
       "hwMstpiStpStatus": hwMstpiStpStatus,
       "hwMstpiPortRootGuard": hwMstpiPortRootGuard,
       "hwMstpiPortLoopGuard": hwMstpiPortLoopGuard,
       "hwMstpPortCompliance": hwMstpPortCompliance,
       "hwMstpConfigDigestSnooping": hwMstpConfigDigestSnooping,
       "hwMstpNoAgreementCheck": hwMstpNoAgreementCheck,
       "hwMstpPortTCNotify": hwMstpPortTCNotify,
       "hwMstpiStpPortBpduFilter": hwMstpiStpPortBpduFilter,
       "hwMstpiPortRole": hwMstpiPortRole,
       "hwMstpSnooping": hwMstpSnooping,
       "hwMstpAccessoryTable": hwMstpAccessoryTable,
       "hwMstpAccessoryEntry": hwMstpAccessoryEntry,
       "hwMstpAccessoryIndex": hwMstpAccessoryIndex,
       "hwMstpBackupReplyAgreement": hwMstpBackupReplyAgreement,
       "hwMstpStpNoAgreementCheck": hwMstpStpNoAgreementCheck,
       "hwMstpProTable": hwMstpProTable,
       "hwMstpProEntry": hwMstpProEntry,
       "hwMstpProID": hwMstpProID,
       "hwMstpProStpState": hwMstpProStpState,
       "hwMstpProPriority": hwMstpProPriority,
       "hwMstpProRootType": hwMstpProRootType,
       "hwMstpProForceVersion": hwMstpProForceVersion,
       "hwMstpProBpduGuard": hwMstpProBpduGuard,
       "hwMstpProDiameter": hwMstpProDiameter,
       "hwMstpProConvergeMode": hwMstpProConvergeMode,
       "hwMstpProMaxHops": hwMstpProMaxHops,
       "hwMstpProMCheck": hwMstpProMCheck,
       "hwMstpProPathCostStandard": hwMstpProPathCostStandard,
       "hwMstpProHelloTime": hwMstpProHelloTime,
       "hwMstpProFwdDelay": hwMstpProFwdDelay,
       "hwMstpProMaxAge": hwMstpProMaxAge,
       "hwMstpProTimerFactor": hwMstpProTimerFactor,
       "hwMstpProTCNotify": hwMstpProTCNotify,
       "hwMstpProNoLinkSharePortList": hwMstpProNoLinkSharePortList,
       "hwMstpProLinkSharePortList": hwMstpProLinkSharePortList,
       "hwMstpProTcGuard": hwMstpProTcGuard,
       "hwMstpProTcGuardThreshold": hwMstpProTcGuardThreshold,
       "hwMstpProTcNotifyProcess": hwMstpProTcNotifyProcess,
       "hwMstpProRegionConfActive": hwMstpProRegionConfActive,
       "hwMstpProLinkShareGuard": hwMstpProLinkShareGuard,
       "hwMstpConfigDegist": hwMstpConfigDegist,
       "hwMstpProRegionConfShare": hwMstpProRegionConfShare,
       "hwMstpProRowStatus": hwMstpProRowStatus,
       "hwMstpProTcGuardInterval": hwMstpProTcGuardInterval,
       "hwMstpPortBindTable": hwMstpPortBindTable,
       "hwMstpPortBindEntry": hwMstpPortBindEntry,
       "hwMstpPortId1": hwMstpPortId1,
       "hwMstpPortId2": hwMstpPortId2,
       "hwMstpPortId3": hwMstpPortId3,
       "hwMstpPortId4": hwMstpPortId4,
       "hwMstpPortIdFlag": hwMstpPortIdFlag,
       "hwMstpPortVlanListLow": hwMstpPortVlanListLow,
       "hwMstpPortVlanListHigh": hwMstpPortVlanListHigh,
       "hwMstpProNewPortType": hwMstpProNewPortType,
       "hwMstpProNewPortBpduVlan": hwMstpProNewPortBpduVlan,
       "hwMstpPortBindRowStatus": hwMstpPortBindRowStatus,
       "hwMstpProPortTable": hwMstpProPortTable,
       "hwMstpProPortEntry": hwMstpProPortEntry,
       "hwMstpProPortState": hwMstpProPortState,
       "hwMstpProPortPriority": hwMstpProPortPriority,
       "hwMstpProPortPathCost": hwMstpProPortPathCost,
       "hwMstpProPortDesignatedRoot": hwMstpProPortDesignatedRoot,
       "hwMstpProPortDesignatedCost": hwMstpProPortDesignatedCost,
       "hwMstpProPortDesignatedBridge": hwMstpProPortDesignatedBridge,
       "hwMstpProPortDesignatedPort": hwMstpProPortDesignatedPort,
       "hwMstpProPortStpEdgeport": hwMstpProPortStpEdgeport,
       "hwMstpProPortStpPointToPoint": hwMstpProPortStpPointToPoint,
       "hwMstpProPortStpMcheck": hwMstpProPortStpMcheck,
       "hwMstpProPortStpTransLimit": hwMstpProPortStpTransLimit,
       "hwMstpProPortStpRXStpBPDU": hwMstpProPortStpRXStpBPDU,
       "hwMstpProPortStpTXStpBPDU": hwMstpProPortStpTXStpBPDU,
       "hwMstpProPortStpRXTCNBPDU": hwMstpProPortStpRXTCNBPDU,
       "hwMstpProPortStpTXTCNBPDU": hwMstpProPortStpTXTCNBPDU,
       "hwMstpProPortStpRXRSTPBPDU": hwMstpProPortStpRXRSTPBPDU,
       "hwMstpProPortStpTXRSTPBPDU": hwMstpProPortStpTXRSTPBPDU,
       "hwMstpProPortStpRXMSTPBPDU": hwMstpProPortStpRXMSTPBPDU,
       "hwMstpProPortStpTXMSTPBPDU": hwMstpProPortStpTXMSTPBPDU,
       "hwMstpProPortStpClearStatistics": hwMstpProPortStpClearStatistics,
       "hwMstpProPortStpDefaultPortCost": hwMstpProPortStpDefaultPortCost,
       "hwMstpProPortStpStatus": hwMstpProPortStpStatus,
       "hwMstpProPortRootGuard": hwMstpProPortRootGuard,
       "hwMstpProPortLoopGuard": hwMstpProPortLoopGuard,
       "hwMstpProPortCompliance": hwMstpProPortCompliance,
       "hwMstpProPortConfigDigestSnooping": hwMstpProPortConfigDigestSnooping,
       "hwMstpProPortNoAgreementCheck": hwMstpProPortNoAgreementCheck,
       "hwMstpProPortTCNotify": hwMstpProPortTCNotify,
       "hwMstpProPortType": hwMstpProPortType,
       "hwMstpTcGuard": hwMstpTcGuard,
       "hwMstpTcGuardThreshold": hwMstpTcGuardThreshold,
       "hwMstpProInstanceTable": hwMstpProInstanceTable,
       "hwMstpProInstanceEntry": hwMstpProInstanceEntry,
       "hwMstpProInstanceBridgeID": hwMstpProInstanceBridgeID,
       "hwMstpProInstanceBridgePriority": hwMstpProInstanceBridgePriority,
       "hwMstpProInstanceDesignedRoot": hwMstpProInstanceDesignedRoot,
       "hwMstpProInstanceRootPathCost": hwMstpProInstanceRootPathCost,
       "hwMstpProInstanceRootPort": hwMstpProInstanceRootPort,
       "hwMstpProInstanceRootType": hwMstpProInstanceRootType,
       "hwMstpProInstanceRemainingHops": hwMstpProInstanceRemainingHops,
       "hwMstpProInstanceAdminMappedVlanListLow": hwMstpProInstanceAdminMappedVlanListLow,
       "hwMstpProInstanceAdminMappedVlanListHigh": hwMstpProInstanceAdminMappedVlanListHigh,
       "hwMstpProInstanceOperMappedVlanListLow": hwMstpProInstanceOperMappedVlanListLow,
       "hwMstpProInstanceOperMappedVlanListHigh": hwMstpProInstanceOperMappedVlanListHigh,
       "hwMstpProInstanceRowStatus": hwMstpProInstanceRowStatus,
       "hwMstpProNewPortTable": hwMstpProNewPortTable,
       "hwMstpProNewPortEntry": hwMstpProNewPortEntry,
       "hwMstpProNewPortState": hwMstpProNewPortState,
       "hwMstpProNewPortPriority": hwMstpProNewPortPriority,
       "hwMstpProNewPortPathCost": hwMstpProNewPortPathCost,
       "hwMstpProNewPortDesignatedRoot": hwMstpProNewPortDesignatedRoot,
       "hwMstpProNewPortDesignatedCost": hwMstpProNewPortDesignatedCost,
       "hwMstpProNewPortDesignatedBridge": hwMstpProNewPortDesignatedBridge,
       "hwMstpProNewPortDesignatedPort": hwMstpProNewPortDesignatedPort,
       "hwMstpProNewPortStpEdgeport": hwMstpProNewPortStpEdgeport,
       "hwMstpProNewPortStpPointToPoint": hwMstpProNewPortStpPointToPoint,
       "hwMstpProNewPortStpMcheck": hwMstpProNewPortStpMcheck,
       "hwMstpProNewPortStpTransLimit": hwMstpProNewPortStpTransLimit,
       "hwMstpProNewPortStpRXStpBPDU": hwMstpProNewPortStpRXStpBPDU,
       "hwMstpProNewPortStpTXStpBPDU": hwMstpProNewPortStpTXStpBPDU,
       "hwMstpProNewPortStpRXTCNBPDU": hwMstpProNewPortStpRXTCNBPDU,
       "hwMstpProNewPortStpTXTCNBPDU": hwMstpProNewPortStpTXTCNBPDU,
       "hwMstpProNewPortStpRXRSTPBPDU": hwMstpProNewPortStpRXRSTPBPDU,
       "hwMstpProNewPortStpTXRSTPBPDU": hwMstpProNewPortStpTXRSTPBPDU,
       "hwMstpProNewPortStpRXMSTPBPDU": hwMstpProNewPortStpRXMSTPBPDU,
       "hwMstpProNewPortStpTXMSTPBPDU": hwMstpProNewPortStpTXMSTPBPDU,
       "hwMstpProNewPortStpClearStatistics": hwMstpProNewPortStpClearStatistics,
       "hwMstpProNewPortStpDefaultPortCost": hwMstpProNewPortStpDefaultPortCost,
       "hwMstpProNewPortStpStatus": hwMstpProNewPortStpStatus,
       "hwMstpProNewPortRootGuard": hwMstpProNewPortRootGuard,
       "hwMstpProNewPortLoopGuard": hwMstpProNewPortLoopGuard,
       "hwMstpProNewPortCompliance": hwMstpProNewPortCompliance,
       "hwMstpProNewPortConfigDigestSnooping": hwMstpProNewPortConfigDigestSnooping,
       "hwMstpProNewPortNoAgreementCheck": hwMstpProNewPortNoAgreementCheck,
       "hwMstpProNewPortVplsSubinterfaceEnable": hwMstpProNewPortVplsSubinterfaceEnable,
       "hwMstpProNewPortBpduEncapsulation": hwMstpProNewPortBpduEncapsulation,
       "hwMstpProNewPortBpduFilter": hwMstpProNewPortBpduFilter,
       "hwMstpProNewPortStpRXTC": hwMstpProNewPortStpRXTC,
       "hwMstpProNewPortStpTXTC": hwMstpProNewPortStpTXTC,
       "hwMstpProNewPortRole": hwMstpProNewPortRole,
       "hwMstpEdgedPortDefault": hwMstpEdgedPortDefault,
       "hwMstpBpduFilterPortDefault": hwMstpBpduFilterPortDefault,
       "hwMstpTransmitLimitDefault": hwMstpTransmitLimitDefault,
       "hwMstpTraps": hwMstpTraps,
       "hwMstpiPortStateForwarding": hwMstpiPortStateForwarding,
       "hwMstpiPortStateDiscarding": hwMstpiPortStateDiscarding,
       "hwMstpiBridgeLostRootPrimary": hwMstpiBridgeLostRootPrimary,
       "hwMstpiPortRootGuarded": hwMstpiPortRootGuarded,
       "hwMstpiPortBpduGuarded": hwMstpiPortBpduGuarded,
       "hwMstpiPortLoopGuarded": hwMstpiPortLoopGuarded,
       "hwMstpiEdgePortChanged": hwMstpiEdgePortChanged,
       "hwMstpProPortStateForwarding": hwMstpProPortStateForwarding,
       "hwMstpProPortStateDiscarding": hwMstpProPortStateDiscarding,
       "hwMstpProBridgeLostRootPrimary": hwMstpProBridgeLostRootPrimary,
       "hwMstpProPortRootGuarded": hwMstpProPortRootGuarded,
       "hwMstpProPortBpduGuarded": hwMstpProPortBpduGuarded,
       "hwMstpProPortLoopGuarded": hwMstpProPortLoopGuarded,
       "hwMstpProEdgePortChanged": hwMstpProEdgePortChanged,
       "hwMstpiTcGuarded": hwMstpiTcGuarded,
       "hwMstpProTcGuarded": hwMstpProTcGuarded,
       "hwMstpProRootChanged": hwMstpProRootChanged,
       "hwMstpProNewPortStateForwarding": hwMstpProNewPortStateForwarding,
       "hwMstpProNewPortStateDiscarding": hwMstpProNewPortStateDiscarding,
       "hwMstpProNewBridgeLostRootPrimary": hwMstpProNewBridgeLostRootPrimary,
       "hwMstpProNewPortRootGuarded": hwMstpProNewPortRootGuarded,
       "hwMstpProNewPortBpduGuarded": hwMstpProNewPortBpduGuarded,
       "hwMstpProNewPortLoopGuarded": hwMstpProNewPortLoopGuarded,
       "hwMstpProNewEdgePortChanged": hwMstpProNewEdgePortChanged,
       "hwMstpProLoopbackDetected": hwMstpProLoopbackDetected,
       "hwMstpConformance": hwMstpConformance,
       "hwMstpGroups": hwMstpGroups,
       "hwMstpBridgeInfoGroup": hwMstpBridgeInfoGroup,
       "hwMstpVlanInfoGroup": hwMstpVlanInfoGroup,
       "hwMstpInstanceInfoGroup": hwMstpInstanceInfoGroup,
       "hwMstpPortInfoGroup": hwMstpPortInfoGroup,
       "hwMstpAccessoryGroup": hwMstpAccessoryGroup,
       "hwMstpNotificationGroup": hwMstpNotificationGroup,
       "hwMstpProGroup": hwMstpProGroup,
       "hwMstpProPortInfoGroup": hwMstpProPortInfoGroup,
       "hwMstpProNotificationGroup": hwMstpProNotificationGroup,
       "hwMstpProInstanceInfoGroup": hwMstpProInstanceInfoGroup,
       "hwMstpCompliances": hwMstpCompliances,
       "hwMstpCompliance": hwMstpCompliance}
)
