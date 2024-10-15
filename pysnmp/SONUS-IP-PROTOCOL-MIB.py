# SNMP MIB module (SONUS-IP-PROTOCOL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SONUS-IP-PROTOCOL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:57:00 2024
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

(sonusPacketMIBs,) = mibBuilder.importSymbols(
    "SONUS-SMI",
    "sonusPacketMIBs")


# MODULE-IDENTITY

sonusIpProtocolMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SonusMib_2_ObjectIdentity = ObjectIdentity
sonusMib_2 = _SonusMib_2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2)
)
_SonusIp_ObjectIdentity = ObjectIdentity
sonusIp = _SonusIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 4)
)
_SonusIpGeneralGroupTable_Object = MibTable
sonusIpGeneralGroupTable = _SonusIpGeneralGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 4, 1)
)
if mibBuilder.loadTexts:
    sonusIpGeneralGroupTable.setStatus("current")
_SonusIpGeneralGroupEntry_Object = MibTableRow
sonusIpGeneralGroupEntry = _SonusIpGeneralGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 4, 1, 1)
)
sonusIpGeneralGroupEntry.setIndexNames(
    (0, "SONUS-IP-PROTOCOL-MIB", "sonusIpGeneralGroupShelf"),
    (0, "SONUS-IP-PROTOCOL-MIB", "sonusIpGeneralGroupSlot"),
    (0, "SONUS-IP-PROTOCOL-MIB", "sonusIpGeneralGroupInstance"),
)
if mibBuilder.loadTexts:
    sonusIpGeneralGroupEntry.setStatus("current")


class _SonusIpForwarding_Type(Integer32):
    """Custom type sonusIpForwarding based on Integer32"""
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


_SonusIpForwarding_Type.__name__ = "Integer32"
_SonusIpForwarding_Object = MibTableColumn
sonusIpForwarding = _SonusIpForwarding_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 4, 1, 1, 1),
    _SonusIpForwarding_Type()
)
sonusIpForwarding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIpForwarding.setStatus("current")


