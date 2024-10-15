# SNMP MIB module (CISCO-DMN-DSG-MOIPINPUT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DMN-DSG-MOIPINPUT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:58:28 2024
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

(ciscoDSGUtilities,) = mibBuilder.importSymbols(
    "CISCO-DMN-DSG-ROOT-MIB",
    "ciscoDSGUtilities")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ciscoDSGMOIPInput = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 41)
)
ciscoDSGMOIPInput.setRevisions(
        ("2012-11-12 18:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MoipInputInfo_ObjectIdentity = ObjectIdentity
moipInputInfo = _MoipInputInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 41, 1)
)


class _MoipInputFlowIsMulticast_Type(Integer32):
    """Custom type moipInputFlowIsMulticast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_MoipInputFlowIsMulticast_Type.__name__ = "Integer32"
_MoipInputFlowIsMulticast_Object = MibScalar
moipInputFlowIsMulticast = _MoipInputFlowIsMulticast_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 41, 1, 1),
    _MoipInputFlowIsMulticast_Type()
)
moipInputFlowIsMulticast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moipInputFlowIsMulticast.setStatus("current")
_MoipInputFlowMulticastDstIPV4_Type = IpAddress
_MoipInputFlowMulticastDstIPV4_Object = MibScalar
moipInputFlowMulticastDstIPV4 = _MoipInputFlowMulticastDstIPV4_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 41, 1, 2),
    _MoipInputFlowMulticastDstIPV4_Type()
)
moipInputFlowMulticastDstIPV4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moipInputFlowMulticastDstIPV4.setStatus("current")


class _MoipInputFlowFecMode_Type(Integer32):
    """Custom type moipInputFlowFecMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("oneD", 2),
          ("twoD", 3))
    )


_MoipInputFlowFecMode_Type.__name__ = "Integer32"
_MoipInputFlowFecMode_Object = MibScalar
moipInputFlowFecMode = _MoipInputFlowFecMode_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 41, 1, 3),
    _MoipInputFlowFecMode_Type()
)
moipInputFlowFecMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moipInputFlowFecMode.setStatus("current")


class _MoipInputFlowSrcFilter_Type(Integer32):
    """Custom type moipInputFlowSrcFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("blackList", 3),
          ("none", 1),
          ("whiteList", 2))
    )


_MoipInputFlowSrcFilter_Type.__name__ = "Integer32"
_MoipInputFlowSrcFilter_Object = MibScalar
moipInputFlowSrcFilter = _MoipInputFlowSrcFilter_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 41, 1, 4),
    _MoipInputFlowSrcFilter_Type()
)
moipInputFlowSrcFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moipInputFlowSrcFilter.setStatus("current")


class _MoipInputFlowTsUDPPort_Type(Integer32):
    """Custom type moipInputFlowTsUDPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65534),
    )


_MoipInputFlowTsUDPPort_Type.__name__ = "Integer32"
_MoipInputFlowTsUDPPort_Object = MibScalar
moipInputFlowTsUDPPort = _MoipInputFlowTsUDPPort_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 41, 1, 5),
    _MoipInputFlowTsUDPPort_Type()
)
moipInputFlowTsUDPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moipInputFlowTsUDPPort.setStatus("current")


class _MoipInputFlowFec1UDPPort_Type(Integer32):
    """Custom type moipInputFlowFec1UDPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 65534),
    )


_MoipInputFlowFec1UDPPort_Type.__name__ = "Integer32"
_MoipInputFlowFec1UDPPort_Object = MibScalar
moipInputFlowFec1UDPPort = _MoipInputFlowFec1UDPPort_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 41, 1, 6),
    _MoipInputFlowFec1UDPPort_Type()
)
moipInputFlowFec1UDPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moipInputFlowFec1UDPPort.setStatus("current")


class _MoipInputFlowFec2UDPPort_Type(Integer32):
    """Custom type moipInputFlowFec2UDPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 65534),
    )


