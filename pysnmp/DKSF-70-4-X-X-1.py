# SNMP MIB module (DKSF-70-4-X-X-1) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DKSF-70-4-X-X-1
# Produced by pysmi-1.5.4 at Mon Oct 14 21:29:26 2024
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

(snmpTraps,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "snmpTraps")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

uniPingServerSolutionV3 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 70)
)
uniPingServerSolutionV3.setRevisions(
        ("2015-05-29 00:00",
         "2014-12-03 00:00",
         "2014-11-26 00:00",
         "2014-02-02 00:00",
         "2014-01-29 00:00",
         "2014-01-21 00:00",
         "2013-04-11 00:00",
         "2012-05-31 00:00",
         "2012-04-17 00:00",
         "2012-03-23 00:00",
         "2011-09-23 00:00",
         "2011-03-24 00:00",
         "2010-10-14 00:00",
         "2010-09-20 00:00",
         "2010-05-31 00:00",
         "2010-04-14 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Lightcom_ObjectIdentity = ObjectIdentity
lightcom = _Lightcom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728)
)
_NpTrapInfo_ObjectIdentity = ObjectIdentity
npTrapInfo = _NpTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 90)
)
_NpTrapEmailTo_Type = DisplayString
_NpTrapEmailTo_Object = MibScalar
npTrapEmailTo = _NpTrapEmailTo_Object(
    (1, 3, 6, 1, 4, 1, 25728, 90, 1),
    _NpTrapEmailTo_Type()
)
npTrapEmailTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npTrapEmailTo.setStatus("current")
_NpReboot_ObjectIdentity = ObjectIdentity
npReboot = _NpReboot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 911)
)
_NpSoftReboot_Type = Integer32
_NpSoftReboot_Object = MibScalar
npSoftReboot = _NpSoftReboot_Object(
    (1, 3, 6, 1, 4, 1, 25728, 911, 1),
    _NpSoftReboot_Type()
)
npSoftReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npSoftReboot.setStatus("current")
_NpResetStack_Type = Integer32
_NpResetStack_Object = MibScalar
npResetStack = _NpResetStack_Object(
    (1, 3, 6, 1, 4, 1, 25728, 911, 2),
    _NpResetStack_Type()
)
npResetStack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npResetStack.setStatus("current")
_NpForcedReboot_Type = Integer32
_NpForcedReboot_Object = MibScalar
npForcedReboot = _NpForcedReboot_Object(
    (1, 3, 6, 1, 4, 1, 25728, 911, 3),
    _NpForcedReboot_Type()
)
npForcedReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npForcedReboot.setStatus("current")
_NpGsm_ObjectIdentity = ObjectIdentity
npGsm = _NpGsm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 3800)
)
_NpGsmInfo_ObjectIdentity = ObjectIdentity
npGsmInfo = _NpGsmInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 3800, 1)
)


class _NpGsmFailed_Type(Integer32):
    """Custom type npGsmFailed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 1),
          ("fatalError", 2),
          ("ok", 0))
    )


_NpGsmFailed_Type.__name__ = "Integer32"
_NpGsmFailed_Object = MibScalar
npGsmFailed = _NpGsmFailed_Object(
    (1, 3, 6, 1, 4, 1, 25728, 3800, 1, 1),
    _NpGsmFailed_Type()
)
npGsmFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npGsmFailed.setStatus("current")


class _NpGsmRegistration_Type(Integer32):
    """Custom type npGsmRegistration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              255)
        )
    )
    namedValues = NamedValues(
        *(("denied", 3),
          ("homeNetwork", 1),
          ("impossible", 0),
          ("infoUpdate", 255),
          ("roaming", 5),
          ("searching", 2),
          ("unknown", 4))
    )


_NpGsmRegistration_Type.__name__ = "Integer32"
_NpGsmRegistration_Object = MibScalar
npGsmRegistration = _NpGsmRegistration_Object(
    (1, 3, 6, 1, 4, 1, 25728, 3800, 1, 2),
    _NpGsmRegistration_Type()
)
npGsmRegistration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npGsmRegistration.setStatus("current")


