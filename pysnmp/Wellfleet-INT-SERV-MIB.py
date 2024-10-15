# SNMP MIB module (Wellfleet-INT-SERV-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-INT-SERV-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:16:25 2024
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

(wfIntegratedServicesGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfIntegratedServicesGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfReservationsResourcesGroup_ObjectIdentity = ObjectIdentity
wfReservationsResourcesGroup = _WfReservationsResourcesGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 2)
)
_WfTxLineRscGroup_ObjectIdentity = ObjectIdentity
wfTxLineRscGroup = _WfTxLineRscGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 2, 1)
)
_WfTxLineRscTable_Object = MibTable
wfTxLineRscTable = _WfTxLineRscTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 2, 1, 1)
)
if mibBuilder.loadTexts:
    wfTxLineRscTable.setStatus("mandatory")
_WfTxLineRscEntry_Object = MibTableRow
wfTxLineRscEntry = _WfTxLineRscEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 2, 1, 1, 1)
)
wfTxLineRscEntry.setIndexNames(
    (0, "Wellfleet-INT-SERV-MIB", "wfTxLineRscLineNumber"),
)
if mibBuilder.loadTexts:
    wfTxLineRscEntry.setStatus("mandatory")


class _WfTxLineRscKillReservations_Type(Integer32):
    """Custom type wfTxLineRscKillReservations based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("keep", 1),
          ("kill", 2))
    )


_WfTxLineRscKillReservations_Type.__name__ = "Integer32"
_WfTxLineRscKillReservations_Object = MibTableColumn
wfTxLineRscKillReservations = _WfTxLineRscKillReservations_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 2, 1, 1, 1, 1),
    _WfTxLineRscKillReservations_Type()
)
wfTxLineRscKillReservations.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTxLineRscKillReservations.setStatus("mandatory")
_WfTxLineRscLineNumber_Type = Integer32
_WfTxLineRscLineNumber_Object = MibTableColumn
wfTxLineRscLineNumber = _WfTxLineRscLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 2, 1, 1, 1, 2),
    _WfTxLineRscLineNumber_Type()
)
wfTxLineRscLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTxLineRscLineNumber.setStatus("mandatory")
_WfTxLineRscReservableBandwidth_Type = Gauge32
_WfTxLineRscReservableBandwidth_Object = MibTableColumn
wfTxLineRscReservableBandwidth = _WfTxLineRscReservableBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 2, 1, 1, 1, 3),
    _WfTxLineRscReservableBandwidth_Type()
)
wfTxLineRscReservableBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTxLineRscReservableBandwidth.setStatus("mandatory")
_WfTxLineRscReservedBandwidth_Type = Gauge32
_WfTxLineRscReservedBandwidth_Object = MibTableColumn
wfTxLineRscReservedBandwidth = _WfTxLineRscReservedBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 2, 1, 1, 1, 4),
    _WfTxLineRscReservedBandwidth_Type()
)
wfTxLineRscReservedBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTxLineRscReservedBandwidth.setStatus("mandatory")
_WfTxLineRscGuaranteedFlows_Type = Gauge32
_WfTxLineRscGuaranteedFlows_Object = MibTableColumn
wfTxLineRscGuaranteedFlows = _WfTxLineRscGuaranteedFlows_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 2, 1, 1, 1, 5),
    _WfTxLineRscGuaranteedFlows_Type()
)
wfTxLineRscGuaranteedFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTxLineRscGuaranteedFlows.setStatus("mandatory")
_WfTxLineRscGuaranteedPackets_Type = Counter32
_WfTxLineRscGuaranteedPackets_Object = MibTableColumn
wfTxLineRscGuaranteedPackets = _WfTxLineRscGuaranteedPackets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 2, 1, 1, 1, 6),
    _WfTxLineRscGuaranteedPackets_Type()
)
wfTxLineRscGuaranteedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTxLineRscGuaranteedPackets.setStatus("mandatory")
_WfTxLineRscGuaranteedBytes_Type = Counter32
_WfTxLineRscGuaranteedBytes_Object = MibTableColumn
wfTxLineRscGuaranteedBytes = _WfTxLineRscGuaranteedBytes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 2, 1, 1, 1, 7),
    _WfTxLineRscGuaranteedBytes_Type()
)
wfTxLineRscGuaranteedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTxLineRscGuaranteedBytes.setStatus("mandatory")
_WfTxLineRscGuaranteedPolicedPackets_Type = Counter32
_WfTxLineRscGuaranteedPolicedPackets_Object = MibTableColumn
wfTxLineRscGuaranteedPolicedPackets = _WfTxLineRscGuaranteedPolicedPackets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 2, 1, 1, 1, 8),
    _WfTxLineRscGuaranteedPolicedPackets_Type()
)
wfTxLineRscGuaranteedPolicedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTxLineRscGuaranteedPolicedPackets.setStatus("mandatory")
_WfTxLineRscGuaranteedPolicedBytes_Type = Counter32
_WfTxLineRscGuaranteedPolicedBytes_Object = MibTableColumn
wfTxLineRscGuaranteedPolicedBytes = _WfTxLineRscGuaranteedPolicedBytes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 2, 1, 1, 1, 9),
    _WfTxLineRscGuaranteedPolicedBytes_Type()
)
wfTxLineRscGuaranteedPolicedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTxLineRscGuaranteedPolicedBytes.setStatus("mandatory")
_WfTxLineRscGuaranteedBandwidth_Type = Gauge32
_WfTxLineRscGuaranteedBandwidth_Object = MibTableColumn
wfTxLineRscGuaranteedBandwidth = _WfTxLineRscGuaranteedBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 2, 1, 1, 1, 10),
    _WfTxLineRscGuaranteedBandwidth_Type()
)
wfTxLineRscGuaranteedBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTxLineRscGuaranteedBandwidth.setStatus("mandatory")
_WfTxLineRscGuaranteedAvgBandwidth_Type = Gauge32
_WfTxLineRscGuaranteedAvgBandwidth_Object = MibTableColumn
wfTxLineRscGuaranteedAvgBandwidth = _WfTxLineRscGuaranteedAvgBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 2, 1, 1, 1, 11),
    _WfTxLineRscGuaranteedAvgBandwidth_Type()
)
wfTxLineRscGuaranteedAvgBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTxLineRscGuaranteedAvgBandwidth.setStatus("mandatory")
_WfTxLineRscGuaranteedMaxBandwidth_Type = Gauge32
_WfTxLineRscGuaranteedMaxBandwidth_Object = MibTableColumn
wfTxLineRscGuaranteedMaxBandwidth = _WfTxLineRscGuaranteedMaxBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 2, 1, 1, 1, 12),
    _WfTxLineRscGuaranteedMaxBandwidth_Type()
)
wfTxLineRscGuaranteedMaxBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTxLineRscGuaranteedMaxBandwidth.setStatus("mandatory")
_WfTxLineRscGuaranteedAvgPacketDelay_Type = Gauge32
_WfTxLineRscGuaranteedAvgPacketDelay_Object = MibTableColumn
wfTxLineRscGuaranteedAvgPacketDelay = _WfTxLineRscGuaranteedAvgPacketDelay_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 2, 1, 1, 1, 13),
    _WfTxLineRscGuaranteedAvgPacketDelay_Type()
)
wfTxLineRscGuaranteedAvgPacketDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTxLineRscGuaranteedAvgPacketDelay.setStatus("mandatory")
_WfTxLineRscGuaranteedMaxPacketDelay_Type = Gauge32
_WfTxLineRscGuaranteedMaxPacketDelay_Object = MibTableColumn
wfTxLineRscGuaranteedMaxPacketDelay = _WfTxLineRscGuaranteedMaxPacketDelay_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 2, 1, 1, 1, 14),
    _WfTxLineRscGuaranteedMaxPacketDelay_Type()
)
wfTxLineRscGuaranteedMaxPacketDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTxLineRscGuaranteedMaxPacketDelay.setStatus("mandatory")
_WfTxLineRscUnreservedPolicedPackets_Type = Counter32
_WfTxLineRscUnreservedPolicedPackets_Object = MibTableColumn
wfTxLineRscUnreservedPolicedPackets = _WfTxLineRscUnreservedPolicedPackets_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 2, 1, 1, 1, 15),
    _WfTxLineRscUnreservedPolicedPackets_Type()
)
wfTxLineRscUnreservedPolicedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTxLineRscUnreservedPolicedPackets.setStatus("mandatory")
_WfTxLineRscUnreservedPolicedBytes_Type = Counter32
_WfTxLineRscUnreservedPolicedBytes_Object = MibTableColumn
wfTxLineRscUnreservedPolicedBytes = _WfTxLineRscUnreservedPolicedBytes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 2, 1, 1, 1, 16),
    _WfTxLineRscUnreservedPolicedBytes_Type()
)
wfTxLineRscUnreservedPolicedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTxLineRscUnreservedPolicedBytes.setStatus("mandatory")
_WfTxLineRscCfgTable_Object = MibTable
wfTxLineRscCfgTable = _WfTxLineRscCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 2, 1, 3)
)
if mibBuilder.loadTexts:
    wfTxLineRscCfgTable.setStatus("mandatory")
_WfTxLineRscCfgEntry_Object = MibTableRow
wfTxLineRscCfgEntry = _WfTxLineRscCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 2, 1, 3, 1)
)
wfTxLineRscCfgEntry.setIndexNames(
    (0, "Wellfleet-INT-SERV-MIB", "wfTxLineRscCfgLineNumber"),
)
if mibBuilder.loadTexts:
    wfTxLineRscCfgEntry.setStatus("mandatory")


class _WfTxLineRscCfgDelete_Type(Integer32):
    """Custom type wfTxLineRscCfgDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfTxLineRscCfgDelete_Type.__name__ = "Integer32"
