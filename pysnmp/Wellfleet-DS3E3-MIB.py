# SNMP MIB module (Wellfleet-DS3E3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-DS3E3-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:16:06 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(wfDsx3Group,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfDsx3Group")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfDs3E3ConfigTable_Object = MibTable
wfDs3E3ConfigTable = _WfDs3E3ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 10)
)
if mibBuilder.loadTexts:
    wfDs3E3ConfigTable.setStatus("mandatory")
_WfDs3E3ConfigEntry_Object = MibTableRow
wfDs3E3ConfigEntry = _WfDs3E3ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 10, 1)
)
wfDs3E3ConfigEntry.setIndexNames(
    (0, "Wellfleet-DS3E3-MIB", "wfDs3E3ConfigLineIndex"),
)
if mibBuilder.loadTexts:
    wfDs3E3ConfigEntry.setStatus("mandatory")


class _WfDs3E3ConfigDelete_Type(Integer32):
    """Custom type wfDs3E3ConfigDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfDs3E3ConfigDelete_Type.__name__ = "Integer32"
_WfDs3E3ConfigDelete_Object = MibTableColumn
wfDs3E3ConfigDelete = _WfDs3E3ConfigDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 10, 1, 1),
    _WfDs3E3ConfigDelete_Type()
)
wfDs3E3ConfigDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs3E3ConfigDelete.setStatus("mandatory")


class _WfDs3E3ConfigDisable_Type(Integer32):
    """Custom type wfDs3E3ConfigDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_WfDs3E3ConfigDisable_Type.__name__ = "Integer32"
_WfDs3E3ConfigDisable_Object = MibTableColumn
wfDs3E3ConfigDisable = _WfDs3E3ConfigDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 10, 1, 2),
    _WfDs3E3ConfigDisable_Type()
)
wfDs3E3ConfigDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs3E3ConfigDisable.setStatus("mandatory")


class _WfDs3E3ConfigState_Type(Integer32):
    """Custom type wfDs3E3ConfigState based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              20)
        )
    )
    namedValues = NamedValues(
        *(("ais", 6),
          ("down", 2),
          ("lof", 4),
          ("loopback", 7),
          ("los", 3),
          ("notpresent", 20),
          ("raif", 5),
          ("up", 1))
    )


_WfDs3E3ConfigState_Type.__name__ = "Integer32"
_WfDs3E3ConfigState_Object = MibTableColumn
wfDs3E3ConfigState = _WfDs3E3ConfigState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 10, 1, 3),
    _WfDs3E3ConfigState_Type()
)
wfDs3E3ConfigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3E3ConfigState.setStatus("mandatory")
_WfDs3E3ConfigLastChange_Type = TimeTicks
_WfDs3E3ConfigLastChange_Object = MibTableColumn
wfDs3E3ConfigLastChange = _WfDs3E3ConfigLastChange_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 10, 1, 4),
    _WfDs3E3ConfigLastChange_Type()
)
wfDs3E3ConfigLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3E3ConfigLastChange.setStatus("mandatory")


class _WfDs3E3ConfigLineIndex_Type(Integer32):
    """Custom type wfDs3E3ConfigLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WfDs3E3ConfigLineIndex_Type.__name__ = "Integer32"
_WfDs3E3ConfigLineIndex_Object = MibTableColumn
wfDs3E3ConfigLineIndex = _WfDs3E3ConfigLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 10, 1, 5),
    _WfDs3E3ConfigLineIndex_Type()
)
wfDs3E3ConfigLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3E3ConfigLineIndex.setStatus("mandatory")
_WfDs3E3ConfigIfIndex_Type = Integer32
_WfDs3E3ConfigIfIndex_Object = MibTableColumn
wfDs3E3ConfigIfIndex = _WfDs3E3ConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 10, 1, 6),
    _WfDs3E3ConfigIfIndex_Type()
)
wfDs3E3ConfigIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3E3ConfigIfIndex.setStatus("mandatory")


class _WfDs3E3ConfigLineType_Type(Integer32):
    """Custom type wfDs3E3ConfigLineType based on Integer32"""
    defaultValue = 9

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("autodetect", 9),
          ("ds3cbitparity", 4),
          ("ds3clearchannel", 5),
          ("ds3m23", 2),
          ("ds3other", 1),
          ("ds3syntran", 3),
          ("e3framed", 7),
          ("e3other", 6),
          ("e3plcp", 8))
    )


