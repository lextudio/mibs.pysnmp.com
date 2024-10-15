# SNMP MIB module (EMSNetrake-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EMSNetrake-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:38:29 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

netrake = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10950)
)
netrake.setRevisions(
        ("2001-09-20 10:05",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Org_ObjectIdentity = ObjectIdentity
org = _Org_ObjectIdentity(
    (1, 3)
)
_Dod_ObjectIdentity = ObjectIdentity
dod = _Dod_ObjectIdentity(
    (1, 3, 6)
)
_Internet_ObjectIdentity = ObjectIdentity
internet = _Internet_ObjectIdentity(
    (1, 3, 6, 1)
)
_Private_ObjectIdentity = ObjectIdentity
private = _Private_ObjectIdentity(
    (1, 3, 6, 1, 4)
)
_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10950, 1)
)
_Ems_ObjectIdentity = ObjectIdentity
ems = _Ems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10950, 1, 2)
)
_ManagedDevices_ObjectIdentity = ObjectIdentity
managedDevices = _ManagedDevices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10950, 1, 2, 1)
)
_ManagedDevicesTable_Object = MibTable
managedDevicesTable = _ManagedDevicesTable_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    managedDevicesTable.setStatus("current")
_ManagedDevicesEntry_Object = MibTableRow
managedDevicesEntry = _ManagedDevicesEntry_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 2, 1, 1, 1)
)
managedDevicesEntry.setIndexNames(
    (0, "EMSNetrake-MIB", "deviceName"),
)
if mibBuilder.loadTexts:
    managedDevicesEntry.setStatus("current")
_DeviceName_Type = DisplayString
_DeviceName_Object = MibTableColumn
deviceName = _DeviceName_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 2, 1, 1, 1, 1),
    _DeviceName_Type()
)
deviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceName.setStatus("current")
_DeviceSerialNumber_Type = DisplayString
_DeviceSerialNumber_Object = MibTableColumn
deviceSerialNumber = _DeviceSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 2, 1, 1, 1, 2),
    _DeviceSerialNumber_Type()
)
deviceSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceSerialNumber.setStatus("current")
_DeviceModel_Type = DisplayString
_DeviceModel_Object = MibTableColumn
deviceModel = _DeviceModel_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 2, 1, 1, 1, 3),
    _DeviceModel_Type()
)
deviceModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceModel.setStatus("current")
_DeviceMgmtIpAddress_Type = IpAddress
_DeviceMgmtIpAddress_Object = MibTableColumn
deviceMgmtIpAddress = _DeviceMgmtIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 2, 1, 1, 1, 4),
    _DeviceMgmtIpAddress_Type()
)
deviceMgmtIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceMgmtIpAddress.setStatus("current")


class _DeviceAlarmStatus_Type(Integer32):
    """Custom type deviceAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("clear", 5),
          ("critical", 1),
          ("info", 6),
          ("major", 2),
          ("minor", 3),
          ("unknown", 0),
          ("warning", 4))
    )


_DeviceAlarmStatus_Type.__name__ = "Integer32"
_DeviceAlarmStatus_Object = MibTableColumn
deviceAlarmStatus = _DeviceAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 2, 1, 1, 1, 5),
    _DeviceAlarmStatus_Type()
)
deviceAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceAlarmStatus.setStatus("current")
_DeviceOperState_Type = DisplayString
_DeviceOperState_Object = MibTableColumn
deviceOperState = _DeviceOperState_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 2, 1, 1, 1, 6),
    _DeviceOperState_Type()
)
deviceOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceOperState.setStatus("current")
_DeviceRowStatus_Type = RowStatus
_DeviceRowStatus_Object = MibTableColumn
deviceRowStatus = _DeviceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 2, 1, 1, 1, 7),
    _DeviceRowStatus_Type()
)
deviceRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceRowStatus.setStatus("current")
_DeviceDisplayName_Type = DisplayString
_DeviceDisplayName_Object = MibTableColumn
deviceDisplayName = _DeviceDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 2, 1, 1, 1, 8),
    _DeviceDisplayName_Type()
)
deviceDisplayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceDisplayName.setStatus("current")
_ActiveAlarm_ObjectIdentity = ObjectIdentity
activeAlarm = _ActiveAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10950, 1, 2, 2)
)
_EmsActiveAlarmTable_Object = MibTable
emsActiveAlarmTable = _EmsActiveAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    emsActiveAlarmTable.setStatus("current")
_EmsActiveAlarmEntry_Object = MibTableRow
emsActiveAlarmEntry = _EmsActiveAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 2, 2, 1, 1)
)
emsActiveAlarmEntry.setIndexNames(
    (0, "EMSNetrake-MIB", "emsActiveAlarmId"),
    (0, "EMSNetrake-MIB", "emsActiveAlarmDeviceName"),
)
if mibBuilder.loadTexts:
    emsActiveAlarmEntry.setStatus("current")


class _EmsActiveAlarmId_Type(Integer32):
    """Custom type emsActiveAlarmId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EmsActiveAlarmId_Type.__name__ = "Integer32"
