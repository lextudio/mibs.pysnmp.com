# SNMP MIB module (F10-CHASSIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/F10-CHASSIS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:43:20 2024
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

(F10CardOperStatus,
 F10ChassisMode,
 F10ChassisType,
 F10HundredthdB,
 F10MfgDate,
 F10ProcessorModuleType,
 F10SlotState,
 F10SwDate,
 F10SystemCardType,
 F10SystemPortType) = mibBuilder.importSymbols(
    "FORCE10-TC",
    "F10CardOperStatus",
    "F10ChassisMode",
    "F10ChassisType",
    "F10HundredthdB",
    "F10MfgDate",
    "F10ProcessorModuleType",
    "F10SlotState",
    "F10SwDate",
    "F10SystemCardType",
    "F10SystemPortType")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

f10ChassisMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1)
)
f10ChassisMib.setRevisions(
        ("2013-01-09 12:00",
         "2008-09-02 12:00",
         "2008-04-30 12:00",
         "2008-04-16 12:00",
         "2008-02-29 12:00",
         "2007-06-28 12:00",
         "2007-05-22 12:00",
         "1906-05-22 00:00",
         "1901-01-02 00:00",
         "1903-10-02 00:00",
         "1903-10-02 00:00",
         "1903-07-30 00:00",
         "1903-07-20 00:00",
         "1902-06-01 00:00",
         "1902-04-01 00:00",
         "1902-12-25 00:00",
         "1902-08-08 00:00",
         "1902-06-16 00:00",
         "1902-05-12 00:00",
         "1902-05-01 00:00",
         "1902-04-15 00:00",
         "1901-11-07 00:00",
         "1901-03-26 00:00",
         "1900-11-21 00:00",
         "1900-10-20 00:00",
         "1900-10-28 00:00",
         "1900-10-18 00:00",
         "1900-10-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_F10ChassisMibObject_ObjectIdentity = ObjectIdentity
f10ChassisMibObject = _F10ChassisMibObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1)
)
_ChObjects_ObjectIdentity = ObjectIdentity
chObjects = _ChObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 1)
)
_ChType_Type = F10ChassisType
_ChType_Object = MibScalar
chType = _ChType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 1, 1),
    _ChType_Type()
)
chType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chType.setStatus("current")
_ChSerialNumber_Type = DisplayString
_ChSerialNumber_Object = MibScalar
chSerialNumber = _ChSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 1, 2),
    _ChSerialNumber_Type()
)
chSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSerialNumber.setStatus("current")
_ChVendorId_Type = DisplayString
_ChVendorId_Object = MibScalar
chVendorId = _ChVendorId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 1, 3),
    _ChVendorId_Type()
)
chVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chVendorId.setStatus("current")
_ChMfgDate_Type = F10MfgDate
_ChMfgDate_Object = MibScalar
chMfgDate = _ChMfgDate_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 1, 4),
    _ChMfgDate_Type()
)
chMfgDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chMfgDate.setStatus("current")
_ChEcLevel_Type = Integer32
_ChEcLevel_Object = MibScalar
chEcLevel = _ChEcLevel_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 1, 5),
    _ChEcLevel_Type()
)
chEcLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chEcLevel.setStatus("deprecated")
_ChNumFanTrays_Type = Integer32
_ChNumFanTrays_Object = MibScalar
chNumFanTrays = _ChNumFanTrays_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 1, 6),
    _ChNumFanTrays_Type()
)
chNumFanTrays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chNumFanTrays.setStatus("current")
_ChNumPowerSupplies_Type = Integer32
_ChNumPowerSupplies_Object = MibScalar
chNumPowerSupplies = _ChNumPowerSupplies_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 1, 7),
    _ChNumPowerSupplies_Type()
)
chNumPowerSupplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chNumPowerSupplies.setStatus("current")
_ChNumSlots_Type = Integer32
_ChNumSlots_Object = MibScalar
chNumSlots = _ChNumSlots_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 1, 8),
    _ChNumSlots_Type()
)
chNumSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chNumSlots.setStatus("current")
_ChNumSfmSlots_Type = Integer32
_ChNumSfmSlots_Object = MibScalar
chNumSfmSlots = _ChNumSfmSlots_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 1, 9),
    _ChNumSfmSlots_Type()
)
chNumSfmSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chNumSfmSlots.setStatus("current")
_ChNumAirFilters_Type = Integer32
_ChNumAirFilters_Object = MibScalar
chNumAirFilters = _ChNumAirFilters_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 1, 10),
    _ChNumAirFilters_Type()
)
chNumAirFilters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chNumAirFilters.setStatus("deprecated")
_ChSlot1to16_Type = F10SlotState
_ChSlot1to16_Object = MibScalar
chSlot1to16 = _ChSlot1to16_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 1, 11),
    _ChSlot1to16_Type()
)
chSlot1to16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSlot1to16.setStatus("current")


class _ChCountryCode_Type(OctetString):
    """Custom type chCountryCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_ChCountryCode_Type.__name__ = "OctetString"
_ChCountryCode_Object = MibScalar
chCountryCode = _ChCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 1, 12),
    _ChCountryCode_Type()
)
chCountryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chCountryCode.setStatus("current")
_ChPartNum_Type = DisplayString
_ChPartNum_Object = MibScalar
chPartNum = _ChPartNum_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 1, 13),
    _ChPartNum_Type()
)
chPartNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chPartNum.setStatus("current")
_ChProductRev_Type = DisplayString
_ChProductRev_Object = MibScalar
chProductRev = _ChProductRev_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 1, 14),
    _ChProductRev_Type()
)
chProductRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chProductRev.setStatus("current")
_ChProductOrder_Type = DisplayString
_ChProductOrder_Object = MibScalar
chProductOrder = _ChProductOrder_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 1, 15),
    _ChProductOrder_Type()
)
chProductOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chProductOrder.setStatus("current")
_ChChassisMode_Type = F10ChassisMode
_ChChassisMode_Object = MibScalar
chChassisMode = _ChChassisMode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 1, 16),
    _ChChassisMode_Type()
)
chChassisMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chChassisMode.setStatus("current")
_ChSysObjects_ObjectIdentity = ObjectIdentity
chSysObjects = _ChSysObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2)
)
_ChSysPowerSupplyTable_Object = MibTable
chSysPowerSupplyTable = _ChSysPowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    chSysPowerSupplyTable.setStatus("current")
_ChSysPowerSupplyEntry_Object = MibTableRow
chSysPowerSupplyEntry = _ChSysPowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 1, 1)
)
chSysPowerSupplyEntry.setIndexNames(
    (0, "F10-CHASSIS-MIB", "chSysPowerSupplyIndex"),
)
if mibBuilder.loadTexts:
    chSysPowerSupplyEntry.setStatus("current")
_ChSysPowerSupplyIndex_Type = Integer32
_ChSysPowerSupplyIndex_Object = MibTableColumn
chSysPowerSupplyIndex = _ChSysPowerSupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 1, 1, 2),
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
              2)
        )
    )
    namedValues = NamedValues(
        *(("ac", 1),
          ("dc", 2))
    )


_ChSysPowerSupplyType_Type.__name__ = "Integer32"
_ChSysPowerSupplyType_Object = MibTableColumn
chSysPowerSupplyType = _ChSysPowerSupplyType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 1, 1, 3),
    _ChSysPowerSupplyType_Type()
)
chSysPowerSupplyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysPowerSupplyType.setStatus("current")
_ChSysFanTrayTable_Object = MibTable
chSysFanTrayTable = _ChSysFanTrayTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    chSysFanTrayTable.setStatus("current")
_ChSysFanTrayEntry_Object = MibTableRow
chSysFanTrayEntry = _ChSysFanTrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 2, 1)
)
chSysFanTrayEntry.setIndexNames(
    (0, "F10-CHASSIS-MIB", "chSysFanTrayIndex"),
)
if mibBuilder.loadTexts:
    chSysFanTrayEntry.setStatus("current")
_ChSysFanTrayIndex_Type = Integer32
_ChSysFanTrayIndex_Object = MibTableColumn
chSysFanTrayIndex = _ChSysFanTrayIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 2, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 2, 1, 2),
    _ChSysFanTrayOperStatus_Type()
)
chSysFanTrayOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysFanTrayOperStatus.setStatus("current")
_ChSysCardTable_Object = MibTable
chSysCardTable = _ChSysCardTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    chSysCardTable.setStatus("current")
_ChSysCardEntry_Object = MibTableRow
chSysCardEntry = _ChSysCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 3, 1)
)
chSysCardEntry.setIndexNames(
    (0, "F10-CHASSIS-MIB", "chSysCardSlotIndex"),
)
if mibBuilder.loadTexts:
    chSysCardEntry.setStatus("current")
_ChSysCardSlotIndex_Type = Integer32
_ChSysCardSlotIndex_Object = MibTableColumn
chSysCardSlotIndex = _ChSysCardSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 3, 1, 1),
    _ChSysCardSlotIndex_Type()
)
chSysCardSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysCardSlotIndex.setStatus("current")
_ChSysCardType_Type = F10SystemCardType
_ChSysCardType_Object = MibTableColumn
chSysCardType = _ChSysCardType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 3, 1, 2),
    _ChSysCardType_Type()
)
chSysCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysCardType.setStatus("current")
_ChSysCardNumber_Type = Integer32
_ChSysCardNumber_Object = MibTableColumn
chSysCardNumber = _ChSysCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 3, 1, 3),
    _ChSysCardNumber_Type()
)
chSysCardNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysCardNumber.setStatus("current")
_ChSysCardSerialNumber_Type = DisplayString
_ChSysCardSerialNumber_Object = MibTableColumn
chSysCardSerialNumber = _ChSysCardSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 3, 1, 4),
    _ChSysCardSerialNumber_Type()
)
chSysCardSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysCardSerialNumber.setStatus("current")
_ChSysCardVendorId_Type = DisplayString
_ChSysCardVendorId_Object = MibTableColumn
chSysCardVendorId = _ChSysCardVendorId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 3, 1, 5),
    _ChSysCardVendorId_Type()
)
chSysCardVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysCardVendorId.setStatus("current")
_ChSysCardMfgDate_Type = F10MfgDate
_ChSysCardMfgDate_Object = MibTableColumn
chSysCardMfgDate = _ChSysCardMfgDate_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 3, 1, 6),
    _ChSysCardMfgDate_Type()
)
chSysCardMfgDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysCardMfgDate.setStatus("current")
_ChSysCardEcLevel_Type = Integer32
_ChSysCardEcLevel_Object = MibTableColumn
chSysCardEcLevel = _ChSysCardEcLevel_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 3, 1, 7),
    _ChSysCardEcLevel_Type()
)
chSysCardEcLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysCardEcLevel.setStatus("deprecated")
_ChSysCardUpperTemp_Type = Gauge32
_ChSysCardUpperTemp_Object = MibTableColumn
chSysCardUpperTemp = _ChSysCardUpperTemp_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 3, 1, 8),
    _ChSysCardUpperTemp_Type()
)
chSysCardUpperTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysCardUpperTemp.setStatus("current")
_ChSysCardLowerTemp_Type = Gauge32
_ChSysCardLowerTemp_Object = MibTableColumn
chSysCardLowerTemp = _ChSysCardLowerTemp_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 3, 1, 9),
    _ChSysCardLowerTemp_Type()
)
chSysCardLowerTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysCardLowerTemp.setStatus("current")
_ChSysCardNumProcessors_Type = Integer32
_ChSysCardNumProcessors_Object = MibTableColumn
chSysCardNumProcessors = _ChSysCardNumProcessors_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 3, 1, 10),
    _ChSysCardNumProcessors_Type()
)
chSysCardNumProcessors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysCardNumProcessors.setStatus("current")
_ChSysCardNumPhyPorts_Type = Integer32
_ChSysCardNumPhyPorts_Object = MibTableColumn
chSysCardNumPhyPorts = _ChSysCardNumPhyPorts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 3, 1, 11),
    _ChSysCardNumPhyPorts_Type()
)
chSysCardNumPhyPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysCardNumPhyPorts.setStatus("current")
_ChSysCardNumLgcPorts_Type = Integer32
_ChSysCardNumLgcPorts_Object = MibTableColumn
chSysCardNumLgcPorts = _ChSysCardNumLgcPorts_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 3, 1, 12),
    _ChSysCardNumLgcPorts_Type()
)
chSysCardNumLgcPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysCardNumLgcPorts.setStatus("current")
_ChSysCardUpTime_Type = TimeTicks
_ChSysCardUpTime_Object = MibTableColumn
chSysCardUpTime = _ChSysCardUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 3, 1, 13),
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
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 3, 1, 14),
    _ChSysCardAdminStatus_Type()
)
chSysCardAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysCardAdminStatus.setStatus("current")
_ChSysCardOperStatus_Type = F10CardOperStatus
_ChSysCardOperStatus_Object = MibTableColumn
chSysCardOperStatus = _ChSysCardOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 3, 1, 15),
    _ChSysCardOperStatus_Type()
)
chSysCardOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysCardOperStatus.setStatus("current")


class _ChSysCardFaultStatus_Type(Integer32):
    """Custom type chSysCardFaultStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_ChSysCardFaultStatus_Type.__name__ = "Integer32"
