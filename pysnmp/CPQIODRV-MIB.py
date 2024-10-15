# SNMP MIB module (CPQIODRV-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CPQIODRV-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:17:29 2024
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

(compaq,
 cpqHoTrapFlags) = mibBuilder.importSymbols(
    "CPQHOST-MIB",
    "compaq",
    "cpqHoTrapFlags")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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

_CpqIoDrv_ObjectIdentity = ObjectIdentity
cpqIoDrv = _CpqIoDrv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 172)
)
_CpqIoDrvMibRev_ObjectIdentity = ObjectIdentity
cpqIoDrvMibRev = _CpqIoDrvMibRev_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 172, 1)
)


class _CpqIoDrvMibRevMajor_Type(Integer32):
    """Custom type cpqIoDrvMibRevMajor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CpqIoDrvMibRevMajor_Type.__name__ = "Integer32"
_CpqIoDrvMibRevMajor_Object = MibScalar
cpqIoDrvMibRevMajor = _CpqIoDrvMibRevMajor_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 1, 1),
    _CpqIoDrvMibRevMajor_Type()
)
cpqIoDrvMibRevMajor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIoDrvMibRevMajor.setStatus("mandatory")


class _CpqIoDrvMibRevMinor_Type(Integer32):
    """Custom type cpqIoDrvMibRevMinor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CpqIoDrvMibRevMinor_Type.__name__ = "Integer32"
_CpqIoDrvMibRevMinor_Object = MibScalar
cpqIoDrvMibRevMinor = _CpqIoDrvMibRevMinor_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 1, 2),
    _CpqIoDrvMibRevMinor_Type()
)
cpqIoDrvMibRevMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIoDrvMibRevMinor.setStatus("mandatory")


class _CpqIoDrvMibCondition_Type(Integer32):
    """Custom type cpqIoDrvMibCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqIoDrvMibCondition_Type.__name__ = "Integer32"
_CpqIoDrvMibCondition_Object = MibScalar
cpqIoDrvMibCondition = _CpqIoDrvMibCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 1, 3),
    _CpqIoDrvMibCondition_Type()
)
cpqIoDrvMibCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIoDrvMibCondition.setStatus("mandatory")
_CpqIoDrvComponent_ObjectIdentity = ObjectIdentity
cpqIoDrvComponent = _CpqIoDrvComponent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 172, 2)
)
_CpqIoDrvInfo_ObjectIdentity = ObjectIdentity
cpqIoDrvInfo = _CpqIoDrvInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 1)
)
_CpqIoDrvInfoTable_Object = MibTable
cpqIoDrvInfoTable = _CpqIoDrvInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cpqIoDrvInfoTable.setStatus("mandatory")
_CpqIoDrvInfoEntry_Object = MibTableRow
cpqIoDrvInfoEntry = _CpqIoDrvInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 1, 1, 1)
)
cpqIoDrvInfoEntry.setIndexNames(
    (0, "CPQIODRV-MIB", "cpqIoDrvInfoIndex"),
)
if mibBuilder.loadTexts:
    cpqIoDrvInfoEntry.setStatus("mandatory")


class _CpqIoDrvInfoIndex_Type(Integer32):
    """Custom type cpqIoDrvInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_CpqIoDrvInfoIndex_Type.__name__ = "Integer32"
_CpqIoDrvInfoIndex_Object = MibTableColumn
cpqIoDrvInfoIndex = _CpqIoDrvInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 1, 1, 1, 1),
    _CpqIoDrvInfoIndex_Type()
)
cpqIoDrvInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIoDrvInfoIndex.setStatus("mandatory")


class _CpqIoDrvInfoStatus_Type(Integer32):
    """Custom type cpqIoDrvInfoStatus based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_CpqIoDrvInfoStatus_Type.__name__ = "Integer32"
_CpqIoDrvInfoStatus_Object = MibTableColumn
cpqIoDrvInfoStatus = _CpqIoDrvInfoStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 1, 1, 1, 2),
    _CpqIoDrvInfoStatus_Type()
)
cpqIoDrvInfoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIoDrvInfoStatus.setStatus("mandatory")


class _CpqIoDrvInfoName_Type(DisplayString):
    """Custom type cpqIoDrvInfoName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_CpqIoDrvInfoName_Type.__name__ = "DisplayString"
_CpqIoDrvInfoName_Object = MibTableColumn
cpqIoDrvInfoName = _CpqIoDrvInfoName_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 1, 1, 1, 3),
    _CpqIoDrvInfoName_Type()
)
cpqIoDrvInfoName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqIoDrvInfoName.setStatus("mandatory")


class _CpqIoDrvInfoSerialNumber_Type(DisplayString):
    """Custom type cpqIoDrvInfoSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_CpqIoDrvInfoSerialNumber_Type.__name__ = "DisplayString"
_CpqIoDrvInfoSerialNumber_Object = MibTableColumn
cpqIoDrvInfoSerialNumber = _CpqIoDrvInfoSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 1, 1, 1, 4),
    _CpqIoDrvInfoSerialNumber_Type()
)
cpqIoDrvInfoSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIoDrvInfoSerialNumber.setStatus("mandatory")


class _CpqIoDrvInfoPartNumber_Type(DisplayString):
    """Custom type cpqIoDrvInfoPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_CpqIoDrvInfoPartNumber_Type.__name__ = "DisplayString"
_CpqIoDrvInfoPartNumber_Object = MibTableColumn
cpqIoDrvInfoPartNumber = _CpqIoDrvInfoPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 1, 1, 1, 5),
    _CpqIoDrvInfoPartNumber_Type()
)
cpqIoDrvInfoPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIoDrvInfoPartNumber.setStatus("mandatory")


class _CpqIoDrvInfoSubVendorPartNumber_Type(DisplayString):
    """Custom type cpqIoDrvInfoSubVendorPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_CpqIoDrvInfoSubVendorPartNumber_Type.__name__ = "DisplayString"
_CpqIoDrvInfoSubVendorPartNumber_Object = MibTableColumn
cpqIoDrvInfoSubVendorPartNumber = _CpqIoDrvInfoSubVendorPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 1, 1, 1, 6),
    _CpqIoDrvInfoSubVendorPartNumber_Type()
)
cpqIoDrvInfoSubVendorPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIoDrvInfoSubVendorPartNumber.setStatus("mandatory")


class _CpqIoDrvInfoSparesPartNumber_Type(DisplayString):
    """Custom type cpqIoDrvInfoSparesPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_CpqIoDrvInfoSparesPartNumber_Type.__name__ = "DisplayString"
_CpqIoDrvInfoSparesPartNumber_Object = MibTableColumn
cpqIoDrvInfoSparesPartNumber = _CpqIoDrvInfoSparesPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 1, 1, 1, 7),
    _CpqIoDrvInfoSparesPartNumber_Type()
)
cpqIoDrvInfoSparesPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIoDrvInfoSparesPartNumber.setStatus("mandatory")


class _CpqIoDrvInfoAssemblyNumber_Type(DisplayString):
    """Custom type cpqIoDrvInfoAssemblyNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_CpqIoDrvInfoAssemblyNumber_Type.__name__ = "DisplayString"
_CpqIoDrvInfoAssemblyNumber_Object = MibTableColumn
cpqIoDrvInfoAssemblyNumber = _CpqIoDrvInfoAssemblyNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 1, 1, 1, 8),
    _CpqIoDrvInfoAssemblyNumber_Type()
)
cpqIoDrvInfoAssemblyNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIoDrvInfoAssemblyNumber.setStatus("mandatory")


class _CpqIoDrvInfoFirmwareVersion_Type(DisplayString):
    """Custom type cpqIoDrvInfoFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_CpqIoDrvInfoFirmwareVersion_Type.__name__ = "DisplayString"
_CpqIoDrvInfoFirmwareVersion_Object = MibTableColumn
cpqIoDrvInfoFirmwareVersion = _CpqIoDrvInfoFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 1, 1, 1, 9),
    _CpqIoDrvInfoFirmwareVersion_Type()
)
cpqIoDrvInfoFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIoDrvInfoFirmwareVersion.setStatus("mandatory")


