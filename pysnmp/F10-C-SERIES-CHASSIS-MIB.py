# SNMP MIB module (F10-C-SERIES-CHASSIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/F10-C-SERIES-CHASSIS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:43:19 2024
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

(f10Mgmt,) = mibBuilder.importSymbols(
    "FORCE10-SMI",
    "f10Mgmt")

(F10CSeriesCardType,
 F10CSeriesPortType,
 F10CardOperStatus,
 F10ChassisMode,
 F10ChassisType,
 F10HundredthdB,
 F10MfgDate,
 F10ProcessorModuleType,
 F10SwDate) = mibBuilder.importSymbols(
    "FORCE10-TC",
    "F10CSeriesCardType",
    "F10CSeriesPortType",
    "F10CardOperStatus",
    "F10ChassisMode",
    "F10ChassisType",
    "F10HundredthdB",
    "F10MfgDate",
    "F10ProcessorModuleType",
    "F10SwDate")

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

f10CSerChassisMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8)
)
f10CSerChassisMib.setRevisions(
        ("2012-07-18 12:00",
         "2008-09-02 12:00",
         "2007-06-28 12:00",
         "2007-05-22 12:00",
         "2013-05-17 12:00",
         "1906-05-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_F10CSerChassisObject_ObjectIdentity = ObjectIdentity
f10CSerChassisObject = _F10CSerChassisObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1)
)
_ChObjects_ObjectIdentity = ObjectIdentity
chObjects = _ChObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 1)
)
_ChType_Type = F10ChassisType
_ChType_Object = MibScalar
chType = _ChType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 1, 1),
    _ChType_Type()
)
chType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chType.setStatus("current")
_ChChassisMode_Type = F10ChassisMode
_ChChassisMode_Object = MibScalar
chChassisMode = _ChChassisMode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 1, 2),
    _ChChassisMode_Type()
)
chChassisMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chChassisMode.setStatus("current")
_ChSwVersion_Type = DisplayString
_ChSwVersion_Object = MibScalar
chSwVersion = _ChSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 1, 3),
    _ChSwVersion_Type()
)
chSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSwVersion.setStatus("current")
_ChMacAddr_Type = MacAddress
_ChMacAddr_Object = MibScalar
chMacAddr = _ChMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 1, 4),
    _ChMacAddr_Type()
)
chMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chMacAddr.setStatus("current")
_ChSerialNumber_Type = DisplayString
_ChSerialNumber_Object = MibScalar
chSerialNumber = _ChSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 1, 5),
    _ChSerialNumber_Type()
)
chSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSerialNumber.setStatus("current")
_ChPartNum_Type = DisplayString
_ChPartNum_Object = MibScalar
chPartNum = _ChPartNum_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 1, 6),
    _ChPartNum_Type()
)
chPartNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chPartNum.setStatus("current")
_ChProductRev_Type = DisplayString
_ChProductRev_Object = MibScalar
chProductRev = _ChProductRev_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 1, 7),
    _ChProductRev_Type()
)
chProductRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chProductRev.setStatus("current")
_ChVendorId_Type = DisplayString
_ChVendorId_Object = MibScalar
chVendorId = _ChVendorId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 1, 8),
    _ChVendorId_Type()
)
chVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chVendorId.setStatus("current")
_ChDateCode_Type = F10MfgDate
_ChDateCode_Object = MibScalar
chDateCode = _ChDateCode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 1, 9),
    _ChDateCode_Type()
)
chDateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chDateCode.setStatus("current")


class _ChCountryCode_Type(OctetString):
    """Custom type chCountryCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_ChCountryCode_Type.__name__ = "OctetString"
_ChCountryCode_Object = MibScalar
chCountryCode = _ChCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 1, 10),
    _ChCountryCode_Type()
)
chCountryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chCountryCode.setStatus("current")
_ChNumSlots_Type = Integer32
_ChNumSlots_Object = MibScalar
chNumSlots = _ChNumSlots_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 1, 11),
    _ChNumSlots_Type()
)
chNumSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chNumSlots.setStatus("current")
_ChNumLinecards_Type = Integer32
_ChNumLinecards_Object = MibScalar
chNumLinecards = _ChNumLinecards_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 1, 12),
    _ChNumLinecards_Type()
)
chNumLinecards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chNumLinecards.setStatus("current")
_ChNumFanTrays_Type = Integer32
_ChNumFanTrays_Object = MibScalar
chNumFanTrays = _ChNumFanTrays_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 1, 13),
    _ChNumFanTrays_Type()
)
chNumFanTrays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chNumFanTrays.setStatus("current")
_ChNumPowerSupplies_Type = Integer32
_ChNumPowerSupplies_Object = MibScalar
chNumPowerSupplies = _ChNumPowerSupplies_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 1, 14),
    _ChNumPowerSupplies_Type()
)
chNumPowerSupplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chNumPowerSupplies.setStatus("current")
_ChNumSfmSlots_Type = Integer32
_ChNumSfmSlots_Object = MibScalar
chNumSfmSlots = _ChNumSfmSlots_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 1, 15),
    _ChNumSfmSlots_Type()
)
chNumSfmSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chNumSfmSlots.setStatus("current")


class _ChPiecePartID_Type(DisplayString):
    """Custom type chPiecePartID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_ChPiecePartID_Type.__name__ = "DisplayString"
_ChPiecePartID_Object = MibScalar
chPiecePartID = _ChPiecePartID_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 1, 16),
    _ChPiecePartID_Type()
)
chPiecePartID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chPiecePartID.setStatus("current")


class _ChPPIDRevision_Type(DisplayString):
    """Custom type chPPIDRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_ChPPIDRevision_Type.__name__ = "DisplayString"
_ChPPIDRevision_Object = MibScalar
chPPIDRevision = _ChPPIDRevision_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 1, 17),
    _ChPPIDRevision_Type()
)
chPPIDRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chPPIDRevision.setStatus("current")


class _ChServiceTag_Type(DisplayString):
    """Custom type chServiceTag based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_ChServiceTag_Type.__name__ = "DisplayString"
_ChServiceTag_Object = MibScalar
chServiceTag = _ChServiceTag_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 1, 18),
    _ChServiceTag_Type()
)
chServiceTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chServiceTag.setStatus("current")


