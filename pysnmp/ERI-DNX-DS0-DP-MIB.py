# SNMP MIB module (ERI-DNX-DS0-DP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ERI-DNX-DS0-DP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:40:22 2024
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

(FunctionSwitch,
 LinkPortAddress,
 PortStatus,
 devices,
 trapSequence) = mibBuilder.importSymbols(
    "ERI-DNX-SMC-MIB",
    "FunctionSwitch",
    "LinkPortAddress",
    "PortStatus",
    "devices",
    "trapSequence")

(eriMibs,) = mibBuilder.importSymbols(
    "ERI-ROOT-SMI",
    "eriMibs")

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

eriDNXDs0dpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 644, 3, 10)
)
eriDNXDs0dpMIB.setRevisions(
        ("2002-10-30 00:00",
         "2002-05-21 00:00",
         "2002-04-11 00:00",
         "2001-08-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DnxDS0DP_ObjectIdentity = ObjectIdentity
dnxDS0DP = _DnxDS0DP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 6)
)
_DnxDS0DPEnterprise_ObjectIdentity = ObjectIdentity
dnxDS0DPEnterprise = _DnxDS0DPEnterprise_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 6, 0)
)
if mibBuilder.loadTexts:
    dnxDS0DPEnterprise.setStatus("current")
_Ds0DpConfig_ObjectIdentity = ObjectIdentity
ds0DpConfig = _Ds0DpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 6, 1)
)
_Ds0DpPortConfigTable_Object = MibTable
ds0DpPortConfigTable = _Ds0DpPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 6, 1, 1)
)
if mibBuilder.loadTexts:
    ds0DpPortConfigTable.setStatus("current")
_Ds0DpPortConfigEntry_Object = MibTableRow
ds0DpPortConfigEntry = _Ds0DpPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 6, 1, 1, 1)
)
ds0DpPortConfigEntry.setIndexNames(
    (0, "ERI-DNX-DS0-DP-MIB", "ds0DpCfgPortAddr"),
)
if mibBuilder.loadTexts:
    ds0DpPortConfigEntry.setStatus("current")
_Ds0DpCfgPortAddr_Type = LinkPortAddress
_Ds0DpCfgPortAddr_Object = MibTableColumn
ds0DpCfgPortAddr = _Ds0DpCfgPortAddr_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 6, 1, 1, 1, 1),
    _Ds0DpCfgPortAddr_Type()
)
ds0DpCfgPortAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds0DpCfgPortAddr.setStatus("current")
_Ds0DpCfgResource_Type = Integer32
_Ds0DpCfgResource_Object = MibTableColumn
ds0DpCfgResource = _Ds0DpCfgResource_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 6, 1, 1, 1, 2),
    _Ds0DpCfgResource_Type()
)
ds0DpCfgResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds0DpCfgResource.setStatus("current")


class _Ds0DpCfgPortName_Type(DisplayString):
    """Custom type ds0DpCfgPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_Ds0DpCfgPortName_Type.__name__ = "DisplayString"
_Ds0DpCfgPortName_Object = MibTableColumn
ds0DpCfgPortName = _Ds0DpCfgPortName_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 6, 1, 1, 1, 3),
    _Ds0DpCfgPortName_Type()
)
ds0DpCfgPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds0DpCfgPortName.setStatus("current")
_Ds0DpCfgStatus_Type = PortStatus
_Ds0DpCfgStatus_Object = MibTableColumn
ds0DpCfgStatus = _Ds0DpCfgStatus_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 6, 1, 1, 1, 4),
    _Ds0DpCfgStatus_Type()
)
ds0DpCfgStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds0DpCfgStatus.setStatus("current")


class _Ds0DpCfgRate_Type(Integer32):
    """Custom type ds0DpCfgRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("r56K", 1),
          ("r64K", 0))
    )


