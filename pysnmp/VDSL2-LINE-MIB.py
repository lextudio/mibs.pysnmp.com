# SNMP MIB module (VDSL2-LINE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VDSL2-LINE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:11:52 2024
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

(HCPerfIntervalThreshold,
 HCPerfTimeElapsed) = mibBuilder.importSymbols(
    "HC-PerfHist-TC-MIB",
    "HCPerfIntervalThreshold",
    "HCPerfTimeElapsed")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 transmission) = mibBuilder.importSymbols(
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
    "transmission")

(DisplayString,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(Xdsl2Band,
 Xdsl2BandUs,
 Xdsl2BitsAlloc,
 Xdsl2BpscResult,
 Xdsl2CarMask,
 Xdsl2ChAtmStatus,
 Xdsl2ChInitPolicy,
 Xdsl2ChInpReport,
 Xdsl2ChPtmStatus,
 Xdsl2ConfPmsForce,
 Xdsl2Direction,
 Xdsl2InitResult,
 Xdsl2LastTransmittedState,
 Xdsl2LdsfResult,
 Xdsl2LineBpsc,
 Xdsl2LineCeFlag,
 Xdsl2LineClassMask,
 Xdsl2LineLdsf,
 Xdsl2LineLimitMask,
 Xdsl2LinePmMode,
 Xdsl2LineProfiles,
 Xdsl2LinePsdMaskSelectUs,
 Xdsl2LineReset,
 Xdsl2LineSnrMode,
 Xdsl2LineStatus,
 Xdsl2LineTxRefVnDs,
 Xdsl2LineTxRefVnUs,
 Xdsl2LineUs0Disable,
 Xdsl2LineUs0Mask,
 Xdsl2MaxBer,
 Xdsl2MrefPsdDs,
 Xdsl2MrefPsdUs,
 Xdsl2OperationModes,
 Xdsl2PowerMngState,
 Xdsl2PsdMaskDs,
 Xdsl2PsdMaskUs,
 Xdsl2RaMode,
 Xdsl2RfiBands,
 Xdsl2ScMaskDs,
 Xdsl2ScMaskUs,
 Xdsl2SymbolProtection,
 Xdsl2SymbolProtection8,
 Xdsl2TransmissionModeType,
 Xdsl2Tssi,
 Xdsl2Unit,
 Xdsl2UpboKLF) = mibBuilder.importSymbols(
    "VDSL2-LINE-TC-MIB",
    "Xdsl2Band",
    "Xdsl2BandUs",
    "Xdsl2BitsAlloc",
    "Xdsl2BpscResult",
    "Xdsl2CarMask",
    "Xdsl2ChAtmStatus",
    "Xdsl2ChInitPolicy",
    "Xdsl2ChInpReport",
    "Xdsl2ChPtmStatus",
    "Xdsl2ConfPmsForce",
    "Xdsl2Direction",
    "Xdsl2InitResult",
    "Xdsl2LastTransmittedState",
    "Xdsl2LdsfResult",
    "Xdsl2LineBpsc",
    "Xdsl2LineCeFlag",
    "Xdsl2LineClassMask",
    "Xdsl2LineLdsf",
    "Xdsl2LineLimitMask",
    "Xdsl2LinePmMode",
    "Xdsl2LineProfiles",
    "Xdsl2LinePsdMaskSelectUs",
    "Xdsl2LineReset",
    "Xdsl2LineSnrMode",
    "Xdsl2LineStatus",
    "Xdsl2LineTxRefVnDs",
    "Xdsl2LineTxRefVnUs",
    "Xdsl2LineUs0Disable",
    "Xdsl2LineUs0Mask",
    "Xdsl2MaxBer",
    "Xdsl2MrefPsdDs",
    "Xdsl2MrefPsdUs",
    "Xdsl2OperationModes",
    "Xdsl2PowerMngState",
    "Xdsl2PsdMaskDs",
    "Xdsl2PsdMaskUs",
    "Xdsl2RaMode",
    "Xdsl2RfiBands",
    "Xdsl2ScMaskDs",
    "Xdsl2ScMaskUs",
    "Xdsl2SymbolProtection",
    "Xdsl2SymbolProtection8",
    "Xdsl2TransmissionModeType",
    "Xdsl2Tssi",
    "Xdsl2Unit",
    "Xdsl2UpboKLF")


# MODULE-IDENTITY

vdsl2MIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 10, 251)
)
vdsl2MIB.setRevisions(
        ("2009-09-30 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Xdsl2Notifications_ObjectIdentity = ObjectIdentity
xdsl2Notifications = _Xdsl2Notifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 251, 0)
)
_Xdsl2Objects_ObjectIdentity = ObjectIdentity
xdsl2Objects = _Xdsl2Objects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 251, 1)
)
_Xdsl2Line_ObjectIdentity = ObjectIdentity
xdsl2Line = _Xdsl2Line_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 1)
)
_Xdsl2LineTable_Object = MibTable
xdsl2LineTable = _Xdsl2LineTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 1, 1)
)
if mibBuilder.loadTexts:
    xdsl2LineTable.setStatus("current")
_Xdsl2LineEntry_Object = MibTableRow
xdsl2LineEntry = _Xdsl2LineEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 1, 1, 1)
)
xdsl2LineEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    xdsl2LineEntry.setStatus("current")


class _Xdsl2LineConfTemplate_Type(SnmpAdminString):
    """Custom type xdsl2LineConfTemplate based on SnmpAdminString"""
    defaultValue = OctetString("DEFVAL")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Xdsl2LineConfTemplate_Type.__name__ = "SnmpAdminString"
_Xdsl2LineConfTemplate_Object = MibTableColumn
xdsl2LineConfTemplate = _Xdsl2LineConfTemplate_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 1, 1, 1, 1),
    _Xdsl2LineConfTemplate_Type()
)
xdsl2LineConfTemplate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdsl2LineConfTemplate.setStatus("current")


class _Xdsl2LineConfFallbackTemplate_Type(SnmpAdminString):
    """Custom type xdsl2LineConfFallbackTemplate based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Xdsl2LineConfFallbackTemplate_Type.__name__ = "SnmpAdminString"
_Xdsl2LineConfFallbackTemplate_Object = MibTableColumn
xdsl2LineConfFallbackTemplate = _Xdsl2LineConfFallbackTemplate_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 1, 1, 1, 2),
    _Xdsl2LineConfFallbackTemplate_Type()
)
xdsl2LineConfFallbackTemplate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdsl2LineConfFallbackTemplate.setStatus("current")


class _Xdsl2LineAlarmConfTemplate_Type(SnmpAdminString):
    """Custom type xdsl2LineAlarmConfTemplate based on SnmpAdminString"""
    defaultValue = OctetString("DEFVAL")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Xdsl2LineAlarmConfTemplate_Type.__name__ = "SnmpAdminString"
_Xdsl2LineAlarmConfTemplate_Object = MibTableColumn
xdsl2LineAlarmConfTemplate = _Xdsl2LineAlarmConfTemplate_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 1, 1, 1, 3),
    _Xdsl2LineAlarmConfTemplate_Type()
)
xdsl2LineAlarmConfTemplate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdsl2LineAlarmConfTemplate.setStatus("current")


class _Xdsl2LineCmndConfPmsf_Type(Xdsl2ConfPmsForce):
    """Custom type xdsl2LineCmndConfPmsf based on Xdsl2ConfPmsForce"""


_Xdsl2LineCmndConfPmsf_Object = MibTableColumn
xdsl2LineCmndConfPmsf = _Xdsl2LineCmndConfPmsf_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 1, 1, 1, 4),
    _Xdsl2LineCmndConfPmsf_Type()
)
xdsl2LineCmndConfPmsf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdsl2LineCmndConfPmsf.setStatus("current")


class _Xdsl2LineCmndConfLdsf_Type(Xdsl2LineLdsf):
    """Custom type xdsl2LineCmndConfLdsf based on Xdsl2LineLdsf"""


_Xdsl2LineCmndConfLdsf_Object = MibTableColumn
xdsl2LineCmndConfLdsf = _Xdsl2LineCmndConfLdsf_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 1, 1, 1, 5),
    _Xdsl2LineCmndConfLdsf_Type()
)
xdsl2LineCmndConfLdsf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdsl2LineCmndConfLdsf.setStatus("current")


class _Xdsl2LineCmndConfLdsfFailReason_Type(Xdsl2LdsfResult):
    """Custom type xdsl2LineCmndConfLdsfFailReason based on Xdsl2LdsfResult"""


_Xdsl2LineCmndConfLdsfFailReason_Object = MibTableColumn
xdsl2LineCmndConfLdsfFailReason = _Xdsl2LineCmndConfLdsfFailReason_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 1, 1, 1, 6),
    _Xdsl2LineCmndConfLdsfFailReason_Type()
)
xdsl2LineCmndConfLdsfFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineCmndConfLdsfFailReason.setStatus("current")


class _Xdsl2LineCmndConfBpsc_Type(Xdsl2LineBpsc):
    """Custom type xdsl2LineCmndConfBpsc based on Xdsl2LineBpsc"""


_Xdsl2LineCmndConfBpsc_Object = MibTableColumn
xdsl2LineCmndConfBpsc = _Xdsl2LineCmndConfBpsc_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 1, 1, 1, 7),
    _Xdsl2LineCmndConfBpsc_Type()
)
xdsl2LineCmndConfBpsc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdsl2LineCmndConfBpsc.setStatus("current")


class _Xdsl2LineCmndConfBpscFailReason_Type(Xdsl2BpscResult):
    """Custom type xdsl2LineCmndConfBpscFailReason based on Xdsl2BpscResult"""


_Xdsl2LineCmndConfBpscFailReason_Object = MibTableColumn
xdsl2LineCmndConfBpscFailReason = _Xdsl2LineCmndConfBpscFailReason_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 1, 1, 1, 8),
    _Xdsl2LineCmndConfBpscFailReason_Type()
)
xdsl2LineCmndConfBpscFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineCmndConfBpscFailReason.setStatus("current")
_Xdsl2LineCmndConfBpscRequests_Type = Counter32
_Xdsl2LineCmndConfBpscRequests_Object = MibTableColumn
xdsl2LineCmndConfBpscRequests = _Xdsl2LineCmndConfBpscRequests_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 1, 1, 1, 9),
    _Xdsl2LineCmndConfBpscRequests_Type()
)
xdsl2LineCmndConfBpscRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineCmndConfBpscRequests.setStatus("current")


class _Xdsl2LineCmndAutomodeColdStart_Type(TruthValue):
    """Custom type xdsl2LineCmndAutomodeColdStart based on TruthValue"""


_Xdsl2LineCmndAutomodeColdStart_Object = MibTableColumn
xdsl2LineCmndAutomodeColdStart = _Xdsl2LineCmndAutomodeColdStart_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 1, 1, 1, 10),
    _Xdsl2LineCmndAutomodeColdStart_Type()
)
xdsl2LineCmndAutomodeColdStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdsl2LineCmndAutomodeColdStart.setStatus("current")


class _Xdsl2LineCmndConfReset_Type(Xdsl2LineReset):
    """Custom type xdsl2LineCmndConfReset based on Xdsl2LineReset"""


_Xdsl2LineCmndConfReset_Object = MibTableColumn
xdsl2LineCmndConfReset = _Xdsl2LineCmndConfReset_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 1, 1, 1, 11),
    _Xdsl2LineCmndConfReset_Type()
)
xdsl2LineCmndConfReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdsl2LineCmndConfReset.setStatus("current")


class _Xdsl2LineStatusActTemplate_Type(SnmpAdminString):
    """Custom type xdsl2LineStatusActTemplate based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Xdsl2LineStatusActTemplate_Type.__name__ = "SnmpAdminString"
_Xdsl2LineStatusActTemplate_Object = MibTableColumn
xdsl2LineStatusActTemplate = _Xdsl2LineStatusActTemplate_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 1, 1, 1, 12),
    _Xdsl2LineStatusActTemplate_Type()
)
xdsl2LineStatusActTemplate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineStatusActTemplate.setStatus("current")


class _Xdsl2LineStatusXtuTransSys_Type(Xdsl2TransmissionModeType):
    """Custom type xdsl2LineStatusXtuTransSys based on Xdsl2TransmissionModeType"""
    defaultBinValue = "0"


_Xdsl2LineStatusXtuTransSys_Object = MibTableColumn
xdsl2LineStatusXtuTransSys = _Xdsl2LineStatusXtuTransSys_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 1, 1, 1, 13),
    _Xdsl2LineStatusXtuTransSys_Type()
)
xdsl2LineStatusXtuTransSys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineStatusXtuTransSys.setStatus("current")


class _Xdsl2LineStatusPwrMngState_Type(Xdsl2PowerMngState):
    """Custom type xdsl2LineStatusPwrMngState based on Xdsl2PowerMngState"""


_Xdsl2LineStatusPwrMngState_Object = MibTableColumn
xdsl2LineStatusPwrMngState = _Xdsl2LineStatusPwrMngState_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 1, 1, 1, 14),
    _Xdsl2LineStatusPwrMngState_Type()
)
xdsl2LineStatusPwrMngState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineStatusPwrMngState.setStatus("current")


class _Xdsl2LineStatusInitResult_Type(Xdsl2InitResult):
    """Custom type xdsl2LineStatusInitResult based on Xdsl2InitResult"""


_Xdsl2LineStatusInitResult_Object = MibTableColumn
xdsl2LineStatusInitResult = _Xdsl2LineStatusInitResult_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 1, 1, 1, 15),
    _Xdsl2LineStatusInitResult_Type()
)
xdsl2LineStatusInitResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineStatusInitResult.setStatus("current")


class _Xdsl2LineStatusLastStateDs_Type(Xdsl2LastTransmittedState):
    """Custom type xdsl2LineStatusLastStateDs based on Xdsl2LastTransmittedState"""


_Xdsl2LineStatusLastStateDs_Object = MibTableColumn
xdsl2LineStatusLastStateDs = _Xdsl2LineStatusLastStateDs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 1, 1, 1, 16),
    _Xdsl2LineStatusLastStateDs_Type()
)
xdsl2LineStatusLastStateDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineStatusLastStateDs.setStatus("current")


class _Xdsl2LineStatusLastStateUs_Type(Xdsl2LastTransmittedState):
    """Custom type xdsl2LineStatusLastStateUs based on Xdsl2LastTransmittedState"""


_Xdsl2LineStatusLastStateUs_Object = MibTableColumn
xdsl2LineStatusLastStateUs = _Xdsl2LineStatusLastStateUs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 1, 1, 1, 17),
    _Xdsl2LineStatusLastStateUs_Type()
)
xdsl2LineStatusLastStateUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineStatusLastStateUs.setStatus("current")


class _Xdsl2LineStatusXtur_Type(Xdsl2LineStatus):
    """Custom type xdsl2LineStatusXtur based on Xdsl2LineStatus"""
    defaultBinValue = "1"


_Xdsl2LineStatusXtur_Object = MibTableColumn
xdsl2LineStatusXtur = _Xdsl2LineStatusXtur_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 1, 1, 1, 18),
    _Xdsl2LineStatusXtur_Type()
)
xdsl2LineStatusXtur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineStatusXtur.setStatus("current")


class _Xdsl2LineStatusXtuc_Type(Xdsl2LineStatus):
    """Custom type xdsl2LineStatusXtuc based on Xdsl2LineStatus"""
    defaultBinValue = "1"


_Xdsl2LineStatusXtuc_Object = MibTableColumn
xdsl2LineStatusXtuc = _Xdsl2LineStatusXtuc_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 1, 1, 1, 19),
    _Xdsl2LineStatusXtuc_Type()
)
xdsl2LineStatusXtuc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineStatusXtuc.setStatus("current")


class _Xdsl2LineStatusAttainableRateDs_Type(Unsigned32):
    """Custom type xdsl2LineStatusAttainableRateDs based on Unsigned32"""
    defaultValue = 0


_Xdsl2LineStatusAttainableRateDs_Object = MibTableColumn
xdsl2LineStatusAttainableRateDs = _Xdsl2LineStatusAttainableRateDs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 1, 1, 1, 20),
    _Xdsl2LineStatusAttainableRateDs_Type()
)
xdsl2LineStatusAttainableRateDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineStatusAttainableRateDs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LineStatusAttainableRateDs.setUnits("bits/second")


class _Xdsl2LineStatusAttainableRateUs_Type(Unsigned32):
    """Custom type xdsl2LineStatusAttainableRateUs based on Unsigned32"""
    defaultValue = 0


_Xdsl2LineStatusAttainableRateUs_Object = MibTableColumn
xdsl2LineStatusAttainableRateUs = _Xdsl2LineStatusAttainableRateUs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 1, 1, 1, 21),
    _Xdsl2LineStatusAttainableRateUs_Type()
)
xdsl2LineStatusAttainableRateUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineStatusAttainableRateUs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LineStatusAttainableRateUs.setUnits("bits/second")


class _Xdsl2LineStatusActPsdDs_Type(Integer32):
    """Custom type xdsl2LineStatusActPsdDs based on Integer32"""
    defaultValue = 2147483647

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-900, 0),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_Xdsl2LineStatusActPsdDs_Type.__name__ = "Integer32"
_Xdsl2LineStatusActPsdDs_Object = MibTableColumn
xdsl2LineStatusActPsdDs = _Xdsl2LineStatusActPsdDs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 1, 1, 1, 22),
    _Xdsl2LineStatusActPsdDs_Type()
)
xdsl2LineStatusActPsdDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineStatusActPsdDs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LineStatusActPsdDs.setUnits("0.1 dBm/Hz")


class _Xdsl2LineStatusActPsdUs_Type(Integer32):
    """Custom type xdsl2LineStatusActPsdUs based on Integer32"""
    defaultValue = 2147483647

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-900, 0),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_Xdsl2LineStatusActPsdUs_Type.__name__ = "Integer32"
_Xdsl2LineStatusActPsdUs_Object = MibTableColumn
xdsl2LineStatusActPsdUs = _Xdsl2LineStatusActPsdUs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 1, 1, 1, 23),
    _Xdsl2LineStatusActPsdUs_Type()
)
xdsl2LineStatusActPsdUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineStatusActPsdUs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LineStatusActPsdUs.setUnits("0.1 dBm/Hz")


class _Xdsl2LineStatusActAtpDs_Type(Integer32):
    """Custom type xdsl2LineStatusActAtpDs based on Integer32"""
    defaultValue = 2147483647

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-310, 310),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_Xdsl2LineStatusActAtpDs_Type.__name__ = "Integer32"
_Xdsl2LineStatusActAtpDs_Object = MibTableColumn
xdsl2LineStatusActAtpDs = _Xdsl2LineStatusActAtpDs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 1, 1, 1, 24),
    _Xdsl2LineStatusActAtpDs_Type()
)
xdsl2LineStatusActAtpDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineStatusActAtpDs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LineStatusActAtpDs.setUnits("0.1 dBm")


class _Xdsl2LineStatusActAtpUs_Type(Integer32):
    """Custom type xdsl2LineStatusActAtpUs based on Integer32"""
    defaultValue = 2147483647

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-310, 310),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_Xdsl2LineStatusActAtpUs_Type.__name__ = "Integer32"
_Xdsl2LineStatusActAtpUs_Object = MibTableColumn
xdsl2LineStatusActAtpUs = _Xdsl2LineStatusActAtpUs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 1, 1, 1, 25),
    _Xdsl2LineStatusActAtpUs_Type()
)
xdsl2LineStatusActAtpUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineStatusActAtpUs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LineStatusActAtpUs.setUnits("0.1 dBm")


class _Xdsl2LineStatusActProfile_Type(Xdsl2LineProfiles):
    """Custom type xdsl2LineStatusActProfile based on Xdsl2LineProfiles"""
    defaultBinValue = "0"


_Xdsl2LineStatusActProfile_Object = MibTableColumn
xdsl2LineStatusActProfile = _Xdsl2LineStatusActProfile_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 1, 1, 1, 26),
    _Xdsl2LineStatusActProfile_Type()
)
xdsl2LineStatusActProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineStatusActProfile.setStatus("current")


class _Xdsl2LineStatusActLimitMask_Type(Xdsl2LineLimitMask):
    """Custom type xdsl2LineStatusActLimitMask based on Xdsl2LineLimitMask"""
    defaultBinValue = "0"


_Xdsl2LineStatusActLimitMask_Object = MibTableColumn
xdsl2LineStatusActLimitMask = _Xdsl2LineStatusActLimitMask_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 1, 1, 1, 27),
    _Xdsl2LineStatusActLimitMask_Type()
)
xdsl2LineStatusActLimitMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineStatusActLimitMask.setStatus("current")


class _Xdsl2LineStatusActUs0Mask_Type(Xdsl2LineUs0Mask):
    """Custom type xdsl2LineStatusActUs0Mask based on Xdsl2LineUs0Mask"""
    defaultBinValue = "0"


_Xdsl2LineStatusActUs0Mask_Object = MibTableColumn
xdsl2LineStatusActUs0Mask = _Xdsl2LineStatusActUs0Mask_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 1, 1, 1, 28),
    _Xdsl2LineStatusActUs0Mask_Type()
)
xdsl2LineStatusActUs0Mask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineStatusActUs0Mask.setStatus("current")


class _Xdsl2LineStatusActSnrModeDs_Type(Xdsl2LineSnrMode):
    """Custom type xdsl2LineStatusActSnrModeDs based on Xdsl2LineSnrMode"""


_Xdsl2LineStatusActSnrModeDs_Object = MibTableColumn
xdsl2LineStatusActSnrModeDs = _Xdsl2LineStatusActSnrModeDs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 1, 1, 1, 29),
    _Xdsl2LineStatusActSnrModeDs_Type()
)
xdsl2LineStatusActSnrModeDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineStatusActSnrModeDs.setStatus("current")


class _Xdsl2LineStatusActSnrModeUs_Type(Xdsl2LineSnrMode):
    """Custom type xdsl2LineStatusActSnrModeUs based on Xdsl2LineSnrMode"""


_Xdsl2LineStatusActSnrModeUs_Object = MibTableColumn
xdsl2LineStatusActSnrModeUs = _Xdsl2LineStatusActSnrModeUs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 1, 1, 1, 30),
    _Xdsl2LineStatusActSnrModeUs_Type()
)
xdsl2LineStatusActSnrModeUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineStatusActSnrModeUs.setStatus("current")


class _Xdsl2LineStatusElectricalLength_Type(Unsigned32):
    """Custom type xdsl2LineStatusElectricalLength based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1280),
    )


_Xdsl2LineStatusElectricalLength_Type.__name__ = "Unsigned32"
_Xdsl2LineStatusElectricalLength_Object = MibTableColumn
xdsl2LineStatusElectricalLength = _Xdsl2LineStatusElectricalLength_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 1, 1, 1, 31),
    _Xdsl2LineStatusElectricalLength_Type()
)
xdsl2LineStatusElectricalLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineStatusElectricalLength.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LineStatusElectricalLength.setUnits("0.1 dB")
_Xdsl2LineStatusTssiDs_Type = Xdsl2Tssi
_Xdsl2LineStatusTssiDs_Object = MibTableColumn
xdsl2LineStatusTssiDs = _Xdsl2LineStatusTssiDs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 1, 1, 1, 32),
    _Xdsl2LineStatusTssiDs_Type()
)
xdsl2LineStatusTssiDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineStatusTssiDs.setStatus("current")
_Xdsl2LineStatusTssiUs_Type = Xdsl2Tssi
_Xdsl2LineStatusTssiUs_Object = MibTableColumn
xdsl2LineStatusTssiUs = _Xdsl2LineStatusTssiUs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 1, 1, 1, 33),
    _Xdsl2LineStatusTssiUs_Type()
)
xdsl2LineStatusTssiUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineStatusTssiUs.setStatus("current")
_Xdsl2LineStatusMrefPsdDs_Type = Xdsl2MrefPsdDs
_Xdsl2LineStatusMrefPsdDs_Object = MibTableColumn
xdsl2LineStatusMrefPsdDs = _Xdsl2LineStatusMrefPsdDs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 1, 1, 1, 34),
    _Xdsl2LineStatusMrefPsdDs_Type()
)
xdsl2LineStatusMrefPsdDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineStatusMrefPsdDs.setStatus("current")
_Xdsl2LineStatusMrefPsdUs_Type = Xdsl2MrefPsdUs
_Xdsl2LineStatusMrefPsdUs_Object = MibTableColumn
xdsl2LineStatusMrefPsdUs = _Xdsl2LineStatusMrefPsdUs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 1, 1, 1, 35),
    _Xdsl2LineStatusMrefPsdUs_Type()
)
xdsl2LineStatusMrefPsdUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineStatusMrefPsdUs.setStatus("current")


class _Xdsl2LineStatusTrellisDs_Type(TruthValue):
    """Custom type xdsl2LineStatusTrellisDs based on TruthValue"""


_Xdsl2LineStatusTrellisDs_Object = MibTableColumn
xdsl2LineStatusTrellisDs = _Xdsl2LineStatusTrellisDs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 1, 1, 1, 36),
    _Xdsl2LineStatusTrellisDs_Type()
)
xdsl2LineStatusTrellisDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineStatusTrellisDs.setStatus("current")


class _Xdsl2LineStatusTrellisUs_Type(TruthValue):
    """Custom type xdsl2LineStatusTrellisUs based on TruthValue"""


_Xdsl2LineStatusTrellisUs_Object = MibTableColumn
xdsl2LineStatusTrellisUs = _Xdsl2LineStatusTrellisUs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 1, 1, 1, 37),
    _Xdsl2LineStatusTrellisUs_Type()
)
xdsl2LineStatusTrellisUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineStatusTrellisUs.setStatus("current")


class _Xdsl2LineStatusActualCe_Type(Unsigned32):
    """Custom type xdsl2LineStatusActualCe based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 16),
    )


_Xdsl2LineStatusActualCe_Type.__name__ = "Unsigned32"
_Xdsl2LineStatusActualCe_Object = MibTableColumn
xdsl2LineStatusActualCe = _Xdsl2LineStatusActualCe_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 1, 1, 1, 38),
    _Xdsl2LineStatusActualCe_Type()
)
xdsl2LineStatusActualCe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineStatusActualCe.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LineStatusActualCe.setUnits("N/32 samples")
_Xdsl2LineBandTable_Object = MibTable
xdsl2LineBandTable = _Xdsl2LineBandTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 1, 2)
)
if mibBuilder.loadTexts:
    xdsl2LineBandTable.setStatus("current")
_Xdsl2LineBandEntry_Object = MibTableRow
xdsl2LineBandEntry = _Xdsl2LineBandEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 1, 2, 1)
)
xdsl2LineBandEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VDSL2-LINE-MIB", "xdsl2LineBand"),
)
if mibBuilder.loadTexts:
    xdsl2LineBandEntry.setStatus("current")
_Xdsl2LineBand_Type = Xdsl2Band
_Xdsl2LineBand_Object = MibTableColumn
xdsl2LineBand = _Xdsl2LineBand_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 1, 2, 1, 1),
    _Xdsl2LineBand_Type()
)
xdsl2LineBand.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xdsl2LineBand.setStatus("current")


class _Xdsl2LineBandStatusLnAtten_Type(Unsigned32):
    """Custom type xdsl2LineBandStatusLnAtten based on Unsigned32"""
    defaultValue = 2147483646

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1270),
        ValueRangeConstraint(2147483646, 2147483646),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_Xdsl2LineBandStatusLnAtten_Type.__name__ = "Unsigned32"
_Xdsl2LineBandStatusLnAtten_Object = MibTableColumn
xdsl2LineBandStatusLnAtten = _Xdsl2LineBandStatusLnAtten_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 1, 2, 1, 2),
    _Xdsl2LineBandStatusLnAtten_Type()
)
xdsl2LineBandStatusLnAtten.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineBandStatusLnAtten.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LineBandStatusLnAtten.setUnits("0.1 dB")


class _Xdsl2LineBandStatusSigAtten_Type(Unsigned32):
    """Custom type xdsl2LineBandStatusSigAtten based on Unsigned32"""
    defaultValue = 2147483646

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1270),
        ValueRangeConstraint(2147483646, 2147483646),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_Xdsl2LineBandStatusSigAtten_Type.__name__ = "Unsigned32"
_Xdsl2LineBandStatusSigAtten_Object = MibTableColumn
xdsl2LineBandStatusSigAtten = _Xdsl2LineBandStatusSigAtten_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 1, 2, 1, 3),
    _Xdsl2LineBandStatusSigAtten_Type()
)
xdsl2LineBandStatusSigAtten.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineBandStatusSigAtten.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LineBandStatusSigAtten.setUnits("0.1 dB")


class _Xdsl2LineBandStatusSnrMargin_Type(Integer32):
    """Custom type xdsl2LineBandStatusSnrMargin based on Integer32"""
    defaultValue = 2147483646

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-640, 630),
        ValueRangeConstraint(2147483646, 2147483646),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_Xdsl2LineBandStatusSnrMargin_Type.__name__ = "Integer32"
_Xdsl2LineBandStatusSnrMargin_Object = MibTableColumn
xdsl2LineBandStatusSnrMargin = _Xdsl2LineBandStatusSnrMargin_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 1, 2, 1, 4),
    _Xdsl2LineBandStatusSnrMargin_Type()
)
xdsl2LineBandStatusSnrMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineBandStatusSnrMargin.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LineBandStatusSnrMargin.setUnits("0.1 dB")
_Xdsl2Status_ObjectIdentity = ObjectIdentity
xdsl2Status = _Xdsl2Status_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 2)
)
_Xdsl2LineSegmentTable_Object = MibTable
xdsl2LineSegmentTable = _Xdsl2LineSegmentTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 2, 1)
)
if mibBuilder.loadTexts:
    xdsl2LineSegmentTable.setStatus("current")
_Xdsl2LineSegmentEntry_Object = MibTableRow
xdsl2LineSegmentEntry = _Xdsl2LineSegmentEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 2, 1, 1)
)
xdsl2LineSegmentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VDSL2-LINE-MIB", "xdsl2LineSegmentDirection"),
    (0, "VDSL2-LINE-MIB", "xdsl2LineSegment"),
)
if mibBuilder.loadTexts:
    xdsl2LineSegmentEntry.setStatus("current")
_Xdsl2LineSegmentDirection_Type = Xdsl2Direction
_Xdsl2LineSegmentDirection_Object = MibTableColumn
xdsl2LineSegmentDirection = _Xdsl2LineSegmentDirection_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 2, 1, 1, 1),
    _Xdsl2LineSegmentDirection_Type()
)
xdsl2LineSegmentDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xdsl2LineSegmentDirection.setStatus("current")


class _Xdsl2LineSegment_Type(Unsigned32):
    """Custom type xdsl2LineSegment based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Xdsl2LineSegment_Type.__name__ = "Unsigned32"
_Xdsl2LineSegment_Object = MibTableColumn
xdsl2LineSegment = _Xdsl2LineSegment_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 2, 1, 1, 2),
    _Xdsl2LineSegment_Type()
)
xdsl2LineSegment.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xdsl2LineSegment.setStatus("current")
_Xdsl2LineSegmentBitsAlloc_Type = Xdsl2BitsAlloc
_Xdsl2LineSegmentBitsAlloc_Object = MibTableColumn
xdsl2LineSegmentBitsAlloc = _Xdsl2LineSegmentBitsAlloc_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 2, 1, 1, 3),
    _Xdsl2LineSegmentBitsAlloc_Type()
)
xdsl2LineSegmentBitsAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LineSegmentBitsAlloc.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LineSegmentBitsAlloc.setUnits("bits")
_Xdsl2LineSegmentRowStatus_Type = RowStatus
_Xdsl2LineSegmentRowStatus_Object = MibTableColumn
xdsl2LineSegmentRowStatus = _Xdsl2LineSegmentRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 2, 1, 1, 4),
    _Xdsl2LineSegmentRowStatus_Type()
)
xdsl2LineSegmentRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdsl2LineSegmentRowStatus.setStatus("current")
_Xdsl2ChannelStatusTable_Object = MibTable
xdsl2ChannelStatusTable = _Xdsl2ChannelStatusTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 2, 2)
)
if mibBuilder.loadTexts:
    xdsl2ChannelStatusTable.setStatus("current")
_Xdsl2ChannelStatusEntry_Object = MibTableRow
xdsl2ChannelStatusEntry = _Xdsl2ChannelStatusEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 2, 2, 1)
)
xdsl2ChannelStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VDSL2-LINE-MIB", "xdsl2ChStatusUnit"),
)
if mibBuilder.loadTexts:
    xdsl2ChannelStatusEntry.setStatus("current")
_Xdsl2ChStatusUnit_Type = Xdsl2Unit
_Xdsl2ChStatusUnit_Object = MibTableColumn
xdsl2ChStatusUnit = _Xdsl2ChStatusUnit_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 2, 2, 1, 1),
    _Xdsl2ChStatusUnit_Type()
)
xdsl2ChStatusUnit.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xdsl2ChStatusUnit.setStatus("current")


class _Xdsl2ChStatusActDataRate_Type(Unsigned32):
    """Custom type xdsl2ChStatusActDataRate based on Unsigned32"""
    defaultValue = 0


_Xdsl2ChStatusActDataRate_Object = MibTableColumn
xdsl2ChStatusActDataRate = _Xdsl2ChStatusActDataRate_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 2, 2, 1, 2),
    _Xdsl2ChStatusActDataRate_Type()
)
xdsl2ChStatusActDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2ChStatusActDataRate.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2ChStatusActDataRate.setUnits("bits/second")


class _Xdsl2ChStatusPrevDataRate_Type(Unsigned32):
    """Custom type xdsl2ChStatusPrevDataRate based on Unsigned32"""
    defaultValue = 0


_Xdsl2ChStatusPrevDataRate_Object = MibTableColumn
xdsl2ChStatusPrevDataRate = _Xdsl2ChStatusPrevDataRate_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 2, 2, 1, 3),
    _Xdsl2ChStatusPrevDataRate_Type()
)
xdsl2ChStatusPrevDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2ChStatusPrevDataRate.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2ChStatusPrevDataRate.setUnits("bits/second")


class _Xdsl2ChStatusActDelay_Type(Unsigned32):
    """Custom type xdsl2ChStatusActDelay based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8176),
    )


_Xdsl2ChStatusActDelay_Type.__name__ = "Unsigned32"
_Xdsl2ChStatusActDelay_Object = MibTableColumn
xdsl2ChStatusActDelay = _Xdsl2ChStatusActDelay_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 2, 2, 1, 4),
    _Xdsl2ChStatusActDelay_Type()
)
xdsl2ChStatusActDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2ChStatusActDelay.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2ChStatusActDelay.setUnits("milliseconds")


class _Xdsl2ChStatusActInp_Type(Unsigned32):
    """Custom type xdsl2ChStatusActInp based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Xdsl2ChStatusActInp_Type.__name__ = "Unsigned32"
_Xdsl2ChStatusActInp_Object = MibTableColumn
xdsl2ChStatusActInp = _Xdsl2ChStatusActInp_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 2, 2, 1, 5),
    _Xdsl2ChStatusActInp_Type()
)
xdsl2ChStatusActInp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2ChStatusActInp.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2ChStatusActInp.setUnits("0.1 symbols")


class _Xdsl2ChStatusInpReport_Type(Xdsl2ChInpReport):
    """Custom type xdsl2ChStatusInpReport based on Xdsl2ChInpReport"""


_Xdsl2ChStatusInpReport_Object = MibTableColumn
xdsl2ChStatusInpReport = _Xdsl2ChStatusInpReport_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 2, 2, 1, 6),
    _Xdsl2ChStatusInpReport_Type()
)
xdsl2ChStatusInpReport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2ChStatusInpReport.setStatus("current")


class _Xdsl2ChStatusNFec_Type(Unsigned32):
    """Custom type xdsl2ChStatusNFec based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Xdsl2ChStatusNFec_Type.__name__ = "Unsigned32"
