# SNMP MIB module (EXTREME-ESRP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EXTREME-BASE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:41:19 2024
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

(ExtremeGenAddr,
 extremeAgent) = mibBuilder.importSymbols(
    "EXTREME-BASE-MIB",
    "ExtremeGenAddr",
    "extremeAgent")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

extremeEsrp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ExtremeEsrpTable_Object = MibTable
extremeEsrpTable = _ExtremeEsrpTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 2)
)
if mibBuilder.loadTexts:
    extremeEsrpTable.setStatus("current")
_ExtremeEsrpEntry_Object = MibTableRow
extremeEsrpEntry = _ExtremeEsrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 2, 1)
)
extremeEsrpEntry.setIndexNames(
    (0, "EXTREME-ESRP-MIB", "extremeEsrpVlanIfIndex"),
    (0, "EXTREME-ESRP-MIB", "extremeEsrpGroup"),
)
if mibBuilder.loadTexts:
    extremeEsrpEntry.setStatus("current")


class _ExtremeEsrpVlanIfIndex_Type(Integer32):
    """Custom type extremeEsrpVlanIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ExtremeEsrpVlanIfIndex_Type.__name__ = "Integer32"
_ExtremeEsrpVlanIfIndex_Object = MibTableColumn
extremeEsrpVlanIfIndex = _ExtremeEsrpVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 2, 1, 1),
    _ExtremeEsrpVlanIfIndex_Type()
)
extremeEsrpVlanIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeEsrpVlanIfIndex.setStatus("current")


class _ExtremeEsrpGroup_Type(Integer32):
    """Custom type extremeEsrpGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ExtremeEsrpGroup_Type.__name__ = "Integer32"
_ExtremeEsrpGroup_Object = MibTableColumn
extremeEsrpGroup = _ExtremeEsrpGroup_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 2, 1, 2),
    _ExtremeEsrpGroup_Type()
)
extremeEsrpGroup.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeEsrpGroup.setStatus("current")
_ExtremeEsrpRowStatus_Type = RowStatus
_ExtremeEsrpRowStatus_Object = MibTableColumn
extremeEsrpRowStatus = _ExtremeEsrpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 2, 1, 3),
    _ExtremeEsrpRowStatus_Type()
)
extremeEsrpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeEsrpRowStatus.setStatus("current")
_ExtremeEsrpNetAddress_Type = ExtremeGenAddr
_ExtremeEsrpNetAddress_Object = MibTableColumn
extremeEsrpNetAddress = _ExtremeEsrpNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 2, 1, 4),
    _ExtremeEsrpNetAddress_Type()
)
extremeEsrpNetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEsrpNetAddress.setStatus("current")


class _ExtremeEsrpState_Type(Integer32):
    """Custom type extremeEsrpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("master", 2),
          ("neutral", 1),
          ("slave", 3))
    )


_ExtremeEsrpState_Type.__name__ = "Integer32"
_ExtremeEsrpState_Object = MibTableColumn
extremeEsrpState = _ExtremeEsrpState_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 2, 1, 5),
    _ExtremeEsrpState_Type()
)
extremeEsrpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEsrpState.setStatus("current")


class _ExtremeEsrpPriority_Type(Integer32):
    """Custom type extremeEsrpPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ExtremeEsrpPriority_Type.__name__ = "Integer32"
_ExtremeEsrpPriority_Object = MibTableColumn
extremeEsrpPriority = _ExtremeEsrpPriority_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 2, 1, 6),
    _ExtremeEsrpPriority_Type()
)
extremeEsrpPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeEsrpPriority.setStatus("current")


class _ExtremeEsrpElectionAlgorithm_Type(Integer32):
    """Custom type extremeEsrpElectionAlgorithm based on Integer32"""
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
        *(("portsTrackPriorityMac", 1),
          ("priorityMacOnly", 5),
          ("priorityPortsTrackMac", 3),
          ("priorityTrackPortsMac", 4),
          ("trackPortsPriorityMac", 2))
    )


