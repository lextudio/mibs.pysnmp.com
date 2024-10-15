# SNMP MIB module (CISCO-VOICE-TONE-CADENCE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-VOICE-TONE-CADENCE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:12:29 2024
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

(CVoiceTonePlanIndex,
 cmgwIndex) = mibBuilder.importSymbols(
    "CISCO-MEDIA-GATEWAY-MIB",
    "CVoiceTonePlanIndex",
    "cmgwIndex")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(CountryCode,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CountryCode")

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
 RowStatus,
 StorageType,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention")


# MODULE-IDENTITY

ciscoVoiceToneCadenceMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 356)
)
ciscoVoiceToneCadenceMIB.setRevisions(
        ("2003-05-28 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CToneFrequency(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )



class CToneAmplitude(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 64),
    )



class CToneCadence(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 64),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoVoiceToneCadenceMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoVoiceToneCadenceMIBNotifs = _CiscoVoiceToneCadenceMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 356, 0)
)
_CiscoVoiceToneCadenceMIBObjects_ObjectIdentity = ObjectIdentity
ciscoVoiceToneCadenceMIBObjects = _CiscoVoiceToneCadenceMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 356, 1)
)
_CVoiceToneCadenceConfig_ObjectIdentity = ObjectIdentity
cVoiceToneCadenceConfig = _CVoiceToneCadenceConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 356, 1, 1)
)
_CvtcTonePlanTable_Object = MibTable
cvtcTonePlanTable = _CvtcTonePlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 356, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cvtcTonePlanTable.setStatus("current")
_CvtcTonePlanEntry_Object = MibTableRow
cvtcTonePlanEntry = _CvtcTonePlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 356, 1, 1, 1, 1)
)
cvtcTonePlanEntry.setIndexNames(
    (0, "CISCO-MEDIA-GATEWAY-MIB", "cmgwIndex"),
    (0, "CISCO-VOICE-TONE-CADENCE-MIB", "cvtcTonePlanId"),
)
if mibBuilder.loadTexts:
    cvtcTonePlanEntry.setStatus("current")
_CvtcTonePlanId_Type = CVoiceTonePlanIndex
_CvtcTonePlanId_Object = MibTableColumn
cvtcTonePlanId = _CvtcTonePlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 356, 1, 1, 1, 1, 1),
    _CvtcTonePlanId_Type()
)
cvtcTonePlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvtcTonePlanId.setStatus("current")
_CvtcTonePlanVifCount_Type = Gauge32
_CvtcTonePlanVifCount_Object = MibTableColumn
cvtcTonePlanVifCount = _CvtcTonePlanVifCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 356, 1, 1, 1, 1, 2),
    _CvtcTonePlanVifCount_Type()
)
cvtcTonePlanVifCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtcTonePlanVifCount.setStatus("current")
_CvtcTonePlanCountry_Type = CountryCode
_CvtcTonePlanCountry_Object = MibTableColumn
cvtcTonePlanCountry = _CvtcTonePlanCountry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 356, 1, 1, 1, 1, 3),
    _CvtcTonePlanCountry_Type()
)
cvtcTonePlanCountry.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvtcTonePlanCountry.setStatus("current")


class _CvtcTonePlanVersion_Type(Unsigned32):
    """Custom type cvtcTonePlanVersion based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CvtcTonePlanVersion_Type.__name__ = "Unsigned32"
_CvtcTonePlanVersion_Object = MibTableColumn
cvtcTonePlanVersion = _CvtcTonePlanVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 356, 1, 1, 1, 1, 4),
    _CvtcTonePlanVersion_Type()
)
cvtcTonePlanVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvtcTonePlanVersion.setStatus("current")


class _CvtcTonePlanFileName_Type(SnmpAdminString):
    """Custom type cvtcTonePlanFileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CvtcTonePlanFileName_Type.__name__ = "SnmpAdminString"
