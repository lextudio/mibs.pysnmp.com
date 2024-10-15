# SNMP MIB module (AVAYA-ENTITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AVAYA-ENTITY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:44:30 2024
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

(lsg,) = mibBuilder.importSymbols(
    "AVAYAGEN-MIB",
    "lsg")

(PhysicalIndex,
 entPhysicalDescr,
 entPhysicalIndex,
 entPhysicalParentRelPos) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndex",
    "entPhysicalDescr",
    "entPhysicalIndex",
    "entPhysicalParentRelPos")

(EntitySensorValue,
 entPhySensorValue) = mibBuilder.importSymbols(
    "ENTITY-SENSOR-MIB",
    "EntitySensorValue",
    "entPhySensorValue")

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

(DisplayString,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

avayaEntity = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 99)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AvEntPhyItuPerceivedSeverity(Integer32, TextualConvention):
    status = "current"
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
        *(("cleared", 1),
          ("critical", 3),
          ("indeterminate", 2),
          ("major", 4),
          ("minor", 5),
          ("warning", 6))
    )



# MIB Managed Objects in the order of their OIDs

_AvEntPhySensorTable_Object = MibTable
avEntPhySensorTable = _AvEntPhySensorTable_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 1)
)
if mibBuilder.loadTexts:
    avEntPhySensorTable.setStatus("current")
_AvEntPhySensorEntry_Object = MibTableRow
avEntPhySensorEntry = _AvEntPhySensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 1, 1)
)
avEntPhySensorEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    avEntPhySensorEntry.setStatus("current")
_AvEntPhySensorHiShutdown_Type = EntitySensorValue
_AvEntPhySensorHiShutdown_Object = MibTableColumn
avEntPhySensorHiShutdown = _AvEntPhySensorHiShutdown_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 1, 1, 1),
    _AvEntPhySensorHiShutdown_Type()
)
avEntPhySensorHiShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avEntPhySensorHiShutdown.setStatus("current")
_AvEntPhySensorHiWarning_Type = EntitySensorValue
_AvEntPhySensorHiWarning_Object = MibTableColumn
avEntPhySensorHiWarning = _AvEntPhySensorHiWarning_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 1, 1, 2),
    _AvEntPhySensorHiWarning_Type()
)
avEntPhySensorHiWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avEntPhySensorHiWarning.setStatus("current")
_AvEntPhySensorHiWarningClear_Type = EntitySensorValue
_AvEntPhySensorHiWarningClear_Object = MibTableColumn
avEntPhySensorHiWarningClear = _AvEntPhySensorHiWarningClear_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 1, 1, 3),
    _AvEntPhySensorHiWarningClear_Type()
)
avEntPhySensorHiWarningClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avEntPhySensorHiWarningClear.setStatus("current")
_AvEntPhySensorLoWarningClear_Type = EntitySensorValue
_AvEntPhySensorLoWarningClear_Object = MibTableColumn
avEntPhySensorLoWarningClear = _AvEntPhySensorLoWarningClear_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 1, 1, 4),
    _AvEntPhySensorLoWarningClear_Type()
)
avEntPhySensorLoWarningClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avEntPhySensorLoWarningClear.setStatus("current")
_AvEntPhySensorLoWarning_Type = EntitySensorValue
_AvEntPhySensorLoWarning_Object = MibTableColumn
avEntPhySensorLoWarning = _AvEntPhySensorLoWarning_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 1, 1, 5),
    _AvEntPhySensorLoWarning_Type()
)
avEntPhySensorLoWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avEntPhySensorLoWarning.setStatus("current")
_AvEntPhySensorLoShutdown_Type = EntitySensorValue
_AvEntPhySensorLoShutdown_Object = MibTableColumn
avEntPhySensorLoShutdown = _AvEntPhySensorLoShutdown_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 1, 1, 6),
    _AvEntPhySensorLoShutdown_Type()
)
avEntPhySensorLoShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avEntPhySensorLoShutdown.setStatus("current")
_AvEntPhySensorEventSupportMask_Type = OctetString
_AvEntPhySensorEventSupportMask_Object = MibTableColumn
avEntPhySensorEventSupportMask = _AvEntPhySensorEventSupportMask_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 1, 1, 7),
    _AvEntPhySensorEventSupportMask_Type()
)
avEntPhySensorEventSupportMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avEntPhySensorEventSupportMask.setStatus("current")
_AvEntTraps_ObjectIdentity = ObjectIdentity
avEntTraps = _AvEntTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 2)
)
_AvEntTrapsV3separator_ObjectIdentity = ObjectIdentity
avEntTrapsV3separator = _AvEntTrapsV3separator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 2, 0)
)
_AvEntPhyUSBDevices_ObjectIdentity = ObjectIdentity
avEntPhyUSBDevices = _AvEntPhyUSBDevices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 3)
)
_AvEntPhyUSBDevicesTraps_ObjectIdentity = ObjectIdentity
avEntPhyUSBDevicesTraps = _AvEntPhyUSBDevicesTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 3, 0)
)
_AvEntPhyUSBDevicesTable_Object = MibTable
avEntPhyUSBDevicesTable = _AvEntPhyUSBDevicesTable_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 3, 1)
)
if mibBuilder.loadTexts:
    avEntPhyUSBDevicesTable.setStatus("current")
