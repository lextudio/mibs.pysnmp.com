# SNMP MIB module (EDS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EDS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:36:35 2024
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

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

edsProducts = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 31440, 1, 6)
)
edsProducts.setRevisions(
        ("2016-06-30 00:00",
         "1970-01-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EdsMain_ObjectIdentity = ObjectIdentity
edsMain = _EdsMain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31440)
)
_EdsEnterprise_ObjectIdentity = ObjectIdentity
edsEnterprise = _EdsEnterprise_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31440, 1)
)
_ECompanyName_Type = DisplayString
_ECompanyName_Object = MibScalar
eCompanyName = _ECompanyName_Object(
    (1, 3, 6, 1, 4, 1, 31440, 1, 1),
    _ECompanyName_Type()
)
eCompanyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eCompanyName.setStatus("current")
_EProductName_Type = DisplayString
_EProductName_Object = MibScalar
eProductName = _EProductName_Object(
    (1, 3, 6, 1, 4, 1, 31440, 1, 2),
    _EProductName_Type()
)
eProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eProductName.setStatus("current")
_EMIBVersion_Type = DisplayString
_EMIBVersion_Object = MibScalar
eMIBVersion = _EMIBVersion_Object(
    (1, 3, 6, 1, 4, 1, 31440, 1, 3),
    _EMIBVersion_Type()
)
eMIBVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eMIBVersion.setStatus("current")
_EFirmwareVersion_Type = DisplayString
_EFirmwareVersion_Object = MibScalar
eFirmwareVersion = _EFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 31440, 1, 4),
    _EFirmwareVersion_Type()
)
eFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eFirmwareVersion.setStatus("current")
_EFirmwareDate_Type = DisplayString
_EFirmwareDate_Object = MibScalar
eFirmwareDate = _EFirmwareDate_Object(
    (1, 3, 6, 1, 4, 1, 31440, 1, 5),
    _EFirmwareDate_Type()
)
eFirmwareDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eFirmwareDate.setStatus("current")
_DTrap_ObjectIdentity = ObjectIdentity
dTrap = _DTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31440, 2)
)
_DTrapTable_Object = MibTable
dTrapTable = _DTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 31440, 2, 1)
)
if mibBuilder.loadTexts:
    dTrapTable.setStatus("current")
_DTrapEntry_Object = MibTableRow
dTrapEntry = _DTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 31440, 2, 1, 1)
)
dTrapEntry.setIndexNames(
    (0, "EDS-MIB", "dTrapIndex"),
)
if mibBuilder.loadTexts:
    dTrapEntry.setStatus("current")


class _DTrapIndex_Type(Integer32):
    """Custom type dTrapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_DTrapIndex_Type.__name__ = "Integer32"
_DTrapIndex_Object = MibTableColumn
dTrapIndex = _DTrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 31440, 2, 1, 1, 1),
    _DTrapIndex_Type()
)
dTrapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dTrapIndex.setStatus("current")


class _DTrapEnable_Type(Integer32):
    """Custom type dTrapEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_DTrapEnable_Type.__name__ = "Integer32"
_DTrapEnable_Object = MibTableColumn
dTrapEnable = _DTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 31440, 2, 1, 1, 2),
    _DTrapEnable_Type()
)
dTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dTrapEnable.setStatus("current")
_DTrapIP_Type = IpAddress
_DTrapIP_Object = MibTableColumn
dTrapIP = _DTrapIP_Object(
    (1, 3, 6, 1, 4, 1, 31440, 2, 1, 1, 3),
    _DTrapIP_Type()
)
dTrapIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dTrapIP.setStatus("current")
_DTrapCommunity_Type = DisplayString
_DTrapCommunity_Object = MibTableColumn
dTrapCommunity = _DTrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 31440, 2, 1, 1, 4),
    _DTrapCommunity_Type()
)
dTrapCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dTrapCommunity.setStatus("current")
_DTrapDeviceTable_Object = MibTable
dTrapDeviceTable = _DTrapDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 31440, 2, 2)
)
if mibBuilder.loadTexts:
    dTrapDeviceTable.setStatus("current")
_DTrapDeviceEntry_Object = MibTableRow
dTrapDeviceEntry = _DTrapDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 31440, 2, 2, 1)
)
dTrapDeviceEntry.setIndexNames(
    (0, "EDS-MIB", "dTrapDeviceIndex"),
)
if mibBuilder.loadTexts:
    dTrapDeviceEntry.setStatus("current")


class _DTrapDeviceIndex_Type(Integer32):
    """Custom type dTrapDeviceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_DTrapDeviceIndex_Type.__name__ = "Integer32"
_DTrapDeviceIndex_Object = MibTableColumn
dTrapDeviceIndex = _DTrapDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 31440, 2, 2, 1, 1),
    _DTrapDeviceIndex_Type()
)
dTrapDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dTrapDeviceIndex.setStatus("current")


class _DTrapDeviceEnable_Type(Integer32):
    """Custom type dTrapDeviceEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_DTrapDeviceEnable_Type.__name__ = "Integer32"
_DTrapDeviceEnable_Object = MibTableColumn
dTrapDeviceEnable = _DTrapDeviceEnable_Object(
    (1, 3, 6, 1, 4, 1, 31440, 2, 2, 1, 2),
    _DTrapDeviceEnable_Type()
)
dTrapDeviceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dTrapDeviceEnable.setStatus("current")


class _DTrapDeviceSendPointer_Type(Integer32):
    """Custom type dTrapDeviceSendPointer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_DTrapDeviceSendPointer_Type.__name__ = "Integer32"
_DTrapDeviceSendPointer_Object = MibTableColumn
dTrapDeviceSendPointer = _DTrapDeviceSendPointer_Object(
    (1, 3, 6, 1, 4, 1, 31440, 2, 2, 1, 3),
    _DTrapDeviceSendPointer_Type()
)
dTrapDeviceSendPointer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dTrapDeviceSendPointer.setStatus("current")


class _DTrapDeviceROM_Type(DisplayString):
    """Custom type dTrapDeviceROM based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_DTrapDeviceROM_Type.__name__ = "DisplayString"
_DTrapDeviceROM_Object = MibTableColumn
dTrapDeviceROM = _DTrapDeviceROM_Object(
    (1, 3, 6, 1, 4, 1, 31440, 2, 2, 1, 4),
    _DTrapDeviceROM_Type()
)
dTrapDeviceROM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dTrapDeviceROM.setStatus("current")


class _DTrapDeviceVariable_Type(Integer32):
    """Custom type dTrapDeviceVariable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_DTrapDeviceVariable_Type.__name__ = "Integer32"
_DTrapDeviceVariable_Object = MibTableColumn
dTrapDeviceVariable = _DTrapDeviceVariable_Object(
    (1, 3, 6, 1, 4, 1, 31440, 2, 2, 1, 5),
    _DTrapDeviceVariable_Type()
)
dTrapDeviceVariable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dTrapDeviceVariable.setStatus("current")
_DTrapDeviceHighThreshold_Type = DisplayString
_DTrapDeviceHighThreshold_Object = MibTableColumn
dTrapDeviceHighThreshold = _DTrapDeviceHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 31440, 2, 2, 1, 6),
    _DTrapDeviceHighThreshold_Type()
)
dTrapDeviceHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dTrapDeviceHighThreshold.setStatus("current")
_DTrapDeviceLowThreshold_Type = DisplayString
_DTrapDeviceLowThreshold_Object = MibTableColumn
dTrapDeviceLowThreshold = _DTrapDeviceLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 31440, 2, 2, 1, 7),
    _DTrapDeviceLowThreshold_Type()
)
dTrapDeviceLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dTrapDeviceLowThreshold.setStatus("current")
_DTrapDeviceHysteresis_Type = DisplayString
_DTrapDeviceHysteresis_Object = MibTableColumn
dTrapDeviceHysteresis = _DTrapDeviceHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 31440, 2, 2, 1, 8),
    _DTrapDeviceHysteresis_Type()
)
dTrapDeviceHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dTrapDeviceHysteresis.setStatus("current")
_WTrap_ObjectIdentity = ObjectIdentity
wTrap = _WTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31440, 3)
)
_WTrapTable_Object = MibTable
wTrapTable = _WTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 31440, 3, 1)
)
if mibBuilder.loadTexts:
    wTrapTable.setStatus("current")
_WTrapEntry_Object = MibTableRow
wTrapEntry = _WTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 31440, 3, 1, 1)
)
wTrapEntry.setIndexNames(
    (0, "EDS-MIB", "wTrapIndex"),
)
if mibBuilder.loadTexts:
    wTrapEntry.setStatus("current")


class _WTrapIndex_Type(Integer32):
    """Custom type wTrapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WTrapIndex_Type.__name__ = "Integer32"
_WTrapIndex_Object = MibTableColumn
wTrapIndex = _WTrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 31440, 3, 1, 1, 1),
    _WTrapIndex_Type()
)
wTrapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wTrapIndex.setStatus("current")
_WTrapIP_Type = IpAddress
_WTrapIP_Object = MibTableColumn
wTrapIP = _WTrapIP_Object(
    (1, 3, 6, 1, 4, 1, 31440, 3, 1, 1, 2),
    _WTrapIP_Type()
)
wTrapIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wTrapIP.setStatus("current")
_WTrapCommunity_Type = DisplayString
_WTrapCommunity_Object = MibTableColumn
wTrapCommunity = _WTrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 31440, 3, 1, 1, 3),
    _WTrapCommunity_Type()
)
wTrapCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wTrapCommunity.setStatus("current")


class _WTrapEUI_Type(DisplayString):
    """Custom type wTrapEUI based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_WTrapEUI_Type.__name__ = "DisplayString"
_WTrapEUI_Object = MibTableColumn
wTrapEUI = _WTrapEUI_Object(
    (1, 3, 6, 1, 4, 1, 31440, 3, 1, 1, 4),
    _WTrapEUI_Type()
)
wTrapEUI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wTrapEUI.setStatus("current")
_WTrapVariable_Type = DisplayString
_WTrapVariable_Object = MibTableColumn
wTrapVariable = _WTrapVariable_Object(
    (1, 3, 6, 1, 4, 1, 31440, 3, 1, 1, 5),
    _WTrapVariable_Type()
)
wTrapVariable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wTrapVariable.setStatus("current")
_WTrapHighThreshold_Type = DisplayString
_WTrapHighThreshold_Object = MibTableColumn
wTrapHighThreshold = _WTrapHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 31440, 3, 1, 1, 6),
    _WTrapHighThreshold_Type()
)
wTrapHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wTrapHighThreshold.setStatus("current")
_WTrapLowThreshold_Type = DisplayString
_WTrapLowThreshold_Object = MibTableColumn
wTrapLowThreshold = _WTrapLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 31440, 3, 1, 1, 7),
    _WTrapLowThreshold_Type()
)
wTrapLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wTrapLowThreshold.setStatus("current")
_OwDevices_ObjectIdentity = ObjectIdentity
owDevices = _OwDevices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31440, 10)
)
_OwDeviceTypes_ObjectIdentity = ObjectIdentity
owDeviceTypes = _OwDeviceTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31440, 10, 1)
)
_OwNone_ObjectIdentity = ObjectIdentity
owNone = _OwNone_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31440, 10, 1, 0)
)
_OwUnknown_ObjectIdentity = ObjectIdentity
owUnknown = _OwUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31440, 10, 1, 1)
)
_OwDS2406_ObjectIdentity = ObjectIdentity
owDS2406 = _OwDS2406_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31440, 10, 1, 2)
)
_OwDS18B20_ObjectIdentity = ObjectIdentity
owDS18B20 = _OwDS18B20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31440, 10, 1, 3)
)
_OwDS18S20_ObjectIdentity = ObjectIdentity
owDS18S20 = _OwDS18S20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31440, 10, 1, 4)
)
_OwDS2438_ObjectIdentity = ObjectIdentity
owDS2438 = _OwDS2438_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31440, 10, 1, 5)
)
_OwDS2423_ObjectIdentity = ObjectIdentity
owDS2423 = _OwDS2423_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31440, 10, 1, 6)
)
_OwDS2408_ObjectIdentity = ObjectIdentity
owDS2408 = _OwDS2408_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31440, 10, 1, 7)
)
_OwDS2450_ObjectIdentity = ObjectIdentity
owDS2450 = _OwDS2450_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31440, 10, 1, 8)
)
_OwEDS0064_ObjectIdentity = ObjectIdentity
owEDS0064 = _OwEDS0064_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31440, 10, 1, 9)
)
_OwEDS0065_ObjectIdentity = ObjectIdentity
owEDS0065 = _OwEDS0065_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31440, 10, 1, 10)
)
_OwEDS0066_ObjectIdentity = ObjectIdentity
owEDS0066 = _OwEDS0066_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31440, 10, 1, 11)
)
_OwEDS0067_ObjectIdentity = ObjectIdentity
owEDS0067 = _OwEDS0067_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31440, 10, 1, 12)
)
_OwEDS0068_ObjectIdentity = ObjectIdentity
owEDS0068 = _OwEDS0068_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31440, 10, 1, 13)
)
_OwEDS0069_ObjectIdentity = ObjectIdentity
owEDS0069 = _OwEDS0069_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31440, 10, 1, 14)
)
_OwEDS0070_ObjectIdentity = ObjectIdentity
owEDS0070 = _OwEDS0070_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31440, 10, 1, 15)
)
_OwEDS0071_ObjectIdentity = ObjectIdentity
owEDS0071 = _OwEDS0071_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31440, 10, 1, 16)
)
_OwEDS0080_ObjectIdentity = ObjectIdentity
owEDS0080 = _OwEDS0080_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31440, 10, 1, 17)
)
_OwEDS0082_ObjectIdentity = ObjectIdentity
owEDS0082 = _OwEDS0082_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31440, 10, 1, 18)
)
_OwEDS0083_ObjectIdentity = ObjectIdentity
owEDS0083 = _OwEDS0083_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31440, 10, 1, 19)
)
_OwEDS0085_ObjectIdentity = ObjectIdentity
owEDS0085 = _OwEDS0085_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31440, 10, 1, 20)
)
_OwEDS0090_ObjectIdentity = ObjectIdentity
owEDS0090 = _OwEDS0090_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31440, 10, 1, 21)
)
_OwEDS0091_ObjectIdentity = ObjectIdentity
owEDS0091 = _OwEDS0091_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31440, 10, 1, 22)
)
_OwEDS0092_ObjectIdentity = ObjectIdentity
owEDS0092 = _OwEDS0092_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31440, 10, 1, 23)
)
_OwDS28EA00_ObjectIdentity = ObjectIdentity
owDS28EA00 = _OwDS28EA00_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31440, 10, 1, 24)
)
_OwEDS0050_ObjectIdentity = ObjectIdentity
owEDS0050 = _OwEDS0050_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31440, 10, 1, 25)
)
_OwEDS0001_ObjectIdentity = ObjectIdentity
owEDS0001 = _OwEDS0001_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31440, 10, 1, 26)
)
_OwDeviceInfo_ObjectIdentity = ObjectIdentity
owDeviceInfo = _OwDeviceInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31440, 10, 2)
)
_OwDeviceNumActive_Type = Integer32
_OwDeviceNumActive_Object = MibScalar
owDeviceNumActive = _OwDeviceNumActive_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 2, 1),
    _OwDeviceNumActive_Type()
)
owDeviceNumActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owDeviceNumActive.setStatus("current")
_OwDeviceTable_Object = MibTable
owDeviceTable = _OwDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 3)
)
if mibBuilder.loadTexts:
    owDeviceTable.setStatus("current")
_OwDeviceEntry_Object = MibTableRow
owDeviceEntry = _OwDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 3, 1)
)
owDeviceEntry.setIndexNames(
    (0, "EDS-MIB", "owDeviceIndex"),
)
if mibBuilder.loadTexts:
    owDeviceEntry.setStatus("current")


class _OwDeviceIndex_Type(Integer32):
    """Custom type owDeviceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_OwDeviceIndex_Type.__name__ = "Integer32"
_OwDeviceIndex_Object = MibTableColumn
owDeviceIndex = _OwDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 3, 1, 1),
    _OwDeviceIndex_Type()
)
owDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owDeviceIndex.setStatus("current")


class _OwDeviceType_Type(Integer32):
    """Custom type owDeviceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_OwDeviceType_Type.__name__ = "Integer32"
_OwDeviceType_Object = MibTableColumn
owDeviceType = _OwDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 3, 1, 2),
    _OwDeviceType_Type()
)
owDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owDeviceType.setStatus("current")
_OwDeviceName_Type = DisplayString
_OwDeviceName_Object = MibTableColumn
owDeviceName = _OwDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 3, 1, 3),
    _OwDeviceName_Type()
)
owDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owDeviceName.setStatus("current")
_OwDeviceDescription_Type = DisplayString
_OwDeviceDescription_Object = MibTableColumn
owDeviceDescription = _OwDeviceDescription_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 3, 1, 4),
    _OwDeviceDescription_Type()
)
owDeviceDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owDeviceDescription.setStatus("current")


class _OwDeviceFamily_Type(OctetString):
    """Custom type owDeviceFamily based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_OwDeviceFamily_Type.__name__ = "OctetString"
_OwDeviceFamily_Object = MibTableColumn
owDeviceFamily = _OwDeviceFamily_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 3, 1, 5),
    _OwDeviceFamily_Type()
)
owDeviceFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owDeviceFamily.setStatus("current")


class _OwDeviceROM_Type(OctetString):
    """Custom type owDeviceROM based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_OwDeviceROM_Type.__name__ = "OctetString"
_OwDeviceROM_Object = MibTableColumn
owDeviceROM = _OwDeviceROM_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 3, 1, 6),
    _OwDeviceROM_Type()
)
owDeviceROM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owDeviceROM.setStatus("current")


class _OwDeviceHealth_Type(Integer32):
    """Custom type owDeviceHealth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_OwDeviceHealth_Type.__name__ = "Integer32"
_OwDeviceHealth_Object = MibTableColumn
owDeviceHealth = _OwDeviceHealth_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 3, 1, 7),
    _OwDeviceHealth_Type()
)
owDeviceHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owDeviceHealth.setStatus("current")
_OwDS2406Table_Object = MibTable
owDS2406Table = _OwDS2406Table_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 4)
)
if mibBuilder.loadTexts:
    owDS2406Table.setStatus("current")
_OwDS2406Entry_Object = MibTableRow
owDS2406Entry = _OwDS2406Entry_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 4, 1)
)
owDS2406Entry.setIndexNames(
    (0, "EDS-MIB", "owDeviceIndex"),
)
if mibBuilder.loadTexts:
    owDS2406Entry.setStatus("current")


class _OwDS2406PIOALevel_Type(Integer32):
    """Custom type owDS2406PIOALevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 0))
    )


_OwDS2406PIOALevel_Type.__name__ = "Integer32"
_OwDS2406PIOALevel_Object = MibTableColumn
owDS2406PIOALevel = _OwDS2406PIOALevel_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 4, 1, 1),
    _OwDS2406PIOALevel_Type()
)
owDS2406PIOALevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owDS2406PIOALevel.setStatus("current")


class _OwDS2406PIOBLevel_Type(Integer32):
    """Custom type owDS2406PIOBLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 0))
    )


_OwDS2406PIOBLevel_Type.__name__ = "Integer32"
_OwDS2406PIOBLevel_Object = MibTableColumn
owDS2406PIOBLevel = _OwDS2406PIOBLevel_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 4, 1, 2),
    _OwDS2406PIOBLevel_Type()
)
owDS2406PIOBLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owDS2406PIOBLevel.setStatus("current")


class _OwDS2406PIOAFlipFlop_Type(Integer32):
    """Custom type owDS2406PIOAFlipFlop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 0))
    )


_OwDS2406PIOAFlipFlop_Type.__name__ = "Integer32"
_OwDS2406PIOAFlipFlop_Object = MibTableColumn
owDS2406PIOAFlipFlop = _OwDS2406PIOAFlipFlop_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 4, 1, 3),
    _OwDS2406PIOAFlipFlop_Type()
)
owDS2406PIOAFlipFlop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    owDS2406PIOAFlipFlop.setStatus("current")


class _OwDS2406PIOBFlipFlop_Type(Integer32):
    """Custom type owDS2406PIOBFlipFlop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 0))
    )


_OwDS2406PIOBFlipFlop_Type.__name__ = "Integer32"
_OwDS2406PIOBFlipFlop_Object = MibTableColumn
owDS2406PIOBFlipFlop = _OwDS2406PIOBFlipFlop_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 4, 1, 4),
    _OwDS2406PIOBFlipFlop_Type()
)
owDS2406PIOBFlipFlop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    owDS2406PIOBFlipFlop.setStatus("current")


class _OwDS2406PIOAActivityLatch_Type(Integer32):
    """Custom type owDS2406PIOAActivityLatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noActivity", 0),
          ("yesActivity", 1))
    )


_OwDS2406PIOAActivityLatch_Type.__name__ = "Integer32"
_OwDS2406PIOAActivityLatch_Object = MibTableColumn
owDS2406PIOAActivityLatch = _OwDS2406PIOAActivityLatch_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 4, 1, 5),
    _OwDS2406PIOAActivityLatch_Type()
)
owDS2406PIOAActivityLatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owDS2406PIOAActivityLatch.setStatus("current")


class _OwDS2406PIOBActivityLatch_Type(Integer32):
    """Custom type owDS2406PIOBActivityLatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noActivity", 0),
          ("yesActivity", 1))
    )


_OwDS2406PIOBActivityLatch_Type.__name__ = "Integer32"
_OwDS2406PIOBActivityLatch_Object = MibTableColumn
owDS2406PIOBActivityLatch = _OwDS2406PIOBActivityLatch_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 4, 1, 6),
    _OwDS2406PIOBActivityLatch_Type()
)
owDS2406PIOBActivityLatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owDS2406PIOBActivityLatch.setStatus("current")


class _OwDS2406NumChnls_Type(Integer32):
    """Custom type owDS2406NumChnls based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("pioAandB", 1),
          ("pioAonly", 0))
    )


_OwDS2406NumChnls_Type.__name__ = "Integer32"
_OwDS2406NumChnls_Object = MibTableColumn
owDS2406NumChnls = _OwDS2406NumChnls_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 4, 1, 7),
    _OwDS2406NumChnls_Type()
)
owDS2406NumChnls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owDS2406NumChnls.setStatus("current")


class _OwDS2406PwrSupply_Type(Integer32):
    """Custom type owDS2406PwrSupply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("pwrExternal", 1),
          ("pwrParasite", 0))
    )


_OwDS2406PwrSupply_Type.__name__ = "Integer32"
_OwDS2406PwrSupply_Object = MibTableColumn
owDS2406PwrSupply = _OwDS2406PwrSupply_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 4, 1, 8),
    _OwDS2406PwrSupply_Type()
)
owDS2406PwrSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owDS2406PwrSupply.setStatus("current")


class _OwDS2406ActivityLatchReset_Type(Integer32):
    """Custom type owDS2406ActivityLatchReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noReset", 0),
          ("yesReset", 1))
    )


_OwDS2406ActivityLatchReset_Type.__name__ = "Integer32"
_OwDS2406ActivityLatchReset_Object = MibTableColumn
owDS2406ActivityLatchReset = _OwDS2406ActivityLatchReset_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 4, 1, 9),
    _OwDS2406ActivityLatchReset_Type()
)
owDS2406ActivityLatchReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    owDS2406ActivityLatchReset.setStatus("current")
_OwDS18B20Table_Object = MibTable
owDS18B20Table = _OwDS18B20Table_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 5)
)
if mibBuilder.loadTexts:
    owDS18B20Table.setStatus("current")
_OwDS18B20Entry_Object = MibTableRow
owDS18B20Entry = _OwDS18B20Entry_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 5, 1)
)
owDS18B20Entry.setIndexNames(
    (0, "EDS-MIB", "owDeviceIndex"),
)
if mibBuilder.loadTexts:
    owDS18B20Entry.setStatus("current")
_OwDS18B20Temperature_Type = DisplayString
_OwDS18B20Temperature_Object = MibTableColumn
owDS18B20Temperature = _OwDS18B20Temperature_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 5, 1, 1),
    _OwDS18B20Temperature_Type()
)
owDS18B20Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owDS18B20Temperature.setStatus("current")
_OwDS18B20UserByte1_Type = Integer32
_OwDS18B20UserByte1_Object = MibTableColumn
owDS18B20UserByte1 = _OwDS18B20UserByte1_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 5, 1, 2),
    _OwDS18B20UserByte1_Type()
)
owDS18B20UserByte1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    owDS18B20UserByte1.setStatus("current")
_OwDS18B20UserByte2_Type = Integer32
_OwDS18B20UserByte2_Object = MibTableColumn
owDS18B20UserByte2 = _OwDS18B20UserByte2_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 5, 1, 3),
    _OwDS18B20UserByte2_Type()
)
owDS18B20UserByte2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    owDS18B20UserByte2.setStatus("current")


class _OwDS18B20Resolution_Type(Integer32):
    """Custom type owDS18B20Resolution based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("elevenBits", 11),
          ("nineBits", 9),
          ("tenBits", 10),
          ("twelveBits", 12))
    )


_OwDS18B20Resolution_Type.__name__ = "Integer32"
_OwDS18B20Resolution_Object = MibTableColumn
owDS18B20Resolution = _OwDS18B20Resolution_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 5, 1, 4),
    _OwDS18B20Resolution_Type()
)
owDS18B20Resolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owDS18B20Resolution.setStatus("current")


