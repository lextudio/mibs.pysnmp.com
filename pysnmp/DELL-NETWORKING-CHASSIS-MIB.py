# SNMP MIB module (DELL-NETWORKING-CHASSIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DELL-NETWORKING-CHASSIS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:23:49 2024
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

(dellNetMgmt,) = mibBuilder.importSymbols(
    "DELL-NETWORKING-SMI",
    "dellNetMgmt")

(DellNetCardOperStatus,
 DellNetChassisType,
 DellNetDeviceType,
 DellNetHundredthdB,
 DellNetIfType,
 DellNetMfgDate,
 DellNetPEOperStatus,
 DellNetProcessorModuleType,
 DellNetSwDate,
 DellNetSystemCardType) = mibBuilder.importSymbols(
    "DELL-NETWORKING-TC",
    "DellNetCardOperStatus",
    "DellNetChassisType",
    "DellNetDeviceType",
    "DellNetHundredthdB",
    "DellNetIfType",
    "DellNetMfgDate",
    "DellNetPEOperStatus",
    "DellNetProcessorModuleType",
    "DellNetSwDate",
    "DellNetSystemCardType")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

dellNetChassisMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26)
)
dellNetChassisMib.setRevisions(
        ("2014-08-05 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DellNetSysObject_ObjectIdentity = ObjectIdentity
dellNetSysObject = _DellNetSysObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1)
)
_DellNetSysParameter_ObjectIdentity = ObjectIdentity
dellNetSysParameter = _DellNetSysParameter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 1)
)
_DellNetDeviceType_Type = DellNetDeviceType
_DellNetDeviceType_Object = MibScalar
dellNetDeviceType = _DellNetDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 1, 1),
    _DellNetDeviceType_Type()
)
dellNetDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetDeviceType.setStatus("current")
_DellNetChassisObject_ObjectIdentity = ObjectIdentity
dellNetChassisObject = _DellNetChassisObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 2)
)
_DellNetNumChassis_Type = Integer32
_DellNetNumChassis_Object = MibScalar
dellNetNumChassis = _DellNetNumChassis_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 2, 1),
    _DellNetNumChassis_Type()
)
dellNetNumChassis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetNumChassis.setStatus("current")
_DellNetMaxNumChassis_Type = Integer32
_DellNetMaxNumChassis_Object = MibScalar
dellNetMaxNumChassis = _DellNetMaxNumChassis_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 2, 2),
    _DellNetMaxNumChassis_Type()
)
dellNetMaxNumChassis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetMaxNumChassis.setStatus("current")
_DellNetChassisTable_Object = MibTable
dellNetChassisTable = _DellNetChassisTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 2, 3)
)
if mibBuilder.loadTexts:
    dellNetChassisTable.setStatus("current")
_DellNetChassisEntry_Object = MibTableRow
dellNetChassisEntry = _DellNetChassisEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 2, 3, 1)
)
dellNetChassisEntry.setIndexNames(
    (0, "DELL-NETWORKING-CHASSIS-MIB", "dellNetChassisIndex"),
)
if mibBuilder.loadTexts:
    dellNetChassisEntry.setStatus("current")
_DellNetChassisIndex_Type = Integer32
_DellNetChassisIndex_Object = MibTableColumn
dellNetChassisIndex = _DellNetChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 2, 3, 1, 1),
    _DellNetChassisIndex_Type()
)
dellNetChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetChassisIndex.setStatus("current")
_DellNetChassisType_Type = DellNetChassisType
_DellNetChassisType_Object = MibTableColumn
dellNetChassisType = _DellNetChassisType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 2, 3, 1, 2),
    _DellNetChassisType_Type()
)
dellNetChassisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetChassisType.setStatus("current")
_DellNetChassisMacAddr_Type = MacAddress
_DellNetChassisMacAddr_Object = MibTableColumn
dellNetChassisMacAddr = _DellNetChassisMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 2, 3, 1, 3),
    _DellNetChassisMacAddr_Type()
)
dellNetChassisMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetChassisMacAddr.setStatus("current")


class _DellNetChassisSerialNumber_Type(DisplayString):
    """Custom type dellNetChassisSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_DellNetChassisSerialNumber_Type.__name__ = "DisplayString"
_DellNetChassisSerialNumber_Object = MibTableColumn
dellNetChassisSerialNumber = _DellNetChassisSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 2, 3, 1, 4),
    _DellNetChassisSerialNumber_Type()
)
dellNetChassisSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetChassisSerialNumber.setStatus("current")


class _DellNetChassisPartNum_Type(DisplayString):
    """Custom type dellNetChassisPartNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_DellNetChassisPartNum_Type.__name__ = "DisplayString"
_DellNetChassisPartNum_Object = MibTableColumn
dellNetChassisPartNum = _DellNetChassisPartNum_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 2, 3, 1, 5),
    _DellNetChassisPartNum_Type()
)
dellNetChassisPartNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetChassisPartNum.setStatus("current")


class _DellNetChassisProductRev_Type(DisplayString):
    """Custom type dellNetChassisProductRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_DellNetChassisProductRev_Type.__name__ = "DisplayString"
_DellNetChassisProductRev_Object = MibTableColumn
dellNetChassisProductRev = _DellNetChassisProductRev_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 2, 3, 1, 6),
    _DellNetChassisProductRev_Type()
)
dellNetChassisProductRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetChassisProductRev.setStatus("current")


class _DellNetChassisVendorId_Type(DisplayString):
    """Custom type dellNetChassisVendorId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_DellNetChassisVendorId_Type.__name__ = "DisplayString"
_DellNetChassisVendorId_Object = MibTableColumn
dellNetChassisVendorId = _DellNetChassisVendorId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 2, 3, 1, 7),
    _DellNetChassisVendorId_Type()
)
dellNetChassisVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetChassisVendorId.setStatus("current")
_DellNetChassisMfgDate_Type = DellNetMfgDate
_DellNetChassisMfgDate_Object = MibTableColumn
dellNetChassisMfgDate = _DellNetChassisMfgDate_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 2, 3, 1, 8),
    _DellNetChassisMfgDate_Type()
)
dellNetChassisMfgDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetChassisMfgDate.setStatus("current")


class _DellNetChassisCountryCode_Type(DisplayString):
    """Custom type dellNetChassisCountryCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_DellNetChassisCountryCode_Type.__name__ = "DisplayString"
_DellNetChassisCountryCode_Object = MibTableColumn
dellNetChassisCountryCode = _DellNetChassisCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 2, 3, 1, 9),
    _DellNetChassisCountryCode_Type()
)
dellNetChassisCountryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetChassisCountryCode.setStatus("current")


class _DellNetChassisPPIDRev_Type(DisplayString):
    """Custom type dellNetChassisPPIDRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_DellNetChassisPPIDRev_Type.__name__ = "DisplayString"
_DellNetChassisPPIDRev_Object = MibTableColumn
dellNetChassisPPIDRev = _DellNetChassisPPIDRev_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 2, 3, 1, 10),
    _DellNetChassisPPIDRev_Type()
)
dellNetChassisPPIDRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetChassisPPIDRev.setStatus("current")


class _DellNetChassisServiceTag_Type(DisplayString):
    """Custom type dellNetChassisServiceTag based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_DellNetChassisServiceTag_Type.__name__ = "DisplayString"
_DellNetChassisServiceTag_Object = MibTableColumn
dellNetChassisServiceTag = _DellNetChassisServiceTag_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 2, 3, 1, 11),
    _DellNetChassisServiceTag_Type()
)
dellNetChassisServiceTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetChassisServiceTag.setStatus("current")


class _DellNetChassisExpServiceCode_Type(DisplayString):
    """Custom type dellNetChassisExpServiceCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_DellNetChassisExpServiceCode_Type.__name__ = "DisplayString"
_DellNetChassisExpServiceCode_Object = MibTableColumn
dellNetChassisExpServiceCode = _DellNetChassisExpServiceCode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 2, 3, 1, 12),
    _DellNetChassisExpServiceCode_Type()
)
dellNetChassisExpServiceCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetChassisExpServiceCode.setStatus("current")
_DellNetChassisNumSlots_Type = Integer32
_DellNetChassisNumSlots_Object = MibTableColumn
dellNetChassisNumSlots = _DellNetChassisNumSlots_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 2, 3, 1, 13),
    _DellNetChassisNumSlots_Type()
)
dellNetChassisNumSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetChassisNumSlots.setStatus("current")
_DellNetChassisNumLineCardSlots_Type = Integer32
_DellNetChassisNumLineCardSlots_Object = MibTableColumn
dellNetChassisNumLineCardSlots = _DellNetChassisNumLineCardSlots_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 2, 3, 1, 14),
    _DellNetChassisNumLineCardSlots_Type()
)
dellNetChassisNumLineCardSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetChassisNumLineCardSlots.setStatus("current")
_DellNetChassisNumFanTrays_Type = Integer32
_DellNetChassisNumFanTrays_Object = MibTableColumn
dellNetChassisNumFanTrays = _DellNetChassisNumFanTrays_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 2, 3, 1, 15),
    _DellNetChassisNumFanTrays_Type()
)
dellNetChassisNumFanTrays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetChassisNumFanTrays.setStatus("current")
_DellNetChassisNumPowerSupplies_Type = Integer32
_DellNetChassisNumPowerSupplies_Object = MibTableColumn
dellNetChassisNumPowerSupplies = _DellNetChassisNumPowerSupplies_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 2, 3, 1, 16),
    _DellNetChassisNumPowerSupplies_Type()
)
dellNetChassisNumPowerSupplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetChassisNumPowerSupplies.setStatus("current")
_DellNetCardTable_Object = MibTable
dellNetCardTable = _DellNetCardTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 2, 4)
)
if mibBuilder.loadTexts:
    dellNetCardTable.setStatus("current")
_DellNetCardEntry_Object = MibTableRow
dellNetCardEntry = _DellNetCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 2, 4, 1)
)
dellNetCardEntry.setIndexNames(
    (0, "DELL-NETWORKING-CHASSIS-MIB", "dellNetChassisIndex"),
    (0, "DELL-NETWORKING-CHASSIS-MIB", "dellNetCardIndex"),
)
if mibBuilder.loadTexts:
    dellNetCardEntry.setStatus("current")
_DellNetCardIndex_Type = Integer32
_DellNetCardIndex_Object = MibTableColumn
dellNetCardIndex = _DellNetCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 2, 4, 1, 1),
    _DellNetCardIndex_Type()
)
dellNetCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dellNetCardIndex.setStatus("current")
_DellNetCardType_Type = DellNetSystemCardType
_DellNetCardType_Object = MibTableColumn
dellNetCardType = _DellNetCardType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 2, 4, 1, 2),
    _DellNetCardType_Type()
)
dellNetCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetCardType.setStatus("current")


class _DellNetCardDescription_Type(DisplayString):
    """Custom type dellNetCardDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_DellNetCardDescription_Type.__name__ = "DisplayString"
_DellNetCardDescription_Object = MibTableColumn
dellNetCardDescription = _DellNetCardDescription_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 2, 4, 1, 3),
    _DellNetCardDescription_Type()
)
dellNetCardDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetCardDescription.setStatus("current")
_DellNetCardChassisIndex_Type = Integer32
_DellNetCardChassisIndex_Object = MibTableColumn
dellNetCardChassisIndex = _DellNetCardChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 2, 4, 1, 4),
    _DellNetCardChassisIndex_Type()
)
dellNetCardChassisIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dellNetCardChassisIndex.setStatus("current")
_DellNetCardStatus_Type = DellNetCardOperStatus
_DellNetCardStatus_Object = MibTableColumn
dellNetCardStatus = _DellNetCardStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 2, 4, 1, 5),
    _DellNetCardStatus_Type()
)
dellNetCardStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetCardStatus.setStatus("current")
_DellNetCardTemp_Type = Integer32
_DellNetCardTemp_Object = MibTableColumn
dellNetCardTemp = _DellNetCardTemp_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 2, 4, 1, 6),
    _DellNetCardTemp_Type()
)
dellNetCardTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetCardTemp.setStatus("current")
if mibBuilder.loadTexts:
    dellNetCardTemp.setUnits("degrees Centigrade")
_DellNetCardVendorId_Type = DisplayString
_DellNetCardVendorId_Object = MibTableColumn
dellNetCardVendorId = _DellNetCardVendorId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 2, 4, 1, 7),
    _DellNetCardVendorId_Type()
)
dellNetCardVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetCardVendorId.setStatus("current")
_DellNetCardMfgDate_Type = DellNetMfgDate
_DellNetCardMfgDate_Object = MibTableColumn
dellNetCardMfgDate = _DellNetCardMfgDate_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 2, 4, 1, 8),
    _DellNetCardMfgDate_Type()
)
dellNetCardMfgDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetCardMfgDate.setStatus("current")
_DellNetCardPartNum_Type = DisplayString
_DellNetCardPartNum_Object = MibTableColumn
dellNetCardPartNum = _DellNetCardPartNum_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 2, 4, 1, 9),
    _DellNetCardPartNum_Type()
)
dellNetCardPartNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetCardPartNum.setStatus("current")
_DellNetCardProductRev_Type = DisplayString
_DellNetCardProductRev_Object = MibTableColumn
dellNetCardProductRev = _DellNetCardProductRev_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 2, 4, 1, 10),
    _DellNetCardProductRev_Type()
)
dellNetCardProductRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetCardProductRev.setStatus("current")
_DellNetCardProductOrder_Type = DisplayString
_DellNetCardProductOrder_Object = MibTableColumn
dellNetCardProductOrder = _DellNetCardProductOrder_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 2, 4, 1, 11),
    _DellNetCardProductOrder_Type()
)
dellNetCardProductOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetCardProductOrder.setStatus("current")


class _DellNetCardCountryCode_Type(OctetString):
    """Custom type dellNetCardCountryCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_DellNetCardCountryCode_Type.__name__ = "OctetString"
_DellNetCardCountryCode_Object = MibTableColumn
dellNetCardCountryCode = _DellNetCardCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 2, 4, 1, 12),
    _DellNetCardCountryCode_Type()
)
dellNetCardCountryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetCardCountryCode.setStatus("current")


class _DellNetCardPiecePartID_Type(DisplayString):
    """Custom type dellNetCardPiecePartID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_DellNetCardPiecePartID_Type.__name__ = "DisplayString"
_DellNetCardPiecePartID_Object = MibTableColumn
dellNetCardPiecePartID = _DellNetCardPiecePartID_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 2, 4, 1, 13),
    _DellNetCardPiecePartID_Type()
)
dellNetCardPiecePartID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetCardPiecePartID.setStatus("current")


class _DellNetCardPPIDRevision_Type(DisplayString):
    """Custom type dellNetCardPPIDRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_DellNetCardPPIDRevision_Type.__name__ = "DisplayString"
