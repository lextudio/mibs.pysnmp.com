# SNMP MIB module (HP-ICF-DLDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-ICF-DLDP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:57:22 2024
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

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

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
 MacAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hpicfDldpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108)
)
hpicfDldpMIB.setRevisions(
        ("2014-03-07 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfDldpNotifications_ObjectIdentity = ObjectIdentity
hpicfDldpNotifications = _HpicfDldpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 0)
)
_HpicfDldpConfigurationObjects_ObjectIdentity = ObjectIdentity
hpicfDldpConfigurationObjects = _HpicfDldpConfigurationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 1)
)
_HpicfDldpScalars_ObjectIdentity = ObjectIdentity
hpicfDldpScalars = _HpicfDldpScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 1, 1)
)
_HpicfDldpGlobalEnable_Type = TruthValue
_HpicfDldpGlobalEnable_Object = MibScalar
hpicfDldpGlobalEnable = _HpicfDldpGlobalEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 1, 1, 1),
    _HpicfDldpGlobalEnable_Type()
)
hpicfDldpGlobalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDldpGlobalEnable.setStatus("current")


class _HpicfDldpInterval_Type(Integer32):
    """Custom type hpicfDldpInterval based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HpicfDldpInterval_Type.__name__ = "Integer32"
_HpicfDldpInterval_Object = MibScalar
hpicfDldpInterval = _HpicfDldpInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 1, 1, 2),
    _HpicfDldpInterval_Type()
)
hpicfDldpInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDldpInterval.setStatus("current")


class _HpicfDldpAuthMode_Type(Integer32):
    """Custom type hpicfDldpAuthMode based on Integer32"""
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


_HpicfDldpAuthMode_Type.__name__ = "Integer32"
_HpicfDldpAuthMode_Object = MibScalar
hpicfDldpAuthMode = _HpicfDldpAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 1, 1, 3),
    _HpicfDldpAuthMode_Type()
)
hpicfDldpAuthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDldpAuthMode.setStatus("current")


class _HpicfDldpAuthPassword_Type(OctetString):
    """Custom type hpicfDldpAuthPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HpicfDldpAuthPassword_Type.__name__ = "OctetString"
_HpicfDldpAuthPassword_Object = MibScalar
hpicfDldpAuthPassword = _HpicfDldpAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 1, 1, 4),
    _HpicfDldpAuthPassword_Type()
)
hpicfDldpAuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDldpAuthPassword.setStatus("current")


class _HpicfDldpAuthPasswordEncrypted_Type(OctetString):
    """Custom type hpicfDldpAuthPasswordEncrypted based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HpicfDldpAuthPasswordEncrypted_Type.__name__ = "OctetString"
_HpicfDldpAuthPasswordEncrypted_Object = MibScalar
hpicfDldpAuthPasswordEncrypted = _HpicfDldpAuthPasswordEncrypted_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 1, 1, 5),
    _HpicfDldpAuthPasswordEncrypted_Type()
)
hpicfDldpAuthPasswordEncrypted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDldpAuthPasswordEncrypted.setStatus("current")


class _HpicfDldpUniShutdown_Type(Integer32):
    """Custom type hpicfDldpUniShutdown based on Integer32"""
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


_HpicfDldpUniShutdown_Type.__name__ = "Integer32"
_HpicfDldpUniShutdown_Object = MibScalar
hpicfDldpUniShutdown = _HpicfDldpUniShutdown_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 1, 1, 6),
    _HpicfDldpUniShutdown_Type()
)
hpicfDldpUniShutdown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDldpUniShutdown.setStatus("current")


class _HpicfDldpDelayDownInterval_Type(Integer32):
    """Custom type hpicfDldpDelayDownInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HpicfDldpDelayDownInterval_Type.__name__ = "Integer32"