class _OwDS18B20PwrSupply_Type(Integer32):
    """Custom type owDS18B20PwrSupply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              255)
        )
    )
    namedValues = NamedValues(
        *(("externalPower", 255),
          ("parasitePower", 0))
    )


_OwDS18B20PwrSupply_Type.__name__ = "Integer32"
_OwDS18B20PwrSupply_Object = MibTableColumn
owDS18B20PwrSupply = _OwDS18B20PwrSupply_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 5, 1, 5),
    _OwDS18B20PwrSupply_Type()
)
owDS18B20PwrSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owDS18B20PwrSupply.setStatus("current")
_OwDS18S20Table_Object = MibTable
owDS18S20Table = _OwDS18S20Table_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 6)
)
if mibBuilder.loadTexts:
    owDS18S20Table.setStatus("current")
_OwDS18S20Entry_Object = MibTableRow
owDS18S20Entry = _OwDS18S20Entry_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 6, 1)
)
owDS18S20Entry.setIndexNames(
    (0, "EDS-MIB", "owDeviceIndex"),
)
if mibBuilder.loadTexts:
    owDS18S20Entry.setStatus("current")
_OwDS18S20Temperature_Type = DisplayString
_OwDS18S20Temperature_Object = MibTableColumn
owDS18S20Temperature = _OwDS18S20Temperature_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 6, 1, 1),
    _OwDS18S20Temperature_Type()
)
owDS18S20Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owDS18S20Temperature.setStatus("current")


class _OwDS18S20UserByte1_Type(Integer32):
    """Custom type owDS18S20UserByte1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_OwDS18S20UserByte1_Type.__name__ = "Integer32"
_OwDS18S20UserByte1_Object = MibTableColumn
owDS18S20UserByte1 = _OwDS18S20UserByte1_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 6, 1, 2),
    _OwDS18S20UserByte1_Type()
)
owDS18S20UserByte1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owDS18S20UserByte1.setStatus("current")


class _OwDS18S20UserByte2_Type(Integer32):
    """Custom type owDS18S20UserByte2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_OwDS18S20UserByte2_Type.__name__ = "Integer32"
_OwDS18S20UserByte2_Object = MibTableColumn
owDS18S20UserByte2 = _OwDS18S20UserByte2_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 6, 1, 3),
    _OwDS18S20UserByte2_Type()
)
owDS18S20UserByte2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owDS18S20UserByte2.setStatus("current")
_OwDS2423Table_Object = MibTable
owDS2423Table = _OwDS2423Table_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 7)
)
if mibBuilder.loadTexts:
    owDS2423Table.setStatus("current")
_OwDS2423Entry_Object = MibTableRow
owDS2423Entry = _OwDS2423Entry_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 7, 1)
)
owDS2423Entry.setIndexNames(
    (0, "EDS-MIB", "owDeviceIndex"),
)
if mibBuilder.loadTexts:
    owDS2423Entry.setStatus("current")
_OwDS2423CounterA_Type = Counter32
_OwDS2423CounterA_Object = MibTableColumn
owDS2423CounterA = _OwDS2423CounterA_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 7, 1, 1),
    _OwDS2423CounterA_Type()
)
owDS2423CounterA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owDS2423CounterA.setStatus("current")
_OwDS2423CounterB_Type = Counter32
_OwDS2423CounterB_Object = MibTableColumn
owDS2423CounterB = _OwDS2423CounterB_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 7, 1, 2),
    _OwDS2423CounterB_Type()
)
owDS2423CounterB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owDS2423CounterB.setStatus("current")
_OwDS2438Table_Object = MibTable
owDS2438Table = _OwDS2438Table_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 8)
)
if mibBuilder.loadTexts:
    owDS2438Table.setStatus("current")
_OwDS2438Entry_Object = MibTableRow
owDS2438Entry = _OwDS2438Entry_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 8, 1)
)
owDS2438Entry.setIndexNames(
    (0, "EDS-MIB", "owDeviceIndex"),
)
if mibBuilder.loadTexts:
    owDS2438Entry.setStatus("current")
_OwDS2438Temperature_Type = DisplayString
_OwDS2438Temperature_Object = MibTableColumn
owDS2438Temperature = _OwDS2438Temperature_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 8, 1, 1),
    _OwDS2438Temperature_Type()
)
owDS2438Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owDS2438Temperature.setStatus("current")
_OwDS2438SupplyVoltage_Type = DisplayString
_OwDS2438SupplyVoltage_Object = MibTableColumn
owDS2438SupplyVoltage = _OwDS2438SupplyVoltage_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 8, 1, 2),
    _OwDS2438SupplyVoltage_Type()
)
owDS2438SupplyVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owDS2438SupplyVoltage.setStatus("current")
_OwDS2438PinVoltage_Type = DisplayString
_OwDS2438PinVoltage_Object = MibTableColumn
owDS2438PinVoltage = _OwDS2438PinVoltage_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 8, 1, 3),
    _OwDS2438PinVoltage_Type()
)
owDS2438PinVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owDS2438PinVoltage.setStatus("current")
_OwDS2438current_Type = DisplayString
_OwDS2438current_Object = MibTableColumn
owDS2438current = _OwDS2438current_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 8, 1, 4),
    _OwDS2438current_Type()
)
owDS2438current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owDS2438current.setStatus("current")
_OwDS2438Humidity_Type = DisplayString
_OwDS2438Humidity_Object = MibTableColumn
owDS2438Humidity = _OwDS2438Humidity_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 8, 1, 5),
    _OwDS2438Humidity_Type()
)
owDS2438Humidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owDS2438Humidity.setStatus("current")
_OwDS2408Table_Object = MibTable
owDS2408Table = _OwDS2408Table_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 9)
)
if mibBuilder.loadTexts:
    owDS2408Table.setStatus("current")
_OwDS2408Entry_Object = MibTableRow
owDS2408Entry = _OwDS2408Entry_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 9, 1)
)
owDS2408Entry.setIndexNames(
    (0, "EDS-MIB", "owDeviceIndex"),
)
if mibBuilder.loadTexts:
    owDS2408Entry.setStatus("current")
_OwDS2408PIOLogicState_Type = Integer32
_OwDS2408PIOLogicState_Object = MibTableColumn
owDS2408PIOLogicState = _OwDS2408PIOLogicState_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 9, 1, 1),
    _OwDS2408PIOLogicState_Type()
)
owDS2408PIOLogicState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owDS2408PIOLogicState.setStatus("current")
_OwDS2408PIOOutputLatchState_Type = Integer32
_OwDS2408PIOOutputLatchState_Object = MibTableColumn
owDS2408PIOOutputLatchState = _OwDS2408PIOOutputLatchState_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 9, 1, 2),
    _OwDS2408PIOOutputLatchState_Type()
)
owDS2408PIOOutputLatchState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    owDS2408PIOOutputLatchState.setStatus("current")


class _OwDS2408PIOActivityLatchState_Type(Integer32):
    """Custom type owDS2408PIOActivityLatchState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              255)
        )
    )
    namedValues = NamedValues(
        *(("high", 255),
          ("low", 0))
    )


_OwDS2408PIOActivityLatchState_Type.__name__ = "Integer32"
_OwDS2408PIOActivityLatchState_Object = MibTableColumn
owDS2408PIOActivityLatchState = _OwDS2408PIOActivityLatchState_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 9, 1, 3),
    _OwDS2408PIOActivityLatchState_Type()
)
owDS2408PIOActivityLatchState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    owDS2408PIOActivityLatchState.setStatus("current")


class _OwDS2408RSTZConfiguration_Type(Integer32):
    """Custom type owDS2408RSTZConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 0))
    )


_OwDS2408RSTZConfiguration_Type.__name__ = "Integer32"
_OwDS2408RSTZConfiguration_Object = MibTableColumn
owDS2408RSTZConfiguration = _OwDS2408RSTZConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 9, 1, 4),
    _OwDS2408RSTZConfiguration_Type()
)
owDS2408RSTZConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    owDS2408RSTZConfiguration.setStatus("current")


class _OwDS2408PowerOnResetLatch_Type(Integer32):
    """Custom type owDS2408PowerOnResetLatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 0))
    )


_OwDS2408PowerOnResetLatch_Type.__name__ = "Integer32"
_OwDS2408PowerOnResetLatch_Object = MibTableColumn
owDS2408PowerOnResetLatch = _OwDS2408PowerOnResetLatch_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 9, 1, 5),
    _OwDS2408PowerOnResetLatch_Type()
)
owDS2408PowerOnResetLatch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    owDS2408PowerOnResetLatch.setStatus("current")


class _OwDS2408VCCPowerStatus_Type(Integer32):
    """Custom type owDS2408VCCPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 0))
    )


_OwDS2408VCCPowerStatus_Type.__name__ = "Integer32"
_OwDS2408VCCPowerStatus_Object = MibTableColumn
owDS2408VCCPowerStatus = _OwDS2408VCCPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 9, 1, 6),
    _OwDS2408VCCPowerStatus_Type()
)
owDS2408VCCPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owDS2408VCCPowerStatus.setStatus("current")
_OwDS2450Table_Object = MibTable
owDS2450Table = _OwDS2450Table_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 10)
)
if mibBuilder.loadTexts:
    owDS2450Table.setStatus("current")
_OwDS2450Entry_Object = MibTableRow
owDS2450Entry = _OwDS2450Entry_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 10, 1)
)
owDS2450Entry.setIndexNames(
    (0, "EDS-MIB", "owDeviceIndex"),
)
if mibBuilder.loadTexts:
    owDS2450Entry.setStatus("current")
_OwDS2450ChannelAConversionValue_Type = DisplayString
_OwDS2450ChannelAConversionValue_Object = MibTableColumn
owDS2450ChannelAConversionValue = _OwDS2450ChannelAConversionValue_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 10, 1, 1),
    _OwDS2450ChannelAConversionValue_Type()
)
owDS2450ChannelAConversionValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owDS2450ChannelAConversionValue.setStatus("current")
_OwDS2450ChannelAConversionResolution_Type = Integer32
_OwDS2450ChannelAConversionResolution_Object = MibTableColumn
owDS2450ChannelAConversionResolution = _OwDS2450ChannelAConversionResolution_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 10, 1, 2),
    _OwDS2450ChannelAConversionResolution_Type()
)
owDS2450ChannelAConversionResolution.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    owDS2450ChannelAConversionResolution.setStatus("current")


class _OwDS2450ChannelAConversionRange_Type(Integer32):
    """Custom type owDS2450ChannelAConversionRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 0))
    )


_OwDS2450ChannelAConversionRange_Type.__name__ = "Integer32"
_OwDS2450ChannelAConversionRange_Object = MibTableColumn
owDS2450ChannelAConversionRange = _OwDS2450ChannelAConversionRange_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 10, 1, 3),
    _OwDS2450ChannelAConversionRange_Type()
)
owDS2450ChannelAConversionRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    owDS2450ChannelAConversionRange.setStatus("current")


class _OwDS2450ChannelAOutputEnable_Type(Integer32):
    """Custom type owDS2450ChannelAOutputEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 0))
    )


_OwDS2450ChannelAOutputEnable_Type.__name__ = "Integer32"
_OwDS2450ChannelAOutputEnable_Object = MibTableColumn
owDS2450ChannelAOutputEnable = _OwDS2450ChannelAOutputEnable_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 10, 1, 4),
    _OwDS2450ChannelAOutputEnable_Type()
)
owDS2450ChannelAOutputEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    owDS2450ChannelAOutputEnable.setStatus("current")


class _OwDS2450ChannelAOutputControl_Type(Integer32):
    """Custom type owDS2450ChannelAOutputControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 0))
    )


_OwDS2450ChannelAOutputControl_Type.__name__ = "Integer32"
_OwDS2450ChannelAOutputControl_Object = MibTableColumn
owDS2450ChannelAOutputControl = _OwDS2450ChannelAOutputControl_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 10, 1, 5),
    _OwDS2450ChannelAOutputControl_Type()
)
owDS2450ChannelAOutputControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    owDS2450ChannelAOutputControl.setStatus("current")
_OwDS2450ChannelBConversionValue_Type = DisplayString
_OwDS2450ChannelBConversionValue_Object = MibTableColumn
owDS2450ChannelBConversionValue = _OwDS2450ChannelBConversionValue_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 10, 1, 6),
    _OwDS2450ChannelBConversionValue_Type()
)
owDS2450ChannelBConversionValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owDS2450ChannelBConversionValue.setStatus("current")
_OwDS2450ChannelBConversionResolution_Type = Integer32
_OwDS2450ChannelBConversionResolution_Object = MibTableColumn
owDS2450ChannelBConversionResolution = _OwDS2450ChannelBConversionResolution_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 10, 1, 7),
    _OwDS2450ChannelBConversionResolution_Type()
)
owDS2450ChannelBConversionResolution.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    owDS2450ChannelBConversionResolution.setStatus("current")


class _OwDS2450ChannelBConversionRange_Type(Integer32):
    """Custom type owDS2450ChannelBConversionRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 0))
    )


_OwDS2450ChannelBConversionRange_Type.__name__ = "Integer32"
_OwDS2450ChannelBConversionRange_Object = MibTableColumn
owDS2450ChannelBConversionRange = _OwDS2450ChannelBConversionRange_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 10, 1, 8),
    _OwDS2450ChannelBConversionRange_Type()
)
owDS2450ChannelBConversionRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    owDS2450ChannelBConversionRange.setStatus("current")


class _OwDS2450ChannelBOutputEnable_Type(Integer32):
    """Custom type owDS2450ChannelBOutputEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 0))
    )


_OwDS2450ChannelBOutputEnable_Type.__name__ = "Integer32"
_OwDS2450ChannelBOutputEnable_Object = MibTableColumn
owDS2450ChannelBOutputEnable = _OwDS2450ChannelBOutputEnable_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 10, 1, 9),
    _OwDS2450ChannelBOutputEnable_Type()
)
owDS2450ChannelBOutputEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    owDS2450ChannelBOutputEnable.setStatus("current")


class _OwDS2450ChannelBOutputControl_Type(Integer32):
    """Custom type owDS2450ChannelBOutputControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 0))
    )


_OwDS2450ChannelBOutputControl_Type.__name__ = "Integer32"
_OwDS2450ChannelBOutputControl_Object = MibTableColumn
owDS2450ChannelBOutputControl = _OwDS2450ChannelBOutputControl_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 10, 1, 10),
    _OwDS2450ChannelBOutputControl_Type()
)
owDS2450ChannelBOutputControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    owDS2450ChannelBOutputControl.setStatus("current")
_OwDS2450ChannelCConversionValue_Type = DisplayString
_OwDS2450ChannelCConversionValue_Object = MibTableColumn
owDS2450ChannelCConversionValue = _OwDS2450ChannelCConversionValue_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 10, 1, 11),
    _OwDS2450ChannelCConversionValue_Type()
)
owDS2450ChannelCConversionValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owDS2450ChannelCConversionValue.setStatus("current")
_OwDS2450ChannelCConversionResolution_Type = Integer32
_OwDS2450ChannelCConversionResolution_Object = MibTableColumn
owDS2450ChannelCConversionResolution = _OwDS2450ChannelCConversionResolution_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 10, 1, 12),
    _OwDS2450ChannelCConversionResolution_Type()
)
owDS2450ChannelCConversionResolution.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    owDS2450ChannelCConversionResolution.setStatus("current")


class _OwDS2450ChannelCConversionRange_Type(Integer32):
    """Custom type owDS2450ChannelCConversionRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 0))
    )


_OwDS2450ChannelCConversionRange_Type.__name__ = "Integer32"
_OwDS2450ChannelCConversionRange_Object = MibTableColumn
owDS2450ChannelCConversionRange = _OwDS2450ChannelCConversionRange_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 10, 1, 13),
    _OwDS2450ChannelCConversionRange_Type()
)
owDS2450ChannelCConversionRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    owDS2450ChannelCConversionRange.setStatus("current")


class _OwDS2450ChannelCOutputEnable_Type(Integer32):
    """Custom type owDS2450ChannelCOutputEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 0))
    )


_OwDS2450ChannelCOutputEnable_Type.__name__ = "Integer32"
_OwDS2450ChannelCOutputEnable_Object = MibTableColumn
owDS2450ChannelCOutputEnable = _OwDS2450ChannelCOutputEnable_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 10, 1, 14),
    _OwDS2450ChannelCOutputEnable_Type()
)
owDS2450ChannelCOutputEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    owDS2450ChannelCOutputEnable.setStatus("current")


class _OwDS2450ChannelCOutputControl_Type(Integer32):
    """Custom type owDS2450ChannelCOutputControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 0))
    )


_OwDS2450ChannelCOutputControl_Type.__name__ = "Integer32"
_OwDS2450ChannelCOutputControl_Object = MibTableColumn
owDS2450ChannelCOutputControl = _OwDS2450ChannelCOutputControl_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 10, 1, 15),
    _OwDS2450ChannelCOutputControl_Type()
)
owDS2450ChannelCOutputControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    owDS2450ChannelCOutputControl.setStatus("current")
_OwDS2450ChannelDConversionValue_Type = DisplayString
_OwDS2450ChannelDConversionValue_Object = MibTableColumn
owDS2450ChannelDConversionValue = _OwDS2450ChannelDConversionValue_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 10, 1, 16),
    _OwDS2450ChannelDConversionValue_Type()
)
owDS2450ChannelDConversionValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owDS2450ChannelDConversionValue.setStatus("current")
_OwDS2450ChannelDConversionResolution_Type = Integer32
_OwDS2450ChannelDConversionResolution_Object = MibTableColumn
owDS2450ChannelDConversionResolution = _OwDS2450ChannelDConversionResolution_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 10, 1, 17),
    _OwDS2450ChannelDConversionResolution_Type()
)
owDS2450ChannelDConversionResolution.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    owDS2450ChannelDConversionResolution.setStatus("current")


class _OwDS2450ChannelDConversionRange_Type(Integer32):
    """Custom type owDS2450ChannelDConversionRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 0))
    )


_OwDS2450ChannelDConversionRange_Type.__name__ = "Integer32"
_OwDS2450ChannelDConversionRange_Object = MibTableColumn
owDS2450ChannelDConversionRange = _OwDS2450ChannelDConversionRange_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 10, 1, 18),
    _OwDS2450ChannelDConversionRange_Type()
)
owDS2450ChannelDConversionRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    owDS2450ChannelDConversionRange.setStatus("current")


class _OwDS2450ChannelDOutputEnable_Type(Integer32):
    """Custom type owDS2450ChannelDOutputEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 0))
    )


_OwDS2450ChannelDOutputEnable_Type.__name__ = "Integer32"
_OwDS2450ChannelDOutputEnable_Object = MibTableColumn
owDS2450ChannelDOutputEnable = _OwDS2450ChannelDOutputEnable_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 10, 1, 19),
    _OwDS2450ChannelDOutputEnable_Type()
)
owDS2450ChannelDOutputEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    owDS2450ChannelDOutputEnable.setStatus("current")


class _OwDS2450ChannelDOutputControl_Type(Integer32):
    """Custom type owDS2450ChannelDOutputControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 0))
    )


_OwDS2450ChannelDOutputControl_Type.__name__ = "Integer32"
_OwDS2450ChannelDOutputControl_Object = MibTableColumn
owDS2450ChannelDOutputControl = _OwDS2450ChannelDOutputControl_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 10, 1, 20),
    _OwDS2450ChannelDOutputControl_Type()
)
owDS2450ChannelDOutputControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    owDS2450ChannelDOutputControl.setStatus("current")


class _OwDS2450PowerOnReset_Type(Integer32):
    """Custom type owDS2450PowerOnReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 0))
    )


_OwDS2450PowerOnReset_Type.__name__ = "Integer32"
_OwDS2450PowerOnReset_Object = MibTableColumn
owDS2450PowerOnReset = _OwDS2450PowerOnReset_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 10, 1, 21),
    _OwDS2450PowerOnReset_Type()
)
owDS2450PowerOnReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    owDS2450PowerOnReset.setStatus("current")


class _OwDS2450VCCControl_Type(Integer32):
    """Custom type owDS2450VCCControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 0))
    )


_OwDS2450VCCControl_Type.__name__ = "Integer32"
_OwDS2450VCCControl_Object = MibTableColumn
owDS2450VCCControl = _OwDS2450VCCControl_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 10, 1, 22),
    _OwDS2450VCCControl_Type()
)
owDS2450VCCControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    owDS2450VCCControl.setStatus("current")
_OwEDS0064Table_Object = MibTable
owEDS0064Table = _OwEDS0064Table_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 11)
)
if mibBuilder.loadTexts:
    owEDS0064Table.setStatus("current")
_OwEDS0064Entry_Object = MibTableRow
owEDS0064Entry = _OwEDS0064Entry_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 11, 1)
)
owEDS0064Entry.setIndexNames(
    (0, "EDS-MIB", "owDeviceIndex"),
)
if mibBuilder.loadTexts:
    owEDS0064Entry.setStatus("current")
_OwEDS0064Temperature_Type = DisplayString
_OwEDS0064Temperature_Object = MibTableColumn
owEDS0064Temperature = _OwEDS0064Temperature_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 11, 1, 1),
    _OwEDS0064Temperature_Type()
)
owEDS0064Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0064Temperature.setStatus("current")
_OwEDS0064Counter_Type = Counter32
_OwEDS0064Counter_Object = MibTableColumn
owEDS0064Counter = _OwEDS0064Counter_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 11, 1, 2),
    _OwEDS0064Counter_Type()
)
owEDS0064Counter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0064Counter.setStatus("current")
_OwEDS0065Table_Object = MibTable
owEDS0065Table = _OwEDS0065Table_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 12)
)
if mibBuilder.loadTexts:
    owEDS0065Table.setStatus("current")
_OwEDS0065Entry_Object = MibTableRow
owEDS0065Entry = _OwEDS0065Entry_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 12, 1)
)
owEDS0065Entry.setIndexNames(
    (0, "EDS-MIB", "owDeviceIndex"),
)
if mibBuilder.loadTexts:
    owEDS0065Entry.setStatus("current")
_OwEDS0065Temperature_Type = DisplayString
_OwEDS0065Temperature_Object = MibTableColumn
owEDS0065Temperature = _OwEDS0065Temperature_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 12, 1, 1),
    _OwEDS0065Temperature_Type()
)
owEDS0065Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0065Temperature.setStatus("current")
_OwEDS0065Humidity_Type = DisplayString
_OwEDS0065Humidity_Object = MibTableColumn
owEDS0065Humidity = _OwEDS0065Humidity_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 12, 1, 2),
    _OwEDS0065Humidity_Type()
)
owEDS0065Humidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0065Humidity.setStatus("current")
_OwEDS0065DewPoint_Type = DisplayString
_OwEDS0065DewPoint_Object = MibTableColumn
owEDS0065DewPoint = _OwEDS0065DewPoint_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 12, 1, 3),
    _OwEDS0065DewPoint_Type()
)
owEDS0065DewPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0065DewPoint.setStatus("current")
_OwEDS0065Humidex_Type = DisplayString
_OwEDS0065Humidex_Object = MibTableColumn
owEDS0065Humidex = _OwEDS0065Humidex_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 12, 1, 4),
    _OwEDS0065Humidex_Type()
)
owEDS0065Humidex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0065Humidex.setStatus("current")
_OwEDS0065HeatIndex_Type = DisplayString
_OwEDS0065HeatIndex_Object = MibTableColumn
owEDS0065HeatIndex = _OwEDS0065HeatIndex_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 12, 1, 5),
    _OwEDS0065HeatIndex_Type()
)
owEDS0065HeatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0065HeatIndex.setStatus("current")
_OwEDS0065Counter_Type = Counter32
_OwEDS0065Counter_Object = MibTableColumn
owEDS0065Counter = _OwEDS0065Counter_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 12, 1, 6),
    _OwEDS0065Counter_Type()
)
owEDS0065Counter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0065Counter.setStatus("current")
_OwEDS0066Table_Object = MibTable
owEDS0066Table = _OwEDS0066Table_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 13)
)
if mibBuilder.loadTexts:
    owEDS0066Table.setStatus("current")
_OwEDS0066Entry_Object = MibTableRow
owEDS0066Entry = _OwEDS0066Entry_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 13, 1)
)
owEDS0066Entry.setIndexNames(
    (0, "EDS-MIB", "owDeviceIndex"),
)
if mibBuilder.loadTexts:
    owEDS0066Entry.setStatus("current")
_OwEDS0066Temperature_Type = DisplayString
_OwEDS0066Temperature_Object = MibTableColumn
owEDS0066Temperature = _OwEDS0066Temperature_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 13, 1, 1),
    _OwEDS0066Temperature_Type()
)
owEDS0066Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0066Temperature.setStatus("current")
_OwEDS0066BarometricPressureMb_Type = DisplayString
_OwEDS0066BarometricPressureMb_Object = MibTableColumn
owEDS0066BarometricPressureMb = _OwEDS0066BarometricPressureMb_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 13, 1, 2),
    _OwEDS0066BarometricPressureMb_Type()
)
owEDS0066BarometricPressureMb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0066BarometricPressureMb.setStatus("current")
_OwEDS0066BarometricPressureHg_Type = DisplayString
_OwEDS0066BarometricPressureHg_Object = MibTableColumn
owEDS0066BarometricPressureHg = _OwEDS0066BarometricPressureHg_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 13, 1, 3),
    _OwEDS0066BarometricPressureHg_Type()
)
owEDS0066BarometricPressureHg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0066BarometricPressureHg.setStatus("current")
_OwEDS0066Counter_Type = Counter32
_OwEDS0066Counter_Object = MibTableColumn
owEDS0066Counter = _OwEDS0066Counter_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 13, 1, 4),
    _OwEDS0066Counter_Type()
)
owEDS0066Counter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0066Counter.setStatus("current")
_OwEDS0067Table_Object = MibTable
owEDS0067Table = _OwEDS0067Table_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 14)
)
if mibBuilder.loadTexts:
    owEDS0067Table.setStatus("current")
_OwEDS0067Entry_Object = MibTableRow
owEDS0067Entry = _OwEDS0067Entry_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 14, 1)
)
owEDS0067Entry.setIndexNames(
    (0, "EDS-MIB", "owDeviceIndex"),
)
if mibBuilder.loadTexts:
    owEDS0067Entry.setStatus("current")
_OwEDS0067Temperature_Type = DisplayString
_OwEDS0067Temperature_Object = MibTableColumn
owEDS0067Temperature = _OwEDS0067Temperature_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 14, 1, 1),
    _OwEDS0067Temperature_Type()
)
owEDS0067Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0067Temperature.setStatus("current")
_OwEDS0067Light_Type = DisplayString
_OwEDS0067Light_Object = MibTableColumn
owEDS0067Light = _OwEDS0067Light_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 14, 1, 2),
    _OwEDS0067Light_Type()
)
owEDS0067Light.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0067Light.setStatus("current")
_OwEDS0067Counter_Type = Counter32
_OwEDS0067Counter_Object = MibTableColumn
owEDS0067Counter = _OwEDS0067Counter_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 14, 1, 3),
    _OwEDS0067Counter_Type()
)
owEDS0067Counter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0067Counter.setStatus("current")
_OwEDS0068Table_Object = MibTable
owEDS0068Table = _OwEDS0068Table_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 15)
)
if mibBuilder.loadTexts:
    owEDS0068Table.setStatus("current")
_OwEDS0068Entry_Object = MibTableRow
owEDS0068Entry = _OwEDS0068Entry_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 15, 1)
)
owEDS0068Entry.setIndexNames(
    (0, "EDS-MIB", "owDeviceIndex"),
)
if mibBuilder.loadTexts:
    owEDS0068Entry.setStatus("current")
_OwEDS0068Temperature_Type = DisplayString
_OwEDS0068Temperature_Object = MibTableColumn
owEDS0068Temperature = _OwEDS0068Temperature_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 15, 1, 1),
    _OwEDS0068Temperature_Type()
)
owEDS0068Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0068Temperature.setStatus("current")
_OwEDS0068Humidity_Type = DisplayString
_OwEDS0068Humidity_Object = MibTableColumn
owEDS0068Humidity = _OwEDS0068Humidity_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 15, 1, 2),
    _OwEDS0068Humidity_Type()
)
owEDS0068Humidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0068Humidity.setStatus("current")
_OwEDS0068DewPoint_Type = DisplayString
_OwEDS0068DewPoint_Object = MibTableColumn
owEDS0068DewPoint = _OwEDS0068DewPoint_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 15, 1, 3),
    _OwEDS0068DewPoint_Type()
)
owEDS0068DewPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0068DewPoint.setStatus("current")
_OwEDS0068Humidex_Type = DisplayString
_OwEDS0068Humidex_Object = MibTableColumn
owEDS0068Humidex = _OwEDS0068Humidex_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 15, 1, 4),
    _OwEDS0068Humidex_Type()
)
owEDS0068Humidex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0068Humidex.setStatus("current")
_OwEDS0068HeatIndex_Type = DisplayString
_OwEDS0068HeatIndex_Object = MibTableColumn
owEDS0068HeatIndex = _OwEDS0068HeatIndex_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 15, 1, 5),
    _OwEDS0068HeatIndex_Type()
)
owEDS0068HeatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0068HeatIndex.setStatus("current")
_OwEDS0068BarometricPressureMb_Type = DisplayString
_OwEDS0068BarometricPressureMb_Object = MibTableColumn
owEDS0068BarometricPressureMb = _OwEDS0068BarometricPressureMb_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 15, 1, 6),
    _OwEDS0068BarometricPressureMb_Type()
)
owEDS0068BarometricPressureMb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0068BarometricPressureMb.setStatus("current")
_OwEDS0068BarometricPressureHg_Type = DisplayString
_OwEDS0068BarometricPressureHg_Object = MibTableColumn
owEDS0068BarometricPressureHg = _OwEDS0068BarometricPressureHg_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 15, 1, 7),
    _OwEDS0068BarometricPressureHg_Type()
)
owEDS0068BarometricPressureHg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0068BarometricPressureHg.setStatus("current")
_OwEDS0068Light_Type = DisplayString
_OwEDS0068Light_Object = MibTableColumn
owEDS0068Light = _OwEDS0068Light_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 15, 1, 8),
    _OwEDS0068Light_Type()
)
owEDS0068Light.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0068Light.setStatus("current")
_OwEDS0068Counter_Type = Counter32
_OwEDS0068Counter_Object = MibTableColumn
owEDS0068Counter = _OwEDS0068Counter_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 15, 1, 9),
    _OwEDS0068Counter_Type()
)
owEDS0068Counter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0068Counter.setStatus("current")
_OwEDS0069Table_Object = MibTable
owEDS0069Table = _OwEDS0069Table_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 16)
)
if mibBuilder.loadTexts:
    owEDS0069Table.setStatus("current")
_OwEDS0069Entry_Object = MibTableRow
owEDS0069Entry = _OwEDS0069Entry_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 16, 1)
)
owEDS0069Entry.setIndexNames(
    (0, "EDS-MIB", "owDeviceIndex"),
)
if mibBuilder.loadTexts:
    owEDS0069Entry.setStatus("current")
_OwEDS0069Temperature_Type = DisplayString
_OwEDS0069Temperature_Object = MibTableColumn
owEDS0069Temperature = _OwEDS0069Temperature_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 16, 1, 1),
    _OwEDS0069Temperature_Type()
)
owEDS0069Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0069Temperature.setStatus("current")
_OwEDS0069Motion_Type = DisplayString
_OwEDS0069Motion_Object = MibTableColumn
owEDS0069Motion = _OwEDS0069Motion_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 16, 1, 2),
    _OwEDS0069Motion_Type()
)
owEDS0069Motion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0069Motion.setStatus("current")
_OwEDS0069Counter_Type = Counter32
_OwEDS0069Counter_Object = MibTableColumn
owEDS0069Counter = _OwEDS0069Counter_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 16, 1, 3),
    _OwEDS0069Counter_Type()
)
owEDS0069Counter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0069Counter.setStatus("current")
_OwEDS0070Table_Object = MibTable
owEDS0070Table = _OwEDS0070Table_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 17)
)
if mibBuilder.loadTexts:
    owEDS0070Table.setStatus("current")
_OwEDS0070Entry_Object = MibTableRow
owEDS0070Entry = _OwEDS0070Entry_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 17, 1)
)
owEDS0070Entry.setIndexNames(
    (0, "EDS-MIB", "owDeviceIndex"),
)
if mibBuilder.loadTexts:
    owEDS0070Entry.setStatus("current")


class _OwEDS0070VibrationInstant_Type(Integer32):
    """Custom type owEDS0070VibrationInstant based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              65535)
        )
    )
    namedValues = NamedValues(
        *(("high", 65535),
          ("low", 0))
    )


