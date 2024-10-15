# SNMP MIB module (ARISTA-VRF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ARISTA-VRF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:40:30 2024
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

(aristaMibs,) = mibBuilder.importSymbols(
    "ARISTA-SMI-MIB",
    "aristaMibs")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

aristaVrfMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 18)
)
aristaVrfMIB.setRevisions(
        ("2015-01-11 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class VrfName(OctetString, TextualConvention):
    status = "current"
    displayHint = "100t"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )



class VrfRouteDistinguisher(OctetString, TextualConvention):
    status = "current"
    displayHint = "256a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class VrfState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )



# MIB Managed Objects in the order of their OIDs

_AristaVrfMibObjects_ObjectIdentity = ObjectIdentity
aristaVrfMibObjects = _AristaVrfMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 18, 1)
)
_AristaVrfTable_Object = MibTable
aristaVrfTable = _AristaVrfTable_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 18, 1, 1)
)
if mibBuilder.loadTexts:
    aristaVrfTable.setStatus("current")
_AristaVrfEntry_Object = MibTableRow
aristaVrfEntry = _AristaVrfEntry_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 18, 1, 1, 1)
)
aristaVrfEntry.setIndexNames(
    (0, "ARISTA-VRF-MIB", "aristaVrfName"),
)
if mibBuilder.loadTexts:
    aristaVrfEntry.setStatus("current")
_AristaVrfName_Type = VrfName
_AristaVrfName_Object = MibTableColumn
aristaVrfName = _AristaVrfName_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 18, 1, 1, 1, 1),
    _AristaVrfName_Type()
)
aristaVrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aristaVrfName.setStatus("current")


class _AristaVrfRoutingStatus_Type(Bits):
    """Custom type aristaVrfRoutingStatus based on Bits"""
    namedValues = NamedValues(
        *(("ipv4", 0),
          ("ipv6", 1))
    )

_AristaVrfRoutingStatus_Type.__name__ = "Bits"
_AristaVrfRoutingStatus_Object = MibTableColumn
aristaVrfRoutingStatus = _AristaVrfRoutingStatus_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 18, 1, 1, 1, 2),
    _AristaVrfRoutingStatus_Type()
)
aristaVrfRoutingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaVrfRoutingStatus.setStatus("current")
_AristaVrfRouteDistinguisher_Type = VrfRouteDistinguisher
_AristaVrfRouteDistinguisher_Object = MibTableColumn
aristaVrfRouteDistinguisher = _AristaVrfRouteDistinguisher_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 18, 1, 1, 1, 3),
    _AristaVrfRouteDistinguisher_Type()
)
aristaVrfRouteDistinguisher.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaVrfRouteDistinguisher.setStatus("current")
_AristaVrfState_Type = VrfState
_AristaVrfState_Object = MibTableColumn
aristaVrfState = _AristaVrfState_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 18, 1, 1, 1, 4),
    _AristaVrfState_Type()
)
aristaVrfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaVrfState.setStatus("current")
_AristaVrfIfTable_Object = MibTable
aristaVrfIfTable = _AristaVrfIfTable_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 18, 1, 2)
)
if mibBuilder.loadTexts:
    aristaVrfIfTable.setStatus("current")
_AristaVrfIfEntry_Object = MibTableRow
aristaVrfIfEntry = _AristaVrfIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 18, 1, 2, 1)
)
aristaVrfIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    aristaVrfIfEntry.setStatus("current")
_AristaVrfIfMembership_Type = VrfName
_AristaVrfIfMembership_Object = MibTableColumn
aristaVrfIfMembership = _AristaVrfIfMembership_Object(
    (1, 3, 6, 1, 4, 1, 30065, 3, 18, 1, 2, 1, 1),
    _AristaVrfIfMembership_Type()
)
aristaVrfIfMembership.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aristaVrfIfMembership.setStatus("current")
_AristaVrfMibConformance_ObjectIdentity = ObjectIdentity
aristaVrfMibConformance = _AristaVrfMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 18, 2)
)
_AristaVrfMibCompliances_ObjectIdentity = ObjectIdentity
aristaVrfMibCompliances = _AristaVrfMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 18, 2, 1)
)
_AristaVrfMibGroups_ObjectIdentity = ObjectIdentity
aristaVrfMibGroups = _AristaVrfMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30065, 3, 18, 2, 2)
)

# Managed Objects groups

aristaVrfInformationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30065, 3, 18, 2, 2, 1)
)
aristaVrfInformationGroup.setObjects(
      *(("ARISTA-VRF-MIB", "aristaVrfRoutingStatus"),
        ("ARISTA-VRF-MIB", "aristaVrfRouteDistinguisher"),
        ("ARISTA-VRF-MIB", "aristaVrfState"),
        ("ARISTA-VRF-MIB", "aristaVrfIfMembership"))
)
if mibBuilder.loadTexts:
    aristaVrfInformationGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

aristaVrfMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 30065, 3, 18, 2, 1, 1)
)
if mibBuilder.loadTexts:
    aristaVrfMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARISTA-VRF-MIB",
    **{"VrfName": VrfName,
       "VrfRouteDistinguisher": VrfRouteDistinguisher,
       "VrfState": VrfState,
       "aristaVrfMIB": aristaVrfMIB,
       "aristaVrfMibObjects": aristaVrfMibObjects,
       "aristaVrfTable": aristaVrfTable,
       "aristaVrfEntry": aristaVrfEntry,
       "aristaVrfName": aristaVrfName,
       "aristaVrfRoutingStatus": aristaVrfRoutingStatus,
       "aristaVrfRouteDistinguisher": aristaVrfRouteDistinguisher,
       "aristaVrfState": aristaVrfState,
       "aristaVrfIfTable": aristaVrfIfTable,
       "aristaVrfIfEntry": aristaVrfIfEntry,
       "aristaVrfIfMembership": aristaVrfIfMembership,
       "aristaVrfMibConformance": aristaVrfMibConformance,
       "aristaVrfMibCompliances": aristaVrfMibCompliances,
       "aristaVrfMibCompliance": aristaVrfMibCompliance,
       "aristaVrfMibGroups": aristaVrfMibGroups,
       "aristaVrfInformationGroup": aristaVrfInformationGroup}
)