_HpicfDldpDelayDownInterval_Object = MibScalar
hpicfDldpDelayDownInterval = _HpicfDldpDelayDownInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 1, 1, 7),
    _HpicfDldpDelayDownInterval_Type()
)
hpicfDldpDelayDownInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDldpDelayDownInterval.setStatus("current")
_HpicfDldpPortConfigTable_Object = MibTable
hpicfDldpPortConfigTable = _HpicfDldpPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 1, 2)
)
if mibBuilder.loadTexts:
    hpicfDldpPortConfigTable.setStatus("current")
_HpicfDldpPortConfigEntry_Object = MibTableRow
hpicfDldpPortConfigEntry = _HpicfDldpPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 1, 2, 1)
)
hpicfDldpPortConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpicfDldpPortConfigEntry.setStatus("current")
_HpicfDldpPortEnable_Type = TruthValue
_HpicfDldpPortEnable_Object = MibTableColumn
hpicfDldpPortEnable = _HpicfDldpPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 1, 2, 1, 1),
    _HpicfDldpPortEnable_Type()
)
hpicfDldpPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDldpPortEnable.setStatus("current")
_HpicfDldpPortStatusTable_Object = MibTable
hpicfDldpPortStatusTable = _HpicfDldpPortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 1, 3)
)
if mibBuilder.loadTexts:
    hpicfDldpPortStatusTable.setStatus("current")
_HpicfDldpPortStatusEntry_Object = MibTableRow
hpicfDldpPortStatusEntry = _HpicfDldpPortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 1, 3, 1)
)
hpicfDldpPortStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpicfDldpPortStatusEntry.setStatus("current")


class _HpicfDldpPortOperStatus_Type(Integer32):
    """Custom type hpicfDldpPortOperStatus based on Integer32"""
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


_HpicfDldpPortOperStatus_Type.__name__ = "Integer32"
_HpicfDldpPortOperStatus_Object = MibTableColumn
hpicfDldpPortOperStatus = _HpicfDldpPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 1, 3, 1, 1),
    _HpicfDldpPortOperStatus_Type()
)
hpicfDldpPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDldpPortOperStatus.setStatus("current")


class _HpicfDldpPortLinkStatus_Type(Integer32):
    """Custom type hpicfDldpPortLinkStatus based on Integer32"""
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


_HpicfDldpPortLinkStatus_Type.__name__ = "Integer32"
_HpicfDldpPortLinkStatus_Object = MibTableColumn
hpicfDldpPortLinkStatus = _HpicfDldpPortLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 1, 3, 1, 2),
    _HpicfDldpPortLinkStatus_Type()
)
hpicfDldpPortLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDldpPortLinkStatus.setStatus("current")
_HpicfDldpPortStatTable_Object = MibTable
hpicfDldpPortStatTable = _HpicfDldpPortStatTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 1, 4)
)
if mibBuilder.loadTexts:
    hpicfDldpPortStatTable.setStatus("current")
