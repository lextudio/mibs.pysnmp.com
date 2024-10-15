# SNMP MIB module (HPN-ICF-DLDP2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-DLDP2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:59:46 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

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

hpnicfDldp2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 117)
)
hpnicfDldp2.setRevisions(
        ("2011-12-26 15:30",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfDldp2ScalarGroup_ObjectIdentity = ObjectIdentity
hpnicfDldp2ScalarGroup = _HpnicfDldp2ScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 117, 1)
)
_HpnicfDldp2GlobalEnable_Type = TruthValue
_HpnicfDldp2GlobalEnable_Object = MibScalar
hpnicfDldp2GlobalEnable = _HpnicfDldp2GlobalEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 117, 1, 1),
    _HpnicfDldp2GlobalEnable_Type()
)
hpnicfDldp2GlobalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDldp2GlobalEnable.setStatus("current")


class _HpnicfDldp2Interval_Type(Integer32):
    """Custom type hpnicfDldp2Interval based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HpnicfDldp2Interval_Type.__name__ = "Integer32"
_HpnicfDldp2Interval_Object = MibScalar
hpnicfDldp2Interval = _HpnicfDldp2Interval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 117, 1, 2),
    _HpnicfDldp2Interval_Type()
)
hpnicfDldp2Interval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDldp2Interval.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDldp2Interval.setUnits("second")


class _HpnicfDldp2AuthMode_Type(Integer32):
    """Custom type hpnicfDldp2AuthMode based on Integer32"""
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


_HpnicfDldp2AuthMode_Type.__name__ = "Integer32"
_HpnicfDldp2AuthMode_Object = MibScalar
hpnicfDldp2AuthMode = _HpnicfDldp2AuthMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 117, 1, 3),
    _HpnicfDldp2AuthMode_Type()
)
hpnicfDldp2AuthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDldp2AuthMode.setStatus("current")


class _HpnicfDldp2AuthPassword_Type(OctetString):
    """Custom type hpnicfDldp2AuthPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HpnicfDldp2AuthPassword_Type.__name__ = "OctetString"
_HpnicfDldp2AuthPassword_Object = MibScalar
hpnicfDldp2AuthPassword = _HpnicfDldp2AuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 117, 1, 4),
    _HpnicfDldp2AuthPassword_Type()
)
hpnicfDldp2AuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDldp2AuthPassword.setStatus("current")


class _HpnicfDldp2UniShutdown_Type(Integer32):
    """Custom type hpnicfDldp2UniShutdown based on Integer32"""
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


_HpnicfDldp2UniShutdown_Type.__name__ = "Integer32"
_HpnicfDldp2UniShutdown_Object = MibScalar
hpnicfDldp2UniShutdown = _HpnicfDldp2UniShutdown_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 117, 1, 5),
    _HpnicfDldp2UniShutdown_Type()
)
hpnicfDldp2UniShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDldp2UniShutdown.setStatus("current")
_HpnicfDldp2TableGroup_ObjectIdentity = ObjectIdentity
hpnicfDldp2TableGroup = _HpnicfDldp2TableGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 117, 2)
)
_HpnicfDldp2PortConfigTable_Object = MibTable
hpnicfDldp2PortConfigTable = _HpnicfDldp2PortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 117, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfDldp2PortConfigTable.setStatus("current")
_HpnicfDldp2PortConfigEntry_Object = MibTableRow
hpnicfDldp2PortConfigEntry = _HpnicfDldp2PortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 117, 2, 1, 1)
)
hpnicfDldp2PortConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfDldp2PortConfigEntry.setStatus("current")
_HpnicfDldp2PortEnable_Type = TruthValue
_HpnicfDldp2PortEnable_Object = MibTableColumn
hpnicfDldp2PortEnable = _HpnicfDldp2PortEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 117, 2, 1, 1, 1),
    _HpnicfDldp2PortEnable_Type()
)
hpnicfDldp2PortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfDldp2PortEnable.setStatus("current")
_HpnicfDldp2PortStatusTable_Object = MibTable
hpnicfDldp2PortStatusTable = _HpnicfDldp2PortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 117, 2, 2)
)
if mibBuilder.loadTexts:
    hpnicfDldp2PortStatusTable.setStatus("current")
