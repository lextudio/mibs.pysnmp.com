# SNMP MIB module (CADANT-CMTS-EQUIPMENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CADANT-CMTS-EQUIPMENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:52:28 2024
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

(cadEquipment,) = mibBuilder.importSymbols(
    "CADANT-PRODUCTS-MIB",
    "cadEquipment")

(AdminState,
 CardId,
 CerCardSubType,
 CerCardType,
 CerPicType,
 CerPortType,
 DiskVolumeUsageLevel,
 DuplexStatus,
 EqActionType,
 FirmwareSource,
 FlowControlMode,
 PicType,
 PortDetectedMode,
 PortId,
 PortMode,
 PortType,
 PrimaryState,
 SecondaryState) = mibBuilder.importSymbols(
    "CADANT-TC",
    "AdminState",
    "CardId",
    "CerCardSubType",
    "CerCardType",
    "CerPicType",
    "CerPortType",
    "DiskVolumeUsageLevel",
    "DuplexStatus",
    "EqActionType",
    "FirmwareSource",
    "FlowControlMode",
    "PicType",
    "PortDetectedMode",
    "PortId",
    "PortMode",
    "PortType",
    "PrimaryState",
    "SecondaryState")

(TenthdBmV,) = mibBuilder.importSymbols(
    "DOCS-IF-MIB",
    "TenthdBmV")

(InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "ifIndex")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

cadEquipmentMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1)
)
cadEquipmentMib.setRevisions(
        ("2015-10-06 00:00",
         "2015-08-26 00:00",
         "2015-08-12 00:00",
         "2015-07-21 00:00",
         "2015-07-12 00:00",
         "2015-07-07 00:00",
         "2015-06-03 00:00",
         "2015-06-01 00:00",
         "2014-12-01 00:00",
         "2014-10-14 00:00",
         "2014-08-01 00:00",
         "2014-03-16 00:00",
         "2013-05-16 00:00",
         "2013-04-12 00:00",
         "2013-02-19 00:00",
         "2013-01-08 00:00",
         "2013-01-07 00:00",
         "2012-09-07 00:00",
         "2012-07-10 00:00",
         "2012-07-03 00:00",
         "2012-05-21 00:00",
         "2012-05-08 00:00",
         "2012-05-03 00:00",
         "2012-05-02 00:00",
         "2012-04-25 00:00",
         "2012-04-11 00:00",
         "2012-03-22 00:00",
         "2012-01-05 00:00",
         "2011-09-13 00:00",
         "2011-08-05 00:00",
         "2011-07-19 00:00",
         "2011-07-18 00:00",
         "2011-07-08 00:00",
         "2011-06-28 00:00",
         "2011-06-14 00:00",
         "2011-03-18 00:00",
         "2011-03-17 00:00",
         "2011-01-27 00:00",
         "2009-07-10 00:00",
         "2009-03-03 00:00",
         "2009-01-05 00:00",
         "2008-10-14 00:00",
         "2008-10-01 00:00",
         "2008-07-03 00:00",
         "2008-06-18 00:00",
         "2008-04-28 00:00",
         "2008-04-02 00:00",
         "2008-02-25 00:00",
         "2007-11-05 00:00",
         "2007-01-10 00:00",
         "2006-11-13 00:00",
         "2006-09-12 00:00",
         "2006-08-23 00:00",
         "2006-02-14 00:00",
         "2005-08-30 00:00",
         "2005-04-06 00:00",
         "2005-02-04 00:00",
         "2005-01-24 00:00",
         "2004-12-01 00:00",
         "2004-11-18 00:00",
         "2004-11-11 00:00",
         "2004-09-07 00:00",
         "2004-07-23 00:00",
         "2004-03-22 00:00",
         "2004-03-18 00:00",
         "2004-02-04 00:00",
         "2003-12-18 00:00",
         "2003-03-31 00:00",
         "2003-03-17 00:00",
         "2003-03-05 00:00",
         "2003-03-02 00:00",
         "2003-01-29 00:00",
         "2002-12-14 00:00",
         "2002-11-07 00:00",
         "2002-09-25 00:00",
         "2002-09-01 00:00",
         "2002-05-01 00:00",
         "2001-12-28 16:30",
         "2001-12-21 16:30",
         "2001-10-03 00:00",
         "2001-07-17 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class TestId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )



class TestType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("diagnostic", 2),
          ("test", 1),
          ("unknown", 3))
    )



class TestCommand(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 4),
          ("noop", 1),
          ("runNow", 5),
          ("stop", 2))
    )



class TestScheduleCommand(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("noop", 1))
    )



class TestSchedule(Integer32, TextualConvention):
    status = "current"


class TestResult(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("abort", 7),
          ("fail", 4),
          ("inProgress", 2),
          ("inconclusive", 5),
          ("notRun", 1),
          ("pass", 3),
          ("timeOut", 6))
    )



class TestTransactionId(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class CerCamFaultTrapType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            12
        )
    )
    namedValues = NamedValues(
        ("fpgaFatalError", 12)
    )



# MIB Managed Objects in the order of their OIDs

_EquipmentTraps_ObjectIdentity = ObjectIdentity
equipmentTraps = _EquipmentTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 0)
)
_CerCamFaultInfo_ObjectIdentity = ObjectIdentity
cerCamFaultInfo = _CerCamFaultInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 0, 40)
)
_CerCamFaultId_Type = CerCamFaultTrapType
_CerCamFaultId_Object = MibScalar
cerCamFaultId = _CerCamFaultId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 0, 40, 1),
    _CerCamFaultId_Type()
)
cerCamFaultId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cerCamFaultId.setStatus("current")
_CerCamFaultRecovery_Type = TruthValue
_CerCamFaultRecovery_Object = MibScalar
cerCamFaultRecovery = _CerCamFaultRecovery_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 0, 40, 2),
    _CerCamFaultRecovery_Type()
)
cerCamFaultRecovery.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cerCamFaultRecovery.setStatus("current")
_CerCamFaultAutoFailback_Type = TruthValue
_CerCamFaultAutoFailback_Object = MibScalar
cerCamFaultAutoFailback = _CerCamFaultAutoFailback_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 0, 40, 3),
    _CerCamFaultAutoFailback_Type()
)
cerCamFaultAutoFailback.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cerCamFaultAutoFailback.setStatus("current")


class _CerCamFaultErrorStr_Type(DisplayString):
    """Custom type cerCamFaultErrorStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_CerCamFaultErrorStr_Type.__name__ = "DisplayString"
_CerCamFaultErrorStr_Object = MibScalar
cerCamFaultErrorStr = _CerCamFaultErrorStr_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 0, 40, 4),
    _CerCamFaultErrorStr_Type()
)
cerCamFaultErrorStr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cerCamFaultErrorStr.setStatus("current")
_SystemGeneral_ObjectIdentity = ObjectIdentity
systemGeneral = _SystemGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 1)
)
_SystemClock_Type = DateAndTime
_SystemClock_Object = MibScalar
systemClock = _SystemClock_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 1, 1),
    _SystemClock_Type()
)
systemClock.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    systemClock.setStatus("current")
_TrapCounter_Type = Counter32
_TrapCounter_Object = MibScalar
trapCounter = _TrapCounter_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 1, 2),
    _TrapCounter_Type()
)
trapCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapCounter.setStatus("current")


class _TrapSeverity_Type(Integer32):
    """Custom type trapSeverity based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 1),
          ("critical", 6),
          ("indeterminate", 2),
          ("informational", 7),
          ("major", 5),
          ("minor", 4),
          ("warning", 3))
    )


_TrapSeverity_Type.__name__ = "Integer32"
_TrapSeverity_Object = MibScalar
trapSeverity = _TrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 1, 3),
    _TrapSeverity_Type()
)
trapSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapSeverity.setStatus("current")
_SystemKey_Type = DisplayString
_SystemKey_Object = MibScalar
systemKey = _SystemKey_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 1, 4),
    _SystemKey_Type()
)
systemKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemKey.setStatus("current")


class _CardNumber_Type(CardId):
    """Custom type cardNumber based on CardId"""
    defaultValue = 0


_CardNumber_Object = MibScalar
cardNumber = _CardNumber_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 1, 98),
    _CardNumber_Type()
)
cardNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cardNumber.setStatus("current")


class _PortNumber_Type(PortId):
    """Custom type portNumber based on PortId"""
    defaultValue = 0


_PortNumber_Object = MibScalar
portNumber = _PortNumber_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 1, 99),
    _PortNumber_Type()
)
portNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    portNumber.setStatus("current")


class _DiskDriveNumber_Type(Integer32):
    """Custom type diskDriveNumber based on Integer32"""
    defaultValue = 99

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_DiskDriveNumber_Type.__name__ = "Integer32"
_DiskDriveNumber_Object = MibScalar
diskDriveNumber = _DiskDriveNumber_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 1, 100),
    _DiskDriveNumber_Type()
)
diskDriveNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    diskDriveNumber.setStatus("current")


class _DiskVolumeNumber_Type(Integer32):
    """Custom type diskVolumeNumber based on Integer32"""
    defaultValue = 99

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_DiskVolumeNumber_Type.__name__ = "Integer32"
_DiskVolumeNumber_Object = MibScalar
diskVolumeNumber = _DiskVolumeNumber_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 1, 101),
    _DiskVolumeNumber_Type()
)
diskVolumeNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    diskVolumeNumber.setStatus("current")


class _CerCardNumber_Type(CardId):
    """Custom type cerCardNumber based on CardId"""
    defaultValue = 0


_CerCardNumber_Object = MibScalar
cerCardNumber = _CerCardNumber_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 1, 200),
    _CerCardNumber_Type()
)
cerCardNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cerCardNumber.setStatus("current")


class _CerPortNumber_Type(PortId):
    """Custom type cerPortNumber based on PortId"""
    defaultValue = 0


_CerPortNumber_Object = MibScalar
cerPortNumber = _CerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 1, 201),
    _CerPortNumber_Type()
)
cerPortNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cerPortNumber.setStatus("current")


class _CerDiskDriveNumber_Type(Integer32):
    """Custom type cerDiskDriveNumber based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_CerDiskDriveNumber_Type.__name__ = "Integer32"
_CerDiskDriveNumber_Object = MibScalar
cerDiskDriveNumber = _CerDiskDriveNumber_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 1, 202),
    _CerDiskDriveNumber_Type()
)
cerDiskDriveNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cerDiskDriveNumber.setStatus("current")


class _CerDiskVolumeNumber_Type(Integer32):
    """Custom type cerDiskVolumeNumber based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_CerDiskVolumeNumber_Type.__name__ = "Integer32"
_CerDiskVolumeNumber_Object = MibScalar
cerDiskVolumeNumber = _CerDiskVolumeNumber_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 1, 203),
    _CerDiskVolumeNumber_Type()
)
cerDiskVolumeNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cerDiskVolumeNumber.setStatus("current")
_ShelfObjects_ObjectIdentity = ObjectIdentity
shelfObjects = _ShelfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 2)
)


class _ShelfName_Type(DisplayString):
    """Custom type shelfName based on DisplayString"""
    defaultValue = OctetString("Arris CER CMTS")


_ShelfName_Object = MibScalar
shelfName = _ShelfName_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 2, 2),
    _ShelfName_Type()
)
shelfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shelfName.setStatus("current")
_ShelfSwVersion_Type = DisplayString
_ShelfSwVersion_Object = MibScalar
shelfSwVersion = _ShelfSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 2, 3),
    _ShelfSwVersion_Type()
)
shelfSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shelfSwVersion.setStatus("current")
_EquipmentState_ObjectIdentity = ObjectIdentity
equipmentState = _EquipmentState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 3)
)
_CardLastChangeTime_Type = TimeStamp
_CardLastChangeTime_Object = MibScalar
cardLastChangeTime = _CardLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 3, 2),
    _CardLastChangeTime_Type()
)
cardLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardLastChangeTime.setStatus("current")
_PortLastChangeTime_Type = TimeStamp
_PortLastChangeTime_Object = MibScalar
portLastChangeTime = _PortLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 3, 3),
    _PortLastChangeTime_Type()
)
portLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portLastChangeTime.setStatus("current")
_EquipmentTbl_ObjectIdentity = ObjectIdentity
equipmentTbl = _EquipmentTbl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4)
)
_CerCardTable_Object = MibTable
cerCardTable = _CerCardTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 12)
)
if mibBuilder.loadTexts:
    cerCardTable.setStatus("current")
_CerCardEntry_Object = MibTableRow
cerCardEntry = _CerCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 12, 1)
)
cerCardEntry.setIndexNames(
    (0, "CADANT-CMTS-EQUIPMENT-MIB", "cerCardId"),
)
if mibBuilder.loadTexts:
    cerCardEntry.setStatus("current")
_CerCardId_Type = CardId
_CerCardId_Object = MibTableColumn
cerCardId = _CerCardId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 12, 1, 2),
    _CerCardId_Type()
)
cerCardId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cerCardId.setStatus("current")


class _CerCardName_Type(DisplayString):
    """Custom type cerCardName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CerCardName_Type.__name__ = "DisplayString"
_CerCardName_Object = MibTableColumn
cerCardName = _CerCardName_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 12, 1, 3),
    _CerCardName_Type()
)
cerCardName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cerCardName.setStatus("current")
_CerCardType_Type = CerCardType
_CerCardType_Object = MibTableColumn
cerCardType = _CerCardType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 12, 1, 4),
    _CerCardType_Type()
)
cerCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerCardType.setStatus("current")
_CerCardSubType_Type = CerCardSubType
_CerCardSubType_Object = MibTableColumn
cerCardSubType = _CerCardSubType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 12, 1, 5),
    _CerCardSubType_Type()
)
cerCardSubType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cerCardSubType.setStatus("current")
_CerCardAdminState_Type = AdminState
_CerCardAdminState_Object = MibTableColumn
cerCardAdminState = _CerCardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 12, 1, 12),
    _CerCardAdminState_Type()
)
cerCardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cerCardAdminState.setStatus("current")
_CerCardPrState_Type = PrimaryState
_CerCardPrState_Object = MibTableColumn
cerCardPrState = _CerCardPrState_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 12, 1, 13),
    _CerCardPrState_Type()
)
cerCardPrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerCardPrState.setStatus("current")
_CerCardSecState_Type = SecondaryState
_CerCardSecState_Object = MibTableColumn
cerCardSecState = _CerCardSecState_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 12, 1, 14),
    _CerCardSecState_Type()
)
cerCardSecState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerCardSecState.setStatus("current")
_CerCardDplxStatus_Type = DuplexStatus
_CerCardDplxStatus_Object = MibTableColumn
cerCardDplxStatus = _CerCardDplxStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 12, 1, 15),
    _CerCardDplxStatus_Type()
)
cerCardDplxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerCardDplxStatus.setStatus("current")
_CerCardAction_Type = EqActionType
_CerCardAction_Object = MibTableColumn
cerCardAction = _CerCardAction_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 12, 1, 17),
    _CerCardAction_Type()
)
cerCardAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cerCardAction.setStatus("current")


class _CerCardTrapInh_Type(Bits):
    """Custom type cerCardTrapInh based on Bits"""
    namedValues = NamedValues(
        *(("detected", 3),
          ("duplex", 2),
          ("overload", 7),
          ("primary", 0),
          ("secondary", 1),
          ("tempnoreport", 5),
          ("tempoutofrange", 4),
          ("tempoverheat", 6))
    )

_CerCardTrapInh_Type.__name__ = "Bits"
_CerCardTrapInh_Object = MibTableColumn
cerCardTrapInh = _CerCardTrapInh_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 12, 1, 18),
    _CerCardTrapInh_Type()
)
cerCardTrapInh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cerCardTrapInh.setStatus("current")


class _CerCardNumPorts_Type(Integer32):
    """Custom type cerCardNumPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_CerCardNumPorts_Type.__name__ = "Integer32"
