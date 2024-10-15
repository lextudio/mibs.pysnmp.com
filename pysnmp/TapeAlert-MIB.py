# SNMP MIB module (TapeAlert-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TapeAlert-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:08:06 2024
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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
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

_Hp_ObjectIdentity = ObjectIdentity
hp = _Hp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11)
)
_Nm_ObjectIdentity = ObjectIdentity
nm = _Nm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2)
)
_System_ObjectIdentity = ObjectIdentity
system = _System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3)
)
_NetPeripheral_ObjectIdentity = ObjectIdentity
netPeripheral = _NetPeripheral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9)
)
_NetTape_ObjectIdentity = ObjectIdentity
netTape = _NetTape_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7)
)
_TapeAlert_ObjectIdentity = ObjectIdentity
tapeAlert = _TapeAlert_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1)
)
_Control_ObjectIdentity = ObjectIdentity
control = _Control_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 1)
)


class _RevMajor_Type(Integer32):
    """Custom type revMajor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RevMajor_Type.__name__ = "Integer32"
_RevMajor_Object = MibScalar
revMajor = _RevMajor_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 1, 1),
    _RevMajor_Type()
)
revMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    revMajor.setStatus("mandatory")


class _RevMinor_Type(Integer32):
    """Custom type revMinor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RevMinor_Type.__name__ = "Integer32"
_RevMinor_Object = MibScalar
revMinor = _RevMinor_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 1, 2),
    _RevMinor_Type()
)
revMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    revMinor.setStatus("mandatory")


class _TrapEnable_Type(Integer32):
    """Custom type trapEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_TrapEnable_Type.__name__ = "Integer32"
_TrapEnable_Object = MibScalar
trapEnable = _TrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 1, 3),
    _TrapEnable_Type()
)
trapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapEnable.setStatus("optional")


class _AutoCleanEnable_Type(Integer32):
    """Custom type autoCleanEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AutoCleanEnable_Type.__name__ = "Integer32"
_AutoCleanEnable_Object = MibScalar
autoCleanEnable = _AutoCleanEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 1, 4),
    _AutoCleanEnable_Type()
)
autoCleanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoCleanEnable.setStatus("optional")


class _AutoCopyEnable_Type(Integer32):
    """Custom type autoCopyEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AutoCopyEnable_Type.__name__ = "Integer32"
_AutoCopyEnable_Object = MibScalar
autoCopyEnable = _AutoCopyEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 1, 5),
    _AutoCopyEnable_Type()
)
autoCopyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoCopyEnable.setStatus("optional")


class _NumDevices_Type(Integer32):
    """Custom type numDevices based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NumDevices_Type.__name__ = "Integer32"
_NumDevices_Object = MibScalar
numDevices = _NumDevices_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 2),
    _NumDevices_Type()
)
numDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numDevices.setStatus("mandatory")
_DevTable_Object = MibTable
devTable = _DevTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 3)
)
if mibBuilder.loadTexts:
    devTable.setStatus("mandatory")
_DevInfo_Object = MibTableRow
devInfo = _DevInfo_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 3, 1)
)
devInfo.setIndexNames(
    (0, "TapeAlert-MIB", "devNum"),
)
if mibBuilder.loadTexts:
    devInfo.setStatus("mandatory")


class _DevNum_Type(Integer32):
    """Custom type devNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DevNum_Type.__name__ = "Integer32"
_DevNum_Object = MibTableColumn
devNum = _DevNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 3, 1, 1),
    _DevNum_Type()
)
devNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devNum.setStatus("mandatory")


class _TapeAlertCapability_Type(Integer32):
    """Custom type tapeAlertCapability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_TapeAlertCapability_Type.__name__ = "Integer32"
_TapeAlertCapability_Object = MibTableColumn
tapeAlertCapability = _TapeAlertCapability_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 3, 1, 2),
    _TapeAlertCapability_Type()
)
tapeAlertCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tapeAlertCapability.setStatus("mandatory")


class _HbaName_Type(DisplayString):
    """Custom type hbaName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HbaName_Type.__name__ = "DisplayString"
_HbaName_Object = MibTableColumn
hbaName = _HbaName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 3, 1, 3),
    _HbaName_Type()
)
hbaName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hbaName.setStatus("mandatory")


class _HbaNumber_Type(Integer32):
    """Custom type hbaNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HbaNumber_Type.__name__ = "Integer32"
_HbaNumber_Object = MibTableColumn
hbaNumber = _HbaNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 3, 1, 4),
    _HbaNumber_Type()
)
hbaNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hbaNumber.setStatus("mandatory")


class _HbaChannel_Type(Integer32):
    """Custom type hbaChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HbaChannel_Type.__name__ = "Integer32"
_HbaChannel_Object = MibTableColumn
hbaChannel = _HbaChannel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 3, 1, 5),
    _HbaChannel_Type()
)
hbaChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hbaChannel.setStatus("mandatory")


class _DriveScsiID_Type(Integer32):
    """Custom type driveScsiID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DriveScsiID_Type.__name__ = "Integer32"
_DriveScsiID_Object = MibTableColumn
driveScsiID = _DriveScsiID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 3, 1, 6),
    _DriveScsiID_Type()
)
driveScsiID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driveScsiID.setStatus("mandatory")