_ChSysCardFaultStatus_Object = MibTableColumn
chSysCardFaultStatus = _ChSysCardFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 3, 1, 16),
    _ChSysCardFaultStatus_Type()
)
chSysCardFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysCardFaultStatus.setStatus("current")
_ChSysCardLogStream_Type = OctetString
_ChSysCardLogStream_Object = MibTableColumn
chSysCardLogStream = _ChSysCardLogStream_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 3, 1, 17),
    _ChSysCardLogStream_Type()
)
chSysCardLogStream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysCardLogStream.setStatus("current")


class _ChSysCardCountryCode_Type(OctetString):
    """Custom type chSysCardCountryCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_ChSysCardCountryCode_Type.__name__ = "OctetString"
_ChSysCardCountryCode_Object = MibTableColumn
chSysCardCountryCode = _ChSysCardCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 3, 1, 18),
    _ChSysCardCountryCode_Type()
)
chSysCardCountryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysCardCountryCode.setStatus("current")
_ChSysCardPartNum_Type = DisplayString
_ChSysCardPartNum_Object = MibTableColumn
chSysCardPartNum = _ChSysCardPartNum_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 3, 1, 19),
    _ChSysCardPartNum_Type()
)
chSysCardPartNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysCardPartNum.setStatus("current")
_ChSysCardProductRev_Type = DisplayString
_ChSysCardProductRev_Object = MibTableColumn
chSysCardProductRev = _ChSysCardProductRev_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 3, 1, 20),
    _ChSysCardProductRev_Type()
)
chSysCardProductRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysCardProductRev.setStatus("current")
_ChSysCardProdOrder_Type = DisplayString
_ChSysCardProdOrder_Object = MibTableColumn
chSysCardProdOrder = _ChSysCardProdOrder_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 3, 1, 21),
    _ChSysCardProdOrder_Type()
)
chSysCardProdOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysCardProdOrder.setStatus("current")
_ChSysCardParityPhantomError_Type = Gauge32
_ChSysCardParityPhantomError_Object = MibTableColumn
chSysCardParityPhantomError = _ChSysCardParityPhantomError_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 3, 1, 22),
    _ChSysCardParityPhantomError_Type()
)
chSysCardParityPhantomError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysCardParityPhantomError.setStatus("current")
_ChSysCardParityRecoverableError_Type = Gauge32
_ChSysCardParityRecoverableError_Object = MibTableColumn
chSysCardParityRecoverableError = _ChSysCardParityRecoverableError_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 3, 1, 23),
    _ChSysCardParityRecoverableError_Type()
)
chSysCardParityRecoverableError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysCardParityRecoverableError.setStatus("current")
_ChSysCardParityNonrecovrableError_Type = Gauge32
_ChSysCardParityNonrecovrableError_Object = MibTableColumn
chSysCardParityNonrecovrableError = _ChSysCardParityNonrecovrableError_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 3, 1, 24),
    _ChSysCardParityNonrecovrableError_Type()
)
chSysCardParityNonrecovrableError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysCardParityNonrecovrableError.setStatus("current")
_ChSysPortTable_Object = MibTable
chSysPortTable = _ChSysPortTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 4)
)
if mibBuilder.loadTexts:
    chSysPortTable.setStatus("current")
_ChSysPortEntry_Object = MibTableRow
chSysPortEntry = _ChSysPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 4, 1)
)
chSysPortEntry.setIndexNames(
    (0, "F10-CHASSIS-MIB", "chSysPortSlotIndex"),
    (0, "F10-CHASSIS-MIB", "chSysPortIndex"),
)
if mibBuilder.loadTexts:
    chSysPortEntry.setStatus("current")
_ChSysPortSlotIndex_Type = Integer32
_ChSysPortSlotIndex_Object = MibTableColumn
chSysPortSlotIndex = _ChSysPortSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 4, 1, 1),
    _ChSysPortSlotIndex_Type()
)
chSysPortSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysPortSlotIndex.setStatus("current")
_ChSysPortIndex_Type = Integer32
_ChSysPortIndex_Object = MibTableColumn
chSysPortIndex = _ChSysPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 4, 1, 2),
    _ChSysPortIndex_Type()
)
chSysPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysPortIndex.setStatus("current")
_ChSysPortType_Type = F10SystemPortType
_ChSysPortType_Object = MibTableColumn
chSysPortType = _ChSysPortType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 4, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 4, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 4, 1, 5),
    _ChSysPortOperStatus_Type()
)
chSysPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysPortOperStatus.setStatus("current")
_ChSysPortIfIndex_Type = Integer32
_ChSysPortIfIndex_Object = MibTableColumn
chSysPortIfIndex = _ChSysPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 4, 1, 6),
    _ChSysPortIfIndex_Type()
)
chSysPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysPortIfIndex.setStatus("current")
_ChSysXfpRecvPower_Type = F10HundredthdB
_ChSysXfpRecvPower_Object = MibTableColumn
chSysXfpRecvPower = _ChSysXfpRecvPower_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 4, 1, 7),
    _ChSysXfpRecvPower_Type()
)
chSysXfpRecvPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysXfpRecvPower.setStatus("current")
if mibBuilder.loadTexts:
    chSysXfpRecvPower.setUnits("dB")
_ChSysProcessorTable_Object = MibTable
chSysProcessorTable = _ChSysProcessorTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 6)
)
if mibBuilder.loadTexts:
    chSysProcessorTable.setStatus("current")
_ChSysProcessorEntry_Object = MibTableRow
chSysProcessorEntry = _ChSysProcessorEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 6, 1)
)
chSysProcessorEntry.setIndexNames(
    (0, "F10-CHASSIS-MIB", "chSysProcessorSlotIndex"),
    (0, "F10-CHASSIS-MIB", "chSysProcessorIndex"),
)
if mibBuilder.loadTexts:
    chSysProcessorEntry.setStatus("current")
_ChSysProcessorSlotIndex_Type = Integer32
_ChSysProcessorSlotIndex_Object = MibTableColumn
chSysProcessorSlotIndex = _ChSysProcessorSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 6, 1, 1),
    _ChSysProcessorSlotIndex_Type()
)
chSysProcessorSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysProcessorSlotIndex.setStatus("current")
_ChSysProcessorIndex_Type = Integer32
_ChSysProcessorIndex_Object = MibTableColumn
chSysProcessorIndex = _ChSysProcessorIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 6, 1, 2),
    _ChSysProcessorIndex_Type()
)
chSysProcessorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysProcessorIndex.setStatus("current")
_ChSysProcessorModule_Type = F10ProcessorModuleType
_ChSysProcessorModule_Object = MibTableColumn
chSysProcessorModule = _ChSysProcessorModule_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 6, 1, 3),
    _ChSysProcessorModule_Type()
)
chSysProcessorModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysProcessorModule.setStatus("current")
_ChSysProcessorUpTime_Type = TimeTicks
_ChSysProcessorUpTime_Object = MibTableColumn
chSysProcessorUpTime = _ChSysProcessorUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 6, 1, 4),
    _ChSysProcessorUpTime_Type()
)
chSysProcessorUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysProcessorUpTime.setStatus("current")
_ChSysProcessorNvramSize_Type = Integer32
_ChSysProcessorNvramSize_Object = MibTableColumn
chSysProcessorNvramSize = _ChSysProcessorNvramSize_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 6, 1, 5),
    _ChSysProcessorNvramSize_Type()
)
chSysProcessorNvramSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysProcessorNvramSize.setStatus("current")
_ChSysProcessorMemSize_Type = Integer32
_ChSysProcessorMemSize_Object = MibTableColumn
chSysProcessorMemSize = _ChSysProcessorMemSize_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 6, 1, 6),
    _ChSysProcessorMemSize_Type()
)
chSysProcessorMemSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysProcessorMemSize.setStatus("current")
_ChSysProcessorLogStream_Type = OctetString
_ChSysProcessorLogStream_Object = MibTableColumn
chSysProcessorLogStream = _ChSysProcessorLogStream_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 6, 1, 7),
    _ChSysProcessorLogStream_Type()
)
chSysProcessorLogStream.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysProcessorLogStream.setStatus("current")
_ChSysSwModuleTable_Object = MibTable
chSysSwModuleTable = _ChSysSwModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 7)
)
if mibBuilder.loadTexts:
    chSysSwModuleTable.setStatus("current")
_ChSysSwModuleEntry_Object = MibTableRow
chSysSwModuleEntry = _ChSysSwModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 7, 1)
)
chSysSwModuleEntry.setIndexNames(
    (0, "F10-CHASSIS-MIB", "chSysSwSlotIndex"),
    (0, "F10-CHASSIS-MIB", "chSysSwProcessorIndex"),
)
if mibBuilder.loadTexts:
    chSysSwModuleEntry.setStatus("current")
_ChSysSwSlotIndex_Type = Integer32
_ChSysSwSlotIndex_Object = MibTableColumn
chSysSwSlotIndex = _ChSysSwSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 7, 1, 1),
    _ChSysSwSlotIndex_Type()
)
chSysSwSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysSwSlotIndex.setStatus("current")
_ChSysSwProcessorIndex_Type = Integer32
_ChSysSwProcessorIndex_Object = MibTableColumn
chSysSwProcessorIndex = _ChSysSwProcessorIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 7, 1, 2),
    _ChSysSwProcessorIndex_Type()
)
chSysSwProcessorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysSwProcessorIndex.setStatus("current")
_ChSysSwRuntimeImgVersion_Type = DisplayString
_ChSysSwRuntimeImgVersion_Object = MibTableColumn
chSysSwRuntimeImgVersion = _ChSysSwRuntimeImgVersion_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 7, 1, 3),
    _ChSysSwRuntimeImgVersion_Type()
)
chSysSwRuntimeImgVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysSwRuntimeImgVersion.setStatus("current")
_ChSysSwRuntimeImgDate_Type = F10SwDate
_ChSysSwRuntimeImgDate_Object = MibTableColumn
chSysSwRuntimeImgDate = _ChSysSwRuntimeImgDate_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 7, 1, 4),
    _ChSysSwRuntimeImgDate_Type()
)
chSysSwRuntimeImgDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysSwRuntimeImgDate.setStatus("current")
_ChSysSwCurrentBootImgVersion_Type = DisplayString
_ChSysSwCurrentBootImgVersion_Object = MibTableColumn
chSysSwCurrentBootImgVersion = _ChSysSwCurrentBootImgVersion_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 7, 1, 5),
    _ChSysSwCurrentBootImgVersion_Type()
)
chSysSwCurrentBootImgVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysSwCurrentBootImgVersion.setStatus("current")
_ChSysSwCurrentBootImgDate_Type = DateAndTime
_ChSysSwCurrentBootImgDate_Object = MibTableColumn
chSysSwCurrentBootImgDate = _ChSysSwCurrentBootImgDate_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 7, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 7, 1, 7),
    _ChSysSwCurrentBootImgStatus_Type()
)
chSysSwCurrentBootImgStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysSwCurrentBootImgStatus.setStatus("current")
_ChSysSwBackupBootImgVersion_Type = DisplayString
_ChSysSwBackupBootImgVersion_Object = MibTableColumn
chSysSwBackupBootImgVersion = _ChSysSwBackupBootImgVersion_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 7, 1, 8),
    _ChSysSwBackupBootImgVersion_Type()
)
chSysSwBackupBootImgVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysSwBackupBootImgVersion.setStatus("current")
_ChSysSwBackupBootImgDate_Type = DateAndTime
_ChSysSwBackupBootImgDate_Object = MibTableColumn
chSysSwBackupBootImgDate = _ChSysSwBackupBootImgDate_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 7, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 7, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 7, 1, 11),
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
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 7, 1, 12),
    _ChSysSwCurrentBootImage_Type()
)
chSysSwCurrentBootImage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysSwCurrentBootImage.setStatus("current")
_ChSysSfmTable_Object = MibTable
chSysSfmTable = _ChSysSfmTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 8)
)
if mibBuilder.loadTexts:
    chSysSfmTable.setStatus("current")
_ChSysSfmEntry_Object = MibTableRow
chSysSfmEntry = _ChSysSfmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 8, 1)
)
chSysSfmEntry.setIndexNames(
    (0, "F10-CHASSIS-MIB", "chSysSfmIndex"),
)
if mibBuilder.loadTexts:
    chSysSfmEntry.setStatus("current")
_ChSysSfmIndex_Type = Integer32
_ChSysSfmIndex_Object = MibTableColumn
chSysSfmIndex = _ChSysSfmIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 8, 1, 1),
    _ChSysSfmIndex_Type()
)
chSysSfmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysSfmIndex.setStatus("current")
_ChSysSfmSerialNumber_Type = DisplayString
_ChSysSfmSerialNumber_Object = MibTableColumn
chSysSfmSerialNumber = _ChSysSfmSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 8, 1, 2),
    _ChSysSfmSerialNumber_Type()
)
chSysSfmSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysSfmSerialNumber.setStatus("current")
_ChSysSfmVendorId_Type = DisplayString
_ChSysSfmVendorId_Object = MibTableColumn
chSysSfmVendorId = _ChSysSfmVendorId_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 8, 1, 3),
    _ChSysSfmVendorId_Type()
)
chSysSfmVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysSfmVendorId.setStatus("current")
_ChSysSfmMfgDate_Type = F10MfgDate
_ChSysSfmMfgDate_Object = MibTableColumn
chSysSfmMfgDate = _ChSysSfmMfgDate_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 8, 1, 4),
    _ChSysSfmMfgDate_Type()
)
chSysSfmMfgDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysSfmMfgDate.setStatus("current")
_ChSysSfmEcLevel_Type = Integer32
_ChSysSfmEcLevel_Object = MibTableColumn
chSysSfmEcLevel = _ChSysSfmEcLevel_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 8, 1, 5),
    _ChSysSfmEcLevel_Type()
)
chSysSfmEcLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysSfmEcLevel.setStatus("deprecated")


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
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 8, 1, 6),
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
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("absent", 2),
          ("active", 1),
          ("incomp", 4),
          ("standby", 3))
    )


_ChSysSfmOperStatus_Type.__name__ = "Integer32"
_ChSysSfmOperStatus_Object = MibTableColumn
chSysSfmOperStatus = _ChSysSfmOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 8, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 8, 1, 8),
    _ChSysSfmErrorStatus_Type()
)
chSysSfmErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysSfmErrorStatus.setStatus("current")


class _ChSysSfmCountryCode_Type(OctetString):
    """Custom type chSysSfmCountryCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_ChSysSfmCountryCode_Type.__name__ = "OctetString"
