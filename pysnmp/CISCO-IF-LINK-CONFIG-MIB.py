# SNMP MIB module (CISCO-IF-LINK-CONFIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-IF-LINK-CONFIG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:02:11 2024
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

(CiscoLocationSpecifier,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "CiscoLocationSpecifier")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

ciscoIfLinkConfigMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 175)
)
ciscoIfLinkConfigMIB.setRevisions(
        ("2001-10-05 00:00",
         "2000-09-14 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CilConfigMIBObjects_ObjectIdentity = ObjectIdentity
cilConfigMIBObjects = _CilConfigMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 175, 1)
)
_CilConfig_ObjectIdentity = ObjectIdentity
cilConfig = _CilConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 175, 1, 1)
)
_CilConfTable_Object = MibTable
cilConfTable = _CilConfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 175, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cilConfTable.setStatus("current")
_CilConfEntry_Object = MibTableRow
cilConfEntry = _CilConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 175, 1, 1, 1, 1)
)
cilConfEntry.setIndexNames(
    (0, "CISCO-IF-LINK-CONFIG-MIB", "cilSourceInterface"),
)
if mibBuilder.loadTexts:
    cilConfEntry.setStatus("current")
_CilSourceInterface_Type = InterfaceIndex
_CilSourceInterface_Object = MibTableColumn
cilSourceInterface = _CilSourceInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 175, 1, 1, 1, 1, 1),
    _CilSourceInterface_Type()
)
cilSourceInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cilSourceInterface.setStatus("current")
_CilTargetModuleInterface_Type = CiscoLocationSpecifier
_CilTargetModuleInterface_Object = MibTableColumn
cilTargetModuleInterface = _CilTargetModuleInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 175, 1, 1, 1, 1, 2),
    _CilTargetModuleInterface_Type()
)
cilTargetModuleInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cilTargetModuleInterface.setStatus("current")
_CilRowStatus_Type = RowStatus
_CilRowStatus_Object = MibTableColumn
cilRowStatus = _CilRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 175, 1, 1, 1, 1, 3),
    _CilRowStatus_Type()
)
cilRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cilRowStatus.setStatus("current")


class _CilTargetModuleFramingType_Type(Integer32):
    """Custom type cilTargetModuleFramingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dsx1D4", 2),
          ("dsx1ESF", 3),
          ("notApplicable", 1))
    )


_CilTargetModuleFramingType_Type.__name__ = "Integer32"
_CilTargetModuleFramingType_Object = MibTableColumn
cilTargetModuleFramingType = _CilTargetModuleFramingType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 175, 1, 1, 1, 1, 4),
    _CilTargetModuleFramingType_Type()
)
cilTargetModuleFramingType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cilTargetModuleFramingType.setStatus("current")
_CilConfigMIBConformance_ObjectIdentity = ObjectIdentity
cilConfigMIBConformance = _CilConfigMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 175, 3)
)
_CilConfigMIBCompliances_ObjectIdentity = ObjectIdentity
cilConfigMIBCompliances = _CilConfigMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 175, 3, 1)
)
_CilConfigMIBGroups_ObjectIdentity = ObjectIdentity
cilConfigMIBGroups = _CilConfigMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 175, 3, 2)
)

# Managed Objects groups

cilConfMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 175, 3, 2, 1)
)
cilConfMIBGroup.setObjects(
      *(("CISCO-IF-LINK-CONFIG-MIB", "cilTargetModuleInterface"),
        ("CISCO-IF-LINK-CONFIG-MIB", "cilRowStatus"))
)
if mibBuilder.loadTexts:
    cilConfMIBGroup.setStatus("deprecated")

cilConfMIBGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 175, 3, 2, 2)
)
cilConfMIBGroupRev1.setObjects(
      *(("CISCO-IF-LINK-CONFIG-MIB", "cilTargetModuleInterface"),
        ("CISCO-IF-LINK-CONFIG-MIB", "cilRowStatus"),
        ("CISCO-IF-LINK-CONFIG-MIB", "cilTargetModuleFramingType"))
)
if mibBuilder.loadTexts:
    cilConfMIBGroupRev1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cilConfigMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 175, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cilConfigMIBCompliance.setStatus(
        "deprecated"
    )

cilConfigMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 175, 3, 1, 2)
)
if mibBuilder.loadTexts:
    cilConfigMIBComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-IF-LINK-CONFIG-MIB",
    **{"ciscoIfLinkConfigMIB": ciscoIfLinkConfigMIB,
       "cilConfigMIBObjects": cilConfigMIBObjects,
       "cilConfig": cilConfig,
       "cilConfTable": cilConfTable,
       "cilConfEntry": cilConfEntry,
       "cilSourceInterface": cilSourceInterface,
       "cilTargetModuleInterface": cilTargetModuleInterface,
       "cilRowStatus": cilRowStatus,
       "cilTargetModuleFramingType": cilTargetModuleFramingType,
       "cilConfigMIBConformance": cilConfigMIBConformance,
       "cilConfigMIBCompliances": cilConfigMIBCompliances,
       "cilConfigMIBCompliance": cilConfigMIBCompliance,
       "cilConfigMIBComplianceRev1": cilConfigMIBComplianceRev1,
       "cilConfigMIBGroups": cilConfigMIBGroups,
       "cilConfMIBGroup": cilConfMIBGroup,
       "cilConfMIBGroupRev1": cilConfMIBGroupRev1}
)