class _NpGsmStrength_Type(Integer32):
    """Custom type npGsmStrength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NpGsmStrength_Type.__name__ = "Integer32"
_NpGsmStrength_Object = MibScalar
npGsmStrength = _NpGsmStrength_Object(
    (1, 3, 6, 1, 4, 1, 25728, 3800, 1, 3),
    _NpGsmStrength_Type()
)
npGsmStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npGsmStrength.setStatus("current")
_NpGsmSendSms_Type = DisplayString
_NpGsmSendSms_Object = MibScalar
npGsmSendSms = _NpGsmSendSms_Object(
    (1, 3, 6, 1, 4, 1, 25728, 3800, 1, 9),
    _NpGsmSendSms_Type()
)
npGsmSendSms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npGsmSendSms.setStatus("current")
_NpGsmTraps_ObjectIdentity = ObjectIdentity
npGsmTraps = _NpGsmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 3800, 2)
)
_NpGsmTrapPrefix_ObjectIdentity = ObjectIdentity
npGsmTrapPrefix = _NpGsmTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 3800, 2, 0)
)
_NpRelay_ObjectIdentity = ObjectIdentity
npRelay = _NpRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 5500)
)
_NpRelayTable_Object = MibTable
npRelayTable = _NpRelayTable_Object(
    (1, 3, 6, 1, 4, 1, 25728, 5500, 5)
)
if mibBuilder.loadTexts:
    npRelayTable.setStatus("current")
_NpRelayEntry_Object = MibTableRow
npRelayEntry = _NpRelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 25728, 5500, 5, 1)
)
npRelayEntry.setIndexNames(
    (0, "DKSF-70-4-X-X-1", "npRelayN"),
)
if mibBuilder.loadTexts:
    npRelayEntry.setStatus("current")


class _NpRelayN_Type(Integer32):
    """Custom type npRelayN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_NpRelayN_Type.__name__ = "Integer32"
_NpRelayN_Object = MibTableColumn
npRelayN = _NpRelayN_Object(
    (1, 3, 6, 1, 4, 1, 25728, 5500, 5, 1, 1),
    _NpRelayN_Type()
)
npRelayN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npRelayN.setStatus("current")


class _NpRelayMode_Type(Integer32):
    """Custom type npRelayMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("flip", -1),
          ("logic", 5),
          ("off", 0),
          ("on", 1),
          ("schedule", 3),
          ("scheduleAndWatchdog", 4),
          ("watchdog", 2))
    )


_NpRelayMode_Type.__name__ = "Integer32"
_NpRelayMode_Object = MibTableColumn
npRelayMode = _NpRelayMode_Object(
    (1, 3, 6, 1, 4, 1, 25728, 5500, 5, 1, 2),
    _NpRelayMode_Type()
)
npRelayMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npRelayMode.setStatus("current")
_NpRelayStartReset_Type = Integer32
_NpRelayStartReset_Object = MibTableColumn
npRelayStartReset = _NpRelayStartReset_Object(
    (1, 3, 6, 1, 4, 1, 25728, 5500, 5, 1, 3),
    _NpRelayStartReset_Type()
)
npRelayStartReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npRelayStartReset.setStatus("current")
_NpRelayMemo_Type = DisplayString
_NpRelayMemo_Object = MibTableColumn
npRelayMemo = _NpRelayMemo_Object(
    (1, 3, 6, 1, 4, 1, 25728, 5500, 5, 1, 6),
    _NpRelayMemo_Type()
)
npRelayMemo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npRelayMemo.setStatus("current")


class _NpRelayState_Type(Integer32):
    """Custom type npRelayState based on Integer32"""
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


_NpRelayState_Type.__name__ = "Integer32"
_NpRelayState_Object = MibTableColumn
npRelayState = _NpRelayState_Object(
    (1, 3, 6, 1, 4, 1, 25728, 5500, 5, 1, 15),
    _NpRelayState_Type()
)
npRelayState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npRelayState.setStatus("current")
_NpIr_ObjectIdentity = ObjectIdentity
npIr = _NpIr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 7900)
)
_NpIrCtrl_ObjectIdentity = ObjectIdentity
npIrCtrl = _NpIrCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 7900, 1)
)


class _NpIrPlayCmd_Type(Integer32):
    """Custom type npIrPlayCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_NpIrPlayCmd_Type.__name__ = "Integer32"
_NpIrPlayCmd_Object = MibScalar
npIrPlayCmd = _NpIrPlayCmd_Object(
    (1, 3, 6, 1, 4, 1, 25728, 7900, 1, 1),
    _NpIrPlayCmd_Type()
)
npIrPlayCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npIrPlayCmd.setStatus("current")


class _NpIrReset_Type(Integer32):
    """Custom type npIrReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_NpIrReset_Type.__name__ = "Integer32"
_NpIrReset_Object = MibScalar
npIrReset = _NpIrReset_Object(
    (1, 3, 6, 1, 4, 1, 25728, 7900, 1, 2),
    _NpIrReset_Type()
)
npIrReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npIrReset.setStatus("current")


class _NpIrStatus_Type(Integer32):
    """Custom type npIrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              16,
              17,
              18,
              19,
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("commandAccepted", 2),
          ("commandCompleted", 0),
          ("errorBadNumber", 17),
          ("errorEmptyRecord", 18),
          ("errorExtBusBusy", 21),
          ("errorFlashChip", 19),
          ("errorTimeout", 20),
          ("errorUnknown", 16),
          ("protocolError", 1))
    )


