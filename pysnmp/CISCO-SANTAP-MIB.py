# SNMP MIB module (CISCO-SANTAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-SANTAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:07:56 2024
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

(FcNameId,
 FcNameIdOrZero,
 VsanIndex) = mibBuilder.importSymbols(
    "CISCO-ST-TC",
    "FcNameId",
    "FcNameIdOrZero",
    "VsanIndex")

(vsanIndex,) = mibBuilder.importSymbols(
    "CISCO-VSAN-MIB",
    "vsanIndex")

(PhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndex")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoSanTapMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 463)
)
ciscoSanTapMIB.setRevisions(
        ("2006-03-16 00:00",
         "2005-10-27 00:00",
         "2005-02-02 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoSanTapMIBObjects_ObjectIdentity = ObjectIdentity
ciscoSanTapMIBObjects = _CiscoSanTapMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 463, 1)
)
_CstModuleTable_Object = MibTable
cstModuleTable = _CstModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 463, 1, 1)
)
if mibBuilder.loadTexts:
    cstModuleTable.setStatus("current")
_CstModuleEntry_Object = MibTableRow
cstModuleEntry = _CstModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 463, 1, 1, 1)
)
cstModuleEntry.setIndexNames(
    (0, "CISCO-SANTAP-MIB", "cstModuleId"),
)
if mibBuilder.loadTexts:
    cstModuleEntry.setStatus("current")
_CstModuleId_Type = PhysicalIndex
_CstModuleId_Object = MibTableColumn
cstModuleId = _CstModuleId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 463, 1, 1, 1, 1),
    _CstModuleId_Type()
)
cstModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cstModuleId.setStatus("current")
_CstServiceConfigTable_Object = MibTable
cstServiceConfigTable = _CstServiceConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 463, 1, 2)
)
if mibBuilder.loadTexts:
    cstServiceConfigTable.setStatus("current")
_CstServiceConfigEntry_Object = MibTableRow
cstServiceConfigEntry = _CstServiceConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 463, 1, 2, 1)
)
cstServiceConfigEntry.setIndexNames(
    (0, "CISCO-SANTAP-MIB", "cstModuleId"),
    (0, "CISCO-VSAN-MIB", "vsanIndex"),
)
if mibBuilder.loadTexts:
    cstServiceConfigEntry.setStatus("current")
_CstCVTNodeWwn_Type = FcNameIdOrZero
_CstCVTNodeWwn_Object = MibTableColumn
cstCVTNodeWwn = _CstCVTNodeWwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 463, 1, 2, 1, 1),
    _CstCVTNodeWwn_Type()
)
cstCVTNodeWwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cstCVTNodeWwn.setStatus("current")
_CstCVTPortWwn_Type = FcNameIdOrZero
_CstCVTPortWwn_Object = MibTableColumn
cstCVTPortWwn = _CstCVTPortWwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 463, 1, 2, 1, 2),
    _CstCVTPortWwn_Type()
)
cstCVTPortWwn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cstCVTPortWwn.setStatus("current")
_CstServiceConfigRowStatus_Type = RowStatus
_CstServiceConfigRowStatus_Object = MibTableColumn
cstServiceConfigRowStatus = _CstServiceConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 463, 1, 2, 1, 3),
    _CstServiceConfigRowStatus_Type()
)
cstServiceConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cstServiceConfigRowStatus.setStatus("current")


