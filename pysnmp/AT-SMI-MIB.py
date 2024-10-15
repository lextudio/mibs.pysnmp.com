# SNMP MIB module (AT-SMI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AT-SMI-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:42:57 2024
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

alliedTelesis = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207)
)
alliedTelesis.setRevisions(
        ("2010-06-15 00:15",
         "2008-02-28 00:00",
         "2006-06-14 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class DisplayStringUnsized(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"


# MIB Managed Objects in the order of their OIDs

_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1)
)
if mibBuilder.loadTexts:
    products.setStatus("current")
_MibObject_ObjectIdentity = ObjectIdentity
mibObject = _MibObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8)
)
if mibBuilder.loadTexts:
    mibObject.setStatus("current")
_BrouterMib_ObjectIdentity = ObjectIdentity
brouterMib = _BrouterMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4)
)
if mibBuilder.loadTexts:
    brouterMib.setStatus("current")
_AtRouter_ObjectIdentity = ObjectIdentity
atRouter = _AtRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4)
)
if mibBuilder.loadTexts:
    atRouter.setStatus("current")
_Objects_ObjectIdentity = ObjectIdentity
objects = _Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 1)
)
if mibBuilder.loadTexts:
    objects.setStatus("current")
_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 2)
)
if mibBuilder.loadTexts:
    traps.setStatus("current")
_Sysinfo_ObjectIdentity = ObjectIdentity
sysinfo = _Sysinfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 3)
)
if mibBuilder.loadTexts:
    sysinfo.setStatus("current")
_Modules_ObjectIdentity = ObjectIdentity
modules = _Modules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4)
)
if mibBuilder.loadTexts:
    modules.setStatus("current")
_ArInterfaces_ObjectIdentity = ObjectIdentity
arInterfaces = _ArInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 5)
)
if mibBuilder.loadTexts:
    arInterfaces.setStatus("current")
_Protocols_ObjectIdentity = ObjectIdentity
protocols = _Protocols_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 6)
)
if mibBuilder.loadTexts:
    protocols.setStatus("current")
_AtAgents_ObjectIdentity = ObjectIdentity
atAgents = _AtAgents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 7)
)
if mibBuilder.loadTexts:
    atAgents.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AT-SMI-MIB",
    **{"DisplayStringUnsized": DisplayStringUnsized,
       "alliedTelesis": alliedTelesis,
       "products": products,
       "mibObject": mibObject,
       "brouterMib": brouterMib,
       "atRouter": atRouter,
       "objects": objects,
       "traps": traps,
       "sysinfo": sysinfo,
       "modules": modules,
       "arInterfaces": arInterfaces,
       "protocols": protocols,
       "atAgents": atAgents}
)