_CerCardNumPorts_Object = MibTableColumn
cerCardNumPorts = _CerCardNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 12, 1, 19),
    _CerCardNumPorts_Type()
)
cerCardNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerCardNumPorts.setStatus("current")
_CerCardDetected_Type = CerCardType
_CerCardDetected_Object = MibTableColumn
cerCardDetected = _CerCardDetected_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 12, 1, 20),
    _CerCardDetected_Type()
)
cerCardDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerCardDetected.setStatus("current")
_CerCardSubDetected_Type = CerCardSubType
_CerCardSubDetected_Object = MibTableColumn
cerCardSubDetected = _CerCardSubDetected_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 12, 1, 21),
    _CerCardSubDetected_Type()
)
cerCardSubDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerCardSubDetected.setStatus("current")


class _CerCardFwUpdateStatus_Type(TruthValue):
    """Custom type cerCardFwUpdateStatus based on TruthValue"""


_CerCardFwUpdateStatus_Object = MibTableColumn
cerCardFwUpdateStatus = _CerCardFwUpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 12, 1, 23),
    _CerCardFwUpdateStatus_Type()
)
cerCardFwUpdateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerCardFwUpdateStatus.setStatus("current")
_CerCardSpareGroupId_Type = CardId
_CerCardSpareGroupId_Object = MibTableColumn
cerCardSpareGroupId = _CerCardSpareGroupId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 12, 1, 24),
    _CerCardSpareGroupId_Type()
)
cerCardSpareGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cerCardSpareGroupId.setStatus("current")


class _CerCardSpareGroupMode_Type(Integer32):
    """Custom type cerCardSpareGroupMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("invalid", 0),
          ("manual", 1))
    )


_CerCardSpareGroupMode_Type.__name__ = "Integer32"
_CerCardSpareGroupMode_Object = MibTableColumn
cerCardSpareGroupMode = _CerCardSpareGroupMode_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 12, 1, 25),
    _CerCardSpareGroupMode_Type()
)
cerCardSpareGroupMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cerCardSpareGroupMode.setStatus("current")
_CerCardUpTime_Type = TimeTicks
_CerCardUpTime_Object = MibTableColumn
cerCardUpTime = _CerCardUpTime_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 12, 1, 26),
    _CerCardUpTime_Type()
)
cerCardUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerCardUpTime.setStatus("current")


class _CerCardTemperature_Type(Integer32):
    """Custom type cerCardTemperature based on Integer32"""
    defaultValue = 999

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
        ValueRangeConstraint(999, 999),
    )


_CerCardTemperature_Type.__name__ = "Integer32"
_CerCardTemperature_Object = MibTableColumn
cerCardTemperature = _CerCardTemperature_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 12, 1, 29),
    _CerCardTemperature_Type()
)
cerCardTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerCardTemperature.setStatus("current")


class _CerCardPicDetected_Type(CerPicType):
    """Custom type cerCardPicDetected based on CerPicType"""


_CerCardPicDetected_Object = MibTableColumn
cerCardPicDetected = _CerCardPicDetected_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 12, 1, 40),
    _CerCardPicDetected_Type()
)
cerCardPicDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerCardPicDetected.setStatus("current")


class _CerCardLastResetReason_Type(DisplayString):
    """Custom type cerCardLastResetReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CerCardLastResetReason_Type.__name__ = "DisplayString"
_CerCardLastResetReason_Object = MibTableColumn
cerCardLastResetReason = _CerCardLastResetReason_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 12, 1, 43),
    _CerCardLastResetReason_Type()
)
cerCardLastResetReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerCardLastResetReason.setStatus("current")


class _CerCardTemperatureHighWarn_Type(Integer32):
    """Custom type cerCardTemperatureHighWarn based on Integer32"""
    defaultValue = 7


_CerCardTemperatureHighWarn_Object = MibTableColumn
cerCardTemperatureHighWarn = _CerCardTemperatureHighWarn_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 12, 1, 44),
    _CerCardTemperatureHighWarn_Type()
)
cerCardTemperatureHighWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cerCardTemperatureHighWarn.setStatus("current")


class _CerCardTemperatureHighError_Type(Integer32):
    """Custom type cerCardTemperatureHighError based on Integer32"""
    defaultValue = 10


_CerCardTemperatureHighError_Object = MibTableColumn
cerCardTemperatureHighError = _CerCardTemperatureHighError_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 12, 1, 45),
    _CerCardTemperatureHighError_Type()
)
cerCardTemperatureHighError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cerCardTemperatureHighError.setStatus("current")


class _CerCardAnnex_Type(Integer32):
    """Custom type cerCardAnnex based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("annexA", 3),
          ("annexB", 4),
          ("annexC", 5),
          ("other", 2),
          ("unknown", 1))
    )


_CerCardAnnex_Type.__name__ = "Integer32"
_CerCardAnnex_Object = MibTableColumn
cerCardAnnex = _CerCardAnnex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 12, 1, 46),
    _CerCardAnnex_Type()
)
cerCardAnnex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerCardAnnex.setStatus("current")


class _CerCardNumRfConnectors_Type(Integer32):
    """Custom type cerCardNumRfConnectors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 48),
    )


_CerCardNumRfConnectors_Type.__name__ = "Integer32"
_CerCardNumRfConnectors_Object = MibTableColumn
cerCardNumRfConnectors = _CerCardNumRfConnectors_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 12, 1, 47),
    _CerCardNumRfConnectors_Type()
)
cerCardNumRfConnectors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerCardNumRfConnectors.setStatus("current")
_CerPortTable_Object = MibTable
cerPortTable = _CerPortTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 13)
)
if mibBuilder.loadTexts:
    cerPortTable.setStatus("current")
_CerPortEntry_Object = MibTableRow
cerPortEntry = _CerPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 13, 1)
)
cerPortEntry.setIndexNames(
    (0, "CADANT-CMTS-EQUIPMENT-MIB", "cerPortCardId"),
    (0, "CADANT-CMTS-EQUIPMENT-MIB", "cerPortId"),
)
if mibBuilder.loadTexts:
    cerPortEntry.setStatus("current")
_CerPortCardId_Type = CardId
_CerPortCardId_Object = MibTableColumn
cerPortCardId = _CerPortCardId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 13, 1, 2),
    _CerPortCardId_Type()
)
cerPortCardId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cerPortCardId.setStatus("current")
_CerPortId_Type = PortId
_CerPortId_Object = MibTableColumn
cerPortId = _CerPortId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 13, 1, 3),
    _CerPortId_Type()
)
cerPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cerPortId.setStatus("current")
_CerPortType_Type = CerPortType
_CerPortType_Object = MibTableColumn
cerPortType = _CerPortType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 13, 1, 4),
    _CerPortType_Type()
)
cerPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cerPortType.setStatus("current")
_CerPortAdminState_Type = AdminState
_CerPortAdminState_Object = MibTableColumn
cerPortAdminState = _CerPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 13, 1, 6),
    _CerPortAdminState_Type()
)
cerPortAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cerPortAdminState.setStatus("current")
_CerPortPrState_Type = PrimaryState
_CerPortPrState_Object = MibTableColumn
cerPortPrState = _CerPortPrState_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 13, 1, 7),
    _CerPortPrState_Type()
)
cerPortPrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerPortPrState.setStatus("current")
_CerPortSecState_Type = SecondaryState
_CerPortSecState_Object = MibTableColumn
cerPortSecState = _CerPortSecState_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 13, 1, 8),
    _CerPortSecState_Type()
)
cerPortSecState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerPortSecState.setStatus("current")
_CerPortDplxStatus_Type = DuplexStatus
_CerPortDplxStatus_Object = MibTableColumn
cerPortDplxStatus = _CerPortDplxStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 13, 1, 9),
    _CerPortDplxStatus_Type()
)
cerPortDplxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerPortDplxStatus.setStatus("current")
_CerPortAction_Type = EqActionType
_CerPortAction_Object = MibTableColumn
cerPortAction = _CerPortAction_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 13, 1, 11),
    _CerPortAction_Type()
)
cerPortAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cerPortAction.setStatus("current")


class _CerPortTrapInh_Type(Bits):
    """Custom type cerPortTrapInh based on Bits"""
    namedValues = NamedValues(
        *(("duplex", 2),
          ("linkUpLinkDown", 3),
          ("primary", 0),
          ("secondary", 1))
    )

_CerPortTrapInh_Type.__name__ = "Bits"
_CerPortTrapInh_Object = MibTableColumn
cerPortTrapInh = _CerPortTrapInh_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 13, 1, 12),
    _CerPortTrapInh_Type()
)
cerPortTrapInh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cerPortTrapInh.setStatus("current")


class _CerPortNumChans_Type(Integer32):
    """Custom type cerPortNumChans based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_CerPortNumChans_Type.__name__ = "Integer32"
_CerPortNumChans_Object = MibTableColumn
cerPortNumChans = _CerPortNumChans_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 13, 1, 13),
    _CerPortNumChans_Type()
)
cerPortNumChans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerPortNumChans.setStatus("current")
_CerPortDocsIfIndex_Type = InterfaceIndexOrZero
_CerPortDocsIfIndex_Object = MibTableColumn
cerPortDocsIfIndex = _CerPortDocsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 13, 1, 14),
    _CerPortDocsIfIndex_Type()
)
cerPortDocsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerPortDocsIfIndex.setStatus("current")
_CerPortMacAddress_Type = MacAddress
_CerPortMacAddress_Object = MibTableColumn
cerPortMacAddress = _CerPortMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 13, 1, 15),
    _CerPortMacAddress_Type()
)
cerPortMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerPortMacAddress.setStatus("current")


class _CerPortMode_Type(PortMode):
    """Custom type cerPortMode based on PortMode"""


_CerPortMode_Object = MibTableColumn
cerPortMode = _CerPortMode_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 13, 1, 16),
    _CerPortMode_Type()
)
cerPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cerPortMode.setStatus("current")
_CerPortDetectedMode_Type = PortDetectedMode
_CerPortDetectedMode_Object = MibTableColumn
cerPortDetectedMode = _CerPortDetectedMode_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 13, 1, 17),
    _CerPortDetectedMode_Type()
)
cerPortDetectedMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerPortDetectedMode.setStatus("current")


class _CerPortBgpId_Type(Integer32):
    """Custom type cerPortBgpId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483647, 2147483647),
    )


_CerPortBgpId_Type.__name__ = "Integer32"
_CerPortBgpId_Object = MibTableColumn
cerPortBgpId = _CerPortBgpId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 13, 1, 19),
    _CerPortBgpId_Type()
)
cerPortBgpId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerPortBgpId.setStatus("current")


class _CerPortConnectorId_Type(PortId):
    """Custom type cerPortConnectorId based on PortId"""
    defaultValue = 0


_CerPortConnectorId_Object = MibTableColumn
cerPortConnectorId = _CerPortConnectorId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 13, 1, 20),
    _CerPortConnectorId_Type()
)
cerPortConnectorId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cerPortConnectorId.setStatus("current")
_CerPortCardSubType_Type = CerCardSubType
_CerPortCardSubType_Object = MibTableColumn
cerPortCardSubType = _CerPortCardSubType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 13, 1, 21),
    _CerPortCardSubType_Type()
)
cerPortCardSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerPortCardSubType.setStatus("current")