class _CpqIoDrvInfoDriverVersion_Type(DisplayString):
    """Custom type cpqIoDrvInfoDriverVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_CpqIoDrvInfoDriverVersion_Type.__name__ = "DisplayString"
_CpqIoDrvInfoDriverVersion_Object = MibTableColumn
cpqIoDrvInfoDriverVersion = _CpqIoDrvInfoDriverVersion_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 1, 1, 1, 10),
    _CpqIoDrvInfoDriverVersion_Type()
)
cpqIoDrvInfoDriverVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIoDrvInfoDriverVersion.setStatus("mandatory")


class _CpqIoDrvInfoUID_Type(DisplayString):
    """Custom type cpqIoDrvInfoUID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_CpqIoDrvInfoUID_Type.__name__ = "DisplayString"
_CpqIoDrvInfoUID_Object = MibTableColumn
cpqIoDrvInfoUID = _CpqIoDrvInfoUID_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 1, 1, 1, 11),
    _CpqIoDrvInfoUID_Type()
)
cpqIoDrvInfoUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIoDrvInfoUID.setStatus("mandatory")


class _CpqIoDrvInfoState_Type(Integer32):
    """Custom type cpqIoDrvInfoState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("attach", 10),
          ("attached", 2),
          ("attaching", 6),
          ("detach", 11),
          ("detached", 1),
          ("detaching", 5),
          ("error", 4),
          ("format", 12),
          ("formatting", 8),
          ("minimal", 3),
          ("scanning", 7),
          ("unknown", 0),
          ("update", 13),
          ("updating", 9))
    )


_CpqIoDrvInfoState_Type.__name__ = "Integer32"
_CpqIoDrvInfoState_Object = MibTableColumn
cpqIoDrvInfoState = _CpqIoDrvInfoState_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 1, 1, 1, 12),
    _CpqIoDrvInfoState_Type()
)
cpqIoDrvInfoState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqIoDrvInfoState.setStatus("mandatory")


class _CpqIoDrvInfoClientDeviceName_Type(DisplayString):
    """Custom type cpqIoDrvInfoClientDeviceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_CpqIoDrvInfoClientDeviceName_Type.__name__ = "DisplayString"
_CpqIoDrvInfoClientDeviceName_Object = MibTableColumn
cpqIoDrvInfoClientDeviceName = _CpqIoDrvInfoClientDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 1, 1, 1, 13),
    _CpqIoDrvInfoClientDeviceName_Type()
)
cpqIoDrvInfoClientDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIoDrvInfoClientDeviceName.setStatus("mandatory")
_CpqIoDrvInfoBeacon_Type = Integer32
_CpqIoDrvInfoBeacon_Object = MibTableColumn
cpqIoDrvInfoBeacon = _CpqIoDrvInfoBeacon_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 1, 1, 1, 14),
    _CpqIoDrvInfoBeacon_Type()
)
cpqIoDrvInfoBeacon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqIoDrvInfoBeacon.setStatus("mandatory")


class _CpqIoDrvInfoPCIAddress_Type(DisplayString):
    """Custom type cpqIoDrvInfoPCIAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_CpqIoDrvInfoPCIAddress_Type.__name__ = "DisplayString"
_CpqIoDrvInfoPCIAddress_Object = MibTableColumn
cpqIoDrvInfoPCIAddress = _CpqIoDrvInfoPCIAddress_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 1, 1, 1, 15),
    _CpqIoDrvInfoPCIAddress_Type()
)
cpqIoDrvInfoPCIAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIoDrvInfoPCIAddress.setStatus("mandatory")


class _CpqIoDrvInfoPCIDeviceID_Type(DisplayString):
    """Custom type cpqIoDrvInfoPCIDeviceID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_CpqIoDrvInfoPCIDeviceID_Type.__name__ = "DisplayString"
_CpqIoDrvInfoPCIDeviceID_Object = MibTableColumn
cpqIoDrvInfoPCIDeviceID = _CpqIoDrvInfoPCIDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 1, 1, 1, 16),
    _CpqIoDrvInfoPCIDeviceID_Type()
)
cpqIoDrvInfoPCIDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIoDrvInfoPCIDeviceID.setStatus("mandatory")


class _CpqIoDrvInfoPCISubdeviceID_Type(DisplayString):
    """Custom type cpqIoDrvInfoPCISubdeviceID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_CpqIoDrvInfoPCISubdeviceID_Type.__name__ = "DisplayString"
_CpqIoDrvInfoPCISubdeviceID_Object = MibTableColumn
cpqIoDrvInfoPCISubdeviceID = _CpqIoDrvInfoPCISubdeviceID_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 1, 1, 1, 17),
    _CpqIoDrvInfoPCISubdeviceID_Type()
)
cpqIoDrvInfoPCISubdeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIoDrvInfoPCISubdeviceID.setStatus("mandatory")


class _CpqIoDrvInfoPCIVendorID_Type(DisplayString):
    """Custom type cpqIoDrvInfoPCIVendorID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_CpqIoDrvInfoPCIVendorID_Type.__name__ = "DisplayString"
_CpqIoDrvInfoPCIVendorID_Object = MibTableColumn
cpqIoDrvInfoPCIVendorID = _CpqIoDrvInfoPCIVendorID_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 1, 1, 1, 18),
    _CpqIoDrvInfoPCIVendorID_Type()
)
cpqIoDrvInfoPCIVendorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIoDrvInfoPCIVendorID.setStatus("mandatory")


class _CpqIoDrvInfoPCISubvendorID_Type(DisplayString):
    """Custom type cpqIoDrvInfoPCISubvendorID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_CpqIoDrvInfoPCISubvendorID_Type.__name__ = "DisplayString"
_CpqIoDrvInfoPCISubvendorID_Object = MibTableColumn
cpqIoDrvInfoPCISubvendorID = _CpqIoDrvInfoPCISubvendorID_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 1, 1, 1, 19),
    _CpqIoDrvInfoPCISubvendorID_Type()
)
cpqIoDrvInfoPCISubvendorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIoDrvInfoPCISubvendorID.setStatus("mandatory")


class _CpqIoDrvInfoPCISlot_Type(Integer32):
    """Custom type cpqIoDrvInfoPCISlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_CpqIoDrvInfoPCISlot_Type.__name__ = "Integer32"
_CpqIoDrvInfoPCISlot_Object = MibTableColumn
cpqIoDrvInfoPCISlot = _CpqIoDrvInfoPCISlot_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 1, 1, 1, 20),
    _CpqIoDrvInfoPCISlot_Type()
)
cpqIoDrvInfoPCISlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIoDrvInfoPCISlot.setStatus("mandatory")
_CpqIoDrvInfoWearoutIndicator_Type = Integer32
_CpqIoDrvInfoWearoutIndicator_Object = MibTableColumn
cpqIoDrvInfoWearoutIndicator = _CpqIoDrvInfoWearoutIndicator_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 1, 1, 1, 21),
    _CpqIoDrvInfoWearoutIndicator_Type()
)
cpqIoDrvInfoWearoutIndicator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIoDrvInfoWearoutIndicator.setStatus("mandatory")
_CpqIoDrvInfoFlashbackIndicator_Type = Integer32
_CpqIoDrvInfoFlashbackIndicator_Object = MibTableColumn
cpqIoDrvInfoFlashbackIndicator = _CpqIoDrvInfoFlashbackIndicator_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 1, 1, 1, 22),
    _CpqIoDrvInfoFlashbackIndicator_Type()
)
cpqIoDrvInfoFlashbackIndicator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIoDrvInfoFlashbackIndicator.setStatus("mandatory")
_CpqIoDrvInfoNonWritableIndicator_Type = Integer32
_CpqIoDrvInfoNonWritableIndicator_Object = MibTableColumn
cpqIoDrvInfoNonWritableIndicator = _CpqIoDrvInfoNonWritableIndicator_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 1, 1, 1, 23),
    _CpqIoDrvInfoNonWritableIndicator_Type()
)
cpqIoDrvInfoNonWritableIndicator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIoDrvInfoNonWritableIndicator.setStatus("mandatory")