class _ChExpressServiceCode_Type(DisplayString):
    """Custom type chExpressServiceCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_ChExpressServiceCode_Type.__name__ = "DisplayString"
_ChExpressServiceCode_Object = MibScalar
chExpressServiceCode = _ChExpressServiceCode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 1, 19),
    _ChExpressServiceCode_Type()
)
chExpressServiceCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chExpressServiceCode.setStatus("current")
_ChSysObjects_ObjectIdentity = ObjectIdentity
chSysObjects = _ChSysObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 2)
)
_ChSysCardTable_Object = MibTable
chSysCardTable = _ChSysCardTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 2, 1)
)
if mibBuilder.loadTexts:
    chSysCardTable.setStatus("current")
_ChSysCardEntry_Object = MibTableRow
chSysCardEntry = _ChSysCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 2, 1, 1)
)
chSysCardEntry.setIndexNames(
    (0, "F10-C-SERIES-CHASSIS-MIB", "chSysCardSlotIndex"),
)
if mibBuilder.loadTexts:
    chSysCardEntry.setStatus("current")
_ChSysCardSlotIndex_Type = Integer32
_ChSysCardSlotIndex_Object = MibTableColumn
chSysCardSlotIndex = _ChSysCardSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 2, 1, 1, 1),
    _ChSysCardSlotIndex_Type()
)
chSysCardSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysCardSlotIndex.setStatus("current")
_ChSysCardType_Type = F10CSeriesCardType
_ChSysCardType_Object = MibTableColumn
chSysCardType = _ChSysCardType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 2, 1, 1, 2),
    _ChSysCardType_Type()
)
chSysCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysCardType.setStatus("current")
_ChSysCardNumber_Type = Integer32
_ChSysCardNumber_Object = MibTableColumn
chSysCardNumber = _ChSysCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 2, 1, 1, 3),
    _ChSysCardNumber_Type()
)
chSysCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysCardNumber.setStatus("current")
_ChSysCardNumPorts_Type = Integer32
_ChSysCardNumPorts_Object = MibTableColumn
chSysCardNumPorts = _ChSysCardNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 2, 1, 1, 4),
    _ChSysCardNumPorts_Type()
)
chSysCardNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysCardNumPorts.setStatus("current")
_ChSysCardTemp_Type = Gauge32
_ChSysCardTemp_Object = MibTableColumn
chSysCardTemp = _ChSysCardTemp_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 2, 1, 1, 5),
    _ChSysCardTemp_Type()
)
chSysCardTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysCardTemp.setStatus("current")
_ChSysCardUpTime_Type = TimeTicks
_ChSysCardUpTime_Object = MibTableColumn
chSysCardUpTime = _ChSysCardUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 2, 1, 1, 6),
    _ChSysCardUpTime_Type()
)
chSysCardUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysCardUpTime.setStatus("current")


class _ChSysCardAdminStatus_Type(Integer32):
    """Custom type chSysCardAdminStatus based on Integer32"""
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


_ChSysCardAdminStatus_Type.__name__ = "Integer32"
_ChSysCardAdminStatus_Object = MibTableColumn
chSysCardAdminStatus = _ChSysCardAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 2, 1, 1, 7),
    _ChSysCardAdminStatus_Type()
)
chSysCardAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysCardAdminStatus.setStatus("current")
_ChSysCardOperStatus_Type = F10CardOperStatus
_ChSysCardOperStatus_Object = MibTableColumn
chSysCardOperStatus = _ChSysCardOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 2, 1, 1, 8),
    _ChSysCardOperStatus_Type()
)
chSysCardOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysCardOperStatus.setStatus("current")
_ChSysCardBootFlashA_Type = DisplayString
_ChSysCardBootFlashA_Object = MibTableColumn
chSysCardBootFlashA = _ChSysCardBootFlashA_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 2, 1, 1, 9),
    _ChSysCardBootFlashA_Type()
)
chSysCardBootFlashA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysCardBootFlashA.setStatus("current")
_ChSysCardBootFlashB_Type = DisplayString
_ChSysCardBootFlashB_Object = MibTableColumn
chSysCardBootFlashB = _ChSysCardBootFlashB_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 2, 1, 1, 10),
    _ChSysCardBootFlashB_Type()
)
chSysCardBootFlashB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysCardBootFlashB.setStatus("current")
_ChSysCardSerialNumber_Type = DisplayString
_ChSysCardSerialNumber_Object = MibTableColumn
chSysCardSerialNumber = _ChSysCardSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 2, 1, 1, 11),
    _ChSysCardSerialNumber_Type()
)
chSysCardSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysCardSerialNumber.setStatus("current")
_ChSysCardPartNum_Type = DisplayString
_ChSysCardPartNum_Object = MibTableColumn
chSysCardPartNum = _ChSysCardPartNum_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 2, 1, 1, 12),
    _ChSysCardPartNum_Type()
)
chSysCardPartNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysCardPartNum.setStatus("current")
_ChSysCardProductRev_Type = DisplayString
_ChSysCardProductRev_Object = MibTableColumn
chSysCardProductRev = _ChSysCardProductRev_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 2, 1, 1, 13),
    _ChSysCardProductRev_Type()
)
chSysCardProductRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysCardProductRev.setStatus("current")
_ChSysCardVendorId_Type = DisplayString
_ChSysCardVendorId_Object = MibTableColumn
chSysCardVendorId = _ChSysCardVendorId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 2, 1, 1, 14),
    _ChSysCardVendorId_Type()
)
chSysCardVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysCardVendorId.setStatus("current")
_ChSysCardDateCode_Type = F10MfgDate
_ChSysCardDateCode_Object = MibTableColumn
chSysCardDateCode = _ChSysCardDateCode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 2, 1, 1, 15),
    _ChSysCardDateCode_Type()
)
chSysCardDateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysCardDateCode.setStatus("current")


class _ChSysCardCountryCode_Type(OctetString):
    """Custom type chSysCardCountryCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_ChSysCardCountryCode_Type.__name__ = "OctetString"
_ChSysCardCountryCode_Object = MibTableColumn
chSysCardCountryCode = _ChSysCardCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 2, 1, 1, 16),
    _ChSysCardCountryCode_Type()
)
chSysCardCountryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysCardCountryCode.setStatus("current")


class _ChSysCardPiecePartID_Type(DisplayString):
    """Custom type chSysCardPiecePartID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_ChSysCardPiecePartID_Type.__name__ = "DisplayString"
_ChSysCardPiecePartID_Object = MibTableColumn
chSysCardPiecePartID = _ChSysCardPiecePartID_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 2, 1, 1, 17),
    _ChSysCardPiecePartID_Type()
)
chSysCardPiecePartID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysCardPiecePartID.setStatus("current")


class _ChSysCardPPIDRevision_Type(DisplayString):
    """Custom type chSysCardPPIDRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_ChSysCardPPIDRevision_Type.__name__ = "DisplayString"
_ChSysCardPPIDRevision_Object = MibTableColumn
chSysCardPPIDRevision = _ChSysCardPPIDRevision_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 2, 1, 1, 18),
    _ChSysCardPPIDRevision_Type()
)
chSysCardPPIDRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysCardPPIDRevision.setStatus("current")


class _ChSysCardServiceTag_Type(DisplayString):
    """Custom type chSysCardServiceTag based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_ChSysCardServiceTag_Type.__name__ = "DisplayString"
_ChSysCardServiceTag_Object = MibTableColumn
chSysCardServiceTag = _ChSysCardServiceTag_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 2, 1, 1, 19),
    _ChSysCardServiceTag_Type()
)
chSysCardServiceTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysCardServiceTag.setStatus("current")


class _ChSysCardExpressServiceCode_Type(DisplayString):
    """Custom type chSysCardExpressServiceCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_ChSysCardExpressServiceCode_Type.__name__ = "DisplayString"
_ChSysCardExpressServiceCode_Object = MibTableColumn
chSysCardExpressServiceCode = _ChSysCardExpressServiceCode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 2, 1, 1, 20),
    _ChSysCardExpressServiceCode_Type()
)
chSysCardExpressServiceCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysCardExpressServiceCode.setStatus("current")
_ChSysPortTable_Object = MibTable
chSysPortTable = _ChSysPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 2, 2)
)
if mibBuilder.loadTexts:
    chSysPortTable.setStatus("current")
_ChSysPortEntry_Object = MibTableRow
chSysPortEntry = _ChSysPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 2, 2, 1)
)
chSysPortEntry.setIndexNames(
    (0, "F10-C-SERIES-CHASSIS-MIB", "chSysPortSlotIndex"),
    (0, "F10-C-SERIES-CHASSIS-MIB", "chSysPortIndex"),
)
if mibBuilder.loadTexts:
    chSysPortEntry.setStatus("current")