_Xdsl2ChStatusNFec_Object = MibTableColumn
xdsl2ChStatusNFec = _Xdsl2ChStatusNFec_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 2, 2, 1, 7),
    _Xdsl2ChStatusNFec_Type()
)
xdsl2ChStatusNFec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2ChStatusNFec.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2ChStatusNFec.setUnits("bytes")


class _Xdsl2ChStatusRFec_Type(Unsigned32):
    """Custom type xdsl2ChStatusRFec based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_Xdsl2ChStatusRFec_Type.__name__ = "Unsigned32"
_Xdsl2ChStatusRFec_Object = MibTableColumn
xdsl2ChStatusRFec = _Xdsl2ChStatusRFec_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 2, 2, 1, 8),
    _Xdsl2ChStatusRFec_Type()
)
xdsl2ChStatusRFec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2ChStatusRFec.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2ChStatusRFec.setUnits("bits")


class _Xdsl2ChStatusLSymb_Type(Unsigned32):
    """Custom type xdsl2ChStatusLSymb based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Xdsl2ChStatusLSymb_Type.__name__ = "Unsigned32"
_Xdsl2ChStatusLSymb_Object = MibTableColumn
xdsl2ChStatusLSymb = _Xdsl2ChStatusLSymb_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 2, 2, 1, 9),
    _Xdsl2ChStatusLSymb_Type()
)
xdsl2ChStatusLSymb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2ChStatusLSymb.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2ChStatusLSymb.setUnits("bits")


class _Xdsl2ChStatusIntlvDepth_Type(Unsigned32):
    """Custom type xdsl2ChStatusIntlvDepth based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_Xdsl2ChStatusIntlvDepth_Type.__name__ = "Unsigned32"
_Xdsl2ChStatusIntlvDepth_Object = MibTableColumn
xdsl2ChStatusIntlvDepth = _Xdsl2ChStatusIntlvDepth_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 2, 2, 1, 10),
    _Xdsl2ChStatusIntlvDepth_Type()
)
xdsl2ChStatusIntlvDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2ChStatusIntlvDepth.setStatus("current")


class _Xdsl2ChStatusIntlvBlock_Type(Unsigned32):
    """Custom type xdsl2ChStatusIntlvBlock based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 255),
    )


_Xdsl2ChStatusIntlvBlock_Type.__name__ = "Unsigned32"
_Xdsl2ChStatusIntlvBlock_Object = MibTableColumn
xdsl2ChStatusIntlvBlock = _Xdsl2ChStatusIntlvBlock_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 2, 2, 1, 11),
    _Xdsl2ChStatusIntlvBlock_Type()
)
xdsl2ChStatusIntlvBlock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2ChStatusIntlvBlock.setStatus("current")


class _Xdsl2ChStatusLPath_Type(Unsigned32):
    """Custom type xdsl2ChStatusLPath based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_Xdsl2ChStatusLPath_Type.__name__ = "Unsigned32"
_Xdsl2ChStatusLPath_Object = MibTableColumn
xdsl2ChStatusLPath = _Xdsl2ChStatusLPath_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 2, 2, 1, 12),
    _Xdsl2ChStatusLPath_Type()
)
xdsl2ChStatusLPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2ChStatusLPath.setStatus("current")


class _Xdsl2ChStatusAtmStatus_Type(Xdsl2ChAtmStatus):
    """Custom type xdsl2ChStatusAtmStatus based on Xdsl2ChAtmStatus"""
    defaultBinValue = "1"


_Xdsl2ChStatusAtmStatus_Object = MibTableColumn
xdsl2ChStatusAtmStatus = _Xdsl2ChStatusAtmStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 2, 2, 1, 13),
    _Xdsl2ChStatusAtmStatus_Type()
)
xdsl2ChStatusAtmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2ChStatusAtmStatus.setStatus("current")


class _Xdsl2ChStatusPtmStatus_Type(Xdsl2ChPtmStatus):
    """Custom type xdsl2ChStatusPtmStatus based on Xdsl2ChPtmStatus"""
    defaultBinValue = "1"


_Xdsl2ChStatusPtmStatus_Object = MibTableColumn
xdsl2ChStatusPtmStatus = _Xdsl2ChStatusPtmStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 2, 2, 1, 14),
    _Xdsl2ChStatusPtmStatus_Type()
)
xdsl2ChStatusPtmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2ChStatusPtmStatus.setStatus("current")
_Xdsl2SCStatusTable_Object = MibTable
xdsl2SCStatusTable = _Xdsl2SCStatusTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 2, 3)
)
if mibBuilder.loadTexts:
    xdsl2SCStatusTable.setStatus("current")
_Xdsl2SCStatusEntry_Object = MibTableRow
xdsl2SCStatusEntry = _Xdsl2SCStatusEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 2, 3, 1)
)
xdsl2SCStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VDSL2-LINE-MIB", "xdsl2SCStatusDirection"),
)
if mibBuilder.loadTexts:
    xdsl2SCStatusEntry.setStatus("current")
_Xdsl2SCStatusDirection_Type = Xdsl2Direction
_Xdsl2SCStatusDirection_Object = MibTableColumn
xdsl2SCStatusDirection = _Xdsl2SCStatusDirection_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 2, 3, 1, 1),
    _Xdsl2SCStatusDirection_Type()
)
xdsl2SCStatusDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xdsl2SCStatusDirection.setStatus("current")


class _Xdsl2SCStatusLinScale_Type(Unsigned32):
    """Custom type xdsl2SCStatusLinScale based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Xdsl2SCStatusLinScale_Type.__name__ = "Unsigned32"
_Xdsl2SCStatusLinScale_Object = MibTableColumn
xdsl2SCStatusLinScale = _Xdsl2SCStatusLinScale_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 2, 3, 1, 2),
    _Xdsl2SCStatusLinScale_Type()
)
xdsl2SCStatusLinScale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2SCStatusLinScale.setStatus("current")


class _Xdsl2SCStatusLinScGroupSize_Type(Unsigned32):
    """Custom type xdsl2SCStatusLinScGroupSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(8, 8),
    )


_Xdsl2SCStatusLinScGroupSize_Type.__name__ = "Unsigned32"
_Xdsl2SCStatusLinScGroupSize_Object = MibTableColumn
xdsl2SCStatusLinScGroupSize = _Xdsl2SCStatusLinScGroupSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 2, 3, 1, 3),
    _Xdsl2SCStatusLinScGroupSize_Type()
)
xdsl2SCStatusLinScGroupSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2SCStatusLinScGroupSize.setStatus("current")


class _Xdsl2SCStatusLogMt_Type(Unsigned32):
    """Custom type xdsl2SCStatusLogMt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Xdsl2SCStatusLogMt_Type.__name__ = "Unsigned32"
_Xdsl2SCStatusLogMt_Object = MibTableColumn
xdsl2SCStatusLogMt = _Xdsl2SCStatusLogMt_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 2, 3, 1, 4),
    _Xdsl2SCStatusLogMt_Type()
)
xdsl2SCStatusLogMt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2SCStatusLogMt.setStatus("current")


class _Xdsl2SCStatusLogScGroupSize_Type(Unsigned32):
    """Custom type xdsl2SCStatusLogScGroupSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(8, 8),
    )


_Xdsl2SCStatusLogScGroupSize_Type.__name__ = "Unsigned32"
_Xdsl2SCStatusLogScGroupSize_Object = MibTableColumn
xdsl2SCStatusLogScGroupSize = _Xdsl2SCStatusLogScGroupSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 2, 3, 1, 5),
    _Xdsl2SCStatusLogScGroupSize_Type()
)
xdsl2SCStatusLogScGroupSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2SCStatusLogScGroupSize.setStatus("current")


class _Xdsl2SCStatusQlnMt_Type(Unsigned32):
    """Custom type xdsl2SCStatusQlnMt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Xdsl2SCStatusQlnMt_Type.__name__ = "Unsigned32"
_Xdsl2SCStatusQlnMt_Object = MibTableColumn
xdsl2SCStatusQlnMt = _Xdsl2SCStatusQlnMt_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 2, 3, 1, 6),
    _Xdsl2SCStatusQlnMt_Type()
)
xdsl2SCStatusQlnMt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2SCStatusQlnMt.setStatus("current")


class _Xdsl2SCStatusQlnScGroupSize_Type(Unsigned32):
    """Custom type xdsl2SCStatusQlnScGroupSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(8, 8),
    )


_Xdsl2SCStatusQlnScGroupSize_Type.__name__ = "Unsigned32"
_Xdsl2SCStatusQlnScGroupSize_Object = MibTableColumn
xdsl2SCStatusQlnScGroupSize = _Xdsl2SCStatusQlnScGroupSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 2, 3, 1, 7),
    _Xdsl2SCStatusQlnScGroupSize_Type()
)
xdsl2SCStatusQlnScGroupSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2SCStatusQlnScGroupSize.setStatus("current")


class _Xdsl2SCStatusSnrMtime_Type(Unsigned32):
    """Custom type xdsl2SCStatusSnrMtime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Xdsl2SCStatusSnrMtime_Type.__name__ = "Unsigned32"
_Xdsl2SCStatusSnrMtime_Object = MibTableColumn
xdsl2SCStatusSnrMtime = _Xdsl2SCStatusSnrMtime_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 2, 3, 1, 8),
    _Xdsl2SCStatusSnrMtime_Type()
)
xdsl2SCStatusSnrMtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2SCStatusSnrMtime.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2SCStatusSnrMtime.setUnits("symbols")


class _Xdsl2SCStatusSnrScGroupSize_Type(Unsigned32):
    """Custom type xdsl2SCStatusSnrScGroupSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(2, 2),
        ValueRangeConstraint(4, 4),
        ValueRangeConstraint(8, 8),
    )


_Xdsl2SCStatusSnrScGroupSize_Type.__name__ = "Unsigned32"
_Xdsl2SCStatusSnrScGroupSize_Object = MibTableColumn
xdsl2SCStatusSnrScGroupSize = _Xdsl2SCStatusSnrScGroupSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 2, 3, 1, 9),
    _Xdsl2SCStatusSnrScGroupSize_Type()
)
xdsl2SCStatusSnrScGroupSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2SCStatusSnrScGroupSize.setStatus("current")
_Xdsl2SCStatusAttainableRate_Type = Unsigned32
_Xdsl2SCStatusAttainableRate_Object = MibTableColumn
xdsl2SCStatusAttainableRate = _Xdsl2SCStatusAttainableRate_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 2, 3, 1, 10),
    _Xdsl2SCStatusAttainableRate_Type()
)
xdsl2SCStatusAttainableRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2SCStatusAttainableRate.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2SCStatusAttainableRate.setUnits("bits/second")
_Xdsl2SCStatusRowStatus_Type = RowStatus
_Xdsl2SCStatusRowStatus_Object = MibTableColumn
xdsl2SCStatusRowStatus = _Xdsl2SCStatusRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 2, 3, 1, 11),
    _Xdsl2SCStatusRowStatus_Type()
)
xdsl2SCStatusRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xdsl2SCStatusRowStatus.setStatus("current")
_Xdsl2SCStatusBandTable_Object = MibTable
xdsl2SCStatusBandTable = _Xdsl2SCStatusBandTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 2, 4)
)
if mibBuilder.loadTexts:
    xdsl2SCStatusBandTable.setStatus("current")
_Xdsl2SCStatusBandEntry_Object = MibTableRow
xdsl2SCStatusBandEntry = _Xdsl2SCStatusBandEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 2, 4, 1)
)
xdsl2SCStatusBandEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VDSL2-LINE-MIB", "xdsl2SCStatusBand"),
)
if mibBuilder.loadTexts:
    xdsl2SCStatusBandEntry.setStatus("current")
_Xdsl2SCStatusBand_Type = Xdsl2Band
_Xdsl2SCStatusBand_Object = MibTableColumn
xdsl2SCStatusBand = _Xdsl2SCStatusBand_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 2, 4, 1, 1),
    _Xdsl2SCStatusBand_Type()
)
xdsl2SCStatusBand.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xdsl2SCStatusBand.setStatus("current")


class _Xdsl2SCStatusBandLnAtten_Type(Unsigned32):
    """Custom type xdsl2SCStatusBandLnAtten based on Unsigned32"""
    defaultValue = 2147483646

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1270),
        ValueRangeConstraint(2147483646, 2147483646),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_Xdsl2SCStatusBandLnAtten_Type.__name__ = "Unsigned32"
_Xdsl2SCStatusBandLnAtten_Object = MibTableColumn
xdsl2SCStatusBandLnAtten = _Xdsl2SCStatusBandLnAtten_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 2, 4, 1, 2),
    _Xdsl2SCStatusBandLnAtten_Type()
)
xdsl2SCStatusBandLnAtten.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2SCStatusBandLnAtten.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2SCStatusBandLnAtten.setUnits("0.1 dB")


class _Xdsl2SCStatusBandSigAtten_Type(Unsigned32):
    """Custom type xdsl2SCStatusBandSigAtten based on Unsigned32"""
    defaultValue = 2147483646

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1270),
        ValueRangeConstraint(2147483646, 2147483646),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_Xdsl2SCStatusBandSigAtten_Type.__name__ = "Unsigned32"
_Xdsl2SCStatusBandSigAtten_Object = MibTableColumn
xdsl2SCStatusBandSigAtten = _Xdsl2SCStatusBandSigAtten_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 2, 4, 1, 3),
    _Xdsl2SCStatusBandSigAtten_Type()
)
xdsl2SCStatusBandSigAtten.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2SCStatusBandSigAtten.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2SCStatusBandSigAtten.setUnits("0.1 dB")
_Xdsl2SCStatusSegmentTable_Object = MibTable
xdsl2SCStatusSegmentTable = _Xdsl2SCStatusSegmentTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 2, 5)
)
if mibBuilder.loadTexts:
    xdsl2SCStatusSegmentTable.setStatus("current")
_Xdsl2SCStatusSegmentEntry_Object = MibTableRow
xdsl2SCStatusSegmentEntry = _Xdsl2SCStatusSegmentEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 2, 5, 1)
)
xdsl2SCStatusSegmentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VDSL2-LINE-MIB", "xdsl2SCStatusDirection"),
    (0, "VDSL2-LINE-MIB", "xdsl2SCStatusSegment"),
)
if mibBuilder.loadTexts:
    xdsl2SCStatusSegmentEntry.setStatus("current")


class _Xdsl2SCStatusSegment_Type(Unsigned32):
    """Custom type xdsl2SCStatusSegment based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Xdsl2SCStatusSegment_Type.__name__ = "Unsigned32"
_Xdsl2SCStatusSegment_Object = MibTableColumn
xdsl2SCStatusSegment = _Xdsl2SCStatusSegment_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 2, 5, 1, 1),
    _Xdsl2SCStatusSegment_Type()
)
xdsl2SCStatusSegment.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xdsl2SCStatusSegment.setStatus("current")


class _Xdsl2SCStatusSegmentLinReal_Type(OctetString):
    """Custom type xdsl2SCStatusSegmentLinReal based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_Xdsl2SCStatusSegmentLinReal_Type.__name__ = "OctetString"
_Xdsl2SCStatusSegmentLinReal_Object = MibTableColumn
xdsl2SCStatusSegmentLinReal = _Xdsl2SCStatusSegmentLinReal_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 2, 5, 1, 2),
    _Xdsl2SCStatusSegmentLinReal_Type()
)
xdsl2SCStatusSegmentLinReal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2SCStatusSegmentLinReal.setStatus("current")


class _Xdsl2SCStatusSegmentLinImg_Type(OctetString):
    """Custom type xdsl2SCStatusSegmentLinImg based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_Xdsl2SCStatusSegmentLinImg_Type.__name__ = "OctetString"
_Xdsl2SCStatusSegmentLinImg_Object = MibTableColumn
xdsl2SCStatusSegmentLinImg = _Xdsl2SCStatusSegmentLinImg_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 2, 5, 1, 3),
    _Xdsl2SCStatusSegmentLinImg_Type()
)
xdsl2SCStatusSegmentLinImg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2SCStatusSegmentLinImg.setStatus("current")


class _Xdsl2SCStatusSegmentLog_Type(OctetString):
    """Custom type xdsl2SCStatusSegmentLog based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_Xdsl2SCStatusSegmentLog_Type.__name__ = "OctetString"
_Xdsl2SCStatusSegmentLog_Object = MibTableColumn
xdsl2SCStatusSegmentLog = _Xdsl2SCStatusSegmentLog_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 2, 5, 1, 4),
    _Xdsl2SCStatusSegmentLog_Type()
)
xdsl2SCStatusSegmentLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2SCStatusSegmentLog.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2SCStatusSegmentLog.setUnits("dB")


class _Xdsl2SCStatusSegmentQln_Type(OctetString):
    """Custom type xdsl2SCStatusSegmentQln based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_Xdsl2SCStatusSegmentQln_Type.__name__ = "OctetString"
_Xdsl2SCStatusSegmentQln_Object = MibTableColumn
xdsl2SCStatusSegmentQln = _Xdsl2SCStatusSegmentQln_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 2, 5, 1, 5),
    _Xdsl2SCStatusSegmentQln_Type()
)
xdsl2SCStatusSegmentQln.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2SCStatusSegmentQln.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2SCStatusSegmentQln.setUnits("dBm/Hz")


class _Xdsl2SCStatusSegmentSnr_Type(OctetString):
    """Custom type xdsl2SCStatusSegmentSnr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_Xdsl2SCStatusSegmentSnr_Type.__name__ = "OctetString"
_Xdsl2SCStatusSegmentSnr_Object = MibTableColumn
xdsl2SCStatusSegmentSnr = _Xdsl2SCStatusSegmentSnr_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 2, 5, 1, 6),
    _Xdsl2SCStatusSegmentSnr_Type()
)
xdsl2SCStatusSegmentSnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2SCStatusSegmentSnr.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2SCStatusSegmentSnr.setUnits("0.5 dB")
_Xdsl2SCStatusSegmentBitsAlloc_Type = Xdsl2BitsAlloc
_Xdsl2SCStatusSegmentBitsAlloc_Object = MibTableColumn
xdsl2SCStatusSegmentBitsAlloc = _Xdsl2SCStatusSegmentBitsAlloc_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 2, 5, 1, 7),
    _Xdsl2SCStatusSegmentBitsAlloc_Type()
)
xdsl2SCStatusSegmentBitsAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2SCStatusSegmentBitsAlloc.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2SCStatusSegmentBitsAlloc.setUnits("bits")


class _Xdsl2SCStatusSegmentGainAlloc_Type(OctetString):
    """Custom type xdsl2SCStatusSegmentGainAlloc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_Xdsl2SCStatusSegmentGainAlloc_Type.__name__ = "OctetString"
_Xdsl2SCStatusSegmentGainAlloc_Object = MibTableColumn
xdsl2SCStatusSegmentGainAlloc = _Xdsl2SCStatusSegmentGainAlloc_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 2, 5, 1, 8),
    _Xdsl2SCStatusSegmentGainAlloc_Type()
)
xdsl2SCStatusSegmentGainAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2SCStatusSegmentGainAlloc.setStatus("current")
_Xdsl2Inventory_ObjectIdentity = ObjectIdentity
xdsl2Inventory = _Xdsl2Inventory_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 3)
)
_Xdsl2LineInventoryTable_Object = MibTable
xdsl2LineInventoryTable = _Xdsl2LineInventoryTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 3, 1)
)
if mibBuilder.loadTexts:
    xdsl2LineInventoryTable.setStatus("current")
_Xdsl2LineInventoryEntry_Object = MibTableRow
xdsl2LineInventoryEntry = _Xdsl2LineInventoryEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 3, 1, 1)
)
xdsl2LineInventoryEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VDSL2-LINE-MIB", "xdsl2LInvUnit"),
)
if mibBuilder.loadTexts:
    xdsl2LineInventoryEntry.setStatus("current")
_Xdsl2LInvUnit_Type = Xdsl2Unit
_Xdsl2LInvUnit_Object = MibTableColumn
xdsl2LInvUnit = _Xdsl2LInvUnit_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 3, 1, 1, 1),
    _Xdsl2LInvUnit_Type()
)
xdsl2LInvUnit.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xdsl2LInvUnit.setStatus("current")


class _Xdsl2LInvG994VendorId_Type(OctetString):
    """Custom type xdsl2LInvG994VendorId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Xdsl2LInvG994VendorId_Type.__name__ = "OctetString"
_Xdsl2LInvG994VendorId_Object = MibTableColumn
xdsl2LInvG994VendorId = _Xdsl2LInvG994VendorId_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 3, 1, 1, 2),
    _Xdsl2LInvG994VendorId_Type()
)
xdsl2LInvG994VendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LInvG994VendorId.setStatus("current")


class _Xdsl2LInvSystemVendorId_Type(OctetString):
    """Custom type xdsl2LInvSystemVendorId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Xdsl2LInvSystemVendorId_Type.__name__ = "OctetString"
_Xdsl2LInvSystemVendorId_Object = MibTableColumn
xdsl2LInvSystemVendorId = _Xdsl2LInvSystemVendorId_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 3, 1, 1, 3),
    _Xdsl2LInvSystemVendorId_Type()
)
xdsl2LInvSystemVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LInvSystemVendorId.setStatus("current")


class _Xdsl2LInvVersionNumber_Type(OctetString):
    """Custom type xdsl2LInvVersionNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Xdsl2LInvVersionNumber_Type.__name__ = "OctetString"
_Xdsl2LInvVersionNumber_Object = MibTableColumn
xdsl2LInvVersionNumber = _Xdsl2LInvVersionNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 3, 1, 1, 4),
    _Xdsl2LInvVersionNumber_Type()
)
xdsl2LInvVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LInvVersionNumber.setStatus("current")


class _Xdsl2LInvSerialNumber_Type(OctetString):
    """Custom type xdsl2LInvSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Xdsl2LInvSerialNumber_Type.__name__ = "OctetString"
_Xdsl2LInvSerialNumber_Object = MibTableColumn
xdsl2LInvSerialNumber = _Xdsl2LInvSerialNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 3, 1, 1, 5),
    _Xdsl2LInvSerialNumber_Type()
)
xdsl2LInvSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LInvSerialNumber.setStatus("current")


class _Xdsl2LInvSelfTestResult_Type(Unsigned32):
    """Custom type xdsl2LInvSelfTestResult based on Unsigned32"""
    defaultValue = 0


_Xdsl2LInvSelfTestResult_Object = MibTableColumn
xdsl2LInvSelfTestResult = _Xdsl2LInvSelfTestResult_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 3, 1, 1, 6),
    _Xdsl2LInvSelfTestResult_Type()
)
xdsl2LInvSelfTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LInvSelfTestResult.setStatus("current")
_Xdsl2LInvTransmissionCapabilities_Type = Xdsl2TransmissionModeType
_Xdsl2LInvTransmissionCapabilities_Object = MibTableColumn
xdsl2LInvTransmissionCapabilities = _Xdsl2LInvTransmissionCapabilities_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 3, 1, 1, 7),
    _Xdsl2LInvTransmissionCapabilities_Type()
)
xdsl2LInvTransmissionCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2LInvTransmissionCapabilities.setStatus("current")
_Xdsl2PM_ObjectIdentity = ObjectIdentity
xdsl2PM = _Xdsl2PM_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4)
)
_Xdsl2PMLine_ObjectIdentity = ObjectIdentity
xdsl2PMLine = _Xdsl2PMLine_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 1)
)
_Xdsl2PMLineCurrTable_Object = MibTable
xdsl2PMLineCurrTable = _Xdsl2PMLineCurrTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    xdsl2PMLineCurrTable.setStatus("current")
_Xdsl2PMLineCurrEntry_Object = MibTableRow
xdsl2PMLineCurrEntry = _Xdsl2PMLineCurrEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 1, 1, 1)
)
xdsl2PMLineCurrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VDSL2-LINE-MIB", "xdsl2PMLCurrUnit"),
)
if mibBuilder.loadTexts:
    xdsl2PMLineCurrEntry.setStatus("current")
_Xdsl2PMLCurrUnit_Type = Xdsl2Unit
_Xdsl2PMLCurrUnit_Object = MibTableColumn
xdsl2PMLCurrUnit = _Xdsl2PMLCurrUnit_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 1, 1, 1, 1),
    _Xdsl2PMLCurrUnit_Type()
)
xdsl2PMLCurrUnit.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xdsl2PMLCurrUnit.setStatus("current")


class _Xdsl2PMLCurr15MValidIntervals_Type(Unsigned32):
    """Custom type xdsl2PMLCurr15MValidIntervals based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_Xdsl2PMLCurr15MValidIntervals_Type.__name__ = "Unsigned32"
_Xdsl2PMLCurr15MValidIntervals_Object = MibTableColumn
xdsl2PMLCurr15MValidIntervals = _Xdsl2PMLCurr15MValidIntervals_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 1, 1, 1, 2),
    _Xdsl2PMLCurr15MValidIntervals_Type()
)
xdsl2PMLCurr15MValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLCurr15MValidIntervals.setStatus("current")


class _Xdsl2PMLCurr15MInvalidIntervals_Type(Unsigned32):
    """Custom type xdsl2PMLCurr15MInvalidIntervals based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_Xdsl2PMLCurr15MInvalidIntervals_Type.__name__ = "Unsigned32"
_Xdsl2PMLCurr15MInvalidIntervals_Object = MibTableColumn
xdsl2PMLCurr15MInvalidIntervals = _Xdsl2PMLCurr15MInvalidIntervals_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 1, 1, 1, 3),
    _Xdsl2PMLCurr15MInvalidIntervals_Type()
)
xdsl2PMLCurr15MInvalidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLCurr15MInvalidIntervals.setStatus("current")
_Xdsl2PMLCurr15MTimeElapsed_Type = HCPerfTimeElapsed
_Xdsl2PMLCurr15MTimeElapsed_Object = MibTableColumn
xdsl2PMLCurr15MTimeElapsed = _Xdsl2PMLCurr15MTimeElapsed_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 1, 1, 1, 4),
    _Xdsl2PMLCurr15MTimeElapsed_Type()
)
xdsl2PMLCurr15MTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLCurr15MTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLCurr15MTimeElapsed.setUnits("seconds")
_Xdsl2PMLCurr15MFecs_Type = Counter32
_Xdsl2PMLCurr15MFecs_Object = MibTableColumn
xdsl2PMLCurr15MFecs = _Xdsl2PMLCurr15MFecs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 1, 1, 1, 5),
    _Xdsl2PMLCurr15MFecs_Type()
)
xdsl2PMLCurr15MFecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLCurr15MFecs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLCurr15MFecs.setUnits("seconds")
_Xdsl2PMLCurr15MEs_Type = Counter32
_Xdsl2PMLCurr15MEs_Object = MibTableColumn
xdsl2PMLCurr15MEs = _Xdsl2PMLCurr15MEs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 1, 1, 1, 6),
    _Xdsl2PMLCurr15MEs_Type()
)
xdsl2PMLCurr15MEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLCurr15MEs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLCurr15MEs.setUnits("seconds")
_Xdsl2PMLCurr15MSes_Type = Counter32
_Xdsl2PMLCurr15MSes_Object = MibTableColumn
xdsl2PMLCurr15MSes = _Xdsl2PMLCurr15MSes_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 1, 1, 1, 7),
    _Xdsl2PMLCurr15MSes_Type()
)
xdsl2PMLCurr15MSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLCurr15MSes.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLCurr15MSes.setUnits("seconds")
_Xdsl2PMLCurr15MLoss_Type = Counter32
_Xdsl2PMLCurr15MLoss_Object = MibTableColumn
xdsl2PMLCurr15MLoss = _Xdsl2PMLCurr15MLoss_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 1, 1, 1, 8),
    _Xdsl2PMLCurr15MLoss_Type()
)
xdsl2PMLCurr15MLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLCurr15MLoss.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLCurr15MLoss.setUnits("seconds")
_Xdsl2PMLCurr15MUas_Type = Counter32
_Xdsl2PMLCurr15MUas_Object = MibTableColumn
xdsl2PMLCurr15MUas = _Xdsl2PMLCurr15MUas_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 1, 1, 1, 9),
    _Xdsl2PMLCurr15MUas_Type()
)
xdsl2PMLCurr15MUas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLCurr15MUas.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLCurr15MUas.setUnits("seconds")


class _Xdsl2PMLCurr1DayValidIntervals_Type(Unsigned32):
    """Custom type xdsl2PMLCurr1DayValidIntervals based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_Xdsl2PMLCurr1DayValidIntervals_Type.__name__ = "Unsigned32"
_Xdsl2PMLCurr1DayValidIntervals_Object = MibTableColumn
xdsl2PMLCurr1DayValidIntervals = _Xdsl2PMLCurr1DayValidIntervals_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 1, 1, 1, 10),
    _Xdsl2PMLCurr1DayValidIntervals_Type()
)
xdsl2PMLCurr1DayValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLCurr1DayValidIntervals.setStatus("current")


class _Xdsl2PMLCurr1DayInvalidIntervals_Type(Unsigned32):
    """Custom type xdsl2PMLCurr1DayInvalidIntervals based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_Xdsl2PMLCurr1DayInvalidIntervals_Type.__name__ = "Unsigned32"
_Xdsl2PMLCurr1DayInvalidIntervals_Object = MibTableColumn
xdsl2PMLCurr1DayInvalidIntervals = _Xdsl2PMLCurr1DayInvalidIntervals_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 1, 1, 1, 11),
    _Xdsl2PMLCurr1DayInvalidIntervals_Type()
)
xdsl2PMLCurr1DayInvalidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLCurr1DayInvalidIntervals.setStatus("current")
_Xdsl2PMLCurr1DayTimeElapsed_Type = HCPerfTimeElapsed
_Xdsl2PMLCurr1DayTimeElapsed_Object = MibTableColumn
xdsl2PMLCurr1DayTimeElapsed = _Xdsl2PMLCurr1DayTimeElapsed_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 1, 1, 1, 12),
    _Xdsl2PMLCurr1DayTimeElapsed_Type()
)
xdsl2PMLCurr1DayTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLCurr1DayTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLCurr1DayTimeElapsed.setUnits("seconds")
_Xdsl2PMLCurr1DayFecs_Type = Counter32
_Xdsl2PMLCurr1DayFecs_Object = MibTableColumn
xdsl2PMLCurr1DayFecs = _Xdsl2PMLCurr1DayFecs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 1, 1, 1, 13),
    _Xdsl2PMLCurr1DayFecs_Type()
)
xdsl2PMLCurr1DayFecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLCurr1DayFecs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLCurr1DayFecs.setUnits("seconds")
_Xdsl2PMLCurr1DayEs_Type = Counter32
_Xdsl2PMLCurr1DayEs_Object = MibTableColumn
xdsl2PMLCurr1DayEs = _Xdsl2PMLCurr1DayEs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 1, 1, 1, 14),
    _Xdsl2PMLCurr1DayEs_Type()
)
xdsl2PMLCurr1DayEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLCurr1DayEs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLCurr1DayEs.setUnits("seconds")
_Xdsl2PMLCurr1DaySes_Type = Counter32
_Xdsl2PMLCurr1DaySes_Object = MibTableColumn
xdsl2PMLCurr1DaySes = _Xdsl2PMLCurr1DaySes_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 1, 1, 1, 15),
    _Xdsl2PMLCurr1DaySes_Type()
)
xdsl2PMLCurr1DaySes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLCurr1DaySes.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLCurr1DaySes.setUnits("seconds")
_Xdsl2PMLCurr1DayLoss_Type = Counter32
_Xdsl2PMLCurr1DayLoss_Object = MibTableColumn
xdsl2PMLCurr1DayLoss = _Xdsl2PMLCurr1DayLoss_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 1, 1, 1, 16),
    _Xdsl2PMLCurr1DayLoss_Type()
)
xdsl2PMLCurr1DayLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLCurr1DayLoss.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLCurr1DayLoss.setUnits("seconds")
_Xdsl2PMLCurr1DayUas_Type = Counter32
_Xdsl2PMLCurr1DayUas_Object = MibTableColumn
xdsl2PMLCurr1DayUas = _Xdsl2PMLCurr1DayUas_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 1, 1, 1, 17),
    _Xdsl2PMLCurr1DayUas_Type()
)
xdsl2PMLCurr1DayUas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLCurr1DayUas.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLCurr1DayUas.setUnits("seconds")
_Xdsl2PMLineInitCurrTable_Object = MibTable
xdsl2PMLineInitCurrTable = _Xdsl2PMLineInitCurrTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 1, 2)
)
if mibBuilder.loadTexts:
    xdsl2PMLineInitCurrTable.setStatus("current")
_Xdsl2PMLineInitCurrEntry_Object = MibTableRow
xdsl2PMLineInitCurrEntry = _Xdsl2PMLineInitCurrEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 1, 2, 1)
)
xdsl2PMLineInitCurrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    xdsl2PMLineInitCurrEntry.setStatus("current")


class _Xdsl2PMLInitCurr15MValidIntervals_Type(Unsigned32):
    """Custom type xdsl2PMLInitCurr15MValidIntervals based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_Xdsl2PMLInitCurr15MValidIntervals_Type.__name__ = "Unsigned32"
_Xdsl2PMLInitCurr15MValidIntervals_Object = MibTableColumn
xdsl2PMLInitCurr15MValidIntervals = _Xdsl2PMLInitCurr15MValidIntervals_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 1, 2, 1, 1),
    _Xdsl2PMLInitCurr15MValidIntervals_Type()
)
xdsl2PMLInitCurr15MValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLInitCurr15MValidIntervals.setStatus("current")


class _Xdsl2PMLInitCurr15MInvalidIntervals_Type(Unsigned32):
    """Custom type xdsl2PMLInitCurr15MInvalidIntervals based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_Xdsl2PMLInitCurr15MInvalidIntervals_Type.__name__ = "Unsigned32"
_Xdsl2PMLInitCurr15MInvalidIntervals_Object = MibTableColumn
xdsl2PMLInitCurr15MInvalidIntervals = _Xdsl2PMLInitCurr15MInvalidIntervals_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 1, 2, 1, 2),
    _Xdsl2PMLInitCurr15MInvalidIntervals_Type()
)
xdsl2PMLInitCurr15MInvalidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLInitCurr15MInvalidIntervals.setStatus("current")
_Xdsl2PMLInitCurr15MTimeElapsed_Type = Unsigned32
_Xdsl2PMLInitCurr15MTimeElapsed_Object = MibTableColumn
xdsl2PMLInitCurr15MTimeElapsed = _Xdsl2PMLInitCurr15MTimeElapsed_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 1, 2, 1, 3),
    _Xdsl2PMLInitCurr15MTimeElapsed_Type()
)
xdsl2PMLInitCurr15MTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLInitCurr15MTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLInitCurr15MTimeElapsed.setUnits("seconds")
_Xdsl2PMLInitCurr15MFullInits_Type = Unsigned32
_Xdsl2PMLInitCurr15MFullInits_Object = MibTableColumn
xdsl2PMLInitCurr15MFullInits = _Xdsl2PMLInitCurr15MFullInits_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 1, 2, 1, 4),
    _Xdsl2PMLInitCurr15MFullInits_Type()
)
xdsl2PMLInitCurr15MFullInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLInitCurr15MFullInits.setStatus("current")
_Xdsl2PMLInitCurr15MFailedFullInits_Type = Unsigned32
_Xdsl2PMLInitCurr15MFailedFullInits_Object = MibTableColumn
xdsl2PMLInitCurr15MFailedFullInits = _Xdsl2PMLInitCurr15MFailedFullInits_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 1, 2, 1, 5),
    _Xdsl2PMLInitCurr15MFailedFullInits_Type()
)
xdsl2PMLInitCurr15MFailedFullInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLInitCurr15MFailedFullInits.setStatus("current")
_Xdsl2PMLInitCurr15MShortInits_Type = Unsigned32
_Xdsl2PMLInitCurr15MShortInits_Object = MibTableColumn
xdsl2PMLInitCurr15MShortInits = _Xdsl2PMLInitCurr15MShortInits_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 1, 2, 1, 6),
    _Xdsl2PMLInitCurr15MShortInits_Type()
)
xdsl2PMLInitCurr15MShortInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLInitCurr15MShortInits.setStatus("current")
_Xdsl2PMLInitCurr15MFailedShortInits_Type = Unsigned32
_Xdsl2PMLInitCurr15MFailedShortInits_Object = MibTableColumn
xdsl2PMLInitCurr15MFailedShortInits = _Xdsl2PMLInitCurr15MFailedShortInits_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 1, 2, 1, 7),
    _Xdsl2PMLInitCurr15MFailedShortInits_Type()
)
xdsl2PMLInitCurr15MFailedShortInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLInitCurr15MFailedShortInits.setStatus("current")