class _CstCVTName_Type(SnmpAdminString):
    """Custom type cstCVTName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CstCVTName_Type.__name__ = "SnmpAdminString"
_CstCVTName_Object = MibTableColumn
cstCVTName = _CstCVTName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 463, 1, 2, 1, 4),
    _CstCVTName_Type()
)
cstCVTName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cstCVTName.setStatus("current")
_CstDVTConfigTable_Object = MibTable
cstDVTConfigTable = _CstDVTConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 463, 1, 3)
)
if mibBuilder.loadTexts:
    cstDVTConfigTable.setStatus("current")
_CstDVTConfigEntry_Object = MibTableRow
cstDVTConfigEntry = _CstDVTConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 463, 1, 3, 1)
)
cstDVTConfigEntry.setIndexNames(
    (0, "CISCO-VSAN-MIB", "vsanIndex"),
    (0, "CISCO-SANTAP-MIB", "cstDVTPortWwn"),
)
if mibBuilder.loadTexts:
    cstDVTConfigEntry.setStatus("current")
_CstDVTPortWwn_Type = FcNameId
_CstDVTPortWwn_Object = MibTableColumn
cstDVTPortWwn = _CstDVTPortWwn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 463, 1, 3, 1, 1),
    _CstDVTPortWwn_Type()
)
cstDVTPortWwn.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cstDVTPortWwn.setStatus("current")
_CstDVTTargetVsan_Type = VsanIndex
_CstDVTTargetVsan_Object = MibTableColumn
cstDVTTargetVsan = _CstDVTTargetVsan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 463, 1, 3, 1, 2),
    _CstDVTTargetVsan_Type()
)
cstDVTTargetVsan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cstDVTTargetVsan.setStatus("current")
_CstDVTPort_Type = InterfaceIndex
_CstDVTPort_Object = MibTableColumn
cstDVTPort = _CstDVTPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 463, 1, 3, 1, 3),
    _CstDVTPort_Type()
)
cstDVTPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cstDVTPort.setStatus("current")


class _CstDVTName_Type(SnmpAdminString):
    """Custom type cstDVTName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CstDVTName_Type.__name__ = "SnmpAdminString"
_CstDVTName_Object = MibTableColumn
cstDVTName = _CstDVTName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 463, 1, 3, 1, 4),
    _CstDVTName_Type()
)
cstDVTName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cstDVTName.setStatus("current")
_CstDVTRowStatus_Type = RowStatus
_CstDVTRowStatus_Object = MibTableColumn
cstDVTRowStatus = _CstDVTRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 463, 1, 3, 1, 5),
    _CstDVTRowStatus_Type()
)
cstDVTRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cstDVTRowStatus.setStatus("current")


class _CstDVTLunSizeHandling_Type(TruthValue):
    """Custom type cstDVTLunSizeHandling based on TruthValue"""


_CstDVTLunSizeHandling_Object = MibTableColumn
cstDVTLunSizeHandling = _CstDVTLunSizeHandling_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 463, 1, 3, 1, 6),
    _CstDVTLunSizeHandling_Type()
)
cstDVTLunSizeHandling.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cstDVTLunSizeHandling.setStatus("current")


