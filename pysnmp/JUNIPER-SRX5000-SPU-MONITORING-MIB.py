# SNMP MIB module (JUNIPER-SRX5000-SPU-MONITORING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-SRX5000-SPU-MONITORING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:14:16 2024
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

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

(jnxJsSPUMonitoringRoot,) = mibBuilder.importSymbols(
    "JUNIPER-JS-SMI",
    "jnxJsSPUMonitoringRoot")

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

jnxJsSPUMonitoringMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 12, 1)
)
jnxJsSPUMonitoringMIB.setRevisions(
        ("2012-07-04 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JnxJsSPUMonitoringObjectsTable_Object = MibTable
jnxJsSPUMonitoringObjectsTable = _JnxJsSPUMonitoringObjectsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 12, 1, 1)
)
if mibBuilder.loadTexts:
    jnxJsSPUMonitoringObjectsTable.setStatus("current")
_JnxJsSPUMonitoringObjectsEntry_Object = MibTableRow
jnxJsSPUMonitoringObjectsEntry = _JnxJsSPUMonitoringObjectsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 12, 1, 1, 1)
)
jnxJsSPUMonitoringObjectsEntry.setIndexNames(
    (0, "JUNIPER-SRX5000-SPU-MONITORING-MIB", "jnxJsSPUMonitoringIndex"),
)
if mibBuilder.loadTexts:
    jnxJsSPUMonitoringObjectsEntry.setStatus("current")
_JnxJsSPUMonitoringIndex_Type = Unsigned32
_JnxJsSPUMonitoringIndex_Object = MibTableColumn
jnxJsSPUMonitoringIndex = _JnxJsSPUMonitoringIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 12, 1, 1, 1, 1),
    _JnxJsSPUMonitoringIndex_Type()
)
jnxJsSPUMonitoringIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxJsSPUMonitoringIndex.setStatus("current")
_JnxJsSPUMonitoringFPCIndex_Type = Unsigned32
_JnxJsSPUMonitoringFPCIndex_Object = MibTableColumn
jnxJsSPUMonitoringFPCIndex = _JnxJsSPUMonitoringFPCIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 12, 1, 1, 1, 2),
    _JnxJsSPUMonitoringFPCIndex_Type()
)
jnxJsSPUMonitoringFPCIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsSPUMonitoringFPCIndex.setStatus("current")
_JnxJsSPUMonitoringSPUIndex_Type = Unsigned32
_JnxJsSPUMonitoringSPUIndex_Object = MibTableColumn
jnxJsSPUMonitoringSPUIndex = _JnxJsSPUMonitoringSPUIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 12, 1, 1, 1, 3),
    _JnxJsSPUMonitoringSPUIndex_Type()
)
jnxJsSPUMonitoringSPUIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsSPUMonitoringSPUIndex.setStatus("current")
_JnxJsSPUMonitoringCPUUsage_Type = Unsigned32
_JnxJsSPUMonitoringCPUUsage_Object = MibTableColumn
jnxJsSPUMonitoringCPUUsage = _JnxJsSPUMonitoringCPUUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 12, 1, 1, 1, 4),
    _JnxJsSPUMonitoringCPUUsage_Type()
)
jnxJsSPUMonitoringCPUUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsSPUMonitoringCPUUsage.setStatus("current")
if mibBuilder.loadTexts:
    jnxJsSPUMonitoringCPUUsage.setUnits("percent")
_JnxJsSPUMonitoringMemoryUsage_Type = Unsigned32
_JnxJsSPUMonitoringMemoryUsage_Object = MibTableColumn
jnxJsSPUMonitoringMemoryUsage = _JnxJsSPUMonitoringMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 12, 1, 1, 1, 5),
    _JnxJsSPUMonitoringMemoryUsage_Type()
)
jnxJsSPUMonitoringMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsSPUMonitoringMemoryUsage.setStatus("current")
if mibBuilder.loadTexts:
    jnxJsSPUMonitoringMemoryUsage.setUnits("percent")