_NpIrStatus_Type.__name__ = "Integer32"
_NpIrStatus_Object = MibScalar
npIrStatus = _NpIrStatus_Object(
    (1, 3, 6, 1, 4, 1, 25728, 7900, 1, 3),
    _NpIrStatus_Type()
)
npIrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npIrStatus.setStatus("current")
_NpCurLoop_ObjectIdentity = ObjectIdentity
npCurLoop = _NpCurLoop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 8300)
)
_NpCurLoopTable_Object = MibTable
npCurLoopTable = _NpCurLoopTable_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8300, 1)
)
if mibBuilder.loadTexts:
    npCurLoopTable.setStatus("current")
_NpCurLoopEntry_Object = MibTableRow
npCurLoopEntry = _NpCurLoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8300, 1, 1)
)
npCurLoopEntry.setIndexNames(
    (0, "DKSF-70-4-X-X-1", "npCurLoopN"),
)
if mibBuilder.loadTexts:
    npCurLoopEntry.setStatus("current")


class _NpCurLoopN_Type(Integer32):
    """Custom type npCurLoopN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_NpCurLoopN_Type.__name__ = "Integer32"
_NpCurLoopN_Object = MibTableColumn
npCurLoopN = _NpCurLoopN_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8300, 1, 1, 1),
    _NpCurLoopN_Type()
)
npCurLoopN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npCurLoopN.setStatus("current")


class _NpCurLoopStatus_Type(Integer32):
    """Custom type npCurLoopStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("alert", 1),
          ("cut", 2),
          ("notPowered", 4),
          ("ok", 0),
          ("short", 3))
    )


_NpCurLoopStatus_Type.__name__ = "Integer32"
_NpCurLoopStatus_Object = MibTableColumn
npCurLoopStatus = _NpCurLoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8300, 1, 1, 2),
    _NpCurLoopStatus_Type()
)
npCurLoopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npCurLoopStatus.setStatus("current")


class _NpCurLoopI_Type(Integer32):
    """Custom type npCurLoopI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_NpCurLoopI_Type.__name__ = "Integer32"
_NpCurLoopI_Object = MibTableColumn
npCurLoopI = _NpCurLoopI_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8300, 1, 1, 3),
    _NpCurLoopI_Type()
)
npCurLoopI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npCurLoopI.setStatus("current")


class _NpCurLoopV_Type(Integer32):
    """Custom type npCurLoopV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_NpCurLoopV_Type.__name__ = "Integer32"
_NpCurLoopV_Object = MibTableColumn
npCurLoopV = _NpCurLoopV_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8300, 1, 1, 4),
    _NpCurLoopV_Type()
)
npCurLoopV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npCurLoopV.setStatus("current")


class _NpCurLoopR_Type(Integer32):
    """Custom type npCurLoopR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_NpCurLoopR_Type.__name__ = "Integer32"
_NpCurLoopR_Object = MibTableColumn
npCurLoopR = _NpCurLoopR_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8300, 1, 1, 5),
    _NpCurLoopR_Type()
)
npCurLoopR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npCurLoopR.setStatus("current")


class _NpCurLoopPower_Type(Integer32):
    """Custom type npCurLoopPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cyclePower", 2),
          ("off", 0),
          ("on", 1))
    )


_NpCurLoopPower_Type.__name__ = "Integer32"
_NpCurLoopPower_Object = MibTableColumn
npCurLoopPower = _NpCurLoopPower_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8300, 1, 1, 7),
    _NpCurLoopPower_Type()
)
npCurLoopPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npCurLoopPower.setStatus("current")
_NpCurLoopTraps_ObjectIdentity = ObjectIdentity
npCurLoopTraps = _NpCurLoopTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 8300, 2)
)
_NpCurLoopTrapPrefix_ObjectIdentity = ObjectIdentity
npCurLoopTrapPrefix = _NpCurLoopTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 8300, 2, 0)
)


class _NpCurLoopTrapN_Type(Integer32):
    """Custom type npCurLoopTrapN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_NpCurLoopTrapN_Type.__name__ = "Integer32"
_NpCurLoopTrapN_Object = MibScalar
npCurLoopTrapN = _NpCurLoopTrapN_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8300, 2, 1),
    _NpCurLoopTrapN_Type()
)
npCurLoopTrapN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npCurLoopTrapN.setStatus("current")


class _NpCurLoopTrapStatus_Type(Integer32):
    """Custom type npCurLoopTrapStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("alert", 1),
          ("cut", 2),
          ("notPowered", 4),
          ("ok", 0),
          ("short", 3))
    )


_NpCurLoopTrapStatus_Type.__name__ = "Integer32"
_NpCurLoopTrapStatus_Object = MibScalar
npCurLoopTrapStatus = _NpCurLoopTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8300, 2, 2),
    _NpCurLoopTrapStatus_Type()
)
npCurLoopTrapStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npCurLoopTrapStatus.setStatus("current")


