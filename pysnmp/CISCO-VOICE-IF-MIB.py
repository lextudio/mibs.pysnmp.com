# SNMP MIB module (CISCO-VOICE-IF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-VOICE-IF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:12:27 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CountryCode,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CountryCode")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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


# MODULE-IDENTITY

ciscoVoiceInterfaceMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 64)
)
ciscoVoiceInterfaceMIB.setRevisions(
        ("2003-07-18 00:00",
         "2001-03-08 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CvIfObjects_ObjectIdentity = ObjectIdentity
cvIfObjects = _CvIfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 64, 1)
)
_CvIfCfgObjects_ObjectIdentity = ObjectIdentity
cvIfCfgObjects = _CvIfCfgObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 64, 1, 1)
)
_CvIfCfgTable_Object = MibTable
cvIfCfgTable = _CvIfCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 64, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cvIfCfgTable.setStatus("current")
_CvIfCfgEntry_Object = MibTableRow
cvIfCfgEntry = _CvIfCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 64, 1, 1, 1, 1)
)
cvIfCfgEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cvIfCfgEntry.setStatus("current")
_CvIfCfgNoiseRegEnable_Type = TruthValue
_CvIfCfgNoiseRegEnable_Object = MibTableColumn
cvIfCfgNoiseRegEnable = _CvIfCfgNoiseRegEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 64, 1, 1, 1, 1, 1),
    _CvIfCfgNoiseRegEnable_Type()
)
cvIfCfgNoiseRegEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvIfCfgNoiseRegEnable.setStatus("current")
_CvIfCfgNonLinearProcEnable_Type = TruthValue
_CvIfCfgNonLinearProcEnable_Object = MibTableColumn
cvIfCfgNonLinearProcEnable = _CvIfCfgNonLinearProcEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 64, 1, 1, 1, 1, 2),
    _CvIfCfgNonLinearProcEnable_Type()
)
cvIfCfgNonLinearProcEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvIfCfgNonLinearProcEnable.setStatus("current")


class _CvIfCfgMusicOnHoldThreshold_Type(Integer32):
    """Custom type cvIfCfgMusicOnHoldThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-70, -30),
    )


_CvIfCfgMusicOnHoldThreshold_Type.__name__ = "Integer32"
_CvIfCfgMusicOnHoldThreshold_Object = MibTableColumn
cvIfCfgMusicOnHoldThreshold = _CvIfCfgMusicOnHoldThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 64, 1, 1, 1, 1, 3),
    _CvIfCfgMusicOnHoldThreshold_Type()
)
cvIfCfgMusicOnHoldThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvIfCfgMusicOnHoldThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cvIfCfgMusicOnHoldThreshold.setUnits("dBm")


class _CvIfCfgInGain_Type(Integer32):
    """Custom type cvIfCfgInGain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-6, 14),
    )


_CvIfCfgInGain_Type.__name__ = "Integer32"
_CvIfCfgInGain_Object = MibTableColumn
cvIfCfgInGain = _CvIfCfgInGain_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 64, 1, 1, 1, 1, 4),
    _CvIfCfgInGain_Type()
)
cvIfCfgInGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvIfCfgInGain.setStatus("current")
if mibBuilder.loadTexts:
    cvIfCfgInGain.setUnits("dB")


class _CvIfCfgOutAttn_Type(Integer32):
    """Custom type cvIfCfgOutAttn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_CvIfCfgOutAttn_Type.__name__ = "Integer32"
_CvIfCfgOutAttn_Object = MibTableColumn
cvIfCfgOutAttn = _CvIfCfgOutAttn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 64, 1, 1, 1, 1, 5),
    _CvIfCfgOutAttn_Type()
)
cvIfCfgOutAttn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvIfCfgOutAttn.setStatus("current")
if mibBuilder.loadTexts:
    cvIfCfgOutAttn.setUnits("dB")
_CvIfCfgEchoCancelEnable_Type = TruthValue
_CvIfCfgEchoCancelEnable_Object = MibTableColumn
cvIfCfgEchoCancelEnable = _CvIfCfgEchoCancelEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 64, 1, 1, 1, 1, 6),
    _CvIfCfgEchoCancelEnable_Type()
)
cvIfCfgEchoCancelEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvIfCfgEchoCancelEnable.setStatus("current")


class _CvIfCfgEchoCancelCoverage_Type(Integer32):
    """Custom type cvIfCfgEchoCancelCoverage based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("echoCanceller112ms", 9),
          ("echoCanceller128ms", 10),
          ("echoCanceller16ms", 1),
          ("echoCanceller24ms", 2),
          ("echoCanceller32ms", 3),
          ("echoCanceller48ms", 5),
          ("echoCanceller64ms", 6),
          ("echoCanceller80ms", 7),
          ("echoCanceller8ms", 4),
          ("echoCanceller96ms", 8))
    )