_AvEntPhyUSBDevicesEntry_Object = MibTableRow
avEntPhyUSBDevicesEntry = _AvEntPhyUSBDevicesEntry_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 3, 1, 1)
)
avEntPhyUSBDevicesEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    avEntPhyUSBDevicesEntry.setStatus("current")


class _AvEntPhyUSBDeviceUSBSupportVersion_Type(DisplayString):
    """Custom type avEntPhyUSBDeviceUSBSupportVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AvEntPhyUSBDeviceUSBSupportVersion_Type.__name__ = "DisplayString"
_AvEntPhyUSBDeviceUSBSupportVersion_Object = MibTableColumn
avEntPhyUSBDeviceUSBSupportVersion = _AvEntPhyUSBDeviceUSBSupportVersion_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 3, 1, 1, 1),
    _AvEntPhyUSBDeviceUSBSupportVersion_Type()
)
avEntPhyUSBDeviceUSBSupportVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avEntPhyUSBDeviceUSBSupportVersion.setStatus("current")
_AvEntPhyUSBDeviceClassCode_Type = Integer32
_AvEntPhyUSBDeviceClassCode_Object = MibTableColumn
avEntPhyUSBDeviceClassCode = _AvEntPhyUSBDeviceClassCode_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 3, 1, 1, 2),
    _AvEntPhyUSBDeviceClassCode_Type()
)
avEntPhyUSBDeviceClassCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avEntPhyUSBDeviceClassCode.setStatus("current")
_AvEntPhyUSBDeviceSubClassCode_Type = Integer32
_AvEntPhyUSBDeviceSubClassCode_Object = MibTableColumn
avEntPhyUSBDeviceSubClassCode = _AvEntPhyUSBDeviceSubClassCode_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 3, 1, 1, 3),
    _AvEntPhyUSBDeviceSubClassCode_Type()
)
avEntPhyUSBDeviceSubClassCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avEntPhyUSBDeviceSubClassCode.setStatus("current")
_AvEntPhyUSBDeviceProtocol_Type = Integer32
_AvEntPhyUSBDeviceProtocol_Object = MibTableColumn
avEntPhyUSBDeviceProtocol = _AvEntPhyUSBDeviceProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 3, 1, 1, 4),
    _AvEntPhyUSBDeviceProtocol_Type()
)
avEntPhyUSBDeviceProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avEntPhyUSBDeviceProtocol.setStatus("current")
_AvEntPhyUSBDeviceVendorId_Type = OctetString
_AvEntPhyUSBDeviceVendorId_Object = MibTableColumn
avEntPhyUSBDeviceVendorId = _AvEntPhyUSBDeviceVendorId_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 3, 1, 1, 5),
    _AvEntPhyUSBDeviceVendorId_Type()
)
avEntPhyUSBDeviceVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avEntPhyUSBDeviceVendorId.setStatus("current")


class _AvEntPhyUSBDeviceSpeed_Type(DisplayString):
    """Custom type avEntPhyUSBDeviceSpeed based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AvEntPhyUSBDeviceSpeed_Type.__name__ = "DisplayString"
_AvEntPhyUSBDeviceSpeed_Object = MibTableColumn
avEntPhyUSBDeviceSpeed = _AvEntPhyUSBDeviceSpeed_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 3, 1, 1, 6),
    _AvEntPhyUSBDeviceSpeed_Type()
)
avEntPhyUSBDeviceSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avEntPhyUSBDeviceSpeed.setStatus("current")


class _AvEntPhyUSBDevicePower_Type(DisplayString):
    """Custom type avEntPhyUSBDevicePower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AvEntPhyUSBDevicePower_Type.__name__ = "DisplayString"
_AvEntPhyUSBDevicePower_Object = MibTableColumn
avEntPhyUSBDevicePower = _AvEntPhyUSBDevicePower_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 3, 1, 1, 7),
    _AvEntPhyUSBDevicePower_Type()
)
avEntPhyUSBDevicePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avEntPhyUSBDevicePower.setStatus("current")
_AvEntPhyUSBDeviceCurrent_Type = Integer32
_AvEntPhyUSBDeviceCurrent_Object = MibTableColumn
avEntPhyUSBDeviceCurrent = _AvEntPhyUSBDeviceCurrent_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 3, 1, 1, 8),
    _AvEntPhyUSBDeviceCurrent_Type()
)
avEntPhyUSBDeviceCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avEntPhyUSBDeviceCurrent.setStatus("current")
_AvEntPhyUSBMassStorageDevicesTable_Object = MibTable
avEntPhyUSBMassStorageDevicesTable = _AvEntPhyUSBMassStorageDevicesTable_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 3, 2)
)
if mibBuilder.loadTexts:
    avEntPhyUSBMassStorageDevicesTable.setStatus("current")
_AvEntPhyUSBMassStorageDevicesEntry_Object = MibTableRow
avEntPhyUSBMassStorageDevicesEntry = _AvEntPhyUSBMassStorageDevicesEntry_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 3, 2, 1)
)
avEntPhyUSBMassStorageDevicesEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    avEntPhyUSBMassStorageDevicesEntry.setStatus("current")


class _AvEntPhyUSBMassStorageDeviceFileSystemName_Type(DisplayString):
    """Custom type avEntPhyUSBMassStorageDeviceFileSystemName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AvEntPhyUSBMassStorageDeviceFileSystemName_Type.__name__ = "DisplayString"
