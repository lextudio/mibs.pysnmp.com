# SNMP MIB module (ZHONE-COM-VOICE-SIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZHONE-COM-VOICE-SIG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:20:24 2024
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

(DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")

(zhoneVoice,) = mibBuilder.importSymbols(
    "Zhone",
    "zhoneVoice")


# MODULE-IDENTITY

zhoneVoiceSignalingMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 7)
)
zhoneVoiceSignalingMib.setRevisions(
        ("2004-10-21 14:51",
         "2000-10-10 18:05")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZhoneVoiceSignalingTimers_ObjectIdentity = ObjectIdentity
zhoneVoiceSignalingTimers = _ZhoneVoiceSignalingTimers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 7, 1)
)
if mibBuilder.loadTexts:
    zhoneVoiceSignalingTimers.setStatus("current")


class _HookFlashTimerMin_Type(Integer32):
    """Custom type hookFlashTimerMin based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HookFlashTimerMin_Type.__name__ = "Integer32"
_HookFlashTimerMin_Object = MibScalar
hookFlashTimerMin = _HookFlashTimerMin_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 7, 1, 1),
    _HookFlashTimerMin_Type()
)
hookFlashTimerMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hookFlashTimerMin.setStatus("current")


class _HookFlashTimerMax_Type(Integer32):
    """Custom type hookFlashTimerMax based on Integer32"""
    defaultValue = 1550

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HookFlashTimerMax_Type.__name__ = "Integer32"
_HookFlashTimerMax_Object = MibScalar
hookFlashTimerMax = _HookFlashTimerMax_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 7, 1, 2),
    _HookFlashTimerMax_Type()
)
hookFlashTimerMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hookFlashTimerMax.setStatus("current")


class _SysPartialDialTo_Type(Unsigned32):
    """Custom type sysPartialDialTo based on Unsigned32"""
    defaultValue = 16


_SysPartialDialTo_Object = MibScalar
sysPartialDialTo = _SysPartialDialTo_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 7, 1, 3),
    _SysPartialDialTo_Type()
)
sysPartialDialTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysPartialDialTo.setStatus("current")
if mibBuilder.loadTexts:
    sysPartialDialTo.setUnits("seconds")


class _SysCriticalDialTo_Type(Unsigned32):
    """Custom type sysCriticalDialTo based on Unsigned32"""
    defaultValue = 4


_SysCriticalDialTo_Object = MibScalar
sysCriticalDialTo = _SysCriticalDialTo_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 7, 1, 4),
    _SysCriticalDialTo_Type()
)
sysCriticalDialTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysCriticalDialTo.setStatus("current")
if mibBuilder.loadTexts:
    sysCriticalDialTo.setUnits("seconds")


class _SysBusyToneTo_Type(Unsigned32):
    """Custom type sysBusyToneTo based on Unsigned32"""
    defaultValue = 30


_SysBusyToneTo_Object = MibScalar
sysBusyToneTo = _SysBusyToneTo_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 7, 1, 5),
    _SysBusyToneTo_Type()
)
sysBusyToneTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysBusyToneTo.setStatus("current")
if mibBuilder.loadTexts:
    sysBusyToneTo.setUnits("seconds")


class _SysDialToneTo_Type(Unsigned32):
    """Custom type sysDialToneTo based on Unsigned32"""
    defaultValue = 16


_SysDialToneTo_Object = MibScalar
sysDialToneTo = _SysDialToneTo_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 7, 1, 6),
    _SysDialToneTo_Type()
)
sysDialToneTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDialToneTo.setStatus("current")
if mibBuilder.loadTexts:
    sysDialToneTo.setUnits("seconds")


class _SysMsgWaitToneTo_Type(Unsigned32):
    """Custom type sysMsgWaitToneTo based on Unsigned32"""
    defaultValue = 16


_SysMsgWaitToneTo_Object = MibScalar
sysMsgWaitToneTo = _SysMsgWaitToneTo_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 7, 1, 7),
    _SysMsgWaitToneTo_Type()
)
sysMsgWaitToneTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMsgWaitToneTo.setStatus("current")
if mibBuilder.loadTexts:
    sysMsgWaitToneTo.setUnits("seconds")


class _SysOffhookWarnToneTo_Type(Unsigned32):
    """Custom type sysOffhookWarnToneTo based on Unsigned32"""
    defaultValue = 0


_SysOffhookWarnToneTo_Object = MibScalar
sysOffhookWarnToneTo = _SysOffhookWarnToneTo_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 7, 1, 8),
    _SysOffhookWarnToneTo_Type()
)
sysOffhookWarnToneTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysOffhookWarnToneTo.setStatus("current")
if mibBuilder.loadTexts:
    sysOffhookWarnToneTo.setUnits("seconds")


class _SysRingingTo_Type(Unsigned32):
    """Custom type sysRingingTo based on Unsigned32"""
    defaultValue = 180


_SysRingingTo_Object = MibScalar
sysRingingTo = _SysRingingTo_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 7, 1, 9),
    _SysRingingTo_Type()
)
sysRingingTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysRingingTo.setStatus("current")
if mibBuilder.loadTexts:
    sysRingingTo.setUnits("seconds")


class _SysRingbackTo_Type(Unsigned32):
    """Custom type sysRingbackTo based on Unsigned32"""
    defaultValue = 180


_SysRingbackTo_Object = MibScalar
sysRingbackTo = _SysRingbackTo_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 7, 1, 10),
    _SysRingbackTo_Type()
)
sysRingbackTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysRingbackTo.setStatus("current")
if mibBuilder.loadTexts:
    sysRingbackTo.setUnits("seconds")


class _SysReorderToneTo_Type(Unsigned32):
    """Custom type sysReorderToneTo based on Unsigned32"""
    defaultValue = 30


_SysReorderToneTo_Object = MibScalar
sysReorderToneTo = _SysReorderToneTo_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 7, 1, 11),
    _SysReorderToneTo_Type()
)
sysReorderToneTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysReorderToneTo.setStatus("current")
if mibBuilder.loadTexts:
    sysReorderToneTo.setUnits("seconds")


class _SysStutterToneTo_Type(Unsigned32):
    """Custom type sysStutterToneTo based on Unsigned32"""
    defaultValue = 16


_SysStutterToneTo_Object = MibScalar
sysStutterToneTo = _SysStutterToneTo_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 7, 1, 12),
    _SysStutterToneTo_Type()
)
sysStutterToneTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysStutterToneTo.setStatus("current")
if mibBuilder.loadTexts:
    sysStutterToneTo.setUnits("seconds")


class _SysServerMaxTimer_Type(Unsigned32):
    """Custom type sysServerMaxTimer based on Unsigned32"""
    defaultValue = 20


_SysServerMaxTimer_Object = MibScalar
sysServerMaxTimer = _SysServerMaxTimer_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 7, 1, 13),
    _SysServerMaxTimer_Type()
)
sysServerMaxTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysServerMaxTimer.setStatus("current")


class _SysConfigMax1_Type(Unsigned32):
    """Custom type sysConfigMax1 based on Unsigned32"""
    defaultValue = 5


_SysConfigMax1_Object = MibScalar
sysConfigMax1 = _SysConfigMax1_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 7, 1, 14),
    _SysConfigMax1_Type()
)
sysConfigMax1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysConfigMax1.setStatus("current")


class _SysConfigMax2_Type(Unsigned32):
    """Custom type sysConfigMax2 based on Unsigned32"""
    defaultValue = 7


_SysConfigMax2_Object = MibScalar
sysConfigMax2 = _SysConfigMax2_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 7, 1, 15),
    _SysConfigMax2_Type()
)
sysConfigMax2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysConfigMax2.setStatus("current")


class _SysMax1Enable_Type(TruthValue):
    """Custom type sysMax1Enable based on TruthValue"""


_SysMax1Enable_Object = MibScalar
sysMax1Enable = _SysMax1Enable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 7, 1, 16),
    _SysMax1Enable_Type()
)
sysMax1Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMax1Enable.setStatus("current")


class _SysMax2Enable_Type(TruthValue):
    """Custom type sysMax2Enable based on TruthValue"""


_SysMax2Enable_Object = MibScalar
sysMax2Enable = _SysMax2Enable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 7, 1, 17),
    _SysMax2Enable_Type()
)
sysMax2Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMax2Enable.setStatus("current")


class _SysMaxWaitingDelay_Type(Unsigned32):
    """Custom type sysMaxWaitingDelay based on Unsigned32"""
    defaultValue = 600


_SysMaxWaitingDelay_Object = MibScalar
sysMaxWaitingDelay = _SysMaxWaitingDelay_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 7, 1, 18),
    _SysMaxWaitingDelay_Type()
)
sysMaxWaitingDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMaxWaitingDelay.setStatus("current")
if mibBuilder.loadTexts:
    sysMaxWaitingDelay.setUnits("seconds")


class _SysDisconnectWaitTimer_Type(Unsigned32):
    """Custom type sysDisconnectWaitTimer based on Unsigned32"""
    defaultValue = 15


_SysDisconnectWaitTimer_Object = MibScalar
sysDisconnectWaitTimer = _SysDisconnectWaitTimer_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 7, 1, 19),
    _SysDisconnectWaitTimer_Type()
)
sysDisconnectWaitTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDisconnectWaitTimer.setStatus("current")
if mibBuilder.loadTexts:
    sysDisconnectWaitTimer.setUnits("seconds")


class _SysDisconnectMinTimer_Type(Unsigned32):
    """Custom type sysDisconnectMinTimer based on Unsigned32"""
    defaultValue = 15


_SysDisconnectMinTimer_Object = MibScalar
sysDisconnectMinTimer = _SysDisconnectMinTimer_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 7, 1, 20),
    _SysDisconnectMinTimer_Type()
)
sysDisconnectMinTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDisconnectMinTimer.setStatus("current")
if mibBuilder.loadTexts:
    sysDisconnectMinTimer.setUnits("seconds")


class _SysDisconnectMaxTimer_Type(Unsigned32):
    """Custom type sysDisconnectMaxTimer based on Unsigned32"""
    defaultValue = 600


_SysDisconnectMaxTimer_Object = MibScalar
sysDisconnectMaxTimer = _SysDisconnectMaxTimer_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 7, 1, 21),
    _SysDisconnectMaxTimer_Type()
)
sysDisconnectMaxTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDisconnectMaxTimer.setStatus("current")
if mibBuilder.loadTexts:
    sysDisconnectMaxTimer.setUnits("seconds")


class _SysMaxRetransmitTimer_Type(Unsigned32):
    """Custom type sysMaxRetransmitTimer based on Unsigned32"""
    defaultValue = 4


_SysMaxRetransmitTimer_Object = MibScalar
sysMaxRetransmitTimer = _SysMaxRetransmitTimer_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 7, 1, 22),
    _SysMaxRetransmitTimer_Type()
)
sysMaxRetransmitTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMaxRetransmitTimer.setStatus("current")
if mibBuilder.loadTexts:
    sysMaxRetransmitTimer.setUnits("seconds")


class _SysInitRetransmitTimer_Type(Unsigned32):
    """Custom type sysInitRetransmitTimer based on Unsigned32"""
    defaultValue = 200


_SysInitRetransmitTimer_Object = MibScalar
sysInitRetransmitTimer = _SysInitRetransmitTimer_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 7, 1, 23),
    _SysInitRetransmitTimer_Type()
)
sysInitRetransmitTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysInitRetransmitTimer.setStatus("current")
if mibBuilder.loadTexts:
    sysInitRetransmitTimer.setUnits("milliseconds")


class _SysKeepAliveTimer_Type(Unsigned32):
    """Custom type sysKeepAliveTimer based on Unsigned32"""
    defaultValue = 60


_SysKeepAliveTimer_Object = MibScalar
sysKeepAliveTimer = _SysKeepAliveTimer_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 7, 1, 24),
    _SysKeepAliveTimer_Type()
)
sysKeepAliveTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysKeepAliveTimer.setStatus("current")
if mibBuilder.loadTexts:
    sysKeepAliveTimer.setUnits("minutes")


class _SysNoResponseTimer_Type(Unsigned32):
    """Custom type sysNoResponseTimer based on Unsigned32"""
    defaultValue = 30


_SysNoResponseTimer_Object = MibScalar
sysNoResponseTimer = _SysNoResponseTimer_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 7, 1, 25),
    _SysNoResponseTimer_Type()
)
sysNoResponseTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysNoResponseTimer.setStatus("current")
if mibBuilder.loadTexts:
    sysNoResponseTimer.setUnits("seconds")


class _SysCallWaitMaxRepeat_Type(Unsigned32):
    """Custom type sysCallWaitMaxRepeat based on Unsigned32"""
    defaultValue = 2


_SysCallWaitMaxRepeat_Object = MibScalar
sysCallWaitMaxRepeat = _SysCallWaitMaxRepeat_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 7, 1, 26),
    _SysCallWaitMaxRepeat_Type()
)
sysCallWaitMaxRepeat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysCallWaitMaxRepeat.setStatus("current")


class _SysCallWaitDelay_Type(Unsigned32):
    """Custom type sysCallWaitDelay based on Unsigned32"""
    defaultValue = 10


_SysCallWaitDelay_Object = MibScalar
sysCallWaitDelay = _SysCallWaitDelay_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 7, 1, 27),
    _SysCallWaitDelay_Type()
)
sysCallWaitDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysCallWaitDelay.setStatus("current")
if mibBuilder.loadTexts:
    sysCallWaitDelay.setUnits("seconds")


class _SysPulseInterDigitTimer_Type(Unsigned32):
    """Custom type sysPulseInterDigitTimer based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1500),
    )