_ExtremeEsrpElectionAlgorithm_Type.__name__ = "Integer32"
_ExtremeEsrpElectionAlgorithm_Object = MibTableColumn
extremeEsrpElectionAlgorithm = _ExtremeEsrpElectionAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 2, 1, 7),
    _ExtremeEsrpElectionAlgorithm_Type()
)
extremeEsrpElectionAlgorithm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeEsrpElectionAlgorithm.setStatus("current")


class _ExtremeEsrpHelloTimer_Type(Integer32):
    """Custom type extremeEsrpHelloTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ExtremeEsrpHelloTimer_Type.__name__ = "Integer32"
_ExtremeEsrpHelloTimer_Object = MibTableColumn
extremeEsrpHelloTimer = _ExtremeEsrpHelloTimer_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 2, 1, 8),
    _ExtremeEsrpHelloTimer_Type()
)
extremeEsrpHelloTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeEsrpHelloTimer.setStatus("current")


class _ExtremeEsrpActivePorts_Type(Integer32):
    """Custom type extremeEsrpActivePorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ExtremeEsrpActivePorts_Type.__name__ = "Integer32"
_ExtremeEsrpActivePorts_Object = MibTableColumn
extremeEsrpActivePorts = _ExtremeEsrpActivePorts_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 2, 1, 9),
    _ExtremeEsrpActivePorts_Type()
)
extremeEsrpActivePorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEsrpActivePorts.setStatus("current")
_ExtremeEsrpTrackedActivePorts_Type = Integer32
_ExtremeEsrpTrackedActivePorts_Object = MibTableColumn
extremeEsrpTrackedActivePorts = _ExtremeEsrpTrackedActivePorts_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 2, 1, 10),
    _ExtremeEsrpTrackedActivePorts_Type()
)
extremeEsrpTrackedActivePorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEsrpTrackedActivePorts.setStatus("current")
_ExtremeEsrpTrackedIpRoutes_Type = Integer32
_ExtremeEsrpTrackedIpRoutes_Object = MibTableColumn
extremeEsrpTrackedIpRoutes = _ExtremeEsrpTrackedIpRoutes_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 2, 1, 11),
    _ExtremeEsrpTrackedIpRoutes_Type()
)
extremeEsrpTrackedIpRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEsrpTrackedIpRoutes.setStatus("current")
_ExtremeEsrpTrackedPings_Type = Integer32
_ExtremeEsrpTrackedPings_Object = MibTableColumn
extremeEsrpTrackedPings = _ExtremeEsrpTrackedPings_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 2, 1, 12),
    _ExtremeEsrpTrackedPings_Type()
)
extremeEsrpTrackedPings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEsrpTrackedPings.setStatus("current")
_ExtremeEsrpNumTransitionsToMaster_Type = Integer32
_ExtremeEsrpNumTransitionsToMaster_Object = MibTableColumn
extremeEsrpNumTransitionsToMaster = _ExtremeEsrpNumTransitionsToMaster_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 2, 1, 13),
    _ExtremeEsrpNumTransitionsToMaster_Type()
)
extremeEsrpNumTransitionsToMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEsrpNumTransitionsToMaster.setStatus("current")
_ExtremeEsrpNumTransitionsToSlave_Type = Integer32
_ExtremeEsrpNumTransitionsToSlave_Object = MibTableColumn
extremeEsrpNumTransitionsToSlave = _ExtremeEsrpNumTransitionsToSlave_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 2, 1, 14),
    _ExtremeEsrpNumTransitionsToSlave_Type()
)
extremeEsrpNumTransitionsToSlave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEsrpNumTransitionsToSlave.setStatus("current")