class _NpCurLoopTrapI_Type(Integer32):
    """Custom type npCurLoopTrapI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_NpCurLoopTrapI_Type.__name__ = "Integer32"
_NpCurLoopTrapI_Object = MibScalar
npCurLoopTrapI = _NpCurLoopTrapI_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8300, 2, 3),
    _NpCurLoopTrapI_Type()
)
npCurLoopTrapI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npCurLoopTrapI.setStatus("current")


class _NpCurLoopTrapV_Type(Integer32):
    """Custom type npCurLoopTrapV based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_NpCurLoopTrapV_Type.__name__ = "Integer32"
_NpCurLoopTrapV_Object = MibScalar
npCurLoopTrapV = _NpCurLoopTrapV_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8300, 2, 4),
    _NpCurLoopTrapV_Type()
)
npCurLoopTrapV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npCurLoopTrapV.setStatus("current")


class _NpCurLoopTrapR_Type(Integer32):
    """Custom type npCurLoopTrapR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_NpCurLoopTrapR_Type.__name__ = "Integer32"
_NpCurLoopTrapR_Object = MibScalar
npCurLoopTrapR = _NpCurLoopTrapR_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8300, 2, 5),
    _NpCurLoopTrapR_Type()
)
npCurLoopTrapR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npCurLoopTrapR.setStatus("current")


class _NpCurLoopTrapPower_Type(Integer32):
    """Custom type npCurLoopTrapPower based on Integer32"""
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


_NpCurLoopTrapPower_Type.__name__ = "Integer32"
_NpCurLoopTrapPower_Object = MibScalar
npCurLoopTrapPower = _NpCurLoopTrapPower_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8300, 2, 7),
    _NpCurLoopTrapPower_Type()
)
npCurLoopTrapPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npCurLoopTrapPower.setStatus("current")
_NpRelHumidity_ObjectIdentity = ObjectIdentity
npRelHumidity = _NpRelHumidity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 8400)
)
_NpRelHumSensor_ObjectIdentity = ObjectIdentity
npRelHumSensor = _NpRelHumSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 2)
)


class _NpRelHumSensorValueH_Type(Integer32):
    """Custom type npRelHumSensorValueH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_NpRelHumSensorValueH_Type.__name__ = "Integer32"
_NpRelHumSensorValueH_Object = MibScalar
npRelHumSensorValueH = _NpRelHumSensorValueH_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 2, 2),
    _NpRelHumSensorValueH_Type()
)
npRelHumSensorValueH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npRelHumSensorValueH.setStatus("current")


class _NpRelHumSensorStatus_Type(Integer32):
    """Custom type npRelHumSensorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("ok", 1))
    )


_NpRelHumSensorStatus_Type.__name__ = "Integer32"
_NpRelHumSensorStatus_Object = MibScalar
npRelHumSensorStatus = _NpRelHumSensorStatus_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 2, 3),
    _NpRelHumSensorStatus_Type()
)
npRelHumSensorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npRelHumSensorStatus.setStatus("current")


class _NpRelHumSensorValueT_Type(Integer32):
    """Custom type npRelHumSensorValueT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-60, 200),
    )


_NpRelHumSensorValueT_Type.__name__ = "Integer32"
_NpRelHumSensorValueT_Object = MibScalar
npRelHumSensorValueT = _NpRelHumSensorValueT_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 2, 4),
    _NpRelHumSensorValueT_Type()
)
npRelHumSensorValueT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npRelHumSensorValueT.setStatus("current")


class _NpRelHumSensorStatusH_Type(Integer32):
    """Custom type npRelHumSensorStatusH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aboveSafeRange", 3),
          ("belowSafeRange", 1),
          ("inSafeRange", 2),
          ("sensorFailed", 0))
    )


_NpRelHumSensorStatusH_Type.__name__ = "Integer32"
_NpRelHumSensorStatusH_Object = MibScalar
npRelHumSensorStatusH = _NpRelHumSensorStatusH_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 2, 5),
    _NpRelHumSensorStatusH_Type()
)
npRelHumSensorStatusH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npRelHumSensorStatusH.setStatus("current")


class _NpRelHumSafeRangeHigh_Type(Integer32):
    """Custom type npRelHumSafeRangeHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_NpRelHumSafeRangeHigh_Type.__name__ = "Integer32"
_NpRelHumSafeRangeHigh_Object = MibScalar
npRelHumSafeRangeHigh = _NpRelHumSafeRangeHigh_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 2, 7),
    _NpRelHumSafeRangeHigh_Type()
)
npRelHumSafeRangeHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npRelHumSafeRangeHigh.setStatus("current")


