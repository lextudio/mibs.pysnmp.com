# SNMP MIB module (HH3C-VOICE-IF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-VOICE-IF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:55:18 2024
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

(hh3cVoice,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cVoice")

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

hh3cVoiceInterface = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 13)
)
hh3cVoiceInterface.setRevisions(
        ("2007-12-10 17:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cVoiceIfObjects_ObjectIdentity = ObjectIdentity
hh3cVoiceIfObjects = _Hh3cVoiceIfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 13, 1)
)
_Hh3cVoiceIfConfigTable_Object = MibTable
hh3cVoiceIfConfigTable = _Hh3cVoiceIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 13, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cVoiceIfConfigTable.setStatus("current")
_Hh3cVoiceIfConfigEntry_Object = MibTableRow
hh3cVoiceIfConfigEntry = _Hh3cVoiceIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 13, 1, 1, 1)
)
hh3cVoiceIfConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hh3cVoiceIfConfigEntry.setStatus("current")


class _Hh3cVoiceIfCfgCngOn_Type(Integer32):
    """Custom type hh3cVoiceIfCfgCngOn based on Integer32"""
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


_Hh3cVoiceIfCfgCngOn_Type.__name__ = "Integer32"
_Hh3cVoiceIfCfgCngOn_Object = MibTableColumn
hh3cVoiceIfCfgCngOn = _Hh3cVoiceIfCfgCngOn_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 13, 1, 1, 1, 1),
    _Hh3cVoiceIfCfgCngOn_Type()
)
hh3cVoiceIfCfgCngOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVoiceIfCfgCngOn.setStatus("current")


class _Hh3cVoiceIfCfgNonLinearSwitch_Type(Integer32):
    """Custom type hh3cVoiceIfCfgNonLinearSwitch based on Integer32"""
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


_Hh3cVoiceIfCfgNonLinearSwitch_Type.__name__ = "Integer32"
_Hh3cVoiceIfCfgNonLinearSwitch_Object = MibTableColumn
hh3cVoiceIfCfgNonLinearSwitch = _Hh3cVoiceIfCfgNonLinearSwitch_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 13, 1, 1, 1, 2),
    _Hh3cVoiceIfCfgNonLinearSwitch_Type()
)
hh3cVoiceIfCfgNonLinearSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVoiceIfCfgNonLinearSwitch.setStatus("current")


class _Hh3cVoiceIfCfgInputGain_Type(Integer32):
    """Custom type hh3cVoiceIfCfgInputGain based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-140, 139),
    )


_Hh3cVoiceIfCfgInputGain_Type.__name__ = "Integer32"
_Hh3cVoiceIfCfgInputGain_Object = MibTableColumn
hh3cVoiceIfCfgInputGain = _Hh3cVoiceIfCfgInputGain_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 13, 1, 1, 1, 3),
    _Hh3cVoiceIfCfgInputGain_Type()
)
hh3cVoiceIfCfgInputGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVoiceIfCfgInputGain.setStatus("current")


class _Hh3cVoiceIfCfgOutputGain_Type(Integer32):
    """Custom type hh3cVoiceIfCfgOutputGain based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-140, 139),
    )


_Hh3cVoiceIfCfgOutputGain_Type.__name__ = "Integer32"
_Hh3cVoiceIfCfgOutputGain_Object = MibTableColumn
hh3cVoiceIfCfgOutputGain = _Hh3cVoiceIfCfgOutputGain_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 13, 1, 1, 1, 4),
    _Hh3cVoiceIfCfgOutputGain_Type()
)
hh3cVoiceIfCfgOutputGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVoiceIfCfgOutputGain.setStatus("current")


class _Hh3cVoiceIfCfgEchoCancelSwitch_Type(Integer32):
    """Custom type hh3cVoiceIfCfgEchoCancelSwitch based on Integer32"""
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


_Hh3cVoiceIfCfgEchoCancelSwitch_Type.__name__ = "Integer32"
_Hh3cVoiceIfCfgEchoCancelSwitch_Object = MibTableColumn
hh3cVoiceIfCfgEchoCancelSwitch = _Hh3cVoiceIfCfgEchoCancelSwitch_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 13, 1, 1, 1, 5),
    _Hh3cVoiceIfCfgEchoCancelSwitch_Type()
)
hh3cVoiceIfCfgEchoCancelSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVoiceIfCfgEchoCancelSwitch.setStatus("current")