_AvEntPhyUSBMassStorageDeviceFileSystemName_Object = MibTableColumn
avEntPhyUSBMassStorageDeviceFileSystemName = _AvEntPhyUSBMassStorageDeviceFileSystemName_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 3, 2, 1, 1),
    _AvEntPhyUSBMassStorageDeviceFileSystemName_Type()
)
avEntPhyUSBMassStorageDeviceFileSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avEntPhyUSBMassStorageDeviceFileSystemName.setStatus("current")
_AvEntPhyUSBMassStorageDeviceCapacity_Type = Integer32
_AvEntPhyUSBMassStorageDeviceCapacity_Object = MibTableColumn
avEntPhyUSBMassStorageDeviceCapacity = _AvEntPhyUSBMassStorageDeviceCapacity_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 3, 2, 1, 2),
    _AvEntPhyUSBMassStorageDeviceCapacity_Type()
)
avEntPhyUSBMassStorageDeviceCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avEntPhyUSBMassStorageDeviceCapacity.setStatus("current")
_AvEntPhyUSBMassStorageDeviceFreeMemory_Type = Integer32
_AvEntPhyUSBMassStorageDeviceFreeMemory_Object = MibTableColumn
avEntPhyUSBMassStorageDeviceFreeMemory = _AvEntPhyUSBMassStorageDeviceFreeMemory_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 3, 2, 1, 3),
    _AvEntPhyUSBMassStorageDeviceFreeMemory_Type()
)
avEntPhyUSBMassStorageDeviceFreeMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avEntPhyUSBMassStorageDeviceFreeMemory.setStatus("current")


class _AvEntPhyUSBMassStorageDeviceFs_Type(DisplayString):
    """Custom type avEntPhyUSBMassStorageDeviceFs based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AvEntPhyUSBMassStorageDeviceFs_Type.__name__ = "DisplayString"
_AvEntPhyUSBMassStorageDeviceFs_Object = MibTableColumn
avEntPhyUSBMassStorageDeviceFs = _AvEntPhyUSBMassStorageDeviceFs_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 3, 2, 1, 4),
    _AvEntPhyUSBMassStorageDeviceFs_Type()
)
avEntPhyUSBMassStorageDeviceFs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avEntPhyUSBMassStorageDeviceFs.setStatus("current")
_AvEntPhyNotificationDefinitions_ObjectIdentity = ObjectIdentity
avEntPhyNotificationDefinitions = _AvEntPhyNotificationDefinitions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 4)
)
_AvEntPhySeverity_Type = AvEntPhyItuPerceivedSeverity
_AvEntPhySeverity_Object = MibScalar
avEntPhySeverity = _AvEntPhySeverity_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 4, 1),
    _AvEntPhySeverity_Type()
)
avEntPhySeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    avEntPhySeverity.setStatus("current")


class _AvEntPhyProductId_Type(DisplayString):
    """Custom type avEntPhyProductId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_AvEntPhyProductId_Type.__name__ = "DisplayString"
_AvEntPhyProductId_Object = MibScalar
avEntPhyProductId = _AvEntPhyProductId_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 4, 2),
    _AvEntPhyProductId_Type()
)
avEntPhyProductId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    avEntPhyProductId.setStatus("current")
_AvEntPhysicalIndex_Type = PhysicalIndex
_AvEntPhysicalIndex_Object = MibScalar
avEntPhysicalIndex = _AvEntPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 4, 3),
    _AvEntPhysicalIndex_Type()
)
avEntPhysicalIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    avEntPhysicalIndex.setStatus("current")
_AvEntPhyChFru_ObjectIdentity = ObjectIdentity
avEntPhyChFru = _AvEntPhyChFru_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 5)
)
_AvEntPhyChFruNotifications_ObjectIdentity = ObjectIdentity
avEntPhyChFruNotifications = _AvEntPhyChFruNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 5, 0)
)
_AvEntPhyChFruTable_Object = MibTable
avEntPhyChFruTable = _AvEntPhyChFruTable_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 5, 1)
)
if mibBuilder.loadTexts:
    avEntPhyChFruTable.setStatus("current")
_AvEntPhyChFruEntry_Object = MibTableRow
avEntPhyChFruEntry = _AvEntPhyChFruEntry_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 5, 1, 1)
)
avEntPhyChFruEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    avEntPhyChFruEntry.setStatus("current")


class _AvEntPhyChFruOperStat_Type(Integer32):
    """Custom type avEntPhyChFruOperStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("fault", 2),
          ("notPresent", 3),
          ("ok", 1),
          ("unknown", 255))
    )


_AvEntPhyChFruOperStat_Type.__name__ = "Integer32"
_AvEntPhyChFruOperStat_Object = MibTableColumn
avEntPhyChFruOperStat = _AvEntPhyChFruOperStat_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 5, 1, 1, 1),
    _AvEntPhyChFruOperStat_Type()
)
avEntPhyChFruOperStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avEntPhyChFruOperStat.setStatus("current")


class _AvEntPhyChFruFault_Type(Integer32):
    """Custom type avEntPhyChFruFault based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("acFault", 3),
          ("badExpansionCable", 7),
          ("malfunctionAndAcFault", 4),
          ("mulfunction", 2),
          ("multipleFanFault", 6),
          ("none", 1),
          ("singleFanFault", 5),
          ("unknown", 255))
    )