class _CerPortDescription_Type(DisplayString):
    """Custom type cerPortDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CerPortDescription_Type.__name__ = "DisplayString"
_CerPortDescription_Object = MibTableColumn
cerPortDescription = _CerPortDescription_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 13, 1, 27),
    _CerPortDescription_Type()
)
cerPortDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cerPortDescription.setStatus("current")


class _CerPortCurrDsPower_Type(TenthdBmV):
    """Custom type cerPortCurrDsPower based on TenthdBmV"""
    defaultValue = 0


_CerPortCurrDsPower_Object = MibTableColumn
cerPortCurrDsPower = _CerPortCurrDsPower_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 13, 1, 28),
    _CerPortCurrDsPower_Type()
)
cerPortCurrDsPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerPortCurrDsPower.setStatus("current")


class _CerPortMinDsPower_Type(TenthdBmV):
    """Custom type cerPortMinDsPower based on TenthdBmV"""
    defaultValue = 0


_CerPortMinDsPower_Object = MibTableColumn
cerPortMinDsPower = _CerPortMinDsPower_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 13, 1, 29),
    _CerPortMinDsPower_Type()
)
cerPortMinDsPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerPortMinDsPower.setStatus("current")


class _CerPortMaxDsPower_Type(TenthdBmV):
    """Custom type cerPortMaxDsPower based on TenthdBmV"""
    defaultValue = 0


_CerPortMaxDsPower_Object = MibTableColumn
cerPortMaxDsPower = _CerPortMaxDsPower_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 13, 1, 30),
    _CerPortMaxDsPower_Type()
)
cerPortMaxDsPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerPortMaxDsPower.setStatus("current")


class _CerPortTxFlowControlMode_Type(FlowControlMode):
    """Custom type cerPortTxFlowControlMode based on FlowControlMode"""


_CerPortTxFlowControlMode_Object = MibTableColumn
cerPortTxFlowControlMode = _CerPortTxFlowControlMode_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 13, 1, 31),
    _CerPortTxFlowControlMode_Type()
)
cerPortTxFlowControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cerPortTxFlowControlMode.setStatus("current")


class _CerPortRxFlowControlMode_Type(FlowControlMode):
    """Custom type cerPortRxFlowControlMode based on FlowControlMode"""


_CerPortRxFlowControlMode_Object = MibTableColumn
cerPortRxFlowControlMode = _CerPortRxFlowControlMode_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 13, 1, 32),
    _CerPortRxFlowControlMode_Type()
)
cerPortRxFlowControlMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cerPortRxFlowControlMode.setStatus("current")


class _CerPortTxFlowControlDetected_Type(FlowControlMode):
    """Custom type cerPortTxFlowControlDetected based on FlowControlMode"""


_CerPortTxFlowControlDetected_Object = MibTableColumn
cerPortTxFlowControlDetected = _CerPortTxFlowControlDetected_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 13, 1, 33),
    _CerPortTxFlowControlDetected_Type()
)
cerPortTxFlowControlDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerPortTxFlowControlDetected.setStatus("current")


class _CerPortRxFlowControlDetected_Type(FlowControlMode):
    """Custom type cerPortRxFlowControlDetected based on FlowControlMode"""


_CerPortRxFlowControlDetected_Object = MibTableColumn
cerPortRxFlowControlDetected = _CerPortRxFlowControlDetected_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 13, 1, 34),
    _CerPortRxFlowControlDetected_Type()
)
cerPortRxFlowControlDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerPortRxFlowControlDetected.setStatus("current")


class _CerPortMacIfIndex_Type(InterfaceIndexOrZero):
    """Custom type cerPortMacIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_CerPortMacIfIndex_Object = MibTableColumn
cerPortMacIfIndex = _CerPortMacIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 13, 1, 35),
    _CerPortMacIfIndex_Type()
)
cerPortMacIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerPortMacIfIndex.setStatus("current")
_CerPortGroupId_Type = PortId
_CerPortGroupId_Object = MibTableColumn
cerPortGroupId = _CerPortGroupId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 13, 1, 36),
    _CerPortGroupId_Type()
)
cerPortGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerPortGroupId.setStatus("current")
_CerPortGroupPortId_Type = PortId
_CerPortGroupPortId_Object = MibTableColumn
cerPortGroupPortId = _CerPortGroupPortId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 13, 1, 37),
    _CerPortGroupPortId_Type()
)
cerPortGroupPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerPortGroupPortId.setStatus("current")
_CerDiskVolumeTable_Object = MibTable
cerDiskVolumeTable = _CerDiskVolumeTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 14)
)
if mibBuilder.loadTexts:
    cerDiskVolumeTable.setStatus("current")
_CerDiskVolumeEntry_Object = MibTableRow
cerDiskVolumeEntry = _CerDiskVolumeEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 14, 1)
)
cerDiskVolumeEntry.setIndexNames(
    (0, "CADANT-CMTS-EQUIPMENT-MIB", "cerDiskVolumeCardId"),
    (0, "CADANT-CMTS-EQUIPMENT-MIB", "cerDiskVolumeDriveId"),
    (0, "CADANT-CMTS-EQUIPMENT-MIB", "cerDiskVolumeId"),
)
if mibBuilder.loadTexts:
    cerDiskVolumeEntry.setStatus("current")
_CerDiskVolumeCardId_Type = CardId
_CerDiskVolumeCardId_Object = MibTableColumn
cerDiskVolumeCardId = _CerDiskVolumeCardId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 14, 1, 2),
    _CerDiskVolumeCardId_Type()
)
cerDiskVolumeCardId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cerDiskVolumeCardId.setStatus("current")


class _CerDiskVolumeDriveId_Type(Integer32):
    """Custom type cerDiskVolumeDriveId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_CerDiskVolumeDriveId_Type.__name__ = "Integer32"
_CerDiskVolumeDriveId_Object = MibTableColumn
cerDiskVolumeDriveId = _CerDiskVolumeDriveId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 14, 1, 3),
    _CerDiskVolumeDriveId_Type()
)
cerDiskVolumeDriveId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cerDiskVolumeDriveId.setStatus("current")


class _CerDiskVolumeId_Type(Integer32):
    """Custom type cerDiskVolumeId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_CerDiskVolumeId_Type.__name__ = "Integer32"
_CerDiskVolumeId_Object = MibTableColumn
cerDiskVolumeId = _CerDiskVolumeId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 14, 1, 4),
    _CerDiskVolumeId_Type()
)
cerDiskVolumeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cerDiskVolumeId.setStatus("current")
_CerDiskVolumeName_Type = DisplayString
_CerDiskVolumeName_Object = MibTableColumn
cerDiskVolumeName = _CerDiskVolumeName_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 14, 1, 5),
    _CerDiskVolumeName_Type()
)
cerDiskVolumeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerDiskVolumeName.setStatus("current")
_CerDiskVolumeSize_Type = Integer32
_CerDiskVolumeSize_Object = MibTableColumn
cerDiskVolumeSize = _CerDiskVolumeSize_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 14, 1, 6),
    _CerDiskVolumeSize_Type()
)
cerDiskVolumeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerDiskVolumeSize.setStatus("current")
if mibBuilder.loadTexts:
    cerDiskVolumeSize.setUnits("bytes")
_CerDiskVolumeUsageLevel_Type = DiskVolumeUsageLevel
_CerDiskVolumeUsageLevel_Object = MibTableColumn
cerDiskVolumeUsageLevel = _CerDiskVolumeUsageLevel_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 14, 1, 7),
    _CerDiskVolumeUsageLevel_Type()
)
cerDiskVolumeUsageLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerDiskVolumeUsageLevel.setStatus("current")


class _CerDiskVolumeUsagePercentage_Type(Integer32):
    """Custom type cerDiskVolumeUsagePercentage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CerDiskVolumeUsagePercentage_Type.__name__ = "Integer32"
_CerDiskVolumeUsagePercentage_Object = MibTableColumn
cerDiskVolumeUsagePercentage = _CerDiskVolumeUsagePercentage_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 14, 1, 8),
    _CerDiskVolumeUsagePercentage_Type()
)
cerDiskVolumeUsagePercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerDiskVolumeUsagePercentage.setStatus("current")
if mibBuilder.loadTexts:
    cerDiskVolumeUsagePercentage.setUnits("percent")


class _CerDiskVolumeUsageCriticalThreshold_Type(Integer32):
    """Custom type cerDiskVolumeUsageCriticalThreshold based on Integer32"""
    defaultValue = 90

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CerDiskVolumeUsageCriticalThreshold_Type.__name__ = "Integer32"
_CerDiskVolumeUsageCriticalThreshold_Object = MibTableColumn
cerDiskVolumeUsageCriticalThreshold = _CerDiskVolumeUsageCriticalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 14, 1, 9),
    _CerDiskVolumeUsageCriticalThreshold_Type()
)
cerDiskVolumeUsageCriticalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cerDiskVolumeUsageCriticalThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cerDiskVolumeUsageCriticalThreshold.setUnits("percent")


class _CerDiskVolumeUsageMajorThreshold_Type(Integer32):
    """Custom type cerDiskVolumeUsageMajorThreshold based on Integer32"""
    defaultValue = 80

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CerDiskVolumeUsageMajorThreshold_Type.__name__ = "Integer32"
_CerDiskVolumeUsageMajorThreshold_Object = MibTableColumn
cerDiskVolumeUsageMajorThreshold = _CerDiskVolumeUsageMajorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 14, 1, 10),
    _CerDiskVolumeUsageMajorThreshold_Type()
)
cerDiskVolumeUsageMajorThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cerDiskVolumeUsageMajorThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cerDiskVolumeUsageMajorThreshold.setUnits("percent")


class _CerDiskVolumeUsageMinorThreshold_Type(Integer32):
    """Custom type cerDiskVolumeUsageMinorThreshold based on Integer32"""
    defaultValue = 70

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CerDiskVolumeUsageMinorThreshold_Type.__name__ = "Integer32"
_CerDiskVolumeUsageMinorThreshold_Object = MibTableColumn
cerDiskVolumeUsageMinorThreshold = _CerDiskVolumeUsageMinorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 14, 1, 11),
    _CerDiskVolumeUsageMinorThreshold_Type()
)
cerDiskVolumeUsageMinorThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cerDiskVolumeUsageMinorThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cerDiskVolumeUsageMinorThreshold.setUnits("percent")


class _CerDiskVolumeAutoDeleteUnusedFile_Type(TruthValue):
    """Custom type cerDiskVolumeAutoDeleteUnusedFile based on TruthValue"""


_CerDiskVolumeAutoDeleteUnusedFile_Object = MibTableColumn
cerDiskVolumeAutoDeleteUnusedFile = _CerDiskVolumeAutoDeleteUnusedFile_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 14, 1, 12),
    _CerDiskVolumeAutoDeleteUnusedFile_Type()
)
cerDiskVolumeAutoDeleteUnusedFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cerDiskVolumeAutoDeleteUnusedFile.setStatus("current")


class _CerDiskVolumeTrapInh_Type(Bits):
    """Custom type cerDiskVolumeTrapInh based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("autoDeleteFiles", 3),
          ("criticalUsageLevel", 0),
          ("majorUsageLevel", 1),
          ("minorUsageLevel", 2))
    )

_CerDiskVolumeTrapInh_Type.__name__ = "Bits"
_CerDiskVolumeTrapInh_Object = MibTableColumn
cerDiskVolumeTrapInh = _CerDiskVolumeTrapInh_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 14, 1, 13),
    _CerDiskVolumeTrapInh_Type()
)
cerDiskVolumeTrapInh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cerDiskVolumeTrapInh.setStatus("current")


class _CerDiskVolumeDiskSize_Type(Integer32):
    """Custom type cerDiskVolumeDiskSize based on Integer32"""
    defaultValue = 0


_CerDiskVolumeDiskSize_Object = MibTableColumn
cerDiskVolumeDiskSize = _CerDiskVolumeDiskSize_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 14, 1, 14),
    _CerDiskVolumeDiskSize_Type()
)
cerDiskVolumeDiskSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerDiskVolumeDiskSize.setStatus("current")
if mibBuilder.loadTexts:
    cerDiskVolumeDiskSize.setUnits("bytes")
_CerDiskVolumeFileName_Type = DisplayString
_CerDiskVolumeFileName_Object = MibScalar
cerDiskVolumeFileName = _CerDiskVolumeFileName_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 15),
    _CerDiskVolumeFileName_Type()
)
cerDiskVolumeFileName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cerDiskVolumeFileName.setStatus("current")
_CerCardDataTable_Object = MibTable
cerCardDataTable = _CerCardDataTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 16)
)
if mibBuilder.loadTexts:
    cerCardDataTable.setStatus("current")
_CerCardDataEntry_Object = MibTableRow
cerCardDataEntry = _CerCardDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 16, 1)
)
if mibBuilder.loadTexts:
    cerCardDataEntry.setStatus("current")


class _CerCardDataSerialNum_Type(SnmpAdminString):
    """Custom type cerCardDataSerialNum based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CerCardDataSerialNum_Type.__name__ = "SnmpAdminString"
_CerCardDataSerialNum_Object = MibTableColumn
cerCardDataSerialNum = _CerCardDataSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 16, 1, 1),
    _CerCardDataSerialNum_Type()
)
cerCardDataSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerCardDataSerialNum.setStatus("current")


class _CerCardDataFwVersion_Type(SnmpAdminString):
    """Custom type cerCardDataFwVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CerCardDataFwVersion_Type.__name__ = "SnmpAdminString"
_CerCardDataFwVersion_Object = MibTableColumn
cerCardDataFwVersion = _CerCardDataFwVersion_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 16, 1, 2),
    _CerCardDataFwVersion_Type()
)
cerCardDataFwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerCardDataFwVersion.setStatus("current")


class _CerCardDataHwVersion_Type(SnmpAdminString):
    """Custom type cerCardDataHwVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CerCardDataHwVersion_Type.__name__ = "SnmpAdminString"
_CerCardDataHwVersion_Object = MibTableColumn
cerCardDataHwVersion = _CerCardDataHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 16, 1, 3),
    _CerCardDataHwVersion_Type()
)
cerCardDataHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerCardDataHwVersion.setStatus("current")


class _CerCardDataHwDeviations_Type(SnmpAdminString):
    """Custom type cerCardDataHwDeviations based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CerCardDataHwDeviations_Type.__name__ = "SnmpAdminString"
_CerCardDataHwDeviations_Object = MibTableColumn
cerCardDataHwDeviations = _CerCardDataHwDeviations_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 16, 1, 4),
    _CerCardDataHwDeviations_Type()
)
cerCardDataHwDeviations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerCardDataHwDeviations.setStatus("current")


class _CerCardDataSwVersion_Type(SnmpAdminString):
    """Custom type cerCardDataSwVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CerCardDataSwVersion_Type.__name__ = "SnmpAdminString"
_CerCardDataSwVersion_Object = MibTableColumn
cerCardDataSwVersion = _CerCardDataSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 16, 1, 5),
    _CerCardDataSwVersion_Type()
)
cerCardDataSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerCardDataSwVersion.setStatus("current")


class _CerCardDataCpuType_Type(SnmpAdminString):
    """Custom type cerCardDataCpuType based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 25),
    )


_CerCardDataCpuType_Type.__name__ = "SnmpAdminString"
_CerCardDataCpuType_Object = MibTableColumn
cerCardDataCpuType = _CerCardDataCpuType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 16, 1, 6),
    _CerCardDataCpuType_Type()
)
cerCardDataCpuType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerCardDataCpuType.setStatus("current")


class _CerCardDataCpuSpeed_Type(Unsigned32):
    """Custom type cerCardDataCpuSpeed based on Unsigned32"""
    defaultValue = 0


_CerCardDataCpuSpeed_Object = MibTableColumn
cerCardDataCpuSpeed = _CerCardDataCpuSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 16, 1, 7),
    _CerCardDataCpuSpeed_Type()
)
cerCardDataCpuSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerCardDataCpuSpeed.setStatus("current")
if mibBuilder.loadTexts:
    cerCardDataCpuSpeed.setUnits("MHz")


class _CerCardDataBusSpeed_Type(Unsigned32):
    """Custom type cerCardDataBusSpeed based on Unsigned32"""
    defaultValue = 0