_MoipInputFlowFec2UDPPort_Type.__name__ = "Integer32"
_MoipInputFlowFec2UDPPort_Object = MibScalar
moipInputFlowFec2UDPPort = _MoipInputFlowFec2UDPPort_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 41, 1, 7),
    _MoipInputFlowFec2UDPPort_Type()
)
moipInputFlowFec2UDPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moipInputFlowFec2UDPPort.setStatus("current")


class _MoipInputFlowSrcStrmSel_Type(Integer32):
    """Custom type moipInputFlowSrcStrmSel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("swMap", 1),
          ("userCfg", 2))
    )


_MoipInputFlowSrcStrmSel_Type.__name__ = "Integer32"
_MoipInputFlowSrcStrmSel_Object = MibScalar
moipInputFlowSrcStrmSel = _MoipInputFlowSrcStrmSel_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 41, 1, 8),
    _MoipInputFlowSrcStrmSel_Type()
)
moipInputFlowSrcStrmSel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moipInputFlowSrcStrmSel.setStatus("current")


class _MoipInputDejitterAlgorithm_Type(Integer32):
    """Custom type moipInputDejitterAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cbr", 1),
          ("vbr", 2))
    )


_MoipInputDejitterAlgorithm_Type.__name__ = "Integer32"
_MoipInputDejitterAlgorithm_Object = MibScalar
moipInputDejitterAlgorithm = _MoipInputDejitterAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 41, 1, 9),
    _MoipInputDejitterAlgorithm_Type()
)
moipInputDejitterAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moipInputDejitterAlgorithm.setStatus("current")


class _MoipInputDejitterBufLatency_Type(Integer32):
    """Custom type moipInputDejitterBufLatency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MoipInputDejitterBufLatency_Type.__name__ = "Integer32"
_MoipInputDejitterBufLatency_Object = MibScalar
moipInputDejitterBufLatency = _MoipInputDejitterBufLatency_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 41, 1, 10),
    _MoipInputDejitterBufLatency_Type()
)
moipInputDejitterBufLatency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moipInputDejitterBufLatency.setStatus("current")


class _MoipInputRednMode_Type(Integer32):
    """Custom type moipInputRednMode based on Integer32"""
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
        *(("bkpPriData1", 1),
          ("bkpPriData2", 2),
          ("manualData1", 3),
          ("manualData2", 4))
    )


_MoipInputRednMode_Type.__name__ = "Integer32"
_MoipInputRednMode_Object = MibScalar
moipInputRednMode = _MoipInputRednMode_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 41, 1, 11),
    _MoipInputRednMode_Type()
)
moipInputRednMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moipInputRednMode.setStatus("current")


class _MoipInputRednDir_Type(Integer32):
    """Custom type moipInputRednDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("Revertive", 1),
          ("nonRevertive", 2))
    )


_MoipInputRednDir_Type.__name__ = "Integer32"
_MoipInputRednDir_Object = MibScalar
moipInputRednDir = _MoipInputRednDir_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 41, 1, 12),
    _MoipInputRednDir_Type()
)
moipInputRednDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moipInputRednDir.setStatus("current")


class _MoipInputRednDelayDir_Type(Integer32):
    """Custom type moipInputRednDelayDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_MoipInputRednDelayDir_Type.__name__ = "Integer32"
_MoipInputRednDelayDir_Object = MibScalar
moipInputRednDelayDir = _MoipInputRednDelayDir_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 41, 1, 13),
    _MoipInputRednDelayDir_Type()
)
moipInputRednDelayDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moipInputRednDelayDir.setStatus("current")


class _MoipInputRednDelRev_Type(Integer32):
    """Custom type moipInputRednDelRev based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_MoipInputRednDelRev_Type.__name__ = "Integer32"
_MoipInputRednDelRev_Object = MibScalar
moipInputRednDelRev = _MoipInputRednDelRev_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 41, 1, 14),
    _MoipInputRednDelRev_Type()
)
moipInputRednDelRev.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moipInputRednDelRev.setStatus("current")


