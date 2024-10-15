# SNMP MIB module (RBN-CIRCUIT-GROUP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RBN-CIRCUIT-GROUP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:45:02 2024
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

(RbnQosClassId,
 RbnQosPolicyType) = mibBuilder.importSymbols(
    "RBN-QOS-MIB",
    "RbnQosClassId",
    "RbnQosPolicyType")

(rbnMgmt,) = mibBuilder.importSymbols(
    "RBN-SMI",
    "rbnMgmt")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

rbnCircuitGroupMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 43)
)
rbnCircuitGroupMib.setRevisions(
        ("2008-07-30 00:00",
         "2007-07-25 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RbnCircuitGroupObjects_ObjectIdentity = ObjectIdentity
rbnCircuitGroupObjects = _RbnCircuitGroupObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 43, 1)
)
_RbnCircuitGroupStatsTable_Object = MibTable
rbnCircuitGroupStatsTable = _RbnCircuitGroupStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 43, 1, 1)
)
if mibBuilder.loadTexts:
    rbnCircuitGroupStatsTable.setStatus("current")
_RbnCircuitGroupStatsEntry_Object = MibTableRow
rbnCircuitGroupStatsEntry = _RbnCircuitGroupStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 43, 1, 1, 1)
)
rbnCircuitGroupStatsEntry.setIndexNames(
    (0, "RBN-CIRCUIT-GROUP-MIB", "rbnCctGrpName"),
)
if mibBuilder.loadTexts:
    rbnCircuitGroupStatsEntry.setStatus("current")


