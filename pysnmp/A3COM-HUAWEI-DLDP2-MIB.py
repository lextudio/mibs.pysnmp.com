# SNMP MIB module (A3COM-HUAWEI-DLDP2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM-HUAWEI-DLDP2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:27:33 2024
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

(h3cCommon,) = mibBuilder.importSymbols(
    "A3COM-HUAWEI-OID-MIB",
    "h3cCommon")

(ifDescr,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifDescr",
    "ifIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

h3cDldp2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 117)
)
h3cDldp2.setRevisions(
        ("2011-12-26 15:30",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cDldp2ScalarGroup_ObjectIdentity = ObjectIdentity
h3cDldp2ScalarGroup = _H3cDldp2ScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 117, 1)
)
_H3cDldp2GlobalEnable_Type = TruthValue
_H3cDldp2GlobalEnable_Object = MibScalar
h3cDldp2GlobalEnable = _H3cDldp2GlobalEnable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 117, 1, 1),
    _H3cDldp2GlobalEnable_Type()
)
h3cDldp2GlobalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDldp2GlobalEnable.setStatus("current")


class _H3cDldp2Interval_Type(Integer32):
    """Custom type h3cDldp2Interval based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_H3cDldp2Interval_Type.__name__ = "Integer32"
_H3cDldp2Interval_Object = MibScalar
h3cDldp2Interval = _H3cDldp2Interval_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 117, 1, 2),
    _H3cDldp2Interval_Type()
)
h3cDldp2Interval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDldp2Interval.setStatus("current")
if mibBuilder.loadTexts:
    h3cDldp2Interval.setUnits("second")


class _H3cDldp2AuthMode_Type(Integer32):
    """Custom type h3cDldp2AuthMode based on Integer32"""
    defaultValue = 2

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
        *(("md5", 4),
          ("none", 2),
          ("simple", 3),
          ("unknown", 1))
    )


_H3cDldp2AuthMode_Type.__name__ = "Integer32"
_H3cDldp2AuthMode_Object = MibScalar
h3cDldp2AuthMode = _H3cDldp2AuthMode_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 117, 1, 3),
    _H3cDldp2AuthMode_Type()
)
h3cDldp2AuthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDldp2AuthMode.setStatus("current")


class _H3cDldp2AuthPassword_Type(OctetString):
    """Custom type h3cDldp2AuthPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_H3cDldp2AuthPassword_Type.__name__ = "OctetString"
_H3cDldp2AuthPassword_Object = MibScalar
h3cDldp2AuthPassword = _H3cDldp2AuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 117, 1, 4),
    _H3cDldp2AuthPassword_Type()
)
h3cDldp2AuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDldp2AuthPassword.setStatus("current")


class _H3cDldp2UniShutdown_Type(Integer32):
    """Custom type h3cDldp2UniShutdown based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 2),
          ("manual", 3),
          ("unknown", 1))
    )


_H3cDldp2UniShutdown_Type.__name__ = "Integer32"
_H3cDldp2UniShutdown_Object = MibScalar
h3cDldp2UniShutdown = _H3cDldp2UniShutdown_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 117, 1, 5),
    _H3cDldp2UniShutdown_Type()
)
h3cDldp2UniShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDldp2UniShutdown.setStatus("current")
_H3cDldp2TableGroup_ObjectIdentity = ObjectIdentity
h3cDldp2TableGroup = _H3cDldp2TableGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 117, 2)
)
_H3cDldp2PortConfigTable_Object = MibTable
h3cDldp2PortConfigTable = _H3cDldp2PortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 117, 2, 1)
)
if mibBuilder.loadTexts:
    h3cDldp2PortConfigTable.setStatus("current")
_H3cDldp2PortConfigEntry_Object = MibTableRow
h3cDldp2PortConfigEntry = _H3cDldp2PortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 117, 2, 1, 1)
)
h3cDldp2PortConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cDldp2PortConfigEntry.setStatus("current")
_H3cDldp2PortEnable_Type = TruthValue
_H3cDldp2PortEnable_Object = MibTableColumn
h3cDldp2PortEnable = _H3cDldp2PortEnable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 117, 2, 1, 1, 1),
    _H3cDldp2PortEnable_Type()
)
h3cDldp2PortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cDldp2PortEnable.setStatus("current")
_H3cDldp2PortStatusTable_Object = MibTable
h3cDldp2PortStatusTable = _H3cDldp2PortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 117, 2, 2)
)
if mibBuilder.loadTexts:
    h3cDldp2PortStatusTable.setStatus("current")
_H3cDldp2PortStatusEntry_Object = MibTableRow
h3cDldp2PortStatusEntry = _H3cDldp2PortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 117, 2, 2, 1)
)
h3cDldp2PortStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cDldp2PortStatusEntry.setStatus("current")


class _H3cDldp2PortOperStatus_Type(Integer32):
    """Custom type h3cDldp2PortOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("bidirectional", 5),
          ("inactive", 3),
          ("initial", 2),
          ("unidirectional", 4),
          ("unknown", 1))
    )