_Ds0DpCfgRate_Type.__name__ = "Integer32"
_Ds0DpCfgRate_Object = MibTableColumn
ds0DpCfgRate = _Ds0DpCfgRate_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 6, 1, 1, 1, 5),
    _Ds0DpCfgRate_Type()
)
ds0DpCfgRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds0DpCfgRate.setStatus("current")
_Ds0DpCfgZeroCodeEnf_Type = FunctionSwitch
_Ds0DpCfgZeroCodeEnf_Object = MibTableColumn
ds0DpCfgZeroCodeEnf = _Ds0DpCfgZeroCodeEnf_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 6, 1, 1, 1, 6),
    _Ds0DpCfgZeroCodeEnf_Type()
)
ds0DpCfgZeroCodeEnf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds0DpCfgZeroCodeEnf.setStatus("current")
_Ds0DpCfgLoopDetect_Type = FunctionSwitch
_Ds0DpCfgLoopDetect_Object = MibTableColumn
ds0DpCfgLoopDetect = _Ds0DpCfgLoopDetect_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 6, 1, 1, 1, 7),
    _Ds0DpCfgLoopDetect_Type()
)
ds0DpCfgLoopDetect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds0DpCfgLoopDetect.setStatus("current")


class _Ds0DpCfgCmdStatus_Type(Integer32):
    """Custom type ds0DpCfgCmdStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              7,
              9,
              12,
              101,
              107,
              109,
              112,
              400,
              401,
              403,
              406,
              407,
              410,
              450,
              500,
              501,
              502)
        )
    )
    namedValues = NamedValues(
        *(("copy-successful", 109),
          ("copyToAll", 9),
          ("err-data-locked-by-another-user", 450),
          ("err-general-config-error", 400),
          ("err-invalid-network-loop", 410),
          ("err-invalid-port-command", 403),
          ("err-invalid-port-rate", 407),
          ("err-invalid-port-status", 401),
          ("err-invalid-snmp-type", 501),
          ("err-invalid-snmp-var-size", 502),
          ("err-invalid-zero-code", 406),
          ("err-snmp-parse-failed", 500),
          ("inServiceAll", 7),
          ("insvc-successful", 107),
          ("oos-successful", 112),
          ("outOfServiceAll", 12),
          ("ready-for-command", 0),
          ("update", 1),
          ("update-successful", 101))
    )


_Ds0DpCfgCmdStatus_Type.__name__ = "Integer32"
_Ds0DpCfgCmdStatus_Object = MibTableColumn
ds0DpCfgCmdStatus = _Ds0DpCfgCmdStatus_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 6, 1, 1, 1, 8),
    _Ds0DpCfgCmdStatus_Type()
)
ds0DpCfgCmdStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds0DpCfgCmdStatus.setStatus("current")
_Ds0DpClockConfigTable_Object = MibTable
ds0DpClockConfigTable = _Ds0DpClockConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 6, 1, 2)
)
if mibBuilder.loadTexts:
    ds0DpClockConfigTable.setStatus("current")
_Ds0DpClockConfigEntry_Object = MibTableRow
ds0DpClockConfigEntry = _Ds0DpClockConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 6, 1, 2, 1)
)
ds0DpClockConfigEntry.setIndexNames(
    (0, "ERI-DNX-DS0-DP-MIB", "ds0DpCompClockAddr"),
)
if mibBuilder.loadTexts:
    ds0DpClockConfigEntry.setStatus("current")
_Ds0DpCompClockAddr_Type = LinkPortAddress
_Ds0DpCompClockAddr_Object = MibTableColumn
ds0DpCompClockAddr = _Ds0DpCompClockAddr_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 6, 1, 2, 1, 1),
    _Ds0DpCompClockAddr_Type()
)
ds0DpCompClockAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds0DpCompClockAddr.setStatus("current")
_Ds0DpCompClockResource_Type = Integer32
_Ds0DpCompClockResource_Object = MibTableColumn
ds0DpCompClockResource = _Ds0DpCompClockResource_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 6, 1, 2, 1, 2),
    _Ds0DpCompClockResource_Type()
)
ds0DpCompClockResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds0DpCompClockResource.setStatus("current")
_Ds0DpCompClockStatus_Type = FunctionSwitch
_Ds0DpCompClockStatus_Object = MibTableColumn
ds0DpCompClockStatus = _Ds0DpCompClockStatus_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 6, 1, 2, 1, 3),
    _Ds0DpCompClockStatus_Type()
)
ds0DpCompClockStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds0DpCompClockStatus.setStatus("current")


class _Ds0DpCompClockCmdStatus_Type(Integer32):
    """Custom type ds0DpCompClockCmdStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              101,
              400,
              401,
              403,
              450,
              500,
              501,
              502)
        )
    )
    namedValues = NamedValues(
        *(("err-data-locked-by-another-user", 450),
          ("err-general-clock-config-error", 400),
          ("err-invalid-clock-command", 403),
          ("err-invalid-clock-status", 401),
          ("err-invalid-snmp-type", 501),
          ("err-invalid-snmp-var-size", 502),
          ("err-snmp-parse-failed", 500),
          ("ready-for-command", 0),
          ("update", 1),
          ("update-successful", 101))
    )


