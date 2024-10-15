# SNMP MIB module (REDSTONE-IP-TEMPLATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/REDSTONE-IP-TEMPLATE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:46:42 2024
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(rsMgmt,) = mibBuilder.importSymbols(
    "REDSTONE-SMI",
    "rsMgmt")

(RsEnable,
 RsName) = mibBuilder.importSymbols(
    "REDSTONE-TC",
    "RsEnable",
    "RsName")

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

rsIpTemplateMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 26)
)
rsIpTemplateMIB.setRevisions(
        ("1999-08-25 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RsIpTemplateObjects_ObjectIdentity = ObjectIdentity
rsIpTemplateObjects = _RsIpTemplateObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 26, 1)
)
_RsIpTemplate_ObjectIdentity = ObjectIdentity
rsIpTemplate = _RsIpTemplate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 26, 1, 1)
)
_RsIpTemplateTable_Object = MibTable
rsIpTemplateTable = _RsIpTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 26, 1, 1, 1)
)
if mibBuilder.loadTexts:
    rsIpTemplateTable.setStatus("current")
_RsIpTemplateEntry_Object = MibTableRow
rsIpTemplateEntry = _RsIpTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 26, 1, 1, 1, 1)
)
rsIpTemplateEntry.setIndexNames(
    (0, "REDSTONE-IP-TEMPLATE-MIB", "rsIpTemplateId"),
)
if mibBuilder.loadTexts:
    rsIpTemplateEntry.setStatus("current")
_RsIpTemplateId_Type = Unsigned32
_RsIpTemplateId_Object = MibTableColumn
rsIpTemplateId = _RsIpTemplateId_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 26, 1, 1, 1, 1, 1),
    _RsIpTemplateId_Type()
)
rsIpTemplateId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rsIpTemplateId.setStatus("current")
_RsIpTemplateRowStatus_Type = RowStatus
_RsIpTemplateRowStatus_Object = MibTableColumn
rsIpTemplateRowStatus = _RsIpTemplateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 26, 1, 1, 1, 1, 2),
    _RsIpTemplateRowStatus_Type()
)
rsIpTemplateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsIpTemplateRowStatus.setStatus("current")


class _RsIpTemplateRouterName_Type(RsName):
    """Custom type rsIpTemplateRouterName based on RsName"""
    defaultHexValue = ""


_RsIpTemplateRouterName_Object = MibTableColumn
rsIpTemplateRouterName = _RsIpTemplateRouterName_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 26, 1, 1, 1, 1, 3),
    _RsIpTemplateRouterName_Type()
)
rsIpTemplateRouterName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsIpTemplateRouterName.setStatus("current")


class _RsIpTemplateIpAddr_Type(IpAddress):
    """Custom type rsIpTemplateIpAddr based on IpAddress"""
    defaultValue = 0


_RsIpTemplateIpAddr_Object = MibTableColumn
rsIpTemplateIpAddr = _RsIpTemplateIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 26, 1, 1, 1, 1, 4),
    _RsIpTemplateIpAddr_Type()
)
rsIpTemplateIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsIpTemplateIpAddr.setStatus("current")


class _RsIpTemplateIpMask_Type(IpAddress):
    """Custom type rsIpTemplateIpMask based on IpAddress"""
    defaultValue = 0


_RsIpTemplateIpMask_Object = MibTableColumn
rsIpTemplateIpMask = _RsIpTemplateIpMask_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 26, 1, 1, 1, 1, 5),
    _RsIpTemplateIpMask_Type()
)
rsIpTemplateIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsIpTemplateIpMask.setStatus("current")


class _RsIpTemplateDirectedBcastEnable_Type(RsEnable):
    """Custom type rsIpTemplateDirectedBcastEnable based on RsEnable"""


_RsIpTemplateDirectedBcastEnable_Object = MibTableColumn
rsIpTemplateDirectedBcastEnable = _RsIpTemplateDirectedBcastEnable_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 26, 1, 1, 1, 1, 6),
    _RsIpTemplateDirectedBcastEnable_Type()
)
rsIpTemplateDirectedBcastEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsIpTemplateDirectedBcastEnable.setStatus("current")


class _RsIpTemplateIcmpRedirectEnable_Type(RsEnable):
    """Custom type rsIpTemplateIcmpRedirectEnable based on RsEnable"""


_RsIpTemplateIcmpRedirectEnable_Object = MibTableColumn
rsIpTemplateIcmpRedirectEnable = _RsIpTemplateIcmpRedirectEnable_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 26, 1, 1, 1, 1, 7),
    _RsIpTemplateIcmpRedirectEnable_Type()
)
rsIpTemplateIcmpRedirectEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsIpTemplateIcmpRedirectEnable.setStatus("current")


class _RsIpTemplateAccessRoute_Type(RsEnable):
    """Custom type rsIpTemplateAccessRoute based on RsEnable"""


