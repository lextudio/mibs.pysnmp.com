# SNMP MIB module (ELFIQ-MODULE-LB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ELFIQ-MODULE-LB-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:36:52 2024
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

(linkBalancer,
 linkBalancerConformance) = mibBuilder.importSymbols(
    "ELFIQ-INC-MIB",
    "linkBalancer",
    "linkBalancerConformance")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(snmpTraps,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "snmpTraps")

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

linkBalancerComponent = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class VfiIndex(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )



class GmacIndex(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class ArpIndex(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



# MIB Managed Objects in the order of their OIDs

_VfiInfo_ObjectIdentity = ObjectIdentity
vfiInfo = _VfiInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 1)
)


class _VfiNumber_Type(Integer32):
    """Custom type vfiNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_VfiNumber_Type.__name__ = "Integer32"
_VfiNumber_Object = MibScalar
vfiNumber = _VfiNumber_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 1, 1),
    _VfiNumber_Type()
)
vfiNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vfiNumber.setStatus("current")
_VfiTable_Object = MibTable
vfiTable = _VfiTable_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    vfiTable.setStatus("current")
_VfiEntry_Object = MibTableRow
vfiEntry = _VfiEntry_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 1, 2, 1)
)
vfiEntry.setIndexNames(
    (0, "ELFIQ-MODULE-LB-MIB", "vfiIndex"),
)
if mibBuilder.loadTexts:
    vfiEntry.setStatus("current")
_VfiIndex_Type = VfiIndex
_VfiIndex_Object = MibTableColumn
vfiIndex = _VfiIndex_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 1, 2, 1, 1),
    _VfiIndex_Type()
)
vfiIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vfiIndex.setStatus("current")


class _VfiDescr_Type(DisplayString):
    """Custom type vfiDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_VfiDescr_Type.__name__ = "DisplayString"
_VfiDescr_Object = MibTableColumn
vfiDescr = _VfiDescr_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 1, 2, 1, 2),
    _VfiDescr_Type()
)
vfiDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vfiDescr.setStatus("current")


class _VfiActivated_Type(Integer32):
    """Custom type vfiActivated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("activated", 1),
          ("desactivated", 2))
    )


_VfiActivated_Type.__name__ = "Integer32"
_VfiActivated_Object = MibTableColumn
vfiActivated = _VfiActivated_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 1, 2, 1, 3),
    _VfiActivated_Type()
)
vfiActivated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vfiActivated.setStatus("current")


class _VfiStatus_Type(Integer32):
    """Custom type vfiStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pause", 2),
          ("resume", 1))
    )


