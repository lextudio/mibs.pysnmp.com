# SNMP MIB module (CISCO-ENHANCED-IMAGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ENHANCED-IMAGE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:59:22 2024
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

(CeImageInstallableStatus,
 CeImageInstallableType) = mibBuilder.importSymbols(
    "CISCO-IMAGE-TC",
    "CeImageInstallableStatus",
    "CeImageInstallableType")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(PhysicalIndex,
 entPhysicalIndex) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndex",
    "entPhysicalIndex")

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

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoEnhancedImageMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 249)
)
ciscoEnhancedImageMIB.setRevisions(
        ("2005-01-06 00:00",
         "2002-02-28 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class MediaType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 3),
          ("ram", 1),
          ("rom", 2))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoEnhancedImageMIBObjects_ObjectIdentity = ObjectIdentity
ciscoEnhancedImageMIBObjects = _CiscoEnhancedImageMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 249, 1)
)
_CeImage_ObjectIdentity = ObjectIdentity
ceImage = _CeImage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 249, 1, 1)
)
_CeImageTable_Object = MibTable
ceImageTable = _CeImageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 249, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ceImageTable.setStatus("current")
_CeImageEntry_Object = MibTableRow
ceImageEntry = _CeImageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 249, 1, 1, 1, 1)
)
ceImageEntry.setIndexNames(
    (0, "CISCO-ENHANCED-IMAGE-MIB", "ceImageIndex"),
)
if mibBuilder.loadTexts:
    ceImageEntry.setStatus("current")
_CeImageIndex_Type = PhysicalIndex
_CeImageIndex_Object = MibTableColumn
ceImageIndex = _CeImageIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 249, 1, 1, 1, 1, 1),
    _CeImageIndex_Type()
)
ceImageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ceImageIndex.setStatus("current")
_CeImageName_Type = SnmpAdminString
_CeImageName_Object = MibTableColumn
ceImageName = _CeImageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 249, 1, 1, 1, 1, 2),
    _CeImageName_Type()
)
ceImageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceImageName.setStatus("current")
_CeImageFamily_Type = SnmpAdminString
_CeImageFamily_Object = MibTableColumn
ceImageFamily = _CeImageFamily_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 249, 1, 1, 1, 1, 3),
    _CeImageFamily_Type()
)
ceImageFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceImageFamily.setStatus("current")
_CeImageFeature_Type = SnmpAdminString
_CeImageFeature_Object = MibTableColumn
ceImageFeature = _CeImageFeature_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 249, 1, 1, 1, 1, 4),
    _CeImageFeature_Type()
)
ceImageFeature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceImageFeature.setStatus("current")
_CeImageVersion_Type = SnmpAdminString
_CeImageVersion_Object = MibTableColumn
ceImageVersion = _CeImageVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 249, 1, 1, 1, 1, 5),
    _CeImageVersion_Type()
)
ceImageVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceImageVersion.setStatus("current")
_CeImageMedia_Type = MediaType
_CeImageMedia_Object = MibTableColumn
ceImageMedia = _CeImageMedia_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 249, 1, 1, 1, 1, 6),
    _CeImageMedia_Type()
)
ceImageMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceImageMedia.setStatus("current")
_CeImageDescription_Type = SnmpAdminString
_CeImageDescription_Object = MibTableColumn
ceImageDescription = _CeImageDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 249, 1, 1, 1, 1, 7),
    _CeImageDescription_Type()
)
ceImageDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceImageDescription.setStatus("current")
_CeImageInstallable_ObjectIdentity = ObjectIdentity
ceImageInstallable = _CeImageInstallable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 249, 1, 2)
)
_CeImageLocationTable_Object = MibTable
ceImageLocationTable = _CeImageLocationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 249, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ceImageLocationTable.setStatus("current")
_CeImageLocationEntry_Object = MibTableRow
ceImageLocationEntry = _CeImageLocationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 249, 1, 2, 1, 1)
)
ceImageLocationEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-ENHANCED-IMAGE-MIB", "ceImageLocationIndex"),
)
if mibBuilder.loadTexts:
    ceImageLocationEntry.setStatus("current")
