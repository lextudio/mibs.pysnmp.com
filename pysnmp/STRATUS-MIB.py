# SNMP MIB module (STRATUS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/STRATUS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:58:25 2024
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
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

_Stratus_ObjectIdentity = ObjectIdentity
stratus = _Stratus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 458)
)
_Experimental_ObjectIdentity = ObjectIdentity
experimental = _Experimental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 458, 101)
)
_AgentInfo_ObjectIdentity = ObjectIdentity
agentInfo = _AgentInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 458, 102)
)


class _SraAgentMibFamily_Type(Integer32):
    """Custom type sraAgentMibFamily based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ftServer", 2),
          ("stcp", 1))
    )


_SraAgentMibFamily_Type.__name__ = "Integer32"
_SraAgentMibFamily_Object = MibScalar
sraAgentMibFamily = _SraAgentMibFamily_Object(
    (1, 3, 6, 1, 4, 1, 458, 102, 1),
    _SraAgentMibFamily_Type()
)
sraAgentMibFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sraAgentMibFamily.setStatus("mandatory")


class _SraAgentMibRevision_Type(Integer32):
    """Custom type sraAgentMibRevision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("rev01", 1)
    )


_SraAgentMibRevision_Type.__name__ = "Integer32"
_SraAgentMibRevision_Object = MibScalar
sraAgentMibRevision = _SraAgentMibRevision_Object(
    (1, 3, 6, 1, 4, 1, 458, 102, 2),
    _SraAgentMibRevision_Type()
)
sraAgentMibRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sraAgentMibRevision.setStatus("mandatory")
_SystemInfo_ObjectIdentity = ObjectIdentity
systemInfo = _SystemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 458, 103)
)
_SraSiSystemType_Type = ObjectIdentifier
_SraSiSystemType_Object = MibScalar
sraSiSystemType = _SraSiSystemType_Object(
    (1, 3, 6, 1, 4, 1, 458, 103, 1),
    _SraSiSystemType_Type()
)
sraSiSystemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sraSiSystemType.setStatus("mandatory")
_SraSiManufacturer_Type = DisplayString
_SraSiManufacturer_Object = MibScalar
sraSiManufacturer = _SraSiManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 458, 103, 2),
    _SraSiManufacturer_Type()
)
sraSiManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sraSiManufacturer.setStatus("mandatory")
_SraSiModel_Type = DisplayString
_SraSiModel_Object = MibScalar
sraSiModel = _SraSiModel_Object(
    (1, 3, 6, 1, 4, 1, 458, 103, 3),
    _SraSiModel_Type()
)
sraSiModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sraSiModel.setStatus("mandatory")


class _SraSiOverallSystemStatus_Type(Integer32):
    """Custom type sraSiOverallSystemStatus based on Integer32"""
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
        *(("noFaults", 2),
          ("systemDown", 4),
          ("systemFault", 3),
          ("unsupported", 1))
    )


_SraSiOverallSystemStatus_Type.__name__ = "Integer32"
_SraSiOverallSystemStatus_Object = MibScalar
sraSiOverallSystemStatus = _SraSiOverallSystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 458, 103, 4),
    _SraSiOverallSystemStatus_Type()
)
sraSiOverallSystemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sraSiOverallSystemStatus.setStatus("mandatory")
_SraSiSystemName_Type = DisplayString
_SraSiSystemName_Object = MibScalar
sraSiSystemName = _SraSiSystemName_Object(
    (1, 3, 6, 1, 4, 1, 458, 103, 5),
    _SraSiSystemName_Type()
)
sraSiSystemName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sraSiSystemName.setStatus("mandatory")
_SraSiSystemSerialNumber_Type = DisplayString
_SraSiSystemSerialNumber_Object = MibScalar
sraSiSystemSerialNumber = _SraSiSystemSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 458, 103, 6),
    _SraSiSystemSerialNumber_Type()
)
sraSiSystemSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sraSiSystemSerialNumber.setStatus("mandatory")
_SraSiSiteID_Type = DisplayString
_SraSiSiteID_Object = MibScalar
sraSiSiteID = _SraSiSiteID_Object(
    (1, 3, 6, 1, 4, 1, 458, 103, 7),
    _SraSiSiteID_Type()
)
sraSiSiteID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sraSiSiteID.setStatus("mandatory")


class _SraSiCpuFamily_Type(Integer32):
    """Custom type sraSiCpuFamily based on Integer32"""
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
        *(("hppa", 4),
          ("i860", 3),
          ("ia32", 5),
          ("ia64", 6),
          ("m68k", 2),
          ("unsupported", 1))
    )