_VfiStatus_Type.__name__ = "Integer32"
_VfiStatus_Object = MibTableColumn
vfiStatus = _VfiStatus_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 1, 2, 1, 4),
    _VfiStatus_Type()
)
vfiStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vfiStatus.setStatus("current")
_TotThroughputIn_Type = Counter64
_TotThroughputIn_Object = MibTableColumn
totThroughputIn = _TotThroughputIn_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 1, 2, 1, 5),
    _TotThroughputIn_Type()
)
totThroughputIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totThroughputIn.setStatus("current")
_TotThroughputOut_Type = Counter64
_TotThroughputOut_Object = MibTableColumn
totThroughputOut = _TotThroughputOut_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 1, 2, 1, 6),
    _TotThroughputOut_Type()
)
totThroughputOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totThroughputOut.setStatus("current")
_TopTotThroughputIn_Type = Counter64
_TopTotThroughputIn_Object = MibTableColumn
topTotThroughputIn = _TopTotThroughputIn_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 1, 2, 1, 7),
    _TopTotThroughputIn_Type()
)
topTotThroughputIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topTotThroughputIn.setStatus("current")
_TopTotThroughputOut_Type = Counter64
_TopTotThroughputOut_Object = MibTableColumn
topTotThroughputOut = _TopTotThroughputOut_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 1, 2, 1, 8),
    _TopTotThroughputOut_Type()
)
topTotThroughputOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topTotThroughputOut.setStatus("current")
_NumPackReceivedOut_Type = Counter64
_NumPackReceivedOut_Object = MibTableColumn
numPackReceivedOut = _NumPackReceivedOut_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 1, 2, 1, 9),
    _NumPackReceivedOut_Type()
)
numPackReceivedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numPackReceivedOut.setStatus("current")
_NumBytesReceivedOut_Type = Counter64
_NumBytesReceivedOut_Object = MibTableColumn
numBytesReceivedOut = _NumBytesReceivedOut_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 1, 2, 1, 10),
    _NumBytesReceivedOut_Type()
)
numBytesReceivedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numBytesReceivedOut.setStatus("current")
_NumPackReceivedIn_Type = Counter64
_NumPackReceivedIn_Object = MibTableColumn
numPackReceivedIn = _NumPackReceivedIn_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 1, 2, 1, 11),
    _NumPackReceivedIn_Type()
)
numPackReceivedIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numPackReceivedIn.setStatus("current")
_NumBytesReceivedIn_Type = Counter64
_NumBytesReceivedIn_Object = MibTableColumn
numBytesReceivedIn = _NumBytesReceivedIn_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 1, 2, 1, 12),
    _NumBytesReceivedIn_Type()
)
numBytesReceivedIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numBytesReceivedIn.setStatus("current")
_NumL2Dropped_Type = Unsigned32
_NumL2Dropped_Object = MibTableColumn
numL2Dropped = _NumL2Dropped_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 1, 2, 1, 13),
    _NumL2Dropped_Type()
)
numL2Dropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numL2Dropped.setStatus("current")
_NumIPDroppedShun_Type = Unsigned32
_NumIPDroppedShun_Object = MibTableColumn
numIPDroppedShun = _NumIPDroppedShun_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 1, 2, 1, 14),
    _NumIPDroppedShun_Type()
)
numIPDroppedShun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numIPDroppedShun.setStatus("current")
_NumIPDroppedAll_Type = Unsigned32
_NumIPDroppedAll_Object = MibTableColumn
numIPDroppedAll = _NumIPDroppedAll_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 1, 2, 1, 15),
    _NumIPDroppedAll_Type()
)
numIPDroppedAll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numIPDroppedAll.setStatus("current")
_NumIPFragNat_Type = Unsigned32
_NumIPFragNat_Object = MibTableColumn
numIPFragNat = _NumIPFragNat_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 1, 2, 1, 16),
    _NumIPFragNat_Type()
)
numIPFragNat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numIPFragNat.setStatus("current")
_NumTCPMSSModif_Type = Unsigned32
_NumTCPMSSModif_Object = MibTableColumn
numTCPMSSModif = _NumTCPMSSModif_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 1, 2, 1, 17),
    _NumTCPMSSModif_Type()
)
numTCPMSSModif.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numTCPMSSModif.setStatus("current")
_NumTCPCheckError_Type = Unsigned32
_NumTCPCheckError_Object = MibTableColumn
numTCPCheckError = _NumTCPCheckError_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 1, 2, 1, 18),
    _NumTCPCheckError_Type()
)
numTCPCheckError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numTCPCheckError.setStatus("current")
_NumUDPCheckError_Type = Unsigned32
_NumUDPCheckError_Object = MibTableColumn
numUDPCheckError = _NumUDPCheckError_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 1, 2, 1, 19),
    _NumUDPCheckError_Type()
)
numUDPCheckError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numUDPCheckError.setStatus("current")
_TotNumDropProbe_Type = Unsigned32
_TotNumDropProbe_Object = MibTableColumn
totNumDropProbe = _TotNumDropProbe_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 1, 2, 1, 20),
    _TotNumDropProbe_Type()
)
totNumDropProbe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totNumDropProbe.setStatus("current")
_TotNumDropProbePerSec_Type = Unsigned32
_TotNumDropProbePerSec_Object = MibTableColumn
totNumDropProbePerSec = _TotNumDropProbePerSec_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 1, 2, 1, 21),
    _TotNumDropProbePerSec_Type()
)
totNumDropProbePerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totNumDropProbePerSec.setStatus("current")
_LastPacketTimeTraver_Type = Unsigned32
_LastPacketTimeTraver_Object = MibTableColumn
lastPacketTimeTraver = _LastPacketTimeTraver_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 1, 2, 1, 22),
    _LastPacketTimeTraver_Type()
)
lastPacketTimeTraver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastPacketTimeTraver.setStatus("current")
_TopPacketTimeTraver_Type = Unsigned32
_TopPacketTimeTraver_Object = MibTableColumn
topPacketTimeTraver = _TopPacketTimeTraver_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 1, 2, 1, 23),
    _TopPacketTimeTraver_Type()
)
topPacketTimeTraver.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topPacketTimeTraver.setStatus("current")
_NumLiveSessIn_Type = Unsigned32
_NumLiveSessIn_Object = MibTableColumn
numLiveSessIn = _NumLiveSessIn_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 1, 2, 1, 24),
    _NumLiveSessIn_Type()
)
numLiveSessIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numLiveSessIn.setStatus("current")
_TopNumLiveSessIn_Type = Unsigned32
_TopNumLiveSessIn_Object = MibTableColumn
topNumLiveSessIn = _TopNumLiveSessIn_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 1, 2, 1, 25),
    _TopNumLiveSessIn_Type()
)
topNumLiveSessIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topNumLiveSessIn.setStatus("current")
_SamplingIntervalIn_Type = Unsigned32
_SamplingIntervalIn_Object = MibTableColumn
samplingIntervalIn = _SamplingIntervalIn_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 1, 2, 1, 26),
    _SamplingIntervalIn_Type()
)
samplingIntervalIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    samplingIntervalIn.setStatus("current")
_NumNewSessPerSecIn_Type = Unsigned32
_NumNewSessPerSecIn_Object = MibTableColumn
numNewSessPerSecIn = _NumNewSessPerSecIn_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 1, 2, 1, 27),
    _NumNewSessPerSecIn_Type()
)
numNewSessPerSecIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numNewSessPerSecIn.setStatus("current")
_NumEndSessPerSecIn_Type = Unsigned32
_NumEndSessPerSecIn_Object = MibTableColumn
numEndSessPerSecIn = _NumEndSessPerSecIn_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 1, 2, 1, 28),
    _NumEndSessPerSecIn_Type()
)
numEndSessPerSecIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numEndSessPerSecIn.setStatus("current")
_NumHandledSessIn_Type = Counter64
_NumHandledSessIn_Object = MibTableColumn
numHandledSessIn = _NumHandledSessIn_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 1, 2, 1, 29),
    _NumHandledSessIn_Type()
)
numHandledSessIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numHandledSessIn.setStatus("current")
_NumLiveSessOut_Type = Unsigned32
_NumLiveSessOut_Object = MibTableColumn
numLiveSessOut = _NumLiveSessOut_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 1, 2, 1, 30),
    _NumLiveSessOut_Type()
)
numLiveSessOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numLiveSessOut.setStatus("current")
_TopNumLiveSessOut_Type = Unsigned32
_TopNumLiveSessOut_Object = MibTableColumn
topNumLiveSessOut = _TopNumLiveSessOut_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 1, 2, 1, 31),
    _TopNumLiveSessOut_Type()
)
topNumLiveSessOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topNumLiveSessOut.setStatus("current")
_SamplingIntervalOut_Type = Unsigned32
_SamplingIntervalOut_Object = MibTableColumn
samplingIntervalOut = _SamplingIntervalOut_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 1, 2, 1, 32),
    _SamplingIntervalOut_Type()
)
samplingIntervalOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    samplingIntervalOut.setStatus("current")
_NumNewSessPerSecOut_Type = Unsigned32
_NumNewSessPerSecOut_Object = MibTableColumn
numNewSessPerSecOut = _NumNewSessPerSecOut_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 1, 2, 1, 33),
    _NumNewSessPerSecOut_Type()
)
numNewSessPerSecOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numNewSessPerSecOut.setStatus("current")
_NumEndSessPerSecOut_Type = Unsigned32
_NumEndSessPerSecOut_Object = MibTableColumn
numEndSessPerSecOut = _NumEndSessPerSecOut_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 1, 2, 1, 34),
    _NumEndSessPerSecOut_Type()
)
numEndSessPerSecOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numEndSessPerSecOut.setStatus("current")
_NumHandledSessOut_Type = Counter64
_NumHandledSessOut_Object = MibTableColumn
numHandledSessOut = _NumHandledSessOut_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 1, 2, 1, 35),
    _NumHandledSessOut_Type()
)
numHandledSessOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numHandledSessOut.setStatus("current")
_NumDNSReqPerSecOut_Type = Unsigned32
_NumDNSReqPerSecOut_Object = MibTableColumn
numDNSReqPerSecOut = _NumDNSReqPerSecOut_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 1, 2, 1, 36),
    _NumDNSReqPerSecOut_Type()
)
numDNSReqPerSecOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numDNSReqPerSecOut.setStatus("current")
_TopNumDNSReqPerSecOut_Type = Unsigned32
_TopNumDNSReqPerSecOut_Object = MibTableColumn
topNumDNSReqPerSecOut = _TopNumDNSReqPerSecOut_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 1, 2, 1, 37),
    _TopNumDNSReqPerSecOut_Type()
)
topNumDNSReqPerSecOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topNumDNSReqPerSecOut.setStatus("current")
_NumHandledDNSReqOut_Type = Counter64
_NumHandledDNSReqOut_Object = MibTableColumn
numHandledDNSReqOut = _NumHandledDNSReqOut_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 1, 2, 1, 38),
    _NumHandledDNSReqOut_Type()
)
numHandledDNSReqOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numHandledDNSReqOut.setStatus("current")
_NumDNSReqPerSecIn_Type = Unsigned32
_NumDNSReqPerSecIn_Object = MibTableColumn
numDNSReqPerSecIn = _NumDNSReqPerSecIn_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 1, 2, 1, 39),
    _NumDNSReqPerSecIn_Type()
)
numDNSReqPerSecIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numDNSReqPerSecIn.setStatus("current")
_TopNumDNSReqPerSecIn_Type = Unsigned32
_TopNumDNSReqPerSecIn_Object = MibTableColumn
topNumDNSReqPerSecIn = _TopNumDNSReqPerSecIn_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 1, 2, 1, 40),
    _TopNumDNSReqPerSecIn_Type()
)
topNumDNSReqPerSecIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    topNumDNSReqPerSecIn.setStatus("current")
_NumHandledDNSReqIn_Type = Counter64
_NumHandledDNSReqIn_Object = MibTableColumn
numHandledDNSReqIn = _NumHandledDNSReqIn_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 1, 2, 1, 41),
    _NumHandledDNSReqIn_Type()
)
numHandledDNSReqIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numHandledDNSReqIn.setStatus("current")
_GmacInfo_ObjectIdentity = ObjectIdentity
gmacInfo = _GmacInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 2)
)
_GmacNumber_Type = Integer32
_GmacNumber_Object = MibScalar
gmacNumber = _GmacNumber_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 2, 1),
    _GmacNumber_Type()
)
gmacNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmacNumber.setStatus("current")
_GmacTable_Object = MibTable
gmacTable = _GmacTable_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    gmacTable.setStatus("current")
_GmacEntry_Object = MibTableRow
gmacEntry = _GmacEntry_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 2, 2, 1)
)
gmacEntry.setIndexNames(
    (0, "ELFIQ-MODULE-LB-MIB", "gmacIndex"),
)
if mibBuilder.loadTexts:
    gmacEntry.setStatus("current")


