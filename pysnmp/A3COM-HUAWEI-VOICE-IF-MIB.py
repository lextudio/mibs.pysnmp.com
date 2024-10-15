# SNMP MIB module (A3COM-HUAWEI-VOICE-IF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-HUAWEI-VOICE-IF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:29:26 2024
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

(h3cVoice,) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
    "h3cVoice")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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


# MODULE-IDENTITY

h3cVoiceInterface = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 13)
)
h3cVoiceInterface.setRevisions(
        ("2007-12-10 17:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cVoiceIfObjects_ObjectIdentity = ObjectIdentity
h3cVoiceIfObjects = _H3cVoiceIfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 13, 1)
)
_H3cVoiceIfConfigTable_Object = MibTable
h3cVoiceIfConfigTable = _H3cVoiceIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 13, 1, 1)
)
if mibBuilder.loadTexts:
    h3cVoiceIfConfigTable.setStatus("current")
_H3cVoiceIfConfigEntry_Object = MibTableRow
h3cVoiceIfConfigEntry = _H3cVoiceIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 13, 1, 1, 1)
)
h3cVoiceIfConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cVoiceIfConfigEntry.setStatus("current")


class _H3cVoiceIfCfgCngOn_Type(Integer32):
    """Custom type h3cVoiceIfCfgCngOn based on Integer32"""
    defaultValue = 1

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


_H3cVoiceIfCfgCngOn_Type.__name__ = "Integer32"
_H3cVoiceIfCfgCngOn_Object = MibTableColumn
h3cVoiceIfCfgCngOn = _H3cVoiceIfCfgCngOn_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 13, 1, 1, 1, 1),
    _H3cVoiceIfCfgCngOn_Type()
)
h3cVoiceIfCfgCngOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoiceIfCfgCngOn.setStatus("current")


class _H3cVoiceIfCfgNonLinearSwitch_Type(Integer32):
    """Custom type h3cVoiceIfCfgNonLinearSwitch based on Integer32"""
    defaultValue = 1

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


_H3cVoiceIfCfgNonLinearSwitch_Type.__name__ = "Integer32"
_H3cVoiceIfCfgNonLinearSwitch_Object = MibTableColumn
h3cVoiceIfCfgNonLinearSwitch = _H3cVoiceIfCfgNonLinearSwitch_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 13, 1, 1, 1, 2),
    _H3cVoiceIfCfgNonLinearSwitch_Type()
)
h3cVoiceIfCfgNonLinearSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoiceIfCfgNonLinearSwitch.setStatus("current")


class _H3cVoiceIfCfgInputGain_Type(Integer32):
    """Custom type h3cVoiceIfCfgInputGain based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-140, 139),
    )


_H3cVoiceIfCfgInputGain_Type.__name__ = "Integer32"
_H3cVoiceIfCfgInputGain_Object = MibTableColumn
h3cVoiceIfCfgInputGain = _H3cVoiceIfCfgInputGain_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 13, 1, 1, 1, 3),
    _H3cVoiceIfCfgInputGain_Type()
)
h3cVoiceIfCfgInputGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoiceIfCfgInputGain.setStatus("current")


class _H3cVoiceIfCfgOutputGain_Type(Integer32):
    """Custom type h3cVoiceIfCfgOutputGain based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-140, 139),
    )


_H3cVoiceIfCfgOutputGain_Type.__name__ = "Integer32"
_H3cVoiceIfCfgOutputGain_Object = MibTableColumn
h3cVoiceIfCfgOutputGain = _H3cVoiceIfCfgOutputGain_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 13, 1, 1, 1, 4),
    _H3cVoiceIfCfgOutputGain_Type()
)
h3cVoiceIfCfgOutputGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoiceIfCfgOutputGain.setStatus("current")


class _H3cVoiceIfCfgEchoCancelSwitch_Type(Integer32):
    """Custom type h3cVoiceIfCfgEchoCancelSwitch based on Integer32"""
    defaultValue = 1

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


_H3cVoiceIfCfgEchoCancelSwitch_Type.__name__ = "Integer32"
_H3cVoiceIfCfgEchoCancelSwitch_Object = MibTableColumn
h3cVoiceIfCfgEchoCancelSwitch = _H3cVoiceIfCfgEchoCancelSwitch_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 13, 1, 1, 1, 5),
    _H3cVoiceIfCfgEchoCancelSwitch_Type()
)
h3cVoiceIfCfgEchoCancelSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoiceIfCfgEchoCancelSwitch.setStatus("current")