class _MoipInputRednPortInUse_Type(DisplayString):
    """Custom type moipInputRednPortInUse based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MoipInputRednPortInUse_Type.__name__ = "DisplayString"
_MoipInputRednPortInUse_Object = MibScalar
moipInputRednPortInUse = _MoipInputRednPortInUse_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 41, 1, 15),
    _MoipInputRednPortInUse_Type()
)
moipInputRednPortInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moipInputRednPortInUse.setStatus("current")


class _MoipInputRednSwReason_Type(DisplayString):
    """Custom type moipInputRednSwReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MoipInputRednSwReason_Type.__name__ = "DisplayString"
_MoipInputRednSwReason_Object = MibScalar
moipInputRednSwReason = _MoipInputRednSwReason_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 41, 1, 16),
    _MoipInputRednSwReason_Type()
)
moipInputRednSwReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moipInputRednSwReason.setStatus("current")


class _MoipInputRednSwDateTime_Type(DisplayString):
    """Custom type moipInputRednSwDateTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MoipInputRednSwDateTime_Type.__name__ = "DisplayString"
_MoipInputRednSwDateTime_Object = MibScalar
moipInputRednSwDateTime = _MoipInputRednSwDateTime_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 41, 1, 17),
    _MoipInputRednSwDateTime_Type()
)
moipInputRednSwDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moipInputRednSwDateTime.setStatus("current")
_MoipInputData1SelIPV4_Type = IpAddress
_MoipInputData1SelIPV4_Object = MibScalar
moipInputData1SelIPV4 = _MoipInputData1SelIPV4_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 41, 1, 18),
    _MoipInputData1SelIPV4_Type()
)
moipInputData1SelIPV4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moipInputData1SelIPV4.setStatus("current")
_MoipInputData2SelIPV4_Type = IpAddress
_MoipInputData2SelIPV4_Object = MibScalar
moipInputData2SelIPV4 = _MoipInputData2SelIPV4_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 41, 1, 19),
    _MoipInputData2SelIPV4_Type()
)
moipInputData2SelIPV4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moipInputData2SelIPV4.setStatus("current")
_MoipInputTable_ObjectIdentity = ObjectIdentity
moipInputTable = _MoipInputTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 41, 2)
)
_MoipInputSrcSelectTable_Object = MibTable
moipInputSrcSelectTable = _MoipInputSrcSelectTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 41, 2, 1)
)
if mibBuilder.loadTexts:
    moipInputSrcSelectTable.setStatus("current")
_MoipInputSrcSelectEntry_Object = MibTableRow
moipInputSrcSelectEntry = _MoipInputSrcSelectEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 41, 2, 1, 1)
)
moipInputSrcSelectEntry.setIndexNames(
    (0, "CISCO-DMN-DSG-MOIPINPUT-MIB", "moipInputSrcSelectIdx"),
)
if mibBuilder.loadTexts:
    moipInputSrcSelectEntry.setStatus("current")


class _MoipInputSrcSelectIdx_Type(Integer32):
    """Custom type moipInputSrcSelectIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_MoipInputSrcSelectIdx_Type.__name__ = "Integer32"
_MoipInputSrcSelectIdx_Object = MibTableColumn
moipInputSrcSelectIdx = _MoipInputSrcSelectIdx_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 41, 2, 1, 1, 1),
    _MoipInputSrcSelectIdx_Type()
)
moipInputSrcSelectIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moipInputSrcSelectIdx.setStatus("current")
_MoipInputSrcSelectV4IPAddr_Type = IpAddress
_MoipInputSrcSelectV4IPAddr_Object = MibTableColumn
moipInputSrcSelectV4IPAddr = _MoipInputSrcSelectV4IPAddr_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 41, 2, 1, 1, 2),
    _MoipInputSrcSelectV4IPAddr_Type()
)
moipInputSrcSelectV4IPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moipInputSrcSelectV4IPAddr.setStatus("current")