_ChSysPortSlotIndex_Type = Integer32
_ChSysPortSlotIndex_Object = MibTableColumn
chSysPortSlotIndex = _ChSysPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 2, 2, 1, 1),
    _ChSysPortSlotIndex_Type()
)
chSysPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysPortSlotIndex.setStatus("current")
_ChSysPortIndex_Type = Integer32
_ChSysPortIndex_Object = MibTableColumn
chSysPortIndex = _ChSysPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 2, 2, 1, 2),
    _ChSysPortIndex_Type()
)
chSysPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysPortIndex.setStatus("current")
_ChSysPortType_Type = F10CSeriesPortType
_ChSysPortType_Object = MibTableColumn
chSysPortType = _ChSysPortType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 2, 2, 1, 3),
    _ChSysPortType_Type()
)
chSysPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysPortType.setStatus("current")


class _ChSysPortAdminStatus_Type(Integer32):
    """Custom type chSysPortAdminStatus based on Integer32"""
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


_ChSysPortAdminStatus_Type.__name__ = "Integer32"
_ChSysPortAdminStatus_Object = MibTableColumn
chSysPortAdminStatus = _ChSysPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 2, 2, 1, 4),
    _ChSysPortAdminStatus_Type()
)
chSysPortAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysPortAdminStatus.setStatus("current")


class _ChSysPortOperStatus_Type(Integer32):
    """Custom type chSysPortOperStatus based on Integer32"""
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


_ChSysPortOperStatus_Type.__name__ = "Integer32"
_ChSysPortOperStatus_Object = MibTableColumn
chSysPortOperStatus = _ChSysPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 2, 2, 1, 5),
    _ChSysPortOperStatus_Type()
)
chSysPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysPortOperStatus.setStatus("current")
_ChSysPortIfIndex_Type = Integer32
_ChSysPortIfIndex_Object = MibTableColumn
chSysPortIfIndex = _ChSysPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 2, 2, 1, 6),
    _ChSysPortIfIndex_Type()
)
chSysPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysPortIfIndex.setStatus("current")
_ChSysXfpRecvPower_Type = F10HundredthdB
_ChSysXfpRecvPower_Object = MibTableColumn
chSysXfpRecvPower = _ChSysXfpRecvPower_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 2, 2, 1, 7),
    _ChSysXfpRecvPower_Type()
)
chSysXfpRecvPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysXfpRecvPower.setStatus("current")
if mibBuilder.loadTexts:
    chSysXfpRecvPower.setUnits("dB")
_ChSysProcessorTable_Object = MibTable
chSysProcessorTable = _ChSysProcessorTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 2, 3)
)
if mibBuilder.loadTexts:
    chSysProcessorTable.setStatus("current")
_ChSysProcessorEntry_Object = MibTableRow
chSysProcessorEntry = _ChSysProcessorEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 2, 3, 1)
)
chSysProcessorEntry.setIndexNames(
    (0, "F10-C-SERIES-CHASSIS-MIB", "chSysProcessorSlotIndex"),
    (0, "F10-C-SERIES-CHASSIS-MIB", "chSysProcessorIndex"),
)
if mibBuilder.loadTexts:
    chSysProcessorEntry.setStatus("current")
_ChSysProcessorSlotIndex_Type = Integer32
_ChSysProcessorSlotIndex_Object = MibTableColumn
chSysProcessorSlotIndex = _ChSysProcessorSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 2, 3, 1, 1),
    _ChSysProcessorSlotIndex_Type()
)
chSysProcessorSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysProcessorSlotIndex.setStatus("current")
_ChSysProcessorIndex_Type = Integer32
_ChSysProcessorIndex_Object = MibTableColumn
chSysProcessorIndex = _ChSysProcessorIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 2, 3, 1, 2),
    _ChSysProcessorIndex_Type()
)
chSysProcessorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysProcessorIndex.setStatus("current")
_ChSysProcessorModule_Type = F10ProcessorModuleType
_ChSysProcessorModule_Object = MibTableColumn
chSysProcessorModule = _ChSysProcessorModule_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 2, 3, 1, 3),
    _ChSysProcessorModule_Type()
)
chSysProcessorModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysProcessorModule.setStatus("current")
_ChSysProcessorUpTime_Type = TimeTicks
_ChSysProcessorUpTime_Object = MibTableColumn
chSysProcessorUpTime = _ChSysProcessorUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 2, 3, 1, 4),
    _ChSysProcessorUpTime_Type()
)
chSysProcessorUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysProcessorUpTime.setStatus("current")
_ChSysProcessorNvramSize_Type = Integer32
_ChSysProcessorNvramSize_Object = MibTableColumn
chSysProcessorNvramSize = _ChSysProcessorNvramSize_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 2, 3, 1, 5),
    _ChSysProcessorNvramSize_Type()
)
chSysProcessorNvramSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysProcessorNvramSize.setStatus("current")
_ChSysProcessorMemSize_Type = Integer32
_ChSysProcessorMemSize_Object = MibTableColumn
chSysProcessorMemSize = _ChSysProcessorMemSize_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 2, 3, 1, 6),
    _ChSysProcessorMemSize_Type()
)
chSysProcessorMemSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysProcessorMemSize.setStatus("current")
_ChSysSwModuleTable_Object = MibTable
chSysSwModuleTable = _ChSysSwModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 2, 4)
)
if mibBuilder.loadTexts:
    chSysSwModuleTable.setStatus("current")
_ChSysSwModuleEntry_Object = MibTableRow
chSysSwModuleEntry = _ChSysSwModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 2, 4, 1)
)
chSysSwModuleEntry.setIndexNames(
    (0, "F10-C-SERIES-CHASSIS-MIB", "chSysSwSlotIndex"),
    (0, "F10-C-SERIES-CHASSIS-MIB", "chSysSwProcessorIndex"),
)
if mibBuilder.loadTexts:
    chSysSwModuleEntry.setStatus("current")
_ChSysSwSlotIndex_Type = Integer32
_ChSysSwSlotIndex_Object = MibTableColumn
chSysSwSlotIndex = _ChSysSwSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 2, 4, 1, 1),
    _ChSysSwSlotIndex_Type()
)
chSysSwSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysSwSlotIndex.setStatus("current")
_ChSysSwProcessorIndex_Type = Integer32
_ChSysSwProcessorIndex_Object = MibTableColumn
chSysSwProcessorIndex = _ChSysSwProcessorIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 2, 4, 1, 2),
    _ChSysSwProcessorIndex_Type()
)
chSysSwProcessorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysSwProcessorIndex.setStatus("current")
_ChSysSwRuntimeImgVersion_Type = DisplayString
_ChSysSwRuntimeImgVersion_Object = MibTableColumn
chSysSwRuntimeImgVersion = _ChSysSwRuntimeImgVersion_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 2, 4, 1, 3),
    _ChSysSwRuntimeImgVersion_Type()
)
chSysSwRuntimeImgVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysSwRuntimeImgVersion.setStatus("current")
_ChSysSwRuntimeImgDate_Type = F10SwDate
_ChSysSwRuntimeImgDate_Object = MibTableColumn
chSysSwRuntimeImgDate = _ChSysSwRuntimeImgDate_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 2, 4, 1, 4),
    _ChSysSwRuntimeImgDate_Type()
)
chSysSwRuntimeImgDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysSwRuntimeImgDate.setStatus("current")
_ChSysSwCurrentBootImgVersion_Type = DisplayString
_ChSysSwCurrentBootImgVersion_Object = MibTableColumn
chSysSwCurrentBootImgVersion = _ChSysSwCurrentBootImgVersion_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 2, 4, 1, 5),
    _ChSysSwCurrentBootImgVersion_Type()
)
chSysSwCurrentBootImgVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysSwCurrentBootImgVersion.setStatus("current")
_ChSysSwCurrentBootImgDate_Type = DateAndTime
_ChSysSwCurrentBootImgDate_Object = MibTableColumn
chSysSwCurrentBootImgDate = _ChSysSwCurrentBootImgDate_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 2, 4, 1, 6),
    _ChSysSwCurrentBootImgDate_Type()
)
chSysSwCurrentBootImgDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysSwCurrentBootImgDate.setStatus("current")