class _CpqIoDrvInfoCurrentTemp_Type(Integer32):
    """Custom type cpqIoDrvInfoCurrentTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_CpqIoDrvInfoCurrentTemp_Type.__name__ = "Integer32"
_CpqIoDrvInfoCurrentTemp_Object = MibTableColumn
cpqIoDrvInfoCurrentTemp = _CpqIoDrvInfoCurrentTemp_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 1, 1, 1, 24),
    _CpqIoDrvInfoCurrentTemp_Type()
)
cpqIoDrvInfoCurrentTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIoDrvInfoCurrentTemp.setStatus("mandatory")


class _CpqIoDrvInfoPercentLifeRemaining_Type(Integer32):
    """Custom type cpqIoDrvInfoPercentLifeRemaining based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CpqIoDrvInfoPercentLifeRemaining_Type.__name__ = "Integer32"
_CpqIoDrvInfoPercentLifeRemaining_Object = MibTableColumn
cpqIoDrvInfoPercentLifeRemaining = _CpqIoDrvInfoPercentLifeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 1, 1, 1, 25),
    _CpqIoDrvInfoPercentLifeRemaining_Type()
)
cpqIoDrvInfoPercentLifeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIoDrvInfoPercentLifeRemaining.setStatus("mandatory")
_CpqIoDrvInfoShortTermWearoutDate_Type = DisplayString
_CpqIoDrvInfoShortTermWearoutDate_Object = MibTableColumn
cpqIoDrvInfoShortTermWearoutDate = _CpqIoDrvInfoShortTermWearoutDate_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 1, 1, 1, 26),
    _CpqIoDrvInfoShortTermWearoutDate_Type()
)
cpqIoDrvInfoShortTermWearoutDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIoDrvInfoShortTermWearoutDate.setStatus("mandatory")
_CpqIoDrvInfoLongTermWearoutDate_Type = DisplayString
_CpqIoDrvInfoLongTermWearoutDate_Object = MibTableColumn
cpqIoDrvInfoLongTermWearoutDate = _CpqIoDrvInfoLongTermWearoutDate_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 1, 1, 1, 27),
    _CpqIoDrvInfoLongTermWearoutDate_Type()
)
cpqIoDrvInfoLongTermWearoutDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIoDrvInfoLongTermWearoutDate.setStatus("mandatory")
_CpqIoDrvInfoShortTermNonWritableDate_Type = DisplayString
_CpqIoDrvInfoShortTermNonWritableDate_Object = MibTableColumn
cpqIoDrvInfoShortTermNonWritableDate = _CpqIoDrvInfoShortTermNonWritableDate_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 1, 1, 1, 28),
    _CpqIoDrvInfoShortTermNonWritableDate_Type()
)
cpqIoDrvInfoShortTermNonWritableDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIoDrvInfoShortTermNonWritableDate.setStatus("mandatory")
_CpqIoDrvInfoLongTermNonWritableDate_Type = DisplayString
_CpqIoDrvInfoLongTermNonWritableDate_Object = MibTableColumn
cpqIoDrvInfoLongTermNonWritableDate = _CpqIoDrvInfoLongTermNonWritableDate_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 1, 1, 1, 29),
    _CpqIoDrvInfoLongTermNonWritableDate_Type()
)
cpqIoDrvInfoLongTermNonWritableDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIoDrvInfoLongTermNonWritableDate.setStatus("mandatory")
_CpqIoDrvExtn_ObjectIdentity = ObjectIdentity
cpqIoDrvExtn = _CpqIoDrvExtn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 2)
)
_CpqIoDrvExtnTable_Object = MibTable
cpqIoDrvExtnTable = _CpqIoDrvExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cpqIoDrvExtnTable.setStatus("mandatory")
_CpqIoDrvExtnEntry_Object = MibTableRow
cpqIoDrvExtnEntry = _CpqIoDrvExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 2, 1, 1)
)
cpqIoDrvExtnEntry.setIndexNames(
    (0, "CPQIODRV-MIB", "cpqIoDrvExtnIndex"),
)
if mibBuilder.loadTexts:
    cpqIoDrvExtnEntry.setStatus("mandatory")