_SraSiCpuFamily_Type.__name__ = "Integer32"
_SraSiCpuFamily_Object = MibScalar
sraSiCpuFamily = _SraSiCpuFamily_Object(
    (1, 3, 6, 1, 4, 1, 458, 103, 8),
    _SraSiCpuFamily_Type()
)
sraSiCpuFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sraSiCpuFamily.setStatus("mandatory")


class _SraSiOsType_Type(Integer32):
    """Custom type sraSiOsType based on Integer32"""
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
        *(("ftx", 2),
          ("hpux", 3),
          ("linux", 4),
          ("unsupported", 1),
          ("vos", 5),
          ("windows", 6))
    )


_SraSiOsType_Type.__name__ = "Integer32"
_SraSiOsType_Object = MibScalar
sraSiOsType = _SraSiOsType_Object(
    (1, 3, 6, 1, 4, 1, 458, 103, 9),
    _SraSiOsType_Type()
)
sraSiOsType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sraSiOsType.setStatus("mandatory")
_ProductIdent_ObjectIdentity = ObjectIdentity
productIdent = _ProductIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 458, 104)
)
_OsFTX_ObjectIdentity = ObjectIdentity
osFTX = _OsFTX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 458, 104, 1)
)
_SraProductIdFtxJetta_ObjectIdentity = ObjectIdentity
sraProductIdFtxJetta = _SraProductIdFtxJetta_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 458, 104, 1, 1)
)
_SraProductIdFtxPolo_ObjectIdentity = ObjectIdentity
sraProductIdFtxPolo = _SraProductIdFtxPolo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 458, 104, 1, 2)
)
_OsHPUX_ObjectIdentity = ObjectIdentity
osHPUX = _OsHPUX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 458, 104, 2)
)
_SraProductIdHpuxPolo_ObjectIdentity = ObjectIdentity
sraProductIdHpuxPolo = _SraProductIdHpuxPolo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 458, 104, 2, 1)
)
_OsLinux_ObjectIdentity = ObjectIdentity
osLinux = _OsLinux_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 458, 104, 3)
)
_SraProductIdLnxFtsIa32_ObjectIdentity = ObjectIdentity
sraProductIdLnxFtsIa32 = _SraProductIdLnxFtsIa32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 458, 104, 3, 1)
)
_OsVOS_ObjectIdentity = ObjectIdentity
osVOS = _OsVOS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 458, 104, 4)
)
_SraProductIdVos68k_ObjectIdentity = ObjectIdentity
sraProductIdVos68k = _SraProductIdVos68k_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 458, 104, 4, 1)
)
_SraProductIdVosI860_ObjectIdentity = ObjectIdentity
sraProductIdVosI860 = _SraProductIdVosI860_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 458, 104, 4, 2)
)
_SraProductIdVosJetta_ObjectIdentity = ObjectIdentity
sraProductIdVosJetta = _SraProductIdVosJetta_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 458, 104, 4, 3)
)
_SraProductIdVosIa32_ObjectIdentity = ObjectIdentity
sraProductIdVosIa32 = _SraProductIdVosIa32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 458, 104, 4, 4)
)
_OsWindowsFt_ObjectIdentity = ObjectIdentity
osWindowsFt = _OsWindowsFt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 458, 104, 5)
)
_SraProductIdWinFtsIa32_ObjectIdentity = ObjectIdentity
sraProductIdWinFtsIa32 = _SraProductIdWinFtsIa32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 458, 104, 5, 1)
)
_SraProductIdWinFtsIa64_ObjectIdentity = ObjectIdentity
sraProductIdWinFtsIa64 = _SraProductIdWinFtsIa64_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 458, 104, 5, 2)
)
_OsRadio_ObjectIdentity = ObjectIdentity
osRadio = _OsRadio_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 458, 104, 6)
)
_SraProductIdWinRadIa32_ObjectIdentity = ObjectIdentity
sraProductIdWinRadIa32 = _SraProductIdWinRadIa32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 458, 104, 6, 1)
)
_FtServerOid_ObjectIdentity = ObjectIdentity
ftServerOid = _FtServerOid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 458, 105)
)
_FtsmVar_ObjectIdentity = ObjectIdentity
ftsmVar = _FtsmVar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 458, 105, 1)
)
_FtsmVarHostModelName_Type = DisplayString
_FtsmVarHostModelName_Object = MibScalar
ftsmVarHostModelName = _FtsmVarHostModelName_Object(
    (1, 3, 6, 1, 4, 1, 458, 105, 1, 1),
    _FtsmVarHostModelName_Type()
)
ftsmVarHostModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftsmVarHostModelName.setStatus("mandatory")
_FtsmTrapId_ObjectIdentity = ObjectIdentity
ftsmTrapId = _FtsmTrapId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 458, 105, 2)
)
_FtsmTrapData_ObjectIdentity = ObjectIdentity
ftsmTrapData = _FtsmTrapData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 458, 105, 3)
)