_DellNetCardPPIDRevision_Object = MibTableColumn
dellNetCardPPIDRevision = _DellNetCardPPIDRevision_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 2, 4, 1, 14),
    _DellNetCardPPIDRevision_Type()
)
dellNetCardPPIDRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetCardPPIDRevision.setStatus("current")


class _DellNetCardServiceTag_Type(DisplayString):
    """Custom type dellNetCardServiceTag based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_DellNetCardServiceTag_Type.__name__ = "DisplayString"
_DellNetCardServiceTag_Object = MibTableColumn
dellNetCardServiceTag = _DellNetCardServiceTag_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 2, 4, 1, 15),
    _DellNetCardServiceTag_Type()
)
dellNetCardServiceTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetCardServiceTag.setStatus("current")


class _DellNetCardExpServiceCode_Type(DisplayString):
    """Custom type dellNetCardExpServiceCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_DellNetCardExpServiceCode_Type.__name__ = "DisplayString"
_DellNetCardExpServiceCode_Object = MibTableColumn
dellNetCardExpServiceCode = _DellNetCardExpServiceCode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 2, 4, 1, 16),
    _DellNetCardExpServiceCode_Type()
)
dellNetCardExpServiceCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetCardExpServiceCode.setStatus("current")
_DellNetCardNumOfPorts_Type = Integer32
_DellNetCardNumOfPorts_Object = MibTableColumn
dellNetCardNumOfPorts = _DellNetCardNumOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 2, 4, 1, 17),
    _DellNetCardNumOfPorts_Type()
)
dellNetCardNumOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetCardNumOfPorts.setStatus("current")
_DellNetStackObject_ObjectIdentity = ObjectIdentity
dellNetStackObject = _DellNetStackObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 3)
)
_DellNetNumStackUnits_Type = Integer32
_DellNetNumStackUnits_Object = MibScalar
dellNetNumStackUnits = _DellNetNumStackUnits_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 3, 1),
    _DellNetNumStackUnits_Type()
)
dellNetNumStackUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetNumStackUnits.setStatus("current")
_DellNetMaxStackableUnits_Type = Integer32
_DellNetMaxStackableUnits_Object = MibScalar
dellNetMaxStackableUnits = _DellNetMaxStackableUnits_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 3, 2),
    _DellNetMaxStackableUnits_Type()
)
dellNetMaxStackableUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetMaxStackableUnits.setStatus("current")


class _DellNetStackUnitIndexNext_Type(Integer32):
    """Custom type dellNetStackUnitIndexNext based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 16),
    )


_DellNetStackUnitIndexNext_Type.__name__ = "Integer32"
_DellNetStackUnitIndexNext_Object = MibScalar
dellNetStackUnitIndexNext = _DellNetStackUnitIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 3, 3),
    _DellNetStackUnitIndexNext_Type()
)
dellNetStackUnitIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetStackUnitIndexNext.setStatus("current")
_DellNetStackUnitTable_Object = MibTable
dellNetStackUnitTable = _DellNetStackUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 3, 4)
)
if mibBuilder.loadTexts:
    dellNetStackUnitTable.setStatus("current")
_DellNetStackUnitEntry_Object = MibTableRow
dellNetStackUnitEntry = _DellNetStackUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 3, 4, 1)
)
dellNetStackUnitEntry.setIndexNames(
    (0, "DELL-NETWORKING-CHASSIS-MIB", "dellNetStackUnitIndex"),
)
if mibBuilder.loadTexts:
    dellNetStackUnitEntry.setStatus("current")
_DellNetStackUnitIndex_Type = Integer32
_DellNetStackUnitIndex_Object = MibTableColumn
dellNetStackUnitIndex = _DellNetStackUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 3, 4, 1, 1),
    _DellNetStackUnitIndex_Type()
)
dellNetStackUnitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dellNetStackUnitIndex.setStatus("current")


class _DellNetStackUnitNumber_Type(Integer32):
    """Custom type dellNetStackUnitNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 12),
    )


_DellNetStackUnitNumber_Type.__name__ = "Integer32"
_DellNetStackUnitNumber_Object = MibTableColumn
dellNetStackUnitNumber = _DellNetStackUnitNumber_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 3, 4, 1, 2),
    _DellNetStackUnitNumber_Type()
)
dellNetStackUnitNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetStackUnitNumber.setStatus("current")


class _DellNetStackUnitMgmtStatus_Type(Integer32):
    """Custom type dellNetStackUnitMgmtStatus based on Integer32"""
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
        *(("mgmtUnit", 1),
          ("stackUnit", 3),
          ("standbyUnit", 2),
          ("unassigned", 4))
    )


_DellNetStackUnitMgmtStatus_Type.__name__ = "Integer32"
_DellNetStackUnitMgmtStatus_Object = MibTableColumn
dellNetStackUnitMgmtStatus = _DellNetStackUnitMgmtStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 3, 4, 1, 4),
    _DellNetStackUnitMgmtStatus_Type()
)
dellNetStackUnitMgmtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetStackUnitMgmtStatus.setStatus("current")


class _DellNetStackUnitHwMgmtPreference_Type(Integer32):
    """Custom type dellNetStackUnitHwMgmtPreference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("assigned", 2),
          ("disabled", 0),
          ("unsassigned", 1))
    )


_DellNetStackUnitHwMgmtPreference_Type.__name__ = "Integer32"
_DellNetStackUnitHwMgmtPreference_Object = MibTableColumn
dellNetStackUnitHwMgmtPreference = _DellNetStackUnitHwMgmtPreference_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 3, 4, 1, 5),
    _DellNetStackUnitHwMgmtPreference_Type()
)
dellNetStackUnitHwMgmtPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetStackUnitHwMgmtPreference.setStatus("current")


class _DellNetStackUnitAdmMgmtPreference_Type(Integer32):
    """Custom type dellNetStackUnitAdmMgmtPreference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 15),
    )


_DellNetStackUnitAdmMgmtPreference_Type.__name__ = "Integer32"
_DellNetStackUnitAdmMgmtPreference_Object = MibTableColumn
dellNetStackUnitAdmMgmtPreference = _DellNetStackUnitAdmMgmtPreference_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 3, 4, 1, 6),
    _DellNetStackUnitAdmMgmtPreference_Type()
)
dellNetStackUnitAdmMgmtPreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetStackUnitAdmMgmtPreference.setStatus("current")
_DellNetStackUnitModelId_Type = DellNetChassisType
_DellNetStackUnitModelId_Object = MibTableColumn
dellNetStackUnitModelId = _DellNetStackUnitModelId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 3, 4, 1, 7),
    _DellNetStackUnitModelId_Type()
)
dellNetStackUnitModelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetStackUnitModelId.setStatus("current")


class _DellNetStackUnitStatus_Type(Integer32):
    """Custom type dellNetStackUnitStatus based on Integer32"""
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
        *(("codeMismatch", 3),
          ("configMismatch", 4),
          ("notPresent", 6),
          ("ok", 1),
          ("unitDown", 5),
          ("unsupported", 2))
    )


_DellNetStackUnitStatus_Type.__name__ = "Integer32"
_DellNetStackUnitStatus_Object = MibTableColumn
dellNetStackUnitStatus = _DellNetStackUnitStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 3, 4, 1, 8),
    _DellNetStackUnitStatus_Type()
)
dellNetStackUnitStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetStackUnitStatus.setStatus("current")
_DellNetStackUnitDescription_Type = DisplayString
_DellNetStackUnitDescription_Object = MibTableColumn
dellNetStackUnitDescription = _DellNetStackUnitDescription_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 3, 4, 1, 9),
    _DellNetStackUnitDescription_Type()
)
dellNetStackUnitDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetStackUnitDescription.setStatus("current")
_DellNetStackUnitCodeVersion_Type = DisplayString
_DellNetStackUnitCodeVersion_Object = MibTableColumn
dellNetStackUnitCodeVersion = _DellNetStackUnitCodeVersion_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 3, 4, 1, 10),
    _DellNetStackUnitCodeVersion_Type()
)
dellNetStackUnitCodeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetStackUnitCodeVersion.setStatus("current")
_DellNetStackUnitSerialNumber_Type = DisplayString
_DellNetStackUnitSerialNumber_Object = MibTableColumn
dellNetStackUnitSerialNumber = _DellNetStackUnitSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 3, 4, 1, 11),
    _DellNetStackUnitSerialNumber_Type()
)
dellNetStackUnitSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetStackUnitSerialNumber.setStatus("current")
_DellNetStackUnitUpTime_Type = TimeTicks
_DellNetStackUnitUpTime_Object = MibTableColumn
dellNetStackUnitUpTime = _DellNetStackUnitUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 3, 4, 1, 12),
    _DellNetStackUnitUpTime_Type()
)
dellNetStackUnitUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetStackUnitUpTime.setStatus("current")
_DellNetStackUnitTemp_Type = Gauge32
_DellNetStackUnitTemp_Object = MibTableColumn
dellNetStackUnitTemp = _DellNetStackUnitTemp_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 3, 4, 1, 13),
    _DellNetStackUnitTemp_Type()
)
dellNetStackUnitTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetStackUnitTemp.setStatus("current")
_DellNetStackUnitVendorId_Type = DisplayString
_DellNetStackUnitVendorId_Object = MibTableColumn
dellNetStackUnitVendorId = _DellNetStackUnitVendorId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 3, 4, 1, 14),
    _DellNetStackUnitVendorId_Type()
)
dellNetStackUnitVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetStackUnitVendorId.setStatus("current")
_DellNetStackUnitMfgDate_Type = DellNetMfgDate
_DellNetStackUnitMfgDate_Object = MibTableColumn
dellNetStackUnitMfgDate = _DellNetStackUnitMfgDate_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 3, 4, 1, 15),
    _DellNetStackUnitMfgDate_Type()
)
dellNetStackUnitMfgDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetStackUnitMfgDate.setStatus("current")
_DellNetStackUnitMacAddress_Type = MacAddress
_DellNetStackUnitMacAddress_Object = MibTableColumn
dellNetStackUnitMacAddress = _DellNetStackUnitMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 3, 4, 1, 16),
    _DellNetStackUnitMacAddress_Type()
)
dellNetStackUnitMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetStackUnitMacAddress.setStatus("current")
_DellNetStackUnitPartNum_Type = DisplayString
_DellNetStackUnitPartNum_Object = MibTableColumn
dellNetStackUnitPartNum = _DellNetStackUnitPartNum_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 3, 4, 1, 17),
    _DellNetStackUnitPartNum_Type()
)
dellNetStackUnitPartNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetStackUnitPartNum.setStatus("current")
_DellNetStackUnitProductRev_Type = DisplayString
_DellNetStackUnitProductRev_Object = MibTableColumn
dellNetStackUnitProductRev = _DellNetStackUnitProductRev_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 3, 4, 1, 18),
    _DellNetStackUnitProductRev_Type()
)
dellNetStackUnitProductRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetStackUnitProductRev.setStatus("current")
_DellNetStackUnitProductOrder_Type = DisplayString
_DellNetStackUnitProductOrder_Object = MibTableColumn
dellNetStackUnitProductOrder = _DellNetStackUnitProductOrder_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 3, 4, 1, 19),
    _DellNetStackUnitProductOrder_Type()
)
dellNetStackUnitProductOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetStackUnitProductOrder.setStatus("current")


class _DellNetStackUnitCountryCode_Type(OctetString):
    """Custom type dellNetStackUnitCountryCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_DellNetStackUnitCountryCode_Type.__name__ = "OctetString"
_DellNetStackUnitCountryCode_Object = MibTableColumn
dellNetStackUnitCountryCode = _DellNetStackUnitCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 3, 4, 1, 20),
    _DellNetStackUnitCountryCode_Type()
)
dellNetStackUnitCountryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetStackUnitCountryCode.setStatus("current")


class _DellNetStackUnitPiecePartID_Type(DisplayString):
    """Custom type dellNetStackUnitPiecePartID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_DellNetStackUnitPiecePartID_Type.__name__ = "DisplayString"
_DellNetStackUnitPiecePartID_Object = MibTableColumn
dellNetStackUnitPiecePartID = _DellNetStackUnitPiecePartID_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 3, 4, 1, 21),
    _DellNetStackUnitPiecePartID_Type()
)
dellNetStackUnitPiecePartID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetStackUnitPiecePartID.setStatus("current")


class _DellNetStackUnitPPIDRevision_Type(DisplayString):
    """Custom type dellNetStackUnitPPIDRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_DellNetStackUnitPPIDRevision_Type.__name__ = "DisplayString"
_DellNetStackUnitPPIDRevision_Object = MibTableColumn
dellNetStackUnitPPIDRevision = _DellNetStackUnitPPIDRevision_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 3, 4, 1, 22),
    _DellNetStackUnitPPIDRevision_Type()
)
dellNetStackUnitPPIDRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetStackUnitPPIDRevision.setStatus("current")


class _DellNetStackUnitServiceTag_Type(DisplayString):
    """Custom type dellNetStackUnitServiceTag based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_DellNetStackUnitServiceTag_Type.__name__ = "DisplayString"
_DellNetStackUnitServiceTag_Object = MibTableColumn
dellNetStackUnitServiceTag = _DellNetStackUnitServiceTag_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 3, 4, 1, 23),
    _DellNetStackUnitServiceTag_Type()
)
dellNetStackUnitServiceTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetStackUnitServiceTag.setStatus("current")