_EmsActiveAlarmId_Object = MibTableColumn
emsActiveAlarmId = _EmsActiveAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 2, 2, 1, 1, 1),
    _EmsActiveAlarmId_Type()
)
emsActiveAlarmId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emsActiveAlarmId.setStatus("current")


class _EmsActiveAlarmDeviceName_Type(DisplayString):
    """Custom type emsActiveAlarmDeviceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EmsActiveAlarmDeviceName_Type.__name__ = "DisplayString"
_EmsActiveAlarmDeviceName_Object = MibTableColumn
emsActiveAlarmDeviceName = _EmsActiveAlarmDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 2, 2, 1, 1, 2),
    _EmsActiveAlarmDeviceName_Type()
)
emsActiveAlarmDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emsActiveAlarmDeviceName.setStatus("current")
_EmsActiveAlarmDateTime_Type = DateAndTime
_EmsActiveAlarmDateTime_Object = MibTableColumn
emsActiveAlarmDateTime = _EmsActiveAlarmDateTime_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 2, 2, 1, 1, 3),
    _EmsActiveAlarmDateTime_Type()
)
emsActiveAlarmDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emsActiveAlarmDateTime.setStatus("current")


class _EmsActiveAlarmSeverity_Type(Integer32):
    """Custom type emsActiveAlarmSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("clear", 5),
          ("critical", 1),
          ("info", 6),
          ("major", 2),
          ("minor", 3),
          ("unknown", 0),
          ("warning", 4))
    )


_EmsActiveAlarmSeverity_Type.__name__ = "Integer32"
_EmsActiveAlarmSeverity_Object = MibTableColumn
emsActiveAlarmSeverity = _EmsActiveAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 2, 2, 1, 1, 4),
    _EmsActiveAlarmSeverity_Type()
)
emsActiveAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emsActiveAlarmSeverity.setStatus("current")


class _EmsActiveAlarmDescription_Type(DisplayString):
    """Custom type emsActiveAlarmDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EmsActiveAlarmDescription_Type.__name__ = "DisplayString"
_EmsActiveAlarmDescription_Object = MibTableColumn
emsActiveAlarmDescription = _EmsActiveAlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 2, 2, 1, 1, 5),
    _EmsActiveAlarmDescription_Type()
)
emsActiveAlarmDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emsActiveAlarmDescription.setStatus("current")


class _EmsActiveAlarmNumOccurances_Type(Integer32):
    """Custom type emsActiveAlarmNumOccurances based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EmsActiveAlarmNumOccurances_Type.__name__ = "Integer32"
_EmsActiveAlarmNumOccurances_Object = MibTableColumn
emsActiveAlarmNumOccurances = _EmsActiveAlarmNumOccurances_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 2, 2, 1, 1, 6),
    _EmsActiveAlarmNumOccurances_Type()
)
emsActiveAlarmNumOccurances.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emsActiveAlarmNumOccurances.setStatus("current")


class _EmsActiveAlarmServiceAffecting_Type(Integer32):
    """Custom type emsActiveAlarmServiceAffecting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notServiceAffecting", 2),
          ("serviceAffecting", 1))
    )


_EmsActiveAlarmServiceAffecting_Type.__name__ = "Integer32"
_EmsActiveAlarmServiceAffecting_Object = MibTableColumn
emsActiveAlarmServiceAffecting = _EmsActiveAlarmServiceAffecting_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 2, 2, 1, 1, 7),
    _EmsActiveAlarmServiceAffecting_Type()
)
emsActiveAlarmServiceAffecting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emsActiveAlarmServiceAffecting.setStatus("current")


class _EmsActiveAlarmRowStatus_Type(RowStatus):
    """Custom type emsActiveAlarmRowStatus based on RowStatus"""
    subtypeSpec = RowStatus.subtypeSpec
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
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6),
          ("notInService", 2),
          ("notReady", 3))
    )


_EmsActiveAlarmRowStatus_Type.__name__ = "RowStatus"
_EmsActiveAlarmRowStatus_Object = MibTableColumn
emsActiveAlarmRowStatus = _EmsActiveAlarmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 2, 2, 1, 1, 8),
    _EmsActiveAlarmRowStatus_Type()
)
emsActiveAlarmRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emsActiveAlarmRowStatus.setStatus("current")


class _EmsActiveAlarmTypeID_Type(Integer32):
    """Custom type emsActiveAlarmTypeID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50000),
    )


