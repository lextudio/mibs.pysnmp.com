# SNMP MIB module (VOICE-OPT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VOICE-OPT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:13:03 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""




class PhysicalPortNumber(Integer32):
    """Custom type PhysicalPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 54),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Codex_ObjectIdentity = ObjectIdentity
codex = _Codex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449)
)
_CdxProductSpecific_ObjectIdentity = ObjectIdentity
cdxProductSpecific = _CdxProductSpecific_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2)
)
_Cdx6500_ObjectIdentity = ObjectIdentity
cdx6500 = _Cdx6500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1)
)
_Cdx6500Configuration_ObjectIdentity = ObjectIdentity
cdx6500Configuration = _Cdx6500Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2)
)
_Cdx6500CfgProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500CfgProtocolGroup = _Cdx6500CfgProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1)
)
_Cdx6500PCTPortProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500PCTPortProtocolGroup = _Cdx6500PCTPortProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1)
)
_Cdx6500PCTVoicePortTable_ObjectIdentity = ObjectIdentity
cdx6500PCTVoicePortTable = _Cdx6500PCTVoicePortTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25)
)
_Cdx6500PPCTVoicePortTable_Object = MibTable
cdx6500PPCTVoicePortTable = _Cdx6500PPCTVoicePortTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1)
)
if mibBuilder.loadTexts:
    cdx6500PPCTVoicePortTable.setStatus("mandatory")
_Cdx6500PPCTVoicePortEntry_Object = MibTableRow
cdx6500PPCTVoicePortEntry = _Cdx6500PPCTVoicePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1)
)
cdx6500PPCTVoicePortEntry.setIndexNames(
    (0, "VOICE-OPT-MIB", "cdx6500VoiceCfgPortNumber"),
)
if mibBuilder.loadTexts:
    cdx6500PPCTVoicePortEntry.setStatus("mandatory")


class _Cdx6500VoiceCfgPortNumber_Type(Integer32):
    """Custom type cdx6500VoiceCfgPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cdx6500VoiceCfgPortNumber_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgPortNumber_Object = MibTableColumn
cdx6500VoiceCfgPortNumber = _Cdx6500VoiceCfgPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 1),
    _Cdx6500VoiceCfgPortNumber_Type()
)
cdx6500VoiceCfgPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgPortNumber.setStatus("mandatory")


class _Cdx6500VoiceCfgPortType_Type(Integer32):
    """Custom type cdx6500VoiceCfgPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            43
        )
    )
    namedValues = NamedValues(
        ("voice", 43)
    )


_Cdx6500VoiceCfgPortType_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgPortType_Object = MibTableColumn
cdx6500VoiceCfgPortType = _Cdx6500VoiceCfgPortType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 2),
    _Cdx6500VoiceCfgPortType_Type()
)
cdx6500VoiceCfgPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgPortType.setStatus("mandatory")


class _Cdx6500VoiceCfgInterfaceType_Type(Integer32):
    """Custom type cdx6500VoiceCfgInterfaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              100)
        )
    )
    namedValues = NamedValues(
        *(("eAndM2", 1),
          ("eAndM4", 2),
          ("fxo", 3),
          ("fxs", 4),
          ("nc", 100))
    )


_Cdx6500VoiceCfgInterfaceType_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgInterfaceType_Object = MibTableColumn
cdx6500VoiceCfgInterfaceType = _Cdx6500VoiceCfgInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 3),
    _Cdx6500VoiceCfgInterfaceType_Type()
)
cdx6500VoiceCfgInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgInterfaceType.setStatus("mandatory")


class _Cdx6500VoiceCfgSignalingType_Type(Integer32):
    """Custom type cdx6500VoiceCfgSignalingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              100)
        )
    )
    namedValues = NamedValues(
        *(("i", 1),
          ("ii", 2),
          ("iii", 4),
          ("nc", 100),
          ("v", 3))
    )


_Cdx6500VoiceCfgSignalingType_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgSignalingType_Object = MibTableColumn
cdx6500VoiceCfgSignalingType = _Cdx6500VoiceCfgSignalingType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 4),
    _Cdx6500VoiceCfgSignalingType_Type()
)
cdx6500VoiceCfgSignalingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgSignalingType.setStatus("mandatory")


class _Cdx6500VoiceCfgELeadFilter_Type(Integer32):
    """Custom type cdx6500VoiceCfgELeadFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              100)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("nc", 100))
    )


_Cdx6500VoiceCfgELeadFilter_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgELeadFilter_Object = MibTableColumn
cdx6500VoiceCfgELeadFilter = _Cdx6500VoiceCfgELeadFilter_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 5),
    _Cdx6500VoiceCfgELeadFilter_Type()
)
cdx6500VoiceCfgELeadFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgELeadFilter.setStatus("mandatory")


class _Cdx6500VoiceCfgHybridFXS_Type(Integer32):
    """Custom type cdx6500VoiceCfgHybridFXS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              8,
              9,
              100)
        )
    )
    namedValues = NamedValues(
        *(("belgium", 8),
          ("canada", 2),
          ("france", 9),
          ("germany", 3),
          ("nc", 100),
          ("sixHundred", 1),
          ("uk", 5))
    )


_Cdx6500VoiceCfgHybridFXS_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgHybridFXS_Object = MibTableColumn
cdx6500VoiceCfgHybridFXS = _Cdx6500VoiceCfgHybridFXS_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 6),
    _Cdx6500VoiceCfgHybridFXS_Type()
)
cdx6500VoiceCfgHybridFXS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgHybridFXS.setStatus("mandatory")


class _Cdx6500VoiceCfgHybridEAndM2_Type(Integer32):
    """Custom type cdx6500VoiceCfgHybridEAndM2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              10,
              100)
        )
    )
    namedValues = NamedValues(
        *(("germany", 3),
          ("nc", 100),
          ("sixHundred", 1),
          ("uk", 10))
    )


_Cdx6500VoiceCfgHybridEAndM2_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgHybridEAndM2_Object = MibTableColumn
cdx6500VoiceCfgHybridEAndM2 = _Cdx6500VoiceCfgHybridEAndM2_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 7),
    _Cdx6500VoiceCfgHybridEAndM2_Type()
)
cdx6500VoiceCfgHybridEAndM2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgHybridEAndM2.setStatus("mandatory")


class _Cdx6500VoiceCfgSignalingMode_Type(Integer32):
    """Custom type cdx6500VoiceCfgSignalingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              100)
        )
    )
    namedValues = NamedValues(
        *(("nc", 100),
          ("none", 2),
          ("normal", 1))
    )


_Cdx6500VoiceCfgSignalingMode_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgSignalingMode_Object = MibTableColumn
cdx6500VoiceCfgSignalingMode = _Cdx6500VoiceCfgSignalingMode_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 8),
    _Cdx6500VoiceCfgSignalingMode_Type()
)
cdx6500VoiceCfgSignalingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgSignalingMode.setStatus("mandatory")


class _Cdx6500VoiceCfgSignalingControl_Type(Integer32):
    """Custom type cdx6500VoiceCfgSignalingControl based on Integer32"""
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
              100)
        )
    )
    namedValues = NamedValues(
        *(("delay", 4),
          ("immediate", 1),
          ("masterColisee", 5),
          ("nc", 100),
          ("seizureAcknowledge", 7),
          ("slaveColisee", 6),
          ("transparent", 3),
          ("wink", 2))
    )


_Cdx6500VoiceCfgSignalingControl_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgSignalingControl_Object = MibTableColumn
cdx6500VoiceCfgSignalingControl = _Cdx6500VoiceCfgSignalingControl_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 9),
    _Cdx6500VoiceCfgSignalingControl_Type()
)
cdx6500VoiceCfgSignalingControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgSignalingControl.setStatus("mandatory")


class _Cdx6500VoiceCfgNoOfDigitsToCollect_Type(Integer32):
    """Custom type cdx6500VoiceCfgNoOfDigitsToCollect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 11),
    )


_Cdx6500VoiceCfgNoOfDigitsToCollect_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgNoOfDigitsToCollect_Object = MibTableColumn
cdx6500VoiceCfgNoOfDigitsToCollect = _Cdx6500VoiceCfgNoOfDigitsToCollect_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 10),
    _Cdx6500VoiceCfgNoOfDigitsToCollect_Type()
)
cdx6500VoiceCfgNoOfDigitsToCollect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgNoOfDigitsToCollect.setStatus("deprecated")


class _Cdx6500VoiceCfgNoOfRings_Type(Integer32):
    """Custom type cdx6500VoiceCfgNoOfRings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_Cdx6500VoiceCfgNoOfRings_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgNoOfRings_Object = MibTableColumn
cdx6500VoiceCfgNoOfRings = _Cdx6500VoiceCfgNoOfRings_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 11),
    _Cdx6500VoiceCfgNoOfRings_Type()
)
cdx6500VoiceCfgNoOfRings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgNoOfRings.setStatus("mandatory")


class _Cdx6500VoiceCfgPCMMode_Type(Integer32):
    """Custom type cdx6500VoiceCfgPCMMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              100)
        )
    )
    namedValues = NamedValues(
        *(("aLaw", 1),
          ("muLaw", 2),
          ("nc", 100))
    )


_Cdx6500VoiceCfgPCMMode_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgPCMMode_Object = MibTableColumn
cdx6500VoiceCfgPCMMode = _Cdx6500VoiceCfgPCMMode_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 12),
    _Cdx6500VoiceCfgPCMMode_Type()
)
cdx6500VoiceCfgPCMMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgPCMMode.setStatus("mandatory")


class _Cdx6500VoiceCfgCompressionRate_Type(Integer32):
    """Custom type cdx6500VoiceCfgCompressionRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              12,
              13,
              100)
        )
    )
    namedValues = NamedValues(
        *(("cBD16K", 4),
          ("cBD8K", 3),
          ("cD16K", 2),
          ("cD8K", 1),
          ("cE16Kb", 13),
          ("cE8Kb", 12),
          ("nc", 100))
    )


_Cdx6500VoiceCfgCompressionRate_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgCompressionRate_Object = MibTableColumn
cdx6500VoiceCfgCompressionRate = _Cdx6500VoiceCfgCompressionRate_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 13),
    _Cdx6500VoiceCfgCompressionRate_Type()
)
cdx6500VoiceCfgCompressionRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgCompressionRate.setStatus("mandatory")


class _Cdx6500VoiceCfgDSIControl_Type(Integer32):
    """Custom type cdx6500VoiceCfgDSIControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              100)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("nc", 100))
    )


_Cdx6500VoiceCfgDSIControl_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgDSIControl_Object = MibTableColumn
cdx6500VoiceCfgDSIControl = _Cdx6500VoiceCfgDSIControl_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 14),
    _Cdx6500VoiceCfgDSIControl_Type()
)
cdx6500VoiceCfgDSIControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgDSIControl.setStatus("mandatory")


class _Cdx6500VoiceCfgSmoothingDelay_Type(Integer32):
    """Custom type cdx6500VoiceCfgSmoothingDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 150),
    )


_Cdx6500VoiceCfgSmoothingDelay_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgSmoothingDelay_Object = MibTableColumn
cdx6500VoiceCfgSmoothingDelay = _Cdx6500VoiceCfgSmoothingDelay_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 15),
    _Cdx6500VoiceCfgSmoothingDelay_Type()
)
cdx6500VoiceCfgSmoothingDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgSmoothingDelay.setStatus("mandatory")


class _Cdx6500VoiceCfgEchoControl_Type(Integer32):
    """Custom type cdx6500VoiceCfgEchoControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              100)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("nc", 100))
    )


_Cdx6500VoiceCfgEchoControl_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgEchoControl_Object = MibTableColumn
cdx6500VoiceCfgEchoControl = _Cdx6500VoiceCfgEchoControl_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 16),
    _Cdx6500VoiceCfgEchoControl_Type()
)
cdx6500VoiceCfgEchoControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgEchoControl.setStatus("mandatory")


class _Cdx6500VoiceCfgEchoReturnLoss_Type(Integer32):
    """Custom type cdx6500VoiceCfgEchoReturnLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              100)
        )
    )
    namedValues = NamedValues(
        *(("minus12", 5),
          ("minus3", 2),
          ("minus6", 3),
          ("minus9", 4),
          ("nc", 100))
    )


_Cdx6500VoiceCfgEchoReturnLoss_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgEchoReturnLoss_Object = MibTableColumn
cdx6500VoiceCfgEchoReturnLoss = _Cdx6500VoiceCfgEchoReturnLoss_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 17),
    _Cdx6500VoiceCfgEchoReturnLoss_Type()
)
cdx6500VoiceCfgEchoReturnLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgEchoReturnLoss.setStatus("mandatory")
_Cdx6500VoiceCfgTxInputSignalLevel_Type = DisplayString
_Cdx6500VoiceCfgTxInputSignalLevel_Object = MibTableColumn
cdx6500VoiceCfgTxInputSignalLevel = _Cdx6500VoiceCfgTxInputSignalLevel_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 18),
    _Cdx6500VoiceCfgTxInputSignalLevel_Type()
)
cdx6500VoiceCfgTxInputSignalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgTxInputSignalLevel.setStatus("mandatory")
_Cdx6500VoiceCfgRxOutputSignalLevel_Type = DisplayString
_Cdx6500VoiceCfgRxOutputSignalLevel_Object = MibTableColumn
cdx6500VoiceCfgRxOutputSignalLevel = _Cdx6500VoiceCfgRxOutputSignalLevel_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 19),
    _Cdx6500VoiceCfgRxOutputSignalLevel_Type()
)
cdx6500VoiceCfgRxOutputSignalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgRxOutputSignalLevel.setStatus("mandatory")


class _Cdx6500VoiceCfgFaxSupport_Type(Integer32):
    """Custom type cdx6500VoiceCfgFaxSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              100)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("nc", 100))
    )


_Cdx6500VoiceCfgFaxSupport_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgFaxSupport_Object = MibTableColumn
cdx6500VoiceCfgFaxSupport = _Cdx6500VoiceCfgFaxSupport_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 20),
    _Cdx6500VoiceCfgFaxSupport_Type()
)
cdx6500VoiceCfgFaxSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgFaxSupport.setStatus("mandatory")


class _Cdx6500VoiceCfgFaxRates_Type(Integer32):
    """Custom type cdx6500VoiceCfgFaxRates based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              100)
        )
    )
    namedValues = NamedValues(
        *(("fr4800", 2),
          ("fr9600", 1),
          ("nc", 100))
    )


_Cdx6500VoiceCfgFaxRates_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgFaxRates_Object = MibTableColumn
cdx6500VoiceCfgFaxRates = _Cdx6500VoiceCfgFaxRates_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 21),
    _Cdx6500VoiceCfgFaxRates_Type()
)
cdx6500VoiceCfgFaxRates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgFaxRates.setStatus("mandatory")


class _Cdx6500VoiceCfgVoiceBandDetection_Type(Integer32):
    """Custom type cdx6500VoiceCfgVoiceBandDetection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              100)
        )
    )
    namedValues = NamedValues(
        *(("nc", 100),
          ("no", 2),
          ("yes", 1))
    )


_Cdx6500VoiceCfgVoiceBandDetection_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgVoiceBandDetection_Object = MibTableColumn
cdx6500VoiceCfgVoiceBandDetection = _Cdx6500VoiceCfgVoiceBandDetection_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 22),
    _Cdx6500VoiceCfgVoiceBandDetection_Type()
)
cdx6500VoiceCfgVoiceBandDetection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgVoiceBandDetection.setStatus("mandatory")


class _Cdx6500VoiceCfgAutoCallMnemonic_Type(DisplayString):
    """Custom type cdx6500VoiceCfgAutoCallMnemonic based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Cdx6500VoiceCfgAutoCallMnemonic_Type.__name__ = "DisplayString"
_Cdx6500VoiceCfgAutoCallMnemonic_Object = MibTableColumn
cdx6500VoiceCfgAutoCallMnemonic = _Cdx6500VoiceCfgAutoCallMnemonic_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 23),
    _Cdx6500VoiceCfgAutoCallMnemonic_Type()
)
cdx6500VoiceCfgAutoCallMnemonic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgAutoCallMnemonic.setStatus("mandatory")


class _Cdx6500VoiceCfgCallControl_Type(Integer32):
    """Custom type cdx6500VoiceCfgCallControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              100)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("nc", 100),
          ("offhook", 1),
          ("switched", 3))
    )


_Cdx6500VoiceCfgCallControl_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgCallControl_Object = MibTableColumn
cdx6500VoiceCfgCallControl = _Cdx6500VoiceCfgCallControl_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 24),
    _Cdx6500VoiceCfgCallControl_Type()
)
cdx6500VoiceCfgCallControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgCallControl.setStatus("mandatory")


class _Cdx6500VoiceCfgAutoCallTimeout_Type(Integer32):
    """Custom type cdx6500VoiceCfgAutoCallTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 255),
    )


_Cdx6500VoiceCfgAutoCallTimeout_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgAutoCallTimeout_Object = MibTableColumn
cdx6500VoiceCfgAutoCallTimeout = _Cdx6500VoiceCfgAutoCallTimeout_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 25),
    _Cdx6500VoiceCfgAutoCallTimeout_Type()
)
cdx6500VoiceCfgAutoCallTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgAutoCallTimeout.setStatus("mandatory")


class _Cdx6500VoiceCfgCallRetries_Type(Integer32):
    """Custom type cdx6500VoiceCfgCallRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Cdx6500VoiceCfgCallRetries_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgCallRetries_Object = MibTableColumn
cdx6500VoiceCfgCallRetries = _Cdx6500VoiceCfgCallRetries_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 26),
    _Cdx6500VoiceCfgCallRetries_Type()
)
cdx6500VoiceCfgCallRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgCallRetries.setStatus("mandatory")


class _Cdx6500VoiceCfgGroupSubaddress_Type(Integer32):
    """Custom type cdx6500VoiceCfgGroupSubaddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_Cdx6500VoiceCfgGroupSubaddress_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgGroupSubaddress_Object = MibTableColumn
cdx6500VoiceCfgGroupSubaddress = _Cdx6500VoiceCfgGroupSubaddress_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 27),
    _Cdx6500VoiceCfgGroupSubaddress_Type()
)
cdx6500VoiceCfgGroupSubaddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgGroupSubaddress.setStatus("mandatory")


class _Cdx6500VoiceCfgBilling_Type(Integer32):
    """Custom type cdx6500VoiceCfgBilling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              100)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("nc", 100))
    )


_Cdx6500VoiceCfgBilling_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgBilling_Object = MibTableColumn
cdx6500VoiceCfgBilling = _Cdx6500VoiceCfgBilling_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 28),
    _Cdx6500VoiceCfgBilling_Type()
)
cdx6500VoiceCfgBilling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgBilling.setStatus("mandatory")


class _Cdx6500VoiceCfgRxSignalingStateChangeFilter_Type(Integer32):
    """Custom type cdx6500VoiceCfgRxSignalingStateChangeFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Cdx6500VoiceCfgRxSignalingStateChangeFilter_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgRxSignalingStateChangeFilter_Object = MibTableColumn
cdx6500VoiceCfgRxSignalingStateChangeFilter = _Cdx6500VoiceCfgRxSignalingStateChangeFilter_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 29),
    _Cdx6500VoiceCfgRxSignalingStateChangeFilter_Type()
)
cdx6500VoiceCfgRxSignalingStateChangeFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgRxSignalingStateChangeFilter.setStatus("mandatory")


class _Cdx6500VoiceCfgT1E1RxIdleOnhookState_Type(DisplayString):
    """Custom type cdx6500VoiceCfgT1E1RxIdleOnhookState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Cdx6500VoiceCfgT1E1RxIdleOnhookState_Type.__name__ = "DisplayString"
_Cdx6500VoiceCfgT1E1RxIdleOnhookState_Object = MibTableColumn
cdx6500VoiceCfgT1E1RxIdleOnhookState = _Cdx6500VoiceCfgT1E1RxIdleOnhookState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 30),
    _Cdx6500VoiceCfgT1E1RxIdleOnhookState_Type()
)
cdx6500VoiceCfgT1E1RxIdleOnhookState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgT1E1RxIdleOnhookState.setStatus("mandatory")


class _Cdx6500VoiceCfgT1E1TxIdleOnhookState_Type(DisplayString):
    """Custom type cdx6500VoiceCfgT1E1TxIdleOnhookState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Cdx6500VoiceCfgT1E1TxIdleOnhookState_Type.__name__ = "DisplayString"
_Cdx6500VoiceCfgT1E1TxIdleOnhookState_Object = MibTableColumn
cdx6500VoiceCfgT1E1TxIdleOnhookState = _Cdx6500VoiceCfgT1E1TxIdleOnhookState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 31),
    _Cdx6500VoiceCfgT1E1TxIdleOnhookState_Type()
)
cdx6500VoiceCfgT1E1TxIdleOnhookState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgT1E1TxIdleOnhookState.setStatus("mandatory")


class _Cdx6500VoiceCfgT1E1RxActiveOffhookState_Type(DisplayString):
    """Custom type cdx6500VoiceCfgT1E1RxActiveOffhookState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Cdx6500VoiceCfgT1E1RxActiveOffhookState_Type.__name__ = "DisplayString"