_HpicfDldpPortStatEntry_Object = MibTableRow
hpicfDldpPortStatEntry = _HpicfDldpPortStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 1, 4, 1)
)
hpicfDldpPortStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpicfDldpPortStatEntry.setStatus("current")
_HpicfDldpRxPackets_Type = Counter64
_HpicfDldpRxPackets_Object = MibTableColumn
hpicfDldpRxPackets = _HpicfDldpRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 1, 4, 1, 1),
    _HpicfDldpRxPackets_Type()
)
hpicfDldpRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDldpRxPackets.setStatus("current")
_HpicfDldpTxPackets_Type = Counter64
_HpicfDldpTxPackets_Object = MibTableColumn
hpicfDldpTxPackets = _HpicfDldpTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 1, 4, 1, 2),
    _HpicfDldpTxPackets_Type()
)
hpicfDldpTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDldpTxPackets.setStatus("current")
_HpicfDldpRxValidPackets_Type = Counter64
_HpicfDldpRxValidPackets_Object = MibTableColumn
hpicfDldpRxValidPackets = _HpicfDldpRxValidPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 1, 4, 1, 3),
    _HpicfDldpRxValidPackets_Type()
)
hpicfDldpRxValidPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDldpRxValidPackets.setStatus("current")
_HpicfDldpRxInvalidPackets_Type = Counter64
_HpicfDldpRxInvalidPackets_Object = MibTableColumn
hpicfDldpRxInvalidPackets = _HpicfDldpRxInvalidPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 1, 4, 1, 4),
    _HpicfDldpRxInvalidPackets_Type()
)
hpicfDldpRxInvalidPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDldpRxInvalidPackets.setStatus("current")
_HpicfDldpAuthFailedPackets_Type = Counter64
_HpicfDldpAuthFailedPackets_Object = MibTableColumn
hpicfDldpAuthFailedPackets = _HpicfDldpAuthFailedPackets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 1, 4, 1, 5),
    _HpicfDldpAuthFailedPackets_Type()
)
hpicfDldpAuthFailedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDldpAuthFailedPackets.setStatus("current")
_HpicfDldpStatClear_Type = TruthValue
_HpicfDldpStatClear_Object = MibTableColumn
hpicfDldpStatClear = _HpicfDldpStatClear_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 1, 4, 1, 6),
    _HpicfDldpStatClear_Type()
)
hpicfDldpStatClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDldpStatClear.setStatus("current")
_HpicfDldpNeighborTable_Object = MibTable
hpicfDldpNeighborTable = _HpicfDldpNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 1, 5)
)
if mibBuilder.loadTexts:
    hpicfDldpNeighborTable.setStatus("current")
_HpicfDldpNeighborEntry_Object = MibTableRow
hpicfDldpNeighborEntry = _HpicfDldpNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 1, 5, 1)
)
hpicfDldpNeighborEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "HP-ICF-DLDP-MIB", "hpicfDldpNeighborPortId"),
)
if mibBuilder.loadTexts:
    hpicfDldpNeighborEntry.setStatus("current")