class _Hh3cVoiceIfCfgEchoCancelDelay_Type(Integer32):
    """Custom type hh3cVoiceIfCfgEchoCancelDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_Hh3cVoiceIfCfgEchoCancelDelay_Type.__name__ = "Integer32"
_Hh3cVoiceIfCfgEchoCancelDelay_Object = MibTableColumn
hh3cVoiceIfCfgEchoCancelDelay = _Hh3cVoiceIfCfgEchoCancelDelay_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 13, 1, 1, 1, 6),
    _Hh3cVoiceIfCfgEchoCancelDelay_Type()
)
hh3cVoiceIfCfgEchoCancelDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVoiceIfCfgEchoCancelDelay.setStatus("current")


class _Hh3cVoiceIfCfgTimerDialInterval_Type(Integer32):
    """Custom type hh3cVoiceIfCfgTimerDialInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_Hh3cVoiceIfCfgTimerDialInterval_Type.__name__ = "Integer32"
_Hh3cVoiceIfCfgTimerDialInterval_Object = MibTableColumn
hh3cVoiceIfCfgTimerDialInterval = _Hh3cVoiceIfCfgTimerDialInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 13, 1, 1, 1, 7),
    _Hh3cVoiceIfCfgTimerDialInterval_Type()
)
hh3cVoiceIfCfgTimerDialInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVoiceIfCfgTimerDialInterval.setStatus("current")


class _Hh3cVoiceIfCfgTimerFirstDial_Type(Integer32):
    """Custom type hh3cVoiceIfCfgTimerFirstDial based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_Hh3cVoiceIfCfgTimerFirstDial_Type.__name__ = "Integer32"
_Hh3cVoiceIfCfgTimerFirstDial_Object = MibTableColumn
hh3cVoiceIfCfgTimerFirstDial = _Hh3cVoiceIfCfgTimerFirstDial_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 13, 1, 1, 1, 8),
    _Hh3cVoiceIfCfgTimerFirstDial_Type()
)
hh3cVoiceIfCfgTimerFirstDial.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVoiceIfCfgTimerFirstDial.setStatus("current")


class _Hh3cVoiceIfCfgPrivateline_Type(DisplayString):
    """Custom type hh3cVoiceIfCfgPrivateline based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_Hh3cVoiceIfCfgPrivateline_Type.__name__ = "DisplayString"
_Hh3cVoiceIfCfgPrivateline_Object = MibTableColumn
hh3cVoiceIfCfgPrivateline = _Hh3cVoiceIfCfgPrivateline_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 13, 1, 1, 1, 9),
    _Hh3cVoiceIfCfgPrivateline_Type()
)
hh3cVoiceIfCfgPrivateline.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVoiceIfCfgPrivateline.setStatus("current")


class _Hh3cVoiceIfCfgRegTone_Type(OctetString):
    """Custom type hh3cVoiceIfCfgRegTone based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(2, 3),
    )


_Hh3cVoiceIfCfgRegTone_Type.__name__ = "OctetString"
_Hh3cVoiceIfCfgRegTone_Object = MibTableColumn
hh3cVoiceIfCfgRegTone = _Hh3cVoiceIfCfgRegTone_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 39, 13, 1, 1, 1, 10),
    _Hh3cVoiceIfCfgRegTone_Type()
)
hh3cVoiceIfCfgRegTone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cVoiceIfCfgRegTone.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-VOICE-IF-MIB",
    **{"hh3cVoiceInterface": hh3cVoiceInterface,
       "hh3cVoiceIfObjects": hh3cVoiceIfObjects,
       "hh3cVoiceIfConfigTable": hh3cVoiceIfConfigTable,
       "hh3cVoiceIfConfigEntry": hh3cVoiceIfConfigEntry,
       "hh3cVoiceIfCfgCngOn": hh3cVoiceIfCfgCngOn,
       "hh3cVoiceIfCfgNonLinearSwitch": hh3cVoiceIfCfgNonLinearSwitch,
       "hh3cVoiceIfCfgInputGain": hh3cVoiceIfCfgInputGain,
       "hh3cVoiceIfCfgOutputGain": hh3cVoiceIfCfgOutputGain,
       "hh3cVoiceIfCfgEchoCancelSwitch": hh3cVoiceIfCfgEchoCancelSwitch,
       "hh3cVoiceIfCfgEchoCancelDelay": hh3cVoiceIfCfgEchoCancelDelay,
       "hh3cVoiceIfCfgTimerDialInterval": hh3cVoiceIfCfgTimerDialInterval,
       "hh3cVoiceIfCfgTimerFirstDial": hh3cVoiceIfCfgTimerFirstDial,
       "hh3cVoiceIfCfgPrivateline": hh3cVoiceIfCfgPrivateline,
       "hh3cVoiceIfCfgRegTone": hh3cVoiceIfCfgRegTone}
)
