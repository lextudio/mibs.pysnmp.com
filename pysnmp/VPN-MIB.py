# SNMP MIB module (VPN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VPN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:13:14 2024
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
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso,
 mgmt) = mibBuilder.importSymbols(
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso",
    "mgmt")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Vpnet_ObjectIdentity = ObjectIdentity
vpnet = _Vpnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1866)
)
_Vpnmib_ObjectIdentity = ObjectIdentity
vpnmib = _Vpnmib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1866, 7)
)
_Waninterface_ObjectIdentity = ObjectIdentity
waninterface = _Waninterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1866, 7, 1)
)
_WanIfTable_Object = MibTable
wanIfTable = _WanIfTable_Object(
    (1, 3, 6, 1, 4, 1, 1866, 7, 1, 1)
)
if mibBuilder.loadTexts:
    wanIfTable.setStatus("mandatory")
_WanIfEntry_Object = MibTableRow
wanIfEntry = _WanIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 1866, 7, 1, 1, 1)
)
wanIfEntry.setIndexNames(
    (0, "VPN-MIB", "wanIfIndex"),
)
if mibBuilder.loadTexts:
    wanIfEntry.setStatus("mandatory")
_WanIfIndex_Type = Integer32
_WanIfIndex_Object = MibTableColumn
wanIfIndex = _WanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1866, 7, 1, 1, 1, 1),
    _WanIfIndex_Type()
)
wanIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanIfIndex.setStatus("mandatory")
_WanIfFramesRcvd_Type = Integer32
_WanIfFramesRcvd_Object = MibTableColumn
wanIfFramesRcvd = _WanIfFramesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 1866, 7, 1, 1, 1, 2),
    _WanIfFramesRcvd_Type()
)
wanIfFramesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanIfFramesRcvd.setStatus("mandatory")
_WanIfFramesXmit_Type = Integer32
_WanIfFramesXmit_Object = MibTableColumn
wanIfFramesXmit = _WanIfFramesXmit_Object(
    (1, 3, 6, 1, 4, 1, 1866, 7, 1, 1, 1, 3),
    _WanIfFramesXmit_Type()
)
wanIfFramesXmit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanIfFramesXmit.setStatus("mandatory")
_WanIfFramesDisc_Type = Integer32
_WanIfFramesDisc_Object = MibTableColumn
wanIfFramesDisc = _WanIfFramesDisc_Object(
    (1, 3, 6, 1, 4, 1, 1866, 7, 1, 1, 1, 4),
    _WanIfFramesDisc_Type()
)
wanIfFramesDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanIfFramesDisc.setStatus("mandatory")
_WanIfRcvOvrn_Type = Integer32
_WanIfRcvOvrn_Object = MibTableColumn
wanIfRcvOvrn = _WanIfRcvOvrn_Object(
    (1, 3, 6, 1, 4, 1, 1866, 7, 1, 1, 1, 5),
    _WanIfRcvOvrn_Type()
)
wanIfRcvOvrn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanIfRcvOvrn.setStatus("mandatory")
_WanIfRcvAbort_Type = Integer32
_WanIfRcvAbort_Object = MibTableColumn
wanIfRcvAbort = _WanIfRcvAbort_Object(
    (1, 3, 6, 1, 4, 1, 1866, 7, 1, 1, 1, 6),
    _WanIfRcvAbort_Type()
)
wanIfRcvAbort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanIfRcvAbort.setStatus("mandatory")
_WanIfRcvAlignErr_Type = Integer32
_WanIfRcvAlignErr_Object = MibTableColumn
wanIfRcvAlignErr = _WanIfRcvAlignErr_Object(
    (1, 3, 6, 1, 4, 1, 1866, 7, 1, 1, 1, 7),
    _WanIfRcvAlignErr_Type()
)
wanIfRcvAlignErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanIfRcvAlignErr.setStatus("mandatory")
_WanIfRcvCRCErr_Type = Integer32
_WanIfRcvCRCErr_Object = MibScalar
wanIfRcvCRCErr = _WanIfRcvCRCErr_Object(
    (1, 3, 6, 1, 4, 1, 1866, 7, 1, 1, 1, 8),
    _WanIfRcvCRCErr_Type()
)
wanIfRcvCRCErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanIfRcvCRCErr.setStatus("mandatory")
_WanIfRcvFrameLong_Type = Integer32
_WanIfRcvFrameLong_Object = MibTableColumn
wanIfRcvFrameLong = _WanIfRcvFrameLong_Object(
    (1, 3, 6, 1, 4, 1, 1866, 7, 1, 1, 1, 9),
    _WanIfRcvFrameLong_Type()
)
wanIfRcvFrameLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanIfRcvFrameLong.setStatus("mandatory")
_WanIfRcvNoBuff_Type = Integer32
_WanIfRcvNoBuff_Object = MibScalar
wanIfRcvNoBuff = _WanIfRcvNoBuff_Object(
    (1, 3, 6, 1, 4, 1, 1866, 7, 1, 1, 1, 10),
    _WanIfRcvNoBuff_Type()
)
wanIfRcvNoBuff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanIfRcvNoBuff.setStatus("mandatory")
_WanIfXmitUnderrun_Type = Integer32
_WanIfXmitUnderrun_Object = MibTableColumn
wanIfXmitUnderrun = _WanIfXmitUnderrun_Object(
    (1, 3, 6, 1, 4, 1, 1866, 7, 1, 1, 1, 11),
    _WanIfXmitUnderrun_Type()
)
wanIfXmitUnderrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanIfXmitUnderrun.setStatus("mandatory")
_WanIfXmitTimeout_Type = Integer32
_WanIfXmitTimeout_Object = MibTableColumn
wanIfXmitTimeout = _WanIfXmitTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1866, 7, 1, 1, 1, 12),
    _WanIfXmitTimeout_Type()
)
wanIfXmitTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanIfXmitTimeout.setStatus("mandatory")
_WanIfXmitNoBuff_Type = Integer32
_WanIfXmitNoBuff_Object = MibTableColumn
wanIfXmitNoBuff = _WanIfXmitNoBuff_Object(
    (1, 3, 6, 1, 4, 1, 1866, 7, 1, 1, 1, 13),
    _WanIfXmitNoBuff_Type()
)
wanIfXmitNoBuff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanIfXmitNoBuff.setStatus("mandatory")
_WanIfRcvByteRate_Type = Counter32
_WanIfRcvByteRate_Object = MibTableColumn
wanIfRcvByteRate = _WanIfRcvByteRate_Object(
    (1, 3, 6, 1, 4, 1, 1866, 7, 1, 1, 1, 14),
    _WanIfRcvByteRate_Type()
)
wanIfRcvByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanIfRcvByteRate.setStatus("mandatory")
_WanIfXmitByteRate_Type = Counter32
_WanIfXmitByteRate_Object = MibTableColumn
wanIfXmitByteRate = _WanIfXmitByteRate_Object(
    (1, 3, 6, 1, 4, 1, 1866, 7, 1, 1, 1, 15),
    _WanIfXmitByteRate_Type()
)
wanIfXmitByteRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanIfXmitByteRate.setStatus("mandatory")
_Vpns_ObjectIdentity = ObjectIdentity
vpns = _Vpns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1866, 7, 2)
)
_VpnTable_Object = MibTable
vpnTable = _VpnTable_Object(
    (1, 3, 6, 1, 4, 1, 1866, 7, 2, 1)
)
if mibBuilder.loadTexts:
    vpnTable.setStatus("mandatory")