_ChSysSfmCountryCode_Object = MibTableColumn
chSysSfmCountryCode = _ChSysSfmCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 8, 1, 9),
    _ChSysSfmCountryCode_Type()
)
chSysSfmCountryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysSfmCountryCode.setStatus("current")
_ChSysSfmPartNum_Type = DisplayString
_ChSysSfmPartNum_Object = MibTableColumn
chSysSfmPartNum = _ChSysSfmPartNum_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 8, 1, 10),
    _ChSysSfmPartNum_Type()
)
chSysSfmPartNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysSfmPartNum.setStatus("current")
_ChSysSfmProductRev_Type = DisplayString
_ChSysSfmProductRev_Object = MibTableColumn
chSysSfmProductRev = _ChSysSfmProductRev_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 8, 1, 11),
    _ChSysSfmProductRev_Type()
)
chSysSfmProductRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysSfmProductRev.setStatus("current")
_ChSysSfmProdOrder_Type = DisplayString
_ChSysSfmProdOrder_Object = MibTableColumn
chSysSfmProdOrder = _ChSysSfmProdOrder_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 8, 1, 12),
    _ChSysSfmProdOrder_Type()
)
chSysSfmProdOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSysSfmProdOrder.setStatus("current")
_ChSysSfmGroup_ObjectIdentity = ObjectIdentity
chSysSfmGroup = _ChSysSfmGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 9)
)


class _ChSfmUtil5Sec_Type(Gauge32):
    """Custom type chSfmUtil5Sec based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ChSfmUtil5Sec_Type.__name__ = "Gauge32"
_ChSfmUtil5Sec_Object = MibScalar
chSfmUtil5Sec = _ChSfmUtil5Sec_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 9, 1),
    _ChSfmUtil5Sec_Type()
)
chSfmUtil5Sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSfmUtil5Sec.setStatus("current")
if mibBuilder.loadTexts:
    chSfmUtil5Sec.setUnits("percent")


class _ChSfmUtil1Min_Type(Gauge32):
    """Custom type chSfmUtil1Min based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ChSfmUtil1Min_Type.__name__ = "Gauge32"
_ChSfmUtil1Min_Object = MibScalar
chSfmUtil1Min = _ChSfmUtil1Min_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 9, 2),
    _ChSfmUtil1Min_Type()
)
chSfmUtil1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSfmUtil1Min.setStatus("current")
if mibBuilder.loadTexts:
    chSfmUtil1Min.setUnits("percent")


class _ChSfmUtil5Min_Type(Gauge32):
    """Custom type chSfmUtil5Min based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ChSfmUtil5Min_Type.__name__ = "Gauge32"
_ChSfmUtil5Min_Object = MibScalar
chSfmUtil5Min = _ChSfmUtil5Min_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 2, 9, 3),
    _ChSfmUtil5Min_Type()
)
chSfmUtil5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chSfmUtil5Min.setStatus("current")
if mibBuilder.loadTexts:
    chSfmUtil5Min.setUnits("percent")
_ChRpmObjects_ObjectIdentity = ObjectIdentity
chRpmObjects = _ChRpmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 3)
)
_ChRpmNumRpms_Type = Integer32
_ChRpmNumRpms_Object = MibScalar
chRpmNumRpms = _ChRpmNumRpms_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 3, 1),
    _ChRpmNumRpms_Type()
)
chRpmNumRpms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chRpmNumRpms.setStatus("current")
_ChRpmSlotNumber_Type = Integer32
_ChRpmSlotNumber_Object = MibScalar
chRpmSlotNumber = _ChRpmSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 3, 2),
    _ChRpmSlotNumber_Type()
)
chRpmSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chRpmSlotNumber.setStatus("current")
_ChRpmUptime_Type = TimeTicks
_ChRpmUptime_Object = MibScalar
chRpmUptime = _ChRpmUptime_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 3, 3),
    _ChRpmUptime_Type()
)
chRpmUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chRpmUptime.setStatus("current")
_ChRpmLastSwitchDate_Type = DateAndTime
_ChRpmLastSwitchDate_Object = MibScalar
chRpmLastSwitchDate = _ChRpmLastSwitchDate_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 3, 4),
    _ChRpmLastSwitchDate_Type()
)
chRpmLastSwitchDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chRpmLastSwitchDate.setStatus("current")


class _ChRpmCOAlarmStatus_Type(Integer32):
    """Custom type chRpmCOAlarmStatus based on Integer32"""
    defaultValue = 1

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


_ChRpmCOAlarmStatus_Type.__name__ = "Integer32"
_ChRpmCOAlarmStatus_Object = MibScalar
chRpmCOAlarmStatus = _ChRpmCOAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 3, 5),
    _ChRpmCOAlarmStatus_Type()
)
chRpmCOAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chRpmCOAlarmStatus.setStatus("current")


class _ChRpmFlashStatus_Type(Integer32):
    """Custom type chRpmFlashStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("absent", 1),
          ("present", 2))
    )