class _CpqIoDrvExtnIndex_Type(Integer32):
    """Custom type cpqIoDrvExtnIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_CpqIoDrvExtnIndex_Type.__name__ = "Integer32"
_CpqIoDrvExtnIndex_Object = MibTableColumn
cpqIoDrvExtnIndex = _CpqIoDrvExtnIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 2, 1, 1, 1),
    _CpqIoDrvExtnIndex_Type()
)
cpqIoDrvExtnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIoDrvExtnIndex.setStatus("mandatory")
_CpqIoDrvExtnTotalPhysicalCapacityU_Type = Counter32
_CpqIoDrvExtnTotalPhysicalCapacityU_Object = MibTableColumn
cpqIoDrvExtnTotalPhysicalCapacityU = _CpqIoDrvExtnTotalPhysicalCapacityU_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 2, 1, 1, 2),
    _CpqIoDrvExtnTotalPhysicalCapacityU_Type()
)
cpqIoDrvExtnTotalPhysicalCapacityU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIoDrvExtnTotalPhysicalCapacityU.setStatus("mandatory")
_CpqIoDrvExtnTotalPhysicalCapacityL_Type = Counter32
_CpqIoDrvExtnTotalPhysicalCapacityL_Object = MibTableColumn
cpqIoDrvExtnTotalPhysicalCapacityL = _CpqIoDrvExtnTotalPhysicalCapacityL_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 2, 1, 1, 3),
    _CpqIoDrvExtnTotalPhysicalCapacityL_Type()
)
cpqIoDrvExtnTotalPhysicalCapacityL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIoDrvExtnTotalPhysicalCapacityL.setStatus("mandatory")
_CpqIoDrvExtnUsablePhysicalCapacityU_Type = Counter32
_CpqIoDrvExtnUsablePhysicalCapacityU_Object = MibTableColumn
cpqIoDrvExtnUsablePhysicalCapacityU = _CpqIoDrvExtnUsablePhysicalCapacityU_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 2, 1, 1, 4),
    _CpqIoDrvExtnUsablePhysicalCapacityU_Type()
)
cpqIoDrvExtnUsablePhysicalCapacityU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIoDrvExtnUsablePhysicalCapacityU.setStatus("mandatory")
_CpqIoDrvExtnUsablePhysicalCapacityL_Type = Counter32
_CpqIoDrvExtnUsablePhysicalCapacityL_Object = MibTableColumn
cpqIoDrvExtnUsablePhysicalCapacityL = _CpqIoDrvExtnUsablePhysicalCapacityL_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 2, 1, 1, 5),
    _CpqIoDrvExtnUsablePhysicalCapacityL_Type()
)
cpqIoDrvExtnUsablePhysicalCapacityL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIoDrvExtnUsablePhysicalCapacityL.setStatus("mandatory")
_CpqIoDrvExtnUsedPhysicalCapacityU_Type = Counter32
_CpqIoDrvExtnUsedPhysicalCapacityU_Object = MibTableColumn
cpqIoDrvExtnUsedPhysicalCapacityU = _CpqIoDrvExtnUsedPhysicalCapacityU_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 2, 1, 1, 6),
    _CpqIoDrvExtnUsedPhysicalCapacityU_Type()
)
cpqIoDrvExtnUsedPhysicalCapacityU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIoDrvExtnUsedPhysicalCapacityU.setStatus("mandatory")
_CpqIoDrvExtnUsedPhysicalCapacityL_Type = Counter32
_CpqIoDrvExtnUsedPhysicalCapacityL_Object = MibTableColumn
cpqIoDrvExtnUsedPhysicalCapacityL = _CpqIoDrvExtnUsedPhysicalCapacityL_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 2, 1, 1, 7),
    _CpqIoDrvExtnUsedPhysicalCapacityL_Type()
)
cpqIoDrvExtnUsedPhysicalCapacityL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIoDrvExtnUsedPhysicalCapacityL.setStatus("mandatory")
_CpqIoDrvExtnTotalLogicalCapacityU_Type = Counter32
_CpqIoDrvExtnTotalLogicalCapacityU_Object = MibTableColumn
cpqIoDrvExtnTotalLogicalCapacityU = _CpqIoDrvExtnTotalLogicalCapacityU_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 2, 1, 1, 8),
    _CpqIoDrvExtnTotalLogicalCapacityU_Type()
)
cpqIoDrvExtnTotalLogicalCapacityU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIoDrvExtnTotalLogicalCapacityU.setStatus("mandatory")
_CpqIoDrvExtnTotalLogicalCapacityL_Type = Counter32
_CpqIoDrvExtnTotalLogicalCapacityL_Object = MibTableColumn
cpqIoDrvExtnTotalLogicalCapacityL = _CpqIoDrvExtnTotalLogicalCapacityL_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 2, 1, 1, 9),
    _CpqIoDrvExtnTotalLogicalCapacityL_Type()
)
cpqIoDrvExtnTotalLogicalCapacityL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIoDrvExtnTotalLogicalCapacityL.setStatus("mandatory")
_CpqIoDrvExtnAvailableLogicalCapacityU_Type = Counter32
_CpqIoDrvExtnAvailableLogicalCapacityU_Object = MibTableColumn
cpqIoDrvExtnAvailableLogicalCapacityU = _CpqIoDrvExtnAvailableLogicalCapacityU_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 2, 1, 1, 10),
    _CpqIoDrvExtnAvailableLogicalCapacityU_Type()
)
cpqIoDrvExtnAvailableLogicalCapacityU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIoDrvExtnAvailableLogicalCapacityU.setStatus("mandatory")
_CpqIoDrvExtnAvailableLogicalCapacityL_Type = Counter32
_CpqIoDrvExtnAvailableLogicalCapacityL_Object = MibTableColumn
cpqIoDrvExtnAvailableLogicalCapacityL = _CpqIoDrvExtnAvailableLogicalCapacityL_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 2, 1, 1, 11),
    _CpqIoDrvExtnAvailableLogicalCapacityL_Type()
)
cpqIoDrvExtnAvailableLogicalCapacityL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIoDrvExtnAvailableLogicalCapacityL.setStatus("mandatory")
_CpqIoDrvExtnBytesReadU_Type = Counter32
_CpqIoDrvExtnBytesReadU_Object = MibTableColumn
cpqIoDrvExtnBytesReadU = _CpqIoDrvExtnBytesReadU_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 2, 1, 1, 12),
    _CpqIoDrvExtnBytesReadU_Type()
)
cpqIoDrvExtnBytesReadU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIoDrvExtnBytesReadU.setStatus("mandatory")
_CpqIoDrvExtnBytesReadL_Type = Counter32
_CpqIoDrvExtnBytesReadL_Object = MibTableColumn
cpqIoDrvExtnBytesReadL = _CpqIoDrvExtnBytesReadL_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 2, 1, 1, 13),
    _CpqIoDrvExtnBytesReadL_Type()
)
cpqIoDrvExtnBytesReadL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIoDrvExtnBytesReadL.setStatus("mandatory")
_CpqIoDrvExtnPhysicalBytesWrittenU_Type = Counter32
_CpqIoDrvExtnPhysicalBytesWrittenU_Object = MibTableColumn
cpqIoDrvExtnPhysicalBytesWrittenU = _CpqIoDrvExtnPhysicalBytesWrittenU_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 2, 1, 1, 14),
    _CpqIoDrvExtnPhysicalBytesWrittenU_Type()
)
cpqIoDrvExtnPhysicalBytesWrittenU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIoDrvExtnPhysicalBytesWrittenU.setStatus("mandatory")
_CpqIoDrvExtnPhysicalBytesWrittenL_Type = Counter32
_CpqIoDrvExtnPhysicalBytesWrittenL_Object = MibTableColumn
cpqIoDrvExtnPhysicalBytesWrittenL = _CpqIoDrvExtnPhysicalBytesWrittenL_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 2, 1, 1, 15),
    _CpqIoDrvExtnPhysicalBytesWrittenL_Type()
)
cpqIoDrvExtnPhysicalBytesWrittenL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIoDrvExtnPhysicalBytesWrittenL.setStatus("mandatory")
_CpqIoDrvExtnLogicalBytesWrittenU_Type = Counter32
_CpqIoDrvExtnLogicalBytesWrittenU_Object = MibTableColumn
cpqIoDrvExtnLogicalBytesWrittenU = _CpqIoDrvExtnLogicalBytesWrittenU_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 2, 1, 1, 16),
    _CpqIoDrvExtnLogicalBytesWrittenU_Type()
)
cpqIoDrvExtnLogicalBytesWrittenU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIoDrvExtnLogicalBytesWrittenU.setStatus("mandatory")
_CpqIoDrvExtnLogicalBytesWrittenL_Type = Counter32
_CpqIoDrvExtnLogicalBytesWrittenL_Object = MibTableColumn
cpqIoDrvExtnLogicalBytesWrittenL = _CpqIoDrvExtnLogicalBytesWrittenL_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 2, 1, 1, 17),
    _CpqIoDrvExtnLogicalBytesWrittenL_Type()
)
cpqIoDrvExtnLogicalBytesWrittenL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIoDrvExtnLogicalBytesWrittenL.setStatus("mandatory")
_CpqIoDrvExtnShortTermStartDate_Type = DisplayString
_CpqIoDrvExtnShortTermStartDate_Object = MibTableColumn
cpqIoDrvExtnShortTermStartDate = _CpqIoDrvExtnShortTermStartDate_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 2, 1, 1, 18),
    _CpqIoDrvExtnShortTermStartDate_Type()
)
cpqIoDrvExtnShortTermStartDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqIoDrvExtnShortTermStartDate.setStatus("mandatory")


class _CpqIoDrvExtnShortTermWindow_Type(Integer32):
    """Custom type cpqIoDrvExtnShortTermWindow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_CpqIoDrvExtnShortTermWindow_Type.__name__ = "Integer32"
_CpqIoDrvExtnShortTermWindow_Object = MibTableColumn
cpqIoDrvExtnShortTermWindow = _CpqIoDrvExtnShortTermWindow_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 2, 1, 1, 19),
    _CpqIoDrvExtnShortTermWindow_Type()
)
cpqIoDrvExtnShortTermWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqIoDrvExtnShortTermWindow.setStatus("mandatory")
_CpqIoDrvExtnShortTermEndDate_Type = DisplayString
_CpqIoDrvExtnShortTermEndDate_Object = MibTableColumn
cpqIoDrvExtnShortTermEndDate = _CpqIoDrvExtnShortTermEndDate_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 2, 1, 1, 20),
    _CpqIoDrvExtnShortTermEndDate_Type()
)
cpqIoDrvExtnShortTermEndDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqIoDrvExtnShortTermEndDate.setStatus("mandatory")
_CpqIoDrvExtnShortTermEndDateFloat_Type = Integer32
_CpqIoDrvExtnShortTermEndDateFloat_Object = MibTableColumn
cpqIoDrvExtnShortTermEndDateFloat = _CpqIoDrvExtnShortTermEndDateFloat_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 2, 1, 1, 21),
    _CpqIoDrvExtnShortTermEndDateFloat_Type()
)
cpqIoDrvExtnShortTermEndDateFloat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqIoDrvExtnShortTermEndDateFloat.setStatus("mandatory")
_CpqIoDrvExtnLongTermStartDate_Type = DisplayString
_CpqIoDrvExtnLongTermStartDate_Object = MibTableColumn
cpqIoDrvExtnLongTermStartDate = _CpqIoDrvExtnLongTermStartDate_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 2, 1, 1, 22),
    _CpqIoDrvExtnLongTermStartDate_Type()
)
cpqIoDrvExtnLongTermStartDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqIoDrvExtnLongTermStartDate.setStatus("mandatory")