class _H3cVoiceIfCfgEchoCancelDelay_Type(Integer32):
    """Custom type h3cVoiceIfCfgEchoCancelDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_H3cVoiceIfCfgEchoCancelDelay_Type.__name__ = "Integer32"
_H3cVoiceIfCfgEchoCancelDelay_Object = MibTableColumn
h3cVoiceIfCfgEchoCancelDelay = _H3cVoiceIfCfgEchoCancelDelay_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 13, 1, 1, 1, 6),
    _H3cVoiceIfCfgEchoCancelDelay_Type()
)
h3cVoiceIfCfgEchoCancelDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoiceIfCfgEchoCancelDelay.setStatus("current")


class _H3cVoiceIfCfgTimerDialInterval_Type(Integer32):
    """Custom type h3cVoiceIfCfgTimerDialInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_H3cVoiceIfCfgTimerDialInterval_Type.__name__ = "Integer32"
_H3cVoiceIfCfgTimerDialInterval_Object = MibTableColumn
h3cVoiceIfCfgTimerDialInterval = _H3cVoiceIfCfgTimerDialInterval_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 13, 1, 1, 1, 7),
    _H3cVoiceIfCfgTimerDialInterval_Type()
)
h3cVoiceIfCfgTimerDialInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoiceIfCfgTimerDialInterval.setStatus("current")


class _H3cVoiceIfCfgTimerFirstDial_Type(Integer32):
    """Custom type h3cVoiceIfCfgTimerFirstDial based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_H3cVoiceIfCfgTimerFirstDial_Type.__name__ = "Integer32"
_H3cVoiceIfCfgTimerFirstDial_Object = MibTableColumn
h3cVoiceIfCfgTimerFirstDial = _H3cVoiceIfCfgTimerFirstDial_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 13, 1, 1, 1, 8),
    _H3cVoiceIfCfgTimerFirstDial_Type()
)
h3cVoiceIfCfgTimerFirstDial.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoiceIfCfgTimerFirstDial.setStatus("current")


class _H3cVoiceIfCfgPrivateline_Type(DisplayString):
    """Custom type h3cVoiceIfCfgPrivateline based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_H3cVoiceIfCfgPrivateline_Type.__name__ = "DisplayString"
_H3cVoiceIfCfgPrivateline_Object = MibTableColumn
h3cVoiceIfCfgPrivateline = _H3cVoiceIfCfgPrivateline_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 13, 1, 1, 1, 9),
    _H3cVoiceIfCfgPrivateline_Type()
)
h3cVoiceIfCfgPrivateline.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoiceIfCfgPrivateline.setStatus("current")


class _H3cVoiceIfCfgRegTone_Type(OctetString):
    """Custom type h3cVoiceIfCfgRegTone based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(2, 3),
    )


_H3cVoiceIfCfgRegTone_Type.__name__ = "OctetString"
_H3cVoiceIfCfgRegTone_Object = MibTableColumn
h3cVoiceIfCfgRegTone = _H3cVoiceIfCfgRegTone_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 39, 13, 1, 1, 1, 10),
    _H3cVoiceIfCfgRegTone_Type()
)
h3cVoiceIfCfgRegTone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cVoiceIfCfgRegTone.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-VOICE-IF-MIB",
    **{"h3cVoiceInterface": h3cVoiceInterface,
       "h3cVoiceIfObjects": h3cVoiceIfObjects,
       "h3cVoiceIfConfigTable": h3cVoiceIfConfigTable,
       "h3cVoiceIfConfigEntry": h3cVoiceIfConfigEntry,
       "h3cVoiceIfCfgCngOn": h3cVoiceIfCfgCngOn,
       "h3cVoiceIfCfgNonLinearSwitch": h3cVoiceIfCfgNonLinearSwitch,
       "h3cVoiceIfCfgInputGain": h3cVoiceIfCfgInputGain,
       "h3cVoiceIfCfgOutputGain": h3cVoiceIfCfgOutputGain,
       "h3cVoiceIfCfgEchoCancelSwitch": h3cVoiceIfCfgEchoCancelSwitch,
       "h3cVoiceIfCfgEchoCancelDelay": h3cVoiceIfCfgEchoCancelDelay,
       "h3cVoiceIfCfgTimerDialInterval": h3cVoiceIfCfgTimerDialInterval,
       "h3cVoiceIfCfgTimerFirstDial": h3cVoiceIfCfgTimerFirstDial,
       "h3cVoiceIfCfgPrivateline": h3cVoiceIfCfgPrivateline,
       "h3cVoiceIfCfgRegTone": h3cVoiceIfCfgRegTone}
)