class _GmacVfiNumber_Type(Integer32):
    """Custom type gmacVfiNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("vfi0", 0),
          ("vfi1", 1),
          ("vfi2", 2),
          ("vfi3", 3),
          ("vfi4", 4))
    )


_GmacVfiNumber_Type.__name__ = "Integer32"
_GmacVfiNumber_Object = MibTableColumn
gmacVfiNumber = _GmacVfiNumber_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 2, 2, 1, 1),
    _GmacVfiNumber_Type()
)
gmacVfiNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmacVfiNumber.setStatus("current")
_GmacIndex_Type = GmacIndex
_GmacIndex_Object = MibTableColumn
gmacIndex = _GmacIndex_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 2, 2, 1, 2),
    _GmacIndex_Type()
)
gmacIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmacIndex.setStatus("current")


class _GmacName_Type(DisplayString):
    """Custom type gmacName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_GmacName_Type.__name__ = "DisplayString"
_GmacName_Object = MibTableColumn
gmacName = _GmacName_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 2, 2, 1, 3),
    _GmacName_Type()
)
gmacName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmacName.setStatus("current")


class _GmacDescr_Type(DisplayString):
    """Custom type gmacDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_GmacDescr_Type.__name__ = "DisplayString"
_GmacDescr_Object = MibTableColumn
gmacDescr = _GmacDescr_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 2, 2, 1, 4),
    _GmacDescr_Type()
)
gmacDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmacDescr.setStatus("current")


class _GmacStatus_Type(Integer32):
    """Custom type gmacStatus based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("disableLinkFlap", 4),
          ("down", 8),
          ("enable", 1),
          ("failure", 5),
          ("incomplete", 6),
          ("shutdown", 2),
          ("up", 7))
    )


_GmacStatus_Type.__name__ = "Integer32"
_GmacStatus_Object = MibTableColumn
gmacStatus = _GmacStatus_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 2, 2, 1, 5),
    _GmacStatus_Type()
)
gmacStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmacStatus.setStatus("current")


class _GmacMessage_Type(DisplayString):
    """Custom type gmacMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_GmacMessage_Type.__name__ = "DisplayString"
_GmacMessage_Object = MibTableColumn
gmacMessage = _GmacMessage_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 2, 2, 1, 6),
    _GmacMessage_Type()
)
gmacMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmacMessage.setStatus("current")


class _GmacMode_Type(DisplayString):
    """Custom type gmacMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_GmacMode_Type.__name__ = "DisplayString"
_GmacMode_Object = MibTableColumn
gmacMode = _GmacMode_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 2, 2, 1, 7),
    _GmacMode_Type()
)
gmacMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmacMode.setStatus("current")


