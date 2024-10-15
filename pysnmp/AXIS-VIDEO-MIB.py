# SNMP MIB module (AXIS-VIDEO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AXIS-VIDEO-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:44:58 2024
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

(axis,
 products) = mibBuilder.importSymbols(
    "AXIS-ROOT-MIB",
    "axis",
    "products")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

video = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 368, 4)
)
video.setRevisions(
        ("2016-09-23 12:18",
         "2012-12-12 12:02")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VideoBased_ObjectIdentity = ObjectIdentity
videoBased = _VideoBased_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 368, 1, 1)
)
_VideoObjects_ObjectIdentity = ObjectIdentity
videoObjects = _VideoObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 368, 4, 1)
)
_PowerSupplyTable_Object = MibTable
powerSupplyTable = _PowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 368, 4, 1, 1)
)
if mibBuilder.loadTexts:
    powerSupplyTable.setStatus("current")
_PowerSupplyEntry_Object = MibTableRow
powerSupplyEntry = _PowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 368, 4, 1, 1, 1)
)
powerSupplyEntry.setIndexNames(
    (0, "AXIS-VIDEO-MIB", "powerSupplyType"),
    (0, "AXIS-VIDEO-MIB", "powerSupplyId"),
)
if mibBuilder.loadTexts:
    powerSupplyEntry.setStatus("current")


class _PowerSupplyType_Type(Integer32):
    """Custom type powerSupplyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("common", 1),
          ("external", 3),
          ("internal", 2))
    )


_PowerSupplyType_Type.__name__ = "Integer32"
_PowerSupplyType_Object = MibTableColumn
powerSupplyType = _PowerSupplyType_Object(
    (1, 3, 6, 1, 4, 1, 368, 4, 1, 1, 1, 1),
    _PowerSupplyType_Type()
)
powerSupplyType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    powerSupplyType.setStatus("current")


class _PowerSupplyId_Type(Unsigned32):
    """Custom type powerSupplyId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_PowerSupplyId_Type.__name__ = "Unsigned32"
_PowerSupplyId_Object = MibTableColumn
powerSupplyId = _PowerSupplyId_Object(
    (1, 3, 6, 1, 4, 1, 368, 4, 1, 1, 1, 2),
    _PowerSupplyId_Type()
)
powerSupplyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    powerSupplyId.setStatus("current")


class _PowerSupplyStatus_Type(Integer32):
    """Custom type powerSupplyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failure", 2),
          ("ok", 1))
    )


_PowerSupplyStatus_Type.__name__ = "Integer32"
_PowerSupplyStatus_Object = MibTableColumn
powerSupplyStatus = _PowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 368, 4, 1, 1, 1, 3),
    _PowerSupplyStatus_Type()
)
powerSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerSupplyStatus.setStatus("current")
_FanTable_Object = MibTable
fanTable = _FanTable_Object(
    (1, 3, 6, 1, 4, 1, 368, 4, 1, 2)
)
if mibBuilder.loadTexts:
    fanTable.setStatus("current")
_FanEntry_Object = MibTableRow
fanEntry = _FanEntry_Object(
    (1, 3, 6, 1, 4, 1, 368, 4, 1, 2, 1)
)
fanEntry.setIndexNames(
    (0, "AXIS-VIDEO-MIB", "fanType"),
    (0, "AXIS-VIDEO-MIB", "fanId"),
)
if mibBuilder.loadTexts:
    fanEntry.setStatus("current")


class _FanType_Type(Integer32):
    """Custom type fanType based on Integer32"""
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
        *(("common", 1),
          ("cpu", 4),
          ("housing", 2),
          ("rack", 3))
    )


_FanType_Type.__name__ = "Integer32"
_FanType_Object = MibTableColumn
fanType = _FanType_Object(
    (1, 3, 6, 1, 4, 1, 368, 4, 1, 2, 1, 1),
    _FanType_Type()
)
fanType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fanType.setStatus("current")


class _FanId_Type(Unsigned32):
    """Custom type fanId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_FanId_Type.__name__ = "Unsigned32"
_FanId_Object = MibTableColumn
fanId = _FanId_Object(
    (1, 3, 6, 1, 4, 1, 368, 4, 1, 2, 1, 2),
    _FanId_Type()
)
fanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fanId.setStatus("current")


