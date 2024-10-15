# SNMP MIB module (CISCO-VOICE-URI-CLASS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-VOICE-URI-CLASS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:12:30 2024
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

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ciscoVoiceUriClassMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999999)
)
ciscoVoiceUriClassMIB.setRevisions(
        ("2002-10-10 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CvUriClassTagIndex(OctetString, TextualConvention):
    status = "current"
    displayHint = "32a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



class CvUriClassTag(OctetString, TextualConvention):
    status = "current"
    displayHint = "32a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class CvUriClassPattern(OctetString, TextualConvention):
    status = "current"
    displayHint = "32a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class CvUriClassPreference(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )



# MIB Managed Objects in the order of their OIDs

_CvUriClassMIBNotifications_ObjectIdentity = ObjectIdentity
cvUriClassMIBNotifications = _CvUriClassMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999999, 0)
)
_CvUriClassMIBObjects_ObjectIdentity = ObjectIdentity
cvUriClassMIBObjects = _CvUriClassMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1)
)
_CvUriClass_ObjectIdentity = ObjectIdentity
cvUriClass = _CvUriClass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1)
)
_CvUriClassCfgTable_Object = MibTable
cvUriClassCfgTable = _CvUriClassCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cvUriClassCfgTable.setStatus("current")
_CvUriClassCfgEntry_Object = MibTableRow
cvUriClassCfgEntry = _CvUriClassCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 1, 1)
)
cvUriClassCfgEntry.setIndexNames(
    (1, "CISCO-VOICE-URI-CLASS-MIB", "cvUriClassCfgTag"),
)
if mibBuilder.loadTexts:
    cvUriClassCfgEntry.setStatus("current")
_CvUriClassCfgTag_Type = CvUriClassTagIndex
_CvUriClassCfgTag_Object = MibTableColumn
cvUriClassCfgTag = _CvUriClassCfgTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 1, 1, 1),
    _CvUriClassCfgTag_Type()
)
cvUriClassCfgTag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvUriClassCfgTag.setStatus("current")