class _ChSysSwCurrentBootImgStatus_Type(Integer32):
    """Custom type chSysSwCurrentBootImgStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 2),
          ("ok", 1))
    )


_ChSysSwCurrentBootImgStatus_Type.__name__ = "Integer32"
_ChSysSwCurrentBootImgStatus_Object = MibTableColumn
chSysSwCurrentBootImgStatus = _ChSysSwCurrentBootImgStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 2, 4, 1, 7),
    _ChSysSwCurrentBootImgStatus_Type()
)
chSysSwCurrentBootImgStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysSwCurrentBootImgStatus.setStatus("current")
_ChSysSwBackupBootImgVersion_Type = DisplayString
_ChSysSwBackupBootImgVersion_Object = MibTableColumn
chSysSwBackupBootImgVersion = _ChSysSwBackupBootImgVersion_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 2, 4, 1, 8),
    _ChSysSwBackupBootImgVersion_Type()
)
chSysSwBackupBootImgVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysSwBackupBootImgVersion.setStatus("current")
_ChSysSwBackupBootImgDate_Type = DateAndTime
_ChSysSwBackupBootImgDate_Object = MibTableColumn
chSysSwBackupBootImgDate = _ChSysSwBackupBootImgDate_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 2, 4, 1, 9),
    _ChSysSwBackupBootImgDate_Type()
)
chSysSwBackupBootImgDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysSwBackupBootImgDate.setStatus("current")


class _ChSysSwBackupBootImgStatus_Type(Integer32):
    """Custom type chSysSwBackupBootImgStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 2),
          ("ok", 1))
    )


_ChSysSwBackupBootImgStatus_Type.__name__ = "Integer32"
_ChSysSwBackupBootImgStatus_Object = MibTableColumn
chSysSwBackupBootImgStatus = _ChSysSwBackupBootImgStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 2, 4, 1, 10),
    _ChSysSwBackupBootImgStatus_Type()
)
chSysSwBackupBootImgStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysSwBackupBootImgStatus.setStatus("current")


class _ChSysSwNextRebootImage_Type(Integer32):
    """Custom type chSysSwNextRebootImage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bootImage-A", 1),
          ("bootImage-B", 2))
    )


_ChSysSwNextRebootImage_Type.__name__ = "Integer32"
_ChSysSwNextRebootImage_Object = MibTableColumn
chSysSwNextRebootImage = _ChSysSwNextRebootImage_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 2, 4, 1, 11),
    _ChSysSwNextRebootImage_Type()
)
chSysSwNextRebootImage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysSwNextRebootImage.setStatus("current")


class _ChSysSwCurrentBootImage_Type(Integer32):
    """Custom type chSysSwCurrentBootImage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bootImage-A", 1),
          ("bootImage-B", 2))
    )


_ChSysSwCurrentBootImage_Type.__name__ = "Integer32"
_ChSysSwCurrentBootImage_Object = MibTableColumn
chSysSwCurrentBootImage = _ChSysSwCurrentBootImage_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 2, 4, 1, 12),
    _ChSysSwCurrentBootImage_Type()
)
chSysSwCurrentBootImage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysSwCurrentBootImage.setStatus("current")
_ChSysPowerSupplyTable_Object = MibTable
chSysPowerSupplyTable = _ChSysPowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 2, 5)
)
if mibBuilder.loadTexts:
    chSysPowerSupplyTable.setStatus("current")
_ChSysPowerSupplyEntry_Object = MibTableRow
chSysPowerSupplyEntry = _ChSysPowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 2, 5, 1)
)
chSysPowerSupplyEntry.setIndexNames(
    (0, "F10-C-SERIES-CHASSIS-MIB", "chSysPowerSupplyIndex"),
)
if mibBuilder.loadTexts:
    chSysPowerSupplyEntry.setStatus("current")
_ChSysPowerSupplyIndex_Type = Integer32
_ChSysPowerSupplyIndex_Object = MibTableColumn
chSysPowerSupplyIndex = _ChSysPowerSupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 2, 5, 1, 1),
    _ChSysPowerSupplyIndex_Type()
)
chSysPowerSupplyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysPowerSupplyIndex.setStatus("current")


class _ChSysPowerSupplyOperStatus_Type(Integer32):
    """Custom type chSysPowerSupplyOperStatus based on Integer32"""
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


_ChSysPowerSupplyOperStatus_Type.__name__ = "Integer32"
_ChSysPowerSupplyOperStatus_Object = MibTableColumn
chSysPowerSupplyOperStatus = _ChSysPowerSupplyOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 2, 5, 1, 2),
    _ChSysPowerSupplyOperStatus_Type()
)
chSysPowerSupplyOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysPowerSupplyOperStatus.setStatus("current")


class _ChSysPowerSupplyType_Type(Integer32):
    """Custom type chSysPowerSupplyType based on Integer32"""
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
          ("ac", 1),
          ("dc", 2))
    )


_ChSysPowerSupplyType_Type.__name__ = "Integer32"
_ChSysPowerSupplyType_Object = MibTableColumn
chSysPowerSupplyType = _ChSysPowerSupplyType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 2, 5, 1, 3),
    _ChSysPowerSupplyType_Type()
)
chSysPowerSupplyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysPowerSupplyType.setStatus("current")


class _ChSysPowerSupplyVersion_Type(Integer32):
    """Custom type chSysPowerSupplyVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("version1", 2),
          ("version2", 3))
    )


_ChSysPowerSupplyVersion_Type.__name__ = "Integer32"
_ChSysPowerSupplyVersion_Object = MibTableColumn
chSysPowerSupplyVersion = _ChSysPowerSupplyVersion_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 2, 5, 1, 4),
    _ChSysPowerSupplyVersion_Type()
)
chSysPowerSupplyVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysPowerSupplyVersion.setStatus("current")


class _ChSysPowerSupplyMode_Type(Integer32):
    """Custom type chSysPowerSupplyMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("high", 3),
          ("low", 2),
          ("unknown", 1))
    )


_ChSysPowerSupplyMode_Type.__name__ = "Integer32"
_ChSysPowerSupplyMode_Object = MibTableColumn
chSysPowerSupplyMode = _ChSysPowerSupplyMode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 2, 5, 1, 5),
    _ChSysPowerSupplyMode_Type()
)
chSysPowerSupplyMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysPowerSupplyMode.setStatus("current")
_ChSysFanTrayTable_Object = MibTable
chSysFanTrayTable = _ChSysFanTrayTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 2, 6)
)
if mibBuilder.loadTexts:
    chSysFanTrayTable.setStatus("current")
