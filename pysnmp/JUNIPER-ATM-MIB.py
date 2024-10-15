# SNMP MIB module (JUNIPER-ATM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JUNIPER-ATM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:12:49 2024
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

(atmInterfaceConfEntry,
 atmVclEntry,
 atmVplEntry) = mibBuilder.importSymbols(
    "ATM-MIB",
    "atmInterfaceConfEntry",
    "atmVclEntry",
    "atmVplEntry")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddressIPv4,
 InetAddressIPv6) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv4",
    "InetAddressIPv6")

(jnxMibs,) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxMibs")

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

jnxAtm = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 10)
)
jnxAtm.setRevisions(
        ("2004-01-06 00:00",
         "2003-12-04 00:00",
         "2003-09-17 00:00",
         "2002-07-04 00:00",
         "2002-01-23 00:00",
         "2001-07-08 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class JnxAtmFlags(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_JnxAtmIfTable_Object = MibTable
jnxAtmIfTable = _JnxAtmIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 10, 1)
)
if mibBuilder.loadTexts:
    jnxAtmIfTable.setStatus("current")
_JnxAtmIfEntry_Object = MibTableRow
jnxAtmIfEntry = _JnxAtmIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 10, 1, 1)
)
if mibBuilder.loadTexts:
    jnxAtmIfEntry.setStatus("current")


class _JnxAtmIfPortType_Type(Integer32):
    """Custom type jnxAtmIfPortType based on Integer32"""
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
        *(("e3", 5),
          ("oc12", 3),
          ("oc3", 2),
          ("oc48", 6),
          ("other", 1),
          ("t3", 4))
    )


_JnxAtmIfPortType_Type.__name__ = "Integer32"
_JnxAtmIfPortType_Object = MibTableColumn
jnxAtmIfPortType = _JnxAtmIfPortType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 10, 1, 1, 1),
    _JnxAtmIfPortType_Type()
)
jnxAtmIfPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAtmIfPortType.setStatus("current")


class _JnxAtmIfEncaps_Type(Integer32):
    """Custom type jnxAtmIfEncaps based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("atmCccCellRelay", 3),
          ("atmPvc", 2),
          ("other", 1))
    )


_JnxAtmIfEncaps_Type.__name__ = "Integer32"
_JnxAtmIfEncaps_Object = MibTableColumn
jnxAtmIfEncaps = _JnxAtmIfEncaps_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 10, 1, 1, 2),
    _JnxAtmIfEncaps_Type()
)
jnxAtmIfEncaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAtmIfEncaps.setStatus("current")


class _JnxAtmIfLpBackInfo_Type(Integer32):
    """Custom type jnxAtmIfLpBackInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("localLoopBack", 2),
          ("noLoopBack", 1),
          ("remoteLoopBack", 3))
    )


_JnxAtmIfLpBackInfo_Type.__name__ = "Integer32"
_JnxAtmIfLpBackInfo_Object = MibTableColumn
jnxAtmIfLpBackInfo = _JnxAtmIfLpBackInfo_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 10, 1, 1, 3),
    _JnxAtmIfLpBackInfo_Type()
)
jnxAtmIfLpBackInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAtmIfLpBackInfo.setStatus("current")