class _Xdsl2PMLInitCurr1DayValidIntervals_Type(Unsigned32):
    """Custom type xdsl2PMLInitCurr1DayValidIntervals based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_Xdsl2PMLInitCurr1DayValidIntervals_Type.__name__ = "Unsigned32"
_Xdsl2PMLInitCurr1DayValidIntervals_Object = MibTableColumn
xdsl2PMLInitCurr1DayValidIntervals = _Xdsl2PMLInitCurr1DayValidIntervals_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 1, 2, 1, 8),
    _Xdsl2PMLInitCurr1DayValidIntervals_Type()
)
xdsl2PMLInitCurr1DayValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLInitCurr1DayValidIntervals.setStatus("current")


class _Xdsl2PMLInitCurr1DayInvalidIntervals_Type(Unsigned32):
    """Custom type xdsl2PMLInitCurr1DayInvalidIntervals based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_Xdsl2PMLInitCurr1DayInvalidIntervals_Type.__name__ = "Unsigned32"
_Xdsl2PMLInitCurr1DayInvalidIntervals_Object = MibTableColumn
xdsl2PMLInitCurr1DayInvalidIntervals = _Xdsl2PMLInitCurr1DayInvalidIntervals_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 1, 2, 1, 9),
    _Xdsl2PMLInitCurr1DayInvalidIntervals_Type()
)
xdsl2PMLInitCurr1DayInvalidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLInitCurr1DayInvalidIntervals.setStatus("current")
_Xdsl2PMLInitCurr1DayTimeElapsed_Type = Unsigned32
_Xdsl2PMLInitCurr1DayTimeElapsed_Object = MibTableColumn
xdsl2PMLInitCurr1DayTimeElapsed = _Xdsl2PMLInitCurr1DayTimeElapsed_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 1, 2, 1, 10),
    _Xdsl2PMLInitCurr1DayTimeElapsed_Type()
)
xdsl2PMLInitCurr1DayTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLInitCurr1DayTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLInitCurr1DayTimeElapsed.setUnits("seconds")
_Xdsl2PMLInitCurr1DayFullInits_Type = Unsigned32
_Xdsl2PMLInitCurr1DayFullInits_Object = MibTableColumn
xdsl2PMLInitCurr1DayFullInits = _Xdsl2PMLInitCurr1DayFullInits_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 1, 2, 1, 11),
    _Xdsl2PMLInitCurr1DayFullInits_Type()
)
xdsl2PMLInitCurr1DayFullInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLInitCurr1DayFullInits.setStatus("current")
_Xdsl2PMLInitCurr1DayFailedFullInits_Type = Unsigned32
_Xdsl2PMLInitCurr1DayFailedFullInits_Object = MibTableColumn
xdsl2PMLInitCurr1DayFailedFullInits = _Xdsl2PMLInitCurr1DayFailedFullInits_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 1, 2, 1, 12),
    _Xdsl2PMLInitCurr1DayFailedFullInits_Type()
)
xdsl2PMLInitCurr1DayFailedFullInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLInitCurr1DayFailedFullInits.setStatus("current")
_Xdsl2PMLInitCurr1DayShortInits_Type = Unsigned32
_Xdsl2PMLInitCurr1DayShortInits_Object = MibTableColumn
xdsl2PMLInitCurr1DayShortInits = _Xdsl2PMLInitCurr1DayShortInits_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 1, 2, 1, 13),
    _Xdsl2PMLInitCurr1DayShortInits_Type()
)
xdsl2PMLInitCurr1DayShortInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLInitCurr1DayShortInits.setStatus("current")
_Xdsl2PMLInitCurr1DayFailedShortInits_Type = Unsigned32
_Xdsl2PMLInitCurr1DayFailedShortInits_Object = MibTableColumn
xdsl2PMLInitCurr1DayFailedShortInits = _Xdsl2PMLInitCurr1DayFailedShortInits_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 1, 2, 1, 14),
    _Xdsl2PMLInitCurr1DayFailedShortInits_Type()
)
xdsl2PMLInitCurr1DayFailedShortInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLInitCurr1DayFailedShortInits.setStatus("current")
_Xdsl2PMLineHist15MinTable_Object = MibTable
xdsl2PMLineHist15MinTable = _Xdsl2PMLineHist15MinTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 1, 3)
)
if mibBuilder.loadTexts:
    xdsl2PMLineHist15MinTable.setStatus("current")
_Xdsl2PMLineHist15MinEntry_Object = MibTableRow
xdsl2PMLineHist15MinEntry = _Xdsl2PMLineHist15MinEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 1, 3, 1)
)
xdsl2PMLineHist15MinEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VDSL2-LINE-MIB", "xdsl2PMLHist15MUnit"),
    (0, "VDSL2-LINE-MIB", "xdsl2PMLHist15MInterval"),
)
if mibBuilder.loadTexts:
    xdsl2PMLineHist15MinEntry.setStatus("current")
_Xdsl2PMLHist15MUnit_Type = Xdsl2Unit
_Xdsl2PMLHist15MUnit_Object = MibTableColumn
xdsl2PMLHist15MUnit = _Xdsl2PMLHist15MUnit_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 1, 3, 1, 1),
    _Xdsl2PMLHist15MUnit_Type()
)
xdsl2PMLHist15MUnit.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xdsl2PMLHist15MUnit.setStatus("current")


class _Xdsl2PMLHist15MInterval_Type(Unsigned32):
    """Custom type xdsl2PMLHist15MInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_Xdsl2PMLHist15MInterval_Type.__name__ = "Unsigned32"
_Xdsl2PMLHist15MInterval_Object = MibTableColumn
xdsl2PMLHist15MInterval = _Xdsl2PMLHist15MInterval_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 1, 3, 1, 2),
    _Xdsl2PMLHist15MInterval_Type()
)
xdsl2PMLHist15MInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xdsl2PMLHist15MInterval.setStatus("current")
_Xdsl2PMLHist15MMonitoredTime_Type = Unsigned32
_Xdsl2PMLHist15MMonitoredTime_Object = MibTableColumn
xdsl2PMLHist15MMonitoredTime = _Xdsl2PMLHist15MMonitoredTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 1, 3, 1, 3),
    _Xdsl2PMLHist15MMonitoredTime_Type()
)
xdsl2PMLHist15MMonitoredTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLHist15MMonitoredTime.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLHist15MMonitoredTime.setUnits("seconds")
_Xdsl2PMLHist15MFecs_Type = Counter32
_Xdsl2PMLHist15MFecs_Object = MibTableColumn
xdsl2PMLHist15MFecs = _Xdsl2PMLHist15MFecs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 1, 3, 1, 4),
    _Xdsl2PMLHist15MFecs_Type()
)
xdsl2PMLHist15MFecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLHist15MFecs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLHist15MFecs.setUnits("seconds")
_Xdsl2PMLHist15MEs_Type = Counter32
_Xdsl2PMLHist15MEs_Object = MibTableColumn
xdsl2PMLHist15MEs = _Xdsl2PMLHist15MEs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 1, 3, 1, 5),
    _Xdsl2PMLHist15MEs_Type()
)
xdsl2PMLHist15MEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLHist15MEs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLHist15MEs.setUnits("seconds")
_Xdsl2PMLHist15MSes_Type = Counter32
_Xdsl2PMLHist15MSes_Object = MibTableColumn
xdsl2PMLHist15MSes = _Xdsl2PMLHist15MSes_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 1, 3, 1, 6),
    _Xdsl2PMLHist15MSes_Type()
)
xdsl2PMLHist15MSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLHist15MSes.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLHist15MSes.setUnits("seconds")
_Xdsl2PMLHist15MLoss_Type = Counter32
_Xdsl2PMLHist15MLoss_Object = MibTableColumn
xdsl2PMLHist15MLoss = _Xdsl2PMLHist15MLoss_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 1, 3, 1, 7),
    _Xdsl2PMLHist15MLoss_Type()
)
xdsl2PMLHist15MLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLHist15MLoss.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLHist15MLoss.setUnits("seconds")
_Xdsl2PMLHist15MUas_Type = Counter32
_Xdsl2PMLHist15MUas_Object = MibTableColumn
xdsl2PMLHist15MUas = _Xdsl2PMLHist15MUas_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 1, 3, 1, 8),
    _Xdsl2PMLHist15MUas_Type()
)
xdsl2PMLHist15MUas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLHist15MUas.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLHist15MUas.setUnits("seconds")
_Xdsl2PMLHist15MValidInterval_Type = TruthValue
_Xdsl2PMLHist15MValidInterval_Object = MibTableColumn
xdsl2PMLHist15MValidInterval = _Xdsl2PMLHist15MValidInterval_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 1, 3, 1, 9),
    _Xdsl2PMLHist15MValidInterval_Type()
)
xdsl2PMLHist15MValidInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLHist15MValidInterval.setStatus("current")
_Xdsl2PMLineHist1DayTable_Object = MibTable
xdsl2PMLineHist1DayTable = _Xdsl2PMLineHist1DayTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 1, 4)
)
if mibBuilder.loadTexts:
    xdsl2PMLineHist1DayTable.setStatus("current")
_Xdsl2PMLineHist1DayEntry_Object = MibTableRow
xdsl2PMLineHist1DayEntry = _Xdsl2PMLineHist1DayEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 1, 4, 1)
)
xdsl2PMLineHist1DayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VDSL2-LINE-MIB", "xdsl2PMLHist1DUnit"),
    (0, "VDSL2-LINE-MIB", "xdsl2PMLHist1DInterval"),
)
if mibBuilder.loadTexts:
    xdsl2PMLineHist1DayEntry.setStatus("current")
_Xdsl2PMLHist1DUnit_Type = Xdsl2Unit
_Xdsl2PMLHist1DUnit_Object = MibTableColumn
xdsl2PMLHist1DUnit = _Xdsl2PMLHist1DUnit_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 1, 4, 1, 1),
    _Xdsl2PMLHist1DUnit_Type()
)
xdsl2PMLHist1DUnit.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xdsl2PMLHist1DUnit.setStatus("current")


class _Xdsl2PMLHist1DInterval_Type(Unsigned32):
    """Custom type xdsl2PMLHist1DInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_Xdsl2PMLHist1DInterval_Type.__name__ = "Unsigned32"
_Xdsl2PMLHist1DInterval_Object = MibTableColumn
xdsl2PMLHist1DInterval = _Xdsl2PMLHist1DInterval_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 1, 4, 1, 2),
    _Xdsl2PMLHist1DInterval_Type()
)
xdsl2PMLHist1DInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xdsl2PMLHist1DInterval.setStatus("current")
_Xdsl2PMLHist1DMonitoredTime_Type = Unsigned32
_Xdsl2PMLHist1DMonitoredTime_Object = MibTableColumn
xdsl2PMLHist1DMonitoredTime = _Xdsl2PMLHist1DMonitoredTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 1, 4, 1, 3),
    _Xdsl2PMLHist1DMonitoredTime_Type()
)
xdsl2PMLHist1DMonitoredTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLHist1DMonitoredTime.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLHist1DMonitoredTime.setUnits("seconds")
_Xdsl2PMLHist1DFecs_Type = Counter32
_Xdsl2PMLHist1DFecs_Object = MibTableColumn
xdsl2PMLHist1DFecs = _Xdsl2PMLHist1DFecs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 1, 4, 1, 4),
    _Xdsl2PMLHist1DFecs_Type()
)
xdsl2PMLHist1DFecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLHist1DFecs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLHist1DFecs.setUnits("seconds")
_Xdsl2PMLHist1DEs_Type = Counter32
_Xdsl2PMLHist1DEs_Object = MibTableColumn
xdsl2PMLHist1DEs = _Xdsl2PMLHist1DEs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 1, 4, 1, 5),
    _Xdsl2PMLHist1DEs_Type()
)
xdsl2PMLHist1DEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLHist1DEs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLHist1DEs.setUnits("seconds")
_Xdsl2PMLHist1DSes_Type = Counter32
_Xdsl2PMLHist1DSes_Object = MibTableColumn
xdsl2PMLHist1DSes = _Xdsl2PMLHist1DSes_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 1, 4, 1, 6),
    _Xdsl2PMLHist1DSes_Type()
)
xdsl2PMLHist1DSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLHist1DSes.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLHist1DSes.setUnits("seconds")
_Xdsl2PMLHist1DLoss_Type = Counter32
_Xdsl2PMLHist1DLoss_Object = MibTableColumn
xdsl2PMLHist1DLoss = _Xdsl2PMLHist1DLoss_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 1, 4, 1, 7),
    _Xdsl2PMLHist1DLoss_Type()
)
xdsl2PMLHist1DLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLHist1DLoss.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLHist1DLoss.setUnits("seconds")
_Xdsl2PMLHist1DUas_Type = Counter32
_Xdsl2PMLHist1DUas_Object = MibTableColumn
xdsl2PMLHist1DUas = _Xdsl2PMLHist1DUas_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 1, 4, 1, 8),
    _Xdsl2PMLHist1DUas_Type()
)
xdsl2PMLHist1DUas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLHist1DUas.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLHist1DUas.setUnits("seconds")
_Xdsl2PMLHist1DValidInterval_Type = TruthValue
_Xdsl2PMLHist1DValidInterval_Object = MibTableColumn
xdsl2PMLHist1DValidInterval = _Xdsl2PMLHist1DValidInterval_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 1, 4, 1, 9),
    _Xdsl2PMLHist1DValidInterval_Type()
)
xdsl2PMLHist1DValidInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLHist1DValidInterval.setStatus("current")
_Xdsl2PMLineInitHist15MinTable_Object = MibTable
xdsl2PMLineInitHist15MinTable = _Xdsl2PMLineInitHist15MinTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 1, 5)
)
if mibBuilder.loadTexts:
    xdsl2PMLineInitHist15MinTable.setStatus("current")
_Xdsl2PMLineInitHist15MinEntry_Object = MibTableRow
xdsl2PMLineInitHist15MinEntry = _Xdsl2PMLineInitHist15MinEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 1, 5, 1)
)
xdsl2PMLineInitHist15MinEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VDSL2-LINE-MIB", "xdsl2PMLInitHist15MInterval"),
)
if mibBuilder.loadTexts:
    xdsl2PMLineInitHist15MinEntry.setStatus("current")


class _Xdsl2PMLInitHist15MInterval_Type(Unsigned32):
    """Custom type xdsl2PMLInitHist15MInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_Xdsl2PMLInitHist15MInterval_Type.__name__ = "Unsigned32"
_Xdsl2PMLInitHist15MInterval_Object = MibTableColumn
xdsl2PMLInitHist15MInterval = _Xdsl2PMLInitHist15MInterval_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 1, 5, 1, 1),
    _Xdsl2PMLInitHist15MInterval_Type()
)
xdsl2PMLInitHist15MInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xdsl2PMLInitHist15MInterval.setStatus("current")
_Xdsl2PMLInitHist15MMonitoredTime_Type = Unsigned32
_Xdsl2PMLInitHist15MMonitoredTime_Object = MibTableColumn
xdsl2PMLInitHist15MMonitoredTime = _Xdsl2PMLInitHist15MMonitoredTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 1, 5, 1, 2),
    _Xdsl2PMLInitHist15MMonitoredTime_Type()
)
xdsl2PMLInitHist15MMonitoredTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLInitHist15MMonitoredTime.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLInitHist15MMonitoredTime.setUnits("seconds")
_Xdsl2PMLInitHist15MFullInits_Type = Unsigned32
_Xdsl2PMLInitHist15MFullInits_Object = MibTableColumn
xdsl2PMLInitHist15MFullInits = _Xdsl2PMLInitHist15MFullInits_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 1, 5, 1, 3),
    _Xdsl2PMLInitHist15MFullInits_Type()
)
xdsl2PMLInitHist15MFullInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLInitHist15MFullInits.setStatus("current")
_Xdsl2PMLInitHist15MFailedFullInits_Type = Unsigned32
_Xdsl2PMLInitHist15MFailedFullInits_Object = MibTableColumn
xdsl2PMLInitHist15MFailedFullInits = _Xdsl2PMLInitHist15MFailedFullInits_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 1, 5, 1, 4),
    _Xdsl2PMLInitHist15MFailedFullInits_Type()
)
xdsl2PMLInitHist15MFailedFullInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLInitHist15MFailedFullInits.setStatus("current")
_Xdsl2PMLInitHist15MShortInits_Type = Unsigned32
_Xdsl2PMLInitHist15MShortInits_Object = MibTableColumn
xdsl2PMLInitHist15MShortInits = _Xdsl2PMLInitHist15MShortInits_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 1, 5, 1, 5),
    _Xdsl2PMLInitHist15MShortInits_Type()
)
xdsl2PMLInitHist15MShortInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLInitHist15MShortInits.setStatus("current")
_Xdsl2PMLInitHist15MFailedShortInits_Type = Unsigned32
_Xdsl2PMLInitHist15MFailedShortInits_Object = MibTableColumn
xdsl2PMLInitHist15MFailedShortInits = _Xdsl2PMLInitHist15MFailedShortInits_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 1, 5, 1, 6),
    _Xdsl2PMLInitHist15MFailedShortInits_Type()
)
xdsl2PMLInitHist15MFailedShortInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLInitHist15MFailedShortInits.setStatus("current")
_Xdsl2PMLInitHist15MValidInterval_Type = TruthValue
_Xdsl2PMLInitHist15MValidInterval_Object = MibTableColumn
xdsl2PMLInitHist15MValidInterval = _Xdsl2PMLInitHist15MValidInterval_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 1, 5, 1, 7),
    _Xdsl2PMLInitHist15MValidInterval_Type()
)
xdsl2PMLInitHist15MValidInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLInitHist15MValidInterval.setStatus("current")
_Xdsl2PMLineInitHist1DayTable_Object = MibTable
xdsl2PMLineInitHist1DayTable = _Xdsl2PMLineInitHist1DayTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 1, 6)
)
if mibBuilder.loadTexts:
    xdsl2PMLineInitHist1DayTable.setStatus("current")
_Xdsl2PMLineInitHist1DayEntry_Object = MibTableRow
xdsl2PMLineInitHist1DayEntry = _Xdsl2PMLineInitHist1DayEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 1, 6, 1)
)
xdsl2PMLineInitHist1DayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VDSL2-LINE-MIB", "xdsl2PMLInitHist1DInterval"),
)
if mibBuilder.loadTexts:
    xdsl2PMLineInitHist1DayEntry.setStatus("current")


class _Xdsl2PMLInitHist1DInterval_Type(Unsigned32):
    """Custom type xdsl2PMLInitHist1DInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_Xdsl2PMLInitHist1DInterval_Type.__name__ = "Unsigned32"
_Xdsl2PMLInitHist1DInterval_Object = MibTableColumn
xdsl2PMLInitHist1DInterval = _Xdsl2PMLInitHist1DInterval_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 1, 6, 1, 1),
    _Xdsl2PMLInitHist1DInterval_Type()
)
xdsl2PMLInitHist1DInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xdsl2PMLInitHist1DInterval.setStatus("current")
_Xdsl2PMLInitHist1DMonitoredTime_Type = Unsigned32
_Xdsl2PMLInitHist1DMonitoredTime_Object = MibTableColumn
xdsl2PMLInitHist1DMonitoredTime = _Xdsl2PMLInitHist1DMonitoredTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 1, 6, 1, 2),
    _Xdsl2PMLInitHist1DMonitoredTime_Type()
)
xdsl2PMLInitHist1DMonitoredTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLInitHist1DMonitoredTime.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMLInitHist1DMonitoredTime.setUnits("seconds")
_Xdsl2PMLInitHist1DFullInits_Type = Unsigned32
_Xdsl2PMLInitHist1DFullInits_Object = MibTableColumn
xdsl2PMLInitHist1DFullInits = _Xdsl2PMLInitHist1DFullInits_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 1, 6, 1, 3),
    _Xdsl2PMLInitHist1DFullInits_Type()
)
xdsl2PMLInitHist1DFullInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLInitHist1DFullInits.setStatus("current")
_Xdsl2PMLInitHist1DFailedFullInits_Type = Unsigned32
_Xdsl2PMLInitHist1DFailedFullInits_Object = MibTableColumn
xdsl2PMLInitHist1DFailedFullInits = _Xdsl2PMLInitHist1DFailedFullInits_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 1, 6, 1, 4),
    _Xdsl2PMLInitHist1DFailedFullInits_Type()
)
xdsl2PMLInitHist1DFailedFullInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLInitHist1DFailedFullInits.setStatus("current")
_Xdsl2PMLInitHist1DShortInits_Type = Unsigned32
_Xdsl2PMLInitHist1DShortInits_Object = MibTableColumn
xdsl2PMLInitHist1DShortInits = _Xdsl2PMLInitHist1DShortInits_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 1, 6, 1, 5),
    _Xdsl2PMLInitHist1DShortInits_Type()
)
xdsl2PMLInitHist1DShortInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLInitHist1DShortInits.setStatus("current")
_Xdsl2PMLInitHist1DFailedShortInits_Type = Unsigned32
_Xdsl2PMLInitHist1DFailedShortInits_Object = MibTableColumn
xdsl2PMLInitHist1DFailedShortInits = _Xdsl2PMLInitHist1DFailedShortInits_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 1, 6, 1, 6),
    _Xdsl2PMLInitHist1DFailedShortInits_Type()
)
xdsl2PMLInitHist1DFailedShortInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLInitHist1DFailedShortInits.setStatus("current")
_Xdsl2PMLInitHist1DValidInterval_Type = TruthValue
_Xdsl2PMLInitHist1DValidInterval_Object = MibTableColumn
xdsl2PMLInitHist1DValidInterval = _Xdsl2PMLInitHist1DValidInterval_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 1, 6, 1, 7),
    _Xdsl2PMLInitHist1DValidInterval_Type()
)
xdsl2PMLInitHist1DValidInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMLInitHist1DValidInterval.setStatus("current")
_Xdsl2PMChannel_ObjectIdentity = ObjectIdentity
xdsl2PMChannel = _Xdsl2PMChannel_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 2)
)
_Xdsl2PMChCurrTable_Object = MibTable
xdsl2PMChCurrTable = _Xdsl2PMChCurrTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    xdsl2PMChCurrTable.setStatus("current")
_Xdsl2PMChCurrEntry_Object = MibTableRow
xdsl2PMChCurrEntry = _Xdsl2PMChCurrEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 2, 1, 1)
)
xdsl2PMChCurrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VDSL2-LINE-MIB", "xdsl2PMChCurrUnit"),
)
if mibBuilder.loadTexts:
    xdsl2PMChCurrEntry.setStatus("current")
_Xdsl2PMChCurrUnit_Type = Xdsl2Unit
_Xdsl2PMChCurrUnit_Object = MibTableColumn
xdsl2PMChCurrUnit = _Xdsl2PMChCurrUnit_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 2, 1, 1, 1),
    _Xdsl2PMChCurrUnit_Type()
)
xdsl2PMChCurrUnit.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xdsl2PMChCurrUnit.setStatus("current")


class _Xdsl2PMChCurr15MValidIntervals_Type(Unsigned32):
    """Custom type xdsl2PMChCurr15MValidIntervals based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_Xdsl2PMChCurr15MValidIntervals_Type.__name__ = "Unsigned32"
_Xdsl2PMChCurr15MValidIntervals_Object = MibTableColumn
xdsl2PMChCurr15MValidIntervals = _Xdsl2PMChCurr15MValidIntervals_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 2, 1, 1, 2),
    _Xdsl2PMChCurr15MValidIntervals_Type()
)
xdsl2PMChCurr15MValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMChCurr15MValidIntervals.setStatus("current")


class _Xdsl2PMChCurr15MInvalidIntervals_Type(Unsigned32):
    """Custom type xdsl2PMChCurr15MInvalidIntervals based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_Xdsl2PMChCurr15MInvalidIntervals_Type.__name__ = "Unsigned32"
_Xdsl2PMChCurr15MInvalidIntervals_Object = MibTableColumn
xdsl2PMChCurr15MInvalidIntervals = _Xdsl2PMChCurr15MInvalidIntervals_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 2, 1, 1, 3),
    _Xdsl2PMChCurr15MInvalidIntervals_Type()
)
xdsl2PMChCurr15MInvalidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMChCurr15MInvalidIntervals.setStatus("current")
_Xdsl2PMChCurr15MTimeElapsed_Type = HCPerfTimeElapsed
_Xdsl2PMChCurr15MTimeElapsed_Object = MibTableColumn
xdsl2PMChCurr15MTimeElapsed = _Xdsl2PMChCurr15MTimeElapsed_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 2, 1, 1, 4),
    _Xdsl2PMChCurr15MTimeElapsed_Type()
)
xdsl2PMChCurr15MTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMChCurr15MTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMChCurr15MTimeElapsed.setUnits("seconds")
_Xdsl2PMChCurr15MCodingViolations_Type = Unsigned32
_Xdsl2PMChCurr15MCodingViolations_Object = MibTableColumn
xdsl2PMChCurr15MCodingViolations = _Xdsl2PMChCurr15MCodingViolations_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 2, 1, 1, 5),
    _Xdsl2PMChCurr15MCodingViolations_Type()
)
xdsl2PMChCurr15MCodingViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMChCurr15MCodingViolations.setStatus("current")
_Xdsl2PMChCurr15MCorrectedBlocks_Type = Unsigned32
_Xdsl2PMChCurr15MCorrectedBlocks_Object = MibTableColumn
xdsl2PMChCurr15MCorrectedBlocks = _Xdsl2PMChCurr15MCorrectedBlocks_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 2, 1, 1, 6),
    _Xdsl2PMChCurr15MCorrectedBlocks_Type()
)
xdsl2PMChCurr15MCorrectedBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMChCurr15MCorrectedBlocks.setStatus("current")


class _Xdsl2PMChCurr1DayValidIntervals_Type(Unsigned32):
    """Custom type xdsl2PMChCurr1DayValidIntervals based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_Xdsl2PMChCurr1DayValidIntervals_Type.__name__ = "Unsigned32"
_Xdsl2PMChCurr1DayValidIntervals_Object = MibTableColumn
xdsl2PMChCurr1DayValidIntervals = _Xdsl2PMChCurr1DayValidIntervals_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 2, 1, 1, 7),
    _Xdsl2PMChCurr1DayValidIntervals_Type()
)
xdsl2PMChCurr1DayValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMChCurr1DayValidIntervals.setStatus("current")


class _Xdsl2PMChCurr1DayInvalidIntervals_Type(Unsigned32):
    """Custom type xdsl2PMChCurr1DayInvalidIntervals based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_Xdsl2PMChCurr1DayInvalidIntervals_Type.__name__ = "Unsigned32"
_Xdsl2PMChCurr1DayInvalidIntervals_Object = MibTableColumn
xdsl2PMChCurr1DayInvalidIntervals = _Xdsl2PMChCurr1DayInvalidIntervals_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 2, 1, 1, 8),
    _Xdsl2PMChCurr1DayInvalidIntervals_Type()
)
xdsl2PMChCurr1DayInvalidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMChCurr1DayInvalidIntervals.setStatus("current")
_Xdsl2PMChCurr1DayTimeElapsed_Type = HCPerfTimeElapsed
_Xdsl2PMChCurr1DayTimeElapsed_Object = MibTableColumn
xdsl2PMChCurr1DayTimeElapsed = _Xdsl2PMChCurr1DayTimeElapsed_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 2, 1, 1, 9),
    _Xdsl2PMChCurr1DayTimeElapsed_Type()
)
xdsl2PMChCurr1DayTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMChCurr1DayTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMChCurr1DayTimeElapsed.setUnits("seconds")
_Xdsl2PMChCurr1DayCodingViolations_Type = Unsigned32
_Xdsl2PMChCurr1DayCodingViolations_Object = MibTableColumn
xdsl2PMChCurr1DayCodingViolations = _Xdsl2PMChCurr1DayCodingViolations_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 2, 1, 1, 10),
    _Xdsl2PMChCurr1DayCodingViolations_Type()
)
xdsl2PMChCurr1DayCodingViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMChCurr1DayCodingViolations.setStatus("current")
_Xdsl2PMChCurr1DayCorrectedBlocks_Type = Unsigned32
_Xdsl2PMChCurr1DayCorrectedBlocks_Object = MibTableColumn
xdsl2PMChCurr1DayCorrectedBlocks = _Xdsl2PMChCurr1DayCorrectedBlocks_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 2, 1, 1, 11),
    _Xdsl2PMChCurr1DayCorrectedBlocks_Type()
)
xdsl2PMChCurr1DayCorrectedBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMChCurr1DayCorrectedBlocks.setStatus("current")
_Xdsl2PMChHist15MinTable_Object = MibTable
xdsl2PMChHist15MinTable = _Xdsl2PMChHist15MinTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 2, 2)
)
if mibBuilder.loadTexts:
    xdsl2PMChHist15MinTable.setStatus("current")
_Xdsl2PMChHist15MinEntry_Object = MibTableRow
xdsl2PMChHist15MinEntry = _Xdsl2PMChHist15MinEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 2, 2, 1)
)
xdsl2PMChHist15MinEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VDSL2-LINE-MIB", "xdsl2PMChHist15MUnit"),
    (0, "VDSL2-LINE-MIB", "xdsl2PMChHist15MInterval"),
)
if mibBuilder.loadTexts:
    xdsl2PMChHist15MinEntry.setStatus("current")
_Xdsl2PMChHist15MUnit_Type = Xdsl2Unit
_Xdsl2PMChHist15MUnit_Object = MibTableColumn
xdsl2PMChHist15MUnit = _Xdsl2PMChHist15MUnit_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 2, 2, 1, 1),
    _Xdsl2PMChHist15MUnit_Type()
)
xdsl2PMChHist15MUnit.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xdsl2PMChHist15MUnit.setStatus("current")


class _Xdsl2PMChHist15MInterval_Type(Unsigned32):
    """Custom type xdsl2PMChHist15MInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_Xdsl2PMChHist15MInterval_Type.__name__ = "Unsigned32"
_Xdsl2PMChHist15MInterval_Object = MibTableColumn
xdsl2PMChHist15MInterval = _Xdsl2PMChHist15MInterval_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 2, 2, 1, 2),
    _Xdsl2PMChHist15MInterval_Type()
)
xdsl2PMChHist15MInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xdsl2PMChHist15MInterval.setStatus("current")
_Xdsl2PMChHist15MMonitoredTime_Type = Unsigned32
_Xdsl2PMChHist15MMonitoredTime_Object = MibTableColumn
xdsl2PMChHist15MMonitoredTime = _Xdsl2PMChHist15MMonitoredTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 2, 2, 1, 3),
    _Xdsl2PMChHist15MMonitoredTime_Type()
)
xdsl2PMChHist15MMonitoredTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMChHist15MMonitoredTime.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMChHist15MMonitoredTime.setUnits("seconds")
_Xdsl2PMChHist15MCodingViolations_Type = Unsigned32
_Xdsl2PMChHist15MCodingViolations_Object = MibTableColumn
xdsl2PMChHist15MCodingViolations = _Xdsl2PMChHist15MCodingViolations_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 2, 2, 1, 4),
    _Xdsl2PMChHist15MCodingViolations_Type()
)
xdsl2PMChHist15MCodingViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMChHist15MCodingViolations.setStatus("current")
_Xdsl2PMChHist15MCorrectedBlocks_Type = Unsigned32
_Xdsl2PMChHist15MCorrectedBlocks_Object = MibTableColumn
xdsl2PMChHist15MCorrectedBlocks = _Xdsl2PMChHist15MCorrectedBlocks_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 2, 2, 1, 5),
    _Xdsl2PMChHist15MCorrectedBlocks_Type()
)
xdsl2PMChHist15MCorrectedBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMChHist15MCorrectedBlocks.setStatus("current")
_Xdsl2PMChHist15MValidInterval_Type = TruthValue
_Xdsl2PMChHist15MValidInterval_Object = MibTableColumn
xdsl2PMChHist15MValidInterval = _Xdsl2PMChHist15MValidInterval_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 2, 2, 1, 6),
    _Xdsl2PMChHist15MValidInterval_Type()
)
xdsl2PMChHist15MValidInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMChHist15MValidInterval.setStatus("current")
_Xdsl2PMChHist1DTable_Object = MibTable
xdsl2PMChHist1DTable = _Xdsl2PMChHist1DTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 2, 3)
)
if mibBuilder.loadTexts:
    xdsl2PMChHist1DTable.setStatus("current")
_Xdsl2PMChHist1DEntry_Object = MibTableRow
xdsl2PMChHist1DEntry = _Xdsl2PMChHist1DEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 2, 3, 1)
)
xdsl2PMChHist1DEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "VDSL2-LINE-MIB", "xdsl2PMChHist1DUnit"),
    (0, "VDSL2-LINE-MIB", "xdsl2PMChHist1DInterval"),
)
if mibBuilder.loadTexts:
    xdsl2PMChHist1DEntry.setStatus("current")
_Xdsl2PMChHist1DUnit_Type = Xdsl2Unit
_Xdsl2PMChHist1DUnit_Object = MibTableColumn
xdsl2PMChHist1DUnit = _Xdsl2PMChHist1DUnit_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 2, 3, 1, 1),
    _Xdsl2PMChHist1DUnit_Type()
)
xdsl2PMChHist1DUnit.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xdsl2PMChHist1DUnit.setStatus("current")


class _Xdsl2PMChHist1DInterval_Type(Unsigned32):
    """Custom type xdsl2PMChHist1DInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_Xdsl2PMChHist1DInterval_Type.__name__ = "Unsigned32"
_Xdsl2PMChHist1DInterval_Object = MibTableColumn
xdsl2PMChHist1DInterval = _Xdsl2PMChHist1DInterval_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 2, 3, 1, 2),
    _Xdsl2PMChHist1DInterval_Type()
)
xdsl2PMChHist1DInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xdsl2PMChHist1DInterval.setStatus("current")
_Xdsl2PMChHist1DMonitoredTime_Type = Unsigned32
_Xdsl2PMChHist1DMonitoredTime_Object = MibTableColumn
xdsl2PMChHist1DMonitoredTime = _Xdsl2PMChHist1DMonitoredTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 2, 3, 1, 3),
    _Xdsl2PMChHist1DMonitoredTime_Type()
)
xdsl2PMChHist1DMonitoredTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMChHist1DMonitoredTime.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2PMChHist1DMonitoredTime.setUnits("seconds")
_Xdsl2PMChHist1DCodingViolations_Type = Unsigned32
_Xdsl2PMChHist1DCodingViolations_Object = MibTableColumn
xdsl2PMChHist1DCodingViolations = _Xdsl2PMChHist1DCodingViolations_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 2, 3, 1, 4),
    _Xdsl2PMChHist1DCodingViolations_Type()
)
xdsl2PMChHist1DCodingViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMChHist1DCodingViolations.setStatus("current")
_Xdsl2PMChHist1DCorrectedBlocks_Type = Unsigned32
_Xdsl2PMChHist1DCorrectedBlocks_Object = MibTableColumn
xdsl2PMChHist1DCorrectedBlocks = _Xdsl2PMChHist1DCorrectedBlocks_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 2, 3, 1, 5),
    _Xdsl2PMChHist1DCorrectedBlocks_Type()
)
xdsl2PMChHist1DCorrectedBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMChHist1DCorrectedBlocks.setStatus("current")
_Xdsl2PMChHist1DValidInterval_Type = TruthValue
_Xdsl2PMChHist1DValidInterval_Object = MibTableColumn
xdsl2PMChHist1DValidInterval = _Xdsl2PMChHist1DValidInterval_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 4, 2, 3, 1, 6),
    _Xdsl2PMChHist1DValidInterval_Type()
)
xdsl2PMChHist1DValidInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2PMChHist1DValidInterval.setStatus("current")
_Xdsl2Profile_ObjectIdentity = ObjectIdentity
xdsl2Profile = _Xdsl2Profile_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5)
)
_Xdsl2ProfileLine_ObjectIdentity = ObjectIdentity
xdsl2ProfileLine = _Xdsl2ProfileLine_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1)
)
_Xdsl2LineConfTemplateTable_Object = MibTable
xdsl2LineConfTemplateTable = _Xdsl2LineConfTemplateTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 1)
)
if mibBuilder.loadTexts:
    xdsl2LineConfTemplateTable.setStatus("current")
