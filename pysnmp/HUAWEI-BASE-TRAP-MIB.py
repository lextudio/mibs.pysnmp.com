# SNMP MIB module (HUAWEI-BASE-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-BASE-TRAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:02:51 2024
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

(entPhysicalClass,
 entPhysicalContainedIn,
 entPhysicalIndex,
 entPhysicalName) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalClass",
    "entPhysicalContainedIn",
    "entPhysicalIndex",
    "entPhysicalName")

(hwStorageName,
 hwStorageSpace,
 hwStorageSpaceFree) = mibBuilder.importSymbols(
    "HUAWEI-FLASH-MAN-MIB",
    "hwStorageName",
    "hwStorageSpace",
    "hwStorageSpaceFree")

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

(IANAItuEventType,
 IANAItuProbableCause) = mibBuilder.importSymbols(
    "IANA-ITU-ALARM-TC-MIB",
    "IANAItuEventType",
    "IANAItuProbableCause")

(ifAdminStatus,
 ifDescr,
 ifIndex,
 ifName,
 ifOperStatus) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifAdminStatus",
    "ifDescr",
    "ifIndex",
    "ifName",
    "ifOperStatus")

(ItuPerceivedSeverity,) = mibBuilder.importSymbols(
    "ITU-ALARM-TC-MIB",
    "ItuPerceivedSeverity")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

hwBaseTrapMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129)
)
hwBaseTrapMIB.setRevisions(
        ("2015-06-02 14:11",
         "2014-10-13 14:11",
         "2014-10-09 14:11",
         "2014-09-01 14:11",
         "2013-06-25 14:11",
         "2013-05-24 00:00",
         "2007-01-17 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwBaseTrapObject_ObjectIdentity = ObjectIdentity
hwBaseTrapObject = _HwBaseTrapObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 1)
)
_HwBaseTrapSeverity_Type = ItuPerceivedSeverity
_HwBaseTrapSeverity_Object = MibScalar
hwBaseTrapSeverity = _HwBaseTrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 1, 1),
    _HwBaseTrapSeverity_Type()
)
hwBaseTrapSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwBaseTrapSeverity.setStatus("current")
_HwBaseTrapProbableCause_Type = IANAItuProbableCause
_HwBaseTrapProbableCause_Object = MibScalar
hwBaseTrapProbableCause = _HwBaseTrapProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 1, 2),
    _HwBaseTrapProbableCause_Type()
)
hwBaseTrapProbableCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwBaseTrapProbableCause.setStatus("current")
_HwBaseTrapEventType_Type = IANAItuEventType
_HwBaseTrapEventType_Object = MibScalar
hwBaseTrapEventType = _HwBaseTrapEventType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 1, 3),
    _HwBaseTrapEventType_Type()
)
hwBaseTrapEventType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwBaseTrapEventType.setStatus("current")
_HwBaseTrapRelativeResource_Type = DisplayString
_HwBaseTrapRelativeResource_Object = MibScalar
hwBaseTrapRelativeResource = _HwBaseTrapRelativeResource_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 1, 4),
    _HwBaseTrapRelativeResource_Type()
)
hwBaseTrapRelativeResource.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwBaseTrapRelativeResource.setStatus("current")
_HwBaseTrapReasonDescr_Type = DisplayString
_HwBaseTrapReasonDescr_Object = MibScalar
hwBaseTrapReasonDescr = _HwBaseTrapReasonDescr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 1, 5),
    _HwBaseTrapReasonDescr_Type()
)
hwBaseTrapReasonDescr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwBaseTrapReasonDescr.setStatus("current")
_HwBaseThresholdTable_Object = MibTable
hwBaseThresholdTable = _HwBaseThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 1, 6)
)
if mibBuilder.loadTexts:
    hwBaseThresholdTable.setStatus("current")
_HwBaseThresholdEntry_Object = MibTableRow
hwBaseThresholdEntry = _HwBaseThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 1, 6, 1)
)
hwBaseThresholdEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdType"),
    (0, "HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdIndex"),
)
if mibBuilder.loadTexts:
    hwBaseThresholdEntry.setStatus("current")


class _HwBaseThresholdType_Type(Integer32):
    """Custom type hwBaseThresholdType based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("currentSensor", 4),
          ("humiditySensor", 2),
          ("portBroadcast", 8),
          ("portCrcError", 7),
          ("portTraffic", 6),
          ("powerSensor", 5),
          ("temperatureSensor", 1),
          ("voltageSensor", 3))
    )


_HwBaseThresholdType_Type.__name__ = "Integer32"
_HwBaseThresholdType_Object = MibTableColumn
hwBaseThresholdType = _HwBaseThresholdType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 1, 6, 1, 1),
    _HwBaseThresholdType_Type()
)
hwBaseThresholdType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBaseThresholdType.setStatus("current")


class _HwBaseThresholdIndex_Type(Integer32):
    """Custom type hwBaseThresholdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwBaseThresholdIndex_Type.__name__ = "Integer32"
_HwBaseThresholdIndex_Object = MibTableColumn
hwBaseThresholdIndex = _HwBaseThresholdIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 1, 6, 1, 2),
    _HwBaseThresholdIndex_Type()
)
hwBaseThresholdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBaseThresholdIndex.setStatus("current")
_HwBaseThresholdValue_Type = Integer32
_HwBaseThresholdValue_Object = MibTableColumn
hwBaseThresholdValue = _HwBaseThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 1, 6, 1, 3),
    _HwBaseThresholdValue_Type()
)
hwBaseThresholdValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBaseThresholdValue.setStatus("current")


class _HwBaseThresholdUnit_Type(Integer32):
    """Custom type hwBaseThresholdUnit based on Integer32"""
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
        *(("centigrade1", 2),
          ("centigrade2", 3),
          ("current1", 6),
          ("current2", 7),
          ("percentage", 1),
          ("power1", 8),
          ("power2", 9),
          ("voltage1", 4),
          ("voltage2", 5))
    )


_HwBaseThresholdUnit_Type.__name__ = "Integer32"
_HwBaseThresholdUnit_Object = MibTableColumn
hwBaseThresholdUnit = _HwBaseThresholdUnit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 1, 6, 1, 4),
    _HwBaseThresholdUnit_Type()
)
hwBaseThresholdUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBaseThresholdUnit.setStatus("current")
_HwBaseThresholdLowCritical_Type = Integer32
_HwBaseThresholdLowCritical_Object = MibTableColumn
hwBaseThresholdLowCritical = _HwBaseThresholdLowCritical_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 1, 6, 1, 5),
    _HwBaseThresholdLowCritical_Type()
)
hwBaseThresholdLowCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBaseThresholdLowCritical.setStatus("current")
_HwBaseThresholdLowWarning_Type = Integer32
_HwBaseThresholdLowWarning_Object = MibTableColumn
hwBaseThresholdLowWarning = _HwBaseThresholdLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 1, 6, 1, 6),
    _HwBaseThresholdLowWarning_Type()
)
hwBaseThresholdLowWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBaseThresholdLowWarning.setStatus("current")
_HwBaseThresholdHighWarning_Type = Integer32
_HwBaseThresholdHighWarning_Object = MibTableColumn
hwBaseThresholdHighWarning = _HwBaseThresholdHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 1, 6, 1, 7),
    _HwBaseThresholdHighWarning_Type()
)
hwBaseThresholdHighWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBaseThresholdHighWarning.setStatus("current")
_HwBaseThresholdHighCritical_Type = Integer32
_HwBaseThresholdHighCritical_Object = MibTableColumn
hwBaseThresholdHighCritical = _HwBaseThresholdHighCritical_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 1, 6, 1, 8),
    _HwBaseThresholdHighCritical_Type()
)
hwBaseThresholdHighCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBaseThresholdHighCritical.setStatus("current")
_HwBaseUsageTable_Object = MibTable
hwBaseUsageTable = _HwBaseUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 1, 7)
)
if mibBuilder.loadTexts:
    hwBaseUsageTable.setStatus("current")