_OwEDS0070VibrationInstant_Type.__name__ = "Integer32"
_OwEDS0070VibrationInstant_Object = MibTableColumn
owEDS0070VibrationInstant = _OwEDS0070VibrationInstant_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 17, 1, 1),
    _OwEDS0070VibrationInstant_Type()
)
owEDS0070VibrationInstant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0070VibrationInstant.setStatus("current")


class _OwEDS0070VibrationPeak_Type(Integer32):
    """Custom type owEDS0070VibrationPeak based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              65535)
        )
    )
    namedValues = NamedValues(
        *(("high", 65535),
          ("low", 0))
    )


_OwEDS0070VibrationPeak_Type.__name__ = "Integer32"
_OwEDS0070VibrationPeak_Object = MibTableColumn
owEDS0070VibrationPeak = _OwEDS0070VibrationPeak_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 17, 1, 2),
    _OwEDS0070VibrationPeak_Type()
)
owEDS0070VibrationPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0070VibrationPeak.setStatus("current")


class _OwEDS0070VibrationMax_Type(Integer32):
    """Custom type owEDS0070VibrationMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              65535)
        )
    )
    namedValues = NamedValues(
        *(("high", 65535),
          ("low", 0))
    )


_OwEDS0070VibrationMax_Type.__name__ = "Integer32"
_OwEDS0070VibrationMax_Object = MibTableColumn
owEDS0070VibrationMax = _OwEDS0070VibrationMax_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 17, 1, 3),
    _OwEDS0070VibrationMax_Type()
)
owEDS0070VibrationMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0070VibrationMax.setStatus("current")


class _OwEDS0070VibrationMin_Type(Integer32):
    """Custom type owEDS0070VibrationMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              65535)
        )
    )
    namedValues = NamedValues(
        *(("high", 65535),
          ("low", 0))
    )


_OwEDS0070VibrationMin_Type.__name__ = "Integer32"
_OwEDS0070VibrationMin_Object = MibTableColumn
owEDS0070VibrationMin = _OwEDS0070VibrationMin_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 17, 1, 4),
    _OwEDS0070VibrationMin_Type()
)
owEDS0070VibrationMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0070VibrationMin.setStatus("current")
_OwEDS0070Counter_Type = Counter32
_OwEDS0070Counter_Object = MibTableColumn
owEDS0070Counter = _OwEDS0070Counter_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 17, 1, 5),
    _OwEDS0070Counter_Type()
)
owEDS0070Counter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0070Counter.setStatus("current")
_OwEDS0071Table_Object = MibTable
owEDS0071Table = _OwEDS0071Table_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 18)
)
if mibBuilder.loadTexts:
    owEDS0071Table.setStatus("current")
_OwEDS0071Entry_Object = MibTableRow
owEDS0071Entry = _OwEDS0071Entry_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 18, 1)
)
owEDS0071Entry.setIndexNames(
    (0, "EDS-MIB", "owDeviceIndex"),
)
if mibBuilder.loadTexts:
    owEDS0071Entry.setStatus("current")
_OwEDS0071Temperature_Type = DisplayString
_OwEDS0071Temperature_Object = MibTableColumn
owEDS0071Temperature = _OwEDS0071Temperature_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 18, 1, 1),
    _OwEDS0071Temperature_Type()
)
owEDS0071Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0071Temperature.setStatus("current")
_OwEDS0071Counter_Type = Counter32
_OwEDS0071Counter_Object = MibTableColumn
owEDS0071Counter = _OwEDS0071Counter_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 18, 1, 2),
    _OwEDS0071Counter_Type()
)
owEDS0071Counter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0071Counter.setStatus("current")
_OwEDS0080Table_Object = MibTable
owEDS0080Table = _OwEDS0080Table_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 19)
)
if mibBuilder.loadTexts:
    owEDS0080Table.setStatus("current")
_OwEDS0080Entry_Object = MibTableRow
owEDS0080Entry = _OwEDS0080Entry_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 19, 1)
)
owEDS0080Entry.setIndexNames(
    (0, "EDS-MIB", "owDeviceIndex"),
)
if mibBuilder.loadTexts:
    owEDS0080Entry.setStatus("current")
_OwEDS0080Input1_Type = DisplayString
_OwEDS0080Input1_Object = MibTableColumn
owEDS0080Input1 = _OwEDS0080Input1_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 19, 1, 1),
    _OwEDS0080Input1_Type()
)
owEDS0080Input1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0080Input1.setStatus("current")
_OwEDS0080Input2_Type = DisplayString
_OwEDS0080Input2_Object = MibTableColumn
owEDS0080Input2 = _OwEDS0080Input2_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 19, 1, 2),
    _OwEDS0080Input2_Type()
)
owEDS0080Input2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0080Input2.setStatus("current")
_OwEDS0080Input3_Type = DisplayString
_OwEDS0080Input3_Object = MibTableColumn
owEDS0080Input3 = _OwEDS0080Input3_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 19, 1, 3),
    _OwEDS0080Input3_Type()
)
owEDS0080Input3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0080Input3.setStatus("current")
_OwEDS0080Input4_Type = DisplayString
_OwEDS0080Input4_Object = MibTableColumn
owEDS0080Input4 = _OwEDS0080Input4_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 19, 1, 4),
    _OwEDS0080Input4_Type()
)
owEDS0080Input4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0080Input4.setStatus("current")
_OwEDS0080Input5_Type = DisplayString
_OwEDS0080Input5_Object = MibTableColumn
owEDS0080Input5 = _OwEDS0080Input5_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 19, 1, 5),
    _OwEDS0080Input5_Type()
)
owEDS0080Input5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0080Input5.setStatus("current")
_OwEDS0080Input6_Type = DisplayString
_OwEDS0080Input6_Object = MibTableColumn
owEDS0080Input6 = _OwEDS0080Input6_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 19, 1, 6),
    _OwEDS0080Input6_Type()
)
owEDS0080Input6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0080Input6.setStatus("current")
_OwEDS0080Input7_Type = DisplayString
_OwEDS0080Input7_Object = MibTableColumn
owEDS0080Input7 = _OwEDS0080Input7_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 19, 1, 7),
    _OwEDS0080Input7_Type()
)
owEDS0080Input7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0080Input7.setStatus("current")
_OwEDS0080Input8_Type = DisplayString
_OwEDS0080Input8_Object = MibTableColumn
owEDS0080Input8 = _OwEDS0080Input8_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 19, 1, 8),
    _OwEDS0080Input8_Type()
)
owEDS0080Input8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0080Input8.setStatus("current")
_OwEDS0080Counter_Type = Counter32
_OwEDS0080Counter_Object = MibTableColumn
owEDS0080Counter = _OwEDS0080Counter_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 19, 1, 9),
    _OwEDS0080Counter_Type()
)
owEDS0080Counter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0080Counter.setStatus("current")
_OwEDS0082Table_Object = MibTable
owEDS0082Table = _OwEDS0082Table_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 20)
)
if mibBuilder.loadTexts:
    owEDS0082Table.setStatus("current")
_OwEDS0082Entry_Object = MibTableRow
owEDS0082Entry = _OwEDS0082Entry_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 20, 1)
)
owEDS0082Entry.setIndexNames(
    (0, "EDS-MIB", "owDeviceIndex"),
)
if mibBuilder.loadTexts:
    owEDS0082Entry.setStatus("current")
_OwEDS0082Input1_Type = DisplayString
_OwEDS0082Input1_Object = MibTableColumn
owEDS0082Input1 = _OwEDS0082Input1_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 20, 1, 1),
    _OwEDS0082Input1_Type()
)
owEDS0082Input1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0082Input1.setStatus("current")
_OwEDS0082Input2_Type = DisplayString
_OwEDS0082Input2_Object = MibTableColumn
owEDS0082Input2 = _OwEDS0082Input2_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 20, 1, 2),
    _OwEDS0082Input2_Type()
)
owEDS0082Input2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0082Input2.setStatus("current")
_OwEDS0082Input3_Type = DisplayString
_OwEDS0082Input3_Object = MibTableColumn
owEDS0082Input3 = _OwEDS0082Input3_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 20, 1, 3),
    _OwEDS0082Input3_Type()
)
owEDS0082Input3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0082Input3.setStatus("current")
_OwEDS0082Input4_Type = DisplayString
_OwEDS0082Input4_Object = MibTableColumn
owEDS0082Input4 = _OwEDS0082Input4_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 20, 1, 4),
    _OwEDS0082Input4_Type()
)
owEDS0082Input4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0082Input4.setStatus("current")
_OwEDS0082Input5_Type = DisplayString
_OwEDS0082Input5_Object = MibTableColumn
owEDS0082Input5 = _OwEDS0082Input5_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 20, 1, 5),
    _OwEDS0082Input5_Type()
)
owEDS0082Input5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0082Input5.setStatus("current")
_OwEDS0082Input6_Type = DisplayString
_OwEDS0082Input6_Object = MibTableColumn
owEDS0082Input6 = _OwEDS0082Input6_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 20, 1, 6),
    _OwEDS0082Input6_Type()
)
owEDS0082Input6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0082Input6.setStatus("current")
_OwEDS0082Input7_Type = DisplayString
_OwEDS0082Input7_Object = MibTableColumn
owEDS0082Input7 = _OwEDS0082Input7_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 20, 1, 7),
    _OwEDS0082Input7_Type()
)
owEDS0082Input7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0082Input7.setStatus("current")
_OwEDS0082Input8_Type = DisplayString
_OwEDS0082Input8_Object = MibTableColumn
owEDS0082Input8 = _OwEDS0082Input8_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 20, 1, 8),
    _OwEDS0082Input8_Type()
)
owEDS0082Input8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0082Input8.setStatus("current")
_OwEDS0082Counter_Type = Counter32
_OwEDS0082Counter_Object = MibTableColumn
owEDS0082Counter = _OwEDS0082Counter_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 20, 1, 9),
    _OwEDS0082Counter_Type()
)
owEDS0082Counter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0082Counter.setStatus("current")
_OwEDS0083Table_Object = MibTable
owEDS0083Table = _OwEDS0083Table_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 21)
)
if mibBuilder.loadTexts:
    owEDS0083Table.setStatus("current")
_OwEDS0083Entry_Object = MibTableRow
owEDS0083Entry = _OwEDS0083Entry_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 21, 1)
)
owEDS0083Entry.setIndexNames(
    (0, "EDS-MIB", "owDeviceIndex"),
)
if mibBuilder.loadTexts:
    owEDS0083Entry.setStatus("current")
_OwEDS0083Input1_Type = DisplayString
_OwEDS0083Input1_Object = MibTableColumn
owEDS0083Input1 = _OwEDS0083Input1_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 21, 1, 1),
    _OwEDS0083Input1_Type()
)
owEDS0083Input1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0083Input1.setStatus("current")
_OwEDS0083Input2_Type = DisplayString
_OwEDS0083Input2_Object = MibTableColumn
owEDS0083Input2 = _OwEDS0083Input2_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 21, 1, 2),
    _OwEDS0083Input2_Type()
)
owEDS0083Input2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0083Input2.setStatus("current")
_OwEDS0083Input3_Type = DisplayString
_OwEDS0083Input3_Object = MibTableColumn
owEDS0083Input3 = _OwEDS0083Input3_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 21, 1, 3),
    _OwEDS0083Input3_Type()
)
owEDS0083Input3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0083Input3.setStatus("current")
_OwEDS0083Input4_Type = DisplayString
_OwEDS0083Input4_Object = MibTableColumn
owEDS0083Input4 = _OwEDS0083Input4_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 21, 1, 4),
    _OwEDS0083Input4_Type()
)
owEDS0083Input4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0083Input4.setStatus("current")
_OwEDS0083Counter_Type = Counter32
_OwEDS0083Counter_Object = MibTableColumn
owEDS0083Counter = _OwEDS0083Counter_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 21, 1, 5),
    _OwEDS0083Counter_Type()
)
owEDS0083Counter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0083Counter.setStatus("current")
_OwEDS0085Table_Object = MibTable
owEDS0085Table = _OwEDS0085Table_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 22)
)
if mibBuilder.loadTexts:
    owEDS0085Table.setStatus("current")
_OwEDS0085Entry_Object = MibTableRow
owEDS0085Entry = _OwEDS0085Entry_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 22, 1)
)
owEDS0085Entry.setIndexNames(
    (0, "EDS-MIB", "owDeviceIndex"),
)
if mibBuilder.loadTexts:
    owEDS0085Entry.setStatus("current")
_OwEDS0085Input1_Type = DisplayString
_OwEDS0085Input1_Object = MibTableColumn
owEDS0085Input1 = _OwEDS0085Input1_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 22, 1, 1),
    _OwEDS0085Input1_Type()
)
owEDS0085Input1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0085Input1.setStatus("current")
_OwEDS0085Input2_Type = DisplayString
_OwEDS0085Input2_Object = MibTableColumn
owEDS0085Input2 = _OwEDS0085Input2_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 22, 1, 2),
    _OwEDS0085Input2_Type()
)
owEDS0085Input2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0085Input2.setStatus("current")
_OwEDS0085Input3_Type = DisplayString
_OwEDS0085Input3_Object = MibTableColumn
owEDS0085Input3 = _OwEDS0085Input3_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 22, 1, 3),
    _OwEDS0085Input3_Type()
)
owEDS0085Input3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0085Input3.setStatus("current")
_OwEDS0085Input4_Type = DisplayString
_OwEDS0085Input4_Object = MibTableColumn
owEDS0085Input4 = _OwEDS0085Input4_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 22, 1, 4),
    _OwEDS0085Input4_Type()
)
owEDS0085Input4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0085Input4.setStatus("current")
_OwEDS0085Counter_Type = Counter32
_OwEDS0085Counter_Object = MibTableColumn
owEDS0085Counter = _OwEDS0085Counter_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 22, 1, 5),
    _OwEDS0085Counter_Type()
)
owEDS0085Counter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0085Counter.setStatus("current")
_OwEDS0090Table_Object = MibTable
owEDS0090Table = _OwEDS0090Table_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 23)
)
if mibBuilder.loadTexts:
    owEDS0090Table.setStatus("current")
_OwEDS0090Entry_Object = MibTableRow
owEDS0090Entry = _OwEDS0090Entry_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 23, 1)
)
owEDS0090Entry.setIndexNames(
    (0, "EDS-MIB", "owDeviceIndex"),
)
if mibBuilder.loadTexts:
    owEDS0090Entry.setStatus("current")


class _OwEDS0090Input1_Type(Integer32):
    """Custom type owEDS0090Input1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 0))
    )


_OwEDS0090Input1_Type.__name__ = "Integer32"
_OwEDS0090Input1_Object = MibTableColumn
owEDS0090Input1 = _OwEDS0090Input1_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 23, 1, 1),
    _OwEDS0090Input1_Type()
)
owEDS0090Input1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0090Input1.setStatus("current")


class _OwEDS0090Input2_Type(Integer32):
    """Custom type owEDS0090Input2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 0))
    )


_OwEDS0090Input2_Type.__name__ = "Integer32"
_OwEDS0090Input2_Object = MibTableColumn
owEDS0090Input2 = _OwEDS0090Input2_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 23, 1, 2),
    _OwEDS0090Input2_Type()
)
owEDS0090Input2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0090Input2.setStatus("current")


class _OwEDS0090Input3_Type(Integer32):
    """Custom type owEDS0090Input3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 0))
    )


_OwEDS0090Input3_Type.__name__ = "Integer32"
_OwEDS0090Input3_Object = MibTableColumn
owEDS0090Input3 = _OwEDS0090Input3_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 23, 1, 3),
    _OwEDS0090Input3_Type()
)
owEDS0090Input3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0090Input3.setStatus("current")


class _OwEDS0090Input4_Type(Integer32):
    """Custom type owEDS0090Input4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 0))
    )


_OwEDS0090Input4_Type.__name__ = "Integer32"
_OwEDS0090Input4_Object = MibTableColumn
owEDS0090Input4 = _OwEDS0090Input4_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 23, 1, 4),
    _OwEDS0090Input4_Type()
)
owEDS0090Input4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0090Input4.setStatus("current")


class _OwEDS0090Input5_Type(Integer32):
    """Custom type owEDS0090Input5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 0))
    )


_OwEDS0090Input5_Type.__name__ = "Integer32"
_OwEDS0090Input5_Object = MibTableColumn
owEDS0090Input5 = _OwEDS0090Input5_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 23, 1, 5),
    _OwEDS0090Input5_Type()
)
owEDS0090Input5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0090Input5.setStatus("current")


class _OwEDS0090Input6_Type(Integer32):
    """Custom type owEDS0090Input6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 0))
    )


_OwEDS0090Input6_Type.__name__ = "Integer32"
_OwEDS0090Input6_Object = MibTableColumn
owEDS0090Input6 = _OwEDS0090Input6_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 23, 1, 6),
    _OwEDS0090Input6_Type()
)
owEDS0090Input6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0090Input6.setStatus("current")


class _OwEDS0090Input7_Type(Integer32):
    """Custom type owEDS0090Input7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 0))
    )


_OwEDS0090Input7_Type.__name__ = "Integer32"
_OwEDS0090Input7_Object = MibTableColumn
owEDS0090Input7 = _OwEDS0090Input7_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 23, 1, 7),
    _OwEDS0090Input7_Type()
)
owEDS0090Input7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0090Input7.setStatus("current")


class _OwEDS0090Input8_Type(Integer32):
    """Custom type owEDS0090Input8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 0))
    )


_OwEDS0090Input8_Type.__name__ = "Integer32"
_OwEDS0090Input8_Object = MibTableColumn
owEDS0090Input8 = _OwEDS0090Input8_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 23, 1, 8),
    _OwEDS0090Input8_Type()
)
owEDS0090Input8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0090Input8.setStatus("current")


class _OwEDS0090ActivityLatch1_Type(Integer32):
    """Custom type owEDS0090ActivityLatch1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_OwEDS0090ActivityLatch1_Type.__name__ = "Integer32"
_OwEDS0090ActivityLatch1_Object = MibTableColumn
owEDS0090ActivityLatch1 = _OwEDS0090ActivityLatch1_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 23, 1, 9),
    _OwEDS0090ActivityLatch1_Type()
)
owEDS0090ActivityLatch1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0090ActivityLatch1.setStatus("current")


class _OwEDS0090ActivityLatch2_Type(Integer32):
    """Custom type owEDS0090ActivityLatch2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_OwEDS0090ActivityLatch2_Type.__name__ = "Integer32"
_OwEDS0090ActivityLatch2_Object = MibTableColumn
owEDS0090ActivityLatch2 = _OwEDS0090ActivityLatch2_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 23, 1, 10),
    _OwEDS0090ActivityLatch2_Type()
)
owEDS0090ActivityLatch2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0090ActivityLatch2.setStatus("current")


class _OwEDS0090ActivityLatch3_Type(Integer32):
    """Custom type owEDS0090ActivityLatch3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_OwEDS0090ActivityLatch3_Type.__name__ = "Integer32"
_OwEDS0090ActivityLatch3_Object = MibTableColumn
owEDS0090ActivityLatch3 = _OwEDS0090ActivityLatch3_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 23, 1, 11),
    _OwEDS0090ActivityLatch3_Type()
)
owEDS0090ActivityLatch3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0090ActivityLatch3.setStatus("current")


class _OwEDS0090ActivityLatch4_Type(Integer32):
    """Custom type owEDS0090ActivityLatch4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_OwEDS0090ActivityLatch4_Type.__name__ = "Integer32"
_OwEDS0090ActivityLatch4_Object = MibTableColumn
owEDS0090ActivityLatch4 = _OwEDS0090ActivityLatch4_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 23, 1, 12),
    _OwEDS0090ActivityLatch4_Type()
)
owEDS0090ActivityLatch4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0090ActivityLatch4.setStatus("current")


class _OwEDS0090ActivityLatch5_Type(Integer32):
    """Custom type owEDS0090ActivityLatch5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_OwEDS0090ActivityLatch5_Type.__name__ = "Integer32"
