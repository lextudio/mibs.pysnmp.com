# SNMP MIB module (FORE-BRIDGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FORE-BRIDGE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:45:29 2024
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

(BridgeId,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "BridgeId")

(preDot1qVlanMIB,) = mibBuilder.importSymbols(
    "Fore-Common-MIB",
    "preDot1qVlanMIB")

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


# MODULE-IDENTITY

foreBridgeExtensions = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 326, 1, 8, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _BridgeDataSource_Type(DisplayString):
    """Custom type bridgeDataSource based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_BridgeDataSource_Type.__name__ = "DisplayString"
_BridgeDataSource_Object = MibScalar
bridgeDataSource = _BridgeDataSource_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 8, 2, 1),
    _BridgeDataSource_Type()
)
bridgeDataSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeDataSource.setStatus("current")
_BridgeNumberOfEntities_Type = Integer32
_BridgeNumberOfEntities_Object = MibScalar
bridgeNumberOfEntities = _BridgeNumberOfEntities_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 8, 2, 2),
    _BridgeNumberOfEntities_Type()
)
bridgeNumberOfEntities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeNumberOfEntities.setStatus("current")
_BridgeStpAtmPortTable_Object = MibTable
bridgeStpAtmPortTable = _BridgeStpAtmPortTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 8, 2, 3)
)
if mibBuilder.loadTexts:
    bridgeStpAtmPortTable.setStatus("current")
_BridgeStpAtmPortEntry_Object = MibTableRow
bridgeStpAtmPortEntry = _BridgeStpAtmPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 8, 2, 3, 1)
)
bridgeStpAtmPortEntry.setIndexNames(
    (0, "FORE-BRIDGE-MIB", "bridgeStpAtmPort"),
)
if mibBuilder.loadTexts:
    bridgeStpAtmPortEntry.setStatus("current")


class _BridgeStpAtmPort_Type(DisplayString):
    """Custom type bridgeStpAtmPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 35),
    )


_BridgeStpAtmPort_Type.__name__ = "DisplayString"
_BridgeStpAtmPort_Object = MibTableColumn
bridgeStpAtmPort = _BridgeStpAtmPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 8, 2, 3, 1, 1),
    _BridgeStpAtmPort_Type()
)
bridgeStpAtmPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeStpAtmPort.setStatus("current")


class _BridgeStpAtmPortPriority_Type(Integer32):
    """Custom type bridgeStpAtmPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BridgeStpAtmPortPriority_Type.__name__ = "Integer32"
_BridgeStpAtmPortPriority_Object = MibTableColumn
bridgeStpAtmPortPriority = _BridgeStpAtmPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 8, 2, 3, 1, 2),
    _BridgeStpAtmPortPriority_Type()
)
bridgeStpAtmPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeStpAtmPortPriority.setStatus("current")


class _BridgeStpAtmPortState_Type(Integer32):
    """Custom type bridgeStpAtmPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("blocking", 2),
          ("broken", 6),
          ("disabled", 1),
          ("forwarding", 5),
          ("learning", 4),
          ("listening", 3))
    )


_BridgeStpAtmPortState_Type.__name__ = "Integer32"
_BridgeStpAtmPortState_Object = MibTableColumn
bridgeStpAtmPortState = _BridgeStpAtmPortState_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 8, 2, 3, 1, 3),
    _BridgeStpAtmPortState_Type()
)
bridgeStpAtmPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeStpAtmPortState.setStatus("current")


class _BridgeStpAtmPortEnable_Type(Integer32):
    """Custom type bridgeStpAtmPortEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_BridgeStpAtmPortEnable_Type.__name__ = "Integer32"
_BridgeStpAtmPortEnable_Object = MibTableColumn
bridgeStpAtmPortEnable = _BridgeStpAtmPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 8, 2, 3, 1, 4),
    _BridgeStpAtmPortEnable_Type()
)
bridgeStpAtmPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeStpAtmPortEnable.setStatus("current")


class _BridgeStpAtmPortPathCost_Type(Integer32):
    """Custom type bridgeStpAtmPortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BridgeStpAtmPortPathCost_Type.__name__ = "Integer32"