_CerCardDataBusSpeed_Object = MibTableColumn
cerCardDataBusSpeed = _CerCardDataBusSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 16, 1, 8),
    _CerCardDataBusSpeed_Type()
)
cerCardDataBusSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerCardDataBusSpeed.setStatus("current")
if mibBuilder.loadTexts:
    cerCardDataBusSpeed.setUnits("hertz")


class _CerCardDataRamSize_Type(Unsigned32):
    """Custom type cerCardDataRamSize based on Unsigned32"""
    defaultValue = 0


_CerCardDataRamSize_Object = MibTableColumn
cerCardDataRamSize = _CerCardDataRamSize_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 16, 1, 9),
    _CerCardDataRamSize_Type()
)
cerCardDataRamSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerCardDataRamSize.setStatus("current")
if mibBuilder.loadTexts:
    cerCardDataRamSize.setUnits("megabytes")


class _CerCardDataNorFlashSize_Type(Unsigned32):
    """Custom type cerCardDataNorFlashSize based on Unsigned32"""
    defaultValue = 0


_CerCardDataNorFlashSize_Object = MibTableColumn
cerCardDataNorFlashSize = _CerCardDataNorFlashSize_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 16, 1, 10),
    _CerCardDataNorFlashSize_Type()
)
cerCardDataNorFlashSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerCardDataNorFlashSize.setStatus("current")
if mibBuilder.loadTexts:
    cerCardDataNorFlashSize.setUnits("bytes")


class _CerCardDataNandFlashSize_Type(Unsigned32):
    """Custom type cerCardDataNandFlashSize based on Unsigned32"""
    defaultValue = 0


_CerCardDataNandFlashSize_Object = MibTableColumn
cerCardDataNandFlashSize = _CerCardDataNandFlashSize_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 16, 1, 11),
    _CerCardDataNandFlashSize_Type()
)
cerCardDataNandFlashSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerCardDataNandFlashSize.setStatus("current")
if mibBuilder.loadTexts:
    cerCardDataNandFlashSize.setUnits("bytes")


class _CerCardDataFpgaSource_Type(FirmwareSource):
    """Custom type cerCardDataFpgaSource based on FirmwareSource"""


_CerCardDataFpgaSource_Object = MibTableColumn
cerCardDataFpgaSource = _CerCardDataFpgaSource_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 16, 1, 12),
    _CerCardDataFpgaSource_Type()
)
cerCardDataFpgaSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerCardDataFpgaSource.setStatus("current")


class _CerCardDataBootVersion_Type(SnmpAdminString):
    """Custom type cerCardDataBootVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 90),
    )


_CerCardDataBootVersion_Type.__name__ = "SnmpAdminString"
_CerCardDataBootVersion_Object = MibTableColumn
cerCardDataBootVersion = _CerCardDataBootVersion_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 16, 1, 13),
    _CerCardDataBootVersion_Type()
)
cerCardDataBootVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerCardDataBootVersion.setStatus("current")


class _CerCardDataLastBootVersion_Type(SnmpAdminString):
    """Custom type cerCardDataLastBootVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 90),
    )


_CerCardDataLastBootVersion_Type.__name__ = "SnmpAdminString"
_CerCardDataLastBootVersion_Object = MibTableColumn
cerCardDataLastBootVersion = _CerCardDataLastBootVersion_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 16, 1, 14),
    _CerCardDataLastBootVersion_Type()
)
cerCardDataLastBootVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerCardDataLastBootVersion.setStatus("current")


class _CerCardDataLastBootSource_Type(FirmwareSource):
    """Custom type cerCardDataLastBootSource based on FirmwareSource"""


_CerCardDataLastBootSource_Object = MibTableColumn
cerCardDataLastBootSource = _CerCardDataLastBootSource_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 16, 1, 15),
    _CerCardDataLastBootSource_Type()
)
cerCardDataLastBootSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerCardDataLastBootSource.setStatus("current")


class _CerCardDataPicSerialNum_Type(SnmpAdminString):
    """Custom type cerCardDataPicSerialNum based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CerCardDataPicSerialNum_Type.__name__ = "SnmpAdminString"
_CerCardDataPicSerialNum_Object = MibTableColumn
cerCardDataPicSerialNum = _CerCardDataPicSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 16, 1, 16),
    _CerCardDataPicSerialNum_Type()
)
cerCardDataPicSerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerCardDataPicSerialNum.setStatus("current")


class _CerCardDataPicHwVersion_Type(SnmpAdminString):
    """Custom type cerCardDataPicHwVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CerCardDataPicHwVersion_Type.__name__ = "SnmpAdminString"
_CerCardDataPicHwVersion_Object = MibTableColumn
cerCardDataPicHwVersion = _CerCardDataPicHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 16, 1, 17),
    _CerCardDataPicHwVersion_Type()
)
cerCardDataPicHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerCardDataPicHwVersion.setStatus("current")


class _CerCardDataPicHwDeviations_Type(SnmpAdminString):
    """Custom type cerCardDataPicHwDeviations based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CerCardDataPicHwDeviations_Type.__name__ = "SnmpAdminString"
_CerCardDataPicHwDeviations_Object = MibTableColumn
cerCardDataPicHwDeviations = _CerCardDataPicHwDeviations_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 16, 1, 18),
    _CerCardDataPicHwDeviations_Type()
)
cerCardDataPicHwDeviations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerCardDataPicHwDeviations.setStatus("current")


class _CerCardDataPicModelNum_Type(SnmpAdminString):
    """Custom type cerCardDataPicModelNum based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CerCardDataPicModelNum_Type.__name__ = "SnmpAdminString"
_CerCardDataPicModelNum_Object = MibTableColumn
cerCardDataPicModelNum = _CerCardDataPicModelNum_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 16, 1, 19),
    _CerCardDataPicModelNum_Type()
)
cerCardDataPicModelNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerCardDataPicModelNum.setStatus("current")


class _CerCardDataMfgDateTime_Type(DateAndTime):
    """Custom type cerCardDataMfgDateTime based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_CerCardDataMfgDateTime_Object = MibTableColumn
cerCardDataMfgDateTime = _CerCardDataMfgDateTime_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 16, 1, 20),
    _CerCardDataMfgDateTime_Type()
)
cerCardDataMfgDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerCardDataMfgDateTime.setStatus("current")


class _CerCardDataMfg_Type(SnmpAdminString):
    """Custom type cerCardDataMfg based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CerCardDataMfg_Type.__name__ = "SnmpAdminString"
_CerCardDataMfg_Object = MibTableColumn
cerCardDataMfg = _CerCardDataMfg_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 16, 1, 21),
    _CerCardDataMfg_Type()
)
cerCardDataMfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerCardDataMfg.setStatus("current")


class _CerCardDataProductName_Type(SnmpAdminString):
    """Custom type cerCardDataProductName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CerCardDataProductName_Type.__name__ = "SnmpAdminString"
_CerCardDataProductName_Object = MibTableColumn
cerCardDataProductName = _CerCardDataProductName_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 16, 1, 22),
    _CerCardDataProductName_Type()
)
cerCardDataProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerCardDataProductName.setStatus("current")


class _CerCardDataPartModelNum_Type(SnmpAdminString):
    """Custom type cerCardDataPartModelNum based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CerCardDataPartModelNum_Type.__name__ = "SnmpAdminString"
_CerCardDataPartModelNum_Object = MibTableColumn
cerCardDataPartModelNum = _CerCardDataPartModelNum_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 16, 1, 23),
    _CerCardDataPartModelNum_Type()
)
cerCardDataPartModelNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerCardDataPartModelNum.setStatus("current")


class _CerCardDataProductVersion_Type(SnmpAdminString):
    """Custom type cerCardDataProductVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CerCardDataProductVersion_Type.__name__ = "SnmpAdminString"
_CerCardDataProductVersion_Object = MibTableColumn
cerCardDataProductVersion = _CerCardDataProductVersion_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 16, 1, 24),
    _CerCardDataProductVersion_Type()
)
cerCardDataProductVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerCardDataProductVersion.setStatus("current")


class _CerCardDataAssetTag_Type(SnmpAdminString):
    """Custom type cerCardDataAssetTag based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CerCardDataAssetTag_Type.__name__ = "SnmpAdminString"
_CerCardDataAssetTag_Object = MibTableColumn
cerCardDataAssetTag = _CerCardDataAssetTag_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 16, 1, 25),
    _CerCardDataAssetTag_Type()
)
cerCardDataAssetTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerCardDataAssetTag.setStatus("current")


class _CerCardDataCommittedSwVersion_Type(SnmpAdminString):
    """Custom type cerCardDataCommittedSwVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CerCardDataCommittedSwVersion_Type.__name__ = "SnmpAdminString"
_CerCardDataCommittedSwVersion_Object = MibTableColumn
cerCardDataCommittedSwVersion = _CerCardDataCommittedSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 16, 1, 26),
    _CerCardDataCommittedSwVersion_Type()
)
cerCardDataCommittedSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerCardDataCommittedSwVersion.setStatus("current")


class _CerCardDataFeedAPresent_Type(TruthValue):
    """Custom type cerCardDataFeedAPresent based on TruthValue"""


_CerCardDataFeedAPresent_Object = MibTableColumn
cerCardDataFeedAPresent = _CerCardDataFeedAPresent_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 16, 1, 27),
    _CerCardDataFeedAPresent_Type()
)
cerCardDataFeedAPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerCardDataFeedAPresent.setStatus("current")


class _CerCardDataFeedBPresent_Type(TruthValue):
    """Custom type cerCardDataFeedBPresent based on TruthValue"""


_CerCardDataFeedBPresent_Object = MibTableColumn
cerCardDataFeedBPresent = _CerCardDataFeedBPresent_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 16, 1, 28),
    _CerCardDataFeedBPresent_Type()
)
cerCardDataFeedBPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerCardDataFeedBPresent.setStatus("current")


class _CerCardDataAllowedPorts_Type(Unsigned32):
    """Custom type cerCardDataAllowedPorts based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_CerCardDataAllowedPorts_Type.__name__ = "Unsigned32"
_CerCardDataAllowedPorts_Object = MibTableColumn
cerCardDataAllowedPorts = _CerCardDataAllowedPorts_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 16, 1, 29),
    _CerCardDataAllowedPorts_Type()
)
cerCardDataAllowedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerCardDataAllowedPorts.setStatus("current")


class _CerCardDataLicenseAnnex_Type(Integer32):
    """Custom type cerCardDataLicenseAnnex based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("annexA", 3),
          ("annexB", 4),
          ("annexC", 5),
          ("other", 2),
          ("unknown", 1))
    )


_CerCardDataLicenseAnnex_Type.__name__ = "Integer32"
_CerCardDataLicenseAnnex_Object = MibTableColumn
cerCardDataLicenseAnnex = _CerCardDataLicenseAnnex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 16, 1, 30),
    _CerCardDataLicenseAnnex_Type()
)
cerCardDataLicenseAnnex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerCardDataLicenseAnnex.setStatus("current")


class _CerCardDataLicensePorts_Type(Unsigned32):
    """Custom type cerCardDataLicensePorts based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_CerCardDataLicensePorts_Type.__name__ = "Unsigned32"
_CerCardDataLicensePorts_Object = MibTableColumn
cerCardDataLicensePorts = _CerCardDataLicensePorts_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 16, 1, 31),
    _CerCardDataLicensePorts_Type()
)
cerCardDataLicensePorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerCardDataLicensePorts.setStatus("current")


class _CerCardDataLicenseDate_Type(DateAndTime):
    """Custom type cerCardDataLicenseDate based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_CerCardDataLicenseDate_Object = MibTableColumn
cerCardDataLicenseDate = _CerCardDataLicenseDate_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 16, 1, 32),
    _CerCardDataLicenseDate_Type()
)
cerCardDataLicenseDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerCardDataLicenseDate.setStatus("current")


class _CerCardDataPatchVersions_Type(SnmpAdminString):
    """Custom type cerCardDataPatchVersions based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CerCardDataPatchVersions_Type.__name__ = "SnmpAdminString"
_CerCardDataPatchVersions_Object = MibTableColumn
cerCardDataPatchVersions = _CerCardDataPatchVersions_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 16, 1, 33),
    _CerCardDataPatchVersions_Type()
)
cerCardDataPatchVersions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerCardDataPatchVersions.setStatus("current")


class _CerCardDataPicModelName_Type(SnmpAdminString):
    """Custom type cerCardDataPicModelName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CerCardDataPicModelName_Type.__name__ = "SnmpAdminString"
_CerCardDataPicModelName_Object = MibTableColumn
cerCardDataPicModelName = _CerCardDataPicModelName_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 16, 1, 34),
    _CerCardDataPicModelName_Type()
)
cerCardDataPicModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerCardDataPicModelName.setStatus("current")


class _CerCardDataPicMfgRevision_Type(SnmpAdminString):
    """Custom type cerCardDataPicMfgRevision based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CerCardDataPicMfgRevision_Type.__name__ = "SnmpAdminString"
_CerCardDataPicMfgRevision_Object = MibTableColumn
cerCardDataPicMfgRevision = _CerCardDataPicMfgRevision_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 16, 1, 35),
    _CerCardDataPicMfgRevision_Type()
)
cerCardDataPicMfgRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerCardDataPicMfgRevision.setStatus("current")


class _CerCardDataPicMfg_Type(SnmpAdminString):
    """Custom type cerCardDataPicMfg based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CerCardDataPicMfg_Type.__name__ = "SnmpAdminString"
_CerCardDataPicMfg_Object = MibTableColumn
cerCardDataPicMfg = _CerCardDataPicMfg_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 16, 1, 36),
    _CerCardDataPicMfg_Type()
)
cerCardDataPicMfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerCardDataPicMfg.setStatus("current")


class _CerCardDataPicMfgDateTime_Type(DateAndTime):
    """Custom type cerCardDataPicMfgDateTime based on DateAndTime"""
    defaultHexValue = "0000000000000000"


_CerCardDataPicMfgDateTime_Object = MibTableColumn
cerCardDataPicMfgDateTime = _CerCardDataPicMfgDateTime_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 16, 1, 37),
    _CerCardDataPicMfgDateTime_Type()
)
cerCardDataPicMfgDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerCardDataPicMfgDateTime.setStatus("current")
_CerFanStatusTable_Object = MibTable
cerFanStatusTable = _CerFanStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 17)
)
if mibBuilder.loadTexts:
    cerFanStatusTable.setStatus("current")
_CerFanStatusEntry_Object = MibTableRow
cerFanStatusEntry = _CerFanStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 17, 1)
)
cerFanStatusEntry.setIndexNames(
    (0, "CADANT-CMTS-EQUIPMENT-MIB", "cerCardId"),
)
if mibBuilder.loadTexts:
    cerFanStatusEntry.setStatus("current")


class _CerFan1Speed_Type(Integer32):
    """Custom type cerFan1Speed based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CerFan1Speed_Type.__name__ = "Integer32"