_OwEDS0090ActivityLatch5_Object = MibTableColumn
owEDS0090ActivityLatch5 = _OwEDS0090ActivityLatch5_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 23, 1, 13),
    _OwEDS0090ActivityLatch5_Type()
)
owEDS0090ActivityLatch5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0090ActivityLatch5.setStatus("current")


class _OwEDS0090ActivityLatch6_Type(Integer32):
    """Custom type owEDS0090ActivityLatch6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_OwEDS0090ActivityLatch6_Type.__name__ = "Integer32"
_OwEDS0090ActivityLatch6_Object = MibTableColumn
owEDS0090ActivityLatch6 = _OwEDS0090ActivityLatch6_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 23, 1, 14),
    _OwEDS0090ActivityLatch6_Type()
)
owEDS0090ActivityLatch6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0090ActivityLatch6.setStatus("current")


class _OwEDS0090ActivityLatch7_Type(Integer32):
    """Custom type owEDS0090ActivityLatch7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_OwEDS0090ActivityLatch7_Type.__name__ = "Integer32"
_OwEDS0090ActivityLatch7_Object = MibTableColumn
owEDS0090ActivityLatch7 = _OwEDS0090ActivityLatch7_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 23, 1, 15),
    _OwEDS0090ActivityLatch7_Type()
)
owEDS0090ActivityLatch7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0090ActivityLatch7.setStatus("current")


class _OwEDS0090ActivityLatch8_Type(Integer32):
    """Custom type owEDS0090ActivityLatch8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_OwEDS0090ActivityLatch8_Type.__name__ = "Integer32"
_OwEDS0090ActivityLatch8_Object = MibTableColumn
owEDS0090ActivityLatch8 = _OwEDS0090ActivityLatch8_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 23, 1, 16),
    _OwEDS0090ActivityLatch8_Type()
)
owEDS0090ActivityLatch8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0090ActivityLatch8.setStatus("current")
_OwEDS0090PulseCounter1_Type = Counter32
_OwEDS0090PulseCounter1_Object = MibTableColumn
owEDS0090PulseCounter1 = _OwEDS0090PulseCounter1_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 23, 1, 17),
    _OwEDS0090PulseCounter1_Type()
)
owEDS0090PulseCounter1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0090PulseCounter1.setStatus("current")
_OwEDS0090PulseCounter2_Type = Counter32
_OwEDS0090PulseCounter2_Object = MibTableColumn
owEDS0090PulseCounter2 = _OwEDS0090PulseCounter2_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 23, 1, 18),
    _OwEDS0090PulseCounter2_Type()
)
owEDS0090PulseCounter2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0090PulseCounter2.setStatus("current")
_OwEDS0090PulseCounter3_Type = Counter32
_OwEDS0090PulseCounter3_Object = MibTableColumn
owEDS0090PulseCounter3 = _OwEDS0090PulseCounter3_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 23, 1, 19),
    _OwEDS0090PulseCounter3_Type()
)
owEDS0090PulseCounter3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0090PulseCounter3.setStatus("current")
_OwEDS0090PulseCounter4_Type = Counter32
_OwEDS0090PulseCounter4_Object = MibTableColumn
owEDS0090PulseCounter4 = _OwEDS0090PulseCounter4_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 23, 1, 20),
    _OwEDS0090PulseCounter4_Type()
)
owEDS0090PulseCounter4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0090PulseCounter4.setStatus("current")
_OwEDS0090PulseCounter5_Type = Counter32
_OwEDS0090PulseCounter5_Object = MibTableColumn
owEDS0090PulseCounter5 = _OwEDS0090PulseCounter5_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 23, 1, 21),
    _OwEDS0090PulseCounter5_Type()
)
owEDS0090PulseCounter5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0090PulseCounter5.setStatus("current")
_OwEDS0090PulseCounter6_Type = Counter32
_OwEDS0090PulseCounter6_Object = MibTableColumn
owEDS0090PulseCounter6 = _OwEDS0090PulseCounter6_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 23, 1, 22),
    _OwEDS0090PulseCounter6_Type()
)
owEDS0090PulseCounter6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0090PulseCounter6.setStatus("current")
_OwEDS0090PulseCounter7_Type = Counter32
_OwEDS0090PulseCounter7_Object = MibTableColumn
owEDS0090PulseCounter7 = _OwEDS0090PulseCounter7_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 23, 1, 23),
    _OwEDS0090PulseCounter7_Type()
)
owEDS0090PulseCounter7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0090PulseCounter7.setStatus("current")
_OwEDS0090PulseCounter8_Type = Counter32
_OwEDS0090PulseCounter8_Object = MibTableColumn
owEDS0090PulseCounter8 = _OwEDS0090PulseCounter8_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 23, 1, 24),
    _OwEDS0090PulseCounter8_Type()
)
owEDS0090PulseCounter8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0090PulseCounter8.setStatus("current")


class _OwEDS0090Output1_Type(Integer32):
    """Custom type owEDS0090Output1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 0))
    )


_OwEDS0090Output1_Type.__name__ = "Integer32"
_OwEDS0090Output1_Object = MibTableColumn
owEDS0090Output1 = _OwEDS0090Output1_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 23, 1, 25),
    _OwEDS0090Output1_Type()
)
owEDS0090Output1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    owEDS0090Output1.setStatus("current")


class _OwEDS0090Output2_Type(Integer32):
    """Custom type owEDS0090Output2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 0))
    )


_OwEDS0090Output2_Type.__name__ = "Integer32"
_OwEDS0090Output2_Object = MibTableColumn
owEDS0090Output2 = _OwEDS0090Output2_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 23, 1, 26),
    _OwEDS0090Output2_Type()
)
owEDS0090Output2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    owEDS0090Output2.setStatus("current")


class _OwEDS0090Output3_Type(Integer32):
    """Custom type owEDS0090Output3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 0))
    )


_OwEDS0090Output3_Type.__name__ = "Integer32"
_OwEDS0090Output3_Object = MibTableColumn
owEDS0090Output3 = _OwEDS0090Output3_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 23, 1, 27),
    _OwEDS0090Output3_Type()
)
owEDS0090Output3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    owEDS0090Output3.setStatus("current")


class _OwEDS0090Output4_Type(Integer32):
    """Custom type owEDS0090Output4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 0))
    )


_OwEDS0090Output4_Type.__name__ = "Integer32"
_OwEDS0090Output4_Object = MibTableColumn
owEDS0090Output4 = _OwEDS0090Output4_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 23, 1, 28),
    _OwEDS0090Output4_Type()
)
owEDS0090Output4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    owEDS0090Output4.setStatus("current")


class _OwEDS0090Output5_Type(Integer32):
    """Custom type owEDS0090Output5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 0))
    )


_OwEDS0090Output5_Type.__name__ = "Integer32"
_OwEDS0090Output5_Object = MibTableColumn
owEDS0090Output5 = _OwEDS0090Output5_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 23, 1, 29),
    _OwEDS0090Output5_Type()
)
owEDS0090Output5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    owEDS0090Output5.setStatus("current")


class _OwEDS0090Output6_Type(Integer32):
    """Custom type owEDS0090Output6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 0))
    )


_OwEDS0090Output6_Type.__name__ = "Integer32"
_OwEDS0090Output6_Object = MibTableColumn
owEDS0090Output6 = _OwEDS0090Output6_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 23, 1, 30),
    _OwEDS0090Output6_Type()
)
owEDS0090Output6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    owEDS0090Output6.setStatus("current")


class _OwEDS0090Output7_Type(Integer32):
    """Custom type owEDS0090Output7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 0))
    )


_OwEDS0090Output7_Type.__name__ = "Integer32"
_OwEDS0090Output7_Object = MibTableColumn
owEDS0090Output7 = _OwEDS0090Output7_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 23, 1, 31),
    _OwEDS0090Output7_Type()
)
owEDS0090Output7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    owEDS0090Output7.setStatus("current")


class _OwEDS0090Output8_Type(Integer32):
    """Custom type owEDS0090Output8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 0))
    )


_OwEDS0090Output8_Type.__name__ = "Integer32"
_OwEDS0090Output8_Object = MibTableColumn
owEDS0090Output8 = _OwEDS0090Output8_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 23, 1, 32),
    _OwEDS0090Output8_Type()
)
owEDS0090Output8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    owEDS0090Output8.setStatus("current")


class _OwEDS0090PullDown1_Type(Integer32):
    """Custom type owEDS0090PullDown1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 0))
    )


_OwEDS0090PullDown1_Type.__name__ = "Integer32"
_OwEDS0090PullDown1_Object = MibTableColumn
owEDS0090PullDown1 = _OwEDS0090PullDown1_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 23, 1, 33),
    _OwEDS0090PullDown1_Type()
)
owEDS0090PullDown1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    owEDS0090PullDown1.setStatus("current")


class _OwEDS0090PullDown2_Type(Integer32):
    """Custom type owEDS0090PullDown2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 0))
    )


_OwEDS0090PullDown2_Type.__name__ = "Integer32"
_OwEDS0090PullDown2_Object = MibTableColumn
owEDS0090PullDown2 = _OwEDS0090PullDown2_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 23, 1, 34),
    _OwEDS0090PullDown2_Type()
)
owEDS0090PullDown2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    owEDS0090PullDown2.setStatus("current")


class _OwEDS0090PullDown3_Type(Integer32):
    """Custom type owEDS0090PullDown3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 0))
    )


_OwEDS0090PullDown3_Type.__name__ = "Integer32"
_OwEDS0090PullDown3_Object = MibTableColumn
owEDS0090PullDown3 = _OwEDS0090PullDown3_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 23, 1, 35),
    _OwEDS0090PullDown3_Type()
)
owEDS0090PullDown3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    owEDS0090PullDown3.setStatus("current")


class _OwEDS0090PullDown4_Type(Integer32):
    """Custom type owEDS0090PullDown4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 0))
    )


_OwEDS0090PullDown4_Type.__name__ = "Integer32"
_OwEDS0090PullDown4_Object = MibTableColumn
owEDS0090PullDown4 = _OwEDS0090PullDown4_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 23, 1, 36),
    _OwEDS0090PullDown4_Type()
)
owEDS0090PullDown4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    owEDS0090PullDown4.setStatus("current")


class _OwEDS0090PullDown5_Type(Integer32):
    """Custom type owEDS0090PullDown5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 0))
    )


_OwEDS0090PullDown5_Type.__name__ = "Integer32"
_OwEDS0090PullDown5_Object = MibTableColumn
owEDS0090PullDown5 = _OwEDS0090PullDown5_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 23, 1, 37),
    _OwEDS0090PullDown5_Type()
)
owEDS0090PullDown5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    owEDS0090PullDown5.setStatus("current")


class _OwEDS0090PullDown6_Type(Integer32):
    """Custom type owEDS0090PullDown6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 0))
    )


_OwEDS0090PullDown6_Type.__name__ = "Integer32"
_OwEDS0090PullDown6_Object = MibTableColumn
owEDS0090PullDown6 = _OwEDS0090PullDown6_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 23, 1, 38),
    _OwEDS0090PullDown6_Type()
)
owEDS0090PullDown6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    owEDS0090PullDown6.setStatus("current")


class _OwEDS0090PullDown7_Type(Integer32):
    """Custom type owEDS0090PullDown7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 0))
    )


_OwEDS0090PullDown7_Type.__name__ = "Integer32"
_OwEDS0090PullDown7_Object = MibTableColumn
owEDS0090PullDown7 = _OwEDS0090PullDown7_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 23, 1, 39),
    _OwEDS0090PullDown7_Type()
)
owEDS0090PullDown7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    owEDS0090PullDown7.setStatus("current")


class _OwEDS0090PullDown8_Type(Integer32):
    """Custom type owEDS0090PullDown8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 0))
    )


_OwEDS0090PullDown8_Type.__name__ = "Integer32"
_OwEDS0090PullDown8_Object = MibTableColumn
owEDS0090PullDown8 = _OwEDS0090PullDown8_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 23, 1, 40),
    _OwEDS0090PullDown8_Type()
)
owEDS0090PullDown8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    owEDS0090PullDown8.setStatus("current")


class _OwEDS0090ActivityLatchReset1_Type(Integer32):
    """Custom type owEDS0090ActivityLatchReset1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nofunction", 0),
          ("reset", 1))
    )


_OwEDS0090ActivityLatchReset1_Type.__name__ = "Integer32"
_OwEDS0090ActivityLatchReset1_Object = MibTableColumn
owEDS0090ActivityLatchReset1 = _OwEDS0090ActivityLatchReset1_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 23, 1, 41),
    _OwEDS0090ActivityLatchReset1_Type()
)
owEDS0090ActivityLatchReset1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    owEDS0090ActivityLatchReset1.setStatus("current")


class _OwEDS0090ActivityLatchReset2_Type(Integer32):
    """Custom type owEDS0090ActivityLatchReset2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nofunction", 0),
          ("reset", 1))
    )


_OwEDS0090ActivityLatchReset2_Type.__name__ = "Integer32"
_OwEDS0090ActivityLatchReset2_Object = MibTableColumn
owEDS0090ActivityLatchReset2 = _OwEDS0090ActivityLatchReset2_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 23, 1, 42),
    _OwEDS0090ActivityLatchReset2_Type()
)
owEDS0090ActivityLatchReset2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    owEDS0090ActivityLatchReset2.setStatus("current")


class _OwEDS0090ActivityLatchReset3_Type(Integer32):
    """Custom type owEDS0090ActivityLatchReset3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nofunction", 0),
          ("reset", 1))
    )


_OwEDS0090ActivityLatchReset3_Type.__name__ = "Integer32"
_OwEDS0090ActivityLatchReset3_Object = MibTableColumn
owEDS0090ActivityLatchReset3 = _OwEDS0090ActivityLatchReset3_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 23, 1, 43),
    _OwEDS0090ActivityLatchReset3_Type()
)
owEDS0090ActivityLatchReset3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    owEDS0090ActivityLatchReset3.setStatus("current")


class _OwEDS0090ActivityLatchReset4_Type(Integer32):
    """Custom type owEDS0090ActivityLatchReset4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nofunction", 0),
          ("reset", 1))
    )


_OwEDS0090ActivityLatchReset4_Type.__name__ = "Integer32"
_OwEDS0090ActivityLatchReset4_Object = MibTableColumn
owEDS0090ActivityLatchReset4 = _OwEDS0090ActivityLatchReset4_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 23, 1, 44),
    _OwEDS0090ActivityLatchReset4_Type()
)
owEDS0090ActivityLatchReset4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    owEDS0090ActivityLatchReset4.setStatus("current")


class _OwEDS0090ActivityLatchReset5_Type(Integer32):
    """Custom type owEDS0090ActivityLatchReset5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nofunction", 0),
          ("reset", 1))
    )


_OwEDS0090ActivityLatchReset5_Type.__name__ = "Integer32"
_OwEDS0090ActivityLatchReset5_Object = MibTableColumn
owEDS0090ActivityLatchReset5 = _OwEDS0090ActivityLatchReset5_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 23, 1, 45),
    _OwEDS0090ActivityLatchReset5_Type()
)
owEDS0090ActivityLatchReset5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    owEDS0090ActivityLatchReset5.setStatus("current")


class _OwEDS0090ActivityLatchReset6_Type(Integer32):
    """Custom type owEDS0090ActivityLatchReset6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nofunction", 0),
          ("reset", 1))
    )


_OwEDS0090ActivityLatchReset6_Type.__name__ = "Integer32"
_OwEDS0090ActivityLatchReset6_Object = MibTableColumn
owEDS0090ActivityLatchReset6 = _OwEDS0090ActivityLatchReset6_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 23, 1, 46),
    _OwEDS0090ActivityLatchReset6_Type()
)
owEDS0090ActivityLatchReset6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    owEDS0090ActivityLatchReset6.setStatus("current")


class _OwEDS0090ActivityLatchReset7_Type(Integer32):
    """Custom type owEDS0090ActivityLatchReset7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nofunction", 0),
          ("reset", 1))
    )


_OwEDS0090ActivityLatchReset7_Type.__name__ = "Integer32"
_OwEDS0090ActivityLatchReset7_Object = MibTableColumn
owEDS0090ActivityLatchReset7 = _OwEDS0090ActivityLatchReset7_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 23, 1, 47),
    _OwEDS0090ActivityLatchReset7_Type()
)
owEDS0090ActivityLatchReset7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    owEDS0090ActivityLatchReset7.setStatus("current")


class _OwEDS0090ActivityLatchReset8_Type(Integer32):
    """Custom type owEDS0090ActivityLatchReset8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nofunction", 0),
          ("reset", 1))
    )


_OwEDS0090ActivityLatchReset8_Type.__name__ = "Integer32"
_OwEDS0090ActivityLatchReset8_Object = MibTableColumn
owEDS0090ActivityLatchReset8 = _OwEDS0090ActivityLatchReset8_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 23, 1, 48),
    _OwEDS0090ActivityLatchReset8_Type()
)
owEDS0090ActivityLatchReset8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    owEDS0090ActivityLatchReset8.setStatus("current")


class _OwEDS0090PulseCounterReset1_Type(Integer32):
    """Custom type owEDS0090PulseCounterReset1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nofunction", 0),
          ("reset", 1))
    )


_OwEDS0090PulseCounterReset1_Type.__name__ = "Integer32"
_OwEDS0090PulseCounterReset1_Object = MibTableColumn
owEDS0090PulseCounterReset1 = _OwEDS0090PulseCounterReset1_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 23, 1, 49),
    _OwEDS0090PulseCounterReset1_Type()
)
owEDS0090PulseCounterReset1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    owEDS0090PulseCounterReset1.setStatus("current")


class _OwEDS0090PulseCounterReset2_Type(Integer32):
    """Custom type owEDS0090PulseCounterReset2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nofunction", 0),
          ("reset", 1))
    )


_OwEDS0090PulseCounterReset2_Type.__name__ = "Integer32"
_OwEDS0090PulseCounterReset2_Object = MibTableColumn
owEDS0090PulseCounterReset2 = _OwEDS0090PulseCounterReset2_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 23, 1, 50),
    _OwEDS0090PulseCounterReset2_Type()
)
owEDS0090PulseCounterReset2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    owEDS0090PulseCounterReset2.setStatus("current")


class _OwEDS0090PulseCounterReset3_Type(Integer32):
    """Custom type owEDS0090PulseCounterReset3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nofunction", 0),
          ("reset", 1))
    )


_OwEDS0090PulseCounterReset3_Type.__name__ = "Integer32"
_OwEDS0090PulseCounterReset3_Object = MibTableColumn
owEDS0090PulseCounterReset3 = _OwEDS0090PulseCounterReset3_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 23, 1, 51),
    _OwEDS0090PulseCounterReset3_Type()
)
owEDS0090PulseCounterReset3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    owEDS0090PulseCounterReset3.setStatus("current")


class _OwEDS0090PulseCounterReset4_Type(Integer32):
    """Custom type owEDS0090PulseCounterReset4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nofunction", 0),
          ("reset", 1))
    )


_OwEDS0090PulseCounterReset4_Type.__name__ = "Integer32"
_OwEDS0090PulseCounterReset4_Object = MibTableColumn
owEDS0090PulseCounterReset4 = _OwEDS0090PulseCounterReset4_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 23, 1, 52),
    _OwEDS0090PulseCounterReset4_Type()
)
owEDS0090PulseCounterReset4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    owEDS0090PulseCounterReset4.setStatus("current")


class _OwEDS0090PulseCounterReset5_Type(Integer32):
    """Custom type owEDS0090PulseCounterReset5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nofunction", 0),
          ("reset", 1))
    )


_OwEDS0090PulseCounterReset5_Type.__name__ = "Integer32"
_OwEDS0090PulseCounterReset5_Object = MibTableColumn
owEDS0090PulseCounterReset5 = _OwEDS0090PulseCounterReset5_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 23, 1, 53),
    _OwEDS0090PulseCounterReset5_Type()
)
owEDS0090PulseCounterReset5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    owEDS0090PulseCounterReset5.setStatus("current")


class _OwEDS0090PulseCounterReset6_Type(Integer32):
    """Custom type owEDS0090PulseCounterReset6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nofunction", 0),
          ("reset", 1))
    )


_OwEDS0090PulseCounterReset6_Type.__name__ = "Integer32"
_OwEDS0090PulseCounterReset6_Object = MibTableColumn
owEDS0090PulseCounterReset6 = _OwEDS0090PulseCounterReset6_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 23, 1, 54),
    _OwEDS0090PulseCounterReset6_Type()
)
owEDS0090PulseCounterReset6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    owEDS0090PulseCounterReset6.setStatus("current")


class _OwEDS0090PulseCounterReset7_Type(Integer32):
    """Custom type owEDS0090PulseCounterReset7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nofunction", 0),
          ("reset", 1))
    )


_OwEDS0090PulseCounterReset7_Type.__name__ = "Integer32"
_OwEDS0090PulseCounterReset7_Object = MibTableColumn
owEDS0090PulseCounterReset7 = _OwEDS0090PulseCounterReset7_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 23, 1, 55),
    _OwEDS0090PulseCounterReset7_Type()
)
owEDS0090PulseCounterReset7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    owEDS0090PulseCounterReset7.setStatus("current")


class _OwEDS0090PulseCounterReset8_Type(Integer32):
    """Custom type owEDS0090PulseCounterReset8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nofunction", 0),
          ("reset", 1))
    )


_OwEDS0090PulseCounterReset8_Type.__name__ = "Integer32"
_OwEDS0090PulseCounterReset8_Object = MibTableColumn
owEDS0090PulseCounterReset8 = _OwEDS0090PulseCounterReset8_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 23, 1, 56),
    _OwEDS0090PulseCounterReset8_Type()
)
owEDS0090PulseCounterReset8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    owEDS0090PulseCounterReset8.setStatus("current")
_OwEDS0090Counter_Type = Counter32
_OwEDS0090Counter_Object = MibTableColumn
owEDS0090Counter = _OwEDS0090Counter_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 23, 1, 57),
    _OwEDS0090Counter_Type()
)
owEDS0090Counter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0090Counter.setStatus("current")
_OwEDS0091Table_Object = MibTable
owEDS0091Table = _OwEDS0091Table_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 24)
)
if mibBuilder.loadTexts:
    owEDS0091Table.setStatus("current")
_OwEDS0091Entry_Object = MibTableRow
owEDS0091Entry = _OwEDS0091Entry_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 24, 1)
)
owEDS0091Entry.setIndexNames(
    (0, "EDS-MIB", "owDeviceIndex"),
)
if mibBuilder.loadTexts:
    owEDS0091Entry.setStatus("current")


class _OwEDS0091Input1_Type(Integer32):
    """Custom type owEDS0091Input1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_OwEDS0091Input1_Type.__name__ = "Integer32"
_OwEDS0091Input1_Object = MibTableColumn
owEDS0091Input1 = _OwEDS0091Input1_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 24, 1, 1),
    _OwEDS0091Input1_Type()
)
owEDS0091Input1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0091Input1.setStatus("current")


class _OwEDS0091Input2_Type(Integer32):
    """Custom type owEDS0091Input2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_OwEDS0091Input2_Type.__name__ = "Integer32"
_OwEDS0091Input2_Object = MibTableColumn
owEDS0091Input2 = _OwEDS0091Input2_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 24, 1, 2),
    _OwEDS0091Input2_Type()
)
owEDS0091Input2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0091Input2.setStatus("current")


class _OwEDS0091Input3_Type(Integer32):
    """Custom type owEDS0091Input3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_OwEDS0091Input3_Type.__name__ = "Integer32"
_OwEDS0091Input3_Object = MibTableColumn
owEDS0091Input3 = _OwEDS0091Input3_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 24, 1, 3),
    _OwEDS0091Input3_Type()
)
owEDS0091Input3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0091Input3.setStatus("current")


class _OwEDS0091Input4_Type(Integer32):
    """Custom type owEDS0091Input4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_OwEDS0091Input4_Type.__name__ = "Integer32"
_OwEDS0091Input4_Object = MibTableColumn
owEDS0091Input4 = _OwEDS0091Input4_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 24, 1, 4),
    _OwEDS0091Input4_Type()
)
owEDS0091Input4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0091Input4.setStatus("current")


class _OwEDS0091ActivityLatch1_Type(Integer32):
    """Custom type owEDS0091ActivityLatch1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_OwEDS0091ActivityLatch1_Type.__name__ = "Integer32"
_OwEDS0091ActivityLatch1_Object = MibTableColumn
owEDS0091ActivityLatch1 = _OwEDS0091ActivityLatch1_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 24, 1, 5),
    _OwEDS0091ActivityLatch1_Type()
)
owEDS0091ActivityLatch1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0091ActivityLatch1.setStatus("current")


class _OwEDS0091ActivityLatch2_Type(Integer32):
    """Custom type owEDS0091ActivityLatch2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_OwEDS0091ActivityLatch2_Type.__name__ = "Integer32"
_OwEDS0091ActivityLatch2_Object = MibTableColumn
owEDS0091ActivityLatch2 = _OwEDS0091ActivityLatch2_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 24, 1, 6),
    _OwEDS0091ActivityLatch2_Type()
)
owEDS0091ActivityLatch2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0091ActivityLatch2.setStatus("current")


class _OwEDS0091ActivityLatch3_Type(Integer32):
    """Custom type owEDS0091ActivityLatch3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_OwEDS0091ActivityLatch3_Type.__name__ = "Integer32"
_OwEDS0091ActivityLatch3_Object = MibTableColumn
owEDS0091ActivityLatch3 = _OwEDS0091ActivityLatch3_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 24, 1, 7),
    _OwEDS0091ActivityLatch3_Type()
)
owEDS0091ActivityLatch3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0091ActivityLatch3.setStatus("current")


