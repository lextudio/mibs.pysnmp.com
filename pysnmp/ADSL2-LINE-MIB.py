# SNMP MIB module (ADSL2-LINE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ADSL2-LINE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:34:00 2024
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

(Adsl2ChAtmStatus,
 Adsl2ChPtmStatus,
 Adsl2ConfPmsForce,
 Adsl2Direction,
 Adsl2InitResult,
 Adsl2LConfProfPmMode,
 Adsl2LastTransmittedState,
 Adsl2LdsfResult,
 Adsl2LineLdsf,
 Adsl2LineStatus,
 Adsl2MaxBer,
 Adsl2OperationModes,
 Adsl2PowerMngState,
 Adsl2PsdMaskDs,
 Adsl2PsdMaskUs,
 Adsl2RaMode,
 Adsl2RfiDs,
 Adsl2ScMaskDs,
 Adsl2ScMaskUs,
 Adsl2SymbolProtection,
 Adsl2TransmissionModeType,
 Adsl2Tssi,
 Adsl2Unit) = mibBuilder.importSymbols(
    "ADSL2-LINE-TC-MIB",
    "Adsl2ChAtmStatus",
    "Adsl2ChPtmStatus",
    "Adsl2ConfPmsForce",
    "Adsl2Direction",
    "Adsl2InitResult",
    "Adsl2LConfProfPmMode",
    "Adsl2LastTransmittedState",
    "Adsl2LdsfResult",
    "Adsl2LineLdsf",
    "Adsl2LineStatus",
    "Adsl2MaxBer",
    "Adsl2OperationModes",
    "Adsl2PowerMngState",
    "Adsl2PsdMaskDs",
    "Adsl2PsdMaskUs",
    "Adsl2RaMode",
    "Adsl2RfiDs",
    "Adsl2ScMaskDs",
    "Adsl2ScMaskUs",
    "Adsl2SymbolProtection",
    "Adsl2TransmissionModeType",
    "Adsl2Tssi",
    "Adsl2Unit")

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


# MODULE-IDENTITY

adsl2MIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 10, 238)
)
adsl2MIB.setRevisions(
        ("2006-10-04 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Adsl2_ObjectIdentity = ObjectIdentity
adsl2 = _Adsl2_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 238, 1)
)
_Adsl2Notifications_ObjectIdentity = ObjectIdentity
adsl2Notifications = _Adsl2Notifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 0)
)
_Adsl2Line_ObjectIdentity = ObjectIdentity
adsl2Line = _Adsl2Line_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 1)
)
_Adsl2LineTable_Object = MibTable
adsl2LineTable = _Adsl2LineTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 1, 1)
)
if mibBuilder.loadTexts:
    adsl2LineTable.setStatus("current")
_Adsl2LineEntry_Object = MibTableRow
adsl2LineEntry = _Adsl2LineEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 1, 1, 1)
)
adsl2LineEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adsl2LineEntry.setStatus("current")


class _Adsl2LineCnfgTemplate_Type(SnmpAdminString):
    """Custom type adsl2LineCnfgTemplate based on SnmpAdminString"""
    defaultValue = OctetString("DEFVAL")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Adsl2LineCnfgTemplate_Type.__name__ = "SnmpAdminString"
_Adsl2LineCnfgTemplate_Object = MibTableColumn
adsl2LineCnfgTemplate = _Adsl2LineCnfgTemplate_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 1, 1, 1, 1),
    _Adsl2LineCnfgTemplate_Type()
)
adsl2LineCnfgTemplate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adsl2LineCnfgTemplate.setStatus("current")


class _Adsl2LineAlarmCnfgTemplate_Type(SnmpAdminString):
    """Custom type adsl2LineAlarmCnfgTemplate based on SnmpAdminString"""
    defaultValue = OctetString("DEFVAL")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Adsl2LineAlarmCnfgTemplate_Type.__name__ = "SnmpAdminString"
_Adsl2LineAlarmCnfgTemplate_Object = MibTableColumn
adsl2LineAlarmCnfgTemplate = _Adsl2LineAlarmCnfgTemplate_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 1, 1, 1, 2),
    _Adsl2LineAlarmCnfgTemplate_Type()
)
adsl2LineAlarmCnfgTemplate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adsl2LineAlarmCnfgTemplate.setStatus("current")


class _Adsl2LineCmndConfPmsf_Type(Adsl2ConfPmsForce):
    """Custom type adsl2LineCmndConfPmsf based on Adsl2ConfPmsForce"""


_Adsl2LineCmndConfPmsf_Object = MibTableColumn
adsl2LineCmndConfPmsf = _Adsl2LineCmndConfPmsf_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 1, 1, 1, 3),
    _Adsl2LineCmndConfPmsf_Type()
)
adsl2LineCmndConfPmsf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adsl2LineCmndConfPmsf.setStatus("current")


class _Adsl2LineCmndConfLdsf_Type(Adsl2LineLdsf):
    """Custom type adsl2LineCmndConfLdsf based on Adsl2LineLdsf"""


_Adsl2LineCmndConfLdsf_Object = MibTableColumn
adsl2LineCmndConfLdsf = _Adsl2LineCmndConfLdsf_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 1, 1, 1, 4),
    _Adsl2LineCmndConfLdsf_Type()
)
adsl2LineCmndConfLdsf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adsl2LineCmndConfLdsf.setStatus("current")


class _Adsl2LineCmndConfLdsfFailReason_Type(Adsl2LdsfResult):
    """Custom type adsl2LineCmndConfLdsfFailReason based on Adsl2LdsfResult"""


_Adsl2LineCmndConfLdsfFailReason_Object = MibTableColumn
adsl2LineCmndConfLdsfFailReason = _Adsl2LineCmndConfLdsfFailReason_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 1, 1, 1, 5),
    _Adsl2LineCmndConfLdsfFailReason_Type()
)
adsl2LineCmndConfLdsfFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2LineCmndConfLdsfFailReason.setStatus("current")


class _Adsl2LineCmndAutomodeColdStart_Type(TruthValue):
    """Custom type adsl2LineCmndAutomodeColdStart based on TruthValue"""


_Adsl2LineCmndAutomodeColdStart_Object = MibTableColumn
adsl2LineCmndAutomodeColdStart = _Adsl2LineCmndAutomodeColdStart_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 1, 1, 1, 6),
    _Adsl2LineCmndAutomodeColdStart_Type()
)
adsl2LineCmndAutomodeColdStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adsl2LineCmndAutomodeColdStart.setStatus("current")
_Adsl2LineStatusAtuTransSys_Type = Adsl2TransmissionModeType
_Adsl2LineStatusAtuTransSys_Object = MibTableColumn
adsl2LineStatusAtuTransSys = _Adsl2LineStatusAtuTransSys_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 1, 1, 1, 7),
    _Adsl2LineStatusAtuTransSys_Type()
)
adsl2LineStatusAtuTransSys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2LineStatusAtuTransSys.setStatus("current")
_Adsl2LineStatusPwrMngState_Type = Adsl2PowerMngState
_Adsl2LineStatusPwrMngState_Object = MibTableColumn
adsl2LineStatusPwrMngState = _Adsl2LineStatusPwrMngState_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 1, 1, 1, 8),
    _Adsl2LineStatusPwrMngState_Type()
)
adsl2LineStatusPwrMngState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2LineStatusPwrMngState.setStatus("current")
_Adsl2LineStatusInitResult_Type = Adsl2InitResult
_Adsl2LineStatusInitResult_Object = MibTableColumn
adsl2LineStatusInitResult = _Adsl2LineStatusInitResult_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 1, 1, 1, 9),
    _Adsl2LineStatusInitResult_Type()
)
adsl2LineStatusInitResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2LineStatusInitResult.setStatus("current")
_Adsl2LineStatusLastStateDs_Type = Adsl2LastTransmittedState
_Adsl2LineStatusLastStateDs_Object = MibTableColumn
adsl2LineStatusLastStateDs = _Adsl2LineStatusLastStateDs_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 1, 1, 1, 10),
    _Adsl2LineStatusLastStateDs_Type()
)
adsl2LineStatusLastStateDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2LineStatusLastStateDs.setStatus("current")
_Adsl2LineStatusLastStateUs_Type = Adsl2LastTransmittedState
_Adsl2LineStatusLastStateUs_Object = MibTableColumn
adsl2LineStatusLastStateUs = _Adsl2LineStatusLastStateUs_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 1, 1, 1, 11),
    _Adsl2LineStatusLastStateUs_Type()
)
adsl2LineStatusLastStateUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2LineStatusLastStateUs.setStatus("current")
_Adsl2LineStatusAtur_Type = Adsl2LineStatus
_Adsl2LineStatusAtur_Object = MibTableColumn
adsl2LineStatusAtur = _Adsl2LineStatusAtur_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 1, 1, 1, 12),
    _Adsl2LineStatusAtur_Type()
)
adsl2LineStatusAtur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2LineStatusAtur.setStatus("current")
_Adsl2LineStatusAtuc_Type = Adsl2LineStatus
_Adsl2LineStatusAtuc_Object = MibTableColumn
adsl2LineStatusAtuc = _Adsl2LineStatusAtuc_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 1, 1, 1, 13),
    _Adsl2LineStatusAtuc_Type()
)
adsl2LineStatusAtuc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2LineStatusAtuc.setStatus("current")


class _Adsl2LineStatusLnAttenDs_Type(Unsigned32):
    """Custom type adsl2LineStatusLnAttenDs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1270),
        ValueRangeConstraint(2147483646, 2147483646),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_Adsl2LineStatusLnAttenDs_Type.__name__ = "Unsigned32"
_Adsl2LineStatusLnAttenDs_Object = MibTableColumn
adsl2LineStatusLnAttenDs = _Adsl2LineStatusLnAttenDs_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 1, 1, 1, 14),
    _Adsl2LineStatusLnAttenDs_Type()
)
adsl2LineStatusLnAttenDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2LineStatusLnAttenDs.setStatus("current")
if mibBuilder.loadTexts:
    adsl2LineStatusLnAttenDs.setUnits("0.1 dB")


class _Adsl2LineStatusLnAttenUs_Type(Unsigned32):
    """Custom type adsl2LineStatusLnAttenUs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1270),
        ValueRangeConstraint(2147483646, 2147483646),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_Adsl2LineStatusLnAttenUs_Type.__name__ = "Unsigned32"
_Adsl2LineStatusLnAttenUs_Object = MibTableColumn
adsl2LineStatusLnAttenUs = _Adsl2LineStatusLnAttenUs_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 1, 1, 1, 15),
    _Adsl2LineStatusLnAttenUs_Type()
)
adsl2LineStatusLnAttenUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2LineStatusLnAttenUs.setStatus("current")
if mibBuilder.loadTexts:
    adsl2LineStatusLnAttenUs.setUnits("0.1 dB")


class _Adsl2LineStatusSigAttenDs_Type(Unsigned32):
    """Custom type adsl2LineStatusSigAttenDs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1270),
        ValueRangeConstraint(2147483646, 2147483646),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_Adsl2LineStatusSigAttenDs_Type.__name__ = "Unsigned32"
_Adsl2LineStatusSigAttenDs_Object = MibTableColumn
adsl2LineStatusSigAttenDs = _Adsl2LineStatusSigAttenDs_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 1, 1, 1, 16),
    _Adsl2LineStatusSigAttenDs_Type()
)
adsl2LineStatusSigAttenDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2LineStatusSigAttenDs.setStatus("current")
if mibBuilder.loadTexts:
    adsl2LineStatusSigAttenDs.setUnits("0.1 dB")


class _Adsl2LineStatusSigAttenUs_Type(Unsigned32):
    """Custom type adsl2LineStatusSigAttenUs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1270),
        ValueRangeConstraint(2147483646, 2147483646),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_Adsl2LineStatusSigAttenUs_Type.__name__ = "Unsigned32"
_Adsl2LineStatusSigAttenUs_Object = MibTableColumn
adsl2LineStatusSigAttenUs = _Adsl2LineStatusSigAttenUs_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 1, 1, 1, 17),
    _Adsl2LineStatusSigAttenUs_Type()
)
adsl2LineStatusSigAttenUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2LineStatusSigAttenUs.setStatus("current")
if mibBuilder.loadTexts:
    adsl2LineStatusSigAttenUs.setUnits("0.1 dB")


class _Adsl2LineStatusSnrMarginDs_Type(Integer32):
    """Custom type adsl2LineStatusSnrMarginDs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-640, 630),
        ValueRangeConstraint(2147483646, 2147483646),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_Adsl2LineStatusSnrMarginDs_Type.__name__ = "Integer32"
_Adsl2LineStatusSnrMarginDs_Object = MibTableColumn
adsl2LineStatusSnrMarginDs = _Adsl2LineStatusSnrMarginDs_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 1, 1, 1, 18),
    _Adsl2LineStatusSnrMarginDs_Type()
)
adsl2LineStatusSnrMarginDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2LineStatusSnrMarginDs.setStatus("current")
if mibBuilder.loadTexts:
    adsl2LineStatusSnrMarginDs.setUnits("0.1 dB")


class _Adsl2LineStatusSnrMarginUs_Type(Integer32):
    """Custom type adsl2LineStatusSnrMarginUs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-640, 630),
        ValueRangeConstraint(2147483646, 2147483646),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_Adsl2LineStatusSnrMarginUs_Type.__name__ = "Integer32"
_Adsl2LineStatusSnrMarginUs_Object = MibTableColumn
adsl2LineStatusSnrMarginUs = _Adsl2LineStatusSnrMarginUs_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 1, 1, 1, 19),
    _Adsl2LineStatusSnrMarginUs_Type()
)
adsl2LineStatusSnrMarginUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2LineStatusSnrMarginUs.setStatus("current")
if mibBuilder.loadTexts:
    adsl2LineStatusSnrMarginUs.setUnits("0.1 dB")
_Adsl2LineStatusAttainableRateDs_Type = Unsigned32
_Adsl2LineStatusAttainableRateDs_Object = MibTableColumn
adsl2LineStatusAttainableRateDs = _Adsl2LineStatusAttainableRateDs_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 1, 1, 1, 20),
    _Adsl2LineStatusAttainableRateDs_Type()
)
adsl2LineStatusAttainableRateDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2LineStatusAttainableRateDs.setStatus("current")
if mibBuilder.loadTexts:
    adsl2LineStatusAttainableRateDs.setUnits("bits/second")
_Adsl2LineStatusAttainableRateUs_Type = Unsigned32
_Adsl2LineStatusAttainableRateUs_Object = MibTableColumn
adsl2LineStatusAttainableRateUs = _Adsl2LineStatusAttainableRateUs_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 1, 1, 1, 21),
    _Adsl2LineStatusAttainableRateUs_Type()
)
adsl2LineStatusAttainableRateUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2LineStatusAttainableRateUs.setStatus("current")
if mibBuilder.loadTexts:
    adsl2LineStatusAttainableRateUs.setUnits("bits/second")


class _Adsl2LineStatusActPsdDs_Type(Integer32):
    """Custom type adsl2LineStatusActPsdDs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-900, 0),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_Adsl2LineStatusActPsdDs_Type.__name__ = "Integer32"
_Adsl2LineStatusActPsdDs_Object = MibTableColumn
adsl2LineStatusActPsdDs = _Adsl2LineStatusActPsdDs_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 1, 1, 1, 22),
    _Adsl2LineStatusActPsdDs_Type()
)
adsl2LineStatusActPsdDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2LineStatusActPsdDs.setStatus("current")
if mibBuilder.loadTexts:
    adsl2LineStatusActPsdDs.setUnits("0.1 dB")


class _Adsl2LineStatusActPsdUs_Type(Integer32):
    """Custom type adsl2LineStatusActPsdUs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-900, 0),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_Adsl2LineStatusActPsdUs_Type.__name__ = "Integer32"
_Adsl2LineStatusActPsdUs_Object = MibTableColumn
adsl2LineStatusActPsdUs = _Adsl2LineStatusActPsdUs_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 1, 1, 1, 23),
    _Adsl2LineStatusActPsdUs_Type()
)
adsl2LineStatusActPsdUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2LineStatusActPsdUs.setStatus("current")
if mibBuilder.loadTexts:
    adsl2LineStatusActPsdUs.setUnits("0.1 dB")


class _Adsl2LineStatusActAtpDs_Type(Integer32):
    """Custom type adsl2LineStatusActAtpDs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-310, 310),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_Adsl2LineStatusActAtpDs_Type.__name__ = "Integer32"
_Adsl2LineStatusActAtpDs_Object = MibTableColumn
adsl2LineStatusActAtpDs = _Adsl2LineStatusActAtpDs_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 1, 1, 1, 24),
    _Adsl2LineStatusActAtpDs_Type()
)
adsl2LineStatusActAtpDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2LineStatusActAtpDs.setStatus("current")
if mibBuilder.loadTexts:
    adsl2LineStatusActAtpDs.setUnits("0.1 dB")


class _Adsl2LineStatusActAtpUs_Type(Integer32):
    """Custom type adsl2LineStatusActAtpUs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-310, 310),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_Adsl2LineStatusActAtpUs_Type.__name__ = "Integer32"
_Adsl2LineStatusActAtpUs_Object = MibTableColumn
adsl2LineStatusActAtpUs = _Adsl2LineStatusActAtpUs_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 1, 1, 1, 25),
    _Adsl2LineStatusActAtpUs_Type()
)
adsl2LineStatusActAtpUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2LineStatusActAtpUs.setStatus("current")
if mibBuilder.loadTexts:
    adsl2LineStatusActAtpUs.setUnits("0.1 dB")
_Adsl2Status_ObjectIdentity = ObjectIdentity
adsl2Status = _Adsl2Status_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 2)
)
_Adsl2ChannelStatusTable_Object = MibTable
adsl2ChannelStatusTable = _Adsl2ChannelStatusTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 2, 1)
)
if mibBuilder.loadTexts:
    adsl2ChannelStatusTable.setStatus("current")
_Adsl2ChannelStatusEntry_Object = MibTableRow
adsl2ChannelStatusEntry = _Adsl2ChannelStatusEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 2, 1, 1)
)
adsl2ChannelStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADSL2-LINE-MIB", "adsl2ChStatusUnit"),
)
if mibBuilder.loadTexts:
    adsl2ChannelStatusEntry.setStatus("current")
_Adsl2ChStatusUnit_Type = Adsl2Unit
_Adsl2ChStatusUnit_Object = MibTableColumn
adsl2ChStatusUnit = _Adsl2ChStatusUnit_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 2, 1, 1, 1),
    _Adsl2ChStatusUnit_Type()
)
adsl2ChStatusUnit.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adsl2ChStatusUnit.setStatus("current")
_Adsl2ChStatusChannelNum_Type = Unsigned32
_Adsl2ChStatusChannelNum_Object = MibTableColumn
adsl2ChStatusChannelNum = _Adsl2ChStatusChannelNum_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 2, 1, 1, 2),
    _Adsl2ChStatusChannelNum_Type()
)
adsl2ChStatusChannelNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2ChStatusChannelNum.setStatus("current")


class _Adsl2ChStatusActDataRate_Type(Unsigned32):
    """Custom type adsl2ChStatusActDataRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Adsl2ChStatusActDataRate_Type.__name__ = "Unsigned32"
_Adsl2ChStatusActDataRate_Object = MibTableColumn
adsl2ChStatusActDataRate = _Adsl2ChStatusActDataRate_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 2, 1, 1, 3),
    _Adsl2ChStatusActDataRate_Type()
)
adsl2ChStatusActDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2ChStatusActDataRate.setStatus("current")
if mibBuilder.loadTexts:
    adsl2ChStatusActDataRate.setUnits("bits/second")


class _Adsl2ChStatusPrevDataRate_Type(Unsigned32):
    """Custom type adsl2ChStatusPrevDataRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Adsl2ChStatusPrevDataRate_Type.__name__ = "Unsigned32"
_Adsl2ChStatusPrevDataRate_Object = MibTableColumn
adsl2ChStatusPrevDataRate = _Adsl2ChStatusPrevDataRate_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 2, 1, 1, 4),
    _Adsl2ChStatusPrevDataRate_Type()
)
adsl2ChStatusPrevDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2ChStatusPrevDataRate.setStatus("current")
if mibBuilder.loadTexts:
    adsl2ChStatusPrevDataRate.setUnits("bits/second")


class _Adsl2ChStatusActDelay_Type(Unsigned32):
    """Custom type adsl2ChStatusActDelay based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8176),
    )


_Adsl2ChStatusActDelay_Type.__name__ = "Unsigned32"
_Adsl2ChStatusActDelay_Object = MibTableColumn
adsl2ChStatusActDelay = _Adsl2ChStatusActDelay_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 2, 1, 1, 5),
    _Adsl2ChStatusActDelay_Type()
)
adsl2ChStatusActDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2ChStatusActDelay.setStatus("current")
if mibBuilder.loadTexts:
    adsl2ChStatusActDelay.setUnits("milliseconds")
_Adsl2ChStatusAtmStatus_Type = Adsl2ChAtmStatus
_Adsl2ChStatusAtmStatus_Object = MibTableColumn
adsl2ChStatusAtmStatus = _Adsl2ChStatusAtmStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 2, 1, 1, 6),
    _Adsl2ChStatusAtmStatus_Type()
)
adsl2ChStatusAtmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2ChStatusAtmStatus.setStatus("current")
_Adsl2ChStatusPtmStatus_Type = Adsl2ChPtmStatus
_Adsl2ChStatusPtmStatus_Object = MibTableColumn
adsl2ChStatusPtmStatus = _Adsl2ChStatusPtmStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 2, 1, 1, 7),
    _Adsl2ChStatusPtmStatus_Type()
)
adsl2ChStatusPtmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2ChStatusPtmStatus.setStatus("current")
_Adsl2SCStatusTable_Object = MibTable
adsl2SCStatusTable = _Adsl2SCStatusTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 2, 2)
)
if mibBuilder.loadTexts:
    adsl2SCStatusTable.setStatus("current")
_Adsl2SCStatusEntry_Object = MibTableRow
adsl2SCStatusEntry = _Adsl2SCStatusEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 2, 2, 1)
)
adsl2SCStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADSL2-LINE-MIB", "adsl2SCStatusDirection"),
)
if mibBuilder.loadTexts:
    adsl2SCStatusEntry.setStatus("current")
_Adsl2SCStatusDirection_Type = Adsl2Direction
_Adsl2SCStatusDirection_Object = MibTableColumn
adsl2SCStatusDirection = _Adsl2SCStatusDirection_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 2, 2, 1, 1),
    _Adsl2SCStatusDirection_Type()
)
adsl2SCStatusDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adsl2SCStatusDirection.setStatus("current")
_Adsl2SCStatusMtime_Type = Unsigned32
_Adsl2SCStatusMtime_Object = MibTableColumn
adsl2SCStatusMtime = _Adsl2SCStatusMtime_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 2, 2, 1, 2),
    _Adsl2SCStatusMtime_Type()
)
adsl2SCStatusMtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2SCStatusMtime.setStatus("current")
if mibBuilder.loadTexts:
    adsl2SCStatusMtime.setUnits("symbols")


class _Adsl2SCStatusSnr_Type(OctetString):
    """Custom type adsl2SCStatusSnr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_Adsl2SCStatusSnr_Type.__name__ = "OctetString"
_Adsl2SCStatusSnr_Object = MibTableColumn
adsl2SCStatusSnr = _Adsl2SCStatusSnr_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 2, 2, 1, 3),
    _Adsl2SCStatusSnr_Type()
)
adsl2SCStatusSnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2SCStatusSnr.setStatus("current")


class _Adsl2SCStatusBitsAlloc_Type(OctetString):
    """Custom type adsl2SCStatusBitsAlloc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_Adsl2SCStatusBitsAlloc_Type.__name__ = "OctetString"
_Adsl2SCStatusBitsAlloc_Object = MibTableColumn
adsl2SCStatusBitsAlloc = _Adsl2SCStatusBitsAlloc_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 2, 2, 1, 4),
    _Adsl2SCStatusBitsAlloc_Type()
)
adsl2SCStatusBitsAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2SCStatusBitsAlloc.setStatus("current")
if mibBuilder.loadTexts:
    adsl2SCStatusBitsAlloc.setUnits("bits")


class _Adsl2SCStatusGainAlloc_Type(OctetString):
    """Custom type adsl2SCStatusGainAlloc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_Adsl2SCStatusGainAlloc_Type.__name__ = "OctetString"
_Adsl2SCStatusGainAlloc_Object = MibTableColumn
adsl2SCStatusGainAlloc = _Adsl2SCStatusGainAlloc_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 2, 2, 1, 5),
    _Adsl2SCStatusGainAlloc_Type()
)
adsl2SCStatusGainAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2SCStatusGainAlloc.setStatus("current")
_Adsl2SCStatusTssi_Type = Adsl2Tssi
_Adsl2SCStatusTssi_Object = MibTableColumn
adsl2SCStatusTssi = _Adsl2SCStatusTssi_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 2, 2, 1, 6),
    _Adsl2SCStatusTssi_Type()
)
adsl2SCStatusTssi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2SCStatusTssi.setStatus("current")
_Adsl2SCStatusLinScale_Type = Unsigned32
_Adsl2SCStatusLinScale_Object = MibTableColumn
adsl2SCStatusLinScale = _Adsl2SCStatusLinScale_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 2, 2, 1, 7),
    _Adsl2SCStatusLinScale_Type()
)
adsl2SCStatusLinScale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2SCStatusLinScale.setStatus("current")


class _Adsl2SCStatusLinReal_Type(OctetString):
    """Custom type adsl2SCStatusLinReal based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_Adsl2SCStatusLinReal_Type.__name__ = "OctetString"
_Adsl2SCStatusLinReal_Object = MibTableColumn
adsl2SCStatusLinReal = _Adsl2SCStatusLinReal_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 2, 2, 1, 8),
    _Adsl2SCStatusLinReal_Type()
)
adsl2SCStatusLinReal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2SCStatusLinReal.setStatus("current")


class _Adsl2SCStatusLinImg_Type(OctetString):
    """Custom type adsl2SCStatusLinImg based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_Adsl2SCStatusLinImg_Type.__name__ = "OctetString"
_Adsl2SCStatusLinImg_Object = MibTableColumn
adsl2SCStatusLinImg = _Adsl2SCStatusLinImg_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 2, 2, 1, 9),
    _Adsl2SCStatusLinImg_Type()
)
adsl2SCStatusLinImg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2SCStatusLinImg.setStatus("current")
_Adsl2SCStatusLogMt_Type = Unsigned32
_Adsl2SCStatusLogMt_Object = MibTableColumn
adsl2SCStatusLogMt = _Adsl2SCStatusLogMt_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 2, 2, 1, 10),
    _Adsl2SCStatusLogMt_Type()
)
adsl2SCStatusLogMt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2SCStatusLogMt.setStatus("current")


class _Adsl2SCStatusLog_Type(OctetString):
    """Custom type adsl2SCStatusLog based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_Adsl2SCStatusLog_Type.__name__ = "OctetString"
_Adsl2SCStatusLog_Object = MibTableColumn
adsl2SCStatusLog = _Adsl2SCStatusLog_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 2, 2, 1, 11),
    _Adsl2SCStatusLog_Type()
)
adsl2SCStatusLog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2SCStatusLog.setStatus("current")
_Adsl2SCStatusQlnMt_Type = Unsigned32
_Adsl2SCStatusQlnMt_Object = MibTableColumn
adsl2SCStatusQlnMt = _Adsl2SCStatusQlnMt_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 2, 2, 1, 12),
    _Adsl2SCStatusQlnMt_Type()
)
adsl2SCStatusQlnMt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2SCStatusQlnMt.setStatus("current")


class _Adsl2SCStatusQln_Type(OctetString):
    """Custom type adsl2SCStatusQln based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_Adsl2SCStatusQln_Type.__name__ = "OctetString"
_Adsl2SCStatusQln_Object = MibTableColumn
adsl2SCStatusQln = _Adsl2SCStatusQln_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 2, 2, 1, 13),
    _Adsl2SCStatusQln_Type()
)
adsl2SCStatusQln.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2SCStatusQln.setStatus("current")
if mibBuilder.loadTexts:
    adsl2SCStatusQln.setUnits("dBm/Hz")


