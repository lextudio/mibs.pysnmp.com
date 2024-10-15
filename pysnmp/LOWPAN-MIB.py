# SNMP MIB module (LOWPAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/LOWPAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:19:22 2024
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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

lowpanMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 226)
)
lowpanMIB.setRevisions(
        ("2014-10-10 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LowpanNotifications_ObjectIdentity = ObjectIdentity
lowpanNotifications = _LowpanNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 226, 0)
)
_LowpanObjects_ObjectIdentity = ObjectIdentity
lowpanObjects = _LowpanObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 226, 1)
)
_LowpanStats_ObjectIdentity = ObjectIdentity
lowpanStats = _LowpanStats_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 226, 1, 1)
)
_LowpanReasmTimeout_Type = Unsigned32
_LowpanReasmTimeout_Object = MibScalar
lowpanReasmTimeout = _LowpanReasmTimeout_Object(
    (1, 3, 6, 1, 2, 1, 226, 1, 1, 1),
    _LowpanReasmTimeout_Type()
)
lowpanReasmTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowpanReasmTimeout.setStatus("current")
if mibBuilder.loadTexts:
    lowpanReasmTimeout.setUnits("seconds")
_LowpanInReceives_Type = Counter32
_LowpanInReceives_Object = MibScalar
lowpanInReceives = _LowpanInReceives_Object(
    (1, 3, 6, 1, 2, 1, 226, 1, 1, 2),
    _LowpanInReceives_Type()
)
lowpanInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowpanInReceives.setStatus("current")
_LowpanInHdrErrors_Type = Counter32
_LowpanInHdrErrors_Object = MibScalar
lowpanInHdrErrors = _LowpanInHdrErrors_Object(
    (1, 3, 6, 1, 2, 1, 226, 1, 1, 3),
    _LowpanInHdrErrors_Type()
)
lowpanInHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowpanInHdrErrors.setStatus("current")
_LowpanInMeshReceives_Type = Counter32
_LowpanInMeshReceives_Object = MibScalar
lowpanInMeshReceives = _LowpanInMeshReceives_Object(
    (1, 3, 6, 1, 2, 1, 226, 1, 1, 4),
    _LowpanInMeshReceives_Type()
)
lowpanInMeshReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowpanInMeshReceives.setStatus("current")
_LowpanInMeshForwds_Type = Counter32
_LowpanInMeshForwds_Object = MibScalar
lowpanInMeshForwds = _LowpanInMeshForwds_Object(
    (1, 3, 6, 1, 2, 1, 226, 1, 1, 5),
    _LowpanInMeshForwds_Type()
)
lowpanInMeshForwds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowpanInMeshForwds.setStatus("current")
_LowpanInMeshDelivers_Type = Counter32
_LowpanInMeshDelivers_Object = MibScalar
lowpanInMeshDelivers = _LowpanInMeshDelivers_Object(
    (1, 3, 6, 1, 2, 1, 226, 1, 1, 6),
    _LowpanInMeshDelivers_Type()
)
lowpanInMeshDelivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowpanInMeshDelivers.setStatus("current")
_LowpanInReasmReqds_Type = Counter32
_LowpanInReasmReqds_Object = MibScalar
lowpanInReasmReqds = _LowpanInReasmReqds_Object(
    (1, 3, 6, 1, 2, 1, 226, 1, 1, 7),
    _LowpanInReasmReqds_Type()
)
lowpanInReasmReqds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowpanInReasmReqds.setStatus("current")
_LowpanInReasmFails_Type = Counter32
_LowpanInReasmFails_Object = MibScalar
lowpanInReasmFails = _LowpanInReasmFails_Object(
    (1, 3, 6, 1, 2, 1, 226, 1, 1, 8),
    _LowpanInReasmFails_Type()
)
lowpanInReasmFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowpanInReasmFails.setStatus("current")
_LowpanInReasmOKs_Type = Counter32
_LowpanInReasmOKs_Object = MibScalar
lowpanInReasmOKs = _LowpanInReasmOKs_Object(
    (1, 3, 6, 1, 2, 1, 226, 1, 1, 9),
    _LowpanInReasmOKs_Type()
)
lowpanInReasmOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowpanInReasmOKs.setStatus("current")
_LowpanInCompReqds_Type = Counter32
_LowpanInCompReqds_Object = MibScalar
lowpanInCompReqds = _LowpanInCompReqds_Object(
    (1, 3, 6, 1, 2, 1, 226, 1, 1, 10),
    _LowpanInCompReqds_Type()
)
lowpanInCompReqds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowpanInCompReqds.setStatus("current")
_LowpanInCompFails_Type = Counter32
_LowpanInCompFails_Object = MibScalar
lowpanInCompFails = _LowpanInCompFails_Object(
    (1, 3, 6, 1, 2, 1, 226, 1, 1, 11),
    _LowpanInCompFails_Type()
)
lowpanInCompFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowpanInCompFails.setStatus("current")
_LowpanInCompOKs_Type = Counter32
_LowpanInCompOKs_Object = MibScalar
lowpanInCompOKs = _LowpanInCompOKs_Object(
    (1, 3, 6, 1, 2, 1, 226, 1, 1, 12),
    _LowpanInCompOKs_Type()
)
lowpanInCompOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowpanInCompOKs.setStatus("current")
_LowpanInDiscards_Type = Counter32
_LowpanInDiscards_Object = MibScalar
lowpanInDiscards = _LowpanInDiscards_Object(
    (1, 3, 6, 1, 2, 1, 226, 1, 1, 13),
    _LowpanInDiscards_Type()
)
lowpanInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowpanInDiscards.setStatus("current")
_LowpanInDelivers_Type = Counter32
_LowpanInDelivers_Object = MibScalar
lowpanInDelivers = _LowpanInDelivers_Object(
    (1, 3, 6, 1, 2, 1, 226, 1, 1, 14),
    _LowpanInDelivers_Type()
)
lowpanInDelivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowpanInDelivers.setStatus("current")
_LowpanOutRequests_Type = Counter32
_LowpanOutRequests_Object = MibScalar
lowpanOutRequests = _LowpanOutRequests_Object(
    (1, 3, 6, 1, 2, 1, 226, 1, 1, 15),
    _LowpanOutRequests_Type()
)
lowpanOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowpanOutRequests.setStatus("current")
_LowpanOutCompReqds_Type = Counter32
_LowpanOutCompReqds_Object = MibScalar
lowpanOutCompReqds = _LowpanOutCompReqds_Object(
    (1, 3, 6, 1, 2, 1, 226, 1, 1, 16),
    _LowpanOutCompReqds_Type()
)
lowpanOutCompReqds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowpanOutCompReqds.setStatus("current")
_LowpanOutCompFails_Type = Counter32
_LowpanOutCompFails_Object = MibScalar
lowpanOutCompFails = _LowpanOutCompFails_Object(
    (1, 3, 6, 1, 2, 1, 226, 1, 1, 17),
    _LowpanOutCompFails_Type()
)
lowpanOutCompFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowpanOutCompFails.setStatus("current")
_LowpanOutCompOKs_Type = Counter32
_LowpanOutCompOKs_Object = MibScalar
lowpanOutCompOKs = _LowpanOutCompOKs_Object(
    (1, 3, 6, 1, 2, 1, 226, 1, 1, 18),
    _LowpanOutCompOKs_Type()
)
lowpanOutCompOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowpanOutCompOKs.setStatus("current")
_LowpanOutFragReqds_Type = Counter32
_LowpanOutFragReqds_Object = MibScalar
lowpanOutFragReqds = _LowpanOutFragReqds_Object(
    (1, 3, 6, 1, 2, 1, 226, 1, 1, 19),
    _LowpanOutFragReqds_Type()
)
lowpanOutFragReqds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowpanOutFragReqds.setStatus("current")
_LowpanOutFragFails_Type = Counter32
_LowpanOutFragFails_Object = MibScalar
lowpanOutFragFails = _LowpanOutFragFails_Object(
    (1, 3, 6, 1, 2, 1, 226, 1, 1, 20),
    _LowpanOutFragFails_Type()
)
lowpanOutFragFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowpanOutFragFails.setStatus("current")
_LowpanOutFragOKs_Type = Counter32
_LowpanOutFragOKs_Object = MibScalar
lowpanOutFragOKs = _LowpanOutFragOKs_Object(
    (1, 3, 6, 1, 2, 1, 226, 1, 1, 21),
    _LowpanOutFragOKs_Type()
)
lowpanOutFragOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowpanOutFragOKs.setStatus("current")
_LowpanOutFragCreates_Type = Counter32
_LowpanOutFragCreates_Object = MibScalar
lowpanOutFragCreates = _LowpanOutFragCreates_Object(
    (1, 3, 6, 1, 2, 1, 226, 1, 1, 22),
    _LowpanOutFragCreates_Type()
)
lowpanOutFragCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowpanOutFragCreates.setStatus("current")
_LowpanOutMeshHopLimitExceeds_Type = Counter32
_LowpanOutMeshHopLimitExceeds_Object = MibScalar
lowpanOutMeshHopLimitExceeds = _LowpanOutMeshHopLimitExceeds_Object(
    (1, 3, 6, 1, 2, 1, 226, 1, 1, 23),
    _LowpanOutMeshHopLimitExceeds_Type()
)
lowpanOutMeshHopLimitExceeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowpanOutMeshHopLimitExceeds.setStatus("current")
_LowpanOutMeshNoRoutes_Type = Counter32
_LowpanOutMeshNoRoutes_Object = MibScalar
lowpanOutMeshNoRoutes = _LowpanOutMeshNoRoutes_Object(
    (1, 3, 6, 1, 2, 1, 226, 1, 1, 24),
    _LowpanOutMeshNoRoutes_Type()
)
lowpanOutMeshNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowpanOutMeshNoRoutes.setStatus("current")
_LowpanOutMeshRequests_Type = Counter32
_LowpanOutMeshRequests_Object = MibScalar
lowpanOutMeshRequests = _LowpanOutMeshRequests_Object(
    (1, 3, 6, 1, 2, 1, 226, 1, 1, 25),
    _LowpanOutMeshRequests_Type()
)
lowpanOutMeshRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowpanOutMeshRequests.setStatus("current")
_LowpanOutMeshForwds_Type = Counter32
_LowpanOutMeshForwds_Object = MibScalar
lowpanOutMeshForwds = _LowpanOutMeshForwds_Object(
    (1, 3, 6, 1, 2, 1, 226, 1, 1, 26),
    _LowpanOutMeshForwds_Type()
)
lowpanOutMeshForwds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowpanOutMeshForwds.setStatus("current")
_LowpanOutMeshTransmits_Type = Counter32
_LowpanOutMeshTransmits_Object = MibScalar
lowpanOutMeshTransmits = _LowpanOutMeshTransmits_Object(
    (1, 3, 6, 1, 2, 1, 226, 1, 1, 27),
    _LowpanOutMeshTransmits_Type()
)
lowpanOutMeshTransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowpanOutMeshTransmits.setStatus("current")
_LowpanOutDiscards_Type = Counter32
_LowpanOutDiscards_Object = MibScalar
lowpanOutDiscards = _LowpanOutDiscards_Object(
    (1, 3, 6, 1, 2, 1, 226, 1, 1, 28),
    _LowpanOutDiscards_Type()
)
lowpanOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowpanOutDiscards.setStatus("current")
_LowpanOutTransmits_Type = Counter32
_LowpanOutTransmits_Object = MibScalar
lowpanOutTransmits = _LowpanOutTransmits_Object(
    (1, 3, 6, 1, 2, 1, 226, 1, 1, 29),
    _LowpanOutTransmits_Type()
)
lowpanOutTransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowpanOutTransmits.setStatus("current")
_LowpanIfStatsTable_Object = MibTable
lowpanIfStatsTable = _LowpanIfStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 226, 1, 2)
)
if mibBuilder.loadTexts:
    lowpanIfStatsTable.setStatus("current")