class _FanStatus_Type(Integer32):
    """Custom type fanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failure", 2),
          ("ok", 1))
    )


_FanStatus_Type.__name__ = "Integer32"
_FanStatus_Object = MibTableColumn
fanStatus = _FanStatus_Object(
    (1, 3, 6, 1, 4, 1, 368, 4, 1, 2, 1, 3),
    _FanStatus_Type()
)
fanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanStatus.setStatus("current")
_TempSensorTable_Object = MibTable
tempSensorTable = _TempSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 368, 4, 1, 3)
)
if mibBuilder.loadTexts:
    tempSensorTable.setStatus("current")
_TempSensorEntry_Object = MibTableRow
tempSensorEntry = _TempSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 368, 4, 1, 3, 1)
)
tempSensorEntry.setIndexNames(
    (0, "AXIS-VIDEO-MIB", "tempSensorType"),
    (0, "AXIS-VIDEO-MIB", "tempSensorId"),
)
if mibBuilder.loadTexts:
    tempSensorEntry.setStatus("current")


class _TempSensorType_Type(Integer32):
    """Custom type tempSensorType based on Integer32"""
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
        *(("common", 1),
          ("cpu", 4),
          ("housing", 2),
          ("rack", 3))
    )


_TempSensorType_Type.__name__ = "Integer32"
_TempSensorType_Object = MibTableColumn
tempSensorType = _TempSensorType_Object(
    (1, 3, 6, 1, 4, 1, 368, 4, 1, 3, 1, 1),
    _TempSensorType_Type()
)
tempSensorType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tempSensorType.setStatus("current")


class _TempSensorId_Type(Unsigned32):
    """Custom type tempSensorId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_TempSensorId_Type.__name__ = "Unsigned32"
_TempSensorId_Object = MibTableColumn
tempSensorId = _TempSensorId_Object(
    (1, 3, 6, 1, 4, 1, 368, 4, 1, 3, 1, 2),
    _TempSensorId_Type()
)
tempSensorId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tempSensorId.setStatus("current")


class _TempSensorStatus_Type(Integer32):
    """Custom type tempSensorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failure", 2),
          ("ok", 1),
          ("outOfBoundary", 3))
    )


_TempSensorStatus_Type.__name__ = "Integer32"
_TempSensorStatus_Object = MibTableColumn
tempSensorStatus = _TempSensorStatus_Object(
    (1, 3, 6, 1, 4, 1, 368, 4, 1, 3, 1, 3),
    _TempSensorStatus_Type()
)
tempSensorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempSensorStatus.setStatus("current")


class _TempSensorValue_Type(Integer32):
    """Custom type tempSensorValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-176, 150),
    )


_TempSensorValue_Type.__name__ = "Integer32"
_TempSensorValue_Object = MibTableColumn
tempSensorValue = _TempSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 368, 4, 1, 3, 1, 4),
    _TempSensorValue_Type()
)
tempSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempSensorValue.setStatus("current")
_VideoChannelTable_Object = MibTable
videoChannelTable = _VideoChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 368, 4, 1, 4)
)
if mibBuilder.loadTexts:
    videoChannelTable.setStatus("current")
_VideoChannelEntry_Object = MibTableRow
videoChannelEntry = _VideoChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 368, 4, 1, 4, 1)
)
videoChannelEntry.setIndexNames(
    (0, "AXIS-VIDEO-MIB", "videoChannelId"),
)
if mibBuilder.loadTexts:
    videoChannelEntry.setStatus("current")


class _VideoChannelId_Type(Unsigned32):
    """Custom type videoChannelId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8192),
    )


_VideoChannelId_Type.__name__ = "Unsigned32"
_VideoChannelId_Object = MibTableColumn
videoChannelId = _VideoChannelId_Object(
    (1, 3, 6, 1, 4, 1, 368, 4, 1, 4, 1, 1),
    _VideoChannelId_Type()
)
videoChannelId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    videoChannelId.setStatus("current")


class _VideoSignalStatus_Type(Integer32):
    """Custom type videoSignalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noSignal", 2),
          ("signalOk", 1))
    )


_VideoSignalStatus_Type.__name__ = "Integer32"
_VideoSignalStatus_Object = MibTableColumn
videoSignalStatus = _VideoSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 368, 4, 1, 4, 1, 2),
    _VideoSignalStatus_Type()
)
videoSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    videoSignalStatus.setStatus("current")
_AudioChannelTable_Object = MibTable
audioChannelTable = _AudioChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 368, 4, 1, 5)
)
if mibBuilder.loadTexts:
    audioChannelTable.setStatus("current")