class _SonusIpDefaultTTL_Type(Integer32):
    """Custom type sonusIpDefaultTTL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SonusIpDefaultTTL_Type.__name__ = "Integer32"
_SonusIpDefaultTTL_Object = MibTableColumn
sonusIpDefaultTTL = _SonusIpDefaultTTL_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 4, 1, 1, 2),
    _SonusIpDefaultTTL_Type()
)
sonusIpDefaultTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIpDefaultTTL.setStatus("current")
_SonusIpInReceives_Type = Counter32
_SonusIpInReceives_Object = MibTableColumn
sonusIpInReceives = _SonusIpInReceives_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 4, 1, 1, 3),
    _SonusIpInReceives_Type()
)
sonusIpInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIpInReceives.setStatus("current")
_SonusIpInHdrErrors_Type = Counter32
_SonusIpInHdrErrors_Object = MibTableColumn
sonusIpInHdrErrors = _SonusIpInHdrErrors_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 4, 1, 1, 4),
    _SonusIpInHdrErrors_Type()
)
sonusIpInHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIpInHdrErrors.setStatus("current")
_SonusIpInAddrErrors_Type = Counter32
_SonusIpInAddrErrors_Object = MibTableColumn
sonusIpInAddrErrors = _SonusIpInAddrErrors_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 4, 1, 1, 5),
    _SonusIpInAddrErrors_Type()
)
sonusIpInAddrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIpInAddrErrors.setStatus("current")
_SonusIpForwDatagrams_Type = Counter32
_SonusIpForwDatagrams_Object = MibTableColumn
sonusIpForwDatagrams = _SonusIpForwDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 4, 1, 1, 6),
    _SonusIpForwDatagrams_Type()
)
sonusIpForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIpForwDatagrams.setStatus("current")
_SonusIpInUnknownProtos_Type = Counter32
_SonusIpInUnknownProtos_Object = MibTableColumn
sonusIpInUnknownProtos = _SonusIpInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 4, 1, 1, 7),
    _SonusIpInUnknownProtos_Type()
)
sonusIpInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIpInUnknownProtos.setStatus("current")
_SonusIpInDiscards_Type = Counter32
_SonusIpInDiscards_Object = MibTableColumn
sonusIpInDiscards = _SonusIpInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 4, 1, 1, 8),
    _SonusIpInDiscards_Type()
)
sonusIpInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIpInDiscards.setStatus("current")
_SonusIpInDelivers_Type = Counter32
_SonusIpInDelivers_Object = MibTableColumn
sonusIpInDelivers = _SonusIpInDelivers_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 4, 1, 1, 9),
    _SonusIpInDelivers_Type()
)
sonusIpInDelivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIpInDelivers.setStatus("current")
_SonusIpOutRequests_Type = Counter32
_SonusIpOutRequests_Object = MibTableColumn
sonusIpOutRequests = _SonusIpOutRequests_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 4, 1, 1, 10),
    _SonusIpOutRequests_Type()
)
sonusIpOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIpOutRequests.setStatus("current")
_SonusIpOutDiscards_Type = Counter32
_SonusIpOutDiscards_Object = MibTableColumn
sonusIpOutDiscards = _SonusIpOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 4, 1, 1, 11),
    _SonusIpOutDiscards_Type()
)
sonusIpOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIpOutDiscards.setStatus("current")
_SonusIpOutNoRoutes_Type = Counter32
_SonusIpOutNoRoutes_Object = MibTableColumn
sonusIpOutNoRoutes = _SonusIpOutNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 4, 1, 1, 12),
    _SonusIpOutNoRoutes_Type()
)
sonusIpOutNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIpOutNoRoutes.setStatus("current")
_SonusIpReasmTimeout_Type = Integer32
_SonusIpReasmTimeout_Object = MibTableColumn
sonusIpReasmTimeout = _SonusIpReasmTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 4, 1, 1, 13),
    _SonusIpReasmTimeout_Type()
)
sonusIpReasmTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIpReasmTimeout.setStatus("current")
_SonusIpReasmReqds_Type = Counter32
_SonusIpReasmReqds_Object = MibTableColumn
sonusIpReasmReqds = _SonusIpReasmReqds_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 4, 1, 1, 14),
    _SonusIpReasmReqds_Type()
)
sonusIpReasmReqds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIpReasmReqds.setStatus("current")
_SonusIpReasmOKs_Type = Counter32
_SonusIpReasmOKs_Object = MibTableColumn
sonusIpReasmOKs = _SonusIpReasmOKs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 4, 1, 1, 15),
    _SonusIpReasmOKs_Type()
)
sonusIpReasmOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIpReasmOKs.setStatus("current")
_SonusIpReasmFails_Type = Counter32
_SonusIpReasmFails_Object = MibTableColumn
sonusIpReasmFails = _SonusIpReasmFails_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 4, 1, 1, 16),
    _SonusIpReasmFails_Type()
)
sonusIpReasmFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIpReasmFails.setStatus("current")
_SonusIpFragOKs_Type = Counter32
_SonusIpFragOKs_Object = MibTableColumn
sonusIpFragOKs = _SonusIpFragOKs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 4, 1, 1, 17),
    _SonusIpFragOKs_Type()
)
sonusIpFragOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIpFragOKs.setStatus("current")
_SonusIpFragFails_Type = Counter32
_SonusIpFragFails_Object = MibTableColumn
sonusIpFragFails = _SonusIpFragFails_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 4, 1, 1, 18),
    _SonusIpFragFails_Type()
)
sonusIpFragFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIpFragFails.setStatus("current")
_SonusIpFragCreates_Type = Counter32
_SonusIpFragCreates_Object = MibTableColumn
sonusIpFragCreates = _SonusIpFragCreates_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 4, 1, 1, 19),
    _SonusIpFragCreates_Type()
)
sonusIpFragCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIpFragCreates.setStatus("current")
_SonusIpRoutingDiscards_Type = Counter32
_SonusIpRoutingDiscards_Object = MibTableColumn
sonusIpRoutingDiscards = _SonusIpRoutingDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 4, 1, 1, 23),
    _SonusIpRoutingDiscards_Type()
)
sonusIpRoutingDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIpRoutingDiscards.setStatus("current")
_SonusIpGeneralGroupShelf_Type = Integer32
_SonusIpGeneralGroupShelf_Object = MibTableColumn
sonusIpGeneralGroupShelf = _SonusIpGeneralGroupShelf_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 4, 1, 1, 24),
    _SonusIpGeneralGroupShelf_Type()
)
sonusIpGeneralGroupShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIpGeneralGroupShelf.setStatus("current")
_SonusIpGeneralGroupSlot_Type = Integer32
_SonusIpGeneralGroupSlot_Object = MibTableColumn
sonusIpGeneralGroupSlot = _SonusIpGeneralGroupSlot_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 4, 1, 1, 25),
    _SonusIpGeneralGroupSlot_Type()
)
sonusIpGeneralGroupSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIpGeneralGroupSlot.setStatus("current")
_SonusIpGeneralGroupInstance_Type = Integer32
_SonusIpGeneralGroupInstance_Object = MibTableColumn
sonusIpGeneralGroupInstance = _SonusIpGeneralGroupInstance_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 4, 1, 1, 26),
    _SonusIpGeneralGroupInstance_Type()
)
sonusIpGeneralGroupInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIpGeneralGroupInstance.setStatus("current")
_SonusIcmp_ObjectIdentity = ObjectIdentity
sonusIcmp = _SonusIcmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 5)
)
_SonusIcmpGeneralGroupTable_Object = MibTable
sonusIcmpGeneralGroupTable = _SonusIcmpGeneralGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 5, 1)
)
if mibBuilder.loadTexts:
    sonusIcmpGeneralGroupTable.setStatus("current")
_SonusIcmpGeneralGroupEntry_Object = MibTableRow
sonusIcmpGeneralGroupEntry = _SonusIcmpGeneralGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 5, 1, 1)
)
sonusIcmpGeneralGroupEntry.setIndexNames(
    (0, "SONUS-IP-PROTOCOL-MIB", "sonusIcmpGeneralGroupShelf"),
    (0, "SONUS-IP-PROTOCOL-MIB", "sonusIcmpGeneralGroupSlot"),
    (0, "SONUS-IP-PROTOCOL-MIB", "sonusIcmpGeneralGroupInstance"),
)
if mibBuilder.loadTexts:
    sonusIcmpGeneralGroupEntry.setStatus("current")
_SonusIcmpInMsgs_Type = Counter32
_SonusIcmpInMsgs_Object = MibTableColumn
sonusIcmpInMsgs = _SonusIcmpInMsgs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 5, 1, 1, 1),
    _SonusIcmpInMsgs_Type()
)
sonusIcmpInMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIcmpInMsgs.setStatus("current")
_SonusIcmpInErrors_Type = Counter32
_SonusIcmpInErrors_Object = MibTableColumn
sonusIcmpInErrors = _SonusIcmpInErrors_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 5, 1, 1, 2),
    _SonusIcmpInErrors_Type()
)
sonusIcmpInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIcmpInErrors.setStatus("current")
_SonusIcmpInDestUnreachs_Type = Counter32
_SonusIcmpInDestUnreachs_Object = MibTableColumn
sonusIcmpInDestUnreachs = _SonusIcmpInDestUnreachs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 5, 1, 1, 3),
    _SonusIcmpInDestUnreachs_Type()
)
sonusIcmpInDestUnreachs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIcmpInDestUnreachs.setStatus("current")
_SonusIcmpInTimeExcds_Type = Counter32
_SonusIcmpInTimeExcds_Object = MibTableColumn
sonusIcmpInTimeExcds = _SonusIcmpInTimeExcds_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 5, 1, 1, 4),
    _SonusIcmpInTimeExcds_Type()
)
sonusIcmpInTimeExcds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIcmpInTimeExcds.setStatus("current")
_SonusIcmpInParmProbs_Type = Counter32
_SonusIcmpInParmProbs_Object = MibTableColumn
sonusIcmpInParmProbs = _SonusIcmpInParmProbs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 5, 1, 1, 5),
    _SonusIcmpInParmProbs_Type()
)
sonusIcmpInParmProbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIcmpInParmProbs.setStatus("current")
_SonusIcmpInSrcQuenchs_Type = Counter32
_SonusIcmpInSrcQuenchs_Object = MibTableColumn
sonusIcmpInSrcQuenchs = _SonusIcmpInSrcQuenchs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 5, 1, 1, 6),
    _SonusIcmpInSrcQuenchs_Type()
)
sonusIcmpInSrcQuenchs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIcmpInSrcQuenchs.setStatus("current")
_SonusIcmpInRedirects_Type = Counter32
_SonusIcmpInRedirects_Object = MibTableColumn
sonusIcmpInRedirects = _SonusIcmpInRedirects_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 5, 1, 1, 7),
    _SonusIcmpInRedirects_Type()
)
sonusIcmpInRedirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIcmpInRedirects.setStatus("current")
_SonusIcmpInEchos_Type = Counter32
_SonusIcmpInEchos_Object = MibTableColumn
sonusIcmpInEchos = _SonusIcmpInEchos_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 5, 1, 1, 8),
    _SonusIcmpInEchos_Type()
)
sonusIcmpInEchos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIcmpInEchos.setStatus("current")
_SonusIcmpInEchoReps_Type = Counter32
_SonusIcmpInEchoReps_Object = MibTableColumn
sonusIcmpInEchoReps = _SonusIcmpInEchoReps_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 5, 1, 1, 9),
    _SonusIcmpInEchoReps_Type()
)
sonusIcmpInEchoReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIcmpInEchoReps.setStatus("current")
_SonusIcmpInTimestamps_Type = Counter32
_SonusIcmpInTimestamps_Object = MibTableColumn
sonusIcmpInTimestamps = _SonusIcmpInTimestamps_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 5, 1, 1, 10),
    _SonusIcmpInTimestamps_Type()
)
sonusIcmpInTimestamps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIcmpInTimestamps.setStatus("current")
_SonusIcmpInTimestampReps_Type = Counter32
_SonusIcmpInTimestampReps_Object = MibTableColumn
sonusIcmpInTimestampReps = _SonusIcmpInTimestampReps_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 5, 1, 1, 11),
    _SonusIcmpInTimestampReps_Type()
)
sonusIcmpInTimestampReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIcmpInTimestampReps.setStatus("current")
_SonusIcmpInAddrMasks_Type = Counter32
_SonusIcmpInAddrMasks_Object = MibTableColumn
sonusIcmpInAddrMasks = _SonusIcmpInAddrMasks_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 5, 1, 1, 12),
    _SonusIcmpInAddrMasks_Type()
)
sonusIcmpInAddrMasks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIcmpInAddrMasks.setStatus("current")
_SonusIcmpInAddrMaskReps_Type = Counter32
_SonusIcmpInAddrMaskReps_Object = MibTableColumn
sonusIcmpInAddrMaskReps = _SonusIcmpInAddrMaskReps_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 5, 1, 1, 13),
    _SonusIcmpInAddrMaskReps_Type()
)
sonusIcmpInAddrMaskReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIcmpInAddrMaskReps.setStatus("current")
_SonusIcmpOutMsgs_Type = Counter32
_SonusIcmpOutMsgs_Object = MibTableColumn
sonusIcmpOutMsgs = _SonusIcmpOutMsgs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 5, 1, 1, 14),
    _SonusIcmpOutMsgs_Type()
)
sonusIcmpOutMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIcmpOutMsgs.setStatus("current")
_SonusIcmpOutErrors_Type = Counter32
_SonusIcmpOutErrors_Object = MibTableColumn
sonusIcmpOutErrors = _SonusIcmpOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 5, 1, 1, 15),
    _SonusIcmpOutErrors_Type()
)
sonusIcmpOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIcmpOutErrors.setStatus("current")
_SonusIcmpOutDestUnreachs_Type = Counter32
_SonusIcmpOutDestUnreachs_Object = MibTableColumn
sonusIcmpOutDestUnreachs = _SonusIcmpOutDestUnreachs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 5, 1, 1, 16),
    _SonusIcmpOutDestUnreachs_Type()
)
sonusIcmpOutDestUnreachs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIcmpOutDestUnreachs.setStatus("current")
_SonusIcmpOutTimeExcds_Type = Counter32
_SonusIcmpOutTimeExcds_Object = MibTableColumn
sonusIcmpOutTimeExcds = _SonusIcmpOutTimeExcds_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 5, 1, 1, 17),
    _SonusIcmpOutTimeExcds_Type()
)
sonusIcmpOutTimeExcds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIcmpOutTimeExcds.setStatus("current")
_SonusIcmpOutParmProbs_Type = Counter32
_SonusIcmpOutParmProbs_Object = MibTableColumn
sonusIcmpOutParmProbs = _SonusIcmpOutParmProbs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 5, 1, 1, 18),
    _SonusIcmpOutParmProbs_Type()
)
sonusIcmpOutParmProbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIcmpOutParmProbs.setStatus("current")
_SonusIcmpOutSrcQuenchs_Type = Counter32
_SonusIcmpOutSrcQuenchs_Object = MibTableColumn
sonusIcmpOutSrcQuenchs = _SonusIcmpOutSrcQuenchs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 5, 1, 1, 19),
    _SonusIcmpOutSrcQuenchs_Type()
)
sonusIcmpOutSrcQuenchs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIcmpOutSrcQuenchs.setStatus("current")
_SonusIcmpOutRedirects_Type = Counter32
_SonusIcmpOutRedirects_Object = MibTableColumn
sonusIcmpOutRedirects = _SonusIcmpOutRedirects_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 5, 1, 1, 20),
    _SonusIcmpOutRedirects_Type()
)
sonusIcmpOutRedirects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIcmpOutRedirects.setStatus("current")
_SonusIcmpOutEchos_Type = Counter32
_SonusIcmpOutEchos_Object = MibTableColumn
sonusIcmpOutEchos = _SonusIcmpOutEchos_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 5, 1, 1, 21),
    _SonusIcmpOutEchos_Type()
)
sonusIcmpOutEchos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIcmpOutEchos.setStatus("current")
_SonusIcmpOutEchoReps_Type = Counter32
_SonusIcmpOutEchoReps_Object = MibTableColumn
sonusIcmpOutEchoReps = _SonusIcmpOutEchoReps_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 5, 1, 1, 22),
    _SonusIcmpOutEchoReps_Type()
)
sonusIcmpOutEchoReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIcmpOutEchoReps.setStatus("current")
_SonusIcmpOutTimestamps_Type = Counter32
_SonusIcmpOutTimestamps_Object = MibTableColumn
sonusIcmpOutTimestamps = _SonusIcmpOutTimestamps_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 5, 1, 1, 23),
    _SonusIcmpOutTimestamps_Type()
)
sonusIcmpOutTimestamps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIcmpOutTimestamps.setStatus("current")
_SonusIcmpOutTimestampReps_Type = Counter32
_SonusIcmpOutTimestampReps_Object = MibTableColumn
sonusIcmpOutTimestampReps = _SonusIcmpOutTimestampReps_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 5, 1, 1, 24),
    _SonusIcmpOutTimestampReps_Type()
)
sonusIcmpOutTimestampReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIcmpOutTimestampReps.setStatus("current")
_SonusIcmpOutAddrMasks_Type = Counter32
_SonusIcmpOutAddrMasks_Object = MibTableColumn
sonusIcmpOutAddrMasks = _SonusIcmpOutAddrMasks_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 5, 1, 1, 25),
    _SonusIcmpOutAddrMasks_Type()
)
sonusIcmpOutAddrMasks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIcmpOutAddrMasks.setStatus("current")
_SonusIcmpOutAddrMaskReps_Type = Counter32
_SonusIcmpOutAddrMaskReps_Object = MibTableColumn
sonusIcmpOutAddrMaskReps = _SonusIcmpOutAddrMaskReps_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 5, 1, 1, 26),
    _SonusIcmpOutAddrMaskReps_Type()
)
sonusIcmpOutAddrMaskReps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIcmpOutAddrMaskReps.setStatus("current")
_SonusIcmpGeneralGroupShelf_Type = Integer32
_SonusIcmpGeneralGroupShelf_Object = MibTableColumn
sonusIcmpGeneralGroupShelf = _SonusIcmpGeneralGroupShelf_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 5, 1, 1, 27),
    _SonusIcmpGeneralGroupShelf_Type()
)
sonusIcmpGeneralGroupShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIcmpGeneralGroupShelf.setStatus("current")
_SonusIcmpGeneralGroupSlot_Type = Integer32
_SonusIcmpGeneralGroupSlot_Object = MibTableColumn
sonusIcmpGeneralGroupSlot = _SonusIcmpGeneralGroupSlot_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 5, 1, 1, 28),
    _SonusIcmpGeneralGroupSlot_Type()
)
sonusIcmpGeneralGroupSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIcmpGeneralGroupSlot.setStatus("current")
_SonusIcmpGeneralGroupInstance_Type = Integer32
_SonusIcmpGeneralGroupInstance_Object = MibTableColumn
sonusIcmpGeneralGroupInstance = _SonusIcmpGeneralGroupInstance_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 5, 1, 1, 29),
    _SonusIcmpGeneralGroupInstance_Type()
)
sonusIcmpGeneralGroupInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusIcmpGeneralGroupInstance.setStatus("current")
_SonusTcp_ObjectIdentity = ObjectIdentity
sonusTcp = _SonusTcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 6)
)
_SonusTcpGeneralGroupTable_Object = MibTable
sonusTcpGeneralGroupTable = _SonusTcpGeneralGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 6, 1)
)
if mibBuilder.loadTexts:
    sonusTcpGeneralGroupTable.setStatus("current")
_SonusTcpGeneralGroupEntry_Object = MibTableRow
sonusTcpGeneralGroupEntry = _SonusTcpGeneralGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 6, 1, 1)
)
sonusTcpGeneralGroupEntry.setIndexNames(
    (0, "SONUS-IP-PROTOCOL-MIB", "sonusTcpGeneralGroupShelf"),
    (0, "SONUS-IP-PROTOCOL-MIB", "sonusTcpGeneralGroupSlot"),
    (0, "SONUS-IP-PROTOCOL-MIB", "sonusTcpGeneralGroupInstance"),
)
if mibBuilder.loadTexts:
    sonusTcpGeneralGroupEntry.setStatus("current")


class _SonusTcpRtoAlgorithm_Type(Integer32):
    """Custom type sonusTcpRtoAlgorithm based on Integer32"""
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
        *(("constant", 2),
          ("other", 1),
          ("rsre", 3),
          ("vanj", 4))
    )


_SonusTcpRtoAlgorithm_Type.__name__ = "Integer32"
_SonusTcpRtoAlgorithm_Object = MibTableColumn
sonusTcpRtoAlgorithm = _SonusTcpRtoAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 6, 1, 1, 1),
    _SonusTcpRtoAlgorithm_Type()
)
sonusTcpRtoAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTcpRtoAlgorithm.setStatus("current")
_SonusTcpRtoMin_Type = Integer32
_SonusTcpRtoMin_Object = MibTableColumn
sonusTcpRtoMin = _SonusTcpRtoMin_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 6, 1, 1, 2),
    _SonusTcpRtoMin_Type()
)
sonusTcpRtoMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTcpRtoMin.setStatus("current")
_SonusTcpRtoMax_Type = Integer32
_SonusTcpRtoMax_Object = MibTableColumn
sonusTcpRtoMax = _SonusTcpRtoMax_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 6, 1, 1, 3),
    _SonusTcpRtoMax_Type()
)
sonusTcpRtoMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTcpRtoMax.setStatus("current")
_SonusTcpMaxConn_Type = Integer32
_SonusTcpMaxConn_Object = MibTableColumn
sonusTcpMaxConn = _SonusTcpMaxConn_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 6, 1, 1, 4),
    _SonusTcpMaxConn_Type()
)
sonusTcpMaxConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTcpMaxConn.setStatus("current")
_SonusTcpActiveOpens_Type = Counter32
_SonusTcpActiveOpens_Object = MibTableColumn
sonusTcpActiveOpens = _SonusTcpActiveOpens_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 6, 1, 1, 5),
    _SonusTcpActiveOpens_Type()
)
sonusTcpActiveOpens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTcpActiveOpens.setStatus("current")
_SonusTcpPassiveOpens_Type = Counter32
_SonusTcpPassiveOpens_Object = MibTableColumn
sonusTcpPassiveOpens = _SonusTcpPassiveOpens_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 6, 1, 1, 6),
    _SonusTcpPassiveOpens_Type()
)
sonusTcpPassiveOpens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTcpPassiveOpens.setStatus("current")
_SonusTcpAttemptFails_Type = Counter32
_SonusTcpAttemptFails_Object = MibTableColumn
sonusTcpAttemptFails = _SonusTcpAttemptFails_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 6, 1, 1, 7),
    _SonusTcpAttemptFails_Type()
)
sonusTcpAttemptFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTcpAttemptFails.setStatus("current")
_SonusTcpEstabResets_Type = Counter32
_SonusTcpEstabResets_Object = MibTableColumn
sonusTcpEstabResets = _SonusTcpEstabResets_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 6, 1, 1, 8),
    _SonusTcpEstabResets_Type()
)
sonusTcpEstabResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTcpEstabResets.setStatus("current")
_SonusTcpCurrEstab_Type = Gauge32
_SonusTcpCurrEstab_Object = MibTableColumn
sonusTcpCurrEstab = _SonusTcpCurrEstab_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 6, 1, 1, 9),
    _SonusTcpCurrEstab_Type()
)
sonusTcpCurrEstab.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTcpCurrEstab.setStatus("current")
_SonusTcpInSegs_Type = Counter32
_SonusTcpInSegs_Object = MibTableColumn
sonusTcpInSegs = _SonusTcpInSegs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 6, 1, 1, 10),
    _SonusTcpInSegs_Type()
)
sonusTcpInSegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTcpInSegs.setStatus("current")
_SonusTcpOutSegs_Type = Counter32
_SonusTcpOutSegs_Object = MibTableColumn
sonusTcpOutSegs = _SonusTcpOutSegs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 6, 1, 1, 11),
    _SonusTcpOutSegs_Type()
)
sonusTcpOutSegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTcpOutSegs.setStatus("current")
_SonusTcpRetransSegs_Type = Counter32
_SonusTcpRetransSegs_Object = MibTableColumn
sonusTcpRetransSegs = _SonusTcpRetransSegs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 6, 1, 1, 12),
    _SonusTcpRetransSegs_Type()
)
sonusTcpRetransSegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTcpRetransSegs.setStatus("current")
_SonusTcpInErrs_Type = Counter32
_SonusTcpInErrs_Object = MibTableColumn
sonusTcpInErrs = _SonusTcpInErrs_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 6, 1, 1, 14),
    _SonusTcpInErrs_Type()
)
sonusTcpInErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTcpInErrs.setStatus("current")
_SonusTcpOutRsts_Type = Counter32
_SonusTcpOutRsts_Object = MibTableColumn
sonusTcpOutRsts = _SonusTcpOutRsts_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 6, 1, 1, 15),
    _SonusTcpOutRsts_Type()
)
sonusTcpOutRsts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTcpOutRsts.setStatus("current")
_SonusTcpGeneralGroupShelf_Type = Integer32
_SonusTcpGeneralGroupShelf_Object = MibTableColumn
sonusTcpGeneralGroupShelf = _SonusTcpGeneralGroupShelf_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 6, 1, 1, 16),
    _SonusTcpGeneralGroupShelf_Type()
)
sonusTcpGeneralGroupShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTcpGeneralGroupShelf.setStatus("current")
_SonusTcpGeneralGroupSlot_Type = Integer32
_SonusTcpGeneralGroupSlot_Object = MibTableColumn
sonusTcpGeneralGroupSlot = _SonusTcpGeneralGroupSlot_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 6, 1, 1, 17),
    _SonusTcpGeneralGroupSlot_Type()
)
sonusTcpGeneralGroupSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTcpGeneralGroupSlot.setStatus("current")
_SonusTcpGeneralGroupInstance_Type = Integer32
_SonusTcpGeneralGroupInstance_Object = MibTableColumn
sonusTcpGeneralGroupInstance = _SonusTcpGeneralGroupInstance_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 6, 1, 1, 18),
    _SonusTcpGeneralGroupInstance_Type()
)
sonusTcpGeneralGroupInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTcpGeneralGroupInstance.setStatus("current")
_SonusTcpConnTable_Object = MibTable
sonusTcpConnTable = _SonusTcpConnTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 6, 13)
)
if mibBuilder.loadTexts:
    sonusTcpConnTable.setStatus("current")
_SonusTcpConnEntry_Object = MibTableRow
sonusTcpConnEntry = _SonusTcpConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 6, 13, 1)
)
sonusTcpConnEntry.setIndexNames(
    (0, "SONUS-IP-PROTOCOL-MIB", "sonusTcpConnShelf"),
    (0, "SONUS-IP-PROTOCOL-MIB", "sonusTcpConnSlot"),
    (0, "SONUS-IP-PROTOCOL-MIB", "sonusTcpConnInstance"),
    (0, "SONUS-IP-PROTOCOL-MIB", "sonusTcpConnLocalAddress"),
    (0, "SONUS-IP-PROTOCOL-MIB", "sonusTcpConnLocalPort"),
    (0, "SONUS-IP-PROTOCOL-MIB", "sonusTcpConnRemAddress"),
    (0, "SONUS-IP-PROTOCOL-MIB", "sonusTcpConnRemPort"),
)
if mibBuilder.loadTexts:
    sonusTcpConnEntry.setStatus("current")


class _SonusTcpConnState_Type(Integer32):
    """Custom type sonusTcpConnState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("closeWait", 8),
          ("closed", 1),
          ("closing", 10),
          ("deleteTCB", 12),
          ("established", 5),
          ("finWait1", 6),
          ("finWait2", 7),
          ("lastAck", 9),
          ("listen", 2),
          ("synReceived", 4),
          ("synSent", 3),
          ("timeWait", 11))
    )


