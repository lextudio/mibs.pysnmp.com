# SNMP MIB module (MICOM-4400-VOICE-NETWORK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MICOM-4400-VOICE-NETWORK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:21:37 2024
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

(micom_oscar,) = mibBuilder.importSymbols(
    "MICOM-OSCAR-MIB",
    "micom-oscar")

(mcmSysAsciiTimeOfDay,) = mibBuilder.importSymbols(
    "MICOM-SYS-MIB",
    "mcmSysAsciiTimeOfDay")

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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Micom_2vnet_ObjectIdentity = ObjectIdentity
micom_2vnet = _Micom_2vnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21)
)
_Vnet_configuration_ObjectIdentity = ObjectIdentity
vnet_configuration = _Vnet_configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1)
)
_McmVNETChCfgTable_Object = MibTable
mcmVNETChCfgTable = _McmVNETChCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 1)
)
if mibBuilder.loadTexts:
    mcmVNETChCfgTable.setStatus("mandatory")
_McmVNETChCfgEntry_Object = MibTableRow
mcmVNETChCfgEntry = _McmVNETChCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 1, 1)
)
mcmVNETChCfgEntry.setIndexNames(
    (0, "MICOM-4400-VOICE-NETWORK-MIB", "mcmVNETChCfgLimID"),
    (0, "MICOM-4400-VOICE-NETWORK-MIB", "mcmVNETChCfgChannelID"),
)
if mibBuilder.loadTexts:
    mcmVNETChCfgEntry.setStatus("mandatory")


class _McmVNETChCfgLimID_Type(Integer32):
    """Custom type mcmVNETChCfgLimID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
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
        *(("lim1", 2),
          ("lim2", 3),
          ("lim3", 4),
          ("lim4", 5),
          ("limB", 6),
          ("limC", 7),
          ("limD", 8),
          ("limE", 9))
    )


_McmVNETChCfgLimID_Type.__name__ = "Integer32"
_McmVNETChCfgLimID_Object = MibTableColumn
mcmVNETChCfgLimID = _McmVNETChCfgLimID_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 1, 1, 1),
    _McmVNETChCfgLimID_Type()
)
mcmVNETChCfgLimID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmVNETChCfgLimID.setStatus("mandatory")


class _McmVNETChCfgChannelID_Type(Integer32):
    """Custom type mcmVNETChCfgChannelID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_McmVNETChCfgChannelID_Type.__name__ = "Integer32"
_McmVNETChCfgChannelID_Object = MibTableColumn
mcmVNETChCfgChannelID = _McmVNETChCfgChannelID_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 1, 1, 2),
    _McmVNETChCfgChannelID_Type()
)
mcmVNETChCfgChannelID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmVNETChCfgChannelID.setStatus("mandatory")


class _McmVNETChCfgVoiceProfile_Type(Integer32):
    """Custom type mcmVNETChCfgVoiceProfile based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_McmVNETChCfgVoiceProfile_Type.__name__ = "Integer32"
_McmVNETChCfgVoiceProfile_Object = MibTableColumn
mcmVNETChCfgVoiceProfile = _McmVNETChCfgVoiceProfile_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 1, 1, 3),
    _McmVNETChCfgVoiceProfile_Type()
)
mcmVNETChCfgVoiceProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmVNETChCfgVoiceProfile.setStatus("mandatory")


class _McmVNETChCfgSwitchingProfile_Type(Integer32):
    """Custom type mcmVNETChCfgSwitchingProfile based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_McmVNETChCfgSwitchingProfile_Type.__name__ = "Integer32"
_McmVNETChCfgSwitchingProfile_Object = MibTableColumn
mcmVNETChCfgSwitchingProfile = _McmVNETChCfgSwitchingProfile_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 1, 1, 4),
    _McmVNETChCfgSwitchingProfile_Type()
)
mcmVNETChCfgSwitchingProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmVNETChCfgSwitchingProfile.setStatus("mandatory")


class _McmVNETChCfgInterfaceType_Type(Integer32):
    """Custom type mcmVNETChCfgInterfaceType based on Integer32"""
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
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("bri", 12),
          ("dvm", 11),
          ("enhanced-EandM", 3),
          ("enhanced-loop-start-FXO", 4),
          ("enhanced-loop-start-FXS", 2),
          ("ground-start-FXO", 9),
          ("ground-start-FXS", 8),
          ("low-cost-EandM", 6),
          ("low-cost-loop-start-FXO", 7),
          ("low-cost-loop-start-FXS", 5),
          ("not-available", 1),
          ("three-port", 10))
    )


_McmVNETChCfgInterfaceType_Type.__name__ = "Integer32"
_McmVNETChCfgInterfaceType_Object = MibTableColumn
mcmVNETChCfgInterfaceType = _McmVNETChCfgInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 1, 1, 5),
    _McmVNETChCfgInterfaceType_Type()
)
mcmVNETChCfgInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmVNETChCfgInterfaceType.setStatus("mandatory")
_McmVNETProfileCfgTable_Object = MibTable
mcmVNETProfileCfgTable = _McmVNETProfileCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 2)
)
if mibBuilder.loadTexts:
    mcmVNETProfileCfgTable.setStatus("mandatory")
_McmVNETProfileCfgEntry_Object = MibTableRow
mcmVNETProfileCfgEntry = _McmVNETProfileCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 2, 1)
)
mcmVNETProfileCfgEntry.setIndexNames(
    (0, "MICOM-4400-VOICE-NETWORK-MIB", "mcmVNETProfileCfgProfileNum"),
)
if mibBuilder.loadTexts:
    mcmVNETProfileCfgEntry.setStatus("mandatory")


class _McmVNETProfileCfgProfileNum_Type(Integer32):
    """Custom type mcmVNETProfileCfgProfileNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_McmVNETProfileCfgProfileNum_Type.__name__ = "Integer32"
_McmVNETProfileCfgProfileNum_Object = MibTableColumn
mcmVNETProfileCfgProfileNum = _McmVNETProfileCfgProfileNum_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 2, 1, 1),
    _McmVNETProfileCfgProfileNum_Type()
)
mcmVNETProfileCfgProfileNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmVNETProfileCfgProfileNum.setStatus("mandatory")


class _McmVNETProfileCfgMode_Type(Integer32):
    """Custom type mcmVNETProfileCfgMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("voiceFax", 1),
          ("voiceOnly", 2))
    )


_McmVNETProfileCfgMode_Type.__name__ = "Integer32"
_McmVNETProfileCfgMode_Object = MibTableColumn
mcmVNETProfileCfgMode = _McmVNETProfileCfgMode_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 2, 1, 2),
    _McmVNETProfileCfgMode_Type()
)
mcmVNETProfileCfgMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmVNETProfileCfgMode.setStatus("mandatory")


class _McmVNETProfileCfgDigitizingRate_Type(Integer32):
    """Custom type mcmVNETProfileCfgDigitizingRate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rateG729", 1),
          ("rateG729-8K-40MS", 2))
    )


_McmVNETProfileCfgDigitizingRate_Type.__name__ = "Integer32"
_McmVNETProfileCfgDigitizingRate_Object = MibTableColumn
mcmVNETProfileCfgDigitizingRate = _McmVNETProfileCfgDigitizingRate_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 2, 1, 3),
    _McmVNETProfileCfgDigitizingRate_Type()
)
mcmVNETProfileCfgDigitizingRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmVNETProfileCfgDigitizingRate.setStatus("mandatory")


class _McmVNETProfileCfgInputLevelGain_Type(Integer32):
    """Custom type mcmVNETProfileCfgInputLevelGain based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-15, 19),
    )


_McmVNETProfileCfgInputLevelGain_Type.__name__ = "Integer32"
_McmVNETProfileCfgInputLevelGain_Object = MibTableColumn
mcmVNETProfileCfgInputLevelGain = _McmVNETProfileCfgInputLevelGain_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 2, 1, 4),
    _McmVNETProfileCfgInputLevelGain_Type()
)
mcmVNETProfileCfgInputLevelGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmVNETProfileCfgInputLevelGain.setStatus("mandatory")


class _McmVNETProfileCfgOutputLevelAttn_Type(Integer32):
    """Custom type mcmVNETProfileCfgOutputLevelAttn based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-15, 25),
    )


_McmVNETProfileCfgOutputLevelAttn_Type.__name__ = "Integer32"
_McmVNETProfileCfgOutputLevelAttn_Object = MibTableColumn
mcmVNETProfileCfgOutputLevelAttn = _McmVNETProfileCfgOutputLevelAttn_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 2, 1, 5),
    _McmVNETProfileCfgOutputLevelAttn_Type()
)
mcmVNETProfileCfgOutputLevelAttn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmVNETProfileCfgOutputLevelAttn.setStatus("mandatory")


class _McmVNETProfileCfgBusyOutMode_Type(Integer32):
    """Custom type mcmVNETProfileCfgBusyOutMode based on Integer32"""
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
        *(("forceOff", 3),
          ("forceOn", 2),
          ("systemControlled", 1))
    )


_McmVNETProfileCfgBusyOutMode_Type.__name__ = "Integer32"
_McmVNETProfileCfgBusyOutMode_Object = MibTableColumn
mcmVNETProfileCfgBusyOutMode = _McmVNETProfileCfgBusyOutMode_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 2, 1, 6),
    _McmVNETProfileCfgBusyOutMode_Type()
)
mcmVNETProfileCfgBusyOutMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmVNETProfileCfgBusyOutMode.setStatus("mandatory")


class _McmVNETProfileCfgBandwidth_Type(Integer32):
    """Custom type mcmVNETProfileCfgBandwidth based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("continuous", 2),
          ("voiceActivated", 1))
    )


_McmVNETProfileCfgBandwidth_Type.__name__ = "Integer32"
_McmVNETProfileCfgBandwidth_Object = MibTableColumn
mcmVNETProfileCfgBandwidth = _McmVNETProfileCfgBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 2, 1, 7),
    _McmVNETProfileCfgBandwidth_Type()
)
mcmVNETProfileCfgBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmVNETProfileCfgBandwidth.setStatus("mandatory")


class _McmVNETProfileCfgBackground_Type(Integer32):
    """Custom type mcmVNETProfileCfgBackground based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("regenerated", 1),
          ("silence", 2))
    )


_McmVNETProfileCfgBackground_Type.__name__ = "Integer32"
_McmVNETProfileCfgBackground_Object = MibTableColumn
mcmVNETProfileCfgBackground = _McmVNETProfileCfgBackground_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 2, 1, 8),
    _McmVNETProfileCfgBackground_Type()
)
mcmVNETProfileCfgBackground.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmVNETProfileCfgBackground.setStatus("mandatory")


class _McmVNETProfileCfgBRIPulseRate_Type(Integer32):
    """Custom type mcmVNETProfileCfgBRIPulseRate based on Integer32"""
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
        *(("pulses10PerSec", 1),
          ("pulses125PerSec", 3),
          ("pulses20PerSec", 2))
    )


_McmVNETProfileCfgBRIPulseRate_Type.__name__ = "Integer32"
_McmVNETProfileCfgBRIPulseRate_Object = MibTableColumn
mcmVNETProfileCfgBRIPulseRate = _McmVNETProfileCfgBRIPulseRate_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 2, 1, 9),
    _McmVNETProfileCfgBRIPulseRate_Type()
)
mcmVNETProfileCfgBRIPulseRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmVNETProfileCfgBRIPulseRate.setStatus("obsolete")


class _McmVNETProfileCfgEMSigFormat_Type(Integer32):
    """Custom type mcmVNETProfileCfgEMSigFormat based on Integer32"""
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
        *(("dc", 1),
          ("pulsedDC", 3),
          ("tone2280", 2),
          ("winkStart", 4))
    )


_McmVNETProfileCfgEMSigFormat_Type.__name__ = "Integer32"
_McmVNETProfileCfgEMSigFormat_Object = MibTableColumn
mcmVNETProfileCfgEMSigFormat = _McmVNETProfileCfgEMSigFormat_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 2, 1, 10),
    _McmVNETProfileCfgEMSigFormat_Type()
)
mcmVNETProfileCfgEMSigFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmVNETProfileCfgEMSigFormat.setStatus("mandatory")


class _McmVNETProfileCfgFXSSigFormat_Type(Integer32):
    """Custom type mcmVNETProfileCfgFXSSigFormat based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("interruptedRing", 2),
          ("repeatedRing", 1))
    )


_McmVNETProfileCfgFXSSigFormat_Type.__name__ = "Integer32"
_McmVNETProfileCfgFXSSigFormat_Object = MibTableColumn
mcmVNETProfileCfgFXSSigFormat = _McmVNETProfileCfgFXSSigFormat_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 2, 1, 11),
    _McmVNETProfileCfgFXSSigFormat_Type()
)
mcmVNETProfileCfgFXSSigFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmVNETProfileCfgFXSSigFormat.setStatus("mandatory")


class _McmVNETProfileCfgDVMSigFormat_Type(Integer32):
    """Custom type mcmVNETProfileCfgDVMSigFormat based on Integer32"""
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
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("clearChannel", 4),
          ("dC5B", 5),
          ("dC5BInvert", 6),
          ("dC5RonTron", 9),
          ("israelCAS", 10),
          ("r2PUNCOM", 7),
          ("r2Q421", 8),
          ("spainCAS", 11),
          ("tieInvert", 2),
          ("tieTrunk", 1),
          ("tone2280", 3),
          ("winkStart", 12))
    )


_McmVNETProfileCfgDVMSigFormat_Type.__name__ = "Integer32"
_McmVNETProfileCfgDVMSigFormat_Object = MibTableColumn
mcmVNETProfileCfgDVMSigFormat = _McmVNETProfileCfgDVMSigFormat_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 2, 1, 12),
    _McmVNETProfileCfgDVMSigFormat_Type()
)
mcmVNETProfileCfgDVMSigFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmVNETProfileCfgDVMSigFormat.setStatus("mandatory")


class _McmVNETProfileCfgNumberOfRings_Type(Integer32):
    """Custom type mcmVNETProfileCfgNumberOfRings based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_McmVNETProfileCfgNumberOfRings_Type.__name__ = "Integer32"
_McmVNETProfileCfgNumberOfRings_Object = MibTableColumn
mcmVNETProfileCfgNumberOfRings = _McmVNETProfileCfgNumberOfRings_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 2, 1, 13),
    _McmVNETProfileCfgNumberOfRings_Type()
)
mcmVNETProfileCfgNumberOfRings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmVNETProfileCfgNumberOfRings.setStatus("mandatory")


class _McmVNETProfileCfgEMAnalOper_Type(Integer32):
    """Custom type mcmVNETProfileCfgEMAnalOper based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fourWire", 2),
          ("twoWire", 1))
    )


_McmVNETProfileCfgEMAnalOper_Type.__name__ = "Integer32"
_McmVNETProfileCfgEMAnalOper_Object = MibTableColumn
mcmVNETProfileCfgEMAnalOper = _McmVNETProfileCfgEMAnalOper_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 2, 1, 14),
    _McmVNETProfileCfgEMAnalOper_Type()
)
mcmVNETProfileCfgEMAnalOper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmVNETProfileCfgEMAnalOper.setStatus("mandatory")


class _McmVNETProfileCfgRingingFreq_Type(Integer32):
    """Custom type mcmVNETProfileCfgRingingFreq based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("freq25Hz", 1),
          ("freq50Hz", 2))
    )


_McmVNETProfileCfgRingingFreq_Type.__name__ = "Integer32"
_McmVNETProfileCfgRingingFreq_Object = MibTableColumn
mcmVNETProfileCfgRingingFreq = _McmVNETProfileCfgRingingFreq_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 2, 1, 15),
    _McmVNETProfileCfgRingingFreq_Type()
)
mcmVNETProfileCfgRingingFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmVNETProfileCfgRingingFreq.setStatus("mandatory")


class _McmVNETProfileCfgFaxDigRate_Type(Integer32):
    """Custom type mcmVNETProfileCfgFaxDigRate based on Integer32"""
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
        *(("rate2400", 2),
          ("rate4800", 3),
          ("rate7200", 4),
          ("rate9600", 5),
          ("voiceRate", 1))
    )


_McmVNETProfileCfgFaxDigRate_Type.__name__ = "Integer32"
_McmVNETProfileCfgFaxDigRate_Object = MibTableColumn
mcmVNETProfileCfgFaxDigRate = _McmVNETProfileCfgFaxDigRate_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 2, 1, 16),
    _McmVNETProfileCfgFaxDigRate_Type()
)
mcmVNETProfileCfgFaxDigRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmVNETProfileCfgFaxDigRate.setStatus("mandatory")


class _McmVNETProfileCfgDiscSupervision_Type(Integer32):
    """Custom type mcmVNETProfileCfgDiscSupervision based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("powerInterrupt", 2),
          ("tone", 1))
    )


_McmVNETProfileCfgDiscSupervision_Type.__name__ = "Integer32"
_McmVNETProfileCfgDiscSupervision_Object = MibTableColumn
mcmVNETProfileCfgDiscSupervision = _McmVNETProfileCfgDiscSupervision_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 2, 1, 17),
    _McmVNETProfileCfgDiscSupervision_Type()
)
mcmVNETProfileCfgDiscSupervision.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmVNETProfileCfgDiscSupervision.setStatus("mandatory")


class _McmVNETProfileCfgLineImpedance_Type(Integer32):
    """Custom type mcmVNETProfileCfgLineImpedance based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("complex", 2),
          ("impedance600Ohms", 1))
    )


_McmVNETProfileCfgLineImpedance_Type.__name__ = "Integer32"
_McmVNETProfileCfgLineImpedance_Object = MibTableColumn
mcmVNETProfileCfgLineImpedance = _McmVNETProfileCfgLineImpedance_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 2, 1, 18),
    _McmVNETProfileCfgLineImpedance_Type()
)
mcmVNETProfileCfgLineImpedance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmVNETProfileCfgLineImpedance.setStatus("mandatory")


class _McmVNETProfileCfgMaxOutputLevel_Type(Integer32):
    """Custom type mcmVNETProfileCfgMaxOutputLevel based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("plus7dBM", 2),
          ("zerodBMNominal", 1))
    )


_McmVNETProfileCfgMaxOutputLevel_Type.__name__ = "Integer32"
_McmVNETProfileCfgMaxOutputLevel_Object = MibTableColumn
mcmVNETProfileCfgMaxOutputLevel = _McmVNETProfileCfgMaxOutputLevel_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 2, 1, 19),
    _McmVNETProfileCfgMaxOutputLevel_Type()
)
mcmVNETProfileCfgMaxOutputLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmVNETProfileCfgMaxOutputLevel.setStatus("mandatory")


