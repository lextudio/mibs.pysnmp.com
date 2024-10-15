# SNMP MIB module (CISCO-VOICE-LMR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-VOICE-LMR-MIB
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

ciscoVoiceLmrMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 510)
)
ciscoVoiceLmrMIB.setRevisions(
        ("2004-10-14 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class VoiceFrequency(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4000),
    )



class VoiceAmplitude(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-30, 3),
    )



class LmrToneDuration(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )



# MIB Managed Objects in the order of their OIDs

_CvlMIBObjects_ObjectIdentity = ObjectIdentity
cvlMIBObjects = _CvlMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1)
)
_CvlToneObjects_ObjectIdentity = ObjectIdentity
cvlToneObjects = _CvlToneObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1)
)
_CvlClassTable_Object = MibTable
cvlClassTable = _CvlClassTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cvlClassTable.setStatus("current")
_CvlClassEntry_Object = MibTableRow
cvlClassEntry = _CvlClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 1, 1)
)
cvlClassEntry.setIndexNames(
    (0, "CISCO-VOICE-LMR-MIB", "cvlClassIndex"),
)
if mibBuilder.loadTexts:
    cvlClassEntry.setStatus("current")


class _CvlClassIndex_Type(Unsigned32):
    """Custom type cvlClassIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_CvlClassIndex_Type.__name__ = "Unsigned32"
_CvlClassIndex_Object = MibTableColumn
cvlClassIndex = _CvlClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 1, 1, 1),
    _CvlClassIndex_Type()
)
cvlClassIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvlClassIndex.setStatus("current")


class _CvlClassName_Type(SnmpAdminString):
    """Custom type cvlClassName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_CvlClassName_Type.__name__ = "SnmpAdminString"
_CvlClassName_Object = MibTableColumn
cvlClassName = _CvlClassName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 1, 1, 2),
    _CvlClassName_Type()
)
cvlClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvlClassName.setStatus("current")


class _CvlDigitalFilter_Type(Integer32):
    """Custom type cvlDigitalFilter based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("digitalFilter1950HZ", 1),
          ("digitalFilter2175HZ", 2),
          ("digitalFilterNone", 0))
    )


_CvlDigitalFilter_Type.__name__ = "Integer32"
_CvlDigitalFilter_Object = MibTableColumn
cvlDigitalFilter = _CvlDigitalFilter_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 1, 1, 3),
    _CvlDigitalFilter_Type()
)
cvlDigitalFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvlDigitalFilter.setStatus("current")


class _CvlGuardToneFreq_Type(VoiceFrequency):
    """Custom type cvlGuardToneFreq based on VoiceFrequency"""
    defaultValue = 0


_CvlGuardToneFreq_Object = MibTableColumn
cvlGuardToneFreq = _CvlGuardToneFreq_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 1, 1, 4),
    _CvlGuardToneFreq_Type()
)
cvlGuardToneFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvlGuardToneFreq.setStatus("current")


class _CvlGuardToneAmp_Type(VoiceAmplitude):
    """Custom type cvlGuardToneAmp based on VoiceAmplitude"""
    defaultValue = 0


_CvlGuardToneAmp_Object = MibTableColumn
cvlGuardToneAmp = _CvlGuardToneAmp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 1, 1, 5),
    _CvlGuardToneAmp_Type()
)
cvlGuardToneAmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvlGuardToneAmp.setStatus("current")


class _CvlIdleToneFlag_Type(TruthValue):
    """Custom type cvlIdleToneFlag based on TruthValue"""


_CvlIdleToneFlag_Object = MibTableColumn
cvlIdleToneFlag = _CvlIdleToneFlag_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 1, 1, 6),
    _CvlIdleToneFlag_Type()
)
cvlIdleToneFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvlIdleToneFlag.setStatus("current")
_CvlSignalToneTable_Object = MibTable
cvlSignalToneTable = _CvlSignalToneTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cvlSignalToneTable.setStatus("current")
_CvlSignalToneEntry_Object = MibTableRow
cvlSignalToneEntry = _CvlSignalToneEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 2, 1)
)
cvlSignalToneEntry.setIndexNames(
    (0, "CISCO-VOICE-LMR-MIB", "cvlSignalToneGroupIndex"),
    (0, "CISCO-VOICE-LMR-MIB", "cvlSignalToneIndex"),
)
if mibBuilder.loadTexts:
    cvlSignalToneEntry.setStatus("current")


class _CvlSignalToneGroupIndex_Type(Unsigned32):
    """Custom type cvlSignalToneGroupIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_CvlSignalToneGroupIndex_Type.__name__ = "Unsigned32"
_CvlSignalToneGroupIndex_Object = MibTableColumn
cvlSignalToneGroupIndex = _CvlSignalToneGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 2, 1, 1),
    _CvlSignalToneGroupIndex_Type()
)
cvlSignalToneGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvlSignalToneGroupIndex.setStatus("current")