_ChRpmFlashStatus_Type.__name__ = "Integer32"
_ChRpmFlashStatus_Object = MibScalar
chRpmFlashStatus = _ChRpmFlashStatus_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 3, 6),
    _ChRpmFlashStatus_Type()
)
chRpmFlashStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chRpmFlashStatus.setStatus("current")
_ChRpmUtilTable_Object = MibTable
chRpmUtilTable = _ChRpmUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 3, 7)
)
if mibBuilder.loadTexts:
    chRpmUtilTable.setStatus("current")
_ChRpmUtilEntry_Object = MibTableRow
chRpmUtilEntry = _ChRpmUtilEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 3, 7, 1)
)
chRpmUtilEntry.setIndexNames(
    (0, "F10-CHASSIS-MIB", "chRpmCpuIndex"),
)
if mibBuilder.loadTexts:
    chRpmUtilEntry.setStatus("current")
_ChRpmCpuIndex_Type = Integer32
_ChRpmCpuIndex_Object = MibTableColumn
chRpmCpuIndex = _ChRpmCpuIndex_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 3, 7, 1, 1),
    _ChRpmCpuIndex_Type()
)
chRpmCpuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chRpmCpuIndex.setStatus("current")
_ChRpmCpuType_Type = F10ProcessorModuleType
_ChRpmCpuType_Object = MibTableColumn
chRpmCpuType = _ChRpmCpuType_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 3, 7, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 3, 7, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 3, 7, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 3, 7, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 3, 7, 1, 6),
    _ChRpmMemUsageUtil_Type()
)
chRpmMemUsageUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chRpmMemUsageUtil.setStatus("current")
if mibBuilder.loadTexts:
    chRpmMemUsageUtil.setUnits("percent")


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
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 3, 8),
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
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 3, 9),
    _ChRpmMinorAlarmStatus_Type()
)
chRpmMinorAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chRpmMinorAlarmStatus.setStatus("current")
_ChAlarmObjects_ObjectIdentity = ObjectIdentity
chAlarmObjects = _ChAlarmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 4)
)
_ChAlarmMibNotifications_ObjectIdentity = ObjectIdentity
chAlarmMibNotifications = _ChAlarmMibNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 4, 0)
)
_ChAlarmVariable_ObjectIdentity = ObjectIdentity
chAlarmVariable = _ChAlarmVariable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 4, 1)
)
_ChAlarmVarInteger_Type = Integer32
_ChAlarmVarInteger_Object = MibScalar
chAlarmVarInteger = _ChAlarmVarInteger_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 4, 1, 1),
    _ChAlarmVarInteger_Type()
)
chAlarmVarInteger.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    chAlarmVarInteger.setStatus("current")
_ChAlarmVarString_Type = OctetString
_ChAlarmVarString_Object = MibScalar
chAlarmVarString = _ChAlarmVarString_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 4, 1, 2),
    _ChAlarmVarString_Type()
)
chAlarmVarString.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    chAlarmVarString.setStatus("current")
_ChAlarmVarSlot_Type = Integer32
_ChAlarmVarSlot_Object = MibScalar
chAlarmVarSlot = _ChAlarmVarSlot_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 4, 1, 3),
    _ChAlarmVarSlot_Type()
)
chAlarmVarSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    chAlarmVarSlot.setStatus("current")
_ChAlarmVarPort_Type = Integer32
_ChAlarmVarPort_Object = MibScalar
chAlarmVarPort = _ChAlarmVarPort_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 4, 1, 4),
    _ChAlarmVarPort_Type()
)
chAlarmVarPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    chAlarmVarPort.setStatus("current")
_ChLineCardObjects_ObjectIdentity = ObjectIdentity
chLineCardObjects = _ChLineCardObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 5)
)
_ChLineCardUtilTable_Object = MibTable
chLineCardUtilTable = _ChLineCardUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    chLineCardUtilTable.setStatus("current")
_ChLineCardUtilEntry_Object = MibTableRow
chLineCardUtilEntry = _ChLineCardUtilEntry_Object(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 5, 1, 1)
)
chLineCardUtilEntry.setIndexNames(
    (0, "F10-CHASSIS-MIB", "chSysCardNumber"),
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
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 5, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 5, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 5, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 5, 1, 1, 4),
    _ChLineCardMemUsageUtil_Type()
)
chLineCardMemUsageUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chLineCardMemUsageUtil.setStatus("current")
if mibBuilder.loadTexts:
    chLineCardMemUsageUtil.setUnits("percent")
_F10ChassisMibConformance_ObjectIdentity = ObjectIdentity
f10ChassisMibConformance = _F10ChassisMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 2)
)
_F10ChassisMibCompliances_ObjectIdentity = ObjectIdentity
f10ChassisMibCompliances = _F10ChassisMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 2, 1)
)
_F10ChassisMibGroups_ObjectIdentity = ObjectIdentity
f10ChassisMibGroups = _F10ChassisMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 2, 2)
)

# Managed Objects groups

f10ComponentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 2, 2, 1)
)
f10ComponentGroup.setObjects(
      *(("F10-CHASSIS-MIB", "chType"),
        ("F10-CHASSIS-MIB", "chSerialNumber"),
        ("F10-CHASSIS-MIB", "chVendorId"),
        ("F10-CHASSIS-MIB", "chMfgDate"),
        ("F10-CHASSIS-MIB", "chEcLevel"),
        ("F10-CHASSIS-MIB", "chNumFanTrays"),
        ("F10-CHASSIS-MIB", "chNumPowerSupplies"),
        ("F10-CHASSIS-MIB", "chNumSlots"),
        ("F10-CHASSIS-MIB", "chNumSfmSlots"),
        ("F10-CHASSIS-MIB", "chSlot1to16"),
        ("F10-CHASSIS-MIB", "chCountryCode"),
        ("F10-CHASSIS-MIB", "chPartNum"),
        ("F10-CHASSIS-MIB", "chProductRev"),
        ("F10-CHASSIS-MIB", "chProductOrder"))
)
if mibBuilder.loadTexts:
    f10ComponentGroup.setStatus("current")

f10SystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 2, 2, 2)
)
f10SystemGroup.setObjects(
      *(("F10-CHASSIS-MIB", "chSysPowerSupplyOperStatus"),
        ("F10-CHASSIS-MIB", "chSysFanTrayOperStatus"),
        ("F10-CHASSIS-MIB", "chSysCardNumber"),
        ("F10-CHASSIS-MIB", "chSysCardType"),
        ("F10-CHASSIS-MIB", "chSysCardSerialNumber"),
        ("F10-CHASSIS-MIB", "chSysCardVendorId"),
        ("F10-CHASSIS-MIB", "chSysCardMfgDate"),
        ("F10-CHASSIS-MIB", "chSysCardEcLevel"),
        ("F10-CHASSIS-MIB", "chSysCardUpperTemp"),
        ("F10-CHASSIS-MIB", "chSysCardLowerTemp"),
        ("F10-CHASSIS-MIB", "chSysCardNumProcessors"),
        ("F10-CHASSIS-MIB", "chSysCardNumPhyPorts"),
        ("F10-CHASSIS-MIB", "chSysCardNumLgcPorts"),
        ("F10-CHASSIS-MIB", "chSysCardUpTime"),
        ("F10-CHASSIS-MIB", "chSysCardAdminStatus"),
        ("F10-CHASSIS-MIB", "chSysCardOperStatus"),
        ("F10-CHASSIS-MIB", "chSysCardFaultStatus"),
        ("F10-CHASSIS-MIB", "chSysCardLogStream"),
        ("F10-CHASSIS-MIB", "chSysCardCountryCode"),
        ("F10-CHASSIS-MIB", "chSysCardPartNum"),
        ("F10-CHASSIS-MIB", "chSysCardProductRev"),
        ("F10-CHASSIS-MIB", "chSysCardProdOrder"),
        ("F10-CHASSIS-MIB", "chSysCardParityPhantomError"),
        ("F10-CHASSIS-MIB", "chSysCardParityRecoverableError"),
        ("F10-CHASSIS-MIB", "chSysCardParityNonrecovrableError"),
        ("F10-CHASSIS-MIB", "chSysProcessorModule"),
        ("F10-CHASSIS-MIB", "chSysProcessorUpTime"),
        ("F10-CHASSIS-MIB", "chSysProcessorNvramSize"),
        ("F10-CHASSIS-MIB", "chSysProcessorMemSize"),
        ("F10-CHASSIS-MIB", "chSysProcessorLogStream"),
        ("F10-CHASSIS-MIB", "chSysPortType"),
        ("F10-CHASSIS-MIB", "chSysPortAdminStatus"),
        ("F10-CHASSIS-MIB", "chSysPortOperStatus"),
        ("F10-CHASSIS-MIB", "chSysPortIfIndex"),
        ("F10-CHASSIS-MIB", "chSysXfpRecvPower"),
        ("F10-CHASSIS-MIB", "chSysSwRuntimeImgVersion"),
        ("F10-CHASSIS-MIB", "chSysSwRuntimeImgDate"),
        ("F10-CHASSIS-MIB", "chSysSwCurrentBootImgVersion"),
        ("F10-CHASSIS-MIB", "chSysSwCurrentBootImgDate"),
        ("F10-CHASSIS-MIB", "chSysSwCurrentBootImgStatus"),
        ("F10-CHASSIS-MIB", "chSysSwBackupBootImgVersion"),
        ("F10-CHASSIS-MIB", "chSysSwBackupBootImgDate"),
        ("F10-CHASSIS-MIB", "chSysSwBackupBootImgStatus"),
        ("F10-CHASSIS-MIB", "chSysSwNextRebootImage"),
        ("F10-CHASSIS-MIB", "chSysSfmSerialNumber"),
        ("F10-CHASSIS-MIB", "chSysSfmVendorId"),
        ("F10-CHASSIS-MIB", "chSysSfmMfgDate"),
        ("F10-CHASSIS-MIB", "chSysSfmEcLevel"),
        ("F10-CHASSIS-MIB", "chSysSfmAdminStatus"),
        ("F10-CHASSIS-MIB", "chSysSfmOperStatus"),
        ("F10-CHASSIS-MIB", "chSysSfmErrorStatus"),
        ("F10-CHASSIS-MIB", "chSysSfmCountryCode"),
        ("F10-CHASSIS-MIB", "chSysSfmPartNum"),
        ("F10-CHASSIS-MIB", "chSysSfmProductRev"),
        ("F10-CHASSIS-MIB", "chSysSfmProdOrder"))
)
if mibBuilder.loadTexts:
    f10SystemGroup.setStatus("current")