_HwBaseUsageEntry_Object = MibTableRow
hwBaseUsageEntry = _HwBaseUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 1, 7, 1)
)
hwBaseUsageEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "HUAWEI-BASE-TRAP-MIB", "hwBaseUsageType"),
    (0, "HUAWEI-BASE-TRAP-MIB", "hwBaseUsageIndex"),
)
if mibBuilder.loadTexts:
    hwBaseUsageEntry.setStatus("current")


class _HwBaseUsageType_Type(Integer32):
    """Custom type hwBaseUsageType based on Integer32"""
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
        *(("cfCardUtilization", 5),
          ("cpuUtilization", 1),
          ("diskUtilizatino", 3),
          ("flashUtilizatino", 4),
          ("memoryUtilization", 2))
    )


_HwBaseUsageType_Type.__name__ = "Integer32"
_HwBaseUsageType_Object = MibTableColumn
hwBaseUsageType = _HwBaseUsageType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 1, 7, 1, 1),
    _HwBaseUsageType_Type()
)
hwBaseUsageType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBaseUsageType.setStatus("current")


class _HwBaseUsageIndex_Type(Integer32):
    """Custom type hwBaseUsageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwBaseUsageIndex_Type.__name__ = "Integer32"
_HwBaseUsageIndex_Object = MibTableColumn
hwBaseUsageIndex = _HwBaseUsageIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 1, 7, 1, 2),
    _HwBaseUsageIndex_Type()
)
hwBaseUsageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBaseUsageIndex.setStatus("current")
_HwBaseUsageValue_Type = Integer32
_HwBaseUsageValue_Object = MibTableColumn
hwBaseUsageValue = _HwBaseUsageValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 1, 7, 1, 3),
    _HwBaseUsageValue_Type()
)
hwBaseUsageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBaseUsageValue.setStatus("current")


class _HwBaseUsageUnit_Type(Integer32):
    """Custom type hwBaseUsageUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("percentage", 1)
    )


_HwBaseUsageUnit_Type.__name__ = "Integer32"
_HwBaseUsageUnit_Object = MibTableColumn
hwBaseUsageUnit = _HwBaseUsageUnit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 1, 7, 1, 4),
    _HwBaseUsageUnit_Type()
)
hwBaseUsageUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBaseUsageUnit.setStatus("current")
_HwBaseUsageThreshold_Type = Integer32
_HwBaseUsageThreshold_Object = MibTableColumn
hwBaseUsageThreshold = _HwBaseUsageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 1, 7, 1, 5),
    _HwBaseUsageThreshold_Type()
)
hwBaseUsageThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBaseUsageThreshold.setStatus("current")


class _HwFIBOverloadModule_Type(Integer32):
    """Custom type hwFIBOverloadModule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_HwFIBOverloadModule_Type.__name__ = "Integer32"
_HwFIBOverloadModule_Object = MibScalar
hwFIBOverloadModule = _HwFIBOverloadModule_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 1, 8),
    _HwFIBOverloadModule_Type()
)
hwFIBOverloadModule.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwFIBOverloadModule.setStatus("current")


class _HwBaseFlowDirectionType_Type(Integer32):
    """Custom type hwBaseFlowDirectionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )


_HwBaseFlowDirectionType_Type.__name__ = "Integer32"
_HwBaseFlowDirectionType_Object = MibScalar
hwBaseFlowDirectionType = _HwBaseFlowDirectionType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 1, 9),
    _HwBaseFlowDirectionType_Type()
)
hwBaseFlowDirectionType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwBaseFlowDirectionType.setStatus("current")


class _HwPowerDirection_Type(Integer32):
    """Custom type hwPowerDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )


_HwPowerDirection_Type.__name__ = "Integer32"
_HwPowerDirection_Object = MibScalar
hwPowerDirection = _HwPowerDirection_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 1, 10),
    _HwPowerDirection_Type()
)
hwPowerDirection.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwPowerDirection.setStatus("current")


class _HwBaseTrapTrafficDir_Type(Integer32):
    """Custom type hwBaseTrapTrafficDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("trafficIn", 1),
          ("trafficOut", 2))
    )


_HwBaseTrapTrafficDir_Type.__name__ = "Integer32"
_HwBaseTrapTrafficDir_Object = MibScalar
hwBaseTrapTrafficDir = _HwBaseTrapTrafficDir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 1, 11),
    _HwBaseTrapTrafficDir_Type()
)
hwBaseTrapTrafficDir.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwBaseTrapTrafficDir.setStatus("current")
_HwEntityRatedPower_Type = Integer32
_HwEntityRatedPower_Object = MibScalar
hwEntityRatedPower = _HwEntityRatedPower_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 1, 12),
    _HwEntityRatedPower_Type()
)
hwEntityRatedPower.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwEntityRatedPower.setStatus("current")
_HwDevAvailablePower_Type = Integer32
_HwDevAvailablePower_Object = MibScalar
hwDevAvailablePower = _HwDevAvailablePower_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 1, 13),
    _HwDevAvailablePower_Type()
)
hwDevAvailablePower.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwDevAvailablePower.setStatus("current")
_HwDeviceTotalPower_Type = Integer32
_HwDeviceTotalPower_Object = MibScalar
hwDeviceTotalPower = _HwDeviceTotalPower_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 1, 14),
    _HwDeviceTotalPower_Type()
)
hwDeviceTotalPower.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwDeviceTotalPower.setStatus("current")
_HwBaseTrapCurPortType_Type = Integer32
_HwBaseTrapCurPortType_Object = MibScalar
hwBaseTrapCurPortType = _HwBaseTrapCurPortType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 1, 15),
    _HwBaseTrapCurPortType_Type()
)
hwBaseTrapCurPortType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwBaseTrapCurPortType.setStatus("current")
_HwBaseTrapLastPortType_Type = Integer32
_HwBaseTrapLastPortType_Object = MibScalar
hwBaseTrapLastPortType = _HwBaseTrapLastPortType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 1, 16),
    _HwBaseTrapLastPortType_Type()
)
hwBaseTrapLastPortType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwBaseTrapLastPortType.setStatus("current")
_HwPortPhysicalDownReason_Type = OctetString
_HwPortPhysicalDownReason_Object = MibScalar
hwPortPhysicalDownReason = _HwPortPhysicalDownReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 1, 17),
    _HwPortPhysicalDownReason_Type()
)
hwPortPhysicalDownReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwPortPhysicalDownReason.setStatus("current")
_HwBaseTraps_ObjectIdentity = ObjectIdentity
hwBaseTraps = _HwBaseTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2)
)
_HwEntityTrap_ObjectIdentity = ObjectIdentity
hwEntityTrap = _HwEntityTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 1)
)
_HwEnvironmentTrap_ObjectIdentity = ObjectIdentity
hwEnvironmentTrap = _HwEnvironmentTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 2)
)
_HwPowerTrap_ObjectIdentity = ObjectIdentity
hwPowerTrap = _HwPowerTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 3)
)
_HwCPUTrap_ObjectIdentity = ObjectIdentity
hwCPUTrap = _HwCPUTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 4)
)
_HwPortTrap_ObjectIdentity = ObjectIdentity
hwPortTrap = _HwPortTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 5)
)
_HwStorageTrap_ObjectIdentity = ObjectIdentity
hwStorageTrap = _HwStorageTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 6)
)
_HwClockTrap_ObjectIdentity = ObjectIdentity
hwClockTrap = _HwClockTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 7)
)
_HwFanTrap_ObjectIdentity = ObjectIdentity
hwFanTrap = _HwFanTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 8)
)
_HwFibTrap_ObjectIdentity = ObjectIdentity
hwFibTrap = _HwFibTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 9)
)
_HwPppTrap_ObjectIdentity = ObjectIdentity
hwPppTrap = _HwPppTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 10)
)
_HwFlowControlTrap_ObjectIdentity = ObjectIdentity
hwFlowControlTrap = _HwFlowControlTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 11)
)
_HwDeviceAbnormalTrap_ObjectIdentity = ObjectIdentity
hwDeviceAbnormalTrap = _HwDeviceAbnormalTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 12)
)
_HwResExhaustBfdTrap_ObjectIdentity = ObjectIdentity
hwResExhaustBfdTrap = _HwResExhaustBfdTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 13)
)
_HwResExhaustOamTrap_ObjectIdentity = ObjectIdentity
hwResExhaustOamTrap = _HwResExhaustOamTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 14)
)
_HwHdlcTrap_ObjectIdentity = ObjectIdentity
hwHdlcTrap = _HwHdlcTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 15)
)
_HwAutoFtpTrap_ObjectIdentity = ObjectIdentity
hwAutoFtpTrap = _HwAutoFtpTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 16)
)
_HwBaseOpticalTrap_ObjectIdentity = ObjectIdentity
hwBaseOpticalTrap = _HwBaseOpticalTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 17)
)
_HwBaseTrapConformance_ObjectIdentity = ObjectIdentity
hwBaseTrapConformance = _HwBaseTrapConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 3)
)
_HwBaseTrapCompliances_ObjectIdentity = ObjectIdentity
hwBaseTrapCompliances = _HwBaseTrapCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 3, 1)
)
_HwBaseTrapGroups_ObjectIdentity = ObjectIdentity
hwBaseTrapGroups = _HwBaseTrapGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 3, 2)
)