_Xdsl2LineConfTemplateEntry_Object = MibTableRow
xdsl2LineConfTemplateEntry = _Xdsl2LineConfTemplateEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 1, 1)
)
xdsl2LineConfTemplateEntry.setIndexNames(
    (0, "VDSL2-LINE-MIB", "xdsl2LConfTempTemplateName"),
)
if mibBuilder.loadTexts:
    xdsl2LineConfTemplateEntry.setStatus("current")


class _Xdsl2LConfTempTemplateName_Type(SnmpAdminString):
    """Custom type xdsl2LConfTempTemplateName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Xdsl2LConfTempTemplateName_Type.__name__ = "SnmpAdminString"
_Xdsl2LConfTempTemplateName_Object = MibTableColumn
xdsl2LConfTempTemplateName = _Xdsl2LConfTempTemplateName_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 1, 1, 1),
    _Xdsl2LConfTempTemplateName_Type()
)
xdsl2LConfTempTemplateName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xdsl2LConfTempTemplateName.setStatus("current")


class _Xdsl2LConfTempLineProfile_Type(SnmpAdminString):
    """Custom type xdsl2LConfTempLineProfile based on SnmpAdminString"""
    defaultValue = OctetString("DEFVAL")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Xdsl2LConfTempLineProfile_Type.__name__ = "SnmpAdminString"
_Xdsl2LConfTempLineProfile_Object = MibTableColumn
xdsl2LConfTempLineProfile = _Xdsl2LConfTempLineProfile_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 1, 1, 2),
    _Xdsl2LConfTempLineProfile_Type()
)
xdsl2LConfTempLineProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LConfTempLineProfile.setStatus("current")


class _Xdsl2LConfTempChan1ConfProfile_Type(SnmpAdminString):
    """Custom type xdsl2LConfTempChan1ConfProfile based on SnmpAdminString"""
    defaultValue = OctetString("DEFVAL")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Xdsl2LConfTempChan1ConfProfile_Type.__name__ = "SnmpAdminString"
_Xdsl2LConfTempChan1ConfProfile_Object = MibTableColumn
xdsl2LConfTempChan1ConfProfile = _Xdsl2LConfTempChan1ConfProfile_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 1, 1, 3),
    _Xdsl2LConfTempChan1ConfProfile_Type()
)
xdsl2LConfTempChan1ConfProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LConfTempChan1ConfProfile.setStatus("current")


class _Xdsl2LConfTempChan1RaRatioDs_Type(Unsigned32):
    """Custom type xdsl2LConfTempChan1RaRatioDs based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Xdsl2LConfTempChan1RaRatioDs_Type.__name__ = "Unsigned32"
_Xdsl2LConfTempChan1RaRatioDs_Object = MibTableColumn
xdsl2LConfTempChan1RaRatioDs = _Xdsl2LConfTempChan1RaRatioDs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 1, 1, 4),
    _Xdsl2LConfTempChan1RaRatioDs_Type()
)
xdsl2LConfTempChan1RaRatioDs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LConfTempChan1RaRatioDs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LConfTempChan1RaRatioDs.setUnits("percent")


class _Xdsl2LConfTempChan1RaRatioUs_Type(Unsigned32):
    """Custom type xdsl2LConfTempChan1RaRatioUs based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Xdsl2LConfTempChan1RaRatioUs_Type.__name__ = "Unsigned32"
_Xdsl2LConfTempChan1RaRatioUs_Object = MibTableColumn
xdsl2LConfTempChan1RaRatioUs = _Xdsl2LConfTempChan1RaRatioUs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 1, 1, 5),
    _Xdsl2LConfTempChan1RaRatioUs_Type()
)
xdsl2LConfTempChan1RaRatioUs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LConfTempChan1RaRatioUs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LConfTempChan1RaRatioUs.setUnits("percent")


class _Xdsl2LConfTempChan2ConfProfile_Type(SnmpAdminString):
    """Custom type xdsl2LConfTempChan2ConfProfile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Xdsl2LConfTempChan2ConfProfile_Type.__name__ = "SnmpAdminString"
_Xdsl2LConfTempChan2ConfProfile_Object = MibTableColumn
xdsl2LConfTempChan2ConfProfile = _Xdsl2LConfTempChan2ConfProfile_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 1, 1, 6),
    _Xdsl2LConfTempChan2ConfProfile_Type()
)
xdsl2LConfTempChan2ConfProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LConfTempChan2ConfProfile.setStatus("current")


class _Xdsl2LConfTempChan2RaRatioDs_Type(Unsigned32):
    """Custom type xdsl2LConfTempChan2RaRatioDs based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Xdsl2LConfTempChan2RaRatioDs_Type.__name__ = "Unsigned32"
_Xdsl2LConfTempChan2RaRatioDs_Object = MibTableColumn
xdsl2LConfTempChan2RaRatioDs = _Xdsl2LConfTempChan2RaRatioDs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 1, 1, 7),
    _Xdsl2LConfTempChan2RaRatioDs_Type()
)
xdsl2LConfTempChan2RaRatioDs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LConfTempChan2RaRatioDs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LConfTempChan2RaRatioDs.setUnits("percent")


class _Xdsl2LConfTempChan2RaRatioUs_Type(Unsigned32):
    """Custom type xdsl2LConfTempChan2RaRatioUs based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Xdsl2LConfTempChan2RaRatioUs_Type.__name__ = "Unsigned32"
_Xdsl2LConfTempChan2RaRatioUs_Object = MibTableColumn
xdsl2LConfTempChan2RaRatioUs = _Xdsl2LConfTempChan2RaRatioUs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 1, 1, 8),
    _Xdsl2LConfTempChan2RaRatioUs_Type()
)
xdsl2LConfTempChan2RaRatioUs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LConfTempChan2RaRatioUs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LConfTempChan2RaRatioUs.setUnits("percent")


class _Xdsl2LConfTempChan3ConfProfile_Type(SnmpAdminString):
    """Custom type xdsl2LConfTempChan3ConfProfile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Xdsl2LConfTempChan3ConfProfile_Type.__name__ = "SnmpAdminString"
_Xdsl2LConfTempChan3ConfProfile_Object = MibTableColumn
xdsl2LConfTempChan3ConfProfile = _Xdsl2LConfTempChan3ConfProfile_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 1, 1, 9),
    _Xdsl2LConfTempChan3ConfProfile_Type()
)
xdsl2LConfTempChan3ConfProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LConfTempChan3ConfProfile.setStatus("current")


class _Xdsl2LConfTempChan3RaRatioDs_Type(Unsigned32):
    """Custom type xdsl2LConfTempChan3RaRatioDs based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Xdsl2LConfTempChan3RaRatioDs_Type.__name__ = "Unsigned32"
_Xdsl2LConfTempChan3RaRatioDs_Object = MibTableColumn
xdsl2LConfTempChan3RaRatioDs = _Xdsl2LConfTempChan3RaRatioDs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 1, 1, 10),
    _Xdsl2LConfTempChan3RaRatioDs_Type()
)
xdsl2LConfTempChan3RaRatioDs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LConfTempChan3RaRatioDs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LConfTempChan3RaRatioDs.setUnits("percent")


class _Xdsl2LConfTempChan3RaRatioUs_Type(Unsigned32):
    """Custom type xdsl2LConfTempChan3RaRatioUs based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Xdsl2LConfTempChan3RaRatioUs_Type.__name__ = "Unsigned32"
_Xdsl2LConfTempChan3RaRatioUs_Object = MibTableColumn
xdsl2LConfTempChan3RaRatioUs = _Xdsl2LConfTempChan3RaRatioUs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 1, 1, 11),
    _Xdsl2LConfTempChan3RaRatioUs_Type()
)
xdsl2LConfTempChan3RaRatioUs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LConfTempChan3RaRatioUs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LConfTempChan3RaRatioUs.setUnits("percent")


class _Xdsl2LConfTempChan4ConfProfile_Type(SnmpAdminString):
    """Custom type xdsl2LConfTempChan4ConfProfile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Xdsl2LConfTempChan4ConfProfile_Type.__name__ = "SnmpAdminString"
_Xdsl2LConfTempChan4ConfProfile_Object = MibTableColumn
xdsl2LConfTempChan4ConfProfile = _Xdsl2LConfTempChan4ConfProfile_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 1, 1, 12),
    _Xdsl2LConfTempChan4ConfProfile_Type()
)
xdsl2LConfTempChan4ConfProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LConfTempChan4ConfProfile.setStatus("current")


class _Xdsl2LConfTempChan4RaRatioDs_Type(Unsigned32):
    """Custom type xdsl2LConfTempChan4RaRatioDs based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Xdsl2LConfTempChan4RaRatioDs_Type.__name__ = "Unsigned32"
_Xdsl2LConfTempChan4RaRatioDs_Object = MibTableColumn
xdsl2LConfTempChan4RaRatioDs = _Xdsl2LConfTempChan4RaRatioDs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 1, 1, 13),
    _Xdsl2LConfTempChan4RaRatioDs_Type()
)
xdsl2LConfTempChan4RaRatioDs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LConfTempChan4RaRatioDs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LConfTempChan4RaRatioDs.setUnits("percent")


class _Xdsl2LConfTempChan4RaRatioUs_Type(Unsigned32):
    """Custom type xdsl2LConfTempChan4RaRatioUs based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Xdsl2LConfTempChan4RaRatioUs_Type.__name__ = "Unsigned32"
_Xdsl2LConfTempChan4RaRatioUs_Object = MibTableColumn
xdsl2LConfTempChan4RaRatioUs = _Xdsl2LConfTempChan4RaRatioUs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 1, 1, 14),
    _Xdsl2LConfTempChan4RaRatioUs_Type()
)
xdsl2LConfTempChan4RaRatioUs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LConfTempChan4RaRatioUs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LConfTempChan4RaRatioUs.setUnits("percent")
_Xdsl2LConfTempRowStatus_Type = RowStatus
_Xdsl2LConfTempRowStatus_Object = MibTableColumn
xdsl2LConfTempRowStatus = _Xdsl2LConfTempRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 1, 1, 15),
    _Xdsl2LConfTempRowStatus_Type()
)
xdsl2LConfTempRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LConfTempRowStatus.setStatus("current")
_Xdsl2LineConfProfTable_Object = MibTable
xdsl2LineConfProfTable = _Xdsl2LineConfProfTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 2)
)
if mibBuilder.loadTexts:
    xdsl2LineConfProfTable.setStatus("current")
_Xdsl2LineConfProfEntry_Object = MibTableRow
xdsl2LineConfProfEntry = _Xdsl2LineConfProfEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 2, 1)
)
xdsl2LineConfProfEntry.setIndexNames(
    (0, "VDSL2-LINE-MIB", "xdsl2LConfProfProfileName"),
)
if mibBuilder.loadTexts:
    xdsl2LineConfProfEntry.setStatus("current")


class _Xdsl2LConfProfProfileName_Type(SnmpAdminString):
    """Custom type xdsl2LConfProfProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Xdsl2LConfProfProfileName_Type.__name__ = "SnmpAdminString"
_Xdsl2LConfProfProfileName_Object = MibTableColumn
xdsl2LConfProfProfileName = _Xdsl2LConfProfProfileName_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 2, 1, 1),
    _Xdsl2LConfProfProfileName_Type()
)
xdsl2LConfProfProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xdsl2LConfProfProfileName.setStatus("current")
_Xdsl2LConfProfScMaskDs_Type = Xdsl2ScMaskDs
_Xdsl2LConfProfScMaskDs_Object = MibTableColumn
xdsl2LConfProfScMaskDs = _Xdsl2LConfProfScMaskDs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 2, 1, 2),
    _Xdsl2LConfProfScMaskDs_Type()
)
xdsl2LConfProfScMaskDs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LConfProfScMaskDs.setStatus("current")
_Xdsl2LConfProfScMaskUs_Type = Xdsl2ScMaskUs
_Xdsl2LConfProfScMaskUs_Object = MibTableColumn
xdsl2LConfProfScMaskUs = _Xdsl2LConfProfScMaskUs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 2, 1, 3),
    _Xdsl2LConfProfScMaskUs_Type()
)
xdsl2LConfProfScMaskUs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LConfProfScMaskUs.setStatus("current")
_Xdsl2LConfProfVdsl2CarMask_Type = Xdsl2CarMask
_Xdsl2LConfProfVdsl2CarMask_Object = MibTableColumn
xdsl2LConfProfVdsl2CarMask = _Xdsl2LConfProfVdsl2CarMask_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 2, 1, 4),
    _Xdsl2LConfProfVdsl2CarMask_Type()
)
xdsl2LConfProfVdsl2CarMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LConfProfVdsl2CarMask.setStatus("current")
_Xdsl2LConfProfRfiBands_Type = Xdsl2RfiBands
_Xdsl2LConfProfRfiBands_Object = MibTableColumn
xdsl2LConfProfRfiBands = _Xdsl2LConfProfRfiBands_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 2, 1, 5),
    _Xdsl2LConfProfRfiBands_Type()
)
xdsl2LConfProfRfiBands.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LConfProfRfiBands.setStatus("current")


class _Xdsl2LConfProfRaModeDs_Type(Xdsl2RaMode):
    """Custom type xdsl2LConfProfRaModeDs based on Xdsl2RaMode"""


_Xdsl2LConfProfRaModeDs_Object = MibTableColumn
xdsl2LConfProfRaModeDs = _Xdsl2LConfProfRaModeDs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 2, 1, 6),
    _Xdsl2LConfProfRaModeDs_Type()
)
xdsl2LConfProfRaModeDs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LConfProfRaModeDs.setStatus("current")


class _Xdsl2LConfProfRaModeUs_Type(Xdsl2RaMode):
    """Custom type xdsl2LConfProfRaModeUs based on Xdsl2RaMode"""


_Xdsl2LConfProfRaModeUs_Object = MibTableColumn
xdsl2LConfProfRaModeUs = _Xdsl2LConfProfRaModeUs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 2, 1, 7),
    _Xdsl2LConfProfRaModeUs_Type()
)
xdsl2LConfProfRaModeUs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LConfProfRaModeUs.setStatus("current")


class _Xdsl2LConfProfRaUsNrmDs_Type(Unsigned32):
    """Custom type xdsl2LConfProfRaUsNrmDs based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_Xdsl2LConfProfRaUsNrmDs_Type.__name__ = "Unsigned32"
_Xdsl2LConfProfRaUsNrmDs_Object = MibTableColumn
xdsl2LConfProfRaUsNrmDs = _Xdsl2LConfProfRaUsNrmDs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 2, 1, 8),
    _Xdsl2LConfProfRaUsNrmDs_Type()
)
xdsl2LConfProfRaUsNrmDs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LConfProfRaUsNrmDs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LConfProfRaUsNrmDs.setUnits("0.1 dB")


class _Xdsl2LConfProfRaUsNrmUs_Type(Unsigned32):
    """Custom type xdsl2LConfProfRaUsNrmUs based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_Xdsl2LConfProfRaUsNrmUs_Type.__name__ = "Unsigned32"
_Xdsl2LConfProfRaUsNrmUs_Object = MibTableColumn
xdsl2LConfProfRaUsNrmUs = _Xdsl2LConfProfRaUsNrmUs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 2, 1, 9),
    _Xdsl2LConfProfRaUsNrmUs_Type()
)
xdsl2LConfProfRaUsNrmUs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LConfProfRaUsNrmUs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LConfProfRaUsNrmUs.setUnits("0.1 dB")


class _Xdsl2LConfProfRaUsTimeDs_Type(Unsigned32):
    """Custom type xdsl2LConfProfRaUsTimeDs based on Unsigned32"""
    defaultValue = 3600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_Xdsl2LConfProfRaUsTimeDs_Type.__name__ = "Unsigned32"
_Xdsl2LConfProfRaUsTimeDs_Object = MibTableColumn
xdsl2LConfProfRaUsTimeDs = _Xdsl2LConfProfRaUsTimeDs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 2, 1, 10),
    _Xdsl2LConfProfRaUsTimeDs_Type()
)
xdsl2LConfProfRaUsTimeDs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LConfProfRaUsTimeDs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LConfProfRaUsTimeDs.setUnits("seconds")


class _Xdsl2LConfProfRaUsTimeUs_Type(Unsigned32):
    """Custom type xdsl2LConfProfRaUsTimeUs based on Unsigned32"""
    defaultValue = 3600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_Xdsl2LConfProfRaUsTimeUs_Type.__name__ = "Unsigned32"
_Xdsl2LConfProfRaUsTimeUs_Object = MibTableColumn
xdsl2LConfProfRaUsTimeUs = _Xdsl2LConfProfRaUsTimeUs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 2, 1, 11),
    _Xdsl2LConfProfRaUsTimeUs_Type()
)
xdsl2LConfProfRaUsTimeUs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LConfProfRaUsTimeUs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LConfProfRaUsTimeUs.setUnits("seconds")


class _Xdsl2LConfProfRaDsNrmDs_Type(Unsigned32):
    """Custom type xdsl2LConfProfRaDsNrmDs based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_Xdsl2LConfProfRaDsNrmDs_Type.__name__ = "Unsigned32"
_Xdsl2LConfProfRaDsNrmDs_Object = MibTableColumn
xdsl2LConfProfRaDsNrmDs = _Xdsl2LConfProfRaDsNrmDs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 2, 1, 12),
    _Xdsl2LConfProfRaDsNrmDs_Type()
)
xdsl2LConfProfRaDsNrmDs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LConfProfRaDsNrmDs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LConfProfRaDsNrmDs.setUnits("0.1 dB")


class _Xdsl2LConfProfRaDsNrmUs_Type(Unsigned32):
    """Custom type xdsl2LConfProfRaDsNrmUs based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_Xdsl2LConfProfRaDsNrmUs_Type.__name__ = "Unsigned32"
_Xdsl2LConfProfRaDsNrmUs_Object = MibTableColumn
xdsl2LConfProfRaDsNrmUs = _Xdsl2LConfProfRaDsNrmUs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 2, 1, 13),
    _Xdsl2LConfProfRaDsNrmUs_Type()
)
xdsl2LConfProfRaDsNrmUs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LConfProfRaDsNrmUs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LConfProfRaDsNrmUs.setUnits("0.1 dB")


class _Xdsl2LConfProfRaDsTimeDs_Type(Unsigned32):
    """Custom type xdsl2LConfProfRaDsTimeDs based on Unsigned32"""
    defaultValue = 3600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_Xdsl2LConfProfRaDsTimeDs_Type.__name__ = "Unsigned32"
_Xdsl2LConfProfRaDsTimeDs_Object = MibTableColumn
xdsl2LConfProfRaDsTimeDs = _Xdsl2LConfProfRaDsTimeDs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 2, 1, 14),
    _Xdsl2LConfProfRaDsTimeDs_Type()
)
xdsl2LConfProfRaDsTimeDs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LConfProfRaDsTimeDs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LConfProfRaDsTimeDs.setUnits("seconds")


class _Xdsl2LConfProfRaDsTimeUs_Type(Unsigned32):
    """Custom type xdsl2LConfProfRaDsTimeUs based on Unsigned32"""
    defaultValue = 3600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_Xdsl2LConfProfRaDsTimeUs_Type.__name__ = "Unsigned32"
_Xdsl2LConfProfRaDsTimeUs_Object = MibTableColumn
xdsl2LConfProfRaDsTimeUs = _Xdsl2LConfProfRaDsTimeUs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 2, 1, 15),
    _Xdsl2LConfProfRaDsTimeUs_Type()
)
xdsl2LConfProfRaDsTimeUs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LConfProfRaDsTimeUs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LConfProfRaDsTimeUs.setUnits("seconds")


class _Xdsl2LConfProfTargetSnrmDs_Type(Unsigned32):
    """Custom type xdsl2LConfProfTargetSnrmDs based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_Xdsl2LConfProfTargetSnrmDs_Type.__name__ = "Unsigned32"
_Xdsl2LConfProfTargetSnrmDs_Object = MibTableColumn
xdsl2LConfProfTargetSnrmDs = _Xdsl2LConfProfTargetSnrmDs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 2, 1, 16),
    _Xdsl2LConfProfTargetSnrmDs_Type()
)
xdsl2LConfProfTargetSnrmDs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LConfProfTargetSnrmDs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LConfProfTargetSnrmDs.setUnits("0.1 dB")


class _Xdsl2LConfProfTargetSnrmUs_Type(Unsigned32):
    """Custom type xdsl2LConfProfTargetSnrmUs based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_Xdsl2LConfProfTargetSnrmUs_Type.__name__ = "Unsigned32"
_Xdsl2LConfProfTargetSnrmUs_Object = MibTableColumn
xdsl2LConfProfTargetSnrmUs = _Xdsl2LConfProfTargetSnrmUs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 2, 1, 17),
    _Xdsl2LConfProfTargetSnrmUs_Type()
)
xdsl2LConfProfTargetSnrmUs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LConfProfTargetSnrmUs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LConfProfTargetSnrmUs.setUnits("0.1 dB")


class _Xdsl2LConfProfMaxSnrmDs_Type(Unsigned32):
    """Custom type xdsl2LConfProfMaxSnrmDs based on Unsigned32"""
    defaultValue = 310

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_Xdsl2LConfProfMaxSnrmDs_Type.__name__ = "Unsigned32"
_Xdsl2LConfProfMaxSnrmDs_Object = MibTableColumn
xdsl2LConfProfMaxSnrmDs = _Xdsl2LConfProfMaxSnrmDs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 2, 1, 18),
    _Xdsl2LConfProfMaxSnrmDs_Type()
)
xdsl2LConfProfMaxSnrmDs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LConfProfMaxSnrmDs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LConfProfMaxSnrmDs.setUnits("0.1 dB")


class _Xdsl2LConfProfMaxSnrmUs_Type(Unsigned32):
    """Custom type xdsl2LConfProfMaxSnrmUs based on Unsigned32"""
    defaultValue = 310

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_Xdsl2LConfProfMaxSnrmUs_Type.__name__ = "Unsigned32"
_Xdsl2LConfProfMaxSnrmUs_Object = MibTableColumn
xdsl2LConfProfMaxSnrmUs = _Xdsl2LConfProfMaxSnrmUs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 2, 1, 19),
    _Xdsl2LConfProfMaxSnrmUs_Type()
)
xdsl2LConfProfMaxSnrmUs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LConfProfMaxSnrmUs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LConfProfMaxSnrmUs.setUnits("0.1 dB")


class _Xdsl2LConfProfMinSnrmDs_Type(Unsigned32):
    """Custom type xdsl2LConfProfMinSnrmDs based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_Xdsl2LConfProfMinSnrmDs_Type.__name__ = "Unsigned32"
_Xdsl2LConfProfMinSnrmDs_Object = MibTableColumn
xdsl2LConfProfMinSnrmDs = _Xdsl2LConfProfMinSnrmDs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 2, 1, 20),
    _Xdsl2LConfProfMinSnrmDs_Type()
)
xdsl2LConfProfMinSnrmDs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LConfProfMinSnrmDs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LConfProfMinSnrmDs.setUnits("0.1 dB")


class _Xdsl2LConfProfMinSnrmUs_Type(Unsigned32):
    """Custom type xdsl2LConfProfMinSnrmUs based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_Xdsl2LConfProfMinSnrmUs_Type.__name__ = "Unsigned32"
_Xdsl2LConfProfMinSnrmUs_Object = MibTableColumn
xdsl2LConfProfMinSnrmUs = _Xdsl2LConfProfMinSnrmUs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 2, 1, 21),
    _Xdsl2LConfProfMinSnrmUs_Type()
)
xdsl2LConfProfMinSnrmUs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LConfProfMinSnrmUs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LConfProfMinSnrmUs.setUnits("0.1 dB")


class _Xdsl2LConfProfMsgMinUs_Type(Unsigned32):
    """Custom type xdsl2LConfProfMsgMinUs based on Unsigned32"""
    defaultValue = 4000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4000, 248000),
    )


_Xdsl2LConfProfMsgMinUs_Type.__name__ = "Unsigned32"
_Xdsl2LConfProfMsgMinUs_Object = MibTableColumn
xdsl2LConfProfMsgMinUs = _Xdsl2LConfProfMsgMinUs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 2, 1, 22),
    _Xdsl2LConfProfMsgMinUs_Type()
)
xdsl2LConfProfMsgMinUs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LConfProfMsgMinUs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LConfProfMsgMinUs.setUnits("bits/second")


class _Xdsl2LConfProfMsgMinDs_Type(Unsigned32):
    """Custom type xdsl2LConfProfMsgMinDs based on Unsigned32"""
    defaultValue = 4000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4000, 248000),
    )


_Xdsl2LConfProfMsgMinDs_Type.__name__ = "Unsigned32"
_Xdsl2LConfProfMsgMinDs_Object = MibTableColumn
xdsl2LConfProfMsgMinDs = _Xdsl2LConfProfMsgMinDs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 2, 1, 23),
    _Xdsl2LConfProfMsgMinDs_Type()
)
xdsl2LConfProfMsgMinDs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LConfProfMsgMinDs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LConfProfMsgMinDs.setUnits("bits/second")


class _Xdsl2LConfProfCeFlag_Type(Xdsl2LineCeFlag):
    """Custom type xdsl2LConfProfCeFlag based on Xdsl2LineCeFlag"""
    defaultBinValue = "0"


_Xdsl2LConfProfCeFlag_Object = MibTableColumn
xdsl2LConfProfCeFlag = _Xdsl2LConfProfCeFlag_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 2, 1, 24),
    _Xdsl2LConfProfCeFlag_Type()
)
xdsl2LConfProfCeFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LConfProfCeFlag.setStatus("current")


class _Xdsl2LConfProfSnrModeDs_Type(Xdsl2LineSnrMode):
    """Custom type xdsl2LConfProfSnrModeDs based on Xdsl2LineSnrMode"""


_Xdsl2LConfProfSnrModeDs_Object = MibTableColumn
xdsl2LConfProfSnrModeDs = _Xdsl2LConfProfSnrModeDs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 2, 1, 25),
    _Xdsl2LConfProfSnrModeDs_Type()
)
xdsl2LConfProfSnrModeDs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LConfProfSnrModeDs.setStatus("current")


class _Xdsl2LConfProfSnrModeUs_Type(Xdsl2LineSnrMode):
    """Custom type xdsl2LConfProfSnrModeUs based on Xdsl2LineSnrMode"""


_Xdsl2LConfProfSnrModeUs_Object = MibTableColumn
xdsl2LConfProfSnrModeUs = _Xdsl2LConfProfSnrModeUs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 2, 1, 26),
    _Xdsl2LConfProfSnrModeUs_Type()
)
xdsl2LConfProfSnrModeUs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LConfProfSnrModeUs.setStatus("current")
_Xdsl2LConfProfTxRefVnDs_Type = Xdsl2LineTxRefVnDs
_Xdsl2LConfProfTxRefVnDs_Object = MibTableColumn
xdsl2LConfProfTxRefVnDs = _Xdsl2LConfProfTxRefVnDs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 2, 1, 27),
    _Xdsl2LConfProfTxRefVnDs_Type()
)
xdsl2LConfProfTxRefVnDs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LConfProfTxRefVnDs.setStatus("current")
_Xdsl2LConfProfTxRefVnUs_Type = Xdsl2LineTxRefVnUs
_Xdsl2LConfProfTxRefVnUs_Object = MibTableColumn
xdsl2LConfProfTxRefVnUs = _Xdsl2LConfProfTxRefVnUs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 2, 1, 28),
    _Xdsl2LConfProfTxRefVnUs_Type()
)
xdsl2LConfProfTxRefVnUs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LConfProfTxRefVnUs.setStatus("current")
_Xdsl2LConfProfXtuTransSysEna_Type = Xdsl2TransmissionModeType
_Xdsl2LConfProfXtuTransSysEna_Object = MibTableColumn
xdsl2LConfProfXtuTransSysEna = _Xdsl2LConfProfXtuTransSysEna_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 2, 1, 29),
    _Xdsl2LConfProfXtuTransSysEna_Type()
)
xdsl2LConfProfXtuTransSysEna.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LConfProfXtuTransSysEna.setStatus("current")


class _Xdsl2LConfProfPmMode_Type(Xdsl2LinePmMode):
    """Custom type xdsl2LConfProfPmMode based on Xdsl2LinePmMode"""
    defaultBinValue = "11"


_Xdsl2LConfProfPmMode_Object = MibTableColumn
xdsl2LConfProfPmMode = _Xdsl2LConfProfPmMode_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 2, 1, 30),
    _Xdsl2LConfProfPmMode_Type()
)
xdsl2LConfProfPmMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LConfProfPmMode.setStatus("current")


class _Xdsl2LConfProfL0Time_Type(Unsigned32):
    """Custom type xdsl2LConfProfL0Time based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Xdsl2LConfProfL0Time_Type.__name__ = "Unsigned32"
_Xdsl2LConfProfL0Time_Object = MibTableColumn
xdsl2LConfProfL0Time = _Xdsl2LConfProfL0Time_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 2, 1, 31),
    _Xdsl2LConfProfL0Time_Type()
)
xdsl2LConfProfL0Time.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LConfProfL0Time.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LConfProfL0Time.setUnits("seconds")


class _Xdsl2LConfProfL2Time_Type(Unsigned32):
    """Custom type xdsl2LConfProfL2Time based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Xdsl2LConfProfL2Time_Type.__name__ = "Unsigned32"
_Xdsl2LConfProfL2Time_Object = MibTableColumn
xdsl2LConfProfL2Time = _Xdsl2LConfProfL2Time_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 2, 1, 32),
    _Xdsl2LConfProfL2Time_Type()
)
xdsl2LConfProfL2Time.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LConfProfL2Time.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LConfProfL2Time.setUnits("seconds")


class _Xdsl2LConfProfL2Atpr_Type(Unsigned32):
    """Custom type xdsl2LConfProfL2Atpr based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_Xdsl2LConfProfL2Atpr_Type.__name__ = "Unsigned32"
_Xdsl2LConfProfL2Atpr_Object = MibTableColumn
xdsl2LConfProfL2Atpr = _Xdsl2LConfProfL2Atpr_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 2, 1, 33),
    _Xdsl2LConfProfL2Atpr_Type()
)
xdsl2LConfProfL2Atpr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LConfProfL2Atpr.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LConfProfL2Atpr.setUnits("dB")


class _Xdsl2LConfProfL2Atprt_Type(Unsigned32):
    """Custom type xdsl2LConfProfL2Atprt based on Unsigned32"""
    defaultValue = 31

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_Xdsl2LConfProfL2Atprt_Type.__name__ = "Unsigned32"
_Xdsl2LConfProfL2Atprt_Object = MibTableColumn
xdsl2LConfProfL2Atprt = _Xdsl2LConfProfL2Atprt_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 2, 1, 34),
    _Xdsl2LConfProfL2Atprt_Type()
)
xdsl2LConfProfL2Atprt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LConfProfL2Atprt.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LConfProfL2Atprt.setUnits("dB")


class _Xdsl2LConfProfProfiles_Type(Xdsl2LineProfiles):
    """Custom type xdsl2LConfProfProfiles based on Xdsl2LineProfiles"""
    defaultBinValue = "11111111"


_Xdsl2LConfProfProfiles_Object = MibTableColumn
xdsl2LConfProfProfiles = _Xdsl2LConfProfProfiles_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 2, 1, 35),
    _Xdsl2LConfProfProfiles_Type()
)
xdsl2LConfProfProfiles.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LConfProfProfiles.setStatus("current")
_Xdsl2LConfProfDpboEPsd_Type = Xdsl2PsdMaskDs
_Xdsl2LConfProfDpboEPsd_Object = MibTableColumn
xdsl2LConfProfDpboEPsd = _Xdsl2LConfProfDpboEPsd_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 2, 1, 36),
    _Xdsl2LConfProfDpboEPsd_Type()
)
xdsl2LConfProfDpboEPsd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LConfProfDpboEPsd.setStatus("current")


class _Xdsl2LConfProfDpboEsEL_Type(Unsigned32):
    """Custom type xdsl2LConfProfDpboEsEL based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 511),
    )


_Xdsl2LConfProfDpboEsEL_Type.__name__ = "Unsigned32"
_Xdsl2LConfProfDpboEsEL_Object = MibTableColumn
xdsl2LConfProfDpboEsEL = _Xdsl2LConfProfDpboEsEL_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 2, 1, 37),
    _Xdsl2LConfProfDpboEsEL_Type()
)
xdsl2LConfProfDpboEsEL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LConfProfDpboEsEL.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LConfProfDpboEsEL.setUnits("0.5 dB")


class _Xdsl2LConfProfDpboEsCableModelA_Type(Unsigned32):
    """Custom type xdsl2LConfProfDpboEsCableModelA based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 640),
    )


_Xdsl2LConfProfDpboEsCableModelA_Type.__name__ = "Unsigned32"
_Xdsl2LConfProfDpboEsCableModelA_Object = MibTableColumn
xdsl2LConfProfDpboEsCableModelA = _Xdsl2LConfProfDpboEsCableModelA_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 2, 1, 38),
    _Xdsl2LConfProfDpboEsCableModelA_Type()
)
xdsl2LConfProfDpboEsCableModelA.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LConfProfDpboEsCableModelA.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LConfProfDpboEsCableModelA.setUnits("2^-8")


class _Xdsl2LConfProfDpboEsCableModelB_Type(Unsigned32):
    """Custom type xdsl2LConfProfDpboEsCableModelB based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 640),
    )


_Xdsl2LConfProfDpboEsCableModelB_Type.__name__ = "Unsigned32"
_Xdsl2LConfProfDpboEsCableModelB_Object = MibTableColumn
xdsl2LConfProfDpboEsCableModelB = _Xdsl2LConfProfDpboEsCableModelB_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 2, 1, 39),
    _Xdsl2LConfProfDpboEsCableModelB_Type()
)
xdsl2LConfProfDpboEsCableModelB.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LConfProfDpboEsCableModelB.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LConfProfDpboEsCableModelB.setUnits("2^-8")


class _Xdsl2LConfProfDpboEsCableModelC_Type(Unsigned32):
    """Custom type xdsl2LConfProfDpboEsCableModelC based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 640),
    )


_Xdsl2LConfProfDpboEsCableModelC_Type.__name__ = "Unsigned32"
_Xdsl2LConfProfDpboEsCableModelC_Object = MibTableColumn
xdsl2LConfProfDpboEsCableModelC = _Xdsl2LConfProfDpboEsCableModelC_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 2, 1, 40),
    _Xdsl2LConfProfDpboEsCableModelC_Type()
)
xdsl2LConfProfDpboEsCableModelC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LConfProfDpboEsCableModelC.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LConfProfDpboEsCableModelC.setUnits("2^-8")