class _CvUriClassCfgType_Type(Integer32):
    """Custom type cvUriClassCfgType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sip", 1),
          ("tel", 2))
    )


_CvUriClassCfgType_Type.__name__ = "Integer32"
_CvUriClassCfgType_Object = MibTableColumn
cvUriClassCfgType = _CvUriClassCfgType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 1, 1, 2),
    _CvUriClassCfgType_Type()
)
cvUriClassCfgType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvUriClassCfgType.setStatus("current")
_CvUriClassCfgStatus_Type = RowStatus
_CvUriClassCfgStatus_Object = MibTableColumn
cvUriClassCfgStatus = _CvUriClassCfgStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 1, 1, 3),
    _CvUriClassCfgStatus_Type()
)
cvUriClassCfgStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvUriClassCfgStatus.setStatus("current")
_CvSIPUriClassCfgTable_Object = MibTable
cvSIPUriClassCfgTable = _CvSIPUriClassCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cvSIPUriClassCfgTable.setStatus("current")
_CvSIPUriClassCfgEntry_Object = MibTableRow
cvSIPUriClassCfgEntry = _CvSIPUriClassCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 2, 1)
)
cvSIPUriClassCfgEntry.setIndexNames(
    (1, "CISCO-VOICE-URI-CLASS-MIB", "cvUriClassCfgTag"),
)
if mibBuilder.loadTexts:
    cvSIPUriClassCfgEntry.setStatus("current")
_CvSIPUriClassCfgUserIDPattern_Type = CvUriClassPattern
_CvSIPUriClassCfgUserIDPattern_Object = MibTableColumn
cvSIPUriClassCfgUserIDPattern = _CvSIPUriClassCfgUserIDPattern_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 2, 1, 1),
    _CvSIPUriClassCfgUserIDPattern_Type()
)
cvSIPUriClassCfgUserIDPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvSIPUriClassCfgUserIDPattern.setStatus("current")
_CvSIPUriClassCfgHostPattern_Type = CvUriClassPattern
_CvSIPUriClassCfgHostPattern_Object = MibTableColumn
cvSIPUriClassCfgHostPattern = _CvSIPUriClassCfgHostPattern_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 2, 1, 2),
    _CvSIPUriClassCfgHostPattern_Type()
)
cvSIPUriClassCfgHostPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvSIPUriClassCfgHostPattern.setStatus("current")
_CvSIPUriClassCfgPhoneCtxtPattern_Type = CvUriClassPattern
_CvSIPUriClassCfgPhoneCtxtPattern_Object = MibTableColumn
cvSIPUriClassCfgPhoneCtxtPattern = _CvSIPUriClassCfgPhoneCtxtPattern_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 2, 1, 3),
    _CvSIPUriClassCfgPhoneCtxtPattern_Type()
)
cvSIPUriClassCfgPhoneCtxtPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvSIPUriClassCfgPhoneCtxtPattern.setStatus("current")
_CvTELUriClassCfgTable_Object = MibTable
cvTELUriClassCfgTable = _CvTELUriClassCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cvTELUriClassCfgTable.setStatus("current")
_CvTELUriClassCfgEntry_Object = MibTableRow
cvTELUriClassCfgEntry = _CvTELUriClassCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 3, 1)
)
cvTELUriClassCfgEntry.setIndexNames(
    (1, "CISCO-VOICE-URI-CLASS-MIB", "cvUriClassCfgTag"),
)
if mibBuilder.loadTexts:
    cvTELUriClassCfgEntry.setStatus("current")
_CvTELUriClassCfgPhoneNumPattern_Type = CvUriClassPattern
_CvTELUriClassCfgPhoneNumPattern_Object = MibTableColumn
cvTELUriClassCfgPhoneNumPattern = _CvTELUriClassCfgPhoneNumPattern_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 3, 1, 1),
    _CvTELUriClassCfgPhoneNumPattern_Type()
)
cvTELUriClassCfgPhoneNumPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvTELUriClassCfgPhoneNumPattern.setStatus("current")
_CvTELUriClassCfgPhoneCtxtPattern_Type = CvUriClassPattern
_CvTELUriClassCfgPhoneCtxtPattern_Object = MibTableColumn
cvTELUriClassCfgPhoneCtxtPattern = _CvTELUriClassCfgPhoneCtxtPattern_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 3, 1, 2),
    _CvTELUriClassCfgPhoneCtxtPattern_Type()
)
cvTELUriClassCfgPhoneCtxtPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvTELUriClassCfgPhoneCtxtPattern.setStatus("current")
_CvCommonUriClassCfgTable_Object = MibTable
cvCommonUriClassCfgTable = _CvCommonUriClassCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 4)
)
if mibBuilder.loadTexts:
    cvCommonUriClassCfgTable.setStatus("current")
_CvCommonUriClassCfgEntry_Object = MibTableRow
cvCommonUriClassCfgEntry = _CvCommonUriClassCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 4, 1)
)
cvCommonUriClassCfgEntry.setIndexNames(
    (1, "CISCO-VOICE-URI-CLASS-MIB", "cvUriClassCfgTag"),
)
if mibBuilder.loadTexts:
    cvCommonUriClassCfgEntry.setStatus("current")


class _CvCommonUriClassCfgURIPattern_Type(OctetString):
    """Custom type cvCommonUriClassCfgURIPattern based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CvCommonUriClassCfgURIPattern_Type.__name__ = "OctetString"
_CvCommonUriClassCfgURIPattern_Object = MibTableColumn
cvCommonUriClassCfgURIPattern = _CvCommonUriClassCfgURIPattern_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 1, 4, 1, 1),
    _CvCommonUriClassCfgURIPattern_Type()
)
cvCommonUriClassCfgURIPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvCommonUriClassCfgURIPattern.setStatus("current")
_CvUriClassSIPGeneralConfig_ObjectIdentity = ObjectIdentity
cvUriClassSIPGeneralConfig = _CvUriClassSIPGeneralConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 2)
)


class _CvUriClassSIPHostPreference_Type(CvUriClassPreference):
    """Custom type cvUriClassSIPHostPreference based on CvUriClassPreference"""
    defaultValue = 1


_CvUriClassSIPHostPreference_Object = MibScalar
cvUriClassSIPHostPreference = _CvUriClassSIPHostPreference_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 2, 1),
    _CvUriClassSIPHostPreference_Type()
)
cvUriClassSIPHostPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvUriClassSIPHostPreference.setStatus("current")


class _CvUriClassSIPUserIDPreference_Type(CvUriClassPreference):
    """Custom type cvUriClassSIPUserIDPreference based on CvUriClassPreference"""
    defaultValue = 2