_BridgeStpAtmPortPathCost_Object = MibTableColumn
bridgeStpAtmPortPathCost = _BridgeStpAtmPortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 8, 2, 3, 1, 5),
    _BridgeStpAtmPortPathCost_Type()
)
bridgeStpAtmPortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeStpAtmPortPathCost.setStatus("current")
_BridgeStpAtmPortDesignatedRoot_Type = BridgeId
_BridgeStpAtmPortDesignatedRoot_Object = MibTableColumn
bridgeStpAtmPortDesignatedRoot = _BridgeStpAtmPortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 8, 2, 3, 1, 6),
    _BridgeStpAtmPortDesignatedRoot_Type()
)
bridgeStpAtmPortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeStpAtmPortDesignatedRoot.setStatus("current")


class _BridgeStpAtmPortDesignatedCost_Type(Integer32):
    """Custom type bridgeStpAtmPortDesignatedCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BridgeStpAtmPortDesignatedCost_Type.__name__ = "Integer32"
_BridgeStpAtmPortDesignatedCost_Object = MibTableColumn
bridgeStpAtmPortDesignatedCost = _BridgeStpAtmPortDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 8, 2, 3, 1, 7),
    _BridgeStpAtmPortDesignatedCost_Type()
)
bridgeStpAtmPortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeStpAtmPortDesignatedCost.setStatus("current")
_BridgeStpAtmPortDesignatedBridge_Type = BridgeId
_BridgeStpAtmPortDesignatedBridge_Object = MibTableColumn
bridgeStpAtmPortDesignatedBridge = _BridgeStpAtmPortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 8, 2, 3, 1, 8),
    _BridgeStpAtmPortDesignatedBridge_Type()
)
bridgeStpAtmPortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeStpAtmPortDesignatedBridge.setStatus("current")


class _BridgeStpAtmPortDesignatedPort_Type(OctetString):
    """Custom type bridgeStpAtmPortDesignatedPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_BridgeStpAtmPortDesignatedPort_Type.__name__ = "OctetString"
_BridgeStpAtmPortDesignatedPort_Object = MibTableColumn
bridgeStpAtmPortDesignatedPort = _BridgeStpAtmPortDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 8, 2, 3, 1, 9),
    _BridgeStpAtmPortDesignatedPort_Type()
)
bridgeStpAtmPortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeStpAtmPortDesignatedPort.setStatus("current")
_BridgeStpAtmPortForwardTransitions_Type = Counter32
_BridgeStpAtmPortForwardTransitions_Object = MibTableColumn
bridgeStpAtmPortForwardTransitions = _BridgeStpAtmPortForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 8, 2, 3, 1, 10),
    _BridgeStpAtmPortForwardTransitions_Type()
)
bridgeStpAtmPortForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeStpAtmPortForwardTransitions.setStatus("current")


class _BridgeStpEnable_Type(Integer32):
    """Custom type bridgeStpEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_BridgeStpEnable_Type.__name__ = "Integer32"
_BridgeStpEnable_Object = MibScalar
bridgeStpEnable = _BridgeStpEnable_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 8, 2, 4),
    _BridgeStpEnable_Type()
)
bridgeStpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeStpEnable.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FORE-BRIDGE-MIB",
    **{"foreBridgeExtensions": foreBridgeExtensions,
       "bridgeDataSource": bridgeDataSource,
       "bridgeNumberOfEntities": bridgeNumberOfEntities,
       "bridgeStpAtmPortTable": bridgeStpAtmPortTable,
       "bridgeStpAtmPortEntry": bridgeStpAtmPortEntry,
       "bridgeStpAtmPort": bridgeStpAtmPort,
       "bridgeStpAtmPortPriority": bridgeStpAtmPortPriority,
       "bridgeStpAtmPortState": bridgeStpAtmPortState,
       "bridgeStpAtmPortEnable": bridgeStpAtmPortEnable,
       "bridgeStpAtmPortPathCost": bridgeStpAtmPortPathCost,
       "bridgeStpAtmPortDesignatedRoot": bridgeStpAtmPortDesignatedRoot,
       "bridgeStpAtmPortDesignatedCost": bridgeStpAtmPortDesignatedCost,
       "bridgeStpAtmPortDesignatedBridge": bridgeStpAtmPortDesignatedBridge,
       "bridgeStpAtmPortDesignatedPort": bridgeStpAtmPortDesignatedPort,
       "bridgeStpAtmPortForwardTransitions": bridgeStpAtmPortForwardTransitions,
       "bridgeStpEnable": bridgeStpEnable}
)
