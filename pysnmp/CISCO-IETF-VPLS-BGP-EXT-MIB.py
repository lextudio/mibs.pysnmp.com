# SNMP MIB module (CISCO-IETF-VPLS-BGP-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IETF-VPLS-BGP-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:02:04 2024
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

(cvplsConfigIndex,
 cvplsPwBindIndex) = mibBuilder.importSymbols(
    "CISCO-IETF-VPLS-GENERIC-MIB",
    "cvplsConfigIndex",
    "cvplsPwBindIndex")

(ciscoExperiment,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoExperiment")

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

ciscoIetfVplsBgpExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 140)
)
ciscoIetfVplsBgpExtMIB.setRevisions(
        ("2008-10-24 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CiVplsBgpExtRouteDistinguisher(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class CiVplsBgpExtRouteTarget(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class CiVplsBgpExtRouteTargetType(Integer32, TextualConvention):
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
        *(("both", 3),
          ("export", 2),
          ("import", 1))
    )



class CiVplsBgpExtVEID(Unsigned32, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_CiscoIetfVplsBgpExtMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoIetfVplsBgpExtMIBNotifs = _CiscoIetfVplsBgpExtMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 140, 0)
)
_CiscoIetfVplsBgpExtMIBObjects_ObjectIdentity = ObjectIdentity
ciscoIetfVplsBgpExtMIBObjects = _CiscoIetfVplsBgpExtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 140, 1)
)
_CiVplsBgpExtConfigTable_Object = MibTable
ciVplsBgpExtConfigTable = _CiVplsBgpExtConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 1)
)
if mibBuilder.loadTexts:
    ciVplsBgpExtConfigTable.setStatus("current")
_CiVplsBgpExtConfigEntry_Object = MibTableRow
ciVplsBgpExtConfigEntry = _CiVplsBgpExtConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 1, 1)
)
ciVplsBgpExtConfigEntry.setIndexNames(
    (0, "CISCO-IETF-VPLS-GENERIC-MIB", "cvplsConfigIndex"),
)
if mibBuilder.loadTexts:
    ciVplsBgpExtConfigEntry.setStatus("current")
_CiVplsBgpExtConfigRouteDistinguisher_Type = CiVplsBgpExtRouteDistinguisher
_CiVplsBgpExtConfigRouteDistinguisher_Object = MibTableColumn
ciVplsBgpExtConfigRouteDistinguisher = _CiVplsBgpExtConfigRouteDistinguisher_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 1, 1, 1),
    _CiVplsBgpExtConfigRouteDistinguisher_Type()
)
ciVplsBgpExtConfigRouteDistinguisher.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciVplsBgpExtConfigRouteDistinguisher.setStatus("current")