class _GmacType_Type(DisplayString):
    """Custom type gmacType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_GmacType_Type.__name__ = "DisplayString"
_GmacType_Object = MibTableColumn
gmacType = _GmacType_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 2, 2, 1, 8),
    _GmacType_Type()
)
gmacType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmacType.setStatus("current")
_GmacIPAddress_Type = IpAddress
_GmacIPAddress_Object = MibTableColumn
gmacIPAddress = _GmacIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 2, 2, 1, 9),
    _GmacIPAddress_Type()
)
gmacIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmacIPAddress.setStatus("current")
_GmacNetmask_Type = IpAddress
_GmacNetmask_Object = MibTableColumn
gmacNetmask = _GmacNetmask_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 2, 2, 1, 10),
    _GmacNetmask_Type()
)
gmacNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmacNetmask.setStatus("current")
_GmacPrimaryNetwork_Type = IpAddress
_GmacPrimaryNetwork_Object = MibTableColumn
gmacPrimaryNetwork = _GmacPrimaryNetwork_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 2, 2, 1, 11),
    _GmacPrimaryNetwork_Type()
)
gmacPrimaryNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmacPrimaryNetwork.setStatus("current")
_GmacMtu_Type = Unsigned32
_GmacMtu_Object = MibTableColumn
gmacMtu = _GmacMtu_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 2, 2, 1, 12),
    _GmacMtu_Type()
)
gmacMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmacMtu.setStatus("current")
_GmacProbeSource_Type = IpAddress
_GmacProbeSource_Object = MibTableColumn
gmacProbeSource = _GmacProbeSource_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 2, 2, 1, 13),
    _GmacProbeSource_Type()
)
gmacProbeSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmacProbeSource.setStatus("current")


class _GmacProbeSourceType_Type(DisplayString):
    """Custom type gmacProbeSourceType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_GmacProbeSourceType_Type.__name__ = "DisplayString"
_GmacProbeSourceType_Object = MibTableColumn
gmacProbeSourceType = _GmacProbeSourceType_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 2, 2, 1, 14),
    _GmacProbeSourceType_Type()
)
gmacProbeSourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmacProbeSourceType.setStatus("current")
_GmacProbeDest_Type = IpAddress
_GmacProbeDest_Object = MibTableColumn
gmacProbeDest = _GmacProbeDest_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 2, 2, 1, 15),
    _GmacProbeDest_Type()
)
gmacProbeDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmacProbeDest.setStatus("current")
_GmacProbeDestInt_Type = Unsigned32
_GmacProbeDestInt_Object = MibTableColumn
gmacProbeDestInt = _GmacProbeDestInt_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 2, 2, 1, 16),
    _GmacProbeDestInt_Type()
)
gmacProbeDestInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmacProbeDestInt.setStatus("current")
_GmacProbeFailThres_Type = Unsigned32
_GmacProbeFailThres_Object = MibTableColumn
gmacProbeFailThres = _GmacProbeFailThres_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 2, 2, 1, 17),
    _GmacProbeFailThres_Type()
)
gmacProbeFailThres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmacProbeFailThres.setStatus("current")
_GmacProbeFailTimeout_Type = Unsigned32
_GmacProbeFailTimeout_Object = MibTableColumn
gmacProbeFailTimeout = _GmacProbeFailTimeout_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 2, 2, 1, 18),
    _GmacProbeFailTimeout_Type()
)
gmacProbeFailTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmacProbeFailTimeout.setStatus("current")
_GmacProbeSynSeq_Type = Unsigned32
_GmacProbeSynSeq_Object = MibTableColumn
gmacProbeSynSeq = _GmacProbeSynSeq_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 2, 2, 1, 19),
    _GmacProbeSynSeq_Type()
)
gmacProbeSynSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmacProbeSynSeq.setStatus("current")
_GmacProbeFail_Type = Unsigned32
_GmacProbeFail_Object = MibTableColumn
gmacProbeFail = _GmacProbeFail_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 2, 2, 1, 20),
    _GmacProbeFail_Type()
)
gmacProbeFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmacProbeFail.setStatus("current")
_GmacRTT_Type = Unsigned32
_GmacRTT_Object = MibTableColumn
gmacRTT = _GmacRTT_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 2, 2, 1, 21),
    _GmacRTT_Type()
)
gmacRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmacRTT.setStatus("current")
_GmacWeight_Type = Unsigned32
_GmacWeight_Object = MibTableColumn
gmacWeight = _GmacWeight_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 2, 2, 1, 22),
    _GmacWeight_Type()
)
gmacWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmacWeight.setStatus("current")
_GmacInThreshold_Type = Unsigned32
_GmacInThreshold_Object = MibTableColumn
gmacInThreshold = _GmacInThreshold_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 2, 2, 1, 23),
    _GmacInThreshold_Type()
)
gmacInThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmacInThreshold.setStatus("current")
_GmacOutThreshold_Type = Unsigned32
_GmacOutThreshold_Object = MibTableColumn
gmacOutThreshold = _GmacOutThreshold_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 2, 2, 1, 24),
    _GmacOutThreshold_Type()
)
gmacOutThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmacOutThreshold.setStatus("current")
_GmacSpeedIn_Type = Unsigned32
_GmacSpeedIn_Object = MibTableColumn
gmacSpeedIn = _GmacSpeedIn_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 2, 2, 1, 25),
    _GmacSpeedIn_Type()
)
gmacSpeedIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmacSpeedIn.setStatus("current")
_GmacSpeedOut_Type = Unsigned32
_GmacSpeedOut_Object = MibTableColumn
gmacSpeedOut = _GmacSpeedOut_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 2, 2, 1, 26),
    _GmacSpeedOut_Type()
)
gmacSpeedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmacSpeedOut.setStatus("current")
_GmacSampleInter_Type = Unsigned32
_GmacSampleInter_Object = MibTableColumn
gmacSampleInter = _GmacSampleInter_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 2, 2, 1, 27),
    _GmacSampleInter_Type()
)
gmacSampleInter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmacSampleInter.setStatus("current")
_GmacSampleCount_Type = Unsigned32
_GmacSampleCount_Object = MibTableColumn
gmacSampleCount = _GmacSampleCount_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 2, 2, 1, 28),
    _GmacSampleCount_Type()
)
gmacSampleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmacSampleCount.setStatus("current")
_GmacL2No_Type = Unsigned32
_GmacL2No_Object = MibTableColumn
gmacL2No = _GmacL2No_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 2, 2, 1, 29),
    _GmacL2No_Type()
)
gmacL2No.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmacL2No.setStatus("current")
_GmacTotalIn_Type = Unsigned32
_GmacTotalIn_Object = MibTableColumn
gmacTotalIn = _GmacTotalIn_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 2, 2, 1, 30),
    _GmacTotalIn_Type()
)
gmacTotalIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmacTotalIn.setStatus("current")
_GmacTotalOut_Type = Unsigned32
_GmacTotalOut_Object = MibTableColumn
gmacTotalOut = _GmacTotalOut_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 2, 2, 1, 31),
    _GmacTotalOut_Type()
)
gmacTotalOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmacTotalOut.setStatus("current")
_GmacAvgIn_Type = Unsigned32
_GmacAvgIn_Object = MibTableColumn
gmacAvgIn = _GmacAvgIn_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 2, 2, 1, 32),
    _GmacAvgIn_Type()
)
gmacAvgIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmacAvgIn.setStatus("current")
_GmacAvgOut_Type = Unsigned32
_GmacAvgOut_Object = MibTableColumn
gmacAvgOut = _GmacAvgOut_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 2, 2, 1, 33),
    _GmacAvgOut_Type()
)
gmacAvgOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmacAvgOut.setStatus("current")
_GmacUsageIn_Type = Unsigned32
_GmacUsageIn_Object = MibTableColumn
gmacUsageIn = _GmacUsageIn_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 2, 2, 1, 34),
    _GmacUsageIn_Type()
)
gmacUsageIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmacUsageIn.setStatus("current")
_GmacUsageOut_Type = Unsigned32
_GmacUsageOut_Object = MibTableColumn
gmacUsageOut = _GmacUsageOut_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 2, 2, 1, 35),
    _GmacUsageOut_Type()
)
gmacUsageOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmacUsageOut.setStatus("current")
_GmacUsageInPercent_Type = Unsigned32
_GmacUsageInPercent_Object = MibTableColumn
gmacUsageInPercent = _GmacUsageInPercent_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 2, 2, 1, 36),
    _GmacUsageInPercent_Type()
)
gmacUsageInPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmacUsageInPercent.setStatus("current")
_GmacUsageOutPercent_Type = Unsigned32
_GmacUsageOutPercent_Object = MibTableColumn
gmacUsageOutPercent = _GmacUsageOutPercent_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 2, 2, 1, 37),
    _GmacUsageOutPercent_Type()
)
gmacUsageOutPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmacUsageOutPercent.setStatus("current")
_GmacTopSpeedIn_Type = Unsigned32
_GmacTopSpeedIn_Object = MibTableColumn
gmacTopSpeedIn = _GmacTopSpeedIn_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 2, 2, 1, 38),
    _GmacTopSpeedIn_Type()
)
gmacTopSpeedIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmacTopSpeedIn.setStatus("current")
_GmacTopSpeedOut_Type = Unsigned32
_GmacTopSpeedOut_Object = MibTableColumn
gmacTopSpeedOut = _GmacTopSpeedOut_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 2, 2, 1, 39),
    _GmacTopSpeedOut_Type()
)
gmacTopSpeedOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmacTopSpeedOut.setStatus("current")


