# SNMP MIB module (IPV6-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IPV6-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:35:51 2024
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

(Ipv6Address,
 Ipv6AddressIfIdentifier,
 Ipv6AddressPrefix,
 Ipv6IfIndex,
 Ipv6IfIndexOrZero) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address",
    "Ipv6AddressIfIdentifier",
    "Ipv6AddressPrefix",
    "Ipv6IfIndex",
    "Ipv6IfIndexOrZero")

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
 PhysAddress,
 RowPointer,
 TextualConvention,
 TimeStamp,
 TruthValue,
 VariablePointer) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowPointer",
    "TextualConvention",
    "TimeStamp",
    "TruthValue",
    "VariablePointer")


# MODULE-IDENTITY

ipv6MIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 55)
)
ipv6MIB.setRevisions(
        ("2017-02-22 00:00",
         "1998-02-05 21:55")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ipv6MIBObjects_ObjectIdentity = ObjectIdentity
ipv6MIBObjects = _Ipv6MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 55, 1)
)


class _Ipv6Forwarding_Type(Integer32):
    """Custom type ipv6Forwarding based on Integer32"""
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


_Ipv6Forwarding_Type.__name__ = "Integer32"
_Ipv6Forwarding_Object = MibScalar
ipv6Forwarding = _Ipv6Forwarding_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 1),
    _Ipv6Forwarding_Type()
)
ipv6Forwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6Forwarding.setStatus("obsolete")


class _Ipv6DefaultHopLimit_Type(Integer32):
    """Custom type ipv6DefaultHopLimit based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Ipv6DefaultHopLimit_Type.__name__ = "Integer32"
_Ipv6DefaultHopLimit_Object = MibScalar
ipv6DefaultHopLimit = _Ipv6DefaultHopLimit_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 2),
    _Ipv6DefaultHopLimit_Type()
)
ipv6DefaultHopLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6DefaultHopLimit.setStatus("obsolete")
_Ipv6Interfaces_Type = Unsigned32
_Ipv6Interfaces_Object = MibScalar
ipv6Interfaces = _Ipv6Interfaces_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 3),
    _Ipv6Interfaces_Type()
)
ipv6Interfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6Interfaces.setStatus("obsolete")
_Ipv6IfTableLastChange_Type = TimeStamp
_Ipv6IfTableLastChange_Object = MibScalar
ipv6IfTableLastChange = _Ipv6IfTableLastChange_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 4),
    _Ipv6IfTableLastChange_Type()
)
ipv6IfTableLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfTableLastChange.setStatus("obsolete")
_Ipv6IfTable_Object = MibTable
ipv6IfTable = _Ipv6IfTable_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 5)
)
if mibBuilder.loadTexts:
    ipv6IfTable.setStatus("obsolete")
_Ipv6IfEntry_Object = MibTableRow
ipv6IfEntry = _Ipv6IfEntry_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 5, 1)
)
ipv6IfEntry.setIndexNames(
    (0, "IPV6-MIB", "ipv6IfIndex"),
)
if mibBuilder.loadTexts:
    ipv6IfEntry.setStatus("obsolete")
_Ipv6IfIndex_Type = Ipv6IfIndex
_Ipv6IfIndex_Object = MibTableColumn
ipv6IfIndex = _Ipv6IfIndex_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 5, 1, 1),
    _Ipv6IfIndex_Type()
)
ipv6IfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipv6IfIndex.setStatus("obsolete")
_Ipv6IfDescr_Type = DisplayString
_Ipv6IfDescr_Object = MibTableColumn
ipv6IfDescr = _Ipv6IfDescr_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 5, 1, 2),
    _Ipv6IfDescr_Type()
)
ipv6IfDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6IfDescr.setStatus("obsolete")
_Ipv6IfLowerLayer_Type = VariablePointer
_Ipv6IfLowerLayer_Object = MibTableColumn
ipv6IfLowerLayer = _Ipv6IfLowerLayer_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 5, 1, 3),
    _Ipv6IfLowerLayer_Type()
)
ipv6IfLowerLayer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfLowerLayer.setStatus("obsolete")
_Ipv6IfEffectiveMtu_Type = Unsigned32
_Ipv6IfEffectiveMtu_Object = MibTableColumn
ipv6IfEffectiveMtu = _Ipv6IfEffectiveMtu_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 5, 1, 4),
    _Ipv6IfEffectiveMtu_Type()
)
ipv6IfEffectiveMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfEffectiveMtu.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6IfEffectiveMtu.setUnits("octets")


class _Ipv6IfReasmMaxSize_Type(Unsigned32):
    """Custom type ipv6IfReasmMaxSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Ipv6IfReasmMaxSize_Type.__name__ = "Unsigned32"
_Ipv6IfReasmMaxSize_Object = MibTableColumn
ipv6IfReasmMaxSize = _Ipv6IfReasmMaxSize_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 5, 1, 5),
    _Ipv6IfReasmMaxSize_Type()
)
ipv6IfReasmMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfReasmMaxSize.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6IfReasmMaxSize.setUnits("octets")
_Ipv6IfIdentifier_Type = Ipv6AddressIfIdentifier
_Ipv6IfIdentifier_Object = MibTableColumn
ipv6IfIdentifier = _Ipv6IfIdentifier_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 5, 1, 6),
    _Ipv6IfIdentifier_Type()
)
ipv6IfIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6IfIdentifier.setStatus("obsolete")


