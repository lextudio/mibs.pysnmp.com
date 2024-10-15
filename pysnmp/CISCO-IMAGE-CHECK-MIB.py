# SNMP MIB module (CISCO-IMAGE-CHECK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IMAGE-CHECK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:02:25 2024
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ciscoImageCheckMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99990)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoImageCheckMIBObjects_ObjectIdentity = ObjectIdentity
ciscoImageCheckMIBObjects = _CiscoImageCheckMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99990, 1)
)
_CiscoImageCheck_ObjectIdentity = ObjectIdentity
ciscoImageCheck = _CiscoImageCheck_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99990, 1, 1)
)
_CiscoImageCheckOpTable_Object = MibTable
ciscoImageCheckOpTable = _CiscoImageCheckOpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99990, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoImageCheckOpTable.setStatus("current")
_CiscoImageCheckOpEntry_Object = MibTableRow
ciscoImageCheckOpEntry = _CiscoImageCheckOpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99990, 1, 1, 1, 1)
)
ciscoImageCheckOpEntry.setIndexNames(
    (0, "CISCO-IMAGE-CHECK-MIB", "ciscoImageCheckSerialNum"),
)
if mibBuilder.loadTexts:
    ciscoImageCheckOpEntry.setStatus("current")


class _CiscoImageCheckSerialNum_Type(Integer32):
    """Custom type ciscoImageCheckSerialNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CiscoImageCheckSerialNum_Type.__name__ = "Integer32"
_CiscoImageCheckSerialNum_Object = MibTableColumn
ciscoImageCheckSerialNum = _CiscoImageCheckSerialNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99990, 1, 1, 1, 1, 1),
    _CiscoImageCheckSerialNum_Type()
)
ciscoImageCheckSerialNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoImageCheckSerialNum.setStatus("current")


class _CiscoImageCheckImageName_Type(SnmpAdminString):
    """Custom type ciscoImageCheckImageName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CiscoImageCheckImageName_Type.__name__ = "SnmpAdminString"
_CiscoImageCheckImageName_Object = MibTableColumn
ciscoImageCheckImageName = _CiscoImageCheckImageName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99990, 1, 1, 1, 1, 2),
    _CiscoImageCheckImageName_Type()
)
ciscoImageCheckImageName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoImageCheckImageName.setStatus("current")


class _CiscoImageCheckStatus_Type(Integer32):
    """Custom type ciscoImageCheckStatus based on Integer32"""
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
        *(("compatible", 5),
          ("extractFail", 8),
          ("fileParseErr", 9),
          ("getIncompatErr", 10),
          ("inCompatLoose", 3),
          ("inCompatStrict", 4),
          ("inProgress", 2),
          ("noStandby", 6),
          ("none", 1),
          ("pssErr", 7))
    )


_CiscoImageCheckStatus_Type.__name__ = "Integer32"
_CiscoImageCheckStatus_Object = MibTableColumn
ciscoImageCheckStatus = _CiscoImageCheckStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99990, 1, 1, 1, 1, 3),
    _CiscoImageCheckStatus_Type()
)
ciscoImageCheckStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoImageCheckStatus.setStatus("current")
_CiscoImageCheckEntryStatus_Type = RowStatus
_CiscoImageCheckEntryStatus_Object = MibTableColumn
ciscoImageCheckEntryStatus = _CiscoImageCheckEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99990, 1, 1, 1, 1, 4),
    _CiscoImageCheckEntryStatus_Type()
)
ciscoImageCheckEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ciscoImageCheckEntryStatus.setStatus("current")
_CiscoImgChkResultsTable_Object = MibTable
ciscoImgChkResultsTable = _CiscoImgChkResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99990, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoImgChkResultsTable.setStatus("current")
_CiscoImgChkResultsEntry_Object = MibTableRow
ciscoImgChkResultsEntry = _CiscoImgChkResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99990, 1, 1, 2, 1)
)
ciscoImgChkResultsEntry.setIndexNames(
    (0, "CISCO-IMAGE-CHECK-MIB", "ciscoImageCheckSerialNum"),
    (0, "CISCO-IMAGE-CHECK-MIB", "ciscoImgChkFeatureIndex"),
    (0, "CISCO-IMAGE-CHECK-MIB", "ciscoImgChkCapabIndex"),
)
if mibBuilder.loadTexts:
    ciscoImgChkResultsEntry.setStatus("current")


class _CiscoImgChkFeatureIndex_Type(Integer32):
    """Custom type ciscoImgChkFeatureIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CiscoImgChkFeatureIndex_Type.__name__ = "Integer32"
_CiscoImgChkFeatureIndex_Object = MibTableColumn
ciscoImgChkFeatureIndex = _CiscoImgChkFeatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99990, 1, 1, 2, 1, 1),
    _CiscoImgChkFeatureIndex_Type()
)
ciscoImgChkFeatureIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoImgChkFeatureIndex.setStatus("current")


class _CiscoImgChkCapabIndex_Type(Integer32):
    """Custom type ciscoImgChkCapabIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CiscoImgChkCapabIndex_Type.__name__ = "Integer32"
_CiscoImgChkCapabIndex_Object = MibTableColumn
ciscoImgChkCapabIndex = _CiscoImgChkCapabIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99990, 1, 1, 2, 1, 2),
    _CiscoImgChkCapabIndex_Type()
)
ciscoImgChkCapabIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoImgChkCapabIndex.setStatus("current")