class _NpRelHumSafeRangeLow_Type(Integer32):
    """Custom type npRelHumSafeRangeLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_NpRelHumSafeRangeLow_Type.__name__ = "Integer32"
_NpRelHumSafeRangeLow_Object = MibScalar
npRelHumSafeRangeLow = _NpRelHumSafeRangeLow_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 2, 8),
    _NpRelHumSafeRangeLow_Type()
)
npRelHumSafeRangeLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npRelHumSafeRangeLow.setStatus("current")
_NpRelHumSensorValueT100_Type = Integer32
_NpRelHumSensorValueT100_Object = MibScalar
npRelHumSensorValueT100 = _NpRelHumSensorValueT100_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 2, 9),
    _NpRelHumSensorValueT100_Type()
)
npRelHumSensorValueT100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npRelHumSensorValueT100.setStatus("current")
_NpRelHumTraps_ObjectIdentity = ObjectIdentity
npRelHumTraps = _NpRelHumTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 9)
)
_NpRelHumTrapPrefix_ObjectIdentity = ObjectIdentity
npRelHumTrapPrefix = _NpRelHumTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 9, 0)
)
_NpThermo_ObjectIdentity = ObjectIdentity
npThermo = _NpThermo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 8800)
)
_NpThermoTable_Object = MibTable
npThermoTable = _NpThermoTable_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8800, 1)
)
if mibBuilder.loadTexts:
    npThermoTable.setStatus("current")
_NpThermoEntry_Object = MibTableRow
npThermoEntry = _NpThermoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8800, 1, 1)
)
npThermoEntry.setIndexNames(
    (0, "DKSF-70-4-X-X-1", "npThermoSensorN"),
)
if mibBuilder.loadTexts:
    npThermoEntry.setStatus("current")


class _NpThermoSensorN_Type(Integer32):
    """Custom type npThermoSensorN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_NpThermoSensorN_Type.__name__ = "Integer32"
_NpThermoSensorN_Object = MibTableColumn
npThermoSensorN = _NpThermoSensorN_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8800, 1, 1, 1),
    _NpThermoSensorN_Type()
)
npThermoSensorN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npThermoSensorN.setStatus("current")


class _NpThermoValue_Type(Integer32):
    """Custom type npThermoValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-60, 280),
    )


_NpThermoValue_Type.__name__ = "Integer32"
_NpThermoValue_Object = MibTableColumn
npThermoValue = _NpThermoValue_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8800, 1, 1, 2),
    _NpThermoValue_Type()
)
npThermoValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npThermoValue.setStatus("current")


class _NpThermoStatus_Type(Integer32):
    """Custom type npThermoStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failed", 0),
          ("high", 3),
          ("low", 1),
          ("norm", 2))
    )


_NpThermoStatus_Type.__name__ = "Integer32"
_NpThermoStatus_Object = MibTableColumn
npThermoStatus = _NpThermoStatus_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8800, 1, 1, 3),
    _NpThermoStatus_Type()
)
npThermoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npThermoStatus.setStatus("current")


class _NpThermoLow_Type(Integer32):
    """Custom type npThermoLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-60, 280),
    )


_NpThermoLow_Type.__name__ = "Integer32"
_NpThermoLow_Object = MibTableColumn
npThermoLow = _NpThermoLow_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8800, 1, 1, 4),
    _NpThermoLow_Type()
)
npThermoLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npThermoLow.setStatus("current")


class _NpThermoHigh_Type(Integer32):
    """Custom type npThermoHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-60, 280),
    )


_NpThermoHigh_Type.__name__ = "Integer32"
_NpThermoHigh_Object = MibTableColumn
npThermoHigh = _NpThermoHigh_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8800, 1, 1, 5),
    _NpThermoHigh_Type()
)
npThermoHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npThermoHigh.setStatus("current")
_NpThermoMemo_Type = DisplayString
_NpThermoMemo_Object = MibTableColumn
npThermoMemo = _NpThermoMemo_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8800, 1, 1, 6),
    _NpThermoMemo_Type()
)
npThermoMemo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npThermoMemo.setStatus("current")
_NpThermoTraps_ObjectIdentity = ObjectIdentity
npThermoTraps = _NpThermoTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 8800, 2)
)
_NpThermoTrapPrefix_ObjectIdentity = ObjectIdentity
npThermoTrapPrefix = _NpThermoTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 8800, 2, 0)
)


class _NpThermoTrapSensorN_Type(Integer32):
    """Custom type npThermoTrapSensorN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_NpThermoTrapSensorN_Type.__name__ = "Integer32"
_NpThermoTrapSensorN_Object = MibScalar
npThermoTrapSensorN = _NpThermoTrapSensorN_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8800, 2, 1),
    _NpThermoTrapSensorN_Type()
)
npThermoTrapSensorN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npThermoTrapSensorN.setStatus("current")


class _NpThermoTrapValue_Type(Integer32):
    """Custom type npThermoTrapValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-60, 280),
    )


_NpThermoTrapValue_Type.__name__ = "Integer32"
_NpThermoTrapValue_Object = MibScalar
npThermoTrapValue = _NpThermoTrapValue_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8800, 2, 2),
    _NpThermoTrapValue_Type()
)
npThermoTrapValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npThermoTrapValue.setStatus("current")