class _CvlSignalToneIndex_Type(Unsigned32):
    """Custom type cvlSignalToneIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_CvlSignalToneIndex_Type.__name__ = "Unsigned32"
_CvlSignalToneIndex_Object = MibTableColumn
cvlSignalToneIndex = _CvlSignalToneIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 2, 1, 2),
    _CvlSignalToneIndex_Type()
)
cvlSignalToneIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvlSignalToneIndex.setStatus("current")


class _CvlSignalToneName_Type(SnmpAdminString):
    """Custom type cvlSignalToneName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 19),
    )


_CvlSignalToneName_Type.__name__ = "SnmpAdminString"
_CvlSignalToneName_Object = MibTableColumn
cvlSignalToneName = _CvlSignalToneName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 2, 1, 3),
    _CvlSignalToneName_Type()
)
cvlSignalToneName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvlSignalToneName.setStatus("current")
_CvlSignalToneFreq_Type = VoiceFrequency
_CvlSignalToneFreq_Object = MibTableColumn
cvlSignalToneFreq = _CvlSignalToneFreq_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 2, 1, 4),
    _CvlSignalToneFreq_Type()
)
cvlSignalToneFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvlSignalToneFreq.setStatus("current")
_CvlSignalToneAmp_Type = VoiceAmplitude
_CvlSignalToneAmp_Object = MibTableColumn
cvlSignalToneAmp = _CvlSignalToneAmp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 2, 1, 5),
    _CvlSignalToneAmp_Type()
)
cvlSignalToneAmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvlSignalToneAmp.setStatus("current")
_CvlSignalToneDur_Type = LmrToneDuration
_CvlSignalToneDur_Object = MibTableColumn
cvlSignalToneDur = _CvlSignalToneDur_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 1, 1, 2, 1, 6),
    _CvlSignalToneDur_Type()
)
cvlSignalToneDur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvlSignalToneDur.setStatus("current")
_CvlMIBConformance_ObjectIdentity = ObjectIdentity
cvlMIBConformance = _CvlMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 2)
)
_CvlMIBCompliances_ObjectIdentity = ObjectIdentity
cvlMIBCompliances = _CvlMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 2, 1)
)
_CvlMIBGroups_ObjectIdentity = ObjectIdentity
cvlMIBGroups = _CvlMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 2, 2)
)

# Managed Objects groups

cvlToneClassGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 2, 2, 1)
)
cvlToneClassGroup.setObjects(
      *(("CISCO-VOICE-LMR-MIB", "cvlClassName"),
        ("CISCO-VOICE-LMR-MIB", "cvlDigitalFilter"),
        ("CISCO-VOICE-LMR-MIB", "cvlGuardToneFreq"),
        ("CISCO-VOICE-LMR-MIB", "cvlGuardToneAmp"),
        ("CISCO-VOICE-LMR-MIB", "cvlIdleToneFlag"))
)
if mibBuilder.loadTexts:
    cvlToneClassGroup.setStatus("current")

cvlToneSignalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 2, 2, 2)
)
cvlToneSignalGroup.setObjects(
      *(("CISCO-VOICE-LMR-MIB", "cvlSignalToneName"),
        ("CISCO-VOICE-LMR-MIB", "cvlSignalToneFreq"),
        ("CISCO-VOICE-LMR-MIB", "cvlSignalToneAmp"),
        ("CISCO-VOICE-LMR-MIB", "cvlSignalToneDur"))
)
if mibBuilder.loadTexts:
    cvlToneSignalGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cvlMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 510, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cvlMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-VOICE-LMR-MIB",
    **{"VoiceFrequency": VoiceFrequency,
       "VoiceAmplitude": VoiceAmplitude,
       "LmrToneDuration": LmrToneDuration,
       "ciscoVoiceLmrMIB": ciscoVoiceLmrMIB,
       "cvlMIBObjects": cvlMIBObjects,
       "cvlToneObjects": cvlToneObjects,
       "cvlClassTable": cvlClassTable,
       "cvlClassEntry": cvlClassEntry,
       "cvlClassIndex": cvlClassIndex,
       "cvlClassName": cvlClassName,
       "cvlDigitalFilter": cvlDigitalFilter,
       "cvlGuardToneFreq": cvlGuardToneFreq,
       "cvlGuardToneAmp": cvlGuardToneAmp,
       "cvlIdleToneFlag": cvlIdleToneFlag,
       "cvlSignalToneTable": cvlSignalToneTable,
       "cvlSignalToneEntry": cvlSignalToneEntry,
       "cvlSignalToneGroupIndex": cvlSignalToneGroupIndex,
       "cvlSignalToneIndex": cvlSignalToneIndex,
       "cvlSignalToneName": cvlSignalToneName,
       "cvlSignalToneFreq": cvlSignalToneFreq,
       "cvlSignalToneAmp": cvlSignalToneAmp,
       "cvlSignalToneDur": cvlSignalToneDur,
       "cvlMIBConformance": cvlMIBConformance,
       "cvlMIBCompliances": cvlMIBCompliances,
       "cvlMIBCompliance": cvlMIBCompliance,
       "cvlMIBGroups": cvlMIBGroups,
       "cvlToneClassGroup": cvlToneClassGroup,
       "cvlToneSignalGroup": cvlToneSignalGroup}
)