# Managed Objects groups

hwBaseObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 3, 2, 1)
)
hwBaseObjectGroup.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdValue"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdUnit"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdLowCritical"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdLowWarning"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdHighWarning"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdHighCritical"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseUsageValue"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseUsageUnit"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseUsageThreshold"),
        ("HUAWEI-BASE-TRAP-MIB", "hwDevAvailablePower"),
        ("HUAWEI-BASE-TRAP-MIB", "hwEntityRatedPower"),
        ("HUAWEI-BASE-TRAP-MIB", "hwDeviceTotalPower"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapLastPortType"),
        ("HUAWEI-BASE-TRAP-MIB", "hwPortPhysicalDownReason"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapCurPortType"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapReasonDescr"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapRelativeResource"),
        ("HUAWEI-BASE-TRAP-MIB", "hwFIBOverloadModule"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseFlowDirectionType"),
        ("HUAWEI-BASE-TRAP-MIB", "hwPowerDirection"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapTrafficDir"))
)
if mibBuilder.loadTexts:
    hwBaseObjectGroup.setStatus("current")


# Notification objects

hwEntityRemove = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 1, 1)
)
hwEntityRemove.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("ENTITY-MIB", "entPhysicalContainedIn"),
        ("ENTITY-MIB", "entPhysicalName"))
)
if mibBuilder.loadTexts:
    hwEntityRemove.setStatus(
        "current"
    )

hwEntityInsert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 1, 2)
)
hwEntityInsert.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("ENTITY-MIB", "entPhysicalContainedIn"),
        ("ENTITY-MIB", "entPhysicalName"))
)
if mibBuilder.loadTexts:
    hwEntityInsert.setStatus(
        "current"
    )

hwEntityUnstable = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 1, 3)
)
hwEntityUnstable.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("ENTITY-MIB", "entPhysicalContainedIn"),
        ("ENTITY-MIB", "entPhysicalName"))
)
if mibBuilder.loadTexts:
    hwEntityUnstable.setStatus(
        "current"
    )

hwEntityUnstableResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 1, 4)
)
hwEntityUnstableResume.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("ENTITY-MIB", "entPhysicalContainedIn"),
        ("ENTITY-MIB", "entPhysicalName"))
)
if mibBuilder.loadTexts:
    hwEntityUnstableResume.setStatus(
        "current"
    )

hwEntityReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 1, 5)
)
hwEntityReset.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("ENTITY-MIB", "entPhysicalContainedIn"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapRelativeResource"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapReasonDescr"))
)
if mibBuilder.loadTexts:
    hwEntityReset.setStatus(
        "current"
    )

hwEntityResetDone = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 1, 6)
)
hwEntityResetDone.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("ENTITY-MIB", "entPhysicalContainedIn"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapRelativeResource"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapReasonDescr"))
)
if mibBuilder.loadTexts:
    hwEntityResetDone.setStatus(
        "current"
    )

hwEntityCommunicateError = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 1, 7)
)
hwEntityCommunicateError.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("ENTITY-MIB", "entPhysicalContainedIn"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapRelativeResource"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapReasonDescr"))
)
if mibBuilder.loadTexts:
    hwEntityCommunicateError.setStatus(
        "current"
    )

hwEntityCommunicateResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 1, 8)
)
hwEntityCommunicateResume.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("ENTITY-MIB", "entPhysicalContainedIn"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapRelativeResource"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapReasonDescr"))
)
if mibBuilder.loadTexts:
    hwEntityCommunicateResume.setStatus(
        "current"
    )

hwEntityInvalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 1, 9)
)
hwEntityInvalid.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("ENTITY-MIB", "entPhysicalContainedIn"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapRelativeResource"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapReasonDescr"))
)
if mibBuilder.loadTexts:
    hwEntityInvalid.setStatus(
        "current"
    )

hwEntityResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 1, 10)
)
hwEntityResume.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("ENTITY-MIB", "entPhysicalContainedIn"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapRelativeResource"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapReasonDescr"))
)
if mibBuilder.loadTexts:
    hwEntityResume.setStatus(
        "current"
    )

hwEntityLeaveMaster = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 1, 11)
)
hwEntityLeaveMaster.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("ENTITY-MIB", "entPhysicalContainedIn"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapRelativeResource"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapReasonDescr"))
)
if mibBuilder.loadTexts:
    hwEntityLeaveMaster.setStatus(
        "current"
    )

hwEntityBecomeMaster = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 1, 12)
)
hwEntityBecomeMaster.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("ENTITY-MIB", "entPhysicalContainedIn"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapRelativeResource"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapReasonDescr"))
)
if mibBuilder.loadTexts:
    hwEntityBecomeMaster.setStatus(
        "current"
    )

hwEntityOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 1, 13)
)
hwEntityOffline.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("ENTITY-MIB", "entPhysicalContainedIn"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapRelativeResource"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapReasonDescr"))
)
if mibBuilder.loadTexts:
    hwEntityOffline.setStatus(
        "current"
    )

hwEntityOnline = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 1, 14)
)
hwEntityOnline.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("ENTITY-MIB", "entPhysicalContainedIn"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapRelativeResource"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapReasonDescr"))
)
if mibBuilder.loadTexts:
    hwEntityOnline.setStatus(
        "current"
    )

hwEntityCheckFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 1, 15)
)
hwEntityCheckFail.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("ENTITY-MIB", "entPhysicalContainedIn"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapRelativeResource"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapReasonDescr"))
)
if mibBuilder.loadTexts:
    hwEntityCheckFail.setStatus(
        "current"
    )

hwEntityCheckResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 1, 16)
)
hwEntityCheckResume.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("ENTITY-MIB", "entPhysicalContainedIn"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapRelativeResource"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapReasonDescr"))
)
if mibBuilder.loadTexts:
    hwEntityCheckResume.setStatus(
        "current"
    )

hwEntityRegFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 1, 17)
)
hwEntityRegFail.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("ENTITY-MIB", "entPhysicalContainedIn"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapRelativeResource"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapReasonDescr"))
)
if mibBuilder.loadTexts:
    hwEntityRegFail.setStatus(
        "current"
    )

hwEntityRegSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 1, 18)
)
hwEntityRegSuccess.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("ENTITY-MIB", "entPhysicalContainedIn"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapRelativeResource"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapReasonDescr"))
)
if mibBuilder.loadTexts:
    hwEntityRegSuccess.setStatus(
        "current"
    )

hwEntityDyingGasp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 1, 19)
)
hwEntityDyingGasp.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapRelativeResource"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapReasonDescr"))
)
if mibBuilder.loadTexts:
    hwEntityDyingGasp.setStatus(
        "current"
    )

hwTempRisingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 2, 1)
)
hwTempRisingAlarm.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdValue"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdUnit"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdHighWarning"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdHighCritical"))
)
if mibBuilder.loadTexts:
    hwTempRisingAlarm.setStatus(
        "current"
    )

hwTempRisingResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 2, 2)
)
hwTempRisingResume.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdValue"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdUnit"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdHighWarning"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdHighCritical"))
)
if mibBuilder.loadTexts:
    hwTempRisingResume.setStatus(
        "current"
    )

hwTempFallingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 2, 3)
)
hwTempFallingAlarm.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdValue"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdUnit"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdLowCritical"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdLowWarning"))
)
if mibBuilder.loadTexts:
    hwTempFallingAlarm.setStatus(
        "current"
    )

hwTempFallingResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 2, 4)
)
hwTempFallingResume.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdValue"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdUnit"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdLowCritical"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdLowWarning"))
)
if mibBuilder.loadTexts:
    hwTempFallingResume.setStatus(
        "current"
    )

hwHumidityRisingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 2, 5)
)
hwHumidityRisingAlarm.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdValue"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdUnit"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdHighWarning"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdHighCritical"))
)
if mibBuilder.loadTexts:
    hwHumidityRisingAlarm.setStatus(
        "current"
    )

hwHumidityRisingResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 2, 6)
)
hwHumidityRisingResume.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdValue"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdUnit"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdHighWarning"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdHighCritical"))
)
if mibBuilder.loadTexts:
    hwHumidityRisingResume.setStatus(
        "current"
    )

hwHumidityFallingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 2, 7)
)
hwHumidityFallingAlarm.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdValue"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdUnit"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdLowCritical"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdLowWarning"))
)
if mibBuilder.loadTexts:
    hwHumidityFallingAlarm.setStatus(
        "current"
    )

hwHumidityFallingResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 2, 8)
)
hwHumidityFallingResume.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdValue"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdUnit"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdLowCritical"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdLowWarning"))
)
if mibBuilder.loadTexts:
    hwHumidityFallingResume.setStatus(
        "current"
    )

hwVoltRisingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 2, 9)
)
hwVoltRisingAlarm.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdValue"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdUnit"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdHighWarning"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdHighCritical"))
)
if mibBuilder.loadTexts:
    hwVoltRisingAlarm.setStatus(
        "current"
    )

hwVoltRisingResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 2, 10)
)
hwVoltRisingResume.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdValue"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdUnit"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdHighWarning"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdHighCritical"))
)
if mibBuilder.loadTexts:
    hwVoltRisingResume.setStatus(
        "current"
    )

hwVoltFallingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 2, 11)
)
hwVoltFallingAlarm.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdValue"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdUnit"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdLowCritical"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdLowWarning"))
)
if mibBuilder.loadTexts:
    hwVoltFallingAlarm.setStatus(
        "current"
    )

hwVoltFallingResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 2, 12)
)
hwVoltFallingResume.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdValue"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdUnit"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdLowCritical"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdLowWarning"))
)
if mibBuilder.loadTexts:
    hwVoltFallingResume.setStatus(
        "current"
    )

hwCurrentRisingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 2, 13)
)
hwCurrentRisingAlarm.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdValue"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdUnit"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdHighWarning"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdHighCritical"))
)
if mibBuilder.loadTexts:
    hwCurrentRisingAlarm.setStatus(
        "current"
    )

hwCurrentRisingResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 2, 14)
)
hwCurrentRisingResume.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdValue"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdUnit"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdHighWarning"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdHighCritical"))
)
if mibBuilder.loadTexts:
    hwCurrentRisingResume.setStatus(
        "current"
    )

hwCurrentFallingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 2, 15)
)
hwCurrentFallingAlarm.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdValue"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdUnit"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdLowCritical"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdLowWarning"))
)
if mibBuilder.loadTexts:
    hwCurrentFallingAlarm.setStatus(
        "current"
    )

hwCurrentFallingResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 2, 16)
)
hwCurrentFallingResume.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdValue"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdUnit"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdLowCritical"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdLowWarning"))
)
if mibBuilder.loadTexts:
    hwCurrentFallingResume.setStatus(
        "current"
    )

hwPowerRisingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 2, 17)
)
hwPowerRisingAlarm.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdValue"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdUnit"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdHighWarning"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdHighCritical"),
        ("HUAWEI-BASE-TRAP-MIB", "hwPowerDirection"))
)
if mibBuilder.loadTexts:
    hwPowerRisingAlarm.setStatus(
        "current"
    )

hwPowerRisingResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 2, 18)
)
hwPowerRisingResume.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdValue"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdUnit"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdHighWarning"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdHighCritical"),
        ("HUAWEI-BASE-TRAP-MIB", "hwPowerDirection"))
)
if mibBuilder.loadTexts:
    hwPowerRisingResume.setStatus(
        "current"
    )

hwPowerFallingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 2, 19)
)
hwPowerFallingAlarm.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdValue"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdUnit"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdLowCritical"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdLowWarning"),
        ("HUAWEI-BASE-TRAP-MIB", "hwPowerDirection"))
)
if mibBuilder.loadTexts:
    hwPowerFallingAlarm.setStatus(
        "current"
    )

hwPowerFallingResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 2, 20)
)
hwPowerFallingResume.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdValue"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdUnit"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdLowCritical"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdLowWarning"),
        ("HUAWEI-BASE-TRAP-MIB", "hwPowerDirection"))
)
if mibBuilder.loadTexts:
    hwPowerFallingResume.setStatus(
        "current"
    )

hwPowerInsufficiencyAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 2, 21)
)
hwPowerInsufficiencyAlarm.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("ENTITY-MIB", "entPhysicalContainedIn"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-BASE-TRAP-MIB", "hwEntityRatedPower"),
        ("HUAWEI-BASE-TRAP-MIB", "hwDevAvailablePower"),
        ("HUAWEI-BASE-TRAP-MIB", "hwDeviceTotalPower"))
)
if mibBuilder.loadTexts:
    hwPowerInsufficiencyAlarm.setStatus(
        "current"
    )

hwPowerInsufficiencyResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 2, 22)
)
hwPowerInsufficiencyResume.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("ENTITY-MIB", "entPhysicalContainedIn"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-BASE-TRAP-MIB", "hwEntityRatedPower"),
        ("HUAWEI-BASE-TRAP-MIB", "hwDevAvailablePower"),
        ("HUAWEI-BASE-TRAP-MIB", "hwDeviceTotalPower"))
)
if mibBuilder.loadTexts:
    hwPowerInsufficiencyResume.setStatus(
        "current"
    )

hwAcuSoftwareUpgradeFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 2, 23)
)
if mibBuilder.loadTexts:
    hwAcuSoftwareUpgradeFailure.setStatus(
        "current"
    )

hwPowerOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 3, 1)
)
hwPowerOff.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("ENTITY-MIB", "entPhysicalContainedIn"),
        ("ENTITY-MIB", "entPhysicalName"))
)
if mibBuilder.loadTexts:
    hwPowerOff.setStatus(
        "current"
    )

hwPowerOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 3, 2)
)
hwPowerOn.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("ENTITY-MIB", "entPhysicalContainedIn"),
        ("ENTITY-MIB", "entPhysicalName"))
)
if mibBuilder.loadTexts:
    hwPowerOn.setStatus(
        "current"
    )

hwPowerMixed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 3, 3)
)
hwPowerMixed.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("ENTITY-MIB", "entPhysicalContainedIn"),
        ("ENTITY-MIB", "entPhysicalName"))
)
if mibBuilder.loadTexts:
    hwPowerMixed.setStatus(
        "current"
    )

hwPowerMixedResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 3, 4)
)
hwPowerMixedResume.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("ENTITY-MIB", "entPhysicalContainedIn"),
        ("ENTITY-MIB", "entPhysicalName"))
)
if mibBuilder.loadTexts:
    hwPowerMixedResume.setStatus(
        "current"
    )

hwCPUUtilizationRisingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 4, 1)
)
hwCPUUtilizationRisingAlarm.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapRelativeResource"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseUsageValue"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseUsageUnit"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseUsageThreshold"))
)
if mibBuilder.loadTexts:
    hwCPUUtilizationRisingAlarm.setStatus(
        "current"
    )

hwCPUUtilizationResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 4, 2)
)
hwCPUUtilizationResume.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapRelativeResource"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseUsageValue"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseUsageUnit"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseUsageThreshold"))
)
if mibBuilder.loadTexts:
    hwCPUUtilizationResume.setStatus(
        "current"
    )

hwPortPhysicalDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 5, 1)
)
hwPortPhysicalDown.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-BASE-TRAP-MIB", "hwPortPhysicalDownReason"),
        ("IF-MIB", "ifOperStatus"),
        ("IF-MIB", "ifAdminStatus"))
)
if mibBuilder.loadTexts:
    hwPortPhysicalDown.setStatus(
        "current"
    )

hwPortPhysicalUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 5, 2)
)
hwPortPhysicalUp.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("IF-MIB", "ifOperStatus"),
        ("IF-MIB", "ifAdminStatus"))
)
if mibBuilder.loadTexts:
    hwPortPhysicalUp.setStatus(
        "current"
    )

hwPortPhysicalNoTrafficAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 5, 3)
)
hwPortPhysicalNoTrafficAlarm.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapRelativeResource"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapTrafficDir"))
)
if mibBuilder.loadTexts:
    hwPortPhysicalNoTrafficAlarm.setStatus(
        "current"
    )

hwPortPhysicalNoTrafficClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 5, 4)
)
hwPortPhysicalNoTrafficClear.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapRelativeResource"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapTrafficDir"))
)
if mibBuilder.loadTexts:
    hwPortPhysicalNoTrafficClear.setStatus(
        "current"
    )

hwPortPhysicalTrafficRisingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 5, 5)
)
hwPortPhysicalTrafficRisingAlarm.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapRelativeResource"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdValue"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdUnit"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdHighWarning"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapTrafficDir"))
)
if mibBuilder.loadTexts:
    hwPortPhysicalTrafficRisingAlarm.setStatus(
        "current"
    )

hwPortPhysicalTrafficClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 5, 6)
)
hwPortPhysicalTrafficClear.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapRelativeResource"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdValue"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdUnit"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdLowWarning"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapTrafficDir"))
)
if mibBuilder.loadTexts:
    hwPortPhysicalTrafficClear.setStatus(
        "current"
    )

hwPortPhysicalCrcErrorRisingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 5, 7)
)
hwPortPhysicalCrcErrorRisingAlarm.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapRelativeResource"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdValue"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdUnit"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdHighWarning"))
)
if mibBuilder.loadTexts:
    hwPortPhysicalCrcErrorRisingAlarm.setStatus(
        "current"
    )

hwPortPhysicalCrcErrorClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 5, 8)
)
hwPortPhysicalCrcErrorClear.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapRelativeResource"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdValue"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdUnit"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdLowWarning"))
)
if mibBuilder.loadTexts:
    hwPortPhysicalCrcErrorClear.setStatus(
        "current"
    )

hwPortPhysicalEthBroadcastRisingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 5, 9)
)
hwPortPhysicalEthBroadcastRisingAlarm.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapRelativeResource"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdValue"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdUnit"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdHighWarning"))
)
if mibBuilder.loadTexts:
    hwPortPhysicalEthBroadcastRisingAlarm.setStatus(
        "current"
    )

hwPortPhysicalEthBroadcastClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 5, 10)
)
hwPortPhysicalEthBroadcastClear.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapRelativeResource"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdValue"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdUnit"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseThresholdLowWarning"))
)
if mibBuilder.loadTexts:
    hwPortPhysicalEthBroadcastClear.setStatus(
        "current"
    )

hwPortPhysicalEthHalfDuplexAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 5, 11)
)
hwPortPhysicalEthHalfDuplexAlarm.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapRelativeResource"))
)
if mibBuilder.loadTexts:
    hwPortPhysicalEthHalfDuplexAlarm.setStatus(
        "current"
    )

hwPortPhysicalEthFullDuplexClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 5, 12)
)
hwPortPhysicalEthFullDuplexClear.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapRelativeResource"))
)
if mibBuilder.loadTexts:
    hwPortPhysicalEthFullDuplexClear.setStatus(
        "current"
    )

hwPortPhysicalPortTypeChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 5, 13)
)
hwPortPhysicalPortTypeChange.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapLastPortType"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapCurPortType"))
)
if mibBuilder.loadTexts:
    hwPortPhysicalPortTypeChange.setStatus(
        "current"
    )

hwPortPhysicalAutoNegotiateFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 5, 14)
)
hwPortPhysicalAutoNegotiateFail.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapRelativeResource"))
)
if mibBuilder.loadTexts:
    hwPortPhysicalAutoNegotiateFail.setStatus(
        "current"
    )

hwPortPhysicalAutoNegotiateResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 5, 15)
)
hwPortPhysicalAutoNegotiateResume.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapRelativeResource"))
)
if mibBuilder.loadTexts:
    hwPortPhysicalAutoNegotiateResume.setStatus(
        "current"
    )

hwStorageUtilizationRisingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 6, 1)
)
hwStorageUtilizationRisingAlarm.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapRelativeResource"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseUsageValue"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseUsageUnit"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseUsageThreshold"))
)
if mibBuilder.loadTexts:
    hwStorageUtilizationRisingAlarm.setStatus(
        "current"
    )

hwStorageUtilizationResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 6, 2)
)
hwStorageUtilizationResume.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapRelativeResource"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseUsageValue"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseUsageUnit"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseUsageThreshold"))
)
if mibBuilder.loadTexts:
    hwStorageUtilizationResume.setStatus(
        "current"
    )

hwVsDiskFullAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 6, 3)
)
hwVsDiskFullAlarm.setObjects(
      *(("HUAWEI-FLASH-MAN-MIB", "hwStorageSpace"),
        ("HUAWEI-FLASH-MAN-MIB", "hwStorageSpaceFree"),
        ("HUAWEI-FLASH-MAN-MIB", "hwStorageName"))
)
if mibBuilder.loadTexts:
    hwVsDiskFullAlarm.setStatus(
        "current"
    )

hwVsDiskResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 6, 4)
)
hwVsDiskResume.setObjects(
      *(("HUAWEI-FLASH-MAN-MIB", "hwStorageSpace"),
        ("HUAWEI-FLASH-MAN-MIB", "hwStorageSpaceFree"),
        ("HUAWEI-FLASH-MAN-MIB", "hwStorageName"))
)
if mibBuilder.loadTexts:
    hwVsDiskResume.setStatus(
        "current"
    )

hwFIBOverloadSuspend = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 9, 1)
)
hwFIBOverloadSuspend.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("HUAWEI-BASE-TRAP-MIB", "hwFIBOverloadModule"),
        ("ENTITY-MIB", "entPhysicalName"))
)
if mibBuilder.loadTexts:
    hwFIBOverloadSuspend.setStatus(
        "current"
    )

hwFIBOverloadSusResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 9, 2)
)
hwFIBOverloadSusResume.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("HUAWEI-BASE-TRAP-MIB", "hwFIBOverloadModule"),
        ("ENTITY-MIB", "entPhysicalName"))
)
if mibBuilder.loadTexts:
    hwFIBOverloadSusResume.setStatus(
        "current"
    )

hwFIBOverloadForward = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 9, 3)
)
hwFIBOverloadForward.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("HUAWEI-BASE-TRAP-MIB", "hwFIBOverloadModule"),
        ("ENTITY-MIB", "entPhysicalName"))
)
if mibBuilder.loadTexts:
    hwFIBOverloadForward.setStatus(
        "current"
    )

hwFIBOverloadFwResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 9, 4)
)
hwFIBOverloadFwResume.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("HUAWEI-BASE-TRAP-MIB", "hwFIBOverloadModule"),
        ("ENTITY-MIB", "entPhysicalName"))
)
if mibBuilder.loadTexts:
    hwFIBOverloadFwResume.setStatus(
        "current"
    )

hwFESInconsistencyForMemoryLack = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 9, 5)
)
hwFESInconsistencyForMemoryLack.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("ENTITY-MIB", "entPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"))
)
if mibBuilder.loadTexts:
    hwFESInconsistencyForMemoryLack.setStatus(
        "current"
    )

hwFESInconsistencyForMemoryLackResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 9, 6)
)
hwFESInconsistencyForMemoryLackResume.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("ENTITY-MIB", "entPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"))
)
if mibBuilder.loadTexts:
    hwFESInconsistencyForMemoryLackResume.setStatus(
        "current"
    )

hwPppLoopbackDetect = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 10, 1)
)
hwPppLoopbackDetect.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifName"))
)
if mibBuilder.loadTexts:
    hwPppLoopbackDetect.setStatus(
        "current"
    )

hwPppLoopbackDetResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 10, 2)
)
hwPppLoopbackDetResume.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifName"))
)
if mibBuilder.loadTexts:
    hwPppLoopbackDetResume.setStatus(
        "current"
    )

hwFlowCongestion = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 11, 1)
)
hwFlowCongestion.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("ENTITY-MIB", "entPhysicalClass"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseFlowDirectionType"))
)
if mibBuilder.loadTexts:
    hwFlowCongestion.setStatus(
        "current"
    )

hwFlowCongestionResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 11, 2)
)
hwFlowCongestionResume.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("ENTITY-MIB", "entPhysicalClass"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseFlowDirectionType"))
)
if mibBuilder.loadTexts:
    hwFlowCongestionResume.setStatus(
        "current"
    )

hwDeviceAbnormalRisingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 12, 1)
)
hwDeviceAbnormalRisingAlarm.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapRelativeResource"))
)
if mibBuilder.loadTexts:
    hwDeviceAbnormalRisingAlarm.setStatus(
        "current"
    )

hwResExhaustBfdAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 13, 1)
)
hwResExhaustBfdAlarm.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"))
)
if mibBuilder.loadTexts:
    hwResExhaustBfdAlarm.setStatus(
        "current"
    )

hwResExhaustBfdResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 13, 2)
)
hwResExhaustBfdResume.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"))
)
if mibBuilder.loadTexts:
    hwResExhaustBfdResume.setStatus(
        "current"
    )

hwResExhaustOamAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 14, 1)
)
hwResExhaustOamAlarm.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"))
)
if mibBuilder.loadTexts:
    hwResExhaustOamAlarm.setStatus(
        "current"
    )

hwResExhaustOamResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 14, 2)
)
hwResExhaustOamResume.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"))
)
if mibBuilder.loadTexts:
    hwResExhaustOamResume.setStatus(
        "current"
    )

hwHdlcLoopbackDetect = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 15, 1)
)
hwHdlcLoopbackDetect.setObjects(
    ("IF-MIB", "ifDescr")
)
if mibBuilder.loadTexts:
    hwHdlcLoopbackDetect.setStatus(
        "current"
    )

hwHdlcLoopbackDetResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 15, 2)
)
hwHdlcLoopbackDetResume.setObjects(
    ("IF-MIB", "ifDescr")
)
if mibBuilder.loadTexts:
    hwHdlcLoopbackDetResume.setStatus(
        "current"
    )

hwAutoFtpFailAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 16, 1)
)
hwAutoFtpFailAlarm.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapReasonDescr"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"))
)
if mibBuilder.loadTexts:
    hwAutoFtpFailAlarm.setStatus(
        "current"
    )

hwOpticalPowerAbnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 17, 1)
)
hwOpticalPowerAbnormal.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("ENTITY-MIB", "entPhysicalContainedIn"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapRelativeResource"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapReasonDescr"))
)
if mibBuilder.loadTexts:
    hwOpticalPowerAbnormal.setStatus(
        "current"
    )

hwOpticalPowerResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 2, 17, 2)
)
hwOpticalPowerResume.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapSeverity"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapProbableCause"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapEventType"),
        ("ENTITY-MIB", "entPhysicalContainedIn"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapRelativeResource"),
        ("HUAWEI-BASE-TRAP-MIB", "hwBaseTrapReasonDescr"))
)
if mibBuilder.loadTexts:
    hwOpticalPowerResume.setStatus(
        "current"
    )


# Notifications groups

hwBaseTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 3, 2, 2)
)
hwBaseTrapGroup.setObjects(
      *(("HUAWEI-BASE-TRAP-MIB", "hwEntityRemove"),
        ("HUAWEI-BASE-TRAP-MIB", "hwEntityInsert"),
        ("HUAWEI-BASE-TRAP-MIB", "hwEntityUnstable"),
        ("HUAWEI-BASE-TRAP-MIB", "hwEntityUnstableResume"),
        ("HUAWEI-BASE-TRAP-MIB", "hwEntityReset"),
        ("HUAWEI-BASE-TRAP-MIB", "hwEntityResetDone"),
        ("HUAWEI-BASE-TRAP-MIB", "hwEntityCommunicateError"),
        ("HUAWEI-BASE-TRAP-MIB", "hwEntityCommunicateResume"),
        ("HUAWEI-BASE-TRAP-MIB", "hwEntityInvalid"),
        ("HUAWEI-BASE-TRAP-MIB", "hwEntityResume"),
        ("HUAWEI-BASE-TRAP-MIB", "hwEntityLeaveMaster"),
        ("HUAWEI-BASE-TRAP-MIB", "hwEntityBecomeMaster"),
        ("HUAWEI-BASE-TRAP-MIB", "hwEntityOffline"),
        ("HUAWEI-BASE-TRAP-MIB", "hwEntityOnline"),
        ("HUAWEI-BASE-TRAP-MIB", "hwEntityRegFail"),
        ("HUAWEI-BASE-TRAP-MIB", "hwEntityRegSuccess"),
        ("HUAWEI-BASE-TRAP-MIB", "hwEntityDyingGasp"),
        ("HUAWEI-BASE-TRAP-MIB", "hwTempRisingAlarm"),
        ("HUAWEI-BASE-TRAP-MIB", "hwTempRisingResume"),
        ("HUAWEI-BASE-TRAP-MIB", "hwTempFallingAlarm"),
        ("HUAWEI-BASE-TRAP-MIB", "hwTempFallingResume"),
        ("HUAWEI-BASE-TRAP-MIB", "hwHumidityRisingAlarm"),
        ("HUAWEI-BASE-TRAP-MIB", "hwHumidityRisingResume"),
        ("HUAWEI-BASE-TRAP-MIB", "hwHumidityFallingAlarm"),
        ("HUAWEI-BASE-TRAP-MIB", "hwHumidityFallingResume"),
        ("HUAWEI-BASE-TRAP-MIB", "hwVoltRisingAlarm"),
        ("HUAWEI-BASE-TRAP-MIB", "hwVoltRisingResume"),
        ("HUAWEI-BASE-TRAP-MIB", "hwVoltFallingAlarm"),
        ("HUAWEI-BASE-TRAP-MIB", "hwVoltFallingResume"),
        ("HUAWEI-BASE-TRAP-MIB", "hwCurrentRisingAlarm"),
        ("HUAWEI-BASE-TRAP-MIB", "hwCurrentRisingResume"),
        ("HUAWEI-BASE-TRAP-MIB", "hwCurrentFallingAlarm"),
        ("HUAWEI-BASE-TRAP-MIB", "hwCurrentFallingResume"),
        ("HUAWEI-BASE-TRAP-MIB", "hwPowerRisingAlarm"),
        ("HUAWEI-BASE-TRAP-MIB", "hwPowerRisingResume"),
        ("HUAWEI-BASE-TRAP-MIB", "hwPowerFallingAlarm"),
        ("HUAWEI-BASE-TRAP-MIB", "hwPowerInsufficiencyAlarm"),
        ("HUAWEI-BASE-TRAP-MIB", "hwPowerInsufficiencyResume"),
        ("HUAWEI-BASE-TRAP-MIB", "hwPowerFallingResume"),
        ("HUAWEI-BASE-TRAP-MIB", "hwPowerOff"),
        ("HUAWEI-BASE-TRAP-MIB", "hwPowerOn"),
        ("HUAWEI-BASE-TRAP-MIB", "hwPowerMixed"),
        ("HUAWEI-BASE-TRAP-MIB", "hwPowerMixedResume"),
        ("HUAWEI-BASE-TRAP-MIB", "hwCPUUtilizationRisingAlarm"),
        ("HUAWEI-BASE-TRAP-MIB", "hwCPUUtilizationResume"),
        ("HUAWEI-BASE-TRAP-MIB", "hwPortPhysicalDown"),
        ("HUAWEI-BASE-TRAP-MIB", "hwPortPhysicalUp"),
        ("HUAWEI-BASE-TRAP-MIB", "hwPortPhysicalNoTrafficAlarm"),
        ("HUAWEI-BASE-TRAP-MIB", "hwPortPhysicalNoTrafficClear"),
        ("HUAWEI-BASE-TRAP-MIB", "hwPortPhysicalTrafficRisingAlarm"),
        ("HUAWEI-BASE-TRAP-MIB", "hwPortPhysicalTrafficClear"),
        ("HUAWEI-BASE-TRAP-MIB", "hwPortPhysicalCrcErrorRisingAlarm"),
        ("HUAWEI-BASE-TRAP-MIB", "hwPortPhysicalCrcErrorClear"),
        ("HUAWEI-BASE-TRAP-MIB", "hwPortPhysicalEthBroadcastRisingAlarm"),
        ("HUAWEI-BASE-TRAP-MIB", "hwPortPhysicalEthBroadcastClear"),
        ("HUAWEI-BASE-TRAP-MIB", "hwPortPhysicalEthHalfDuplexAlarm"),
        ("HUAWEI-BASE-TRAP-MIB", "hwPortPhysicalEthFullDuplexClear"),
        ("HUAWEI-BASE-TRAP-MIB", "hwStorageUtilizationRisingAlarm"),
        ("HUAWEI-BASE-TRAP-MIB", "hwStorageUtilizationResume"),
        ("HUAWEI-BASE-TRAP-MIB", "hwVsDiskFullAlarm"),
        ("HUAWEI-BASE-TRAP-MIB", "hwVsDiskResume"),
        ("HUAWEI-BASE-TRAP-MIB", "hwFIBOverloadSuspend"),
        ("HUAWEI-BASE-TRAP-MIB", "hwFIBOverloadSusResume"),
        ("HUAWEI-BASE-TRAP-MIB", "hwFIBOverloadForward"),
        ("HUAWEI-BASE-TRAP-MIB", "hwFIBOverloadFwResume"),
        ("HUAWEI-BASE-TRAP-MIB", "hwFESInconsistencyForMemoryLack"),
        ("HUAWEI-BASE-TRAP-MIB", "hwFESInconsistencyForMemoryLackResume"),
        ("HUAWEI-BASE-TRAP-MIB", "hwPppLoopbackDetect"),
        ("HUAWEI-BASE-TRAP-MIB", "hwPppLoopbackDetResume"),
        ("HUAWEI-BASE-TRAP-MIB", "hwEntityCheckFail"),
        ("HUAWEI-BASE-TRAP-MIB", "hwEntityCheckResume"),
        ("HUAWEI-BASE-TRAP-MIB", "hwFlowCongestion"),
        ("HUAWEI-BASE-TRAP-MIB", "hwFlowCongestionResume"),
        ("HUAWEI-BASE-TRAP-MIB", "hwDeviceAbnormalRisingAlarm"),
        ("HUAWEI-BASE-TRAP-MIB", "hwResExhaustBfdAlarm"),
        ("HUAWEI-BASE-TRAP-MIB", "hwResExhaustBfdResume"),
        ("HUAWEI-BASE-TRAP-MIB", "hwResExhaustOamAlarm"),
        ("HUAWEI-BASE-TRAP-MIB", "hwResExhaustOamResume"),
        ("HUAWEI-BASE-TRAP-MIB", "hwHdlcLoopbackDetect"),
        ("HUAWEI-BASE-TRAP-MIB", "hwAutoFtpFailAlarm"),
        ("HUAWEI-BASE-TRAP-MIB", "hwOpticalPowerResume"),
        ("HUAWEI-BASE-TRAP-MIB", "hwHdlcLoopbackDetResume"),
        ("HUAWEI-BASE-TRAP-MIB", "hwPortPhysicalPortTypeChange"),
        ("HUAWEI-BASE-TRAP-MIB", "hwPortPhysicalAutoNegotiateFail"),
        ("HUAWEI-BASE-TRAP-MIB", "hwPortPhysicalAutoNegotiateResume"),
        ("HUAWEI-BASE-TRAP-MIB", "hwOpticalPowerAbnormal"),
        ("HUAWEI-BASE-TRAP-MIB", "hwAcuSoftwareUpgradeFailure"))
)
if mibBuilder.loadTexts:
    hwBaseTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwBaseTrapCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 129, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hwBaseTrapCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-BASE-TRAP-MIB",
    **{"hwBaseTrapMIB": hwBaseTrapMIB,
       "hwBaseTrapObject": hwBaseTrapObject,
       "hwBaseTrapSeverity": hwBaseTrapSeverity,
       "hwBaseTrapProbableCause": hwBaseTrapProbableCause,
       "hwBaseTrapEventType": hwBaseTrapEventType,
       "hwBaseTrapRelativeResource": hwBaseTrapRelativeResource,
       "hwBaseTrapReasonDescr": hwBaseTrapReasonDescr,
       "hwBaseThresholdTable": hwBaseThresholdTable,
       "hwBaseThresholdEntry": hwBaseThresholdEntry,
       "hwBaseThresholdType": hwBaseThresholdType,
       "hwBaseThresholdIndex": hwBaseThresholdIndex,
       "hwBaseThresholdValue": hwBaseThresholdValue,
       "hwBaseThresholdUnit": hwBaseThresholdUnit,
       "hwBaseThresholdLowCritical": hwBaseThresholdLowCritical,
       "hwBaseThresholdLowWarning": hwBaseThresholdLowWarning,
       "hwBaseThresholdHighWarning": hwBaseThresholdHighWarning,
       "hwBaseThresholdHighCritical": hwBaseThresholdHighCritical,
       "hwBaseUsageTable": hwBaseUsageTable,
       "hwBaseUsageEntry": hwBaseUsageEntry,
       "hwBaseUsageType": hwBaseUsageType,
       "hwBaseUsageIndex": hwBaseUsageIndex,
       "hwBaseUsageValue": hwBaseUsageValue,
       "hwBaseUsageUnit": hwBaseUsageUnit,
       "hwBaseUsageThreshold": hwBaseUsageThreshold,
       "hwFIBOverloadModule": hwFIBOverloadModule,
       "hwBaseFlowDirectionType": hwBaseFlowDirectionType,
       "hwPowerDirection": hwPowerDirection,
       "hwBaseTrapTrafficDir": hwBaseTrapTrafficDir,
       "hwEntityRatedPower": hwEntityRatedPower,
       "hwDevAvailablePower": hwDevAvailablePower,
       "hwDeviceTotalPower": hwDeviceTotalPower,
       "hwBaseTrapCurPortType": hwBaseTrapCurPortType,
       "hwBaseTrapLastPortType": hwBaseTrapLastPortType,
       "hwPortPhysicalDownReason": hwPortPhysicalDownReason,
       "hwBaseTraps": hwBaseTraps,
       "hwEntityTrap": hwEntityTrap,
       "hwEntityRemove": hwEntityRemove,
       "hwEntityInsert": hwEntityInsert,
       "hwEntityUnstable": hwEntityUnstable,
       "hwEntityUnstableResume": hwEntityUnstableResume,
       "hwEntityReset": hwEntityReset,
       "hwEntityResetDone": hwEntityResetDone,
       "hwEntityCommunicateError": hwEntityCommunicateError,
       "hwEntityCommunicateResume": hwEntityCommunicateResume,
       "hwEntityInvalid": hwEntityInvalid,
       "hwEntityResume": hwEntityResume,
       "hwEntityLeaveMaster": hwEntityLeaveMaster,
       "hwEntityBecomeMaster": hwEntityBecomeMaster,
       "hwEntityOffline": hwEntityOffline,
       "hwEntityOnline": hwEntityOnline,
       "hwEntityCheckFail": hwEntityCheckFail,
       "hwEntityCheckResume": hwEntityCheckResume,
       "hwEntityRegFail": hwEntityRegFail,
       "hwEntityRegSuccess": hwEntityRegSuccess,
       "hwEntityDyingGasp": hwEntityDyingGasp,
       "hwEnvironmentTrap": hwEnvironmentTrap,
       "hwTempRisingAlarm": hwTempRisingAlarm,
       "hwTempRisingResume": hwTempRisingResume,
       "hwTempFallingAlarm": hwTempFallingAlarm,
       "hwTempFallingResume": hwTempFallingResume,
       "hwHumidityRisingAlarm": hwHumidityRisingAlarm,
       "hwHumidityRisingResume": hwHumidityRisingResume,
       "hwHumidityFallingAlarm": hwHumidityFallingAlarm,
       "hwHumidityFallingResume": hwHumidityFallingResume,
       "hwVoltRisingAlarm": hwVoltRisingAlarm,
       "hwVoltRisingResume": hwVoltRisingResume,
       "hwVoltFallingAlarm": hwVoltFallingAlarm,
       "hwVoltFallingResume": hwVoltFallingResume,
       "hwCurrentRisingAlarm": hwCurrentRisingAlarm,
       "hwCurrentRisingResume": hwCurrentRisingResume,
       "hwCurrentFallingAlarm": hwCurrentFallingAlarm,
       "hwCurrentFallingResume": hwCurrentFallingResume,
       "hwPowerRisingAlarm": hwPowerRisingAlarm,
       "hwPowerRisingResume": hwPowerRisingResume,
       "hwPowerFallingAlarm": hwPowerFallingAlarm,
       "hwPowerFallingResume": hwPowerFallingResume,
       "hwPowerInsufficiencyAlarm": hwPowerInsufficiencyAlarm,
       "hwPowerInsufficiencyResume": hwPowerInsufficiencyResume,
       "hwAcuSoftwareUpgradeFailure": hwAcuSoftwareUpgradeFailure,
       "hwPowerTrap": hwPowerTrap,
       "hwPowerOff": hwPowerOff,
       "hwPowerOn": hwPowerOn,
       "hwPowerMixed": hwPowerMixed,
       "hwPowerMixedResume": hwPowerMixedResume,
       "hwCPUTrap": hwCPUTrap,
       "hwCPUUtilizationRisingAlarm": hwCPUUtilizationRisingAlarm,
       "hwCPUUtilizationResume": hwCPUUtilizationResume,
       "hwPortTrap": hwPortTrap,
       "hwPortPhysicalDown": hwPortPhysicalDown,
       "hwPortPhysicalUp": hwPortPhysicalUp,
       "hwPortPhysicalNoTrafficAlarm": hwPortPhysicalNoTrafficAlarm,
       "hwPortPhysicalNoTrafficClear": hwPortPhysicalNoTrafficClear,
       "hwPortPhysicalTrafficRisingAlarm": hwPortPhysicalTrafficRisingAlarm,
       "hwPortPhysicalTrafficClear": hwPortPhysicalTrafficClear,
       "hwPortPhysicalCrcErrorRisingAlarm": hwPortPhysicalCrcErrorRisingAlarm,
       "hwPortPhysicalCrcErrorClear": hwPortPhysicalCrcErrorClear,
       "hwPortPhysicalEthBroadcastRisingAlarm": hwPortPhysicalEthBroadcastRisingAlarm,
       "hwPortPhysicalEthBroadcastClear": hwPortPhysicalEthBroadcastClear,
       "hwPortPhysicalEthHalfDuplexAlarm": hwPortPhysicalEthHalfDuplexAlarm,
       "hwPortPhysicalEthFullDuplexClear": hwPortPhysicalEthFullDuplexClear,
       "hwPortPhysicalPortTypeChange": hwPortPhysicalPortTypeChange,
       "hwPortPhysicalAutoNegotiateFail": hwPortPhysicalAutoNegotiateFail,
       "hwPortPhysicalAutoNegotiateResume": hwPortPhysicalAutoNegotiateResume,
       "hwStorageTrap": hwStorageTrap,
       "hwStorageUtilizationRisingAlarm": hwStorageUtilizationRisingAlarm,
       "hwStorageUtilizationResume": hwStorageUtilizationResume,
       "hwVsDiskFullAlarm": hwVsDiskFullAlarm,
       "hwVsDiskResume": hwVsDiskResume,
       "hwClockTrap": hwClockTrap,
       "hwFanTrap": hwFanTrap,
       "hwFibTrap": hwFibTrap,
       "hwFIBOverloadSuspend": hwFIBOverloadSuspend,
       "hwFIBOverloadSusResume": hwFIBOverloadSusResume,
       "hwFIBOverloadForward": hwFIBOverloadForward,
       "hwFIBOverloadFwResume": hwFIBOverloadFwResume,
       "hwFESInconsistencyForMemoryLack": hwFESInconsistencyForMemoryLack,
       "hwFESInconsistencyForMemoryLackResume": hwFESInconsistencyForMemoryLackResume,
       "hwPppTrap": hwPppTrap,
       "hwPppLoopbackDetect": hwPppLoopbackDetect,
       "hwPppLoopbackDetResume": hwPppLoopbackDetResume,
       "hwFlowControlTrap": hwFlowControlTrap,
       "hwFlowCongestion": hwFlowCongestion,
       "hwFlowCongestionResume": hwFlowCongestionResume,
       "hwDeviceAbnormalTrap": hwDeviceAbnormalTrap,
       "hwDeviceAbnormalRisingAlarm": hwDeviceAbnormalRisingAlarm,
       "hwResExhaustBfdTrap": hwResExhaustBfdTrap,
       "hwResExhaustBfdAlarm": hwResExhaustBfdAlarm,
       "hwResExhaustBfdResume": hwResExhaustBfdResume,
       "hwResExhaustOamTrap": hwResExhaustOamTrap,
       "hwResExhaustOamAlarm": hwResExhaustOamAlarm,
       "hwResExhaustOamResume": hwResExhaustOamResume,
       "hwHdlcTrap": hwHdlcTrap,
       "hwHdlcLoopbackDetect": hwHdlcLoopbackDetect,
       "hwHdlcLoopbackDetResume": hwHdlcLoopbackDetResume,
       "hwAutoFtpTrap": hwAutoFtpTrap,
       "hwAutoFtpFailAlarm": hwAutoFtpFailAlarm,
       "hwBaseOpticalTrap": hwBaseOpticalTrap,
       "hwOpticalPowerAbnormal": hwOpticalPowerAbnormal,
       "hwOpticalPowerResume": hwOpticalPowerResume,
       "hwBaseTrapConformance": hwBaseTrapConformance,
       "hwBaseTrapCompliances": hwBaseTrapCompliances,
       "hwBaseTrapCompliance": hwBaseTrapCompliance,
       "hwBaseTrapGroups": hwBaseTrapGroups,
       "hwBaseObjectGroup": hwBaseObjectGroup,
       "hwBaseTrapGroup": hwBaseTrapGroup}
)