class _Xdsl2LConfProfDpboMus_Type(Unsigned32):
    """Custom type xdsl2LConfProfDpboMus based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Xdsl2LConfProfDpboMus_Type.__name__ = "Unsigned32"
_Xdsl2LConfProfDpboMus_Object = MibTableColumn
xdsl2LConfProfDpboMus = _Xdsl2LConfProfDpboMus_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 2, 1, 41),
    _Xdsl2LConfProfDpboMus_Type()
)
xdsl2LConfProfDpboMus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LConfProfDpboMus.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LConfProfDpboMus.setUnits("0.5 dBm/Hz")


class _Xdsl2LConfProfDpboFMin_Type(Unsigned32):
    """Custom type xdsl2LConfProfDpboFMin based on Unsigned32"""
    defaultValue = 32

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_Xdsl2LConfProfDpboFMin_Type.__name__ = "Unsigned32"
_Xdsl2LConfProfDpboFMin_Object = MibTableColumn
xdsl2LConfProfDpboFMin = _Xdsl2LConfProfDpboFMin_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 2, 1, 42),
    _Xdsl2LConfProfDpboFMin_Type()
)
xdsl2LConfProfDpboFMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LConfProfDpboFMin.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LConfProfDpboFMin.setUnits("4.3125 kHz")


class _Xdsl2LConfProfDpboFMax_Type(Unsigned32):
    """Custom type xdsl2LConfProfDpboFMax based on Unsigned32"""
    defaultValue = 512

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 6956),
    )


_Xdsl2LConfProfDpboFMax_Type.__name__ = "Unsigned32"
_Xdsl2LConfProfDpboFMax_Object = MibTableColumn
xdsl2LConfProfDpboFMax = _Xdsl2LConfProfDpboFMax_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 2, 1, 43),
    _Xdsl2LConfProfDpboFMax_Type()
)
xdsl2LConfProfDpboFMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LConfProfDpboFMax.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LConfProfDpboFMax.setUnits("4.3125 kHz")


class _Xdsl2LConfProfUpboKL_Type(Unsigned32):
    """Custom type xdsl2LConfProfUpboKL based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1280),
    )


_Xdsl2LConfProfUpboKL_Type.__name__ = "Unsigned32"
_Xdsl2LConfProfUpboKL_Object = MibTableColumn
xdsl2LConfProfUpboKL = _Xdsl2LConfProfUpboKL_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 2, 1, 44),
    _Xdsl2LConfProfUpboKL_Type()
)
xdsl2LConfProfUpboKL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LConfProfUpboKL.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LConfProfUpboKL.setUnits("0.1 dB")


class _Xdsl2LConfProfUpboKLF_Type(Xdsl2UpboKLF):
    """Custom type xdsl2LConfProfUpboKLF based on Xdsl2UpboKLF"""


_Xdsl2LConfProfUpboKLF_Object = MibTableColumn
xdsl2LConfProfUpboKLF = _Xdsl2LConfProfUpboKLF_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 2, 1, 45),
    _Xdsl2LConfProfUpboKLF_Type()
)
xdsl2LConfProfUpboKLF.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LConfProfUpboKLF.setStatus("current")


class _Xdsl2LConfProfUs0Mask_Type(Xdsl2LineUs0Mask):
    """Custom type xdsl2LConfProfUs0Mask based on Xdsl2LineUs0Mask"""
    defaultBinValue = "0"


_Xdsl2LConfProfUs0Mask_Object = MibTableColumn
xdsl2LConfProfUs0Mask = _Xdsl2LConfProfUs0Mask_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 2, 1, 46),
    _Xdsl2LConfProfUs0Mask_Type()
)
xdsl2LConfProfUs0Mask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LConfProfUs0Mask.setStatus("current")


class _Xdsl2LConfProfForceInp_Type(TruthValue):
    """Custom type xdsl2LConfProfForceInp based on TruthValue"""


_Xdsl2LConfProfForceInp_Object = MibTableColumn
xdsl2LConfProfForceInp = _Xdsl2LConfProfForceInp_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 2, 1, 47),
    _Xdsl2LConfProfForceInp_Type()
)
xdsl2LConfProfForceInp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LConfProfForceInp.setStatus("current")
_Xdsl2LConfProfRowStatus_Type = RowStatus
_Xdsl2LConfProfRowStatus_Object = MibTableColumn
xdsl2LConfProfRowStatus = _Xdsl2LConfProfRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 2, 1, 48),
    _Xdsl2LConfProfRowStatus_Type()
)
xdsl2LConfProfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LConfProfRowStatus.setStatus("current")
_Xdsl2LineConfProfModeSpecTable_Object = MibTable
xdsl2LineConfProfModeSpecTable = _Xdsl2LineConfProfModeSpecTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 3)
)
if mibBuilder.loadTexts:
    xdsl2LineConfProfModeSpecTable.setStatus("current")
_Xdsl2LineConfProfModeSpecEntry_Object = MibTableRow
xdsl2LineConfProfModeSpecEntry = _Xdsl2LineConfProfModeSpecEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 3, 1)
)
xdsl2LineConfProfModeSpecEntry.setIndexNames(
    (0, "VDSL2-LINE-MIB", "xdsl2LConfProfProfileName"),
    (0, "VDSL2-LINE-MIB", "xdsl2LConfProfXdslMode"),
)
if mibBuilder.loadTexts:
    xdsl2LineConfProfModeSpecEntry.setStatus("current")
_Xdsl2LConfProfXdslMode_Type = Xdsl2OperationModes
_Xdsl2LConfProfXdslMode_Object = MibTableColumn
xdsl2LConfProfXdslMode = _Xdsl2LConfProfXdslMode_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 3, 1, 1),
    _Xdsl2LConfProfXdslMode_Type()
)
xdsl2LConfProfXdslMode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xdsl2LConfProfXdslMode.setStatus("current")


class _Xdsl2LConfProfMaxNomPsdDs_Type(Integer32):
    """Custom type xdsl2LConfProfMaxNomPsdDs based on Integer32"""
    defaultValue = -300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-600, -300),
    )


_Xdsl2LConfProfMaxNomPsdDs_Type.__name__ = "Integer32"
_Xdsl2LConfProfMaxNomPsdDs_Object = MibTableColumn
xdsl2LConfProfMaxNomPsdDs = _Xdsl2LConfProfMaxNomPsdDs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 3, 1, 2),
    _Xdsl2LConfProfMaxNomPsdDs_Type()
)
xdsl2LConfProfMaxNomPsdDs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LConfProfMaxNomPsdDs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LConfProfMaxNomPsdDs.setUnits("0.1 dBm/Hz")


class _Xdsl2LConfProfMaxNomPsdUs_Type(Integer32):
    """Custom type xdsl2LConfProfMaxNomPsdUs based on Integer32"""
    defaultValue = -300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-600, -300),
    )


_Xdsl2LConfProfMaxNomPsdUs_Type.__name__ = "Integer32"
_Xdsl2LConfProfMaxNomPsdUs_Object = MibTableColumn
xdsl2LConfProfMaxNomPsdUs = _Xdsl2LConfProfMaxNomPsdUs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 3, 1, 3),
    _Xdsl2LConfProfMaxNomPsdUs_Type()
)
xdsl2LConfProfMaxNomPsdUs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LConfProfMaxNomPsdUs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LConfProfMaxNomPsdUs.setUnits("0.1 dBm/Hz")


class _Xdsl2LConfProfMaxNomAtpDs_Type(Unsigned32):
    """Custom type xdsl2LConfProfMaxNomAtpDs based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Xdsl2LConfProfMaxNomAtpDs_Type.__name__ = "Unsigned32"
_Xdsl2LConfProfMaxNomAtpDs_Object = MibTableColumn
xdsl2LConfProfMaxNomAtpDs = _Xdsl2LConfProfMaxNomAtpDs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 3, 1, 4),
    _Xdsl2LConfProfMaxNomAtpDs_Type()
)
xdsl2LConfProfMaxNomAtpDs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LConfProfMaxNomAtpDs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LConfProfMaxNomAtpDs.setUnits("0.1 dBm")


class _Xdsl2LConfProfMaxNomAtpUs_Type(Unsigned32):
    """Custom type xdsl2LConfProfMaxNomAtpUs based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Xdsl2LConfProfMaxNomAtpUs_Type.__name__ = "Unsigned32"
_Xdsl2LConfProfMaxNomAtpUs_Object = MibTableColumn
xdsl2LConfProfMaxNomAtpUs = _Xdsl2LConfProfMaxNomAtpUs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 3, 1, 5),
    _Xdsl2LConfProfMaxNomAtpUs_Type()
)
xdsl2LConfProfMaxNomAtpUs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LConfProfMaxNomAtpUs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LConfProfMaxNomAtpUs.setUnits("0.1 dBm")


class _Xdsl2LConfProfMaxAggRxPwrUs_Type(Integer32):
    """Custom type xdsl2LConfProfMaxAggRxPwrUs based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-255, 255),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_Xdsl2LConfProfMaxAggRxPwrUs_Type.__name__ = "Integer32"
_Xdsl2LConfProfMaxAggRxPwrUs_Object = MibTableColumn
xdsl2LConfProfMaxAggRxPwrUs = _Xdsl2LConfProfMaxAggRxPwrUs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 3, 1, 6),
    _Xdsl2LConfProfMaxAggRxPwrUs_Type()
)
xdsl2LConfProfMaxAggRxPwrUs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LConfProfMaxAggRxPwrUs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LConfProfMaxAggRxPwrUs.setUnits("0.1 dBm")
_Xdsl2LConfProfPsdMaskDs_Type = Xdsl2PsdMaskDs
_Xdsl2LConfProfPsdMaskDs_Object = MibTableColumn
xdsl2LConfProfPsdMaskDs = _Xdsl2LConfProfPsdMaskDs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 3, 1, 7),
    _Xdsl2LConfProfPsdMaskDs_Type()
)
xdsl2LConfProfPsdMaskDs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LConfProfPsdMaskDs.setStatus("current")
_Xdsl2LConfProfPsdMaskUs_Type = Xdsl2PsdMaskUs
_Xdsl2LConfProfPsdMaskUs_Object = MibTableColumn
xdsl2LConfProfPsdMaskUs = _Xdsl2LConfProfPsdMaskUs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 3, 1, 8),
    _Xdsl2LConfProfPsdMaskUs_Type()
)
xdsl2LConfProfPsdMaskUs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LConfProfPsdMaskUs.setStatus("current")


class _Xdsl2LConfProfPsdMaskSelectUs_Type(Xdsl2LinePsdMaskSelectUs):
    """Custom type xdsl2LConfProfPsdMaskSelectUs based on Xdsl2LinePsdMaskSelectUs"""


_Xdsl2LConfProfPsdMaskSelectUs_Object = MibTableColumn
xdsl2LConfProfPsdMaskSelectUs = _Xdsl2LConfProfPsdMaskSelectUs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 3, 1, 9),
    _Xdsl2LConfProfPsdMaskSelectUs_Type()
)
xdsl2LConfProfPsdMaskSelectUs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LConfProfPsdMaskSelectUs.setStatus("current")


class _Xdsl2LConfProfClassMask_Type(Xdsl2LineClassMask):
    """Custom type xdsl2LConfProfClassMask based on Xdsl2LineClassMask"""


_Xdsl2LConfProfClassMask_Object = MibTableColumn
xdsl2LConfProfClassMask = _Xdsl2LConfProfClassMask_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 3, 1, 10),
    _Xdsl2LConfProfClassMask_Type()
)
xdsl2LConfProfClassMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LConfProfClassMask.setStatus("current")


class _Xdsl2LConfProfLimitMask_Type(Xdsl2LineLimitMask):
    """Custom type xdsl2LConfProfLimitMask based on Xdsl2LineLimitMask"""
    defaultBinValue = "0"


_Xdsl2LConfProfLimitMask_Object = MibTableColumn
xdsl2LConfProfLimitMask = _Xdsl2LConfProfLimitMask_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 3, 1, 11),
    _Xdsl2LConfProfLimitMask_Type()
)
xdsl2LConfProfLimitMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LConfProfLimitMask.setStatus("current")


class _Xdsl2LConfProfUs0Disable_Type(Xdsl2LineUs0Disable):
    """Custom type xdsl2LConfProfUs0Disable based on Xdsl2LineUs0Disable"""
    defaultBinValue = "0"


_Xdsl2LConfProfUs0Disable_Object = MibTableColumn
xdsl2LConfProfUs0Disable = _Xdsl2LConfProfUs0Disable_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 3, 1, 12),
    _Xdsl2LConfProfUs0Disable_Type()
)
xdsl2LConfProfUs0Disable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LConfProfUs0Disable.setStatus("current")
_Xdsl2LConfProfModeSpecRowStatus_Type = RowStatus
_Xdsl2LConfProfModeSpecRowStatus_Object = MibTableColumn
xdsl2LConfProfModeSpecRowStatus = _Xdsl2LConfProfModeSpecRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 3, 1, 13),
    _Xdsl2LConfProfModeSpecRowStatus_Type()
)
xdsl2LConfProfModeSpecRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LConfProfModeSpecRowStatus.setStatus("current")
_Xdsl2LineConfProfModeSpecBandUsTable_Object = MibTable
xdsl2LineConfProfModeSpecBandUsTable = _Xdsl2LineConfProfModeSpecBandUsTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 4)
)
if mibBuilder.loadTexts:
    xdsl2LineConfProfModeSpecBandUsTable.setStatus("current")
_Xdsl2LineConfProfModeSpecBandUsEntry_Object = MibTableRow
xdsl2LineConfProfModeSpecBandUsEntry = _Xdsl2LineConfProfModeSpecBandUsEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 4, 1)
)
xdsl2LineConfProfModeSpecBandUsEntry.setIndexNames(
    (0, "VDSL2-LINE-MIB", "xdsl2LConfProfProfileName"),
    (0, "VDSL2-LINE-MIB", "xdsl2LConfProfXdslMode"),
    (0, "VDSL2-LINE-MIB", "xdsl2LConfProfXdslBandUs"),
)
if mibBuilder.loadTexts:
    xdsl2LineConfProfModeSpecBandUsEntry.setStatus("current")
_Xdsl2LConfProfXdslBandUs_Type = Xdsl2BandUs
_Xdsl2LConfProfXdslBandUs_Object = MibTableColumn
xdsl2LConfProfXdslBandUs = _Xdsl2LConfProfXdslBandUs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 4, 1, 1),
    _Xdsl2LConfProfXdslBandUs_Type()
)
xdsl2LConfProfXdslBandUs.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xdsl2LConfProfXdslBandUs.setStatus("current")


class _Xdsl2LConfProfUpboPsdA_Type(Integer32):
    """Custom type xdsl2LConfProfUpboPsdA based on Integer32"""
    defaultValue = 4000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4000, 8095),
    )


_Xdsl2LConfProfUpboPsdA_Type.__name__ = "Integer32"
_Xdsl2LConfProfUpboPsdA_Object = MibTableColumn
xdsl2LConfProfUpboPsdA = _Xdsl2LConfProfUpboPsdA_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 4, 1, 2),
    _Xdsl2LConfProfUpboPsdA_Type()
)
xdsl2LConfProfUpboPsdA.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LConfProfUpboPsdA.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LConfProfUpboPsdA.setUnits("0.01 dBm/Hz")


class _Xdsl2LConfProfUpboPsdB_Type(Integer32):
    """Custom type xdsl2LConfProfUpboPsdB based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_Xdsl2LConfProfUpboPsdB_Type.__name__ = "Integer32"
_Xdsl2LConfProfUpboPsdB_Object = MibTableColumn
xdsl2LConfProfUpboPsdB = _Xdsl2LConfProfUpboPsdB_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 4, 1, 3),
    _Xdsl2LConfProfUpboPsdB_Type()
)
xdsl2LConfProfUpboPsdB.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LConfProfUpboPsdB.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LConfProfUpboPsdB.setUnits("0.01 dBm/Hz")
_Xdsl2LConfProfModeSpecBandUsRowStatus_Type = RowStatus
_Xdsl2LConfProfModeSpecBandUsRowStatus_Object = MibTableColumn
xdsl2LConfProfModeSpecBandUsRowStatus = _Xdsl2LConfProfModeSpecBandUsRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 1, 4, 1, 4),
    _Xdsl2LConfProfModeSpecBandUsRowStatus_Type()
)
xdsl2LConfProfModeSpecBandUsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LConfProfModeSpecBandUsRowStatus.setStatus("current")
_Xdsl2ProfileChannel_ObjectIdentity = ObjectIdentity
xdsl2ProfileChannel = _Xdsl2ProfileChannel_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 2)
)
_Xdsl2ChConfProfileTable_Object = MibTable
xdsl2ChConfProfileTable = _Xdsl2ChConfProfileTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 2, 1)
)
if mibBuilder.loadTexts:
    xdsl2ChConfProfileTable.setStatus("current")
_Xdsl2ChConfProfileEntry_Object = MibTableRow
xdsl2ChConfProfileEntry = _Xdsl2ChConfProfileEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 2, 1, 1)
)
xdsl2ChConfProfileEntry.setIndexNames(
    (0, "VDSL2-LINE-MIB", "xdsl2ChConfProfProfileName"),
)
if mibBuilder.loadTexts:
    xdsl2ChConfProfileEntry.setStatus("current")


class _Xdsl2ChConfProfProfileName_Type(SnmpAdminString):
    """Custom type xdsl2ChConfProfProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Xdsl2ChConfProfProfileName_Type.__name__ = "SnmpAdminString"
_Xdsl2ChConfProfProfileName_Object = MibTableColumn
xdsl2ChConfProfProfileName = _Xdsl2ChConfProfProfileName_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 2, 1, 1, 1),
    _Xdsl2ChConfProfProfileName_Type()
)
xdsl2ChConfProfProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xdsl2ChConfProfProfileName.setStatus("current")
_Xdsl2ChConfProfMinDataRateDs_Type = Unsigned32
_Xdsl2ChConfProfMinDataRateDs_Object = MibTableColumn
xdsl2ChConfProfMinDataRateDs = _Xdsl2ChConfProfMinDataRateDs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 2, 1, 1, 2),
    _Xdsl2ChConfProfMinDataRateDs_Type()
)
xdsl2ChConfProfMinDataRateDs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2ChConfProfMinDataRateDs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2ChConfProfMinDataRateDs.setUnits("bits/second")
_Xdsl2ChConfProfMinDataRateUs_Type = Unsigned32
_Xdsl2ChConfProfMinDataRateUs_Object = MibTableColumn
xdsl2ChConfProfMinDataRateUs = _Xdsl2ChConfProfMinDataRateUs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 2, 1, 1, 3),
    _Xdsl2ChConfProfMinDataRateUs_Type()
)
xdsl2ChConfProfMinDataRateUs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2ChConfProfMinDataRateUs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2ChConfProfMinDataRateUs.setUnits("bits/second")
_Xdsl2ChConfProfMinResDataRateDs_Type = Unsigned32
_Xdsl2ChConfProfMinResDataRateDs_Object = MibTableColumn
xdsl2ChConfProfMinResDataRateDs = _Xdsl2ChConfProfMinResDataRateDs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 2, 1, 1, 4),
    _Xdsl2ChConfProfMinResDataRateDs_Type()
)
xdsl2ChConfProfMinResDataRateDs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2ChConfProfMinResDataRateDs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2ChConfProfMinResDataRateDs.setUnits("bits/second")
_Xdsl2ChConfProfMinResDataRateUs_Type = Unsigned32
_Xdsl2ChConfProfMinResDataRateUs_Object = MibTableColumn
xdsl2ChConfProfMinResDataRateUs = _Xdsl2ChConfProfMinResDataRateUs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 2, 1, 1, 5),
    _Xdsl2ChConfProfMinResDataRateUs_Type()
)
xdsl2ChConfProfMinResDataRateUs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2ChConfProfMinResDataRateUs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2ChConfProfMinResDataRateUs.setUnits("bits/second")
_Xdsl2ChConfProfMaxDataRateDs_Type = Unsigned32
_Xdsl2ChConfProfMaxDataRateDs_Object = MibTableColumn
xdsl2ChConfProfMaxDataRateDs = _Xdsl2ChConfProfMaxDataRateDs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 2, 1, 1, 6),
    _Xdsl2ChConfProfMaxDataRateDs_Type()
)
xdsl2ChConfProfMaxDataRateDs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2ChConfProfMaxDataRateDs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2ChConfProfMaxDataRateDs.setUnits("bits/second")
_Xdsl2ChConfProfMaxDataRateUs_Type = Unsigned32
_Xdsl2ChConfProfMaxDataRateUs_Object = MibTableColumn
xdsl2ChConfProfMaxDataRateUs = _Xdsl2ChConfProfMaxDataRateUs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 2, 1, 1, 7),
    _Xdsl2ChConfProfMaxDataRateUs_Type()
)
xdsl2ChConfProfMaxDataRateUs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2ChConfProfMaxDataRateUs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2ChConfProfMaxDataRateUs.setUnits("bits/second")
_Xdsl2ChConfProfMinDataRateLowPwrDs_Type = Unsigned32
_Xdsl2ChConfProfMinDataRateLowPwrDs_Object = MibTableColumn
xdsl2ChConfProfMinDataRateLowPwrDs = _Xdsl2ChConfProfMinDataRateLowPwrDs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 2, 1, 1, 8),
    _Xdsl2ChConfProfMinDataRateLowPwrDs_Type()
)
xdsl2ChConfProfMinDataRateLowPwrDs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2ChConfProfMinDataRateLowPwrDs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2ChConfProfMinDataRateLowPwrDs.setUnits("bits/second")
_Xdsl2ChConfProfMinDataRateLowPwrUs_Type = Unsigned32
_Xdsl2ChConfProfMinDataRateLowPwrUs_Object = MibTableColumn
xdsl2ChConfProfMinDataRateLowPwrUs = _Xdsl2ChConfProfMinDataRateLowPwrUs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 2, 1, 1, 9),
    _Xdsl2ChConfProfMinDataRateLowPwrUs_Type()
)
xdsl2ChConfProfMinDataRateLowPwrUs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2ChConfProfMinDataRateLowPwrUs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2ChConfProfMinDataRateLowPwrUs.setUnits("bits/second")


class _Xdsl2ChConfProfMaxDelayDs_Type(Unsigned32):
    """Custom type xdsl2ChConfProfMaxDelayDs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Xdsl2ChConfProfMaxDelayDs_Type.__name__ = "Unsigned32"
_Xdsl2ChConfProfMaxDelayDs_Object = MibTableColumn
xdsl2ChConfProfMaxDelayDs = _Xdsl2ChConfProfMaxDelayDs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 2, 1, 1, 10),
    _Xdsl2ChConfProfMaxDelayDs_Type()
)
xdsl2ChConfProfMaxDelayDs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2ChConfProfMaxDelayDs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2ChConfProfMaxDelayDs.setUnits("milliseconds")


class _Xdsl2ChConfProfMaxDelayUs_Type(Unsigned32):
    """Custom type xdsl2ChConfProfMaxDelayUs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Xdsl2ChConfProfMaxDelayUs_Type.__name__ = "Unsigned32"
_Xdsl2ChConfProfMaxDelayUs_Object = MibTableColumn
xdsl2ChConfProfMaxDelayUs = _Xdsl2ChConfProfMaxDelayUs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 2, 1, 1, 11),
    _Xdsl2ChConfProfMaxDelayUs_Type()
)
xdsl2ChConfProfMaxDelayUs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2ChConfProfMaxDelayUs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2ChConfProfMaxDelayUs.setUnits("milliseconds")


class _Xdsl2ChConfProfMinProtectionDs_Type(Xdsl2SymbolProtection):
    """Custom type xdsl2ChConfProfMinProtectionDs based on Xdsl2SymbolProtection"""


_Xdsl2ChConfProfMinProtectionDs_Object = MibTableColumn
xdsl2ChConfProfMinProtectionDs = _Xdsl2ChConfProfMinProtectionDs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 2, 1, 1, 12),
    _Xdsl2ChConfProfMinProtectionDs_Type()
)
xdsl2ChConfProfMinProtectionDs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2ChConfProfMinProtectionDs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2ChConfProfMinProtectionDs.setUnits("symbols")


class _Xdsl2ChConfProfMinProtectionUs_Type(Xdsl2SymbolProtection):
    """Custom type xdsl2ChConfProfMinProtectionUs based on Xdsl2SymbolProtection"""


_Xdsl2ChConfProfMinProtectionUs_Object = MibTableColumn
xdsl2ChConfProfMinProtectionUs = _Xdsl2ChConfProfMinProtectionUs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 2, 1, 1, 13),
    _Xdsl2ChConfProfMinProtectionUs_Type()
)
xdsl2ChConfProfMinProtectionUs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2ChConfProfMinProtectionUs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2ChConfProfMinProtectionUs.setUnits("symbols")


class _Xdsl2ChConfProfMinProtection8Ds_Type(Xdsl2SymbolProtection8):
    """Custom type xdsl2ChConfProfMinProtection8Ds based on Xdsl2SymbolProtection8"""


_Xdsl2ChConfProfMinProtection8Ds_Object = MibTableColumn
xdsl2ChConfProfMinProtection8Ds = _Xdsl2ChConfProfMinProtection8Ds_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 2, 1, 1, 14),
    _Xdsl2ChConfProfMinProtection8Ds_Type()
)
xdsl2ChConfProfMinProtection8Ds.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2ChConfProfMinProtection8Ds.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2ChConfProfMinProtection8Ds.setUnits("symbols")


class _Xdsl2ChConfProfMinProtection8Us_Type(Xdsl2SymbolProtection8):
    """Custom type xdsl2ChConfProfMinProtection8Us based on Xdsl2SymbolProtection8"""


_Xdsl2ChConfProfMinProtection8Us_Object = MibTableColumn
xdsl2ChConfProfMinProtection8Us = _Xdsl2ChConfProfMinProtection8Us_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 2, 1, 1, 15),
    _Xdsl2ChConfProfMinProtection8Us_Type()
)
xdsl2ChConfProfMinProtection8Us.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2ChConfProfMinProtection8Us.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2ChConfProfMinProtection8Us.setUnits("symbols")


class _Xdsl2ChConfProfMaxBerDs_Type(Xdsl2MaxBer):
    """Custom type xdsl2ChConfProfMaxBerDs based on Xdsl2MaxBer"""


_Xdsl2ChConfProfMaxBerDs_Object = MibTableColumn
xdsl2ChConfProfMaxBerDs = _Xdsl2ChConfProfMaxBerDs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 2, 1, 1, 16),
    _Xdsl2ChConfProfMaxBerDs_Type()
)
xdsl2ChConfProfMaxBerDs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2ChConfProfMaxBerDs.setStatus("current")


class _Xdsl2ChConfProfMaxBerUs_Type(Xdsl2MaxBer):
    """Custom type xdsl2ChConfProfMaxBerUs based on Xdsl2MaxBer"""


_Xdsl2ChConfProfMaxBerUs_Object = MibTableColumn
xdsl2ChConfProfMaxBerUs = _Xdsl2ChConfProfMaxBerUs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 2, 1, 1, 17),
    _Xdsl2ChConfProfMaxBerUs_Type()
)
xdsl2ChConfProfMaxBerUs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2ChConfProfMaxBerUs.setStatus("current")
_Xdsl2ChConfProfUsDataRateDs_Type = Unsigned32
_Xdsl2ChConfProfUsDataRateDs_Object = MibTableColumn
xdsl2ChConfProfUsDataRateDs = _Xdsl2ChConfProfUsDataRateDs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 2, 1, 1, 18),
    _Xdsl2ChConfProfUsDataRateDs_Type()
)
xdsl2ChConfProfUsDataRateDs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2ChConfProfUsDataRateDs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2ChConfProfUsDataRateDs.setUnits("bits/second")
_Xdsl2ChConfProfDsDataRateDs_Type = Unsigned32
_Xdsl2ChConfProfDsDataRateDs_Object = MibTableColumn
xdsl2ChConfProfDsDataRateDs = _Xdsl2ChConfProfDsDataRateDs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 2, 1, 1, 19),
    _Xdsl2ChConfProfDsDataRateDs_Type()
)
xdsl2ChConfProfDsDataRateDs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2ChConfProfDsDataRateDs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2ChConfProfDsDataRateDs.setUnits("bits/second")
_Xdsl2ChConfProfUsDataRateUs_Type = Unsigned32
_Xdsl2ChConfProfUsDataRateUs_Object = MibTableColumn
xdsl2ChConfProfUsDataRateUs = _Xdsl2ChConfProfUsDataRateUs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 2, 1, 1, 20),
    _Xdsl2ChConfProfUsDataRateUs_Type()
)
xdsl2ChConfProfUsDataRateUs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2ChConfProfUsDataRateUs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2ChConfProfUsDataRateUs.setUnits("bits/second")
_Xdsl2ChConfProfDsDataRateUs_Type = Unsigned32
_Xdsl2ChConfProfDsDataRateUs_Object = MibTableColumn
xdsl2ChConfProfDsDataRateUs = _Xdsl2ChConfProfDsDataRateUs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 2, 1, 1, 21),
    _Xdsl2ChConfProfDsDataRateUs_Type()
)
xdsl2ChConfProfDsDataRateUs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2ChConfProfDsDataRateUs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2ChConfProfDsDataRateUs.setUnits("bits/second")


class _Xdsl2ChConfProfImaEnabled_Type(TruthValue):
    """Custom type xdsl2ChConfProfImaEnabled based on TruthValue"""


_Xdsl2ChConfProfImaEnabled_Object = MibTableColumn
xdsl2ChConfProfImaEnabled = _Xdsl2ChConfProfImaEnabled_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 2, 1, 1, 22),
    _Xdsl2ChConfProfImaEnabled_Type()
)
xdsl2ChConfProfImaEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2ChConfProfImaEnabled.setStatus("current")


class _Xdsl2ChConfProfMaxDelayVar_Type(Unsigned32):
    """Custom type xdsl2ChConfProfMaxDelayVar based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Xdsl2ChConfProfMaxDelayVar_Type.__name__ = "Unsigned32"
_Xdsl2ChConfProfMaxDelayVar_Object = MibTableColumn
xdsl2ChConfProfMaxDelayVar = _Xdsl2ChConfProfMaxDelayVar_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 2, 1, 1, 23),
    _Xdsl2ChConfProfMaxDelayVar_Type()
)
xdsl2ChConfProfMaxDelayVar.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2ChConfProfMaxDelayVar.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2ChConfProfMaxDelayVar.setUnits("0.1 milliseconds")


class _Xdsl2ChConfProfInitPolicy_Type(Xdsl2ChInitPolicy):
    """Custom type xdsl2ChConfProfInitPolicy based on Xdsl2ChInitPolicy"""


_Xdsl2ChConfProfInitPolicy_Object = MibTableColumn
xdsl2ChConfProfInitPolicy = _Xdsl2ChConfProfInitPolicy_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 2, 1, 1, 24),
    _Xdsl2ChConfProfInitPolicy_Type()
)
xdsl2ChConfProfInitPolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2ChConfProfInitPolicy.setStatus("current")
_Xdsl2ChConfProfRowStatus_Type = RowStatus
_Xdsl2ChConfProfRowStatus_Object = MibTableColumn
xdsl2ChConfProfRowStatus = _Xdsl2ChConfProfRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 2, 1, 1, 25),
    _Xdsl2ChConfProfRowStatus_Type()
)
xdsl2ChConfProfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2ChConfProfRowStatus.setStatus("current")
_Xdsl2ProfileAlarmConf_ObjectIdentity = ObjectIdentity
xdsl2ProfileAlarmConf = _Xdsl2ProfileAlarmConf_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 3)
)
_Xdsl2LineAlarmConfTemplateTable_Object = MibTable
xdsl2LineAlarmConfTemplateTable = _Xdsl2LineAlarmConfTemplateTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 3, 1)
)
if mibBuilder.loadTexts:
    xdsl2LineAlarmConfTemplateTable.setStatus("current")
_Xdsl2LineAlarmConfTemplateEntry_Object = MibTableRow
xdsl2LineAlarmConfTemplateEntry = _Xdsl2LineAlarmConfTemplateEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 3, 1, 1)
)
xdsl2LineAlarmConfTemplateEntry.setIndexNames(
    (0, "VDSL2-LINE-MIB", "xdsl2LAlarmConfTempTemplateName"),
)
if mibBuilder.loadTexts:
    xdsl2LineAlarmConfTemplateEntry.setStatus("current")


class _Xdsl2LAlarmConfTempTemplateName_Type(SnmpAdminString):
    """Custom type xdsl2LAlarmConfTempTemplateName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Xdsl2LAlarmConfTempTemplateName_Type.__name__ = "SnmpAdminString"
_Xdsl2LAlarmConfTempTemplateName_Object = MibTableColumn
xdsl2LAlarmConfTempTemplateName = _Xdsl2LAlarmConfTempTemplateName_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 3, 1, 1, 1),
    _Xdsl2LAlarmConfTempTemplateName_Type()
)
xdsl2LAlarmConfTempTemplateName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xdsl2LAlarmConfTempTemplateName.setStatus("current")


class _Xdsl2LAlarmConfTempLineProfile_Type(SnmpAdminString):
    """Custom type xdsl2LAlarmConfTempLineProfile based on SnmpAdminString"""
    defaultValue = OctetString("DEFVAL")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Xdsl2LAlarmConfTempLineProfile_Type.__name__ = "SnmpAdminString"
_Xdsl2LAlarmConfTempLineProfile_Object = MibTableColumn
xdsl2LAlarmConfTempLineProfile = _Xdsl2LAlarmConfTempLineProfile_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 3, 1, 1, 2),
    _Xdsl2LAlarmConfTempLineProfile_Type()
)
xdsl2LAlarmConfTempLineProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LAlarmConfTempLineProfile.setStatus("current")


class _Xdsl2LAlarmConfTempChan1ConfProfile_Type(SnmpAdminString):
    """Custom type xdsl2LAlarmConfTempChan1ConfProfile based on SnmpAdminString"""
    defaultValue = OctetString("DEFVAL")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Xdsl2LAlarmConfTempChan1ConfProfile_Type.__name__ = "SnmpAdminString"
_Xdsl2LAlarmConfTempChan1ConfProfile_Object = MibTableColumn
xdsl2LAlarmConfTempChan1ConfProfile = _Xdsl2LAlarmConfTempChan1ConfProfile_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 3, 1, 1, 3),
    _Xdsl2LAlarmConfTempChan1ConfProfile_Type()
)
xdsl2LAlarmConfTempChan1ConfProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LAlarmConfTempChan1ConfProfile.setStatus("current")


class _Xdsl2LAlarmConfTempChan2ConfProfile_Type(SnmpAdminString):
    """Custom type xdsl2LAlarmConfTempChan2ConfProfile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Xdsl2LAlarmConfTempChan2ConfProfile_Type.__name__ = "SnmpAdminString"
_Xdsl2LAlarmConfTempChan2ConfProfile_Object = MibTableColumn
xdsl2LAlarmConfTempChan2ConfProfile = _Xdsl2LAlarmConfTempChan2ConfProfile_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 3, 1, 1, 4),
    _Xdsl2LAlarmConfTempChan2ConfProfile_Type()
)
xdsl2LAlarmConfTempChan2ConfProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LAlarmConfTempChan2ConfProfile.setStatus("current")


class _Xdsl2LAlarmConfTempChan3ConfProfile_Type(SnmpAdminString):
    """Custom type xdsl2LAlarmConfTempChan3ConfProfile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Xdsl2LAlarmConfTempChan3ConfProfile_Type.__name__ = "SnmpAdminString"
_Xdsl2LAlarmConfTempChan3ConfProfile_Object = MibTableColumn
xdsl2LAlarmConfTempChan3ConfProfile = _Xdsl2LAlarmConfTempChan3ConfProfile_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 3, 1, 1, 5),
    _Xdsl2LAlarmConfTempChan3ConfProfile_Type()
)
xdsl2LAlarmConfTempChan3ConfProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LAlarmConfTempChan3ConfProfile.setStatus("current")


class _Xdsl2LAlarmConfTempChan4ConfProfile_Type(SnmpAdminString):
    """Custom type xdsl2LAlarmConfTempChan4ConfProfile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Xdsl2LAlarmConfTempChan4ConfProfile_Type.__name__ = "SnmpAdminString"