_CerFan1Speed_Object = MibTableColumn
cerFan1Speed = _CerFan1Speed_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 17, 1, 1),
    _CerFan1Speed_Type()
)
cerFan1Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerFan1Speed.setStatus("current")
if mibBuilder.loadTexts:
    cerFan1Speed.setUnits("rpm")


class _CerFan2Speed_Type(Integer32):
    """Custom type cerFan2Speed based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CerFan2Speed_Type.__name__ = "Integer32"
_CerFan2Speed_Object = MibTableColumn
cerFan2Speed = _CerFan2Speed_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 17, 1, 2),
    _CerFan2Speed_Type()
)
cerFan2Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerFan2Speed.setStatus("current")
if mibBuilder.loadTexts:
    cerFan2Speed.setUnits("rpm")


class _CerFan3Speed_Type(Integer32):
    """Custom type cerFan3Speed based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CerFan3Speed_Type.__name__ = "Integer32"
_CerFan3Speed_Object = MibTableColumn
cerFan3Speed = _CerFan3Speed_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 17, 1, 3),
    _CerFan3Speed_Type()
)
cerFan3Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerFan3Speed.setStatus("current")
if mibBuilder.loadTexts:
    cerFan3Speed.setUnits("rpm")


class _CerFanLevel_Type(Integer32):
    """Custom type cerFanLevel based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CerFanLevel_Type.__name__ = "Integer32"
_CerFanLevel_Object = MibTableColumn
cerFanLevel = _CerFanLevel_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 17, 1, 4),
    _CerFanLevel_Type()
)
cerFanLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerFanLevel.setStatus("current")


class _CerFanAmbientTemperature_Type(Integer32):
    """Custom type cerFanAmbientTemperature based on Integer32"""
    defaultValue = 0


_CerFanAmbientTemperature_Object = MibTableColumn
cerFanAmbientTemperature = _CerFanAmbientTemperature_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 17, 1, 5),
    _CerFanAmbientTemperature_Type()
)
cerFanAmbientTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerFanAmbientTemperature.setStatus("current")
if mibBuilder.loadTexts:
    cerFanAmbientTemperature.setUnits("degrees C")
_CerPemStatusTable_Object = MibTable
cerPemStatusTable = _CerPemStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 18)
)
if mibBuilder.loadTexts:
    cerPemStatusTable.setStatus("current")
_CerPemStatusEntry_Object = MibTableRow
cerPemStatusEntry = _CerPemStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 18, 1)
)
cerPemStatusEntry.setIndexNames(
    (0, "CADANT-CMTS-EQUIPMENT-MIB", "cerCardId"),
)
if mibBuilder.loadTexts:
    cerPemStatusEntry.setStatus("current")


class _CerPemLedStatus_Type(Integer32):
    """Custom type cerPemLedStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 2),
          ("normal", 1))
    )


_CerPemLedStatus_Type.__name__ = "Integer32"
_CerPemLedStatus_Object = MibTableColumn
cerPemLedStatus = _CerPemLedStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 18, 1, 1),
    _CerPemLedStatus_Type()
)
cerPemLedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerPemLedStatus.setStatus("current")
_CerPemFeed1Voltage_Type = Integer32
_CerPemFeed1Voltage_Object = MibTableColumn
cerPemFeed1Voltage = _CerPemFeed1Voltage_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 18, 1, 2),
    _CerPemFeed1Voltage_Type()
)
cerPemFeed1Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerPemFeed1Voltage.setStatus("current")
if mibBuilder.loadTexts:
    cerPemFeed1Voltage.setUnits("decivolt")
_CerPemFeed1Current_Type = Integer32
_CerPemFeed1Current_Object = MibTableColumn
cerPemFeed1Current = _CerPemFeed1Current_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 18, 1, 3),
    _CerPemFeed1Current_Type()
)
cerPemFeed1Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerPemFeed1Current.setStatus("current")
if mibBuilder.loadTexts:
    cerPemFeed1Current.setUnits("deciiamp")
_CerPemFeed2Voltage_Type = Integer32
_CerPemFeed2Voltage_Object = MibTableColumn
cerPemFeed2Voltage = _CerPemFeed2Voltage_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 18, 1, 4),
    _CerPemFeed2Voltage_Type()
)
cerPemFeed2Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerPemFeed2Voltage.setStatus("current")
if mibBuilder.loadTexts:
    cerPemFeed2Voltage.setUnits("decivolt")
_CerPemFeed2Current_Type = Integer32
_CerPemFeed2Current_Object = MibTableColumn
cerPemFeed2Current = _CerPemFeed2Current_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 18, 1, 5),
    _CerPemFeed2Current_Type()
)
cerPemFeed2Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerPemFeed2Current.setStatus("current")
if mibBuilder.loadTexts:
    cerPemFeed2Current.setUnits("deciamp")
_CerPemFeed1Present_Type = TruthValue
_CerPemFeed1Present_Object = MibTableColumn
cerPemFeed1Present = _CerPemFeed1Present_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 18, 1, 6),
    _CerPemFeed1Present_Type()
)
cerPemFeed1Present.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerPemFeed1Present.setStatus("current")
_CerPemFeed2Present_Type = TruthValue
_CerPemFeed2Present_Object = MibTableColumn
cerPemFeed2Present = _CerPemFeed2Present_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 18, 1, 7),
    _CerPemFeed2Present_Type()
)
cerPemFeed2Present.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerPemFeed2Present.setStatus("current")
_CerPemCircuitBreaker1Enable_Type = TruthValue
_CerPemCircuitBreaker1Enable_Object = MibTableColumn
cerPemCircuitBreaker1Enable = _CerPemCircuitBreaker1Enable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 18, 1, 8),
    _CerPemCircuitBreaker1Enable_Type()
)
cerPemCircuitBreaker1Enable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerPemCircuitBreaker1Enable.setStatus("current")
_CerPemCircuitBreaker2Enable_Type = TruthValue
_CerPemCircuitBreaker2Enable_Object = MibTableColumn
cerPemCircuitBreaker2Enable = _CerPemCircuitBreaker2Enable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 18, 1, 9),
    _CerPemCircuitBreaker2Enable_Type()
)
cerPemCircuitBreaker2Enable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerPemCircuitBreaker2Enable.setStatus("current")


class _CerPemBranchPresent_Type(Bits):
    """Custom type cerPemBranchPresent based on Bits"""
    namedValues = NamedValues(
        *(("a", 0),
          ("b", 1),
          ("c", 2),
          ("d", 3),
          ("e", 4),
          ("f", 5),
          ("g", 6),
          ("h", 7),
          ("i", 8))
    )

_CerPemBranchPresent_Type.__name__ = "Bits"
_CerPemBranchPresent_Object = MibTableColumn
cerPemBranchPresent = _CerPemBranchPresent_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 4, 18, 1, 10),
    _CerPemBranchPresent_Type()
)
cerPemBranchPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerPemBranchPresent.setStatus("current")
_EquipmentDiag_ObjectIdentity = ObjectIdentity
equipmentDiag = _EquipmentDiag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 5)
)
_EqDiagConfig_ObjectIdentity = ObjectIdentity
eqDiagConfig = _EqDiagConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 5, 1)
)


class _RemainInDiagMode_Type(TruthValue):
    """Custom type remainInDiagMode based on TruthValue"""


_RemainInDiagMode_Object = MibScalar
remainInDiagMode = _RemainInDiagMode_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 5, 1, 1),
    _RemainInDiagMode_Type()
)
remainInDiagMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remainInDiagMode.setStatus("current")


class _ConsoleOutput_Type(TruthValue):
    """Custom type consoleOutput based on TruthValue"""


_ConsoleOutput_Object = MibScalar
consoleOutput = _ConsoleOutput_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 5, 1, 2),
    _ConsoleOutput_Type()
)
consoleOutput.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    consoleOutput.setStatus("obsolete")


class _VerboseLevel_Type(Integer32):
    """Custom type verboseLevel based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_VerboseLevel_Type.__name__ = "Integer32"
_VerboseLevel_Object = MibScalar
verboseLevel = _VerboseLevel_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 5, 1, 3),
    _VerboseLevel_Type()
)
verboseLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    verboseLevel.setStatus("current")
_DiagTestId_Type = TestId
_DiagTestId_Object = MibScalar
diagTestId = _DiagTestId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 5, 2),
    _DiagTestId_Type()
)
diagTestId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    diagTestId.setStatus("current")
_CardTestTable_Object = MibTable
cardTestTable = _CardTestTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 5, 3)
)
if mibBuilder.loadTexts:
    cardTestTable.setStatus("current")
_CardTestEntry_Object = MibTableRow
cardTestEntry = _CardTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 5, 3, 1)
)
cardTestEntry.setIndexNames(
    (0, "CADANT-CMTS-EQUIPMENT-MIB", "cardTestIndex"),
    (0, "CADANT-CMTS-EQUIPMENT-MIB", "cardTestId"),
)
if mibBuilder.loadTexts:
    cardTestEntry.setStatus("current")
_CardTestIndex_Type = CardId
_CardTestIndex_Object = MibTableColumn
cardTestIndex = _CardTestIndex_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 5, 3, 1, 2),
    _CardTestIndex_Type()
)
cardTestIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cardTestIndex.setStatus("current")
_CardTestId_Type = TestId
_CardTestId_Object = MibTableColumn
cardTestId = _CardTestId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 5, 3, 1, 3),
    _CardTestId_Type()
)
cardTestId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cardTestId.setStatus("current")


class _CardTestName_Type(DisplayString):
    """Custom type cardTestName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_CardTestName_Type.__name__ = "DisplayString"
_CardTestName_Object = MibTableColumn
cardTestName = _CardTestName_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 5, 3, 1, 4),
    _CardTestName_Type()
)
cardTestName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardTestName.setStatus("current")


class _CardTestType_Type(TestType):
    """Custom type cardTestType based on TestType"""


_CardTestType_Object = MibTableColumn
cardTestType = _CardTestType_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 5, 3, 1, 5),
    _CardTestType_Type()
)
cardTestType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardTestType.setStatus("current")
_CardTestDescription_Type = DisplayString
_CardTestDescription_Object = MibTableColumn
cardTestDescription = _CardTestDescription_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 5, 3, 1, 6),
    _CardTestDescription_Type()
)
cardTestDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardTestDescription.setStatus("current")


class _CardTestCommand_Type(TestCommand):
    """Custom type cardTestCommand based on TestCommand"""


_CardTestCommand_Object = MibTableColumn
cardTestCommand = _CardTestCommand_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 5, 3, 1, 7),
    _CardTestCommand_Type()
)
cardTestCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardTestCommand.setStatus("current")


class _CardTestScheduleCommand_Type(TestScheduleCommand):
    """Custom type cardTestScheduleCommand based on TestScheduleCommand"""


_CardTestScheduleCommand_Object = MibTableColumn
cardTestScheduleCommand = _CardTestScheduleCommand_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 5, 3, 1, 8),
    _CardTestScheduleCommand_Type()
)
cardTestScheduleCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardTestScheduleCommand.setStatus("current")


class _CardTestSchedule_Type(TestSchedule):
    """Custom type cardTestSchedule based on TestSchedule"""
    defaultValue = 0


_CardTestSchedule_Object = MibTableColumn
cardTestSchedule = _CardTestSchedule_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 5, 3, 1, 9),
    _CardTestSchedule_Type()
)
cardTestSchedule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardTestSchedule.setStatus("current")
_CardTestTime_Type = DateAndTime
_CardTestTime_Object = MibTableColumn
cardTestTime = _CardTestTime_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 5, 3, 1, 10),
    _CardTestTime_Type()
)
cardTestTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardTestTime.setStatus("current")


class _CardTestResult_Type(TestResult):
    """Custom type cardTestResult based on TestResult"""


_CardTestResult_Object = MibTableColumn
cardTestResult = _CardTestResult_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 5, 3, 1, 11),
    _CardTestResult_Type()
)
cardTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardTestResult.setStatus("current")
_CardTestResultDesc_Type = DisplayString
_CardTestResultDesc_Object = MibTableColumn
cardTestResultDesc = _CardTestResultDesc_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 5, 3, 1, 12),
    _CardTestResultDesc_Type()
)
cardTestResultDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cardTestResultDesc.setStatus("current")
_CardTestTransId_Type = TestTransactionId
_CardTestTransId_Object = MibTableColumn
cardTestTransId = _CardTestTransId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 5, 3, 1, 13),
    _CardTestTransId_Type()
)
cardTestTransId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cardTestTransId.setStatus("current")
_EquipmentAudit_ObjectIdentity = ObjectIdentity
equipmentAudit = _EquipmentAudit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 6)
)


class _AuditAutoScheduling_Type(TruthValue):
    """Custom type auditAutoScheduling based on TruthValue"""


_AuditAutoScheduling_Object = MibScalar
auditAutoScheduling = _AuditAutoScheduling_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 6, 1),
    _AuditAutoScheduling_Type()
)
auditAutoScheduling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auditAutoScheduling.setStatus("current")


class _AuditLogOutput_Type(TruthValue):
    """Custom type auditLogOutput based on TruthValue"""


_AuditLogOutput_Object = MibScalar
auditLogOutput = _AuditLogOutput_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 6, 2),
    _AuditLogOutput_Type()
)
auditLogOutput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auditLogOutput.setStatus("current")


class _AuditLogThrottle_Type(TruthValue):
    """Custom type auditLogThrottle based on TruthValue"""


_AuditLogThrottle_Object = MibScalar
auditLogThrottle = _AuditLogThrottle_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 6, 3),
    _AuditLogThrottle_Type()
)
auditLogThrottle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auditLogThrottle.setStatus("current")
_AuditTable_Object = MibTable
auditTable = _AuditTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 6, 4)
)
if mibBuilder.loadTexts:
    auditTable.setStatus("current")