_LowpanIfStatsEntry_Object = MibTableRow
lowpanIfStatsEntry = _LowpanIfStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 226, 1, 2, 1)
)
lowpanIfStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    lowpanIfStatsEntry.setStatus("current")
_LowpanIfReasmTimeout_Type = Unsigned32
_LowpanIfReasmTimeout_Object = MibTableColumn
lowpanIfReasmTimeout = _LowpanIfReasmTimeout_Object(
    (1, 3, 6, 1, 2, 1, 226, 1, 2, 1, 1),
    _LowpanIfReasmTimeout_Type()
)
lowpanIfReasmTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowpanIfReasmTimeout.setStatus("current")
if mibBuilder.loadTexts:
    lowpanIfReasmTimeout.setUnits("seconds")
_LowpanIfInReceives_Type = Counter32
_LowpanIfInReceives_Object = MibTableColumn
lowpanIfInReceives = _LowpanIfInReceives_Object(
    (1, 3, 6, 1, 2, 1, 226, 1, 2, 1, 2),
    _LowpanIfInReceives_Type()
)
lowpanIfInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowpanIfInReceives.setStatus("current")
_LowpanIfInHdrErrors_Type = Counter32
_LowpanIfInHdrErrors_Object = MibTableColumn
lowpanIfInHdrErrors = _LowpanIfInHdrErrors_Object(
    (1, 3, 6, 1, 2, 1, 226, 1, 2, 1, 3),
    _LowpanIfInHdrErrors_Type()
)
lowpanIfInHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowpanIfInHdrErrors.setStatus("current")
_LowpanIfInMeshReceives_Type = Counter32
_LowpanIfInMeshReceives_Object = MibTableColumn
lowpanIfInMeshReceives = _LowpanIfInMeshReceives_Object(
    (1, 3, 6, 1, 2, 1, 226, 1, 2, 1, 4),
    _LowpanIfInMeshReceives_Type()
)
lowpanIfInMeshReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowpanIfInMeshReceives.setStatus("current")
_LowpanIfInMeshForwds_Type = Counter32
_LowpanIfInMeshForwds_Object = MibTableColumn
lowpanIfInMeshForwds = _LowpanIfInMeshForwds_Object(
    (1, 3, 6, 1, 2, 1, 226, 1, 2, 1, 5),
    _LowpanIfInMeshForwds_Type()
)
lowpanIfInMeshForwds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowpanIfInMeshForwds.setStatus("current")
_LowpanIfInMeshDelivers_Type = Counter32
_LowpanIfInMeshDelivers_Object = MibTableColumn
lowpanIfInMeshDelivers = _LowpanIfInMeshDelivers_Object(
    (1, 3, 6, 1, 2, 1, 226, 1, 2, 1, 6),
    _LowpanIfInMeshDelivers_Type()
)
lowpanIfInMeshDelivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowpanIfInMeshDelivers.setStatus("current")
_LowpanIfInReasmReqds_Type = Counter32
_LowpanIfInReasmReqds_Object = MibTableColumn
lowpanIfInReasmReqds = _LowpanIfInReasmReqds_Object(
    (1, 3, 6, 1, 2, 1, 226, 1, 2, 1, 7),
    _LowpanIfInReasmReqds_Type()
)
lowpanIfInReasmReqds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowpanIfInReasmReqds.setStatus("current")
_LowpanIfInReasmFails_Type = Counter32
_LowpanIfInReasmFails_Object = MibTableColumn
lowpanIfInReasmFails = _LowpanIfInReasmFails_Object(
    (1, 3, 6, 1, 2, 1, 226, 1, 2, 1, 8),
    _LowpanIfInReasmFails_Type()
)
lowpanIfInReasmFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowpanIfInReasmFails.setStatus("current")
_LowpanIfInReasmOKs_Type = Counter32
_LowpanIfInReasmOKs_Object = MibTableColumn
lowpanIfInReasmOKs = _LowpanIfInReasmOKs_Object(
    (1, 3, 6, 1, 2, 1, 226, 1, 2, 1, 9),
    _LowpanIfInReasmOKs_Type()
)
lowpanIfInReasmOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowpanIfInReasmOKs.setStatus("current")
_LowpanIfInCompReqds_Type = Counter32
_LowpanIfInCompReqds_Object = MibTableColumn
lowpanIfInCompReqds = _LowpanIfInCompReqds_Object(
    (1, 3, 6, 1, 2, 1, 226, 1, 2, 1, 10),
    _LowpanIfInCompReqds_Type()
)
lowpanIfInCompReqds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowpanIfInCompReqds.setStatus("current")
_LowpanIfInCompFails_Type = Counter32
_LowpanIfInCompFails_Object = MibTableColumn
lowpanIfInCompFails = _LowpanIfInCompFails_Object(
    (1, 3, 6, 1, 2, 1, 226, 1, 2, 1, 11),
    _LowpanIfInCompFails_Type()
)
lowpanIfInCompFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowpanIfInCompFails.setStatus("current")
_LowpanIfInCompOKs_Type = Counter32
_LowpanIfInCompOKs_Object = MibTableColumn
lowpanIfInCompOKs = _LowpanIfInCompOKs_Object(
    (1, 3, 6, 1, 2, 1, 226, 1, 2, 1, 12),
    _LowpanIfInCompOKs_Type()
)
lowpanIfInCompOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowpanIfInCompOKs.setStatus("current")
_LowpanIfInDiscards_Type = Counter32
_LowpanIfInDiscards_Object = MibTableColumn
lowpanIfInDiscards = _LowpanIfInDiscards_Object(
    (1, 3, 6, 1, 2, 1, 226, 1, 2, 1, 13),
    _LowpanIfInDiscards_Type()
)
lowpanIfInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowpanIfInDiscards.setStatus("current")
_LowpanIfInDelivers_Type = Counter32
_LowpanIfInDelivers_Object = MibTableColumn
lowpanIfInDelivers = _LowpanIfInDelivers_Object(
    (1, 3, 6, 1, 2, 1, 226, 1, 2, 1, 14),
    _LowpanIfInDelivers_Type()
)
lowpanIfInDelivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowpanIfInDelivers.setStatus("current")
_LowpanIfOutRequests_Type = Counter32
_LowpanIfOutRequests_Object = MibTableColumn
lowpanIfOutRequests = _LowpanIfOutRequests_Object(
    (1, 3, 6, 1, 2, 1, 226, 1, 2, 1, 15),
    _LowpanIfOutRequests_Type()
)
lowpanIfOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowpanIfOutRequests.setStatus("current")
_LowpanIfOutCompReqds_Type = Counter32
_LowpanIfOutCompReqds_Object = MibTableColumn
lowpanIfOutCompReqds = _LowpanIfOutCompReqds_Object(
    (1, 3, 6, 1, 2, 1, 226, 1, 2, 1, 16),
    _LowpanIfOutCompReqds_Type()
)
lowpanIfOutCompReqds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowpanIfOutCompReqds.setStatus("current")
_LowpanIfOutCompFails_Type = Counter32
_LowpanIfOutCompFails_Object = MibTableColumn
lowpanIfOutCompFails = _LowpanIfOutCompFails_Object(
    (1, 3, 6, 1, 2, 1, 226, 1, 2, 1, 17),
    _LowpanIfOutCompFails_Type()
)
lowpanIfOutCompFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowpanIfOutCompFails.setStatus("current")
_LowpanIfOutCompOKs_Type = Counter32
_LowpanIfOutCompOKs_Object = MibTableColumn
lowpanIfOutCompOKs = _LowpanIfOutCompOKs_Object(
    (1, 3, 6, 1, 2, 1, 226, 1, 2, 1, 18),
    _LowpanIfOutCompOKs_Type()
)
lowpanIfOutCompOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowpanIfOutCompOKs.setStatus("current")
_LowpanIfOutFragReqds_Type = Counter32
_LowpanIfOutFragReqds_Object = MibTableColumn
lowpanIfOutFragReqds = _LowpanIfOutFragReqds_Object(
    (1, 3, 6, 1, 2, 1, 226, 1, 2, 1, 19),
    _LowpanIfOutFragReqds_Type()
)
lowpanIfOutFragReqds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowpanIfOutFragReqds.setStatus("current")
_LowpanIfOutFragFails_Type = Counter32
_LowpanIfOutFragFails_Object = MibTableColumn
lowpanIfOutFragFails = _LowpanIfOutFragFails_Object(
    (1, 3, 6, 1, 2, 1, 226, 1, 2, 1, 20),
    _LowpanIfOutFragFails_Type()
)
lowpanIfOutFragFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowpanIfOutFragFails.setStatus("current")
_LowpanIfOutFragOKs_Type = Counter32
_LowpanIfOutFragOKs_Object = MibTableColumn
lowpanIfOutFragOKs = _LowpanIfOutFragOKs_Object(
    (1, 3, 6, 1, 2, 1, 226, 1, 2, 1, 21),
    _LowpanIfOutFragOKs_Type()
)
lowpanIfOutFragOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowpanIfOutFragOKs.setStatus("current")
_LowpanIfOutFragCreates_Type = Counter32
_LowpanIfOutFragCreates_Object = MibTableColumn
lowpanIfOutFragCreates = _LowpanIfOutFragCreates_Object(
    (1, 3, 6, 1, 2, 1, 226, 1, 2, 1, 22),
    _LowpanIfOutFragCreates_Type()
)
lowpanIfOutFragCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowpanIfOutFragCreates.setStatus("current")
_LowpanIfOutMeshHopLimitExceeds_Type = Counter32
_LowpanIfOutMeshHopLimitExceeds_Object = MibTableColumn
lowpanIfOutMeshHopLimitExceeds = _LowpanIfOutMeshHopLimitExceeds_Object(
    (1, 3, 6, 1, 2, 1, 226, 1, 2, 1, 23),
    _LowpanIfOutMeshHopLimitExceeds_Type()
)
lowpanIfOutMeshHopLimitExceeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowpanIfOutMeshHopLimitExceeds.setStatus("current")
_LowpanIfOutMeshNoRoutes_Type = Counter32
_LowpanIfOutMeshNoRoutes_Object = MibTableColumn
lowpanIfOutMeshNoRoutes = _LowpanIfOutMeshNoRoutes_Object(
    (1, 3, 6, 1, 2, 1, 226, 1, 2, 1, 24),
    _LowpanIfOutMeshNoRoutes_Type()
)
lowpanIfOutMeshNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowpanIfOutMeshNoRoutes.setStatus("current")
_LowpanIfOutMeshRequests_Type = Counter32
_LowpanIfOutMeshRequests_Object = MibTableColumn
lowpanIfOutMeshRequests = _LowpanIfOutMeshRequests_Object(
    (1, 3, 6, 1, 2, 1, 226, 1, 2, 1, 25),
    _LowpanIfOutMeshRequests_Type()
)
lowpanIfOutMeshRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowpanIfOutMeshRequests.setStatus("current")
_LowpanIfOutMeshForwds_Type = Counter32
_LowpanIfOutMeshForwds_Object = MibTableColumn
lowpanIfOutMeshForwds = _LowpanIfOutMeshForwds_Object(
    (1, 3, 6, 1, 2, 1, 226, 1, 2, 1, 26),
    _LowpanIfOutMeshForwds_Type()
)
lowpanIfOutMeshForwds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowpanIfOutMeshForwds.setStatus("current")
_LowpanIfOutMeshTransmits_Type = Counter32
_LowpanIfOutMeshTransmits_Object = MibTableColumn
lowpanIfOutMeshTransmits = _LowpanIfOutMeshTransmits_Object(
    (1, 3, 6, 1, 2, 1, 226, 1, 2, 1, 27),
    _LowpanIfOutMeshTransmits_Type()
)
lowpanIfOutMeshTransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowpanIfOutMeshTransmits.setStatus("current")
_LowpanIfOutDiscards_Type = Counter32
_LowpanIfOutDiscards_Object = MibTableColumn
lowpanIfOutDiscards = _LowpanIfOutDiscards_Object(
    (1, 3, 6, 1, 2, 1, 226, 1, 2, 1, 28),
    _LowpanIfOutDiscards_Type()
)
lowpanIfOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowpanIfOutDiscards.setStatus("current")
_LowpanIfOutTransmits_Type = Counter32
_LowpanIfOutTransmits_Object = MibTableColumn
lowpanIfOutTransmits = _LowpanIfOutTransmits_Object(
    (1, 3, 6, 1, 2, 1, 226, 1, 2, 1, 29),
    _LowpanIfOutTransmits_Type()
)
lowpanIfOutTransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lowpanIfOutTransmits.setStatus("current")
_LowpanConformance_ObjectIdentity = ObjectIdentity
lowpanConformance = _LowpanConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 226, 2)
)
_LowpanGroups_ObjectIdentity = ObjectIdentity
lowpanGroups = _LowpanGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 226, 2, 1)
)
_LowpanCompliances_ObjectIdentity = ObjectIdentity
lowpanCompliances = _LowpanCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 226, 2, 2)
)