class _ExtremeEsrpInternalActivePorts_Type(Integer32):
    """Custom type extremeEsrpInternalActivePorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ExtremeEsrpInternalActivePorts_Type.__name__ = "Integer32"
_ExtremeEsrpInternalActivePorts_Object = MibTableColumn
extremeEsrpInternalActivePorts = _ExtremeEsrpInternalActivePorts_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 2, 1, 15),
    _ExtremeEsrpInternalActivePorts_Type()
)
extremeEsrpInternalActivePorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEsrpInternalActivePorts.setStatus("current")
_ExtremeEsrpNeighborTable_Object = MibTable
extremeEsrpNeighborTable = _ExtremeEsrpNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 3)
)
if mibBuilder.loadTexts:
    extremeEsrpNeighborTable.setStatus("current")
_ExtremeEsrpNeighborEntry_Object = MibTableRow
extremeEsrpNeighborEntry = _ExtremeEsrpNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 3, 1)
)
extremeEsrpNeighborEntry.setIndexNames(
    (0, "EXTREME-ESRP-MIB", "extremeEsrpVlanIfIndex"),
    (0, "EXTREME-ESRP-MIB", "extremeEsrpGroup"),
    (0, "EXTREME-ESRP-MIB", "extremeEsrpNeighborMacAddress"),
)
if mibBuilder.loadTexts:
    extremeEsrpNeighborEntry.setStatus("current")
_ExtremeEsrpNeighborMacAddress_Type = MacAddress
_ExtremeEsrpNeighborMacAddress_Object = MibTableColumn
extremeEsrpNeighborMacAddress = _ExtremeEsrpNeighborMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 3, 1, 1),
    _ExtremeEsrpNeighborMacAddress_Type()
)
extremeEsrpNeighborMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeEsrpNeighborMacAddress.setStatus("current")


class _ExtremeEsrpNeighborGroup_Type(Integer32):
    """Custom type extremeEsrpNeighborGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ExtremeEsrpNeighborGroup_Type.__name__ = "Integer32"
_ExtremeEsrpNeighborGroup_Object = MibTableColumn
extremeEsrpNeighborGroup = _ExtremeEsrpNeighborGroup_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 3, 1, 2),
    _ExtremeEsrpNeighborGroup_Type()
)
extremeEsrpNeighborGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeEsrpNeighborGroup.setStatus("current")
_ExtremeEsrpNeighborNetAddress_Type = ExtremeGenAddr
_ExtremeEsrpNeighborNetAddress_Object = MibTableColumn
extremeEsrpNeighborNetAddress = _ExtremeEsrpNeighborNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 3, 1, 3),
    _ExtremeEsrpNeighborNetAddress_Type()
)
extremeEsrpNeighborNetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEsrpNeighborNetAddress.setStatus("current")


class _ExtremeEsrpNeighborState_Type(Integer32):
    """Custom type extremeEsrpNeighborState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("master", 2),
          ("neutral", 1),
          ("slave", 3))
    )


_ExtremeEsrpNeighborState_Type.__name__ = "Integer32"
_ExtremeEsrpNeighborState_Object = MibTableColumn
extremeEsrpNeighborState = _ExtremeEsrpNeighborState_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 3, 1, 4),
    _ExtremeEsrpNeighborState_Type()
)
extremeEsrpNeighborState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEsrpNeighborState.setStatus("current")
_ExtremeEsrpNeighborPriority_Type = Integer32
_ExtremeEsrpNeighborPriority_Object = MibTableColumn
extremeEsrpNeighborPriority = _ExtremeEsrpNeighborPriority_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 3, 1, 5),
    _ExtremeEsrpNeighborPriority_Type()
)
extremeEsrpNeighborPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEsrpNeighborPriority.setStatus("current")


class _ExtremeEsrpNeighborElectionAlgorithm_Type(Integer32):
    """Custom type extremeEsrpNeighborElectionAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("portAndPriority", 1),
          ("priority", 2),
          ("priorityThenPort", 3))
    )