_Ds0DpCompClockCmdStatus_Type.__name__ = "Integer32"
_Ds0DpCompClockCmdStatus_Object = MibTableColumn
ds0DpCompClockCmdStatus = _Ds0DpCompClockCmdStatus_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 6, 1, 2, 1, 4),
    _Ds0DpCompClockCmdStatus_Type()
)
ds0DpCompClockCmdStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds0DpCompClockCmdStatus.setStatus("current")
_Ds0DpDiag_ObjectIdentity = ObjectIdentity
ds0DpDiag = _Ds0DpDiag_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 6, 2)
)
_Ds0dpPortDiagTable_Object = MibTable
ds0dpPortDiagTable = _Ds0dpPortDiagTable_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 6, 2, 1)
)
if mibBuilder.loadTexts:
    ds0dpPortDiagTable.setStatus("current")
_Ds0dpPortDiagEntry_Object = MibTableRow
ds0dpPortDiagEntry = _Ds0dpPortDiagEntry_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 6, 2, 1, 1)
)
ds0dpPortDiagEntry.setIndexNames(
    (0, "ERI-DNX-DS0-DP-MIB", "ds0dpDiagAddr"),
)
if mibBuilder.loadTexts:
    ds0dpPortDiagEntry.setStatus("current")
_Ds0dpDiagAddr_Type = LinkPortAddress
_Ds0dpDiagAddr_Object = MibTableColumn
ds0dpDiagAddr = _Ds0dpDiagAddr_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 6, 2, 1, 1, 1),
    _Ds0dpDiagAddr_Type()
)
ds0dpDiagAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds0dpDiagAddr.setStatus("current")
_Ds0dpDiagResource_Type = Integer32
_Ds0dpDiagResource_Object = MibTableColumn
ds0dpDiagResource = _Ds0dpDiagResource_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 6, 2, 1, 1, 2),
    _Ds0dpDiagResource_Type()
)
ds0dpDiagResource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds0dpDiagResource.setStatus("current")


class _Ds0dpDiagState_Type(Integer32):
    """Custom type ds0dpDiagState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              8,
              16,
              64,
              65535,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("drop-loop", 16),
          ("errors", 2147483647),
          ("los", 64),
          ("net-loop", 8),
          ("ok", 0),
          ("oos", 65535))
    )


_Ds0dpDiagState_Type.__name__ = "Integer32"
_Ds0dpDiagState_Object = MibTableColumn
ds0dpDiagState = _Ds0dpDiagState_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 6, 2, 1, 1, 3),
    _Ds0dpDiagState_Type()
)
ds0dpDiagState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds0dpDiagState.setStatus("current")
_Ds0dpDiagErrSecs_Type = Counter32
_Ds0dpDiagErrSecs_Object = MibTableColumn
ds0dpDiagErrSecs = _Ds0dpDiagErrSecs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 6, 2, 1, 1, 4),
    _Ds0dpDiagErrSecs_Type()
)
ds0dpDiagErrSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds0dpDiagErrSecs.setStatus("current")


class _Ds0dpDiagDropLoop_Type(Integer32):
    """Custom type ds0dpDiagDropLoop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              40,
              41,
              42,
              43,
              49)
        )
    )
    namedValues = NamedValues(
        *(("csu", 41),
          ("ds0FromDrop", 49),
          ("ds0ToDrop", 42),
          ("local", 43),
          ("ocu", 40),
          ("off", 0))
    )


_Ds0dpDiagDropLoop_Type.__name__ = "Integer32"
_Ds0dpDiagDropLoop_Object = MibTableColumn
ds0dpDiagDropLoop = _Ds0dpDiagDropLoop_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 6, 2, 1, 1, 5),
    _Ds0dpDiagDropLoop_Type()
)
ds0dpDiagDropLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds0dpDiagDropLoop.setStatus("current")