class _FtsmTrapDataDevicePathId_Type(DisplayString):
    """Custom type ftsmTrapDataDevicePathId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_FtsmTrapDataDevicePathId_Type.__name__ = "DisplayString"
_FtsmTrapDataDevicePathId_Object = MibScalar
ftsmTrapDataDevicePathId = _FtsmTrapDataDevicePathId_Object(
    (1, 3, 6, 1, 4, 1, 458, 105, 3, 1),
    _FtsmTrapDataDevicePathId_Type()
)
ftsmTrapDataDevicePathId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftsmTrapDataDevicePathId.setStatus("mandatory")
_FtsmTrapDataDeviceClassname_Type = DisplayString
_FtsmTrapDataDeviceClassname_Object = MibScalar
ftsmTrapDataDeviceClassname = _FtsmTrapDataDeviceClassname_Object(
    (1, 3, 6, 1, 4, 1, 458, 105, 3, 2),
    _FtsmTrapDataDeviceClassname_Type()
)
ftsmTrapDataDeviceClassname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftsmTrapDataDeviceClassname.setStatus("mandatory")


class _FtsmTrapDataNewState_Type(Integer32):
    """Custom type ftsmTrapDataNewState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(65536,
              65560,
              131073,
              131076,
              131078,
              131079,
              131080,
              131081,
              131082,
              131083,
              131084,
              131085,
              131086,
              131087,
              131088,
              262149,
              524308,
              524309,
              1572886,
              1572887,
              2097154,
              2097155)
        )
    )
    namedValues = NamedValues(
        *(("sraFtsm-state-broken", 2097155),
          ("sraFtsm-state-device-ready", 131083),
          ("sraFtsm-state-diagnostics", 262149),
          ("sraFtsm-state-diagnostics-passed", 131078),
          ("sraFtsm-state-dumping", 131076),
          ("sraFtsm-state-duplex", 1572886),
          ("sraFtsm-state-empty", 65536),
          ("sraFtsm-state-firmware-update", 131081),
          ("sraFtsm-state-firmware-update-complete", 131088),
          ("sraFtsm-state-initializing", 131079),
          ("sraFtsm-state-not-present", 65560),
          ("sraFtsm-state-offline", 131082),
          ("sraFtsm-state-online", 524308),
          ("sraFtsm-state-remove-pending", 131086),
          ("sraFtsm-state-removed", 131073),
          ("sraFtsm-state-shot", 2097154),
          ("sraFtsm-state-simplex", 524309),
          ("sraFtsm-state-stop-pending", 131085),
          ("sraFtsm-state-stopped", 131084),
          ("sraFtsm-state-surprise-removal", 131087),
          ("sraFtsm-state-syncing", 131080),
          ("sraFtsm-state-triplex", 1572887))
    )


_FtsmTrapDataNewState_Type.__name__ = "Integer32"
_FtsmTrapDataNewState_Object = MibScalar
ftsmTrapDataNewState = _FtsmTrapDataNewState_Object(
    (1, 3, 6, 1, 4, 1, 458, 105, 3, 3),
    _FtsmTrapDataNewState_Type()
)
ftsmTrapDataNewState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftsmTrapDataNewState.setStatus("mandatory")


