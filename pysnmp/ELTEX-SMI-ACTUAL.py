# SNMP MIB module (ELTEX-SMI-ACTUAL) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ELTEX-SMI-ACTUAL
# Produced by pysmi-1.5.4 at Mon Oct 14 21:36:57 2024
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

eltexLtd = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265)
)
eltexLtd.setRevisions(
        ("2012-05-29 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ElHardware_ObjectIdentity = ObjectIdentity
elHardware = _ElHardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1)
)
if mibBuilder.loadTexts:
    elHardware.setStatus("current")
_ElSoftware_ObjectIdentity = ObjectIdentity
elSoftware = _ElSoftware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 2)
)
if mibBuilder.loadTexts:
    elSoftware.setStatus("current")
_EltrapGroup_ObjectIdentity = ObjectIdentity
eltrapGroup = _EltrapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 3)
)
if mibBuilder.loadTexts:
    eltrapGroup.setStatus("current")
_Mc240TrapTypes_ObjectIdentity = ObjectIdentity
mc240TrapTypes = _Mc240TrapTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 3, 5)
)
_McTrapExState_Type = Integer32
_McTrapExState_Object = MibScalar
mcTrapExState = _McTrapExState_Object(
    (1, 3, 6, 1, 4, 1, 35265, 3, 5, 1),
    _McTrapExState_Type()
)
mcTrapExState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcTrapExState.setStatus("current")
_McTrapLParam1_Type = Integer32
_McTrapLParam1_Object = MibScalar
mcTrapLParam1 = _McTrapLParam1_Object(
    (1, 3, 6, 1, 4, 1, 35265, 3, 5, 2),
    _McTrapLParam1_Type()
)
mcTrapLParam1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcTrapLParam1.setStatus("current")
_McTrapLParam2_Type = Integer32
_McTrapLParam2_Object = MibScalar
mcTrapLParam2 = _McTrapLParam2_Object(
    (1, 3, 6, 1, 4, 1, 35265, 3, 5, 3),
    _McTrapLParam2_Type()
)
mcTrapLParam2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcTrapLParam2.setStatus("current")
_McTrapLParam3_Type = Integer32
_McTrapLParam3_Object = MibScalar
mcTrapLParam3 = _McTrapLParam3_Object(
    (1, 3, 6, 1, 4, 1, 35265, 3, 5, 4),
    _McTrapLParam3_Type()
)
mcTrapLParam3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcTrapLParam3.setStatus("current")
_McTrapID_Type = Integer32
_McTrapID_Object = MibScalar
mcTrapID = _McTrapID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 3, 5, 5),
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
    (1, 3, 6, 1, 4, 1, 35265, 3, 5, 6),
    _McTrapDescr_Type()
)
mcTrapDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcTrapDescr.setStatus("current")
_McTrapRestoredAlarmID_Type = Integer32
_McTrapRestoredAlarmID_Object = MibScalar
mcTrapRestoredAlarmID = _McTrapRestoredAlarmID_Object(
    (1, 3, 6, 1, 4, 1, 35265, 3, 5, 7),
    _McTrapRestoredAlarmID_Type()
)
mcTrapRestoredAlarmID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcTrapRestoredAlarmID.setStatus("current")
_McTrapSyncType_Type = Integer32
_McTrapSyncType_Object = MibScalar
mcTrapSyncType = _McTrapSyncType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 3, 5, 8),
    _McTrapSyncType_Type()
)
mcTrapSyncType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcTrapSyncType.setStatus("current")
_McReservedFlag_Type = Integer32
_McReservedFlag_Object = MibScalar
mcReservedFlag = _McReservedFlag_Object(
    (1, 3, 6, 1, 4, 1, 35265, 3, 5, 9),
    _McReservedFlag_Type()
)
mcReservedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcReservedFlag.setStatus("current")
_RadiusSeqNum_Type = Integer32
_RadiusSeqNum_Object = MibScalar
radiusSeqNum = _RadiusSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 35265, 3, 5, 10),
    _RadiusSeqNum_Type()
)
radiusSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusSeqNum.setStatus("current")
_RadiusStatus_Type = Integer32
_RadiusStatus_Object = MibScalar
radiusStatus = _RadiusStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 3, 5, 11),
    _RadiusStatus_Type()
)
radiusStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusStatus.setStatus("current")
_RadiusTimeout_Type = Integer32
_RadiusTimeout_Object = MibScalar
radiusTimeout = _RadiusTimeout_Object(
    (1, 3, 6, 1, 4, 1, 35265, 3, 5, 12),
    _RadiusTimeout_Type()
)
radiusTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusTimeout.setStatus("current")
_RadiusSwitchSrv_Type = Integer32
_RadiusSwitchSrv_Object = MibScalar
radiusSwitchSrv = _RadiusSwitchSrv_Object(
    (1, 3, 6, 1, 4, 1, 35265, 3, 5, 13),
    _RadiusSwitchSrv_Type()
)
radiusSwitchSrv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusSwitchSrv.setStatus("current")
_RadiusTypeResp_Type = Integer32
_RadiusTypeResp_Object = MibScalar
radiusTypeResp = _RadiusTypeResp_Object(
    (1, 3, 6, 1, 4, 1, 35265, 3, 5, 14),
    _RadiusTypeResp_Type()
)
radiusTypeResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusTypeResp.setStatus("current")