class _RbnCctGrpName_Type(SnmpAdminString):
    """Custom type rbnCctGrpName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 113),
    )


_RbnCctGrpName_Type.__name__ = "SnmpAdminString"
_RbnCctGrpName_Object = MibTableColumn
rbnCctGrpName = _RbnCctGrpName_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 43, 1, 1, 1, 1),
    _RbnCctGrpName_Type()
)
rbnCctGrpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnCctGrpName.setStatus("current")
_RbnCctGrpTxOctets_Type = Counter64
_RbnCctGrpTxOctets_Object = MibTableColumn
rbnCctGrpTxOctets = _RbnCctGrpTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 43, 1, 1, 1, 2),
    _RbnCctGrpTxOctets_Type()
)
rbnCctGrpTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCctGrpTxOctets.setStatus("current")
_RbnCctGrpTxPackets_Type = Counter64
_RbnCctGrpTxPackets_Object = MibTableColumn
rbnCctGrpTxPackets = _RbnCctGrpTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 43, 1, 1, 1, 3),
    _RbnCctGrpTxPackets_Type()
)
rbnCctGrpTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCctGrpTxPackets.setStatus("current")
_RbnCctGrpTxMulticastOctets_Type = Counter64
_RbnCctGrpTxMulticastOctets_Object = MibTableColumn
rbnCctGrpTxMulticastOctets = _RbnCctGrpTxMulticastOctets_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 43, 1, 1, 1, 4),
    _RbnCctGrpTxMulticastOctets_Type()
)
rbnCctGrpTxMulticastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCctGrpTxMulticastOctets.setStatus("current")
_RbnCctGrpTxMulticastPackets_Type = Counter64
_RbnCctGrpTxMulticastPackets_Object = MibTableColumn
rbnCctGrpTxMulticastPackets = _RbnCctGrpTxMulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 43, 1, 1, 1, 5),
    _RbnCctGrpTxMulticastPackets_Type()
)
rbnCctGrpTxMulticastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCctGrpTxMulticastPackets.setStatus("current")
_RbnCctGrpRxOctets_Type = Counter64
_RbnCctGrpRxOctets_Object = MibTableColumn
rbnCctGrpRxOctets = _RbnCctGrpRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 43, 1, 1, 1, 6),
    _RbnCctGrpRxOctets_Type()
)
rbnCctGrpRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCctGrpRxOctets.setStatus("current")
_RbnCctGrpRxPackets_Type = Counter64
_RbnCctGrpRxPackets_Object = MibTableColumn
rbnCctGrpRxPackets = _RbnCctGrpRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 43, 1, 1, 1, 7),
    _RbnCctGrpRxPackets_Type()
)
rbnCctGrpRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCctGrpRxPackets.setStatus("current")
_RbnCctGrpRxMulticastOctets_Type = Counter64
_RbnCctGrpRxMulticastOctets_Object = MibTableColumn
rbnCctGrpRxMulticastOctets = _RbnCctGrpRxMulticastOctets_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 43, 1, 1, 1, 8),
    _RbnCctGrpRxMulticastOctets_Type()
)
rbnCctGrpRxMulticastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCctGrpRxMulticastOctets.setStatus("current")
_RbnCctGrpRxMulticastPackets_Type = Counter64
_RbnCctGrpRxMulticastPackets_Object = MibTableColumn
rbnCctGrpRxMulticastPackets = _RbnCctGrpRxMulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 43, 1, 1, 1, 9),
    _RbnCctGrpRxMulticastPackets_Type()
)
rbnCctGrpRxMulticastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCctGrpRxMulticastPackets.setStatus("current")
_RbnCctGrpAdjDroppedOctets_Type = Counter64
_RbnCctGrpAdjDroppedOctets_Object = MibTableColumn
rbnCctGrpAdjDroppedOctets = _RbnCctGrpAdjDroppedOctets_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 43, 1, 1, 1, 10),
    _RbnCctGrpAdjDroppedOctets_Type()
)
rbnCctGrpAdjDroppedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCctGrpAdjDroppedOctets.setStatus("current")
_RbnCctGrpAdjDroppedPackets_Type = Counter64
_RbnCctGrpAdjDroppedPackets_Object = MibTableColumn
rbnCctGrpAdjDroppedPackets = _RbnCctGrpAdjDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 43, 1, 1, 1, 11),
    _RbnCctGrpAdjDroppedPackets_Type()
)
rbnCctGrpAdjDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCctGrpAdjDroppedPackets.setStatus("current")
_RbnCctGrpDownDroppedOctets_Type = Counter64
_RbnCctGrpDownDroppedOctets_Object = MibTableColumn
rbnCctGrpDownDroppedOctets = _RbnCctGrpDownDroppedOctets_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 43, 1, 1, 1, 12),
    _RbnCctGrpDownDroppedOctets_Type()
)
rbnCctGrpDownDroppedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCctGrpDownDroppedOctets.setStatus("current")
_RbnCctGrpDownDroppedPackets_Type = Counter64
_RbnCctGrpDownDroppedPackets_Object = MibTableColumn
rbnCctGrpDownDroppedPackets = _RbnCctGrpDownDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 43, 1, 1, 1, 13),
    _RbnCctGrpDownDroppedPackets_Type()
)
rbnCctGrpDownDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCctGrpDownDroppedPackets.setStatus("current")
_RbnCctGrpUnreachDroppedOctets_Type = Counter64
_RbnCctGrpUnreachDroppedOctets_Object = MibTableColumn
rbnCctGrpUnreachDroppedOctets = _RbnCctGrpUnreachDroppedOctets_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 43, 1, 1, 1, 14),
    _RbnCctGrpUnreachDroppedOctets_Type()
)
rbnCctGrpUnreachDroppedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCctGrpUnreachDroppedOctets.setStatus("current")
_RbnCctGrpUnreachDroppedPackets_Type = Counter64
_RbnCctGrpUnreachDroppedPackets_Object = MibTableColumn
rbnCctGrpUnreachDroppedPackets = _RbnCctGrpUnreachDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 43, 1, 1, 1, 15),
    _RbnCctGrpUnreachDroppedPackets_Type()
)
rbnCctGrpUnreachDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCctGrpUnreachDroppedPackets.setStatus("current")
_RbnCctGrpUnknownEncapsOctets_Type = Counter64
_RbnCctGrpUnknownEncapsOctets_Object = MibTableColumn
rbnCctGrpUnknownEncapsOctets = _RbnCctGrpUnknownEncapsOctets_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 43, 1, 1, 1, 16),
    _RbnCctGrpUnknownEncapsOctets_Type()
)
rbnCctGrpUnknownEncapsOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCctGrpUnknownEncapsOctets.setStatus("current")
_RbnCctGrpUnknownEncapsPackets_Type = Counter64
_RbnCctGrpUnknownEncapsPackets_Object = MibTableColumn
rbnCctGrpUnknownEncapsPackets = _RbnCctGrpUnknownEncapsPackets_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 43, 1, 1, 1, 17),
    _RbnCctGrpUnknownEncapsPackets_Type()
)
rbnCctGrpUnknownEncapsPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCctGrpUnknownEncapsPackets.setStatus("current")
_RbnCircuitGroupQTable_Object = MibTable
rbnCircuitGroupQTable = _RbnCircuitGroupQTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 43, 1, 2)
)
if mibBuilder.loadTexts:
    rbnCircuitGroupQTable.setStatus("current")
_RbnCircuitGroupQEntry_Object = MibTableRow
rbnCircuitGroupQEntry = _RbnCircuitGroupQEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 43, 1, 2, 1)
)
rbnCircuitGroupQEntry.setIndexNames(
    (0, "RBN-CIRCUIT-GROUP-MIB", "rbnCctGrpName"),
    (0, "RBN-CIRCUIT-GROUP-MIB", "rbnCctGrpQueueId"),
)
if mibBuilder.loadTexts:
    rbnCircuitGroupQEntry.setStatus("current")


class _RbnCctGrpQueueId_Type(Unsigned32):
    """Custom type rbnCctGrpQueueId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RbnCctGrpQueueId_Type.__name__ = "Unsigned32"