_CeImageLocationIndex_Type = Unsigned32
_CeImageLocationIndex_Object = MibTableColumn
ceImageLocationIndex = _CeImageLocationIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 249, 1, 2, 1, 1, 1),
    _CeImageLocationIndex_Type()
)
ceImageLocationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ceImageLocationIndex.setStatus("current")
_CeImageLocation_Type = SnmpAdminString
_CeImageLocation_Object = MibTableColumn
ceImageLocation = _CeImageLocation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 249, 1, 2, 1, 1, 2),
    _CeImageLocation_Type()
)
ceImageLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceImageLocation.setStatus("current")
_CeImageLocationRunningStatus_Type = TruthValue
_CeImageLocationRunningStatus_Object = MibTableColumn
ceImageLocationRunningStatus = _CeImageLocationRunningStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 249, 1, 2, 1, 1, 3),
    _CeImageLocationRunningStatus_Type()
)
ceImageLocationRunningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceImageLocationRunningStatus.setStatus("current")
_CeImageInstallableTable_Object = MibTable
ceImageInstallableTable = _CeImageInstallableTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 249, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ceImageInstallableTable.setStatus("current")
_CeImageInstallableEntry_Object = MibTableRow
ceImageInstallableEntry = _CeImageInstallableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 249, 1, 2, 2, 1)
)
ceImageInstallableEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-ENHANCED-IMAGE-MIB", "ceImageLocationIndex"),
    (0, "CISCO-ENHANCED-IMAGE-MIB", "ceImageInstallableIndex"),
)
if mibBuilder.loadTexts:
    ceImageInstallableEntry.setStatus("current")
_CeImageInstallableIndex_Type = Unsigned32
_CeImageInstallableIndex_Object = MibTableColumn
ceImageInstallableIndex = _CeImageInstallableIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 249, 1, 2, 2, 1, 1),
    _CeImageInstallableIndex_Type()
)
ceImageInstallableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ceImageInstallableIndex.setStatus("current")
_CeImageInstallableType_Type = CeImageInstallableType
_CeImageInstallableType_Object = MibTableColumn
ceImageInstallableType = _CeImageInstallableType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 249, 1, 2, 2, 1, 2),
    _CeImageInstallableType_Type()
)
ceImageInstallableType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ceImageInstallableType.setStatus("current")
_CeImageInstallableName_Type = SnmpAdminString
_CeImageInstallableName_Object = MibTableColumn
ceImageInstallableName = _CeImageInstallableName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 249, 1, 2, 2, 1, 3),
    _CeImageInstallableName_Type()
)
ceImageInstallableName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ceImageInstallableName.setStatus("current")
_CeImageInstallableStatus_Type = CeImageInstallableStatus
_CeImageInstallableStatus_Object = MibTableColumn
ceImageInstallableStatus = _CeImageInstallableStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 249, 1, 2, 2, 1, 4),
    _CeImageInstallableStatus_Type()
)
ceImageInstallableStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ceImageInstallableStatus.setStatus("current")
_CeImageInstallableMajorVerNumber_Type = Unsigned32
_CeImageInstallableMajorVerNumber_Object = MibTableColumn
ceImageInstallableMajorVerNumber = _CeImageInstallableMajorVerNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 249, 1, 2, 2, 1, 5),
    _CeImageInstallableMajorVerNumber_Type()
)
ceImageInstallableMajorVerNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceImageInstallableMajorVerNumber.setStatus("current")
_CeImageInstallableMinorVerNumber_Type = Unsigned32
_CeImageInstallableMinorVerNumber_Object = MibTableColumn
ceImageInstallableMinorVerNumber = _CeImageInstallableMinorVerNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 249, 1, 2, 2, 1, 6),
    _CeImageInstallableMinorVerNumber_Type()
)
ceImageInstallableMinorVerNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceImageInstallableMinorVerNumber.setStatus("current")
_CeImageInstallableRevisionVerNum_Type = SnmpAdminString
_CeImageInstallableRevisionVerNum_Object = MibTableColumn
ceImageInstallableRevisionVerNum = _CeImageInstallableRevisionVerNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 249, 1, 2, 2, 1, 7),
    _CeImageInstallableRevisionVerNum_Type()
)
ceImageInstallableRevisionVerNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceImageInstallableRevisionVerNum.setStatus("current")
_CeImageInstallableDate_Type = DateAndTime
_CeImageInstallableDate_Object = MibTableColumn
ceImageInstallableDate = _CeImageInstallableDate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 249, 1, 2, 2, 1, 8),
    _CeImageInstallableDate_Type()
)
ceImageInstallableDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceImageInstallableDate.setStatus("current")
_CeImageInstallableRowStatus_Type = RowStatus
_CeImageInstallableRowStatus_Object = MibTableColumn
ceImageInstallableRowStatus = _CeImageInstallableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 249, 1, 2, 2, 1, 9),
    _CeImageInstallableRowStatus_Type()
)
ceImageInstallableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ceImageInstallableRowStatus.setStatus("current")
_CeImageTags_ObjectIdentity = ObjectIdentity
ceImageTags = _CeImageTags_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 249, 1, 3)
)
_CeImageTagTable_Object = MibTable
ceImageTagTable = _CeImageTagTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 249, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ceImageTagTable.setStatus("current")
_CeImageTagEntry_Object = MibTableRow
ceImageTagEntry = _CeImageTagEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 249, 1, 3, 1, 1)
)
ceImageTagEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-ENHANCED-IMAGE-MIB", "ceImageLocationIndex"),
    (0, "CISCO-ENHANCED-IMAGE-MIB", "ceImageTagName"),
)
if mibBuilder.loadTexts:
    ceImageTagEntry.setStatus("current")