_CvtcTonePlanFileName_Object = MibTableColumn
cvtcTonePlanFileName = _CvtcTonePlanFileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 356, 1, 1, 1, 1, 5),
    _CvtcTonePlanFileName_Type()
)
cvtcTonePlanFileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvtcTonePlanFileName.setStatus("current")
_CvtcTonePlanStorageType_Type = StorageType
_CvtcTonePlanStorageType_Object = MibTableColumn
cvtcTonePlanStorageType = _CvtcTonePlanStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 356, 1, 1, 1, 1, 6),
    _CvtcTonePlanStorageType_Type()
)
cvtcTonePlanStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvtcTonePlanStorageType.setStatus("current")
_CvtcTonePlanRowStatus_Type = RowStatus
_CvtcTonePlanRowStatus_Object = MibTableColumn
cvtcTonePlanRowStatus = _CvtcTonePlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 356, 1, 1, 1, 1, 7),
    _CvtcTonePlanRowStatus_Type()
)
cvtcTonePlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvtcTonePlanRowStatus.setStatus("current")
_CvtcToneIdTable_Object = MibTable
cvtcToneIdTable = _CvtcToneIdTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 356, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cvtcToneIdTable.setStatus("current")
_CvtcToneIdEntry_Object = MibTableRow
cvtcToneIdEntry = _CvtcToneIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 356, 1, 1, 2, 1)
)
cvtcToneIdEntry.setIndexNames(
    (0, "CISCO-MEDIA-GATEWAY-MIB", "cmgwIndex"),
    (0, "CISCO-VOICE-TONE-CADENCE-MIB", "cvtcToneId"),
)
if mibBuilder.loadTexts:
    cvtcToneIdEntry.setStatus("current")


class _CvtcToneId_Type(Unsigned32):
    """Custom type cvtcToneId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CvtcToneId_Type.__name__ = "Unsigned32"
_CvtcToneId_Object = MibTableColumn
cvtcToneId = _CvtcToneId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 356, 1, 1, 2, 1, 1),
    _CvtcToneId_Type()
)
cvtcToneId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvtcToneId.setStatus("current")


class _CvtcToneName_Type(SnmpAdminString):
    """Custom type cvtcToneName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CvtcToneName_Type.__name__ = "SnmpAdminString"
_CvtcToneName_Object = MibTableColumn
cvtcToneName = _CvtcToneName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 356, 1, 1, 2, 1, 2),
    _CvtcToneName_Type()
)
cvtcToneName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvtcToneName.setStatus("current")
_CvtcToneIdRowStatus_Type = RowStatus
_CvtcToneIdRowStatus_Object = MibTableColumn
cvtcToneIdRowStatus = _CvtcToneIdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 356, 1, 1, 2, 1, 3),
    _CvtcToneIdRowStatus_Type()
)
cvtcToneIdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvtcToneIdRowStatus.setStatus("current")
_CvtcProgrammableToneTable_Object = MibTable
cvtcProgrammableToneTable = _CvtcProgrammableToneTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 356, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cvtcProgrammableToneTable.setStatus("current")
_CvtcProgrammableToneEntry_Object = MibTableRow
cvtcProgrammableToneEntry = _CvtcProgrammableToneEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 356, 1, 1, 3, 1)
)
cvtcProgrammableToneEntry.setIndexNames(
    (0, "CISCO-MEDIA-GATEWAY-MIB", "cmgwIndex"),
    (0, "CISCO-VOICE-TONE-CADENCE-MIB", "cvtcTonePlanId"),
    (0, "CISCO-VOICE-TONE-CADENCE-MIB", "cvtcToneId"),
)
if mibBuilder.loadTexts:
    cvtcProgrammableToneEntry.setStatus("current")
