# SNMP MIB module (HUAWEI-VO-IF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-VO-IF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:06:32 2024
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

(voice,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "voice")

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

hwVoiceIfMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 2)
)
hwVoiceIfMIB.setRevisions(
        ("2004-04-08 13:45",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwVoIfObjects_ObjectIdentity = ObjectIdentity
hwVoIfObjects = _HwVoIfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 2, 1)
)
_HwVoIfConfigTable_Object = MibTable
hwVoIfConfigTable = _HwVoIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hwVoIfConfigTable.setStatus("current")
_HwVoIfConfigEntry_Object = MibTableRow
hwVoIfConfigEntry = _HwVoIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 2, 1, 1, 1)
)
hwVoIfConfigEntry.setIndexNames(
    (0, "HUAWEI-VO-IF-MIB", "hwVoIfConfigPortNumber"),
    (0, "HUAWEI-VO-IF-MIB", "hwVoIfConfigGroupNumber"),
)
if mibBuilder.loadTexts:
    hwVoIfConfigEntry.setStatus("current")
_HwVoIfConfigPortNumber_Type = Integer32
_HwVoIfConfigPortNumber_Object = MibTableColumn
hwVoIfConfigPortNumber = _HwVoIfConfigPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 2, 1, 1, 1, 1),
    _HwVoIfConfigPortNumber_Type()
)
hwVoIfConfigPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoIfConfigPortNumber.setStatus("current")
_HwVoIfConfigGroupNumber_Type = Integer32
_HwVoIfConfigGroupNumber_Object = MibTableColumn
hwVoIfConfigGroupNumber = _HwVoIfConfigGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 2, 1, 1, 1, 2),
    _HwVoIfConfigGroupNumber_Type()
)
hwVoIfConfigGroupNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoIfConfigGroupNumber.setStatus("current")


class _HwVoIfConfigCngOn_Type(Integer32):
    """Custom type hwVoIfConfigCngOn based on Integer32"""
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


_HwVoIfConfigCngOn_Type.__name__ = "Integer32"
_HwVoIfConfigCngOn_Object = MibTableColumn
hwVoIfConfigCngOn = _HwVoIfConfigCngOn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 2, 1, 1, 1, 3),
    _HwVoIfConfigCngOn_Type()
)
hwVoIfConfigCngOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoIfConfigCngOn.setStatus("current")


class _HwVoIfConfigNonLinearProcessSwitch_Type(Integer32):
    """Custom type hwVoIfConfigNonLinearProcessSwitch based on Integer32"""
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


_HwVoIfConfigNonLinearProcessSwitch_Type.__name__ = "Integer32"
_HwVoIfConfigNonLinearProcessSwitch_Object = MibTableColumn
hwVoIfConfigNonLinearProcessSwitch = _HwVoIfConfigNonLinearProcessSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 2, 1, 1, 1, 4),
    _HwVoIfConfigNonLinearProcessSwitch_Type()
)
hwVoIfConfigNonLinearProcessSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoIfConfigNonLinearProcessSwitch.setStatus("obsolete")


class _HwVoIfConfigMusicThreshold_Type(Integer32):
    """Custom type hwVoIfConfigMusicThreshold based on Integer32"""
    defaultValue = -38

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-70, -30),
    )


_HwVoIfConfigMusicThreshold_Type.__name__ = "Integer32"
_HwVoIfConfigMusicThreshold_Object = MibTableColumn
hwVoIfConfigMusicThreshold = _HwVoIfConfigMusicThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 2, 1, 1, 1, 5),
    _HwVoIfConfigMusicThreshold_Type()
)
hwVoIfConfigMusicThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoIfConfigMusicThreshold.setStatus("obsolete")


class _HwVoIfConfigInputGain_Type(Integer32):
    """Custom type hwVoIfConfigInputGain based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-14, 14),
    )


_HwVoIfConfigInputGain_Type.__name__ = "Integer32"
_HwVoIfConfigInputGain_Object = MibTableColumn
hwVoIfConfigInputGain = _HwVoIfConfigInputGain_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 2, 1, 1, 1, 6),
    _HwVoIfConfigInputGain_Type()
)
hwVoIfConfigInputGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoIfConfigInputGain.setStatus("current")


class _HwVoIfConfigOutputGain_Type(Integer32):
    """Custom type hwVoIfConfigOutputGain based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-14, 14),
    )