class _CiscoImgChkFeatureName_Type(SnmpAdminString):
    """Custom type ciscoImgChkFeatureName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CiscoImgChkFeatureName_Type.__name__ = "SnmpAdminString"
_CiscoImgChkFeatureName_Object = MibTableColumn
ciscoImgChkFeatureName = _CiscoImgChkFeatureName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99990, 1, 1, 2, 1, 3),
    _CiscoImgChkFeatureName_Type()
)
ciscoImgChkFeatureName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoImgChkFeatureName.setStatus("current")


class _CiscoImgChkCapabilityName_Type(SnmpAdminString):
    """Custom type ciscoImgChkCapabilityName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CiscoImgChkCapabilityName_Type.__name__ = "SnmpAdminString"
_CiscoImgChkCapabilityName_Object = MibTableColumn
ciscoImgChkCapabilityName = _CiscoImgChkCapabilityName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99990, 1, 1, 2, 1, 4),
    _CiscoImgChkCapabilityName_Type()
)
ciscoImgChkCapabilityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoImgChkCapabilityName.setStatus("current")


class _CiscoImgChkCapabilityReq_Type(Integer32):
    """Custom type ciscoImgChkCapabilityReq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loose", 2),
          ("strict", 1))
    )


_CiscoImgChkCapabilityReq_Type.__name__ = "Integer32"
_CiscoImgChkCapabilityReq_Object = MibTableColumn
ciscoImgChkCapabilityReq = _CiscoImgChkCapabilityReq_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99990, 1, 1, 2, 1, 5),
    _CiscoImgChkCapabilityReq_Type()
)
ciscoImgChkCapabilityReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoImgChkCapabilityReq.setStatus("current")


class _CiscoImgChkInCompDescr_Type(SnmpAdminString):
    """Custom type ciscoImgChkInCompDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CiscoImgChkInCompDescr_Type.__name__ = "SnmpAdminString"
_CiscoImgChkInCompDescr_Object = MibTableColumn
ciscoImgChkInCompDescr = _CiscoImgChkInCompDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99990, 1, 1, 2, 1, 6),
    _CiscoImgChkInCompDescr_Type()
)
ciscoImgChkInCompDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoImgChkInCompDescr.setStatus("current")
_CiscoImageCheckMIBConformance_ObjectIdentity = ObjectIdentity
ciscoImageCheckMIBConformance = _CiscoImageCheckMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99990, 2)
)
_CiscoImageCheckMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoImageCheckMIBCompliances = _CiscoImageCheckMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99990, 2, 1)
)
_CiscoImageCheckMIBGroups_ObjectIdentity = ObjectIdentity
ciscoImageCheckMIBGroups = _CiscoImageCheckMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99990, 2, 2)
)

# Managed Objects groups

ciscoImageCheckOpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 99990, 2, 2, 1)
)
ciscoImageCheckOpGroup.setObjects(
      *(("CISCO-IMAGE-CHECK-MIB", "ciscoImageCheckImageName"),
        ("CISCO-IMAGE-CHECK-MIB", "ciscoImageCheckStatus"),
        ("CISCO-IMAGE-CHECK-MIB", "ciscoImageCheckEntryStatus"))
)
if mibBuilder.loadTexts:
    ciscoImageCheckOpGroup.setStatus("current")

ciscoImgChkResultsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 99990, 2, 2, 2)
)
ciscoImgChkResultsGroup.setObjects(
      *(("CISCO-IMAGE-CHECK-MIB", "ciscoImgChkFeatureName"),
        ("CISCO-IMAGE-CHECK-MIB", "ciscoImgChkCapabilityName"),
        ("CISCO-IMAGE-CHECK-MIB", "ciscoImgChkCapabilityReq"),
        ("CISCO-IMAGE-CHECK-MIB", "ciscoImgChkInCompDescr"))
)
if mibBuilder.loadTexts:
    ciscoImgChkResultsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoImageCheckMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 99990, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoImageCheckMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IMAGE-CHECK-MIB",
    **{"ciscoImageCheckMIB": ciscoImageCheckMIB,
       "ciscoImageCheckMIBObjects": ciscoImageCheckMIBObjects,
       "ciscoImageCheck": ciscoImageCheck,
       "ciscoImageCheckOpTable": ciscoImageCheckOpTable,
       "ciscoImageCheckOpEntry": ciscoImageCheckOpEntry,
       "ciscoImageCheckSerialNum": ciscoImageCheckSerialNum,
       "ciscoImageCheckImageName": ciscoImageCheckImageName,
       "ciscoImageCheckStatus": ciscoImageCheckStatus,
       "ciscoImageCheckEntryStatus": ciscoImageCheckEntryStatus,
       "ciscoImgChkResultsTable": ciscoImgChkResultsTable,
       "ciscoImgChkResultsEntry": ciscoImgChkResultsEntry,
       "ciscoImgChkFeatureIndex": ciscoImgChkFeatureIndex,
       "ciscoImgChkCapabIndex": ciscoImgChkCapabIndex,
       "ciscoImgChkFeatureName": ciscoImgChkFeatureName,
       "ciscoImgChkCapabilityName": ciscoImgChkCapabilityName,
       "ciscoImgChkCapabilityReq": ciscoImgChkCapabilityReq,
       "ciscoImgChkInCompDescr": ciscoImgChkInCompDescr,
       "ciscoImageCheckMIBConformance": ciscoImageCheckMIBConformance,
       "ciscoImageCheckMIBCompliances": ciscoImageCheckMIBCompliances,
       "ciscoImageCheckMIBCompliance": ciscoImageCheckMIBCompliance,
       "ciscoImageCheckMIBGroups": ciscoImageCheckMIBGroups,
       "ciscoImageCheckOpGroup": ciscoImageCheckOpGroup,
       "ciscoImgChkResultsGroup": ciscoImgChkResultsGroup}
)