class _CiVplsBgpExtConfigVERangeSize_Type(Unsigned32):
    """Custom type ciVplsBgpExtConfigVERangeSize based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CiVplsBgpExtConfigVERangeSize_Type.__name__ = "Unsigned32"
_CiVplsBgpExtConfigVERangeSize_Object = MibTableColumn
ciVplsBgpExtConfigVERangeSize = _CiVplsBgpExtConfigVERangeSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 1, 1, 4),
    _CiVplsBgpExtConfigVERangeSize_Type()
)
ciVplsBgpExtConfigVERangeSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciVplsBgpExtConfigVERangeSize.setStatus("current")
_CivplsBgpExtRTTable_Object = MibTable
civplsBgpExtRTTable = _CivplsBgpExtRTTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 2)
)
if mibBuilder.loadTexts:
    civplsBgpExtRTTable.setStatus("current")
_CivplsBgpExtRTEntry_Object = MibTableRow
civplsBgpExtRTEntry = _CivplsBgpExtRTEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 2, 1)
)
civplsBgpExtRTEntry.setIndexNames(
    (0, "CISCO-IETF-VPLS-GENERIC-MIB", "cvplsConfigIndex"),
    (0, "CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtRTType"),
    (0, "CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtRT"),
)
if mibBuilder.loadTexts:
    civplsBgpExtRTEntry.setStatus("current")
_CiVplsBgpExtRTType_Type = CiVplsBgpExtRouteTargetType
_CiVplsBgpExtRTType_Object = MibTableColumn
ciVplsBgpExtRTType = _CiVplsBgpExtRTType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 2, 1, 1),
    _CiVplsBgpExtRTType_Type()
)
ciVplsBgpExtRTType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciVplsBgpExtRTType.setStatus("current")


class _CiVplsBgpExtRT_Type(CiVplsBgpExtRouteTarget):
    """Custom type ciVplsBgpExtRT based on CiVplsBgpExtRouteTarget"""
    subtypeSpec = CiVplsBgpExtRouteTarget.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CiVplsBgpExtRT_Type.__name__ = "CiVplsBgpExtRouteTarget"
_CiVplsBgpExtRT_Object = MibTableColumn
ciVplsBgpExtRT = _CiVplsBgpExtRT_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 2, 1, 2),
    _CiVplsBgpExtRT_Type()
)
ciVplsBgpExtRT.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciVplsBgpExtRT.setStatus("current")


class _CiVplsBgpExtRTStorageType_Type(StorageType):
    """Custom type ciVplsBgpExtRTStorageType based on StorageType"""


_CiVplsBgpExtRTStorageType_Object = MibTableColumn
ciVplsBgpExtRTStorageType = _CiVplsBgpExtRTStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 2, 1, 3),
    _CiVplsBgpExtRTStorageType_Type()
)
ciVplsBgpExtRTStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciVplsBgpExtRTStorageType.setStatus("current")
_CiVplsBgpExtRTRowStatus_Type = RowStatus
_CiVplsBgpExtRTRowStatus_Object = MibTableColumn
ciVplsBgpExtRTRowStatus = _CiVplsBgpExtRTRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 2, 1, 4),
    _CiVplsBgpExtRTRowStatus_Type()
)
ciVplsBgpExtRTRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciVplsBgpExtRTRowStatus.setStatus("current")
_CiVplsBgpExtVETable_Object = MibTable
ciVplsBgpExtVETable = _CiVplsBgpExtVETable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 3)
)
if mibBuilder.loadTexts:
    ciVplsBgpExtVETable.setStatus("current")
_CiVplsBgpExtVEEntry_Object = MibTableRow
ciVplsBgpExtVEEntry = _CiVplsBgpExtVEEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 3, 1)
)
ciVplsBgpExtVEEntry.setIndexNames(
    (0, "CISCO-IETF-VPLS-GENERIC-MIB", "cvplsConfigIndex"),
    (0, "CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtVEId"),
)
if mibBuilder.loadTexts:
    ciVplsBgpExtVEEntry.setStatus("current")
_CiVplsBgpExtVEId_Type = CiVplsBgpExtVEID
_CiVplsBgpExtVEId_Object = MibTableColumn
ciVplsBgpExtVEId = _CiVplsBgpExtVEId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 3, 1, 1),
    _CiVplsBgpExtVEId_Type()
)
ciVplsBgpExtVEId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciVplsBgpExtVEId.setStatus("current")
_CiVplsBgpExtVEName_Type = SnmpAdminString
_CiVplsBgpExtVEName_Object = MibTableColumn
ciVplsBgpExtVEName = _CiVplsBgpExtVEName_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 3, 1, 2),
    _CiVplsBgpExtVEName_Type()
)
ciVplsBgpExtVEName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciVplsBgpExtVEName.setStatus("current")


class _CiVplsBgpExtVEPreference_Type(Unsigned32):
    """Custom type ciVplsBgpExtVEPreference based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CiVplsBgpExtVEPreference_Type.__name__ = "Unsigned32"
_CiVplsBgpExtVEPreference_Object = MibTableColumn
ciVplsBgpExtVEPreference = _CiVplsBgpExtVEPreference_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 3, 1, 3),
    _CiVplsBgpExtVEPreference_Type()
)
ciVplsBgpExtVEPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciVplsBgpExtVEPreference.setStatus("current")


class _CiVplsBgpExtVEStorageType_Type(StorageType):
    """Custom type ciVplsBgpExtVEStorageType based on StorageType"""