_WfTxLineRscCfgDelete_Object = MibTableColumn
wfTxLineRscCfgDelete = _WfTxLineRscCfgDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 2, 1, 3, 1, 1),
    _WfTxLineRscCfgDelete_Type()
)
wfTxLineRscCfgDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTxLineRscCfgDelete.setStatus("mandatory")
_WfTxLineRscCfgLineNumber_Type = Integer32
_WfTxLineRscCfgLineNumber_Object = MibTableColumn
wfTxLineRscCfgLineNumber = _WfTxLineRscCfgLineNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 2, 1, 3, 1, 2),
    _WfTxLineRscCfgLineNumber_Type()
)
wfTxLineRscCfgLineNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTxLineRscCfgLineNumber.setStatus("mandatory")
_WfTxLineRscCfgEstBandwidth_Type = Integer32
_WfTxLineRscCfgEstBandwidth_Object = MibTableColumn
wfTxLineRscCfgEstBandwidth = _WfTxLineRscCfgEstBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 2, 1, 3, 1, 3),
    _WfTxLineRscCfgEstBandwidth_Type()
)
wfTxLineRscCfgEstBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTxLineRscCfgEstBandwidth.setStatus("mandatory")
_WfTxLineRscCfgResvBandwidth_Type = Integer32
_WfTxLineRscCfgResvBandwidth_Object = MibTableColumn
wfTxLineRscCfgResvBandwidth = _WfTxLineRscCfgResvBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 2, 1, 3, 1, 4),
    _WfTxLineRscCfgResvBandwidth_Type()
)
wfTxLineRscCfgResvBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTxLineRscCfgResvBandwidth.setStatus("mandatory")


