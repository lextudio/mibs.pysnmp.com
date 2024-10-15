# SNMP MIB module (HPN-ICF-VOICE-IF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-VOICE-IF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:02:11 2024
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

(hpnicfVoice,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfVoice")

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

hpnicfVoiceInterface = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 13)
)
hpnicfVoiceInterface.setRevisions(
        ("2007-12-10 17:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfVoiceIfObjects_ObjectIdentity = ObjectIdentity
hpnicfVoiceIfObjects = _HpnicfVoiceIfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 13, 1)
)
_HpnicfVoiceIfConfigTable_Object = MibTable
hpnicfVoiceIfConfigTable = _HpnicfVoiceIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 13, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfVoiceIfConfigTable.setStatus("current")
_HpnicfVoiceIfConfigEntry_Object = MibTableRow
hpnicfVoiceIfConfigEntry = _HpnicfVoiceIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 13, 1, 1, 1)
)
hpnicfVoiceIfConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfVoiceIfConfigEntry.setStatus("current")


class _HpnicfVoiceIfCfgCngOn_Type(Integer32):
    """Custom type hpnicfVoiceIfCfgCngOn based on Integer32"""
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


_HpnicfVoiceIfCfgCngOn_Type.__name__ = "Integer32"
_HpnicfVoiceIfCfgCngOn_Object = MibTableColumn
hpnicfVoiceIfCfgCngOn = _HpnicfVoiceIfCfgCngOn_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 13, 1, 1, 1, 1),
    _HpnicfVoiceIfCfgCngOn_Type()
)
hpnicfVoiceIfCfgCngOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfVoiceIfCfgCngOn.setStatus("current")


class _HpnicfVoiceIfCfgNonLinearSwitch_Type(Integer32):
    """Custom type hpnicfVoiceIfCfgNonLinearSwitch based on Integer32"""
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


_HpnicfVoiceIfCfgNonLinearSwitch_Type.__name__ = "Integer32"
_HpnicfVoiceIfCfgNonLinearSwitch_Object = MibTableColumn
hpnicfVoiceIfCfgNonLinearSwitch = _HpnicfVoiceIfCfgNonLinearSwitch_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 13, 1, 1, 1, 2),
    _HpnicfVoiceIfCfgNonLinearSwitch_Type()
)
hpnicfVoiceIfCfgNonLinearSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfVoiceIfCfgNonLinearSwitch.setStatus("current")


class _HpnicfVoiceIfCfgInputGain_Type(Integer32):
    """Custom type hpnicfVoiceIfCfgInputGain based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-140, 139),
    )


_HpnicfVoiceIfCfgInputGain_Type.__name__ = "Integer32"
_HpnicfVoiceIfCfgInputGain_Object = MibTableColumn
hpnicfVoiceIfCfgInputGain = _HpnicfVoiceIfCfgInputGain_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 13, 1, 1, 1, 3),
    _HpnicfVoiceIfCfgInputGain_Type()
)
hpnicfVoiceIfCfgInputGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfVoiceIfCfgInputGain.setStatus("current")


class _HpnicfVoiceIfCfgOutputGain_Type(Integer32):
    """Custom type hpnicfVoiceIfCfgOutputGain based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-140, 139),
    )


_HpnicfVoiceIfCfgOutputGain_Type.__name__ = "Integer32"
_HpnicfVoiceIfCfgOutputGain_Object = MibTableColumn
hpnicfVoiceIfCfgOutputGain = _HpnicfVoiceIfCfgOutputGain_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 13, 1, 1, 1, 4),
    _HpnicfVoiceIfCfgOutputGain_Type()
)
hpnicfVoiceIfCfgOutputGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfVoiceIfCfgOutputGain.setStatus("current")


class _HpnicfVoiceIfCfgEchoCancelSwitch_Type(Integer32):
    """Custom type hpnicfVoiceIfCfgEchoCancelSwitch based on Integer32"""
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


_HpnicfVoiceIfCfgEchoCancelSwitch_Type.__name__ = "Integer32"
_HpnicfVoiceIfCfgEchoCancelSwitch_Object = MibTableColumn
hpnicfVoiceIfCfgEchoCancelSwitch = _HpnicfVoiceIfCfgEchoCancelSwitch_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 13, 1, 1, 1, 5),
    _HpnicfVoiceIfCfgEchoCancelSwitch_Type()
)
hpnicfVoiceIfCfgEchoCancelSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfVoiceIfCfgEchoCancelSwitch.setStatus("current")