class _Adsl2SCStatusLnAtten_Type(Unsigned32):
    """Custom type adsl2SCStatusLnAtten based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1270),
        ValueRangeConstraint(2147483646, 2147483646),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_Adsl2SCStatusLnAtten_Type.__name__ = "Unsigned32"
_Adsl2SCStatusLnAtten_Object = MibTableColumn
adsl2SCStatusLnAtten = _Adsl2SCStatusLnAtten_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 2, 2, 1, 14),
    _Adsl2SCStatusLnAtten_Type()
)
adsl2SCStatusLnAtten.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2SCStatusLnAtten.setStatus("current")
if mibBuilder.loadTexts:
    adsl2SCStatusLnAtten.setUnits("0.1 dB")


class _Adsl2SCStatusSigAtten_Type(Unsigned32):
    """Custom type adsl2SCStatusSigAtten based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1270),
        ValueRangeConstraint(2147483646, 2147483646),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_Adsl2SCStatusSigAtten_Type.__name__ = "Unsigned32"
_Adsl2SCStatusSigAtten_Object = MibTableColumn
adsl2SCStatusSigAtten = _Adsl2SCStatusSigAtten_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 2, 2, 1, 15),
    _Adsl2SCStatusSigAtten_Type()
)
adsl2SCStatusSigAtten.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2SCStatusSigAtten.setStatus("current")
if mibBuilder.loadTexts:
    adsl2SCStatusSigAtten.setUnits("0.1 dB")


class _Adsl2SCStatusSnrMargin_Type(Integer32):
    """Custom type adsl2SCStatusSnrMargin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-640, 630),
        ValueRangeConstraint(2147483646, 2147483646),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_Adsl2SCStatusSnrMargin_Type.__name__ = "Integer32"
_Adsl2SCStatusSnrMargin_Object = MibTableColumn
adsl2SCStatusSnrMargin = _Adsl2SCStatusSnrMargin_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 2, 2, 1, 16),
    _Adsl2SCStatusSnrMargin_Type()
)
adsl2SCStatusSnrMargin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2SCStatusSnrMargin.setStatus("current")
if mibBuilder.loadTexts:
    adsl2SCStatusSnrMargin.setUnits("0.1 dB")
_Adsl2SCStatusAttainableRate_Type = Unsigned32
_Adsl2SCStatusAttainableRate_Object = MibTableColumn
adsl2SCStatusAttainableRate = _Adsl2SCStatusAttainableRate_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 2, 2, 1, 17),
    _Adsl2SCStatusAttainableRate_Type()
)
adsl2SCStatusAttainableRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2SCStatusAttainableRate.setStatus("current")
if mibBuilder.loadTexts:
    adsl2SCStatusAttainableRate.setUnits("bits/second")
_Adsl2SCStatusActAtp_Type = Integer32
_Adsl2SCStatusActAtp_Object = MibTableColumn
adsl2SCStatusActAtp = _Adsl2SCStatusActAtp_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 2, 2, 1, 18),
    _Adsl2SCStatusActAtp_Type()
)
adsl2SCStatusActAtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2SCStatusActAtp.setStatus("current")
if mibBuilder.loadTexts:
    adsl2SCStatusActAtp.setUnits("0.1 dB")
_Adsl2SCStatusRowStatus_Type = RowStatus
_Adsl2SCStatusRowStatus_Object = MibTableColumn
adsl2SCStatusRowStatus = _Adsl2SCStatusRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 2, 2, 1, 19),
    _Adsl2SCStatusRowStatus_Type()
)
adsl2SCStatusRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2SCStatusRowStatus.setStatus("current")
_Adsl2Inventory_ObjectIdentity = ObjectIdentity
adsl2Inventory = _Adsl2Inventory_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 3)
)
_Adsl2LineInventoryTable_Object = MibTable
adsl2LineInventoryTable = _Adsl2LineInventoryTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 3, 1)
)
if mibBuilder.loadTexts:
    adsl2LineInventoryTable.setStatus("current")
_Adsl2LineInventoryEntry_Object = MibTableRow
adsl2LineInventoryEntry = _Adsl2LineInventoryEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 3, 1, 1)
)
adsl2LineInventoryEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADSL2-LINE-MIB", "adsl2LInvUnit"),
)
if mibBuilder.loadTexts:
    adsl2LineInventoryEntry.setStatus("current")
_Adsl2LInvUnit_Type = Adsl2Unit
_Adsl2LInvUnit_Object = MibTableColumn
adsl2LInvUnit = _Adsl2LInvUnit_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 3, 1, 1, 1),
    _Adsl2LInvUnit_Type()
)
adsl2LInvUnit.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adsl2LInvUnit.setStatus("current")


class _Adsl2LInvG994VendorId_Type(OctetString):
    """Custom type adsl2LInvG994VendorId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Adsl2LInvG994VendorId_Type.__name__ = "OctetString"
_Adsl2LInvG994VendorId_Object = MibTableColumn
adsl2LInvG994VendorId = _Adsl2LInvG994VendorId_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 3, 1, 1, 2),
    _Adsl2LInvG994VendorId_Type()
)
adsl2LInvG994VendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2LInvG994VendorId.setStatus("current")


class _Adsl2LInvSystemVendorId_Type(OctetString):
    """Custom type adsl2LInvSystemVendorId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_Adsl2LInvSystemVendorId_Type.__name__ = "OctetString"
_Adsl2LInvSystemVendorId_Object = MibTableColumn
adsl2LInvSystemVendorId = _Adsl2LInvSystemVendorId_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 3, 1, 1, 3),
    _Adsl2LInvSystemVendorId_Type()
)
adsl2LInvSystemVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2LInvSystemVendorId.setStatus("current")


class _Adsl2LInvVersionNumber_Type(OctetString):
    """Custom type adsl2LInvVersionNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Adsl2LInvVersionNumber_Type.__name__ = "OctetString"
_Adsl2LInvVersionNumber_Object = MibTableColumn
adsl2LInvVersionNumber = _Adsl2LInvVersionNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 3, 1, 1, 4),
    _Adsl2LInvVersionNumber_Type()
)
adsl2LInvVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2LInvVersionNumber.setStatus("current")


class _Adsl2LInvSerialNumber_Type(OctetString):
    """Custom type adsl2LInvSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Adsl2LInvSerialNumber_Type.__name__ = "OctetString"
_Adsl2LInvSerialNumber_Object = MibTableColumn
adsl2LInvSerialNumber = _Adsl2LInvSerialNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 3, 1, 1, 5),
    _Adsl2LInvSerialNumber_Type()
)
adsl2LInvSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2LInvSerialNumber.setStatus("current")
_Adsl2LInvSelfTestResult_Type = Unsigned32
_Adsl2LInvSelfTestResult_Object = MibTableColumn
adsl2LInvSelfTestResult = _Adsl2LInvSelfTestResult_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 3, 1, 1, 6),
    _Adsl2LInvSelfTestResult_Type()
)
adsl2LInvSelfTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2LInvSelfTestResult.setStatus("current")
_Adsl2LInvTransmissionCapabilities_Type = Adsl2TransmissionModeType
_Adsl2LInvTransmissionCapabilities_Object = MibTableColumn
adsl2LInvTransmissionCapabilities = _Adsl2LInvTransmissionCapabilities_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 3, 1, 1, 7),
    _Adsl2LInvTransmissionCapabilities_Type()
)
adsl2LInvTransmissionCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2LInvTransmissionCapabilities.setStatus("current")
_Adsl2PM_ObjectIdentity = ObjectIdentity
adsl2PM = _Adsl2PM_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4)
)
_Adsl2PMLine_ObjectIdentity = ObjectIdentity
adsl2PMLine = _Adsl2PMLine_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 1)
)
_Adsl2PMLineCurrTable_Object = MibTable
adsl2PMLineCurrTable = _Adsl2PMLineCurrTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    adsl2PMLineCurrTable.setStatus("current")
_Adsl2PMLineCurrEntry_Object = MibTableRow
adsl2PMLineCurrEntry = _Adsl2PMLineCurrEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 1, 1, 1)
)
adsl2PMLineCurrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADSL2-LINE-MIB", "adsl2PMLCurrUnit"),
)
if mibBuilder.loadTexts:
    adsl2PMLineCurrEntry.setStatus("current")
_Adsl2PMLCurrUnit_Type = Adsl2Unit
_Adsl2PMLCurrUnit_Object = MibTableColumn
adsl2PMLCurrUnit = _Adsl2PMLCurrUnit_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 1, 1, 1, 1),
    _Adsl2PMLCurrUnit_Type()
)
adsl2PMLCurrUnit.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adsl2PMLCurrUnit.setStatus("current")
_Adsl2PMLCurrValidIntervals_Type = Unsigned32
_Adsl2PMLCurrValidIntervals_Object = MibTableColumn
adsl2PMLCurrValidIntervals = _Adsl2PMLCurrValidIntervals_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 1, 1, 1, 2),
    _Adsl2PMLCurrValidIntervals_Type()
)
adsl2PMLCurrValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2PMLCurrValidIntervals.setStatus("current")
_Adsl2PMLCurrInvalidIntervals_Type = Unsigned32
_Adsl2PMLCurrInvalidIntervals_Object = MibTableColumn
adsl2PMLCurrInvalidIntervals = _Adsl2PMLCurrInvalidIntervals_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 1, 1, 1, 3),
    _Adsl2PMLCurrInvalidIntervals_Type()
)
adsl2PMLCurrInvalidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2PMLCurrInvalidIntervals.setStatus("current")
_Adsl2PMLCurr15MTimeElapsed_Type = HCPerfTimeElapsed
_Adsl2PMLCurr15MTimeElapsed_Object = MibTableColumn
adsl2PMLCurr15MTimeElapsed = _Adsl2PMLCurr15MTimeElapsed_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 1, 1, 1, 4),
    _Adsl2PMLCurr15MTimeElapsed_Type()
)
adsl2PMLCurr15MTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2PMLCurr15MTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    adsl2PMLCurr15MTimeElapsed.setUnits("seconds")
_Adsl2PMLCurr15MFecs_Type = Counter32
_Adsl2PMLCurr15MFecs_Object = MibTableColumn
adsl2PMLCurr15MFecs = _Adsl2PMLCurr15MFecs_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 1, 1, 1, 5),
    _Adsl2PMLCurr15MFecs_Type()
)
adsl2PMLCurr15MFecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2PMLCurr15MFecs.setStatus("current")
if mibBuilder.loadTexts:
    adsl2PMLCurr15MFecs.setUnits("seconds")
_Adsl2PMLCurr15MEs_Type = Counter32
_Adsl2PMLCurr15MEs_Object = MibTableColumn
adsl2PMLCurr15MEs = _Adsl2PMLCurr15MEs_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 1, 1, 1, 6),
    _Adsl2PMLCurr15MEs_Type()
)
adsl2PMLCurr15MEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2PMLCurr15MEs.setStatus("current")
if mibBuilder.loadTexts:
    adsl2PMLCurr15MEs.setUnits("seconds")
_Adsl2PMLCurr15MSes_Type = Counter32
_Adsl2PMLCurr15MSes_Object = MibTableColumn
adsl2PMLCurr15MSes = _Adsl2PMLCurr15MSes_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 1, 1, 1, 7),
    _Adsl2PMLCurr15MSes_Type()
)
adsl2PMLCurr15MSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2PMLCurr15MSes.setStatus("current")
if mibBuilder.loadTexts:
    adsl2PMLCurr15MSes.setUnits("seconds")
_Adsl2PMLCurr15MLoss_Type = Counter32
_Adsl2PMLCurr15MLoss_Object = MibTableColumn
adsl2PMLCurr15MLoss = _Adsl2PMLCurr15MLoss_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 1, 1, 1, 8),
    _Adsl2PMLCurr15MLoss_Type()
)
adsl2PMLCurr15MLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2PMLCurr15MLoss.setStatus("current")
if mibBuilder.loadTexts:
    adsl2PMLCurr15MLoss.setUnits("seconds")
_Adsl2PMLCurr15MUas_Type = Counter32
_Adsl2PMLCurr15MUas_Object = MibTableColumn
adsl2PMLCurr15MUas = _Adsl2PMLCurr15MUas_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 1, 1, 1, 9),
    _Adsl2PMLCurr15MUas_Type()
)
adsl2PMLCurr15MUas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2PMLCurr15MUas.setStatus("current")
if mibBuilder.loadTexts:
    adsl2PMLCurr15MUas.setUnits("seconds")
_Adsl2PMLCurr1DayValidIntervals_Type = Unsigned32
_Adsl2PMLCurr1DayValidIntervals_Object = MibTableColumn
adsl2PMLCurr1DayValidIntervals = _Adsl2PMLCurr1DayValidIntervals_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 1, 1, 1, 10),
    _Adsl2PMLCurr1DayValidIntervals_Type()
)
adsl2PMLCurr1DayValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2PMLCurr1DayValidIntervals.setStatus("current")
_Adsl2PMLCurr1DayInvalidIntervals_Type = Unsigned32
_Adsl2PMLCurr1DayInvalidIntervals_Object = MibTableColumn
adsl2PMLCurr1DayInvalidIntervals = _Adsl2PMLCurr1DayInvalidIntervals_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 1, 1, 1, 11),
    _Adsl2PMLCurr1DayInvalidIntervals_Type()
)
adsl2PMLCurr1DayInvalidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2PMLCurr1DayInvalidIntervals.setStatus("current")
_Adsl2PMLCurr1DayTimeElapsed_Type = HCPerfTimeElapsed
_Adsl2PMLCurr1DayTimeElapsed_Object = MibTableColumn
adsl2PMLCurr1DayTimeElapsed = _Adsl2PMLCurr1DayTimeElapsed_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 1, 1, 1, 12),
    _Adsl2PMLCurr1DayTimeElapsed_Type()
)
adsl2PMLCurr1DayTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2PMLCurr1DayTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    adsl2PMLCurr1DayTimeElapsed.setUnits("seconds")
_Adsl2PMLCurr1DayFecs_Type = Counter32
_Adsl2PMLCurr1DayFecs_Object = MibTableColumn
adsl2PMLCurr1DayFecs = _Adsl2PMLCurr1DayFecs_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 1, 1, 1, 13),
    _Adsl2PMLCurr1DayFecs_Type()
)
adsl2PMLCurr1DayFecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2PMLCurr1DayFecs.setStatus("current")
if mibBuilder.loadTexts:
    adsl2PMLCurr1DayFecs.setUnits("seconds")
_Adsl2PMLCurr1DayEs_Type = Counter32
_Adsl2PMLCurr1DayEs_Object = MibTableColumn
adsl2PMLCurr1DayEs = _Adsl2PMLCurr1DayEs_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 1, 1, 1, 14),
    _Adsl2PMLCurr1DayEs_Type()
)
adsl2PMLCurr1DayEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2PMLCurr1DayEs.setStatus("current")
if mibBuilder.loadTexts:
    adsl2PMLCurr1DayEs.setUnits("seconds")
_Adsl2PMLCurr1DaySes_Type = Counter32
_Adsl2PMLCurr1DaySes_Object = MibTableColumn
adsl2PMLCurr1DaySes = _Adsl2PMLCurr1DaySes_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 1, 1, 1, 15),
    _Adsl2PMLCurr1DaySes_Type()
)
adsl2PMLCurr1DaySes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2PMLCurr1DaySes.setStatus("current")
if mibBuilder.loadTexts:
    adsl2PMLCurr1DaySes.setUnits("seconds")
_Adsl2PMLCurr1DayLoss_Type = Counter32
_Adsl2PMLCurr1DayLoss_Object = MibTableColumn
adsl2PMLCurr1DayLoss = _Adsl2PMLCurr1DayLoss_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 1, 1, 1, 16),
    _Adsl2PMLCurr1DayLoss_Type()
)
adsl2PMLCurr1DayLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2PMLCurr1DayLoss.setStatus("current")
if mibBuilder.loadTexts:
    adsl2PMLCurr1DayLoss.setUnits("seconds")
_Adsl2PMLCurr1DayUas_Type = Counter32
_Adsl2PMLCurr1DayUas_Object = MibTableColumn
adsl2PMLCurr1DayUas = _Adsl2PMLCurr1DayUas_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 1, 1, 1, 17),
    _Adsl2PMLCurr1DayUas_Type()
)
adsl2PMLCurr1DayUas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2PMLCurr1DayUas.setStatus("current")
if mibBuilder.loadTexts:
    adsl2PMLCurr1DayUas.setUnits("seconds")
_Adsl2PMLineCurrInitTable_Object = MibTable
adsl2PMLineCurrInitTable = _Adsl2PMLineCurrInitTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 1, 2)
)
if mibBuilder.loadTexts:
    adsl2PMLineCurrInitTable.setStatus("current")
_Adsl2PMLineCurrInitEntry_Object = MibTableRow
adsl2PMLineCurrInitEntry = _Adsl2PMLineCurrInitEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 1, 2, 1)
)
adsl2PMLineCurrInitEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adsl2PMLineCurrInitEntry.setStatus("current")
_Adsl2PMLCurrInit15MTimeElapsed_Type = Unsigned32
_Adsl2PMLCurrInit15MTimeElapsed_Object = MibTableColumn
adsl2PMLCurrInit15MTimeElapsed = _Adsl2PMLCurrInit15MTimeElapsed_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 1, 2, 1, 1),
    _Adsl2PMLCurrInit15MTimeElapsed_Type()
)
adsl2PMLCurrInit15MTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2PMLCurrInit15MTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    adsl2PMLCurrInit15MTimeElapsed.setUnits("seconds")
_Adsl2PMLCurrInit15MFullInits_Type = Unsigned32
_Adsl2PMLCurrInit15MFullInits_Object = MibTableColumn
adsl2PMLCurrInit15MFullInits = _Adsl2PMLCurrInit15MFullInits_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 1, 2, 1, 2),
    _Adsl2PMLCurrInit15MFullInits_Type()
)
adsl2PMLCurrInit15MFullInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2PMLCurrInit15MFullInits.setStatus("current")
_Adsl2PMLCurrInit15MFailedFullInits_Type = Unsigned32
_Adsl2PMLCurrInit15MFailedFullInits_Object = MibTableColumn
adsl2PMLCurrInit15MFailedFullInits = _Adsl2PMLCurrInit15MFailedFullInits_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 1, 2, 1, 3),
    _Adsl2PMLCurrInit15MFailedFullInits_Type()
)
adsl2PMLCurrInit15MFailedFullInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2PMLCurrInit15MFailedFullInits.setStatus("current")
_Adsl2PMLCurrInit15MShortInits_Type = Unsigned32
_Adsl2PMLCurrInit15MShortInits_Object = MibTableColumn
adsl2PMLCurrInit15MShortInits = _Adsl2PMLCurrInit15MShortInits_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 1, 2, 1, 4),
    _Adsl2PMLCurrInit15MShortInits_Type()
)
adsl2PMLCurrInit15MShortInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2PMLCurrInit15MShortInits.setStatus("current")
_Adsl2PMLCurrInit15MFailedShortInits_Type = Unsigned32
_Adsl2PMLCurrInit15MFailedShortInits_Object = MibTableColumn
adsl2PMLCurrInit15MFailedShortInits = _Adsl2PMLCurrInit15MFailedShortInits_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 1, 2, 1, 5),
    _Adsl2PMLCurrInit15MFailedShortInits_Type()
)
adsl2PMLCurrInit15MFailedShortInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2PMLCurrInit15MFailedShortInits.setStatus("current")
_Adsl2PMLCurrInit1DayTimeElapsed_Type = Unsigned32
_Adsl2PMLCurrInit1DayTimeElapsed_Object = MibTableColumn
adsl2PMLCurrInit1DayTimeElapsed = _Adsl2PMLCurrInit1DayTimeElapsed_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 1, 2, 1, 6),
    _Adsl2PMLCurrInit1DayTimeElapsed_Type()
)
adsl2PMLCurrInit1DayTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2PMLCurrInit1DayTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    adsl2PMLCurrInit1DayTimeElapsed.setUnits("seconds")
_Adsl2PMLCurrInit1DayFullInits_Type = Unsigned32
_Adsl2PMLCurrInit1DayFullInits_Object = MibTableColumn
adsl2PMLCurrInit1DayFullInits = _Adsl2PMLCurrInit1DayFullInits_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 1, 2, 1, 7),
    _Adsl2PMLCurrInit1DayFullInits_Type()
)
adsl2PMLCurrInit1DayFullInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2PMLCurrInit1DayFullInits.setStatus("current")
_Adsl2PMLCurrInit1DayFailedFullInits_Type = Unsigned32
_Adsl2PMLCurrInit1DayFailedFullInits_Object = MibTableColumn
adsl2PMLCurrInit1DayFailedFullInits = _Adsl2PMLCurrInit1DayFailedFullInits_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 1, 2, 1, 8),
    _Adsl2PMLCurrInit1DayFailedFullInits_Type()
)
adsl2PMLCurrInit1DayFailedFullInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2PMLCurrInit1DayFailedFullInits.setStatus("current")
_Adsl2PMLCurrInit1DayShortInits_Type = Unsigned32
_Adsl2PMLCurrInit1DayShortInits_Object = MibTableColumn
adsl2PMLCurrInit1DayShortInits = _Adsl2PMLCurrInit1DayShortInits_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 1, 2, 1, 9),
    _Adsl2PMLCurrInit1DayShortInits_Type()
)
adsl2PMLCurrInit1DayShortInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2PMLCurrInit1DayShortInits.setStatus("current")
_Adsl2PMLCurrInit1DayFailedShortInits_Type = Unsigned32
_Adsl2PMLCurrInit1DayFailedShortInits_Object = MibTableColumn
adsl2PMLCurrInit1DayFailedShortInits = _Adsl2PMLCurrInit1DayFailedShortInits_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 1, 2, 1, 10),
    _Adsl2PMLCurrInit1DayFailedShortInits_Type()
)
adsl2PMLCurrInit1DayFailedShortInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2PMLCurrInit1DayFailedShortInits.setStatus("current")
_Adsl2PMLineHist15MinTable_Object = MibTable
adsl2PMLineHist15MinTable = _Adsl2PMLineHist15MinTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 1, 3)
)
if mibBuilder.loadTexts:
    adsl2PMLineHist15MinTable.setStatus("current")
_Adsl2PMLineHist15MinEntry_Object = MibTableRow
adsl2PMLineHist15MinEntry = _Adsl2PMLineHist15MinEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 1, 3, 1)
)
adsl2PMLineHist15MinEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADSL2-LINE-MIB", "adsl2PMLHist15MUnit"),
    (0, "ADSL2-LINE-MIB", "adsl2PMLHist15MInterval"),
)
if mibBuilder.loadTexts:
    adsl2PMLineHist15MinEntry.setStatus("current")
_Adsl2PMLHist15MUnit_Type = Adsl2Unit
_Adsl2PMLHist15MUnit_Object = MibTableColumn
adsl2PMLHist15MUnit = _Adsl2PMLHist15MUnit_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 1, 3, 1, 1),
    _Adsl2PMLHist15MUnit_Type()
)
adsl2PMLHist15MUnit.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adsl2PMLHist15MUnit.setStatus("current")


class _Adsl2PMLHist15MInterval_Type(Unsigned32):
    """Custom type adsl2PMLHist15MInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_Adsl2PMLHist15MInterval_Type.__name__ = "Unsigned32"
_Adsl2PMLHist15MInterval_Object = MibTableColumn
adsl2PMLHist15MInterval = _Adsl2PMLHist15MInterval_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 1, 3, 1, 2),
    _Adsl2PMLHist15MInterval_Type()
)
adsl2PMLHist15MInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adsl2PMLHist15MInterval.setStatus("current")
_Adsl2PMLHist15MMonitoredTime_Type = Unsigned32
_Adsl2PMLHist15MMonitoredTime_Object = MibTableColumn
adsl2PMLHist15MMonitoredTime = _Adsl2PMLHist15MMonitoredTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 1, 3, 1, 3),
    _Adsl2PMLHist15MMonitoredTime_Type()
)
adsl2PMLHist15MMonitoredTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2PMLHist15MMonitoredTime.setStatus("current")
if mibBuilder.loadTexts:
    adsl2PMLHist15MMonitoredTime.setUnits("seconds")
_Adsl2PMLHist15MFecs_Type = Counter32
_Adsl2PMLHist15MFecs_Object = MibTableColumn
adsl2PMLHist15MFecs = _Adsl2PMLHist15MFecs_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 1, 3, 1, 4),
    _Adsl2PMLHist15MFecs_Type()
)
adsl2PMLHist15MFecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2PMLHist15MFecs.setStatus("current")
if mibBuilder.loadTexts:
    adsl2PMLHist15MFecs.setUnits("seconds")
_Adsl2PMLHist15MEs_Type = Counter32
_Adsl2PMLHist15MEs_Object = MibTableColumn
adsl2PMLHist15MEs = _Adsl2PMLHist15MEs_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 1, 3, 1, 5),
    _Adsl2PMLHist15MEs_Type()
)
adsl2PMLHist15MEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2PMLHist15MEs.setStatus("current")
if mibBuilder.loadTexts:
    adsl2PMLHist15MEs.setUnits("seconds")
_Adsl2PMLHist15MSes_Type = Counter32
_Adsl2PMLHist15MSes_Object = MibTableColumn
adsl2PMLHist15MSes = _Adsl2PMLHist15MSes_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 1, 3, 1, 6),
    _Adsl2PMLHist15MSes_Type()
)
adsl2PMLHist15MSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2PMLHist15MSes.setStatus("current")
if mibBuilder.loadTexts:
    adsl2PMLHist15MSes.setUnits("seconds")
_Adsl2PMLHist15MLoss_Type = Counter32
_Adsl2PMLHist15MLoss_Object = MibTableColumn
adsl2PMLHist15MLoss = _Adsl2PMLHist15MLoss_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 1, 3, 1, 7),
    _Adsl2PMLHist15MLoss_Type()
)
adsl2PMLHist15MLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2PMLHist15MLoss.setStatus("current")
if mibBuilder.loadTexts:
    adsl2PMLHist15MLoss.setUnits("seconds")
_Adsl2PMLHist15MUas_Type = Counter32
_Adsl2PMLHist15MUas_Object = MibTableColumn
adsl2PMLHist15MUas = _Adsl2PMLHist15MUas_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 1, 3, 1, 8),
    _Adsl2PMLHist15MUas_Type()
)
adsl2PMLHist15MUas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2PMLHist15MUas.setStatus("current")
if mibBuilder.loadTexts:
    adsl2PMLHist15MUas.setUnits("seconds")
_Adsl2PMLHist15MValidInterval_Type = TruthValue
_Adsl2PMLHist15MValidInterval_Object = MibTableColumn
adsl2PMLHist15MValidInterval = _Adsl2PMLHist15MValidInterval_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 1, 3, 1, 9),
    _Adsl2PMLHist15MValidInterval_Type()
)
adsl2PMLHist15MValidInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2PMLHist15MValidInterval.setStatus("current")
_Adsl2PMLineHist1DayTable_Object = MibTable
adsl2PMLineHist1DayTable = _Adsl2PMLineHist1DayTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 1, 4)
)
if mibBuilder.loadTexts:
    adsl2PMLineHist1DayTable.setStatus("current")
_Adsl2PMLineHist1DayEntry_Object = MibTableRow
adsl2PMLineHist1DayEntry = _Adsl2PMLineHist1DayEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 1, 4, 1)
)
adsl2PMLineHist1DayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADSL2-LINE-MIB", "adsl2PMLHist1DUnit"),
    (0, "ADSL2-LINE-MIB", "adsl2PMLHist1DInterval"),
)
if mibBuilder.loadTexts:
    adsl2PMLineHist1DayEntry.setStatus("current")
_Adsl2PMLHist1DUnit_Type = Adsl2Unit
_Adsl2PMLHist1DUnit_Object = MibTableColumn
adsl2PMLHist1DUnit = _Adsl2PMLHist1DUnit_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 1, 4, 1, 1),
    _Adsl2PMLHist1DUnit_Type()
)
adsl2PMLHist1DUnit.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adsl2PMLHist1DUnit.setStatus("current")