_AvEntPhyChFruFault_Type.__name__ = "Integer32"
_AvEntPhyChFruFault_Object = MibTableColumn
avEntPhyChFruFault = _AvEntPhyChFruFault_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 5, 1, 1, 2),
    _AvEntPhyChFruFault_Type()
)
avEntPhyChFruFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avEntPhyChFruFault.setStatus("current")

# Managed Objects groups

avEntPhyChFruGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 5, 2)
)
avEntPhyChFruGroup.setObjects(
      *(("AVAYA-ENTITY-MIB", "avEntPhyChFruOperStat"),
        ("AVAYA-ENTITY-MIB", "avEntPhyChFruFault"))
)
if mibBuilder.loadTexts:
    avEntPhyChFruGroup.setStatus("current")


# Notification objects

avEntFanFlt = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 2, 0, 1)
)
avEntFanFlt.setObjects(
      *(("AVAYA-ENTITY-MIB", "avEntPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalDescr"),
        ("ENTITY-SENSOR-MIB", "entPhySensorValue"),
        ("AVAYA-ENTITY-MIB", "avEntPhySensorLoWarning"))
)
if mibBuilder.loadTexts:
    avEntFanFlt.setStatus(
        "current"
    )

avEntFanOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 2, 0, 2)
)
avEntFanOk.setObjects(
      *(("AVAYA-ENTITY-MIB", "avEntPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalDescr"),
        ("ENTITY-SENSOR-MIB", "entPhySensorValue"),
        ("AVAYA-ENTITY-MIB", "avEntPhySensorLoWarningClear"))
)
if mibBuilder.loadTexts:
    avEntFanOk.setStatus(
        "current"
    )

avEnt48vPwrFlt = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 2, 0, 4)
)
avEnt48vPwrFlt.setObjects(
      *(("AVAYA-ENTITY-MIB", "avEntPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalDescr"),
        ("ENTITY-SENSOR-MIB", "entPhySensorValue"),
        ("AVAYA-ENTITY-MIB", "avEntPhySensorHiWarning"),
        ("AVAYA-ENTITY-MIB", "avEntPhySensorLoWarning"),
        ("ENTITY-MIB", "entPhysicalParentRelPos"))
)
if mibBuilder.loadTexts:
    avEnt48vPwrFlt.setStatus(
        "current"
    )

avEnt48vPwrFltOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 2, 0, 5)
)
avEnt48vPwrFltOk.setObjects(
      *(("AVAYA-ENTITY-MIB", "avEntPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalDescr"),
        ("ENTITY-SENSOR-MIB", "entPhySensorValue"),
        ("AVAYA-ENTITY-MIB", "avEntPhySensorHiWarningClear"),
        ("AVAYA-ENTITY-MIB", "avEntPhySensorLoWarningClear"),
        ("ENTITY-MIB", "entPhysicalParentRelPos"))
)
if mibBuilder.loadTexts:
    avEnt48vPwrFltOk.setStatus(
        "current"
    )

avEnt5vPwrFlt = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 2, 0, 7)
)
avEnt5vPwrFlt.setObjects(
      *(("AVAYA-ENTITY-MIB", "avEntPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalDescr"),
        ("ENTITY-SENSOR-MIB", "entPhySensorValue"),
        ("AVAYA-ENTITY-MIB", "avEntPhySensorHiWarning"),
        ("AVAYA-ENTITY-MIB", "avEntPhySensorLoWarning"),
        ("ENTITY-MIB", "entPhysicalParentRelPos"))
)
if mibBuilder.loadTexts:
    avEnt5vPwrFlt.setStatus(
        "current"
    )

avEnt5vPwrFltOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 2, 0, 8)
)
avEnt5vPwrFltOk.setObjects(
      *(("AVAYA-ENTITY-MIB", "avEntPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalDescr"),
        ("ENTITY-SENSOR-MIB", "entPhySensorValue"),
        ("AVAYA-ENTITY-MIB", "avEntPhySensorHiWarningClear"),
        ("AVAYA-ENTITY-MIB", "avEntPhySensorLoWarningClear"),
        ("ENTITY-MIB", "entPhysicalParentRelPos"))
)
if mibBuilder.loadTexts:
    avEnt5vPwrFltOk.setStatus(
        "current"
    )

avEnt3300mvPwrFlt = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 2, 0, 10)
)
avEnt3300mvPwrFlt.setObjects(
      *(("AVAYA-ENTITY-MIB", "avEntPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalDescr"),
        ("ENTITY-SENSOR-MIB", "entPhySensorValue"),
        ("AVAYA-ENTITY-MIB", "avEntPhySensorHiWarning"),
        ("AVAYA-ENTITY-MIB", "avEntPhySensorLoWarning"),
        ("ENTITY-MIB", "entPhysicalParentRelPos"))
)
if mibBuilder.loadTexts:
    avEnt3300mvPwrFlt.setStatus(
        "current"
    )

avEnt3300mvPwrFltOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 2, 0, 11)
)
avEnt3300mvPwrFltOk.setObjects(
      *(("AVAYA-ENTITY-MIB", "avEntPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalDescr"),
        ("ENTITY-SENSOR-MIB", "entPhySensorValue"),
        ("AVAYA-ENTITY-MIB", "avEntPhySensorHiWarningClear"),
        ("AVAYA-ENTITY-MIB", "avEntPhySensorLoWarningClear"),
        ("ENTITY-MIB", "entPhysicalParentRelPos"))
)
if mibBuilder.loadTexts:
    avEnt3300mvPwrFltOk.setStatus(
        "current"
    )