_AudioChannelEntry_Object = MibTableRow
audioChannelEntry = _AudioChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 368, 4, 1, 5, 1)
)
audioChannelEntry.setIndexNames(
    (0, "AXIS-VIDEO-MIB", "audioChannelId"),
)
if mibBuilder.loadTexts:
    audioChannelEntry.setStatus("current")


class _AudioChannelId_Type(Unsigned32):
    """Custom type audioChannelId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8192),
    )


_AudioChannelId_Type.__name__ = "Unsigned32"
_AudioChannelId_Object = MibTableColumn
audioChannelId = _AudioChannelId_Object(
    (1, 3, 6, 1, 4, 1, 368, 4, 1, 5, 1, 1),
    _AudioChannelId_Type()
)
audioChannelId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    audioChannelId.setStatus("current")


class _AudioSignalStatus_Type(Integer32):
    """Custom type audioSignalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noSignal", 2),
          ("signalOk", 1))
    )


_AudioSignalStatus_Type.__name__ = "Integer32"
_AudioSignalStatus_Object = MibTableColumn
audioSignalStatus = _AudioSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 368, 4, 1, 5, 1, 2),
    _AudioSignalStatus_Type()
)
audioSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    audioSignalStatus.setStatus("current")
_CasingTable_Object = MibTable
casingTable = _CasingTable_Object(
    (1, 3, 6, 1, 4, 1, 368, 4, 1, 6)
)
if mibBuilder.loadTexts:
    casingTable.setStatus("current")
_CasingEntry_Object = MibTableRow
casingEntry = _CasingEntry_Object(
    (1, 3, 6, 1, 4, 1, 368, 4, 1, 6, 1)
)
casingEntry.setIndexNames(
    (0, "AXIS-VIDEO-MIB", "casingId"),
)
if mibBuilder.loadTexts:
    casingEntry.setStatus("current")


class _CasingId_Type(Unsigned32):
    """Custom type casingId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_CasingId_Type.__name__ = "Unsigned32"
_CasingId_Object = MibTableColumn
casingId = _CasingId_Object(
    (1, 3, 6, 1, 4, 1, 368, 4, 1, 6, 1, 1),
    _CasingId_Type()
)
casingId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    casingId.setStatus("current")


class _CasingName_Type(SnmpAdminString):
    """Custom type casingName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CasingName_Type.__name__ = "SnmpAdminString"
_CasingName_Object = MibTableColumn
casingName = _CasingName_Object(
    (1, 3, 6, 1, 4, 1, 368, 4, 1, 6, 1, 2),
    _CasingName_Type()
)
casingName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casingName.setStatus("current")


class _CasingStatus_Type(Integer32):
    """Custom type casingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("closed", 1),
          ("open", 2))
    )


_CasingStatus_Type.__name__ = "Integer32"
_CasingStatus_Object = MibTableColumn
casingStatus = _CasingStatus_Object(
    (1, 3, 6, 1, 4, 1, 368, 4, 1, 6, 1, 3),
    _CasingStatus_Type()
)
casingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    casingStatus.setStatus("current")
_StorageTable_Object = MibTable
storageTable = _StorageTable_Object(
    (1, 3, 6, 1, 4, 1, 368, 4, 1, 8)
)
if mibBuilder.loadTexts:
    storageTable.setStatus("current")
_StorageEntry_Object = MibTableRow
storageEntry = _StorageEntry_Object(
    (1, 3, 6, 1, 4, 1, 368, 4, 1, 8, 1)
)
storageEntry.setIndexNames(
    (0, "AXIS-VIDEO-MIB", "storageId"),
)
if mibBuilder.loadTexts:
    storageEntry.setStatus("current")


class _StorageId_Type(Unsigned32):
    """Custom type storageId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_StorageId_Type.__name__ = "Unsigned32"
_StorageId_Object = MibTableColumn
storageId = _StorageId_Object(
    (1, 3, 6, 1, 4, 1, 368, 4, 1, 8, 1, 1),
    _StorageId_Type()
)
storageId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    storageId.setStatus("current")