class _DellNetStackUnitExpServiceCode_Type(DisplayString):
    """Custom type dellNetStackUnitExpServiceCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_DellNetStackUnitExpServiceCode_Type.__name__ = "DisplayString"
_DellNetStackUnitExpServiceCode_Object = MibTableColumn
dellNetStackUnitExpServiceCode = _DellNetStackUnitExpServiceCode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 3, 4, 1, 24),
    _DellNetStackUnitExpServiceCode_Type()
)
dellNetStackUnitExpServiceCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetStackUnitExpServiceCode.setStatus("current")
_DellNetStackUnitNumOfPorts_Type = Integer32
_DellNetStackUnitNumOfPorts_Object = MibTableColumn
dellNetStackUnitNumOfPorts = _DellNetStackUnitNumOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 3, 4, 1, 25),
    _DellNetStackUnitNumOfPorts_Type()
)
dellNetStackUnitNumOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetStackUnitNumOfPorts.setStatus("current")
_DellNetStackUnitNumFanTrays_Type = Integer32
_DellNetStackUnitNumFanTrays_Object = MibTableColumn
dellNetStackUnitNumFanTrays = _DellNetStackUnitNumFanTrays_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 3, 4, 1, 26),
    _DellNetStackUnitNumFanTrays_Type()
)
dellNetStackUnitNumFanTrays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetStackUnitNumFanTrays.setStatus("current")
_DellNetStackUnitNumPowerSupplies_Type = Integer32
_DellNetStackUnitNumPowerSupplies_Object = MibTableColumn
dellNetStackUnitNumPowerSupplies = _DellNetStackUnitNumPowerSupplies_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 3, 4, 1, 27),
    _DellNetStackUnitNumPowerSupplies_Type()
)
dellNetStackUnitNumPowerSupplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetStackUnitNumPowerSupplies.setStatus("current")
_DellNetStackUnitNumPluggableModules_Type = Integer32
_DellNetStackUnitNumPluggableModules_Object = MibTableColumn
dellNetStackUnitNumPluggableModules = _DellNetStackUnitNumPluggableModules_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 3, 4, 1, 28),
    _DellNetStackUnitNumPluggableModules_Type()
)
dellNetStackUnitNumPluggableModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetStackUnitNumPluggableModules.setStatus("current")
_DellNetStackPortTable_Object = MibTable
dellNetStackPortTable = _DellNetStackPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 3, 5)
)
if mibBuilder.loadTexts:
    dellNetStackPortTable.setStatus("current")
_DellNetStackPortEntry_Object = MibTableRow
dellNetStackPortEntry = _DellNetStackPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 3, 5, 1)
)
dellNetStackPortEntry.setIndexNames(
    (0, "DELL-NETWORKING-CHASSIS-MIB", "dellNetStackUnitNumber"),
    (0, "DELL-NETWORKING-CHASSIS-MIB", "dellNetStackPortIndex"),
)
if mibBuilder.loadTexts:
    dellNetStackPortEntry.setStatus("current")
_DellNetStackPortIndex_Type = Integer32
_DellNetStackPortIndex_Object = MibTableColumn
dellNetStackPortIndex = _DellNetStackPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 3, 5, 1, 1),
    _DellNetStackPortIndex_Type()
)
dellNetStackPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetStackPortIndex.setStatus("current")


class _DellNetStackPortConfiguredMode_Type(Integer32):
    """Custom type dellNetStackPortConfiguredMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 2),
          ("stack", 1),
          ("unknown", 3))
    )


_DellNetStackPortConfiguredMode_Type.__name__ = "Integer32"
_DellNetStackPortConfiguredMode_Object = MibTableColumn
dellNetStackPortConfiguredMode = _DellNetStackPortConfiguredMode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 3, 5, 1, 2),
    _DellNetStackPortConfiguredMode_Type()
)
dellNetStackPortConfiguredMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetStackPortConfiguredMode.setStatus("current")


class _DellNetStackPortRunningMode_Type(Integer32):
    """Custom type dellNetStackPortRunningMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 2),
          ("stack", 1),
          ("unknown", 3))
    )


_DellNetStackPortRunningMode_Type.__name__ = "Integer32"
_DellNetStackPortRunningMode_Object = MibTableColumn
dellNetStackPortRunningMode = _DellNetStackPortRunningMode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 3, 5, 1, 3),
    _DellNetStackPortRunningMode_Type()
)
dellNetStackPortRunningMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetStackPortRunningMode.setStatus("current")


class _DellNetStackPortLinkStatus_Type(Integer32):
    """Custom type dellNetStackPortLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_DellNetStackPortLinkStatus_Type.__name__ = "Integer32"
_DellNetStackPortLinkStatus_Object = MibTableColumn
dellNetStackPortLinkStatus = _DellNetStackPortLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 3, 5, 1, 4),
    _DellNetStackPortLinkStatus_Type()
)
dellNetStackPortLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetStackPortLinkStatus.setStatus("current")
_DellNetStackPortLinkSpeed_Type = Gauge32
_DellNetStackPortLinkSpeed_Object = MibTableColumn
dellNetStackPortLinkSpeed = _DellNetStackPortLinkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 3, 5, 1, 5),
    _DellNetStackPortLinkSpeed_Type()
)
dellNetStackPortLinkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetStackPortLinkSpeed.setStatus("current")
_DellNetStackPortRxDataRate_Type = Counter32
_DellNetStackPortRxDataRate_Object = MibTableColumn
dellNetStackPortRxDataRate = _DellNetStackPortRxDataRate_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 3, 5, 1, 6),
    _DellNetStackPortRxDataRate_Type()
)
dellNetStackPortRxDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetStackPortRxDataRate.setStatus("current")
_DellNetStackPortRxErrorRate_Type = Counter32
_DellNetStackPortRxErrorRate_Object = MibTableColumn
dellNetStackPortRxErrorRate = _DellNetStackPortRxErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 3, 5, 1, 7),
    _DellNetStackPortRxErrorRate_Type()
)
dellNetStackPortRxErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetStackPortRxErrorRate.setStatus("current")
_DellNetStackPortRxTotalErrors_Type = Counter32
_DellNetStackPortRxTotalErrors_Object = MibTableColumn
dellNetStackPortRxTotalErrors = _DellNetStackPortRxTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 3, 5, 1, 8),
    _DellNetStackPortRxTotalErrors_Type()
)
dellNetStackPortRxTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetStackPortRxTotalErrors.setStatus("current")
_DellNetStackPortTxDataRate_Type = Counter32
_DellNetStackPortTxDataRate_Object = MibTableColumn
dellNetStackPortTxDataRate = _DellNetStackPortTxDataRate_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 3, 5, 1, 9),
    _DellNetStackPortTxDataRate_Type()
)
dellNetStackPortTxDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetStackPortTxDataRate.setStatus("current")
_DellNetStackPortTxErrorRate_Type = Counter32
_DellNetStackPortTxErrorRate_Object = MibTableColumn
dellNetStackPortTxErrorRate = _DellNetStackPortTxErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 3, 5, 1, 10),
    _DellNetStackPortTxErrorRate_Type()
)
dellNetStackPortTxErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetStackPortTxErrorRate.setStatus("current")
_DellNetStackPortTxTotalErrors_Type = Counter32
_DellNetStackPortTxTotalErrors_Object = MibTableColumn
dellNetStackPortTxTotalErrors = _DellNetStackPortTxTotalErrors_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 3, 5, 1, 11),
    _DellNetStackPortTxTotalErrors_Type()
)
dellNetStackPortTxTotalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetStackPortTxTotalErrors.setStatus("current")
_DellNetSystemComponent_ObjectIdentity = ObjectIdentity
dellNetSystemComponent = _DellNetSystemComponent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4)
)
_DellNetPEBindingTable_Object = MibTable
dellNetPEBindingTable = _DellNetPEBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 1)
)
if mibBuilder.loadTexts:
    dellNetPEBindingTable.setStatus("current")
_DellNetPEBindingEntry_Object = MibTableRow
dellNetPEBindingEntry = _DellNetPEBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 1, 1)
)
dellNetPEBindingEntry.setIndexNames(
    (0, "DELL-NETWORKING-CHASSIS-MIB", "dellNetPEBindCascadePortIfIndex"),
)
if mibBuilder.loadTexts:
    dellNetPEBindingEntry.setStatus("current")
_DellNetPEBindCascadePortIfIndex_Type = InterfaceIndex
_DellNetPEBindCascadePortIfIndex_Object = MibTableColumn
dellNetPEBindCascadePortIfIndex = _DellNetPEBindCascadePortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 1, 1, 1),
    _DellNetPEBindCascadePortIfIndex_Type()
)
dellNetPEBindCascadePortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dellNetPEBindCascadePortIfIndex.setStatus("current")
_DellNetPEBindPEIndex_Type = Integer32
_DellNetPEBindPEIndex_Object = MibTableColumn
dellNetPEBindPEIndex = _DellNetPEBindPEIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 1, 1, 2),
    _DellNetPEBindPEIndex_Type()
)
dellNetPEBindPEIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetPEBindPEIndex.setStatus("current")
_DellNetPETable_Object = MibTable
dellNetPETable = _DellNetPETable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 2)
)
if mibBuilder.loadTexts:
    dellNetPETable.setStatus("current")
_DellNetPEEntry_Object = MibTableRow
dellNetPEEntry = _DellNetPEEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 2, 1)
)
dellNetPEEntry.setIndexNames(
    (0, "DELL-NETWORKING-CHASSIS-MIB", "dellNetPEIndex"),
)
if mibBuilder.loadTexts:
    dellNetPEEntry.setStatus("current")
_DellNetPEIndex_Type = Integer32
_DellNetPEIndex_Object = MibTableColumn
dellNetPEIndex = _DellNetPEIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 2, 1, 1),
    _DellNetPEIndex_Type()
)
dellNetPEIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dellNetPEIndex.setStatus("current")


class _DellNetPEPEID_Type(Integer32):
    """Custom type dellNetPEPEID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DellNetPEPEID_Type.__name__ = "Integer32"
_DellNetPEPEID_Object = MibTableColumn
dellNetPEPEID = _DellNetPEPEID_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 2, 1, 2),
    _DellNetPEPEID_Type()
)
dellNetPEPEID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetPEPEID.setStatus("current")


class _DellNetPEUnitID_Type(Integer32):
    """Custom type dellNetPEUnitID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_DellNetPEUnitID_Type.__name__ = "Integer32"
_DellNetPEUnitID_Object = MibTableColumn
dellNetPEUnitID = _DellNetPEUnitID_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 2, 1, 3),
    _DellNetPEUnitID_Type()
)
dellNetPEUnitID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetPEUnitID.setStatus("current")
_DellNetPEType_Type = DellNetChassisType
_DellNetPEType_Object = MibTableColumn
dellNetPEType = _DellNetPEType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 2, 1, 4),
    _DellNetPEType_Type()
)
dellNetPEType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetPEType.setStatus("current")


class _DellNetPEDescription_Type(DisplayString):
    """Custom type dellNetPEDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_DellNetPEDescription_Type.__name__ = "DisplayString"
_DellNetPEDescription_Object = MibTableColumn
dellNetPEDescription = _DellNetPEDescription_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 2, 1, 5),
    _DellNetPEDescription_Type()
)
dellNetPEDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetPEDescription.setStatus("current")
_DellNetPEStatus_Type = DellNetPEOperStatus
_DellNetPEStatus_Object = MibTableColumn
dellNetPEStatus = _DellNetPEStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 2, 1, 6),
    _DellNetPEStatus_Type()
)
dellNetPEStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetPEStatus.setStatus("current")
_DellNetPETemp_Type = Integer32
_DellNetPETemp_Object = MibTableColumn
dellNetPETemp = _DellNetPETemp_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 2, 1, 7),
    _DellNetPETemp_Type()
)
dellNetPETemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetPETemp.setStatus("current")
if mibBuilder.loadTexts:
    dellNetPETemp.setUnits("degrees Centigrade")
_DellNetPEVendorId_Type = DisplayString
_DellNetPEVendorId_Object = MibTableColumn
dellNetPEVendorId = _DellNetPEVendorId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 2, 1, 8),
    _DellNetPEVendorId_Type()
)
dellNetPEVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetPEVendorId.setStatus("current")
_DellNetPEMfgDate_Type = DellNetMfgDate
_DellNetPEMfgDate_Object = MibTableColumn
dellNetPEMfgDate = _DellNetPEMfgDate_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 2, 1, 9),
    _DellNetPEMfgDate_Type()
)
dellNetPEMfgDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetPEMfgDate.setStatus("current")
_DellNetPEPartNum_Type = DisplayString
_DellNetPEPartNum_Object = MibTableColumn
dellNetPEPartNum = _DellNetPEPartNum_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 2, 1, 10),
    _DellNetPEPartNum_Type()
)
dellNetPEPartNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetPEPartNum.setStatus("current")
_DellNetPEProductRev_Type = DisplayString
_DellNetPEProductRev_Object = MibTableColumn
dellNetPEProductRev = _DellNetPEProductRev_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 2, 1, 11),
    _DellNetPEProductRev_Type()
)
dellNetPEProductRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetPEProductRev.setStatus("current")
_DellNetPEProductOrder_Type = DisplayString
_DellNetPEProductOrder_Object = MibTableColumn
dellNetPEProductOrder = _DellNetPEProductOrder_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 2, 1, 12),
    _DellNetPEProductOrder_Type()
)
dellNetPEProductOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetPEProductOrder.setStatus("current")


class _DellNetPECountryCode_Type(OctetString):
    """Custom type dellNetPECountryCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_DellNetPECountryCode_Type.__name__ = "OctetString"
_DellNetPECountryCode_Object = MibTableColumn
dellNetPECountryCode = _DellNetPECountryCode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 2, 1, 13),
    _DellNetPECountryCode_Type()
)
dellNetPECountryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetPECountryCode.setStatus("current")


class _DellNetPEPiecePartID_Type(DisplayString):
    """Custom type dellNetPEPiecePartID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_DellNetPEPiecePartID_Type.__name__ = "DisplayString"
_DellNetPEPiecePartID_Object = MibTableColumn
dellNetPEPiecePartID = _DellNetPEPiecePartID_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 2, 1, 14),
    _DellNetPEPiecePartID_Type()
)
dellNetPEPiecePartID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetPEPiecePartID.setStatus("current")


class _DellNetPEPPIDRevision_Type(DisplayString):
    """Custom type dellNetPEPPIDRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_DellNetPEPPIDRevision_Type.__name__ = "DisplayString"
_DellNetPEPPIDRevision_Object = MibTableColumn
dellNetPEPPIDRevision = _DellNetPEPPIDRevision_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 2, 1, 15),
    _DellNetPEPPIDRevision_Type()
)
dellNetPEPPIDRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetPEPPIDRevision.setStatus("current")


class _DellNetPEServiceTag_Type(DisplayString):
    """Custom type dellNetPEServiceTag based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_DellNetPEServiceTag_Type.__name__ = "DisplayString"
_DellNetPEServiceTag_Object = MibTableColumn
dellNetPEServiceTag = _DellNetPEServiceTag_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 2, 1, 16),
    _DellNetPEServiceTag_Type()
)
dellNetPEServiceTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetPEServiceTag.setStatus("current")


class _DellNetPEExpServiceCode_Type(DisplayString):
    """Custom type dellNetPEExpServiceCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_DellNetPEExpServiceCode_Type.__name__ = "DisplayString"
