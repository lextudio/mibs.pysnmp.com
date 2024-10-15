# SNMP MIB module (BAS-ALIAS-IP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BAS-ALIAS-IP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:45:17 2024
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

(BasChassisId,
 BasInterfaceId,
 BasLogicalPortId,
 BasSlotId,
 basAliasIp) = mibBuilder.importSymbols(
    "BAS-MIB",
    "BasChassisId",
    "BasInterfaceId",
    "BasLogicalPortId",
    "BasSlotId",
    "basAliasIp")

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

basAliasIpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BasIpAlias_ObjectIdentity = ObjectIdentity
basIpAlias = _BasIpAlias_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 1)
)
_BasIpTable_Object = MibTable
basIpTable = _BasIpTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    basIpTable.setStatus("current")
_BasIpEntry_Object = MibTableRow
basIpEntry = _BasIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 1, 1, 1)
)
basIpEntry.setIndexNames(
    (0, "BAS-ALIAS-IP-MIB", "basIpChassis"),
    (0, "BAS-ALIAS-IP-MIB", "basIpSlot"),
    (0, "BAS-ALIAS-IP-MIB", "basIpIf"),
    (0, "BAS-ALIAS-IP-MIB", "basIpLPort"),
)
if mibBuilder.loadTexts:
    basIpEntry.setStatus("current")


class _BasIpForwarding_Type(Integer32):
    """Custom type basIpForwarding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forwarding", 1),
          ("notForwarding", 2))
    )


_BasIpForwarding_Type.__name__ = "Integer32"
_BasIpForwarding_Object = MibTableColumn
basIpForwarding = _BasIpForwarding_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 1, 1, 1, 1),
    _BasIpForwarding_Type()
)
basIpForwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basIpForwarding.setStatus("current")


class _BasIpDefaultTTL_Type(Integer32):
    """Custom type basIpDefaultTTL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_BasIpDefaultTTL_Type.__name__ = "Integer32"