class _Adsl2PMLHist1DInterval_Type(Unsigned32):
    """Custom type adsl2PMLHist1DInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_Adsl2PMLHist1DInterval_Type.__name__ = "Unsigned32"
_Adsl2PMLHist1DInterval_Object = MibTableColumn
adsl2PMLHist1DInterval = _Adsl2PMLHist1DInterval_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 1, 4, 1, 2),
    _Adsl2PMLHist1DInterval_Type()
)
adsl2PMLHist1DInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adsl2PMLHist1DInterval.setStatus("current")
_Adsl2PMLHist1DMonitoredTime_Type = Unsigned32
_Adsl2PMLHist1DMonitoredTime_Object = MibTableColumn
adsl2PMLHist1DMonitoredTime = _Adsl2PMLHist1DMonitoredTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 1, 4, 1, 3),
    _Adsl2PMLHist1DMonitoredTime_Type()
)
adsl2PMLHist1DMonitoredTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2PMLHist1DMonitoredTime.setStatus("current")
if mibBuilder.loadTexts:
    adsl2PMLHist1DMonitoredTime.setUnits("seconds")
_Adsl2PMLHist1DFecs_Type = Counter32
_Adsl2PMLHist1DFecs_Object = MibTableColumn
adsl2PMLHist1DFecs = _Adsl2PMLHist1DFecs_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 1, 4, 1, 4),
    _Adsl2PMLHist1DFecs_Type()
)
adsl2PMLHist1DFecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2PMLHist1DFecs.setStatus("current")
if mibBuilder.loadTexts:
    adsl2PMLHist1DFecs.setUnits("seconds")
_Adsl2PMLHist1DEs_Type = Counter32
_Adsl2PMLHist1DEs_Object = MibTableColumn
adsl2PMLHist1DEs = _Adsl2PMLHist1DEs_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 1, 4, 1, 5),
    _Adsl2PMLHist1DEs_Type()
)
adsl2PMLHist1DEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2PMLHist1DEs.setStatus("current")
if mibBuilder.loadTexts:
    adsl2PMLHist1DEs.setUnits("seconds")
_Adsl2PMLHist1DSes_Type = Counter32
_Adsl2PMLHist1DSes_Object = MibTableColumn
adsl2PMLHist1DSes = _Adsl2PMLHist1DSes_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 1, 4, 1, 6),
    _Adsl2PMLHist1DSes_Type()
)
adsl2PMLHist1DSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2PMLHist1DSes.setStatus("current")
if mibBuilder.loadTexts:
    adsl2PMLHist1DSes.setUnits("seconds")
_Adsl2PMLHist1DLoss_Type = Counter32
_Adsl2PMLHist1DLoss_Object = MibTableColumn
adsl2PMLHist1DLoss = _Adsl2PMLHist1DLoss_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 1, 4, 1, 7),
    _Adsl2PMLHist1DLoss_Type()
)
adsl2PMLHist1DLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2PMLHist1DLoss.setStatus("current")
if mibBuilder.loadTexts:
    adsl2PMLHist1DLoss.setUnits("seconds")
_Adsl2PMLHist1DUas_Type = Counter32
_Adsl2PMLHist1DUas_Object = MibTableColumn
adsl2PMLHist1DUas = _Adsl2PMLHist1DUas_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 1, 4, 1, 8),
    _Adsl2PMLHist1DUas_Type()
)
adsl2PMLHist1DUas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2PMLHist1DUas.setStatus("current")
if mibBuilder.loadTexts:
    adsl2PMLHist1DUas.setUnits("seconds")
_Adsl2PMLHist1DValidInterval_Type = TruthValue
_Adsl2PMLHist1DValidInterval_Object = MibTableColumn
adsl2PMLHist1DValidInterval = _Adsl2PMLHist1DValidInterval_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 1, 4, 1, 9),
    _Adsl2PMLHist1DValidInterval_Type()
)
adsl2PMLHist1DValidInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2PMLHist1DValidInterval.setStatus("current")
_Adsl2PMLineInitHist15MinTable_Object = MibTable
adsl2PMLineInitHist15MinTable = _Adsl2PMLineInitHist15MinTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 1, 5)
)
if mibBuilder.loadTexts:
    adsl2PMLineInitHist15MinTable.setStatus("current")
_Adsl2PMLineInitHist15MinEntry_Object = MibTableRow
adsl2PMLineInitHist15MinEntry = _Adsl2PMLineInitHist15MinEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 1, 5, 1)
)
adsl2PMLineInitHist15MinEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADSL2-LINE-MIB", "adsl2PMLHistInit15MInterval"),
)
if mibBuilder.loadTexts:
    adsl2PMLineInitHist15MinEntry.setStatus("current")


class _Adsl2PMLHistInit15MInterval_Type(Unsigned32):
    """Custom type adsl2PMLHistInit15MInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_Adsl2PMLHistInit15MInterval_Type.__name__ = "Unsigned32"
_Adsl2PMLHistInit15MInterval_Object = MibTableColumn
adsl2PMLHistInit15MInterval = _Adsl2PMLHistInit15MInterval_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 1, 5, 1, 1),
    _Adsl2PMLHistInit15MInterval_Type()
)
adsl2PMLHistInit15MInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adsl2PMLHistInit15MInterval.setStatus("current")
_Adsl2PMLHistInit15MMonitoredTime_Type = Unsigned32
_Adsl2PMLHistInit15MMonitoredTime_Object = MibTableColumn
adsl2PMLHistInit15MMonitoredTime = _Adsl2PMLHistInit15MMonitoredTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 1, 5, 1, 2),
    _Adsl2PMLHistInit15MMonitoredTime_Type()
)
adsl2PMLHistInit15MMonitoredTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2PMLHistInit15MMonitoredTime.setStatus("current")
if mibBuilder.loadTexts:
    adsl2PMLHistInit15MMonitoredTime.setUnits("seconds")
_Adsl2PMLHistInit15MFullInits_Type = Unsigned32
_Adsl2PMLHistInit15MFullInits_Object = MibTableColumn
adsl2PMLHistInit15MFullInits = _Adsl2PMLHistInit15MFullInits_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 1, 5, 1, 3),
    _Adsl2PMLHistInit15MFullInits_Type()
)
adsl2PMLHistInit15MFullInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2PMLHistInit15MFullInits.setStatus("current")
_Adsl2PMLHistInit15MFailedFullInits_Type = Unsigned32
_Adsl2PMLHistInit15MFailedFullInits_Object = MibTableColumn
adsl2PMLHistInit15MFailedFullInits = _Adsl2PMLHistInit15MFailedFullInits_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 1, 5, 1, 4),
    _Adsl2PMLHistInit15MFailedFullInits_Type()
)
adsl2PMLHistInit15MFailedFullInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2PMLHistInit15MFailedFullInits.setStatus("current")
_Adsl2PMLHistInit15MShortInits_Type = Unsigned32
_Adsl2PMLHistInit15MShortInits_Object = MibTableColumn
adsl2PMLHistInit15MShortInits = _Adsl2PMLHistInit15MShortInits_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 1, 5, 1, 5),
    _Adsl2PMLHistInit15MShortInits_Type()
)
adsl2PMLHistInit15MShortInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2PMLHistInit15MShortInits.setStatus("current")
_Adsl2PMLHistInit15MFailedShortInits_Type = Unsigned32
_Adsl2PMLHistInit15MFailedShortInits_Object = MibTableColumn
adsl2PMLHistInit15MFailedShortInits = _Adsl2PMLHistInit15MFailedShortInits_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 1, 5, 1, 6),
    _Adsl2PMLHistInit15MFailedShortInits_Type()
)
adsl2PMLHistInit15MFailedShortInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2PMLHistInit15MFailedShortInits.setStatus("current")
_Adsl2PMLHistInit15MValidInterval_Type = TruthValue
_Adsl2PMLHistInit15MValidInterval_Object = MibTableColumn
adsl2PMLHistInit15MValidInterval = _Adsl2PMLHistInit15MValidInterval_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 1, 5, 1, 7),
    _Adsl2PMLHistInit15MValidInterval_Type()
)
adsl2PMLHistInit15MValidInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2PMLHistInit15MValidInterval.setStatus("current")
_Adsl2PMLineInitHist1DayTable_Object = MibTable
adsl2PMLineInitHist1DayTable = _Adsl2PMLineInitHist1DayTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 1, 6)
)
if mibBuilder.loadTexts:
    adsl2PMLineInitHist1DayTable.setStatus("current")
_Adsl2PMLineInitHist1DayEntry_Object = MibTableRow
adsl2PMLineInitHist1DayEntry = _Adsl2PMLineInitHist1DayEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 1, 6, 1)
)
adsl2PMLineInitHist1DayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADSL2-LINE-MIB", "adsl2PMLHistinit1DInterval"),
)
if mibBuilder.loadTexts:
    adsl2PMLineInitHist1DayEntry.setStatus("current")


class _Adsl2PMLHistinit1DInterval_Type(Unsigned32):
    """Custom type adsl2PMLHistinit1DInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_Adsl2PMLHistinit1DInterval_Type.__name__ = "Unsigned32"
_Adsl2PMLHistinit1DInterval_Object = MibTableColumn
adsl2PMLHistinit1DInterval = _Adsl2PMLHistinit1DInterval_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 1, 6, 1, 1),
    _Adsl2PMLHistinit1DInterval_Type()
)
adsl2PMLHistinit1DInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adsl2PMLHistinit1DInterval.setStatus("current")
_Adsl2PMLHistinit1DMonitoredTime_Type = Unsigned32
_Adsl2PMLHistinit1DMonitoredTime_Object = MibTableColumn
adsl2PMLHistinit1DMonitoredTime = _Adsl2PMLHistinit1DMonitoredTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 1, 6, 1, 2),
    _Adsl2PMLHistinit1DMonitoredTime_Type()
)
adsl2PMLHistinit1DMonitoredTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2PMLHistinit1DMonitoredTime.setStatus("current")
if mibBuilder.loadTexts:
    adsl2PMLHistinit1DMonitoredTime.setUnits("seconds")
_Adsl2PMLHistinit1DFullInits_Type = Unsigned32
_Adsl2PMLHistinit1DFullInits_Object = MibTableColumn
adsl2PMLHistinit1DFullInits = _Adsl2PMLHistinit1DFullInits_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 1, 6, 1, 3),
    _Adsl2PMLHistinit1DFullInits_Type()
)
adsl2PMLHistinit1DFullInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2PMLHistinit1DFullInits.setStatus("current")
_Adsl2PMLHistinit1DFailedFullInits_Type = Unsigned32
_Adsl2PMLHistinit1DFailedFullInits_Object = MibTableColumn
adsl2PMLHistinit1DFailedFullInits = _Adsl2PMLHistinit1DFailedFullInits_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 1, 6, 1, 4),
    _Adsl2PMLHistinit1DFailedFullInits_Type()
)
adsl2PMLHistinit1DFailedFullInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2PMLHistinit1DFailedFullInits.setStatus("current")
_Adsl2PMLHistinit1DShortInits_Type = Unsigned32
_Adsl2PMLHistinit1DShortInits_Object = MibTableColumn
adsl2PMLHistinit1DShortInits = _Adsl2PMLHistinit1DShortInits_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 1, 6, 1, 5),
    _Adsl2PMLHistinit1DShortInits_Type()
)
adsl2PMLHistinit1DShortInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2PMLHistinit1DShortInits.setStatus("current")
_Adsl2PMLHistinit1DFailedShortInits_Type = Unsigned32
_Adsl2PMLHistinit1DFailedShortInits_Object = MibTableColumn
adsl2PMLHistinit1DFailedShortInits = _Adsl2PMLHistinit1DFailedShortInits_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 1, 6, 1, 6),
    _Adsl2PMLHistinit1DFailedShortInits_Type()
)
adsl2PMLHistinit1DFailedShortInits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2PMLHistinit1DFailedShortInits.setStatus("current")
_Adsl2PMLHistinit1DValidInterval_Type = TruthValue
_Adsl2PMLHistinit1DValidInterval_Object = MibTableColumn
adsl2PMLHistinit1DValidInterval = _Adsl2PMLHistinit1DValidInterval_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 1, 6, 1, 7),
    _Adsl2PMLHistinit1DValidInterval_Type()
)
adsl2PMLHistinit1DValidInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2PMLHistinit1DValidInterval.setStatus("current")
_Adsl2PMChannel_ObjectIdentity = ObjectIdentity
adsl2PMChannel = _Adsl2PMChannel_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 2)
)
_Adsl2PMChCurrTable_Object = MibTable
adsl2PMChCurrTable = _Adsl2PMChCurrTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    adsl2PMChCurrTable.setStatus("current")
_Adsl2PMChCurrEntry_Object = MibTableRow
adsl2PMChCurrEntry = _Adsl2PMChCurrEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 2, 1, 1)
)
adsl2PMChCurrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADSL2-LINE-MIB", "adsl2PMChCurrUnit"),
)
if mibBuilder.loadTexts:
    adsl2PMChCurrEntry.setStatus("current")
_Adsl2PMChCurrUnit_Type = Adsl2Unit
_Adsl2PMChCurrUnit_Object = MibTableColumn
adsl2PMChCurrUnit = _Adsl2PMChCurrUnit_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 2, 1, 1, 1),
    _Adsl2PMChCurrUnit_Type()
)
adsl2PMChCurrUnit.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adsl2PMChCurrUnit.setStatus("current")
_Adsl2PMChCurrValidIntervals_Type = Unsigned32
_Adsl2PMChCurrValidIntervals_Object = MibTableColumn
adsl2PMChCurrValidIntervals = _Adsl2PMChCurrValidIntervals_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 2, 1, 1, 2),
    _Adsl2PMChCurrValidIntervals_Type()
)
adsl2PMChCurrValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2PMChCurrValidIntervals.setStatus("current")
_Adsl2PMChCurrInvalidIntervals_Type = Unsigned32
_Adsl2PMChCurrInvalidIntervals_Object = MibTableColumn
adsl2PMChCurrInvalidIntervals = _Adsl2PMChCurrInvalidIntervals_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 2, 1, 1, 3),
    _Adsl2PMChCurrInvalidIntervals_Type()
)
adsl2PMChCurrInvalidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2PMChCurrInvalidIntervals.setStatus("current")
_Adsl2PMChCurr15MTimeElapsed_Type = HCPerfTimeElapsed
_Adsl2PMChCurr15MTimeElapsed_Object = MibTableColumn
adsl2PMChCurr15MTimeElapsed = _Adsl2PMChCurr15MTimeElapsed_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 2, 1, 1, 4),
    _Adsl2PMChCurr15MTimeElapsed_Type()
)
adsl2PMChCurr15MTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2PMChCurr15MTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    adsl2PMChCurr15MTimeElapsed.setUnits("seconds")
_Adsl2PMChCurr15MCodingViolations_Type = Unsigned32
_Adsl2PMChCurr15MCodingViolations_Object = MibTableColumn
adsl2PMChCurr15MCodingViolations = _Adsl2PMChCurr15MCodingViolations_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 2, 1, 1, 5),
    _Adsl2PMChCurr15MCodingViolations_Type()
)
adsl2PMChCurr15MCodingViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2PMChCurr15MCodingViolations.setStatus("current")
_Adsl2PMChCurr15MCorrectedBlocks_Type = Unsigned32
_Adsl2PMChCurr15MCorrectedBlocks_Object = MibTableColumn
adsl2PMChCurr15MCorrectedBlocks = _Adsl2PMChCurr15MCorrectedBlocks_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 2, 1, 1, 6),
    _Adsl2PMChCurr15MCorrectedBlocks_Type()
)
adsl2PMChCurr15MCorrectedBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2PMChCurr15MCorrectedBlocks.setStatus("current")
_Adsl2PMChCurr1DayValidIntervals_Type = Unsigned32
_Adsl2PMChCurr1DayValidIntervals_Object = MibTableColumn
adsl2PMChCurr1DayValidIntervals = _Adsl2PMChCurr1DayValidIntervals_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 2, 1, 1, 7),
    _Adsl2PMChCurr1DayValidIntervals_Type()
)
adsl2PMChCurr1DayValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2PMChCurr1DayValidIntervals.setStatus("current")
_Adsl2PMChCurr1DayInvalidIntervals_Type = Unsigned32
_Adsl2PMChCurr1DayInvalidIntervals_Object = MibTableColumn
adsl2PMChCurr1DayInvalidIntervals = _Adsl2PMChCurr1DayInvalidIntervals_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 2, 1, 1, 8),
    _Adsl2PMChCurr1DayInvalidIntervals_Type()
)
adsl2PMChCurr1DayInvalidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2PMChCurr1DayInvalidIntervals.setStatus("current")
_Adsl2PMChCurr1DayTimeElapsed_Type = HCPerfTimeElapsed
_Adsl2PMChCurr1DayTimeElapsed_Object = MibTableColumn
adsl2PMChCurr1DayTimeElapsed = _Adsl2PMChCurr1DayTimeElapsed_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 2, 1, 1, 9),
    _Adsl2PMChCurr1DayTimeElapsed_Type()
)
adsl2PMChCurr1DayTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2PMChCurr1DayTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    adsl2PMChCurr1DayTimeElapsed.setUnits("seconds")
_Adsl2PMChCurr1DayCodingViolations_Type = Unsigned32
_Adsl2PMChCurr1DayCodingViolations_Object = MibTableColumn
adsl2PMChCurr1DayCodingViolations = _Adsl2PMChCurr1DayCodingViolations_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 2, 1, 1, 10),
    _Adsl2PMChCurr1DayCodingViolations_Type()
)
adsl2PMChCurr1DayCodingViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2PMChCurr1DayCodingViolations.setStatus("current")
_Adsl2PMChCurr1DayCorrectedBlocks_Type = Unsigned32
_Adsl2PMChCurr1DayCorrectedBlocks_Object = MibTableColumn
adsl2PMChCurr1DayCorrectedBlocks = _Adsl2PMChCurr1DayCorrectedBlocks_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 2, 1, 1, 11),
    _Adsl2PMChCurr1DayCorrectedBlocks_Type()
)
adsl2PMChCurr1DayCorrectedBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2PMChCurr1DayCorrectedBlocks.setStatus("current")
_Adsl2PMChHist15MinTable_Object = MibTable
adsl2PMChHist15MinTable = _Adsl2PMChHist15MinTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 2, 2)
)
if mibBuilder.loadTexts:
    adsl2PMChHist15MinTable.setStatus("current")
_Adsl2PMChHist15MinEntry_Object = MibTableRow
adsl2PMChHist15MinEntry = _Adsl2PMChHist15MinEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 2, 2, 1)
)
adsl2PMChHist15MinEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADSL2-LINE-MIB", "adsl2PMChHist15MUnit"),
    (0, "ADSL2-LINE-MIB", "adsl2PMChHist15MInterval"),
)
if mibBuilder.loadTexts:
    adsl2PMChHist15MinEntry.setStatus("current")
_Adsl2PMChHist15MUnit_Type = Adsl2Unit
_Adsl2PMChHist15MUnit_Object = MibTableColumn
adsl2PMChHist15MUnit = _Adsl2PMChHist15MUnit_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 2, 2, 1, 1),
    _Adsl2PMChHist15MUnit_Type()
)
adsl2PMChHist15MUnit.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adsl2PMChHist15MUnit.setStatus("current")


class _Adsl2PMChHist15MInterval_Type(Unsigned32):
    """Custom type adsl2PMChHist15MInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_Adsl2PMChHist15MInterval_Type.__name__ = "Unsigned32"
_Adsl2PMChHist15MInterval_Object = MibTableColumn
adsl2PMChHist15MInterval = _Adsl2PMChHist15MInterval_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 2, 2, 1, 2),
    _Adsl2PMChHist15MInterval_Type()
)
adsl2PMChHist15MInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adsl2PMChHist15MInterval.setStatus("current")
_Adsl2PMChHist15MMonitoredTime_Type = Unsigned32
_Adsl2PMChHist15MMonitoredTime_Object = MibTableColumn
adsl2PMChHist15MMonitoredTime = _Adsl2PMChHist15MMonitoredTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 2, 2, 1, 3),
    _Adsl2PMChHist15MMonitoredTime_Type()
)
adsl2PMChHist15MMonitoredTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2PMChHist15MMonitoredTime.setStatus("current")
if mibBuilder.loadTexts:
    adsl2PMChHist15MMonitoredTime.setUnits("seconds")
_Adsl2PMChHist15MCodingViolations_Type = Unsigned32
_Adsl2PMChHist15MCodingViolations_Object = MibTableColumn
adsl2PMChHist15MCodingViolations = _Adsl2PMChHist15MCodingViolations_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 2, 2, 1, 4),
    _Adsl2PMChHist15MCodingViolations_Type()
)
adsl2PMChHist15MCodingViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2PMChHist15MCodingViolations.setStatus("current")
_Adsl2PMChHist15MCorrectedBlocks_Type = Unsigned32
_Adsl2PMChHist15MCorrectedBlocks_Object = MibTableColumn
adsl2PMChHist15MCorrectedBlocks = _Adsl2PMChHist15MCorrectedBlocks_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 2, 2, 1, 5),
    _Adsl2PMChHist15MCorrectedBlocks_Type()
)
adsl2PMChHist15MCorrectedBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2PMChHist15MCorrectedBlocks.setStatus("current")
_Adsl2PMChHist15MValidInterval_Type = TruthValue
_Adsl2PMChHist15MValidInterval_Object = MibTableColumn
adsl2PMChHist15MValidInterval = _Adsl2PMChHist15MValidInterval_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 2, 2, 1, 6),
    _Adsl2PMChHist15MValidInterval_Type()
)
adsl2PMChHist15MValidInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2PMChHist15MValidInterval.setStatus("current")
_Adsl2PMChHist1DTable_Object = MibTable
adsl2PMChHist1DTable = _Adsl2PMChHist1DTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 2, 3)
)
if mibBuilder.loadTexts:
    adsl2PMChHist1DTable.setStatus("current")
_Adsl2PMChHist1DEntry_Object = MibTableRow
adsl2PMChHist1DEntry = _Adsl2PMChHist1DEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 2, 3, 1)
)
adsl2PMChHist1DEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADSL2-LINE-MIB", "adsl2PMChHist1DUnit"),
    (0, "ADSL2-LINE-MIB", "adsl2PMChHist1DInterval"),
)
if mibBuilder.loadTexts:
    adsl2PMChHist1DEntry.setStatus("current")
_Adsl2PMChHist1DUnit_Type = Adsl2Unit
_Adsl2PMChHist1DUnit_Object = MibTableColumn
adsl2PMChHist1DUnit = _Adsl2PMChHist1DUnit_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 2, 3, 1, 1),
    _Adsl2PMChHist1DUnit_Type()
)
adsl2PMChHist1DUnit.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adsl2PMChHist1DUnit.setStatus("current")


class _Adsl2PMChHist1DInterval_Type(Unsigned32):
    """Custom type adsl2PMChHist1DInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_Adsl2PMChHist1DInterval_Type.__name__ = "Unsigned32"
_Adsl2PMChHist1DInterval_Object = MibTableColumn
adsl2PMChHist1DInterval = _Adsl2PMChHist1DInterval_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 2, 3, 1, 2),
    _Adsl2PMChHist1DInterval_Type()
)
adsl2PMChHist1DInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adsl2PMChHist1DInterval.setStatus("current")
_Adsl2PMChHist1DMonitoredTime_Type = Unsigned32
_Adsl2PMChHist1DMonitoredTime_Object = MibTableColumn
adsl2PMChHist1DMonitoredTime = _Adsl2PMChHist1DMonitoredTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 2, 3, 1, 3),
    _Adsl2PMChHist1DMonitoredTime_Type()
)
adsl2PMChHist1DMonitoredTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2PMChHist1DMonitoredTime.setStatus("current")
if mibBuilder.loadTexts:
    adsl2PMChHist1DMonitoredTime.setUnits("seconds")
_Adsl2PMChHist1DCodingViolations_Type = Unsigned32
_Adsl2PMChHist1DCodingViolations_Object = MibTableColumn
adsl2PMChHist1DCodingViolations = _Adsl2PMChHist1DCodingViolations_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 2, 3, 1, 4),
    _Adsl2PMChHist1DCodingViolations_Type()
)
adsl2PMChHist1DCodingViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2PMChHist1DCodingViolations.setStatus("current")
_Adsl2PMChHist1DCorrectedBlocks_Type = Unsigned32
_Adsl2PMChHist1DCorrectedBlocks_Object = MibTableColumn
adsl2PMChHist1DCorrectedBlocks = _Adsl2PMChHist1DCorrectedBlocks_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 2, 3, 1, 5),
    _Adsl2PMChHist1DCorrectedBlocks_Type()
)
adsl2PMChHist1DCorrectedBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2PMChHist1DCorrectedBlocks.setStatus("current")
_Adsl2PMChHist1DValidInterval_Type = TruthValue
_Adsl2PMChHist1DValidInterval_Object = MibTableColumn
adsl2PMChHist1DValidInterval = _Adsl2PMChHist1DValidInterval_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 4, 2, 3, 1, 6),
    _Adsl2PMChHist1DValidInterval_Type()
)
adsl2PMChHist1DValidInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2PMChHist1DValidInterval.setStatus("current")
_Adsl2Profile_ObjectIdentity = ObjectIdentity
adsl2Profile = _Adsl2Profile_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5)
)
_Adsl2ProfileLine_ObjectIdentity = ObjectIdentity
adsl2ProfileLine = _Adsl2ProfileLine_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 1)
)
_Adsl2LineConfTemplateTable_Object = MibTable
adsl2LineConfTemplateTable = _Adsl2LineConfTemplateTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 1, 1)
)
if mibBuilder.loadTexts:
    adsl2LineConfTemplateTable.setStatus("current")
_Adsl2LineConfTemplateEntry_Object = MibTableRow
adsl2LineConfTemplateEntry = _Adsl2LineConfTemplateEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 1, 1, 1)
)
adsl2LineConfTemplateEntry.setIndexNames(
    (0, "ADSL2-LINE-MIB", "adsl2LConfTempTemplateName"),
)
if mibBuilder.loadTexts:
    adsl2LineConfTemplateEntry.setStatus("current")


class _Adsl2LConfTempTemplateName_Type(SnmpAdminString):
    """Custom type adsl2LConfTempTemplateName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Adsl2LConfTempTemplateName_Type.__name__ = "SnmpAdminString"
_Adsl2LConfTempTemplateName_Object = MibTableColumn
adsl2LConfTempTemplateName = _Adsl2LConfTempTemplateName_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 1, 1, 1, 1),
    _Adsl2LConfTempTemplateName_Type()
)
adsl2LConfTempTemplateName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adsl2LConfTempTemplateName.setStatus("current")


class _Adsl2LConfTempLineProfile_Type(SnmpAdminString):
    """Custom type adsl2LConfTempLineProfile based on SnmpAdminString"""
    defaultValue = OctetString("DEFVAL")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Adsl2LConfTempLineProfile_Type.__name__ = "SnmpAdminString"
_Adsl2LConfTempLineProfile_Object = MibTableColumn
adsl2LConfTempLineProfile = _Adsl2LConfTempLineProfile_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 1, 1, 1, 2),
    _Adsl2LConfTempLineProfile_Type()
)
adsl2LConfTempLineProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2LConfTempLineProfile.setStatus("current")


class _Adsl2LConfTempChan1ConfProfile_Type(SnmpAdminString):
    """Custom type adsl2LConfTempChan1ConfProfile based on SnmpAdminString"""
    defaultValue = OctetString("DEFVAL")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Adsl2LConfTempChan1ConfProfile_Type.__name__ = "SnmpAdminString"
_Adsl2LConfTempChan1ConfProfile_Object = MibTableColumn
adsl2LConfTempChan1ConfProfile = _Adsl2LConfTempChan1ConfProfile_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 1, 1, 1, 3),
    _Adsl2LConfTempChan1ConfProfile_Type()
)
adsl2LConfTempChan1ConfProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2LConfTempChan1ConfProfile.setStatus("current")


class _Adsl2LConfTempChan1RaRatioDs_Type(Unsigned32):
    """Custom type adsl2LConfTempChan1RaRatioDs based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Adsl2LConfTempChan1RaRatioDs_Type.__name__ = "Unsigned32"
_Adsl2LConfTempChan1RaRatioDs_Object = MibTableColumn
adsl2LConfTempChan1RaRatioDs = _Adsl2LConfTempChan1RaRatioDs_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 1, 1, 1, 4),
    _Adsl2LConfTempChan1RaRatioDs_Type()
)
adsl2LConfTempChan1RaRatioDs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2LConfTempChan1RaRatioDs.setStatus("current")
if mibBuilder.loadTexts:
    adsl2LConfTempChan1RaRatioDs.setUnits("percent")


class _Adsl2LConfTempChan1RaRatioUs_Type(Unsigned32):
    """Custom type adsl2LConfTempChan1RaRatioUs based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Adsl2LConfTempChan1RaRatioUs_Type.__name__ = "Unsigned32"
_Adsl2LConfTempChan1RaRatioUs_Object = MibTableColumn
adsl2LConfTempChan1RaRatioUs = _Adsl2LConfTempChan1RaRatioUs_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 1, 1, 1, 5),
    _Adsl2LConfTempChan1RaRatioUs_Type()
)
adsl2LConfTempChan1RaRatioUs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2LConfTempChan1RaRatioUs.setStatus("current")
if mibBuilder.loadTexts:
    adsl2LConfTempChan1RaRatioUs.setUnits("percent")