_Cdx6500VoiceCfgT1E1RxActiveOffhookState_Object = MibTableColumn
cdx6500VoiceCfgT1E1RxActiveOffhookState = _Cdx6500VoiceCfgT1E1RxActiveOffhookState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 32),
    _Cdx6500VoiceCfgT1E1RxActiveOffhookState_Type()
)
cdx6500VoiceCfgT1E1RxActiveOffhookState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgT1E1RxActiveOffhookState.setStatus("mandatory")


class _Cdx6500VoiceCfgT1E1TxActiveOffhookState_Type(DisplayString):
    """Custom type cdx6500VoiceCfgT1E1TxActiveOffhookState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Cdx6500VoiceCfgT1E1TxActiveOffhookState_Type.__name__ = "DisplayString"
_Cdx6500VoiceCfgT1E1TxActiveOffhookState_Object = MibTableColumn
cdx6500VoiceCfgT1E1TxActiveOffhookState = _Cdx6500VoiceCfgT1E1TxActiveOffhookState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 33),
    _Cdx6500VoiceCfgT1E1TxActiveOffhookState_Type()
)
cdx6500VoiceCfgT1E1TxActiveOffhookState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgT1E1TxActiveOffhookState.setStatus("mandatory")


class _Cdx6500VoiceCfgT1E1RingingState_Type(DisplayString):
    """Custom type cdx6500VoiceCfgT1E1RingingState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Cdx6500VoiceCfgT1E1RingingState_Type.__name__ = "DisplayString"
_Cdx6500VoiceCfgT1E1RingingState_Object = MibTableColumn
cdx6500VoiceCfgT1E1RingingState = _Cdx6500VoiceCfgT1E1RingingState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 34),
    _Cdx6500VoiceCfgT1E1RingingState_Type()
)
cdx6500VoiceCfgT1E1RingingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgT1E1RingingState.setStatus("mandatory")


class _Cdx6500VoiceCfgT1E1NoRingingState_Type(DisplayString):
    """Custom type cdx6500VoiceCfgT1E1NoRingingState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Cdx6500VoiceCfgT1E1NoRingingState_Type.__name__ = "DisplayString"
_Cdx6500VoiceCfgT1E1NoRingingState_Object = MibTableColumn
cdx6500VoiceCfgT1E1NoRingingState = _Cdx6500VoiceCfgT1E1NoRingingState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 35),
    _Cdx6500VoiceCfgT1E1NoRingingState_Type()
)
cdx6500VoiceCfgT1E1NoRingingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgT1E1NoRingingState.setStatus("mandatory")


class _Cdx6500VoiceCfgRxWinkStartTimer_Type(Integer32):
    """Custom type cdx6500VoiceCfgRxWinkStartTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_Cdx6500VoiceCfgRxWinkStartTimer_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgRxWinkStartTimer_Object = MibTableColumn
cdx6500VoiceCfgRxWinkStartTimer = _Cdx6500VoiceCfgRxWinkStartTimer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 36),
    _Cdx6500VoiceCfgRxWinkStartTimer_Type()
)
cdx6500VoiceCfgRxWinkStartTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgRxWinkStartTimer.setStatus("mandatory")


class _Cdx6500VoiceCfgRxMinimumReceiveWink_Type(Integer32):
    """Custom type cdx6500VoiceCfgRxMinimumReceiveWink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 2000),
    )


_Cdx6500VoiceCfgRxMinimumReceiveWink_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgRxMinimumReceiveWink_Object = MibTableColumn
cdx6500VoiceCfgRxMinimumReceiveWink = _Cdx6500VoiceCfgRxMinimumReceiveWink_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 37),
    _Cdx6500VoiceCfgRxMinimumReceiveWink_Type()
)
cdx6500VoiceCfgRxMinimumReceiveWink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgRxMinimumReceiveWink.setStatus("mandatory")


class _Cdx6500VoiceCfgRxCalledEndGlareDetect_Type(Integer32):
    """Custom type cdx6500VoiceCfgRxCalledEndGlareDetect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 10000),
    )


_Cdx6500VoiceCfgRxCalledEndGlareDetect_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgRxCalledEndGlareDetect_Object = MibTableColumn
cdx6500VoiceCfgRxCalledEndGlareDetect = _Cdx6500VoiceCfgRxCalledEndGlareDetect_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 38),
    _Cdx6500VoiceCfgRxCalledEndGlareDetect_Type()
)
cdx6500VoiceCfgRxCalledEndGlareDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgRxCalledEndGlareDetect.setStatus("mandatory")


class _Cdx6500VoiceCfgRxFirstDigitTimer_Type(Integer32):
    """Custom type cdx6500VoiceCfgRxFirstDigitTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_Cdx6500VoiceCfgRxFirstDigitTimer_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgRxFirstDigitTimer_Object = MibTableColumn
cdx6500VoiceCfgRxFirstDigitTimer = _Cdx6500VoiceCfgRxFirstDigitTimer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 39),
    _Cdx6500VoiceCfgRxFirstDigitTimer_Type()
)
cdx6500VoiceCfgRxFirstDigitTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgRxFirstDigitTimer.setStatus("mandatory")


class _Cdx6500VoiceCfgRxInterdigitTimer_Type(Integer32):
    """Custom type cdx6500VoiceCfgRxInterdigitTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_Cdx6500VoiceCfgRxInterdigitTimer_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgRxInterdigitTimer_Object = MibTableColumn
cdx6500VoiceCfgRxInterdigitTimer = _Cdx6500VoiceCfgRxInterdigitTimer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 40),
    _Cdx6500VoiceCfgRxInterdigitTimer_Type()
)
cdx6500VoiceCfgRxInterdigitTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgRxInterdigitTimer.setStatus("mandatory")


class _Cdx6500VoiceCfgTxWinkDelay_Type(Integer32):
    """Custom type cdx6500VoiceCfgTxWinkDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000),
    )


_Cdx6500VoiceCfgTxWinkDelay_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgTxWinkDelay_Object = MibTableColumn
cdx6500VoiceCfgTxWinkDelay = _Cdx6500VoiceCfgTxWinkDelay_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 41),
    _Cdx6500VoiceCfgTxWinkDelay_Type()
)
cdx6500VoiceCfgTxWinkDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgTxWinkDelay.setStatus("mandatory")


class _Cdx6500VoiceCfgTxWinkWidth_Type(Integer32):
    """Custom type cdx6500VoiceCfgTxWinkWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 2000),
    )


_Cdx6500VoiceCfgTxWinkWidth_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgTxWinkWidth_Object = MibTableColumn
cdx6500VoiceCfgTxWinkWidth = _Cdx6500VoiceCfgTxWinkWidth_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 42),
    _Cdx6500VoiceCfgTxWinkWidth_Type()
)
cdx6500VoiceCfgTxWinkWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgTxWinkWidth.setStatus("mandatory")


class _Cdx6500VoiceCfgTxDigitDelay_Type(Integer32):
    """Custom type cdx6500VoiceCfgTxDigitDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_Cdx6500VoiceCfgTxDigitDelay_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgTxDigitDelay_Object = MibTableColumn
cdx6500VoiceCfgTxDigitDelay = _Cdx6500VoiceCfgTxDigitDelay_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 43),
    _Cdx6500VoiceCfgTxDigitDelay_Type()
)
cdx6500VoiceCfgTxDigitDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgTxDigitDelay.setStatus("mandatory")


class _Cdx6500VoiceCfgTxDigitOn_Type(Integer32):
    """Custom type cdx6500VoiceCfgTxDigitOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 1000),
    )


_Cdx6500VoiceCfgTxDigitOn_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgTxDigitOn_Object = MibTableColumn
cdx6500VoiceCfgTxDigitOn = _Cdx6500VoiceCfgTxDigitOn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 44),
    _Cdx6500VoiceCfgTxDigitOn_Type()
)
cdx6500VoiceCfgTxDigitOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgTxDigitOn.setStatus("mandatory")


class _Cdx6500VoiceCfgTxInterdigitTime_Type(Integer32):
    """Custom type cdx6500VoiceCfgTxInterdigitTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 1000),
    )


_Cdx6500VoiceCfgTxInterdigitTime_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgTxInterdigitTime_Object = MibTableColumn
cdx6500VoiceCfgTxInterdigitTime = _Cdx6500VoiceCfgTxInterdigitTime_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 45),
    _Cdx6500VoiceCfgTxInterdigitTime_Type()
)
cdx6500VoiceCfgTxInterdigitTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgTxInterdigitTime.setStatus("mandatory")


class _Cdx6500VoiceCfgRxInterringWait_Type(Integer32):
    """Custom type cdx6500VoiceCfgRxInterringWait based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_Cdx6500VoiceCfgRxInterringWait_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgRxInterringWait_Object = MibTableColumn
cdx6500VoiceCfgRxInterringWait = _Cdx6500VoiceCfgRxInterringWait_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 46),
    _Cdx6500VoiceCfgRxInterringWait_Type()
)
cdx6500VoiceCfgRxInterringWait.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgRxInterringWait.setStatus("mandatory")


class _Cdx6500VoiceCfgRxRingStateChangeFilter_Type(Integer32):
    """Custom type cdx6500VoiceCfgRxRingStateChangeFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_Cdx6500VoiceCfgRxRingStateChangeFilter_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgRxRingStateChangeFilter_Object = MibTableColumn
cdx6500VoiceCfgRxRingStateChangeFilter = _Cdx6500VoiceCfgRxRingStateChangeFilter_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 47),
    _Cdx6500VoiceCfgRxRingStateChangeFilter_Type()
)
cdx6500VoiceCfgRxRingStateChangeFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgRxRingStateChangeFilter.setStatus("mandatory")


class _Cdx6500VoiceCfgTxRingerOffLong_Type(Integer32):
    """Custom type cdx6500VoiceCfgTxRingerOffLong based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000),
    )


_Cdx6500VoiceCfgTxRingerOffLong_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgTxRingerOffLong_Object = MibTableColumn
cdx6500VoiceCfgTxRingerOffLong = _Cdx6500VoiceCfgTxRingerOffLong_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 48),
    _Cdx6500VoiceCfgTxRingerOffLong_Type()
)
cdx6500VoiceCfgTxRingerOffLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgTxRingerOffLong.setStatus("mandatory")


class _Cdx6500VoiceCfgTxRingerOffShort_Type(Integer32):
    """Custom type cdx6500VoiceCfgTxRingerOffShort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000),
    )


_Cdx6500VoiceCfgTxRingerOffShort_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgTxRingerOffShort_Object = MibTableColumn
cdx6500VoiceCfgTxRingerOffShort = _Cdx6500VoiceCfgTxRingerOffShort_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 49),
    _Cdx6500VoiceCfgTxRingerOffShort_Type()
)
cdx6500VoiceCfgTxRingerOffShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgTxRingerOffShort.setStatus("mandatory")


class _Cdx6500VoiceCfgTxRingerOn_Type(Integer32):
    """Custom type cdx6500VoiceCfgTxRingerOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000),
    )


_Cdx6500VoiceCfgTxRingerOn_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgTxRingerOn_Object = MibTableColumn
cdx6500VoiceCfgTxRingerOn = _Cdx6500VoiceCfgTxRingerOn_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 50),
    _Cdx6500VoiceCfgTxRingerOn_Type()
)
cdx6500VoiceCfgTxRingerOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgTxRingerOn.setStatus("mandatory")


class _Cdx6500VoiceCfgRxDisconnectTimer_Type(Integer32):
    """Custom type cdx6500VoiceCfgRxDisconnectTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 30000),
    )


_Cdx6500VoiceCfgRxDisconnectTimer_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgRxDisconnectTimer_Object = MibTableColumn
cdx6500VoiceCfgRxDisconnectTimer = _Cdx6500VoiceCfgRxDisconnectTimer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 51),
    _Cdx6500VoiceCfgRxDisconnectTimer_Type()
)
cdx6500VoiceCfgRxDisconnectTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgRxDisconnectTimer.setStatus("mandatory")


class _Cdx6500VoiceCfgRxCalledEndDisconnectDelayTimer_Type(Integer32):
    """Custom type cdx6500VoiceCfgRxCalledEndDisconnectDelayTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_Cdx6500VoiceCfgRxCalledEndDisconnectDelayTimer_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgRxCalledEndDisconnectDelayTimer_Object = MibTableColumn
cdx6500VoiceCfgRxCalledEndDisconnectDelayTimer = _Cdx6500VoiceCfgRxCalledEndDisconnectDelayTimer_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 52),
    _Cdx6500VoiceCfgRxCalledEndDisconnectDelayTimer_Type()
)
cdx6500VoiceCfgRxCalledEndDisconnectDelayTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgRxCalledEndDisconnectDelayTimer.setStatus("mandatory")


class _Cdx6500VoiceCfgLineErrorRecovery_Type(Integer32):
    """Custom type cdx6500VoiceCfgLineErrorRecovery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Cdx6500VoiceCfgLineErrorRecovery_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgLineErrorRecovery_Object = MibTableColumn
cdx6500VoiceCfgLineErrorRecovery = _Cdx6500VoiceCfgLineErrorRecovery_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 53),
    _Cdx6500VoiceCfgLineErrorRecovery_Type()
)
cdx6500VoiceCfgLineErrorRecovery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgLineErrorRecovery.setStatus("mandatory")


class _Cdx6500VoiceCfgSignalingSampleRate_Type(Integer32):
    """Custom type cdx6500VoiceCfgSignalingSampleRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_Cdx6500VoiceCfgSignalingSampleRate_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgSignalingSampleRate_Object = MibTableColumn
cdx6500VoiceCfgSignalingSampleRate = _Cdx6500VoiceCfgSignalingSampleRate_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 54),
    _Cdx6500VoiceCfgSignalingSampleRate_Type()
)
cdx6500VoiceCfgSignalingSampleRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgSignalingSampleRate.setStatus("mandatory")


class _Cdx6500VoiceCfgWaitForParams_Type(Integer32):
    """Custom type cdx6500VoiceCfgWaitForParams based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_Cdx6500VoiceCfgWaitForParams_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgWaitForParams_Object = MibTableColumn
cdx6500VoiceCfgWaitForParams = _Cdx6500VoiceCfgWaitForParams_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 55),
    _Cdx6500VoiceCfgWaitForParams_Type()
)
cdx6500VoiceCfgWaitForParams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgWaitForParams.setStatus("mandatory")


class _Cdx6500VoiceCfgSpareTimer1_Type(Integer32):
    """Custom type cdx6500VoiceCfgSpareTimer1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_Cdx6500VoiceCfgSpareTimer1_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgSpareTimer1_Object = MibTableColumn
cdx6500VoiceCfgSpareTimer1 = _Cdx6500VoiceCfgSpareTimer1_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 56),
    _Cdx6500VoiceCfgSpareTimer1_Type()
)
cdx6500VoiceCfgSpareTimer1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgSpareTimer1.setStatus("mandatory")


class _Cdx6500VoiceCfgSpareTimer2_Type(Integer32):
    """Custom type cdx6500VoiceCfgSpareTimer2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_Cdx6500VoiceCfgSpareTimer2_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgSpareTimer2_Object = MibTableColumn
cdx6500VoiceCfgSpareTimer2 = _Cdx6500VoiceCfgSpareTimer2_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 57),
    _Cdx6500VoiceCfgSpareTimer2_Type()
)
cdx6500VoiceCfgSpareTimer2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgSpareTimer2.setStatus("mandatory")


class _Cdx6500VoiceCfgTxInterdigitPauseTime_Type(Integer32):
    """Custom type cdx6500VoiceCfgTxInterdigitPauseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_Cdx6500VoiceCfgTxInterdigitPauseTime_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgTxInterdigitPauseTime_Object = MibTableColumn
cdx6500VoiceCfgTxInterdigitPauseTime = _Cdx6500VoiceCfgTxInterdigitPauseTime_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 58),
    _Cdx6500VoiceCfgTxInterdigitPauseTime_Type()
)
cdx6500VoiceCfgTxInterdigitPauseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgTxInterdigitPauseTime.setStatus("mandatory")


class _Cdx6500VoiceCfgRxMinimumFlashHookTime_Type(Integer32):
    """Custom type cdx6500VoiceCfgRxMinimumFlashHookTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000),
    )


_Cdx6500VoiceCfgRxMinimumFlashHookTime_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgRxMinimumFlashHookTime_Object = MibTableColumn
cdx6500VoiceCfgRxMinimumFlashHookTime = _Cdx6500VoiceCfgRxMinimumFlashHookTime_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 59),
    _Cdx6500VoiceCfgRxMinimumFlashHookTime_Type()
)
cdx6500VoiceCfgRxMinimumFlashHookTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgRxMinimumFlashHookTime.setStatus("mandatory")


class _Cdx6500VoiceCfgRxMaximumFlashHookTime_Type(Integer32):
    """Custom type cdx6500VoiceCfgRxMaximumFlashHookTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000),
    )


_Cdx6500VoiceCfgRxMaximumFlashHookTime_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgRxMaximumFlashHookTime_Object = MibTableColumn
cdx6500VoiceCfgRxMaximumFlashHookTime = _Cdx6500VoiceCfgRxMaximumFlashHookTime_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 60),
    _Cdx6500VoiceCfgRxMaximumFlashHookTime_Type()
)
cdx6500VoiceCfgRxMaximumFlashHookTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgRxMaximumFlashHookTime.setStatus("mandatory")


class _Cdx6500VoiceCfgTransparentSignalingIdleState_Type(DisplayString):
    """Custom type cdx6500VoiceCfgTransparentSignalingIdleState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Cdx6500VoiceCfgTransparentSignalingIdleState_Type.__name__ = "DisplayString"
_Cdx6500VoiceCfgTransparentSignalingIdleState_Object = MibTableColumn
cdx6500VoiceCfgTransparentSignalingIdleState = _Cdx6500VoiceCfgTransparentSignalingIdleState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 61),
    _Cdx6500VoiceCfgTransparentSignalingIdleState_Type()
)
cdx6500VoiceCfgTransparentSignalingIdleState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgTransparentSignalingIdleState.setStatus("mandatory")


class _Cdx6500VoiceCfgTransparentRxDisconnectFilter_Type(Integer32):
    """Custom type cdx6500VoiceCfgTransparentRxDisconnectFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_Cdx6500VoiceCfgTransparentRxDisconnectFilter_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgTransparentRxDisconnectFilter_Object = MibTableColumn
cdx6500VoiceCfgTransparentRxDisconnectFilter = _Cdx6500VoiceCfgTransparentRxDisconnectFilter_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 62),
    _Cdx6500VoiceCfgTransparentRxDisconnectFilter_Type()
)
cdx6500VoiceCfgTransparentRxDisconnectFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgTransparentRxDisconnectFilter.setStatus("mandatory")


class _Cdx6500VoiceCfgTransparentSignalingBusyoutState_Type(DisplayString):
    """Custom type cdx6500VoiceCfgTransparentSignalingBusyoutState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Cdx6500VoiceCfgTransparentSignalingBusyoutState_Type.__name__ = "DisplayString"
_Cdx6500VoiceCfgTransparentSignalingBusyoutState_Object = MibTableColumn
cdx6500VoiceCfgTransparentSignalingBusyoutState = _Cdx6500VoiceCfgTransparentSignalingBusyoutState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 63),
    _Cdx6500VoiceCfgTransparentSignalingBusyoutState_Type()
)
cdx6500VoiceCfgTransparentSignalingBusyoutState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgTransparentSignalingBusyoutState.setStatus("mandatory")


class _Cdx6500VoiceCfgXlateSigInfo0000FromRemoteToLocalPort_Type(DisplayString):
    """Custom type cdx6500VoiceCfgXlateSigInfo0000FromRemoteToLocalPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Cdx6500VoiceCfgXlateSigInfo0000FromRemoteToLocalPort_Type.__name__ = "DisplayString"
_Cdx6500VoiceCfgXlateSigInfo0000FromRemoteToLocalPort_Object = MibTableColumn
cdx6500VoiceCfgXlateSigInfo0000FromRemoteToLocalPort = _Cdx6500VoiceCfgXlateSigInfo0000FromRemoteToLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 64),
    _Cdx6500VoiceCfgXlateSigInfo0000FromRemoteToLocalPort_Type()
)
cdx6500VoiceCfgXlateSigInfo0000FromRemoteToLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgXlateSigInfo0000FromRemoteToLocalPort.setStatus("mandatory")