class _DriveInquiry_Type(DisplayString):
    """Custom type driveInquiry based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DriveInquiry_Type.__name__ = "DisplayString"
_DriveInquiry_Object = MibTableColumn
driveInquiry = _DriveInquiry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 3, 1, 7),
    _DriveInquiry_Type()
)
driveInquiry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driveInquiry.setStatus("mandatory")


class _DriveFirmware_Type(DisplayString):
    """Custom type driveFirmware based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DriveFirmware_Type.__name__ = "DisplayString"
_DriveFirmware_Object = MibTableColumn
driveFirmware = _DriveFirmware_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 3, 1, 8),
    _DriveFirmware_Type()
)
driveFirmware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driveFirmware.setStatus("mandatory")


class _DriveType_Type(DisplayString):
    """Custom type driveType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DriveType_Type.__name__ = "DisplayString"
_DriveType_Object = MibTableColumn
driveType = _DriveType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 3, 1, 9),
    _DriveType_Type()
)
driveType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driveType.setStatus("mandatory")


class _DriveCompress_Type(Integer32):
    """Custom type driveCompress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_DriveCompress_Type.__name__ = "Integer32"
_DriveCompress_Object = MibTableColumn
driveCompress = _DriveCompress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 3, 1, 10),
    _DriveCompress_Type()
)
driveCompress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driveCompress.setStatus("mandatory")


class _CurrentMedia_Type(DisplayString):
    """Custom type currentMedia based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CurrentMedia_Type.__name__ = "DisplayString"
_CurrentMedia_Object = MibTableColumn
currentMedia = _CurrentMedia_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 3, 1, 11),
    _CurrentMedia_Type()
)
currentMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentMedia.setStatus("mandatory")


class _DriveSerialNum_Type(DisplayString):
    """Custom type driveSerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DriveSerialNum_Type.__name__ = "DisplayString"
_DriveSerialNum_Object = MibTableColumn
driveSerialNum = _DriveSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 3, 1, 12),
    _DriveSerialNum_Type()
)
driveSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    driveSerialNum.setStatus("optional")


class _NumErrors_Type(Integer32):
    """Custom type numErrors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NumErrors_Type.__name__ = "Integer32"
_NumErrors_Object = MibScalar
numErrors = _NumErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 4),
    _NumErrors_Type()
)
numErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numErrors.setStatus("mandatory")
_ErrorHistoryTable_Object = MibTable
errorHistoryTable = _ErrorHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 5)
)
if mibBuilder.loadTexts:
    errorHistoryTable.setStatus("mandatory")
_ErrorHistoryEntry_Object = MibTableRow
errorHistoryEntry = _ErrorHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 5, 1)
)
errorHistoryEntry.setIndexNames(
    (0, "TapeAlert-MIB", "errorIndex"),
)
if mibBuilder.loadTexts:
    errorHistoryEntry.setStatus("mandatory")


class _ErrorIndex_Type(Integer32):
    """Custom type errorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ErrorIndex_Type.__name__ = "Integer32"
_ErrorIndex_Object = MibTableColumn
errorIndex = _ErrorIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 5, 1, 1),
    _ErrorIndex_Type()
)
errorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorIndex.setStatus("mandatory")


class _ErrorHbaNumber_Type(Integer32):
    """Custom type errorHbaNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ErrorHbaNumber_Type.__name__ = "Integer32"
_ErrorHbaNumber_Object = MibTableColumn
errorHbaNumber = _ErrorHbaNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 5, 1, 2),
    _ErrorHbaNumber_Type()
)
errorHbaNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorHbaNumber.setStatus("mandatory")


class _ErrorHbaChannel_Type(Integer32):
    """Custom type errorHbaChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ErrorHbaChannel_Type.__name__ = "Integer32"
_ErrorHbaChannel_Object = MibTableColumn
errorHbaChannel = _ErrorHbaChannel_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 5, 1, 3),
    _ErrorHbaChannel_Type()
)
errorHbaChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorHbaChannel.setStatus("mandatory")


class _ErrorDriveScsiID_Type(Integer32):
    """Custom type errorDriveScsiID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ErrorDriveScsiID_Type.__name__ = "Integer32"
_ErrorDriveScsiID_Object = MibTableColumn
errorDriveScsiID = _ErrorDriveScsiID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 5, 1, 4),
    _ErrorDriveScsiID_Type()
)
errorDriveScsiID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorDriveScsiID.setStatus("mandatory")


class _ErrorDate_Type(OctetString):
    """Custom type errorDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(14, 14),
    )


_ErrorDate_Type.__name__ = "OctetString"
_ErrorDate_Object = MibTableColumn
errorDate = _ErrorDate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 5, 1, 5),
    _ErrorDate_Type()
)
errorDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorDate.setStatus("mandatory")


class _ErrorTrapNum_Type(Integer32):
    """Custom type errorTrapNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_ErrorTrapNum_Type.__name__ = "Integer32"
_ErrorTrapNum_Object = MibTableColumn
errorTrapNum = _ErrorTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 5, 1, 6),
    _ErrorTrapNum_Type()
)
errorTrapNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorTrapNum.setStatus("mandatory")


class _ErrorMedia_Type(DisplayString):
    """Custom type errorMedia based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ErrorMedia_Type.__name__ = "DisplayString"