_CvUriClassSIPUserIDPreference_Object = MibScalar
cvUriClassSIPUserIDPreference = _CvUriClassSIPUserIDPreference_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999999, 1, 2, 2),
    _CvUriClassSIPUserIDPreference_Type()
)
cvUriClassSIPUserIDPreference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cvUriClassSIPUserIDPreference.setStatus("current")
_CvUriClassMIBConformance_ObjectIdentity = ObjectIdentity
cvUriClassMIBConformance = _CvUriClassMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999999, 2)
)
_CvUriClassMIBCompliances_ObjectIdentity = ObjectIdentity
cvUriClassMIBCompliances = _CvUriClassMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999999, 2, 1)
)
_CvUriClassMIBGroups_ObjectIdentity = ObjectIdentity
cvUriClassMIBGroups = _CvUriClassMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999999, 2, 2)
)

# Managed Objects groups

cvUriClassGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999999, 2, 2, 1)
)
cvUriClassGroup.setObjects(
      *(("CISCO-VOICE-URI-CLASS-MIB", "cvUriClassCfgType"),
        ("CISCO-VOICE-URI-CLASS-MIB", "cvUriClassCfgStatus"),
        ("CISCO-VOICE-URI-CLASS-MIB", "cvSIPUriClassCfgUserIDPattern"),
        ("CISCO-VOICE-URI-CLASS-MIB", "cvSIPUriClassCfgHostPattern"),
        ("CISCO-VOICE-URI-CLASS-MIB", "cvSIPUriClassCfgPhoneCtxtPattern"),
        ("CISCO-VOICE-URI-CLASS-MIB", "cvTELUriClassCfgPhoneNumPattern"),
        ("CISCO-VOICE-URI-CLASS-MIB", "cvTELUriClassCfgPhoneCtxtPattern"),
        ("CISCO-VOICE-URI-CLASS-MIB", "cvCommonUriClassCfgURIPattern"),
        ("CISCO-VOICE-URI-CLASS-MIB", "cvUriClassSIPHostPreference"),
        ("CISCO-VOICE-URI-CLASS-MIB", "cvUriClassSIPUserIDPreference"))
)
if mibBuilder.loadTexts:
    cvUriClassGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cvUriClassMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 99999999, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cvUriClassMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-VOICE-URI-CLASS-MIB",
    **{"CvUriClassTagIndex": CvUriClassTagIndex,
       "CvUriClassTag": CvUriClassTag,
       "CvUriClassPattern": CvUriClassPattern,
       "CvUriClassPreference": CvUriClassPreference,
       "ciscoVoiceUriClassMIB": ciscoVoiceUriClassMIB,
       "cvUriClassMIBNotifications": cvUriClassMIBNotifications,
       "cvUriClassMIBObjects": cvUriClassMIBObjects,
       "cvUriClass": cvUriClass,
       "cvUriClassCfgTable": cvUriClassCfgTable,
       "cvUriClassCfgEntry": cvUriClassCfgEntry,
       "cvUriClassCfgTag": cvUriClassCfgTag,
       "cvUriClassCfgType": cvUriClassCfgType,
       "cvUriClassCfgStatus": cvUriClassCfgStatus,
       "cvSIPUriClassCfgTable": cvSIPUriClassCfgTable,
       "cvSIPUriClassCfgEntry": cvSIPUriClassCfgEntry,
       "cvSIPUriClassCfgUserIDPattern": cvSIPUriClassCfgUserIDPattern,
       "cvSIPUriClassCfgHostPattern": cvSIPUriClassCfgHostPattern,
       "cvSIPUriClassCfgPhoneCtxtPattern": cvSIPUriClassCfgPhoneCtxtPattern,
       "cvTELUriClassCfgTable": cvTELUriClassCfgTable,
       "cvTELUriClassCfgEntry": cvTELUriClassCfgEntry,
       "cvTELUriClassCfgPhoneNumPattern": cvTELUriClassCfgPhoneNumPattern,
       "cvTELUriClassCfgPhoneCtxtPattern": cvTELUriClassCfgPhoneCtxtPattern,
       "cvCommonUriClassCfgTable": cvCommonUriClassCfgTable,
       "cvCommonUriClassCfgEntry": cvCommonUriClassCfgEntry,
       "cvCommonUriClassCfgURIPattern": cvCommonUriClassCfgURIPattern,
       "cvUriClassSIPGeneralConfig": cvUriClassSIPGeneralConfig,
       "cvUriClassSIPHostPreference": cvUriClassSIPHostPreference,
       "cvUriClassSIPUserIDPreference": cvUriClassSIPUserIDPreference,
       "cvUriClassMIBConformance": cvUriClassMIBConformance,
       "cvUriClassMIBCompliances": cvUriClassMIBCompliances,
       "cvUriClassMIBCompliance": cvUriClassMIBCompliance,
       "cvUriClassMIBGroups": cvUriClassMIBGroups,
       "cvUriClassGroup": cvUriClassGroup}
)