class _Cdx6500VoiceCfgXlateSigInfo1000FromRemoteToLocalPort_Type(DisplayString):
    """Custom type cdx6500VoiceCfgXlateSigInfo1000FromRemoteToLocalPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Cdx6500VoiceCfgXlateSigInfo1000FromRemoteToLocalPort_Type.__name__ = "DisplayString"
_Cdx6500VoiceCfgXlateSigInfo1000FromRemoteToLocalPort_Object = MibTableColumn
cdx6500VoiceCfgXlateSigInfo1000FromRemoteToLocalPort = _Cdx6500VoiceCfgXlateSigInfo1000FromRemoteToLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 65),
    _Cdx6500VoiceCfgXlateSigInfo1000FromRemoteToLocalPort_Type()
)
cdx6500VoiceCfgXlateSigInfo1000FromRemoteToLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgXlateSigInfo1000FromRemoteToLocalPort.setStatus("mandatory")


class _Cdx6500VoiceCfgXlateSigInfo0100FromRemoteToLocalPort_Type(DisplayString):
    """Custom type cdx6500VoiceCfgXlateSigInfo0100FromRemoteToLocalPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Cdx6500VoiceCfgXlateSigInfo0100FromRemoteToLocalPort_Type.__name__ = "DisplayString"
_Cdx6500VoiceCfgXlateSigInfo0100FromRemoteToLocalPort_Object = MibTableColumn
cdx6500VoiceCfgXlateSigInfo0100FromRemoteToLocalPort = _Cdx6500VoiceCfgXlateSigInfo0100FromRemoteToLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 66),
    _Cdx6500VoiceCfgXlateSigInfo0100FromRemoteToLocalPort_Type()
)
cdx6500VoiceCfgXlateSigInfo0100FromRemoteToLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgXlateSigInfo0100FromRemoteToLocalPort.setStatus("mandatory")


class _Cdx6500VoiceCfgXlateSigInfo1100FromRemoteToLocalPort_Type(DisplayString):
    """Custom type cdx6500VoiceCfgXlateSigInfo1100FromRemoteToLocalPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Cdx6500VoiceCfgXlateSigInfo1100FromRemoteToLocalPort_Type.__name__ = "DisplayString"
_Cdx6500VoiceCfgXlateSigInfo1100FromRemoteToLocalPort_Object = MibTableColumn
cdx6500VoiceCfgXlateSigInfo1100FromRemoteToLocalPort = _Cdx6500VoiceCfgXlateSigInfo1100FromRemoteToLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 67),
    _Cdx6500VoiceCfgXlateSigInfo1100FromRemoteToLocalPort_Type()
)
cdx6500VoiceCfgXlateSigInfo1100FromRemoteToLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgXlateSigInfo1100FromRemoteToLocalPort.setStatus("mandatory")


class _Cdx6500VoiceCfgXlateSigInfo0010FromRemoteToLocalPort_Type(DisplayString):
    """Custom type cdx6500VoiceCfgXlateSigInfo0010FromRemoteToLocalPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Cdx6500VoiceCfgXlateSigInfo0010FromRemoteToLocalPort_Type.__name__ = "DisplayString"
_Cdx6500VoiceCfgXlateSigInfo0010FromRemoteToLocalPort_Object = MibTableColumn
cdx6500VoiceCfgXlateSigInfo0010FromRemoteToLocalPort = _Cdx6500VoiceCfgXlateSigInfo0010FromRemoteToLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 68),
    _Cdx6500VoiceCfgXlateSigInfo0010FromRemoteToLocalPort_Type()
)
cdx6500VoiceCfgXlateSigInfo0010FromRemoteToLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgXlateSigInfo0010FromRemoteToLocalPort.setStatus("mandatory")


class _Cdx6500VoiceCfgXlateSigInfo1010FromRemoteToLocalPort_Type(DisplayString):
    """Custom type cdx6500VoiceCfgXlateSigInfo1010FromRemoteToLocalPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Cdx6500VoiceCfgXlateSigInfo1010FromRemoteToLocalPort_Type.__name__ = "DisplayString"
_Cdx6500VoiceCfgXlateSigInfo1010FromRemoteToLocalPort_Object = MibTableColumn
cdx6500VoiceCfgXlateSigInfo1010FromRemoteToLocalPort = _Cdx6500VoiceCfgXlateSigInfo1010FromRemoteToLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 69),
    _Cdx6500VoiceCfgXlateSigInfo1010FromRemoteToLocalPort_Type()
)
cdx6500VoiceCfgXlateSigInfo1010FromRemoteToLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgXlateSigInfo1010FromRemoteToLocalPort.setStatus("mandatory")


class _Cdx6500VoiceCfgXlateSigInfo0110FromRemoteToLocalPort_Type(DisplayString):
    """Custom type cdx6500VoiceCfgXlateSigInfo0110FromRemoteToLocalPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Cdx6500VoiceCfgXlateSigInfo0110FromRemoteToLocalPort_Type.__name__ = "DisplayString"
_Cdx6500VoiceCfgXlateSigInfo0110FromRemoteToLocalPort_Object = MibTableColumn
cdx6500VoiceCfgXlateSigInfo0110FromRemoteToLocalPort = _Cdx6500VoiceCfgXlateSigInfo0110FromRemoteToLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 70),
    _Cdx6500VoiceCfgXlateSigInfo0110FromRemoteToLocalPort_Type()
)
cdx6500VoiceCfgXlateSigInfo0110FromRemoteToLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgXlateSigInfo0110FromRemoteToLocalPort.setStatus("mandatory")


class _Cdx6500VoiceCfgXlateSigInfo1110FromRemoteToLocalPort_Type(DisplayString):
    """Custom type cdx6500VoiceCfgXlateSigInfo1110FromRemoteToLocalPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Cdx6500VoiceCfgXlateSigInfo1110FromRemoteToLocalPort_Type.__name__ = "DisplayString"
_Cdx6500VoiceCfgXlateSigInfo1110FromRemoteToLocalPort_Object = MibTableColumn
cdx6500VoiceCfgXlateSigInfo1110FromRemoteToLocalPort = _Cdx6500VoiceCfgXlateSigInfo1110FromRemoteToLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 71),
    _Cdx6500VoiceCfgXlateSigInfo1110FromRemoteToLocalPort_Type()
)
cdx6500VoiceCfgXlateSigInfo1110FromRemoteToLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgXlateSigInfo1110FromRemoteToLocalPort.setStatus("mandatory")


class _Cdx6500VoiceCfgXlateSigInfo0001FromRemoteToLocalPort_Type(DisplayString):
    """Custom type cdx6500VoiceCfgXlateSigInfo0001FromRemoteToLocalPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Cdx6500VoiceCfgXlateSigInfo0001FromRemoteToLocalPort_Type.__name__ = "DisplayString"
_Cdx6500VoiceCfgXlateSigInfo0001FromRemoteToLocalPort_Object = MibTableColumn
cdx6500VoiceCfgXlateSigInfo0001FromRemoteToLocalPort = _Cdx6500VoiceCfgXlateSigInfo0001FromRemoteToLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 72),
    _Cdx6500VoiceCfgXlateSigInfo0001FromRemoteToLocalPort_Type()
)
cdx6500VoiceCfgXlateSigInfo0001FromRemoteToLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgXlateSigInfo0001FromRemoteToLocalPort.setStatus("mandatory")


class _Cdx6500VoiceCfgXlateSigInfo1001FromRemoteToLocalPort_Type(DisplayString):
    """Custom type cdx6500VoiceCfgXlateSigInfo1001FromRemoteToLocalPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Cdx6500VoiceCfgXlateSigInfo1001FromRemoteToLocalPort_Type.__name__ = "DisplayString"
_Cdx6500VoiceCfgXlateSigInfo1001FromRemoteToLocalPort_Object = MibTableColumn
cdx6500VoiceCfgXlateSigInfo1001FromRemoteToLocalPort = _Cdx6500VoiceCfgXlateSigInfo1001FromRemoteToLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 73),
    _Cdx6500VoiceCfgXlateSigInfo1001FromRemoteToLocalPort_Type()
)
cdx6500VoiceCfgXlateSigInfo1001FromRemoteToLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgXlateSigInfo1001FromRemoteToLocalPort.setStatus("mandatory")


class _Cdx6500VoiceCfgXlateSigInfo0101FromRemoteToLocalPort_Type(DisplayString):
    """Custom type cdx6500VoiceCfgXlateSigInfo0101FromRemoteToLocalPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Cdx6500VoiceCfgXlateSigInfo0101FromRemoteToLocalPort_Type.__name__ = "DisplayString"
_Cdx6500VoiceCfgXlateSigInfo0101FromRemoteToLocalPort_Object = MibTableColumn
cdx6500VoiceCfgXlateSigInfo0101FromRemoteToLocalPort = _Cdx6500VoiceCfgXlateSigInfo0101FromRemoteToLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 74),
    _Cdx6500VoiceCfgXlateSigInfo0101FromRemoteToLocalPort_Type()
)
cdx6500VoiceCfgXlateSigInfo0101FromRemoteToLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgXlateSigInfo0101FromRemoteToLocalPort.setStatus("mandatory")


class _Cdx6500VoiceCfgXlateSigInfo1101FromRemoteToLocalPort_Type(DisplayString):
    """Custom type cdx6500VoiceCfgXlateSigInfo1101FromRemoteToLocalPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Cdx6500VoiceCfgXlateSigInfo1101FromRemoteToLocalPort_Type.__name__ = "DisplayString"
_Cdx6500VoiceCfgXlateSigInfo1101FromRemoteToLocalPort_Object = MibTableColumn
cdx6500VoiceCfgXlateSigInfo1101FromRemoteToLocalPort = _Cdx6500VoiceCfgXlateSigInfo1101FromRemoteToLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 75),
    _Cdx6500VoiceCfgXlateSigInfo1101FromRemoteToLocalPort_Type()
)
cdx6500VoiceCfgXlateSigInfo1101FromRemoteToLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgXlateSigInfo1101FromRemoteToLocalPort.setStatus("mandatory")


class _Cdx6500VoiceCfgXlateSigInfo0011FromRemoteToLocalPort_Type(DisplayString):
    """Custom type cdx6500VoiceCfgXlateSigInfo0011FromRemoteToLocalPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Cdx6500VoiceCfgXlateSigInfo0011FromRemoteToLocalPort_Type.__name__ = "DisplayString"
_Cdx6500VoiceCfgXlateSigInfo0011FromRemoteToLocalPort_Object = MibTableColumn
cdx6500VoiceCfgXlateSigInfo0011FromRemoteToLocalPort = _Cdx6500VoiceCfgXlateSigInfo0011FromRemoteToLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 76),
    _Cdx6500VoiceCfgXlateSigInfo0011FromRemoteToLocalPort_Type()
)
cdx6500VoiceCfgXlateSigInfo0011FromRemoteToLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgXlateSigInfo0011FromRemoteToLocalPort.setStatus("mandatory")


class _Cdx6500VoiceCfgXlateSigInfo1011FromRemoteToLocalPort_Type(DisplayString):
    """Custom type cdx6500VoiceCfgXlateSigInfo1011FromRemoteToLocalPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Cdx6500VoiceCfgXlateSigInfo1011FromRemoteToLocalPort_Type.__name__ = "DisplayString"
_Cdx6500VoiceCfgXlateSigInfo1011FromRemoteToLocalPort_Object = MibTableColumn
cdx6500VoiceCfgXlateSigInfo1011FromRemoteToLocalPort = _Cdx6500VoiceCfgXlateSigInfo1011FromRemoteToLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 77),
    _Cdx6500VoiceCfgXlateSigInfo1011FromRemoteToLocalPort_Type()
)
cdx6500VoiceCfgXlateSigInfo1011FromRemoteToLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgXlateSigInfo1011FromRemoteToLocalPort.setStatus("mandatory")


class _Cdx6500VoiceCfgXlateSigInfo0111FromRemoteToLocalPort_Type(DisplayString):
    """Custom type cdx6500VoiceCfgXlateSigInfo0111FromRemoteToLocalPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Cdx6500VoiceCfgXlateSigInfo0111FromRemoteToLocalPort_Type.__name__ = "DisplayString"
_Cdx6500VoiceCfgXlateSigInfo0111FromRemoteToLocalPort_Object = MibTableColumn
cdx6500VoiceCfgXlateSigInfo0111FromRemoteToLocalPort = _Cdx6500VoiceCfgXlateSigInfo0111FromRemoteToLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 78),
    _Cdx6500VoiceCfgXlateSigInfo0111FromRemoteToLocalPort_Type()
)
cdx6500VoiceCfgXlateSigInfo0111FromRemoteToLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgXlateSigInfo0111FromRemoteToLocalPort.setStatus("mandatory")


class _Cdx6500VoiceCfgXlateSigInfo1111FromRemoteToLocalPort_Type(DisplayString):
    """Custom type cdx6500VoiceCfgXlateSigInfo1111FromRemoteToLocalPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Cdx6500VoiceCfgXlateSigInfo1111FromRemoteToLocalPort_Type.__name__ = "DisplayString"
_Cdx6500VoiceCfgXlateSigInfo1111FromRemoteToLocalPort_Object = MibTableColumn
cdx6500VoiceCfgXlateSigInfo1111FromRemoteToLocalPort = _Cdx6500VoiceCfgXlateSigInfo1111FromRemoteToLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 79),
    _Cdx6500VoiceCfgXlateSigInfo1111FromRemoteToLocalPort_Type()
)
cdx6500VoiceCfgXlateSigInfo1111FromRemoteToLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgXlateSigInfo1111FromRemoteToLocalPort.setStatus("mandatory")


class _Cdx6500VoiceCfgDialToneLowerFrequency_Type(Integer32):
    """Custom type cdx6500VoiceCfgDialToneLowerFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 3500),
    )


_Cdx6500VoiceCfgDialToneLowerFrequency_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgDialToneLowerFrequency_Object = MibTableColumn
cdx6500VoiceCfgDialToneLowerFrequency = _Cdx6500VoiceCfgDialToneLowerFrequency_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 80),
    _Cdx6500VoiceCfgDialToneLowerFrequency_Type()
)
cdx6500VoiceCfgDialToneLowerFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgDialToneLowerFrequency.setStatus("mandatory")
_Cdx6500VoiceCfgDialToneLowerFrequencyAmplitude_Type = DisplayString
_Cdx6500VoiceCfgDialToneLowerFrequencyAmplitude_Object = MibTableColumn
cdx6500VoiceCfgDialToneLowerFrequencyAmplitude = _Cdx6500VoiceCfgDialToneLowerFrequencyAmplitude_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 81),
    _Cdx6500VoiceCfgDialToneLowerFrequencyAmplitude_Type()
)
cdx6500VoiceCfgDialToneLowerFrequencyAmplitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgDialToneLowerFrequencyAmplitude.setStatus("mandatory")


class _Cdx6500VoiceCfgDialToneUpperFrequency_Type(Integer32):
    """Custom type cdx6500VoiceCfgDialToneUpperFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 3500),
    )


_Cdx6500VoiceCfgDialToneUpperFrequency_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgDialToneUpperFrequency_Object = MibTableColumn
cdx6500VoiceCfgDialToneUpperFrequency = _Cdx6500VoiceCfgDialToneUpperFrequency_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 82),
    _Cdx6500VoiceCfgDialToneUpperFrequency_Type()
)
cdx6500VoiceCfgDialToneUpperFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgDialToneUpperFrequency.setStatus("mandatory")
_Cdx6500VoiceCfgDialToneUpperFrequencyAmplitude_Type = DisplayString
_Cdx6500VoiceCfgDialToneUpperFrequencyAmplitude_Object = MibTableColumn
cdx6500VoiceCfgDialToneUpperFrequencyAmplitude = _Cdx6500VoiceCfgDialToneUpperFrequencyAmplitude_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 83),
    _Cdx6500VoiceCfgDialToneUpperFrequencyAmplitude_Type()
)
cdx6500VoiceCfgDialToneUpperFrequencyAmplitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgDialToneUpperFrequencyAmplitude.setStatus("mandatory")


class _Cdx6500VoiceCfgRingBackToneLowerFrequency_Type(Integer32):
    """Custom type cdx6500VoiceCfgRingBackToneLowerFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 3500),
    )


_Cdx6500VoiceCfgRingBackToneLowerFrequency_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgRingBackToneLowerFrequency_Object = MibTableColumn
cdx6500VoiceCfgRingBackToneLowerFrequency = _Cdx6500VoiceCfgRingBackToneLowerFrequency_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 84),
    _Cdx6500VoiceCfgRingBackToneLowerFrequency_Type()
)
cdx6500VoiceCfgRingBackToneLowerFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgRingBackToneLowerFrequency.setStatus("mandatory")
_Cdx6500VoiceCfgRingBackToneLowerFrequencyAmplitude_Type = DisplayString
_Cdx6500VoiceCfgRingBackToneLowerFrequencyAmplitude_Object = MibTableColumn
cdx6500VoiceCfgRingBackToneLowerFrequencyAmplitude = _Cdx6500VoiceCfgRingBackToneLowerFrequencyAmplitude_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 85),
    _Cdx6500VoiceCfgRingBackToneLowerFrequencyAmplitude_Type()
)
cdx6500VoiceCfgRingBackToneLowerFrequencyAmplitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgRingBackToneLowerFrequencyAmplitude.setStatus("mandatory")


class _Cdx6500VoiceCfgRingBackToneUpperFrequency_Type(Integer32):
    """Custom type cdx6500VoiceCfgRingBackToneUpperFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 3500),
    )


_Cdx6500VoiceCfgRingBackToneUpperFrequency_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgRingBackToneUpperFrequency_Object = MibTableColumn
cdx6500VoiceCfgRingBackToneUpperFrequency = _Cdx6500VoiceCfgRingBackToneUpperFrequency_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 86),
    _Cdx6500VoiceCfgRingBackToneUpperFrequency_Type()
)
cdx6500VoiceCfgRingBackToneUpperFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgRingBackToneUpperFrequency.setStatus("mandatory")
_Cdx6500VoiceCfgRingBackToneUpperFrequencyAmplitude_Type = DisplayString
_Cdx6500VoiceCfgRingBackToneUpperFrequencyAmplitude_Object = MibTableColumn
cdx6500VoiceCfgRingBackToneUpperFrequencyAmplitude = _Cdx6500VoiceCfgRingBackToneUpperFrequencyAmplitude_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 87),
    _Cdx6500VoiceCfgRingBackToneUpperFrequencyAmplitude_Type()
)
cdx6500VoiceCfgRingBackToneUpperFrequencyAmplitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgRingBackToneUpperFrequencyAmplitude.setStatus("mandatory")


class _Cdx6500VoiceCfgBusyToneLowerFrequency_Type(Integer32):
    """Custom type cdx6500VoiceCfgBusyToneLowerFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 3500),
    )


_Cdx6500VoiceCfgBusyToneLowerFrequency_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgBusyToneLowerFrequency_Object = MibTableColumn
cdx6500VoiceCfgBusyToneLowerFrequency = _Cdx6500VoiceCfgBusyToneLowerFrequency_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 88),
    _Cdx6500VoiceCfgBusyToneLowerFrequency_Type()
)
cdx6500VoiceCfgBusyToneLowerFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgBusyToneLowerFrequency.setStatus("mandatory")
_Cdx6500VoiceCfgBusyToneLowerFrequencyAmplitude_Type = DisplayString
_Cdx6500VoiceCfgBusyToneLowerFrequencyAmplitude_Object = MibTableColumn
cdx6500VoiceCfgBusyToneLowerFrequencyAmplitude = _Cdx6500VoiceCfgBusyToneLowerFrequencyAmplitude_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 89),
    _Cdx6500VoiceCfgBusyToneLowerFrequencyAmplitude_Type()
)
cdx6500VoiceCfgBusyToneLowerFrequencyAmplitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgBusyToneLowerFrequencyAmplitude.setStatus("mandatory")


class _Cdx6500VoiceCfgBusyToneUpperFrequency_Type(Integer32):
    """Custom type cdx6500VoiceCfgBusyToneUpperFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 3500),
    )


_Cdx6500VoiceCfgBusyToneUpperFrequency_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgBusyToneUpperFrequency_Object = MibTableColumn
cdx6500VoiceCfgBusyToneUpperFrequency = _Cdx6500VoiceCfgBusyToneUpperFrequency_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 90),
    _Cdx6500VoiceCfgBusyToneUpperFrequency_Type()
)
cdx6500VoiceCfgBusyToneUpperFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgBusyToneUpperFrequency.setStatus("mandatory")
_Cdx6500VoiceCfgBusyToneUpperFrequencyAmplitude_Type = DisplayString
_Cdx6500VoiceCfgBusyToneUpperFrequencyAmplitude_Object = MibTableColumn
cdx6500VoiceCfgBusyToneUpperFrequencyAmplitude = _Cdx6500VoiceCfgBusyToneUpperFrequencyAmplitude_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 91),
    _Cdx6500VoiceCfgBusyToneUpperFrequencyAmplitude_Type()
)
cdx6500VoiceCfgBusyToneUpperFrequencyAmplitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgBusyToneUpperFrequencyAmplitude.setStatus("mandatory")


class _Cdx6500VoiceCfgTxBusyToneOffTime_Type(Integer32):
    """Custom type cdx6500VoiceCfgTxBusyToneOffTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_Cdx6500VoiceCfgTxBusyToneOffTime_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgTxBusyToneOffTime_Object = MibTableColumn
