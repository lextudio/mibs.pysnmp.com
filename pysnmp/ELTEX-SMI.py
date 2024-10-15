# SNMP MIB module (ELTEX-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ELTEX-SMI
# Produced by pysmi-1.5.4 at Mon Oct 14 21:37:19 2024
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
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

eltex = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 34300)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ElHardware_ObjectIdentity = ObjectIdentity
elHardware = _ElHardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34300, 1)
)
if mibBuilder.loadTexts:
    elHardware.setStatus("current")
_ElSoftware_ObjectIdentity = ObjectIdentity
elSoftware = _ElSoftware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34300, 2)
)
if mibBuilder.loadTexts:
    elSoftware.setStatus("current")
_EltrapGroup_ObjectIdentity = ObjectIdentity
eltrapGroup = _EltrapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34300, 3)
)
if mibBuilder.loadTexts:
    eltrapGroup.setStatus("current")
_Mc240AlarmTraps_ObjectIdentity = ObjectIdentity
mc240AlarmTraps = _Mc240AlarmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34300, 3, 3)
)
_Mc240OkTraps_ObjectIdentity = ObjectIdentity
mc240OkTraps = _Mc240OkTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34300, 3, 4)
)
_Mc240TrapTypes_ObjectIdentity = ObjectIdentity
mc240TrapTypes = _Mc240TrapTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34300, 3, 5)
)
_McTrapExState_Type = Integer32
_McTrapExState_Object = MibScalar
mcTrapExState = _McTrapExState_Object(
    (1, 3, 6, 1, 4, 1, 34300, 3, 5, 1),
    _McTrapExState_Type()
)
mcTrapExState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcTrapExState.setStatus("current")
_McTrapLParam1_Type = Integer32
_McTrapLParam1_Object = MibScalar
mcTrapLParam1 = _McTrapLParam1_Object(
    (1, 3, 6, 1, 4, 1, 34300, 3, 5, 2),
    _McTrapLParam1_Type()
)
mcTrapLParam1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcTrapLParam1.setStatus("current")
_McTrapLParam2_Type = Integer32
_McTrapLParam2_Object = MibScalar
mcTrapLParam2 = _McTrapLParam2_Object(
    (1, 3, 6, 1, 4, 1, 34300, 3, 5, 3),
    _McTrapLParam2_Type()
)
mcTrapLParam2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcTrapLParam2.setStatus("current")
_McTrapLParam3_Type = Integer32
_McTrapLParam3_Object = MibScalar
mcTrapLParam3 = _McTrapLParam3_Object(
    (1, 3, 6, 1, 4, 1, 34300, 3, 5, 4),
    _McTrapLParam3_Type()
)
mcTrapLParam3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcTrapLParam3.setStatus("current")
_McTrapID_Type = Integer32
_McTrapID_Object = MibScalar
mcTrapID = _McTrapID_Object(
    (1, 3, 6, 1, 4, 1, 34300, 3, 5, 5),
    _McTrapID_Type()
)
mcTrapID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcTrapID.setStatus("current")


