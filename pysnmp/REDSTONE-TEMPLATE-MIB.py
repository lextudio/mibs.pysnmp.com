# SNMP MIB module (REDSTONE-TEMPLATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/REDSTONE-TEMPLATE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:46:49 2024
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

(rsMgmt,) = mibBuilder.importSymbols(
    "REDSTONE-SMI",
    "rsMgmt")

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

rsTemplateMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 25)
)
rsTemplateMIB.setRevisions(
        ("1999-06-01 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RsTemplateObjects_ObjectIdentity = ObjectIdentity
rsTemplateObjects = _RsTemplateObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 25, 1)
)
_RsTemplateName_ObjectIdentity = ObjectIdentity
rsTemplateName = _RsTemplateName_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 25, 1, 1)
)
_RsTemplateNameTable_Object = MibTable
rsTemplateNameTable = _RsTemplateNameTable_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 25, 1, 1, 1)
)
if mibBuilder.loadTexts:
    rsTemplateNameTable.setStatus("current")
_RsTemplateNameEntry_Object = MibTableRow
rsTemplateNameEntry = _RsTemplateNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 25, 1, 1, 1, 1)
)
rsTemplateNameEntry.setIndexNames(
    (1, "REDSTONE-TEMPLATE-MIB", "rsTemplateNameName"),
)
if mibBuilder.loadTexts:
    rsTemplateNameEntry.setStatus("current")


class _RsTemplateNameName_Type(DisplayString):
    """Custom type rsTemplateNameName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_RsTemplateNameName_Type.__name__ = "DisplayString"
_RsTemplateNameName_Object = MibTableColumn
rsTemplateNameName = _RsTemplateNameName_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 25, 1, 1, 1, 1, 1),
    _RsTemplateNameName_Type()
)
rsTemplateNameName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsTemplateNameName.setStatus("current")
_RsTemplateNameRowStatus_Type = RowStatus
_RsTemplateNameRowStatus_Object = MibTableColumn
rsTemplateNameRowStatus = _RsTemplateNameRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 25, 1, 1, 1, 1, 2),
    _RsTemplateNameRowStatus_Type()
)
rsTemplateNameRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsTemplateNameRowStatus.setStatus("current")
_RsTemplateNameId_Type = Unsigned32
_RsTemplateNameId_Object = MibTableColumn
rsTemplateNameId = _RsTemplateNameId_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 25, 1, 1, 1, 1, 3),
    _RsTemplateNameId_Type()
)
rsTemplateNameId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsTemplateNameId.setStatus("current")
_RsTemplateIdTable_Object = MibTable
rsTemplateIdTable = _RsTemplateIdTable_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 25, 1, 1, 2)
)
if mibBuilder.loadTexts:
    rsTemplateIdTable.setStatus("current")
_RsTemplateIdEntry_Object = MibTableRow
rsTemplateIdEntry = _RsTemplateIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 25, 1, 1, 2, 1)
)
rsTemplateIdEntry.setIndexNames(
    (0, "REDSTONE-TEMPLATE-MIB", "rsTemplateIdId"),
)
if mibBuilder.loadTexts:
    rsTemplateIdEntry.setStatus("current")
_RsTemplateIdId_Type = Unsigned32
_RsTemplateIdId_Object = MibTableColumn
rsTemplateIdId = _RsTemplateIdId_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 25, 1, 1, 2, 1, 1),
    _RsTemplateIdId_Type()
)
rsTemplateIdId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rsTemplateIdId.setStatus("current")


class _RsTemplateIdName_Type(DisplayString):
    """Custom type rsTemplateIdName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_RsTemplateIdName_Type.__name__ = "DisplayString"
_RsTemplateIdName_Object = MibTableColumn
rsTemplateIdName = _RsTemplateIdName_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 25, 1, 1, 2, 1, 2),
    _RsTemplateIdName_Type()
)
rsTemplateIdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsTemplateIdName.setStatus("current")
_RsTemplateMIBConformance_ObjectIdentity = ObjectIdentity
rsTemplateMIBConformance = _RsTemplateMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 25, 4)
)
_RsTemplateMIBCompliances_ObjectIdentity = ObjectIdentity
rsTemplateMIBCompliances = _RsTemplateMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 25, 4, 1)
)
_RsTemplateMIBGroups_ObjectIdentity = ObjectIdentity
rsTemplateMIBGroups = _RsTemplateMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 25, 4, 2)
)

# Managed Objects groups

rsTemplateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2773, 2, 25, 4, 2, 1)
)
rsTemplateGroup.setObjects(
      *(("REDSTONE-TEMPLATE-MIB", "rsTemplateNameName"),
        ("REDSTONE-TEMPLATE-MIB", "rsTemplateNameRowStatus"),
        ("REDSTONE-TEMPLATE-MIB", "rsTemplateNameId"),
        ("REDSTONE-TEMPLATE-MIB", "rsTemplateIdName"))
)
if mibBuilder.loadTexts:
    rsTemplateGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rsTemplateCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2773, 2, 25, 4, 1, 1)
)
if mibBuilder.loadTexts:
    rsTemplateCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "REDSTONE-TEMPLATE-MIB",
    **{"rsTemplateMIB": rsTemplateMIB,
       "rsTemplateObjects": rsTemplateObjects,
       "rsTemplateName": rsTemplateName,
       "rsTemplateNameTable": rsTemplateNameTable,
       "rsTemplateNameEntry": rsTemplateNameEntry,
       "rsTemplateNameName": rsTemplateNameName,
       "rsTemplateNameRowStatus": rsTemplateNameRowStatus,
       "rsTemplateNameId": rsTemplateNameId,
       "rsTemplateIdTable": rsTemplateIdTable,
       "rsTemplateIdEntry": rsTemplateIdEntry,
       "rsTemplateIdId": rsTemplateIdId,
       "rsTemplateIdName": rsTemplateIdName,
       "rsTemplateMIBConformance": rsTemplateMIBConformance,
       "rsTemplateMIBCompliances": rsTemplateMIBCompliances,
       "rsTemplateCompliance": rsTemplateCompliance,
       "rsTemplateMIBGroups": rsTemplateMIBGroups,
       "rsTemplateGroup": rsTemplateGroup}
)