class _McmVNETProfileCfgRegenDelay_Type(Integer32):
    """Custom type mcmVNETProfileCfgRegenDelay based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_McmVNETProfileCfgRegenDelay_Type.__name__ = "Integer32"
_McmVNETProfileCfgRegenDelay_Object = MibTableColumn
mcmVNETProfileCfgRegenDelay = _McmVNETProfileCfgRegenDelay_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 2, 1, 20),
    _McmVNETProfileCfgRegenDelay_Type()
)
mcmVNETProfileCfgRegenDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmVNETProfileCfgRegenDelay.setStatus("mandatory")


class _McmVNETProfileCfgDialDigTimeLimit_Type(Integer32):
    """Custom type mcmVNETProfileCfgDialDigTimeLimit based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_McmVNETProfileCfgDialDigTimeLimit_Type.__name__ = "Integer32"
_McmVNETProfileCfgDialDigTimeLimit_Object = MibTableColumn
mcmVNETProfileCfgDialDigTimeLimit = _McmVNETProfileCfgDialDigTimeLimit_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 2, 1, 21),
    _McmVNETProfileCfgDialDigTimeLimit_Type()
)
mcmVNETProfileCfgDialDigTimeLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmVNETProfileCfgDialDigTimeLimit.setStatus("mandatory")


class _McmVNETProfileCfgMaxNumForDig_Type(Integer32):
    """Custom type mcmVNETProfileCfgMaxNumForDig based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 40),
    )


_McmVNETProfileCfgMaxNumForDig_Type.__name__ = "Integer32"
_McmVNETProfileCfgMaxNumForDig_Object = MibTableColumn
mcmVNETProfileCfgMaxNumForDig = _McmVNETProfileCfgMaxNumForDig_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 2, 1, 22),
    _McmVNETProfileCfgMaxNumForDig_Type()
)
mcmVNETProfileCfgMaxNumForDig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmVNETProfileCfgMaxNumForDig.setStatus("mandatory")


class _McmVNETProfileCfgRegenFormat_Type(Integer32):
    """Custom type mcmVNETProfileCfgRegenFormat based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dialPulse", 1),
          ("dtmf", 2))
    )


_McmVNETProfileCfgRegenFormat_Type.__name__ = "Integer32"
_McmVNETProfileCfgRegenFormat_Object = MibTableColumn
mcmVNETProfileCfgRegenFormat = _McmVNETProfileCfgRegenFormat_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 2, 1, 23),
    _McmVNETProfileCfgRegenFormat_Type()
)
mcmVNETProfileCfgRegenFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmVNETProfileCfgRegenFormat.setStatus("mandatory")


class _McmVNETProfileCfgCallProgTone_Type(Integer32):
    """Custom type mcmVNETProfileCfgCallProgTone based on Integer32"""
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
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("australia", 8),
          ("centralAmerica", 6),
          ("chile", 7),
          ("europe", 4),
          ("france", 5),
          ("japan", 2),
          ("northAmerica", 1),
          ("unitedKingdom", 3))
    )


_McmVNETProfileCfgCallProgTone_Type.__name__ = "Integer32"
_McmVNETProfileCfgCallProgTone_Object = MibTableColumn
mcmVNETProfileCfgCallProgTone = _McmVNETProfileCfgCallProgTone_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 2, 1, 24),
    _McmVNETProfileCfgCallProgTone_Type()
)
mcmVNETProfileCfgCallProgTone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmVNETProfileCfgCallProgTone.setStatus("mandatory")


class _McmVNETProfileCfgDTMFDetector_Type(Integer32):
    """Custom type mcmVNETProfileCfgDTMFDetector based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_McmVNETProfileCfgDTMFDetector_Type.__name__ = "Integer32"
_McmVNETProfileCfgDTMFDetector_Object = MibTableColumn
mcmVNETProfileCfgDTMFDetector = _McmVNETProfileCfgDTMFDetector_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 2, 1, 25),
    _McmVNETProfileCfgDTMFDetector_Type()
)
mcmVNETProfileCfgDTMFDetector.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmVNETProfileCfgDTMFDetector.setStatus("mandatory")


class _McmVNETProfileCfgJitters_Type(Integer32):
    """Custom type mcmVNETProfileCfgJitters based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_McmVNETProfileCfgJitters_Type.__name__ = "Integer32"
_McmVNETProfileCfgJitters_Object = MibTableColumn
mcmVNETProfileCfgJitters = _McmVNETProfileCfgJitters_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 2, 1, 26),
    _McmVNETProfileCfgJitters_Type()
)
mcmVNETProfileCfgJitters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmVNETProfileCfgJitters.setStatus("mandatory")


class _McmVNETProfileCfgEchoCanceller_Type(Integer32):
    """Custom type mcmVNETProfileCfgEchoCanceller based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_McmVNETProfileCfgEchoCanceller_Type.__name__ = "Integer32"
_McmVNETProfileCfgEchoCanceller_Object = MibTableColumn
mcmVNETProfileCfgEchoCanceller = _McmVNETProfileCfgEchoCanceller_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 2, 1, 27),
    _McmVNETProfileCfgEchoCanceller_Type()
)
mcmVNETProfileCfgEchoCanceller.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmVNETProfileCfgEchoCanceller.setStatus("mandatory")


class _McmVNETProfileCfgAutoGainControl_Type(Integer32):
    """Custom type mcmVNETProfileCfgAutoGainControl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_McmVNETProfileCfgAutoGainControl_Type.__name__ = "Integer32"
_McmVNETProfileCfgAutoGainControl_Object = MibTableColumn
mcmVNETProfileCfgAutoGainControl = _McmVNETProfileCfgAutoGainControl_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 2, 1, 28),
    _McmVNETProfileCfgAutoGainControl_Type()
)
mcmVNETProfileCfgAutoGainControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmVNETProfileCfgAutoGainControl.setStatus("mandatory")


class _McmVNETProfileCfgCompanderFormat_Type(Integer32):
    """Custom type mcmVNETProfileCfgCompanderFormat based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aLaw", 2),
          ("uLaw", 1))
    )


_McmVNETProfileCfgCompanderFormat_Type.__name__ = "Integer32"
_McmVNETProfileCfgCompanderFormat_Object = MibTableColumn
mcmVNETProfileCfgCompanderFormat = _McmVNETProfileCfgCompanderFormat_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 2, 1, 29),
    _McmVNETProfileCfgCompanderFormat_Type()
)
mcmVNETProfileCfgCompanderFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmVNETProfileCfgCompanderFormat.setStatus("mandatory")


class _McmVNETProfileCfgPremiumVoice_Type(Integer32):
    """Custom type mcmVNETProfileCfgPremiumVoice based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable-compress", 1),
          ("enable-notcompress", 2))
    )


_McmVNETProfileCfgPremiumVoice_Type.__name__ = "Integer32"
_McmVNETProfileCfgPremiumVoice_Object = MibTableColumn
mcmVNETProfileCfgPremiumVoice = _McmVNETProfileCfgPremiumVoice_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 2, 1, 30),
    _McmVNETProfileCfgPremiumVoice_Type()
)
mcmVNETProfileCfgPremiumVoice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmVNETProfileCfgPremiumVoice.setStatus("mandatory")


class _McmVNETProfileCfgEndOfDialChar_Type(Integer32):
    """Custom type mcmVNETProfileCfgEndOfDialChar based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_McmVNETProfileCfgEndOfDialChar_Type.__name__ = "Integer32"
_McmVNETProfileCfgEndOfDialChar_Object = MibTableColumn
mcmVNETProfileCfgEndOfDialChar = _McmVNETProfileCfgEndOfDialChar_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 2, 1, 31),
    _McmVNETProfileCfgEndOfDialChar_Type()
)
mcmVNETProfileCfgEndOfDialChar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmVNETProfileCfgEndOfDialChar.setStatus("mandatory")


class _McmVNETProfileCfgBckGrndNoiseLevel_Type(Integer32):
    """Custom type mcmVNETProfileCfgBckGrndNoiseLevel based on Integer32"""
    defaultValue = 2

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
        *(("neg25dbm0", 1),
          ("neg30dbm0", 2),
          ("neg35dbm0", 3),
          ("neg40dbm0", 4),
          ("neg45dbm0", 5))
    )


_McmVNETProfileCfgBckGrndNoiseLevel_Type.__name__ = "Integer32"
_McmVNETProfileCfgBckGrndNoiseLevel_Object = MibTableColumn
mcmVNETProfileCfgBckGrndNoiseLevel = _McmVNETProfileCfgBckGrndNoiseLevel_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 2, 1, 32),
    _McmVNETProfileCfgBckGrndNoiseLevel_Type()
)
mcmVNETProfileCfgBckGrndNoiseLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmVNETProfileCfgBckGrndNoiseLevel.setStatus("mandatory")


class _McmVNETProfileCfgSilenceHngOvrTime_Type(Integer32):
    """Custom type mcmVNETProfileCfgSilenceHngOvrTime based on Integer32"""
    defaultValue = 3

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
              8)
        )
    )
    namedValues = NamedValues(
        *(("msec100", 1),
          ("msec200", 2),
          ("msec300", 3),
          ("msec400", 4),
          ("msec500", 5),
          ("msec600", 6),
          ("msec700", 7),
          ("msec800", 8))
    )


_McmVNETProfileCfgSilenceHngOvrTime_Type.__name__ = "Integer32"
_McmVNETProfileCfgSilenceHngOvrTime_Object = MibTableColumn
mcmVNETProfileCfgSilenceHngOvrTime = _McmVNETProfileCfgSilenceHngOvrTime_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 2, 1, 33),
    _McmVNETProfileCfgSilenceHngOvrTime_Type()
)
mcmVNETProfileCfgSilenceHngOvrTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmVNETProfileCfgSilenceHngOvrTime.setStatus("mandatory")


class _McmVNETProfileCfgIdlePattern_Type(Integer32):
    """Custom type mcmVNETProfileCfgIdlePattern based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_McmVNETProfileCfgIdlePattern_Type.__name__ = "Integer32"
_McmVNETProfileCfgIdlePattern_Object = MibTableColumn
mcmVNETProfileCfgIdlePattern = _McmVNETProfileCfgIdlePattern_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 2, 1, 34),
    _McmVNETProfileCfgIdlePattern_Type()
)
mcmVNETProfileCfgIdlePattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmVNETProfileCfgIdlePattern.setStatus("mandatory")


class _McmVNETProfileCfgEcanFilterLength_Type(Integer32):
    """Custom type mcmVNETProfileCfgEcanFilterLength based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("length128", 1),
          ("length256", 2))
    )


_McmVNETProfileCfgEcanFilterLength_Type.__name__ = "Integer32"
_McmVNETProfileCfgEcanFilterLength_Object = MibTableColumn
mcmVNETProfileCfgEcanFilterLength = _McmVNETProfileCfgEcanFilterLength_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 2, 1, 35),
    _McmVNETProfileCfgEcanFilterLength_Type()
)
mcmVNETProfileCfgEcanFilterLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmVNETProfileCfgEcanFilterLength.setStatus("mandatory")


class _McmVNETProfileCfgEcanErlImprovement_Type(Integer32):
    """Custom type mcmVNETProfileCfgEcanErlImprovement based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-18, 0),
    )


_McmVNETProfileCfgEcanErlImprovement_Type.__name__ = "Integer32"
_McmVNETProfileCfgEcanErlImprovement_Object = MibTableColumn
mcmVNETProfileCfgEcanErlImprovement = _McmVNETProfileCfgEcanErlImprovement_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 2, 1, 36),
    _McmVNETProfileCfgEcanErlImprovement_Type()
)
mcmVNETProfileCfgEcanErlImprovement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmVNETProfileCfgEcanErlImprovement.setStatus("mandatory")


class _McmVNETProfileCfgNoiseFloorOffset_Type(Integer32):
    """Custom type mcmVNETProfileCfgNoiseFloorOffset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_McmVNETProfileCfgNoiseFloorOffset_Type.__name__ = "Integer32"
_McmVNETProfileCfgNoiseFloorOffset_Object = MibTableColumn
mcmVNETProfileCfgNoiseFloorOffset = _McmVNETProfileCfgNoiseFloorOffset_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 2, 1, 37),
    _McmVNETProfileCfgNoiseFloorOffset_Type()
)
mcmVNETProfileCfgNoiseFloorOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmVNETProfileCfgNoiseFloorOffset.setStatus("mandatory")


class _McmVNETProfileCfgDtmfGenBurstLength_Type(Integer32):
    """Custom type mcmVNETProfileCfgDtmfGenBurstLength based on Integer32"""
    defaultValue = 4

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
        *(("time100msec", 4),
          ("time50msec", 1),
          ("time60msec", 2),
          ("time70msec", 3))
    )


_McmVNETProfileCfgDtmfGenBurstLength_Type.__name__ = "Integer32"
_McmVNETProfileCfgDtmfGenBurstLength_Object = MibTableColumn
mcmVNETProfileCfgDtmfGenBurstLength = _McmVNETProfileCfgDtmfGenBurstLength_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 2, 1, 38),
    _McmVNETProfileCfgDtmfGenBurstLength_Type()
)
mcmVNETProfileCfgDtmfGenBurstLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmVNETProfileCfgDtmfGenBurstLength.setStatus("mandatory")


class _McmVNETProfileCfgDtmRegenBurstLength_Type(Integer32):
    """Custom type mcmVNETProfileCfgDtmRegenBurstLength based on Integer32"""
    defaultValue = 4

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
        *(("time100msec", 4),
          ("time50msec", 1),
          ("time60msec", 2),
          ("time70msec", 3))
    )


_McmVNETProfileCfgDtmRegenBurstLength_Type.__name__ = "Integer32"
_McmVNETProfileCfgDtmRegenBurstLength_Object = MibTableColumn
mcmVNETProfileCfgDtmRegenBurstLength = _McmVNETProfileCfgDtmRegenBurstLength_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 2, 1, 39),
    _McmVNETProfileCfgDtmRegenBurstLength_Type()
)
mcmVNETProfileCfgDtmRegenBurstLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmVNETProfileCfgDtmRegenBurstLength.setStatus("mandatory")
_McmVNETSwProfCfgTable_Object = MibTable
mcmVNETSwProfCfgTable = _McmVNETSwProfCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 3)
)
if mibBuilder.loadTexts:
    mcmVNETSwProfCfgTable.setStatus("mandatory")
_McmVNETSwProfCfgEntry_Object = MibTableRow
mcmVNETSwProfCfgEntry = _McmVNETSwProfCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 3, 1)
)
mcmVNETSwProfCfgEntry.setIndexNames(
    (0, "MICOM-4400-VOICE-NETWORK-MIB", "mcmVNETSwProfCfgProfileNum"),
)
if mibBuilder.loadTexts:
    mcmVNETSwProfCfgEntry.setStatus("mandatory")


class _McmVNETSwProfCfgProfileNum_Type(Integer32):
    """Custom type mcmVNETSwProfCfgProfileNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_McmVNETSwProfCfgProfileNum_Type.__name__ = "Integer32"
_McmVNETSwProfCfgProfileNum_Object = MibTableColumn
mcmVNETSwProfCfgProfileNum = _McmVNETSwProfCfgProfileNum_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 3, 1, 1),
    _McmVNETSwProfCfgProfileNum_Type()
)
mcmVNETSwProfCfgProfileNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmVNETSwProfCfgProfileNum.setStatus("mandatory")


class _McmVNETSwProfCfgOutCallRestrict_Type(Integer32):
    """Custom type mcmVNETSwProfCfgOutCallRestrict based on Integer32"""
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
        *(("bothCUGandRCCall", 4),
          ("closedUserGroupCall", 2),
          ("inhibitAll", 5),
          ("noRestriction", 1),
          ("restrictionClassCall", 3))
    )


_McmVNETSwProfCfgOutCallRestrict_Type.__name__ = "Integer32"
_McmVNETSwProfCfgOutCallRestrict_Object = MibTableColumn
mcmVNETSwProfCfgOutCallRestrict = _McmVNETSwProfCfgOutCallRestrict_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 3, 1, 2),
    _McmVNETSwProfCfgOutCallRestrict_Type()
)
mcmVNETSwProfCfgOutCallRestrict.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmVNETSwProfCfgOutCallRestrict.setStatus("mandatory")


class _McmVNETSwProfCfgInCallRestrict_Type(Integer32):
    """Custom type mcmVNETSwProfCfgInCallRestrict based on Integer32"""
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
        *(("cUGandPublicClassInhibit", 4),
          ("checkCUGID", 2),
          ("checkRestrictionClassCode", 3),
          ("inhibitAll", 5),
          ("noRestriction", 1))
    )


_McmVNETSwProfCfgInCallRestrict_Type.__name__ = "Integer32"
_McmVNETSwProfCfgInCallRestrict_Object = MibTableColumn
mcmVNETSwProfCfgInCallRestrict = _McmVNETSwProfCfgInCallRestrict_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 3, 1, 3),
    _McmVNETSwProfCfgInCallRestrict_Type()
)
mcmVNETSwProfCfgInCallRestrict.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmVNETSwProfCfgInCallRestrict.setStatus("mandatory")


class _McmVNETSwProfCfgCUGID_Type(Integer32):
    """Custom type mcmVNETSwProfCfgCUGID based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_McmVNETSwProfCfgCUGID_Type.__name__ = "Integer32"
_McmVNETSwProfCfgCUGID_Object = MibTableColumn
mcmVNETSwProfCfgCUGID = _McmVNETSwProfCfgCUGID_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 3, 1, 4),
    _McmVNETSwProfCfgCUGID_Type()
)
mcmVNETSwProfCfgCUGID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmVNETSwProfCfgCUGID.setStatus("mandatory")


class _McmVNETSwProfCfgRestrictClassCd_Type(Integer32):
    """Custom type mcmVNETSwProfCfgRestrictClassCd based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_McmVNETSwProfCfgRestrictClassCd_Type.__name__ = "Integer32"
_McmVNETSwProfCfgRestrictClassCd_Object = MibTableColumn
mcmVNETSwProfCfgRestrictClassCd = _McmVNETSwProfCfgRestrictClassCd_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 3, 1, 5),
    _McmVNETSwProfCfgRestrictClassCd_Type()
)
mcmVNETSwProfCfgRestrictClassCd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmVNETSwProfCfgRestrictClassCd.setStatus("mandatory")