class _Ipv6IfIdentifierLength_Type(Integer32):
    """Custom type ipv6IfIdentifierLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_Ipv6IfIdentifierLength_Type.__name__ = "Integer32"
_Ipv6IfIdentifierLength_Object = MibTableColumn
ipv6IfIdentifierLength = _Ipv6IfIdentifierLength_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 5, 1, 7),
    _Ipv6IfIdentifierLength_Type()
)
ipv6IfIdentifierLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6IfIdentifierLength.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6IfIdentifierLength.setUnits("bits")
_Ipv6IfPhysicalAddress_Type = PhysAddress
_Ipv6IfPhysicalAddress_Object = MibTableColumn
ipv6IfPhysicalAddress = _Ipv6IfPhysicalAddress_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 5, 1, 8),
    _Ipv6IfPhysicalAddress_Type()
)
ipv6IfPhysicalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfPhysicalAddress.setStatus("obsolete")


class _Ipv6IfAdminStatus_Type(Integer32):
    """Custom type ipv6IfAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_Ipv6IfAdminStatus_Type.__name__ = "Integer32"
_Ipv6IfAdminStatus_Object = MibTableColumn
ipv6IfAdminStatus = _Ipv6IfAdminStatus_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 5, 1, 9),
    _Ipv6IfAdminStatus_Type()
)
ipv6IfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6IfAdminStatus.setStatus("obsolete")


class _Ipv6IfOperStatus_Type(Integer32):
    """Custom type ipv6IfOperStatus based on Integer32"""
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
        *(("down", 2),
          ("noIfIdentifier", 3),
          ("notPresent", 5),
          ("unknown", 4),
          ("up", 1))
    )


_Ipv6IfOperStatus_Type.__name__ = "Integer32"
_Ipv6IfOperStatus_Object = MibTableColumn
ipv6IfOperStatus = _Ipv6IfOperStatus_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 5, 1, 10),
    _Ipv6IfOperStatus_Type()
)
ipv6IfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfOperStatus.setStatus("obsolete")
_Ipv6IfLastChange_Type = TimeStamp
_Ipv6IfLastChange_Object = MibTableColumn
ipv6IfLastChange = _Ipv6IfLastChange_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 5, 1, 11),
    _Ipv6IfLastChange_Type()
)
ipv6IfLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfLastChange.setStatus("obsolete")
_Ipv6IfStatsTable_Object = MibTable
ipv6IfStatsTable = _Ipv6IfStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 6)
)
if mibBuilder.loadTexts:
    ipv6IfStatsTable.setStatus("obsolete")
_Ipv6IfStatsEntry_Object = MibTableRow
ipv6IfStatsEntry = _Ipv6IfStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 6, 1)
)
if mibBuilder.loadTexts:
    ipv6IfStatsEntry.setStatus("obsolete")