_CvIfCfgEchoCancelCoverage_Type.__name__ = "Integer32"
_CvIfCfgEchoCancelCoverage_Object = MibTableColumn
cvIfCfgEchoCancelCoverage = _CvIfCfgEchoCancelCoverage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 64, 1, 1, 1, 1, 7),
    _CvIfCfgEchoCancelCoverage_Type()
)
cvIfCfgEchoCancelCoverage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvIfCfgEchoCancelCoverage.setStatus("current")


class _CvIfCfgConnectionMode_Type(Integer32):
    """Custom type cvIfCfgConnectionMode based on Integer32"""
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
        *(("normal", 1),
          ("plar", 3),
          ("tieline", 4),
          ("trunk", 2))
    )


_CvIfCfgConnectionMode_Type.__name__ = "Integer32"
_CvIfCfgConnectionMode_Object = MibTableColumn
cvIfCfgConnectionMode = _CvIfCfgConnectionMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 64, 1, 1, 1, 1, 8),
    _CvIfCfgConnectionMode_Type()
)
cvIfCfgConnectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvIfCfgConnectionMode.setStatus("current")


class _CvIfCfgConnectionNumber_Type(DisplayString):
    """Custom type cvIfCfgConnectionNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CvIfCfgConnectionNumber_Type.__name__ = "DisplayString"
_CvIfCfgConnectionNumber_Object = MibTableColumn
cvIfCfgConnectionNumber = _CvIfCfgConnectionNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 64, 1, 1, 1, 1, 9),
    _CvIfCfgConnectionNumber_Type()
)
cvIfCfgConnectionNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvIfCfgConnectionNumber.setStatus("current")


class _CvIfCfgInitialDigitTimeOut_Type(Integer32):
    """Custom type cvIfCfgInitialDigitTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_CvIfCfgInitialDigitTimeOut_Type.__name__ = "Integer32"
_CvIfCfgInitialDigitTimeOut_Object = MibTableColumn
cvIfCfgInitialDigitTimeOut = _CvIfCfgInitialDigitTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 64, 1, 1, 1, 1, 10),
    _CvIfCfgInitialDigitTimeOut_Type()
)
cvIfCfgInitialDigitTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvIfCfgInitialDigitTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    cvIfCfgInitialDigitTimeOut.setUnits("seconds")


class _CvIfCfgInterDigitTimeOut_Type(Integer32):
    """Custom type cvIfCfgInterDigitTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_CvIfCfgInterDigitTimeOut_Type.__name__ = "Integer32"
_CvIfCfgInterDigitTimeOut_Object = MibTableColumn
cvIfCfgInterDigitTimeOut = _CvIfCfgInterDigitTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 64, 1, 1, 1, 1, 11),
    _CvIfCfgInterDigitTimeOut_Type()
)
cvIfCfgInterDigitTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvIfCfgInterDigitTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    cvIfCfgInterDigitTimeOut.setUnits("seconds")
_CvIfCfgRegionalTone_Type = CountryCode
_CvIfCfgRegionalTone_Object = MibTableColumn
cvIfCfgRegionalTone = _CvIfCfgRegionalTone_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 64, 1, 1, 1, 1, 12),
    _CvIfCfgRegionalTone_Type()
)
cvIfCfgRegionalTone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvIfCfgRegionalTone.setStatus("current")


class _CvIfCfgEchoCancelWorstERL_Type(Integer32):
    """Custom type cvIfCfgEchoCancelWorstERL based on Integer32"""
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
        *(("echoCancellerWorstERL0dB", 4),
          ("echoCancellerWorstERL3dB", 3),
          ("echoCancellerWorstERL6dB", 2),
          ("echoCancellerWorstERLUnknown", 1))
    )


_CvIfCfgEchoCancelWorstERL_Type.__name__ = "Integer32"
_CvIfCfgEchoCancelWorstERL_Object = MibTableColumn
cvIfCfgEchoCancelWorstERL = _CvIfCfgEchoCancelWorstERL_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 64, 1, 1, 1, 1, 13),
    _CvIfCfgEchoCancelWorstERL_Type()
)
cvIfCfgEchoCancelWorstERL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvIfCfgEchoCancelWorstERL.setStatus("current")


class _CvIfCfgEchoCanceller_Type(Integer32):
    """Custom type cvIfCfgEchoCanceller based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("echoCancellerExtended", 2),
          ("echoCancellerStandard", 1))
    )