class _McmVNETSwProfCfgAutoCallEntNum_Type(Integer32):
    """Custom type mcmVNETSwProfCfgAutoCallEntNum based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_McmVNETSwProfCfgAutoCallEntNum_Type.__name__ = "Integer32"
_McmVNETSwProfCfgAutoCallEntNum_Object = MibTableColumn
mcmVNETSwProfCfgAutoCallEntNum = _McmVNETSwProfCfgAutoCallEntNum_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 3, 1, 6),
    _McmVNETSwProfCfgAutoCallEntNum_Type()
)
mcmVNETSwProfCfgAutoCallEntNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmVNETSwProfCfgAutoCallEntNum.setStatus("mandatory")


class _McmVNETSwProfCfgCallNegStrategy_Type(Integer32):
    """Custom type mcmVNETSwProfCfgCallNegStrategy based on Integer32"""
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
        *(("bandwidth", 2),
          ("delay", 3),
          ("specific", 1))
    )


_McmVNETSwProfCfgCallNegStrategy_Type.__name__ = "Integer32"
_McmVNETSwProfCfgCallNegStrategy_Object = MibTableColumn
mcmVNETSwProfCfgCallNegStrategy = _McmVNETSwProfCfgCallNegStrategy_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 3, 1, 7),
    _McmVNETSwProfCfgCallNegStrategy_Type()
)
mcmVNETSwProfCfgCallNegStrategy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmVNETSwProfCfgCallNegStrategy.setStatus("mandatory")


class _McmVNETSwProfCfgTransmitPriority_Type(Integer32):
    """Custom type mcmVNETSwProfCfgTransmitPriority based on Integer32"""
    defaultValue = 11

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_McmVNETSwProfCfgTransmitPriority_Type.__name__ = "Integer32"
_McmVNETSwProfCfgTransmitPriority_Object = MibTableColumn
mcmVNETSwProfCfgTransmitPriority = _McmVNETSwProfCfgTransmitPriority_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 3, 1, 8),
    _McmVNETSwProfCfgTransmitPriority_Type()
)
mcmVNETSwProfCfgTransmitPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmVNETSwProfCfgTransmitPriority.setStatus("mandatory")


class _McmVNETSwProfCfgAutoCallType_Type(Integer32):
    """Custom type mcmVNETSwProfCfgAutoCallType based on Integer32"""
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
        *(("masterHootnHoller", 2),
          ("normal", 1),
          ("slaveHootnHoller", 3))
    )


_McmVNETSwProfCfgAutoCallType_Type.__name__ = "Integer32"
_McmVNETSwProfCfgAutoCallType_Object = MibTableColumn
mcmVNETSwProfCfgAutoCallType = _McmVNETSwProfCfgAutoCallType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 3, 1, 9),
    _McmVNETSwProfCfgAutoCallType_Type()
)
mcmVNETSwProfCfgAutoCallType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmVNETSwProfCfgAutoCallType.setStatus("mandatory")


class _McmVNETSwProfCfgAddServerSelect_Type(Integer32):
    """Custom type mcmVNETSwProfCfgAddServerSelect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nas", 1),
          ("vncs", 2))
    )


_McmVNETSwProfCfgAddServerSelect_Type.__name__ = "Integer32"
_McmVNETSwProfCfgAddServerSelect_Object = MibTableColumn
mcmVNETSwProfCfgAddServerSelect = _McmVNETSwProfCfgAddServerSelect_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 3, 1, 10),
    _McmVNETSwProfCfgAddServerSelect_Type()
)
mcmVNETSwProfCfgAddServerSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmVNETSwProfCfgAddServerSelect.setStatus("mandatory")


class _McmVNETSwProfCfgOutCallMode_Type(Integer32):
    """Custom type mcmVNETSwProfCfgOutCallMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("enblock-only", 1))
    )


_McmVNETSwProfCfgOutCallMode_Type.__name__ = "Integer32"
_McmVNETSwProfCfgOutCallMode_Object = MibTableColumn
mcmVNETSwProfCfgOutCallMode = _McmVNETSwProfCfgOutCallMode_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 3, 1, 11),
    _McmVNETSwProfCfgOutCallMode_Type()
)
mcmVNETSwProfCfgOutCallMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmVNETSwProfCfgOutCallMode.setStatus("mandatory")
_McmVNETIngressDigFilterTable_Object = MibTable
mcmVNETIngressDigFilterTable = _McmVNETIngressDigFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 4)
)
if mibBuilder.loadTexts:
    mcmVNETIngressDigFilterTable.setStatus("mandatory")
_McmVNETIngressDigFilterEntry_Object = MibTableRow
mcmVNETIngressDigFilterEntry = _McmVNETIngressDigFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 4, 1)
)
mcmVNETIngressDigFilterEntry.setIndexNames(
    (0, "MICOM-4400-VOICE-NETWORK-MIB", "mcmVNETIngressDigFilterIndex"),
)
if mibBuilder.loadTexts:
    mcmVNETIngressDigFilterEntry.setStatus("mandatory")


class _McmVNETIngressDigFilterIndex_Type(Integer32):
    """Custom type mcmVNETIngressDigFilterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_McmVNETIngressDigFilterIndex_Type.__name__ = "Integer32"
_McmVNETIngressDigFilterIndex_Object = MibTableColumn
mcmVNETIngressDigFilterIndex = _McmVNETIngressDigFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 4, 1, 1),
    _McmVNETIngressDigFilterIndex_Type()
)
mcmVNETIngressDigFilterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmVNETIngressDigFilterIndex.setStatus("mandatory")


class _McmVNETIngressDigFilterIngressNum_Type(DisplayString):
    """Custom type mcmVNETIngressDigFilterIngressNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_McmVNETIngressDigFilterIngressNum_Type.__name__ = "DisplayString"
_McmVNETIngressDigFilterIngressNum_Object = MibTableColumn
mcmVNETIngressDigFilterIngressNum = _McmVNETIngressDigFilterIngressNum_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 4, 1, 2),
    _McmVNETIngressDigFilterIngressNum_Type()
)
mcmVNETIngressDigFilterIngressNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmVNETIngressDigFilterIngressNum.setStatus("mandatory")


class _McmVNETIngressDigFilterManipString_Type(DisplayString):
    """Custom type mcmVNETIngressDigFilterManipString based on DisplayString"""
    defaultValue = OctetString("#")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_McmVNETIngressDigFilterManipString_Type.__name__ = "DisplayString"
_McmVNETIngressDigFilterManipString_Object = MibTableColumn
mcmVNETIngressDigFilterManipString = _McmVNETIngressDigFilterManipString_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 4, 1, 3),
    _McmVNETIngressDigFilterManipString_Type()
)
mcmVNETIngressDigFilterManipString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmVNETIngressDigFilterManipString.setStatus("mandatory")
_McmVNETEgressDigManipTable_Object = MibTable
mcmVNETEgressDigManipTable = _McmVNETEgressDigManipTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 5)
)
if mibBuilder.loadTexts:
    mcmVNETEgressDigManipTable.setStatus("mandatory")
_McmVNETEgressDigManipEntry_Object = MibTableRow
mcmVNETEgressDigManipEntry = _McmVNETEgressDigManipEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 5, 1)
)
mcmVNETEgressDigManipEntry.setIndexNames(
    (0, "MICOM-4400-VOICE-NETWORK-MIB", "mcmVNETEgressDigManipIndex"),
)
if mibBuilder.loadTexts:
    mcmVNETEgressDigManipEntry.setStatus("mandatory")


class _McmVNETEgressDigManipIndex_Type(Integer32):
    """Custom type mcmVNETEgressDigManipIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_McmVNETEgressDigManipIndex_Type.__name__ = "Integer32"
_McmVNETEgressDigManipIndex_Object = MibTableColumn
mcmVNETEgressDigManipIndex = _McmVNETEgressDigManipIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 5, 1, 1),
    _McmVNETEgressDigManipIndex_Type()
)
mcmVNETEgressDigManipIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmVNETEgressDigManipIndex.setStatus("mandatory")


class _McmVNETEgressDigManipPhoneNum_Type(DisplayString):
    """Custom type mcmVNETEgressDigManipPhoneNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_McmVNETEgressDigManipPhoneNum_Type.__name__ = "DisplayString"
_McmVNETEgressDigManipPhoneNum_Object = MibTableColumn
mcmVNETEgressDigManipPhoneNum = _McmVNETEgressDigManipPhoneNum_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 5, 1, 2),
    _McmVNETEgressDigManipPhoneNum_Type()
)
mcmVNETEgressDigManipPhoneNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmVNETEgressDigManipPhoneNum.setStatus("mandatory")


class _McmVNETEgressDigManipString_Type(DisplayString):
    """Custom type mcmVNETEgressDigManipString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_McmVNETEgressDigManipString_Type.__name__ = "DisplayString"
_McmVNETEgressDigManipString_Object = MibTableColumn
mcmVNETEgressDigManipString = _McmVNETEgressDigManipString_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 5, 1, 3),
    _McmVNETEgressDigManipString_Type()
)
mcmVNETEgressDigManipString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmVNETEgressDigManipString.setStatus("mandatory")


class _McmVNETEgressDigManipChIDList_Type(DisplayString):
    """Custom type mcmVNETEgressDigManipChIDList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 70),
    )


_McmVNETEgressDigManipChIDList_Type.__name__ = "DisplayString"
_McmVNETEgressDigManipChIDList_Object = MibTableColumn
mcmVNETEgressDigManipChIDList = _McmVNETEgressDigManipChIDList_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 5, 1, 4),
    _McmVNETEgressDigManipChIDList_Type()
)
mcmVNETEgressDigManipChIDList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmVNETEgressDigManipChIDList.setStatus("mandatory")
_NvmVNETChCfgTable_Object = MibTable
nvmVNETChCfgTable = _NvmVNETChCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 6)
)
if mibBuilder.loadTexts:
    nvmVNETChCfgTable.setStatus("mandatory")
_NvmVNETChCfgEntry_Object = MibTableRow
nvmVNETChCfgEntry = _NvmVNETChCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 6, 1)
)
nvmVNETChCfgEntry.setIndexNames(
    (0, "MICOM-4400-VOICE-NETWORK-MIB", "nvmVNETChCfgLimID"),
    (0, "MICOM-4400-VOICE-NETWORK-MIB", "nvmVNETChCfgChannelID"),
)
if mibBuilder.loadTexts:
    nvmVNETChCfgEntry.setStatus("mandatory")


class _NvmVNETChCfgLimID_Type(Integer32):
    """Custom type nvmVNETChCfgLimID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
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
        *(("lim1", 2),
          ("lim2", 3),
          ("lim3", 4),
          ("lim4", 5),
          ("limB", 6),
          ("limC", 7),
          ("limD", 8),
          ("limE", 9))
    )


_NvmVNETChCfgLimID_Type.__name__ = "Integer32"
_NvmVNETChCfgLimID_Object = MibTableColumn
nvmVNETChCfgLimID = _NvmVNETChCfgLimID_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 6, 1, 1),
    _NvmVNETChCfgLimID_Type()
)
nvmVNETChCfgLimID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmVNETChCfgLimID.setStatus("mandatory")


class _NvmVNETChCfgChannelID_Type(Integer32):
    """Custom type nvmVNETChCfgChannelID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_NvmVNETChCfgChannelID_Type.__name__ = "Integer32"
_NvmVNETChCfgChannelID_Object = MibTableColumn
nvmVNETChCfgChannelID = _NvmVNETChCfgChannelID_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 6, 1, 2),
    _NvmVNETChCfgChannelID_Type()
)
nvmVNETChCfgChannelID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmVNETChCfgChannelID.setStatus("mandatory")


class _NvmVNETChCfgVoiceProfile_Type(Integer32):
    """Custom type nvmVNETChCfgVoiceProfile based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_NvmVNETChCfgVoiceProfile_Type.__name__ = "Integer32"
_NvmVNETChCfgVoiceProfile_Object = MibTableColumn
nvmVNETChCfgVoiceProfile = _NvmVNETChCfgVoiceProfile_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 6, 1, 3),
    _NvmVNETChCfgVoiceProfile_Type()
)
nvmVNETChCfgVoiceProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmVNETChCfgVoiceProfile.setStatus("mandatory")


class _NvmVNETChCfgSwitchingProfile_Type(Integer32):
    """Custom type nvmVNETChCfgSwitchingProfile based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_NvmVNETChCfgSwitchingProfile_Type.__name__ = "Integer32"
_NvmVNETChCfgSwitchingProfile_Object = MibTableColumn
nvmVNETChCfgSwitchingProfile = _NvmVNETChCfgSwitchingProfile_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 6, 1, 4),
    _NvmVNETChCfgSwitchingProfile_Type()
)
nvmVNETChCfgSwitchingProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmVNETChCfgSwitchingProfile.setStatus("mandatory")


class _NvmVNETChCfgInterfaceType_Type(Integer32):
    """Custom type nvmVNETChCfgInterfaceType based on Integer32"""
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
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("bri", 12),
          ("dvm", 11),
          ("enhanced-EandM", 3),
          ("enhanced-loop-start-FXO", 4),
          ("enhanced-loop-start-FXS", 2),
          ("ground-start-FXO", 9),
          ("ground-start-FXS", 8),
          ("low-cost-EandM", 6),
          ("low-cost-loop-start-FXO", 7),
          ("low-cost-loop-start-FXS", 5),
          ("not-available", 1),
          ("three-port", 10))
    )


_NvmVNETChCfgInterfaceType_Type.__name__ = "Integer32"
_NvmVNETChCfgInterfaceType_Object = MibTableColumn
nvmVNETChCfgInterfaceType = _NvmVNETChCfgInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 6, 1, 5),
    _NvmVNETChCfgInterfaceType_Type()
)
nvmVNETChCfgInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmVNETChCfgInterfaceType.setStatus("mandatory")
_NvmVNETProfileCfgTable_Object = MibTable
nvmVNETProfileCfgTable = _NvmVNETProfileCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 7)
)
if mibBuilder.loadTexts:
    nvmVNETProfileCfgTable.setStatus("mandatory")
_NvmVNETProfileCfgEntry_Object = MibTableRow
nvmVNETProfileCfgEntry = _NvmVNETProfileCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 7, 1)
)
nvmVNETProfileCfgEntry.setIndexNames(
    (0, "MICOM-4400-VOICE-NETWORK-MIB", "nvmVNETProfileCfgProfileNum"),
)
if mibBuilder.loadTexts:
    nvmVNETProfileCfgEntry.setStatus("mandatory")


class _NvmVNETProfileCfgProfileNum_Type(Integer32):
    """Custom type nvmVNETProfileCfgProfileNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_NvmVNETProfileCfgProfileNum_Type.__name__ = "Integer32"
_NvmVNETProfileCfgProfileNum_Object = MibTableColumn
nvmVNETProfileCfgProfileNum = _NvmVNETProfileCfgProfileNum_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 7, 1, 1),
    _NvmVNETProfileCfgProfileNum_Type()
)
nvmVNETProfileCfgProfileNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmVNETProfileCfgProfileNum.setStatus("mandatory")


class _NvmVNETProfileCfgMode_Type(Integer32):
    """Custom type nvmVNETProfileCfgMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("voiceFax", 1),
          ("voiceOnly", 2))
    )


_NvmVNETProfileCfgMode_Type.__name__ = "Integer32"
_NvmVNETProfileCfgMode_Object = MibTableColumn
nvmVNETProfileCfgMode = _NvmVNETProfileCfgMode_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 7, 1, 2),
    _NvmVNETProfileCfgMode_Type()
)
nvmVNETProfileCfgMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmVNETProfileCfgMode.setStatus("mandatory")


class _NvmVNETProfileCfgDigitizingRate_Type(Integer32):
    """Custom type nvmVNETProfileCfgDigitizingRate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rateG729", 1),
          ("rateG729-8k-40ms", 2))
    )


_NvmVNETProfileCfgDigitizingRate_Type.__name__ = "Integer32"
_NvmVNETProfileCfgDigitizingRate_Object = MibTableColumn
nvmVNETProfileCfgDigitizingRate = _NvmVNETProfileCfgDigitizingRate_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 7, 1, 3),
    _NvmVNETProfileCfgDigitizingRate_Type()
)
nvmVNETProfileCfgDigitizingRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmVNETProfileCfgDigitizingRate.setStatus("mandatory")


class _NvmVNETProfileCfgInputLevelGain_Type(Integer32):
    """Custom type nvmVNETProfileCfgInputLevelGain based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-15, 19),
    )


_NvmVNETProfileCfgInputLevelGain_Type.__name__ = "Integer32"
_NvmVNETProfileCfgInputLevelGain_Object = MibTableColumn
nvmVNETProfileCfgInputLevelGain = _NvmVNETProfileCfgInputLevelGain_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 7, 1, 4),
    _NvmVNETProfileCfgInputLevelGain_Type()
)
nvmVNETProfileCfgInputLevelGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmVNETProfileCfgInputLevelGain.setStatus("mandatory")


class _NvmVNETProfileCfgOutputLevelAttn_Type(Integer32):
    """Custom type nvmVNETProfileCfgOutputLevelAttn based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-15, 25),
    )


_NvmVNETProfileCfgOutputLevelAttn_Type.__name__ = "Integer32"
_NvmVNETProfileCfgOutputLevelAttn_Object = MibTableColumn
nvmVNETProfileCfgOutputLevelAttn = _NvmVNETProfileCfgOutputLevelAttn_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 7, 1, 5),
    _NvmVNETProfileCfgOutputLevelAttn_Type()
)
nvmVNETProfileCfgOutputLevelAttn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmVNETProfileCfgOutputLevelAttn.setStatus("mandatory")


class _NvmVNETProfileCfgBusyOutMode_Type(Integer32):
    """Custom type nvmVNETProfileCfgBusyOutMode based on Integer32"""
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
        *(("forceOff", 3),
          ("forceOn", 2),
          ("systemControlled", 1))
    )


_NvmVNETProfileCfgBusyOutMode_Type.__name__ = "Integer32"
_NvmVNETProfileCfgBusyOutMode_Object = MibTableColumn
nvmVNETProfileCfgBusyOutMode = _NvmVNETProfileCfgBusyOutMode_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 7, 1, 6),
    _NvmVNETProfileCfgBusyOutMode_Type()
)
nvmVNETProfileCfgBusyOutMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmVNETProfileCfgBusyOutMode.setStatus("mandatory")


class _NvmVNETProfileCfgBandwidth_Type(Integer32):
    """Custom type nvmVNETProfileCfgBandwidth based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("continuous", 2),
          ("voiceActivated", 1))
    )


_NvmVNETProfileCfgBandwidth_Type.__name__ = "Integer32"
_NvmVNETProfileCfgBandwidth_Object = MibTableColumn
nvmVNETProfileCfgBandwidth = _NvmVNETProfileCfgBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 7, 1, 7),
    _NvmVNETProfileCfgBandwidth_Type()
)
nvmVNETProfileCfgBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmVNETProfileCfgBandwidth.setStatus("mandatory")


class _NvmVNETProfileCfgBackground_Type(Integer32):
    """Custom type nvmVNETProfileCfgBackground based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("regenerated", 1),
          ("silence", 2))
    )


_NvmVNETProfileCfgBackground_Type.__name__ = "Integer32"
_NvmVNETProfileCfgBackground_Object = MibTableColumn
nvmVNETProfileCfgBackground = _NvmVNETProfileCfgBackground_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 7, 1, 8),
    _NvmVNETProfileCfgBackground_Type()
)
nvmVNETProfileCfgBackground.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmVNETProfileCfgBackground.setStatus("mandatory")