_ChSysFanTrayEntry_Object = MibTableRow
chSysFanTrayEntry = _ChSysFanTrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 2, 6, 1)
)
chSysFanTrayEntry.setIndexNames(
    (0, "F10-C-SERIES-CHASSIS-MIB", "chSysFanTrayIndex"),
)
if mibBuilder.loadTexts:
    chSysFanTrayEntry.setStatus("current")
_ChSysFanTrayIndex_Type = Integer32
_ChSysFanTrayIndex_Object = MibTableColumn
chSysFanTrayIndex = _ChSysFanTrayIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 2, 6, 1, 1),
    _ChSysFanTrayIndex_Type()
)
chSysFanTrayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysFanTrayIndex.setStatus("current")


class _ChSysFanTrayOperStatus_Type(Integer32):
    """Custom type chSysFanTrayOperStatus based on Integer32"""
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


_ChSysFanTrayOperStatus_Type.__name__ = "Integer32"
_ChSysFanTrayOperStatus_Object = MibTableColumn
chSysFanTrayOperStatus = _ChSysFanTrayOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 2, 6, 1, 2),
    _ChSysFanTrayOperStatus_Type()
)
chSysFanTrayOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysFanTrayOperStatus.setStatus("current")
_ChSysSfmTable_Object = MibTable
chSysSfmTable = _ChSysSfmTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 2, 7)
)
if mibBuilder.loadTexts:
    chSysSfmTable.setStatus("current")
_ChSysSfmEntry_Object = MibTableRow
chSysSfmEntry = _ChSysSfmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 2, 7, 1)
)
chSysSfmEntry.setIndexNames(
    (0, "F10-C-SERIES-CHASSIS-MIB", "chSysSfmIndex"),
)
if mibBuilder.loadTexts:
    chSysSfmEntry.setStatus("current")
_ChSysSfmIndex_Type = Integer32
_ChSysSfmIndex_Object = MibTableColumn
chSysSfmIndex = _ChSysSfmIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 2, 7, 1, 1),
    _ChSysSfmIndex_Type()
)
chSysSfmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysSfmIndex.setStatus("current")


class _ChSysSfmAdminStatus_Type(Integer32):
    """Custom type chSysSfmAdminStatus based on Integer32"""
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


_ChSysSfmAdminStatus_Type.__name__ = "Integer32"
_ChSysSfmAdminStatus_Object = MibTableColumn
chSysSfmAdminStatus = _ChSysSfmAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 2, 7, 1, 2),
    _ChSysSfmAdminStatus_Type()
)
chSysSfmAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysSfmAdminStatus.setStatus("current")


class _ChSysSfmOperStatus_Type(Integer32):
    """Custom type chSysSfmOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("absent", 2),
          ("active", 1),
          ("standby", 3))
    )


_ChSysSfmOperStatus_Type.__name__ = "Integer32"
_ChSysSfmOperStatus_Object = MibTableColumn
chSysSfmOperStatus = _ChSysSfmOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 2, 7, 1, 3),
    _ChSysSfmOperStatus_Type()
)
chSysSfmOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysSfmOperStatus.setStatus("current")


class _ChSysSfmErrorStatus_Type(Integer32):
    """Custom type chSysSfmErrorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("error", 2),
          ("not-available", 3),
          ("ok", 1))
    )


_ChSysSfmErrorStatus_Type.__name__ = "Integer32"
_ChSysSfmErrorStatus_Object = MibTableColumn
chSysSfmErrorStatus = _ChSysSfmErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 2, 7, 1, 4),
    _ChSysSfmErrorStatus_Type()
)
chSysSfmErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysSfmErrorStatus.setStatus("current")
_ChRpmObjects_ObjectIdentity = ObjectIdentity
chRpmObjects = _ChRpmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 3)
)
_ChRpmNumRpms_Type = Integer32
_ChRpmNumRpms_Object = MibScalar
chRpmNumRpms = _ChRpmNumRpms_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 3, 1),
    _ChRpmNumRpms_Type()
)
chRpmNumRpms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chRpmNumRpms.setStatus("current")
_ChRpmSlotNumber_Type = Integer32
_ChRpmSlotNumber_Object = MibScalar
chRpmSlotNumber = _ChRpmSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 3, 2),
    _ChRpmSlotNumber_Type()
)
chRpmSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chRpmSlotNumber.setStatus("current")
_ChRpmUptime_Type = TimeTicks
_ChRpmUptime_Object = MibScalar
chRpmUptime = _ChRpmUptime_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 3, 3),
    _ChRpmUptime_Type()
)
chRpmUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chRpmUptime.setStatus("current")
_ChRpmLastSwitchDate_Type = DateAndTime
_ChRpmLastSwitchDate_Object = MibScalar
chRpmLastSwitchDate = _ChRpmLastSwitchDate_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 3, 4),
    _ChRpmLastSwitchDate_Type()
)
chRpmLastSwitchDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chRpmLastSwitchDate.setStatus("current")


class _ChRpmMajorAlarmStatus_Type(Integer32):
    """Custom type chRpmMajorAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_ChRpmMajorAlarmStatus_Type.__name__ = "Integer32"
_ChRpmMajorAlarmStatus_Object = MibScalar
chRpmMajorAlarmStatus = _ChRpmMajorAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 3, 5),
    _ChRpmMajorAlarmStatus_Type()
)
chRpmMajorAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chRpmMajorAlarmStatus.setStatus("current")


class _ChRpmMinorAlarmStatus_Type(Integer32):
    """Custom type chRpmMinorAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_ChRpmMinorAlarmStatus_Type.__name__ = "Integer32"
_ChRpmMinorAlarmStatus_Object = MibScalar
chRpmMinorAlarmStatus = _ChRpmMinorAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 3, 6),
    _ChRpmMinorAlarmStatus_Type()
)
chRpmMinorAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chRpmMinorAlarmStatus.setStatus("current")
_ChRpmUtilTable_Object = MibTable
chRpmUtilTable = _ChRpmUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 3, 7)
)
if mibBuilder.loadTexts:
    chRpmUtilTable.setStatus("current")
_ChRpmUtilEntry_Object = MibTableRow
chRpmUtilEntry = _ChRpmUtilEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 3, 7, 1)
)
chRpmUtilEntry.setIndexNames(
    (0, "F10-C-SERIES-CHASSIS-MIB", "chRpmCpuIndex"),
)
if mibBuilder.loadTexts:
    chRpmUtilEntry.setStatus("current")
_ChRpmCpuIndex_Type = Integer32
_ChRpmCpuIndex_Object = MibTableColumn
chRpmCpuIndex = _ChRpmCpuIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 3, 7, 1, 1),
    _ChRpmCpuIndex_Type()
)
chRpmCpuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chRpmCpuIndex.setStatus("current")
_ChRpmCpuType_Type = F10ProcessorModuleType
_ChRpmCpuType_Object = MibTableColumn
chRpmCpuType = _ChRpmCpuType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 3, 7, 1, 2),
    _ChRpmCpuType_Type()
)
chRpmCpuType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chRpmCpuType.setStatus("current")


class _ChRpmCpuUtil5Sec_Type(Gauge32):
    """Custom type chRpmCpuUtil5Sec based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ChRpmCpuUtil5Sec_Type.__name__ = "Gauge32"
_ChRpmCpuUtil5Sec_Object = MibTableColumn
chRpmCpuUtil5Sec = _ChRpmCpuUtil5Sec_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 3, 7, 1, 3),
    _ChRpmCpuUtil5Sec_Type()
)
chRpmCpuUtil5Sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chRpmCpuUtil5Sec.setStatus("current")
if mibBuilder.loadTexts:
    chRpmCpuUtil5Sec.setUnits("percent")


class _ChRpmCpuUtil1Min_Type(Gauge32):
    """Custom type chRpmCpuUtil1Min based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ChRpmCpuUtil1Min_Type.__name__ = "Gauge32"
