# SNMP MIB module (ZYXEL-QUEUING-METHOD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-QUEUING-METHOD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:22:41 2024
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

(dot1dBasePort,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dBasePort")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelQueuingMethod = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 70)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelQueuingMethodSetup_ObjectIdentity = ObjectIdentity
zyxelQueuingMethodSetup = _ZyxelQueuingMethodSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 70, 1)
)
_ZyxelQueuingMethodPortTable_Object = MibTable
zyxelQueuingMethodPortTable = _ZyxelQueuingMethodPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 70, 1, 1)
)
if mibBuilder.loadTexts:
    zyxelQueuingMethodPortTable.setStatus("current")
_ZyxelQueuingMethodPortEntry_Object = MibTableRow
zyxelQueuingMethodPortEntry = _ZyxelQueuingMethodPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 70, 1, 1, 1)
)
zyxelQueuingMethodPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "ZYXEL-QUEUING-METHOD-MIB", "zyQueuingMethodPortQueue"),
)
if mibBuilder.loadTexts:
    zyxelQueuingMethodPortEntry.setStatus("current")
_ZyQueuingMethodPortQueue_Type = Integer32
_ZyQueuingMethodPortQueue_Object = MibTableColumn
zyQueuingMethodPortQueue = _ZyQueuingMethodPortQueue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 70, 1, 1, 1, 1),
    _ZyQueuingMethodPortQueue_Type()
)
zyQueuingMethodPortQueue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyQueuingMethodPortQueue.setStatus("current")
_ZyQueuingMethodPortWeight_Type = Integer32
_ZyQueuingMethodPortWeight_Object = MibTableColumn
zyQueuingMethodPortWeight = _ZyQueuingMethodPortWeight_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 70, 1, 1, 1, 2),
    _ZyQueuingMethodPortWeight_Type()
)
zyQueuingMethodPortWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyQueuingMethodPortWeight.setStatus("current")


class _ZyQueuingMethodPortMode_Type(Integer32):
    """Custom type zyQueuingMethodPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("strictlyPriority", 0),
          ("weightedFairScheduling", 1),
          ("weightedRoundRobin", 2))
    )


_ZyQueuingMethodPortMode_Type.__name__ = "Integer32"
_ZyQueuingMethodPortMode_Object = MibTableColumn
zyQueuingMethodPortMode = _ZyQueuingMethodPortMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 70, 1, 1, 1, 3),
    _ZyQueuingMethodPortMode_Type()
)
zyQueuingMethodPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyQueuingMethodPortMode.setStatus("current")
_ZyxelQueuingMethodHybridSpqPortTable_Object = MibTable
zyxelQueuingMethodHybridSpqPortTable = _ZyxelQueuingMethodHybridSpqPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 70, 1, 2)
)
if mibBuilder.loadTexts:
    zyxelQueuingMethodHybridSpqPortTable.setStatus("current")
_ZyxelQueuingMethodHybridSpqPortEntry_Object = MibTableRow
zyxelQueuingMethodHybridSpqPortEntry = _ZyxelQueuingMethodHybridSpqPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 70, 1, 2, 1)
)
zyxelQueuingMethodHybridSpqPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    zyxelQueuingMethodHybridSpqPortEntry.setStatus("current")


class _ZyQueuingMethodHybridSpqPortQueue_Type(Integer32):
    """Custom type zyQueuingMethodHybridSpqPortQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("q0", 1),
          ("q1", 2),
          ("q2", 3),
          ("q3", 4),
          ("q4", 5),
          ("q5", 6),
          ("q6", 7),
          ("q7", 8))
    )


_ZyQueuingMethodHybridSpqPortQueue_Type.__name__ = "Integer32"
_ZyQueuingMethodHybridSpqPortQueue_Object = MibTableColumn
zyQueuingMethodHybridSpqPortQueue = _ZyQueuingMethodHybridSpqPortQueue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 70, 1, 2, 1, 1),
    _ZyQueuingMethodHybridSpqPortQueue_Type()
)
zyQueuingMethodHybridSpqPortQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyQueuingMethodHybridSpqPortQueue.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-QUEUING-METHOD-MIB",
    **{"zyxelQueuingMethod": zyxelQueuingMethod,
       "zyxelQueuingMethodSetup": zyxelQueuingMethodSetup,
       "zyxelQueuingMethodPortTable": zyxelQueuingMethodPortTable,
       "zyxelQueuingMethodPortEntry": zyxelQueuingMethodPortEntry,
       "zyQueuingMethodPortQueue": zyQueuingMethodPortQueue,
       "zyQueuingMethodPortWeight": zyQueuingMethodPortWeight,
       "zyQueuingMethodPortMode": zyQueuingMethodPortMode,
       "zyxelQueuingMethodHybridSpqPortTable": zyxelQueuingMethodHybridSpqPortTable,
       "zyxelQueuingMethodHybridSpqPortEntry": zyxelQueuingMethodHybridSpqPortEntry,
       "zyQueuingMethodHybridSpqPortQueue": zyQueuingMethodHybridSpqPortQueue}
)