class _WfTxLineRscCfgResvTrafficAlgorithm_Type(Integer32):
    """Custom type wfTxLineRscCfgResvTrafficAlgorithm based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("priority", 2))
    )


_WfTxLineRscCfgResvTrafficAlgorithm_Type.__name__ = "Integer32"
_WfTxLineRscCfgResvTrafficAlgorithm_Object = MibTableColumn
wfTxLineRscCfgResvTrafficAlgorithm = _WfTxLineRscCfgResvTrafficAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 2, 1, 3, 1, 5),
    _WfTxLineRscCfgResvTrafficAlgorithm_Type()
)
wfTxLineRscCfgResvTrafficAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTxLineRscCfgResvTrafficAlgorithm.setStatus("mandatory")


class _WfTxLineRscCfgResvPolicingAlgorithm_Type(Integer32):
    """Custom type wfTxLineRscCfgResvPolicingAlgorithm based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lbucket", 2),
          ("none", 1))
    )


_WfTxLineRscCfgResvPolicingAlgorithm_Type.__name__ = "Integer32"
_WfTxLineRscCfgResvPolicingAlgorithm_Object = MibTableColumn
wfTxLineRscCfgResvPolicingAlgorithm = _WfTxLineRscCfgResvPolicingAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 2, 1, 3, 1, 6),
    _WfTxLineRscCfgResvPolicingAlgorithm_Type()
)
wfTxLineRscCfgResvPolicingAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTxLineRscCfgResvPolicingAlgorithm.setStatus("mandatory")


class _WfTxLineRscCfgBandwidthInterval_Type(Integer32):
    """Custom type wfTxLineRscCfgBandwidthInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            10
        )
    )
    namedValues = NamedValues(
        ("default", 10)
    )


_WfTxLineRscCfgBandwidthInterval_Type.__name__ = "Integer32"
_WfTxLineRscCfgBandwidthInterval_Object = MibTableColumn
wfTxLineRscCfgBandwidthInterval = _WfTxLineRscCfgBandwidthInterval_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 2, 1, 3, 1, 7),
    _WfTxLineRscCfgBandwidthInterval_Type()
)
wfTxLineRscCfgBandwidthInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTxLineRscCfgBandwidthInterval.setStatus("mandatory")


class _WfTxLineRscCfgInflateReservations_Type(Integer32):
    """Custom type wfTxLineRscCfgInflateReservations based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_WfTxLineRscCfgInflateReservations_Type.__name__ = "Integer32"
_WfTxLineRscCfgInflateReservations_Object = MibTableColumn
wfTxLineRscCfgInflateReservations = _WfTxLineRscCfgInflateReservations_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 2, 1, 3, 1, 8),
    _WfTxLineRscCfgInflateReservations_Type()
)
wfTxLineRscCfgInflateReservations.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTxLineRscCfgInflateReservations.setStatus("mandatory")


class _WfTxLineRscCfgUnreservedPolicingAlgorithm_Type(Integer32):
    """Custom type wfTxLineRscCfgUnreservedPolicingAlgorithm based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lbucket", 2),
          ("qlimit", 1))
    )


_WfTxLineRscCfgUnreservedPolicingAlgorithm_Type.__name__ = "Integer32"
_WfTxLineRscCfgUnreservedPolicingAlgorithm_Object = MibTableColumn
wfTxLineRscCfgUnreservedPolicingAlgorithm = _WfTxLineRscCfgUnreservedPolicingAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 2, 1, 3, 1, 9),
    _WfTxLineRscCfgUnreservedPolicingAlgorithm_Type()
)
wfTxLineRscCfgUnreservedPolicingAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTxLineRscCfgUnreservedPolicingAlgorithm.setStatus("mandatory")


class _WfTxLineRscCfgUnreservedQueueLength_Type(Integer32):
    """Custom type wfTxLineRscCfgUnreservedQueueLength based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            20
        )
    )
    namedValues = NamedValues(
        ("default", 20)
    )