_ChRpmCpuUtil1Min_Object = MibTableColumn
chRpmCpuUtil1Min = _ChRpmCpuUtil1Min_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 3, 7, 1, 4),
    _ChRpmCpuUtil1Min_Type()
)
chRpmCpuUtil1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chRpmCpuUtil1Min.setStatus("current")
if mibBuilder.loadTexts:
    chRpmCpuUtil1Min.setUnits("percent")


class _ChRpmCpuUtil5Min_Type(Gauge32):
    """Custom type chRpmCpuUtil5Min based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ChRpmCpuUtil5Min_Type.__name__ = "Gauge32"
_ChRpmCpuUtil5Min_Object = MibTableColumn
chRpmCpuUtil5Min = _ChRpmCpuUtil5Min_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 3, 7, 1, 5),
    _ChRpmCpuUtil5Min_Type()
)
chRpmCpuUtil5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chRpmCpuUtil5Min.setStatus("current")
if mibBuilder.loadTexts:
    chRpmCpuUtil5Min.setUnits("percent")


class _ChRpmMemUsageUtil_Type(Gauge32):
    """Custom type chRpmMemUsageUtil based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ChRpmMemUsageUtil_Type.__name__ = "Gauge32"
_ChRpmMemUsageUtil_Object = MibTableColumn
chRpmMemUsageUtil = _ChRpmMemUsageUtil_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 3, 7, 1, 6),
    _ChRpmMemUsageUtil_Type()
)
chRpmMemUsageUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chRpmMemUsageUtil.setStatus("current")
if mibBuilder.loadTexts:
    chRpmMemUsageUtil.setUnits("percent")
_ChAlarmObjects_ObjectIdentity = ObjectIdentity
chAlarmObjects = _ChAlarmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 4)
)
_ChLineCardObjects_ObjectIdentity = ObjectIdentity
chLineCardObjects = _ChLineCardObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 5)
)
_ChLineCardUtilTable_Object = MibTable
chLineCardUtilTable = _ChLineCardUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 5, 1)
)
if mibBuilder.loadTexts:
    chLineCardUtilTable.setStatus("current")
_ChLineCardUtilEntry_Object = MibTableRow
chLineCardUtilEntry = _ChLineCardUtilEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 5, 1, 1)
)
chLineCardUtilEntry.setIndexNames(
    (0, "F10-C-SERIES-CHASSIS-MIB", "chSysCardNumber"),
)
if mibBuilder.loadTexts:
    chLineCardUtilEntry.setStatus("current")


class _ChLineCardCpuUtil5Sec_Type(Gauge32):
    """Custom type chLineCardCpuUtil5Sec based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ChLineCardCpuUtil5Sec_Type.__name__ = "Gauge32"
_ChLineCardCpuUtil5Sec_Object = MibTableColumn
chLineCardCpuUtil5Sec = _ChLineCardCpuUtil5Sec_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 5, 1, 1, 1),
    _ChLineCardCpuUtil5Sec_Type()
)
chLineCardCpuUtil5Sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chLineCardCpuUtil5Sec.setStatus("current")
if mibBuilder.loadTexts:
    chLineCardCpuUtil5Sec.setUnits("percent")


class _ChLineCardCpuUtil1Min_Type(Gauge32):
    """Custom type chLineCardCpuUtil1Min based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ChLineCardCpuUtil1Min_Type.__name__ = "Gauge32"
_ChLineCardCpuUtil1Min_Object = MibTableColumn
chLineCardCpuUtil1Min = _ChLineCardCpuUtil1Min_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 5, 1, 1, 2),
    _ChLineCardCpuUtil1Min_Type()
)
chLineCardCpuUtil1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chLineCardCpuUtil1Min.setStatus("current")
if mibBuilder.loadTexts:
    chLineCardCpuUtil1Min.setUnits("percent")


class _ChLineCardCpuUtil5Min_Type(Gauge32):
    """Custom type chLineCardCpuUtil5Min based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ChLineCardCpuUtil5Min_Type.__name__ = "Gauge32"
_ChLineCardCpuUtil5Min_Object = MibTableColumn
chLineCardCpuUtil5Min = _ChLineCardCpuUtil5Min_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 5, 1, 1, 3),
    _ChLineCardCpuUtil5Min_Type()
)
chLineCardCpuUtil5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chLineCardCpuUtil5Min.setStatus("current")
if mibBuilder.loadTexts:
    chLineCardCpuUtil5Min.setUnits("percent")


class _ChLineCardMemUsageUtil_Type(Gauge32):
    """Custom type chLineCardMemUsageUtil based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ChLineCardMemUsageUtil_Type.__name__ = "Gauge32"
_ChLineCardMemUsageUtil_Object = MibTableColumn
chLineCardMemUsageUtil = _ChLineCardMemUsageUtil_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 1, 5, 1, 1, 4),
    _ChLineCardMemUsageUtil_Type()
)
chLineCardMemUsageUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chLineCardMemUsageUtil.setStatus("current")
if mibBuilder.loadTexts:
    chLineCardMemUsageUtil.setUnits("percent")
_F10CSerChassisMibConformance_ObjectIdentity = ObjectIdentity
f10CSerChassisMibConformance = _F10CSerChassisMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 2)
)
_F10CSerChassisMibCompliances_ObjectIdentity = ObjectIdentity
f10CSerChassisMibCompliances = _F10CSerChassisMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 2, 1)
)
_F10CSerChassisMibGroups_ObjectIdentity = ObjectIdentity
f10CSerChassisMibGroups = _F10CSerChassisMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 2, 2)
)

# Managed Objects groups

f10CSerComponentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 2, 2, 1)
)
f10CSerComponentGroup.setObjects(
      *(("F10-C-SERIES-CHASSIS-MIB", "chType"),
        ("F10-C-SERIES-CHASSIS-MIB", "chChassisMode"),
        ("F10-C-SERIES-CHASSIS-MIB", "chSwVersion"),
        ("F10-C-SERIES-CHASSIS-MIB", "chMacAddr"),
        ("F10-C-SERIES-CHASSIS-MIB", "chSerialNumber"),
        ("F10-C-SERIES-CHASSIS-MIB", "chPartNum"),
        ("F10-C-SERIES-CHASSIS-MIB", "chProductRev"),
        ("F10-C-SERIES-CHASSIS-MIB", "chVendorId"),
        ("F10-C-SERIES-CHASSIS-MIB", "chDateCode"),
        ("F10-C-SERIES-CHASSIS-MIB", "chCountryCode"),
        ("F10-C-SERIES-CHASSIS-MIB", "chPiecePartID"),
        ("F10-C-SERIES-CHASSIS-MIB", "chPPIDRevision"),
        ("F10-C-SERIES-CHASSIS-MIB", "chServiceTag"),
        ("F10-C-SERIES-CHASSIS-MIB", "chExpressServiceCode"),
        ("F10-C-SERIES-CHASSIS-MIB", "chNumSlots"),
        ("F10-C-SERIES-CHASSIS-MIB", "chNumLinecards"),
        ("F10-C-SERIES-CHASSIS-MIB", "chNumFanTrays"),
        ("F10-C-SERIES-CHASSIS-MIB", "chNumPowerSupplies"),
        ("F10-C-SERIES-CHASSIS-MIB", "chNumSfmSlots"))
)
if mibBuilder.loadTexts:
    f10CSerComponentGroup.setStatus("current")