class _FtsmTrapDataNewReason_Type(Integer32):
    """Custom type ftsmTrapDataNewReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("sraFtsm-reason-autoburn-disabled", 12),
          ("sraFtsm-reason-below-mtbf", 1),
          ("sraFtsm-reason-bringup-failed", 5),
          ("sraFtsm-reason-deferred-bringup", 17),
          ("sraFtsm-reason-diagnostics-failed", 2),
          ("sraFtsm-reason-firmware-burn-fail", 8),
          ("sraFtsm-reason-firmware-file-error", 10),
          ("sraFtsm-reason-firmware-file-not-found", 9),
          ("sraFtsm-reason-firmware-prom-error", 11),
          ("sraFtsm-reason-hardware-incompatible", 3),
          ("sraFtsm-reason-holding-dump", 4),
          ("sraFtsm-reason-idprom-read-error", 13),
          ("sraFtsm-reason-media-disconnect", 7),
          ("sraFtsm-reason-none", 0),
          ("sraFtsm-reason-parent-broken", 6),
          ("sraFtsm-reason-parent-empty", 16),
          ("sraFtsm-reason-primary", 14),
          ("sraFtsm-reason-secondary", 15))
    )


_FtsmTrapDataNewReason_Type.__name__ = "Integer32"
_FtsmTrapDataNewReason_Object = MibScalar
ftsmTrapDataNewReason = _FtsmTrapDataNewReason_Object(
    (1, 3, 6, 1, 4, 1, 458, 105, 3, 4),
    _FtsmTrapDataNewReason_Type()
)
ftsmTrapDataNewReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftsmTrapDataNewReason.setStatus("mandatory")


class _FtsmTrapDataNewThreshold_Type(Integer32):
    """Custom type ftsmTrapDataNewThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("sraFtsm-sensor-status-above-critical", 5),
          ("sraFtsm-sensor-status-above-fatal", 7),
          ("sraFtsm-sensor-status-above-warning", 4),
          ("sraFtsm-sensor-status-below-critical", 3),
          ("sraFtsm-sensor-status-below-fatal", 6),
          ("sraFtsm-sensor-status-below-warning", 2),
          ("sraFtsm-sensor-status-normal", 1),
          ("sraFtsm-sensor-status-unavailable", 0))
    )