_WfTxLineRscCfgUnreservedQueueLength_Type.__name__ = "Integer32"
_WfTxLineRscCfgUnreservedQueueLength_Object = MibTableColumn
wfTxLineRscCfgUnreservedQueueLength = _WfTxLineRscCfgUnreservedQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 2, 1, 3, 1, 10),
    _WfTxLineRscCfgUnreservedQueueLength_Type()
)
wfTxLineRscCfgUnreservedQueueLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTxLineRscCfgUnreservedQueueLength.setStatus("mandatory")


class _WfTxLineRscCfgMultiLineSelectAlgorithm_Type(Integer32):
    """Custom type wfTxLineRscCfgMultiLineSelectAlgorithm based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("first", 1),
          ("round", 2))
    )


_WfTxLineRscCfgMultiLineSelectAlgorithm_Type.__name__ = "Integer32"
_WfTxLineRscCfgMultiLineSelectAlgorithm_Object = MibTableColumn
wfTxLineRscCfgMultiLineSelectAlgorithm = _WfTxLineRscCfgMultiLineSelectAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 2, 1, 3, 1, 11),
    _WfTxLineRscCfgMultiLineSelectAlgorithm_Type()
)
wfTxLineRscCfgMultiLineSelectAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTxLineRscCfgMultiLineSelectAlgorithm.setStatus("mandatory")
_WfTxLineRscCfgMultiLineThresholdBandwidth_Type = Integer32
_WfTxLineRscCfgMultiLineThresholdBandwidth_Object = MibTableColumn
wfTxLineRscCfgMultiLineThresholdBandwidth = _WfTxLineRscCfgMultiLineThresholdBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 2, 1, 3, 1, 12),
    _WfTxLineRscCfgMultiLineThresholdBandwidth_Type()
)
wfTxLineRscCfgMultiLineThresholdBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTxLineRscCfgMultiLineThresholdBandwidth.setStatus("mandatory")


class _WfTxLineRscCfgResvLatency_Type(Integer32):
    """Custom type wfTxLineRscCfgResvLatency based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WfTxLineRscCfgResvLatency_Type.__name__ = "Integer32"
_WfTxLineRscCfgResvLatency_Object = MibTableColumn
wfTxLineRscCfgResvLatency = _WfTxLineRscCfgResvLatency_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 2, 1, 3, 1, 13),
    _WfTxLineRscCfgResvLatency_Type()
)
wfTxLineRscCfgResvLatency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTxLineRscCfgResvLatency.setStatus("mandatory")


class _WfTxLineRscCfgLargestBandwidth_Type(Integer32):
    """Custom type wfTxLineRscCfgLargestBandwidth based on Integer32"""
    defaultValue = 0


_WfTxLineRscCfgLargestBandwidth_Object = MibTableColumn
wfTxLineRscCfgLargestBandwidth = _WfTxLineRscCfgLargestBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 2, 1, 3, 1, 14),
    _WfTxLineRscCfgLargestBandwidth_Type()
)
wfTxLineRscCfgLargestBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTxLineRscCfgLargestBandwidth.setStatus("mandatory")


class _WfTxLineRscCfgLargestBuffer_Type(Integer32):
    """Custom type wfTxLineRscCfgLargestBuffer based on Integer32"""
    defaultValue = 0


_WfTxLineRscCfgLargestBuffer_Object = MibTableColumn
wfTxLineRscCfgLargestBuffer = _WfTxLineRscCfgLargestBuffer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 2, 1, 3, 1, 15),
    _WfTxLineRscCfgLargestBuffer_Type()
)
wfTxLineRscCfgLargestBuffer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTxLineRscCfgLargestBuffer.setStatus("mandatory")
_WfReservationsFlowspecGroup_ObjectIdentity = ObjectIdentity
wfReservationsFlowspecGroup = _WfReservationsFlowspecGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 3)
)
_WfFlowspecSt2V3Table_Object = MibTable
wfFlowspecSt2V3Table = _WfFlowspecSt2V3Table_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 3, 1)
)
if mibBuilder.loadTexts:
    wfFlowspecSt2V3Table.setStatus("mandatory")
_WfFlowspecSt2V3Entry_Object = MibTableRow
wfFlowspecSt2V3Entry = _WfFlowspecSt2V3Entry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 3, 1, 1)
)
wfFlowspecSt2V3Entry.setIndexNames(
    (0, "Wellfleet-INT-SERV-MIB", "wfFlowspecSt2V3Index"),
)
if mibBuilder.loadTexts:
    wfFlowspecSt2V3Entry.setStatus("mandatory")