class _JnxAtmIfScrambleEnable_Type(Integer32):
    """Custom type jnxAtmIfScrambleEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_JnxAtmIfScrambleEnable_Type.__name__ = "Integer32"
_JnxAtmIfScrambleEnable_Object = MibTableColumn
jnxAtmIfScrambleEnable = _JnxAtmIfScrambleEnable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 10, 1, 1, 4),
    _JnxAtmIfScrambleEnable_Type()
)
jnxAtmIfScrambleEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAtmIfScrambleEnable.setStatus("current")
_JnxAtmIfTxCellCount_Type = Counter64
_JnxAtmIfTxCellCount_Object = MibTableColumn
jnxAtmIfTxCellCount = _JnxAtmIfTxCellCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 10, 1, 1, 5),
    _JnxAtmIfTxCellCount_Type()
)
jnxAtmIfTxCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAtmIfTxCellCount.setStatus("current")
_JnxAtmIfRxCellCount_Type = Counter64
_JnxAtmIfRxCellCount_Object = MibTableColumn
jnxAtmIfRxCellCount = _JnxAtmIfRxCellCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 10, 1, 1, 6),
    _JnxAtmIfRxCellCount_Type()
)
jnxAtmIfRxCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAtmIfRxCellCount.setStatus("current")
_JnxAtmIfTxIdleCellCount_Type = Counter64
_JnxAtmIfTxIdleCellCount_Object = MibTableColumn
jnxAtmIfTxIdleCellCount = _JnxAtmIfTxIdleCellCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 10, 1, 1, 7),
    _JnxAtmIfTxIdleCellCount_Type()
)
jnxAtmIfTxIdleCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAtmIfTxIdleCellCount.setStatus("current")
_JnxAtmIfUncorrHCSErrs_Type = Counter64
_JnxAtmIfUncorrHCSErrs_Object = MibTableColumn
jnxAtmIfUncorrHCSErrs = _JnxAtmIfUncorrHCSErrs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 10, 1, 1, 8),
    _JnxAtmIfUncorrHCSErrs_Type()
)
jnxAtmIfUncorrHCSErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAtmIfUncorrHCSErrs.setStatus("current")
_JnxAtmIfCorrHCSErrs_Type = Counter64
_JnxAtmIfCorrHCSErrs_Object = MibTableColumn
jnxAtmIfCorrHCSErrs = _JnxAtmIfCorrHCSErrs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 10, 1, 1, 9),
    _JnxAtmIfCorrHCSErrs_Type()
)
jnxAtmIfCorrHCSErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAtmIfCorrHCSErrs.setStatus("current")
_JnxAtmIfTxCellFIFOOverRuns_Type = Counter64
_JnxAtmIfTxCellFIFOOverRuns_Object = MibTableColumn
jnxAtmIfTxCellFIFOOverRuns = _JnxAtmIfTxCellFIFOOverRuns_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 10, 1, 1, 10),
    _JnxAtmIfTxCellFIFOOverRuns_Type()
)
jnxAtmIfTxCellFIFOOverRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAtmIfTxCellFIFOOverRuns.setStatus("current")
_JnxAtmIfRxCellFIFOOverRuns_Type = Counter64
_JnxAtmIfRxCellFIFOOverRuns_Object = MibTableColumn
jnxAtmIfRxCellFIFOOverRuns = _JnxAtmIfRxCellFIFOOverRuns_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 10, 1, 1, 11),
    _JnxAtmIfRxCellFIFOOverRuns_Type()
)
jnxAtmIfRxCellFIFOOverRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAtmIfRxCellFIFOOverRuns.setStatus("current")
_JnxAtmIfRxCellFIFOUnderRuns_Type = Counter64
_JnxAtmIfRxCellFIFOUnderRuns_Object = MibTableColumn
jnxAtmIfRxCellFIFOUnderRuns = _JnxAtmIfRxCellFIFOUnderRuns_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 10, 1, 1, 12),
    _JnxAtmIfRxCellFIFOUnderRuns_Type()
)
jnxAtmIfRxCellFIFOUnderRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAtmIfRxCellFIFOUnderRuns.setStatus("current")
_JnxAtmIfInInvalidVCCells_Type = Counter64
_JnxAtmIfInInvalidVCCells_Object = MibTableColumn
jnxAtmIfInInvalidVCCells = _JnxAtmIfInInvalidVCCells_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 10, 1, 1, 13),
    _JnxAtmIfInInvalidVCCells_Type()
)
jnxAtmIfInInvalidVCCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAtmIfInInvalidVCCells.setStatus("current")
_JnxAtmIfInNoBufferOAMCells_Type = Counter64
_JnxAtmIfInNoBufferOAMCells_Object = MibTableColumn
jnxAtmIfInNoBufferOAMCells = _JnxAtmIfInNoBufferOAMCells_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 10, 1, 1, 14),
    _JnxAtmIfInNoBufferOAMCells_Type()
)
jnxAtmIfInNoBufferOAMCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAtmIfInNoBufferOAMCells.setStatus("current")
_JnxAtmIfInNoBufDropPkts_Type = Counter64
_JnxAtmIfInNoBufDropPkts_Object = MibTableColumn
jnxAtmIfInNoBufDropPkts = _JnxAtmIfInNoBufDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 10, 1, 1, 15),
    _JnxAtmIfInNoBufDropPkts_Type()
)
jnxAtmIfInNoBufDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAtmIfInNoBufDropPkts.setStatus("current")
_JnxAtmIfOutVCQueueDrops_Type = Counter64
_JnxAtmIfOutVCQueueDrops_Object = MibTableColumn
jnxAtmIfOutVCQueueDrops = _JnxAtmIfOutVCQueueDrops_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 10, 1, 1, 16),
    _JnxAtmIfOutVCQueueDrops_Type()
)
jnxAtmIfOutVCQueueDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAtmIfOutVCQueueDrops.setStatus("current")
_JnxAtmIfInBadCrcs_Type = Counter64
_JnxAtmIfInBadCrcs_Object = MibTableColumn
jnxAtmIfInBadCrcs = _JnxAtmIfInBadCrcs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 10, 1, 1, 17),
    _JnxAtmIfInBadCrcs_Type()
)
jnxAtmIfInBadCrcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAtmIfInBadCrcs.setStatus("current")
_JnxAtmIfInLenErrPkts_Type = Counter64
_JnxAtmIfInLenErrPkts_Object = MibTableColumn
jnxAtmIfInLenErrPkts = _JnxAtmIfInLenErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 10, 1, 1, 18),
    _JnxAtmIfInLenErrPkts_Type()
)
jnxAtmIfInLenErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAtmIfInLenErrPkts.setStatus("current")
_JnxAtmIfInTimeoutPkts_Type = Counter64
_JnxAtmIfInTimeoutPkts_Object = MibTableColumn
jnxAtmIfInTimeoutPkts = _JnxAtmIfInTimeoutPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 10, 1, 1, 19),
    _JnxAtmIfInTimeoutPkts_Type()
)
jnxAtmIfInTimeoutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAtmIfInTimeoutPkts.setStatus("current")


class _JnxAtmIfL2CircuitMode_Type(Integer32):
    """Custom type jnxAtmIfL2CircuitMode based on Integer32"""
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
        *(("aal5", 3),
          ("cell", 4),
          ("nniTrunk", 6),
          ("none", 2),
          ("notApplicable", 1),
          ("uniTrunk", 5))
    )


_JnxAtmIfL2CircuitMode_Type.__name__ = "Integer32"
_JnxAtmIfL2CircuitMode_Object = MibTableColumn
jnxAtmIfL2CircuitMode = _JnxAtmIfL2CircuitMode_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 10, 1, 1, 20),
    _JnxAtmIfL2CircuitMode_Type()
)
jnxAtmIfL2CircuitMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAtmIfL2CircuitMode.setStatus("current")
_JnxAtmVCTable_Object = MibTable
jnxAtmVCTable = _JnxAtmVCTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 10, 2)
)
if mibBuilder.loadTexts:
    jnxAtmVCTable.setStatus("current")
_JnxAtmVCEntry_Object = MibTableRow
jnxAtmVCEntry = _JnxAtmVCEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 10, 2, 1)
)
if mibBuilder.loadTexts:
    jnxAtmVCEntry.setStatus("current")


class _JnxAtmVCConnType_Type(Integer32):
    """Custom type jnxAtmVCConnType based on Integer32"""
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
        *(("multicast", 4),
          ("other", 1),
          ("p2mp", 3),
          ("p2p", 2))
    )


_JnxAtmVCConnType_Type.__name__ = "Integer32"
_JnxAtmVCConnType_Object = MibTableColumn
jnxAtmVCConnType = _JnxAtmVCConnType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 10, 2, 1, 1),
    _JnxAtmVCConnType_Type()
)
jnxAtmVCConnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAtmVCConnType.setStatus("current")


class _JnxAtmVCEncapsulation_Type(Integer32):
    """Custom type jnxAtmVCEncapsulation based on Integer32"""
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
        *(("atmCccCellRelay", 2),
          ("atmCccVcMux", 3),
          ("atmCiscoNlpid", 4),
          ("atmNlpid", 5),
          ("atmSnap", 6),
          ("atmTccSnap", 9),
          ("atmTccVcMux", 8),
          ("atmVcMux", 7),
          ("other", 1))
    )


_JnxAtmVCEncapsulation_Type.__name__ = "Integer32"
_JnxAtmVCEncapsulation_Object = MibTableColumn
jnxAtmVCEncapsulation = _JnxAtmVCEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 10, 2, 1, 2),
    _JnxAtmVCEncapsulation_Type()
)
jnxAtmVCEncapsulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAtmVCEncapsulation.setStatus("current")
_JnxAtmVCMpDestIPv4Addr_Type = InetAddressIPv4
_JnxAtmVCMpDestIPv4Addr_Object = MibTableColumn
jnxAtmVCMpDestIPv4Addr = _JnxAtmVCMpDestIPv4Addr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 10, 2, 1, 3),
    _JnxAtmVCMpDestIPv4Addr_Type()
)
jnxAtmVCMpDestIPv4Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAtmVCMpDestIPv4Addr.setStatus("current")
_JnxAtmVCMpDestIPv6Addr_Type = InetAddressIPv6
_JnxAtmVCMpDestIPv6Addr_Object = MibTableColumn
jnxAtmVCMpDestIPv6Addr = _JnxAtmVCMpDestIPv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 10, 2, 1, 4),
    _JnxAtmVCMpDestIPv6Addr_Type()
)
jnxAtmVCMpDestIPv6Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAtmVCMpDestIPv6Addr.setStatus("current")
_JnxAtmVCFlags_Type = JnxAtmFlags
_JnxAtmVCFlags_Object = MibTableColumn
jnxAtmVCFlags = _JnxAtmVCFlags_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 10, 2, 1, 5),
    _JnxAtmVCFlags_Type()
)
jnxAtmVCFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAtmVCFlags.setStatus("current")
_JnxAtmVCTotalDownTime_Type = Integer32
_JnxAtmVCTotalDownTime_Object = MibTableColumn
jnxAtmVCTotalDownTime = _JnxAtmVCTotalDownTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 10, 2, 1, 6),
    _JnxAtmVCTotalDownTime_Type()
)
jnxAtmVCTotalDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAtmVCTotalDownTime.setStatus("current")
_JnxAtmVCInBytes_Type = Counter64
_JnxAtmVCInBytes_Object = MibTableColumn
jnxAtmVCInBytes = _JnxAtmVCInBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 10, 2, 1, 7),
    _JnxAtmVCInBytes_Type()
)
jnxAtmVCInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAtmVCInBytes.setStatus("current")
_JnxAtmVCOutBytes_Type = Counter64
_JnxAtmVCOutBytes_Object = MibTableColumn
jnxAtmVCOutBytes = _JnxAtmVCOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 10, 2, 1, 8),
    _JnxAtmVCOutBytes_Type()
)
jnxAtmVCOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAtmVCOutBytes.setStatus("current")
_JnxAtmVCInPkts_Type = Counter64
_JnxAtmVCInPkts_Object = MibTableColumn
jnxAtmVCInPkts = _JnxAtmVCInPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 10, 2, 1, 9),
    _JnxAtmVCInPkts_Type()
)
jnxAtmVCInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAtmVCInPkts.setStatus("current")
_JnxAtmVCOutPkts_Type = Counter64
_JnxAtmVCOutPkts_Object = MibTableColumn
jnxAtmVCOutPkts = _JnxAtmVCOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 10, 2, 1, 10),
    _JnxAtmVCOutPkts_Type()
)
jnxAtmVCOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAtmVCOutPkts.setStatus("current")
_JnxAtmVCTailQueuePktDrops_Type = Counter64
_JnxAtmVCTailQueuePktDrops_Object = MibTableColumn
jnxAtmVCTailQueuePktDrops = _JnxAtmVCTailQueuePktDrops_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 10, 2, 1, 11),
    _JnxAtmVCTailQueuePktDrops_Type()
)
jnxAtmVCTailQueuePktDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAtmVCTailQueuePktDrops.setStatus("current")
_JnxAtmVCOAMPeriod_Type = Integer32
_JnxAtmVCOAMPeriod_Object = MibTableColumn
jnxAtmVCOAMPeriod = _JnxAtmVCOAMPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 10, 2, 1, 12),
    _JnxAtmVCOAMPeriod_Type()
)
jnxAtmVCOAMPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAtmVCOAMPeriod.setStatus("current")
_JnxAtmVCOAMUpCellCount_Type = Integer32
_JnxAtmVCOAMUpCellCount_Object = MibTableColumn
jnxAtmVCOAMUpCellCount = _JnxAtmVCOAMUpCellCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 10, 2, 1, 13),
    _JnxAtmVCOAMUpCellCount_Type()
)
jnxAtmVCOAMUpCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAtmVCOAMUpCellCount.setStatus("current")
_JnxAtmVCOAMDownCellCount_Type = Integer32
_JnxAtmVCOAMDownCellCount_Object = MibTableColumn
jnxAtmVCOAMDownCellCount = _JnxAtmVCOAMDownCellCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 10, 2, 1, 14),
    _JnxAtmVCOAMDownCellCount_Type()
)
jnxAtmVCOAMDownCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAtmVCOAMDownCellCount.setStatus("current")
_JnxAtmVCInOAMF5LoopCells_Type = Counter32
_JnxAtmVCInOAMF5LoopCells_Object = MibTableColumn
jnxAtmVCInOAMF5LoopCells = _JnxAtmVCInOAMF5LoopCells_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 10, 2, 1, 15),
    _JnxAtmVCInOAMF5LoopCells_Type()
)
jnxAtmVCInOAMF5LoopCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAtmVCInOAMF5LoopCells.setStatus("current")
_JnxAtmVCOutOAMF5LoopCells_Type = Counter32
_JnxAtmVCOutOAMF5LoopCells_Object = MibTableColumn
jnxAtmVCOutOAMF5LoopCells = _JnxAtmVCOutOAMF5LoopCells_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 10, 2, 1, 16),
    _JnxAtmVCOutOAMF5LoopCells_Type()
)
jnxAtmVCOutOAMF5LoopCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAtmVCOutOAMF5LoopCells.setStatus("current")
_JnxAtmVCInOAMF5RDICells_Type = Counter32
_JnxAtmVCInOAMF5RDICells_Object = MibTableColumn
jnxAtmVCInOAMF5RDICells = _JnxAtmVCInOAMF5RDICells_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 10, 2, 1, 17),
    _JnxAtmVCInOAMF5RDICells_Type()
)
jnxAtmVCInOAMF5RDICells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAtmVCInOAMF5RDICells.setStatus("current")
_JnxAtmVCOutOAMF5RDICells_Type = Counter32
_JnxAtmVCOutOAMF5RDICells_Object = MibTableColumn
jnxAtmVCOutOAMF5RDICells = _JnxAtmVCOutOAMF5RDICells_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 10, 2, 1, 18),
    _JnxAtmVCOutOAMF5RDICells_Type()
)
jnxAtmVCOutOAMF5RDICells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAtmVCOutOAMF5RDICells.setStatus("current")
_JnxAtmVCInOAMF5AISCells_Type = Counter32
_JnxAtmVCInOAMF5AISCells_Object = MibTableColumn
jnxAtmVCInOAMF5AISCells = _JnxAtmVCInOAMF5AISCells_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 10, 2, 1, 19),
    _JnxAtmVCInOAMF5AISCells_Type()
)
jnxAtmVCInOAMF5AISCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAtmVCInOAMF5AISCells.setStatus("current")
_JnxAtmVCOutOAMF5AISCells_Type = Counter32
_JnxAtmVCOutOAMF5AISCells_Object = MibTableColumn
jnxAtmVCOutOAMF5AISCells = _JnxAtmVCOutOAMF5AISCells_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 10, 2, 1, 20),
    _JnxAtmVCOutOAMF5AISCells_Type()
)
jnxAtmVCOutOAMF5AISCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAtmVCOutOAMF5AISCells.setStatus("current")
_JnxAtmVpTable_Object = MibTable
jnxAtmVpTable = _JnxAtmVpTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 10, 3)
)
if mibBuilder.loadTexts:
    jnxAtmVpTable.setStatus("current")
_JnxAtmVpEntry_Object = MibTableRow
jnxAtmVpEntry = _JnxAtmVpEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 10, 3, 1)
)
if mibBuilder.loadTexts:
    jnxAtmVpEntry.setStatus("current")


class _JnxAtmVpFlags_Type(Bits):
    """Custom type jnxAtmVpFlags based on Bits"""
    namedValues = NamedValues(
        *(("active", 0),
          ("down", 1),
          ("oamEnabled", 2),
          ("passiveOam", 4),
          ("shapingEnabled", 3))
    )

_JnxAtmVpFlags_Type.__name__ = "Bits"
_JnxAtmVpFlags_Object = MibTableColumn
jnxAtmVpFlags = _JnxAtmVpFlags_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 10, 3, 1, 1),
    _JnxAtmVpFlags_Type()
)
jnxAtmVpFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAtmVpFlags.setStatus("current")
_JnxAtmVpTotalDownTime_Type = Integer32
_JnxAtmVpTotalDownTime_Object = MibTableColumn
jnxAtmVpTotalDownTime = _JnxAtmVpTotalDownTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 10, 3, 1, 2),
    _JnxAtmVpTotalDownTime_Type()
)
jnxAtmVpTotalDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAtmVpTotalDownTime.setStatus("current")
_JnxAtmVpOamPeriod_Type = Integer32
_JnxAtmVpOamPeriod_Object = MibTableColumn
jnxAtmVpOamPeriod = _JnxAtmVpOamPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 10, 3, 1, 3),
    _JnxAtmVpOamPeriod_Type()
)
jnxAtmVpOamPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAtmVpOamPeriod.setStatus("current")
_JnxAtmVpOamUpCellCount_Type = Integer32
_JnxAtmVpOamUpCellCount_Object = MibTableColumn
jnxAtmVpOamUpCellCount = _JnxAtmVpOamUpCellCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 10, 3, 1, 4),
    _JnxAtmVpOamUpCellCount_Type()
)
jnxAtmVpOamUpCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAtmVpOamUpCellCount.setStatus("current")
_JnxAtmVpOamDownCellCount_Type = Integer32
_JnxAtmVpOamDownCellCount_Object = MibTableColumn
jnxAtmVpOamDownCellCount = _JnxAtmVpOamDownCellCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 10, 3, 1, 5),
    _JnxAtmVpOamDownCellCount_Type()
)
jnxAtmVpOamDownCellCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAtmVpOamDownCellCount.setStatus("current")
_JnxAtmVpInBytes_Type = Counter64
_JnxAtmVpInBytes_Object = MibTableColumn
jnxAtmVpInBytes = _JnxAtmVpInBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 10, 3, 1, 6),
    _JnxAtmVpInBytes_Type()
)
jnxAtmVpInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAtmVpInBytes.setStatus("current")
_JnxAtmVpOutBytes_Type = Counter64
_JnxAtmVpOutBytes_Object = MibTableColumn
jnxAtmVpOutBytes = _JnxAtmVpOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 10, 3, 1, 7),
    _JnxAtmVpOutBytes_Type()
)
jnxAtmVpOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAtmVpOutBytes.setStatus("current")
_JnxAtmVpInPkts_Type = Counter64
_JnxAtmVpInPkts_Object = MibTableColumn
jnxAtmVpInPkts = _JnxAtmVpInPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 10, 3, 1, 8),
    _JnxAtmVpInPkts_Type()
)
jnxAtmVpInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAtmVpInPkts.setStatus("current")
_JnxAtmVpOutPkts_Type = Counter64
_JnxAtmVpOutPkts_Object = MibTableColumn
jnxAtmVpOutPkts = _JnxAtmVpOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 10, 3, 1, 9),
    _JnxAtmVpOutPkts_Type()
)
jnxAtmVpOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAtmVpOutPkts.setStatus("current")
_JnxAtmVpInOamF4Cells_Type = Counter32
_JnxAtmVpInOamF4Cells_Object = MibTableColumn
jnxAtmVpInOamF4Cells = _JnxAtmVpInOamF4Cells_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 10, 3, 1, 10),
    _JnxAtmVpInOamF4Cells_Type()
)
jnxAtmVpInOamF4Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAtmVpInOamF4Cells.setStatus("current")
_JnxAtmVpOutOamF4Cells_Type = Counter32
_JnxAtmVpOutOamF4Cells_Object = MibTableColumn
jnxAtmVpOutOamF4Cells = _JnxAtmVpOutOamF4Cells_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 10, 3, 1, 11),
    _JnxAtmVpOutOamF4Cells_Type()
)
jnxAtmVpOutOamF4Cells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAtmVpOutOamF4Cells.setStatus("current")
_JnxAtmVpInOamF4LoopCells_Type = Counter32
_JnxAtmVpInOamF4LoopCells_Object = MibTableColumn
jnxAtmVpInOamF4LoopCells = _JnxAtmVpInOamF4LoopCells_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 10, 3, 1, 12),
    _JnxAtmVpInOamF4LoopCells_Type()
)
jnxAtmVpInOamF4LoopCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAtmVpInOamF4LoopCells.setStatus("current")
_JnxAtmVpOutOamF4LoopCells_Type = Counter32
_JnxAtmVpOutOamF4LoopCells_Object = MibTableColumn
jnxAtmVpOutOamF4LoopCells = _JnxAtmVpOutOamF4LoopCells_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 10, 3, 1, 13),
    _JnxAtmVpOutOamF4LoopCells_Type()
)
jnxAtmVpOutOamF4LoopCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAtmVpOutOamF4LoopCells.setStatus("current")
_JnxAtmVpInOamF4RdiCells_Type = Counter32
_JnxAtmVpInOamF4RdiCells_Object = MibTableColumn
jnxAtmVpInOamF4RdiCells = _JnxAtmVpInOamF4RdiCells_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 10, 3, 1, 14),
    _JnxAtmVpInOamF4RdiCells_Type()
)
jnxAtmVpInOamF4RdiCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAtmVpInOamF4RdiCells.setStatus("current")
_JnxAtmVpOutOamF4RdiCells_Type = Counter32
_JnxAtmVpOutOamF4RdiCells_Object = MibTableColumn
jnxAtmVpOutOamF4RdiCells = _JnxAtmVpOutOamF4RdiCells_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 10, 3, 1, 15),
    _JnxAtmVpOutOamF4RdiCells_Type()
)
jnxAtmVpOutOamF4RdiCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAtmVpOutOamF4RdiCells.setStatus("current")
_JnxAtmVpInOamF4AisCells_Type = Counter32
_JnxAtmVpInOamF4AisCells_Object = MibTableColumn
jnxAtmVpInOamF4AisCells = _JnxAtmVpInOamF4AisCells_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 10, 3, 1, 16),
    _JnxAtmVpInOamF4AisCells_Type()
)
jnxAtmVpInOamF4AisCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAtmVpInOamF4AisCells.setStatus("current")
_JnxAtmTrunkTable_Object = MibTable
jnxAtmTrunkTable = _JnxAtmTrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 10, 4)
)
if mibBuilder.loadTexts:
    jnxAtmTrunkTable.setStatus("current")
_JnxAtmTrunkEntry_Object = MibTableRow
jnxAtmTrunkEntry = _JnxAtmTrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 10, 4, 1)
)
jnxAtmTrunkEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    jnxAtmTrunkEntry.setStatus("current")
_JnxAtmTrunkId_Type = Integer32
_JnxAtmTrunkId_Object = MibTableColumn
jnxAtmTrunkId = _JnxAtmTrunkId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 10, 4, 1, 1),
    _JnxAtmTrunkId_Type()
)
jnxAtmTrunkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAtmTrunkId.setStatus("current")


class _JnxAtmTrunkConnType_Type(Integer32):
    """Custom type jnxAtmTrunkConnType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("p2p", 2))
    )