_FtsmTrapDataNewThreshold_Type.__name__ = "Integer32"
_FtsmTrapDataNewThreshold_Object = MibScalar
ftsmTrapDataNewThreshold = _FtsmTrapDataNewThreshold_Object(
    (1, 3, 6, 1, 4, 1, 458, 105, 3, 5),
    _FtsmTrapDataNewThreshold_Type()
)
ftsmTrapDataNewThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftsmTrapDataNewThreshold.setStatus("mandatory")
_FtsmTrapDataEventId_Type = Integer32
_FtsmTrapDataEventId_Object = MibScalar
ftsmTrapDataEventId = _FtsmTrapDataEventId_Object(
    (1, 3, 6, 1, 4, 1, 458, 105, 3, 6),
    _FtsmTrapDataEventId_Type()
)
ftsmTrapDataEventId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftsmTrapDataEventId.setStatus("mandatory")
_FtsmTrapDataAlarmId_Type = Integer32
_FtsmTrapDataAlarmId_Object = MibScalar
ftsmTrapDataAlarmId = _FtsmTrapDataAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 458, 105, 3, 7),
    _FtsmTrapDataAlarmId_Type()
)
ftsmTrapDataAlarmId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftsmTrapDataAlarmId.setStatus("mandatory")
_FtsmTrapDataEventDescription_Type = DisplayString
_FtsmTrapDataEventDescription_Object = MibScalar
ftsmTrapDataEventDescription = _FtsmTrapDataEventDescription_Object(
    (1, 3, 6, 1, 4, 1, 458, 105, 3, 8),
    _FtsmTrapDataEventDescription_Type()
)
ftsmTrapDataEventDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftsmTrapDataEventDescription.setStatus("mandatory")
_FtsmTrapDataEventParameterStrings_ObjectIdentity = ObjectIdentity
ftsmTrapDataEventParameterStrings = _FtsmTrapDataEventParameterStrings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 458, 105, 3, 9)
)
_FtsmTrapDataEventP1_Type = DisplayString
_FtsmTrapDataEventP1_Object = MibScalar
ftsmTrapDataEventP1 = _FtsmTrapDataEventP1_Object(
    (1, 3, 6, 1, 4, 1, 458, 105, 3, 9, 1),
    _FtsmTrapDataEventP1_Type()
)
ftsmTrapDataEventP1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftsmTrapDataEventP1.setStatus("mandatory")
_FtsmTrapDataEventP2_Type = DisplayString
_FtsmTrapDataEventP2_Object = MibScalar
ftsmTrapDataEventP2 = _FtsmTrapDataEventP2_Object(
    (1, 3, 6, 1, 4, 1, 458, 105, 3, 9, 2),
    _FtsmTrapDataEventP2_Type()
)
ftsmTrapDataEventP2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftsmTrapDataEventP2.setStatus("mandatory")
_FtsmTrapDataEventP3_Type = DisplayString
_FtsmTrapDataEventP3_Object = MibScalar
ftsmTrapDataEventP3 = _FtsmTrapDataEventP3_Object(
    (1, 3, 6, 1, 4, 1, 458, 105, 3, 9, 3),
    _FtsmTrapDataEventP3_Type()
)
ftsmTrapDataEventP3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftsmTrapDataEventP3.setStatus("mandatory")
_FtsmTrapDataEventP4_Type = DisplayString
_FtsmTrapDataEventP4_Object = MibScalar
ftsmTrapDataEventP4 = _FtsmTrapDataEventP4_Object(
    (1, 3, 6, 1, 4, 1, 458, 105, 3, 9, 4),
    _FtsmTrapDataEventP4_Type()
)
ftsmTrapDataEventP4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftsmTrapDataEventP4.setStatus("mandatory")
_FtsmTrapDataEventP5_Type = DisplayString
_FtsmTrapDataEventP5_Object = MibScalar
ftsmTrapDataEventP5 = _FtsmTrapDataEventP5_Object(
    (1, 3, 6, 1, 4, 1, 458, 105, 3, 9, 5),
    _FtsmTrapDataEventP5_Type()
)
ftsmTrapDataEventP5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftsmTrapDataEventP5.setStatus("mandatory")
_FtsmTrapDataEventP6_Type = DisplayString
_FtsmTrapDataEventP6_Object = MibScalar
ftsmTrapDataEventP6 = _FtsmTrapDataEventP6_Object(
    (1, 3, 6, 1, 4, 1, 458, 105, 3, 9, 6),
    _FtsmTrapDataEventP6_Type()
)
ftsmTrapDataEventP6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftsmTrapDataEventP6.setStatus("mandatory")
_FtsmTrapDataEventP7_Type = DisplayString
_FtsmTrapDataEventP7_Object = MibScalar
ftsmTrapDataEventP7 = _FtsmTrapDataEventP7_Object(
    (1, 3, 6, 1, 4, 1, 458, 105, 3, 9, 7),
    _FtsmTrapDataEventP7_Type()
)
ftsmTrapDataEventP7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftsmTrapDataEventP7.setStatus("mandatory")
_FtsmTrapDataEventP8_Type = DisplayString
_FtsmTrapDataEventP8_Object = MibScalar
ftsmTrapDataEventP8 = _FtsmTrapDataEventP8_Object(
    (1, 3, 6, 1, 4, 1, 458, 105, 3, 9, 8),
    _FtsmTrapDataEventP8_Type()
)
ftsmTrapDataEventP8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftsmTrapDataEventP8.setStatus("mandatory")
_FtsmTrapDataEventP9_Type = DisplayString
_FtsmTrapDataEventP9_Object = MibScalar
ftsmTrapDataEventP9 = _FtsmTrapDataEventP9_Object(
    (1, 3, 6, 1, 4, 1, 458, 105, 3, 9, 9),
    _FtsmTrapDataEventP9_Type()
)
ftsmTrapDataEventP9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftsmTrapDataEventP9.setStatus("mandatory")
_StcpOid_ObjectIdentity = ObjectIdentity
stcpOid = _StcpOid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 458, 106)
)

# Managed Objects groups


# Notification objects

ftsmTrapEnterBrokenState = NotificationType(
    (1, 3, 6, 1, 4, 1, 458, 105, 2, 0, 101)
)
ftsmTrapEnterBrokenState.setObjects(
      *(("STRATUS-MIB", "ftsmTrapDataDevicePathId"),
        ("STRATUS-MIB", "ftsmTrapDataDeviceClassname"),
        ("STRATUS-MIB", "ftsmTrapDataNewState"),
        ("STRATUS-MIB", "ftsmTrapDataNewReason"))
)
if mibBuilder.loadTexts:
    ftsmTrapEnterBrokenState.setStatus(
        ""
    )

ftsmTrapLeaveBrokenState = NotificationType(
    (1, 3, 6, 1, 4, 1, 458, 105, 2, 0, 102)
)
ftsmTrapLeaveBrokenState.setObjects(
      *(("STRATUS-MIB", "ftsmTrapDataDevicePathId"),
        ("STRATUS-MIB", "ftsmTrapDataDeviceClassname"),
        ("STRATUS-MIB", "ftsmTrapDataNewState"),
        ("STRATUS-MIB", "ftsmTrapDataNewReason"))
)
if mibBuilder.loadTexts:
    ftsmTrapLeaveBrokenState.setStatus(
        ""
    )