cdx6500VoiceCfgTxBusyToneOffTime = _Cdx6500VoiceCfgTxBusyToneOffTime_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 92),
    _Cdx6500VoiceCfgTxBusyToneOffTime_Type()
)
cdx6500VoiceCfgTxBusyToneOffTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgTxBusyToneOffTime.setStatus("mandatory")


class _Cdx6500VoiceCfgTxBusyToneOnTime_Type(Integer32):
    """Custom type cdx6500VoiceCfgTxBusyToneOnTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_Cdx6500VoiceCfgTxBusyToneOnTime_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgTxBusyToneOnTime_Object = MibTableColumn
cdx6500VoiceCfgTxBusyToneOnTime = _Cdx6500VoiceCfgTxBusyToneOnTime_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 93),
    _Cdx6500VoiceCfgTxBusyToneOnTime_Type()
)
cdx6500VoiceCfgTxBusyToneOnTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgTxBusyToneOnTime.setStatus("mandatory")


class _Cdx6500VoiceCfgFastBusyToneLowerFrequency_Type(Integer32):
    """Custom type cdx6500VoiceCfgFastBusyToneLowerFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 3500),
    )


_Cdx6500VoiceCfgFastBusyToneLowerFrequency_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgFastBusyToneLowerFrequency_Object = MibTableColumn
cdx6500VoiceCfgFastBusyToneLowerFrequency = _Cdx6500VoiceCfgFastBusyToneLowerFrequency_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 94),
    _Cdx6500VoiceCfgFastBusyToneLowerFrequency_Type()
)
cdx6500VoiceCfgFastBusyToneLowerFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgFastBusyToneLowerFrequency.setStatus("mandatory")
_Cdx6500VoiceCfgFastBusyToneLowerFrequencyAmplitude_Type = DisplayString
_Cdx6500VoiceCfgFastBusyToneLowerFrequencyAmplitude_Object = MibTableColumn
cdx6500VoiceCfgFastBusyToneLowerFrequencyAmplitude = _Cdx6500VoiceCfgFastBusyToneLowerFrequencyAmplitude_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 95),
    _Cdx6500VoiceCfgFastBusyToneLowerFrequencyAmplitude_Type()
)
cdx6500VoiceCfgFastBusyToneLowerFrequencyAmplitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgFastBusyToneLowerFrequencyAmplitude.setStatus("mandatory")


class _Cdx6500VoiceCfgFastBusyToneUpperFrequency_Type(Integer32):
    """Custom type cdx6500VoiceCfgFastBusyToneUpperFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 3500),
    )


_Cdx6500VoiceCfgFastBusyToneUpperFrequency_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgFastBusyToneUpperFrequency_Object = MibTableColumn
cdx6500VoiceCfgFastBusyToneUpperFrequency = _Cdx6500VoiceCfgFastBusyToneUpperFrequency_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 96),
    _Cdx6500VoiceCfgFastBusyToneUpperFrequency_Type()
)
cdx6500VoiceCfgFastBusyToneUpperFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgFastBusyToneUpperFrequency.setStatus("mandatory")
_Cdx6500VoiceCfgFastBusyToneUpperFrequencyAmplitude_Type = DisplayString
_Cdx6500VoiceCfgFastBusyToneUpperFrequencyAmplitude_Object = MibTableColumn
cdx6500VoiceCfgFastBusyToneUpperFrequencyAmplitude = _Cdx6500VoiceCfgFastBusyToneUpperFrequencyAmplitude_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 97),
    _Cdx6500VoiceCfgFastBusyToneUpperFrequencyAmplitude_Type()
)
cdx6500VoiceCfgFastBusyToneUpperFrequencyAmplitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgFastBusyToneUpperFrequencyAmplitude.setStatus("mandatory")


class _Cdx6500VoiceCfgTxFastBusyToneOffTime_Type(Integer32):
    """Custom type cdx6500VoiceCfgTxFastBusyToneOffTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_Cdx6500VoiceCfgTxFastBusyToneOffTime_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgTxFastBusyToneOffTime_Object = MibTableColumn
cdx6500VoiceCfgTxFastBusyToneOffTime = _Cdx6500VoiceCfgTxFastBusyToneOffTime_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 98),
    _Cdx6500VoiceCfgTxFastBusyToneOffTime_Type()
)
cdx6500VoiceCfgTxFastBusyToneOffTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgTxFastBusyToneOffTime.setStatus("mandatory")


class _Cdx6500VoiceCfgTxFastBusyToneOnTime_Type(Integer32):
    """Custom type cdx6500VoiceCfgTxFastBusyToneOnTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_Cdx6500VoiceCfgTxFastBusyToneOnTime_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgTxFastBusyToneOnTime_Object = MibTableColumn
cdx6500VoiceCfgTxFastBusyToneOnTime = _Cdx6500VoiceCfgTxFastBusyToneOnTime_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 99),
    _Cdx6500VoiceCfgTxFastBusyToneOnTime_Type()
)
cdx6500VoiceCfgTxFastBusyToneOnTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgTxFastBusyToneOnTime.setStatus("mandatory")


class _Cdx6500VoiceCfgHybridFXO_Type(Integer32):
    """Custom type cdx6500VoiceCfgHybridFXO based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              11,
              100)
        )
    )
    namedValues = NamedValues(
        *(("adaptive", 11),
          ("nc", 100),
          ("sixHundred", 1))
    )


_Cdx6500VoiceCfgHybridFXO_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgHybridFXO_Object = MibTableColumn
cdx6500VoiceCfgHybridFXO = _Cdx6500VoiceCfgHybridFXO_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 100),
    _Cdx6500VoiceCfgHybridFXO_Type()
)
cdx6500VoiceCfgHybridFXO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgHybridFXO.setStatus("mandatory")


class _Cdx6500VoiceCfgTxPulse_Type(Integer32):
    """Custom type cdx6500VoiceCfgTxPulse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 200),
    )


_Cdx6500VoiceCfgTxPulse_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgTxPulse_Object = MibTableColumn
cdx6500VoiceCfgTxPulse = _Cdx6500VoiceCfgTxPulse_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 101),
    _Cdx6500VoiceCfgTxPulse_Type()
)
cdx6500VoiceCfgTxPulse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgTxPulse.setStatus("mandatory")


class _Cdx6500VoiceCfgRxMinPulse_Type(Integer32):
    """Custom type cdx6500VoiceCfgRxMinPulse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 200),
    )


_Cdx6500VoiceCfgRxMinPulse_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgRxMinPulse_Object = MibTableColumn
cdx6500VoiceCfgRxMinPulse = _Cdx6500VoiceCfgRxMinPulse_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 102),
    _Cdx6500VoiceCfgRxMinPulse_Type()
)
cdx6500VoiceCfgRxMinPulse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgRxMinPulse.setStatus("mandatory")


class _Cdx6500VoiceCfgRxMaxPulse_Type(Integer32):
    """Custom type cdx6500VoiceCfgRxMaxPulse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 200),
    )


_Cdx6500VoiceCfgRxMaxPulse_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgRxMaxPulse_Object = MibTableColumn
cdx6500VoiceCfgRxMaxPulse = _Cdx6500VoiceCfgRxMaxPulse_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 103),
    _Cdx6500VoiceCfgRxMaxPulse_Type()
)
cdx6500VoiceCfgRxMaxPulse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgRxMaxPulse.setStatus("mandatory")


class _Cdx6500VoiceCfgTxMasterClear_Type(Integer32):
    """Custom type cdx6500VoiceCfgTxMasterClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 2000),
    )


_Cdx6500VoiceCfgTxMasterClear_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgTxMasterClear_Object = MibTableColumn
cdx6500VoiceCfgTxMasterClear = _Cdx6500VoiceCfgTxMasterClear_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 104),
    _Cdx6500VoiceCfgTxMasterClear_Type()
)
cdx6500VoiceCfgTxMasterClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgTxMasterClear.setStatus("mandatory")


class _Cdx6500VoiceCfgRxMinMasterClear_Type(Integer32):
    """Custom type cdx6500VoiceCfgRxMinMasterClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 2000),
    )


_Cdx6500VoiceCfgRxMinMasterClear_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgRxMinMasterClear_Object = MibTableColumn
cdx6500VoiceCfgRxMinMasterClear = _Cdx6500VoiceCfgRxMinMasterClear_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 105),
    _Cdx6500VoiceCfgRxMinMasterClear_Type()
)
cdx6500VoiceCfgRxMinMasterClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgRxMinMasterClear.setStatus("mandatory")


class _Cdx6500VoiceCfgRxMaxMasterClear_Type(Integer32):
    """Custom type cdx6500VoiceCfgRxMaxMasterClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 2000),
    )


_Cdx6500VoiceCfgRxMaxMasterClear_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgRxMaxMasterClear_Object = MibTableColumn
cdx6500VoiceCfgRxMaxMasterClear = _Cdx6500VoiceCfgRxMaxMasterClear_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 106),
    _Cdx6500VoiceCfgRxMaxMasterClear_Type()
)
cdx6500VoiceCfgRxMaxMasterClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgRxMaxMasterClear.setStatus("mandatory")


class _Cdx6500VoiceCfgTxSlaveClear_Type(Integer32):
    """Custom type cdx6500VoiceCfgTxSlaveClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 2000),
    )


_Cdx6500VoiceCfgTxSlaveClear_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgTxSlaveClear_Object = MibTableColumn
cdx6500VoiceCfgTxSlaveClear = _Cdx6500VoiceCfgTxSlaveClear_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 107),
    _Cdx6500VoiceCfgTxSlaveClear_Type()
)
cdx6500VoiceCfgTxSlaveClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgTxSlaveClear.setStatus("mandatory")


class _Cdx6500VoiceCfgRxMinSlaveClear_Type(Integer32):
    """Custom type cdx6500VoiceCfgRxMinSlaveClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 2000),
    )


_Cdx6500VoiceCfgRxMinSlaveClear_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgRxMinSlaveClear_Object = MibTableColumn
cdx6500VoiceCfgRxMinSlaveClear = _Cdx6500VoiceCfgRxMinSlaveClear_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 108),
    _Cdx6500VoiceCfgRxMinSlaveClear_Type()
)
cdx6500VoiceCfgRxMinSlaveClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgRxMinSlaveClear.setStatus("mandatory")


class _Cdx6500VoiceCfgRxMaxSlaveClear_Type(Integer32):
    """Custom type cdx6500VoiceCfgRxMaxSlaveClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 2000),
    )


_Cdx6500VoiceCfgRxMaxSlaveClear_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgRxMaxSlaveClear_Object = MibTableColumn
cdx6500VoiceCfgRxMaxSlaveClear = _Cdx6500VoiceCfgRxMaxSlaveClear_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 109),
    _Cdx6500VoiceCfgRxMaxSlaveClear_Type()
)
cdx6500VoiceCfgRxMaxSlaveClear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgRxMaxSlaveClear.setStatus("mandatory")


class _Cdx6500VoiceCfgTxSlaveRelease_Type(Integer32):
    """Custom type cdx6500VoiceCfgTxSlaveRelease based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_Cdx6500VoiceCfgTxSlaveRelease_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgTxSlaveRelease_Object = MibTableColumn
cdx6500VoiceCfgTxSlaveRelease = _Cdx6500VoiceCfgTxSlaveRelease_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 110),
    _Cdx6500VoiceCfgTxSlaveRelease_Type()
)
cdx6500VoiceCfgTxSlaveRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgTxSlaveRelease.setStatus("mandatory")


class _Cdx6500VoiceCfgRxMinSlaveRelease_Type(Integer32):
    """Custom type cdx6500VoiceCfgRxMinSlaveRelease based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_Cdx6500VoiceCfgRxMinSlaveRelease_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgRxMinSlaveRelease_Object = MibTableColumn
cdx6500VoiceCfgRxMinSlaveRelease = _Cdx6500VoiceCfgRxMinSlaveRelease_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 111),
    _Cdx6500VoiceCfgRxMinSlaveRelease_Type()
)
cdx6500VoiceCfgRxMinSlaveRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgRxMinSlaveRelease.setStatus("mandatory")


class _Cdx6500VoiceCfgRxMaxSlaveRelease_Type(Integer32):
    """Custom type cdx6500VoiceCfgRxMaxSlaveRelease based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_Cdx6500VoiceCfgRxMaxSlaveRelease_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgRxMaxSlaveRelease_Object = MibTableColumn
cdx6500VoiceCfgRxMaxSlaveRelease = _Cdx6500VoiceCfgRxMaxSlaveRelease_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 112),
    _Cdx6500VoiceCfgRxMaxSlaveRelease_Type()
)
cdx6500VoiceCfgRxMaxSlaveRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgRxMaxSlaveRelease.setStatus("mandatory")


class _Cdx6500VoiceCfgTxPTSTime_Type(Integer32):
    """Custom type cdx6500VoiceCfgTxPTSTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_Cdx6500VoiceCfgTxPTSTime_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgTxPTSTime_Object = MibTableColumn
cdx6500VoiceCfgTxPTSTime = _Cdx6500VoiceCfgTxPTSTime_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 113),
    _Cdx6500VoiceCfgTxPTSTime_Type()
)
cdx6500VoiceCfgTxPTSTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgTxPTSTime.setStatus("mandatory")


class _Cdx6500VoiceCfgRxPTSTime_Type(Integer32):
    """Custom type cdx6500VoiceCfgRxPTSTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_Cdx6500VoiceCfgRxPTSTime_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgRxPTSTime_Object = MibTableColumn
cdx6500VoiceCfgRxPTSTime = _Cdx6500VoiceCfgRxPTSTime_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 114),
    _Cdx6500VoiceCfgRxPTSTime_Type()
)
cdx6500VoiceCfgRxPTSTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgRxPTSTime.setStatus("mandatory")


class _Cdx6500VoiceCfgMasterGuard_Type(Integer32):
    """Custom type cdx6500VoiceCfgMasterGuard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_Cdx6500VoiceCfgMasterGuard_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgMasterGuard_Object = MibTableColumn
cdx6500VoiceCfgMasterGuard = _Cdx6500VoiceCfgMasterGuard_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 115),
    _Cdx6500VoiceCfgMasterGuard_Type()
)
cdx6500VoiceCfgMasterGuard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgMasterGuard.setStatus("mandatory")


class _Cdx6500VoiceCfgSlaveGuard_Type(Integer32):
    """Custom type cdx6500VoiceCfgSlaveGuard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_Cdx6500VoiceCfgSlaveGuard_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgSlaveGuard_Object = MibTableColumn
cdx6500VoiceCfgSlaveGuard = _Cdx6500VoiceCfgSlaveGuard_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 116),
    _Cdx6500VoiceCfgSlaveGuard_Type()
)
cdx6500VoiceCfgSlaveGuard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgSlaveGuard.setStatus("mandatory")


class _Cdx6500VoiceCfgTxFlashHookTime_Type(Integer32):
    """Custom type cdx6500VoiceCfgTxFlashHookTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 10000),
    )


_Cdx6500VoiceCfgTxFlashHookTime_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgTxFlashHookTime_Object = MibTableColumn
cdx6500VoiceCfgTxFlashHookTime = _Cdx6500VoiceCfgTxFlashHookTime_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 117),
    _Cdx6500VoiceCfgTxFlashHookTime_Type()
)
cdx6500VoiceCfgTxFlashHookTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgTxFlashHookTime.setStatus("mandatory")
_Cdx6500VoiceCfgDtmfAmplitude_Type = DisplayString
_Cdx6500VoiceCfgDtmfAmplitude_Object = MibTableColumn
cdx6500VoiceCfgDtmfAmplitude = _Cdx6500VoiceCfgDtmfAmplitude_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 118),
    _Cdx6500VoiceCfgDtmfAmplitude_Type()
)
cdx6500VoiceCfgDtmfAmplitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgDtmfAmplitude.setStatus("mandatory")


class _Cdx6500VoiceCfgFXSOffhookFilter_Type(Integer32):
    """Custom type cdx6500VoiceCfgFXSOffhookFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 500),
    )


_Cdx6500VoiceCfgFXSOffhookFilter_Type.__name__ = "Integer32"
_Cdx6500VoiceCfgFXSOffhookFilter_Object = MibTableColumn
cdx6500VoiceCfgFXSOffhookFilter = _Cdx6500VoiceCfgFXSOffhookFilter_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 1, 1, 25, 1, 1, 119),
    _Cdx6500VoiceCfgFXSOffhookFilter_Type()
)
cdx6500VoiceCfgFXSOffhookFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCfgFXSOffhookFilter.setStatus("mandatory")
_Cdx6500CfgGeneralGroup_ObjectIdentity = ObjectIdentity
cdx6500CfgGeneralGroup = _Cdx6500CfgGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2)
)
_Cdx6500GCTVoiceSwitchTable_ObjectIdentity = ObjectIdentity
cdx6500GCTVoiceSwitchTable = _Cdx6500GCTVoiceSwitchTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 21)
)
_Cdx6500GGCTVoiceSwitchTable_Object = MibTable
cdx6500GGCTVoiceSwitchTable = _Cdx6500GGCTVoiceSwitchTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 21, 1)
)
if mibBuilder.loadTexts:
    cdx6500GGCTVoiceSwitchTable.setStatus("mandatory")
_Cdx6500VoiceSwitchEntry_Object = MibTableRow
cdx6500VoiceSwitchEntry = _Cdx6500VoiceSwitchEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 21, 1, 1)
)
cdx6500VoiceSwitchEntry.setIndexNames(
    (0, "VOICE-OPT-MIB", "cdx6500VoiceSwitchEntryNumber"),
)
if mibBuilder.loadTexts:
    cdx6500VoiceSwitchEntry.setStatus("mandatory")


class _Cdx6500VoiceSwitchRxDTMFDigitString_Type(DisplayString):
    """Custom type cdx6500VoiceSwitchRxDTMFDigitString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Cdx6500VoiceSwitchRxDTMFDigitString_Type.__name__ = "DisplayString"
_Cdx6500VoiceSwitchRxDTMFDigitString_Object = MibTableColumn
cdx6500VoiceSwitchRxDTMFDigitString = _Cdx6500VoiceSwitchRxDTMFDigitString_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 21, 1, 1, 1),
    _Cdx6500VoiceSwitchRxDTMFDigitString_Type()
)
cdx6500VoiceSwitchRxDTMFDigitString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceSwitchRxDTMFDigitString.setStatus("mandatory")


class _Cdx6500VoiceSwitchNumRxDigitToReceive_Type(Integer32):
    """Custom type cdx6500VoiceSwitchNumRxDigitToReceive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_Cdx6500VoiceSwitchNumRxDigitToReceive_Type.__name__ = "Integer32"
_Cdx6500VoiceSwitchNumRxDigitToReceive_Object = MibTableColumn
cdx6500VoiceSwitchNumRxDigitToReceive = _Cdx6500VoiceSwitchNumRxDigitToReceive_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 21, 1, 1, 2),
    _Cdx6500VoiceSwitchNumRxDigitToReceive_Type()
)
cdx6500VoiceSwitchNumRxDigitToReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceSwitchNumRxDigitToReceive.setStatus("mandatory")


class _Cdx6500VoiceSwitchCallParam_Type(DisplayString):
    """Custom type cdx6500VoiceSwitchCallParam based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Cdx6500VoiceSwitchCallParam_Type.__name__ = "DisplayString"
_Cdx6500VoiceSwitchCallParam_Object = MibTableColumn
cdx6500VoiceSwitchCallParam = _Cdx6500VoiceSwitchCallParam_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 21, 1, 1, 3),
    _Cdx6500VoiceSwitchCallParam_Type()
)
cdx6500VoiceSwitchCallParam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceSwitchCallParam.setStatus("mandatory")


class _Cdx6500VoiceSwitchAlternateDestination_Type(Integer32):
    """Custom type cdx6500VoiceSwitchAlternateDestination based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("deprecatedObj", 1)
    )


_Cdx6500VoiceSwitchAlternateDestination_Type.__name__ = "Integer32"
_Cdx6500VoiceSwitchAlternateDestination_Object = MibTableColumn
cdx6500VoiceSwitchAlternateDestination = _Cdx6500VoiceSwitchAlternateDestination_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 21, 1, 1, 4),
    _Cdx6500VoiceSwitchAlternateDestination_Type()
)
cdx6500VoiceSwitchAlternateDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceSwitchAlternateDestination.setStatus("deprecated")