_WfDs3E3ConfigLineType_Type.__name__ = "Integer32"
_WfDs3E3ConfigLineType_Object = MibTableColumn
wfDs3E3ConfigLineType = _WfDs3E3ConfigLineType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 10, 1, 7),
    _WfDs3E3ConfigLineType_Type()
)
wfDs3E3ConfigLineType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs3E3ConfigLineType.setStatus("mandatory")


class _WfDs3E3ConfigLineCoding_Type(Integer32):
    """Custom type wfDs3E3ConfigLineCoding based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("b3zs", 2),
          ("hdb3", 3),
          ("other", 1))
    )


_WfDs3E3ConfigLineCoding_Type.__name__ = "Integer32"
_WfDs3E3ConfigLineCoding_Object = MibTableColumn
wfDs3E3ConfigLineCoding = _WfDs3E3ConfigLineCoding_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 10, 1, 8),
    _WfDs3E3ConfigLineCoding_Type()
)
wfDs3E3ConfigLineCoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs3E3ConfigLineCoding.setStatus("mandatory")


class _WfDs3E3ConfigLoopbackConfig_Type(Integer32):
    """Custom type wfDs3E3ConfigLoopbackConfig based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("lineloop", 3),
          ("noloop", 1),
          ("payloadloop", 2))
    )


_WfDs3E3ConfigLoopbackConfig_Type.__name__ = "Integer32"
_WfDs3E3ConfigLoopbackConfig_Object = MibTableColumn
wfDs3E3ConfigLoopbackConfig = _WfDs3E3ConfigLoopbackConfig_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 10, 1, 9),
    _WfDs3E3ConfigLoopbackConfig_Type()
)
wfDs3E3ConfigLoopbackConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs3E3ConfigLoopbackConfig.setStatus("mandatory")


class _WfDs3E3ConfigLineStatus_Type(Integer32):
    """Custom type wfDs3E3ConfigLineStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32,
              64,
              128,
              256,
              512)
        )
    )
    namedValues = NamedValues(
        *(("lof", 32),
          ("loopback", 128),
          ("los", 64),
          ("noalarm", 1),
          ("otherfailure", 512),
          ("rcais", 8),
          ("rcrai", 2),
          ("rctestcode", 256),
          ("txais", 16),
          ("txrai", 4))
    )


_WfDs3E3ConfigLineStatus_Type.__name__ = "Integer32"
_WfDs3E3ConfigLineStatus_Object = MibTableColumn
wfDs3E3ConfigLineStatus = _WfDs3E3ConfigLineStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 10, 1, 10),
    _WfDs3E3ConfigLineStatus_Type()
)
wfDs3E3ConfigLineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3E3ConfigLineStatus.setStatus("mandatory")


class _WfDs3E3ConfigPrimaryClockSource_Type(Integer32):
    """Custom type wfDs3E3ConfigPrimaryClockSource based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("external", 2),
          ("internal", 1),
          ("loop", 3))
    )


_WfDs3E3ConfigPrimaryClockSource_Type.__name__ = "Integer32"
_WfDs3E3ConfigPrimaryClockSource_Object = MibTableColumn
wfDs3E3ConfigPrimaryClockSource = _WfDs3E3ConfigPrimaryClockSource_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 10, 1, 11),
    _WfDs3E3ConfigPrimaryClockSource_Type()
)
wfDs3E3ConfigPrimaryClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs3E3ConfigPrimaryClockSource.setStatus("mandatory")