_ErrorMedia_Object = MibTableColumn
errorMedia = _ErrorMedia_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 5, 1, 7),
    _ErrorMedia_Type()
)
errorMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorMedia.setStatus("mandatory")

# Managed Objects groups


# Notification objects

tapeAlertTrap1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 0, 1)
)
tapeAlertTrap1.setObjects(
      *(("TapeAlert-MIB", "hbaNumber"),
        ("TapeAlert-MIB", "hbaChannel"),
        ("TapeAlert-MIB", "driveScsiID"))
)
if mibBuilder.loadTexts:
    tapeAlertTrap1.setStatus(
        ""
    )

tapeAlertTrap2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 0, 2)
)
tapeAlertTrap2.setObjects(
      *(("TapeAlert-MIB", "hbaNumber"),
        ("TapeAlert-MIB", "hbaChannel"),
        ("TapeAlert-MIB", "driveScsiID"))
)
if mibBuilder.loadTexts:
    tapeAlertTrap2.setStatus(
        ""
    )

tapeAlertTrap3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 0, 3)
)
tapeAlertTrap3.setObjects(
      *(("TapeAlert-MIB", "hbaNumber"),
        ("TapeAlert-MIB", "hbaChannel"),
        ("TapeAlert-MIB", "driveScsiID"))
)
if mibBuilder.loadTexts:
    tapeAlertTrap3.setStatus(
        ""
    )

tapeAlertTrap4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 0, 4)
)
tapeAlertTrap4.setObjects(
      *(("TapeAlert-MIB", "hbaNumber"),
        ("TapeAlert-MIB", "hbaChannel"),
        ("TapeAlert-MIB", "driveScsiID"),
        ("TapeAlert-MIB", "currentMedia"))
)
if mibBuilder.loadTexts:
    tapeAlertTrap4.setStatus(
        ""
    )

tapeAlertTrap5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 0, 5)
)
tapeAlertTrap5.setObjects(
      *(("TapeAlert-MIB", "hbaNumber"),
        ("TapeAlert-MIB", "hbaChannel"),
        ("TapeAlert-MIB", "driveScsiID"))
)
if mibBuilder.loadTexts:
    tapeAlertTrap5.setStatus(
        ""
    )

tapeAlertTrap6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 0, 6)
)
tapeAlertTrap6.setObjects(
      *(("TapeAlert-MIB", "hbaNumber"),
        ("TapeAlert-MIB", "hbaChannel"),
        ("TapeAlert-MIB", "driveScsiID"))
)
if mibBuilder.loadTexts:
    tapeAlertTrap6.setStatus(
        ""
    )

tapeAlertTrap7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 0, 7)
)
tapeAlertTrap7.setObjects(
      *(("TapeAlert-MIB", "hbaNumber"),
        ("TapeAlert-MIB", "hbaChannel"),
        ("TapeAlert-MIB", "driveScsiID"),
        ("TapeAlert-MIB", "currentMedia"))
)
if mibBuilder.loadTexts:
    tapeAlertTrap7.setStatus(
        ""
    )

tapeAlertTrap8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 0, 8)
)
tapeAlertTrap8.setObjects(
      *(("TapeAlert-MIB", "hbaNumber"),
        ("TapeAlert-MIB", "hbaChannel"),
        ("TapeAlert-MIB", "driveScsiID"))
)
if mibBuilder.loadTexts:
    tapeAlertTrap8.setStatus(
        ""
    )

tapeAlertTrap9 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 0, 9)
)
tapeAlertTrap9.setObjects(
      *(("TapeAlert-MIB", "hbaNumber"),
        ("TapeAlert-MIB", "hbaChannel"),
        ("TapeAlert-MIB", "driveScsiID"))
)
if mibBuilder.loadTexts:
    tapeAlertTrap9.setStatus(
        ""
    )

tapeAlertTrap10 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 0, 10)
)
tapeAlertTrap10.setObjects(
      *(("TapeAlert-MIB", "hbaNumber"),
        ("TapeAlert-MIB", "hbaChannel"),
        ("TapeAlert-MIB", "driveScsiID"))
)
if mibBuilder.loadTexts:
    tapeAlertTrap10.setStatus(
        ""
    )

tapeAlertTrap11 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 0, 11)
)
tapeAlertTrap11.setObjects(
      *(("TapeAlert-MIB", "hbaNumber"),
        ("TapeAlert-MIB", "hbaChannel"),
        ("TapeAlert-MIB", "driveScsiID"))
)
if mibBuilder.loadTexts:
    tapeAlertTrap11.setStatus(
        ""
    )

tapeAlertTrap12 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 0, 12)
)
tapeAlertTrap12.setObjects(
      *(("TapeAlert-MIB", "hbaNumber"),
        ("TapeAlert-MIB", "hbaChannel"),
        ("TapeAlert-MIB", "driveScsiID"))
)
if mibBuilder.loadTexts:
    tapeAlertTrap12.setStatus(
        ""
    )

tapeAlertTrap13 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 0, 13)
)
tapeAlertTrap13.setObjects(
      *(("TapeAlert-MIB", "hbaNumber"),
        ("TapeAlert-MIB", "hbaChannel"),
        ("TapeAlert-MIB", "driveScsiID"))
)
if mibBuilder.loadTexts:
    tapeAlertTrap13.setStatus(
        ""
    )