_JnxJsSPUMonitoringCurrentFlowSession_Type = Unsigned32
_JnxJsSPUMonitoringCurrentFlowSession_Object = MibTableColumn
jnxJsSPUMonitoringCurrentFlowSession = _JnxJsSPUMonitoringCurrentFlowSession_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 12, 1, 1, 1, 6),
    _JnxJsSPUMonitoringCurrentFlowSession_Type()
)
jnxJsSPUMonitoringCurrentFlowSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsSPUMonitoringCurrentFlowSession.setStatus("current")
_JnxJsSPUMonitoringMaxFlowSession_Type = Unsigned32
_JnxJsSPUMonitoringMaxFlowSession_Object = MibTableColumn
jnxJsSPUMonitoringMaxFlowSession = _JnxJsSPUMonitoringMaxFlowSession_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 12, 1, 1, 1, 7),
    _JnxJsSPUMonitoringMaxFlowSession_Type()
)
jnxJsSPUMonitoringMaxFlowSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsSPUMonitoringMaxFlowSession.setStatus("current")
_JnxJsSPUMonitoringCurrentCPSession_Type = Unsigned32
_JnxJsSPUMonitoringCurrentCPSession_Object = MibTableColumn
jnxJsSPUMonitoringCurrentCPSession = _JnxJsSPUMonitoringCurrentCPSession_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 12, 1, 1, 1, 8),
    _JnxJsSPUMonitoringCurrentCPSession_Type()
)
jnxJsSPUMonitoringCurrentCPSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsSPUMonitoringCurrentCPSession.setStatus("current")
_JnxJsSPUMonitoringMaxCPSession_Type = Unsigned32
_JnxJsSPUMonitoringMaxCPSession_Object = MibTableColumn
jnxJsSPUMonitoringMaxCPSession = _JnxJsSPUMonitoringMaxCPSession_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 12, 1, 1, 1, 9),
    _JnxJsSPUMonitoringMaxCPSession_Type()
)
jnxJsSPUMonitoringMaxCPSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsSPUMonitoringMaxCPSession.setStatus("current")
_JnxJsSPUMonitoringNodeIndex_Type = Unsigned32
_JnxJsSPUMonitoringNodeIndex_Object = MibTableColumn
jnxJsSPUMonitoringNodeIndex = _JnxJsSPUMonitoringNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 12, 1, 1, 1, 10),
    _JnxJsSPUMonitoringNodeIndex_Type()
)
jnxJsSPUMonitoringNodeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsSPUMonitoringNodeIndex.setStatus("current")