class _WfDs3E3ConfigSecondaryClockSource_Type(Integer32):
    """Custom type wfDs3E3ConfigSecondaryClockSource based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("external", 2),
          ("internal", 1),
          ("loop", 3))
    )


_WfDs3E3ConfigSecondaryClockSource_Type.__name__ = "Integer32"
_WfDs3E3ConfigSecondaryClockSource_Object = MibTableColumn
wfDs3E3ConfigSecondaryClockSource = _WfDs3E3ConfigSecondaryClockSource_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 10, 1, 12),
    _WfDs3E3ConfigSecondaryClockSource_Type()
)
wfDs3E3ConfigSecondaryClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs3E3ConfigSecondaryClockSource.setStatus("mandatory")


class _WfDs3E3ConfigMtu_Type(Integer32):
    """Custom type wfDs3E3ConfigMtu based on Integer32"""
    defaultValue = 4608

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 4608),
    )


_WfDs3E3ConfigMtu_Type.__name__ = "Integer32"
_WfDs3E3ConfigMtu_Object = MibTableColumn
wfDs3E3ConfigMtu = _WfDs3E3ConfigMtu_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 10, 1, 13),
    _WfDs3E3ConfigMtu_Type()
)
wfDs3E3ConfigMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs3E3ConfigMtu.setStatus("mandatory")


class _WfDs3E3ConfigLineBuildOut_Type(Integer32):
    """Custom type wfDs3E3ConfigLineBuildOut based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("long", 1),
          ("short", 2))
    )


_WfDs3E3ConfigLineBuildOut_Type.__name__ = "Integer32"
_WfDs3E3ConfigLineBuildOut_Object = MibTableColumn
wfDs3E3ConfigLineBuildOut = _WfDs3E3ConfigLineBuildOut_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 10, 1, 14),
    _WfDs3E3ConfigLineBuildOut_Type()
)
wfDs3E3ConfigLineBuildOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs3E3ConfigLineBuildOut.setStatus("mandatory")


class _WfDs3E3ConfigCurrentClock_Type(Integer32):
    """Custom type wfDs3E3ConfigCurrentClock based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("external", 2),
          ("internal", 1),
          ("loop", 3))
    )


_WfDs3E3ConfigCurrentClock_Type.__name__ = "Integer32"
_WfDs3E3ConfigCurrentClock_Object = MibTableColumn
wfDs3E3ConfigCurrentClock = _WfDs3E3ConfigCurrentClock_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 10, 1, 15),
    _WfDs3E3ConfigCurrentClock_Type()
)
wfDs3E3ConfigCurrentClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3E3ConfigCurrentClock.setStatus("mandatory")


class _WfDs3E3ConfigExtClockOperational_Type(Integer32):
    """Custom type wfDs3E3ConfigExtClockOperational based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notpresent", 2),
          ("present", 1))
    )


_WfDs3E3ConfigExtClockOperational_Type.__name__ = "Integer32"
_WfDs3E3ConfigExtClockOperational_Object = MibTableColumn
wfDs3E3ConfigExtClockOperational = _WfDs3E3ConfigExtClockOperational_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 10, 1, 16),
    _WfDs3E3ConfigExtClockOperational_Type()
)
wfDs3E3ConfigExtClockOperational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3E3ConfigExtClockOperational.setStatus("mandatory")


class _WfDs3E3ConfigSetupAlarmThreshold_Type(Integer32):
    """Custom type wfDs3E3ConfigSetupAlarmThreshold based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_WfDs3E3ConfigSetupAlarmThreshold_Type.__name__ = "Integer32"
_WfDs3E3ConfigSetupAlarmThreshold_Object = MibTableColumn
wfDs3E3ConfigSetupAlarmThreshold = _WfDs3E3ConfigSetupAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 10, 1, 17),
    _WfDs3E3ConfigSetupAlarmThreshold_Type()
)
wfDs3E3ConfigSetupAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs3E3ConfigSetupAlarmThreshold.setStatus("mandatory")


class _WfDs3E3ConfigClearAlarmThreshold_Type(Integer32):
    """Custom type wfDs3E3ConfigClearAlarmThreshold based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_WfDs3E3ConfigClearAlarmThreshold_Type.__name__ = "Integer32"
_WfDs3E3ConfigClearAlarmThreshold_Object = MibTableColumn
wfDs3E3ConfigClearAlarmThreshold = _WfDs3E3ConfigClearAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 10, 1, 18),
    _WfDs3E3ConfigClearAlarmThreshold_Type()
)
wfDs3E3ConfigClearAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs3E3ConfigClearAlarmThreshold.setStatus("mandatory")


class _WfDs3E3ConfigLoopbackState_Type(Integer32):
    """Custom type wfDs3E3ConfigLoopbackState based on Integer32"""
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
        *(("mgrreqlineloop", 2),
          ("mgrreqpayloadloop", 3),
          ("netreqlineloop", 4),
          ("netreqpayloadloop", 5),
          ("noloop", 1))
    )