_JnxAtmTrunkConnType_Type.__name__ = "Integer32"
_JnxAtmTrunkConnType_Object = MibTableColumn
jnxAtmTrunkConnType = _JnxAtmTrunkConnType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 10, 4, 1, 2),
    _JnxAtmTrunkConnType_Type()
)
jnxAtmTrunkConnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAtmTrunkConnType.setStatus("current")


class _JnxAtmTrunkEncapsulation_Type(Integer32):
    """Custom type jnxAtmTrunkEncapsulation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("atmCccCellRelay", 2),
          ("other", 1))
    )


_JnxAtmTrunkEncapsulation_Type.__name__ = "Integer32"
_JnxAtmTrunkEncapsulation_Object = MibTableColumn
jnxAtmTrunkEncapsulation = _JnxAtmTrunkEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 10, 4, 1, 3),
    _JnxAtmTrunkEncapsulation_Type()
)
jnxAtmTrunkEncapsulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAtmTrunkEncapsulation.setStatus("current")
_JnxAtmTrunkFlags_Type = JnxAtmFlags
_JnxAtmTrunkFlags_Object = MibTableColumn
jnxAtmTrunkFlags = _JnxAtmTrunkFlags_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 10, 4, 1, 4),
    _JnxAtmTrunkFlags_Type()
)
jnxAtmTrunkFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAtmTrunkFlags.setStatus("current")
_JnxAtmTrunkTotalDownTime_Type = Integer32
_JnxAtmTrunkTotalDownTime_Object = MibTableColumn
jnxAtmTrunkTotalDownTime = _JnxAtmTrunkTotalDownTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 10, 4, 1, 5),
    _JnxAtmTrunkTotalDownTime_Type()
)
jnxAtmTrunkTotalDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAtmTrunkTotalDownTime.setStatus("current")
_JnxAtmTrunkInBytes_Type = Counter64
_JnxAtmTrunkInBytes_Object = MibTableColumn
jnxAtmTrunkInBytes = _JnxAtmTrunkInBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 10, 4, 1, 6),
    _JnxAtmTrunkInBytes_Type()
)
jnxAtmTrunkInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAtmTrunkInBytes.setStatus("current")
_JnxAtmTrunkOutBytes_Type = Counter64
_JnxAtmTrunkOutBytes_Object = MibTableColumn
jnxAtmTrunkOutBytes = _JnxAtmTrunkOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 10, 4, 1, 7),
    _JnxAtmTrunkOutBytes_Type()
)
jnxAtmTrunkOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAtmTrunkOutBytes.setStatus("current")
_JnxAtmTrunkInPkts_Type = Counter64
_JnxAtmTrunkInPkts_Object = MibTableColumn
jnxAtmTrunkInPkts = _JnxAtmTrunkInPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 10, 4, 1, 8),
    _JnxAtmTrunkInPkts_Type()
)
jnxAtmTrunkInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAtmTrunkInPkts.setStatus("current")
_JnxAtmTrunkOutPkts_Type = Counter64
_JnxAtmTrunkOutPkts_Object = MibTableColumn
jnxAtmTrunkOutPkts = _JnxAtmTrunkOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 10, 4, 1, 9),
    _JnxAtmTrunkOutPkts_Type()
)
jnxAtmTrunkOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAtmTrunkOutPkts.setStatus("current")
_JnxAtmTrunkTailQueuePktDrops_Type = Counter64
_JnxAtmTrunkTailQueuePktDrops_Object = MibTableColumn
jnxAtmTrunkTailQueuePktDrops = _JnxAtmTrunkTailQueuePktDrops_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 10, 4, 1, 10),
    _JnxAtmTrunkTailQueuePktDrops_Type()
)
jnxAtmTrunkTailQueuePktDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAtmTrunkTailQueuePktDrops.setStatus("current")
_JnxAtmTrunkInOAMF4AISCells_Type = Counter32
_JnxAtmTrunkInOAMF4AISCells_Object = MibTableColumn
jnxAtmTrunkInOAMF4AISCells = _JnxAtmTrunkInOAMF4AISCells_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 10, 4, 1, 15),
    _JnxAtmTrunkInOAMF4AISCells_Type()
)
jnxAtmTrunkInOAMF4AISCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAtmTrunkInOAMF4AISCells.setStatus("current")
_JnxAtmTrunkOutOAMF4AISCells_Type = Counter32
_JnxAtmTrunkOutOAMF4AISCells_Object = MibTableColumn
jnxAtmTrunkOutOAMF4AISCells = _JnxAtmTrunkOutOAMF4AISCells_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 10, 4, 1, 16),
    _JnxAtmTrunkOutOAMF4AISCells_Type()
)
jnxAtmTrunkOutOAMF4AISCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxAtmTrunkOutOAMF4AISCells.setStatus("current")
atmInterfaceConfEntry.registerAugmentions(
    ("JUNIPER-ATM-MIB",
     "jnxAtmIfEntry")
)
jnxAtmIfEntry.setIndexNames(*atmInterfaceConfEntry.getIndexNames())
atmVclEntry.registerAugmentions(
    ("JUNIPER-ATM-MIB",
     "jnxAtmVCEntry")
)
jnxAtmVCEntry.setIndexNames(*atmVclEntry.getIndexNames())
atmVplEntry.registerAugmentions(
    ("JUNIPER-ATM-MIB",
     "jnxAtmVpEntry")
)
jnxAtmVpEntry.setIndexNames(*atmVplEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-ATM-MIB",
    **{"JnxAtmFlags": JnxAtmFlags,
       "jnxAtm": jnxAtm,
       "jnxAtmIfTable": jnxAtmIfTable,
       "jnxAtmIfEntry": jnxAtmIfEntry,
       "jnxAtmIfPortType": jnxAtmIfPortType,
       "jnxAtmIfEncaps": jnxAtmIfEncaps,
       "jnxAtmIfLpBackInfo": jnxAtmIfLpBackInfo,
       "jnxAtmIfScrambleEnable": jnxAtmIfScrambleEnable,
       "jnxAtmIfTxCellCount": jnxAtmIfTxCellCount,
       "jnxAtmIfRxCellCount": jnxAtmIfRxCellCount,
       "jnxAtmIfTxIdleCellCount": jnxAtmIfTxIdleCellCount,
       "jnxAtmIfUncorrHCSErrs": jnxAtmIfUncorrHCSErrs,
       "jnxAtmIfCorrHCSErrs": jnxAtmIfCorrHCSErrs,
       "jnxAtmIfTxCellFIFOOverRuns": jnxAtmIfTxCellFIFOOverRuns,
       "jnxAtmIfRxCellFIFOOverRuns": jnxAtmIfRxCellFIFOOverRuns,
       "jnxAtmIfRxCellFIFOUnderRuns": jnxAtmIfRxCellFIFOUnderRuns,
       "jnxAtmIfInInvalidVCCells": jnxAtmIfInInvalidVCCells,
       "jnxAtmIfInNoBufferOAMCells": jnxAtmIfInNoBufferOAMCells,
       "jnxAtmIfInNoBufDropPkts": jnxAtmIfInNoBufDropPkts,
       "jnxAtmIfOutVCQueueDrops": jnxAtmIfOutVCQueueDrops,
       "jnxAtmIfInBadCrcs": jnxAtmIfInBadCrcs,
       "jnxAtmIfInLenErrPkts": jnxAtmIfInLenErrPkts,
       "jnxAtmIfInTimeoutPkts": jnxAtmIfInTimeoutPkts,
       "jnxAtmIfL2CircuitMode": jnxAtmIfL2CircuitMode,
       "jnxAtmVCTable": jnxAtmVCTable,
       "jnxAtmVCEntry": jnxAtmVCEntry,
       "jnxAtmVCConnType": jnxAtmVCConnType,
       "jnxAtmVCEncapsulation": jnxAtmVCEncapsulation,
       "jnxAtmVCMpDestIPv4Addr": jnxAtmVCMpDestIPv4Addr,
       "jnxAtmVCMpDestIPv6Addr": jnxAtmVCMpDestIPv6Addr,
       "jnxAtmVCFlags": jnxAtmVCFlags,
       "jnxAtmVCTotalDownTime": jnxAtmVCTotalDownTime,
       "jnxAtmVCInBytes": jnxAtmVCInBytes,
       "jnxAtmVCOutBytes": jnxAtmVCOutBytes,
       "jnxAtmVCInPkts": jnxAtmVCInPkts,
       "jnxAtmVCOutPkts": jnxAtmVCOutPkts,
       "jnxAtmVCTailQueuePktDrops": jnxAtmVCTailQueuePktDrops,
       "jnxAtmVCOAMPeriod": jnxAtmVCOAMPeriod,
       "jnxAtmVCOAMUpCellCount": jnxAtmVCOAMUpCellCount,
       "jnxAtmVCOAMDownCellCount": jnxAtmVCOAMDownCellCount,
       "jnxAtmVCInOAMF5LoopCells": jnxAtmVCInOAMF5LoopCells,
       "jnxAtmVCOutOAMF5LoopCells": jnxAtmVCOutOAMF5LoopCells,
       "jnxAtmVCInOAMF5RDICells": jnxAtmVCInOAMF5RDICells,
       "jnxAtmVCOutOAMF5RDICells": jnxAtmVCOutOAMF5RDICells,
       "jnxAtmVCInOAMF5AISCells": jnxAtmVCInOAMF5AISCells,
       "jnxAtmVCOutOAMF5AISCells": jnxAtmVCOutOAMF5AISCells,
       "jnxAtmVpTable": jnxAtmVpTable,
       "jnxAtmVpEntry": jnxAtmVpEntry,
       "jnxAtmVpFlags": jnxAtmVpFlags,
       "jnxAtmVpTotalDownTime": jnxAtmVpTotalDownTime,
       "jnxAtmVpOamPeriod": jnxAtmVpOamPeriod,
       "jnxAtmVpOamUpCellCount": jnxAtmVpOamUpCellCount,
       "jnxAtmVpOamDownCellCount": jnxAtmVpOamDownCellCount,
       "jnxAtmVpInBytes": jnxAtmVpInBytes,
       "jnxAtmVpOutBytes": jnxAtmVpOutBytes,
       "jnxAtmVpInPkts": jnxAtmVpInPkts,
       "jnxAtmVpOutPkts": jnxAtmVpOutPkts,
       "jnxAtmVpInOamF4Cells": jnxAtmVpInOamF4Cells,
       "jnxAtmVpOutOamF4Cells": jnxAtmVpOutOamF4Cells,
       "jnxAtmVpInOamF4LoopCells": jnxAtmVpInOamF4LoopCells,
       "jnxAtmVpOutOamF4LoopCells": jnxAtmVpOutOamF4LoopCells,
       "jnxAtmVpInOamF4RdiCells": jnxAtmVpInOamF4RdiCells,
       "jnxAtmVpOutOamF4RdiCells": jnxAtmVpOutOamF4RdiCells,
       "jnxAtmVpInOamF4AisCells": jnxAtmVpInOamF4AisCells,
       "jnxAtmTrunkTable": jnxAtmTrunkTable,
       "jnxAtmTrunkEntry": jnxAtmTrunkEntry,
       "jnxAtmTrunkId": jnxAtmTrunkId,
       "jnxAtmTrunkConnType": jnxAtmTrunkConnType,
       "jnxAtmTrunkEncapsulation": jnxAtmTrunkEncapsulation,
       "jnxAtmTrunkFlags": jnxAtmTrunkFlags,
       "jnxAtmTrunkTotalDownTime": jnxAtmTrunkTotalDownTime,
       "jnxAtmTrunkInBytes": jnxAtmTrunkInBytes,
       "jnxAtmTrunkOutBytes": jnxAtmTrunkOutBytes,
       "jnxAtmTrunkInPkts": jnxAtmTrunkInPkts,
       "jnxAtmTrunkOutPkts": jnxAtmTrunkOutPkts,
       "jnxAtmTrunkTailQueuePktDrops": jnxAtmTrunkTailQueuePktDrops,
       "jnxAtmTrunkInOAMF4AISCells": jnxAtmTrunkInOAMF4AISCells,
       "jnxAtmTrunkOutOAMF4AISCells": jnxAtmTrunkOutOAMF4AISCells}
)
