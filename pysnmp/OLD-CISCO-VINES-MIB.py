# SNMP MIB module (OLD-CISCO-VINES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OLD-CISCO-VINES-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:34:08 2024
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

(temporary,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "temporary")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Tmpvines_ObjectIdentity = ObjectIdentity
tmpvines = _Tmpvines_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 3, 5)
)
_VinesInput_Type = Integer32
_VinesInput_Object = MibScalar
vinesInput = _VinesInput_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 1),
    _VinesInput_Type()
)
vinesInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesInput.setStatus("mandatory")
_VinesOutput_Type = Integer32
_VinesOutput_Object = MibScalar
vinesOutput = _VinesOutput_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 2),
    _VinesOutput_Type()
)
vinesOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesOutput.setStatus("mandatory")
_VinesLocaldest_Type = Integer32
_VinesLocaldest_Object = MibScalar
vinesLocaldest = _VinesLocaldest_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 3),
    _VinesLocaldest_Type()
)
vinesLocaldest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesLocaldest.setStatus("mandatory")
_VinesForwarded_Type = Integer32
_VinesForwarded_Object = MibScalar
vinesForwarded = _VinesForwarded_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 4),
    _VinesForwarded_Type()
)
vinesForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesForwarded.setStatus("mandatory")
_VinesBcastin_Type = Integer32
_VinesBcastin_Object = MibScalar
vinesBcastin = _VinesBcastin_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 5),
    _VinesBcastin_Type()
)
vinesBcastin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesBcastin.setStatus("mandatory")
_VinesBcastout_Type = Integer32
_VinesBcastout_Object = MibScalar
vinesBcastout = _VinesBcastout_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 6),
    _VinesBcastout_Type()
)
vinesBcastout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesBcastout.setStatus("mandatory")
_VinesBcastfwd_Type = Integer32
_VinesBcastfwd_Object = MibScalar
vinesBcastfwd = _VinesBcastfwd_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 7),
    _VinesBcastfwd_Type()
)
vinesBcastfwd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesBcastfwd.setStatus("mandatory")
_VinesNotlan_Type = Integer32
_VinesNotlan_Object = MibScalar
vinesNotlan = _VinesNotlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 8),
    _VinesNotlan_Type()
)
vinesNotlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesNotlan.setStatus("mandatory")
_VinesNotgt4800_Type = Integer32
_VinesNotgt4800_Object = MibScalar
vinesNotgt4800 = _VinesNotgt4800_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 9),
    _VinesNotgt4800_Type()
)
vinesNotgt4800.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesNotgt4800.setStatus("mandatory")
_VinesNocharges_Type = Integer32
_VinesNocharges_Object = MibScalar
vinesNocharges = _VinesNocharges_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 10),
    _VinesNocharges_Type()
)
vinesNocharges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesNocharges.setStatus("mandatory")
_VinesFormaterror_Type = Integer32
_VinesFormaterror_Object = MibScalar
vinesFormaterror = _VinesFormaterror_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 11),
    _VinesFormaterror_Type()
)
vinesFormaterror.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesFormaterror.setStatus("mandatory")
_VinesCksumerr_Type = Integer32
_VinesCksumerr_Object = MibScalar
vinesCksumerr = _VinesCksumerr_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 12),
    _VinesCksumerr_Type()
)
vinesCksumerr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesCksumerr.setStatus("mandatory")
_VinesHopcount_Type = Integer32
_VinesHopcount_Object = MibScalar
vinesHopcount = _VinesHopcount_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 13),
    _VinesHopcount_Type()
)
vinesHopcount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesHopcount.setStatus("mandatory")
_VinesNoroute_Type = Integer32
_VinesNoroute_Object = MibScalar
vinesNoroute = _VinesNoroute_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 14),
    _VinesNoroute_Type()
)
vinesNoroute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesNoroute.setStatus("mandatory")
_VinesEncapsfailed_Type = Integer32
_VinesEncapsfailed_Object = MibScalar
vinesEncapsfailed = _VinesEncapsfailed_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 15),
    _VinesEncapsfailed_Type()
)
vinesEncapsfailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesEncapsfailed.setStatus("mandatory")
_VinesUnknown_Type = Integer32
_VinesUnknown_Object = MibScalar
vinesUnknown = _VinesUnknown_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 16),
    _VinesUnknown_Type()
)
vinesUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesUnknown.setStatus("mandatory")
_VinesIcpIn_Type = Integer32
_VinesIcpIn_Object = MibScalar
vinesIcpIn = _VinesIcpIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 17),
    _VinesIcpIn_Type()
)
vinesIcpIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIcpIn.setStatus("mandatory")
_VinesIcpOut_Type = Integer32
_VinesIcpOut_Object = MibScalar
vinesIcpOut = _VinesIcpOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 18),
    _VinesIcpOut_Type()
)
vinesIcpOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIcpOut.setStatus("mandatory")
_VinesMetricOut_Type = Integer32
_VinesMetricOut_Object = MibScalar
vinesMetricOut = _VinesMetricOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 19),
    _VinesMetricOut_Type()
)
vinesMetricOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesMetricOut.setStatus("mandatory")
_VinesMacEchoIn_Type = Integer32
_VinesMacEchoIn_Object = MibScalar
vinesMacEchoIn = _VinesMacEchoIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 20),
    _VinesMacEchoIn_Type()
)
vinesMacEchoIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesMacEchoIn.setStatus("mandatory")
_VinesMacEchoOut_Type = Integer32
_VinesMacEchoOut_Object = MibScalar
vinesMacEchoOut = _VinesMacEchoOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 21),
    _VinesMacEchoOut_Type()
)
vinesMacEchoOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesMacEchoOut.setStatus("mandatory")
_VinesEchoIn_Type = Integer32
_VinesEchoIn_Object = MibScalar
vinesEchoIn = _VinesEchoIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 22),
    _VinesEchoIn_Type()
)
vinesEchoIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesEchoIn.setStatus("mandatory")
_VinesEchoOut_Type = Integer32
_VinesEchoOut_Object = MibScalar
vinesEchoOut = _VinesEchoOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 23),
    _VinesEchoOut_Type()
)
vinesEchoOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesEchoOut.setStatus("mandatory")
_VinesProxyCnt_Type = Counter32
_VinesProxyCnt_Object = MibScalar
vinesProxyCnt = _VinesProxyCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 24),
    _VinesProxyCnt_Type()
)
vinesProxyCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesProxyCnt.setStatus("mandatory")
_VinesProxyReplyCnt_Type = Counter32
_VinesProxyReplyCnt_Object = MibScalar
vinesProxyReplyCnt = _VinesProxyReplyCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 25),
    _VinesProxyReplyCnt_Type()
)
vinesProxyReplyCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesProxyReplyCnt.setStatus("mandatory")
_VinesNet_Type = Integer32
_VinesNet_Object = MibScalar
vinesNet = _VinesNet_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 26),
    _VinesNet_Type()
)
vinesNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesNet.setStatus("mandatory")
_VinesSubNet_Type = Integer32
_VinesSubNet_Object = MibScalar
vinesSubNet = _VinesSubNet_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 27),
    _VinesSubNet_Type()
)
vinesSubNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesSubNet.setStatus("mandatory")
_VinesClient_Type = Integer32
_VinesClient_Object = MibScalar
vinesClient = _VinesClient_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 28),
    _VinesClient_Type()
)
vinesClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesClient.setStatus("mandatory")
_VinesIfTable_Object = MibTable
vinesIfTable = _VinesIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29)
)
if mibBuilder.loadTexts:
    vinesIfTable.setStatus("mandatory")
