# SNMP MIB module (OA-ZBFW-STATUS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OA-ZBFW-STATUS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:33:32 2024
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

(oacExpIMZbFw,
 oacMIBModules) = mibBuilder.importSymbols(
    "ONEACCESS-GLOBAL-REG",
    "oacExpIMZbFw",
    "oacMIBModules")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

oacZbfwStatusMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 1, 100, 2003)
)


# Types definitions



class TableIndex(Unsigned32):
    """Custom type TableIndex based on Unsigned32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OacZbfw_ObjectIdentity = ObjectIdentity
oacZbfw = _OacZbfw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131)
)
_OacZbfwPerf_ObjectIdentity = ObjectIdentity
oacZbfwPerf = _OacZbfwPerf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12)
)
_OacZbfwRtrConnPerf_ObjectIdentity = ObjectIdentity
oacZbfwRtrConnPerf = _OacZbfwRtrConnPerf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12, 40)
)
_OacZbfwRtrConnPerfSSCTable_Object = MibTable
oacZbfwRtrConnPerfSSCTable = _OacZbfwRtrConnPerfSSCTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12, 40, 1)
)
if mibBuilder.loadTexts:
    oacZbfwRtrConnPerfSSCTable.setStatus("current")
_OacZbfwRtrConnPerfEntry_Object = MibTableRow
oacZbfwRtrConnPerfEntry = _OacZbfwRtrConnPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12, 40, 1, 1)
)
oacZbfwRtrConnPerfEntry.setIndexNames(
    (1, "OA-ZBFW-STATUS-MIB", "oacZbfwRtrConnPerfGlobalIx"),
)
if mibBuilder.loadTexts:
    oacZbfwRtrConnPerfEntry.setStatus("current")
_OacZbfwRouterConnectionsCreated_Type = Counter32
_OacZbfwRouterConnectionsCreated_Object = MibTableColumn
oacZbfwRouterConnectionsCreated = _OacZbfwRouterConnectionsCreated_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12, 40, 1, 1, 1),
    _OacZbfwRouterConnectionsCreated_Type()
)
oacZbfwRouterConnectionsCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacZbfwRouterConnectionsCreated.setStatus("current")
_OacZbfwRouterConnectionsClosed_Type = Counter32
_OacZbfwRouterConnectionsClosed_Object = MibTableColumn
oacZbfwRouterConnectionsClosed = _OacZbfwRouterConnectionsClosed_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12, 40, 1, 1, 2),
    _OacZbfwRouterConnectionsClosed_Type()
)
oacZbfwRouterConnectionsClosed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacZbfwRouterConnectionsClosed.setStatus("current")
_OacZbfwRouterConnectionsTimedOut_Type = Counter32
_OacZbfwRouterConnectionsTimedOut_Object = MibTableColumn
oacZbfwRouterConnectionsTimedOut = _OacZbfwRouterConnectionsTimedOut_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12, 40, 1, 1, 3),
    _OacZbfwRouterConnectionsTimedOut_Type()
)
oacZbfwRouterConnectionsTimedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacZbfwRouterConnectionsTimedOut.setStatus("current")
_OacZbfwRouterConnectionsMax_Type = Counter32
_OacZbfwRouterConnectionsMax_Object = MibTableColumn
oacZbfwRouterConnectionsMax = _OacZbfwRouterConnectionsMax_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12, 40, 1, 1, 4),
    _OacZbfwRouterConnectionsMax_Type()
)
oacZbfwRouterConnectionsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacZbfwRouterConnectionsMax.setStatus("current")
_OacZbfwRouterConnectionsMaxUsed_Type = Counter32
_OacZbfwRouterConnectionsMaxUsed_Object = MibTableColumn
oacZbfwRouterConnectionsMaxUsed = _OacZbfwRouterConnectionsMaxUsed_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12, 40, 1, 1, 5),
    _OacZbfwRouterConnectionsMaxUsed_Type()
)
oacZbfwRouterConnectionsMaxUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacZbfwRouterConnectionsMaxUsed.setStatus("current")
_OacZbfwRouterConnectionsUsed_Type = Counter32
_OacZbfwRouterConnectionsUsed_Object = MibTableColumn
oacZbfwRouterConnectionsUsed = _OacZbfwRouterConnectionsUsed_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12, 40, 1, 1, 6),
    _OacZbfwRouterConnectionsUsed_Type()
)
oacZbfwRouterConnectionsUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacZbfwRouterConnectionsUsed.setStatus("current")
_OacZbfwRtrConnPerfGlobalIx_Type = SnmpAdminString
_OacZbfwRtrConnPerfGlobalIx_Object = MibTableColumn
oacZbfwRtrConnPerfGlobalIx = _OacZbfwRtrConnPerfGlobalIx_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12, 40, 1, 1, 10),
    _OacZbfwRtrConnPerfGlobalIx_Type()
)
oacZbfwRtrConnPerfGlobalIx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oacZbfwRtrConnPerfGlobalIx.setStatus("current")
_OacZbfwPackets_ObjectIdentity = ObjectIdentity
oacZbfwPackets = _OacZbfwPackets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12, 41)
)
_OacZbfwPacketsSSCTable_Object = MibTable
oacZbfwPacketsSSCTable = _OacZbfwPacketsSSCTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12, 41, 1)
)
if mibBuilder.loadTexts:
    oacZbfwPacketsSSCTable.setStatus("current")
_OacZbfwPacketsEntry_Object = MibTableRow
oacZbfwPacketsEntry = _OacZbfwPacketsEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12, 41, 1, 1)
)
oacZbfwPacketsEntry.setIndexNames(
    (1, "OA-ZBFW-STATUS-MIB", "oacZbfwPacketsGlobalIx"),
)
if mibBuilder.loadTexts:
    oacZbfwPacketsEntry.setStatus("current")
_OacZbfwPacketsGlobalIx_Type = SnmpAdminString
_OacZbfwPacketsGlobalIx_Object = MibTableColumn
oacZbfwPacketsGlobalIx = _OacZbfwPacketsGlobalIx_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12, 41, 1, 1, 1),
    _OacZbfwPacketsGlobalIx_Type()
)
oacZbfwPacketsGlobalIx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oacZbfwPacketsGlobalIx.setStatus("current")
_OacZbfwPacketsProcessed_Type = Counter32
_OacZbfwPacketsProcessed_Object = MibTableColumn
oacZbfwPacketsProcessed = _OacZbfwPacketsProcessed_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12, 41, 1, 1, 2),
    _OacZbfwPacketsProcessed_Type()
)
oacZbfwPacketsProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacZbfwPacketsProcessed.setStatus("current")
_OacZbfwPacketsPassed_Type = Counter32
_OacZbfwPacketsPassed_Object = MibTableColumn
oacZbfwPacketsPassed = _OacZbfwPacketsPassed_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12, 41, 1, 1, 3),
    _OacZbfwPacketsPassed_Type()
)
oacZbfwPacketsPassed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacZbfwPacketsPassed.setStatus("current")
_OacZbfwPacketsDropped_Type = Counter32
_OacZbfwPacketsDropped_Object = MibTableColumn
oacZbfwPacketsDropped = _OacZbfwPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12, 41, 1, 1, 4),
    _OacZbfwPacketsDropped_Type()
)
oacZbfwPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacZbfwPacketsDropped.setStatus("current")
_OacZbfwPacketsRejected_Type = Counter32
_OacZbfwPacketsRejected_Object = MibTableColumn
oacZbfwPacketsRejected = _OacZbfwPacketsRejected_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12, 41, 1, 1, 5),
    _OacZbfwPacketsRejected_Type()
)
oacZbfwPacketsRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacZbfwPacketsRejected.setStatus("current")
_OacZbfwPacketsRejectStatsInvalidIntf_Type = Counter32
_OacZbfwPacketsRejectStatsInvalidIntf_Object = MibTableColumn
oacZbfwPacketsRejectStatsInvalidIntf = _OacZbfwPacketsRejectStatsInvalidIntf_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12, 41, 1, 1, 6),
    _OacZbfwPacketsRejectStatsInvalidIntf_Type()
)
oacZbfwPacketsRejectStatsInvalidIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacZbfwPacketsRejectStatsInvalidIntf.setStatus("current")
_OacZbfwPacketsRejectStatsNoPolicy_Type = Counter32
_OacZbfwPacketsRejectStatsNoPolicy_Object = MibTableColumn
oacZbfwPacketsRejectStatsNoPolicy = _OacZbfwPacketsRejectStatsNoPolicy_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12, 41, 1, 1, 7),
    _OacZbfwPacketsRejectStatsNoPolicy_Type()
)
oacZbfwPacketsRejectStatsNoPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacZbfwPacketsRejectStatsNoPolicy.setStatus("current")
_OacZbfwPacketsRejectStatsNoConnSetup_Type = Counter32
_OacZbfwPacketsRejectStatsNoConnSetup_Object = MibTableColumn
oacZbfwPacketsRejectStatsNoConnSetup = _OacZbfwPacketsRejectStatsNoConnSetup_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12, 41, 1, 1, 8),
    _OacZbfwPacketsRejectStatsNoConnSetup_Type()
)
oacZbfwPacketsRejectStatsNoConnSetup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacZbfwPacketsRejectStatsNoConnSetup.setStatus("current")
_OacZbfwPacketsRejectStatsProtocol_Type = Counter32
_OacZbfwPacketsRejectStatsProtocol_Object = MibTableColumn
oacZbfwPacketsRejectStatsProtocol = _OacZbfwPacketsRejectStatsProtocol_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12, 41, 1, 1, 9),
    _OacZbfwPacketsRejectStatsProtocol_Type()
)
oacZbfwPacketsRejectStatsProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacZbfwPacketsRejectStatsProtocol.setStatus("current")
_OacZbfwPacketsRejectStatsAlg_Type = Counter32
_OacZbfwPacketsRejectStatsAlg_Object = MibTableColumn
oacZbfwPacketsRejectStatsAlg = _OacZbfwPacketsRejectStatsAlg_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12, 41, 1, 1, 10),
    _OacZbfwPacketsRejectStatsAlg_Type()
)
oacZbfwPacketsRejectStatsAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacZbfwPacketsRejectStatsAlg.setStatus("current")
_OacZbfwPacketsRejectStatsConnExceeded_Type = Counter32
_OacZbfwPacketsRejectStatsConnExceeded_Object = MibTableColumn
oacZbfwPacketsRejectStatsConnExceeded = _OacZbfwPacketsRejectStatsConnExceeded_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12, 41, 1, 1, 11),
    _OacZbfwPacketsRejectStatsConnExceeded_Type()
)
oacZbfwPacketsRejectStatsConnExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacZbfwPacketsRejectStatsConnExceeded.setStatus("current")
_OacZbfwPolicyRules_ObjectIdentity = ObjectIdentity
oacZbfwPolicyRules = _OacZbfwPolicyRules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12, 42)
)
_OacZbfwPolicyRulesSSCTable_Object = MibTable
oacZbfwPolicyRulesSSCTable = _OacZbfwPolicyRulesSSCTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12, 42, 1)
)
if mibBuilder.loadTexts:
    oacZbfwPolicyRulesSSCTable.setStatus("current")
_OacZbfwPolicyRulesEntry_Object = MibTableRow
oacZbfwPolicyRulesEntry = _OacZbfwPolicyRulesEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12, 42, 1, 1)
)
oacZbfwPolicyRulesEntry.setIndexNames(
    (0, "OA-ZBFW-STATUS-MIB", "oacZbfwPolicyRulesTableIx"),
    (1, "OA-ZBFW-STATUS-MIB", "oacZbfwPolicyRulesGlobalIx"),
)
if mibBuilder.loadTexts:
    oacZbfwPolicyRulesEntry.setStatus("current")
_OacZbfwPolicyRulesTableIx_Type = TableIndex
_OacZbfwPolicyRulesTableIx_Object = MibTableColumn
oacZbfwPolicyRulesTableIx = _OacZbfwPolicyRulesTableIx_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12, 42, 1, 1, 1),
    _OacZbfwPolicyRulesTableIx_Type()
)
oacZbfwPolicyRulesTableIx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oacZbfwPolicyRulesTableIx.setStatus("current")
_OacZbfwPolicyRulesGlobalIx_Type = SnmpAdminString
_OacZbfwPolicyRulesGlobalIx_Object = MibTableColumn
oacZbfwPolicyRulesGlobalIx = _OacZbfwPolicyRulesGlobalIx_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12, 42, 1, 1, 2),
    _OacZbfwPolicyRulesGlobalIx_Type()
)
oacZbfwPolicyRulesGlobalIx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oacZbfwPolicyRulesGlobalIx.setStatus("current")
_OacZbfwPolicyRulesZonePair_Type = DisplayString
_OacZbfwPolicyRulesZonePair_Object = MibTableColumn
oacZbfwPolicyRulesZonePair = _OacZbfwPolicyRulesZonePair_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12, 42, 1, 1, 3),
    _OacZbfwPolicyRulesZonePair_Type()
)
oacZbfwPolicyRulesZonePair.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacZbfwPolicyRulesZonePair.setStatus("current")
_OacZbfwPolicyRulesPolicy_Type = DisplayString
_OacZbfwPolicyRulesPolicy_Object = MibTableColumn
oacZbfwPolicyRulesPolicy = _OacZbfwPolicyRulesPolicy_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12, 42, 1, 1, 4),
    _OacZbfwPolicyRulesPolicy_Type()
)
oacZbfwPolicyRulesPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacZbfwPolicyRulesPolicy.setStatus("current")
_OacZbfwPolicyRulesPolicyRule_Type = DisplayString
_OacZbfwPolicyRulesPolicyRule_Object = MibTableColumn
oacZbfwPolicyRulesPolicyRule = _OacZbfwPolicyRulesPolicyRule_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12, 42, 1, 1, 5),
    _OacZbfwPolicyRulesPolicyRule_Type()
)
oacZbfwPolicyRulesPolicyRule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacZbfwPolicyRulesPolicyRule.setStatus("current")
_OacZbfwPolicyRulesCountersProcessed_Type = Counter32
_OacZbfwPolicyRulesCountersProcessed_Object = MibTableColumn
oacZbfwPolicyRulesCountersProcessed = _OacZbfwPolicyRulesCountersProcessed_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12, 42, 1, 1, 6),
    _OacZbfwPolicyRulesCountersProcessed_Type()
)
oacZbfwPolicyRulesCountersProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacZbfwPolicyRulesCountersProcessed.setStatus("current")
_OacZbfwPolicyRulesCountersApplied_Type = Counter32
_OacZbfwPolicyRulesCountersApplied_Object = MibTableColumn
oacZbfwPolicyRulesCountersApplied = _OacZbfwPolicyRulesCountersApplied_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12, 42, 1, 1, 7),
    _OacZbfwPolicyRulesCountersApplied_Type()
)
oacZbfwPolicyRulesCountersApplied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacZbfwPolicyRulesCountersApplied.setStatus("current")
_OacZbfwPolicyRulesCountersConnections_Type = Counter32
_OacZbfwPolicyRulesCountersConnections_Object = MibTableColumn
oacZbfwPolicyRulesCountersConnections = _OacZbfwPolicyRulesCountersConnections_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12, 42, 1, 1, 8),
    _OacZbfwPolicyRulesCountersConnections_Type()
)
oacZbfwPolicyRulesCountersConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacZbfwPolicyRulesCountersConnections.setStatus("current")
_OacZbfwPolicyRulesCountersPackets_Type = Counter32
_OacZbfwPolicyRulesCountersPackets_Object = MibTableColumn
oacZbfwPolicyRulesCountersPackets = _OacZbfwPolicyRulesCountersPackets_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12, 42, 1, 1, 9),
    _OacZbfwPolicyRulesCountersPackets_Type()
)
oacZbfwPolicyRulesCountersPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacZbfwPolicyRulesCountersPackets.setStatus("current")
_OacZbfwPolicyRulesCountersOctets_Type = Counter32
_OacZbfwPolicyRulesCountersOctets_Object = MibTableColumn
oacZbfwPolicyRulesCountersOctets = _OacZbfwPolicyRulesCountersOctets_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12, 42, 1, 1, 10),
    _OacZbfwPolicyRulesCountersOctets_Type()
)
oacZbfwPolicyRulesCountersOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacZbfwPolicyRulesCountersOctets.setStatus("current")
_OacZbfwPolicyRulesCountersReversePackets_Type = Counter32
_OacZbfwPolicyRulesCountersReversePackets_Object = MibTableColumn
oacZbfwPolicyRulesCountersReversePackets = _OacZbfwPolicyRulesCountersReversePackets_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12, 42, 1, 1, 11),
    _OacZbfwPolicyRulesCountersReversePackets_Type()
)
oacZbfwPolicyRulesCountersReversePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacZbfwPolicyRulesCountersReversePackets.setStatus("current")
_OacZbfwPolicyRulesCountersReverseOctets_Type = Counter32
_OacZbfwPolicyRulesCountersReverseOctets_Object = MibTableColumn
oacZbfwPolicyRulesCountersReverseOctets = _OacZbfwPolicyRulesCountersReverseOctets_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12, 42, 1, 1, 12),
    _OacZbfwPolicyRulesCountersReverseOctets_Type()
)
oacZbfwPolicyRulesCountersReverseOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacZbfwPolicyRulesCountersReverseOctets.setStatus("current")
_OacZbfwClearCounters_Type = Integer32
_OacZbfwClearCounters_Object = MibScalar
oacZbfwClearCounters = _OacZbfwClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 12, 43),
    _OacZbfwClearCounters_Type()
)
oacZbfwClearCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oacZbfwClearCounters.setStatus("current")
_OacZbfwStatus_ObjectIdentity = ObjectIdentity
oacZbfwStatus = _OacZbfwStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 14)
)
_OacZbfwZonePairs_ObjectIdentity = ObjectIdentity
oacZbfwZonePairs = _OacZbfwZonePairs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 14, 22)
)
_OacZbfwZonePairsSSCTable_Object = MibTable
oacZbfwZonePairsSSCTable = _OacZbfwZonePairsSSCTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 14, 22, 1)
)
if mibBuilder.loadTexts:
    oacZbfwZonePairsSSCTable.setStatus("current")
_OacZbfwZonePairsEntry_Object = MibTableRow
oacZbfwZonePairsEntry = _OacZbfwZonePairsEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 14, 22, 1, 1)
)
oacZbfwZonePairsEntry.setIndexNames(
    (0, "OA-ZBFW-STATUS-MIB", "oacZbfwZonePairsTableIx"),
    (1, "OA-ZBFW-STATUS-MIB", "oacZbfwZonePairsGlobalIx"),
)
if mibBuilder.loadTexts:
    oacZbfwZonePairsEntry.setStatus("current")
_OacZbfwZonePairsTableIx_Type = TableIndex
_OacZbfwZonePairsTableIx_Object = MibTableColumn
oacZbfwZonePairsTableIx = _OacZbfwZonePairsTableIx_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 14, 22, 1, 1, 1),
    _OacZbfwZonePairsTableIx_Type()
)
oacZbfwZonePairsTableIx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oacZbfwZonePairsTableIx.setStatus("current")
_OacZbfwZonePairsGlobalIx_Type = SnmpAdminString
_OacZbfwZonePairsGlobalIx_Object = MibTableColumn
oacZbfwZonePairsGlobalIx = _OacZbfwZonePairsGlobalIx_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 14, 22, 1, 1, 2),
    _OacZbfwZonePairsGlobalIx_Type()
)
oacZbfwZonePairsGlobalIx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oacZbfwZonePairsGlobalIx.setStatus("current")
_OacZbfwZonePairsName_Type = DisplayString
_OacZbfwZonePairsName_Object = MibTableColumn
oacZbfwZonePairsName = _OacZbfwZonePairsName_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 14, 22, 1, 1, 3),
    _OacZbfwZonePairsName_Type()
)
oacZbfwZonePairsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacZbfwZonePairsName.setStatus("current")
_OacZbfwZonePairsSrcZone_Type = DisplayString
_OacZbfwZonePairsSrcZone_Object = MibTableColumn
oacZbfwZonePairsSrcZone = _OacZbfwZonePairsSrcZone_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 14, 22, 1, 1, 4),
    _OacZbfwZonePairsSrcZone_Type()
)
oacZbfwZonePairsSrcZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacZbfwZonePairsSrcZone.setStatus("current")
_OacZbfwZonePairsDstZone_Type = DisplayString
_OacZbfwZonePairsDstZone_Object = MibTableColumn
oacZbfwZonePairsDstZone = _OacZbfwZonePairsDstZone_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 14, 22, 1, 1, 5),
    _OacZbfwZonePairsDstZone_Type()
)
oacZbfwZonePairsDstZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacZbfwZonePairsDstZone.setStatus("current")
_OacZbfwZonePairsPolicy_Type = DisplayString
_OacZbfwZonePairsPolicy_Object = MibTableColumn
oacZbfwZonePairsPolicy = _OacZbfwZonePairsPolicy_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 14, 22, 1, 1, 7),
    _OacZbfwZonePairsPolicy_Type()
)
oacZbfwZonePairsPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacZbfwZonePairsPolicy.setStatus("current")
_OacZbfwZonePairsCountersProcessed_Type = Counter32
_OacZbfwZonePairsCountersProcessed_Object = MibTableColumn
oacZbfwZonePairsCountersProcessed = _OacZbfwZonePairsCountersProcessed_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 14, 22, 1, 1, 8),
    _OacZbfwZonePairsCountersProcessed_Type()
)
oacZbfwZonePairsCountersProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacZbfwZonePairsCountersProcessed.setStatus("current")
_OacZbfwZonePairsCountersApplied_Type = Counter32
_OacZbfwZonePairsCountersApplied_Object = MibTableColumn
oacZbfwZonePairsCountersApplied = _OacZbfwZonePairsCountersApplied_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 14, 22, 1, 1, 9),
    _OacZbfwZonePairsCountersApplied_Type()
)
oacZbfwZonePairsCountersApplied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacZbfwZonePairsCountersApplied.setStatus("current")
_OacZbfwZonePairsCountersConnections_Type = Counter32
_OacZbfwZonePairsCountersConnections_Object = MibTableColumn
oacZbfwZonePairsCountersConnections = _OacZbfwZonePairsCountersConnections_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 14, 22, 1, 1, 10),
    _OacZbfwZonePairsCountersConnections_Type()
)
oacZbfwZonePairsCountersConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacZbfwZonePairsCountersConnections.setStatus("current")
_OacZbfwZonePairsCountersPackets_Type = Counter32
_OacZbfwZonePairsCountersPackets_Object = MibTableColumn
oacZbfwZonePairsCountersPackets = _OacZbfwZonePairsCountersPackets_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 14, 22, 1, 1, 11),
    _OacZbfwZonePairsCountersPackets_Type()
)
oacZbfwZonePairsCountersPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacZbfwZonePairsCountersPackets.setStatus("current")
_OacZbfwZonePairsCountersOctets_Type = Counter32
_OacZbfwZonePairsCountersOctets_Object = MibTableColumn
oacZbfwZonePairsCountersOctets = _OacZbfwZonePairsCountersOctets_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 14, 22, 1, 1, 12),
    _OacZbfwZonePairsCountersOctets_Type()
)
oacZbfwZonePairsCountersOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacZbfwZonePairsCountersOctets.setStatus("current")
_OacZbfwZonePairsCountersReversePackets_Type = Counter32
_OacZbfwZonePairsCountersReversePackets_Object = MibTableColumn
oacZbfwZonePairsCountersReversePackets = _OacZbfwZonePairsCountersReversePackets_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 14, 22, 1, 1, 13),
    _OacZbfwZonePairsCountersReversePackets_Type()
)
oacZbfwZonePairsCountersReversePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacZbfwZonePairsCountersReversePackets.setStatus("current")
_OacZbfwZonePairsCountersReverseOctets_Type = Counter32
_OacZbfwZonePairsCountersReverseOctets_Object = MibTableColumn
oacZbfwZonePairsCountersReverseOctets = _OacZbfwZonePairsCountersReverseOctets_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 14, 22, 1, 1, 14),
    _OacZbfwZonePairsCountersReverseOctets_Type()
)
oacZbfwZonePairsCountersReverseOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacZbfwZonePairsCountersReverseOctets.setStatus("current")
_OacZbfwFlows_ObjectIdentity = ObjectIdentity
oacZbfwFlows = _OacZbfwFlows_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 14, 23)
)
_OacZbfwFlowsSSCTable_Object = MibTable
oacZbfwFlowsSSCTable = _OacZbfwFlowsSSCTable_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 14, 23, 1)
)
if mibBuilder.loadTexts:
    oacZbfwFlowsSSCTable.setStatus("current")
_OacZbfwFlowsEntry_Object = MibTableRow
oacZbfwFlowsEntry = _OacZbfwFlowsEntry_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 14, 23, 1, 1)
)
oacZbfwFlowsEntry.setIndexNames(
    (0, "OA-ZBFW-STATUS-MIB", "oacZbfwFlowsTableIx"),
    (1, "OA-ZBFW-STATUS-MIB", "oacZbfwFlowsGlobalIx"),
)
if mibBuilder.loadTexts:
    oacZbfwFlowsEntry.setStatus("current")
_OacZbfwFlowsTableIx_Type = TableIndex
_OacZbfwFlowsTableIx_Object = MibTableColumn
oacZbfwFlowsTableIx = _OacZbfwFlowsTableIx_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 14, 23, 1, 1, 1),
    _OacZbfwFlowsTableIx_Type()
)
oacZbfwFlowsTableIx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oacZbfwFlowsTableIx.setStatus("current")
_OacZbfwFlowsGlobalIx_Type = SnmpAdminString
_OacZbfwFlowsGlobalIx_Object = MibTableColumn
oacZbfwFlowsGlobalIx = _OacZbfwFlowsGlobalIx_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 14, 23, 1, 1, 2),
    _OacZbfwFlowsGlobalIx_Type()
)
oacZbfwFlowsGlobalIx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oacZbfwFlowsGlobalIx.setStatus("current")
_OacZbfwFlowsConnectionId_Type = Counter32
_OacZbfwFlowsConnectionId_Object = MibTableColumn
oacZbfwFlowsConnectionId = _OacZbfwFlowsConnectionId_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 14, 23, 1, 1, 3),
    _OacZbfwFlowsConnectionId_Type()
)
oacZbfwFlowsConnectionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacZbfwFlowsConnectionId.setStatus("current")
_OacZbfwFlowsSrcIntf_Type = DisplayString
_OacZbfwFlowsSrcIntf_Object = MibTableColumn
oacZbfwFlowsSrcIntf = _OacZbfwFlowsSrcIntf_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 14, 23, 1, 1, 4),
    _OacZbfwFlowsSrcIntf_Type()
)
oacZbfwFlowsSrcIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacZbfwFlowsSrcIntf.setStatus("current")
_OacZbfwFlowsSrcZone_Type = DisplayString
_OacZbfwFlowsSrcZone_Object = MibTableColumn
oacZbfwFlowsSrcZone = _OacZbfwFlowsSrcZone_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 14, 23, 1, 1, 5),
    _OacZbfwFlowsSrcZone_Type()
)
oacZbfwFlowsSrcZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacZbfwFlowsSrcZone.setStatus("current")
_OacZbfwFlowsDstIntf_Type = DisplayString
_OacZbfwFlowsDstIntf_Object = MibTableColumn
oacZbfwFlowsDstIntf = _OacZbfwFlowsDstIntf_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 14, 23, 1, 1, 6),
    _OacZbfwFlowsDstIntf_Type()
)
oacZbfwFlowsDstIntf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacZbfwFlowsDstIntf.setStatus("current")
_OacZbfwFlowsDstZone_Type = DisplayString
_OacZbfwFlowsDstZone_Object = MibTableColumn
oacZbfwFlowsDstZone = _OacZbfwFlowsDstZone_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 14, 23, 1, 1, 7),
    _OacZbfwFlowsDstZone_Type()
)
oacZbfwFlowsDstZone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacZbfwFlowsDstZone.setStatus("current")
_OacZbfwFlowsSrcAddress_Type = IpAddress
_OacZbfwFlowsSrcAddress_Object = MibTableColumn
oacZbfwFlowsSrcAddress = _OacZbfwFlowsSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 14, 23, 1, 1, 8),
    _OacZbfwFlowsSrcAddress_Type()
)
oacZbfwFlowsSrcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacZbfwFlowsSrcAddress.setStatus("current")
_OacZbfwFlowsDstAddress_Type = IpAddress
_OacZbfwFlowsDstAddress_Object = MibTableColumn
oacZbfwFlowsDstAddress = _OacZbfwFlowsDstAddress_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 14, 23, 1, 1, 9),
    _OacZbfwFlowsDstAddress_Type()
)
oacZbfwFlowsDstAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacZbfwFlowsDstAddress.setStatus("current")


class _OacZbfwFlowsProtocol_Type(Integer32):
    """Custom type oacZbfwFlowsProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              6,
              8,
              9,
              17,
              46,
              47,
              50,
              51,
              88,
              89)
        )
    )
    namedValues = NamedValues(
        *(("ah", 51),
          ("any", 0),
          ("egp", 8),
          ("esp", 50),
          ("gre", 47),
          ("icmp", 1),
          ("igmp", 2),
          ("igp", 9),
          ("igrp", 88),
          ("ipInIp", 4),
          ("ospf", 89),
          ("rsvp", 46),
          ("tcp", 6),
          ("udp", 17))
    )