_SysPulseInterDigitTimer_Type.__name__ = "Unsigned32"
_SysPulseInterDigitTimer_Object = MibScalar
sysPulseInterDigitTimer = _SysPulseInterDigitTimer_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 7, 1, 28),
    _SysPulseInterDigitTimer_Type()
)
sysPulseInterDigitTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysPulseInterDigitTimer.setStatus("current")
if mibBuilder.loadTexts:
    sysPulseInterDigitTimer.setUnits("milliseconds")


class _SysMinMakePulseWidth_Type(Unsigned32):
    """Custom type sysMinMakePulseWidth based on Unsigned32"""
    defaultValue = 25

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 200),
    )


_SysMinMakePulseWidth_Type.__name__ = "Unsigned32"
_SysMinMakePulseWidth_Object = MibScalar
sysMinMakePulseWidth = _SysMinMakePulseWidth_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 7, 1, 29),
    _SysMinMakePulseWidth_Type()
)
sysMinMakePulseWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMinMakePulseWidth.setStatus("current")
if mibBuilder.loadTexts:
    sysMinMakePulseWidth.setUnits("milliseconds")


class _SysMaxMakePulseWidth_Type(Unsigned32):
    """Custom type sysMaxMakePulseWidth based on Unsigned32"""
    defaultValue = 55

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 200),
    )