class _CpqIoDrvExtnLongTermWindow_Type(Integer32):
    """Custom type cpqIoDrvExtnLongTermWindow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_CpqIoDrvExtnLongTermWindow_Type.__name__ = "Integer32"
_CpqIoDrvExtnLongTermWindow_Object = MibTableColumn
cpqIoDrvExtnLongTermWindow = _CpqIoDrvExtnLongTermWindow_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 2, 1, 1, 23),
    _CpqIoDrvExtnLongTermWindow_Type()
)
cpqIoDrvExtnLongTermWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqIoDrvExtnLongTermWindow.setStatus("mandatory")
_CpqIoDrvExtnLongTermEndDate_Type = DisplayString
_CpqIoDrvExtnLongTermEndDate_Object = MibTableColumn
cpqIoDrvExtnLongTermEndDate = _CpqIoDrvExtnLongTermEndDate_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 2, 1, 1, 24),
    _CpqIoDrvExtnLongTermEndDate_Type()
)
cpqIoDrvExtnLongTermEndDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqIoDrvExtnLongTermEndDate.setStatus("mandatory")
_CpqIoDrvExtnLongTermEndDateFloat_Type = Integer32
_CpqIoDrvExtnLongTermEndDateFloat_Object = MibTableColumn
cpqIoDrvExtnLongTermEndDateFloat = _CpqIoDrvExtnLongTermEndDateFloat_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 2, 1, 1, 25),
    _CpqIoDrvExtnLongTermEndDateFloat_Type()
)
cpqIoDrvExtnLongTermEndDateFloat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqIoDrvExtnLongTermEndDateFloat.setStatus("mandatory")
_CpqIoDrvExtnWriteRateAutoCalc_Type = Integer32
_CpqIoDrvExtnWriteRateAutoCalc_Object = MibTableColumn
cpqIoDrvExtnWriteRateAutoCalc = _CpqIoDrvExtnWriteRateAutoCalc_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 2, 1, 1, 26),
    _CpqIoDrvExtnWriteRateAutoCalc_Type()
)
cpqIoDrvExtnWriteRateAutoCalc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqIoDrvExtnWriteRateAutoCalc.setStatus("mandatory")
_CpqIoDrvExtnShortTermAvgU_Type = Counter32
_CpqIoDrvExtnShortTermAvgU_Object = MibTableColumn
cpqIoDrvExtnShortTermAvgU = _CpqIoDrvExtnShortTermAvgU_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 2, 1, 1, 27),
    _CpqIoDrvExtnShortTermAvgU_Type()
)
cpqIoDrvExtnShortTermAvgU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqIoDrvExtnShortTermAvgU.setStatus("mandatory")
_CpqIoDrvExtnShortTermAvgL_Type = Counter32
_CpqIoDrvExtnShortTermAvgL_Object = MibTableColumn
cpqIoDrvExtnShortTermAvgL = _CpqIoDrvExtnShortTermAvgL_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 2, 1, 1, 28),
    _CpqIoDrvExtnShortTermAvgL_Type()
)
cpqIoDrvExtnShortTermAvgL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqIoDrvExtnShortTermAvgL.setStatus("mandatory")
_CpqIoDrvExtnLongTermAvgU_Type = Counter32
_CpqIoDrvExtnLongTermAvgU_Object = MibTableColumn
cpqIoDrvExtnLongTermAvgU = _CpqIoDrvExtnLongTermAvgU_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 2, 1, 1, 29),
    _CpqIoDrvExtnLongTermAvgU_Type()
)
cpqIoDrvExtnLongTermAvgU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqIoDrvExtnLongTermAvgU.setStatus("mandatory")
_CpqIoDrvExtnLongTermAvgL_Type = Counter32
_CpqIoDrvExtnLongTermAvgL_Object = MibTableColumn
cpqIoDrvExtnLongTermAvgL = _CpqIoDrvExtnLongTermAvgL_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 2, 1, 1, 30),
    _CpqIoDrvExtnLongTermAvgL_Type()
)
cpqIoDrvExtnLongTermAvgL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqIoDrvExtnLongTermAvgL.setStatus("mandatory")


class _CpqIoDrvExtnConfidenceInterval_Type(Integer32):
    """Custom type cpqIoDrvExtnConfidenceInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CpqIoDrvExtnConfidenceInterval_Type.__name__ = "Integer32"
_CpqIoDrvExtnConfidenceInterval_Object = MibTableColumn
cpqIoDrvExtnConfidenceInterval = _CpqIoDrvExtnConfidenceInterval_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 2, 1, 1, 31),
    _CpqIoDrvExtnConfidenceInterval_Type()
)
cpqIoDrvExtnConfidenceInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpqIoDrvExtnConfidenceInterval.setStatus("mandatory")
_CpqIoDrvCapacity_ObjectIdentity = ObjectIdentity
cpqIoDrvCapacity = _CpqIoDrvCapacity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 3)
)
_CpqIoDrvCapacityTable_Object = MibTable
cpqIoDrvCapacityTable = _CpqIoDrvCapacityTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 3, 1)
)
if mibBuilder.loadTexts:
    cpqIoDrvCapacityTable.setStatus("mandatory")
_CpqIoDrvCapacityEntry_Object = MibTableRow
cpqIoDrvCapacityEntry = _CpqIoDrvCapacityEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 3, 1, 1)
)
cpqIoDrvCapacityEntry.setIndexNames(
    (0, "CPQIODRV-MIB", "cpqIoDrvCapacityInfoIndex"),
    (0, "CPQIODRV-MIB", "cpqIoDrvCapacityIndex"),
)
if mibBuilder.loadTexts:
    cpqIoDrvCapacityEntry.setStatus("mandatory")


class _CpqIoDrvCapacityInfoIndex_Type(Integer32):
    """Custom type cpqIoDrvCapacityInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_CpqIoDrvCapacityInfoIndex_Type.__name__ = "Integer32"
_CpqIoDrvCapacityInfoIndex_Object = MibTableColumn
cpqIoDrvCapacityInfoIndex = _CpqIoDrvCapacityInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 3, 1, 1, 1),
    _CpqIoDrvCapacityInfoIndex_Type()
)
cpqIoDrvCapacityInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIoDrvCapacityInfoIndex.setStatus("mandatory")


class _CpqIoDrvCapacityIndex_Type(Integer32):
    """Custom type cpqIoDrvCapacityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_CpqIoDrvCapacityIndex_Type.__name__ = "Integer32"
_CpqIoDrvCapacityIndex_Object = MibTableColumn
cpqIoDrvCapacityIndex = _CpqIoDrvCapacityIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 3, 1, 1, 2),
    _CpqIoDrvCapacityIndex_Type()
)
cpqIoDrvCapacityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIoDrvCapacityIndex.setStatus("optional")
_CpqIoDrvCapacityValueU_Type = Counter32
_CpqIoDrvCapacityValueU_Object = MibTableColumn
cpqIoDrvCapacityValueU = _CpqIoDrvCapacityValueU_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 3, 1, 1, 3),
    _CpqIoDrvCapacityValueU_Type()
)
cpqIoDrvCapacityValueU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIoDrvCapacityValueU.setStatus("mandatory")
_CpqIoDrvCapacityValueL_Type = Counter32
_CpqIoDrvCapacityValueL_Object = MibTableColumn
cpqIoDrvCapacityValueL = _CpqIoDrvCapacityValueL_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 3, 1, 1, 4),
    _CpqIoDrvCapacityValueL_Type()
)
cpqIoDrvCapacityValueL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIoDrvCapacityValueL.setStatus("mandatory")
_CpqIoDrvCapacityTimestamp_Type = DisplayString
_CpqIoDrvCapacityTimestamp_Object = MibTableColumn
cpqIoDrvCapacityTimestamp = _CpqIoDrvCapacityTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 3, 1, 1, 5),
    _CpqIoDrvCapacityTimestamp_Type()
)
cpqIoDrvCapacityTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIoDrvCapacityTimestamp.setStatus("mandatory")
_CpqIoDrvWrite_ObjectIdentity = ObjectIdentity
cpqIoDrvWrite = _CpqIoDrvWrite_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 4)
)
_CpqIoDrvWriteTable_Object = MibTable
cpqIoDrvWriteTable = _CpqIoDrvWriteTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 4, 1)
)
if mibBuilder.loadTexts:
    cpqIoDrvWriteTable.setStatus("optional")