class _Adsl2LConfTempChan2ConfProfile_Type(SnmpAdminString):
    """Custom type adsl2LConfTempChan2ConfProfile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Adsl2LConfTempChan2ConfProfile_Type.__name__ = "SnmpAdminString"
_Adsl2LConfTempChan2ConfProfile_Object = MibTableColumn
adsl2LConfTempChan2ConfProfile = _Adsl2LConfTempChan2ConfProfile_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 1, 1, 1, 6),
    _Adsl2LConfTempChan2ConfProfile_Type()
)
adsl2LConfTempChan2ConfProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2LConfTempChan2ConfProfile.setStatus("current")


class _Adsl2LConfTempChan2RaRatioDs_Type(Unsigned32):
    """Custom type adsl2LConfTempChan2RaRatioDs based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Adsl2LConfTempChan2RaRatioDs_Type.__name__ = "Unsigned32"
_Adsl2LConfTempChan2RaRatioDs_Object = MibTableColumn
adsl2LConfTempChan2RaRatioDs = _Adsl2LConfTempChan2RaRatioDs_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 1, 1, 1, 7),
    _Adsl2LConfTempChan2RaRatioDs_Type()
)
adsl2LConfTempChan2RaRatioDs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2LConfTempChan2RaRatioDs.setStatus("current")
if mibBuilder.loadTexts:
    adsl2LConfTempChan2RaRatioDs.setUnits("percent")


class _Adsl2LConfTempChan2RaRatioUs_Type(Unsigned32):
    """Custom type adsl2LConfTempChan2RaRatioUs based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Adsl2LConfTempChan2RaRatioUs_Type.__name__ = "Unsigned32"
_Adsl2LConfTempChan2RaRatioUs_Object = MibTableColumn
adsl2LConfTempChan2RaRatioUs = _Adsl2LConfTempChan2RaRatioUs_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 1, 1, 1, 8),
    _Adsl2LConfTempChan2RaRatioUs_Type()
)
adsl2LConfTempChan2RaRatioUs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2LConfTempChan2RaRatioUs.setStatus("current")
if mibBuilder.loadTexts:
    adsl2LConfTempChan2RaRatioUs.setUnits("percent")


class _Adsl2LConfTempChan3ConfProfile_Type(SnmpAdminString):
    """Custom type adsl2LConfTempChan3ConfProfile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Adsl2LConfTempChan3ConfProfile_Type.__name__ = "SnmpAdminString"
_Adsl2LConfTempChan3ConfProfile_Object = MibTableColumn
adsl2LConfTempChan3ConfProfile = _Adsl2LConfTempChan3ConfProfile_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 1, 1, 1, 9),
    _Adsl2LConfTempChan3ConfProfile_Type()
)
adsl2LConfTempChan3ConfProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2LConfTempChan3ConfProfile.setStatus("current")


class _Adsl2LConfTempChan3RaRatioDs_Type(Unsigned32):
    """Custom type adsl2LConfTempChan3RaRatioDs based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Adsl2LConfTempChan3RaRatioDs_Type.__name__ = "Unsigned32"
_Adsl2LConfTempChan3RaRatioDs_Object = MibTableColumn
adsl2LConfTempChan3RaRatioDs = _Adsl2LConfTempChan3RaRatioDs_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 1, 1, 1, 10),
    _Adsl2LConfTempChan3RaRatioDs_Type()
)
adsl2LConfTempChan3RaRatioDs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2LConfTempChan3RaRatioDs.setStatus("current")
if mibBuilder.loadTexts:
    adsl2LConfTempChan3RaRatioDs.setUnits("percent")


class _Adsl2LConfTempChan3RaRatioUs_Type(Unsigned32):
    """Custom type adsl2LConfTempChan3RaRatioUs based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Adsl2LConfTempChan3RaRatioUs_Type.__name__ = "Unsigned32"
_Adsl2LConfTempChan3RaRatioUs_Object = MibTableColumn
adsl2LConfTempChan3RaRatioUs = _Adsl2LConfTempChan3RaRatioUs_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 1, 1, 1, 11),
    _Adsl2LConfTempChan3RaRatioUs_Type()
)
adsl2LConfTempChan3RaRatioUs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2LConfTempChan3RaRatioUs.setStatus("current")
if mibBuilder.loadTexts:
    adsl2LConfTempChan3RaRatioUs.setUnits("percent")


class _Adsl2LConfTempChan4ConfProfile_Type(SnmpAdminString):
    """Custom type adsl2LConfTempChan4ConfProfile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Adsl2LConfTempChan4ConfProfile_Type.__name__ = "SnmpAdminString"
_Adsl2LConfTempChan4ConfProfile_Object = MibTableColumn
adsl2LConfTempChan4ConfProfile = _Adsl2LConfTempChan4ConfProfile_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 1, 1, 1, 12),
    _Adsl2LConfTempChan4ConfProfile_Type()
)
adsl2LConfTempChan4ConfProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2LConfTempChan4ConfProfile.setStatus("current")


class _Adsl2LConfTempChan4RaRatioDs_Type(Unsigned32):
    """Custom type adsl2LConfTempChan4RaRatioDs based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Adsl2LConfTempChan4RaRatioDs_Type.__name__ = "Unsigned32"
_Adsl2LConfTempChan4RaRatioDs_Object = MibTableColumn
adsl2LConfTempChan4RaRatioDs = _Adsl2LConfTempChan4RaRatioDs_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 1, 1, 1, 13),
    _Adsl2LConfTempChan4RaRatioDs_Type()
)
adsl2LConfTempChan4RaRatioDs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2LConfTempChan4RaRatioDs.setStatus("current")
if mibBuilder.loadTexts:
    adsl2LConfTempChan4RaRatioDs.setUnits("percent")


class _Adsl2LConfTempChan4RaRatioUs_Type(Unsigned32):
    """Custom type adsl2LConfTempChan4RaRatioUs based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Adsl2LConfTempChan4RaRatioUs_Type.__name__ = "Unsigned32"
_Adsl2LConfTempChan4RaRatioUs_Object = MibTableColumn
adsl2LConfTempChan4RaRatioUs = _Adsl2LConfTempChan4RaRatioUs_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 1, 1, 1, 14),
    _Adsl2LConfTempChan4RaRatioUs_Type()
)
adsl2LConfTempChan4RaRatioUs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2LConfTempChan4RaRatioUs.setStatus("current")
if mibBuilder.loadTexts:
    adsl2LConfTempChan4RaRatioUs.setUnits("percent")
_Adsl2LConfTempRowStatus_Type = RowStatus
_Adsl2LConfTempRowStatus_Object = MibTableColumn
adsl2LConfTempRowStatus = _Adsl2LConfTempRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 1, 1, 1, 15),
    _Adsl2LConfTempRowStatus_Type()
)
adsl2LConfTempRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2LConfTempRowStatus.setStatus("current")
_Adsl2LineConfProfTable_Object = MibTable
adsl2LineConfProfTable = _Adsl2LineConfProfTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 1, 2)
)
if mibBuilder.loadTexts:
    adsl2LineConfProfTable.setStatus("current")
_Adsl2LineConfProfEntry_Object = MibTableRow
adsl2LineConfProfEntry = _Adsl2LineConfProfEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 1, 2, 1)
)
adsl2LineConfProfEntry.setIndexNames(
    (0, "ADSL2-LINE-MIB", "adsl2LConfProfProfileName"),
)
if mibBuilder.loadTexts:
    adsl2LineConfProfEntry.setStatus("current")


class _Adsl2LConfProfProfileName_Type(SnmpAdminString):
    """Custom type adsl2LConfProfProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Adsl2LConfProfProfileName_Type.__name__ = "SnmpAdminString"
_Adsl2LConfProfProfileName_Object = MibTableColumn
adsl2LConfProfProfileName = _Adsl2LConfProfProfileName_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 1, 2, 1, 1),
    _Adsl2LConfProfProfileName_Type()
)
adsl2LConfProfProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adsl2LConfProfProfileName.setStatus("current")
_Adsl2LConfProfScMaskDs_Type = Adsl2ScMaskDs
_Adsl2LConfProfScMaskDs_Object = MibTableColumn
adsl2LConfProfScMaskDs = _Adsl2LConfProfScMaskDs_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 1, 2, 1, 2),
    _Adsl2LConfProfScMaskDs_Type()
)
adsl2LConfProfScMaskDs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2LConfProfScMaskDs.setStatus("current")
_Adsl2LConfProfScMaskUs_Type = Adsl2ScMaskUs
_Adsl2LConfProfScMaskUs_Object = MibTableColumn
adsl2LConfProfScMaskUs = _Adsl2LConfProfScMaskUs_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 1, 2, 1, 3),
    _Adsl2LConfProfScMaskUs_Type()
)
adsl2LConfProfScMaskUs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2LConfProfScMaskUs.setStatus("current")
_Adsl2LConfProfRfiBandsDs_Type = Adsl2RfiDs
_Adsl2LConfProfRfiBandsDs_Object = MibTableColumn
adsl2LConfProfRfiBandsDs = _Adsl2LConfProfRfiBandsDs_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 1, 2, 1, 4),
    _Adsl2LConfProfRfiBandsDs_Type()
)
adsl2LConfProfRfiBandsDs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2LConfProfRfiBandsDs.setStatus("current")


class _Adsl2LConfProfRaModeDs_Type(Adsl2RaMode):
    """Custom type adsl2LConfProfRaModeDs based on Adsl2RaMode"""


_Adsl2LConfProfRaModeDs_Object = MibTableColumn
adsl2LConfProfRaModeDs = _Adsl2LConfProfRaModeDs_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 1, 2, 1, 5),
    _Adsl2LConfProfRaModeDs_Type()
)
adsl2LConfProfRaModeDs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2LConfProfRaModeDs.setStatus("current")


class _Adsl2LConfProfRaModeUs_Type(Adsl2RaMode):
    """Custom type adsl2LConfProfRaModeUs based on Adsl2RaMode"""


_Adsl2LConfProfRaModeUs_Object = MibTableColumn
adsl2LConfProfRaModeUs = _Adsl2LConfProfRaModeUs_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 1, 2, 1, 6),
    _Adsl2LConfProfRaModeUs_Type()
)
adsl2LConfProfRaModeUs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2LConfProfRaModeUs.setStatus("current")


class _Adsl2LConfProfRaUsNrmDs_Type(Unsigned32):
    """Custom type adsl2LConfProfRaUsNrmDs based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_Adsl2LConfProfRaUsNrmDs_Type.__name__ = "Unsigned32"
_Adsl2LConfProfRaUsNrmDs_Object = MibTableColumn
adsl2LConfProfRaUsNrmDs = _Adsl2LConfProfRaUsNrmDs_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 1, 2, 1, 7),
    _Adsl2LConfProfRaUsNrmDs_Type()
)
adsl2LConfProfRaUsNrmDs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2LConfProfRaUsNrmDs.setStatus("current")
if mibBuilder.loadTexts:
    adsl2LConfProfRaUsNrmDs.setUnits("0.1 dB")


class _Adsl2LConfProfRaUsNrmUs_Type(Unsigned32):
    """Custom type adsl2LConfProfRaUsNrmUs based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_Adsl2LConfProfRaUsNrmUs_Type.__name__ = "Unsigned32"
_Adsl2LConfProfRaUsNrmUs_Object = MibTableColumn
adsl2LConfProfRaUsNrmUs = _Adsl2LConfProfRaUsNrmUs_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 1, 2, 1, 8),
    _Adsl2LConfProfRaUsNrmUs_Type()
)
adsl2LConfProfRaUsNrmUs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2LConfProfRaUsNrmUs.setStatus("current")
if mibBuilder.loadTexts:
    adsl2LConfProfRaUsNrmUs.setUnits("0.1 dB")


class _Adsl2LConfProfRaUsTimeDs_Type(Unsigned32):
    """Custom type adsl2LConfProfRaUsTimeDs based on Unsigned32"""
    defaultValue = 3600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_Adsl2LConfProfRaUsTimeDs_Type.__name__ = "Unsigned32"
_Adsl2LConfProfRaUsTimeDs_Object = MibTableColumn
adsl2LConfProfRaUsTimeDs = _Adsl2LConfProfRaUsTimeDs_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 1, 2, 1, 9),
    _Adsl2LConfProfRaUsTimeDs_Type()
)
adsl2LConfProfRaUsTimeDs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2LConfProfRaUsTimeDs.setStatus("current")
if mibBuilder.loadTexts:
    adsl2LConfProfRaUsTimeDs.setUnits("seconds")


class _Adsl2LConfProfRaUsTimeUs_Type(Unsigned32):
    """Custom type adsl2LConfProfRaUsTimeUs based on Unsigned32"""
    defaultValue = 3600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_Adsl2LConfProfRaUsTimeUs_Type.__name__ = "Unsigned32"
_Adsl2LConfProfRaUsTimeUs_Object = MibTableColumn
adsl2LConfProfRaUsTimeUs = _Adsl2LConfProfRaUsTimeUs_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 1, 2, 1, 10),
    _Adsl2LConfProfRaUsTimeUs_Type()
)
adsl2LConfProfRaUsTimeUs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2LConfProfRaUsTimeUs.setStatus("current")
if mibBuilder.loadTexts:
    adsl2LConfProfRaUsTimeUs.setUnits("seconds")


class _Adsl2LConfProfRaDsNrmsDs_Type(Unsigned32):
    """Custom type adsl2LConfProfRaDsNrmsDs based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_Adsl2LConfProfRaDsNrmsDs_Type.__name__ = "Unsigned32"
_Adsl2LConfProfRaDsNrmsDs_Object = MibTableColumn
adsl2LConfProfRaDsNrmsDs = _Adsl2LConfProfRaDsNrmsDs_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 1, 2, 1, 11),
    _Adsl2LConfProfRaDsNrmsDs_Type()
)
adsl2LConfProfRaDsNrmsDs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2LConfProfRaDsNrmsDs.setStatus("current")
if mibBuilder.loadTexts:
    adsl2LConfProfRaDsNrmsDs.setUnits("0.1 dB")


class _Adsl2LConfProfRaDsNrmsUs_Type(Unsigned32):
    """Custom type adsl2LConfProfRaDsNrmsUs based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_Adsl2LConfProfRaDsNrmsUs_Type.__name__ = "Unsigned32"
_Adsl2LConfProfRaDsNrmsUs_Object = MibTableColumn
adsl2LConfProfRaDsNrmsUs = _Adsl2LConfProfRaDsNrmsUs_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 1, 2, 1, 12),
    _Adsl2LConfProfRaDsNrmsUs_Type()
)
adsl2LConfProfRaDsNrmsUs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2LConfProfRaDsNrmsUs.setStatus("current")
if mibBuilder.loadTexts:
    adsl2LConfProfRaDsNrmsUs.setUnits("0.1 dB")


class _Adsl2LConfProfRaDsTimeDs_Type(Unsigned32):
    """Custom type adsl2LConfProfRaDsTimeDs based on Unsigned32"""
    defaultValue = 3600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_Adsl2LConfProfRaDsTimeDs_Type.__name__ = "Unsigned32"
_Adsl2LConfProfRaDsTimeDs_Object = MibTableColumn
adsl2LConfProfRaDsTimeDs = _Adsl2LConfProfRaDsTimeDs_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 1, 2, 1, 13),
    _Adsl2LConfProfRaDsTimeDs_Type()
)
adsl2LConfProfRaDsTimeDs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2LConfProfRaDsTimeDs.setStatus("current")
if mibBuilder.loadTexts:
    adsl2LConfProfRaDsTimeDs.setUnits("seconds")


class _Adsl2LConfProfRaDsTimeUs_Type(Unsigned32):
    """Custom type adsl2LConfProfRaDsTimeUs based on Unsigned32"""
    defaultValue = 3600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_Adsl2LConfProfRaDsTimeUs_Type.__name__ = "Unsigned32"
_Adsl2LConfProfRaDsTimeUs_Object = MibTableColumn
adsl2LConfProfRaDsTimeUs = _Adsl2LConfProfRaDsTimeUs_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 1, 2, 1, 14),
    _Adsl2LConfProfRaDsTimeUs_Type()
)
adsl2LConfProfRaDsTimeUs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2LConfProfRaDsTimeUs.setStatus("current")
if mibBuilder.loadTexts:
    adsl2LConfProfRaDsTimeUs.setUnits("seconds")


class _Adsl2LConfProfTargetSnrmDs_Type(Unsigned32):
    """Custom type adsl2LConfProfTargetSnrmDs based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_Adsl2LConfProfTargetSnrmDs_Type.__name__ = "Unsigned32"
_Adsl2LConfProfTargetSnrmDs_Object = MibTableColumn
adsl2LConfProfTargetSnrmDs = _Adsl2LConfProfTargetSnrmDs_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 1, 2, 1, 15),
    _Adsl2LConfProfTargetSnrmDs_Type()
)
adsl2LConfProfTargetSnrmDs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2LConfProfTargetSnrmDs.setStatus("current")
if mibBuilder.loadTexts:
    adsl2LConfProfTargetSnrmDs.setUnits("0.1 dB")


class _Adsl2LConfProfTargetSnrmUs_Type(Unsigned32):
    """Custom type adsl2LConfProfTargetSnrmUs based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_Adsl2LConfProfTargetSnrmUs_Type.__name__ = "Unsigned32"
_Adsl2LConfProfTargetSnrmUs_Object = MibTableColumn
adsl2LConfProfTargetSnrmUs = _Adsl2LConfProfTargetSnrmUs_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 1, 2, 1, 16),
    _Adsl2LConfProfTargetSnrmUs_Type()
)
adsl2LConfProfTargetSnrmUs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2LConfProfTargetSnrmUs.setStatus("current")
if mibBuilder.loadTexts:
    adsl2LConfProfTargetSnrmUs.setUnits("0.1 dB")


class _Adsl2LConfProfMaxSnrmDs_Type(Unsigned32):
    """Custom type adsl2LConfProfMaxSnrmDs based on Unsigned32"""
    defaultValue = 310

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_Adsl2LConfProfMaxSnrmDs_Type.__name__ = "Unsigned32"
_Adsl2LConfProfMaxSnrmDs_Object = MibTableColumn
adsl2LConfProfMaxSnrmDs = _Adsl2LConfProfMaxSnrmDs_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 1, 2, 1, 17),
    _Adsl2LConfProfMaxSnrmDs_Type()
)
adsl2LConfProfMaxSnrmDs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2LConfProfMaxSnrmDs.setStatus("current")
if mibBuilder.loadTexts:
    adsl2LConfProfMaxSnrmDs.setUnits("0.1 dB")


class _Adsl2LConfProfMaxSnrmUs_Type(Unsigned32):
    """Custom type adsl2LConfProfMaxSnrmUs based on Unsigned32"""
    defaultValue = 310

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_Adsl2LConfProfMaxSnrmUs_Type.__name__ = "Unsigned32"
_Adsl2LConfProfMaxSnrmUs_Object = MibTableColumn
adsl2LConfProfMaxSnrmUs = _Adsl2LConfProfMaxSnrmUs_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 1, 2, 1, 18),
    _Adsl2LConfProfMaxSnrmUs_Type()
)
adsl2LConfProfMaxSnrmUs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2LConfProfMaxSnrmUs.setStatus("current")
if mibBuilder.loadTexts:
    adsl2LConfProfMaxSnrmUs.setUnits("0.1 dB")


class _Adsl2LConfProfMinSnrmDs_Type(Unsigned32):
    """Custom type adsl2LConfProfMinSnrmDs based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_Adsl2LConfProfMinSnrmDs_Type.__name__ = "Unsigned32"
_Adsl2LConfProfMinSnrmDs_Object = MibTableColumn
adsl2LConfProfMinSnrmDs = _Adsl2LConfProfMinSnrmDs_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 1, 2, 1, 19),
    _Adsl2LConfProfMinSnrmDs_Type()
)
adsl2LConfProfMinSnrmDs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2LConfProfMinSnrmDs.setStatus("current")
if mibBuilder.loadTexts:
    adsl2LConfProfMinSnrmDs.setUnits("0.1 dB")


class _Adsl2LConfProfMinSnrmUs_Type(Unsigned32):
    """Custom type adsl2LConfProfMinSnrmUs based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 310),
    )


_Adsl2LConfProfMinSnrmUs_Type.__name__ = "Unsigned32"
_Adsl2LConfProfMinSnrmUs_Object = MibTableColumn
adsl2LConfProfMinSnrmUs = _Adsl2LConfProfMinSnrmUs_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 1, 2, 1, 20),
    _Adsl2LConfProfMinSnrmUs_Type()
)
adsl2LConfProfMinSnrmUs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2LConfProfMinSnrmUs.setStatus("current")
if mibBuilder.loadTexts:
    adsl2LConfProfMinSnrmUs.setUnits("0.1 dB")


class _Adsl2LConfProfMsgMinUs_Type(Unsigned32):
    """Custom type adsl2LConfProfMsgMinUs based on Unsigned32"""
    defaultValue = 4000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4000, 63000),
    )


_Adsl2LConfProfMsgMinUs_Type.__name__ = "Unsigned32"
_Adsl2LConfProfMsgMinUs_Object = MibTableColumn
adsl2LConfProfMsgMinUs = _Adsl2LConfProfMsgMinUs_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 1, 2, 1, 21),
    _Adsl2LConfProfMsgMinUs_Type()
)
adsl2LConfProfMsgMinUs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2LConfProfMsgMinUs.setStatus("current")
if mibBuilder.loadTexts:
    adsl2LConfProfMsgMinUs.setUnits("bits/second")


class _Adsl2LConfProfMsgMinDs_Type(Unsigned32):
    """Custom type adsl2LConfProfMsgMinDs based on Unsigned32"""
    defaultValue = 4000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4000, 63000),
    )


_Adsl2LConfProfMsgMinDs_Type.__name__ = "Unsigned32"
_Adsl2LConfProfMsgMinDs_Object = MibTableColumn
adsl2LConfProfMsgMinDs = _Adsl2LConfProfMsgMinDs_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 1, 2, 1, 22),
    _Adsl2LConfProfMsgMinDs_Type()
)
adsl2LConfProfMsgMinDs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2LConfProfMsgMinDs.setStatus("current")
if mibBuilder.loadTexts:
    adsl2LConfProfMsgMinDs.setUnits("bits/second")
_Adsl2LConfProfAtuTransSysEna_Type = Adsl2TransmissionModeType
_Adsl2LConfProfAtuTransSysEna_Object = MibTableColumn
adsl2LConfProfAtuTransSysEna = _Adsl2LConfProfAtuTransSysEna_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 1, 2, 1, 23),
    _Adsl2LConfProfAtuTransSysEna_Type()
)
adsl2LConfProfAtuTransSysEna.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2LConfProfAtuTransSysEna.setStatus("current")


class _Adsl2LConfProfPmMode_Type(Adsl2LConfProfPmMode):
    """Custom type adsl2LConfProfPmMode based on Adsl2LConfProfPmMode"""
    defaultBinValue = "0"


_Adsl2LConfProfPmMode_Object = MibTableColumn
adsl2LConfProfPmMode = _Adsl2LConfProfPmMode_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 1, 2, 1, 24),
    _Adsl2LConfProfPmMode_Type()
)
adsl2LConfProfPmMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2LConfProfPmMode.setStatus("current")


class _Adsl2LConfProfL0Time_Type(Unsigned32):
    """Custom type adsl2LConfProfL0Time based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Adsl2LConfProfL0Time_Type.__name__ = "Unsigned32"
_Adsl2LConfProfL0Time_Object = MibTableColumn
adsl2LConfProfL0Time = _Adsl2LConfProfL0Time_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 1, 2, 1, 25),
    _Adsl2LConfProfL0Time_Type()
)
adsl2LConfProfL0Time.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2LConfProfL0Time.setStatus("current")
if mibBuilder.loadTexts:
    adsl2LConfProfL0Time.setUnits("seconds")


class _Adsl2LConfProfL2Time_Type(Unsigned32):
    """Custom type adsl2LConfProfL2Time based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Adsl2LConfProfL2Time_Type.__name__ = "Unsigned32"
_Adsl2LConfProfL2Time_Object = MibTableColumn
adsl2LConfProfL2Time = _Adsl2LConfProfL2Time_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 1, 2, 1, 26),
    _Adsl2LConfProfL2Time_Type()
)
adsl2LConfProfL2Time.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2LConfProfL2Time.setStatus("current")
if mibBuilder.loadTexts:
    adsl2LConfProfL2Time.setUnits("seconds")


class _Adsl2LConfProfL2Atpr_Type(Unsigned32):
    """Custom type adsl2LConfProfL2Atpr based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_Adsl2LConfProfL2Atpr_Type.__name__ = "Unsigned32"
_Adsl2LConfProfL2Atpr_Object = MibTableColumn
adsl2LConfProfL2Atpr = _Adsl2LConfProfL2Atpr_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 1, 2, 1, 27),
    _Adsl2LConfProfL2Atpr_Type()
)
adsl2LConfProfL2Atpr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2LConfProfL2Atpr.setStatus("current")
if mibBuilder.loadTexts:
    adsl2LConfProfL2Atpr.setUnits("dB")


class _Adsl2LConfProfL2Atprt_Type(Unsigned32):
    """Custom type adsl2LConfProfL2Atprt based on Unsigned32"""
    defaultValue = 31

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_Adsl2LConfProfL2Atprt_Type.__name__ = "Unsigned32"
_Adsl2LConfProfL2Atprt_Object = MibTableColumn
adsl2LConfProfL2Atprt = _Adsl2LConfProfL2Atprt_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 1, 2, 1, 28),
    _Adsl2LConfProfL2Atprt_Type()
)
adsl2LConfProfL2Atprt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2LConfProfL2Atprt.setStatus("current")
if mibBuilder.loadTexts:
    adsl2LConfProfL2Atprt.setUnits("dB")
_Adsl2LConfProfRowStatus_Type = RowStatus
_Adsl2LConfProfRowStatus_Object = MibTableColumn
adsl2LConfProfRowStatus = _Adsl2LConfProfRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 1, 2, 1, 29),
    _Adsl2LConfProfRowStatus_Type()
)
adsl2LConfProfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2LConfProfRowStatus.setStatus("current")
_Adsl2LineConfProfModeSpecTable_Object = MibTable
adsl2LineConfProfModeSpecTable = _Adsl2LineConfProfModeSpecTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 1, 3)
)
if mibBuilder.loadTexts:
    adsl2LineConfProfModeSpecTable.setStatus("current")
_Adsl2LineConfProfModeSpecEntry_Object = MibTableRow
adsl2LineConfProfModeSpecEntry = _Adsl2LineConfProfModeSpecEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 1, 3, 1)
)
adsl2LineConfProfModeSpecEntry.setIndexNames(
    (0, "ADSL2-LINE-MIB", "adsl2LConfProfProfileName"),
    (0, "ADSL2-LINE-MIB", "adsl2LConfProfAdslMode"),
)
if mibBuilder.loadTexts:
    adsl2LineConfProfModeSpecEntry.setStatus("current")
_Adsl2LConfProfAdslMode_Type = Adsl2OperationModes
_Adsl2LConfProfAdslMode_Object = MibTableColumn
adsl2LConfProfAdslMode = _Adsl2LConfProfAdslMode_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 1, 3, 1, 1),
    _Adsl2LConfProfAdslMode_Type()
)
adsl2LConfProfAdslMode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adsl2LConfProfAdslMode.setStatus("current")


class _Adsl2LConfProfMaxNomPsdDs_Type(Integer32):
    """Custom type adsl2LConfProfMaxNomPsdDs based on Integer32"""
    defaultValue = -300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-600, -300),
    )


_Adsl2LConfProfMaxNomPsdDs_Type.__name__ = "Integer32"
_Adsl2LConfProfMaxNomPsdDs_Object = MibTableColumn
adsl2LConfProfMaxNomPsdDs = _Adsl2LConfProfMaxNomPsdDs_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 1, 3, 1, 2),
    _Adsl2LConfProfMaxNomPsdDs_Type()
)
adsl2LConfProfMaxNomPsdDs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2LConfProfMaxNomPsdDs.setStatus("current")
if mibBuilder.loadTexts:
    adsl2LConfProfMaxNomPsdDs.setUnits("0.1 dBm/Hz")


class _Adsl2LConfProfMaxNomPsdUs_Type(Integer32):
    """Custom type adsl2LConfProfMaxNomPsdUs based on Integer32"""
    defaultValue = -300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-600, -300),
    )


_Adsl2LConfProfMaxNomPsdUs_Type.__name__ = "Integer32"
_Adsl2LConfProfMaxNomPsdUs_Object = MibTableColumn
adsl2LConfProfMaxNomPsdUs = _Adsl2LConfProfMaxNomPsdUs_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 1, 3, 1, 3),
    _Adsl2LConfProfMaxNomPsdUs_Type()
)
adsl2LConfProfMaxNomPsdUs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2LConfProfMaxNomPsdUs.setStatus("current")
if mibBuilder.loadTexts:
    adsl2LConfProfMaxNomPsdUs.setUnits("0.1 dBm/Hz")


class _Adsl2LConfProfMaxNomAtpDs_Type(Unsigned32):
    """Custom type adsl2LConfProfMaxNomAtpDs based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Adsl2LConfProfMaxNomAtpDs_Type.__name__ = "Unsigned32"