class _OwEDS0091ActivityLatch4_Type(Integer32):
    """Custom type owEDS0091ActivityLatch4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_OwEDS0091ActivityLatch4_Type.__name__ = "Integer32"
_OwEDS0091ActivityLatch4_Object = MibTableColumn
owEDS0091ActivityLatch4 = _OwEDS0091ActivityLatch4_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 24, 1, 8),
    _OwEDS0091ActivityLatch4_Type()
)
owEDS0091ActivityLatch4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0091ActivityLatch4.setStatus("current")
_OwEDS0091PulseCounter1_Type = Counter32
_OwEDS0091PulseCounter1_Object = MibTableColumn
owEDS0091PulseCounter1 = _OwEDS0091PulseCounter1_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 24, 1, 9),
    _OwEDS0091PulseCounter1_Type()
)
owEDS0091PulseCounter1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0091PulseCounter1.setStatus("current")
_OwEDS0091PulseCounter2_Type = Counter32
_OwEDS0091PulseCounter2_Object = MibTableColumn
owEDS0091PulseCounter2 = _OwEDS0091PulseCounter2_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 24, 1, 10),
    _OwEDS0091PulseCounter2_Type()
)
owEDS0091PulseCounter2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0091PulseCounter2.setStatus("current")
_OwEDS0091PulseCounter3_Type = Counter32
_OwEDS0091PulseCounter3_Object = MibTableColumn
owEDS0091PulseCounter3 = _OwEDS0091PulseCounter3_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 24, 1, 11),
    _OwEDS0091PulseCounter3_Type()
)
owEDS0091PulseCounter3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0091PulseCounter3.setStatus("current")
_OwEDS0091PulseCounter4_Type = Counter32
_OwEDS0091PulseCounter4_Object = MibTableColumn
owEDS0091PulseCounter4 = _OwEDS0091PulseCounter4_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 24, 1, 12),
    _OwEDS0091PulseCounter4_Type()
)
owEDS0091PulseCounter4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0091PulseCounter4.setStatus("current")


class _OwEDS0091PulseCounterReset1_Type(Integer32):
    """Custom type owEDS0091PulseCounterReset1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_OwEDS0091PulseCounterReset1_Type.__name__ = "Integer32"
_OwEDS0091PulseCounterReset1_Object = MibTableColumn
owEDS0091PulseCounterReset1 = _OwEDS0091PulseCounterReset1_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 24, 1, 13),
    _OwEDS0091PulseCounterReset1_Type()
)
owEDS0091PulseCounterReset1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    owEDS0091PulseCounterReset1.setStatus("current")


class _OwEDS0091PulseCounterReset2_Type(Integer32):
    """Custom type owEDS0091PulseCounterReset2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_OwEDS0091PulseCounterReset2_Type.__name__ = "Integer32"
_OwEDS0091PulseCounterReset2_Object = MibTableColumn
owEDS0091PulseCounterReset2 = _OwEDS0091PulseCounterReset2_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 24, 1, 14),
    _OwEDS0091PulseCounterReset2_Type()
)
owEDS0091PulseCounterReset2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    owEDS0091PulseCounterReset2.setStatus("current")


class _OwEDS0091PulseCounterReset3_Type(Integer32):
    """Custom type owEDS0091PulseCounterReset3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_OwEDS0091PulseCounterReset3_Type.__name__ = "Integer32"
_OwEDS0091PulseCounterReset3_Object = MibTableColumn
owEDS0091PulseCounterReset3 = _OwEDS0091PulseCounterReset3_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 24, 1, 15),
    _OwEDS0091PulseCounterReset3_Type()
)
owEDS0091PulseCounterReset3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    owEDS0091PulseCounterReset3.setStatus("current")


class _OwEDS0091PulseCounterReset4_Type(Integer32):
    """Custom type owEDS0091PulseCounterReset4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_OwEDS0091PulseCounterReset4_Type.__name__ = "Integer32"
_OwEDS0091PulseCounterReset4_Object = MibTableColumn
owEDS0091PulseCounterReset4 = _OwEDS0091PulseCounterReset4_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 24, 1, 16),
    _OwEDS0091PulseCounterReset4_Type()
)
owEDS0091PulseCounterReset4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    owEDS0091PulseCounterReset4.setStatus("current")


class _OwEDS0091ActivityLatchReset1_Type(Integer32):
    """Custom type owEDS0091ActivityLatchReset1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_OwEDS0091ActivityLatchReset1_Type.__name__ = "Integer32"
_OwEDS0091ActivityLatchReset1_Object = MibTableColumn
owEDS0091ActivityLatchReset1 = _OwEDS0091ActivityLatchReset1_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 24, 1, 17),
    _OwEDS0091ActivityLatchReset1_Type()
)
owEDS0091ActivityLatchReset1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    owEDS0091ActivityLatchReset1.setStatus("current")


class _OwEDS0091ActivityLatchReset2_Type(Integer32):
    """Custom type owEDS0091ActivityLatchReset2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_OwEDS0091ActivityLatchReset2_Type.__name__ = "Integer32"
_OwEDS0091ActivityLatchReset2_Object = MibTableColumn
owEDS0091ActivityLatchReset2 = _OwEDS0091ActivityLatchReset2_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 24, 1, 18),
    _OwEDS0091ActivityLatchReset2_Type()
)
owEDS0091ActivityLatchReset2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    owEDS0091ActivityLatchReset2.setStatus("current")


class _OwEDS0091ActivityLatchReset3_Type(Integer32):
    """Custom type owEDS0091ActivityLatchReset3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_OwEDS0091ActivityLatchReset3_Type.__name__ = "Integer32"
_OwEDS0091ActivityLatchReset3_Object = MibTableColumn
owEDS0091ActivityLatchReset3 = _OwEDS0091ActivityLatchReset3_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 24, 1, 19),
    _OwEDS0091ActivityLatchReset3_Type()
)
owEDS0091ActivityLatchReset3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    owEDS0091ActivityLatchReset3.setStatus("current")


class _OwEDS0091ActivityLatchReset4_Type(Integer32):
    """Custom type owEDS0091ActivityLatchReset4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_OwEDS0091ActivityLatchReset4_Type.__name__ = "Integer32"
_OwEDS0091ActivityLatchReset4_Object = MibTableColumn
owEDS0091ActivityLatchReset4 = _OwEDS0091ActivityLatchReset4_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 24, 1, 20),
    _OwEDS0091ActivityLatchReset4_Type()
)
owEDS0091ActivityLatchReset4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    owEDS0091ActivityLatchReset4.setStatus("current")
_OwEDS0091Counter_Type = Counter32
_OwEDS0091Counter_Object = MibTableColumn
owEDS0091Counter = _OwEDS0091Counter_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 24, 1, 21),
    _OwEDS0091Counter_Type()
)
owEDS0091Counter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0091Counter.setStatus("current")
_OwEDS0092Table_Object = MibTable
owEDS0092Table = _OwEDS0092Table_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 25)
)
if mibBuilder.loadTexts:
    owEDS0092Table.setStatus("current")
_OwEDS0092Entry_Object = MibTableRow
owEDS0092Entry = _OwEDS0092Entry_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 25, 1)
)
owEDS0092Entry.setIndexNames(
    (0, "EDS-MIB", "owDeviceIndex"),
)
if mibBuilder.loadTexts:
    owEDS0092Entry.setStatus("current")


class _OwEDS0092Output1_Type(Integer32):
    """Custom type owEDS0092Output1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_OwEDS0092Output1_Type.__name__ = "Integer32"
_OwEDS0092Output1_Object = MibTableColumn
owEDS0092Output1 = _OwEDS0092Output1_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 25, 1, 1),
    _OwEDS0092Output1_Type()
)
owEDS0092Output1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0092Output1.setStatus("current")


class _OwEDS0092Output2_Type(Integer32):
    """Custom type owEDS0092Output2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_OwEDS0092Output2_Type.__name__ = "Integer32"
_OwEDS0092Output2_Object = MibTableColumn
owEDS0092Output2 = _OwEDS0092Output2_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 25, 1, 2),
    _OwEDS0092Output2_Type()
)
owEDS0092Output2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0092Output2.setStatus("current")


class _OwEDS0092Output3_Type(Integer32):
    """Custom type owEDS0092Output3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_OwEDS0092Output3_Type.__name__ = "Integer32"
_OwEDS0092Output3_Object = MibTableColumn
owEDS0092Output3 = _OwEDS0092Output3_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 25, 1, 3),
    _OwEDS0092Output3_Type()
)
owEDS0092Output3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0092Output3.setStatus("current")


class _OwEDS0092Output4_Type(Integer32):
    """Custom type owEDS0092Output4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_OwEDS0092Output4_Type.__name__ = "Integer32"
_OwEDS0092Output4_Object = MibTableColumn
owEDS0092Output4 = _OwEDS0092Output4_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 25, 1, 4),
    _OwEDS0092Output4_Type()
)
owEDS0092Output4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0092Output4.setStatus("current")
_OwEDS0092Counter_Type = Counter32
_OwEDS0092Counter_Object = MibTableColumn
owEDS0092Counter = _OwEDS0092Counter_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 25, 1, 5),
    _OwEDS0092Counter_Type()
)
owEDS0092Counter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0092Counter.setStatus("current")
_OwDS28EA00Table_Object = MibTable
owDS28EA00Table = _OwDS28EA00Table_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 26)
)
if mibBuilder.loadTexts:
    owDS28EA00Table.setStatus("current")
_OwDS28EA00Entry_Object = MibTableRow
owDS28EA00Entry = _OwDS28EA00Entry_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 26, 1)
)
owDS28EA00Entry.setIndexNames(
    (0, "EDS-MIB", "owDeviceIndex"),
)
if mibBuilder.loadTexts:
    owDS28EA00Entry.setStatus("current")
_OwDS28EA00Temperature_Type = DisplayString
_OwDS28EA00Temperature_Object = MibTableColumn
owDS28EA00Temperature = _OwDS28EA00Temperature_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 26, 1, 1),
    _OwDS28EA00Temperature_Type()
)
owDS28EA00Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owDS28EA00Temperature.setStatus("current")
_OwDS28EA00UserByte1_Type = Integer32
_OwDS28EA00UserByte1_Object = MibTableColumn
owDS28EA00UserByte1 = _OwDS28EA00UserByte1_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 26, 1, 2),
    _OwDS28EA00UserByte1_Type()
)
owDS28EA00UserByte1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    owDS28EA00UserByte1.setStatus("current")
_OwDS28EA00UserByte2_Type = Integer32
_OwDS28EA00UserByte2_Object = MibTableColumn
owDS28EA00UserByte2 = _OwDS28EA00UserByte2_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 26, 1, 3),
    _OwDS28EA00UserByte2_Type()
)
owDS28EA00UserByte2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    owDS28EA00UserByte2.setStatus("current")


class _OwDS28EA00PIOALevel_Type(Integer32):
    """Custom type owDS28EA00PIOALevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 0))
    )


_OwDS28EA00PIOALevel_Type.__name__ = "Integer32"
_OwDS28EA00PIOALevel_Object = MibTableColumn
owDS28EA00PIOALevel = _OwDS28EA00PIOALevel_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 26, 1, 4),
    _OwDS28EA00PIOALevel_Type()
)
owDS28EA00PIOALevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owDS28EA00PIOALevel.setStatus("current")


class _OwDS28EA00PIOBLevel_Type(Integer32):
    """Custom type owDS28EA00PIOBLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 0))
    )


_OwDS28EA00PIOBLevel_Type.__name__ = "Integer32"
_OwDS28EA00PIOBLevel_Object = MibTableColumn
owDS28EA00PIOBLevel = _OwDS28EA00PIOBLevel_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 26, 1, 5),
    _OwDS28EA00PIOBLevel_Type()
)
owDS28EA00PIOBLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owDS28EA00PIOBLevel.setStatus("current")


class _OwDS28EA00PIOAFlipFlop_Type(Integer32):
    """Custom type owDS28EA00PIOAFlipFlop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 0))
    )


_OwDS28EA00PIOAFlipFlop_Type.__name__ = "Integer32"
_OwDS28EA00PIOAFlipFlop_Object = MibTableColumn
owDS28EA00PIOAFlipFlop = _OwDS28EA00PIOAFlipFlop_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 26, 1, 6),
    _OwDS28EA00PIOAFlipFlop_Type()
)
owDS28EA00PIOAFlipFlop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    owDS28EA00PIOAFlipFlop.setStatus("current")


class _OwDS28EA00PIOBFlipFlop_Type(Integer32):
    """Custom type owDS28EA00PIOBFlipFlop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 0))
    )


_OwDS28EA00PIOBFlipFlop_Type.__name__ = "Integer32"
_OwDS28EA00PIOBFlipFlop_Object = MibTableColumn
owDS28EA00PIOBFlipFlop = _OwDS28EA00PIOBFlipFlop_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 26, 1, 7),
    _OwDS28EA00PIOBFlipFlop_Type()
)
owDS28EA00PIOBFlipFlop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    owDS28EA00PIOBFlipFlop.setStatus("current")
_OwEDS0050Table_Object = MibTable
owEDS0050Table = _OwEDS0050Table_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 27)
)
if mibBuilder.loadTexts:
    owEDS0050Table.setStatus("current")
_OwEDS0050Entry_Object = MibTableRow
owEDS0050Entry = _OwEDS0050Entry_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 27, 1)
)
owEDS0050Entry.setIndexNames(
    (0, "EDS-MIB", "owDeviceIndex"),
)
if mibBuilder.loadTexts:
    owEDS0050Entry.setStatus("current")
_OwEDS0050Temperature_Type = DisplayString
_OwEDS0050Temperature_Object = MibTableColumn
owEDS0050Temperature = _OwEDS0050Temperature_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 27, 1, 1),
    _OwEDS0050Temperature_Type()
)
owEDS0050Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0050Temperature.setStatus("current")
_OwEDS0050InputVoltage_Type = DisplayString
_OwEDS0050InputVoltage_Object = MibTableColumn
owEDS0050InputVoltage = _OwEDS0050InputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 27, 1, 2),
    _OwEDS0050InputVoltage_Type()
)
owEDS0050InputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0050InputVoltage.setStatus("current")


class _OwEDS0050Input1_Type(Integer32):
    """Custom type owEDS0050Input1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 0))
    )


_OwEDS0050Input1_Type.__name__ = "Integer32"
_OwEDS0050Input1_Object = MibTableColumn
owEDS0050Input1 = _OwEDS0050Input1_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 27, 1, 3),
    _OwEDS0050Input1_Type()
)
owEDS0050Input1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0050Input1.setStatus("current")


class _OwEDS0050Input2_Type(Integer32):
    """Custom type owEDS0050Input2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 0))
    )


_OwEDS0050Input2_Type.__name__ = "Integer32"
_OwEDS0050Input2_Object = MibTableColumn
owEDS0050Input2 = _OwEDS0050Input2_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 27, 1, 4),
    _OwEDS0050Input2_Type()
)
owEDS0050Input2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0050Input2.setStatus("current")


class _OwEDS0050ActivityLatch1_Type(Integer32):
    """Custom type owEDS0050ActivityLatch1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 0))
    )


_OwEDS0050ActivityLatch1_Type.__name__ = "Integer32"
_OwEDS0050ActivityLatch1_Object = MibTableColumn
owEDS0050ActivityLatch1 = _OwEDS0050ActivityLatch1_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 27, 1, 5),
    _OwEDS0050ActivityLatch1_Type()
)
owEDS0050ActivityLatch1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0050ActivityLatch1.setStatus("current")


class _OwEDS0050ActivityLatch2_Type(Integer32):
    """Custom type owEDS0050ActivityLatch2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 0))
    )


_OwEDS0050ActivityLatch2_Type.__name__ = "Integer32"
_OwEDS0050ActivityLatch2_Object = MibTableColumn
owEDS0050ActivityLatch2 = _OwEDS0050ActivityLatch2_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 27, 1, 6),
    _OwEDS0050ActivityLatch2_Type()
)
owEDS0050ActivityLatch2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    owEDS0050ActivityLatch2.setStatus("current")
_OwEDS0050PulseCounter1_Type = Counter32
_OwEDS0050PulseCounter1_Object = MibTableColumn
owEDS0050PulseCounter1 = _OwEDS0050PulseCounter1_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 27, 1, 7),
    _OwEDS0050PulseCounter1_Type()
)
owEDS0050PulseCounter1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    owEDS0050PulseCounter1.setStatus("current")
_OwEDS0050PulseCounter2_Type = Counter32
_OwEDS0050PulseCounter2_Object = MibTableColumn
owEDS0050PulseCounter2 = _OwEDS0050PulseCounter2_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 27, 1, 8),
    _OwEDS0050PulseCounter2_Type()
)
owEDS0050PulseCounter2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    owEDS0050PulseCounter2.setStatus("current")


class _OwEDS0050Output1_Type(Integer32):
    """Custom type owEDS0050Output1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 0))
    )


_OwEDS0050Output1_Type.__name__ = "Integer32"
_OwEDS0050Output1_Object = MibTableColumn
owEDS0050Output1 = _OwEDS0050Output1_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 27, 1, 9),
    _OwEDS0050Output1_Type()
)
owEDS0050Output1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    owEDS0050Output1.setStatus("current")


class _OwEDS0050Output2_Type(Integer32):
    """Custom type owEDS0050Output2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("high", 1),
          ("low", 0))
    )


_OwEDS0050Output2_Type.__name__ = "Integer32"
_OwEDS0050Output2_Object = MibTableColumn
owEDS0050Output2 = _OwEDS0050Output2_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 27, 1, 10),
    _OwEDS0050Output2_Type()
)
owEDS0050Output2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    owEDS0050Output2.setStatus("current")


class _OwEDS0050ActivityLatchReset1_Type(Integer32):
    """Custom type owEDS0050ActivityLatchReset1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nofunction", 0),
          ("reset", 1))
    )


_OwEDS0050ActivityLatchReset1_Type.__name__ = "Integer32"
_OwEDS0050ActivityLatchReset1_Object = MibTableColumn
owEDS0050ActivityLatchReset1 = _OwEDS0050ActivityLatchReset1_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 27, 1, 11),
    _OwEDS0050ActivityLatchReset1_Type()
)
owEDS0050ActivityLatchReset1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    owEDS0050ActivityLatchReset1.setStatus("current")


class _OwEDS0050ActivityLatchReset2_Type(Integer32):
    """Custom type owEDS0050ActivityLatchReset2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nofunction", 0),
          ("reset", 1))
    )


_OwEDS0050ActivityLatchReset2_Type.__name__ = "Integer32"
_OwEDS0050ActivityLatchReset2_Object = MibTableColumn
owEDS0050ActivityLatchReset2 = _OwEDS0050ActivityLatchReset2_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 27, 1, 12),
    _OwEDS0050ActivityLatchReset2_Type()
)
owEDS0050ActivityLatchReset2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    owEDS0050ActivityLatchReset2.setStatus("current")


class _OwEDS0050PulseCounterReset1_Type(Integer32):
    """Custom type owEDS0050PulseCounterReset1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_OwEDS0050PulseCounterReset1_Type.__name__ = "Integer32"
_OwEDS0050PulseCounterReset1_Object = MibTableColumn
owEDS0050PulseCounterReset1 = _OwEDS0050PulseCounterReset1_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 27, 1, 13),
    _OwEDS0050PulseCounterReset1_Type()
)
owEDS0050PulseCounterReset1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    owEDS0050PulseCounterReset1.setStatus("current")


class _OwEDS0050PulseCounterReset2_Type(Integer32):
    """Custom type owEDS0050PulseCounterReset2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_OwEDS0050PulseCounterReset2_Type.__name__ = "Integer32"
_OwEDS0050PulseCounterReset2_Object = MibTableColumn
owEDS0050PulseCounterReset2 = _OwEDS0050PulseCounterReset2_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 27, 1, 14),
    _OwEDS0050PulseCounterReset2_Type()
)
owEDS0050PulseCounterReset2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    owEDS0050PulseCounterReset2.setStatus("current")
_OwEDS0050Counter_Type = Counter32
_OwEDS0050Counter_Object = MibTableColumn
owEDS0050Counter = _OwEDS0050Counter_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 27, 1, 15),
    _OwEDS0050Counter_Type()
)
owEDS0050Counter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0050Counter.setStatus("current")
_OwEDS0001Table_Object = MibTable
owEDS0001Table = _OwEDS0001Table_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 28)
)
if mibBuilder.loadTexts:
    owEDS0001Table.setStatus("current")
_OwEDS0001Entry_Object = MibTableRow
owEDS0001Entry = _OwEDS0001Entry_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 28, 1)
)
owEDS0001Entry.setIndexNames(
    (0, "EDS-MIB", "owDeviceIndex"),
)
if mibBuilder.loadTexts:
    owEDS0001Entry.setStatus("current")
_OwEDS0001PollCount_Type = Counter32
_OwEDS0001PollCount_Object = MibTableColumn
owEDS0001PollCount = _OwEDS0001PollCount_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 28, 1, 1),
    _OwEDS0001PollCount_Type()
)
owEDS0001PollCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0001PollCount.setStatus("current")
_OwEDS0001DevicesConnected_Type = Counter32
_OwEDS0001DevicesConnected_Object = MibTableColumn
owEDS0001DevicesConnected = _OwEDS0001DevicesConnected_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 28, 1, 2),
    _OwEDS0001DevicesConnected_Type()
)
owEDS0001DevicesConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0001DevicesConnected.setStatus("current")
_OwEDS0001LoopTime_Type = DisplayString
_OwEDS0001LoopTime_Object = MibTableColumn
owEDS0001LoopTime = _OwEDS0001LoopTime_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 28, 1, 3),
    _OwEDS0001LoopTime_Type()
)
owEDS0001LoopTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0001LoopTime.setStatus("current")
_OwEDS0001DevicesConnectedChannel1_Type = Integer32
_OwEDS0001DevicesConnectedChannel1_Object = MibTableColumn
owEDS0001DevicesConnectedChannel1 = _OwEDS0001DevicesConnectedChannel1_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 28, 1, 4),
    _OwEDS0001DevicesConnectedChannel1_Type()
)
owEDS0001DevicesConnectedChannel1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0001DevicesConnectedChannel1.setStatus("current")
_OwEDS0001DevicesConnectedChannel2_Type = Integer32
_OwEDS0001DevicesConnectedChannel2_Object = MibTableColumn
owEDS0001DevicesConnectedChannel2 = _OwEDS0001DevicesConnectedChannel2_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 28, 1, 5),
    _OwEDS0001DevicesConnectedChannel2_Type()
)
owEDS0001DevicesConnectedChannel2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0001DevicesConnectedChannel2.setStatus("current")
_OwEDS0001DevicesConnectedChannel3_Type = Integer32
_OwEDS0001DevicesConnectedChannel3_Object = MibTableColumn
owEDS0001DevicesConnectedChannel3 = _OwEDS0001DevicesConnectedChannel3_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 28, 1, 6),
    _OwEDS0001DevicesConnectedChannel3_Type()
)
owEDS0001DevicesConnectedChannel3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0001DevicesConnectedChannel3.setStatus("current")
_OwEDS0001ErrorsChannel1_Type = Counter32
_OwEDS0001ErrorsChannel1_Object = MibTableColumn
owEDS0001ErrorsChannel1 = _OwEDS0001ErrorsChannel1_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 28, 1, 7),
    _OwEDS0001ErrorsChannel1_Type()
)
owEDS0001ErrorsChannel1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0001ErrorsChannel1.setStatus("current")
_OwEDS0001ErrorsChannel2_Type = Counter32
_OwEDS0001ErrorsChannel2_Object = MibTableColumn
owEDS0001ErrorsChannel2 = _OwEDS0001ErrorsChannel2_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 28, 1, 8),
    _OwEDS0001ErrorsChannel2_Type()
)
owEDS0001ErrorsChannel2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0001ErrorsChannel2.setStatus("current")
_OwEDS0001ErrorsChannel3_Type = Counter32
_OwEDS0001ErrorsChannel3_Object = MibTableColumn
owEDS0001ErrorsChannel3 = _OwEDS0001ErrorsChannel3_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 28, 1, 9),
    _OwEDS0001ErrorsChannel3_Type()
)
owEDS0001ErrorsChannel3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0001ErrorsChannel3.setStatus("current")
_OwEDS0001VoltageChannel1_Type = DisplayString
_OwEDS0001VoltageChannel1_Object = MibTableColumn
owEDS0001VoltageChannel1 = _OwEDS0001VoltageChannel1_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 28, 1, 10),
    _OwEDS0001VoltageChannel1_Type()
)
owEDS0001VoltageChannel1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0001VoltageChannel1.setStatus("current")
_OwEDS0001VoltageChannel2_Type = DisplayString
_OwEDS0001VoltageChannel2_Object = MibTableColumn
owEDS0001VoltageChannel2 = _OwEDS0001VoltageChannel2_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 28, 1, 11),
    _OwEDS0001VoltageChannel2_Type()
)
owEDS0001VoltageChannel2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0001VoltageChannel2.setStatus("current")
_OwEDS0001VoltageChannel3_Type = DisplayString
_OwEDS0001VoltageChannel3_Object = MibTableColumn
owEDS0001VoltageChannel3 = _OwEDS0001VoltageChannel3_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 28, 1, 12),
    _OwEDS0001VoltageChannel3_Type()
)
owEDS0001VoltageChannel3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0001VoltageChannel3.setStatus("current")
_OwEDS0001InputVoltage_Type = DisplayString
_OwEDS0001InputVoltage_Object = MibTableColumn
owEDS0001InputVoltage = _OwEDS0001InputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 28, 1, 13),
    _OwEDS0001InputVoltage_Type()
)
owEDS0001InputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0001InputVoltage.setStatus("current")
_OwEDS0001DeviceName_Type = DisplayString
_OwEDS0001DeviceName_Object = MibTableColumn
owEDS0001DeviceName = _OwEDS0001DeviceName_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 28, 1, 14),
    _OwEDS0001DeviceName_Type()
)
owEDS0001DeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0001DeviceName.setStatus("current")
_OwEDS0001HostName_Type = DisplayString
_OwEDS0001HostName_Object = MibTableColumn
owEDS0001HostName = _OwEDS0001HostName_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 28, 1, 15),
    _OwEDS0001HostName_Type()
)
owEDS0001HostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0001HostName.setStatus("current")
_OwEDS0001MACAddress_Type = DisplayString
_OwEDS0001MACAddress_Object = MibTableColumn
owEDS0001MACAddress = _OwEDS0001MACAddress_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 28, 1, 16),
    _OwEDS0001MACAddress_Type()
)
owEDS0001MACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0001MACAddress.setStatus("current")
_OwEDS0001TimeStamp_Type = DisplayString
_OwEDS0001TimeStamp_Object = MibTableColumn
owEDS0001TimeStamp = _OwEDS0001TimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 31440, 10, 28, 1, 17),
    _OwEDS0001TimeStamp_Type()
)
owEDS0001TimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    owEDS0001TimeStamp.setStatus("current")
_WDevices_ObjectIdentity = ObjectIdentity
wDevices = _WDevices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31440, 11)
)
_WDeviceTypes_ObjectIdentity = ObjectIdentity
wDeviceTypes = _WDeviceTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31440, 11, 1)
)
_WNone_ObjectIdentity = ObjectIdentity
wNone = _WNone_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31440, 11, 1, 0)
)
_WUnknown_ObjectIdentity = ObjectIdentity
wUnknown = _WUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31440, 11, 1, 1)
)
_WUnused1_ObjectIdentity = ObjectIdentity
wUnused1 = _WUnused1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31440, 11, 1, 2)
)
_WUnused2_ObjectIdentity = ObjectIdentity
wUnused2 = _WUnused2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31440, 11, 1, 3)
)
_WEDS1068_ObjectIdentity = ObjectIdentity
wEDS1068 = _WEDS1068_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31440, 11, 1, 4)
)
_WEDS1067_ObjectIdentity = ObjectIdentity
wEDS1067 = _WEDS1067_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31440, 11, 1, 5)
)
_WEDS1066_ObjectIdentity = ObjectIdentity
wEDS1066 = _WEDS1066_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31440, 11, 1, 6)
)
_WEDS1065_ObjectIdentity = ObjectIdentity
wEDS1065 = _WEDS1065_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31440, 11, 1, 7)
)
_WEDS1064_ObjectIdentity = ObjectIdentity
wEDS1064 = _WEDS1064_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31440, 11, 1, 8)
)
_WEDS1101_ObjectIdentity = ObjectIdentity
wEDS1101 = _WEDS1101_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31440, 11, 1, 9)
)
_WEDS2101_ObjectIdentity = ObjectIdentity
wEDS2101 = _WEDS2101_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31440, 11, 1, 10)
)
_WEDS3030_ObjectIdentity = ObjectIdentity
wEDS3030 = _WEDS3030_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31440, 11, 1, 11)
)
_WEDS3031_ObjectIdentity = ObjectIdentity
wEDS3031 = _WEDS3031_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31440, 11, 1, 12)
)
_WEDS3032_ObjectIdentity = ObjectIdentity
wEDS3032 = _WEDS3032_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31440, 11, 1, 13)
)
_WDeviceInfo_ObjectIdentity = ObjectIdentity
wDeviceInfo = _WDeviceInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31440, 11, 2)
)
_WDeviceNumActive_Type = Integer32
_WDeviceNumActive_Object = MibScalar
wDeviceNumActive = _WDeviceNumActive_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 2, 1),
    _WDeviceNumActive_Type()
)
wDeviceNumActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wDeviceNumActive.setStatus("current")
_WDeviceTable_Object = MibTable
wDeviceTable = _WDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 3)
)
if mibBuilder.loadTexts:
    wDeviceTable.setStatus("current")
_WDeviceEntry_Object = MibTableRow
wDeviceEntry = _WDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 3, 1)
)
wDeviceEntry.setIndexNames(
    (0, "EDS-MIB", "wDeviceIndex"),
)
if mibBuilder.loadTexts:
    wDeviceEntry.setStatus("current")


class _WDeviceIndex_Type(Integer32):
    """Custom type wDeviceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WDeviceIndex_Type.__name__ = "Integer32"