_OacZbfwFlowsProtocol_Type.__name__ = "Integer32"
_OacZbfwFlowsProtocol_Object = MibTableColumn
oacZbfwFlowsProtocol = _OacZbfwFlowsProtocol_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 14, 23, 1, 1, 10),
    _OacZbfwFlowsProtocol_Type()
)
oacZbfwFlowsProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacZbfwFlowsProtocol.setStatus("current")
_OacZbfwFlowsSrcPort_Type = Integer32
_OacZbfwFlowsSrcPort_Object = MibTableColumn
oacZbfwFlowsSrcPort = _OacZbfwFlowsSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 14, 23, 1, 1, 11),
    _OacZbfwFlowsSrcPort_Type()
)
oacZbfwFlowsSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacZbfwFlowsSrcPort.setStatus("current")
_OacZbfwFlowsDstPort_Type = Integer32
_OacZbfwFlowsDstPort_Object = MibTableColumn
oacZbfwFlowsDstPort = _OacZbfwFlowsDstPort_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 14, 23, 1, 1, 12),
    _OacZbfwFlowsDstPort_Type()
)
oacZbfwFlowsDstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacZbfwFlowsDstPort.setStatus("current")
_OacZbfwFlowsAge_Type = TimeTicks
_OacZbfwFlowsAge_Object = MibTableColumn
oacZbfwFlowsAge = _OacZbfwFlowsAge_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 14, 23, 1, 1, 13),
    _OacZbfwFlowsAge_Type()
)
oacZbfwFlowsAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacZbfwFlowsAge.setStatus("current")
_OacZbfwFlowsTimeOut_Type = TimeTicks
_OacZbfwFlowsTimeOut_Object = MibTableColumn
oacZbfwFlowsTimeOut = _OacZbfwFlowsTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 14, 23, 1, 1, 14),
    _OacZbfwFlowsTimeOut_Type()
)
oacZbfwFlowsTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacZbfwFlowsTimeOut.setStatus("current")
_OacZbfwFlowsRulesZonePair_Type = DisplayString
_OacZbfwFlowsRulesZonePair_Object = MibTableColumn
oacZbfwFlowsRulesZonePair = _OacZbfwFlowsRulesZonePair_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 14, 23, 1, 1, 15),
    _OacZbfwFlowsRulesZonePair_Type()
)
oacZbfwFlowsRulesZonePair.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacZbfwFlowsRulesZonePair.setStatus("current")
_OacZbfwFlowsRulesPolicy_Type = DisplayString
_OacZbfwFlowsRulesPolicy_Object = MibTableColumn
oacZbfwFlowsRulesPolicy = _OacZbfwFlowsRulesPolicy_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 14, 23, 1, 1, 16),
    _OacZbfwFlowsRulesPolicy_Type()
)
oacZbfwFlowsRulesPolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacZbfwFlowsRulesPolicy.setStatus("current")
_OacZbfwFlowsRulesPolicyRule_Type = DisplayString
_OacZbfwFlowsRulesPolicyRule_Object = MibTableColumn
oacZbfwFlowsRulesPolicyRule = _OacZbfwFlowsRulesPolicyRule_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 14, 23, 1, 1, 17),
    _OacZbfwFlowsRulesPolicyRule_Type()
)
oacZbfwFlowsRulesPolicyRule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacZbfwFlowsRulesPolicyRule.setStatus("current")
_OacZbfwFlowsRulesFilter_Type = DisplayString
_OacZbfwFlowsRulesFilter_Object = MibTableColumn
oacZbfwFlowsRulesFilter = _OacZbfwFlowsRulesFilter_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 14, 23, 1, 1, 18),
    _OacZbfwFlowsRulesFilter_Type()
)
oacZbfwFlowsRulesFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacZbfwFlowsRulesFilter.setStatus("current")
_OacZbfwFlowsRulesFilterRule_Type = DisplayString
_OacZbfwFlowsRulesFilterRule_Object = MibTableColumn
oacZbfwFlowsRulesFilterRule = _OacZbfwFlowsRulesFilterRule_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 14, 23, 1, 1, 19),
    _OacZbfwFlowsRulesFilterRule_Type()
)
oacZbfwFlowsRulesFilterRule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacZbfwFlowsRulesFilterRule.setStatus("current")