_Adsl2LConfProfMaxNomAtpDs_Object = MibTableColumn
adsl2LConfProfMaxNomAtpDs = _Adsl2LConfProfMaxNomAtpDs_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 1, 3, 1, 4),
    _Adsl2LConfProfMaxNomAtpDs_Type()
)
adsl2LConfProfMaxNomAtpDs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2LConfProfMaxNomAtpDs.setStatus("current")
if mibBuilder.loadTexts:
    adsl2LConfProfMaxNomAtpDs.setUnits("0.1 dBm")


class _Adsl2LConfProfMaxNomAtpUs_Type(Unsigned32):
    """Custom type adsl2LConfProfMaxNomAtpUs based on Unsigned32"""
    defaultValue = 255

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Adsl2LConfProfMaxNomAtpUs_Type.__name__ = "Unsigned32"
_Adsl2LConfProfMaxNomAtpUs_Object = MibTableColumn
adsl2LConfProfMaxNomAtpUs = _Adsl2LConfProfMaxNomAtpUs_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 1, 3, 1, 5),
    _Adsl2LConfProfMaxNomAtpUs_Type()
)
adsl2LConfProfMaxNomAtpUs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2LConfProfMaxNomAtpUs.setStatus("current")
if mibBuilder.loadTexts:
    adsl2LConfProfMaxNomAtpUs.setUnits("0.1 dBm")


class _Adsl2LConfProfMaxAggRxPwrUs_Type(Integer32):
    """Custom type adsl2LConfProfMaxAggRxPwrUs based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-255, 255),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_Adsl2LConfProfMaxAggRxPwrUs_Type.__name__ = "Integer32"
_Adsl2LConfProfMaxAggRxPwrUs_Object = MibTableColumn
adsl2LConfProfMaxAggRxPwrUs = _Adsl2LConfProfMaxAggRxPwrUs_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 1, 3, 1, 6),
    _Adsl2LConfProfMaxAggRxPwrUs_Type()
)
adsl2LConfProfMaxAggRxPwrUs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2LConfProfMaxAggRxPwrUs.setStatus("current")
if mibBuilder.loadTexts:
    adsl2LConfProfMaxAggRxPwrUs.setUnits("0.1 dBm")
_Adsl2LConfProfPsdMaskDs_Type = Adsl2PsdMaskDs
_Adsl2LConfProfPsdMaskDs_Object = MibTableColumn
adsl2LConfProfPsdMaskDs = _Adsl2LConfProfPsdMaskDs_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 1, 3, 1, 7),
    _Adsl2LConfProfPsdMaskDs_Type()
)
adsl2LConfProfPsdMaskDs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2LConfProfPsdMaskDs.setStatus("current")
_Adsl2LConfProfPsdMaskUs_Type = Adsl2PsdMaskUs
_Adsl2LConfProfPsdMaskUs_Object = MibTableColumn
adsl2LConfProfPsdMaskUs = _Adsl2LConfProfPsdMaskUs_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 1, 3, 1, 8),
    _Adsl2LConfProfPsdMaskUs_Type()
)
adsl2LConfProfPsdMaskUs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2LConfProfPsdMaskUs.setStatus("current")


class _Adsl2LConfProfPsdMaskSelectUs_Type(Unsigned32):
    """Custom type adsl2LConfProfPsdMaskSelectUs based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_Adsl2LConfProfPsdMaskSelectUs_Type.__name__ = "Unsigned32"
_Adsl2LConfProfPsdMaskSelectUs_Object = MibTableColumn
adsl2LConfProfPsdMaskSelectUs = _Adsl2LConfProfPsdMaskSelectUs_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 1, 3, 1, 9),
    _Adsl2LConfProfPsdMaskSelectUs_Type()
)
adsl2LConfProfPsdMaskSelectUs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2LConfProfPsdMaskSelectUs.setStatus("current")
_Adsl2LConfProfModeSpecRowStatus_Type = RowStatus
_Adsl2LConfProfModeSpecRowStatus_Object = MibTableColumn
adsl2LConfProfModeSpecRowStatus = _Adsl2LConfProfModeSpecRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 1, 3, 1, 10),
    _Adsl2LConfProfModeSpecRowStatus_Type()
)
adsl2LConfProfModeSpecRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2LConfProfModeSpecRowStatus.setStatus("current")
_Adsl2ProfileChannel_ObjectIdentity = ObjectIdentity
adsl2ProfileChannel = _Adsl2ProfileChannel_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 2)
)
_Adsl2ChConfProfileTable_Object = MibTable
adsl2ChConfProfileTable = _Adsl2ChConfProfileTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 2, 1)
)
if mibBuilder.loadTexts:
    adsl2ChConfProfileTable.setStatus("current")
_Adsl2ChConfProfileEntry_Object = MibTableRow
adsl2ChConfProfileEntry = _Adsl2ChConfProfileEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 2, 1, 1)
)
adsl2ChConfProfileEntry.setIndexNames(
    (0, "ADSL2-LINE-MIB", "adsl2ChConfProfProfileName"),
)
if mibBuilder.loadTexts:
    adsl2ChConfProfileEntry.setStatus("current")


class _Adsl2ChConfProfProfileName_Type(SnmpAdminString):
    """Custom type adsl2ChConfProfProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Adsl2ChConfProfProfileName_Type.__name__ = "SnmpAdminString"
_Adsl2ChConfProfProfileName_Object = MibTableColumn
adsl2ChConfProfProfileName = _Adsl2ChConfProfProfileName_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 2, 1, 1, 1),
    _Adsl2ChConfProfProfileName_Type()
)
adsl2ChConfProfProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adsl2ChConfProfProfileName.setStatus("current")


class _Adsl2ChConfProfMinDataRateDs_Type(Unsigned32):
    """Custom type adsl2ChConfProfMinDataRateDs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Adsl2ChConfProfMinDataRateDs_Type.__name__ = "Unsigned32"
_Adsl2ChConfProfMinDataRateDs_Object = MibTableColumn
adsl2ChConfProfMinDataRateDs = _Adsl2ChConfProfMinDataRateDs_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 2, 1, 1, 2),
    _Adsl2ChConfProfMinDataRateDs_Type()
)
adsl2ChConfProfMinDataRateDs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2ChConfProfMinDataRateDs.setStatus("current")
if mibBuilder.loadTexts:
    adsl2ChConfProfMinDataRateDs.setUnits("bits/second")


class _Adsl2ChConfProfMinDataRateUs_Type(Unsigned32):
    """Custom type adsl2ChConfProfMinDataRateUs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Adsl2ChConfProfMinDataRateUs_Type.__name__ = "Unsigned32"
_Adsl2ChConfProfMinDataRateUs_Object = MibTableColumn
adsl2ChConfProfMinDataRateUs = _Adsl2ChConfProfMinDataRateUs_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 2, 1, 1, 3),
    _Adsl2ChConfProfMinDataRateUs_Type()
)
adsl2ChConfProfMinDataRateUs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2ChConfProfMinDataRateUs.setStatus("current")
if mibBuilder.loadTexts:
    adsl2ChConfProfMinDataRateUs.setUnits("bits/second")


class _Adsl2ChConfProfMinResDataRateDs_Type(Unsigned32):
    """Custom type adsl2ChConfProfMinResDataRateDs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Adsl2ChConfProfMinResDataRateDs_Type.__name__ = "Unsigned32"
_Adsl2ChConfProfMinResDataRateDs_Object = MibTableColumn
adsl2ChConfProfMinResDataRateDs = _Adsl2ChConfProfMinResDataRateDs_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 2, 1, 1, 4),
    _Adsl2ChConfProfMinResDataRateDs_Type()
)
adsl2ChConfProfMinResDataRateDs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2ChConfProfMinResDataRateDs.setStatus("current")
if mibBuilder.loadTexts:
    adsl2ChConfProfMinResDataRateDs.setUnits("bits/second")


class _Adsl2ChConfProfMinResDataRateUs_Type(Unsigned32):
    """Custom type adsl2ChConfProfMinResDataRateUs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Adsl2ChConfProfMinResDataRateUs_Type.__name__ = "Unsigned32"
_Adsl2ChConfProfMinResDataRateUs_Object = MibTableColumn
adsl2ChConfProfMinResDataRateUs = _Adsl2ChConfProfMinResDataRateUs_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 2, 1, 1, 5),
    _Adsl2ChConfProfMinResDataRateUs_Type()
)
adsl2ChConfProfMinResDataRateUs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2ChConfProfMinResDataRateUs.setStatus("current")
if mibBuilder.loadTexts:
    adsl2ChConfProfMinResDataRateUs.setUnits("bits/second")


class _Adsl2ChConfProfMaxDataRateDs_Type(Unsigned32):
    """Custom type adsl2ChConfProfMaxDataRateDs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Adsl2ChConfProfMaxDataRateDs_Type.__name__ = "Unsigned32"
_Adsl2ChConfProfMaxDataRateDs_Object = MibTableColumn
adsl2ChConfProfMaxDataRateDs = _Adsl2ChConfProfMaxDataRateDs_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 2, 1, 1, 6),
    _Adsl2ChConfProfMaxDataRateDs_Type()
)
adsl2ChConfProfMaxDataRateDs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2ChConfProfMaxDataRateDs.setStatus("current")
if mibBuilder.loadTexts:
    adsl2ChConfProfMaxDataRateDs.setUnits("bits/second")


class _Adsl2ChConfProfMaxDataRateUs_Type(Unsigned32):
    """Custom type adsl2ChConfProfMaxDataRateUs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Adsl2ChConfProfMaxDataRateUs_Type.__name__ = "Unsigned32"
_Adsl2ChConfProfMaxDataRateUs_Object = MibTableColumn
adsl2ChConfProfMaxDataRateUs = _Adsl2ChConfProfMaxDataRateUs_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 2, 1, 1, 7),
    _Adsl2ChConfProfMaxDataRateUs_Type()
)
adsl2ChConfProfMaxDataRateUs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2ChConfProfMaxDataRateUs.setStatus("current")
if mibBuilder.loadTexts:
    adsl2ChConfProfMaxDataRateUs.setUnits("bits/second")


class _Adsl2ChConfProfMinDataRateLowPwrDs_Type(Unsigned32):
    """Custom type adsl2ChConfProfMinDataRateLowPwrDs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Adsl2ChConfProfMinDataRateLowPwrDs_Type.__name__ = "Unsigned32"
_Adsl2ChConfProfMinDataRateLowPwrDs_Object = MibTableColumn
adsl2ChConfProfMinDataRateLowPwrDs = _Adsl2ChConfProfMinDataRateLowPwrDs_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 2, 1, 1, 8),
    _Adsl2ChConfProfMinDataRateLowPwrDs_Type()
)
adsl2ChConfProfMinDataRateLowPwrDs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2ChConfProfMinDataRateLowPwrDs.setStatus("current")
if mibBuilder.loadTexts:
    adsl2ChConfProfMinDataRateLowPwrDs.setUnits("bits/second")


class _Adsl2ChConfProfMaxDelayDs_Type(Unsigned32):
    """Custom type adsl2ChConfProfMaxDelayDs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Adsl2ChConfProfMaxDelayDs_Type.__name__ = "Unsigned32"
_Adsl2ChConfProfMaxDelayDs_Object = MibTableColumn
adsl2ChConfProfMaxDelayDs = _Adsl2ChConfProfMaxDelayDs_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 2, 1, 1, 9),
    _Adsl2ChConfProfMaxDelayDs_Type()
)
adsl2ChConfProfMaxDelayDs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2ChConfProfMaxDelayDs.setStatus("current")
if mibBuilder.loadTexts:
    adsl2ChConfProfMaxDelayDs.setUnits("milliseconds")


class _Adsl2ChConfProfMaxDelayUs_Type(Unsigned32):
    """Custom type adsl2ChConfProfMaxDelayUs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_Adsl2ChConfProfMaxDelayUs_Type.__name__ = "Unsigned32"
_Adsl2ChConfProfMaxDelayUs_Object = MibTableColumn
adsl2ChConfProfMaxDelayUs = _Adsl2ChConfProfMaxDelayUs_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 2, 1, 1, 10),
    _Adsl2ChConfProfMaxDelayUs_Type()
)
adsl2ChConfProfMaxDelayUs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2ChConfProfMaxDelayUs.setStatus("current")
if mibBuilder.loadTexts:
    adsl2ChConfProfMaxDelayUs.setUnits("milliseconds")


class _Adsl2ChConfProfMinProtectionDs_Type(Adsl2SymbolProtection):
    """Custom type adsl2ChConfProfMinProtectionDs based on Adsl2SymbolProtection"""


_Adsl2ChConfProfMinProtectionDs_Object = MibTableColumn
adsl2ChConfProfMinProtectionDs = _Adsl2ChConfProfMinProtectionDs_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 2, 1, 1, 11),
    _Adsl2ChConfProfMinProtectionDs_Type()
)
adsl2ChConfProfMinProtectionDs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2ChConfProfMinProtectionDs.setStatus("current")
if mibBuilder.loadTexts:
    adsl2ChConfProfMinProtectionDs.setUnits("symbols")


class _Adsl2ChConfProfMinProtectionUs_Type(Adsl2SymbolProtection):
    """Custom type adsl2ChConfProfMinProtectionUs based on Adsl2SymbolProtection"""


_Adsl2ChConfProfMinProtectionUs_Object = MibTableColumn
adsl2ChConfProfMinProtectionUs = _Adsl2ChConfProfMinProtectionUs_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 2, 1, 1, 12),
    _Adsl2ChConfProfMinProtectionUs_Type()
)
adsl2ChConfProfMinProtectionUs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2ChConfProfMinProtectionUs.setStatus("current")
if mibBuilder.loadTexts:
    adsl2ChConfProfMinProtectionUs.setUnits("symbols")


class _Adsl2ChConfProfMaxBerDs_Type(Adsl2MaxBer):
    """Custom type adsl2ChConfProfMaxBerDs based on Adsl2MaxBer"""


_Adsl2ChConfProfMaxBerDs_Object = MibTableColumn
adsl2ChConfProfMaxBerDs = _Adsl2ChConfProfMaxBerDs_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 2, 1, 1, 13),
    _Adsl2ChConfProfMaxBerDs_Type()
)
adsl2ChConfProfMaxBerDs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2ChConfProfMaxBerDs.setStatus("current")


class _Adsl2ChConfProfMaxBerUs_Type(Adsl2MaxBer):
    """Custom type adsl2ChConfProfMaxBerUs based on Adsl2MaxBer"""


_Adsl2ChConfProfMaxBerUs_Object = MibTableColumn
adsl2ChConfProfMaxBerUs = _Adsl2ChConfProfMaxBerUs_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 2, 1, 1, 14),
    _Adsl2ChConfProfMaxBerUs_Type()
)
adsl2ChConfProfMaxBerUs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2ChConfProfMaxBerUs.setStatus("current")


class _Adsl2ChConfProfUsDataRateDs_Type(Unsigned32):
    """Custom type adsl2ChConfProfUsDataRateDs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Adsl2ChConfProfUsDataRateDs_Type.__name__ = "Unsigned32"
_Adsl2ChConfProfUsDataRateDs_Object = MibTableColumn
adsl2ChConfProfUsDataRateDs = _Adsl2ChConfProfUsDataRateDs_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 2, 1, 1, 15),
    _Adsl2ChConfProfUsDataRateDs_Type()
)
adsl2ChConfProfUsDataRateDs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2ChConfProfUsDataRateDs.setStatus("current")
if mibBuilder.loadTexts:
    adsl2ChConfProfUsDataRateDs.setUnits("bits/second")


class _Adsl2ChConfProfDsDataRateDs_Type(Unsigned32):
    """Custom type adsl2ChConfProfDsDataRateDs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Adsl2ChConfProfDsDataRateDs_Type.__name__ = "Unsigned32"
_Adsl2ChConfProfDsDataRateDs_Object = MibTableColumn
adsl2ChConfProfDsDataRateDs = _Adsl2ChConfProfDsDataRateDs_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 2, 1, 1, 16),
    _Adsl2ChConfProfDsDataRateDs_Type()
)
adsl2ChConfProfDsDataRateDs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2ChConfProfDsDataRateDs.setStatus("current")
if mibBuilder.loadTexts:
    adsl2ChConfProfDsDataRateDs.setUnits("bits/second")


class _Adsl2ChConfProfUsDataRateUs_Type(Unsigned32):
    """Custom type adsl2ChConfProfUsDataRateUs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Adsl2ChConfProfUsDataRateUs_Type.__name__ = "Unsigned32"
_Adsl2ChConfProfUsDataRateUs_Object = MibTableColumn
adsl2ChConfProfUsDataRateUs = _Adsl2ChConfProfUsDataRateUs_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 2, 1, 1, 17),
    _Adsl2ChConfProfUsDataRateUs_Type()
)
adsl2ChConfProfUsDataRateUs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2ChConfProfUsDataRateUs.setStatus("current")
if mibBuilder.loadTexts:
    adsl2ChConfProfUsDataRateUs.setUnits("bits/second")


class _Adsl2ChConfProfDsDataRateUs_Type(Unsigned32):
    """Custom type adsl2ChConfProfDsDataRateUs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_Adsl2ChConfProfDsDataRateUs_Type.__name__ = "Unsigned32"
_Adsl2ChConfProfDsDataRateUs_Object = MibTableColumn
adsl2ChConfProfDsDataRateUs = _Adsl2ChConfProfDsDataRateUs_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 2, 1, 1, 18),
    _Adsl2ChConfProfDsDataRateUs_Type()
)
adsl2ChConfProfDsDataRateUs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2ChConfProfDsDataRateUs.setStatus("current")
if mibBuilder.loadTexts:
    adsl2ChConfProfDsDataRateUs.setUnits("bits/second")


class _Adsl2ChConfProfImaEnabled_Type(TruthValue):
    """Custom type adsl2ChConfProfImaEnabled based on TruthValue"""


_Adsl2ChConfProfImaEnabled_Object = MibTableColumn
adsl2ChConfProfImaEnabled = _Adsl2ChConfProfImaEnabled_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 2, 1, 1, 19),
    _Adsl2ChConfProfImaEnabled_Type()
)
adsl2ChConfProfImaEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2ChConfProfImaEnabled.setStatus("current")
_Adsl2ChConfProfRowStatus_Type = RowStatus
_Adsl2ChConfProfRowStatus_Object = MibTableColumn
adsl2ChConfProfRowStatus = _Adsl2ChConfProfRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 2, 1, 1, 20),
    _Adsl2ChConfProfRowStatus_Type()
)
adsl2ChConfProfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2ChConfProfRowStatus.setStatus("current")
_Adsl2ProfileAlarmConf_ObjectIdentity = ObjectIdentity
adsl2ProfileAlarmConf = _Adsl2ProfileAlarmConf_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 3)
)
_Adsl2LineAlarmConfTemplateTable_Object = MibTable
adsl2LineAlarmConfTemplateTable = _Adsl2LineAlarmConfTemplateTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 3, 1)
)
if mibBuilder.loadTexts:
    adsl2LineAlarmConfTemplateTable.setStatus("current")
_Adsl2LineAlarmConfTemplateEntry_Object = MibTableRow
adsl2LineAlarmConfTemplateEntry = _Adsl2LineAlarmConfTemplateEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 3, 1, 1)
)
adsl2LineAlarmConfTemplateEntry.setIndexNames(
    (0, "ADSL2-LINE-MIB", "adsl2LAlarmConfTempTemplateName"),
)
if mibBuilder.loadTexts:
    adsl2LineAlarmConfTemplateEntry.setStatus("current")


class _Adsl2LAlarmConfTempTemplateName_Type(SnmpAdminString):
    """Custom type adsl2LAlarmConfTempTemplateName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Adsl2LAlarmConfTempTemplateName_Type.__name__ = "SnmpAdminString"
_Adsl2LAlarmConfTempTemplateName_Object = MibTableColumn
adsl2LAlarmConfTempTemplateName = _Adsl2LAlarmConfTempTemplateName_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 3, 1, 1, 1),
    _Adsl2LAlarmConfTempTemplateName_Type()
)
adsl2LAlarmConfTempTemplateName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adsl2LAlarmConfTempTemplateName.setStatus("current")


class _Adsl2LAlarmConfTempLineProfile_Type(SnmpAdminString):
    """Custom type adsl2LAlarmConfTempLineProfile based on SnmpAdminString"""
    defaultValue = OctetString("DEFVAL")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Adsl2LAlarmConfTempLineProfile_Type.__name__ = "SnmpAdminString"
_Adsl2LAlarmConfTempLineProfile_Object = MibTableColumn
adsl2LAlarmConfTempLineProfile = _Adsl2LAlarmConfTempLineProfile_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 3, 1, 1, 2),
    _Adsl2LAlarmConfTempLineProfile_Type()
)
adsl2LAlarmConfTempLineProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2LAlarmConfTempLineProfile.setStatus("current")


class _Adsl2LAlarmConfTempChan1ConfProfile_Type(SnmpAdminString):
    """Custom type adsl2LAlarmConfTempChan1ConfProfile based on SnmpAdminString"""
    defaultValue = OctetString("DEFVAL")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Adsl2LAlarmConfTempChan1ConfProfile_Type.__name__ = "SnmpAdminString"
_Adsl2LAlarmConfTempChan1ConfProfile_Object = MibTableColumn
adsl2LAlarmConfTempChan1ConfProfile = _Adsl2LAlarmConfTempChan1ConfProfile_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 3, 1, 1, 3),
    _Adsl2LAlarmConfTempChan1ConfProfile_Type()
)
adsl2LAlarmConfTempChan1ConfProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2LAlarmConfTempChan1ConfProfile.setStatus("current")


class _Adsl2LAlarmConfTempChan2ConfProfile_Type(SnmpAdminString):
    """Custom type adsl2LAlarmConfTempChan2ConfProfile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Adsl2LAlarmConfTempChan2ConfProfile_Type.__name__ = "SnmpAdminString"
_Adsl2LAlarmConfTempChan2ConfProfile_Object = MibTableColumn
adsl2LAlarmConfTempChan2ConfProfile = _Adsl2LAlarmConfTempChan2ConfProfile_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 3, 1, 1, 4),
    _Adsl2LAlarmConfTempChan2ConfProfile_Type()
)
adsl2LAlarmConfTempChan2ConfProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2LAlarmConfTempChan2ConfProfile.setStatus("current")


class _Adsl2LAlarmConfTempChan3ConfProfile_Type(SnmpAdminString):
    """Custom type adsl2LAlarmConfTempChan3ConfProfile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Adsl2LAlarmConfTempChan3ConfProfile_Type.__name__ = "SnmpAdminString"
_Adsl2LAlarmConfTempChan3ConfProfile_Object = MibTableColumn
adsl2LAlarmConfTempChan3ConfProfile = _Adsl2LAlarmConfTempChan3ConfProfile_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 3, 1, 1, 5),
    _Adsl2LAlarmConfTempChan3ConfProfile_Type()
)
adsl2LAlarmConfTempChan3ConfProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2LAlarmConfTempChan3ConfProfile.setStatus("current")


class _Adsl2LAlarmConfTempChan4ConfProfile_Type(SnmpAdminString):
    """Custom type adsl2LAlarmConfTempChan4ConfProfile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Adsl2LAlarmConfTempChan4ConfProfile_Type.__name__ = "SnmpAdminString"
_Adsl2LAlarmConfTempChan4ConfProfile_Object = MibTableColumn
adsl2LAlarmConfTempChan4ConfProfile = _Adsl2LAlarmConfTempChan4ConfProfile_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 3, 1, 1, 6),
    _Adsl2LAlarmConfTempChan4ConfProfile_Type()
)
adsl2LAlarmConfTempChan4ConfProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2LAlarmConfTempChan4ConfProfile.setStatus("current")
_Adsl2LAlarmConfTempRowStatus_Type = RowStatus
_Adsl2LAlarmConfTempRowStatus_Object = MibTableColumn
adsl2LAlarmConfTempRowStatus = _Adsl2LAlarmConfTempRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 3, 1, 1, 7),
    _Adsl2LAlarmConfTempRowStatus_Type()
)
adsl2LAlarmConfTempRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2LAlarmConfTempRowStatus.setStatus("current")
_Adsl2LineAlarmConfProfileTable_Object = MibTable
adsl2LineAlarmConfProfileTable = _Adsl2LineAlarmConfProfileTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 3, 2)
)
if mibBuilder.loadTexts:
    adsl2LineAlarmConfProfileTable.setStatus("current")
_Adsl2LineAlarmConfProfileEntry_Object = MibTableRow
adsl2LineAlarmConfProfileEntry = _Adsl2LineAlarmConfProfileEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 3, 2, 1)
)
adsl2LineAlarmConfProfileEntry.setIndexNames(
    (0, "ADSL2-LINE-MIB", "adsl2LineAlarmConfProfileName"),
)
if mibBuilder.loadTexts:
    adsl2LineAlarmConfProfileEntry.setStatus("current")