_SonusTcpConnState_Type.__name__ = "Integer32"
_SonusTcpConnState_Object = MibTableColumn
sonusTcpConnState = _SonusTcpConnState_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 6, 13, 1, 1),
    _SonusTcpConnState_Type()
)
sonusTcpConnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTcpConnState.setStatus("current")
_SonusTcpConnLocalAddress_Type = IpAddress
_SonusTcpConnLocalAddress_Object = MibTableColumn
sonusTcpConnLocalAddress = _SonusTcpConnLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 6, 13, 1, 2),
    _SonusTcpConnLocalAddress_Type()
)
sonusTcpConnLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTcpConnLocalAddress.setStatus("current")


class _SonusTcpConnLocalPort_Type(Integer32):
    """Custom type sonusTcpConnLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SonusTcpConnLocalPort_Type.__name__ = "Integer32"
_SonusTcpConnLocalPort_Object = MibTableColumn
sonusTcpConnLocalPort = _SonusTcpConnLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 6, 13, 1, 3),
    _SonusTcpConnLocalPort_Type()
)
sonusTcpConnLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTcpConnLocalPort.setStatus("current")
_SonusTcpConnRemAddress_Type = IpAddress
_SonusTcpConnRemAddress_Object = MibTableColumn
sonusTcpConnRemAddress = _SonusTcpConnRemAddress_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 6, 13, 1, 4),
    _SonusTcpConnRemAddress_Type()
)
sonusTcpConnRemAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTcpConnRemAddress.setStatus("current")


class _SonusTcpConnRemPort_Type(Integer32):
    """Custom type sonusTcpConnRemPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SonusTcpConnRemPort_Type.__name__ = "Integer32"