_Xdsl2LAlarmConfTempChan4ConfProfile_Object = MibTableColumn
xdsl2LAlarmConfTempChan4ConfProfile = _Xdsl2LAlarmConfTempChan4ConfProfile_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 3, 1, 1, 6),
    _Xdsl2LAlarmConfTempChan4ConfProfile_Type()
)
xdsl2LAlarmConfTempChan4ConfProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LAlarmConfTempChan4ConfProfile.setStatus("current")
_Xdsl2LAlarmConfTempRowStatus_Type = RowStatus
_Xdsl2LAlarmConfTempRowStatus_Object = MibTableColumn
xdsl2LAlarmConfTempRowStatus = _Xdsl2LAlarmConfTempRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 3, 1, 1, 7),
    _Xdsl2LAlarmConfTempRowStatus_Type()
)
xdsl2LAlarmConfTempRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LAlarmConfTempRowStatus.setStatus("current")
_Xdsl2LineAlarmConfProfileTable_Object = MibTable
xdsl2LineAlarmConfProfileTable = _Xdsl2LineAlarmConfProfileTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 3, 2)
)
if mibBuilder.loadTexts:
    xdsl2LineAlarmConfProfileTable.setStatus("current")
_Xdsl2LineAlarmConfProfileEntry_Object = MibTableRow
xdsl2LineAlarmConfProfileEntry = _Xdsl2LineAlarmConfProfileEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 3, 2, 1)
)
xdsl2LineAlarmConfProfileEntry.setIndexNames(
    (0, "VDSL2-LINE-MIB", "xdsl2LineAlarmConfProfileName"),
)
if mibBuilder.loadTexts:
    xdsl2LineAlarmConfProfileEntry.setStatus("current")


class _Xdsl2LineAlarmConfProfileName_Type(SnmpAdminString):
    """Custom type xdsl2LineAlarmConfProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Xdsl2LineAlarmConfProfileName_Type.__name__ = "SnmpAdminString"
_Xdsl2LineAlarmConfProfileName_Object = MibTableColumn
xdsl2LineAlarmConfProfileName = _Xdsl2LineAlarmConfProfileName_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 3, 2, 1, 1),
    _Xdsl2LineAlarmConfProfileName_Type()
)
xdsl2LineAlarmConfProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xdsl2LineAlarmConfProfileName.setStatus("current")


class _Xdsl2LineAlarmConfProfileXtucThresh15MinFecs_Type(HCPerfIntervalThreshold):
    """Custom type xdsl2LineAlarmConfProfileXtucThresh15MinFecs based on HCPerfIntervalThreshold"""
    defaultValue = 0


_Xdsl2LineAlarmConfProfileXtucThresh15MinFecs_Object = MibTableColumn
xdsl2LineAlarmConfProfileXtucThresh15MinFecs = _Xdsl2LineAlarmConfProfileXtucThresh15MinFecs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 3, 2, 1, 2),
    _Xdsl2LineAlarmConfProfileXtucThresh15MinFecs_Type()
)
xdsl2LineAlarmConfProfileXtucThresh15MinFecs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LineAlarmConfProfileXtucThresh15MinFecs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LineAlarmConfProfileXtucThresh15MinFecs.setUnits("seconds")


class _Xdsl2LineAlarmConfProfileXtucThresh15MinEs_Type(HCPerfIntervalThreshold):
    """Custom type xdsl2LineAlarmConfProfileXtucThresh15MinEs based on HCPerfIntervalThreshold"""
    defaultValue = 0


_Xdsl2LineAlarmConfProfileXtucThresh15MinEs_Object = MibTableColumn
xdsl2LineAlarmConfProfileXtucThresh15MinEs = _Xdsl2LineAlarmConfProfileXtucThresh15MinEs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 3, 2, 1, 3),
    _Xdsl2LineAlarmConfProfileXtucThresh15MinEs_Type()
)
xdsl2LineAlarmConfProfileXtucThresh15MinEs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LineAlarmConfProfileXtucThresh15MinEs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LineAlarmConfProfileXtucThresh15MinEs.setUnits("seconds")


class _Xdsl2LineAlarmConfProfileXtucThresh15MinSes_Type(HCPerfIntervalThreshold):
    """Custom type xdsl2LineAlarmConfProfileXtucThresh15MinSes based on HCPerfIntervalThreshold"""
    defaultValue = 0


_Xdsl2LineAlarmConfProfileXtucThresh15MinSes_Object = MibTableColumn
xdsl2LineAlarmConfProfileXtucThresh15MinSes = _Xdsl2LineAlarmConfProfileXtucThresh15MinSes_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 3, 2, 1, 4),
    _Xdsl2LineAlarmConfProfileXtucThresh15MinSes_Type()
)
xdsl2LineAlarmConfProfileXtucThresh15MinSes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LineAlarmConfProfileXtucThresh15MinSes.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LineAlarmConfProfileXtucThresh15MinSes.setUnits("seconds")


class _Xdsl2LineAlarmConfProfileXtucThresh15MinLoss_Type(HCPerfIntervalThreshold):
    """Custom type xdsl2LineAlarmConfProfileXtucThresh15MinLoss based on HCPerfIntervalThreshold"""
    defaultValue = 0


_Xdsl2LineAlarmConfProfileXtucThresh15MinLoss_Object = MibTableColumn
xdsl2LineAlarmConfProfileXtucThresh15MinLoss = _Xdsl2LineAlarmConfProfileXtucThresh15MinLoss_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 3, 2, 1, 5),
    _Xdsl2LineAlarmConfProfileXtucThresh15MinLoss_Type()
)
xdsl2LineAlarmConfProfileXtucThresh15MinLoss.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LineAlarmConfProfileXtucThresh15MinLoss.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LineAlarmConfProfileXtucThresh15MinLoss.setUnits("seconds")


class _Xdsl2LineAlarmConfProfileXtucThresh15MinUas_Type(HCPerfIntervalThreshold):
    """Custom type xdsl2LineAlarmConfProfileXtucThresh15MinUas based on HCPerfIntervalThreshold"""
    defaultValue = 0


_Xdsl2LineAlarmConfProfileXtucThresh15MinUas_Object = MibTableColumn
xdsl2LineAlarmConfProfileXtucThresh15MinUas = _Xdsl2LineAlarmConfProfileXtucThresh15MinUas_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 3, 2, 1, 6),
    _Xdsl2LineAlarmConfProfileXtucThresh15MinUas_Type()
)
xdsl2LineAlarmConfProfileXtucThresh15MinUas.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LineAlarmConfProfileXtucThresh15MinUas.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LineAlarmConfProfileXtucThresh15MinUas.setUnits("seconds")


class _Xdsl2LineAlarmConfProfileXturThresh15MinFecs_Type(HCPerfIntervalThreshold):
    """Custom type xdsl2LineAlarmConfProfileXturThresh15MinFecs based on HCPerfIntervalThreshold"""
    defaultValue = 0


_Xdsl2LineAlarmConfProfileXturThresh15MinFecs_Object = MibTableColumn
xdsl2LineAlarmConfProfileXturThresh15MinFecs = _Xdsl2LineAlarmConfProfileXturThresh15MinFecs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 3, 2, 1, 7),
    _Xdsl2LineAlarmConfProfileXturThresh15MinFecs_Type()
)
xdsl2LineAlarmConfProfileXturThresh15MinFecs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LineAlarmConfProfileXturThresh15MinFecs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LineAlarmConfProfileXturThresh15MinFecs.setUnits("seconds")


class _Xdsl2LineAlarmConfProfileXturThresh15MinEs_Type(HCPerfIntervalThreshold):
    """Custom type xdsl2LineAlarmConfProfileXturThresh15MinEs based on HCPerfIntervalThreshold"""
    defaultValue = 0


_Xdsl2LineAlarmConfProfileXturThresh15MinEs_Object = MibTableColumn
xdsl2LineAlarmConfProfileXturThresh15MinEs = _Xdsl2LineAlarmConfProfileXturThresh15MinEs_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 3, 2, 1, 8),
    _Xdsl2LineAlarmConfProfileXturThresh15MinEs_Type()
)
xdsl2LineAlarmConfProfileXturThresh15MinEs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LineAlarmConfProfileXturThresh15MinEs.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LineAlarmConfProfileXturThresh15MinEs.setUnits("seconds")


class _Xdsl2LineAlarmConfProfileXturThresh15MinSes_Type(HCPerfIntervalThreshold):
    """Custom type xdsl2LineAlarmConfProfileXturThresh15MinSes based on HCPerfIntervalThreshold"""
    defaultValue = 0


_Xdsl2LineAlarmConfProfileXturThresh15MinSes_Object = MibTableColumn
xdsl2LineAlarmConfProfileXturThresh15MinSes = _Xdsl2LineAlarmConfProfileXturThresh15MinSes_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 3, 2, 1, 9),
    _Xdsl2LineAlarmConfProfileXturThresh15MinSes_Type()
)
xdsl2LineAlarmConfProfileXturThresh15MinSes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LineAlarmConfProfileXturThresh15MinSes.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LineAlarmConfProfileXturThresh15MinSes.setUnits("seconds")


class _Xdsl2LineAlarmConfProfileXturThresh15MinLoss_Type(HCPerfIntervalThreshold):
    """Custom type xdsl2LineAlarmConfProfileXturThresh15MinLoss based on HCPerfIntervalThreshold"""
    defaultValue = 0


_Xdsl2LineAlarmConfProfileXturThresh15MinLoss_Object = MibTableColumn
xdsl2LineAlarmConfProfileXturThresh15MinLoss = _Xdsl2LineAlarmConfProfileXturThresh15MinLoss_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 3, 2, 1, 10),
    _Xdsl2LineAlarmConfProfileXturThresh15MinLoss_Type()
)
xdsl2LineAlarmConfProfileXturThresh15MinLoss.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LineAlarmConfProfileXturThresh15MinLoss.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LineAlarmConfProfileXturThresh15MinLoss.setUnits("seconds")


class _Xdsl2LineAlarmConfProfileXturThresh15MinUas_Type(HCPerfIntervalThreshold):
    """Custom type xdsl2LineAlarmConfProfileXturThresh15MinUas based on HCPerfIntervalThreshold"""
    defaultValue = 0


_Xdsl2LineAlarmConfProfileXturThresh15MinUas_Object = MibTableColumn
xdsl2LineAlarmConfProfileXturThresh15MinUas = _Xdsl2LineAlarmConfProfileXturThresh15MinUas_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 3, 2, 1, 11),
    _Xdsl2LineAlarmConfProfileXturThresh15MinUas_Type()
)
xdsl2LineAlarmConfProfileXturThresh15MinUas.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LineAlarmConfProfileXturThresh15MinUas.setStatus("current")
if mibBuilder.loadTexts:
    xdsl2LineAlarmConfProfileXturThresh15MinUas.setUnits("seconds")


class _Xdsl2LineAlarmConfProfileThresh15MinFailedFullInt_Type(Unsigned32):
    """Custom type xdsl2LineAlarmConfProfileThresh15MinFailedFullInt based on Unsigned32"""
    defaultValue = 0


_Xdsl2LineAlarmConfProfileThresh15MinFailedFullInt_Object = MibTableColumn
xdsl2LineAlarmConfProfileThresh15MinFailedFullInt = _Xdsl2LineAlarmConfProfileThresh15MinFailedFullInt_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 3, 2, 1, 12),
    _Xdsl2LineAlarmConfProfileThresh15MinFailedFullInt_Type()
)
xdsl2LineAlarmConfProfileThresh15MinFailedFullInt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LineAlarmConfProfileThresh15MinFailedFullInt.setStatus("current")


class _Xdsl2LineAlarmConfProfileThresh15MinFailedShrtInt_Type(Unsigned32):
    """Custom type xdsl2LineAlarmConfProfileThresh15MinFailedShrtInt based on Unsigned32"""
    defaultValue = 0


_Xdsl2LineAlarmConfProfileThresh15MinFailedShrtInt_Object = MibTableColumn
xdsl2LineAlarmConfProfileThresh15MinFailedShrtInt = _Xdsl2LineAlarmConfProfileThresh15MinFailedShrtInt_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 3, 2, 1, 13),
    _Xdsl2LineAlarmConfProfileThresh15MinFailedShrtInt_Type()
)
xdsl2LineAlarmConfProfileThresh15MinFailedShrtInt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LineAlarmConfProfileThresh15MinFailedShrtInt.setStatus("current")
_Xdsl2LineAlarmConfProfileRowStatus_Type = RowStatus
_Xdsl2LineAlarmConfProfileRowStatus_Object = MibTableColumn
xdsl2LineAlarmConfProfileRowStatus = _Xdsl2LineAlarmConfProfileRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 3, 2, 1, 14),
    _Xdsl2LineAlarmConfProfileRowStatus_Type()
)
xdsl2LineAlarmConfProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2LineAlarmConfProfileRowStatus.setStatus("current")
_Xdsl2ChAlarmConfProfileTable_Object = MibTable
xdsl2ChAlarmConfProfileTable = _Xdsl2ChAlarmConfProfileTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 3, 3)
)
if mibBuilder.loadTexts:
    xdsl2ChAlarmConfProfileTable.setStatus("current")
_Xdsl2ChAlarmConfProfileEntry_Object = MibTableRow
xdsl2ChAlarmConfProfileEntry = _Xdsl2ChAlarmConfProfileEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 3, 3, 1)
)
xdsl2ChAlarmConfProfileEntry.setIndexNames(
    (0, "VDSL2-LINE-MIB", "xdsl2ChAlarmConfProfileName"),
)
if mibBuilder.loadTexts:
    xdsl2ChAlarmConfProfileEntry.setStatus("current")


class _Xdsl2ChAlarmConfProfileName_Type(SnmpAdminString):
    """Custom type xdsl2ChAlarmConfProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Xdsl2ChAlarmConfProfileName_Type.__name__ = "SnmpAdminString"
_Xdsl2ChAlarmConfProfileName_Object = MibTableColumn
xdsl2ChAlarmConfProfileName = _Xdsl2ChAlarmConfProfileName_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 3, 3, 1, 1),
    _Xdsl2ChAlarmConfProfileName_Type()
)
xdsl2ChAlarmConfProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xdsl2ChAlarmConfProfileName.setStatus("current")


class _Xdsl2ChAlarmConfProfileXtucThresh15MinCodingViolations_Type(Unsigned32):
    """Custom type xdsl2ChAlarmConfProfileXtucThresh15MinCodingViolations based on Unsigned32"""
    defaultValue = 0


_Xdsl2ChAlarmConfProfileXtucThresh15MinCodingViolations_Object = MibTableColumn
xdsl2ChAlarmConfProfileXtucThresh15MinCodingViolations = _Xdsl2ChAlarmConfProfileXtucThresh15MinCodingViolations_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 3, 3, 1, 2),
    _Xdsl2ChAlarmConfProfileXtucThresh15MinCodingViolations_Type()
)
xdsl2ChAlarmConfProfileXtucThresh15MinCodingViolations.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2ChAlarmConfProfileXtucThresh15MinCodingViolations.setStatus("current")


class _Xdsl2ChAlarmConfProfileXtucThresh15MinCorrected_Type(Unsigned32):
    """Custom type xdsl2ChAlarmConfProfileXtucThresh15MinCorrected based on Unsigned32"""
    defaultValue = 0


_Xdsl2ChAlarmConfProfileXtucThresh15MinCorrected_Object = MibTableColumn
xdsl2ChAlarmConfProfileXtucThresh15MinCorrected = _Xdsl2ChAlarmConfProfileXtucThresh15MinCorrected_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 3, 3, 1, 3),
    _Xdsl2ChAlarmConfProfileXtucThresh15MinCorrected_Type()
)
xdsl2ChAlarmConfProfileXtucThresh15MinCorrected.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2ChAlarmConfProfileXtucThresh15MinCorrected.setStatus("current")


class _Xdsl2ChAlarmConfProfileXturThresh15MinCodingViolations_Type(Unsigned32):
    """Custom type xdsl2ChAlarmConfProfileXturThresh15MinCodingViolations based on Unsigned32"""
    defaultValue = 0


_Xdsl2ChAlarmConfProfileXturThresh15MinCodingViolations_Object = MibTableColumn
xdsl2ChAlarmConfProfileXturThresh15MinCodingViolations = _Xdsl2ChAlarmConfProfileXturThresh15MinCodingViolations_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 3, 3, 1, 4),
    _Xdsl2ChAlarmConfProfileXturThresh15MinCodingViolations_Type()
)
xdsl2ChAlarmConfProfileXturThresh15MinCodingViolations.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2ChAlarmConfProfileXturThresh15MinCodingViolations.setStatus("current")


class _Xdsl2ChAlarmConfProfileXturThresh15MinCorrected_Type(Unsigned32):
    """Custom type xdsl2ChAlarmConfProfileXturThresh15MinCorrected based on Unsigned32"""
    defaultValue = 0


_Xdsl2ChAlarmConfProfileXturThresh15MinCorrected_Object = MibTableColumn
xdsl2ChAlarmConfProfileXturThresh15MinCorrected = _Xdsl2ChAlarmConfProfileXturThresh15MinCorrected_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 3, 3, 1, 5),
    _Xdsl2ChAlarmConfProfileXturThresh15MinCorrected_Type()
)
xdsl2ChAlarmConfProfileXturThresh15MinCorrected.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2ChAlarmConfProfileXturThresh15MinCorrected.setStatus("current")
_Xdsl2ChAlarmConfProfileRowStatus_Type = RowStatus
_Xdsl2ChAlarmConfProfileRowStatus_Object = MibTableColumn
xdsl2ChAlarmConfProfileRowStatus = _Xdsl2ChAlarmConfProfileRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 5, 3, 3, 1, 6),
    _Xdsl2ChAlarmConfProfileRowStatus_Type()
)
xdsl2ChAlarmConfProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    xdsl2ChAlarmConfProfileRowStatus.setStatus("current")
_Xdsl2Scalar_ObjectIdentity = ObjectIdentity
xdsl2Scalar = _Xdsl2Scalar_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 6)
)
_Xdsl2ScalarSC_ObjectIdentity = ObjectIdentity
xdsl2ScalarSC = _Xdsl2ScalarSC_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 6, 1)
)
_Xdsl2ScalarSCMaxInterfaces_Type = Unsigned32
_Xdsl2ScalarSCMaxInterfaces_Object = MibScalar
xdsl2ScalarSCMaxInterfaces = _Xdsl2ScalarSCMaxInterfaces_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 6, 1, 1),
    _Xdsl2ScalarSCMaxInterfaces_Type()
)
xdsl2ScalarSCMaxInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2ScalarSCMaxInterfaces.setStatus("current")
_Xdsl2ScalarSCAvailInterfaces_Type = Unsigned32
_Xdsl2ScalarSCAvailInterfaces_Object = MibScalar
xdsl2ScalarSCAvailInterfaces = _Xdsl2ScalarSCAvailInterfaces_Object(
    (1, 3, 6, 1, 2, 1, 10, 251, 1, 6, 1, 2),
    _Xdsl2ScalarSCAvailInterfaces_Type()
)
xdsl2ScalarSCAvailInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xdsl2ScalarSCAvailInterfaces.setStatus("current")
_Xdsl2Conformance_ObjectIdentity = ObjectIdentity
xdsl2Conformance = _Xdsl2Conformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 251, 2)
)
_Xdsl2Groups_ObjectIdentity = ObjectIdentity
xdsl2Groups = _Xdsl2Groups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 251, 2, 1)
)
_Xdsl2Compliances_ObjectIdentity = ObjectIdentity
xdsl2Compliances = _Xdsl2Compliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 251, 2, 2)
)

# Managed Objects groups

xdsl2LineGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 251, 2, 1, 1)
)
xdsl2LineGroup.setObjects(
      *(("VDSL2-LINE-MIB", "xdsl2LineConfTemplate"),
        ("VDSL2-LINE-MIB", "xdsl2LineAlarmConfTemplate"),
        ("VDSL2-LINE-MIB", "xdsl2LineCmndConfPmsf"),
        ("VDSL2-LINE-MIB", "xdsl2LineCmndConfLdsf"),
        ("VDSL2-LINE-MIB", "xdsl2LineCmndConfLdsfFailReason"),
        ("VDSL2-LINE-MIB", "xdsl2LineCmndAutomodeColdStart"),
        ("VDSL2-LINE-MIB", "xdsl2LineCmndConfReset"),
        ("VDSL2-LINE-MIB", "xdsl2LineStatusXtuTransSys"),
        ("VDSL2-LINE-MIB", "xdsl2LineStatusPwrMngState"),
        ("VDSL2-LINE-MIB", "xdsl2LineStatusInitResult"),
        ("VDSL2-LINE-MIB", "xdsl2LineStatusLastStateDs"),
        ("VDSL2-LINE-MIB", "xdsl2LineStatusLastStateUs"),
        ("VDSL2-LINE-MIB", "xdsl2LineStatusXtur"),
        ("VDSL2-LINE-MIB", "xdsl2LineStatusXtuc"),
        ("VDSL2-LINE-MIB", "xdsl2LineStatusAttainableRateDs"),
        ("VDSL2-LINE-MIB", "xdsl2LineStatusAttainableRateUs"),
        ("VDSL2-LINE-MIB", "xdsl2LineStatusActPsdDs"),
        ("VDSL2-LINE-MIB", "xdsl2LineStatusActPsdUs"),
        ("VDSL2-LINE-MIB", "xdsl2LineStatusActAtpDs"),
        ("VDSL2-LINE-MIB", "xdsl2LineStatusActAtpUs"),
        ("VDSL2-LINE-MIB", "xdsl2LineStatusActProfile"),
        ("VDSL2-LINE-MIB", "xdsl2LineStatusActLimitMask"),
        ("VDSL2-LINE-MIB", "xdsl2LineStatusActUs0Mask"),
        ("VDSL2-LINE-MIB", "xdsl2LineStatusActSnrModeDs"),
        ("VDSL2-LINE-MIB", "xdsl2LineStatusActSnrModeUs"),
        ("VDSL2-LINE-MIB", "xdsl2LineStatusElectricalLength"),
        ("VDSL2-LINE-MIB", "xdsl2LineStatusTssiDs"),
        ("VDSL2-LINE-MIB", "xdsl2LineStatusTssiUs"),
        ("VDSL2-LINE-MIB", "xdsl2LineStatusMrefPsdDs"),
        ("VDSL2-LINE-MIB", "xdsl2LineStatusMrefPsdUs"),
        ("VDSL2-LINE-MIB", "xdsl2LineStatusTrellisDs"),
        ("VDSL2-LINE-MIB", "xdsl2LineStatusTrellisUs"),
        ("VDSL2-LINE-MIB", "xdsl2LineStatusActualCe"),
        ("VDSL2-LINE-MIB", "xdsl2LineBandStatusLnAtten"),
        ("VDSL2-LINE-MIB", "xdsl2LineBandStatusSigAtten"),
        ("VDSL2-LINE-MIB", "xdsl2LineBandStatusSnrMargin"))
)
if mibBuilder.loadTexts:
    xdsl2LineGroup.setStatus("current")

xdsl2LineFallbackGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 251, 2, 1, 2)
)
xdsl2LineFallbackGroup.setObjects(
      *(("VDSL2-LINE-MIB", "xdsl2LineConfFallbackTemplate"),
        ("VDSL2-LINE-MIB", "xdsl2LineStatusActTemplate"))
)
if mibBuilder.loadTexts:
    xdsl2LineFallbackGroup.setStatus("current")

xdsl2LineBpscGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 251, 2, 1, 3)
)
xdsl2LineBpscGroup.setObjects(
      *(("VDSL2-LINE-MIB", "xdsl2LineCmndConfBpsc"),
        ("VDSL2-LINE-MIB", "xdsl2LineCmndConfBpscFailReason"),
        ("VDSL2-LINE-MIB", "xdsl2LineCmndConfBpscRequests"))
)
if mibBuilder.loadTexts:
    xdsl2LineBpscGroup.setStatus("current")

xdsl2LineSegmentGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 251, 2, 1, 4)
)
xdsl2LineSegmentGroup.setObjects(
      *(("VDSL2-LINE-MIB", "xdsl2LineSegmentBitsAlloc"),
        ("VDSL2-LINE-MIB", "xdsl2LineSegmentRowStatus"))
)
if mibBuilder.loadTexts:
    xdsl2LineSegmentGroup.setStatus("current")

xdsl2ChannelStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 251, 2, 1, 5)
)
xdsl2ChannelStatusGroup.setObjects(
      *(("VDSL2-LINE-MIB", "xdsl2ChStatusActDataRate"),
        ("VDSL2-LINE-MIB", "xdsl2ChStatusPrevDataRate"),
        ("VDSL2-LINE-MIB", "xdsl2ChStatusActDelay"),
        ("VDSL2-LINE-MIB", "xdsl2ChStatusActInp"),
        ("VDSL2-LINE-MIB", "xdsl2ChStatusInpReport"),
        ("VDSL2-LINE-MIB", "xdsl2ChStatusNFec"),
        ("VDSL2-LINE-MIB", "xdsl2ChStatusRFec"),
        ("VDSL2-LINE-MIB", "xdsl2ChStatusLSymb"),
        ("VDSL2-LINE-MIB", "xdsl2ChStatusIntlvDepth"),
        ("VDSL2-LINE-MIB", "xdsl2ChStatusIntlvBlock"),
        ("VDSL2-LINE-MIB", "xdsl2ChStatusLPath"))
)
if mibBuilder.loadTexts:
    xdsl2ChannelStatusGroup.setStatus("current")

xdsl2ChannelStatusAtmGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 251, 2, 1, 6)
)
xdsl2ChannelStatusAtmGroup.setObjects(
    ("VDSL2-LINE-MIB", "xdsl2ChStatusAtmStatus")
)
if mibBuilder.loadTexts:
    xdsl2ChannelStatusAtmGroup.setStatus("current")

xdsl2ChannelStatusPtmGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 251, 2, 1, 7)
)
xdsl2ChannelStatusPtmGroup.setObjects(
    ("VDSL2-LINE-MIB", "xdsl2ChStatusPtmStatus")
)
if mibBuilder.loadTexts:
    xdsl2ChannelStatusPtmGroup.setStatus("current")

xdsl2SCStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 251, 2, 1, 8)
)
xdsl2SCStatusGroup.setObjects(
      *(("VDSL2-LINE-MIB", "xdsl2SCStatusLinScale"),
        ("VDSL2-LINE-MIB", "xdsl2SCStatusLinScGroupSize"),
        ("VDSL2-LINE-MIB", "xdsl2SCStatusLogMt"),
        ("VDSL2-LINE-MIB", "xdsl2SCStatusLogScGroupSize"),
        ("VDSL2-LINE-MIB", "xdsl2SCStatusQlnMt"),
        ("VDSL2-LINE-MIB", "xdsl2SCStatusQlnScGroupSize"),
        ("VDSL2-LINE-MIB", "xdsl2SCStatusSnrMtime"),
        ("VDSL2-LINE-MIB", "xdsl2SCStatusSnrScGroupSize"),
        ("VDSL2-LINE-MIB", "xdsl2SCStatusBandLnAtten"),
        ("VDSL2-LINE-MIB", "xdsl2SCStatusBandSigAtten"),
        ("VDSL2-LINE-MIB", "xdsl2SCStatusAttainableRate"),
        ("VDSL2-LINE-MIB", "xdsl2SCStatusRowStatus"),
        ("VDSL2-LINE-MIB", "xdsl2SCStatusSegmentLinReal"),
        ("VDSL2-LINE-MIB", "xdsl2SCStatusSegmentLinImg"),
        ("VDSL2-LINE-MIB", "xdsl2SCStatusSegmentLog"),
        ("VDSL2-LINE-MIB", "xdsl2SCStatusSegmentQln"),
        ("VDSL2-LINE-MIB", "xdsl2SCStatusSegmentSnr"),
        ("VDSL2-LINE-MIB", "xdsl2SCStatusSegmentBitsAlloc"),
        ("VDSL2-LINE-MIB", "xdsl2SCStatusSegmentGainAlloc"))
)
if mibBuilder.loadTexts:
    xdsl2SCStatusGroup.setStatus("current")

xdsl2LineInventoryGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 251, 2, 1, 9)
)
xdsl2LineInventoryGroup.setObjects(
      *(("VDSL2-LINE-MIB", "xdsl2LInvG994VendorId"),
        ("VDSL2-LINE-MIB", "xdsl2LInvSystemVendorId"),
        ("VDSL2-LINE-MIB", "xdsl2LInvVersionNumber"),
        ("VDSL2-LINE-MIB", "xdsl2LInvSerialNumber"),
        ("VDSL2-LINE-MIB", "xdsl2LInvSelfTestResult"),
        ("VDSL2-LINE-MIB", "xdsl2LInvTransmissionCapabilities"))
)
if mibBuilder.loadTexts:
    xdsl2LineInventoryGroup.setStatus("current")

xdsl2LineConfTemplateGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 251, 2, 1, 10)
)
xdsl2LineConfTemplateGroup.setObjects(
      *(("VDSL2-LINE-MIB", "xdsl2LConfTempLineProfile"),
        ("VDSL2-LINE-MIB", "xdsl2LConfTempChan1ConfProfile"),
        ("VDSL2-LINE-MIB", "xdsl2LConfTempChan1RaRatioDs"),
        ("VDSL2-LINE-MIB", "xdsl2LConfTempChan1RaRatioUs"),
        ("VDSL2-LINE-MIB", "xdsl2LConfTempChan2ConfProfile"),
        ("VDSL2-LINE-MIB", "xdsl2LConfTempChan2RaRatioDs"),
        ("VDSL2-LINE-MIB", "xdsl2LConfTempChan2RaRatioUs"),
        ("VDSL2-LINE-MIB", "xdsl2LConfTempChan3ConfProfile"),
        ("VDSL2-LINE-MIB", "xdsl2LConfTempChan3RaRatioDs"),
        ("VDSL2-LINE-MIB", "xdsl2LConfTempChan3RaRatioUs"),
        ("VDSL2-LINE-MIB", "xdsl2LConfTempChan4ConfProfile"),
        ("VDSL2-LINE-MIB", "xdsl2LConfTempChan4RaRatioDs"),
        ("VDSL2-LINE-MIB", "xdsl2LConfTempChan4RaRatioUs"),
        ("VDSL2-LINE-MIB", "xdsl2LConfTempRowStatus"))
)
if mibBuilder.loadTexts:
    xdsl2LineConfTemplateGroup.setStatus("current")

xdsl2LineConfProfGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 251, 2, 1, 11)
)
xdsl2LineConfProfGroup.setObjects(
      *(("VDSL2-LINE-MIB", "xdsl2LConfProfScMaskDs"),
        ("VDSL2-LINE-MIB", "xdsl2LConfProfScMaskUs"),
        ("VDSL2-LINE-MIB", "xdsl2LConfProfVdsl2CarMask"),
        ("VDSL2-LINE-MIB", "xdsl2LConfProfRfiBands"),
        ("VDSL2-LINE-MIB", "xdsl2LConfProfRaModeDs"),
        ("VDSL2-LINE-MIB", "xdsl2LConfProfRaModeUs"),
        ("VDSL2-LINE-MIB", "xdsl2LConfProfTargetSnrmDs"),
        ("VDSL2-LINE-MIB", "xdsl2LConfProfTargetSnrmUs"),
        ("VDSL2-LINE-MIB", "xdsl2LConfProfMaxSnrmDs"),
        ("VDSL2-LINE-MIB", "xdsl2LConfProfMaxSnrmUs"),
        ("VDSL2-LINE-MIB", "xdsl2LConfProfMinSnrmDs"),
        ("VDSL2-LINE-MIB", "xdsl2LConfProfMinSnrmUs"),
        ("VDSL2-LINE-MIB", "xdsl2LConfProfCeFlag"),
        ("VDSL2-LINE-MIB", "xdsl2LConfProfSnrModeDs"),
        ("VDSL2-LINE-MIB", "xdsl2LConfProfSnrModeUs"),
        ("VDSL2-LINE-MIB", "xdsl2LConfProfTxRefVnDs"),
        ("VDSL2-LINE-MIB", "xdsl2LConfProfTxRefVnUs"),
        ("VDSL2-LINE-MIB", "xdsl2LConfProfXtuTransSysEna"),
        ("VDSL2-LINE-MIB", "xdsl2LConfProfPmMode"),
        ("VDSL2-LINE-MIB", "xdsl2LConfProfL0Time"),
        ("VDSL2-LINE-MIB", "xdsl2LConfProfL2Time"),
        ("VDSL2-LINE-MIB", "xdsl2LConfProfL2Atpr"),
        ("VDSL2-LINE-MIB", "xdsl2LConfProfL2Atprt"),
        ("VDSL2-LINE-MIB", "xdsl2LConfProfProfiles"),
        ("VDSL2-LINE-MIB", "xdsl2LConfProfDpboEPsd"),
        ("VDSL2-LINE-MIB", "xdsl2LConfProfDpboEsEL"),
        ("VDSL2-LINE-MIB", "xdsl2LConfProfDpboEsCableModelA"),
        ("VDSL2-LINE-MIB", "xdsl2LConfProfDpboEsCableModelB"),
        ("VDSL2-LINE-MIB", "xdsl2LConfProfDpboEsCableModelC"),
        ("VDSL2-LINE-MIB", "xdsl2LConfProfDpboMus"),
        ("VDSL2-LINE-MIB", "xdsl2LConfProfDpboFMin"),
        ("VDSL2-LINE-MIB", "xdsl2LConfProfDpboFMax"),
        ("VDSL2-LINE-MIB", "xdsl2LConfProfUpboKL"),
        ("VDSL2-LINE-MIB", "xdsl2LConfProfUpboKLF"),
        ("VDSL2-LINE-MIB", "xdsl2LConfProfUs0Mask"),
        ("VDSL2-LINE-MIB", "xdsl2LConfProfForceInp"),
        ("VDSL2-LINE-MIB", "xdsl2LConfProfRowStatus"))
)
if mibBuilder.loadTexts:
    xdsl2LineConfProfGroup.setStatus("current")

xdsl2LineConfProfRaGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 251, 2, 1, 12)
)
xdsl2LineConfProfRaGroup.setObjects(
      *(("VDSL2-LINE-MIB", "xdsl2LConfProfRaUsNrmDs"),
        ("VDSL2-LINE-MIB", "xdsl2LConfProfRaUsNrmUs"),
        ("VDSL2-LINE-MIB", "xdsl2LConfProfRaUsTimeDs"),
        ("VDSL2-LINE-MIB", "xdsl2LConfProfRaUsTimeUs"),
        ("VDSL2-LINE-MIB", "xdsl2LConfProfRaDsNrmDs"),
        ("VDSL2-LINE-MIB", "xdsl2LConfProfRaDsNrmUs"),
        ("VDSL2-LINE-MIB", "xdsl2LConfProfRaDsTimeDs"),
        ("VDSL2-LINE-MIB", "xdsl2LConfProfRaDsTimeUs"))
)
if mibBuilder.loadTexts:
    xdsl2LineConfProfRaGroup.setStatus("current")

xdsl2LineConfProfMsgMinGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 251, 2, 1, 13)
)
xdsl2LineConfProfMsgMinGroup.setObjects(
      *(("VDSL2-LINE-MIB", "xdsl2LConfProfMsgMinUs"),
        ("VDSL2-LINE-MIB", "xdsl2LConfProfMsgMinDs"))
)
if mibBuilder.loadTexts:
    xdsl2LineConfProfMsgMinGroup.setStatus("current")