_WfFlowspecSt2V3Index_Type = Integer32
_WfFlowspecSt2V3Index_Object = MibTableColumn
wfFlowspecSt2V3Index = _WfFlowspecSt2V3Index_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 3, 1, 1, 1),
    _WfFlowspecSt2V3Index_Type()
)
wfFlowspecSt2V3Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFlowspecSt2V3Index.setStatus("mandatory")
_WfFlowspecSt2V3Version_Type = Integer32
_WfFlowspecSt2V3Version_Object = MibTableColumn
wfFlowspecSt2V3Version = _WfFlowspecSt2V3Version_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 3, 1, 1, 2),
    _WfFlowspecSt2V3Version_Type()
)
wfFlowspecSt2V3Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFlowspecSt2V3Version.setStatus("mandatory")
_WfFlowspecSt2V3DutyFactor_Type = Integer32
_WfFlowspecSt2V3DutyFactor_Object = MibTableColumn
wfFlowspecSt2V3DutyFactor = _WfFlowspecSt2V3DutyFactor_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 3, 1, 1, 3),
    _WfFlowspecSt2V3DutyFactor_Type()
)
wfFlowspecSt2V3DutyFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFlowspecSt2V3DutyFactor.setStatus("mandatory")
_WfFlowspecSt2V3ErrorRate_Type = Integer32
_WfFlowspecSt2V3ErrorRate_Object = MibTableColumn
wfFlowspecSt2V3ErrorRate = _WfFlowspecSt2V3ErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 3, 1, 1, 4),
    _WfFlowspecSt2V3ErrorRate_Type()
)
wfFlowspecSt2V3ErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFlowspecSt2V3ErrorRate.setStatus("mandatory")
_WfFlowspecSt2V3Precedence_Type = Integer32
_WfFlowspecSt2V3Precedence_Object = MibTableColumn
wfFlowspecSt2V3Precedence = _WfFlowspecSt2V3Precedence_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 3, 1, 1, 5),
    _WfFlowspecSt2V3Precedence_Type()
)
wfFlowspecSt2V3Precedence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFlowspecSt2V3Precedence.setStatus("mandatory")
_WfFlowspecSt2V3Reliability_Type = Integer32
_WfFlowspecSt2V3Reliability_Object = MibTableColumn
wfFlowspecSt2V3Reliability = _WfFlowspecSt2V3Reliability_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 3, 1, 1, 6),
    _WfFlowspecSt2V3Reliability_Type()
)
wfFlowspecSt2V3Reliability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFlowspecSt2V3Reliability.setStatus("mandatory")
_WfFlowspecSt2V3Tradeoffs_Type = Integer32
_WfFlowspecSt2V3Tradeoffs_Object = MibTableColumn
wfFlowspecSt2V3Tradeoffs = _WfFlowspecSt2V3Tradeoffs_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 3, 1, 1, 7),
    _WfFlowspecSt2V3Tradeoffs_Type()
)
wfFlowspecSt2V3Tradeoffs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFlowspecSt2V3Tradeoffs.setStatus("mandatory")
_WfFlowspecSt2V3RecoveryTimeout_Type = Integer32
_WfFlowspecSt2V3RecoveryTimeout_Object = MibTableColumn
wfFlowspecSt2V3RecoveryTimeout = _WfFlowspecSt2V3RecoveryTimeout_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 3, 1, 1, 8),
    _WfFlowspecSt2V3RecoveryTimeout_Type()
)
wfFlowspecSt2V3RecoveryTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFlowspecSt2V3RecoveryTimeout.setStatus("mandatory")
_WfFlowspecSt2V3LimitOnCost_Type = Integer32
_WfFlowspecSt2V3LimitOnCost_Object = MibTableColumn
wfFlowspecSt2V3LimitOnCost = _WfFlowspecSt2V3LimitOnCost_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 3, 1, 1, 9),
    _WfFlowspecSt2V3LimitOnCost_Type()
)
wfFlowspecSt2V3LimitOnCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFlowspecSt2V3LimitOnCost.setStatus("mandatory")
_WfFlowspecSt2V3LimitOnDelay_Type = Integer32
_WfFlowspecSt2V3LimitOnDelay_Object = MibTableColumn
wfFlowspecSt2V3LimitOnDelay = _WfFlowspecSt2V3LimitOnDelay_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 3, 1, 1, 10),
    _WfFlowspecSt2V3LimitOnDelay_Type()
)
wfFlowspecSt2V3LimitOnDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFlowspecSt2V3LimitOnDelay.setStatus("mandatory")
_WfFlowspecSt2V3LimitOnPDUBytes_Type = Integer32
_WfFlowspecSt2V3LimitOnPDUBytes_Object = MibTableColumn
wfFlowspecSt2V3LimitOnPDUBytes = _WfFlowspecSt2V3LimitOnPDUBytes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 3, 1, 1, 11),
    _WfFlowspecSt2V3LimitOnPDUBytes_Type()
)
wfFlowspecSt2V3LimitOnPDUBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFlowspecSt2V3LimitOnPDUBytes.setStatus("mandatory")
_WfFlowspecSt2V3LimitOnPDURate_Type = Integer32
_WfFlowspecSt2V3LimitOnPDURate_Object = MibTableColumn
wfFlowspecSt2V3LimitOnPDURate = _WfFlowspecSt2V3LimitOnPDURate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 3, 1, 1, 12),
    _WfFlowspecSt2V3LimitOnPDURate_Type()
)
wfFlowspecSt2V3LimitOnPDURate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFlowspecSt2V3LimitOnPDURate.setStatus("mandatory")
_WfFlowspecSt2V3MinBytesXRate_Type = Integer32
_WfFlowspecSt2V3MinBytesXRate_Object = MibTableColumn
wfFlowspecSt2V3MinBytesXRate = _WfFlowspecSt2V3MinBytesXRate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 3, 1, 1, 13),
    _WfFlowspecSt2V3MinBytesXRate_Type()
)
wfFlowspecSt2V3MinBytesXRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFlowspecSt2V3MinBytesXRate.setStatus("mandatory")
_WfFlowspecSt2V3AccdMeanDelay_Type = Integer32
_WfFlowspecSt2V3AccdMeanDelay_Object = MibTableColumn
wfFlowspecSt2V3AccdMeanDelay = _WfFlowspecSt2V3AccdMeanDelay_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 3, 1, 1, 14),
    _WfFlowspecSt2V3AccdMeanDelay_Type()
)
wfFlowspecSt2V3AccdMeanDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFlowspecSt2V3AccdMeanDelay.setStatus("mandatory")
_WfFlowspecSt2V3AccdDelayVariance_Type = Integer32
_WfFlowspecSt2V3AccdDelayVariance_Object = MibTableColumn
wfFlowspecSt2V3AccdDelayVariance = _WfFlowspecSt2V3AccdDelayVariance_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 3, 1, 1, 15),
    _WfFlowspecSt2V3AccdDelayVariance_Type()
)
wfFlowspecSt2V3AccdDelayVariance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFlowspecSt2V3AccdDelayVariance.setStatus("mandatory")
_WfFlowspecSt2V3DesPDUBytes_Type = Integer32
_WfFlowspecSt2V3DesPDUBytes_Object = MibTableColumn
wfFlowspecSt2V3DesPDUBytes = _WfFlowspecSt2V3DesPDUBytes_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 3, 1, 1, 16),
    _WfFlowspecSt2V3DesPDUBytes_Type()
)
wfFlowspecSt2V3DesPDUBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFlowspecSt2V3DesPDUBytes.setStatus("mandatory")
_WfFlowspecSt2V3DesPDURate_Type = Integer32
_WfFlowspecSt2V3DesPDURate_Object = MibTableColumn
wfFlowspecSt2V3DesPDURate = _WfFlowspecSt2V3DesPDURate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 3, 1, 1, 17),
    _WfFlowspecSt2V3DesPDURate_Type()
)
wfFlowspecSt2V3DesPDURate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfFlowspecSt2V3DesPDURate.setStatus("mandatory")
_WfIntSrvIfFlowGroup_ObjectIdentity = ObjectIdentity
wfIntSrvIfFlowGroup = _WfIntSrvIfFlowGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 4)
)
_WfIntSrvIfFlowTable_Object = MibTable
wfIntSrvIfFlowTable = _WfIntSrvIfFlowTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 4, 1)
)
if mibBuilder.loadTexts:
    wfIntSrvIfFlowTable.setStatus("mandatory")