# Managed Objects groups

lowpanStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 226, 2, 1, 1)
)
lowpanStatsGroup.setObjects(
      *(("LOWPAN-MIB", "lowpanReasmTimeout"),
        ("LOWPAN-MIB", "lowpanInReceives"),
        ("LOWPAN-MIB", "lowpanInHdrErrors"),
        ("LOWPAN-MIB", "lowpanInMeshReceives"),
        ("LOWPAN-MIB", "lowpanInReasmReqds"),
        ("LOWPAN-MIB", "lowpanInReasmFails"),
        ("LOWPAN-MIB", "lowpanInReasmOKs"),
        ("LOWPAN-MIB", "lowpanInCompReqds"),
        ("LOWPAN-MIB", "lowpanInCompFails"),
        ("LOWPAN-MIB", "lowpanInCompOKs"),
        ("LOWPAN-MIB", "lowpanInDiscards"),
        ("LOWPAN-MIB", "lowpanInDelivers"),
        ("LOWPAN-MIB", "lowpanOutRequests"),
        ("LOWPAN-MIB", "lowpanOutCompReqds"),
        ("LOWPAN-MIB", "lowpanOutCompFails"),
        ("LOWPAN-MIB", "lowpanOutCompOKs"),
        ("LOWPAN-MIB", "lowpanOutFragReqds"),
        ("LOWPAN-MIB", "lowpanOutFragFails"),
        ("LOWPAN-MIB", "lowpanOutFragOKs"),
        ("LOWPAN-MIB", "lowpanOutFragCreates"),
        ("LOWPAN-MIB", "lowpanOutDiscards"),
        ("LOWPAN-MIB", "lowpanOutTransmits"))
)
if mibBuilder.loadTexts:
    lowpanStatsGroup.setStatus("current")

lowpanStatsMeshGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 226, 2, 1, 2)
)
lowpanStatsMeshGroup.setObjects(
      *(("LOWPAN-MIB", "lowpanInMeshForwds"),
        ("LOWPAN-MIB", "lowpanInMeshDelivers"),
        ("LOWPAN-MIB", "lowpanOutMeshHopLimitExceeds"),
        ("LOWPAN-MIB", "lowpanOutMeshNoRoutes"),
        ("LOWPAN-MIB", "lowpanOutMeshRequests"),
        ("LOWPAN-MIB", "lowpanOutMeshForwds"),
        ("LOWPAN-MIB", "lowpanOutMeshTransmits"))
)
if mibBuilder.loadTexts:
    lowpanStatsMeshGroup.setStatus("current")

lowpanIfStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 226, 2, 1, 3)
)
lowpanIfStatsGroup.setObjects(
      *(("LOWPAN-MIB", "lowpanIfReasmTimeout"),
        ("LOWPAN-MIB", "lowpanIfInReceives"),
        ("LOWPAN-MIB", "lowpanIfInHdrErrors"),
        ("LOWPAN-MIB", "lowpanIfInMeshReceives"),
        ("LOWPAN-MIB", "lowpanIfInReasmReqds"),
        ("LOWPAN-MIB", "lowpanIfInReasmFails"),
        ("LOWPAN-MIB", "lowpanIfInReasmOKs"),
        ("LOWPAN-MIB", "lowpanIfInCompReqds"),
        ("LOWPAN-MIB", "lowpanIfInCompFails"),
        ("LOWPAN-MIB", "lowpanIfInCompOKs"),
        ("LOWPAN-MIB", "lowpanIfInDiscards"),
        ("LOWPAN-MIB", "lowpanIfInDelivers"),
        ("LOWPAN-MIB", "lowpanIfOutRequests"),
        ("LOWPAN-MIB", "lowpanIfOutCompReqds"),
        ("LOWPAN-MIB", "lowpanIfOutCompFails"),
        ("LOWPAN-MIB", "lowpanIfOutCompOKs"),
        ("LOWPAN-MIB", "lowpanIfOutFragReqds"),
        ("LOWPAN-MIB", "lowpanIfOutFragFails"),
        ("LOWPAN-MIB", "lowpanIfOutFragOKs"),
        ("LOWPAN-MIB", "lowpanIfOutFragCreates"),
        ("LOWPAN-MIB", "lowpanIfOutDiscards"),
        ("LOWPAN-MIB", "lowpanIfOutTransmits"))
)
if mibBuilder.loadTexts:
    lowpanIfStatsGroup.setStatus("current")

lowpanIfStatsMeshGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 226, 2, 1, 4)
)
lowpanIfStatsMeshGroup.setObjects(
      *(("LOWPAN-MIB", "lowpanIfInMeshForwds"),
        ("LOWPAN-MIB", "lowpanIfInMeshDelivers"),
        ("LOWPAN-MIB", "lowpanIfOutMeshHopLimitExceeds"),
        ("LOWPAN-MIB", "lowpanIfOutMeshNoRoutes"),
        ("LOWPAN-MIB", "lowpanIfOutMeshRequests"),
        ("LOWPAN-MIB", "lowpanIfOutMeshForwds"),
        ("LOWPAN-MIB", "lowpanIfOutMeshTransmits"))
)
if mibBuilder.loadTexts:
    lowpanIfStatsMeshGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lowpanCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 226, 2, 2, 1)
)
if mibBuilder.loadTexts:
    lowpanCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LOWPAN-MIB",
    **{"lowpanMIB": lowpanMIB,
       "lowpanNotifications": lowpanNotifications,
       "lowpanObjects": lowpanObjects,
       "lowpanStats": lowpanStats,
       "lowpanReasmTimeout": lowpanReasmTimeout,
       "lowpanInReceives": lowpanInReceives,
       "lowpanInHdrErrors": lowpanInHdrErrors,
       "lowpanInMeshReceives": lowpanInMeshReceives,
       "lowpanInMeshForwds": lowpanInMeshForwds,
       "lowpanInMeshDelivers": lowpanInMeshDelivers,
       "lowpanInReasmReqds": lowpanInReasmReqds,
       "lowpanInReasmFails": lowpanInReasmFails,
       "lowpanInReasmOKs": lowpanInReasmOKs,
       "lowpanInCompReqds": lowpanInCompReqds,
       "lowpanInCompFails": lowpanInCompFails,
       "lowpanInCompOKs": lowpanInCompOKs,
       "lowpanInDiscards": lowpanInDiscards,
       "lowpanInDelivers": lowpanInDelivers,
       "lowpanOutRequests": lowpanOutRequests,
       "lowpanOutCompReqds": lowpanOutCompReqds,
       "lowpanOutCompFails": lowpanOutCompFails,
       "lowpanOutCompOKs": lowpanOutCompOKs,
       "lowpanOutFragReqds": lowpanOutFragReqds,
       "lowpanOutFragFails": lowpanOutFragFails,
       "lowpanOutFragOKs": lowpanOutFragOKs,
       "lowpanOutFragCreates": lowpanOutFragCreates,
       "lowpanOutMeshHopLimitExceeds": lowpanOutMeshHopLimitExceeds,
       "lowpanOutMeshNoRoutes": lowpanOutMeshNoRoutes,
       "lowpanOutMeshRequests": lowpanOutMeshRequests,
       "lowpanOutMeshForwds": lowpanOutMeshForwds,
       "lowpanOutMeshTransmits": lowpanOutMeshTransmits,
       "lowpanOutDiscards": lowpanOutDiscards,
       "lowpanOutTransmits": lowpanOutTransmits,
       "lowpanIfStatsTable": lowpanIfStatsTable,
       "lowpanIfStatsEntry": lowpanIfStatsEntry,
       "lowpanIfReasmTimeout": lowpanIfReasmTimeout,
       "lowpanIfInReceives": lowpanIfInReceives,
       "lowpanIfInHdrErrors": lowpanIfInHdrErrors,
       "lowpanIfInMeshReceives": lowpanIfInMeshReceives,
       "lowpanIfInMeshForwds": lowpanIfInMeshForwds,
       "lowpanIfInMeshDelivers": lowpanIfInMeshDelivers,
       "lowpanIfInReasmReqds": lowpanIfInReasmReqds,
       "lowpanIfInReasmFails": lowpanIfInReasmFails,
       "lowpanIfInReasmOKs": lowpanIfInReasmOKs,
       "lowpanIfInCompReqds": lowpanIfInCompReqds,
       "lowpanIfInCompFails": lowpanIfInCompFails,
       "lowpanIfInCompOKs": lowpanIfInCompOKs,
       "lowpanIfInDiscards": lowpanIfInDiscards,
       "lowpanIfInDelivers": lowpanIfInDelivers,
       "lowpanIfOutRequests": lowpanIfOutRequests,
       "lowpanIfOutCompReqds": lowpanIfOutCompReqds,
       "lowpanIfOutCompFails": lowpanIfOutCompFails,
       "lowpanIfOutCompOKs": lowpanIfOutCompOKs,
       "lowpanIfOutFragReqds": lowpanIfOutFragReqds,
       "lowpanIfOutFragFails": lowpanIfOutFragFails,
       "lowpanIfOutFragOKs": lowpanIfOutFragOKs,
       "lowpanIfOutFragCreates": lowpanIfOutFragCreates,
       "lowpanIfOutMeshHopLimitExceeds": lowpanIfOutMeshHopLimitExceeds,
       "lowpanIfOutMeshNoRoutes": lowpanIfOutMeshNoRoutes,
       "lowpanIfOutMeshRequests": lowpanIfOutMeshRequests,
       "lowpanIfOutMeshForwds": lowpanIfOutMeshForwds,
       "lowpanIfOutMeshTransmits": lowpanIfOutMeshTransmits,
       "lowpanIfOutDiscards": lowpanIfOutDiscards,
       "lowpanIfOutTransmits": lowpanIfOutTransmits,
       "lowpanConformance": lowpanConformance,
       "lowpanGroups": lowpanGroups,
       "lowpanStatsGroup": lowpanStatsGroup,
       "lowpanStatsMeshGroup": lowpanStatsMeshGroup,
       "lowpanIfStatsGroup": lowpanIfStatsGroup,
       "lowpanIfStatsMeshGroup": lowpanIfStatsMeshGroup,
       "lowpanCompliances": lowpanCompliances,
       "lowpanCompliance": lowpanCompliance}
)