class _Adsl2LineAlarmConfProfileName_Type(SnmpAdminString):
    """Custom type adsl2LineAlarmConfProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Adsl2LineAlarmConfProfileName_Type.__name__ = "SnmpAdminString"
_Adsl2LineAlarmConfProfileName_Object = MibTableColumn
adsl2LineAlarmConfProfileName = _Adsl2LineAlarmConfProfileName_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 3, 2, 1, 1),
    _Adsl2LineAlarmConfProfileName_Type()
)
adsl2LineAlarmConfProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adsl2LineAlarmConfProfileName.setStatus("current")


class _Adsl2LineAlarmConfProfileAtucThresh15MinFecs_Type(HCPerfIntervalThreshold):
    """Custom type adsl2LineAlarmConfProfileAtucThresh15MinFecs based on HCPerfIntervalThreshold"""
    defaultValue = 0


_Adsl2LineAlarmConfProfileAtucThresh15MinFecs_Object = MibTableColumn
adsl2LineAlarmConfProfileAtucThresh15MinFecs = _Adsl2LineAlarmConfProfileAtucThresh15MinFecs_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 3, 2, 1, 2),
    _Adsl2LineAlarmConfProfileAtucThresh15MinFecs_Type()
)
adsl2LineAlarmConfProfileAtucThresh15MinFecs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2LineAlarmConfProfileAtucThresh15MinFecs.setStatus("current")
if mibBuilder.loadTexts:
    adsl2LineAlarmConfProfileAtucThresh15MinFecs.setUnits("seconds")


class _Adsl2LineAlarmConfProfileAtucThresh15MinEs_Type(HCPerfIntervalThreshold):
    """Custom type adsl2LineAlarmConfProfileAtucThresh15MinEs based on HCPerfIntervalThreshold"""
    defaultValue = 0


_Adsl2LineAlarmConfProfileAtucThresh15MinEs_Object = MibTableColumn
adsl2LineAlarmConfProfileAtucThresh15MinEs = _Adsl2LineAlarmConfProfileAtucThresh15MinEs_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 3, 2, 1, 3),
    _Adsl2LineAlarmConfProfileAtucThresh15MinEs_Type()
)
adsl2LineAlarmConfProfileAtucThresh15MinEs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2LineAlarmConfProfileAtucThresh15MinEs.setStatus("current")
if mibBuilder.loadTexts:
    adsl2LineAlarmConfProfileAtucThresh15MinEs.setUnits("seconds")


class _Adsl2LineAlarmConfProfileAtucThresh15MinSes_Type(HCPerfIntervalThreshold):
    """Custom type adsl2LineAlarmConfProfileAtucThresh15MinSes based on HCPerfIntervalThreshold"""
    defaultValue = 0


_Adsl2LineAlarmConfProfileAtucThresh15MinSes_Object = MibTableColumn
adsl2LineAlarmConfProfileAtucThresh15MinSes = _Adsl2LineAlarmConfProfileAtucThresh15MinSes_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 3, 2, 1, 4),
    _Adsl2LineAlarmConfProfileAtucThresh15MinSes_Type()
)
adsl2LineAlarmConfProfileAtucThresh15MinSes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2LineAlarmConfProfileAtucThresh15MinSes.setStatus("current")
if mibBuilder.loadTexts:
    adsl2LineAlarmConfProfileAtucThresh15MinSes.setUnits("seconds")


class _Adsl2LineAlarmConfProfileAtucThresh15MinLoss_Type(HCPerfIntervalThreshold):
    """Custom type adsl2LineAlarmConfProfileAtucThresh15MinLoss based on HCPerfIntervalThreshold"""
    defaultValue = 0


_Adsl2LineAlarmConfProfileAtucThresh15MinLoss_Object = MibTableColumn
adsl2LineAlarmConfProfileAtucThresh15MinLoss = _Adsl2LineAlarmConfProfileAtucThresh15MinLoss_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 3, 2, 1, 5),
    _Adsl2LineAlarmConfProfileAtucThresh15MinLoss_Type()
)
adsl2LineAlarmConfProfileAtucThresh15MinLoss.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2LineAlarmConfProfileAtucThresh15MinLoss.setStatus("current")
if mibBuilder.loadTexts:
    adsl2LineAlarmConfProfileAtucThresh15MinLoss.setUnits("seconds")


class _Adsl2LineAlarmConfProfileAtucThresh15MinUas_Type(HCPerfIntervalThreshold):
    """Custom type adsl2LineAlarmConfProfileAtucThresh15MinUas based on HCPerfIntervalThreshold"""
    defaultValue = 0


_Adsl2LineAlarmConfProfileAtucThresh15MinUas_Object = MibTableColumn
adsl2LineAlarmConfProfileAtucThresh15MinUas = _Adsl2LineAlarmConfProfileAtucThresh15MinUas_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 3, 2, 1, 6),
    _Adsl2LineAlarmConfProfileAtucThresh15MinUas_Type()
)
adsl2LineAlarmConfProfileAtucThresh15MinUas.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2LineAlarmConfProfileAtucThresh15MinUas.setStatus("current")
if mibBuilder.loadTexts:
    adsl2LineAlarmConfProfileAtucThresh15MinUas.setUnits("seconds")


class _Adsl2LineAlarmConfProfileAturThresh15MinFecs_Type(HCPerfIntervalThreshold):
    """Custom type adsl2LineAlarmConfProfileAturThresh15MinFecs based on HCPerfIntervalThreshold"""
    defaultValue = 0


_Adsl2LineAlarmConfProfileAturThresh15MinFecs_Object = MibTableColumn
adsl2LineAlarmConfProfileAturThresh15MinFecs = _Adsl2LineAlarmConfProfileAturThresh15MinFecs_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 3, 2, 1, 7),
    _Adsl2LineAlarmConfProfileAturThresh15MinFecs_Type()
)
adsl2LineAlarmConfProfileAturThresh15MinFecs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2LineAlarmConfProfileAturThresh15MinFecs.setStatus("current")
if mibBuilder.loadTexts:
    adsl2LineAlarmConfProfileAturThresh15MinFecs.setUnits("seconds")


class _Adsl2LineAlarmConfProfileAturThresh15MinEs_Type(HCPerfIntervalThreshold):
    """Custom type adsl2LineAlarmConfProfileAturThresh15MinEs based on HCPerfIntervalThreshold"""
    defaultValue = 0


_Adsl2LineAlarmConfProfileAturThresh15MinEs_Object = MibTableColumn
adsl2LineAlarmConfProfileAturThresh15MinEs = _Adsl2LineAlarmConfProfileAturThresh15MinEs_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 3, 2, 1, 8),
    _Adsl2LineAlarmConfProfileAturThresh15MinEs_Type()
)
adsl2LineAlarmConfProfileAturThresh15MinEs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2LineAlarmConfProfileAturThresh15MinEs.setStatus("current")
if mibBuilder.loadTexts:
    adsl2LineAlarmConfProfileAturThresh15MinEs.setUnits("seconds")


class _Adsl2LineAlarmConfProfileAturThresh15MinSes_Type(HCPerfIntervalThreshold):
    """Custom type adsl2LineAlarmConfProfileAturThresh15MinSes based on HCPerfIntervalThreshold"""
    defaultValue = 0


_Adsl2LineAlarmConfProfileAturThresh15MinSes_Object = MibTableColumn
adsl2LineAlarmConfProfileAturThresh15MinSes = _Adsl2LineAlarmConfProfileAturThresh15MinSes_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 3, 2, 1, 9),
    _Adsl2LineAlarmConfProfileAturThresh15MinSes_Type()
)
adsl2LineAlarmConfProfileAturThresh15MinSes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2LineAlarmConfProfileAturThresh15MinSes.setStatus("current")
if mibBuilder.loadTexts:
    adsl2LineAlarmConfProfileAturThresh15MinSes.setUnits("seconds")


class _Adsl2LineAlarmConfProfileAturThresh15MinLoss_Type(HCPerfIntervalThreshold):
    """Custom type adsl2LineAlarmConfProfileAturThresh15MinLoss based on HCPerfIntervalThreshold"""
    defaultValue = 0


_Adsl2LineAlarmConfProfileAturThresh15MinLoss_Object = MibTableColumn
adsl2LineAlarmConfProfileAturThresh15MinLoss = _Adsl2LineAlarmConfProfileAturThresh15MinLoss_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 3, 2, 1, 10),
    _Adsl2LineAlarmConfProfileAturThresh15MinLoss_Type()
)
adsl2LineAlarmConfProfileAturThresh15MinLoss.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2LineAlarmConfProfileAturThresh15MinLoss.setStatus("current")
if mibBuilder.loadTexts:
    adsl2LineAlarmConfProfileAturThresh15MinLoss.setUnits("seconds")


class _Adsl2LineAlarmConfProfileAturThresh15MinUas_Type(HCPerfIntervalThreshold):
    """Custom type adsl2LineAlarmConfProfileAturThresh15MinUas based on HCPerfIntervalThreshold"""
    defaultValue = 0


_Adsl2LineAlarmConfProfileAturThresh15MinUas_Object = MibTableColumn
adsl2LineAlarmConfProfileAturThresh15MinUas = _Adsl2LineAlarmConfProfileAturThresh15MinUas_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 3, 2, 1, 11),
    _Adsl2LineAlarmConfProfileAturThresh15MinUas_Type()
)
adsl2LineAlarmConfProfileAturThresh15MinUas.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2LineAlarmConfProfileAturThresh15MinUas.setStatus("current")
if mibBuilder.loadTexts:
    adsl2LineAlarmConfProfileAturThresh15MinUas.setUnits("seconds")


class _Adsl2LineAlarmConfProfileThresh15MinFailedFullInt_Type(Unsigned32):
    """Custom type adsl2LineAlarmConfProfileThresh15MinFailedFullInt based on Unsigned32"""
    defaultValue = 0


_Adsl2LineAlarmConfProfileThresh15MinFailedFullInt_Object = MibTableColumn
adsl2LineAlarmConfProfileThresh15MinFailedFullInt = _Adsl2LineAlarmConfProfileThresh15MinFailedFullInt_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 3, 2, 1, 12),
    _Adsl2LineAlarmConfProfileThresh15MinFailedFullInt_Type()
)
adsl2LineAlarmConfProfileThresh15MinFailedFullInt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2LineAlarmConfProfileThresh15MinFailedFullInt.setStatus("current")


class _Adsl2LineAlarmConfProfileThresh15MinFailedShrtInt_Type(Unsigned32):
    """Custom type adsl2LineAlarmConfProfileThresh15MinFailedShrtInt based on Unsigned32"""
    defaultValue = 0


_Adsl2LineAlarmConfProfileThresh15MinFailedShrtInt_Object = MibTableColumn
adsl2LineAlarmConfProfileThresh15MinFailedShrtInt = _Adsl2LineAlarmConfProfileThresh15MinFailedShrtInt_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 3, 2, 1, 13),
    _Adsl2LineAlarmConfProfileThresh15MinFailedShrtInt_Type()
)
adsl2LineAlarmConfProfileThresh15MinFailedShrtInt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2LineAlarmConfProfileThresh15MinFailedShrtInt.setStatus("current")
_Adsl2LineAlarmConfProfileRowStatus_Type = RowStatus
_Adsl2LineAlarmConfProfileRowStatus_Object = MibTableColumn
adsl2LineAlarmConfProfileRowStatus = _Adsl2LineAlarmConfProfileRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 3, 2, 1, 14),
    _Adsl2LineAlarmConfProfileRowStatus_Type()
)
adsl2LineAlarmConfProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2LineAlarmConfProfileRowStatus.setStatus("current")
_Adsl2ChAlarmConfProfileTable_Object = MibTable
adsl2ChAlarmConfProfileTable = _Adsl2ChAlarmConfProfileTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 3, 3)
)
if mibBuilder.loadTexts:
    adsl2ChAlarmConfProfileTable.setStatus("current")
_Adsl2ChAlarmConfProfileEntry_Object = MibTableRow
adsl2ChAlarmConfProfileEntry = _Adsl2ChAlarmConfProfileEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 3, 3, 1)
)
adsl2ChAlarmConfProfileEntry.setIndexNames(
    (0, "ADSL2-LINE-MIB", "adsl2ChAlarmConfProfileName"),
)
if mibBuilder.loadTexts:
    adsl2ChAlarmConfProfileEntry.setStatus("current")


class _Adsl2ChAlarmConfProfileName_Type(SnmpAdminString):
    """Custom type adsl2ChAlarmConfProfileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Adsl2ChAlarmConfProfileName_Type.__name__ = "SnmpAdminString"
_Adsl2ChAlarmConfProfileName_Object = MibTableColumn
adsl2ChAlarmConfProfileName = _Adsl2ChAlarmConfProfileName_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 3, 3, 1, 1),
    _Adsl2ChAlarmConfProfileName_Type()
)
adsl2ChAlarmConfProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adsl2ChAlarmConfProfileName.setStatus("current")


class _Adsl2ChAlarmConfProfileAtucThresh15MinCodingViolations_Type(Unsigned32):
    """Custom type adsl2ChAlarmConfProfileAtucThresh15MinCodingViolations based on Unsigned32"""
    defaultValue = 0


_Adsl2ChAlarmConfProfileAtucThresh15MinCodingViolations_Object = MibTableColumn
adsl2ChAlarmConfProfileAtucThresh15MinCodingViolations = _Adsl2ChAlarmConfProfileAtucThresh15MinCodingViolations_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 3, 3, 1, 2),
    _Adsl2ChAlarmConfProfileAtucThresh15MinCodingViolations_Type()
)
adsl2ChAlarmConfProfileAtucThresh15MinCodingViolations.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2ChAlarmConfProfileAtucThresh15MinCodingViolations.setStatus("current")


class _Adsl2ChAlarmConfProfileAtucThresh15MinCorrected_Type(Unsigned32):
    """Custom type adsl2ChAlarmConfProfileAtucThresh15MinCorrected based on Unsigned32"""
    defaultValue = 0


_Adsl2ChAlarmConfProfileAtucThresh15MinCorrected_Object = MibTableColumn
adsl2ChAlarmConfProfileAtucThresh15MinCorrected = _Adsl2ChAlarmConfProfileAtucThresh15MinCorrected_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 3, 3, 1, 3),
    _Adsl2ChAlarmConfProfileAtucThresh15MinCorrected_Type()
)
adsl2ChAlarmConfProfileAtucThresh15MinCorrected.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2ChAlarmConfProfileAtucThresh15MinCorrected.setStatus("current")


class _Adsl2ChAlarmConfProfileAturThresh15MinCodingViolations_Type(Unsigned32):
    """Custom type adsl2ChAlarmConfProfileAturThresh15MinCodingViolations based on Unsigned32"""
    defaultValue = 0


_Adsl2ChAlarmConfProfileAturThresh15MinCodingViolations_Object = MibTableColumn
adsl2ChAlarmConfProfileAturThresh15MinCodingViolations = _Adsl2ChAlarmConfProfileAturThresh15MinCodingViolations_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 3, 3, 1, 4),
    _Adsl2ChAlarmConfProfileAturThresh15MinCodingViolations_Type()
)
adsl2ChAlarmConfProfileAturThresh15MinCodingViolations.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2ChAlarmConfProfileAturThresh15MinCodingViolations.setStatus("current")


class _Adsl2ChAlarmConfProfileAturThresh15MinCorrected_Type(Unsigned32):
    """Custom type adsl2ChAlarmConfProfileAturThresh15MinCorrected based on Unsigned32"""
    defaultValue = 0


_Adsl2ChAlarmConfProfileAturThresh15MinCorrected_Object = MibTableColumn
adsl2ChAlarmConfProfileAturThresh15MinCorrected = _Adsl2ChAlarmConfProfileAturThresh15MinCorrected_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 3, 3, 1, 5),
    _Adsl2ChAlarmConfProfileAturThresh15MinCorrected_Type()
)
adsl2ChAlarmConfProfileAturThresh15MinCorrected.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2ChAlarmConfProfileAturThresh15MinCorrected.setStatus("current")
_Adsl2ChAlarmConfProfileRowStatus_Type = RowStatus
_Adsl2ChAlarmConfProfileRowStatus_Object = MibTableColumn
adsl2ChAlarmConfProfileRowStatus = _Adsl2ChAlarmConfProfileRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 5, 3, 3, 1, 6),
    _Adsl2ChAlarmConfProfileRowStatus_Type()
)
adsl2ChAlarmConfProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adsl2ChAlarmConfProfileRowStatus.setStatus("current")
_Adsl2Scalar_ObjectIdentity = ObjectIdentity
adsl2Scalar = _Adsl2Scalar_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 6)
)
_Adsl2ScalarSC_ObjectIdentity = ObjectIdentity
adsl2ScalarSC = _Adsl2ScalarSC_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 6, 1)
)
_Adsl2ScalarSCMaxInterfaces_Type = Unsigned32
_Adsl2ScalarSCMaxInterfaces_Object = MibScalar
adsl2ScalarSCMaxInterfaces = _Adsl2ScalarSCMaxInterfaces_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 6, 1, 1),
    _Adsl2ScalarSCMaxInterfaces_Type()
)
adsl2ScalarSCMaxInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2ScalarSCMaxInterfaces.setStatus("current")
_Adsl2ScalarSCAvailInterfaces_Type = Unsigned32
_Adsl2ScalarSCAvailInterfaces_Object = MibScalar
adsl2ScalarSCAvailInterfaces = _Adsl2ScalarSCAvailInterfaces_Object(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 6, 1, 2),
    _Adsl2ScalarSCAvailInterfaces_Type()
)
adsl2ScalarSCAvailInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adsl2ScalarSCAvailInterfaces.setStatus("current")
_Adsl2Conformance_ObjectIdentity = ObjectIdentity
adsl2Conformance = _Adsl2Conformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 7)
)
_Adsl2Groups_ObjectIdentity = ObjectIdentity
adsl2Groups = _Adsl2Groups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 7, 1)
)
_Adsl2Compliances_ObjectIdentity = ObjectIdentity
adsl2Compliances = _Adsl2Compliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 7, 2)
)

# Managed Objects groups

adsl2LineGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 7, 1, 1)
)
adsl2LineGroup.setObjects(
      *(("ADSL2-LINE-MIB", "adsl2LineCnfgTemplate"),
        ("ADSL2-LINE-MIB", "adsl2LineAlarmCnfgTemplate"),
        ("ADSL2-LINE-MIB", "adsl2LineCmndConfPmsf"),
        ("ADSL2-LINE-MIB", "adsl2LineCmndConfLdsf"),
        ("ADSL2-LINE-MIB", "adsl2LineCmndConfLdsfFailReason"),
        ("ADSL2-LINE-MIB", "adsl2LineCmndAutomodeColdStart"),
        ("ADSL2-LINE-MIB", "adsl2LineStatusAtuTransSys"),
        ("ADSL2-LINE-MIB", "adsl2LineStatusPwrMngState"),
        ("ADSL2-LINE-MIB", "adsl2LineStatusInitResult"),
        ("ADSL2-LINE-MIB", "adsl2LineStatusLastStateDs"),
        ("ADSL2-LINE-MIB", "adsl2LineStatusLastStateUs"),
        ("ADSL2-LINE-MIB", "adsl2LineStatusAtur"),
        ("ADSL2-LINE-MIB", "adsl2LineStatusAtuc"),
        ("ADSL2-LINE-MIB", "adsl2LineStatusLnAttenDs"),
        ("ADSL2-LINE-MIB", "adsl2LineStatusLnAttenUs"),
        ("ADSL2-LINE-MIB", "adsl2LineStatusSigAttenDs"),
        ("ADSL2-LINE-MIB", "adsl2LineStatusSigAttenUs"),
        ("ADSL2-LINE-MIB", "adsl2LineStatusSnrMarginDs"),
        ("ADSL2-LINE-MIB", "adsl2LineStatusSnrMarginUs"),
        ("ADSL2-LINE-MIB", "adsl2LineStatusAttainableRateDs"),
        ("ADSL2-LINE-MIB", "adsl2LineStatusAttainableRateUs"),
        ("ADSL2-LINE-MIB", "adsl2LineStatusActPsdDs"),
        ("ADSL2-LINE-MIB", "adsl2LineStatusActPsdUs"),
        ("ADSL2-LINE-MIB", "adsl2LineStatusActAtpDs"),
        ("ADSL2-LINE-MIB", "adsl2LineStatusActAtpUs"))
)
if mibBuilder.loadTexts:
    adsl2LineGroup.setStatus("current")

adsl2ChannelStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 7, 1, 2)
)
adsl2ChannelStatusGroup.setObjects(
      *(("ADSL2-LINE-MIB", "adsl2ChStatusChannelNum"),
        ("ADSL2-LINE-MIB", "adsl2ChStatusActDataRate"),
        ("ADSL2-LINE-MIB", "adsl2ChStatusPrevDataRate"),
        ("ADSL2-LINE-MIB", "adsl2ChStatusActDelay"))
)
if mibBuilder.loadTexts:
    adsl2ChannelStatusGroup.setStatus("current")

adsl2ChannelStatusAtmGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 7, 1, 3)
)
adsl2ChannelStatusAtmGroup.setObjects(
    ("ADSL2-LINE-MIB", "adsl2ChStatusAtmStatus")
)
if mibBuilder.loadTexts:
    adsl2ChannelStatusAtmGroup.setStatus("current")

adsl2ChannelStatusPtmGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 7, 1, 4)
)
adsl2ChannelStatusPtmGroup.setObjects(
    ("ADSL2-LINE-MIB", "adsl2ChStatusPtmStatus")
)
if mibBuilder.loadTexts:
    adsl2ChannelStatusPtmGroup.setStatus("current")

adsl2SCStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 7, 1, 5)
)
adsl2SCStatusGroup.setObjects(
      *(("ADSL2-LINE-MIB", "adsl2SCStatusMtime"),
        ("ADSL2-LINE-MIB", "adsl2SCStatusSnr"),
        ("ADSL2-LINE-MIB", "adsl2SCStatusBitsAlloc"),
        ("ADSL2-LINE-MIB", "adsl2SCStatusGainAlloc"),
        ("ADSL2-LINE-MIB", "adsl2SCStatusTssi"),
        ("ADSL2-LINE-MIB", "adsl2SCStatusLinScale"),
        ("ADSL2-LINE-MIB", "adsl2SCStatusLinReal"),
        ("ADSL2-LINE-MIB", "adsl2SCStatusLinImg"),
        ("ADSL2-LINE-MIB", "adsl2SCStatusLogMt"),
        ("ADSL2-LINE-MIB", "adsl2SCStatusLog"),
        ("ADSL2-LINE-MIB", "adsl2SCStatusQlnMt"),
        ("ADSL2-LINE-MIB", "adsl2SCStatusQln"),
        ("ADSL2-LINE-MIB", "adsl2SCStatusLnAtten"),
        ("ADSL2-LINE-MIB", "adsl2SCStatusSigAtten"),
        ("ADSL2-LINE-MIB", "adsl2SCStatusSnrMargin"),
        ("ADSL2-LINE-MIB", "adsl2SCStatusAttainableRate"),
        ("ADSL2-LINE-MIB", "adsl2SCStatusActAtp"),
        ("ADSL2-LINE-MIB", "adsl2SCStatusRowStatus"))
)
if mibBuilder.loadTexts:
    adsl2SCStatusGroup.setStatus("current")

adsl2LineInventoryGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 7, 1, 6)
)
adsl2LineInventoryGroup.setObjects(
      *(("ADSL2-LINE-MIB", "adsl2LInvG994VendorId"),
        ("ADSL2-LINE-MIB", "adsl2LInvSystemVendorId"),
        ("ADSL2-LINE-MIB", "adsl2LInvVersionNumber"),
        ("ADSL2-LINE-MIB", "adsl2LInvSerialNumber"),
        ("ADSL2-LINE-MIB", "adsl2LInvSelfTestResult"),
        ("ADSL2-LINE-MIB", "adsl2LInvTransmissionCapabilities"))
)
if mibBuilder.loadTexts:
    adsl2LineInventoryGroup.setStatus("current")

adsl2LineConfTemplateGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 7, 1, 7)
)
adsl2LineConfTemplateGroup.setObjects(
      *(("ADSL2-LINE-MIB", "adsl2LConfTempLineProfile"),
        ("ADSL2-LINE-MIB", "adsl2LConfTempChan1ConfProfile"),
        ("ADSL2-LINE-MIB", "adsl2LConfTempChan1RaRatioDs"),
        ("ADSL2-LINE-MIB", "adsl2LConfTempChan1RaRatioUs"),
        ("ADSL2-LINE-MIB", "adsl2LConfTempChan2ConfProfile"),
        ("ADSL2-LINE-MIB", "adsl2LConfTempChan2RaRatioDs"),
        ("ADSL2-LINE-MIB", "adsl2LConfTempChan2RaRatioUs"),
        ("ADSL2-LINE-MIB", "adsl2LConfTempChan3ConfProfile"),
        ("ADSL2-LINE-MIB", "adsl2LConfTempChan3RaRatioDs"),
        ("ADSL2-LINE-MIB", "adsl2LConfTempChan3RaRatioUs"),
        ("ADSL2-LINE-MIB", "adsl2LConfTempChan4ConfProfile"),
        ("ADSL2-LINE-MIB", "adsl2LConfTempChan4RaRatioDs"),
        ("ADSL2-LINE-MIB", "adsl2LConfTempChan4RaRatioUs"),
        ("ADSL2-LINE-MIB", "adsl2LConfTempRowStatus"))
)
if mibBuilder.loadTexts:
    adsl2LineConfTemplateGroup.setStatus("current")

adsl2LineConfProfGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 7, 1, 8)
)
adsl2LineConfProfGroup.setObjects(
      *(("ADSL2-LINE-MIB", "adsl2LConfProfScMaskDs"),
        ("ADSL2-LINE-MIB", "adsl2LConfProfScMaskUs"),
        ("ADSL2-LINE-MIB", "adsl2LConfProfRfiBandsDs"),
        ("ADSL2-LINE-MIB", "adsl2LConfProfRaModeDs"),
        ("ADSL2-LINE-MIB", "adsl2LConfProfRaModeUs"),
        ("ADSL2-LINE-MIB", "adsl2LConfProfTargetSnrmDs"),
        ("ADSL2-LINE-MIB", "adsl2LConfProfTargetSnrmUs"),
        ("ADSL2-LINE-MIB", "adsl2LConfProfMaxSnrmDs"),
        ("ADSL2-LINE-MIB", "adsl2LConfProfMaxSnrmUs"),
        ("ADSL2-LINE-MIB", "adsl2LConfProfMinSnrmDs"),
        ("ADSL2-LINE-MIB", "adsl2LConfProfMinSnrmUs"),
        ("ADSL2-LINE-MIB", "adsl2LConfProfAtuTransSysEna"),
        ("ADSL2-LINE-MIB", "adsl2LConfProfPmMode"),
        ("ADSL2-LINE-MIB", "adsl2LConfProfL0Time"),
        ("ADSL2-LINE-MIB", "adsl2LConfProfL2Time"),
        ("ADSL2-LINE-MIB", "adsl2LConfProfL2Atpr"),
        ("ADSL2-LINE-MIB", "adsl2LConfProfL2Atprt"),
        ("ADSL2-LINE-MIB", "adsl2LConfProfRowStatus"))
)
if mibBuilder.loadTexts:
    adsl2LineConfProfGroup.setStatus("current")

adsl2LineConfProfRaGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 7, 1, 9)
)
adsl2LineConfProfRaGroup.setObjects(
      *(("ADSL2-LINE-MIB", "adsl2LConfProfRaUsNrmDs"),
        ("ADSL2-LINE-MIB", "adsl2LConfProfRaUsNrmUs"),
        ("ADSL2-LINE-MIB", "adsl2LConfProfRaUsTimeDs"),
        ("ADSL2-LINE-MIB", "adsl2LConfProfRaUsTimeUs"),
        ("ADSL2-LINE-MIB", "adsl2LConfProfRaDsNrmsDs"),
        ("ADSL2-LINE-MIB", "adsl2LConfProfRaDsNrmsUs"),
        ("ADSL2-LINE-MIB", "adsl2LConfProfRaDsTimeDs"),
        ("ADSL2-LINE-MIB", "adsl2LConfProfRaDsTimeUs"))
)
if mibBuilder.loadTexts:
    adsl2LineConfProfRaGroup.setStatus("current")

adsl2LineConfProfMsgMinGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 7, 1, 10)
)
adsl2LineConfProfMsgMinGroup.setObjects(
      *(("ADSL2-LINE-MIB", "adsl2LConfProfMsgMinUs"),
        ("ADSL2-LINE-MIB", "adsl2LConfProfMsgMinDs"))
)
if mibBuilder.loadTexts:
    adsl2LineConfProfMsgMinGroup.setStatus("current")

adsl2LineConfProfModeSpecGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 7, 1, 11)
)
adsl2LineConfProfModeSpecGroup.setObjects(
      *(("ADSL2-LINE-MIB", "adsl2LConfProfMaxNomPsdDs"),
        ("ADSL2-LINE-MIB", "adsl2LConfProfMaxNomPsdUs"),
        ("ADSL2-LINE-MIB", "adsl2LConfProfMaxNomAtpDs"),
        ("ADSL2-LINE-MIB", "adsl2LConfProfMaxNomAtpUs"),
        ("ADSL2-LINE-MIB", "adsl2LConfProfMaxAggRxPwrUs"),
        ("ADSL2-LINE-MIB", "adsl2LConfProfPsdMaskDs"),
        ("ADSL2-LINE-MIB", "adsl2LConfProfPsdMaskUs"),
        ("ADSL2-LINE-MIB", "adsl2LConfProfPsdMaskSelectUs"),
        ("ADSL2-LINE-MIB", "adsl2LConfProfModeSpecRowStatus"))
)
if mibBuilder.loadTexts:
    adsl2LineConfProfModeSpecGroup.setStatus("current")

adsl2ChConfProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 7, 1, 12)
)
adsl2ChConfProfileGroup.setObjects(
      *(("ADSL2-LINE-MIB", "adsl2ChConfProfMinDataRateDs"),
        ("ADSL2-LINE-MIB", "adsl2ChConfProfMinDataRateUs"),
        ("ADSL2-LINE-MIB", "adsl2ChConfProfMaxDataRateDs"),
        ("ADSL2-LINE-MIB", "adsl2ChConfProfMaxDataRateUs"),
        ("ADSL2-LINE-MIB", "adsl2ChConfProfMinDataRateLowPwrDs"),
        ("ADSL2-LINE-MIB", "adsl2ChConfProfMaxDelayDs"),
        ("ADSL2-LINE-MIB", "adsl2ChConfProfMaxDelayUs"),
        ("ADSL2-LINE-MIB", "adsl2ChConfProfMinProtectionDs"),
        ("ADSL2-LINE-MIB", "adsl2ChConfProfMinProtectionUs"),
        ("ADSL2-LINE-MIB", "adsl2ChConfProfMaxBerDs"),
        ("ADSL2-LINE-MIB", "adsl2ChConfProfMaxBerUs"),
        ("ADSL2-LINE-MIB", "adsl2ChConfProfUsDataRateDs"),
        ("ADSL2-LINE-MIB", "adsl2ChConfProfDsDataRateDs"),
        ("ADSL2-LINE-MIB", "adsl2ChConfProfUsDataRateUs"),
        ("ADSL2-LINE-MIB", "adsl2ChConfProfDsDataRateUs"),
        ("ADSL2-LINE-MIB", "adsl2ChConfProfRowStatus"))
)
if mibBuilder.loadTexts:
    adsl2ChConfProfileGroup.setStatus("current")