tapeAlertTrap14 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 0, 14)
)
tapeAlertTrap14.setObjects(
      *(("TapeAlert-MIB", "hbaNumber"),
        ("TapeAlert-MIB", "hbaChannel"),
        ("TapeAlert-MIB", "driveScsiID"))
)
if mibBuilder.loadTexts:
    tapeAlertTrap14.setStatus(
        ""
    )

tapeAlertTrap15 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 0, 15)
)
tapeAlertTrap15.setObjects(
      *(("TapeAlert-MIB", "hbaNumber"),
        ("TapeAlert-MIB", "hbaChannel"),
        ("TapeAlert-MIB", "driveScsiID"),
        ("TapeAlert-MIB", "currentMedia"))
)
if mibBuilder.loadTexts:
    tapeAlertTrap15.setStatus(
        ""
    )

tapeAlertTrap16 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 0, 16)
)
tapeAlertTrap16.setObjects(
      *(("TapeAlert-MIB", "hbaNumber"),
        ("TapeAlert-MIB", "hbaChannel"),
        ("TapeAlert-MIB", "driveScsiID"))
)
if mibBuilder.loadTexts:
    tapeAlertTrap16.setStatus(
        ""
    )

tapeAlertTrap17 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 0, 17)
)
tapeAlertTrap17.setObjects(
      *(("TapeAlert-MIB", "hbaNumber"),
        ("TapeAlert-MIB", "hbaChannel"),
        ("TapeAlert-MIB", "driveScsiID"))
)
if mibBuilder.loadTexts:
    tapeAlertTrap17.setStatus(
        ""
    )

tapeAlertTrap18 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 0, 18)
)
tapeAlertTrap18.setObjects(
      *(("TapeAlert-MIB", "hbaNumber"),
        ("TapeAlert-MIB", "hbaChannel"),
        ("TapeAlert-MIB", "driveScsiID"))
)
if mibBuilder.loadTexts:
    tapeAlertTrap18.setStatus(
        ""
    )

tapeAlertTrap19 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 0, 19)
)
tapeAlertTrap19.setObjects(
      *(("TapeAlert-MIB", "hbaNumber"),
        ("TapeAlert-MIB", "hbaChannel"),
        ("TapeAlert-MIB", "driveScsiID"),
        ("TapeAlert-MIB", "currentMedia"))
)
if mibBuilder.loadTexts:
    tapeAlertTrap19.setStatus(
        ""
    )

tapeAlertTrap20 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 0, 20)
)
tapeAlertTrap20.setObjects(
      *(("TapeAlert-MIB", "hbaNumber"),
        ("TapeAlert-MIB", "hbaChannel"),
        ("TapeAlert-MIB", "driveScsiID"))
)
if mibBuilder.loadTexts:
    tapeAlertTrap20.setStatus(
        ""
    )

tapeAlertTrap21 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 0, 21)
)
tapeAlertTrap21.setObjects(
      *(("TapeAlert-MIB", "hbaNumber"),
        ("TapeAlert-MIB", "hbaChannel"),
        ("TapeAlert-MIB", "driveScsiID"))
)
if mibBuilder.loadTexts:
    tapeAlertTrap21.setStatus(
        ""
    )

tapeAlertTrap22 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 0, 22)
)
tapeAlertTrap22.setObjects(
      *(("TapeAlert-MIB", "hbaNumber"),
        ("TapeAlert-MIB", "hbaChannel"),
        ("TapeAlert-MIB", "driveScsiID"))
)
if mibBuilder.loadTexts:
    tapeAlertTrap22.setStatus(
        ""
    )

tapeAlertTrap23 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 0, 23)
)
tapeAlertTrap23.setObjects(
      *(("TapeAlert-MIB", "hbaNumber"),
        ("TapeAlert-MIB", "hbaChannel"),
        ("TapeAlert-MIB", "driveScsiID"))
)
if mibBuilder.loadTexts:
    tapeAlertTrap23.setStatus(
        ""
    )

tapeAlertTrap29 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 0, 29)
)
tapeAlertTrap29.setObjects(
      *(("TapeAlert-MIB", "hbaNumber"),
        ("TapeAlert-MIB", "hbaChannel"),
        ("TapeAlert-MIB", "driveScsiID"))
)
if mibBuilder.loadTexts:
    tapeAlertTrap29.setStatus(
        ""
    )

tapeAlertTrap30 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 0, 30)
)
tapeAlertTrap30.setObjects(
      *(("TapeAlert-MIB", "hbaNumber"),
        ("TapeAlert-MIB", "hbaChannel"),
        ("TapeAlert-MIB", "driveScsiID"))
)
if mibBuilder.loadTexts:
    tapeAlertTrap30.setStatus(
        ""
    )

tapeAlertTrap31 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 0, 31)
)
tapeAlertTrap31.setObjects(
      *(("TapeAlert-MIB", "hbaNumber"),
        ("TapeAlert-MIB", "hbaChannel"),
        ("TapeAlert-MIB", "driveScsiID"))
)
if mibBuilder.loadTexts:
    tapeAlertTrap31.setStatus(
        ""
    )