_Ipv6IfStatsInReceives_Type = Counter32
_Ipv6IfStatsInReceives_Object = MibTableColumn
ipv6IfStatsInReceives = _Ipv6IfStatsInReceives_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 6, 1, 1),
    _Ipv6IfStatsInReceives_Type()
)
ipv6IfStatsInReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfStatsInReceives.setStatus("obsolete")
_Ipv6IfStatsInHdrErrors_Type = Counter32
_Ipv6IfStatsInHdrErrors_Object = MibTableColumn
ipv6IfStatsInHdrErrors = _Ipv6IfStatsInHdrErrors_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 6, 1, 2),
    _Ipv6IfStatsInHdrErrors_Type()
)
ipv6IfStatsInHdrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfStatsInHdrErrors.setStatus("obsolete")
_Ipv6IfStatsInTooBigErrors_Type = Counter32
_Ipv6IfStatsInTooBigErrors_Object = MibTableColumn
ipv6IfStatsInTooBigErrors = _Ipv6IfStatsInTooBigErrors_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 6, 1, 3),
    _Ipv6IfStatsInTooBigErrors_Type()
)
ipv6IfStatsInTooBigErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfStatsInTooBigErrors.setStatus("obsolete")
_Ipv6IfStatsInNoRoutes_Type = Counter32
_Ipv6IfStatsInNoRoutes_Object = MibTableColumn
ipv6IfStatsInNoRoutes = _Ipv6IfStatsInNoRoutes_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 6, 1, 4),
    _Ipv6IfStatsInNoRoutes_Type()
)
ipv6IfStatsInNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfStatsInNoRoutes.setStatus("obsolete")
_Ipv6IfStatsInAddrErrors_Type = Counter32
_Ipv6IfStatsInAddrErrors_Object = MibTableColumn
ipv6IfStatsInAddrErrors = _Ipv6IfStatsInAddrErrors_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 6, 1, 5),
    _Ipv6IfStatsInAddrErrors_Type()
)
ipv6IfStatsInAddrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfStatsInAddrErrors.setStatus("obsolete")
_Ipv6IfStatsInUnknownProtos_Type = Counter32
_Ipv6IfStatsInUnknownProtos_Object = MibTableColumn
ipv6IfStatsInUnknownProtos = _Ipv6IfStatsInUnknownProtos_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 6, 1, 6),
    _Ipv6IfStatsInUnknownProtos_Type()
)
ipv6IfStatsInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfStatsInUnknownProtos.setStatus("obsolete")
_Ipv6IfStatsInTruncatedPkts_Type = Counter32
_Ipv6IfStatsInTruncatedPkts_Object = MibTableColumn
ipv6IfStatsInTruncatedPkts = _Ipv6IfStatsInTruncatedPkts_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 6, 1, 7),
    _Ipv6IfStatsInTruncatedPkts_Type()
)
ipv6IfStatsInTruncatedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfStatsInTruncatedPkts.setStatus("obsolete")
_Ipv6IfStatsInDiscards_Type = Counter32
_Ipv6IfStatsInDiscards_Object = MibTableColumn
ipv6IfStatsInDiscards = _Ipv6IfStatsInDiscards_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 6, 1, 8),
    _Ipv6IfStatsInDiscards_Type()
)
ipv6IfStatsInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfStatsInDiscards.setStatus("obsolete")
_Ipv6IfStatsInDelivers_Type = Counter32
_Ipv6IfStatsInDelivers_Object = MibTableColumn
ipv6IfStatsInDelivers = _Ipv6IfStatsInDelivers_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 6, 1, 9),
    _Ipv6IfStatsInDelivers_Type()
)
ipv6IfStatsInDelivers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfStatsInDelivers.setStatus("obsolete")
_Ipv6IfStatsOutForwDatagrams_Type = Counter32
_Ipv6IfStatsOutForwDatagrams_Object = MibTableColumn
ipv6IfStatsOutForwDatagrams = _Ipv6IfStatsOutForwDatagrams_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 6, 1, 10),
    _Ipv6IfStatsOutForwDatagrams_Type()
)
ipv6IfStatsOutForwDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfStatsOutForwDatagrams.setStatus("obsolete")
_Ipv6IfStatsOutRequests_Type = Counter32
_Ipv6IfStatsOutRequests_Object = MibTableColumn
ipv6IfStatsOutRequests = _Ipv6IfStatsOutRequests_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 6, 1, 11),
    _Ipv6IfStatsOutRequests_Type()
)
ipv6IfStatsOutRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfStatsOutRequests.setStatus("obsolete")
_Ipv6IfStatsOutDiscards_Type = Counter32
_Ipv6IfStatsOutDiscards_Object = MibTableColumn
ipv6IfStatsOutDiscards = _Ipv6IfStatsOutDiscards_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 6, 1, 12),
    _Ipv6IfStatsOutDiscards_Type()
)
ipv6IfStatsOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfStatsOutDiscards.setStatus("obsolete")
_Ipv6IfStatsOutFragOKs_Type = Counter32
_Ipv6IfStatsOutFragOKs_Object = MibTableColumn
ipv6IfStatsOutFragOKs = _Ipv6IfStatsOutFragOKs_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 6, 1, 13),
    _Ipv6IfStatsOutFragOKs_Type()
)
ipv6IfStatsOutFragOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfStatsOutFragOKs.setStatus("obsolete")
_Ipv6IfStatsOutFragFails_Type = Counter32
_Ipv6IfStatsOutFragFails_Object = MibTableColumn
ipv6IfStatsOutFragFails = _Ipv6IfStatsOutFragFails_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 6, 1, 14),
    _Ipv6IfStatsOutFragFails_Type()
)
ipv6IfStatsOutFragFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfStatsOutFragFails.setStatus("obsolete")
_Ipv6IfStatsOutFragCreates_Type = Counter32
_Ipv6IfStatsOutFragCreates_Object = MibTableColumn
ipv6IfStatsOutFragCreates = _Ipv6IfStatsOutFragCreates_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 6, 1, 15),
    _Ipv6IfStatsOutFragCreates_Type()
)
ipv6IfStatsOutFragCreates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfStatsOutFragCreates.setStatus("obsolete")
_Ipv6IfStatsReasmReqds_Type = Counter32
_Ipv6IfStatsReasmReqds_Object = MibTableColumn
ipv6IfStatsReasmReqds = _Ipv6IfStatsReasmReqds_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 6, 1, 16),
    _Ipv6IfStatsReasmReqds_Type()
)
ipv6IfStatsReasmReqds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfStatsReasmReqds.setStatus("obsolete")
_Ipv6IfStatsReasmOKs_Type = Counter32
_Ipv6IfStatsReasmOKs_Object = MibTableColumn
ipv6IfStatsReasmOKs = _Ipv6IfStatsReasmOKs_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 6, 1, 17),
    _Ipv6IfStatsReasmOKs_Type()
)
ipv6IfStatsReasmOKs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfStatsReasmOKs.setStatus("obsolete")
_Ipv6IfStatsReasmFails_Type = Counter32
_Ipv6IfStatsReasmFails_Object = MibTableColumn
ipv6IfStatsReasmFails = _Ipv6IfStatsReasmFails_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 6, 1, 18),
    _Ipv6IfStatsReasmFails_Type()
)
ipv6IfStatsReasmFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfStatsReasmFails.setStatus("obsolete")
_Ipv6IfStatsInMcastPkts_Type = Counter32
_Ipv6IfStatsInMcastPkts_Object = MibTableColumn
ipv6IfStatsInMcastPkts = _Ipv6IfStatsInMcastPkts_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 6, 1, 19),
    _Ipv6IfStatsInMcastPkts_Type()
)
ipv6IfStatsInMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfStatsInMcastPkts.setStatus("obsolete")
_Ipv6IfStatsOutMcastPkts_Type = Counter32
_Ipv6IfStatsOutMcastPkts_Object = MibTableColumn
ipv6IfStatsOutMcastPkts = _Ipv6IfStatsOutMcastPkts_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 6, 1, 20),
    _Ipv6IfStatsOutMcastPkts_Type()
)
ipv6IfStatsOutMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfStatsOutMcastPkts.setStatus("obsolete")
_Ipv6AddrPrefixTable_Object = MibTable
ipv6AddrPrefixTable = _Ipv6AddrPrefixTable_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 7)
)
if mibBuilder.loadTexts:
    ipv6AddrPrefixTable.setStatus("obsolete")
_Ipv6AddrPrefixEntry_Object = MibTableRow
ipv6AddrPrefixEntry = _Ipv6AddrPrefixEntry_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 7, 1)
)
ipv6AddrPrefixEntry.setIndexNames(
    (0, "IPV6-MIB", "ipv6IfIndex"),
    (0, "IPV6-MIB", "ipv6AddrPrefix"),
    (0, "IPV6-MIB", "ipv6AddrPrefixLength"),
)
if mibBuilder.loadTexts:
    ipv6AddrPrefixEntry.setStatus("obsolete")
_Ipv6AddrPrefix_Type = Ipv6AddressPrefix
_Ipv6AddrPrefix_Object = MibTableColumn
ipv6AddrPrefix = _Ipv6AddrPrefix_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 7, 1, 1),
    _Ipv6AddrPrefix_Type()
)
ipv6AddrPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipv6AddrPrefix.setStatus("obsolete")


