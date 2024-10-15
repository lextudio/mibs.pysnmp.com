# SNMP MIB module (TOKENRING-STATION-SR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TOKENRING-STATION-SR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:05:34 2024
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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

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

dot5SrMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 42)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SourceRoute(OctetString, TextualConvention):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )



# MIB Managed Objects in the order of their OIDs

_Dot5SrMIBObjects_ObjectIdentity = ObjectIdentity
dot5SrMIBObjects = _Dot5SrMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 42, 1)
)
_Dot5SrRouteTable_Object = MibTable
dot5SrRouteTable = _Dot5SrRouteTable_Object(
    (1, 3, 6, 1, 2, 1, 42, 1, 1)
)
if mibBuilder.loadTexts:
    dot5SrRouteTable.setStatus("current")
_Dot5SrRouteEntry_Object = MibTableRow
dot5SrRouteEntry = _Dot5SrRouteEntry_Object(
    (1, 3, 6, 1, 2, 1, 42, 1, 1, 1)
)
dot5SrRouteEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TOKENRING-STATION-SR-MIB", "dot5SrRouteDestination"),
)
if mibBuilder.loadTexts:
    dot5SrRouteEntry.setStatus("current")
_Dot5SrRouteDestination_Type = MacAddress
_Dot5SrRouteDestination_Object = MibTableColumn
dot5SrRouteDestination = _Dot5SrRouteDestination_Object(
    (1, 3, 6, 1, 2, 1, 42, 1, 1, 1, 2),
    _Dot5SrRouteDestination_Type()
)
dot5SrRouteDestination.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot5SrRouteDestination.setStatus("current")


class _Dot5SrRouteControl_Type(OctetString):
    """Custom type dot5SrRouteControl based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_Dot5SrRouteControl_Type.__name__ = "OctetString"
_Dot5SrRouteControl_Object = MibTableColumn
dot5SrRouteControl = _Dot5SrRouteControl_Object(
    (1, 3, 6, 1, 2, 1, 42, 1, 1, 1, 3),
    _Dot5SrRouteControl_Type()
)
dot5SrRouteControl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot5SrRouteControl.setStatus("current")
_Dot5SrRouteDescr_Type = SourceRoute
_Dot5SrRouteDescr_Object = MibTableColumn
dot5SrRouteDescr = _Dot5SrRouteDescr_Object(
    (1, 3, 6, 1, 2, 1, 42, 1, 1, 1, 4),
    _Dot5SrRouteDescr_Type()
)
dot5SrRouteDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot5SrRouteDescr.setStatus("current")
_Dot5SrRouteStatus_Type = RowStatus
_Dot5SrRouteStatus_Object = MibTableColumn
dot5SrRouteStatus = _Dot5SrRouteStatus_Object(
    (1, 3, 6, 1, 2, 1, 42, 1, 1, 1, 5),
    _Dot5SrRouteStatus_Type()
)
dot5SrRouteStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dot5SrRouteStatus.setStatus("current")
_Dot5SrConformance_ObjectIdentity = ObjectIdentity
dot5SrConformance = _Dot5SrConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 42, 2)
)
_Dot5SrGroups_ObjectIdentity = ObjectIdentity
dot5SrGroups = _Dot5SrGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 42, 2, 1)
)
_Dot5SrCompliances_ObjectIdentity = ObjectIdentity
dot5SrCompliances = _Dot5SrCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 42, 2, 2)
)

# Managed Objects groups

dot5SrRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 42, 2, 1, 1)
)
dot5SrRouteGroup.setObjects(
      *(("TOKENRING-STATION-SR-MIB", "dot5SrRouteControl"),
        ("TOKENRING-STATION-SR-MIB", "dot5SrRouteDescr"),
        ("TOKENRING-STATION-SR-MIB", "dot5SrRouteStatus"))
)
if mibBuilder.loadTexts:
    dot5SrRouteGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dot5SrCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 42, 2, 2, 1)
)
if mibBuilder.loadTexts:
    dot5SrCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TOKENRING-STATION-SR-MIB",
    **{"SourceRoute": SourceRoute,
       "dot5SrMIB": dot5SrMIB,
       "dot5SrMIBObjects": dot5SrMIBObjects,
       "dot5SrRouteTable": dot5SrRouteTable,
       "dot5SrRouteEntry": dot5SrRouteEntry,
       "dot5SrRouteDestination": dot5SrRouteDestination,
       "dot5SrRouteControl": dot5SrRouteControl,
       "dot5SrRouteDescr": dot5SrRouteDescr,
       "dot5SrRouteStatus": dot5SrRouteStatus,
       "dot5SrConformance": dot5SrConformance,
       "dot5SrGroups": dot5SrGroups,
       "dot5SrRouteGroup": dot5SrRouteGroup,
       "dot5SrCompliances": dot5SrCompliances,
       "dot5SrCompliance": dot5SrCompliance}
)