_WfDs3E3ConfigLoopbackState_Type.__name__ = "Integer32"
_WfDs3E3ConfigLoopbackState_Object = MibTableColumn
wfDs3E3ConfigLoopbackState = _WfDs3E3ConfigLoopbackState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 10, 1, 19),
    _WfDs3E3ConfigLoopbackState_Type()
)
wfDs3E3ConfigLoopbackState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3E3ConfigLoopbackState.setStatus("mandatory")


class _WfDs3E3ConfigSendCode_Type(Integer32):
    """Custom type wfDs3E3ConfigSendCode based on Integer32"""
    defaultValue = 1

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
        *(("sendds1loopcode", 4),
          ("sendlinecode", 2),
          ("sendnocode", 1),
          ("sendpayloadcode", 3))
    )


_WfDs3E3ConfigSendCode_Type.__name__ = "Integer32"
_WfDs3E3ConfigSendCode_Object = MibTableColumn
wfDs3E3ConfigSendCode = _WfDs3E3ConfigSendCode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 10, 1, 20),
    _WfDs3E3ConfigSendCode_Type()
)
wfDs3E3ConfigSendCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3E3ConfigSendCode.setStatus("mandatory")
_WfDs3E3ActionTable_Object = MibTable
wfDs3E3ActionTable = _WfDs3E3ActionTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 17)
)
if mibBuilder.loadTexts:
    wfDs3E3ActionTable.setStatus("mandatory")
_WfDs3E3ActionEntry_Object = MibTableRow
wfDs3E3ActionEntry = _WfDs3E3ActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 17, 1)
)
wfDs3E3ActionEntry.setIndexNames(
    (0, "Wellfleet-DS3E3-MIB", "wfDs3E3ActionPortLineNumber"),
)
if mibBuilder.loadTexts:
    wfDs3E3ActionEntry.setStatus("mandatory")
_WfDs3E3ActionPortLineNumber_Type = Integer32
_WfDs3E3ActionPortLineNumber_Object = MibTableColumn
wfDs3E3ActionPortLineNumber = _WfDs3E3ActionPortLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 17, 1, 1),
    _WfDs3E3ActionPortLineNumber_Type()
)
wfDs3E3ActionPortLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfDs3E3ActionPortLineNumber.setStatus("mandatory")


class _WfDs3E3ActionSendFeacLoopCode_Type(Integer32):
    """Custom type wfDs3E3ActionSendFeacLoopCode based on Integer32"""
    defaultValue = 21

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              21)
        )
    )
    namedValues = NamedValues(
        *(("deactivatell", 2),
          ("deactivatepl", 4),
          ("lineloop", 1),
          ("noaction", 21),
          ("payloadloop", 3))
    )


_WfDs3E3ActionSendFeacLoopCode_Type.__name__ = "Integer32"
_WfDs3E3ActionSendFeacLoopCode_Object = MibTableColumn
wfDs3E3ActionSendFeacLoopCode = _WfDs3E3ActionSendFeacLoopCode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 17, 1, 2),
    _WfDs3E3ActionSendFeacLoopCode_Type()
)
wfDs3E3ActionSendFeacLoopCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs3E3ActionSendFeacLoopCode.setStatus("mandatory")


class _WfDs3E3ActionSendFeacDs1LoopUpCode_Type(Integer32):
    """Custom type wfDs3E3ActionSendFeacDs1LoopUpCode based on Integer32"""
    defaultValue = 29

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            29
        )
    )
    namedValues = NamedValues(
        ("noaction", 29)
    )


_WfDs3E3ActionSendFeacDs1LoopUpCode_Type.__name__ = "Integer32"
_WfDs3E3ActionSendFeacDs1LoopUpCode_Object = MibTableColumn
wfDs3E3ActionSendFeacDs1LoopUpCode = _WfDs3E3ActionSendFeacDs1LoopUpCode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 17, 1, 3),
    _WfDs3E3ActionSendFeacDs1LoopUpCode_Type()
)
wfDs3E3ActionSendFeacDs1LoopUpCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs3E3ActionSendFeacDs1LoopUpCode.setStatus("mandatory")


class _WfDs3E3ActionSendFeacDs1LoopDownCode_Type(Integer32):
    """Custom type wfDs3E3ActionSendFeacDs1LoopDownCode based on Integer32"""
    defaultValue = 29

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            29
        )
    )
    namedValues = NamedValues(
        ("noaction", 29)
    )