_WDeviceIndex_Object = MibTableColumn
wDeviceIndex = _WDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 3, 1, 1),
    _WDeviceIndex_Type()
)
wDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wDeviceIndex.setStatus("current")
_WDeviceType_Type = Integer32
_WDeviceType_Object = MibTableColumn
wDeviceType = _WDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 3, 1, 2),
    _WDeviceType_Type()
)
wDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wDeviceType.setStatus("current")
_WDeviceName_Type = DisplayString
_WDeviceName_Object = MibTableColumn
wDeviceName = _WDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 3, 1, 3),
    _WDeviceName_Type()
)
wDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wDeviceName.setStatus("current")
_WDeviceDescription_Type = DisplayString
_WDeviceDescription_Object = MibTableColumn
wDeviceDescription = _WDeviceDescription_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 3, 1, 4),
    _WDeviceDescription_Type()
)
wDeviceDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wDeviceDescription.setStatus("current")


class _WDeviceFamily_Type(OctetString):
    """Custom type wDeviceFamily based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_WDeviceFamily_Type.__name__ = "OctetString"
_WDeviceFamily_Object = MibTableColumn
wDeviceFamily = _WDeviceFamily_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 3, 1, 5),
    _WDeviceFamily_Type()
)
wDeviceFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wDeviceFamily.setStatus("current")


class _WDeviceEUI_Type(OctetString):
    """Custom type wDeviceEUI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_WDeviceEUI_Type.__name__ = "OctetString"
_WDeviceEUI_Object = MibTableColumn
wDeviceEUI = _WDeviceEUI_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 3, 1, 6),
    _WDeviceEUI_Type()
)
wDeviceEUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wDeviceEUI.setStatus("current")