_CvIfCfgEchoCanceller_Type.__name__ = "Integer32"
_CvIfCfgEchoCanceller_Object = MibTableColumn
cvIfCfgEchoCanceller = _CvIfCfgEchoCanceller_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 64, 1, 1, 1, 1, 14),
    _CvIfCfgEchoCanceller_Type()
)
cvIfCfgEchoCanceller.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvIfCfgEchoCanceller.setStatus("current")
_CvIfConformance_ObjectIdentity = ObjectIdentity
cvIfConformance = _CvIfConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 64, 2)
)
_CvIfCompliances_ObjectIdentity = ObjectIdentity
cvIfCompliances = _CvIfCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 64, 2, 1)
)
_CvIfGroups_ObjectIdentity = ObjectIdentity
cvIfGroups = _CvIfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 64, 2, 2)
)

# Managed Objects groups

cvIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 64, 2, 2, 1)
)
cvIfGroup.setObjects(
      *(("CISCO-VOICE-IF-MIB", "cvIfCfgNoiseRegEnable"),
        ("CISCO-VOICE-IF-MIB", "cvIfCfgNonLinearProcEnable"),
        ("CISCO-VOICE-IF-MIB", "cvIfCfgMusicOnHoldThreshold"),
        ("CISCO-VOICE-IF-MIB", "cvIfCfgInGain"),
        ("CISCO-VOICE-IF-MIB", "cvIfCfgOutAttn"),
        ("CISCO-VOICE-IF-MIB", "cvIfCfgEchoCancelEnable"),
        ("CISCO-VOICE-IF-MIB", "cvIfCfgEchoCancelCoverage"),
        ("CISCO-VOICE-IF-MIB", "cvIfCfgInitialDigitTimeOut"),
        ("CISCO-VOICE-IF-MIB", "cvIfCfgInterDigitTimeOut"),
        ("CISCO-VOICE-IF-MIB", "cvIfCfgRegionalTone"),
        ("CISCO-VOICE-IF-MIB", "cvIfCfgEchoCancelWorstERL"),
        ("CISCO-VOICE-IF-MIB", "cvIfCfgEchoCanceller"))
)
if mibBuilder.loadTexts:
    cvIfGroup.setStatus("current")

cvIfConnectionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 64, 2, 2, 2)
)
cvIfConnectionGroup.setObjects(
      *(("CISCO-VOICE-IF-MIB", "cvIfCfgConnectionMode"),
        ("CISCO-VOICE-IF-MIB", "cvIfCfgConnectionNumber"))
)
if mibBuilder.loadTexts:
    cvIfConnectionGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cvIfCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 64, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cvIfCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-VOICE-IF-MIB",
    **{"ciscoVoiceInterfaceMIB": ciscoVoiceInterfaceMIB,
       "cvIfObjects": cvIfObjects,
       "cvIfCfgObjects": cvIfCfgObjects,
       "cvIfCfgTable": cvIfCfgTable,
       "cvIfCfgEntry": cvIfCfgEntry,
       "cvIfCfgNoiseRegEnable": cvIfCfgNoiseRegEnable,
       "cvIfCfgNonLinearProcEnable": cvIfCfgNonLinearProcEnable,
       "cvIfCfgMusicOnHoldThreshold": cvIfCfgMusicOnHoldThreshold,
       "cvIfCfgInGain": cvIfCfgInGain,
       "cvIfCfgOutAttn": cvIfCfgOutAttn,
       "cvIfCfgEchoCancelEnable": cvIfCfgEchoCancelEnable,
       "cvIfCfgEchoCancelCoverage": cvIfCfgEchoCancelCoverage,
       "cvIfCfgConnectionMode": cvIfCfgConnectionMode,
       "cvIfCfgConnectionNumber": cvIfCfgConnectionNumber,
       "cvIfCfgInitialDigitTimeOut": cvIfCfgInitialDigitTimeOut,
       "cvIfCfgInterDigitTimeOut": cvIfCfgInterDigitTimeOut,
       "cvIfCfgRegionalTone": cvIfCfgRegionalTone,
       "cvIfCfgEchoCancelWorstERL": cvIfCfgEchoCancelWorstERL,
       "cvIfCfgEchoCanceller": cvIfCfgEchoCanceller,
       "cvIfConformance": cvIfConformance,
       "cvIfCompliances": cvIfCompliances,
       "cvIfCompliance": cvIfCompliance,
       "cvIfGroups": cvIfGroups,
       "cvIfGroup": cvIfGroup,
       "cvIfConnectionGroup": cvIfConnectionGroup}
)