_HwVoIfConfigOutputGain_Type.__name__ = "Integer32"
_HwVoIfConfigOutputGain_Object = MibTableColumn
hwVoIfConfigOutputGain = _HwVoIfConfigOutputGain_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 2, 1, 1, 1, 7),
    _HwVoIfConfigOutputGain_Type()
)
hwVoIfConfigOutputGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoIfConfigOutputGain.setStatus("current")


class _HwVoIfConfigEchoCancellationSwitch_Type(Integer32):
    """Custom type hwVoIfConfigEchoCancellationSwitch based on Integer32"""
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


_HwVoIfConfigEchoCancellationSwitch_Type.__name__ = "Integer32"
_HwVoIfConfigEchoCancellationSwitch_Object = MibTableColumn
hwVoIfConfigEchoCancellationSwitch = _HwVoIfConfigEchoCancellationSwitch_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 2, 1, 1, 1, 8),
    _HwVoIfConfigEchoCancellationSwitch_Type()
)
hwVoIfConfigEchoCancellationSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoIfConfigEchoCancellationSwitch.setStatus("current")


class _HwVoIfConfigEchoCancellationCoverage_Type(Integer32):
    """Custom type hwVoIfConfigEchoCancellationCoverage based on Integer32"""
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
        *(("echoCancelCoverage16ms", 1),
          ("echoCancelCoverage24ms", 2),
          ("echoCancelCoverage32ms", 3))
    )


_HwVoIfConfigEchoCancellationCoverage_Type.__name__ = "Integer32"
_HwVoIfConfigEchoCancellationCoverage_Object = MibTableColumn
hwVoIfConfigEchoCancellationCoverage = _HwVoIfConfigEchoCancellationCoverage_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 2, 1, 1, 1, 9),
    _HwVoIfConfigEchoCancellationCoverage_Type()
)
hwVoIfConfigEchoCancellationCoverage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoIfConfigEchoCancellationCoverage.setStatus("obsolete")


class _HwVoIfConfigEchoCancellationDelay_Type(Integer32):
    """Custom type hwVoIfConfigEchoCancellationDelay based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_HwVoIfConfigEchoCancellationDelay_Type.__name__ = "Integer32"
_HwVoIfConfigEchoCancellationDelay_Object = MibTableColumn
hwVoIfConfigEchoCancellationDelay = _HwVoIfConfigEchoCancellationDelay_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 2, 1, 1, 1, 10),
    _HwVoIfConfigEchoCancellationDelay_Type()
)
hwVoIfConfigEchoCancellationDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoIfConfigEchoCancellationDelay.setStatus("current")


class _HwVoIfConfigPlarNumber_Type(OctetString):
    """Custom type hwVoIfConfigPlarNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwVoIfConfigPlarNumber_Type.__name__ = "OctetString"
_HwVoIfConfigPlarNumber_Object = MibTableColumn
hwVoIfConfigPlarNumber = _HwVoIfConfigPlarNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 2, 1, 1, 1, 11),
    _HwVoIfConfigPlarNumber_Type()
)
hwVoIfConfigPlarNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoIfConfigPlarNumber.setStatus("current")


class _HwVoIfConfigRegionalTone_Type(OctetString):
    """Custom type hwVoIfConfigRegionalTone based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(2, 2),
    )


_HwVoIfConfigRegionalTone_Type.__name__ = "OctetString"
_HwVoIfConfigRegionalTone_Object = MibTableColumn
hwVoIfConfigRegionalTone = _HwVoIfConfigRegionalTone_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 2, 1, 1, 1, 12),
    _HwVoIfConfigRegionalTone_Type()
)
hwVoIfConfigRegionalTone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoIfConfigRegionalTone.setStatus("current")


class _HwVoIfConfigDescription_Type(OctetString):
    """Custom type hwVoIfConfigDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwVoIfConfigDescription_Type.__name__ = "OctetString"
_HwVoIfConfigDescription_Object = MibTableColumn
hwVoIfConfigDescription = _HwVoIfConfigDescription_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 2, 1, 1, 1, 13),
    _HwVoIfConfigDescription_Type()
)
hwVoIfConfigDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoIfConfigDescription.setStatus("current")