_SonusTcpConnRemPort_Object = MibTableColumn
sonusTcpConnRemPort = _SonusTcpConnRemPort_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 6, 13, 1, 5),
    _SonusTcpConnRemPort_Type()
)
sonusTcpConnRemPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTcpConnRemPort.setStatus("current")
_SonusTcpConnShelf_Type = Integer32
_SonusTcpConnShelf_Object = MibTableColumn
sonusTcpConnShelf = _SonusTcpConnShelf_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 6, 13, 1, 6),
    _SonusTcpConnShelf_Type()
)
sonusTcpConnShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTcpConnShelf.setStatus("current")
_SonusTcpConnSlot_Type = Integer32
_SonusTcpConnSlot_Object = MibTableColumn
sonusTcpConnSlot = _SonusTcpConnSlot_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 6, 13, 1, 7),
    _SonusTcpConnSlot_Type()
)
sonusTcpConnSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTcpConnSlot.setStatus("current")
_SonusTcpConnInstance_Type = Integer32
_SonusTcpConnInstance_Object = MibTableColumn
sonusTcpConnInstance = _SonusTcpConnInstance_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 6, 13, 1, 8),
    _SonusTcpConnInstance_Type()
)
sonusTcpConnInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusTcpConnInstance.setStatus("current")
_SonusUdp_ObjectIdentity = ObjectIdentity
sonusUdp = _SonusUdp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 7)
)
_SonusUdpGeneralGroupTable_Object = MibTable
sonusUdpGeneralGroupTable = _SonusUdpGeneralGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 7, 1)
)
if mibBuilder.loadTexts:
    sonusUdpGeneralGroupTable.setStatus("current")