_RbnCctGrpQueueId_Object = MibTableColumn
rbnCctGrpQueueId = _RbnCctGrpQueueId_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 43, 1, 2, 1, 1),
    _RbnCctGrpQueueId_Type()
)
rbnCctGrpQueueId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnCctGrpQueueId.setStatus("current")
_RbnCctGrpQTxOctets_Type = Counter64
_RbnCctGrpQTxOctets_Object = MibTableColumn
rbnCctGrpQTxOctets = _RbnCctGrpQTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 43, 1, 2, 1, 2),
    _RbnCctGrpQTxOctets_Type()
)
rbnCctGrpQTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCctGrpQTxOctets.setStatus("current")
_RbnCctGrpQTxPackets_Type = Counter64
_RbnCctGrpQTxPackets_Object = MibTableColumn
rbnCctGrpQTxPackets = _RbnCctGrpQTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 43, 1, 2, 1, 3),
    _RbnCctGrpQTxPackets_Type()
)
rbnCctGrpQTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCctGrpQTxPackets.setStatus("current")
_RbnCctGrpQWredDroppedOctets_Type = Counter64
_RbnCctGrpQWredDroppedOctets_Object = MibTableColumn
rbnCctGrpQWredDroppedOctets = _RbnCctGrpQWredDroppedOctets_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 43, 1, 2, 1, 4),
    _RbnCctGrpQWredDroppedOctets_Type()
)
rbnCctGrpQWredDroppedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCctGrpQWredDroppedOctets.setStatus("current")
_RbnCctGrpQWredDroppedPkts_Type = Counter64
_RbnCctGrpQWredDroppedPkts_Object = MibTableColumn
rbnCctGrpQWredDroppedPkts = _RbnCctGrpQWredDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 43, 1, 2, 1, 5),
    _RbnCctGrpQWredDroppedPkts_Type()
)
rbnCctGrpQWredDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCctGrpQWredDroppedPkts.setStatus("current")
_RbnCctGrpQTailDroppedOctets_Type = Counter64
_RbnCctGrpQTailDroppedOctets_Object = MibTableColumn
rbnCctGrpQTailDroppedOctets = _RbnCctGrpQTailDroppedOctets_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 43, 1, 2, 1, 6),
    _RbnCctGrpQTailDroppedOctets_Type()
)
rbnCctGrpQTailDroppedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCctGrpQTailDroppedOctets.setStatus("current")
_RbnCctGrpQTailDroppedPkts_Type = Counter64
_RbnCctGrpQTailDroppedPkts_Object = MibTableColumn
rbnCctGrpQTailDroppedPkts = _RbnCctGrpQTailDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 43, 1, 2, 1, 7),
    _RbnCctGrpQTailDroppedPkts_Type()
)
rbnCctGrpQTailDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCctGrpQTailDroppedPkts.setStatus("current")
_RbnCctGrpRLPolicyStatsTable_Object = MibTable
rbnCctGrpRLPolicyStatsTable = _RbnCctGrpRLPolicyStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 43, 1, 3)
)
if mibBuilder.loadTexts:
    rbnCctGrpRLPolicyStatsTable.setStatus("current")
_RbnCctGrpRLPolicyStatsEntry_Object = MibTableRow
rbnCctGrpRLPolicyStatsEntry = _RbnCctGrpRLPolicyStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 43, 1, 3, 1)
)
rbnCctGrpRLPolicyStatsEntry.setIndexNames(
    (0, "RBN-CIRCUIT-GROUP-MIB", "rbnCctGrpName"),
    (0, "RBN-CIRCUIT-GROUP-MIB", "rbnCctGrpRLPolicyType"),
)
if mibBuilder.loadTexts:
    rbnCctGrpRLPolicyStatsEntry.setStatus("current")
_RbnCctGrpRLPolicyType_Type = RbnQosPolicyType
_RbnCctGrpRLPolicyType_Object = MibTableColumn
rbnCctGrpRLPolicyType = _RbnCctGrpRLPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 43, 1, 3, 1, 1),
    _RbnCctGrpRLPolicyType_Type()
)
rbnCctGrpRLPolicyType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnCctGrpRLPolicyType.setStatus("current")