class _Cdx6500VoiceSwitchCompressionOverrideRate_Type(Integer32):
    """Custom type cdx6500VoiceSwitchCompressionOverrideRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              7,
              8,
              10,
              11,
              14,
              15,
              100)
        )
    )
    namedValues = NamedValues(
        *(("cBD16K", 11),
          ("cBD8K", 10),
          ("cD16K", 8),
          ("cD8K", 7),
          ("cE16Kb", 15),
          ("cE8Kb", 14),
          ("nc", 100),
          ("none", 6))
    )


_Cdx6500VoiceSwitchCompressionOverrideRate_Type.__name__ = "Integer32"
_Cdx6500VoiceSwitchCompressionOverrideRate_Object = MibTableColumn
cdx6500VoiceSwitchCompressionOverrideRate = _Cdx6500VoiceSwitchCompressionOverrideRate_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 21, 1, 1, 5),
    _Cdx6500VoiceSwitchCompressionOverrideRate_Type()
)
cdx6500VoiceSwitchCompressionOverrideRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceSwitchCompressionOverrideRate.setStatus("mandatory")


class _Cdx6500VoiceSwitchNumLeadingDigitToStrip_Type(Integer32):
    """Custom type cdx6500VoiceSwitchNumLeadingDigitToStrip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_Cdx6500VoiceSwitchNumLeadingDigitToStrip_Type.__name__ = "Integer32"
_Cdx6500VoiceSwitchNumLeadingDigitToStrip_Object = MibTableColumn
cdx6500VoiceSwitchNumLeadingDigitToStrip = _Cdx6500VoiceSwitchNumLeadingDigitToStrip_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 21, 1, 1, 6),
    _Cdx6500VoiceSwitchNumLeadingDigitToStrip_Type()
)
cdx6500VoiceSwitchNumLeadingDigitToStrip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceSwitchNumLeadingDigitToStrip.setStatus("mandatory")


class _Cdx6500VoiceSwitchPreFixDigits_Type(DisplayString):
    """Custom type cdx6500VoiceSwitchPreFixDigits based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Cdx6500VoiceSwitchPreFixDigits_Type.__name__ = "DisplayString"
_Cdx6500VoiceSwitchPreFixDigits_Object = MibTableColumn
cdx6500VoiceSwitchPreFixDigits = _Cdx6500VoiceSwitchPreFixDigits_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 21, 1, 1, 7),
    _Cdx6500VoiceSwitchPreFixDigits_Type()
)
cdx6500VoiceSwitchPreFixDigits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceSwitchPreFixDigits.setStatus("mandatory")


class _Cdx6500VoiceSwitchPostFixDigits_Type(DisplayString):
    """Custom type cdx6500VoiceSwitchPostFixDigits based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Cdx6500VoiceSwitchPostFixDigits_Type.__name__ = "DisplayString"
_Cdx6500VoiceSwitchPostFixDigits_Object = MibTableColumn
cdx6500VoiceSwitchPostFixDigits = _Cdx6500VoiceSwitchPostFixDigits_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 21, 1, 1, 8),
    _Cdx6500VoiceSwitchPostFixDigits_Type()
)
cdx6500VoiceSwitchPostFixDigits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceSwitchPostFixDigits.setStatus("deprecated")
_Cdx6500VoiceSwitchEntryNumber_Type = Integer32
_Cdx6500VoiceSwitchEntryNumber_Object = MibTableColumn
cdx6500VoiceSwitchEntryNumber = _Cdx6500VoiceSwitchEntryNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 2, 2, 21, 1, 1, 9),
    _Cdx6500VoiceSwitchEntryNumber_Type()
)
cdx6500VoiceSwitchEntryNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceSwitchEntryNumber.setStatus("mandatory")
_Cdx6500Statistics_ObjectIdentity = ObjectIdentity
cdx6500Statistics = _Cdx6500Statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3)
)
_Cdx6500StatProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500StatProtocolGroup = _Cdx6500StatProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1)
)
_Cdx6500PSTPortProtocolGroup_ObjectIdentity = ObjectIdentity
cdx6500PSTPortProtocolGroup = _Cdx6500PSTPortProtocolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1)
)
_Cdx6500PSTVoicePortTable_ObjectIdentity = ObjectIdentity
cdx6500PSTVoicePortTable = _Cdx6500PSTVoicePortTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 26)
)
_Cdx6500PPSTVoicePortTable_Object = MibTable
cdx6500PPSTVoicePortTable = _Cdx6500PPSTVoicePortTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 26, 1)
)
if mibBuilder.loadTexts:
    cdx6500PPSTVoicePortTable.setStatus("mandatory")
_Cdx6500PPSTVoicePortEntry_Object = MibTableRow
cdx6500PPSTVoicePortEntry = _Cdx6500PPSTVoicePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 26, 1, 1)
)
cdx6500PPSTVoicePortEntry.setIndexNames(
    (0, "VOICE-OPT-MIB", "cdx6500VoiceStatsPortNumber"),
)
if mibBuilder.loadTexts:
    cdx6500PPSTVoicePortEntry.setStatus("mandatory")


class _Cdx6500VoiceStatsPortNumber_Type(Integer32):
    """Custom type cdx6500VoiceStatsPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Cdx6500VoiceStatsPortNumber_Type.__name__ = "Integer32"
_Cdx6500VoiceStatsPortNumber_Object = MibTableColumn
cdx6500VoiceStatsPortNumber = _Cdx6500VoiceStatsPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 26, 1, 1, 1),
    _Cdx6500VoiceStatsPortNumber_Type()
)
cdx6500VoiceStatsPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceStatsPortNumber.setStatus("mandatory")


class _Cdx6500VoiceStatsPortInterfaceType_Type(Integer32):
    """Custom type cdx6500VoiceStatsPortInterfaceType based on Integer32"""
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
        *(("eAndM2", 1),
          ("eAndM4", 2),
          ("fxo", 3),
          ("fxs", 4))
    )


_Cdx6500VoiceStatsPortInterfaceType_Type.__name__ = "Integer32"
_Cdx6500VoiceStatsPortInterfaceType_Object = MibTableColumn
cdx6500VoiceStatsPortInterfaceType = _Cdx6500VoiceStatsPortInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 26, 1, 1, 2),
    _Cdx6500VoiceStatsPortInterfaceType_Type()
)
cdx6500VoiceStatsPortInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceStatsPortInterfaceType.setStatus("mandatory")
_Cdx6500VoiceStatsHWRevAndPartNumber_Type = DisplayString
_Cdx6500VoiceStatsHWRevAndPartNumber_Object = MibTableColumn
cdx6500VoiceStatsHWRevAndPartNumber = _Cdx6500VoiceStatsHWRevAndPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 26, 1, 1, 3),
    _Cdx6500VoiceStatsHWRevAndPartNumber_Type()
)
cdx6500VoiceStatsHWRevAndPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceStatsHWRevAndPartNumber.setStatus("mandatory")


class _Cdx6500VoiceStatsFortyEightVolts_Type(Integer32):
    """Custom type cdx6500VoiceStatsFortyEightVolts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              100)
        )
    )
    namedValues = NamedValues(
        *(("na", 100),
          ("none", 1),
          ("present", 2))
    )


_Cdx6500VoiceStatsFortyEightVolts_Type.__name__ = "Integer32"
_Cdx6500VoiceStatsFortyEightVolts_Object = MibTableColumn
cdx6500VoiceStatsFortyEightVolts = _Cdx6500VoiceStatsFortyEightVolts_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 26, 1, 1, 4),
    _Cdx6500VoiceStatsFortyEightVolts_Type()
)
cdx6500VoiceStatsFortyEightVolts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceStatsFortyEightVolts.setStatus("mandatory")


class _Cdx6500VoiceStatsPortState_Type(Integer32):
    """Custom type cdx6500VoiceStatsPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_Cdx6500VoiceStatsPortState_Type.__name__ = "Integer32"
_Cdx6500VoiceStatsPortState_Object = MibTableColumn
cdx6500VoiceStatsPortState = _Cdx6500VoiceStatsPortState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 26, 1, 1, 5),
    _Cdx6500VoiceStatsPortState_Type()
)
cdx6500VoiceStatsPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceStatsPortState.setStatus("mandatory")


class _Cdx6500VoiceStatsCircuitState_Type(Integer32):
    """Custom type cdx6500VoiceStatsCircuitState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connected", 1),
          ("disconnected", 2))
    )


_Cdx6500VoiceStatsCircuitState_Type.__name__ = "Integer32"
_Cdx6500VoiceStatsCircuitState_Object = MibTableColumn
cdx6500VoiceStatsCircuitState = _Cdx6500VoiceStatsCircuitState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 26, 1, 1, 6),
    _Cdx6500VoiceStatsCircuitState_Type()
)
cdx6500VoiceStatsCircuitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceStatsCircuitState.setStatus("mandatory")


class _Cdx6500VoiceStatsCurrentMode_Type(Integer32):
    """Custom type cdx6500VoiceStatsCurrentMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fax", 3),
          ("pcm", 2),
          ("voice", 1))
    )


_Cdx6500VoiceStatsCurrentMode_Type.__name__ = "Integer32"
_Cdx6500VoiceStatsCurrentMode_Object = MibTableColumn
cdx6500VoiceStatsCurrentMode = _Cdx6500VoiceStatsCurrentMode_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 26, 1, 1, 7),
    _Cdx6500VoiceStatsCurrentMode_Type()
)
cdx6500VoiceStatsCurrentMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceStatsCurrentMode.setStatus("mandatory")
_Cdx6500VoiceStatsTimeOfLastStatReset_Type = DisplayString
_Cdx6500VoiceStatsTimeOfLastStatReset_Object = MibTableColumn
cdx6500VoiceStatsTimeOfLastStatReset = _Cdx6500VoiceStatsTimeOfLastStatReset_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 26, 1, 1, 8),
    _Cdx6500VoiceStatsTimeOfLastStatReset_Type()
)
cdx6500VoiceStatsTimeOfLastStatReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceStatsTimeOfLastStatReset.setStatus("mandatory")
_Cdx6500VoiceStatsCallDuration_Type = DisplayString
_Cdx6500VoiceStatsCallDuration_Object = MibTableColumn
cdx6500VoiceStatsCallDuration = _Cdx6500VoiceStatsCallDuration_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 26, 1, 1, 9),
    _Cdx6500VoiceStatsCallDuration_Type()
)
cdx6500VoiceStatsCallDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceStatsCallDuration.setStatus("mandatory")
_Cdx6500VoiceStatsTotalCallDuration_Type = DisplayString
_Cdx6500VoiceStatsTotalCallDuration_Object = MibTableColumn
cdx6500VoiceStatsTotalCallDuration = _Cdx6500VoiceStatsTotalCallDuration_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 26, 1, 1, 10),
    _Cdx6500VoiceStatsTotalCallDuration_Type()
)
cdx6500VoiceStatsTotalCallDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceStatsTotalCallDuration.setStatus("mandatory")


class _Cdx6500VoiceStatsPortUtilization_Type(Integer32):
    """Custom type cdx6500VoiceStatsPortUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Cdx6500VoiceStatsPortUtilization_Type.__name__ = "Integer32"
_Cdx6500VoiceStatsPortUtilization_Object = MibTableColumn
cdx6500VoiceStatsPortUtilization = _Cdx6500VoiceStatsPortUtilization_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 26, 1, 1, 11),
    _Cdx6500VoiceStatsPortUtilization_Type()
)
cdx6500VoiceStatsPortUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceStatsPortUtilization.setStatus("mandatory")
_Cdx6500VoiceStatsNumberOfCalls_Type = Counter32
_Cdx6500VoiceStatsNumberOfCalls_Object = MibTableColumn
cdx6500VoiceStatsNumberOfCalls = _Cdx6500VoiceStatsNumberOfCalls_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 26, 1, 1, 12),
    _Cdx6500VoiceStatsNumberOfCalls_Type()
)
cdx6500VoiceStatsNumberOfCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceStatsNumberOfCalls.setStatus("mandatory")
_Cdx6500VoiceStatsLastDigitsTransmitted_Type = DisplayString
_Cdx6500VoiceStatsLastDigitsTransmitted_Object = MibTableColumn
cdx6500VoiceStatsLastDigitsTransmitted = _Cdx6500VoiceStatsLastDigitsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 26, 1, 1, 13),
    _Cdx6500VoiceStatsLastDigitsTransmitted_Type()
)
cdx6500VoiceStatsLastDigitsTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceStatsLastDigitsTransmitted.setStatus("mandatory")
_Cdx6500VoiceStatsLastDigitsReceived_Type = DisplayString
_Cdx6500VoiceStatsLastDigitsReceived_Object = MibTableColumn
cdx6500VoiceStatsLastDigitsReceived = _Cdx6500VoiceStatsLastDigitsReceived_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 26, 1, 1, 14),
    _Cdx6500VoiceStatsLastDigitsReceived_Type()
)
cdx6500VoiceStatsLastDigitsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceStatsLastDigitsReceived.setStatus("mandatory")
_Cdx6500VoiceStatsTxPacketDropped_Type = Counter32
_Cdx6500VoiceStatsTxPacketDropped_Object = MibTableColumn
cdx6500VoiceStatsTxPacketDropped = _Cdx6500VoiceStatsTxPacketDropped_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 26, 1, 1, 15),
    _Cdx6500VoiceStatsTxPacketDropped_Type()
)
cdx6500VoiceStatsTxPacketDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceStatsTxPacketDropped.setStatus("mandatory")
_Cdx6500VoiceStatsRxPacketDropped_Type = Counter32
_Cdx6500VoiceStatsRxPacketDropped_Object = MibTableColumn
cdx6500VoiceStatsRxPacketDropped = _Cdx6500VoiceStatsRxPacketDropped_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 26, 1, 1, 16),
    _Cdx6500VoiceStatsRxPacketDropped_Type()
)
cdx6500VoiceStatsRxPacketDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceStatsRxPacketDropped.setStatus("mandatory")
_Cdx6500VoiceStatsDroppedPackets_Type = Counter32
_Cdx6500VoiceStatsDroppedPackets_Object = MibTableColumn
cdx6500VoiceStatsDroppedPackets = _Cdx6500VoiceStatsDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 26, 1, 1, 17),
    _Cdx6500VoiceStatsDroppedPackets_Type()
)
cdx6500VoiceStatsDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceStatsDroppedPackets.setStatus("mandatory")
_Cdx6500VoiceStatsDSPInternalFaults_Type = Counter32
_Cdx6500VoiceStatsDSPInternalFaults_Object = MibTableColumn
cdx6500VoiceStatsDSPInternalFaults = _Cdx6500VoiceStatsDSPInternalFaults_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 26, 1, 1, 18),
    _Cdx6500VoiceStatsDSPInternalFaults_Type()
)
cdx6500VoiceStatsDSPInternalFaults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceStatsDSPInternalFaults.setStatus("mandatory")
_Cdx6500VoiceStatsTxPackets_Type = Counter32
_Cdx6500VoiceStatsTxPackets_Object = MibTableColumn
cdx6500VoiceStatsTxPackets = _Cdx6500VoiceStatsTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 26, 1, 1, 19),
    _Cdx6500VoiceStatsTxPackets_Type()
)
cdx6500VoiceStatsTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceStatsTxPackets.setStatus("mandatory")
_Cdx6500VoiceStatsRxPackets_Type = Counter32
_Cdx6500VoiceStatsRxPackets_Object = MibTableColumn
cdx6500VoiceStatsRxPackets = _Cdx6500VoiceStatsRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 26, 1, 1, 20),
    _Cdx6500VoiceStatsRxPackets_Type()
)
cdx6500VoiceStatsRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceStatsRxPackets.setStatus("mandatory")
_Cdx6500VoiceStatsTxPacketsPerSecond_Type = Counter32
_Cdx6500VoiceStatsTxPacketsPerSecond_Object = MibTableColumn
cdx6500VoiceStatsTxPacketsPerSecond = _Cdx6500VoiceStatsTxPacketsPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 26, 1, 1, 21),
    _Cdx6500VoiceStatsTxPacketsPerSecond_Type()
)
cdx6500VoiceStatsTxPacketsPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceStatsTxPacketsPerSecond.setStatus("mandatory")
_Cdx6500VoiceStatsRxPacketsPerSecond_Type = Counter32
_Cdx6500VoiceStatsRxPacketsPerSecond_Object = MibTableColumn
cdx6500VoiceStatsRxPacketsPerSecond = _Cdx6500VoiceStatsRxPacketsPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 26, 1, 1, 22),
    _Cdx6500VoiceStatsRxPacketsPerSecond_Type()
)
cdx6500VoiceStatsRxPacketsPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceStatsRxPacketsPerSecond.setStatus("mandatory")


class _Cdx6500VoiceStatsDSIEfficiency_Type(Integer32):
    """Custom type cdx6500VoiceStatsDSIEfficiency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Cdx6500VoiceStatsDSIEfficiency_Type.__name__ = "Integer32"
_Cdx6500VoiceStatsDSIEfficiency_Object = MibTableColumn
cdx6500VoiceStatsDSIEfficiency = _Cdx6500VoiceStatsDSIEfficiency_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 26, 1, 1, 23),
    _Cdx6500VoiceStatsDSIEfficiency_Type()
)
cdx6500VoiceStatsDSIEfficiency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceStatsDSIEfficiency.setStatus("mandatory")


class _Cdx6500VoiceStatsCurrentRate_Type(Integer32):
    """Custom type cdx6500VoiceStatsCurrentRate based on Integer32"""
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
              100)
        )
    )
    namedValues = NamedValues(
        *(("cBD16K", 5),
          ("cBD8K", 2),
          ("cD16K", 4),
          ("cD8K", 1),
          ("cE16Kb", 6),
          ("cE8Kb", 3),
          ("cFax", 8),
          ("cPcm", 7),
          ("na", 100))
    )


_Cdx6500VoiceStatsCurrentRate_Type.__name__ = "Integer32"
_Cdx6500VoiceStatsCurrentRate_Object = MibTableColumn
cdx6500VoiceStatsCurrentRate = _Cdx6500VoiceStatsCurrentRate_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 26, 1, 1, 24),
    _Cdx6500VoiceStatsCurrentRate_Type()
)
cdx6500VoiceStatsCurrentRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceStatsCurrentRate.setStatus("mandatory")
_Cdx6500VoiceStatsInputPower_Type = DisplayString
_Cdx6500VoiceStatsInputPower_Object = MibTableColumn
cdx6500VoiceStatsInputPower = _Cdx6500VoiceStatsInputPower_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 26, 1, 1, 25),
    _Cdx6500VoiceStatsInputPower_Type()
)
cdx6500VoiceStatsInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceStatsInputPower.setStatus("mandatory")
_Cdx6500VoiceStatsOutputPower_Type = DisplayString
_Cdx6500VoiceStatsOutputPower_Object = MibTableColumn
cdx6500VoiceStatsOutputPower = _Cdx6500VoiceStatsOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 26, 1, 1, 26),
    _Cdx6500VoiceStatsOutputPower_Type()
)
cdx6500VoiceStatsOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceStatsOutputPower.setStatus("mandatory")
_Cdx6500VoiceStatsFAXTransmissions_Type = Integer32
_Cdx6500VoiceStatsFAXTransmissions_Object = MibTableColumn
cdx6500VoiceStatsFAXTransmissions = _Cdx6500VoiceStatsFAXTransmissions_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 26, 1, 1, 27),
    _Cdx6500VoiceStatsFAXTransmissions_Type()
)
cdx6500VoiceStatsFAXTransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceStatsFAXTransmissions.setStatus("mandatory")
_Cdx6500VoiceStatsUnsupportedFmtsFAXXmissions_Type = Integer32
_Cdx6500VoiceStatsUnsupportedFmtsFAXXmissions_Object = MibTableColumn
cdx6500VoiceStatsUnsupportedFmtsFAXXmissions = _Cdx6500VoiceStatsUnsupportedFmtsFAXXmissions_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 26, 1, 1, 28),
    _Cdx6500VoiceStatsUnsupportedFmtsFAXXmissions_Type()
)
cdx6500VoiceStatsUnsupportedFmtsFAXXmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceStatsUnsupportedFmtsFAXXmissions.setStatus("mandatory")
_Cdx6500PPSTSignalingSequenceTrapTxState_Type = DisplayString
_Cdx6500PPSTSignalingSequenceTrapTxState_Object = MibTableColumn
cdx6500PPSTSignalingSequenceTrapTxState = _Cdx6500PPSTSignalingSequenceTrapTxState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 26, 1, 1, 29),
    _Cdx6500PPSTSignalingSequenceTrapTxState_Type()
)
cdx6500PPSTSignalingSequenceTrapTxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PPSTSignalingSequenceTrapTxState.setStatus("deprecated")
_Cdx6500PPSTSignalingSequenceTrapRxState_Type = DisplayString
_Cdx6500PPSTSignalingSequenceTrapRxState_Object = MibTableColumn
cdx6500PPSTSignalingSequenceTrapRxState = _Cdx6500PPSTSignalingSequenceTrapRxState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 26, 1, 1, 30),
    _Cdx6500PPSTSignalingSequenceTrapRxState_Type()
)
cdx6500PPSTSignalingSequenceTrapRxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PPSTSignalingSequenceTrapRxState.setStatus("deprecated")


class _Cdx6500PPSTSignalingSequenceTrapMachineState_Type(DisplayString):
    """Custom type cdx6500PPSTSignalingSequenceTrapMachineState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )


_Cdx6500PPSTSignalingSequenceTrapMachineState_Type.__name__ = "DisplayString"
_Cdx6500PPSTSignalingSequenceTrapMachineState_Object = MibTableColumn
cdx6500PPSTSignalingSequenceTrapMachineState = _Cdx6500PPSTSignalingSequenceTrapMachineState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 26, 1, 1, 31),
    _Cdx6500PPSTSignalingSequenceTrapMachineState_Type()
)
cdx6500PPSTSignalingSequenceTrapMachineState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PPSTSignalingSequenceTrapMachineState.setStatus("deprecated")
_Cdx6500PPSTSignalingSequenceTrapTimeSinceLastChange_Type = Integer32
_Cdx6500PPSTSignalingSequenceTrapTimeSinceLastChange_Object = MibTableColumn
cdx6500PPSTSignalingSequenceTrapTimeSinceLastChange = _Cdx6500PPSTSignalingSequenceTrapTimeSinceLastChange_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 26, 1, 1, 32),
    _Cdx6500PPSTSignalingSequenceTrapTimeSinceLastChange_Type()
)
cdx6500PPSTSignalingSequenceTrapTimeSinceLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PPSTSignalingSequenceTrapTimeSinceLastChange.setStatus("deprecated")


class _Cdx6500PPSTSignalingSequenceTrapComment_Type(DisplayString):
    """Custom type cdx6500PPSTSignalingSequenceTrapComment based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Cdx6500PPSTSignalingSequenceTrapComment_Type.__name__ = "DisplayString"
_Cdx6500PPSTSignalingSequenceTrapComment_Object = MibTableColumn
cdx6500PPSTSignalingSequenceTrapComment = _Cdx6500PPSTSignalingSequenceTrapComment_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 26, 1, 1, 33),
    _Cdx6500PPSTSignalingSequenceTrapComment_Type()
)
cdx6500PPSTSignalingSequenceTrapComment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500PPSTSignalingSequenceTrapComment.setStatus("deprecated")


class _Cdx6500VoiceStatsCurrentStatus_Type(Integer32):
    """Custom type cdx6500VoiceStatsCurrentStatus based on Integer32"""
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
        *(("called", 4),
          ("calling", 3),
          ("connected", 5),
          ("disconnected", 2),
          ("inhibited", 1),
          ("null", 6))
    )


_Cdx6500VoiceStatsCurrentStatus_Type.__name__ = "Integer32"
_Cdx6500VoiceStatsCurrentStatus_Object = MibTableColumn
cdx6500VoiceStatsCurrentStatus = _Cdx6500VoiceStatsCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 26, 1, 1, 34),
    _Cdx6500VoiceStatsCurrentStatus_Type()
)
cdx6500VoiceStatsCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceStatsCurrentStatus.setStatus("mandatory")
_Cdx6500VoiceStatsLastClearCauseCode_Type = DisplayString
_Cdx6500VoiceStatsLastClearCauseCode_Object = MibTableColumn
cdx6500VoiceStatsLastClearCauseCode = _Cdx6500VoiceStatsLastClearCauseCode_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 26, 1, 1, 35),
    _Cdx6500VoiceStatsLastClearCauseCode_Type()
)
cdx6500VoiceStatsLastClearCauseCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceStatsLastClearCauseCode.setStatus("mandatory")
_Cdx6500VoiceStatsLastClearDiagnosticCode_Type = DisplayString
_Cdx6500VoiceStatsLastClearDiagnosticCode_Object = MibTableColumn
cdx6500VoiceStatsLastClearDiagnosticCode = _Cdx6500VoiceStatsLastClearDiagnosticCode_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 26, 1, 1, 36),
    _Cdx6500VoiceStatsLastClearDiagnosticCode_Type()
)
cdx6500VoiceStatsLastClearDiagnosticCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceStatsLastClearDiagnosticCode.setStatus("mandatory")


class _Cdx6500VoiceStatsLastInboundCallPacketCalledAddress_Type(DisplayString):
    """Custom type cdx6500VoiceStatsLastInboundCallPacketCalledAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 15),
    )


_Cdx6500VoiceStatsLastInboundCallPacketCalledAddress_Type.__name__ = "DisplayString"
_Cdx6500VoiceStatsLastInboundCallPacketCalledAddress_Object = MibTableColumn
cdx6500VoiceStatsLastInboundCallPacketCalledAddress = _Cdx6500VoiceStatsLastInboundCallPacketCalledAddress_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 26, 1, 1, 37),
    _Cdx6500VoiceStatsLastInboundCallPacketCalledAddress_Type()
)
cdx6500VoiceStatsLastInboundCallPacketCalledAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceStatsLastInboundCallPacketCalledAddress.setStatus("mandatory")


class _Cdx6500VoiceStatsLastInboundCallPacketCallingAddress_Type(DisplayString):
    """Custom type cdx6500VoiceStatsLastInboundCallPacketCallingAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 15),
    )


_Cdx6500VoiceStatsLastInboundCallPacketCallingAddress_Type.__name__ = "DisplayString"
_Cdx6500VoiceStatsLastInboundCallPacketCallingAddress_Object = MibTableColumn
cdx6500VoiceStatsLastInboundCallPacketCallingAddress = _Cdx6500VoiceStatsLastInboundCallPacketCallingAddress_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 26, 1, 1, 38),
    _Cdx6500VoiceStatsLastInboundCallPacketCallingAddress_Type()
)
cdx6500VoiceStatsLastInboundCallPacketCallingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceStatsLastInboundCallPacketCallingAddress.setStatus("mandatory")


class _Cdx6500VoiceStatsLastInboundCallPacketFacilities_Type(DisplayString):
    """Custom type cdx6500VoiceStatsLastInboundCallPacketFacilities based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 105),
    )


_Cdx6500VoiceStatsLastInboundCallPacketFacilities_Type.__name__ = "DisplayString"
_Cdx6500VoiceStatsLastInboundCallPacketFacilities_Object = MibTableColumn
cdx6500VoiceStatsLastInboundCallPacketFacilities = _Cdx6500VoiceStatsLastInboundCallPacketFacilities_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 26, 1, 1, 39),
    _Cdx6500VoiceStatsLastInboundCallPacketFacilities_Type()
)
cdx6500VoiceStatsLastInboundCallPacketFacilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceStatsLastInboundCallPacketFacilities.setStatus("mandatory")


class _Cdx6500VoiceStatsLastInboundCallPacketCUD_Type(DisplayString):
    """Custom type cdx6500VoiceStatsLastInboundCallPacketCUD based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Cdx6500VoiceStatsLastInboundCallPacketCUD_Type.__name__ = "DisplayString"
_Cdx6500VoiceStatsLastInboundCallPacketCUD_Object = MibTableColumn
cdx6500VoiceStatsLastInboundCallPacketCUD = _Cdx6500VoiceStatsLastInboundCallPacketCUD_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 26, 1, 1, 40),
    _Cdx6500VoiceStatsLastInboundCallPacketCUD_Type()
)
cdx6500VoiceStatsLastInboundCallPacketCUD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceStatsLastInboundCallPacketCUD.setStatus("mandatory")


class _Cdx6500VoiceStatsLastOutboundCallPacketCalledAddress_Type(DisplayString):
    """Custom type cdx6500VoiceStatsLastOutboundCallPacketCalledAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 15),
    )


_Cdx6500VoiceStatsLastOutboundCallPacketCalledAddress_Type.__name__ = "DisplayString"
_Cdx6500VoiceStatsLastOutboundCallPacketCalledAddress_Object = MibTableColumn
cdx6500VoiceStatsLastOutboundCallPacketCalledAddress = _Cdx6500VoiceStatsLastOutboundCallPacketCalledAddress_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 26, 1, 1, 41),
    _Cdx6500VoiceStatsLastOutboundCallPacketCalledAddress_Type()
)
cdx6500VoiceStatsLastOutboundCallPacketCalledAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceStatsLastOutboundCallPacketCalledAddress.setStatus("mandatory")


class _Cdx6500VoiceStatsLastOutboundCallPacketCallingAddress_Type(DisplayString):
    """Custom type cdx6500VoiceStatsLastOutboundCallPacketCallingAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 15),
    )


_Cdx6500VoiceStatsLastOutboundCallPacketCallingAddress_Type.__name__ = "DisplayString"
_Cdx6500VoiceStatsLastOutboundCallPacketCallingAddress_Object = MibTableColumn
cdx6500VoiceStatsLastOutboundCallPacketCallingAddress = _Cdx6500VoiceStatsLastOutboundCallPacketCallingAddress_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 26, 1, 1, 42),
    _Cdx6500VoiceStatsLastOutboundCallPacketCallingAddress_Type()
)
cdx6500VoiceStatsLastOutboundCallPacketCallingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceStatsLastOutboundCallPacketCallingAddress.setStatus("mandatory")


class _Cdx6500VoiceStatsLastOutboundCallPacketFacilities_Type(DisplayString):
    """Custom type cdx6500VoiceStatsLastOutboundCallPacketFacilities based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 105),
    )


_Cdx6500VoiceStatsLastOutboundCallPacketFacilities_Type.__name__ = "DisplayString"
_Cdx6500VoiceStatsLastOutboundCallPacketFacilities_Object = MibTableColumn
cdx6500VoiceStatsLastOutboundCallPacketFacilities = _Cdx6500VoiceStatsLastOutboundCallPacketFacilities_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 26, 1, 1, 43),
    _Cdx6500VoiceStatsLastOutboundCallPacketFacilities_Type()
)
cdx6500VoiceStatsLastOutboundCallPacketFacilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceStatsLastOutboundCallPacketFacilities.setStatus("mandatory")


class _Cdx6500VoiceStatsLastOutboundCallPacketCUD_Type(DisplayString):
    """Custom type cdx6500VoiceStatsLastOutboundCallPacketCUD based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Cdx6500VoiceStatsLastOutboundCallPacketCUD_Type.__name__ = "DisplayString"
_Cdx6500VoiceStatsLastOutboundCallPacketCUD_Object = MibTableColumn
cdx6500VoiceStatsLastOutboundCallPacketCUD = _Cdx6500VoiceStatsLastOutboundCallPacketCUD_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 26, 1, 1, 44),
    _Cdx6500VoiceStatsLastOutboundCallPacketCUD_Type()
)
cdx6500VoiceStatsLastOutboundCallPacketCUD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceStatsLastOutboundCallPacketCUD.setStatus("mandatory")


class _Cdx6500VoiceStatsRingerStatus_Type(Integer32):
    """Custom type cdx6500VoiceStatsRingerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              100)
        )
    )
    namedValues = NamedValues(
        *(("na", 100),
          ("rs25Hz", 1),
          ("rs50Hz", 2))
    )


_Cdx6500VoiceStatsRingerStatus_Type.__name__ = "Integer32"
_Cdx6500VoiceStatsRingerStatus_Object = MibTableColumn
cdx6500VoiceStatsRingerStatus = _Cdx6500VoiceStatsRingerStatus_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 26, 1, 1, 45),
    _Cdx6500VoiceStatsRingerStatus_Type()
)
cdx6500VoiceStatsRingerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceStatsRingerStatus.setStatus("mandatory")


class _Cdx6500VoiceStatsDSPMSMSlotNumber_Type(Integer32):
    """Custom type cdx6500VoiceStatsDSPMSMSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_Cdx6500VoiceStatsDSPMSMSlotNumber_Type.__name__ = "Integer32"
_Cdx6500VoiceStatsDSPMSMSlotNumber_Object = MibTableColumn
cdx6500VoiceStatsDSPMSMSlotNumber = _Cdx6500VoiceStatsDSPMSMSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 26, 1, 1, 46),
    _Cdx6500VoiceStatsDSPMSMSlotNumber_Type()
)
cdx6500VoiceStatsDSPMSMSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceStatsDSPMSMSlotNumber.setStatus("mandatory")


class _Cdx6500VoiceStatsDSPMNumber_Type(Integer32):
    """Custom type cdx6500VoiceStatsDSPMNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_Cdx6500VoiceStatsDSPMNumber_Type.__name__ = "Integer32"
_Cdx6500VoiceStatsDSPMNumber_Object = MibTableColumn
cdx6500VoiceStatsDSPMNumber = _Cdx6500VoiceStatsDSPMNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 26, 1, 1, 47),
    _Cdx6500VoiceStatsDSPMNumber_Type()
)
cdx6500VoiceStatsDSPMNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceStatsDSPMNumber.setStatus("mandatory")
_Cdx6500VoiceStatsT1E1PortNumber_Type = Integer32
_Cdx6500VoiceStatsT1E1PortNumber_Object = MibTableColumn
cdx6500VoiceStatsT1E1PortNumber = _Cdx6500VoiceStatsT1E1PortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 26, 1, 1, 48),
    _Cdx6500VoiceStatsT1E1PortNumber_Type()
)
cdx6500VoiceStatsT1E1PortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceStatsT1E1PortNumber.setStatus("mandatory")
_Cdx6500VoiceStatsTimeSlotNumber_Type = DisplayString
_Cdx6500VoiceStatsTimeSlotNumber_Object = MibTableColumn
cdx6500VoiceStatsTimeSlotNumber = _Cdx6500VoiceStatsTimeSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 26, 1, 1, 49),
    _Cdx6500VoiceStatsTimeSlotNumber_Type()
)
cdx6500VoiceStatsTimeSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceStatsTimeSlotNumber.setStatus("mandatory")
_Cdx6500VoiceStatsDaughterCardRevAndPartNumber_Type = DisplayString
_Cdx6500VoiceStatsDaughterCardRevAndPartNumber_Object = MibTableColumn
cdx6500VoiceStatsDaughterCardRevAndPartNumber = _Cdx6500VoiceStatsDaughterCardRevAndPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 26, 1, 1, 50),
    _Cdx6500VoiceStatsDaughterCardRevAndPartNumber_Type()
)
cdx6500VoiceStatsDaughterCardRevAndPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceStatsDaughterCardRevAndPartNumber.setStatus("mandatory")
_Cdx6500VoiceStatsVADEfficiency_Type = Integer32
_Cdx6500VoiceStatsVADEfficiency_Object = MibTableColumn
cdx6500VoiceStatsVADEfficiency = _Cdx6500VoiceStatsVADEfficiency_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 26, 1, 1, 51),
    _Cdx6500VoiceStatsVADEfficiency_Type()
)
cdx6500VoiceStatsVADEfficiency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceStatsVADEfficiency.setStatus("mandatory")
_Cdx6500VoiceStatsMeanDelayDeviation_Type = Integer32
_Cdx6500VoiceStatsMeanDelayDeviation_Object = MibTableColumn
cdx6500VoiceStatsMeanDelayDeviation = _Cdx6500VoiceStatsMeanDelayDeviation_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 26, 1, 1, 52),
    _Cdx6500VoiceStatsMeanDelayDeviation_Type()
)
cdx6500VoiceStatsMeanDelayDeviation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceStatsMeanDelayDeviation.setStatus("mandatory")
_Cdx6500VoiceStatsMaxDelayDeviation_Type = DisplayString
_Cdx6500VoiceStatsMaxDelayDeviation_Object = MibTableColumn
cdx6500VoiceStatsMaxDelayDeviation = _Cdx6500VoiceStatsMaxDelayDeviation_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 26, 1, 1, 53),
    _Cdx6500VoiceStatsMaxDelayDeviation_Type()
)
cdx6500VoiceStatsMaxDelayDeviation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceStatsMaxDelayDeviation.setStatus("mandatory")
_Cdx6500VoiceStatsPktRecResync_Type = Integer32
_Cdx6500VoiceStatsPktRecResync_Object = MibTableColumn
cdx6500VoiceStatsPktRecResync = _Cdx6500VoiceStatsPktRecResync_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 26, 1, 1, 54),
    _Cdx6500VoiceStatsPktRecResync_Type()
)
cdx6500VoiceStatsPktRecResync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceStatsPktRecResync.setStatus("mandatory")
_Cdx6500VoiceCallStatsNoPacketDropped_Type = DisplayString
_Cdx6500VoiceCallStatsNoPacketDropped_Object = MibTableColumn
cdx6500VoiceCallStatsNoPacketDropped = _Cdx6500VoiceCallStatsNoPacketDropped_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 26, 1, 1, 55),
    _Cdx6500VoiceCallStatsNoPacketDropped_Type()
)
cdx6500VoiceCallStatsNoPacketDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCallStatsNoPacketDropped.setStatus("mandatory")
_Cdx6500VoiceCallStatsNoCallsDropped_Type = DisplayString
_Cdx6500VoiceCallStatsNoCallsDropped_Object = MibTableColumn
cdx6500VoiceCallStatsNoCallsDropped = _Cdx6500VoiceCallStatsNoCallsDropped_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 26, 1, 1, 56),
    _Cdx6500VoiceCallStatsNoCallsDropped_Type()
)
cdx6500VoiceCallStatsNoCallsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCallStatsNoCallsDropped.setStatus("mandatory")
_Cdx6500VoiceCallStatsDroppedReason0_Type = DisplayString
_Cdx6500VoiceCallStatsDroppedReason0_Object = MibTableColumn
cdx6500VoiceCallStatsDroppedReason0 = _Cdx6500VoiceCallStatsDroppedReason0_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 26, 1, 1, 57),
    _Cdx6500VoiceCallStatsDroppedReason0_Type()
)
cdx6500VoiceCallStatsDroppedReason0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCallStatsDroppedReason0.setStatus("mandatory")
_Cdx6500VoiceCallStatsDroppedReason1_Type = DisplayString
_Cdx6500VoiceCallStatsDroppedReason1_Object = MibTableColumn
cdx6500VoiceCallStatsDroppedReason1 = _Cdx6500VoiceCallStatsDroppedReason1_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 26, 1, 1, 58),
    _Cdx6500VoiceCallStatsDroppedReason1_Type()
)
cdx6500VoiceCallStatsDroppedReason1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCallStatsDroppedReason1.setStatus("mandatory")
_Cdx6500VoiceCallStatsDroppedReason3_Type = DisplayString
_Cdx6500VoiceCallStatsDroppedReason3_Object = MibTableColumn
cdx6500VoiceCallStatsDroppedReason3 = _Cdx6500VoiceCallStatsDroppedReason3_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 26, 1, 1, 59),
    _Cdx6500VoiceCallStatsDroppedReason3_Type()
)
cdx6500VoiceCallStatsDroppedReason3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCallStatsDroppedReason3.setStatus("mandatory")
_Cdx6500VoiceCallStatsDroppedReason5_Type = DisplayString
_Cdx6500VoiceCallStatsDroppedReason5_Object = MibTableColumn
cdx6500VoiceCallStatsDroppedReason5 = _Cdx6500VoiceCallStatsDroppedReason5_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 26, 1, 1, 60),
    _Cdx6500VoiceCallStatsDroppedReason5_Type()
)
cdx6500VoiceCallStatsDroppedReason5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCallStatsDroppedReason5.setStatus("mandatory")
_Cdx6500VoiceCallStatsDroppedReason9_Type = DisplayString
_Cdx6500VoiceCallStatsDroppedReason9_Object = MibTableColumn
cdx6500VoiceCallStatsDroppedReason9 = _Cdx6500VoiceCallStatsDroppedReason9_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 26, 1, 1, 61),
    _Cdx6500VoiceCallStatsDroppedReason9_Type()
)
cdx6500VoiceCallStatsDroppedReason9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCallStatsDroppedReason9.setStatus("mandatory")
_Cdx6500VoiceCallStatsDroppedReason11_Type = DisplayString
_Cdx6500VoiceCallStatsDroppedReason11_Object = MibTableColumn
cdx6500VoiceCallStatsDroppedReason11 = _Cdx6500VoiceCallStatsDroppedReason11_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 26, 1, 1, 62),
    _Cdx6500VoiceCallStatsDroppedReason11_Type()
)
cdx6500VoiceCallStatsDroppedReason11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCallStatsDroppedReason11.setStatus("mandatory")
_Cdx6500VoiceCallStatsDroppedReason13_Type = DisplayString
_Cdx6500VoiceCallStatsDroppedReason13_Object = MibTableColumn
cdx6500VoiceCallStatsDroppedReason13 = _Cdx6500VoiceCallStatsDroppedReason13_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 26, 1, 1, 63),
    _Cdx6500VoiceCallStatsDroppedReason13_Type()
)
cdx6500VoiceCallStatsDroppedReason13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCallStatsDroppedReason13.setStatus("mandatory")
_Cdx6500VoiceCallStatsDroppedReason17_Type = DisplayString
_Cdx6500VoiceCallStatsDroppedReason17_Object = MibTableColumn
cdx6500VoiceCallStatsDroppedReason17 = _Cdx6500VoiceCallStatsDroppedReason17_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 26, 1, 1, 64),
    _Cdx6500VoiceCallStatsDroppedReason17_Type()
)
cdx6500VoiceCallStatsDroppedReason17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCallStatsDroppedReason17.setStatus("mandatory")
_Cdx6500VoiceCallStatsDroppedReason19_Type = DisplayString
_Cdx6500VoiceCallStatsDroppedReason19_Object = MibTableColumn
cdx6500VoiceCallStatsDroppedReason19 = _Cdx6500VoiceCallStatsDroppedReason19_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 26, 1, 1, 65),
    _Cdx6500VoiceCallStatsDroppedReason19_Type()
)
cdx6500VoiceCallStatsDroppedReason19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCallStatsDroppedReason19.setStatus("mandatory")
_Cdx6500VoiceCallStatsDroppedReason21_Type = DisplayString
_Cdx6500VoiceCallStatsDroppedReason21_Object = MibTableColumn
cdx6500VoiceCallStatsDroppedReason21 = _Cdx6500VoiceCallStatsDroppedReason21_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 26, 1, 1, 66),
    _Cdx6500VoiceCallStatsDroppedReason21_Type()
)
cdx6500VoiceCallStatsDroppedReason21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCallStatsDroppedReason21.setStatus("mandatory")
_Cdx6500VoiceCallStatsDroppedReason33_Type = DisplayString
_Cdx6500VoiceCallStatsDroppedReason33_Object = MibTableColumn
cdx6500VoiceCallStatsDroppedReason33 = _Cdx6500VoiceCallStatsDroppedReason33_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 26, 1, 1, 67),
    _Cdx6500VoiceCallStatsDroppedReason33_Type()
)
cdx6500VoiceCallStatsDroppedReason33.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCallStatsDroppedReason33.setStatus("mandatory")
_Cdx6500VoiceCallStatsDroppedReason_Rest_Type = DisplayString
_Cdx6500VoiceCallStatsDroppedReason_Rest_Object = MibScalar
cdx6500VoiceCallStatsDroppedReason_Rest = _Cdx6500VoiceCallStatsDroppedReason_Rest_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 26, 1, 1, 68),
    _Cdx6500VoiceCallStatsDroppedReason_Rest_Type()
)
cdx6500VoiceCallStatsDroppedReason_Rest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500VoiceCallStatsDroppedReason_Rest.setStatus("mandatory")
_Cdx6500PPSTSignalingSequenceTrapTable_Object = MibTable
cdx6500PPSTSignalingSequenceTrapTable = _Cdx6500PPSTSignalingSequenceTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 26, 2)
)
if mibBuilder.loadTexts:
    cdx6500PPSTSignalingSequenceTrapTable.setStatus("mandatory")