_RsIpTemplateAccessRoute_Object = MibTableColumn
rsIpTemplateAccessRoute = _RsIpTemplateAccessRoute_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 26, 1, 1, 1, 1, 8),
    _RsIpTemplateAccessRoute_Type()
)
rsIpTemplateAccessRoute.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsIpTemplateAccessRoute.setStatus("current")


class _RsIpTemplateMtu_Type(Integer32):
    """Custom type rsIpTemplateMtu based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(512, 10240),
    )


_RsIpTemplateMtu_Type.__name__ = "Integer32"
_RsIpTemplateMtu_Object = MibTableColumn
rsIpTemplateMtu = _RsIpTemplateMtu_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 26, 1, 1, 1, 1, 9),
    _RsIpTemplateMtu_Type()
)
rsIpTemplateMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsIpTemplateMtu.setStatus("current")


class _RsIpTemplateLoopbackIfIndex_Type(InterfaceIndexOrZero):
    """Custom type rsIpTemplateLoopbackIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_RsIpTemplateLoopbackIfIndex_Object = MibTableColumn
rsIpTemplateLoopbackIfIndex = _RsIpTemplateLoopbackIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 26, 1, 1, 1, 1, 10),
    _RsIpTemplateLoopbackIfIndex_Type()
)
rsIpTemplateLoopbackIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsIpTemplateLoopbackIfIndex.setStatus("current")
_RsIpTemplateMIBConformance_ObjectIdentity = ObjectIdentity
rsIpTemplateMIBConformance = _RsIpTemplateMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 26, 4)
)
_RsIpTemplateMIBCompliances_ObjectIdentity = ObjectIdentity
rsIpTemplateMIBCompliances = _RsIpTemplateMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 26, 4, 1)
)
_RsIpTemplateMIBGroups_ObjectIdentity = ObjectIdentity
rsIpTemplateMIBGroups = _RsIpTemplateMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 26, 4, 2)
)

# Managed Objects groups

rsIpTemplateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2773, 2, 26, 4, 2, 1)
)
rsIpTemplateGroup.setObjects(
      *(("REDSTONE-IP-TEMPLATE-MIB", "rsIpTemplateRowStatus"),
        ("REDSTONE-IP-TEMPLATE-MIB", "rsIpTemplateRouterName"),
        ("REDSTONE-IP-TEMPLATE-MIB", "rsIpTemplateIpAddr"),
        ("REDSTONE-IP-TEMPLATE-MIB", "rsIpTemplateIpMask"),
        ("REDSTONE-IP-TEMPLATE-MIB", "rsIpTemplateDirectedBcastEnable"),
        ("REDSTONE-IP-TEMPLATE-MIB", "rsIpTemplateIcmpRedirectEnable"),
        ("REDSTONE-IP-TEMPLATE-MIB", "rsIpTemplateAccessRoute"),
        ("REDSTONE-IP-TEMPLATE-MIB", "rsIpTemplateMtu"),
        ("REDSTONE-IP-TEMPLATE-MIB", "rsIpTemplateLoopbackIfIndex"))
)
if mibBuilder.loadTexts:
    rsIpTemplateGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rsIpTemplateCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2773, 2, 26, 4, 1, 1)
)
if mibBuilder.loadTexts:
    rsIpTemplateCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "REDSTONE-IP-TEMPLATE-MIB",
    **{"rsIpTemplateMIB": rsIpTemplateMIB,
       "rsIpTemplateObjects": rsIpTemplateObjects,
       "rsIpTemplate": rsIpTemplate,
       "rsIpTemplateTable": rsIpTemplateTable,
       "rsIpTemplateEntry": rsIpTemplateEntry,
       "rsIpTemplateId": rsIpTemplateId,
       "rsIpTemplateRowStatus": rsIpTemplateRowStatus,
       "rsIpTemplateRouterName": rsIpTemplateRouterName,
       "rsIpTemplateIpAddr": rsIpTemplateIpAddr,
       "rsIpTemplateIpMask": rsIpTemplateIpMask,
       "rsIpTemplateDirectedBcastEnable": rsIpTemplateDirectedBcastEnable,
       "rsIpTemplateIcmpRedirectEnable": rsIpTemplateIcmpRedirectEnable,
       "rsIpTemplateAccessRoute": rsIpTemplateAccessRoute,
       "rsIpTemplateMtu": rsIpTemplateMtu,
       "rsIpTemplateLoopbackIfIndex": rsIpTemplateLoopbackIfIndex,
       "rsIpTemplateMIBConformance": rsIpTemplateMIBConformance,
       "rsIpTemplateMIBCompliances": rsIpTemplateMIBCompliances,
       "rsIpTemplateCompliance": rsIpTemplateCompliance,
       "rsIpTemplateMIBGroups": rsIpTemplateMIBGroups,
       "rsIpTemplateGroup": rsIpTemplateGroup}
)