class _Ipv6AddrPrefixLength_Type(Integer32):
    """Custom type ipv6AddrPrefixLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Ipv6AddrPrefixLength_Type.__name__ = "Integer32"
_Ipv6AddrPrefixLength_Object = MibTableColumn
ipv6AddrPrefixLength = _Ipv6AddrPrefixLength_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 7, 1, 2),
    _Ipv6AddrPrefixLength_Type()
)
ipv6AddrPrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipv6AddrPrefixLength.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6AddrPrefixLength.setUnits("bits")
_Ipv6AddrPrefixOnLinkFlag_Type = TruthValue
_Ipv6AddrPrefixOnLinkFlag_Object = MibTableColumn
ipv6AddrPrefixOnLinkFlag = _Ipv6AddrPrefixOnLinkFlag_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 7, 1, 3),
    _Ipv6AddrPrefixOnLinkFlag_Type()
)
ipv6AddrPrefixOnLinkFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6AddrPrefixOnLinkFlag.setStatus("obsolete")
_Ipv6AddrPrefixAutonomousFlag_Type = TruthValue
_Ipv6AddrPrefixAutonomousFlag_Object = MibTableColumn
ipv6AddrPrefixAutonomousFlag = _Ipv6AddrPrefixAutonomousFlag_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 7, 1, 4),
    _Ipv6AddrPrefixAutonomousFlag_Type()
)
ipv6AddrPrefixAutonomousFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6AddrPrefixAutonomousFlag.setStatus("obsolete")
_Ipv6AddrPrefixAdvPreferredLifetime_Type = Unsigned32
_Ipv6AddrPrefixAdvPreferredLifetime_Object = MibTableColumn
ipv6AddrPrefixAdvPreferredLifetime = _Ipv6AddrPrefixAdvPreferredLifetime_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 7, 1, 5),
    _Ipv6AddrPrefixAdvPreferredLifetime_Type()
)
ipv6AddrPrefixAdvPreferredLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6AddrPrefixAdvPreferredLifetime.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6AddrPrefixAdvPreferredLifetime.setUnits("seconds")
_Ipv6AddrPrefixAdvValidLifetime_Type = Unsigned32
_Ipv6AddrPrefixAdvValidLifetime_Object = MibTableColumn
ipv6AddrPrefixAdvValidLifetime = _Ipv6AddrPrefixAdvValidLifetime_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 7, 1, 6),
    _Ipv6AddrPrefixAdvValidLifetime_Type()
)
ipv6AddrPrefixAdvValidLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6AddrPrefixAdvValidLifetime.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6AddrPrefixAdvValidLifetime.setUnits("seconds")
_Ipv6AddrTable_Object = MibTable
ipv6AddrTable = _Ipv6AddrTable_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 8)
)
if mibBuilder.loadTexts:
    ipv6AddrTable.setStatus("obsolete")
_Ipv6AddrEntry_Object = MibTableRow
ipv6AddrEntry = _Ipv6AddrEntry_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 8, 1)
)
ipv6AddrEntry.setIndexNames(
    (0, "IPV6-MIB", "ipv6IfIndex"),
    (0, "IPV6-MIB", "ipv6AddrAddress"),
)
if mibBuilder.loadTexts:
    ipv6AddrEntry.setStatus("obsolete")
_Ipv6AddrAddress_Type = Ipv6Address
_Ipv6AddrAddress_Object = MibTableColumn
ipv6AddrAddress = _Ipv6AddrAddress_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 8, 1, 1),
    _Ipv6AddrAddress_Type()
)
ipv6AddrAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipv6AddrAddress.setStatus("obsolete")


class _Ipv6AddrPfxLength_Type(Integer32):
    """Custom type ipv6AddrPfxLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Ipv6AddrPfxLength_Type.__name__ = "Integer32"
_Ipv6AddrPfxLength_Object = MibTableColumn
ipv6AddrPfxLength = _Ipv6AddrPfxLength_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 8, 1, 2),
    _Ipv6AddrPfxLength_Type()
)
ipv6AddrPfxLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6AddrPfxLength.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6AddrPfxLength.setUnits("bits")


class _Ipv6AddrType_Type(Integer32):
    """Custom type ipv6AddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("stateful", 2),
          ("stateless", 1),
          ("unknown", 3))
    )


_Ipv6AddrType_Type.__name__ = "Integer32"
_Ipv6AddrType_Object = MibTableColumn
ipv6AddrType = _Ipv6AddrType_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 8, 1, 3),
    _Ipv6AddrType_Type()
)
ipv6AddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6AddrType.setStatus("obsolete")
_Ipv6AddrAnycastFlag_Type = TruthValue
_Ipv6AddrAnycastFlag_Object = MibTableColumn
ipv6AddrAnycastFlag = _Ipv6AddrAnycastFlag_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 8, 1, 4),
    _Ipv6AddrAnycastFlag_Type()
)
ipv6AddrAnycastFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6AddrAnycastFlag.setStatus("obsolete")


class _Ipv6AddrStatus_Type(Integer32):
    """Custom type ipv6AddrStatus based on Integer32"""
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
        *(("deprecated", 2),
          ("inaccessible", 4),
          ("invalid", 3),
          ("preferred", 1),
          ("unknown", 5))
    )


_Ipv6AddrStatus_Type.__name__ = "Integer32"
_Ipv6AddrStatus_Object = MibTableColumn
ipv6AddrStatus = _Ipv6AddrStatus_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 8, 1, 5),
    _Ipv6AddrStatus_Type()
)
ipv6AddrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6AddrStatus.setStatus("obsolete")
_Ipv6RouteNumber_Type = Gauge32
_Ipv6RouteNumber_Object = MibScalar
ipv6RouteNumber = _Ipv6RouteNumber_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 9),
    _Ipv6RouteNumber_Type()
)
ipv6RouteNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6RouteNumber.setStatus("obsolete")
_Ipv6DiscardedRoutes_Type = Counter32
_Ipv6DiscardedRoutes_Object = MibScalar
ipv6DiscardedRoutes = _Ipv6DiscardedRoutes_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 10),
    _Ipv6DiscardedRoutes_Type()
)
ipv6DiscardedRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6DiscardedRoutes.setStatus("obsolete")
_Ipv6RouteTable_Object = MibTable
ipv6RouteTable = _Ipv6RouteTable_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 11)
)
if mibBuilder.loadTexts:
    ipv6RouteTable.setStatus("obsolete")
_Ipv6RouteEntry_Object = MibTableRow
ipv6RouteEntry = _Ipv6RouteEntry_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 11, 1)
)
ipv6RouteEntry.setIndexNames(
    (0, "IPV6-MIB", "ipv6RouteDest"),
    (0, "IPV6-MIB", "ipv6RoutePfxLength"),
    (0, "IPV6-MIB", "ipv6RouteIndex"),
)
if mibBuilder.loadTexts:
    ipv6RouteEntry.setStatus("obsolete")
_Ipv6RouteDest_Type = Ipv6Address
_Ipv6RouteDest_Object = MibTableColumn
ipv6RouteDest = _Ipv6RouteDest_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 11, 1, 1),
    _Ipv6RouteDest_Type()
)
ipv6RouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipv6RouteDest.setStatus("obsolete")


class _Ipv6RoutePfxLength_Type(Integer32):
    """Custom type ipv6RoutePfxLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_Ipv6RoutePfxLength_Type.__name__ = "Integer32"