_VpnEntry_Object = MibTableRow
vpnEntry = _VpnEntry_Object(
    (1, 3, 6, 1, 4, 1, 1866, 7, 2, 1, 1)
)
vpnEntry.setIndexNames(
    (0, "VPN-MIB", "vpnIndex"),
)
if mibBuilder.loadTexts:
    vpnEntry.setStatus("mandatory")
_VpnIndex_Type = Integer32
_VpnIndex_Object = MibTableColumn
vpnIndex = _VpnIndex_Object(
    (1, 3, 6, 1, 4, 1, 1866, 7, 2, 1, 1, 1),
    _VpnIndex_Type()
)
vpnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnIndex.setStatus("mandatory")
_VpnDescr_Type = DisplayString
_VpnDescr_Object = MibTableColumn
vpnDescr = _VpnDescr_Object(
    (1, 3, 6, 1, 4, 1, 1866, 7, 2, 1, 1, 2),
    _VpnDescr_Type()
)
vpnDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnDescr.setStatus("mandatory")
_VpnSkipInPktDecap_Type = Integer32
_VpnSkipInPktDecap_Object = MibTableColumn
vpnSkipInPktDecap = _VpnSkipInPktDecap_Object(
    (1, 3, 6, 1, 4, 1, 1866, 7, 2, 1, 1, 3),
    _VpnSkipInPktDecap_Type()
)
vpnSkipInPktDecap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnSkipInPktDecap.setStatus("mandatory")
_VpnSkipOutPktEncap_Type = Integer32
_VpnSkipOutPktEncap_Object = MibTableColumn
vpnSkipOutPktEncap = _VpnSkipOutPktEncap_Object(
    (1, 3, 6, 1, 4, 1, 1866, 7, 2, 1, 1, 4),
    _VpnSkipOutPktEncap_Type()
)
vpnSkipOutPktEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnSkipOutPktEncap.setStatus("mandatory")
_VpnSkipInPktParseErr_Type = Integer32
_VpnSkipInPktParseErr_Object = MibTableColumn
vpnSkipInPktParseErr = _VpnSkipInPktParseErr_Object(
    (1, 3, 6, 1, 4, 1, 1866, 7, 2, 1, 1, 5),
    _VpnSkipInPktParseErr_Type()
)
vpnSkipInPktParseErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnSkipInPktParseErr.setStatus("mandatory")
_VpnSkipInKPUpdt_Type = Integer32
_VpnSkipInKPUpdt_Object = MibTableColumn
vpnSkipInKPUpdt = _VpnSkipInKPUpdt_Object(
    (1, 3, 6, 1, 4, 1, 1866, 7, 2, 1, 1, 6),
    _VpnSkipInKPUpdt_Type()
)
vpnSkipInKPUpdt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnSkipInKPUpdt.setStatus("mandatory")
_VpnSkipOutKPUpdt_Type = Integer32
_VpnSkipOutKPUpdt_Object = MibTableColumn
vpnSkipOutKPUpdt = _VpnSkipOutKPUpdt_Object(
    (1, 3, 6, 1, 4, 1, 1866, 7, 2, 1, 1, 7),
    _VpnSkipOutKPUpdt_Type()
)
vpnSkipOutKPUpdt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnSkipOutKPUpdt.setStatus("mandatory")
_VpnOutFrag_Type = Integer32
_VpnOutFrag_Object = MibTableColumn
vpnOutFrag = _VpnOutFrag_Object(
    (1, 3, 6, 1, 4, 1, 1866, 7, 2, 1, 1, 8),
    _VpnOutFrag_Type()
)
vpnOutFrag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnOutFrag.setStatus("mandatory")
_VpnOctetsIn_Type = Integer32
_VpnOctetsIn_Object = MibTableColumn
vpnOctetsIn = _VpnOctetsIn_Object(
    (1, 3, 6, 1, 4, 1, 1866, 7, 2, 1, 1, 9),
    _VpnOctetsIn_Type()
)
vpnOctetsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnOctetsIn.setStatus("mandatory")
_VpnOctetsOut_Type = Integer32
_VpnOctetsOut_Object = MibTableColumn
vpnOctetsOut = _VpnOctetsOut_Object(
    (1, 3, 6, 1, 4, 1, 1866, 7, 2, 1, 1, 10),
    _VpnOctetsOut_Type()
)
vpnOctetsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnOctetsOut.setStatus("mandatory")
_VpnNOutOfOrder_Type = Integer32
_VpnNOutOfOrder_Object = MibTableColumn
vpnNOutOfOrder = _VpnNOutOfOrder_Object(
    (1, 3, 6, 1, 4, 1, 1866, 7, 2, 1, 1, 11),
    _VpnNOutOfOrder_Type()
)
vpnNOutOfOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnNOutOfOrder.setStatus("mandatory")
_VpnSkipAlgMismatch_Type = Integer32
_VpnSkipAlgMismatch_Object = MibTableColumn
vpnSkipAlgMismatch = _VpnSkipAlgMismatch_Object(
    (1, 3, 6, 1, 4, 1, 1866, 7, 2, 1, 1, 12),
    _VpnSkipAlgMismatch_Type()
)
vpnSkipAlgMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnSkipAlgMismatch.setStatus("mandatory")
_VpnAuthInPktInvdSig_Type = Integer32
_VpnAuthInPktInvdSig_Object = MibTableColumn
vpnAuthInPktInvdSig = _VpnAuthInPktInvdSig_Object(
    (1, 3, 6, 1, 4, 1, 1866, 7, 2, 1, 1, 13),
    _VpnAuthInPktInvdSig_Type()
)
vpnAuthInPktInvdSig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnAuthInPktInvdSig.setStatus("mandatory")
_VpnAuthInPktParseErr_Type = Integer32
_VpnAuthInPktParseErr_Object = MibTableColumn
vpnAuthInPktParseErr = _VpnAuthInPktParseErr_Object(
    (1, 3, 6, 1, 4, 1, 1866, 7, 2, 1, 1, 14),
    _VpnAuthInPktParseErr_Type()
)
vpnAuthInPktParseErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnAuthInPktParseErr.setStatus("mandatory")
_VpnEncryptImpEncap_Type = Integer32
_VpnEncryptImpEncap_Object = MibTableColumn
vpnEncryptImpEncap = _VpnEncryptImpEncap_Object(
    (1, 3, 6, 1, 4, 1, 1866, 7, 2, 1, 1, 15),
    _VpnEncryptImpEncap_Type()
)
vpnEncryptImpEncap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnEncryptImpEncap.setStatus("mandatory")
_VpnEncryptInPktParseErr_Type = Integer32
_VpnEncryptInPktParseErr_Object = MibTableColumn
vpnEncryptInPktParseErr = _VpnEncryptInPktParseErr_Object(
    (1, 3, 6, 1, 4, 1, 1866, 7, 2, 1, 1, 16),
    _VpnEncryptInPktParseErr_Type()
)
vpnEncryptInPktParseErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnEncryptInPktParseErr.setStatus("mandatory")
_Log_ObjectIdentity = ObjectIdentity
log = _Log_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1866, 7, 3)
)
_LogTable_Object = MibTable
logTable = _LogTable_Object(
    (1, 3, 6, 1, 4, 1, 1866, 7, 3, 1)
)
if mibBuilder.loadTexts:
    logTable.setStatus("mandatory")