_DellNetPEExpServiceCode_Object = MibTableColumn
dellNetPEExpServiceCode = _DellNetPEExpServiceCode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 2, 1, 17),
    _DellNetPEExpServiceCode_Type()
)
dellNetPEExpServiceCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetPEExpServiceCode.setStatus("current")
_DellNetPENumOfPorts_Type = Integer32
_DellNetPENumOfPorts_Object = MibTableColumn
dellNetPENumOfPorts = _DellNetPENumOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 2, 1, 18),
    _DellNetPENumOfPorts_Type()
)
dellNetPENumOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetPENumOfPorts.setStatus("current")
_DellNetPENumFanTrays_Type = Integer32
_DellNetPENumFanTrays_Object = MibTableColumn
dellNetPENumFanTrays = _DellNetPENumFanTrays_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 2, 1, 19),
    _DellNetPENumFanTrays_Type()
)
dellNetPENumFanTrays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetPENumFanTrays.setStatus("current")
_DellNetPENumPowerSupplies_Type = Integer32
_DellNetPENumPowerSupplies_Object = MibTableColumn
dellNetPENumPowerSupplies = _DellNetPENumPowerSupplies_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 2, 1, 20),
    _DellNetPENumPowerSupplies_Type()
)
dellNetPENumPowerSupplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetPENumPowerSupplies.setStatus("current")
_DellNetPENumPluggableModules_Type = Integer32
_DellNetPENumPluggableModules_Object = MibTableColumn
dellNetPENumPluggableModules = _DellNetPENumPluggableModules_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 2, 1, 21),
    _DellNetPENumPluggableModules_Type()
)
dellNetPENumPluggableModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetPENumPluggableModules.setStatus("current")
_DellNetProcessorTable_Object = MibTable
dellNetProcessorTable = _DellNetProcessorTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 3)
)
if mibBuilder.loadTexts:
    dellNetProcessorTable.setStatus("current")
_DellNetProcessorEntry_Object = MibTableRow
dellNetProcessorEntry = _DellNetProcessorEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 3, 1)
)
dellNetProcessorEntry.setIndexNames(
    (0, "DELL-NETWORKING-CHASSIS-MIB", "dellNetProcessorDeviceType"),
    (0, "DELL-NETWORKING-CHASSIS-MIB", "dellNetProcessorDeviceIndex"),
    (0, "DELL-NETWORKING-CHASSIS-MIB", "dellNetProcessorIndex"),
)
if mibBuilder.loadTexts:
    dellNetProcessorEntry.setStatus("current")
_DellNetProcessorDeviceType_Type = DellNetDeviceType
_DellNetProcessorDeviceType_Object = MibTableColumn
dellNetProcessorDeviceType = _DellNetProcessorDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 3, 1, 1),
    _DellNetProcessorDeviceType_Type()
)
dellNetProcessorDeviceType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dellNetProcessorDeviceType.setStatus("current")
_DellNetProcessorDeviceIndex_Type = Integer32
_DellNetProcessorDeviceIndex_Object = MibTableColumn
dellNetProcessorDeviceIndex = _DellNetProcessorDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 3, 1, 2),
    _DellNetProcessorDeviceIndex_Type()
)
dellNetProcessorDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dellNetProcessorDeviceIndex.setStatus("current")
_DellNetProcessorIndex_Type = Integer32
_DellNetProcessorIndex_Object = MibTableColumn
dellNetProcessorIndex = _DellNetProcessorIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 3, 1, 3),
    _DellNetProcessorIndex_Type()
)
dellNetProcessorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dellNetProcessorIndex.setStatus("current")
_DellNetProcessorModule_Type = DellNetProcessorModuleType
_DellNetProcessorModule_Object = MibTableColumn
dellNetProcessorModule = _DellNetProcessorModule_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 3, 1, 4),
    _DellNetProcessorModule_Type()
)
dellNetProcessorModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetProcessorModule.setStatus("current")
_DellNetProcessorUpTime_Type = TimeTicks
_DellNetProcessorUpTime_Object = MibTableColumn
dellNetProcessorUpTime = _DellNetProcessorUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 3, 1, 5),
    _DellNetProcessorUpTime_Type()
)
dellNetProcessorUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetProcessorUpTime.setStatus("current")
_DellNetProcessorMemSize_Type = Integer32
_DellNetProcessorMemSize_Object = MibTableColumn
dellNetProcessorMemSize = _DellNetProcessorMemSize_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 3, 1, 6),
    _DellNetProcessorMemSize_Type()
)
dellNetProcessorMemSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetProcessorMemSize.setStatus("current")
_DellNetCpuUtilTable_Object = MibTable
dellNetCpuUtilTable = _DellNetCpuUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 4)
)
if mibBuilder.loadTexts:
    dellNetCpuUtilTable.setStatus("current")
_DellNetCpuUtilEntry_Object = MibTableRow
dellNetCpuUtilEntry = _DellNetCpuUtilEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 4, 1)
)
dellNetCpuUtilEntry.setIndexNames(
    (0, "DELL-NETWORKING-CHASSIS-MIB", "dellNetProcessorDeviceType"),
    (0, "DELL-NETWORKING-CHASSIS-MIB", "dellNetProcessorDeviceIndex"),
    (0, "DELL-NETWORKING-CHASSIS-MIB", "dellNetProcessorIndex"),
)
if mibBuilder.loadTexts:
    dellNetCpuUtilEntry.setStatus("current")


class _DellNetCpuUtil5Sec_Type(Gauge32):
    """Custom type dellNetCpuUtil5Sec based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DellNetCpuUtil5Sec_Type.__name__ = "Gauge32"
_DellNetCpuUtil5Sec_Object = MibTableColumn
dellNetCpuUtil5Sec = _DellNetCpuUtil5Sec_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 4, 1, 1),
    _DellNetCpuUtil5Sec_Type()
)
dellNetCpuUtil5Sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetCpuUtil5Sec.setStatus("current")
if mibBuilder.loadTexts:
    dellNetCpuUtil5Sec.setUnits("percent")


class _DellNetCpuUtil1Min_Type(Gauge32):
    """Custom type dellNetCpuUtil1Min based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DellNetCpuUtil1Min_Type.__name__ = "Gauge32"
_DellNetCpuUtil1Min_Object = MibTableColumn
dellNetCpuUtil1Min = _DellNetCpuUtil1Min_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 4, 1, 4),
    _DellNetCpuUtil1Min_Type()
)
dellNetCpuUtil1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetCpuUtil1Min.setStatus("current")
if mibBuilder.loadTexts:
    dellNetCpuUtil1Min.setUnits("percent")


class _DellNetCpuUtil5Min_Type(Gauge32):
    """Custom type dellNetCpuUtil5Min based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DellNetCpuUtil5Min_Type.__name__ = "Gauge32"
_DellNetCpuUtil5Min_Object = MibTableColumn
dellNetCpuUtil5Min = _DellNetCpuUtil5Min_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 4, 1, 5),
    _DellNetCpuUtil5Min_Type()
)
dellNetCpuUtil5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetCpuUtil5Min.setStatus("current")
if mibBuilder.loadTexts:
    dellNetCpuUtil5Min.setUnits("percent")


class _DellNetCpuUtilMemUsage_Type(Gauge32):
    """Custom type dellNetCpuUtilMemUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DellNetCpuUtilMemUsage_Type.__name__ = "Gauge32"
_DellNetCpuUtilMemUsage_Object = MibTableColumn
dellNetCpuUtilMemUsage = _DellNetCpuUtilMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 4, 1, 6),
    _DellNetCpuUtilMemUsage_Type()
)
dellNetCpuUtilMemUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetCpuUtilMemUsage.setStatus("current")
if mibBuilder.loadTexts:
    dellNetCpuUtilMemUsage.setUnits("percent")


class _DellNetCpuFlashUsageUtil_Type(Gauge32):
    """Custom type dellNetCpuFlashUsageUtil based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DellNetCpuFlashUsageUtil_Type.__name__ = "Gauge32"
_DellNetCpuFlashUsageUtil_Object = MibTableColumn
dellNetCpuFlashUsageUtil = _DellNetCpuFlashUsageUtil_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 4, 1, 7),
    _DellNetCpuFlashUsageUtil_Type()
)
dellNetCpuFlashUsageUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetCpuFlashUsageUtil.setStatus("current")
if mibBuilder.loadTexts:
    dellNetCpuFlashUsageUtil.setUnits("percent")
_DellNetSwModuleTable_Object = MibTable
dellNetSwModuleTable = _DellNetSwModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 5)
)
if mibBuilder.loadTexts:
    dellNetSwModuleTable.setStatus("current")
_DellNetSwModuleEntry_Object = MibTableRow
dellNetSwModuleEntry = _DellNetSwModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 5, 1)
)
dellNetSwModuleEntry.setIndexNames(
    (0, "DELL-NETWORKING-CHASSIS-MIB", "dellNetProcessorDeviceType"),
    (0, "DELL-NETWORKING-CHASSIS-MIB", "dellNetProcessorDeviceIndex"),
)
if mibBuilder.loadTexts:
    dellNetSwModuleEntry.setStatus("current")


class _DellNetSwModuleRuntimeImgVersion_Type(DisplayString):
    """Custom type dellNetSwModuleRuntimeImgVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DellNetSwModuleRuntimeImgVersion_Type.__name__ = "DisplayString"
_DellNetSwModuleRuntimeImgVersion_Object = MibTableColumn
dellNetSwModuleRuntimeImgVersion = _DellNetSwModuleRuntimeImgVersion_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 5, 1, 1),
    _DellNetSwModuleRuntimeImgVersion_Type()
)
dellNetSwModuleRuntimeImgVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetSwModuleRuntimeImgVersion.setStatus("current")


class _DellNetSwModuleRuntimeImgDate_Type(DellNetSwDate):
    """Custom type dellNetSwModuleRuntimeImgDate based on DellNetSwDate"""
    subtypeSpec = DellNetSwDate.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_DellNetSwModuleRuntimeImgDate_Type.__name__ = "DellNetSwDate"
_DellNetSwModuleRuntimeImgDate_Object = MibTableColumn
dellNetSwModuleRuntimeImgDate = _DellNetSwModuleRuntimeImgDate_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 5, 1, 2),
    _DellNetSwModuleRuntimeImgDate_Type()
)
dellNetSwModuleRuntimeImgDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetSwModuleRuntimeImgDate.setStatus("current")


class _DellNetSwModuleBootFlashImgVersion_Type(DisplayString):
    """Custom type dellNetSwModuleBootFlashImgVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DellNetSwModuleBootFlashImgVersion_Type.__name__ = "DisplayString"
_DellNetSwModuleBootFlashImgVersion_Object = MibTableColumn
dellNetSwModuleBootFlashImgVersion = _DellNetSwModuleBootFlashImgVersion_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 5, 1, 3),
    _DellNetSwModuleBootFlashImgVersion_Type()
)
dellNetSwModuleBootFlashImgVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetSwModuleBootFlashImgVersion.setStatus("current")


class _DellNetSwModuleBootSelectorImgVersion_Type(DisplayString):
    """Custom type dellNetSwModuleBootSelectorImgVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DellNetSwModuleBootSelectorImgVersion_Type.__name__ = "DisplayString"
_DellNetSwModuleBootSelectorImgVersion_Object = MibTableColumn
dellNetSwModuleBootSelectorImgVersion = _DellNetSwModuleBootSelectorImgVersion_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 5, 1, 4),
    _DellNetSwModuleBootSelectorImgVersion_Type()
)
dellNetSwModuleBootSelectorImgVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetSwModuleBootSelectorImgVersion.setStatus("current")


class _DellNetSwModuleNextRebootImage_Type(Integer32):
    """Custom type dellNetSwModuleNextRebootImage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("networkBoot", 3),
          ("partitionA", 1),
          ("partitionB", 2))
    )


_DellNetSwModuleNextRebootImage_Type.__name__ = "Integer32"
_DellNetSwModuleNextRebootImage_Object = MibTableColumn
dellNetSwModuleNextRebootImage = _DellNetSwModuleNextRebootImage_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 5, 1, 5),
    _DellNetSwModuleNextRebootImage_Type()
)
dellNetSwModuleNextRebootImage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetSwModuleNextRebootImage.setStatus("current")


class _DellNetSwModuleCurrentBootImage_Type(Integer32):
    """Custom type dellNetSwModuleCurrentBootImage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("networkBoot", 3),
          ("partitionA", 1),
          ("partitionB", 2))
    )


_DellNetSwModuleCurrentBootImage_Type.__name__ = "Integer32"
_DellNetSwModuleCurrentBootImage_Object = MibTableColumn
dellNetSwModuleCurrentBootImage = _DellNetSwModuleCurrentBootImage_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 5, 1, 6),
    _DellNetSwModuleCurrentBootImage_Type()
)
dellNetSwModuleCurrentBootImage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetSwModuleCurrentBootImage.setStatus("current")


class _DellNetSwModuleInPartitionAImgVers_Type(DisplayString):
    """Custom type dellNetSwModuleInPartitionAImgVers based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DellNetSwModuleInPartitionAImgVers_Type.__name__ = "DisplayString"
_DellNetSwModuleInPartitionAImgVers_Object = MibTableColumn
dellNetSwModuleInPartitionAImgVers = _DellNetSwModuleInPartitionAImgVers_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 5, 1, 7),
    _DellNetSwModuleInPartitionAImgVers_Type()
)
dellNetSwModuleInPartitionAImgVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetSwModuleInPartitionAImgVers.setStatus("current")


class _DellNetSwModuleInPartitionBImgVers_Type(DisplayString):
    """Custom type dellNetSwModuleInPartitionBImgVers based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DellNetSwModuleInPartitionBImgVers_Type.__name__ = "DisplayString"
_DellNetSwModuleInPartitionBImgVers_Object = MibTableColumn
dellNetSwModuleInPartitionBImgVers = _DellNetSwModuleInPartitionBImgVers_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 5, 1, 8),
    _DellNetSwModuleInPartitionBImgVers_Type()
)
dellNetSwModuleInPartitionBImgVers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetSwModuleInPartitionBImgVers.setStatus("current")
_DellNetPowerSupplyTable_Object = MibTable
dellNetPowerSupplyTable = _DellNetPowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 6)
)
if mibBuilder.loadTexts:
    dellNetPowerSupplyTable.setStatus("current")
_DellNetPowerSupplyEntry_Object = MibTableRow
dellNetPowerSupplyEntry = _DellNetPowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 6, 1)
)
dellNetPowerSupplyEntry.setIndexNames(
    (0, "DELL-NETWORKING-CHASSIS-MIB", "dellNetPowerDeviceType"),
    (0, "DELL-NETWORKING-CHASSIS-MIB", "dellNetPowerDeviceIndex"),
    (0, "DELL-NETWORKING-CHASSIS-MIB", "dellNetPowerSupplyIndex"),
)
if mibBuilder.loadTexts:
    dellNetPowerSupplyEntry.setStatus("current")