_CvtcProgrammableToneFrequency_Type = CToneFrequency
_CvtcProgrammableToneFrequency_Object = MibTableColumn
cvtcProgrammableToneFrequency = _CvtcProgrammableToneFrequency_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 356, 1, 1, 3, 1, 1),
    _CvtcProgrammableToneFrequency_Type()
)
cvtcProgrammableToneFrequency.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvtcProgrammableToneFrequency.setStatus("current")
_CvtcProgrammableToneAmplitude_Type = CToneAmplitude
_CvtcProgrammableToneAmplitude_Object = MibTableColumn
cvtcProgrammableToneAmplitude = _CvtcProgrammableToneAmplitude_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 356, 1, 1, 3, 1, 2),
    _CvtcProgrammableToneAmplitude_Type()
)
cvtcProgrammableToneAmplitude.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvtcProgrammableToneAmplitude.setStatus("current")
_CvtcProgrammableToneCadence_Type = CToneCadence
_CvtcProgrammableToneCadence_Object = MibTableColumn
cvtcProgrammableToneCadence = _CvtcProgrammableToneCadence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 356, 1, 1, 3, 1, 3),
    _CvtcProgrammableToneCadence_Type()
)
cvtcProgrammableToneCadence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvtcProgrammableToneCadence.setStatus("current")