class _StorageName_Type(SnmpAdminString):
    """Custom type storageName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_StorageName_Type.__name__ = "SnmpAdminString"
_StorageName_Object = MibTableColumn
storageName = _StorageName_Object(
    (1, 3, 6, 1, 4, 1, 368, 4, 1, 8, 1, 2),
    _StorageName_Type()
)
storageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageName.setStatus("current")


class _StorageDisruptionDetected_Type(Integer32):
    """Custom type storageDisruptionDetected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_StorageDisruptionDetected_Type.__name__ = "Integer32"
_StorageDisruptionDetected_Object = MibTableColumn
storageDisruptionDetected = _StorageDisruptionDetected_Object(
    (1, 3, 6, 1, 4, 1, 368, 4, 1, 8, 1, 3),
    _StorageDisruptionDetected_Type()
)
storageDisruptionDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    storageDisruptionDetected.setStatus("current")
_VideoNotifications_ObjectIdentity = ObjectIdentity
videoNotifications = _VideoNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 368, 4, 2)
)
_VideoNotificationPrefix_ObjectIdentity = ObjectIdentity
videoNotificationPrefix = _VideoNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 368, 4, 2, 0)
)
_AlarmID_Type = Unsigned32
_AlarmID_Object = MibScalar
alarmID = _AlarmID_Object(
    (1, 3, 6, 1, 4, 1, 368, 4, 2, 1),
    _AlarmID_Type()
)
alarmID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alarmID.setStatus("current")
_AlarmName_Type = SnmpAdminString
_AlarmName_Object = MibScalar
alarmName = _AlarmName_Object(
    (1, 3, 6, 1, 4, 1, 368, 4, 2, 2),
    _AlarmName_Type()
)
alarmName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alarmName.setStatus("current")
_AlarmText_Type = SnmpAdminString
_AlarmText_Object = MibScalar
alarmText = _AlarmText_Object(
    (1, 3, 6, 1, 4, 1, 368, 4, 2, 3),
    _AlarmText_Type()
)
alarmText.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alarmText.setStatus("current")
_VideoConformance_ObjectIdentity = ObjectIdentity
videoConformance = _VideoConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 368, 4, 3)
)
_VideoGroups_ObjectIdentity = ObjectIdentity
videoGroups = _VideoGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 368, 4, 3, 1)
)
_VideoCompliances_ObjectIdentity = ObjectIdentity
videoCompliances = _VideoCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 368, 4, 3, 2)
)

# Managed Objects groups

videoObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 368, 4, 3, 1, 1)
)
videoObjectGroup.setObjects(
      *(("AXIS-VIDEO-MIB", "powerSupplyStatus"),
        ("AXIS-VIDEO-MIB", "fanStatus"),
        ("AXIS-VIDEO-MIB", "tempSensorStatus"),
        ("AXIS-VIDEO-MIB", "tempSensorValue"),
        ("AXIS-VIDEO-MIB", "videoSignalStatus"),
        ("AXIS-VIDEO-MIB", "audioSignalStatus"),
        ("AXIS-VIDEO-MIB", "casingName"),
        ("AXIS-VIDEO-MIB", "casingStatus"),
        ("AXIS-VIDEO-MIB", "storageDisruptionDetected"),
        ("AXIS-VIDEO-MIB", "storageName"),
        ("AXIS-VIDEO-MIB", "alarmID"),
        ("AXIS-VIDEO-MIB", "alarmName"),
        ("AXIS-VIDEO-MIB", "alarmText"))
)
if mibBuilder.loadTexts:
    videoObjectGroup.setStatus("obsolete")

tempSensorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 368, 4, 3, 1, 3)
)
tempSensorGroup.setObjects(
      *(("AXIS-VIDEO-MIB", "tempSensorStatus"),
        ("AXIS-VIDEO-MIB", "tempSensorValue"))
)
if mibBuilder.loadTexts:
    tempSensorGroup.setStatus("current")

casingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 368, 4, 3, 1, 4)
)
casingGroup.setObjects(
      *(("AXIS-VIDEO-MIB", "casingName"),
        ("AXIS-VIDEO-MIB", "casingStatus"))
)
if mibBuilder.loadTexts:
    casingGroup.setStatus("current")

storageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 368, 4, 3, 1, 5)
)
storageGroup.setObjects(
      *(("AXIS-VIDEO-MIB", "storageDisruptionDetected"),
        ("AXIS-VIDEO-MIB", "storageName"))
)
if mibBuilder.loadTexts:
    storageGroup.setStatus("current")