tapeAlertTrap32 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 0, 32)
)
tapeAlertTrap32.setObjects(
      *(("TapeAlert-MIB", "hbaNumber"),
        ("TapeAlert-MIB", "hbaChannel"),
        ("TapeAlert-MIB", "driveScsiID"))
)
if mibBuilder.loadTexts:
    tapeAlertTrap32.setStatus(
        ""
    )

tapeAlertTrap33 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 0, 33)
)
tapeAlertTrap33.setObjects(
      *(("TapeAlert-MIB", "hbaNumber"),
        ("TapeAlert-MIB", "hbaChannel"),
        ("TapeAlert-MIB", "driveScsiID"))
)
if mibBuilder.loadTexts:
    tapeAlertTrap33.setStatus(
        ""
    )

tapeAlertTrap34 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 0, 34)
)
tapeAlertTrap34.setObjects(
      *(("TapeAlert-MIB", "hbaNumber"),
        ("TapeAlert-MIB", "hbaChannel"),
        ("TapeAlert-MIB", "driveScsiID"))
)
if mibBuilder.loadTexts:
    tapeAlertTrap34.setStatus(
        ""
    )

tapeAlertTrap35 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 0, 35)
)
tapeAlertTrap35.setObjects(
      *(("TapeAlert-MIB", "hbaNumber"),
        ("TapeAlert-MIB", "hbaChannel"),
        ("TapeAlert-MIB", "driveScsiID"))
)
if mibBuilder.loadTexts:
    tapeAlertTrap35.setStatus(
        ""
    )

tapeAlertTrap36 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 0, 36)
)
tapeAlertTrap36.setObjects(
      *(("TapeAlert-MIB", "hbaNumber"),
        ("TapeAlert-MIB", "hbaChannel"),
        ("TapeAlert-MIB", "driveScsiID"))
)
if mibBuilder.loadTexts:
    tapeAlertTrap36.setStatus(
        ""
    )

tapeAlertTrap37 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 0, 37)
)
tapeAlertTrap37.setObjects(
      *(("TapeAlert-MIB", "hbaNumber"),
        ("TapeAlert-MIB", "hbaChannel"),
        ("TapeAlert-MIB", "driveScsiID"))
)
if mibBuilder.loadTexts:
    tapeAlertTrap37.setStatus(
        ""
    )

tapeAlertTrap38 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 0, 38)
)
tapeAlertTrap38.setObjects(
      *(("TapeAlert-MIB", "hbaNumber"),
        ("TapeAlert-MIB", "hbaChannel"),
        ("TapeAlert-MIB", "driveScsiID"))
)
if mibBuilder.loadTexts:
    tapeAlertTrap38.setStatus(
        ""
    )

tapeAlertTrap39 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 0, 39)
)
tapeAlertTrap39.setObjects(
      *(("TapeAlert-MIB", "hbaNumber"),
        ("TapeAlert-MIB", "hbaChannel"),
        ("TapeAlert-MIB", "driveScsiID"))
)
if mibBuilder.loadTexts:
    tapeAlertTrap39.setStatus(
        ""
    )

tapeAlertTrap40 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 0, 40)
)
tapeAlertTrap40.setObjects(
      *(("TapeAlert-MIB", "hbaNumber"),
        ("TapeAlert-MIB", "hbaChannel"),
        ("TapeAlert-MIB", "driveScsiID"))
)
if mibBuilder.loadTexts:
    tapeAlertTrap40.setStatus(
        ""
    )

tapeAlertTrap41 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 0, 41)
)
tapeAlertTrap41.setObjects(
      *(("TapeAlert-MIB", "hbaNumber"),
        ("TapeAlert-MIB", "hbaChannel"),
        ("TapeAlert-MIB", "driveScsiID"))
)
if mibBuilder.loadTexts:
    tapeAlertTrap41.setStatus(
        ""
    )

tapeAlertTrap42 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 0, 42)
)
tapeAlertTrap42.setObjects(
      *(("TapeAlert-MIB", "hbaNumber"),
        ("TapeAlert-MIB", "hbaChannel"),
        ("TapeAlert-MIB", "driveScsiID"))
)
if mibBuilder.loadTexts:
    tapeAlertTrap42.setStatus(
        ""
    )

tapeAlertTrap43 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 0, 43)
)
tapeAlertTrap43.setObjects(
      *(("TapeAlert-MIB", "hbaNumber"),
        ("TapeAlert-MIB", "hbaChannel"),
        ("TapeAlert-MIB", "driveScsiID"))
)
if mibBuilder.loadTexts:
    tapeAlertTrap43.setStatus(
        ""
    )

tapeAlertTrap44 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 0, 44)
)
tapeAlertTrap44.setObjects(
      *(("TapeAlert-MIB", "hbaNumber"),
        ("TapeAlert-MIB", "hbaChannel"),
        ("TapeAlert-MIB", "driveScsiID"))
)
if mibBuilder.loadTexts:
    tapeAlertTrap44.setStatus(
        ""
    )

tapeAlertTrap45 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 0, 45)
)
tapeAlertTrap45.setObjects(
      *(("TapeAlert-MIB", "hbaNumber"),
        ("TapeAlert-MIB", "hbaChannel"),
        ("TapeAlert-MIB", "driveScsiID"))
)
if mibBuilder.loadTexts:
    tapeAlertTrap45.setStatus(
        ""
    )