_Ipv6RoutePfxLength_Object = MibTableColumn
ipv6RoutePfxLength = _Ipv6RoutePfxLength_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 11, 1, 2),
    _Ipv6RoutePfxLength_Type()
)
ipv6RoutePfxLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipv6RoutePfxLength.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6RoutePfxLength.setUnits("bits")
_Ipv6RouteIndex_Type = Unsigned32
_Ipv6RouteIndex_Object = MibTableColumn
ipv6RouteIndex = _Ipv6RouteIndex_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 11, 1, 3),
    _Ipv6RouteIndex_Type()
)
ipv6RouteIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipv6RouteIndex.setStatus("obsolete")
_Ipv6RouteIfIndex_Type = Ipv6IfIndexOrZero
_Ipv6RouteIfIndex_Object = MibTableColumn
ipv6RouteIfIndex = _Ipv6RouteIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 11, 1, 4),
    _Ipv6RouteIfIndex_Type()
)
ipv6RouteIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6RouteIfIndex.setStatus("obsolete")
_Ipv6RouteNextHop_Type = Ipv6Address
_Ipv6RouteNextHop_Object = MibTableColumn
ipv6RouteNextHop = _Ipv6RouteNextHop_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 11, 1, 5),
    _Ipv6RouteNextHop_Type()
)
ipv6RouteNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6RouteNextHop.setStatus("obsolete")


class _Ipv6RouteType_Type(Integer32):
    """Custom type ipv6RouteType based on Integer32"""
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
        *(("discard", 2),
          ("local", 3),
          ("other", 1),
          ("remote", 4))
    )


_Ipv6RouteType_Type.__name__ = "Integer32"
_Ipv6RouteType_Object = MibTableColumn
ipv6RouteType = _Ipv6RouteType_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 11, 1, 6),
    _Ipv6RouteType_Type()
)
ipv6RouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6RouteType.setStatus("obsolete")