# Notification objects

alarmNew = NotificationType(
    (1, 3, 6, 1, 4, 1, 368, 4, 2, 0, 1)
)
alarmNew.setObjects(
      *(("AXIS-VIDEO-MIB", "alarmID"),
        ("AXIS-VIDEO-MIB", "alarmName"),
        ("AXIS-VIDEO-MIB", "alarmText"))
)
if mibBuilder.loadTexts:
    alarmNew.setStatus(
        "current"
    )

alarmCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 368, 4, 2, 0, 2)
)
alarmCleared.setObjects(
      *(("AXIS-VIDEO-MIB", "alarmID"),
        ("AXIS-VIDEO-MIB", "alarmName"),
        ("AXIS-VIDEO-MIB", "alarmText"))
)
if mibBuilder.loadTexts:
    alarmCleared.setStatus(
        "current"
    )

alarmSingle = NotificationType(
    (1, 3, 6, 1, 4, 1, 368, 4, 2, 0, 3)
)
alarmSingle.setObjects(
      *(("AXIS-VIDEO-MIB", "alarmID"),
        ("AXIS-VIDEO-MIB", "alarmName"),
        ("AXIS-VIDEO-MIB", "alarmText"))
)
if mibBuilder.loadTexts:
    alarmSingle.setStatus(
        "current"
    )


# Notifications groups

videoNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 368, 4, 3, 1, 2)
)
videoNotificationGroup.setObjects(
      *(("AXIS-VIDEO-MIB", "alarmNew"),
        ("AXIS-VIDEO-MIB", "alarmCleared"),
        ("AXIS-VIDEO-MIB", "alarmSingle"))
)
if mibBuilder.loadTexts:
    videoNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

videoCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 368, 4, 3, 2, 1)
)
if mibBuilder.loadTexts:
    videoCompliance.setStatus(
        "obsolete"
    )

videoComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 368, 4, 3, 2, 2)
)
if mibBuilder.loadTexts:
    videoComplianceRev2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AXIS-VIDEO-MIB",
    **{"videoBased": videoBased,
       "video": video,
       "videoObjects": videoObjects,
       "powerSupplyTable": powerSupplyTable,
       "powerSupplyEntry": powerSupplyEntry,
       "powerSupplyType": powerSupplyType,
       "powerSupplyId": powerSupplyId,
       "powerSupplyStatus": powerSupplyStatus,
       "fanTable": fanTable,
       "fanEntry": fanEntry,
       "fanType": fanType,
       "fanId": fanId,
       "fanStatus": fanStatus,
       "tempSensorTable": tempSensorTable,
       "tempSensorEntry": tempSensorEntry,
       "tempSensorType": tempSensorType,
       "tempSensorId": tempSensorId,
       "tempSensorStatus": tempSensorStatus,
       "tempSensorValue": tempSensorValue,
       "videoChannelTable": videoChannelTable,
       "videoChannelEntry": videoChannelEntry,
       "videoChannelId": videoChannelId,
       "videoSignalStatus": videoSignalStatus,
       "audioChannelTable": audioChannelTable,
       "audioChannelEntry": audioChannelEntry,
       "audioChannelId": audioChannelId,
       "audioSignalStatus": audioSignalStatus,
       "casingTable": casingTable,
       "casingEntry": casingEntry,
       "casingId": casingId,
       "casingName": casingName,
       "casingStatus": casingStatus,
       "storageTable": storageTable,
       "storageEntry": storageEntry,
       "storageId": storageId,
       "storageName": storageName,
       "storageDisruptionDetected": storageDisruptionDetected,
       "videoNotifications": videoNotifications,
       "videoNotificationPrefix": videoNotificationPrefix,
       "alarmNew": alarmNew,
       "alarmCleared": alarmCleared,
       "alarmSingle": alarmSingle,
       "alarmID": alarmID,
       "alarmName": alarmName,
       "alarmText": alarmText,
       "videoConformance": videoConformance,
       "videoGroups": videoGroups,
       "videoObjectGroup": videoObjectGroup,
       "videoNotificationGroup": videoNotificationGroup,
       "tempSensorGroup": tempSensorGroup,
       "casingGroup": casingGroup,
       "storageGroup": storageGroup,
       "videoCompliances": videoCompliances,
       "videoCompliance": videoCompliance,
       "videoComplianceRev2": videoComplianceRev2}
)