ftsmTrapEnterOnlineState = NotificationType(
    (1, 3, 6, 1, 4, 1, 458, 105, 2, 0, 103)
)
ftsmTrapEnterOnlineState.setObjects(
      *(("STRATUS-MIB", "ftsmTrapDataDevicePathId"),
        ("STRATUS-MIB", "ftsmTrapDataDeviceClassname"),
        ("STRATUS-MIB", "ftsmTrapDataNewState"),
        ("STRATUS-MIB", "ftsmTrapDataNewReason"))
)
if mibBuilder.loadTexts:
    ftsmTrapEnterOnlineState.setStatus(
        ""
    )

ftsmTrapLeaveOnlineState = NotificationType(
    (1, 3, 6, 1, 4, 1, 458, 105, 2, 0, 104)
)
ftsmTrapLeaveOnlineState.setObjects(
      *(("STRATUS-MIB", "ftsmTrapDataDevicePathId"),
        ("STRATUS-MIB", "ftsmTrapDataDeviceClassname"),
        ("STRATUS-MIB", "ftsmTrapDataNewState"),
        ("STRATUS-MIB", "ftsmTrapDataNewReason"))
)
if mibBuilder.loadTexts:
    ftsmTrapLeaveOnlineState.setStatus(
        ""
    )

ftsmTrapEnterOutOfServiceState = NotificationType(
    (1, 3, 6, 1, 4, 1, 458, 105, 2, 0, 105)
)
ftsmTrapEnterOutOfServiceState.setObjects(
      *(("STRATUS-MIB", "ftsmTrapDataDevicePathId"),
        ("STRATUS-MIB", "ftsmTrapDataDeviceClassname"),
        ("STRATUS-MIB", "ftsmTrapDataNewState"),
        ("STRATUS-MIB", "ftsmTrapDataNewReason"))
)
if mibBuilder.loadTexts:
    ftsmTrapEnterOutOfServiceState.setStatus(
        ""
    )

ftsmTrapLeaveOutOfServiceState = NotificationType(
    (1, 3, 6, 1, 4, 1, 458, 105, 2, 0, 106)
)
ftsmTrapLeaveOutOfServiceState.setObjects(
      *(("STRATUS-MIB", "ftsmTrapDataDevicePathId"),
        ("STRATUS-MIB", "ftsmTrapDataDeviceClassname"),
        ("STRATUS-MIB", "ftsmTrapDataNewState"),
        ("STRATUS-MIB", "ftsmTrapDataNewReason"))
)
if mibBuilder.loadTexts:
    ftsmTrapLeaveOutOfServiceState.setStatus(
        ""
    )

ftsmTrapImprove2Normal = NotificationType(
    (1, 3, 6, 1, 4, 1, 458, 105, 2, 0, 201)
)
ftsmTrapImprove2Normal.setObjects(
      *(("STRATUS-MIB", "ftsmTrapDataDevicePathId"),
        ("STRATUS-MIB", "ftsmTrapDataDeviceClassname"),
        ("STRATUS-MIB", "ftsmTrapDataNewState"),
        ("STRATUS-MIB", "ftsmTrapDataNewReason"),
        ("STRATUS-MIB", "ftsmTrapDataNewThreshold"))
)
if mibBuilder.loadTexts:
    ftsmTrapImprove2Normal.setStatus(
        ""
    )

ftsmTrapImprove2Warning = NotificationType(
    (1, 3, 6, 1, 4, 1, 458, 105, 2, 0, 202)
)
ftsmTrapImprove2Warning.setObjects(
      *(("STRATUS-MIB", "ftsmTrapDataDevicePathId"),
        ("STRATUS-MIB", "ftsmTrapDataDeviceClassname"),
        ("STRATUS-MIB", "ftsmTrapDataNewState"),
        ("STRATUS-MIB", "ftsmTrapDataNewReason"),
        ("STRATUS-MIB", "ftsmTrapDataNewThreshold"))
)
if mibBuilder.loadTexts:
    ftsmTrapImprove2Warning.setStatus(
        ""
    )

ftsmTrapImprove2Critical = NotificationType(
    (1, 3, 6, 1, 4, 1, 458, 105, 2, 0, 203)
)
ftsmTrapImprove2Critical.setObjects(
      *(("STRATUS-MIB", "ftsmTrapDataDevicePathId"),
        ("STRATUS-MIB", "ftsmTrapDataDeviceClassname"),
        ("STRATUS-MIB", "ftsmTrapDataNewState"),
        ("STRATUS-MIB", "ftsmTrapDataNewReason"),
        ("STRATUS-MIB", "ftsmTrapDataNewThreshold"))
)
if mibBuilder.loadTexts:
    ftsmTrapImprove2Critical.setStatus(
        ""
    )

ftsmTrapUnavailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 458, 105, 2, 0, 204)
)
ftsmTrapUnavailable.setObjects(
      *(("STRATUS-MIB", "ftsmTrapDataDevicePathId"),
        ("STRATUS-MIB", "ftsmTrapDataDeviceClassname"),
        ("STRATUS-MIB", "ftsmTrapDataNewState"),
        ("STRATUS-MIB", "ftsmTrapDataNewReason"),
        ("STRATUS-MIB", "ftsmTrapDataNewThreshold"))
)
if mibBuilder.loadTexts:
    ftsmTrapUnavailable.setStatus(
        ""
    )

ftsmTrapWorse2Fatal = NotificationType(
    (1, 3, 6, 1, 4, 1, 458, 105, 2, 0, 205)
)
ftsmTrapWorse2Fatal.setObjects(
      *(("STRATUS-MIB", "ftsmTrapDataDevicePathId"),
        ("STRATUS-MIB", "ftsmTrapDataDeviceClassname"),
        ("STRATUS-MIB", "ftsmTrapDataNewState"),
        ("STRATUS-MIB", "ftsmTrapDataNewReason"),
        ("STRATUS-MIB", "ftsmTrapDataNewThreshold"))
)
if mibBuilder.loadTexts:
    ftsmTrapWorse2Fatal.setStatus(
        ""
    )

ftsmTrapWorse2Critical = NotificationType(
    (1, 3, 6, 1, 4, 1, 458, 105, 2, 0, 206)
)
ftsmTrapWorse2Critical.setObjects(
      *(("STRATUS-MIB", "ftsmTrapDataDevicePathId"),
        ("STRATUS-MIB", "ftsmTrapDataDeviceClassname"),
        ("STRATUS-MIB", "ftsmTrapDataNewState"),
        ("STRATUS-MIB", "ftsmTrapDataNewReason"),
        ("STRATUS-MIB", "ftsmTrapDataNewThreshold"))
)
if mibBuilder.loadTexts:
    ftsmTrapWorse2Critical.setStatus(
        ""
    )

ftsmTrapWorse2Warning = NotificationType(
    (1, 3, 6, 1, 4, 1, 458, 105, 2, 0, 207)
)
ftsmTrapWorse2Warning.setObjects(
      *(("STRATUS-MIB", "ftsmTrapDataDevicePathId"),
        ("STRATUS-MIB", "ftsmTrapDataDeviceClassname"),
        ("STRATUS-MIB", "ftsmTrapDataNewState"),
        ("STRATUS-MIB", "ftsmTrapDataNewReason"),
        ("STRATUS-MIB", "ftsmTrapDataNewThreshold"))
)
if mibBuilder.loadTexts:
    ftsmTrapWorse2Warning.setStatus(
        ""
    )

ftsmTrapMgmtServiceFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 458, 105, 2, 0, 301)
)
ftsmTrapMgmtServiceFailure.setObjects(
      *(("STRATUS-MIB", "ftsmTrapDataEventId"),
        ("STRATUS-MIB", "ftsmTrapDataAlarmId"),
        ("STRATUS-MIB", "ftsmTrapDataEventDescription"))
)
if mibBuilder.loadTexts:
    ftsmTrapMgmtServiceFailure.setStatus(
        ""
    )

ftsmTrapUnsentAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 458, 105, 2, 0, 302)
)
ftsmTrapUnsentAlarm.setObjects(
      *(("STRATUS-MIB", "ftsmTrapDataEventId"),
        ("STRATUS-MIB", "ftsmTrapDataAlarmId"),
        ("STRATUS-MIB", "ftsmTrapDataEventDescription"))
)
if mibBuilder.loadTexts:
    ftsmTrapUnsentAlarm.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "STRATUS-MIB",
    **{"stratus": stratus,
       "experimental": experimental,
       "agentInfo": agentInfo,
       "sraAgentMibFamily": sraAgentMibFamily,
       "sraAgentMibRevision": sraAgentMibRevision,
       "systemInfo": systemInfo,
       "sraSiSystemType": sraSiSystemType,
       "sraSiManufacturer": sraSiManufacturer,
       "sraSiModel": sraSiModel,
       "sraSiOverallSystemStatus": sraSiOverallSystemStatus,
       "sraSiSystemName": sraSiSystemName,
       "sraSiSystemSerialNumber": sraSiSystemSerialNumber,
       "sraSiSiteID": sraSiSiteID,
       "sraSiCpuFamily": sraSiCpuFamily,
       "sraSiOsType": sraSiOsType,
       "productIdent": productIdent,
       "osFTX": osFTX,
       "sraProductIdFtxJetta": sraProductIdFtxJetta,
       "sraProductIdFtxPolo": sraProductIdFtxPolo,
       "osHPUX": osHPUX,
       "sraProductIdHpuxPolo": sraProductIdHpuxPolo,
       "osLinux": osLinux,
       "sraProductIdLnxFtsIa32": sraProductIdLnxFtsIa32,
       "osVOS": osVOS,
       "sraProductIdVos68k": sraProductIdVos68k,
       "sraProductIdVosI860": sraProductIdVosI860,
       "sraProductIdVosJetta": sraProductIdVosJetta,
       "sraProductIdVosIa32": sraProductIdVosIa32,
       "osWindowsFt": osWindowsFt,
       "sraProductIdWinFtsIa32": sraProductIdWinFtsIa32,
       "sraProductIdWinFtsIa64": sraProductIdWinFtsIa64,
       "osRadio": osRadio,
       "sraProductIdWinRadIa32": sraProductIdWinRadIa32,
       "ftServerOid": ftServerOid,
       "ftsmVar": ftsmVar,
       "ftsmVarHostModelName": ftsmVarHostModelName,
       "ftsmTrapId": ftsmTrapId,
       "ftsmTrapEnterBrokenState": ftsmTrapEnterBrokenState,
       "ftsmTrapLeaveBrokenState": ftsmTrapLeaveBrokenState,
       "ftsmTrapEnterOnlineState": ftsmTrapEnterOnlineState,
       "ftsmTrapLeaveOnlineState": ftsmTrapLeaveOnlineState,
       "ftsmTrapEnterOutOfServiceState": ftsmTrapEnterOutOfServiceState,
       "ftsmTrapLeaveOutOfServiceState": ftsmTrapLeaveOutOfServiceState,
       "ftsmTrapImprove2Normal": ftsmTrapImprove2Normal,
       "ftsmTrapImprove2Warning": ftsmTrapImprove2Warning,
       "ftsmTrapImprove2Critical": ftsmTrapImprove2Critical,
       "ftsmTrapUnavailable": ftsmTrapUnavailable,
       "ftsmTrapWorse2Fatal": ftsmTrapWorse2Fatal,
       "ftsmTrapWorse2Critical": ftsmTrapWorse2Critical,
       "ftsmTrapWorse2Warning": ftsmTrapWorse2Warning,
       "ftsmTrapMgmtServiceFailure": ftsmTrapMgmtServiceFailure,
       "ftsmTrapUnsentAlarm": ftsmTrapUnsentAlarm,
       "ftsmTrapData": ftsmTrapData,
       "ftsmTrapDataDevicePathId": ftsmTrapDataDevicePathId,
       "ftsmTrapDataDeviceClassname": ftsmTrapDataDeviceClassname,
       "ftsmTrapDataNewState": ftsmTrapDataNewState,
       "ftsmTrapDataNewReason": ftsmTrapDataNewReason,
       "ftsmTrapDataNewThreshold": ftsmTrapDataNewThreshold,
       "ftsmTrapDataEventId": ftsmTrapDataEventId,
       "ftsmTrapDataAlarmId": ftsmTrapDataAlarmId,
       "ftsmTrapDataEventDescription": ftsmTrapDataEventDescription,
       "ftsmTrapDataEventParameterStrings": ftsmTrapDataEventParameterStrings,
       "ftsmTrapDataEventP1": ftsmTrapDataEventP1,
       "ftsmTrapDataEventP2": ftsmTrapDataEventP2,
       "ftsmTrapDataEventP3": ftsmTrapDataEventP3,
       "ftsmTrapDataEventP4": ftsmTrapDataEventP4,
       "ftsmTrapDataEventP5": ftsmTrapDataEventP5,
       "ftsmTrapDataEventP6": ftsmTrapDataEventP6,
       "ftsmTrapDataEventP7": ftsmTrapDataEventP7,
       "ftsmTrapDataEventP8": ftsmTrapDataEventP8,
       "ftsmTrapDataEventP9": ftsmTrapDataEventP9,
       "stcpOid": stcpOid}
)
