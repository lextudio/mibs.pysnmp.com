# SNMP MIB module (ALCATEL-IND1-GLOBALROUTETABLE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-IND1-GLOBALROUTETABLE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:36:04 2024
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

(routingIND1GlobalRouteTable,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "routingIND1GlobalRouteTable")

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

alcatelIND1GRTMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1)
)
alcatelIND1GRTMIB.setRevisions(
        ("2011-04-28 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AlaGrtRouteDistinguisher(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1GRTMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1GRTMIBObjects = _AlcatelIND1GRTMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1, 1)
)
_AlaGrtConfig_ObjectIdentity = ObjectIdentity
alaGrtConfig = _AlaGrtConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1, 1, 1)
)
_AlaGrtRouteTable_Object = MibTable
alaGrtRouteTable = _AlaGrtRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    alaGrtRouteTable.setStatus("current")
_AlaGrtRouteEntry_Object = MibTableRow
alaGrtRouteEntry = _AlaGrtRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1, 1, 1, 1, 1)
)
alaGrtRouteEntry.setIndexNames(
    (0, "ALCATEL-IND1-GLOBALROUTETABLE-MIB", "alaGrtRouteDistinguisher"),
    (0, "ALCATEL-IND1-GLOBALROUTETABLE-MIB", "alaGrtRouteDest"),
    (0, "ALCATEL-IND1-GLOBALROUTETABLE-MIB", "alaGrtRouteMaskLen"),
    (0, "ALCATEL-IND1-GLOBALROUTETABLE-MIB", "alaGrtRouteNextHop"),
)
if mibBuilder.loadTexts:
    alaGrtRouteEntry.setStatus("current")
_AlaGrtRouteDistinguisher_Type = AlaGrtRouteDistinguisher
_AlaGrtRouteDistinguisher_Object = MibTableColumn
alaGrtRouteDistinguisher = _AlaGrtRouteDistinguisher_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1, 1, 1, 1, 1, 1),
    _AlaGrtRouteDistinguisher_Type()
)
alaGrtRouteDistinguisher.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaGrtRouteDistinguisher.setStatus("current")
_AlaGrtRouteDest_Type = IpAddress
_AlaGrtRouteDest_Object = MibTableColumn
alaGrtRouteDest = _AlaGrtRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1, 1, 1, 1, 1, 2),
    _AlaGrtRouteDest_Type()
)
alaGrtRouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaGrtRouteDest.setStatus("current")
_AlaGrtRouteMaskLen_Type = Unsigned32
_AlaGrtRouteMaskLen_Object = MibTableColumn
alaGrtRouteMaskLen = _AlaGrtRouteMaskLen_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1, 1, 1, 1, 1, 3),
    _AlaGrtRouteMaskLen_Type()
)
alaGrtRouteMaskLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaGrtRouteMaskLen.setStatus("current")
_AlaGrtRouteNextHop_Type = IpAddress
_AlaGrtRouteNextHop_Object = MibTableColumn
alaGrtRouteNextHop = _AlaGrtRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1, 1, 1, 1, 1, 4),
    _AlaGrtRouteNextHop_Type()
)
alaGrtRouteNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaGrtRouteNextHop.setStatus("current")
_AlaGrtRouteMetric_Type = Unsigned32
_AlaGrtRouteMetric_Object = MibTableColumn
alaGrtRouteMetric = _AlaGrtRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1, 1, 1, 1, 1, 5),
    _AlaGrtRouteMetric_Type()
)
alaGrtRouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaGrtRouteMetric.setStatus("current")
_AlaGrtRouteTag_Type = Unsigned32
_AlaGrtRouteTag_Object = MibTableColumn
alaGrtRouteTag = _AlaGrtRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1, 1, 1, 1, 1, 6),
    _AlaGrtRouteTag_Type()
)
alaGrtRouteTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaGrtRouteTag.setStatus("current")


class _AlaGrtRouteVrfName_Type(OctetString):
    """Custom type alaGrtRouteVrfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AlaGrtRouteVrfName_Type.__name__ = "OctetString"
_AlaGrtRouteVrfName_Object = MibTableColumn
alaGrtRouteVrfName = _AlaGrtRouteVrfName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1, 1, 1, 1, 1, 7),
    _AlaGrtRouteVrfName_Type()
)
alaGrtRouteVrfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaGrtRouteVrfName.setStatus("current")
_AlaGrtRouteIsid_Type = Unsigned32
_AlaGrtRouteIsid_Object = MibTableColumn
alaGrtRouteIsid = _AlaGrtRouteIsid_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1, 1, 1, 1, 1, 8),
    _AlaGrtRouteIsid_Type()
)
alaGrtRouteIsid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaGrtRouteIsid.setStatus("current")
_AlcatelIND1GRTMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1GRTMIBConformance = _AlcatelIND1GRTMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1, 2)
)
_AlcatelIND1GRTMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1GRTMIBCompliances = _AlcatelIND1GRTMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1, 2, 1)
)
_AlcatelIND1GRTMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1GRTMIBGroups = _AlcatelIND1GRTMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1, 2, 2)
)

# Managed Objects groups

alaGrtConfigMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1, 2, 2, 1)
)
alaGrtConfigMIBGroup.setObjects(
      *(("ALCATEL-IND1-GLOBALROUTETABLE-MIB", "alaGrtRouteMetric"),
        ("ALCATEL-IND1-GLOBALROUTETABLE-MIB", "alaGrtRouteTag"),
        ("ALCATEL-IND1-GLOBALROUTETABLE-MIB", "alaGrtRouteVrfName"),
        ("ALCATEL-IND1-GLOBALROUTETABLE-MIB", "alaGrtRouteIsid"))
)
if mibBuilder.loadTexts:
    alaGrtConfigMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

alaGrtCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 16, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    alaGrtCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-IND1-GLOBALROUTETABLE-MIB",
    **{"AlaGrtRouteDistinguisher": AlaGrtRouteDistinguisher,
       "alcatelIND1GRTMIB": alcatelIND1GRTMIB,
       "alcatelIND1GRTMIBObjects": alcatelIND1GRTMIBObjects,
       "alaGrtConfig": alaGrtConfig,
       "alaGrtRouteTable": alaGrtRouteTable,
       "alaGrtRouteEntry": alaGrtRouteEntry,
       "alaGrtRouteDistinguisher": alaGrtRouteDistinguisher,
       "alaGrtRouteDest": alaGrtRouteDest,
       "alaGrtRouteMaskLen": alaGrtRouteMaskLen,
       "alaGrtRouteNextHop": alaGrtRouteNextHop,
       "alaGrtRouteMetric": alaGrtRouteMetric,
       "alaGrtRouteTag": alaGrtRouteTag,
       "alaGrtRouteVrfName": alaGrtRouteVrfName,
       "alaGrtRouteIsid": alaGrtRouteIsid,
       "alcatelIND1GRTMIBConformance": alcatelIND1GRTMIBConformance,
       "alcatelIND1GRTMIBCompliances": alcatelIND1GRTMIBCompliances,
       "alaGrtCompliance": alaGrtCompliance,
       "alcatelIND1GRTMIBGroups": alcatelIND1GRTMIBGroups,
       "alaGrtConfigMIBGroup": alaGrtConfigMIBGroup}
)