class _RadiusDescr_Type(DisplayString):
    """Custom type radiusDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RadiusDescr_Type.__name__ = "DisplayString"
_RadiusDescr_Object = MibScalar
radiusDescr = _RadiusDescr_Object(
    (1, 3, 6, 1, 4, 1, 35265, 3, 5, 15),
    _RadiusDescr_Type()
)
radiusDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusDescr.setStatus("current")
_Fxs72AlarmTraps_ObjectIdentity = ObjectIdentity
fxs72AlarmTraps = _Fxs72AlarmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 3, 6)
)
_Fxs72OkTraps_ObjectIdentity = ObjectIdentity
fxs72OkTraps = _Fxs72OkTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 3, 7)
)
_PonTeknovusAlarmTraps_ObjectIdentity = ObjectIdentity
ponTeknovusAlarmTraps = _PonTeknovusAlarmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 3, 10)
)
_PonTeknovusOkTraps_ObjectIdentity = ObjectIdentity
ponTeknovusOkTraps = _PonTeknovusOkTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 3, 11)
)
_Pp4AlarmTraps_ObjectIdentity = ObjectIdentity
pp4AlarmTraps = _Pp4AlarmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 3, 12)
)
_Pp4OkTraps_ObjectIdentity = ObjectIdentity
pp4OkTraps = _Pp4OkTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 3, 13)
)
_Mxa32AlarmTraps_ObjectIdentity = ObjectIdentity
mxa32AlarmTraps = _Mxa32AlarmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 3, 14)
)
_Mxa32OkTraps_ObjectIdentity = ObjectIdentity
mxa32OkTraps = _Mxa32OkTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 3, 15)
)
_Mxa64AlarmTraps_ObjectIdentity = ObjectIdentity
mxa64AlarmTraps = _Mxa64AlarmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 3, 16)
)
_Mxa64OkTraps_ObjectIdentity = ObjectIdentity
mxa64OkTraps = _Mxa64OkTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 3, 17)
)
_Mxa24AlarmTraps_ObjectIdentity = ObjectIdentity
mxa24AlarmTraps = _Mxa24AlarmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 3, 18)
)
_Mxa24OkTraps_ObjectIdentity = ObjectIdentity
mxa24OkTraps = _Mxa24OkTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 3, 19)
)
_OmsOperationAlarmTraps_ObjectIdentity = ObjectIdentity
omsOperationAlarmTraps = _OmsOperationAlarmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 3, 20)
)
_OmsOperationOkTraps_ObjectIdentity = ObjectIdentity
omsOperationOkTraps = _OmsOperationOkTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 3, 21)
)
_ElcAlarmTraps_ObjectIdentity = ObjectIdentity
elcAlarmTraps = _ElcAlarmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 3, 22)
)
_ElcOkTraps_ObjectIdentity = ObjectIdentity
elcOkTraps = _ElcOkTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 3, 23)
)
_SmgTraps_ObjectIdentity = ObjectIdentity
smgTraps = _SmgTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 3, 29)
)
_SmgAlarm_ObjectIdentity = ObjectIdentity
smgAlarm = _SmgAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 3, 29, 1)
)
_SmgOK_ObjectIdentity = ObjectIdentity
smgOK = _SmgOK_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 3, 29, 2)
)
_MccpAlarmTraps_ObjectIdentity = ObjectIdentity
mccpAlarmTraps = _MccpAlarmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 3, 30)
)
_MccpOkTraps_ObjectIdentity = ObjectIdentity
mccpOkTraps = _MccpOkTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 3, 31)
)
_RadiusTraps_ObjectIdentity = ObjectIdentity
radiusTraps = _RadiusTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 3, 32)
)
_RadiusNotification_ObjectIdentity = ObjectIdentity
radiusNotification = _RadiusNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 3, 32, 1)
)

# Managed Objects groups

eltrapObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 35265, 3, 101)
)
eltrapObjectGroup.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"),
        ("ELTEX-SMI-ACTUAL", "mcTrapRestoredAlarmID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapSyncType"),
        ("ELTEX-SMI-ACTUAL", "mcReservedFlag"),
        ("ELTEX-SMI-ACTUAL", "radiusSeqNum"),
        ("ELTEX-SMI-ACTUAL", "radiusStatus"),
        ("ELTEX-SMI-ACTUAL", "radiusTimeout"),
        ("ELTEX-SMI-ACTUAL", "radiusSwitchSrv"),
        ("ELTEX-SMI-ACTUAL", "radiusTypeResp"),
        ("ELTEX-SMI-ACTUAL", "radiusDescr"))
)
if mibBuilder.loadTexts:
    eltrapObjectGroup.setStatus("current")


# Notification objects

fxs72VbatAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 6, 1)
)
fxs72VbatAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    fxs72VbatAlarmTrap.setStatus(
        "current"
    )

fxs72VringAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 6, 2)
)
fxs72VringAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    fxs72VringAlarmTrap.setStatus(
        "current"
    )

fxs72TemperatureAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 6, 3)
)
fxs72TemperatureAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    fxs72TemperatureAlarmTrap.setStatus(
        "current"
    )

fxs72FanAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 6, 4)
)
fxs72FanAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    fxs72FanAlarmTrap.setStatus(
        "current"
    )

fxs72SSwAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 6, 5)
)
fxs72SSwAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    fxs72SSwAlarmTrap.setStatus(
        "current"
    )

fxs72PortAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 6, 6)
)
fxs72PortAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    fxs72PortAlarmTrap.setStatus(
        "current"
    )

fxs72BpuAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 6, 12)
)
fxs72BpuAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    fxs72BpuAlarmTrap.setStatus(
        "current"
    )

fxs72TempmeasurementAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 6, 13)
)
fxs72TempmeasurementAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    fxs72TempmeasurementAlarmTrap.setStatus(
        "current"
    )

fxs72LicenseAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 6, 14)
)
fxs72LicenseAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    fxs72LicenseAlarmTrap.setStatus(
        "current"
    )

fxs72updateFwFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 6, 20)
)
fxs72updateFwFail.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    fxs72updateFwFail.setStatus(
        "current"
    )

fxs72PowerUnitTermAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 6, 21)
)
fxs72PowerUnitTermAlarm.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    fxs72PowerUnitTermAlarm.setStatus(
        "current"
    )

fxs72FanLowSpeedAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 6, 22)
)
fxs72FanLowSpeedAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    fxs72FanLowSpeedAlarmTrap.setStatus(
        "current"
    )

fxs72VbatOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 7, 1)
)
fxs72VbatOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    fxs72VbatOkTrap.setStatus(
        "current"
    )

fxs72VringOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 7, 2)
)
fxs72VringOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    fxs72VringOkTrap.setStatus(
        "current"
    )

fxs72TemperatureOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 7, 3)
)
fxs72TemperatureOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    fxs72TemperatureOkTrap.setStatus(
        "current"
    )

fxs72FanOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 7, 4)
)
fxs72FanOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    fxs72FanOkTrap.setStatus(
        "current"
    )

fxs72SSwOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 7, 5)
)
fxs72SSwOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    fxs72SSwOkTrap.setStatus(
        "current"
    )

fxs72PortOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 7, 6)
)
fxs72PortOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    fxs72PortOkTrap.setStatus(
        "current"
    )

fxs72VmodeSwitchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 7, 10)
)
fxs72VmodeSwitchTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    fxs72VmodeSwitchTrap.setStatus(
        "current"
    )

fxs72FansSwitchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 7, 11)
)
fxs72FansSwitchTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    fxs72FansSwitchTrap.setStatus(
        "current"
    )

fxs72BpuOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 7, 12)
)
fxs72BpuOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    fxs72BpuOkTrap.setStatus(
        "current"
    )

fxs72TempmeasurementOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 7, 13)
)
fxs72TempmeasurementOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    fxs72TempmeasurementOkTrap.setStatus(
        "current"
    )

fxs72LicenseOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 7, 14)
)
fxs72LicenseOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    fxs72LicenseOkTrap.setStatus(
        "current"
    )

fxs72updateFwOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 7, 20)
)
fxs72updateFwOk.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    fxs72updateFwOk.setStatus(
        "current"
    )

fxs72PowerUnitTermOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 7, 21)
)
fxs72PowerUnitTermOk.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    fxs72PowerUnitTermOk.setStatus(
        "current"
    )

fxs72FanLowSpeedOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 7, 22)
)
fxs72FanLowSpeedOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    fxs72FanLowSpeedOkTrap.setStatus(
        "current"
    )

ponTeknovusONTAuthAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 10, 1)
)
ponTeknovusONTAuthAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ponTeknovusONTAuthAlarmTrap.setStatus(
        "current"
    )

ponTeknovusUplinkAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 10, 2)
)
ponTeknovusUplinkAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ponTeknovusUplinkAlarmTrap.setStatus(
        "current"
    )

ponTeknovusOpticalAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 10, 3)
)
ponTeknovusOpticalAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ponTeknovusOpticalAlarmTrap.setStatus(
        "current"
    )

ponTeknovusFanAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 10, 4)
)
ponTeknovusFanAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ponTeknovusFanAlarmTrap.setStatus(
        "current"
    )

ponTeknovusONTConfAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 10, 5)
)
ponTeknovusONTConfAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ponTeknovusONTConfAlarmTrap.setStatus(
        "current"
    )

ponTeknovusFlappingAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 10, 6)
)
ponTeknovusFlappingAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ponTeknovusFlappingAlarmTrap.setStatus(
        "current"
    )

ponTeknovusEponAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 10, 7)
)
ponTeknovusEponAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ponTeknovusEponAlarmTrap.setStatus(
        "deprecated"
    )

ponTeknovusConfigSavedAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 10, 8)
)
ponTeknovusConfigSavedAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ponTeknovusConfigSavedAlarmTrap.setStatus(
        "current"
    )

ponTeknovusFirmwareUpdateAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 10, 9)
)
ponTeknovusFirmwareUpdateAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ponTeknovusFirmwareUpdateAlarmTrap.setStatus(
        "current"
    )

ponTeknovusUserLoginAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 10, 10)
)
ponTeknovusUserLoginAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ponTeknovusUserLoginAlarmTrap.setStatus(
        "deprecated"
    )

ponTeknovusRAMAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 10, 11)
)
ponTeknovusRAMAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ponTeknovusRAMAlarmTrap.setStatus(
        "current"
    )

ponTeknovusLoginAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 10, 12)
)
ponTeknovusLoginAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ponTeknovusLoginAlarmTrap.setStatus(
        "current"
    )

ponTeknovusDuplicateMacAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 10, 14)
)
ponTeknovusDuplicateMacAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ponTeknovusDuplicateMacAlarmTrap.setStatus(
        "current"
    )

ponTeknovusLoadAverageAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 10, 15)
)
ponTeknovusLoadAverageAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ponTeknovusLoadAverageAlarmTrap.setStatus(
        "current"
    )

ponTeknovusTemperatureAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 10, 16)
)
ponTeknovusTemperatureAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ponTeknovusTemperatureAlarmTrap.setStatus(
        "current"
    )

ponTeknovusONTPortBlockedAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 10, 17)
)
ponTeknovusONTPortBlockedAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ponTeknovusONTPortBlockedAlarmTrap.setStatus(
        "current"
    )

ponTeknovusConfigMigrateAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 10, 18)
)
ponTeknovusConfigMigrateAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ponTeknovusConfigMigrateAlarmTrap.setStatus(
        "current"
    )

ponTeknovusONTAuthOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 11, 1)
)
ponTeknovusONTAuthOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ponTeknovusONTAuthOkTrap.setStatus(
        "current"
    )

ponTeknovusUplinkOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 11, 2)
)
ponTeknovusUplinkOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ponTeknovusUplinkOkTrap.setStatus(
        "current"
    )

ponTeknovusOpticalOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 11, 3)
)
ponTeknovusOpticalOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ponTeknovusOpticalOkTrap.setStatus(
        "current"
    )

ponTeknovusFanOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 11, 4)
)
ponTeknovusFanOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ponTeknovusFanOkTrap.setStatus(
        "current"
    )

ponTeknovusONTConfOKTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 11, 5)
)
ponTeknovusONTConfOKTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ponTeknovusONTConfOKTrap.setStatus(
        "current"
    )

ponTeknovusFlappingOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 11, 6)
)
ponTeknovusFlappingOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ponTeknovusFlappingOkTrap.setStatus(
        "current"
    )

ponTeknovusEponOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 11, 7)
)
ponTeknovusEponOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ponTeknovusEponOkTrap.setStatus(
        "deprecated"
    )

ponTeknovusConfigSavedOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 11, 8)
)
ponTeknovusConfigSavedOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ponTeknovusConfigSavedOkTrap.setStatus(
        "current"
    )

ponTeknovusFirmwareUpdateOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 11, 9)
)
ponTeknovusFirmwareUpdateOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ponTeknovusFirmwareUpdateOkTrap.setStatus(
        "current"
    )

ponTeknovusUserLoginOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 11, 10)
)
ponTeknovusUserLoginOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ponTeknovusUserLoginOkTrap.setStatus(
        "deprecated"
    )

ponTeknovusRAMOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 11, 11)
)
ponTeknovusRAMOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ponTeknovusRAMOkTrap.setStatus(
        "current"
    )

ponTeknovusLoginOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 11, 12)
)
ponTeknovusLoginOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ponTeknovusLoginOkTrap.setStatus(
        "current"
    )

ponTeknovusLogoutOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 11, 13)
)
ponTeknovusLogoutOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ponTeknovusLogoutOkTrap.setStatus(
        "current"
    )

ponTeknovusSwitchConfigChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 11, 14)
)
ponTeknovusSwitchConfigChangeTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ponTeknovusSwitchConfigChangeTrap.setStatus(
        "current"
    )

ponTeknovusLoadAverageOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 11, 15)
)
ponTeknovusLoadAverageOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ponTeknovusLoadAverageOkTrap.setStatus(
        "current"
    )

ponTeknovusTemperatureOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 11, 16)
)
ponTeknovusTemperatureOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ponTeknovusTemperatureOkTrap.setStatus(
        "current"
    )

ponTeknovusONTPortBlockedOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 11, 17)
)
ponTeknovusONTPortBlockedOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ponTeknovusONTPortBlockedOkTrap.setStatus(
        "current"
    )

ponTeknovusConfigMigrateOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 11, 18)
)
ponTeknovusConfigMigrateOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ponTeknovusConfigMigrateOkTrap.setStatus(
        "current"
    )

ponTeknovusBoardRebootTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 11, 20)
)
ponTeknovusBoardRebootTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ponTeknovusBoardRebootTrap.setStatus(
        "current"
    )

ponTeknovusONTDeconfigureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 11, 21)
)
ponTeknovusONTDeconfigureTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ponTeknovusONTDeconfigureTrap.setStatus(
        "current"
    )

ponTeknovusONTStateChangedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 11, 22)
)
ponTeknovusONTStateChangedTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ponTeknovusONTStateChangedTrap.setStatus(
        "current"
    )

ponTeknovusONTConfigChangedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 11, 23)
)
ponTeknovusONTConfigChangedTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ponTeknovusONTConfigChangedTrap.setStatus(
        "current"
    )

ponTeknovusConfigRereadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 11, 24)
)
ponTeknovusConfigRereadTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    ponTeknovusConfigRereadTrap.setStatus(
        "current"
    )

pp4LinkAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 12, 1)
)
pp4LinkAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    pp4LinkAlarmTrap.setStatus(
        "current"
    )

pp4AutoNegotiationAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 12, 2)
)
pp4AutoNegotiationAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    pp4AutoNegotiationAlarmTrap.setStatus(
        "current"
    )

pp4MemoryAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 12, 3)
)
pp4MemoryAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    pp4MemoryAlarmTrap.setStatus(
        "current"
    )

pp4LoadAvgAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 12, 4)
)
pp4LoadAvgAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    pp4LoadAvgAlarmTrap.setStatus(
        "current"
    )

pp4LoginAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 12, 5)
)
pp4LoginAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    pp4LoginAlarmTrap.setStatus(
        "current"
    )

pp4LogoutAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 12, 6)
)
pp4LogoutAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    pp4LogoutAlarmTrap.setStatus(
        "current"
    )

pp4SaveAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 12, 8)
)
pp4SaveAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    pp4SaveAlarmTrap.setStatus(
        "current"
    )

pp4LoadCpuAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 12, 9)
)
pp4LoadCpuAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    pp4LoadCpuAlarmTrap.setStatus(
        "current"
    )

pp4DuplicationMacAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 12, 10)
)
pp4DuplicationMacAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    pp4DuplicationMacAlarmTrap.setStatus(
        "current"
    )

pp4LinkFlapAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 12, 11)
)
pp4LinkFlapAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    pp4LinkFlapAlarmTrap.setStatus(
        "current"
    )

pp4BoardRemoveAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 12, 13)
)
pp4BoardRemoveAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    pp4BoardRemoveAlarmTrap.setStatus(
        "current"
    )

pp4UnitRemoveAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 12, 14)
)
pp4UnitRemoveAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    pp4UnitRemoveAlarmTrap.setStatus(
        "current"
    )

pp4PortCounterErrorFoundAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 12, 16)
)
pp4PortCounterErrorFoundAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    pp4PortCounterErrorFoundAlarmTrap.setStatus(
        "current"
    )

pp4SyncDisallowedAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 12, 17)
)
pp4SyncDisallowedAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    pp4SyncDisallowedAlarmTrap.setStatus(
        "current"
    )

pp4RebootUnitAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 12, 19)
)
pp4RebootUnitAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    pp4RebootUnitAlarmTrap.setStatus(
        "current"
    )

pp4RebootStackAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 12, 20)
)
pp4RebootStackAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    pp4RebootStackAlarmTrap.setStatus(
        "current"
    )

pp4RebootFwTimerAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 12, 21)
)
pp4RebootFwTimerAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    pp4RebootFwTimerAlarmTrap.setStatus(
        "current"
    )

pp4FwUpdateAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 12, 22)
)
pp4FwUpdateAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    pp4FwUpdateAlarmTrap.setStatus(
        "current"
    )

pp4FwConfirmNeededAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 12, 23)
)
pp4FwConfirmNeededAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    pp4FwConfirmNeededAlarmTrap.setStatus(
        "current"
    )

pp4LinkOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 13, 1)
)
pp4LinkOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    pp4LinkOkTrap.setStatus(
        "current"
    )

pp4AutoNegotiationOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 13, 2)
)
pp4AutoNegotiationOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    pp4AutoNegotiationOkTrap.setStatus(
        "current"
    )

pp4MemoryOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 13, 3)
)
pp4MemoryOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    pp4MemoryOkTrap.setStatus(
        "current"
    )

pp4LoadAvgOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 13, 4)
)
pp4LoadAvgOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    pp4LoadAvgOkTrap.setStatus(
        "current"
    )

pp4LoginOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 13, 5)
)
pp4LoginOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    pp4LoginOkTrap.setStatus(
        "current"
    )

pp4LogoutOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 13, 6)
)
pp4LogoutOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    pp4LogoutOkTrap.setStatus(
        "current"
    )

pp4CommitOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 13, 7)
)
pp4CommitOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    pp4CommitOkTrap.setStatus(
        "current"
    )

pp4SaveOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 13, 8)
)
pp4SaveOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    pp4SaveOkTrap.setStatus(
        "current"
    )

pp4LinkFlapEndOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 13, 11)
)
pp4LinkFlapEndOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    pp4LinkFlapEndOkTrap.setStatus(
        "current"
    )

pp4ConfigChangedOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 13, 12)
)
pp4ConfigChangedOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    pp4ConfigChangedOkTrap.setStatus(
        "current"
    )

pp4BoardAddOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 13, 13)
)
pp4BoardAddOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    pp4BoardAddOkTrap.setStatus(
        "current"
    )

pp4UnitAddOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 13, 14)
)
pp4UnitAddOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    pp4UnitAddOkTrap.setStatus(
        "current"
    )

pp4RoleChangedOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 13, 15)
)
pp4RoleChangedOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    pp4RoleChangedOkTrap.setStatus(
        "current"
    )

pp4PortCounterErrorFreeOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 13, 16)
)
pp4PortCounterErrorFreeOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    pp4PortCounterErrorFreeOkTrap.setStatus(
        "current"
    )

pp4SyncDisallowedOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 13, 17)
)
pp4SyncDisallowedOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    pp4SyncDisallowedOkTrap.setStatus(
        "current"
    )

pp4ConfigRestoredOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 13, 18)
)
pp4ConfigRestoredOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    pp4ConfigRestoredOkTrap.setStatus(
        "current"
    )

pp4RebootUnitOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 13, 19)
)
pp4RebootUnitOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    pp4RebootUnitOkTrap.setStatus(
        "current"
    )

pp4FwUpdateOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 13, 22)
)
pp4FwUpdateOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    pp4FwUpdateOkTrap.setStatus(
        "current"
    )

mxa32DslLinkAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 14, 1)
)
mxa32DslLinkAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapSyncType"))
)
if mibBuilder.loadTexts:
    mxa32DslLinkAlarmTrap.setStatus(
        "current"
    )

mxa32EthLinkAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 14, 2)
)
mxa32EthLinkAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapSyncType"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    mxa32EthLinkAlarmTrap.setStatus(
        "current"
    )

mxa32TempAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 14, 3)
)
mxa32TempAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"),
        ("ELTEX-SMI-ACTUAL", "mcTrapSyncType"))
)
if mibBuilder.loadTexts:
    mxa32TempAlarmTrap.setStatus(
        "current"
    )

mxa32VoltAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 14, 4)
)
mxa32VoltAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"),
        ("ELTEX-SMI-ACTUAL", "mcTrapSyncType"))
)
if mibBuilder.loadTexts:
    mxa32VoltAlarmTrap.setStatus(
        "current"
    )

mxa32UserLoginTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 14, 5)
)
mxa32UserLoginTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"),
        ("ELTEX-SMI-ACTUAL", "mcTrapSyncType"))
)
if mibBuilder.loadTexts:
    mxa32UserLoginTrap.setStatus(
        "current"
    )

mxa32DslLinkOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 15, 1)
)
mxa32DslLinkOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"),
        ("ELTEX-SMI-ACTUAL", "mcTrapSyncType"))
)
if mibBuilder.loadTexts:
    mxa32DslLinkOkTrap.setStatus(
        "current"
    )

mxa32EthLinkOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 15, 2)
)
mxa32EthLinkOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"),
        ("ELTEX-SMI-ACTUAL", "mcTrapSyncType"))
)
if mibBuilder.loadTexts:
    mxa32EthLinkOkTrap.setStatus(
        "current"
    )

mxa32TempOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 15, 3)
)
mxa32TempOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"),
        ("ELTEX-SMI-ACTUAL", "mcTrapSyncType"))
)
if mibBuilder.loadTexts:
    mxa32TempOkTrap.setStatus(
        "current"
    )

mxa32VoltOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 15, 4)
)
mxa32VoltOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"),
        ("ELTEX-SMI-ACTUAL", "mcTrapSyncType"))
)
if mibBuilder.loadTexts:
    mxa32VoltOkTrap.setStatus(
        "current"
    )

mxa32UserLogoutTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 15, 5)
)
mxa32UserLogoutTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"),
        ("ELTEX-SMI-ACTUAL", "mcTrapSyncType"))
)
if mibBuilder.loadTexts:
    mxa32UserLogoutTrap.setStatus(
        "current"
    )

mxa64DslLinkAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 16, 1)
)
mxa64DslLinkAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapSyncType"))
)
if mibBuilder.loadTexts:
    mxa64DslLinkAlarmTrap.setStatus(
        "current"
    )

mxa64EthLinkAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 16, 2)
)
mxa64EthLinkAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapSyncType"))
)
if mibBuilder.loadTexts:
    mxa64EthLinkAlarmTrap.setStatus(
        "current"
    )

mxa64TempAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 16, 3)
)
mxa64TempAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"),
        ("ELTEX-SMI-ACTUAL", "mcTrapSyncType"))
)
if mibBuilder.loadTexts:
    mxa64TempAlarmTrap.setStatus(
        "current"
    )

mxa64VoltAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 16, 4)
)
mxa64VoltAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"),
        ("ELTEX-SMI-ACTUAL", "mcTrapSyncType"))
)
if mibBuilder.loadTexts:
    mxa64VoltAlarmTrap.setStatus(
        "current"
    )

mxa64UserLoginTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 16, 5)
)
mxa64UserLoginTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"),
        ("ELTEX-SMI-ACTUAL", "mcTrapSyncType"))
)
if mibBuilder.loadTexts:
    mxa64UserLoginTrap.setStatus(
        "current"
    )

mxa64DslLinkOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 17, 1)
)
mxa64DslLinkOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"),
        ("ELTEX-SMI-ACTUAL", "mcTrapSyncType"))
)
if mibBuilder.loadTexts:
    mxa64DslLinkOkTrap.setStatus(
        "current"
    )

mxa64EthLinkOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 17, 2)
)
mxa64EthLinkOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"),
        ("ELTEX-SMI-ACTUAL", "mcTrapSyncType"))
)
if mibBuilder.loadTexts:
    mxa64EthLinkOkTrap.setStatus(
        "current"
    )

mxa64TempOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 17, 3)
)
mxa64TempOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"),
        ("ELTEX-SMI-ACTUAL", "mcTrapSyncType"))
)
if mibBuilder.loadTexts:
    mxa64TempOkTrap.setStatus(
        "current"
    )

mxa64VoltOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 17, 4)
)
mxa64VoltOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"),
        ("ELTEX-SMI-ACTUAL", "mcTrapSyncType"))
)
if mibBuilder.loadTexts:
    mxa64VoltOkTrap.setStatus(
        "current"
    )

mxa64UserLogoutTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 17, 5)
)
mxa64UserLogoutTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"),
        ("ELTEX-SMI-ACTUAL", "mcTrapSyncType"))
)
if mibBuilder.loadTexts:
    mxa64UserLogoutTrap.setStatus(
        "current"
    )

mxa24DslLinkAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 18, 1)
)
mxa24DslLinkAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapSyncType"))
)
if mibBuilder.loadTexts:
    mxa24DslLinkAlarmTrap.setStatus(
        "current"
    )

mxa24EthLinkAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 18, 2)
)
mxa24EthLinkAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapSyncType"))
)
if mibBuilder.loadTexts:
    mxa24EthLinkAlarmTrap.setStatus(
        "current"
    )

mxa24TempAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 18, 3)
)
mxa24TempAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"),
        ("ELTEX-SMI-ACTUAL", "mcTrapSyncType"))
)
if mibBuilder.loadTexts:
    mxa24TempAlarmTrap.setStatus(
        "current"
    )

mxa24VoltAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 18, 4)
)
mxa24VoltAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"),
        ("ELTEX-SMI-ACTUAL", "mcTrapSyncType"))
)
if mibBuilder.loadTexts:
    mxa24VoltAlarmTrap.setStatus(
        "current"
    )

mxa24UserLoginTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 18, 5)
)
mxa24UserLoginTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"),
        ("ELTEX-SMI-ACTUAL", "mcTrapSyncType"))
)
if mibBuilder.loadTexts:
    mxa24UserLoginTrap.setStatus(
        "current"
    )

mxa24DslLinkOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 19, 1)
)
mxa24DslLinkOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"),
        ("ELTEX-SMI-ACTUAL", "mcTrapSyncType"))
)
if mibBuilder.loadTexts:
    mxa24DslLinkOkTrap.setStatus(
        "current"
    )

mxa24EthLinkOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 19, 2)
)
mxa24EthLinkOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"),
        ("ELTEX-SMI-ACTUAL", "mcTrapSyncType"))
)
if mibBuilder.loadTexts:
    mxa24EthLinkOkTrap.setStatus(
        "current"
    )

mxa24TempOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 19, 3)
)
mxa24TempOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"),
        ("ELTEX-SMI-ACTUAL", "mcTrapSyncType"))
)
if mibBuilder.loadTexts:
    mxa24TempOkTrap.setStatus(
        "current"
    )

mxa24VoltOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 19, 4)
)
mxa24VoltOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"),
        ("ELTEX-SMI-ACTUAL", "mcTrapSyncType"))
)
if mibBuilder.loadTexts:
    mxa24VoltOkTrap.setStatus(
        "current"
    )

mxa24UserLogoutTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 19, 5)
)
mxa24UserLogoutTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"),
        ("ELTEX-SMI-ACTUAL", "mcTrapSyncType"))
)
if mibBuilder.loadTexts:
    mxa24UserLogoutTrap.setStatus(
        "current"
    )

omsOperationCommandAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 20, 1)
)
omsOperationCommandAlarm.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    omsOperationCommandAlarm.setStatus(
        "current"
    )

omsOperationCommandOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 21, 1)
)
omsOperationCommandOk.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    omsOperationCommandOk.setStatus(
        "current"
    )

elcONTAuthAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 22, 1)
)
elcONTAuthAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    elcONTAuthAlarmTrap.setStatus(
        "current"
    )

elcUplinkAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 22, 2)
)
elcUplinkAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    elcUplinkAlarmTrap.setStatus(
        "current"
    )

elcOpticalAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 22, 3)
)
elcOpticalAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    elcOpticalAlarmTrap.setStatus(
        "current"
    )

elcFanAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 22, 4)
)
elcFanAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    elcFanAlarmTrap.setStatus(
        "current"
    )

elcONTConfAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 22, 5)
)
elcONTConfAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    elcONTConfAlarmTrap.setStatus(
        "current"
    )

elcFlappingAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 22, 6)
)
elcFlappingAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    elcFlappingAlarmTrap.setStatus(
        "current"
    )

elcEponAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 22, 7)
)
elcEponAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    elcEponAlarmTrap.setStatus(
        "deprecated"
    )

elcConfigSavedAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 22, 8)
)
elcConfigSavedAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    elcConfigSavedAlarmTrap.setStatus(
        "current"
    )

elcFirmwareUpdateAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 22, 9)
)
elcFirmwareUpdateAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    elcFirmwareUpdateAlarmTrap.setStatus(
        "current"
    )

elcUserLoginAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 22, 10)
)
elcUserLoginAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    elcUserLoginAlarmTrap.setStatus(
        "deprecated"
    )

elcRAMAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 22, 11)
)
elcRAMAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    elcRAMAlarmTrap.setStatus(
        "current"
    )

elcLoginAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 22, 12)
)
elcLoginAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    elcLoginAlarmTrap.setStatus(
        "current"
    )

elcDuplicateMacAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 22, 14)
)
elcDuplicateMacAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    elcDuplicateMacAlarmTrap.setStatus(
        "current"
    )

elcLoadAverageAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 22, 15)
)
elcLoadAverageAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    elcLoadAverageAlarmTrap.setStatus(
        "current"
    )

elcTemperatureAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 22, 16)
)
elcTemperatureAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    elcTemperatureAlarmTrap.setStatus(
        "current"
    )

elcONTAuthOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 23, 1)
)
elcONTAuthOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    elcONTAuthOkTrap.setStatus(
        "current"
    )

elcUplinkOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 23, 2)
)
elcUplinkOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    elcUplinkOkTrap.setStatus(
        "current"
    )

elcOpticalOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 23, 3)
)
elcOpticalOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    elcOpticalOkTrap.setStatus(
        "current"
    )

elcFanOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 23, 4)
)
elcFanOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    elcFanOkTrap.setStatus(
        "current"
    )

elcONTConfOKTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 23, 5)
)
elcONTConfOKTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    elcONTConfOKTrap.setStatus(
        "current"
    )

elcFlappingOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 23, 6)
)
elcFlappingOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    elcFlappingOkTrap.setStatus(
        "current"
    )

elcEponOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 23, 7)
)
elcEponOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    elcEponOkTrap.setStatus(
        "deprecated"
    )

elcConfigSavedOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 23, 8)
)
elcConfigSavedOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    elcConfigSavedOkTrap.setStatus(
        "current"
    )

elcFirmwareUpdateOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 23, 9)
)
elcFirmwareUpdateOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    elcFirmwareUpdateOkTrap.setStatus(
        "current"
    )

elcUserLoginOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 23, 10)
)
elcUserLoginOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    elcUserLoginOkTrap.setStatus(
        "deprecated"
    )

elcRAMOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 23, 11)
)
elcRAMOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    elcRAMOkTrap.setStatus(
        "current"
    )

elcLoginOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 23, 12)
)
elcLoginOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    elcLoginOkTrap.setStatus(
        "current"
    )

elcLogoutOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 23, 13)
)
elcLogoutOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    elcLogoutOkTrap.setStatus(
        "current"
    )

elcSwitchConfigChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 23, 14)
)
elcSwitchConfigChangeTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    elcSwitchConfigChangeTrap.setStatus(
        "current"
    )

elcLoadAverageOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 23, 15)
)
elcLoadAverageOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    elcLoadAverageOkTrap.setStatus(
        "current"
    )

elcTemperatureOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 23, 16)
)
elcTemperatureOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    elcTemperatureOkTrap.setStatus(
        "current"
    )

smgAlarmConfigTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 29, 1, 1)
)
smgAlarmConfigTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    smgAlarmConfigTrap.setStatus(
        "current"
    )

smgAlarmSiptNodeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 29, 1, 2)
)
smgAlarmSiptNodeTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    smgAlarmSiptNodeTrap.setStatus(
        "current"
    )

smgAlarmMspDevTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 29, 1, 3)
)
smgAlarmMspDevTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    smgAlarmMspDevTrap.setStatus(
        "current"
    )

smgAlarmLinkSetTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 29, 1, 4)
)
smgAlarmLinkSetTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    smgAlarmLinkSetTrap.setStatus(
        "current"
    )

smgAlarmStreamTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 29, 1, 5)
)
smgAlarmStreamTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    smgAlarmStreamTrap.setStatus(
        "current"
    )

smgAlarmSS7LinkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 29, 1, 6)
)
smgAlarmSS7LinkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    smgAlarmSS7LinkTrap.setStatus(
        "current"
    )

smgAlarmSyncTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 29, 1, 7)
)
smgAlarmSyncTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    smgAlarmSyncTrap.setStatus(
        "current"
    )

smgAlarmCdrFtpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 29, 1, 12)
)
smgAlarmCdrFtpTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    smgAlarmCdrFtpTrap.setStatus(
        "current"
    )

smgAlarmMemoryLimitTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 29, 1, 13)
)
smgAlarmMemoryLimitTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    smgAlarmMemoryLimitTrap.setStatus(
        "current"
    )

smgAlarmPowerModuleStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 29, 1, 14)
)
smgAlarmPowerModuleStateTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    smgAlarmPowerModuleStateTrap.setStatus(
        "current"
    )

smgAlarmH323NodeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 29, 1, 16)
)
smgAlarmH323NodeTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    smgAlarmH323NodeTrap.setStatus(
        "current"
    )

smgAlarmTemperatureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 29, 1, 17)
)
smgAlarmTemperatureTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    smgAlarmTemperatureTrap.setStatus(
        "current"
    )

smgAlarmMaintenanceTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 29, 1, 18)
)
smgAlarmMaintenanceTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    smgAlarmMaintenanceTrap.setStatus(
        "current"
    )

smgAlarmSipAccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 29, 1, 19)
)
smgAlarmSipAccessTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    smgAlarmSipAccessTrap.setStatus(
        "current"
    )

smgUpdateFwFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 29, 1, 20)
)
smgUpdateFwFail.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    smgUpdateFwFail.setStatus(
        "current"
    )

smgAlarmProcOverloadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 29, 1, 21)
)
smgAlarmProcOverloadTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    smgAlarmProcOverloadTrap.setStatus(
        "current"
    )

smgAlarmFansIdleTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 29, 1, 23)
)
smgAlarmFansIdleTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    smgAlarmFansIdleTrap.setStatus(
        "current"
    )

smgAlarmDriveLimitTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 29, 1, 24)
)
smgAlarmDriveLimitTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    smgAlarmDriveLimitTrap.setStatus(
        "current"
    )

smgAlarmSipOptionsQueueOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 29, 1, 25)
)
smgAlarmSipOptionsQueueOverload.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    smgAlarmSipOptionsQueueOverload.setStatus(
        "current"
    )

smgAlarmCDRFileTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 29, 1, 26)
)
smgAlarmCDRFileTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    smgAlarmCDRFileTrap.setStatus(
        "current"
    )

smgAlarmMegacoNodeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 29, 1, 27)
)
smgAlarmMegacoNodeTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    smgAlarmMegacoNodeTrap.setStatus(
        "current"
    )

smgFail2banBlockTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 29, 1, 28)
)
smgFail2banBlockTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    smgFail2banBlockTrap.setStatus(
        "current"
    )

smgTrunkGroupCPSTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 29, 1, 29)
)
smgTrunkGroupCPSTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    smgTrunkGroupCPSTrap.setStatus(
        "current"
    )

smgDemoLicenseTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 29, 1, 30)
)
smgDemoLicenseTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    smgDemoLicenseTrap.setStatus(
        "current"
    )

smgAlarmSipDuplicateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 29, 1, 31)
)
smgAlarmSipDuplicateTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    smgAlarmSipDuplicateTrap.setStatus(
        "current"
    )

smgAlarmSbcRegistrationExpiredTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 29, 1, 50)
)
smgAlarmSbcRegistrationExpiredTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    smgAlarmSbcRegistrationExpiredTrap.setStatus(
        "current"
    )

smgAlarmIpcOverloadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 29, 1, 51)
)
smgAlarmIpcOverloadTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    smgAlarmIpcOverloadTrap.setStatus(
        "current"
    )

smgCallForbiddenTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 29, 1, 52)
)
smgCallForbiddenTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    smgCallForbiddenTrap.setStatus(
        "current"
    )

smgRegForbiddenTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 29, 1, 53)
)
smgRegForbiddenTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    smgRegForbiddenTrap.setStatus(
        "current"
    )

smgSIPinterfaceTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 29, 1, 54)
)
smgSIPinterfaceTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    smgSIPinterfaceTrap.setStatus(
        "current"
    )

smgReserveSlaveLinkChangedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 29, 1, 55)
)
smgReserveSlaveLinkChangedTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    smgReserveSlaveLinkChangedTrap.setStatus(
        "current"
    )

smgReserveSlaveSoftVersionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 29, 1, 56)
)
smgReserveSlaveSoftVersionTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    smgReserveSlaveSoftVersionTrap.setStatus(
        "current"
    )

smgSipAttackedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 29, 1, 57)
)
smgSipAttackedTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    smgSipAttackedTrap.setStatus(
        "current"
    )

smgPctlModuleTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 29, 1, 58)
)
smgPctlModuleTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    smgPctlModuleTrap.setStatus(
        "current"
    )

smgPortScanDetectorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 29, 1, 59)
)
smgPortScanDetectorTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    smgPortScanDetectorTrap.setStatus(
        "current"
    )

smgFirewallTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 29, 1, 60)
)
smgFirewallTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    smgFirewallTrap.setStatus(
        "current"
    )

smgOkConfigTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 29, 2, 1)
)
smgOkConfigTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    smgOkConfigTrap.setStatus(
        "current"
    )

smgOkSiptNodeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 29, 2, 2)
)
smgOkSiptNodeTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    smgOkSiptNodeTrap.setStatus(
        "current"
    )

smgOkMspDevTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 29, 2, 3)
)
smgOkMspDevTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    smgOkMspDevTrap.setStatus(
        "current"
    )

smgOkLinkSetTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 29, 2, 4)
)
smgOkLinkSetTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    smgOkLinkSetTrap.setStatus(
        "current"
    )

smgOkStreamTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 29, 2, 5)
)
smgOkStreamTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    smgOkStreamTrap.setStatus(
        "current"
    )

smgOkSS7LinkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 29, 2, 6)
)
smgOkSS7LinkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    smgOkSS7LinkTrap.setStatus(
        "current"
    )

smgOkSyncTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 29, 2, 7)
)
smgOkSyncTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    smgOkSyncTrap.setStatus(
        "current"
    )

smgOkCdrFtpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 29, 2, 12)
)
smgOkCdrFtpTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    smgOkCdrFtpTrap.setStatus(
        "current"
    )

smgOkMemoryLimitTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 29, 2, 13)
)
smgOkMemoryLimitTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    smgOkMemoryLimitTrap.setStatus(
        "current"
    )

smgOkPowerModuleStateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 29, 2, 14)
)
smgOkPowerModuleStateTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    smgOkPowerModuleStateTrap.setStatus(
        "current"
    )

smgOkH323NodeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 29, 2, 16)
)
smgOkH323NodeTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    smgOkH323NodeTrap.setStatus(
        "current"
    )

smgOkTemperatureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 29, 2, 17)
)
smgOkTemperatureTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    smgOkTemperatureTrap.setStatus(
        "current"
    )

smgOkMaintenanceTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 29, 2, 18)
)
smgOkMaintenanceTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    smgOkMaintenanceTrap.setStatus(
        "current"
    )

smgOkSipAccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 29, 2, 19)
)
smgOkSipAccessTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    smgOkSipAccessTrap.setStatus(
        "current"
    )

smgUpdateFwOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 29, 2, 20)
)
smgUpdateFwOk.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    smgUpdateFwOk.setStatus(
        "current"
    )

smgOkProcOverloadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 29, 2, 21)
)
smgOkProcOverloadTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    smgOkProcOverloadTrap.setStatus(
        "current"
    )

smgOkRebootTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 29, 2, 22)
)
smgOkRebootTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    smgOkRebootTrap.setStatus(
        "current"
    )

smgOkFansIdleTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 29, 2, 23)
)
smgOkFansIdleTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    smgOkFansIdleTrap.setStatus(
        "current"
    )

smgOkDriveLimitTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 29, 2, 24)
)
smgOkDriveLimitTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    smgOkDriveLimitTrap.setStatus(
        "current"
    )

smgAlarmSipOptionsQueueOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 29, 2, 25)
)
smgAlarmSipOptionsQueueOk.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    smgAlarmSipOptionsQueueOk.setStatus(
        "current"
    )

smgOkCDRFileTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 29, 2, 26)
)
smgOkCDRFileTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    smgOkCDRFileTrap.setStatus(
        "current"
    )

smgOkTrunkGroupCPSTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 29, 2, 29)
)
smgOkTrunkGroupCPSTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    smgOkTrunkGroupCPSTrap.setStatus(
        "current"
    )

smgOkDemoLicenseTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 29, 2, 30)
)
smgOkDemoLicenseTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    smgOkDemoLicenseTrap.setStatus(
        "current"
    )

smgOkSipDuplicateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 29, 2, 31)
)
smgOkSipDuplicateTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    smgOkSipDuplicateTrap.setStatus(
        "current"
    )

smgOkIpcOverloadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 29, 2, 51)
)
smgOkIpcOverloadTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    smgOkIpcOverloadTrap.setStatus(
        "current"
    )

smgOkCallForbiddenTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 29, 2, 52)
)
smgOkCallForbiddenTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    smgOkCallForbiddenTrap.setStatus(
        "current"
    )

smgOkRegForbiddenTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 29, 2, 53)
)
smgOkRegForbiddenTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    smgOkRegForbiddenTrap.setStatus(
        "current"
    )

smgOkSIPinterfaceTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 29, 2, 54)
)
smgOkSIPinterfaceTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    smgOkSIPinterfaceTrap.setStatus(
        "current"
    )

smgOkReserveSlaveLinkChangedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 29, 2, 55)
)
smgOkReserveSlaveLinkChangedTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    smgOkReserveSlaveLinkChangedTrap.setStatus(
        "current"
    )

smgOkReserveSlaveSoftVersionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 29, 2, 56)
)
smgOkReserveSlaveSoftVersionTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    smgOkReserveSlaveSoftVersionTrap.setStatus(
        "current"
    )

smgOkSipAttackedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 29, 2, 57)
)
smgOkSipAttackedTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    smgOkSipAttackedTrap.setStatus(
        "current"
    )

smgOkPctlModuleTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 29, 2, 58)
)
smgOkPctlModuleTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    smgOkPctlModuleTrap.setStatus(
        "current"
    )

smgOkPortScanDetectorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 29, 2, 59)
)
smgOkPortScanDetectorTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    smgOkPortScanDetectorTrap.setStatus(
        "current"
    )

smgOkFirewallTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 29, 2, 60)
)
smgOkFirewallTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    smgOkFirewallTrap.setStatus(
        "current"
    )

mccpConfigAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 30, 1)
)
mccpConfigAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    mccpConfigAlarmTrap.setStatus(
        "current"
    )

mccpSlotAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 30, 2)
)
mccpSlotAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    mccpSlotAlarmTrap.setStatus(
        "current"
    )

mccpLinksetAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 30, 3)
)
mccpLinksetAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    mccpLinksetAlarmTrap.setStatus(
        "current"
    )

mccpStreamAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 30, 4)
)
mccpStreamAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    mccpStreamAlarmTrap.setStatus(
        "current"
    )

mccpSS7LinkAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 30, 5)
)
mccpSS7LinkAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    mccpSS7LinkAlarmTrap.setStatus(
        "current"
    )

mccpSyncAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 30, 6)
)
mccpSyncAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    mccpSyncAlarmTrap.setStatus(
        "current"
    )

mccpIntfAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 30, 7)
)
mccpIntfAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    mccpIntfAlarmTrap.setStatus(
        "current"
    )

mccpIntfSlotAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 30, 8)
)
mccpIntfSlotAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    mccpIntfSlotAlarmTrap.setStatus(
        "current"
    )

mccpSutdownSnmpdAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 30, 17)
)
mccpSutdownSnmpdAlarmTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    mccpSutdownSnmpdAlarmTrap.setStatus(
        "current"
    )

mccpConfigOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 31, 1)
)
mccpConfigOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    mccpConfigOkTrap.setStatus(
        "current"
    )

mccpSlotOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 31, 2)
)
mccpSlotOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    mccpSlotOkTrap.setStatus(
        "current"
    )

mccpLinksetOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 31, 3)
)
mccpLinksetOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    mccpLinksetOkTrap.setStatus(
        "current"
    )

mccpStreamOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 31, 4)
)
mccpStreamOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    mccpStreamOkTrap.setStatus(
        "current"
    )

mccpSS7LinkOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 31, 5)
)
mccpSS7LinkOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    mccpSS7LinkOkTrap.setStatus(
        "current"
    )

mccpSyncOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 31, 6)
)
mccpSyncOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    mccpSyncOkTrap.setStatus(
        "current"
    )

mccpIntfOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 31, 7)
)
mccpIntfOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    mccpIntfOkTrap.setStatus(
        "current"
    )

mccpIntfSlotOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 31, 8)
)
mccpIntfSlotOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    mccpIntfSlotOkTrap.setStatus(
        "current"
    )

mccpStartOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 31, 16)
)
mccpStartOkTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    mccpStartOkTrap.setStatus(
        "current"
    )

radiusRequestNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 32, 1, 1)
)
radiusRequestNotification.setObjects(
      *(("ELTEX-SMI-ACTUAL", "radiusSeqNum"),
        ("ELTEX-SMI-ACTUAL", "radiusStatus"),
        ("ELTEX-SMI-ACTUAL", "radiusTimeout"),
        ("ELTEX-SMI-ACTUAL", "radiusSwitchSrv"),
        ("ELTEX-SMI-ACTUAL", "radiusTypeResp"),
        ("ELTEX-SMI-ACTUAL", "radiusDescr"))
)
if mibBuilder.loadTexts:
    radiusRequestNotification.setStatus(
        "current"
    )

eltexShutdownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 3, 99)
)
eltexShutdownTrap.setObjects(
      *(("ELTEX-SMI-ACTUAL", "mcTrapExState"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam1"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam2"),
        ("ELTEX-SMI-ACTUAL", "mcTrapLParam3"),
        ("ELTEX-SMI-ACTUAL", "mcTrapID"),
        ("ELTEX-SMI-ACTUAL", "mcTrapDescr"))
)
if mibBuilder.loadTexts:
    eltexShutdownTrap.setStatus(
        "current"
    )


# Notifications groups

eltrapNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 35265, 3, 100)
)
eltrapNotificationGroup.setObjects(
      *(("ELTEX-SMI-ACTUAL", "ponTeknovusONTAuthAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "ponTeknovusUplinkAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "ponTeknovusOpticalAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "ponTeknovusFanAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "ponTeknovusONTConfAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "ponTeknovusFlappingAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "ponTeknovusConfigSavedAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "ponTeknovusFirmwareUpdateAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "ponTeknovusRAMAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "ponTeknovusLoginAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "ponTeknovusDuplicateMacAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "ponTeknovusLoadAverageAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "ponTeknovusTemperatureAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "ponTeknovusONTPortBlockedAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "ponTeknovusONTAuthOkTrap"),
        ("ELTEX-SMI-ACTUAL", "ponTeknovusUplinkOkTrap"),
        ("ELTEX-SMI-ACTUAL", "ponTeknovusOpticalOkTrap"),
        ("ELTEX-SMI-ACTUAL", "ponTeknovusFanOkTrap"),
        ("ELTEX-SMI-ACTUAL", "ponTeknovusONTConfOKTrap"),
        ("ELTEX-SMI-ACTUAL", "ponTeknovusFlappingOkTrap"),
        ("ELTEX-SMI-ACTUAL", "ponTeknovusConfigSavedOkTrap"),
        ("ELTEX-SMI-ACTUAL", "ponTeknovusFirmwareUpdateOkTrap"),
        ("ELTEX-SMI-ACTUAL", "ponTeknovusRAMOkTrap"),
        ("ELTEX-SMI-ACTUAL", "ponTeknovusLoginOkTrap"),
        ("ELTEX-SMI-ACTUAL", "ponTeknovusLogoutOkTrap"),
        ("ELTEX-SMI-ACTUAL", "ponTeknovusSwitchConfigChangeTrap"),
        ("ELTEX-SMI-ACTUAL", "ponTeknovusLoadAverageOkTrap"),
        ("ELTEX-SMI-ACTUAL", "ponTeknovusTemperatureOkTrap"),
        ("ELTEX-SMI-ACTUAL", "ponTeknovusONTPortBlockedOkTrap"),
        ("ELTEX-SMI-ACTUAL", "ponTeknovusBoardRebootTrap"),
        ("ELTEX-SMI-ACTUAL", "ponTeknovusConfigMigrateAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "ponTeknovusConfigMigrateOkTrap"),
        ("ELTEX-SMI-ACTUAL", "ponTeknovusONTDeconfigureTrap"),
        ("ELTEX-SMI-ACTUAL", "ponTeknovusONTStateChangedTrap"),
        ("ELTEX-SMI-ACTUAL", "ponTeknovusONTConfigChangedTrap"),
        ("ELTEX-SMI-ACTUAL", "ponTeknovusConfigRereadTrap"),
        ("ELTEX-SMI-ACTUAL", "fxs72VbatAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "fxs72VringAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "fxs72TemperatureAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "fxs72FanAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "fxs72SSwAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "fxs72PortAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "fxs72VbatOkTrap"),
        ("ELTEX-SMI-ACTUAL", "fxs72VringOkTrap"),
        ("ELTEX-SMI-ACTUAL", "fxs72TemperatureOkTrap"),
        ("ELTEX-SMI-ACTUAL", "fxs72FanOkTrap"),
        ("ELTEX-SMI-ACTUAL", "fxs72SSwOkTrap"),
        ("ELTEX-SMI-ACTUAL", "fxs72PortOkTrap"),
        ("ELTEX-SMI-ACTUAL", "fxs72VmodeSwitchTrap"),
        ("ELTEX-SMI-ACTUAL", "fxs72FansSwitchTrap"),
        ("ELTEX-SMI-ACTUAL", "fxs72BpuAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "fxs72updateFwFail"),
        ("ELTEX-SMI-ACTUAL", "fxs72BpuOkTrap"),
        ("ELTEX-SMI-ACTUAL", "fxs72updateFwOk"),
        ("ELTEX-SMI-ACTUAL", "fxs72TempmeasurementAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "fxs72TempmeasurementOkTrap"),
        ("ELTEX-SMI-ACTUAL", "fxs72PowerUnitTermAlarm"),
        ("ELTEX-SMI-ACTUAL", "fxs72PowerUnitTermOk"),
        ("ELTEX-SMI-ACTUAL", "fxs72FanLowSpeedAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "fxs72FanLowSpeedOkTrap"),
        ("ELTEX-SMI-ACTUAL", "pp4LinkAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "pp4AutoNegotiationAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "pp4MemoryAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "pp4LoadAvgAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "pp4LoginAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "pp4LogoutAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "pp4LoadCpuAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "pp4DuplicationMacAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "pp4LinkFlapAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "pp4LinkOkTrap"),
        ("ELTEX-SMI-ACTUAL", "pp4AutoNegotiationOkTrap"),
        ("ELTEX-SMI-ACTUAL", "pp4MemoryOkTrap"),
        ("ELTEX-SMI-ACTUAL", "pp4LoadAvgOkTrap"),
        ("ELTEX-SMI-ACTUAL", "pp4LoginOkTrap"),
        ("ELTEX-SMI-ACTUAL", "pp4LogoutOkTrap"),
        ("ELTEX-SMI-ACTUAL", "pp4CommitOkTrap"),
        ("ELTEX-SMI-ACTUAL", "pp4SaveOkTrap"),
        ("ELTEX-SMI-ACTUAL", "pp4LinkFlapEndOkTrap"),
        ("ELTEX-SMI-ACTUAL", "pp4ConfigChangedOkTrap"),
        ("ELTEX-SMI-ACTUAL", "pp4SaveAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "pp4BoardRemoveAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "pp4UnitRemoveAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "pp4PortCounterErrorFoundAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "pp4SyncDisallowedAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "pp4RebootUnitAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "pp4RebootStackAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "pp4RebootFwTimerAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "pp4FwUpdateAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "pp4FwConfirmNeededAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "pp4BoardAddOkTrap"),
        ("ELTEX-SMI-ACTUAL", "pp4UnitAddOkTrap"),
        ("ELTEX-SMI-ACTUAL", "pp4RoleChangedOkTrap"),
        ("ELTEX-SMI-ACTUAL", "pp4PortCounterErrorFreeOkTrap"),
        ("ELTEX-SMI-ACTUAL", "pp4SyncDisallowedOkTrap"),
        ("ELTEX-SMI-ACTUAL", "pp4ConfigRestoredOkTrap"),
        ("ELTEX-SMI-ACTUAL", "pp4RebootUnitOkTrap"),
        ("ELTEX-SMI-ACTUAL", "pp4FwUpdateOkTrap"),
        ("ELTEX-SMI-ACTUAL", "mxa32DslLinkAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "mxa32EthLinkAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "mxa32TempAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "mxa32VoltAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "mxa32UserLoginTrap"),
        ("ELTEX-SMI-ACTUAL", "mxa32DslLinkOkTrap"),
        ("ELTEX-SMI-ACTUAL", "mxa32EthLinkOkTrap"),
        ("ELTEX-SMI-ACTUAL", "mxa32TempOkTrap"),
        ("ELTEX-SMI-ACTUAL", "mxa32VoltOkTrap"),
        ("ELTEX-SMI-ACTUAL", "mxa32UserLogoutTrap"),
        ("ELTEX-SMI-ACTUAL", "mxa64DslLinkAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "mxa64EthLinkAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "mxa64TempAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "mxa64VoltAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "mxa64UserLoginTrap"),
        ("ELTEX-SMI-ACTUAL", "mxa64DslLinkOkTrap"),
        ("ELTEX-SMI-ACTUAL", "mxa64EthLinkOkTrap"),
        ("ELTEX-SMI-ACTUAL", "mxa64TempOkTrap"),
        ("ELTEX-SMI-ACTUAL", "mxa64VoltOkTrap"),
        ("ELTEX-SMI-ACTUAL", "mxa64UserLogoutTrap"),
        ("ELTEX-SMI-ACTUAL", "mxa24DslLinkAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "mxa24EthLinkAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "mxa24TempAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "mxa24VoltAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "mxa24UserLoginTrap"),
        ("ELTEX-SMI-ACTUAL", "mxa24DslLinkOkTrap"),
        ("ELTEX-SMI-ACTUAL", "mxa24EthLinkOkTrap"),
        ("ELTEX-SMI-ACTUAL", "mxa24TempOkTrap"),
        ("ELTEX-SMI-ACTUAL", "mxa24VoltOkTrap"),
        ("ELTEX-SMI-ACTUAL", "mxa24UserLogoutTrap"),
        ("ELTEX-SMI-ACTUAL", "omsOperationCommandAlarm"),
        ("ELTEX-SMI-ACTUAL", "omsOperationCommandOk"),
        ("ELTEX-SMI-ACTUAL", "elcONTAuthAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "elcUplinkAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "elcOpticalAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "elcFanAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "elcONTConfAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "elcFlappingAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "elcConfigSavedAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "elcFirmwareUpdateAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "elcRAMAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "elcLoginAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "elcDuplicateMacAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "elcLoadAverageAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "elcTemperatureAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "elcONTAuthOkTrap"),
        ("ELTEX-SMI-ACTUAL", "elcUplinkOkTrap"),
        ("ELTEX-SMI-ACTUAL", "elcOpticalOkTrap"),
        ("ELTEX-SMI-ACTUAL", "elcFanOkTrap"),
        ("ELTEX-SMI-ACTUAL", "elcONTConfOKTrap"),
        ("ELTEX-SMI-ACTUAL", "elcFlappingOkTrap"),
        ("ELTEX-SMI-ACTUAL", "elcConfigSavedOkTrap"),
        ("ELTEX-SMI-ACTUAL", "elcFirmwareUpdateOkTrap"),
        ("ELTEX-SMI-ACTUAL", "elcRAMOkTrap"),
        ("ELTEX-SMI-ACTUAL", "elcLoginOkTrap"),
        ("ELTEX-SMI-ACTUAL", "elcLogoutOkTrap"),
        ("ELTEX-SMI-ACTUAL", "elcSwitchConfigChangeTrap"),
        ("ELTEX-SMI-ACTUAL", "elcLoadAverageOkTrap"),
        ("ELTEX-SMI-ACTUAL", "elcTemperatureOkTrap"),
        ("ELTEX-SMI-ACTUAL", "smgAlarmConfigTrap"),
        ("ELTEX-SMI-ACTUAL", "smgAlarmSiptNodeTrap"),
        ("ELTEX-SMI-ACTUAL", "smgAlarmMspDevTrap"),
        ("ELTEX-SMI-ACTUAL", "smgAlarmLinkSetTrap"),
        ("ELTEX-SMI-ACTUAL", "smgAlarmStreamTrap"),
        ("ELTEX-SMI-ACTUAL", "smgAlarmSS7LinkTrap"),
        ("ELTEX-SMI-ACTUAL", "smgAlarmSyncTrap"),
        ("ELTEX-SMI-ACTUAL", "smgOkConfigTrap"),
        ("ELTEX-SMI-ACTUAL", "smgOkSiptNodeTrap"),
        ("ELTEX-SMI-ACTUAL", "smgOkMspDevTrap"),
        ("ELTEX-SMI-ACTUAL", "smgOkLinkSetTrap"),
        ("ELTEX-SMI-ACTUAL", "smgOkStreamTrap"),
        ("ELTEX-SMI-ACTUAL", "smgOkSS7LinkTrap"),
        ("ELTEX-SMI-ACTUAL", "smgOkSyncTrap"),
        ("ELTEX-SMI-ACTUAL", "smgAlarmCdrFtpTrap"),
        ("ELTEX-SMI-ACTUAL", "smgOkCdrFtpTrap"),
        ("ELTEX-SMI-ACTUAL", "smgUpdateFwFail"),
        ("ELTEX-SMI-ACTUAL", "smgUpdateFwOk"),
        ("ELTEX-SMI-ACTUAL", "smgAlarmMemoryLimitTrap"),
        ("ELTEX-SMI-ACTUAL", "smgAlarmSbcRegistrationExpiredTrap"),
        ("ELTEX-SMI-ACTUAL", "smgAlarmIpcOverloadTrap"),
        ("ELTEX-SMI-ACTUAL", "smgOkMemoryLimitTrap"),
        ("ELTEX-SMI-ACTUAL", "smgOkIpcOverloadTrap"),
        ("ELTEX-SMI-ACTUAL", "smgAlarmProcOverloadTrap"),
        ("ELTEX-SMI-ACTUAL", "smgOkProcOverloadTrap"),
        ("ELTEX-SMI-ACTUAL", "smgOkRebootTrap"),
        ("ELTEX-SMI-ACTUAL", "smgOkFansIdleTrap"),
        ("ELTEX-SMI-ACTUAL", "smgOkDriveLimitTrap"),
        ("ELTEX-SMI-ACTUAL", "smgAlarmFansIdleTrap"),
        ("ELTEX-SMI-ACTUAL", "smgAlarmDriveLimitTrap"),
        ("ELTEX-SMI-ACTUAL", "smgAlarmSipOptionsQueueOverload"),
        ("ELTEX-SMI-ACTUAL", "smgAlarmSipOptionsQueueOk"),
        ("ELTEX-SMI-ACTUAL", "smgAlarmCDRFileTrap"),
        ("ELTEX-SMI-ACTUAL", "smgOkCDRFileTrap"),
        ("ELTEX-SMI-ACTUAL", "smgAlarmSipDuplicateTrap"),
        ("ELTEX-SMI-ACTUAL", "smgOkSipDuplicateTrap"),
        ("ELTEX-SMI-ACTUAL", "smgReserveSlaveLinkChangedTrap"),
        ("ELTEX-SMI-ACTUAL", "smgOkReserveSlaveLinkChangedTrap"),
        ("ELTEX-SMI-ACTUAL", "smgReserveSlaveSoftVersionTrap"),
        ("ELTEX-SMI-ACTUAL", "smgOkReserveSlaveSoftVersionTrap"),
        ("ELTEX-SMI-ACTUAL", "smgSipAttackedTrap"),
        ("ELTEX-SMI-ACTUAL", "smgOkSipAttackedTrap"),
        ("ELTEX-SMI-ACTUAL", "smgCallForbiddenTrap"),
        ("ELTEX-SMI-ACTUAL", "smgOkCallForbiddenTrap"),
        ("ELTEX-SMI-ACTUAL", "smgRegForbiddenTrap"),
        ("ELTEX-SMI-ACTUAL", "smgOkRegForbiddenTrap"),
        ("ELTEX-SMI-ACTUAL", "smgSIPinterfaceTrap"),
        ("ELTEX-SMI-ACTUAL", "smgOkSIPinterfaceTrap"),
        ("ELTEX-SMI-ACTUAL", "smgPctlModuleTrap"),
        ("ELTEX-SMI-ACTUAL", "smgOkPctlModuleTrap"),
        ("ELTEX-SMI-ACTUAL", "smgPortScanDetectorTrap"),
        ("ELTEX-SMI-ACTUAL", "smgOkPortScanDetectorTrap"),
        ("ELTEX-SMI-ACTUAL", "smgFirewallTrap"),
        ("ELTEX-SMI-ACTUAL", "smgOkFirewallTrap"),
        ("ELTEX-SMI-ACTUAL", "mccpConfigAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "mccpSlotAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "mccpLinksetAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "mccpStreamAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "mccpSS7LinkAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "mccpSyncAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "mccpIntfAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "mccpIntfSlotAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "mccpSutdownSnmpdAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "mccpConfigOkTrap"),
        ("ELTEX-SMI-ACTUAL", "mccpSlotOkTrap"),
        ("ELTEX-SMI-ACTUAL", "mccpLinksetOkTrap"),
        ("ELTEX-SMI-ACTUAL", "mccpStreamOkTrap"),
        ("ELTEX-SMI-ACTUAL", "mccpSS7LinkOkTrap"),
        ("ELTEX-SMI-ACTUAL", "mccpSyncOkTrap"),
        ("ELTEX-SMI-ACTUAL", "mccpIntfOkTrap"),
        ("ELTEX-SMI-ACTUAL", "mccpIntfSlotOkTrap"),
        ("ELTEX-SMI-ACTUAL", "mccpStartOkTrap"),
        ("ELTEX-SMI-ACTUAL", "radiusRequestNotification"),
        ("ELTEX-SMI-ACTUAL", "eltexShutdownTrap"))
)
if mibBuilder.loadTexts:
    eltrapNotificationGroup.setStatus(
        "current"
    )

eltrapDepNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 35265, 3, 103)
)
eltrapDepNotificationGroup.setObjects(
      *(("ELTEX-SMI-ACTUAL", "ponTeknovusEponAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "ponTeknovusUserLoginAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "ponTeknovusUserLoginOkTrap"),
        ("ELTEX-SMI-ACTUAL", "ponTeknovusEponOkTrap"),
        ("ELTEX-SMI-ACTUAL", "elcEponAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "elcUserLoginAlarmTrap"),
        ("ELTEX-SMI-ACTUAL", "elcUserLoginOkTrap"),
        ("ELTEX-SMI-ACTUAL", "elcEponOkTrap"))
)
if mibBuilder.loadTexts:
    eltrapDepNotificationGroup.setStatus(
        "deprecated"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-SMI-ACTUAL",
    **{"eltexLtd": eltexLtd,
       "elHardware": elHardware,
       "elSoftware": elSoftware,
       "eltrapGroup": eltrapGroup,
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
       "radiusSeqNum": radiusSeqNum,
       "radiusStatus": radiusStatus,
       "radiusTimeout": radiusTimeout,
       "radiusSwitchSrv": radiusSwitchSrv,
       "radiusTypeResp": radiusTypeResp,
       "radiusDescr": radiusDescr,
       "fxs72AlarmTraps": fxs72AlarmTraps,
       "fxs72VbatAlarmTrap": fxs72VbatAlarmTrap,
       "fxs72VringAlarmTrap": fxs72VringAlarmTrap,
       "fxs72TemperatureAlarmTrap": fxs72TemperatureAlarmTrap,
       "fxs72FanAlarmTrap": fxs72FanAlarmTrap,
       "fxs72SSwAlarmTrap": fxs72SSwAlarmTrap,
       "fxs72PortAlarmTrap": fxs72PortAlarmTrap,
       "fxs72BpuAlarmTrap": fxs72BpuAlarmTrap,
       "fxs72TempmeasurementAlarmTrap": fxs72TempmeasurementAlarmTrap,
       "fxs72LicenseAlarmTrap": fxs72LicenseAlarmTrap,
       "fxs72updateFwFail": fxs72updateFwFail,
       "fxs72PowerUnitTermAlarm": fxs72PowerUnitTermAlarm,
       "fxs72FanLowSpeedAlarmTrap": fxs72FanLowSpeedAlarmTrap,
       "fxs72OkTraps": fxs72OkTraps,
       "fxs72VbatOkTrap": fxs72VbatOkTrap,
       "fxs72VringOkTrap": fxs72VringOkTrap,
       "fxs72TemperatureOkTrap": fxs72TemperatureOkTrap,
       "fxs72FanOkTrap": fxs72FanOkTrap,
       "fxs72SSwOkTrap": fxs72SSwOkTrap,
       "fxs72PortOkTrap": fxs72PortOkTrap,
       "fxs72VmodeSwitchTrap": fxs72VmodeSwitchTrap,
       "fxs72FansSwitchTrap": fxs72FansSwitchTrap,
       "fxs72BpuOkTrap": fxs72BpuOkTrap,
       "fxs72TempmeasurementOkTrap": fxs72TempmeasurementOkTrap,
       "fxs72LicenseOkTrap": fxs72LicenseOkTrap,
       "fxs72updateFwOk": fxs72updateFwOk,
       "fxs72PowerUnitTermOk": fxs72PowerUnitTermOk,
       "fxs72FanLowSpeedOkTrap": fxs72FanLowSpeedOkTrap,
       "ponTeknovusAlarmTraps": ponTeknovusAlarmTraps,
       "ponTeknovusONTAuthAlarmTrap": ponTeknovusONTAuthAlarmTrap,
       "ponTeknovusUplinkAlarmTrap": ponTeknovusUplinkAlarmTrap,
       "ponTeknovusOpticalAlarmTrap": ponTeknovusOpticalAlarmTrap,
       "ponTeknovusFanAlarmTrap": ponTeknovusFanAlarmTrap,
       "ponTeknovusONTConfAlarmTrap": ponTeknovusONTConfAlarmTrap,
       "ponTeknovusFlappingAlarmTrap": ponTeknovusFlappingAlarmTrap,
       "ponTeknovusEponAlarmTrap": ponTeknovusEponAlarmTrap,
       "ponTeknovusConfigSavedAlarmTrap": ponTeknovusConfigSavedAlarmTrap,
       "ponTeknovusFirmwareUpdateAlarmTrap": ponTeknovusFirmwareUpdateAlarmTrap,
       "ponTeknovusUserLoginAlarmTrap": ponTeknovusUserLoginAlarmTrap,
       "ponTeknovusRAMAlarmTrap": ponTeknovusRAMAlarmTrap,
       "ponTeknovusLoginAlarmTrap": ponTeknovusLoginAlarmTrap,
       "ponTeknovusDuplicateMacAlarmTrap": ponTeknovusDuplicateMacAlarmTrap,
       "ponTeknovusLoadAverageAlarmTrap": ponTeknovusLoadAverageAlarmTrap,
       "ponTeknovusTemperatureAlarmTrap": ponTeknovusTemperatureAlarmTrap,
       "ponTeknovusONTPortBlockedAlarmTrap": ponTeknovusONTPortBlockedAlarmTrap,
       "ponTeknovusConfigMigrateAlarmTrap": ponTeknovusConfigMigrateAlarmTrap,
       "ponTeknovusOkTraps": ponTeknovusOkTraps,
       "ponTeknovusONTAuthOkTrap": ponTeknovusONTAuthOkTrap,
       "ponTeknovusUplinkOkTrap": ponTeknovusUplinkOkTrap,
       "ponTeknovusOpticalOkTrap": ponTeknovusOpticalOkTrap,
       "ponTeknovusFanOkTrap": ponTeknovusFanOkTrap,
       "ponTeknovusONTConfOKTrap": ponTeknovusONTConfOKTrap,
       "ponTeknovusFlappingOkTrap": ponTeknovusFlappingOkTrap,
       "ponTeknovusEponOkTrap": ponTeknovusEponOkTrap,
       "ponTeknovusConfigSavedOkTrap": ponTeknovusConfigSavedOkTrap,
       "ponTeknovusFirmwareUpdateOkTrap": ponTeknovusFirmwareUpdateOkTrap,
       "ponTeknovusUserLoginOkTrap": ponTeknovusUserLoginOkTrap,
       "ponTeknovusRAMOkTrap": ponTeknovusRAMOkTrap,
       "ponTeknovusLoginOkTrap": ponTeknovusLoginOkTrap,
       "ponTeknovusLogoutOkTrap": ponTeknovusLogoutOkTrap,
       "ponTeknovusSwitchConfigChangeTrap": ponTeknovusSwitchConfigChangeTrap,
       "ponTeknovusLoadAverageOkTrap": ponTeknovusLoadAverageOkTrap,
       "ponTeknovusTemperatureOkTrap": ponTeknovusTemperatureOkTrap,
       "ponTeknovusONTPortBlockedOkTrap": ponTeknovusONTPortBlockedOkTrap,
       "ponTeknovusConfigMigrateOkTrap": ponTeknovusConfigMigrateOkTrap,
       "ponTeknovusBoardRebootTrap": ponTeknovusBoardRebootTrap,
       "ponTeknovusONTDeconfigureTrap": ponTeknovusONTDeconfigureTrap,
       "ponTeknovusONTStateChangedTrap": ponTeknovusONTStateChangedTrap,
       "ponTeknovusONTConfigChangedTrap": ponTeknovusONTConfigChangedTrap,
       "ponTeknovusConfigRereadTrap": ponTeknovusConfigRereadTrap,
       "pp4AlarmTraps": pp4AlarmTraps,
       "pp4LinkAlarmTrap": pp4LinkAlarmTrap,
       "pp4AutoNegotiationAlarmTrap": pp4AutoNegotiationAlarmTrap,
       "pp4MemoryAlarmTrap": pp4MemoryAlarmTrap,
       "pp4LoadAvgAlarmTrap": pp4LoadAvgAlarmTrap,
       "pp4LoginAlarmTrap": pp4LoginAlarmTrap,
       "pp4LogoutAlarmTrap": pp4LogoutAlarmTrap,
       "pp4SaveAlarmTrap": pp4SaveAlarmTrap,
       "pp4LoadCpuAlarmTrap": pp4LoadCpuAlarmTrap,
       "pp4DuplicationMacAlarmTrap": pp4DuplicationMacAlarmTrap,
       "pp4LinkFlapAlarmTrap": pp4LinkFlapAlarmTrap,
       "pp4BoardRemoveAlarmTrap": pp4BoardRemoveAlarmTrap,
       "pp4UnitRemoveAlarmTrap": pp4UnitRemoveAlarmTrap,
       "pp4PortCounterErrorFoundAlarmTrap": pp4PortCounterErrorFoundAlarmTrap,
       "pp4SyncDisallowedAlarmTrap": pp4SyncDisallowedAlarmTrap,
       "pp4RebootUnitAlarmTrap": pp4RebootUnitAlarmTrap,
       "pp4RebootStackAlarmTrap": pp4RebootStackAlarmTrap,
       "pp4RebootFwTimerAlarmTrap": pp4RebootFwTimerAlarmTrap,
       "pp4FwUpdateAlarmTrap": pp4FwUpdateAlarmTrap,
       "pp4FwConfirmNeededAlarmTrap": pp4FwConfirmNeededAlarmTrap,
       "pp4OkTraps": pp4OkTraps,
       "pp4LinkOkTrap": pp4LinkOkTrap,
       "pp4AutoNegotiationOkTrap": pp4AutoNegotiationOkTrap,
       "pp4MemoryOkTrap": pp4MemoryOkTrap,
       "pp4LoadAvgOkTrap": pp4LoadAvgOkTrap,
       "pp4LoginOkTrap": pp4LoginOkTrap,
       "pp4LogoutOkTrap": pp4LogoutOkTrap,
       "pp4CommitOkTrap": pp4CommitOkTrap,
       "pp4SaveOkTrap": pp4SaveOkTrap,
       "pp4LinkFlapEndOkTrap": pp4LinkFlapEndOkTrap,
       "pp4ConfigChangedOkTrap": pp4ConfigChangedOkTrap,
       "pp4BoardAddOkTrap": pp4BoardAddOkTrap,
       "pp4UnitAddOkTrap": pp4UnitAddOkTrap,
       "pp4RoleChangedOkTrap": pp4RoleChangedOkTrap,
       "pp4PortCounterErrorFreeOkTrap": pp4PortCounterErrorFreeOkTrap,
       "pp4SyncDisallowedOkTrap": pp4SyncDisallowedOkTrap,
       "pp4ConfigRestoredOkTrap": pp4ConfigRestoredOkTrap,
       "pp4RebootUnitOkTrap": pp4RebootUnitOkTrap,
       "pp4FwUpdateOkTrap": pp4FwUpdateOkTrap,
       "mxa32AlarmTraps": mxa32AlarmTraps,
       "mxa32DslLinkAlarmTrap": mxa32DslLinkAlarmTrap,
       "mxa32EthLinkAlarmTrap": mxa32EthLinkAlarmTrap,
       "mxa32TempAlarmTrap": mxa32TempAlarmTrap,
       "mxa32VoltAlarmTrap": mxa32VoltAlarmTrap,
       "mxa32UserLoginTrap": mxa32UserLoginTrap,
       "mxa32OkTraps": mxa32OkTraps,
       "mxa32DslLinkOkTrap": mxa32DslLinkOkTrap,
       "mxa32EthLinkOkTrap": mxa32EthLinkOkTrap,
       "mxa32TempOkTrap": mxa32TempOkTrap,
       "mxa32VoltOkTrap": mxa32VoltOkTrap,
       "mxa32UserLogoutTrap": mxa32UserLogoutTrap,
       "mxa64AlarmTraps": mxa64AlarmTraps,
       "mxa64DslLinkAlarmTrap": mxa64DslLinkAlarmTrap,
       "mxa64EthLinkAlarmTrap": mxa64EthLinkAlarmTrap,
       "mxa64TempAlarmTrap": mxa64TempAlarmTrap,
       "mxa64VoltAlarmTrap": mxa64VoltAlarmTrap,
       "mxa64UserLoginTrap": mxa64UserLoginTrap,
       "mxa64OkTraps": mxa64OkTraps,
       "mxa64DslLinkOkTrap": mxa64DslLinkOkTrap,
       "mxa64EthLinkOkTrap": mxa64EthLinkOkTrap,
       "mxa64TempOkTrap": mxa64TempOkTrap,
       "mxa64VoltOkTrap": mxa64VoltOkTrap,
       "mxa64UserLogoutTrap": mxa64UserLogoutTrap,
       "mxa24AlarmTraps": mxa24AlarmTraps,
       "mxa24DslLinkAlarmTrap": mxa24DslLinkAlarmTrap,
       "mxa24EthLinkAlarmTrap": mxa24EthLinkAlarmTrap,
       "mxa24TempAlarmTrap": mxa24TempAlarmTrap,
       "mxa24VoltAlarmTrap": mxa24VoltAlarmTrap,
       "mxa24UserLoginTrap": mxa24UserLoginTrap,
       "mxa24OkTraps": mxa24OkTraps,
       "mxa24DslLinkOkTrap": mxa24DslLinkOkTrap,
       "mxa24EthLinkOkTrap": mxa24EthLinkOkTrap,
       "mxa24TempOkTrap": mxa24TempOkTrap,
       "mxa24VoltOkTrap": mxa24VoltOkTrap,
       "mxa24UserLogoutTrap": mxa24UserLogoutTrap,
       "omsOperationAlarmTraps": omsOperationAlarmTraps,
       "omsOperationCommandAlarm": omsOperationCommandAlarm,
       "omsOperationOkTraps": omsOperationOkTraps,
       "omsOperationCommandOk": omsOperationCommandOk,
       "elcAlarmTraps": elcAlarmTraps,
       "elcONTAuthAlarmTrap": elcONTAuthAlarmTrap,
       "elcUplinkAlarmTrap": elcUplinkAlarmTrap,
       "elcOpticalAlarmTrap": elcOpticalAlarmTrap,
       "elcFanAlarmTrap": elcFanAlarmTrap,
       "elcONTConfAlarmTrap": elcONTConfAlarmTrap,
       "elcFlappingAlarmTrap": elcFlappingAlarmTrap,
       "elcEponAlarmTrap": elcEponAlarmTrap,
       "elcConfigSavedAlarmTrap": elcConfigSavedAlarmTrap,
       "elcFirmwareUpdateAlarmTrap": elcFirmwareUpdateAlarmTrap,
       "elcUserLoginAlarmTrap": elcUserLoginAlarmTrap,
       "elcRAMAlarmTrap": elcRAMAlarmTrap,
       "elcLoginAlarmTrap": elcLoginAlarmTrap,
       "elcDuplicateMacAlarmTrap": elcDuplicateMacAlarmTrap,
       "elcLoadAverageAlarmTrap": elcLoadAverageAlarmTrap,
       "elcTemperatureAlarmTrap": elcTemperatureAlarmTrap,
       "elcOkTraps": elcOkTraps,
       "elcONTAuthOkTrap": elcONTAuthOkTrap,
       "elcUplinkOkTrap": elcUplinkOkTrap,
       "elcOpticalOkTrap": elcOpticalOkTrap,
       "elcFanOkTrap": elcFanOkTrap,
       "elcONTConfOKTrap": elcONTConfOKTrap,
       "elcFlappingOkTrap": elcFlappingOkTrap,
       "elcEponOkTrap": elcEponOkTrap,
       "elcConfigSavedOkTrap": elcConfigSavedOkTrap,
       "elcFirmwareUpdateOkTrap": elcFirmwareUpdateOkTrap,
       "elcUserLoginOkTrap": elcUserLoginOkTrap,
       "elcRAMOkTrap": elcRAMOkTrap,
       "elcLoginOkTrap": elcLoginOkTrap,
       "elcLogoutOkTrap": elcLogoutOkTrap,
       "elcSwitchConfigChangeTrap": elcSwitchConfigChangeTrap,
       "elcLoadAverageOkTrap": elcLoadAverageOkTrap,
       "elcTemperatureOkTrap": elcTemperatureOkTrap,
       "smgTraps": smgTraps,
       "smgAlarm": smgAlarm,
       "smgAlarmConfigTrap": smgAlarmConfigTrap,
       "smgAlarmSiptNodeTrap": smgAlarmSiptNodeTrap,
       "smgAlarmMspDevTrap": smgAlarmMspDevTrap,
       "smgAlarmLinkSetTrap": smgAlarmLinkSetTrap,
       "smgAlarmStreamTrap": smgAlarmStreamTrap,
       "smgAlarmSS7LinkTrap": smgAlarmSS7LinkTrap,
       "smgAlarmSyncTrap": smgAlarmSyncTrap,
       "smgAlarmCdrFtpTrap": smgAlarmCdrFtpTrap,
       "smgAlarmMemoryLimitTrap": smgAlarmMemoryLimitTrap,
       "smgAlarmPowerModuleStateTrap": smgAlarmPowerModuleStateTrap,
       "smgAlarmH323NodeTrap": smgAlarmH323NodeTrap,
       "smgAlarmTemperatureTrap": smgAlarmTemperatureTrap,
       "smgAlarmMaintenanceTrap": smgAlarmMaintenanceTrap,
       "smgAlarmSipAccessTrap": smgAlarmSipAccessTrap,
       "smgUpdateFwFail": smgUpdateFwFail,
       "smgAlarmProcOverloadTrap": smgAlarmProcOverloadTrap,
       "smgAlarmFansIdleTrap": smgAlarmFansIdleTrap,
       "smgAlarmDriveLimitTrap": smgAlarmDriveLimitTrap,
       "smgAlarmSipOptionsQueueOverload": smgAlarmSipOptionsQueueOverload,
       "smgAlarmCDRFileTrap": smgAlarmCDRFileTrap,
       "smgAlarmMegacoNodeTrap": smgAlarmMegacoNodeTrap,
       "smgFail2banBlockTrap": smgFail2banBlockTrap,
       "smgTrunkGroupCPSTrap": smgTrunkGroupCPSTrap,
       "smgDemoLicenseTrap": smgDemoLicenseTrap,
       "smgAlarmSipDuplicateTrap": smgAlarmSipDuplicateTrap,
       "smgAlarmSbcRegistrationExpiredTrap": smgAlarmSbcRegistrationExpiredTrap,
       "smgAlarmIpcOverloadTrap": smgAlarmIpcOverloadTrap,
       "smgCallForbiddenTrap": smgCallForbiddenTrap,
       "smgRegForbiddenTrap": smgRegForbiddenTrap,
       "smgSIPinterfaceTrap": smgSIPinterfaceTrap,
       "smgReserveSlaveLinkChangedTrap": smgReserveSlaveLinkChangedTrap,
       "smgReserveSlaveSoftVersionTrap": smgReserveSlaveSoftVersionTrap,
       "smgSipAttackedTrap": smgSipAttackedTrap,
       "smgPctlModuleTrap": smgPctlModuleTrap,
       "smgPortScanDetectorTrap": smgPortScanDetectorTrap,
       "smgFirewallTrap": smgFirewallTrap,
       "smgOK": smgOK,
       "smgOkConfigTrap": smgOkConfigTrap,
       "smgOkSiptNodeTrap": smgOkSiptNodeTrap,
       "smgOkMspDevTrap": smgOkMspDevTrap,
       "smgOkLinkSetTrap": smgOkLinkSetTrap,
       "smgOkStreamTrap": smgOkStreamTrap,
       "smgOkSS7LinkTrap": smgOkSS7LinkTrap,
       "smgOkSyncTrap": smgOkSyncTrap,
       "smgOkCdrFtpTrap": smgOkCdrFtpTrap,
       "smgOkMemoryLimitTrap": smgOkMemoryLimitTrap,
       "smgOkPowerModuleStateTrap": smgOkPowerModuleStateTrap,
       "smgOkH323NodeTrap": smgOkH323NodeTrap,
       "smgOkTemperatureTrap": smgOkTemperatureTrap,
       "smgOkMaintenanceTrap": smgOkMaintenanceTrap,
       "smgOkSipAccessTrap": smgOkSipAccessTrap,
       "smgUpdateFwOk": smgUpdateFwOk,
       "smgOkProcOverloadTrap": smgOkProcOverloadTrap,
       "smgOkRebootTrap": smgOkRebootTrap,
       "smgOkFansIdleTrap": smgOkFansIdleTrap,
       "smgOkDriveLimitTrap": smgOkDriveLimitTrap,
       "smgAlarmSipOptionsQueueOk": smgAlarmSipOptionsQueueOk,
       "smgOkCDRFileTrap": smgOkCDRFileTrap,
       "smgOkTrunkGroupCPSTrap": smgOkTrunkGroupCPSTrap,
       "smgOkDemoLicenseTrap": smgOkDemoLicenseTrap,
       "smgOkSipDuplicateTrap": smgOkSipDuplicateTrap,
       "smgOkIpcOverloadTrap": smgOkIpcOverloadTrap,
       "smgOkCallForbiddenTrap": smgOkCallForbiddenTrap,
       "smgOkRegForbiddenTrap": smgOkRegForbiddenTrap,
       "smgOkSIPinterfaceTrap": smgOkSIPinterfaceTrap,
       "smgOkReserveSlaveLinkChangedTrap": smgOkReserveSlaveLinkChangedTrap,
       "smgOkReserveSlaveSoftVersionTrap": smgOkReserveSlaveSoftVersionTrap,
       "smgOkSipAttackedTrap": smgOkSipAttackedTrap,
       "smgOkPctlModuleTrap": smgOkPctlModuleTrap,
       "smgOkPortScanDetectorTrap": smgOkPortScanDetectorTrap,
       "smgOkFirewallTrap": smgOkFirewallTrap,
       "mccpAlarmTraps": mccpAlarmTraps,
       "mccpConfigAlarmTrap": mccpConfigAlarmTrap,
       "mccpSlotAlarmTrap": mccpSlotAlarmTrap,
       "mccpLinksetAlarmTrap": mccpLinksetAlarmTrap,
       "mccpStreamAlarmTrap": mccpStreamAlarmTrap,
       "mccpSS7LinkAlarmTrap": mccpSS7LinkAlarmTrap,
       "mccpSyncAlarmTrap": mccpSyncAlarmTrap,
       "mccpIntfAlarmTrap": mccpIntfAlarmTrap,
       "mccpIntfSlotAlarmTrap": mccpIntfSlotAlarmTrap,
       "mccpSutdownSnmpdAlarmTrap": mccpSutdownSnmpdAlarmTrap,
       "mccpOkTraps": mccpOkTraps,
       "mccpConfigOkTrap": mccpConfigOkTrap,
       "mccpSlotOkTrap": mccpSlotOkTrap,
       "mccpLinksetOkTrap": mccpLinksetOkTrap,
       "mccpStreamOkTrap": mccpStreamOkTrap,
       "mccpSS7LinkOkTrap": mccpSS7LinkOkTrap,
       "mccpSyncOkTrap": mccpSyncOkTrap,
       "mccpIntfOkTrap": mccpIntfOkTrap,
       "mccpIntfSlotOkTrap": mccpIntfSlotOkTrap,
       "mccpStartOkTrap": mccpStartOkTrap,
       "radiusTraps": radiusTraps,
       "radiusNotification": radiusNotification,
       "radiusRequestNotification": radiusRequestNotification,
       "eltexShutdownTrap": eltexShutdownTrap,
       "eltrapNotificationGroup": eltrapNotificationGroup,
       "eltrapObjectGroup": eltrapObjectGroup,
       "eltrapDepNotificationGroup": eltrapDepNotificationGroup}
)