_HpnicfDldp2PortStatusEntry_Object = MibTableRow
hpnicfDldp2PortStatusEntry = _HpnicfDldp2PortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 117, 2, 2, 1)
)
hpnicfDldp2PortStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpnicfDldp2PortStatusEntry.setStatus("current")


class _HpnicfDldp2PortOperStatus_Type(Integer32):
    """Custom type hpnicfDldp2PortOperStatus based on Integer32"""
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


_HpnicfDldp2PortOperStatus_Type.__name__ = "Integer32"
_HpnicfDldp2PortOperStatus_Object = MibTableColumn
hpnicfDldp2PortOperStatus = _HpnicfDldp2PortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 117, 2, 2, 1, 1),
    _HpnicfDldp2PortOperStatus_Type()
)
hpnicfDldp2PortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDldp2PortOperStatus.setStatus("current")


class _HpnicfDldp2PortLinkStatus_Type(Integer32):
    """Custom type hpnicfDldp2PortLinkStatus based on Integer32"""
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


_HpnicfDldp2PortLinkStatus_Type.__name__ = "Integer32"
_HpnicfDldp2PortLinkStatus_Object = MibTableColumn
hpnicfDldp2PortLinkStatus = _HpnicfDldp2PortLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 117, 2, 2, 1, 2),
    _HpnicfDldp2PortLinkStatus_Type()
)
hpnicfDldp2PortLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDldp2PortLinkStatus.setStatus("current")
_HpnicfDldp2NeighborTable_Object = MibTable
hpnicfDldp2NeighborTable = _HpnicfDldp2NeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 117, 2, 3)
)
if mibBuilder.loadTexts:
    hpnicfDldp2NeighborTable.setStatus("current")
_HpnicfDldp2NeighborEntry_Object = MibTableRow
hpnicfDldp2NeighborEntry = _HpnicfDldp2NeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 117, 2, 3, 1)
)
hpnicfDldp2NeighborEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HPN-ICF-DLDP2-MIB", "hpnicfDldp2NeighborBridgeMac"),
    (0, "HPN-ICF-DLDP2-MIB", "hpnicfDldp2NeighborPortIndex"),
)
if mibBuilder.loadTexts:
    hpnicfDldp2NeighborEntry.setStatus("current")
_HpnicfDldp2NeighborBridgeMac_Type = MacAddress
_HpnicfDldp2NeighborBridgeMac_Object = MibTableColumn
hpnicfDldp2NeighborBridgeMac = _HpnicfDldp2NeighborBridgeMac_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 117, 2, 3, 1, 1),
    _HpnicfDldp2NeighborBridgeMac_Type()
)
hpnicfDldp2NeighborBridgeMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDldp2NeighborBridgeMac.setStatus("current")