f10RpmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 2, 2, 3)
)
f10RpmGroup.setObjects(
      *(("F10-CHASSIS-MIB", "chRpmNumRpms"),
        ("F10-CHASSIS-MIB", "chRpmSlotNumber"),
        ("F10-CHASSIS-MIB", "chRpmUptime"),
        ("F10-CHASSIS-MIB", "chRpmLastSwitchDate"),
        ("F10-CHASSIS-MIB", "chRpmCOAlarmStatus"),
        ("F10-CHASSIS-MIB", "chRpmFlashStatus"),
        ("F10-CHASSIS-MIB", "chRpmCpuType"),
        ("F10-CHASSIS-MIB", "chRpmCpuUtil5Sec"),
        ("F10-CHASSIS-MIB", "chRpmCpuUtil1Min"),
        ("F10-CHASSIS-MIB", "chRpmCpuUtil5Min"),
        ("F10-CHASSIS-MIB", "chRpmMemUsageUtil"))
)
if mibBuilder.loadTexts:
    f10RpmGroup.setStatus("current")

f10LineCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 2, 2, 4)
)
f10LineCardGroup.setObjects(
      *(("F10-CHASSIS-MIB", "chLineCardCpuUtil5Sec"),
        ("F10-CHASSIS-MIB", "chLineCardCpuUtil1Min"),
        ("F10-CHASSIS-MIB", "chLineCardCpuUtil5Min"),
        ("F10-CHASSIS-MIB", "chLineCardMemUsageUtil"))
)
if mibBuilder.loadTexts:
    f10LineCardGroup.setStatus("current")


# Notification objects

chAlarmCardDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 4, 0, 1)
)
chAlarmCardDown.setObjects(
      *(("F10-CHASSIS-MIB", "chAlarmVarInteger"),
        ("F10-CHASSIS-MIB", "chAlarmVarString"),
        ("F10-CHASSIS-MIB", "chAlarmVarSlot"),
        ("F10-CHASSIS-MIB", "chAlarmVarPort"))
)
if mibBuilder.loadTexts:
    chAlarmCardDown.setStatus(
        "current"
    )

chAlarmCardUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 4, 0, 2)
)
chAlarmCardUp.setObjects(
      *(("F10-CHASSIS-MIB", "chAlarmVarInteger"),
        ("F10-CHASSIS-MIB", "chAlarmVarString"),
        ("F10-CHASSIS-MIB", "chAlarmVarSlot"),
        ("F10-CHASSIS-MIB", "chAlarmVarPort"))
)
if mibBuilder.loadTexts:
    chAlarmCardUp.setStatus(
        "current"
    )

chAlarmCardReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 4, 0, 3)
)
chAlarmCardReset.setObjects(
      *(("F10-CHASSIS-MIB", "chAlarmVarInteger"),
        ("F10-CHASSIS-MIB", "chAlarmVarString"),
        ("F10-CHASSIS-MIB", "chAlarmVarSlot"),
        ("F10-CHASSIS-MIB", "chAlarmVarPort"))
)
if mibBuilder.loadTexts:
    chAlarmCardReset.setStatus(
        "current"
    )

chAlarmCardOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 4, 0, 4)
)
chAlarmCardOffline.setObjects(
      *(("F10-CHASSIS-MIB", "chAlarmVarInteger"),
        ("F10-CHASSIS-MIB", "chAlarmVarString"),
        ("F10-CHASSIS-MIB", "chAlarmVarSlot"),
        ("F10-CHASSIS-MIB", "chAlarmVarPort"))
)
if mibBuilder.loadTexts:
    chAlarmCardOffline.setStatus(
        "current"
    )

chAlarmCardMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 4, 0, 5)
)
chAlarmCardMismatch.setObjects(
      *(("F10-CHASSIS-MIB", "chAlarmVarInteger"),
        ("F10-CHASSIS-MIB", "chAlarmVarString"),
        ("F10-CHASSIS-MIB", "chAlarmVarSlot"),
        ("F10-CHASSIS-MIB", "chAlarmVarPort"))
)
if mibBuilder.loadTexts:
    chAlarmCardMismatch.setStatus(
        "current"
    )

chAlarmCardRemove = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 4, 0, 6)
)
chAlarmCardRemove.setObjects(
      *(("F10-CHASSIS-MIB", "chAlarmVarInteger"),
        ("F10-CHASSIS-MIB", "chAlarmVarString"),
        ("F10-CHASSIS-MIB", "chAlarmVarSlot"),
        ("F10-CHASSIS-MIB", "chAlarmVarPort"))
)
if mibBuilder.loadTexts:
    chAlarmCardRemove.setStatus(
        "current"
    )

chAlarmCardProblem = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 4, 0, 7)
)
chAlarmCardProblem.setObjects(
      *(("F10-CHASSIS-MIB", "chAlarmVarInteger"),
        ("F10-CHASSIS-MIB", "chAlarmVarString"),
        ("F10-CHASSIS-MIB", "chAlarmVarSlot"),
        ("F10-CHASSIS-MIB", "chAlarmVarPort"))
)
if mibBuilder.loadTexts:
    chAlarmCardProblem.setStatus(
        "current"
    )

chAlarmCutoff = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 4, 0, 8)
)
chAlarmCutoff.setObjects(
      *(("F10-CHASSIS-MIB", "chAlarmVarInteger"),
        ("F10-CHASSIS-MIB", "chAlarmVarString"),
        ("F10-CHASSIS-MIB", "chAlarmVarSlot"),
        ("F10-CHASSIS-MIB", "chAlarmVarPort"))
)
if mibBuilder.loadTexts:
    chAlarmCutoff.setStatus(
        "current"
    )

chAlarmSfmUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 4, 0, 9)
)
chAlarmSfmUp.setObjects(
      *(("F10-CHASSIS-MIB", "chAlarmVarInteger"),
        ("F10-CHASSIS-MIB", "chAlarmVarString"),
        ("F10-CHASSIS-MIB", "chAlarmVarSlot"),
        ("F10-CHASSIS-MIB", "chAlarmVarPort"))
)
if mibBuilder.loadTexts:
    chAlarmSfmUp.setStatus(
        "current"
    )

chAlarmSfmDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 4, 0, 10)
)
chAlarmSfmDown.setObjects(
      *(("F10-CHASSIS-MIB", "chAlarmVarInteger"),
        ("F10-CHASSIS-MIB", "chAlarmVarString"),
        ("F10-CHASSIS-MIB", "chAlarmVarSlot"),
        ("F10-CHASSIS-MIB", "chAlarmVarPort"))
)
if mibBuilder.loadTexts:
    chAlarmSfmDown.setStatus(
        "current"
    )

chAlarmRpmUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 4, 0, 11)
)
chAlarmRpmUp.setObjects(
      *(("F10-CHASSIS-MIB", "chAlarmVarInteger"),
        ("F10-CHASSIS-MIB", "chAlarmVarString"),
        ("F10-CHASSIS-MIB", "chAlarmVarSlot"),
        ("F10-CHASSIS-MIB", "chAlarmVarPort"))
)
if mibBuilder.loadTexts:
    chAlarmRpmUp.setStatus(
        "current"
    )

chAlarmRpmDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 4, 0, 12)
)
chAlarmRpmDown.setObjects(
      *(("F10-CHASSIS-MIB", "chAlarmVarInteger"),
        ("F10-CHASSIS-MIB", "chAlarmVarString"),
        ("F10-CHASSIS-MIB", "chAlarmVarSlot"),
        ("F10-CHASSIS-MIB", "chAlarmVarPort"))
)
if mibBuilder.loadTexts:
    chAlarmRpmDown.setStatus(
        "current"
    )

chAlarmPowersupplyDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 4, 0, 13)
)
chAlarmPowersupplyDown.setObjects(
      *(("F10-CHASSIS-MIB", "chAlarmVarInteger"),
        ("F10-CHASSIS-MIB", "chAlarmVarString"),
        ("F10-CHASSIS-MIB", "chAlarmVarSlot"),
        ("F10-CHASSIS-MIB", "chAlarmVarPort"))
)
if mibBuilder.loadTexts:
    chAlarmPowersupplyDown.setStatus(
        "current"
    )

chAlarmMinorTemperatureHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 4, 0, 14)
)
chAlarmMinorTemperatureHigh.setObjects(
      *(("F10-CHASSIS-MIB", "chAlarmVarInteger"),
        ("F10-CHASSIS-MIB", "chAlarmVarString"),
        ("F10-CHASSIS-MIB", "chAlarmVarSlot"),
        ("F10-CHASSIS-MIB", "chAlarmVarPort"))
)
if mibBuilder.loadTexts:
    chAlarmMinorTemperatureHigh.setStatus(
        "current"
    )

chAlarmMajorTemperatureHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 4, 0, 15)
)
chAlarmMajorTemperatureHigh.setObjects(
      *(("F10-CHASSIS-MIB", "chAlarmVarInteger"),
        ("F10-CHASSIS-MIB", "chAlarmVarString"),
        ("F10-CHASSIS-MIB", "chAlarmVarSlot"),
        ("F10-CHASSIS-MIB", "chAlarmVarPort"))
)
if mibBuilder.loadTexts:
    chAlarmMajorTemperatureHigh.setStatus(
        "current"
    )

chAlarmFanTrayDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 4, 0, 16)
)
chAlarmFanTrayDown.setObjects(
      *(("F10-CHASSIS-MIB", "chAlarmVarInteger"),
        ("F10-CHASSIS-MIB", "chAlarmVarString"),
        ("F10-CHASSIS-MIB", "chAlarmVarSlot"),
        ("F10-CHASSIS-MIB", "chAlarmVarPort"))
)
if mibBuilder.loadTexts:
    chAlarmFanTrayDown.setStatus(
        "current"
    )

chAlarmPowersupplyClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 4, 0, 17)
)
chAlarmPowersupplyClear.setObjects(
      *(("F10-CHASSIS-MIB", "chAlarmVarInteger"),
        ("F10-CHASSIS-MIB", "chAlarmVarString"),
        ("F10-CHASSIS-MIB", "chAlarmVarSlot"),
        ("F10-CHASSIS-MIB", "chAlarmVarPort"))
)
if mibBuilder.loadTexts:
    chAlarmPowersupplyClear.setStatus(
        "current"
    )

chAlarmMinorTemperatureClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 4, 0, 18)
)
chAlarmMinorTemperatureClear.setObjects(
      *(("F10-CHASSIS-MIB", "chAlarmVarInteger"),
        ("F10-CHASSIS-MIB", "chAlarmVarString"),
        ("F10-CHASSIS-MIB", "chAlarmVarSlot"),
        ("F10-CHASSIS-MIB", "chAlarmVarPort"))
)
if mibBuilder.loadTexts:
    chAlarmMinorTemperatureClear.setStatus(
        "current"
    )

chAlarmMajorTemperatureClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 4, 0, 19)
)
chAlarmMajorTemperatureClear.setObjects(
      *(("F10-CHASSIS-MIB", "chAlarmVarInteger"),
        ("F10-CHASSIS-MIB", "chAlarmVarString"),
        ("F10-CHASSIS-MIB", "chAlarmVarSlot"),
        ("F10-CHASSIS-MIB", "chAlarmVarPort"))
)
if mibBuilder.loadTexts:
    chAlarmMajorTemperatureClear.setStatus(
        "current"
    )

chAlarmFanTrayClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 4, 0, 20)
)
chAlarmFanTrayClear.setObjects(
      *(("F10-CHASSIS-MIB", "chAlarmVarInteger"),
        ("F10-CHASSIS-MIB", "chAlarmVarString"),
        ("F10-CHASSIS-MIB", "chAlarmVarSlot"),
        ("F10-CHASSIS-MIB", "chAlarmVarPort"))
)
if mibBuilder.loadTexts:
    chAlarmFanTrayClear.setStatus(
        "current"
    )

chAlarmMinorFanBadClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 4, 0, 21)
)
chAlarmMinorFanBadClear.setObjects(
      *(("F10-CHASSIS-MIB", "chAlarmVarInteger"),
        ("F10-CHASSIS-MIB", "chAlarmVarString"),
        ("F10-CHASSIS-MIB", "chAlarmVarSlot"),
        ("F10-CHASSIS-MIB", "chAlarmVarPort"))
)
if mibBuilder.loadTexts:
    chAlarmMinorFanBadClear.setStatus(
        "current"
    )

chAlarmMajorSfmDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 4, 0, 22)
)
chAlarmMajorSfmDown.setObjects(
      *(("F10-CHASSIS-MIB", "chAlarmVarInteger"),
        ("F10-CHASSIS-MIB", "chAlarmVarString"),
        ("F10-CHASSIS-MIB", "chAlarmVarSlot"),
        ("F10-CHASSIS-MIB", "chAlarmVarPort"))
)
if mibBuilder.loadTexts:
    chAlarmMajorSfmDown.setStatus(
        "current"
    )

chAlarmMajorSfmDownClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 4, 0, 23)
)
chAlarmMajorSfmDownClr.setObjects(
      *(("F10-CHASSIS-MIB", "chAlarmVarInteger"),
        ("F10-CHASSIS-MIB", "chAlarmVarString"),
        ("F10-CHASSIS-MIB", "chAlarmVarSlot"),
        ("F10-CHASSIS-MIB", "chAlarmVarPort"))
)
if mibBuilder.loadTexts:
    chAlarmMajorSfmDownClr.setStatus(
        "current"
    )

chAlarmMinorSfmDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 4, 0, 24)
)
chAlarmMinorSfmDown.setObjects(
      *(("F10-CHASSIS-MIB", "chAlarmVarInteger"),
        ("F10-CHASSIS-MIB", "chAlarmVarString"),
        ("F10-CHASSIS-MIB", "chAlarmVarSlot"),
        ("F10-CHASSIS-MIB", "chAlarmVarPort"))
)
if mibBuilder.loadTexts:
    chAlarmMinorSfmDown.setStatus(
        "current"
    )

chAlarmMinorSfmDownClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 4, 0, 25)
)
chAlarmMinorSfmDownClr.setObjects(
      *(("F10-CHASSIS-MIB", "chAlarmVarInteger"),
        ("F10-CHASSIS-MIB", "chAlarmVarString"),
        ("F10-CHASSIS-MIB", "chAlarmVarSlot"),
        ("F10-CHASSIS-MIB", "chAlarmVarPort"))
)
if mibBuilder.loadTexts:
    chAlarmMinorSfmDownClr.setStatus(
        "current"
    )

chAlarmTaskSuspend = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 4, 0, 26)
)
chAlarmTaskSuspend.setObjects(
      *(("F10-CHASSIS-MIB", "chAlarmVarInteger"),
        ("F10-CHASSIS-MIB", "chAlarmVarString"),
        ("F10-CHASSIS-MIB", "chAlarmVarSlot"),
        ("F10-CHASSIS-MIB", "chAlarmVarPort"))
)
if mibBuilder.loadTexts:
    chAlarmTaskSuspend.setStatus(
        "current"
    )

chAlarmTaskTerm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 4, 0, 27)
)
chAlarmTaskTerm.setObjects(
      *(("F10-CHASSIS-MIB", "chAlarmVarInteger"),
        ("F10-CHASSIS-MIB", "chAlarmVarString"),
        ("F10-CHASSIS-MIB", "chAlarmVarSlot"),
        ("F10-CHASSIS-MIB", "chAlarmVarPort"))
)
if mibBuilder.loadTexts:
    chAlarmTaskTerm.setStatus(
        "current"
    )

chAlarmVrrpGoMaster = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 4, 0, 28)
)
chAlarmVrrpGoMaster.setObjects(
      *(("F10-CHASSIS-MIB", "chAlarmVarInteger"),
        ("F10-CHASSIS-MIB", "chAlarmVarString"),
        ("F10-CHASSIS-MIB", "chAlarmVarSlot"),
        ("F10-CHASSIS-MIB", "chAlarmVarPort"))
)
if mibBuilder.loadTexts:
    chAlarmVrrpGoMaster.setStatus(
        "current"
    )

chAlarmVrrpGiveupMaster = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 4, 0, 29)
)
chAlarmVrrpGiveupMaster.setObjects(
      *(("F10-CHASSIS-MIB", "chAlarmVarInteger"),
        ("F10-CHASSIS-MIB", "chAlarmVarString"),
        ("F10-CHASSIS-MIB", "chAlarmVarSlot"),
        ("F10-CHASSIS-MIB", "chAlarmVarPort"))
)
if mibBuilder.loadTexts:
    chAlarmVrrpGiveupMaster.setStatus(
        "current"
    )

chAlarmBgpEstb = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 4, 0, 30)
)
chAlarmBgpEstb.setObjects(
      *(("F10-CHASSIS-MIB", "chAlarmVarInteger"),
        ("F10-CHASSIS-MIB", "chAlarmVarString"),
        ("F10-CHASSIS-MIB", "chAlarmVarSlot"),
        ("F10-CHASSIS-MIB", "chAlarmVarPort"))
)
if mibBuilder.loadTexts:
    chAlarmBgpEstb.setStatus(
        "current"
    )

chAlarmBgpXsition = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 4, 0, 31)
)
chAlarmBgpXsition.setObjects(
      *(("F10-CHASSIS-MIB", "chAlarmVarInteger"),
        ("F10-CHASSIS-MIB", "chAlarmVarString"),
        ("F10-CHASSIS-MIB", "chAlarmVarSlot"),
        ("F10-CHASSIS-MIB", "chAlarmVarPort"))
)
if mibBuilder.loadTexts:
    chAlarmBgpXsition.setStatus(
        "current"
    )

chAlarmMajorPS = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 4, 0, 32)
)
chAlarmMajorPS.setObjects(
      *(("F10-CHASSIS-MIB", "chAlarmVarInteger"),
        ("F10-CHASSIS-MIB", "chAlarmVarString"),
        ("F10-CHASSIS-MIB", "chAlarmVarSlot"),
        ("F10-CHASSIS-MIB", "chAlarmVarPort"))
)
if mibBuilder.loadTexts:
    chAlarmMajorPS.setStatus(
        "current"
    )

chAlarmMajorPSClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 4, 0, 33)
)
chAlarmMajorPSClr.setObjects(
      *(("F10-CHASSIS-MIB", "chAlarmVarInteger"),
        ("F10-CHASSIS-MIB", "chAlarmVarString"),
        ("F10-CHASSIS-MIB", "chAlarmVarSlot"),
        ("F10-CHASSIS-MIB", "chAlarmVarPort"))
)
if mibBuilder.loadTexts:
    chAlarmMajorPSClr.setStatus(
        "current"
    )

chAlarmMinorPS = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 4, 0, 34)
)
chAlarmMinorPS.setObjects(
      *(("F10-CHASSIS-MIB", "chAlarmVarInteger"),
        ("F10-CHASSIS-MIB", "chAlarmVarString"),
        ("F10-CHASSIS-MIB", "chAlarmVarSlot"),
        ("F10-CHASSIS-MIB", "chAlarmVarPort"))
)
if mibBuilder.loadTexts:
    chAlarmMinorPS.setStatus(
        "current"
    )

chAlarmMinorPSClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 4, 0, 35)
)
chAlarmMinorPSClr.setObjects(
      *(("F10-CHASSIS-MIB", "chAlarmVarInteger"),
        ("F10-CHASSIS-MIB", "chAlarmVarString"),
        ("F10-CHASSIS-MIB", "chAlarmVarSlot"),
        ("F10-CHASSIS-MIB", "chAlarmVarPort"))
)
if mibBuilder.loadTexts:
    chAlarmMinorPSClr.setStatus(
        "current"
    )

chAlarmMinorFanBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 4, 0, 36)
)
chAlarmMinorFanBad.setObjects(
      *(("F10-CHASSIS-MIB", "chAlarmVarInteger"),
        ("F10-CHASSIS-MIB", "chAlarmVarString"),
        ("F10-CHASSIS-MIB", "chAlarmVarSlot"),
        ("F10-CHASSIS-MIB", "chAlarmVarPort"))
)
if mibBuilder.loadTexts:
    chAlarmMinorFanBad.setStatus(
        "current"
    )

chAlarmExdCpuThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 4, 0, 37)
)
chAlarmExdCpuThreshold.setObjects(
      *(("F10-CHASSIS-MIB", "chAlarmVarInteger"),
        ("F10-CHASSIS-MIB", "chAlarmVarString"),
        ("F10-CHASSIS-MIB", "chAlarmVarSlot"),
        ("F10-CHASSIS-MIB", "chAlarmVarPort"))
)
if mibBuilder.loadTexts:
    chAlarmExdCpuThreshold.setStatus(
        "current"
    )

chAlarmClrCpuThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 4, 0, 38)
)
chAlarmClrCpuThreshold.setObjects(
      *(("F10-CHASSIS-MIB", "chAlarmVarInteger"),
        ("F10-CHASSIS-MIB", "chAlarmVarString"),
        ("F10-CHASSIS-MIB", "chAlarmVarSlot"),
        ("F10-CHASSIS-MIB", "chAlarmVarPort"))
)
if mibBuilder.loadTexts:
    chAlarmClrCpuThreshold.setStatus(
        "current"
    )

chAlarmExdMemThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 4, 0, 39)
)
chAlarmExdMemThreshold.setObjects(
      *(("F10-CHASSIS-MIB", "chAlarmVarInteger"),
        ("F10-CHASSIS-MIB", "chAlarmVarString"),
        ("F10-CHASSIS-MIB", "chAlarmVarSlot"),
        ("F10-CHASSIS-MIB", "chAlarmVarPort"))
)
if mibBuilder.loadTexts:
    chAlarmExdMemThreshold.setStatus(
        "current"
    )

chAlarmClrMemThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 4, 0, 40)
)
chAlarmClrMemThreshold.setObjects(
      *(("F10-CHASSIS-MIB", "chAlarmVarInteger"),
        ("F10-CHASSIS-MIB", "chAlarmVarString"),
        ("F10-CHASSIS-MIB", "chAlarmVarSlot"),
        ("F10-CHASSIS-MIB", "chAlarmVarPort"))
)
if mibBuilder.loadTexts:
    chAlarmClrMemThreshold.setStatus(
        "current"
    )

chAlarmMacStationMove = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 4, 0, 41)
)
chAlarmMacStationMove.setObjects(
      *(("F10-CHASSIS-MIB", "chAlarmVarInteger"),
        ("F10-CHASSIS-MIB", "chAlarmVarString"),
        ("F10-CHASSIS-MIB", "chAlarmVarSlot"),
        ("F10-CHASSIS-MIB", "chAlarmVarPort"))
)
if mibBuilder.loadTexts:
    chAlarmMacStationMove.setStatus(
        "current"
    )

chAlarmSfmAdd = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 4, 0, 42)
)
chAlarmSfmAdd.setObjects(
      *(("F10-CHASSIS-MIB", "chAlarmVarInteger"),
        ("F10-CHASSIS-MIB", "chAlarmVarString"),
        ("F10-CHASSIS-MIB", "chAlarmVarSlot"),
        ("F10-CHASSIS-MIB", "chAlarmVarPort"))
)
if mibBuilder.loadTexts:
    chAlarmSfmAdd.setStatus(
        "current"
    )

chAlarmSfmRemove = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 4, 0, 43)
)
chAlarmSfmRemove.setObjects(
      *(("F10-CHASSIS-MIB", "chAlarmVarInteger"),
        ("F10-CHASSIS-MIB", "chAlarmVarString"),
        ("F10-CHASSIS-MIB", "chAlarmVarSlot"),
        ("F10-CHASSIS-MIB", "chAlarmVarPort"))
)
if mibBuilder.loadTexts:
    chAlarmSfmRemove.setStatus(
        "current"
    )

chAlarmRpmPrimary = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 4, 0, 44)
)
chAlarmRpmPrimary.setObjects(
      *(("F10-CHASSIS-MIB", "chAlarmVarInteger"),
        ("F10-CHASSIS-MIB", "chAlarmVarString"),
        ("F10-CHASSIS-MIB", "chAlarmVarSlot"),
        ("F10-CHASSIS-MIB", "chAlarmVarPort"))
)
if mibBuilder.loadTexts:
    chAlarmRpmPrimary.setStatus(
        "current"
    )

chSnmpIpAclDeny = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 4, 0, 45)
)
chSnmpIpAclDeny.setObjects(
      *(("F10-CHASSIS-MIB", "chAlarmVarInteger"),
        ("F10-CHASSIS-MIB", "chAlarmVarString"),
        ("F10-CHASSIS-MIB", "chAlarmVarSlot"),
        ("F10-CHASSIS-MIB", "chAlarmVarPort"))
)
if mibBuilder.loadTexts:
    chSnmpIpAclDeny.setStatus(
        "current"
    )

chAlarmSRAMParityErrorDetect = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 4, 0, 47)
)
chAlarmSRAMParityErrorDetect.setObjects(
      *(("F10-CHASSIS-MIB", "chAlarmVarInteger"),
        ("F10-CHASSIS-MIB", "chAlarmVarString"),
        ("F10-CHASSIS-MIB", "chAlarmVarSlot"),
        ("F10-CHASSIS-MIB", "chAlarmVarPort"))
)
if mibBuilder.loadTexts:
    chAlarmSRAMParityErrorDetect.setStatus(
        "current"
    )

chAlarmAcDcMixedPowerSupplyDetect = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 4, 0, 48)
)
chAlarmAcDcMixedPowerSupplyDetect.setObjects(
      *(("F10-CHASSIS-MIB", "chAlarmVarInteger"),
        ("F10-CHASSIS-MIB", "chAlarmVarString"),
        ("F10-CHASSIS-MIB", "chAlarmVarSlot"),
        ("F10-CHASSIS-MIB", "chAlarmVarPort"))
)
if mibBuilder.loadTexts:
    chAlarmAcDcMixedPowerSupplyDetect.setStatus(
        "current"
    )

chAlarmCardVersionMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 4, 0, 56)
)
chAlarmCardVersionMismatch.setObjects(
      *(("F10-CHASSIS-MIB", "chAlarmVarInteger"),
        ("F10-CHASSIS-MIB", "chAlarmVarString"),
        ("F10-CHASSIS-MIB", "chAlarmVarSlot"),
        ("F10-CHASSIS-MIB", "chAlarmVarPort"))
)
if mibBuilder.loadTexts:
    chAlarmCardVersionMismatch.setStatus(
        "current"
    )

chAlarmUnsupportedOptic = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 4, 0, 57)
)
chAlarmUnsupportedOptic.setObjects(
      *(("F10-CHASSIS-MIB", "chAlarmVarInteger"),
        ("F10-CHASSIS-MIB", "chAlarmVarString"),
        ("F10-CHASSIS-MIB", "chAlarmVarSlot"),
        ("F10-CHASSIS-MIB", "chAlarmVarPort"))
)
if mibBuilder.loadTexts:
    chAlarmUnsupportedOptic.setStatus(
        "current"
    )

chAlarmFanTrayOrPsuDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 4, 0, 58)
)
chAlarmFanTrayOrPsuDown.setObjects(
      *(("F10-CHASSIS-MIB", "chAlarmVarInteger"),
        ("F10-CHASSIS-MIB", "chAlarmVarString"),
        ("F10-CHASSIS-MIB", "chAlarmVarSlot"),
        ("F10-CHASSIS-MIB", "chAlarmVarPort"))
)
if mibBuilder.loadTexts:
    chAlarmFanTrayOrPsuDown.setStatus(
        "current"
    )

chAlarmFanTrayOrPsuClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 1, 4, 0, 59)
)
chAlarmFanTrayOrPsuClear.setObjects(
      *(("F10-CHASSIS-MIB", "chAlarmVarInteger"),
        ("F10-CHASSIS-MIB", "chAlarmVarString"),
        ("F10-CHASSIS-MIB", "chAlarmVarSlot"),
        ("F10-CHASSIS-MIB", "chAlarmVarPort"))
)
if mibBuilder.loadTexts:
    chAlarmFanTrayOrPsuClear.setStatus(
        "current"
    )


# Notifications groups

f10ChassisNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 2, 2, 5)
)
f10ChassisNotificationGroup.setObjects(
      *(("F10-CHASSIS-MIB", "chAlarmCardDown"),
        ("F10-CHASSIS-MIB", "chAlarmCardUp"),
        ("F10-CHASSIS-MIB", "chAlarmCardReset"),
        ("F10-CHASSIS-MIB", "chAlarmCardOffline"),
        ("F10-CHASSIS-MIB", "chAlarmCardMismatch"),
        ("F10-CHASSIS-MIB", "chAlarmCardRemove"),
        ("F10-CHASSIS-MIB", "chAlarmCardProblem"),
        ("F10-CHASSIS-MIB", "chAlarmCutoff"),
        ("F10-CHASSIS-MIB", "chAlarmSfmUp"),
        ("F10-CHASSIS-MIB", "chAlarmSfmDown"),
        ("F10-CHASSIS-MIB", "chAlarmRpmUp"),
        ("F10-CHASSIS-MIB", "chAlarmRpmDown"),
        ("F10-CHASSIS-MIB", "chAlarmPowersupplyDown"),
        ("F10-CHASSIS-MIB", "chAlarmMinorTemperatureHigh"),
        ("F10-CHASSIS-MIB", "chAlarmMajorTemperatureHigh"),
        ("F10-CHASSIS-MIB", "chAlarmFanTrayDown"),
        ("F10-CHASSIS-MIB", "chAlarmPowersupplyClear"),
        ("F10-CHASSIS-MIB", "chAlarmMinorTemperatureClear"),
        ("F10-CHASSIS-MIB", "chAlarmMajorTemperatureClear"),
        ("F10-CHASSIS-MIB", "chAlarmFanTrayClear"),
        ("F10-CHASSIS-MIB", "chAlarmMinorFanBadClear"),
        ("F10-CHASSIS-MIB", "chAlarmMajorSfmDown"),
        ("F10-CHASSIS-MIB", "chAlarmMajorSfmDownClr"),
        ("F10-CHASSIS-MIB", "chAlarmMinorSfmDown"),
        ("F10-CHASSIS-MIB", "chAlarmMinorSfmDownClr"),
        ("F10-CHASSIS-MIB", "chAlarmTaskSuspend"),
        ("F10-CHASSIS-MIB", "chAlarmTaskTerm"),
        ("F10-CHASSIS-MIB", "chAlarmVrrpGoMaster"),
        ("F10-CHASSIS-MIB", "chAlarmVrrpGiveupMaster"),
        ("F10-CHASSIS-MIB", "chAlarmBgpEstb"),
        ("F10-CHASSIS-MIB", "chAlarmBgpXsition"),
        ("F10-CHASSIS-MIB", "chAlarmMajorPS"),
        ("F10-CHASSIS-MIB", "chAlarmMajorPSClr"),
        ("F10-CHASSIS-MIB", "chAlarmMinorPS"),
        ("F10-CHASSIS-MIB", "chAlarmMinorPSClr"),
        ("F10-CHASSIS-MIB", "chAlarmMinorFanBad"),
        ("F10-CHASSIS-MIB", "chAlarmExdCpuThreshold"),
        ("F10-CHASSIS-MIB", "chAlarmClrCpuThreshold"),
        ("F10-CHASSIS-MIB", "chAlarmExdMemThreshold"),
        ("F10-CHASSIS-MIB", "chAlarmClrMemThreshold"),
        ("F10-CHASSIS-MIB", "chAlarmMacStationMove"),
        ("F10-CHASSIS-MIB", "chAlarmSfmAdd"),
        ("F10-CHASSIS-MIB", "chAlarmSfmRemove"),
        ("F10-CHASSIS-MIB", "chAlarmRpmPrimary"),
        ("F10-CHASSIS-MIB", "chSnmpIpAclDeny"),
        ("F10-CHASSIS-MIB", "chAlarmSRAMParityErrorDetect"),
        ("F10-CHASSIS-MIB", "chAlarmAcDcMixedPowerSupplyDetect"),
        ("F10-CHASSIS-MIB", "chAlarmCardVersionMismatch"),
        ("F10-CHASSIS-MIB", "chAlarmUnsupportedOptic"))
)
if mibBuilder.loadTexts:
    f10ChassisNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