class _GmacQosActivated_Type(Integer32):
    """Custom type gmacQosActivated based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("activated", 1),
          ("desactivated", 0))
    )


_GmacQosActivated_Type.__name__ = "Integer32"
_GmacQosActivated_Object = MibTableColumn
gmacQosActivated = _GmacQosActivated_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 2, 2, 1, 40),
    _GmacQosActivated_Type()
)
gmacQosActivated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmacQosActivated.setStatus("current")
_GmacBeforeQosUsageIn_Type = Unsigned32
_GmacBeforeQosUsageIn_Object = MibTableColumn
gmacBeforeQosUsageIn = _GmacBeforeQosUsageIn_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 2, 2, 1, 41),
    _GmacBeforeQosUsageIn_Type()
)
gmacBeforeQosUsageIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmacBeforeQosUsageIn.setStatus("current")
_GmacBeforeQosUsageOut_Type = Unsigned32
_GmacBeforeQosUsageOut_Object = MibTableColumn
gmacBeforeQosUsageOut = _GmacBeforeQosUsageOut_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 2, 2, 1, 42),
    _GmacBeforeQosUsageOut_Type()
)
gmacBeforeQosUsageOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmacBeforeQosUsageOut.setStatus("current")
_ArpInfo_ObjectIdentity = ObjectIdentity
arpInfo = _ArpInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 3)
)
_ArpNumber_Type = Integer32
_ArpNumber_Object = MibScalar
arpNumber = _ArpNumber_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 3, 1),
    _ArpNumber_Type()
)
arpNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arpNumber.setStatus("current")
_ArpTable_Object = MibTable
arpTable = _ArpTable_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    arpTable.setStatus("current")
_ArpEntry_Object = MibTableRow
arpEntry = _ArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 3, 2, 1)
)
arpEntry.setIndexNames(
    (0, "ELFIQ-MODULE-LB-MIB", "arpIndex"),
)
if mibBuilder.loadTexts:
    arpEntry.setStatus("current")


class _ArpVfiNumber_Type(Integer32):
    """Custom type arpVfiNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("vfi0", 0),
          ("vfi1", 1),
          ("vfi2", 2),
          ("vfi3", 3),
          ("vfi4", 4))
    )


_ArpVfiNumber_Type.__name__ = "Integer32"
_ArpVfiNumber_Object = MibTableColumn
arpVfiNumber = _ArpVfiNumber_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 3, 2, 1, 1),
    _ArpVfiNumber_Type()
)
arpVfiNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpVfiNumber.setStatus("current")
_ArpIndex_Type = ArpIndex
_ArpIndex_Object = MibTableColumn
arpIndex = _ArpIndex_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 3, 2, 1, 2),
    _ArpIndex_Type()
)
arpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpIndex.setStatus("current")