class _NvmVNETProfileCfgBRIPulseRate_Type(Integer32):
    """Custom type nvmVNETProfileCfgBRIPulseRate based on Integer32"""
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
        *(("pulses10PerSec", 1),
          ("pulses125PerSec", 3),
          ("pulses20PerSec", 2))
    )


_NvmVNETProfileCfgBRIPulseRate_Type.__name__ = "Integer32"
_NvmVNETProfileCfgBRIPulseRate_Object = MibTableColumn
nvmVNETProfileCfgBRIPulseRate = _NvmVNETProfileCfgBRIPulseRate_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 7, 1, 9),
    _NvmVNETProfileCfgBRIPulseRate_Type()
)
nvmVNETProfileCfgBRIPulseRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmVNETProfileCfgBRIPulseRate.setStatus("obsolete")


class _NvmVNETProfileCfgEMSigFormat_Type(Integer32):
    """Custom type nvmVNETProfileCfgEMSigFormat based on Integer32"""
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
        *(("dc", 1),
          ("pulsedDC", 3),
          ("tone2280", 2),
          ("winkStart", 4))
    )


_NvmVNETProfileCfgEMSigFormat_Type.__name__ = "Integer32"
_NvmVNETProfileCfgEMSigFormat_Object = MibTableColumn
nvmVNETProfileCfgEMSigFormat = _NvmVNETProfileCfgEMSigFormat_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 7, 1, 10),
    _NvmVNETProfileCfgEMSigFormat_Type()
)
nvmVNETProfileCfgEMSigFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmVNETProfileCfgEMSigFormat.setStatus("mandatory")


class _NvmVNETProfileCfgFXSSigFormat_Type(Integer32):
    """Custom type nvmVNETProfileCfgFXSSigFormat based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("interruptedRing", 2),
          ("repeatedRing", 1))
    )


_NvmVNETProfileCfgFXSSigFormat_Type.__name__ = "Integer32"
_NvmVNETProfileCfgFXSSigFormat_Object = MibTableColumn
nvmVNETProfileCfgFXSSigFormat = _NvmVNETProfileCfgFXSSigFormat_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 7, 1, 11),
    _NvmVNETProfileCfgFXSSigFormat_Type()
)
nvmVNETProfileCfgFXSSigFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmVNETProfileCfgFXSSigFormat.setStatus("mandatory")


class _NvmVNETProfileCfgDVMSigFormat_Type(Integer32):
    """Custom type nvmVNETProfileCfgDVMSigFormat based on Integer32"""
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
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("clearChannel", 4),
          ("dC5B", 5),
          ("dC5BInvert", 6),
          ("dC5RonTron", 9),
          ("israelCAS", 10),
          ("r2PUNCOM", 7),
          ("r2Q421", 8),
          ("spainCAS", 11),
          ("tieInvert", 2),
          ("tieTrunk", 1),
          ("tone2280", 3),
          ("winkStart", 12))
    )


_NvmVNETProfileCfgDVMSigFormat_Type.__name__ = "Integer32"
_NvmVNETProfileCfgDVMSigFormat_Object = MibTableColumn
nvmVNETProfileCfgDVMSigFormat = _NvmVNETProfileCfgDVMSigFormat_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 7, 1, 12),
    _NvmVNETProfileCfgDVMSigFormat_Type()
)
nvmVNETProfileCfgDVMSigFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmVNETProfileCfgDVMSigFormat.setStatus("mandatory")


class _NvmVNETProfileCfgNumberOfRings_Type(Integer32):
    """Custom type nvmVNETProfileCfgNumberOfRings based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_NvmVNETProfileCfgNumberOfRings_Type.__name__ = "Integer32"
_NvmVNETProfileCfgNumberOfRings_Object = MibTableColumn
nvmVNETProfileCfgNumberOfRings = _NvmVNETProfileCfgNumberOfRings_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 7, 1, 13),
    _NvmVNETProfileCfgNumberOfRings_Type()
)
nvmVNETProfileCfgNumberOfRings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmVNETProfileCfgNumberOfRings.setStatus("mandatory")


class _NvmVNETProfileCfgEMAnalOper_Type(Integer32):
    """Custom type nvmVNETProfileCfgEMAnalOper based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fourWire", 2),
          ("twoWire", 1))
    )


_NvmVNETProfileCfgEMAnalOper_Type.__name__ = "Integer32"
_NvmVNETProfileCfgEMAnalOper_Object = MibTableColumn
nvmVNETProfileCfgEMAnalOper = _NvmVNETProfileCfgEMAnalOper_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 7, 1, 14),
    _NvmVNETProfileCfgEMAnalOper_Type()
)
nvmVNETProfileCfgEMAnalOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmVNETProfileCfgEMAnalOper.setStatus("mandatory")


class _NvmVNETProfileCfgRingingFreq_Type(Integer32):
    """Custom type nvmVNETProfileCfgRingingFreq based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("freq25Hz", 1),
          ("freq50Hz", 2))
    )


_NvmVNETProfileCfgRingingFreq_Type.__name__ = "Integer32"
_NvmVNETProfileCfgRingingFreq_Object = MibTableColumn
nvmVNETProfileCfgRingingFreq = _NvmVNETProfileCfgRingingFreq_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 7, 1, 15),
    _NvmVNETProfileCfgRingingFreq_Type()
)
nvmVNETProfileCfgRingingFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmVNETProfileCfgRingingFreq.setStatus("mandatory")


class _NvmVNETProfileCfgFaxDigRate_Type(Integer32):
    """Custom type nvmVNETProfileCfgFaxDigRate based on Integer32"""
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
        *(("rate2400", 2),
          ("rate4800", 3),
          ("rate7200", 4),
          ("rate9600", 5),
          ("voiceRate", 1))
    )


_NvmVNETProfileCfgFaxDigRate_Type.__name__ = "Integer32"
_NvmVNETProfileCfgFaxDigRate_Object = MibTableColumn
nvmVNETProfileCfgFaxDigRate = _NvmVNETProfileCfgFaxDigRate_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 7, 1, 16),
    _NvmVNETProfileCfgFaxDigRate_Type()
)
nvmVNETProfileCfgFaxDigRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmVNETProfileCfgFaxDigRate.setStatus("mandatory")


class _NvmVNETProfileCfgDiscSupervision_Type(Integer32):
    """Custom type nvmVNETProfileCfgDiscSupervision based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("powerInterrupt", 2),
          ("tone", 1))
    )


_NvmVNETProfileCfgDiscSupervision_Type.__name__ = "Integer32"
_NvmVNETProfileCfgDiscSupervision_Object = MibTableColumn
nvmVNETProfileCfgDiscSupervision = _NvmVNETProfileCfgDiscSupervision_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 7, 1, 17),
    _NvmVNETProfileCfgDiscSupervision_Type()
)
nvmVNETProfileCfgDiscSupervision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmVNETProfileCfgDiscSupervision.setStatus("mandatory")


class _NvmVNETProfileCfgLineImpedance_Type(Integer32):
    """Custom type nvmVNETProfileCfgLineImpedance based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("complex", 2),
          ("impedance600Ohms", 1))
    )


_NvmVNETProfileCfgLineImpedance_Type.__name__ = "Integer32"
_NvmVNETProfileCfgLineImpedance_Object = MibTableColumn
nvmVNETProfileCfgLineImpedance = _NvmVNETProfileCfgLineImpedance_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 7, 1, 18),
    _NvmVNETProfileCfgLineImpedance_Type()
)
nvmVNETProfileCfgLineImpedance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmVNETProfileCfgLineImpedance.setStatus("mandatory")


class _NvmVNETProfileCfgMaxOutputLevel_Type(Integer32):
    """Custom type nvmVNETProfileCfgMaxOutputLevel based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("plus7dBM", 2),
          ("zerodBMNominal", 1))
    )


_NvmVNETProfileCfgMaxOutputLevel_Type.__name__ = "Integer32"
_NvmVNETProfileCfgMaxOutputLevel_Object = MibTableColumn
nvmVNETProfileCfgMaxOutputLevel = _NvmVNETProfileCfgMaxOutputLevel_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 7, 1, 19),
    _NvmVNETProfileCfgMaxOutputLevel_Type()
)
nvmVNETProfileCfgMaxOutputLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmVNETProfileCfgMaxOutputLevel.setStatus("mandatory")


class _NvmVNETProfileCfgRegenDelay_Type(Integer32):
    """Custom type nvmVNETProfileCfgRegenDelay based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_NvmVNETProfileCfgRegenDelay_Type.__name__ = "Integer32"
_NvmVNETProfileCfgRegenDelay_Object = MibTableColumn
nvmVNETProfileCfgRegenDelay = _NvmVNETProfileCfgRegenDelay_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 7, 1, 20),
    _NvmVNETProfileCfgRegenDelay_Type()
)
nvmVNETProfileCfgRegenDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmVNETProfileCfgRegenDelay.setStatus("mandatory")


class _NvmVNETProfileCfgDialDigTimeLimit_Type(Integer32):
    """Custom type nvmVNETProfileCfgDialDigTimeLimit based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_NvmVNETProfileCfgDialDigTimeLimit_Type.__name__ = "Integer32"
_NvmVNETProfileCfgDialDigTimeLimit_Object = MibTableColumn
nvmVNETProfileCfgDialDigTimeLimit = _NvmVNETProfileCfgDialDigTimeLimit_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 7, 1, 21),
    _NvmVNETProfileCfgDialDigTimeLimit_Type()
)
nvmVNETProfileCfgDialDigTimeLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmVNETProfileCfgDialDigTimeLimit.setStatus("mandatory")


class _NvmVNETProfileCfgMaxNumForDig_Type(Integer32):
    """Custom type nvmVNETProfileCfgMaxNumForDig based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 40),
    )


_NvmVNETProfileCfgMaxNumForDig_Type.__name__ = "Integer32"
_NvmVNETProfileCfgMaxNumForDig_Object = MibTableColumn
nvmVNETProfileCfgMaxNumForDig = _NvmVNETProfileCfgMaxNumForDig_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 7, 1, 22),
    _NvmVNETProfileCfgMaxNumForDig_Type()
)
nvmVNETProfileCfgMaxNumForDig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmVNETProfileCfgMaxNumForDig.setStatus("mandatory")


class _NvmVNETProfileCfgRegenFormat_Type(Integer32):
    """Custom type nvmVNETProfileCfgRegenFormat based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dialPulse", 1),
          ("dtmf", 2))
    )


_NvmVNETProfileCfgRegenFormat_Type.__name__ = "Integer32"
_NvmVNETProfileCfgRegenFormat_Object = MibTableColumn
nvmVNETProfileCfgRegenFormat = _NvmVNETProfileCfgRegenFormat_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 7, 1, 23),
    _NvmVNETProfileCfgRegenFormat_Type()
)
nvmVNETProfileCfgRegenFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmVNETProfileCfgRegenFormat.setStatus("mandatory")


class _NvmVNETProfileCfgCallProgTone_Type(Integer32):
    """Custom type nvmVNETProfileCfgCallProgTone based on Integer32"""
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
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("australia", 8),
          ("centralAmerica", 6),
          ("chile", 7),
          ("europe-germany", 4),
          ("france", 5),
          ("japan", 2),
          ("northAmerica", 1),
          ("unitedKingdom", 3))
    )


_NvmVNETProfileCfgCallProgTone_Type.__name__ = "Integer32"
_NvmVNETProfileCfgCallProgTone_Object = MibTableColumn
nvmVNETProfileCfgCallProgTone = _NvmVNETProfileCfgCallProgTone_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 7, 1, 24),
    _NvmVNETProfileCfgCallProgTone_Type()
)
nvmVNETProfileCfgCallProgTone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmVNETProfileCfgCallProgTone.setStatus("mandatory")


class _NvmVNETProfileCfgDTMFDetector_Type(Integer32):
    """Custom type nvmVNETProfileCfgDTMFDetector based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_NvmVNETProfileCfgDTMFDetector_Type.__name__ = "Integer32"
_NvmVNETProfileCfgDTMFDetector_Object = MibTableColumn
nvmVNETProfileCfgDTMFDetector = _NvmVNETProfileCfgDTMFDetector_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 7, 1, 25),
    _NvmVNETProfileCfgDTMFDetector_Type()
)
nvmVNETProfileCfgDTMFDetector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmVNETProfileCfgDTMFDetector.setStatus("mandatory")


class _NvmVNETProfileCfgJitters_Type(Integer32):
    """Custom type nvmVNETProfileCfgJitters based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_NvmVNETProfileCfgJitters_Type.__name__ = "Integer32"
_NvmVNETProfileCfgJitters_Object = MibTableColumn
nvmVNETProfileCfgJitters = _NvmVNETProfileCfgJitters_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 7, 1, 26),
    _NvmVNETProfileCfgJitters_Type()
)
nvmVNETProfileCfgJitters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmVNETProfileCfgJitters.setStatus("mandatory")


class _NvmVNETProfileCfgEchoCanceller_Type(Integer32):
    """Custom type nvmVNETProfileCfgEchoCanceller based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_NvmVNETProfileCfgEchoCanceller_Type.__name__ = "Integer32"
_NvmVNETProfileCfgEchoCanceller_Object = MibTableColumn
nvmVNETProfileCfgEchoCanceller = _NvmVNETProfileCfgEchoCanceller_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 7, 1, 27),
    _NvmVNETProfileCfgEchoCanceller_Type()
)
nvmVNETProfileCfgEchoCanceller.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmVNETProfileCfgEchoCanceller.setStatus("mandatory")


class _NvmVNETProfileCfgAutoGainControl_Type(Integer32):
    """Custom type nvmVNETProfileCfgAutoGainControl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_NvmVNETProfileCfgAutoGainControl_Type.__name__ = "Integer32"
_NvmVNETProfileCfgAutoGainControl_Object = MibTableColumn
nvmVNETProfileCfgAutoGainControl = _NvmVNETProfileCfgAutoGainControl_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 7, 1, 28),
    _NvmVNETProfileCfgAutoGainControl_Type()
)
nvmVNETProfileCfgAutoGainControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmVNETProfileCfgAutoGainControl.setStatus("mandatory")


class _NvmVNETProfileCfgCompanderFormat_Type(Integer32):
    """Custom type nvmVNETProfileCfgCompanderFormat based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aLaw", 2),
          ("uLaw", 1))
    )


_NvmVNETProfileCfgCompanderFormat_Type.__name__ = "Integer32"
_NvmVNETProfileCfgCompanderFormat_Object = MibTableColumn
nvmVNETProfileCfgCompanderFormat = _NvmVNETProfileCfgCompanderFormat_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 7, 1, 29),
    _NvmVNETProfileCfgCompanderFormat_Type()
)
nvmVNETProfileCfgCompanderFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmVNETProfileCfgCompanderFormat.setStatus("mandatory")


class _NvmVNETProfileCfgPremiumVoice_Type(Integer32):
    """Custom type nvmVNETProfileCfgPremiumVoice based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable-compress", 1),
          ("enable-notcompress", 2))
    )


_NvmVNETProfileCfgPremiumVoice_Type.__name__ = "Integer32"
_NvmVNETProfileCfgPremiumVoice_Object = MibTableColumn
nvmVNETProfileCfgPremiumVoice = _NvmVNETProfileCfgPremiumVoice_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 7, 1, 30),
    _NvmVNETProfileCfgPremiumVoice_Type()
)
nvmVNETProfileCfgPremiumVoice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmVNETProfileCfgPremiumVoice.setStatus("mandatory")


class _NvmVNETProfileCfgEndOfDialChar_Type(Integer32):
    """Custom type nvmVNETProfileCfgEndOfDialChar based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_NvmVNETProfileCfgEndOfDialChar_Type.__name__ = "Integer32"
_NvmVNETProfileCfgEndOfDialChar_Object = MibTableColumn
nvmVNETProfileCfgEndOfDialChar = _NvmVNETProfileCfgEndOfDialChar_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 7, 1, 31),
    _NvmVNETProfileCfgEndOfDialChar_Type()
)
nvmVNETProfileCfgEndOfDialChar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmVNETProfileCfgEndOfDialChar.setStatus("mandatory")


class _NvmVNETProfileCfgBckGrndNoiseLevel_Type(Integer32):
    """Custom type nvmVNETProfileCfgBckGrndNoiseLevel based on Integer32"""
    defaultValue = 2

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
        *(("neg25dbm0", 1),
          ("neg30dbm0", 2),
          ("neg35dbm0", 3),
          ("neg40dbm0", 4),
          ("neg45dbm0", 5))
    )


_NvmVNETProfileCfgBckGrndNoiseLevel_Type.__name__ = "Integer32"
_NvmVNETProfileCfgBckGrndNoiseLevel_Object = MibTableColumn
nvmVNETProfileCfgBckGrndNoiseLevel = _NvmVNETProfileCfgBckGrndNoiseLevel_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 7, 1, 32),
    _NvmVNETProfileCfgBckGrndNoiseLevel_Type()
)
nvmVNETProfileCfgBckGrndNoiseLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmVNETProfileCfgBckGrndNoiseLevel.setStatus("mandatory")


class _NvmVNETProfileCfgSilenceHngOvrTime_Type(Integer32):
    """Custom type nvmVNETProfileCfgSilenceHngOvrTime based on Integer32"""
    defaultValue = 3

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
              8)
        )
    )
    namedValues = NamedValues(
        *(("msec100", 1),
          ("msec200", 2),
          ("msec300", 3),
          ("msec400", 4),
          ("msec500", 5),
          ("msec600", 6),
          ("msec700", 7),
          ("msec800", 8))
    )


_NvmVNETProfileCfgSilenceHngOvrTime_Type.__name__ = "Integer32"
_NvmVNETProfileCfgSilenceHngOvrTime_Object = MibTableColumn
nvmVNETProfileCfgSilenceHngOvrTime = _NvmVNETProfileCfgSilenceHngOvrTime_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 7, 1, 33),
    _NvmVNETProfileCfgSilenceHngOvrTime_Type()
)
nvmVNETProfileCfgSilenceHngOvrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmVNETProfileCfgSilenceHngOvrTime.setStatus("mandatory")