tapeAlertTrap46 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 0, 46)
)
tapeAlertTrap46.setObjects(
      *(("TapeAlert-MIB", "hbaNumber"),
        ("TapeAlert-MIB", "hbaChannel"),
        ("TapeAlert-MIB", "driveScsiID"))
)
if mibBuilder.loadTexts:
    tapeAlertTrap46.setStatus(
        ""
    )

tapeAlertTrap256 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 0, 256)
)
tapeAlertTrap256.setObjects(
      *(("TapeAlert-MIB", "hbaNumber"),
        ("TapeAlert-MIB", "hbaChannel"),
        ("TapeAlert-MIB", "driveScsiID"))
)
if mibBuilder.loadTexts:
    tapeAlertTrap256.setStatus(
        ""
    )

tapeAlertTrap257 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 0, 257)
)
tapeAlertTrap257.setObjects(
      *(("TapeAlert-MIB", "hbaNumber"),
        ("TapeAlert-MIB", "hbaChannel"),
        ("TapeAlert-MIB", "driveScsiID"))
)
if mibBuilder.loadTexts:
    tapeAlertTrap257.setStatus(
        ""
    )

tapeAlertTrap258 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 0, 258)
)
tapeAlertTrap258.setObjects(
      *(("TapeAlert-MIB", "hbaNumber"),
        ("TapeAlert-MIB", "hbaChannel"),
        ("TapeAlert-MIB", "driveScsiID"))
)
if mibBuilder.loadTexts:
    tapeAlertTrap258.setStatus(
        ""
    )

tapeAlertTrap259 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 0, 259)
)
tapeAlertTrap259.setObjects(
      *(("TapeAlert-MIB", "hbaNumber"),
        ("TapeAlert-MIB", "hbaChannel"),
        ("TapeAlert-MIB", "driveScsiID"))
)
if mibBuilder.loadTexts:
    tapeAlertTrap259.setStatus(
        ""
    )

tapeAlertTrap260 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 0, 260)
)
tapeAlertTrap260.setObjects(
      *(("TapeAlert-MIB", "hbaNumber"),
        ("TapeAlert-MIB", "hbaChannel"),
        ("TapeAlert-MIB", "driveScsiID"))
)
if mibBuilder.loadTexts:
    tapeAlertTrap260.setStatus(
        ""
    )

tapeAlertTrap261 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 0, 261)
)
tapeAlertTrap261.setObjects(
      *(("TapeAlert-MIB", "hbaNumber"),
        ("TapeAlert-MIB", "hbaChannel"),
        ("TapeAlert-MIB", "driveScsiID"))
)
if mibBuilder.loadTexts:
    tapeAlertTrap261.setStatus(
        ""
    )

tapeAlertTrap262 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 0, 262)
)
tapeAlertTrap262.setObjects(
      *(("TapeAlert-MIB", "hbaNumber"),
        ("TapeAlert-MIB", "hbaChannel"),
        ("TapeAlert-MIB", "driveScsiID"))
)
if mibBuilder.loadTexts:
    tapeAlertTrap262.setStatus(
        ""
    )

tapeAlertTrap263 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 0, 263)
)
tapeAlertTrap263.setObjects(
      *(("TapeAlert-MIB", "hbaNumber"),
        ("TapeAlert-MIB", "hbaChannel"),
        ("TapeAlert-MIB", "driveScsiID"))
)
if mibBuilder.loadTexts:
    tapeAlertTrap263.setStatus(
        ""
    )

tapeAlertTrap264 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 0, 264)
)
tapeAlertTrap264.setObjects(
      *(("TapeAlert-MIB", "hbaNumber"),
        ("TapeAlert-MIB", "hbaChannel"),
        ("TapeAlert-MIB", "driveScsiID"))
)
if mibBuilder.loadTexts:
    tapeAlertTrap264.setStatus(
        ""
    )

tapeAlertTrap265 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 0, 265)
)
tapeAlertTrap265.setObjects(
      *(("TapeAlert-MIB", "hbaNumber"),
        ("TapeAlert-MIB", "hbaChannel"),
        ("TapeAlert-MIB", "driveScsiID"))
)
if mibBuilder.loadTexts:
    tapeAlertTrap265.setStatus(
        ""
    )

tapeAlertTrap266 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 0, 266)
)
tapeAlertTrap266.setObjects(
      *(("TapeAlert-MIB", "hbaNumber"),
        ("TapeAlert-MIB", "hbaChannel"),
        ("TapeAlert-MIB", "driveScsiID"))
)
if mibBuilder.loadTexts:
    tapeAlertTrap266.setStatus(
        ""
    )

tapeAlertTrap267 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 0, 267)
)
tapeAlertTrap267.setObjects(
      *(("TapeAlert-MIB", "hbaNumber"),
        ("TapeAlert-MIB", "hbaChannel"),
        ("TapeAlert-MIB", "driveScsiID"))
)
if mibBuilder.loadTexts:
    tapeAlertTrap267.setStatus(
        ""
    )