class _Ipv6RouteProtocol_Type(Integer32):
    """Custom type ipv6RouteProtocol based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("bgp", 7),
          ("idrp", 8),
          ("igrp", 9),
          ("local", 2),
          ("ndisc", 4),
          ("netmgmt", 3),
          ("ospf", 6),
          ("other", 1),
          ("rip", 5))
    )


_Ipv6RouteProtocol_Type.__name__ = "Integer32"
_Ipv6RouteProtocol_Object = MibTableColumn
ipv6RouteProtocol = _Ipv6RouteProtocol_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 11, 1, 7),
    _Ipv6RouteProtocol_Type()
)
ipv6RouteProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6RouteProtocol.setStatus("obsolete")
_Ipv6RoutePolicy_Type = Integer32
_Ipv6RoutePolicy_Object = MibTableColumn
ipv6RoutePolicy = _Ipv6RoutePolicy_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 11, 1, 8),
    _Ipv6RoutePolicy_Type()
)
ipv6RoutePolicy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6RoutePolicy.setStatus("obsolete")
_Ipv6RouteAge_Type = Unsigned32
_Ipv6RouteAge_Object = MibTableColumn
ipv6RouteAge = _Ipv6RouteAge_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 11, 1, 9),
    _Ipv6RouteAge_Type()
)
ipv6RouteAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6RouteAge.setStatus("obsolete")
if mibBuilder.loadTexts:
    ipv6RouteAge.setUnits("seconds")
_Ipv6RouteNextHopRDI_Type = Unsigned32
_Ipv6RouteNextHopRDI_Object = MibTableColumn
ipv6RouteNextHopRDI = _Ipv6RouteNextHopRDI_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 11, 1, 10),
    _Ipv6RouteNextHopRDI_Type()
)
ipv6RouteNextHopRDI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6RouteNextHopRDI.setStatus("obsolete")
_Ipv6RouteMetric_Type = Unsigned32
_Ipv6RouteMetric_Object = MibTableColumn
ipv6RouteMetric = _Ipv6RouteMetric_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 11, 1, 11),
    _Ipv6RouteMetric_Type()
)
ipv6RouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6RouteMetric.setStatus("obsolete")
_Ipv6RouteWeight_Type = Unsigned32
_Ipv6RouteWeight_Object = MibTableColumn
ipv6RouteWeight = _Ipv6RouteWeight_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 11, 1, 12),
    _Ipv6RouteWeight_Type()
)
ipv6RouteWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6RouteWeight.setStatus("obsolete")
_Ipv6RouteInfo_Type = RowPointer
_Ipv6RouteInfo_Object = MibTableColumn
ipv6RouteInfo = _Ipv6RouteInfo_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 11, 1, 13),
    _Ipv6RouteInfo_Type()
)
ipv6RouteInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6RouteInfo.setStatus("obsolete")


class _Ipv6RouteValid_Type(TruthValue):
    """Custom type ipv6RouteValid based on TruthValue"""


_Ipv6RouteValid_Object = MibTableColumn
ipv6RouteValid = _Ipv6RouteValid_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 11, 1, 14),
    _Ipv6RouteValid_Type()
)
ipv6RouteValid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6RouteValid.setStatus("obsolete")
_Ipv6NetToMediaTable_Object = MibTable
ipv6NetToMediaTable = _Ipv6NetToMediaTable_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 12)
)
if mibBuilder.loadTexts:
    ipv6NetToMediaTable.setStatus("obsolete")
_Ipv6NetToMediaEntry_Object = MibTableRow
ipv6NetToMediaEntry = _Ipv6NetToMediaEntry_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 12, 1)
)
ipv6NetToMediaEntry.setIndexNames(
    (0, "IPV6-MIB", "ipv6IfIndex"),
    (0, "IPV6-MIB", "ipv6NetToMediaNetAddress"),
)
if mibBuilder.loadTexts:
    ipv6NetToMediaEntry.setStatus("obsolete")
_Ipv6NetToMediaNetAddress_Type = Ipv6Address
_Ipv6NetToMediaNetAddress_Object = MibTableColumn
ipv6NetToMediaNetAddress = _Ipv6NetToMediaNetAddress_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 12, 1, 1),
    _Ipv6NetToMediaNetAddress_Type()
)
ipv6NetToMediaNetAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipv6NetToMediaNetAddress.setStatus("obsolete")
_Ipv6NetToMediaPhysAddress_Type = PhysAddress
_Ipv6NetToMediaPhysAddress_Object = MibTableColumn
ipv6NetToMediaPhysAddress = _Ipv6NetToMediaPhysAddress_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 12, 1, 2),
    _Ipv6NetToMediaPhysAddress_Type()
)
ipv6NetToMediaPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6NetToMediaPhysAddress.setStatus("obsolete")


class _Ipv6NetToMediaType_Type(Integer32):
    """Custom type ipv6NetToMediaType based on Integer32"""
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
        *(("dynamic", 2),
          ("local", 4),
          ("other", 1),
          ("static", 3))
    )


_Ipv6NetToMediaType_Type.__name__ = "Integer32"
_Ipv6NetToMediaType_Object = MibTableColumn
ipv6NetToMediaType = _Ipv6NetToMediaType_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 12, 1, 3),
    _Ipv6NetToMediaType_Type()
)
ipv6NetToMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6NetToMediaType.setStatus("obsolete")


class _Ipv6IfNetToMediaState_Type(Integer32):
    """Custom type ipv6IfNetToMediaState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("delay", 3),
          ("invalid", 5),
          ("probe", 4),
          ("reachable", 1),
          ("stale", 2),
          ("unknown", 6))
    )


_Ipv6IfNetToMediaState_Type.__name__ = "Integer32"
_Ipv6IfNetToMediaState_Object = MibTableColumn
ipv6IfNetToMediaState = _Ipv6IfNetToMediaState_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 12, 1, 4),
    _Ipv6IfNetToMediaState_Type()
)
ipv6IfNetToMediaState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfNetToMediaState.setStatus("obsolete")
_Ipv6IfNetToMediaLastUpdated_Type = TimeStamp
_Ipv6IfNetToMediaLastUpdated_Object = MibTableColumn
ipv6IfNetToMediaLastUpdated = _Ipv6IfNetToMediaLastUpdated_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 12, 1, 5),
    _Ipv6IfNetToMediaLastUpdated_Type()
)
ipv6IfNetToMediaLastUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipv6IfNetToMediaLastUpdated.setStatus("obsolete")


class _Ipv6NetToMediaValid_Type(TruthValue):
    """Custom type ipv6NetToMediaValid based on TruthValue"""


_Ipv6NetToMediaValid_Object = MibTableColumn
ipv6NetToMediaValid = _Ipv6NetToMediaValid_Object(
    (1, 3, 6, 1, 2, 1, 55, 1, 12, 1, 6),
    _Ipv6NetToMediaValid_Type()
)
ipv6NetToMediaValid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6NetToMediaValid.setStatus("obsolete")
_Ipv6Notifications_ObjectIdentity = ObjectIdentity
ipv6Notifications = _Ipv6Notifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 55, 2)
)
_Ipv6NotificationPrefix_ObjectIdentity = ObjectIdentity
ipv6NotificationPrefix = _Ipv6NotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 55, 2, 0)
)
_Ipv6Conformance_ObjectIdentity = ObjectIdentity
ipv6Conformance = _Ipv6Conformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 55, 3)
)
_Ipv6Compliances_ObjectIdentity = ObjectIdentity
ipv6Compliances = _Ipv6Compliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 55, 3, 1)
)
_Ipv6Groups_ObjectIdentity = ObjectIdentity
ipv6Groups = _Ipv6Groups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 55, 3, 2)
)
ipv6IfEntry.registerAugmentions(
    ("IPV6-MIB",
     "ipv6IfStatsEntry")
)
ipv6IfStatsEntry.setIndexNames(*ipv6IfEntry.getIndexNames())

# Managed Objects groups