class _NpThermoTrapStatus_Type(Integer32):
    """Custom type npThermoTrapStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failed", 0),
          ("high", 3),
          ("low", 1),
          ("norm", 2))
    )


_NpThermoTrapStatus_Type.__name__ = "Integer32"
_NpThermoTrapStatus_Object = MibScalar
npThermoTrapStatus = _NpThermoTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8800, 2, 3),
    _NpThermoTrapStatus_Type()
)
npThermoTrapStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npThermoTrapStatus.setStatus("current")


class _NpThermoTrapLow_Type(Integer32):
    """Custom type npThermoTrapLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-60, 280),
    )


_NpThermoTrapLow_Type.__name__ = "Integer32"
_NpThermoTrapLow_Object = MibScalar
npThermoTrapLow = _NpThermoTrapLow_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8800, 2, 4),
    _NpThermoTrapLow_Type()
)
npThermoTrapLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npThermoTrapLow.setStatus("current")


class _NpThermoTrapHigh_Type(Integer32):
    """Custom type npThermoTrapHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-60, 280),
    )


_NpThermoTrapHigh_Type.__name__ = "Integer32"
_NpThermoTrapHigh_Object = MibScalar
npThermoTrapHigh = _NpThermoTrapHigh_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8800, 2, 5),
    _NpThermoTrapHigh_Type()
)
npThermoTrapHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npThermoTrapHigh.setStatus("current")
_NpThermoTrapMemo_Type = DisplayString
_NpThermoTrapMemo_Object = MibScalar
npThermoTrapMemo = _NpThermoTrapMemo_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8800, 2, 6),
    _NpThermoTrapMemo_Type()
)
npThermoTrapMemo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npThermoTrapMemo.setStatus("current")
_NpIo_ObjectIdentity = ObjectIdentity
npIo = _NpIo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 8900)
)
_NpIoTable_Object = MibTable
npIoTable = _NpIoTable_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8900, 1)
)
if mibBuilder.loadTexts:
    npIoTable.setStatus("current")
_NpIoEntry_Object = MibTableRow
npIoEntry = _NpIoEntry_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8900, 1, 1)
)
npIoEntry.setIndexNames(
    (0, "DKSF-70-4-X-X-1", "npIoLineN"),
)
if mibBuilder.loadTexts:
    npIoEntry.setStatus("current")


class _NpIoLineN_Type(Integer32):
    """Custom type npIoLineN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_NpIoLineN_Type.__name__ = "Integer32"
_NpIoLineN_Object = MibTableColumn
npIoLineN = _NpIoLineN_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8900, 1, 1, 1),
    _NpIoLineN_Type()
)
npIoLineN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npIoLineN.setStatus("current")


class _NpIoLevelIn_Type(Integer32):
    """Custom type npIoLevelIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_NpIoLevelIn_Type.__name__ = "Integer32"
_NpIoLevelIn_Object = MibTableColumn
npIoLevelIn = _NpIoLevelIn_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8900, 1, 1, 2),
    _NpIoLevelIn_Type()
)
npIoLevelIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npIoLevelIn.setStatus("current")


class _NpIoLevelOut_Type(Integer32):
    """Custom type npIoLevelOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("flip", -1),
          ("high", 1),
          ("low", 0))
    )


_NpIoLevelOut_Type.__name__ = "Integer32"
_NpIoLevelOut_Object = MibTableColumn
npIoLevelOut = _NpIoLevelOut_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8900, 1, 1, 3),
    _NpIoLevelOut_Type()
)
npIoLevelOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npIoLevelOut.setStatus("current")
_NpIoMemo_Type = DisplayString
_NpIoMemo_Object = MibTableColumn
npIoMemo = _NpIoMemo_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8900, 1, 1, 6),
    _NpIoMemo_Type()
)
npIoMemo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npIoMemo.setStatus("current")
_NpIoPulseCounter_Type = Counter32
_NpIoPulseCounter_Object = MibTableColumn
npIoPulseCounter = _NpIoPulseCounter_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8900, 1, 1, 9),
    _NpIoPulseCounter_Type()
)
npIoPulseCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npIoPulseCounter.setStatus("current")


class _NpIoSinglePulseDuration_Type(Integer32):
    """Custom type npIoSinglePulseDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 25500),
    )


_NpIoSinglePulseDuration_Type.__name__ = "Integer32"
_NpIoSinglePulseDuration_Object = MibTableColumn
npIoSinglePulseDuration = _NpIoSinglePulseDuration_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8900, 1, 1, 12),
    _NpIoSinglePulseDuration_Type()
)
npIoSinglePulseDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npIoSinglePulseDuration.setStatus("current")
_NpIoSinglePulseStart_Type = Integer32
_NpIoSinglePulseStart_Object = MibTableColumn
npIoSinglePulseStart = _NpIoSinglePulseStart_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8900, 1, 1, 13),
    _NpIoSinglePulseStart_Type()
)
npIoSinglePulseStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    npIoSinglePulseStart.setStatus("current")
_NpIoTraps_ObjectIdentity = ObjectIdentity
npIoTraps = _NpIoTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 8900, 2)
)
_NpIoTrapPrefix_ObjectIdentity = ObjectIdentity
npIoTrapPrefix = _NpIoTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25728, 8900, 2, 0)
)


class _NpIoTrapLineN_Type(Integer32):
    """Custom type npIoTrapLineN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_NpIoTrapLineN_Type.__name__ = "Integer32"