class _NvmVNETProfileCfgIdlePattern_Type(Integer32):
    """Custom type nvmVNETProfileCfgIdlePattern based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NvmVNETProfileCfgIdlePattern_Type.__name__ = "Integer32"
_NvmVNETProfileCfgIdlePattern_Object = MibTableColumn
nvmVNETProfileCfgIdlePattern = _NvmVNETProfileCfgIdlePattern_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 7, 1, 34),
    _NvmVNETProfileCfgIdlePattern_Type()
)
nvmVNETProfileCfgIdlePattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmVNETProfileCfgIdlePattern.setStatus("mandatory")


class _NvmVNETProfileCfgEcanFilterLength_Type(Integer32):
    """Custom type nvmVNETProfileCfgEcanFilterLength based on Integer32"""
    defaultValue = 256

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("length128", 1),
          ("length256", 2))
    )


_NvmVNETProfileCfgEcanFilterLength_Type.__name__ = "Integer32"
_NvmVNETProfileCfgEcanFilterLength_Object = MibTableColumn
nvmVNETProfileCfgEcanFilterLength = _NvmVNETProfileCfgEcanFilterLength_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 7, 1, 35),
    _NvmVNETProfileCfgEcanFilterLength_Type()
)
nvmVNETProfileCfgEcanFilterLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmVNETProfileCfgEcanFilterLength.setStatus("mandatory")


class _NvmVNETProfileCfgEcanErlImprovement_Type(Integer32):
    """Custom type nvmVNETProfileCfgEcanErlImprovement based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-18, 0),
    )


_NvmVNETProfileCfgEcanErlImprovement_Type.__name__ = "Integer32"
_NvmVNETProfileCfgEcanErlImprovement_Object = MibTableColumn
nvmVNETProfileCfgEcanErlImprovement = _NvmVNETProfileCfgEcanErlImprovement_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 7, 1, 36),
    _NvmVNETProfileCfgEcanErlImprovement_Type()
)
nvmVNETProfileCfgEcanErlImprovement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmVNETProfileCfgEcanErlImprovement.setStatus("mandatory")


class _NvmVNETProfileCfgNoiseFloorOffset_Type(Integer32):
    """Custom type nvmVNETProfileCfgNoiseFloorOffset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NvmVNETProfileCfgNoiseFloorOffset_Type.__name__ = "Integer32"
_NvmVNETProfileCfgNoiseFloorOffset_Object = MibTableColumn
nvmVNETProfileCfgNoiseFloorOffset = _NvmVNETProfileCfgNoiseFloorOffset_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 7, 1, 37),
    _NvmVNETProfileCfgNoiseFloorOffset_Type()
)
nvmVNETProfileCfgNoiseFloorOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmVNETProfileCfgNoiseFloorOffset.setStatus("mandatory")


class _NvmVNETProfileCfgDtmfGenBurstLength_Type(Integer32):
    """Custom type nvmVNETProfileCfgDtmfGenBurstLength based on Integer32"""
    defaultValue = 100

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
        *(("time100msec", 4),
          ("time50msec", 1),
          ("time60msec", 2),
          ("time70msec", 3))
    )


_NvmVNETProfileCfgDtmfGenBurstLength_Type.__name__ = "Integer32"
_NvmVNETProfileCfgDtmfGenBurstLength_Object = MibTableColumn
nvmVNETProfileCfgDtmfGenBurstLength = _NvmVNETProfileCfgDtmfGenBurstLength_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 7, 1, 38),
    _NvmVNETProfileCfgDtmfGenBurstLength_Type()
)
nvmVNETProfileCfgDtmfGenBurstLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmVNETProfileCfgDtmfGenBurstLength.setStatus("mandatory")


class _NvmVNETProfileCfgDtmRegenBurstLength_Type(Integer32):
    """Custom type nvmVNETProfileCfgDtmRegenBurstLength based on Integer32"""
    defaultValue = 100

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
        *(("time100msec", 4),
          ("time50msec", 1),
          ("time60msec", 2),
          ("time70msec", 3))
    )


_NvmVNETProfileCfgDtmRegenBurstLength_Type.__name__ = "Integer32"
_NvmVNETProfileCfgDtmRegenBurstLength_Object = MibTableColumn
nvmVNETProfileCfgDtmRegenBurstLength = _NvmVNETProfileCfgDtmRegenBurstLength_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 7, 1, 39),
    _NvmVNETProfileCfgDtmRegenBurstLength_Type()
)
nvmVNETProfileCfgDtmRegenBurstLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmVNETProfileCfgDtmRegenBurstLength.setStatus("mandatory")
_NvmVNETSwProfCfgTable_Object = MibTable
nvmVNETSwProfCfgTable = _NvmVNETSwProfCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 8)
)
if mibBuilder.loadTexts:
    nvmVNETSwProfCfgTable.setStatus("mandatory")
_NvmVNETSwProfCfgEntry_Object = MibTableRow
nvmVNETSwProfCfgEntry = _NvmVNETSwProfCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 8, 1)
)
nvmVNETSwProfCfgEntry.setIndexNames(
    (0, "MICOM-4400-VOICE-NETWORK-MIB", "nvmVNETSwProfCfgProfileNum"),
)
if mibBuilder.loadTexts:
    nvmVNETSwProfCfgEntry.setStatus("mandatory")


class _NvmVNETSwProfCfgProfileNum_Type(Integer32):
    """Custom type nvmVNETSwProfCfgProfileNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_NvmVNETSwProfCfgProfileNum_Type.__name__ = "Integer32"
_NvmVNETSwProfCfgProfileNum_Object = MibTableColumn
nvmVNETSwProfCfgProfileNum = _NvmVNETSwProfCfgProfileNum_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 8, 1, 1),
    _NvmVNETSwProfCfgProfileNum_Type()
)
nvmVNETSwProfCfgProfileNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmVNETSwProfCfgProfileNum.setStatus("mandatory")


class _NvmVNETSwProfCfgOutCallRestrict_Type(Integer32):
    """Custom type nvmVNETSwProfCfgOutCallRestrict based on Integer32"""
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
        *(("bothCUGandRCCall", 4),
          ("closedUserGroupCall", 2),
          ("inhibitAll", 5),
          ("noRestriction", 1),
          ("restrictionClassCall", 3))
    )


_NvmVNETSwProfCfgOutCallRestrict_Type.__name__ = "Integer32"
_NvmVNETSwProfCfgOutCallRestrict_Object = MibTableColumn
nvmVNETSwProfCfgOutCallRestrict = _NvmVNETSwProfCfgOutCallRestrict_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 8, 1, 2),
    _NvmVNETSwProfCfgOutCallRestrict_Type()
)
nvmVNETSwProfCfgOutCallRestrict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmVNETSwProfCfgOutCallRestrict.setStatus("mandatory")


class _NvmVNETSwProfCfgInCallRestrict_Type(Integer32):
    """Custom type nvmVNETSwProfCfgInCallRestrict based on Integer32"""
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
        *(("cUGandPublicClassInhibit", 4),
          ("checkCUGID", 2),
          ("checkRestrictionClassCode", 3),
          ("inhibitAll", 5),
          ("noRestriction", 1))
    )


_NvmVNETSwProfCfgInCallRestrict_Type.__name__ = "Integer32"
_NvmVNETSwProfCfgInCallRestrict_Object = MibTableColumn
nvmVNETSwProfCfgInCallRestrict = _NvmVNETSwProfCfgInCallRestrict_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 8, 1, 3),
    _NvmVNETSwProfCfgInCallRestrict_Type()
)
nvmVNETSwProfCfgInCallRestrict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmVNETSwProfCfgInCallRestrict.setStatus("mandatory")


class _NvmVNETSwProfCfgCUGID_Type(Integer32):
    """Custom type nvmVNETSwProfCfgCUGID based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NvmVNETSwProfCfgCUGID_Type.__name__ = "Integer32"
_NvmVNETSwProfCfgCUGID_Object = MibTableColumn
nvmVNETSwProfCfgCUGID = _NvmVNETSwProfCfgCUGID_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 8, 1, 4),
    _NvmVNETSwProfCfgCUGID_Type()
)
nvmVNETSwProfCfgCUGID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmVNETSwProfCfgCUGID.setStatus("mandatory")


class _NvmVNETSwProfCfgRestrictClassCd_Type(Integer32):
    """Custom type nvmVNETSwProfCfgRestrictClassCd based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_NvmVNETSwProfCfgRestrictClassCd_Type.__name__ = "Integer32"
_NvmVNETSwProfCfgRestrictClassCd_Object = MibTableColumn
nvmVNETSwProfCfgRestrictClassCd = _NvmVNETSwProfCfgRestrictClassCd_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 8, 1, 5),
    _NvmVNETSwProfCfgRestrictClassCd_Type()
)
nvmVNETSwProfCfgRestrictClassCd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmVNETSwProfCfgRestrictClassCd.setStatus("mandatory")


class _NvmVNETSwProfCfgAutoCallEntNum_Type(Integer32):
    """Custom type nvmVNETSwProfCfgAutoCallEntNum based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_NvmVNETSwProfCfgAutoCallEntNum_Type.__name__ = "Integer32"
_NvmVNETSwProfCfgAutoCallEntNum_Object = MibTableColumn
nvmVNETSwProfCfgAutoCallEntNum = _NvmVNETSwProfCfgAutoCallEntNum_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 8, 1, 6),
    _NvmVNETSwProfCfgAutoCallEntNum_Type()
)
nvmVNETSwProfCfgAutoCallEntNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmVNETSwProfCfgAutoCallEntNum.setStatus("mandatory")


class _NvmVNETSwProfCfgCallNegStrategy_Type(Integer32):
    """Custom type nvmVNETSwProfCfgCallNegStrategy based on Integer32"""
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
        *(("bandwidth", 2),
          ("delay", 3),
          ("specific", 1))
    )


_NvmVNETSwProfCfgCallNegStrategy_Type.__name__ = "Integer32"
_NvmVNETSwProfCfgCallNegStrategy_Object = MibTableColumn
nvmVNETSwProfCfgCallNegStrategy = _NvmVNETSwProfCfgCallNegStrategy_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 8, 1, 7),
    _NvmVNETSwProfCfgCallNegStrategy_Type()
)
nvmVNETSwProfCfgCallNegStrategy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmVNETSwProfCfgCallNegStrategy.setStatus("mandatory")


class _NvmVNETSwProfCfgTransmitPriority_Type(Integer32):
    """Custom type nvmVNETSwProfCfgTransmitPriority based on Integer32"""
    defaultValue = 11

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_NvmVNETSwProfCfgTransmitPriority_Type.__name__ = "Integer32"
_NvmVNETSwProfCfgTransmitPriority_Object = MibTableColumn
nvmVNETSwProfCfgTransmitPriority = _NvmVNETSwProfCfgTransmitPriority_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 8, 1, 8),
    _NvmVNETSwProfCfgTransmitPriority_Type()
)
nvmVNETSwProfCfgTransmitPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmVNETSwProfCfgTransmitPriority.setStatus("mandatory")


class _NvmVNETSwProfCfgAutoCallType_Type(Integer32):
    """Custom type nvmVNETSwProfCfgAutoCallType based on Integer32"""
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
        *(("masterHootnHoller", 2),
          ("normal", 1),
          ("slaveHootnHoller", 3))
    )


_NvmVNETSwProfCfgAutoCallType_Type.__name__ = "Integer32"
_NvmVNETSwProfCfgAutoCallType_Object = MibTableColumn
nvmVNETSwProfCfgAutoCallType = _NvmVNETSwProfCfgAutoCallType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 8, 1, 9),
    _NvmVNETSwProfCfgAutoCallType_Type()
)
nvmVNETSwProfCfgAutoCallType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmVNETSwProfCfgAutoCallType.setStatus("mandatory")


class _NvmVNETSwProfCfgAddServerSelect_Type(Integer32):
    """Custom type nvmVNETSwProfCfgAddServerSelect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nas", 1),
          ("vncs", 2))
    )


_NvmVNETSwProfCfgAddServerSelect_Type.__name__ = "Integer32"
_NvmVNETSwProfCfgAddServerSelect_Object = MibTableColumn
nvmVNETSwProfCfgAddServerSelect = _NvmVNETSwProfCfgAddServerSelect_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 8, 1, 10),
    _NvmVNETSwProfCfgAddServerSelect_Type()
)
nvmVNETSwProfCfgAddServerSelect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmVNETSwProfCfgAddServerSelect.setStatus("mandatory")


class _NvmVNETSwProfCfgOutCallMode_Type(Integer32):
    """Custom type nvmVNETSwProfCfgOutCallMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("enblock-only", 1))
    )


_NvmVNETSwProfCfgOutCallMode_Type.__name__ = "Integer32"
_NvmVNETSwProfCfgOutCallMode_Object = MibTableColumn
nvmVNETSwProfCfgOutCallMode = _NvmVNETSwProfCfgOutCallMode_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 8, 1, 11),
    _NvmVNETSwProfCfgOutCallMode_Type()
)
nvmVNETSwProfCfgOutCallMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmVNETSwProfCfgOutCallMode.setStatus("mandatory")
_NvmVNETIngressDigFilterTable_Object = MibTable
nvmVNETIngressDigFilterTable = _NvmVNETIngressDigFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 9)
)
if mibBuilder.loadTexts:
    nvmVNETIngressDigFilterTable.setStatus("mandatory")
_NvmVNETIngressDigFilterEntry_Object = MibTableRow
nvmVNETIngressDigFilterEntry = _NvmVNETIngressDigFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 9, 1)
)
nvmVNETIngressDigFilterEntry.setIndexNames(
    (0, "MICOM-4400-VOICE-NETWORK-MIB", "nvmVNETIngressDigFilterIndex"),
)
if mibBuilder.loadTexts:
    nvmVNETIngressDigFilterEntry.setStatus("mandatory")


class _NvmVNETIngressDigFilterIndex_Type(Integer32):
    """Custom type nvmVNETIngressDigFilterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_NvmVNETIngressDigFilterIndex_Type.__name__ = "Integer32"
_NvmVNETIngressDigFilterIndex_Object = MibTableColumn
nvmVNETIngressDigFilterIndex = _NvmVNETIngressDigFilterIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 9, 1, 1),
    _NvmVNETIngressDigFilterIndex_Type()
)
nvmVNETIngressDigFilterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmVNETIngressDigFilterIndex.setStatus("mandatory")


class _NvmVNETIngressDigFilterIngressNum_Type(DisplayString):
    """Custom type nvmVNETIngressDigFilterIngressNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_NvmVNETIngressDigFilterIngressNum_Type.__name__ = "DisplayString"
_NvmVNETIngressDigFilterIngressNum_Object = MibTableColumn
nvmVNETIngressDigFilterIngressNum = _NvmVNETIngressDigFilterIngressNum_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 9, 1, 2),
    _NvmVNETIngressDigFilterIngressNum_Type()
)
nvmVNETIngressDigFilterIngressNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmVNETIngressDigFilterIngressNum.setStatus("mandatory")


class _NvmVNETIngressDigFilterManipString_Type(DisplayString):
    """Custom type nvmVNETIngressDigFilterManipString based on DisplayString"""
    defaultValue = OctetString("#")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_NvmVNETIngressDigFilterManipString_Type.__name__ = "DisplayString"
_NvmVNETIngressDigFilterManipString_Object = MibTableColumn
nvmVNETIngressDigFilterManipString = _NvmVNETIngressDigFilterManipString_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 9, 1, 3),
    _NvmVNETIngressDigFilterManipString_Type()
)
nvmVNETIngressDigFilterManipString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmVNETIngressDigFilterManipString.setStatus("mandatory")
_NvmVNETEgressDigManipTable_Object = MibTable
nvmVNETEgressDigManipTable = _NvmVNETEgressDigManipTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 10)
)
if mibBuilder.loadTexts:
    nvmVNETEgressDigManipTable.setStatus("mandatory")
_NvmVNETEgressDigManipEntry_Object = MibTableRow
nvmVNETEgressDigManipEntry = _NvmVNETEgressDigManipEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 10, 1)
)
nvmVNETEgressDigManipEntry.setIndexNames(
    (0, "MICOM-4400-VOICE-NETWORK-MIB", "nvmVNETEgressDigManipIndex"),
)
if mibBuilder.loadTexts:
    nvmVNETEgressDigManipEntry.setStatus("mandatory")


class _NvmVNETEgressDigManipIndex_Type(Integer32):
    """Custom type nvmVNETEgressDigManipIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_NvmVNETEgressDigManipIndex_Type.__name__ = "Integer32"
_NvmVNETEgressDigManipIndex_Object = MibTableColumn
nvmVNETEgressDigManipIndex = _NvmVNETEgressDigManipIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 10, 1, 1),
    _NvmVNETEgressDigManipIndex_Type()
)
nvmVNETEgressDigManipIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmVNETEgressDigManipIndex.setStatus("mandatory")


class _NvmVNETEgressDigManipPhoneNum_Type(DisplayString):
    """Custom type nvmVNETEgressDigManipPhoneNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_NvmVNETEgressDigManipPhoneNum_Type.__name__ = "DisplayString"
_NvmVNETEgressDigManipPhoneNum_Object = MibTableColumn
nvmVNETEgressDigManipPhoneNum = _NvmVNETEgressDigManipPhoneNum_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 10, 1, 2),
    _NvmVNETEgressDigManipPhoneNum_Type()
)
nvmVNETEgressDigManipPhoneNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmVNETEgressDigManipPhoneNum.setStatus("mandatory")


class _NvmVNETEgressDigManipString_Type(DisplayString):
    """Custom type nvmVNETEgressDigManipString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_NvmVNETEgressDigManipString_Type.__name__ = "DisplayString"
_NvmVNETEgressDigManipString_Object = MibTableColumn
nvmVNETEgressDigManipString = _NvmVNETEgressDigManipString_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 10, 1, 3),
    _NvmVNETEgressDigManipString_Type()
)
nvmVNETEgressDigManipString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmVNETEgressDigManipString.setStatus("mandatory")


class _NvmVNETEgressDigManipChIDList_Type(DisplayString):
    """Custom type nvmVNETEgressDigManipChIDList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 70),
    )


_NvmVNETEgressDigManipChIDList_Type.__name__ = "DisplayString"
_NvmVNETEgressDigManipChIDList_Object = MibTableColumn
nvmVNETEgressDigManipChIDList = _NvmVNETEgressDigManipChIDList_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 1, 10, 1, 4),
    _NvmVNETEgressDigManipChIDList_Type()
)
nvmVNETEgressDigManipChIDList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nvmVNETEgressDigManipChIDList.setStatus("mandatory")
_Vnet_control_ObjectIdentity = ObjectIdentity
vnet_control = _Vnet_control_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 2)
)
_McmVNETChControlTable_Object = MibTable
mcmVNETChControlTable = _McmVNETChControlTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 2, 1)
)
if mibBuilder.loadTexts:
    mcmVNETChControlTable.setStatus("mandatory")
_McmVNETChControlEntry_Object = MibTableRow
mcmVNETChControlEntry = _McmVNETChControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 2, 1, 1)
)
mcmVNETChControlEntry.setIndexNames(
    (0, "MICOM-4400-VOICE-NETWORK-MIB", "mcmVNETChControlLimID"),
    (0, "MICOM-4400-VOICE-NETWORK-MIB", "mcmVNETChControlChannelID"),
)
if mibBuilder.loadTexts:
    mcmVNETChControlEntry.setStatus("mandatory")


class _McmVNETChControlLimID_Type(Integer32):
    """Custom type mcmVNETChControlLimID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
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
        *(("lim1", 2),
          ("lim2", 3),
          ("lim3", 4),
          ("lim4", 5),
          ("limB", 6),
          ("limC", 7),
          ("limD", 8),
          ("limE", 9))
    )