class _JnxJsSPUMonitoringNodeDescr_Type(DisplayString):
    """Custom type jnxJsSPUMonitoringNodeDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_JnxJsSPUMonitoringNodeDescr_Type.__name__ = "DisplayString"
_JnxJsSPUMonitoringNodeDescr_Object = MibTableColumn
jnxJsSPUMonitoringNodeDescr = _JnxJsSPUMonitoringNodeDescr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 12, 1, 1, 1, 11),
    _JnxJsSPUMonitoringNodeDescr_Type()
)
jnxJsSPUMonitoringNodeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsSPUMonitoringNodeDescr.setStatus("current")
_JnxJsSPUMonitoringFlowSessIPv4_Type = Unsigned32
_JnxJsSPUMonitoringFlowSessIPv4_Object = MibTableColumn
jnxJsSPUMonitoringFlowSessIPv4 = _JnxJsSPUMonitoringFlowSessIPv4_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 12, 1, 1, 1, 12),
    _JnxJsSPUMonitoringFlowSessIPv4_Type()
)
jnxJsSPUMonitoringFlowSessIPv4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsSPUMonitoringFlowSessIPv4.setStatus("current")
_JnxJsSPUMonitoringFlowSessIPv6_Type = Unsigned32
_JnxJsSPUMonitoringFlowSessIPv6_Object = MibTableColumn
jnxJsSPUMonitoringFlowSessIPv6 = _JnxJsSPUMonitoringFlowSessIPv6_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 12, 1, 1, 1, 13),
    _JnxJsSPUMonitoringFlowSessIPv6_Type()
)
jnxJsSPUMonitoringFlowSessIPv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsSPUMonitoringFlowSessIPv6.setStatus("current")
_JnxJsSPUMonitoringCPSessIPv4_Type = Unsigned32
_JnxJsSPUMonitoringCPSessIPv4_Object = MibTableColumn
jnxJsSPUMonitoringCPSessIPv4 = _JnxJsSPUMonitoringCPSessIPv4_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 12, 1, 1, 1, 14),
    _JnxJsSPUMonitoringCPSessIPv4_Type()
)
jnxJsSPUMonitoringCPSessIPv4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsSPUMonitoringCPSessIPv4.setStatus("current")
_JnxJsSPUMonitoringCPSessIPv6_Type = Unsigned32
_JnxJsSPUMonitoringCPSessIPv6_Object = MibTableColumn
jnxJsSPUMonitoringCPSessIPv6 = _JnxJsSPUMonitoringCPSessIPv6_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 12, 1, 1, 1, 15),
    _JnxJsSPUMonitoringCPSessIPv6_Type()
)
jnxJsSPUMonitoringCPSessIPv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsSPUMonitoringCPSessIPv6.setStatus("current")
_JnxJsSPUMonitoringCurrentTotalSession_Type = Unsigned32
_JnxJsSPUMonitoringCurrentTotalSession_Object = MibScalar
jnxJsSPUMonitoringCurrentTotalSession = _JnxJsSPUMonitoringCurrentTotalSession_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 12, 1, 2),
    _JnxJsSPUMonitoringCurrentTotalSession_Type()
)
jnxJsSPUMonitoringCurrentTotalSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsSPUMonitoringCurrentTotalSession.setStatus("current")
_JnxJsSPUMonitoringMaxTotalSession_Type = Unsigned32
_JnxJsSPUMonitoringMaxTotalSession_Object = MibScalar
jnxJsSPUMonitoringMaxTotalSession = _JnxJsSPUMonitoringMaxTotalSession_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 12, 1, 3),
    _JnxJsSPUMonitoringMaxTotalSession_Type()
)
jnxJsSPUMonitoringMaxTotalSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsSPUMonitoringMaxTotalSession.setStatus("current")
_JnxSPUClusterObjectsTable_Object = MibTable
jnxSPUClusterObjectsTable = _JnxSPUClusterObjectsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 12, 1, 4)
)
if mibBuilder.loadTexts:
    jnxSPUClusterObjectsTable.setStatus("current")
_JnxSPUClusterObjectsEntry_Object = MibTableRow
jnxSPUClusterObjectsEntry = _JnxSPUClusterObjectsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 12, 1, 4, 1)
)
jnxSPUClusterObjectsEntry.setIndexNames(
    (0, "JUNIPER-SRX5000-SPU-MONITORING-MIB", "jnxJsClusterMonitoringNodeIndex"),
)
if mibBuilder.loadTexts:
    jnxSPUClusterObjectsEntry.setStatus("current")
_JnxJsClusterMonitoringNodeIndex_Type = Unsigned32
_JnxJsClusterMonitoringNodeIndex_Object = MibTableColumn
jnxJsClusterMonitoringNodeIndex = _JnxJsClusterMonitoringNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 12, 1, 4, 1, 1),
    _JnxJsClusterMonitoringNodeIndex_Type()
)
jnxJsClusterMonitoringNodeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxJsClusterMonitoringNodeIndex.setStatus("current")


class _JnxJsClusterMonitoringNodeDescr_Type(DisplayString):
    """Custom type jnxJsClusterMonitoringNodeDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_JnxJsClusterMonitoringNodeDescr_Type.__name__ = "DisplayString"