class _RbnCctGrpRLPolicyName_Type(SnmpAdminString):
    """Custom type rbnCctGrpRLPolicyName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 39),
    )


_RbnCctGrpRLPolicyName_Type.__name__ = "SnmpAdminString"
_RbnCctGrpRLPolicyName_Object = MibTableColumn
rbnCctGrpRLPolicyName = _RbnCctGrpRLPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 43, 1, 3, 1, 2),
    _RbnCctGrpRLPolicyName_Type()
)
rbnCctGrpRLPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCctGrpRLPolicyName.setStatus("current")
_RbnCctGrpRLPolicyConformOctets_Type = Counter64
_RbnCctGrpRLPolicyConformOctets_Object = MibTableColumn
rbnCctGrpRLPolicyConformOctets = _RbnCctGrpRLPolicyConformOctets_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 43, 1, 3, 1, 3),
    _RbnCctGrpRLPolicyConformOctets_Type()
)
rbnCctGrpRLPolicyConformOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCctGrpRLPolicyConformOctets.setStatus("current")
_RbnCctGrpRLPolicyConformPkts_Type = Counter64
_RbnCctGrpRLPolicyConformPkts_Object = MibTableColumn
rbnCctGrpRLPolicyConformPkts = _RbnCctGrpRLPolicyConformPkts_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 43, 1, 3, 1, 4),
    _RbnCctGrpRLPolicyConformPkts_Type()
)
rbnCctGrpRLPolicyConformPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCctGrpRLPolicyConformPkts.setStatus("current")
_RbnCctGrpRLPolicyExceedOctets_Type = Counter64
_RbnCctGrpRLPolicyExceedOctets_Object = MibTableColumn
rbnCctGrpRLPolicyExceedOctets = _RbnCctGrpRLPolicyExceedOctets_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 43, 1, 3, 1, 5),
    _RbnCctGrpRLPolicyExceedOctets_Type()
)
rbnCctGrpRLPolicyExceedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCctGrpRLPolicyExceedOctets.setStatus("current")
_RbnCctGrpRLPolicyExceedPkts_Type = Counter64
_RbnCctGrpRLPolicyExceedPkts_Object = MibTableColumn
rbnCctGrpRLPolicyExceedPkts = _RbnCctGrpRLPolicyExceedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 43, 1, 3, 1, 6),
    _RbnCctGrpRLPolicyExceedPkts_Type()
)
rbnCctGrpRLPolicyExceedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCctGrpRLPolicyExceedPkts.setStatus("current")
_RbnCctGrpRLPolicyExceedDroppedOctets_Type = Counter64
_RbnCctGrpRLPolicyExceedDroppedOctets_Object = MibTableColumn
rbnCctGrpRLPolicyExceedDroppedOctets = _RbnCctGrpRLPolicyExceedDroppedOctets_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 43, 1, 3, 1, 7),
    _RbnCctGrpRLPolicyExceedDroppedOctets_Type()
)
rbnCctGrpRLPolicyExceedDroppedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCctGrpRLPolicyExceedDroppedOctets.setStatus("current")
_RbnCctGrpRLPolicyExceedDroppedPkts_Type = Counter64
_RbnCctGrpRLPolicyExceedDroppedPkts_Object = MibTableColumn
rbnCctGrpRLPolicyExceedDroppedPkts = _RbnCctGrpRLPolicyExceedDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 43, 1, 3, 1, 8),
    _RbnCctGrpRLPolicyExceedDroppedPkts_Type()
)
rbnCctGrpRLPolicyExceedDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCctGrpRLPolicyExceedDroppedPkts.setStatus("current")
_RbnCctGrpRLPolicyViolateOctets_Type = Counter64
_RbnCctGrpRLPolicyViolateOctets_Object = MibTableColumn
rbnCctGrpRLPolicyViolateOctets = _RbnCctGrpRLPolicyViolateOctets_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 43, 1, 3, 1, 9),
    _RbnCctGrpRLPolicyViolateOctets_Type()
)
rbnCctGrpRLPolicyViolateOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCctGrpRLPolicyViolateOctets.setStatus("current")
_RbnCctGrpRLPolicyViolatePkts_Type = Counter64
_RbnCctGrpRLPolicyViolatePkts_Object = MibTableColumn
rbnCctGrpRLPolicyViolatePkts = _RbnCctGrpRLPolicyViolatePkts_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 43, 1, 3, 1, 10),
    _RbnCctGrpRLPolicyViolatePkts_Type()
)
rbnCctGrpRLPolicyViolatePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCctGrpRLPolicyViolatePkts.setStatus("current")
_RbnCctGrpRLPolicyViolateDroppedOctets_Type = Counter64
_RbnCctGrpRLPolicyViolateDroppedOctets_Object = MibTableColumn
rbnCctGrpRLPolicyViolateDroppedOctets = _RbnCctGrpRLPolicyViolateDroppedOctets_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 43, 1, 3, 1, 11),
    _RbnCctGrpRLPolicyViolateDroppedOctets_Type()
)
rbnCctGrpRLPolicyViolateDroppedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCctGrpRLPolicyViolateDroppedOctets.setStatus("current")
_RbnCctGrpRLPolicyViolateDroppedPkts_Type = Counter64
_RbnCctGrpRLPolicyViolateDroppedPkts_Object = MibTableColumn
rbnCctGrpRLPolicyViolateDroppedPkts = _RbnCctGrpRLPolicyViolateDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 43, 1, 3, 1, 12),
    _RbnCctGrpRLPolicyViolateDroppedPkts_Type()
)
rbnCctGrpRLPolicyViolateDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCctGrpRLPolicyViolateDroppedPkts.setStatus("current")
_RbnCctGrpRLClassStatsTable_Object = MibTable
rbnCctGrpRLClassStatsTable = _RbnCctGrpRLClassStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 43, 1, 4)
)
if mibBuilder.loadTexts:
    rbnCctGrpRLClassStatsTable.setStatus("current")
_RbnCctGrpRLClassStatsEntry_Object = MibTableRow
rbnCctGrpRLClassStatsEntry = _RbnCctGrpRLClassStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 43, 1, 4, 1)
)
rbnCctGrpRLClassStatsEntry.setIndexNames(
    (0, "RBN-CIRCUIT-GROUP-MIB", "rbnCctGrpName"),
    (0, "RBN-CIRCUIT-GROUP-MIB", "rbnCctGrpRLPolicyType"),
    (0, "RBN-CIRCUIT-GROUP-MIB", "rbnCctGrpRLClassId"),
)
if mibBuilder.loadTexts:
    rbnCctGrpRLClassStatsEntry.setStatus("current")
_RbnCctGrpRLClassId_Type = RbnQosClassId
_RbnCctGrpRLClassId_Object = MibTableColumn
rbnCctGrpRLClassId = _RbnCctGrpRLClassId_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 43, 1, 4, 1, 1),
    _RbnCctGrpRLClassId_Type()
)
rbnCctGrpRLClassId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnCctGrpRLClassId.setStatus("current")


class _RbnCctGrpRLClassName_Type(SnmpAdminString):
    """Custom type rbnCctGrpRLClassName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 39),
    )