_WfIntSrvIfFlowEntry_Object = MibTableRow
wfIntSrvIfFlowEntry = _WfIntSrvIfFlowEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 4, 1, 1)
)
wfIntSrvIfFlowEntry.setIndexNames(
    (0, "Wellfleet-INT-SERV-MIB", "wfIntSrvIfFlowDestination"),
    (0, "Wellfleet-INT-SERV-MIB", "wfIntSrvIfFlowDestinationProtocol"),
    (0, "Wellfleet-INT-SERV-MIB", "wfIntSrvIfFlowDestinationPort"),
    (0, "Wellfleet-INT-SERV-MIB", "wfIntSrvIfFlowSource"),
    (0, "Wellfleet-INT-SERV-MIB", "wfIntSrvIfFlowSourcePort"),
    (0, "Wellfleet-INT-SERV-MIB", "wfIntSrvIfFlowCct"),
)
if mibBuilder.loadTexts:
    wfIntSrvIfFlowEntry.setStatus("mandatory")
_WfIntSrvIfFlowDestination_Type = IpAddress
_WfIntSrvIfFlowDestination_Object = MibTableColumn
wfIntSrvIfFlowDestination = _WfIntSrvIfFlowDestination_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 4, 1, 1, 1),
    _WfIntSrvIfFlowDestination_Type()
)
wfIntSrvIfFlowDestination.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIntSrvIfFlowDestination.setStatus("mandatory")


class _WfIntSrvIfFlowDestinationProtocol_Type(Integer32):
    """Custom type wfIntSrvIfFlowDestinationProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_WfIntSrvIfFlowDestinationProtocol_Type.__name__ = "Integer32"
_WfIntSrvIfFlowDestinationProtocol_Object = MibTableColumn
wfIntSrvIfFlowDestinationProtocol = _WfIntSrvIfFlowDestinationProtocol_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 4, 1, 1, 2),
    _WfIntSrvIfFlowDestinationProtocol_Type()
)
wfIntSrvIfFlowDestinationProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIntSrvIfFlowDestinationProtocol.setStatus("mandatory")


class _WfIntSrvIfFlowDestinationPort_Type(Integer32):
    """Custom type wfIntSrvIfFlowDestinationPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WfIntSrvIfFlowDestinationPort_Type.__name__ = "Integer32"