_NpIoTrapLineN_Object = MibScalar
npIoTrapLineN = _NpIoTrapLineN_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8900, 2, 1),
    _NpIoTrapLineN_Type()
)
npIoTrapLineN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npIoTrapLineN.setStatus("current")


class _NpIoTrapLevelIn_Type(Integer32):
    """Custom type npIoTrapLevelIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_NpIoTrapLevelIn_Type.__name__ = "Integer32"
_NpIoTrapLevelIn_Object = MibScalar
npIoTrapLevelIn = _NpIoTrapLevelIn_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8900, 2, 2),
    _NpIoTrapLevelIn_Type()
)
npIoTrapLevelIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npIoTrapLevelIn.setStatus("current")
_NpIoTrapMemo_Type = DisplayString
_NpIoTrapMemo_Object = MibScalar
npIoTrapMemo = _NpIoTrapMemo_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8900, 2, 6),
    _NpIoTrapMemo_Type()
)
npIoTrapMemo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npIoTrapMemo.setStatus("current")
_NpIoTrapLevelLegend_Type = DisplayString
_NpIoTrapLevelLegend_Object = MibScalar
npIoTrapLevelLegend = _NpIoTrapLevelLegend_Object(
    (1, 3, 6, 1, 4, 1, 25728, 8900, 2, 7),
    _NpIoTrapLevelLegend_Type()
)
npIoTrapLevelLegend.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    npIoTrapLevelLegend.setStatus("current")

# Managed Objects groups


# Notification objects

npGsmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25728, 3800, 2, 0, 1)
)
npGsmTrap.setObjects(
      *(("DKSF-70-4-X-X-1", "npGsmFailed"),
        ("DKSF-70-4-X-X-1", "npGsmRegistration"),
        ("DKSF-70-4-X-X-1", "npGsmStrength"))
)
if mibBuilder.loadTexts:
    npGsmTrap.setStatus(
        "current"
    )

npCurLoopTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25728, 8300, 2, 0, 1)
)
npCurLoopTrap.setObjects(
      *(("DKSF-70-4-X-X-1", "npCurLoopTrapN"),
        ("DKSF-70-4-X-X-1", "npCurLoopTrapStatus"),
        ("DKSF-70-4-X-X-1", "npCurLoopTrapI"),
        ("DKSF-70-4-X-X-1", "npCurLoopTrapV"),
        ("DKSF-70-4-X-X-1", "npCurLoopTrapR"),
        ("DKSF-70-4-X-X-1", "npCurLoopTrapPower"),
        ("DKSF-70-4-X-X-1", "npTrapEmailTo"))
)
if mibBuilder.loadTexts:
    npCurLoopTrap.setStatus(
        "current"
    )

npRelHumTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25728, 8400, 9, 0, 1)
)
npRelHumTrap.setObjects(
      *(("DKSF-70-4-X-X-1", "npRelHumSensorStatusH"),
        ("DKSF-70-4-X-X-1", "npRelHumSensorValueH"),
        ("DKSF-70-4-X-X-1", "npRelHumSafeRangeHigh"),
        ("DKSF-70-4-X-X-1", "npRelHumSafeRangeLow"),
        ("DKSF-70-4-X-X-1", "npTrapEmailTo"))
)
if mibBuilder.loadTexts:
    npRelHumTrap.setStatus(
        "current"
    )

npThermoTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25728, 8800, 2, 0, 1)
)
npThermoTrap.setObjects(
      *(("DKSF-70-4-X-X-1", "npThermoTrapSensorN"),
        ("DKSF-70-4-X-X-1", "npThermoTrapValue"),
        ("DKSF-70-4-X-X-1", "npThermoTrapStatus"),
        ("DKSF-70-4-X-X-1", "npThermoTrapLow"),
        ("DKSF-70-4-X-X-1", "npThermoTrapHigh"),
        ("DKSF-70-4-X-X-1", "npThermoTrapMemo"))
)
if mibBuilder.loadTexts:
    npThermoTrap.setStatus(
        "current"
    )

npIoTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25728, 8900, 2, 0, 1)
)
npIoTrap.setObjects(
      *(("DKSF-70-4-X-X-1", "npIoTrapLineN"),
        ("DKSF-70-4-X-X-1", "npIoTrapLevelIn"),
        ("DKSF-70-4-X-X-1", "npIoTrapMemo"),
        ("DKSF-70-4-X-X-1", "npIoTrapLevelLegend"))
)
if mibBuilder.loadTexts:
    npIoTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DKSF-70-4-X-X-1",
    **{"lightcom": lightcom,
       "uniPingServerSolutionV3": uniPingServerSolutionV3,
       "npTrapInfo": npTrapInfo,
       "npTrapEmailTo": npTrapEmailTo,
       "npReboot": npReboot,
       "npSoftReboot": npSoftReboot,
       "npResetStack": npResetStack,
       "npForcedReboot": npForcedReboot,
       "npGsm": npGsm,
       "npGsmInfo": npGsmInfo,
       "npGsmFailed": npGsmFailed,
       "npGsmRegistration": npGsmRegistration,
       "npGsmStrength": npGsmStrength,
       "npGsmSendSms": npGsmSendSms,
       "npGsmTraps": npGsmTraps,
       "npGsmTrapPrefix": npGsmTrapPrefix,
       "npGsmTrap": npGsmTrap,
       "npRelay": npRelay,
       "npRelayTable": npRelayTable,
       "npRelayEntry": npRelayEntry,
       "npRelayN": npRelayN,
       "npRelayMode": npRelayMode,
       "npRelayStartReset": npRelayStartReset,
       "npRelayMemo": npRelayMemo,
       "npRelayState": npRelayState,
       "npIr": npIr,
       "npIrCtrl": npIrCtrl,
       "npIrPlayCmd": npIrPlayCmd,
       "npIrReset": npIrReset,
       "npIrStatus": npIrStatus,
       "npCurLoop": npCurLoop,
       "npCurLoopTable": npCurLoopTable,
       "npCurLoopEntry": npCurLoopEntry,
       "npCurLoopN": npCurLoopN,
       "npCurLoopStatus": npCurLoopStatus,
       "npCurLoopI": npCurLoopI,
       "npCurLoopV": npCurLoopV,
       "npCurLoopR": npCurLoopR,
       "npCurLoopPower": npCurLoopPower,
       "npCurLoopTraps": npCurLoopTraps,
       "npCurLoopTrapPrefix": npCurLoopTrapPrefix,
       "npCurLoopTrap": npCurLoopTrap,
       "npCurLoopTrapN": npCurLoopTrapN,
       "npCurLoopTrapStatus": npCurLoopTrapStatus,
       "npCurLoopTrapI": npCurLoopTrapI,
       "npCurLoopTrapV": npCurLoopTrapV,
       "npCurLoopTrapR": npCurLoopTrapR,
       "npCurLoopTrapPower": npCurLoopTrapPower,
       "npRelHumidity": npRelHumidity,
       "npRelHumSensor": npRelHumSensor,
       "npRelHumSensorValueH": npRelHumSensorValueH,
       "npRelHumSensorStatus": npRelHumSensorStatus,
       "npRelHumSensorValueT": npRelHumSensorValueT,
       "npRelHumSensorStatusH": npRelHumSensorStatusH,
       "npRelHumSafeRangeHigh": npRelHumSafeRangeHigh,
       "npRelHumSafeRangeLow": npRelHumSafeRangeLow,
       "npRelHumSensorValueT100": npRelHumSensorValueT100,
       "npRelHumTraps": npRelHumTraps,
       "npRelHumTrapPrefix": npRelHumTrapPrefix,
       "npRelHumTrap": npRelHumTrap,
       "npThermo": npThermo,
       "npThermoTable": npThermoTable,
       "npThermoEntry": npThermoEntry,
       "npThermoSensorN": npThermoSensorN,
       "npThermoValue": npThermoValue,
       "npThermoStatus": npThermoStatus,
       "npThermoLow": npThermoLow,
       "npThermoHigh": npThermoHigh,
       "npThermoMemo": npThermoMemo,
       "npThermoTraps": npThermoTraps,
       "npThermoTrapPrefix": npThermoTrapPrefix,
       "npThermoTrap": npThermoTrap,
       "npThermoTrapSensorN": npThermoTrapSensorN,
       "npThermoTrapValue": npThermoTrapValue,
       "npThermoTrapStatus": npThermoTrapStatus,
       "npThermoTrapLow": npThermoTrapLow,
       "npThermoTrapHigh": npThermoTrapHigh,
       "npThermoTrapMemo": npThermoTrapMemo,
       "npIo": npIo,
       "npIoTable": npIoTable,
       "npIoEntry": npIoEntry,
       "npIoLineN": npIoLineN,
       "npIoLevelIn": npIoLevelIn,
       "npIoLevelOut": npIoLevelOut,
       "npIoMemo": npIoMemo,
       "npIoPulseCounter": npIoPulseCounter,
       "npIoSinglePulseDuration": npIoSinglePulseDuration,
       "npIoSinglePulseStart": npIoSinglePulseStart,
       "npIoTraps": npIoTraps,
       "npIoTrapPrefix": npIoTrapPrefix,
       "npIoTrap": npIoTrap,
       "npIoTrapLineN": npIoTrapLineN,
       "npIoTrapLevelIn": npIoTrapLevelIn,
       "npIoTrapMemo": npIoTrapMemo,
       "npIoTrapLevelLegend": npIoTrapLevelLegend}
)