_Cdx6500PPSTSignalingSequenceTrapEntry_Object = MibTableRow
cdx6500PPSTSignalingSequenceTrapEntry = _Cdx6500PPSTSignalingSequenceTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 26, 2, 1)
)
cdx6500PPSTSignalingSequenceTrapEntry.setIndexNames(
    (0, "VOICE-OPT-MIB", "cdx6500SignalingSequenceTrapPortNumber"),
    (0, "VOICE-OPT-MIB", "cdx6500SignalingSequenceTrapEventNumber"),
)
if mibBuilder.loadTexts:
    cdx6500PPSTSignalingSequenceTrapEntry.setStatus("mandatory")
_Cdx6500SignalingSequenceTrapPortNumber_Type = Integer32
_Cdx6500SignalingSequenceTrapPortNumber_Object = MibTableColumn
cdx6500SignalingSequenceTrapPortNumber = _Cdx6500SignalingSequenceTrapPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 26, 2, 1, 1),
    _Cdx6500SignalingSequenceTrapPortNumber_Type()
)
cdx6500SignalingSequenceTrapPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SignalingSequenceTrapPortNumber.setStatus("mandatory")


class _Cdx6500SignalingSequenceTrapEventNumber_Type(Integer32):
    """Custom type cdx6500SignalingSequenceTrapEventNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Cdx6500SignalingSequenceTrapEventNumber_Type.__name__ = "Integer32"
_Cdx6500SignalingSequenceTrapEventNumber_Object = MibTableColumn
cdx6500SignalingSequenceTrapEventNumber = _Cdx6500SignalingSequenceTrapEventNumber_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 26, 2, 1, 2),
    _Cdx6500SignalingSequenceTrapEventNumber_Type()
)
cdx6500SignalingSequenceTrapEventNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SignalingSequenceTrapEventNumber.setStatus("mandatory")
_Cdx6500SignalingSequenceTrapTxState_Type = DisplayString
_Cdx6500SignalingSequenceTrapTxState_Object = MibTableColumn
cdx6500SignalingSequenceTrapTxState = _Cdx6500SignalingSequenceTrapTxState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 26, 2, 1, 3),
    _Cdx6500SignalingSequenceTrapTxState_Type()
)
cdx6500SignalingSequenceTrapTxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SignalingSequenceTrapTxState.setStatus("mandatory")
_Cdx6500SignalingSequenceTrapRxState_Type = DisplayString
_Cdx6500SignalingSequenceTrapRxState_Object = MibTableColumn
cdx6500SignalingSequenceTrapRxState = _Cdx6500SignalingSequenceTrapRxState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 26, 2, 1, 4),
    _Cdx6500SignalingSequenceTrapRxState_Type()
)
cdx6500SignalingSequenceTrapRxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SignalingSequenceTrapRxState.setStatus("mandatory")


class _Cdx6500SignalingSequenceTrapMachineState_Type(DisplayString):
    """Custom type cdx6500SignalingSequenceTrapMachineState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 11),
    )


_Cdx6500SignalingSequenceTrapMachineState_Type.__name__ = "DisplayString"
_Cdx6500SignalingSequenceTrapMachineState_Object = MibTableColumn
cdx6500SignalingSequenceTrapMachineState = _Cdx6500SignalingSequenceTrapMachineState_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 26, 2, 1, 5),
    _Cdx6500SignalingSequenceTrapMachineState_Type()
)
cdx6500SignalingSequenceTrapMachineState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SignalingSequenceTrapMachineState.setStatus("mandatory")
_Cdx6500SignalingSequenceTrapTimeSinceLastChange_Type = Integer32
_Cdx6500SignalingSequenceTrapTimeSinceLastChange_Object = MibTableColumn
cdx6500SignalingSequenceTrapTimeSinceLastChange = _Cdx6500SignalingSequenceTrapTimeSinceLastChange_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 26, 2, 1, 6),
    _Cdx6500SignalingSequenceTrapTimeSinceLastChange_Type()
)
cdx6500SignalingSequenceTrapTimeSinceLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SignalingSequenceTrapTimeSinceLastChange.setStatus("mandatory")