_CpqIoDrvWriteEntry_Object = MibTableRow
cpqIoDrvWriteEntry = _CpqIoDrvWriteEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 4, 1, 1)
)
cpqIoDrvWriteEntry.setIndexNames(
    (0, "CPQIODRV-MIB", "cpqIoDrvWriteInfoIndex"),
    (0, "CPQIODRV-MIB", "cpqIoDrvWriteIndex"),
)
if mibBuilder.loadTexts:
    cpqIoDrvWriteEntry.setStatus("optional")


class _CpqIoDrvWriteInfoIndex_Type(Integer32):
    """Custom type cpqIoDrvWriteInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_CpqIoDrvWriteInfoIndex_Type.__name__ = "Integer32"
_CpqIoDrvWriteInfoIndex_Object = MibTableColumn
cpqIoDrvWriteInfoIndex = _CpqIoDrvWriteInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 4, 1, 1, 1),
    _CpqIoDrvWriteInfoIndex_Type()
)
cpqIoDrvWriteInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIoDrvWriteInfoIndex.setStatus("mandatory")


class _CpqIoDrvWriteIndex_Type(Integer32):
    """Custom type cpqIoDrvWriteIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_CpqIoDrvWriteIndex_Type.__name__ = "Integer32"
_CpqIoDrvWriteIndex_Object = MibTableColumn
cpqIoDrvWriteIndex = _CpqIoDrvWriteIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 4, 1, 1, 2),
    _CpqIoDrvWriteIndex_Type()
)
cpqIoDrvWriteIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIoDrvWriteIndex.setStatus("optional")
_CpqIoDrvWriteValueU_Type = Counter32
_CpqIoDrvWriteValueU_Object = MibTableColumn
cpqIoDrvWriteValueU = _CpqIoDrvWriteValueU_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 4, 1, 1, 3),
    _CpqIoDrvWriteValueU_Type()
)
cpqIoDrvWriteValueU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIoDrvWriteValueU.setStatus("mandatory")
_CpqIoDrvWriteValueL_Type = Counter32
_CpqIoDrvWriteValueL_Object = MibTableColumn
cpqIoDrvWriteValueL = _CpqIoDrvWriteValueL_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 4, 1, 1, 4),
    _CpqIoDrvWriteValueL_Type()
)
cpqIoDrvWriteValueL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIoDrvWriteValueL.setStatus("mandatory")
_CpqIoDrvWriteTimestamp_Type = DisplayString
_CpqIoDrvWriteTimestamp_Object = MibTableColumn
cpqIoDrvWriteTimestamp = _CpqIoDrvWriteTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 4, 1, 1, 5),
    _CpqIoDrvWriteTimestamp_Type()
)
cpqIoDrvWriteTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIoDrvWriteTimestamp.setStatus("mandatory")
_CpqIoDrvTemp_ObjectIdentity = ObjectIdentity
cpqIoDrvTemp = _CpqIoDrvTemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 5)
)
_CpqIoDrvTempTable_Object = MibTable
cpqIoDrvTempTable = _CpqIoDrvTempTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 5, 1)
)
if mibBuilder.loadTexts:
    cpqIoDrvTempTable.setStatus("optional")
_CpqIoDrvTempEntry_Object = MibTableRow
cpqIoDrvTempEntry = _CpqIoDrvTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 5, 1, 1)
)
cpqIoDrvTempEntry.setIndexNames(
    (0, "CPQIODRV-MIB", "cpqIoDrvTempInfoIndex"),
    (0, "CPQIODRV-MIB", "cpqIoDrvTempIndex"),
)
if mibBuilder.loadTexts:
    cpqIoDrvTempEntry.setStatus("optional")


class _CpqIoDrvTempInfoIndex_Type(Integer32):
    """Custom type cpqIoDrvTempInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_CpqIoDrvTempInfoIndex_Type.__name__ = "Integer32"
_CpqIoDrvTempInfoIndex_Object = MibTableColumn
cpqIoDrvTempInfoIndex = _CpqIoDrvTempInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 5, 1, 1, 1),
    _CpqIoDrvTempInfoIndex_Type()
)
cpqIoDrvTempInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIoDrvTempInfoIndex.setStatus("mandatory")


class _CpqIoDrvTempIndex_Type(Integer32):
    """Custom type cpqIoDrvTempIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CpqIoDrvTempIndex_Type.__name__ = "Integer32"
_CpqIoDrvTempIndex_Object = MibTableColumn
cpqIoDrvTempIndex = _CpqIoDrvTempIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 5, 1, 1, 2),
    _CpqIoDrvTempIndex_Type()
)
cpqIoDrvTempIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIoDrvTempIndex.setStatus("optional")


class _CpqIoDrvTempValue_Type(Integer32):
    """Custom type cpqIoDrvTempValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_CpqIoDrvTempValue_Type.__name__ = "Integer32"
_CpqIoDrvTempValue_Object = MibTableColumn
cpqIoDrvTempValue = _CpqIoDrvTempValue_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 5, 1, 1, 3),
    _CpqIoDrvTempValue_Type()
)
cpqIoDrvTempValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIoDrvTempValue.setStatus("mandatory")
_CpqIoDrvTempTimestamp_Type = Counter32
_CpqIoDrvTempTimestamp_Object = MibTableColumn
cpqIoDrvTempTimestamp = _CpqIoDrvTempTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 5, 1, 1, 4),
    _CpqIoDrvTempTimestamp_Type()
)
cpqIoDrvTempTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIoDrvTempTimestamp.setStatus("mandatory")
_CpqIoDrvProc_ObjectIdentity = ObjectIdentity
cpqIoDrvProc = _CpqIoDrvProc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 6)
)
_CpqIoDrvProcTable_Object = MibTable
cpqIoDrvProcTable = _CpqIoDrvProcTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 6, 1)
)
if mibBuilder.loadTexts:
    cpqIoDrvProcTable.setStatus("optional")
_CpqIoDrvProcEntry_Object = MibTableRow
cpqIoDrvProcEntry = _CpqIoDrvProcEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 6, 1, 1)
)
cpqIoDrvProcEntry.setIndexNames(
    (0, "CPQIODRV-MIB", "cpqIoDrvProcIndex"),
)
if mibBuilder.loadTexts:
    cpqIoDrvProcEntry.setStatus("optional")


class _CpqIoDrvProcIndex_Type(Integer32):
    """Custom type cpqIoDrvProcIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_CpqIoDrvProcIndex_Type.__name__ = "Integer32"
_CpqIoDrvProcIndex_Object = MibTableColumn
cpqIoDrvProcIndex = _CpqIoDrvProcIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 6, 1, 1, 1),
    _CpqIoDrvProcIndex_Type()
)
cpqIoDrvProcIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIoDrvProcIndex.setStatus("optional")


class _CpqIoDrvProcName_Type(DisplayString):
    """Custom type cpqIoDrvProcName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_CpqIoDrvProcName_Type.__name__ = "DisplayString"
_CpqIoDrvProcName_Object = MibTableColumn
cpqIoDrvProcName = _CpqIoDrvProcName_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 6, 1, 1, 2),
    _CpqIoDrvProcName_Type()
)
cpqIoDrvProcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIoDrvProcName.setStatus("mandatory")


class _CpqIoDrvProcState_Type(DisplayString):
    """Custom type cpqIoDrvProcState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_CpqIoDrvProcState_Type.__name__ = "DisplayString"
_CpqIoDrvProcState_Object = MibTableColumn
cpqIoDrvProcState = _CpqIoDrvProcState_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 6, 1, 1, 3),
    _CpqIoDrvProcState_Type()
)
cpqIoDrvProcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIoDrvProcState.setStatus("mandatory")
_CpqIoDrvProcRAM_Type = Counter32
_CpqIoDrvProcRAM_Object = MibTableColumn
cpqIoDrvProcRAM = _CpqIoDrvProcRAM_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 6, 1, 1, 4),
    _CpqIoDrvProcRAM_Type()
)
cpqIoDrvProcRAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIoDrvProcRAM.setStatus("mandatory")