f10ChassisMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6027, 3, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    f10ChassisMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "F10-CHASSIS-MIB",
    **{"f10ChassisMib": f10ChassisMib,
       "f10ChassisMibObject": f10ChassisMibObject,
       "chObjects": chObjects,
       "chType": chType,
       "chSerialNumber": chSerialNumber,
       "chVendorId": chVendorId,
       "chMfgDate": chMfgDate,
       "chEcLevel": chEcLevel,
       "chNumFanTrays": chNumFanTrays,
       "chNumPowerSupplies": chNumPowerSupplies,
       "chNumSlots": chNumSlots,
       "chNumSfmSlots": chNumSfmSlots,
       "chNumAirFilters": chNumAirFilters,
       "chSlot1to16": chSlot1to16,
       "chCountryCode": chCountryCode,
       "chPartNum": chPartNum,
       "chProductRev": chProductRev,
       "chProductOrder": chProductOrder,
       "chChassisMode": chChassisMode,
       "chSysObjects": chSysObjects,
       "chSysPowerSupplyTable": chSysPowerSupplyTable,
       "chSysPowerSupplyEntry": chSysPowerSupplyEntry,
       "chSysPowerSupplyIndex": chSysPowerSupplyIndex,
       "chSysPowerSupplyOperStatus": chSysPowerSupplyOperStatus,
       "chSysPowerSupplyType": chSysPowerSupplyType,
       "chSysFanTrayTable": chSysFanTrayTable,
       "chSysFanTrayEntry": chSysFanTrayEntry,
       "chSysFanTrayIndex": chSysFanTrayIndex,
       "chSysFanTrayOperStatus": chSysFanTrayOperStatus,
       "chSysCardTable": chSysCardTable,
       "chSysCardEntry": chSysCardEntry,
       "chSysCardSlotIndex": chSysCardSlotIndex,
       "chSysCardType": chSysCardType,
       "chSysCardNumber": chSysCardNumber,
       "chSysCardSerialNumber": chSysCardSerialNumber,
       "chSysCardVendorId": chSysCardVendorId,
       "chSysCardMfgDate": chSysCardMfgDate,
       "chSysCardEcLevel": chSysCardEcLevel,
       "chSysCardUpperTemp": chSysCardUpperTemp,
       "chSysCardLowerTemp": chSysCardLowerTemp,
       "chSysCardNumProcessors": chSysCardNumProcessors,
       "chSysCardNumPhyPorts": chSysCardNumPhyPorts,
       "chSysCardNumLgcPorts": chSysCardNumLgcPorts,
       "chSysCardUpTime": chSysCardUpTime,
       "chSysCardAdminStatus": chSysCardAdminStatus,
       "chSysCardOperStatus": chSysCardOperStatus,
       "chSysCardFaultStatus": chSysCardFaultStatus,
       "chSysCardLogStream": chSysCardLogStream,
       "chSysCardCountryCode": chSysCardCountryCode,
       "chSysCardPartNum": chSysCardPartNum,
       "chSysCardProductRev": chSysCardProductRev,
       "chSysCardProdOrder": chSysCardProdOrder,
       "chSysCardParityPhantomError": chSysCardParityPhantomError,
       "chSysCardParityRecoverableError": chSysCardParityRecoverableError,
       "chSysCardParityNonrecovrableError": chSysCardParityNonrecovrableError,
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
       "chSysProcessorLogStream": chSysProcessorLogStream,
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
       "chSysSfmTable": chSysSfmTable,
       "chSysSfmEntry": chSysSfmEntry,
       "chSysSfmIndex": chSysSfmIndex,
       "chSysSfmSerialNumber": chSysSfmSerialNumber,
       "chSysSfmVendorId": chSysSfmVendorId,
       "chSysSfmMfgDate": chSysSfmMfgDate,
       "chSysSfmEcLevel": chSysSfmEcLevel,
       "chSysSfmAdminStatus": chSysSfmAdminStatus,
       "chSysSfmOperStatus": chSysSfmOperStatus,
       "chSysSfmErrorStatus": chSysSfmErrorStatus,
       "chSysSfmCountryCode": chSysSfmCountryCode,
       "chSysSfmPartNum": chSysSfmPartNum,
       "chSysSfmProductRev": chSysSfmProductRev,
       "chSysSfmProdOrder": chSysSfmProdOrder,
       "chSysSfmGroup": chSysSfmGroup,
       "chSfmUtil5Sec": chSfmUtil5Sec,
       "chSfmUtil1Min": chSfmUtil1Min,
       "chSfmUtil5Min": chSfmUtil5Min,
       "chRpmObjects": chRpmObjects,
       "chRpmNumRpms": chRpmNumRpms,
       "chRpmSlotNumber": chRpmSlotNumber,
       "chRpmUptime": chRpmUptime,
       "chRpmLastSwitchDate": chRpmLastSwitchDate,
       "chRpmCOAlarmStatus": chRpmCOAlarmStatus,
       "chRpmFlashStatus": chRpmFlashStatus,
       "chRpmUtilTable": chRpmUtilTable,
       "chRpmUtilEntry": chRpmUtilEntry,
       "chRpmCpuIndex": chRpmCpuIndex,
       "chRpmCpuType": chRpmCpuType,
       "chRpmCpuUtil5Sec": chRpmCpuUtil5Sec,
       "chRpmCpuUtil1Min": chRpmCpuUtil1Min,
       "chRpmCpuUtil5Min": chRpmCpuUtil5Min,
       "chRpmMemUsageUtil": chRpmMemUsageUtil,
       "chRpmMajorAlarmStatus": chRpmMajorAlarmStatus,
       "chRpmMinorAlarmStatus": chRpmMinorAlarmStatus,
       "chAlarmObjects": chAlarmObjects,
       "chAlarmMibNotifications": chAlarmMibNotifications,
       "chAlarmCardDown": chAlarmCardDown,
       "chAlarmCardUp": chAlarmCardUp,
       "chAlarmCardReset": chAlarmCardReset,
       "chAlarmCardOffline": chAlarmCardOffline,
       "chAlarmCardMismatch": chAlarmCardMismatch,
       "chAlarmCardRemove": chAlarmCardRemove,
       "chAlarmCardProblem": chAlarmCardProblem,
       "chAlarmCutoff": chAlarmCutoff,
       "chAlarmSfmUp": chAlarmSfmUp,
       "chAlarmSfmDown": chAlarmSfmDown,
       "chAlarmRpmUp": chAlarmRpmUp,
       "chAlarmRpmDown": chAlarmRpmDown,
       "chAlarmPowersupplyDown": chAlarmPowersupplyDown,
       "chAlarmMinorTemperatureHigh": chAlarmMinorTemperatureHigh,
       "chAlarmMajorTemperatureHigh": chAlarmMajorTemperatureHigh,
       "chAlarmFanTrayDown": chAlarmFanTrayDown,
       "chAlarmPowersupplyClear": chAlarmPowersupplyClear,
       "chAlarmMinorTemperatureClear": chAlarmMinorTemperatureClear,
       "chAlarmMajorTemperatureClear": chAlarmMajorTemperatureClear,
       "chAlarmFanTrayClear": chAlarmFanTrayClear,
       "chAlarmMinorFanBadClear": chAlarmMinorFanBadClear,
       "chAlarmMajorSfmDown": chAlarmMajorSfmDown,
       "chAlarmMajorSfmDownClr": chAlarmMajorSfmDownClr,
       "chAlarmMinorSfmDown": chAlarmMinorSfmDown,
       "chAlarmMinorSfmDownClr": chAlarmMinorSfmDownClr,
       "chAlarmTaskSuspend": chAlarmTaskSuspend,
       "chAlarmTaskTerm": chAlarmTaskTerm,
       "chAlarmVrrpGoMaster": chAlarmVrrpGoMaster,
       "chAlarmVrrpGiveupMaster": chAlarmVrrpGiveupMaster,
       "chAlarmBgpEstb": chAlarmBgpEstb,
       "chAlarmBgpXsition": chAlarmBgpXsition,
       "chAlarmMajorPS": chAlarmMajorPS,
       "chAlarmMajorPSClr": chAlarmMajorPSClr,
       "chAlarmMinorPS": chAlarmMinorPS,
       "chAlarmMinorPSClr": chAlarmMinorPSClr,
       "chAlarmMinorFanBad": chAlarmMinorFanBad,
       "chAlarmExdCpuThreshold": chAlarmExdCpuThreshold,
       "chAlarmClrCpuThreshold": chAlarmClrCpuThreshold,
       "chAlarmExdMemThreshold": chAlarmExdMemThreshold,
       "chAlarmClrMemThreshold": chAlarmClrMemThreshold,
       "chAlarmMacStationMove": chAlarmMacStationMove,
       "chAlarmSfmAdd": chAlarmSfmAdd,
       "chAlarmSfmRemove": chAlarmSfmRemove,
       "chAlarmRpmPrimary": chAlarmRpmPrimary,
       "chSnmpIpAclDeny": chSnmpIpAclDeny,
       "chAlarmSRAMParityErrorDetect": chAlarmSRAMParityErrorDetect,
       "chAlarmAcDcMixedPowerSupplyDetect": chAlarmAcDcMixedPowerSupplyDetect,
       "chAlarmCardVersionMismatch": chAlarmCardVersionMismatch,
       "chAlarmUnsupportedOptic": chAlarmUnsupportedOptic,
       "chAlarmFanTrayOrPsuDown": chAlarmFanTrayOrPsuDown,
       "chAlarmFanTrayOrPsuClear": chAlarmFanTrayOrPsuClear,
       "chAlarmVariable": chAlarmVariable,
       "chAlarmVarInteger": chAlarmVarInteger,
       "chAlarmVarString": chAlarmVarString,
       "chAlarmVarSlot": chAlarmVarSlot,
       "chAlarmVarPort": chAlarmVarPort,
       "chLineCardObjects": chLineCardObjects,
       "chLineCardUtilTable": chLineCardUtilTable,
       "chLineCardUtilEntry": chLineCardUtilEntry,
       "chLineCardCpuUtil5Sec": chLineCardCpuUtil5Sec,
       "chLineCardCpuUtil1Min": chLineCardCpuUtil1Min,
       "chLineCardCpuUtil5Min": chLineCardCpuUtil5Min,
       "chLineCardMemUsageUtil": chLineCardMemUsageUtil,
       "f10ChassisMibConformance": f10ChassisMibConformance,
       "f10ChassisMibCompliances": f10ChassisMibCompliances,
       "f10ChassisMibCompliance": f10ChassisMibCompliance,
       "f10ChassisMibGroups": f10ChassisMibGroups,
       "f10ComponentGroup": f10ComponentGroup,
       "f10SystemGroup": f10SystemGroup,
       "f10RpmGroup": f10RpmGroup,
       "f10LineCardGroup": f10LineCardGroup,
       "f10ChassisNotificationGroup": f10ChassisNotificationGroup}
)