_McmVNETChControlLimID_Type.__name__ = "Integer32"
_McmVNETChControlLimID_Object = MibTableColumn
mcmVNETChControlLimID = _McmVNETChControlLimID_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 2, 1, 1, 1),
    _McmVNETChControlLimID_Type()
)
mcmVNETChControlLimID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmVNETChControlLimID.setStatus("mandatory")


class _McmVNETChControlChannelID_Type(Integer32):
    """Custom type mcmVNETChControlChannelID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_McmVNETChControlChannelID_Type.__name__ = "Integer32"
_McmVNETChControlChannelID_Object = MibTableColumn
mcmVNETChControlChannelID = _McmVNETChControlChannelID_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 2, 1, 1, 2),
    _McmVNETChControlChannelID_Type()
)
mcmVNETChControlChannelID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmVNETChControlChannelID.setStatus("mandatory")


class _McmVNETChControlActionCmd_Type(Integer32):
    """Custom type mcmVNETChControlActionCmd based on Integer32"""
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
        *(("clearChannelCounters", 2),
          ("codeDownload", 3),
          ("disconnect", 4),
          ("forceConnect", 7),
          ("loopbackTest", 5),
          ("resetChannel", 1),
          ("terminateTests", 6))
    )


_McmVNETChControlActionCmd_Type.__name__ = "Integer32"
_McmVNETChControlActionCmd_Object = MibTableColumn
mcmVNETChControlActionCmd = _McmVNETChControlActionCmd_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 2, 1, 1, 3),
    _McmVNETChControlActionCmd_Type()
)
mcmVNETChControlActionCmd.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mcmVNETChControlActionCmd.setStatus("mandatory")


class _McmVNETSysControlActionCmd_Type(Integer32):
    """Custom type mcmVNETSysControlActionCmd based on Integer32"""
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
        *(("clearChannelCounters", 3),
          ("clearNetworkCounters", 1),
          ("disconnect", 5),
          ("download", 4),
          ("forceConnects", 8),
          ("loopbackTests", 6),
          ("reRegisterPhoneNum", 9),
          ("resetChannels", 2),
          ("terminateTests", 7))
    )


_McmVNETSysControlActionCmd_Type.__name__ = "Integer32"
_McmVNETSysControlActionCmd_Object = MibScalar
mcmVNETSysControlActionCmd = _McmVNETSysControlActionCmd_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 2, 2),
    _McmVNETSysControlActionCmd_Type()
)
mcmVNETSysControlActionCmd.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    mcmVNETSysControlActionCmd.setStatus("mandatory")
_Vnet_status_ObjectIdentity = ObjectIdentity
vnet_status = _Vnet_status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 3)
)
_McmVNETChStatusTable_Object = MibTable
mcmVNETChStatusTable = _McmVNETChStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 3, 1)
)
if mibBuilder.loadTexts:
    mcmVNETChStatusTable.setStatus("mandatory")
_McmVNETChStatusEntry_Object = MibTableRow
mcmVNETChStatusEntry = _McmVNETChStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 3, 1, 1)
)
mcmVNETChStatusEntry.setIndexNames(
    (0, "MICOM-4400-VOICE-NETWORK-MIB", "mcmVNETChStatusLimID"),
    (0, "MICOM-4400-VOICE-NETWORK-MIB", "mcmVNETChStatusChannelID"),
)
if mibBuilder.loadTexts:
    mcmVNETChStatusEntry.setStatus("mandatory")


class _McmVNETChStatusLimID_Type(Integer32):
    """Custom type mcmVNETChStatusLimID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
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
        *(("lim1", 2),
          ("lim2", 3),
          ("lim3", 4),
          ("lim4", 5),
          ("limB", 6),
          ("limC", 7),
          ("limD", 8),
          ("limE", 9))
    )


_McmVNETChStatusLimID_Type.__name__ = "Integer32"
_McmVNETChStatusLimID_Object = MibTableColumn
mcmVNETChStatusLimID = _McmVNETChStatusLimID_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 3, 1, 1, 1),
    _McmVNETChStatusLimID_Type()
)
mcmVNETChStatusLimID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmVNETChStatusLimID.setStatus("mandatory")


class _McmVNETChStatusChannelID_Type(Integer32):
    """Custom type mcmVNETChStatusChannelID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_McmVNETChStatusChannelID_Type.__name__ = "Integer32"
_McmVNETChStatusChannelID_Object = MibTableColumn
mcmVNETChStatusChannelID = _McmVNETChStatusChannelID_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 3, 1, 1, 2),
    _McmVNETChStatusChannelID_Type()
)
mcmVNETChStatusChannelID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmVNETChStatusChannelID.setStatus("mandatory")


class _McmVNETChStatusInterfaceType_Type(Integer32):
    """Custom type mcmVNETChStatusInterfaceType based on Integer32"""
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
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("bri", 12),
          ("dvm", 11),
          ("enhanced-EandM", 3),
          ("enhanced-loop-start-FXO", 4),
          ("enhanced-loop-start-FXS", 2),
          ("ground-start-FXO", 9),
          ("ground-start-FXS", 8),
          ("low-cost-EandM", 6),
          ("low-cost-loop-start-FXO", 7),
          ("low-cost-loop-start-FXS", 5),
          ("not-available", 1),
          ("three-port", 10))
    )


_McmVNETChStatusInterfaceType_Type.__name__ = "Integer32"
_McmVNETChStatusInterfaceType_Object = MibTableColumn
mcmVNETChStatusInterfaceType = _McmVNETChStatusInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 3, 1, 1, 3),
    _McmVNETChStatusInterfaceType_Type()
)
mcmVNETChStatusInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmVNETChStatusInterfaceType.setStatus("mandatory")


class _McmVNETChStatusInterfaceSwID_Type(Integer32):
    """Custom type mcmVNETChStatusInterfaceSwID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_McmVNETChStatusInterfaceSwID_Type.__name__ = "Integer32"
_McmVNETChStatusInterfaceSwID_Object = MibTableColumn
mcmVNETChStatusInterfaceSwID = _McmVNETChStatusInterfaceSwID_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 3, 1, 1, 4),
    _McmVNETChStatusInterfaceSwID_Type()
)
mcmVNETChStatusInterfaceSwID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmVNETChStatusInterfaceSwID.setStatus("mandatory")


class _McmVNETChStatusEMType_Type(Integer32):
    """Custom type mcmVNETChStatusEMType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 6),
          ("typeI", 1),
          ("typeII", 2),
          ("typeIII", 3),
          ("typeIV", 4),
          ("typeV", 5))
    )


_McmVNETChStatusEMType_Type.__name__ = "Integer32"
_McmVNETChStatusEMType_Object = MibTableColumn
mcmVNETChStatusEMType = _McmVNETChStatusEMType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 3, 1, 1, 5),
    _McmVNETChStatusEMType_Type()
)
mcmVNETChStatusEMType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmVNETChStatusEMType.setStatus("mandatory")


class _McmVNETChStatusModelID_Type(Integer32):
    """Custom type mcmVNETChStatusModelID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("e1", 2),
          ("notApplicable", 3),
          ("t1", 1))
    )


_McmVNETChStatusModelID_Type.__name__ = "Integer32"
_McmVNETChStatusModelID_Object = MibTableColumn
mcmVNETChStatusModelID = _McmVNETChStatusModelID_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 3, 1, 1, 6),
    _McmVNETChStatusModelID_Type()
)
mcmVNETChStatusModelID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmVNETChStatusModelID.setStatus("mandatory")


class _McmVNETChStatusDSPOperation_Type(Integer32):
    """Custom type mcmVNETChStatusDSPOperation based on Integer32"""
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
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("busyOut", 10),
          ("codeDownloadInProgress", 11),
          ("dead", 1),
          ("downloadFailure", 3),
          ("forceConnected", 4),
          ("forceConnected-TimedOut", 5),
          ("idle", 6),
          ("notReady", 2),
          ("pcmChannelNotInstalled", 12),
          ("switchConnectInProgress", 7),
          ("switchConnected", 8),
          ("switchDisconnectInProgress", 9))
    )


_McmVNETChStatusDSPOperation_Type.__name__ = "Integer32"
_McmVNETChStatusDSPOperation_Object = MibTableColumn
mcmVNETChStatusDSPOperation = _McmVNETChStatusDSPOperation_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 3, 1, 1, 7),
    _McmVNETChStatusDSPOperation_Type()
)
mcmVNETChStatusDSPOperation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmVNETChStatusDSPOperation.setStatus("mandatory")


class _McmVNETChStatusNetworkConnect_Type(Integer32):
    """Custom type mcmVNETChStatusNetworkConnect based on Integer32"""
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
        *(("callInProgress", 2),
          ("disconnectInProgress", 5),
          ("idle", 1),
          ("locallyConnected", 3),
          ("remotelyConnected", 4))
    )


_McmVNETChStatusNetworkConnect_Type.__name__ = "Integer32"
_McmVNETChStatusNetworkConnect_Object = MibTableColumn
mcmVNETChStatusNetworkConnect = _McmVNETChStatusNetworkConnect_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 3, 1, 1, 8),
    _McmVNETChStatusNetworkConnect_Type()
)
mcmVNETChStatusNetworkConnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmVNETChStatusNetworkConnect.setStatus("mandatory")


class _McmVNETChStatusRemoteChHwType_Type(DisplayString):
    """Custom type mcmVNETChStatusRemoteChHwType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_McmVNETChStatusRemoteChHwType_Type.__name__ = "DisplayString"
_McmVNETChStatusRemoteChHwType_Object = MibTableColumn
mcmVNETChStatusRemoteChHwType = _McmVNETChStatusRemoteChHwType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 3, 1, 1, 9),
    _McmVNETChStatusRemoteChHwType_Type()
)
mcmVNETChStatusRemoteChHwType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmVNETChStatusRemoteChHwType.setStatus("mandatory")


class _McmVNETChStatusRemoteChNodeName_Type(DisplayString):
    """Custom type mcmVNETChStatusRemoteChNodeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_McmVNETChStatusRemoteChNodeName_Type.__name__ = "DisplayString"
_McmVNETChStatusRemoteChNodeName_Object = MibTableColumn
mcmVNETChStatusRemoteChNodeName = _McmVNETChStatusRemoteChNodeName_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 3, 1, 1, 10),
    _McmVNETChStatusRemoteChNodeName_Type()
)
mcmVNETChStatusRemoteChNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmVNETChStatusRemoteChNodeName.setStatus("mandatory")


class _McmVNETChStatusRemoteChNum_Type(DisplayString):
    """Custom type mcmVNETChStatusRemoteChNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_McmVNETChStatusRemoteChNum_Type.__name__ = "DisplayString"
_McmVNETChStatusRemoteChNum_Object = MibTableColumn
mcmVNETChStatusRemoteChNum = _McmVNETChStatusRemoteChNum_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 3, 1, 1, 11),
    _McmVNETChStatusRemoteChNum_Type()
)
mcmVNETChStatusRemoteChNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmVNETChStatusRemoteChNum.setStatus("mandatory")


class _McmVNETChStatusRemoteChIfType_Type(DisplayString):
    """Custom type mcmVNETChStatusRemoteChIfType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_McmVNETChStatusRemoteChIfType_Type.__name__ = "DisplayString"
_McmVNETChStatusRemoteChIfType_Object = MibTableColumn
mcmVNETChStatusRemoteChIfType = _McmVNETChStatusRemoteChIfType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 3, 1, 1, 12),
    _McmVNETChStatusRemoteChIfType_Type()
)
mcmVNETChStatusRemoteChIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmVNETChStatusRemoteChIfType.setStatus("mandatory")


class _McmVNETChStatusRemoteFrameIfVer_Type(Integer32):
    """Custom type mcmVNETChStatusRemoteFrameIfVer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_McmVNETChStatusRemoteFrameIfVer_Type.__name__ = "Integer32"
_McmVNETChStatusRemoteFrameIfVer_Object = MibTableColumn
mcmVNETChStatusRemoteFrameIfVer = _McmVNETChStatusRemoteFrameIfVer_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 3, 1, 1, 13),
    _McmVNETChStatusRemoteFrameIfVer_Type()
)
mcmVNETChStatusRemoteFrameIfVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmVNETChStatusRemoteFrameIfVer.setStatus("mandatory")


class _McmVNETChStatusRemoteChVoiceAlg_Type(DisplayString):
    """Custom type mcmVNETChStatusRemoteChVoiceAlg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_McmVNETChStatusRemoteChVoiceAlg_Type.__name__ = "DisplayString"
_McmVNETChStatusRemoteChVoiceAlg_Object = MibTableColumn
mcmVNETChStatusRemoteChVoiceAlg = _McmVNETChStatusRemoteChVoiceAlg_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 3, 1, 1, 14),
    _McmVNETChStatusRemoteChVoiceAlg_Type()
)
mcmVNETChStatusRemoteChVoiceAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmVNETChStatusRemoteChVoiceAlg.setStatus("mandatory")


class _McmVNETChStatusRemoteChFaxAlg_Type(DisplayString):
    """Custom type mcmVNETChStatusRemoteChFaxAlg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_McmVNETChStatusRemoteChFaxAlg_Type.__name__ = "DisplayString"
_McmVNETChStatusRemoteChFaxAlg_Object = MibTableColumn
mcmVNETChStatusRemoteChFaxAlg = _McmVNETChStatusRemoteChFaxAlg_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 3, 1, 1, 15),
    _McmVNETChStatusRemoteChFaxAlg_Type()
)
mcmVNETChStatusRemoteChFaxAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmVNETChStatusRemoteChFaxAlg.setStatus("mandatory")


class _McmVNETChStatusRemoteChModemAlg_Type(DisplayString):
    """Custom type mcmVNETChStatusRemoteChModemAlg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_McmVNETChStatusRemoteChModemAlg_Type.__name__ = "DisplayString"
_McmVNETChStatusRemoteChModemAlg_Object = MibTableColumn
mcmVNETChStatusRemoteChModemAlg = _McmVNETChStatusRemoteChModemAlg_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 3, 1, 1, 16),
    _McmVNETChStatusRemoteChModemAlg_Type()
)
mcmVNETChStatusRemoteChModemAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmVNETChStatusRemoteChModemAlg.setStatus("mandatory")


class _McmVNETChStatusSelfTestResult_Type(Integer32):
    """Custom type mcmVNETChStatusSelfTestResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("testFailed", 2),
          ("testPassed", 1))
    )


_McmVNETChStatusSelfTestResult_Type.__name__ = "Integer32"
_McmVNETChStatusSelfTestResult_Object = MibTableColumn
mcmVNETChStatusSelfTestResult = _McmVNETChStatusSelfTestResult_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 3, 1, 1, 17),
    _McmVNETChStatusSelfTestResult_Type()
)
mcmVNETChStatusSelfTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmVNETChStatusSelfTestResult.setStatus("mandatory")


class _McmVNETChStatusFlashEPROM_Type(Integer32):
    """Custom type mcmVNETChStatusFlashEPROM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("erased", 3),
          ("invalidChecksum", 4),
          ("noAnalogInterfaceDriver", 5),
          ("notInstalled", 1),
          ("securityViolation", 6),
          ("valid", 2))
    )


_McmVNETChStatusFlashEPROM_Type.__name__ = "Integer32"
_McmVNETChStatusFlashEPROM_Object = MibTableColumn
mcmVNETChStatusFlashEPROM = _McmVNETChStatusFlashEPROM_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 3, 1, 1, 18),
    _McmVNETChStatusFlashEPROM_Type()
)
mcmVNETChStatusFlashEPROM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmVNETChStatusFlashEPROM.setStatus("mandatory")


class _McmVNETChStatusEPROM_Type(Integer32):
    """Custom type mcmVNETChStatusEPROM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("currentlyOperating", 2),
          ("notInstalled", 1),
          ("presentButNotOperating", 3))
    )


_McmVNETChStatusEPROM_Type.__name__ = "Integer32"
_McmVNETChStatusEPROM_Object = MibTableColumn
mcmVNETChStatusEPROM = _McmVNETChStatusEPROM_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 3, 1, 1, 19),
    _McmVNETChStatusEPROM_Type()
)
mcmVNETChStatusEPROM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmVNETChStatusEPROM.setStatus("mandatory")


class _McmVNETChStatusDspPROMVer_Type(DisplayString):
    """Custom type mcmVNETChStatusDspPROMVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_McmVNETChStatusDspPROMVer_Type.__name__ = "DisplayString"
_McmVNETChStatusDspPROMVer_Object = MibTableColumn
mcmVNETChStatusDspPROMVer = _McmVNETChStatusDspPROMVer_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 3, 1, 1, 20),
    _McmVNETChStatusDspPROMVer_Type()
)
mcmVNETChStatusDspPROMVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmVNETChStatusDspPROMVer.setStatus("mandatory")


class _McmVNETChStatusPROMID_Type(DisplayString):
    """Custom type mcmVNETChStatusPROMID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_McmVNETChStatusPROMID_Type.__name__ = "DisplayString"
_McmVNETChStatusPROMID_Object = MibTableColumn
mcmVNETChStatusPROMID = _McmVNETChStatusPROMID_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 3, 1, 1, 21),
    _McmVNETChStatusPROMID_Type()
)
mcmVNETChStatusPROMID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmVNETChStatusPROMID.setStatus("mandatory")


class _McmVNETChStatusInputLevel_Type(Integer32):
    """Custom type mcmVNETChStatusInputLevel based on Integer32"""
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
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("greaterThan0dBm", 16),
          ("lessThanNeg25dBm", 1),
          ("neg10dBm", 7),
          ("neg12dBm", 6),
          ("neg15dBm", 5),
          ("neg18dBm", 4),
          ("neg1dBm", 14),
          ("neg21dBm", 3),
          ("neg24dBm", 2),
          ("neg2dBm", 13),
          ("neg3dBm", 12),
          ("neg4dBm", 11),
          ("neg5dBm", 10),
          ("neg6dBm", 9),
          ("neg8dBm", 8),
          ("notApplicable", 17),
          ("zerodBm", 15))
    )


_McmVNETChStatusInputLevel_Type.__name__ = "Integer32"
_McmVNETChStatusInputLevel_Object = MibTableColumn
mcmVNETChStatusInputLevel = _McmVNETChStatusInputLevel_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 3, 1, 1, 22),
    _McmVNETChStatusInputLevel_Type()
)
mcmVNETChStatusInputLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmVNETChStatusInputLevel.setStatus("mandatory")
_VoiceSysStatusGroup_ObjectIdentity = ObjectIdentity
voiceSysStatusGroup = _VoiceSysStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 3, 2)
)


class _VoiceSysStatusPhoneRegistrationStatus_Type(Integer32):
    """Custom type voiceSysStatusPhoneRegistrationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("lostCommunicationWithNAS", 4),
          ("nasAddressNotConfigured", 3),
          ("noResponseFromNAS", 5),
          ("registrationComplete", 1),
          ("registrationFailed", 6),
          ("registrationInProgress", 2))
    )


