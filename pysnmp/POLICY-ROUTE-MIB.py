# SNMP MIB module (POLICY-ROUTE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/POLICY-ROUTE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:39:13 2024
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

(dlink_common_mgmt,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlink-common-mgmt")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 MacAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

swPolicyRouteMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 32)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwPolicyRouteCtrl_ObjectIdentity = ObjectIdentity
swPolicyRouteCtrl = _SwPolicyRouteCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 32, 1)
)
_SwPolicyRouteInfo_ObjectIdentity = ObjectIdentity
swPolicyRouteInfo = _SwPolicyRouteInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 32, 2)
)
_SwPolicyRouteMgmt_ObjectIdentity = ObjectIdentity
swPolicyRouteMgmt = _SwPolicyRouteMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 32, 3)
)
_SwPolicyRouteTable_Object = MibTable
swPolicyRouteTable = _SwPolicyRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 32, 3, 1)
)
if mibBuilder.loadTexts:
    swPolicyRouteTable.setStatus("current")
_SwPolicyRouteEntry_Object = MibTableRow
swPolicyRouteEntry = _SwPolicyRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 32, 3, 1, 1)
)
swPolicyRouteEntry.setIndexNames(
    (0, "POLICY-ROUTE-MIB", "swPolicyRouteName"),
)
if mibBuilder.loadTexts:
    swPolicyRouteEntry.setStatus("current")


class _SwPolicyRouteName_Type(DisplayString):
    """Custom type swPolicyRouteName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_SwPolicyRouteName_Type.__name__ = "DisplayString"
_SwPolicyRouteName_Object = MibTableColumn
swPolicyRouteName = _SwPolicyRouteName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 32, 3, 1, 1, 1),
    _SwPolicyRouteName_Type()
)
swPolicyRouteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPolicyRouteName.setStatus("current")
_SwPolicyRouteProfileId_Type = Integer32
_SwPolicyRouteProfileId_Object = MibTableColumn
swPolicyRouteProfileId = _SwPolicyRouteProfileId_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 32, 3, 1, 1, 2),
    _SwPolicyRouteProfileId_Type()
)
swPolicyRouteProfileId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swPolicyRouteProfileId.setStatus("current")
_SwPolicyRouteAccessId_Type = Integer32
_SwPolicyRouteAccessId_Object = MibTableColumn
swPolicyRouteAccessId = _SwPolicyRouteAccessId_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 32, 3, 1, 1, 3),
    _SwPolicyRouteAccessId_Type()
)
swPolicyRouteAccessId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swPolicyRouteAccessId.setStatus("current")
_SwPolicyRouteNextHop_Type = IpAddress
_SwPolicyRouteNextHop_Object = MibTableColumn
swPolicyRouteNextHop = _SwPolicyRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 32, 3, 1, 1, 4),
    _SwPolicyRouteNextHop_Type()
)
swPolicyRouteNextHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swPolicyRouteNextHop.setStatus("current")
_SwPolicyRouteRowStatus_Type = RowStatus
_SwPolicyRouteRowStatus_Object = MibTableColumn
swPolicyRouteRowStatus = _SwPolicyRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 32, 3, 1, 1, 5),
    _SwPolicyRouteRowStatus_Type()
)
swPolicyRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swPolicyRouteRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "POLICY-ROUTE-MIB",
    **{"swPolicyRouteMIB": swPolicyRouteMIB,
       "swPolicyRouteCtrl": swPolicyRouteCtrl,
       "swPolicyRouteInfo": swPolicyRouteInfo,
       "swPolicyRouteMgmt": swPolicyRouteMgmt,
       "swPolicyRouteTable": swPolicyRouteTable,
       "swPolicyRouteEntry": swPolicyRouteEntry,
       "swPolicyRouteName": swPolicyRouteName,
       "swPolicyRouteProfileId": swPolicyRouteProfileId,
       "swPolicyRouteAccessId": swPolicyRouteAccessId,
       "swPolicyRouteNextHop": swPolicyRouteNextHop,
       "swPolicyRouteRowStatus": swPolicyRouteRowStatus}
)
