# SNMP MIB module (L2PROTOCOL-TUNNEL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/L2PROTOCOL-TUNNEL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:16:45 2024
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

swL2ProtocolTunnelMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 93)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwL2PTMIBObjects_ObjectIdentity = ObjectIdentity
swL2PTMIBObjects = _SwL2PTMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 93, 1)
)


class _SwL2PTState_Type(Integer32):
    """Custom type swL2PTState based on Integer32"""
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


_SwL2PTState_Type.__name__ = "Integer32"
_SwL2PTState_Object = MibScalar
swL2PTState = _SwL2PTState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 93, 1, 1),
    _SwL2PTState_Type()
)
swL2PTState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PTState.setStatus("current")
_SwL2PTPortTable_Object = MibTable
swL2PTPortTable = _SwL2PTPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 93, 1, 2)
)
if mibBuilder.loadTexts:
    swL2PTPortTable.setStatus("current")
_SwL2PTPortEntry_Object = MibTableRow
swL2PTPortEntry = _SwL2PTPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 93, 1, 2, 1)
)
swL2PTPortEntry.setIndexNames(
    (0, "L2PROTOCOL-TUNNEL-MIB", "swL2PTPortIndex"),
)
if mibBuilder.loadTexts:
    swL2PTPortEntry.setStatus("current")
_SwL2PTPortIndex_Type = Integer32
_SwL2PTPortIndex_Object = MibTableColumn
swL2PTPortIndex = _SwL2PTPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 93, 1, 2, 1, 1),
    _SwL2PTPortIndex_Type()
)
swL2PTPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swL2PTPortIndex.setStatus("current")


class _SwL2PTPortType_Type(Integer32):
    """Custom type swL2PTPortType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nni", 3),
          ("none", 1),
          ("uni", 2))
    )


_SwL2PTPortType_Type.__name__ = "Integer32"
_SwL2PTPortType_Object = MibTableColumn
swL2PTPortType = _SwL2PTPortType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 93, 1, 2, 1, 2),
    _SwL2PTPortType_Type()
)
swL2PTPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PTPortType.setStatus("current")


class _SwL2PTProtocol_Type(Bits):
    """Custom type swL2PTProtocol based on Bits"""
    namedValues = NamedValues(
        *(("gvrp", 1),
          ("mac-01-00-0C-CC-CC-CC", 2),
          ("mac-01-00-0C-CC-CC-CD", 3),
          ("stp", 0))
    )

_SwL2PTProtocol_Type.__name__ = "Bits"
_SwL2PTProtocol_Object = MibTableColumn
swL2PTProtocol = _SwL2PTProtocol_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 93, 1, 2, 1, 3),
    _SwL2PTProtocol_Type()
)
swL2PTProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PTProtocol.setStatus("current")
_SwL2PTThresholdTable_Object = MibTable
swL2PTThresholdTable = _SwL2PTThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 93, 1, 3)
)
if mibBuilder.loadTexts:
    swL2PTThresholdTable.setStatus("current")
_SwL2PTThresholdEntry_Object = MibTableRow
swL2PTThresholdEntry = _SwL2PTThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 93, 1, 3, 1)
)
swL2PTThresholdEntry.setIndexNames(
    (0, "L2PROTOCOL-TUNNEL-MIB", "swL2PTPortIndex"),
    (0, "L2PROTOCOL-TUNNEL-MIB", "swL2PTProtocolIndex"),
)
if mibBuilder.loadTexts:
    swL2PTThresholdEntry.setStatus("current")


class _SwL2PTProtocolIndex_Type(Integer32):
    """Custom type swL2PTProtocolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("gvrp", 2),
          ("mac-01-00-0C-CC-CC-CC", 3),
          ("mac-01-00-0C-CC-CC-CD", 4),
          ("stp", 1))
    )


_SwL2PTProtocolIndex_Type.__name__ = "Integer32"
_SwL2PTProtocolIndex_Object = MibTableColumn
swL2PTProtocolIndex = _SwL2PTProtocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 93, 1, 3, 1, 1),
    _SwL2PTProtocolIndex_Type()
)
swL2PTProtocolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swL2PTProtocolIndex.setStatus("current")


class _SwL2PTDropThreshold_Type(Integer32):
    """Custom type swL2PTDropThreshold based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwL2PTDropThreshold_Type.__name__ = "Integer32"
_SwL2PTDropThreshold_Object = MibTableColumn
swL2PTDropThreshold = _SwL2PTDropThreshold_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 93, 1, 3, 1, 2),
    _SwL2PTDropThreshold_Type()
)
swL2PTDropThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swL2PTDropThreshold.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "L2PROTOCOL-TUNNEL-MIB",
    **{"swL2ProtocolTunnelMIB": swL2ProtocolTunnelMIB,
       "swL2PTMIBObjects": swL2PTMIBObjects,
       "swL2PTState": swL2PTState,
       "swL2PTPortTable": swL2PTPortTable,
       "swL2PTPortEntry": swL2PTPortEntry,
       "swL2PTPortIndex": swL2PTPortIndex,
       "swL2PTPortType": swL2PTPortType,
       "swL2PTProtocol": swL2PTProtocol,
       "swL2PTThresholdTable": swL2PTThresholdTable,
       "swL2PTThresholdEntry": swL2PTThresholdEntry,
       "swL2PTProtocolIndex": swL2PTProtocolIndex,
       "swL2PTDropThreshold": swL2PTDropThreshold}
)