_DellNetPowerDeviceType_Type = DellNetDeviceType
_DellNetPowerDeviceType_Object = MibTableColumn
dellNetPowerDeviceType = _DellNetPowerDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 6, 1, 1),
    _DellNetPowerDeviceType_Type()
)
dellNetPowerDeviceType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dellNetPowerDeviceType.setStatus("current")
_DellNetPowerDeviceIndex_Type = Integer32
_DellNetPowerDeviceIndex_Object = MibTableColumn
dellNetPowerDeviceIndex = _DellNetPowerDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 6, 1, 2),
    _DellNetPowerDeviceIndex_Type()
)
dellNetPowerDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dellNetPowerDeviceIndex.setStatus("current")
_DellNetPowerSupplyIndex_Type = Integer32
_DellNetPowerSupplyIndex_Object = MibTableColumn
dellNetPowerSupplyIndex = _DellNetPowerSupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 6, 1, 3),
    _DellNetPowerSupplyIndex_Type()
)
dellNetPowerSupplyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetPowerSupplyIndex.setStatus("current")


class _DellNetPowerSupplyOperStatus_Type(Integer32):
    """Custom type dellNetPowerSupplyOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("absent", 3),
          ("down", 2),
          ("up", 1))
    )


_DellNetPowerSupplyOperStatus_Type.__name__ = "Integer32"
_DellNetPowerSupplyOperStatus_Object = MibTableColumn
dellNetPowerSupplyOperStatus = _DellNetPowerSupplyOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 6, 1, 4),
    _DellNetPowerSupplyOperStatus_Type()
)
dellNetPowerSupplyOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetPowerSupplyOperStatus.setStatus("current")


class _DellNetPowerSupplyType_Type(Integer32):
    """Custom type dellNetPowerSupplyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ac", 2),
          ("dc", 3),
          ("unknown", 1))
    )


_DellNetPowerSupplyType_Type.__name__ = "Integer32"
_DellNetPowerSupplyType_Object = MibTableColumn
dellNetPowerSupplyType = _DellNetPowerSupplyType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 6, 1, 5),
    _DellNetPowerSupplyType_Type()
)
dellNetPowerSupplyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetPowerSupplyType.setStatus("current")


class _DellNetPowerSupplyPiecePartID_Type(DisplayString):
    """Custom type dellNetPowerSupplyPiecePartID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_DellNetPowerSupplyPiecePartID_Type.__name__ = "DisplayString"
_DellNetPowerSupplyPiecePartID_Object = MibTableColumn
dellNetPowerSupplyPiecePartID = _DellNetPowerSupplyPiecePartID_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 6, 1, 6),
    _DellNetPowerSupplyPiecePartID_Type()
)
dellNetPowerSupplyPiecePartID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetPowerSupplyPiecePartID.setStatus("current")


class _DellNetPowerSupplyPPIDRevision_Type(DisplayString):
    """Custom type dellNetPowerSupplyPPIDRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_DellNetPowerSupplyPPIDRevision_Type.__name__ = "DisplayString"
_DellNetPowerSupplyPPIDRevision_Object = MibTableColumn
dellNetPowerSupplyPPIDRevision = _DellNetPowerSupplyPPIDRevision_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 6, 1, 7),
    _DellNetPowerSupplyPPIDRevision_Type()
)
dellNetPowerSupplyPPIDRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetPowerSupplyPPIDRevision.setStatus("current")


class _DellNetPowerSupplyServiceTag_Type(DisplayString):
    """Custom type dellNetPowerSupplyServiceTag based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_DellNetPowerSupplyServiceTag_Type.__name__ = "DisplayString"
_DellNetPowerSupplyServiceTag_Object = MibTableColumn
dellNetPowerSupplyServiceTag = _DellNetPowerSupplyServiceTag_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 6, 1, 8),
    _DellNetPowerSupplyServiceTag_Type()
)
dellNetPowerSupplyServiceTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetPowerSupplyServiceTag.setStatus("current")


class _DellNetPowerSupplyExpressServiceCode_Type(DisplayString):
    """Custom type dellNetPowerSupplyExpressServiceCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_DellNetPowerSupplyExpressServiceCode_Type.__name__ = "DisplayString"
_DellNetPowerSupplyExpressServiceCode_Object = MibTableColumn
dellNetPowerSupplyExpressServiceCode = _DellNetPowerSupplyExpressServiceCode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 6, 1, 9),
    _DellNetPowerSupplyExpressServiceCode_Type()
)
dellNetPowerSupplyExpressServiceCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetPowerSupplyExpressServiceCode.setStatus("current")
_DellNetPowerSupplyUsage_Type = Integer32
_DellNetPowerSupplyUsage_Object = MibTableColumn
dellNetPowerSupplyUsage = _DellNetPowerSupplyUsage_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 6, 1, 10),
    _DellNetPowerSupplyUsage_Type()
)
dellNetPowerSupplyUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetPowerSupplyUsage.setStatus("current")
_DellNetFanTrayTable_Object = MibTable
dellNetFanTrayTable = _DellNetFanTrayTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 7)
)
if mibBuilder.loadTexts:
    dellNetFanTrayTable.setStatus("current")
_DellNetFanTrayEntry_Object = MibTableRow
dellNetFanTrayEntry = _DellNetFanTrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 7, 1)
)
dellNetFanTrayEntry.setIndexNames(
    (0, "DELL-NETWORKING-CHASSIS-MIB", "dellNetFanDeviceType"),
    (0, "DELL-NETWORKING-CHASSIS-MIB", "dellNetFanDeviceIndex"),
    (0, "DELL-NETWORKING-CHASSIS-MIB", "dellNetFanTrayIndex"),
)
if mibBuilder.loadTexts:
    dellNetFanTrayEntry.setStatus("current")
_DellNetFanDeviceType_Type = DellNetDeviceType
_DellNetFanDeviceType_Object = MibTableColumn
dellNetFanDeviceType = _DellNetFanDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 7, 1, 1),
    _DellNetFanDeviceType_Type()
)
dellNetFanDeviceType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dellNetFanDeviceType.setStatus("current")
_DellNetFanDeviceIndex_Type = Integer32
_DellNetFanDeviceIndex_Object = MibTableColumn
dellNetFanDeviceIndex = _DellNetFanDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 7, 1, 2),
    _DellNetFanDeviceIndex_Type()
)
dellNetFanDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dellNetFanDeviceIndex.setStatus("current")
_DellNetFanTrayIndex_Type = Integer32
_DellNetFanTrayIndex_Object = MibTableColumn
dellNetFanTrayIndex = _DellNetFanTrayIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 7, 1, 3),
    _DellNetFanTrayIndex_Type()
)
dellNetFanTrayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetFanTrayIndex.setStatus("current")


class _DellNetFanTrayOperStatus_Type(Integer32):
    """Custom type dellNetFanTrayOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("absent", 3),
          ("down", 2),
          ("up", 1))
    )


_DellNetFanTrayOperStatus_Type.__name__ = "Integer32"
_DellNetFanTrayOperStatus_Object = MibTableColumn
dellNetFanTrayOperStatus = _DellNetFanTrayOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 7, 1, 4),
    _DellNetFanTrayOperStatus_Type()
)
dellNetFanTrayOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetFanTrayOperStatus.setStatus("current")


class _DellNetFanTrayPiecePartID_Type(DisplayString):
    """Custom type dellNetFanTrayPiecePartID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_DellNetFanTrayPiecePartID_Type.__name__ = "DisplayString"
_DellNetFanTrayPiecePartID_Object = MibTableColumn
dellNetFanTrayPiecePartID = _DellNetFanTrayPiecePartID_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 7, 1, 5),
    _DellNetFanTrayPiecePartID_Type()
)
dellNetFanTrayPiecePartID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetFanTrayPiecePartID.setStatus("current")


class _DellNetFanTrayPPIDRevision_Type(DisplayString):
    """Custom type dellNetFanTrayPPIDRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_DellNetFanTrayPPIDRevision_Type.__name__ = "DisplayString"
_DellNetFanTrayPPIDRevision_Object = MibTableColumn
dellNetFanTrayPPIDRevision = _DellNetFanTrayPPIDRevision_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 7, 1, 6),
    _DellNetFanTrayPPIDRevision_Type()
)
dellNetFanTrayPPIDRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetFanTrayPPIDRevision.setStatus("current")


class _DellNetFanTrayServiceTag_Type(DisplayString):
    """Custom type dellNetFanTrayServiceTag based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_DellNetFanTrayServiceTag_Type.__name__ = "DisplayString"
_DellNetFanTrayServiceTag_Object = MibTableColumn
dellNetFanTrayServiceTag = _DellNetFanTrayServiceTag_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 7, 1, 7),
    _DellNetFanTrayServiceTag_Type()
)
dellNetFanTrayServiceTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetFanTrayServiceTag.setStatus("current")


class _DellNetFanTrayExpressServiceCode_Type(DisplayString):
    """Custom type dellNetFanTrayExpressServiceCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_DellNetFanTrayExpressServiceCode_Type.__name__ = "DisplayString"
_DellNetFanTrayExpressServiceCode_Object = MibTableColumn
dellNetFanTrayExpressServiceCode = _DellNetFanTrayExpressServiceCode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 7, 1, 8),
    _DellNetFanTrayExpressServiceCode_Type()
)
dellNetFanTrayExpressServiceCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetFanTrayExpressServiceCode.setStatus("current")
_DellNetSysSwCoresTable_Object = MibTable
dellNetSysSwCoresTable = _DellNetSysSwCoresTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 9)
)
if mibBuilder.loadTexts:
    dellNetSysSwCoresTable.setStatus("current")
_DellNetSysCoresEntry_Object = MibTableRow
dellNetSysCoresEntry = _DellNetSysCoresEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 9, 1)
)
dellNetSysCoresEntry.setIndexNames(
    (0, "DELL-NETWORKING-CHASSIS-MIB", "dellNetStackUnitNumber"),
    (0, "DELL-NETWORKING-CHASSIS-MIB", "dellNetSysCoresInstance"),
)
if mibBuilder.loadTexts:
    dellNetSysCoresEntry.setStatus("current")
_DellNetSysCoresInstance_Type = Integer32
_DellNetSysCoresInstance_Object = MibTableColumn
dellNetSysCoresInstance = _DellNetSysCoresInstance_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 9, 1, 1),
    _DellNetSysCoresInstance_Type()
)
dellNetSysCoresInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetSysCoresInstance.setStatus("current")
_DellNetSysCoresFileName_Type = DisplayString
_DellNetSysCoresFileName_Object = MibTableColumn
dellNetSysCoresFileName = _DellNetSysCoresFileName_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 9, 1, 2),
    _DellNetSysCoresFileName_Type()
)
dellNetSysCoresFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetSysCoresFileName.setStatus("current")
_DellNetSysCoresTimeCreated_Type = DellNetSwDate
_DellNetSysCoresTimeCreated_Object = MibTableColumn
dellNetSysCoresTimeCreated = _DellNetSysCoresTimeCreated_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 9, 1, 3),
    _DellNetSysCoresTimeCreated_Type()
)
dellNetSysCoresTimeCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetSysCoresTimeCreated.setStatus("current")


class _DellNetSysCoresStackUnitNumber_Type(Integer32):
    """Custom type dellNetSysCoresStackUnitNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_DellNetSysCoresStackUnitNumber_Type.__name__ = "Integer32"
_DellNetSysCoresStackUnitNumber_Object = MibTableColumn
dellNetSysCoresStackUnitNumber = _DellNetSysCoresStackUnitNumber_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 9, 1, 4),
    _DellNetSysCoresStackUnitNumber_Type()
)
dellNetSysCoresStackUnitNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetSysCoresStackUnitNumber.setStatus("current")
_DellNetSysCoresProcess_Type = DisplayString
_DellNetSysCoresProcess_Object = MibTableColumn
dellNetSysCoresProcess = _DellNetSysCoresProcess_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 9, 1, 5),
    _DellNetSysCoresProcess_Type()
)
dellNetSysCoresProcess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetSysCoresProcess.setStatus("current")
_DellNetSysIfTable_Object = MibTable
dellNetSysIfTable = _DellNetSysIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 10)
)
if mibBuilder.loadTexts:
    dellNetSysIfTable.setStatus("current")
_DellNetSysIfEntry_Object = MibTableRow
dellNetSysIfEntry = _DellNetSysIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 10, 1)
)
dellNetSysIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dellNetSysIfEntry.setStatus("current")
_DellNetSysIfType_Type = DellNetIfType
_DellNetSysIfType_Object = MibTableColumn
dellNetSysIfType = _DellNetSysIfType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 10, 1, 1),
    _DellNetSysIfType_Type()
)
dellNetSysIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetSysIfType.setStatus("current")
_DellNetSysIfName_Type = DisplayString
_DellNetSysIfName_Object = MibTableColumn
dellNetSysIfName = _DellNetSysIfName_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 10, 1, 2),
    _DellNetSysIfName_Type()
)
dellNetSysIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetSysIfName.setStatus("current")