_LogEntry_Object = MibTableRow
logEntry = _LogEntry_Object(
    (1, 3, 6, 1, 4, 1, 1866, 7, 3, 1, 1)
)
logEntry.setIndexNames(
    (0, "VPN-MIB", "logIndex"),
)
if mibBuilder.loadTexts:
    logEntry.setStatus("mandatory")
_LogIndex_Type = Integer32
_LogIndex_Object = MibTableColumn
logIndex = _LogIndex_Object(
    (1, 3, 6, 1, 4, 1, 1866, 7, 3, 1, 1, 1),
    _LogIndex_Type()
)
logIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logIndex.setStatus("mandatory")
_LogTime_Type = Integer32
_LogTime_Object = MibTableColumn
logTime = _LogTime_Object(
    (1, 3, 6, 1, 4, 1, 1866, 7, 3, 1, 1, 2),
    _LogTime_Type()
)
logTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logTime.setStatus("mandatory")
_LogAttackType_Type = Integer32
_LogAttackType_Object = MibTableColumn
logAttackType = _LogAttackType_Object(
    (1, 3, 6, 1, 4, 1, 1866, 7, 3, 1, 1, 3),
    _LogAttackType_Type()
)
logAttackType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logAttackType.setStatus("mandatory")


class _LogDescription_Type(DisplayString):
    """Custom type logDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 65),
    )


_LogDescription_Type.__name__ = "DisplayString"
_LogDescription_Object = MibTableColumn
logDescription = _LogDescription_Object(
    (1, 3, 6, 1, 4, 1, 1866, 7, 3, 1, 1, 4),
    _LogDescription_Type()
)
logDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logDescription.setStatus("mandatory")
_VsuSystem_ObjectIdentity = ObjectIdentity
vsuSystem = _VsuSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1866, 7, 4)
)
_CpuUtilization_Type = Counter32
_CpuUtilization_Object = MibScalar
cpuUtilization = _CpuUtilization_Object(
    (1, 3, 6, 1, 4, 1, 1866, 7, 4, 1),
    _CpuUtilization_Type()
)
cpuUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuUtilization.setStatus("mandatory")
_ActiveSessions_ObjectIdentity = ObjectIdentity
activeSessions = _ActiveSessions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1866, 7, 5)
)
_ActiveSessionTable_Object = MibTable
activeSessionTable = _ActiveSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 1866, 7, 5, 1)
)
if mibBuilder.loadTexts:
    activeSessionTable.setStatus("mandatory")
_ActiveSessionEntry_Object = MibTableRow
activeSessionEntry = _ActiveSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 1866, 7, 5, 1, 1)
)
activeSessionEntry.setIndexNames(
    (0, "VPN-MIB", "asName"),
)
if mibBuilder.loadTexts:
    activeSessionEntry.setStatus("mandatory")
_AsName_Type = DisplayString
_AsName_Object = MibTableColumn
asName = _AsName_Object(
    (1, 3, 6, 1, 4, 1, 1866, 7, 5, 1, 1, 1),
    _AsName_Type()
)
asName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asName.setStatus("mandatory")
_AsLength_Type = TimeTicks
_AsLength_Object = MibTableColumn
asLength = _AsLength_Object(
    (1, 3, 6, 1, 4, 1, 1866, 7, 5, 1, 1, 2),
    _AsLength_Type()
)
asLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asLength.setStatus("mandatory")
_AsOrgIPAddress_Type = IpAddress
_AsOrgIPAddress_Object = MibTableColumn
asOrgIPAddress = _AsOrgIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 1866, 7, 5, 1, 1, 3),
    _AsOrgIPAddress_Type()
)
asOrgIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asOrgIPAddress.setStatus("mandatory")
_AsXlateIPAddress_Type = IpAddress
_AsXlateIPAddress_Object = MibScalar
asXlateIPAddress = _AsXlateIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 1866, 7, 5, 1, 1, 4),
    _AsXlateIPAddress_Type()
)
asXlateIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asXlateIPAddress.setStatus("mandatory")
_AsDescr_Type = DisplayString
_AsDescr_Object = MibTableColumn
asDescr = _AsDescr_Object(
    (1, 3, 6, 1, 4, 1, 1866, 7, 5, 1, 1, 5),
    _AsDescr_Type()
)
asDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asDescr.setStatus("mandatory")
_AsPktsIn_Type = Counter32
_AsPktsIn_Object = MibTableColumn
asPktsIn = _AsPktsIn_Object(
    (1, 3, 6, 1, 4, 1, 1866, 7, 5, 1, 1, 6),
    _AsPktsIn_Type()
)
asPktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asPktsIn.setStatus("mandatory")
_AsPktsOut_Type = Counter32
_AsPktsOut_Object = MibTableColumn
asPktsOut = _AsPktsOut_Object(
    (1, 3, 6, 1, 4, 1, 1866, 7, 5, 1, 1, 7),
    _AsPktsOut_Type()
)
asPktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asPktsOut.setStatus("mandatory")
_AsBytesIn_Type = Counter32
_AsBytesIn_Object = MibTableColumn
asBytesIn = _AsBytesIn_Object(
    (1, 3, 6, 1, 4, 1, 1866, 7, 5, 1, 1, 8),
    _AsBytesIn_Type()
)
asBytesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asBytesIn.setStatus("mandatory")
_AsBytesOut_Type = Counter32
_AsBytesOut_Object = MibTableColumn
asBytesOut = _AsBytesOut_Object(
    (1, 3, 6, 1, 4, 1, 1866, 7, 5, 1, 1, 9),
    _AsBytesOut_Type()
)
asBytesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asBytesOut.setStatus("mandatory")

# Managed Objects groups


# Notification objects

skipHdrErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 1866, 0, 1)
)
if mibBuilder.loadTexts:
    skipHdrErr.setStatus(
        ""
    )

skipNCounterErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 1866, 0, 2)
)
if mibBuilder.loadTexts:
    skipNCounterErr.setStatus(
        ""
    )

skipAlgMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 1866, 0, 3)
)
if mibBuilder.loadTexts:
    skipAlgMismatch.setStatus(
        ""
    )

authFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1866, 0, 4)
)
if mibBuilder.loadTexts:
    authFailure.setStatus(
        ""
    )

authHdrErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 1866, 0, 5)
)
if mibBuilder.loadTexts:
    authHdrErr.setStatus(
        ""
    )

encryptHdrErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 1866, 0, 6)
)
if mibBuilder.loadTexts:
    encryptHdrErr.setStatus(
        ""
    )

authFailureLimitErr = NotificationType(
    (1, 3, 6, 1, 4, 1, 1866, 0, 7)
)
if mibBuilder.loadTexts:
    authFailureLimitErr.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VPN-MIB",
    **{"vpnet": vpnet,
       "skipHdrErr": skipHdrErr,
       "skipNCounterErr": skipNCounterErr,
       "skipAlgMismatch": skipAlgMismatch,
       "authFailure": authFailure,
       "authHdrErr": authHdrErr,
       "encryptHdrErr": encryptHdrErr,
       "authFailureLimitErr": authFailureLimitErr,
       "vpnmib": vpnmib,
       "waninterface": waninterface,
       "wanIfTable": wanIfTable,
       "wanIfEntry": wanIfEntry,
       "wanIfIndex": wanIfIndex,
       "wanIfFramesRcvd": wanIfFramesRcvd,
       "wanIfFramesXmit": wanIfFramesXmit,
       "wanIfFramesDisc": wanIfFramesDisc,
       "wanIfRcvOvrn": wanIfRcvOvrn,
       "wanIfRcvAbort": wanIfRcvAbort,
       "wanIfRcvAlignErr": wanIfRcvAlignErr,
       "wanIfRcvCRCErr": wanIfRcvCRCErr,
       "wanIfRcvFrameLong": wanIfRcvFrameLong,
       "wanIfRcvNoBuff": wanIfRcvNoBuff,
       "wanIfXmitUnderrun": wanIfXmitUnderrun,
       "wanIfXmitTimeout": wanIfXmitTimeout,
       "wanIfXmitNoBuff": wanIfXmitNoBuff,
       "wanIfRcvByteRate": wanIfRcvByteRate,
       "wanIfXmitByteRate": wanIfXmitByteRate,
       "vpns": vpns,
       "vpnTable": vpnTable,
       "vpnEntry": vpnEntry,
       "vpnIndex": vpnIndex,
       "vpnDescr": vpnDescr,
       "vpnSkipInPktDecap": vpnSkipInPktDecap,
       "vpnSkipOutPktEncap": vpnSkipOutPktEncap,
       "vpnSkipInPktParseErr": vpnSkipInPktParseErr,
       "vpnSkipInKPUpdt": vpnSkipInKPUpdt,
       "vpnSkipOutKPUpdt": vpnSkipOutKPUpdt,
       "vpnOutFrag": vpnOutFrag,
       "vpnOctetsIn": vpnOctetsIn,
       "vpnOctetsOut": vpnOctetsOut,
       "vpnNOutOfOrder": vpnNOutOfOrder,
       "vpnSkipAlgMismatch": vpnSkipAlgMismatch,
       "vpnAuthInPktInvdSig": vpnAuthInPktInvdSig,
       "vpnAuthInPktParseErr": vpnAuthInPktParseErr,
       "vpnEncryptImpEncap": vpnEncryptImpEncap,
       "vpnEncryptInPktParseErr": vpnEncryptInPktParseErr,
       "log": log,
       "logTable": logTable,
       "logEntry": logEntry,
       "logIndex": logIndex,
       "logTime": logTime,
       "logAttackType": logAttackType,
       "logDescription": logDescription,
       "vsuSystem": vsuSystem,
       "cpuUtilization": cpuUtilization,
       "activeSessions": activeSessions,
       "activeSessionTable": activeSessionTable,
       "activeSessionEntry": activeSessionEntry,
       "asName": asName,
       "asLength": asLength,
       "asOrgIPAddress": asOrgIPAddress,
       "asXlateIPAddress": asXlateIPAddress,
       "asDescr": asDescr,
       "asPktsIn": asPktsIn,
       "asPktsOut": asPktsOut,
       "asBytesIn": asBytesIn,
       "asBytesOut": asBytesOut}
)