class _Ds0dpDiagNetLoop_Type(Integer32):
    """Custom type ds0dpDiagNetLoop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              44,
              45,
              46,
              47,
              48)
        )
    )
    namedValues = NamedValues(
        *(("csu", 46),
          ("ds0FromNet", 48),
          ("ds0ToNet", 47),
          ("local", 44),
          ("ocu", 45),
          ("off", 5))
    )


_Ds0dpDiagNetLoop_Type.__name__ = "Integer32"
_Ds0dpDiagNetLoop_Object = MibTableColumn
ds0dpDiagNetLoop = _Ds0dpDiagNetLoop_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 6, 2, 1, 1, 6),
    _Ds0dpDiagNetLoop_Type()
)
ds0dpDiagNetLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds0dpDiagNetLoop.setStatus("current")


class _Ds0dpDiagBertState_Type(Integer32):
    """Custom type ds0dpDiagBertState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(51,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100)
        )
    )
    namedValues = NamedValues(
        *(("bertOff", 51),
          ("drop2047", 95),
          ("drop511", 94),
          ("dropAllOnes", 93),
          ("dropQRSS", 96),
          ("net2047", 99),
          ("net511", 98),
          ("netAllOnes", 97),
          ("netQRSS", 100))
    )


_Ds0dpDiagBertState_Type.__name__ = "Integer32"
_Ds0dpDiagBertState_Object = MibTableColumn
ds0dpDiagBertState = _Ds0dpDiagBertState_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 6, 2, 1, 1, 7),
    _Ds0dpDiagBertState_Type()
)
ds0dpDiagBertState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds0dpDiagBertState.setStatus("current")
_Ds0dpDiagTestDuration_Type = Counter32
_Ds0dpDiagTestDuration_Object = MibTableColumn
ds0dpDiagTestDuration = _Ds0dpDiagTestDuration_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 6, 2, 1, 1, 8),
    _Ds0dpDiagTestDuration_Type()
)
ds0dpDiagTestDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds0dpDiagTestDuration.setStatus("current")
_Ds0dpDiagBertErrSecs_Type = Counter32
_Ds0dpDiagBertErrSecs_Object = MibTableColumn
ds0dpDiagBertErrSecs = _Ds0dpDiagBertErrSecs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 6, 2, 1, 1, 9),
    _Ds0dpDiagBertErrSecs_Type()
)
ds0dpDiagBertErrSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds0dpDiagBertErrSecs.setStatus("current")
_Ds0dpDiagBpvErrSecs_Type = Counter32
_Ds0dpDiagBpvErrSecs_Object = MibTableColumn
ds0dpDiagBpvErrSecs = _Ds0dpDiagBpvErrSecs_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 6, 2, 1, 1, 10),
    _Ds0dpDiagBpvErrSecs_Type()
)
ds0dpDiagBpvErrSecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ds0dpDiagBpvErrSecs.setStatus("current")


class _Ds0dpDiagInsErrMode_Type(Integer32):
    """Custom type ds0dpDiagInsErrMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bert-error", 1),
          ("bpv", 2))
    )


_Ds0dpDiagInsErrMode_Type.__name__ = "Integer32"
_Ds0dpDiagInsErrMode_Object = MibTableColumn
ds0dpDiagInsErrMode = _Ds0dpDiagInsErrMode_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 6, 2, 1, 1, 11),
    _Ds0dpDiagInsErrMode_Type()
)
ds0dpDiagInsErrMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds0dpDiagInsErrMode.setStatus("current")


class _Ds0dpDiagCmdStatus_Type(Integer32):
    """Custom type ds0dpDiagCmdStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              14,
              16,
              101,
              114,
              116,
              200,
              201,
              202,
              203,
              205,
              206,
              208,
              500,
              501,
              502)
        )
    )
    namedValues = NamedValues(
        *(("clear-successful", 114),
          ("clearErrors", 14),
          ("err-field-cannot-be-set", 206),
          ("err-general-diag-error", 200),
          ("err-invalid-bert", 203),
          ("err-invalid-command", 208),
          ("err-invalid-loop", 202),
          ("err-invalid-snmp-type", 501),
          ("err-invalid-snmp-var-size", 502),
          ("err-link-out-of-service", 201),
          ("err-snmp-parse-failed", 500),
          ("err-test-in-progress", 205),
          ("insert-successful", 116),
          ("insertError", 16),
          ("ready-for-command", 0),
          ("update", 1),
          ("update-successful", 101))
    )