_RbnCctGrpRLClassName_Type.__name__ = "SnmpAdminString"
_RbnCctGrpRLClassName_Object = MibTableColumn
rbnCctGrpRLClassName = _RbnCctGrpRLClassName_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 43, 1, 4, 1, 2),
    _RbnCctGrpRLClassName_Type()
)
rbnCctGrpRLClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCctGrpRLClassName.setStatus("current")
_RbnCctGrpRLClassConformOctets_Type = Counter64
_RbnCctGrpRLClassConformOctets_Object = MibTableColumn
rbnCctGrpRLClassConformOctets = _RbnCctGrpRLClassConformOctets_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 43, 1, 4, 1, 3),
    _RbnCctGrpRLClassConformOctets_Type()
)
rbnCctGrpRLClassConformOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCctGrpRLClassConformOctets.setStatus("current")
_RbnCctGrpRLClassConformPkts_Type = Counter64
_RbnCctGrpRLClassConformPkts_Object = MibTableColumn
rbnCctGrpRLClassConformPkts = _RbnCctGrpRLClassConformPkts_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 43, 1, 4, 1, 4),
    _RbnCctGrpRLClassConformPkts_Type()
)
rbnCctGrpRLClassConformPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCctGrpRLClassConformPkts.setStatus("current")
_RbnCctGrpRLClassConformDroppedOctets_Type = Counter64
_RbnCctGrpRLClassConformDroppedOctets_Object = MibTableColumn
rbnCctGrpRLClassConformDroppedOctets = _RbnCctGrpRLClassConformDroppedOctets_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 43, 1, 4, 1, 5),
    _RbnCctGrpRLClassConformDroppedOctets_Type()
)
rbnCctGrpRLClassConformDroppedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCctGrpRLClassConformDroppedOctets.setStatus("current")
_RbnCctGrpRLClassConformDroppedPkts_Type = Counter64
_RbnCctGrpRLClassConformDroppedPkts_Object = MibTableColumn
rbnCctGrpRLClassConformDroppedPkts = _RbnCctGrpRLClassConformDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 43, 1, 4, 1, 6),
    _RbnCctGrpRLClassConformDroppedPkts_Type()
)
rbnCctGrpRLClassConformDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCctGrpRLClassConformDroppedPkts.setStatus("current")
_RbnCctGrpRLClassExceedOctets_Type = Counter64
_RbnCctGrpRLClassExceedOctets_Object = MibTableColumn
rbnCctGrpRLClassExceedOctets = _RbnCctGrpRLClassExceedOctets_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 43, 1, 4, 1, 7),
    _RbnCctGrpRLClassExceedOctets_Type()
)
rbnCctGrpRLClassExceedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCctGrpRLClassExceedOctets.setStatus("current")
_RbnCctGrpRLClassExceedPkts_Type = Counter64
_RbnCctGrpRLClassExceedPkts_Object = MibTableColumn
rbnCctGrpRLClassExceedPkts = _RbnCctGrpRLClassExceedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 43, 1, 4, 1, 8),
    _RbnCctGrpRLClassExceedPkts_Type()
)
rbnCctGrpRLClassExceedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCctGrpRLClassExceedPkts.setStatus("current")
_RbnCctGrpRLClassExceedDroppedOctets_Type = Counter64
_RbnCctGrpRLClassExceedDroppedOctets_Object = MibTableColumn
rbnCctGrpRLClassExceedDroppedOctets = _RbnCctGrpRLClassExceedDroppedOctets_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 43, 1, 4, 1, 9),
    _RbnCctGrpRLClassExceedDroppedOctets_Type()
)
rbnCctGrpRLClassExceedDroppedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCctGrpRLClassExceedDroppedOctets.setStatus("current")
_RbnCctGrpRLClassExceedDroppedPkts_Type = Counter64
_RbnCctGrpRLClassExceedDroppedPkts_Object = MibTableColumn
rbnCctGrpRLClassExceedDroppedPkts = _RbnCctGrpRLClassExceedDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 43, 1, 4, 1, 10),
    _RbnCctGrpRLClassExceedDroppedPkts_Type()
)
rbnCctGrpRLClassExceedDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCctGrpRLClassExceedDroppedPkts.setStatus("current")
_RbnCctGrpRLClassViolateOctets_Type = Counter64
_RbnCctGrpRLClassViolateOctets_Object = MibTableColumn
rbnCctGrpRLClassViolateOctets = _RbnCctGrpRLClassViolateOctets_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 43, 1, 4, 1, 11),
    _RbnCctGrpRLClassViolateOctets_Type()
)
rbnCctGrpRLClassViolateOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCctGrpRLClassViolateOctets.setStatus("current")
_RbnCctGrpRLClassViolatePkts_Type = Counter64
_RbnCctGrpRLClassViolatePkts_Object = MibTableColumn
rbnCctGrpRLClassViolatePkts = _RbnCctGrpRLClassViolatePkts_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 43, 1, 4, 1, 12),
    _RbnCctGrpRLClassViolatePkts_Type()
)
rbnCctGrpRLClassViolatePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCctGrpRLClassViolatePkts.setStatus("current")
_RbnCctGrpRLClassViolateDroppedOctets_Type = Counter64
_RbnCctGrpRLClassViolateDroppedOctets_Object = MibTableColumn
rbnCctGrpRLClassViolateDroppedOctets = _RbnCctGrpRLClassViolateDroppedOctets_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 43, 1, 4, 1, 13),
    _RbnCctGrpRLClassViolateDroppedOctets_Type()
)
rbnCctGrpRLClassViolateDroppedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCctGrpRLClassViolateDroppedOctets.setStatus("current")
_RbnCctGrpRLClassViolateDroppedPkts_Type = Counter64
_RbnCctGrpRLClassViolateDroppedPkts_Object = MibTableColumn
rbnCctGrpRLClassViolateDroppedPkts = _RbnCctGrpRLClassViolateDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 43, 1, 4, 1, 14),
    _RbnCctGrpRLClassViolateDroppedPkts_Type()
)
rbnCctGrpRLClassViolateDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnCctGrpRLClassViolateDroppedPkts.setStatus("current")
_RbnCircuitGroupConformance_ObjectIdentity = ObjectIdentity
rbnCircuitGroupConformance = _RbnCircuitGroupConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 43, 2)
)
_RbnCircuitGroupCompliances_ObjectIdentity = ObjectIdentity
rbnCircuitGroupCompliances = _RbnCircuitGroupCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 43, 2, 1)
)
_RbnCircuitGroupConformGroups_ObjectIdentity = ObjectIdentity
rbnCircuitGroupConformGroups = _RbnCircuitGroupConformGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 43, 2, 2)
)