class _HwVoIfConfigStatus_Type(Integer32):
    """Custom type hwVoIfConfigStatus based on Integer32"""
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


_HwVoIfConfigStatus_Type.__name__ = "Integer32"
_HwVoIfConfigStatus_Object = MibTableColumn
hwVoIfConfigStatus = _HwVoIfConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 2, 1, 1, 1, 14),
    _HwVoIfConfigStatus_Type()
)
hwVoIfConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwVoIfConfigStatus.setStatus("current")


class _HwVoIfConfigDtmfThreshold_Type(Integer32):
    """Custom type hwVoIfConfigDtmfThreshold based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("insensitivty", 2),
          ("sensitivity", 1))
    )


_HwVoIfConfigDtmfThreshold_Type.__name__ = "Integer32"
_HwVoIfConfigDtmfThreshold_Object = MibTableColumn
hwVoIfConfigDtmfThreshold = _HwVoIfConfigDtmfThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 2, 1, 1, 1, 15),
    _HwVoIfConfigDtmfThreshold_Type()
)
hwVoIfConfigDtmfThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoIfConfigDtmfThreshold.setStatus("current")


class _HwVoIfConfigCallingNumSubstRule_Type(Integer32):
    """Custom type hwVoIfConfigCallingNumSubstRule based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwVoIfConfigCallingNumSubstRule_Type.__name__ = "Integer32"
_HwVoIfConfigCallingNumSubstRule_Object = MibTableColumn
hwVoIfConfigCallingNumSubstRule = _HwVoIfConfigCallingNumSubstRule_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 2, 1, 1, 1, 16),
    _HwVoIfConfigCallingNumSubstRule_Type()
)
hwVoIfConfigCallingNumSubstRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoIfConfigCallingNumSubstRule.setStatus("current")


class _HwVoIfConfigCalledNumSubstRule_Type(Integer32):
    """Custom type hwVoIfConfigCalledNumSubstRule based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwVoIfConfigCalledNumSubstRule_Type.__name__ = "Integer32"
_HwVoIfConfigCalledNumSubstRule_Object = MibTableColumn
hwVoIfConfigCalledNumSubstRule = _HwVoIfConfigCalledNumSubstRule_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 1, 2, 1, 1, 1, 17),
    _HwVoIfConfigCalledNumSubstRule_Type()
)
hwVoIfConfigCalledNumSubstRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwVoIfConfigCalledNumSubstRule.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-VO-IF-MIB",
    **{"hwVoiceIfMIB": hwVoiceIfMIB,
       "hwVoIfObjects": hwVoIfObjects,
       "hwVoIfConfigTable": hwVoIfConfigTable,
       "hwVoIfConfigEntry": hwVoIfConfigEntry,
       "hwVoIfConfigPortNumber": hwVoIfConfigPortNumber,
       "hwVoIfConfigGroupNumber": hwVoIfConfigGroupNumber,
       "hwVoIfConfigCngOn": hwVoIfConfigCngOn,
       "hwVoIfConfigNonLinearProcessSwitch": hwVoIfConfigNonLinearProcessSwitch,
       "hwVoIfConfigMusicThreshold": hwVoIfConfigMusicThreshold,
       "hwVoIfConfigInputGain": hwVoIfConfigInputGain,
       "hwVoIfConfigOutputGain": hwVoIfConfigOutputGain,
       "hwVoIfConfigEchoCancellationSwitch": hwVoIfConfigEchoCancellationSwitch,
       "hwVoIfConfigEchoCancellationCoverage": hwVoIfConfigEchoCancellationCoverage,
       "hwVoIfConfigEchoCancellationDelay": hwVoIfConfigEchoCancellationDelay,
       "hwVoIfConfigPlarNumber": hwVoIfConfigPlarNumber,
       "hwVoIfConfigRegionalTone": hwVoIfConfigRegionalTone,
       "hwVoIfConfigDescription": hwVoIfConfigDescription,
       "hwVoIfConfigStatus": hwVoIfConfigStatus,
       "hwVoIfConfigDtmfThreshold": hwVoIfConfigDtmfThreshold,
       "hwVoIfConfigCallingNumSubstRule": hwVoIfConfigCallingNumSubstRule,
       "hwVoIfConfigCalledNumSubstRule": hwVoIfConfigCalledNumSubstRule}
)