f10CSerSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 2, 2, 2)
)
f10CSerSystemGroup.setObjects(
      *(("F10-C-SERIES-CHASSIS-MIB", "chSysCardType"),
        ("F10-C-SERIES-CHASSIS-MIB", "chSysCardNumber"),
        ("F10-C-SERIES-CHASSIS-MIB", "chSysCardNumPorts"),
        ("F10-C-SERIES-CHASSIS-MIB", "chSysCardTemp"),
        ("F10-C-SERIES-CHASSIS-MIB", "chSysCardUpTime"),
        ("F10-C-SERIES-CHASSIS-MIB", "chSysCardAdminStatus"),
        ("F10-C-SERIES-CHASSIS-MIB", "chSysCardOperStatus"),
        ("F10-C-SERIES-CHASSIS-MIB", "chSysCardBootFlashA"),
        ("F10-C-SERIES-CHASSIS-MIB", "chSysCardBootFlashB"),
        ("F10-C-SERIES-CHASSIS-MIB", "chSysCardSerialNumber"),
        ("F10-C-SERIES-CHASSIS-MIB", "chSysCardPartNum"),
        ("F10-C-SERIES-CHASSIS-MIB", "chSysCardProductRev"),
        ("F10-C-SERIES-CHASSIS-MIB", "chSysCardVendorId"),
        ("F10-C-SERIES-CHASSIS-MIB", "chSysCardDateCode"),
        ("F10-C-SERIES-CHASSIS-MIB", "chSysCardCountryCode"),
        ("F10-C-SERIES-CHASSIS-MIB", "chSysCardPiecePartID"),
        ("F10-C-SERIES-CHASSIS-MIB", "chSysCardPPIDRevision"),
        ("F10-C-SERIES-CHASSIS-MIB", "chSysCardServiceTag"),
        ("F10-C-SERIES-CHASSIS-MIB", "chSysCardExpressServiceCode"),
        ("F10-C-SERIES-CHASSIS-MIB", "chSysPortType"),
        ("F10-C-SERIES-CHASSIS-MIB", "chSysPortAdminStatus"),
        ("F10-C-SERIES-CHASSIS-MIB", "chSysPortOperStatus"),
        ("F10-C-SERIES-CHASSIS-MIB", "chSysPortIfIndex"),
        ("F10-C-SERIES-CHASSIS-MIB", "chSysXfpRecvPower"),
        ("F10-C-SERIES-CHASSIS-MIB", "chSysProcessorModule"),
        ("F10-C-SERIES-CHASSIS-MIB", "chSysProcessorUpTime"),
        ("F10-C-SERIES-CHASSIS-MIB", "chSysProcessorNvramSize"),
        ("F10-C-SERIES-CHASSIS-MIB", "chSysProcessorMemSize"),
        ("F10-C-SERIES-CHASSIS-MIB", "chSysSwRuntimeImgVersion"),
        ("F10-C-SERIES-CHASSIS-MIB", "chSysSwRuntimeImgDate"),
        ("F10-C-SERIES-CHASSIS-MIB", "chSysSwCurrentBootImgVersion"),
        ("F10-C-SERIES-CHASSIS-MIB", "chSysSwCurrentBootImgDate"),
        ("F10-C-SERIES-CHASSIS-MIB", "chSysSwCurrentBootImgStatus"),
        ("F10-C-SERIES-CHASSIS-MIB", "chSysSwBackupBootImgVersion"),
        ("F10-C-SERIES-CHASSIS-MIB", "chSysSwBackupBootImgDate"),
        ("F10-C-SERIES-CHASSIS-MIB", "chSysSwBackupBootImgStatus"),
        ("F10-C-SERIES-CHASSIS-MIB", "chSysSwNextRebootImage"),
        ("F10-C-SERIES-CHASSIS-MIB", "chSysSwCurrentBootImage"),
        ("F10-C-SERIES-CHASSIS-MIB", "chSysPowerSupplyOperStatus"),
        ("F10-C-SERIES-CHASSIS-MIB", "chSysPowerSupplyType"),
        ("F10-C-SERIES-CHASSIS-MIB", "chSysPowerSupplyVersion"),
        ("F10-C-SERIES-CHASSIS-MIB", "chSysPowerSupplyMode"),
        ("F10-C-SERIES-CHASSIS-MIB", "chSysFanTrayOperStatus"),
        ("F10-C-SERIES-CHASSIS-MIB", "chSysSfmAdminStatus"),
        ("F10-C-SERIES-CHASSIS-MIB", "chSysSfmOperStatus"),
        ("F10-C-SERIES-CHASSIS-MIB", "chSysSfmErrorStatus"))
)
if mibBuilder.loadTexts:
    f10CSerSystemGroup.setStatus("current")

f10CSerRpmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 2, 2, 3)
)
f10CSerRpmGroup.setObjects(
      *(("F10-C-SERIES-CHASSIS-MIB", "chRpmNumRpms"),
        ("F10-C-SERIES-CHASSIS-MIB", "chRpmSlotNumber"),
        ("F10-C-SERIES-CHASSIS-MIB", "chRpmUptime"),
        ("F10-C-SERIES-CHASSIS-MIB", "chRpmLastSwitchDate"),
        ("F10-C-SERIES-CHASSIS-MIB", "chRpmMajorAlarmStatus"),
        ("F10-C-SERIES-CHASSIS-MIB", "chRpmMinorAlarmStatus"),
        ("F10-C-SERIES-CHASSIS-MIB", "chRpmCpuType"),
        ("F10-C-SERIES-CHASSIS-MIB", "chRpmCpuUtil5Sec"),
        ("F10-C-SERIES-CHASSIS-MIB", "chRpmCpuUtil1Min"),
        ("F10-C-SERIES-CHASSIS-MIB", "chRpmCpuUtil5Min"),
        ("F10-C-SERIES-CHASSIS-MIB", "chRpmMemUsageUtil"))
)
if mibBuilder.loadTexts:
    f10CSerRpmGroup.setStatus("current")

f10CSerLineCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 2, 2, 4)
)
f10CSerLineCardGroup.setObjects(
      *(("F10-C-SERIES-CHASSIS-MIB", "chLineCardCpuUtil5Sec"),
        ("F10-C-SERIES-CHASSIS-MIB", "chLineCardCpuUtil1Min"),
        ("F10-C-SERIES-CHASSIS-MIB", "chLineCardCpuUtil5Min"),
        ("F10-C-SERIES-CHASSIS-MIB", "chLineCardMemUsageUtil"))
)
if mibBuilder.loadTexts:
    f10CSerLineCardGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