class _MoipInputSrcSelectData1Sel_Type(Integer32):
    """Custom type moipInputSrcSelectData1Sel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_MoipInputSrcSelectData1Sel_Type.__name__ = "Integer32"
_MoipInputSrcSelectData1Sel_Object = MibTableColumn
moipInputSrcSelectData1Sel = _MoipInputSrcSelectData1Sel_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 41, 2, 1, 1, 3),
    _MoipInputSrcSelectData1Sel_Type()
)
moipInputSrcSelectData1Sel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moipInputSrcSelectData1Sel.setStatus("current")


class _MoipInputSrcSelectData2Sel_Type(Integer32):
    """Custom type moipInputSrcSelectData2Sel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_MoipInputSrcSelectData2Sel_Type.__name__ = "Integer32"
_MoipInputSrcSelectData2Sel_Object = MibTableColumn
moipInputSrcSelectData2Sel = _MoipInputSrcSelectData2Sel_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 41, 2, 1, 1, 4),
    _MoipInputSrcSelectData2Sel_Type()
)
moipInputSrcSelectData2Sel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moipInputSrcSelectData2Sel.setStatus("current")


class _MoipInputSrcSelectData1Avail_Type(Integer32):
    """Custom type moipInputSrcSelectData1Avail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_MoipInputSrcSelectData1Avail_Type.__name__ = "Integer32"
_MoipInputSrcSelectData1Avail_Object = MibTableColumn
moipInputSrcSelectData1Avail = _MoipInputSrcSelectData1Avail_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 41, 2, 1, 1, 5),
    _MoipInputSrcSelectData1Avail_Type()
)
moipInputSrcSelectData1Avail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moipInputSrcSelectData1Avail.setStatus("current")


class _MoipInputSrcSelectData2Avail_Type(Integer32):
    """Custom type moipInputSrcSelectData2Avail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_MoipInputSrcSelectData2Avail_Type.__name__ = "Integer32"
_MoipInputSrcSelectData2Avail_Object = MibTableColumn
moipInputSrcSelectData2Avail = _MoipInputSrcSelectData2Avail_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 41, 2, 1, 1, 6),
    _MoipInputSrcSelectData2Avail_Type()
)
moipInputSrcSelectData2Avail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moipInputSrcSelectData2Avail.setStatus("current")


class _MoipInputSrcSelectData1Enabled_Type(Integer32):
    """Custom type moipInputSrcSelectData1Enabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_MoipInputSrcSelectData1Enabled_Type.__name__ = "Integer32"
_MoipInputSrcSelectData1Enabled_Object = MibTableColumn
moipInputSrcSelectData1Enabled = _MoipInputSrcSelectData1Enabled_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 41, 2, 1, 1, 7),
    _MoipInputSrcSelectData1Enabled_Type()
)
moipInputSrcSelectData1Enabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moipInputSrcSelectData1Enabled.setStatus("current")


class _MoipInputSrcSelectData2Enabled_Type(Integer32):
    """Custom type moipInputSrcSelectData2Enabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_MoipInputSrcSelectData2Enabled_Type.__name__ = "Integer32"
_MoipInputSrcSelectData2Enabled_Object = MibTableColumn
moipInputSrcSelectData2Enabled = _MoipInputSrcSelectData2Enabled_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 41, 2, 1, 1, 8),
    _MoipInputSrcSelectData2Enabled_Type()
)
moipInputSrcSelectData2Enabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moipInputSrcSelectData2Enabled.setStatus("current")


class _MoipInputSrcSelectRowEnabled_Type(Integer32):
    """Custom type moipInputSrcSelectRowEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_MoipInputSrcSelectRowEnabled_Type.__name__ = "Integer32"
_MoipInputSrcSelectRowEnabled_Object = MibTableColumn
moipInputSrcSelectRowEnabled = _MoipInputSrcSelectRowEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 41, 2, 1, 1, 9),
    _MoipInputSrcSelectRowEnabled_Type()
)
moipInputSrcSelectRowEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moipInputSrcSelectRowEnabled.setStatus("current")
_MoipInputSrcFilterTable_Object = MibTable
moipInputSrcFilterTable = _MoipInputSrcFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 41, 2, 2)
)
if mibBuilder.loadTexts:
    moipInputSrcFilterTable.setStatus("current")
_MoipInputSrcFilterEntry_Object = MibTableRow
moipInputSrcFilterEntry = _MoipInputSrcFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 41, 2, 2, 1)
)
moipInputSrcFilterEntry.setIndexNames(
    (0, "CISCO-DMN-DSG-MOIPINPUT-MIB", "moipInputSrcFilterIdx"),
)
if mibBuilder.loadTexts:
    moipInputSrcFilterEntry.setStatus("current")


class _MoipInputSrcFilterIdx_Type(Integer32):
    """Custom type moipInputSrcFilterIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_MoipInputSrcFilterIdx_Type.__name__ = "Integer32"
