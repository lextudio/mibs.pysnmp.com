# SNMP MIB module (BRIDGEEXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BRIDGEEXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:49:15 2024
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

(bridgeExt,) = mibBuilder.importSymbols(
    "APENT-MIB",
    "bridgeExt")

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


# Types definitions



class Timeout(Integer32):
    """Custom type Timeout based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ApBridge_ObjectIdentity = ObjectIdentity
apBridge = _ApBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 14, 1)
)


class _ApBridgeMaxAge_Type(Timeout):
    """Custom type apBridgeMaxAge based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 40),
    )


_ApBridgeMaxAge_Type.__name__ = "Timeout"
_ApBridgeMaxAge_Object = MibScalar
apBridgeMaxAge = _ApBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 14, 1, 1),
    _ApBridgeMaxAge_Type()
)
apBridgeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBridgeMaxAge.setStatus("mandatory")


class _ApBridgeHelloTime_Type(Timeout):
    """Custom type apBridgeHelloTime based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ApBridgeHelloTime_Type.__name__ = "Timeout"
_ApBridgeHelloTime_Object = MibScalar
apBridgeHelloTime = _ApBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 14, 1, 2),
    _ApBridgeHelloTime_Type()
)
apBridgeHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBridgeHelloTime.setStatus("mandatory")


class _ApBridgeForwardDelay_Type(Timeout):
    """Custom type apBridgeForwardDelay based on Timeout"""
    subtypeSpec = Timeout.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 30),
    )


_ApBridgeForwardDelay_Type.__name__ = "Timeout"
_ApBridgeForwardDelay_Object = MibScalar
apBridgeForwardDelay = _ApBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 14, 1, 3),
    _ApBridgeForwardDelay_Type()
)
apBridgeForwardDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBridgeForwardDelay.setStatus("mandatory")
_ApBridgePortTable_Object = MibTable
apBridgePortTable = _ApBridgePortTable_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 14, 1, 4)
)
if mibBuilder.loadTexts:
    apBridgePortTable.setStatus("mandatory")
_ApBridgePortEntry_Object = MibTableRow
apBridgePortEntry = _ApBridgePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 14, 1, 4, 1)
)
apBridgePortEntry.setIndexNames(
    (0, "BRIDGEEXT-MIB", "apBridgePort"),
)
if mibBuilder.loadTexts:
    apBridgePortEntry.setStatus("mandatory")
_ApBridgePort_Type = Integer32
_ApBridgePort_Object = MibTableColumn
apBridgePort = _ApBridgePort_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 14, 1, 4, 1, 1),
    _ApBridgePort_Type()
)
apBridgePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apBridgePort.setStatus("mandatory")


class _ApBridgePortVlan_Type(Integer32):
    """Custom type apBridgePortVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_ApBridgePortVlan_Type.__name__ = "Integer32"
_ApBridgePortVlan_Object = MibTableColumn
apBridgePortVlan = _ApBridgePortVlan_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 14, 1, 4, 1, 2),
    _ApBridgePortVlan_Type()
)
apBridgePortVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBridgePortVlan.setStatus("mandatory")


class _ApBridgeSpanningTreeState_Type(Integer32):
    """Custom type apBridgeSpanningTreeState based on Integer32"""
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


_ApBridgeSpanningTreeState_Type.__name__ = "Integer32"
_ApBridgeSpanningTreeState_Object = MibScalar
apBridgeSpanningTreeState = _ApBridgeSpanningTreeState_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 14, 1, 5),
    _ApBridgeSpanningTreeState_Type()
)
apBridgeSpanningTreeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBridgeSpanningTreeState.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BRIDGEEXT-MIB",
    **{"Timeout": Timeout,
       "apBridge": apBridge,
       "apBridgeMaxAge": apBridgeMaxAge,
       "apBridgeHelloTime": apBridgeHelloTime,
       "apBridgeForwardDelay": apBridgeForwardDelay,
       "apBridgePortTable": apBridgePortTable,
       "apBridgePortEntry": apBridgePortEntry,
       "apBridgePort": apBridgePort,
       "apBridgePortVlan": apBridgePortVlan,
       "apBridgeSpanningTreeState": apBridgeSpanningTreeState}
)