f10CSerChassisMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6027, 3, 8, 2, 1, 1)
)
if mibBuilder.loadTexts:
    f10CSerChassisMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "F10-C-SERIES-CHASSIS-MIB",
    **{"f10CSerChassisMib": f10CSerChassisMib,
       "f10CSerChassisObject": f10CSerChassisObject,
       "chObjects": chObjects,
       "chType": chType,
       "chChassisMode": chChassisMode,
       "chSwVersion": chSwVersion,
       "chMacAddr": chMacAddr,
       "chSerialNumber": chSerialNumber,
       "chPartNum": chPartNum,
       "chProductRev": chProductRev,
       "chVendorId": chVendorId,
       "chDateCode": chDateCode,
       "chCountryCode": chCountryCode,
       "chNumSlots": chNumSlots,
       "chNumLinecards": chNumLinecards,
       "chNumFanTrays": chNumFanTrays,
       "chNumPowerSupplies": chNumPowerSupplies,
       "chNumSfmSlots": chNumSfmSlots,
       "chPiecePartID": chPiecePartID,
       "chPPIDRevision": chPPIDRevision,
       "chServiceTag": chServiceTag,
       "chExpressServiceCode": chExpressServiceCode,
       "chSysObjects": chSysObjects,
       "chSysCardTable": chSysCardTable,
       "chSysCardEntry": chSysCardEntry,
       "chSysCardSlotIndex": chSysCardSlotIndex,
       "chSysCardType": chSysCardType,
       "chSysCardNumber": chSysCardNumber,
       "chSysCardNumPorts": chSysCardNumPorts,
       "chSysCardTemp": chSysCardTemp,
       "chSysCardUpTime": chSysCardUpTime,
       "chSysCardAdminStatus": chSysCardAdminStatus,
       "chSysCardOperStatus": chSysCardOperStatus,
       "chSysCardBootFlashA": chSysCardBootFlashA,
       "chSysCardBootFlashB": chSysCardBootFlashB,
       "chSysCardSerialNumber": chSysCardSerialNumber,
       "chSysCardPartNum": chSysCardPartNum,
       "chSysCardProductRev": chSysCardProductRev,
       "chSysCardVendorId": chSysCardVendorId,
       "chSysCardDateCode": chSysCardDateCode,
       "chSysCardCountryCode": chSysCardCountryCode,
       "chSysCardPiecePartID": chSysCardPiecePartID,
       "chSysCardPPIDRevision": chSysCardPPIDRevision,
       "chSysCardServiceTag": chSysCardServiceTag,
       "chSysCardExpressServiceCode": chSysCardExpressServiceCode,
       "chSysPortTable": chSysPortTable,
       "chSysPortEntry": chSysPortEntry,
       "chSysPortSlotIndex": chSysPortSlotIndex,
       "chSysPortIndex": chSysPortIndex,
       "chSysPortType": chSysPortType,
       "chSysPortAdminStatus": chSysPortAdminStatus,
       "chSysPortOperStatus": chSysPortOperStatus,
       "chSysPortIfIndex": chSysPortIfIndex,
       "chSysXfpRecvPower": chSysXfpRecvPower,
       "chSysProcessorTable": chSysProcessorTable,
       "chSysProcessorEntry": chSysProcessorEntry,
       "chSysProcessorSlotIndex": chSysProcessorSlotIndex,
       "chSysProcessorIndex": chSysProcessorIndex,
       "chSysProcessorModule": chSysProcessorModule,
       "chSysProcessorUpTime": chSysProcessorUpTime,
       "chSysProcessorNvramSize": chSysProcessorNvramSize,
       "chSysProcessorMemSize": chSysProcessorMemSize,
       "chSysSwModuleTable": chSysSwModuleTable,
       "chSysSwModuleEntry": chSysSwModuleEntry,
       "chSysSwSlotIndex": chSysSwSlotIndex,
       "chSysSwProcessorIndex": chSysSwProcessorIndex,
       "chSysSwRuntimeImgVersion": chSysSwRuntimeImgVersion,
       "chSysSwRuntimeImgDate": chSysSwRuntimeImgDate,
       "chSysSwCurrentBootImgVersion": chSysSwCurrentBootImgVersion,
       "chSysSwCurrentBootImgDate": chSysSwCurrentBootImgDate,
       "chSysSwCurrentBootImgStatus": chSysSwCurrentBootImgStatus,
       "chSysSwBackupBootImgVersion": chSysSwBackupBootImgVersion,
       "chSysSwBackupBootImgDate": chSysSwBackupBootImgDate,
       "chSysSwBackupBootImgStatus": chSysSwBackupBootImgStatus,
       "chSysSwNextRebootImage": chSysSwNextRebootImage,
       "chSysSwCurrentBootImage": chSysSwCurrentBootImage,
       "chSysPowerSupplyTable": chSysPowerSupplyTable,
       "chSysPowerSupplyEntry": chSysPowerSupplyEntry,
       "chSysPowerSupplyIndex": chSysPowerSupplyIndex,
       "chSysPowerSupplyOperStatus": chSysPowerSupplyOperStatus,
       "chSysPowerSupplyType": chSysPowerSupplyType,
       "chSysPowerSupplyVersion": chSysPowerSupplyVersion,
       "chSysPowerSupplyMode": chSysPowerSupplyMode,
       "chSysFanTrayTable": chSysFanTrayTable,
       "chSysFanTrayEntry": chSysFanTrayEntry,
       "chSysFanTrayIndex": chSysFanTrayIndex,
       "chSysFanTrayOperStatus": chSysFanTrayOperStatus,
       "chSysSfmTable": chSysSfmTable,
       "chSysSfmEntry": chSysSfmEntry,
       "chSysSfmIndex": chSysSfmIndex,
       "chSysSfmAdminStatus": chSysSfmAdminStatus,
       "chSysSfmOperStatus": chSysSfmOperStatus,
       "chSysSfmErrorStatus": chSysSfmErrorStatus,
       "chRpmObjects": chRpmObjects,
       "chRpmNumRpms": chRpmNumRpms,
       "chRpmSlotNumber": chRpmSlotNumber,
       "chRpmUptime": chRpmUptime,
       "chRpmLastSwitchDate": chRpmLastSwitchDate,
       "chRpmMajorAlarmStatus": chRpmMajorAlarmStatus,
       "chRpmMinorAlarmStatus": chRpmMinorAlarmStatus,
       "chRpmUtilTable": chRpmUtilTable,
       "chRpmUtilEntry": chRpmUtilEntry,
       "chRpmCpuIndex": chRpmCpuIndex,
       "chRpmCpuType": chRpmCpuType,
       "chRpmCpuUtil5Sec": chRpmCpuUtil5Sec,
       "chRpmCpuUtil1Min": chRpmCpuUtil1Min,
       "chRpmCpuUtil5Min": chRpmCpuUtil5Min,
       "chRpmMemUsageUtil": chRpmMemUsageUtil,
       "chAlarmObjects": chAlarmObjects,
       "chLineCardObjects": chLineCardObjects,
       "chLineCardUtilTable": chLineCardUtilTable,
       "chLineCardUtilEntry": chLineCardUtilEntry,
       "chLineCardCpuUtil5Sec": chLineCardCpuUtil5Sec,
       "chLineCardCpuUtil1Min": chLineCardCpuUtil1Min,
       "chLineCardCpuUtil5Min": chLineCardCpuUtil5Min,
       "chLineCardMemUsageUtil": chLineCardMemUsageUtil,
       "f10CSerChassisMibConformance": f10CSerChassisMibConformance,
       "f10CSerChassisMibCompliances": f10CSerChassisMibCompliances,
       "f10CSerChassisMibCompliance": f10CSerChassisMibCompliance,
       "f10CSerChassisMibGroups": f10CSerChassisMibGroups,
       "f10CSerComponentGroup": f10CSerComponentGroup,
       "f10CSerSystemGroup": f10CSerSystemGroup,
       "f10CSerRpmGroup": f10CSerRpmGroup,
       "f10CSerLineCardGroup": f10CSerLineCardGroup}
)