avEnt2500mvPwrFlt = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 2, 0, 13)
)
avEnt2500mvPwrFlt.setObjects(
      *(("AVAYA-ENTITY-MIB", "avEntPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalDescr"),
        ("ENTITY-SENSOR-MIB", "entPhySensorValue"),
        ("AVAYA-ENTITY-MIB", "avEntPhySensorHiWarning"),
        ("AVAYA-ENTITY-MIB", "avEntPhySensorLoWarning"),
        ("ENTITY-MIB", "entPhysicalParentRelPos"))
)
if mibBuilder.loadTexts:
    avEnt2500mvPwrFlt.setStatus(
        "current"
    )

avEnt2500mvPwrFltOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 2, 0, 14)
)
avEnt2500mvPwrFltOk.setObjects(
      *(("AVAYA-ENTITY-MIB", "avEntPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalDescr"),
        ("ENTITY-SENSOR-MIB", "entPhySensorValue"),
        ("AVAYA-ENTITY-MIB", "avEntPhySensorHiWarningClear"),
        ("AVAYA-ENTITY-MIB", "avEntPhySensorLoWarningClear"),
        ("ENTITY-MIB", "entPhysicalParentRelPos"))
)
if mibBuilder.loadTexts:
    avEnt2500mvPwrFltOk.setStatus(
        "current"
    )

avEnt1800mvPwrFlt = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 2, 0, 16)
)
avEnt1800mvPwrFlt.setObjects(
      *(("AVAYA-ENTITY-MIB", "avEntPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalDescr"),
        ("ENTITY-SENSOR-MIB", "entPhySensorValue"),
        ("AVAYA-ENTITY-MIB", "avEntPhySensorHiWarning"),
        ("AVAYA-ENTITY-MIB", "avEntPhySensorLoWarning"),
        ("ENTITY-MIB", "entPhysicalParentRelPos"))
)
if mibBuilder.loadTexts:
    avEnt1800mvPwrFlt.setStatus(
        "current"
    )

avEnt1800mvPwrFltOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 2, 0, 17)
)
avEnt1800mvPwrFltOk.setObjects(
      *(("AVAYA-ENTITY-MIB", "avEntPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalDescr"),
        ("ENTITY-SENSOR-MIB", "entPhySensorValue"),
        ("AVAYA-ENTITY-MIB", "avEntPhySensorHiWarningClear"),
        ("AVAYA-ENTITY-MIB", "avEntPhySensorLoWarningClear"),
        ("ENTITY-MIB", "entPhysicalParentRelPos"))
)
if mibBuilder.loadTexts:
    avEnt1800mvPwrFltOk.setStatus(
        "current"
    )

avEnt1600mvPwrFlt = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 2, 0, 19)
)
avEnt1600mvPwrFlt.setObjects(
      *(("AVAYA-ENTITY-MIB", "avEntPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalDescr"),
        ("ENTITY-SENSOR-MIB", "entPhySensorValue"),
        ("AVAYA-ENTITY-MIB", "avEntPhySensorHiWarning"),
        ("AVAYA-ENTITY-MIB", "avEntPhySensorLoWarning"),
        ("ENTITY-MIB", "entPhysicalParentRelPos"))
)
if mibBuilder.loadTexts:
    avEnt1600mvPwrFlt.setStatus(
        "current"
    )

avEnt1600mvPwrFltOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 2, 0, 20)
)
avEnt1600mvPwrFltOk.setObjects(
      *(("AVAYA-ENTITY-MIB", "avEntPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalDescr"),
        ("ENTITY-SENSOR-MIB", "entPhySensorValue"),
        ("AVAYA-ENTITY-MIB", "avEntPhySensorHiWarningClear"),
        ("AVAYA-ENTITY-MIB", "avEntPhySensorLoWarningClear"),
        ("ENTITY-MIB", "entPhysicalParentRelPos"))
)
if mibBuilder.loadTexts:
    avEnt1600mvPwrFltOk.setStatus(
        "current"
    )

avEntAmbientHiTempFlt = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 2, 0, 22)
)
avEntAmbientHiTempFlt.setObjects(
      *(("AVAYA-ENTITY-MIB", "avEntPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalDescr"),
        ("ENTITY-SENSOR-MIB", "entPhySensorValue"),
        ("AVAYA-ENTITY-MIB", "avEntPhySensorHiWarning"),
        ("ENTITY-MIB", "entPhysicalParentRelPos"))
)
if mibBuilder.loadTexts:
    avEntAmbientHiTempFlt.setStatus(
        "current"
    )

avEntAmbientHiTempFltOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 2, 0, 23)
)
avEntAmbientHiTempFltOk.setObjects(
      *(("AVAYA-ENTITY-MIB", "avEntPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalDescr"),
        ("ENTITY-SENSOR-MIB", "entPhySensorValue"),
        ("AVAYA-ENTITY-MIB", "avEntPhySensorHiWarningClear"),
        ("ENTITY-MIB", "entPhysicalParentRelPos"))
)
if mibBuilder.loadTexts:
    avEntAmbientHiTempFltOk.setStatus(
        "current"
    )

avEntAmbientLoTempFlt = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 2, 0, 24)
)
avEntAmbientLoTempFlt.setObjects(
      *(("AVAYA-ENTITY-MIB", "avEntPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalDescr"),
        ("ENTITY-SENSOR-MIB", "entPhySensorValue"),
        ("AVAYA-ENTITY-MIB", "avEntPhySensorLoWarning"),
        ("ENTITY-MIB", "entPhysicalParentRelPos"))
)
if mibBuilder.loadTexts:
    avEntAmbientLoTempFlt.setStatus(
        "current"
    )

avEntAmbientLoTempFltOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 2, 0, 25)
)
avEntAmbientLoTempFltOk.setObjects(
      *(("AVAYA-ENTITY-MIB", "avEntPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalDescr"),
        ("ENTITY-SENSOR-MIB", "entPhySensorValue"),
        ("AVAYA-ENTITY-MIB", "avEntPhySensorLoWarningClear"),
        ("ENTITY-MIB", "entPhysicalParentRelPos"))
)
if mibBuilder.loadTexts:
    avEntAmbientLoTempFltOk.setStatus(
        "current"
    )

avEntPhyUSBDeviceRemovalOnBackupRestoreOperation = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 3, 0, 1)
)
avEntPhyUSBDeviceRemovalOnBackupRestoreOperation.setObjects(
      *(("AVAYA-ENTITY-MIB", "avEntPhyProductId"),
        ("AVAYA-ENTITY-MIB", "avEntPhySeverity"))
)
if mibBuilder.loadTexts:
    avEntPhyUSBDeviceRemovalOnBackupRestoreOperation.setStatus(
        "current"
    )

avEntPhyUSBDeviceInsecureRemoval = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 3, 0, 2)
)
avEntPhyUSBDeviceInsecureRemoval.setObjects(
      *(("AVAYA-ENTITY-MIB", "avEntPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalDescr"),
        ("AVAYA-ENTITY-MIB", "avEntPhyUSBDeviceUSBSupportVersion"),
        ("AVAYA-ENTITY-MIB", "avEntPhyUSBDeviceSpeed"),
        ("AVAYA-ENTITY-MIB", "avEntPhyUSBDevicePower"),
        ("AVAYA-ENTITY-MIB", "avEntPhyProductId"),
        ("AVAYA-ENTITY-MIB", "avEntPhySeverity"))
)
if mibBuilder.loadTexts:
    avEntPhyUSBDeviceInsecureRemoval.setStatus(
        "current"
    )

avEntPhyUSBDevicePowerFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 3, 0, 3)
)
avEntPhyUSBDevicePowerFailure.setObjects(
      *(("AVAYA-ENTITY-MIB", "avEntPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalDescr"),
        ("AVAYA-ENTITY-MIB", "avEntPhyUSBDeviceUSBSupportVersion"),
        ("AVAYA-ENTITY-MIB", "avEntPhyUSBDeviceSpeed"),
        ("AVAYA-ENTITY-MIB", "avEntPhyUSBDevicePower"),
        ("AVAYA-ENTITY-MIB", "avEntPhyProductId"),
        ("AVAYA-ENTITY-MIB", "avEntPhySeverity"))
)
if mibBuilder.loadTexts:
    avEntPhyUSBDevicePowerFailure.setStatus(
        "current"
    )

avEntPhyUSBDeviceNotSupported = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 3, 0, 4)
)
avEntPhyUSBDeviceNotSupported.setObjects(
      *(("AVAYA-ENTITY-MIB", "avEntPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalDescr"),
        ("AVAYA-ENTITY-MIB", "avEntPhyUSBDeviceUSBSupportVersion"),
        ("AVAYA-ENTITY-MIB", "avEntPhyUSBDeviceSpeed"),
        ("AVAYA-ENTITY-MIB", "avEntPhyUSBDevicePower"),
        ("AVAYA-ENTITY-MIB", "avEntPhyProductId"),
        ("AVAYA-ENTITY-MIB", "avEntPhySeverity"))
)
if mibBuilder.loadTexts:
    avEntPhyUSBDeviceNotSupported.setStatus(
        "current"
    )

avEntPhyUSBDeviceExceedMaxNumber = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 3, 0, 5)
)
avEntPhyUSBDeviceExceedMaxNumber.setObjects(
      *(("AVAYA-ENTITY-MIB", "avEntPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalDescr"),
        ("AVAYA-ENTITY-MIB", "avEntPhyUSBDeviceUSBSupportVersion"),
        ("AVAYA-ENTITY-MIB", "avEntPhyUSBDeviceSpeed"),
        ("AVAYA-ENTITY-MIB", "avEntPhyUSBDevicePower"),
        ("AVAYA-ENTITY-MIB", "avEntPhyProductId"),
        ("AVAYA-ENTITY-MIB", "avEntPhySeverity"))
)
if mibBuilder.loadTexts:
    avEntPhyUSBDeviceExceedMaxNumber.setStatus(
        "current"
    )

avEntPhyUSBFileSystemNotSupported = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 3, 0, 6)
)
avEntPhyUSBFileSystemNotSupported.setObjects(
      *(("AVAYA-ENTITY-MIB", "avEntPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalDescr"),
        ("AVAYA-ENTITY-MIB", "avEntPhyUSBDeviceUSBSupportVersion"),
        ("AVAYA-ENTITY-MIB", "avEntPhyUSBDeviceSpeed"),
        ("AVAYA-ENTITY-MIB", "avEntPhyUSBDevicePower"),
        ("AVAYA-ENTITY-MIB", "avEntPhyProductId"),
        ("AVAYA-ENTITY-MIB", "avEntPhySeverity"))
)
if mibBuilder.loadTexts:
    avEntPhyUSBFileSystemNotSupported.setStatus(
        "current"
    )