class _WDeviceHealth_Type(Integer32):
    """Custom type wDeviceHealth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_WDeviceHealth_Type.__name__ = "Integer32"
_WDeviceHealth_Object = MibTableColumn
wDeviceHealth = _WDeviceHealth_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 3, 1, 7),
    _WDeviceHealth_Type()
)
wDeviceHealth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wDeviceHealth.setStatus("current")
_WDeviceTag_Type = DisplayString
_WDeviceTag_Object = MibTableColumn
wDeviceTag = _WDeviceTag_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 3, 1, 8),
    _WDeviceTag_Type()
)
wDeviceTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wDeviceTag.setStatus("current")
_WEDS1068Table_Object = MibTable
wEDS1068Table = _WEDS1068Table_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 4)
)
if mibBuilder.loadTexts:
    wEDS1068Table.setStatus("current")
_WEDS1068Entry_Object = MibTableRow
wEDS1068Entry = _WEDS1068Entry_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 4, 1)
)
wEDS1068Entry.setIndexNames(
    (0, "EDS-MIB", "wDeviceIndex"),
)
if mibBuilder.loadTexts:
    wEDS1068Entry.setStatus("current")
_WEDS1068Temperature_Type = DisplayString
_WEDS1068Temperature_Object = MibTableColumn
wEDS1068Temperature = _WEDS1068Temperature_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 4, 1, 1),
    _WEDS1068Temperature_Type()
)
wEDS1068Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS1068Temperature.setStatus("current")
_WEDS1068Humidity_Type = DisplayString
_WEDS1068Humidity_Object = MibTableColumn
wEDS1068Humidity = _WEDS1068Humidity_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 4, 1, 2),
    _WEDS1068Humidity_Type()
)
wEDS1068Humidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS1068Humidity.setStatus("current")
_WEDS1068DewPoint_Type = DisplayString
_WEDS1068DewPoint_Object = MibTableColumn
wEDS1068DewPoint = _WEDS1068DewPoint_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 4, 1, 3),
    _WEDS1068DewPoint_Type()
)
wEDS1068DewPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS1068DewPoint.setStatus("current")
_WEDS1068Humidex_Type = DisplayString
_WEDS1068Humidex_Object = MibTableColumn
wEDS1068Humidex = _WEDS1068Humidex_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 4, 1, 4),
    _WEDS1068Humidex_Type()
)
wEDS1068Humidex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS1068Humidex.setStatus("current")
_WEDS1068HeatIndex_Type = DisplayString
_WEDS1068HeatIndex_Object = MibTableColumn
wEDS1068HeatIndex = _WEDS1068HeatIndex_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 4, 1, 5),
    _WEDS1068HeatIndex_Type()
)
wEDS1068HeatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS1068HeatIndex.setStatus("current")
_WEDS1068BarometricPressure_Type = DisplayString
_WEDS1068BarometricPressure_Object = MibTableColumn
wEDS1068BarometricPressure = _WEDS1068BarometricPressure_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 4, 1, 6),
    _WEDS1068BarometricPressure_Type()
)
wEDS1068BarometricPressure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS1068BarometricPressure.setStatus("current")
_WEDS1068LEDState_Type = Integer32
_WEDS1068LEDState_Object = MibTableColumn
wEDS1068LEDState = _WEDS1068LEDState_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 4, 1, 7),
    _WEDS1068LEDState_Type()
)
wEDS1068LEDState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS1068LEDState.setStatus("current")
_WEDS1068RelayState_Type = Integer32
_WEDS1068RelayState_Object = MibTableColumn
wEDS1068RelayState = _WEDS1068RelayState_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 4, 1, 8),
    _WEDS1068RelayState_Type()
)
wEDS1068RelayState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS1068RelayState.setStatus("current")
_WEDS1068Light_Type = DisplayString
_WEDS1068Light_Object = MibTableColumn
wEDS1068Light = _WEDS1068Light_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 4, 1, 9),
    _WEDS1068Light_Type()
)
wEDS1068Light.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS1068Light.setStatus("current")
_WEDS1068Input1_Type = Integer32
_WEDS1068Input1_Object = MibTableColumn
wEDS1068Input1 = _WEDS1068Input1_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 4, 1, 10),
    _WEDS1068Input1_Type()
)
wEDS1068Input1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS1068Input1.setStatus("current")
_WEDS1068ActivityLatch1_Type = Integer32
_WEDS1068ActivityLatch1_Object = MibTableColumn
wEDS1068ActivityLatch1 = _WEDS1068ActivityLatch1_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 4, 1, 11),
    _WEDS1068ActivityLatch1_Type()
)
wEDS1068ActivityLatch1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS1068ActivityLatch1.setStatus("current")
_WEDS1068PulseCounter1_Type = Counter32
_WEDS1068PulseCounter1_Object = MibTableColumn
wEDS1068PulseCounter1 = _WEDS1068PulseCounter1_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 4, 1, 12),
    _WEDS1068PulseCounter1_Type()
)
wEDS1068PulseCounter1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS1068PulseCounter1.setStatus("current")
_WEDS1068Battery_Type = DisplayString
_WEDS1068Battery_Object = MibTableColumn
wEDS1068Battery = _WEDS1068Battery_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 4, 1, 13),
    _WEDS1068Battery_Type()
)
wEDS1068Battery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS1068Battery.setStatus("current")
_WEDS1068ReadCounter_Type = Counter32
_WEDS1068ReadCounter_Object = MibTableColumn
wEDS1068ReadCounter = _WEDS1068ReadCounter_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 4, 1, 14),
    _WEDS1068ReadCounter_Type()
)
wEDS1068ReadCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS1068ReadCounter.setStatus("current")
_WEDS1068LEDFunction_Type = Integer32
_WEDS1068LEDFunction_Object = MibTableColumn
wEDS1068LEDFunction = _WEDS1068LEDFunction_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 4, 1, 15),
    _WEDS1068LEDFunction_Type()
)
wEDS1068LEDFunction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wEDS1068LEDFunction.setStatus("current")
_WEDS1068RelayFunction_Type = Integer32
_WEDS1068RelayFunction_Object = MibTableColumn
wEDS1068RelayFunction = _WEDS1068RelayFunction_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 4, 1, 16),
    _WEDS1068RelayFunction_Type()
)
wEDS1068RelayFunction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wEDS1068RelayFunction.setStatus("current")
_WEDS1068LEDSetState_Type = Integer32
_WEDS1068LEDSetState_Object = MibTableColumn
wEDS1068LEDSetState = _WEDS1068LEDSetState_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 4, 1, 17),
    _WEDS1068LEDSetState_Type()
)
wEDS1068LEDSetState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wEDS1068LEDSetState.setStatus("current")
_WEDS1068RelaySetState_Type = Integer32
_WEDS1068RelaySetState_Object = MibTableColumn
wEDS1068RelaySetState = _WEDS1068RelaySetState_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 4, 1, 18),
    _WEDS1068RelaySetState_Type()
)
wEDS1068RelaySetState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wEDS1068RelaySetState.setStatus("current")
_WEDS1067Table_Object = MibTable
wEDS1067Table = _WEDS1067Table_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 5)
)
if mibBuilder.loadTexts:
    wEDS1067Table.setStatus("current")
_WEDS1067Entry_Object = MibTableRow
wEDS1067Entry = _WEDS1067Entry_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 5, 1)
)
wEDS1067Entry.setIndexNames(
    (0, "EDS-MIB", "wDeviceIndex"),
)
if mibBuilder.loadTexts:
    wEDS1067Entry.setStatus("current")
_WEDS1067Temperature_Type = DisplayString
_WEDS1067Temperature_Object = MibTableColumn
wEDS1067Temperature = _WEDS1067Temperature_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 5, 1, 1),
    _WEDS1067Temperature_Type()
)
wEDS1067Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS1067Temperature.setStatus("current")
_WEDS1067LEDState_Type = Integer32
_WEDS1067LEDState_Object = MibTableColumn
wEDS1067LEDState = _WEDS1067LEDState_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 5, 1, 2),
    _WEDS1067LEDState_Type()
)
wEDS1067LEDState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS1067LEDState.setStatus("current")
_WEDS1067RelayState_Type = Integer32
_WEDS1067RelayState_Object = MibTableColumn
wEDS1067RelayState = _WEDS1067RelayState_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 5, 1, 3),
    _WEDS1067RelayState_Type()
)
wEDS1067RelayState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS1067RelayState.setStatus("current")
_WEDS1067Light_Type = DisplayString
_WEDS1067Light_Object = MibTableColumn
wEDS1067Light = _WEDS1067Light_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 5, 1, 4),
    _WEDS1067Light_Type()
)
wEDS1067Light.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS1067Light.setStatus("current")
_WEDS1067Input1_Type = Integer32
_WEDS1067Input1_Object = MibTableColumn
wEDS1067Input1 = _WEDS1067Input1_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 5, 1, 5),
    _WEDS1067Input1_Type()
)
wEDS1067Input1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS1067Input1.setStatus("current")
_WEDS1067ActivityLatch1_Type = Integer32
_WEDS1067ActivityLatch1_Object = MibTableColumn
wEDS1067ActivityLatch1 = _WEDS1067ActivityLatch1_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 5, 1, 6),
    _WEDS1067ActivityLatch1_Type()
)
wEDS1067ActivityLatch1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS1067ActivityLatch1.setStatus("current")
_WEDS1067PulseCounter1_Type = Counter32
_WEDS1067PulseCounter1_Object = MibTableColumn
wEDS1067PulseCounter1 = _WEDS1067PulseCounter1_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 5, 1, 7),
    _WEDS1067PulseCounter1_Type()
)
wEDS1067PulseCounter1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS1067PulseCounter1.setStatus("current")
_WEDS1067Battery_Type = DisplayString
_WEDS1067Battery_Object = MibTableColumn
wEDS1067Battery = _WEDS1067Battery_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 5, 1, 8),
    _WEDS1067Battery_Type()
)
wEDS1067Battery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS1067Battery.setStatus("current")
_WEDS1067ReadCounter_Type = Counter32
_WEDS1067ReadCounter_Object = MibTableColumn
wEDS1067ReadCounter = _WEDS1067ReadCounter_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 5, 1, 9),
    _WEDS1067ReadCounter_Type()
)
wEDS1067ReadCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS1067ReadCounter.setStatus("current")
_WEDS1067LEDFunction_Type = Integer32
_WEDS1067LEDFunction_Object = MibTableColumn
wEDS1067LEDFunction = _WEDS1067LEDFunction_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 5, 1, 10),
    _WEDS1067LEDFunction_Type()
)
wEDS1067LEDFunction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wEDS1067LEDFunction.setStatus("current")
_WEDS1067RelayFunction_Type = Integer32
_WEDS1067RelayFunction_Object = MibTableColumn
wEDS1067RelayFunction = _WEDS1067RelayFunction_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 5, 1, 11),
    _WEDS1067RelayFunction_Type()
)
wEDS1067RelayFunction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wEDS1067RelayFunction.setStatus("current")
_WEDS1067LEDSetState_Type = Integer32
_WEDS1067LEDSetState_Object = MibTableColumn
wEDS1067LEDSetState = _WEDS1067LEDSetState_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 5, 1, 12),
    _WEDS1067LEDSetState_Type()
)
wEDS1067LEDSetState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wEDS1067LEDSetState.setStatus("current")
_WEDS1067RelaySetState_Type = Integer32
_WEDS1067RelaySetState_Object = MibTableColumn
wEDS1067RelaySetState = _WEDS1067RelaySetState_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 5, 1, 13),
    _WEDS1067RelaySetState_Type()
)
wEDS1067RelaySetState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wEDS1067RelaySetState.setStatus("current")
_WEDS1066Table_Object = MibTable
wEDS1066Table = _WEDS1066Table_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 6)
)
if mibBuilder.loadTexts:
    wEDS1066Table.setStatus("current")
_WEDS1066Entry_Object = MibTableRow
wEDS1066Entry = _WEDS1066Entry_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 6, 1)
)
wEDS1066Entry.setIndexNames(
    (0, "EDS-MIB", "wDeviceIndex"),
)
if mibBuilder.loadTexts:
    wEDS1066Entry.setStatus("current")
_WEDS1066Temperature_Type = DisplayString
_WEDS1066Temperature_Object = MibTableColumn
wEDS1066Temperature = _WEDS1066Temperature_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 6, 1, 1),
    _WEDS1066Temperature_Type()
)
wEDS1066Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS1066Temperature.setStatus("current")
_WEDS1066BarometricPressure_Type = DisplayString
_WEDS1066BarometricPressure_Object = MibTableColumn
wEDS1066BarometricPressure = _WEDS1066BarometricPressure_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 6, 1, 2),
    _WEDS1066BarometricPressure_Type()
)
wEDS1066BarometricPressure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS1066BarometricPressure.setStatus("current")
_WEDS1066LEDState_Type = Integer32
_WEDS1066LEDState_Object = MibTableColumn
wEDS1066LEDState = _WEDS1066LEDState_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 6, 1, 3),
    _WEDS1066LEDState_Type()
)
wEDS1066LEDState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS1066LEDState.setStatus("current")
_WEDS1066RelayState_Type = Integer32
_WEDS1066RelayState_Object = MibTableColumn
wEDS1066RelayState = _WEDS1066RelayState_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 6, 1, 4),
    _WEDS1066RelayState_Type()
)
wEDS1066RelayState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS1066RelayState.setStatus("current")
_WEDS1066Input1_Type = Integer32
_WEDS1066Input1_Object = MibTableColumn
wEDS1066Input1 = _WEDS1066Input1_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 6, 1, 5),
    _WEDS1066Input1_Type()
)
wEDS1066Input1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS1066Input1.setStatus("current")
_WEDS1066ActivityLatch1_Type = Integer32
_WEDS1066ActivityLatch1_Object = MibTableColumn
wEDS1066ActivityLatch1 = _WEDS1066ActivityLatch1_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 6, 1, 6),
    _WEDS1066ActivityLatch1_Type()
)
wEDS1066ActivityLatch1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS1066ActivityLatch1.setStatus("current")
_WEDS1066PulseCounter1_Type = Counter32
_WEDS1066PulseCounter1_Object = MibTableColumn
wEDS1066PulseCounter1 = _WEDS1066PulseCounter1_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 6, 1, 7),
    _WEDS1066PulseCounter1_Type()
)
wEDS1066PulseCounter1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS1066PulseCounter1.setStatus("current")
_WEDS1066Battery_Type = DisplayString
_WEDS1066Battery_Object = MibTableColumn
wEDS1066Battery = _WEDS1066Battery_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 6, 1, 8),
    _WEDS1066Battery_Type()
)
wEDS1066Battery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS1066Battery.setStatus("current")
_WEDS1066ReadCounter_Type = Counter32
_WEDS1066ReadCounter_Object = MibTableColumn
wEDS1066ReadCounter = _WEDS1066ReadCounter_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 6, 1, 9),
    _WEDS1066ReadCounter_Type()
)
wEDS1066ReadCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS1066ReadCounter.setStatus("current")
_WEDS1066LEDFunction_Type = Integer32
_WEDS1066LEDFunction_Object = MibTableColumn
wEDS1066LEDFunction = _WEDS1066LEDFunction_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 6, 1, 10),
    _WEDS1066LEDFunction_Type()
)
wEDS1066LEDFunction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wEDS1066LEDFunction.setStatus("current")
_WEDS1066RelayFunction_Type = Integer32
_WEDS1066RelayFunction_Object = MibTableColumn
wEDS1066RelayFunction = _WEDS1066RelayFunction_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 6, 1, 11),
    _WEDS1066RelayFunction_Type()
)
wEDS1066RelayFunction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wEDS1066RelayFunction.setStatus("current")
_WEDS1066LEDSetState_Type = Integer32
_WEDS1066LEDSetState_Object = MibTableColumn
wEDS1066LEDSetState = _WEDS1066LEDSetState_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 6, 1, 12),
    _WEDS1066LEDSetState_Type()
)
wEDS1066LEDSetState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wEDS1066LEDSetState.setStatus("current")
_WEDS1066RelaySetState_Type = Integer32
_WEDS1066RelaySetState_Object = MibTableColumn
wEDS1066RelaySetState = _WEDS1066RelaySetState_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 6, 1, 13),
    _WEDS1066RelaySetState_Type()
)
wEDS1066RelaySetState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wEDS1066RelaySetState.setStatus("current")
_WEDS1065Table_Object = MibTable
wEDS1065Table = _WEDS1065Table_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 7)
)
if mibBuilder.loadTexts:
    wEDS1065Table.setStatus("current")
_WEDS1065Entry_Object = MibTableRow
wEDS1065Entry = _WEDS1065Entry_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 7, 1)
)
wEDS1065Entry.setIndexNames(
    (0, "EDS-MIB", "wDeviceIndex"),
)
if mibBuilder.loadTexts:
    wEDS1065Entry.setStatus("current")
_WEDS1065Temperature_Type = DisplayString
_WEDS1065Temperature_Object = MibTableColumn
wEDS1065Temperature = _WEDS1065Temperature_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 7, 1, 1),
    _WEDS1065Temperature_Type()
)
wEDS1065Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS1065Temperature.setStatus("current")
_WEDS1065Humidity_Type = DisplayString
_WEDS1065Humidity_Object = MibTableColumn
wEDS1065Humidity = _WEDS1065Humidity_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 7, 1, 2),
    _WEDS1065Humidity_Type()
)
wEDS1065Humidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS1065Humidity.setStatus("current")
_WEDS1065DewPoint_Type = DisplayString
_WEDS1065DewPoint_Object = MibTableColumn
wEDS1065DewPoint = _WEDS1065DewPoint_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 7, 1, 3),
    _WEDS1065DewPoint_Type()
)
wEDS1065DewPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS1065DewPoint.setStatus("current")
_WEDS1065Humidex_Type = DisplayString
_WEDS1065Humidex_Object = MibTableColumn
wEDS1065Humidex = _WEDS1065Humidex_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 7, 1, 4),
    _WEDS1065Humidex_Type()
)
wEDS1065Humidex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS1065Humidex.setStatus("current")
_WEDS1065HeatIndex_Type = DisplayString
_WEDS1065HeatIndex_Object = MibTableColumn
wEDS1065HeatIndex = _WEDS1065HeatIndex_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 7, 1, 5),
    _WEDS1065HeatIndex_Type()
)
wEDS1065HeatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS1065HeatIndex.setStatus("current")
_WEDS1065LEDState_Type = Integer32
_WEDS1065LEDState_Object = MibTableColumn
wEDS1065LEDState = _WEDS1065LEDState_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 7, 1, 6),
    _WEDS1065LEDState_Type()
)
wEDS1065LEDState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS1065LEDState.setStatus("current")
_WEDS1065RelayState_Type = Integer32
_WEDS1065RelayState_Object = MibTableColumn
wEDS1065RelayState = _WEDS1065RelayState_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 7, 1, 7),
    _WEDS1065RelayState_Type()
)
wEDS1065RelayState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS1065RelayState.setStatus("current")
_WEDS1065Input1_Type = Integer32
_WEDS1065Input1_Object = MibTableColumn
wEDS1065Input1 = _WEDS1065Input1_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 7, 1, 8),
    _WEDS1065Input1_Type()
)
wEDS1065Input1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS1065Input1.setStatus("current")
_WEDS1065ActivityLatch1_Type = Integer32
_WEDS1065ActivityLatch1_Object = MibTableColumn
wEDS1065ActivityLatch1 = _WEDS1065ActivityLatch1_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 7, 1, 9),
    _WEDS1065ActivityLatch1_Type()
)
wEDS1065ActivityLatch1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS1065ActivityLatch1.setStatus("current")
_WEDS1065PulseCounter1_Type = Counter32
_WEDS1065PulseCounter1_Object = MibTableColumn
wEDS1065PulseCounter1 = _WEDS1065PulseCounter1_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 7, 1, 10),
    _WEDS1065PulseCounter1_Type()
)
wEDS1065PulseCounter1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS1065PulseCounter1.setStatus("current")
_WEDS1065Battery_Type = DisplayString
_WEDS1065Battery_Object = MibTableColumn
wEDS1065Battery = _WEDS1065Battery_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 7, 1, 11),
    _WEDS1065Battery_Type()
)
wEDS1065Battery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS1065Battery.setStatus("current")
_WEDS1065ReadCounter_Type = Counter32
_WEDS1065ReadCounter_Object = MibTableColumn
wEDS1065ReadCounter = _WEDS1065ReadCounter_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 7, 1, 12),
    _WEDS1065ReadCounter_Type()
)
wEDS1065ReadCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS1065ReadCounter.setStatus("current")
_WEDS1065LEDFunction_Type = Integer32
_WEDS1065LEDFunction_Object = MibTableColumn
wEDS1065LEDFunction = _WEDS1065LEDFunction_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 7, 1, 13),
    _WEDS1065LEDFunction_Type()
)
wEDS1065LEDFunction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wEDS1065LEDFunction.setStatus("current")
_WEDS1065RelayFunction_Type = Integer32
_WEDS1065RelayFunction_Object = MibTableColumn
wEDS1065RelayFunction = _WEDS1065RelayFunction_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 7, 1, 14),
    _WEDS1065RelayFunction_Type()
)
wEDS1065RelayFunction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wEDS1065RelayFunction.setStatus("current")
_WEDS1065LEDSetState_Type = Integer32
_WEDS1065LEDSetState_Object = MibTableColumn
wEDS1065LEDSetState = _WEDS1065LEDSetState_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 7, 1, 15),
    _WEDS1065LEDSetState_Type()
)
wEDS1065LEDSetState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wEDS1065LEDSetState.setStatus("current")
_WEDS1065RelaySetState_Type = Integer32
_WEDS1065RelaySetState_Object = MibTableColumn
wEDS1065RelaySetState = _WEDS1065RelaySetState_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 7, 1, 16),
    _WEDS1065RelaySetState_Type()
)
wEDS1065RelaySetState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wEDS1065RelaySetState.setStatus("current")
_WEDS1064Table_Object = MibTable
wEDS1064Table = _WEDS1064Table_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 8)
)
if mibBuilder.loadTexts:
    wEDS1064Table.setStatus("current")
_WEDS1064Entry_Object = MibTableRow
wEDS1064Entry = _WEDS1064Entry_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 8, 1)
)
wEDS1064Entry.setIndexNames(
    (0, "EDS-MIB", "wDeviceIndex"),
)
if mibBuilder.loadTexts:
    wEDS1064Entry.setStatus("current")
_WEDS1064Temperature_Type = DisplayString
_WEDS1064Temperature_Object = MibTableColumn
wEDS1064Temperature = _WEDS1064Temperature_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 8, 1, 1),
    _WEDS1064Temperature_Type()
)
wEDS1064Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS1064Temperature.setStatus("current")
_WEDS1064LEDState_Type = Integer32
_WEDS1064LEDState_Object = MibTableColumn
wEDS1064LEDState = _WEDS1064LEDState_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 8, 1, 2),
    _WEDS1064LEDState_Type()
)
wEDS1064LEDState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS1064LEDState.setStatus("current")
_WEDS1064RelayState_Type = Integer32
_WEDS1064RelayState_Object = MibTableColumn
wEDS1064RelayState = _WEDS1064RelayState_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 8, 1, 3),
    _WEDS1064RelayState_Type()
)
wEDS1064RelayState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS1064RelayState.setStatus("current")
_WEDS1064Input1_Type = Integer32
_WEDS1064Input1_Object = MibTableColumn
wEDS1064Input1 = _WEDS1064Input1_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 8, 1, 4),
    _WEDS1064Input1_Type()
)
wEDS1064Input1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS1064Input1.setStatus("current")
_WEDS1064ActivityLatch1_Type = Integer32
_WEDS1064ActivityLatch1_Object = MibTableColumn
wEDS1064ActivityLatch1 = _WEDS1064ActivityLatch1_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 8, 1, 5),
    _WEDS1064ActivityLatch1_Type()
)
wEDS1064ActivityLatch1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS1064ActivityLatch1.setStatus("current")
_WEDS1064PulseCounter1_Type = Counter32
_WEDS1064PulseCounter1_Object = MibTableColumn
wEDS1064PulseCounter1 = _WEDS1064PulseCounter1_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 8, 1, 6),
    _WEDS1064PulseCounter1_Type()
)
wEDS1064PulseCounter1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS1064PulseCounter1.setStatus("current")
_WEDS1064Battery_Type = DisplayString
_WEDS1064Battery_Object = MibTableColumn
wEDS1064Battery = _WEDS1064Battery_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 8, 1, 7),
    _WEDS1064Battery_Type()
)
wEDS1064Battery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS1064Battery.setStatus("current")
_WEDS1064ReadCounter_Type = Counter32
_WEDS1064ReadCounter_Object = MibTableColumn
wEDS1064ReadCounter = _WEDS1064ReadCounter_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 8, 1, 8),
    _WEDS1064ReadCounter_Type()
)
wEDS1064ReadCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS1064ReadCounter.setStatus("current")
_WEDS1064LEDFunction_Type = Integer32
_WEDS1064LEDFunction_Object = MibTableColumn
wEDS1064LEDFunction = _WEDS1064LEDFunction_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 8, 1, 9),
    _WEDS1064LEDFunction_Type()
)
wEDS1064LEDFunction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wEDS1064LEDFunction.setStatus("current")
_WEDS1064RelayFunction_Type = Integer32
_WEDS1064RelayFunction_Object = MibTableColumn
wEDS1064RelayFunction = _WEDS1064RelayFunction_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 8, 1, 10),
    _WEDS1064RelayFunction_Type()
)
wEDS1064RelayFunction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wEDS1064RelayFunction.setStatus("current")
_WEDS1064LEDSetState_Type = Integer32
_WEDS1064LEDSetState_Object = MibTableColumn
wEDS1064LEDSetState = _WEDS1064LEDSetState_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 8, 1, 11),
    _WEDS1064LEDSetState_Type()
)
wEDS1064LEDSetState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wEDS1064LEDSetState.setStatus("current")
_WEDS1064RelaySetState_Type = Integer32
_WEDS1064RelaySetState_Object = MibTableColumn
wEDS1064RelaySetState = _WEDS1064RelaySetState_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 8, 1, 12),
    _WEDS1064RelaySetState_Type()
)
wEDS1064RelaySetState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wEDS1064RelaySetState.setStatus("current")
_WEDS1101Table_Object = MibTable
wEDS1101Table = _WEDS1101Table_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 9)
)
if mibBuilder.loadTexts:
    wEDS1101Table.setStatus("current")
_WEDS1101Entry_Object = MibTableRow
wEDS1101Entry = _WEDS1101Entry_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 9, 1)
)
wEDS1101Entry.setIndexNames(
    (0, "EDS-MIB", "wDeviceIndex"),
)
if mibBuilder.loadTexts:
    wEDS1101Entry.setStatus("current")
_WEDS1101DevicesConnected_Type = Integer32
_WEDS1101DevicesConnected_Object = MibTableColumn
wEDS1101DevicesConnected = _WEDS1101DevicesConnected_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 9, 1, 1),
    _WEDS1101DevicesConnected_Type()
)
wEDS1101DevicesConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS1101DevicesConnected.setStatus("current")
_WEDS1101SendCounter_Type = Counter32
_WEDS1101SendCounter_Object = MibTableColumn
wEDS1101SendCounter = _WEDS1101SendCounter_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 9, 1, 2),
    _WEDS1101SendCounter_Type()
)
wEDS1101SendCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS1101SendCounter.setStatus("current")
_WEDS2101Table_Object = MibTable
wEDS2101Table = _WEDS2101Table_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 10)
)
if mibBuilder.loadTexts:
    wEDS2101Table.setStatus("current")
_WEDS2101Entry_Object = MibTableRow
wEDS2101Entry = _WEDS2101Entry_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 10, 1)
)
wEDS2101Entry.setIndexNames(
    (0, "EDS-MIB", "wDeviceIndex"),
)
if mibBuilder.loadTexts:
    wEDS2101Entry.setStatus("current")
_WEDS2101DevicesConnected_Type = Integer32
_WEDS2101DevicesConnected_Object = MibTableColumn
wEDS2101DevicesConnected = _WEDS2101DevicesConnected_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 10, 1, 1),
    _WEDS2101DevicesConnected_Type()
)
wEDS2101DevicesConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS2101DevicesConnected.setStatus("current")
_WEDS2101SendCounter_Type = Counter32
_WEDS2101SendCounter_Object = MibTableColumn
wEDS2101SendCounter = _WEDS2101SendCounter_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 10, 1, 2),
    _WEDS2101SendCounter_Type()
)
wEDS2101SendCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS2101SendCounter.setStatus("current")
_WEDS3030Table_Object = MibTable
wEDS3030Table = _WEDS3030Table_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 11)
)
if mibBuilder.loadTexts:
    wEDS3030Table.setStatus("current")
_WEDS3030Entry_Object = MibTableRow
wEDS3030Entry = _WEDS3030Entry_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 11, 1)
)
wEDS3030Entry.setIndexNames(
    (0, "EDS-MIB", "wDeviceIndex"),
)
if mibBuilder.loadTexts:
    wEDS3030Entry.setStatus("current")
_WEDS3030Temperature_Type = DisplayString
_WEDS3030Temperature_Object = MibTableColumn
wEDS3030Temperature = _WEDS3030Temperature_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 11, 1, 1),
    _WEDS3030Temperature_Type()
)
wEDS3030Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS3030Temperature.setStatus("current")
_WEDS3030Probe_Type = DisplayString
_WEDS3030Probe_Object = MibTableColumn
wEDS3030Probe = _WEDS3030Probe_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 11, 1, 2),
    _WEDS3030Probe_Type()
)
wEDS3030Probe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS3030Probe.setStatus("current")
_WEDS3030LEDState_Type = Integer32
_WEDS3030LEDState_Object = MibTableColumn
wEDS3030LEDState = _WEDS3030LEDState_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 11, 1, 3),
    _WEDS3030LEDState_Type()
)
wEDS3030LEDState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS3030LEDState.setStatus("current")
_WEDS3030Light_Type = DisplayString
_WEDS3030Light_Object = MibTableColumn
wEDS3030Light = _WEDS3030Light_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 11, 1, 4),
    _WEDS3030Light_Type()
)
wEDS3030Light.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS3030Light.setStatus("current")
_WEDS3030Input1_Type = Integer32
_WEDS3030Input1_Object = MibTableColumn
wEDS3030Input1 = _WEDS3030Input1_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 11, 1, 5),
    _WEDS3030Input1_Type()
)
wEDS3030Input1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS3030Input1.setStatus("current")
_WEDS3030ActivityLatch1_Type = Integer32
_WEDS3030ActivityLatch1_Object = MibTableColumn
wEDS3030ActivityLatch1 = _WEDS3030ActivityLatch1_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 11, 1, 6),
    _WEDS3030ActivityLatch1_Type()
)
wEDS3030ActivityLatch1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS3030ActivityLatch1.setStatus("current")
_WEDS3030PulseCounter1_Type = Counter32
_WEDS3030PulseCounter1_Object = MibTableColumn
wEDS3030PulseCounter1 = _WEDS3030PulseCounter1_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 11, 1, 7),
    _WEDS3030PulseCounter1_Type()
)
wEDS3030PulseCounter1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS3030PulseCounter1.setStatus("current")
_WEDS3030Battery_Type = DisplayString
_WEDS3030Battery_Object = MibTableColumn
wEDS3030Battery = _WEDS3030Battery_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 11, 1, 8),
    _WEDS3030Battery_Type()
)
wEDS3030Battery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS3030Battery.setStatus("current")
_WEDS3030ReadCounter_Type = Counter32
_WEDS3030ReadCounter_Object = MibTableColumn
wEDS3030ReadCounter = _WEDS3030ReadCounter_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 11, 1, 9),
    _WEDS3030ReadCounter_Type()
)
wEDS3030ReadCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS3030ReadCounter.setStatus("current")
_WEDS3030LEDFunction_Type = Integer32
_WEDS3030LEDFunction_Object = MibTableColumn
wEDS3030LEDFunction = _WEDS3030LEDFunction_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 11, 1, 10),
    _WEDS3030LEDFunction_Type()
)
wEDS3030LEDFunction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wEDS3030LEDFunction.setStatus("current")
_WEDS3030LEDSetState_Type = Integer32
_WEDS3030LEDSetState_Object = MibTableColumn
wEDS3030LEDSetState = _WEDS3030LEDSetState_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 11, 1, 11),
    _WEDS3030LEDSetState_Type()
)
wEDS3030LEDSetState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wEDS3030LEDSetState.setStatus("current")
_WEDS3031Table_Object = MibTable
wEDS3031Table = _WEDS3031Table_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 12)
)
if mibBuilder.loadTexts:
    wEDS3031Table.setStatus("current")
_WEDS3031Entry_Object = MibTableRow
wEDS3031Entry = _WEDS3031Entry_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 12, 1)
)
wEDS3031Entry.setIndexNames(
    (0, "EDS-MIB", "wDeviceIndex"),
)
if mibBuilder.loadTexts:
    wEDS3031Entry.setStatus("current")
_WEDS3031Temperature_Type = DisplayString
_WEDS3031Temperature_Object = MibTableColumn
wEDS3031Temperature = _WEDS3031Temperature_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 12, 1, 1),
    _WEDS3031Temperature_Type()
)
wEDS3031Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS3031Temperature.setStatus("current")
_WEDS3031RTDTemperature_Type = DisplayString
_WEDS3031RTDTemperature_Object = MibTableColumn
wEDS3031RTDTemperature = _WEDS3031RTDTemperature_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 12, 1, 2),
    _WEDS3031RTDTemperature_Type()
)
wEDS3031RTDTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS3031RTDTemperature.setStatus("current")
_WEDS3031LEDState_Type = Integer32
_WEDS3031LEDState_Object = MibTableColumn
wEDS3031LEDState = _WEDS3031LEDState_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 12, 1, 3),
    _WEDS3031LEDState_Type()
)
wEDS3031LEDState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS3031LEDState.setStatus("current")
_WEDS3031Input1_Type = Integer32
_WEDS3031Input1_Object = MibTableColumn
wEDS3031Input1 = _WEDS3031Input1_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 12, 1, 4),
    _WEDS3031Input1_Type()
)
wEDS3031Input1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS3031Input1.setStatus("current")
_WEDS3031ActivityLatch1_Type = Integer32
_WEDS3031ActivityLatch1_Object = MibTableColumn
wEDS3031ActivityLatch1 = _WEDS3031ActivityLatch1_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 12, 1, 5),
    _WEDS3031ActivityLatch1_Type()
)
wEDS3031ActivityLatch1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS3031ActivityLatch1.setStatus("current")
_WEDS3031PulseCounter1_Type = Counter32
_WEDS3031PulseCounter1_Object = MibTableColumn
wEDS3031PulseCounter1 = _WEDS3031PulseCounter1_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 12, 1, 6),
    _WEDS3031PulseCounter1_Type()
)
wEDS3031PulseCounter1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS3031PulseCounter1.setStatus("current")
_WEDS3031Battery_Type = DisplayString
_WEDS3031Battery_Object = MibTableColumn
wEDS3031Battery = _WEDS3031Battery_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 12, 1, 7),
    _WEDS3031Battery_Type()
)
wEDS3031Battery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS3031Battery.setStatus("current")
_WEDS3031ReadCounter_Type = Counter32
_WEDS3031ReadCounter_Object = MibTableColumn
wEDS3031ReadCounter = _WEDS3031ReadCounter_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 12, 1, 8),
    _WEDS3031ReadCounter_Type()
)
wEDS3031ReadCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS3031ReadCounter.setStatus("current")
_WEDS3031LEDFunction_Type = Integer32
_WEDS3031LEDFunction_Object = MibTableColumn
wEDS3031LEDFunction = _WEDS3031LEDFunction_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 12, 1, 9),
    _WEDS3031LEDFunction_Type()
)
wEDS3031LEDFunction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wEDS3031LEDFunction.setStatus("current")
_WEDS3031LEDSetState_Type = Integer32
_WEDS3031LEDSetState_Object = MibTableColumn
wEDS3031LEDSetState = _WEDS3031LEDSetState_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 12, 1, 10),
    _WEDS3031LEDSetState_Type()
)
wEDS3031LEDSetState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wEDS3031LEDSetState.setStatus("current")
_WEDS3032Table_Object = MibTable
wEDS3032Table = _WEDS3032Table_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 13)
)
if mibBuilder.loadTexts:
    wEDS3032Table.setStatus("current")
_WEDS3032Entry_Object = MibTableRow
wEDS3032Entry = _WEDS3032Entry_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 13, 1)
)
wEDS3032Entry.setIndexNames(
    (0, "EDS-MIB", "wDeviceIndex"),
)
if mibBuilder.loadTexts:
    wEDS3032Entry.setStatus("current")
_WEDS3032Temperature_Type = DisplayString
_WEDS3032Temperature_Object = MibTableColumn
wEDS3032Temperature = _WEDS3032Temperature_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 13, 1, 1),
    _WEDS3032Temperature_Type()
)
wEDS3032Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS3032Temperature.setStatus("current")
_WEDS3032RTD1Temperature_Type = DisplayString
_WEDS3032RTD1Temperature_Object = MibTableColumn
wEDS3032RTD1Temperature = _WEDS3032RTD1Temperature_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 13, 1, 2),
    _WEDS3032RTD1Temperature_Type()
)
wEDS3032RTD1Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS3032RTD1Temperature.setStatus("current")
_WEDS3032RTD2Temperature_Type = DisplayString
_WEDS3032RTD2Temperature_Object = MibTableColumn
wEDS3032RTD2Temperature = _WEDS3032RTD2Temperature_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 13, 1, 3),
    _WEDS3032RTD2Temperature_Type()
)
wEDS3032RTD2Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS3032RTD2Temperature.setStatus("current")
_WEDS3032LEDState_Type = Integer32
_WEDS3032LEDState_Object = MibTableColumn
wEDS3032LEDState = _WEDS3032LEDState_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 13, 1, 4),
    _WEDS3032LEDState_Type()
)
wEDS3032LEDState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS3032LEDState.setStatus("current")
_WEDS3032Input1_Type = Integer32
_WEDS3032Input1_Object = MibTableColumn
wEDS3032Input1 = _WEDS3032Input1_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 13, 1, 5),
    _WEDS3032Input1_Type()
)
wEDS3032Input1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS3032Input1.setStatus("current")
_WEDS3032ActivityLatch1_Type = Integer32
_WEDS3032ActivityLatch1_Object = MibTableColumn
wEDS3032ActivityLatch1 = _WEDS3032ActivityLatch1_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 13, 1, 6),
    _WEDS3032ActivityLatch1_Type()
)
wEDS3032ActivityLatch1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS3032ActivityLatch1.setStatus("current")
_WEDS3032PulseCounter1_Type = Counter32
_WEDS3032PulseCounter1_Object = MibTableColumn
wEDS3032PulseCounter1 = _WEDS3032PulseCounter1_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 13, 1, 7),
    _WEDS3032PulseCounter1_Type()
)
wEDS3032PulseCounter1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS3032PulseCounter1.setStatus("current")
_WEDS3032Battery_Type = DisplayString
_WEDS3032Battery_Object = MibTableColumn
wEDS3032Battery = _WEDS3032Battery_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 13, 1, 8),
    _WEDS3032Battery_Type()
)
wEDS3032Battery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS3032Battery.setStatus("current")
_WEDS3032ReadCounter_Type = Counter32
_WEDS3032ReadCounter_Object = MibTableColumn
wEDS3032ReadCounter = _WEDS3032ReadCounter_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 13, 1, 9),
    _WEDS3032ReadCounter_Type()
)
wEDS3032ReadCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wEDS3032ReadCounter.setStatus("current")
_WEDS3032LEDFunction_Type = Integer32
_WEDS3032LEDFunction_Object = MibTableColumn
wEDS3032LEDFunction = _WEDS3032LEDFunction_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 13, 1, 10),
    _WEDS3032LEDFunction_Type()
)
wEDS3032LEDFunction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wEDS3032LEDFunction.setStatus("current")
_WEDS3032LEDSetState_Type = Integer32
_WEDS3032LEDSetState_Object = MibTableColumn
wEDS3032LEDSetState = _WEDS3032LEDSetState_Object(
    (1, 3, 6, 1, 4, 1, 31440, 11, 13, 1, 11),
    _WEDS3032LEDSetState_Type()
)
wEDS3032LEDSetState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wEDS3032LEDSetState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EDS-MIB",
    **{"edsMain": edsMain,
       "edsEnterprise": edsEnterprise,
       "eCompanyName": eCompanyName,
       "eProductName": eProductName,
       "eMIBVersion": eMIBVersion,
       "eFirmwareVersion": eFirmwareVersion,
       "eFirmwareDate": eFirmwareDate,
       "edsProducts": edsProducts,
       "dTrap": dTrap,
       "dTrapTable": dTrapTable,
       "dTrapEntry": dTrapEntry,
       "dTrapIndex": dTrapIndex,
       "dTrapEnable": dTrapEnable,
       "dTrapIP": dTrapIP,
       "dTrapCommunity": dTrapCommunity,
       "dTrapDeviceTable": dTrapDeviceTable,
       "dTrapDeviceEntry": dTrapDeviceEntry,
       "dTrapDeviceIndex": dTrapDeviceIndex,
       "dTrapDeviceEnable": dTrapDeviceEnable,
       "dTrapDeviceSendPointer": dTrapDeviceSendPointer,
       "dTrapDeviceROM": dTrapDeviceROM,
       "dTrapDeviceVariable": dTrapDeviceVariable,
       "dTrapDeviceHighThreshold": dTrapDeviceHighThreshold,
       "dTrapDeviceLowThreshold": dTrapDeviceLowThreshold,
       "dTrapDeviceHysteresis": dTrapDeviceHysteresis,
       "wTrap": wTrap,
       "wTrapTable": wTrapTable,
       "wTrapEntry": wTrapEntry,
       "wTrapIndex": wTrapIndex,
       "wTrapIP": wTrapIP,
       "wTrapCommunity": wTrapCommunity,
       "wTrapEUI": wTrapEUI,
       "wTrapVariable": wTrapVariable,
       "wTrapHighThreshold": wTrapHighThreshold,
       "wTrapLowThreshold": wTrapLowThreshold,
       "owDevices": owDevices,
       "owDeviceTypes": owDeviceTypes,
       "owNone": owNone,
       "owUnknown": owUnknown,
       "owDS2406": owDS2406,
       "owDS18B20": owDS18B20,
       "owDS18S20": owDS18S20,
       "owDS2438": owDS2438,
       "owDS2423": owDS2423,
       "owDS2408": owDS2408,
       "owDS2450": owDS2450,
       "owEDS0064": owEDS0064,
       "owEDS0065": owEDS0065,
       "owEDS0066": owEDS0066,
       "owEDS0067": owEDS0067,
       "owEDS0068": owEDS0068,
       "owEDS0069": owEDS0069,
       "owEDS0070": owEDS0070,
       "owEDS0071": owEDS0071,
       "owEDS0080": owEDS0080,
       "owEDS0082": owEDS0082,
       "owEDS0083": owEDS0083,
       "owEDS0085": owEDS0085,
       "owEDS0090": owEDS0090,
       "owEDS0091": owEDS0091,
       "owEDS0092": owEDS0092,
       "owDS28EA00": owDS28EA00,
       "owEDS0050": owEDS0050,
       "owEDS0001": owEDS0001,
       "owDeviceInfo": owDeviceInfo,
       "owDeviceNumActive": owDeviceNumActive,
       "owDeviceTable": owDeviceTable,
       "owDeviceEntry": owDeviceEntry,
       "owDeviceIndex": owDeviceIndex,
       "owDeviceType": owDeviceType,
       "owDeviceName": owDeviceName,
       "owDeviceDescription": owDeviceDescription,
       "owDeviceFamily": owDeviceFamily,
       "owDeviceROM": owDeviceROM,
       "owDeviceHealth": owDeviceHealth,
       "owDS2406Table": owDS2406Table,
       "owDS2406Entry": owDS2406Entry,
       "owDS2406PIOALevel": owDS2406PIOALevel,
       "owDS2406PIOBLevel": owDS2406PIOBLevel,
       "owDS2406PIOAFlipFlop": owDS2406PIOAFlipFlop,
       "owDS2406PIOBFlipFlop": owDS2406PIOBFlipFlop,
       "owDS2406PIOAActivityLatch": owDS2406PIOAActivityLatch,
       "owDS2406PIOBActivityLatch": owDS2406PIOBActivityLatch,
       "owDS2406NumChnls": owDS2406NumChnls,
       "owDS2406PwrSupply": owDS2406PwrSupply,
       "owDS2406ActivityLatchReset": owDS2406ActivityLatchReset,
       "owDS18B20Table": owDS18B20Table,
       "owDS18B20Entry": owDS18B20Entry,
       "owDS18B20Temperature": owDS18B20Temperature,
       "owDS18B20UserByte1": owDS18B20UserByte1,
       "owDS18B20UserByte2": owDS18B20UserByte2,
       "owDS18B20Resolution": owDS18B20Resolution,
       "owDS18B20PwrSupply": owDS18B20PwrSupply,
       "owDS18S20Table": owDS18S20Table,
       "owDS18S20Entry": owDS18S20Entry,
       "owDS18S20Temperature": owDS18S20Temperature,
       "owDS18S20UserByte1": owDS18S20UserByte1,
       "owDS18S20UserByte2": owDS18S20UserByte2,
       "owDS2423Table": owDS2423Table,
       "owDS2423Entry": owDS2423Entry,
       "owDS2423CounterA": owDS2423CounterA,
       "owDS2423CounterB": owDS2423CounterB,
       "owDS2438Table": owDS2438Table,
       "owDS2438Entry": owDS2438Entry,
       "owDS2438Temperature": owDS2438Temperature,
       "owDS2438SupplyVoltage": owDS2438SupplyVoltage,
       "owDS2438PinVoltage": owDS2438PinVoltage,
       "owDS2438current": owDS2438current,
       "owDS2438Humidity": owDS2438Humidity,
       "owDS2408Table": owDS2408Table,
       "owDS2408Entry": owDS2408Entry,
       "owDS2408PIOLogicState": owDS2408PIOLogicState,
       "owDS2408PIOOutputLatchState": owDS2408PIOOutputLatchState,
       "owDS2408PIOActivityLatchState": owDS2408PIOActivityLatchState,
       "owDS2408RSTZConfiguration": owDS2408RSTZConfiguration,
       "owDS2408PowerOnResetLatch": owDS2408PowerOnResetLatch,
       "owDS2408VCCPowerStatus": owDS2408VCCPowerStatus,
       "owDS2450Table": owDS2450Table,
       "owDS2450Entry": owDS2450Entry,
       "owDS2450ChannelAConversionValue": owDS2450ChannelAConversionValue,
       "owDS2450ChannelAConversionResolution": owDS2450ChannelAConversionResolution,
       "owDS2450ChannelAConversionRange": owDS2450ChannelAConversionRange,
       "owDS2450ChannelAOutputEnable": owDS2450ChannelAOutputEnable,
       "owDS2450ChannelAOutputControl": owDS2450ChannelAOutputControl,
       "owDS2450ChannelBConversionValue": owDS2450ChannelBConversionValue,
       "owDS2450ChannelBConversionResolution": owDS2450ChannelBConversionResolution,
       "owDS2450ChannelBConversionRange": owDS2450ChannelBConversionRange,
       "owDS2450ChannelBOutputEnable": owDS2450ChannelBOutputEnable,
       "owDS2450ChannelBOutputControl": owDS2450ChannelBOutputControl,
       "owDS2450ChannelCConversionValue": owDS2450ChannelCConversionValue,
       "owDS2450ChannelCConversionResolution": owDS2450ChannelCConversionResolution,
       "owDS2450ChannelCConversionRange": owDS2450ChannelCConversionRange,
       "owDS2450ChannelCOutputEnable": owDS2450ChannelCOutputEnable,
       "owDS2450ChannelCOutputControl": owDS2450ChannelCOutputControl,
       "owDS2450ChannelDConversionValue": owDS2450ChannelDConversionValue,
       "owDS2450ChannelDConversionResolution": owDS2450ChannelDConversionResolution,
       "owDS2450ChannelDConversionRange": owDS2450ChannelDConversionRange,
       "owDS2450ChannelDOutputEnable": owDS2450ChannelDOutputEnable,
       "owDS2450ChannelDOutputControl": owDS2450ChannelDOutputControl,
       "owDS2450PowerOnReset": owDS2450PowerOnReset,
       "owDS2450VCCControl": owDS2450VCCControl,
       "owEDS0064Table": owEDS0064Table,
       "owEDS0064Entry": owEDS0064Entry,
       "owEDS0064Temperature": owEDS0064Temperature,
       "owEDS0064Counter": owEDS0064Counter,
       "owEDS0065Table": owEDS0065Table,
       "owEDS0065Entry": owEDS0065Entry,
       "owEDS0065Temperature": owEDS0065Temperature,
       "owEDS0065Humidity": owEDS0065Humidity,
       "owEDS0065DewPoint": owEDS0065DewPoint,
       "owEDS0065Humidex": owEDS0065Humidex,
       "owEDS0065HeatIndex": owEDS0065HeatIndex,
       "owEDS0065Counter": owEDS0065Counter,
       "owEDS0066Table": owEDS0066Table,
       "owEDS0066Entry": owEDS0066Entry,
       "owEDS0066Temperature": owEDS0066Temperature,
       "owEDS0066BarometricPressureMb": owEDS0066BarometricPressureMb,
       "owEDS0066BarometricPressureHg": owEDS0066BarometricPressureHg,
       "owEDS0066Counter": owEDS0066Counter,
       "owEDS0067Table": owEDS0067Table,
       "owEDS0067Entry": owEDS0067Entry,
       "owEDS0067Temperature": owEDS0067Temperature,
       "owEDS0067Light": owEDS0067Light,
       "owEDS0067Counter": owEDS0067Counter,
       "owEDS0068Table": owEDS0068Table,
       "owEDS0068Entry": owEDS0068Entry,
       "owEDS0068Temperature": owEDS0068Temperature,
       "owEDS0068Humidity": owEDS0068Humidity,
       "owEDS0068DewPoint": owEDS0068DewPoint,
       "owEDS0068Humidex": owEDS0068Humidex,
       "owEDS0068HeatIndex": owEDS0068HeatIndex,
       "owEDS0068BarometricPressureMb": owEDS0068BarometricPressureMb,
       "owEDS0068BarometricPressureHg": owEDS0068BarometricPressureHg,
       "owEDS0068Light": owEDS0068Light,
       "owEDS0068Counter": owEDS0068Counter,
       "owEDS0069Table": owEDS0069Table,
       "owEDS0069Entry": owEDS0069Entry,
       "owEDS0069Temperature": owEDS0069Temperature,
       "owEDS0069Motion": owEDS0069Motion,
       "owEDS0069Counter": owEDS0069Counter,
       "owEDS0070Table": owEDS0070Table,
       "owEDS0070Entry": owEDS0070Entry,
       "owEDS0070VibrationInstant": owEDS0070VibrationInstant,
       "owEDS0070VibrationPeak": owEDS0070VibrationPeak,
       "owEDS0070VibrationMax": owEDS0070VibrationMax,
       "owEDS0070VibrationMin": owEDS0070VibrationMin,
       "owEDS0070Counter": owEDS0070Counter,
       "owEDS0071Table": owEDS0071Table,
       "owEDS0071Entry": owEDS0071Entry,
       "owEDS0071Temperature": owEDS0071Temperature,
       "owEDS0071Counter": owEDS0071Counter,
       "owEDS0080Table": owEDS0080Table,
       "owEDS0080Entry": owEDS0080Entry,
       "owEDS0080Input1": owEDS0080Input1,
       "owEDS0080Input2": owEDS0080Input2,
       "owEDS0080Input3": owEDS0080Input3,
       "owEDS0080Input4": owEDS0080Input4,
       "owEDS0080Input5": owEDS0080Input5,
       "owEDS0080Input6": owEDS0080Input6,
       "owEDS0080Input7": owEDS0080Input7,
       "owEDS0080Input8": owEDS0080Input8,
       "owEDS0080Counter": owEDS0080Counter,
       "owEDS0082Table": owEDS0082Table,
       "owEDS0082Entry": owEDS0082Entry,
       "owEDS0082Input1": owEDS0082Input1,
       "owEDS0082Input2": owEDS0082Input2,
       "owEDS0082Input3": owEDS0082Input3,
       "owEDS0082Input4": owEDS0082Input4,
       "owEDS0082Input5": owEDS0082Input5,
       "owEDS0082Input6": owEDS0082Input6,
       "owEDS0082Input7": owEDS0082Input7,
       "owEDS0082Input8": owEDS0082Input8,
       "owEDS0082Counter": owEDS0082Counter,
       "owEDS0083Table": owEDS0083Table,
       "owEDS0083Entry": owEDS0083Entry,
       "owEDS0083Input1": owEDS0083Input1,
       "owEDS0083Input2": owEDS0083Input2,
       "owEDS0083Input3": owEDS0083Input3,
       "owEDS0083Input4": owEDS0083Input4,
       "owEDS0083Counter": owEDS0083Counter,
       "owEDS0085Table": owEDS0085Table,
       "owEDS0085Entry": owEDS0085Entry,
       "owEDS0085Input1": owEDS0085Input1,
       "owEDS0085Input2": owEDS0085Input2,
       "owEDS0085Input3": owEDS0085Input3,
       "owEDS0085Input4": owEDS0085Input4,
       "owEDS0085Counter": owEDS0085Counter,
       "owEDS0090Table": owEDS0090Table,
       "owEDS0090Entry": owEDS0090Entry,
       "owEDS0090Input1": owEDS0090Input1,
       "owEDS0090Input2": owEDS0090Input2,
       "owEDS0090Input3": owEDS0090Input3,
       "owEDS0090Input4": owEDS0090Input4,
       "owEDS0090Input5": owEDS0090Input5,
       "owEDS0090Input6": owEDS0090Input6,
       "owEDS0090Input7": owEDS0090Input7,
       "owEDS0090Input8": owEDS0090Input8,
       "owEDS0090ActivityLatch1": owEDS0090ActivityLatch1,
       "owEDS0090ActivityLatch2": owEDS0090ActivityLatch2,
       "owEDS0090ActivityLatch3": owEDS0090ActivityLatch3,
       "owEDS0090ActivityLatch4": owEDS0090ActivityLatch4,
       "owEDS0090ActivityLatch5": owEDS0090ActivityLatch5,
       "owEDS0090ActivityLatch6": owEDS0090ActivityLatch6,
       "owEDS0090ActivityLatch7": owEDS0090ActivityLatch7,
       "owEDS0090ActivityLatch8": owEDS0090ActivityLatch8,
       "owEDS0090PulseCounter1": owEDS0090PulseCounter1,
       "owEDS0090PulseCounter2": owEDS0090PulseCounter2,
       "owEDS0090PulseCounter3": owEDS0090PulseCounter3,
       "owEDS0090PulseCounter4": owEDS0090PulseCounter4,
       "owEDS0090PulseCounter5": owEDS0090PulseCounter5,
       "owEDS0090PulseCounter6": owEDS0090PulseCounter6,
       "owEDS0090PulseCounter7": owEDS0090PulseCounter7,
       "owEDS0090PulseCounter8": owEDS0090PulseCounter8,
       "owEDS0090Output1": owEDS0090Output1,
       "owEDS0090Output2": owEDS0090Output2,
       "owEDS0090Output3": owEDS0090Output3,
       "owEDS0090Output4": owEDS0090Output4,
       "owEDS0090Output5": owEDS0090Output5,
       "owEDS0090Output6": owEDS0090Output6,
       "owEDS0090Output7": owEDS0090Output7,
       "owEDS0090Output8": owEDS0090Output8,
       "owEDS0090PullDown1": owEDS0090PullDown1,
       "owEDS0090PullDown2": owEDS0090PullDown2,
       "owEDS0090PullDown3": owEDS0090PullDown3,
       "owEDS0090PullDown4": owEDS0090PullDown4,
       "owEDS0090PullDown5": owEDS0090PullDown5,
       "owEDS0090PullDown6": owEDS0090PullDown6,
       "owEDS0090PullDown7": owEDS0090PullDown7,
       "owEDS0090PullDown8": owEDS0090PullDown8,
       "owEDS0090ActivityLatchReset1": owEDS0090ActivityLatchReset1,
       "owEDS0090ActivityLatchReset2": owEDS0090ActivityLatchReset2,
       "owEDS0090ActivityLatchReset3": owEDS0090ActivityLatchReset3,
       "owEDS0090ActivityLatchReset4": owEDS0090ActivityLatchReset4,
       "owEDS0090ActivityLatchReset5": owEDS0090ActivityLatchReset5,
       "owEDS0090ActivityLatchReset6": owEDS0090ActivityLatchReset6,
       "owEDS0090ActivityLatchReset7": owEDS0090ActivityLatchReset7,
       "owEDS0090ActivityLatchReset8": owEDS0090ActivityLatchReset8,
       "owEDS0090PulseCounterReset1": owEDS0090PulseCounterReset1,
       "owEDS0090PulseCounterReset2": owEDS0090PulseCounterReset2,
       "owEDS0090PulseCounterReset3": owEDS0090PulseCounterReset3,
       "owEDS0090PulseCounterReset4": owEDS0090PulseCounterReset4,
       "owEDS0090PulseCounterReset5": owEDS0090PulseCounterReset5,
       "owEDS0090PulseCounterReset6": owEDS0090PulseCounterReset6,
       "owEDS0090PulseCounterReset7": owEDS0090PulseCounterReset7,
       "owEDS0090PulseCounterReset8": owEDS0090PulseCounterReset8,
       "owEDS0090Counter": owEDS0090Counter,
       "owEDS0091Table": owEDS0091Table,
       "owEDS0091Entry": owEDS0091Entry,
       "owEDS0091Input1": owEDS0091Input1,
       "owEDS0091Input2": owEDS0091Input2,
       "owEDS0091Input3": owEDS0091Input3,
       "owEDS0091Input4": owEDS0091Input4,
       "owEDS0091ActivityLatch1": owEDS0091ActivityLatch1,
       "owEDS0091ActivityLatch2": owEDS0091ActivityLatch2,
       "owEDS0091ActivityLatch3": owEDS0091ActivityLatch3,
       "owEDS0091ActivityLatch4": owEDS0091ActivityLatch4,
       "owEDS0091PulseCounter1": owEDS0091PulseCounter1,
       "owEDS0091PulseCounter2": owEDS0091PulseCounter2,
       "owEDS0091PulseCounter3": owEDS0091PulseCounter3,
       "owEDS0091PulseCounter4": owEDS0091PulseCounter4,
       "owEDS0091PulseCounterReset1": owEDS0091PulseCounterReset1,
       "owEDS0091PulseCounterReset2": owEDS0091PulseCounterReset2,
       "owEDS0091PulseCounterReset3": owEDS0091PulseCounterReset3,
       "owEDS0091PulseCounterReset4": owEDS0091PulseCounterReset4,
       "owEDS0091ActivityLatchReset1": owEDS0091ActivityLatchReset1,
       "owEDS0091ActivityLatchReset2": owEDS0091ActivityLatchReset2,
       "owEDS0091ActivityLatchReset3": owEDS0091ActivityLatchReset3,
       "owEDS0091ActivityLatchReset4": owEDS0091ActivityLatchReset4,
       "owEDS0091Counter": owEDS0091Counter,
       "owEDS0092Table": owEDS0092Table,
       "owEDS0092Entry": owEDS0092Entry,
       "owEDS0092Output1": owEDS0092Output1,
       "owEDS0092Output2": owEDS0092Output2,
       "owEDS0092Output3": owEDS0092Output3,
       "owEDS0092Output4": owEDS0092Output4,
       "owEDS0092Counter": owEDS0092Counter,
       "owDS28EA00Table": owDS28EA00Table,
       "owDS28EA00Entry": owDS28EA00Entry,
       "owDS28EA00Temperature": owDS28EA00Temperature,
       "owDS28EA00UserByte1": owDS28EA00UserByte1,
       "owDS28EA00UserByte2": owDS28EA00UserByte2,
       "owDS28EA00PIOALevel": owDS28EA00PIOALevel,
       "owDS28EA00PIOBLevel": owDS28EA00PIOBLevel,
       "owDS28EA00PIOAFlipFlop": owDS28EA00PIOAFlipFlop,
       "owDS28EA00PIOBFlipFlop": owDS28EA00PIOBFlipFlop,
       "owEDS0050Table": owEDS0050Table,
       "owEDS0050Entry": owEDS0050Entry,
       "owEDS0050Temperature": owEDS0050Temperature,
       "owEDS0050InputVoltage": owEDS0050InputVoltage,
       "owEDS0050Input1": owEDS0050Input1,
       "owEDS0050Input2": owEDS0050Input2,
       "owEDS0050ActivityLatch1": owEDS0050ActivityLatch1,
       "owEDS0050ActivityLatch2": owEDS0050ActivityLatch2,
       "owEDS0050PulseCounter1": owEDS0050PulseCounter1,
       "owEDS0050PulseCounter2": owEDS0050PulseCounter2,
       "owEDS0050Output1": owEDS0050Output1,
       "owEDS0050Output2": owEDS0050Output2,
       "owEDS0050ActivityLatchReset1": owEDS0050ActivityLatchReset1,
       "owEDS0050ActivityLatchReset2": owEDS0050ActivityLatchReset2,
       "owEDS0050PulseCounterReset1": owEDS0050PulseCounterReset1,
       "owEDS0050PulseCounterReset2": owEDS0050PulseCounterReset2,
       "owEDS0050Counter": owEDS0050Counter,
       "owEDS0001Table": owEDS0001Table,
       "owEDS0001Entry": owEDS0001Entry,
       "owEDS0001PollCount": owEDS0001PollCount,
       "owEDS0001DevicesConnected": owEDS0001DevicesConnected,
       "owEDS0001LoopTime": owEDS0001LoopTime,
       "owEDS0001DevicesConnectedChannel1": owEDS0001DevicesConnectedChannel1,
       "owEDS0001DevicesConnectedChannel2": owEDS0001DevicesConnectedChannel2,
       "owEDS0001DevicesConnectedChannel3": owEDS0001DevicesConnectedChannel3,
       "owEDS0001ErrorsChannel1": owEDS0001ErrorsChannel1,
       "owEDS0001ErrorsChannel2": owEDS0001ErrorsChannel2,
       "owEDS0001ErrorsChannel3": owEDS0001ErrorsChannel3,
       "owEDS0001VoltageChannel1": owEDS0001VoltageChannel1,
       "owEDS0001VoltageChannel2": owEDS0001VoltageChannel2,
       "owEDS0001VoltageChannel3": owEDS0001VoltageChannel3,
       "owEDS0001InputVoltage": owEDS0001InputVoltage,
       "owEDS0001DeviceName": owEDS0001DeviceName,
       "owEDS0001HostName": owEDS0001HostName,
       "owEDS0001MACAddress": owEDS0001MACAddress,
       "owEDS0001TimeStamp": owEDS0001TimeStamp,
       "wDevices": wDevices,
       "wDeviceTypes": wDeviceTypes,
       "wNone": wNone,
       "wUnknown": wUnknown,
       "wUnused1": wUnused1,
       "wUnused2": wUnused2,
       "wEDS1068": wEDS1068,
       "wEDS1067": wEDS1067,
       "wEDS1066": wEDS1066,
       "wEDS1065": wEDS1065,
       "wEDS1064": wEDS1064,
       "wEDS1101": wEDS1101,
       "wEDS2101": wEDS2101,
       "wEDS3030": wEDS3030,
       "wEDS3031": wEDS3031,
       "wEDS3032": wEDS3032,
       "wDeviceInfo": wDeviceInfo,
       "wDeviceNumActive": wDeviceNumActive,
       "wDeviceTable": wDeviceTable,
       "wDeviceEntry": wDeviceEntry,
       "wDeviceIndex": wDeviceIndex,
       "wDeviceType": wDeviceType,
       "wDeviceName": wDeviceName,
       "wDeviceDescription": wDeviceDescription,
       "wDeviceFamily": wDeviceFamily,
       "wDeviceEUI": wDeviceEUI,
       "wDeviceHealth": wDeviceHealth,
       "wDeviceTag": wDeviceTag,
       "wEDS1068Table": wEDS1068Table,
       "wEDS1068Entry": wEDS1068Entry,
       "wEDS1068Temperature": wEDS1068Temperature,
       "wEDS1068Humidity": wEDS1068Humidity,
       "wEDS1068DewPoint": wEDS1068DewPoint,
       "wEDS1068Humidex": wEDS1068Humidex,
       "wEDS1068HeatIndex": wEDS1068HeatIndex,
       "wEDS1068BarometricPressure": wEDS1068BarometricPressure,
       "wEDS1068LEDState": wEDS1068LEDState,
       "wEDS1068RelayState": wEDS1068RelayState,
       "wEDS1068Light": wEDS1068Light,
       "wEDS1068Input1": wEDS1068Input1,
       "wEDS1068ActivityLatch1": wEDS1068ActivityLatch1,
       "wEDS1068PulseCounter1": wEDS1068PulseCounter1,
       "wEDS1068Battery": wEDS1068Battery,
       "wEDS1068ReadCounter": wEDS1068ReadCounter,
       "wEDS1068LEDFunction": wEDS1068LEDFunction,
       "wEDS1068RelayFunction": wEDS1068RelayFunction,
       "wEDS1068LEDSetState": wEDS1068LEDSetState,
       "wEDS1068RelaySetState": wEDS1068RelaySetState,
       "wEDS1067Table": wEDS1067Table,
       "wEDS1067Entry": wEDS1067Entry,
       "wEDS1067Temperature": wEDS1067Temperature,
       "wEDS1067LEDState": wEDS1067LEDState,
       "wEDS1067RelayState": wEDS1067RelayState,
       "wEDS1067Light": wEDS1067Light,
       "wEDS1067Input1": wEDS1067Input1,
       "wEDS1067ActivityLatch1": wEDS1067ActivityLatch1,
       "wEDS1067PulseCounter1": wEDS1067PulseCounter1,
       "wEDS1067Battery": wEDS1067Battery,
       "wEDS1067ReadCounter": wEDS1067ReadCounter,
       "wEDS1067LEDFunction": wEDS1067LEDFunction,
       "wEDS1067RelayFunction": wEDS1067RelayFunction,
       "wEDS1067LEDSetState": wEDS1067LEDSetState,
       "wEDS1067RelaySetState": wEDS1067RelaySetState,
       "wEDS1066Table": wEDS1066Table,
       "wEDS1066Entry": wEDS1066Entry,
       "wEDS1066Temperature": wEDS1066Temperature,
       "wEDS1066BarometricPressure": wEDS1066BarometricPressure,
       "wEDS1066LEDState": wEDS1066LEDState,
       "wEDS1066RelayState": wEDS1066RelayState,
       "wEDS1066Input1": wEDS1066Input1,
       "wEDS1066ActivityLatch1": wEDS1066ActivityLatch1,
       "wEDS1066PulseCounter1": wEDS1066PulseCounter1,
       "wEDS1066Battery": wEDS1066Battery,
       "wEDS1066ReadCounter": wEDS1066ReadCounter,
       "wEDS1066LEDFunction": wEDS1066LEDFunction,
       "wEDS1066RelayFunction": wEDS1066RelayFunction,
       "wEDS1066LEDSetState": wEDS1066LEDSetState,
       "wEDS1066RelaySetState": wEDS1066RelaySetState,
       "wEDS1065Table": wEDS1065Table,
       "wEDS1065Entry": wEDS1065Entry,
       "wEDS1065Temperature": wEDS1065Temperature,
       "wEDS1065Humidity": wEDS1065Humidity,
       "wEDS1065DewPoint": wEDS1065DewPoint,
       "wEDS1065Humidex": wEDS1065Humidex,
       "wEDS1065HeatIndex": wEDS1065HeatIndex,
       "wEDS1065LEDState": wEDS1065LEDState,
       "wEDS1065RelayState": wEDS1065RelayState,
       "wEDS1065Input1": wEDS1065Input1,
       "wEDS1065ActivityLatch1": wEDS1065ActivityLatch1,
       "wEDS1065PulseCounter1": wEDS1065PulseCounter1,
       "wEDS1065Battery": wEDS1065Battery,
       "wEDS1065ReadCounter": wEDS1065ReadCounter,
       "wEDS1065LEDFunction": wEDS1065LEDFunction,
       "wEDS1065RelayFunction": wEDS1065RelayFunction,
       "wEDS1065LEDSetState": wEDS1065LEDSetState,
       "wEDS1065RelaySetState": wEDS1065RelaySetState,
       "wEDS1064Table": wEDS1064Table,
       "wEDS1064Entry": wEDS1064Entry,
       "wEDS1064Temperature": wEDS1064Temperature,
       "wEDS1064LEDState": wEDS1064LEDState,
       "wEDS1064RelayState": wEDS1064RelayState,
       "wEDS1064Input1": wEDS1064Input1,
       "wEDS1064ActivityLatch1": wEDS1064ActivityLatch1,
       "wEDS1064PulseCounter1": wEDS1064PulseCounter1,
       "wEDS1064Battery": wEDS1064Battery,
       "wEDS1064ReadCounter": wEDS1064ReadCounter,
       "wEDS1064LEDFunction": wEDS1064LEDFunction,
       "wEDS1064RelayFunction": wEDS1064RelayFunction,
       "wEDS1064LEDSetState": wEDS1064LEDSetState,
       "wEDS1064RelaySetState": wEDS1064RelaySetState,
       "wEDS1101Table": wEDS1101Table,
       "wEDS1101Entry": wEDS1101Entry,
       "wEDS1101DevicesConnected": wEDS1101DevicesConnected,
       "wEDS1101SendCounter": wEDS1101SendCounter,
       "wEDS2101Table": wEDS2101Table,
       "wEDS2101Entry": wEDS2101Entry,
       "wEDS2101DevicesConnected": wEDS2101DevicesConnected,
       "wEDS2101SendCounter": wEDS2101SendCounter,
       "wEDS3030Table": wEDS3030Table,
       "wEDS3030Entry": wEDS3030Entry,
       "wEDS3030Temperature": wEDS3030Temperature,
       "wEDS3030Probe": wEDS3030Probe,
       "wEDS3030LEDState": wEDS3030LEDState,
       "wEDS3030Light": wEDS3030Light,
       "wEDS3030Input1": wEDS3030Input1,
       "wEDS3030ActivityLatch1": wEDS3030ActivityLatch1,
       "wEDS3030PulseCounter1": wEDS3030PulseCounter1,
       "wEDS3030Battery": wEDS3030Battery,
       "wEDS3030ReadCounter": wEDS3030ReadCounter,
       "wEDS3030LEDFunction": wEDS3030LEDFunction,
       "wEDS3030LEDSetState": wEDS3030LEDSetState,
       "wEDS3031Table": wEDS3031Table,
       "wEDS3031Entry": wEDS3031Entry,
       "wEDS3031Temperature": wEDS3031Temperature,
       "wEDS3031RTDTemperature": wEDS3031RTDTemperature,
       "wEDS3031LEDState": wEDS3031LEDState,
       "wEDS3031Input1": wEDS3031Input1,
       "wEDS3031ActivityLatch1": wEDS3031ActivityLatch1,
       "wEDS3031PulseCounter1": wEDS3031PulseCounter1,
       "wEDS3031Battery": wEDS3031Battery,
       "wEDS3031ReadCounter": wEDS3031ReadCounter,
       "wEDS3031LEDFunction": wEDS3031LEDFunction,
       "wEDS3031LEDSetState": wEDS3031LEDSetState,
       "wEDS3032Table": wEDS3032Table,
       "wEDS3032Entry": wEDS3032Entry,
       "wEDS3032Temperature": wEDS3032Temperature,
       "wEDS3032RTD1Temperature": wEDS3032RTD1Temperature,
       "wEDS3032RTD2Temperature": wEDS3032RTD2Temperature,
       "wEDS3032LEDState": wEDS3032LEDState,
       "wEDS3032Input1": wEDS3032Input1,
       "wEDS3032ActivityLatch1": wEDS3032ActivityLatch1,
       "wEDS3032PulseCounter1": wEDS3032PulseCounter1,
       "wEDS3032Battery": wEDS3032Battery,
       "wEDS3032ReadCounter": wEDS3032ReadCounter,
       "wEDS3032LEDFunction": wEDS3032LEDFunction,
       "wEDS3032LEDSetState": wEDS3032LEDSetState}
)