class _McTrapDescr_Type(DisplayString):
    """Custom type mcTrapDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_McTrapDescr_Type.__name__ = "DisplayString"
_McTrapDescr_Object = MibScalar
mcTrapDescr = _McTrapDescr_Object(
    (1, 3, 6, 1, 4, 1, 34300, 3, 5, 6),
    _McTrapDescr_Type()
)
mcTrapDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcTrapDescr.setStatus("current")
_McTrapRestoredAlarmID_Type = Integer32
_McTrapRestoredAlarmID_Object = MibScalar
mcTrapRestoredAlarmID = _McTrapRestoredAlarmID_Object(
    (1, 3, 6, 1, 4, 1, 34300, 3, 5, 7),
    _McTrapRestoredAlarmID_Type()
)
mcTrapRestoredAlarmID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcTrapRestoredAlarmID.setStatus("current")
_McTrapSyncType_Type = Integer32
_McTrapSyncType_Object = MibScalar
mcTrapSyncType = _McTrapSyncType_Object(
    (1, 3, 6, 1, 4, 1, 34300, 3, 5, 8),
    _McTrapSyncType_Type()
)
mcTrapSyncType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcTrapSyncType.setStatus("current")
_McReservedFlag_Type = Integer32
_McReservedFlag_Object = MibScalar
mcReservedFlag = _McReservedFlag_Object(
    (1, 3, 6, 1, 4, 1, 34300, 3, 5, 9),
    _McReservedFlag_Type()
)
mcReservedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcReservedFlag.setStatus("current")
_Mp800mkAlarmTraps_ObjectIdentity = ObjectIdentity
mp800mkAlarmTraps = _Mp800mkAlarmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34300, 3, 8)
)
_Mp800mkOkTraps_ObjectIdentity = ObjectIdentity
mp800mkOkTraps = _Mp800mkOkTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34300, 3, 9)
)
_Mp800mkTrapTypes_ObjectIdentity = ObjectIdentity
mp800mkTrapTypes = _Mp800mkTrapTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34300, 3, 10)
)
_Mp800mkTrapParameter_Type = DisplayString
_Mp800mkTrapParameter_Object = MibScalar
mp800mkTrapParameter = _Mp800mkTrapParameter_Object(
    (1, 3, 6, 1, 4, 1, 34300, 3, 10, 1),
    _Mp800mkTrapParameter_Type()
)
mp800mkTrapParameter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp800mkTrapParameter.setStatus("current")
_Mp800mkTrapValue_Type = DisplayString
_Mp800mkTrapValue_Object = MibScalar
mp800mkTrapValue = _Mp800mkTrapValue_Object(
    (1, 3, 6, 1, 4, 1, 34300, 3, 10, 2),
    _Mp800mkTrapValue_Type()
)
mp800mkTrapValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp800mkTrapValue.setStatus("current")
_Mp800mkTrapComment_Type = DisplayString
_Mp800mkTrapComment_Object = MibScalar
mp800mkTrapComment = _Mp800mkTrapComment_Object(
    (1, 3, 6, 1, 4, 1, 34300, 3, 10, 3),
    _Mp800mkTrapComment_Type()
)
mp800mkTrapComment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mp800mkTrapComment.setStatus("current")
_OmsOperationAlarmTraps_ObjectIdentity = ObjectIdentity
omsOperationAlarmTraps = _OmsOperationAlarmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34300, 3, 20)
)
_OmsOperationOkTraps_ObjectIdentity = ObjectIdentity
omsOperationOkTraps = _OmsOperationOkTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34300, 3, 21)
)

# Managed Objects groups

eltrapObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 34300, 3, 101)
)
eltrapObjectGroup.setObjects(
      *(("ELTEX-SMI", "mcTrapExState"),
        ("ELTEX-SMI", "mcTrapLParam1"),
        ("ELTEX-SMI", "mcTrapLParam2"),
        ("ELTEX-SMI", "mcTrapLParam3"),
        ("ELTEX-SMI", "mcTrapID"),
        ("ELTEX-SMI", "mcTrapDescr"),
        ("ELTEX-SMI", "mcTrapRestoredAlarmID"),
        ("ELTEX-SMI", "mcTrapSyncType"),
        ("ELTEX-SMI", "mcReservedFlag"))
)
if mibBuilder.loadTexts:
    eltrapObjectGroup.setStatus("current")


# Notification objects

mc240StreamAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 34300, 3, 3, 1)
)
mc240StreamAlarmTrap.setObjects(
      *(("ELTEX-SMI", "mcTrapExState"),
        ("ELTEX-SMI", "mcTrapLParam1"),
        ("ELTEX-SMI", "mcTrapLParam2"),
        ("ELTEX-SMI", "mcTrapLParam3"),
        ("ELTEX-SMI", "mcTrapID"),
        ("ELTEX-SMI", "mcTrapDescr"),
        ("ELTEX-SMI", "mcTrapRestoredAlarmID"),
        ("ELTEX-SMI", "mcTrapSyncType"),
        ("ELTEX-SMI", "mcReservedFlag"))
)
if mibBuilder.loadTexts:
    mc240StreamAlarmTrap.setStatus(
        "current"
    )

mc240SyncAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 34300, 3, 3, 2)
)
mc240SyncAlarmTrap.setObjects(
      *(("ELTEX-SMI", "mcTrapExState"),
        ("ELTEX-SMI", "mcTrapLParam1"),
        ("ELTEX-SMI", "mcTrapLParam2"),
        ("ELTEX-SMI", "mcTrapLParam3"),
        ("ELTEX-SMI", "mcTrapID"),
        ("ELTEX-SMI", "mcTrapDescr"),
        ("ELTEX-SMI", "mcTrapRestoredAlarmID"),
        ("ELTEX-SMI", "mcTrapSyncType"),
        ("ELTEX-SMI", "mcReservedFlag"))
)
if mibBuilder.loadTexts:
    mc240SyncAlarmTrap.setStatus(
        "current"
    )

mc240ss7LinkAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 34300, 3, 3, 3)
)
mc240ss7LinkAlarmTrap.setObjects(
      *(("ELTEX-SMI", "mcTrapExState"),
        ("ELTEX-SMI", "mcTrapLParam1"),
        ("ELTEX-SMI", "mcTrapLParam2"),
        ("ELTEX-SMI", "mcTrapLParam3"),
        ("ELTEX-SMI", "mcTrapID"),
        ("ELTEX-SMI", "mcTrapDescr"),
        ("ELTEX-SMI", "mcTrapRestoredAlarmID"),
        ("ELTEX-SMI", "mcTrapSyncType"),
        ("ELTEX-SMI", "mcReservedFlag"))
)
if mibBuilder.loadTexts:
    mc240ss7LinkAlarmTrap.setStatus(
        "current"
    )

mc240ss7LinksetAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 34300, 3, 3, 4)
)
mc240ss7LinksetAlarmTrap.setObjects(
      *(("ELTEX-SMI", "mcTrapExState"),
        ("ELTEX-SMI", "mcTrapLParam1"),
        ("ELTEX-SMI", "mcTrapLParam2"),
        ("ELTEX-SMI", "mcTrapLParam3"),
        ("ELTEX-SMI", "mcTrapID"),
        ("ELTEX-SMI", "mcTrapDescr"),
        ("ELTEX-SMI", "mcTrapRestoredAlarmID"),
        ("ELTEX-SMI", "mcTrapSyncType"),
        ("ELTEX-SMI", "mcReservedFlag"))
)
if mibBuilder.loadTexts:
    mc240ss7LinksetAlarmTrap.setStatus(
        "current"
    )

mc240FileAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 34300, 3, 3, 5)
)
mc240FileAlarmTrap.setObjects(
      *(("ELTEX-SMI", "mcTrapExState"),
        ("ELTEX-SMI", "mcTrapLParam1"),
        ("ELTEX-SMI", "mcTrapLParam2"),
        ("ELTEX-SMI", "mcTrapLParam3"),
        ("ELTEX-SMI", "mcTrapID"),
        ("ELTEX-SMI", "mcTrapDescr"),
        ("ELTEX-SMI", "mcTrapRestoredAlarmID"),
        ("ELTEX-SMI", "mcTrapSyncType"),
        ("ELTEX-SMI", "mcReservedFlag"))
)
if mibBuilder.loadTexts:
    mc240FileAlarmTrap.setStatus(
        "current"
    )

mc240CardAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 34300, 3, 3, 6)
)
mc240CardAlarmTrap.setObjects(
      *(("ELTEX-SMI", "mcTrapExState"),
        ("ELTEX-SMI", "mcTrapLParam1"),
        ("ELTEX-SMI", "mcTrapLParam2"),
        ("ELTEX-SMI", "mcTrapLParam3"),
        ("ELTEX-SMI", "mcTrapID"),
        ("ELTEX-SMI", "mcTrapDescr"),
        ("ELTEX-SMI", "mcTrapRestoredAlarmID"),
        ("ELTEX-SMI", "mcTrapSyncType"),
        ("ELTEX-SMI", "mcReservedFlag"))
)
if mibBuilder.loadTexts:
    mc240CardAlarmTrap.setStatus(
        "current"
    )

mxlDPSAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 34300, 3, 3, 7)
)
mxlDPSAlarmTrap.setObjects(
      *(("ELTEX-SMI", "mcTrapExState"),
        ("ELTEX-SMI", "mcTrapLParam1"),
        ("ELTEX-SMI", "mcTrapLParam2"),
        ("ELTEX-SMI", "mcTrapLParam3"),
        ("ELTEX-SMI", "mcTrapID"),
        ("ELTEX-SMI", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    mxlDPSAlarmTrap.setStatus(
        "current"
    )

mxlTELEAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 34300, 3, 3, 8)
)
mxlTELEAlarmTrap.setObjects(
      *(("ELTEX-SMI", "mcTrapExState"),
        ("ELTEX-SMI", "mcTrapLParam1"),
        ("ELTEX-SMI", "mcTrapLParam2"),
        ("ELTEX-SMI", "mcTrapLParam3"),
        ("ELTEX-SMI", "mcTrapID"),
        ("ELTEX-SMI", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    mxlTELEAlarmTrap.setStatus(
        "current"
    )

mc240UPSAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 34300, 3, 3, 9)
)
mc240UPSAlarmTrap.setObjects(
      *(("ELTEX-SMI", "mcTrapExState"),
        ("ELTEX-SMI", "mcTrapLParam1"),
        ("ELTEX-SMI", "mcTrapLParam2"),
        ("ELTEX-SMI", "mcTrapLParam3"),
        ("ELTEX-SMI", "mcTrapID"),
        ("ELTEX-SMI", "mcTrapDescr"),
        ("ELTEX-SMI", "mcTrapRestoredAlarmID"),
        ("ELTEX-SMI", "mcTrapSyncType"),
        ("ELTEX-SMI", "mcReservedFlag"))
)
if mibBuilder.loadTexts:
    mc240UPSAlarmTrap.setStatus(
        "current"
    )

mc240SensAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 34300, 3, 3, 10)
)
mc240SensAlarmTrap.setObjects(
      *(("ELTEX-SMI", "mcTrapExState"),
        ("ELTEX-SMI", "mcTrapLParam1"),
        ("ELTEX-SMI", "mcTrapLParam2"),
        ("ELTEX-SMI", "mcTrapLParam3"),
        ("ELTEX-SMI", "mcTrapID"),
        ("ELTEX-SMI", "mcTrapDescr"),
        ("ELTEX-SMI", "mcTrapRestoredAlarmID"),
        ("ELTEX-SMI", "mcTrapSyncType"),
        ("ELTEX-SMI", "mcReservedFlag"))
)
if mibBuilder.loadTexts:
    mc240SensAlarmTrap.setStatus(
        "current"
    )

dslamLinkDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 34300, 3, 3, 11)
)
dslamLinkDownTrap.setObjects(
      *(("ELTEX-SMI", "mcTrapExState"),
        ("ELTEX-SMI", "mcTrapLParam1"),
        ("ELTEX-SMI", "mcTrapLParam2"),
        ("ELTEX-SMI", "mcTrapLParam3"),
        ("ELTEX-SMI", "mcTrapID"),
        ("ELTEX-SMI", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    dslamLinkDownTrap.setStatus(
        "current"
    )

dslamDSRateAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 34300, 3, 3, 12)
)
dslamDSRateAlarmTrap.setObjects(
      *(("ELTEX-SMI", "mcTrapExState"),
        ("ELTEX-SMI", "mcTrapLParam1"),
        ("ELTEX-SMI", "mcTrapLParam2"),
        ("ELTEX-SMI", "mcTrapLParam3"),
        ("ELTEX-SMI", "mcTrapID"),
        ("ELTEX-SMI", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    dslamDSRateAlarmTrap.setStatus(
        "current"
    )

dslamUSRateAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 34300, 3, 3, 13)
)
dslamUSRateAlarmTrap.setObjects(
      *(("ELTEX-SMI", "mcTrapExState"),
        ("ELTEX-SMI", "mcTrapLParam1"),
        ("ELTEX-SMI", "mcTrapLParam2"),
        ("ELTEX-SMI", "mcTrapLParam3"),
        ("ELTEX-SMI", "mcTrapID"),
        ("ELTEX-SMI", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    dslamUSRateAlarmTrap.setStatus(
        "current"
    )

ponONUAuthAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 34300, 3, 3, 14)
)
ponONUAuthAlarmTrap.setObjects(
      *(("ELTEX-SMI", "mcTrapExState"),
        ("ELTEX-SMI", "mcTrapLParam1"),
        ("ELTEX-SMI", "mcTrapLParam2"),
        ("ELTEX-SMI", "mcTrapLParam3"),
        ("ELTEX-SMI", "mcTrapID"),
        ("ELTEX-SMI", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ponONUAuthAlarmTrap.setStatus(
        "current"
    )

ponEthAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 34300, 3, 3, 15)
)
ponEthAlarmTrap.setObjects(
      *(("ELTEX-SMI", "mcTrapExState"),
        ("ELTEX-SMI", "mcTrapLParam1"),
        ("ELTEX-SMI", "mcTrapLParam2"),
        ("ELTEX-SMI", "mcTrapLParam3"),
        ("ELTEX-SMI", "mcTrapID"),
        ("ELTEX-SMI", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ponEthAlarmTrap.setStatus(
        "current"
    )

ponOpticalAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 34300, 3, 3, 16)
)
ponOpticalAlarmTrap.setObjects(
      *(("ELTEX-SMI", "mcTrapExState"),
        ("ELTEX-SMI", "mcTrapLParam1"),
        ("ELTEX-SMI", "mcTrapLParam2"),
        ("ELTEX-SMI", "mcTrapLParam3"),
        ("ELTEX-SMI", "mcTrapID"),
        ("ELTEX-SMI", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ponOpticalAlarmTrap.setStatus(
        "current"
    )

dslamOverheatAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 34300, 3, 3, 17)
)
dslamOverheatAlarmTrap.setObjects(
      *(("ELTEX-SMI", "mcTrapExState"),
        ("ELTEX-SMI", "mcTrapLParam1"),
        ("ELTEX-SMI", "mcTrapLParam2"),
        ("ELTEX-SMI", "mcTrapLParam3"),
        ("ELTEX-SMI", "mcTrapID"),
        ("ELTEX-SMI", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    dslamOverheatAlarmTrap.setStatus(
        "current"
    )

dslamVoltageAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 34300, 3, 3, 18)
)
dslamVoltageAlarmTrap.setObjects(
      *(("ELTEX-SMI", "mcTrapExState"),
        ("ELTEX-SMI", "mcTrapLParam1"),
        ("ELTEX-SMI", "mcTrapLParam2"),
        ("ELTEX-SMI", "mcTrapLParam3"),
        ("ELTEX-SMI", "mcTrapID"),
        ("ELTEX-SMI", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    dslamVoltageAlarmTrap.setStatus(
        "current"
    )

dslamSessionAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 34300, 3, 3, 19)
)
dslamSessionAlarmTrap.setObjects(
      *(("ELTEX-SMI", "mcTrapExState"),
        ("ELTEX-SMI", "mcTrapLParam1"),
        ("ELTEX-SMI", "mcTrapLParam2"),
        ("ELTEX-SMI", "mcTrapLParam3"),
        ("ELTEX-SMI", "mcTrapID"),
        ("ELTEX-SMI", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    dslamSessionAlarmTrap.setStatus(
        "current"
    )

dslamEthLinkAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 34300, 3, 3, 20)
)
dslamEthLinkAlarmTrap.setObjects(
      *(("ELTEX-SMI", "mcTrapExState"),
        ("ELTEX-SMI", "mcTrapLParam1"),
        ("ELTEX-SMI", "mcTrapLParam2"),
        ("ELTEX-SMI", "mcTrapLParam3"),
        ("ELTEX-SMI", "mcTrapID"),
        ("ELTEX-SMI", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    dslamEthLinkAlarmTrap.setStatus(
        "current"
    )

mc240StreamOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 34300, 3, 4, 1)
)
mc240StreamOkTrap.setObjects(
      *(("ELTEX-SMI", "mcTrapExState"),
        ("ELTEX-SMI", "mcTrapLParam1"),
        ("ELTEX-SMI", "mcTrapLParam2"),
        ("ELTEX-SMI", "mcTrapLParam3"),
        ("ELTEX-SMI", "mcTrapID"),
        ("ELTEX-SMI", "mcTrapDescr"),
        ("ELTEX-SMI", "mcTrapRestoredAlarmID"),
        ("ELTEX-SMI", "mcTrapSyncType"),
        ("ELTEX-SMI", "mcReservedFlag"))
)
if mibBuilder.loadTexts:
    mc240StreamOkTrap.setStatus(
        "current"
    )

mc240SyncOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 34300, 3, 4, 2)
)
mc240SyncOkTrap.setObjects(
      *(("ELTEX-SMI", "mcTrapExState"),
        ("ELTEX-SMI", "mcTrapLParam1"),
        ("ELTEX-SMI", "mcTrapLParam2"),
        ("ELTEX-SMI", "mcTrapLParam3"),
        ("ELTEX-SMI", "mcTrapID"),
        ("ELTEX-SMI", "mcTrapDescr"),
        ("ELTEX-SMI", "mcTrapRestoredAlarmID"),
        ("ELTEX-SMI", "mcTrapSyncType"),
        ("ELTEX-SMI", "mcReservedFlag"))
)
if mibBuilder.loadTexts:
    mc240SyncOkTrap.setStatus(
        "current"
    )

mc240ss7LinkOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 34300, 3, 4, 3)
)
mc240ss7LinkOkTrap.setObjects(
      *(("ELTEX-SMI", "mcTrapExState"),
        ("ELTEX-SMI", "mcTrapLParam1"),
        ("ELTEX-SMI", "mcTrapLParam2"),
        ("ELTEX-SMI", "mcTrapLParam3"),
        ("ELTEX-SMI", "mcTrapID"),
        ("ELTEX-SMI", "mcTrapDescr"),
        ("ELTEX-SMI", "mcTrapRestoredAlarmID"),
        ("ELTEX-SMI", "mcTrapSyncType"),
        ("ELTEX-SMI", "mcReservedFlag"))
)
if mibBuilder.loadTexts:
    mc240ss7LinkOkTrap.setStatus(
        "current"
    )

mc240ss7LinksetOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 34300, 3, 4, 4)
)
mc240ss7LinksetOkTrap.setObjects(
      *(("ELTEX-SMI", "mcTrapExState"),
        ("ELTEX-SMI", "mcTrapLParam1"),
        ("ELTEX-SMI", "mcTrapLParam2"),
        ("ELTEX-SMI", "mcTrapLParam3"),
        ("ELTEX-SMI", "mcTrapID"),
        ("ELTEX-SMI", "mcTrapDescr"),
        ("ELTEX-SMI", "mcTrapRestoredAlarmID"),
        ("ELTEX-SMI", "mcTrapSyncType"),
        ("ELTEX-SMI", "mcReservedFlag"))
)
if mibBuilder.loadTexts:
    mc240ss7LinksetOkTrap.setStatus(
        "current"
    )

mc240FileOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 34300, 3, 4, 5)
)
mc240FileOkTrap.setObjects(
      *(("ELTEX-SMI", "mcTrapExState"),
        ("ELTEX-SMI", "mcTrapLParam1"),
        ("ELTEX-SMI", "mcTrapLParam2"),
        ("ELTEX-SMI", "mcTrapLParam3"),
        ("ELTEX-SMI", "mcTrapID"),
        ("ELTEX-SMI", "mcTrapDescr"),
        ("ELTEX-SMI", "mcTrapRestoredAlarmID"),
        ("ELTEX-SMI", "mcTrapSyncType"),
        ("ELTEX-SMI", "mcReservedFlag"))
)
if mibBuilder.loadTexts:
    mc240FileOkTrap.setStatus(
        "current"
    )

mc240CardOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 34300, 3, 4, 6)
)
mc240CardOkTrap.setObjects(
      *(("ELTEX-SMI", "mcTrapExState"),
        ("ELTEX-SMI", "mcTrapLParam1"),
        ("ELTEX-SMI", "mcTrapLParam2"),
        ("ELTEX-SMI", "mcTrapLParam3"),
        ("ELTEX-SMI", "mcTrapID"),
        ("ELTEX-SMI", "mcTrapDescr"),
        ("ELTEX-SMI", "mcTrapRestoredAlarmID"),
        ("ELTEX-SMI", "mcTrapSyncType"),
        ("ELTEX-SMI", "mcReservedFlag"))
)
if mibBuilder.loadTexts:
    mc240CardOkTrap.setStatus(
        "current"
    )

mxlDPSOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 34300, 3, 4, 7)
)
mxlDPSOkTrap.setObjects(
      *(("ELTEX-SMI", "mcTrapExState"),
        ("ELTEX-SMI", "mcTrapLParam1"),
        ("ELTEX-SMI", "mcTrapLParam2"),
        ("ELTEX-SMI", "mcTrapLParam3"),
        ("ELTEX-SMI", "mcTrapID"),
        ("ELTEX-SMI", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    mxlDPSOkTrap.setStatus(
        "current"
    )

mxlTELEOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 34300, 3, 4, 8)
)
mxlTELEOkTrap.setObjects(
      *(("ELTEX-SMI", "mcTrapExState"),
        ("ELTEX-SMI", "mcTrapLParam1"),
        ("ELTEX-SMI", "mcTrapLParam2"),
        ("ELTEX-SMI", "mcTrapLParam3"),
        ("ELTEX-SMI", "mcTrapID"),
        ("ELTEX-SMI", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    mxlTELEOkTrap.setStatus(
        "current"
    )

mc240UPSOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 34300, 3, 4, 9)
)
mc240UPSOkTrap.setObjects(
      *(("ELTEX-SMI", "mcTrapExState"),
        ("ELTEX-SMI", "mcTrapLParam1"),
        ("ELTEX-SMI", "mcTrapLParam2"),
        ("ELTEX-SMI", "mcTrapLParam3"),
        ("ELTEX-SMI", "mcTrapID"),
        ("ELTEX-SMI", "mcTrapDescr"),
        ("ELTEX-SMI", "mcTrapRestoredAlarmID"),
        ("ELTEX-SMI", "mcTrapSyncType"),
        ("ELTEX-SMI", "mcReservedFlag"))
)
if mibBuilder.loadTexts:
    mc240UPSOkTrap.setStatus(
        "current"
    )

mc240SensOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 34300, 3, 4, 10)
)
mc240SensOkTrap.setObjects(
      *(("ELTEX-SMI", "mcTrapExState"),
        ("ELTEX-SMI", "mcTrapLParam1"),
        ("ELTEX-SMI", "mcTrapLParam2"),
        ("ELTEX-SMI", "mcTrapLParam3"),
        ("ELTEX-SMI", "mcTrapID"),
        ("ELTEX-SMI", "mcTrapDescr"),
        ("ELTEX-SMI", "mcTrapRestoredAlarmID"),
        ("ELTEX-SMI", "mcTrapSyncType"),
        ("ELTEX-SMI", "mcReservedFlag"))
)
if mibBuilder.loadTexts:
    mc240SensOkTrap.setStatus(
        "current"
    )

dslamLinkUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 34300, 3, 4, 11)
)
dslamLinkUpTrap.setObjects(
      *(("ELTEX-SMI", "mcTrapExState"),
        ("ELTEX-SMI", "mcTrapLParam1"),
        ("ELTEX-SMI", "mcTrapLParam2"),
        ("ELTEX-SMI", "mcTrapLParam3"),
        ("ELTEX-SMI", "mcTrapID"),
        ("ELTEX-SMI", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    dslamLinkUpTrap.setStatus(
        "current"
    )

dslamDSRateOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 34300, 3, 4, 12)
)
dslamDSRateOkTrap.setObjects(
      *(("ELTEX-SMI", "mcTrapExState"),
        ("ELTEX-SMI", "mcTrapLParam1"),
        ("ELTEX-SMI", "mcTrapLParam2"),
        ("ELTEX-SMI", "mcTrapLParam3"),
        ("ELTEX-SMI", "mcTrapID"),
        ("ELTEX-SMI", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    dslamDSRateOkTrap.setStatus(
        "current"
    )

dslamUSRateOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 34300, 3, 4, 13)
)
dslamUSRateOkTrap.setObjects(
      *(("ELTEX-SMI", "mcTrapExState"),
        ("ELTEX-SMI", "mcTrapLParam1"),
        ("ELTEX-SMI", "mcTrapLParam2"),
        ("ELTEX-SMI", "mcTrapLParam3"),
        ("ELTEX-SMI", "mcTrapID"),
        ("ELTEX-SMI", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    dslamUSRateOkTrap.setStatus(
        "current"
    )

ponONUAuthOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 34300, 3, 4, 14)
)
ponONUAuthOkTrap.setObjects(
      *(("ELTEX-SMI", "mcTrapExState"),
        ("ELTEX-SMI", "mcTrapLParam1"),
        ("ELTEX-SMI", "mcTrapLParam2"),
        ("ELTEX-SMI", "mcTrapLParam3"),
        ("ELTEX-SMI", "mcTrapID"),
        ("ELTEX-SMI", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ponONUAuthOkTrap.setStatus(
        "current"
    )

ponEthOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 34300, 3, 4, 15)
)
ponEthOkTrap.setObjects(
      *(("ELTEX-SMI", "mcTrapExState"),
        ("ELTEX-SMI", "mcTrapLParam1"),
        ("ELTEX-SMI", "mcTrapLParam2"),
        ("ELTEX-SMI", "mcTrapLParam3"),
        ("ELTEX-SMI", "mcTrapID"),
        ("ELTEX-SMI", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ponEthOkTrap.setStatus(
        "current"
    )

ponOpticalOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 34300, 3, 4, 16)
)
ponOpticalOkTrap.setObjects(
      *(("ELTEX-SMI", "mcTrapExState"),
        ("ELTEX-SMI", "mcTrapLParam1"),
        ("ELTEX-SMI", "mcTrapLParam2"),
        ("ELTEX-SMI", "mcTrapLParam3"),
        ("ELTEX-SMI", "mcTrapID"),
        ("ELTEX-SMI", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ponOpticalOkTrap.setStatus(
        "current"
    )

dslamOverheatOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 34300, 3, 4, 17)
)
dslamOverheatOkTrap.setObjects(
      *(("ELTEX-SMI", "mcTrapExState"),
        ("ELTEX-SMI", "mcTrapLParam1"),
        ("ELTEX-SMI", "mcTrapLParam2"),
        ("ELTEX-SMI", "mcTrapLParam3"),
        ("ELTEX-SMI", "mcTrapID"),
        ("ELTEX-SMI", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    dslamOverheatOkTrap.setStatus(
        "current"
    )

dslamVoltageOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 34300, 3, 4, 18)
)
dslamVoltageOkTrap.setObjects(
      *(("ELTEX-SMI", "mcTrapExState"),
        ("ELTEX-SMI", "mcTrapLParam1"),
        ("ELTEX-SMI", "mcTrapLParam2"),
        ("ELTEX-SMI", "mcTrapLParam3"),
        ("ELTEX-SMI", "mcTrapID"),
        ("ELTEX-SMI", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    dslamVoltageOkTrap.setStatus(
        "current"
    )

dslamSessionOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 34300, 3, 4, 19)
)
dslamSessionOkTrap.setObjects(
      *(("ELTEX-SMI", "mcTrapExState"),
        ("ELTEX-SMI", "mcTrapLParam1"),
        ("ELTEX-SMI", "mcTrapLParam2"),
        ("ELTEX-SMI", "mcTrapLParam3"),
        ("ELTEX-SMI", "mcTrapID"),
        ("ELTEX-SMI", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    dslamSessionOkTrap.setStatus(
        "current"
    )

dslamEthLinkOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 34300, 3, 4, 20)
)
dslamEthLinkOkTrap.setObjects(
      *(("ELTEX-SMI", "mcTrapExState"),
        ("ELTEX-SMI", "mcTrapLParam1"),
        ("ELTEX-SMI", "mcTrapLParam2"),
        ("ELTEX-SMI", "mcTrapLParam3"),
        ("ELTEX-SMI", "mcTrapID"),
        ("ELTEX-SMI", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    dslamEthLinkOkTrap.setStatus(
        "current"
    )

mp800mkMPStatusAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 34300, 3, 8, 1)
)
mp800mkMPStatusAlarmTrap.setObjects(
      *(("ELTEX-SMI", "mp800mkTrapParameter"),
        ("ELTEX-SMI", "mp800mkTrapValue"),
        ("ELTEX-SMI", "mp800mkTrapComment"))
)
if mibBuilder.loadTexts:
    mp800mkMPStatusAlarmTrap.setStatus(
        "current"
    )

mp800mkInpParmAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 34300, 3, 8, 2)
)
mp800mkInpParmAlarmTrap.setObjects(
      *(("ELTEX-SMI", "mp800mkTrapParameter"),
        ("ELTEX-SMI", "mp800mkTrapValue"),
        ("ELTEX-SMI", "mp800mkTrapComment"))
)
if mibBuilder.loadTexts:
    mp800mkInpParmAlarmTrap.setStatus(
        "current"
    )

mp800mkUEPConfAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 34300, 3, 8, 3)
)
mp800mkUEPConfAlarmTrap.setObjects(
      *(("ELTEX-SMI", "mp800mkTrapParameter"),
        ("ELTEX-SMI", "mp800mkTrapValue"),
        ("ELTEX-SMI", "mp800mkTrapComment"))
)
if mibBuilder.loadTexts:
    mp800mkUEPConfAlarmTrap.setStatus(
        "current"
    )

mp800mkTMAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 34300, 3, 8, 4)
)
mp800mkTMAlarmTrap.setObjects(
      *(("ELTEX-SMI", "mp800mkTrapParameter"),
        ("ELTEX-SMI", "mp800mkTrapValue"),
        ("ELTEX-SMI", "mp800mkTrapComment"))
)
if mibBuilder.loadTexts:
    mp800mkTMAlarmTrap.setStatus(
        "current"
    )

mp800mkACVMAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 34300, 3, 8, 5)
)
mp800mkACVMAlarmTrap.setObjects(
      *(("ELTEX-SMI", "mp800mkTrapParameter"),
        ("ELTEX-SMI", "mp800mkTrapValue"),
        ("ELTEX-SMI", "mp800mkTrapComment"))
)
if mibBuilder.loadTexts:
    mp800mkACVMAlarmTrap.setStatus(
        "current"
    )

mp800mkIbatMAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 34300, 3, 8, 6)
)
mp800mkIbatMAlarmTrap.setObjects(
      *(("ELTEX-SMI", "mp800mkTrapParameter"),
        ("ELTEX-SMI", "mp800mkTrapValue"),
        ("ELTEX-SMI", "mp800mkTrapComment"))
)
if mibBuilder.loadTexts:
    mp800mkIbatMAlarmTrap.setStatus(
        "current"
    )

mp800mkVbatMAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 34300, 3, 8, 7)
)
mp800mkVbatMAlarmTrap.setObjects(
      *(("ELTEX-SMI", "mp800mkTrapParameter"),
        ("ELTEX-SMI", "mp800mkTrapValue"),
        ("ELTEX-SMI", "mp800mkTrapComment"))
)
if mibBuilder.loadTexts:
    mp800mkVbatMAlarmTrap.setStatus(
        "current"
    )

mp800mkVbatChAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 34300, 3, 8, 8)
)
mp800mkVbatChAlarmTrap.setObjects(
      *(("ELTEX-SMI", "mp800mkTrapParameter"),
        ("ELTEX-SMI", "mp800mkTrapValue"),
        ("ELTEX-SMI", "mp800mkTrapComment"))
)
if mibBuilder.loadTexts:
    mp800mkVbatChAlarmTrap.setStatus(
        "current"
    )

mp800mkRlsDevAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 34300, 3, 8, 9)
)
mp800mkRlsDevAlarmTrap.setObjects(
      *(("ELTEX-SMI", "mp800mkTrapParameter"),
        ("ELTEX-SMI", "mp800mkTrapValue"),
        ("ELTEX-SMI", "mp800mkTrapComment"))
)
if mibBuilder.loadTexts:
    mp800mkRlsDevAlarmTrap.setStatus(
        "current"
    )

mp800mkDVcellAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 34300, 3, 8, 10)
)
mp800mkDVcellAlarmTrap.setObjects(
      *(("ELTEX-SMI", "mp800mkTrapParameter"),
        ("ELTEX-SMI", "mp800mkTrapValue"),
        ("ELTEX-SMI", "mp800mkTrapComment"))
)
if mibBuilder.loadTexts:
    mp800mkDVcellAlarmTrap.setStatus(
        "current"
    )

mp800mkACVAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 34300, 3, 8, 11)
)
mp800mkACVAlarmTrap.setObjects(
      *(("ELTEX-SMI", "mp800mkTrapParameter"),
        ("ELTEX-SMI", "mp800mkTrapValue"),
        ("ELTEX-SMI", "mp800mkTrapComment"))
)
if mibBuilder.loadTexts:
    mp800mkACVAlarmTrap.setStatus(
        "current"
    )

mp800mkBatChargeAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 34300, 3, 8, 12)
)
mp800mkBatChargeAlarmTrap.setObjects(
      *(("ELTEX-SMI", "mp800mkTrapParameter"),
        ("ELTEX-SMI", "mp800mkTrapValue"),
        ("ELTEX-SMI", "mp800mkTrapComment"))
)
if mibBuilder.loadTexts:
    mp800mkBatChargeAlarmTrap.setStatus(
        "current"
    )

mp800mkIloadAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 34300, 3, 8, 13)
)
mp800mkIloadAlarmTrap.setObjects(
      *(("ELTEX-SMI", "mp800mkTrapParameter"),
        ("ELTEX-SMI", "mp800mkTrapValue"),
        ("ELTEX-SMI", "mp800mkTrapComment"))
)
if mibBuilder.loadTexts:
    mp800mkIloadAlarmTrap.setStatus(
        "current"
    )

mp800mkIbatChAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 34300, 3, 8, 14)
)
mp800mkIbatChAlarmTrap.setObjects(
      *(("ELTEX-SMI", "mp800mkTrapParameter"),
        ("ELTEX-SMI", "mp800mkTrapValue"),
        ("ELTEX-SMI", "mp800mkTrapComment"))
)
if mibBuilder.loadTexts:
    mp800mkIbatChAlarmTrap.setStatus(
        "current"
    )

mp800mkSuppAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 34300, 3, 8, 15)
)
mp800mkSuppAlarmTrap.setObjects(
      *(("ELTEX-SMI", "mp800mkTrapParameter"),
        ("ELTEX-SMI", "mp800mkTrapValue"),
        ("ELTEX-SMI", "mp800mkTrapComment"))
)
if mibBuilder.loadTexts:
    mp800mkSuppAlarmTrap.setStatus(
        "current"
    )

mp800mkBatConnAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 34300, 3, 8, 16)
)
mp800mkBatConnAlarmTrap.setObjects(
      *(("ELTEX-SMI", "mp800mkTrapParameter"),
        ("ELTEX-SMI", "mp800mkTrapValue"),
        ("ELTEX-SMI", "mp800mkTrapComment"))
)
if mibBuilder.loadTexts:
    mp800mkBatConnAlarmTrap.setStatus(
        "current"
    )

mp800mkMPStatusOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 34300, 3, 9, 1)
)
mp800mkMPStatusOkTrap.setObjects(
      *(("ELTEX-SMI", "mp800mkTrapParameter"),
        ("ELTEX-SMI", "mp800mkTrapValue"),
        ("ELTEX-SMI", "mp800mkTrapComment"))
)
if mibBuilder.loadTexts:
    mp800mkMPStatusOkTrap.setStatus(
        "current"
    )

mp800mkInpParmOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 34300, 3, 9, 2)
)
mp800mkInpParmOkTrap.setObjects(
      *(("ELTEX-SMI", "mp800mkTrapParameter"),
        ("ELTEX-SMI", "mp800mkTrapValue"),
        ("ELTEX-SMI", "mp800mkTrapComment"))
)
if mibBuilder.loadTexts:
    mp800mkInpParmOkTrap.setStatus(
        "current"
    )

mp800mkUEPConfOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 34300, 3, 9, 3)
)
mp800mkUEPConfOkTrap.setObjects(
      *(("ELTEX-SMI", "mp800mkTrapParameter"),
        ("ELTEX-SMI", "mp800mkTrapValue"),
        ("ELTEX-SMI", "mp800mkTrapComment"))
)
if mibBuilder.loadTexts:
    mp800mkUEPConfOkTrap.setStatus(
        "current"
    )

mp800mkTMOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 34300, 3, 9, 4)
)
mp800mkTMOkTrap.setObjects(
      *(("ELTEX-SMI", "mp800mkTrapParameter"),
        ("ELTEX-SMI", "mp800mkTrapValue"),
        ("ELTEX-SMI", "mp800mkTrapComment"))
)
if mibBuilder.loadTexts:
    mp800mkTMOkTrap.setStatus(
        "current"
    )

mp800mkACVMOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 34300, 3, 9, 5)
)
mp800mkACVMOkTrap.setObjects(
      *(("ELTEX-SMI", "mp800mkTrapParameter"),
        ("ELTEX-SMI", "mp800mkTrapValue"),
        ("ELTEX-SMI", "mp800mkTrapComment"))
)
if mibBuilder.loadTexts:
    mp800mkACVMOkTrap.setStatus(
        "current"
    )

mp800mkIbatMOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 34300, 3, 9, 6)
)
mp800mkIbatMOkTrap.setObjects(
      *(("ELTEX-SMI", "mp800mkTrapParameter"),
        ("ELTEX-SMI", "mp800mkTrapValue"),
        ("ELTEX-SMI", "mp800mkTrapComment"))
)
if mibBuilder.loadTexts:
    mp800mkIbatMOkTrap.setStatus(
        "current"
    )

mp800mkVbatMOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 34300, 3, 9, 7)
)
mp800mkVbatMOkTrap.setObjects(
      *(("ELTEX-SMI", "mp800mkTrapParameter"),
        ("ELTEX-SMI", "mp800mkTrapValue"),
        ("ELTEX-SMI", "mp800mkTrapComment"))
)
if mibBuilder.loadTexts:
    mp800mkVbatMOkTrap.setStatus(
        "current"
    )

mp800mkVbatChOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 34300, 3, 9, 8)
)
mp800mkVbatChOkTrap.setObjects(
      *(("ELTEX-SMI", "mp800mkTrapParameter"),
        ("ELTEX-SMI", "mp800mkTrapValue"),
        ("ELTEX-SMI", "mp800mkTrapComment"))
)
if mibBuilder.loadTexts:
    mp800mkVbatChOkTrap.setStatus(
        "current"
    )

mp800mkRlsDevOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 34300, 3, 9, 9)
)
mp800mkRlsDevOkTrap.setObjects(
      *(("ELTEX-SMI", "mp800mkTrapParameter"),
        ("ELTEX-SMI", "mp800mkTrapValue"),
        ("ELTEX-SMI", "mp800mkTrapComment"))
)
if mibBuilder.loadTexts:
    mp800mkRlsDevOkTrap.setStatus(
        "current"
    )

mp800mkDVcellOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 34300, 3, 9, 10)
)
mp800mkDVcellOkTrap.setObjects(
      *(("ELTEX-SMI", "mp800mkTrapParameter"),
        ("ELTEX-SMI", "mp800mkTrapValue"),
        ("ELTEX-SMI", "mp800mkTrapComment"))
)
if mibBuilder.loadTexts:
    mp800mkDVcellOkTrap.setStatus(
        "current"
    )

mp800mkACVOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 34300, 3, 9, 11)
)
mp800mkACVOkTrap.setObjects(
      *(("ELTEX-SMI", "mp800mkTrapParameter"),
        ("ELTEX-SMI", "mp800mkTrapValue"),
        ("ELTEX-SMI", "mp800mkTrapComment"))
)
if mibBuilder.loadTexts:
    mp800mkACVOkTrap.setStatus(
        "current"
    )

mp800mkBatChargeOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 34300, 3, 9, 12)
)
mp800mkBatChargeOkTrap.setObjects(
      *(("ELTEX-SMI", "mp800mkTrapParameter"),
        ("ELTEX-SMI", "mp800mkTrapValue"),
        ("ELTEX-SMI", "mp800mkTrapComment"))
)
if mibBuilder.loadTexts:
    mp800mkBatChargeOkTrap.setStatus(
        "current"
    )

mp800mkIloadOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 34300, 3, 9, 13)
)
mp800mkIloadOkTrap.setObjects(
      *(("ELTEX-SMI", "mp800mkTrapParameter"),
        ("ELTEX-SMI", "mp800mkTrapValue"),
        ("ELTEX-SMI", "mp800mkTrapComment"))
)
if mibBuilder.loadTexts:
    mp800mkIloadOkTrap.setStatus(
        "current"
    )

mp800mkIbatChOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 34300, 3, 9, 14)
)
mp800mkIbatChOkTrap.setObjects(
      *(("ELTEX-SMI", "mp800mkTrapParameter"),
        ("ELTEX-SMI", "mp800mkTrapValue"),
        ("ELTEX-SMI", "mp800mkTrapComment"))
)
if mibBuilder.loadTexts:
    mp800mkIbatChOkTrap.setStatus(
        "current"
    )

mp800mkSuppOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 34300, 3, 9, 15)
)
mp800mkSuppOkTrap.setObjects(
      *(("ELTEX-SMI", "mp800mkTrapParameter"),
        ("ELTEX-SMI", "mp800mkTrapValue"),
        ("ELTEX-SMI", "mp800mkTrapComment"))
)
if mibBuilder.loadTexts:
    mp800mkSuppOkTrap.setStatus(
        "current"
    )

mp800mkBatConnOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 34300, 3, 9, 16)
)
mp800mkBatConnOkTrap.setObjects(
      *(("ELTEX-SMI", "mp800mkTrapParameter"),
        ("ELTEX-SMI", "mp800mkTrapValue"),
        ("ELTEX-SMI", "mp800mkTrapComment"))
)
if mibBuilder.loadTexts:
    mp800mkBatConnOkTrap.setStatus(
        "current"
    )

omsOperationCommandAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 34300, 3, 20, 1)
)
omsOperationCommandAlarm.setObjects(
      *(("ELTEX-SMI", "mcTrapExState"),
        ("ELTEX-SMI", "mcTrapLParam1"),
        ("ELTEX-SMI", "mcTrapLParam2"),
        ("ELTEX-SMI", "mcTrapLParam3"),
        ("ELTEX-SMI", "mcTrapID"),
        ("ELTEX-SMI", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    omsOperationCommandAlarm.setStatus(
        "current"
    )

omsOperationCommandOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 34300, 3, 21, 1)
)
omsOperationCommandOk.setObjects(
      *(("ELTEX-SMI", "mcTrapExState"),
        ("ELTEX-SMI", "mcTrapLParam1"),
        ("ELTEX-SMI", "mcTrapLParam2"),
        ("ELTEX-SMI", "mcTrapLParam3"),
        ("ELTEX-SMI", "mcTrapID"),
        ("ELTEX-SMI", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    omsOperationCommandOk.setStatus(
        "current"
    )


# Notifications groups

eltrapNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 34300, 3, 100)
)
eltrapNotificationGroup.setObjects(
      *(("ELTEX-SMI", "mc240StreamAlarmTrap"),
        ("ELTEX-SMI", "mc240SyncAlarmTrap"),
        ("ELTEX-SMI", "mc240ss7LinkAlarmTrap"),
        ("ELTEX-SMI", "mc240ss7LinksetAlarmTrap"),
        ("ELTEX-SMI", "mc240FileAlarmTrap"),
        ("ELTEX-SMI", "mc240CardAlarmTrap"),
        ("ELTEX-SMI", "mxlDPSAlarmTrap"),
        ("ELTEX-SMI", "mxlTELEAlarmTrap"),
        ("ELTEX-SMI", "mc240UPSAlarmTrap"),
        ("ELTEX-SMI", "mc240SensAlarmTrap"),
        ("ELTEX-SMI", "dslamLinkDownTrap"),
        ("ELTEX-SMI", "dslamDSRateAlarmTrap"),
        ("ELTEX-SMI", "dslamUSRateAlarmTrap"),
        ("ELTEX-SMI", "ponONUAuthAlarmTrap"),
        ("ELTEX-SMI", "ponEthAlarmTrap"),
        ("ELTEX-SMI", "ponOpticalAlarmTrap"),
        ("ELTEX-SMI", "mc240StreamOkTrap"),
        ("ELTEX-SMI", "mc240SyncOkTrap"),
        ("ELTEX-SMI", "mc240ss7LinkOkTrap"),
        ("ELTEX-SMI", "mc240ss7LinksetOkTrap"),
        ("ELTEX-SMI", "mc240FileOkTrap"),
        ("ELTEX-SMI", "mc240CardOkTrap"),
        ("ELTEX-SMI", "mxlDPSOkTrap"),
        ("ELTEX-SMI", "mxlTELEOkTrap"),
        ("ELTEX-SMI", "mc240UPSOkTrap"),
        ("ELTEX-SMI", "mc240SensOkTrap"),
        ("ELTEX-SMI", "dslamLinkUpTrap"),
        ("ELTEX-SMI", "dslamDSRateOkTrap"),
        ("ELTEX-SMI", "dslamUSRateOkTrap"),
        ("ELTEX-SMI", "ponONUAuthOkTrap"),
        ("ELTEX-SMI", "ponEthOkTrap"),
        ("ELTEX-SMI", "ponOpticalOkTrap"),
        ("ELTEX-SMI", "dslamOverheatAlarmTrap"),
        ("ELTEX-SMI", "dslamVoltageAlarmTrap"),
        ("ELTEX-SMI", "dslamSessionAlarmTrap"),
        ("ELTEX-SMI", "dslamEthLinkAlarmTrap"),
        ("ELTEX-SMI", "dslamOverheatOkTrap"),
        ("ELTEX-SMI", "dslamVoltageOkTrap"),
        ("ELTEX-SMI", "dslamSessionOkTrap"),
        ("ELTEX-SMI", "dslamEthLinkOkTrap"),
        ("ELTEX-SMI", "mp800mkMPStatusAlarmTrap"),
        ("ELTEX-SMI", "mp800mkInpParmAlarmTrap"),
        ("ELTEX-SMI", "mp800mkUEPConfAlarmTrap"),
        ("ELTEX-SMI", "mp800mkTMAlarmTrap"),
        ("ELTEX-SMI", "mp800mkACVMAlarmTrap"),
        ("ELTEX-SMI", "mp800mkIbatMAlarmTrap"),
        ("ELTEX-SMI", "mp800mkVbatMAlarmTrap"),
        ("ELTEX-SMI", "mp800mkVbatChAlarmTrap"),
        ("ELTEX-SMI", "mp800mkRlsDevAlarmTrap"),
        ("ELTEX-SMI", "mp800mkDVcellAlarmTrap"),
        ("ELTEX-SMI", "mp800mkACVAlarmTrap"),
        ("ELTEX-SMI", "mp800mkBatChargeAlarmTrap"),
        ("ELTEX-SMI", "mp800mkIloadAlarmTrap"),
        ("ELTEX-SMI", "mp800mkIbatChAlarmTrap"),
        ("ELTEX-SMI", "mp800mkSuppAlarmTrap"),
        ("ELTEX-SMI", "mp800mkBatConnAlarmTrap"),
        ("ELTEX-SMI", "mp800mkMPStatusOkTrap"),
        ("ELTEX-SMI", "mp800mkInpParmOkTrap"),
        ("ELTEX-SMI", "mp800mkUEPConfOkTrap"),
        ("ELTEX-SMI", "mp800mkTMOkTrap"),
        ("ELTEX-SMI", "mp800mkACVMOkTrap"),
        ("ELTEX-SMI", "mp800mkIbatMOkTrap"),
        ("ELTEX-SMI", "mp800mkVbatMOkTrap"),
        ("ELTEX-SMI", "mp800mkVbatChOkTrap"),
        ("ELTEX-SMI", "mp800mkRlsDevOkTrap"),
        ("ELTEX-SMI", "mp800mkDVcellOkTrap"),
        ("ELTEX-SMI", "mp800mkACVOkTrap"),
        ("ELTEX-SMI", "mp800mkBatChargeOkTrap"),
        ("ELTEX-SMI", "mp800mkIloadOkTrap"),
        ("ELTEX-SMI", "mp800mkIbatChOkTrap"),
        ("ELTEX-SMI", "mp800mkSuppOkTrap"),
        ("ELTEX-SMI", "mp800mkBatConnOkTrap"),
        ("ELTEX-SMI", "omsOperationCommandAlarm"),
        ("ELTEX-SMI", "omsOperationCommandOk"))
)
if mibBuilder.loadTexts:
    eltrapNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-SMI",
    **{"eltex": eltex,
       "elHardware": elHardware,
       "elSoftware": elSoftware,
       "eltrapGroup": eltrapGroup,
       "mc240AlarmTraps": mc240AlarmTraps,
       "mc240StreamAlarmTrap": mc240StreamAlarmTrap,
       "mc240SyncAlarmTrap": mc240SyncAlarmTrap,
       "mc240ss7LinkAlarmTrap": mc240ss7LinkAlarmTrap,
       "mc240ss7LinksetAlarmTrap": mc240ss7LinksetAlarmTrap,
       "mc240FileAlarmTrap": mc240FileAlarmTrap,
       "mc240CardAlarmTrap": mc240CardAlarmTrap,
       "mxlDPSAlarmTrap": mxlDPSAlarmTrap,
       "mxlTELEAlarmTrap": mxlTELEAlarmTrap,
       "mc240UPSAlarmTrap": mc240UPSAlarmTrap,
       "mc240SensAlarmTrap": mc240SensAlarmTrap,
       "dslamLinkDownTrap": dslamLinkDownTrap,
       "dslamDSRateAlarmTrap": dslamDSRateAlarmTrap,
       "dslamUSRateAlarmTrap": dslamUSRateAlarmTrap,
       "ponONUAuthAlarmTrap": ponONUAuthAlarmTrap,
       "ponEthAlarmTrap": ponEthAlarmTrap,
       "ponOpticalAlarmTrap": ponOpticalAlarmTrap,
       "dslamOverheatAlarmTrap": dslamOverheatAlarmTrap,
       "dslamVoltageAlarmTrap": dslamVoltageAlarmTrap,
       "dslamSessionAlarmTrap": dslamSessionAlarmTrap,
       "dslamEthLinkAlarmTrap": dslamEthLinkAlarmTrap,
       "mc240OkTraps": mc240OkTraps,
       "mc240StreamOkTrap": mc240StreamOkTrap,
       "mc240SyncOkTrap": mc240SyncOkTrap,
       "mc240ss7LinkOkTrap": mc240ss7LinkOkTrap,
       "mc240ss7LinksetOkTrap": mc240ss7LinksetOkTrap,
       "mc240FileOkTrap": mc240FileOkTrap,
       "mc240CardOkTrap": mc240CardOkTrap,
       "mxlDPSOkTrap": mxlDPSOkTrap,
       "mxlTELEOkTrap": mxlTELEOkTrap,
       "mc240UPSOkTrap": mc240UPSOkTrap,
       "mc240SensOkTrap": mc240SensOkTrap,
       "dslamLinkUpTrap": dslamLinkUpTrap,
       "dslamDSRateOkTrap": dslamDSRateOkTrap,
       "dslamUSRateOkTrap": dslamUSRateOkTrap,
       "ponONUAuthOkTrap": ponONUAuthOkTrap,
       "ponEthOkTrap": ponEthOkTrap,
       "ponOpticalOkTrap": ponOpticalOkTrap,
       "dslamOverheatOkTrap": dslamOverheatOkTrap,
       "dslamVoltageOkTrap": dslamVoltageOkTrap,
       "dslamSessionOkTrap": dslamSessionOkTrap,
       "dslamEthLinkOkTrap": dslamEthLinkOkTrap,
       "mc240TrapTypes": mc240TrapTypes,
       "mcTrapExState": mcTrapExState,
       "mcTrapLParam1": mcTrapLParam1,
       "mcTrapLParam2": mcTrapLParam2,
       "mcTrapLParam3": mcTrapLParam3,
       "mcTrapID": mcTrapID,
       "mcTrapDescr": mcTrapDescr,
       "mcTrapRestoredAlarmID": mcTrapRestoredAlarmID,
       "mcTrapSyncType": mcTrapSyncType,
       "mcReservedFlag": mcReservedFlag,
       "mp800mkAlarmTraps": mp800mkAlarmTraps,
       "mp800mkMPStatusAlarmTrap": mp800mkMPStatusAlarmTrap,
       "mp800mkInpParmAlarmTrap": mp800mkInpParmAlarmTrap,
       "mp800mkUEPConfAlarmTrap": mp800mkUEPConfAlarmTrap,
       "mp800mkTMAlarmTrap": mp800mkTMAlarmTrap,
       "mp800mkACVMAlarmTrap": mp800mkACVMAlarmTrap,
       "mp800mkIbatMAlarmTrap": mp800mkIbatMAlarmTrap,
       "mp800mkVbatMAlarmTrap": mp800mkVbatMAlarmTrap,
       "mp800mkVbatChAlarmTrap": mp800mkVbatChAlarmTrap,
       "mp800mkRlsDevAlarmTrap": mp800mkRlsDevAlarmTrap,
       "mp800mkDVcellAlarmTrap": mp800mkDVcellAlarmTrap,
       "mp800mkACVAlarmTrap": mp800mkACVAlarmTrap,
       "mp800mkBatChargeAlarmTrap": mp800mkBatChargeAlarmTrap,
       "mp800mkIloadAlarmTrap": mp800mkIloadAlarmTrap,
       "mp800mkIbatChAlarmTrap": mp800mkIbatChAlarmTrap,
       "mp800mkSuppAlarmTrap": mp800mkSuppAlarmTrap,
       "mp800mkBatConnAlarmTrap": mp800mkBatConnAlarmTrap,
       "mp800mkOkTraps": mp800mkOkTraps,
       "mp800mkMPStatusOkTrap": mp800mkMPStatusOkTrap,
       "mp800mkInpParmOkTrap": mp800mkInpParmOkTrap,
       "mp800mkUEPConfOkTrap": mp800mkUEPConfOkTrap,
       "mp800mkTMOkTrap": mp800mkTMOkTrap,
       "mp800mkACVMOkTrap": mp800mkACVMOkTrap,
       "mp800mkIbatMOkTrap": mp800mkIbatMOkTrap,
       "mp800mkVbatMOkTrap": mp800mkVbatMOkTrap,
       "mp800mkVbatChOkTrap": mp800mkVbatChOkTrap,
       "mp800mkRlsDevOkTrap": mp800mkRlsDevOkTrap,
       "mp800mkDVcellOkTrap": mp800mkDVcellOkTrap,
       "mp800mkACVOkTrap": mp800mkACVOkTrap,
       "mp800mkBatChargeOkTrap": mp800mkBatChargeOkTrap,
       "mp800mkIloadOkTrap": mp800mkIloadOkTrap,
       "mp800mkIbatChOkTrap": mp800mkIbatChOkTrap,
       "mp800mkSuppOkTrap": mp800mkSuppOkTrap,
       "mp800mkBatConnOkTrap": mp800mkBatConnOkTrap,
       "mp800mkTrapTypes": mp800mkTrapTypes,
       "mp800mkTrapParameter": mp800mkTrapParameter,
       "mp800mkTrapValue": mp800mkTrapValue,
       "mp800mkTrapComment": mp800mkTrapComment,
       "omsOperationAlarmTraps": omsOperationAlarmTraps,
       "omsOperationCommandAlarm": omsOperationCommandAlarm,
       "omsOperationOkTraps": omsOperationOkTraps,
       "omsOperationCommandOk": omsOperationCommandOk,
       "eltrapNotificationGroup": eltrapNotificationGroup,
       "eltrapObjectGroup": eltrapObjectGroup}
)