_WfIntSrvIfFlowDestinationPort_Object = MibTableColumn
wfIntSrvIfFlowDestinationPort = _WfIntSrvIfFlowDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 4, 1, 1, 3),
    _WfIntSrvIfFlowDestinationPort_Type()
)
wfIntSrvIfFlowDestinationPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIntSrvIfFlowDestinationPort.setStatus("mandatory")
_WfIntSrvIfFlowSource_Type = IpAddress
_WfIntSrvIfFlowSource_Object = MibTableColumn
wfIntSrvIfFlowSource = _WfIntSrvIfFlowSource_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 4, 1, 1, 4),
    _WfIntSrvIfFlowSource_Type()
)
wfIntSrvIfFlowSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIntSrvIfFlowSource.setStatus("mandatory")


class _WfIntSrvIfFlowSourcePort_Type(Integer32):
    """Custom type wfIntSrvIfFlowSourcePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WfIntSrvIfFlowSourcePort_Type.__name__ = "Integer32"
_WfIntSrvIfFlowSourcePort_Object = MibTableColumn
wfIntSrvIfFlowSourcePort = _WfIntSrvIfFlowSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 4, 1, 1, 5),
    _WfIntSrvIfFlowSourcePort_Type()
)
wfIntSrvIfFlowSourcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIntSrvIfFlowSourcePort.setStatus("mandatory")


class _WfIntSrvIfFlowRate_Type(Integer32):
    """Custom type wfIntSrvIfFlowRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WfIntSrvIfFlowRate_Type.__name__ = "Integer32"