class _CvtcProgrammableToneDuration_Type(Unsigned32):
    """Custom type cvtcProgrammableToneDuration based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CvtcProgrammableToneDuration_Type.__name__ = "Unsigned32"
_CvtcProgrammableToneDuration_Object = MibTableColumn
cvtcProgrammableToneDuration = _CvtcProgrammableToneDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 356, 1, 1, 3, 1, 4),
    _CvtcProgrammableToneDuration_Type()
)
cvtcProgrammableToneDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvtcProgrammableToneDuration.setStatus("current")
if mibBuilder.loadTexts:
    cvtcProgrammableToneDuration.setUnits("milliseconds")
_CvtcProgrammableToneStorageType_Type = StorageType
_CvtcProgrammableToneStorageType_Object = MibTableColumn
cvtcProgrammableToneStorageType = _CvtcProgrammableToneStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 356, 1, 1, 3, 1, 5),
    _CvtcProgrammableToneStorageType_Type()
)
cvtcProgrammableToneStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvtcProgrammableToneStorageType.setStatus("current")
_CvtcProgrammableToneRowStatus_Type = RowStatus
_CvtcProgrammableToneRowStatus_Object = MibTableColumn
cvtcProgrammableToneRowStatus = _CvtcProgrammableToneRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 356, 1, 1, 3, 1, 6),
    _CvtcProgrammableToneRowStatus_Type()
)
cvtcProgrammableToneRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvtcProgrammableToneRowStatus.setStatus("current")
_CiscoVoiceToneCadenceMIBConform_ObjectIdentity = ObjectIdentity
ciscoVoiceToneCadenceMIBConform = _CiscoVoiceToneCadenceMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 356, 3)
)
_CVoiceToneCadenceCompliances_ObjectIdentity = ObjectIdentity
cVoiceToneCadenceCompliances = _CVoiceToneCadenceCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 356, 3, 1)
)
_CVoiceToneCadenceGroups_ObjectIdentity = ObjectIdentity
cVoiceToneCadenceGroups = _CVoiceToneCadenceGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 356, 3, 2)
)

# Managed Objects groups

cvtcToneConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 356, 3, 2, 1)
)
cvtcToneConfigGroup.setObjects(
      *(("CISCO-VOICE-TONE-CADENCE-MIB", "cvtcTonePlanVifCount"),
        ("CISCO-VOICE-TONE-CADENCE-MIB", "cvtcTonePlanCountry"),
        ("CISCO-VOICE-TONE-CADENCE-MIB", "cvtcTonePlanVersion"),
        ("CISCO-VOICE-TONE-CADENCE-MIB", "cvtcTonePlanFileName"),
        ("CISCO-VOICE-TONE-CADENCE-MIB", "cvtcTonePlanStorageType"),
        ("CISCO-VOICE-TONE-CADENCE-MIB", "cvtcTonePlanRowStatus"),
        ("CISCO-VOICE-TONE-CADENCE-MIB", "cvtcToneName"),
        ("CISCO-VOICE-TONE-CADENCE-MIB", "cvtcToneIdRowStatus"),
        ("CISCO-VOICE-TONE-CADENCE-MIB", "cvtcProgrammableToneFrequency"),
        ("CISCO-VOICE-TONE-CADENCE-MIB", "cvtcProgrammableToneAmplitude"),
        ("CISCO-VOICE-TONE-CADENCE-MIB", "cvtcProgrammableToneCadence"),
        ("CISCO-VOICE-TONE-CADENCE-MIB", "cvtcProgrammableToneDuration"),
        ("CISCO-VOICE-TONE-CADENCE-MIB", "cvtcProgrammableToneStorageType"),
        ("CISCO-VOICE-TONE-CADENCE-MIB", "cvtcProgrammableToneRowStatus"))
)
if mibBuilder.loadTexts:
    cvtcToneConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cVoiceToneCadenceCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 356, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cVoiceToneCadenceCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-VOICE-TONE-CADENCE-MIB",
    **{"CToneFrequency": CToneFrequency,
       "CToneAmplitude": CToneAmplitude,
       "CToneCadence": CToneCadence,
       "ciscoVoiceToneCadenceMIB": ciscoVoiceToneCadenceMIB,
       "ciscoVoiceToneCadenceMIBNotifs": ciscoVoiceToneCadenceMIBNotifs,
       "ciscoVoiceToneCadenceMIBObjects": ciscoVoiceToneCadenceMIBObjects,
       "cVoiceToneCadenceConfig": cVoiceToneCadenceConfig,
       "cvtcTonePlanTable": cvtcTonePlanTable,
       "cvtcTonePlanEntry": cvtcTonePlanEntry,
       "cvtcTonePlanId": cvtcTonePlanId,
       "cvtcTonePlanVifCount": cvtcTonePlanVifCount,
       "cvtcTonePlanCountry": cvtcTonePlanCountry,
       "cvtcTonePlanVersion": cvtcTonePlanVersion,
       "cvtcTonePlanFileName": cvtcTonePlanFileName,
       "cvtcTonePlanStorageType": cvtcTonePlanStorageType,
       "cvtcTonePlanRowStatus": cvtcTonePlanRowStatus,
       "cvtcToneIdTable": cvtcToneIdTable,
       "cvtcToneIdEntry": cvtcToneIdEntry,
       "cvtcToneId": cvtcToneId,
       "cvtcToneName": cvtcToneName,
       "cvtcToneIdRowStatus": cvtcToneIdRowStatus,
       "cvtcProgrammableToneTable": cvtcProgrammableToneTable,
       "cvtcProgrammableToneEntry": cvtcProgrammableToneEntry,
       "cvtcProgrammableToneFrequency": cvtcProgrammableToneFrequency,
       "cvtcProgrammableToneAmplitude": cvtcProgrammableToneAmplitude,
       "cvtcProgrammableToneCadence": cvtcProgrammableToneCadence,
       "cvtcProgrammableToneDuration": cvtcProgrammableToneDuration,
       "cvtcProgrammableToneStorageType": cvtcProgrammableToneStorageType,
       "cvtcProgrammableToneRowStatus": cvtcProgrammableToneRowStatus,
       "ciscoVoiceToneCadenceMIBConform": ciscoVoiceToneCadenceMIBConform,
       "cVoiceToneCadenceCompliances": cVoiceToneCadenceCompliances,
       "cVoiceToneCadenceCompliance": cVoiceToneCadenceCompliance,
       "cVoiceToneCadenceGroups": cVoiceToneCadenceGroups,
       "cvtcToneConfigGroup": cvtcToneConfigGroup}
)