ipv6GeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 55, 3, 2, 1)
)
ipv6GeneralGroup.setObjects(
      *(("IPV6-MIB", "ipv6Forwarding"),
        ("IPV6-MIB", "ipv6DefaultHopLimit"),
        ("IPV6-MIB", "ipv6Interfaces"),
        ("IPV6-MIB", "ipv6IfTableLastChange"),
        ("IPV6-MIB", "ipv6IfDescr"),
        ("IPV6-MIB", "ipv6IfLowerLayer"),
        ("IPV6-MIB", "ipv6IfEffectiveMtu"),
        ("IPV6-MIB", "ipv6IfReasmMaxSize"),
        ("IPV6-MIB", "ipv6IfIdentifier"),
        ("IPV6-MIB", "ipv6IfIdentifierLength"),
        ("IPV6-MIB", "ipv6IfPhysicalAddress"),
        ("IPV6-MIB", "ipv6IfAdminStatus"),
        ("IPV6-MIB", "ipv6IfOperStatus"),
        ("IPV6-MIB", "ipv6IfLastChange"),
        ("IPV6-MIB", "ipv6IfStatsInReceives"),
        ("IPV6-MIB", "ipv6IfStatsInHdrErrors"),
        ("IPV6-MIB", "ipv6IfStatsInTooBigErrors"),
        ("IPV6-MIB", "ipv6IfStatsInNoRoutes"),
        ("IPV6-MIB", "ipv6IfStatsInAddrErrors"),
        ("IPV6-MIB", "ipv6IfStatsInUnknownProtos"),
        ("IPV6-MIB", "ipv6IfStatsInTruncatedPkts"),
        ("IPV6-MIB", "ipv6IfStatsInDiscards"),
        ("IPV6-MIB", "ipv6IfStatsInDelivers"),
        ("IPV6-MIB", "ipv6IfStatsOutForwDatagrams"),
        ("IPV6-MIB", "ipv6IfStatsOutRequests"),
        ("IPV6-MIB", "ipv6IfStatsOutDiscards"),
        ("IPV6-MIB", "ipv6IfStatsOutFragOKs"),
        ("IPV6-MIB", "ipv6IfStatsOutFragFails"),
        ("IPV6-MIB", "ipv6IfStatsOutFragCreates"),
        ("IPV6-MIB", "ipv6IfStatsReasmReqds"),
        ("IPV6-MIB", "ipv6IfStatsReasmOKs"),
        ("IPV6-MIB", "ipv6IfStatsReasmFails"),
        ("IPV6-MIB", "ipv6IfStatsInMcastPkts"),
        ("IPV6-MIB", "ipv6IfStatsOutMcastPkts"),
        ("IPV6-MIB", "ipv6AddrPrefixOnLinkFlag"),
        ("IPV6-MIB", "ipv6AddrPrefixAutonomousFlag"),
        ("IPV6-MIB", "ipv6AddrPrefixAdvPreferredLifetime"),
        ("IPV6-MIB", "ipv6AddrPrefixAdvValidLifetime"),
        ("IPV6-MIB", "ipv6AddrPfxLength"),
        ("IPV6-MIB", "ipv6AddrType"),
        ("IPV6-MIB", "ipv6AddrAnycastFlag"),
        ("IPV6-MIB", "ipv6AddrStatus"),
        ("IPV6-MIB", "ipv6RouteNumber"),
        ("IPV6-MIB", "ipv6DiscardedRoutes"),
        ("IPV6-MIB", "ipv6RouteIfIndex"),
        ("IPV6-MIB", "ipv6RouteNextHop"),
        ("IPV6-MIB", "ipv6RouteType"),
        ("IPV6-MIB", "ipv6RouteProtocol"),
        ("IPV6-MIB", "ipv6RoutePolicy"),
        ("IPV6-MIB", "ipv6RouteAge"),
        ("IPV6-MIB", "ipv6RouteNextHopRDI"),
        ("IPV6-MIB", "ipv6RouteMetric"),
        ("IPV6-MIB", "ipv6RouteWeight"),
        ("IPV6-MIB", "ipv6RouteInfo"),
        ("IPV6-MIB", "ipv6RouteValid"),
        ("IPV6-MIB", "ipv6NetToMediaPhysAddress"),
        ("IPV6-MIB", "ipv6NetToMediaType"),
        ("IPV6-MIB", "ipv6IfNetToMediaState"),
        ("IPV6-MIB", "ipv6IfNetToMediaLastUpdated"),
        ("IPV6-MIB", "ipv6NetToMediaValid"))
)
if mibBuilder.loadTexts:
    ipv6GeneralGroup.setStatus("obsolete")


# Notification objects

ipv6IfStateChange = NotificationType(
    (1, 3, 6, 1, 2, 1, 55, 2, 0, 1)
)
ipv6IfStateChange.setObjects(
      *(("IPV6-MIB", "ipv6IfDescr"),
        ("IPV6-MIB", "ipv6IfOperStatus"))
)
if mibBuilder.loadTexts:
    ipv6IfStateChange.setStatus(
        "obsolete"
    )


# Notifications groups

ipv6NotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 55, 3, 2, 2)
)
ipv6NotificationGroup.setObjects(
    ("IPV6-MIB", "ipv6IfStateChange")
)
if mibBuilder.loadTexts:
    ipv6NotificationGroup.setStatus(
        "obsolete"
    )


# Agent capabilities


# Module compliance