_SysMaxMakePulseWidth_Type.__name__ = "Unsigned32"
_SysMaxMakePulseWidth_Object = MibScalar
sysMaxMakePulseWidth = _SysMaxMakePulseWidth_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 7, 1, 30),
    _SysMaxMakePulseWidth_Type()
)
sysMaxMakePulseWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMaxMakePulseWidth.setStatus("current")
if mibBuilder.loadTexts:
    sysMaxMakePulseWidth.setUnits("milliseconds")


class _SysMinBreakPulseWidth_Type(Unsigned32):
    """Custom type sysMinBreakPulseWidth based on Unsigned32"""
    defaultValue = 45

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 200),
    )


_SysMinBreakPulseWidth_Type.__name__ = "Unsigned32"
_SysMinBreakPulseWidth_Object = MibScalar
sysMinBreakPulseWidth = _SysMinBreakPulseWidth_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 7, 1, 31),
    _SysMinBreakPulseWidth_Type()
)
sysMinBreakPulseWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMinBreakPulseWidth.setStatus("current")
if mibBuilder.loadTexts:
    sysMinBreakPulseWidth.setUnits("milliseconds")


class _SysMaxBreakPulseWidth_Type(Unsigned32):
    """Custom type sysMaxBreakPulseWidth based on Unsigned32"""
    defaultValue = 75

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 200),
    )