adsl2ChConfProfileAtmGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 7, 1, 13)
)
adsl2ChConfProfileAtmGroup.setObjects(
      *(("ADSL2-LINE-MIB", "adsl2ChConfProfImaEnabled"),
        ("ADSL2-LINE-MIB", "adsl2ChStatusAtmStatus"))
)
if mibBuilder.loadTexts:
    adsl2ChConfProfileAtmGroup.setStatus("current")

adsl2ChConfProfileMinResGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 7, 1, 14)
)
adsl2ChConfProfileMinResGroup.setObjects(
      *(("ADSL2-LINE-MIB", "adsl2ChConfProfMinResDataRateDs"),
        ("ADSL2-LINE-MIB", "adsl2ChConfProfMinResDataRateUs"))
)
if mibBuilder.loadTexts:
    adsl2ChConfProfileMinResGroup.setStatus("current")

adsl2LineAlarmConfTemplateGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 7, 1, 15)
)
adsl2LineAlarmConfTemplateGroup.setObjects(
      *(("ADSL2-LINE-MIB", "adsl2LAlarmConfTempLineProfile"),
        ("ADSL2-LINE-MIB", "adsl2LAlarmConfTempChan1ConfProfile"),
        ("ADSL2-LINE-MIB", "adsl2LAlarmConfTempChan2ConfProfile"),
        ("ADSL2-LINE-MIB", "adsl2LAlarmConfTempChan3ConfProfile"),
        ("ADSL2-LINE-MIB", "adsl2LAlarmConfTempChan4ConfProfile"),
        ("ADSL2-LINE-MIB", "adsl2LAlarmConfTempRowStatus"))
)
if mibBuilder.loadTexts:
    adsl2LineAlarmConfTemplateGroup.setStatus("current")

adsl2LineAlarmConfProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 7, 1, 16)
)
adsl2LineAlarmConfProfileGroup.setObjects(
      *(("ADSL2-LINE-MIB", "adsl2LineAlarmConfProfileAtucThresh15MinFecs"),
        ("ADSL2-LINE-MIB", "adsl2LineAlarmConfProfileAtucThresh15MinEs"),
        ("ADSL2-LINE-MIB", "adsl2LineAlarmConfProfileAtucThresh15MinSes"),
        ("ADSL2-LINE-MIB", "adsl2LineAlarmConfProfileAtucThresh15MinLoss"),
        ("ADSL2-LINE-MIB", "adsl2LineAlarmConfProfileAtucThresh15MinUas"),
        ("ADSL2-LINE-MIB", "adsl2LineAlarmConfProfileAturThresh15MinFecs"),
        ("ADSL2-LINE-MIB", "adsl2LineAlarmConfProfileAturThresh15MinEs"),
        ("ADSL2-LINE-MIB", "adsl2LineAlarmConfProfileAturThresh15MinSes"),
        ("ADSL2-LINE-MIB", "adsl2LineAlarmConfProfileAturThresh15MinLoss"),
        ("ADSL2-LINE-MIB", "adsl2LineAlarmConfProfileAturThresh15MinUas"),
        ("ADSL2-LINE-MIB", "adsl2LineAlarmConfProfileThresh15MinFailedFullInt"),
        ("ADSL2-LINE-MIB", "adsl2LineAlarmConfProfileThresh15MinFailedShrtInt"),
        ("ADSL2-LINE-MIB", "adsl2LineAlarmConfProfileRowStatus"))
)
if mibBuilder.loadTexts:
    adsl2LineAlarmConfProfileGroup.setStatus("current")

adsl2ChAlarmConfProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 7, 1, 17)
)
adsl2ChAlarmConfProfileGroup.setObjects(
      *(("ADSL2-LINE-MIB", "adsl2ChAlarmConfProfileAtucThresh15MinCodingViolations"),
        ("ADSL2-LINE-MIB", "adsl2ChAlarmConfProfileAtucThresh15MinCorrected"),
        ("ADSL2-LINE-MIB", "adsl2ChAlarmConfProfileAturThresh15MinCodingViolations"),
        ("ADSL2-LINE-MIB", "adsl2ChAlarmConfProfileAturThresh15MinCorrected"),
        ("ADSL2-LINE-MIB", "adsl2ChAlarmConfProfileRowStatus"))
)
if mibBuilder.loadTexts:
    adsl2ChAlarmConfProfileGroup.setStatus("current")

adsl2PMLineCurrGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 7, 1, 18)
)
adsl2PMLineCurrGroup.setObjects(
      *(("ADSL2-LINE-MIB", "adsl2PMLCurrValidIntervals"),
        ("ADSL2-LINE-MIB", "adsl2PMLCurrInvalidIntervals"),
        ("ADSL2-LINE-MIB", "adsl2PMLCurr15MTimeElapsed"),
        ("ADSL2-LINE-MIB", "adsl2PMLCurr15MFecs"),
        ("ADSL2-LINE-MIB", "adsl2PMLCurr15MEs"),
        ("ADSL2-LINE-MIB", "adsl2PMLCurr15MSes"),
        ("ADSL2-LINE-MIB", "adsl2PMLCurr15MLoss"),
        ("ADSL2-LINE-MIB", "adsl2PMLCurr15MUas"),
        ("ADSL2-LINE-MIB", "adsl2PMLCurr1DayValidIntervals"),
        ("ADSL2-LINE-MIB", "adsl2PMLCurr1DayInvalidIntervals"),
        ("ADSL2-LINE-MIB", "adsl2PMLCurr1DayTimeElapsed"),
        ("ADSL2-LINE-MIB", "adsl2PMLCurr1DayFecs"),
        ("ADSL2-LINE-MIB", "adsl2PMLCurr1DayEs"),
        ("ADSL2-LINE-MIB", "adsl2PMLCurr1DaySes"),
        ("ADSL2-LINE-MIB", "adsl2PMLCurr1DayLoss"),
        ("ADSL2-LINE-MIB", "adsl2PMLCurr1DayUas"))
)
if mibBuilder.loadTexts:
    adsl2PMLineCurrGroup.setStatus("current")

adsl2PMLineCurrInitGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 7, 1, 19)
)
adsl2PMLineCurrInitGroup.setObjects(
      *(("ADSL2-LINE-MIB", "adsl2PMLCurrInit15MTimeElapsed"),
        ("ADSL2-LINE-MIB", "adsl2PMLCurrInit15MFullInits"),
        ("ADSL2-LINE-MIB", "adsl2PMLCurrInit15MFailedFullInits"),
        ("ADSL2-LINE-MIB", "adsl2PMLCurrInit1DayTimeElapsed"),
        ("ADSL2-LINE-MIB", "adsl2PMLCurrInit1DayFullInits"),
        ("ADSL2-LINE-MIB", "adsl2PMLCurrInit1DayFailedFullInits"))
)
if mibBuilder.loadTexts:
    adsl2PMLineCurrInitGroup.setStatus("current")

adsl2PMLineCurrInitShortGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 7, 1, 20)
)
adsl2PMLineCurrInitShortGroup.setObjects(
      *(("ADSL2-LINE-MIB", "adsl2PMLCurrInit15MShortInits"),
        ("ADSL2-LINE-MIB", "adsl2PMLCurrInit15MFailedShortInits"),
        ("ADSL2-LINE-MIB", "adsl2PMLCurrInit1DayShortInits"),
        ("ADSL2-LINE-MIB", "adsl2PMLCurrInit1DayFailedShortInits"))
)
if mibBuilder.loadTexts:
    adsl2PMLineCurrInitShortGroup.setStatus("current")

adsl2PMLineHist15MinGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 7, 1, 21)
)
adsl2PMLineHist15MinGroup.setObjects(
      *(("ADSL2-LINE-MIB", "adsl2PMLHist15MMonitoredTime"),
        ("ADSL2-LINE-MIB", "adsl2PMLHist15MFecs"),
        ("ADSL2-LINE-MIB", "adsl2PMLHist15MEs"),
        ("ADSL2-LINE-MIB", "adsl2PMLHist15MSes"),
        ("ADSL2-LINE-MIB", "adsl2PMLHist15MLoss"),
        ("ADSL2-LINE-MIB", "adsl2PMLHist15MUas"),
        ("ADSL2-LINE-MIB", "adsl2PMLHist15MValidInterval"))
)
if mibBuilder.loadTexts:
    adsl2PMLineHist15MinGroup.setStatus("current")

adsl2PMLineHist1DayGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 7, 1, 22)
)
adsl2PMLineHist1DayGroup.setObjects(
      *(("ADSL2-LINE-MIB", "adsl2PMLHist1DMonitoredTime"),
        ("ADSL2-LINE-MIB", "adsl2PMLHist1DFecs"),
        ("ADSL2-LINE-MIB", "adsl2PMLHist1DEs"),
        ("ADSL2-LINE-MIB", "adsl2PMLHist1DSes"),
        ("ADSL2-LINE-MIB", "adsl2PMLHist1DLoss"),
        ("ADSL2-LINE-MIB", "adsl2PMLHist1DUas"),
        ("ADSL2-LINE-MIB", "adsl2PMLHist1DValidInterval"))
)
if mibBuilder.loadTexts:
    adsl2PMLineHist1DayGroup.setStatus("current")

adsl2PMLineInitHist15MinGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 7, 1, 23)
)
adsl2PMLineInitHist15MinGroup.setObjects(
      *(("ADSL2-LINE-MIB", "adsl2PMLHistInit15MMonitoredTime"),
        ("ADSL2-LINE-MIB", "adsl2PMLHistInit15MFullInits"),
        ("ADSL2-LINE-MIB", "adsl2PMLHistInit15MFailedFullInits"),
        ("ADSL2-LINE-MIB", "adsl2PMLHistInit15MValidInterval"))
)
if mibBuilder.loadTexts:
    adsl2PMLineInitHist15MinGroup.setStatus("current")

adsl2PMLineInitHist15MinShortGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 7, 1, 24)
)
adsl2PMLineInitHist15MinShortGroup.setObjects(
      *(("ADSL2-LINE-MIB", "adsl2PMLHistInit15MShortInits"),
        ("ADSL2-LINE-MIB", "adsl2PMLHistInit15MFailedShortInits"))
)
if mibBuilder.loadTexts:
    adsl2PMLineInitHist15MinShortGroup.setStatus("current")

adsl2PMLineInitHist1DayGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 7, 1, 25)
)
adsl2PMLineInitHist1DayGroup.setObjects(
      *(("ADSL2-LINE-MIB", "adsl2PMLHistinit1DMonitoredTime"),
        ("ADSL2-LINE-MIB", "adsl2PMLHistinit1DFullInits"),
        ("ADSL2-LINE-MIB", "adsl2PMLHistinit1DFailedFullInits"),
        ("ADSL2-LINE-MIB", "adsl2PMLHistinit1DValidInterval"))
)
if mibBuilder.loadTexts:
    adsl2PMLineInitHist1DayGroup.setStatus("current")

adsl2PMLineInitHist1DayShortGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 7, 1, 26)
)
adsl2PMLineInitHist1DayShortGroup.setObjects(
      *(("ADSL2-LINE-MIB", "adsl2PMLHistinit1DShortInits"),
        ("ADSL2-LINE-MIB", "adsl2PMLHistinit1DFailedShortInits"))
)
if mibBuilder.loadTexts:
    adsl2PMLineInitHist1DayShortGroup.setStatus("current")

adsl2PMChCurrGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 7, 1, 27)
)
adsl2PMChCurrGroup.setObjects(
      *(("ADSL2-LINE-MIB", "adsl2PMChCurrValidIntervals"),
        ("ADSL2-LINE-MIB", "adsl2PMChCurrInvalidIntervals"),
        ("ADSL2-LINE-MIB", "adsl2PMChCurr15MTimeElapsed"),
        ("ADSL2-LINE-MIB", "adsl2PMChCurr15MCodingViolations"),
        ("ADSL2-LINE-MIB", "adsl2PMChCurr15MCorrectedBlocks"),
        ("ADSL2-LINE-MIB", "adsl2PMChCurr1DayValidIntervals"),
        ("ADSL2-LINE-MIB", "adsl2PMChCurr1DayInvalidIntervals"),
        ("ADSL2-LINE-MIB", "adsl2PMChCurr1DayTimeElapsed"),
        ("ADSL2-LINE-MIB", "adsl2PMChCurr1DayCodingViolations"),
        ("ADSL2-LINE-MIB", "adsl2PMChCurr1DayCorrectedBlocks"))
)
if mibBuilder.loadTexts:
    adsl2PMChCurrGroup.setStatus("current")

adsl2PMChHist15MinGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 7, 1, 28)
)
adsl2PMChHist15MinGroup.setObjects(
      *(("ADSL2-LINE-MIB", "adsl2PMChHist15MMonitoredTime"),
        ("ADSL2-LINE-MIB", "adsl2PMChHist15MCodingViolations"),
        ("ADSL2-LINE-MIB", "adsl2PMChHist15MCorrectedBlocks"),
        ("ADSL2-LINE-MIB", "adsl2PMChHist15MValidInterval"))
)
if mibBuilder.loadTexts:
    adsl2PMChHist15MinGroup.setStatus("current")

adsl2PMChHist1DGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 7, 1, 29)
)
adsl2PMChHist1DGroup.setObjects(
      *(("ADSL2-LINE-MIB", "adsl2PMChHist1DMonitoredTime"),
        ("ADSL2-LINE-MIB", "adsl2PMChHist1DCodingViolations"),
        ("ADSL2-LINE-MIB", "adsl2PMChHist1DCorrectedBlocks"),
        ("ADSL2-LINE-MIB", "adsl2PMChHist1DValidInterval"))
)
if mibBuilder.loadTexts:
    adsl2PMChHist1DGroup.setStatus("current")

adsl2ScalarSCGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 7, 1, 30)
)
adsl2ScalarSCGroup.setObjects(
      *(("ADSL2-LINE-MIB", "adsl2ScalarSCMaxInterfaces"),
        ("ADSL2-LINE-MIB", "adsl2ScalarSCAvailInterfaces"))
)
if mibBuilder.loadTexts:
    adsl2ScalarSCGroup.setStatus("current")


# Notification objects

adsl2LinePerfFECSThreshAtuc = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 0, 1)
)
adsl2LinePerfFECSThreshAtuc.setObjects(
      *(("ADSL2-LINE-MIB", "adsl2PMLCurr15MFecs"),
        ("ADSL2-LINE-MIB", "adsl2LineAlarmConfProfileAtucThresh15MinFecs"))
)
if mibBuilder.loadTexts:
    adsl2LinePerfFECSThreshAtuc.setStatus(
        "current"
    )

adsl2LinePerfFECSThreshAtur = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 0, 2)
)
adsl2LinePerfFECSThreshAtur.setObjects(
      *(("ADSL2-LINE-MIB", "adsl2PMLCurr15MFecs"),
        ("ADSL2-LINE-MIB", "adsl2LineAlarmConfProfileAturThresh15MinFecs"))
)
if mibBuilder.loadTexts:
    adsl2LinePerfFECSThreshAtur.setStatus(
        "current"
    )

adsl2LinePerfESThreshAtuc = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 0, 3)
)
adsl2LinePerfESThreshAtuc.setObjects(
      *(("ADSL2-LINE-MIB", "adsl2PMLCurr15MEs"),
        ("ADSL2-LINE-MIB", "adsl2LineAlarmConfProfileAtucThresh15MinEs"))
)
if mibBuilder.loadTexts:
    adsl2LinePerfESThreshAtuc.setStatus(
        "current"
    )

adsl2LinePerfESThreshAtur = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 0, 4)
)
adsl2LinePerfESThreshAtur.setObjects(
      *(("ADSL2-LINE-MIB", "adsl2PMLCurr15MEs"),
        ("ADSL2-LINE-MIB", "adsl2LineAlarmConfProfileAturThresh15MinEs"))
)
if mibBuilder.loadTexts:
    adsl2LinePerfESThreshAtur.setStatus(
        "current"
    )

adsl2LinePerfSESThreshAtuc = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 0, 5)
)
adsl2LinePerfSESThreshAtuc.setObjects(
      *(("ADSL2-LINE-MIB", "adsl2PMLCurr15MSes"),
        ("ADSL2-LINE-MIB", "adsl2LineAlarmConfProfileAtucThresh15MinSes"))
)
if mibBuilder.loadTexts:
    adsl2LinePerfSESThreshAtuc.setStatus(
        "current"
    )

adsl2LinePerfSESThreshAtur = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 0, 6)
)
adsl2LinePerfSESThreshAtur.setObjects(
      *(("ADSL2-LINE-MIB", "adsl2PMLCurr15MSes"),
        ("ADSL2-LINE-MIB", "adsl2LineAlarmConfProfileAturThresh15MinSes"))
)
if mibBuilder.loadTexts:
    adsl2LinePerfSESThreshAtur.setStatus(
        "current"
    )

adsl2LinePerfLOSSThreshAtuc = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 0, 7)
)
adsl2LinePerfLOSSThreshAtuc.setObjects(
      *(("ADSL2-LINE-MIB", "adsl2PMLCurr15MLoss"),
        ("ADSL2-LINE-MIB", "adsl2LineAlarmConfProfileAtucThresh15MinLoss"))
)
if mibBuilder.loadTexts:
    adsl2LinePerfLOSSThreshAtuc.setStatus(
        "current"
    )

adsl2LinePerfLOSSThreshAtur = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 0, 8)
)
adsl2LinePerfLOSSThreshAtur.setObjects(
      *(("ADSL2-LINE-MIB", "adsl2PMLCurr15MLoss"),
        ("ADSL2-LINE-MIB", "adsl2LineAlarmConfProfileAturThresh15MinLoss"))
)
if mibBuilder.loadTexts:
    adsl2LinePerfLOSSThreshAtur.setStatus(
        "current"
    )

adsl2LinePerfUASThreshAtuc = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 0, 9)
)
adsl2LinePerfUASThreshAtuc.setObjects(
      *(("ADSL2-LINE-MIB", "adsl2PMLCurr15MUas"),
        ("ADSL2-LINE-MIB", "adsl2LineAlarmConfProfileAtucThresh15MinUas"))
)
if mibBuilder.loadTexts:
    adsl2LinePerfUASThreshAtuc.setStatus(
        "current"
    )

adsl2LinePerfUASThreshAtur = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 0, 10)
)
adsl2LinePerfUASThreshAtur.setObjects(
      *(("ADSL2-LINE-MIB", "adsl2PMLCurr15MUas"),
        ("ADSL2-LINE-MIB", "adsl2LineAlarmConfProfileAturThresh15MinUas"))
)
if mibBuilder.loadTexts:
    adsl2LinePerfUASThreshAtur.setStatus(
        "current"
    )

adsl2LinePerfCodingViolationsThreshAtuc = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 0, 11)
)
adsl2LinePerfCodingViolationsThreshAtuc.setObjects(
      *(("ADSL2-LINE-MIB", "adsl2PMChCurr15MCodingViolations"),
        ("ADSL2-LINE-MIB", "adsl2ChAlarmConfProfileAtucThresh15MinCodingViolations"))
)
if mibBuilder.loadTexts:
    adsl2LinePerfCodingViolationsThreshAtuc.setStatus(
        "current"
    )

adsl2LinePerfCodingViolationsThreshAtur = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 0, 12)
)
adsl2LinePerfCodingViolationsThreshAtur.setObjects(
      *(("ADSL2-LINE-MIB", "adsl2PMChCurr15MCodingViolations"),
        ("ADSL2-LINE-MIB", "adsl2ChAlarmConfProfileAturThresh15MinCodingViolations"))
)
if mibBuilder.loadTexts:
    adsl2LinePerfCodingViolationsThreshAtur.setStatus(
        "current"
    )

adsl2LinePerfCorrectedThreshAtuc = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 0, 13)
)
adsl2LinePerfCorrectedThreshAtuc.setObjects(
      *(("ADSL2-LINE-MIB", "adsl2PMChCurr15MCorrectedBlocks"),
        ("ADSL2-LINE-MIB", "adsl2ChAlarmConfProfileAtucThresh15MinCorrected"))
)
if mibBuilder.loadTexts:
    adsl2LinePerfCorrectedThreshAtuc.setStatus(
        "current"
    )

adsl2LinePerfCorrectedThreshAtur = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 0, 14)
)
adsl2LinePerfCorrectedThreshAtur.setObjects(
      *(("ADSL2-LINE-MIB", "adsl2PMChCurr15MCorrectedBlocks"),
        ("ADSL2-LINE-MIB", "adsl2ChAlarmConfProfileAturThresh15MinCorrected"))
)
if mibBuilder.loadTexts:
    adsl2LinePerfCorrectedThreshAtur.setStatus(
        "current"
    )

adsl2LinePerfFailedFullInitThresh = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 0, 15)
)
adsl2LinePerfFailedFullInitThresh.setObjects(
      *(("ADSL2-LINE-MIB", "adsl2PMLCurrInit15MFailedFullInits"),
        ("ADSL2-LINE-MIB", "adsl2LineAlarmConfProfileThresh15MinFailedFullInt"))
)
if mibBuilder.loadTexts:
    adsl2LinePerfFailedFullInitThresh.setStatus(
        "current"
    )

adsl2LinePerfFailedShortInitThresh = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 0, 16)
)
adsl2LinePerfFailedShortInitThresh.setObjects(
      *(("ADSL2-LINE-MIB", "adsl2PMLCurrInit15MFailedShortInits"),
        ("ADSL2-LINE-MIB", "adsl2LineAlarmConfProfileThresh15MinFailedShrtInt"))
)
if mibBuilder.loadTexts:
    adsl2LinePerfFailedShortInitThresh.setStatus(
        "current"
    )

adsl2LineStatusChangeAtuc = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 0, 17)
)
adsl2LineStatusChangeAtuc.setObjects(
    ("ADSL2-LINE-MIB", "adsl2LineStatusAtuc")
)
if mibBuilder.loadTexts:
    adsl2LineStatusChangeAtuc.setStatus(
        "current"
    )

adsl2LineStatusChangeAtur = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 0, 18)
)
adsl2LineStatusChangeAtur.setObjects(
    ("ADSL2-LINE-MIB", "adsl2LineStatusAtur")
)
if mibBuilder.loadTexts:
    adsl2LineStatusChangeAtur.setStatus(
        "current"
    )


# Notifications groups

adsl2ThreshNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 7, 1, 31)
)
adsl2ThreshNotificationGroup.setObjects(
      *(("ADSL2-LINE-MIB", "adsl2LinePerfFECSThreshAtuc"),
        ("ADSL2-LINE-MIB", "adsl2LinePerfFECSThreshAtur"),
        ("ADSL2-LINE-MIB", "adsl2LinePerfESThreshAtuc"),
        ("ADSL2-LINE-MIB", "adsl2LinePerfESThreshAtur"),
        ("ADSL2-LINE-MIB", "adsl2LinePerfSESThreshAtuc"),
        ("ADSL2-LINE-MIB", "adsl2LinePerfSESThreshAtur"),
        ("ADSL2-LINE-MIB", "adsl2LinePerfLOSSThreshAtuc"),
        ("ADSL2-LINE-MIB", "adsl2LinePerfLOSSThreshAtur"),
        ("ADSL2-LINE-MIB", "adsl2LinePerfUASThreshAtuc"),
        ("ADSL2-LINE-MIB", "adsl2LinePerfUASThreshAtur"),
        ("ADSL2-LINE-MIB", "adsl2LinePerfCodingViolationsThreshAtuc"),
        ("ADSL2-LINE-MIB", "adsl2LinePerfCodingViolationsThreshAtur"),
        ("ADSL2-LINE-MIB", "adsl2LinePerfCorrectedThreshAtuc"),
        ("ADSL2-LINE-MIB", "adsl2LinePerfCorrectedThreshAtur"),
        ("ADSL2-LINE-MIB", "adsl2LinePerfFailedFullInitThresh"),
        ("ADSL2-LINE-MIB", "adsl2LinePerfFailedShortInitThresh"))
)
if mibBuilder.loadTexts:
    adsl2ThreshNotificationGroup.setStatus(
        "current"
    )

adsl2StatusChangeNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 7, 1, 32)
)
adsl2StatusChangeNotificationGroup.setObjects(
      *(("ADSL2-LINE-MIB", "adsl2LineStatusChangeAtuc"),
        ("ADSL2-LINE-MIB", "adsl2LineStatusChangeAtur"))
)
if mibBuilder.loadTexts:
    adsl2StatusChangeNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