ipv6Compliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 55, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ipv6Compliance.setStatus(
        "obsolete"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPV6-MIB",
    **{"ipv6MIB": ipv6MIB,
       "ipv6MIBObjects": ipv6MIBObjects,
       "ipv6Forwarding": ipv6Forwarding,
       "ipv6DefaultHopLimit": ipv6DefaultHopLimit,
       "ipv6Interfaces": ipv6Interfaces,
       "ipv6IfTableLastChange": ipv6IfTableLastChange,
       "ipv6IfTable": ipv6IfTable,
       "ipv6IfEntry": ipv6IfEntry,
       "ipv6IfIndex": ipv6IfIndex,
       "ipv6IfDescr": ipv6IfDescr,
       "ipv6IfLowerLayer": ipv6IfLowerLayer,
       "ipv6IfEffectiveMtu": ipv6IfEffectiveMtu,
       "ipv6IfReasmMaxSize": ipv6IfReasmMaxSize,
       "ipv6IfIdentifier": ipv6IfIdentifier,
       "ipv6IfIdentifierLength": ipv6IfIdentifierLength,
       "ipv6IfPhysicalAddress": ipv6IfPhysicalAddress,
       "ipv6IfAdminStatus": ipv6IfAdminStatus,
       "ipv6IfOperStatus": ipv6IfOperStatus,
       "ipv6IfLastChange": ipv6IfLastChange,
       "ipv6IfStatsTable": ipv6IfStatsTable,
       "ipv6IfStatsEntry": ipv6IfStatsEntry,
       "ipv6IfStatsInReceives": ipv6IfStatsInReceives,
       "ipv6IfStatsInHdrErrors": ipv6IfStatsInHdrErrors,
       "ipv6IfStatsInTooBigErrors": ipv6IfStatsInTooBigErrors,
       "ipv6IfStatsInNoRoutes": ipv6IfStatsInNoRoutes,
       "ipv6IfStatsInAddrErrors": ipv6IfStatsInAddrErrors,
       "ipv6IfStatsInUnknownProtos": ipv6IfStatsInUnknownProtos,
       "ipv6IfStatsInTruncatedPkts": ipv6IfStatsInTruncatedPkts,
       "ipv6IfStatsInDiscards": ipv6IfStatsInDiscards,
       "ipv6IfStatsInDelivers": ipv6IfStatsInDelivers,
       "ipv6IfStatsOutForwDatagrams": ipv6IfStatsOutForwDatagrams,
       "ipv6IfStatsOutRequests": ipv6IfStatsOutRequests,
       "ipv6IfStatsOutDiscards": ipv6IfStatsOutDiscards,
       "ipv6IfStatsOutFragOKs": ipv6IfStatsOutFragOKs,
       "ipv6IfStatsOutFragFails": ipv6IfStatsOutFragFails,
       "ipv6IfStatsOutFragCreates": ipv6IfStatsOutFragCreates,
       "ipv6IfStatsReasmReqds": ipv6IfStatsReasmReqds,
       "ipv6IfStatsReasmOKs": ipv6IfStatsReasmOKs,
       "ipv6IfStatsReasmFails": ipv6IfStatsReasmFails,
       "ipv6IfStatsInMcastPkts": ipv6IfStatsInMcastPkts,
       "ipv6IfStatsOutMcastPkts": ipv6IfStatsOutMcastPkts,
       "ipv6AddrPrefixTable": ipv6AddrPrefixTable,
       "ipv6AddrPrefixEntry": ipv6AddrPrefixEntry,
       "ipv6AddrPrefix": ipv6AddrPrefix,
       "ipv6AddrPrefixLength": ipv6AddrPrefixLength,
       "ipv6AddrPrefixOnLinkFlag": ipv6AddrPrefixOnLinkFlag,
       "ipv6AddrPrefixAutonomousFlag": ipv6AddrPrefixAutonomousFlag,
       "ipv6AddrPrefixAdvPreferredLifetime": ipv6AddrPrefixAdvPreferredLifetime,
       "ipv6AddrPrefixAdvValidLifetime": ipv6AddrPrefixAdvValidLifetime,
       "ipv6AddrTable": ipv6AddrTable,
       "ipv6AddrEntry": ipv6AddrEntry,
       "ipv6AddrAddress": ipv6AddrAddress,
       "ipv6AddrPfxLength": ipv6AddrPfxLength,
       "ipv6AddrType": ipv6AddrType,
       "ipv6AddrAnycastFlag": ipv6AddrAnycastFlag,
       "ipv6AddrStatus": ipv6AddrStatus,
       "ipv6RouteNumber": ipv6RouteNumber,
       "ipv6DiscardedRoutes": ipv6DiscardedRoutes,
       "ipv6RouteTable": ipv6RouteTable,
       "ipv6RouteEntry": ipv6RouteEntry,
       "ipv6RouteDest": ipv6RouteDest,
       "ipv6RoutePfxLength": ipv6RoutePfxLength,
       "ipv6RouteIndex": ipv6RouteIndex,
       "ipv6RouteIfIndex": ipv6RouteIfIndex,
       "ipv6RouteNextHop": ipv6RouteNextHop,
       "ipv6RouteType": ipv6RouteType,
       "ipv6RouteProtocol": ipv6RouteProtocol,
       "ipv6RoutePolicy": ipv6RoutePolicy,
       "ipv6RouteAge": ipv6RouteAge,
       "ipv6RouteNextHopRDI": ipv6RouteNextHopRDI,
       "ipv6RouteMetric": ipv6RouteMetric,
       "ipv6RouteWeight": ipv6RouteWeight,
       "ipv6RouteInfo": ipv6RouteInfo,
       "ipv6RouteValid": ipv6RouteValid,
       "ipv6NetToMediaTable": ipv6NetToMediaTable,
       "ipv6NetToMediaEntry": ipv6NetToMediaEntry,
       "ipv6NetToMediaNetAddress": ipv6NetToMediaNetAddress,
       "ipv6NetToMediaPhysAddress": ipv6NetToMediaPhysAddress,
       "ipv6NetToMediaType": ipv6NetToMediaType,
       "ipv6IfNetToMediaState": ipv6IfNetToMediaState,
       "ipv6IfNetToMediaLastUpdated": ipv6IfNetToMediaLastUpdated,
       "ipv6NetToMediaValid": ipv6NetToMediaValid,
       "ipv6Notifications": ipv6Notifications,
       "ipv6NotificationPrefix": ipv6NotificationPrefix,
       "ipv6IfStateChange": ipv6IfStateChange,
       "ipv6Conformance": ipv6Conformance,
       "ipv6Compliances": ipv6Compliances,
       "ipv6Compliance": ipv6Compliance,
       "ipv6Groups": ipv6Groups,
       "ipv6GeneralGroup": ipv6GeneralGroup,
       "ipv6NotificationGroup": ipv6NotificationGroup}
)