_EmsActiveAlarmTypeID_Type.__name__ = "Integer32"
_EmsActiveAlarmTypeID_Object = MibTableColumn
emsActiveAlarmTypeID = _EmsActiveAlarmTypeID_Object(
    (1, 3, 6, 1, 4, 1, 10950, 1, 2, 2, 1, 1, 9),
    _EmsActiveAlarmTypeID_Type()
)
emsActiveAlarmTypeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emsActiveAlarmTypeID.setStatus("current")

# Managed Objects groups


# Notification objects

deviceChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10950, 1, 2, 1, 2)
)
deviceChangeTrap.setObjects(
      *(("EMSNetrake-MIB", "deviceAlarmStatus"),
        ("EMSNetrake-MIB", "deviceDisplayName"),
        ("EMSNetrake-MIB", "deviceMgmtIpAddress"),
        ("EMSNetrake-MIB", "deviceModel"),
        ("EMSNetrake-MIB", "deviceName"),
        ("EMSNetrake-MIB", "deviceOperState"),
        ("EMSNetrake-MIB", "deviceRowStatus"),
        ("EMSNetrake-MIB", "deviceSerialNumber"))
)
if mibBuilder.loadTexts:
    deviceChangeTrap.setStatus(
        "current"
    )

emsActiveAlarmChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 10950, 1, 2, 2, 2)
)
emsActiveAlarmChangeTrap.setObjects(
      *(("EMSNetrake-MIB", "emsActiveAlarmDateTime"),
        ("EMSNetrake-MIB", "emsActiveAlarmDescription"),
        ("EMSNetrake-MIB", "emsActiveAlarmDeviceName"),
        ("EMSNetrake-MIB", "emsActiveAlarmId"),
        ("EMSNetrake-MIB", "emsActiveAlarmNumOccurances"),
        ("EMSNetrake-MIB", "emsActiveAlarmRowStatus"),
        ("EMSNetrake-MIB", "emsActiveAlarmServiceAffecting"),
        ("EMSNetrake-MIB", "emsActiveAlarmSeverity"),
        ("EMSNetrake-MIB", "emsActiveAlarmTypeID"))
)
if mibBuilder.loadTexts:
    emsActiveAlarmChangeTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EMSNetrake-MIB",
    **{"org": org,
       "dod": dod,
       "internet": internet,
       "private": private,
       "enterprises": enterprises,
       "netrake": netrake,
       "products": products,
       "ems": ems,
       "managedDevices": managedDevices,
       "managedDevicesTable": managedDevicesTable,
       "managedDevicesEntry": managedDevicesEntry,
       "deviceName": deviceName,
       "deviceSerialNumber": deviceSerialNumber,
       "deviceModel": deviceModel,
       "deviceMgmtIpAddress": deviceMgmtIpAddress,
       "deviceAlarmStatus": deviceAlarmStatus,
       "deviceOperState": deviceOperState,
       "deviceRowStatus": deviceRowStatus,
       "deviceDisplayName": deviceDisplayName,
       "deviceChangeTrap": deviceChangeTrap,
       "activeAlarm": activeAlarm,
       "emsActiveAlarmTable": emsActiveAlarmTable,
       "emsActiveAlarmEntry": emsActiveAlarmEntry,
       "emsActiveAlarmId": emsActiveAlarmId,
       "emsActiveAlarmDeviceName": emsActiveAlarmDeviceName,
       "emsActiveAlarmDateTime": emsActiveAlarmDateTime,
       "emsActiveAlarmSeverity": emsActiveAlarmSeverity,
       "emsActiveAlarmDescription": emsActiveAlarmDescription,
       "emsActiveAlarmNumOccurances": emsActiveAlarmNumOccurances,
       "emsActiveAlarmServiceAffecting": emsActiveAlarmServiceAffecting,
       "emsActiveAlarmRowStatus": emsActiveAlarmRowStatus,
       "emsActiveAlarmTypeID": emsActiveAlarmTypeID,
       "emsActiveAlarmChangeTrap": emsActiveAlarmChangeTrap}
)
