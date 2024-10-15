# SNMP MIB module (HUAWEI-ENTITY-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-ENTITY-TRAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:03:41 2024
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

(entPhysicalIndex,
 entPhysicalName) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex",
    "entPhysicalName")

(hwBaseTrapEventType,
 hwBaseTrapProbableCause,
 hwBaseTrapSeverity) = mibBuilder.importSymbols(
    "HUAWEI-BASE-TRAP-MIB",
    "hwBaseTrapEventType",
    "hwBaseTrapProbableCause",
    "hwBaseTrapSeverity")

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

(IANAItuProbableCause,) = mibBuilder.importSymbols(
    "IANA-ITU-ALARM-TC-MIB",
    "IANAItuProbableCause")

(ifIndex,
 ifName) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex",
    "ifName")

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

hwEntityTrapMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwEntityTrapObject_ObjectIdentity = ObjectIdentity
hwEntityTrapObject = _HwEntityTrapObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 1)
)
_HwEntityPhysicalIndex_Type = Integer32
_HwEntityPhysicalIndex_Object = MibScalar
hwEntityPhysicalIndex = _HwEntityPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 1, 1),
    _HwEntityPhysicalIndex_Type()
)
hwEntityPhysicalIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEntityPhysicalIndex.setStatus("current")


class _HwEntityTrapEntType_Type(Integer32):
    """Custom type hwEntityTrapEntType based on Integer32"""
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
        *(("cfcard", 5),
          ("lpu", 2),
          ("mpu", 1),
          ("ofc", 6),
          ("pic", 4),
          ("sfu", 3))
    )


_HwEntityTrapEntType_Type.__name__ = "Integer32"
_HwEntityTrapEntType_Object = MibScalar
hwEntityTrapEntType = _HwEntityTrapEntType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 1, 2),
    _HwEntityTrapEntType_Type()
)
hwEntityTrapEntType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEntityTrapEntType.setStatus("current")
_HwEntityTrapFaultID_Type = IANAItuProbableCause
_HwEntityTrapFaultID_Object = MibScalar
hwEntityTrapFaultID = _HwEntityTrapFaultID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 1, 3),
    _HwEntityTrapFaultID_Type()
)
hwEntityTrapFaultID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwEntityTrapFaultID.setStatus("current")


class _HwEntityCommunicateType_Type(Integer32):
    """Custom type hwEntityCommunicateType based on Integer32"""
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
        *(("clockChannel", 3),
          ("controlChannel", 1),
          ("dataChannel", 4),
          ("monitorChannel", 2))
    )


_HwEntityCommunicateType_Type.__name__ = "Integer32"
_HwEntityCommunicateType_Object = MibScalar
hwEntityCommunicateType = _HwEntityCommunicateType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 1, 4),
    _HwEntityCommunicateType_Type()
)
hwEntityCommunicateType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEntityCommunicateType.setStatus("current")
_HwEntityThresholdTable_Object = MibTable
hwEntityThresholdTable = _HwEntityThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 1, 5)
)
if mibBuilder.loadTexts:
    hwEntityThresholdTable.setStatus("current")
_HwEntityThresholdEntry_Object = MibTableRow
hwEntityThresholdEntry = _HwEntityThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 1, 5, 1)
)
hwEntityThresholdEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    hwEntityThresholdEntry.setStatus("current")