_WfDs3E3ActionSendFeacDs1LoopDownCode_Type.__name__ = "Integer32"
_WfDs3E3ActionSendFeacDs1LoopDownCode_Object = MibTableColumn
wfDs3E3ActionSendFeacDs1LoopDownCode = _WfDs3E3ActionSendFeacDs1LoopDownCode_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 17, 1, 4),
    _WfDs3E3ActionSendFeacDs1LoopDownCode_Type()
)
wfDs3E3ActionSendFeacDs1LoopDownCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs3E3ActionSendFeacDs1LoopDownCode.setStatus("mandatory")


class _WfDs3E3ActionClearCurrentStats_Type(Integer32):
    """Custom type wfDs3E3ActionClearCurrentStats based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clrStats", 1),
          ("noaction", 2))
    )


_WfDs3E3ActionClearCurrentStats_Type.__name__ = "Integer32"
_WfDs3E3ActionClearCurrentStats_Object = MibTableColumn
wfDs3E3ActionClearCurrentStats = _WfDs3E3ActionClearCurrentStats_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 17, 1, 5),
    _WfDs3E3ActionClearCurrentStats_Type()
)
wfDs3E3ActionClearCurrentStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs3E3ActionClearCurrentStats.setStatus("mandatory")


class _WfDs3E3ActionClearFarEndCurrentStats_Type(Integer32):
    """Custom type wfDs3E3ActionClearFarEndCurrentStats based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clrStats", 1),
          ("noaction", 2))
    )


_WfDs3E3ActionClearFarEndCurrentStats_Type.__name__ = "Integer32"
_WfDs3E3ActionClearFarEndCurrentStats_Object = MibTableColumn
wfDs3E3ActionClearFarEndCurrentStats = _WfDs3E3ActionClearFarEndCurrentStats_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 17, 1, 6),
    _WfDs3E3ActionClearFarEndCurrentStats_Type()
)
wfDs3E3ActionClearFarEndCurrentStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs3E3ActionClearFarEndCurrentStats.setStatus("mandatory")


class _WfDs3E3ActionClearDayCurrentStats_Type(Integer32):
    """Custom type wfDs3E3ActionClearDayCurrentStats based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clrStats", 1),
          ("noaction", 2))
    )


_WfDs3E3ActionClearDayCurrentStats_Type.__name__ = "Integer32"
_WfDs3E3ActionClearDayCurrentStats_Object = MibTableColumn
wfDs3E3ActionClearDayCurrentStats = _WfDs3E3ActionClearDayCurrentStats_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 17, 1, 7),
    _WfDs3E3ActionClearDayCurrentStats_Type()
)
wfDs3E3ActionClearDayCurrentStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs3E3ActionClearDayCurrentStats.setStatus("mandatory")


class _WfDs3E3ActionClearFarEndDayCurrentStats_Type(Integer32):
    """Custom type wfDs3E3ActionClearFarEndDayCurrentStats based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clrStats", 1),
          ("noaction", 2))
    )


_WfDs3E3ActionClearFarEndDayCurrentStats_Type.__name__ = "Integer32"
_WfDs3E3ActionClearFarEndDayCurrentStats_Object = MibTableColumn
wfDs3E3ActionClearFarEndDayCurrentStats = _WfDs3E3ActionClearFarEndDayCurrentStats_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 17, 1, 8),
    _WfDs3E3ActionClearFarEndDayCurrentStats_Type()
)
wfDs3E3ActionClearFarEndDayCurrentStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs3E3ActionClearFarEndDayCurrentStats.setStatus("mandatory")


class _WfDs3E3ActionClearIntervalStats_Type(Integer32):
    """Custom type wfDs3E3ActionClearIntervalStats based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clrStats", 1),
          ("noaction", 2))
    )


_WfDs3E3ActionClearIntervalStats_Type.__name__ = "Integer32"
_WfDs3E3ActionClearIntervalStats_Object = MibTableColumn
wfDs3E3ActionClearIntervalStats = _WfDs3E3ActionClearIntervalStats_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 17, 1, 9),
    _WfDs3E3ActionClearIntervalStats_Type()
)
wfDs3E3ActionClearIntervalStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs3E3ActionClearIntervalStats.setStatus("mandatory")


class _WfDs3E3ActionClearFarEndIntervalStats_Type(Integer32):
    """Custom type wfDs3E3ActionClearFarEndIntervalStats based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clrStats", 1),
          ("noaction", 2))
    )