_MoipInputSrcFilterIdx_Object = MibTableColumn
moipInputSrcFilterIdx = _MoipInputSrcFilterIdx_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 41, 2, 2, 1, 1),
    _MoipInputSrcFilterIdx_Type()
)
moipInputSrcFilterIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moipInputSrcFilterIdx.setStatus("current")
_MoipInputSrcFilterV4IPAddr_Type = IpAddress
_MoipInputSrcFilterV4IPAddr_Object = MibTableColumn
moipInputSrcFilterV4IPAddr = _MoipInputSrcFilterV4IPAddr_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 41, 2, 2, 1, 2),
    _MoipInputSrcFilterV4IPAddr_Type()
)
moipInputSrcFilterV4IPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moipInputSrcFilterV4IPAddr.setStatus("current")
_MoipInputSrcFilterRowStatus_Type = RowStatus
_MoipInputSrcFilterRowStatus_Object = MibTableColumn
moipInputSrcFilterRowStatus = _MoipInputSrcFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 41, 2, 2, 1, 3),
    _MoipInputSrcFilterRowStatus_Type()
)
moipInputSrcFilterRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moipInputSrcFilterRowStatus.setStatus("current")
_MoipInputFlowTable_Object = MibTable
moipInputFlowTable = _MoipInputFlowTable_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 41, 2, 3)
)
if mibBuilder.loadTexts:
    moipInputFlowTable.setStatus("current")
_MoipInputFlowEntry_Object = MibTableRow
moipInputFlowEntry = _MoipInputFlowEntry_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 41, 2, 3, 1)
)
moipInputFlowEntry.setIndexNames(
    (0, "CISCO-DMN-DSG-MOIPINPUT-MIB", "moipInputFlowID"),
)
if mibBuilder.loadTexts:
    moipInputFlowEntry.setStatus("current")


class _MoipInputFlowID_Type(Integer32):
    """Custom type moipInputFlowID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_MoipInputFlowID_Type.__name__ = "Integer32"
_MoipInputFlowID_Object = MibTableColumn
moipInputFlowID = _MoipInputFlowID_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 41, 2, 3, 1, 1),
    _MoipInputFlowID_Type()
)
moipInputFlowID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moipInputFlowID.setStatus("current")


class _MoipInputFlowTsAct_Type(Integer32):
    """Custom type moipInputFlowTsAct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_MoipInputFlowTsAct_Type.__name__ = "Integer32"
_MoipInputFlowTsAct_Object = MibTableColumn
moipInputFlowTsAct = _MoipInputFlowTsAct_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 41, 2, 3, 1, 2),
    _MoipInputFlowTsAct_Type()
)
moipInputFlowTsAct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moipInputFlowTsAct.setStatus("current")


class _MoipInputFlowFecColStrmAct_Type(Integer32):
    """Custom type moipInputFlowFecColStrmAct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_MoipInputFlowFecColStrmAct_Type.__name__ = "Integer32"
_MoipInputFlowFecColStrmAct_Object = MibTableColumn
moipInputFlowFecColStrmAct = _MoipInputFlowFecColStrmAct_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 41, 2, 3, 1, 3),
    _MoipInputFlowFecColStrmAct_Type()
)
moipInputFlowFecColStrmAct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moipInputFlowFecColStrmAct.setStatus("current")


class _MoipInputFlowFecRowStrmAct_Type(Integer32):
    """Custom type moipInputFlowFecRowStrmAct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_MoipInputFlowFecRowStrmAct_Type.__name__ = "Integer32"