class _HpnicfVoiceIfCfgEchoCancelDelay_Type(Integer32):
    """Custom type hpnicfVoiceIfCfgEchoCancelDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_HpnicfVoiceIfCfgEchoCancelDelay_Type.__name__ = "Integer32"
_HpnicfVoiceIfCfgEchoCancelDelay_Object = MibTableColumn
hpnicfVoiceIfCfgEchoCancelDelay = _HpnicfVoiceIfCfgEchoCancelDelay_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 13, 1, 1, 1, 6),
    _HpnicfVoiceIfCfgEchoCancelDelay_Type()
)
hpnicfVoiceIfCfgEchoCancelDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfVoiceIfCfgEchoCancelDelay.setStatus("current")


class _HpnicfVoiceIfCfgTimerDialInterval_Type(Integer32):
    """Custom type hpnicfVoiceIfCfgTimerDialInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_HpnicfVoiceIfCfgTimerDialInterval_Type.__name__ = "Integer32"
_HpnicfVoiceIfCfgTimerDialInterval_Object = MibTableColumn
hpnicfVoiceIfCfgTimerDialInterval = _HpnicfVoiceIfCfgTimerDialInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 13, 1, 1, 1, 7),
    _HpnicfVoiceIfCfgTimerDialInterval_Type()
)
hpnicfVoiceIfCfgTimerDialInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfVoiceIfCfgTimerDialInterval.setStatus("current")


class _HpnicfVoiceIfCfgTimerFirstDial_Type(Integer32):
    """Custom type hpnicfVoiceIfCfgTimerFirstDial based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_HpnicfVoiceIfCfgTimerFirstDial_Type.__name__ = "Integer32"
_HpnicfVoiceIfCfgTimerFirstDial_Object = MibTableColumn
hpnicfVoiceIfCfgTimerFirstDial = _HpnicfVoiceIfCfgTimerFirstDial_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 13, 1, 1, 1, 8),
    _HpnicfVoiceIfCfgTimerFirstDial_Type()
)
hpnicfVoiceIfCfgTimerFirstDial.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfVoiceIfCfgTimerFirstDial.setStatus("current")


class _HpnicfVoiceIfCfgPrivateline_Type(DisplayString):
    """Custom type hpnicfVoiceIfCfgPrivateline based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HpnicfVoiceIfCfgPrivateline_Type.__name__ = "DisplayString"
_HpnicfVoiceIfCfgPrivateline_Object = MibTableColumn
hpnicfVoiceIfCfgPrivateline = _HpnicfVoiceIfCfgPrivateline_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 13, 1, 1, 1, 9),
    _HpnicfVoiceIfCfgPrivateline_Type()
)
hpnicfVoiceIfCfgPrivateline.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfVoiceIfCfgPrivateline.setStatus("current")


class _HpnicfVoiceIfCfgRegTone_Type(OctetString):
    """Custom type hpnicfVoiceIfCfgRegTone based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(2, 3),
    )


_HpnicfVoiceIfCfgRegTone_Type.__name__ = "OctetString"
_HpnicfVoiceIfCfgRegTone_Object = MibTableColumn
hpnicfVoiceIfCfgRegTone = _HpnicfVoiceIfCfgRegTone_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 39, 13, 1, 1, 1, 10),
    _HpnicfVoiceIfCfgRegTone_Type()
)
hpnicfVoiceIfCfgRegTone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfVoiceIfCfgRegTone.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-VOICE-IF-MIB",
    **{"hpnicfVoiceInterface": hpnicfVoiceInterface,
       "hpnicfVoiceIfObjects": hpnicfVoiceIfObjects,
       "hpnicfVoiceIfConfigTable": hpnicfVoiceIfConfigTable,
       "hpnicfVoiceIfConfigEntry": hpnicfVoiceIfConfigEntry,
       "hpnicfVoiceIfCfgCngOn": hpnicfVoiceIfCfgCngOn,
       "hpnicfVoiceIfCfgNonLinearSwitch": hpnicfVoiceIfCfgNonLinearSwitch,
       "hpnicfVoiceIfCfgInputGain": hpnicfVoiceIfCfgInputGain,
       "hpnicfVoiceIfCfgOutputGain": hpnicfVoiceIfCfgOutputGain,
       "hpnicfVoiceIfCfgEchoCancelSwitch": hpnicfVoiceIfCfgEchoCancelSwitch,
       "hpnicfVoiceIfCfgEchoCancelDelay": hpnicfVoiceIfCfgEchoCancelDelay,
       "hpnicfVoiceIfCfgTimerDialInterval": hpnicfVoiceIfCfgTimerDialInterval,
       "hpnicfVoiceIfCfgTimerFirstDial": hpnicfVoiceIfCfgTimerFirstDial,
       "hpnicfVoiceIfCfgPrivateline": hpnicfVoiceIfCfgPrivateline,
       "hpnicfVoiceIfCfgRegTone": hpnicfVoiceIfCfgRegTone}
)