class _HpnicfDldp2NeighborPortIndex_Type(Integer32):
    """Custom type hpnicfDldp2NeighborPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfDldp2NeighborPortIndex_Type.__name__ = "Integer32"
_HpnicfDldp2NeighborPortIndex_Object = MibTableColumn
hpnicfDldp2NeighborPortIndex = _HpnicfDldp2NeighborPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 117, 2, 3, 1, 2),
    _HpnicfDldp2NeighborPortIndex_Type()
)
hpnicfDldp2NeighborPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfDldp2NeighborPortIndex.setStatus("current")


class _HpnicfDldp2NeighborStatus_Type(Integer32):
    """Custom type hpnicfDldp2NeighborStatus based on Integer32"""
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


_HpnicfDldp2NeighborStatus_Type.__name__ = "Integer32"
_HpnicfDldp2NeighborStatus_Object = MibTableColumn
hpnicfDldp2NeighborStatus = _HpnicfDldp2NeighborStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 117, 2, 3, 1, 3),
    _HpnicfDldp2NeighborStatus_Type()
)
hpnicfDldp2NeighborStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDldp2NeighborStatus.setStatus("current")
_HpnicfDldp2NeighborAgingTime_Type = Integer32
_HpnicfDldp2NeighborAgingTime_Object = MibTableColumn
hpnicfDldp2NeighborAgingTime = _HpnicfDldp2NeighborAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 117, 2, 3, 1, 4),
    _HpnicfDldp2NeighborAgingTime_Type()
)
hpnicfDldp2NeighborAgingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfDldp2NeighborAgingTime.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfDldp2NeighborAgingTime.setUnits("second")
_HpnicfDldp2TrapBindObjects_ObjectIdentity = ObjectIdentity
hpnicfDldp2TrapBindObjects = _HpnicfDldp2TrapBindObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 117, 3)
)
_HpnicfDldp2Trap_ObjectIdentity = ObjectIdentity
hpnicfDldp2Trap = _HpnicfDldp2Trap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 117, 4)
)
_HpnicfDldp2TrapPrefix_ObjectIdentity = ObjectIdentity
hpnicfDldp2TrapPrefix = _HpnicfDldp2TrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 117, 4, 0)
)

# Managed Objects groups


# Notification objects

hpnicfDldp2TrapUniLink = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 117, 4, 0, 1)
)
hpnicfDldp2TrapUniLink.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hpnicfDldp2TrapUniLink.setStatus(
        "current"
    )

hpnicfDldp2TrapBidLink = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 117, 4, 0, 2)
)
hpnicfDldp2TrapBidLink.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    hpnicfDldp2TrapBidLink.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-DLDP2-MIB",
    **{"hpnicfDldp2": hpnicfDldp2,
       "hpnicfDldp2ScalarGroup": hpnicfDldp2ScalarGroup,
       "hpnicfDldp2GlobalEnable": hpnicfDldp2GlobalEnable,
       "hpnicfDldp2Interval": hpnicfDldp2Interval,
       "hpnicfDldp2AuthMode": hpnicfDldp2AuthMode,
       "hpnicfDldp2AuthPassword": hpnicfDldp2AuthPassword,
       "hpnicfDldp2UniShutdown": hpnicfDldp2UniShutdown,
       "hpnicfDldp2TableGroup": hpnicfDldp2TableGroup,
       "hpnicfDldp2PortConfigTable": hpnicfDldp2PortConfigTable,
       "hpnicfDldp2PortConfigEntry": hpnicfDldp2PortConfigEntry,
       "hpnicfDldp2PortEnable": hpnicfDldp2PortEnable,
       "hpnicfDldp2PortStatusTable": hpnicfDldp2PortStatusTable,
       "hpnicfDldp2PortStatusEntry": hpnicfDldp2PortStatusEntry,
       "hpnicfDldp2PortOperStatus": hpnicfDldp2PortOperStatus,
       "hpnicfDldp2PortLinkStatus": hpnicfDldp2PortLinkStatus,
       "hpnicfDldp2NeighborTable": hpnicfDldp2NeighborTable,
       "hpnicfDldp2NeighborEntry": hpnicfDldp2NeighborEntry,
       "hpnicfDldp2NeighborBridgeMac": hpnicfDldp2NeighborBridgeMac,
       "hpnicfDldp2NeighborPortIndex": hpnicfDldp2NeighborPortIndex,
       "hpnicfDldp2NeighborStatus": hpnicfDldp2NeighborStatus,
       "hpnicfDldp2NeighborAgingTime": hpnicfDldp2NeighborAgingTime,
       "hpnicfDldp2TrapBindObjects": hpnicfDldp2TrapBindObjects,
       "hpnicfDldp2Trap": hpnicfDldp2Trap,
       "hpnicfDldp2TrapPrefix": hpnicfDldp2TrapPrefix,
       "hpnicfDldp2TrapUniLink": hpnicfDldp2TrapUniLink,
       "hpnicfDldp2TrapBidLink": hpnicfDldp2TrapBidLink}
)