_WfDs3E3ActionClearFarEndIntervalStats_Type.__name__ = "Integer32"
_WfDs3E3ActionClearFarEndIntervalStats_Object = MibTableColumn
wfDs3E3ActionClearFarEndIntervalStats = _WfDs3E3ActionClearFarEndIntervalStats_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 4, 26, 17, 1, 10),
    _WfDs3E3ActionClearFarEndIntervalStats_Type()
)
wfDs3E3ActionClearFarEndIntervalStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDs3E3ActionClearFarEndIntervalStats.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-DS3E3-MIB",
    **{"wfDs3E3ConfigTable": wfDs3E3ConfigTable,
       "wfDs3E3ConfigEntry": wfDs3E3ConfigEntry,
       "wfDs3E3ConfigDelete": wfDs3E3ConfigDelete,
       "wfDs3E3ConfigDisable": wfDs3E3ConfigDisable,
       "wfDs3E3ConfigState": wfDs3E3ConfigState,
       "wfDs3E3ConfigLastChange": wfDs3E3ConfigLastChange,
       "wfDs3E3ConfigLineIndex": wfDs3E3ConfigLineIndex,
       "wfDs3E3ConfigIfIndex": wfDs3E3ConfigIfIndex,
       "wfDs3E3ConfigLineType": wfDs3E3ConfigLineType,
       "wfDs3E3ConfigLineCoding": wfDs3E3ConfigLineCoding,
       "wfDs3E3ConfigLoopbackConfig": wfDs3E3ConfigLoopbackConfig,
       "wfDs3E3ConfigLineStatus": wfDs3E3ConfigLineStatus,
       "wfDs3E3ConfigPrimaryClockSource": wfDs3E3ConfigPrimaryClockSource,
       "wfDs3E3ConfigSecondaryClockSource": wfDs3E3ConfigSecondaryClockSource,
       "wfDs3E3ConfigMtu": wfDs3E3ConfigMtu,
       "wfDs3E3ConfigLineBuildOut": wfDs3E3ConfigLineBuildOut,
       "wfDs3E3ConfigCurrentClock": wfDs3E3ConfigCurrentClock,
       "wfDs3E3ConfigExtClockOperational": wfDs3E3ConfigExtClockOperational,
       "wfDs3E3ConfigSetupAlarmThreshold": wfDs3E3ConfigSetupAlarmThreshold,
       "wfDs3E3ConfigClearAlarmThreshold": wfDs3E3ConfigClearAlarmThreshold,
       "wfDs3E3ConfigLoopbackState": wfDs3E3ConfigLoopbackState,
       "wfDs3E3ConfigSendCode": wfDs3E3ConfigSendCode,
       "wfDs3E3ActionTable": wfDs3E3ActionTable,
       "wfDs3E3ActionEntry": wfDs3E3ActionEntry,
       "wfDs3E3ActionPortLineNumber": wfDs3E3ActionPortLineNumber,
       "wfDs3E3ActionSendFeacLoopCode": wfDs3E3ActionSendFeacLoopCode,
       "wfDs3E3ActionSendFeacDs1LoopUpCode": wfDs3E3ActionSendFeacDs1LoopUpCode,
       "wfDs3E3ActionSendFeacDs1LoopDownCode": wfDs3E3ActionSendFeacDs1LoopDownCode,
       "wfDs3E3ActionClearCurrentStats": wfDs3E3ActionClearCurrentStats,
       "wfDs3E3ActionClearFarEndCurrentStats": wfDs3E3ActionClearFarEndCurrentStats,
       "wfDs3E3ActionClearDayCurrentStats": wfDs3E3ActionClearDayCurrentStats,
       "wfDs3E3ActionClearFarEndDayCurrentStats": wfDs3E3ActionClearFarEndDayCurrentStats,
       "wfDs3E3ActionClearIntervalStats": wfDs3E3ActionClearIntervalStats,
       "wfDs3E3ActionClearFarEndIntervalStats": wfDs3E3ActionClearFarEndIntervalStats}
)