_VoiceSysStatusPhoneRegistrationStatus_Type.__name__ = "Integer32"
_VoiceSysStatusPhoneRegistrationStatus_Object = MibScalar
voiceSysStatusPhoneRegistrationStatus = _VoiceSysStatusPhoneRegistrationStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 3, 2, 1),
    _VoiceSysStatusPhoneRegistrationStatus_Type()
)
voiceSysStatusPhoneRegistrationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceSysStatusPhoneRegistrationStatus.setStatus("mandatory")
_Vnet_statistics_ObjectIdentity = ObjectIdentity
vnet_statistics = _Vnet_statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 4)
)
_McmVNETChStatsTable_Object = MibTable
mcmVNETChStatsTable = _McmVNETChStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 4, 1)
)
if mibBuilder.loadTexts:
    mcmVNETChStatsTable.setStatus("mandatory")
_McmVNETChStatsEntry_Object = MibTableRow
mcmVNETChStatsEntry = _McmVNETChStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 4, 1, 1)
)
mcmVNETChStatsEntry.setIndexNames(
    (0, "MICOM-4400-VOICE-NETWORK-MIB", "mcmVNETChStatsLimID"),
    (0, "MICOM-4400-VOICE-NETWORK-MIB", "mcmVNETChStatsChannelID"),
)
if mibBuilder.loadTexts:
    mcmVNETChStatsEntry.setStatus("mandatory")


class _McmVNETChStatsLimID_Type(Integer32):
    """Custom type mcmVNETChStatsLimID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
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
        *(("lim1", 2),
          ("lim2", 3),
          ("lim3", 4),
          ("lim4", 5),
          ("limB", 6),
          ("limC", 7),
          ("limD", 8),
          ("limE", 9))
    )


_McmVNETChStatsLimID_Type.__name__ = "Integer32"
_McmVNETChStatsLimID_Object = MibTableColumn
mcmVNETChStatsLimID = _McmVNETChStatsLimID_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 4, 1, 1, 1),
    _McmVNETChStatsLimID_Type()
)
mcmVNETChStatsLimID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmVNETChStatsLimID.setStatus("mandatory")


class _McmVNETChStatsChannelID_Type(Integer32):
    """Custom type mcmVNETChStatsChannelID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_McmVNETChStatsChannelID_Type.__name__ = "Integer32"
_McmVNETChStatsChannelID_Object = MibTableColumn
mcmVNETChStatsChannelID = _McmVNETChStatsChannelID_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 4, 1, 1, 2),
    _McmVNETChStatsChannelID_Type()
)
mcmVNETChStatsChannelID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmVNETChStatsChannelID.setStatus("mandatory")
_McmVNETChStatsOutCallConnTime_Type = Counter32
_McmVNETChStatsOutCallConnTime_Object = MibTableColumn
mcmVNETChStatsOutCallConnTime = _McmVNETChStatsOutCallConnTime_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 4, 1, 1, 3),
    _McmVNETChStatsOutCallConnTime_Type()
)
mcmVNETChStatsOutCallConnTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmVNETChStatsOutCallConnTime.setStatus("mandatory")
_McmVNETChStatsInCallConnTime_Type = Counter32
_McmVNETChStatsInCallConnTime_Object = MibTableColumn
mcmVNETChStatsInCallConnTime = _McmVNETChStatsInCallConnTime_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 4, 1, 1, 4),
    _McmVNETChStatsInCallConnTime_Type()
)
mcmVNETChStatsInCallConnTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmVNETChStatsInCallConnTime.setStatus("mandatory")
_McmVNETChStatsOutCallsSucceded_Type = Counter32
_McmVNETChStatsOutCallsSucceded_Object = MibTableColumn
mcmVNETChStatsOutCallsSucceded = _McmVNETChStatsOutCallsSucceded_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 4, 1, 1, 5),
    _McmVNETChStatsOutCallsSucceded_Type()
)
mcmVNETChStatsOutCallsSucceded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmVNETChStatsOutCallsSucceded.setStatus("mandatory")
_McmVNETChStatsOutCallsFailed_Type = Counter32
_McmVNETChStatsOutCallsFailed_Object = MibTableColumn
mcmVNETChStatsOutCallsFailed = _McmVNETChStatsOutCallsFailed_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 4, 1, 1, 6),
    _McmVNETChStatsOutCallsFailed_Type()
)
mcmVNETChStatsOutCallsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmVNETChStatsOutCallsFailed.setStatus("mandatory")
_McmVNETChStatsInCallsAccepted_Type = Counter32
_McmVNETChStatsInCallsAccepted_Object = MibTableColumn
mcmVNETChStatsInCallsAccepted = _McmVNETChStatsInCallsAccepted_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 4, 1, 1, 7),
    _McmVNETChStatsInCallsAccepted_Type()
)
mcmVNETChStatsInCallsAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmVNETChStatsInCallsAccepted.setStatus("mandatory")
_McmVNETChStatsInCallsRejected_Type = Counter32
_McmVNETChStatsInCallsRejected_Object = MibTableColumn
mcmVNETChStatsInCallsRejected = _McmVNETChStatsInCallsRejected_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 4, 1, 1, 8),
    _McmVNETChStatsInCallsRejected_Type()
)
mcmVNETChStatsInCallsRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmVNETChStatsInCallsRejected.setStatus("mandatory")
_McmVNETChStatsNumberOfResets_Type = Counter32
_McmVNETChStatsNumberOfResets_Object = MibTableColumn
mcmVNETChStatsNumberOfResets = _McmVNETChStatsNumberOfResets_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 4, 1, 1, 9),
    _McmVNETChStatsNumberOfResets_Type()
)
mcmVNETChStatsNumberOfResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmVNETChStatsNumberOfResets.setStatus("mandatory")
_McmVNETChStatsNumberOfRetries_Type = Counter32
_McmVNETChStatsNumberOfRetries_Object = MibTableColumn
mcmVNETChStatsNumberOfRetries = _McmVNETChStatsNumberOfRetries_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 4, 1, 1, 10),
    _McmVNETChStatsNumberOfRetries_Type()
)
mcmVNETChStatsNumberOfRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmVNETChStatsNumberOfRetries.setStatus("mandatory")
_McmVNETChStatsBBCFramesRcvd_Type = Counter32
_McmVNETChStatsBBCFramesRcvd_Object = MibTableColumn
mcmVNETChStatsBBCFramesRcvd = _McmVNETChStatsBBCFramesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 4, 1, 1, 11),
    _McmVNETChStatsBBCFramesRcvd_Type()
)
mcmVNETChStatsBBCFramesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmVNETChStatsBBCFramesRcvd.setStatus("mandatory")
_McmVNETChStatsBEOFFramesRcvd_Type = Counter32
_McmVNETChStatsBEOFFramesRcvd_Object = MibTableColumn
mcmVNETChStatsBEOFFramesRcvd = _McmVNETChStatsBEOFFramesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 4, 1, 1, 12),
    _McmVNETChStatsBEOFFramesRcvd_Type()
)
mcmVNETChStatsBEOFFramesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmVNETChStatsBEOFFramesRcvd.setStatus("mandatory")
_McmVNETChStatsLostSpeechFrames_Type = Counter32
_McmVNETChStatsLostSpeechFrames_Object = MibTableColumn
mcmVNETChStatsLostSpeechFrames = _McmVNETChStatsLostSpeechFrames_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 4, 1, 1, 13),
    _McmVNETChStatsLostSpeechFrames_Type()
)
mcmVNETChStatsLostSpeechFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmVNETChStatsLostSpeechFrames.setStatus("mandatory")
_McmVNETChStatsLostControlFrames_Type = Counter32
_McmVNETChStatsLostControlFrames_Object = MibTableColumn
mcmVNETChStatsLostControlFrames = _McmVNETChStatsLostControlFrames_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 4, 1, 1, 14),
    _McmVNETChStatsLostControlFrames_Type()
)
mcmVNETChStatsLostControlFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmVNETChStatsLostControlFrames.setStatus("mandatory")
_McmVNETChStatsInvalPayloadFrRcvd_Type = Counter32
_McmVNETChStatsInvalPayloadFrRcvd_Object = MibTableColumn
mcmVNETChStatsInvalPayloadFrRcvd = _McmVNETChStatsInvalPayloadFrRcvd_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 4, 1, 1, 15),
    _McmVNETChStatsInvalPayloadFrRcvd_Type()
)
mcmVNETChStatsInvalPayloadFrRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmVNETChStatsInvalPayloadFrRcvd.setStatus("mandatory")
_McmVNETChStatsInvalPUMPMsgRcvd_Type = Counter32
_McmVNETChStatsInvalPUMPMsgRcvd_Object = MibTableColumn
mcmVNETChStatsInvalPUMPMsgRcvd = _McmVNETChStatsInvalPUMPMsgRcvd_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 4, 1, 1, 16),
    _McmVNETChStatsInvalPUMPMsgRcvd_Type()
)
mcmVNETChStatsInvalPUMPMsgRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmVNETChStatsInvalPUMPMsgRcvd.setStatus("mandatory")
_McmVNETNetStatsGroup_ObjectIdentity = ObjectIdentity
mcmVNETNetStatsGroup = _McmVNETNetStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 4, 2)
)
_McmVNETNetStatsSucceedOutSVCCalls_Type = Counter32
_McmVNETNetStatsSucceedOutSVCCalls_Object = MibScalar
mcmVNETNetStatsSucceedOutSVCCalls = _McmVNETNetStatsSucceedOutSVCCalls_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 4, 2, 1),
    _McmVNETNetStatsSucceedOutSVCCalls_Type()
)
mcmVNETNetStatsSucceedOutSVCCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmVNETNetStatsSucceedOutSVCCalls.setStatus("mandatory")
_McmVNETNetStatsFailedOutSVCCalls_Type = Counter32
_McmVNETNetStatsFailedOutSVCCalls_Object = MibScalar
mcmVNETNetStatsFailedOutSVCCalls = _McmVNETNetStatsFailedOutSVCCalls_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 4, 2, 2),
    _McmVNETNetStatsFailedOutSVCCalls_Type()
)
mcmVNETNetStatsFailedOutSVCCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmVNETNetStatsFailedOutSVCCalls.setStatus("mandatory")
_McmVNETNetStatsAcceptedInCalls_Type = Counter32
_McmVNETNetStatsAcceptedInCalls_Object = MibScalar
mcmVNETNetStatsAcceptedInCalls = _McmVNETNetStatsAcceptedInCalls_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 4, 2, 3),
    _McmVNETNetStatsAcceptedInCalls_Type()
)
mcmVNETNetStatsAcceptedInCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmVNETNetStatsAcceptedInCalls.setStatus("mandatory")
_McmVNETNetStatsRejectedInCalls_Type = Counter32
_McmVNETNetStatsRejectedInCalls_Object = MibScalar
mcmVNETNetStatsRejectedInCalls = _McmVNETNetStatsRejectedInCalls_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 4, 2, 4),
    _McmVNETNetStatsRejectedInCalls_Type()
)
mcmVNETNetStatsRejectedInCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmVNETNetStatsRejectedInCalls.setStatus("mandatory")
_McmVNETNetStatsSucceedDNARequests_Type = Counter32
_McmVNETNetStatsSucceedDNARequests_Object = MibScalar
mcmVNETNetStatsSucceedDNARequests = _McmVNETNetStatsSucceedDNARequests_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 4, 2, 5),
    _McmVNETNetStatsSucceedDNARequests_Type()
)
mcmVNETNetStatsSucceedDNARequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmVNETNetStatsSucceedDNARequests.setStatus("mandatory")
_McmVNETNetStatsFailedDNARequests_Type = Counter32
_McmVNETNetStatsFailedDNARequests_Object = MibScalar
mcmVNETNetStatsFailedDNARequests = _McmVNETNetStatsFailedDNARequests_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 4, 2, 6),
    _McmVNETNetStatsFailedDNARequests_Type()
)
mcmVNETNetStatsFailedDNARequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmVNETNetStatsFailedDNARequests.setStatus("mandatory")
_McmVNETNetStatsFailedBuffAllocations_Type = Counter32
_McmVNETNetStatsFailedBuffAllocations_Object = MibScalar
mcmVNETNetStatsFailedBuffAllocations = _McmVNETNetStatsFailedBuffAllocations_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 4, 2, 7),
    _McmVNETNetStatsFailedBuffAllocations_Type()
)
mcmVNETNetStatsFailedBuffAllocations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmVNETNetStatsFailedBuffAllocations.setStatus("mandatory")
_McmVNETNetStatsNumActiveCalls_Type = Counter32
_McmVNETNetStatsNumActiveCalls_Object = MibScalar
mcmVNETNetStatsNumActiveCalls = _McmVNETNetStatsNumActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 4, 2, 8),
    _McmVNETNetStatsNumActiveCalls_Type()
)
mcmVNETNetStatsNumActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmVNETNetStatsNumActiveCalls.setStatus("mandatory")

# Managed Objects groups


# Notification objects

mcmVNETDownloadFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 0, 1)
)
mcmVNETDownloadFail.setObjects(
      *(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"),
        ("MICOM-4400-VOICE-NETWORK-MIB", "mcmVNETChCfgLimID"),
        ("MICOM-4400-VOICE-NETWORK-MIB", "mcmVNETChCfgChannelID"))
)
if mibBuilder.loadTexts:
    mcmVNETDownloadFail.setStatus(
        ""
    )

mcmVNETOutOfOrder = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 0, 2)
)
mcmVNETOutOfOrder.setObjects(
      *(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"),
        ("MICOM-4400-VOICE-NETWORK-MIB", "mcmVNETChCfgLimID"),
        ("MICOM-4400-VOICE-NETWORK-MIB", "mcmVNETChCfgChannelID"))
)
if mibBuilder.loadTexts:
    mcmVNETOutOfOrder.setStatus(
        ""
    )

mcmVNETOutOfOrderRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 0, 3)
)
mcmVNETOutOfOrderRecovered.setObjects(
      *(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"),
        ("MICOM-4400-VOICE-NETWORK-MIB", "mcmVNETChCfgLimID"),
        ("MICOM-4400-VOICE-NETWORK-MIB", "mcmVNETChCfgChannelID"))
)
if mibBuilder.loadTexts:
    mcmVNETOutOfOrderRecovered.setStatus(
        ""
    )

mcmVNETFailedToSyncUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 0, 4)
)
mcmVNETFailedToSyncUp.setObjects(
      *(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"),
        ("MICOM-4400-VOICE-NETWORK-MIB", "mcmVNETChCfgLimID"),
        ("MICOM-4400-VOICE-NETWORK-MIB", "mcmVNETChCfgChannelID"))
)
if mibBuilder.loadTexts:
    mcmVNETFailedToSyncUp.setStatus(
        ""
    )

mcmVNETFailedToSyncUpRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 0, 5)
)
mcmVNETFailedToSyncUpRecovered.setObjects(
      *(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"),
        ("MICOM-4400-VOICE-NETWORK-MIB", "mcmVNETChCfgLimID"),
        ("MICOM-4400-VOICE-NETWORK-MIB", "mcmVNETChCfgChannelID"))
)
if mibBuilder.loadTexts:
    mcmVNETFailedToSyncUpRecovered.setStatus(
        ""
    )

mcmVNETNoCVMCodeImage = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 0, 6)
)
mcmVNETNoCVMCodeImage.setObjects(
    ("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay")
)
if mibBuilder.loadTexts:
    mcmVNETNoCVMCodeImage.setStatus(
        ""
    )

mcmVNETNoTUVMCodeImage = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 0, 7)
)
mcmVNETNoTUVMCodeImage.setObjects(
    ("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay")
)
if mibBuilder.loadTexts:
    mcmVNETNoTUVMCodeImage.setStatus(
        ""
    )