avEntPhyChFruRemoval = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 5, 0, 1)
)
avEntPhyChFruRemoval.setObjects(
      *(("AVAYA-ENTITY-MIB", "avEntPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalDescr"),
        ("AVAYA-ENTITY-MIB", "avEntPhyProductId"),
        ("AVAYA-ENTITY-MIB", "avEntPhySeverity"))
)
if mibBuilder.loadTexts:
    avEntPhyChFruRemoval.setStatus(
        "current"
    )

avEntPhyChFruInsertion = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 5, 0, 2)
)
avEntPhyChFruInsertion.setObjects(
      *(("AVAYA-ENTITY-MIB", "avEntPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalDescr"),
        ("AVAYA-ENTITY-MIB", "avEntPhyProductId"),
        ("AVAYA-ENTITY-MIB", "avEntPhySeverity"))
)
if mibBuilder.loadTexts:
    avEntPhyChFruInsertion.setStatus(
        "current"
    )

avEntPhyChFruPsuFlt = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 5, 0, 3)
)
avEntPhyChFruPsuFlt.setObjects(
      *(("AVAYA-ENTITY-MIB", "avEntPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalDescr"),
        ("AVAYA-ENTITY-MIB", "avEntPhyChFruOperStat"),
        ("AVAYA-ENTITY-MIB", "avEntPhyChFruFault"),
        ("AVAYA-ENTITY-MIB", "avEntPhyProductId"),
        ("AVAYA-ENTITY-MIB", "avEntPhySeverity"))
)
if mibBuilder.loadTexts:
    avEntPhyChFruPsuFlt.setStatus(
        "current"
    )

avEntPhyChFruPsuFltOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 5, 0, 4)
)
avEntPhyChFruPsuFltOk.setObjects(
      *(("AVAYA-ENTITY-MIB", "avEntPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalDescr"),
        ("AVAYA-ENTITY-MIB", "avEntPhyChFruOperStat"),
        ("AVAYA-ENTITY-MIB", "avEntPhyChFruFault"),
        ("AVAYA-ENTITY-MIB", "avEntPhyProductId"),
        ("AVAYA-ENTITY-MIB", "avEntPhySeverity"))
)
if mibBuilder.loadTexts:
    avEntPhyChFruPsuFltOk.setStatus(
        "current"
    )

avEntPhyChFruExpansionTestFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 5, 0, 5)
)
avEntPhyChFruExpansionTestFailure.setObjects(
      *(("AVAYA-ENTITY-MIB", "avEntPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalDescr"),
        ("AVAYA-ENTITY-MIB", "avEntPhyChFruOperStat"),
        ("AVAYA-ENTITY-MIB", "avEntPhyChFruFault"),
        ("AVAYA-ENTITY-MIB", "avEntPhyProductId"),
        ("AVAYA-ENTITY-MIB", "avEntPhySeverity"))
)
if mibBuilder.loadTexts:
    avEntPhyChFruExpansionTestFailure.setStatus(
        "current"
    )

avEntPhyChFruExpansionTestClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 5, 0, 6)
)
avEntPhyChFruExpansionTestClear.setObjects(
      *(("AVAYA-ENTITY-MIB", "avEntPhysicalIndex"),
        ("ENTITY-MIB", "entPhysicalDescr"),
        ("AVAYA-ENTITY-MIB", "avEntPhyChFruOperStat"),
        ("AVAYA-ENTITY-MIB", "avEntPhyChFruFault"),
        ("AVAYA-ENTITY-MIB", "avEntPhyProductId"),
        ("AVAYA-ENTITY-MIB", "avEntPhySeverity"))
)
if mibBuilder.loadTexts:
    avEntPhyChFruExpansionTestClear.setStatus(
        "current"
    )


# Notifications groups

avEntPhyChFruNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 99, 5, 3)
)
avEntPhyChFruNotificationGroup.setObjects(
      *(("AVAYA-ENTITY-MIB", "avEntPhyChFruRemoval"),
        ("AVAYA-ENTITY-MIB", "avEntPhyChFruInsertion"),
        ("AVAYA-ENTITY-MIB", "avEntPhyChFruPsuFlt"),
        ("AVAYA-ENTITY-MIB", "avEntPhyChFruPsuFltOk"))
)
if mibBuilder.loadTexts:
    avEntPhyChFruNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AVAYA-ENTITY-MIB",
    **{"AvEntPhyItuPerceivedSeverity": AvEntPhyItuPerceivedSeverity,
       "avayaEntity": avayaEntity,
       "avEntPhySensorTable": avEntPhySensorTable,
       "avEntPhySensorEntry": avEntPhySensorEntry,
       "avEntPhySensorHiShutdown": avEntPhySensorHiShutdown,
       "avEntPhySensorHiWarning": avEntPhySensorHiWarning,
       "avEntPhySensorHiWarningClear": avEntPhySensorHiWarningClear,
       "avEntPhySensorLoWarningClear": avEntPhySensorLoWarningClear,
       "avEntPhySensorLoWarning": avEntPhySensorLoWarning,
       "avEntPhySensorLoShutdown": avEntPhySensorLoShutdown,
       "avEntPhySensorEventSupportMask": avEntPhySensorEventSupportMask,
       "avEntTraps": avEntTraps,
       "avEntTrapsV3separator": avEntTrapsV3separator,
       "avEntFanFlt": avEntFanFlt,
       "avEntFanOk": avEntFanOk,
       "avEnt48vPwrFlt": avEnt48vPwrFlt,
       "avEnt48vPwrFltOk": avEnt48vPwrFltOk,
       "avEnt5vPwrFlt": avEnt5vPwrFlt,
       "avEnt5vPwrFltOk": avEnt5vPwrFltOk,
       "avEnt3300mvPwrFlt": avEnt3300mvPwrFlt,
       "avEnt3300mvPwrFltOk": avEnt3300mvPwrFltOk,
       "avEnt2500mvPwrFlt": avEnt2500mvPwrFlt,
       "avEnt2500mvPwrFltOk": avEnt2500mvPwrFltOk,
       "avEnt1800mvPwrFlt": avEnt1800mvPwrFlt,
       "avEnt1800mvPwrFltOk": avEnt1800mvPwrFltOk,
       "avEnt1600mvPwrFlt": avEnt1600mvPwrFlt,
       "avEnt1600mvPwrFltOk": avEnt1600mvPwrFltOk,
       "avEntAmbientHiTempFlt": avEntAmbientHiTempFlt,
       "avEntAmbientHiTempFltOk": avEntAmbientHiTempFltOk,
       "avEntAmbientLoTempFlt": avEntAmbientLoTempFlt,
       "avEntAmbientLoTempFltOk": avEntAmbientLoTempFltOk,
       "avEntPhyUSBDevices": avEntPhyUSBDevices,
       "avEntPhyUSBDevicesTraps": avEntPhyUSBDevicesTraps,
       "avEntPhyUSBDeviceRemovalOnBackupRestoreOperation": avEntPhyUSBDeviceRemovalOnBackupRestoreOperation,
       "avEntPhyUSBDeviceInsecureRemoval": avEntPhyUSBDeviceInsecureRemoval,
       "avEntPhyUSBDevicePowerFailure": avEntPhyUSBDevicePowerFailure,
       "avEntPhyUSBDeviceNotSupported": avEntPhyUSBDeviceNotSupported,
       "avEntPhyUSBDeviceExceedMaxNumber": avEntPhyUSBDeviceExceedMaxNumber,
       "avEntPhyUSBFileSystemNotSupported": avEntPhyUSBFileSystemNotSupported,
       "avEntPhyUSBDevicesTable": avEntPhyUSBDevicesTable,
       "avEntPhyUSBDevicesEntry": avEntPhyUSBDevicesEntry,
       "avEntPhyUSBDeviceUSBSupportVersion": avEntPhyUSBDeviceUSBSupportVersion,
       "avEntPhyUSBDeviceClassCode": avEntPhyUSBDeviceClassCode,
       "avEntPhyUSBDeviceSubClassCode": avEntPhyUSBDeviceSubClassCode,
       "avEntPhyUSBDeviceProtocol": avEntPhyUSBDeviceProtocol,
       "avEntPhyUSBDeviceVendorId": avEntPhyUSBDeviceVendorId,
       "avEntPhyUSBDeviceSpeed": avEntPhyUSBDeviceSpeed,
       "avEntPhyUSBDevicePower": avEntPhyUSBDevicePower,
       "avEntPhyUSBDeviceCurrent": avEntPhyUSBDeviceCurrent,
       "avEntPhyUSBMassStorageDevicesTable": avEntPhyUSBMassStorageDevicesTable,
       "avEntPhyUSBMassStorageDevicesEntry": avEntPhyUSBMassStorageDevicesEntry,
       "avEntPhyUSBMassStorageDeviceFileSystemName": avEntPhyUSBMassStorageDeviceFileSystemName,
       "avEntPhyUSBMassStorageDeviceCapacity": avEntPhyUSBMassStorageDeviceCapacity,
       "avEntPhyUSBMassStorageDeviceFreeMemory": avEntPhyUSBMassStorageDeviceFreeMemory,
       "avEntPhyUSBMassStorageDeviceFs": avEntPhyUSBMassStorageDeviceFs,
       "avEntPhyNotificationDefinitions": avEntPhyNotificationDefinitions,
       "avEntPhySeverity": avEntPhySeverity,
       "avEntPhyProductId": avEntPhyProductId,
       "avEntPhysicalIndex": avEntPhysicalIndex,
       "avEntPhyChFru": avEntPhyChFru,
       "avEntPhyChFruNotifications": avEntPhyChFruNotifications,
       "avEntPhyChFruRemoval": avEntPhyChFruRemoval,
       "avEntPhyChFruInsertion": avEntPhyChFruInsertion,
       "avEntPhyChFruPsuFlt": avEntPhyChFruPsuFlt,
       "avEntPhyChFruPsuFltOk": avEntPhyChFruPsuFltOk,
       "avEntPhyChFruExpansionTestFailure": avEntPhyChFruExpansionTestFailure,
       "avEntPhyChFruExpansionTestClear": avEntPhyChFruExpansionTestClear,
       "avEntPhyChFruTable": avEntPhyChFruTable,
       "avEntPhyChFruEntry": avEntPhyChFruEntry,
       "avEntPhyChFruOperStat": avEntPhyChFruOperStat,
       "avEntPhyChFruFault": avEntPhyChFruFault,
       "avEntPhyChFruGroup": avEntPhyChFruGroup,
       "avEntPhyChFruNotificationGroup": avEntPhyChFruNotificationGroup}
)