_WfIntSrvIfFlowRate_Object = MibTableColumn
wfIntSrvIfFlowRate = _WfIntSrvIfFlowRate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 4, 1, 1, 6),
    _WfIntSrvIfFlowRate_Type()
)
wfIntSrvIfFlowRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIntSrvIfFlowRate.setStatus("mandatory")
_WfIntSrvIfFlowWeight_Type = Integer32
_WfIntSrvIfFlowWeight_Object = MibTableColumn
wfIntSrvIfFlowWeight = _WfIntSrvIfFlowWeight_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 4, 1, 1, 7),
    _WfIntSrvIfFlowWeight_Type()
)
wfIntSrvIfFlowWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIntSrvIfFlowWeight.setStatus("mandatory")
_WfIntSrvIfFlowQueue_Type = Integer32
_WfIntSrvIfFlowQueue_Object = MibTableColumn
wfIntSrvIfFlowQueue = _WfIntSrvIfFlowQueue_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 4, 1, 1, 8),
    _WfIntSrvIfFlowQueue_Type()
)
wfIntSrvIfFlowQueue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIntSrvIfFlowQueue.setStatus("mandatory")
_WfIntSrvIfFlowMin_Type = Integer32
_WfIntSrvIfFlowMin_Object = MibTableColumn
wfIntSrvIfFlowMin = _WfIntSrvIfFlowMin_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 4, 1, 1, 9),
    _WfIntSrvIfFlowMin_Type()
)
wfIntSrvIfFlowMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIntSrvIfFlowMin.setStatus("mandatory")
_WfIntSrvIfFlowCct_Type = Integer32
_WfIntSrvIfFlowCct_Object = MibTableColumn
wfIntSrvIfFlowCct = _WfIntSrvIfFlowCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 16, 4, 1, 1, 10),
    _WfIntSrvIfFlowCct_Type()
)
wfIntSrvIfFlowCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfIntSrvIfFlowCct.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-INT-SERV-MIB",
    **{"wfReservationsResourcesGroup": wfReservationsResourcesGroup,
       "wfTxLineRscGroup": wfTxLineRscGroup,
       "wfTxLineRscTable": wfTxLineRscTable,
       "wfTxLineRscEntry": wfTxLineRscEntry,
       "wfTxLineRscKillReservations": wfTxLineRscKillReservations,
       "wfTxLineRscLineNumber": wfTxLineRscLineNumber,
       "wfTxLineRscReservableBandwidth": wfTxLineRscReservableBandwidth,
       "wfTxLineRscReservedBandwidth": wfTxLineRscReservedBandwidth,
       "wfTxLineRscGuaranteedFlows": wfTxLineRscGuaranteedFlows,
       "wfTxLineRscGuaranteedPackets": wfTxLineRscGuaranteedPackets,
       "wfTxLineRscGuaranteedBytes": wfTxLineRscGuaranteedBytes,
       "wfTxLineRscGuaranteedPolicedPackets": wfTxLineRscGuaranteedPolicedPackets,
       "wfTxLineRscGuaranteedPolicedBytes": wfTxLineRscGuaranteedPolicedBytes,
       "wfTxLineRscGuaranteedBandwidth": wfTxLineRscGuaranteedBandwidth,
       "wfTxLineRscGuaranteedAvgBandwidth": wfTxLineRscGuaranteedAvgBandwidth,
       "wfTxLineRscGuaranteedMaxBandwidth": wfTxLineRscGuaranteedMaxBandwidth,
       "wfTxLineRscGuaranteedAvgPacketDelay": wfTxLineRscGuaranteedAvgPacketDelay,
       "wfTxLineRscGuaranteedMaxPacketDelay": wfTxLineRscGuaranteedMaxPacketDelay,
       "wfTxLineRscUnreservedPolicedPackets": wfTxLineRscUnreservedPolicedPackets,
       "wfTxLineRscUnreservedPolicedBytes": wfTxLineRscUnreservedPolicedBytes,
       "wfTxLineRscCfgTable": wfTxLineRscCfgTable,
       "wfTxLineRscCfgEntry": wfTxLineRscCfgEntry,
       "wfTxLineRscCfgDelete": wfTxLineRscCfgDelete,
       "wfTxLineRscCfgLineNumber": wfTxLineRscCfgLineNumber,
       "wfTxLineRscCfgEstBandwidth": wfTxLineRscCfgEstBandwidth,
       "wfTxLineRscCfgResvBandwidth": wfTxLineRscCfgResvBandwidth,
       "wfTxLineRscCfgResvTrafficAlgorithm": wfTxLineRscCfgResvTrafficAlgorithm,
       "wfTxLineRscCfgResvPolicingAlgorithm": wfTxLineRscCfgResvPolicingAlgorithm,
       "wfTxLineRscCfgBandwidthInterval": wfTxLineRscCfgBandwidthInterval,
       "wfTxLineRscCfgInflateReservations": wfTxLineRscCfgInflateReservations,
       "wfTxLineRscCfgUnreservedPolicingAlgorithm": wfTxLineRscCfgUnreservedPolicingAlgorithm,
       "wfTxLineRscCfgUnreservedQueueLength": wfTxLineRscCfgUnreservedQueueLength,
       "wfTxLineRscCfgMultiLineSelectAlgorithm": wfTxLineRscCfgMultiLineSelectAlgorithm,
       "wfTxLineRscCfgMultiLineThresholdBandwidth": wfTxLineRscCfgMultiLineThresholdBandwidth,
       "wfTxLineRscCfgResvLatency": wfTxLineRscCfgResvLatency,
       "wfTxLineRscCfgLargestBandwidth": wfTxLineRscCfgLargestBandwidth,
       "wfTxLineRscCfgLargestBuffer": wfTxLineRscCfgLargestBuffer,
       "wfReservationsFlowspecGroup": wfReservationsFlowspecGroup,
       "wfFlowspecSt2V3Table": wfFlowspecSt2V3Table,
       "wfFlowspecSt2V3Entry": wfFlowspecSt2V3Entry,
       "wfFlowspecSt2V3Index": wfFlowspecSt2V3Index,
       "wfFlowspecSt2V3Version": wfFlowspecSt2V3Version,
       "wfFlowspecSt2V3DutyFactor": wfFlowspecSt2V3DutyFactor,
       "wfFlowspecSt2V3ErrorRate": wfFlowspecSt2V3ErrorRate,
       "wfFlowspecSt2V3Precedence": wfFlowspecSt2V3Precedence,
       "wfFlowspecSt2V3Reliability": wfFlowspecSt2V3Reliability,
       "wfFlowspecSt2V3Tradeoffs": wfFlowspecSt2V3Tradeoffs,
       "wfFlowspecSt2V3RecoveryTimeout": wfFlowspecSt2V3RecoveryTimeout,
       "wfFlowspecSt2V3LimitOnCost": wfFlowspecSt2V3LimitOnCost,
       "wfFlowspecSt2V3LimitOnDelay": wfFlowspecSt2V3LimitOnDelay,
       "wfFlowspecSt2V3LimitOnPDUBytes": wfFlowspecSt2V3LimitOnPDUBytes,
       "wfFlowspecSt2V3LimitOnPDURate": wfFlowspecSt2V3LimitOnPDURate,
       "wfFlowspecSt2V3MinBytesXRate": wfFlowspecSt2V3MinBytesXRate,
       "wfFlowspecSt2V3AccdMeanDelay": wfFlowspecSt2V3AccdMeanDelay,
       "wfFlowspecSt2V3AccdDelayVariance": wfFlowspecSt2V3AccdDelayVariance,
       "wfFlowspecSt2V3DesPDUBytes": wfFlowspecSt2V3DesPDUBytes,
       "wfFlowspecSt2V3DesPDURate": wfFlowspecSt2V3DesPDURate,
       "wfIntSrvIfFlowGroup": wfIntSrvIfFlowGroup,
       "wfIntSrvIfFlowTable": wfIntSrvIfFlowTable,
       "wfIntSrvIfFlowEntry": wfIntSrvIfFlowEntry,
       "wfIntSrvIfFlowDestination": wfIntSrvIfFlowDestination,
       "wfIntSrvIfFlowDestinationProtocol": wfIntSrvIfFlowDestinationProtocol,
       "wfIntSrvIfFlowDestinationPort": wfIntSrvIfFlowDestinationPort,
       "wfIntSrvIfFlowSource": wfIntSrvIfFlowSource,
       "wfIntSrvIfFlowSourcePort": wfIntSrvIfFlowSourcePort,
       "wfIntSrvIfFlowRate": wfIntSrvIfFlowRate,
       "wfIntSrvIfFlowWeight": wfIntSrvIfFlowWeight,
       "wfIntSrvIfFlowQueue": wfIntSrvIfFlowQueue,
       "wfIntSrvIfFlowMin": wfIntSrvIfFlowMin,
       "wfIntSrvIfFlowCct": wfIntSrvIfFlowCct}
)