mcmVNETNoDVMCodeImage = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 21, 0, 8)
)
mcmVNETNoDVMCodeImage.setObjects(
    ("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay")
)
if mibBuilder.loadTexts:
    mcmVNETNoDVMCodeImage.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MICOM-4400-VOICE-NETWORK-MIB",
    **{"micom-2vnet": micom_2vnet,
       "mcmVNETDownloadFail": mcmVNETDownloadFail,
       "mcmVNETOutOfOrder": mcmVNETOutOfOrder,
       "mcmVNETOutOfOrderRecovered": mcmVNETOutOfOrderRecovered,
       "mcmVNETFailedToSyncUp": mcmVNETFailedToSyncUp,
       "mcmVNETFailedToSyncUpRecovered": mcmVNETFailedToSyncUpRecovered,
       "mcmVNETNoCVMCodeImage": mcmVNETNoCVMCodeImage,
       "mcmVNETNoTUVMCodeImage": mcmVNETNoTUVMCodeImage,
       "mcmVNETNoDVMCodeImage": mcmVNETNoDVMCodeImage,
       "vnet-configuration": vnet_configuration,
       "mcmVNETChCfgTable": mcmVNETChCfgTable,
       "mcmVNETChCfgEntry": mcmVNETChCfgEntry,
       "mcmVNETChCfgLimID": mcmVNETChCfgLimID,
       "mcmVNETChCfgChannelID": mcmVNETChCfgChannelID,
       "mcmVNETChCfgVoiceProfile": mcmVNETChCfgVoiceProfile,
       "mcmVNETChCfgSwitchingProfile": mcmVNETChCfgSwitchingProfile,
       "mcmVNETChCfgInterfaceType": mcmVNETChCfgInterfaceType,
       "mcmVNETProfileCfgTable": mcmVNETProfileCfgTable,
       "mcmVNETProfileCfgEntry": mcmVNETProfileCfgEntry,
       "mcmVNETProfileCfgProfileNum": mcmVNETProfileCfgProfileNum,
       "mcmVNETProfileCfgMode": mcmVNETProfileCfgMode,
       "mcmVNETProfileCfgDigitizingRate": mcmVNETProfileCfgDigitizingRate,
       "mcmVNETProfileCfgInputLevelGain": mcmVNETProfileCfgInputLevelGain,
       "mcmVNETProfileCfgOutputLevelAttn": mcmVNETProfileCfgOutputLevelAttn,
       "mcmVNETProfileCfgBusyOutMode": mcmVNETProfileCfgBusyOutMode,
       "mcmVNETProfileCfgBandwidth": mcmVNETProfileCfgBandwidth,
       "mcmVNETProfileCfgBackground": mcmVNETProfileCfgBackground,
       "mcmVNETProfileCfgBRIPulseRate": mcmVNETProfileCfgBRIPulseRate,
       "mcmVNETProfileCfgEMSigFormat": mcmVNETProfileCfgEMSigFormat,
       "mcmVNETProfileCfgFXSSigFormat": mcmVNETProfileCfgFXSSigFormat,
       "mcmVNETProfileCfgDVMSigFormat": mcmVNETProfileCfgDVMSigFormat,
       "mcmVNETProfileCfgNumberOfRings": mcmVNETProfileCfgNumberOfRings,
       "mcmVNETProfileCfgEMAnalOper": mcmVNETProfileCfgEMAnalOper,
       "mcmVNETProfileCfgRingingFreq": mcmVNETProfileCfgRingingFreq,
       "mcmVNETProfileCfgFaxDigRate": mcmVNETProfileCfgFaxDigRate,
       "mcmVNETProfileCfgDiscSupervision": mcmVNETProfileCfgDiscSupervision,
       "mcmVNETProfileCfgLineImpedance": mcmVNETProfileCfgLineImpedance,
       "mcmVNETProfileCfgMaxOutputLevel": mcmVNETProfileCfgMaxOutputLevel,
       "mcmVNETProfileCfgRegenDelay": mcmVNETProfileCfgRegenDelay,
       "mcmVNETProfileCfgDialDigTimeLimit": mcmVNETProfileCfgDialDigTimeLimit,
       "mcmVNETProfileCfgMaxNumForDig": mcmVNETProfileCfgMaxNumForDig,
       "mcmVNETProfileCfgRegenFormat": mcmVNETProfileCfgRegenFormat,
       "mcmVNETProfileCfgCallProgTone": mcmVNETProfileCfgCallProgTone,
       "mcmVNETProfileCfgDTMFDetector": mcmVNETProfileCfgDTMFDetector,
       "mcmVNETProfileCfgJitters": mcmVNETProfileCfgJitters,
       "mcmVNETProfileCfgEchoCanceller": mcmVNETProfileCfgEchoCanceller,
       "mcmVNETProfileCfgAutoGainControl": mcmVNETProfileCfgAutoGainControl,
       "mcmVNETProfileCfgCompanderFormat": mcmVNETProfileCfgCompanderFormat,
       "mcmVNETProfileCfgPremiumVoice": mcmVNETProfileCfgPremiumVoice,
       "mcmVNETProfileCfgEndOfDialChar": mcmVNETProfileCfgEndOfDialChar,
       "mcmVNETProfileCfgBckGrndNoiseLevel": mcmVNETProfileCfgBckGrndNoiseLevel,
       "mcmVNETProfileCfgSilenceHngOvrTime": mcmVNETProfileCfgSilenceHngOvrTime,
       "mcmVNETProfileCfgIdlePattern": mcmVNETProfileCfgIdlePattern,
       "mcmVNETProfileCfgEcanFilterLength": mcmVNETProfileCfgEcanFilterLength,
       "mcmVNETProfileCfgEcanErlImprovement": mcmVNETProfileCfgEcanErlImprovement,
       "mcmVNETProfileCfgNoiseFloorOffset": mcmVNETProfileCfgNoiseFloorOffset,
       "mcmVNETProfileCfgDtmfGenBurstLength": mcmVNETProfileCfgDtmfGenBurstLength,
       "mcmVNETProfileCfgDtmRegenBurstLength": mcmVNETProfileCfgDtmRegenBurstLength,
       "mcmVNETSwProfCfgTable": mcmVNETSwProfCfgTable,
       "mcmVNETSwProfCfgEntry": mcmVNETSwProfCfgEntry,
       "mcmVNETSwProfCfgProfileNum": mcmVNETSwProfCfgProfileNum,
       "mcmVNETSwProfCfgOutCallRestrict": mcmVNETSwProfCfgOutCallRestrict,
       "mcmVNETSwProfCfgInCallRestrict": mcmVNETSwProfCfgInCallRestrict,
       "mcmVNETSwProfCfgCUGID": mcmVNETSwProfCfgCUGID,
       "mcmVNETSwProfCfgRestrictClassCd": mcmVNETSwProfCfgRestrictClassCd,
       "mcmVNETSwProfCfgAutoCallEntNum": mcmVNETSwProfCfgAutoCallEntNum,
       "mcmVNETSwProfCfgCallNegStrategy": mcmVNETSwProfCfgCallNegStrategy,
       "mcmVNETSwProfCfgTransmitPriority": mcmVNETSwProfCfgTransmitPriority,
       "mcmVNETSwProfCfgAutoCallType": mcmVNETSwProfCfgAutoCallType,
       "mcmVNETSwProfCfgAddServerSelect": mcmVNETSwProfCfgAddServerSelect,
       "mcmVNETSwProfCfgOutCallMode": mcmVNETSwProfCfgOutCallMode,
       "mcmVNETIngressDigFilterTable": mcmVNETIngressDigFilterTable,
       "mcmVNETIngressDigFilterEntry": mcmVNETIngressDigFilterEntry,
       "mcmVNETIngressDigFilterIndex": mcmVNETIngressDigFilterIndex,
       "mcmVNETIngressDigFilterIngressNum": mcmVNETIngressDigFilterIngressNum,
       "mcmVNETIngressDigFilterManipString": mcmVNETIngressDigFilterManipString,
       "mcmVNETEgressDigManipTable": mcmVNETEgressDigManipTable,
       "mcmVNETEgressDigManipEntry": mcmVNETEgressDigManipEntry,
       "mcmVNETEgressDigManipIndex": mcmVNETEgressDigManipIndex,
       "mcmVNETEgressDigManipPhoneNum": mcmVNETEgressDigManipPhoneNum,
       "mcmVNETEgressDigManipString": mcmVNETEgressDigManipString,
       "mcmVNETEgressDigManipChIDList": mcmVNETEgressDigManipChIDList,
       "nvmVNETChCfgTable": nvmVNETChCfgTable,
       "nvmVNETChCfgEntry": nvmVNETChCfgEntry,
       "nvmVNETChCfgLimID": nvmVNETChCfgLimID,
       "nvmVNETChCfgChannelID": nvmVNETChCfgChannelID,
       "nvmVNETChCfgVoiceProfile": nvmVNETChCfgVoiceProfile,
       "nvmVNETChCfgSwitchingProfile": nvmVNETChCfgSwitchingProfile,
       "nvmVNETChCfgInterfaceType": nvmVNETChCfgInterfaceType,
       "nvmVNETProfileCfgTable": nvmVNETProfileCfgTable,
       "nvmVNETProfileCfgEntry": nvmVNETProfileCfgEntry,
       "nvmVNETProfileCfgProfileNum": nvmVNETProfileCfgProfileNum,
       "nvmVNETProfileCfgMode": nvmVNETProfileCfgMode,
       "nvmVNETProfileCfgDigitizingRate": nvmVNETProfileCfgDigitizingRate,
       "nvmVNETProfileCfgInputLevelGain": nvmVNETProfileCfgInputLevelGain,
       "nvmVNETProfileCfgOutputLevelAttn": nvmVNETProfileCfgOutputLevelAttn,
       "nvmVNETProfileCfgBusyOutMode": nvmVNETProfileCfgBusyOutMode,
       "nvmVNETProfileCfgBandwidth": nvmVNETProfileCfgBandwidth,
       "nvmVNETProfileCfgBackground": nvmVNETProfileCfgBackground,
       "nvmVNETProfileCfgBRIPulseRate": nvmVNETProfileCfgBRIPulseRate,
       "nvmVNETProfileCfgEMSigFormat": nvmVNETProfileCfgEMSigFormat,
       "nvmVNETProfileCfgFXSSigFormat": nvmVNETProfileCfgFXSSigFormat,
       "nvmVNETProfileCfgDVMSigFormat": nvmVNETProfileCfgDVMSigFormat,
       "nvmVNETProfileCfgNumberOfRings": nvmVNETProfileCfgNumberOfRings,
       "nvmVNETProfileCfgEMAnalOper": nvmVNETProfileCfgEMAnalOper,
       "nvmVNETProfileCfgRingingFreq": nvmVNETProfileCfgRingingFreq,
       "nvmVNETProfileCfgFaxDigRate": nvmVNETProfileCfgFaxDigRate,
       "nvmVNETProfileCfgDiscSupervision": nvmVNETProfileCfgDiscSupervision,
       "nvmVNETProfileCfgLineImpedance": nvmVNETProfileCfgLineImpedance,
       "nvmVNETProfileCfgMaxOutputLevel": nvmVNETProfileCfgMaxOutputLevel,
       "nvmVNETProfileCfgRegenDelay": nvmVNETProfileCfgRegenDelay,
       "nvmVNETProfileCfgDialDigTimeLimit": nvmVNETProfileCfgDialDigTimeLimit,
       "nvmVNETProfileCfgMaxNumForDig": nvmVNETProfileCfgMaxNumForDig,
       "nvmVNETProfileCfgRegenFormat": nvmVNETProfileCfgRegenFormat,
       "nvmVNETProfileCfgCallProgTone": nvmVNETProfileCfgCallProgTone,
       "nvmVNETProfileCfgDTMFDetector": nvmVNETProfileCfgDTMFDetector,
       "nvmVNETProfileCfgJitters": nvmVNETProfileCfgJitters,
       "nvmVNETProfileCfgEchoCanceller": nvmVNETProfileCfgEchoCanceller,
       "nvmVNETProfileCfgAutoGainControl": nvmVNETProfileCfgAutoGainControl,
       "nvmVNETProfileCfgCompanderFormat": nvmVNETProfileCfgCompanderFormat,
       "nvmVNETProfileCfgPremiumVoice": nvmVNETProfileCfgPremiumVoice,
       "nvmVNETProfileCfgEndOfDialChar": nvmVNETProfileCfgEndOfDialChar,
       "nvmVNETProfileCfgBckGrndNoiseLevel": nvmVNETProfileCfgBckGrndNoiseLevel,
       "nvmVNETProfileCfgSilenceHngOvrTime": nvmVNETProfileCfgSilenceHngOvrTime,
       "nvmVNETProfileCfgIdlePattern": nvmVNETProfileCfgIdlePattern,
       "nvmVNETProfileCfgEcanFilterLength": nvmVNETProfileCfgEcanFilterLength,
       "nvmVNETProfileCfgEcanErlImprovement": nvmVNETProfileCfgEcanErlImprovement,
       "nvmVNETProfileCfgNoiseFloorOffset": nvmVNETProfileCfgNoiseFloorOffset,
       "nvmVNETProfileCfgDtmfGenBurstLength": nvmVNETProfileCfgDtmfGenBurstLength,
       "nvmVNETProfileCfgDtmRegenBurstLength": nvmVNETProfileCfgDtmRegenBurstLength,
       "nvmVNETSwProfCfgTable": nvmVNETSwProfCfgTable,
       "nvmVNETSwProfCfgEntry": nvmVNETSwProfCfgEntry,
       "nvmVNETSwProfCfgProfileNum": nvmVNETSwProfCfgProfileNum,
       "nvmVNETSwProfCfgOutCallRestrict": nvmVNETSwProfCfgOutCallRestrict,
       "nvmVNETSwProfCfgInCallRestrict": nvmVNETSwProfCfgInCallRestrict,
       "nvmVNETSwProfCfgCUGID": nvmVNETSwProfCfgCUGID,
       "nvmVNETSwProfCfgRestrictClassCd": nvmVNETSwProfCfgRestrictClassCd,
       "nvmVNETSwProfCfgAutoCallEntNum": nvmVNETSwProfCfgAutoCallEntNum,
       "nvmVNETSwProfCfgCallNegStrategy": nvmVNETSwProfCfgCallNegStrategy,
       "nvmVNETSwProfCfgTransmitPriority": nvmVNETSwProfCfgTransmitPriority,
       "nvmVNETSwProfCfgAutoCallType": nvmVNETSwProfCfgAutoCallType,
       "nvmVNETSwProfCfgAddServerSelect": nvmVNETSwProfCfgAddServerSelect,
       "nvmVNETSwProfCfgOutCallMode": nvmVNETSwProfCfgOutCallMode,
       "nvmVNETIngressDigFilterTable": nvmVNETIngressDigFilterTable,
       "nvmVNETIngressDigFilterEntry": nvmVNETIngressDigFilterEntry,
       "nvmVNETIngressDigFilterIndex": nvmVNETIngressDigFilterIndex,
       "nvmVNETIngressDigFilterIngressNum": nvmVNETIngressDigFilterIngressNum,
       "nvmVNETIngressDigFilterManipString": nvmVNETIngressDigFilterManipString,
       "nvmVNETEgressDigManipTable": nvmVNETEgressDigManipTable,
       "nvmVNETEgressDigManipEntry": nvmVNETEgressDigManipEntry,
       "nvmVNETEgressDigManipIndex": nvmVNETEgressDigManipIndex,
       "nvmVNETEgressDigManipPhoneNum": nvmVNETEgressDigManipPhoneNum,
       "nvmVNETEgressDigManipString": nvmVNETEgressDigManipString,
       "nvmVNETEgressDigManipChIDList": nvmVNETEgressDigManipChIDList,
       "vnet-control": vnet_control,
       "mcmVNETChControlTable": mcmVNETChControlTable,
       "mcmVNETChControlEntry": mcmVNETChControlEntry,
       "mcmVNETChControlLimID": mcmVNETChControlLimID,
       "mcmVNETChControlChannelID": mcmVNETChControlChannelID,
       "mcmVNETChControlActionCmd": mcmVNETChControlActionCmd,
       "mcmVNETSysControlActionCmd": mcmVNETSysControlActionCmd,
       "vnet-status": vnet_status,
       "mcmVNETChStatusTable": mcmVNETChStatusTable,
       "mcmVNETChStatusEntry": mcmVNETChStatusEntry,
       "mcmVNETChStatusLimID": mcmVNETChStatusLimID,
       "mcmVNETChStatusChannelID": mcmVNETChStatusChannelID,
       "mcmVNETChStatusInterfaceType": mcmVNETChStatusInterfaceType,
       "mcmVNETChStatusInterfaceSwID": mcmVNETChStatusInterfaceSwID,
       "mcmVNETChStatusEMType": mcmVNETChStatusEMType,
       "mcmVNETChStatusModelID": mcmVNETChStatusModelID,
       "mcmVNETChStatusDSPOperation": mcmVNETChStatusDSPOperation,
       "mcmVNETChStatusNetworkConnect": mcmVNETChStatusNetworkConnect,
       "mcmVNETChStatusRemoteChHwType": mcmVNETChStatusRemoteChHwType,
       "mcmVNETChStatusRemoteChNodeName": mcmVNETChStatusRemoteChNodeName,
       "mcmVNETChStatusRemoteChNum": mcmVNETChStatusRemoteChNum,
       "mcmVNETChStatusRemoteChIfType": mcmVNETChStatusRemoteChIfType,
       "mcmVNETChStatusRemoteFrameIfVer": mcmVNETChStatusRemoteFrameIfVer,
       "mcmVNETChStatusRemoteChVoiceAlg": mcmVNETChStatusRemoteChVoiceAlg,
       "mcmVNETChStatusRemoteChFaxAlg": mcmVNETChStatusRemoteChFaxAlg,
       "mcmVNETChStatusRemoteChModemAlg": mcmVNETChStatusRemoteChModemAlg,
       "mcmVNETChStatusSelfTestResult": mcmVNETChStatusSelfTestResult,
       "mcmVNETChStatusFlashEPROM": mcmVNETChStatusFlashEPROM,
       "mcmVNETChStatusEPROM": mcmVNETChStatusEPROM,
       "mcmVNETChStatusDspPROMVer": mcmVNETChStatusDspPROMVer,
       "mcmVNETChStatusPROMID": mcmVNETChStatusPROMID,
       "mcmVNETChStatusInputLevel": mcmVNETChStatusInputLevel,
       "voiceSysStatusGroup": voiceSysStatusGroup,
       "voiceSysStatusPhoneRegistrationStatus": voiceSysStatusPhoneRegistrationStatus,
       "vnet-statistics": vnet_statistics,
       "mcmVNETChStatsTable": mcmVNETChStatsTable,
       "mcmVNETChStatsEntry": mcmVNETChStatsEntry,
       "mcmVNETChStatsLimID": mcmVNETChStatsLimID,
       "mcmVNETChStatsChannelID": mcmVNETChStatsChannelID,
       "mcmVNETChStatsOutCallConnTime": mcmVNETChStatsOutCallConnTime,
       "mcmVNETChStatsInCallConnTime": mcmVNETChStatsInCallConnTime,
       "mcmVNETChStatsOutCallsSucceded": mcmVNETChStatsOutCallsSucceded,
       "mcmVNETChStatsOutCallsFailed": mcmVNETChStatsOutCallsFailed,
       "mcmVNETChStatsInCallsAccepted": mcmVNETChStatsInCallsAccepted,
       "mcmVNETChStatsInCallsRejected": mcmVNETChStatsInCallsRejected,
       "mcmVNETChStatsNumberOfResets": mcmVNETChStatsNumberOfResets,
       "mcmVNETChStatsNumberOfRetries": mcmVNETChStatsNumberOfRetries,
       "mcmVNETChStatsBBCFramesRcvd": mcmVNETChStatsBBCFramesRcvd,
       "mcmVNETChStatsBEOFFramesRcvd": mcmVNETChStatsBEOFFramesRcvd,
       "mcmVNETChStatsLostSpeechFrames": mcmVNETChStatsLostSpeechFrames,
       "mcmVNETChStatsLostControlFrames": mcmVNETChStatsLostControlFrames,
       "mcmVNETChStatsInvalPayloadFrRcvd": mcmVNETChStatsInvalPayloadFrRcvd,
       "mcmVNETChStatsInvalPUMPMsgRcvd": mcmVNETChStatsInvalPUMPMsgRcvd,
       "mcmVNETNetStatsGroup": mcmVNETNetStatsGroup,
       "mcmVNETNetStatsSucceedOutSVCCalls": mcmVNETNetStatsSucceedOutSVCCalls,
       "mcmVNETNetStatsFailedOutSVCCalls": mcmVNETNetStatsFailedOutSVCCalls,
       "mcmVNETNetStatsAcceptedInCalls": mcmVNETNetStatsAcceptedInCalls,
       "mcmVNETNetStatsRejectedInCalls": mcmVNETNetStatsRejectedInCalls,
       "mcmVNETNetStatsSucceedDNARequests": mcmVNETNetStatsSucceedDNARequests,
       "mcmVNETNetStatsFailedDNARequests": mcmVNETNetStatsFailedDNARequests,
       "mcmVNETNetStatsFailedBuffAllocations": mcmVNETNetStatsFailedBuffAllocations,
       "mcmVNETNetStatsNumActiveCalls": mcmVNETNetStatsNumActiveCalls}
)