class _CpqIoDrvProcCPU_Type(Integer32):
    """Custom type cpqIoDrvProcCPU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CpqIoDrvProcCPU_Type.__name__ = "Integer32"
_CpqIoDrvProcCPU_Object = MibTableColumn
cpqIoDrvProcCPU = _CpqIoDrvProcCPU_Object(
    (1, 3, 6, 1, 4, 1, 232, 172, 2, 6, 1, 1, 5),
    _CpqIoDrvProcCPU_Type()
)
cpqIoDrvProcCPU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpqIoDrvProcCPU.setStatus("mandatory")

# Managed Objects groups


# Notification objects

cpqIoDrvWearoutTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 172001)
)
cpqIoDrvWearoutTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQIODRV-MIB", "cpqIoDrvInfoWearoutIndicator"),
        ("CPQIODRV-MIB", "cpqIoDrvInfoIndex"),
        ("CPQIODRV-MIB", "cpqIoDrvInfoName"),
        ("CPQIODRV-MIB", "cpqIoDrvInfoFirmwareVersion"),
        ("CPQIODRV-MIB", "cpqIoDrvInfoSparesPartNumber"),
        ("CPQIODRV-MIB", "cpqIoDrvInfoSerialNumber"),
        ("CPQIODRV-MIB", "cpqIoDrvInfoPCISlot"))
)
if mibBuilder.loadTexts:
    cpqIoDrvWearoutTrap.setStatus(
        ""
    )

cpqIoDrvNonWritableTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 172002)
)
cpqIoDrvNonWritableTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQIODRV-MIB", "cpqIoDrvInfoNonWritableIndicator"),
        ("CPQIODRV-MIB", "cpqIoDrvInfoIndex"),
        ("CPQIODRV-MIB", "cpqIoDrvInfoName"),
        ("CPQIODRV-MIB", "cpqIoDrvInfoFirmwareVersion"),
        ("CPQIODRV-MIB", "cpqIoDrvInfoSparesPartNumber"),
        ("CPQIODRV-MIB", "cpqIoDrvInfoSerialNumber"),
        ("CPQIODRV-MIB", "cpqIoDrvInfoPCISlot"))
)
if mibBuilder.loadTexts:
    cpqIoDrvNonWritableTrap.setStatus(
        ""
    )

cpqIoDrvFlashbackTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 172003)
)
cpqIoDrvFlashbackTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQIODRV-MIB", "cpqIoDrvInfoFlashbackIndicator"),
        ("CPQIODRV-MIB", "cpqIoDrvInfoIndex"),
        ("CPQIODRV-MIB", "cpqIoDrvInfoName"),
        ("CPQIODRV-MIB", "cpqIoDrvInfoFirmwareVersion"),
        ("CPQIODRV-MIB", "cpqIoDrvInfoSparesPartNumber"),
        ("CPQIODRV-MIB", "cpqIoDrvInfoSerialNumber"),
        ("CPQIODRV-MIB", "cpqIoDrvInfoPCISlot"))
)
if mibBuilder.loadTexts:
    cpqIoDrvFlashbackTrap.setStatus(
        ""
    )

cpqIoDrvTempHighTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 172004)
)
cpqIoDrvTempHighTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQIODRV-MIB", "cpqIoDrvInfoCurrentTemp"),
        ("CPQIODRV-MIB", "cpqIoDrvInfoIndex"),
        ("CPQIODRV-MIB", "cpqIoDrvInfoName"),
        ("CPQIODRV-MIB", "cpqIoDrvInfoFirmwareVersion"),
        ("CPQIODRV-MIB", "cpqIoDrvInfoSparesPartNumber"),
        ("CPQIODRV-MIB", "cpqIoDrvInfoSerialNumber"),
        ("CPQIODRV-MIB", "cpqIoDrvInfoPCISlot"))
)
if mibBuilder.loadTexts:
    cpqIoDrvTempHighTrap.setStatus(
        ""
    )

cpqIoDrvTempOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 172005)
)
cpqIoDrvTempOkTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQIODRV-MIB", "cpqIoDrvInfoCurrentTemp"),
        ("CPQIODRV-MIB", "cpqIoDrvInfoIndex"),
        ("CPQIODRV-MIB", "cpqIoDrvInfoName"),
        ("CPQIODRV-MIB", "cpqIoDrvInfoFirmwareVersion"),
        ("CPQIODRV-MIB", "cpqIoDrvInfoSparesPartNumber"),
        ("CPQIODRV-MIB", "cpqIoDrvInfoSerialNumber"),
        ("CPQIODRV-MIB", "cpqIoDrvInfoPCISlot"))
)
if mibBuilder.loadTexts:
    cpqIoDrvTempOkTrap.setStatus(
        ""
    )

cpqIoDrvErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 232, 0, 172006)
)
cpqIoDrvErrorTrap.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("CPQHOST-MIB", "cpqHoTrapFlags"),
        ("CPQIODRV-MIB", "cpqIoDrvInfoState"),
        ("CPQIODRV-MIB", "cpqIoDrvInfoIndex"),
        ("CPQIODRV-MIB", "cpqIoDrvInfoName"),
        ("CPQIODRV-MIB", "cpqIoDrvInfoFirmwareVersion"),
        ("CPQIODRV-MIB", "cpqIoDrvInfoSparesPartNumber"),
        ("CPQIODRV-MIB", "cpqIoDrvInfoSerialNumber"),
        ("CPQIODRV-MIB", "cpqIoDrvInfoPCISlot"))
)
if mibBuilder.loadTexts:
    cpqIoDrvErrorTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CPQIODRV-MIB",
    **{"cpqIoDrvWearoutTrap": cpqIoDrvWearoutTrap,
       "cpqIoDrvNonWritableTrap": cpqIoDrvNonWritableTrap,
       "cpqIoDrvFlashbackTrap": cpqIoDrvFlashbackTrap,
       "cpqIoDrvTempHighTrap": cpqIoDrvTempHighTrap,
       "cpqIoDrvTempOkTrap": cpqIoDrvTempOkTrap,
       "cpqIoDrvErrorTrap": cpqIoDrvErrorTrap,
       "cpqIoDrv": cpqIoDrv,
       "cpqIoDrvMibRev": cpqIoDrvMibRev,
       "cpqIoDrvMibRevMajor": cpqIoDrvMibRevMajor,
       "cpqIoDrvMibRevMinor": cpqIoDrvMibRevMinor,
       "cpqIoDrvMibCondition": cpqIoDrvMibCondition,
       "cpqIoDrvComponent": cpqIoDrvComponent,
       "cpqIoDrvInfo": cpqIoDrvInfo,
       "cpqIoDrvInfoTable": cpqIoDrvInfoTable,
       "cpqIoDrvInfoEntry": cpqIoDrvInfoEntry,
       "cpqIoDrvInfoIndex": cpqIoDrvInfoIndex,
       "cpqIoDrvInfoStatus": cpqIoDrvInfoStatus,
       "cpqIoDrvInfoName": cpqIoDrvInfoName,
       "cpqIoDrvInfoSerialNumber": cpqIoDrvInfoSerialNumber,
       "cpqIoDrvInfoPartNumber": cpqIoDrvInfoPartNumber,
       "cpqIoDrvInfoSubVendorPartNumber": cpqIoDrvInfoSubVendorPartNumber,
       "cpqIoDrvInfoSparesPartNumber": cpqIoDrvInfoSparesPartNumber,
       "cpqIoDrvInfoAssemblyNumber": cpqIoDrvInfoAssemblyNumber,
       "cpqIoDrvInfoFirmwareVersion": cpqIoDrvInfoFirmwareVersion,
       "cpqIoDrvInfoDriverVersion": cpqIoDrvInfoDriverVersion,
       "cpqIoDrvInfoUID": cpqIoDrvInfoUID,
       "cpqIoDrvInfoState": cpqIoDrvInfoState,
       "cpqIoDrvInfoClientDeviceName": cpqIoDrvInfoClientDeviceName,
       "cpqIoDrvInfoBeacon": cpqIoDrvInfoBeacon,
       "cpqIoDrvInfoPCIAddress": cpqIoDrvInfoPCIAddress,
       "cpqIoDrvInfoPCIDeviceID": cpqIoDrvInfoPCIDeviceID,
       "cpqIoDrvInfoPCISubdeviceID": cpqIoDrvInfoPCISubdeviceID,
       "cpqIoDrvInfoPCIVendorID": cpqIoDrvInfoPCIVendorID,
       "cpqIoDrvInfoPCISubvendorID": cpqIoDrvInfoPCISubvendorID,
       "cpqIoDrvInfoPCISlot": cpqIoDrvInfoPCISlot,
       "cpqIoDrvInfoWearoutIndicator": cpqIoDrvInfoWearoutIndicator,
       "cpqIoDrvInfoFlashbackIndicator": cpqIoDrvInfoFlashbackIndicator,
       "cpqIoDrvInfoNonWritableIndicator": cpqIoDrvInfoNonWritableIndicator,
       "cpqIoDrvInfoCurrentTemp": cpqIoDrvInfoCurrentTemp,
       "cpqIoDrvInfoPercentLifeRemaining": cpqIoDrvInfoPercentLifeRemaining,
       "cpqIoDrvInfoShortTermWearoutDate": cpqIoDrvInfoShortTermWearoutDate,
       "cpqIoDrvInfoLongTermWearoutDate": cpqIoDrvInfoLongTermWearoutDate,
       "cpqIoDrvInfoShortTermNonWritableDate": cpqIoDrvInfoShortTermNonWritableDate,
       "cpqIoDrvInfoLongTermNonWritableDate": cpqIoDrvInfoLongTermNonWritableDate,
       "cpqIoDrvExtn": cpqIoDrvExtn,
       "cpqIoDrvExtnTable": cpqIoDrvExtnTable,
       "cpqIoDrvExtnEntry": cpqIoDrvExtnEntry,
       "cpqIoDrvExtnIndex": cpqIoDrvExtnIndex,
       "cpqIoDrvExtnTotalPhysicalCapacityU": cpqIoDrvExtnTotalPhysicalCapacityU,
       "cpqIoDrvExtnTotalPhysicalCapacityL": cpqIoDrvExtnTotalPhysicalCapacityL,
       "cpqIoDrvExtnUsablePhysicalCapacityU": cpqIoDrvExtnUsablePhysicalCapacityU,
       "cpqIoDrvExtnUsablePhysicalCapacityL": cpqIoDrvExtnUsablePhysicalCapacityL,
       "cpqIoDrvExtnUsedPhysicalCapacityU": cpqIoDrvExtnUsedPhysicalCapacityU,
       "cpqIoDrvExtnUsedPhysicalCapacityL": cpqIoDrvExtnUsedPhysicalCapacityL,
       "cpqIoDrvExtnTotalLogicalCapacityU": cpqIoDrvExtnTotalLogicalCapacityU,
       "cpqIoDrvExtnTotalLogicalCapacityL": cpqIoDrvExtnTotalLogicalCapacityL,
       "cpqIoDrvExtnAvailableLogicalCapacityU": cpqIoDrvExtnAvailableLogicalCapacityU,
       "cpqIoDrvExtnAvailableLogicalCapacityL": cpqIoDrvExtnAvailableLogicalCapacityL,
       "cpqIoDrvExtnBytesReadU": cpqIoDrvExtnBytesReadU,
       "cpqIoDrvExtnBytesReadL": cpqIoDrvExtnBytesReadL,
       "cpqIoDrvExtnPhysicalBytesWrittenU": cpqIoDrvExtnPhysicalBytesWrittenU,
       "cpqIoDrvExtnPhysicalBytesWrittenL": cpqIoDrvExtnPhysicalBytesWrittenL,
       "cpqIoDrvExtnLogicalBytesWrittenU": cpqIoDrvExtnLogicalBytesWrittenU,
       "cpqIoDrvExtnLogicalBytesWrittenL": cpqIoDrvExtnLogicalBytesWrittenL,
       "cpqIoDrvExtnShortTermStartDate": cpqIoDrvExtnShortTermStartDate,
       "cpqIoDrvExtnShortTermWindow": cpqIoDrvExtnShortTermWindow,
       "cpqIoDrvExtnShortTermEndDate": cpqIoDrvExtnShortTermEndDate,
       "cpqIoDrvExtnShortTermEndDateFloat": cpqIoDrvExtnShortTermEndDateFloat,
       "cpqIoDrvExtnLongTermStartDate": cpqIoDrvExtnLongTermStartDate,
       "cpqIoDrvExtnLongTermWindow": cpqIoDrvExtnLongTermWindow,
       "cpqIoDrvExtnLongTermEndDate": cpqIoDrvExtnLongTermEndDate,
       "cpqIoDrvExtnLongTermEndDateFloat": cpqIoDrvExtnLongTermEndDateFloat,
       "cpqIoDrvExtnWriteRateAutoCalc": cpqIoDrvExtnWriteRateAutoCalc,
       "cpqIoDrvExtnShortTermAvgU": cpqIoDrvExtnShortTermAvgU,
       "cpqIoDrvExtnShortTermAvgL": cpqIoDrvExtnShortTermAvgL,
       "cpqIoDrvExtnLongTermAvgU": cpqIoDrvExtnLongTermAvgU,
       "cpqIoDrvExtnLongTermAvgL": cpqIoDrvExtnLongTermAvgL,
       "cpqIoDrvExtnConfidenceInterval": cpqIoDrvExtnConfidenceInterval,
       "cpqIoDrvCapacity": cpqIoDrvCapacity,
       "cpqIoDrvCapacityTable": cpqIoDrvCapacityTable,
       "cpqIoDrvCapacityEntry": cpqIoDrvCapacityEntry,
       "cpqIoDrvCapacityInfoIndex": cpqIoDrvCapacityInfoIndex,
       "cpqIoDrvCapacityIndex": cpqIoDrvCapacityIndex,
       "cpqIoDrvCapacityValueU": cpqIoDrvCapacityValueU,
       "cpqIoDrvCapacityValueL": cpqIoDrvCapacityValueL,
       "cpqIoDrvCapacityTimestamp": cpqIoDrvCapacityTimestamp,
       "cpqIoDrvWrite": cpqIoDrvWrite,
       "cpqIoDrvWriteTable": cpqIoDrvWriteTable,
       "cpqIoDrvWriteEntry": cpqIoDrvWriteEntry,
       "cpqIoDrvWriteInfoIndex": cpqIoDrvWriteInfoIndex,
       "cpqIoDrvWriteIndex": cpqIoDrvWriteIndex,
       "cpqIoDrvWriteValueU": cpqIoDrvWriteValueU,
       "cpqIoDrvWriteValueL": cpqIoDrvWriteValueL,
       "cpqIoDrvWriteTimestamp": cpqIoDrvWriteTimestamp,
       "cpqIoDrvTemp": cpqIoDrvTemp,
       "cpqIoDrvTempTable": cpqIoDrvTempTable,
       "cpqIoDrvTempEntry": cpqIoDrvTempEntry,
       "cpqIoDrvTempInfoIndex": cpqIoDrvTempInfoIndex,
       "cpqIoDrvTempIndex": cpqIoDrvTempIndex,
       "cpqIoDrvTempValue": cpqIoDrvTempValue,
       "cpqIoDrvTempTimestamp": cpqIoDrvTempTimestamp,
       "cpqIoDrvProc": cpqIoDrvProc,
       "cpqIoDrvProcTable": cpqIoDrvProcTable,
       "cpqIoDrvProcEntry": cpqIoDrvProcEntry,
       "cpqIoDrvProcIndex": cpqIoDrvProcIndex,
       "cpqIoDrvProcName": cpqIoDrvProcName,
       "cpqIoDrvProcState": cpqIoDrvProcState,
       "cpqIoDrvProcRAM": cpqIoDrvProcRAM,
       "cpqIoDrvProcCPU": cpqIoDrvProcCPU}
)