_VinesIfTableEntry_Object = MibTableRow
vinesIfTableEntry = _VinesIfTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1)
)
vinesIfTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    vinesIfTableEntry.setStatus("mandatory")
_VinesIfMetric_Type = Integer32
_VinesIfMetric_Object = MibTableColumn
vinesIfMetric = _VinesIfMetric_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 1),
    _VinesIfMetric_Type()
)
vinesIfMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfMetric.setStatus("mandatory")
_VinesIfEnctype_Type = Integer32
_VinesIfEnctype_Object = MibTableColumn
vinesIfEnctype = _VinesIfEnctype_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 2),
    _VinesIfEnctype_Type()
)
vinesIfEnctype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfEnctype.setStatus("mandatory")
_VinesIfAccesslist_Type = Integer32
_VinesIfAccesslist_Object = MibTableColumn
vinesIfAccesslist = _VinesIfAccesslist_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 3),
    _VinesIfAccesslist_Type()
)
vinesIfAccesslist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfAccesslist.setStatus("mandatory")


class _VinesIfPropagate_Type(Integer32):
    """Custom type vinesIfPropagate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alwaysPropagate", 2),
          ("dynamicPropagate", 3),
          ("neverPropagate", 1))
    )


_VinesIfPropagate_Type.__name__ = "Integer32"
_VinesIfPropagate_Object = MibTableColumn
vinesIfPropagate = _VinesIfPropagate_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 4),
    _VinesIfPropagate_Type()
)
vinesIfPropagate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfPropagate.setStatus("mandatory")
_VinesIfArpEnabled_Type = Integer32
_VinesIfArpEnabled_Object = MibTableColumn
vinesIfArpEnabled = _VinesIfArpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 5),
    _VinesIfArpEnabled_Type()
)
vinesIfArpEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfArpEnabled.setStatus("mandatory")


class _VinesIfServerless_Type(Integer32):
    """Custom type vinesIfServerless based on Integer32"""
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
        *(("alwaysBcastSvrless", 4),
          ("alwaysSvrless", 3),
          ("dynamicSvrless", 2),
          ("neverSvrless", 1))
    )


_VinesIfServerless_Type.__name__ = "Integer32"
_VinesIfServerless_Object = MibTableColumn
vinesIfServerless = _VinesIfServerless_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 6),
    _VinesIfServerless_Type()
)
vinesIfServerless.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfServerless.setStatus("mandatory")
_VinesIfRedirectInterval_Type = Integer32
_VinesIfRedirectInterval_Object = MibTableColumn
vinesIfRedirectInterval = _VinesIfRedirectInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 8),
    _VinesIfRedirectInterval_Type()
)
vinesIfRedirectInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfRedirectInterval.setStatus("mandatory")
_VinesIfSplitDisabled_Type = Integer32
_VinesIfSplitDisabled_Object = MibTableColumn
vinesIfSplitDisabled = _VinesIfSplitDisabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 9),
    _VinesIfSplitDisabled_Type()
)
vinesIfSplitDisabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfSplitDisabled.setStatus("mandatory")
_VinesIfLineup_Type = Integer32
_VinesIfLineup_Object = MibTableColumn
vinesIfLineup = _VinesIfLineup_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 10),
    _VinesIfLineup_Type()
)
vinesIfLineup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfLineup.setStatus("mandatory")
_VinesIfFastokay_Type = Integer32
_VinesIfFastokay_Object = MibTableColumn
vinesIfFastokay = _VinesIfFastokay_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 11),
    _VinesIfFastokay_Type()
)
vinesIfFastokay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfFastokay.setStatus("mandatory")
_VinesIfRouteCache_Type = Integer32
_VinesIfRouteCache_Object = MibTableColumn
vinesIfRouteCache = _VinesIfRouteCache_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 12),
    _VinesIfRouteCache_Type()
)
vinesIfRouteCache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfRouteCache.setStatus("mandatory")
_VinesIfRxNotEnabledCnt_Type = Counter32
_VinesIfRxNotEnabledCnt_Object = MibTableColumn
vinesIfRxNotEnabledCnt = _VinesIfRxNotEnabledCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 17),
    _VinesIfRxNotEnabledCnt_Type()
)
vinesIfRxNotEnabledCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfRxNotEnabledCnt.setStatus("mandatory")
_VinesIfRxFormatErrorCnt_Type = Counter32
_VinesIfRxFormatErrorCnt_Object = MibTableColumn
vinesIfRxFormatErrorCnt = _VinesIfRxFormatErrorCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 18),
    _VinesIfRxFormatErrorCnt_Type()
)
vinesIfRxFormatErrorCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfRxFormatErrorCnt.setStatus("mandatory")
_VinesIfRxLocalDestCnt_Type = Counter32
_VinesIfRxLocalDestCnt_Object = MibTableColumn
vinesIfRxLocalDestCnt = _VinesIfRxLocalDestCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 19),
    _VinesIfRxLocalDestCnt_Type()
)
vinesIfRxLocalDestCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfRxLocalDestCnt.setStatus("mandatory")
_VinesIfRxBcastinCnt_Type = Counter32
_VinesIfRxBcastinCnt_Object = MibTableColumn
vinesIfRxBcastinCnt = _VinesIfRxBcastinCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 20),
    _VinesIfRxBcastinCnt_Type()
)
vinesIfRxBcastinCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfRxBcastinCnt.setStatus("mandatory")
_VinesIfRxForwardedCnt_Type = Counter32
_VinesIfRxForwardedCnt_Object = MibTableColumn
vinesIfRxForwardedCnt = _VinesIfRxForwardedCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 21),
    _VinesIfRxForwardedCnt_Type()
)
vinesIfRxForwardedCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfRxForwardedCnt.setStatus("mandatory")
_VinesIfRxNoRouteCnt_Type = Counter32
_VinesIfRxNoRouteCnt_Object = MibTableColumn
vinesIfRxNoRouteCnt = _VinesIfRxNoRouteCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 22),
    _VinesIfRxNoRouteCnt_Type()
)
vinesIfRxNoRouteCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfRxNoRouteCnt.setStatus("mandatory")
_VinesIfRxZeroHopCountCnt_Type = Counter32
_VinesIfRxZeroHopCountCnt_Object = MibTableColumn
vinesIfRxZeroHopCountCnt = _VinesIfRxZeroHopCountCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 23),
    _VinesIfRxZeroHopCountCnt_Type()
)
vinesIfRxZeroHopCountCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfRxZeroHopCountCnt.setStatus("mandatory")
_VinesIfRxChecksumErrorCnt_Type = Counter32
_VinesIfRxChecksumErrorCnt_Object = MibTableColumn
vinesIfRxChecksumErrorCnt = _VinesIfRxChecksumErrorCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 24),
    _VinesIfRxChecksumErrorCnt_Type()
)
vinesIfRxChecksumErrorCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfRxChecksumErrorCnt.setStatus("mandatory")
_VinesIfRxArp0Cnt_Type = Counter32
_VinesIfRxArp0Cnt_Object = MibTableColumn
vinesIfRxArp0Cnt = _VinesIfRxArp0Cnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 25),
    _VinesIfRxArp0Cnt_Type()
)
vinesIfRxArp0Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfRxArp0Cnt.setStatus("mandatory")
_VinesIfRxArp1Cnt_Type = Counter32
_VinesIfRxArp1Cnt_Object = MibTableColumn
vinesIfRxArp1Cnt = _VinesIfRxArp1Cnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 26),
    _VinesIfRxArp1Cnt_Type()
)
vinesIfRxArp1Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfRxArp1Cnt.setStatus("mandatory")
_VinesIfRxArp2Cnt_Type = Counter32
_VinesIfRxArp2Cnt_Object = MibTableColumn
vinesIfRxArp2Cnt = _VinesIfRxArp2Cnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 27),
    _VinesIfRxArp2Cnt_Type()
)
vinesIfRxArp2Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfRxArp2Cnt.setStatus("mandatory")
_VinesIfRxArp3Cnt_Type = Counter32
_VinesIfRxArp3Cnt_Object = MibTableColumn
vinesIfRxArp3Cnt = _VinesIfRxArp3Cnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 28),
    _VinesIfRxArp3Cnt_Type()
)
vinesIfRxArp3Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfRxArp3Cnt.setStatus("mandatory")
_VinesIfRxArpIllegalCnt_Type = Counter32
_VinesIfRxArpIllegalCnt_Object = MibTableColumn
vinesIfRxArpIllegalCnt = _VinesIfRxArpIllegalCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 29),
    _VinesIfRxArpIllegalCnt_Type()
)
vinesIfRxArpIllegalCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfRxArpIllegalCnt.setStatus("mandatory")
_VinesIfRxIcpErrorCnt_Type = Counter32
_VinesIfRxIcpErrorCnt_Object = MibTableColumn
vinesIfRxIcpErrorCnt = _VinesIfRxIcpErrorCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 30),
    _VinesIfRxIcpErrorCnt_Type()
)
vinesIfRxIcpErrorCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfRxIcpErrorCnt.setStatus("mandatory")
_VinesIfRxIcpMetricCnt_Type = Counter32
_VinesIfRxIcpMetricCnt_Object = MibTableColumn
vinesIfRxIcpMetricCnt = _VinesIfRxIcpMetricCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 31),
    _VinesIfRxIcpMetricCnt_Type()
)
vinesIfRxIcpMetricCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfRxIcpMetricCnt.setStatus("mandatory")
_VinesIfRxIcpIllegalCnt_Type = Counter32
_VinesIfRxIcpIllegalCnt_Object = MibTableColumn
vinesIfRxIcpIllegalCnt = _VinesIfRxIcpIllegalCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 32),
    _VinesIfRxIcpIllegalCnt_Type()
)
vinesIfRxIcpIllegalCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfRxIcpIllegalCnt.setStatus("mandatory")
_VinesIfRxIpcCnt_Type = Counter32
_VinesIfRxIpcCnt_Object = MibTableColumn
vinesIfRxIpcCnt = _VinesIfRxIpcCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 33),
    _VinesIfRxIpcCnt_Type()
)
vinesIfRxIpcCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfRxIpcCnt.setStatus("mandatory")
_VinesIfRxRtp0Cnt_Type = Counter32
_VinesIfRxRtp0Cnt_Object = MibTableColumn
vinesIfRxRtp0Cnt = _VinesIfRxRtp0Cnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 34),
    _VinesIfRxRtp0Cnt_Type()
)
vinesIfRxRtp0Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfRxRtp0Cnt.setStatus("mandatory")
_VinesIfRxRtp1Cnt_Type = Counter32
_VinesIfRxRtp1Cnt_Object = MibTableColumn
vinesIfRxRtp1Cnt = _VinesIfRxRtp1Cnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 35),
    _VinesIfRxRtp1Cnt_Type()
)
vinesIfRxRtp1Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfRxRtp1Cnt.setStatus("mandatory")
_VinesIfRxRtp2Cnt_Type = Counter32
_VinesIfRxRtp2Cnt_Object = MibTableColumn
vinesIfRxRtp2Cnt = _VinesIfRxRtp2Cnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 36),
    _VinesIfRxRtp2Cnt_Type()
)
vinesIfRxRtp2Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfRxRtp2Cnt.setStatus("mandatory")
_VinesIfRxRtp3Cnt_Type = Counter32
_VinesIfRxRtp3Cnt_Object = MibTableColumn
vinesIfRxRtp3Cnt = _VinesIfRxRtp3Cnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 37),
    _VinesIfRxRtp3Cnt_Type()
)
vinesIfRxRtp3Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfRxRtp3Cnt.setStatus("mandatory")
_VinesIfRxRtp4Cnt_Type = Counter32
_VinesIfRxRtp4Cnt_Object = MibTableColumn
vinesIfRxRtp4Cnt = _VinesIfRxRtp4Cnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 38),
    _VinesIfRxRtp4Cnt_Type()
)
vinesIfRxRtp4Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfRxRtp4Cnt.setStatus("mandatory")
_VinesIfRxRtp5Cnt_Type = Counter32
_VinesIfRxRtp5Cnt_Object = MibTableColumn
vinesIfRxRtp5Cnt = _VinesIfRxRtp5Cnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 39),
    _VinesIfRxRtp5Cnt_Type()
)
vinesIfRxRtp5Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfRxRtp5Cnt.setStatus("mandatory")
_VinesIfRxRtp6Cnt_Type = Counter32
_VinesIfRxRtp6Cnt_Object = MibTableColumn
vinesIfRxRtp6Cnt = _VinesIfRxRtp6Cnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 40),
    _VinesIfRxRtp6Cnt_Type()
)
vinesIfRxRtp6Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfRxRtp6Cnt.setStatus("mandatory")
_VinesIfRxRtpIllegalCnt_Type = Counter32
_VinesIfRxRtpIllegalCnt_Object = MibTableColumn
vinesIfRxRtpIllegalCnt = _VinesIfRxRtpIllegalCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 41),
    _VinesIfRxRtpIllegalCnt_Type()
)
vinesIfRxRtpIllegalCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfRxRtpIllegalCnt.setStatus("mandatory")
_VinesIfRxSppCnt_Type = Counter32
_VinesIfRxSppCnt_Object = MibTableColumn
vinesIfRxSppCnt = _VinesIfRxSppCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 42),
    _VinesIfRxSppCnt_Type()
)
vinesIfRxSppCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfRxSppCnt.setStatus("mandatory")
_VinesIfRxIpUnknownCnt_Type = Counter32
_VinesIfRxIpUnknownCnt_Object = MibTableColumn
vinesIfRxIpUnknownCnt = _VinesIfRxIpUnknownCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 43),
    _VinesIfRxIpUnknownCnt_Type()
)
vinesIfRxIpUnknownCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfRxIpUnknownCnt.setStatus("mandatory")
_VinesIfRxIpcUnknownCnt_Type = Counter32
_VinesIfRxIpcUnknownCnt_Object = MibTableColumn
vinesIfRxIpcUnknownCnt = _VinesIfRxIpcUnknownCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 44),
    _VinesIfRxIpcUnknownCnt_Type()
)
vinesIfRxIpcUnknownCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfRxIpcUnknownCnt.setStatus("mandatory")
_VinesIfRxBcastHelperedCnt_Type = Counter32
_VinesIfRxBcastHelperedCnt_Object = MibTableColumn
vinesIfRxBcastHelperedCnt = _VinesIfRxBcastHelperedCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 45),
    _VinesIfRxBcastHelperedCnt_Type()
)
vinesIfRxBcastHelperedCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfRxBcastHelperedCnt.setStatus("mandatory")
_VinesIfRxBcastForwardedCnt_Type = Counter32
_VinesIfRxBcastForwardedCnt_Object = MibTableColumn
vinesIfRxBcastForwardedCnt = _VinesIfRxBcastForwardedCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 46),
    _VinesIfRxBcastForwardedCnt_Type()
)
vinesIfRxBcastForwardedCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfRxBcastForwardedCnt.setStatus("mandatory")
_VinesIfRxBcastDuplicateCnt_Type = Counter32
_VinesIfRxBcastDuplicateCnt_Object = MibTableColumn
vinesIfRxBcastDuplicateCnt = _VinesIfRxBcastDuplicateCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 47),
    _VinesIfRxBcastDuplicateCnt_Type()
)
vinesIfRxBcastDuplicateCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfRxBcastDuplicateCnt.setStatus("mandatory")
_VinesIfRxEchoCnt_Type = Counter32
_VinesIfRxEchoCnt_Object = MibTableColumn
vinesIfRxEchoCnt = _VinesIfRxEchoCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 48),
    _VinesIfRxEchoCnt_Type()
)
vinesIfRxEchoCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfRxEchoCnt.setStatus("mandatory")
_VinesIfRxMacEchoCnt_Type = Counter32
_VinesIfRxMacEchoCnt_Object = MibTableColumn
vinesIfRxMacEchoCnt = _VinesIfRxMacEchoCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 49),
    _VinesIfRxMacEchoCnt_Type()
)
vinesIfRxMacEchoCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfRxMacEchoCnt.setStatus("mandatory")
_VinesIfRxProxyReplyCnt_Type = Counter32
_VinesIfRxProxyReplyCnt_Object = MibTableColumn
vinesIfRxProxyReplyCnt = _VinesIfRxProxyReplyCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 50),
    _VinesIfRxProxyReplyCnt_Type()
)
vinesIfRxProxyReplyCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfRxProxyReplyCnt.setStatus("mandatory")
_VinesIfTxUnicastCnt_Type = Counter32
_VinesIfTxUnicastCnt_Object = MibTableColumn
vinesIfTxUnicastCnt = _VinesIfTxUnicastCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 51),
    _VinesIfTxUnicastCnt_Type()
)
vinesIfTxUnicastCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfTxUnicastCnt.setStatus("mandatory")
_VinesIfTxBcastCnt_Type = Counter32
_VinesIfTxBcastCnt_Object = MibTableColumn
vinesIfTxBcastCnt = _VinesIfTxBcastCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 52),
    _VinesIfTxBcastCnt_Type()
)
vinesIfTxBcastCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfTxBcastCnt.setStatus("mandatory")
_VinesIfTxForwardedCnt_Type = Counter32
_VinesIfTxForwardedCnt_Object = MibTableColumn
vinesIfTxForwardedCnt = _VinesIfTxForwardedCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 53),
    _VinesIfTxForwardedCnt_Type()
)
vinesIfTxForwardedCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfTxForwardedCnt.setStatus("mandatory")
_VinesIfTxFailedEncapsCnt_Type = Counter32
_VinesIfTxFailedEncapsCnt_Object = MibTableColumn
vinesIfTxFailedEncapsCnt = _VinesIfTxFailedEncapsCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 54),
    _VinesIfTxFailedEncapsCnt_Type()
)
vinesIfTxFailedEncapsCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfTxFailedEncapsCnt.setStatus("mandatory")
_VinesIfTxFailedAccessCnt_Type = Counter32
_VinesIfTxFailedAccessCnt_Object = MibTableColumn
vinesIfTxFailedAccessCnt = _VinesIfTxFailedAccessCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 55),
    _VinesIfTxFailedAccessCnt_Type()
)
vinesIfTxFailedAccessCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfTxFailedAccessCnt.setStatus("mandatory")
_VinesIfTxFailedDownCnt_Type = Counter32
_VinesIfTxFailedDownCnt_Object = MibTableColumn
vinesIfTxFailedDownCnt = _VinesIfTxFailedDownCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 56),
    _VinesIfTxFailedDownCnt_Type()
)
vinesIfTxFailedDownCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfTxFailedDownCnt.setStatus("mandatory")
_VinesIfTxNotBcastToSourceCnt_Type = Counter32
_VinesIfTxNotBcastToSourceCnt_Object = MibTableColumn
vinesIfTxNotBcastToSourceCnt = _VinesIfTxNotBcastToSourceCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 57),
    _VinesIfTxNotBcastToSourceCnt_Type()
)
vinesIfTxNotBcastToSourceCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfTxNotBcastToSourceCnt.setStatus("mandatory")
_VinesIfTxNotBcastNotlanCnt_Type = Counter32
_VinesIfTxNotBcastNotlanCnt_Object = MibTableColumn
vinesIfTxNotBcastNotlanCnt = _VinesIfTxNotBcastNotlanCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 58),
    _VinesIfTxNotBcastNotlanCnt_Type()
)
vinesIfTxNotBcastNotlanCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfTxNotBcastNotlanCnt.setStatus("mandatory")
_VinesIfTxNotBcastNotgt4800Cnt_Type = Counter32
_VinesIfTxNotBcastNotgt4800Cnt_Object = MibTableColumn
vinesIfTxNotBcastNotgt4800Cnt = _VinesIfTxNotBcastNotgt4800Cnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 59),
    _VinesIfTxNotBcastNotgt4800Cnt_Type()
)
vinesIfTxNotBcastNotgt4800Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfTxNotBcastNotgt4800Cnt.setStatus("mandatory")
_VinesIfTxNotBcastPpchargeCnt_Type = Counter32
_VinesIfTxNotBcastPpchargeCnt_Object = MibTableColumn
vinesIfTxNotBcastPpchargeCnt = _VinesIfTxNotBcastPpchargeCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 60),
    _VinesIfTxNotBcastPpchargeCnt_Type()
)
vinesIfTxNotBcastPpchargeCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfTxNotBcastPpchargeCnt.setStatus("mandatory")
_VinesIfTxBcastForwardedCnt_Type = Counter32
_VinesIfTxBcastForwardedCnt_Object = MibTableColumn
vinesIfTxBcastForwardedCnt = _VinesIfTxBcastForwardedCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 61),
    _VinesIfTxBcastForwardedCnt_Type()
)
vinesIfTxBcastForwardedCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfTxBcastForwardedCnt.setStatus("mandatory")
_VinesIfTxBcastHelperedCnt_Type = Counter32
_VinesIfTxBcastHelperedCnt_Object = MibTableColumn
vinesIfTxBcastHelperedCnt = _VinesIfTxBcastHelperedCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 62),
    _VinesIfTxBcastHelperedCnt_Type()
)
vinesIfTxBcastHelperedCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfTxBcastHelperedCnt.setStatus("mandatory")
_VinesIfTxArp0Cnt_Type = Counter32
_VinesIfTxArp0Cnt_Object = MibTableColumn
vinesIfTxArp0Cnt = _VinesIfTxArp0Cnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 63),
    _VinesIfTxArp0Cnt_Type()
)
vinesIfTxArp0Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfTxArp0Cnt.setStatus("mandatory")
_VinesIfTxArp1Cnt_Type = Counter32
_VinesIfTxArp1Cnt_Object = MibTableColumn
vinesIfTxArp1Cnt = _VinesIfTxArp1Cnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 64),
    _VinesIfTxArp1Cnt_Type()
)
vinesIfTxArp1Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfTxArp1Cnt.setStatus("mandatory")
_VinesIfTxArp2Cnt_Type = Counter32
_VinesIfTxArp2Cnt_Object = MibTableColumn
vinesIfTxArp2Cnt = _VinesIfTxArp2Cnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 65),
    _VinesIfTxArp2Cnt_Type()
)
vinesIfTxArp2Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfTxArp2Cnt.setStatus("mandatory")
_VinesIfTxArp3Cnt_Type = Counter32
_VinesIfTxArp3Cnt_Object = MibTableColumn
vinesIfTxArp3Cnt = _VinesIfTxArp3Cnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 66),
    _VinesIfTxArp3Cnt_Type()
)
vinesIfTxArp3Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfTxArp3Cnt.setStatus("mandatory")
_VinesIfTxIcpErrorCnt_Type = Counter32
_VinesIfTxIcpErrorCnt_Object = MibTableColumn
vinesIfTxIcpErrorCnt = _VinesIfTxIcpErrorCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 67),
    _VinesIfTxIcpErrorCnt_Type()
)
vinesIfTxIcpErrorCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfTxIcpErrorCnt.setStatus("mandatory")
_VinesIfTxIcpMetricCnt_Type = Counter32
_VinesIfTxIcpMetricCnt_Object = MibTableColumn
vinesIfTxIcpMetricCnt = _VinesIfTxIcpMetricCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 68),
    _VinesIfTxIcpMetricCnt_Type()
)
vinesIfTxIcpMetricCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfTxIcpMetricCnt.setStatus("mandatory")
_VinesIfTxIpcCnt_Type = Counter32
_VinesIfTxIpcCnt_Object = MibTableColumn
vinesIfTxIpcCnt = _VinesIfTxIpcCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 69),
    _VinesIfTxIpcCnt_Type()
)
vinesIfTxIpcCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfTxIpcCnt.setStatus("mandatory")
_VinesIfTxRtp0Cnt_Type = Counter32
_VinesIfTxRtp0Cnt_Object = MibTableColumn
vinesIfTxRtp0Cnt = _VinesIfTxRtp0Cnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 70),
    _VinesIfTxRtp0Cnt_Type()
)
vinesIfTxRtp0Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfTxRtp0Cnt.setStatus("mandatory")
_VinesIfTxRtp1Cnt_Type = Counter32
_VinesIfTxRtp1Cnt_Object = MibTableColumn
vinesIfTxRtp1Cnt = _VinesIfTxRtp1Cnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 71),
    _VinesIfTxRtp1Cnt_Type()
)
vinesIfTxRtp1Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfTxRtp1Cnt.setStatus("mandatory")
_VinesIfTxRtp2Cnt_Type = Counter32
_VinesIfTxRtp2Cnt_Object = MibTableColumn
vinesIfTxRtp2Cnt = _VinesIfTxRtp2Cnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 72),
    _VinesIfTxRtp2Cnt_Type()
)
vinesIfTxRtp2Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfTxRtp2Cnt.setStatus("mandatory")
_VinesIfTxRtp3Cnt_Type = Counter32
_VinesIfTxRtp3Cnt_Object = MibTableColumn
vinesIfTxRtp3Cnt = _VinesIfTxRtp3Cnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 73),
    _VinesIfTxRtp3Cnt_Type()
)
vinesIfTxRtp3Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfTxRtp3Cnt.setStatus("mandatory")
_VinesIfTxRtp4Cnt_Type = Counter32
_VinesIfTxRtp4Cnt_Object = MibTableColumn
vinesIfTxRtp4Cnt = _VinesIfTxRtp4Cnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 74),
    _VinesIfTxRtp4Cnt_Type()
)
vinesIfTxRtp4Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfTxRtp4Cnt.setStatus("mandatory")
_VinesIfTxRtp5Cnt_Type = Counter32
_VinesIfTxRtp5Cnt_Object = MibTableColumn
vinesIfTxRtp5Cnt = _VinesIfTxRtp5Cnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 75),
    _VinesIfTxRtp5Cnt_Type()
)
vinesIfTxRtp5Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfTxRtp5Cnt.setStatus("mandatory")
_VinesIfTxRtp6Cnt_Type = Counter32
_VinesIfTxRtp6Cnt_Object = MibTableColumn
vinesIfTxRtp6Cnt = _VinesIfTxRtp6Cnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 76),
    _VinesIfTxRtp6Cnt_Type()
)
vinesIfTxRtp6Cnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfTxRtp6Cnt.setStatus("mandatory")
_VinesIfTxSppCnt_Type = Counter32
_VinesIfTxSppCnt_Object = MibTableColumn
vinesIfTxSppCnt = _VinesIfTxSppCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 77),
    _VinesIfTxSppCnt_Type()
)
vinesIfTxSppCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfTxSppCnt.setStatus("mandatory")
_VinesIfTxEchoCnt_Type = Counter32
_VinesIfTxEchoCnt_Object = MibTableColumn
vinesIfTxEchoCnt = _VinesIfTxEchoCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 78),
    _VinesIfTxEchoCnt_Type()
)
vinesIfTxEchoCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfTxEchoCnt.setStatus("mandatory")
_VinesIfTxMacEchoCnt_Type = Counter32
_VinesIfTxMacEchoCnt_Object = MibTableColumn
vinesIfTxMacEchoCnt = _VinesIfTxMacEchoCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 79),
    _VinesIfTxMacEchoCnt_Type()
)
vinesIfTxMacEchoCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfTxMacEchoCnt.setStatus("mandatory")
_VinesIfTxProxyCnt_Type = Counter32
_VinesIfTxProxyCnt_Object = MibTableColumn
vinesIfTxProxyCnt = _VinesIfTxProxyCnt_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 80),
    _VinesIfTxProxyCnt_Type()
)
vinesIfTxProxyCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfTxProxyCnt.setStatus("mandatory")
_VinesIfInputRouterFilter_Type = Integer32
_VinesIfInputRouterFilter_Object = MibTableColumn
vinesIfInputRouterFilter = _VinesIfInputRouterFilter_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 81),
    _VinesIfInputRouterFilter_Type()
)
vinesIfInputRouterFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfInputRouterFilter.setStatus("mandatory")
_VinesIfInputNetworkFilter_Type = Integer32
_VinesIfInputNetworkFilter_Object = MibTableColumn
vinesIfInputNetworkFilter = _VinesIfInputNetworkFilter_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 82),
    _VinesIfInputNetworkFilter_Type()
)
vinesIfInputNetworkFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfInputNetworkFilter.setStatus("mandatory")
_VinesIfOutputNetworkFilter_Type = Integer32
_VinesIfOutputNetworkFilter_Object = MibTableColumn
vinesIfOutputNetworkFilter = _VinesIfOutputNetworkFilter_Object(
    (1, 3, 6, 1, 4, 1, 9, 3, 5, 29, 1, 83),
    _VinesIfOutputNetworkFilter_Type()
)
vinesIfOutputNetworkFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vinesIfOutputNetworkFilter.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OLD-CISCO-VINES-MIB",
    **{"tmpvines": tmpvines,
       "vinesInput": vinesInput,
       "vinesOutput": vinesOutput,
       "vinesLocaldest": vinesLocaldest,
       "vinesForwarded": vinesForwarded,
       "vinesBcastin": vinesBcastin,
       "vinesBcastout": vinesBcastout,
       "vinesBcastfwd": vinesBcastfwd,
       "vinesNotlan": vinesNotlan,
       "vinesNotgt4800": vinesNotgt4800,
       "vinesNocharges": vinesNocharges,
       "vinesFormaterror": vinesFormaterror,
       "vinesCksumerr": vinesCksumerr,
       "vinesHopcount": vinesHopcount,
       "vinesNoroute": vinesNoroute,
       "vinesEncapsfailed": vinesEncapsfailed,
       "vinesUnknown": vinesUnknown,
       "vinesIcpIn": vinesIcpIn,
       "vinesIcpOut": vinesIcpOut,
       "vinesMetricOut": vinesMetricOut,
       "vinesMacEchoIn": vinesMacEchoIn,
       "vinesMacEchoOut": vinesMacEchoOut,
       "vinesEchoIn": vinesEchoIn,
       "vinesEchoOut": vinesEchoOut,
       "vinesProxyCnt": vinesProxyCnt,
       "vinesProxyReplyCnt": vinesProxyReplyCnt,
       "vinesNet": vinesNet,
       "vinesSubNet": vinesSubNet,
       "vinesClient": vinesClient,
       "vinesIfTable": vinesIfTable,
       "vinesIfTableEntry": vinesIfTableEntry,
       "vinesIfMetric": vinesIfMetric,
       "vinesIfEnctype": vinesIfEnctype,
       "vinesIfAccesslist": vinesIfAccesslist,
       "vinesIfPropagate": vinesIfPropagate,
       "vinesIfArpEnabled": vinesIfArpEnabled,
       "vinesIfServerless": vinesIfServerless,
       "vinesIfRedirectInterval": vinesIfRedirectInterval,
       "vinesIfSplitDisabled": vinesIfSplitDisabled,
       "vinesIfLineup": vinesIfLineup,
       "vinesIfFastokay": vinesIfFastokay,
       "vinesIfRouteCache": vinesIfRouteCache,
       "vinesIfRxNotEnabledCnt": vinesIfRxNotEnabledCnt,
       "vinesIfRxFormatErrorCnt": vinesIfRxFormatErrorCnt,
       "vinesIfRxLocalDestCnt": vinesIfRxLocalDestCnt,
       "vinesIfRxBcastinCnt": vinesIfRxBcastinCnt,
       "vinesIfRxForwardedCnt": vinesIfRxForwardedCnt,
       "vinesIfRxNoRouteCnt": vinesIfRxNoRouteCnt,
       "vinesIfRxZeroHopCountCnt": vinesIfRxZeroHopCountCnt,
       "vinesIfRxChecksumErrorCnt": vinesIfRxChecksumErrorCnt,
       "vinesIfRxArp0Cnt": vinesIfRxArp0Cnt,
       "vinesIfRxArp1Cnt": vinesIfRxArp1Cnt,
       "vinesIfRxArp2Cnt": vinesIfRxArp2Cnt,
       "vinesIfRxArp3Cnt": vinesIfRxArp3Cnt,
       "vinesIfRxArpIllegalCnt": vinesIfRxArpIllegalCnt,
       "vinesIfRxIcpErrorCnt": vinesIfRxIcpErrorCnt,
       "vinesIfRxIcpMetricCnt": vinesIfRxIcpMetricCnt,
       "vinesIfRxIcpIllegalCnt": vinesIfRxIcpIllegalCnt,
       "vinesIfRxIpcCnt": vinesIfRxIpcCnt,
       "vinesIfRxRtp0Cnt": vinesIfRxRtp0Cnt,
       "vinesIfRxRtp1Cnt": vinesIfRxRtp1Cnt,
       "vinesIfRxRtp2Cnt": vinesIfRxRtp2Cnt,
       "vinesIfRxRtp3Cnt": vinesIfRxRtp3Cnt,
       "vinesIfRxRtp4Cnt": vinesIfRxRtp4Cnt,
       "vinesIfRxRtp5Cnt": vinesIfRxRtp5Cnt,
       "vinesIfRxRtp6Cnt": vinesIfRxRtp6Cnt,
       "vinesIfRxRtpIllegalCnt": vinesIfRxRtpIllegalCnt,
       "vinesIfRxSppCnt": vinesIfRxSppCnt,
       "vinesIfRxIpUnknownCnt": vinesIfRxIpUnknownCnt,
       "vinesIfRxIpcUnknownCnt": vinesIfRxIpcUnknownCnt,
       "vinesIfRxBcastHelperedCnt": vinesIfRxBcastHelperedCnt,
       "vinesIfRxBcastForwardedCnt": vinesIfRxBcastForwardedCnt,
       "vinesIfRxBcastDuplicateCnt": vinesIfRxBcastDuplicateCnt,
       "vinesIfRxEchoCnt": vinesIfRxEchoCnt,
       "vinesIfRxMacEchoCnt": vinesIfRxMacEchoCnt,
       "vinesIfRxProxyReplyCnt": vinesIfRxProxyReplyCnt,
       "vinesIfTxUnicastCnt": vinesIfTxUnicastCnt,
       "vinesIfTxBcastCnt": vinesIfTxBcastCnt,
       "vinesIfTxForwardedCnt": vinesIfTxForwardedCnt,
       "vinesIfTxFailedEncapsCnt": vinesIfTxFailedEncapsCnt,
       "vinesIfTxFailedAccessCnt": vinesIfTxFailedAccessCnt,
       "vinesIfTxFailedDownCnt": vinesIfTxFailedDownCnt,
       "vinesIfTxNotBcastToSourceCnt": vinesIfTxNotBcastToSourceCnt,
       "vinesIfTxNotBcastNotlanCnt": vinesIfTxNotBcastNotlanCnt,
       "vinesIfTxNotBcastNotgt4800Cnt": vinesIfTxNotBcastNotgt4800Cnt,
       "vinesIfTxNotBcastPpchargeCnt": vinesIfTxNotBcastPpchargeCnt,
       "vinesIfTxBcastForwardedCnt": vinesIfTxBcastForwardedCnt,
       "vinesIfTxBcastHelperedCnt": vinesIfTxBcastHelperedCnt,
       "vinesIfTxArp0Cnt": vinesIfTxArp0Cnt,
       "vinesIfTxArp1Cnt": vinesIfTxArp1Cnt,
       "vinesIfTxArp2Cnt": vinesIfTxArp2Cnt,
       "vinesIfTxArp3Cnt": vinesIfTxArp3Cnt,
       "vinesIfTxIcpErrorCnt": vinesIfTxIcpErrorCnt,
       "vinesIfTxIcpMetricCnt": vinesIfTxIcpMetricCnt,
       "vinesIfTxIpcCnt": vinesIfTxIpcCnt,
       "vinesIfTxRtp0Cnt": vinesIfTxRtp0Cnt,
       "vinesIfTxRtp1Cnt": vinesIfTxRtp1Cnt,
       "vinesIfTxRtp2Cnt": vinesIfTxRtp2Cnt,
       "vinesIfTxRtp3Cnt": vinesIfTxRtp3Cnt,
       "vinesIfTxRtp4Cnt": vinesIfTxRtp4Cnt,
       "vinesIfTxRtp5Cnt": vinesIfTxRtp5Cnt,
       "vinesIfTxRtp6Cnt": vinesIfTxRtp6Cnt,
       "vinesIfTxSppCnt": vinesIfTxSppCnt,
       "vinesIfTxEchoCnt": vinesIfTxEchoCnt,
       "vinesIfTxMacEchoCnt": vinesIfTxMacEchoCnt,
       "vinesIfTxProxyCnt": vinesIfTxProxyCnt,
       "vinesIfInputRouterFilter": vinesIfInputRouterFilter,
       "vinesIfInputNetworkFilter": vinesIfInputNetworkFilter,
       "vinesIfOutputNetworkFilter": vinesIfOutputNetworkFilter}
)
