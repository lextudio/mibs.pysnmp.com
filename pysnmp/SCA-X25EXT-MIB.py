# SNMP MIB module (SCA-X25EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SCA-X25EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:49:57 2024
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

(scanet,) = mibBuilder.importSymbols(
    "SCANET-MIB",
    "scanet")

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



class IfIndexType(Integer32):
    """Custom type IfIndexType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_X25ext_ObjectIdentity = ObjectIdentity
x25ext = _X25ext_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 51)
)
_X25extCircuit_ObjectIdentity = ObjectIdentity
x25extCircuit = _X25extCircuit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 208, 51, 1)
)
_X25extCircuitTable_Object = MibTable
x25extCircuitTable = _X25extCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 208, 51, 1, 1)
)
if mibBuilder.loadTexts:
    x25extCircuitTable.setStatus("mandatory")
_X25extCircuitEntry_Object = MibTableRow
x25extCircuitEntry = _X25extCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 208, 51, 1, 1, 1)
)
x25extCircuitEntry.setIndexNames(
    (0, "SCA-X25EXT-MIB", "x25extCircuitIndex"),
    (0, "SCA-X25EXT-MIB", "x25extCircuitChannel"),
)
if mibBuilder.loadTexts:
    x25extCircuitEntry.setStatus("mandatory")
_X25extCircuitIndex_Type = IfIndexType
_X25extCircuitIndex_Object = MibTableColumn
x25extCircuitIndex = _X25extCircuitIndex_Object(
    (1, 3, 6, 1, 4, 1, 208, 51, 1, 1, 1, 1),
    _X25extCircuitIndex_Type()
)
x25extCircuitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25extCircuitIndex.setStatus("mandatory")


class _X25extCircuitChannel_Type(Integer32):
    """Custom type x25extCircuitChannel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_X25extCircuitChannel_Type.__name__ = "Integer32"
_X25extCircuitChannel_Object = MibTableColumn
x25extCircuitChannel = _X25extCircuitChannel_Object(
    (1, 3, 6, 1, 4, 1, 208, 51, 1, 1, 1, 2),
    _X25extCircuitChannel_Type()
)
x25extCircuitChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25extCircuitChannel.setStatus("mandatory")
_X25extCircuitLogicalIndex_Type = IfIndexType
_X25extCircuitLogicalIndex_Object = MibTableColumn
x25extCircuitLogicalIndex = _X25extCircuitLogicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 208, 51, 1, 1, 1, 3),
    _X25extCircuitLogicalIndex_Type()
)
x25extCircuitLogicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25extCircuitLogicalIndex.setStatus("mandatory")


class _X25extCircuitPacketSize_Type(Integer32):
    """Custom type x25extCircuitPacketSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_X25extCircuitPacketSize_Type.__name__ = "Integer32"
_X25extCircuitPacketSize_Object = MibTableColumn
x25extCircuitPacketSize = _X25extCircuitPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 208, 51, 1, 1, 1, 4),
    _X25extCircuitPacketSize_Type()
)
x25extCircuitPacketSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25extCircuitPacketSize.setStatus("mandatory")


class _X25extCircuitWindowSize_Type(Integer32):
    """Custom type x25extCircuitWindowSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_X25extCircuitWindowSize_Type.__name__ = "Integer32"
_X25extCircuitWindowSize_Object = MibTableColumn
x25extCircuitWindowSize = _X25extCircuitWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 208, 51, 1, 1, 1, 5),
    _X25extCircuitWindowSize_Type()
)
x25extCircuitWindowSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25extCircuitWindowSize.setStatus("mandatory")
_X25extCircuitTimeout_Type = Integer32
_X25extCircuitTimeout_Object = MibTableColumn
x25extCircuitTimeout = _X25extCircuitTimeout_Object(
    (1, 3, 6, 1, 4, 1, 208, 51, 1, 1, 1, 6),
    _X25extCircuitTimeout_Type()
)
x25extCircuitTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25extCircuitTimeout.setStatus("mandatory")
_X25extCircuitOutResets_Type = Counter32
_X25extCircuitOutResets_Object = MibTableColumn
x25extCircuitOutResets = _X25extCircuitOutResets_Object(
    (1, 3, 6, 1, 4, 1, 208, 51, 1, 1, 1, 7),
    _X25extCircuitOutResets_Type()
)
x25extCircuitOutResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25extCircuitOutResets.setStatus("mandatory")
_X25extCircuitOutFlowStuckResets_Type = Counter32
_X25extCircuitOutFlowStuckResets_Object = MibTableColumn
x25extCircuitOutFlowStuckResets = _X25extCircuitOutFlowStuckResets_Object(
    (1, 3, 6, 1, 4, 1, 208, 51, 1, 1, 1, 8),
    _X25extCircuitOutFlowStuckResets_Type()
)
x25extCircuitOutFlowStuckResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25extCircuitOutFlowStuckResets.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SCA-X25EXT-MIB",
    **{"IfIndexType": IfIndexType,
       "x25ext": x25ext,
       "x25extCircuit": x25extCircuit,
       "x25extCircuitTable": x25extCircuitTable,
       "x25extCircuitEntry": x25extCircuitEntry,
       "x25extCircuitIndex": x25extCircuitIndex,
       "x25extCircuitChannel": x25extCircuitChannel,
       "x25extCircuitLogicalIndex": x25extCircuitLogicalIndex,
       "x25extCircuitPacketSize": x25extCircuitPacketSize,
       "x25extCircuitWindowSize": x25extCircuitWindowSize,
       "x25extCircuitTimeout": x25extCircuitTimeout,
       "x25extCircuitOutResets": x25extCircuitOutResets,
       "x25extCircuitOutFlowStuckResets": x25extCircuitOutFlowStuckResets}
)