tapeAlertTrap268 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 0, 268)
)
tapeAlertTrap268.setObjects(
      *(("TapeAlert-MIB", "hbaNumber"),
        ("TapeAlert-MIB", "hbaChannel"),
        ("TapeAlert-MIB", "driveScsiID"))
)
if mibBuilder.loadTexts:
    tapeAlertTrap268.setStatus(
        ""
    )

tapeAlertTrap269 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 0, 269)
)
tapeAlertTrap269.setObjects(
      *(("TapeAlert-MIB", "hbaNumber"),
        ("TapeAlert-MIB", "hbaChannel"),
        ("TapeAlert-MIB", "driveScsiID"))
)
if mibBuilder.loadTexts:
    tapeAlertTrap269.setStatus(
        ""
    )

tapeAlertTrap270 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 0, 270)
)
tapeAlertTrap270.setObjects(
      *(("TapeAlert-MIB", "hbaNumber"),
        ("TapeAlert-MIB", "hbaChannel"),
        ("TapeAlert-MIB", "driveScsiID"))
)
if mibBuilder.loadTexts:
    tapeAlertTrap270.setStatus(
        ""
    )

tapeAlertTrap271 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 0, 271)
)
tapeAlertTrap271.setObjects(
      *(("TapeAlert-MIB", "hbaNumber"),
        ("TapeAlert-MIB", "hbaChannel"),
        ("TapeAlert-MIB", "driveScsiID"))
)
if mibBuilder.loadTexts:
    tapeAlertTrap271.setStatus(
        ""
    )

tapeAlertTrap272 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 0, 272)
)
tapeAlertTrap272.setObjects(
      *(("TapeAlert-MIB", "hbaNumber"),
        ("TapeAlert-MIB", "hbaChannel"),
        ("TapeAlert-MIB", "driveScsiID"))
)
if mibBuilder.loadTexts:
    tapeAlertTrap272.setStatus(
        ""
    )

tapeAlertTrap273 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 0, 273)
)
tapeAlertTrap273.setObjects(
      *(("TapeAlert-MIB", "hbaNumber"),
        ("TapeAlert-MIB", "hbaChannel"),
        ("TapeAlert-MIB", "driveScsiID"))
)
if mibBuilder.loadTexts:
    tapeAlertTrap273.setStatus(
        ""
    )

tapeAlertTrap274 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 0, 274)
)
tapeAlertTrap274.setObjects(
      *(("TapeAlert-MIB", "hbaNumber"),
        ("TapeAlert-MIB", "hbaChannel"),
        ("TapeAlert-MIB", "driveScsiID"))
)
if mibBuilder.loadTexts:
    tapeAlertTrap274.setStatus(
        ""
    )

tapeAlertTrap275 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 0, 275)
)
tapeAlertTrap275.setObjects(
      *(("TapeAlert-MIB", "hbaNumber"),
        ("TapeAlert-MIB", "hbaChannel"),
        ("TapeAlert-MIB", "driveScsiID"))
)
if mibBuilder.loadTexts:
    tapeAlertTrap275.setStatus(
        ""
    )

tapeAlertTrap276 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 0, 276)
)
tapeAlertTrap276.setObjects(
      *(("TapeAlert-MIB", "hbaNumber"),
        ("TapeAlert-MIB", "hbaChannel"),
        ("TapeAlert-MIB", "driveScsiID"))
)
if mibBuilder.loadTexts:
    tapeAlertTrap276.setStatus(
        ""
    )

tapeAlertTrap277 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 0, 277)
)
tapeAlertTrap277.setObjects(
      *(("TapeAlert-MIB", "hbaNumber"),
        ("TapeAlert-MIB", "hbaChannel"),
        ("TapeAlert-MIB", "driveScsiID"))
)
if mibBuilder.loadTexts:
    tapeAlertTrap277.setStatus(
        ""
    )

tapeAlertTrap278 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 0, 278)
)
tapeAlertTrap278.setObjects(
      *(("TapeAlert-MIB", "hbaNumber"),
        ("TapeAlert-MIB", "hbaChannel"),
        ("TapeAlert-MIB", "driveScsiID"))
)
if mibBuilder.loadTexts:
    tapeAlertTrap278.setStatus(
        ""
    )

tapeAlertTrap279 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 0, 279)
)
tapeAlertTrap279.setObjects(
      *(("TapeAlert-MIB", "hbaNumber"),
        ("TapeAlert-MIB", "hbaChannel"),
        ("TapeAlert-MIB", "driveScsiID"))
)
if mibBuilder.loadTexts:
    tapeAlertTrap279.setStatus(
        ""
    )