class _HwEntityThresholdType_Type(Integer32):
    """Custom type hwEntityThresholdType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fallBelow", 2),
          ("riseOver", 1))
    )


_HwEntityThresholdType_Type.__name__ = "Integer32"
_HwEntityThresholdType_Object = MibTableColumn
hwEntityThresholdType = _HwEntityThresholdType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 1, 5, 1, 1),
    _HwEntityThresholdType_Type()
)
hwEntityThresholdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityThresholdType.setStatus("current")
_HwEntityThresholdValue_Type = Integer32
_HwEntityThresholdValue_Object = MibTableColumn
hwEntityThresholdValue = _HwEntityThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 1, 5, 1, 2),
    _HwEntityThresholdValue_Type()
)
hwEntityThresholdValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEntityThresholdValue.setStatus("current")
_HwEntityThresholdCurrent_Type = Integer32
_HwEntityThresholdCurrent_Object = MibTableColumn
hwEntityThresholdCurrent = _HwEntityThresholdCurrent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 1, 5, 1, 3),
    _HwEntityThresholdCurrent_Type()
)
hwEntityThresholdCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEntityThresholdCurrent.setStatus("current")
_HwEntityThresholdCritical_Type = Integer32
_HwEntityThresholdCritical_Object = MibTableColumn
hwEntityThresholdCritical = _HwEntityThresholdCritical_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 1, 5, 1, 4),
    _HwEntityThresholdCritical_Type()
)
hwEntityThresholdCritical.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEntityThresholdCritical.setStatus("current")
_HwEntityThresholdWarning_Type = Integer32
_HwEntityThresholdWarning_Object = MibTableColumn
hwEntityThresholdWarning = _HwEntityThresholdWarning_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 1, 5, 1, 5),
    _HwEntityThresholdWarning_Type()
)
hwEntityThresholdWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEntityThresholdWarning.setStatus("current")
_HwUserDefAlarmName_Type = OctetString
_HwUserDefAlarmName_Object = MibScalar
hwUserDefAlarmName = _HwUserDefAlarmName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 1, 6),
    _HwUserDefAlarmName_Type()
)
hwUserDefAlarmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwUserDefAlarmName.setStatus("current")
_HwUserDefChannel_Type = Integer32
_HwUserDefChannel_Object = MibScalar
hwUserDefChannel = _HwUserDefChannel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 1, 7),
    _HwUserDefChannel_Type()
)
hwUserDefChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwUserDefChannel.setStatus("current")
_HwSoftwareVersion_Type = OctetString
_HwSoftwareVersion_Object = MibScalar
hwSoftwareVersion = _HwSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 1, 8),
    _HwSoftwareVersion_Type()
)
hwSoftwareVersion.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwSoftwareVersion.setStatus("current")
_HwStartupSoftwareFileName_Type = OctetString
_HwStartupSoftwareFileName_Object = MibScalar
hwStartupSoftwareFileName = _HwStartupSoftwareFileName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 1, 9),
    _HwStartupSoftwareFileName_Type()
)
hwStartupSoftwareFileName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwStartupSoftwareFileName.setStatus("current")
_HwStorageDevName_Type = OctetString
_HwStorageDevName_Object = MibScalar
hwStorageDevName = _HwStorageDevName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 1, 10),
    _HwStorageDevName_Type()
)
hwStorageDevName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwStorageDevName.setStatus("current")
_HwEntityTraps_ObjectIdentity = ObjectIdentity
hwEntityTraps = _HwEntityTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2)
)
_HwChassisTrap_ObjectIdentity = ObjectIdentity
hwChassisTrap = _HwChassisTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 1)
)
_HwBoardTrap_ObjectIdentity = ObjectIdentity
hwBoardTrap = _HwBoardTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 2)
)
_HwCardTrap_ObjectIdentity = ObjectIdentity
hwCardTrap = _HwCardTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 3)
)
_HwOpticalTrap_ObjectIdentity = ObjectIdentity
hwOpticalTrap = _HwOpticalTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 4)
)
_HwPowerTrap_ObjectIdentity = ObjectIdentity
hwPowerTrap = _HwPowerTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 5)
)
_HwFanTrap_ObjectIdentity = ObjectIdentity
hwFanTrap = _HwFanTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 6)
)
_HwLcdTrap_ObjectIdentity = ObjectIdentity
hwLcdTrap = _HwLcdTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 7)
)
_HwCmuTrap_ObjectIdentity = ObjectIdentity
hwCmuTrap = _HwCmuTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 8)
)
_HwCommunicateTrap_ObjectIdentity = ObjectIdentity
hwCommunicateTrap = _HwCommunicateTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 9)
)
_HwEnvironmentTrap_ObjectIdentity = ObjectIdentity
hwEnvironmentTrap = _HwEnvironmentTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 10)
)
_HwSystemConfigTrap_ObjectIdentity = ObjectIdentity
hwSystemConfigTrap = _HwSystemConfigTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 11)
)
_HwPortTrap_ObjectIdentity = ObjectIdentity
hwPortTrap = _HwPortTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 12)
)
_HwUserDefTrap_ObjectIdentity = ObjectIdentity
hwUserDefTrap = _HwUserDefTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 13)
)
_HwCPUTrap_ObjectIdentity = ObjectIdentity
hwCPUTrap = _HwCPUTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 14)
)
_HwMemoryTrap_ObjectIdentity = ObjectIdentity
hwMemoryTrap = _HwMemoryTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 15)
)
_HwStorageDevTrap_ObjectIdentity = ObjectIdentity
hwStorageDevTrap = _HwStorageDevTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 16)
)
_HwPppTrap_ObjectIdentity = ObjectIdentity
hwPppTrap = _HwPppTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 17)
)
_HwFileStatusTrap_ObjectIdentity = ObjectIdentity
hwFileStatusTrap = _HwFileStatusTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 18)
)
_HwUSBTrap_ObjectIdentity = ObjectIdentity
hwUSBTrap = _HwUSBTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 19)
)
_HwEntityTrapConformance_ObjectIdentity = ObjectIdentity
hwEntityTrapConformance = _HwEntityTrapConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 3)
)
_HwEntityTrapCompliances_ObjectIdentity = ObjectIdentity
hwEntityTrapCompliances = _HwEntityTrapCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 3, 1)
)
_HwEntityTrapGroups_ObjectIdentity = ObjectIdentity
hwEntityTrapGroups = _HwEntityTrapGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 3, 2)
)

# Managed Objects groups

hwEntityObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 3, 2, 1)
)
hwEntityObjectGroup.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityPhysicalIndex"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapEntType"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityCommunicateType"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityThresholdType"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityThresholdValue"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityThresholdCurrent"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityThresholdCritical"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityThresholdWarning"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwUserDefAlarmName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwUserDefChannel"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwSoftwareVersion"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwStartupSoftwareFileName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwStorageDevName"))
)
if mibBuilder.loadTexts:
    hwEntityObjectGroup.setStatus("current")


# Notification objects

hwChassisRemove = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 1, 1)
)
hwChassisRemove.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwChassisRemove.setStatus(
        "current"
    )

hwChassisInsert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 1, 2)
)
hwChassisInsert.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwChassisInsert.setStatus(
        "current"
    )

hwChassisFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 1, 3)
)
hwChassisFail.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwChassisFail.setStatus(
        "current"
    )

hwChassisFailResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 1, 4)
)
hwChassisFailResume.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwChassisFailResume.setStatus(
        "current"
    )

hwChassisInvalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 1, 5)
)
hwChassisInvalid.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwChassisInvalid.setStatus(
        "current"
    )

hwChassisInvalidResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 1, 6)
)
hwChassisInvalidResume.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwChassisInvalidResume.setStatus(
        "current"
    )

hwBoardRemove = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 2, 1)
)
hwBoardRemove.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapEntType"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwBoardRemove.setStatus(
        "current"
    )

hwBoardInsert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 2, 2)
)
hwBoardInsert.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapEntType"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwBoardInsert.setStatus(
        "current"
    )

hwBoardFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 2, 3)
)
hwBoardFail.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapEntType"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwBoardFail.setStatus(
        "current"
    )

hwBoardFailResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 2, 4)
)
hwBoardFailResume.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapEntType"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwBoardFailResume.setStatus(
        "current"
    )

hwBoardInvalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 2, 5)
)
hwBoardInvalid.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapEntType"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwBoardInvalid.setStatus(
        "current"
    )

hwBoardInvalidResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 2, 6)
)
hwBoardInvalidResume.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapEntType"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwBoardInvalidResume.setStatus(
        "current"
    )

hwBoardLeaveMaster = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 2, 7)
)
hwBoardLeaveMaster.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapEntType"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwBoardLeaveMaster.setStatus(
        "current"
    )

hwBoardBecomeMaster = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 2, 8)
)
hwBoardBecomeMaster.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapEntType"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwBoardBecomeMaster.setStatus(
        "current"
    )

hwUpMicroSwitchOpen = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 2, 9)
)
hwUpMicroSwitchOpen.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapEntType"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwUpMicroSwitchOpen.setStatus(
        "current"
    )

hwUpMicroSwitchClose = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 2, 10)
)
hwUpMicroSwitchClose.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapEntType"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwUpMicroSwitchClose.setStatus(
        "current"
    )

hwDownMicroSwitchOpen = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 2, 11)
)
hwDownMicroSwitchOpen.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapEntType"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwDownMicroSwitchOpen.setStatus(
        "current"
    )

hwDownMicroSwitchClose = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 2, 12)
)
hwDownMicroSwitchClose.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapEntType"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwDownMicroSwitchClose.setStatus(
        "current"
    )

hwCardRemove = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 3, 1)
)
hwCardRemove.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapEntType"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwCardRemove.setStatus(
        "current"
    )

hwCardInsert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 3, 2)
)
hwCardInsert.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapEntType"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwCardInsert.setStatus(
        "current"
    )

hwCardFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 3, 3)
)
hwCardFail.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapEntType"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwCardFail.setStatus(
        "current"
    )

hwCardFailResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 3, 4)
)
hwCardFailResume.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapEntType"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwCardFailResume.setStatus(
        "current"
    )

hwCardInvalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 3, 5)
)
hwCardInvalid.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapEntType"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwCardInvalid.setStatus(
        "current"
    )

hwCardInvalidResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 3, 6)
)
hwCardInvalidResume.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapEntType"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwCardInvalidResume.setStatus(
        "current"
    )

hwOpticalRemove = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 4, 1)
)
hwOpticalRemove.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwOpticalRemove.setStatus(
        "current"
    )

hwOpticalInsert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 4, 2)
)
hwOpticalInsert.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwOpticalInsert.setStatus(
        "current"
    )

hwOpticalFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 4, 3)
)
hwOpticalFail.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwOpticalFail.setStatus(
        "current"
    )

hwOpticalFailResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 4, 4)
)
hwOpticalFailResume.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwOpticalFailResume.setStatus(
        "current"
    )

hwOpticalInvalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 4, 5)
)
hwOpticalInvalid.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwOpticalInvalid.setStatus(
        "current"
    )

hwOpticalInvalidResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 4, 6)
)
hwOpticalInvalidResume.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwOpticalInvalidResume.setStatus(
        "current"
    )

hwOpticalPowerAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 4, 7)
)
hwOpticalPowerAlarm.setObjects(
      *(("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwUserDefAlarmName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwOpticalPowerAlarm.setStatus(
        "current"
    )

hwOpticalPowerAlarmResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 4, 8)
)
hwOpticalPowerAlarmResume.setObjects(
      *(("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwUserDefAlarmName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwOpticalPowerAlarmResume.setStatus(
        "current"
    )

hwPowerRemove = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 5, 1)
)
hwPowerRemove.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwPowerRemove.setStatus(
        "current"
    )

hwPowerInsert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 5, 2)
)
hwPowerInsert.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwPowerInsert.setStatus(
        "current"
    )

hwPowerFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 5, 3)
)
hwPowerFail.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwPowerFail.setStatus(
        "current"
    )

hwPowerFailResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 5, 4)
)
hwPowerFailResume.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwPowerFailResume.setStatus(
        "current"
    )

hwPowerInvalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 5, 5)
)
hwPowerInvalid.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwPowerInvalid.setStatus(
        "current"
    )

hwPowerInvalidResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 5, 6)
)
hwPowerInvalidResume.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwPowerInvalidResume.setStatus(
        "current"
    )

hwPowerUnusable = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 5, 7)
)
hwPowerUnusable.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwPowerUnusable.setStatus(
        "current"
    )

hwPowerUnusableResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 5, 8)
)
hwPowerUnusableResume.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwPowerUnusableResume.setStatus(
        "current"
    )

hwFanRemove = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 6, 1)
)
hwFanRemove.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwFanRemove.setStatus(
        "current"
    )

hwFanInsert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 6, 2)
)
hwFanInsert.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwFanInsert.setStatus(
        "current"
    )

hwFanFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 6, 3)
)
hwFanFail.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwFanFail.setStatus(
        "current"
    )

hwFanFailResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 6, 4)
)
hwFanFailResume.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwFanFailResume.setStatus(
        "current"
    )

hwFanInvalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 6, 5)
)
hwFanInvalid.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwFanInvalid.setStatus(
        "current"
    )

hwFanInvalidResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 6, 6)
)
hwFanInvalidResume.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwFanInvalidResume.setStatus(
        "current"
    )

hwFanUnusable = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 6, 7)
)
hwFanUnusable.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwFanUnusable.setStatus(
        "current"
    )

hwFanUnusableResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 6, 8)
)
hwFanUnusableResume.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwFanUnusableResume.setStatus(
        "current"
    )

hwLcdRemove = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 7, 1)
)
hwLcdRemove.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwLcdRemove.setStatus(
        "current"
    )

hwLcdInsert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 7, 2)
)
hwLcdInsert.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwLcdInsert.setStatus(
        "current"
    )

hwLcdInvalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 7, 3)
)
hwLcdInvalid.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwLcdInvalid.setStatus(
        "current"
    )

hwLcdInvalidResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 7, 4)
)
hwLcdInvalidResume.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwLcdInvalidResume.setStatus(
        "current"
    )

hwLcdUnusable = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 7, 5)
)
hwLcdUnusable.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwLcdUnusable.setStatus(
        "current"
    )

hwLcdUnusableResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 7, 6)
)
hwLcdUnusableResume.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwLcdUnusableResume.setStatus(
        "current"
    )

hwCmuRemove = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 8, 1)
)
hwCmuRemove.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwCmuRemove.setStatus(
        "current"
    )

hwCmuInsert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 8, 2)
)
hwCmuInsert.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwCmuInsert.setStatus(
        "current"
    )

hwCmuInvalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 8, 3)
)
hwCmuInvalid.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwCmuInvalid.setStatus(
        "current"
    )

hwCmuInvalidResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 8, 4)
)
hwCmuInvalidResume.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwCmuInvalidResume.setStatus(
        "current"
    )

hwCmuUnusable = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 8, 5)
)
hwCmuUnusable.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwCmuUnusable.setStatus(
        "current"
    )

hwCmuUnusableResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 8, 6)
)
hwCmuUnusableResume.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwCmuUnusableResume.setStatus(
        "current"
    )

hwCommunicateError = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 9, 1)
)
hwCommunicateError.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapEntType"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityCommunicateType"))
)
if mibBuilder.loadTexts:
    hwCommunicateError.setStatus(
        "current"
    )

hwCommunicateResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 9, 2)
)
hwCommunicateResume.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapEntType"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityCommunicateType"))
)
if mibBuilder.loadTexts:
    hwCommunicateResume.setStatus(
        "current"
    )

hwTempAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 10, 1)
)
hwTempAlarm.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityThresholdType"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityThresholdValue"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityThresholdCurrent"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwTempAlarm.setStatus(
        "current"
    )

hwTempResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 10, 2)
)
hwTempResume.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityThresholdType"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityThresholdValue"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityThresholdCurrent"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwTempResume.setStatus(
        "current"
    )

hwHumidityAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 10, 3)
)
hwHumidityAlarm.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityThresholdType"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityThresholdValue"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityThresholdCurrent"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwHumidityAlarm.setStatus(
        "current"
    )

hwHumidityResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 10, 4)
)
hwHumidityResume.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityThresholdType"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityThresholdValue"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityThresholdCurrent"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwHumidityResume.setStatus(
        "current"
    )

hwVoltAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 10, 5)
)
hwVoltAlarm.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityThresholdType"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityThresholdValue"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityThresholdCurrent"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwVoltAlarm.setStatus(
        "current"
    )

hwVoltResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 10, 6)
)
hwVoltResume.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityThresholdType"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityThresholdValue"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityThresholdCurrent"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwVoltResume.setStatus(
        "current"
    )

hwGateAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 10, 7)
)
hwGateAlarm.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityThresholdType"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityThresholdValue"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityThresholdCurrent"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwGateAlarm.setStatus(
        "current"
    )

hwGateResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 10, 8)
)
hwGateResume.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityThresholdType"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityThresholdValue"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityThresholdCurrent"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwGateResume.setStatus(
        "current"
    )

hwFogAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 10, 9)
)
hwFogAlarm.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityThresholdType"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityThresholdValue"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityThresholdCurrent"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwFogAlarm.setStatus(
        "current"
    )

hwFogResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 10, 10)
)
hwFogResume.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityThresholdType"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityThresholdValue"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityThresholdCurrent"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwFogResume.setStatus(
        "current"
    )

hwUnstableAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 10, 11)
)
hwUnstableAlarm.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapEntType"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwUnstableAlarm.setStatus(
        "current"
    )

hwUnstableResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 10, 12)
)
hwUnstableResume.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapEntType"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwUnstableResume.setStatus(
        "current"
    )

hwBrdTempAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 10, 13)
)
hwBrdTempAlarm.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityThresholdType"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityThresholdWarning"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityThresholdCurrent"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwBrdTempAlarm.setStatus(
        "current"
    )

hwBrdTempResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 10, 14)
)
hwBrdTempResume.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityThresholdType"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityThresholdWarning"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityThresholdCurrent"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwBrdTempResume.setStatus(
        "current"
    )

hwBrdTempFatalAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 10, 15)
)
hwBrdTempFatalAlarm.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityThresholdType"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityThresholdCritical"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityThresholdCurrent"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwBrdTempFatalAlarm.setStatus(
        "current"
    )

hwBrdTempFatalResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 10, 16)
)
hwBrdTempFatalResume.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityThresholdType"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityThresholdCritical"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityThresholdCurrent"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwBrdTempFatalResume.setStatus(
        "current"
    )

hwPowerFailureAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 10, 17)
)
if mibBuilder.loadTexts:
    hwPowerFailureAlarm.setStatus(
        "current"
    )

hwPowerFailureResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 10, 18)
)
if mibBuilder.loadTexts:
    hwPowerFailureResume.setStatus(
        "current"
    )

hwSystemConfigError = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 11, 1)
)
hwSystemConfigError.setObjects(
    ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID")
)
if mibBuilder.loadTexts:
    hwSystemConfigError.setStatus(
        "current"
    )

hwSystemConfigResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 11, 2)
)
hwSystemConfigResume.setObjects(
    ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID")
)
if mibBuilder.loadTexts:
    hwSystemConfigResume.setStatus(
        "current"
    )

hwSystemRollback = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 11, 3)
)
hwSystemRollback.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwSoftwareVersion"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwStartupSoftwareFileName"))
)
if mibBuilder.loadTexts:
    hwSystemRollback.setStatus(
        "current"
    )

hwPortDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 12, 1)
)
hwPortDown.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwPortDown.setStatus(
        "current"
    )

hwPortUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 12, 2)
)
hwPortUp.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwPortUp.setStatus(
        "current"
    )

hwUserDefAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 13, 1)
)
hwUserDefAlarm.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwUserDefAlarmName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwUserDefChannel"))
)
if mibBuilder.loadTexts:
    hwUserDefAlarm.setStatus(
        "current"
    )

hwUserDefResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 13, 2)
)
hwUserDefResume.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwUserDefAlarmName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwUserDefChannel"))
)
if mibBuilder.loadTexts:
    hwUserDefResume.setStatus(
        "current"
    )

hwCPUUtilizationRising = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 14, 1)
)
hwCPUUtilizationRising.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityThresholdType"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityThresholdWarning"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityThresholdCurrent"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwCPUUtilizationRising.setStatus(
        "current"
    )

hwCPUUtilizationResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 14, 2)
)
hwCPUUtilizationResume.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityThresholdType"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityThresholdWarning"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityThresholdCurrent"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwCPUUtilizationResume.setStatus(
        "current"
    )

hwMemUtilizationRising = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 15, 1)
)
hwMemUtilizationRising.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityThresholdType"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityThresholdWarning"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityThresholdCurrent"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwMemUtilizationRising.setStatus(
        "current"
    )

hwMemUtilizationResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 15, 2)
)
hwMemUtilizationResume.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityThresholdType"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityThresholdWarning"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityThresholdCurrent"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwMemUtilizationResume.setStatus(
        "current"
    )

hwStorageDevRemove = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 16, 1)
)
hwStorageDevRemove.setObjects(
      *(("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwStorageDevName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwStorageDevRemove.setStatus(
        "current"
    )

hwStorageDevInsert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 16, 2)
)
hwStorageDevInsert.setObjects(
      *(("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwStorageDevName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwStorageDevInsert.setStatus(
        "current"
    )

hwPppLoopbackDetect = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 17, 1)
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
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 17, 2)
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

hwFileError = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 18, 1)
)
hwFileError.setObjects(
      *(("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwStorageDevName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwFileError.setStatus(
        "current"
    )

hwFileErrorResume = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 18, 2)
)
hwFileErrorResume.setObjects(
      *(("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwStorageDevName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwFileErrorResume.setStatus(
        "current"
    )

hwUSBInsert = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 19, 1)
)
hwUSBInsert.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapEntType"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwUSBInsert.setStatus(
        "current"
    )

hwUSBRemove = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 2, 19, 2)
)
hwUSBRemove.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwEntityPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapEntType"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwEntityTrapFaultID"))
)
if mibBuilder.loadTexts:
    hwUSBRemove.setStatus(
        "current"
    )


# Notifications groups

hwEntityTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 3, 2, 2)
)
hwEntityTrapGroup.setObjects(
      *(("HUAWEI-ENTITY-TRAP-MIB", "hwChassisRemove"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwChassisInsert"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwChassisFail"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwChassisFailResume"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwChassisInvalid"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwChassisInvalidResume"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwBoardRemove"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwBoardInsert"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwBoardFail"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwBoardFailResume"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwBoardInvalid"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwBoardInvalidResume"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwBoardLeaveMaster"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwBoardBecomeMaster"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwCardRemove"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwCardInsert"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwCardFail"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwCardFailResume"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwCardInvalid"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwCardInvalidResume"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwOpticalRemove"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwOpticalInsert"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwOpticalFail"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwOpticalFailResume"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwOpticalInvalid"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwOpticalInvalidResume"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwPowerRemove"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwPowerInsert"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwPowerFail"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwPowerFailResume"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwPowerInvalid"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwPowerInvalidResume"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwPowerUnusable"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwPowerUnusableResume"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwFanRemove"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwFanInsert"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwFanFail"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwFanFailResume"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwFanInvalid"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwFanInvalidResume"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwFanUnusable"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwFanUnusableResume"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwLcdRemove"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwLcdInsert"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwLcdInvalid"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwLcdInvalidResume"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwLcdUnusable"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwLcdUnusableResume"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwCmuRemove"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwCmuInsert"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwCmuInvalid"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwCmuInvalidResume"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwCmuUnusable"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwCmuUnusableResume"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwCommunicateError"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwCommunicateResume"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwTempAlarm"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwTempResume"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwHumidityAlarm"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwHumidityResume"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwVoltAlarm"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwVoltResume"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwGateAlarm"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwGateResume"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwFogAlarm"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwFogResume"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwUnstableAlarm"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwUnstableResume"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwBrdTempAlarm"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwBrdTempResume"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwBrdTempFatalAlarm"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwBrdTempFatalResume"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwPowerFailureAlarm"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwPowerFailureResume"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwSystemConfigError"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwSystemConfigResume"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwPortDown"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwPortUp"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwUserDefAlarm"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwUserDefResume"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwCPUUtilizationRising"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwCPUUtilizationResume"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwMemUtilizationRising"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwMemUtilizationResume"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwStorageDevRemove"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwStorageDevInsert"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwSystemRollback"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwUpMicroSwitchOpen"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwUpMicroSwitchClose"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwDownMicroSwitchOpen"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwDownMicroSwitchClose"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwOpticalPowerAlarm"),
        ("HUAWEI-ENTITY-TRAP-MIB", "hwOpticalPowerAlarmResume"))
)
if mibBuilder.loadTexts:
    hwEntityTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwEntityTrapCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 219, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hwEntityTrapCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-ENTITY-TRAP-MIB",
    **{"hwEntityTrapMIB": hwEntityTrapMIB,
       "hwEntityTrapObject": hwEntityTrapObject,
       "hwEntityPhysicalIndex": hwEntityPhysicalIndex,
       "hwEntityTrapEntType": hwEntityTrapEntType,
       "hwEntityTrapFaultID": hwEntityTrapFaultID,
       "hwEntityCommunicateType": hwEntityCommunicateType,
       "hwEntityThresholdTable": hwEntityThresholdTable,
       "hwEntityThresholdEntry": hwEntityThresholdEntry,
       "hwEntityThresholdType": hwEntityThresholdType,
       "hwEntityThresholdValue": hwEntityThresholdValue,
       "hwEntityThresholdCurrent": hwEntityThresholdCurrent,
       "hwEntityThresholdCritical": hwEntityThresholdCritical,
       "hwEntityThresholdWarning": hwEntityThresholdWarning,
       "hwUserDefAlarmName": hwUserDefAlarmName,
       "hwUserDefChannel": hwUserDefChannel,
       "hwSoftwareVersion": hwSoftwareVersion,
       "hwStartupSoftwareFileName": hwStartupSoftwareFileName,
       "hwStorageDevName": hwStorageDevName,
       "hwEntityTraps": hwEntityTraps,
       "hwChassisTrap": hwChassisTrap,
       "hwChassisRemove": hwChassisRemove,
       "hwChassisInsert": hwChassisInsert,
       "hwChassisFail": hwChassisFail,
       "hwChassisFailResume": hwChassisFailResume,
       "hwChassisInvalid": hwChassisInvalid,
       "hwChassisInvalidResume": hwChassisInvalidResume,
       "hwBoardTrap": hwBoardTrap,
       "hwBoardRemove": hwBoardRemove,
       "hwBoardInsert": hwBoardInsert,
       "hwBoardFail": hwBoardFail,
       "hwBoardFailResume": hwBoardFailResume,
       "hwBoardInvalid": hwBoardInvalid,
       "hwBoardInvalidResume": hwBoardInvalidResume,
       "hwBoardLeaveMaster": hwBoardLeaveMaster,
       "hwBoardBecomeMaster": hwBoardBecomeMaster,
       "hwUpMicroSwitchOpen": hwUpMicroSwitchOpen,
       "hwUpMicroSwitchClose": hwUpMicroSwitchClose,
       "hwDownMicroSwitchOpen": hwDownMicroSwitchOpen,
       "hwDownMicroSwitchClose": hwDownMicroSwitchClose,
       "hwCardTrap": hwCardTrap,
       "hwCardRemove": hwCardRemove,
       "hwCardInsert": hwCardInsert,
       "hwCardFail": hwCardFail,
       "hwCardFailResume": hwCardFailResume,
       "hwCardInvalid": hwCardInvalid,
       "hwCardInvalidResume": hwCardInvalidResume,
       "hwOpticalTrap": hwOpticalTrap,
       "hwOpticalRemove": hwOpticalRemove,
       "hwOpticalInsert": hwOpticalInsert,
       "hwOpticalFail": hwOpticalFail,
       "hwOpticalFailResume": hwOpticalFailResume,
       "hwOpticalInvalid": hwOpticalInvalid,
       "hwOpticalInvalidResume": hwOpticalInvalidResume,
       "hwOpticalPowerAlarm": hwOpticalPowerAlarm,
       "hwOpticalPowerAlarmResume": hwOpticalPowerAlarmResume,
       "hwPowerTrap": hwPowerTrap,
       "hwPowerRemove": hwPowerRemove,
       "hwPowerInsert": hwPowerInsert,
       "hwPowerFail": hwPowerFail,
       "hwPowerFailResume": hwPowerFailResume,
       "hwPowerInvalid": hwPowerInvalid,
       "hwPowerInvalidResume": hwPowerInvalidResume,
       "hwPowerUnusable": hwPowerUnusable,
       "hwPowerUnusableResume": hwPowerUnusableResume,
       "hwFanTrap": hwFanTrap,
       "hwFanRemove": hwFanRemove,
       "hwFanInsert": hwFanInsert,
       "hwFanFail": hwFanFail,
       "hwFanFailResume": hwFanFailResume,
       "hwFanInvalid": hwFanInvalid,
       "hwFanInvalidResume": hwFanInvalidResume,
       "hwFanUnusable": hwFanUnusable,
       "hwFanUnusableResume": hwFanUnusableResume,
       "hwLcdTrap": hwLcdTrap,
       "hwLcdRemove": hwLcdRemove,
       "hwLcdInsert": hwLcdInsert,
       "hwLcdInvalid": hwLcdInvalid,
       "hwLcdInvalidResume": hwLcdInvalidResume,
       "hwLcdUnusable": hwLcdUnusable,
       "hwLcdUnusableResume": hwLcdUnusableResume,
       "hwCmuTrap": hwCmuTrap,
       "hwCmuRemove": hwCmuRemove,
       "hwCmuInsert": hwCmuInsert,
       "hwCmuInvalid": hwCmuInvalid,
       "hwCmuInvalidResume": hwCmuInvalidResume,
       "hwCmuUnusable": hwCmuUnusable,
       "hwCmuUnusableResume": hwCmuUnusableResume,
       "hwCommunicateTrap": hwCommunicateTrap,
       "hwCommunicateError": hwCommunicateError,
       "hwCommunicateResume": hwCommunicateResume,
       "hwEnvironmentTrap": hwEnvironmentTrap,
       "hwTempAlarm": hwTempAlarm,
       "hwTempResume": hwTempResume,
       "hwHumidityAlarm": hwHumidityAlarm,
       "hwHumidityResume": hwHumidityResume,
       "hwVoltAlarm": hwVoltAlarm,
       "hwVoltResume": hwVoltResume,
       "hwGateAlarm": hwGateAlarm,
       "hwGateResume": hwGateResume,
       "hwFogAlarm": hwFogAlarm,
       "hwFogResume": hwFogResume,
       "hwUnstableAlarm": hwUnstableAlarm,
       "hwUnstableResume": hwUnstableResume,
       "hwBrdTempAlarm": hwBrdTempAlarm,
       "hwBrdTempResume": hwBrdTempResume,
       "hwBrdTempFatalAlarm": hwBrdTempFatalAlarm,
       "hwBrdTempFatalResume": hwBrdTempFatalResume,
       "hwPowerFailureAlarm": hwPowerFailureAlarm,
       "hwPowerFailureResume": hwPowerFailureResume,
       "hwSystemConfigTrap": hwSystemConfigTrap,
       "hwSystemConfigError": hwSystemConfigError,
       "hwSystemConfigResume": hwSystemConfigResume,
       "hwSystemRollback": hwSystemRollback,
       "hwPortTrap": hwPortTrap,
       "hwPortDown": hwPortDown,
       "hwPortUp": hwPortUp,
       "hwUserDefTrap": hwUserDefTrap,
       "hwUserDefAlarm": hwUserDefAlarm,
       "hwUserDefResume": hwUserDefResume,
       "hwCPUTrap": hwCPUTrap,
       "hwCPUUtilizationRising": hwCPUUtilizationRising,
       "hwCPUUtilizationResume": hwCPUUtilizationResume,
       "hwMemoryTrap": hwMemoryTrap,
       "hwMemUtilizationRising": hwMemUtilizationRising,
       "hwMemUtilizationResume": hwMemUtilizationResume,
       "hwStorageDevTrap": hwStorageDevTrap,
       "hwStorageDevRemove": hwStorageDevRemove,
       "hwStorageDevInsert": hwStorageDevInsert,
       "hwPppTrap": hwPppTrap,
       "hwPppLoopbackDetect": hwPppLoopbackDetect,
       "hwPppLoopbackDetResume": hwPppLoopbackDetResume,
       "hwFileStatusTrap": hwFileStatusTrap,
       "hwFileError": hwFileError,
       "hwFileErrorResume": hwFileErrorResume,
       "hwUSBTrap": hwUSBTrap,
       "hwUSBInsert": hwUSBInsert,
       "hwUSBRemove": hwUSBRemove,
       "hwEntityTrapConformance": hwEntityTrapConformance,
       "hwEntityTrapCompliances": hwEntityTrapCompliances,
       "hwEntityTrapCompliance": hwEntityTrapCompliance,
       "hwEntityTrapGroups": hwEntityTrapGroups,
       "hwEntityObjectGroup": hwEntityObjectGroup,
       "hwEntityTrapGroup": hwEntityTrapGroup}
)