_ExtremeEsrpNeighborElectionAlgorithm_Type.__name__ = "Integer32"
_ExtremeEsrpNeighborElectionAlgorithm_Object = MibTableColumn
extremeEsrpNeighborElectionAlgorithm = _ExtremeEsrpNeighborElectionAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 3, 1, 6),
    _ExtremeEsrpNeighborElectionAlgorithm_Type()
)
extremeEsrpNeighborElectionAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEsrpNeighborElectionAlgorithm.setStatus("current")
_ExtremeEsrpNeighborHelloTimer_Type = Integer32
_ExtremeEsrpNeighborHelloTimer_Object = MibTableColumn
extremeEsrpNeighborHelloTimer = _ExtremeEsrpNeighborHelloTimer_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 3, 1, 7),
    _ExtremeEsrpNeighborHelloTimer_Type()
)
extremeEsrpNeighborHelloTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEsrpNeighborHelloTimer.setStatus("current")
_ExtremeEsrpNeighborActivePorts_Type = Integer32
_ExtremeEsrpNeighborActivePorts_Object = MibTableColumn
extremeEsrpNeighborActivePorts = _ExtremeEsrpNeighborActivePorts_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 3, 1, 8),
    _ExtremeEsrpNeighborActivePorts_Type()
)
extremeEsrpNeighborActivePorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEsrpNeighborActivePorts.setStatus("current")
_ExtremeEsrpNeighborTrackedActivePorts_Type = Integer32
_ExtremeEsrpNeighborTrackedActivePorts_Object = MibTableColumn
extremeEsrpNeighborTrackedActivePorts = _ExtremeEsrpNeighborTrackedActivePorts_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 3, 1, 9),
    _ExtremeEsrpNeighborTrackedActivePorts_Type()
)
extremeEsrpNeighborTrackedActivePorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEsrpNeighborTrackedActivePorts.setStatus("current")
_ExtremeEsrpNeighborTrackedIpRoutes_Type = Integer32
_ExtremeEsrpNeighborTrackedIpRoutes_Object = MibTableColumn
extremeEsrpNeighborTrackedIpRoutes = _ExtremeEsrpNeighborTrackedIpRoutes_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 3, 1, 10),
    _ExtremeEsrpNeighborTrackedIpRoutes_Type()
)
extremeEsrpNeighborTrackedIpRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEsrpNeighborTrackedIpRoutes.setStatus("current")
_ExtremeEsrpNeighborInternalActivePorts_Type = Integer32
_ExtremeEsrpNeighborInternalActivePorts_Object = MibTableColumn
extremeEsrpNeighborInternalActivePorts = _ExtremeEsrpNeighborInternalActivePorts_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 3, 1, 11),
    _ExtremeEsrpNeighborInternalActivePorts_Type()
)
extremeEsrpNeighborInternalActivePorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extremeEsrpNeighborInternalActivePorts.setStatus("current")
_ExtremeEsrpTrackVlanTable_Object = MibTable
extremeEsrpTrackVlanTable = _ExtremeEsrpTrackVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 4)
)
if mibBuilder.loadTexts:
    extremeEsrpTrackVlanTable.setStatus("current")
_ExtremeEsrpTrackVlanEntry_Object = MibTableRow
extremeEsrpTrackVlanEntry = _ExtremeEsrpTrackVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 4, 1)
)
extremeEsrpTrackVlanEntry.setIndexNames(
    (0, "EXTREME-ESRP-MIB", "extremeEsrpVlanIfIndex"),
    (0, "EXTREME-ESRP-MIB", "extremeEsrpGroup"),
    (0, "EXTREME-ESRP-MIB", "extremeEsrpTrackVlanIfIndex"),
)
if mibBuilder.loadTexts:
    extremeEsrpTrackVlanEntry.setStatus("current")