_CeImageTagName_Type = SnmpAdminString
_CeImageTagName_Object = MibTableColumn
ceImageTagName = _CeImageTagName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 249, 1, 3, 1, 1, 1),
    _CeImageTagName_Type()
)
ceImageTagName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ceImageTagName.setStatus("current")
_CeImageTagListofInstIndex_Type = SnmpAdminString
_CeImageTagListofInstIndex_Object = MibTableColumn
ceImageTagListofInstIndex = _CeImageTagListofInstIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 249, 1, 3, 1, 1, 2),
    _CeImageTagListofInstIndex_Type()
)
ceImageTagListofInstIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceImageTagListofInstIndex.setStatus("current")
_CeImageTagDate_Type = DateAndTime
_CeImageTagDate_Object = MibTableColumn
ceImageTagDate = _CeImageTagDate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 249, 1, 3, 1, 1, 3),
    _CeImageTagDate_Type()
)
ceImageTagDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceImageTagDate.setStatus("current")
_CeImageTagRowStatus_Type = RowStatus
_CeImageTagRowStatus_Object = MibTableColumn
ceImageTagRowStatus = _CeImageTagRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 249, 1, 3, 1, 1, 4),
    _CeImageTagRowStatus_Type()
)
ceImageTagRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ceImageTagRowStatus.setStatus("current")
_CiscoEnhancedImageMIBConformance_ObjectIdentity = ObjectIdentity
ciscoEnhancedImageMIBConformance = _CiscoEnhancedImageMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 249, 3)
)
_CiscoEnhancedImageMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoEnhancedImageMIBCompliances = _CiscoEnhancedImageMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 249, 3, 1)
)
_CiscoEnhancedImageMIBGroups_ObjectIdentity = ObjectIdentity
ciscoEnhancedImageMIBGroups = _CiscoEnhancedImageMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 249, 3, 2)
)

# Managed Objects groups

ciscoEnhancedImageMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 249, 3, 2, 1)
)
ciscoEnhancedImageMIBGroup.setObjects(
      *(("CISCO-ENHANCED-IMAGE-MIB", "ceImageName"),
        ("CISCO-ENHANCED-IMAGE-MIB", "ceImageFamily"),
        ("CISCO-ENHANCED-IMAGE-MIB", "ceImageFeature"),
        ("CISCO-ENHANCED-IMAGE-MIB", "ceImageVersion"),
        ("CISCO-ENHANCED-IMAGE-MIB", "ceImageMedia"),
        ("CISCO-ENHANCED-IMAGE-MIB", "ceImageDescription"))
)
if mibBuilder.loadTexts:
    ciscoEnhancedImageMIBGroup.setStatus("current")

ceImageLocationMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 249, 3, 2, 2)
)
ceImageLocationMIBGroup.setObjects(
      *(("CISCO-ENHANCED-IMAGE-MIB", "ceImageLocation"),
        ("CISCO-ENHANCED-IMAGE-MIB", "ceImageLocationRunningStatus"))
)
if mibBuilder.loadTexts:
    ceImageLocationMIBGroup.setStatus("current")

ceImageInstallableMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 249, 3, 2, 3)
)
ceImageInstallableMIBGroup.setObjects(
      *(("CISCO-ENHANCED-IMAGE-MIB", "ceImageInstallableType"),
        ("CISCO-ENHANCED-IMAGE-MIB", "ceImageInstallableName"),
        ("CISCO-ENHANCED-IMAGE-MIB", "ceImageInstallableStatus"),
        ("CISCO-ENHANCED-IMAGE-MIB", "ceImageInstallableMajorVerNumber"),
        ("CISCO-ENHANCED-IMAGE-MIB", "ceImageInstallableMinorVerNumber"),
        ("CISCO-ENHANCED-IMAGE-MIB", "ceImageInstallableRevisionVerNum"),
        ("CISCO-ENHANCED-IMAGE-MIB", "ceImageInstallableDate"),
        ("CISCO-ENHANCED-IMAGE-MIB", "ceImageInstallableRowStatus"))
)
if mibBuilder.loadTexts:
    ceImageInstallableMIBGroup.setStatus("current")

ceImageTagMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 249, 3, 2, 4)
)
ceImageTagMIBGroup.setObjects(
      *(("CISCO-ENHANCED-IMAGE-MIB", "ceImageTagListofInstIndex"),
        ("CISCO-ENHANCED-IMAGE-MIB", "ceImageTagDate"),
        ("CISCO-ENHANCED-IMAGE-MIB", "ceImageTagRowStatus"))
)
if mibBuilder.loadTexts:
    ceImageTagMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoEnhancedImageMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 249, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoEnhancedImageMIBCompliance.setStatus(
        "deprecated"
    )

ceImageMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 249, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ceImageMIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ENHANCED-IMAGE-MIB",
    **{"MediaType": MediaType,
       "ciscoEnhancedImageMIB": ciscoEnhancedImageMIB,
       "ciscoEnhancedImageMIBObjects": ciscoEnhancedImageMIBObjects,
       "ceImage": ceImage,
       "ceImageTable": ceImageTable,
       "ceImageEntry": ceImageEntry,
       "ceImageIndex": ceImageIndex,
       "ceImageName": ceImageName,
       "ceImageFamily": ceImageFamily,
       "ceImageFeature": ceImageFeature,
       "ceImageVersion": ceImageVersion,
       "ceImageMedia": ceImageMedia,
       "ceImageDescription": ceImageDescription,
       "ceImageInstallable": ceImageInstallable,
       "ceImageLocationTable": ceImageLocationTable,
       "ceImageLocationEntry": ceImageLocationEntry,
       "ceImageLocationIndex": ceImageLocationIndex,
       "ceImageLocation": ceImageLocation,
       "ceImageLocationRunningStatus": ceImageLocationRunningStatus,
       "ceImageInstallableTable": ceImageInstallableTable,
       "ceImageInstallableEntry": ceImageInstallableEntry,
       "ceImageInstallableIndex": ceImageInstallableIndex,
       "ceImageInstallableType": ceImageInstallableType,
       "ceImageInstallableName": ceImageInstallableName,
       "ceImageInstallableStatus": ceImageInstallableStatus,
       "ceImageInstallableMajorVerNumber": ceImageInstallableMajorVerNumber,
       "ceImageInstallableMinorVerNumber": ceImageInstallableMinorVerNumber,
       "ceImageInstallableRevisionVerNum": ceImageInstallableRevisionVerNum,
       "ceImageInstallableDate": ceImageInstallableDate,
       "ceImageInstallableRowStatus": ceImageInstallableRowStatus,
       "ceImageTags": ceImageTags,
       "ceImageTagTable": ceImageTagTable,
       "ceImageTagEntry": ceImageTagEntry,
       "ceImageTagName": ceImageTagName,
       "ceImageTagListofInstIndex": ceImageTagListofInstIndex,
       "ceImageTagDate": ceImageTagDate,
       "ceImageTagRowStatus": ceImageTagRowStatus,
       "ciscoEnhancedImageMIBConformance": ciscoEnhancedImageMIBConformance,
       "ciscoEnhancedImageMIBCompliances": ciscoEnhancedImageMIBCompliances,
       "ciscoEnhancedImageMIBCompliance": ciscoEnhancedImageMIBCompliance,
       "ceImageMIBComplianceRev1": ceImageMIBComplianceRev1,
       "ciscoEnhancedImageMIBGroups": ciscoEnhancedImageMIBGroups,
       "ciscoEnhancedImageMIBGroup": ciscoEnhancedImageMIBGroup,
       "ceImageLocationMIBGroup": ceImageLocationMIBGroup,
       "ceImageInstallableMIBGroup": ceImageInstallableMIBGroup,
       "ceImageTagMIBGroup": ceImageTagMIBGroup}
)