adsl2LineMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 238, 1, 7, 2, 1)
)
if mibBuilder.loadTexts:
    adsl2LineMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADSL2-LINE-MIB",
    **{"adsl2MIB": adsl2MIB,
       "adsl2": adsl2,
       "adsl2Notifications": adsl2Notifications,
       "adsl2LinePerfFECSThreshAtuc": adsl2LinePerfFECSThreshAtuc,
       "adsl2LinePerfFECSThreshAtur": adsl2LinePerfFECSThreshAtur,
       "adsl2LinePerfESThreshAtuc": adsl2LinePerfESThreshAtuc,
       "adsl2LinePerfESThreshAtur": adsl2LinePerfESThreshAtur,
       "adsl2LinePerfSESThreshAtuc": adsl2LinePerfSESThreshAtuc,
       "adsl2LinePerfSESThreshAtur": adsl2LinePerfSESThreshAtur,
       "adsl2LinePerfLOSSThreshAtuc": adsl2LinePerfLOSSThreshAtuc,
       "adsl2LinePerfLOSSThreshAtur": adsl2LinePerfLOSSThreshAtur,
       "adsl2LinePerfUASThreshAtuc": adsl2LinePerfUASThreshAtuc,
       "adsl2LinePerfUASThreshAtur": adsl2LinePerfUASThreshAtur,
       "adsl2LinePerfCodingViolationsThreshAtuc": adsl2LinePerfCodingViolationsThreshAtuc,
       "adsl2LinePerfCodingViolationsThreshAtur": adsl2LinePerfCodingViolationsThreshAtur,
       "adsl2LinePerfCorrectedThreshAtuc": adsl2LinePerfCorrectedThreshAtuc,
       "adsl2LinePerfCorrectedThreshAtur": adsl2LinePerfCorrectedThreshAtur,
       "adsl2LinePerfFailedFullInitThresh": adsl2LinePerfFailedFullInitThresh,
       "adsl2LinePerfFailedShortInitThresh": adsl2LinePerfFailedShortInitThresh,
       "adsl2LineStatusChangeAtuc": adsl2LineStatusChangeAtuc,
       "adsl2LineStatusChangeAtur": adsl2LineStatusChangeAtur,
       "adsl2Line": adsl2Line,
       "adsl2LineTable": adsl2LineTable,
       "adsl2LineEntry": adsl2LineEntry,
       "adsl2LineCnfgTemplate": adsl2LineCnfgTemplate,
       "adsl2LineAlarmCnfgTemplate": adsl2LineAlarmCnfgTemplate,
       "adsl2LineCmndConfPmsf": adsl2LineCmndConfPmsf,
       "adsl2LineCmndConfLdsf": adsl2LineCmndConfLdsf,
       "adsl2LineCmndConfLdsfFailReason": adsl2LineCmndConfLdsfFailReason,
       "adsl2LineCmndAutomodeColdStart": adsl2LineCmndAutomodeColdStart,
       "adsl2LineStatusAtuTransSys": adsl2LineStatusAtuTransSys,
       "adsl2LineStatusPwrMngState": adsl2LineStatusPwrMngState,
       "adsl2LineStatusInitResult": adsl2LineStatusInitResult,
       "adsl2LineStatusLastStateDs": adsl2LineStatusLastStateDs,
       "adsl2LineStatusLastStateUs": adsl2LineStatusLastStateUs,
       "adsl2LineStatusAtur": adsl2LineStatusAtur,
       "adsl2LineStatusAtuc": adsl2LineStatusAtuc,
       "adsl2LineStatusLnAttenDs": adsl2LineStatusLnAttenDs,
       "adsl2LineStatusLnAttenUs": adsl2LineStatusLnAttenUs,
       "adsl2LineStatusSigAttenDs": adsl2LineStatusSigAttenDs,
       "adsl2LineStatusSigAttenUs": adsl2LineStatusSigAttenUs,
       "adsl2LineStatusSnrMarginDs": adsl2LineStatusSnrMarginDs,
       "adsl2LineStatusSnrMarginUs": adsl2LineStatusSnrMarginUs,
       "adsl2LineStatusAttainableRateDs": adsl2LineStatusAttainableRateDs,
       "adsl2LineStatusAttainableRateUs": adsl2LineStatusAttainableRateUs,
       "adsl2LineStatusActPsdDs": adsl2LineStatusActPsdDs,
       "adsl2LineStatusActPsdUs": adsl2LineStatusActPsdUs,
       "adsl2LineStatusActAtpDs": adsl2LineStatusActAtpDs,
       "adsl2LineStatusActAtpUs": adsl2LineStatusActAtpUs,
       "adsl2Status": adsl2Status,
       "adsl2ChannelStatusTable": adsl2ChannelStatusTable,
       "adsl2ChannelStatusEntry": adsl2ChannelStatusEntry,
       "adsl2ChStatusUnit": adsl2ChStatusUnit,
       "adsl2ChStatusChannelNum": adsl2ChStatusChannelNum,
       "adsl2ChStatusActDataRate": adsl2ChStatusActDataRate,
       "adsl2ChStatusPrevDataRate": adsl2ChStatusPrevDataRate,
       "adsl2ChStatusActDelay": adsl2ChStatusActDelay,
       "adsl2ChStatusAtmStatus": adsl2ChStatusAtmStatus,
       "adsl2ChStatusPtmStatus": adsl2ChStatusPtmStatus,
       "adsl2SCStatusTable": adsl2SCStatusTable,
       "adsl2SCStatusEntry": adsl2SCStatusEntry,
       "adsl2SCStatusDirection": adsl2SCStatusDirection,
       "adsl2SCStatusMtime": adsl2SCStatusMtime,
       "adsl2SCStatusSnr": adsl2SCStatusSnr,
       "adsl2SCStatusBitsAlloc": adsl2SCStatusBitsAlloc,
       "adsl2SCStatusGainAlloc": adsl2SCStatusGainAlloc,
       "adsl2SCStatusTssi": adsl2SCStatusTssi,
       "adsl2SCStatusLinScale": adsl2SCStatusLinScale,
       "adsl2SCStatusLinReal": adsl2SCStatusLinReal,
       "adsl2SCStatusLinImg": adsl2SCStatusLinImg,
       "adsl2SCStatusLogMt": adsl2SCStatusLogMt,
       "adsl2SCStatusLog": adsl2SCStatusLog,
       "adsl2SCStatusQlnMt": adsl2SCStatusQlnMt,
       "adsl2SCStatusQln": adsl2SCStatusQln,
       "adsl2SCStatusLnAtten": adsl2SCStatusLnAtten,
       "adsl2SCStatusSigAtten": adsl2SCStatusSigAtten,
       "adsl2SCStatusSnrMargin": adsl2SCStatusSnrMargin,
       "adsl2SCStatusAttainableRate": adsl2SCStatusAttainableRate,
       "adsl2SCStatusActAtp": adsl2SCStatusActAtp,
       "adsl2SCStatusRowStatus": adsl2SCStatusRowStatus,
       "adsl2Inventory": adsl2Inventory,
       "adsl2LineInventoryTable": adsl2LineInventoryTable,
       "adsl2LineInventoryEntry": adsl2LineInventoryEntry,
       "adsl2LInvUnit": adsl2LInvUnit,
       "adsl2LInvG994VendorId": adsl2LInvG994VendorId,
       "adsl2LInvSystemVendorId": adsl2LInvSystemVendorId,
       "adsl2LInvVersionNumber": adsl2LInvVersionNumber,
       "adsl2LInvSerialNumber": adsl2LInvSerialNumber,
       "adsl2LInvSelfTestResult": adsl2LInvSelfTestResult,
       "adsl2LInvTransmissionCapabilities": adsl2LInvTransmissionCapabilities,
       "adsl2PM": adsl2PM,
       "adsl2PMLine": adsl2PMLine,
       "adsl2PMLineCurrTable": adsl2PMLineCurrTable,
       "adsl2PMLineCurrEntry": adsl2PMLineCurrEntry,
       "adsl2PMLCurrUnit": adsl2PMLCurrUnit,
       "adsl2PMLCurrValidIntervals": adsl2PMLCurrValidIntervals,
       "adsl2PMLCurrInvalidIntervals": adsl2PMLCurrInvalidIntervals,
       "adsl2PMLCurr15MTimeElapsed": adsl2PMLCurr15MTimeElapsed,
       "adsl2PMLCurr15MFecs": adsl2PMLCurr15MFecs,
       "adsl2PMLCurr15MEs": adsl2PMLCurr15MEs,
       "adsl2PMLCurr15MSes": adsl2PMLCurr15MSes,
       "adsl2PMLCurr15MLoss": adsl2PMLCurr15MLoss,
       "adsl2PMLCurr15MUas": adsl2PMLCurr15MUas,
       "adsl2PMLCurr1DayValidIntervals": adsl2PMLCurr1DayValidIntervals,
       "adsl2PMLCurr1DayInvalidIntervals": adsl2PMLCurr1DayInvalidIntervals,
       "adsl2PMLCurr1DayTimeElapsed": adsl2PMLCurr1DayTimeElapsed,
       "adsl2PMLCurr1DayFecs": adsl2PMLCurr1DayFecs,
       "adsl2PMLCurr1DayEs": adsl2PMLCurr1DayEs,
       "adsl2PMLCurr1DaySes": adsl2PMLCurr1DaySes,
       "adsl2PMLCurr1DayLoss": adsl2PMLCurr1DayLoss,
       "adsl2PMLCurr1DayUas": adsl2PMLCurr1DayUas,
       "adsl2PMLineCurrInitTable": adsl2PMLineCurrInitTable,
       "adsl2PMLineCurrInitEntry": adsl2PMLineCurrInitEntry,
       "adsl2PMLCurrInit15MTimeElapsed": adsl2PMLCurrInit15MTimeElapsed,
       "adsl2PMLCurrInit15MFullInits": adsl2PMLCurrInit15MFullInits,
       "adsl2PMLCurrInit15MFailedFullInits": adsl2PMLCurrInit15MFailedFullInits,
       "adsl2PMLCurrInit15MShortInits": adsl2PMLCurrInit15MShortInits,
       "adsl2PMLCurrInit15MFailedShortInits": adsl2PMLCurrInit15MFailedShortInits,
       "adsl2PMLCurrInit1DayTimeElapsed": adsl2PMLCurrInit1DayTimeElapsed,
       "adsl2PMLCurrInit1DayFullInits": adsl2PMLCurrInit1DayFullInits,
       "adsl2PMLCurrInit1DayFailedFullInits": adsl2PMLCurrInit1DayFailedFullInits,
       "adsl2PMLCurrInit1DayShortInits": adsl2PMLCurrInit1DayShortInits,
       "adsl2PMLCurrInit1DayFailedShortInits": adsl2PMLCurrInit1DayFailedShortInits,
       "adsl2PMLineHist15MinTable": adsl2PMLineHist15MinTable,
       "adsl2PMLineHist15MinEntry": adsl2PMLineHist15MinEntry,
       "adsl2PMLHist15MUnit": adsl2PMLHist15MUnit,
       "adsl2PMLHist15MInterval": adsl2PMLHist15MInterval,
       "adsl2PMLHist15MMonitoredTime": adsl2PMLHist15MMonitoredTime,
       "adsl2PMLHist15MFecs": adsl2PMLHist15MFecs,
       "adsl2PMLHist15MEs": adsl2PMLHist15MEs,
       "adsl2PMLHist15MSes": adsl2PMLHist15MSes,
       "adsl2PMLHist15MLoss": adsl2PMLHist15MLoss,
       "adsl2PMLHist15MUas": adsl2PMLHist15MUas,
       "adsl2PMLHist15MValidInterval": adsl2PMLHist15MValidInterval,
       "adsl2PMLineHist1DayTable": adsl2PMLineHist1DayTable,
       "adsl2PMLineHist1DayEntry": adsl2PMLineHist1DayEntry,
       "adsl2PMLHist1DUnit": adsl2PMLHist1DUnit,
       "adsl2PMLHist1DInterval": adsl2PMLHist1DInterval,
       "adsl2PMLHist1DMonitoredTime": adsl2PMLHist1DMonitoredTime,
       "adsl2PMLHist1DFecs": adsl2PMLHist1DFecs,
       "adsl2PMLHist1DEs": adsl2PMLHist1DEs,
       "adsl2PMLHist1DSes": adsl2PMLHist1DSes,
       "adsl2PMLHist1DLoss": adsl2PMLHist1DLoss,
       "adsl2PMLHist1DUas": adsl2PMLHist1DUas,
       "adsl2PMLHist1DValidInterval": adsl2PMLHist1DValidInterval,
       "adsl2PMLineInitHist15MinTable": adsl2PMLineInitHist15MinTable,
       "adsl2PMLineInitHist15MinEntry": adsl2PMLineInitHist15MinEntry,
       "adsl2PMLHistInit15MInterval": adsl2PMLHistInit15MInterval,
       "adsl2PMLHistInit15MMonitoredTime": adsl2PMLHistInit15MMonitoredTime,
       "adsl2PMLHistInit15MFullInits": adsl2PMLHistInit15MFullInits,
       "adsl2PMLHistInit15MFailedFullInits": adsl2PMLHistInit15MFailedFullInits,
       "adsl2PMLHistInit15MShortInits": adsl2PMLHistInit15MShortInits,
       "adsl2PMLHistInit15MFailedShortInits": adsl2PMLHistInit15MFailedShortInits,
       "adsl2PMLHistInit15MValidInterval": adsl2PMLHistInit15MValidInterval,
       "adsl2PMLineInitHist1DayTable": adsl2PMLineInitHist1DayTable,
       "adsl2PMLineInitHist1DayEntry": adsl2PMLineInitHist1DayEntry,
       "adsl2PMLHistinit1DInterval": adsl2PMLHistinit1DInterval,
       "adsl2PMLHistinit1DMonitoredTime": adsl2PMLHistinit1DMonitoredTime,
       "adsl2PMLHistinit1DFullInits": adsl2PMLHistinit1DFullInits,
       "adsl2PMLHistinit1DFailedFullInits": adsl2PMLHistinit1DFailedFullInits,
       "adsl2PMLHistinit1DShortInits": adsl2PMLHistinit1DShortInits,
       "adsl2PMLHistinit1DFailedShortInits": adsl2PMLHistinit1DFailedShortInits,
       "adsl2PMLHistinit1DValidInterval": adsl2PMLHistinit1DValidInterval,
       "adsl2PMChannel": adsl2PMChannel,
       "adsl2PMChCurrTable": adsl2PMChCurrTable,
       "adsl2PMChCurrEntry": adsl2PMChCurrEntry,
       "adsl2PMChCurrUnit": adsl2PMChCurrUnit,
       "adsl2PMChCurrValidIntervals": adsl2PMChCurrValidIntervals,
       "adsl2PMChCurrInvalidIntervals": adsl2PMChCurrInvalidIntervals,
       "adsl2PMChCurr15MTimeElapsed": adsl2PMChCurr15MTimeElapsed,
       "adsl2PMChCurr15MCodingViolations": adsl2PMChCurr15MCodingViolations,
       "adsl2PMChCurr15MCorrectedBlocks": adsl2PMChCurr15MCorrectedBlocks,
       "adsl2PMChCurr1DayValidIntervals": adsl2PMChCurr1DayValidIntervals,
       "adsl2PMChCurr1DayInvalidIntervals": adsl2PMChCurr1DayInvalidIntervals,
       "adsl2PMChCurr1DayTimeElapsed": adsl2PMChCurr1DayTimeElapsed,
       "adsl2PMChCurr1DayCodingViolations": adsl2PMChCurr1DayCodingViolations,
       "adsl2PMChCurr1DayCorrectedBlocks": adsl2PMChCurr1DayCorrectedBlocks,
       "adsl2PMChHist15MinTable": adsl2PMChHist15MinTable,
       "adsl2PMChHist15MinEntry": adsl2PMChHist15MinEntry,
       "adsl2PMChHist15MUnit": adsl2PMChHist15MUnit,
       "adsl2PMChHist15MInterval": adsl2PMChHist15MInterval,
       "adsl2PMChHist15MMonitoredTime": adsl2PMChHist15MMonitoredTime,
       "adsl2PMChHist15MCodingViolations": adsl2PMChHist15MCodingViolations,
       "adsl2PMChHist15MCorrectedBlocks": adsl2PMChHist15MCorrectedBlocks,
       "adsl2PMChHist15MValidInterval": adsl2PMChHist15MValidInterval,
       "adsl2PMChHist1DTable": adsl2PMChHist1DTable,
       "adsl2PMChHist1DEntry": adsl2PMChHist1DEntry,
       "adsl2PMChHist1DUnit": adsl2PMChHist1DUnit,
       "adsl2PMChHist1DInterval": adsl2PMChHist1DInterval,
       "adsl2PMChHist1DMonitoredTime": adsl2PMChHist1DMonitoredTime,
       "adsl2PMChHist1DCodingViolations": adsl2PMChHist1DCodingViolations,
       "adsl2PMChHist1DCorrectedBlocks": adsl2PMChHist1DCorrectedBlocks,
       "adsl2PMChHist1DValidInterval": adsl2PMChHist1DValidInterval,
       "adsl2Profile": adsl2Profile,
       "adsl2ProfileLine": adsl2ProfileLine,
       "adsl2LineConfTemplateTable": adsl2LineConfTemplateTable,
       "adsl2LineConfTemplateEntry": adsl2LineConfTemplateEntry,
       "adsl2LConfTempTemplateName": adsl2LConfTempTemplateName,
       "adsl2LConfTempLineProfile": adsl2LConfTempLineProfile,
       "adsl2LConfTempChan1ConfProfile": adsl2LConfTempChan1ConfProfile,
       "adsl2LConfTempChan1RaRatioDs": adsl2LConfTempChan1RaRatioDs,
       "adsl2LConfTempChan1RaRatioUs": adsl2LConfTempChan1RaRatioUs,
       "adsl2LConfTempChan2ConfProfile": adsl2LConfTempChan2ConfProfile,
       "adsl2LConfTempChan2RaRatioDs": adsl2LConfTempChan2RaRatioDs,
       "adsl2LConfTempChan2RaRatioUs": adsl2LConfTempChan2RaRatioUs,
       "adsl2LConfTempChan3ConfProfile": adsl2LConfTempChan3ConfProfile,
       "adsl2LConfTempChan3RaRatioDs": adsl2LConfTempChan3RaRatioDs,
       "adsl2LConfTempChan3RaRatioUs": adsl2LConfTempChan3RaRatioUs,
       "adsl2LConfTempChan4ConfProfile": adsl2LConfTempChan4ConfProfile,
       "adsl2LConfTempChan4RaRatioDs": adsl2LConfTempChan4RaRatioDs,
       "adsl2LConfTempChan4RaRatioUs": adsl2LConfTempChan4RaRatioUs,
       "adsl2LConfTempRowStatus": adsl2LConfTempRowStatus,
       "adsl2LineConfProfTable": adsl2LineConfProfTable,
       "adsl2LineConfProfEntry": adsl2LineConfProfEntry,
       "adsl2LConfProfProfileName": adsl2LConfProfProfileName,
       "adsl2LConfProfScMaskDs": adsl2LConfProfScMaskDs,
       "adsl2LConfProfScMaskUs": adsl2LConfProfScMaskUs,
       "adsl2LConfProfRfiBandsDs": adsl2LConfProfRfiBandsDs,
       "adsl2LConfProfRaModeDs": adsl2LConfProfRaModeDs,
       "adsl2LConfProfRaModeUs": adsl2LConfProfRaModeUs,
       "adsl2LConfProfRaUsNrmDs": adsl2LConfProfRaUsNrmDs,
       "adsl2LConfProfRaUsNrmUs": adsl2LConfProfRaUsNrmUs,
       "adsl2LConfProfRaUsTimeDs": adsl2LConfProfRaUsTimeDs,
       "adsl2LConfProfRaUsTimeUs": adsl2LConfProfRaUsTimeUs,
       "adsl2LConfProfRaDsNrmsDs": adsl2LConfProfRaDsNrmsDs,
       "adsl2LConfProfRaDsNrmsUs": adsl2LConfProfRaDsNrmsUs,
       "adsl2LConfProfRaDsTimeDs": adsl2LConfProfRaDsTimeDs,
       "adsl2LConfProfRaDsTimeUs": adsl2LConfProfRaDsTimeUs,
       "adsl2LConfProfTargetSnrmDs": adsl2LConfProfTargetSnrmDs,
       "adsl2LConfProfTargetSnrmUs": adsl2LConfProfTargetSnrmUs,
       "adsl2LConfProfMaxSnrmDs": adsl2LConfProfMaxSnrmDs,
       "adsl2LConfProfMaxSnrmUs": adsl2LConfProfMaxSnrmUs,
       "adsl2LConfProfMinSnrmDs": adsl2LConfProfMinSnrmDs,
       "adsl2LConfProfMinSnrmUs": adsl2LConfProfMinSnrmUs,
       "adsl2LConfProfMsgMinUs": adsl2LConfProfMsgMinUs,
       "adsl2LConfProfMsgMinDs": adsl2LConfProfMsgMinDs,
       "adsl2LConfProfAtuTransSysEna": adsl2LConfProfAtuTransSysEna,
       "adsl2LConfProfPmMode": adsl2LConfProfPmMode,
       "adsl2LConfProfL0Time": adsl2LConfProfL0Time,
       "adsl2LConfProfL2Time": adsl2LConfProfL2Time,
       "adsl2LConfProfL2Atpr": adsl2LConfProfL2Atpr,
       "adsl2LConfProfL2Atprt": adsl2LConfProfL2Atprt,
       "adsl2LConfProfRowStatus": adsl2LConfProfRowStatus,
       "adsl2LineConfProfModeSpecTable": adsl2LineConfProfModeSpecTable,
       "adsl2LineConfProfModeSpecEntry": adsl2LineConfProfModeSpecEntry,
       "adsl2LConfProfAdslMode": adsl2LConfProfAdslMode,
       "adsl2LConfProfMaxNomPsdDs": adsl2LConfProfMaxNomPsdDs,
       "adsl2LConfProfMaxNomPsdUs": adsl2LConfProfMaxNomPsdUs,
       "adsl2LConfProfMaxNomAtpDs": adsl2LConfProfMaxNomAtpDs,
       "adsl2LConfProfMaxNomAtpUs": adsl2LConfProfMaxNomAtpUs,
       "adsl2LConfProfMaxAggRxPwrUs": adsl2LConfProfMaxAggRxPwrUs,
       "adsl2LConfProfPsdMaskDs": adsl2LConfProfPsdMaskDs,
       "adsl2LConfProfPsdMaskUs": adsl2LConfProfPsdMaskUs,
       "adsl2LConfProfPsdMaskSelectUs": adsl2LConfProfPsdMaskSelectUs,
       "adsl2LConfProfModeSpecRowStatus": adsl2LConfProfModeSpecRowStatus,
       "adsl2ProfileChannel": adsl2ProfileChannel,
       "adsl2ChConfProfileTable": adsl2ChConfProfileTable,
       "adsl2ChConfProfileEntry": adsl2ChConfProfileEntry,
       "adsl2ChConfProfProfileName": adsl2ChConfProfProfileName,
       "adsl2ChConfProfMinDataRateDs": adsl2ChConfProfMinDataRateDs,
       "adsl2ChConfProfMinDataRateUs": adsl2ChConfProfMinDataRateUs,
       "adsl2ChConfProfMinResDataRateDs": adsl2ChConfProfMinResDataRateDs,
       "adsl2ChConfProfMinResDataRateUs": adsl2ChConfProfMinResDataRateUs,
       "adsl2ChConfProfMaxDataRateDs": adsl2ChConfProfMaxDataRateDs,
       "adsl2ChConfProfMaxDataRateUs": adsl2ChConfProfMaxDataRateUs,
       "adsl2ChConfProfMinDataRateLowPwrDs": adsl2ChConfProfMinDataRateLowPwrDs,
       "adsl2ChConfProfMaxDelayDs": adsl2ChConfProfMaxDelayDs,
       "adsl2ChConfProfMaxDelayUs": adsl2ChConfProfMaxDelayUs,
       "adsl2ChConfProfMinProtectionDs": adsl2ChConfProfMinProtectionDs,
       "adsl2ChConfProfMinProtectionUs": adsl2ChConfProfMinProtectionUs,
       "adsl2ChConfProfMaxBerDs": adsl2ChConfProfMaxBerDs,
       "adsl2ChConfProfMaxBerUs": adsl2ChConfProfMaxBerUs,
       "adsl2ChConfProfUsDataRateDs": adsl2ChConfProfUsDataRateDs,
       "adsl2ChConfProfDsDataRateDs": adsl2ChConfProfDsDataRateDs,
       "adsl2ChConfProfUsDataRateUs": adsl2ChConfProfUsDataRateUs,
       "adsl2ChConfProfDsDataRateUs": adsl2ChConfProfDsDataRateUs,
       "adsl2ChConfProfImaEnabled": adsl2ChConfProfImaEnabled,
       "adsl2ChConfProfRowStatus": adsl2ChConfProfRowStatus,
       "adsl2ProfileAlarmConf": adsl2ProfileAlarmConf,
       "adsl2LineAlarmConfTemplateTable": adsl2LineAlarmConfTemplateTable,
       "adsl2LineAlarmConfTemplateEntry": adsl2LineAlarmConfTemplateEntry,
       "adsl2LAlarmConfTempTemplateName": adsl2LAlarmConfTempTemplateName,
       "adsl2LAlarmConfTempLineProfile": adsl2LAlarmConfTempLineProfile,
       "adsl2LAlarmConfTempChan1ConfProfile": adsl2LAlarmConfTempChan1ConfProfile,
       "adsl2LAlarmConfTempChan2ConfProfile": adsl2LAlarmConfTempChan2ConfProfile,
       "adsl2LAlarmConfTempChan3ConfProfile": adsl2LAlarmConfTempChan3ConfProfile,
       "adsl2LAlarmConfTempChan4ConfProfile": adsl2LAlarmConfTempChan4ConfProfile,
       "adsl2LAlarmConfTempRowStatus": adsl2LAlarmConfTempRowStatus,
       "adsl2LineAlarmConfProfileTable": adsl2LineAlarmConfProfileTable,
       "adsl2LineAlarmConfProfileEntry": adsl2LineAlarmConfProfileEntry,
       "adsl2LineAlarmConfProfileName": adsl2LineAlarmConfProfileName,
       "adsl2LineAlarmConfProfileAtucThresh15MinFecs": adsl2LineAlarmConfProfileAtucThresh15MinFecs,
       "adsl2LineAlarmConfProfileAtucThresh15MinEs": adsl2LineAlarmConfProfileAtucThresh15MinEs,
       "adsl2LineAlarmConfProfileAtucThresh15MinSes": adsl2LineAlarmConfProfileAtucThresh15MinSes,
       "adsl2LineAlarmConfProfileAtucThresh15MinLoss": adsl2LineAlarmConfProfileAtucThresh15MinLoss,
       "adsl2LineAlarmConfProfileAtucThresh15MinUas": adsl2LineAlarmConfProfileAtucThresh15MinUas,
       "adsl2LineAlarmConfProfileAturThresh15MinFecs": adsl2LineAlarmConfProfileAturThresh15MinFecs,
       "adsl2LineAlarmConfProfileAturThresh15MinEs": adsl2LineAlarmConfProfileAturThresh15MinEs,
       "adsl2LineAlarmConfProfileAturThresh15MinSes": adsl2LineAlarmConfProfileAturThresh15MinSes,
       "adsl2LineAlarmConfProfileAturThresh15MinLoss": adsl2LineAlarmConfProfileAturThresh15MinLoss,
       "adsl2LineAlarmConfProfileAturThresh15MinUas": adsl2LineAlarmConfProfileAturThresh15MinUas,
       "adsl2LineAlarmConfProfileThresh15MinFailedFullInt": adsl2LineAlarmConfProfileThresh15MinFailedFullInt,
       "adsl2LineAlarmConfProfileThresh15MinFailedShrtInt": adsl2LineAlarmConfProfileThresh15MinFailedShrtInt,
       "adsl2LineAlarmConfProfileRowStatus": adsl2LineAlarmConfProfileRowStatus,
       "adsl2ChAlarmConfProfileTable": adsl2ChAlarmConfProfileTable,
       "adsl2ChAlarmConfProfileEntry": adsl2ChAlarmConfProfileEntry,
       "adsl2ChAlarmConfProfileName": adsl2ChAlarmConfProfileName,
       "adsl2ChAlarmConfProfileAtucThresh15MinCodingViolations": adsl2ChAlarmConfProfileAtucThresh15MinCodingViolations,
       "adsl2ChAlarmConfProfileAtucThresh15MinCorrected": adsl2ChAlarmConfProfileAtucThresh15MinCorrected,
       "adsl2ChAlarmConfProfileAturThresh15MinCodingViolations": adsl2ChAlarmConfProfileAturThresh15MinCodingViolations,
       "adsl2ChAlarmConfProfileAturThresh15MinCorrected": adsl2ChAlarmConfProfileAturThresh15MinCorrected,
       "adsl2ChAlarmConfProfileRowStatus": adsl2ChAlarmConfProfileRowStatus,
       "adsl2Scalar": adsl2Scalar,
       "adsl2ScalarSC": adsl2ScalarSC,
       "adsl2ScalarSCMaxInterfaces": adsl2ScalarSCMaxInterfaces,
       "adsl2ScalarSCAvailInterfaces": adsl2ScalarSCAvailInterfaces,
       "adsl2Conformance": adsl2Conformance,
       "adsl2Groups": adsl2Groups,
       "adsl2LineGroup": adsl2LineGroup,
       "adsl2ChannelStatusGroup": adsl2ChannelStatusGroup,
       "adsl2ChannelStatusAtmGroup": adsl2ChannelStatusAtmGroup,
       "adsl2ChannelStatusPtmGroup": adsl2ChannelStatusPtmGroup,
       "adsl2SCStatusGroup": adsl2SCStatusGroup,
       "adsl2LineInventoryGroup": adsl2LineInventoryGroup,
       "adsl2LineConfTemplateGroup": adsl2LineConfTemplateGroup,
       "adsl2LineConfProfGroup": adsl2LineConfProfGroup,
       "adsl2LineConfProfRaGroup": adsl2LineConfProfRaGroup,
       "adsl2LineConfProfMsgMinGroup": adsl2LineConfProfMsgMinGroup,
       "adsl2LineConfProfModeSpecGroup": adsl2LineConfProfModeSpecGroup,
       "adsl2ChConfProfileGroup": adsl2ChConfProfileGroup,
       "adsl2ChConfProfileAtmGroup": adsl2ChConfProfileAtmGroup,
       "adsl2ChConfProfileMinResGroup": adsl2ChConfProfileMinResGroup,
       "adsl2LineAlarmConfTemplateGroup": adsl2LineAlarmConfTemplateGroup,
       "adsl2LineAlarmConfProfileGroup": adsl2LineAlarmConfProfileGroup,
       "adsl2ChAlarmConfProfileGroup": adsl2ChAlarmConfProfileGroup,
       "adsl2PMLineCurrGroup": adsl2PMLineCurrGroup,
       "adsl2PMLineCurrInitGroup": adsl2PMLineCurrInitGroup,
       "adsl2PMLineCurrInitShortGroup": adsl2PMLineCurrInitShortGroup,
       "adsl2PMLineHist15MinGroup": adsl2PMLineHist15MinGroup,
       "adsl2PMLineHist1DayGroup": adsl2PMLineHist1DayGroup,
       "adsl2PMLineInitHist15MinGroup": adsl2PMLineInitHist15MinGroup,
       "adsl2PMLineInitHist15MinShortGroup": adsl2PMLineInitHist15MinShortGroup,
       "adsl2PMLineInitHist1DayGroup": adsl2PMLineInitHist1DayGroup,
       "adsl2PMLineInitHist1DayShortGroup": adsl2PMLineInitHist1DayShortGroup,
       "adsl2PMChCurrGroup": adsl2PMChCurrGroup,
       "adsl2PMChHist15MinGroup": adsl2PMChHist15MinGroup,
       "adsl2PMChHist1DGroup": adsl2PMChHist1DGroup,
       "adsl2ScalarSCGroup": adsl2ScalarSCGroup,
       "adsl2ThreshNotificationGroup": adsl2ThreshNotificationGroup,
       "adsl2StatusChangeNotificationGroup": adsl2StatusChangeNotificationGroup,
       "adsl2Compliances": adsl2Compliances,
       "adsl2LineMibCompliance": adsl2LineMibCompliance}
)