class _HpicfDldpNeighborPortId_Type(Integer32):
    """Custom type hpicfDldpNeighborPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpicfDldpNeighborPortId_Type.__name__ = "Integer32"
_HpicfDldpNeighborPortId_Object = MibTableColumn
hpicfDldpNeighborPortId = _HpicfDldpNeighborPortId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 1, 5, 1, 1),
    _HpicfDldpNeighborPortId_Type()
)
hpicfDldpNeighborPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfDldpNeighborPortId.setStatus("current")
_HpicfDldpNeighborBridgeMac_Type = MacAddress
_HpicfDldpNeighborBridgeMac_Object = MibTableColumn
hpicfDldpNeighborBridgeMac = _HpicfDldpNeighborBridgeMac_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 1, 5, 1, 2),
    _HpicfDldpNeighborBridgeMac_Type()
)
hpicfDldpNeighborBridgeMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDldpNeighborBridgeMac.setStatus("current")
_HpicfDldpNeighborPortIndex_Type = Integer32
_HpicfDldpNeighborPortIndex_Object = MibTableColumn
hpicfDldpNeighborPortIndex = _HpicfDldpNeighborPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 1, 5, 1, 3),
    _HpicfDldpNeighborPortIndex_Type()
)
hpicfDldpNeighborPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDldpNeighborPortIndex.setStatus("current")


class _HpicfDldpNeighborStatus_Type(Integer32):
    """Custom type hpicfDldpNeighborStatus based on Integer32"""
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


_HpicfDldpNeighborStatus_Type.__name__ = "Integer32"
_HpicfDldpNeighborStatus_Object = MibTableColumn
hpicfDldpNeighborStatus = _HpicfDldpNeighborStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 1, 5, 1, 4),
    _HpicfDldpNeighborStatus_Type()
)
hpicfDldpNeighborStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDldpNeighborStatus.setStatus("current")
_HpicfDldpNeighborAgingTime_Type = Integer32
_HpicfDldpNeighborAgingTime_Object = MibTableColumn
hpicfDldpNeighborAgingTime = _HpicfDldpNeighborAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 1, 5, 1, 5),
    _HpicfDldpNeighborAgingTime_Type()
)
hpicfDldpNeighborAgingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDldpNeighborAgingTime.setStatus("current")
_HpicfDldpStatisticsObjects_ObjectIdentity = ObjectIdentity
hpicfDldpStatisticsObjects = _HpicfDldpStatisticsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 2)
)
_HpicfDldpScalarStats_ObjectIdentity = ObjectIdentity
hpicfDldpScalarStats = _HpicfDldpScalarStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 2, 1)
)
_HpicfDldpConformance_ObjectIdentity = ObjectIdentity
hpicfDldpConformance = _HpicfDldpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 3)
)
_HpicfDldpCompliances_ObjectIdentity = ObjectIdentity
hpicfDldpCompliances = _HpicfDldpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 3, 1)
)
_HpicfDldpGroups_ObjectIdentity = ObjectIdentity
hpicfDldpGroups = _HpicfDldpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 3, 2)
)

# Managed Objects groups

hpicfDldpScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 3, 2, 1)
)
hpicfDldpScalarsGroup.setObjects(
      *(("HP-ICF-DLDP-MIB", "hpicfDldpGlobalEnable"),
        ("HP-ICF-DLDP-MIB", "hpicfDldpInterval"),
        ("HP-ICF-DLDP-MIB", "hpicfDldpAuthMode"),
        ("HP-ICF-DLDP-MIB", "hpicfDldpAuthPassword"),
        ("HP-ICF-DLDP-MIB", "hpicfDldpAuthPasswordEncrypted"),
        ("HP-ICF-DLDP-MIB", "hpicfDldpUniShutdown"),
        ("HP-ICF-DLDP-MIB", "hpicfDldpDelayDownInterval"))
)
if mibBuilder.loadTexts:
    hpicfDldpScalarsGroup.setStatus("current")

hpicfDldpPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 3, 2, 2)
)
hpicfDldpPortGroup.setObjects(
      *(("HP-ICF-DLDP-MIB", "hpicfDldpPortEnable"),
        ("HP-ICF-DLDP-MIB", "hpicfDldpPortOperStatus"),
        ("HP-ICF-DLDP-MIB", "hpicfDldpPortLinkStatus"))
)
if mibBuilder.loadTexts:
    hpicfDldpPortGroup.setStatus("current")

hpicfDldpNeighborGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 3, 2, 3)
)
hpicfDldpNeighborGroup.setObjects(
      *(("HP-ICF-DLDP-MIB", "hpicfDldpNeighborBridgeMac"),
        ("HP-ICF-DLDP-MIB", "hpicfDldpNeighborPortIndex"),
        ("HP-ICF-DLDP-MIB", "hpicfDldpNeighborStatus"),
        ("HP-ICF-DLDP-MIB", "hpicfDldpNeighborAgingTime"))
)
if mibBuilder.loadTexts:
    hpicfDldpNeighborGroup.setStatus("current")

hpicfDldpStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 3, 2, 4)
)
hpicfDldpStatsGroup.setObjects(
      *(("HP-ICF-DLDP-MIB", "hpicfDldpRxPackets"),
        ("HP-ICF-DLDP-MIB", "hpicfDldpTxPackets"),
        ("HP-ICF-DLDP-MIB", "hpicfDldpRxValidPackets"),
        ("HP-ICF-DLDP-MIB", "hpicfDldpRxInvalidPackets"),
        ("HP-ICF-DLDP-MIB", "hpicfDldpAuthFailedPackets"),
        ("HP-ICF-DLDP-MIB", "hpicfDldpStatClear"))
)
if mibBuilder.loadTexts:
    hpicfDldpStatsGroup.setStatus("current")


# Notification objects

hpicfDldpTrapUniLink = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 0, 1)
)
hpicfDldpTrapUniLink.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    hpicfDldpTrapUniLink.setStatus(
        "current"
    )

hpicfDldpTrapBidLink = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 0, 2)
)
hpicfDldpTrapBidLink.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    hpicfDldpTrapBidLink.setStatus(
        "current"
    )


# Notifications groups

hpicfDldpNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 3, 2, 5)
)
hpicfDldpNotificationGroup.setObjects(
      *(("HP-ICF-DLDP-MIB", "hpicfDldpTrapUniLink"),
        ("HP-ICF-DLDP-MIB", "hpicfDldpTrapBidLink"))
)
if mibBuilder.loadTexts:
    hpicfDldpNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hpicfDldpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 108, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfDldpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-DLDP-MIB",
    **{"hpicfDldpMIB": hpicfDldpMIB,
       "hpicfDldpNotifications": hpicfDldpNotifications,
       "hpicfDldpTrapUniLink": hpicfDldpTrapUniLink,
       "hpicfDldpTrapBidLink": hpicfDldpTrapBidLink,
       "hpicfDldpConfigurationObjects": hpicfDldpConfigurationObjects,
       "hpicfDldpScalars": hpicfDldpScalars,
       "hpicfDldpGlobalEnable": hpicfDldpGlobalEnable,
       "hpicfDldpInterval": hpicfDldpInterval,
       "hpicfDldpAuthMode": hpicfDldpAuthMode,
       "hpicfDldpAuthPassword": hpicfDldpAuthPassword,
       "hpicfDldpAuthPasswordEncrypted": hpicfDldpAuthPasswordEncrypted,
       "hpicfDldpUniShutdown": hpicfDldpUniShutdown,
       "hpicfDldpDelayDownInterval": hpicfDldpDelayDownInterval,
       "hpicfDldpPortConfigTable": hpicfDldpPortConfigTable,
       "hpicfDldpPortConfigEntry": hpicfDldpPortConfigEntry,
       "hpicfDldpPortEnable": hpicfDldpPortEnable,
       "hpicfDldpPortStatusTable": hpicfDldpPortStatusTable,
       "hpicfDldpPortStatusEntry": hpicfDldpPortStatusEntry,
       "hpicfDldpPortOperStatus": hpicfDldpPortOperStatus,
       "hpicfDldpPortLinkStatus": hpicfDldpPortLinkStatus,
       "hpicfDldpPortStatTable": hpicfDldpPortStatTable,
       "hpicfDldpPortStatEntry": hpicfDldpPortStatEntry,
       "hpicfDldpRxPackets": hpicfDldpRxPackets,
       "hpicfDldpTxPackets": hpicfDldpTxPackets,
       "hpicfDldpRxValidPackets": hpicfDldpRxValidPackets,
       "hpicfDldpRxInvalidPackets": hpicfDldpRxInvalidPackets,
       "hpicfDldpAuthFailedPackets": hpicfDldpAuthFailedPackets,
       "hpicfDldpStatClear": hpicfDldpStatClear,
       "hpicfDldpNeighborTable": hpicfDldpNeighborTable,
       "hpicfDldpNeighborEntry": hpicfDldpNeighborEntry,
       "hpicfDldpNeighborPortId": hpicfDldpNeighborPortId,
       "hpicfDldpNeighborBridgeMac": hpicfDldpNeighborBridgeMac,
       "hpicfDldpNeighborPortIndex": hpicfDldpNeighborPortIndex,
       "hpicfDldpNeighborStatus": hpicfDldpNeighborStatus,
       "hpicfDldpNeighborAgingTime": hpicfDldpNeighborAgingTime,
       "hpicfDldpStatisticsObjects": hpicfDldpStatisticsObjects,
       "hpicfDldpScalarStats": hpicfDldpScalarStats,
       "hpicfDldpConformance": hpicfDldpConformance,
       "hpicfDldpCompliances": hpicfDldpCompliances,
       "hpicfDldpCompliance": hpicfDldpCompliance,
       "hpicfDldpGroups": hpicfDldpGroups,
       "hpicfDldpScalarsGroup": hpicfDldpScalarsGroup,
       "hpicfDldpPortGroup": hpicfDldpPortGroup,
       "hpicfDldpNeighborGroup": hpicfDldpNeighborGroup,
       "hpicfDldpStatsGroup": hpicfDldpStatsGroup,
       "hpicfDldpNotificationGroup": hpicfDldpNotificationGroup}
)