_SonusUdpGeneralGroupEntry_Object = MibTableRow
sonusUdpGeneralGroupEntry = _SonusUdpGeneralGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 7, 1, 1)
)
sonusUdpGeneralGroupEntry.setIndexNames(
    (0, "SONUS-IP-PROTOCOL-MIB", "sonusUdpGeneralGroupShelf"),
    (0, "SONUS-IP-PROTOCOL-MIB", "sonusUdpGeneralGroupSlot"),
    (0, "SONUS-IP-PROTOCOL-MIB", "sonusUdpGeneralGroupInstance"),
)
if mibBuilder.loadTexts:
    sonusUdpGeneralGroupEntry.setStatus("current")
_SonusUdpInDatagrams_Type = Counter32
_SonusUdpInDatagrams_Object = MibTableColumn
sonusUdpInDatagrams = _SonusUdpInDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 7, 1, 1, 1),
    _SonusUdpInDatagrams_Type()
)
sonusUdpInDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusUdpInDatagrams.setStatus("current")
_SonusUdpNoPorts_Type = Counter32
_SonusUdpNoPorts_Object = MibTableColumn
sonusUdpNoPorts = _SonusUdpNoPorts_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 7, 1, 1, 2),
    _SonusUdpNoPorts_Type()
)
sonusUdpNoPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusUdpNoPorts.setStatus("current")
_SonusUdpInErrors_Type = Counter32
_SonusUdpInErrors_Object = MibTableColumn
sonusUdpInErrors = _SonusUdpInErrors_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 7, 1, 1, 3),
    _SonusUdpInErrors_Type()
)
sonusUdpInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusUdpInErrors.setStatus("current")
_SonusUdpOutDatagrams_Type = Counter32
_SonusUdpOutDatagrams_Object = MibTableColumn
sonusUdpOutDatagrams = _SonusUdpOutDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 7, 1, 1, 4),
    _SonusUdpOutDatagrams_Type()
)
sonusUdpOutDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusUdpOutDatagrams.setStatus("current")
_SonusUdpGeneralGroupShelf_Type = Integer32
_SonusUdpGeneralGroupShelf_Object = MibTableColumn
sonusUdpGeneralGroupShelf = _SonusUdpGeneralGroupShelf_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 7, 1, 1, 5),
    _SonusUdpGeneralGroupShelf_Type()
)
sonusUdpGeneralGroupShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusUdpGeneralGroupShelf.setStatus("current")
_SonusUdpGeneralGroupSlot_Type = Integer32
_SonusUdpGeneralGroupSlot_Object = MibTableColumn
sonusUdpGeneralGroupSlot = _SonusUdpGeneralGroupSlot_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 7, 1, 1, 6),
    _SonusUdpGeneralGroupSlot_Type()
)
sonusUdpGeneralGroupSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusUdpGeneralGroupSlot.setStatus("current")
_SonusUdpGeneralGroupInstance_Type = Integer32
_SonusUdpGeneralGroupInstance_Object = MibTableColumn
sonusUdpGeneralGroupInstance = _SonusUdpGeneralGroupInstance_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 7, 1, 1, 7),
    _SonusUdpGeneralGroupInstance_Type()
)
sonusUdpGeneralGroupInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusUdpGeneralGroupInstance.setStatus("current")
_SonusUdpTable_Object = MibTable
sonusUdpTable = _SonusUdpTable_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 7, 5)
)
if mibBuilder.loadTexts:
    sonusUdpTable.setStatus("current")