_SysMaxBreakPulseWidth_Type.__name__ = "Unsigned32"
_SysMaxBreakPulseWidth_Object = MibScalar
sysMaxBreakPulseWidth = _SysMaxBreakPulseWidth_Object(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 7, 1, 32),
    _SysMaxBreakPulseWidth_Type()
)
sysMaxBreakPulseWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMaxBreakPulseWidth.setStatus("current")
if mibBuilder.loadTexts:
    sysMaxBreakPulseWidth.setUnits("milliseconds")

# Managed Objects groups

zhoneVoiceSignalingObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 4, 3, 7, 1, 33)
)
zhoneVoiceSignalingObjectsGroup.setObjects(
      *(("ZHONE-COM-VOICE-SIG-MIB", "sysPartialDialTo"),
        ("ZHONE-COM-VOICE-SIG-MIB", "sysCriticalDialTo"),
        ("ZHONE-COM-VOICE-SIG-MIB", "sysBusyToneTo"),
        ("ZHONE-COM-VOICE-SIG-MIB", "sysDialToneTo"),
        ("ZHONE-COM-VOICE-SIG-MIB", "sysMsgWaitToneTo"),
        ("ZHONE-COM-VOICE-SIG-MIB", "sysOffhookWarnToneTo"),
        ("ZHONE-COM-VOICE-SIG-MIB", "sysRingingTo"),
        ("ZHONE-COM-VOICE-SIG-MIB", "sysRingbackTo"),
        ("ZHONE-COM-VOICE-SIG-MIB", "sysReorderToneTo"),
        ("ZHONE-COM-VOICE-SIG-MIB", "sysStutterToneTo"),
        ("ZHONE-COM-VOICE-SIG-MIB", "sysServerMaxTimer"),
        ("ZHONE-COM-VOICE-SIG-MIB", "sysConfigMax1"),
        ("ZHONE-COM-VOICE-SIG-MIB", "sysConfigMax2"),
        ("ZHONE-COM-VOICE-SIG-MIB", "sysMax1Enable"),
        ("ZHONE-COM-VOICE-SIG-MIB", "sysMax2Enable"),
        ("ZHONE-COM-VOICE-SIG-MIB", "sysMaxWaitingDelay"),
        ("ZHONE-COM-VOICE-SIG-MIB", "sysDisconnectWaitTimer"),
        ("ZHONE-COM-VOICE-SIG-MIB", "sysDisconnectMinTimer"),
        ("ZHONE-COM-VOICE-SIG-MIB", "sysDisconnectMaxTimer"),
        ("ZHONE-COM-VOICE-SIG-MIB", "sysMaxRetransmitTimer"),
        ("ZHONE-COM-VOICE-SIG-MIB", "sysInitRetransmitTimer"),
        ("ZHONE-COM-VOICE-SIG-MIB", "sysKeepAliveTimer"),
        ("ZHONE-COM-VOICE-SIG-MIB", "sysNoResponseTimer"),
        ("ZHONE-COM-VOICE-SIG-MIB", "sysCallWaitMaxRepeat"),
        ("ZHONE-COM-VOICE-SIG-MIB", "sysCallWaitDelay"),
        ("ZHONE-COM-VOICE-SIG-MIB", "sysPulseInterDigitTimer"),
        ("ZHONE-COM-VOICE-SIG-MIB", "sysMinMakePulseWidth"),
        ("ZHONE-COM-VOICE-SIG-MIB", "sysMaxMakePulseWidth"),
        ("ZHONE-COM-VOICE-SIG-MIB", "sysMinBreakPulseWidth"),
        ("ZHONE-COM-VOICE-SIG-MIB", "sysMaxBreakPulseWidth"),
        ("ZHONE-COM-VOICE-SIG-MIB", "hookFlashTimerMin"),
        ("ZHONE-COM-VOICE-SIG-MIB", "hookFlashTimerMax"))
)
if mibBuilder.loadTexts:
    zhoneVoiceSignalingObjectsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZHONE-COM-VOICE-SIG-MIB",
    **{"zhoneVoiceSignalingMib": zhoneVoiceSignalingMib,
       "zhoneVoiceSignalingTimers": zhoneVoiceSignalingTimers,
       "hookFlashTimerMin": hookFlashTimerMin,
       "hookFlashTimerMax": hookFlashTimerMax,
       "sysPartialDialTo": sysPartialDialTo,
       "sysCriticalDialTo": sysCriticalDialTo,
       "sysBusyToneTo": sysBusyToneTo,
       "sysDialToneTo": sysDialToneTo,
       "sysMsgWaitToneTo": sysMsgWaitToneTo,
       "sysOffhookWarnToneTo": sysOffhookWarnToneTo,
       "sysRingingTo": sysRingingTo,
       "sysRingbackTo": sysRingbackTo,
       "sysReorderToneTo": sysReorderToneTo,
       "sysStutterToneTo": sysStutterToneTo,
       "sysServerMaxTimer": sysServerMaxTimer,
       "sysConfigMax1": sysConfigMax1,
       "sysConfigMax2": sysConfigMax2,
       "sysMax1Enable": sysMax1Enable,
       "sysMax2Enable": sysMax2Enable,
       "sysMaxWaitingDelay": sysMaxWaitingDelay,
       "sysDisconnectWaitTimer": sysDisconnectWaitTimer,
       "sysDisconnectMinTimer": sysDisconnectMinTimer,
       "sysDisconnectMaxTimer": sysDisconnectMaxTimer,
       "sysMaxRetransmitTimer": sysMaxRetransmitTimer,
       "sysInitRetransmitTimer": sysInitRetransmitTimer,
       "sysKeepAliveTimer": sysKeepAliveTimer,
       "sysNoResponseTimer": sysNoResponseTimer,
       "sysCallWaitMaxRepeat": sysCallWaitMaxRepeat,
       "sysCallWaitDelay": sysCallWaitDelay,
       "sysPulseInterDigitTimer": sysPulseInterDigitTimer,
       "sysMinMakePulseWidth": sysMinMakePulseWidth,
       "sysMaxMakePulseWidth": sysMaxMakePulseWidth,
       "sysMinBreakPulseWidth": sysMinBreakPulseWidth,
       "sysMaxBreakPulseWidth": sysMaxBreakPulseWidth,
       "zhoneVoiceSignalingObjectsGroup": zhoneVoiceSignalingObjectsGroup}
)