class _OacZbfwFlowsModeAlg_Type(Integer32):
    """Custom type oacZbfwFlowsModeAlg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_OacZbfwFlowsModeAlg_Type.__name__ = "Integer32"
_OacZbfwFlowsModeAlg_Object = MibTableColumn
oacZbfwFlowsModeAlg = _OacZbfwFlowsModeAlg_Object(
    (1, 3, 6, 1, 4, 1, 13191, 10, 3, 1, 9, 3131, 14, 23, 1, 1, 20),
    _OacZbfwFlowsModeAlg_Type()
)
oacZbfwFlowsModeAlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oacZbfwFlowsModeAlg.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OA-ZBFW-STATUS-MIB",
    **{"TableIndex": TableIndex,
       "oacZbfwStatusMIB": oacZbfwStatusMIB,
       "oacZbfw": oacZbfw,
       "oacZbfwPerf": oacZbfwPerf,
       "oacZbfwRtrConnPerf": oacZbfwRtrConnPerf,
       "oacZbfwRtrConnPerfSSCTable": oacZbfwRtrConnPerfSSCTable,
       "oacZbfwRtrConnPerfEntry": oacZbfwRtrConnPerfEntry,
       "oacZbfwRouterConnectionsCreated": oacZbfwRouterConnectionsCreated,
       "oacZbfwRouterConnectionsClosed": oacZbfwRouterConnectionsClosed,
       "oacZbfwRouterConnectionsTimedOut": oacZbfwRouterConnectionsTimedOut,
       "oacZbfwRouterConnectionsMax": oacZbfwRouterConnectionsMax,
       "oacZbfwRouterConnectionsMaxUsed": oacZbfwRouterConnectionsMaxUsed,
       "oacZbfwRouterConnectionsUsed": oacZbfwRouterConnectionsUsed,
       "oacZbfwRtrConnPerfGlobalIx": oacZbfwRtrConnPerfGlobalIx,
       "oacZbfwPackets": oacZbfwPackets,
       "oacZbfwPacketsSSCTable": oacZbfwPacketsSSCTable,
       "oacZbfwPacketsEntry": oacZbfwPacketsEntry,
       "oacZbfwPacketsGlobalIx": oacZbfwPacketsGlobalIx,
       "oacZbfwPacketsProcessed": oacZbfwPacketsProcessed,
       "oacZbfwPacketsPassed": oacZbfwPacketsPassed,
       "oacZbfwPacketsDropped": oacZbfwPacketsDropped,
       "oacZbfwPacketsRejected": oacZbfwPacketsRejected,
       "oacZbfwPacketsRejectStatsInvalidIntf": oacZbfwPacketsRejectStatsInvalidIntf,
       "oacZbfwPacketsRejectStatsNoPolicy": oacZbfwPacketsRejectStatsNoPolicy,
       "oacZbfwPacketsRejectStatsNoConnSetup": oacZbfwPacketsRejectStatsNoConnSetup,
       "oacZbfwPacketsRejectStatsProtocol": oacZbfwPacketsRejectStatsProtocol,
       "oacZbfwPacketsRejectStatsAlg": oacZbfwPacketsRejectStatsAlg,
       "oacZbfwPacketsRejectStatsConnExceeded": oacZbfwPacketsRejectStatsConnExceeded,
       "oacZbfwPolicyRules": oacZbfwPolicyRules,
       "oacZbfwPolicyRulesSSCTable": oacZbfwPolicyRulesSSCTable,
       "oacZbfwPolicyRulesEntry": oacZbfwPolicyRulesEntry,
       "oacZbfwPolicyRulesTableIx": oacZbfwPolicyRulesTableIx,
       "oacZbfwPolicyRulesGlobalIx": oacZbfwPolicyRulesGlobalIx,
       "oacZbfwPolicyRulesZonePair": oacZbfwPolicyRulesZonePair,
       "oacZbfwPolicyRulesPolicy": oacZbfwPolicyRulesPolicy,
       "oacZbfwPolicyRulesPolicyRule": oacZbfwPolicyRulesPolicyRule,
       "oacZbfwPolicyRulesCountersProcessed": oacZbfwPolicyRulesCountersProcessed,
       "oacZbfwPolicyRulesCountersApplied": oacZbfwPolicyRulesCountersApplied,
       "oacZbfwPolicyRulesCountersConnections": oacZbfwPolicyRulesCountersConnections,
       "oacZbfwPolicyRulesCountersPackets": oacZbfwPolicyRulesCountersPackets,
       "oacZbfwPolicyRulesCountersOctets": oacZbfwPolicyRulesCountersOctets,
       "oacZbfwPolicyRulesCountersReversePackets": oacZbfwPolicyRulesCountersReversePackets,
       "oacZbfwPolicyRulesCountersReverseOctets": oacZbfwPolicyRulesCountersReverseOctets,
       "oacZbfwClearCounters": oacZbfwClearCounters,
       "oacZbfwStatus": oacZbfwStatus,
       "oacZbfwZonePairs": oacZbfwZonePairs,
       "oacZbfwZonePairsSSCTable": oacZbfwZonePairsSSCTable,
       "oacZbfwZonePairsEntry": oacZbfwZonePairsEntry,
       "oacZbfwZonePairsTableIx": oacZbfwZonePairsTableIx,
       "oacZbfwZonePairsGlobalIx": oacZbfwZonePairsGlobalIx,
       "oacZbfwZonePairsName": oacZbfwZonePairsName,
       "oacZbfwZonePairsSrcZone": oacZbfwZonePairsSrcZone,
       "oacZbfwZonePairsDstZone": oacZbfwZonePairsDstZone,
       "oacZbfwZonePairsPolicy": oacZbfwZonePairsPolicy,
       "oacZbfwZonePairsCountersProcessed": oacZbfwZonePairsCountersProcessed,
       "oacZbfwZonePairsCountersApplied": oacZbfwZonePairsCountersApplied,
       "oacZbfwZonePairsCountersConnections": oacZbfwZonePairsCountersConnections,
       "oacZbfwZonePairsCountersPackets": oacZbfwZonePairsCountersPackets,
       "oacZbfwZonePairsCountersOctets": oacZbfwZonePairsCountersOctets,
       "oacZbfwZonePairsCountersReversePackets": oacZbfwZonePairsCountersReversePackets,
       "oacZbfwZonePairsCountersReverseOctets": oacZbfwZonePairsCountersReverseOctets,
       "oacZbfwFlows": oacZbfwFlows,
       "oacZbfwFlowsSSCTable": oacZbfwFlowsSSCTable,
       "oacZbfwFlowsEntry": oacZbfwFlowsEntry,
       "oacZbfwFlowsTableIx": oacZbfwFlowsTableIx,
       "oacZbfwFlowsGlobalIx": oacZbfwFlowsGlobalIx,
       "oacZbfwFlowsConnectionId": oacZbfwFlowsConnectionId,
       "oacZbfwFlowsSrcIntf": oacZbfwFlowsSrcIntf,
       "oacZbfwFlowsSrcZone": oacZbfwFlowsSrcZone,
       "oacZbfwFlowsDstIntf": oacZbfwFlowsDstIntf,
       "oacZbfwFlowsDstZone": oacZbfwFlowsDstZone,
       "oacZbfwFlowsSrcAddress": oacZbfwFlowsSrcAddress,
       "oacZbfwFlowsDstAddress": oacZbfwFlowsDstAddress,
       "oacZbfwFlowsProtocol": oacZbfwFlowsProtocol,
       "oacZbfwFlowsSrcPort": oacZbfwFlowsSrcPort,
       "oacZbfwFlowsDstPort": oacZbfwFlowsDstPort,
       "oacZbfwFlowsAge": oacZbfwFlowsAge,
       "oacZbfwFlowsTimeOut": oacZbfwFlowsTimeOut,
       "oacZbfwFlowsRulesZonePair": oacZbfwFlowsRulesZonePair,
       "oacZbfwFlowsRulesPolicy": oacZbfwFlowsRulesPolicy,
       "oacZbfwFlowsRulesPolicyRule": oacZbfwFlowsRulesPolicyRule,
       "oacZbfwFlowsRulesFilter": oacZbfwFlowsRulesFilter,
       "oacZbfwFlowsRulesFilterRule": oacZbfwFlowsRulesFilterRule,
       "oacZbfwFlowsModeAlg": oacZbfwFlowsModeAlg}
)