_SonusUdpEntry_Object = MibTableRow
sonusUdpEntry = _SonusUdpEntry_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 7, 5, 1)
)
sonusUdpEntry.setIndexNames(
    (0, "SONUS-IP-PROTOCOL-MIB", "sonusUdpShelf"),
    (0, "SONUS-IP-PROTOCOL-MIB", "sonusUdpSlot"),
    (0, "SONUS-IP-PROTOCOL-MIB", "sonusUdpInstance"),
    (0, "SONUS-IP-PROTOCOL-MIB", "sonusUdpLocalAddress"),
    (0, "SONUS-IP-PROTOCOL-MIB", "sonusUdpLocalPort"),
)
if mibBuilder.loadTexts:
    sonusUdpEntry.setStatus("current")
_SonusUdpLocalAddress_Type = IpAddress
_SonusUdpLocalAddress_Object = MibTableColumn
sonusUdpLocalAddress = _SonusUdpLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 7, 5, 1, 1),
    _SonusUdpLocalAddress_Type()
)
sonusUdpLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusUdpLocalAddress.setStatus("current")


class _SonusUdpLocalPort_Type(Integer32):
    """Custom type sonusUdpLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SonusUdpLocalPort_Type.__name__ = "Integer32"
_SonusUdpLocalPort_Object = MibTableColumn
sonusUdpLocalPort = _SonusUdpLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 7, 5, 1, 2),
    _SonusUdpLocalPort_Type()
)
sonusUdpLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusUdpLocalPort.setStatus("current")
_SonusUdpShelf_Type = Integer32
_SonusUdpShelf_Object = MibTableColumn
sonusUdpShelf = _SonusUdpShelf_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 7, 5, 1, 3),
    _SonusUdpShelf_Type()
)
sonusUdpShelf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusUdpShelf.setStatus("current")
_SonusUdpSlot_Type = Integer32
_SonusUdpSlot_Object = MibTableColumn
sonusUdpSlot = _SonusUdpSlot_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 7, 5, 1, 4),
    _SonusUdpSlot_Type()
)
sonusUdpSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusUdpSlot.setStatus("current")
_SonusUdpInstance_Type = Integer32
_SonusUdpInstance_Object = MibTableColumn
sonusUdpInstance = _SonusUdpInstance_Object(
    (1, 3, 6, 1, 4, 1, 2879, 2, 3, 4, 2, 7, 5, 1, 5),
    _SonusUdpInstance_Type()
)
sonusUdpInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonusUdpInstance.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SONUS-IP-PROTOCOL-MIB",
    **{"sonusIpProtocolMIB": sonusIpProtocolMIB,
       "sonusMib-2": sonusMib_2,
       "sonusIp": sonusIp,
       "sonusIpGeneralGroupTable": sonusIpGeneralGroupTable,
       "sonusIpGeneralGroupEntry": sonusIpGeneralGroupEntry,
       "sonusIpForwarding": sonusIpForwarding,
       "sonusIpDefaultTTL": sonusIpDefaultTTL,
       "sonusIpInReceives": sonusIpInReceives,
       "sonusIpInHdrErrors": sonusIpInHdrErrors,
       "sonusIpInAddrErrors": sonusIpInAddrErrors,
       "sonusIpForwDatagrams": sonusIpForwDatagrams,
       "sonusIpInUnknownProtos": sonusIpInUnknownProtos,
       "sonusIpInDiscards": sonusIpInDiscards,
       "sonusIpInDelivers": sonusIpInDelivers,
       "sonusIpOutRequests": sonusIpOutRequests,
       "sonusIpOutDiscards": sonusIpOutDiscards,
       "sonusIpOutNoRoutes": sonusIpOutNoRoutes,
       "sonusIpReasmTimeout": sonusIpReasmTimeout,
       "sonusIpReasmReqds": sonusIpReasmReqds,
       "sonusIpReasmOKs": sonusIpReasmOKs,
       "sonusIpReasmFails": sonusIpReasmFails,
       "sonusIpFragOKs": sonusIpFragOKs,
       "sonusIpFragFails": sonusIpFragFails,
       "sonusIpFragCreates": sonusIpFragCreates,
       "sonusIpRoutingDiscards": sonusIpRoutingDiscards,
       "sonusIpGeneralGroupShelf": sonusIpGeneralGroupShelf,
       "sonusIpGeneralGroupSlot": sonusIpGeneralGroupSlot,
       "sonusIpGeneralGroupInstance": sonusIpGeneralGroupInstance,
       "sonusIcmp": sonusIcmp,
       "sonusIcmpGeneralGroupTable": sonusIcmpGeneralGroupTable,
       "sonusIcmpGeneralGroupEntry": sonusIcmpGeneralGroupEntry,
       "sonusIcmpInMsgs": sonusIcmpInMsgs,
       "sonusIcmpInErrors": sonusIcmpInErrors,
       "sonusIcmpInDestUnreachs": sonusIcmpInDestUnreachs,
       "sonusIcmpInTimeExcds": sonusIcmpInTimeExcds,
       "sonusIcmpInParmProbs": sonusIcmpInParmProbs,
       "sonusIcmpInSrcQuenchs": sonusIcmpInSrcQuenchs,
       "sonusIcmpInRedirects": sonusIcmpInRedirects,
       "sonusIcmpInEchos": sonusIcmpInEchos,
       "sonusIcmpInEchoReps": sonusIcmpInEchoReps,
       "sonusIcmpInTimestamps": sonusIcmpInTimestamps,
       "sonusIcmpInTimestampReps": sonusIcmpInTimestampReps,
       "sonusIcmpInAddrMasks": sonusIcmpInAddrMasks,
       "sonusIcmpInAddrMaskReps": sonusIcmpInAddrMaskReps,
       "sonusIcmpOutMsgs": sonusIcmpOutMsgs,
       "sonusIcmpOutErrors": sonusIcmpOutErrors,
       "sonusIcmpOutDestUnreachs": sonusIcmpOutDestUnreachs,
       "sonusIcmpOutTimeExcds": sonusIcmpOutTimeExcds,
       "sonusIcmpOutParmProbs": sonusIcmpOutParmProbs,
       "sonusIcmpOutSrcQuenchs": sonusIcmpOutSrcQuenchs,
       "sonusIcmpOutRedirects": sonusIcmpOutRedirects,
       "sonusIcmpOutEchos": sonusIcmpOutEchos,
       "sonusIcmpOutEchoReps": sonusIcmpOutEchoReps,
       "sonusIcmpOutTimestamps": sonusIcmpOutTimestamps,
       "sonusIcmpOutTimestampReps": sonusIcmpOutTimestampReps,
       "sonusIcmpOutAddrMasks": sonusIcmpOutAddrMasks,
       "sonusIcmpOutAddrMaskReps": sonusIcmpOutAddrMaskReps,
       "sonusIcmpGeneralGroupShelf": sonusIcmpGeneralGroupShelf,
       "sonusIcmpGeneralGroupSlot": sonusIcmpGeneralGroupSlot,
       "sonusIcmpGeneralGroupInstance": sonusIcmpGeneralGroupInstance,
       "sonusTcp": sonusTcp,
       "sonusTcpGeneralGroupTable": sonusTcpGeneralGroupTable,
       "sonusTcpGeneralGroupEntry": sonusTcpGeneralGroupEntry,
       "sonusTcpRtoAlgorithm": sonusTcpRtoAlgorithm,
       "sonusTcpRtoMin": sonusTcpRtoMin,
       "sonusTcpRtoMax": sonusTcpRtoMax,
       "sonusTcpMaxConn": sonusTcpMaxConn,
       "sonusTcpActiveOpens": sonusTcpActiveOpens,
       "sonusTcpPassiveOpens": sonusTcpPassiveOpens,
       "sonusTcpAttemptFails": sonusTcpAttemptFails,
       "sonusTcpEstabResets": sonusTcpEstabResets,
       "sonusTcpCurrEstab": sonusTcpCurrEstab,
       "sonusTcpInSegs": sonusTcpInSegs,
       "sonusTcpOutSegs": sonusTcpOutSegs,
       "sonusTcpRetransSegs": sonusTcpRetransSegs,
       "sonusTcpInErrs": sonusTcpInErrs,
       "sonusTcpOutRsts": sonusTcpOutRsts,
       "sonusTcpGeneralGroupShelf": sonusTcpGeneralGroupShelf,
       "sonusTcpGeneralGroupSlot": sonusTcpGeneralGroupSlot,
       "sonusTcpGeneralGroupInstance": sonusTcpGeneralGroupInstance,
       "sonusTcpConnTable": sonusTcpConnTable,
       "sonusTcpConnEntry": sonusTcpConnEntry,
       "sonusTcpConnState": sonusTcpConnState,
       "sonusTcpConnLocalAddress": sonusTcpConnLocalAddress,
       "sonusTcpConnLocalPort": sonusTcpConnLocalPort,
       "sonusTcpConnRemAddress": sonusTcpConnRemAddress,
       "sonusTcpConnRemPort": sonusTcpConnRemPort,
       "sonusTcpConnShelf": sonusTcpConnShelf,
       "sonusTcpConnSlot": sonusTcpConnSlot,
       "sonusTcpConnInstance": sonusTcpConnInstance,
       "sonusUdp": sonusUdp,
       "sonusUdpGeneralGroupTable": sonusUdpGeneralGroupTable,
       "sonusUdpGeneralGroupEntry": sonusUdpGeneralGroupEntry,
       "sonusUdpInDatagrams": sonusUdpInDatagrams,
       "sonusUdpNoPorts": sonusUdpNoPorts,
       "sonusUdpInErrors": sonusUdpInErrors,
       "sonusUdpOutDatagrams": sonusUdpOutDatagrams,
       "sonusUdpGeneralGroupShelf": sonusUdpGeneralGroupShelf,
       "sonusUdpGeneralGroupSlot": sonusUdpGeneralGroupSlot,
       "sonusUdpGeneralGroupInstance": sonusUdpGeneralGroupInstance,
       "sonusUdpTable": sonusUdpTable,
       "sonusUdpEntry": sonusUdpEntry,
       "sonusUdpLocalAddress": sonusUdpLocalAddress,
       "sonusUdpLocalPort": sonusUdpLocalPort,
       "sonusUdpShelf": sonusUdpShelf,
       "sonusUdpSlot": sonusUdpSlot,
       "sonusUdpInstance": sonusUdpInstance}
)