tapeAlertTrap280 = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 9, 7, 1, 0, 280)
)
tapeAlertTrap280.setObjects(
      *(("TapeAlert-MIB", "hbaNumber"),
        ("TapeAlert-MIB", "hbaChannel"),
        ("TapeAlert-MIB", "driveScsiID"))
)
if mibBuilder.loadTexts:
    tapeAlertTrap280.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TapeAlert-MIB",
    **{"hp": hp,
       "nm": nm,
       "system": system,
       "netPeripheral": netPeripheral,
       "netTape": netTape,
       "tapeAlert": tapeAlert,
       "tapeAlertTrap1": tapeAlertTrap1,
       "tapeAlertTrap2": tapeAlertTrap2,
       "tapeAlertTrap3": tapeAlertTrap3,
       "tapeAlertTrap4": tapeAlertTrap4,
       "tapeAlertTrap5": tapeAlertTrap5,
       "tapeAlertTrap6": tapeAlertTrap6,
       "tapeAlertTrap7": tapeAlertTrap7,
       "tapeAlertTrap8": tapeAlertTrap8,
       "tapeAlertTrap9": tapeAlertTrap9,
       "tapeAlertTrap10": tapeAlertTrap10,
       "tapeAlertTrap11": tapeAlertTrap11,
       "tapeAlertTrap12": tapeAlertTrap12,
       "tapeAlertTrap13": tapeAlertTrap13,
       "tapeAlertTrap14": tapeAlertTrap14,
       "tapeAlertTrap15": tapeAlertTrap15,
       "tapeAlertTrap16": tapeAlertTrap16,
       "tapeAlertTrap17": tapeAlertTrap17,
       "tapeAlertTrap18": tapeAlertTrap18,
       "tapeAlertTrap19": tapeAlertTrap19,
       "tapeAlertTrap20": tapeAlertTrap20,
       "tapeAlertTrap21": tapeAlertTrap21,
       "tapeAlertTrap22": tapeAlertTrap22,
       "tapeAlertTrap23": tapeAlertTrap23,
       "tapeAlertTrap29": tapeAlertTrap29,
       "tapeAlertTrap30": tapeAlertTrap30,
       "tapeAlertTrap31": tapeAlertTrap31,
       "tapeAlertTrap32": tapeAlertTrap32,
       "tapeAlertTrap33": tapeAlertTrap33,
       "tapeAlertTrap34": tapeAlertTrap34,
       "tapeAlertTrap35": tapeAlertTrap35,
       "tapeAlertTrap36": tapeAlertTrap36,
       "tapeAlertTrap37": tapeAlertTrap37,
       "tapeAlertTrap38": tapeAlertTrap38,
       "tapeAlertTrap39": tapeAlertTrap39,
       "tapeAlertTrap40": tapeAlertTrap40,
       "tapeAlertTrap41": tapeAlertTrap41,
       "tapeAlertTrap42": tapeAlertTrap42,
       "tapeAlertTrap43": tapeAlertTrap43,
       "tapeAlertTrap44": tapeAlertTrap44,
       "tapeAlertTrap45": tapeAlertTrap45,
       "tapeAlertTrap46": tapeAlertTrap46,
       "tapeAlertTrap256": tapeAlertTrap256,
       "tapeAlertTrap257": tapeAlertTrap257,
       "tapeAlertTrap258": tapeAlertTrap258,
       "tapeAlertTrap259": tapeAlertTrap259,
       "tapeAlertTrap260": tapeAlertTrap260,
       "tapeAlertTrap261": tapeAlertTrap261,
       "tapeAlertTrap262": tapeAlertTrap262,
       "tapeAlertTrap263": tapeAlertTrap263,
       "tapeAlertTrap264": tapeAlertTrap264,
       "tapeAlertTrap265": tapeAlertTrap265,
       "tapeAlertTrap266": tapeAlertTrap266,
       "tapeAlertTrap267": tapeAlertTrap267,
       "tapeAlertTrap268": tapeAlertTrap268,
       "tapeAlertTrap269": tapeAlertTrap269,
       "tapeAlertTrap270": tapeAlertTrap270,
       "tapeAlertTrap271": tapeAlertTrap271,
       "tapeAlertTrap272": tapeAlertTrap272,
       "tapeAlertTrap273": tapeAlertTrap273,
       "tapeAlertTrap274": tapeAlertTrap274,
       "tapeAlertTrap275": tapeAlertTrap275,
       "tapeAlertTrap276": tapeAlertTrap276,
       "tapeAlertTrap277": tapeAlertTrap277,
       "tapeAlertTrap278": tapeAlertTrap278,
       "tapeAlertTrap279": tapeAlertTrap279,
       "tapeAlertTrap280": tapeAlertTrap280,
       "control": control,
       "revMajor": revMajor,
       "revMinor": revMinor,
       "trapEnable": trapEnable,
       "autoCleanEnable": autoCleanEnable,
       "autoCopyEnable": autoCopyEnable,
       "numDevices": numDevices,
       "devTable": devTable,
       "devInfo": devInfo,
       "devNum": devNum,
       "tapeAlertCapability": tapeAlertCapability,
       "hbaName": hbaName,
       "hbaNumber": hbaNumber,
       "hbaChannel": hbaChannel,
       "driveScsiID": driveScsiID,
       "driveInquiry": driveInquiry,
       "driveFirmware": driveFirmware,
       "driveType": driveType,
       "driveCompress": driveCompress,
       "currentMedia": currentMedia,
       "driveSerialNum": driveSerialNum,
       "numErrors": numErrors,
       "errorHistoryTable": errorHistoryTable,
       "errorHistoryEntry": errorHistoryEntry,
       "errorIndex": errorIndex,
       "errorHbaNumber": errorHbaNumber,
       "errorHbaChannel": errorHbaChannel,
       "errorDriveScsiID": errorDriveScsiID,
       "errorDate": errorDate,
       "errorTrapNum": errorTrapNum,
       "errorMedia": errorMedia}
)