xdsl2LineConfProfModeSpecGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 251, 2, 1, 14)
)
xdsl2LineConfProfModeSpecGroup.setObjects(
      *(("VDSL2-LINE-MIB", "xdsl2LConfProfMaxNomPsdDs"),
        ("VDSL2-LINE-MIB", "xdsl2LConfProfMaxNomPsdUs"),
        ("VDSL2-LINE-MIB", "xdsl2LConfProfMaxNomAtpDs"),
        ("VDSL2-LINE-MIB", "xdsl2LConfProfMaxNomAtpUs"),
        ("VDSL2-LINE-MIB", "xdsl2LConfProfMaxAggRxPwrUs"),
        ("VDSL2-LINE-MIB", "xdsl2LConfProfPsdMaskDs"),
        ("VDSL2-LINE-MIB", "xdsl2LConfProfPsdMaskUs"),
        ("VDSL2-LINE-MIB", "xdsl2LConfProfPsdMaskSelectUs"),
        ("VDSL2-LINE-MIB", "xdsl2LConfProfClassMask"),
        ("VDSL2-LINE-MIB", "xdsl2LConfProfLimitMask"),
        ("VDSL2-LINE-MIB", "xdsl2LConfProfUs0Disable"),
        ("VDSL2-LINE-MIB", "xdsl2LConfProfModeSpecRowStatus"))
)
if mibBuilder.loadTexts:
    xdsl2LineConfProfModeSpecGroup.setStatus("current")

xdsl2LineConfProfModeSpecBandUsGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 251, 2, 1, 15)
)
xdsl2LineConfProfModeSpecBandUsGroup.setObjects(
      *(("VDSL2-LINE-MIB", "xdsl2LConfProfUpboPsdA"),
        ("VDSL2-LINE-MIB", "xdsl2LConfProfUpboPsdB"),
        ("VDSL2-LINE-MIB", "xdsl2LConfProfModeSpecBandUsRowStatus"))
)
if mibBuilder.loadTexts:
    xdsl2LineConfProfModeSpecBandUsGroup.setStatus("current")

xdsl2ChConfProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 251, 2, 1, 16)
)
xdsl2ChConfProfileGroup.setObjects(
      *(("VDSL2-LINE-MIB", "xdsl2ChConfProfMinDataRateDs"),
        ("VDSL2-LINE-MIB", "xdsl2ChConfProfMinDataRateUs"),
        ("VDSL2-LINE-MIB", "xdsl2ChConfProfMaxDataRateDs"),
        ("VDSL2-LINE-MIB", "xdsl2ChConfProfMaxDataRateUs"),
        ("VDSL2-LINE-MIB", "xdsl2ChConfProfMinDataRateLowPwrDs"),
        ("VDSL2-LINE-MIB", "xdsl2ChConfProfMinDataRateLowPwrUs"),
        ("VDSL2-LINE-MIB", "xdsl2ChConfProfMaxDelayDs"),
        ("VDSL2-LINE-MIB", "xdsl2ChConfProfMaxDelayUs"),
        ("VDSL2-LINE-MIB", "xdsl2ChConfProfMinProtectionDs"),
        ("VDSL2-LINE-MIB", "xdsl2ChConfProfMinProtectionUs"),
        ("VDSL2-LINE-MIB", "xdsl2ChConfProfMinProtection8Ds"),
        ("VDSL2-LINE-MIB", "xdsl2ChConfProfMinProtection8Us"),
        ("VDSL2-LINE-MIB", "xdsl2ChConfProfMaxBerDs"),
        ("VDSL2-LINE-MIB", "xdsl2ChConfProfMaxBerUs"),
        ("VDSL2-LINE-MIB", "xdsl2ChConfProfUsDataRateDs"),
        ("VDSL2-LINE-MIB", "xdsl2ChConfProfDsDataRateDs"),
        ("VDSL2-LINE-MIB", "xdsl2ChConfProfUsDataRateUs"),
        ("VDSL2-LINE-MIB", "xdsl2ChConfProfDsDataRateUs"),
        ("VDSL2-LINE-MIB", "xdsl2ChConfProfRowStatus"))
)
if mibBuilder.loadTexts:
    xdsl2ChConfProfileGroup.setStatus("current")

xdsl2ChConfProfileAtmGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 251, 2, 1, 17)
)
xdsl2ChConfProfileAtmGroup.setObjects(
      *(("VDSL2-LINE-MIB", "xdsl2ChConfProfImaEnabled"),
        ("VDSL2-LINE-MIB", "xdsl2ChStatusAtmStatus"))
)
if mibBuilder.loadTexts:
    xdsl2ChConfProfileAtmGroup.setStatus("current")

xdsl2ChConfProfileMinResGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 251, 2, 1, 18)
)
xdsl2ChConfProfileMinResGroup.setObjects(
      *(("VDSL2-LINE-MIB", "xdsl2ChConfProfMinResDataRateDs"),
        ("VDSL2-LINE-MIB", "xdsl2ChConfProfMinResDataRateUs"))
)
if mibBuilder.loadTexts:
    xdsl2ChConfProfileMinResGroup.setStatus("current")

xdsl2ChConfProfileOptAttrGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 251, 2, 1, 19)
)
xdsl2ChConfProfileOptAttrGroup.setObjects(
      *(("VDSL2-LINE-MIB", "xdsl2ChConfProfMaxDelayVar"),
        ("VDSL2-LINE-MIB", "xdsl2ChConfProfInitPolicy"))
)
if mibBuilder.loadTexts:
    xdsl2ChConfProfileOptAttrGroup.setStatus("current")

xdsl2LineAlarmConfTemplateGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 251, 2, 1, 20)
)
xdsl2LineAlarmConfTemplateGroup.setObjects(
      *(("VDSL2-LINE-MIB", "xdsl2LAlarmConfTempLineProfile"),
        ("VDSL2-LINE-MIB", "xdsl2LAlarmConfTempChan1ConfProfile"),
        ("VDSL2-LINE-MIB", "xdsl2LAlarmConfTempChan2ConfProfile"),
        ("VDSL2-LINE-MIB", "xdsl2LAlarmConfTempChan3ConfProfile"),
        ("VDSL2-LINE-MIB", "xdsl2LAlarmConfTempChan4ConfProfile"),
        ("VDSL2-LINE-MIB", "xdsl2LAlarmConfTempRowStatus"))
)
if mibBuilder.loadTexts:
    xdsl2LineAlarmConfTemplateGroup.setStatus("current")

xdsl2LineAlarmConfProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 251, 2, 1, 21)
)
xdsl2LineAlarmConfProfileGroup.setObjects(
      *(("VDSL2-LINE-MIB", "xdsl2LineAlarmConfProfileXtucThresh15MinFecs"),
        ("VDSL2-LINE-MIB", "xdsl2LineAlarmConfProfileXtucThresh15MinEs"),
        ("VDSL2-LINE-MIB", "xdsl2LineAlarmConfProfileXtucThresh15MinSes"),
        ("VDSL2-LINE-MIB", "xdsl2LineAlarmConfProfileXtucThresh15MinLoss"),
        ("VDSL2-LINE-MIB", "xdsl2LineAlarmConfProfileXtucThresh15MinUas"),
        ("VDSL2-LINE-MIB", "xdsl2LineAlarmConfProfileXturThresh15MinFecs"),
        ("VDSL2-LINE-MIB", "xdsl2LineAlarmConfProfileXturThresh15MinEs"),
        ("VDSL2-LINE-MIB", "xdsl2LineAlarmConfProfileXturThresh15MinSes"),
        ("VDSL2-LINE-MIB", "xdsl2LineAlarmConfProfileXturThresh15MinLoss"),
        ("VDSL2-LINE-MIB", "xdsl2LineAlarmConfProfileXturThresh15MinUas"),
        ("VDSL2-LINE-MIB", "xdsl2LineAlarmConfProfileThresh15MinFailedFullInt"),
        ("VDSL2-LINE-MIB", "xdsl2LineAlarmConfProfileThresh15MinFailedShrtInt"),
        ("VDSL2-LINE-MIB", "xdsl2LineAlarmConfProfileRowStatus"))
)
if mibBuilder.loadTexts:
    xdsl2LineAlarmConfProfileGroup.setStatus("current")

xdsl2ChAlarmConfProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 251, 2, 1, 22)
)
xdsl2ChAlarmConfProfileGroup.setObjects(
      *(("VDSL2-LINE-MIB", "xdsl2ChAlarmConfProfileXtucThresh15MinCodingViolations"),
        ("VDSL2-LINE-MIB", "xdsl2ChAlarmConfProfileXtucThresh15MinCorrected"),
        ("VDSL2-LINE-MIB", "xdsl2ChAlarmConfProfileXturThresh15MinCodingViolations"),
        ("VDSL2-LINE-MIB", "xdsl2ChAlarmConfProfileXturThresh15MinCorrected"),
        ("VDSL2-LINE-MIB", "xdsl2ChAlarmConfProfileRowStatus"))
)
if mibBuilder.loadTexts:
    xdsl2ChAlarmConfProfileGroup.setStatus("current")

xdsl2PMLineCurrGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 251, 2, 1, 23)
)
xdsl2PMLineCurrGroup.setObjects(
      *(("VDSL2-LINE-MIB", "xdsl2PMLCurr15MValidIntervals"),
        ("VDSL2-LINE-MIB", "xdsl2PMLCurr15MInvalidIntervals"),
        ("VDSL2-LINE-MIB", "xdsl2PMLCurr15MTimeElapsed"),
        ("VDSL2-LINE-MIB", "xdsl2PMLCurr15MFecs"),
        ("VDSL2-LINE-MIB", "xdsl2PMLCurr15MEs"),
        ("VDSL2-LINE-MIB", "xdsl2PMLCurr15MSes"),
        ("VDSL2-LINE-MIB", "xdsl2PMLCurr15MLoss"),
        ("VDSL2-LINE-MIB", "xdsl2PMLCurr15MUas"),
        ("VDSL2-LINE-MIB", "xdsl2PMLCurr1DayValidIntervals"),
        ("VDSL2-LINE-MIB", "xdsl2PMLCurr1DayInvalidIntervals"),
        ("VDSL2-LINE-MIB", "xdsl2PMLCurr1DayTimeElapsed"),
        ("VDSL2-LINE-MIB", "xdsl2PMLCurr1DayFecs"),
        ("VDSL2-LINE-MIB", "xdsl2PMLCurr1DayEs"),
        ("VDSL2-LINE-MIB", "xdsl2PMLCurr1DaySes"),
        ("VDSL2-LINE-MIB", "xdsl2PMLCurr1DayLoss"),
        ("VDSL2-LINE-MIB", "xdsl2PMLCurr1DayUas"))
)
if mibBuilder.loadTexts:
    xdsl2PMLineCurrGroup.setStatus("current")

xdsl2PMLineInitCurrGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 251, 2, 1, 24)
)
xdsl2PMLineInitCurrGroup.setObjects(
      *(("VDSL2-LINE-MIB", "xdsl2PMLInitCurr15MValidIntervals"),
        ("VDSL2-LINE-MIB", "xdsl2PMLInitCurr15MInvalidIntervals"),
        ("VDSL2-LINE-MIB", "xdsl2PMLInitCurr15MTimeElapsed"),
        ("VDSL2-LINE-MIB", "xdsl2PMLInitCurr15MFullInits"),
        ("VDSL2-LINE-MIB", "xdsl2PMLInitCurr15MFailedFullInits"),
        ("VDSL2-LINE-MIB", "xdsl2PMLInitCurr1DayValidIntervals"),
        ("VDSL2-LINE-MIB", "xdsl2PMLInitCurr1DayInvalidIntervals"),
        ("VDSL2-LINE-MIB", "xdsl2PMLInitCurr1DayTimeElapsed"),
        ("VDSL2-LINE-MIB", "xdsl2PMLInitCurr1DayFullInits"),
        ("VDSL2-LINE-MIB", "xdsl2PMLInitCurr1DayFailedFullInits"))
)
if mibBuilder.loadTexts:
    xdsl2PMLineInitCurrGroup.setStatus("current")

xdsl2PMLineInitCurrShortGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 251, 2, 1, 25)
)
xdsl2PMLineInitCurrShortGroup.setObjects(
      *(("VDSL2-LINE-MIB", "xdsl2PMLInitCurr15MShortInits"),
        ("VDSL2-LINE-MIB", "xdsl2PMLInitCurr15MFailedShortInits"),
        ("VDSL2-LINE-MIB", "xdsl2PMLInitCurr1DayShortInits"),
        ("VDSL2-LINE-MIB", "xdsl2PMLInitCurr1DayFailedShortInits"))
)
if mibBuilder.loadTexts:
    xdsl2PMLineInitCurrShortGroup.setStatus("current")

xdsl2PMLineHist15MinGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 251, 2, 1, 26)
)
xdsl2PMLineHist15MinGroup.setObjects(
      *(("VDSL2-LINE-MIB", "xdsl2PMLHist15MMonitoredTime"),
        ("VDSL2-LINE-MIB", "xdsl2PMLHist15MFecs"),
        ("VDSL2-LINE-MIB", "xdsl2PMLHist15MEs"),
        ("VDSL2-LINE-MIB", "xdsl2PMLHist15MSes"),
        ("VDSL2-LINE-MIB", "xdsl2PMLHist15MLoss"),
        ("VDSL2-LINE-MIB", "xdsl2PMLHist15MUas"),
        ("VDSL2-LINE-MIB", "xdsl2PMLHist15MValidInterval"))
)
if mibBuilder.loadTexts:
    xdsl2PMLineHist15MinGroup.setStatus("current")

xdsl2PMLineHist1DayGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 251, 2, 1, 27)
)
xdsl2PMLineHist1DayGroup.setObjects(
      *(("VDSL2-LINE-MIB", "xdsl2PMLHist1DMonitoredTime"),
        ("VDSL2-LINE-MIB", "xdsl2PMLHist1DFecs"),
        ("VDSL2-LINE-MIB", "xdsl2PMLHist1DEs"),
        ("VDSL2-LINE-MIB", "xdsl2PMLHist1DSes"),
        ("VDSL2-LINE-MIB", "xdsl2PMLHist1DLoss"),
        ("VDSL2-LINE-MIB", "xdsl2PMLHist1DUas"),
        ("VDSL2-LINE-MIB", "xdsl2PMLHist1DValidInterval"))
)
if mibBuilder.loadTexts:
    xdsl2PMLineHist1DayGroup.setStatus("current")

xdsl2PMLineInitHist15MinGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 251, 2, 1, 28)
)
xdsl2PMLineInitHist15MinGroup.setObjects(
      *(("VDSL2-LINE-MIB", "xdsl2PMLInitHist15MMonitoredTime"),
        ("VDSL2-LINE-MIB", "xdsl2PMLInitHist15MFullInits"),
        ("VDSL2-LINE-MIB", "xdsl2PMLInitHist15MFailedFullInits"),
        ("VDSL2-LINE-MIB", "xdsl2PMLInitHist15MValidInterval"))
)
if mibBuilder.loadTexts:
    xdsl2PMLineInitHist15MinGroup.setStatus("current")

xdsl2PMLineInitHist15MinShortGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 251, 2, 1, 29)
)
xdsl2PMLineInitHist15MinShortGroup.setObjects(
      *(("VDSL2-LINE-MIB", "xdsl2PMLInitHist15MShortInits"),
        ("VDSL2-LINE-MIB", "xdsl2PMLInitHist15MFailedShortInits"))
)
if mibBuilder.loadTexts:
    xdsl2PMLineInitHist15MinShortGroup.setStatus("current")

xdsl2PMLineInitHist1DayGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 251, 2, 1, 30)
)
xdsl2PMLineInitHist1DayGroup.setObjects(
      *(("VDSL2-LINE-MIB", "xdsl2PMLInitHist1DMonitoredTime"),
        ("VDSL2-LINE-MIB", "xdsl2PMLInitHist1DFullInits"),
        ("VDSL2-LINE-MIB", "xdsl2PMLInitHist1DFailedFullInits"),
        ("VDSL2-LINE-MIB", "xdsl2PMLInitHist1DValidInterval"))
)
if mibBuilder.loadTexts:
    xdsl2PMLineInitHist1DayGroup.setStatus("current")

xdsl2PMLineInitHist1DayShortGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 251, 2, 1, 31)
)
xdsl2PMLineInitHist1DayShortGroup.setObjects(
      *(("VDSL2-LINE-MIB", "xdsl2PMLInitHist1DShortInits"),
        ("VDSL2-LINE-MIB", "xdsl2PMLInitHist1DFailedShortInits"))
)
if mibBuilder.loadTexts:
    xdsl2PMLineInitHist1DayShortGroup.setStatus("current")

xdsl2PMChCurrGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 251, 2, 1, 32)
)
xdsl2PMChCurrGroup.setObjects(
      *(("VDSL2-LINE-MIB", "xdsl2PMChCurr15MValidIntervals"),
        ("VDSL2-LINE-MIB", "xdsl2PMChCurr15MInvalidIntervals"),
        ("VDSL2-LINE-MIB", "xdsl2PMChCurr15MTimeElapsed"),
        ("VDSL2-LINE-MIB", "xdsl2PMChCurr15MCodingViolations"),
        ("VDSL2-LINE-MIB", "xdsl2PMChCurr15MCorrectedBlocks"),
        ("VDSL2-LINE-MIB", "xdsl2PMChCurr1DayValidIntervals"),
        ("VDSL2-LINE-MIB", "xdsl2PMChCurr1DayInvalidIntervals"),
        ("VDSL2-LINE-MIB", "xdsl2PMChCurr1DayTimeElapsed"),
        ("VDSL2-LINE-MIB", "xdsl2PMChCurr1DayCodingViolations"),
        ("VDSL2-LINE-MIB", "xdsl2PMChCurr1DayCorrectedBlocks"))
)
if mibBuilder.loadTexts:
    xdsl2PMChCurrGroup.setStatus("current")

xdsl2PMChHist15MinGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 251, 2, 1, 33)
)
xdsl2PMChHist15MinGroup.setObjects(
      *(("VDSL2-LINE-MIB", "xdsl2PMChHist15MMonitoredTime"),
        ("VDSL2-LINE-MIB", "xdsl2PMChHist15MCodingViolations"),
        ("VDSL2-LINE-MIB", "xdsl2PMChHist15MCorrectedBlocks"),
        ("VDSL2-LINE-MIB", "xdsl2PMChHist15MValidInterval"))
)
if mibBuilder.loadTexts:
    xdsl2PMChHist15MinGroup.setStatus("current")

xdsl2PMChHist1DGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 251, 2, 1, 34)
)
xdsl2PMChHist1DGroup.setObjects(
      *(("VDSL2-LINE-MIB", "xdsl2PMChHist1DMonitoredTime"),
        ("VDSL2-LINE-MIB", "xdsl2PMChHist1DCodingViolations"),
        ("VDSL2-LINE-MIB", "xdsl2PMChHist1DCorrectedBlocks"),
        ("VDSL2-LINE-MIB", "xdsl2PMChHist1DValidInterval"))
)
if mibBuilder.loadTexts:
    xdsl2PMChHist1DGroup.setStatus("current")

xdsl2ScalarSCGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 251, 2, 1, 35)
)
xdsl2ScalarSCGroup.setObjects(
      *(("VDSL2-LINE-MIB", "xdsl2ScalarSCMaxInterfaces"),
        ("VDSL2-LINE-MIB", "xdsl2ScalarSCAvailInterfaces"))
)
if mibBuilder.loadTexts:
    xdsl2ScalarSCGroup.setStatus("current")


# Notification objects

xdsl2LinePerfFECSThreshXtuc = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 251, 0, 1)
)
xdsl2LinePerfFECSThreshXtuc.setObjects(
      *(("VDSL2-LINE-MIB", "xdsl2PMLCurr15MFecs"),
        ("VDSL2-LINE-MIB", "xdsl2LineAlarmConfProfileXtucThresh15MinFecs"))
)
if mibBuilder.loadTexts:
    xdsl2LinePerfFECSThreshXtuc.setStatus(
        "current"
    )

xdsl2LinePerfFECSThreshXtur = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 251, 0, 2)
)
xdsl2LinePerfFECSThreshXtur.setObjects(
      *(("VDSL2-LINE-MIB", "xdsl2PMLCurr15MFecs"),
        ("VDSL2-LINE-MIB", "xdsl2LineAlarmConfProfileXturThresh15MinFecs"))
)
if mibBuilder.loadTexts:
    xdsl2LinePerfFECSThreshXtur.setStatus(
        "current"
    )

xdsl2LinePerfESThreshXtuc = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 251, 0, 3)
)
xdsl2LinePerfESThreshXtuc.setObjects(
      *(("VDSL2-LINE-MIB", "xdsl2PMLCurr15MEs"),
        ("VDSL2-LINE-MIB", "xdsl2LineAlarmConfProfileXtucThresh15MinEs"))
)
if mibBuilder.loadTexts:
    xdsl2LinePerfESThreshXtuc.setStatus(
        "current"
    )

xdsl2LinePerfESThreshXtur = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 251, 0, 4)
)
xdsl2LinePerfESThreshXtur.setObjects(
      *(("VDSL2-LINE-MIB", "xdsl2PMLCurr15MEs"),
        ("VDSL2-LINE-MIB", "xdsl2LineAlarmConfProfileXturThresh15MinEs"))
)
if mibBuilder.loadTexts:
    xdsl2LinePerfESThreshXtur.setStatus(
        "current"
    )

xdsl2LinePerfSESThreshXtuc = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 251, 0, 5)
)
xdsl2LinePerfSESThreshXtuc.setObjects(
      *(("VDSL2-LINE-MIB", "xdsl2PMLCurr15MSes"),
        ("VDSL2-LINE-MIB", "xdsl2LineAlarmConfProfileXtucThresh15MinSes"))
)
if mibBuilder.loadTexts:
    xdsl2LinePerfSESThreshXtuc.setStatus(
        "current"
    )

xdsl2LinePerfSESThreshXtur = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 251, 0, 6)
)
xdsl2LinePerfSESThreshXtur.setObjects(
      *(("VDSL2-LINE-MIB", "xdsl2PMLCurr15MSes"),
        ("VDSL2-LINE-MIB", "xdsl2LineAlarmConfProfileXturThresh15MinSes"))
)
if mibBuilder.loadTexts:
    xdsl2LinePerfSESThreshXtur.setStatus(
        "current"
    )

xdsl2LinePerfLOSSThreshXtuc = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 251, 0, 7)
)
xdsl2LinePerfLOSSThreshXtuc.setObjects(
      *(("VDSL2-LINE-MIB", "xdsl2PMLCurr15MLoss"),
        ("VDSL2-LINE-MIB", "xdsl2LineAlarmConfProfileXtucThresh15MinLoss"))
)
if mibBuilder.loadTexts:
    xdsl2LinePerfLOSSThreshXtuc.setStatus(
        "current"
    )

xdsl2LinePerfLOSSThreshXtur = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 251, 0, 8)
)
xdsl2LinePerfLOSSThreshXtur.setObjects(
      *(("VDSL2-LINE-MIB", "xdsl2PMLCurr15MLoss"),
        ("VDSL2-LINE-MIB", "xdsl2LineAlarmConfProfileXturThresh15MinLoss"))
)
if mibBuilder.loadTexts:
    xdsl2LinePerfLOSSThreshXtur.setStatus(
        "current"
    )

xdsl2LinePerfUASThreshXtuc = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 251, 0, 9)
)
xdsl2LinePerfUASThreshXtuc.setObjects(
      *(("VDSL2-LINE-MIB", "xdsl2PMLCurr15MUas"),
        ("VDSL2-LINE-MIB", "xdsl2LineAlarmConfProfileXtucThresh15MinUas"))
)
if mibBuilder.loadTexts:
    xdsl2LinePerfUASThreshXtuc.setStatus(
        "current"
    )

xdsl2LinePerfUASThreshXtur = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 251, 0, 10)
)
xdsl2LinePerfUASThreshXtur.setObjects(
      *(("VDSL2-LINE-MIB", "xdsl2PMLCurr15MUas"),
        ("VDSL2-LINE-MIB", "xdsl2LineAlarmConfProfileXturThresh15MinUas"))
)
if mibBuilder.loadTexts:
    xdsl2LinePerfUASThreshXtur.setStatus(
        "current"
    )

xdsl2LinePerfCodingViolationsThreshXtuc = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 251, 0, 11)
)
xdsl2LinePerfCodingViolationsThreshXtuc.setObjects(
      *(("VDSL2-LINE-MIB", "xdsl2PMChCurr15MCodingViolations"),
        ("VDSL2-LINE-MIB", "xdsl2ChAlarmConfProfileXtucThresh15MinCodingViolations"))
)
if mibBuilder.loadTexts:
    xdsl2LinePerfCodingViolationsThreshXtuc.setStatus(
        "current"
    )

xdsl2LinePerfCodingViolationsThreshXtur = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 251, 0, 12)
)
xdsl2LinePerfCodingViolationsThreshXtur.setObjects(
      *(("VDSL2-LINE-MIB", "xdsl2PMChCurr15MCodingViolations"),
        ("VDSL2-LINE-MIB", "xdsl2ChAlarmConfProfileXturThresh15MinCodingViolations"))
)
if mibBuilder.loadTexts:
    xdsl2LinePerfCodingViolationsThreshXtur.setStatus(
        "current"
    )

xdsl2LinePerfCorrectedThreshXtuc = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 251, 0, 13)
)
xdsl2LinePerfCorrectedThreshXtuc.setObjects(
      *(("VDSL2-LINE-MIB", "xdsl2PMChCurr15MCorrectedBlocks"),
        ("VDSL2-LINE-MIB", "xdsl2ChAlarmConfProfileXtucThresh15MinCorrected"))
)
if mibBuilder.loadTexts:
    xdsl2LinePerfCorrectedThreshXtuc.setStatus(
        "current"
    )

xdsl2LinePerfCorrectedThreshXtur = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 251, 0, 14)
)
xdsl2LinePerfCorrectedThreshXtur.setObjects(
      *(("VDSL2-LINE-MIB", "xdsl2PMChCurr15MCorrectedBlocks"),
        ("VDSL2-LINE-MIB", "xdsl2ChAlarmConfProfileXturThresh15MinCorrected"))
)
if mibBuilder.loadTexts:
    xdsl2LinePerfCorrectedThreshXtur.setStatus(
        "current"
    )

xdsl2LinePerfFailedFullInitThresh = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 251, 0, 15)
)
xdsl2LinePerfFailedFullInitThresh.setObjects(
      *(("VDSL2-LINE-MIB", "xdsl2PMLInitCurr15MFailedFullInits"),
        ("VDSL2-LINE-MIB", "xdsl2LineAlarmConfProfileThresh15MinFailedFullInt"))
)
if mibBuilder.loadTexts:
    xdsl2LinePerfFailedFullInitThresh.setStatus(
        "current"
    )

xdsl2LinePerfFailedShortInitThresh = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 251, 0, 16)
)
xdsl2LinePerfFailedShortInitThresh.setObjects(
      *(("VDSL2-LINE-MIB", "xdsl2PMLInitCurr15MFailedShortInits"),
        ("VDSL2-LINE-MIB", "xdsl2LineAlarmConfProfileThresh15MinFailedShrtInt"))
)
if mibBuilder.loadTexts:
    xdsl2LinePerfFailedShortInitThresh.setStatus(
        "current"
    )

xdsl2LineStatusChangeXtuc = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 251, 0, 17)
)
xdsl2LineStatusChangeXtuc.setObjects(
    ("VDSL2-LINE-MIB", "xdsl2LineStatusXtuc")
)
if mibBuilder.loadTexts:
    xdsl2LineStatusChangeXtuc.setStatus(
        "current"
    )

xdsl2LineStatusChangeXtur = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 251, 0, 18)
)
xdsl2LineStatusChangeXtur.setObjects(
    ("VDSL2-LINE-MIB", "xdsl2LineStatusXtur")
)
if mibBuilder.loadTexts:
    xdsl2LineStatusChangeXtur.setStatus(
        "current"
    )


# Notifications groups

xdsl2ThreshNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 10, 251, 2, 1, 36)
)
xdsl2ThreshNotificationGroup.setObjects(
      *(("VDSL2-LINE-MIB", "xdsl2LinePerfFECSThreshXtuc"),
        ("VDSL2-LINE-MIB", "xdsl2LinePerfFECSThreshXtur"),
        ("VDSL2-LINE-MIB", "xdsl2LinePerfESThreshXtuc"),
        ("VDSL2-LINE-MIB", "xdsl2LinePerfESThreshXtur"),
        ("VDSL2-LINE-MIB", "xdsl2LinePerfSESThreshXtuc"),
        ("VDSL2-LINE-MIB", "xdsl2LinePerfSESThreshXtur"),
        ("VDSL2-LINE-MIB", "xdsl2LinePerfLOSSThreshXtuc"),
        ("VDSL2-LINE-MIB", "xdsl2LinePerfLOSSThreshXtur"),
        ("VDSL2-LINE-MIB", "xdsl2LinePerfUASThreshXtuc"),
        ("VDSL2-LINE-MIB", "xdsl2LinePerfUASThreshXtur"),
        ("VDSL2-LINE-MIB", "xdsl2LinePerfCodingViolationsThreshXtuc"),
        ("VDSL2-LINE-MIB", "xdsl2LinePerfCodingViolationsThreshXtur"),
        ("VDSL2-LINE-MIB", "xdsl2LinePerfCorrectedThreshXtuc"),
        ("VDSL2-LINE-MIB", "xdsl2LinePerfCorrectedThreshXtur"),
        ("VDSL2-LINE-MIB", "xdsl2LinePerfFailedFullInitThresh"),
        ("VDSL2-LINE-MIB", "xdsl2LinePerfFailedShortInitThresh"))
)
if mibBuilder.loadTexts:
    xdsl2ThreshNotificationGroup.setStatus(
        "current"
    )

xdsl2StatusChangeNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 10, 251, 2, 1, 37)
)
xdsl2StatusChangeNotificationGroup.setObjects(
      *(("VDSL2-LINE-MIB", "xdsl2LineStatusChangeXtuc"),
        ("VDSL2-LINE-MIB", "xdsl2LineStatusChangeXtur"))
)
if mibBuilder.loadTexts:
    xdsl2StatusChangeNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