_CiVplsBgpExtVEStorageType_Object = MibTableColumn
ciVplsBgpExtVEStorageType = _CiVplsBgpExtVEStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 3, 1, 5),
    _CiVplsBgpExtVEStorageType_Type()
)
ciVplsBgpExtVEStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciVplsBgpExtVEStorageType.setStatus("current")
_CiVplsBgpExtVERowStatus_Type = RowStatus
_CiVplsBgpExtVERowStatus_Object = MibTableColumn
ciVplsBgpExtVERowStatus = _CiVplsBgpExtVERowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 3, 1, 6),
    _CiVplsBgpExtVERowStatus_Type()
)
ciVplsBgpExtVERowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciVplsBgpExtVERowStatus.setStatus("current")
_CiVplsBgpExtPwBindTable_Object = MibTable
ciVplsBgpExtPwBindTable = _CiVplsBgpExtPwBindTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 4)
)
if mibBuilder.loadTexts:
    ciVplsBgpExtPwBindTable.setStatus("current")
_CiVplsBgpExtPwBindEntry_Object = MibTableRow
ciVplsBgpExtPwBindEntry = _CiVplsBgpExtPwBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 4, 1)
)
ciVplsBgpExtPwBindEntry.setIndexNames(
    (0, "CISCO-IETF-VPLS-GENERIC-MIB", "cvplsConfigIndex"),
    (0, "CISCO-IETF-VPLS-GENERIC-MIB", "cvplsPwBindIndex"),
)
if mibBuilder.loadTexts:
    ciVplsBgpExtPwBindEntry.setStatus("current")
_CiVplsBgpExtPwBindLocalVEId_Type = CiVplsBgpExtVEID
_CiVplsBgpExtPwBindLocalVEId_Object = MibTableColumn
ciVplsBgpExtPwBindLocalVEId = _CiVplsBgpExtPwBindLocalVEId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 4, 1, 1),
    _CiVplsBgpExtPwBindLocalVEId_Type()
)
ciVplsBgpExtPwBindLocalVEId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciVplsBgpExtPwBindLocalVEId.setStatus("current")
_CiVplsBgpExtPwBindRemoteVEId_Type = CiVplsBgpExtVEID
_CiVplsBgpExtPwBindRemoteVEId_Object = MibTableColumn
ciVplsBgpExtPwBindRemoteVEId = _CiVplsBgpExtPwBindRemoteVEId_Object(
    (1, 3, 6, 1, 4, 1, 9, 10, 140, 1, 4, 1, 2),
    _CiVplsBgpExtPwBindRemoteVEId_Type()
)
ciVplsBgpExtPwBindRemoteVEId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciVplsBgpExtPwBindRemoteVEId.setStatus("current")
_CiscoIetfVplsBgpExtMIBConform_ObjectIdentity = ObjectIdentity
ciscoIetfVplsBgpExtMIBConform = _CiscoIetfVplsBgpExtMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 140, 2)
)
_CiscoIetfVplsBgpExtMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoIetfVplsBgpExtMIBCompliances = _CiscoIetfVplsBgpExtMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 140, 2, 1)
)
_CiscoIetfVplsBgpExtMIBGroups_ObjectIdentity = ObjectIdentity
ciscoIetfVplsBgpExtMIBGroups = _CiscoIetfVplsBgpExtMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 10, 140, 2, 2)
)

# Managed Objects groups

ciVplsBgpExtConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 140, 2, 2, 1)
)
ciVplsBgpExtConfigGroup.setObjects(
      *(("CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtConfigRouteDistinguisher"),
        ("CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtConfigVERangeSize"))
)
if mibBuilder.loadTexts:
    ciVplsBgpExtConfigGroup.setStatus("current")

ciVplsBgpExtRTGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 140, 2, 2, 2)
)
ciVplsBgpExtRTGroup.setObjects(
      *(("CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtRTType"),
        ("CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtRT"),
        ("CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtRTStorageType"),
        ("CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtRTRowStatus"))
)
if mibBuilder.loadTexts:
    ciVplsBgpExtRTGroup.setStatus("current")

ciVplsBgpExtVEGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 140, 2, 2, 3)
)
ciVplsBgpExtVEGroup.setObjects(
      *(("CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtVEName"),
        ("CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtVEPreference"),
        ("CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtVERowStatus"),
        ("CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtVEStorageType"))
)
if mibBuilder.loadTexts:
    ciVplsBgpExtVEGroup.setStatus("current")

ciVplsBgpExtPwBindGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 10, 140, 2, 2, 4)
)
ciVplsBgpExtPwBindGroup.setObjects(
      *(("CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtPwBindLocalVEId"),
        ("CISCO-IETF-VPLS-BGP-EXT-MIB", "ciVplsBgpExtPwBindRemoteVEId"))
)
if mibBuilder.loadTexts:
    ciVplsBgpExtPwBindGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoIetfVplsBgpExtMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 10, 140, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoIetfVplsBgpExtMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IETF-VPLS-BGP-EXT-MIB",
    **{"CiVplsBgpExtRouteDistinguisher": CiVplsBgpExtRouteDistinguisher,
       "CiVplsBgpExtRouteTarget": CiVplsBgpExtRouteTarget,
       "CiVplsBgpExtRouteTargetType": CiVplsBgpExtRouteTargetType,
       "CiVplsBgpExtVEID": CiVplsBgpExtVEID,
       "ciscoIetfVplsBgpExtMIB": ciscoIetfVplsBgpExtMIB,
       "ciscoIetfVplsBgpExtMIBNotifs": ciscoIetfVplsBgpExtMIBNotifs,
       "ciscoIetfVplsBgpExtMIBObjects": ciscoIetfVplsBgpExtMIBObjects,
       "ciVplsBgpExtConfigTable": ciVplsBgpExtConfigTable,
       "ciVplsBgpExtConfigEntry": ciVplsBgpExtConfigEntry,
       "ciVplsBgpExtConfigRouteDistinguisher": ciVplsBgpExtConfigRouteDistinguisher,
       "ciVplsBgpExtConfigVERangeSize": ciVplsBgpExtConfigVERangeSize,
       "civplsBgpExtRTTable": civplsBgpExtRTTable,
       "civplsBgpExtRTEntry": civplsBgpExtRTEntry,
       "ciVplsBgpExtRTType": ciVplsBgpExtRTType,
       "ciVplsBgpExtRT": ciVplsBgpExtRT,
       "ciVplsBgpExtRTStorageType": ciVplsBgpExtRTStorageType,
       "ciVplsBgpExtRTRowStatus": ciVplsBgpExtRTRowStatus,
       "ciVplsBgpExtVETable": ciVplsBgpExtVETable,
       "ciVplsBgpExtVEEntry": ciVplsBgpExtVEEntry,
       "ciVplsBgpExtVEId": ciVplsBgpExtVEId,
       "ciVplsBgpExtVEName": ciVplsBgpExtVEName,
       "ciVplsBgpExtVEPreference": ciVplsBgpExtVEPreference,
       "ciVplsBgpExtVEStorageType": ciVplsBgpExtVEStorageType,
       "ciVplsBgpExtVERowStatus": ciVplsBgpExtVERowStatus,
       "ciVplsBgpExtPwBindTable": ciVplsBgpExtPwBindTable,
       "ciVplsBgpExtPwBindEntry": ciVplsBgpExtPwBindEntry,
       "ciVplsBgpExtPwBindLocalVEId": ciVplsBgpExtPwBindLocalVEId,
       "ciVplsBgpExtPwBindRemoteVEId": ciVplsBgpExtPwBindRemoteVEId,
       "ciscoIetfVplsBgpExtMIBConform": ciscoIetfVplsBgpExtMIBConform,
       "ciscoIetfVplsBgpExtMIBCompliances": ciscoIetfVplsBgpExtMIBCompliances,
       "ciscoIetfVplsBgpExtMIBCompliance": ciscoIetfVplsBgpExtMIBCompliance,
       "ciscoIetfVplsBgpExtMIBGroups": ciscoIetfVplsBgpExtMIBGroups,
       "ciVplsBgpExtConfigGroup": ciVplsBgpExtConfigGroup,
       "ciVplsBgpExtRTGroup": ciVplsBgpExtRTGroup,
       "ciVplsBgpExtVEGroup": ciVplsBgpExtVEGroup,
       "ciVplsBgpExtPwBindGroup": ciVplsBgpExtPwBindGroup}
)