_Ds0dpDiagCmdStatus_Type.__name__ = "Integer32"
_Ds0dpDiagCmdStatus_Object = MibTableColumn
ds0dpDiagCmdStatus = _Ds0dpDiagCmdStatus_Object(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 6, 2, 1, 1, 12),
    _Ds0dpDiagCmdStatus_Type()
)
ds0dpDiagCmdStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ds0dpDiagCmdStatus.setStatus("current")

# Managed Objects groups


# Notification objects

ds0DpPortConfigTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 6, 0, 1)
)
ds0DpPortConfigTrap.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-DS0-DP-MIB", "ds0DpCfgPortAddr"),
        ("ERI-DNX-DS0-DP-MIB", "ds0DpCfgCmdStatus"))
)
if mibBuilder.loadTexts:
    ds0DpPortConfigTrap.setStatus(
        "current"
    )

ds0DpClockConfigTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 644, 2, 4, 2, 6, 0, 2)
)
ds0DpClockConfigTrap.setObjects(
      *(("ERI-DNX-SMC-MIB", "trapSequence"),
        ("ERI-DNX-DS0-DP-MIB", "ds0DpCompClockAddr"),
        ("ERI-DNX-DS0-DP-MIB", "ds0DpCompClockCmdStatus"))
)
if mibBuilder.loadTexts:
    ds0DpClockConfigTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ERI-DNX-DS0-DP-MIB",
    **{"dnxDS0DP": dnxDS0DP,
       "dnxDS0DPEnterprise": dnxDS0DPEnterprise,
       "ds0DpPortConfigTrap": ds0DpPortConfigTrap,
       "ds0DpClockConfigTrap": ds0DpClockConfigTrap,
       "ds0DpConfig": ds0DpConfig,
       "ds0DpPortConfigTable": ds0DpPortConfigTable,
       "ds0DpPortConfigEntry": ds0DpPortConfigEntry,
       "ds0DpCfgPortAddr": ds0DpCfgPortAddr,
       "ds0DpCfgResource": ds0DpCfgResource,
       "ds0DpCfgPortName": ds0DpCfgPortName,
       "ds0DpCfgStatus": ds0DpCfgStatus,
       "ds0DpCfgRate": ds0DpCfgRate,
       "ds0DpCfgZeroCodeEnf": ds0DpCfgZeroCodeEnf,
       "ds0DpCfgLoopDetect": ds0DpCfgLoopDetect,
       "ds0DpCfgCmdStatus": ds0DpCfgCmdStatus,
       "ds0DpClockConfigTable": ds0DpClockConfigTable,
       "ds0DpClockConfigEntry": ds0DpClockConfigEntry,
       "ds0DpCompClockAddr": ds0DpCompClockAddr,
       "ds0DpCompClockResource": ds0DpCompClockResource,
       "ds0DpCompClockStatus": ds0DpCompClockStatus,
       "ds0DpCompClockCmdStatus": ds0DpCompClockCmdStatus,
       "ds0DpDiag": ds0DpDiag,
       "ds0dpPortDiagTable": ds0dpPortDiagTable,
       "ds0dpPortDiagEntry": ds0dpPortDiagEntry,
       "ds0dpDiagAddr": ds0dpDiagAddr,
       "ds0dpDiagResource": ds0dpDiagResource,
       "ds0dpDiagState": ds0dpDiagState,
       "ds0dpDiagErrSecs": ds0dpDiagErrSecs,
       "ds0dpDiagDropLoop": ds0dpDiagDropLoop,
       "ds0dpDiagNetLoop": ds0dpDiagNetLoop,
       "ds0dpDiagBertState": ds0dpDiagBertState,
       "ds0dpDiagTestDuration": ds0dpDiagTestDuration,
       "ds0dpDiagBertErrSecs": ds0dpDiagBertErrSecs,
       "ds0dpDiagBpvErrSecs": ds0dpDiagBpvErrSecs,
       "ds0dpDiagInsErrMode": ds0dpDiagInsErrMode,
       "ds0dpDiagCmdStatus": ds0dpDiagCmdStatus,
       "eriDNXDs0dpMIB": eriDNXDs0dpMIB}
)
