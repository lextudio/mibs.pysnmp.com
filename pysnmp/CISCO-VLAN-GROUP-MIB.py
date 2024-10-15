# SNMP MIB module (CISCO-VLAN-GROUP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-VLAN-GROUP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:12:04 2024
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

(Cisco2KVlanList,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "Cisco2KVlanList")

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

ciscoVlanGroupMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 709)
)
ciscoVlanGroupMIB.setRevisions(
        ("2011-03-22 00:00",
         "2009-11-20 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoVlanGroupMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoVlanGroupMIBNotifs = _CiscoVlanGroupMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 709, 0)
)
_CiscoVlanGroupMIBObjects_ObjectIdentity = ObjectIdentity
ciscoVlanGroupMIBObjects = _CiscoVlanGroupMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 709, 1)
)
_CvgConfigTable_Object = MibTable
cvgConfigTable = _CvgConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 709, 1, 1)
)
if mibBuilder.loadTexts:
    cvgConfigTable.setStatus("current")
_CvgConfigEntry_Object = MibTableRow
cvgConfigEntry = _CvgConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 709, 1, 1, 1)
)
cvgConfigEntry.setIndexNames(
    (0, "CISCO-VLAN-GROUP-MIB", "cvgConfigGroupName"),
)
if mibBuilder.loadTexts:
    cvgConfigEntry.setStatus("current")


class _CvgConfigGroupName_Type(SnmpAdminString):
    """Custom type cvgConfigGroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CvgConfigGroupName_Type.__name__ = "SnmpAdminString"
_CvgConfigGroupName_Object = MibTableColumn
cvgConfigGroupName = _CvgConfigGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 709, 1, 1, 1, 1),
    _CvgConfigGroupName_Type()
)
cvgConfigGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cvgConfigGroupName.setStatus("current")
_CvgConfigVlansFirst2K_Type = Cisco2KVlanList
_CvgConfigVlansFirst2K_Object = MibTableColumn
cvgConfigVlansFirst2K = _CvgConfigVlansFirst2K_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 709, 1, 1, 1, 2),
    _CvgConfigVlansFirst2K_Type()
)
cvgConfigVlansFirst2K.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvgConfigVlansFirst2K.setStatus("current")
_CvgConfigVlansSecond2K_Type = Cisco2KVlanList
_CvgConfigVlansSecond2K_Object = MibTableColumn
cvgConfigVlansSecond2K = _CvgConfigVlansSecond2K_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 709, 1, 1, 1, 3),
    _CvgConfigVlansSecond2K_Type()
)
cvgConfigVlansSecond2K.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvgConfigVlansSecond2K.setStatus("current")


class _CvgConfigStorageType_Type(StorageType):
    """Custom type cvgConfigStorageType based on StorageType"""


_CvgConfigStorageType_Object = MibTableColumn
cvgConfigStorageType = _CvgConfigStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 709, 1, 1, 1, 4),
    _CvgConfigStorageType_Type()
)
cvgConfigStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvgConfigStorageType.setStatus("current")
_CvgConfigRowStatus_Type = RowStatus
_CvgConfigRowStatus_Object = MibTableColumn
cvgConfigRowStatus = _CvgConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 709, 1, 1, 1, 5),
    _CvgConfigRowStatus_Type()
)
cvgConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cvgConfigRowStatus.setStatus("current")
_CvgConfigTableSize_Type = Unsigned32
_CvgConfigTableSize_Object = MibScalar
cvgConfigTableSize = _CvgConfigTableSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 709, 1, 2),
    _CvgConfigTableSize_Type()
)
cvgConfigTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cvgConfigTableSize.setStatus("current")
_CiscoVlanGroupMIBConform_ObjectIdentity = ObjectIdentity
ciscoVlanGroupMIBConform = _CiscoVlanGroupMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 709, 2)
)
_CiscoVlanGroupMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoVlanGroupMIBCompliances = _CiscoVlanGroupMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 709, 2, 1)
)
_CiscoVlanGroupMIBGroups_ObjectIdentity = ObjectIdentity
ciscoVlanGroupMIBGroups = _CiscoVlanGroupMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 709, 2, 2)
)

# Managed Objects groups

ciscoVlanGroupConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 709, 2, 2, 1)
)
ciscoVlanGroupConfigGroup.setObjects(
      *(("CISCO-VLAN-GROUP-MIB", "cvgConfigVlansFirst2K"),
        ("CISCO-VLAN-GROUP-MIB", "cvgConfigVlansSecond2K"),
        ("CISCO-VLAN-GROUP-MIB", "cvgConfigRowStatus"),
        ("CISCO-VLAN-GROUP-MIB", "cvgConfigStorageType"))
)
if mibBuilder.loadTexts:
    ciscoVlanGroupConfigGroup.setStatus("current")

cvgConfigTableSizeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 709, 2, 2, 2)
)
cvgConfigTableSizeGroup.setObjects(
    ("CISCO-VLAN-GROUP-MIB", "cvgConfigTableSize")
)
if mibBuilder.loadTexts:
    cvgConfigTableSizeGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoVlanGroupMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 709, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoVlanGroupMIBCompliance.setStatus(
        "deprecated"
    )

ciscoVlanGroupMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 709, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoVlanGroupMIBCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-VLAN-GROUP-MIB",
    **{"ciscoVlanGroupMIB": ciscoVlanGroupMIB,
       "ciscoVlanGroupMIBNotifs": ciscoVlanGroupMIBNotifs,
       "ciscoVlanGroupMIBObjects": ciscoVlanGroupMIBObjects,
       "cvgConfigTable": cvgConfigTable,
       "cvgConfigEntry": cvgConfigEntry,
       "cvgConfigGroupName": cvgConfigGroupName,
       "cvgConfigVlansFirst2K": cvgConfigVlansFirst2K,
       "cvgConfigVlansSecond2K": cvgConfigVlansSecond2K,
       "cvgConfigStorageType": cvgConfigStorageType,
       "cvgConfigRowStatus": cvgConfigRowStatus,
       "cvgConfigTableSize": cvgConfigTableSize,
       "ciscoVlanGroupMIBConform": ciscoVlanGroupMIBConform,
       "ciscoVlanGroupMIBCompliances": ciscoVlanGroupMIBCompliances,
       "ciscoVlanGroupMIBCompliance": ciscoVlanGroupMIBCompliance,
       "ciscoVlanGroupMIBCompliance2": ciscoVlanGroupMIBCompliance2,
       "ciscoVlanGroupMIBGroups": ciscoVlanGroupMIBGroups,
       "ciscoVlanGroupConfigGroup": ciscoVlanGroupConfigGroup,
       "cvgConfigTableSizeGroup": cvgConfigTableSizeGroup}
)