class _Cdx6500SignalingSequenceTrapComment_Type(DisplayString):
    """Custom type cdx6500SignalingSequenceTrapComment based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Cdx6500SignalingSequenceTrapComment_Type.__name__ = "DisplayString"
_Cdx6500SignalingSequenceTrapComment_Object = MibTableColumn
cdx6500SignalingSequenceTrapComment = _Cdx6500SignalingSequenceTrapComment_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 1, 1, 26, 2, 1, 7),
    _Cdx6500SignalingSequenceTrapComment_Type()
)
cdx6500SignalingSequenceTrapComment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500SignalingSequenceTrapComment.setStatus("mandatory")
_Cdx6500StatNetworkSvcsGroup_ObjectIdentity = ObjectIdentity
cdx6500StatNetworkSvcsGroup = _Cdx6500StatNetworkSvcsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 4)
)
_Cdx6500StatVCSTable_Object = MibTable
cdx6500StatVCSTable = _Cdx6500StatVCSTable_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 4, 4)
)
if mibBuilder.loadTexts:
    cdx6500StatVCSTable.setStatus("mandatory")
_Cdx6500StatVCSEntry_Object = MibTableRow
cdx6500StatVCSEntry = _Cdx6500StatVCSEntry_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 4, 4, 1)
)
cdx6500StatVCSEntry.setIndexNames(
    (0, "VOICE-OPT-MIB", "cdx6500StatVCSIndex"),
)
if mibBuilder.loadTexts:
    cdx6500StatVCSEntry.setStatus("mandatory")
_Cdx6500StatVCSIndex_Type = Integer32
_Cdx6500StatVCSIndex_Object = MibTableColumn
cdx6500StatVCSIndex = _Cdx6500StatVCSIndex_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 4, 4, 1, 1),
    _Cdx6500StatVCSIndex_Type()
)
cdx6500StatVCSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500StatVCSIndex.setStatus("mandatory")
_Cdx6500StatVCSTime_Type = DisplayString
_Cdx6500StatVCSTime_Object = MibTableColumn
cdx6500StatVCSTime = _Cdx6500StatVCSTime_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 4, 4, 1, 2),
    _Cdx6500StatVCSTime_Type()
)
cdx6500StatVCSTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500StatVCSTime.setStatus("mandatory")
_Cdx6500StatVCSNoPacketDropped_Type = Integer32
_Cdx6500StatVCSNoPacketDropped_Object = MibTableColumn
cdx6500StatVCSNoPacketDropped = _Cdx6500StatVCSNoPacketDropped_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 4, 4, 1, 3),
    _Cdx6500StatVCSNoPacketDropped_Type()
)
cdx6500StatVCSNoPacketDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500StatVCSNoPacketDropped.setStatus("mandatory")
_Cdx6500StatVCSNoCallsDropped_Type = Integer32
_Cdx6500StatVCSNoCallsDropped_Object = MibTableColumn
cdx6500StatVCSNoCallsDropped = _Cdx6500StatVCSNoCallsDropped_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 4, 4, 1, 4),
    _Cdx6500StatVCSNoCallsDropped_Type()
)
cdx6500StatVCSNoCallsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500StatVCSNoCallsDropped.setStatus("mandatory")
_Cdx6500StatVCSDroppedReasons_Type = DisplayString
_Cdx6500StatVCSDroppedReasons_Object = MibTableColumn
cdx6500StatVCSDroppedReasons = _Cdx6500StatVCSDroppedReasons_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 4, 4, 1, 5),
    _Cdx6500StatVCSDroppedReasons_Type()
)
cdx6500StatVCSDroppedReasons.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500StatVCSDroppedReasons.setStatus("mandatory")
_Cdx6500StatVCSNoCallsProcessed_Type = Integer32
_Cdx6500StatVCSNoCallsProcessed_Object = MibTableColumn
cdx6500StatVCSNoCallsProcessed = _Cdx6500StatVCSNoCallsProcessed_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 4, 4, 1, 6),
    _Cdx6500StatVCSNoCallsProcessed_Type()
)
cdx6500StatVCSNoCallsProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500StatVCSNoCallsProcessed.setStatus("mandatory")
_Cdx6500StatVCSPercentPeakAvgCurOfCPULoad_Type = DisplayString
_Cdx6500StatVCSPercentPeakAvgCurOfCPULoad_Object = MibTableColumn
cdx6500StatVCSPercentPeakAvgCurOfCPULoad = _Cdx6500StatVCSPercentPeakAvgCurOfCPULoad_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 4, 4, 1, 7),
    _Cdx6500StatVCSPercentPeakAvgCurOfCPULoad_Type()
)
cdx6500StatVCSPercentPeakAvgCurOfCPULoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500StatVCSPercentPeakAvgCurOfCPULoad.setStatus("mandatory")
_Cdx6500StatVCSPercentPeakAvgCurOfDataBuf_Type = DisplayString
_Cdx6500StatVCSPercentPeakAvgCurOfDataBuf_Object = MibTableColumn
cdx6500StatVCSPercentPeakAvgCurOfDataBuf = _Cdx6500StatVCSPercentPeakAvgCurOfDataBuf_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 4, 4, 1, 8),
    _Cdx6500StatVCSPercentPeakAvgCurOfDataBuf_Type()
)
cdx6500StatVCSPercentPeakAvgCurOfDataBuf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500StatVCSPercentPeakAvgCurOfDataBuf.setStatus("mandatory")
_Cdx6500StatVCSPercentPeakAvgCurOfIORBBuf_Type = DisplayString
_Cdx6500StatVCSPercentPeakAvgCurOfIORBBuf_Object = MibTableColumn
cdx6500StatVCSPercentPeakAvgCurOfIORBBuf = _Cdx6500StatVCSPercentPeakAvgCurOfIORBBuf_Object(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 3, 4, 4, 1, 9),
    _Cdx6500StatVCSPercentPeakAvgCurOfIORBBuf_Type()
)
cdx6500StatVCSPercentPeakAvgCurOfIORBBuf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cdx6500StatVCSPercentPeakAvgCurOfIORBBuf.setStatus("mandatory")
_Cdx6500Controls_ObjectIdentity = ObjectIdentity
cdx6500Controls = _Cdx6500Controls_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 449, 2, 1, 4)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VOICE-OPT-MIB",
    **{"DisplayString": DisplayString,
       "PhysicalPortNumber": PhysicalPortNumber,
       "codex": codex,
       "cdxProductSpecific": cdxProductSpecific,
       "cdx6500": cdx6500,
       "cdx6500Configuration": cdx6500Configuration,
       "cdx6500CfgProtocolGroup": cdx6500CfgProtocolGroup,
       "cdx6500PCTPortProtocolGroup": cdx6500PCTPortProtocolGroup,
       "cdx6500PCTVoicePortTable": cdx6500PCTVoicePortTable,
       "cdx6500PPCTVoicePortTable": cdx6500PPCTVoicePortTable,
       "cdx6500PPCTVoicePortEntry": cdx6500PPCTVoicePortEntry,
       "cdx6500VoiceCfgPortNumber": cdx6500VoiceCfgPortNumber,
       "cdx6500VoiceCfgPortType": cdx6500VoiceCfgPortType,
       "cdx6500VoiceCfgInterfaceType": cdx6500VoiceCfgInterfaceType,
       "cdx6500VoiceCfgSignalingType": cdx6500VoiceCfgSignalingType,
       "cdx6500VoiceCfgELeadFilter": cdx6500VoiceCfgELeadFilter,
       "cdx6500VoiceCfgHybridFXS": cdx6500VoiceCfgHybridFXS,
       "cdx6500VoiceCfgHybridEAndM2": cdx6500VoiceCfgHybridEAndM2,
       "cdx6500VoiceCfgSignalingMode": cdx6500VoiceCfgSignalingMode,
       "cdx6500VoiceCfgSignalingControl": cdx6500VoiceCfgSignalingControl,
       "cdx6500VoiceCfgNoOfDigitsToCollect": cdx6500VoiceCfgNoOfDigitsToCollect,
       "cdx6500VoiceCfgNoOfRings": cdx6500VoiceCfgNoOfRings,
       "cdx6500VoiceCfgPCMMode": cdx6500VoiceCfgPCMMode,
       "cdx6500VoiceCfgCompressionRate": cdx6500VoiceCfgCompressionRate,
       "cdx6500VoiceCfgDSIControl": cdx6500VoiceCfgDSIControl,
       "cdx6500VoiceCfgSmoothingDelay": cdx6500VoiceCfgSmoothingDelay,
       "cdx6500VoiceCfgEchoControl": cdx6500VoiceCfgEchoControl,
       "cdx6500VoiceCfgEchoReturnLoss": cdx6500VoiceCfgEchoReturnLoss,
       "cdx6500VoiceCfgTxInputSignalLevel": cdx6500VoiceCfgTxInputSignalLevel,
       "cdx6500VoiceCfgRxOutputSignalLevel": cdx6500VoiceCfgRxOutputSignalLevel,
       "cdx6500VoiceCfgFaxSupport": cdx6500VoiceCfgFaxSupport,
       "cdx6500VoiceCfgFaxRates": cdx6500VoiceCfgFaxRates,
       "cdx6500VoiceCfgVoiceBandDetection": cdx6500VoiceCfgVoiceBandDetection,
       "cdx6500VoiceCfgAutoCallMnemonic": cdx6500VoiceCfgAutoCallMnemonic,
       "cdx6500VoiceCfgCallControl": cdx6500VoiceCfgCallControl,
       "cdx6500VoiceCfgAutoCallTimeout": cdx6500VoiceCfgAutoCallTimeout,
       "cdx6500VoiceCfgCallRetries": cdx6500VoiceCfgCallRetries,
       "cdx6500VoiceCfgGroupSubaddress": cdx6500VoiceCfgGroupSubaddress,
       "cdx6500VoiceCfgBilling": cdx6500VoiceCfgBilling,
       "cdx6500VoiceCfgRxSignalingStateChangeFilter": cdx6500VoiceCfgRxSignalingStateChangeFilter,
       "cdx6500VoiceCfgT1E1RxIdleOnhookState": cdx6500VoiceCfgT1E1RxIdleOnhookState,
       "cdx6500VoiceCfgT1E1TxIdleOnhookState": cdx6500VoiceCfgT1E1TxIdleOnhookState,
       "cdx6500VoiceCfgT1E1RxActiveOffhookState": cdx6500VoiceCfgT1E1RxActiveOffhookState,
       "cdx6500VoiceCfgT1E1TxActiveOffhookState": cdx6500VoiceCfgT1E1TxActiveOffhookState,
       "cdx6500VoiceCfgT1E1RingingState": cdx6500VoiceCfgT1E1RingingState,
       "cdx6500VoiceCfgT1E1NoRingingState": cdx6500VoiceCfgT1E1NoRingingState,
       "cdx6500VoiceCfgRxWinkStartTimer": cdx6500VoiceCfgRxWinkStartTimer,
       "cdx6500VoiceCfgRxMinimumReceiveWink": cdx6500VoiceCfgRxMinimumReceiveWink,
       "cdx6500VoiceCfgRxCalledEndGlareDetect": cdx6500VoiceCfgRxCalledEndGlareDetect,
       "cdx6500VoiceCfgRxFirstDigitTimer": cdx6500VoiceCfgRxFirstDigitTimer,
       "cdx6500VoiceCfgRxInterdigitTimer": cdx6500VoiceCfgRxInterdigitTimer,
       "cdx6500VoiceCfgTxWinkDelay": cdx6500VoiceCfgTxWinkDelay,
       "cdx6500VoiceCfgTxWinkWidth": cdx6500VoiceCfgTxWinkWidth,
       "cdx6500VoiceCfgTxDigitDelay": cdx6500VoiceCfgTxDigitDelay,
       "cdx6500VoiceCfgTxDigitOn": cdx6500VoiceCfgTxDigitOn,
       "cdx6500VoiceCfgTxInterdigitTime": cdx6500VoiceCfgTxInterdigitTime,
       "cdx6500VoiceCfgRxInterringWait": cdx6500VoiceCfgRxInterringWait,
       "cdx6500VoiceCfgRxRingStateChangeFilter": cdx6500VoiceCfgRxRingStateChangeFilter,
       "cdx6500VoiceCfgTxRingerOffLong": cdx6500VoiceCfgTxRingerOffLong,
       "cdx6500VoiceCfgTxRingerOffShort": cdx6500VoiceCfgTxRingerOffShort,
       "cdx6500VoiceCfgTxRingerOn": cdx6500VoiceCfgTxRingerOn,
       "cdx6500VoiceCfgRxDisconnectTimer": cdx6500VoiceCfgRxDisconnectTimer,
       "cdx6500VoiceCfgRxCalledEndDisconnectDelayTimer": cdx6500VoiceCfgRxCalledEndDisconnectDelayTimer,
       "cdx6500VoiceCfgLineErrorRecovery": cdx6500VoiceCfgLineErrorRecovery,
       "cdx6500VoiceCfgSignalingSampleRate": cdx6500VoiceCfgSignalingSampleRate,
       "cdx6500VoiceCfgWaitForParams": cdx6500VoiceCfgWaitForParams,
       "cdx6500VoiceCfgSpareTimer1": cdx6500VoiceCfgSpareTimer1,
       "cdx6500VoiceCfgSpareTimer2": cdx6500VoiceCfgSpareTimer2,
       "cdx6500VoiceCfgTxInterdigitPauseTime": cdx6500VoiceCfgTxInterdigitPauseTime,
       "cdx6500VoiceCfgRxMinimumFlashHookTime": cdx6500VoiceCfgRxMinimumFlashHookTime,
       "cdx6500VoiceCfgRxMaximumFlashHookTime": cdx6500VoiceCfgRxMaximumFlashHookTime,
       "cdx6500VoiceCfgTransparentSignalingIdleState": cdx6500VoiceCfgTransparentSignalingIdleState,
       "cdx6500VoiceCfgTransparentRxDisconnectFilter": cdx6500VoiceCfgTransparentRxDisconnectFilter,
       "cdx6500VoiceCfgTransparentSignalingBusyoutState": cdx6500VoiceCfgTransparentSignalingBusyoutState,
       "cdx6500VoiceCfgXlateSigInfo0000FromRemoteToLocalPort": cdx6500VoiceCfgXlateSigInfo0000FromRemoteToLocalPort,
       "cdx6500VoiceCfgXlateSigInfo1000FromRemoteToLocalPort": cdx6500VoiceCfgXlateSigInfo1000FromRemoteToLocalPort,
       "cdx6500VoiceCfgXlateSigInfo0100FromRemoteToLocalPort": cdx6500VoiceCfgXlateSigInfo0100FromRemoteToLocalPort,
       "cdx6500VoiceCfgXlateSigInfo1100FromRemoteToLocalPort": cdx6500VoiceCfgXlateSigInfo1100FromRemoteToLocalPort,
       "cdx6500VoiceCfgXlateSigInfo0010FromRemoteToLocalPort": cdx6500VoiceCfgXlateSigInfo0010FromRemoteToLocalPort,
       "cdx6500VoiceCfgXlateSigInfo1010FromRemoteToLocalPort": cdx6500VoiceCfgXlateSigInfo1010FromRemoteToLocalPort,
       "cdx6500VoiceCfgXlateSigInfo0110FromRemoteToLocalPort": cdx6500VoiceCfgXlateSigInfo0110FromRemoteToLocalPort,
       "cdx6500VoiceCfgXlateSigInfo1110FromRemoteToLocalPort": cdx6500VoiceCfgXlateSigInfo1110FromRemoteToLocalPort,
       "cdx6500VoiceCfgXlateSigInfo0001FromRemoteToLocalPort": cdx6500VoiceCfgXlateSigInfo0001FromRemoteToLocalPort,
       "cdx6500VoiceCfgXlateSigInfo1001FromRemoteToLocalPort": cdx6500VoiceCfgXlateSigInfo1001FromRemoteToLocalPort,
       "cdx6500VoiceCfgXlateSigInfo0101FromRemoteToLocalPort": cdx6500VoiceCfgXlateSigInfo0101FromRemoteToLocalPort,
       "cdx6500VoiceCfgXlateSigInfo1101FromRemoteToLocalPort": cdx6500VoiceCfgXlateSigInfo1101FromRemoteToLocalPort,
       "cdx6500VoiceCfgXlateSigInfo0011FromRemoteToLocalPort": cdx6500VoiceCfgXlateSigInfo0011FromRemoteToLocalPort,
       "cdx6500VoiceCfgXlateSigInfo1011FromRemoteToLocalPort": cdx6500VoiceCfgXlateSigInfo1011FromRemoteToLocalPort,
       "cdx6500VoiceCfgXlateSigInfo0111FromRemoteToLocalPort": cdx6500VoiceCfgXlateSigInfo0111FromRemoteToLocalPort,
       "cdx6500VoiceCfgXlateSigInfo1111FromRemoteToLocalPort": cdx6500VoiceCfgXlateSigInfo1111FromRemoteToLocalPort,
       "cdx6500VoiceCfgDialToneLowerFrequency": cdx6500VoiceCfgDialToneLowerFrequency,
       "cdx6500VoiceCfgDialToneLowerFrequencyAmplitude": cdx6500VoiceCfgDialToneLowerFrequencyAmplitude,
       "cdx6500VoiceCfgDialToneUpperFrequency": cdx6500VoiceCfgDialToneUpperFrequency,
       "cdx6500VoiceCfgDialToneUpperFrequencyAmplitude": cdx6500VoiceCfgDialToneUpperFrequencyAmplitude,
       "cdx6500VoiceCfgRingBackToneLowerFrequency": cdx6500VoiceCfgRingBackToneLowerFrequency,
       "cdx6500VoiceCfgRingBackToneLowerFrequencyAmplitude": cdx6500VoiceCfgRingBackToneLowerFrequencyAmplitude,
       "cdx6500VoiceCfgRingBackToneUpperFrequency": cdx6500VoiceCfgRingBackToneUpperFrequency,
       "cdx6500VoiceCfgRingBackToneUpperFrequencyAmplitude": cdx6500VoiceCfgRingBackToneUpperFrequencyAmplitude,
       "cdx6500VoiceCfgBusyToneLowerFrequency": cdx6500VoiceCfgBusyToneLowerFrequency,
       "cdx6500VoiceCfgBusyToneLowerFrequencyAmplitude": cdx6500VoiceCfgBusyToneLowerFrequencyAmplitude,
       "cdx6500VoiceCfgBusyToneUpperFrequency": cdx6500VoiceCfgBusyToneUpperFrequency,
       "cdx6500VoiceCfgBusyToneUpperFrequencyAmplitude": cdx6500VoiceCfgBusyToneUpperFrequencyAmplitude,
       "cdx6500VoiceCfgTxBusyToneOffTime": cdx6500VoiceCfgTxBusyToneOffTime,
       "cdx6500VoiceCfgTxBusyToneOnTime": cdx6500VoiceCfgTxBusyToneOnTime,
       "cdx6500VoiceCfgFastBusyToneLowerFrequency": cdx6500VoiceCfgFastBusyToneLowerFrequency,
       "cdx6500VoiceCfgFastBusyToneLowerFrequencyAmplitude": cdx6500VoiceCfgFastBusyToneLowerFrequencyAmplitude,
       "cdx6500VoiceCfgFastBusyToneUpperFrequency": cdx6500VoiceCfgFastBusyToneUpperFrequency,
       "cdx6500VoiceCfgFastBusyToneUpperFrequencyAmplitude": cdx6500VoiceCfgFastBusyToneUpperFrequencyAmplitude,
       "cdx6500VoiceCfgTxFastBusyToneOffTime": cdx6500VoiceCfgTxFastBusyToneOffTime,
       "cdx6500VoiceCfgTxFastBusyToneOnTime": cdx6500VoiceCfgTxFastBusyToneOnTime,
       "cdx6500VoiceCfgHybridFXO": cdx6500VoiceCfgHybridFXO,
       "cdx6500VoiceCfgTxPulse": cdx6500VoiceCfgTxPulse,
       "cdx6500VoiceCfgRxMinPulse": cdx6500VoiceCfgRxMinPulse,
       "cdx6500VoiceCfgRxMaxPulse": cdx6500VoiceCfgRxMaxPulse,
       "cdx6500VoiceCfgTxMasterClear": cdx6500VoiceCfgTxMasterClear,
       "cdx6500VoiceCfgRxMinMasterClear": cdx6500VoiceCfgRxMinMasterClear,
       "cdx6500VoiceCfgRxMaxMasterClear": cdx6500VoiceCfgRxMaxMasterClear,
       "cdx6500VoiceCfgTxSlaveClear": cdx6500VoiceCfgTxSlaveClear,
       "cdx6500VoiceCfgRxMinSlaveClear": cdx6500VoiceCfgRxMinSlaveClear,
       "cdx6500VoiceCfgRxMaxSlaveClear": cdx6500VoiceCfgRxMaxSlaveClear,
       "cdx6500VoiceCfgTxSlaveRelease": cdx6500VoiceCfgTxSlaveRelease,
       "cdx6500VoiceCfgRxMinSlaveRelease": cdx6500VoiceCfgRxMinSlaveRelease,
       "cdx6500VoiceCfgRxMaxSlaveRelease": cdx6500VoiceCfgRxMaxSlaveRelease,
       "cdx6500VoiceCfgTxPTSTime": cdx6500VoiceCfgTxPTSTime,
       "cdx6500VoiceCfgRxPTSTime": cdx6500VoiceCfgRxPTSTime,
       "cdx6500VoiceCfgMasterGuard": cdx6500VoiceCfgMasterGuard,
       "cdx6500VoiceCfgSlaveGuard": cdx6500VoiceCfgSlaveGuard,
       "cdx6500VoiceCfgTxFlashHookTime": cdx6500VoiceCfgTxFlashHookTime,
       "cdx6500VoiceCfgDtmfAmplitude": cdx6500VoiceCfgDtmfAmplitude,
       "cdx6500VoiceCfgFXSOffhookFilter": cdx6500VoiceCfgFXSOffhookFilter,
       "cdx6500CfgGeneralGroup": cdx6500CfgGeneralGroup,
       "cdx6500GCTVoiceSwitchTable": cdx6500GCTVoiceSwitchTable,
       "cdx6500GGCTVoiceSwitchTable": cdx6500GGCTVoiceSwitchTable,
       "cdx6500VoiceSwitchEntry": cdx6500VoiceSwitchEntry,
       "cdx6500VoiceSwitchRxDTMFDigitString": cdx6500VoiceSwitchRxDTMFDigitString,
       "cdx6500VoiceSwitchNumRxDigitToReceive": cdx6500VoiceSwitchNumRxDigitToReceive,
       "cdx6500VoiceSwitchCallParam": cdx6500VoiceSwitchCallParam,
       "cdx6500VoiceSwitchAlternateDestination": cdx6500VoiceSwitchAlternateDestination,
       "cdx6500VoiceSwitchCompressionOverrideRate": cdx6500VoiceSwitchCompressionOverrideRate,
       "cdx6500VoiceSwitchNumLeadingDigitToStrip": cdx6500VoiceSwitchNumLeadingDigitToStrip,
       "cdx6500VoiceSwitchPreFixDigits": cdx6500VoiceSwitchPreFixDigits,
       "cdx6500VoiceSwitchPostFixDigits": cdx6500VoiceSwitchPostFixDigits,
       "cdx6500VoiceSwitchEntryNumber": cdx6500VoiceSwitchEntryNumber,
       "cdx6500Statistics": cdx6500Statistics,
       "cdx6500StatProtocolGroup": cdx6500StatProtocolGroup,
       "cdx6500PSTPortProtocolGroup": cdx6500PSTPortProtocolGroup,
       "cdx6500PSTVoicePortTable": cdx6500PSTVoicePortTable,
       "cdx6500PPSTVoicePortTable": cdx6500PPSTVoicePortTable,
       "cdx6500PPSTVoicePortEntry": cdx6500PPSTVoicePortEntry,
       "cdx6500VoiceStatsPortNumber": cdx6500VoiceStatsPortNumber,
       "cdx6500VoiceStatsPortInterfaceType": cdx6500VoiceStatsPortInterfaceType,
       "cdx6500VoiceStatsHWRevAndPartNumber": cdx6500VoiceStatsHWRevAndPartNumber,
       "cdx6500VoiceStatsFortyEightVolts": cdx6500VoiceStatsFortyEightVolts,
       "cdx6500VoiceStatsPortState": cdx6500VoiceStatsPortState,
       "cdx6500VoiceStatsCircuitState": cdx6500VoiceStatsCircuitState,
       "cdx6500VoiceStatsCurrentMode": cdx6500VoiceStatsCurrentMode,
       "cdx6500VoiceStatsTimeOfLastStatReset": cdx6500VoiceStatsTimeOfLastStatReset,
       "cdx6500VoiceStatsCallDuration": cdx6500VoiceStatsCallDuration,
       "cdx6500VoiceStatsTotalCallDuration": cdx6500VoiceStatsTotalCallDuration,
       "cdx6500VoiceStatsPortUtilization": cdx6500VoiceStatsPortUtilization,
       "cdx6500VoiceStatsNumberOfCalls": cdx6500VoiceStatsNumberOfCalls,
       "cdx6500VoiceStatsLastDigitsTransmitted": cdx6500VoiceStatsLastDigitsTransmitted,
       "cdx6500VoiceStatsLastDigitsReceived": cdx6500VoiceStatsLastDigitsReceived,
       "cdx6500VoiceStatsTxPacketDropped": cdx6500VoiceStatsTxPacketDropped,
       "cdx6500VoiceStatsRxPacketDropped": cdx6500VoiceStatsRxPacketDropped,
       "cdx6500VoiceStatsDroppedPackets": cdx6500VoiceStatsDroppedPackets,
       "cdx6500VoiceStatsDSPInternalFaults": cdx6500VoiceStatsDSPInternalFaults,
       "cdx6500VoiceStatsTxPackets": cdx6500VoiceStatsTxPackets,
       "cdx6500VoiceStatsRxPackets": cdx6500VoiceStatsRxPackets,
       "cdx6500VoiceStatsTxPacketsPerSecond": cdx6500VoiceStatsTxPacketsPerSecond,
       "cdx6500VoiceStatsRxPacketsPerSecond": cdx6500VoiceStatsRxPacketsPerSecond,
       "cdx6500VoiceStatsDSIEfficiency": cdx6500VoiceStatsDSIEfficiency,
       "cdx6500VoiceStatsCurrentRate": cdx6500VoiceStatsCurrentRate,
       "cdx6500VoiceStatsInputPower": cdx6500VoiceStatsInputPower,
       "cdx6500VoiceStatsOutputPower": cdx6500VoiceStatsOutputPower,
       "cdx6500VoiceStatsFAXTransmissions": cdx6500VoiceStatsFAXTransmissions,
       "cdx6500VoiceStatsUnsupportedFmtsFAXXmissions": cdx6500VoiceStatsUnsupportedFmtsFAXXmissions,
       "cdx6500PPSTSignalingSequenceTrapTxState": cdx6500PPSTSignalingSequenceTrapTxState,
       "cdx6500PPSTSignalingSequenceTrapRxState": cdx6500PPSTSignalingSequenceTrapRxState,
       "cdx6500PPSTSignalingSequenceTrapMachineState": cdx6500PPSTSignalingSequenceTrapMachineState,
       "cdx6500PPSTSignalingSequenceTrapTimeSinceLastChange": cdx6500PPSTSignalingSequenceTrapTimeSinceLastChange,
       "cdx6500PPSTSignalingSequenceTrapComment": cdx6500PPSTSignalingSequenceTrapComment,
       "cdx6500VoiceStatsCurrentStatus": cdx6500VoiceStatsCurrentStatus,
       "cdx6500VoiceStatsLastClearCauseCode": cdx6500VoiceStatsLastClearCauseCode,
       "cdx6500VoiceStatsLastClearDiagnosticCode": cdx6500VoiceStatsLastClearDiagnosticCode,
       "cdx6500VoiceStatsLastInboundCallPacketCalledAddress": cdx6500VoiceStatsLastInboundCallPacketCalledAddress,
       "cdx6500VoiceStatsLastInboundCallPacketCallingAddress": cdx6500VoiceStatsLastInboundCallPacketCallingAddress,
       "cdx6500VoiceStatsLastInboundCallPacketFacilities": cdx6500VoiceStatsLastInboundCallPacketFacilities,
       "cdx6500VoiceStatsLastInboundCallPacketCUD": cdx6500VoiceStatsLastInboundCallPacketCUD,
       "cdx6500VoiceStatsLastOutboundCallPacketCalledAddress": cdx6500VoiceStatsLastOutboundCallPacketCalledAddress,
       "cdx6500VoiceStatsLastOutboundCallPacketCallingAddress": cdx6500VoiceStatsLastOutboundCallPacketCallingAddress,
       "cdx6500VoiceStatsLastOutboundCallPacketFacilities": cdx6500VoiceStatsLastOutboundCallPacketFacilities,
       "cdx6500VoiceStatsLastOutboundCallPacketCUD": cdx6500VoiceStatsLastOutboundCallPacketCUD,
       "cdx6500VoiceStatsRingerStatus": cdx6500VoiceStatsRingerStatus,
       "cdx6500VoiceStatsDSPMSMSlotNumber": cdx6500VoiceStatsDSPMSMSlotNumber,
       "cdx6500VoiceStatsDSPMNumber": cdx6500VoiceStatsDSPMNumber,
       "cdx6500VoiceStatsT1E1PortNumber": cdx6500VoiceStatsT1E1PortNumber,
       "cdx6500VoiceStatsTimeSlotNumber": cdx6500VoiceStatsTimeSlotNumber,
       "cdx6500VoiceStatsDaughterCardRevAndPartNumber": cdx6500VoiceStatsDaughterCardRevAndPartNumber,
       "cdx6500VoiceStatsVADEfficiency": cdx6500VoiceStatsVADEfficiency,
       "cdx6500VoiceStatsMeanDelayDeviation": cdx6500VoiceStatsMeanDelayDeviation,
       "cdx6500VoiceStatsMaxDelayDeviation": cdx6500VoiceStatsMaxDelayDeviation,
       "cdx6500VoiceStatsPktRecResync": cdx6500VoiceStatsPktRecResync,
       "cdx6500VoiceCallStatsNoPacketDropped": cdx6500VoiceCallStatsNoPacketDropped,
       "cdx6500VoiceCallStatsNoCallsDropped": cdx6500VoiceCallStatsNoCallsDropped,
       "cdx6500VoiceCallStatsDroppedReason0": cdx6500VoiceCallStatsDroppedReason0,
       "cdx6500VoiceCallStatsDroppedReason1": cdx6500VoiceCallStatsDroppedReason1,
       "cdx6500VoiceCallStatsDroppedReason3": cdx6500VoiceCallStatsDroppedReason3,
       "cdx6500VoiceCallStatsDroppedReason5": cdx6500VoiceCallStatsDroppedReason5,
       "cdx6500VoiceCallStatsDroppedReason9": cdx6500VoiceCallStatsDroppedReason9,
       "cdx6500VoiceCallStatsDroppedReason11": cdx6500VoiceCallStatsDroppedReason11,
       "cdx6500VoiceCallStatsDroppedReason13": cdx6500VoiceCallStatsDroppedReason13,
       "cdx6500VoiceCallStatsDroppedReason17": cdx6500VoiceCallStatsDroppedReason17,
       "cdx6500VoiceCallStatsDroppedReason19": cdx6500VoiceCallStatsDroppedReason19,
       "cdx6500VoiceCallStatsDroppedReason21": cdx6500VoiceCallStatsDroppedReason21,
       "cdx6500VoiceCallStatsDroppedReason33": cdx6500VoiceCallStatsDroppedReason33,
       "cdx6500VoiceCallStatsDroppedReason-Rest": cdx6500VoiceCallStatsDroppedReason_Rest,
       "cdx6500PPSTSignalingSequenceTrapTable": cdx6500PPSTSignalingSequenceTrapTable,
       "cdx6500PPSTSignalingSequenceTrapEntry": cdx6500PPSTSignalingSequenceTrapEntry,
       "cdx6500SignalingSequenceTrapPortNumber": cdx6500SignalingSequenceTrapPortNumber,
       "cdx6500SignalingSequenceTrapEventNumber": cdx6500SignalingSequenceTrapEventNumber,
       "cdx6500SignalingSequenceTrapTxState": cdx6500SignalingSequenceTrapTxState,
       "cdx6500SignalingSequenceTrapRxState": cdx6500SignalingSequenceTrapRxState,
       "cdx6500SignalingSequenceTrapMachineState": cdx6500SignalingSequenceTrapMachineState,
       "cdx6500SignalingSequenceTrapTimeSinceLastChange": cdx6500SignalingSequenceTrapTimeSinceLastChange,
       "cdx6500SignalingSequenceTrapComment": cdx6500SignalingSequenceTrapComment,
       "cdx6500StatNetworkSvcsGroup": cdx6500StatNetworkSvcsGroup,
       "cdx6500StatVCSTable": cdx6500StatVCSTable,
       "cdx6500StatVCSEntry": cdx6500StatVCSEntry,
       "cdx6500StatVCSIndex": cdx6500StatVCSIndex,
       "cdx6500StatVCSTime": cdx6500StatVCSTime,
       "cdx6500StatVCSNoPacketDropped": cdx6500StatVCSNoPacketDropped,
       "cdx6500StatVCSNoCallsDropped": cdx6500StatVCSNoCallsDropped,
       "cdx6500StatVCSDroppedReasons": cdx6500StatVCSDroppedReasons,
       "cdx6500StatVCSNoCallsProcessed": cdx6500StatVCSNoCallsProcessed,
       "cdx6500StatVCSPercentPeakAvgCurOfCPULoad": cdx6500StatVCSPercentPeakAvgCurOfCPULoad,
       "cdx6500StatVCSPercentPeakAvgCurOfDataBuf": cdx6500StatVCSPercentPeakAvgCurOfDataBuf,
       "cdx6500StatVCSPercentPeakAvgCurOfIORBBuf": cdx6500StatVCSPercentPeakAvgCurOfIORBBuf,
       "cdx6500Controls": cdx6500Controls}
)