_MoipInputFlowFecRowStrmAct_Object = MibTableColumn
moipInputFlowFecRowStrmAct = _MoipInputFlowFecRowStrmAct_Object(
    (1, 3, 6, 1, 4, 1, 1429, 2, 2, 5, 41, 2, 3, 1, 4),
    _MoipInputFlowFecRowStrmAct_Type()
)
moipInputFlowFecRowStrmAct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moipInputFlowFecRowStrmAct.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DMN-DSG-MOIPINPUT-MIB",
    **{"ciscoDSGMOIPInput": ciscoDSGMOIPInput,
       "moipInputInfo": moipInputInfo,
       "moipInputFlowIsMulticast": moipInputFlowIsMulticast,
       "moipInputFlowMulticastDstIPV4": moipInputFlowMulticastDstIPV4,
       "moipInputFlowFecMode": moipInputFlowFecMode,
       "moipInputFlowSrcFilter": moipInputFlowSrcFilter,
       "moipInputFlowTsUDPPort": moipInputFlowTsUDPPort,
       "moipInputFlowFec1UDPPort": moipInputFlowFec1UDPPort,
       "moipInputFlowFec2UDPPort": moipInputFlowFec2UDPPort,
       "moipInputFlowSrcStrmSel": moipInputFlowSrcStrmSel,
       "moipInputDejitterAlgorithm": moipInputDejitterAlgorithm,
       "moipInputDejitterBufLatency": moipInputDejitterBufLatency,
       "moipInputRednMode": moipInputRednMode,
       "moipInputRednDir": moipInputRednDir,
       "moipInputRednDelayDir": moipInputRednDelayDir,
       "moipInputRednDelRev": moipInputRednDelRev,
       "moipInputRednPortInUse": moipInputRednPortInUse,
       "moipInputRednSwReason": moipInputRednSwReason,
       "moipInputRednSwDateTime": moipInputRednSwDateTime,
       "moipInputData1SelIPV4": moipInputData1SelIPV4,
       "moipInputData2SelIPV4": moipInputData2SelIPV4,
       "moipInputTable": moipInputTable,
       "moipInputSrcSelectTable": moipInputSrcSelectTable,
       "moipInputSrcSelectEntry": moipInputSrcSelectEntry,
       "moipInputSrcSelectIdx": moipInputSrcSelectIdx,
       "moipInputSrcSelectV4IPAddr": moipInputSrcSelectV4IPAddr,
       "moipInputSrcSelectData1Sel": moipInputSrcSelectData1Sel,
       "moipInputSrcSelectData2Sel": moipInputSrcSelectData2Sel,
       "moipInputSrcSelectData1Avail": moipInputSrcSelectData1Avail,
       "moipInputSrcSelectData2Avail": moipInputSrcSelectData2Avail,
       "moipInputSrcSelectData1Enabled": moipInputSrcSelectData1Enabled,
       "moipInputSrcSelectData2Enabled": moipInputSrcSelectData2Enabled,
       "moipInputSrcSelectRowEnabled": moipInputSrcSelectRowEnabled,
       "moipInputSrcFilterTable": moipInputSrcFilterTable,
       "moipInputSrcFilterEntry": moipInputSrcFilterEntry,
       "moipInputSrcFilterIdx": moipInputSrcFilterIdx,
       "moipInputSrcFilterV4IPAddr": moipInputSrcFilterV4IPAddr,
       "moipInputSrcFilterRowStatus": moipInputSrcFilterRowStatus,
       "moipInputFlowTable": moipInputFlowTable,
       "moipInputFlowEntry": moipInputFlowEntry,
       "moipInputFlowID": moipInputFlowID,
       "moipInputFlowTsAct": moipInputFlowTsAct,
       "moipInputFlowFecColStrmAct": moipInputFlowFecColStrmAct,
       "moipInputFlowFecRowStrmAct": moipInputFlowFecRowStrmAct}
)