_AuditEntry_Object = MibTableRow
auditEntry = _AuditEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 6, 4, 1)
)
auditEntry.setIndexNames(
    (0, "CADANT-CMTS-EQUIPMENT-MIB", "auditCardId"),
    (0, "CADANT-CMTS-EQUIPMENT-MIB", "auditId"),
)
if mibBuilder.loadTexts:
    auditEntry.setStatus("current")
_AuditCardId_Type = CardId
_AuditCardId_Object = MibTableColumn
auditCardId = _AuditCardId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 6, 4, 1, 2),
    _AuditCardId_Type()
)
auditCardId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    auditCardId.setStatus("current")
_AuditId_Type = Unsigned32
_AuditId_Object = MibTableColumn
auditId = _AuditId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 6, 4, 1, 3),
    _AuditId_Type()
)
auditId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    auditId.setStatus("current")
_AuditName_Type = DisplayString
_AuditName_Object = MibTableColumn
auditName = _AuditName_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 6, 4, 1, 4),
    _AuditName_Type()
)
auditName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auditName.setStatus("current")
_AuditDescription_Type = DisplayString
_AuditDescription_Object = MibTableColumn
auditDescription = _AuditDescription_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 6, 4, 1, 5),
    _AuditDescription_Type()
)
auditDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auditDescription.setStatus("current")
_AuditTime_Type = DateAndTime
_AuditTime_Object = MibTableColumn
auditTime = _AuditTime_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 6, 4, 1, 6),
    _AuditTime_Type()
)
auditTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auditTime.setStatus("current")


class _AuditCommand_Type(Integer32):
    """Custom type auditCommand based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("runnow", 4))
    )


_AuditCommand_Type.__name__ = "Integer32"
_AuditCommand_Object = MibTableColumn
auditCommand = _AuditCommand_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 6, 4, 1, 7),
    _AuditCommand_Type()
)
auditCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auditCommand.setStatus("current")


class _AuditStatus_Type(Integer32):
    """Custom type auditStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AuditStatus_Type.__name__ = "Integer32"
_AuditStatus_Object = MibTableColumn
auditStatus = _AuditStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 6, 4, 1, 8),
    _AuditStatus_Type()
)
auditStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auditStatus.setStatus("current")


class _AuditResult_Type(Integer32):
    """Custom type auditResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("abort", 4),
          ("failed", 2),
          ("notRun", 5),
          ("passed", 1))
    )


_AuditResult_Type.__name__ = "Integer32"
_AuditResult_Object = MibTableColumn
auditResult = _AuditResult_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 6, 4, 1, 9),
    _AuditResult_Type()
)
auditResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auditResult.setStatus("current")
_AuditPassedCount_Type = Unsigned32
_AuditPassedCount_Object = MibTableColumn
auditPassedCount = _AuditPassedCount_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 6, 4, 1, 10),
    _AuditPassedCount_Type()
)
auditPassedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auditPassedCount.setStatus("current")
_AuditFailedCount_Type = Unsigned32
_AuditFailedCount_Object = MibTableColumn
auditFailedCount = _AuditFailedCount_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 6, 4, 1, 11),
    _AuditFailedCount_Type()
)
auditFailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auditFailedCount.setStatus("current")
_AuditCycleCount_Type = Unsigned32
_AuditCycleCount_Object = MibTableColumn
auditCycleCount = _AuditCycleCount_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 6, 4, 1, 12),
    _AuditCycleCount_Type()
)
auditCycleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auditCycleCount.setStatus("current")
_AuditTotalPassedCount_Type = Unsigned32
_AuditTotalPassedCount_Object = MibTableColumn
auditTotalPassedCount = _AuditTotalPassedCount_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 6, 4, 1, 13),
    _AuditTotalPassedCount_Type()
)
auditTotalPassedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auditTotalPassedCount.setStatus("current")
_AuditTotalFailedCount_Type = Unsigned32
_AuditTotalFailedCount_Object = MibTableColumn
auditTotalFailedCount = _AuditTotalFailedCount_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 6, 4, 1, 14),
    _AuditTotalFailedCount_Type()
)
auditTotalFailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auditTotalFailedCount.setStatus("current")
_CmDevice_ObjectIdentity = ObjectIdentity
cmDevice = _CmDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 8)
)
_CmMacAddress_Type = MacAddress
_CmMacAddress_Object = MibScalar
cmMacAddress = _CmMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 8, 1),
    _CmMacAddress_Type()
)
cmMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cmMacAddress.setStatus("current")
_CmVendor_Type = DisplayString
_CmVendor_Object = MibScalar
cmVendor = _CmVendor_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 8, 2),
    _CmVendor_Type()
)
cmVendor.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cmVendor.setStatus("current")
_CmResetReason_Type = DisplayString
_CmResetReason_Object = MibScalar
cmResetReason = _CmResetReason_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 8, 3),
    _CmResetReason_Type()
)
cmResetReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cmResetReason.setStatus("current")


class _CmUChannelID_Type(Integer32):
    """Custom type cmUChannelID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CmUChannelID_Type.__name__ = "Integer32"
_CmUChannelID_Object = MibScalar
cmUChannelID = _CmUChannelID_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 8, 4),
    _CmUChannelID_Type()
)
cmUChannelID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cmUChannelID.setStatus("current")


class _CmPrimarySID_Type(Unsigned32):
    """Custom type cmPrimarySID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_CmPrimarySID_Type.__name__ = "Unsigned32"
_CmPrimarySID_Object = MibScalar
cmPrimarySID = _CmPrimarySID_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 8, 5),
    _CmPrimarySID_Type()
)
cmPrimarySID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cmPrimarySID.setStatus("current")
_CmResetStatus_Type = DisplayString
_CmResetStatus_Object = MibScalar
cmResetStatus = _CmResetStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 8, 6),
    _CmResetStatus_Type()
)
cmResetStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cmResetStatus.setStatus("current")
_CmResetUpTime_Type = TimeTicks
_CmResetUpTime_Object = MibScalar
cmResetUpTime = _CmResetUpTime_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 8, 7),
    _CmResetUpTime_Type()
)
cmResetUpTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cmResetUpTime.setStatus("current")
_CmResetInfo_Type = DisplayString
_CmResetInfo_Object = MibScalar
cmResetInfo = _CmResetInfo_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 8, 8),
    _CmResetInfo_Type()
)
cmResetInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cmResetInfo.setStatus("current")


class _CmIpAddress_Type(OctetString):
    """Custom type cmIpAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_CmIpAddress_Type.__name__ = "OctetString"
_CmIpAddress_Object = MibScalar
cmIpAddress = _CmIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 8, 9),
    _CmIpAddress_Type()
)
cmIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cmIpAddress.setStatus("current")
_EquipmentError_ObjectIdentity = ObjectIdentity
equipmentError = _EquipmentError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 9)
)
_FpgaErrorEventTable_Object = MibTable
fpgaErrorEventTable = _FpgaErrorEventTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 9, 1)
)
if mibBuilder.loadTexts:
    fpgaErrorEventTable.setStatus("current")
_FpgaErrorEventEntry_Object = MibTableRow
fpgaErrorEventEntry = _FpgaErrorEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 9, 1, 1)
)
fpgaErrorEventEntry.setIndexNames(
    (0, "CADANT-CMTS-EQUIPMENT-MIB", "errEvCardId"),
    (0, "CADANT-CMTS-EQUIPMENT-MIB", "errEventId"),
)
if mibBuilder.loadTexts:
    fpgaErrorEventEntry.setStatus("current")


class _ErrEventId_Type(Unsigned32):
    """Custom type errEventId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ErrEventId_Type.__name__ = "Unsigned32"
_ErrEventId_Object = MibTableColumn
errEventId = _ErrEventId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 9, 1, 1, 1),
    _ErrEventId_Type()
)
errEventId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    errEventId.setStatus("current")


class _ErrEvRecoveryEnabled_Type(TruthValue):
    """Custom type errEvRecoveryEnabled based on TruthValue"""


_ErrEvRecoveryEnabled_Object = MibTableColumn
errEvRecoveryEnabled = _ErrEvRecoveryEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 9, 1, 1, 2),
    _ErrEvRecoveryEnabled_Type()
)
errEvRecoveryEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    errEvRecoveryEnabled.setStatus("current")


class _ErrEvLoggingEnabled_Type(TruthValue):
    """Custom type errEvLoggingEnabled based on TruthValue"""


_ErrEvLoggingEnabled_Object = MibTableColumn
errEvLoggingEnabled = _ErrEvLoggingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 9, 1, 1, 3),
    _ErrEvLoggingEnabled_Type()
)
errEvLoggingEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    errEvLoggingEnabled.setStatus("current")


class _ErrEvLogLevel_Type(Integer32):
    """Custom type errEvLogLevel based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ErrEvLogLevel_Type.__name__ = "Integer32"
_ErrEvLogLevel_Object = MibTableColumn
errEvLogLevel = _ErrEvLogLevel_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 9, 1, 1, 4),
    _ErrEvLogLevel_Type()
)
errEvLogLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    errEvLogLevel.setStatus("current")
_ErrEvRowStatus_Type = RowStatus
_ErrEvRowStatus_Object = MibTableColumn
errEvRowStatus = _ErrEvRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 9, 1, 1, 5),
    _ErrEvRowStatus_Type()
)
errEvRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    errEvRowStatus.setStatus("current")
_ErrEvCardId_Type = CardId
_ErrEvCardId_Object = MibTableColumn
errEvCardId = _ErrEvCardId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 9, 1, 1, 6),
    _ErrEvCardId_Type()
)
errEvCardId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    errEvCardId.setStatus("current")
_CadEquipmentMibConformance_ObjectIdentity = ObjectIdentity
cadEquipmentMibConformance = _CadEquipmentMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 10)
)
_CadEquipmentMibCompliances_ObjectIdentity = ObjectIdentity
cadEquipmentMibCompliances = _CadEquipmentMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 10, 1)
)
_CadEquipmentMibGroup_ObjectIdentity = ObjectIdentity
cadEquipmentMibGroup = _CadEquipmentMibGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 10, 2)
)
_CerSpareModeExt_ObjectIdentity = ObjectIdentity
cerSpareModeExt = _CerSpareModeExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 11)
)
_CerSpareModeExtTable_Object = MibTable
cerSpareModeExtTable = _CerSpareModeExtTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 11, 1)
)
if mibBuilder.loadTexts:
    cerSpareModeExtTable.setStatus("current")
_CerSpareModeExtEntry_Object = MibTableRow
cerSpareModeExtEntry = _CerSpareModeExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 11, 1, 1)
)
cerSpareModeExtEntry.setIndexNames(
    (0, "CADANT-CMTS-EQUIPMENT-MIB", "cerSpareModeCardId"),
    (0, "CADANT-CMTS-EQUIPMENT-MIB", "cerSpareModeFaultId"),
)
if mibBuilder.loadTexts:
    cerSpareModeExtEntry.setStatus("current")
_CerSpareModeCardId_Type = CardId
_CerSpareModeCardId_Object = MibTableColumn
cerSpareModeCardId = _CerSpareModeCardId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 11, 1, 1, 1),
    _CerSpareModeCardId_Type()
)
cerSpareModeCardId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cerSpareModeCardId.setStatus("current")


class _CerSpareModeFaultId_Type(Integer32):
    """Custom type cerSpareModeFaultId based on Integer32"""
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
              13,
              14,
              15,
              16,
              17,
              18)
        )
    )
    namedValues = NamedValues(
        *(("bcm3142Err", 5),
          ("clockLost", 13),
          ("dataplaneFailure", 7),
          ("dataplaneLinkFault", 17),
          ("deviceFatal", 11),
          ("dsOverPower", 9),
          ("dsUnderPower", 8),
          ("dulFailure", 6),
          ("ersmFault", 3),
          ("fpgaBufferPoolFault", 16),
          ("fpgaFatalError", 12),
          ("initTimeout", 2),
          ("monitoredTaskFailure", 18),
          ("none", 0),
          ("pingFault", 1),
          ("pwrSensorHighFault", 14),
          ("pwrSensorLowFault", 15),
          ("sbecOverflow", 10),
          ("swException", 4))
    )


_CerSpareModeFaultId_Type.__name__ = "Integer32"
_CerSpareModeFaultId_Object = MibTableColumn
cerSpareModeFaultId = _CerSpareModeFaultId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 11, 1, 1, 2),
    _CerSpareModeFaultId_Type()
)
cerSpareModeFaultId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cerSpareModeFaultId.setStatus("current")


class _CerSpareModeMode_Type(Integer32):
    """Custom type cerSpareModeMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("invalid", 0),
          ("manual", 1))
    )


_CerSpareModeMode_Type.__name__ = "Integer32"
_CerSpareModeMode_Object = MibTableColumn
cerSpareModeMode = _CerSpareModeMode_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 11, 1, 1, 3),
    _CerSpareModeMode_Type()
)
cerSpareModeMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cerSpareModeMode.setStatus("current")
_CerSpareModeRowStatus_Type = RowStatus
_CerSpareModeRowStatus_Object = MibTableColumn
cerSpareModeRowStatus = _CerSpareModeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 11, 1, 1, 4),
    _CerSpareModeRowStatus_Type()
)
cerSpareModeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cerSpareModeRowStatus.setStatus("current")
_LicenseError_ObjectIdentity = ObjectIdentity
licenseError = _LicenseError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 12)
)


class _CerLicenseTypeStr_Type(DisplayString):
    """Custom type cerLicenseTypeStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_CerLicenseTypeStr_Type.__name__ = "DisplayString"
_CerLicenseTypeStr_Object = MibScalar
cerLicenseTypeStr = _CerLicenseTypeStr_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 12, 1),
    _CerLicenseTypeStr_Type()
)
cerLicenseTypeStr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cerLicenseTypeStr.setStatus("current")
cerCardEntry.registerAugmentions(
    ("CADANT-CMTS-EQUIPMENT-MIB",
     "cerCardDataEntry")
)
cerCardDataEntry.setIndexNames(*cerCardEntry.getIndexNames())

# Managed Objects groups

systemGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 10, 2, 1)
)
systemGeneralGroup.setObjects(
      *(("CADANT-CMTS-EQUIPMENT-MIB", "systemClock"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "trapCounter"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "trapSeverity"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "systemKey"))
)
if mibBuilder.loadTexts:
    systemGeneralGroup.setStatus("current")

equipmentStateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 10, 2, 2)
)
equipmentStateGroup.setObjects(
      *(("CADANT-CMTS-EQUIPMENT-MIB", "cardLastChangeTime"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "portLastChangeTime"))
)
if mibBuilder.loadTexts:
    equipmentStateGroup.setStatus("current")

equipmentShelfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 10, 2, 3)
)
equipmentShelfGroup.setObjects(
      *(("CADANT-CMTS-EQUIPMENT-MIB", "shelfName"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "shelfSwVersion"))
)
if mibBuilder.loadTexts:
    equipmentShelfGroup.setStatus("current")

equipmentDiagGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 10, 2, 6)
)
equipmentDiagGroup.setObjects(
      *(("CADANT-CMTS-EQUIPMENT-MIB", "remainInDiagMode"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "verboseLevel"))
)
if mibBuilder.loadTexts:
    equipmentDiagGroup.setStatus("current")

equipmentCardTestGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 10, 2, 8)
)
equipmentCardTestGroup.setObjects(
      *(("CADANT-CMTS-EQUIPMENT-MIB", "cardTestName"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardTestType"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardTestDescription"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardTestCommand"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardTestScheduleCommand"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardTestSchedule"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardTestTime"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardTestResult"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardTestResultDesc"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardTestTransId"))
)
if mibBuilder.loadTexts:
    equipmentCardTestGroup.setStatus("current")

equipmentAuditGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 10, 2, 10)
)
equipmentAuditGroup.setObjects(
      *(("CADANT-CMTS-EQUIPMENT-MIB", "auditAutoScheduling"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "auditLogOutput"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "auditLogThrottle"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "auditName"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "auditDescription"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "auditTime"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "auditCommand"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "auditStatus"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "auditResult"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "auditPassedCount"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "auditFailedCount"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "auditCycleCount"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "auditTotalPassedCount"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "auditTotalFailedCount"))
)
if mibBuilder.loadTexts:
    equipmentAuditGroup.setStatus("current")

fpgaErrorEventGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 10, 2, 12)
)
fpgaErrorEventGroup.setObjects(
      *(("CADANT-CMTS-EQUIPMENT-MIB", "errEvRecoveryEnabled"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "errEvLoggingEnabled"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "errEvLogLevel"))
)
if mibBuilder.loadTexts:
    fpgaErrorEventGroup.setStatus("current")

equipmentCerCardGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 10, 2, 14)
)
equipmentCerCardGroup.setObjects(
      *(("CADANT-CMTS-EQUIPMENT-MIB", "cerCardName"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerCardType"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerCardSubType"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerCardAdminState"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerCardPrState"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerCardSecState"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerCardDplxStatus"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerCardAction"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerCardTrapInh"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerCardNumPorts"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerCardDetected"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerCardSubDetected"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerCardFwUpdateStatus"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerCardSpareGroupId"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerCardSpareGroupMode"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerCardUpTime"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerCardTemperature"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerCardTemperatureHighWarn"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerCardTemperatureHighError"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerCardAnnex"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerCardNumRfConnectors"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerCardDataSerialNum"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerCardDataFwVersion"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerCardDataHwVersion"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerCardDataHwDeviations"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerCardDataSwVersion"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerCardDataCpuType"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerCardDataCpuSpeed"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerCardDataBusSpeed"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerCardDataRamSize"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerCardDataNorFlashSize"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerCardDataNandFlashSize"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerCardDataFpgaSource"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerCardDataBootVersion"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerCardDataLastBootVersion"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerCardDataLastBootSource"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerCardDataPicSerialNum"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerCardDataPicHwVersion"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerCardDataPicHwDeviations"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerCardDataPicModelNum"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerCardDataMfgDateTime"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerCardDataMfg"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerCardDataProductName"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerCardDataPartModelNum"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerCardDataProductVersion"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerCardDataAssetTag"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerCardDataCommittedSwVersion"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerCardDataFeedAPresent"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerCardDataFeedBPresent"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerCardDataAllowedPorts"))
)
if mibBuilder.loadTexts:
    equipmentCerCardGroup.setStatus("current")

equipmentCerPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 10, 2, 15)
)
equipmentCerPortGroup.setObjects(
      *(("CADANT-CMTS-EQUIPMENT-MIB", "cerPortType"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerPortAdminState"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerPortPrState"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerPortSecState"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerPortDplxStatus"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerPortAction"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerPortTrapInh"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerPortNumChans"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerPortMacAddress"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerPortMode"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerPortDetectedMode"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerPortDocsIfIndex"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerPortBgpId"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerPortConnectorId"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerPortCardSubType"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerPortDescription"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerPortCurrDsPower"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerPortMinDsPower"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerPortMaxDsPower"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerPortTxFlowControlMode"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerPortRxFlowControlMode"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerPortTxFlowControlDetected"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerPortRxFlowControlDetected"))
)
if mibBuilder.loadTexts:
    equipmentCerPortGroup.setStatus("current")

cerDiskVolumeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 10, 2, 21)
)
cerDiskVolumeGroup.setObjects(
      *(("CADANT-CMTS-EQUIPMENT-MIB", "cerDiskVolumeName"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerDiskVolumeSize"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerDiskVolumeUsageLevel"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerDiskVolumeUsagePercentage"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerDiskVolumeUsageCriticalThreshold"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerDiskVolumeUsageMajorThreshold"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerDiskVolumeUsageMinorThreshold"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerDiskVolumeAutoDeleteUnusedFile"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerDiskVolumeTrapInh"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerDiskVolumeFileName"))
)
if mibBuilder.loadTexts:
    cerDiskVolumeGroup.setStatus("current")


# Notification objects

cmResetClearNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 0, 15)
)
cmResetClearNotification.setObjects(
      *(("CADANT-CMTS-EQUIPMENT-MIB", "trapCounter"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "systemClock"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "trapSeverity"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cmMacAddress"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cmUChannelID"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerCardNumber"))
)
if mibBuilder.loadTexts:
    cmResetClearNotification.setStatus(
        "current"
    )

cmResetNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 0, 16)
)
cmResetNotification.setObjects(
      *(("CADANT-CMTS-EQUIPMENT-MIB", "trapCounter"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "systemClock"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "trapSeverity"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cmMacAddress"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cmVendor"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cmResetReason"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cmUChannelID"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cmPrimarySID"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cmResetStatus"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cmResetUpTime"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerCardNumber"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cmResetInfo"))
)
if mibBuilder.loadTexts:
    cmResetNotification.setStatus(
        "current"
    )

cardTempOutOfRangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 0, 19)
)
cardTempOutOfRangeNotification.setObjects(
      *(("CADANT-CMTS-EQUIPMENT-MIB", "trapCounter"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "trapSeverity"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardNumber"))
)
if mibBuilder.loadTexts:
    cardTempOutOfRangeNotification.setStatus(
        "current"
    )

cardTempNoReportNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 0, 20)
)
cardTempNoReportNotification.setObjects(
      *(("CADANT-CMTS-EQUIPMENT-MIB", "trapCounter"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "trapSeverity"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardNumber"))
)
if mibBuilder.loadTexts:
    cardTempNoReportNotification.setStatus(
        "current"
    )

cardTempOverHeatNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 0, 21)
)
cardTempOverHeatNotification.setObjects(
      *(("CADANT-CMTS-EQUIPMENT-MIB", "trapCounter"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "trapSeverity"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardNumber"))
)
if mibBuilder.loadTexts:
    cardTempOverHeatNotification.setStatus(
        "current"
    )

downstreamPowerLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 0, 22)
)
downstreamPowerLoss.setObjects(
      *(("CADANT-CMTS-EQUIPMENT-MIB", "trapCounter"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "trapSeverity"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardNumber"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "portNumber"))
)
if mibBuilder.loadTexts:
    downstreamPowerLoss.setStatus(
        "current"
    )

cmRegistrationNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 0, 23)
)
cmRegistrationNotification.setObjects(
      *(("CADANT-CMTS-EQUIPMENT-MIB", "trapCounter"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "systemClock"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "trapSeverity"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cmMacAddress"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cmVendor"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cmUChannelID"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardNumber"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cmIpAddress"))
)
if mibBuilder.loadTexts:
    cmRegistrationNotification.setStatus(
        "current"
    )

noLicenseNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 0, 24)
)
noLicenseNotification.setObjects(
      *(("CADANT-CMTS-EQUIPMENT-MIB", "trapCounter"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "trapSeverity"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerCardNumber"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerPortNumber"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerPortType"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerPortCardSubType"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerPortDocsIfIndex"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerLicenseTypeStr"))
)
if mibBuilder.loadTexts:
    noLicenseNotification.setStatus(
        "current"
    )

cerCardPrStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 0, 25)
)
cerCardPrStateChange.setObjects(
      *(("CADANT-CMTS-EQUIPMENT-MIB", "trapCounter"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "trapSeverity"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerCardNumber"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerCardType"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerCardSubType"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerCardPrState"))
)
if mibBuilder.loadTexts:
    cerCardPrStateChange.setStatus(
        "current"
    )

cerCardSecStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 0, 26)
)
cerCardSecStateChange.setObjects(
      *(("CADANT-CMTS-EQUIPMENT-MIB", "trapCounter"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "trapSeverity"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerCardNumber"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerCardType"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerCardSubType"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerCardSecState"))
)
if mibBuilder.loadTexts:
    cerCardSecStateChange.setStatus(
        "current"
    )

cerCardDetectedChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 0, 27)
)
cerCardDetectedChange.setObjects(
      *(("CADANT-CMTS-EQUIPMENT-MIB", "trapCounter"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "trapSeverity"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerCardNumber"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerCardDetected"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerCardSubDetected"))
)
if mibBuilder.loadTexts:
    cerCardDetectedChange.setStatus(
        "current"
    )

cerCardDplxStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 0, 28)
)
cerCardDplxStatusChange.setObjects(
      *(("CADANT-CMTS-EQUIPMENT-MIB", "trapCounter"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "trapSeverity"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerCardNumber"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerCardType"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerCardSubType"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerCardDplxStatus"))
)
if mibBuilder.loadTexts:
    cerCardDplxStatusChange.setStatus(
        "current"
    )

cerPortPrStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 0, 29)
)
cerPortPrStateChange.setObjects(
      *(("CADANT-CMTS-EQUIPMENT-MIB", "trapCounter"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "trapSeverity"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerCardNumber"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerPortNumber"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerPortType"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerPortPrState"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerPortCardSubType"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerPortDocsIfIndex"))
)
if mibBuilder.loadTexts:
    cerPortPrStateChange.setStatus(
        "current"
    )

cerPortSecStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 0, 30)
)
cerPortSecStateChange.setObjects(
      *(("CADANT-CMTS-EQUIPMENT-MIB", "trapCounter"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "trapSeverity"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerCardNumber"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerPortNumber"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerPortType"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerPortSecState"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerPortCardSubType"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerPortDocsIfIndex"))
)
if mibBuilder.loadTexts:
    cerPortSecStateChange.setStatus(
        "current"
    )

cerPortDplxStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 0, 31)
)
cerPortDplxStatusChange.setObjects(
      *(("CADANT-CMTS-EQUIPMENT-MIB", "trapCounter"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "trapSeverity"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerCardNumber"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerPortNumber"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerPortType"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerPortDplxStatus"))
)
if mibBuilder.loadTexts:
    cerPortDplxStatusChange.setStatus(
        "current"
    )

cardTestResultNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 0, 33)
)
cardTestResultNotification.setObjects(
      *(("CADANT-CMTS-EQUIPMENT-MIB", "trapCounter"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "trapSeverity"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerCardNumber"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "diagTestId"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardTestName"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardTestResult"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardTestResultDesc"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cardTestTransId"))
)
if mibBuilder.loadTexts:
    cardTestResultNotification.setStatus(
        "current"
    )

cerDiskVolumeUsageNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 0, 35)
)
cerDiskVolumeUsageNotification.setObjects(
      *(("CADANT-CMTS-EQUIPMENT-MIB", "trapCounter"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "trapSeverity"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerCardNumber"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerDiskDriveNumber"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerDiskVolumeNumber"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerDiskVolumeUsageLevel"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerDiskVolumeName"))
)
if mibBuilder.loadTexts:
    cerDiskVolumeUsageNotification.setStatus(
        "current"
    )

cerDiskVolumeAutoDeleteFileNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 0, 36)
)
cerDiskVolumeAutoDeleteFileNotification.setObjects(
      *(("CADANT-CMTS-EQUIPMENT-MIB", "trapCounter"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "trapSeverity"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerCardNumber"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerDiskDriveNumber"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerDiskVolumeNumber"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerDiskVolumeName"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerDiskVolumeFileName"))
)
if mibBuilder.loadTexts:
    cerDiskVolumeAutoDeleteFileNotification.setStatus(
        "current"
    )

cerCamFaultNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 0, 41)
)
cerCamFaultNotification.setObjects(
      *(("CADANT-CMTS-EQUIPMENT-MIB", "trapCounter"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "trapSeverity"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerCamFaultId"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerCamFaultRecovery"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerCamFaultAutoFailback"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerCardNumber"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerCardSubType"),
        ("CADANT-CMTS-EQUIPMENT-MIB", "cerCamFaultErrorStr"))
)
if mibBuilder.loadTexts:
    cerCamFaultNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

cadEquipmentMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 10, 1, 10, 1, 1)
)
if mibBuilder.loadTexts:
    cadEquipmentMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CADANT-CMTS-EQUIPMENT-MIB",
    **{"TestId": TestId,
       "TestType": TestType,
       "TestCommand": TestCommand,
       "TestScheduleCommand": TestScheduleCommand,
       "TestSchedule": TestSchedule,
       "TestResult": TestResult,
       "TestTransactionId": TestTransactionId,
       "CerCamFaultTrapType": CerCamFaultTrapType,
       "cadEquipmentMib": cadEquipmentMib,
       "equipmentTraps": equipmentTraps,
       "cmResetClearNotification": cmResetClearNotification,
       "cmResetNotification": cmResetNotification,
       "cardTempOutOfRangeNotification": cardTempOutOfRangeNotification,
       "cardTempNoReportNotification": cardTempNoReportNotification,
       "cardTempOverHeatNotification": cardTempOverHeatNotification,
       "downstreamPowerLoss": downstreamPowerLoss,
       "cmRegistrationNotification": cmRegistrationNotification,
       "noLicenseNotification": noLicenseNotification,
       "cerCardPrStateChange": cerCardPrStateChange,
       "cerCardSecStateChange": cerCardSecStateChange,
       "cerCardDetectedChange": cerCardDetectedChange,
       "cerCardDplxStatusChange": cerCardDplxStatusChange,
       "cerPortPrStateChange": cerPortPrStateChange,
       "cerPortSecStateChange": cerPortSecStateChange,
       "cerPortDplxStatusChange": cerPortDplxStatusChange,
       "cardTestResultNotification": cardTestResultNotification,
       "cerDiskVolumeUsageNotification": cerDiskVolumeUsageNotification,
       "cerDiskVolumeAutoDeleteFileNotification": cerDiskVolumeAutoDeleteFileNotification,
       "cerCamFaultInfo": cerCamFaultInfo,
       "cerCamFaultId": cerCamFaultId,
       "cerCamFaultRecovery": cerCamFaultRecovery,
       "cerCamFaultAutoFailback": cerCamFaultAutoFailback,
       "cerCamFaultErrorStr": cerCamFaultErrorStr,
       "cerCamFaultNotification": cerCamFaultNotification,
       "systemGeneral": systemGeneral,
       "systemClock": systemClock,
       "trapCounter": trapCounter,
       "trapSeverity": trapSeverity,
       "systemKey": systemKey,
       "cardNumber": cardNumber,
       "portNumber": portNumber,
       "diskDriveNumber": diskDriveNumber,
       "diskVolumeNumber": diskVolumeNumber,
       "cerCardNumber": cerCardNumber,
       "cerPortNumber": cerPortNumber,
       "cerDiskDriveNumber": cerDiskDriveNumber,
       "cerDiskVolumeNumber": cerDiskVolumeNumber,
       "shelfObjects": shelfObjects,
       "shelfName": shelfName,
       "shelfSwVersion": shelfSwVersion,
       "equipmentState": equipmentState,
       "cardLastChangeTime": cardLastChangeTime,
       "portLastChangeTime": portLastChangeTime,
       "equipmentTbl": equipmentTbl,
       "cerCardTable": cerCardTable,
       "cerCardEntry": cerCardEntry,
       "cerCardId": cerCardId,
       "cerCardName": cerCardName,
       "cerCardType": cerCardType,
       "cerCardSubType": cerCardSubType,
       "cerCardAdminState": cerCardAdminState,
       "cerCardPrState": cerCardPrState,
       "cerCardSecState": cerCardSecState,
       "cerCardDplxStatus": cerCardDplxStatus,
       "cerCardAction": cerCardAction,
       "cerCardTrapInh": cerCardTrapInh,
       "cerCardNumPorts": cerCardNumPorts,
       "cerCardDetected": cerCardDetected,
       "cerCardSubDetected": cerCardSubDetected,
       "cerCardFwUpdateStatus": cerCardFwUpdateStatus,
       "cerCardSpareGroupId": cerCardSpareGroupId,
       "cerCardSpareGroupMode": cerCardSpareGroupMode,
       "cerCardUpTime": cerCardUpTime,
       "cerCardTemperature": cerCardTemperature,
       "cerCardPicDetected": cerCardPicDetected,
       "cerCardLastResetReason": cerCardLastResetReason,
       "cerCardTemperatureHighWarn": cerCardTemperatureHighWarn,
       "cerCardTemperatureHighError": cerCardTemperatureHighError,
       "cerCardAnnex": cerCardAnnex,
       "cerCardNumRfConnectors": cerCardNumRfConnectors,
       "cerPortTable": cerPortTable,
       "cerPortEntry": cerPortEntry,
       "cerPortCardId": cerPortCardId,
       "cerPortId": cerPortId,
       "cerPortType": cerPortType,
       "cerPortAdminState": cerPortAdminState,
       "cerPortPrState": cerPortPrState,
       "cerPortSecState": cerPortSecState,
       "cerPortDplxStatus": cerPortDplxStatus,
       "cerPortAction": cerPortAction,
       "cerPortTrapInh": cerPortTrapInh,
       "cerPortNumChans": cerPortNumChans,
       "cerPortDocsIfIndex": cerPortDocsIfIndex,
       "cerPortMacAddress": cerPortMacAddress,
       "cerPortMode": cerPortMode,
       "cerPortDetectedMode": cerPortDetectedMode,
       "cerPortBgpId": cerPortBgpId,
       "cerPortConnectorId": cerPortConnectorId,
       "cerPortCardSubType": cerPortCardSubType,
       "cerPortDescription": cerPortDescription,
       "cerPortCurrDsPower": cerPortCurrDsPower,
       "cerPortMinDsPower": cerPortMinDsPower,
       "cerPortMaxDsPower": cerPortMaxDsPower,
       "cerPortTxFlowControlMode": cerPortTxFlowControlMode,
       "cerPortRxFlowControlMode": cerPortRxFlowControlMode,
       "cerPortTxFlowControlDetected": cerPortTxFlowControlDetected,
       "cerPortRxFlowControlDetected": cerPortRxFlowControlDetected,
       "cerPortMacIfIndex": cerPortMacIfIndex,
       "cerPortGroupId": cerPortGroupId,
       "cerPortGroupPortId": cerPortGroupPortId,
       "cerDiskVolumeTable": cerDiskVolumeTable,
       "cerDiskVolumeEntry": cerDiskVolumeEntry,
       "cerDiskVolumeCardId": cerDiskVolumeCardId,
       "cerDiskVolumeDriveId": cerDiskVolumeDriveId,
       "cerDiskVolumeId": cerDiskVolumeId,
       "cerDiskVolumeName": cerDiskVolumeName,
       "cerDiskVolumeSize": cerDiskVolumeSize,
       "cerDiskVolumeUsageLevel": cerDiskVolumeUsageLevel,
       "cerDiskVolumeUsagePercentage": cerDiskVolumeUsagePercentage,
       "cerDiskVolumeUsageCriticalThreshold": cerDiskVolumeUsageCriticalThreshold,
       "cerDiskVolumeUsageMajorThreshold": cerDiskVolumeUsageMajorThreshold,
       "cerDiskVolumeUsageMinorThreshold": cerDiskVolumeUsageMinorThreshold,
       "cerDiskVolumeAutoDeleteUnusedFile": cerDiskVolumeAutoDeleteUnusedFile,
       "cerDiskVolumeTrapInh": cerDiskVolumeTrapInh,
       "cerDiskVolumeDiskSize": cerDiskVolumeDiskSize,
       "cerDiskVolumeFileName": cerDiskVolumeFileName,
       "cerCardDataTable": cerCardDataTable,
       "cerCardDataEntry": cerCardDataEntry,
       "cerCardDataSerialNum": cerCardDataSerialNum,
       "cerCardDataFwVersion": cerCardDataFwVersion,
       "cerCardDataHwVersion": cerCardDataHwVersion,
       "cerCardDataHwDeviations": cerCardDataHwDeviations,
       "cerCardDataSwVersion": cerCardDataSwVersion,
       "cerCardDataCpuType": cerCardDataCpuType,
       "cerCardDataCpuSpeed": cerCardDataCpuSpeed,
       "cerCardDataBusSpeed": cerCardDataBusSpeed,
       "cerCardDataRamSize": cerCardDataRamSize,
       "cerCardDataNorFlashSize": cerCardDataNorFlashSize,
       "cerCardDataNandFlashSize": cerCardDataNandFlashSize,
       "cerCardDataFpgaSource": cerCardDataFpgaSource,
       "cerCardDataBootVersion": cerCardDataBootVersion,
       "cerCardDataLastBootVersion": cerCardDataLastBootVersion,
       "cerCardDataLastBootSource": cerCardDataLastBootSource,
       "cerCardDataPicSerialNum": cerCardDataPicSerialNum,
       "cerCardDataPicHwVersion": cerCardDataPicHwVersion,
       "cerCardDataPicHwDeviations": cerCardDataPicHwDeviations,
       "cerCardDataPicModelNum": cerCardDataPicModelNum,
       "cerCardDataMfgDateTime": cerCardDataMfgDateTime,
       "cerCardDataMfg": cerCardDataMfg,
       "cerCardDataProductName": cerCardDataProductName,
       "cerCardDataPartModelNum": cerCardDataPartModelNum,
       "cerCardDataProductVersion": cerCardDataProductVersion,
       "cerCardDataAssetTag": cerCardDataAssetTag,
       "cerCardDataCommittedSwVersion": cerCardDataCommittedSwVersion,
       "cerCardDataFeedAPresent": cerCardDataFeedAPresent,
       "cerCardDataFeedBPresent": cerCardDataFeedBPresent,
       "cerCardDataAllowedPorts": cerCardDataAllowedPorts,
       "cerCardDataLicenseAnnex": cerCardDataLicenseAnnex,
       "cerCardDataLicensePorts": cerCardDataLicensePorts,
       "cerCardDataLicenseDate": cerCardDataLicenseDate,
       "cerCardDataPatchVersions": cerCardDataPatchVersions,
       "cerCardDataPicModelName": cerCardDataPicModelName,
       "cerCardDataPicMfgRevision": cerCardDataPicMfgRevision,
       "cerCardDataPicMfg": cerCardDataPicMfg,
       "cerCardDataPicMfgDateTime": cerCardDataPicMfgDateTime,
       "cerFanStatusTable": cerFanStatusTable,
       "cerFanStatusEntry": cerFanStatusEntry,
       "cerFan1Speed": cerFan1Speed,
       "cerFan2Speed": cerFan2Speed,
       "cerFan3Speed": cerFan3Speed,
       "cerFanLevel": cerFanLevel,
       "cerFanAmbientTemperature": cerFanAmbientTemperature,
       "cerPemStatusTable": cerPemStatusTable,
       "cerPemStatusEntry": cerPemStatusEntry,
       "cerPemLedStatus": cerPemLedStatus,
       "cerPemFeed1Voltage": cerPemFeed1Voltage,
       "cerPemFeed1Current": cerPemFeed1Current,
       "cerPemFeed2Voltage": cerPemFeed2Voltage,
       "cerPemFeed2Current": cerPemFeed2Current,
       "cerPemFeed1Present": cerPemFeed1Present,
       "cerPemFeed2Present": cerPemFeed2Present,
       "cerPemCircuitBreaker1Enable": cerPemCircuitBreaker1Enable,
       "cerPemCircuitBreaker2Enable": cerPemCircuitBreaker2Enable,
       "cerPemBranchPresent": cerPemBranchPresent,
       "equipmentDiag": equipmentDiag,
       "eqDiagConfig": eqDiagConfig,
       "remainInDiagMode": remainInDiagMode,
       "consoleOutput": consoleOutput,
       "verboseLevel": verboseLevel,
       "diagTestId": diagTestId,
       "cardTestTable": cardTestTable,
       "cardTestEntry": cardTestEntry,
       "cardTestIndex": cardTestIndex,
       "cardTestId": cardTestId,
       "cardTestName": cardTestName,
       "cardTestType": cardTestType,
       "cardTestDescription": cardTestDescription,
       "cardTestCommand": cardTestCommand,
       "cardTestScheduleCommand": cardTestScheduleCommand,
       "cardTestSchedule": cardTestSchedule,
       "cardTestTime": cardTestTime,
       "cardTestResult": cardTestResult,
       "cardTestResultDesc": cardTestResultDesc,
       "cardTestTransId": cardTestTransId,
       "equipmentAudit": equipmentAudit,
       "auditAutoScheduling": auditAutoScheduling,
       "auditLogOutput": auditLogOutput,
       "auditLogThrottle": auditLogThrottle,
       "auditTable": auditTable,
       "auditEntry": auditEntry,
       "auditCardId": auditCardId,
       "auditId": auditId,
       "auditName": auditName,
       "auditDescription": auditDescription,
       "auditTime": auditTime,
       "auditCommand": auditCommand,
       "auditStatus": auditStatus,
       "auditResult": auditResult,
       "auditPassedCount": auditPassedCount,
       "auditFailedCount": auditFailedCount,
       "auditCycleCount": auditCycleCount,
       "auditTotalPassedCount": auditTotalPassedCount,
       "auditTotalFailedCount": auditTotalFailedCount,
       "cmDevice": cmDevice,
       "cmMacAddress": cmMacAddress,
       "cmVendor": cmVendor,
       "cmResetReason": cmResetReason,
       "cmUChannelID": cmUChannelID,
       "cmPrimarySID": cmPrimarySID,
       "cmResetStatus": cmResetStatus,
       "cmResetUpTime": cmResetUpTime,
       "cmResetInfo": cmResetInfo,
       "cmIpAddress": cmIpAddress,
       "equipmentError": equipmentError,
       "fpgaErrorEventTable": fpgaErrorEventTable,
       "fpgaErrorEventEntry": fpgaErrorEventEntry,
       "errEventId": errEventId,
       "errEvRecoveryEnabled": errEvRecoveryEnabled,
       "errEvLoggingEnabled": errEvLoggingEnabled,
       "errEvLogLevel": errEvLogLevel,
       "errEvRowStatus": errEvRowStatus,
       "errEvCardId": errEvCardId,
       "cadEquipmentMibConformance": cadEquipmentMibConformance,
       "cadEquipmentMibCompliances": cadEquipmentMibCompliances,
       "cadEquipmentMibCompliance": cadEquipmentMibCompliance,
       "cadEquipmentMibGroup": cadEquipmentMibGroup,
       "systemGeneralGroup": systemGeneralGroup,
       "equipmentStateGroup": equipmentStateGroup,
       "equipmentShelfGroup": equipmentShelfGroup,
       "equipmentDiagGroup": equipmentDiagGroup,
       "equipmentCardTestGroup": equipmentCardTestGroup,
       "equipmentAuditGroup": equipmentAuditGroup,
       "fpgaErrorEventGroup": fpgaErrorEventGroup,
       "equipmentCerCardGroup": equipmentCerCardGroup,
       "equipmentCerPortGroup": equipmentCerPortGroup,
       "cerDiskVolumeGroup": cerDiskVolumeGroup,
       "cerSpareModeExt": cerSpareModeExt,
       "cerSpareModeExtTable": cerSpareModeExtTable,
       "cerSpareModeExtEntry": cerSpareModeExtEntry,
       "cerSpareModeCardId": cerSpareModeCardId,
       "cerSpareModeFaultId": cerSpareModeFaultId,
       "cerSpareModeMode": cerSpareModeMode,
       "cerSpareModeRowStatus": cerSpareModeRowStatus,
       "licenseError": licenseError,
       "cerLicenseTypeStr": cerLicenseTypeStr}
)