class _ArpMessage_Type(DisplayString):
    """Custom type arpMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_ArpMessage_Type.__name__ = "DisplayString"
_ArpMessage_Object = MibTableColumn
arpMessage = _ArpMessage_Object(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 1, 3, 2, 1, 3),
    _ArpMessage_Type()
)
arpMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpMessage.setStatus("current")
_LinkBalancerNotification_ObjectIdentity = ObjectIdentity
linkBalancerNotification = _LinkBalancerNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 2)
)
_GmacNotification_ObjectIdentity = ObjectIdentity
gmacNotification = _GmacNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 2, 1)
)
_VfiNotification_ObjectIdentity = ObjectIdentity
vfiNotification = _VfiNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 2, 2)
)
_ArpNotification_ObjectIdentity = ObjectIdentity
arpNotification = _ArpNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 2, 3)
)
_VfiGroups_ObjectIdentity = ObjectIdentity
vfiGroups = _VfiGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19713, 2, 2, 2)
)
_GmacGroups_ObjectIdentity = ObjectIdentity
gmacGroups = _GmacGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19713, 2, 2, 3)
)
_ArpGroups_ObjectIdentity = ObjectIdentity
arpGroups = _ArpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19713, 2, 2, 4)
)

# Managed Objects groups

vfiStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 19713, 2, 2, 2, 1)
)
vfiStatsGroup.setObjects(
      *(("ELFIQ-MODULE-LB-MIB", "vfiNumber"),
        ("ELFIQ-MODULE-LB-MIB", "vfiIndex"),
        ("ELFIQ-MODULE-LB-MIB", "vfiDescr"),
        ("ELFIQ-MODULE-LB-MIB", "vfiActivated"),
        ("ELFIQ-MODULE-LB-MIB", "vfiStatus"),
        ("ELFIQ-MODULE-LB-MIB", "totThroughputIn"),
        ("ELFIQ-MODULE-LB-MIB", "totThroughputOut"),
        ("ELFIQ-MODULE-LB-MIB", "topTotThroughputIn"),
        ("ELFIQ-MODULE-LB-MIB", "topTotThroughputOut"),
        ("ELFIQ-MODULE-LB-MIB", "numPackReceivedOut"),
        ("ELFIQ-MODULE-LB-MIB", "numBytesReceivedOut"),
        ("ELFIQ-MODULE-LB-MIB", "numPackReceivedIn"),
        ("ELFIQ-MODULE-LB-MIB", "numBytesReceivedIn"),
        ("ELFIQ-MODULE-LB-MIB", "numL2Dropped"),
        ("ELFIQ-MODULE-LB-MIB", "numIPDroppedShun"),
        ("ELFIQ-MODULE-LB-MIB", "numIPDroppedAll"),
        ("ELFIQ-MODULE-LB-MIB", "numIPFragNat"),
        ("ELFIQ-MODULE-LB-MIB", "numTCPMSSModif"),
        ("ELFIQ-MODULE-LB-MIB", "numTCPCheckError"),
        ("ELFIQ-MODULE-LB-MIB", "numUDPCheckError"),
        ("ELFIQ-MODULE-LB-MIB", "totNumDropProbe"),
        ("ELFIQ-MODULE-LB-MIB", "totNumDropProbePerSec"),
        ("ELFIQ-MODULE-LB-MIB", "lastPacketTimeTraver"),
        ("ELFIQ-MODULE-LB-MIB", "topPacketTimeTraver"),
        ("ELFIQ-MODULE-LB-MIB", "numLiveSessIn"),
        ("ELFIQ-MODULE-LB-MIB", "topNumLiveSessIn"),
        ("ELFIQ-MODULE-LB-MIB", "samplingIntervalIn"),
        ("ELFIQ-MODULE-LB-MIB", "numNewSessPerSecIn"),
        ("ELFIQ-MODULE-LB-MIB", "numEndSessPerSecIn"),
        ("ELFIQ-MODULE-LB-MIB", "numHandledSessIn"),
        ("ELFIQ-MODULE-LB-MIB", "numLiveSessOut"),
        ("ELFIQ-MODULE-LB-MIB", "topNumLiveSessOut"),
        ("ELFIQ-MODULE-LB-MIB", "samplingIntervalOut"),
        ("ELFIQ-MODULE-LB-MIB", "numNewSessPerSecOut"),
        ("ELFIQ-MODULE-LB-MIB", "numEndSessPerSecOut"),
        ("ELFIQ-MODULE-LB-MIB", "numHandledSessOut"),
        ("ELFIQ-MODULE-LB-MIB", "numDNSReqPerSecOut"),
        ("ELFIQ-MODULE-LB-MIB", "topNumDNSReqPerSecOut"),
        ("ELFIQ-MODULE-LB-MIB", "numHandledDNSReqOut"),
        ("ELFIQ-MODULE-LB-MIB", "numDNSReqPerSecIn"),
        ("ELFIQ-MODULE-LB-MIB", "topNumDNSReqPerSecIn"),
        ("ELFIQ-MODULE-LB-MIB", "numHandledDNSReqIn"))
)
if mibBuilder.loadTexts:
    vfiStatsGroup.setStatus("current")

gmacNetworkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 19713, 2, 2, 3, 1)
)
gmacNetworkGroup.setObjects(
      *(("ELFIQ-MODULE-LB-MIB", "gmacNumber"),
        ("ELFIQ-MODULE-LB-MIB", "gmacVfiNumber"),
        ("ELFIQ-MODULE-LB-MIB", "gmacIndex"),
        ("ELFIQ-MODULE-LB-MIB", "gmacName"),
        ("ELFIQ-MODULE-LB-MIB", "gmacDescr"),
        ("ELFIQ-MODULE-LB-MIB", "gmacStatus"),
        ("ELFIQ-MODULE-LB-MIB", "gmacMessage"),
        ("ELFIQ-MODULE-LB-MIB", "gmacMode"),
        ("ELFIQ-MODULE-LB-MIB", "gmacIPAddress"),
        ("ELFIQ-MODULE-LB-MIB", "gmacNetmask"),
        ("ELFIQ-MODULE-LB-MIB", "gmacType"),
        ("ELFIQ-MODULE-LB-MIB", "gmacMtu"),
        ("ELFIQ-MODULE-LB-MIB", "gmacProbeSource"),
        ("ELFIQ-MODULE-LB-MIB", "gmacProbeSourceType"),
        ("ELFIQ-MODULE-LB-MIB", "gmacProbeDest"),
        ("ELFIQ-MODULE-LB-MIB", "gmacProbeDestInt"),
        ("ELFIQ-MODULE-LB-MIB", "gmacProbeFailThres"),
        ("ELFIQ-MODULE-LB-MIB", "gmacProbeFailTimeout"),
        ("ELFIQ-MODULE-LB-MIB", "gmacProbeSynSeq"),
        ("ELFIQ-MODULE-LB-MIB", "gmacProbeFail"),
        ("ELFIQ-MODULE-LB-MIB", "gmacRTT"),
        ("ELFIQ-MODULE-LB-MIB", "gmacWeight"),
        ("ELFIQ-MODULE-LB-MIB", "gmacInThreshold"),
        ("ELFIQ-MODULE-LB-MIB", "gmacOutThreshold"),
        ("ELFIQ-MODULE-LB-MIB", "gmacSpeedIn"),
        ("ELFIQ-MODULE-LB-MIB", "gmacSpeedOut"),
        ("ELFIQ-MODULE-LB-MIB", "gmacSampleInter"),
        ("ELFIQ-MODULE-LB-MIB", "gmacSampleCount"),
        ("ELFIQ-MODULE-LB-MIB", "gmacL2No"),
        ("ELFIQ-MODULE-LB-MIB", "gmacTotalIn"),
        ("ELFIQ-MODULE-LB-MIB", "gmacTotalOut"),
        ("ELFIQ-MODULE-LB-MIB", "gmacAvgIn"),
        ("ELFIQ-MODULE-LB-MIB", "gmacAvgOut"),
        ("ELFIQ-MODULE-LB-MIB", "gmacUsageIn"),
        ("ELFIQ-MODULE-LB-MIB", "gmacUsageOut"),
        ("ELFIQ-MODULE-LB-MIB", "gmacUsageInPercent"),
        ("ELFIQ-MODULE-LB-MIB", "gmacUsageOutPercent"),
        ("ELFIQ-MODULE-LB-MIB", "gmacTopSpeedIn"),
        ("ELFIQ-MODULE-LB-MIB", "gmacTopSpeedOut"),
        ("ELFIQ-MODULE-LB-MIB", "gmacQosActivated"),
        ("ELFIQ-MODULE-LB-MIB", "gmacBeforeQosUsageIn"),
        ("ELFIQ-MODULE-LB-MIB", "gmacBeforeQosUsageOut"),
        ("ELFIQ-MODULE-LB-MIB", "gmacPrimaryNetwork"))
)
if mibBuilder.loadTexts:
    gmacNetworkGroup.setStatus("current")

arpNetworkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 19713, 2, 2, 4, 1)
)
arpNetworkGroup.setObjects(
      *(("ELFIQ-MODULE-LB-MIB", "arpVfiNumber"),
        ("ELFIQ-MODULE-LB-MIB", "arpIndex"),
        ("ELFIQ-MODULE-LB-MIB", "arpMessage"))
)
if mibBuilder.loadTexts:
    arpNetworkGroup.setStatus("current")


# Notification objects

gmacStatusNotInitialiazed = NotificationType(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 2, 1, 1)
)
gmacStatusNotInitialiazed.setObjects(
      *(("ELFIQ-MODULE-LB-MIB", "gmacName"),
        ("ELFIQ-MODULE-LB-MIB", "gmacVfiNumber"),
        ("ELFIQ-MODULE-LB-MIB", "gmacStatus"),
        ("ELFIQ-MODULE-LB-MIB", "gmacMessage"))
)
if mibBuilder.loadTexts:
    gmacStatusNotInitialiazed.setStatus(
        "current"
    )

gmacStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 2, 1, 2)
)
gmacStatusChanged.setObjects(
      *(("ELFIQ-MODULE-LB-MIB", "gmacName"),
        ("ELFIQ-MODULE-LB-MIB", "gmacVfiNumber"),
        ("ELFIQ-MODULE-LB-MIB", "gmacStatus"),
        ("ELFIQ-MODULE-LB-MIB", "gmacMessage"))
)
if mibBuilder.loadTexts:
    gmacStatusChanged.setStatus(
        "current"
    )

gmacInSaturated = NotificationType(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 2, 1, 3)
)
gmacInSaturated.setObjects(
      *(("ELFIQ-MODULE-LB-MIB", "gmacName"),
        ("ELFIQ-MODULE-LB-MIB", "gmacVfiNumber"),
        ("ELFIQ-MODULE-LB-MIB", "gmacUsageInPercent"))
)
if mibBuilder.loadTexts:
    gmacInSaturated.setStatus(
        "current"
    )

gmacOutSaturated = NotificationType(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 2, 1, 4)
)
gmacOutSaturated.setObjects(
      *(("ELFIQ-MODULE-LB-MIB", "gmacName"),
        ("ELFIQ-MODULE-LB-MIB", "gmacVfiNumber"),
        ("ELFIQ-MODULE-LB-MIB", "gmacUsageOutPercent"))
)
if mibBuilder.loadTexts:
    gmacOutSaturated.setStatus(
        "current"
    )

arpDeviceNotResponding = NotificationType(
    (1, 3, 6, 1, 4, 1, 19713, 1, 2, 2, 3, 1)
)
arpDeviceNotResponding.setObjects(
      *(("ELFIQ-MODULE-LB-MIB", "arpVfiNumber"),
        ("ELFIQ-MODULE-LB-MIB", "arpMessage"))
)
if mibBuilder.loadTexts:
    arpDeviceNotResponding.setStatus(
        "current"
    )


# Notifications groups

gmacNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 19713, 2, 2, 3, 2)
)
gmacNotificationGroup.setObjects(
      *(("ELFIQ-MODULE-LB-MIB", "gmacStatusNotInitialiazed"),
        ("ELFIQ-MODULE-LB-MIB", "gmacStatusChanged"),
        ("ELFIQ-MODULE-LB-MIB", "gmacInSaturated"),
        ("ELFIQ-MODULE-LB-MIB", "gmacOutSaturated"))
)
if mibBuilder.loadTexts:
    gmacNotificationGroup.setStatus(
        "current"
    )

arpNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 19713, 2, 2, 4, 2)
)
arpNotificationGroup.setObjects(
    ("ELFIQ-MODULE-LB-MIB", "arpDeviceNotResponding")
)
if mibBuilder.loadTexts:
    arpNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELFIQ-MODULE-LB-MIB",
    **{"VfiIndex": VfiIndex,
       "GmacIndex": GmacIndex,
       "ArpIndex": ArpIndex,
       "linkBalancerComponent": linkBalancerComponent,
       "vfiInfo": vfiInfo,
       "vfiNumber": vfiNumber,
       "vfiTable": vfiTable,
       "vfiEntry": vfiEntry,
       "vfiIndex": vfiIndex,
       "vfiDescr": vfiDescr,
       "vfiActivated": vfiActivated,
       "vfiStatus": vfiStatus,
       "totThroughputIn": totThroughputIn,
       "totThroughputOut": totThroughputOut,
       "topTotThroughputIn": topTotThroughputIn,
       "topTotThroughputOut": topTotThroughputOut,
       "numPackReceivedOut": numPackReceivedOut,
       "numBytesReceivedOut": numBytesReceivedOut,
       "numPackReceivedIn": numPackReceivedIn,
       "numBytesReceivedIn": numBytesReceivedIn,
       "numL2Dropped": numL2Dropped,
       "numIPDroppedShun": numIPDroppedShun,
       "numIPDroppedAll": numIPDroppedAll,
       "numIPFragNat": numIPFragNat,
       "numTCPMSSModif": numTCPMSSModif,
       "numTCPCheckError": numTCPCheckError,
       "numUDPCheckError": numUDPCheckError,
       "totNumDropProbe": totNumDropProbe,
       "totNumDropProbePerSec": totNumDropProbePerSec,
       "lastPacketTimeTraver": lastPacketTimeTraver,
       "topPacketTimeTraver": topPacketTimeTraver,
       "numLiveSessIn": numLiveSessIn,
       "topNumLiveSessIn": topNumLiveSessIn,
       "samplingIntervalIn": samplingIntervalIn,
       "numNewSessPerSecIn": numNewSessPerSecIn,
       "numEndSessPerSecIn": numEndSessPerSecIn,
       "numHandledSessIn": numHandledSessIn,
       "numLiveSessOut": numLiveSessOut,
       "topNumLiveSessOut": topNumLiveSessOut,
       "samplingIntervalOut": samplingIntervalOut,
       "numNewSessPerSecOut": numNewSessPerSecOut,
       "numEndSessPerSecOut": numEndSessPerSecOut,
       "numHandledSessOut": numHandledSessOut,
       "numDNSReqPerSecOut": numDNSReqPerSecOut,
       "topNumDNSReqPerSecOut": topNumDNSReqPerSecOut,
       "numHandledDNSReqOut": numHandledDNSReqOut,
       "numDNSReqPerSecIn": numDNSReqPerSecIn,
       "topNumDNSReqPerSecIn": topNumDNSReqPerSecIn,
       "numHandledDNSReqIn": numHandledDNSReqIn,
       "gmacInfo": gmacInfo,
       "gmacNumber": gmacNumber,
       "gmacTable": gmacTable,
       "gmacEntry": gmacEntry,
       "gmacVfiNumber": gmacVfiNumber,
       "gmacIndex": gmacIndex,
       "gmacName": gmacName,
       "gmacDescr": gmacDescr,
       "gmacStatus": gmacStatus,
       "gmacMessage": gmacMessage,
       "gmacMode": gmacMode,
       "gmacType": gmacType,
       "gmacIPAddress": gmacIPAddress,
       "gmacNetmask": gmacNetmask,
       "gmacPrimaryNetwork": gmacPrimaryNetwork,
       "gmacMtu": gmacMtu,
       "gmacProbeSource": gmacProbeSource,
       "gmacProbeSourceType": gmacProbeSourceType,
       "gmacProbeDest": gmacProbeDest,
       "gmacProbeDestInt": gmacProbeDestInt,
       "gmacProbeFailThres": gmacProbeFailThres,
       "gmacProbeFailTimeout": gmacProbeFailTimeout,
       "gmacProbeSynSeq": gmacProbeSynSeq,
       "gmacProbeFail": gmacProbeFail,
       "gmacRTT": gmacRTT,
       "gmacWeight": gmacWeight,
       "gmacInThreshold": gmacInThreshold,
       "gmacOutThreshold": gmacOutThreshold,
       "gmacSpeedIn": gmacSpeedIn,
       "gmacSpeedOut": gmacSpeedOut,
       "gmacSampleInter": gmacSampleInter,
       "gmacSampleCount": gmacSampleCount,
       "gmacL2No": gmacL2No,
       "gmacTotalIn": gmacTotalIn,
       "gmacTotalOut": gmacTotalOut,
       "gmacAvgIn": gmacAvgIn,
       "gmacAvgOut": gmacAvgOut,
       "gmacUsageIn": gmacUsageIn,
       "gmacUsageOut": gmacUsageOut,
       "gmacUsageInPercent": gmacUsageInPercent,
       "gmacUsageOutPercent": gmacUsageOutPercent,
       "gmacTopSpeedIn": gmacTopSpeedIn,
       "gmacTopSpeedOut": gmacTopSpeedOut,
       "gmacQosActivated": gmacQosActivated,
       "gmacBeforeQosUsageIn": gmacBeforeQosUsageIn,
       "gmacBeforeQosUsageOut": gmacBeforeQosUsageOut,
       "arpInfo": arpInfo,
       "arpNumber": arpNumber,
       "arpTable": arpTable,
       "arpEntry": arpEntry,
       "arpVfiNumber": arpVfiNumber,
       "arpIndex": arpIndex,
       "arpMessage": arpMessage,
       "linkBalancerNotification": linkBalancerNotification,
       "gmacNotification": gmacNotification,
       "gmacStatusNotInitialiazed": gmacStatusNotInitialiazed,
       "gmacStatusChanged": gmacStatusChanged,
       "gmacInSaturated": gmacInSaturated,
       "gmacOutSaturated": gmacOutSaturated,
       "vfiNotification": vfiNotification,
       "arpNotification": arpNotification,
       "arpDeviceNotResponding": arpDeviceNotResponding,
       "vfiGroups": vfiGroups,
       "vfiStatsGroup": vfiStatsGroup,
       "gmacGroups": gmacGroups,
       "gmacNetworkGroup": gmacNetworkGroup,
       "gmacNotificationGroup": gmacNotificationGroup,
       "arpGroups": arpGroups,
       "arpNetworkGroup": arpNetworkGroup,
       "arpNotificationGroup": arpNotificationGroup}
)