class _CstDVTIOTimeout_Type(Unsigned32):
    """Custom type cstDVTIOTimeout based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 200),
    )


_CstDVTIOTimeout_Type.__name__ = "Unsigned32"
_CstDVTIOTimeout_Object = MibTableColumn
cstDVTIOTimeout = _CstDVTIOTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 463, 1, 3, 1, 7),
    _CstDVTIOTimeout_Type()
)
cstDVTIOTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cstDVTIOTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cstDVTIOTimeout.setUnits("seconds")
_CiscoSanTapMIBConformance_ObjectIdentity = ObjectIdentity
ciscoSanTapMIBConformance = _CiscoSanTapMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 463, 2)
)
_CiscoSanTapMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoSanTapMIBCompliances = _CiscoSanTapMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 463, 2, 1)
)
_CiscoSanTapMIBGroups_ObjectIdentity = ObjectIdentity
ciscoSanTapMIBGroups = _CiscoSanTapMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 463, 2, 2)
)
_CiscoSanTapNotifications_ObjectIdentity = ObjectIdentity
ciscoSanTapNotifications = _CiscoSanTapNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 463, 3)
)

# Managed Objects groups

ciscoSanTapServiceConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 463, 2, 2, 1)
)
ciscoSanTapServiceConfigGroup.setObjects(
      *(("CISCO-SANTAP-MIB", "cstModuleId"),
        ("CISCO-SANTAP-MIB", "cstCVTNodeWwn"),
        ("CISCO-SANTAP-MIB", "cstCVTPortWwn"),
        ("CISCO-SANTAP-MIB", "cstServiceConfigRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoSanTapServiceConfigGroup.setStatus("deprecated")

ciscoSanTapServiceConfigGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 463, 2, 2, 2)
)
ciscoSanTapServiceConfigGroupRev1.setObjects(
      *(("CISCO-SANTAP-MIB", "cstModuleId"),
        ("CISCO-SANTAP-MIB", "cstCVTNodeWwn"),
        ("CISCO-SANTAP-MIB", "cstCVTPortWwn"),
        ("CISCO-SANTAP-MIB", "cstServiceConfigRowStatus"),
        ("CISCO-SANTAP-MIB", "cstCVTName"))
)
if mibBuilder.loadTexts:
    ciscoSanTapServiceConfigGroupRev1.setStatus("current")

ciscoSanTapDVTConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 463, 2, 2, 3)
)
ciscoSanTapDVTConfigGroup.setObjects(
      *(("CISCO-SANTAP-MIB", "cstDVTTargetVsan"),
        ("CISCO-SANTAP-MIB", "cstDVTPort"),
        ("CISCO-SANTAP-MIB", "cstDVTName"),
        ("CISCO-SANTAP-MIB", "cstDVTRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoSanTapDVTConfigGroup.setStatus("deprecated")

ciscoSanTapDVTConfigGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 463, 2, 2, 4)
)
ciscoSanTapDVTConfigGroup1.setObjects(
      *(("CISCO-SANTAP-MIB", "cstDVTTargetVsan"),
        ("CISCO-SANTAP-MIB", "cstDVTPort"),
        ("CISCO-SANTAP-MIB", "cstDVTName"),
        ("CISCO-SANTAP-MIB", "cstDVTRowStatus"),
        ("CISCO-SANTAP-MIB", "cstDVTLunSizeHandling"),
        ("CISCO-SANTAP-MIB", "cstDVTIOTimeout"))
)
if mibBuilder.loadTexts:
    ciscoSanTapDVTConfigGroup1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoSanTapMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 463, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoSanTapMIBCompliance.setStatus(
        "deprecated"
    )

ciscoSanTapMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 463, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoSanTapMIBComplianceRev1.setStatus(
        "deprecated"
    )

ciscoSanTapMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 463, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoSanTapMIBComplianceRev2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SANTAP-MIB",
    **{"ciscoSanTapMIB": ciscoSanTapMIB,
       "ciscoSanTapMIBObjects": ciscoSanTapMIBObjects,
       "cstModuleTable": cstModuleTable,
       "cstModuleEntry": cstModuleEntry,
       "cstModuleId": cstModuleId,
       "cstServiceConfigTable": cstServiceConfigTable,
       "cstServiceConfigEntry": cstServiceConfigEntry,
       "cstCVTNodeWwn": cstCVTNodeWwn,
       "cstCVTPortWwn": cstCVTPortWwn,
       "cstServiceConfigRowStatus": cstServiceConfigRowStatus,
       "cstCVTName": cstCVTName,
       "cstDVTConfigTable": cstDVTConfigTable,
       "cstDVTConfigEntry": cstDVTConfigEntry,
       "cstDVTPortWwn": cstDVTPortWwn,
       "cstDVTTargetVsan": cstDVTTargetVsan,
       "cstDVTPort": cstDVTPort,
       "cstDVTName": cstDVTName,
       "cstDVTRowStatus": cstDVTRowStatus,
       "cstDVTLunSizeHandling": cstDVTLunSizeHandling,
       "cstDVTIOTimeout": cstDVTIOTimeout,
       "ciscoSanTapMIBConformance": ciscoSanTapMIBConformance,
       "ciscoSanTapMIBCompliances": ciscoSanTapMIBCompliances,
       "ciscoSanTapMIBCompliance": ciscoSanTapMIBCompliance,
       "ciscoSanTapMIBComplianceRev1": ciscoSanTapMIBComplianceRev1,
       "ciscoSanTapMIBComplianceRev2": ciscoSanTapMIBComplianceRev2,
       "ciscoSanTapMIBGroups": ciscoSanTapMIBGroups,
       "ciscoSanTapServiceConfigGroup": ciscoSanTapServiceConfigGroup,
       "ciscoSanTapServiceConfigGroupRev1": ciscoSanTapServiceConfigGroupRev1,
       "ciscoSanTapDVTConfigGroup": ciscoSanTapDVTConfigGroup,
       "ciscoSanTapDVTConfigGroup1": ciscoSanTapDVTConfigGroup1,
       "ciscoSanTapNotifications": ciscoSanTapNotifications}
)