_JnxJsClusterMonitoringNodeDescr_Object = MibTableColumn
jnxJsClusterMonitoringNodeDescr = _JnxJsClusterMonitoringNodeDescr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 12, 1, 4, 1, 2),
    _JnxJsClusterMonitoringNodeDescr_Type()
)
jnxJsClusterMonitoringNodeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsClusterMonitoringNodeDescr.setStatus("current")
_JnxJsNodeCurrentTotalSession_Type = Unsigned32
_JnxJsNodeCurrentTotalSession_Object = MibTableColumn
jnxJsNodeCurrentTotalSession = _JnxJsNodeCurrentTotalSession_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 12, 1, 4, 1, 3),
    _JnxJsNodeCurrentTotalSession_Type()
)
jnxJsNodeCurrentTotalSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsNodeCurrentTotalSession.setStatus("current")
_JnxJsNodeMaxTotalSession_Type = Unsigned32
_JnxJsNodeMaxTotalSession_Object = MibTableColumn
jnxJsNodeMaxTotalSession = _JnxJsNodeMaxTotalSession_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 12, 1, 4, 1, 4),
    _JnxJsNodeMaxTotalSession_Type()
)
jnxJsNodeMaxTotalSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsNodeMaxTotalSession.setStatus("current")
_JnxJsNodeSessionCreationPerSecond_Type = CounterBasedGauge64
_JnxJsNodeSessionCreationPerSecond_Object = MibTableColumn
jnxJsNodeSessionCreationPerSecond = _JnxJsNodeSessionCreationPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 12, 1, 4, 1, 5),
    _JnxJsNodeSessionCreationPerSecond_Type()
)
jnxJsNodeSessionCreationPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsNodeSessionCreationPerSecond.setStatus("current")
_JnxJsNodeSessCreationPerSecIPv4_Type = CounterBasedGauge64
_JnxJsNodeSessCreationPerSecIPv4_Object = MibTableColumn
jnxJsNodeSessCreationPerSecIPv4 = _JnxJsNodeSessCreationPerSecIPv4_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 12, 1, 4, 1, 6),
    _JnxJsNodeSessCreationPerSecIPv4_Type()
)
jnxJsNodeSessCreationPerSecIPv4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsNodeSessCreationPerSecIPv4.setStatus("current")
_JnxJsNodeSessCreationPerSecIPv6_Type = CounterBasedGauge64
_JnxJsNodeSessCreationPerSecIPv6_Object = MibTableColumn
jnxJsNodeSessCreationPerSecIPv6 = _JnxJsNodeSessCreationPerSecIPv6_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 12, 1, 4, 1, 7),
    _JnxJsNodeSessCreationPerSecIPv6_Type()
)
jnxJsNodeSessCreationPerSecIPv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsNodeSessCreationPerSecIPv6.setStatus("current")
_JnxJsNodeCurrentTotalSessIPv4_Type = Unsigned32
_JnxJsNodeCurrentTotalSessIPv4_Object = MibTableColumn
jnxJsNodeCurrentTotalSessIPv4 = _JnxJsNodeCurrentTotalSessIPv4_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 12, 1, 4, 1, 8),
    _JnxJsNodeCurrentTotalSessIPv4_Type()
)
jnxJsNodeCurrentTotalSessIPv4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsNodeCurrentTotalSessIPv4.setStatus("current")
_JnxJsNodeCurrentTotalSessIPv6_Type = Unsigned32
_JnxJsNodeCurrentTotalSessIPv6_Object = MibTableColumn
jnxJsNodeCurrentTotalSessIPv6 = _JnxJsNodeCurrentTotalSessIPv6_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 12, 1, 4, 1, 9),
    _JnxJsNodeCurrentTotalSessIPv6_Type()
)
jnxJsNodeCurrentTotalSessIPv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsNodeCurrentTotalSessIPv6.setStatus("current")
_JnxJsSPUMonitoringTotalSessIPv4_Type = Unsigned32
_JnxJsSPUMonitoringTotalSessIPv4_Object = MibScalar
jnxJsSPUMonitoringTotalSessIPv4 = _JnxJsSPUMonitoringTotalSessIPv4_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 12, 1, 5),
    _JnxJsSPUMonitoringTotalSessIPv4_Type()
)
jnxJsSPUMonitoringTotalSessIPv4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsSPUMonitoringTotalSessIPv4.setStatus("current")
_JnxJsSPUMonitoringTotalSessIPv6_Type = Unsigned32
_JnxJsSPUMonitoringTotalSessIPv6_Object = MibScalar
jnxJsSPUMonitoringTotalSessIPv6 = _JnxJsSPUMonitoringTotalSessIPv6_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 39, 1, 12, 1, 6),
    _JnxJsSPUMonitoringTotalSessIPv6_Type()
)
jnxJsSPUMonitoringTotalSessIPv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxJsSPUMonitoringTotalSessIPv6.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-SRX5000-SPU-MONITORING-MIB",
    **{"jnxJsSPUMonitoringMIB": jnxJsSPUMonitoringMIB,
       "jnxJsSPUMonitoringObjectsTable": jnxJsSPUMonitoringObjectsTable,
       "jnxJsSPUMonitoringObjectsEntry": jnxJsSPUMonitoringObjectsEntry,
       "jnxJsSPUMonitoringIndex": jnxJsSPUMonitoringIndex,
       "jnxJsSPUMonitoringFPCIndex": jnxJsSPUMonitoringFPCIndex,
       "jnxJsSPUMonitoringSPUIndex": jnxJsSPUMonitoringSPUIndex,
       "jnxJsSPUMonitoringCPUUsage": jnxJsSPUMonitoringCPUUsage,
       "jnxJsSPUMonitoringMemoryUsage": jnxJsSPUMonitoringMemoryUsage,
       "jnxJsSPUMonitoringCurrentFlowSession": jnxJsSPUMonitoringCurrentFlowSession,
       "jnxJsSPUMonitoringMaxFlowSession": jnxJsSPUMonitoringMaxFlowSession,
       "jnxJsSPUMonitoringCurrentCPSession": jnxJsSPUMonitoringCurrentCPSession,
       "jnxJsSPUMonitoringMaxCPSession": jnxJsSPUMonitoringMaxCPSession,
       "jnxJsSPUMonitoringNodeIndex": jnxJsSPUMonitoringNodeIndex,
       "jnxJsSPUMonitoringNodeDescr": jnxJsSPUMonitoringNodeDescr,
       "jnxJsSPUMonitoringFlowSessIPv4": jnxJsSPUMonitoringFlowSessIPv4,
       "jnxJsSPUMonitoringFlowSessIPv6": jnxJsSPUMonitoringFlowSessIPv6,
       "jnxJsSPUMonitoringCPSessIPv4": jnxJsSPUMonitoringCPSessIPv4,
       "jnxJsSPUMonitoringCPSessIPv6": jnxJsSPUMonitoringCPSessIPv6,
       "jnxJsSPUMonitoringCurrentTotalSession": jnxJsSPUMonitoringCurrentTotalSession,
       "jnxJsSPUMonitoringMaxTotalSession": jnxJsSPUMonitoringMaxTotalSession,
       "jnxSPUClusterObjectsTable": jnxSPUClusterObjectsTable,
       "jnxSPUClusterObjectsEntry": jnxSPUClusterObjectsEntry,
       "jnxJsClusterMonitoringNodeIndex": jnxJsClusterMonitoringNodeIndex,
       "jnxJsClusterMonitoringNodeDescr": jnxJsClusterMonitoringNodeDescr,
       "jnxJsNodeCurrentTotalSession": jnxJsNodeCurrentTotalSession,
       "jnxJsNodeMaxTotalSession": jnxJsNodeMaxTotalSession,
       "jnxJsNodeSessionCreationPerSecond": jnxJsNodeSessionCreationPerSecond,
       "jnxJsNodeSessCreationPerSecIPv4": jnxJsNodeSessCreationPerSecIPv4,
       "jnxJsNodeSessCreationPerSecIPv6": jnxJsNodeSessCreationPerSecIPv6,
       "jnxJsNodeCurrentTotalSessIPv4": jnxJsNodeCurrentTotalSessIPv4,
       "jnxJsNodeCurrentTotalSessIPv6": jnxJsNodeCurrentTotalSessIPv6,
       "jnxJsSPUMonitoringTotalSessIPv4": jnxJsSPUMonitoringTotalSessIPv4,
       "jnxJsSPUMonitoringTotalSessIPv6": jnxJsSPUMonitoringTotalSessIPv6}
)