# Managed Objects groups

rbnCctGrpStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 43, 2, 2, 1)
)
rbnCctGrpStatsGroup.setObjects(
      *(("RBN-CIRCUIT-GROUP-MIB", "rbnCctGrpTxOctets"),
        ("RBN-CIRCUIT-GROUP-MIB", "rbnCctGrpTxPackets"),
        ("RBN-CIRCUIT-GROUP-MIB", "rbnCctGrpTxMulticastOctets"),
        ("RBN-CIRCUIT-GROUP-MIB", "rbnCctGrpTxMulticastPackets"),
        ("RBN-CIRCUIT-GROUP-MIB", "rbnCctGrpRxOctets"),
        ("RBN-CIRCUIT-GROUP-MIB", "rbnCctGrpRxPackets"),
        ("RBN-CIRCUIT-GROUP-MIB", "rbnCctGrpRxMulticastOctets"),
        ("RBN-CIRCUIT-GROUP-MIB", "rbnCctGrpRxMulticastPackets"),
        ("RBN-CIRCUIT-GROUP-MIB", "rbnCctGrpAdjDroppedOctets"),
        ("RBN-CIRCUIT-GROUP-MIB", "rbnCctGrpAdjDroppedPackets"),
        ("RBN-CIRCUIT-GROUP-MIB", "rbnCctGrpDownDroppedOctets"),
        ("RBN-CIRCUIT-GROUP-MIB", "rbnCctGrpDownDroppedPackets"),
        ("RBN-CIRCUIT-GROUP-MIB", "rbnCctGrpUnreachDroppedOctets"),
        ("RBN-CIRCUIT-GROUP-MIB", "rbnCctGrpUnreachDroppedPackets"),
        ("RBN-CIRCUIT-GROUP-MIB", "rbnCctGrpUnknownEncapsOctets"),
        ("RBN-CIRCUIT-GROUP-MIB", "rbnCctGrpUnknownEncapsPackets"))
)
if mibBuilder.loadTexts:
    rbnCctGrpStatsGroup.setStatus("current")

rbnCctGrpQStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 43, 2, 2, 2)
)
rbnCctGrpQStatsGroup.setObjects(
      *(("RBN-CIRCUIT-GROUP-MIB", "rbnCctGrpQTxOctets"),
        ("RBN-CIRCUIT-GROUP-MIB", "rbnCctGrpQTxPackets"),
        ("RBN-CIRCUIT-GROUP-MIB", "rbnCctGrpQWredDroppedOctets"),
        ("RBN-CIRCUIT-GROUP-MIB", "rbnCctGrpQWredDroppedPkts"),
        ("RBN-CIRCUIT-GROUP-MIB", "rbnCctGrpQTailDroppedOctets"),
        ("RBN-CIRCUIT-GROUP-MIB", "rbnCctGrpQTailDroppedPkts"))
)
if mibBuilder.loadTexts:
    rbnCctGrpQStatsGroup.setStatus("current")

rbnCctGrpPolicyStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 43, 2, 2, 3)
)
rbnCctGrpPolicyStatsGroup.setObjects(
      *(("RBN-CIRCUIT-GROUP-MIB", "rbnCctGrpRLPolicyName"),
        ("RBN-CIRCUIT-GROUP-MIB", "rbnCctGrpRLPolicyConformOctets"),
        ("RBN-CIRCUIT-GROUP-MIB", "rbnCctGrpRLPolicyConformPkts"),
        ("RBN-CIRCUIT-GROUP-MIB", "rbnCctGrpRLPolicyExceedOctets"),
        ("RBN-CIRCUIT-GROUP-MIB", "rbnCctGrpRLPolicyExceedPkts"),
        ("RBN-CIRCUIT-GROUP-MIB", "rbnCctGrpRLPolicyExceedDroppedOctets"),
        ("RBN-CIRCUIT-GROUP-MIB", "rbnCctGrpRLPolicyExceedDroppedPkts"),
        ("RBN-CIRCUIT-GROUP-MIB", "rbnCctGrpRLPolicyViolateOctets"),
        ("RBN-CIRCUIT-GROUP-MIB", "rbnCctGrpRLPolicyViolatePkts"),
        ("RBN-CIRCUIT-GROUP-MIB", "rbnCctGrpRLPolicyViolateDroppedOctets"),
        ("RBN-CIRCUIT-GROUP-MIB", "rbnCctGrpRLPolicyViolateDroppedPkts"),
        ("RBN-CIRCUIT-GROUP-MIB", "rbnCctGrpRLClassName"),
        ("RBN-CIRCUIT-GROUP-MIB", "rbnCctGrpRLClassConformOctets"),
        ("RBN-CIRCUIT-GROUP-MIB", "rbnCctGrpRLClassConformPkts"),
        ("RBN-CIRCUIT-GROUP-MIB", "rbnCctGrpRLClassConformDroppedOctets"),
        ("RBN-CIRCUIT-GROUP-MIB", "rbnCctGrpRLClassConformDroppedPkts"),
        ("RBN-CIRCUIT-GROUP-MIB", "rbnCctGrpRLClassExceedOctets"),
        ("RBN-CIRCUIT-GROUP-MIB", "rbnCctGrpRLClassExceedPkts"),
        ("RBN-CIRCUIT-GROUP-MIB", "rbnCctGrpRLClassExceedDroppedOctets"),
        ("RBN-CIRCUIT-GROUP-MIB", "rbnCctGrpRLClassExceedDroppedPkts"),
        ("RBN-CIRCUIT-GROUP-MIB", "rbnCctGrpRLClassViolateOctets"),
        ("RBN-CIRCUIT-GROUP-MIB", "rbnCctGrpRLClassViolatePkts"),
        ("RBN-CIRCUIT-GROUP-MIB", "rbnCctGrpRLClassViolateDroppedOctets"),
        ("RBN-CIRCUIT-GROUP-MIB", "rbnCctGrpRLClassViolateDroppedPkts"))
)
if mibBuilder.loadTexts:
    rbnCctGrpPolicyStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rbnCCircuitGroupCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 43, 2, 1, 1)
)
if mibBuilder.loadTexts:
    rbnCCircuitGroupCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RBN-CIRCUIT-GROUP-MIB",
    **{"rbnCircuitGroupMib": rbnCircuitGroupMib,
       "rbnCircuitGroupObjects": rbnCircuitGroupObjects,
       "rbnCircuitGroupStatsTable": rbnCircuitGroupStatsTable,
       "rbnCircuitGroupStatsEntry": rbnCircuitGroupStatsEntry,
       "rbnCctGrpName": rbnCctGrpName,
       "rbnCctGrpTxOctets": rbnCctGrpTxOctets,
       "rbnCctGrpTxPackets": rbnCctGrpTxPackets,
       "rbnCctGrpTxMulticastOctets": rbnCctGrpTxMulticastOctets,
       "rbnCctGrpTxMulticastPackets": rbnCctGrpTxMulticastPackets,
       "rbnCctGrpRxOctets": rbnCctGrpRxOctets,
       "rbnCctGrpRxPackets": rbnCctGrpRxPackets,
       "rbnCctGrpRxMulticastOctets": rbnCctGrpRxMulticastOctets,
       "rbnCctGrpRxMulticastPackets": rbnCctGrpRxMulticastPackets,
       "rbnCctGrpAdjDroppedOctets": rbnCctGrpAdjDroppedOctets,
       "rbnCctGrpAdjDroppedPackets": rbnCctGrpAdjDroppedPackets,
       "rbnCctGrpDownDroppedOctets": rbnCctGrpDownDroppedOctets,
       "rbnCctGrpDownDroppedPackets": rbnCctGrpDownDroppedPackets,
       "rbnCctGrpUnreachDroppedOctets": rbnCctGrpUnreachDroppedOctets,
       "rbnCctGrpUnreachDroppedPackets": rbnCctGrpUnreachDroppedPackets,
       "rbnCctGrpUnknownEncapsOctets": rbnCctGrpUnknownEncapsOctets,
       "rbnCctGrpUnknownEncapsPackets": rbnCctGrpUnknownEncapsPackets,
       "rbnCircuitGroupQTable": rbnCircuitGroupQTable,
       "rbnCircuitGroupQEntry": rbnCircuitGroupQEntry,
       "rbnCctGrpQueueId": rbnCctGrpQueueId,
       "rbnCctGrpQTxOctets": rbnCctGrpQTxOctets,
       "rbnCctGrpQTxPackets": rbnCctGrpQTxPackets,
       "rbnCctGrpQWredDroppedOctets": rbnCctGrpQWredDroppedOctets,
       "rbnCctGrpQWredDroppedPkts": rbnCctGrpQWredDroppedPkts,
       "rbnCctGrpQTailDroppedOctets": rbnCctGrpQTailDroppedOctets,
       "rbnCctGrpQTailDroppedPkts": rbnCctGrpQTailDroppedPkts,
       "rbnCctGrpRLPolicyStatsTable": rbnCctGrpRLPolicyStatsTable,
       "rbnCctGrpRLPolicyStatsEntry": rbnCctGrpRLPolicyStatsEntry,
       "rbnCctGrpRLPolicyType": rbnCctGrpRLPolicyType,
       "rbnCctGrpRLPolicyName": rbnCctGrpRLPolicyName,
       "rbnCctGrpRLPolicyConformOctets": rbnCctGrpRLPolicyConformOctets,
       "rbnCctGrpRLPolicyConformPkts": rbnCctGrpRLPolicyConformPkts,
       "rbnCctGrpRLPolicyExceedOctets": rbnCctGrpRLPolicyExceedOctets,
       "rbnCctGrpRLPolicyExceedPkts": rbnCctGrpRLPolicyExceedPkts,
       "rbnCctGrpRLPolicyExceedDroppedOctets": rbnCctGrpRLPolicyExceedDroppedOctets,
       "rbnCctGrpRLPolicyExceedDroppedPkts": rbnCctGrpRLPolicyExceedDroppedPkts,
       "rbnCctGrpRLPolicyViolateOctets": rbnCctGrpRLPolicyViolateOctets,
       "rbnCctGrpRLPolicyViolatePkts": rbnCctGrpRLPolicyViolatePkts,
       "rbnCctGrpRLPolicyViolateDroppedOctets": rbnCctGrpRLPolicyViolateDroppedOctets,
       "rbnCctGrpRLPolicyViolateDroppedPkts": rbnCctGrpRLPolicyViolateDroppedPkts,
       "rbnCctGrpRLClassStatsTable": rbnCctGrpRLClassStatsTable,
       "rbnCctGrpRLClassStatsEntry": rbnCctGrpRLClassStatsEntry,
       "rbnCctGrpRLClassId": rbnCctGrpRLClassId,
       "rbnCctGrpRLClassName": rbnCctGrpRLClassName,
       "rbnCctGrpRLClassConformOctets": rbnCctGrpRLClassConformOctets,
       "rbnCctGrpRLClassConformPkts": rbnCctGrpRLClassConformPkts,
       "rbnCctGrpRLClassConformDroppedOctets": rbnCctGrpRLClassConformDroppedOctets,
       "rbnCctGrpRLClassConformDroppedPkts": rbnCctGrpRLClassConformDroppedPkts,
       "rbnCctGrpRLClassExceedOctets": rbnCctGrpRLClassExceedOctets,
       "rbnCctGrpRLClassExceedPkts": rbnCctGrpRLClassExceedPkts,
       "rbnCctGrpRLClassExceedDroppedOctets": rbnCctGrpRLClassExceedDroppedOctets,
       "rbnCctGrpRLClassExceedDroppedPkts": rbnCctGrpRLClassExceedDroppedPkts,
       "rbnCctGrpRLClassViolateOctets": rbnCctGrpRLClassViolateOctets,
       "rbnCctGrpRLClassViolatePkts": rbnCctGrpRLClassViolatePkts,
       "rbnCctGrpRLClassViolateDroppedOctets": rbnCctGrpRLClassViolateDroppedOctets,
       "rbnCctGrpRLClassViolateDroppedPkts": rbnCctGrpRLClassViolateDroppedPkts,
       "rbnCircuitGroupConformance": rbnCircuitGroupConformance,
       "rbnCircuitGroupCompliances": rbnCircuitGroupCompliances,
       "rbnCCircuitGroupCompliance": rbnCCircuitGroupCompliance,
       "rbnCircuitGroupConformGroups": rbnCircuitGroupConformGroups,
       "rbnCctGrpStatsGroup": rbnCctGrpStatsGroup,
       "rbnCctGrpQStatsGroup": rbnCctGrpQStatsGroup,
       "rbnCctGrpPolicyStatsGroup": rbnCctGrpPolicyStatsGroup}
)