_BasIpDefaultTTL_Object = MibTableColumn
basIpDefaultTTL = _BasIpDefaultTTL_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 1, 1, 1, 2),
    _BasIpDefaultTTL_Type()
)
basIpDefaultTTL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    basIpDefaultTTL.setStatus("current")
_BasIpInReceives_Type = Counter32
_BasIpInReceives_Object = MibTableColumn
basIpInReceives = _BasIpInReceives_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 1, 1, 1, 3),
    _BasIpInReceives_Type()
)
basIpInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basIpInReceives.setStatus("current")
_BasIpInHdrErrors_Type = Counter32
_BasIpInHdrErrors_Object = MibTableColumn
basIpInHdrErrors = _BasIpInHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 1, 1, 1, 4),
    _BasIpInHdrErrors_Type()
)
basIpInHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basIpInHdrErrors.setStatus("current")
_BasIpInAddrErrors_Type = Counter32
_BasIpInAddrErrors_Object = MibTableColumn
basIpInAddrErrors = _BasIpInAddrErrors_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 1, 1, 1, 5),
    _BasIpInAddrErrors_Type()
)
basIpInAddrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basIpInAddrErrors.setStatus("current")
_BasIpForwDatagrams_Type = Counter32
_BasIpForwDatagrams_Object = MibTableColumn
basIpForwDatagrams = _BasIpForwDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 1, 1, 1, 6),
    _BasIpForwDatagrams_Type()
)
basIpForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basIpForwDatagrams.setStatus("current")
_BasIpInUnknownProtos_Type = Counter32
_BasIpInUnknownProtos_Object = MibTableColumn
basIpInUnknownProtos = _BasIpInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 1, 1, 1, 7),
    _BasIpInUnknownProtos_Type()
)
basIpInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basIpInUnknownProtos.setStatus("current")
_BasIpInDiscards_Type = Counter32
_BasIpInDiscards_Object = MibTableColumn
basIpInDiscards = _BasIpInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 1, 1, 1, 8),
    _BasIpInDiscards_Type()
)
basIpInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basIpInDiscards.setStatus("current")
_BasIpInDelivers_Type = Counter32
_BasIpInDelivers_Object = MibTableColumn
basIpInDelivers = _BasIpInDelivers_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 1, 1, 1, 9),
    _BasIpInDelivers_Type()
)
basIpInDelivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basIpInDelivers.setStatus("current")
_BasIpOutRequests_Type = Counter32
_BasIpOutRequests_Object = MibTableColumn
basIpOutRequests = _BasIpOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 1, 1, 1, 10),
    _BasIpOutRequests_Type()
)
basIpOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basIpOutRequests.setStatus("current")
_BasIpOutDiscards_Type = Counter32
_BasIpOutDiscards_Object = MibTableColumn
basIpOutDiscards = _BasIpOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 1, 1, 1, 11),
    _BasIpOutDiscards_Type()
)
basIpOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basIpOutDiscards.setStatus("current")
_BasIpOutNoRoutes_Type = Counter32
_BasIpOutNoRoutes_Object = MibTableColumn
basIpOutNoRoutes = _BasIpOutNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 1, 1, 1, 12),
    _BasIpOutNoRoutes_Type()
)
basIpOutNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basIpOutNoRoutes.setStatus("current")
_BasIpReasmTimeout_Type = Integer32
_BasIpReasmTimeout_Object = MibTableColumn
basIpReasmTimeout = _BasIpReasmTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 1, 1, 1, 13),
    _BasIpReasmTimeout_Type()
)
basIpReasmTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basIpReasmTimeout.setStatus("current")
_BasIpReasmReqds_Type = Counter32
_BasIpReasmReqds_Object = MibTableColumn
basIpReasmReqds = _BasIpReasmReqds_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 1, 1, 1, 14),
    _BasIpReasmReqds_Type()
)
basIpReasmReqds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basIpReasmReqds.setStatus("current")
_BasIpReasmOKs_Type = Counter32
_BasIpReasmOKs_Object = MibTableColumn
basIpReasmOKs = _BasIpReasmOKs_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 1, 1, 1, 15),
    _BasIpReasmOKs_Type()
)
basIpReasmOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basIpReasmOKs.setStatus("current")
_BasIpReasmFails_Type = Counter32
_BasIpReasmFails_Object = MibTableColumn
basIpReasmFails = _BasIpReasmFails_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 1, 1, 1, 16),
    _BasIpReasmFails_Type()
)
basIpReasmFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basIpReasmFails.setStatus("current")
_BasIpFragOKs_Type = Counter32
_BasIpFragOKs_Object = MibTableColumn
basIpFragOKs = _BasIpFragOKs_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 1, 1, 1, 17),
    _BasIpFragOKs_Type()
)
basIpFragOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basIpFragOKs.setStatus("current")
_BasIpFragFails_Type = Counter32
_BasIpFragFails_Object = MibTableColumn
basIpFragFails = _BasIpFragFails_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 1, 1, 1, 18),
    _BasIpFragFails_Type()
)
basIpFragFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basIpFragFails.setStatus("current")
_BasIpFragCreates_Type = Counter32
_BasIpFragCreates_Object = MibTableColumn
basIpFragCreates = _BasIpFragCreates_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 1, 1, 1, 19),
    _BasIpFragCreates_Type()
)
basIpFragCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basIpFragCreates.setStatus("current")
_BasIpChassis_Type = BasChassisId
_BasIpChassis_Object = MibTableColumn
basIpChassis = _BasIpChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 1, 1, 1, 20),
    _BasIpChassis_Type()
)
basIpChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basIpChassis.setStatus("current")
_BasIpSlot_Type = BasSlotId
_BasIpSlot_Object = MibTableColumn
basIpSlot = _BasIpSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 1, 1, 1, 21),
    _BasIpSlot_Type()
)
basIpSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basIpSlot.setStatus("current")
_BasIpIf_Type = BasInterfaceId
_BasIpIf_Object = MibTableColumn
basIpIf = _BasIpIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 1, 1, 1, 22),
    _BasIpIf_Type()
)
basIpIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basIpIf.setStatus("current")
_BasIpLPort_Type = BasLogicalPortId
_BasIpLPort_Object = MibTableColumn
basIpLPort = _BasIpLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 1, 1, 1, 23),
    _BasIpLPort_Type()
)
basIpLPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basIpLPort.setStatus("current")
_BasIcmp_ObjectIdentity = ObjectIdentity
basIcmp = _BasIcmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2)
)
_BasIcmpTable_Object = MibTable
basIcmpTable = _BasIcmpTable_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    basIcmpTable.setStatus("current")
_BasIcmpEntry_Object = MibTableRow
basIcmpEntry = _BasIcmpEntry_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1)
)
basIcmpEntry.setIndexNames(
    (0, "BAS-ALIAS-IP-MIB", "basIcmpChassis"),
    (0, "BAS-ALIAS-IP-MIB", "basIcmpSlot"),
    (0, "BAS-ALIAS-IP-MIB", "basIcmpIf"),
    (0, "BAS-ALIAS-IP-MIB", "basIcmpLPort"),
)
if mibBuilder.loadTexts:
    basIcmpEntry.setStatus("current")