_H3cDldp2PortOperStatus_Type.__name__ = "Integer32"
_H3cDldp2PortOperStatus_Object = MibTableColumn
h3cDldp2PortOperStatus = _H3cDldp2PortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 117, 2, 2, 1, 1),
    _H3cDldp2PortOperStatus_Type()
)
h3cDldp2PortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDldp2PortOperStatus.setStatus("current")


class _H3cDldp2PortLinkStatus_Type(Integer32):
    """Custom type h3cDldp2PortLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("unknown", 1),
          ("up", 3))
    )


_H3cDldp2PortLinkStatus_Type.__name__ = "Integer32"
_H3cDldp2PortLinkStatus_Object = MibTableColumn
h3cDldp2PortLinkStatus = _H3cDldp2PortLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 117, 2, 2, 1, 2),
    _H3cDldp2PortLinkStatus_Type()
)
h3cDldp2PortLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDldp2PortLinkStatus.setStatus("current")
_H3cDldp2NeighborTable_Object = MibTable
h3cDldp2NeighborTable = _H3cDldp2NeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 117, 2, 3)
)
if mibBuilder.loadTexts:
    h3cDldp2NeighborTable.setStatus("current")
_H3cDldp2NeighborEntry_Object = MibTableRow
h3cDldp2NeighborEntry = _H3cDldp2NeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 117, 2, 3, 1)
)
h3cDldp2NeighborEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "A3COM-HUAWEI-DLDP2-MIB", "h3cDldp2NeighborBridgeMac"),
    (0, "A3COM-HUAWEI-DLDP2-MIB", "h3cDldp2NeighborPortIndex"),
)
if mibBuilder.loadTexts:
    h3cDldp2NeighborEntry.setStatus("current")
_H3cDldp2NeighborBridgeMac_Type = MacAddress
_H3cDldp2NeighborBridgeMac_Object = MibTableColumn
h3cDldp2NeighborBridgeMac = _H3cDldp2NeighborBridgeMac_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 117, 2, 3, 1, 1),
    _H3cDldp2NeighborBridgeMac_Type()
)
h3cDldp2NeighborBridgeMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDldp2NeighborBridgeMac.setStatus("current")


class _H3cDldp2NeighborPortIndex_Type(Integer32):
    """Custom type h3cDldp2NeighborPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_H3cDldp2NeighborPortIndex_Type.__name__ = "Integer32"
_H3cDldp2NeighborPortIndex_Object = MibTableColumn
h3cDldp2NeighborPortIndex = _H3cDldp2NeighborPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 117, 2, 3, 1, 2),
    _H3cDldp2NeighborPortIndex_Type()
)
h3cDldp2NeighborPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cDldp2NeighborPortIndex.setStatus("current")