xdsl2LineMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 251, 2, 2, 1)
)
if mibBuilder.loadTexts:
    xdsl2LineMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VDSL2-LINE-MIB",
    **{"vdsl2MIB": vdsl2MIB,
       "xdsl2Notifications": xdsl2Notifications,
       "xdsl2LinePerfFECSThreshXtuc": xdsl2LinePerfFECSThreshXtuc,
       "xdsl2LinePerfFECSThreshXtur": xdsl2LinePerfFECSThreshXtur,
       "xdsl2LinePerfESThreshXtuc": xdsl2LinePerfESThreshXtuc,
       "xdsl2LinePerfESThreshXtur": xdsl2LinePerfESThreshXtur,
       "xdsl2LinePerfSESThreshXtuc": xdsl2LinePerfSESThreshXtuc,
       "xdsl2LinePerfSESThreshXtur": xdsl2LinePerfSESThreshXtur,
       "xdsl2LinePerfLOSSThreshXtuc": xdsl2LinePerfLOSSThreshXtuc,
       "xdsl2LinePerfLOSSThreshXtur": xdsl2LinePerfLOSSThreshXtur,
       "xdsl2LinePerfUASThreshXtuc": xdsl2LinePerfUASThreshXtuc,
       "xdsl2LinePerfUASThreshXtur": xdsl2LinePerfUASThreshXtur,
       "xdsl2LinePerfCodingViolationsThreshXtuc": xdsl2LinePerfCodingViolationsThreshXtuc,
       "xdsl2LinePerfCodingViolationsThreshXtur": xdsl2LinePerfCodingViolationsThreshXtur,
       "xdsl2LinePerfCorrectedThreshXtuc": xdsl2LinePerfCorrectedThreshXtuc,
       "xdsl2LinePerfCorrectedThreshXtur": xdsl2LinePerfCorrectedThreshXtur,
       "xdsl2LinePerfFailedFullInitThresh": xdsl2LinePerfFailedFullInitThresh,
       "xdsl2LinePerfFailedShortInitThresh": xdsl2LinePerfFailedShortInitThresh,
       "xdsl2LineStatusChangeXtuc": xdsl2LineStatusChangeXtuc,
       "xdsl2LineStatusChangeXtur": xdsl2LineStatusChangeXtur,
       "xdsl2Objects": xdsl2Objects,
       "xdsl2Line": xdsl2Line,
       "xdsl2LineTable": xdsl2LineTable,
       "xdsl2LineEntry": xdsl2LineEntry,
       "xdsl2LineConfTemplate": xdsl2LineConfTemplate,
       "xdsl2LineConfFallbackTemplate": xdsl2LineConfFallbackTemplate,
       "xdsl2LineAlarmConfTemplate": xdsl2LineAlarmConfTemplate,
       "xdsl2LineCmndConfPmsf": xdsl2LineCmndConfPmsf,
       "xdsl2LineCmndConfLdsf": xdsl2LineCmndConfLdsf,
       "xdsl2LineCmndConfLdsfFailReason": xdsl2LineCmndConfLdsfFailReason,
       "xdsl2LineCmndConfBpsc": xdsl2LineCmndConfBpsc,
       "xdsl2LineCmndConfBpscFailReason": xdsl2LineCmndConfBpscFailReason,
       "xdsl2LineCmndConfBpscRequests": xdsl2LineCmndConfBpscRequests,
       "xdsl2LineCmndAutomodeColdStart": xdsl2LineCmndAutomodeColdStart,
       "xdsl2LineCmndConfReset": xdsl2LineCmndConfReset,
       "xdsl2LineStatusActTemplate": xdsl2LineStatusActTemplate,
       "xdsl2LineStatusXtuTransSys": xdsl2LineStatusXtuTransSys,
       "xdsl2LineStatusPwrMngState": xdsl2LineStatusPwrMngState,
       "xdsl2LineStatusInitResult": xdsl2LineStatusInitResult,
       "xdsl2LineStatusLastStateDs": xdsl2LineStatusLastStateDs,
       "xdsl2LineStatusLastStateUs": xdsl2LineStatusLastStateUs,
       "xdsl2LineStatusXtur": xdsl2LineStatusXtur,
       "xdsl2LineStatusXtuc": xdsl2LineStatusXtuc,
       "xdsl2LineStatusAttainableRateDs": xdsl2LineStatusAttainableRateDs,
       "xdsl2LineStatusAttainableRateUs": xdsl2LineStatusAttainableRateUs,
       "xdsl2LineStatusActPsdDs": xdsl2LineStatusActPsdDs,
       "xdsl2LineStatusActPsdUs": xdsl2LineStatusActPsdUs,
       "xdsl2LineStatusActAtpDs": xdsl2LineStatusActAtpDs,
       "xdsl2LineStatusActAtpUs": xdsl2LineStatusActAtpUs,
       "xdsl2LineStatusActProfile": xdsl2LineStatusActProfile,
       "xdsl2LineStatusActLimitMask": xdsl2LineStatusActLimitMask,
       "xdsl2LineStatusActUs0Mask": xdsl2LineStatusActUs0Mask,
       "xdsl2LineStatusActSnrModeDs": xdsl2LineStatusActSnrModeDs,
       "xdsl2LineStatusActSnrModeUs": xdsl2LineStatusActSnrModeUs,
       "xdsl2LineStatusElectricalLength": xdsl2LineStatusElectricalLength,
       "xdsl2LineStatusTssiDs": xdsl2LineStatusTssiDs,
       "xdsl2LineStatusTssiUs": xdsl2LineStatusTssiUs,
       "xdsl2LineStatusMrefPsdDs": xdsl2LineStatusMrefPsdDs,
       "xdsl2LineStatusMrefPsdUs": xdsl2LineStatusMrefPsdUs,
       "xdsl2LineStatusTrellisDs": xdsl2LineStatusTrellisDs,
       "xdsl2LineStatusTrellisUs": xdsl2LineStatusTrellisUs,
       "xdsl2LineStatusActualCe": xdsl2LineStatusActualCe,
       "xdsl2LineBandTable": xdsl2LineBandTable,
       "xdsl2LineBandEntry": xdsl2LineBandEntry,
       "xdsl2LineBand": xdsl2LineBand,
       "xdsl2LineBandStatusLnAtten": xdsl2LineBandStatusLnAtten,
       "xdsl2LineBandStatusSigAtten": xdsl2LineBandStatusSigAtten,
       "xdsl2LineBandStatusSnrMargin": xdsl2LineBandStatusSnrMargin,
       "xdsl2Status": xdsl2Status,
       "xdsl2LineSegmentTable": xdsl2LineSegmentTable,
       "xdsl2LineSegmentEntry": xdsl2LineSegmentEntry,
       "xdsl2LineSegmentDirection": xdsl2LineSegmentDirection,
       "xdsl2LineSegment": xdsl2LineSegment,
       "xdsl2LineSegmentBitsAlloc": xdsl2LineSegmentBitsAlloc,
       "xdsl2LineSegmentRowStatus": xdsl2LineSegmentRowStatus,
       "xdsl2ChannelStatusTable": xdsl2ChannelStatusTable,
       "xdsl2ChannelStatusEntry": xdsl2ChannelStatusEntry,
       "xdsl2ChStatusUnit": xdsl2ChStatusUnit,
       "xdsl2ChStatusActDataRate": xdsl2ChStatusActDataRate,
       "xdsl2ChStatusPrevDataRate": xdsl2ChStatusPrevDataRate,
       "xdsl2ChStatusActDelay": xdsl2ChStatusActDelay,
       "xdsl2ChStatusActInp": xdsl2ChStatusActInp,
       "xdsl2ChStatusInpReport": xdsl2ChStatusInpReport,
       "xdsl2ChStatusNFec": xdsl2ChStatusNFec,
       "xdsl2ChStatusRFec": xdsl2ChStatusRFec,
       "xdsl2ChStatusLSymb": xdsl2ChStatusLSymb,
       "xdsl2ChStatusIntlvDepth": xdsl2ChStatusIntlvDepth,
       "xdsl2ChStatusIntlvBlock": xdsl2ChStatusIntlvBlock,
       "xdsl2ChStatusLPath": xdsl2ChStatusLPath,
       "xdsl2ChStatusAtmStatus": xdsl2ChStatusAtmStatus,
       "xdsl2ChStatusPtmStatus": xdsl2ChStatusPtmStatus,
       "xdsl2SCStatusTable": xdsl2SCStatusTable,
       "xdsl2SCStatusEntry": xdsl2SCStatusEntry,
       "xdsl2SCStatusDirection": xdsl2SCStatusDirection,
       "xdsl2SCStatusLinScale": xdsl2SCStatusLinScale,
       "xdsl2SCStatusLinScGroupSize": xdsl2SCStatusLinScGroupSize,
       "xdsl2SCStatusLogMt": xdsl2SCStatusLogMt,
       "xdsl2SCStatusLogScGroupSize": xdsl2SCStatusLogScGroupSize,
       "xdsl2SCStatusQlnMt": xdsl2SCStatusQlnMt,
       "xdsl2SCStatusQlnScGroupSize": xdsl2SCStatusQlnScGroupSize,
       "xdsl2SCStatusSnrMtime": xdsl2SCStatusSnrMtime,
       "xdsl2SCStatusSnrScGroupSize": xdsl2SCStatusSnrScGroupSize,
       "xdsl2SCStatusAttainableRate": xdsl2SCStatusAttainableRate,
       "xdsl2SCStatusRowStatus": xdsl2SCStatusRowStatus,
       "xdsl2SCStatusBandTable": xdsl2SCStatusBandTable,
       "xdsl2SCStatusBandEntry": xdsl2SCStatusBandEntry,
       "xdsl2SCStatusBand": xdsl2SCStatusBand,
       "xdsl2SCStatusBandLnAtten": xdsl2SCStatusBandLnAtten,
       "xdsl2SCStatusBandSigAtten": xdsl2SCStatusBandSigAtten,
       "xdsl2SCStatusSegmentTable": xdsl2SCStatusSegmentTable,
       "xdsl2SCStatusSegmentEntry": xdsl2SCStatusSegmentEntry,
       "xdsl2SCStatusSegment": xdsl2SCStatusSegment,
       "xdsl2SCStatusSegmentLinReal": xdsl2SCStatusSegmentLinReal,
       "xdsl2SCStatusSegmentLinImg": xdsl2SCStatusSegmentLinImg,
       "xdsl2SCStatusSegmentLog": xdsl2SCStatusSegmentLog,
       "xdsl2SCStatusSegmentQln": xdsl2SCStatusSegmentQln,
       "xdsl2SCStatusSegmentSnr": xdsl2SCStatusSegmentSnr,
       "xdsl2SCStatusSegmentBitsAlloc": xdsl2SCStatusSegmentBitsAlloc,
       "xdsl2SCStatusSegmentGainAlloc": xdsl2SCStatusSegmentGainAlloc,
       "xdsl2Inventory": xdsl2Inventory,
       "xdsl2LineInventoryTable": xdsl2LineInventoryTable,
       "xdsl2LineInventoryEntry": xdsl2LineInventoryEntry,
       "xdsl2LInvUnit": xdsl2LInvUnit,
       "xdsl2LInvG994VendorId": xdsl2LInvG994VendorId,
       "xdsl2LInvSystemVendorId": xdsl2LInvSystemVendorId,
       "xdsl2LInvVersionNumber": xdsl2LInvVersionNumber,
       "xdsl2LInvSerialNumber": xdsl2LInvSerialNumber,
       "xdsl2LInvSelfTestResult": xdsl2LInvSelfTestResult,
       "xdsl2LInvTransmissionCapabilities": xdsl2LInvTransmissionCapabilities,
       "xdsl2PM": xdsl2PM,
       "xdsl2PMLine": xdsl2PMLine,
       "xdsl2PMLineCurrTable": xdsl2PMLineCurrTable,
       "xdsl2PMLineCurrEntry": xdsl2PMLineCurrEntry,
       "xdsl2PMLCurrUnit": xdsl2PMLCurrUnit,
       "xdsl2PMLCurr15MValidIntervals": xdsl2PMLCurr15MValidIntervals,
       "xdsl2PMLCurr15MInvalidIntervals": xdsl2PMLCurr15MInvalidIntervals,
       "xdsl2PMLCurr15MTimeElapsed": xdsl2PMLCurr15MTimeElapsed,
       "xdsl2PMLCurr15MFecs": xdsl2PMLCurr15MFecs,
       "xdsl2PMLCurr15MEs": xdsl2PMLCurr15MEs,
       "xdsl2PMLCurr15MSes": xdsl2PMLCurr15MSes,
       "xdsl2PMLCurr15MLoss": xdsl2PMLCurr15MLoss,
       "xdsl2PMLCurr15MUas": xdsl2PMLCurr15MUas,
       "xdsl2PMLCurr1DayValidIntervals": xdsl2PMLCurr1DayValidIntervals,
       "xdsl2PMLCurr1DayInvalidIntervals": xdsl2PMLCurr1DayInvalidIntervals,
       "xdsl2PMLCurr1DayTimeElapsed": xdsl2PMLCurr1DayTimeElapsed,
       "xdsl2PMLCurr1DayFecs": xdsl2PMLCurr1DayFecs,
       "xdsl2PMLCurr1DayEs": xdsl2PMLCurr1DayEs,
       "xdsl2PMLCurr1DaySes": xdsl2PMLCurr1DaySes,
       "xdsl2PMLCurr1DayLoss": xdsl2PMLCurr1DayLoss,
       "xdsl2PMLCurr1DayUas": xdsl2PMLCurr1DayUas,
       "xdsl2PMLineInitCurrTable": xdsl2PMLineInitCurrTable,
       "xdsl2PMLineInitCurrEntry": xdsl2PMLineInitCurrEntry,
       "xdsl2PMLInitCurr15MValidIntervals": xdsl2PMLInitCurr15MValidIntervals,
       "xdsl2PMLInitCurr15MInvalidIntervals": xdsl2PMLInitCurr15MInvalidIntervals,
       "xdsl2PMLInitCurr15MTimeElapsed": xdsl2PMLInitCurr15MTimeElapsed,
       "xdsl2PMLInitCurr15MFullInits": xdsl2PMLInitCurr15MFullInits,
       "xdsl2PMLInitCurr15MFailedFullInits": xdsl2PMLInitCurr15MFailedFullInits,
       "xdsl2PMLInitCurr15MShortInits": xdsl2PMLInitCurr15MShortInits,
       "xdsl2PMLInitCurr15MFailedShortInits": xdsl2PMLInitCurr15MFailedShortInits,
       "xdsl2PMLInitCurr1DayValidIntervals": xdsl2PMLInitCurr1DayValidIntervals,
       "xdsl2PMLInitCurr1DayInvalidIntervals": xdsl2PMLInitCurr1DayInvalidIntervals,
       "xdsl2PMLInitCurr1DayTimeElapsed": xdsl2PMLInitCurr1DayTimeElapsed,
       "xdsl2PMLInitCurr1DayFullInits": xdsl2PMLInitCurr1DayFullInits,
       "xdsl2PMLInitCurr1DayFailedFullInits": xdsl2PMLInitCurr1DayFailedFullInits,
       "xdsl2PMLInitCurr1DayShortInits": xdsl2PMLInitCurr1DayShortInits,
       "xdsl2PMLInitCurr1DayFailedShortInits": xdsl2PMLInitCurr1DayFailedShortInits,
       "xdsl2PMLineHist15MinTable": xdsl2PMLineHist15MinTable,
       "xdsl2PMLineHist15MinEntry": xdsl2PMLineHist15MinEntry,
       "xdsl2PMLHist15MUnit": xdsl2PMLHist15MUnit,
       "xdsl2PMLHist15MInterval": xdsl2PMLHist15MInterval,
       "xdsl2PMLHist15MMonitoredTime": xdsl2PMLHist15MMonitoredTime,
       "xdsl2PMLHist15MFecs": xdsl2PMLHist15MFecs,
       "xdsl2PMLHist15MEs": xdsl2PMLHist15MEs,
       "xdsl2PMLHist15MSes": xdsl2PMLHist15MSes,
       "xdsl2PMLHist15MLoss": xdsl2PMLHist15MLoss,
       "xdsl2PMLHist15MUas": xdsl2PMLHist15MUas,
       "xdsl2PMLHist15MValidInterval": xdsl2PMLHist15MValidInterval,
       "xdsl2PMLineHist1DayTable": xdsl2PMLineHist1DayTable,
       "xdsl2PMLineHist1DayEntry": xdsl2PMLineHist1DayEntry,
       "xdsl2PMLHist1DUnit": xdsl2PMLHist1DUnit,
       "xdsl2PMLHist1DInterval": xdsl2PMLHist1DInterval,
       "xdsl2PMLHist1DMonitoredTime": xdsl2PMLHist1DMonitoredTime,
       "xdsl2PMLHist1DFecs": xdsl2PMLHist1DFecs,
       "xdsl2PMLHist1DEs": xdsl2PMLHist1DEs,
       "xdsl2PMLHist1DSes": xdsl2PMLHist1DSes,
       "xdsl2PMLHist1DLoss": xdsl2PMLHist1DLoss,
       "xdsl2PMLHist1DUas": xdsl2PMLHist1DUas,
       "xdsl2PMLHist1DValidInterval": xdsl2PMLHist1DValidInterval,
       "xdsl2PMLineInitHist15MinTable": xdsl2PMLineInitHist15MinTable,
       "xdsl2PMLineInitHist15MinEntry": xdsl2PMLineInitHist15MinEntry,
       "xdsl2PMLInitHist15MInterval": xdsl2PMLInitHist15MInterval,
       "xdsl2PMLInitHist15MMonitoredTime": xdsl2PMLInitHist15MMonitoredTime,
       "xdsl2PMLInitHist15MFullInits": xdsl2PMLInitHist15MFullInits,
       "xdsl2PMLInitHist15MFailedFullInits": xdsl2PMLInitHist15MFailedFullInits,
       "xdsl2PMLInitHist15MShortInits": xdsl2PMLInitHist15MShortInits,
       "xdsl2PMLInitHist15MFailedShortInits": xdsl2PMLInitHist15MFailedShortInits,
       "xdsl2PMLInitHist15MValidInterval": xdsl2PMLInitHist15MValidInterval,
       "xdsl2PMLineInitHist1DayTable": xdsl2PMLineInitHist1DayTable,
       "xdsl2PMLineInitHist1DayEntry": xdsl2PMLineInitHist1DayEntry,
       "xdsl2PMLInitHist1DInterval": xdsl2PMLInitHist1DInterval,
       "xdsl2PMLInitHist1DMonitoredTime": xdsl2PMLInitHist1DMonitoredTime,
       "xdsl2PMLInitHist1DFullInits": xdsl2PMLInitHist1DFullInits,
       "xdsl2PMLInitHist1DFailedFullInits": xdsl2PMLInitHist1DFailedFullInits,
       "xdsl2PMLInitHist1DShortInits": xdsl2PMLInitHist1DShortInits,
       "xdsl2PMLInitHist1DFailedShortInits": xdsl2PMLInitHist1DFailedShortInits,
       "xdsl2PMLInitHist1DValidInterval": xdsl2PMLInitHist1DValidInterval,
       "xdsl2PMChannel": xdsl2PMChannel,
       "xdsl2PMChCurrTable": xdsl2PMChCurrTable,
       "xdsl2PMChCurrEntry": xdsl2PMChCurrEntry,
       "xdsl2PMChCurrUnit": xdsl2PMChCurrUnit,
       "xdsl2PMChCurr15MValidIntervals": xdsl2PMChCurr15MValidIntervals,
       "xdsl2PMChCurr15MInvalidIntervals": xdsl2PMChCurr15MInvalidIntervals,
       "xdsl2PMChCurr15MTimeElapsed": xdsl2PMChCurr15MTimeElapsed,
       "xdsl2PMChCurr15MCodingViolations": xdsl2PMChCurr15MCodingViolations,
       "xdsl2PMChCurr15MCorrectedBlocks": xdsl2PMChCurr15MCorrectedBlocks,
       "xdsl2PMChCurr1DayValidIntervals": xdsl2PMChCurr1DayValidIntervals,
       "xdsl2PMChCurr1DayInvalidIntervals": xdsl2PMChCurr1DayInvalidIntervals,
       "xdsl2PMChCurr1DayTimeElapsed": xdsl2PMChCurr1DayTimeElapsed,
       "xdsl2PMChCurr1DayCodingViolations": xdsl2PMChCurr1DayCodingViolations,
       "xdsl2PMChCurr1DayCorrectedBlocks": xdsl2PMChCurr1DayCorrectedBlocks,
       "xdsl2PMChHist15MinTable": xdsl2PMChHist15MinTable,
       "xdsl2PMChHist15MinEntry": xdsl2PMChHist15MinEntry,
       "xdsl2PMChHist15MUnit": xdsl2PMChHist15MUnit,
       "xdsl2PMChHist15MInterval": xdsl2PMChHist15MInterval,
       "xdsl2PMChHist15MMonitoredTime": xdsl2PMChHist15MMonitoredTime,
       "xdsl2PMChHist15MCodingViolations": xdsl2PMChHist15MCodingViolations,
       "xdsl2PMChHist15MCorrectedBlocks": xdsl2PMChHist15MCorrectedBlocks,
       "xdsl2PMChHist15MValidInterval": xdsl2PMChHist15MValidInterval,
       "xdsl2PMChHist1DTable": xdsl2PMChHist1DTable,
       "xdsl2PMChHist1DEntry": xdsl2PMChHist1DEntry,
       "xdsl2PMChHist1DUnit": xdsl2PMChHist1DUnit,
       "xdsl2PMChHist1DInterval": xdsl2PMChHist1DInterval,
       "xdsl2PMChHist1DMonitoredTime": xdsl2PMChHist1DMonitoredTime,
       "xdsl2PMChHist1DCodingViolations": xdsl2PMChHist1DCodingViolations,
       "xdsl2PMChHist1DCorrectedBlocks": xdsl2PMChHist1DCorrectedBlocks,
       "xdsl2PMChHist1DValidInterval": xdsl2PMChHist1DValidInterval,
       "xdsl2Profile": xdsl2Profile,
       "xdsl2ProfileLine": xdsl2ProfileLine,
       "xdsl2LineConfTemplateTable": xdsl2LineConfTemplateTable,
       "xdsl2LineConfTemplateEntry": xdsl2LineConfTemplateEntry,
       "xdsl2LConfTempTemplateName": xdsl2LConfTempTemplateName,
       "xdsl2LConfTempLineProfile": xdsl2LConfTempLineProfile,
       "xdsl2LConfTempChan1ConfProfile": xdsl2LConfTempChan1ConfProfile,
       "xdsl2LConfTempChan1RaRatioDs": xdsl2LConfTempChan1RaRatioDs,
       "xdsl2LConfTempChan1RaRatioUs": xdsl2LConfTempChan1RaRatioUs,
       "xdsl2LConfTempChan2ConfProfile": xdsl2LConfTempChan2ConfProfile,
       "xdsl2LConfTempChan2RaRatioDs": xdsl2LConfTempChan2RaRatioDs,
       "xdsl2LConfTempChan2RaRatioUs": xdsl2LConfTempChan2RaRatioUs,
       "xdsl2LConfTempChan3ConfProfile": xdsl2LConfTempChan3ConfProfile,
       "xdsl2LConfTempChan3RaRatioDs": xdsl2LConfTempChan3RaRatioDs,
       "xdsl2LConfTempChan3RaRatioUs": xdsl2LConfTempChan3RaRatioUs,
       "xdsl2LConfTempChan4ConfProfile": xdsl2LConfTempChan4ConfProfile,
       "xdsl2LConfTempChan4RaRatioDs": xdsl2LConfTempChan4RaRatioDs,
       "xdsl2LConfTempChan4RaRatioUs": xdsl2LConfTempChan4RaRatioUs,
       "xdsl2LConfTempRowStatus": xdsl2LConfTempRowStatus,
       "xdsl2LineConfProfTable": xdsl2LineConfProfTable,
       "xdsl2LineConfProfEntry": xdsl2LineConfProfEntry,
       "xdsl2LConfProfProfileName": xdsl2LConfProfProfileName,
       "xdsl2LConfProfScMaskDs": xdsl2LConfProfScMaskDs,
       "xdsl2LConfProfScMaskUs": xdsl2LConfProfScMaskUs,
       "xdsl2LConfProfVdsl2CarMask": xdsl2LConfProfVdsl2CarMask,
       "xdsl2LConfProfRfiBands": xdsl2LConfProfRfiBands,
       "xdsl2LConfProfRaModeDs": xdsl2LConfProfRaModeDs,
       "xdsl2LConfProfRaModeUs": xdsl2LConfProfRaModeUs,
       "xdsl2LConfProfRaUsNrmDs": xdsl2LConfProfRaUsNrmDs,
       "xdsl2LConfProfRaUsNrmUs": xdsl2LConfProfRaUsNrmUs,
       "xdsl2LConfProfRaUsTimeDs": xdsl2LConfProfRaUsTimeDs,
       "xdsl2LConfProfRaUsTimeUs": xdsl2LConfProfRaUsTimeUs,
       "xdsl2LConfProfRaDsNrmDs": xdsl2LConfProfRaDsNrmDs,
       "xdsl2LConfProfRaDsNrmUs": xdsl2LConfProfRaDsNrmUs,
       "xdsl2LConfProfRaDsTimeDs": xdsl2LConfProfRaDsTimeDs,
       "xdsl2LConfProfRaDsTimeUs": xdsl2LConfProfRaDsTimeUs,
       "xdsl2LConfProfTargetSnrmDs": xdsl2LConfProfTargetSnrmDs,
       "xdsl2LConfProfTargetSnrmUs": xdsl2LConfProfTargetSnrmUs,
       "xdsl2LConfProfMaxSnrmDs": xdsl2LConfProfMaxSnrmDs,
       "xdsl2LConfProfMaxSnrmUs": xdsl2LConfProfMaxSnrmUs,
       "xdsl2LConfProfMinSnrmDs": xdsl2LConfProfMinSnrmDs,
       "xdsl2LConfProfMinSnrmUs": xdsl2LConfProfMinSnrmUs,
       "xdsl2LConfProfMsgMinUs": xdsl2LConfProfMsgMinUs,
       "xdsl2LConfProfMsgMinDs": xdsl2LConfProfMsgMinDs,
       "xdsl2LConfProfCeFlag": xdsl2LConfProfCeFlag,
       "xdsl2LConfProfSnrModeDs": xdsl2LConfProfSnrModeDs,
       "xdsl2LConfProfSnrModeUs": xdsl2LConfProfSnrModeUs,
       "xdsl2LConfProfTxRefVnDs": xdsl2LConfProfTxRefVnDs,
       "xdsl2LConfProfTxRefVnUs": xdsl2LConfProfTxRefVnUs,
       "xdsl2LConfProfXtuTransSysEna": xdsl2LConfProfXtuTransSysEna,
       "xdsl2LConfProfPmMode": xdsl2LConfProfPmMode,
       "xdsl2LConfProfL0Time": xdsl2LConfProfL0Time,
       "xdsl2LConfProfL2Time": xdsl2LConfProfL2Time,
       "xdsl2LConfProfL2Atpr": xdsl2LConfProfL2Atpr,
       "xdsl2LConfProfL2Atprt": xdsl2LConfProfL2Atprt,
       "xdsl2LConfProfProfiles": xdsl2LConfProfProfiles,
       "xdsl2LConfProfDpboEPsd": xdsl2LConfProfDpboEPsd,
       "xdsl2LConfProfDpboEsEL": xdsl2LConfProfDpboEsEL,
       "xdsl2LConfProfDpboEsCableModelA": xdsl2LConfProfDpboEsCableModelA,
       "xdsl2LConfProfDpboEsCableModelB": xdsl2LConfProfDpboEsCableModelB,
       "xdsl2LConfProfDpboEsCableModelC": xdsl2LConfProfDpboEsCableModelC,
       "xdsl2LConfProfDpboMus": xdsl2LConfProfDpboMus,
       "xdsl2LConfProfDpboFMin": xdsl2LConfProfDpboFMin,
       "xdsl2LConfProfDpboFMax": xdsl2LConfProfDpboFMax,
       "xdsl2LConfProfUpboKL": xdsl2LConfProfUpboKL,
       "xdsl2LConfProfUpboKLF": xdsl2LConfProfUpboKLF,
       "xdsl2LConfProfUs0Mask": xdsl2LConfProfUs0Mask,
       "xdsl2LConfProfForceInp": xdsl2LConfProfForceInp,
       "xdsl2LConfProfRowStatus": xdsl2LConfProfRowStatus,
       "xdsl2LineConfProfModeSpecTable": xdsl2LineConfProfModeSpecTable,
       "xdsl2LineConfProfModeSpecEntry": xdsl2LineConfProfModeSpecEntry,
       "xdsl2LConfProfXdslMode": xdsl2LConfProfXdslMode,
       "xdsl2LConfProfMaxNomPsdDs": xdsl2LConfProfMaxNomPsdDs,
       "xdsl2LConfProfMaxNomPsdUs": xdsl2LConfProfMaxNomPsdUs,
       "xdsl2LConfProfMaxNomAtpDs": xdsl2LConfProfMaxNomAtpDs,
       "xdsl2LConfProfMaxNomAtpUs": xdsl2LConfProfMaxNomAtpUs,
       "xdsl2LConfProfMaxAggRxPwrUs": xdsl2LConfProfMaxAggRxPwrUs,
       "xdsl2LConfProfPsdMaskDs": xdsl2LConfProfPsdMaskDs,
       "xdsl2LConfProfPsdMaskUs": xdsl2LConfProfPsdMaskUs,
       "xdsl2LConfProfPsdMaskSelectUs": xdsl2LConfProfPsdMaskSelectUs,
       "xdsl2LConfProfClassMask": xdsl2LConfProfClassMask,
       "xdsl2LConfProfLimitMask": xdsl2LConfProfLimitMask,
       "xdsl2LConfProfUs0Disable": xdsl2LConfProfUs0Disable,
       "xdsl2LConfProfModeSpecRowStatus": xdsl2LConfProfModeSpecRowStatus,
       "xdsl2LineConfProfModeSpecBandUsTable": xdsl2LineConfProfModeSpecBandUsTable,
       "xdsl2LineConfProfModeSpecBandUsEntry": xdsl2LineConfProfModeSpecBandUsEntry,
       "xdsl2LConfProfXdslBandUs": xdsl2LConfProfXdslBandUs,
       "xdsl2LConfProfUpboPsdA": xdsl2LConfProfUpboPsdA,
       "xdsl2LConfProfUpboPsdB": xdsl2LConfProfUpboPsdB,
       "xdsl2LConfProfModeSpecBandUsRowStatus": xdsl2LConfProfModeSpecBandUsRowStatus,
       "xdsl2ProfileChannel": xdsl2ProfileChannel,
       "xdsl2ChConfProfileTable": xdsl2ChConfProfileTable,
       "xdsl2ChConfProfileEntry": xdsl2ChConfProfileEntry,
       "xdsl2ChConfProfProfileName": xdsl2ChConfProfProfileName,
       "xdsl2ChConfProfMinDataRateDs": xdsl2ChConfProfMinDataRateDs,
       "xdsl2ChConfProfMinDataRateUs": xdsl2ChConfProfMinDataRateUs,
       "xdsl2ChConfProfMinResDataRateDs": xdsl2ChConfProfMinResDataRateDs,
       "xdsl2ChConfProfMinResDataRateUs": xdsl2ChConfProfMinResDataRateUs,
       "xdsl2ChConfProfMaxDataRateDs": xdsl2ChConfProfMaxDataRateDs,
       "xdsl2ChConfProfMaxDataRateUs": xdsl2ChConfProfMaxDataRateUs,
       "xdsl2ChConfProfMinDataRateLowPwrDs": xdsl2ChConfProfMinDataRateLowPwrDs,
       "xdsl2ChConfProfMinDataRateLowPwrUs": xdsl2ChConfProfMinDataRateLowPwrUs,
       "xdsl2ChConfProfMaxDelayDs": xdsl2ChConfProfMaxDelayDs,
       "xdsl2ChConfProfMaxDelayUs": xdsl2ChConfProfMaxDelayUs,
       "xdsl2ChConfProfMinProtectionDs": xdsl2ChConfProfMinProtectionDs,
       "xdsl2ChConfProfMinProtectionUs": xdsl2ChConfProfMinProtectionUs,
       "xdsl2ChConfProfMinProtection8Ds": xdsl2ChConfProfMinProtection8Ds,
       "xdsl2ChConfProfMinProtection8Us": xdsl2ChConfProfMinProtection8Us,
       "xdsl2ChConfProfMaxBerDs": xdsl2ChConfProfMaxBerDs,
       "xdsl2ChConfProfMaxBerUs": xdsl2ChConfProfMaxBerUs,
       "xdsl2ChConfProfUsDataRateDs": xdsl2ChConfProfUsDataRateDs,
       "xdsl2ChConfProfDsDataRateDs": xdsl2ChConfProfDsDataRateDs,
       "xdsl2ChConfProfUsDataRateUs": xdsl2ChConfProfUsDataRateUs,
       "xdsl2ChConfProfDsDataRateUs": xdsl2ChConfProfDsDataRateUs,
       "xdsl2ChConfProfImaEnabled": xdsl2ChConfProfImaEnabled,
       "xdsl2ChConfProfMaxDelayVar": xdsl2ChConfProfMaxDelayVar,
       "xdsl2ChConfProfInitPolicy": xdsl2ChConfProfInitPolicy,
       "xdsl2ChConfProfRowStatus": xdsl2ChConfProfRowStatus,
       "xdsl2ProfileAlarmConf": xdsl2ProfileAlarmConf,
       "xdsl2LineAlarmConfTemplateTable": xdsl2LineAlarmConfTemplateTable,
       "xdsl2LineAlarmConfTemplateEntry": xdsl2LineAlarmConfTemplateEntry,
       "xdsl2LAlarmConfTempTemplateName": xdsl2LAlarmConfTempTemplateName,
       "xdsl2LAlarmConfTempLineProfile": xdsl2LAlarmConfTempLineProfile,
       "xdsl2LAlarmConfTempChan1ConfProfile": xdsl2LAlarmConfTempChan1ConfProfile,
       "xdsl2LAlarmConfTempChan2ConfProfile": xdsl2LAlarmConfTempChan2ConfProfile,
       "xdsl2LAlarmConfTempChan3ConfProfile": xdsl2LAlarmConfTempChan3ConfProfile,
       "xdsl2LAlarmConfTempChan4ConfProfile": xdsl2LAlarmConfTempChan4ConfProfile,
       "xdsl2LAlarmConfTempRowStatus": xdsl2LAlarmConfTempRowStatus,
       "xdsl2LineAlarmConfProfileTable": xdsl2LineAlarmConfProfileTable,
       "xdsl2LineAlarmConfProfileEntry": xdsl2LineAlarmConfProfileEntry,
       "xdsl2LineAlarmConfProfileName": xdsl2LineAlarmConfProfileName,
       "xdsl2LineAlarmConfProfileXtucThresh15MinFecs": xdsl2LineAlarmConfProfileXtucThresh15MinFecs,
       "xdsl2LineAlarmConfProfileXtucThresh15MinEs": xdsl2LineAlarmConfProfileXtucThresh15MinEs,
       "xdsl2LineAlarmConfProfileXtucThresh15MinSes": xdsl2LineAlarmConfProfileXtucThresh15MinSes,
       "xdsl2LineAlarmConfProfileXtucThresh15MinLoss": xdsl2LineAlarmConfProfileXtucThresh15MinLoss,
       "xdsl2LineAlarmConfProfileXtucThresh15MinUas": xdsl2LineAlarmConfProfileXtucThresh15MinUas,
       "xdsl2LineAlarmConfProfileXturThresh15MinFecs": xdsl2LineAlarmConfProfileXturThresh15MinFecs,
       "xdsl2LineAlarmConfProfileXturThresh15MinEs": xdsl2LineAlarmConfProfileXturThresh15MinEs,
       "xdsl2LineAlarmConfProfileXturThresh15MinSes": xdsl2LineAlarmConfProfileXturThresh15MinSes,
       "xdsl2LineAlarmConfProfileXturThresh15MinLoss": xdsl2LineAlarmConfProfileXturThresh15MinLoss,
       "xdsl2LineAlarmConfProfileXturThresh15MinUas": xdsl2LineAlarmConfProfileXturThresh15MinUas,
       "xdsl2LineAlarmConfProfileThresh15MinFailedFullInt": xdsl2LineAlarmConfProfileThresh15MinFailedFullInt,
       "xdsl2LineAlarmConfProfileThresh15MinFailedShrtInt": xdsl2LineAlarmConfProfileThresh15MinFailedShrtInt,
       "xdsl2LineAlarmConfProfileRowStatus": xdsl2LineAlarmConfProfileRowStatus,
       "xdsl2ChAlarmConfProfileTable": xdsl2ChAlarmConfProfileTable,
       "xdsl2ChAlarmConfProfileEntry": xdsl2ChAlarmConfProfileEntry,
       "xdsl2ChAlarmConfProfileName": xdsl2ChAlarmConfProfileName,
       "xdsl2ChAlarmConfProfileXtucThresh15MinCodingViolations": xdsl2ChAlarmConfProfileXtucThresh15MinCodingViolations,
       "xdsl2ChAlarmConfProfileXtucThresh15MinCorrected": xdsl2ChAlarmConfProfileXtucThresh15MinCorrected,
       "xdsl2ChAlarmConfProfileXturThresh15MinCodingViolations": xdsl2ChAlarmConfProfileXturThresh15MinCodingViolations,
       "xdsl2ChAlarmConfProfileXturThresh15MinCorrected": xdsl2ChAlarmConfProfileXturThresh15MinCorrected,
       "xdsl2ChAlarmConfProfileRowStatus": xdsl2ChAlarmConfProfileRowStatus,
       "xdsl2Scalar": xdsl2Scalar,
       "xdsl2ScalarSC": xdsl2ScalarSC,
       "xdsl2ScalarSCMaxInterfaces": xdsl2ScalarSCMaxInterfaces,
       "xdsl2ScalarSCAvailInterfaces": xdsl2ScalarSCAvailInterfaces,
       "xdsl2Conformance": xdsl2Conformance,
       "xdsl2Groups": xdsl2Groups,
       "xdsl2LineGroup": xdsl2LineGroup,
       "xdsl2LineFallbackGroup": xdsl2LineFallbackGroup,
       "xdsl2LineBpscGroup": xdsl2LineBpscGroup,
       "xdsl2LineSegmentGroup": xdsl2LineSegmentGroup,
       "xdsl2ChannelStatusGroup": xdsl2ChannelStatusGroup,
       "xdsl2ChannelStatusAtmGroup": xdsl2ChannelStatusAtmGroup,
       "xdsl2ChannelStatusPtmGroup": xdsl2ChannelStatusPtmGroup,
       "xdsl2SCStatusGroup": xdsl2SCStatusGroup,
       "xdsl2LineInventoryGroup": xdsl2LineInventoryGroup,
       "xdsl2LineConfTemplateGroup": xdsl2LineConfTemplateGroup,
       "xdsl2LineConfProfGroup": xdsl2LineConfProfGroup,
       "xdsl2LineConfProfRaGroup": xdsl2LineConfProfRaGroup,
       "xdsl2LineConfProfMsgMinGroup": xdsl2LineConfProfMsgMinGroup,
       "xdsl2LineConfProfModeSpecGroup": xdsl2LineConfProfModeSpecGroup,
       "xdsl2LineConfProfModeSpecBandUsGroup": xdsl2LineConfProfModeSpecBandUsGroup,
       "xdsl2ChConfProfileGroup": xdsl2ChConfProfileGroup,
       "xdsl2ChConfProfileAtmGroup": xdsl2ChConfProfileAtmGroup,
       "xdsl2ChConfProfileMinResGroup": xdsl2ChConfProfileMinResGroup,
       "xdsl2ChConfProfileOptAttrGroup": xdsl2ChConfProfileOptAttrGroup,
       "xdsl2LineAlarmConfTemplateGroup": xdsl2LineAlarmConfTemplateGroup,
       "xdsl2LineAlarmConfProfileGroup": xdsl2LineAlarmConfProfileGroup,
       "xdsl2ChAlarmConfProfileGroup": xdsl2ChAlarmConfProfileGroup,
       "xdsl2PMLineCurrGroup": xdsl2PMLineCurrGroup,
       "xdsl2PMLineInitCurrGroup": xdsl2PMLineInitCurrGroup,
       "xdsl2PMLineInitCurrShortGroup": xdsl2PMLineInitCurrShortGroup,
       "xdsl2PMLineHist15MinGroup": xdsl2PMLineHist15MinGroup,
       "xdsl2PMLineHist1DayGroup": xdsl2PMLineHist1DayGroup,
       "xdsl2PMLineInitHist15MinGroup": xdsl2PMLineInitHist15MinGroup,
       "xdsl2PMLineInitHist15MinShortGroup": xdsl2PMLineInitHist15MinShortGroup,
       "xdsl2PMLineInitHist1DayGroup": xdsl2PMLineInitHist1DayGroup,
       "xdsl2PMLineInitHist1DayShortGroup": xdsl2PMLineInitHist1DayShortGroup,
       "xdsl2PMChCurrGroup": xdsl2PMChCurrGroup,
       "xdsl2PMChHist15MinGroup": xdsl2PMChHist15MinGroup,
       "xdsl2PMChHist1DGroup": xdsl2PMChHist1DGroup,
       "xdsl2ScalarSCGroup": xdsl2ScalarSCGroup,
       "xdsl2ThreshNotificationGroup": xdsl2ThreshNotificationGroup,
       "xdsl2StatusChangeNotificationGroup": xdsl2StatusChangeNotificationGroup,
       "xdsl2Compliances": xdsl2Compliances,
       "xdsl2LineMibCompliance": xdsl2LineMibCompliance}
)