class _DellNetSysIfAdminStatus_Type(Integer32):
    """Custom type dellNetSysIfAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_DellNetSysIfAdminStatus_Type.__name__ = "Integer32"
_DellNetSysIfAdminStatus_Object = MibTableColumn
dellNetSysIfAdminStatus = _DellNetSysIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 10, 1, 3),
    _DellNetSysIfAdminStatus_Type()
)
dellNetSysIfAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetSysIfAdminStatus.setStatus("current")


class _DellNetSysIfOperStatus_Type(Integer32):
    """Custom type dellNetSysIfOperStatus based on Integer32"""
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
        *(("cardDown", 5),
          ("cardProblem", 4),
          ("notPresent", 6),
          ("portDown", 2),
          ("portProblem", 3),
          ("ready", 1))
    )


_DellNetSysIfOperStatus_Type.__name__ = "Integer32"
_DellNetSysIfOperStatus_Object = MibTableColumn
dellNetSysIfOperStatus = _DellNetSysIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 10, 1, 4),
    _DellNetSysIfOperStatus_Type()
)
dellNetSysIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetSysIfOperStatus.setStatus("current")
_DellNetSysIfXfpRecvPower_Type = DellNetHundredthdB
_DellNetSysIfXfpRecvPower_Object = MibTableColumn
dellNetSysIfXfpRecvPower = _DellNetSysIfXfpRecvPower_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 10, 1, 5),
    _DellNetSysIfXfpRecvPower_Type()
)
dellNetSysIfXfpRecvPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetSysIfXfpRecvPower.setStatus("current")
if mibBuilder.loadTexts:
    dellNetSysIfXfpRecvPower.setUnits("dB")
_DellNetSysIfXfpRecvTemp_Type = Integer32
_DellNetSysIfXfpRecvTemp_Object = MibTableColumn
dellNetSysIfXfpRecvTemp = _DellNetSysIfXfpRecvTemp_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 10, 1, 6),
    _DellNetSysIfXfpRecvTemp_Type()
)
dellNetSysIfXfpRecvTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetSysIfXfpRecvTemp.setStatus("current")
_DellNetSysIfXfpTxPower_Type = DellNetHundredthdB
_DellNetSysIfXfpTxPower_Object = MibTableColumn
dellNetSysIfXfpTxPower = _DellNetSysIfXfpTxPower_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 4, 10, 1, 7),
    _DellNetSysIfXfpTxPower_Type()
)
dellNetSysIfXfpTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dellNetSysIfXfpTxPower.setStatus("current")
if mibBuilder.loadTexts:
    dellNetSysIfXfpTxPower.setUnits("dB")
_DellNetSysAlarmObjects_ObjectIdentity = ObjectIdentity
dellNetSysAlarmObjects = _DellNetSysAlarmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 5)
)
_DellNetSysAlarmMibNotifications_ObjectIdentity = ObjectIdentity
dellNetSysAlarmMibNotifications = _DellNetSysAlarmMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 5, 1)
)
_DellNetSysAlarmVariable_ObjectIdentity = ObjectIdentity
dellNetSysAlarmVariable = _DellNetSysAlarmVariable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 5, 2)
)
_DellNetSysAlarmVarInteger_Type = Integer32
_DellNetSysAlarmVarInteger_Object = MibScalar
dellNetSysAlarmVarInteger = _DellNetSysAlarmVarInteger_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 5, 2, 1),
    _DellNetSysAlarmVarInteger_Type()
)
dellNetSysAlarmVarInteger.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dellNetSysAlarmVarInteger.setStatus("current")
_DellNetSysAlarmVarString_Type = OctetString
_DellNetSysAlarmVarString_Object = MibScalar
dellNetSysAlarmVarString = _DellNetSysAlarmVarString_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 5, 2, 2),
    _DellNetSysAlarmVarString_Type()
)
dellNetSysAlarmVarString.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dellNetSysAlarmVarString.setStatus("current")
_DellNetSysAlarmVarSlot_Type = Integer32
_DellNetSysAlarmVarSlot_Object = MibScalar
dellNetSysAlarmVarSlot = _DellNetSysAlarmVarSlot_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 5, 2, 3),
    _DellNetSysAlarmVarSlot_Type()
)
dellNetSysAlarmVarSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dellNetSysAlarmVarSlot.setStatus("current")
_DellNetSysAlarmVarPort_Type = Integer32
_DellNetSysAlarmVarPort_Object = MibScalar
dellNetSysAlarmVarPort = _DellNetSysAlarmVarPort_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 5, 2, 4),
    _DellNetSysAlarmVarPort_Type()
)
dellNetSysAlarmVarPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dellNetSysAlarmVarPort.setStatus("current")
_DellNetSysAlarmVarChassisId_Type = Integer32
_DellNetSysAlarmVarChassisId_Object = MibScalar
dellNetSysAlarmVarChassisId = _DellNetSysAlarmVarChassisId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 5, 2, 5),
    _DellNetSysAlarmVarChassisId_Type()
)
dellNetSysAlarmVarChassisId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dellNetSysAlarmVarChassisId.setStatus("current")
_DellNetsysAlarmVarFanTrayId_Type = Integer32
_DellNetsysAlarmVarFanTrayId_Object = MibScalar
dellNetsysAlarmVarFanTrayId = _DellNetsysAlarmVarFanTrayId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 5, 2, 6),
    _DellNetsysAlarmVarFanTrayId_Type()
)
dellNetsysAlarmVarFanTrayId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dellNetsysAlarmVarFanTrayId.setStatus("current")
_DellNetsysAlarmVarPsuId_Type = Integer32
_DellNetsysAlarmVarPsuId_Object = MibScalar
dellNetsysAlarmVarPsuId = _DellNetsysAlarmVarPsuId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 5, 2, 7),
    _DellNetsysAlarmVarPsuId_Type()
)
dellNetsysAlarmVarPsuId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dellNetsysAlarmVarPsuId.setStatus("current")
_DellNetsysAlarmVarFanId_Type = Integer32
_DellNetsysAlarmVarFanId_Object = MibScalar
dellNetsysAlarmVarFanId = _DellNetsysAlarmVarFanId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 5, 2, 8),
    _DellNetsysAlarmVarFanId_Type()
)
dellNetsysAlarmVarFanId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dellNetsysAlarmVarFanId.setStatus("current")
_DellNetSysAlarmVarPeId_Type = Integer32
_DellNetSysAlarmVarPeId_Object = MibScalar
dellNetSysAlarmVarPeId = _DellNetSysAlarmVarPeId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 5, 2, 9),
    _DellNetSysAlarmVarPeId_Type()
)
dellNetSysAlarmVarPeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    dellNetSysAlarmVarPeId.setStatus("current")
_DellNetChassisMibConformance_ObjectIdentity = ObjectIdentity
dellNetChassisMibConformance = _DellNetChassisMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 2)
)
_DellNetChassisMibCompliances_ObjectIdentity = ObjectIdentity
dellNetChassisMibCompliances = _DellNetChassisMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 2, 1)
)
_DellNetChassisMibGroups_ObjectIdentity = ObjectIdentity
dellNetChassisMibGroups = _DellNetChassisMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 2, 2)
)

# Managed Objects groups

dellNetComponentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 2, 2, 1)
)
dellNetComponentGroup.setObjects(
    ("DELL-NETWORKING-CHASSIS-MIB", "dellNetDeviceType")
)
if mibBuilder.loadTexts:
    dellNetComponentGroup.setStatus("current")

dellNetSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 2, 2, 2)
)
dellNetSystemGroup.setObjects(
      *(("DELL-NETWORKING-CHASSIS-MIB", "dellNetProcessorModule"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetProcessorUpTime"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetProcessorMemSize"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetCpuUtil5Sec"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetCpuUtil1Min"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetCpuUtil5Min"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetCpuUtilMemUsage"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSwModuleRuntimeImgVersion"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSwModuleRuntimeImgDate"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSwModuleBootFlashImgVersion"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSwModuleBootSelectorImgVersion"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSwModuleNextRebootImage"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSwModuleCurrentBootImage"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSwModuleInPartitionAImgVers"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSwModuleInPartitionBImgVers"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetPowerSupplyOperStatus"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetPowerSupplyType"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetPowerSupplyPiecePartID"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetPowerSupplyPPIDRevision"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetPowerSupplyServiceTag"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetPowerSupplyExpressServiceCode"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetPowerSupplyUsage"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetFanTrayOperStatus"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetFanTrayPiecePartID"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetFanTrayPPIDRevision"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetFanTrayServiceTag"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetFanTrayExpressServiceCode"))
)
if mibBuilder.loadTexts:
    dellNetSystemGroup.setStatus("current")


# Notification objects

dellNetSysAlarmCardDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 5, 1, 1)
)
dellNetSysAlarmCardDown.setObjects(
      *(("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarInteger"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarString"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarChassisId"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarSlot"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarPort"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarPeId"))
)
if mibBuilder.loadTexts:
    dellNetSysAlarmCardDown.setStatus(
        "current"
    )

dellNetSysAlarmCardUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 5, 1, 2)
)
dellNetSysAlarmCardUp.setObjects(
      *(("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarInteger"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarString"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarChassisId"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarSlot"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarPort"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarPeId"))
)
if mibBuilder.loadTexts:
    dellNetSysAlarmCardUp.setStatus(
        "current"
    )

dellNetSysAlarmCardOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 5, 1, 3)
)
dellNetSysAlarmCardOffline.setObjects(
      *(("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarInteger"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarString"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarChassisId"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarSlot"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarPort"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarPeId"))
)
if mibBuilder.loadTexts:
    dellNetSysAlarmCardOffline.setStatus(
        "current"
    )

dellNetSysAlarmCardMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 5, 1, 4)
)
dellNetSysAlarmCardMismatch.setObjects(
      *(("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarInteger"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarString"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarChassisId"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarSlot"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarPort"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarPeId"))
)
if mibBuilder.loadTexts:
    dellNetSysAlarmCardMismatch.setStatus(
        "current"
    )

dellNetSysAlarmRpmUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 5, 1, 5)
)
dellNetSysAlarmRpmUp.setObjects(
      *(("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarInteger"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarString"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarChassisId"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarSlot"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarPort"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarPeId"))
)
if mibBuilder.loadTexts:
    dellNetSysAlarmRpmUp.setStatus(
        "current"
    )

dellNetSysAlarmRpmDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 5, 1, 6)
)
dellNetSysAlarmRpmDown.setObjects(
      *(("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarInteger"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarString"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarChassisId"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarSlot"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarPort"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarPeId"))
)
if mibBuilder.loadTexts:
    dellNetSysAlarmRpmDown.setStatus(
        "current"
    )

dellNetSysAlarmPowersupplyDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 5, 1, 7)
)
dellNetSysAlarmPowersupplyDown.setObjects(
      *(("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarInteger"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarString"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarChassisId"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarSlot"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarPort"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarPeId"))
)
if mibBuilder.loadTexts:
    dellNetSysAlarmPowersupplyDown.setStatus(
        "current"
    )

dellNetSysAlarmMinorTemperatureHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 5, 1, 8)
)
dellNetSysAlarmMinorTemperatureHigh.setObjects(
      *(("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarInteger"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarString"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarChassisId"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarSlot"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarPort"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarPeId"))
)
if mibBuilder.loadTexts:
    dellNetSysAlarmMinorTemperatureHigh.setStatus(
        "current"
    )

dellNetSysAlarmMajorTemperatureHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 5, 1, 9)
)
dellNetSysAlarmMajorTemperatureHigh.setObjects(
      *(("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarInteger"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarString"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarChassisId"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarSlot"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarPort"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarPeId"))
)
if mibBuilder.loadTexts:
    dellNetSysAlarmMajorTemperatureHigh.setStatus(
        "current"
    )

dellNetSysAlarmFanTrayDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 5, 1, 10)
)
dellNetSysAlarmFanTrayDown.setObjects(
      *(("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarInteger"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarString"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarChassisId"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarSlot"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetsysAlarmVarFanTrayId"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarPeId"))
)
if mibBuilder.loadTexts:
    dellNetSysAlarmFanTrayDown.setStatus(
        "current"
    )

dellNetSysAlarmPowersupplyClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 5, 1, 11)
)
dellNetSysAlarmPowersupplyClear.setObjects(
      *(("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarInteger"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarString"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarChassisId"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarSlot"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetsysAlarmVarPsuId"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarPeId"))
)
if mibBuilder.loadTexts:
    dellNetSysAlarmPowersupplyClear.setStatus(
        "current"
    )

dellNetSysAlarmMinorTemperatureClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 5, 1, 12)
)
dellNetSysAlarmMinorTemperatureClear.setObjects(
      *(("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarInteger"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarString"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarChassisId"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarSlot"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarPort"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarPeId"))
)
if mibBuilder.loadTexts:
    dellNetSysAlarmMinorTemperatureClear.setStatus(
        "current"
    )

dellNetSysAlarmMajorTemperatureClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 5, 1, 13)
)
dellNetSysAlarmMajorTemperatureClear.setObjects(
      *(("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarInteger"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarString"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarChassisId"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarSlot"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarPort"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarPeId"))
)
if mibBuilder.loadTexts:
    dellNetSysAlarmMajorTemperatureClear.setStatus(
        "current"
    )

dellNetSysAlarmFanTrayClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 5, 1, 14)
)
dellNetSysAlarmFanTrayClear.setObjects(
      *(("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarInteger"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarString"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarChassisId"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarSlot"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetsysAlarmVarFanTrayId"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarPeId"))
)
if mibBuilder.loadTexts:
    dellNetSysAlarmFanTrayClear.setStatus(
        "current"
    )

dellNetSysAlarmMinorFanBadClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 5, 1, 15)
)
dellNetSysAlarmMinorFanBadClear.setObjects(
      *(("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarInteger"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarString"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarChassisId"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarSlot"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetsysAlarmVarFanTrayId"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetsysAlarmVarFanId"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarPeId"))
)
if mibBuilder.loadTexts:
    dellNetSysAlarmMinorFanBadClear.setStatus(
        "current"
    )

dellNetSysAlarmMajorPS = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 5, 1, 16)
)
dellNetSysAlarmMajorPS.setObjects(
      *(("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarInteger"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarString"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarChassisId"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarSlot"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetsysAlarmVarPsuId"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarPeId"))
)
if mibBuilder.loadTexts:
    dellNetSysAlarmMajorPS.setStatus(
        "current"
    )

dellNetSysAlarmMajorPSClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 5, 1, 17)
)
dellNetSysAlarmMajorPSClr.setObjects(
      *(("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarInteger"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarString"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarChassisId"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarSlot"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetsysAlarmVarPsuId"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarPeId"))
)
if mibBuilder.loadTexts:
    dellNetSysAlarmMajorPSClr.setStatus(
        "current"
    )

dellNetSysAlarmMinorPS = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 5, 1, 18)
)
dellNetSysAlarmMinorPS.setObjects(
      *(("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarInteger"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarString"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarChassisId"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarSlot"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetsysAlarmVarPsuId"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarPeId"))
)
if mibBuilder.loadTexts:
    dellNetSysAlarmMinorPS.setStatus(
        "current"
    )

dellNetSysAlarmMinorPSClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 5, 1, 19)
)
dellNetSysAlarmMinorPSClr.setObjects(
      *(("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarInteger"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarString"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarChassisId"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarSlot"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetsysAlarmVarPsuId"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarPeId"))
)
if mibBuilder.loadTexts:
    dellNetSysAlarmMinorPSClr.setStatus(
        "current"
    )

dellNetSysAlarmMinorFanBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 5, 1, 20)
)
dellNetSysAlarmMinorFanBad.setObjects(
      *(("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarInteger"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarString"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarChassisId"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarSlot"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetsysAlarmVarFanTrayId"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetsysAlarmVarFanId"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarPeId"))
)
if mibBuilder.loadTexts:
    dellNetSysAlarmMinorFanBad.setStatus(
        "current"
    )

dellNetSysAlarmRpmPrimary = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 5, 1, 21)
)
dellNetSysAlarmRpmPrimary.setObjects(
      *(("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarInteger"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarString"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarChassisId"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarSlot"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarPort"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarPeId"))
)
if mibBuilder.loadTexts:
    dellNetSysAlarmRpmPrimary.setStatus(
        "current"
    )

dellNetSysSnmpIpAclDeny = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 5, 1, 22)
)
dellNetSysSnmpIpAclDeny.setObjects(
      *(("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarInteger"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarString"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarChassisId"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarSlot"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarPort"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarPeId"))
)
if mibBuilder.loadTexts:
    dellNetSysSnmpIpAclDeny.setStatus(
        "current"
    )

dellNetSysAlarmCardVersionMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 5, 1, 23)
)
dellNetSysAlarmCardVersionMismatch.setObjects(
      *(("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarInteger"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarString"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarChassisId"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarSlot"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarPort"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarPeId"))
)
if mibBuilder.loadTexts:
    dellNetSysAlarmCardVersionMismatch.setStatus(
        "current"
    )

dellNetSysAlarmUnsupportedOptic = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 5, 1, 24)
)
dellNetSysAlarmUnsupportedOptic.setObjects(
      *(("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarInteger"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarString"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarChassisId"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarSlot"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarPort"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarPeId"))
)
if mibBuilder.loadTexts:
    dellNetSysAlarmUnsupportedOptic.setStatus(
        "current"
    )

dellNetSysAlarmFanTrayOrPsuDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 5, 1, 25)
)
dellNetSysAlarmFanTrayOrPsuDown.setObjects(
      *(("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarInteger"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarString"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarChassisId"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarSlot"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetsysAlarmVarFanTrayId"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetsysAlarmVarPsuId"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarPeId"))
)
if mibBuilder.loadTexts:
    dellNetSysAlarmFanTrayOrPsuDown.setStatus(
        "current"
    )

dellNetSysAlarmFanTrayOrPsuClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 5, 1, 26)
)
dellNetSysAlarmFanTrayOrPsuClear.setObjects(
      *(("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarInteger"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarString"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarChassisId"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarSlot"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetsysAlarmVarFanTrayId"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetsysAlarmVarPsuId"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarPeId"))
)
if mibBuilder.loadTexts:
    dellNetSysAlarmFanTrayOrPsuClear.setStatus(
        "current"
    )

dellNetSysAlarmPEUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 5, 1, 27)
)
dellNetSysAlarmPEUp.setObjects(
      *(("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarInteger"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarString"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarChassisId"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarSlot"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarPort"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarPeId"))
)
if mibBuilder.loadTexts:
    dellNetSysAlarmPEUp.setStatus(
        "current"
    )

dellNetSysAlarmPEDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 5, 1, 28)
)
dellNetSysAlarmPEDown.setObjects(
      *(("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarInteger"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarString"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarChassisId"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarSlot"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarPort"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarPeId"))
)
if mibBuilder.loadTexts:
    dellNetSysAlarmPEDown.setStatus(
        "current"
    )

dellNetSysAlarmPEUnitUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 5, 1, 29)
)
dellNetSysAlarmPEUnitUp.setObjects(
      *(("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarInteger"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarString"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarChassisId"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarSlot"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarPort"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarPeId"))
)
if mibBuilder.loadTexts:
    dellNetSysAlarmPEUnitUp.setStatus(
        "current"
    )

dellNetSysAlarmPEUnitDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 5, 1, 30)
)
dellNetSysAlarmPEUnitDown.setObjects(
      *(("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarInteger"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarString"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarChassisId"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarSlot"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarPort"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarPeId"))
)
if mibBuilder.loadTexts:
    dellNetSysAlarmPEUnitDown.setStatus(
        "current"
    )

dellNetSysAlarmExdCpuThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 5, 1, 31)
)
dellNetSysAlarmExdCpuThreshold.setObjects(
      *(("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarInteger"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarString"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarChassisId"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarSlot"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarPort"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarPeId"))
)
if mibBuilder.loadTexts:
    dellNetSysAlarmExdCpuThreshold.setStatus(
        "current"
    )

dellNetSysAlarmClrCpuThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 5, 1, 32)
)
dellNetSysAlarmClrCpuThreshold.setObjects(
      *(("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarInteger"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarString"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarChassisId"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarSlot"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarPort"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarPeId"))
)
if mibBuilder.loadTexts:
    dellNetSysAlarmClrCpuThreshold.setStatus(
        "current"
    )

dellNetSysAlarmExdMemThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 5, 1, 33)
)
dellNetSysAlarmExdMemThreshold.setObjects(
      *(("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarInteger"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarString"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarChassisId"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarSlot"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarPort"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarPeId"))
)
if mibBuilder.loadTexts:
    dellNetSysAlarmExdMemThreshold.setStatus(
        "current"
    )

dellNetSysAlarmClrMemThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 5, 1, 34)
)
dellNetSysAlarmClrMemThreshold.setObjects(
      *(("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarInteger"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarString"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarChassisId"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarSlot"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarPort"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarPeId"))
)
if mibBuilder.loadTexts:
    dellNetSysAlarmClrMemThreshold.setStatus(
        "current"
    )

dellNetSysAlarmTaskSuspend = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 5, 1, 35)
)
dellNetSysAlarmTaskSuspend.setObjects(
      *(("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarInteger"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarString"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarChassisId"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarSlot"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarPort"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarPeId"))
)
if mibBuilder.loadTexts:
    dellNetSysAlarmTaskSuspend.setStatus(
        "current"
    )

dellNetSysAlarmTaskTerm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 5, 1, 36)
)
dellNetSysAlarmTaskTerm.setObjects(
      *(("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarInteger"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarString"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarChassisId"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarSlot"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarPort"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarPeId"))
)
if mibBuilder.loadTexts:
    dellNetSysAlarmTaskTerm.setStatus(
        "current"
    )

dellNetSysAlarmMacStationMove = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 5, 1, 37)
)
dellNetSysAlarmMacStationMove.setObjects(
      *(("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarInteger"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarString"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarChassisId"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarSlot"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarPort"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarPeId"))
)
if mibBuilder.loadTexts:
    dellNetSysAlarmMacStationMove.setStatus(
        "current"
    )

dellNetSysAlarmCardReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 5, 1, 38)
)
dellNetSysAlarmCardReset.setObjects(
      *(("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarInteger"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarString"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarChassisId"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarSlot"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarPort"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarPeId"))
)
if mibBuilder.loadTexts:
    dellNetSysAlarmCardReset.setStatus(
        "deprecated"
    )

dellNetSysAlarmCardRemove = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 5, 1, 39)
)
dellNetSysAlarmCardRemove.setObjects(
      *(("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarInteger"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarString"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarChassisId"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarSlot"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarPort"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarPeId"))
)
if mibBuilder.loadTexts:
    dellNetSysAlarmCardRemove.setStatus(
        "deprecated"
    )

dellNetSysAlarmCardProblem = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 5, 1, 40)
)
dellNetSysAlarmCardProblem.setObjects(
      *(("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarInteger"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarString"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarChassisId"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarSlot"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarPort"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarPeId"))
)
if mibBuilder.loadTexts:
    dellNetSysAlarmCardProblem.setStatus(
        "deprecated"
    )

dellNetSysAlarmCutoff = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 5, 1, 41)
)
dellNetSysAlarmCutoff.setObjects(
      *(("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarInteger"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarString"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarChassisId"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarSlot"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarPort"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarPeId"))
)
if mibBuilder.loadTexts:
    dellNetSysAlarmCutoff.setStatus(
        "deprecated"
    )

dellNetSysAlarmSRAMParityErrorDetect = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 5, 1, 42)
)
dellNetSysAlarmSRAMParityErrorDetect.setObjects(
      *(("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarInteger"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarString"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarChassisId"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarSlot"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarPort"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarPeId"))
)
if mibBuilder.loadTexts:
    dellNetSysAlarmSRAMParityErrorDetect.setStatus(
        "deprecated"
    )

dellNetSysAlarmAcDcMixedPowerSupplyDetect = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 5, 1, 43)
)
dellNetSysAlarmAcDcMixedPowerSupplyDetect.setObjects(
      *(("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarInteger"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarString"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarChassisId"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarSlot"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarPort"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarPeId"))
)
if mibBuilder.loadTexts:
    dellNetSysAlarmAcDcMixedPowerSupplyDetect.setStatus(
        "deprecated"
    )

dellNetSysAlarmVrrpGoMaster = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 5, 1, 44)
)
dellNetSysAlarmVrrpGoMaster.setObjects(
      *(("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarInteger"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarString"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarChassisId"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarSlot"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarPort"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarPeId"))
)
if mibBuilder.loadTexts:
    dellNetSysAlarmVrrpGoMaster.setStatus(
        "deprecated"
    )

dellNetSysAlarmVrrpGiveupMaster = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 1, 5, 1, 45)
)
dellNetSysAlarmVrrpGiveupMaster.setObjects(
      *(("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarInteger"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarString"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarChassisId"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarSlot"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarPort"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVarPeId"))
)
if mibBuilder.loadTexts:
    dellNetSysAlarmVrrpGiveupMaster.setStatus(
        "deprecated"
    )


# Notifications groups

dellNetChassisNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 2, 2, 3)
)
dellNetChassisNotificationGroup.setObjects(
      *(("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmCardDown"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmCardUp"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmCardOffline"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmCardMismatch"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmRpmUp"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmRpmDown"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmPowersupplyDown"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmMinorTemperatureHigh"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmMajorTemperatureHigh"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmFanTrayDown"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmPowersupplyClear"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmMinorTemperatureClear"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmMajorTemperatureClear"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmFanTrayClear"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmMinorFanBadClear"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmMajorPS"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmMajorPSClr"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmMinorPS"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmMinorPSClr"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmMinorFanBad"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmRpmPrimary"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysSnmpIpAclDeny"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmCardVersionMismatch"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmUnsupportedOptic"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmPEUnitUp"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmPEUnitDown"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmPEUp"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmPEDown"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmExdCpuThreshold"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmClrCpuThreshold"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmExdMemThreshold"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmClrMemThreshold"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmTaskSuspend"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmTaskTerm"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmMacStationMove"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmCardReset"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmCardRemove"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmCardProblem"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmCutoff"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmSRAMParityErrorDetect"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmAcDcMixedPowerSupplyDetect"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVrrpGoMaster"),
        ("DELL-NETWORKING-CHASSIS-MIB", "dellNetSysAlarmVrrpGiveupMaster"))
)
if mibBuilder.loadTexts:
    dellNetChassisNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

dellNetChassisMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6027, 3, 26, 2, 1, 1)
)
if mibBuilder.loadTexts:
    dellNetChassisMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DELL-NETWORKING-CHASSIS-MIB",
    **{"dellNetChassisMib": dellNetChassisMib,
       "dellNetSysObject": dellNetSysObject,
       "dellNetSysParameter": dellNetSysParameter,
       "dellNetDeviceType": dellNetDeviceType,
       "dellNetChassisObject": dellNetChassisObject,
       "dellNetNumChassis": dellNetNumChassis,
       "dellNetMaxNumChassis": dellNetMaxNumChassis,
       "dellNetChassisTable": dellNetChassisTable,
       "dellNetChassisEntry": dellNetChassisEntry,
       "dellNetChassisIndex": dellNetChassisIndex,
       "dellNetChassisType": dellNetChassisType,
       "dellNetChassisMacAddr": dellNetChassisMacAddr,
       "dellNetChassisSerialNumber": dellNetChassisSerialNumber,
       "dellNetChassisPartNum": dellNetChassisPartNum,
       "dellNetChassisProductRev": dellNetChassisProductRev,
       "dellNetChassisVendorId": dellNetChassisVendorId,
       "dellNetChassisMfgDate": dellNetChassisMfgDate,
       "dellNetChassisCountryCode": dellNetChassisCountryCode,
       "dellNetChassisPPIDRev": dellNetChassisPPIDRev,
       "dellNetChassisServiceTag": dellNetChassisServiceTag,
       "dellNetChassisExpServiceCode": dellNetChassisExpServiceCode,
       "dellNetChassisNumSlots": dellNetChassisNumSlots,
       "dellNetChassisNumLineCardSlots": dellNetChassisNumLineCardSlots,
       "dellNetChassisNumFanTrays": dellNetChassisNumFanTrays,
       "dellNetChassisNumPowerSupplies": dellNetChassisNumPowerSupplies,
       "dellNetCardTable": dellNetCardTable,
       "dellNetCardEntry": dellNetCardEntry,
       "dellNetCardIndex": dellNetCardIndex,
       "dellNetCardType": dellNetCardType,
       "dellNetCardDescription": dellNetCardDescription,
       "dellNetCardChassisIndex": dellNetCardChassisIndex,
       "dellNetCardStatus": dellNetCardStatus,
       "dellNetCardTemp": dellNetCardTemp,
       "dellNetCardVendorId": dellNetCardVendorId,
       "dellNetCardMfgDate": dellNetCardMfgDate,
       "dellNetCardPartNum": dellNetCardPartNum,
       "dellNetCardProductRev": dellNetCardProductRev,
       "dellNetCardProductOrder": dellNetCardProductOrder,
       "dellNetCardCountryCode": dellNetCardCountryCode,
       "dellNetCardPiecePartID": dellNetCardPiecePartID,
       "dellNetCardPPIDRevision": dellNetCardPPIDRevision,
       "dellNetCardServiceTag": dellNetCardServiceTag,
       "dellNetCardExpServiceCode": dellNetCardExpServiceCode,
       "dellNetCardNumOfPorts": dellNetCardNumOfPorts,
       "dellNetStackObject": dellNetStackObject,
       "dellNetNumStackUnits": dellNetNumStackUnits,
       "dellNetMaxStackableUnits": dellNetMaxStackableUnits,
       "dellNetStackUnitIndexNext": dellNetStackUnitIndexNext,
       "dellNetStackUnitTable": dellNetStackUnitTable,
       "dellNetStackUnitEntry": dellNetStackUnitEntry,
       "dellNetStackUnitIndex": dellNetStackUnitIndex,
       "dellNetStackUnitNumber": dellNetStackUnitNumber,
       "dellNetStackUnitMgmtStatus": dellNetStackUnitMgmtStatus,
       "dellNetStackUnitHwMgmtPreference": dellNetStackUnitHwMgmtPreference,
       "dellNetStackUnitAdmMgmtPreference": dellNetStackUnitAdmMgmtPreference,
       "dellNetStackUnitModelId": dellNetStackUnitModelId,
       "dellNetStackUnitStatus": dellNetStackUnitStatus,
       "dellNetStackUnitDescription": dellNetStackUnitDescription,
       "dellNetStackUnitCodeVersion": dellNetStackUnitCodeVersion,
       "dellNetStackUnitSerialNumber": dellNetStackUnitSerialNumber,
       "dellNetStackUnitUpTime": dellNetStackUnitUpTime,
       "dellNetStackUnitTemp": dellNetStackUnitTemp,
       "dellNetStackUnitVendorId": dellNetStackUnitVendorId,
       "dellNetStackUnitMfgDate": dellNetStackUnitMfgDate,
       "dellNetStackUnitMacAddress": dellNetStackUnitMacAddress,
       "dellNetStackUnitPartNum": dellNetStackUnitPartNum,
       "dellNetStackUnitProductRev": dellNetStackUnitProductRev,
       "dellNetStackUnitProductOrder": dellNetStackUnitProductOrder,
       "dellNetStackUnitCountryCode": dellNetStackUnitCountryCode,
       "dellNetStackUnitPiecePartID": dellNetStackUnitPiecePartID,
       "dellNetStackUnitPPIDRevision": dellNetStackUnitPPIDRevision,
       "dellNetStackUnitServiceTag": dellNetStackUnitServiceTag,
       "dellNetStackUnitExpServiceCode": dellNetStackUnitExpServiceCode,
       "dellNetStackUnitNumOfPorts": dellNetStackUnitNumOfPorts,
       "dellNetStackUnitNumFanTrays": dellNetStackUnitNumFanTrays,
       "dellNetStackUnitNumPowerSupplies": dellNetStackUnitNumPowerSupplies,
       "dellNetStackUnitNumPluggableModules": dellNetStackUnitNumPluggableModules,
       "dellNetStackPortTable": dellNetStackPortTable,
       "dellNetStackPortEntry": dellNetStackPortEntry,
       "dellNetStackPortIndex": dellNetStackPortIndex,
       "dellNetStackPortConfiguredMode": dellNetStackPortConfiguredMode,
       "dellNetStackPortRunningMode": dellNetStackPortRunningMode,
       "dellNetStackPortLinkStatus": dellNetStackPortLinkStatus,
       "dellNetStackPortLinkSpeed": dellNetStackPortLinkSpeed,
       "dellNetStackPortRxDataRate": dellNetStackPortRxDataRate,
       "dellNetStackPortRxErrorRate": dellNetStackPortRxErrorRate,
       "dellNetStackPortRxTotalErrors": dellNetStackPortRxTotalErrors,
       "dellNetStackPortTxDataRate": dellNetStackPortTxDataRate,
       "dellNetStackPortTxErrorRate": dellNetStackPortTxErrorRate,
       "dellNetStackPortTxTotalErrors": dellNetStackPortTxTotalErrors,
       "dellNetSystemComponent": dellNetSystemComponent,
       "dellNetPEBindingTable": dellNetPEBindingTable,
       "dellNetPEBindingEntry": dellNetPEBindingEntry,
       "dellNetPEBindCascadePortIfIndex": dellNetPEBindCascadePortIfIndex,
       "dellNetPEBindPEIndex": dellNetPEBindPEIndex,
       "dellNetPETable": dellNetPETable,
       "dellNetPEEntry": dellNetPEEntry,
       "dellNetPEIndex": dellNetPEIndex,
       "dellNetPEPEID": dellNetPEPEID,
       "dellNetPEUnitID": dellNetPEUnitID,
       "dellNetPEType": dellNetPEType,
       "dellNetPEDescription": dellNetPEDescription,
       "dellNetPEStatus": dellNetPEStatus,
       "dellNetPETemp": dellNetPETemp,
       "dellNetPEVendorId": dellNetPEVendorId,
       "dellNetPEMfgDate": dellNetPEMfgDate,
       "dellNetPEPartNum": dellNetPEPartNum,
       "dellNetPEProductRev": dellNetPEProductRev,
       "dellNetPEProductOrder": dellNetPEProductOrder,
       "dellNetPECountryCode": dellNetPECountryCode,
       "dellNetPEPiecePartID": dellNetPEPiecePartID,
       "dellNetPEPPIDRevision": dellNetPEPPIDRevision,
       "dellNetPEServiceTag": dellNetPEServiceTag,
       "dellNetPEExpServiceCode": dellNetPEExpServiceCode,
       "dellNetPENumOfPorts": dellNetPENumOfPorts,
       "dellNetPENumFanTrays": dellNetPENumFanTrays,
       "dellNetPENumPowerSupplies": dellNetPENumPowerSupplies,
       "dellNetPENumPluggableModules": dellNetPENumPluggableModules,
       "dellNetProcessorTable": dellNetProcessorTable,
       "dellNetProcessorEntry": dellNetProcessorEntry,
       "dellNetProcessorDeviceType": dellNetProcessorDeviceType,
       "dellNetProcessorDeviceIndex": dellNetProcessorDeviceIndex,
       "dellNetProcessorIndex": dellNetProcessorIndex,
       "dellNetProcessorModule": dellNetProcessorModule,
       "dellNetProcessorUpTime": dellNetProcessorUpTime,
       "dellNetProcessorMemSize": dellNetProcessorMemSize,
       "dellNetCpuUtilTable": dellNetCpuUtilTable,
       "dellNetCpuUtilEntry": dellNetCpuUtilEntry,
       "dellNetCpuUtil5Sec": dellNetCpuUtil5Sec,
       "dellNetCpuUtil1Min": dellNetCpuUtil1Min,
       "dellNetCpuUtil5Min": dellNetCpuUtil5Min,
       "dellNetCpuUtilMemUsage": dellNetCpuUtilMemUsage,
       "dellNetCpuFlashUsageUtil": dellNetCpuFlashUsageUtil,
       "dellNetSwModuleTable": dellNetSwModuleTable,
       "dellNetSwModuleEntry": dellNetSwModuleEntry,
       "dellNetSwModuleRuntimeImgVersion": dellNetSwModuleRuntimeImgVersion,
       "dellNetSwModuleRuntimeImgDate": dellNetSwModuleRuntimeImgDate,
       "dellNetSwModuleBootFlashImgVersion": dellNetSwModuleBootFlashImgVersion,
       "dellNetSwModuleBootSelectorImgVersion": dellNetSwModuleBootSelectorImgVersion,
       "dellNetSwModuleNextRebootImage": dellNetSwModuleNextRebootImage,
       "dellNetSwModuleCurrentBootImage": dellNetSwModuleCurrentBootImage,
       "dellNetSwModuleInPartitionAImgVers": dellNetSwModuleInPartitionAImgVers,
       "dellNetSwModuleInPartitionBImgVers": dellNetSwModuleInPartitionBImgVers,
       "dellNetPowerSupplyTable": dellNetPowerSupplyTable,
       "dellNetPowerSupplyEntry": dellNetPowerSupplyEntry,
       "dellNetPowerDeviceType": dellNetPowerDeviceType,
       "dellNetPowerDeviceIndex": dellNetPowerDeviceIndex,
       "dellNetPowerSupplyIndex": dellNetPowerSupplyIndex,
       "dellNetPowerSupplyOperStatus": dellNetPowerSupplyOperStatus,
       "dellNetPowerSupplyType": dellNetPowerSupplyType,
       "dellNetPowerSupplyPiecePartID": dellNetPowerSupplyPiecePartID,
       "dellNetPowerSupplyPPIDRevision": dellNetPowerSupplyPPIDRevision,
       "dellNetPowerSupplyServiceTag": dellNetPowerSupplyServiceTag,
       "dellNetPowerSupplyExpressServiceCode": dellNetPowerSupplyExpressServiceCode,
       "dellNetPowerSupplyUsage": dellNetPowerSupplyUsage,
       "dellNetFanTrayTable": dellNetFanTrayTable,
       "dellNetFanTrayEntry": dellNetFanTrayEntry,
       "dellNetFanDeviceType": dellNetFanDeviceType,
       "dellNetFanDeviceIndex": dellNetFanDeviceIndex,
       "dellNetFanTrayIndex": dellNetFanTrayIndex,
       "dellNetFanTrayOperStatus": dellNetFanTrayOperStatus,
       "dellNetFanTrayPiecePartID": dellNetFanTrayPiecePartID,
       "dellNetFanTrayPPIDRevision": dellNetFanTrayPPIDRevision,
       "dellNetFanTrayServiceTag": dellNetFanTrayServiceTag,
       "dellNetFanTrayExpressServiceCode": dellNetFanTrayExpressServiceCode,
       "dellNetSysSwCoresTable": dellNetSysSwCoresTable,
       "dellNetSysCoresEntry": dellNetSysCoresEntry,
       "dellNetSysCoresInstance": dellNetSysCoresInstance,
       "dellNetSysCoresFileName": dellNetSysCoresFileName,
       "dellNetSysCoresTimeCreated": dellNetSysCoresTimeCreated,
       "dellNetSysCoresStackUnitNumber": dellNetSysCoresStackUnitNumber,
       "dellNetSysCoresProcess": dellNetSysCoresProcess,
       "dellNetSysIfTable": dellNetSysIfTable,
       "dellNetSysIfEntry": dellNetSysIfEntry,
       "dellNetSysIfType": dellNetSysIfType,
       "dellNetSysIfName": dellNetSysIfName,
       "dellNetSysIfAdminStatus": dellNetSysIfAdminStatus,
       "dellNetSysIfOperStatus": dellNetSysIfOperStatus,
       "dellNetSysIfXfpRecvPower": dellNetSysIfXfpRecvPower,
       "dellNetSysIfXfpRecvTemp": dellNetSysIfXfpRecvTemp,
       "dellNetSysIfXfpTxPower": dellNetSysIfXfpTxPower,
       "dellNetSysAlarmObjects": dellNetSysAlarmObjects,
       "dellNetSysAlarmMibNotifications": dellNetSysAlarmMibNotifications,
       "dellNetSysAlarmCardDown": dellNetSysAlarmCardDown,
       "dellNetSysAlarmCardUp": dellNetSysAlarmCardUp,
       "dellNetSysAlarmCardOffline": dellNetSysAlarmCardOffline,
       "dellNetSysAlarmCardMismatch": dellNetSysAlarmCardMismatch,
       "dellNetSysAlarmRpmUp": dellNetSysAlarmRpmUp,
       "dellNetSysAlarmRpmDown": dellNetSysAlarmRpmDown,
       "dellNetSysAlarmPowersupplyDown": dellNetSysAlarmPowersupplyDown,
       "dellNetSysAlarmMinorTemperatureHigh": dellNetSysAlarmMinorTemperatureHigh,
       "dellNetSysAlarmMajorTemperatureHigh": dellNetSysAlarmMajorTemperatureHigh,
       "dellNetSysAlarmFanTrayDown": dellNetSysAlarmFanTrayDown,
       "dellNetSysAlarmPowersupplyClear": dellNetSysAlarmPowersupplyClear,
       "dellNetSysAlarmMinorTemperatureClear": dellNetSysAlarmMinorTemperatureClear,
       "dellNetSysAlarmMajorTemperatureClear": dellNetSysAlarmMajorTemperatureClear,
       "dellNetSysAlarmFanTrayClear": dellNetSysAlarmFanTrayClear,
       "dellNetSysAlarmMinorFanBadClear": dellNetSysAlarmMinorFanBadClear,
       "dellNetSysAlarmMajorPS": dellNetSysAlarmMajorPS,
       "dellNetSysAlarmMajorPSClr": dellNetSysAlarmMajorPSClr,
       "dellNetSysAlarmMinorPS": dellNetSysAlarmMinorPS,
       "dellNetSysAlarmMinorPSClr": dellNetSysAlarmMinorPSClr,
       "dellNetSysAlarmMinorFanBad": dellNetSysAlarmMinorFanBad,
       "dellNetSysAlarmRpmPrimary": dellNetSysAlarmRpmPrimary,
       "dellNetSysSnmpIpAclDeny": dellNetSysSnmpIpAclDeny,
       "dellNetSysAlarmCardVersionMismatch": dellNetSysAlarmCardVersionMismatch,
       "dellNetSysAlarmUnsupportedOptic": dellNetSysAlarmUnsupportedOptic,
       "dellNetSysAlarmFanTrayOrPsuDown": dellNetSysAlarmFanTrayOrPsuDown,
       "dellNetSysAlarmFanTrayOrPsuClear": dellNetSysAlarmFanTrayOrPsuClear,
       "dellNetSysAlarmPEUp": dellNetSysAlarmPEUp,
       "dellNetSysAlarmPEDown": dellNetSysAlarmPEDown,
       "dellNetSysAlarmPEUnitUp": dellNetSysAlarmPEUnitUp,
       "dellNetSysAlarmPEUnitDown": dellNetSysAlarmPEUnitDown,
       "dellNetSysAlarmExdCpuThreshold": dellNetSysAlarmExdCpuThreshold,
       "dellNetSysAlarmClrCpuThreshold": dellNetSysAlarmClrCpuThreshold,
       "dellNetSysAlarmExdMemThreshold": dellNetSysAlarmExdMemThreshold,
       "dellNetSysAlarmClrMemThreshold": dellNetSysAlarmClrMemThreshold,
       "dellNetSysAlarmTaskSuspend": dellNetSysAlarmTaskSuspend,
       "dellNetSysAlarmTaskTerm": dellNetSysAlarmTaskTerm,
       "dellNetSysAlarmMacStationMove": dellNetSysAlarmMacStationMove,
       "dellNetSysAlarmCardReset": dellNetSysAlarmCardReset,
       "dellNetSysAlarmCardRemove": dellNetSysAlarmCardRemove,
       "dellNetSysAlarmCardProblem": dellNetSysAlarmCardProblem,
       "dellNetSysAlarmCutoff": dellNetSysAlarmCutoff,
       "dellNetSysAlarmSRAMParityErrorDetect": dellNetSysAlarmSRAMParityErrorDetect,
       "dellNetSysAlarmAcDcMixedPowerSupplyDetect": dellNetSysAlarmAcDcMixedPowerSupplyDetect,
       "dellNetSysAlarmVrrpGoMaster": dellNetSysAlarmVrrpGoMaster,
       "dellNetSysAlarmVrrpGiveupMaster": dellNetSysAlarmVrrpGiveupMaster,
       "dellNetSysAlarmVariable": dellNetSysAlarmVariable,
       "dellNetSysAlarmVarInteger": dellNetSysAlarmVarInteger,
       "dellNetSysAlarmVarString": dellNetSysAlarmVarString,
       "dellNetSysAlarmVarSlot": dellNetSysAlarmVarSlot,
       "dellNetSysAlarmVarPort": dellNetSysAlarmVarPort,
       "dellNetSysAlarmVarChassisId": dellNetSysAlarmVarChassisId,
       "dellNetsysAlarmVarFanTrayId": dellNetsysAlarmVarFanTrayId,
       "dellNetsysAlarmVarPsuId": dellNetsysAlarmVarPsuId,
       "dellNetsysAlarmVarFanId": dellNetsysAlarmVarFanId,
       "dellNetSysAlarmVarPeId": dellNetSysAlarmVarPeId,
       "dellNetChassisMibConformance": dellNetChassisMibConformance,
       "dellNetChassisMibCompliances": dellNetChassisMibCompliances,
       "dellNetChassisMibCompliance": dellNetChassisMibCompliance,
       "dellNetChassisMibGroups": dellNetChassisMibGroups,
       "dellNetComponentGroup": dellNetComponentGroup,
       "dellNetSystemGroup": dellNetSystemGroup,
       "dellNetChassisNotificationGroup": dellNetChassisNotificationGroup}
)