class _ExtremeEsrpTrackVlanIfIndex_Type(Integer32):
    """Custom type extremeEsrpTrackVlanIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ExtremeEsrpTrackVlanIfIndex_Type.__name__ = "Integer32"
_ExtremeEsrpTrackVlanIfIndex_Object = MibTableColumn
extremeEsrpTrackVlanIfIndex = _ExtremeEsrpTrackVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 4, 1, 1),
    _ExtremeEsrpTrackVlanIfIndex_Type()
)
extremeEsrpTrackVlanIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeEsrpTrackVlanIfIndex.setStatus("current")
_ExtremeEsrpTrackVlanRowStatus_Type = RowStatus
_ExtremeEsrpTrackVlanRowStatus_Object = MibTableColumn
extremeEsrpTrackVlanRowStatus = _ExtremeEsrpTrackVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 4, 1, 2),
    _ExtremeEsrpTrackVlanRowStatus_Type()
)
extremeEsrpTrackVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeEsrpTrackVlanRowStatus.setStatus("current")
_ExtremeEsrpTrackIpRouteTable_Object = MibTable
extremeEsrpTrackIpRouteTable = _ExtremeEsrpTrackIpRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 5)
)
if mibBuilder.loadTexts:
    extremeEsrpTrackIpRouteTable.setStatus("current")
_ExtremeEsrpTrackIpRouteEntry_Object = MibTableRow
extremeEsrpTrackIpRouteEntry = _ExtremeEsrpTrackIpRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 5, 1)
)
extremeEsrpTrackIpRouteEntry.setIndexNames(
    (0, "EXTREME-ESRP-MIB", "extremeEsrpVlanIfIndex"),
    (0, "EXTREME-ESRP-MIB", "extremeEsrpGroup"),
    (0, "EXTREME-ESRP-MIB", "extremeEsrpTrackIpRouteIpAddress"),
    (0, "EXTREME-ESRP-MIB", "extremeEsrpTrackIpRouteNetMask"),
)
if mibBuilder.loadTexts:
    extremeEsrpTrackIpRouteEntry.setStatus("current")
_ExtremeEsrpTrackIpRouteIpAddress_Type = IpAddress
_ExtremeEsrpTrackIpRouteIpAddress_Object = MibTableColumn
extremeEsrpTrackIpRouteIpAddress = _ExtremeEsrpTrackIpRouteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 5, 1, 1),
    _ExtremeEsrpTrackIpRouteIpAddress_Type()
)
extremeEsrpTrackIpRouteIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeEsrpTrackIpRouteIpAddress.setStatus("current")
_ExtremeEsrpTrackIpRouteNetMask_Type = IpAddress
_ExtremeEsrpTrackIpRouteNetMask_Object = MibTableColumn
extremeEsrpTrackIpRouteNetMask = _ExtremeEsrpTrackIpRouteNetMask_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 5, 1, 2),
    _ExtremeEsrpTrackIpRouteNetMask_Type()
)
extremeEsrpTrackIpRouteNetMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeEsrpTrackIpRouteNetMask.setStatus("current")
_ExtremeEsrpTrackIpRouteRowStatus_Type = RowStatus
_ExtremeEsrpTrackIpRouteRowStatus_Object = MibTableColumn
extremeEsrpTrackIpRouteRowStatus = _ExtremeEsrpTrackIpRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 5, 1, 3),
    _ExtremeEsrpTrackIpRouteRowStatus_Type()
)
extremeEsrpTrackIpRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    extremeEsrpTrackIpRouteRowStatus.setStatus("current")
_ExtremeEsrpPortTable_Object = MibTable
extremeEsrpPortTable = _ExtremeEsrpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 6)
)
if mibBuilder.loadTexts:
    extremeEsrpPortTable.setStatus("current")
_ExtremeEsrpPortEntry_Object = MibTableRow
extremeEsrpPortEntry = _ExtremeEsrpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 6, 1)
)
extremeEsrpPortEntry.setIndexNames(
    (0, "EXTREME-ESRP-MIB", "extremeEsrpVlanIfIndex"),
    (0, "EXTREME-ESRP-MIB", "extremeEsrpPortIfIndex"),
)
if mibBuilder.loadTexts:
    extremeEsrpPortEntry.setStatus("current")
_ExtremeEsrpPortIfIndex_Type = Integer32
_ExtremeEsrpPortIfIndex_Object = MibTableColumn
extremeEsrpPortIfIndex = _ExtremeEsrpPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 6, 1, 1),
    _ExtremeEsrpPortIfIndex_Type()
)
extremeEsrpPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extremeEsrpPortIfIndex.setStatus("current")
_ExtremeEsrpPortState_Type = TruthValue
_ExtremeEsrpPortState_Object = MibTableColumn
extremeEsrpPortState = _ExtremeEsrpPortState_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 12, 6, 1, 2),
    _ExtremeEsrpPortState_Type()
)
extremeEsrpPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    extremeEsrpPortState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXTREME-ESRP-MIB",
    **{"extremeEsrp": extremeEsrp,
       "extremeEsrpTable": extremeEsrpTable,
       "extremeEsrpEntry": extremeEsrpEntry,
       "extremeEsrpVlanIfIndex": extremeEsrpVlanIfIndex,
       "extremeEsrpGroup": extremeEsrpGroup,
       "extremeEsrpRowStatus": extremeEsrpRowStatus,
       "extremeEsrpNetAddress": extremeEsrpNetAddress,
       "extremeEsrpState": extremeEsrpState,
       "extremeEsrpPriority": extremeEsrpPriority,
       "extremeEsrpElectionAlgorithm": extremeEsrpElectionAlgorithm,
       "extremeEsrpHelloTimer": extremeEsrpHelloTimer,
       "extremeEsrpActivePorts": extremeEsrpActivePorts,
       "extremeEsrpTrackedActivePorts": extremeEsrpTrackedActivePorts,
       "extremeEsrpTrackedIpRoutes": extremeEsrpTrackedIpRoutes,
       "extremeEsrpTrackedPings": extremeEsrpTrackedPings,
       "extremeEsrpNumTransitionsToMaster": extremeEsrpNumTransitionsToMaster,
       "extremeEsrpNumTransitionsToSlave": extremeEsrpNumTransitionsToSlave,
       "extremeEsrpInternalActivePorts": extremeEsrpInternalActivePorts,
       "extremeEsrpNeighborTable": extremeEsrpNeighborTable,
       "extremeEsrpNeighborEntry": extremeEsrpNeighborEntry,
       "extremeEsrpNeighborMacAddress": extremeEsrpNeighborMacAddress,
       "extremeEsrpNeighborGroup": extremeEsrpNeighborGroup,
       "extremeEsrpNeighborNetAddress": extremeEsrpNeighborNetAddress,
       "extremeEsrpNeighborState": extremeEsrpNeighborState,
       "extremeEsrpNeighborPriority": extremeEsrpNeighborPriority,
       "extremeEsrpNeighborElectionAlgorithm": extremeEsrpNeighborElectionAlgorithm,
       "extremeEsrpNeighborHelloTimer": extremeEsrpNeighborHelloTimer,
       "extremeEsrpNeighborActivePorts": extremeEsrpNeighborActivePorts,
       "extremeEsrpNeighborTrackedActivePorts": extremeEsrpNeighborTrackedActivePorts,
       "extremeEsrpNeighborTrackedIpRoutes": extremeEsrpNeighborTrackedIpRoutes,
       "extremeEsrpNeighborInternalActivePorts": extremeEsrpNeighborInternalActivePorts,
       "extremeEsrpTrackVlanTable": extremeEsrpTrackVlanTable,
       "extremeEsrpTrackVlanEntry": extremeEsrpTrackVlanEntry,
       "extremeEsrpTrackVlanIfIndex": extremeEsrpTrackVlanIfIndex,
       "extremeEsrpTrackVlanRowStatus": extremeEsrpTrackVlanRowStatus,
       "extremeEsrpTrackIpRouteTable": extremeEsrpTrackIpRouteTable,
       "extremeEsrpTrackIpRouteEntry": extremeEsrpTrackIpRouteEntry,
       "extremeEsrpTrackIpRouteIpAddress": extremeEsrpTrackIpRouteIpAddress,
       "extremeEsrpTrackIpRouteNetMask": extremeEsrpTrackIpRouteNetMask,
       "extremeEsrpTrackIpRouteRowStatus": extremeEsrpTrackIpRouteRowStatus,
       "extremeEsrpPortTable": extremeEsrpPortTable,
       "extremeEsrpPortEntry": extremeEsrpPortEntry,
       "extremeEsrpPortIfIndex": extremeEsrpPortIfIndex,
       "extremeEsrpPortState": extremeEsrpPortState}
)