class _H3cDldp2NeighborStatus_Type(Integer32):
    """Custom type h3cDldp2NeighborStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("confirmed", 3),
          ("unconfirmed", 2),
          ("unknown", 1))
    )


_H3cDldp2NeighborStatus_Type.__name__ = "Integer32"
_H3cDldp2NeighborStatus_Object = MibTableColumn
h3cDldp2NeighborStatus = _H3cDldp2NeighborStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 117, 2, 3, 1, 3),
    _H3cDldp2NeighborStatus_Type()
)
h3cDldp2NeighborStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDldp2NeighborStatus.setStatus("current")
_H3cDldp2NeighborAgingTime_Type = Integer32
_H3cDldp2NeighborAgingTime_Object = MibTableColumn
h3cDldp2NeighborAgingTime = _H3cDldp2NeighborAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 117, 2, 3, 1, 4),
    _H3cDldp2NeighborAgingTime_Type()
)
h3cDldp2NeighborAgingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cDldp2NeighborAgingTime.setStatus("current")
if mibBuilder.loadTexts:
    h3cDldp2NeighborAgingTime.setUnits("second")
_H3cDldp2TrapBindObjects_ObjectIdentity = ObjectIdentity
h3cDldp2TrapBindObjects = _H3cDldp2TrapBindObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 117, 3)
)
_H3cDldp2Trap_ObjectIdentity = ObjectIdentity
h3cDldp2Trap = _H3cDldp2Trap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 117, 4)
)
_H3cDldp2TrapPrefix_ObjectIdentity = ObjectIdentity
h3cDldp2TrapPrefix = _H3cDldp2TrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 117, 4, 0)
)

# Managed Objects groups


# Notification objects

h3cDldp2TrapUniLink = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 117, 4, 0, 1)
)
h3cDldp2TrapUniLink.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    h3cDldp2TrapUniLink.setStatus(
        "current"
    )

h3cDldp2TrapBidLink = NotificationType(
    (1, 3, 6, 1, 4, 1, 43, 45, 1, 10, 2, 117, 4, 0, 2)
)
h3cDldp2TrapBidLink.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    h3cDldp2TrapBidLink.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-HUAWEI-DLDP2-MIB",
    **{"h3cDldp2": h3cDldp2,
       "h3cDldp2ScalarGroup": h3cDldp2ScalarGroup,
       "h3cDldp2GlobalEnable": h3cDldp2GlobalEnable,
       "h3cDldp2Interval": h3cDldp2Interval,
       "h3cDldp2AuthMode": h3cDldp2AuthMode,
       "h3cDldp2AuthPassword": h3cDldp2AuthPassword,
       "h3cDldp2UniShutdown": h3cDldp2UniShutdown,
       "h3cDldp2TableGroup": h3cDldp2TableGroup,
       "h3cDldp2PortConfigTable": h3cDldp2PortConfigTable,
       "h3cDldp2PortConfigEntry": h3cDldp2PortConfigEntry,
       "h3cDldp2PortEnable": h3cDldp2PortEnable,
       "h3cDldp2PortStatusTable": h3cDldp2PortStatusTable,
       "h3cDldp2PortStatusEntry": h3cDldp2PortStatusEntry,
       "h3cDldp2PortOperStatus": h3cDldp2PortOperStatus,
       "h3cDldp2PortLinkStatus": h3cDldp2PortLinkStatus,
       "h3cDldp2NeighborTable": h3cDldp2NeighborTable,
       "h3cDldp2NeighborEntry": h3cDldp2NeighborEntry,
       "h3cDldp2NeighborBridgeMac": h3cDldp2NeighborBridgeMac,
       "h3cDldp2NeighborPortIndex": h3cDldp2NeighborPortIndex,
       "h3cDldp2NeighborStatus": h3cDldp2NeighborStatus,
       "h3cDldp2NeighborAgingTime": h3cDldp2NeighborAgingTime,
       "h3cDldp2TrapBindObjects": h3cDldp2TrapBindObjects,
       "h3cDldp2Trap": h3cDldp2Trap,
       "h3cDldp2TrapPrefix": h3cDldp2TrapPrefix,
       "h3cDldp2TrapUniLink": h3cDldp2TrapUniLink,
       "h3cDldp2TrapBidLink": h3cDldp2TrapBidLink}
)