_BasIcmpInMsgs_Type = Counter32
_BasIcmpInMsgs_Object = MibTableColumn
basIcmpInMsgs = _BasIcmpInMsgs_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 1),
    _BasIcmpInMsgs_Type()
)
basIcmpInMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basIcmpInMsgs.setStatus("current")
_BasIcmpInErrors_Type = Counter32
_BasIcmpInErrors_Object = MibTableColumn
basIcmpInErrors = _BasIcmpInErrors_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 2),
    _BasIcmpInErrors_Type()
)
basIcmpInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basIcmpInErrors.setStatus("current")
_BasIcmpInDestUnreachs_Type = Counter32
_BasIcmpInDestUnreachs_Object = MibTableColumn
basIcmpInDestUnreachs = _BasIcmpInDestUnreachs_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 3),
    _BasIcmpInDestUnreachs_Type()
)
basIcmpInDestUnreachs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basIcmpInDestUnreachs.setStatus("current")
_BasIcmpInTimeExcds_Type = Counter32
_BasIcmpInTimeExcds_Object = MibTableColumn
basIcmpInTimeExcds = _BasIcmpInTimeExcds_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 4),
    _BasIcmpInTimeExcds_Type()
)
basIcmpInTimeExcds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basIcmpInTimeExcds.setStatus("current")
_BasIcmpInParmProbs_Type = Counter32
_BasIcmpInParmProbs_Object = MibTableColumn
basIcmpInParmProbs = _BasIcmpInParmProbs_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 5),
    _BasIcmpInParmProbs_Type()
)
basIcmpInParmProbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basIcmpInParmProbs.setStatus("current")
_BasIcmpInSrcQuenchs_Type = Counter32
_BasIcmpInSrcQuenchs_Object = MibTableColumn
basIcmpInSrcQuenchs = _BasIcmpInSrcQuenchs_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 6),
    _BasIcmpInSrcQuenchs_Type()
)
basIcmpInSrcQuenchs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basIcmpInSrcQuenchs.setStatus("current")
_BasIcmpInRedirects_Type = Counter32
_BasIcmpInRedirects_Object = MibTableColumn
basIcmpInRedirects = _BasIcmpInRedirects_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 7),
    _BasIcmpInRedirects_Type()
)
basIcmpInRedirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basIcmpInRedirects.setStatus("current")
_BasIcmpInEchos_Type = Counter32
_BasIcmpInEchos_Object = MibTableColumn
basIcmpInEchos = _BasIcmpInEchos_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 8),
    _BasIcmpInEchos_Type()
)
basIcmpInEchos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basIcmpInEchos.setStatus("current")
_BasIcmpInEchoReps_Type = Counter32
_BasIcmpInEchoReps_Object = MibTableColumn
basIcmpInEchoReps = _BasIcmpInEchoReps_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 9),
    _BasIcmpInEchoReps_Type()
)
basIcmpInEchoReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basIcmpInEchoReps.setStatus("current")
_BasIcmpInTimestamps_Type = Counter32
_BasIcmpInTimestamps_Object = MibTableColumn
basIcmpInTimestamps = _BasIcmpInTimestamps_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 10),
    _BasIcmpInTimestamps_Type()
)
basIcmpInTimestamps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basIcmpInTimestamps.setStatus("current")
_BasIcmpInTimestampReps_Type = Counter32
_BasIcmpInTimestampReps_Object = MibTableColumn
basIcmpInTimestampReps = _BasIcmpInTimestampReps_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 11),
    _BasIcmpInTimestampReps_Type()
)
basIcmpInTimestampReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basIcmpInTimestampReps.setStatus("current")
_BasIcmpInAddrMasks_Type = Counter32
_BasIcmpInAddrMasks_Object = MibTableColumn
basIcmpInAddrMasks = _BasIcmpInAddrMasks_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 12),
    _BasIcmpInAddrMasks_Type()
)
basIcmpInAddrMasks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basIcmpInAddrMasks.setStatus("current")
_BasIcmpInAddrMaskReps_Type = Counter32
_BasIcmpInAddrMaskReps_Object = MibTableColumn
basIcmpInAddrMaskReps = _BasIcmpInAddrMaskReps_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 13),
    _BasIcmpInAddrMaskReps_Type()
)
basIcmpInAddrMaskReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basIcmpInAddrMaskReps.setStatus("current")
_BasIcmpOutMsgs_Type = Counter32
_BasIcmpOutMsgs_Object = MibTableColumn
basIcmpOutMsgs = _BasIcmpOutMsgs_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 14),
    _BasIcmpOutMsgs_Type()
)
basIcmpOutMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basIcmpOutMsgs.setStatus("current")
_BasIcmpOutErrors_Type = Counter32
_BasIcmpOutErrors_Object = MibTableColumn
basIcmpOutErrors = _BasIcmpOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 15),
    _BasIcmpOutErrors_Type()
)
basIcmpOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basIcmpOutErrors.setStatus("current")
_BasIcmpOutDestUnreachs_Type = Counter32
_BasIcmpOutDestUnreachs_Object = MibTableColumn
basIcmpOutDestUnreachs = _BasIcmpOutDestUnreachs_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 16),
    _BasIcmpOutDestUnreachs_Type()
)
basIcmpOutDestUnreachs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basIcmpOutDestUnreachs.setStatus("current")
_BasIcmpOutTimeExcds_Type = Counter32
_BasIcmpOutTimeExcds_Object = MibTableColumn
basIcmpOutTimeExcds = _BasIcmpOutTimeExcds_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 17),
    _BasIcmpOutTimeExcds_Type()
)
basIcmpOutTimeExcds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basIcmpOutTimeExcds.setStatus("current")
_BasIcmpOutParmProbs_Type = Counter32
_BasIcmpOutParmProbs_Object = MibTableColumn
basIcmpOutParmProbs = _BasIcmpOutParmProbs_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 18),
    _BasIcmpOutParmProbs_Type()
)
basIcmpOutParmProbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basIcmpOutParmProbs.setStatus("current")
_BasIcmpOutSrcQuenchs_Type = Counter32
_BasIcmpOutSrcQuenchs_Object = MibTableColumn
basIcmpOutSrcQuenchs = _BasIcmpOutSrcQuenchs_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 19),
    _BasIcmpOutSrcQuenchs_Type()
)
basIcmpOutSrcQuenchs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basIcmpOutSrcQuenchs.setStatus("current")
_BasIcmpOutRedirects_Type = Counter32
_BasIcmpOutRedirects_Object = MibTableColumn
basIcmpOutRedirects = _BasIcmpOutRedirects_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 20),
    _BasIcmpOutRedirects_Type()
)
basIcmpOutRedirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basIcmpOutRedirects.setStatus("current")
_BasIcmpOutEchos_Type = Counter32
_BasIcmpOutEchos_Object = MibTableColumn
basIcmpOutEchos = _BasIcmpOutEchos_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 21),
    _BasIcmpOutEchos_Type()
)
basIcmpOutEchos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basIcmpOutEchos.setStatus("current")
_BasIcmpOutEchoReps_Type = Counter32
_BasIcmpOutEchoReps_Object = MibTableColumn
basIcmpOutEchoReps = _BasIcmpOutEchoReps_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 22),
    _BasIcmpOutEchoReps_Type()
)
basIcmpOutEchoReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basIcmpOutEchoReps.setStatus("current")
_BasIcmpOutTimestamps_Type = Counter32
_BasIcmpOutTimestamps_Object = MibTableColumn
basIcmpOutTimestamps = _BasIcmpOutTimestamps_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 23),
    _BasIcmpOutTimestamps_Type()
)
basIcmpOutTimestamps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basIcmpOutTimestamps.setStatus("current")
_BasIcmpOutTimestampReps_Type = Counter32
_BasIcmpOutTimestampReps_Object = MibTableColumn
basIcmpOutTimestampReps = _BasIcmpOutTimestampReps_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 24),
    _BasIcmpOutTimestampReps_Type()
)
basIcmpOutTimestampReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basIcmpOutTimestampReps.setStatus("current")
_BasIcmpOutAddrMasks_Type = Counter32
_BasIcmpOutAddrMasks_Object = MibTableColumn
basIcmpOutAddrMasks = _BasIcmpOutAddrMasks_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 25),
    _BasIcmpOutAddrMasks_Type()
)
basIcmpOutAddrMasks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basIcmpOutAddrMasks.setStatus("current")
_BasIcmpOutAddrMaskReps_Type = Counter32
_BasIcmpOutAddrMaskReps_Object = MibTableColumn
basIcmpOutAddrMaskReps = _BasIcmpOutAddrMaskReps_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 26),
    _BasIcmpOutAddrMaskReps_Type()
)
basIcmpOutAddrMaskReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    basIcmpOutAddrMaskReps.setStatus("current")
_BasIcmpChassis_Type = BasChassisId
_BasIcmpChassis_Object = MibTableColumn
basIcmpChassis = _BasIcmpChassis_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 27),
    _BasIcmpChassis_Type()
)
basIcmpChassis.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basIcmpChassis.setStatus("current")
_BasIcmpSlot_Type = BasSlotId
_BasIcmpSlot_Object = MibTableColumn
basIcmpSlot = _BasIcmpSlot_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 28),
    _BasIcmpSlot_Type()
)
basIcmpSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basIcmpSlot.setStatus("current")
_BasIcmpIf_Type = BasInterfaceId
_BasIcmpIf_Object = MibTableColumn
basIcmpIf = _BasIcmpIf_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 29),
    _BasIcmpIf_Type()
)
basIcmpIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basIcmpIf.setStatus("current")
_BasIcmpLPort_Type = BasLogicalPortId
_BasIcmpLPort_Object = MibTableColumn
basIcmpLPort = _BasIcmpLPort_Object(
    (1, 3, 6, 1, 4, 1, 3493, 2, 7, 2, 1, 2, 1, 1, 30),
    _BasIcmpLPort_Type()
)
basIcmpLPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    basIcmpLPort.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BAS-ALIAS-IP-MIB",
    **{"basAliasIpMib": basAliasIpMib,
       "basIpAlias": basIpAlias,
       "basIpTable": basIpTable,
       "basIpEntry": basIpEntry,
       "basIpForwarding": basIpForwarding,
       "basIpDefaultTTL": basIpDefaultTTL,
       "basIpInReceives": basIpInReceives,
       "basIpInHdrErrors": basIpInHdrErrors,
       "basIpInAddrErrors": basIpInAddrErrors,
       "basIpForwDatagrams": basIpForwDatagrams,
       "basIpInUnknownProtos": basIpInUnknownProtos,
       "basIpInDiscards": basIpInDiscards,
       "basIpInDelivers": basIpInDelivers,
       "basIpOutRequests": basIpOutRequests,
       "basIpOutDiscards": basIpOutDiscards,
       "basIpOutNoRoutes": basIpOutNoRoutes,
       "basIpReasmTimeout": basIpReasmTimeout,
       "basIpReasmReqds": basIpReasmReqds,
       "basIpReasmOKs": basIpReasmOKs,
       "basIpReasmFails": basIpReasmFails,
       "basIpFragOKs": basIpFragOKs,
       "basIpFragFails": basIpFragFails,
       "basIpFragCreates": basIpFragCreates,
       "basIpChassis": basIpChassis,
       "basIpSlot": basIpSlot,
       "basIpIf": basIpIf,
       "basIpLPort": basIpLPort,
       "basIcmp": basIcmp,
       "basIcmpTable": basIcmpTable,
       "basIcmpEntry": basIcmpEntry,
       "basIcmpInMsgs": basIcmpInMsgs,
       "basIcmpInErrors": basIcmpInErrors,
       "basIcmpInDestUnreachs": basIcmpInDestUnreachs,
       "basIcmpInTimeExcds": basIcmpInTimeExcds,
       "basIcmpInParmProbs": basIcmpInParmProbs,
       "basIcmpInSrcQuenchs": basIcmpInSrcQuenchs,
       "basIcmpInRedirects": basIcmpInRedirects,
       "basIcmpInEchos": basIcmpInEchos,
       "basIcmpInEchoReps": basIcmpInEchoReps,
       "basIcmpInTimestamps": basIcmpInTimestamps,
       "basIcmpInTimestampReps": basIcmpInTimestampReps,
       "basIcmpInAddrMasks": basIcmpInAddrMasks,
       "basIcmpInAddrMaskReps": basIcmpInAddrMaskReps,
       "basIcmpOutMsgs": basIcmpOutMsgs,
       "basIcmpOutErrors": basIcmpOutErrors,
       "basIcmpOutDestUnreachs": basIcmpOutDestUnreachs,
       "basIcmpOutTimeExcds": basIcmpOutTimeExcds,
       "basIcmpOutParmProbs": basIcmpOutParmProbs,
       "basIcmpOutSrcQuenchs": basIcmpOutSrcQuenchs,
       "basIcmpOutRedirects": basIcmpOutRedirects,
       "basIcmpOutEchos": basIcmpOutEchos,
       "basIcmpOutEchoReps": basIcmpOutEchoReps,
       "basIcmpOutTimestamps": basIcmpOutTimestamps,
       "basIcmpOutTimestampReps": basIcmpOutTimestampReps,
       "basIcmpOutAddrMasks": basIcmpOutAddrMasks,
       "basIcmpOutAddrMaskReps": basIcmpOutAddrMaskReps,
       "basIcmpChassis": basIcmpChassis,
       "basIcmpSlot": basIcmpSlot,
       "basIcmpIf": basIcmpIf,
       "basIcmpLPort": basIcmpLPort}
)
