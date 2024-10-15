# SNMP MIB module (CA-W2KOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CA-W2KOS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:51:57 2024
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

_Cai_ObjectIdentity = ObjectIdentity
cai = _Cai_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791)
)
_CaiSysMgr_ObjectIdentity = ObjectIdentity
caiSysMgr = _CaiSysMgr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2)
)
_Tng_ObjectIdentity = ObjectIdentity
tng = _Tng_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 10)
)
_Agents_ObjectIdentity = ObjectIdentity
agents = _Agents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2)
)
_CaiW2kOs_ObjectIdentity = ObjectIdentity
caiW2kOs = _CaiW2kOs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43)
)
_W2kConfigGroup_ObjectIdentity = ObjectIdentity
w2kConfigGroup = _W2kConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1)
)
_W2kConfigGeneralGroup_ObjectIdentity = ObjectIdentity
w2kConfigGeneralGroup = _W2kConfigGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 1)
)
_W2kConfigGeneralAgentVersion_Type = DisplayString
_W2kConfigGeneralAgentVersion_Object = MibScalar
w2kConfigGeneralAgentVersion = _W2kConfigGeneralAgentVersion_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 1, 1),
    _W2kConfigGeneralAgentVersion_Type()
)
w2kConfigGeneralAgentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kConfigGeneralAgentVersion.setStatus("mandatory")
_W2kConfigGeneralColdStartTime_Type = DisplayString
_W2kConfigGeneralColdStartTime_Object = MibScalar
w2kConfigGeneralColdStartTime = _W2kConfigGeneralColdStartTime_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 1, 2),
    _W2kConfigGeneralColdStartTime_Type()
)
w2kConfigGeneralColdStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kConfigGeneralColdStartTime.setStatus("mandatory")
_W2kConfigGeneralWarmStartTime_Type = DisplayString
_W2kConfigGeneralWarmStartTime_Object = MibScalar
w2kConfigGeneralWarmStartTime = _W2kConfigGeneralWarmStartTime_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 1, 3),
    _W2kConfigGeneralWarmStartTime_Type()
)
w2kConfigGeneralWarmStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kConfigGeneralWarmStartTime.setStatus("mandatory")
_W2kConfigGeneralCpuPollTime_Type = DisplayString
_W2kConfigGeneralCpuPollTime_Object = MibScalar
w2kConfigGeneralCpuPollTime = _W2kConfigGeneralCpuPollTime_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 1, 4),
    _W2kConfigGeneralCpuPollTime_Type()
)
w2kConfigGeneralCpuPollTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kConfigGeneralCpuPollTime.setStatus("mandatory")
_W2kConfigGeneralMemPollTime_Type = DisplayString
_W2kConfigGeneralMemPollTime_Object = MibScalar
w2kConfigGeneralMemPollTime = _W2kConfigGeneralMemPollTime_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 1, 5),
    _W2kConfigGeneralMemPollTime_Type()
)
w2kConfigGeneralMemPollTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kConfigGeneralMemPollTime.setStatus("mandatory")
_W2kConfigGeneralLVolPollTime_Type = DisplayString
_W2kConfigGeneralLVolPollTime_Object = MibScalar
w2kConfigGeneralLVolPollTime = _W2kConfigGeneralLVolPollTime_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 1, 6),
    _W2kConfigGeneralLVolPollTime_Type()
)
w2kConfigGeneralLVolPollTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kConfigGeneralLVolPollTime.setStatus("mandatory")
_W2kConfigGeneralMntPollTime_Type = DisplayString
_W2kConfigGeneralMntPollTime_Object = MibScalar
w2kConfigGeneralMntPollTime = _W2kConfigGeneralMntPollTime_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 1, 7),
    _W2kConfigGeneralMntPollTime_Type()
)
w2kConfigGeneralMntPollTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kConfigGeneralMntPollTime.setStatus("mandatory")
_W2kConfigGeneralDfsPollTime_Type = DisplayString
_W2kConfigGeneralDfsPollTime_Object = MibScalar
w2kConfigGeneralDfsPollTime = _W2kConfigGeneralDfsPollTime_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 1, 8),
    _W2kConfigGeneralDfsPollTime_Type()
)
w2kConfigGeneralDfsPollTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kConfigGeneralDfsPollTime.setStatus("mandatory")
_W2kConfigGeneralQuotPollTime_Type = DisplayString
_W2kConfigGeneralQuotPollTime_Object = MibScalar
w2kConfigGeneralQuotPollTime = _W2kConfigGeneralQuotPollTime_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 1, 9),
    _W2kConfigGeneralQuotPollTime_Type()
)
w2kConfigGeneralQuotPollTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kConfigGeneralQuotPollTime.setStatus("mandatory")
_W2kConfigGeneralDirPollTime_Type = DisplayString
_W2kConfigGeneralDirPollTime_Object = MibScalar
w2kConfigGeneralDirPollTime = _W2kConfigGeneralDirPollTime_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 1, 10),
    _W2kConfigGeneralDirPollTime_Type()
)
w2kConfigGeneralDirPollTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kConfigGeneralDirPollTime.setStatus("mandatory")
_W2kConfigGeneralFilePollTime_Type = DisplayString
_W2kConfigGeneralFilePollTime_Object = MibScalar
w2kConfigGeneralFilePollTime = _W2kConfigGeneralFilePollTime_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 1, 11),
    _W2kConfigGeneralFilePollTime_Type()
)
w2kConfigGeneralFilePollTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kConfigGeneralFilePollTime.setStatus("mandatory")
_W2kConfigGeneralProcPollTime_Type = DisplayString
_W2kConfigGeneralProcPollTime_Object = MibScalar
w2kConfigGeneralProcPollTime = _W2kConfigGeneralProcPollTime_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 1, 12),
    _W2kConfigGeneralProcPollTime_Type()
)
w2kConfigGeneralProcPollTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kConfigGeneralProcPollTime.setStatus("mandatory")
_W2kConfigGeneralSrvcPollTime_Type = DisplayString
_W2kConfigGeneralSrvcPollTime_Object = MibScalar
w2kConfigGeneralSrvcPollTime = _W2kConfigGeneralSrvcPollTime_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 1, 13),
    _W2kConfigGeneralSrvcPollTime_Type()
)
w2kConfigGeneralSrvcPollTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kConfigGeneralSrvcPollTime.setStatus("mandatory")
_W2kConfigGeneralJobPollTime_Type = DisplayString
_W2kConfigGeneralJobPollTime_Object = MibScalar
w2kConfigGeneralJobPollTime = _W2kConfigGeneralJobPollTime_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 1, 14),
    _W2kConfigGeneralJobPollTime_Type()
)
w2kConfigGeneralJobPollTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kConfigGeneralJobPollTime.setStatus("mandatory")
_W2kConfigGeneralSessPollTime_Type = DisplayString
_W2kConfigGeneralSessPollTime_Object = MibScalar
w2kConfigGeneralSessPollTime = _W2kConfigGeneralSessPollTime_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 1, 15),
    _W2kConfigGeneralSessPollTime_Type()
)
w2kConfigGeneralSessPollTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kConfigGeneralSessPollTime.setStatus("mandatory")
_W2kConfigGeneralPrnPollTime_Type = DisplayString
_W2kConfigGeneralPrnPollTime_Object = MibScalar
w2kConfigGeneralPrnPollTime = _W2kConfigGeneralPrnPollTime_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 1, 16),
    _W2kConfigGeneralPrnPollTime_Type()
)
w2kConfigGeneralPrnPollTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kConfigGeneralPrnPollTime.setStatus("mandatory")
_W2kConfigGeneralNetPollTime_Type = DisplayString
_W2kConfigGeneralNetPollTime_Object = MibScalar
w2kConfigGeneralNetPollTime = _W2kConfigGeneralNetPollTime_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 1, 17),
    _W2kConfigGeneralNetPollTime_Type()
)
w2kConfigGeneralNetPollTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kConfigGeneralNetPollTime.setStatus("mandatory")
_W2kConfigGeneralRegPollTime_Type = DisplayString
_W2kConfigGeneralRegPollTime_Object = MibScalar
w2kConfigGeneralRegPollTime = _W2kConfigGeneralRegPollTime_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 1, 18),
    _W2kConfigGeneralRegPollTime_Type()
)
w2kConfigGeneralRegPollTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kConfigGeneralRegPollTime.setStatus("mandatory")
_W2kConfigSysGroup_ObjectIdentity = ObjectIdentity
w2kConfigSysGroup = _W2kConfigSysGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 2)
)
_W2kConfigSysNodeName_Type = DisplayString
_W2kConfigSysNodeName_Object = MibScalar
w2kConfigSysNodeName = _W2kConfigSysNodeName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 2, 1),
    _W2kConfigSysNodeName_Type()
)
w2kConfigSysNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kConfigSysNodeName.setStatus("mandatory")
_W2kConfigSysVersion_Type = DisplayString
_W2kConfigSysVersion_Object = MibScalar
w2kConfigSysVersion = _W2kConfigSysVersion_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 2, 2),
    _W2kConfigSysVersion_Type()
)
w2kConfigSysVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kConfigSysVersion.setStatus("mandatory")
_W2kConfigSysBios_Type = DisplayString
_W2kConfigSysBios_Object = MibScalar
w2kConfigSysBios = _W2kConfigSysBios_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 2, 3),
    _W2kConfigSysBios_Type()
)
w2kConfigSysBios.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kConfigSysBios.setStatus("mandatory")
_W2kConfigSysColdStartTime_Type = DisplayString
_W2kConfigSysColdStartTime_Object = MibScalar
w2kConfigSysColdStartTime = _W2kConfigSysColdStartTime_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 2, 4),
    _W2kConfigSysColdStartTime_Type()
)
w2kConfigSysColdStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kConfigSysColdStartTime.setStatus("mandatory")
_W2kConfigCpuGroup_ObjectIdentity = ObjectIdentity
w2kConfigCpuGroup = _W2kConfigCpuGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 3)
)


class _W2kConfigCpuPollInterval_Type(Integer32):
    """Custom type w2kConfigCpuPollInterval based on Integer32"""
    defaultValue = 120


_W2kConfigCpuPollInterval_Object = MibScalar
w2kConfigCpuPollInterval = _W2kConfigCpuPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 3, 1),
    _W2kConfigCpuPollInterval_Type()
)
w2kConfigCpuPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigCpuPollInterval.setStatus("mandatory")


class _W2kConfigCpuPollMethod_Type(Integer32):
    """Custom type w2kConfigCpuPollMethod based on Integer32"""
    defaultValue = 2

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
        *(("disabled", 1),
          ("poll-interval-and-query", 3),
          ("poll-interval-only", 2),
          ("query-only", 4))
    )


_W2kConfigCpuPollMethod_Type.__name__ = "Integer32"
_W2kConfigCpuPollMethod_Object = MibScalar
w2kConfigCpuPollMethod = _W2kConfigCpuPollMethod_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 3, 2),
    _W2kConfigCpuPollMethod_Type()
)
w2kConfigCpuPollMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigCpuPollMethod.setStatus("mandatory")


class _W2kConfigCpuLoadLag_Type(Integer32):
    """Custom type w2kConfigCpuLoadLag based on Integer32"""
    defaultValue = 3


_W2kConfigCpuLoadLag_Object = MibScalar
w2kConfigCpuLoadLag = _W2kConfigCpuLoadLag_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 3, 3),
    _W2kConfigCpuLoadLag_Type()
)
w2kConfigCpuLoadLag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigCpuLoadLag.setStatus("mandatory")


class _W2kConfigCpuLoadWarn_Type(Integer32):
    """Custom type w2kConfigCpuLoadWarn based on Integer32"""
    defaultValue = 70


_W2kConfigCpuLoadWarn_Object = MibScalar
w2kConfigCpuLoadWarn = _W2kConfigCpuLoadWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 3, 4),
    _W2kConfigCpuLoadWarn_Type()
)
w2kConfigCpuLoadWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigCpuLoadWarn.setStatus("mandatory")


class _W2kConfigCpuLoadCrit_Type(Integer32):
    """Custom type w2kConfigCpuLoadCrit based on Integer32"""
    defaultValue = 90


_W2kConfigCpuLoadCrit_Object = MibScalar
w2kConfigCpuLoadCrit = _W2kConfigCpuLoadCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 3, 5),
    _W2kConfigCpuLoadCrit_Type()
)
w2kConfigCpuLoadCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigCpuLoadCrit.setStatus("mandatory")


class _W2kConfigCpuLoadMonitor_Type(Integer32):
    """Custom type w2kConfigCpuLoadMonitor based on Integer32"""
    defaultValue = 4

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
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_W2kConfigCpuLoadMonitor_Type.__name__ = "Integer32"
_W2kConfigCpuLoadMonitor_Object = MibScalar
w2kConfigCpuLoadMonitor = _W2kConfigCpuLoadMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 3, 6),
    _W2kConfigCpuLoadMonitor_Type()
)
w2kConfigCpuLoadMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigCpuLoadMonitor.setStatus("mandatory")


class _W2kConfigCpuLossAction_Type(Integer32):
    """Custom type w2kConfigCpuLossAction based on Integer32"""
    defaultValue = 1

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
        *(("down-critical", 4),
          ("down-warning", 3),
          ("remove", 1),
          ("up", 2))
    )


_W2kConfigCpuLossAction_Type.__name__ = "Integer32"
_W2kConfigCpuLossAction_Object = MibScalar
w2kConfigCpuLossAction = _W2kConfigCpuLossAction_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 3, 7),
    _W2kConfigCpuLossAction_Type()
)
w2kConfigCpuLossAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigCpuLossAction.setStatus("mandatory")
_W2kConfigMemGroup_ObjectIdentity = ObjectIdentity
w2kConfigMemGroup = _W2kConfigMemGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 4)
)


class _W2kConfigMemPollInterval_Type(Integer32):
    """Custom type w2kConfigMemPollInterval based on Integer32"""
    defaultValue = 120


_W2kConfigMemPollInterval_Object = MibScalar
w2kConfigMemPollInterval = _W2kConfigMemPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 4, 1),
    _W2kConfigMemPollInterval_Type()
)
w2kConfigMemPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigMemPollInterval.setStatus("mandatory")


class _W2kConfigMemPollMethod_Type(Integer32):
    """Custom type w2kConfigMemPollMethod based on Integer32"""
    defaultValue = 2

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
        *(("disabled", 1),
          ("poll-interval-and-query", 3),
          ("poll-interval-only", 2),
          ("query-only", 4))
    )


_W2kConfigMemPollMethod_Type.__name__ = "Integer32"
_W2kConfigMemPollMethod_Object = MibScalar
w2kConfigMemPollMethod = _W2kConfigMemPollMethod_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 4, 2),
    _W2kConfigMemPollMethod_Type()
)
w2kConfigMemPollMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigMemPollMethod.setStatus("mandatory")
_W2kConfigLVolGroup_ObjectIdentity = ObjectIdentity
w2kConfigLVolGroup = _W2kConfigLVolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 5)
)


class _W2kConfigLVolPollInterval_Type(Integer32):
    """Custom type w2kConfigLVolPollInterval based on Integer32"""
    defaultValue = 120


_W2kConfigLVolPollInterval_Object = MibScalar
w2kConfigLVolPollInterval = _W2kConfigLVolPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 5, 1),
    _W2kConfigLVolPollInterval_Type()
)
w2kConfigLVolPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigLVolPollInterval.setStatus("mandatory")


class _W2kConfigLVolPollMethod_Type(Integer32):
    """Custom type w2kConfigLVolPollMethod based on Integer32"""
    defaultValue = 2

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
        *(("disabled", 1),
          ("poll-interval-and-query", 3),
          ("poll-interval-only", 2),
          ("query-only", 4))
    )


_W2kConfigLVolPollMethod_Type.__name__ = "Integer32"
_W2kConfigLVolPollMethod_Object = MibScalar
w2kConfigLVolPollMethod = _W2kConfigLVolPollMethod_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 5, 2),
    _W2kConfigLVolPollMethod_Type()
)
w2kConfigLVolPollMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigLVolPollMethod.setStatus("mandatory")


class _W2kConfigLVolAutoPollInterval_Type(Integer32):
    """Custom type w2kConfigLVolAutoPollInterval based on Integer32"""
    defaultValue = 60


_W2kConfigLVolAutoPollInterval_Object = MibScalar
w2kConfigLVolAutoPollInterval = _W2kConfigLVolAutoPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 5, 3),
    _W2kConfigLVolAutoPollInterval_Type()
)
w2kConfigLVolAutoPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigLVolAutoPollInterval.setStatus("mandatory")


class _W2kConfigLVolFragPollInterval_Type(Integer32):
    """Custom type w2kConfigLVolFragPollInterval based on Integer32"""
    defaultValue = 8


_W2kConfigLVolFragPollInterval_Object = MibScalar
w2kConfigLVolFragPollInterval = _W2kConfigLVolFragPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 5, 4),
    _W2kConfigLVolFragPollInterval_Type()
)
w2kConfigLVolFragPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigLVolFragPollInterval.setStatus("mandatory")
_W2kConfigLVolName_Type = DisplayString
_W2kConfigLVolName_Object = MibScalar
w2kConfigLVolName = _W2kConfigLVolName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 5, 5),
    _W2kConfigLVolName_Type()
)
w2kConfigLVolName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigLVolName.setStatus("mandatory")
_W2kConfigLVolDescription_Type = DisplayString
_W2kConfigLVolDescription_Object = MibScalar
w2kConfigLVolDescription = _W2kConfigLVolDescription_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 5, 6),
    _W2kConfigLVolDescription_Type()
)
w2kConfigLVolDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigLVolDescription.setStatus("mandatory")


class _W2kConfigLVolAggLag_Type(Integer32):
    """Custom type w2kConfigLVolAggLag based on Integer32"""
    defaultValue = 1


_W2kConfigLVolAggLag_Object = MibScalar
w2kConfigLVolAggLag = _W2kConfigLVolAggLag_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 5, 7),
    _W2kConfigLVolAggLag_Type()
)
w2kConfigLVolAggLag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigLVolAggLag.setStatus("mandatory")


class _W2kConfigLVolSizeWarn_Type(DisplayString):
    """Custom type w2kConfigLVolSizeWarn based on DisplayString"""
    defaultValue = OctetString("70%")


_W2kConfigLVolSizeWarn_Object = MibScalar
w2kConfigLVolSizeWarn = _W2kConfigLVolSizeWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 5, 8),
    _W2kConfigLVolSizeWarn_Type()
)
w2kConfigLVolSizeWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigLVolSizeWarn.setStatus("mandatory")


class _W2kConfigLVolSizeCrit_Type(DisplayString):
    """Custom type w2kConfigLVolSizeCrit based on DisplayString"""
    defaultValue = OctetString("90%")


_W2kConfigLVolSizeCrit_Object = MibScalar
w2kConfigLVolSizeCrit = _W2kConfigLVolSizeCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 5, 9),
    _W2kConfigLVolSizeCrit_Type()
)
w2kConfigLVolSizeCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigLVolSizeCrit.setStatus("mandatory")


class _W2kConfigLVolSizeMonitor_Type(Integer32):
    """Custom type w2kConfigLVolSizeMonitor based on Integer32"""
    defaultValue = 4

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
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_W2kConfigLVolSizeMonitor_Type.__name__ = "Integer32"
_W2kConfigLVolSizeMonitor_Object = MibScalar
w2kConfigLVolSizeMonitor = _W2kConfigLVolSizeMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 5, 10),
    _W2kConfigLVolSizeMonitor_Type()
)
w2kConfigLVolSizeMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigLVolSizeMonitor.setStatus("mandatory")


class _W2kConfigLVolSizeDWarn_Type(DisplayString):
    """Custom type w2kConfigLVolSizeDWarn based on DisplayString"""
    defaultValue = OctetString("1%")


_W2kConfigLVolSizeDWarn_Object = MibScalar
w2kConfigLVolSizeDWarn = _W2kConfigLVolSizeDWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 5, 11),
    _W2kConfigLVolSizeDWarn_Type()
)
w2kConfigLVolSizeDWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigLVolSizeDWarn.setStatus("mandatory")


class _W2kConfigLVolSizeDCrit_Type(DisplayString):
    """Custom type w2kConfigLVolSizeDCrit based on DisplayString"""
    defaultValue = OctetString("2%")


_W2kConfigLVolSizeDCrit_Object = MibScalar
w2kConfigLVolSizeDCrit = _W2kConfigLVolSizeDCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 5, 12),
    _W2kConfigLVolSizeDCrit_Type()
)
w2kConfigLVolSizeDCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigLVolSizeDCrit.setStatus("mandatory")


class _W2kConfigLVolSizeDMonitor_Type(Integer32):
    """Custom type w2kConfigLVolSizeDMonitor based on Integer32"""
    defaultValue = 4

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
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_W2kConfigLVolSizeDMonitor_Type.__name__ = "Integer32"
_W2kConfigLVolSizeDMonitor_Object = MibScalar
w2kConfigLVolSizeDMonitor = _W2kConfigLVolSizeDMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 5, 13),
    _W2kConfigLVolSizeDMonitor_Type()
)
w2kConfigLVolSizeDMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigLVolSizeDMonitor.setStatus("mandatory")


class _W2kConfigLVolTPutWarn_Type(Integer32):
    """Custom type w2kConfigLVolTPutWarn based on Integer32"""
    defaultValue = 400


_W2kConfigLVolTPutWarn_Object = MibScalar
w2kConfigLVolTPutWarn = _W2kConfigLVolTPutWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 5, 14),
    _W2kConfigLVolTPutWarn_Type()
)
w2kConfigLVolTPutWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigLVolTPutWarn.setStatus("mandatory")


class _W2kConfigLVolTPutCrit_Type(Integer32):
    """Custom type w2kConfigLVolTPutCrit based on Integer32"""
    defaultValue = 800


_W2kConfigLVolTPutCrit_Object = MibScalar
w2kConfigLVolTPutCrit = _W2kConfigLVolTPutCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 5, 15),
    _W2kConfigLVolTPutCrit_Type()
)
w2kConfigLVolTPutCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigLVolTPutCrit.setStatus("mandatory")


class _W2kConfigLVolTPutMonitor_Type(Integer32):
    """Custom type w2kConfigLVolTPutMonitor based on Integer32"""
    defaultValue = 4

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
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_W2kConfigLVolTPutMonitor_Type.__name__ = "Integer32"
_W2kConfigLVolTPutMonitor_Object = MibScalar
w2kConfigLVolTPutMonitor = _W2kConfigLVolTPutMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 5, 16),
    _W2kConfigLVolTPutMonitor_Type()
)
w2kConfigLVolTPutMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigLVolTPutMonitor.setStatus("mandatory")


class _W2kConfigLVolFragWarn_Type(Integer32):
    """Custom type w2kConfigLVolFragWarn based on Integer32"""
    defaultValue = 30


_W2kConfigLVolFragWarn_Object = MibScalar
w2kConfigLVolFragWarn = _W2kConfigLVolFragWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 5, 17),
    _W2kConfigLVolFragWarn_Type()
)
w2kConfigLVolFragWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigLVolFragWarn.setStatus("mandatory")


class _W2kConfigLVolFragCrit_Type(Integer32):
    """Custom type w2kConfigLVolFragCrit based on Integer32"""
    defaultValue = 50


_W2kConfigLVolFragCrit_Object = MibScalar
w2kConfigLVolFragCrit = _W2kConfigLVolFragCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 5, 18),
    _W2kConfigLVolFragCrit_Type()
)
w2kConfigLVolFragCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigLVolFragCrit.setStatus("mandatory")


class _W2kConfigLVolFragMonitor_Type(Integer32):
    """Custom type w2kConfigLVolFragMonitor based on Integer32"""
    defaultValue = 4

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
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_W2kConfigLVolFragMonitor_Type.__name__ = "Integer32"
_W2kConfigLVolFragMonitor_Object = MibScalar
w2kConfigLVolFragMonitor = _W2kConfigLVolFragMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 5, 19),
    _W2kConfigLVolFragMonitor_Type()
)
w2kConfigLVolFragMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigLVolFragMonitor.setStatus("mandatory")


class _W2kConfigLVolLossAction_Type(Integer32):
    """Custom type w2kConfigLVolLossAction based on Integer32"""
    defaultValue = 4

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
        *(("down-critical", 4),
          ("down-warning", 3),
          ("remove", 1),
          ("up", 2))
    )


_W2kConfigLVolLossAction_Type.__name__ = "Integer32"
_W2kConfigLVolLossAction_Object = MibScalar
w2kConfigLVolLossAction = _W2kConfigLVolLossAction_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 5, 20),
    _W2kConfigLVolLossAction_Type()
)
w2kConfigLVolLossAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigLVolLossAction.setStatus("mandatory")
_W2kConfigLVolAutoTableWatcherName_Type = DisplayString
_W2kConfigLVolAutoTableWatcherName_Object = MibScalar
w2kConfigLVolAutoTableWatcherName = _W2kConfigLVolAutoTableWatcherName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 5, 21),
    _W2kConfigLVolAutoTableWatcherName_Type()
)
w2kConfigLVolAutoTableWatcherName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigLVolAutoTableWatcherName.setStatus("mandatory")


class _W2kConfigLVolButton_Type(Integer32):
    """Custom type w2kConfigLVolButton based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("add", 2),
          ("add-auto", 4),
          ("none", 1),
          ("remove", 3),
          ("remove-auto", 5))
    )


_W2kConfigLVolButton_Type.__name__ = "Integer32"
_W2kConfigLVolButton_Object = MibScalar
w2kConfigLVolButton = _W2kConfigLVolButton_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 5, 22),
    _W2kConfigLVolButton_Type()
)
w2kConfigLVolButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigLVolButton.setStatus("mandatory")
_W2kConfigLVolAutoTable_Object = MibTable
w2kConfigLVolAutoTable = _W2kConfigLVolAutoTable_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 5, 23)
)
if mibBuilder.loadTexts:
    w2kConfigLVolAutoTable.setStatus("mandatory")
_W2kConfigLVolAutoEntry_Object = MibTableRow
w2kConfigLVolAutoEntry = _W2kConfigLVolAutoEntry_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 5, 23, 1)
)
w2kConfigLVolAutoEntry.setIndexNames(
    (0, "CA-W2KOS-MIB", "w2kConfigLVolAutoWatcherName"),
)
if mibBuilder.loadTexts:
    w2kConfigLVolAutoEntry.setStatus("mandatory")
_W2kConfigLVolAutoWatcherName_Type = DisplayString
_W2kConfigLVolAutoWatcherName_Object = MibTableColumn
w2kConfigLVolAutoWatcherName = _W2kConfigLVolAutoWatcherName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 5, 23, 1, 1),
    _W2kConfigLVolAutoWatcherName_Type()
)
w2kConfigLVolAutoWatcherName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kConfigLVolAutoWatcherName.setStatus("mandatory")
_W2kConfigLVolAutoName_Type = DisplayString
_W2kConfigLVolAutoName_Object = MibTableColumn
w2kConfigLVolAutoName = _W2kConfigLVolAutoName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 5, 23, 1, 2),
    _W2kConfigLVolAutoName_Type()
)
w2kConfigLVolAutoName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigLVolAutoName.setStatus("mandatory")
_W2kConfigLVolAutoDescription_Type = DisplayString
_W2kConfigLVolAutoDescription_Object = MibTableColumn
w2kConfigLVolAutoDescription = _W2kConfigLVolAutoDescription_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 5, 23, 1, 3),
    _W2kConfigLVolAutoDescription_Type()
)
w2kConfigLVolAutoDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigLVolAutoDescription.setStatus("mandatory")
_W2kConfigLVolAutoAggLag_Type = Integer32
_W2kConfigLVolAutoAggLag_Object = MibTableColumn
w2kConfigLVolAutoAggLag = _W2kConfigLVolAutoAggLag_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 5, 23, 1, 4),
    _W2kConfigLVolAutoAggLag_Type()
)
w2kConfigLVolAutoAggLag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigLVolAutoAggLag.setStatus("mandatory")
_W2kConfigLVolAutoSizeWarn_Type = DisplayString
_W2kConfigLVolAutoSizeWarn_Object = MibTableColumn
w2kConfigLVolAutoSizeWarn = _W2kConfigLVolAutoSizeWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 5, 23, 1, 5),
    _W2kConfigLVolAutoSizeWarn_Type()
)
w2kConfigLVolAutoSizeWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigLVolAutoSizeWarn.setStatus("mandatory")
_W2kConfigLVolAutoSizeCrit_Type = DisplayString
_W2kConfigLVolAutoSizeCrit_Object = MibTableColumn
w2kConfigLVolAutoSizeCrit = _W2kConfigLVolAutoSizeCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 5, 23, 1, 6),
    _W2kConfigLVolAutoSizeCrit_Type()
)
w2kConfigLVolAutoSizeCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigLVolAutoSizeCrit.setStatus("mandatory")


class _W2kConfigLVolAutoSizeMonitor_Type(Integer32):
    """Custom type w2kConfigLVolAutoSizeMonitor based on Integer32"""
    defaultValue = 0

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
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_W2kConfigLVolAutoSizeMonitor_Type.__name__ = "Integer32"
_W2kConfigLVolAutoSizeMonitor_Object = MibTableColumn
w2kConfigLVolAutoSizeMonitor = _W2kConfigLVolAutoSizeMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 5, 23, 1, 7),
    _W2kConfigLVolAutoSizeMonitor_Type()
)
w2kConfigLVolAutoSizeMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigLVolAutoSizeMonitor.setStatus("mandatory")
_W2kConfigLVolAutoSizeDWarn_Type = DisplayString
_W2kConfigLVolAutoSizeDWarn_Object = MibTableColumn
w2kConfigLVolAutoSizeDWarn = _W2kConfigLVolAutoSizeDWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 5, 23, 1, 8),
    _W2kConfigLVolAutoSizeDWarn_Type()
)
w2kConfigLVolAutoSizeDWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigLVolAutoSizeDWarn.setStatus("mandatory")
_W2kConfigLVolAutoSizeDCrit_Type = DisplayString
_W2kConfigLVolAutoSizeDCrit_Object = MibTableColumn
w2kConfigLVolAutoSizeDCrit = _W2kConfigLVolAutoSizeDCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 5, 23, 1, 9),
    _W2kConfigLVolAutoSizeDCrit_Type()
)
w2kConfigLVolAutoSizeDCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigLVolAutoSizeDCrit.setStatus("mandatory")


class _W2kConfigLVolAutoSizeDMonitor_Type(Integer32):
    """Custom type w2kConfigLVolAutoSizeDMonitor based on Integer32"""
    defaultValue = 0

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
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_W2kConfigLVolAutoSizeDMonitor_Type.__name__ = "Integer32"
_W2kConfigLVolAutoSizeDMonitor_Object = MibTableColumn
w2kConfigLVolAutoSizeDMonitor = _W2kConfigLVolAutoSizeDMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 5, 23, 1, 10),
    _W2kConfigLVolAutoSizeDMonitor_Type()
)
w2kConfigLVolAutoSizeDMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigLVolAutoSizeDMonitor.setStatus("mandatory")
_W2kConfigLVolAutoTPutWarn_Type = Integer32
_W2kConfigLVolAutoTPutWarn_Object = MibTableColumn
w2kConfigLVolAutoTPutWarn = _W2kConfigLVolAutoTPutWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 5, 23, 1, 11),
    _W2kConfigLVolAutoTPutWarn_Type()
)
w2kConfigLVolAutoTPutWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigLVolAutoTPutWarn.setStatus("mandatory")
_W2kConfigLVolAutoTPutCrit_Type = Integer32
_W2kConfigLVolAutoTPutCrit_Object = MibTableColumn
w2kConfigLVolAutoTPutCrit = _W2kConfigLVolAutoTPutCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 5, 23, 1, 12),
    _W2kConfigLVolAutoTPutCrit_Type()
)
w2kConfigLVolAutoTPutCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigLVolAutoTPutCrit.setStatus("mandatory")


class _W2kConfigLVolAutoTPutMonitor_Type(Integer32):
    """Custom type w2kConfigLVolAutoTPutMonitor based on Integer32"""
    defaultValue = 0

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
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_W2kConfigLVolAutoTPutMonitor_Type.__name__ = "Integer32"
_W2kConfigLVolAutoTPutMonitor_Object = MibTableColumn
w2kConfigLVolAutoTPutMonitor = _W2kConfigLVolAutoTPutMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 5, 23, 1, 13),
    _W2kConfigLVolAutoTPutMonitor_Type()
)
w2kConfigLVolAutoTPutMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigLVolAutoTPutMonitor.setStatus("mandatory")
_W2kConfigLVolAutoFragWarn_Type = Integer32
_W2kConfigLVolAutoFragWarn_Object = MibTableColumn
w2kConfigLVolAutoFragWarn = _W2kConfigLVolAutoFragWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 5, 23, 1, 14),
    _W2kConfigLVolAutoFragWarn_Type()
)
w2kConfigLVolAutoFragWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigLVolAutoFragWarn.setStatus("mandatory")
_W2kConfigLVolAutoFragCrit_Type = Integer32
_W2kConfigLVolAutoFragCrit_Object = MibTableColumn
w2kConfigLVolAutoFragCrit = _W2kConfigLVolAutoFragCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 5, 23, 1, 15),
    _W2kConfigLVolAutoFragCrit_Type()
)
w2kConfigLVolAutoFragCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigLVolAutoFragCrit.setStatus("mandatory")


class _W2kConfigLVolAutoFragMonitor_Type(Integer32):
    """Custom type w2kConfigLVolAutoFragMonitor based on Integer32"""
    defaultValue = 0

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
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_W2kConfigLVolAutoFragMonitor_Type.__name__ = "Integer32"
_W2kConfigLVolAutoFragMonitor_Object = MibTableColumn
w2kConfigLVolAutoFragMonitor = _W2kConfigLVolAutoFragMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 5, 23, 1, 16),
    _W2kConfigLVolAutoFragMonitor_Type()
)
w2kConfigLVolAutoFragMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigLVolAutoFragMonitor.setStatus("mandatory")


class _W2kConfigLVolAutoLossAction_Type(Integer32):
    """Custom type w2kConfigLVolAutoLossAction based on Integer32"""
    defaultValue = 0

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
        *(("down-critical", 4),
          ("down-warning", 3),
          ("remove", 1),
          ("up", 2))
    )


_W2kConfigLVolAutoLossAction_Type.__name__ = "Integer32"
_W2kConfigLVolAutoLossAction_Object = MibTableColumn
w2kConfigLVolAutoLossAction = _W2kConfigLVolAutoLossAction_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 5, 23, 1, 17),
    _W2kConfigLVolAutoLossAction_Type()
)
w2kConfigLVolAutoLossAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigLVolAutoLossAction.setStatus("mandatory")


class _W2kConfigLVolAutoButton_Type(Integer32):
    """Custom type w2kConfigLVolAutoButton based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("remove", 2))
    )


_W2kConfigLVolAutoButton_Type.__name__ = "Integer32"
_W2kConfigLVolAutoButton_Object = MibTableColumn
w2kConfigLVolAutoButton = _W2kConfigLVolAutoButton_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 5, 23, 1, 18),
    _W2kConfigLVolAutoButton_Type()
)
w2kConfigLVolAutoButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigLVolAutoButton.setStatus("mandatory")
_W2kConfigMntGroup_ObjectIdentity = ObjectIdentity
w2kConfigMntGroup = _W2kConfigMntGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 6)
)


class _W2kConfigMntPollInterval_Type(Integer32):
    """Custom type w2kConfigMntPollInterval based on Integer32"""
    defaultValue = 120


_W2kConfigMntPollInterval_Object = MibScalar
w2kConfigMntPollInterval = _W2kConfigMntPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 6, 1),
    _W2kConfigMntPollInterval_Type()
)
w2kConfigMntPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigMntPollInterval.setStatus("mandatory")


class _W2kConfigMntPollMethod_Type(Integer32):
    """Custom type w2kConfigMntPollMethod based on Integer32"""
    defaultValue = 2

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
        *(("disabled", 1),
          ("poll-interval-and-query", 3),
          ("poll-interval-only", 2),
          ("query-only", 4))
    )


_W2kConfigMntPollMethod_Type.__name__ = "Integer32"
_W2kConfigMntPollMethod_Object = MibScalar
w2kConfigMntPollMethod = _W2kConfigMntPollMethod_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 6, 2),
    _W2kConfigMntPollMethod_Type()
)
w2kConfigMntPollMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigMntPollMethod.setStatus("mandatory")


class _W2kConfigMntAutoPollInterval_Type(Integer32):
    """Custom type w2kConfigMntAutoPollInterval based on Integer32"""
    defaultValue = 60


_W2kConfigMntAutoPollInterval_Object = MibScalar
w2kConfigMntAutoPollInterval = _W2kConfigMntAutoPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 6, 3),
    _W2kConfigMntAutoPollInterval_Type()
)
w2kConfigMntAutoPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigMntAutoPollInterval.setStatus("mandatory")
_W2kConfigMntName_Type = DisplayString
_W2kConfigMntName_Object = MibScalar
w2kConfigMntName = _W2kConfigMntName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 6, 4),
    _W2kConfigMntName_Type()
)
w2kConfigMntName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigMntName.setStatus("mandatory")
_W2kConfigMntDescription_Type = DisplayString
_W2kConfigMntDescription_Object = MibScalar
w2kConfigMntDescription = _W2kConfigMntDescription_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 6, 5),
    _W2kConfigMntDescription_Type()
)
w2kConfigMntDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigMntDescription.setStatus("mandatory")


class _W2kConfigMntAggLag_Type(Integer32):
    """Custom type w2kConfigMntAggLag based on Integer32"""
    defaultValue = 1


_W2kConfigMntAggLag_Object = MibScalar
w2kConfigMntAggLag = _W2kConfigMntAggLag_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 6, 6),
    _W2kConfigMntAggLag_Type()
)
w2kConfigMntAggLag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigMntAggLag.setStatus("mandatory")


class _W2kConfigMntRelToMonitor_Type(Integer32):
    """Custom type w2kConfigMntRelToMonitor based on Integer32"""
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
        *(("do-not-monitor", 1),
          ("down-critical", 3),
          ("down-warning", 2))
    )


_W2kConfigMntRelToMonitor_Type.__name__ = "Integer32"
_W2kConfigMntRelToMonitor_Object = MibScalar
w2kConfigMntRelToMonitor = _W2kConfigMntRelToMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 6, 7),
    _W2kConfigMntRelToMonitor_Type()
)
w2kConfigMntRelToMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigMntRelToMonitor.setStatus("mandatory")


class _W2kConfigMntLossAction_Type(Integer32):
    """Custom type w2kConfigMntLossAction based on Integer32"""
    defaultValue = 4

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
        *(("down-critical", 4),
          ("down-warning", 3),
          ("remove", 1),
          ("up", 2))
    )


_W2kConfigMntLossAction_Type.__name__ = "Integer32"
_W2kConfigMntLossAction_Object = MibScalar
w2kConfigMntLossAction = _W2kConfigMntLossAction_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 6, 8),
    _W2kConfigMntLossAction_Type()
)
w2kConfigMntLossAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigMntLossAction.setStatus("mandatory")
_W2kConfigMntAutoTableWatcherName_Type = DisplayString
_W2kConfigMntAutoTableWatcherName_Object = MibScalar
w2kConfigMntAutoTableWatcherName = _W2kConfigMntAutoTableWatcherName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 6, 9),
    _W2kConfigMntAutoTableWatcherName_Type()
)
w2kConfigMntAutoTableWatcherName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigMntAutoTableWatcherName.setStatus("mandatory")


class _W2kConfigMntButton_Type(Integer32):
    """Custom type w2kConfigMntButton based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("add", 2),
          ("add-auto", 4),
          ("none", 1),
          ("remove", 3),
          ("remove-auto", 5))
    )


_W2kConfigMntButton_Type.__name__ = "Integer32"
_W2kConfigMntButton_Object = MibScalar
w2kConfigMntButton = _W2kConfigMntButton_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 6, 10),
    _W2kConfigMntButton_Type()
)
w2kConfigMntButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigMntButton.setStatus("mandatory")
_W2kConfigMntAutoTable_Object = MibTable
w2kConfigMntAutoTable = _W2kConfigMntAutoTable_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 6, 11)
)
if mibBuilder.loadTexts:
    w2kConfigMntAutoTable.setStatus("mandatory")
_W2kConfigMntAutoEntry_Object = MibTableRow
w2kConfigMntAutoEntry = _W2kConfigMntAutoEntry_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 6, 11, 1)
)
w2kConfigMntAutoEntry.setIndexNames(
    (0, "CA-W2KOS-MIB", "w2kConfigMntAutoWatcherName"),
)
if mibBuilder.loadTexts:
    w2kConfigMntAutoEntry.setStatus("mandatory")
_W2kConfigMntAutoWatcherName_Type = DisplayString
_W2kConfigMntAutoWatcherName_Object = MibTableColumn
w2kConfigMntAutoWatcherName = _W2kConfigMntAutoWatcherName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 6, 11, 1, 1),
    _W2kConfigMntAutoWatcherName_Type()
)
w2kConfigMntAutoWatcherName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kConfigMntAutoWatcherName.setStatus("mandatory")
_W2kConfigMntAutoName_Type = DisplayString
_W2kConfigMntAutoName_Object = MibTableColumn
w2kConfigMntAutoName = _W2kConfigMntAutoName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 6, 11, 1, 2),
    _W2kConfigMntAutoName_Type()
)
w2kConfigMntAutoName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigMntAutoName.setStatus("mandatory")
_W2kConfigMntAutoDescription_Type = DisplayString
_W2kConfigMntAutoDescription_Object = MibTableColumn
w2kConfigMntAutoDescription = _W2kConfigMntAutoDescription_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 6, 11, 1, 3),
    _W2kConfigMntAutoDescription_Type()
)
w2kConfigMntAutoDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigMntAutoDescription.setStatus("mandatory")
_W2kConfigMntAutoAggLag_Type = Integer32
_W2kConfigMntAutoAggLag_Object = MibTableColumn
w2kConfigMntAutoAggLag = _W2kConfigMntAutoAggLag_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 6, 11, 1, 4),
    _W2kConfigMntAutoAggLag_Type()
)
w2kConfigMntAutoAggLag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigMntAutoAggLag.setStatus("mandatory")


class _W2kConfigMntAutoRelToMonitor_Type(Integer32):
    """Custom type w2kConfigMntAutoRelToMonitor based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("do-not-monitor", 1),
          ("down-critical", 3),
          ("down-warning", 2))
    )


_W2kConfigMntAutoRelToMonitor_Type.__name__ = "Integer32"
_W2kConfigMntAutoRelToMonitor_Object = MibTableColumn
w2kConfigMntAutoRelToMonitor = _W2kConfigMntAutoRelToMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 6, 11, 1, 5),
    _W2kConfigMntAutoRelToMonitor_Type()
)
w2kConfigMntAutoRelToMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigMntAutoRelToMonitor.setStatus("mandatory")


class _W2kConfigMntAutoLossAction_Type(Integer32):
    """Custom type w2kConfigMntAutoLossAction based on Integer32"""
    defaultValue = 0

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
        *(("down-critical", 4),
          ("down-warning", 3),
          ("remove", 1),
          ("up", 2))
    )


_W2kConfigMntAutoLossAction_Type.__name__ = "Integer32"
_W2kConfigMntAutoLossAction_Object = MibTableColumn
w2kConfigMntAutoLossAction = _W2kConfigMntAutoLossAction_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 6, 11, 1, 6),
    _W2kConfigMntAutoLossAction_Type()
)
w2kConfigMntAutoLossAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigMntAutoLossAction.setStatus("mandatory")


class _W2kConfigMntAutoButton_Type(Integer32):
    """Custom type w2kConfigMntAutoButton based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("remove", 2))
    )


_W2kConfigMntAutoButton_Type.__name__ = "Integer32"
_W2kConfigMntAutoButton_Object = MibTableColumn
w2kConfigMntAutoButton = _W2kConfigMntAutoButton_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 6, 11, 1, 9),
    _W2kConfigMntAutoButton_Type()
)
w2kConfigMntAutoButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigMntAutoButton.setStatus("mandatory")
_W2kConfigDfsGroup_ObjectIdentity = ObjectIdentity
w2kConfigDfsGroup = _W2kConfigDfsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 7)
)


class _W2kConfigDfsPollInterval_Type(Integer32):
    """Custom type w2kConfigDfsPollInterval based on Integer32"""
    defaultValue = 120


_W2kConfigDfsPollInterval_Object = MibScalar
w2kConfigDfsPollInterval = _W2kConfigDfsPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 7, 1),
    _W2kConfigDfsPollInterval_Type()
)
w2kConfigDfsPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigDfsPollInterval.setStatus("mandatory")


class _W2kConfigDfsPollMethod_Type(Integer32):
    """Custom type w2kConfigDfsPollMethod based on Integer32"""
    defaultValue = 2

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
        *(("disabled", 1),
          ("poll-interval-and-query", 3),
          ("poll-interval-only", 2),
          ("query-only", 4))
    )


_W2kConfigDfsPollMethod_Type.__name__ = "Integer32"
_W2kConfigDfsPollMethod_Object = MibScalar
w2kConfigDfsPollMethod = _W2kConfigDfsPollMethod_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 7, 2),
    _W2kConfigDfsPollMethod_Type()
)
w2kConfigDfsPollMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigDfsPollMethod.setStatus("mandatory")


class _W2kConfigDfsAutoPollInterval_Type(Integer32):
    """Custom type w2kConfigDfsAutoPollInterval based on Integer32"""
    defaultValue = 60


_W2kConfigDfsAutoPollInterval_Object = MibScalar
w2kConfigDfsAutoPollInterval = _W2kConfigDfsAutoPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 7, 3),
    _W2kConfigDfsAutoPollInterval_Type()
)
w2kConfigDfsAutoPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigDfsAutoPollInterval.setStatus("mandatory")
_W2kConfigDfsName_Type = DisplayString
_W2kConfigDfsName_Object = MibScalar
w2kConfigDfsName = _W2kConfigDfsName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 7, 4),
    _W2kConfigDfsName_Type()
)
w2kConfigDfsName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigDfsName.setStatus("mandatory")
_W2kConfigDfsDescription_Type = DisplayString
_W2kConfigDfsDescription_Object = MibScalar
w2kConfigDfsDescription = _W2kConfigDfsDescription_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 7, 5),
    _W2kConfigDfsDescription_Type()
)
w2kConfigDfsDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigDfsDescription.setStatus("mandatory")


class _W2kConfigDfsAggLag_Type(Integer32):
    """Custom type w2kConfigDfsAggLag based on Integer32"""
    defaultValue = 1


_W2kConfigDfsAggLag_Object = MibScalar
w2kConfigDfsAggLag = _W2kConfigDfsAggLag_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 7, 6),
    _W2kConfigDfsAggLag_Type()
)
w2kConfigDfsAggLag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigDfsAggLag.setStatus("mandatory")


class _W2kConfigDfsReplicaWarn_Type(Integer32):
    """Custom type w2kConfigDfsReplicaWarn based on Integer32"""
    defaultValue = 1


_W2kConfigDfsReplicaWarn_Object = MibScalar
w2kConfigDfsReplicaWarn = _W2kConfigDfsReplicaWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 7, 7),
    _W2kConfigDfsReplicaWarn_Type()
)
w2kConfigDfsReplicaWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigDfsReplicaWarn.setStatus("mandatory")


class _W2kConfigDfsReplicaCrit_Type(Integer32):
    """Custom type w2kConfigDfsReplicaCrit based on Integer32"""
    defaultValue = 2


_W2kConfigDfsReplicaCrit_Object = MibScalar
w2kConfigDfsReplicaCrit = _W2kConfigDfsReplicaCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 7, 8),
    _W2kConfigDfsReplicaCrit_Type()
)
w2kConfigDfsReplicaCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigDfsReplicaCrit.setStatus("mandatory")


class _W2kConfigDfsReplicaMonitor_Type(Integer32):
    """Custom type w2kConfigDfsReplicaMonitor based on Integer32"""
    defaultValue = 4

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
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_W2kConfigDfsReplicaMonitor_Type.__name__ = "Integer32"
_W2kConfigDfsReplicaMonitor_Object = MibScalar
w2kConfigDfsReplicaMonitor = _W2kConfigDfsReplicaMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 7, 9),
    _W2kConfigDfsReplicaMonitor_Type()
)
w2kConfigDfsReplicaMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigDfsReplicaMonitor.setStatus("mandatory")


class _W2kConfigDfsLossAction_Type(Integer32):
    """Custom type w2kConfigDfsLossAction based on Integer32"""
    defaultValue = 4

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
        *(("down-critical", 4),
          ("down-warning", 3),
          ("remove", 1),
          ("up", 2))
    )


_W2kConfigDfsLossAction_Type.__name__ = "Integer32"
_W2kConfigDfsLossAction_Object = MibScalar
w2kConfigDfsLossAction = _W2kConfigDfsLossAction_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 7, 10),
    _W2kConfigDfsLossAction_Type()
)
w2kConfigDfsLossAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigDfsLossAction.setStatus("mandatory")
_W2kConfigDfsAutoTableWatcherName_Type = DisplayString
_W2kConfigDfsAutoTableWatcherName_Object = MibScalar
w2kConfigDfsAutoTableWatcherName = _W2kConfigDfsAutoTableWatcherName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 7, 11),
    _W2kConfigDfsAutoTableWatcherName_Type()
)
w2kConfigDfsAutoTableWatcherName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigDfsAutoTableWatcherName.setStatus("mandatory")


class _W2kConfigDfsButton_Type(Integer32):
    """Custom type w2kConfigDfsButton based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("add", 2),
          ("add-auto", 4),
          ("none", 1),
          ("remove", 3),
          ("remove-auto", 5))
    )


_W2kConfigDfsButton_Type.__name__ = "Integer32"
_W2kConfigDfsButton_Object = MibScalar
w2kConfigDfsButton = _W2kConfigDfsButton_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 7, 12),
    _W2kConfigDfsButton_Type()
)
w2kConfigDfsButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigDfsButton.setStatus("mandatory")
_W2kConfigDfsAutoTable_Object = MibTable
w2kConfigDfsAutoTable = _W2kConfigDfsAutoTable_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 7, 13)
)
if mibBuilder.loadTexts:
    w2kConfigDfsAutoTable.setStatus("mandatory")
_W2kConfigDfsAutoEntry_Object = MibTableRow
w2kConfigDfsAutoEntry = _W2kConfigDfsAutoEntry_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 7, 13, 1)
)
w2kConfigDfsAutoEntry.setIndexNames(
    (0, "CA-W2KOS-MIB", "w2kConfigDfsAutoWatcherName"),
)
if mibBuilder.loadTexts:
    w2kConfigDfsAutoEntry.setStatus("mandatory")
_W2kConfigDfsAutoWatcherName_Type = DisplayString
_W2kConfigDfsAutoWatcherName_Object = MibTableColumn
w2kConfigDfsAutoWatcherName = _W2kConfigDfsAutoWatcherName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 7, 13, 1, 1),
    _W2kConfigDfsAutoWatcherName_Type()
)
w2kConfigDfsAutoWatcherName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kConfigDfsAutoWatcherName.setStatus("mandatory")
_W2kConfigDfsAutoName_Type = DisplayString
_W2kConfigDfsAutoName_Object = MibTableColumn
w2kConfigDfsAutoName = _W2kConfigDfsAutoName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 7, 13, 1, 2),
    _W2kConfigDfsAutoName_Type()
)
w2kConfigDfsAutoName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigDfsAutoName.setStatus("mandatory")
_W2kConfigDfsAutoDescription_Type = DisplayString
_W2kConfigDfsAutoDescription_Object = MibTableColumn
w2kConfigDfsAutoDescription = _W2kConfigDfsAutoDescription_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 7, 13, 1, 3),
    _W2kConfigDfsAutoDescription_Type()
)
w2kConfigDfsAutoDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigDfsAutoDescription.setStatus("mandatory")
_W2kConfigDfsAutoAggLag_Type = Integer32
_W2kConfigDfsAutoAggLag_Object = MibTableColumn
w2kConfigDfsAutoAggLag = _W2kConfigDfsAutoAggLag_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 7, 13, 1, 4),
    _W2kConfigDfsAutoAggLag_Type()
)
w2kConfigDfsAutoAggLag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigDfsAutoAggLag.setStatus("mandatory")
_W2kConfigDfsAutoReplicaWarn_Type = Integer32
_W2kConfigDfsAutoReplicaWarn_Object = MibTableColumn
w2kConfigDfsAutoReplicaWarn = _W2kConfigDfsAutoReplicaWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 7, 13, 1, 5),
    _W2kConfigDfsAutoReplicaWarn_Type()
)
w2kConfigDfsAutoReplicaWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigDfsAutoReplicaWarn.setStatus("mandatory")
_W2kConfigDfsAutoReplicaCrit_Type = Integer32
_W2kConfigDfsAutoReplicaCrit_Object = MibTableColumn
w2kConfigDfsAutoReplicaCrit = _W2kConfigDfsAutoReplicaCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 7, 13, 1, 6),
    _W2kConfigDfsAutoReplicaCrit_Type()
)
w2kConfigDfsAutoReplicaCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigDfsAutoReplicaCrit.setStatus("mandatory")


class _W2kConfigDfsAutoReplicaMonitor_Type(Integer32):
    """Custom type w2kConfigDfsAutoReplicaMonitor based on Integer32"""
    defaultValue = 0

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
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_W2kConfigDfsAutoReplicaMonitor_Type.__name__ = "Integer32"
_W2kConfigDfsAutoReplicaMonitor_Object = MibTableColumn
w2kConfigDfsAutoReplicaMonitor = _W2kConfigDfsAutoReplicaMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 7, 13, 1, 7),
    _W2kConfigDfsAutoReplicaMonitor_Type()
)
w2kConfigDfsAutoReplicaMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigDfsAutoReplicaMonitor.setStatus("mandatory")


class _W2kConfigDfsAutoLossAction_Type(Integer32):
    """Custom type w2kConfigDfsAutoLossAction based on Integer32"""
    defaultValue = 0

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
        *(("down-critical", 4),
          ("down-warning", 3),
          ("remove", 1),
          ("up", 2))
    )


_W2kConfigDfsAutoLossAction_Type.__name__ = "Integer32"
_W2kConfigDfsAutoLossAction_Object = MibTableColumn
w2kConfigDfsAutoLossAction = _W2kConfigDfsAutoLossAction_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 7, 13, 1, 8),
    _W2kConfigDfsAutoLossAction_Type()
)
w2kConfigDfsAutoLossAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigDfsAutoLossAction.setStatus("mandatory")


class _W2kConfigDfsAutoButton_Type(Integer32):
    """Custom type w2kConfigDfsAutoButton based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("remove", 2))
    )


_W2kConfigDfsAutoButton_Type.__name__ = "Integer32"
_W2kConfigDfsAutoButton_Object = MibTableColumn
w2kConfigDfsAutoButton = _W2kConfigDfsAutoButton_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 7, 13, 1, 9),
    _W2kConfigDfsAutoButton_Type()
)
w2kConfigDfsAutoButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigDfsAutoButton.setStatus("mandatory")
_W2kConfigQuotGroup_ObjectIdentity = ObjectIdentity
w2kConfigQuotGroup = _W2kConfigQuotGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 8)
)


class _W2kConfigQuotPollInterval_Type(Integer32):
    """Custom type w2kConfigQuotPollInterval based on Integer32"""
    defaultValue = 120


_W2kConfigQuotPollInterval_Object = MibScalar
w2kConfigQuotPollInterval = _W2kConfigQuotPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 8, 1),
    _W2kConfigQuotPollInterval_Type()
)
w2kConfigQuotPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigQuotPollInterval.setStatus("mandatory")


class _W2kConfigQuotPollMethod_Type(Integer32):
    """Custom type w2kConfigQuotPollMethod based on Integer32"""
    defaultValue = 2

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
        *(("disabled", 1),
          ("poll-interval-and-query", 3),
          ("poll-interval-only", 2),
          ("query-only", 4))
    )


_W2kConfigQuotPollMethod_Type.__name__ = "Integer32"
_W2kConfigQuotPollMethod_Object = MibScalar
w2kConfigQuotPollMethod = _W2kConfigQuotPollMethod_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 8, 2),
    _W2kConfigQuotPollMethod_Type()
)
w2kConfigQuotPollMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigQuotPollMethod.setStatus("mandatory")
_W2kConfigQuotLVolName_Type = DisplayString
_W2kConfigQuotLVolName_Object = MibScalar
w2kConfigQuotLVolName = _W2kConfigQuotLVolName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 8, 3),
    _W2kConfigQuotLVolName_Type()
)
w2kConfigQuotLVolName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigQuotLVolName.setStatus("mandatory")
_W2kConfigQuotUserName_Type = DisplayString
_W2kConfigQuotUserName_Object = MibScalar
w2kConfigQuotUserName = _W2kConfigQuotUserName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 8, 4),
    _W2kConfigQuotUserName_Type()
)
w2kConfigQuotUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigQuotUserName.setStatus("mandatory")
_W2kConfigQuotDescription_Type = DisplayString
_W2kConfigQuotDescription_Object = MibScalar
w2kConfigQuotDescription = _W2kConfigQuotDescription_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 8, 5),
    _W2kConfigQuotDescription_Type()
)
w2kConfigQuotDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigQuotDescription.setStatus("mandatory")


class _W2kConfigQuotAggLag_Type(Integer32):
    """Custom type w2kConfigQuotAggLag based on Integer32"""
    defaultValue = 1


_W2kConfigQuotAggLag_Object = MibScalar
w2kConfigQuotAggLag = _W2kConfigQuotAggLag_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 8, 6),
    _W2kConfigQuotAggLag_Type()
)
w2kConfigQuotAggLag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigQuotAggLag.setStatus("mandatory")


class _W2kConfigQuotExist_Type(Integer32):
    """Custom type w2kConfigQuotExist based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("should-exist", 1),
          ("should-not-exist", 2))
    )


_W2kConfigQuotExist_Type.__name__ = "Integer32"
_W2kConfigQuotExist_Object = MibScalar
w2kConfigQuotExist = _W2kConfigQuotExist_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 8, 7),
    _W2kConfigQuotExist_Type()
)
w2kConfigQuotExist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigQuotExist.setStatus("mandatory")


class _W2kConfigQuotExistMonitor_Type(Integer32):
    """Custom type w2kConfigQuotExistMonitor based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("do-not-monitor", 1),
          ("down-critical", 3),
          ("down-warning", 2))
    )


_W2kConfigQuotExistMonitor_Type.__name__ = "Integer32"
_W2kConfigQuotExistMonitor_Object = MibScalar
w2kConfigQuotExistMonitor = _W2kConfigQuotExistMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 8, 8),
    _W2kConfigQuotExistMonitor_Type()
)
w2kConfigQuotExistMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigQuotExistMonitor.setStatus("mandatory")


class _W2kConfigQuotSizeWarn_Type(Integer32):
    """Custom type w2kConfigQuotSizeWarn based on Integer32"""
    defaultValue = 1000


_W2kConfigQuotSizeWarn_Object = MibScalar
w2kConfigQuotSizeWarn = _W2kConfigQuotSizeWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 8, 9),
    _W2kConfigQuotSizeWarn_Type()
)
w2kConfigQuotSizeWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigQuotSizeWarn.setStatus("mandatory")


class _W2kConfigQuotSizeCrit_Type(Integer32):
    """Custom type w2kConfigQuotSizeCrit based on Integer32"""
    defaultValue = 5000


_W2kConfigQuotSizeCrit_Object = MibScalar
w2kConfigQuotSizeCrit = _W2kConfigQuotSizeCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 8, 10),
    _W2kConfigQuotSizeCrit_Type()
)
w2kConfigQuotSizeCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigQuotSizeCrit.setStatus("mandatory")


class _W2kConfigQuotSizeMonitor_Type(Integer32):
    """Custom type w2kConfigQuotSizeMonitor based on Integer32"""
    defaultValue = 4

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
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_W2kConfigQuotSizeMonitor_Type.__name__ = "Integer32"
_W2kConfigQuotSizeMonitor_Object = MibScalar
w2kConfigQuotSizeMonitor = _W2kConfigQuotSizeMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 8, 11),
    _W2kConfigQuotSizeMonitor_Type()
)
w2kConfigQuotSizeMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigQuotSizeMonitor.setStatus("mandatory")


class _W2kConfigQuotButton_Type(Integer32):
    """Custom type w2kConfigQuotButton based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("add", 2),
          ("none", 1),
          ("remove", 3))
    )


_W2kConfigQuotButton_Type.__name__ = "Integer32"
_W2kConfigQuotButton_Object = MibScalar
w2kConfigQuotButton = _W2kConfigQuotButton_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 8, 12),
    _W2kConfigQuotButton_Type()
)
w2kConfigQuotButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigQuotButton.setStatus("mandatory")
_W2kConfigDirGroup_ObjectIdentity = ObjectIdentity
w2kConfigDirGroup = _W2kConfigDirGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 9)
)


class _W2kConfigDirPollInterval_Type(Integer32):
    """Custom type w2kConfigDirPollInterval based on Integer32"""
    defaultValue = 120


_W2kConfigDirPollInterval_Object = MibScalar
w2kConfigDirPollInterval = _W2kConfigDirPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 9, 1),
    _W2kConfigDirPollInterval_Type()
)
w2kConfigDirPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigDirPollInterval.setStatus("mandatory")


class _W2kConfigDirPollMethod_Type(Integer32):
    """Custom type w2kConfigDirPollMethod based on Integer32"""
    defaultValue = 2

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
        *(("disabled", 1),
          ("poll-interval-and-query", 3),
          ("poll-interval-only", 2),
          ("query-only", 4))
    )


_W2kConfigDirPollMethod_Type.__name__ = "Integer32"
_W2kConfigDirPollMethod_Object = MibScalar
w2kConfigDirPollMethod = _W2kConfigDirPollMethod_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 9, 2),
    _W2kConfigDirPollMethod_Type()
)
w2kConfigDirPollMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigDirPollMethod.setStatus("mandatory")
_W2kConfigDirName_Type = DisplayString
_W2kConfigDirName_Object = MibScalar
w2kConfigDirName = _W2kConfigDirName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 9, 3),
    _W2kConfigDirName_Type()
)
w2kConfigDirName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigDirName.setStatus("mandatory")
_W2kConfigDirDescription_Type = DisplayString
_W2kConfigDirDescription_Object = MibScalar
w2kConfigDirDescription = _W2kConfigDirDescription_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 9, 4),
    _W2kConfigDirDescription_Type()
)
w2kConfigDirDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigDirDescription.setStatus("mandatory")


class _W2kConfigDirAggLag_Type(Integer32):
    """Custom type w2kConfigDirAggLag based on Integer32"""
    defaultValue = 1


_W2kConfigDirAggLag_Object = MibScalar
w2kConfigDirAggLag = _W2kConfigDirAggLag_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 9, 5),
    _W2kConfigDirAggLag_Type()
)
w2kConfigDirAggLag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigDirAggLag.setStatus("mandatory")


class _W2kConfigDirExist_Type(Integer32):
    """Custom type w2kConfigDirExist based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("should-exist", 1),
          ("should-not-exist", 2))
    )


_W2kConfigDirExist_Type.__name__ = "Integer32"
_W2kConfigDirExist_Object = MibScalar
w2kConfigDirExist = _W2kConfigDirExist_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 9, 6),
    _W2kConfigDirExist_Type()
)
w2kConfigDirExist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigDirExist.setStatus("mandatory")


class _W2kConfigDirExistMonitor_Type(Integer32):
    """Custom type w2kConfigDirExistMonitor based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("do-not-monitor", 1),
          ("down-critical", 3),
          ("down-warning", 2))
    )


_W2kConfigDirExistMonitor_Type.__name__ = "Integer32"
_W2kConfigDirExistMonitor_Object = MibScalar
w2kConfigDirExistMonitor = _W2kConfigDirExistMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 9, 7),
    _W2kConfigDirExistMonitor_Type()
)
w2kConfigDirExistMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigDirExistMonitor.setStatus("mandatory")


class _W2kConfigDirTimeMonitor_Type(Integer32):
    """Custom type w2kConfigDirTimeMonitor based on Integer32"""
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
        *(("do-not-monitor", 1),
          ("down-critical", 3),
          ("down-warning", 2))
    )


_W2kConfigDirTimeMonitor_Type.__name__ = "Integer32"
_W2kConfigDirTimeMonitor_Object = MibScalar
w2kConfigDirTimeMonitor = _W2kConfigDirTimeMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 9, 8),
    _W2kConfigDirTimeMonitor_Type()
)
w2kConfigDirTimeMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigDirTimeMonitor.setStatus("mandatory")


class _W2kConfigDirSizeWarn_Type(DisplayString):
    """Custom type w2kConfigDirSizeWarn based on DisplayString"""
    defaultValue = OctetString("150%")


_W2kConfigDirSizeWarn_Object = MibScalar
w2kConfigDirSizeWarn = _W2kConfigDirSizeWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 9, 9),
    _W2kConfigDirSizeWarn_Type()
)
w2kConfigDirSizeWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigDirSizeWarn.setStatus("mandatory")


class _W2kConfigDirSizeCrit_Type(DisplayString):
    """Custom type w2kConfigDirSizeCrit based on DisplayString"""
    defaultValue = OctetString("200%")


_W2kConfigDirSizeCrit_Object = MibScalar
w2kConfigDirSizeCrit = _W2kConfigDirSizeCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 9, 10),
    _W2kConfigDirSizeCrit_Type()
)
w2kConfigDirSizeCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigDirSizeCrit.setStatus("mandatory")


class _W2kConfigDirSizeMonitor_Type(Integer32):
    """Custom type w2kConfigDirSizeMonitor based on Integer32"""
    defaultValue = 4

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
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_W2kConfigDirSizeMonitor_Type.__name__ = "Integer32"
_W2kConfigDirSizeMonitor_Object = MibScalar
w2kConfigDirSizeMonitor = _W2kConfigDirSizeMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 9, 11),
    _W2kConfigDirSizeMonitor_Type()
)
w2kConfigDirSizeMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigDirSizeMonitor.setStatus("mandatory")


class _W2kConfigDirSizeDWarn_Type(DisplayString):
    """Custom type w2kConfigDirSizeDWarn based on DisplayString"""
    defaultValue = OctetString("1%")


_W2kConfigDirSizeDWarn_Object = MibScalar
w2kConfigDirSizeDWarn = _W2kConfigDirSizeDWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 9, 12),
    _W2kConfigDirSizeDWarn_Type()
)
w2kConfigDirSizeDWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigDirSizeDWarn.setStatus("mandatory")


class _W2kConfigDirSizeDCrit_Type(DisplayString):
    """Custom type w2kConfigDirSizeDCrit based on DisplayString"""
    defaultValue = OctetString("2%")


_W2kConfigDirSizeDCrit_Object = MibScalar
w2kConfigDirSizeDCrit = _W2kConfigDirSizeDCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 9, 13),
    _W2kConfigDirSizeDCrit_Type()
)
w2kConfigDirSizeDCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigDirSizeDCrit.setStatus("mandatory")


class _W2kConfigDirSizeDMonitor_Type(Integer32):
    """Custom type w2kConfigDirSizeDMonitor based on Integer32"""
    defaultValue = 4

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
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_W2kConfigDirSizeDMonitor_Type.__name__ = "Integer32"
_W2kConfigDirSizeDMonitor_Object = MibScalar
w2kConfigDirSizeDMonitor = _W2kConfigDirSizeDMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 9, 14),
    _W2kConfigDirSizeDMonitor_Type()
)
w2kConfigDirSizeDMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigDirSizeDMonitor.setStatus("mandatory")


class _W2kConfigDirEntryWarn_Type(Integer32):
    """Custom type w2kConfigDirEntryWarn based on Integer32"""
    defaultValue = 5


_W2kConfigDirEntryWarn_Object = MibScalar
w2kConfigDirEntryWarn = _W2kConfigDirEntryWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 9, 15),
    _W2kConfigDirEntryWarn_Type()
)
w2kConfigDirEntryWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigDirEntryWarn.setStatus("mandatory")


class _W2kConfigDirEntryCrit_Type(Integer32):
    """Custom type w2kConfigDirEntryCrit based on Integer32"""
    defaultValue = 10


_W2kConfigDirEntryCrit_Object = MibScalar
w2kConfigDirEntryCrit = _W2kConfigDirEntryCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 9, 16),
    _W2kConfigDirEntryCrit_Type()
)
w2kConfigDirEntryCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigDirEntryCrit.setStatus("mandatory")


class _W2kConfigDirEntryMonitor_Type(Integer32):
    """Custom type w2kConfigDirEntryMonitor based on Integer32"""
    defaultValue = 4

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
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_W2kConfigDirEntryMonitor_Type.__name__ = "Integer32"
_W2kConfigDirEntryMonitor_Object = MibScalar
w2kConfigDirEntryMonitor = _W2kConfigDirEntryMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 9, 17),
    _W2kConfigDirEntryMonitor_Type()
)
w2kConfigDirEntryMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigDirEntryMonitor.setStatus("mandatory")


class _W2kConfigDirButton_Type(Integer32):
    """Custom type w2kConfigDirButton based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("add", 2),
          ("none", 1),
          ("remove", 3))
    )


_W2kConfigDirButton_Type.__name__ = "Integer32"
_W2kConfigDirButton_Object = MibScalar
w2kConfigDirButton = _W2kConfigDirButton_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 9, 18),
    _W2kConfigDirButton_Type()
)
w2kConfigDirButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigDirButton.setStatus("mandatory")
_W2kConfigFileGroup_ObjectIdentity = ObjectIdentity
w2kConfigFileGroup = _W2kConfigFileGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 10)
)


class _W2kConfigFilePollInterval_Type(Integer32):
    """Custom type w2kConfigFilePollInterval based on Integer32"""
    defaultValue = 120


_W2kConfigFilePollInterval_Object = MibScalar
w2kConfigFilePollInterval = _W2kConfigFilePollInterval_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 10, 1),
    _W2kConfigFilePollInterval_Type()
)
w2kConfigFilePollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigFilePollInterval.setStatus("mandatory")


class _W2kConfigFilePollMethod_Type(Integer32):
    """Custom type w2kConfigFilePollMethod based on Integer32"""
    defaultValue = 2

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
        *(("disabled", 1),
          ("poll-interval-and-query", 3),
          ("poll-interval-only", 2),
          ("query-only", 4))
    )


_W2kConfigFilePollMethod_Type.__name__ = "Integer32"
_W2kConfigFilePollMethod_Object = MibScalar
w2kConfigFilePollMethod = _W2kConfigFilePollMethod_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 10, 2),
    _W2kConfigFilePollMethod_Type()
)
w2kConfigFilePollMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigFilePollMethod.setStatus("mandatory")
_W2kConfigFileName_Type = DisplayString
_W2kConfigFileName_Object = MibScalar
w2kConfigFileName = _W2kConfigFileName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 10, 3),
    _W2kConfigFileName_Type()
)
w2kConfigFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigFileName.setStatus("mandatory")
_W2kConfigFileDescription_Type = DisplayString
_W2kConfigFileDescription_Object = MibScalar
w2kConfigFileDescription = _W2kConfigFileDescription_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 10, 4),
    _W2kConfigFileDescription_Type()
)
w2kConfigFileDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigFileDescription.setStatus("mandatory")


class _W2kConfigFileAggLag_Type(Integer32):
    """Custom type w2kConfigFileAggLag based on Integer32"""
    defaultValue = 1


_W2kConfigFileAggLag_Object = MibScalar
w2kConfigFileAggLag = _W2kConfigFileAggLag_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 10, 5),
    _W2kConfigFileAggLag_Type()
)
w2kConfigFileAggLag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigFileAggLag.setStatus("mandatory")


class _W2kConfigFileExist_Type(Integer32):
    """Custom type w2kConfigFileExist based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("should-exist", 1),
          ("should-not-exist", 2))
    )


_W2kConfigFileExist_Type.__name__ = "Integer32"
_W2kConfigFileExist_Object = MibScalar
w2kConfigFileExist = _W2kConfigFileExist_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 10, 6),
    _W2kConfigFileExist_Type()
)
w2kConfigFileExist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigFileExist.setStatus("mandatory")


class _W2kConfigFileExistMonitor_Type(Integer32):
    """Custom type w2kConfigFileExistMonitor based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("do-not-monitor", 1),
          ("down-critical", 3),
          ("down-warning", 2))
    )


_W2kConfigFileExistMonitor_Type.__name__ = "Integer32"
_W2kConfigFileExistMonitor_Object = MibScalar
w2kConfigFileExistMonitor = _W2kConfigFileExistMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 10, 7),
    _W2kConfigFileExistMonitor_Type()
)
w2kConfigFileExistMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigFileExistMonitor.setStatus("mandatory")


class _W2kConfigFileTimeMonitor_Type(Integer32):
    """Custom type w2kConfigFileTimeMonitor based on Integer32"""
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
        *(("do-not-monitor", 1),
          ("down-critical", 3),
          ("down-warning", 2))
    )


_W2kConfigFileTimeMonitor_Type.__name__ = "Integer32"
_W2kConfigFileTimeMonitor_Object = MibScalar
w2kConfigFileTimeMonitor = _W2kConfigFileTimeMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 10, 8),
    _W2kConfigFileTimeMonitor_Type()
)
w2kConfigFileTimeMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigFileTimeMonitor.setStatus("mandatory")


class _W2kConfigFileSizeWarn_Type(DisplayString):
    """Custom type w2kConfigFileSizeWarn based on DisplayString"""
    defaultValue = OctetString("150%")


_W2kConfigFileSizeWarn_Object = MibScalar
w2kConfigFileSizeWarn = _W2kConfigFileSizeWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 10, 9),
    _W2kConfigFileSizeWarn_Type()
)
w2kConfigFileSizeWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigFileSizeWarn.setStatus("mandatory")


class _W2kConfigFileSizeCrit_Type(DisplayString):
    """Custom type w2kConfigFileSizeCrit based on DisplayString"""
    defaultValue = OctetString("200%")


_W2kConfigFileSizeCrit_Object = MibScalar
w2kConfigFileSizeCrit = _W2kConfigFileSizeCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 10, 10),
    _W2kConfigFileSizeCrit_Type()
)
w2kConfigFileSizeCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigFileSizeCrit.setStatus("mandatory")


class _W2kConfigFileSizeMonitor_Type(Integer32):
    """Custom type w2kConfigFileSizeMonitor based on Integer32"""
    defaultValue = 4

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
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_W2kConfigFileSizeMonitor_Type.__name__ = "Integer32"
_W2kConfigFileSizeMonitor_Object = MibScalar
w2kConfigFileSizeMonitor = _W2kConfigFileSizeMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 10, 11),
    _W2kConfigFileSizeMonitor_Type()
)
w2kConfigFileSizeMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigFileSizeMonitor.setStatus("mandatory")


class _W2kConfigFileSizeDWarn_Type(DisplayString):
    """Custom type w2kConfigFileSizeDWarn based on DisplayString"""
    defaultValue = OctetString("1%")


_W2kConfigFileSizeDWarn_Object = MibScalar
w2kConfigFileSizeDWarn = _W2kConfigFileSizeDWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 10, 12),
    _W2kConfigFileSizeDWarn_Type()
)
w2kConfigFileSizeDWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigFileSizeDWarn.setStatus("mandatory")


class _W2kConfigFileSizeDCrit_Type(DisplayString):
    """Custom type w2kConfigFileSizeDCrit based on DisplayString"""
    defaultValue = OctetString("2%")


_W2kConfigFileSizeDCrit_Object = MibScalar
w2kConfigFileSizeDCrit = _W2kConfigFileSizeDCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 10, 13),
    _W2kConfigFileSizeDCrit_Type()
)
w2kConfigFileSizeDCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigFileSizeDCrit.setStatus("mandatory")


class _W2kConfigFileSizeDMonitor_Type(Integer32):
    """Custom type w2kConfigFileSizeDMonitor based on Integer32"""
    defaultValue = 4

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
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_W2kConfigFileSizeDMonitor_Type.__name__ = "Integer32"
_W2kConfigFileSizeDMonitor_Object = MibScalar
w2kConfigFileSizeDMonitor = _W2kConfigFileSizeDMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 10, 14),
    _W2kConfigFileSizeDMonitor_Type()
)
w2kConfigFileSizeDMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigFileSizeDMonitor.setStatus("mandatory")


class _W2kConfigFileButton_Type(Integer32):
    """Custom type w2kConfigFileButton based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("add", 2),
          ("none", 1),
          ("remove", 3))
    )


_W2kConfigFileButton_Type.__name__ = "Integer32"
_W2kConfigFileButton_Object = MibScalar
w2kConfigFileButton = _W2kConfigFileButton_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 10, 15),
    _W2kConfigFileButton_Type()
)
w2kConfigFileButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigFileButton.setStatus("mandatory")
_W2kConfigProcGroup_ObjectIdentity = ObjectIdentity
w2kConfigProcGroup = _W2kConfigProcGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 11)
)


class _W2kConfigProcPollInterval_Type(Integer32):
    """Custom type w2kConfigProcPollInterval based on Integer32"""
    defaultValue = 120


_W2kConfigProcPollInterval_Object = MibScalar
w2kConfigProcPollInterval = _W2kConfigProcPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 11, 1),
    _W2kConfigProcPollInterval_Type()
)
w2kConfigProcPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigProcPollInterval.setStatus("mandatory")


class _W2kConfigProcPollMethod_Type(Integer32):
    """Custom type w2kConfigProcPollMethod based on Integer32"""
    defaultValue = 2

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
        *(("disabled", 1),
          ("poll-interval-and-query", 3),
          ("poll-interval-only", 2),
          ("query-only", 4))
    )


_W2kConfigProcPollMethod_Type.__name__ = "Integer32"
_W2kConfigProcPollMethod_Object = MibScalar
w2kConfigProcPollMethod = _W2kConfigProcPollMethod_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 11, 2),
    _W2kConfigProcPollMethod_Type()
)
w2kConfigProcPollMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigProcPollMethod.setStatus("mandatory")
_W2kConfigProcProcName_Type = DisplayString
_W2kConfigProcProcName_Object = MibScalar
w2kConfigProcProcName = _W2kConfigProcProcName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 11, 3),
    _W2kConfigProcProcName_Type()
)
w2kConfigProcProcName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigProcProcName.setStatus("mandatory")
_W2kConfigProcPathName_Type = DisplayString
_W2kConfigProcPathName_Object = MibScalar
w2kConfigProcPathName = _W2kConfigProcPathName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 11, 4),
    _W2kConfigProcPathName_Type()
)
w2kConfigProcPathName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigProcPathName.setStatus("mandatory")
_W2kConfigProcUserName_Type = DisplayString
_W2kConfigProcUserName_Object = MibScalar
w2kConfigProcUserName = _W2kConfigProcUserName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 11, 5),
    _W2kConfigProcUserName_Type()
)
w2kConfigProcUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigProcUserName.setStatus("mandatory")
_W2kConfigProcDescription_Type = DisplayString
_W2kConfigProcDescription_Object = MibScalar
w2kConfigProcDescription = _W2kConfigProcDescription_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 11, 6),
    _W2kConfigProcDescription_Type()
)
w2kConfigProcDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigProcDescription.setStatus("mandatory")


class _W2kConfigProcAggLag_Type(Integer32):
    """Custom type w2kConfigProcAggLag based on Integer32"""
    defaultValue = 1


_W2kConfigProcAggLag_Object = MibScalar
w2kConfigProcAggLag = _W2kConfigProcAggLag_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 11, 7),
    _W2kConfigProcAggLag_Type()
)
w2kConfigProcAggLag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigProcAggLag.setStatus("mandatory")


class _W2kConfigProcInstMin_Type(Integer32):
    """Custom type w2kConfigProcInstMin based on Integer32"""
    defaultValue = 1


_W2kConfigProcInstMin_Object = MibScalar
w2kConfigProcInstMin = _W2kConfigProcInstMin_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 11, 8),
    _W2kConfigProcInstMin_Type()
)
w2kConfigProcInstMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigProcInstMin.setStatus("mandatory")


class _W2kConfigProcInstMax_Type(Integer32):
    """Custom type w2kConfigProcInstMax based on Integer32"""
    defaultValue = 1


_W2kConfigProcInstMax_Object = MibScalar
w2kConfigProcInstMax = _W2kConfigProcInstMax_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 11, 9),
    _W2kConfigProcInstMax_Type()
)
w2kConfigProcInstMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigProcInstMax.setStatus("mandatory")


class _W2kConfigProcInstMonitor_Type(Integer32):
    """Custom type w2kConfigProcInstMonitor based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("do-not-monitor", 1),
          ("down-critical", 3),
          ("down-warning", 2))
    )


_W2kConfigProcInstMonitor_Type.__name__ = "Integer32"
_W2kConfigProcInstMonitor_Object = MibScalar
w2kConfigProcInstMonitor = _W2kConfigProcInstMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 11, 10),
    _W2kConfigProcInstMonitor_Type()
)
w2kConfigProcInstMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigProcInstMonitor.setStatus("mandatory")


class _W2kConfigProcChildMin_Type(Integer32):
    """Custom type w2kConfigProcChildMin based on Integer32"""
    defaultValue = 0


_W2kConfigProcChildMin_Object = MibScalar
w2kConfigProcChildMin = _W2kConfigProcChildMin_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 11, 11),
    _W2kConfigProcChildMin_Type()
)
w2kConfigProcChildMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigProcChildMin.setStatus("mandatory")


class _W2kConfigProcChildMax_Type(Integer32):
    """Custom type w2kConfigProcChildMax based on Integer32"""
    defaultValue = 1


_W2kConfigProcChildMax_Object = MibScalar
w2kConfigProcChildMax = _W2kConfigProcChildMax_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 11, 12),
    _W2kConfigProcChildMax_Type()
)
w2kConfigProcChildMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigProcChildMax.setStatus("mandatory")


class _W2kConfigProcChildMonitor_Type(Integer32):
    """Custom type w2kConfigProcChildMonitor based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("do-not-monitor", 1),
          ("down-critical", 3),
          ("down-warning", 2))
    )


_W2kConfigProcChildMonitor_Type.__name__ = "Integer32"
_W2kConfigProcChildMonitor_Object = MibScalar
w2kConfigProcChildMonitor = _W2kConfigProcChildMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 11, 13),
    _W2kConfigProcChildMonitor_Type()
)
w2kConfigProcChildMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigProcChildMonitor.setStatus("mandatory")


class _W2kConfigProcThreadMin_Type(Integer32):
    """Custom type w2kConfigProcThreadMin based on Integer32"""
    defaultValue = 1


_W2kConfigProcThreadMin_Object = MibScalar
w2kConfigProcThreadMin = _W2kConfigProcThreadMin_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 11, 14),
    _W2kConfigProcThreadMin_Type()
)
w2kConfigProcThreadMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigProcThreadMin.setStatus("mandatory")


class _W2kConfigProcThreadMax_Type(Integer32):
    """Custom type w2kConfigProcThreadMax based on Integer32"""
    defaultValue = 10


_W2kConfigProcThreadMax_Object = MibScalar
w2kConfigProcThreadMax = _W2kConfigProcThreadMax_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 11, 15),
    _W2kConfigProcThreadMax_Type()
)
w2kConfigProcThreadMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigProcThreadMax.setStatus("mandatory")


class _W2kConfigProcThreadMonitor_Type(Integer32):
    """Custom type w2kConfigProcThreadMonitor based on Integer32"""
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
        *(("do-not-monitor", 1),
          ("down-critical", 3),
          ("down-warning", 2))
    )


_W2kConfigProcThreadMonitor_Type.__name__ = "Integer32"
_W2kConfigProcThreadMonitor_Object = MibScalar
w2kConfigProcThreadMonitor = _W2kConfigProcThreadMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 11, 16),
    _W2kConfigProcThreadMonitor_Type()
)
w2kConfigProcThreadMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigProcThreadMonitor.setStatus("mandatory")


class _W2kConfigProcMemoryWarn_Type(Integer32):
    """Custom type w2kConfigProcMemoryWarn based on Integer32"""
    defaultValue = 20000


_W2kConfigProcMemoryWarn_Object = MibScalar
w2kConfigProcMemoryWarn = _W2kConfigProcMemoryWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 11, 17),
    _W2kConfigProcMemoryWarn_Type()
)
w2kConfigProcMemoryWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigProcMemoryWarn.setStatus("mandatory")


class _W2kConfigProcMemoryCrit_Type(Integer32):
    """Custom type w2kConfigProcMemoryCrit based on Integer32"""
    defaultValue = 40000


_W2kConfigProcMemoryCrit_Object = MibScalar
w2kConfigProcMemoryCrit = _W2kConfigProcMemoryCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 11, 18),
    _W2kConfigProcMemoryCrit_Type()
)
w2kConfigProcMemoryCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigProcMemoryCrit.setStatus("mandatory")


class _W2kConfigProcMemoryMonitor_Type(Integer32):
    """Custom type w2kConfigProcMemoryMonitor based on Integer32"""
    defaultValue = 4

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
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_W2kConfigProcMemoryMonitor_Type.__name__ = "Integer32"
_W2kConfigProcMemoryMonitor_Object = MibScalar
w2kConfigProcMemoryMonitor = _W2kConfigProcMemoryMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 11, 19),
    _W2kConfigProcMemoryMonitor_Type()
)
w2kConfigProcMemoryMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigProcMemoryMonitor.setStatus("mandatory")


class _W2kConfigProcCpuWarn_Type(Integer32):
    """Custom type w2kConfigProcCpuWarn based on Integer32"""
    defaultValue = 10


_W2kConfigProcCpuWarn_Object = MibScalar
w2kConfigProcCpuWarn = _W2kConfigProcCpuWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 11, 20),
    _W2kConfigProcCpuWarn_Type()
)
w2kConfigProcCpuWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigProcCpuWarn.setStatus("mandatory")


class _W2kConfigProcCpuCrit_Type(Integer32):
    """Custom type w2kConfigProcCpuCrit based on Integer32"""
    defaultValue = 20


_W2kConfigProcCpuCrit_Object = MibScalar
w2kConfigProcCpuCrit = _W2kConfigProcCpuCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 11, 21),
    _W2kConfigProcCpuCrit_Type()
)
w2kConfigProcCpuCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigProcCpuCrit.setStatus("mandatory")


class _W2kConfigProcCpuMonitor_Type(Integer32):
    """Custom type w2kConfigProcCpuMonitor based on Integer32"""
    defaultValue = 4

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
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_W2kConfigProcCpuMonitor_Type.__name__ = "Integer32"
_W2kConfigProcCpuMonitor_Object = MibScalar
w2kConfigProcCpuMonitor = _W2kConfigProcCpuMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 11, 22),
    _W2kConfigProcCpuMonitor_Type()
)
w2kConfigProcCpuMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigProcCpuMonitor.setStatus("mandatory")


class _W2kConfigProcButton_Type(Integer32):
    """Custom type w2kConfigProcButton based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("add", 2),
          ("none", 1),
          ("remove", 3))
    )


_W2kConfigProcButton_Type.__name__ = "Integer32"
_W2kConfigProcButton_Object = MibScalar
w2kConfigProcButton = _W2kConfigProcButton_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 11, 23),
    _W2kConfigProcButton_Type()
)
w2kConfigProcButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigProcButton.setStatus("mandatory")
_W2kConfigSrvcGroup_ObjectIdentity = ObjectIdentity
w2kConfigSrvcGroup = _W2kConfigSrvcGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 12)
)


class _W2kConfigSrvcPollInterval_Type(Integer32):
    """Custom type w2kConfigSrvcPollInterval based on Integer32"""
    defaultValue = 120


_W2kConfigSrvcPollInterval_Object = MibScalar
w2kConfigSrvcPollInterval = _W2kConfigSrvcPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 12, 1),
    _W2kConfigSrvcPollInterval_Type()
)
w2kConfigSrvcPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigSrvcPollInterval.setStatus("mandatory")


class _W2kConfigSrvcPollMethod_Type(Integer32):
    """Custom type w2kConfigSrvcPollMethod based on Integer32"""
    defaultValue = 2

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
        *(("disabled", 1),
          ("poll-interval-and-query", 3),
          ("poll-interval-only", 2),
          ("query-only", 4))
    )


_W2kConfigSrvcPollMethod_Type.__name__ = "Integer32"
_W2kConfigSrvcPollMethod_Object = MibScalar
w2kConfigSrvcPollMethod = _W2kConfigSrvcPollMethod_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 12, 2),
    _W2kConfigSrvcPollMethod_Type()
)
w2kConfigSrvcPollMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigSrvcPollMethod.setStatus("mandatory")


class _W2kConfigSrvcAutoPollInterval_Type(Integer32):
    """Custom type w2kConfigSrvcAutoPollInterval based on Integer32"""
    defaultValue = 60


_W2kConfigSrvcAutoPollInterval_Object = MibScalar
w2kConfigSrvcAutoPollInterval = _W2kConfigSrvcAutoPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 12, 3),
    _W2kConfigSrvcAutoPollInterval_Type()
)
w2kConfigSrvcAutoPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigSrvcAutoPollInterval.setStatus("mandatory")
_W2kConfigSrvcName_Type = DisplayString
_W2kConfigSrvcName_Object = MibScalar
w2kConfigSrvcName = _W2kConfigSrvcName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 12, 4),
    _W2kConfigSrvcName_Type()
)
w2kConfigSrvcName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigSrvcName.setStatus("mandatory")
_W2kConfigSrvcDescription_Type = DisplayString
_W2kConfigSrvcDescription_Object = MibScalar
w2kConfigSrvcDescription = _W2kConfigSrvcDescription_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 12, 5),
    _W2kConfigSrvcDescription_Type()
)
w2kConfigSrvcDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigSrvcDescription.setStatus("mandatory")


class _W2kConfigSrvcAggLag_Type(Integer32):
    """Custom type w2kConfigSrvcAggLag based on Integer32"""
    defaultValue = 1


_W2kConfigSrvcAggLag_Object = MibScalar
w2kConfigSrvcAggLag = _W2kConfigSrvcAggLag_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 12, 6),
    _W2kConfigSrvcAggLag_Type()
)
w2kConfigSrvcAggLag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigSrvcAggLag.setStatus("mandatory")


class _W2kConfigSrvcExist_Type(Integer32):
    """Custom type w2kConfigSrvcExist based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("should-exist", 1),
          ("should-not-exist", 2))
    )


_W2kConfigSrvcExist_Type.__name__ = "Integer32"
_W2kConfigSrvcExist_Object = MibScalar
w2kConfigSrvcExist = _W2kConfigSrvcExist_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 12, 7),
    _W2kConfigSrvcExist_Type()
)
w2kConfigSrvcExist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigSrvcExist.setStatus("mandatory")


class _W2kConfigSrvcExistMonitor_Type(Integer32):
    """Custom type w2kConfigSrvcExistMonitor based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("do-not-monitor", 1),
          ("down-critical", 3),
          ("down-warning", 2))
    )


_W2kConfigSrvcExistMonitor_Type.__name__ = "Integer32"
_W2kConfigSrvcExistMonitor_Object = MibScalar
w2kConfigSrvcExistMonitor = _W2kConfigSrvcExistMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 12, 8),
    _W2kConfigSrvcExistMonitor_Type()
)
w2kConfigSrvcExistMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigSrvcExistMonitor.setStatus("mandatory")


class _W2kConfigSrvcActive_Type(Integer32):
    """Custom type w2kConfigSrvcActive based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("should-be-active", 1),
          ("should-not-be-active", 2))
    )


_W2kConfigSrvcActive_Type.__name__ = "Integer32"
_W2kConfigSrvcActive_Object = MibScalar
w2kConfigSrvcActive = _W2kConfigSrvcActive_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 12, 9),
    _W2kConfigSrvcActive_Type()
)
w2kConfigSrvcActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigSrvcActive.setStatus("mandatory")


class _W2kConfigSrvcActiveMonitor_Type(Integer32):
    """Custom type w2kConfigSrvcActiveMonitor based on Integer32"""
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
        *(("do-not-monitor", 1),
          ("down-critical", 3),
          ("down-warning", 2))
    )


_W2kConfigSrvcActiveMonitor_Type.__name__ = "Integer32"
_W2kConfigSrvcActiveMonitor_Object = MibScalar
w2kConfigSrvcActiveMonitor = _W2kConfigSrvcActiveMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 12, 10),
    _W2kConfigSrvcActiveMonitor_Type()
)
w2kConfigSrvcActiveMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigSrvcActiveMonitor.setStatus("mandatory")
_W2kConfigSrvcAutoTableWatcherName_Type = DisplayString
_W2kConfigSrvcAutoTableWatcherName_Object = MibScalar
w2kConfigSrvcAutoTableWatcherName = _W2kConfigSrvcAutoTableWatcherName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 12, 11),
    _W2kConfigSrvcAutoTableWatcherName_Type()
)
w2kConfigSrvcAutoTableWatcherName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigSrvcAutoTableWatcherName.setStatus("mandatory")


class _W2kConfigSrvcButton_Type(Integer32):
    """Custom type w2kConfigSrvcButton based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("add", 2),
          ("add-auto", 4),
          ("none", 1),
          ("remove", 3),
          ("remove-auto", 5))
    )


_W2kConfigSrvcButton_Type.__name__ = "Integer32"
_W2kConfigSrvcButton_Object = MibScalar
w2kConfigSrvcButton = _W2kConfigSrvcButton_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 12, 12),
    _W2kConfigSrvcButton_Type()
)
w2kConfigSrvcButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigSrvcButton.setStatus("mandatory")
_W2kConfigSrvcAutoTable_Object = MibTable
w2kConfigSrvcAutoTable = _W2kConfigSrvcAutoTable_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 12, 13)
)
if mibBuilder.loadTexts:
    w2kConfigSrvcAutoTable.setStatus("mandatory")
_W2kConfigSrvcAutoEntry_Object = MibTableRow
w2kConfigSrvcAutoEntry = _W2kConfigSrvcAutoEntry_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 12, 13, 1)
)
w2kConfigSrvcAutoEntry.setIndexNames(
    (0, "CA-W2KOS-MIB", "w2kConfigSrvcAutoWatcherName"),
)
if mibBuilder.loadTexts:
    w2kConfigSrvcAutoEntry.setStatus("mandatory")
_W2kConfigSrvcAutoWatcherName_Type = DisplayString
_W2kConfigSrvcAutoWatcherName_Object = MibTableColumn
w2kConfigSrvcAutoWatcherName = _W2kConfigSrvcAutoWatcherName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 12, 13, 1, 1),
    _W2kConfigSrvcAutoWatcherName_Type()
)
w2kConfigSrvcAutoWatcherName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kConfigSrvcAutoWatcherName.setStatus("mandatory")
_W2kConfigSrvcAutoName_Type = DisplayString
_W2kConfigSrvcAutoName_Object = MibTableColumn
w2kConfigSrvcAutoName = _W2kConfigSrvcAutoName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 12, 13, 1, 2),
    _W2kConfigSrvcAutoName_Type()
)
w2kConfigSrvcAutoName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigSrvcAutoName.setStatus("mandatory")
_W2kConfigSrvcAutoDescription_Type = DisplayString
_W2kConfigSrvcAutoDescription_Object = MibTableColumn
w2kConfigSrvcAutoDescription = _W2kConfigSrvcAutoDescription_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 12, 13, 1, 3),
    _W2kConfigSrvcAutoDescription_Type()
)
w2kConfigSrvcAutoDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigSrvcAutoDescription.setStatus("mandatory")
_W2kConfigSrvcAutoAggLag_Type = Integer32
_W2kConfigSrvcAutoAggLag_Object = MibTableColumn
w2kConfigSrvcAutoAggLag = _W2kConfigSrvcAutoAggLag_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 12, 13, 1, 4),
    _W2kConfigSrvcAutoAggLag_Type()
)
w2kConfigSrvcAutoAggLag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigSrvcAutoAggLag.setStatus("mandatory")


class _W2kConfigSrvcAutoExist_Type(Integer32):
    """Custom type w2kConfigSrvcAutoExist based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("should-exist", 1),
          ("should-not-exist", 2))
    )


_W2kConfigSrvcAutoExist_Type.__name__ = "Integer32"
_W2kConfigSrvcAutoExist_Object = MibTableColumn
w2kConfigSrvcAutoExist = _W2kConfigSrvcAutoExist_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 12, 13, 1, 5),
    _W2kConfigSrvcAutoExist_Type()
)
w2kConfigSrvcAutoExist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigSrvcAutoExist.setStatus("mandatory")


class _W2kConfigSrvcAutoExistMonitor_Type(Integer32):
    """Custom type w2kConfigSrvcAutoExistMonitor based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("do-not-monitor", 1),
          ("down-critical", 3),
          ("down-warning", 2))
    )


_W2kConfigSrvcAutoExistMonitor_Type.__name__ = "Integer32"
_W2kConfigSrvcAutoExistMonitor_Object = MibTableColumn
w2kConfigSrvcAutoExistMonitor = _W2kConfigSrvcAutoExistMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 12, 13, 1, 6),
    _W2kConfigSrvcAutoExistMonitor_Type()
)
w2kConfigSrvcAutoExistMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigSrvcAutoExistMonitor.setStatus("mandatory")


class _W2kConfigSrvcAutoActive_Type(Integer32):
    """Custom type w2kConfigSrvcAutoActive based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("should-be-active", 1),
          ("should-not-be-active", 2))
    )


_W2kConfigSrvcAutoActive_Type.__name__ = "Integer32"
_W2kConfigSrvcAutoActive_Object = MibTableColumn
w2kConfigSrvcAutoActive = _W2kConfigSrvcAutoActive_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 12, 13, 1, 7),
    _W2kConfigSrvcAutoActive_Type()
)
w2kConfigSrvcAutoActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigSrvcAutoActive.setStatus("mandatory")


class _W2kConfigSrvcAutoActiveMonitor_Type(Integer32):
    """Custom type w2kConfigSrvcAutoActiveMonitor based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("do-not-monitor", 1),
          ("down-critical", 3),
          ("down-warning", 2))
    )


_W2kConfigSrvcAutoActiveMonitor_Type.__name__ = "Integer32"
_W2kConfigSrvcAutoActiveMonitor_Object = MibTableColumn
w2kConfigSrvcAutoActiveMonitor = _W2kConfigSrvcAutoActiveMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 12, 13, 1, 8),
    _W2kConfigSrvcAutoActiveMonitor_Type()
)
w2kConfigSrvcAutoActiveMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigSrvcAutoActiveMonitor.setStatus("mandatory")


class _W2kConfigSrvcAutoButton_Type(Integer32):
    """Custom type w2kConfigSrvcAutoButton based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("remove", 2))
    )


_W2kConfigSrvcAutoButton_Type.__name__ = "Integer32"
_W2kConfigSrvcAutoButton_Object = MibTableColumn
w2kConfigSrvcAutoButton = _W2kConfigSrvcAutoButton_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 12, 13, 1, 9),
    _W2kConfigSrvcAutoButton_Type()
)
w2kConfigSrvcAutoButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigSrvcAutoButton.setStatus("mandatory")
_W2kConfigJobGroup_ObjectIdentity = ObjectIdentity
w2kConfigJobGroup = _W2kConfigJobGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 13)
)


class _W2kConfigJobPollInterval_Type(Integer32):
    """Custom type w2kConfigJobPollInterval based on Integer32"""
    defaultValue = 120


_W2kConfigJobPollInterval_Object = MibScalar
w2kConfigJobPollInterval = _W2kConfigJobPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 13, 1),
    _W2kConfigJobPollInterval_Type()
)
w2kConfigJobPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigJobPollInterval.setStatus("mandatory")


class _W2kConfigJobPollMethod_Type(Integer32):
    """Custom type w2kConfigJobPollMethod based on Integer32"""
    defaultValue = 2

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
        *(("disabled", 1),
          ("poll-interval-and-query", 3),
          ("poll-interval-only", 2),
          ("query-only", 4))
    )


_W2kConfigJobPollMethod_Type.__name__ = "Integer32"
_W2kConfigJobPollMethod_Object = MibScalar
w2kConfigJobPollMethod = _W2kConfigJobPollMethod_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 13, 2),
    _W2kConfigJobPollMethod_Type()
)
w2kConfigJobPollMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigJobPollMethod.setStatus("mandatory")
_W2kConfigJobName_Type = DisplayString
_W2kConfigJobName_Object = MibScalar
w2kConfigJobName = _W2kConfigJobName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 13, 3),
    _W2kConfigJobName_Type()
)
w2kConfigJobName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigJobName.setStatus("mandatory")
_W2kConfigJobDescription_Type = DisplayString
_W2kConfigJobDescription_Object = MibScalar
w2kConfigJobDescription = _W2kConfigJobDescription_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 13, 4),
    _W2kConfigJobDescription_Type()
)
w2kConfigJobDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigJobDescription.setStatus("mandatory")


class _W2kConfigJobAggLag_Type(Integer32):
    """Custom type w2kConfigJobAggLag based on Integer32"""
    defaultValue = 1


_W2kConfigJobAggLag_Object = MibScalar
w2kConfigJobAggLag = _W2kConfigJobAggLag_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 13, 5),
    _W2kConfigJobAggLag_Type()
)
w2kConfigJobAggLag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigJobAggLag.setStatus("mandatory")


class _W2kConfigJobExist_Type(Integer32):
    """Custom type w2kConfigJobExist based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("should-exist", 1),
          ("should-not-exist", 2))
    )


_W2kConfigJobExist_Type.__name__ = "Integer32"
_W2kConfigJobExist_Object = MibScalar
w2kConfigJobExist = _W2kConfigJobExist_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 13, 6),
    _W2kConfigJobExist_Type()
)
w2kConfigJobExist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigJobExist.setStatus("mandatory")


class _W2kConfigJobExistMonitor_Type(Integer32):
    """Custom type w2kConfigJobExistMonitor based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("do-not-monitor", 1),
          ("down-critical", 3),
          ("down-warning", 2))
    )


_W2kConfigJobExistMonitor_Type.__name__ = "Integer32"
_W2kConfigJobExistMonitor_Object = MibScalar
w2kConfigJobExistMonitor = _W2kConfigJobExistMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 13, 7),
    _W2kConfigJobExistMonitor_Type()
)
w2kConfigJobExistMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigJobExistMonitor.setStatus("mandatory")


class _W2kConfigJobProcessMin_Type(Integer32):
    """Custom type w2kConfigJobProcessMin based on Integer32"""
    defaultValue = 1


_W2kConfigJobProcessMin_Object = MibScalar
w2kConfigJobProcessMin = _W2kConfigJobProcessMin_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 13, 8),
    _W2kConfigJobProcessMin_Type()
)
w2kConfigJobProcessMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigJobProcessMin.setStatus("mandatory")


class _W2kConfigJobProcessMax_Type(Integer32):
    """Custom type w2kConfigJobProcessMax based on Integer32"""
    defaultValue = 10


_W2kConfigJobProcessMax_Object = MibScalar
w2kConfigJobProcessMax = _W2kConfigJobProcessMax_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 13, 9),
    _W2kConfigJobProcessMax_Type()
)
w2kConfigJobProcessMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigJobProcessMax.setStatus("mandatory")


class _W2kConfigJobProcessMonitor_Type(Integer32):
    """Custom type w2kConfigJobProcessMonitor based on Integer32"""
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
        *(("do-not-monitor", 1),
          ("down-critical", 3),
          ("down-warning", 2))
    )


_W2kConfigJobProcessMonitor_Type.__name__ = "Integer32"
_W2kConfigJobProcessMonitor_Object = MibScalar
w2kConfigJobProcessMonitor = _W2kConfigJobProcessMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 13, 10),
    _W2kConfigJobProcessMonitor_Type()
)
w2kConfigJobProcessMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigJobProcessMonitor.setStatus("mandatory")


class _W2kConfigJobCpuWarn_Type(Integer32):
    """Custom type w2kConfigJobCpuWarn based on Integer32"""
    defaultValue = 10


_W2kConfigJobCpuWarn_Object = MibScalar
w2kConfigJobCpuWarn = _W2kConfigJobCpuWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 13, 11),
    _W2kConfigJobCpuWarn_Type()
)
w2kConfigJobCpuWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigJobCpuWarn.setStatus("mandatory")


class _W2kConfigJobCpuCrit_Type(Integer32):
    """Custom type w2kConfigJobCpuCrit based on Integer32"""
    defaultValue = 20


_W2kConfigJobCpuCrit_Object = MibScalar
w2kConfigJobCpuCrit = _W2kConfigJobCpuCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 13, 12),
    _W2kConfigJobCpuCrit_Type()
)
w2kConfigJobCpuCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigJobCpuCrit.setStatus("mandatory")


class _W2kConfigJobCpuMonitor_Type(Integer32):
    """Custom type w2kConfigJobCpuMonitor based on Integer32"""
    defaultValue = 4

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
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_W2kConfigJobCpuMonitor_Type.__name__ = "Integer32"
_W2kConfigJobCpuMonitor_Object = MibScalar
w2kConfigJobCpuMonitor = _W2kConfigJobCpuMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 13, 13),
    _W2kConfigJobCpuMonitor_Type()
)
w2kConfigJobCpuMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigJobCpuMonitor.setStatus("mandatory")


class _W2kConfigJobButton_Type(Integer32):
    """Custom type w2kConfigJobButton based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("add", 2),
          ("none", 1),
          ("remove", 3))
    )


_W2kConfigJobButton_Type.__name__ = "Integer32"
_W2kConfigJobButton_Object = MibScalar
w2kConfigJobButton = _W2kConfigJobButton_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 13, 14),
    _W2kConfigJobButton_Type()
)
w2kConfigJobButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigJobButton.setStatus("mandatory")
_W2kConfigSessGroup_ObjectIdentity = ObjectIdentity
w2kConfigSessGroup = _W2kConfigSessGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 14)
)


class _W2kConfigSessPollInterval_Type(Integer32):
    """Custom type w2kConfigSessPollInterval based on Integer32"""
    defaultValue = 120


_W2kConfigSessPollInterval_Object = MibScalar
w2kConfigSessPollInterval = _W2kConfigSessPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 14, 1),
    _W2kConfigSessPollInterval_Type()
)
w2kConfigSessPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigSessPollInterval.setStatus("mandatory")


class _W2kConfigSessPollMethod_Type(Integer32):
    """Custom type w2kConfigSessPollMethod based on Integer32"""
    defaultValue = 2

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
        *(("disabled", 1),
          ("poll-interval-and-query", 3),
          ("poll-interval-only", 2),
          ("query-only", 4))
    )


_W2kConfigSessPollMethod_Type.__name__ = "Integer32"
_W2kConfigSessPollMethod_Object = MibScalar
w2kConfigSessPollMethod = _W2kConfigSessPollMethod_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 14, 2),
    _W2kConfigSessPollMethod_Type()
)
w2kConfigSessPollMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigSessPollMethod.setStatus("mandatory")
_W2kConfigSessClientName_Type = DisplayString
_W2kConfigSessClientName_Object = MibScalar
w2kConfigSessClientName = _W2kConfigSessClientName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 14, 3),
    _W2kConfigSessClientName_Type()
)
w2kConfigSessClientName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigSessClientName.setStatus("mandatory")
_W2kConfigSessUserName_Type = DisplayString
_W2kConfigSessUserName_Object = MibScalar
w2kConfigSessUserName = _W2kConfigSessUserName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 14, 4),
    _W2kConfigSessUserName_Type()
)
w2kConfigSessUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigSessUserName.setStatus("mandatory")
_W2kConfigSessDescription_Type = DisplayString
_W2kConfigSessDescription_Object = MibScalar
w2kConfigSessDescription = _W2kConfigSessDescription_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 14, 5),
    _W2kConfigSessDescription_Type()
)
w2kConfigSessDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigSessDescription.setStatus("mandatory")


class _W2kConfigSessAggLag_Type(Integer32):
    """Custom type w2kConfigSessAggLag based on Integer32"""
    defaultValue = 1


_W2kConfigSessAggLag_Object = MibScalar
w2kConfigSessAggLag = _W2kConfigSessAggLag_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 14, 6),
    _W2kConfigSessAggLag_Type()
)
w2kConfigSessAggLag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigSessAggLag.setStatus("mandatory")


class _W2kConfigSessInstMin_Type(Integer32):
    """Custom type w2kConfigSessInstMin based on Integer32"""
    defaultValue = 0


_W2kConfigSessInstMin_Object = MibScalar
w2kConfigSessInstMin = _W2kConfigSessInstMin_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 14, 7),
    _W2kConfigSessInstMin_Type()
)
w2kConfigSessInstMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigSessInstMin.setStatus("mandatory")


class _W2kConfigSessInstMax_Type(Integer32):
    """Custom type w2kConfigSessInstMax based on Integer32"""
    defaultValue = 2


_W2kConfigSessInstMax_Object = MibScalar
w2kConfigSessInstMax = _W2kConfigSessInstMax_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 14, 8),
    _W2kConfigSessInstMax_Type()
)
w2kConfigSessInstMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigSessInstMax.setStatus("mandatory")


class _W2kConfigSessInstMonitor_Type(Integer32):
    """Custom type w2kConfigSessInstMonitor based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("do-not-monitor", 1),
          ("down-critical", 3),
          ("down-warning", 2))
    )


_W2kConfigSessInstMonitor_Type.__name__ = "Integer32"
_W2kConfigSessInstMonitor_Object = MibScalar
w2kConfigSessInstMonitor = _W2kConfigSessInstMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 14, 9),
    _W2kConfigSessInstMonitor_Type()
)
w2kConfigSessInstMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigSessInstMonitor.setStatus("mandatory")


class _W2kConfigSessMemoryWarn_Type(Integer32):
    """Custom type w2kConfigSessMemoryWarn based on Integer32"""
    defaultValue = 20000


_W2kConfigSessMemoryWarn_Object = MibScalar
w2kConfigSessMemoryWarn = _W2kConfigSessMemoryWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 14, 10),
    _W2kConfigSessMemoryWarn_Type()
)
w2kConfigSessMemoryWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigSessMemoryWarn.setStatus("mandatory")


class _W2kConfigSessMemoryCrit_Type(Integer32):
    """Custom type w2kConfigSessMemoryCrit based on Integer32"""
    defaultValue = 40000


_W2kConfigSessMemoryCrit_Object = MibScalar
w2kConfigSessMemoryCrit = _W2kConfigSessMemoryCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 14, 11),
    _W2kConfigSessMemoryCrit_Type()
)
w2kConfigSessMemoryCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigSessMemoryCrit.setStatus("mandatory")


class _W2kConfigSessMemoryMonitor_Type(Integer32):
    """Custom type w2kConfigSessMemoryMonitor based on Integer32"""
    defaultValue = 4

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
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_W2kConfigSessMemoryMonitor_Type.__name__ = "Integer32"
_W2kConfigSessMemoryMonitor_Object = MibScalar
w2kConfigSessMemoryMonitor = _W2kConfigSessMemoryMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 14, 12),
    _W2kConfigSessMemoryMonitor_Type()
)
w2kConfigSessMemoryMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigSessMemoryMonitor.setStatus("mandatory")


class _W2kConfigSessCpuWarn_Type(Integer32):
    """Custom type w2kConfigSessCpuWarn based on Integer32"""
    defaultValue = 10


_W2kConfigSessCpuWarn_Object = MibScalar
w2kConfigSessCpuWarn = _W2kConfigSessCpuWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 14, 13),
    _W2kConfigSessCpuWarn_Type()
)
w2kConfigSessCpuWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigSessCpuWarn.setStatus("mandatory")


class _W2kConfigSessCpuCrit_Type(Integer32):
    """Custom type w2kConfigSessCpuCrit based on Integer32"""
    defaultValue = 20


_W2kConfigSessCpuCrit_Object = MibScalar
w2kConfigSessCpuCrit = _W2kConfigSessCpuCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 14, 14),
    _W2kConfigSessCpuCrit_Type()
)
w2kConfigSessCpuCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigSessCpuCrit.setStatus("mandatory")


class _W2kConfigSessCpuMonitor_Type(Integer32):
    """Custom type w2kConfigSessCpuMonitor based on Integer32"""
    defaultValue = 4

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
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_W2kConfigSessCpuMonitor_Type.__name__ = "Integer32"
_W2kConfigSessCpuMonitor_Object = MibScalar
w2kConfigSessCpuMonitor = _W2kConfigSessCpuMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 14, 15),
    _W2kConfigSessCpuMonitor_Type()
)
w2kConfigSessCpuMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigSessCpuMonitor.setStatus("mandatory")


class _W2kConfigSessButton_Type(Integer32):
    """Custom type w2kConfigSessButton based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("add", 2),
          ("none", 1),
          ("remove", 3))
    )


_W2kConfigSessButton_Type.__name__ = "Integer32"
_W2kConfigSessButton_Object = MibScalar
w2kConfigSessButton = _W2kConfigSessButton_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 14, 16),
    _W2kConfigSessButton_Type()
)
w2kConfigSessButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigSessButton.setStatus("mandatory")
_W2kConfigPrnGroup_ObjectIdentity = ObjectIdentity
w2kConfigPrnGroup = _W2kConfigPrnGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 15)
)


class _W2kConfigPrnPollInterval_Type(Integer32):
    """Custom type w2kConfigPrnPollInterval based on Integer32"""
    defaultValue = 120


_W2kConfigPrnPollInterval_Object = MibScalar
w2kConfigPrnPollInterval = _W2kConfigPrnPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 15, 1),
    _W2kConfigPrnPollInterval_Type()
)
w2kConfigPrnPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigPrnPollInterval.setStatus("mandatory")


class _W2kConfigPrnPollMethod_Type(Integer32):
    """Custom type w2kConfigPrnPollMethod based on Integer32"""
    defaultValue = 2

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
        *(("disabled", 1),
          ("poll-interval-and-query", 3),
          ("poll-interval-only", 2),
          ("query-only", 4))
    )


_W2kConfigPrnPollMethod_Type.__name__ = "Integer32"
_W2kConfigPrnPollMethod_Object = MibScalar
w2kConfigPrnPollMethod = _W2kConfigPrnPollMethod_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 15, 2),
    _W2kConfigPrnPollMethod_Type()
)
w2kConfigPrnPollMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigPrnPollMethod.setStatus("mandatory")


class _W2kConfigPrnAutoPollInterval_Type(Integer32):
    """Custom type w2kConfigPrnAutoPollInterval based on Integer32"""
    defaultValue = 60


_W2kConfigPrnAutoPollInterval_Object = MibScalar
w2kConfigPrnAutoPollInterval = _W2kConfigPrnAutoPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 15, 3),
    _W2kConfigPrnAutoPollInterval_Type()
)
w2kConfigPrnAutoPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigPrnAutoPollInterval.setStatus("mandatory")
_W2kConfigPrnName_Type = DisplayString
_W2kConfigPrnName_Object = MibScalar
w2kConfigPrnName = _W2kConfigPrnName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 15, 4),
    _W2kConfigPrnName_Type()
)
w2kConfigPrnName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigPrnName.setStatus("mandatory")
_W2kConfigPrnDescription_Type = DisplayString
_W2kConfigPrnDescription_Object = MibScalar
w2kConfigPrnDescription = _W2kConfigPrnDescription_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 15, 5),
    _W2kConfigPrnDescription_Type()
)
w2kConfigPrnDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigPrnDescription.setStatus("mandatory")


class _W2kConfigPrnAggLag_Type(Integer32):
    """Custom type w2kConfigPrnAggLag based on Integer32"""
    defaultValue = 1


_W2kConfigPrnAggLag_Object = MibScalar
w2kConfigPrnAggLag = _W2kConfigPrnAggLag_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 15, 6),
    _W2kConfigPrnAggLag_Type()
)
w2kConfigPrnAggLag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigPrnAggLag.setStatus("mandatory")


class _W2kConfigPrnEventMonitor_Type(Integer32):
    """Custom type w2kConfigPrnEventMonitor based on Integer32"""
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
        *(("do-not-monitor", 1),
          ("down-critical", 3),
          ("down-warning", 2))
    )


_W2kConfigPrnEventMonitor_Type.__name__ = "Integer32"
_W2kConfigPrnEventMonitor_Object = MibScalar
w2kConfigPrnEventMonitor = _W2kConfigPrnEventMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 15, 7),
    _W2kConfigPrnEventMonitor_Type()
)
w2kConfigPrnEventMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigPrnEventMonitor.setStatus("mandatory")


class _W2kConfigPrnQueueWarn_Type(Integer32):
    """Custom type w2kConfigPrnQueueWarn based on Integer32"""
    defaultValue = 5


_W2kConfigPrnQueueWarn_Object = MibScalar
w2kConfigPrnQueueWarn = _W2kConfigPrnQueueWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 15, 8),
    _W2kConfigPrnQueueWarn_Type()
)
w2kConfigPrnQueueWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigPrnQueueWarn.setStatus("mandatory")


class _W2kConfigPrnQueueCrit_Type(Integer32):
    """Custom type w2kConfigPrnQueueCrit based on Integer32"""
    defaultValue = 10


_W2kConfigPrnQueueCrit_Object = MibScalar
w2kConfigPrnQueueCrit = _W2kConfigPrnQueueCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 15, 9),
    _W2kConfigPrnQueueCrit_Type()
)
w2kConfigPrnQueueCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigPrnQueueCrit.setStatus("mandatory")


class _W2kConfigPrnQueueMonitor_Type(Integer32):
    """Custom type w2kConfigPrnQueueMonitor based on Integer32"""
    defaultValue = 4

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
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_W2kConfigPrnQueueMonitor_Type.__name__ = "Integer32"
_W2kConfigPrnQueueMonitor_Object = MibScalar
w2kConfigPrnQueueMonitor = _W2kConfigPrnQueueMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 15, 10),
    _W2kConfigPrnQueueMonitor_Type()
)
w2kConfigPrnQueueMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigPrnQueueMonitor.setStatus("mandatory")


class _W2kConfigPrnLossAction_Type(Integer32):
    """Custom type w2kConfigPrnLossAction based on Integer32"""
    defaultValue = 4

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
        *(("down-critical", 4),
          ("down-warning", 3),
          ("remove", 1),
          ("up", 2))
    )


_W2kConfigPrnLossAction_Type.__name__ = "Integer32"
_W2kConfigPrnLossAction_Object = MibScalar
w2kConfigPrnLossAction = _W2kConfigPrnLossAction_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 15, 11),
    _W2kConfigPrnLossAction_Type()
)
w2kConfigPrnLossAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigPrnLossAction.setStatus("mandatory")
_W2kConfigPrnAutoTableWatcherName_Type = DisplayString
_W2kConfigPrnAutoTableWatcherName_Object = MibScalar
w2kConfigPrnAutoTableWatcherName = _W2kConfigPrnAutoTableWatcherName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 15, 12),
    _W2kConfigPrnAutoTableWatcherName_Type()
)
w2kConfigPrnAutoTableWatcherName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigPrnAutoTableWatcherName.setStatus("mandatory")


class _W2kConfigPrnButton_Type(Integer32):
    """Custom type w2kConfigPrnButton based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("add", 2),
          ("add-auto", 4),
          ("none", 1),
          ("remove", 3),
          ("remove-auto", 5))
    )


_W2kConfigPrnButton_Type.__name__ = "Integer32"
_W2kConfigPrnButton_Object = MibScalar
w2kConfigPrnButton = _W2kConfigPrnButton_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 15, 13),
    _W2kConfigPrnButton_Type()
)
w2kConfigPrnButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigPrnButton.setStatus("mandatory")
_W2kConfigPrnAutoTable_Object = MibTable
w2kConfigPrnAutoTable = _W2kConfigPrnAutoTable_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 15, 14)
)
if mibBuilder.loadTexts:
    w2kConfigPrnAutoTable.setStatus("mandatory")
_W2kConfigPrnAutoEntry_Object = MibTableRow
w2kConfigPrnAutoEntry = _W2kConfigPrnAutoEntry_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 15, 14, 1)
)
w2kConfigPrnAutoEntry.setIndexNames(
    (0, "CA-W2KOS-MIB", "w2kConfigPrnAutoWatcherName"),
)
if mibBuilder.loadTexts:
    w2kConfigPrnAutoEntry.setStatus("mandatory")
_W2kConfigPrnAutoWatcherName_Type = DisplayString
_W2kConfigPrnAutoWatcherName_Object = MibTableColumn
w2kConfigPrnAutoWatcherName = _W2kConfigPrnAutoWatcherName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 15, 14, 1, 1),
    _W2kConfigPrnAutoWatcherName_Type()
)
w2kConfigPrnAutoWatcherName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kConfigPrnAutoWatcherName.setStatus("mandatory")
_W2kConfigPrnAutoName_Type = DisplayString
_W2kConfigPrnAutoName_Object = MibTableColumn
w2kConfigPrnAutoName = _W2kConfigPrnAutoName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 15, 14, 1, 2),
    _W2kConfigPrnAutoName_Type()
)
w2kConfigPrnAutoName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigPrnAutoName.setStatus("mandatory")
_W2kConfigPrnAutoDescription_Type = DisplayString
_W2kConfigPrnAutoDescription_Object = MibTableColumn
w2kConfigPrnAutoDescription = _W2kConfigPrnAutoDescription_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 15, 14, 1, 3),
    _W2kConfigPrnAutoDescription_Type()
)
w2kConfigPrnAutoDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigPrnAutoDescription.setStatus("mandatory")
_W2kConfigPrnAutoAggLag_Type = Integer32
_W2kConfigPrnAutoAggLag_Object = MibTableColumn
w2kConfigPrnAutoAggLag = _W2kConfigPrnAutoAggLag_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 15, 14, 1, 4),
    _W2kConfigPrnAutoAggLag_Type()
)
w2kConfigPrnAutoAggLag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigPrnAutoAggLag.setStatus("mandatory")


class _W2kConfigPrnAutoEventMonitor_Type(Integer32):
    """Custom type w2kConfigPrnAutoEventMonitor based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("do-not-monitor", 1),
          ("down-critical", 3),
          ("down-warning", 2))
    )


_W2kConfigPrnAutoEventMonitor_Type.__name__ = "Integer32"
_W2kConfigPrnAutoEventMonitor_Object = MibTableColumn
w2kConfigPrnAutoEventMonitor = _W2kConfigPrnAutoEventMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 15, 14, 1, 5),
    _W2kConfigPrnAutoEventMonitor_Type()
)
w2kConfigPrnAutoEventMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigPrnAutoEventMonitor.setStatus("mandatory")
_W2kConfigPrnAutoQueueWarn_Type = Integer32
_W2kConfigPrnAutoQueueWarn_Object = MibTableColumn
w2kConfigPrnAutoQueueWarn = _W2kConfigPrnAutoQueueWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 15, 14, 1, 6),
    _W2kConfigPrnAutoQueueWarn_Type()
)
w2kConfigPrnAutoQueueWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigPrnAutoQueueWarn.setStatus("mandatory")
_W2kConfigPrnAutoQueueCrit_Type = Integer32
_W2kConfigPrnAutoQueueCrit_Object = MibTableColumn
w2kConfigPrnAutoQueueCrit = _W2kConfigPrnAutoQueueCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 15, 14, 1, 7),
    _W2kConfigPrnAutoQueueCrit_Type()
)
w2kConfigPrnAutoQueueCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigPrnAutoQueueCrit.setStatus("mandatory")


class _W2kConfigPrnAutoQueueMonitor_Type(Integer32):
    """Custom type w2kConfigPrnAutoQueueMonitor based on Integer32"""
    defaultValue = 0

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
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_W2kConfigPrnAutoQueueMonitor_Type.__name__ = "Integer32"
_W2kConfigPrnAutoQueueMonitor_Object = MibTableColumn
w2kConfigPrnAutoQueueMonitor = _W2kConfigPrnAutoQueueMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 15, 14, 1, 8),
    _W2kConfigPrnAutoQueueMonitor_Type()
)
w2kConfigPrnAutoQueueMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigPrnAutoQueueMonitor.setStatus("mandatory")


class _W2kConfigPrnAutoLossAction_Type(Integer32):
    """Custom type w2kConfigPrnAutoLossAction based on Integer32"""
    defaultValue = 0

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
        *(("down-critical", 4),
          ("down-warning", 3),
          ("remove", 1),
          ("up", 2))
    )


_W2kConfigPrnAutoLossAction_Type.__name__ = "Integer32"
_W2kConfigPrnAutoLossAction_Object = MibTableColumn
w2kConfigPrnAutoLossAction = _W2kConfigPrnAutoLossAction_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 15, 14, 1, 9),
    _W2kConfigPrnAutoLossAction_Type()
)
w2kConfigPrnAutoLossAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigPrnAutoLossAction.setStatus("mandatory")


class _W2kConfigPrnAutoButton_Type(Integer32):
    """Custom type w2kConfigPrnAutoButton based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("remove", 2))
    )


_W2kConfigPrnAutoButton_Type.__name__ = "Integer32"
_W2kConfigPrnAutoButton_Object = MibTableColumn
w2kConfigPrnAutoButton = _W2kConfigPrnAutoButton_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 15, 14, 1, 10),
    _W2kConfigPrnAutoButton_Type()
)
w2kConfigPrnAutoButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigPrnAutoButton.setStatus("mandatory")
_W2kConfigNetGroup_ObjectIdentity = ObjectIdentity
w2kConfigNetGroup = _W2kConfigNetGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 16)
)


class _W2kConfigNetPollInterval_Type(Integer32):
    """Custom type w2kConfigNetPollInterval based on Integer32"""
    defaultValue = 120


_W2kConfigNetPollInterval_Object = MibScalar
w2kConfigNetPollInterval = _W2kConfigNetPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 16, 1),
    _W2kConfigNetPollInterval_Type()
)
w2kConfigNetPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigNetPollInterval.setStatus("mandatory")


class _W2kConfigNetPollMethod_Type(Integer32):
    """Custom type w2kConfigNetPollMethod based on Integer32"""
    defaultValue = 2

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
        *(("disabled", 1),
          ("poll-interval-and-query", 3),
          ("poll-interval-only", 2),
          ("query-only", 4))
    )


_W2kConfigNetPollMethod_Type.__name__ = "Integer32"
_W2kConfigNetPollMethod_Object = MibScalar
w2kConfigNetPollMethod = _W2kConfigNetPollMethod_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 16, 2),
    _W2kConfigNetPollMethod_Type()
)
w2kConfigNetPollMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigNetPollMethod.setStatus("mandatory")


class _W2kConfigNetAggLag_Type(Integer32):
    """Custom type w2kConfigNetAggLag based on Integer32"""
    defaultValue = 1


_W2kConfigNetAggLag_Object = MibScalar
w2kConfigNetAggLag = _W2kConfigNetAggLag_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 16, 3),
    _W2kConfigNetAggLag_Type()
)
w2kConfigNetAggLag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigNetAggLag.setStatus("mandatory")


class _W2kConfigNetInPktWarn_Type(Integer32):
    """Custom type w2kConfigNetInPktWarn based on Integer32"""
    defaultValue = 200


_W2kConfigNetInPktWarn_Object = MibScalar
w2kConfigNetInPktWarn = _W2kConfigNetInPktWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 16, 4),
    _W2kConfigNetInPktWarn_Type()
)
w2kConfigNetInPktWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigNetInPktWarn.setStatus("mandatory")


class _W2kConfigNetInPktCrit_Type(Integer32):
    """Custom type w2kConfigNetInPktCrit based on Integer32"""
    defaultValue = 400


_W2kConfigNetInPktCrit_Object = MibScalar
w2kConfigNetInPktCrit = _W2kConfigNetInPktCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 16, 5),
    _W2kConfigNetInPktCrit_Type()
)
w2kConfigNetInPktCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigNetInPktCrit.setStatus("mandatory")


class _W2kConfigNetInPktMonitor_Type(Integer32):
    """Custom type w2kConfigNetInPktMonitor based on Integer32"""
    defaultValue = 4

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
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_W2kConfigNetInPktMonitor_Type.__name__ = "Integer32"
_W2kConfigNetInPktMonitor_Object = MibScalar
w2kConfigNetInPktMonitor = _W2kConfigNetInPktMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 16, 6),
    _W2kConfigNetInPktMonitor_Type()
)
w2kConfigNetInPktMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigNetInPktMonitor.setStatus("mandatory")


class _W2kConfigNetOutPktWarn_Type(Integer32):
    """Custom type w2kConfigNetOutPktWarn based on Integer32"""
    defaultValue = 200


_W2kConfigNetOutPktWarn_Object = MibScalar
w2kConfigNetOutPktWarn = _W2kConfigNetOutPktWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 16, 7),
    _W2kConfigNetOutPktWarn_Type()
)
w2kConfigNetOutPktWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigNetOutPktWarn.setStatus("mandatory")


class _W2kConfigNetOutPktCrit_Type(Integer32):
    """Custom type w2kConfigNetOutPktCrit based on Integer32"""
    defaultValue = 400


_W2kConfigNetOutPktCrit_Object = MibScalar
w2kConfigNetOutPktCrit = _W2kConfigNetOutPktCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 16, 8),
    _W2kConfigNetOutPktCrit_Type()
)
w2kConfigNetOutPktCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigNetOutPktCrit.setStatus("mandatory")


class _W2kConfigNetOutPktMonitor_Type(Integer32):
    """Custom type w2kConfigNetOutPktMonitor based on Integer32"""
    defaultValue = 4

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
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_W2kConfigNetOutPktMonitor_Type.__name__ = "Integer32"
_W2kConfigNetOutPktMonitor_Object = MibScalar
w2kConfigNetOutPktMonitor = _W2kConfigNetOutPktMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 16, 9),
    _W2kConfigNetOutPktMonitor_Type()
)
w2kConfigNetOutPktMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigNetOutPktMonitor.setStatus("mandatory")


class _W2kConfigNetInErrDWarn_Type(Integer32):
    """Custom type w2kConfigNetInErrDWarn based on Integer32"""
    defaultValue = 20


_W2kConfigNetInErrDWarn_Object = MibScalar
w2kConfigNetInErrDWarn = _W2kConfigNetInErrDWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 16, 10),
    _W2kConfigNetInErrDWarn_Type()
)
w2kConfigNetInErrDWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigNetInErrDWarn.setStatus("mandatory")


class _W2kConfigNetInErrDCrit_Type(Integer32):
    """Custom type w2kConfigNetInErrDCrit based on Integer32"""
    defaultValue = 40


_W2kConfigNetInErrDCrit_Object = MibScalar
w2kConfigNetInErrDCrit = _W2kConfigNetInErrDCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 16, 11),
    _W2kConfigNetInErrDCrit_Type()
)
w2kConfigNetInErrDCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigNetInErrDCrit.setStatus("mandatory")


class _W2kConfigNetInErrDMonitor_Type(Integer32):
    """Custom type w2kConfigNetInErrDMonitor based on Integer32"""
    defaultValue = 4

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
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_W2kConfigNetInErrDMonitor_Type.__name__ = "Integer32"
_W2kConfigNetInErrDMonitor_Object = MibScalar
w2kConfigNetInErrDMonitor = _W2kConfigNetInErrDMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 16, 12),
    _W2kConfigNetInErrDMonitor_Type()
)
w2kConfigNetInErrDMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigNetInErrDMonitor.setStatus("mandatory")


class _W2kConfigNetOutErrDWarn_Type(Integer32):
    """Custom type w2kConfigNetOutErrDWarn based on Integer32"""
    defaultValue = 20


_W2kConfigNetOutErrDWarn_Object = MibScalar
w2kConfigNetOutErrDWarn = _W2kConfigNetOutErrDWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 16, 13),
    _W2kConfigNetOutErrDWarn_Type()
)
w2kConfigNetOutErrDWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigNetOutErrDWarn.setStatus("mandatory")


class _W2kConfigNetOutErrDCrit_Type(Integer32):
    """Custom type w2kConfigNetOutErrDCrit based on Integer32"""
    defaultValue = 40


_W2kConfigNetOutErrDCrit_Object = MibScalar
w2kConfigNetOutErrDCrit = _W2kConfigNetOutErrDCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 16, 14),
    _W2kConfigNetOutErrDCrit_Type()
)
w2kConfigNetOutErrDCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigNetOutErrDCrit.setStatus("mandatory")


class _W2kConfigNetOutErrDMonitor_Type(Integer32):
    """Custom type w2kConfigNetOutErrDMonitor based on Integer32"""
    defaultValue = 4

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
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_W2kConfigNetOutErrDMonitor_Type.__name__ = "Integer32"
_W2kConfigNetOutErrDMonitor_Object = MibScalar
w2kConfigNetOutErrDMonitor = _W2kConfigNetOutErrDMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 16, 15),
    _W2kConfigNetOutErrDMonitor_Type()
)
w2kConfigNetOutErrDMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigNetOutErrDMonitor.setStatus("mandatory")


class _W2kConfigNetLossAction_Type(Integer32):
    """Custom type w2kConfigNetLossAction based on Integer32"""
    defaultValue = 1

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
        *(("down-critical", 4),
          ("down-warning", 3),
          ("remove", 1),
          ("up", 2))
    )


_W2kConfigNetLossAction_Type.__name__ = "Integer32"
_W2kConfigNetLossAction_Object = MibScalar
w2kConfigNetLossAction = _W2kConfigNetLossAction_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 16, 16),
    _W2kConfigNetLossAction_Type()
)
w2kConfigNetLossAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigNetLossAction.setStatus("mandatory")
_W2kConfigRegGroup_ObjectIdentity = ObjectIdentity
w2kConfigRegGroup = _W2kConfigRegGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 17)
)


class _W2kConfigRegPollInterval_Type(Integer32):
    """Custom type w2kConfigRegPollInterval based on Integer32"""
    defaultValue = 120


_W2kConfigRegPollInterval_Object = MibScalar
w2kConfigRegPollInterval = _W2kConfigRegPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 17, 1),
    _W2kConfigRegPollInterval_Type()
)
w2kConfigRegPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigRegPollInterval.setStatus("mandatory")


class _W2kConfigRegPollMethod_Type(Integer32):
    """Custom type w2kConfigRegPollMethod based on Integer32"""
    defaultValue = 2

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
        *(("disabled", 1),
          ("poll-interval-and-query", 3),
          ("poll-interval-only", 2),
          ("query-only", 4))
    )


_W2kConfigRegPollMethod_Type.__name__ = "Integer32"
_W2kConfigRegPollMethod_Object = MibScalar
w2kConfigRegPollMethod = _W2kConfigRegPollMethod_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 17, 2),
    _W2kConfigRegPollMethod_Type()
)
w2kConfigRegPollMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigRegPollMethod.setStatus("mandatory")
_W2kConfigRegName_Type = DisplayString
_W2kConfigRegName_Object = MibScalar
w2kConfigRegName = _W2kConfigRegName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 17, 3),
    _W2kConfigRegName_Type()
)
w2kConfigRegName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigRegName.setStatus("mandatory")
_W2kConfigRegDescription_Type = DisplayString
_W2kConfigRegDescription_Object = MibScalar
w2kConfigRegDescription = _W2kConfigRegDescription_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 17, 4),
    _W2kConfigRegDescription_Type()
)
w2kConfigRegDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigRegDescription.setStatus("mandatory")


class _W2kConfigRegAggLag_Type(Integer32):
    """Custom type w2kConfigRegAggLag based on Integer32"""
    defaultValue = 1


_W2kConfigRegAggLag_Object = MibScalar
w2kConfigRegAggLag = _W2kConfigRegAggLag_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 17, 5),
    _W2kConfigRegAggLag_Type()
)
w2kConfigRegAggLag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigRegAggLag.setStatus("mandatory")


class _W2kConfigRegExist_Type(Integer32):
    """Custom type w2kConfigRegExist based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("should-exist", 1),
          ("should-not-exist", 2))
    )


_W2kConfigRegExist_Type.__name__ = "Integer32"
_W2kConfigRegExist_Object = MibScalar
w2kConfigRegExist = _W2kConfigRegExist_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 17, 6),
    _W2kConfigRegExist_Type()
)
w2kConfigRegExist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigRegExist.setStatus("mandatory")


class _W2kConfigRegExistMonitor_Type(Integer32):
    """Custom type w2kConfigRegExistMonitor based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("do-not-monitor", 1),
          ("down-critical", 3),
          ("down-warning", 2))
    )


_W2kConfigRegExistMonitor_Type.__name__ = "Integer32"
_W2kConfigRegExistMonitor_Object = MibScalar
w2kConfigRegExistMonitor = _W2kConfigRegExistMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 17, 7),
    _W2kConfigRegExistMonitor_Type()
)
w2kConfigRegExistMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigRegExistMonitor.setStatus("mandatory")


class _W2kConfigRegValueRef_Type(DisplayString):
    """Custom type w2kConfigRegValueRef based on DisplayString"""
    defaultValue = OctetString("0")


_W2kConfigRegValueRef_Object = MibScalar
w2kConfigRegValueRef = _W2kConfigRegValueRef_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 17, 8),
    _W2kConfigRegValueRef_Type()
)
w2kConfigRegValueRef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigRegValueRef.setStatus("mandatory")


class _W2kConfigRegValueCond_Type(Integer32):
    """Custom type w2kConfigRegValueCond based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("should-be-above", 4),
          ("should-be-below", 3),
          ("should-be-equal", 1),
          ("should-not-be-equal", 2),
          ("should-not-change", 5))
    )


_W2kConfigRegValueCond_Type.__name__ = "Integer32"
_W2kConfigRegValueCond_Object = MibScalar
w2kConfigRegValueCond = _W2kConfigRegValueCond_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 17, 9),
    _W2kConfigRegValueCond_Type()
)
w2kConfigRegValueCond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigRegValueCond.setStatus("mandatory")


class _W2kConfigRegValueMonitor_Type(Integer32):
    """Custom type w2kConfigRegValueMonitor based on Integer32"""
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
        *(("do-not-monitor", 1),
          ("down-critical", 3),
          ("down-warning", 2))
    )


_W2kConfigRegValueMonitor_Type.__name__ = "Integer32"
_W2kConfigRegValueMonitor_Object = MibScalar
w2kConfigRegValueMonitor = _W2kConfigRegValueMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 17, 10),
    _W2kConfigRegValueMonitor_Type()
)
w2kConfigRegValueMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigRegValueMonitor.setStatus("mandatory")


class _W2kConfigRegButton_Type(Integer32):
    """Custom type w2kConfigRegButton based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("add", 2),
          ("none", 1),
          ("remove", 3))
    )


_W2kConfigRegButton_Type.__name__ = "Integer32"
_W2kConfigRegButton_Object = MibScalar
w2kConfigRegButton = _W2kConfigRegButton_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 1, 17, 11),
    _W2kConfigRegButton_Type()
)
w2kConfigRegButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kConfigRegButton.setStatus("mandatory")
_W2kStatusGroup_ObjectIdentity = ObjectIdentity
w2kStatusGroup = _W2kStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2)
)
_W2kStatusGeneralGroup_ObjectIdentity = ObjectIdentity
w2kStatusGeneralGroup = _W2kStatusGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 1)
)
_W2kStatusGeneralTotalCount_Type = Integer32
_W2kStatusGeneralTotalCount_Object = MibScalar
w2kStatusGeneralTotalCount = _W2kStatusGeneralTotalCount_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 1, 1),
    _W2kStatusGeneralTotalCount_Type()
)
w2kStatusGeneralTotalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusGeneralTotalCount.setStatus("mandatory")
_W2kStatusGeneralTotalWarn_Type = Integer32
_W2kStatusGeneralTotalWarn_Object = MibScalar
w2kStatusGeneralTotalWarn = _W2kStatusGeneralTotalWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 1, 2),
    _W2kStatusGeneralTotalWarn_Type()
)
w2kStatusGeneralTotalWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusGeneralTotalWarn.setStatus("mandatory")
_W2kStatusGeneralTotalCrit_Type = Integer32
_W2kStatusGeneralTotalCrit_Object = MibScalar
w2kStatusGeneralTotalCrit = _W2kStatusGeneralTotalCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 1, 3),
    _W2kStatusGeneralTotalCrit_Type()
)
w2kStatusGeneralTotalCrit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusGeneralTotalCrit.setStatus("mandatory")
_W2kStatusGeneralCpuCount_Type = Integer32
_W2kStatusGeneralCpuCount_Object = MibScalar
w2kStatusGeneralCpuCount = _W2kStatusGeneralCpuCount_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 1, 4),
    _W2kStatusGeneralCpuCount_Type()
)
w2kStatusGeneralCpuCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusGeneralCpuCount.setStatus("mandatory")
_W2kStatusGeneralCpuWarn_Type = Integer32
_W2kStatusGeneralCpuWarn_Object = MibScalar
w2kStatusGeneralCpuWarn = _W2kStatusGeneralCpuWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 1, 5),
    _W2kStatusGeneralCpuWarn_Type()
)
w2kStatusGeneralCpuWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusGeneralCpuWarn.setStatus("mandatory")
_W2kStatusGeneralCpuCrit_Type = Integer32
_W2kStatusGeneralCpuCrit_Object = MibScalar
w2kStatusGeneralCpuCrit = _W2kStatusGeneralCpuCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 1, 6),
    _W2kStatusGeneralCpuCrit_Type()
)
w2kStatusGeneralCpuCrit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusGeneralCpuCrit.setStatus("mandatory")
_W2kStatusGeneralMemCount_Type = Integer32
_W2kStatusGeneralMemCount_Object = MibScalar
w2kStatusGeneralMemCount = _W2kStatusGeneralMemCount_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 1, 7),
    _W2kStatusGeneralMemCount_Type()
)
w2kStatusGeneralMemCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusGeneralMemCount.setStatus("mandatory")
_W2kStatusGeneralMemWarn_Type = Integer32
_W2kStatusGeneralMemWarn_Object = MibScalar
w2kStatusGeneralMemWarn = _W2kStatusGeneralMemWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 1, 8),
    _W2kStatusGeneralMemWarn_Type()
)
w2kStatusGeneralMemWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusGeneralMemWarn.setStatus("mandatory")
_W2kStatusGeneralMemCrit_Type = Integer32
_W2kStatusGeneralMemCrit_Object = MibScalar
w2kStatusGeneralMemCrit = _W2kStatusGeneralMemCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 1, 9),
    _W2kStatusGeneralMemCrit_Type()
)
w2kStatusGeneralMemCrit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusGeneralMemCrit.setStatus("mandatory")
_W2kStatusGeneralLVolCount_Type = Integer32
_W2kStatusGeneralLVolCount_Object = MibScalar
w2kStatusGeneralLVolCount = _W2kStatusGeneralLVolCount_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 1, 10),
    _W2kStatusGeneralLVolCount_Type()
)
w2kStatusGeneralLVolCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusGeneralLVolCount.setStatus("mandatory")
_W2kStatusGeneralLVolWarn_Type = Integer32
_W2kStatusGeneralLVolWarn_Object = MibScalar
w2kStatusGeneralLVolWarn = _W2kStatusGeneralLVolWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 1, 11),
    _W2kStatusGeneralLVolWarn_Type()
)
w2kStatusGeneralLVolWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusGeneralLVolWarn.setStatus("mandatory")
_W2kStatusGeneralLVolCrit_Type = Integer32
_W2kStatusGeneralLVolCrit_Object = MibScalar
w2kStatusGeneralLVolCrit = _W2kStatusGeneralLVolCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 1, 12),
    _W2kStatusGeneralLVolCrit_Type()
)
w2kStatusGeneralLVolCrit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusGeneralLVolCrit.setStatus("mandatory")
_W2kStatusGeneralMntCount_Type = Integer32
_W2kStatusGeneralMntCount_Object = MibScalar
w2kStatusGeneralMntCount = _W2kStatusGeneralMntCount_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 1, 13),
    _W2kStatusGeneralMntCount_Type()
)
w2kStatusGeneralMntCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusGeneralMntCount.setStatus("mandatory")
_W2kStatusGeneralMntWarn_Type = Integer32
_W2kStatusGeneralMntWarn_Object = MibScalar
w2kStatusGeneralMntWarn = _W2kStatusGeneralMntWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 1, 14),
    _W2kStatusGeneralMntWarn_Type()
)
w2kStatusGeneralMntWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusGeneralMntWarn.setStatus("mandatory")
_W2kStatusGeneralMntCrit_Type = Integer32
_W2kStatusGeneralMntCrit_Object = MibScalar
w2kStatusGeneralMntCrit = _W2kStatusGeneralMntCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 1, 15),
    _W2kStatusGeneralMntCrit_Type()
)
w2kStatusGeneralMntCrit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusGeneralMntCrit.setStatus("mandatory")
_W2kStatusGeneralDfsCount_Type = Integer32
_W2kStatusGeneralDfsCount_Object = MibScalar
w2kStatusGeneralDfsCount = _W2kStatusGeneralDfsCount_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 1, 16),
    _W2kStatusGeneralDfsCount_Type()
)
w2kStatusGeneralDfsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusGeneralDfsCount.setStatus("mandatory")
_W2kStatusGeneralDfsWarn_Type = Integer32
_W2kStatusGeneralDfsWarn_Object = MibScalar
w2kStatusGeneralDfsWarn = _W2kStatusGeneralDfsWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 1, 17),
    _W2kStatusGeneralDfsWarn_Type()
)
w2kStatusGeneralDfsWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusGeneralDfsWarn.setStatus("mandatory")
_W2kStatusGeneralDfsCrit_Type = Integer32
_W2kStatusGeneralDfsCrit_Object = MibScalar
w2kStatusGeneralDfsCrit = _W2kStatusGeneralDfsCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 1, 18),
    _W2kStatusGeneralDfsCrit_Type()
)
w2kStatusGeneralDfsCrit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusGeneralDfsCrit.setStatus("mandatory")
_W2kStatusGeneralQuotCount_Type = Integer32
_W2kStatusGeneralQuotCount_Object = MibScalar
w2kStatusGeneralQuotCount = _W2kStatusGeneralQuotCount_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 1, 19),
    _W2kStatusGeneralQuotCount_Type()
)
w2kStatusGeneralQuotCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusGeneralQuotCount.setStatus("mandatory")
_W2kStatusGeneralQuotWarn_Type = Integer32
_W2kStatusGeneralQuotWarn_Object = MibScalar
w2kStatusGeneralQuotWarn = _W2kStatusGeneralQuotWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 1, 20),
    _W2kStatusGeneralQuotWarn_Type()
)
w2kStatusGeneralQuotWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusGeneralQuotWarn.setStatus("mandatory")
_W2kStatusGeneralQuotCrit_Type = Integer32
_W2kStatusGeneralQuotCrit_Object = MibScalar
w2kStatusGeneralQuotCrit = _W2kStatusGeneralQuotCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 1, 21),
    _W2kStatusGeneralQuotCrit_Type()
)
w2kStatusGeneralQuotCrit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusGeneralQuotCrit.setStatus("mandatory")
_W2kStatusGeneralDirCount_Type = Integer32
_W2kStatusGeneralDirCount_Object = MibScalar
w2kStatusGeneralDirCount = _W2kStatusGeneralDirCount_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 1, 22),
    _W2kStatusGeneralDirCount_Type()
)
w2kStatusGeneralDirCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusGeneralDirCount.setStatus("mandatory")
_W2kStatusGeneralDirWarn_Type = Integer32
_W2kStatusGeneralDirWarn_Object = MibScalar
w2kStatusGeneralDirWarn = _W2kStatusGeneralDirWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 1, 23),
    _W2kStatusGeneralDirWarn_Type()
)
w2kStatusGeneralDirWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusGeneralDirWarn.setStatus("mandatory")
_W2kStatusGeneralDirCrit_Type = Integer32
_W2kStatusGeneralDirCrit_Object = MibScalar
w2kStatusGeneralDirCrit = _W2kStatusGeneralDirCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 1, 24),
    _W2kStatusGeneralDirCrit_Type()
)
w2kStatusGeneralDirCrit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusGeneralDirCrit.setStatus("mandatory")
_W2kStatusGeneralFileCount_Type = Integer32
_W2kStatusGeneralFileCount_Object = MibScalar
w2kStatusGeneralFileCount = _W2kStatusGeneralFileCount_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 1, 25),
    _W2kStatusGeneralFileCount_Type()
)
w2kStatusGeneralFileCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusGeneralFileCount.setStatus("mandatory")
_W2kStatusGeneralFileWarn_Type = Integer32
_W2kStatusGeneralFileWarn_Object = MibScalar
w2kStatusGeneralFileWarn = _W2kStatusGeneralFileWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 1, 26),
    _W2kStatusGeneralFileWarn_Type()
)
w2kStatusGeneralFileWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusGeneralFileWarn.setStatus("mandatory")
_W2kStatusGeneralFileCrit_Type = Integer32
_W2kStatusGeneralFileCrit_Object = MibScalar
w2kStatusGeneralFileCrit = _W2kStatusGeneralFileCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 1, 27),
    _W2kStatusGeneralFileCrit_Type()
)
w2kStatusGeneralFileCrit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusGeneralFileCrit.setStatus("mandatory")
_W2kStatusGeneralProcCount_Type = Integer32
_W2kStatusGeneralProcCount_Object = MibScalar
w2kStatusGeneralProcCount = _W2kStatusGeneralProcCount_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 1, 28),
    _W2kStatusGeneralProcCount_Type()
)
w2kStatusGeneralProcCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusGeneralProcCount.setStatus("mandatory")
_W2kStatusGeneralProcWarn_Type = Integer32
_W2kStatusGeneralProcWarn_Object = MibScalar
w2kStatusGeneralProcWarn = _W2kStatusGeneralProcWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 1, 29),
    _W2kStatusGeneralProcWarn_Type()
)
w2kStatusGeneralProcWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusGeneralProcWarn.setStatus("mandatory")
_W2kStatusGeneralProcCrit_Type = Integer32
_W2kStatusGeneralProcCrit_Object = MibScalar
w2kStatusGeneralProcCrit = _W2kStatusGeneralProcCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 1, 30),
    _W2kStatusGeneralProcCrit_Type()
)
w2kStatusGeneralProcCrit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusGeneralProcCrit.setStatus("mandatory")
_W2kStatusGeneralSrvcCount_Type = Integer32
_W2kStatusGeneralSrvcCount_Object = MibScalar
w2kStatusGeneralSrvcCount = _W2kStatusGeneralSrvcCount_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 1, 31),
    _W2kStatusGeneralSrvcCount_Type()
)
w2kStatusGeneralSrvcCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusGeneralSrvcCount.setStatus("mandatory")
_W2kStatusGeneralSrvcWarn_Type = Integer32
_W2kStatusGeneralSrvcWarn_Object = MibScalar
w2kStatusGeneralSrvcWarn = _W2kStatusGeneralSrvcWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 1, 32),
    _W2kStatusGeneralSrvcWarn_Type()
)
w2kStatusGeneralSrvcWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusGeneralSrvcWarn.setStatus("mandatory")
_W2kStatusGeneralSrvcCrit_Type = Integer32
_W2kStatusGeneralSrvcCrit_Object = MibScalar
w2kStatusGeneralSrvcCrit = _W2kStatusGeneralSrvcCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 1, 33),
    _W2kStatusGeneralSrvcCrit_Type()
)
w2kStatusGeneralSrvcCrit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusGeneralSrvcCrit.setStatus("mandatory")
_W2kStatusGeneralJobCount_Type = Integer32
_W2kStatusGeneralJobCount_Object = MibScalar
w2kStatusGeneralJobCount = _W2kStatusGeneralJobCount_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 1, 34),
    _W2kStatusGeneralJobCount_Type()
)
w2kStatusGeneralJobCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusGeneralJobCount.setStatus("mandatory")
_W2kStatusGeneralJobWarn_Type = Integer32
_W2kStatusGeneralJobWarn_Object = MibScalar
w2kStatusGeneralJobWarn = _W2kStatusGeneralJobWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 1, 35),
    _W2kStatusGeneralJobWarn_Type()
)
w2kStatusGeneralJobWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusGeneralJobWarn.setStatus("mandatory")
_W2kStatusGeneralJobCrit_Type = Integer32
_W2kStatusGeneralJobCrit_Object = MibScalar
w2kStatusGeneralJobCrit = _W2kStatusGeneralJobCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 1, 36),
    _W2kStatusGeneralJobCrit_Type()
)
w2kStatusGeneralJobCrit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusGeneralJobCrit.setStatus("mandatory")
_W2kStatusGeneralSessCount_Type = Integer32
_W2kStatusGeneralSessCount_Object = MibScalar
w2kStatusGeneralSessCount = _W2kStatusGeneralSessCount_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 1, 37),
    _W2kStatusGeneralSessCount_Type()
)
w2kStatusGeneralSessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusGeneralSessCount.setStatus("mandatory")
_W2kStatusGeneralSessWarn_Type = Integer32
_W2kStatusGeneralSessWarn_Object = MibScalar
w2kStatusGeneralSessWarn = _W2kStatusGeneralSessWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 1, 38),
    _W2kStatusGeneralSessWarn_Type()
)
w2kStatusGeneralSessWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusGeneralSessWarn.setStatus("mandatory")
_W2kStatusGeneralSessCrit_Type = Integer32
_W2kStatusGeneralSessCrit_Object = MibScalar
w2kStatusGeneralSessCrit = _W2kStatusGeneralSessCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 1, 39),
    _W2kStatusGeneralSessCrit_Type()
)
w2kStatusGeneralSessCrit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusGeneralSessCrit.setStatus("mandatory")
_W2kStatusGeneralPrnCount_Type = Integer32
_W2kStatusGeneralPrnCount_Object = MibScalar
w2kStatusGeneralPrnCount = _W2kStatusGeneralPrnCount_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 1, 40),
    _W2kStatusGeneralPrnCount_Type()
)
w2kStatusGeneralPrnCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusGeneralPrnCount.setStatus("mandatory")
_W2kStatusGeneralPrnWarn_Type = Integer32
_W2kStatusGeneralPrnWarn_Object = MibScalar
w2kStatusGeneralPrnWarn = _W2kStatusGeneralPrnWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 1, 41),
    _W2kStatusGeneralPrnWarn_Type()
)
w2kStatusGeneralPrnWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusGeneralPrnWarn.setStatus("mandatory")
_W2kStatusGeneralPrnCrit_Type = Integer32
_W2kStatusGeneralPrnCrit_Object = MibScalar
w2kStatusGeneralPrnCrit = _W2kStatusGeneralPrnCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 1, 42),
    _W2kStatusGeneralPrnCrit_Type()
)
w2kStatusGeneralPrnCrit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusGeneralPrnCrit.setStatus("mandatory")
_W2kStatusGeneralNetCount_Type = Integer32
_W2kStatusGeneralNetCount_Object = MibScalar
w2kStatusGeneralNetCount = _W2kStatusGeneralNetCount_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 1, 43),
    _W2kStatusGeneralNetCount_Type()
)
w2kStatusGeneralNetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusGeneralNetCount.setStatus("mandatory")
_W2kStatusGeneralNetWarn_Type = Integer32
_W2kStatusGeneralNetWarn_Object = MibScalar
w2kStatusGeneralNetWarn = _W2kStatusGeneralNetWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 1, 44),
    _W2kStatusGeneralNetWarn_Type()
)
w2kStatusGeneralNetWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusGeneralNetWarn.setStatus("mandatory")
_W2kStatusGeneralNetCrit_Type = Integer32
_W2kStatusGeneralNetCrit_Object = MibScalar
w2kStatusGeneralNetCrit = _W2kStatusGeneralNetCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 1, 45),
    _W2kStatusGeneralNetCrit_Type()
)
w2kStatusGeneralNetCrit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusGeneralNetCrit.setStatus("mandatory")
_W2kStatusGeneralRegCount_Type = Integer32
_W2kStatusGeneralRegCount_Object = MibScalar
w2kStatusGeneralRegCount = _W2kStatusGeneralRegCount_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 1, 46),
    _W2kStatusGeneralRegCount_Type()
)
w2kStatusGeneralRegCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusGeneralRegCount.setStatus("mandatory")
_W2kStatusGeneralRegWarn_Type = Integer32
_W2kStatusGeneralRegWarn_Object = MibScalar
w2kStatusGeneralRegWarn = _W2kStatusGeneralRegWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 1, 47),
    _W2kStatusGeneralRegWarn_Type()
)
w2kStatusGeneralRegWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusGeneralRegWarn.setStatus("mandatory")
_W2kStatusGeneralRegCrit_Type = Integer32
_W2kStatusGeneralRegCrit_Object = MibScalar
w2kStatusGeneralRegCrit = _W2kStatusGeneralRegCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 1, 48),
    _W2kStatusGeneralRegCrit_Type()
)
w2kStatusGeneralRegCrit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusGeneralRegCrit.setStatus("mandatory")
_W2kStatusCpuGroup_ObjectIdentity = ObjectIdentity
w2kStatusCpuGroup = _W2kStatusCpuGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 2)
)
_W2kStatusCpuTotalLoadValue_Type = Integer32
_W2kStatusCpuTotalLoadValue_Object = MibScalar
w2kStatusCpuTotalLoadValue = _W2kStatusCpuTotalLoadValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 2, 1),
    _W2kStatusCpuTotalLoadValue_Type()
)
w2kStatusCpuTotalLoadValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusCpuTotalLoadValue.setStatus("mandatory")
_W2kStatusCpuTotalLoadLagValue_Type = Integer32
_W2kStatusCpuTotalLoadLagValue_Object = MibScalar
w2kStatusCpuTotalLoadLagValue = _W2kStatusCpuTotalLoadLagValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 2, 2),
    _W2kStatusCpuTotalLoadLagValue_Type()
)
w2kStatusCpuTotalLoadLagValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusCpuTotalLoadLagValue.setStatus("mandatory")


class _W2kStatusCpuTotalLoadLag_Type(Integer32):
    """Custom type w2kStatusCpuTotalLoadLag based on Integer32"""
    defaultValue = 3


_W2kStatusCpuTotalLoadLag_Object = MibScalar
w2kStatusCpuTotalLoadLag = _W2kStatusCpuTotalLoadLag_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 2, 3),
    _W2kStatusCpuTotalLoadLag_Type()
)
w2kStatusCpuTotalLoadLag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusCpuTotalLoadLag.setStatus("mandatory")


class _W2kStatusCpuTotalLoadWarn_Type(Integer32):
    """Custom type w2kStatusCpuTotalLoadWarn based on Integer32"""
    defaultValue = 70


_W2kStatusCpuTotalLoadWarn_Object = MibScalar
w2kStatusCpuTotalLoadWarn = _W2kStatusCpuTotalLoadWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 2, 4),
    _W2kStatusCpuTotalLoadWarn_Type()
)
w2kStatusCpuTotalLoadWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusCpuTotalLoadWarn.setStatus("mandatory")


class _W2kStatusCpuTotalLoadCrit_Type(Integer32):
    """Custom type w2kStatusCpuTotalLoadCrit based on Integer32"""
    defaultValue = 90


_W2kStatusCpuTotalLoadCrit_Object = MibScalar
w2kStatusCpuTotalLoadCrit = _W2kStatusCpuTotalLoadCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 2, 5),
    _W2kStatusCpuTotalLoadCrit_Type()
)
w2kStatusCpuTotalLoadCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusCpuTotalLoadCrit.setStatus("mandatory")


class _W2kStatusCpuTotalLoadMonitor_Type(Integer32):
    """Custom type w2kStatusCpuTotalLoadMonitor based on Integer32"""
    defaultValue = 4

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
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_W2kStatusCpuTotalLoadMonitor_Type.__name__ = "Integer32"
_W2kStatusCpuTotalLoadMonitor_Object = MibScalar
w2kStatusCpuTotalLoadMonitor = _W2kStatusCpuTotalLoadMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 2, 6),
    _W2kStatusCpuTotalLoadMonitor_Type()
)
w2kStatusCpuTotalLoadMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusCpuTotalLoadMonitor.setStatus("mandatory")


class _W2kStatusCpuTotalLoadStatus_Type(Integer32):
    """Custom type w2kStatusCpuTotalLoadStatus based on Integer32"""
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
        *(("critical", 4),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_W2kStatusCpuTotalLoadStatus_Type.__name__ = "Integer32"
_W2kStatusCpuTotalLoadStatus_Object = MibScalar
w2kStatusCpuTotalLoadStatus = _W2kStatusCpuTotalLoadStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 2, 7),
    _W2kStatusCpuTotalLoadStatus_Type()
)
w2kStatusCpuTotalLoadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusCpuTotalLoadStatus.setStatus("mandatory")
_W2kStatusCpuTotalCallBackRef_Type = DisplayString
_W2kStatusCpuTotalCallBackRef_Object = MibScalar
w2kStatusCpuTotalCallBackRef = _W2kStatusCpuTotalCallBackRef_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 2, 8),
    _W2kStatusCpuTotalCallBackRef_Type()
)
w2kStatusCpuTotalCallBackRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusCpuTotalCallBackRef.setStatus("mandatory")
_W2kStatusCpuCount_Type = Integer32
_W2kStatusCpuCount_Object = MibScalar
w2kStatusCpuCount = _W2kStatusCpuCount_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 2, 9),
    _W2kStatusCpuCount_Type()
)
w2kStatusCpuCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusCpuCount.setStatus("mandatory")
_W2kStatusCpuTable_Object = MibTable
w2kStatusCpuTable = _W2kStatusCpuTable_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 2, 10)
)
if mibBuilder.loadTexts:
    w2kStatusCpuTable.setStatus("mandatory")
_W2kStatusCpuEntry_Object = MibTableRow
w2kStatusCpuEntry = _W2kStatusCpuEntry_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 2, 10, 1)
)
w2kStatusCpuEntry.setIndexNames(
    (0, "CA-W2KOS-MIB", "w2kStatusCpuName"),
)
if mibBuilder.loadTexts:
    w2kStatusCpuEntry.setStatus("mandatory")
_W2kStatusCpuName_Type = DisplayString
_W2kStatusCpuName_Object = MibTableColumn
w2kStatusCpuName = _W2kStatusCpuName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 2, 10, 1, 1),
    _W2kStatusCpuName_Type()
)
w2kStatusCpuName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusCpuName.setStatus("mandatory")
_W2kStatusCpuType_Type = DisplayString
_W2kStatusCpuType_Object = MibTableColumn
w2kStatusCpuType = _W2kStatusCpuType_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 2, 10, 1, 2),
    _W2kStatusCpuType_Type()
)
w2kStatusCpuType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusCpuType.setStatus("mandatory")


class _W2kStatusCpuAggStatus_Type(Integer32):
    """Custom type w2kStatusCpuAggStatus based on Integer32"""
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
        *(("critical", 4),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_W2kStatusCpuAggStatus_Type.__name__ = "Integer32"
_W2kStatusCpuAggStatus_Object = MibTableColumn
w2kStatusCpuAggStatus = _W2kStatusCpuAggStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 2, 10, 1, 3),
    _W2kStatusCpuAggStatus_Type()
)
w2kStatusCpuAggStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusCpuAggStatus.setStatus("mandatory")
_W2kStatusCpuLoadValue_Type = Integer32
_W2kStatusCpuLoadValue_Object = MibTableColumn
w2kStatusCpuLoadValue = _W2kStatusCpuLoadValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 2, 10, 1, 4),
    _W2kStatusCpuLoadValue_Type()
)
w2kStatusCpuLoadValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusCpuLoadValue.setStatus("mandatory")
_W2kStatusCpuLoadLagValue_Type = Integer32
_W2kStatusCpuLoadLagValue_Object = MibTableColumn
w2kStatusCpuLoadLagValue = _W2kStatusCpuLoadLagValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 2, 10, 1, 5),
    _W2kStatusCpuLoadLagValue_Type()
)
w2kStatusCpuLoadLagValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusCpuLoadLagValue.setStatus("mandatory")
_W2kStatusCpuLoadLag_Type = Integer32
_W2kStatusCpuLoadLag_Object = MibTableColumn
w2kStatusCpuLoadLag = _W2kStatusCpuLoadLag_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 2, 10, 1, 6),
    _W2kStatusCpuLoadLag_Type()
)
w2kStatusCpuLoadLag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusCpuLoadLag.setStatus("mandatory")
_W2kStatusCpuLoadWarn_Type = Integer32
_W2kStatusCpuLoadWarn_Object = MibTableColumn
w2kStatusCpuLoadWarn = _W2kStatusCpuLoadWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 2, 10, 1, 7),
    _W2kStatusCpuLoadWarn_Type()
)
w2kStatusCpuLoadWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusCpuLoadWarn.setStatus("mandatory")
_W2kStatusCpuLoadCrit_Type = Integer32
_W2kStatusCpuLoadCrit_Object = MibTableColumn
w2kStatusCpuLoadCrit = _W2kStatusCpuLoadCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 2, 10, 1, 8),
    _W2kStatusCpuLoadCrit_Type()
)
w2kStatusCpuLoadCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusCpuLoadCrit.setStatus("mandatory")


class _W2kStatusCpuLoadMonitor_Type(Integer32):
    """Custom type w2kStatusCpuLoadMonitor based on Integer32"""
    defaultValue = 0

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
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_W2kStatusCpuLoadMonitor_Type.__name__ = "Integer32"
_W2kStatusCpuLoadMonitor_Object = MibTableColumn
w2kStatusCpuLoadMonitor = _W2kStatusCpuLoadMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 2, 10, 1, 9),
    _W2kStatusCpuLoadMonitor_Type()
)
w2kStatusCpuLoadMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusCpuLoadMonitor.setStatus("mandatory")


class _W2kStatusCpuLoadStatus_Type(Integer32):
    """Custom type w2kStatusCpuLoadStatus based on Integer32"""
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
        *(("critical", 4),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_W2kStatusCpuLoadStatus_Type.__name__ = "Integer32"
_W2kStatusCpuLoadStatus_Object = MibTableColumn
w2kStatusCpuLoadStatus = _W2kStatusCpuLoadStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 2, 10, 1, 10),
    _W2kStatusCpuLoadStatus_Type()
)
w2kStatusCpuLoadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusCpuLoadStatus.setStatus("mandatory")


class _W2kStatusCpuLossAction_Type(Integer32):
    """Custom type w2kStatusCpuLossAction based on Integer32"""
    defaultValue = 0

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
        *(("down-critical", 4),
          ("down-warning", 3),
          ("remove", 1),
          ("up", 2))
    )


_W2kStatusCpuLossAction_Type.__name__ = "Integer32"
_W2kStatusCpuLossAction_Object = MibTableColumn
w2kStatusCpuLossAction = _W2kStatusCpuLossAction_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 2, 10, 1, 11),
    _W2kStatusCpuLossAction_Type()
)
w2kStatusCpuLossAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusCpuLossAction.setStatus("mandatory")


class _W2kStatusCpuLossStatus_Type(Integer32):
    """Custom type w2kStatusCpuLossStatus based on Integer32"""
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
        *(("down-critical", 4),
          ("down-warning", 3),
          ("unknown", 1),
          ("up", 2))
    )


_W2kStatusCpuLossStatus_Type.__name__ = "Integer32"
_W2kStatusCpuLossStatus_Object = MibTableColumn
w2kStatusCpuLossStatus = _W2kStatusCpuLossStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 2, 10, 1, 12),
    _W2kStatusCpuLossStatus_Type()
)
w2kStatusCpuLossStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusCpuLossStatus.setStatus("mandatory")
_W2kStatusCpuCallBackRef_Type = DisplayString
_W2kStatusCpuCallBackRef_Object = MibTableColumn
w2kStatusCpuCallBackRef = _W2kStatusCpuCallBackRef_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 2, 10, 1, 13),
    _W2kStatusCpuCallBackRef_Type()
)
w2kStatusCpuCallBackRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusCpuCallBackRef.setStatus("mandatory")
_W2kStatusMemGroup_ObjectIdentity = ObjectIdentity
w2kStatusMemGroup = _W2kStatusMemGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 3)
)
_W2kStatusMemVirtTotal_Type = Integer32
_W2kStatusMemVirtTotal_Object = MibScalar
w2kStatusMemVirtTotal = _W2kStatusMemVirtTotal_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 3, 1),
    _W2kStatusMemVirtTotal_Type()
)
w2kStatusMemVirtTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusMemVirtTotal.setStatus("mandatory")
_W2kStatusMemVirtValue_Type = Integer32
_W2kStatusMemVirtValue_Object = MibScalar
w2kStatusMemVirtValue = _W2kStatusMemVirtValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 3, 2),
    _W2kStatusMemVirtValue_Type()
)
w2kStatusMemVirtValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusMemVirtValue.setStatus("mandatory")
_W2kStatusMemVirtLagValue_Type = Integer32
_W2kStatusMemVirtLagValue_Object = MibScalar
w2kStatusMemVirtLagValue = _W2kStatusMemVirtLagValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 3, 3),
    _W2kStatusMemVirtLagValue_Type()
)
w2kStatusMemVirtLagValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusMemVirtLagValue.setStatus("mandatory")


class _W2kStatusMemVirtLag_Type(Integer32):
    """Custom type w2kStatusMemVirtLag based on Integer32"""
    defaultValue = 3


_W2kStatusMemVirtLag_Object = MibScalar
w2kStatusMemVirtLag = _W2kStatusMemVirtLag_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 3, 4),
    _W2kStatusMemVirtLag_Type()
)
w2kStatusMemVirtLag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusMemVirtLag.setStatus("mandatory")
_W2kStatusMemVirtWarnValue_Type = Integer32
_W2kStatusMemVirtWarnValue_Object = MibScalar
w2kStatusMemVirtWarnValue = _W2kStatusMemVirtWarnValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 3, 5),
    _W2kStatusMemVirtWarnValue_Type()
)
w2kStatusMemVirtWarnValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusMemVirtWarnValue.setStatus("mandatory")
_W2kStatusMemVirtCritValue_Type = Integer32
_W2kStatusMemVirtCritValue_Object = MibScalar
w2kStatusMemVirtCritValue = _W2kStatusMemVirtCritValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 3, 6),
    _W2kStatusMemVirtCritValue_Type()
)
w2kStatusMemVirtCritValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusMemVirtCritValue.setStatus("mandatory")


class _W2kStatusMemVirtWarn_Type(DisplayString):
    """Custom type w2kStatusMemVirtWarn based on DisplayString"""
    defaultValue = OctetString("70%")


_W2kStatusMemVirtWarn_Object = MibScalar
w2kStatusMemVirtWarn = _W2kStatusMemVirtWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 3, 7),
    _W2kStatusMemVirtWarn_Type()
)
w2kStatusMemVirtWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusMemVirtWarn.setStatus("mandatory")


class _W2kStatusMemVirtCrit_Type(DisplayString):
    """Custom type w2kStatusMemVirtCrit based on DisplayString"""
    defaultValue = OctetString("90%")


_W2kStatusMemVirtCrit_Object = MibScalar
w2kStatusMemVirtCrit = _W2kStatusMemVirtCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 3, 8),
    _W2kStatusMemVirtCrit_Type()
)
w2kStatusMemVirtCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusMemVirtCrit.setStatus("mandatory")


class _W2kStatusMemVirtMonitor_Type(Integer32):
    """Custom type w2kStatusMemVirtMonitor based on Integer32"""
    defaultValue = 4

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
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_W2kStatusMemVirtMonitor_Type.__name__ = "Integer32"
_W2kStatusMemVirtMonitor_Object = MibScalar
w2kStatusMemVirtMonitor = _W2kStatusMemVirtMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 3, 9),
    _W2kStatusMemVirtMonitor_Type()
)
w2kStatusMemVirtMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusMemVirtMonitor.setStatus("mandatory")


class _W2kStatusMemVirtStatus_Type(Integer32):
    """Custom type w2kStatusMemVirtStatus based on Integer32"""
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
        *(("critical", 4),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_W2kStatusMemVirtStatus_Type.__name__ = "Integer32"
_W2kStatusMemVirtStatus_Object = MibScalar
w2kStatusMemVirtStatus = _W2kStatusMemVirtStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 3, 10),
    _W2kStatusMemVirtStatus_Type()
)
w2kStatusMemVirtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusMemVirtStatus.setStatus("mandatory")
_W2kStatusMemPhysTotal_Type = Integer32
_W2kStatusMemPhysTotal_Object = MibScalar
w2kStatusMemPhysTotal = _W2kStatusMemPhysTotal_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 3, 11),
    _W2kStatusMemPhysTotal_Type()
)
w2kStatusMemPhysTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusMemPhysTotal.setStatus("mandatory")
_W2kStatusMemPhysValue_Type = Integer32
_W2kStatusMemPhysValue_Object = MibScalar
w2kStatusMemPhysValue = _W2kStatusMemPhysValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 3, 12),
    _W2kStatusMemPhysValue_Type()
)
w2kStatusMemPhysValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusMemPhysValue.setStatus("mandatory")
_W2kStatusMemPhysLagValue_Type = Integer32
_W2kStatusMemPhysLagValue_Object = MibScalar
w2kStatusMemPhysLagValue = _W2kStatusMemPhysLagValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 3, 13),
    _W2kStatusMemPhysLagValue_Type()
)
w2kStatusMemPhysLagValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusMemPhysLagValue.setStatus("mandatory")


class _W2kStatusMemPhysLag_Type(Integer32):
    """Custom type w2kStatusMemPhysLag based on Integer32"""
    defaultValue = 3


_W2kStatusMemPhysLag_Object = MibScalar
w2kStatusMemPhysLag = _W2kStatusMemPhysLag_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 3, 14),
    _W2kStatusMemPhysLag_Type()
)
w2kStatusMemPhysLag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusMemPhysLag.setStatus("mandatory")
_W2kStatusMemPhysWarnValue_Type = Integer32
_W2kStatusMemPhysWarnValue_Object = MibScalar
w2kStatusMemPhysWarnValue = _W2kStatusMemPhysWarnValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 3, 15),
    _W2kStatusMemPhysWarnValue_Type()
)
w2kStatusMemPhysWarnValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusMemPhysWarnValue.setStatus("mandatory")
_W2kStatusMemPhysCritValue_Type = Integer32
_W2kStatusMemPhysCritValue_Object = MibScalar
w2kStatusMemPhysCritValue = _W2kStatusMemPhysCritValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 3, 16),
    _W2kStatusMemPhysCritValue_Type()
)
w2kStatusMemPhysCritValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusMemPhysCritValue.setStatus("mandatory")


class _W2kStatusMemPhysWarn_Type(DisplayString):
    """Custom type w2kStatusMemPhysWarn based on DisplayString"""
    defaultValue = OctetString("70%")


_W2kStatusMemPhysWarn_Object = MibScalar
w2kStatusMemPhysWarn = _W2kStatusMemPhysWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 3, 17),
    _W2kStatusMemPhysWarn_Type()
)
w2kStatusMemPhysWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusMemPhysWarn.setStatus("mandatory")


class _W2kStatusMemPhysCrit_Type(DisplayString):
    """Custom type w2kStatusMemPhysCrit based on DisplayString"""
    defaultValue = OctetString("90%")


_W2kStatusMemPhysCrit_Object = MibScalar
w2kStatusMemPhysCrit = _W2kStatusMemPhysCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 3, 18),
    _W2kStatusMemPhysCrit_Type()
)
w2kStatusMemPhysCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusMemPhysCrit.setStatus("mandatory")


class _W2kStatusMemPhysMonitor_Type(Integer32):
    """Custom type w2kStatusMemPhysMonitor based on Integer32"""
    defaultValue = 4

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
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_W2kStatusMemPhysMonitor_Type.__name__ = "Integer32"
_W2kStatusMemPhysMonitor_Object = MibScalar
w2kStatusMemPhysMonitor = _W2kStatusMemPhysMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 3, 19),
    _W2kStatusMemPhysMonitor_Type()
)
w2kStatusMemPhysMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusMemPhysMonitor.setStatus("mandatory")


class _W2kStatusMemPhysStatus_Type(Integer32):
    """Custom type w2kStatusMemPhysStatus based on Integer32"""
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
        *(("critical", 4),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_W2kStatusMemPhysStatus_Type.__name__ = "Integer32"
_W2kStatusMemPhysStatus_Object = MibScalar
w2kStatusMemPhysStatus = _W2kStatusMemPhysStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 3, 20),
    _W2kStatusMemPhysStatus_Type()
)
w2kStatusMemPhysStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusMemPhysStatus.setStatus("mandatory")
_W2kStatusMemPageTotal_Type = Integer32
_W2kStatusMemPageTotal_Object = MibScalar
w2kStatusMemPageTotal = _W2kStatusMemPageTotal_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 3, 21),
    _W2kStatusMemPageTotal_Type()
)
w2kStatusMemPageTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusMemPageTotal.setStatus("mandatory")
_W2kStatusMemPageValue_Type = Integer32
_W2kStatusMemPageValue_Object = MibScalar
w2kStatusMemPageValue = _W2kStatusMemPageValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 3, 22),
    _W2kStatusMemPageValue_Type()
)
w2kStatusMemPageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusMemPageValue.setStatus("mandatory")
_W2kStatusMemPageLagValue_Type = Integer32
_W2kStatusMemPageLagValue_Object = MibScalar
w2kStatusMemPageLagValue = _W2kStatusMemPageLagValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 3, 23),
    _W2kStatusMemPageLagValue_Type()
)
w2kStatusMemPageLagValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusMemPageLagValue.setStatus("mandatory")


class _W2kStatusMemPageLag_Type(Integer32):
    """Custom type w2kStatusMemPageLag based on Integer32"""
    defaultValue = 3


_W2kStatusMemPageLag_Object = MibScalar
w2kStatusMemPageLag = _W2kStatusMemPageLag_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 3, 24),
    _W2kStatusMemPageLag_Type()
)
w2kStatusMemPageLag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusMemPageLag.setStatus("mandatory")
_W2kStatusMemPageWarnValue_Type = Integer32
_W2kStatusMemPageWarnValue_Object = MibScalar
w2kStatusMemPageWarnValue = _W2kStatusMemPageWarnValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 3, 25),
    _W2kStatusMemPageWarnValue_Type()
)
w2kStatusMemPageWarnValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusMemPageWarnValue.setStatus("mandatory")
_W2kStatusMemPageCritValue_Type = Integer32
_W2kStatusMemPageCritValue_Object = MibScalar
w2kStatusMemPageCritValue = _W2kStatusMemPageCritValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 3, 26),
    _W2kStatusMemPageCritValue_Type()
)
w2kStatusMemPageCritValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusMemPageCritValue.setStatus("mandatory")


class _W2kStatusMemPageWarn_Type(DisplayString):
    """Custom type w2kStatusMemPageWarn based on DisplayString"""
    defaultValue = OctetString("70%")


_W2kStatusMemPageWarn_Object = MibScalar
w2kStatusMemPageWarn = _W2kStatusMemPageWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 3, 27),
    _W2kStatusMemPageWarn_Type()
)
w2kStatusMemPageWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusMemPageWarn.setStatus("mandatory")


class _W2kStatusMemPageCrit_Type(DisplayString):
    """Custom type w2kStatusMemPageCrit based on DisplayString"""
    defaultValue = OctetString("90%")


_W2kStatusMemPageCrit_Object = MibScalar
w2kStatusMemPageCrit = _W2kStatusMemPageCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 3, 28),
    _W2kStatusMemPageCrit_Type()
)
w2kStatusMemPageCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusMemPageCrit.setStatus("mandatory")


class _W2kStatusMemPageMonitor_Type(Integer32):
    """Custom type w2kStatusMemPageMonitor based on Integer32"""
    defaultValue = 4

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
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_W2kStatusMemPageMonitor_Type.__name__ = "Integer32"
_W2kStatusMemPageMonitor_Object = MibScalar
w2kStatusMemPageMonitor = _W2kStatusMemPageMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 3, 29),
    _W2kStatusMemPageMonitor_Type()
)
w2kStatusMemPageMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusMemPageMonitor.setStatus("mandatory")


class _W2kStatusMemPageStatus_Type(Integer32):
    """Custom type w2kStatusMemPageStatus based on Integer32"""
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
        *(("critical", 4),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_W2kStatusMemPageStatus_Type.__name__ = "Integer32"
_W2kStatusMemPageStatus_Object = MibScalar
w2kStatusMemPageStatus = _W2kStatusMemPageStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 3, 30),
    _W2kStatusMemPageStatus_Type()
)
w2kStatusMemPageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusMemPageStatus.setStatus("mandatory")
_W2kStatusMemCallBackRef_Type = DisplayString
_W2kStatusMemCallBackRef_Object = MibScalar
w2kStatusMemCallBackRef = _W2kStatusMemCallBackRef_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 3, 31),
    _W2kStatusMemCallBackRef_Type()
)
w2kStatusMemCallBackRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusMemCallBackRef.setStatus("mandatory")
_W2kStatusLVolGroup_ObjectIdentity = ObjectIdentity
w2kStatusLVolGroup = _W2kStatusLVolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 4)
)
_W2kStatusLVolCount_Type = Integer32
_W2kStatusLVolCount_Object = MibScalar
w2kStatusLVolCount = _W2kStatusLVolCount_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 4, 1),
    _W2kStatusLVolCount_Type()
)
w2kStatusLVolCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusLVolCount.setStatus("mandatory")
_W2kStatusLVolTable_Object = MibTable
w2kStatusLVolTable = _W2kStatusLVolTable_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 4, 2)
)
if mibBuilder.loadTexts:
    w2kStatusLVolTable.setStatus("mandatory")
_W2kStatusLVolEntry_Object = MibTableRow
w2kStatusLVolEntry = _W2kStatusLVolEntry_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 4, 2, 1)
)
w2kStatusLVolEntry.setIndexNames(
    (0, "CA-W2KOS-MIB", "w2kStatusLVolName"),
)
if mibBuilder.loadTexts:
    w2kStatusLVolEntry.setStatus("mandatory")
_W2kStatusLVolName_Type = DisplayString
_W2kStatusLVolName_Object = MibTableColumn
w2kStatusLVolName = _W2kStatusLVolName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 4, 2, 1, 1),
    _W2kStatusLVolName_Type()
)
w2kStatusLVolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusLVolName.setStatus("mandatory")
_W2kStatusLVolDescription_Type = DisplayString
_W2kStatusLVolDescription_Object = MibTableColumn
w2kStatusLVolDescription = _W2kStatusLVolDescription_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 4, 2, 1, 2),
    _W2kStatusLVolDescription_Type()
)
w2kStatusLVolDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusLVolDescription.setStatus("mandatory")
_W2kStatusLVolMounts_Type = DisplayString
_W2kStatusLVolMounts_Object = MibTableColumn
w2kStatusLVolMounts = _W2kStatusLVolMounts_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 4, 2, 1, 3),
    _W2kStatusLVolMounts_Type()
)
w2kStatusLVolMounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusLVolMounts.setStatus("mandatory")
_W2kStatusLVolInfo_Type = DisplayString
_W2kStatusLVolInfo_Object = MibTableColumn
w2kStatusLVolInfo = _W2kStatusLVolInfo_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 4, 2, 1, 4),
    _W2kStatusLVolInfo_Type()
)
w2kStatusLVolInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusLVolInfo.setStatus("mandatory")
_W2kStatusLVolAutoWatcherName_Type = DisplayString
_W2kStatusLVolAutoWatcherName_Object = MibTableColumn
w2kStatusLVolAutoWatcherName = _W2kStatusLVolAutoWatcherName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 4, 2, 1, 5),
    _W2kStatusLVolAutoWatcherName_Type()
)
w2kStatusLVolAutoWatcherName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusLVolAutoWatcherName.setStatus("mandatory")
_W2kStatusLVolAggLagValue_Type = Integer32
_W2kStatusLVolAggLagValue_Object = MibTableColumn
w2kStatusLVolAggLagValue = _W2kStatusLVolAggLagValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 4, 2, 1, 6),
    _W2kStatusLVolAggLagValue_Type()
)
w2kStatusLVolAggLagValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusLVolAggLagValue.setStatus("mandatory")
_W2kStatusLVolAggLag_Type = Integer32
_W2kStatusLVolAggLag_Object = MibTableColumn
w2kStatusLVolAggLag = _W2kStatusLVolAggLag_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 4, 2, 1, 7),
    _W2kStatusLVolAggLag_Type()
)
w2kStatusLVolAggLag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusLVolAggLag.setStatus("mandatory")


class _W2kStatusLVolAggStatus_Type(Integer32):
    """Custom type w2kStatusLVolAggStatus based on Integer32"""
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
        *(("critical", 4),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_W2kStatusLVolAggStatus_Type.__name__ = "Integer32"
_W2kStatusLVolAggStatus_Object = MibTableColumn
w2kStatusLVolAggStatus = _W2kStatusLVolAggStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 4, 2, 1, 8),
    _W2kStatusLVolAggStatus_Type()
)
w2kStatusLVolAggStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusLVolAggStatus.setStatus("mandatory")
_W2kStatusLVolSizeTotal_Type = Integer32
_W2kStatusLVolSizeTotal_Object = MibTableColumn
w2kStatusLVolSizeTotal = _W2kStatusLVolSizeTotal_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 4, 2, 1, 9),
    _W2kStatusLVolSizeTotal_Type()
)
w2kStatusLVolSizeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusLVolSizeTotal.setStatus("mandatory")
_W2kStatusLVolSizeValue_Type = Integer32
_W2kStatusLVolSizeValue_Object = MibTableColumn
w2kStatusLVolSizeValue = _W2kStatusLVolSizeValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 4, 2, 1, 10),
    _W2kStatusLVolSizeValue_Type()
)
w2kStatusLVolSizeValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusLVolSizeValue.setStatus("mandatory")
_W2kStatusLVolSizeWarnValue_Type = Integer32
_W2kStatusLVolSizeWarnValue_Object = MibTableColumn
w2kStatusLVolSizeWarnValue = _W2kStatusLVolSizeWarnValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 4, 2, 1, 11),
    _W2kStatusLVolSizeWarnValue_Type()
)
w2kStatusLVolSizeWarnValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusLVolSizeWarnValue.setStatus("mandatory")
_W2kStatusLVolSizeCritValue_Type = Integer32
_W2kStatusLVolSizeCritValue_Object = MibTableColumn
w2kStatusLVolSizeCritValue = _W2kStatusLVolSizeCritValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 4, 2, 1, 12),
    _W2kStatusLVolSizeCritValue_Type()
)
w2kStatusLVolSizeCritValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusLVolSizeCritValue.setStatus("mandatory")
_W2kStatusLVolSizeWarn_Type = DisplayString
_W2kStatusLVolSizeWarn_Object = MibTableColumn
w2kStatusLVolSizeWarn = _W2kStatusLVolSizeWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 4, 2, 1, 13),
    _W2kStatusLVolSizeWarn_Type()
)
w2kStatusLVolSizeWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusLVolSizeWarn.setStatus("mandatory")
_W2kStatusLVolSizeCrit_Type = DisplayString
_W2kStatusLVolSizeCrit_Object = MibTableColumn
w2kStatusLVolSizeCrit = _W2kStatusLVolSizeCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 4, 2, 1, 14),
    _W2kStatusLVolSizeCrit_Type()
)
w2kStatusLVolSizeCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusLVolSizeCrit.setStatus("mandatory")


class _W2kStatusLVolSizeMonitor_Type(Integer32):
    """Custom type w2kStatusLVolSizeMonitor based on Integer32"""
    defaultValue = 0

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
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_W2kStatusLVolSizeMonitor_Type.__name__ = "Integer32"
_W2kStatusLVolSizeMonitor_Object = MibTableColumn
w2kStatusLVolSizeMonitor = _W2kStatusLVolSizeMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 4, 2, 1, 15),
    _W2kStatusLVolSizeMonitor_Type()
)
w2kStatusLVolSizeMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusLVolSizeMonitor.setStatus("mandatory")


class _W2kStatusLVolSizeStatus_Type(Integer32):
    """Custom type w2kStatusLVolSizeStatus based on Integer32"""
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
        *(("critical", 4),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_W2kStatusLVolSizeStatus_Type.__name__ = "Integer32"
_W2kStatusLVolSizeStatus_Object = MibTableColumn
w2kStatusLVolSizeStatus = _W2kStatusLVolSizeStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 4, 2, 1, 16),
    _W2kStatusLVolSizeStatus_Type()
)
w2kStatusLVolSizeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusLVolSizeStatus.setStatus("mandatory")
_W2kStatusLVolSizeDValue_Type = Integer32
_W2kStatusLVolSizeDValue_Object = MibTableColumn
w2kStatusLVolSizeDValue = _W2kStatusLVolSizeDValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 4, 2, 1, 17),
    _W2kStatusLVolSizeDValue_Type()
)
w2kStatusLVolSizeDValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusLVolSizeDValue.setStatus("mandatory")
_W2kStatusLVolSizeDWarnValue_Type = DisplayString
_W2kStatusLVolSizeDWarnValue_Object = MibTableColumn
w2kStatusLVolSizeDWarnValue = _W2kStatusLVolSizeDWarnValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 4, 2, 1, 18),
    _W2kStatusLVolSizeDWarnValue_Type()
)
w2kStatusLVolSizeDWarnValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusLVolSizeDWarnValue.setStatus("mandatory")
_W2kStatusLVolSizeDCritValue_Type = DisplayString
_W2kStatusLVolSizeDCritValue_Object = MibTableColumn
w2kStatusLVolSizeDCritValue = _W2kStatusLVolSizeDCritValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 4, 2, 1, 19),
    _W2kStatusLVolSizeDCritValue_Type()
)
w2kStatusLVolSizeDCritValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusLVolSizeDCritValue.setStatus("mandatory")
_W2kStatusLVolSizeDWarn_Type = DisplayString
_W2kStatusLVolSizeDWarn_Object = MibTableColumn
w2kStatusLVolSizeDWarn = _W2kStatusLVolSizeDWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 4, 2, 1, 20),
    _W2kStatusLVolSizeDWarn_Type()
)
w2kStatusLVolSizeDWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusLVolSizeDWarn.setStatus("mandatory")
_W2kStatusLVolSizeDCrit_Type = DisplayString
_W2kStatusLVolSizeDCrit_Object = MibTableColumn
w2kStatusLVolSizeDCrit = _W2kStatusLVolSizeDCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 4, 2, 1, 21),
    _W2kStatusLVolSizeDCrit_Type()
)
w2kStatusLVolSizeDCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusLVolSizeDCrit.setStatus("mandatory")


class _W2kStatusLVolSizeDMonitor_Type(Integer32):
    """Custom type w2kStatusLVolSizeDMonitor based on Integer32"""
    defaultValue = 0

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
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_W2kStatusLVolSizeDMonitor_Type.__name__ = "Integer32"
_W2kStatusLVolSizeDMonitor_Object = MibTableColumn
w2kStatusLVolSizeDMonitor = _W2kStatusLVolSizeDMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 4, 2, 1, 22),
    _W2kStatusLVolSizeDMonitor_Type()
)
w2kStatusLVolSizeDMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusLVolSizeDMonitor.setStatus("mandatory")


class _W2kStatusLVolSizeDStatus_Type(Integer32):
    """Custom type w2kStatusLVolSizeDStatus based on Integer32"""
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
        *(("critical", 4),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_W2kStatusLVolSizeDStatus_Type.__name__ = "Integer32"
_W2kStatusLVolSizeDStatus_Object = MibTableColumn
w2kStatusLVolSizeDStatus = _W2kStatusLVolSizeDStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 4, 2, 1, 23),
    _W2kStatusLVolSizeDStatus_Type()
)
w2kStatusLVolSizeDStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusLVolSizeDStatus.setStatus("mandatory")
_W2kStatusLVolTPutValue_Type = Integer32
_W2kStatusLVolTPutValue_Object = MibTableColumn
w2kStatusLVolTPutValue = _W2kStatusLVolTPutValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 4, 2, 1, 24),
    _W2kStatusLVolTPutValue_Type()
)
w2kStatusLVolTPutValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusLVolTPutValue.setStatus("mandatory")
_W2kStatusLVolTPutWarn_Type = Integer32
_W2kStatusLVolTPutWarn_Object = MibTableColumn
w2kStatusLVolTPutWarn = _W2kStatusLVolTPutWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 4, 2, 1, 25),
    _W2kStatusLVolTPutWarn_Type()
)
w2kStatusLVolTPutWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusLVolTPutWarn.setStatus("mandatory")
_W2kStatusLVolTPutCrit_Type = Integer32
_W2kStatusLVolTPutCrit_Object = MibTableColumn
w2kStatusLVolTPutCrit = _W2kStatusLVolTPutCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 4, 2, 1, 26),
    _W2kStatusLVolTPutCrit_Type()
)
w2kStatusLVolTPutCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusLVolTPutCrit.setStatus("mandatory")


class _W2kStatusLVolTPutMonitor_Type(Integer32):
    """Custom type w2kStatusLVolTPutMonitor based on Integer32"""
    defaultValue = 0

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
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_W2kStatusLVolTPutMonitor_Type.__name__ = "Integer32"
_W2kStatusLVolTPutMonitor_Object = MibTableColumn
w2kStatusLVolTPutMonitor = _W2kStatusLVolTPutMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 4, 2, 1, 27),
    _W2kStatusLVolTPutMonitor_Type()
)
w2kStatusLVolTPutMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusLVolTPutMonitor.setStatus("mandatory")


class _W2kStatusLVolTPutStatus_Type(Integer32):
    """Custom type w2kStatusLVolTPutStatus based on Integer32"""
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
        *(("critical", 4),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_W2kStatusLVolTPutStatus_Type.__name__ = "Integer32"
_W2kStatusLVolTPutStatus_Object = MibTableColumn
w2kStatusLVolTPutStatus = _W2kStatusLVolTPutStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 4, 2, 1, 28),
    _W2kStatusLVolTPutStatus_Type()
)
w2kStatusLVolTPutStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusLVolTPutStatus.setStatus("mandatory")
_W2kStatusLVolFragValue_Type = Integer32
_W2kStatusLVolFragValue_Object = MibTableColumn
w2kStatusLVolFragValue = _W2kStatusLVolFragValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 4, 2, 1, 29),
    _W2kStatusLVolFragValue_Type()
)
w2kStatusLVolFragValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusLVolFragValue.setStatus("mandatory")
_W2kStatusLVolFragWarn_Type = Integer32
_W2kStatusLVolFragWarn_Object = MibTableColumn
w2kStatusLVolFragWarn = _W2kStatusLVolFragWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 4, 2, 1, 30),
    _W2kStatusLVolFragWarn_Type()
)
w2kStatusLVolFragWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusLVolFragWarn.setStatus("mandatory")
_W2kStatusLVolFragCrit_Type = Integer32
_W2kStatusLVolFragCrit_Object = MibTableColumn
w2kStatusLVolFragCrit = _W2kStatusLVolFragCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 4, 2, 1, 31),
    _W2kStatusLVolFragCrit_Type()
)
w2kStatusLVolFragCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusLVolFragCrit.setStatus("mandatory")


class _W2kStatusLVolFragMonitor_Type(Integer32):
    """Custom type w2kStatusLVolFragMonitor based on Integer32"""
    defaultValue = 0

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
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_W2kStatusLVolFragMonitor_Type.__name__ = "Integer32"
_W2kStatusLVolFragMonitor_Object = MibTableColumn
w2kStatusLVolFragMonitor = _W2kStatusLVolFragMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 4, 2, 1, 32),
    _W2kStatusLVolFragMonitor_Type()
)
w2kStatusLVolFragMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusLVolFragMonitor.setStatus("mandatory")


class _W2kStatusLVolFragStatus_Type(Integer32):
    """Custom type w2kStatusLVolFragStatus based on Integer32"""
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
        *(("critical", 4),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_W2kStatusLVolFragStatus_Type.__name__ = "Integer32"
_W2kStatusLVolFragStatus_Object = MibTableColumn
w2kStatusLVolFragStatus = _W2kStatusLVolFragStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 4, 2, 1, 33),
    _W2kStatusLVolFragStatus_Type()
)
w2kStatusLVolFragStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusLVolFragStatus.setStatus("mandatory")


class _W2kStatusLVolLossAction_Type(Integer32):
    """Custom type w2kStatusLVolLossAction based on Integer32"""
    defaultValue = 0

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
        *(("down-critical", 4),
          ("down-warning", 3),
          ("remove", 1),
          ("up", 2))
    )


_W2kStatusLVolLossAction_Type.__name__ = "Integer32"
_W2kStatusLVolLossAction_Object = MibTableColumn
w2kStatusLVolLossAction = _W2kStatusLVolLossAction_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 4, 2, 1, 34),
    _W2kStatusLVolLossAction_Type()
)
w2kStatusLVolLossAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusLVolLossAction.setStatus("mandatory")


class _W2kStatusLVolLossStatus_Type(Integer32):
    """Custom type w2kStatusLVolLossStatus based on Integer32"""
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
        *(("down-critical", 4),
          ("down-warning", 3),
          ("unknown", 1),
          ("up", 2))
    )


_W2kStatusLVolLossStatus_Type.__name__ = "Integer32"
_W2kStatusLVolLossStatus_Object = MibTableColumn
w2kStatusLVolLossStatus = _W2kStatusLVolLossStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 4, 2, 1, 35),
    _W2kStatusLVolLossStatus_Type()
)
w2kStatusLVolLossStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusLVolLossStatus.setStatus("mandatory")
_W2kStatusLVolCallBackRef_Type = DisplayString
_W2kStatusLVolCallBackRef_Object = MibTableColumn
w2kStatusLVolCallBackRef = _W2kStatusLVolCallBackRef_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 4, 2, 1, 36),
    _W2kStatusLVolCallBackRef_Type()
)
w2kStatusLVolCallBackRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusLVolCallBackRef.setStatus("mandatory")


class _W2kStatusLVolButton_Type(Integer32):
    """Custom type w2kStatusLVolButton based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("remove", 2))
    )


_W2kStatusLVolButton_Type.__name__ = "Integer32"
_W2kStatusLVolButton_Object = MibTableColumn
w2kStatusLVolButton = _W2kStatusLVolButton_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 4, 2, 1, 37),
    _W2kStatusLVolButton_Type()
)
w2kStatusLVolButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusLVolButton.setStatus("mandatory")
_W2kStatusMntGroup_ObjectIdentity = ObjectIdentity
w2kStatusMntGroup = _W2kStatusMntGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 5)
)
_W2kStatusMntCount_Type = Integer32
_W2kStatusMntCount_Object = MibScalar
w2kStatusMntCount = _W2kStatusMntCount_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 5, 1),
    _W2kStatusMntCount_Type()
)
w2kStatusMntCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusMntCount.setStatus("mandatory")
_W2kStatusMntTable_Object = MibTable
w2kStatusMntTable = _W2kStatusMntTable_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 5, 2)
)
if mibBuilder.loadTexts:
    w2kStatusMntTable.setStatus("mandatory")
_W2kStatusMntEntry_Object = MibTableRow
w2kStatusMntEntry = _W2kStatusMntEntry_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 5, 2, 1)
)
w2kStatusMntEntry.setIndexNames(
    (0, "CA-W2KOS-MIB", "w2kStatusMntName"),
)
if mibBuilder.loadTexts:
    w2kStatusMntEntry.setStatus("mandatory")
_W2kStatusMntName_Type = DisplayString
_W2kStatusMntName_Object = MibTableColumn
w2kStatusMntName = _W2kStatusMntName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 5, 2, 1, 1),
    _W2kStatusMntName_Type()
)
w2kStatusMntName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusMntName.setStatus("mandatory")
_W2kStatusMntDescription_Type = DisplayString
_W2kStatusMntDescription_Object = MibTableColumn
w2kStatusMntDescription = _W2kStatusMntDescription_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 5, 2, 1, 2),
    _W2kStatusMntDescription_Type()
)
w2kStatusMntDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusMntDescription.setStatus("mandatory")
_W2kStatusMntAutoWatcherName_Type = DisplayString
_W2kStatusMntAutoWatcherName_Object = MibTableColumn
w2kStatusMntAutoWatcherName = _W2kStatusMntAutoWatcherName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 5, 2, 1, 3),
    _W2kStatusMntAutoWatcherName_Type()
)
w2kStatusMntAutoWatcherName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusMntAutoWatcherName.setStatus("mandatory")
_W2kStatusMntAggLagValue_Type = Integer32
_W2kStatusMntAggLagValue_Object = MibTableColumn
w2kStatusMntAggLagValue = _W2kStatusMntAggLagValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 5, 2, 1, 4),
    _W2kStatusMntAggLagValue_Type()
)
w2kStatusMntAggLagValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusMntAggLagValue.setStatus("mandatory")
_W2kStatusMntAggLag_Type = Integer32
_W2kStatusMntAggLag_Object = MibTableColumn
w2kStatusMntAggLag = _W2kStatusMntAggLag_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 5, 2, 1, 5),
    _W2kStatusMntAggLag_Type()
)
w2kStatusMntAggLag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusMntAggLag.setStatus("mandatory")


class _W2kStatusMntAggStatus_Type(Integer32):
    """Custom type w2kStatusMntAggStatus based on Integer32"""
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
        *(("critical", 4),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_W2kStatusMntAggStatus_Type.__name__ = "Integer32"
_W2kStatusMntAggStatus_Object = MibTableColumn
w2kStatusMntAggStatus = _W2kStatusMntAggStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 5, 2, 1, 6),
    _W2kStatusMntAggStatus_Type()
)
w2kStatusMntAggStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusMntAggStatus.setStatus("mandatory")
_W2kStatusMntRelToValue_Type = DisplayString
_W2kStatusMntRelToValue_Object = MibTableColumn
w2kStatusMntRelToValue = _W2kStatusMntRelToValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 5, 2, 1, 7),
    _W2kStatusMntRelToValue_Type()
)
w2kStatusMntRelToValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusMntRelToValue.setStatus("mandatory")
_W2kStatusMntRelToRef_Type = DisplayString
_W2kStatusMntRelToRef_Object = MibTableColumn
w2kStatusMntRelToRef = _W2kStatusMntRelToRef_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 5, 2, 1, 8),
    _W2kStatusMntRelToRef_Type()
)
w2kStatusMntRelToRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusMntRelToRef.setStatus("mandatory")


class _W2kStatusMntRelToMonitor_Type(Integer32):
    """Custom type w2kStatusMntRelToMonitor based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("do-not-monitor", 1),
          ("down-critical", 3),
          ("down-warning", 2))
    )


_W2kStatusMntRelToMonitor_Type.__name__ = "Integer32"
_W2kStatusMntRelToMonitor_Object = MibTableColumn
w2kStatusMntRelToMonitor = _W2kStatusMntRelToMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 5, 2, 1, 9),
    _W2kStatusMntRelToMonitor_Type()
)
w2kStatusMntRelToMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusMntRelToMonitor.setStatus("mandatory")


class _W2kStatusMntRelToStatus_Type(Integer32):
    """Custom type w2kStatusMntRelToStatus based on Integer32"""
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
        *(("down-critical", 4),
          ("down-warning", 3),
          ("unknown", 1),
          ("up", 2))
    )


_W2kStatusMntRelToStatus_Type.__name__ = "Integer32"
_W2kStatusMntRelToStatus_Object = MibTableColumn
w2kStatusMntRelToStatus = _W2kStatusMntRelToStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 5, 2, 1, 10),
    _W2kStatusMntRelToStatus_Type()
)
w2kStatusMntRelToStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusMntRelToStatus.setStatus("mandatory")


class _W2kStatusMntLossAction_Type(Integer32):
    """Custom type w2kStatusMntLossAction based on Integer32"""
    defaultValue = 0

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
        *(("down-critical", 4),
          ("down-warning", 3),
          ("remove", 1),
          ("up", 2))
    )


_W2kStatusMntLossAction_Type.__name__ = "Integer32"
_W2kStatusMntLossAction_Object = MibTableColumn
w2kStatusMntLossAction = _W2kStatusMntLossAction_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 5, 2, 1, 11),
    _W2kStatusMntLossAction_Type()
)
w2kStatusMntLossAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusMntLossAction.setStatus("mandatory")


class _W2kStatusMntLossStatus_Type(Integer32):
    """Custom type w2kStatusMntLossStatus based on Integer32"""
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
        *(("down-critical", 4),
          ("down-warning", 3),
          ("unknown", 1),
          ("up", 2))
    )


_W2kStatusMntLossStatus_Type.__name__ = "Integer32"
_W2kStatusMntLossStatus_Object = MibTableColumn
w2kStatusMntLossStatus = _W2kStatusMntLossStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 5, 2, 1, 12),
    _W2kStatusMntLossStatus_Type()
)
w2kStatusMntLossStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusMntLossStatus.setStatus("mandatory")
_W2kStatusMntCallBackRef_Type = DisplayString
_W2kStatusMntCallBackRef_Object = MibTableColumn
w2kStatusMntCallBackRef = _W2kStatusMntCallBackRef_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 5, 2, 1, 13),
    _W2kStatusMntCallBackRef_Type()
)
w2kStatusMntCallBackRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusMntCallBackRef.setStatus("mandatory")


class _W2kStatusMntButton_Type(Integer32):
    """Custom type w2kStatusMntButton based on Integer32"""
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
          ("remove", 2),
          ("reset-relTo", 3))
    )


_W2kStatusMntButton_Type.__name__ = "Integer32"
_W2kStatusMntButton_Object = MibTableColumn
w2kStatusMntButton = _W2kStatusMntButton_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 5, 2, 1, 14),
    _W2kStatusMntButton_Type()
)
w2kStatusMntButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusMntButton.setStatus("mandatory")
_W2kStatusDfsGroup_ObjectIdentity = ObjectIdentity
w2kStatusDfsGroup = _W2kStatusDfsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 6)
)
_W2kStatusDfsCount_Type = Integer32
_W2kStatusDfsCount_Object = MibScalar
w2kStatusDfsCount = _W2kStatusDfsCount_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 6, 1),
    _W2kStatusDfsCount_Type()
)
w2kStatusDfsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusDfsCount.setStatus("mandatory")
_W2kStatusDfsTable_Object = MibTable
w2kStatusDfsTable = _W2kStatusDfsTable_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 6, 2)
)
if mibBuilder.loadTexts:
    w2kStatusDfsTable.setStatus("mandatory")
_W2kStatusDfsEntry_Object = MibTableRow
w2kStatusDfsEntry = _W2kStatusDfsEntry_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 6, 2, 1)
)
w2kStatusDfsEntry.setIndexNames(
    (0, "CA-W2KOS-MIB", "w2kStatusDfsName"),
)
if mibBuilder.loadTexts:
    w2kStatusDfsEntry.setStatus("mandatory")
_W2kStatusDfsName_Type = DisplayString
_W2kStatusDfsName_Object = MibTableColumn
w2kStatusDfsName = _W2kStatusDfsName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 6, 2, 1, 1),
    _W2kStatusDfsName_Type()
)
w2kStatusDfsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusDfsName.setStatus("mandatory")
_W2kStatusDfsDescription_Type = DisplayString
_W2kStatusDfsDescription_Object = MibTableColumn
w2kStatusDfsDescription = _W2kStatusDfsDescription_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 6, 2, 1, 2),
    _W2kStatusDfsDescription_Type()
)
w2kStatusDfsDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusDfsDescription.setStatus("mandatory")
_W2kStatusDfsIds_Type = DisplayString
_W2kStatusDfsIds_Object = MibTableColumn
w2kStatusDfsIds = _W2kStatusDfsIds_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 6, 2, 1, 3),
    _W2kStatusDfsIds_Type()
)
w2kStatusDfsIds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusDfsIds.setStatus("mandatory")
_W2kStatusDfsAutoWatcherName_Type = DisplayString
_W2kStatusDfsAutoWatcherName_Object = MibTableColumn
w2kStatusDfsAutoWatcherName = _W2kStatusDfsAutoWatcherName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 6, 2, 1, 4),
    _W2kStatusDfsAutoWatcherName_Type()
)
w2kStatusDfsAutoWatcherName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusDfsAutoWatcherName.setStatus("mandatory")
_W2kStatusDfsAggLagValue_Type = Integer32
_W2kStatusDfsAggLagValue_Object = MibTableColumn
w2kStatusDfsAggLagValue = _W2kStatusDfsAggLagValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 6, 2, 1, 5),
    _W2kStatusDfsAggLagValue_Type()
)
w2kStatusDfsAggLagValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusDfsAggLagValue.setStatus("mandatory")
_W2kStatusDfsAggLag_Type = Integer32
_W2kStatusDfsAggLag_Object = MibTableColumn
w2kStatusDfsAggLag = _W2kStatusDfsAggLag_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 6, 2, 1, 6),
    _W2kStatusDfsAggLag_Type()
)
w2kStatusDfsAggLag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusDfsAggLag.setStatus("mandatory")


class _W2kStatusDfsAggStatus_Type(Integer32):
    """Custom type w2kStatusDfsAggStatus based on Integer32"""
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
        *(("critical", 4),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_W2kStatusDfsAggStatus_Type.__name__ = "Integer32"
_W2kStatusDfsAggStatus_Object = MibTableColumn
w2kStatusDfsAggStatus = _W2kStatusDfsAggStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 6, 2, 1, 7),
    _W2kStatusDfsAggStatus_Type()
)
w2kStatusDfsAggStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusDfsAggStatus.setStatus("mandatory")
_W2kStatusDfsReplicaTotal_Type = Integer32
_W2kStatusDfsReplicaTotal_Object = MibTableColumn
w2kStatusDfsReplicaTotal = _W2kStatusDfsReplicaTotal_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 6, 2, 1, 8),
    _W2kStatusDfsReplicaTotal_Type()
)
w2kStatusDfsReplicaTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusDfsReplicaTotal.setStatus("mandatory")
_W2kStatusDfsReplicaValue_Type = Integer32
_W2kStatusDfsReplicaValue_Object = MibTableColumn
w2kStatusDfsReplicaValue = _W2kStatusDfsReplicaValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 6, 2, 1, 9),
    _W2kStatusDfsReplicaValue_Type()
)
w2kStatusDfsReplicaValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusDfsReplicaValue.setStatus("mandatory")
_W2kStatusDfsReplicaWarn_Type = Integer32
_W2kStatusDfsReplicaWarn_Object = MibTableColumn
w2kStatusDfsReplicaWarn = _W2kStatusDfsReplicaWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 6, 2, 1, 10),
    _W2kStatusDfsReplicaWarn_Type()
)
w2kStatusDfsReplicaWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusDfsReplicaWarn.setStatus("mandatory")
_W2kStatusDfsReplicaCrit_Type = Integer32
_W2kStatusDfsReplicaCrit_Object = MibTableColumn
w2kStatusDfsReplicaCrit = _W2kStatusDfsReplicaCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 6, 2, 1, 11),
    _W2kStatusDfsReplicaCrit_Type()
)
w2kStatusDfsReplicaCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusDfsReplicaCrit.setStatus("mandatory")


class _W2kStatusDfsReplicaMonitor_Type(Integer32):
    """Custom type w2kStatusDfsReplicaMonitor based on Integer32"""
    defaultValue = 0

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
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_W2kStatusDfsReplicaMonitor_Type.__name__ = "Integer32"
_W2kStatusDfsReplicaMonitor_Object = MibTableColumn
w2kStatusDfsReplicaMonitor = _W2kStatusDfsReplicaMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 6, 2, 1, 12),
    _W2kStatusDfsReplicaMonitor_Type()
)
w2kStatusDfsReplicaMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusDfsReplicaMonitor.setStatus("mandatory")


class _W2kStatusDfsReplicaStatus_Type(Integer32):
    """Custom type w2kStatusDfsReplicaStatus based on Integer32"""
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
        *(("critical", 4),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_W2kStatusDfsReplicaStatus_Type.__name__ = "Integer32"
_W2kStatusDfsReplicaStatus_Object = MibTableColumn
w2kStatusDfsReplicaStatus = _W2kStatusDfsReplicaStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 6, 2, 1, 13),
    _W2kStatusDfsReplicaStatus_Type()
)
w2kStatusDfsReplicaStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusDfsReplicaStatus.setStatus("mandatory")


class _W2kStatusDfsLossAction_Type(Integer32):
    """Custom type w2kStatusDfsLossAction based on Integer32"""
    defaultValue = 0

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
        *(("down-critical", 4),
          ("down-warning", 3),
          ("remove", 1),
          ("up", 2))
    )


_W2kStatusDfsLossAction_Type.__name__ = "Integer32"
_W2kStatusDfsLossAction_Object = MibTableColumn
w2kStatusDfsLossAction = _W2kStatusDfsLossAction_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 6, 2, 1, 14),
    _W2kStatusDfsLossAction_Type()
)
w2kStatusDfsLossAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusDfsLossAction.setStatus("mandatory")


class _W2kStatusDfsLossStatus_Type(Integer32):
    """Custom type w2kStatusDfsLossStatus based on Integer32"""
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
        *(("down-critical", 4),
          ("down-warning", 3),
          ("unknown", 1),
          ("up", 2))
    )


_W2kStatusDfsLossStatus_Type.__name__ = "Integer32"
_W2kStatusDfsLossStatus_Object = MibTableColumn
w2kStatusDfsLossStatus = _W2kStatusDfsLossStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 6, 2, 1, 15),
    _W2kStatusDfsLossStatus_Type()
)
w2kStatusDfsLossStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusDfsLossStatus.setStatus("mandatory")
_W2kStatusDfsCallBackRef_Type = DisplayString
_W2kStatusDfsCallBackRef_Object = MibTableColumn
w2kStatusDfsCallBackRef = _W2kStatusDfsCallBackRef_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 6, 2, 1, 16),
    _W2kStatusDfsCallBackRef_Type()
)
w2kStatusDfsCallBackRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusDfsCallBackRef.setStatus("mandatory")


class _W2kStatusDfsButton_Type(Integer32):
    """Custom type w2kStatusDfsButton based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("remove", 2))
    )


_W2kStatusDfsButton_Type.__name__ = "Integer32"
_W2kStatusDfsButton_Object = MibTableColumn
w2kStatusDfsButton = _W2kStatusDfsButton_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 6, 2, 1, 17),
    _W2kStatusDfsButton_Type()
)
w2kStatusDfsButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusDfsButton.setStatus("mandatory")
_W2kStatusQuotGroup_ObjectIdentity = ObjectIdentity
w2kStatusQuotGroup = _W2kStatusQuotGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 7)
)
_W2kStatusQuotCount_Type = Integer32
_W2kStatusQuotCount_Object = MibScalar
w2kStatusQuotCount = _W2kStatusQuotCount_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 7, 1),
    _W2kStatusQuotCount_Type()
)
w2kStatusQuotCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusQuotCount.setStatus("mandatory")
_W2kStatusQuotTable_Object = MibTable
w2kStatusQuotTable = _W2kStatusQuotTable_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 7, 2)
)
if mibBuilder.loadTexts:
    w2kStatusQuotTable.setStatus("mandatory")
_W2kStatusQuotEntry_Object = MibTableRow
w2kStatusQuotEntry = _W2kStatusQuotEntry_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 7, 2, 1)
)
w2kStatusQuotEntry.setIndexNames(
    (0, "CA-W2KOS-MIB", "w2kStatusQuotLVolName"),
    (0, "CA-W2KOS-MIB", "w2kStatusQuotUserName"),
)
if mibBuilder.loadTexts:
    w2kStatusQuotEntry.setStatus("mandatory")
_W2kStatusQuotLVolName_Type = DisplayString
_W2kStatusQuotLVolName_Object = MibTableColumn
w2kStatusQuotLVolName = _W2kStatusQuotLVolName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 7, 2, 1, 1),
    _W2kStatusQuotLVolName_Type()
)
w2kStatusQuotLVolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusQuotLVolName.setStatus("mandatory")
_W2kStatusQuotUserName_Type = DisplayString
_W2kStatusQuotUserName_Object = MibTableColumn
w2kStatusQuotUserName = _W2kStatusQuotUserName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 7, 2, 1, 2),
    _W2kStatusQuotUserName_Type()
)
w2kStatusQuotUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusQuotUserName.setStatus("mandatory")
_W2kStatusQuotDescription_Type = DisplayString
_W2kStatusQuotDescription_Object = MibTableColumn
w2kStatusQuotDescription = _W2kStatusQuotDescription_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 7, 2, 1, 3),
    _W2kStatusQuotDescription_Type()
)
w2kStatusQuotDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusQuotDescription.setStatus("mandatory")
_W2kStatusQuotAggLagValue_Type = Integer32
_W2kStatusQuotAggLagValue_Object = MibTableColumn
w2kStatusQuotAggLagValue = _W2kStatusQuotAggLagValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 7, 2, 1, 4),
    _W2kStatusQuotAggLagValue_Type()
)
w2kStatusQuotAggLagValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusQuotAggLagValue.setStatus("mandatory")
_W2kStatusQuotAggLag_Type = Integer32
_W2kStatusQuotAggLag_Object = MibTableColumn
w2kStatusQuotAggLag = _W2kStatusQuotAggLag_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 7, 2, 1, 5),
    _W2kStatusQuotAggLag_Type()
)
w2kStatusQuotAggLag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusQuotAggLag.setStatus("mandatory")


class _W2kStatusQuotAggStatus_Type(Integer32):
    """Custom type w2kStatusQuotAggStatus based on Integer32"""
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
        *(("critical", 4),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_W2kStatusQuotAggStatus_Type.__name__ = "Integer32"
_W2kStatusQuotAggStatus_Object = MibTableColumn
w2kStatusQuotAggStatus = _W2kStatusQuotAggStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 7, 2, 1, 6),
    _W2kStatusQuotAggStatus_Type()
)
w2kStatusQuotAggStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusQuotAggStatus.setStatus("mandatory")


class _W2kStatusQuotExist_Type(Integer32):
    """Custom type w2kStatusQuotExist based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("should-exist", 1),
          ("should-not-exist", 2))
    )


_W2kStatusQuotExist_Type.__name__ = "Integer32"
_W2kStatusQuotExist_Object = MibTableColumn
w2kStatusQuotExist = _W2kStatusQuotExist_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 7, 2, 1, 7),
    _W2kStatusQuotExist_Type()
)
w2kStatusQuotExist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusQuotExist.setStatus("mandatory")


class _W2kStatusQuotExistMonitor_Type(Integer32):
    """Custom type w2kStatusQuotExistMonitor based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("do-not-monitor", 1),
          ("down-critical", 3),
          ("down-warning", 2))
    )


_W2kStatusQuotExistMonitor_Type.__name__ = "Integer32"
_W2kStatusQuotExistMonitor_Object = MibTableColumn
w2kStatusQuotExistMonitor = _W2kStatusQuotExistMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 7, 2, 1, 8),
    _W2kStatusQuotExistMonitor_Type()
)
w2kStatusQuotExistMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusQuotExistMonitor.setStatus("mandatory")


class _W2kStatusQuotExistStatus_Type(Integer32):
    """Custom type w2kStatusQuotExistStatus based on Integer32"""
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
        *(("down-critical", 4),
          ("down-warning", 3),
          ("unknown", 1),
          ("up", 2))
    )


_W2kStatusQuotExistStatus_Type.__name__ = "Integer32"
_W2kStatusQuotExistStatus_Object = MibTableColumn
w2kStatusQuotExistStatus = _W2kStatusQuotExistStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 7, 2, 1, 9),
    _W2kStatusQuotExistStatus_Type()
)
w2kStatusQuotExistStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusQuotExistStatus.setStatus("mandatory")
_W2kStatusQuotSizeValue_Type = Integer32
_W2kStatusQuotSizeValue_Object = MibTableColumn
w2kStatusQuotSizeValue = _W2kStatusQuotSizeValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 7, 2, 1, 10),
    _W2kStatusQuotSizeValue_Type()
)
w2kStatusQuotSizeValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusQuotSizeValue.setStatus("mandatory")
_W2kStatusQuotSizeWarn_Type = Integer32
_W2kStatusQuotSizeWarn_Object = MibTableColumn
w2kStatusQuotSizeWarn = _W2kStatusQuotSizeWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 7, 2, 1, 11),
    _W2kStatusQuotSizeWarn_Type()
)
w2kStatusQuotSizeWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusQuotSizeWarn.setStatus("mandatory")
_W2kStatusQuotSizeCrit_Type = Integer32
_W2kStatusQuotSizeCrit_Object = MibTableColumn
w2kStatusQuotSizeCrit = _W2kStatusQuotSizeCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 7, 2, 1, 12),
    _W2kStatusQuotSizeCrit_Type()
)
w2kStatusQuotSizeCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusQuotSizeCrit.setStatus("mandatory")


class _W2kStatusQuotSizeMonitor_Type(Integer32):
    """Custom type w2kStatusQuotSizeMonitor based on Integer32"""
    defaultValue = 0

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
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_W2kStatusQuotSizeMonitor_Type.__name__ = "Integer32"
_W2kStatusQuotSizeMonitor_Object = MibTableColumn
w2kStatusQuotSizeMonitor = _W2kStatusQuotSizeMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 7, 2, 1, 13),
    _W2kStatusQuotSizeMonitor_Type()
)
w2kStatusQuotSizeMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusQuotSizeMonitor.setStatus("mandatory")


class _W2kStatusQuotSizeStatus_Type(Integer32):
    """Custom type w2kStatusQuotSizeStatus based on Integer32"""
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
        *(("critical", 4),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_W2kStatusQuotSizeStatus_Type.__name__ = "Integer32"
_W2kStatusQuotSizeStatus_Object = MibTableColumn
w2kStatusQuotSizeStatus = _W2kStatusQuotSizeStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 7, 2, 1, 14),
    _W2kStatusQuotSizeStatus_Type()
)
w2kStatusQuotSizeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusQuotSizeStatus.setStatus("mandatory")
_W2kStatusQuotCallBackRef_Type = DisplayString
_W2kStatusQuotCallBackRef_Object = MibTableColumn
w2kStatusQuotCallBackRef = _W2kStatusQuotCallBackRef_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 7, 2, 1, 15),
    _W2kStatusQuotCallBackRef_Type()
)
w2kStatusQuotCallBackRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusQuotCallBackRef.setStatus("mandatory")


class _W2kStatusQuotButton_Type(Integer32):
    """Custom type w2kStatusQuotButton based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("remove", 2))
    )


_W2kStatusQuotButton_Type.__name__ = "Integer32"
_W2kStatusQuotButton_Object = MibTableColumn
w2kStatusQuotButton = _W2kStatusQuotButton_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 7, 2, 1, 16),
    _W2kStatusQuotButton_Type()
)
w2kStatusQuotButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusQuotButton.setStatus("mandatory")
_W2kStatusDirGroup_ObjectIdentity = ObjectIdentity
w2kStatusDirGroup = _W2kStatusDirGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 8)
)
_W2kStatusDirCount_Type = Integer32
_W2kStatusDirCount_Object = MibScalar
w2kStatusDirCount = _W2kStatusDirCount_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 8, 1),
    _W2kStatusDirCount_Type()
)
w2kStatusDirCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusDirCount.setStatus("mandatory")
_W2kStatusDirTable_Object = MibTable
w2kStatusDirTable = _W2kStatusDirTable_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 8, 2)
)
if mibBuilder.loadTexts:
    w2kStatusDirTable.setStatus("mandatory")
_W2kStatusDirEntry_Object = MibTableRow
w2kStatusDirEntry = _W2kStatusDirEntry_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 8, 2, 1)
)
w2kStatusDirEntry.setIndexNames(
    (0, "CA-W2KOS-MIB", "w2kStatusDirName"),
)
if mibBuilder.loadTexts:
    w2kStatusDirEntry.setStatus("mandatory")
_W2kStatusDirName_Type = DisplayString
_W2kStatusDirName_Object = MibTableColumn
w2kStatusDirName = _W2kStatusDirName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 8, 2, 1, 1),
    _W2kStatusDirName_Type()
)
w2kStatusDirName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusDirName.setStatus("mandatory")
_W2kStatusDirDescription_Type = DisplayString
_W2kStatusDirDescription_Object = MibTableColumn
w2kStatusDirDescription = _W2kStatusDirDescription_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 8, 2, 1, 2),
    _W2kStatusDirDescription_Type()
)
w2kStatusDirDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusDirDescription.setStatus("mandatory")
_W2kStatusDirAggLagValue_Type = Integer32
_W2kStatusDirAggLagValue_Object = MibTableColumn
w2kStatusDirAggLagValue = _W2kStatusDirAggLagValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 8, 2, 1, 3),
    _W2kStatusDirAggLagValue_Type()
)
w2kStatusDirAggLagValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusDirAggLagValue.setStatus("mandatory")
_W2kStatusDirAggLag_Type = Integer32
_W2kStatusDirAggLag_Object = MibTableColumn
w2kStatusDirAggLag = _W2kStatusDirAggLag_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 8, 2, 1, 4),
    _W2kStatusDirAggLag_Type()
)
w2kStatusDirAggLag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusDirAggLag.setStatus("mandatory")


class _W2kStatusDirAggStatus_Type(Integer32):
    """Custom type w2kStatusDirAggStatus based on Integer32"""
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
        *(("critical", 4),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_W2kStatusDirAggStatus_Type.__name__ = "Integer32"
_W2kStatusDirAggStatus_Object = MibTableColumn
w2kStatusDirAggStatus = _W2kStatusDirAggStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 8, 2, 1, 5),
    _W2kStatusDirAggStatus_Type()
)
w2kStatusDirAggStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusDirAggStatus.setStatus("mandatory")


class _W2kStatusDirExist_Type(Integer32):
    """Custom type w2kStatusDirExist based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("should-exist", 1),
          ("should-not-exist", 2))
    )


_W2kStatusDirExist_Type.__name__ = "Integer32"
_W2kStatusDirExist_Object = MibTableColumn
w2kStatusDirExist = _W2kStatusDirExist_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 8, 2, 1, 6),
    _W2kStatusDirExist_Type()
)
w2kStatusDirExist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusDirExist.setStatus("mandatory")


class _W2kStatusDirExistMonitor_Type(Integer32):
    """Custom type w2kStatusDirExistMonitor based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("do-not-monitor", 1),
          ("down-critical", 3),
          ("down-warning", 2))
    )


_W2kStatusDirExistMonitor_Type.__name__ = "Integer32"
_W2kStatusDirExistMonitor_Object = MibTableColumn
w2kStatusDirExistMonitor = _W2kStatusDirExistMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 8, 2, 1, 7),
    _W2kStatusDirExistMonitor_Type()
)
w2kStatusDirExistMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusDirExistMonitor.setStatus("mandatory")


class _W2kStatusDirExistStatus_Type(Integer32):
    """Custom type w2kStatusDirExistStatus based on Integer32"""
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
        *(("down-critical", 4),
          ("down-warning", 3),
          ("unknown", 1),
          ("up", 2))
    )


_W2kStatusDirExistStatus_Type.__name__ = "Integer32"
_W2kStatusDirExistStatus_Object = MibTableColumn
w2kStatusDirExistStatus = _W2kStatusDirExistStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 8, 2, 1, 8),
    _W2kStatusDirExistStatus_Type()
)
w2kStatusDirExistStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusDirExistStatus.setStatus("mandatory")
_W2kStatusDirTimeValue_Type = DisplayString
_W2kStatusDirTimeValue_Object = MibTableColumn
w2kStatusDirTimeValue = _W2kStatusDirTimeValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 8, 2, 1, 9),
    _W2kStatusDirTimeValue_Type()
)
w2kStatusDirTimeValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusDirTimeValue.setStatus("mandatory")
_W2kStatusDirTimeRef_Type = DisplayString
_W2kStatusDirTimeRef_Object = MibTableColumn
w2kStatusDirTimeRef = _W2kStatusDirTimeRef_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 8, 2, 1, 10),
    _W2kStatusDirTimeRef_Type()
)
w2kStatusDirTimeRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusDirTimeRef.setStatus("mandatory")


class _W2kStatusDirTimeMonitor_Type(Integer32):
    """Custom type w2kStatusDirTimeMonitor based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("do-not-monitor", 1),
          ("down-critical", 3),
          ("down-warning", 2))
    )


_W2kStatusDirTimeMonitor_Type.__name__ = "Integer32"
_W2kStatusDirTimeMonitor_Object = MibTableColumn
w2kStatusDirTimeMonitor = _W2kStatusDirTimeMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 8, 2, 1, 11),
    _W2kStatusDirTimeMonitor_Type()
)
w2kStatusDirTimeMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusDirTimeMonitor.setStatus("mandatory")


class _W2kStatusDirTimeStatus_Type(Integer32):
    """Custom type w2kStatusDirTimeStatus based on Integer32"""
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
        *(("down-critical", 4),
          ("down-warning", 3),
          ("unknown", 1),
          ("up", 2))
    )


_W2kStatusDirTimeStatus_Type.__name__ = "Integer32"
_W2kStatusDirTimeStatus_Object = MibTableColumn
w2kStatusDirTimeStatus = _W2kStatusDirTimeStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 8, 2, 1, 12),
    _W2kStatusDirTimeStatus_Type()
)
w2kStatusDirTimeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusDirTimeStatus.setStatus("mandatory")
_W2kStatusDirSizeRef_Type = Integer32
_W2kStatusDirSizeRef_Object = MibTableColumn
w2kStatusDirSizeRef = _W2kStatusDirSizeRef_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 8, 2, 1, 13),
    _W2kStatusDirSizeRef_Type()
)
w2kStatusDirSizeRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusDirSizeRef.setStatus("mandatory")
_W2kStatusDirSizeValue_Type = Integer32
_W2kStatusDirSizeValue_Object = MibTableColumn
w2kStatusDirSizeValue = _W2kStatusDirSizeValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 8, 2, 1, 14),
    _W2kStatusDirSizeValue_Type()
)
w2kStatusDirSizeValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusDirSizeValue.setStatus("mandatory")
_W2kStatusDirSizeWarnValue_Type = Integer32
_W2kStatusDirSizeWarnValue_Object = MibTableColumn
w2kStatusDirSizeWarnValue = _W2kStatusDirSizeWarnValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 8, 2, 1, 15),
    _W2kStatusDirSizeWarnValue_Type()
)
w2kStatusDirSizeWarnValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusDirSizeWarnValue.setStatus("mandatory")
_W2kStatusDirSizeCritValue_Type = Integer32
_W2kStatusDirSizeCritValue_Object = MibTableColumn
w2kStatusDirSizeCritValue = _W2kStatusDirSizeCritValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 8, 2, 1, 16),
    _W2kStatusDirSizeCritValue_Type()
)
w2kStatusDirSizeCritValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusDirSizeCritValue.setStatus("mandatory")
_W2kStatusDirSizeWarn_Type = DisplayString
_W2kStatusDirSizeWarn_Object = MibTableColumn
w2kStatusDirSizeWarn = _W2kStatusDirSizeWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 8, 2, 1, 17),
    _W2kStatusDirSizeWarn_Type()
)
w2kStatusDirSizeWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusDirSizeWarn.setStatus("mandatory")
_W2kStatusDirSizeCrit_Type = DisplayString
_W2kStatusDirSizeCrit_Object = MibTableColumn
w2kStatusDirSizeCrit = _W2kStatusDirSizeCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 8, 2, 1, 18),
    _W2kStatusDirSizeCrit_Type()
)
w2kStatusDirSizeCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusDirSizeCrit.setStatus("mandatory")


class _W2kStatusDirSizeMonitor_Type(Integer32):
    """Custom type w2kStatusDirSizeMonitor based on Integer32"""
    defaultValue = 0

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
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_W2kStatusDirSizeMonitor_Type.__name__ = "Integer32"
_W2kStatusDirSizeMonitor_Object = MibTableColumn
w2kStatusDirSizeMonitor = _W2kStatusDirSizeMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 8, 2, 1, 19),
    _W2kStatusDirSizeMonitor_Type()
)
w2kStatusDirSizeMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusDirSizeMonitor.setStatus("mandatory")


class _W2kStatusDirSizeStatus_Type(Integer32):
    """Custom type w2kStatusDirSizeStatus based on Integer32"""
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
        *(("critical", 4),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_W2kStatusDirSizeStatus_Type.__name__ = "Integer32"
_W2kStatusDirSizeStatus_Object = MibTableColumn
w2kStatusDirSizeStatus = _W2kStatusDirSizeStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 8, 2, 1, 20),
    _W2kStatusDirSizeStatus_Type()
)
w2kStatusDirSizeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusDirSizeStatus.setStatus("mandatory")
_W2kStatusDirSizeDValue_Type = Integer32
_W2kStatusDirSizeDValue_Object = MibTableColumn
w2kStatusDirSizeDValue = _W2kStatusDirSizeDValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 8, 2, 1, 21),
    _W2kStatusDirSizeDValue_Type()
)
w2kStatusDirSizeDValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusDirSizeDValue.setStatus("mandatory")
_W2kStatusDirSizeDWarnValue_Type = DisplayString
_W2kStatusDirSizeDWarnValue_Object = MibTableColumn
w2kStatusDirSizeDWarnValue = _W2kStatusDirSizeDWarnValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 8, 2, 1, 22),
    _W2kStatusDirSizeDWarnValue_Type()
)
w2kStatusDirSizeDWarnValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusDirSizeDWarnValue.setStatus("mandatory")
_W2kStatusDirSizeDCritValue_Type = DisplayString
_W2kStatusDirSizeDCritValue_Object = MibTableColumn
w2kStatusDirSizeDCritValue = _W2kStatusDirSizeDCritValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 8, 2, 1, 23),
    _W2kStatusDirSizeDCritValue_Type()
)
w2kStatusDirSizeDCritValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusDirSizeDCritValue.setStatus("mandatory")
_W2kStatusDirSizeDWarn_Type = DisplayString
_W2kStatusDirSizeDWarn_Object = MibTableColumn
w2kStatusDirSizeDWarn = _W2kStatusDirSizeDWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 8, 2, 1, 24),
    _W2kStatusDirSizeDWarn_Type()
)
w2kStatusDirSizeDWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusDirSizeDWarn.setStatus("mandatory")
_W2kStatusDirSizeDCrit_Type = DisplayString
_W2kStatusDirSizeDCrit_Object = MibTableColumn
w2kStatusDirSizeDCrit = _W2kStatusDirSizeDCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 8, 2, 1, 25),
    _W2kStatusDirSizeDCrit_Type()
)
w2kStatusDirSizeDCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusDirSizeDCrit.setStatus("mandatory")


class _W2kStatusDirSizeDMonitor_Type(Integer32):
    """Custom type w2kStatusDirSizeDMonitor based on Integer32"""
    defaultValue = 0

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
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_W2kStatusDirSizeDMonitor_Type.__name__ = "Integer32"
_W2kStatusDirSizeDMonitor_Object = MibTableColumn
w2kStatusDirSizeDMonitor = _W2kStatusDirSizeDMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 8, 2, 1, 26),
    _W2kStatusDirSizeDMonitor_Type()
)
w2kStatusDirSizeDMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusDirSizeDMonitor.setStatus("mandatory")


class _W2kStatusDirSizeDStatus_Type(Integer32):
    """Custom type w2kStatusDirSizeDStatus based on Integer32"""
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
        *(("critical", 4),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_W2kStatusDirSizeDStatus_Type.__name__ = "Integer32"
_W2kStatusDirSizeDStatus_Object = MibTableColumn
w2kStatusDirSizeDStatus = _W2kStatusDirSizeDStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 8, 2, 1, 27),
    _W2kStatusDirSizeDStatus_Type()
)
w2kStatusDirSizeDStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusDirSizeDStatus.setStatus("mandatory")
_W2kStatusDirEntryValue_Type = Integer32
_W2kStatusDirEntryValue_Object = MibTableColumn
w2kStatusDirEntryValue = _W2kStatusDirEntryValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 8, 2, 1, 28),
    _W2kStatusDirEntryValue_Type()
)
w2kStatusDirEntryValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusDirEntryValue.setStatus("mandatory")
_W2kStatusDirEntryWarn_Type = Integer32
_W2kStatusDirEntryWarn_Object = MibTableColumn
w2kStatusDirEntryWarn = _W2kStatusDirEntryWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 8, 2, 1, 29),
    _W2kStatusDirEntryWarn_Type()
)
w2kStatusDirEntryWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusDirEntryWarn.setStatus("mandatory")
_W2kStatusDirEntryCrit_Type = Integer32
_W2kStatusDirEntryCrit_Object = MibTableColumn
w2kStatusDirEntryCrit = _W2kStatusDirEntryCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 8, 2, 1, 30),
    _W2kStatusDirEntryCrit_Type()
)
w2kStatusDirEntryCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusDirEntryCrit.setStatus("mandatory")


class _W2kStatusDirEntryMonitor_Type(Integer32):
    """Custom type w2kStatusDirEntryMonitor based on Integer32"""
    defaultValue = 0

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
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_W2kStatusDirEntryMonitor_Type.__name__ = "Integer32"
_W2kStatusDirEntryMonitor_Object = MibTableColumn
w2kStatusDirEntryMonitor = _W2kStatusDirEntryMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 8, 2, 1, 31),
    _W2kStatusDirEntryMonitor_Type()
)
w2kStatusDirEntryMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusDirEntryMonitor.setStatus("mandatory")


class _W2kStatusDirEntryStatus_Type(Integer32):
    """Custom type w2kStatusDirEntryStatus based on Integer32"""
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
        *(("critical", 4),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_W2kStatusDirEntryStatus_Type.__name__ = "Integer32"
_W2kStatusDirEntryStatus_Object = MibTableColumn
w2kStatusDirEntryStatus = _W2kStatusDirEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 8, 2, 1, 32),
    _W2kStatusDirEntryStatus_Type()
)
w2kStatusDirEntryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusDirEntryStatus.setStatus("mandatory")
_W2kStatusDirCallBackRef_Type = DisplayString
_W2kStatusDirCallBackRef_Object = MibTableColumn
w2kStatusDirCallBackRef = _W2kStatusDirCallBackRef_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 8, 2, 1, 33),
    _W2kStatusDirCallBackRef_Type()
)
w2kStatusDirCallBackRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusDirCallBackRef.setStatus("mandatory")


class _W2kStatusDirButton_Type(Integer32):
    """Custom type w2kStatusDirButton based on Integer32"""
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
          ("remove", 2),
          ("reset-time", 3))
    )


_W2kStatusDirButton_Type.__name__ = "Integer32"
_W2kStatusDirButton_Object = MibTableColumn
w2kStatusDirButton = _W2kStatusDirButton_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 8, 2, 1, 34),
    _W2kStatusDirButton_Type()
)
w2kStatusDirButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusDirButton.setStatus("mandatory")
_W2kStatusFileGroup_ObjectIdentity = ObjectIdentity
w2kStatusFileGroup = _W2kStatusFileGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 9)
)
_W2kStatusFileCount_Type = Integer32
_W2kStatusFileCount_Object = MibScalar
w2kStatusFileCount = _W2kStatusFileCount_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 9, 1),
    _W2kStatusFileCount_Type()
)
w2kStatusFileCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusFileCount.setStatus("mandatory")
_W2kStatusFileTable_Object = MibTable
w2kStatusFileTable = _W2kStatusFileTable_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 9, 2)
)
if mibBuilder.loadTexts:
    w2kStatusFileTable.setStatus("mandatory")
_W2kStatusFileEntry_Object = MibTableRow
w2kStatusFileEntry = _W2kStatusFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 9, 2, 1)
)
w2kStatusFileEntry.setIndexNames(
    (0, "CA-W2KOS-MIB", "w2kStatusFileName"),
)
if mibBuilder.loadTexts:
    w2kStatusFileEntry.setStatus("mandatory")
_W2kStatusFileName_Type = DisplayString
_W2kStatusFileName_Object = MibTableColumn
w2kStatusFileName = _W2kStatusFileName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 9, 2, 1, 1),
    _W2kStatusFileName_Type()
)
w2kStatusFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusFileName.setStatus("mandatory")
_W2kStatusFileDescription_Type = DisplayString
_W2kStatusFileDescription_Object = MibTableColumn
w2kStatusFileDescription = _W2kStatusFileDescription_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 9, 2, 1, 2),
    _W2kStatusFileDescription_Type()
)
w2kStatusFileDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusFileDescription.setStatus("mandatory")
_W2kStatusFileAggLagValue_Type = Integer32
_W2kStatusFileAggLagValue_Object = MibTableColumn
w2kStatusFileAggLagValue = _W2kStatusFileAggLagValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 9, 2, 1, 3),
    _W2kStatusFileAggLagValue_Type()
)
w2kStatusFileAggLagValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusFileAggLagValue.setStatus("mandatory")
_W2kStatusFileAggLag_Type = Integer32
_W2kStatusFileAggLag_Object = MibTableColumn
w2kStatusFileAggLag = _W2kStatusFileAggLag_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 9, 2, 1, 4),
    _W2kStatusFileAggLag_Type()
)
w2kStatusFileAggLag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusFileAggLag.setStatus("mandatory")


class _W2kStatusFileAggStatus_Type(Integer32):
    """Custom type w2kStatusFileAggStatus based on Integer32"""
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
        *(("critical", 4),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_W2kStatusFileAggStatus_Type.__name__ = "Integer32"
_W2kStatusFileAggStatus_Object = MibTableColumn
w2kStatusFileAggStatus = _W2kStatusFileAggStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 9, 2, 1, 5),
    _W2kStatusFileAggStatus_Type()
)
w2kStatusFileAggStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusFileAggStatus.setStatus("mandatory")


class _W2kStatusFileExist_Type(Integer32):
    """Custom type w2kStatusFileExist based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("should-exist", 1),
          ("should-not-exist", 2))
    )


_W2kStatusFileExist_Type.__name__ = "Integer32"
_W2kStatusFileExist_Object = MibTableColumn
w2kStatusFileExist = _W2kStatusFileExist_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 9, 2, 1, 6),
    _W2kStatusFileExist_Type()
)
w2kStatusFileExist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusFileExist.setStatus("mandatory")


class _W2kStatusFileExistMonitor_Type(Integer32):
    """Custom type w2kStatusFileExistMonitor based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("do-not-monitor", 1),
          ("down-critical", 3),
          ("down-warning", 2))
    )


_W2kStatusFileExistMonitor_Type.__name__ = "Integer32"
_W2kStatusFileExistMonitor_Object = MibTableColumn
w2kStatusFileExistMonitor = _W2kStatusFileExistMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 9, 2, 1, 7),
    _W2kStatusFileExistMonitor_Type()
)
w2kStatusFileExistMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusFileExistMonitor.setStatus("mandatory")


class _W2kStatusFileExistStatus_Type(Integer32):
    """Custom type w2kStatusFileExistStatus based on Integer32"""
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
        *(("down-critical", 4),
          ("down-warning", 3),
          ("unknown", 1),
          ("up", 2))
    )


_W2kStatusFileExistStatus_Type.__name__ = "Integer32"
_W2kStatusFileExistStatus_Object = MibTableColumn
w2kStatusFileExistStatus = _W2kStatusFileExistStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 9, 2, 1, 8),
    _W2kStatusFileExistStatus_Type()
)
w2kStatusFileExistStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusFileExistStatus.setStatus("mandatory")
_W2kStatusFileTimeValue_Type = DisplayString
_W2kStatusFileTimeValue_Object = MibTableColumn
w2kStatusFileTimeValue = _W2kStatusFileTimeValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 9, 2, 1, 9),
    _W2kStatusFileTimeValue_Type()
)
w2kStatusFileTimeValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusFileTimeValue.setStatus("mandatory")
_W2kStatusFileTimeRef_Type = DisplayString
_W2kStatusFileTimeRef_Object = MibTableColumn
w2kStatusFileTimeRef = _W2kStatusFileTimeRef_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 9, 2, 1, 10),
    _W2kStatusFileTimeRef_Type()
)
w2kStatusFileTimeRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusFileTimeRef.setStatus("mandatory")


class _W2kStatusFileTimeMonitor_Type(Integer32):
    """Custom type w2kStatusFileTimeMonitor based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("do-not-monitor", 1),
          ("down-critical", 3),
          ("down-warning", 2))
    )


_W2kStatusFileTimeMonitor_Type.__name__ = "Integer32"
_W2kStatusFileTimeMonitor_Object = MibTableColumn
w2kStatusFileTimeMonitor = _W2kStatusFileTimeMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 9, 2, 1, 11),
    _W2kStatusFileTimeMonitor_Type()
)
w2kStatusFileTimeMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusFileTimeMonitor.setStatus("mandatory")


class _W2kStatusFileTimeStatus_Type(Integer32):
    """Custom type w2kStatusFileTimeStatus based on Integer32"""
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
        *(("down-critical", 4),
          ("down-warning", 3),
          ("unknown", 1),
          ("up", 2))
    )


_W2kStatusFileTimeStatus_Type.__name__ = "Integer32"
_W2kStatusFileTimeStatus_Object = MibTableColumn
w2kStatusFileTimeStatus = _W2kStatusFileTimeStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 9, 2, 1, 12),
    _W2kStatusFileTimeStatus_Type()
)
w2kStatusFileTimeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusFileTimeStatus.setStatus("mandatory")
_W2kStatusFileSizeRef_Type = Integer32
_W2kStatusFileSizeRef_Object = MibTableColumn
w2kStatusFileSizeRef = _W2kStatusFileSizeRef_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 9, 2, 1, 13),
    _W2kStatusFileSizeRef_Type()
)
w2kStatusFileSizeRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusFileSizeRef.setStatus("mandatory")
_W2kStatusFileSizeValue_Type = Integer32
_W2kStatusFileSizeValue_Object = MibTableColumn
w2kStatusFileSizeValue = _W2kStatusFileSizeValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 9, 2, 1, 14),
    _W2kStatusFileSizeValue_Type()
)
w2kStatusFileSizeValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusFileSizeValue.setStatus("mandatory")
_W2kStatusFileSizeWarnValue_Type = Integer32
_W2kStatusFileSizeWarnValue_Object = MibTableColumn
w2kStatusFileSizeWarnValue = _W2kStatusFileSizeWarnValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 9, 2, 1, 15),
    _W2kStatusFileSizeWarnValue_Type()
)
w2kStatusFileSizeWarnValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusFileSizeWarnValue.setStatus("mandatory")
_W2kStatusFileSizeCritValue_Type = Integer32
_W2kStatusFileSizeCritValue_Object = MibTableColumn
w2kStatusFileSizeCritValue = _W2kStatusFileSizeCritValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 9, 2, 1, 16),
    _W2kStatusFileSizeCritValue_Type()
)
w2kStatusFileSizeCritValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusFileSizeCritValue.setStatus("mandatory")
_W2kStatusFileSizeWarn_Type = DisplayString
_W2kStatusFileSizeWarn_Object = MibTableColumn
w2kStatusFileSizeWarn = _W2kStatusFileSizeWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 9, 2, 1, 17),
    _W2kStatusFileSizeWarn_Type()
)
w2kStatusFileSizeWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusFileSizeWarn.setStatus("mandatory")
_W2kStatusFileSizeCrit_Type = DisplayString
_W2kStatusFileSizeCrit_Object = MibTableColumn
w2kStatusFileSizeCrit = _W2kStatusFileSizeCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 9, 2, 1, 18),
    _W2kStatusFileSizeCrit_Type()
)
w2kStatusFileSizeCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusFileSizeCrit.setStatus("mandatory")


class _W2kStatusFileSizeMonitor_Type(Integer32):
    """Custom type w2kStatusFileSizeMonitor based on Integer32"""
    defaultValue = 0

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
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_W2kStatusFileSizeMonitor_Type.__name__ = "Integer32"
_W2kStatusFileSizeMonitor_Object = MibTableColumn
w2kStatusFileSizeMonitor = _W2kStatusFileSizeMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 9, 2, 1, 19),
    _W2kStatusFileSizeMonitor_Type()
)
w2kStatusFileSizeMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusFileSizeMonitor.setStatus("mandatory")


class _W2kStatusFileSizeStatus_Type(Integer32):
    """Custom type w2kStatusFileSizeStatus based on Integer32"""
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
        *(("critical", 4),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_W2kStatusFileSizeStatus_Type.__name__ = "Integer32"
_W2kStatusFileSizeStatus_Object = MibTableColumn
w2kStatusFileSizeStatus = _W2kStatusFileSizeStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 9, 2, 1, 20),
    _W2kStatusFileSizeStatus_Type()
)
w2kStatusFileSizeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusFileSizeStatus.setStatus("mandatory")
_W2kStatusFileSizeDValue_Type = Integer32
_W2kStatusFileSizeDValue_Object = MibTableColumn
w2kStatusFileSizeDValue = _W2kStatusFileSizeDValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 9, 2, 1, 21),
    _W2kStatusFileSizeDValue_Type()
)
w2kStatusFileSizeDValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusFileSizeDValue.setStatus("mandatory")
_W2kStatusFileSizeDWarnValue_Type = DisplayString
_W2kStatusFileSizeDWarnValue_Object = MibTableColumn
w2kStatusFileSizeDWarnValue = _W2kStatusFileSizeDWarnValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 9, 2, 1, 22),
    _W2kStatusFileSizeDWarnValue_Type()
)
w2kStatusFileSizeDWarnValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusFileSizeDWarnValue.setStatus("mandatory")
_W2kStatusFileSizeDCritValue_Type = DisplayString
_W2kStatusFileSizeDCritValue_Object = MibTableColumn
w2kStatusFileSizeDCritValue = _W2kStatusFileSizeDCritValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 9, 2, 1, 23),
    _W2kStatusFileSizeDCritValue_Type()
)
w2kStatusFileSizeDCritValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusFileSizeDCritValue.setStatus("mandatory")
_W2kStatusFileSizeDWarn_Type = DisplayString
_W2kStatusFileSizeDWarn_Object = MibTableColumn
w2kStatusFileSizeDWarn = _W2kStatusFileSizeDWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 9, 2, 1, 24),
    _W2kStatusFileSizeDWarn_Type()
)
w2kStatusFileSizeDWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusFileSizeDWarn.setStatus("mandatory")
_W2kStatusFileSizeDCrit_Type = DisplayString
_W2kStatusFileSizeDCrit_Object = MibTableColumn
w2kStatusFileSizeDCrit = _W2kStatusFileSizeDCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 9, 2, 1, 25),
    _W2kStatusFileSizeDCrit_Type()
)
w2kStatusFileSizeDCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusFileSizeDCrit.setStatus("mandatory")


class _W2kStatusFileSizeDMonitor_Type(Integer32):
    """Custom type w2kStatusFileSizeDMonitor based on Integer32"""
    defaultValue = 0

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
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_W2kStatusFileSizeDMonitor_Type.__name__ = "Integer32"
_W2kStatusFileSizeDMonitor_Object = MibTableColumn
w2kStatusFileSizeDMonitor = _W2kStatusFileSizeDMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 9, 2, 1, 26),
    _W2kStatusFileSizeDMonitor_Type()
)
w2kStatusFileSizeDMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusFileSizeDMonitor.setStatus("mandatory")


class _W2kStatusFileSizeDStatus_Type(Integer32):
    """Custom type w2kStatusFileSizeDStatus based on Integer32"""
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
        *(("critical", 4),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_W2kStatusFileSizeDStatus_Type.__name__ = "Integer32"
_W2kStatusFileSizeDStatus_Object = MibTableColumn
w2kStatusFileSizeDStatus = _W2kStatusFileSizeDStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 9, 2, 1, 27),
    _W2kStatusFileSizeDStatus_Type()
)
w2kStatusFileSizeDStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusFileSizeDStatus.setStatus("mandatory")
_W2kStatusFileCallBackRef_Type = DisplayString
_W2kStatusFileCallBackRef_Object = MibTableColumn
w2kStatusFileCallBackRef = _W2kStatusFileCallBackRef_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 9, 2, 1, 28),
    _W2kStatusFileCallBackRef_Type()
)
w2kStatusFileCallBackRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusFileCallBackRef.setStatus("mandatory")


class _W2kStatusFileButton_Type(Integer32):
    """Custom type w2kStatusFileButton based on Integer32"""
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
          ("remove", 2),
          ("reset-time", 3))
    )


_W2kStatusFileButton_Type.__name__ = "Integer32"
_W2kStatusFileButton_Object = MibTableColumn
w2kStatusFileButton = _W2kStatusFileButton_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 9, 2, 1, 29),
    _W2kStatusFileButton_Type()
)
w2kStatusFileButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusFileButton.setStatus("mandatory")
_W2kStatusProcGroup_ObjectIdentity = ObjectIdentity
w2kStatusProcGroup = _W2kStatusProcGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 10)
)
_W2kStatusProcCount_Type = Integer32
_W2kStatusProcCount_Object = MibScalar
w2kStatusProcCount = _W2kStatusProcCount_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 10, 1),
    _W2kStatusProcCount_Type()
)
w2kStatusProcCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusProcCount.setStatus("mandatory")
_W2kStatusProcTable_Object = MibTable
w2kStatusProcTable = _W2kStatusProcTable_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 10, 2)
)
if mibBuilder.loadTexts:
    w2kStatusProcTable.setStatus("mandatory")
_W2kStatusProcEntry_Object = MibTableRow
w2kStatusProcEntry = _W2kStatusProcEntry_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 10, 2, 1)
)
w2kStatusProcEntry.setIndexNames(
    (0, "CA-W2KOS-MIB", "w2kStatusProcProcName"),
    (0, "CA-W2KOS-MIB", "w2kStatusProcPathName"),
    (0, "CA-W2KOS-MIB", "w2kStatusProcUserName"),
)
if mibBuilder.loadTexts:
    w2kStatusProcEntry.setStatus("mandatory")
_W2kStatusProcProcName_Type = DisplayString
_W2kStatusProcProcName_Object = MibTableColumn
w2kStatusProcProcName = _W2kStatusProcProcName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 10, 2, 1, 1),
    _W2kStatusProcProcName_Type()
)
w2kStatusProcProcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusProcProcName.setStatus("mandatory")
_W2kStatusProcPathName_Type = DisplayString
_W2kStatusProcPathName_Object = MibTableColumn
w2kStatusProcPathName = _W2kStatusProcPathName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 10, 2, 1, 2),
    _W2kStatusProcPathName_Type()
)
w2kStatusProcPathName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusProcPathName.setStatus("mandatory")
_W2kStatusProcUserName_Type = DisplayString
_W2kStatusProcUserName_Object = MibTableColumn
w2kStatusProcUserName = _W2kStatusProcUserName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 10, 2, 1, 3),
    _W2kStatusProcUserName_Type()
)
w2kStatusProcUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusProcUserName.setStatus("mandatory")
_W2kStatusProcDescription_Type = DisplayString
_W2kStatusProcDescription_Object = MibTableColumn
w2kStatusProcDescription = _W2kStatusProcDescription_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 10, 2, 1, 4),
    _W2kStatusProcDescription_Type()
)
w2kStatusProcDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusProcDescription.setStatus("mandatory")
_W2kStatusProcIds_Type = DisplayString
_W2kStatusProcIds_Object = MibTableColumn
w2kStatusProcIds = _W2kStatusProcIds_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 10, 2, 1, 5),
    _W2kStatusProcIds_Type()
)
w2kStatusProcIds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusProcIds.setStatus("mandatory")
_W2kStatusProcAggLagValue_Type = Integer32
_W2kStatusProcAggLagValue_Object = MibTableColumn
w2kStatusProcAggLagValue = _W2kStatusProcAggLagValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 10, 2, 1, 6),
    _W2kStatusProcAggLagValue_Type()
)
w2kStatusProcAggLagValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusProcAggLagValue.setStatus("mandatory")
_W2kStatusProcAggLag_Type = Integer32
_W2kStatusProcAggLag_Object = MibTableColumn
w2kStatusProcAggLag = _W2kStatusProcAggLag_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 10, 2, 1, 7),
    _W2kStatusProcAggLag_Type()
)
w2kStatusProcAggLag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusProcAggLag.setStatus("mandatory")


class _W2kStatusProcAggStatus_Type(Integer32):
    """Custom type w2kStatusProcAggStatus based on Integer32"""
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
        *(("critical", 4),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_W2kStatusProcAggStatus_Type.__name__ = "Integer32"
_W2kStatusProcAggStatus_Object = MibTableColumn
w2kStatusProcAggStatus = _W2kStatusProcAggStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 10, 2, 1, 8),
    _W2kStatusProcAggStatus_Type()
)
w2kStatusProcAggStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusProcAggStatus.setStatus("mandatory")
_W2kStatusProcInstValue_Type = Integer32
_W2kStatusProcInstValue_Object = MibTableColumn
w2kStatusProcInstValue = _W2kStatusProcInstValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 10, 2, 1, 9),
    _W2kStatusProcInstValue_Type()
)
w2kStatusProcInstValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusProcInstValue.setStatus("mandatory")


class _W2kStatusProcInstMin_Type(Integer32):
    """Custom type w2kStatusProcInstMin based on Integer32"""
    defaultValue = -2


_W2kStatusProcInstMin_Object = MibTableColumn
w2kStatusProcInstMin = _W2kStatusProcInstMin_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 10, 2, 1, 10),
    _W2kStatusProcInstMin_Type()
)
w2kStatusProcInstMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusProcInstMin.setStatus("mandatory")


class _W2kStatusProcInstMax_Type(Integer32):
    """Custom type w2kStatusProcInstMax based on Integer32"""
    defaultValue = -2


_W2kStatusProcInstMax_Object = MibTableColumn
w2kStatusProcInstMax = _W2kStatusProcInstMax_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 10, 2, 1, 11),
    _W2kStatusProcInstMax_Type()
)
w2kStatusProcInstMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusProcInstMax.setStatus("mandatory")


class _W2kStatusProcInstMonitor_Type(Integer32):
    """Custom type w2kStatusProcInstMonitor based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("do-not-monitor", 1),
          ("down-critical", 3),
          ("down-warning", 2))
    )


_W2kStatusProcInstMonitor_Type.__name__ = "Integer32"
_W2kStatusProcInstMonitor_Object = MibTableColumn
w2kStatusProcInstMonitor = _W2kStatusProcInstMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 10, 2, 1, 12),
    _W2kStatusProcInstMonitor_Type()
)
w2kStatusProcInstMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusProcInstMonitor.setStatus("mandatory")


class _W2kStatusProcInstStatus_Type(Integer32):
    """Custom type w2kStatusProcInstStatus based on Integer32"""
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
        *(("down-critical", 4),
          ("down-warning", 3),
          ("unknown", 1),
          ("up", 2))
    )


_W2kStatusProcInstStatus_Type.__name__ = "Integer32"
_W2kStatusProcInstStatus_Object = MibTableColumn
w2kStatusProcInstStatus = _W2kStatusProcInstStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 10, 2, 1, 13),
    _W2kStatusProcInstStatus_Type()
)
w2kStatusProcInstStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusProcInstStatus.setStatus("mandatory")
_W2kStatusProcChildMinValue_Type = Integer32
_W2kStatusProcChildMinValue_Object = MibTableColumn
w2kStatusProcChildMinValue = _W2kStatusProcChildMinValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 10, 2, 1, 14),
    _W2kStatusProcChildMinValue_Type()
)
w2kStatusProcChildMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusProcChildMinValue.setStatus("mandatory")
_W2kStatusProcChildMaxValue_Type = Integer32
_W2kStatusProcChildMaxValue_Object = MibTableColumn
w2kStatusProcChildMaxValue = _W2kStatusProcChildMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 10, 2, 1, 15),
    _W2kStatusProcChildMaxValue_Type()
)
w2kStatusProcChildMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusProcChildMaxValue.setStatus("mandatory")


class _W2kStatusProcChildMin_Type(Integer32):
    """Custom type w2kStatusProcChildMin based on Integer32"""
    defaultValue = -2


_W2kStatusProcChildMin_Object = MibTableColumn
w2kStatusProcChildMin = _W2kStatusProcChildMin_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 10, 2, 1, 16),
    _W2kStatusProcChildMin_Type()
)
w2kStatusProcChildMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusProcChildMin.setStatus("mandatory")


class _W2kStatusProcChildMax_Type(Integer32):
    """Custom type w2kStatusProcChildMax based on Integer32"""
    defaultValue = -2


_W2kStatusProcChildMax_Object = MibTableColumn
w2kStatusProcChildMax = _W2kStatusProcChildMax_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 10, 2, 1, 17),
    _W2kStatusProcChildMax_Type()
)
w2kStatusProcChildMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusProcChildMax.setStatus("mandatory")


class _W2kStatusProcChildMonitor_Type(Integer32):
    """Custom type w2kStatusProcChildMonitor based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("do-not-monitor", 1),
          ("down-critical", 3),
          ("down-warning", 2))
    )


_W2kStatusProcChildMonitor_Type.__name__ = "Integer32"
_W2kStatusProcChildMonitor_Object = MibTableColumn
w2kStatusProcChildMonitor = _W2kStatusProcChildMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 10, 2, 1, 18),
    _W2kStatusProcChildMonitor_Type()
)
w2kStatusProcChildMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusProcChildMonitor.setStatus("mandatory")


class _W2kStatusProcChildStatus_Type(Integer32):
    """Custom type w2kStatusProcChildStatus based on Integer32"""
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
        *(("down-critical", 4),
          ("down-warning", 3),
          ("unknown", 1),
          ("up", 2))
    )


_W2kStatusProcChildStatus_Type.__name__ = "Integer32"
_W2kStatusProcChildStatus_Object = MibTableColumn
w2kStatusProcChildStatus = _W2kStatusProcChildStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 10, 2, 1, 19),
    _W2kStatusProcChildStatus_Type()
)
w2kStatusProcChildStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusProcChildStatus.setStatus("mandatory")
_W2kStatusProcThreadMinValue_Type = Integer32
_W2kStatusProcThreadMinValue_Object = MibTableColumn
w2kStatusProcThreadMinValue = _W2kStatusProcThreadMinValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 10, 2, 1, 20),
    _W2kStatusProcThreadMinValue_Type()
)
w2kStatusProcThreadMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusProcThreadMinValue.setStatus("mandatory")
_W2kStatusProcThreadMaxValue_Type = Integer32
_W2kStatusProcThreadMaxValue_Object = MibTableColumn
w2kStatusProcThreadMaxValue = _W2kStatusProcThreadMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 10, 2, 1, 21),
    _W2kStatusProcThreadMaxValue_Type()
)
w2kStatusProcThreadMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusProcThreadMaxValue.setStatus("mandatory")


class _W2kStatusProcThreadMin_Type(Integer32):
    """Custom type w2kStatusProcThreadMin based on Integer32"""
    defaultValue = -2


_W2kStatusProcThreadMin_Object = MibTableColumn
w2kStatusProcThreadMin = _W2kStatusProcThreadMin_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 10, 2, 1, 22),
    _W2kStatusProcThreadMin_Type()
)
w2kStatusProcThreadMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusProcThreadMin.setStatus("mandatory")


class _W2kStatusProcThreadMax_Type(Integer32):
    """Custom type w2kStatusProcThreadMax based on Integer32"""
    defaultValue = -2


_W2kStatusProcThreadMax_Object = MibTableColumn
w2kStatusProcThreadMax = _W2kStatusProcThreadMax_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 10, 2, 1, 23),
    _W2kStatusProcThreadMax_Type()
)
w2kStatusProcThreadMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusProcThreadMax.setStatus("mandatory")


class _W2kStatusProcThreadMonitor_Type(Integer32):
    """Custom type w2kStatusProcThreadMonitor based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("do-not-monitor", 1),
          ("down-critical", 3),
          ("down-warning", 2))
    )


_W2kStatusProcThreadMonitor_Type.__name__ = "Integer32"
_W2kStatusProcThreadMonitor_Object = MibTableColumn
w2kStatusProcThreadMonitor = _W2kStatusProcThreadMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 10, 2, 1, 24),
    _W2kStatusProcThreadMonitor_Type()
)
w2kStatusProcThreadMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusProcThreadMonitor.setStatus("mandatory")


class _W2kStatusProcThreadStatus_Type(Integer32):
    """Custom type w2kStatusProcThreadStatus based on Integer32"""
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
        *(("down-critical", 4),
          ("down-warning", 3),
          ("unknown", 1),
          ("up", 2))
    )


_W2kStatusProcThreadStatus_Type.__name__ = "Integer32"
_W2kStatusProcThreadStatus_Object = MibTableColumn
w2kStatusProcThreadStatus = _W2kStatusProcThreadStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 10, 2, 1, 25),
    _W2kStatusProcThreadStatus_Type()
)
w2kStatusProcThreadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusProcThreadStatus.setStatus("mandatory")
_W2kStatusProcMemoryValue_Type = Integer32
_W2kStatusProcMemoryValue_Object = MibTableColumn
w2kStatusProcMemoryValue = _W2kStatusProcMemoryValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 10, 2, 1, 26),
    _W2kStatusProcMemoryValue_Type()
)
w2kStatusProcMemoryValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusProcMemoryValue.setStatus("mandatory")
_W2kStatusProcMemoryWarn_Type = Integer32
_W2kStatusProcMemoryWarn_Object = MibTableColumn
w2kStatusProcMemoryWarn = _W2kStatusProcMemoryWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 10, 2, 1, 27),
    _W2kStatusProcMemoryWarn_Type()
)
w2kStatusProcMemoryWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusProcMemoryWarn.setStatus("mandatory")
_W2kStatusProcMemoryCrit_Type = Integer32
_W2kStatusProcMemoryCrit_Object = MibTableColumn
w2kStatusProcMemoryCrit = _W2kStatusProcMemoryCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 10, 2, 1, 28),
    _W2kStatusProcMemoryCrit_Type()
)
w2kStatusProcMemoryCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusProcMemoryCrit.setStatus("mandatory")


class _W2kStatusProcMemoryMonitor_Type(Integer32):
    """Custom type w2kStatusProcMemoryMonitor based on Integer32"""
    defaultValue = 0

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
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_W2kStatusProcMemoryMonitor_Type.__name__ = "Integer32"
_W2kStatusProcMemoryMonitor_Object = MibTableColumn
w2kStatusProcMemoryMonitor = _W2kStatusProcMemoryMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 10, 2, 1, 29),
    _W2kStatusProcMemoryMonitor_Type()
)
w2kStatusProcMemoryMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusProcMemoryMonitor.setStatus("mandatory")


class _W2kStatusProcMemoryStatus_Type(Integer32):
    """Custom type w2kStatusProcMemoryStatus based on Integer32"""
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
        *(("critical", 4),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_W2kStatusProcMemoryStatus_Type.__name__ = "Integer32"
_W2kStatusProcMemoryStatus_Object = MibTableColumn
w2kStatusProcMemoryStatus = _W2kStatusProcMemoryStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 10, 2, 1, 30),
    _W2kStatusProcMemoryStatus_Type()
)
w2kStatusProcMemoryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusProcMemoryStatus.setStatus("mandatory")
_W2kStatusProcCpuValue_Type = Integer32
_W2kStatusProcCpuValue_Object = MibTableColumn
w2kStatusProcCpuValue = _W2kStatusProcCpuValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 10, 2, 1, 31),
    _W2kStatusProcCpuValue_Type()
)
w2kStatusProcCpuValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusProcCpuValue.setStatus("mandatory")
_W2kStatusProcCpuWarn_Type = Integer32
_W2kStatusProcCpuWarn_Object = MibTableColumn
w2kStatusProcCpuWarn = _W2kStatusProcCpuWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 10, 2, 1, 32),
    _W2kStatusProcCpuWarn_Type()
)
w2kStatusProcCpuWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusProcCpuWarn.setStatus("mandatory")
_W2kStatusProcCpuCrit_Type = Integer32
_W2kStatusProcCpuCrit_Object = MibTableColumn
w2kStatusProcCpuCrit = _W2kStatusProcCpuCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 10, 2, 1, 33),
    _W2kStatusProcCpuCrit_Type()
)
w2kStatusProcCpuCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusProcCpuCrit.setStatus("mandatory")


class _W2kStatusProcCpuMonitor_Type(Integer32):
    """Custom type w2kStatusProcCpuMonitor based on Integer32"""
    defaultValue = 0

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
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_W2kStatusProcCpuMonitor_Type.__name__ = "Integer32"
_W2kStatusProcCpuMonitor_Object = MibTableColumn
w2kStatusProcCpuMonitor = _W2kStatusProcCpuMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 10, 2, 1, 34),
    _W2kStatusProcCpuMonitor_Type()
)
w2kStatusProcCpuMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusProcCpuMonitor.setStatus("mandatory")


class _W2kStatusProcCpuStatus_Type(Integer32):
    """Custom type w2kStatusProcCpuStatus based on Integer32"""
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
        *(("critical", 4),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_W2kStatusProcCpuStatus_Type.__name__ = "Integer32"
_W2kStatusProcCpuStatus_Object = MibTableColumn
w2kStatusProcCpuStatus = _W2kStatusProcCpuStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 10, 2, 1, 35),
    _W2kStatusProcCpuStatus_Type()
)
w2kStatusProcCpuStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusProcCpuStatus.setStatus("mandatory")
_W2kStatusProcCallBackRef_Type = DisplayString
_W2kStatusProcCallBackRef_Object = MibTableColumn
w2kStatusProcCallBackRef = _W2kStatusProcCallBackRef_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 10, 2, 1, 36),
    _W2kStatusProcCallBackRef_Type()
)
w2kStatusProcCallBackRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusProcCallBackRef.setStatus("mandatory")


class _W2kStatusProcButton_Type(Integer32):
    """Custom type w2kStatusProcButton based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("remove", 2))
    )


_W2kStatusProcButton_Type.__name__ = "Integer32"
_W2kStatusProcButton_Object = MibTableColumn
w2kStatusProcButton = _W2kStatusProcButton_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 10, 2, 1, 37),
    _W2kStatusProcButton_Type()
)
w2kStatusProcButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusProcButton.setStatus("mandatory")
_W2kStatusSrvcGroup_ObjectIdentity = ObjectIdentity
w2kStatusSrvcGroup = _W2kStatusSrvcGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 11)
)
_W2kStatusSrvcCount_Type = Integer32
_W2kStatusSrvcCount_Object = MibScalar
w2kStatusSrvcCount = _W2kStatusSrvcCount_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 11, 1),
    _W2kStatusSrvcCount_Type()
)
w2kStatusSrvcCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusSrvcCount.setStatus("mandatory")
_W2kStatusSrvcTable_Object = MibTable
w2kStatusSrvcTable = _W2kStatusSrvcTable_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 11, 2)
)
if mibBuilder.loadTexts:
    w2kStatusSrvcTable.setStatus("mandatory")
_W2kStatusSrvcEntry_Object = MibTableRow
w2kStatusSrvcEntry = _W2kStatusSrvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 11, 2, 1)
)
w2kStatusSrvcEntry.setIndexNames(
    (0, "CA-W2KOS-MIB", "w2kStatusSrvcName"),
)
if mibBuilder.loadTexts:
    w2kStatusSrvcEntry.setStatus("mandatory")
_W2kStatusSrvcName_Type = DisplayString
_W2kStatusSrvcName_Object = MibTableColumn
w2kStatusSrvcName = _W2kStatusSrvcName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 11, 2, 1, 1),
    _W2kStatusSrvcName_Type()
)
w2kStatusSrvcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusSrvcName.setStatus("mandatory")
_W2kStatusSrvcDescription_Type = DisplayString
_W2kStatusSrvcDescription_Object = MibTableColumn
w2kStatusSrvcDescription = _W2kStatusSrvcDescription_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 11, 2, 1, 2),
    _W2kStatusSrvcDescription_Type()
)
w2kStatusSrvcDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusSrvcDescription.setStatus("mandatory")
_W2kStatusSrvcDescr_Type = DisplayString
_W2kStatusSrvcDescr_Object = MibTableColumn
w2kStatusSrvcDescr = _W2kStatusSrvcDescr_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 11, 2, 1, 3),
    _W2kStatusSrvcDescr_Type()
)
w2kStatusSrvcDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusSrvcDescr.setStatus("mandatory")
_W2kStatusSrvcAutoWatcherName_Type = DisplayString
_W2kStatusSrvcAutoWatcherName_Object = MibTableColumn
w2kStatusSrvcAutoWatcherName = _W2kStatusSrvcAutoWatcherName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 11, 2, 1, 4),
    _W2kStatusSrvcAutoWatcherName_Type()
)
w2kStatusSrvcAutoWatcherName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusSrvcAutoWatcherName.setStatus("mandatory")
_W2kStatusSrvcAggLagValue_Type = Integer32
_W2kStatusSrvcAggLagValue_Object = MibTableColumn
w2kStatusSrvcAggLagValue = _W2kStatusSrvcAggLagValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 11, 2, 1, 5),
    _W2kStatusSrvcAggLagValue_Type()
)
w2kStatusSrvcAggLagValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusSrvcAggLagValue.setStatus("mandatory")
_W2kStatusSrvcAggLag_Type = Integer32
_W2kStatusSrvcAggLag_Object = MibTableColumn
w2kStatusSrvcAggLag = _W2kStatusSrvcAggLag_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 11, 2, 1, 6),
    _W2kStatusSrvcAggLag_Type()
)
w2kStatusSrvcAggLag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusSrvcAggLag.setStatus("mandatory")


class _W2kStatusSrvcAggStatus_Type(Integer32):
    """Custom type w2kStatusSrvcAggStatus based on Integer32"""
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
        *(("critical", 4),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_W2kStatusSrvcAggStatus_Type.__name__ = "Integer32"
_W2kStatusSrvcAggStatus_Object = MibTableColumn
w2kStatusSrvcAggStatus = _W2kStatusSrvcAggStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 11, 2, 1, 7),
    _W2kStatusSrvcAggStatus_Type()
)
w2kStatusSrvcAggStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusSrvcAggStatus.setStatus("mandatory")


class _W2kStatusSrvcExist_Type(Integer32):
    """Custom type w2kStatusSrvcExist based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("should-exist", 1),
          ("should-not-exist", 2))
    )


_W2kStatusSrvcExist_Type.__name__ = "Integer32"
_W2kStatusSrvcExist_Object = MibTableColumn
w2kStatusSrvcExist = _W2kStatusSrvcExist_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 11, 2, 1, 8),
    _W2kStatusSrvcExist_Type()
)
w2kStatusSrvcExist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusSrvcExist.setStatus("mandatory")


class _W2kStatusSrvcExistMonitor_Type(Integer32):
    """Custom type w2kStatusSrvcExistMonitor based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("do-not-monitor", 1),
          ("down-critical", 3),
          ("down-warning", 2))
    )


_W2kStatusSrvcExistMonitor_Type.__name__ = "Integer32"
_W2kStatusSrvcExistMonitor_Object = MibTableColumn
w2kStatusSrvcExistMonitor = _W2kStatusSrvcExistMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 11, 2, 1, 9),
    _W2kStatusSrvcExistMonitor_Type()
)
w2kStatusSrvcExistMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusSrvcExistMonitor.setStatus("mandatory")


class _W2kStatusSrvcExistStatus_Type(Integer32):
    """Custom type w2kStatusSrvcExistStatus based on Integer32"""
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
        *(("down-critical", 4),
          ("down-warning", 3),
          ("unknown", 1),
          ("up", 2))
    )


_W2kStatusSrvcExistStatus_Type.__name__ = "Integer32"
_W2kStatusSrvcExistStatus_Object = MibTableColumn
w2kStatusSrvcExistStatus = _W2kStatusSrvcExistStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 11, 2, 1, 10),
    _W2kStatusSrvcExistStatus_Type()
)
w2kStatusSrvcExistStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusSrvcExistStatus.setStatus("mandatory")


class _W2kStatusSrvcActiveValue_Type(Integer32):
    """Custom type w2kStatusSrvcActiveValue based on Integer32"""
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
        *(("active-pausePending", 3),
          ("active-running", 2),
          ("active-stopPending", 4),
          ("notActive-continuePending", 7),
          ("notActive-paused", 6),
          ("notActive-startPending", 8),
          ("notActive-stopped", 5),
          ("unknown", 1))
    )


_W2kStatusSrvcActiveValue_Type.__name__ = "Integer32"
_W2kStatusSrvcActiveValue_Object = MibTableColumn
w2kStatusSrvcActiveValue = _W2kStatusSrvcActiveValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 11, 2, 1, 11),
    _W2kStatusSrvcActiveValue_Type()
)
w2kStatusSrvcActiveValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusSrvcActiveValue.setStatus("mandatory")


class _W2kStatusSrvcActive_Type(Integer32):
    """Custom type w2kStatusSrvcActive based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("should-be-active", 1),
          ("should-not-be-active", 2))
    )


_W2kStatusSrvcActive_Type.__name__ = "Integer32"
_W2kStatusSrvcActive_Object = MibTableColumn
w2kStatusSrvcActive = _W2kStatusSrvcActive_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 11, 2, 1, 12),
    _W2kStatusSrvcActive_Type()
)
w2kStatusSrvcActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusSrvcActive.setStatus("mandatory")


class _W2kStatusSrvcActiveMonitor_Type(Integer32):
    """Custom type w2kStatusSrvcActiveMonitor based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("do-not-monitor", 1),
          ("down-critical", 3),
          ("down-warning", 2))
    )


_W2kStatusSrvcActiveMonitor_Type.__name__ = "Integer32"
_W2kStatusSrvcActiveMonitor_Object = MibTableColumn
w2kStatusSrvcActiveMonitor = _W2kStatusSrvcActiveMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 11, 2, 1, 13),
    _W2kStatusSrvcActiveMonitor_Type()
)
w2kStatusSrvcActiveMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusSrvcActiveMonitor.setStatus("mandatory")


class _W2kStatusSrvcActiveStatus_Type(Integer32):
    """Custom type w2kStatusSrvcActiveStatus based on Integer32"""
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
        *(("down-critical", 4),
          ("down-warning", 3),
          ("unknown", 1),
          ("up", 2))
    )


_W2kStatusSrvcActiveStatus_Type.__name__ = "Integer32"
_W2kStatusSrvcActiveStatus_Object = MibTableColumn
w2kStatusSrvcActiveStatus = _W2kStatusSrvcActiveStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 11, 2, 1, 14),
    _W2kStatusSrvcActiveStatus_Type()
)
w2kStatusSrvcActiveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusSrvcActiveStatus.setStatus("mandatory")
_W2kStatusSrvcCallBackRef_Type = DisplayString
_W2kStatusSrvcCallBackRef_Object = MibTableColumn
w2kStatusSrvcCallBackRef = _W2kStatusSrvcCallBackRef_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 11, 2, 1, 15),
    _W2kStatusSrvcCallBackRef_Type()
)
w2kStatusSrvcCallBackRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusSrvcCallBackRef.setStatus("mandatory")


class _W2kStatusSrvcButton_Type(Integer32):
    """Custom type w2kStatusSrvcButton based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("remove", 2))
    )


_W2kStatusSrvcButton_Type.__name__ = "Integer32"
_W2kStatusSrvcButton_Object = MibTableColumn
w2kStatusSrvcButton = _W2kStatusSrvcButton_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 11, 2, 1, 16),
    _W2kStatusSrvcButton_Type()
)
w2kStatusSrvcButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusSrvcButton.setStatus("mandatory")
_W2kStatusJobGroup_ObjectIdentity = ObjectIdentity
w2kStatusJobGroup = _W2kStatusJobGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 12)
)
_W2kStatusJobCount_Type = Integer32
_W2kStatusJobCount_Object = MibScalar
w2kStatusJobCount = _W2kStatusJobCount_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 12, 1),
    _W2kStatusJobCount_Type()
)
w2kStatusJobCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusJobCount.setStatus("mandatory")
_W2kStatusJobTable_Object = MibTable
w2kStatusJobTable = _W2kStatusJobTable_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 12, 2)
)
if mibBuilder.loadTexts:
    w2kStatusJobTable.setStatus("mandatory")
_W2kStatusJobEntry_Object = MibTableRow
w2kStatusJobEntry = _W2kStatusJobEntry_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 12, 2, 1)
)
w2kStatusJobEntry.setIndexNames(
    (0, "CA-W2KOS-MIB", "w2kStatusJobName"),
)
if mibBuilder.loadTexts:
    w2kStatusJobEntry.setStatus("mandatory")
_W2kStatusJobName_Type = DisplayString
_W2kStatusJobName_Object = MibTableColumn
w2kStatusJobName = _W2kStatusJobName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 12, 2, 1, 1),
    _W2kStatusJobName_Type()
)
w2kStatusJobName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusJobName.setStatus("mandatory")
_W2kStatusJobDescription_Type = DisplayString
_W2kStatusJobDescription_Object = MibTableColumn
w2kStatusJobDescription = _W2kStatusJobDescription_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 12, 2, 1, 2),
    _W2kStatusJobDescription_Type()
)
w2kStatusJobDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusJobDescription.setStatus("mandatory")
_W2kStatusJobAggLagValue_Type = Integer32
_W2kStatusJobAggLagValue_Object = MibTableColumn
w2kStatusJobAggLagValue = _W2kStatusJobAggLagValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 12, 2, 1, 3),
    _W2kStatusJobAggLagValue_Type()
)
w2kStatusJobAggLagValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusJobAggLagValue.setStatus("mandatory")
_W2kStatusJobAggLag_Type = Integer32
_W2kStatusJobAggLag_Object = MibTableColumn
w2kStatusJobAggLag = _W2kStatusJobAggLag_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 12, 2, 1, 4),
    _W2kStatusJobAggLag_Type()
)
w2kStatusJobAggLag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusJobAggLag.setStatus("mandatory")


class _W2kStatusJobAggStatus_Type(Integer32):
    """Custom type w2kStatusJobAggStatus based on Integer32"""
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
        *(("critical", 4),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_W2kStatusJobAggStatus_Type.__name__ = "Integer32"
_W2kStatusJobAggStatus_Object = MibTableColumn
w2kStatusJobAggStatus = _W2kStatusJobAggStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 12, 2, 1, 5),
    _W2kStatusJobAggStatus_Type()
)
w2kStatusJobAggStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusJobAggStatus.setStatus("mandatory")


class _W2kStatusJobExist_Type(Integer32):
    """Custom type w2kStatusJobExist based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("should-exist", 1),
          ("should-not-exist", 2))
    )


_W2kStatusJobExist_Type.__name__ = "Integer32"
_W2kStatusJobExist_Object = MibTableColumn
w2kStatusJobExist = _W2kStatusJobExist_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 12, 2, 1, 6),
    _W2kStatusJobExist_Type()
)
w2kStatusJobExist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusJobExist.setStatus("mandatory")


class _W2kStatusJobExistMonitor_Type(Integer32):
    """Custom type w2kStatusJobExistMonitor based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("do-not-monitor", 1),
          ("down-critical", 3),
          ("down-warning", 2))
    )


_W2kStatusJobExistMonitor_Type.__name__ = "Integer32"
_W2kStatusJobExistMonitor_Object = MibTableColumn
w2kStatusJobExistMonitor = _W2kStatusJobExistMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 12, 2, 1, 7),
    _W2kStatusJobExistMonitor_Type()
)
w2kStatusJobExistMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusJobExistMonitor.setStatus("mandatory")


class _W2kStatusJobExistStatus_Type(Integer32):
    """Custom type w2kStatusJobExistStatus based on Integer32"""
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
        *(("down-critical", 4),
          ("down-warning", 3),
          ("unknown", 1),
          ("up", 2))
    )


_W2kStatusJobExistStatus_Type.__name__ = "Integer32"
_W2kStatusJobExistStatus_Object = MibTableColumn
w2kStatusJobExistStatus = _W2kStatusJobExistStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 12, 2, 1, 8),
    _W2kStatusJobExistStatus_Type()
)
w2kStatusJobExistStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusJobExistStatus.setStatus("mandatory")
_W2kStatusJobProcessValue_Type = Integer32
_W2kStatusJobProcessValue_Object = MibTableColumn
w2kStatusJobProcessValue = _W2kStatusJobProcessValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 12, 2, 1, 9),
    _W2kStatusJobProcessValue_Type()
)
w2kStatusJobProcessValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusJobProcessValue.setStatus("mandatory")


class _W2kStatusJobProcessMin_Type(Integer32):
    """Custom type w2kStatusJobProcessMin based on Integer32"""
    defaultValue = -2


_W2kStatusJobProcessMin_Object = MibTableColumn
w2kStatusJobProcessMin = _W2kStatusJobProcessMin_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 12, 2, 1, 10),
    _W2kStatusJobProcessMin_Type()
)
w2kStatusJobProcessMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusJobProcessMin.setStatus("mandatory")


class _W2kStatusJobProcessMax_Type(Integer32):
    """Custom type w2kStatusJobProcessMax based on Integer32"""
    defaultValue = -2


_W2kStatusJobProcessMax_Object = MibTableColumn
w2kStatusJobProcessMax = _W2kStatusJobProcessMax_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 12, 2, 1, 11),
    _W2kStatusJobProcessMax_Type()
)
w2kStatusJobProcessMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusJobProcessMax.setStatus("mandatory")


class _W2kStatusJobProcessMonitor_Type(Integer32):
    """Custom type w2kStatusJobProcessMonitor based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("do-not-monitor", 1),
          ("down-critical", 3),
          ("down-warning", 2))
    )


_W2kStatusJobProcessMonitor_Type.__name__ = "Integer32"
_W2kStatusJobProcessMonitor_Object = MibTableColumn
w2kStatusJobProcessMonitor = _W2kStatusJobProcessMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 12, 2, 1, 12),
    _W2kStatusJobProcessMonitor_Type()
)
w2kStatusJobProcessMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusJobProcessMonitor.setStatus("mandatory")


class _W2kStatusJobProcessStatus_Type(Integer32):
    """Custom type w2kStatusJobProcessStatus based on Integer32"""
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
        *(("down-critical", 4),
          ("down-warning", 3),
          ("unknown", 1),
          ("up", 2))
    )


_W2kStatusJobProcessStatus_Type.__name__ = "Integer32"
_W2kStatusJobProcessStatus_Object = MibTableColumn
w2kStatusJobProcessStatus = _W2kStatusJobProcessStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 12, 2, 1, 13),
    _W2kStatusJobProcessStatus_Type()
)
w2kStatusJobProcessStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusJobProcessStatus.setStatus("mandatory")
_W2kStatusJobCpuValue_Type = Integer32
_W2kStatusJobCpuValue_Object = MibTableColumn
w2kStatusJobCpuValue = _W2kStatusJobCpuValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 12, 2, 1, 14),
    _W2kStatusJobCpuValue_Type()
)
w2kStatusJobCpuValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusJobCpuValue.setStatus("mandatory")
_W2kStatusJobCpuWarn_Type = Integer32
_W2kStatusJobCpuWarn_Object = MibTableColumn
w2kStatusJobCpuWarn = _W2kStatusJobCpuWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 12, 2, 1, 15),
    _W2kStatusJobCpuWarn_Type()
)
w2kStatusJobCpuWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusJobCpuWarn.setStatus("mandatory")
_W2kStatusJobCpuCrit_Type = Integer32
_W2kStatusJobCpuCrit_Object = MibTableColumn
w2kStatusJobCpuCrit = _W2kStatusJobCpuCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 12, 2, 1, 16),
    _W2kStatusJobCpuCrit_Type()
)
w2kStatusJobCpuCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusJobCpuCrit.setStatus("mandatory")


class _W2kStatusJobCpuMonitor_Type(Integer32):
    """Custom type w2kStatusJobCpuMonitor based on Integer32"""
    defaultValue = 0

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
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_W2kStatusJobCpuMonitor_Type.__name__ = "Integer32"
_W2kStatusJobCpuMonitor_Object = MibTableColumn
w2kStatusJobCpuMonitor = _W2kStatusJobCpuMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 12, 2, 1, 17),
    _W2kStatusJobCpuMonitor_Type()
)
w2kStatusJobCpuMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusJobCpuMonitor.setStatus("mandatory")


class _W2kStatusJobCpuStatus_Type(Integer32):
    """Custom type w2kStatusJobCpuStatus based on Integer32"""
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
        *(("critical", 4),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_W2kStatusJobCpuStatus_Type.__name__ = "Integer32"
_W2kStatusJobCpuStatus_Object = MibTableColumn
w2kStatusJobCpuStatus = _W2kStatusJobCpuStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 12, 2, 1, 18),
    _W2kStatusJobCpuStatus_Type()
)
w2kStatusJobCpuStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusJobCpuStatus.setStatus("mandatory")
_W2kStatusJobCallBackRef_Type = DisplayString
_W2kStatusJobCallBackRef_Object = MibTableColumn
w2kStatusJobCallBackRef = _W2kStatusJobCallBackRef_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 12, 2, 1, 19),
    _W2kStatusJobCallBackRef_Type()
)
w2kStatusJobCallBackRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusJobCallBackRef.setStatus("mandatory")


class _W2kStatusJobButton_Type(Integer32):
    """Custom type w2kStatusJobButton based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("remove", 2))
    )


_W2kStatusJobButton_Type.__name__ = "Integer32"
_W2kStatusJobButton_Object = MibTableColumn
w2kStatusJobButton = _W2kStatusJobButton_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 12, 2, 1, 20),
    _W2kStatusJobButton_Type()
)
w2kStatusJobButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusJobButton.setStatus("mandatory")
_W2kStatusSessGroup_ObjectIdentity = ObjectIdentity
w2kStatusSessGroup = _W2kStatusSessGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 13)
)
_W2kStatusSessCount_Type = Integer32
_W2kStatusSessCount_Object = MibScalar
w2kStatusSessCount = _W2kStatusSessCount_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 13, 1),
    _W2kStatusSessCount_Type()
)
w2kStatusSessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusSessCount.setStatus("mandatory")
_W2kStatusSessTable_Object = MibTable
w2kStatusSessTable = _W2kStatusSessTable_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 13, 2)
)
if mibBuilder.loadTexts:
    w2kStatusSessTable.setStatus("mandatory")
_W2kStatusSessEntry_Object = MibTableRow
w2kStatusSessEntry = _W2kStatusSessEntry_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 13, 2, 1)
)
w2kStatusSessEntry.setIndexNames(
    (0, "CA-W2KOS-MIB", "w2kStatusSessClientName"),
    (0, "CA-W2KOS-MIB", "w2kStatusSessUserName"),
)
if mibBuilder.loadTexts:
    w2kStatusSessEntry.setStatus("mandatory")
_W2kStatusSessClientName_Type = DisplayString
_W2kStatusSessClientName_Object = MibTableColumn
w2kStatusSessClientName = _W2kStatusSessClientName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 13, 2, 1, 1),
    _W2kStatusSessClientName_Type()
)
w2kStatusSessClientName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusSessClientName.setStatus("mandatory")
_W2kStatusSessUserName_Type = DisplayString
_W2kStatusSessUserName_Object = MibTableColumn
w2kStatusSessUserName = _W2kStatusSessUserName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 13, 2, 1, 2),
    _W2kStatusSessUserName_Type()
)
w2kStatusSessUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusSessUserName.setStatus("mandatory")
_W2kStatusSessDescription_Type = DisplayString
_W2kStatusSessDescription_Object = MibTableColumn
w2kStatusSessDescription = _W2kStatusSessDescription_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 13, 2, 1, 3),
    _W2kStatusSessDescription_Type()
)
w2kStatusSessDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusSessDescription.setStatus("mandatory")
_W2kStatusSessIds_Type = DisplayString
_W2kStatusSessIds_Object = MibTableColumn
w2kStatusSessIds = _W2kStatusSessIds_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 13, 2, 1, 4),
    _W2kStatusSessIds_Type()
)
w2kStatusSessIds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusSessIds.setStatus("mandatory")
_W2kStatusSessAggLagValue_Type = Integer32
_W2kStatusSessAggLagValue_Object = MibTableColumn
w2kStatusSessAggLagValue = _W2kStatusSessAggLagValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 13, 2, 1, 5),
    _W2kStatusSessAggLagValue_Type()
)
w2kStatusSessAggLagValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusSessAggLagValue.setStatus("mandatory")
_W2kStatusSessAggLag_Type = Integer32
_W2kStatusSessAggLag_Object = MibTableColumn
w2kStatusSessAggLag = _W2kStatusSessAggLag_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 13, 2, 1, 6),
    _W2kStatusSessAggLag_Type()
)
w2kStatusSessAggLag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusSessAggLag.setStatus("mandatory")


class _W2kStatusSessAggStatus_Type(Integer32):
    """Custom type w2kStatusSessAggStatus based on Integer32"""
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
        *(("critical", 4),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_W2kStatusSessAggStatus_Type.__name__ = "Integer32"
_W2kStatusSessAggStatus_Object = MibTableColumn
w2kStatusSessAggStatus = _W2kStatusSessAggStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 13, 2, 1, 7),
    _W2kStatusSessAggStatus_Type()
)
w2kStatusSessAggStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusSessAggStatus.setStatus("mandatory")
_W2kStatusSessInstValue_Type = Integer32
_W2kStatusSessInstValue_Object = MibTableColumn
w2kStatusSessInstValue = _W2kStatusSessInstValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 13, 2, 1, 8),
    _W2kStatusSessInstValue_Type()
)
w2kStatusSessInstValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusSessInstValue.setStatus("mandatory")


class _W2kStatusSessInstMin_Type(Integer32):
    """Custom type w2kStatusSessInstMin based on Integer32"""
    defaultValue = -2


_W2kStatusSessInstMin_Object = MibTableColumn
w2kStatusSessInstMin = _W2kStatusSessInstMin_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 13, 2, 1, 9),
    _W2kStatusSessInstMin_Type()
)
w2kStatusSessInstMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusSessInstMin.setStatus("mandatory")


class _W2kStatusSessInstMax_Type(Integer32):
    """Custom type w2kStatusSessInstMax based on Integer32"""
    defaultValue = -2


_W2kStatusSessInstMax_Object = MibTableColumn
w2kStatusSessInstMax = _W2kStatusSessInstMax_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 13, 2, 1, 10),
    _W2kStatusSessInstMax_Type()
)
w2kStatusSessInstMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusSessInstMax.setStatus("mandatory")


class _W2kStatusSessInstMonitor_Type(Integer32):
    """Custom type w2kStatusSessInstMonitor based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("do-not-monitor", 1),
          ("down-critical", 3),
          ("down-warning", 2))
    )


_W2kStatusSessInstMonitor_Type.__name__ = "Integer32"
_W2kStatusSessInstMonitor_Object = MibTableColumn
w2kStatusSessInstMonitor = _W2kStatusSessInstMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 13, 2, 1, 11),
    _W2kStatusSessInstMonitor_Type()
)
w2kStatusSessInstMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusSessInstMonitor.setStatus("mandatory")


class _W2kStatusSessInstStatus_Type(Integer32):
    """Custom type w2kStatusSessInstStatus based on Integer32"""
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
        *(("down-critical", 4),
          ("down-warning", 3),
          ("unknown", 1),
          ("up", 2))
    )


_W2kStatusSessInstStatus_Type.__name__ = "Integer32"
_W2kStatusSessInstStatus_Object = MibTableColumn
w2kStatusSessInstStatus = _W2kStatusSessInstStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 13, 2, 1, 12),
    _W2kStatusSessInstStatus_Type()
)
w2kStatusSessInstStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusSessInstStatus.setStatus("mandatory")
_W2kStatusSessMemoryValue_Type = Integer32
_W2kStatusSessMemoryValue_Object = MibTableColumn
w2kStatusSessMemoryValue = _W2kStatusSessMemoryValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 13, 2, 1, 13),
    _W2kStatusSessMemoryValue_Type()
)
w2kStatusSessMemoryValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusSessMemoryValue.setStatus("mandatory")
_W2kStatusSessMemoryWarn_Type = Integer32
_W2kStatusSessMemoryWarn_Object = MibTableColumn
w2kStatusSessMemoryWarn = _W2kStatusSessMemoryWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 13, 2, 1, 14),
    _W2kStatusSessMemoryWarn_Type()
)
w2kStatusSessMemoryWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusSessMemoryWarn.setStatus("mandatory")
_W2kStatusSessMemoryCrit_Type = Integer32
_W2kStatusSessMemoryCrit_Object = MibTableColumn
w2kStatusSessMemoryCrit = _W2kStatusSessMemoryCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 13, 2, 1, 15),
    _W2kStatusSessMemoryCrit_Type()
)
w2kStatusSessMemoryCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusSessMemoryCrit.setStatus("mandatory")


class _W2kStatusSessMemoryMonitor_Type(Integer32):
    """Custom type w2kStatusSessMemoryMonitor based on Integer32"""
    defaultValue = 0

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
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_W2kStatusSessMemoryMonitor_Type.__name__ = "Integer32"
_W2kStatusSessMemoryMonitor_Object = MibTableColumn
w2kStatusSessMemoryMonitor = _W2kStatusSessMemoryMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 13, 2, 1, 16),
    _W2kStatusSessMemoryMonitor_Type()
)
w2kStatusSessMemoryMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusSessMemoryMonitor.setStatus("mandatory")


class _W2kStatusSessMemoryStatus_Type(Integer32):
    """Custom type w2kStatusSessMemoryStatus based on Integer32"""
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
        *(("critical", 4),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_W2kStatusSessMemoryStatus_Type.__name__ = "Integer32"
_W2kStatusSessMemoryStatus_Object = MibTableColumn
w2kStatusSessMemoryStatus = _W2kStatusSessMemoryStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 13, 2, 1, 17),
    _W2kStatusSessMemoryStatus_Type()
)
w2kStatusSessMemoryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusSessMemoryStatus.setStatus("mandatory")
_W2kStatusSessCpuValue_Type = Integer32
_W2kStatusSessCpuValue_Object = MibTableColumn
w2kStatusSessCpuValue = _W2kStatusSessCpuValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 13, 2, 1, 18),
    _W2kStatusSessCpuValue_Type()
)
w2kStatusSessCpuValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusSessCpuValue.setStatus("mandatory")
_W2kStatusSessCpuWarn_Type = Integer32
_W2kStatusSessCpuWarn_Object = MibTableColumn
w2kStatusSessCpuWarn = _W2kStatusSessCpuWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 13, 2, 1, 19),
    _W2kStatusSessCpuWarn_Type()
)
w2kStatusSessCpuWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusSessCpuWarn.setStatus("mandatory")
_W2kStatusSessCpuCrit_Type = Integer32
_W2kStatusSessCpuCrit_Object = MibTableColumn
w2kStatusSessCpuCrit = _W2kStatusSessCpuCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 13, 2, 1, 20),
    _W2kStatusSessCpuCrit_Type()
)
w2kStatusSessCpuCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusSessCpuCrit.setStatus("mandatory")


class _W2kStatusSessCpuMonitor_Type(Integer32):
    """Custom type w2kStatusSessCpuMonitor based on Integer32"""
    defaultValue = 0

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
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_W2kStatusSessCpuMonitor_Type.__name__ = "Integer32"
_W2kStatusSessCpuMonitor_Object = MibTableColumn
w2kStatusSessCpuMonitor = _W2kStatusSessCpuMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 13, 2, 1, 21),
    _W2kStatusSessCpuMonitor_Type()
)
w2kStatusSessCpuMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusSessCpuMonitor.setStatus("mandatory")


class _W2kStatusSessCpuStatus_Type(Integer32):
    """Custom type w2kStatusSessCpuStatus based on Integer32"""
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
        *(("critical", 4),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_W2kStatusSessCpuStatus_Type.__name__ = "Integer32"
_W2kStatusSessCpuStatus_Object = MibTableColumn
w2kStatusSessCpuStatus = _W2kStatusSessCpuStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 13, 2, 1, 22),
    _W2kStatusSessCpuStatus_Type()
)
w2kStatusSessCpuStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusSessCpuStatus.setStatus("mandatory")
_W2kStatusSessCallBackRef_Type = DisplayString
_W2kStatusSessCallBackRef_Object = MibTableColumn
w2kStatusSessCallBackRef = _W2kStatusSessCallBackRef_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 13, 2, 1, 23),
    _W2kStatusSessCallBackRef_Type()
)
w2kStatusSessCallBackRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusSessCallBackRef.setStatus("mandatory")


class _W2kStatusSessButton_Type(Integer32):
    """Custom type w2kStatusSessButton based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("remove", 2))
    )


_W2kStatusSessButton_Type.__name__ = "Integer32"
_W2kStatusSessButton_Object = MibTableColumn
w2kStatusSessButton = _W2kStatusSessButton_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 13, 2, 1, 24),
    _W2kStatusSessButton_Type()
)
w2kStatusSessButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusSessButton.setStatus("mandatory")
_W2kStatusPrnGroup_ObjectIdentity = ObjectIdentity
w2kStatusPrnGroup = _W2kStatusPrnGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 14)
)
_W2kStatusPrnCount_Type = Integer32
_W2kStatusPrnCount_Object = MibScalar
w2kStatusPrnCount = _W2kStatusPrnCount_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 14, 1),
    _W2kStatusPrnCount_Type()
)
w2kStatusPrnCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusPrnCount.setStatus("mandatory")
_W2kStatusPrnTable_Object = MibTable
w2kStatusPrnTable = _W2kStatusPrnTable_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 14, 2)
)
if mibBuilder.loadTexts:
    w2kStatusPrnTable.setStatus("mandatory")
_W2kStatusPrnEntry_Object = MibTableRow
w2kStatusPrnEntry = _W2kStatusPrnEntry_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 14, 2, 1)
)
w2kStatusPrnEntry.setIndexNames(
    (0, "CA-W2KOS-MIB", "w2kStatusPrnName"),
)
if mibBuilder.loadTexts:
    w2kStatusPrnEntry.setStatus("mandatory")
_W2kStatusPrnName_Type = DisplayString
_W2kStatusPrnName_Object = MibTableColumn
w2kStatusPrnName = _W2kStatusPrnName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 14, 2, 1, 1),
    _W2kStatusPrnName_Type()
)
w2kStatusPrnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusPrnName.setStatus("mandatory")
_W2kStatusPrnDescription_Type = DisplayString
_W2kStatusPrnDescription_Object = MibTableColumn
w2kStatusPrnDescription = _W2kStatusPrnDescription_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 14, 2, 1, 2),
    _W2kStatusPrnDescription_Type()
)
w2kStatusPrnDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusPrnDescription.setStatus("mandatory")
_W2kStatusPrnAutoWatcherName_Type = DisplayString
_W2kStatusPrnAutoWatcherName_Object = MibTableColumn
w2kStatusPrnAutoWatcherName = _W2kStatusPrnAutoWatcherName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 14, 2, 1, 3),
    _W2kStatusPrnAutoWatcherName_Type()
)
w2kStatusPrnAutoWatcherName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusPrnAutoWatcherName.setStatus("mandatory")
_W2kStatusPrnAggLagValue_Type = Integer32
_W2kStatusPrnAggLagValue_Object = MibTableColumn
w2kStatusPrnAggLagValue = _W2kStatusPrnAggLagValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 14, 2, 1, 4),
    _W2kStatusPrnAggLagValue_Type()
)
w2kStatusPrnAggLagValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusPrnAggLagValue.setStatus("mandatory")
_W2kStatusPrnAggLag_Type = Integer32
_W2kStatusPrnAggLag_Object = MibTableColumn
w2kStatusPrnAggLag = _W2kStatusPrnAggLag_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 14, 2, 1, 5),
    _W2kStatusPrnAggLag_Type()
)
w2kStatusPrnAggLag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusPrnAggLag.setStatus("mandatory")


class _W2kStatusPrnAggStatus_Type(Integer32):
    """Custom type w2kStatusPrnAggStatus based on Integer32"""
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
        *(("critical", 4),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_W2kStatusPrnAggStatus_Type.__name__ = "Integer32"
_W2kStatusPrnAggStatus_Object = MibTableColumn
w2kStatusPrnAggStatus = _W2kStatusPrnAggStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 14, 2, 1, 6),
    _W2kStatusPrnAggStatus_Type()
)
w2kStatusPrnAggStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusPrnAggStatus.setStatus("mandatory")


class _W2kStatusPrnEventDescr_Type(Integer32):
    """Custom type w2kStatusPrnEventDescr based on Integer32"""
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
        *(("general-error", 9),
          ("manual", 5),
          ("offline", 6),
          ("paper-error", 3),
          ("paused", 7),
          ("printing", 2),
          ("software-error", 8),
          ("toner-error", 4),
          ("unknown-no-print-jobs", 1))
    )


_W2kStatusPrnEventDescr_Type.__name__ = "Integer32"
_W2kStatusPrnEventDescr_Object = MibTableColumn
w2kStatusPrnEventDescr = _W2kStatusPrnEventDescr_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 14, 2, 1, 7),
    _W2kStatusPrnEventDescr_Type()
)
w2kStatusPrnEventDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusPrnEventDescr.setStatus("mandatory")


class _W2kStatusPrnEventMonitor_Type(Integer32):
    """Custom type w2kStatusPrnEventMonitor based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("do-not-monitor", 1),
          ("down-critical", 3),
          ("down-warning", 2))
    )


_W2kStatusPrnEventMonitor_Type.__name__ = "Integer32"
_W2kStatusPrnEventMonitor_Object = MibTableColumn
w2kStatusPrnEventMonitor = _W2kStatusPrnEventMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 14, 2, 1, 8),
    _W2kStatusPrnEventMonitor_Type()
)
w2kStatusPrnEventMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusPrnEventMonitor.setStatus("mandatory")


class _W2kStatusPrnEventStatus_Type(Integer32):
    """Custom type w2kStatusPrnEventStatus based on Integer32"""
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
        *(("down-critical", 4),
          ("down-warning", 3),
          ("unknown", 1),
          ("up", 2))
    )


_W2kStatusPrnEventStatus_Type.__name__ = "Integer32"
_W2kStatusPrnEventStatus_Object = MibTableColumn
w2kStatusPrnEventStatus = _W2kStatusPrnEventStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 14, 2, 1, 9),
    _W2kStatusPrnEventStatus_Type()
)
w2kStatusPrnEventStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusPrnEventStatus.setStatus("mandatory")
_W2kStatusPrnQueueValue_Type = Integer32
_W2kStatusPrnQueueValue_Object = MibTableColumn
w2kStatusPrnQueueValue = _W2kStatusPrnQueueValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 14, 2, 1, 10),
    _W2kStatusPrnQueueValue_Type()
)
w2kStatusPrnQueueValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusPrnQueueValue.setStatus("mandatory")
_W2kStatusPrnQueueWarn_Type = Integer32
_W2kStatusPrnQueueWarn_Object = MibTableColumn
w2kStatusPrnQueueWarn = _W2kStatusPrnQueueWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 14, 2, 1, 11),
    _W2kStatusPrnQueueWarn_Type()
)
w2kStatusPrnQueueWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusPrnQueueWarn.setStatus("mandatory")
_W2kStatusPrnQueueCrit_Type = Integer32
_W2kStatusPrnQueueCrit_Object = MibTableColumn
w2kStatusPrnQueueCrit = _W2kStatusPrnQueueCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 14, 2, 1, 12),
    _W2kStatusPrnQueueCrit_Type()
)
w2kStatusPrnQueueCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusPrnQueueCrit.setStatus("mandatory")


class _W2kStatusPrnQueueMonitor_Type(Integer32):
    """Custom type w2kStatusPrnQueueMonitor based on Integer32"""
    defaultValue = 0

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
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_W2kStatusPrnQueueMonitor_Type.__name__ = "Integer32"
_W2kStatusPrnQueueMonitor_Object = MibTableColumn
w2kStatusPrnQueueMonitor = _W2kStatusPrnQueueMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 14, 2, 1, 13),
    _W2kStatusPrnQueueMonitor_Type()
)
w2kStatusPrnQueueMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusPrnQueueMonitor.setStatus("mandatory")


class _W2kStatusPrnQueueStatus_Type(Integer32):
    """Custom type w2kStatusPrnQueueStatus based on Integer32"""
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
        *(("critical", 4),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_W2kStatusPrnQueueStatus_Type.__name__ = "Integer32"
_W2kStatusPrnQueueStatus_Object = MibTableColumn
w2kStatusPrnQueueStatus = _W2kStatusPrnQueueStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 14, 2, 1, 14),
    _W2kStatusPrnQueueStatus_Type()
)
w2kStatusPrnQueueStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusPrnQueueStatus.setStatus("mandatory")


class _W2kStatusPrnLossAction_Type(Integer32):
    """Custom type w2kStatusPrnLossAction based on Integer32"""
    defaultValue = 0

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
        *(("down-critical", 4),
          ("down-warning", 3),
          ("remove", 1),
          ("up", 2))
    )


_W2kStatusPrnLossAction_Type.__name__ = "Integer32"
_W2kStatusPrnLossAction_Object = MibTableColumn
w2kStatusPrnLossAction = _W2kStatusPrnLossAction_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 14, 2, 1, 15),
    _W2kStatusPrnLossAction_Type()
)
w2kStatusPrnLossAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusPrnLossAction.setStatus("mandatory")


class _W2kStatusPrnLossStatus_Type(Integer32):
    """Custom type w2kStatusPrnLossStatus based on Integer32"""
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
        *(("down-critical", 4),
          ("down-warning", 3),
          ("unknown", 1),
          ("up", 2))
    )


_W2kStatusPrnLossStatus_Type.__name__ = "Integer32"
_W2kStatusPrnLossStatus_Object = MibTableColumn
w2kStatusPrnLossStatus = _W2kStatusPrnLossStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 14, 2, 1, 16),
    _W2kStatusPrnLossStatus_Type()
)
w2kStatusPrnLossStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusPrnLossStatus.setStatus("mandatory")
_W2kStatusPrnCallBackRef_Type = DisplayString
_W2kStatusPrnCallBackRef_Object = MibTableColumn
w2kStatusPrnCallBackRef = _W2kStatusPrnCallBackRef_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 14, 2, 1, 17),
    _W2kStatusPrnCallBackRef_Type()
)
w2kStatusPrnCallBackRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusPrnCallBackRef.setStatus("mandatory")


class _W2kStatusPrnButton_Type(Integer32):
    """Custom type w2kStatusPrnButton based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("remove", 2))
    )


_W2kStatusPrnButton_Type.__name__ = "Integer32"
_W2kStatusPrnButton_Object = MibTableColumn
w2kStatusPrnButton = _W2kStatusPrnButton_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 14, 2, 1, 18),
    _W2kStatusPrnButton_Type()
)
w2kStatusPrnButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusPrnButton.setStatus("mandatory")
_W2kStatusNetGroup_ObjectIdentity = ObjectIdentity
w2kStatusNetGroup = _W2kStatusNetGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 15)
)
_W2kStatusNetTotalAggLagValue_Type = Integer32
_W2kStatusNetTotalAggLagValue_Object = MibScalar
w2kStatusNetTotalAggLagValue = _W2kStatusNetTotalAggLagValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 15, 1),
    _W2kStatusNetTotalAggLagValue_Type()
)
w2kStatusNetTotalAggLagValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusNetTotalAggLagValue.setStatus("mandatory")


class _W2kStatusNetTotalAggLag_Type(Integer32):
    """Custom type w2kStatusNetTotalAggLag based on Integer32"""
    defaultValue = 1


_W2kStatusNetTotalAggLag_Object = MibScalar
w2kStatusNetTotalAggLag = _W2kStatusNetTotalAggLag_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 15, 2),
    _W2kStatusNetTotalAggLag_Type()
)
w2kStatusNetTotalAggLag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusNetTotalAggLag.setStatus("mandatory")


class _W2kStatusNetTotalAggStatus_Type(Integer32):
    """Custom type w2kStatusNetTotalAggStatus based on Integer32"""
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
        *(("critical", 4),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_W2kStatusNetTotalAggStatus_Type.__name__ = "Integer32"
_W2kStatusNetTotalAggStatus_Object = MibScalar
w2kStatusNetTotalAggStatus = _W2kStatusNetTotalAggStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 15, 3),
    _W2kStatusNetTotalAggStatus_Type()
)
w2kStatusNetTotalAggStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusNetTotalAggStatus.setStatus("mandatory")
_W2kStatusNetTotalInPktValue_Type = Integer32
_W2kStatusNetTotalInPktValue_Object = MibScalar
w2kStatusNetTotalInPktValue = _W2kStatusNetTotalInPktValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 15, 4),
    _W2kStatusNetTotalInPktValue_Type()
)
w2kStatusNetTotalInPktValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusNetTotalInPktValue.setStatus("mandatory")


class _W2kStatusNetTotalInPktWarn_Type(Integer32):
    """Custom type w2kStatusNetTotalInPktWarn based on Integer32"""
    defaultValue = 200


_W2kStatusNetTotalInPktWarn_Object = MibScalar
w2kStatusNetTotalInPktWarn = _W2kStatusNetTotalInPktWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 15, 5),
    _W2kStatusNetTotalInPktWarn_Type()
)
w2kStatusNetTotalInPktWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusNetTotalInPktWarn.setStatus("mandatory")


class _W2kStatusNetTotalInPktCrit_Type(Integer32):
    """Custom type w2kStatusNetTotalInPktCrit based on Integer32"""
    defaultValue = 400


_W2kStatusNetTotalInPktCrit_Object = MibScalar
w2kStatusNetTotalInPktCrit = _W2kStatusNetTotalInPktCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 15, 6),
    _W2kStatusNetTotalInPktCrit_Type()
)
w2kStatusNetTotalInPktCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusNetTotalInPktCrit.setStatus("mandatory")


class _W2kStatusNetTotalInPktMonitor_Type(Integer32):
    """Custom type w2kStatusNetTotalInPktMonitor based on Integer32"""
    defaultValue = 4

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
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_W2kStatusNetTotalInPktMonitor_Type.__name__ = "Integer32"
_W2kStatusNetTotalInPktMonitor_Object = MibScalar
w2kStatusNetTotalInPktMonitor = _W2kStatusNetTotalInPktMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 15, 7),
    _W2kStatusNetTotalInPktMonitor_Type()
)
w2kStatusNetTotalInPktMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusNetTotalInPktMonitor.setStatus("mandatory")


class _W2kStatusNetTotalInPktStatus_Type(Integer32):
    """Custom type w2kStatusNetTotalInPktStatus based on Integer32"""
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
        *(("critical", 4),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_W2kStatusNetTotalInPktStatus_Type.__name__ = "Integer32"
_W2kStatusNetTotalInPktStatus_Object = MibScalar
w2kStatusNetTotalInPktStatus = _W2kStatusNetTotalInPktStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 15, 8),
    _W2kStatusNetTotalInPktStatus_Type()
)
w2kStatusNetTotalInPktStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusNetTotalInPktStatus.setStatus("mandatory")
_W2kStatusNetTotalOutPktValue_Type = Integer32
_W2kStatusNetTotalOutPktValue_Object = MibScalar
w2kStatusNetTotalOutPktValue = _W2kStatusNetTotalOutPktValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 15, 9),
    _W2kStatusNetTotalOutPktValue_Type()
)
w2kStatusNetTotalOutPktValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusNetTotalOutPktValue.setStatus("mandatory")


class _W2kStatusNetTotalOutPktWarn_Type(Integer32):
    """Custom type w2kStatusNetTotalOutPktWarn based on Integer32"""
    defaultValue = 200


_W2kStatusNetTotalOutPktWarn_Object = MibScalar
w2kStatusNetTotalOutPktWarn = _W2kStatusNetTotalOutPktWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 15, 10),
    _W2kStatusNetTotalOutPktWarn_Type()
)
w2kStatusNetTotalOutPktWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusNetTotalOutPktWarn.setStatus("mandatory")


class _W2kStatusNetTotalOutPktCrit_Type(Integer32):
    """Custom type w2kStatusNetTotalOutPktCrit based on Integer32"""
    defaultValue = 400


_W2kStatusNetTotalOutPktCrit_Object = MibScalar
w2kStatusNetTotalOutPktCrit = _W2kStatusNetTotalOutPktCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 15, 11),
    _W2kStatusNetTotalOutPktCrit_Type()
)
w2kStatusNetTotalOutPktCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusNetTotalOutPktCrit.setStatus("mandatory")


class _W2kStatusNetTotalOutPktMonitor_Type(Integer32):
    """Custom type w2kStatusNetTotalOutPktMonitor based on Integer32"""
    defaultValue = 4

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
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_W2kStatusNetTotalOutPktMonitor_Type.__name__ = "Integer32"
_W2kStatusNetTotalOutPktMonitor_Object = MibScalar
w2kStatusNetTotalOutPktMonitor = _W2kStatusNetTotalOutPktMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 15, 12),
    _W2kStatusNetTotalOutPktMonitor_Type()
)
w2kStatusNetTotalOutPktMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusNetTotalOutPktMonitor.setStatus("mandatory")


class _W2kStatusNetTotalOutPktStatus_Type(Integer32):
    """Custom type w2kStatusNetTotalOutPktStatus based on Integer32"""
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
        *(("critical", 4),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_W2kStatusNetTotalOutPktStatus_Type.__name__ = "Integer32"
_W2kStatusNetTotalOutPktStatus_Object = MibScalar
w2kStatusNetTotalOutPktStatus = _W2kStatusNetTotalOutPktStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 15, 13),
    _W2kStatusNetTotalOutPktStatus_Type()
)
w2kStatusNetTotalOutPktStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusNetTotalOutPktStatus.setStatus("mandatory")
_W2kStatusNetTotalInErrDValue_Type = Integer32
_W2kStatusNetTotalInErrDValue_Object = MibScalar
w2kStatusNetTotalInErrDValue = _W2kStatusNetTotalInErrDValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 15, 14),
    _W2kStatusNetTotalInErrDValue_Type()
)
w2kStatusNetTotalInErrDValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusNetTotalInErrDValue.setStatus("mandatory")


class _W2kStatusNetTotalInErrDWarn_Type(Integer32):
    """Custom type w2kStatusNetTotalInErrDWarn based on Integer32"""
    defaultValue = 20


_W2kStatusNetTotalInErrDWarn_Object = MibScalar
w2kStatusNetTotalInErrDWarn = _W2kStatusNetTotalInErrDWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 15, 15),
    _W2kStatusNetTotalInErrDWarn_Type()
)
w2kStatusNetTotalInErrDWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusNetTotalInErrDWarn.setStatus("mandatory")


class _W2kStatusNetTotalInErrDCrit_Type(Integer32):
    """Custom type w2kStatusNetTotalInErrDCrit based on Integer32"""
    defaultValue = 40


_W2kStatusNetTotalInErrDCrit_Object = MibScalar
w2kStatusNetTotalInErrDCrit = _W2kStatusNetTotalInErrDCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 15, 16),
    _W2kStatusNetTotalInErrDCrit_Type()
)
w2kStatusNetTotalInErrDCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusNetTotalInErrDCrit.setStatus("mandatory")


class _W2kStatusNetTotalInErrDMonitor_Type(Integer32):
    """Custom type w2kStatusNetTotalInErrDMonitor based on Integer32"""
    defaultValue = 4

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
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_W2kStatusNetTotalInErrDMonitor_Type.__name__ = "Integer32"
_W2kStatusNetTotalInErrDMonitor_Object = MibScalar
w2kStatusNetTotalInErrDMonitor = _W2kStatusNetTotalInErrDMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 15, 17),
    _W2kStatusNetTotalInErrDMonitor_Type()
)
w2kStatusNetTotalInErrDMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusNetTotalInErrDMonitor.setStatus("mandatory")


class _W2kStatusNetTotalInErrDStatus_Type(Integer32):
    """Custom type w2kStatusNetTotalInErrDStatus based on Integer32"""
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
        *(("critical", 4),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_W2kStatusNetTotalInErrDStatus_Type.__name__ = "Integer32"
_W2kStatusNetTotalInErrDStatus_Object = MibScalar
w2kStatusNetTotalInErrDStatus = _W2kStatusNetTotalInErrDStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 15, 18),
    _W2kStatusNetTotalInErrDStatus_Type()
)
w2kStatusNetTotalInErrDStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusNetTotalInErrDStatus.setStatus("mandatory")
_W2kStatusNetTotalOutErrDValue_Type = Integer32
_W2kStatusNetTotalOutErrDValue_Object = MibScalar
w2kStatusNetTotalOutErrDValue = _W2kStatusNetTotalOutErrDValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 15, 19),
    _W2kStatusNetTotalOutErrDValue_Type()
)
w2kStatusNetTotalOutErrDValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusNetTotalOutErrDValue.setStatus("mandatory")


class _W2kStatusNetTotalOutErrDWarn_Type(Integer32):
    """Custom type w2kStatusNetTotalOutErrDWarn based on Integer32"""
    defaultValue = 20


_W2kStatusNetTotalOutErrDWarn_Object = MibScalar
w2kStatusNetTotalOutErrDWarn = _W2kStatusNetTotalOutErrDWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 15, 20),
    _W2kStatusNetTotalOutErrDWarn_Type()
)
w2kStatusNetTotalOutErrDWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusNetTotalOutErrDWarn.setStatus("mandatory")


class _W2kStatusNetTotalOutErrDCrit_Type(Integer32):
    """Custom type w2kStatusNetTotalOutErrDCrit based on Integer32"""
    defaultValue = 40


_W2kStatusNetTotalOutErrDCrit_Object = MibScalar
w2kStatusNetTotalOutErrDCrit = _W2kStatusNetTotalOutErrDCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 15, 21),
    _W2kStatusNetTotalOutErrDCrit_Type()
)
w2kStatusNetTotalOutErrDCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusNetTotalOutErrDCrit.setStatus("mandatory")


class _W2kStatusNetTotalOutErrDMonitor_Type(Integer32):
    """Custom type w2kStatusNetTotalOutErrDMonitor based on Integer32"""
    defaultValue = 4

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
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_W2kStatusNetTotalOutErrDMonitor_Type.__name__ = "Integer32"
_W2kStatusNetTotalOutErrDMonitor_Object = MibScalar
w2kStatusNetTotalOutErrDMonitor = _W2kStatusNetTotalOutErrDMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 15, 22),
    _W2kStatusNetTotalOutErrDMonitor_Type()
)
w2kStatusNetTotalOutErrDMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusNetTotalOutErrDMonitor.setStatus("mandatory")


class _W2kStatusNetTotalOutErrDStatus_Type(Integer32):
    """Custom type w2kStatusNetTotalOutErrDStatus based on Integer32"""
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
        *(("critical", 4),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_W2kStatusNetTotalOutErrDStatus_Type.__name__ = "Integer32"
_W2kStatusNetTotalOutErrDStatus_Object = MibScalar
w2kStatusNetTotalOutErrDStatus = _W2kStatusNetTotalOutErrDStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 15, 23),
    _W2kStatusNetTotalOutErrDStatus_Type()
)
w2kStatusNetTotalOutErrDStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusNetTotalOutErrDStatus.setStatus("mandatory")
_W2kStatusNetTotalCallBackRef_Type = DisplayString
_W2kStatusNetTotalCallBackRef_Object = MibScalar
w2kStatusNetTotalCallBackRef = _W2kStatusNetTotalCallBackRef_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 15, 24),
    _W2kStatusNetTotalCallBackRef_Type()
)
w2kStatusNetTotalCallBackRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusNetTotalCallBackRef.setStatus("mandatory")
_W2kStatusNetCount_Type = Integer32
_W2kStatusNetCount_Object = MibScalar
w2kStatusNetCount = _W2kStatusNetCount_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 15, 25),
    _W2kStatusNetCount_Type()
)
w2kStatusNetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusNetCount.setStatus("mandatory")
_W2kStatusNetTable_Object = MibTable
w2kStatusNetTable = _W2kStatusNetTable_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 15, 26)
)
if mibBuilder.loadTexts:
    w2kStatusNetTable.setStatus("mandatory")
_W2kStatusNetEntry_Object = MibTableRow
w2kStatusNetEntry = _W2kStatusNetEntry_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 15, 26, 1)
)
w2kStatusNetEntry.setIndexNames(
    (0, "CA-W2KOS-MIB", "w2kStatusNetName"),
)
if mibBuilder.loadTexts:
    w2kStatusNetEntry.setStatus("mandatory")
_W2kStatusNetName_Type = DisplayString
_W2kStatusNetName_Object = MibTableColumn
w2kStatusNetName = _W2kStatusNetName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 15, 26, 1, 1),
    _W2kStatusNetName_Type()
)
w2kStatusNetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusNetName.setStatus("mandatory")
_W2kStatusNetAggLagValue_Type = Integer32
_W2kStatusNetAggLagValue_Object = MibTableColumn
w2kStatusNetAggLagValue = _W2kStatusNetAggLagValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 15, 26, 1, 2),
    _W2kStatusNetAggLagValue_Type()
)
w2kStatusNetAggLagValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusNetAggLagValue.setStatus("mandatory")
_W2kStatusNetAggLag_Type = Integer32
_W2kStatusNetAggLag_Object = MibTableColumn
w2kStatusNetAggLag = _W2kStatusNetAggLag_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 15, 26, 1, 3),
    _W2kStatusNetAggLag_Type()
)
w2kStatusNetAggLag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusNetAggLag.setStatus("mandatory")


class _W2kStatusNetAggStatus_Type(Integer32):
    """Custom type w2kStatusNetAggStatus based on Integer32"""
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
        *(("critical", 4),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_W2kStatusNetAggStatus_Type.__name__ = "Integer32"
_W2kStatusNetAggStatus_Object = MibTableColumn
w2kStatusNetAggStatus = _W2kStatusNetAggStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 15, 26, 1, 4),
    _W2kStatusNetAggStatus_Type()
)
w2kStatusNetAggStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusNetAggStatus.setStatus("mandatory")
_W2kStatusNetInPktValue_Type = Integer32
_W2kStatusNetInPktValue_Object = MibTableColumn
w2kStatusNetInPktValue = _W2kStatusNetInPktValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 15, 26, 1, 5),
    _W2kStatusNetInPktValue_Type()
)
w2kStatusNetInPktValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusNetInPktValue.setStatus("mandatory")
_W2kStatusNetInPktWarn_Type = Integer32
_W2kStatusNetInPktWarn_Object = MibTableColumn
w2kStatusNetInPktWarn = _W2kStatusNetInPktWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 15, 26, 1, 6),
    _W2kStatusNetInPktWarn_Type()
)
w2kStatusNetInPktWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusNetInPktWarn.setStatus("mandatory")
_W2kStatusNetInPktCrit_Type = Integer32
_W2kStatusNetInPktCrit_Object = MibTableColumn
w2kStatusNetInPktCrit = _W2kStatusNetInPktCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 15, 26, 1, 7),
    _W2kStatusNetInPktCrit_Type()
)
w2kStatusNetInPktCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusNetInPktCrit.setStatus("mandatory")


class _W2kStatusNetInPktMonitor_Type(Integer32):
    """Custom type w2kStatusNetInPktMonitor based on Integer32"""
    defaultValue = 0

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
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_W2kStatusNetInPktMonitor_Type.__name__ = "Integer32"
_W2kStatusNetInPktMonitor_Object = MibTableColumn
w2kStatusNetInPktMonitor = _W2kStatusNetInPktMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 15, 26, 1, 8),
    _W2kStatusNetInPktMonitor_Type()
)
w2kStatusNetInPktMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusNetInPktMonitor.setStatus("mandatory")


class _W2kStatusNetInPktStatus_Type(Integer32):
    """Custom type w2kStatusNetInPktStatus based on Integer32"""
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
        *(("critical", 4),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_W2kStatusNetInPktStatus_Type.__name__ = "Integer32"
_W2kStatusNetInPktStatus_Object = MibTableColumn
w2kStatusNetInPktStatus = _W2kStatusNetInPktStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 15, 26, 1, 9),
    _W2kStatusNetInPktStatus_Type()
)
w2kStatusNetInPktStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusNetInPktStatus.setStatus("mandatory")
_W2kStatusNetOutPktValue_Type = Integer32
_W2kStatusNetOutPktValue_Object = MibTableColumn
w2kStatusNetOutPktValue = _W2kStatusNetOutPktValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 15, 26, 1, 10),
    _W2kStatusNetOutPktValue_Type()
)
w2kStatusNetOutPktValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusNetOutPktValue.setStatus("mandatory")
_W2kStatusNetOutPktWarn_Type = Integer32
_W2kStatusNetOutPktWarn_Object = MibTableColumn
w2kStatusNetOutPktWarn = _W2kStatusNetOutPktWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 15, 26, 1, 11),
    _W2kStatusNetOutPktWarn_Type()
)
w2kStatusNetOutPktWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusNetOutPktWarn.setStatus("mandatory")
_W2kStatusNetOutPktCrit_Type = Integer32
_W2kStatusNetOutPktCrit_Object = MibTableColumn
w2kStatusNetOutPktCrit = _W2kStatusNetOutPktCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 15, 26, 1, 12),
    _W2kStatusNetOutPktCrit_Type()
)
w2kStatusNetOutPktCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusNetOutPktCrit.setStatus("mandatory")


class _W2kStatusNetOutPktMonitor_Type(Integer32):
    """Custom type w2kStatusNetOutPktMonitor based on Integer32"""
    defaultValue = 0

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
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_W2kStatusNetOutPktMonitor_Type.__name__ = "Integer32"
_W2kStatusNetOutPktMonitor_Object = MibTableColumn
w2kStatusNetOutPktMonitor = _W2kStatusNetOutPktMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 15, 26, 1, 13),
    _W2kStatusNetOutPktMonitor_Type()
)
w2kStatusNetOutPktMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusNetOutPktMonitor.setStatus("mandatory")


class _W2kStatusNetOutPktStatus_Type(Integer32):
    """Custom type w2kStatusNetOutPktStatus based on Integer32"""
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
        *(("critical", 4),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_W2kStatusNetOutPktStatus_Type.__name__ = "Integer32"
_W2kStatusNetOutPktStatus_Object = MibTableColumn
w2kStatusNetOutPktStatus = _W2kStatusNetOutPktStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 15, 26, 1, 14),
    _W2kStatusNetOutPktStatus_Type()
)
w2kStatusNetOutPktStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusNetOutPktStatus.setStatus("mandatory")
_W2kStatusNetInErrDValue_Type = Integer32
_W2kStatusNetInErrDValue_Object = MibTableColumn
w2kStatusNetInErrDValue = _W2kStatusNetInErrDValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 15, 26, 1, 15),
    _W2kStatusNetInErrDValue_Type()
)
w2kStatusNetInErrDValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusNetInErrDValue.setStatus("mandatory")
_W2kStatusNetInErrDWarn_Type = Integer32
_W2kStatusNetInErrDWarn_Object = MibTableColumn
w2kStatusNetInErrDWarn = _W2kStatusNetInErrDWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 15, 26, 1, 16),
    _W2kStatusNetInErrDWarn_Type()
)
w2kStatusNetInErrDWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusNetInErrDWarn.setStatus("mandatory")
_W2kStatusNetInErrDCrit_Type = Integer32
_W2kStatusNetInErrDCrit_Object = MibTableColumn
w2kStatusNetInErrDCrit = _W2kStatusNetInErrDCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 15, 26, 1, 17),
    _W2kStatusNetInErrDCrit_Type()
)
w2kStatusNetInErrDCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusNetInErrDCrit.setStatus("mandatory")


class _W2kStatusNetInErrDMonitor_Type(Integer32):
    """Custom type w2kStatusNetInErrDMonitor based on Integer32"""
    defaultValue = 0

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
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_W2kStatusNetInErrDMonitor_Type.__name__ = "Integer32"
_W2kStatusNetInErrDMonitor_Object = MibTableColumn
w2kStatusNetInErrDMonitor = _W2kStatusNetInErrDMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 15, 26, 1, 18),
    _W2kStatusNetInErrDMonitor_Type()
)
w2kStatusNetInErrDMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusNetInErrDMonitor.setStatus("mandatory")


class _W2kStatusNetInErrDStatus_Type(Integer32):
    """Custom type w2kStatusNetInErrDStatus based on Integer32"""
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
        *(("critical", 4),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_W2kStatusNetInErrDStatus_Type.__name__ = "Integer32"
_W2kStatusNetInErrDStatus_Object = MibTableColumn
w2kStatusNetInErrDStatus = _W2kStatusNetInErrDStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 15, 26, 1, 19),
    _W2kStatusNetInErrDStatus_Type()
)
w2kStatusNetInErrDStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusNetInErrDStatus.setStatus("mandatory")
_W2kStatusNetOutErrDValue_Type = Integer32
_W2kStatusNetOutErrDValue_Object = MibTableColumn
w2kStatusNetOutErrDValue = _W2kStatusNetOutErrDValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 15, 26, 1, 20),
    _W2kStatusNetOutErrDValue_Type()
)
w2kStatusNetOutErrDValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusNetOutErrDValue.setStatus("mandatory")
_W2kStatusNetOutErrDWarn_Type = Integer32
_W2kStatusNetOutErrDWarn_Object = MibTableColumn
w2kStatusNetOutErrDWarn = _W2kStatusNetOutErrDWarn_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 15, 26, 1, 21),
    _W2kStatusNetOutErrDWarn_Type()
)
w2kStatusNetOutErrDWarn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusNetOutErrDWarn.setStatus("mandatory")
_W2kStatusNetOutErrDCrit_Type = Integer32
_W2kStatusNetOutErrDCrit_Object = MibTableColumn
w2kStatusNetOutErrDCrit = _W2kStatusNetOutErrDCrit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 15, 26, 1, 22),
    _W2kStatusNetOutErrDCrit_Type()
)
w2kStatusNetOutErrDCrit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusNetOutErrDCrit.setStatus("mandatory")


class _W2kStatusNetOutErrDMonitor_Type(Integer32):
    """Custom type w2kStatusNetOutErrDMonitor based on Integer32"""
    defaultValue = 0

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
        *(("both", 4),
          ("critical-only", 3),
          ("do-not-monitor", 1),
          ("warning-only", 2))
    )


_W2kStatusNetOutErrDMonitor_Type.__name__ = "Integer32"
_W2kStatusNetOutErrDMonitor_Object = MibTableColumn
w2kStatusNetOutErrDMonitor = _W2kStatusNetOutErrDMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 15, 26, 1, 23),
    _W2kStatusNetOutErrDMonitor_Type()
)
w2kStatusNetOutErrDMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusNetOutErrDMonitor.setStatus("mandatory")


class _W2kStatusNetOutErrDStatus_Type(Integer32):
    """Custom type w2kStatusNetOutErrDStatus based on Integer32"""
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
        *(("critical", 4),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_W2kStatusNetOutErrDStatus_Type.__name__ = "Integer32"
_W2kStatusNetOutErrDStatus_Object = MibTableColumn
w2kStatusNetOutErrDStatus = _W2kStatusNetOutErrDStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 15, 26, 1, 24),
    _W2kStatusNetOutErrDStatus_Type()
)
w2kStatusNetOutErrDStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusNetOutErrDStatus.setStatus("mandatory")


class _W2kStatusNetLossAction_Type(Integer32):
    """Custom type w2kStatusNetLossAction based on Integer32"""
    defaultValue = 0

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
        *(("down-critical", 4),
          ("down-warning", 3),
          ("remove", 1),
          ("up", 2))
    )


_W2kStatusNetLossAction_Type.__name__ = "Integer32"
_W2kStatusNetLossAction_Object = MibTableColumn
w2kStatusNetLossAction = _W2kStatusNetLossAction_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 15, 26, 1, 25),
    _W2kStatusNetLossAction_Type()
)
w2kStatusNetLossAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusNetLossAction.setStatus("mandatory")


class _W2kStatusNetLossStatus_Type(Integer32):
    """Custom type w2kStatusNetLossStatus based on Integer32"""
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
        *(("down-critical", 4),
          ("down-warning", 3),
          ("unknown", 1),
          ("up", 2))
    )


_W2kStatusNetLossStatus_Type.__name__ = "Integer32"
_W2kStatusNetLossStatus_Object = MibTableColumn
w2kStatusNetLossStatus = _W2kStatusNetLossStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 15, 26, 1, 26),
    _W2kStatusNetLossStatus_Type()
)
w2kStatusNetLossStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusNetLossStatus.setStatus("mandatory")
_W2kStatusNetCallBackRef_Type = DisplayString
_W2kStatusNetCallBackRef_Object = MibTableColumn
w2kStatusNetCallBackRef = _W2kStatusNetCallBackRef_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 15, 26, 1, 27),
    _W2kStatusNetCallBackRef_Type()
)
w2kStatusNetCallBackRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusNetCallBackRef.setStatus("mandatory")
_W2kStatusRegGroup_ObjectIdentity = ObjectIdentity
w2kStatusRegGroup = _W2kStatusRegGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 16)
)
_W2kStatusRegCount_Type = Integer32
_W2kStatusRegCount_Object = MibScalar
w2kStatusRegCount = _W2kStatusRegCount_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 16, 1),
    _W2kStatusRegCount_Type()
)
w2kStatusRegCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusRegCount.setStatus("mandatory")
_W2kStatusRegTable_Object = MibTable
w2kStatusRegTable = _W2kStatusRegTable_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 16, 2)
)
if mibBuilder.loadTexts:
    w2kStatusRegTable.setStatus("mandatory")
_W2kStatusRegEntry_Object = MibTableRow
w2kStatusRegEntry = _W2kStatusRegEntry_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 16, 2, 1)
)
w2kStatusRegEntry.setIndexNames(
    (0, "CA-W2KOS-MIB", "w2kStatusRegName"),
)
if mibBuilder.loadTexts:
    w2kStatusRegEntry.setStatus("mandatory")
_W2kStatusRegName_Type = DisplayString
_W2kStatusRegName_Object = MibTableColumn
w2kStatusRegName = _W2kStatusRegName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 16, 2, 1, 1),
    _W2kStatusRegName_Type()
)
w2kStatusRegName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusRegName.setStatus("mandatory")
_W2kStatusRegDescription_Type = DisplayString
_W2kStatusRegDescription_Object = MibTableColumn
w2kStatusRegDescription = _W2kStatusRegDescription_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 16, 2, 1, 2),
    _W2kStatusRegDescription_Type()
)
w2kStatusRegDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusRegDescription.setStatus("mandatory")
_W2kStatusRegAggLagValue_Type = Integer32
_W2kStatusRegAggLagValue_Object = MibTableColumn
w2kStatusRegAggLagValue = _W2kStatusRegAggLagValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 16, 2, 1, 3),
    _W2kStatusRegAggLagValue_Type()
)
w2kStatusRegAggLagValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusRegAggLagValue.setStatus("mandatory")
_W2kStatusRegAggLag_Type = Integer32
_W2kStatusRegAggLag_Object = MibTableColumn
w2kStatusRegAggLag = _W2kStatusRegAggLag_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 16, 2, 1, 4),
    _W2kStatusRegAggLag_Type()
)
w2kStatusRegAggLag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusRegAggLag.setStatus("mandatory")


class _W2kStatusRegAggStatus_Type(Integer32):
    """Custom type w2kStatusRegAggStatus based on Integer32"""
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
        *(("critical", 4),
          ("ok", 2),
          ("unknown", 1),
          ("warning", 3))
    )


_W2kStatusRegAggStatus_Type.__name__ = "Integer32"
_W2kStatusRegAggStatus_Object = MibTableColumn
w2kStatusRegAggStatus = _W2kStatusRegAggStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 16, 2, 1, 5),
    _W2kStatusRegAggStatus_Type()
)
w2kStatusRegAggStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusRegAggStatus.setStatus("mandatory")


class _W2kStatusRegExist_Type(Integer32):
    """Custom type w2kStatusRegExist based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("should-exist", 1),
          ("should-not-exist", 2))
    )


_W2kStatusRegExist_Type.__name__ = "Integer32"
_W2kStatusRegExist_Object = MibTableColumn
w2kStatusRegExist = _W2kStatusRegExist_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 16, 2, 1, 6),
    _W2kStatusRegExist_Type()
)
w2kStatusRegExist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusRegExist.setStatus("mandatory")


class _W2kStatusRegExistMonitor_Type(Integer32):
    """Custom type w2kStatusRegExistMonitor based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("do-not-monitor", 1),
          ("down-critical", 3),
          ("down-warning", 2))
    )


_W2kStatusRegExistMonitor_Type.__name__ = "Integer32"
_W2kStatusRegExistMonitor_Object = MibTableColumn
w2kStatusRegExistMonitor = _W2kStatusRegExistMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 16, 2, 1, 7),
    _W2kStatusRegExistMonitor_Type()
)
w2kStatusRegExistMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusRegExistMonitor.setStatus("mandatory")


class _W2kStatusRegExistStatus_Type(Integer32):
    """Custom type w2kStatusRegExistStatus based on Integer32"""
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
        *(("down-critical", 4),
          ("down-warning", 3),
          ("unknown", 1),
          ("up", 2))
    )


_W2kStatusRegExistStatus_Type.__name__ = "Integer32"
_W2kStatusRegExistStatus_Object = MibTableColumn
w2kStatusRegExistStatus = _W2kStatusRegExistStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 16, 2, 1, 8),
    _W2kStatusRegExistStatus_Type()
)
w2kStatusRegExistStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusRegExistStatus.setStatus("mandatory")
_W2kStatusRegValueValue_Type = DisplayString
_W2kStatusRegValueValue_Object = MibTableColumn
w2kStatusRegValueValue = _W2kStatusRegValueValue_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 16, 2, 1, 9),
    _W2kStatusRegValueValue_Type()
)
w2kStatusRegValueValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusRegValueValue.setStatus("mandatory")


class _W2kStatusRegValueType_Type(Integer32):
    """Custom type w2kStatusRegValueType based on Integer32"""
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
        *(("binary", 2),
          ("dword", 3),
          ("string", 1),
          ("unknown", 4))
    )


_W2kStatusRegValueType_Type.__name__ = "Integer32"
_W2kStatusRegValueType_Object = MibTableColumn
w2kStatusRegValueType = _W2kStatusRegValueType_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 16, 2, 1, 10),
    _W2kStatusRegValueType_Type()
)
w2kStatusRegValueType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusRegValueType.setStatus("mandatory")
_W2kStatusRegValueRef_Type = DisplayString
_W2kStatusRegValueRef_Object = MibTableColumn
w2kStatusRegValueRef = _W2kStatusRegValueRef_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 16, 2, 1, 11),
    _W2kStatusRegValueRef_Type()
)
w2kStatusRegValueRef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusRegValueRef.setStatus("mandatory")


class _W2kStatusRegValueCond_Type(Integer32):
    """Custom type w2kStatusRegValueCond based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("should-be-above", 4),
          ("should-be-below", 3),
          ("should-be-equal", 1),
          ("should-not-be-equal", 2),
          ("should-not-change", 5))
    )


_W2kStatusRegValueCond_Type.__name__ = "Integer32"
_W2kStatusRegValueCond_Object = MibTableColumn
w2kStatusRegValueCond = _W2kStatusRegValueCond_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 16, 2, 1, 12),
    _W2kStatusRegValueCond_Type()
)
w2kStatusRegValueCond.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusRegValueCond.setStatus("mandatory")


class _W2kStatusRegValueMonitor_Type(Integer32):
    """Custom type w2kStatusRegValueMonitor based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("do-not-monitor", 1),
          ("down-critical", 3),
          ("down-warning", 2))
    )


_W2kStatusRegValueMonitor_Type.__name__ = "Integer32"
_W2kStatusRegValueMonitor_Object = MibTableColumn
w2kStatusRegValueMonitor = _W2kStatusRegValueMonitor_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 16, 2, 1, 13),
    _W2kStatusRegValueMonitor_Type()
)
w2kStatusRegValueMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusRegValueMonitor.setStatus("mandatory")


class _W2kStatusRegValueStatus_Type(Integer32):
    """Custom type w2kStatusRegValueStatus based on Integer32"""
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
        *(("down-critical", 4),
          ("down-warning", 3),
          ("unknown", 1),
          ("up", 2))
    )


_W2kStatusRegValueStatus_Type.__name__ = "Integer32"
_W2kStatusRegValueStatus_Object = MibTableColumn
w2kStatusRegValueStatus = _W2kStatusRegValueStatus_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 16, 2, 1, 14),
    _W2kStatusRegValueStatus_Type()
)
w2kStatusRegValueStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusRegValueStatus.setStatus("mandatory")
_W2kStatusRegCallBackRef_Type = DisplayString
_W2kStatusRegCallBackRef_Object = MibTableColumn
w2kStatusRegCallBackRef = _W2kStatusRegCallBackRef_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 16, 2, 1, 15),
    _W2kStatusRegCallBackRef_Type()
)
w2kStatusRegCallBackRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kStatusRegCallBackRef.setStatus("mandatory")


class _W2kStatusRegButton_Type(Integer32):
    """Custom type w2kStatusRegButton based on Integer32"""
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
          ("remove", 2),
          ("reset-value", 3))
    )


_W2kStatusRegButton_Type.__name__ = "Integer32"
_W2kStatusRegButton_Object = MibTableColumn
w2kStatusRegButton = _W2kStatusRegButton_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 2, 16, 2, 1, 16),
    _W2kStatusRegButton_Type()
)
w2kStatusRegButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kStatusRegButton.setStatus("mandatory")
_W2kAvailableGroup_ObjectIdentity = ObjectIdentity
w2kAvailableGroup = _W2kAvailableGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 3)
)
_W2kAvailLVolGroup_ObjectIdentity = ObjectIdentity
w2kAvailLVolGroup = _W2kAvailLVolGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 3, 1)
)


class _W2kAvailLVolRefresh_Type(Integer32):
    """Custom type w2kAvailLVolRefresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("refresh", 2))
    )


_W2kAvailLVolRefresh_Type.__name__ = "Integer32"
_W2kAvailLVolRefresh_Object = MibScalar
w2kAvailLVolRefresh = _W2kAvailLVolRefresh_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 3, 1, 1),
    _W2kAvailLVolRefresh_Type()
)
w2kAvailLVolRefresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kAvailLVolRefresh.setStatus("mandatory")
_W2kAvailLVolCount_Type = Integer32
_W2kAvailLVolCount_Object = MibScalar
w2kAvailLVolCount = _W2kAvailLVolCount_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 3, 1, 2),
    _W2kAvailLVolCount_Type()
)
w2kAvailLVolCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kAvailLVolCount.setStatus("mandatory")
_W2kAvailLVolTable_Object = MibTable
w2kAvailLVolTable = _W2kAvailLVolTable_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 3, 1, 3)
)
if mibBuilder.loadTexts:
    w2kAvailLVolTable.setStatus("mandatory")
_W2kAvailLVolEntry_Object = MibTableRow
w2kAvailLVolEntry = _W2kAvailLVolEntry_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 3, 1, 3, 1)
)
w2kAvailLVolEntry.setIndexNames(
    (0, "CA-W2KOS-MIB", "w2kAvailLVolName"),
)
if mibBuilder.loadTexts:
    w2kAvailLVolEntry.setStatus("mandatory")
_W2kAvailLVolName_Type = DisplayString
_W2kAvailLVolName_Object = MibTableColumn
w2kAvailLVolName = _W2kAvailLVolName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 3, 1, 3, 1, 1),
    _W2kAvailLVolName_Type()
)
w2kAvailLVolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kAvailLVolName.setStatus("mandatory")
_W2kAvailLVolMounts_Type = DisplayString
_W2kAvailLVolMounts_Object = MibTableColumn
w2kAvailLVolMounts = _W2kAvailLVolMounts_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 3, 1, 3, 1, 2),
    _W2kAvailLVolMounts_Type()
)
w2kAvailLVolMounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kAvailLVolMounts.setStatus("mandatory")
_W2kAvailLVolInfo_Type = DisplayString
_W2kAvailLVolInfo_Object = MibTableColumn
w2kAvailLVolInfo = _W2kAvailLVolInfo_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 3, 1, 3, 1, 3),
    _W2kAvailLVolInfo_Type()
)
w2kAvailLVolInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kAvailLVolInfo.setStatus("mandatory")
_W2kAvailLVolTime_Type = DisplayString
_W2kAvailLVolTime_Object = MibTableColumn
w2kAvailLVolTime = _W2kAvailLVolTime_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 3, 1, 3, 1, 4),
    _W2kAvailLVolTime_Type()
)
w2kAvailLVolTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kAvailLVolTime.setStatus("mandatory")
_W2kAvailMntGroup_ObjectIdentity = ObjectIdentity
w2kAvailMntGroup = _W2kAvailMntGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 3, 2)
)


class _W2kAvailMntRefresh_Type(Integer32):
    """Custom type w2kAvailMntRefresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("refresh", 2))
    )


_W2kAvailMntRefresh_Type.__name__ = "Integer32"
_W2kAvailMntRefresh_Object = MibScalar
w2kAvailMntRefresh = _W2kAvailMntRefresh_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 3, 2, 1),
    _W2kAvailMntRefresh_Type()
)
w2kAvailMntRefresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kAvailMntRefresh.setStatus("mandatory")
_W2kAvailMntCount_Type = Integer32
_W2kAvailMntCount_Object = MibScalar
w2kAvailMntCount = _W2kAvailMntCount_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 3, 2, 2),
    _W2kAvailMntCount_Type()
)
w2kAvailMntCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kAvailMntCount.setStatus("mandatory")
_W2kAvailMntTable_Object = MibTable
w2kAvailMntTable = _W2kAvailMntTable_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 3, 2, 3)
)
if mibBuilder.loadTexts:
    w2kAvailMntTable.setStatus("mandatory")
_W2kAvailMntEntry_Object = MibTableRow
w2kAvailMntEntry = _W2kAvailMntEntry_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 3, 2, 3, 1)
)
w2kAvailMntEntry.setIndexNames(
    (0, "CA-W2KOS-MIB", "w2kAvailMntName"),
)
if mibBuilder.loadTexts:
    w2kAvailMntEntry.setStatus("mandatory")
_W2kAvailMntName_Type = DisplayString
_W2kAvailMntName_Object = MibTableColumn
w2kAvailMntName = _W2kAvailMntName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 3, 2, 3, 1, 1),
    _W2kAvailMntName_Type()
)
w2kAvailMntName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kAvailMntName.setStatus("mandatory")
_W2kAvailMntRelTo_Type = DisplayString
_W2kAvailMntRelTo_Object = MibTableColumn
w2kAvailMntRelTo = _W2kAvailMntRelTo_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 3, 2, 3, 1, 2),
    _W2kAvailMntRelTo_Type()
)
w2kAvailMntRelTo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kAvailMntRelTo.setStatus("mandatory")
_W2kAvailMntTime_Type = DisplayString
_W2kAvailMntTime_Object = MibTableColumn
w2kAvailMntTime = _W2kAvailMntTime_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 3, 2, 3, 1, 3),
    _W2kAvailMntTime_Type()
)
w2kAvailMntTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kAvailMntTime.setStatus("mandatory")
_W2kAvailDfsGroup_ObjectIdentity = ObjectIdentity
w2kAvailDfsGroup = _W2kAvailDfsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 3, 3)
)


class _W2kAvailDfsRefresh_Type(Integer32):
    """Custom type w2kAvailDfsRefresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("refresh", 2))
    )


_W2kAvailDfsRefresh_Type.__name__ = "Integer32"
_W2kAvailDfsRefresh_Object = MibScalar
w2kAvailDfsRefresh = _W2kAvailDfsRefresh_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 3, 3, 1),
    _W2kAvailDfsRefresh_Type()
)
w2kAvailDfsRefresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kAvailDfsRefresh.setStatus("mandatory")
_W2kAvailDfsCount_Type = Integer32
_W2kAvailDfsCount_Object = MibScalar
w2kAvailDfsCount = _W2kAvailDfsCount_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 3, 3, 2),
    _W2kAvailDfsCount_Type()
)
w2kAvailDfsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kAvailDfsCount.setStatus("mandatory")
_W2kAvailDfsTable_Object = MibTable
w2kAvailDfsTable = _W2kAvailDfsTable_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 3, 3, 3)
)
if mibBuilder.loadTexts:
    w2kAvailDfsTable.setStatus("mandatory")
_W2kAvailDfsEntry_Object = MibTableRow
w2kAvailDfsEntry = _W2kAvailDfsEntry_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 3, 3, 3, 1)
)
w2kAvailDfsEntry.setIndexNames(
    (0, "CA-W2KOS-MIB", "w2kAvailDfsName"),
)
if mibBuilder.loadTexts:
    w2kAvailDfsEntry.setStatus("mandatory")
_W2kAvailDfsName_Type = DisplayString
_W2kAvailDfsName_Object = MibTableColumn
w2kAvailDfsName = _W2kAvailDfsName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 3, 3, 3, 1, 1),
    _W2kAvailDfsName_Type()
)
w2kAvailDfsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kAvailDfsName.setStatus("mandatory")
_W2kAvailDfsTime_Type = DisplayString
_W2kAvailDfsTime_Object = MibTableColumn
w2kAvailDfsTime = _W2kAvailDfsTime_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 3, 3, 3, 1, 2),
    _W2kAvailDfsTime_Type()
)
w2kAvailDfsTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kAvailDfsTime.setStatus("mandatory")
_W2kAvailQuotGroup_ObjectIdentity = ObjectIdentity
w2kAvailQuotGroup = _W2kAvailQuotGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 3, 4)
)


class _W2kAvailQuotRefresh_Type(Integer32):
    """Custom type w2kAvailQuotRefresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("refresh", 2))
    )


_W2kAvailQuotRefresh_Type.__name__ = "Integer32"
_W2kAvailQuotRefresh_Object = MibScalar
w2kAvailQuotRefresh = _W2kAvailQuotRefresh_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 3, 4, 1),
    _W2kAvailQuotRefresh_Type()
)
w2kAvailQuotRefresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kAvailQuotRefresh.setStatus("mandatory")
_W2kAvailQuotCount_Type = Integer32
_W2kAvailQuotCount_Object = MibScalar
w2kAvailQuotCount = _W2kAvailQuotCount_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 3, 4, 2),
    _W2kAvailQuotCount_Type()
)
w2kAvailQuotCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kAvailQuotCount.setStatus("mandatory")
_W2kAvailQuotTable_Object = MibTable
w2kAvailQuotTable = _W2kAvailQuotTable_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 3, 4, 3)
)
if mibBuilder.loadTexts:
    w2kAvailQuotTable.setStatus("mandatory")
_W2kAvailQuotEntry_Object = MibTableRow
w2kAvailQuotEntry = _W2kAvailQuotEntry_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 3, 4, 3, 1)
)
w2kAvailQuotEntry.setIndexNames(
    (0, "CA-W2KOS-MIB", "w2kAvailQuotLVolName"),
    (0, "CA-W2KOS-MIB", "w2kAvailQuotUserName"),
)
if mibBuilder.loadTexts:
    w2kAvailQuotEntry.setStatus("mandatory")
_W2kAvailQuotLVolName_Type = DisplayString
_W2kAvailQuotLVolName_Object = MibTableColumn
w2kAvailQuotLVolName = _W2kAvailQuotLVolName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 3, 4, 3, 1, 1),
    _W2kAvailQuotLVolName_Type()
)
w2kAvailQuotLVolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kAvailQuotLVolName.setStatus("mandatory")
_W2kAvailQuotUserName_Type = DisplayString
_W2kAvailQuotUserName_Object = MibTableColumn
w2kAvailQuotUserName = _W2kAvailQuotUserName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 3, 4, 3, 1, 2),
    _W2kAvailQuotUserName_Type()
)
w2kAvailQuotUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kAvailQuotUserName.setStatus("mandatory")
_W2kAvailQuotWarnLevel_Type = Integer32
_W2kAvailQuotWarnLevel_Object = MibTableColumn
w2kAvailQuotWarnLevel = _W2kAvailQuotWarnLevel_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 3, 4, 3, 1, 3),
    _W2kAvailQuotWarnLevel_Type()
)
w2kAvailQuotWarnLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kAvailQuotWarnLevel.setStatus("mandatory")
_W2kAvailQuotLimit_Type = Integer32
_W2kAvailQuotLimit_Object = MibTableColumn
w2kAvailQuotLimit = _W2kAvailQuotLimit_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 3, 4, 3, 1, 4),
    _W2kAvailQuotLimit_Type()
)
w2kAvailQuotLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kAvailQuotLimit.setStatus("mandatory")
_W2kAvailQuotTime_Type = DisplayString
_W2kAvailQuotTime_Object = MibTableColumn
w2kAvailQuotTime = _W2kAvailQuotTime_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 3, 4, 3, 1, 5),
    _W2kAvailQuotTime_Type()
)
w2kAvailQuotTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kAvailQuotTime.setStatus("mandatory")
_W2kAvailProcGroup_ObjectIdentity = ObjectIdentity
w2kAvailProcGroup = _W2kAvailProcGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 3, 5)
)


class _W2kAvailProcRefresh_Type(Integer32):
    """Custom type w2kAvailProcRefresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("refresh", 2))
    )


_W2kAvailProcRefresh_Type.__name__ = "Integer32"
_W2kAvailProcRefresh_Object = MibScalar
w2kAvailProcRefresh = _W2kAvailProcRefresh_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 3, 5, 1),
    _W2kAvailProcRefresh_Type()
)
w2kAvailProcRefresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kAvailProcRefresh.setStatus("mandatory")
_W2kAvailProcCount_Type = Integer32
_W2kAvailProcCount_Object = MibScalar
w2kAvailProcCount = _W2kAvailProcCount_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 3, 5, 2),
    _W2kAvailProcCount_Type()
)
w2kAvailProcCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kAvailProcCount.setStatus("mandatory")
_W2kAvailProcTable_Object = MibTable
w2kAvailProcTable = _W2kAvailProcTable_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 3, 5, 3)
)
if mibBuilder.loadTexts:
    w2kAvailProcTable.setStatus("mandatory")
_W2kAvailProcEntry_Object = MibTableRow
w2kAvailProcEntry = _W2kAvailProcEntry_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 3, 5, 3, 1)
)
w2kAvailProcEntry.setIndexNames(
    (0, "CA-W2KOS-MIB", "w2kAvailProcProcName"),
    (0, "CA-W2KOS-MIB", "w2kAvailProcPathName"),
    (0, "CA-W2KOS-MIB", "w2kAvailProcUserName"),
)
if mibBuilder.loadTexts:
    w2kAvailProcEntry.setStatus("mandatory")
_W2kAvailProcProcName_Type = DisplayString
_W2kAvailProcProcName_Object = MibTableColumn
w2kAvailProcProcName = _W2kAvailProcProcName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 3, 5, 3, 1, 1),
    _W2kAvailProcProcName_Type()
)
w2kAvailProcProcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kAvailProcProcName.setStatus("mandatory")
_W2kAvailProcPathName_Type = DisplayString
_W2kAvailProcPathName_Object = MibTableColumn
w2kAvailProcPathName = _W2kAvailProcPathName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 3, 5, 3, 1, 2),
    _W2kAvailProcPathName_Type()
)
w2kAvailProcPathName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kAvailProcPathName.setStatus("mandatory")
_W2kAvailProcUserName_Type = DisplayString
_W2kAvailProcUserName_Object = MibTableColumn
w2kAvailProcUserName = _W2kAvailProcUserName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 3, 5, 3, 1, 3),
    _W2kAvailProcUserName_Type()
)
w2kAvailProcUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kAvailProcUserName.setStatus("mandatory")
_W2kAvailProcTime_Type = DisplayString
_W2kAvailProcTime_Object = MibTableColumn
w2kAvailProcTime = _W2kAvailProcTime_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 3, 5, 3, 1, 4),
    _W2kAvailProcTime_Type()
)
w2kAvailProcTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kAvailProcTime.setStatus("mandatory")
_W2kAvailSrvcGroup_ObjectIdentity = ObjectIdentity
w2kAvailSrvcGroup = _W2kAvailSrvcGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 3, 6)
)


class _W2kAvailSrvcRefresh_Type(Integer32):
    """Custom type w2kAvailSrvcRefresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("refresh", 2))
    )


_W2kAvailSrvcRefresh_Type.__name__ = "Integer32"
_W2kAvailSrvcRefresh_Object = MibScalar
w2kAvailSrvcRefresh = _W2kAvailSrvcRefresh_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 3, 6, 1),
    _W2kAvailSrvcRefresh_Type()
)
w2kAvailSrvcRefresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kAvailSrvcRefresh.setStatus("mandatory")
_W2kAvailSrvcCount_Type = Integer32
_W2kAvailSrvcCount_Object = MibScalar
w2kAvailSrvcCount = _W2kAvailSrvcCount_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 3, 6, 2),
    _W2kAvailSrvcCount_Type()
)
w2kAvailSrvcCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kAvailSrvcCount.setStatus("mandatory")
_W2kAvailSrvcTable_Object = MibTable
w2kAvailSrvcTable = _W2kAvailSrvcTable_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 3, 6, 3)
)
if mibBuilder.loadTexts:
    w2kAvailSrvcTable.setStatus("mandatory")
_W2kAvailSrvcEntry_Object = MibTableRow
w2kAvailSrvcEntry = _W2kAvailSrvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 3, 6, 3, 1)
)
w2kAvailSrvcEntry.setIndexNames(
    (0, "CA-W2KOS-MIB", "w2kAvailSrvcName"),
)
if mibBuilder.loadTexts:
    w2kAvailSrvcEntry.setStatus("mandatory")
_W2kAvailSrvcName_Type = DisplayString
_W2kAvailSrvcName_Object = MibTableColumn
w2kAvailSrvcName = _W2kAvailSrvcName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 3, 6, 3, 1, 1),
    _W2kAvailSrvcName_Type()
)
w2kAvailSrvcName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kAvailSrvcName.setStatus("mandatory")
_W2kAvailSrvcDescr_Type = DisplayString
_W2kAvailSrvcDescr_Object = MibTableColumn
w2kAvailSrvcDescr = _W2kAvailSrvcDescr_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 3, 6, 3, 1, 2),
    _W2kAvailSrvcDescr_Type()
)
w2kAvailSrvcDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kAvailSrvcDescr.setStatus("mandatory")
_W2kAvailSrvcTime_Type = DisplayString
_W2kAvailSrvcTime_Object = MibTableColumn
w2kAvailSrvcTime = _W2kAvailSrvcTime_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 3, 6, 3, 1, 3),
    _W2kAvailSrvcTime_Type()
)
w2kAvailSrvcTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kAvailSrvcTime.setStatus("mandatory")
_W2kAvailJobGroup_ObjectIdentity = ObjectIdentity
w2kAvailJobGroup = _W2kAvailJobGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 3, 7)
)


class _W2kAvailJobRefresh_Type(Integer32):
    """Custom type w2kAvailJobRefresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("refresh", 2))
    )


_W2kAvailJobRefresh_Type.__name__ = "Integer32"
_W2kAvailJobRefresh_Object = MibScalar
w2kAvailJobRefresh = _W2kAvailJobRefresh_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 3, 7, 1),
    _W2kAvailJobRefresh_Type()
)
w2kAvailJobRefresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kAvailJobRefresh.setStatus("mandatory")
_W2kAvailJobCount_Type = Integer32
_W2kAvailJobCount_Object = MibScalar
w2kAvailJobCount = _W2kAvailJobCount_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 3, 7, 2),
    _W2kAvailJobCount_Type()
)
w2kAvailJobCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kAvailJobCount.setStatus("mandatory")
_W2kAvailJobTable_Object = MibTable
w2kAvailJobTable = _W2kAvailJobTable_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 3, 7, 3)
)
if mibBuilder.loadTexts:
    w2kAvailJobTable.setStatus("mandatory")
_W2kAvailJobEntry_Object = MibTableRow
w2kAvailJobEntry = _W2kAvailJobEntry_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 3, 7, 3, 1)
)
w2kAvailJobEntry.setIndexNames(
    (0, "CA-W2KOS-MIB", "w2kAvailJobName"),
)
if mibBuilder.loadTexts:
    w2kAvailJobEntry.setStatus("mandatory")
_W2kAvailJobName_Type = DisplayString
_W2kAvailJobName_Object = MibTableColumn
w2kAvailJobName = _W2kAvailJobName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 3, 7, 3, 1, 1),
    _W2kAvailJobName_Type()
)
w2kAvailJobName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kAvailJobName.setStatus("mandatory")
_W2kAvailJobTime_Type = DisplayString
_W2kAvailJobTime_Object = MibTableColumn
w2kAvailJobTime = _W2kAvailJobTime_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 3, 7, 3, 1, 2),
    _W2kAvailJobTime_Type()
)
w2kAvailJobTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kAvailJobTime.setStatus("mandatory")
_W2kAvailSessGroup_ObjectIdentity = ObjectIdentity
w2kAvailSessGroup = _W2kAvailSessGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 3, 8)
)


class _W2kAvailSessRefresh_Type(Integer32):
    """Custom type w2kAvailSessRefresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("refresh", 2))
    )


_W2kAvailSessRefresh_Type.__name__ = "Integer32"
_W2kAvailSessRefresh_Object = MibScalar
w2kAvailSessRefresh = _W2kAvailSessRefresh_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 3, 8, 1),
    _W2kAvailSessRefresh_Type()
)
w2kAvailSessRefresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kAvailSessRefresh.setStatus("mandatory")
_W2kAvailSessCount_Type = Integer32
_W2kAvailSessCount_Object = MibScalar
w2kAvailSessCount = _W2kAvailSessCount_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 3, 8, 2),
    _W2kAvailSessCount_Type()
)
w2kAvailSessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kAvailSessCount.setStatus("mandatory")
_W2kAvailSessTable_Object = MibTable
w2kAvailSessTable = _W2kAvailSessTable_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 3, 8, 3)
)
if mibBuilder.loadTexts:
    w2kAvailSessTable.setStatus("mandatory")
_W2kAvailSessEntry_Object = MibTableRow
w2kAvailSessEntry = _W2kAvailSessEntry_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 3, 8, 3, 1)
)
w2kAvailSessEntry.setIndexNames(
    (0, "CA-W2KOS-MIB", "w2kAvailSessClientName"),
    (0, "CA-W2KOS-MIB", "w2kAvailSessUserName"),
)
if mibBuilder.loadTexts:
    w2kAvailSessEntry.setStatus("mandatory")
_W2kAvailSessClientName_Type = DisplayString
_W2kAvailSessClientName_Object = MibTableColumn
w2kAvailSessClientName = _W2kAvailSessClientName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 3, 8, 3, 1, 1),
    _W2kAvailSessClientName_Type()
)
w2kAvailSessClientName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kAvailSessClientName.setStatus("mandatory")
_W2kAvailSessUserName_Type = DisplayString
_W2kAvailSessUserName_Object = MibTableColumn
w2kAvailSessUserName = _W2kAvailSessUserName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 3, 8, 3, 1, 2),
    _W2kAvailSessUserName_Type()
)
w2kAvailSessUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kAvailSessUserName.setStatus("mandatory")
_W2kAvailSessTime_Type = DisplayString
_W2kAvailSessTime_Object = MibTableColumn
w2kAvailSessTime = _W2kAvailSessTime_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 3, 8, 3, 1, 3),
    _W2kAvailSessTime_Type()
)
w2kAvailSessTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kAvailSessTime.setStatus("mandatory")
_W2kAvailPrnGroup_ObjectIdentity = ObjectIdentity
w2kAvailPrnGroup = _W2kAvailPrnGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 3, 9)
)


class _W2kAvailPrnRefresh_Type(Integer32):
    """Custom type w2kAvailPrnRefresh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("refresh", 2))
    )


_W2kAvailPrnRefresh_Type.__name__ = "Integer32"
_W2kAvailPrnRefresh_Object = MibScalar
w2kAvailPrnRefresh = _W2kAvailPrnRefresh_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 3, 9, 1),
    _W2kAvailPrnRefresh_Type()
)
w2kAvailPrnRefresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kAvailPrnRefresh.setStatus("mandatory")
_W2kAvailPrnCount_Type = Integer32
_W2kAvailPrnCount_Object = MibScalar
w2kAvailPrnCount = _W2kAvailPrnCount_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 3, 9, 2),
    _W2kAvailPrnCount_Type()
)
w2kAvailPrnCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kAvailPrnCount.setStatus("mandatory")
_W2kAvailPrnTable_Object = MibTable
w2kAvailPrnTable = _W2kAvailPrnTable_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 3, 9, 3)
)
if mibBuilder.loadTexts:
    w2kAvailPrnTable.setStatus("mandatory")
_W2kAvailPrnEntry_Object = MibTableRow
w2kAvailPrnEntry = _W2kAvailPrnEntry_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 3, 9, 3, 1)
)
w2kAvailPrnEntry.setIndexNames(
    (0, "CA-W2KOS-MIB", "w2kAvailPrnName"),
)
if mibBuilder.loadTexts:
    w2kAvailPrnEntry.setStatus("mandatory")
_W2kAvailPrnName_Type = DisplayString
_W2kAvailPrnName_Object = MibTableColumn
w2kAvailPrnName = _W2kAvailPrnName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 3, 9, 3, 1, 1),
    _W2kAvailPrnName_Type()
)
w2kAvailPrnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kAvailPrnName.setStatus("mandatory")
_W2kAvailPrnTime_Type = DisplayString
_W2kAvailPrnTime_Object = MibTableColumn
w2kAvailPrnTime = _W2kAvailPrnTime_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 3, 9, 3, 1, 2),
    _W2kAvailPrnTime_Type()
)
w2kAvailPrnTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kAvailPrnTime.setStatus("mandatory")
_W2kHistoryGroup_ObjectIdentity = ObjectIdentity
w2kHistoryGroup = _W2kHistoryGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 4)
)


class _W2kHistoryCpuCollect_Type(Integer32):
    """Custom type w2kHistoryCpuCollect based on Integer32"""
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


_W2kHistoryCpuCollect_Type.__name__ = "Integer32"
_W2kHistoryCpuCollect_Object = MibScalar
w2kHistoryCpuCollect = _W2kHistoryCpuCollect_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 4, 1),
    _W2kHistoryCpuCollect_Type()
)
w2kHistoryCpuCollect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kHistoryCpuCollect.setStatus("mandatory")


class _W2kHistoryMemCollect_Type(Integer32):
    """Custom type w2kHistoryMemCollect based on Integer32"""
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


_W2kHistoryMemCollect_Type.__name__ = "Integer32"
_W2kHistoryMemCollect_Object = MibScalar
w2kHistoryMemCollect = _W2kHistoryMemCollect_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 4, 2),
    _W2kHistoryMemCollect_Type()
)
w2kHistoryMemCollect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kHistoryMemCollect.setStatus("mandatory")


class _W2kHistoryLVolCollect_Type(Integer32):
    """Custom type w2kHistoryLVolCollect based on Integer32"""
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


_W2kHistoryLVolCollect_Type.__name__ = "Integer32"
_W2kHistoryLVolCollect_Object = MibScalar
w2kHistoryLVolCollect = _W2kHistoryLVolCollect_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 4, 3),
    _W2kHistoryLVolCollect_Type()
)
w2kHistoryLVolCollect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kHistoryLVolCollect.setStatus("mandatory")


class _W2kHistoryMntCollect_Type(Integer32):
    """Custom type w2kHistoryMntCollect based on Integer32"""
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


_W2kHistoryMntCollect_Type.__name__ = "Integer32"
_W2kHistoryMntCollect_Object = MibScalar
w2kHistoryMntCollect = _W2kHistoryMntCollect_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 4, 4),
    _W2kHistoryMntCollect_Type()
)
w2kHistoryMntCollect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kHistoryMntCollect.setStatus("mandatory")


class _W2kHistoryDfsCollect_Type(Integer32):
    """Custom type w2kHistoryDfsCollect based on Integer32"""
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


_W2kHistoryDfsCollect_Type.__name__ = "Integer32"
_W2kHistoryDfsCollect_Object = MibScalar
w2kHistoryDfsCollect = _W2kHistoryDfsCollect_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 4, 5),
    _W2kHistoryDfsCollect_Type()
)
w2kHistoryDfsCollect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kHistoryDfsCollect.setStatus("mandatory")


class _W2kHistoryQuotCollect_Type(Integer32):
    """Custom type w2kHistoryQuotCollect based on Integer32"""
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


_W2kHistoryQuotCollect_Type.__name__ = "Integer32"
_W2kHistoryQuotCollect_Object = MibScalar
w2kHistoryQuotCollect = _W2kHistoryQuotCollect_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 4, 6),
    _W2kHistoryQuotCollect_Type()
)
w2kHistoryQuotCollect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kHistoryQuotCollect.setStatus("mandatory")


class _W2kHistoryDirCollect_Type(Integer32):
    """Custom type w2kHistoryDirCollect based on Integer32"""
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


_W2kHistoryDirCollect_Type.__name__ = "Integer32"
_W2kHistoryDirCollect_Object = MibScalar
w2kHistoryDirCollect = _W2kHistoryDirCollect_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 4, 7),
    _W2kHistoryDirCollect_Type()
)
w2kHistoryDirCollect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kHistoryDirCollect.setStatus("mandatory")


class _W2kHistoryFileCollect_Type(Integer32):
    """Custom type w2kHistoryFileCollect based on Integer32"""
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


_W2kHistoryFileCollect_Type.__name__ = "Integer32"
_W2kHistoryFileCollect_Object = MibScalar
w2kHistoryFileCollect = _W2kHistoryFileCollect_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 4, 8),
    _W2kHistoryFileCollect_Type()
)
w2kHistoryFileCollect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kHistoryFileCollect.setStatus("mandatory")


class _W2kHistoryProcCollect_Type(Integer32):
    """Custom type w2kHistoryProcCollect based on Integer32"""
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


_W2kHistoryProcCollect_Type.__name__ = "Integer32"
_W2kHistoryProcCollect_Object = MibScalar
w2kHistoryProcCollect = _W2kHistoryProcCollect_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 4, 9),
    _W2kHistoryProcCollect_Type()
)
w2kHistoryProcCollect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kHistoryProcCollect.setStatus("mandatory")


class _W2kHistorySrvcCollect_Type(Integer32):
    """Custom type w2kHistorySrvcCollect based on Integer32"""
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


_W2kHistorySrvcCollect_Type.__name__ = "Integer32"
_W2kHistorySrvcCollect_Object = MibScalar
w2kHistorySrvcCollect = _W2kHistorySrvcCollect_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 4, 10),
    _W2kHistorySrvcCollect_Type()
)
w2kHistorySrvcCollect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kHistorySrvcCollect.setStatus("mandatory")


class _W2kHistoryJobCollect_Type(Integer32):
    """Custom type w2kHistoryJobCollect based on Integer32"""
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


_W2kHistoryJobCollect_Type.__name__ = "Integer32"
_W2kHistoryJobCollect_Object = MibScalar
w2kHistoryJobCollect = _W2kHistoryJobCollect_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 4, 11),
    _W2kHistoryJobCollect_Type()
)
w2kHistoryJobCollect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kHistoryJobCollect.setStatus("mandatory")


class _W2kHistorySessCollect_Type(Integer32):
    """Custom type w2kHistorySessCollect based on Integer32"""
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


_W2kHistorySessCollect_Type.__name__ = "Integer32"
_W2kHistorySessCollect_Object = MibScalar
w2kHistorySessCollect = _W2kHistorySessCollect_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 4, 12),
    _W2kHistorySessCollect_Type()
)
w2kHistorySessCollect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kHistorySessCollect.setStatus("mandatory")


class _W2kHistoryPrnCollect_Type(Integer32):
    """Custom type w2kHistoryPrnCollect based on Integer32"""
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


_W2kHistoryPrnCollect_Type.__name__ = "Integer32"
_W2kHistoryPrnCollect_Object = MibScalar
w2kHistoryPrnCollect = _W2kHistoryPrnCollect_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 4, 13),
    _W2kHistoryPrnCollect_Type()
)
w2kHistoryPrnCollect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kHistoryPrnCollect.setStatus("mandatory")


class _W2kHistoryNetCollect_Type(Integer32):
    """Custom type w2kHistoryNetCollect based on Integer32"""
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


_W2kHistoryNetCollect_Type.__name__ = "Integer32"
_W2kHistoryNetCollect_Object = MibScalar
w2kHistoryNetCollect = _W2kHistoryNetCollect_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 4, 14),
    _W2kHistoryNetCollect_Type()
)
w2kHistoryNetCollect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kHistoryNetCollect.setStatus("mandatory")


class _W2kHistoryRegCollect_Type(Integer32):
    """Custom type w2kHistoryRegCollect based on Integer32"""
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


_W2kHistoryRegCollect_Type.__name__ = "Integer32"
_W2kHistoryRegCollect_Object = MibScalar
w2kHistoryRegCollect = _W2kHistoryRegCollect_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 4, 15),
    _W2kHistoryRegCollect_Type()
)
w2kHistoryRegCollect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kHistoryRegCollect.setStatus("mandatory")


class _W2kHistoryButton_Type(Integer32):
    """Custom type w2kHistoryButton based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("none", 1))
    )


_W2kHistoryButton_Type.__name__ = "Integer32"
_W2kHistoryButton_Object = MibScalar
w2kHistoryButton = _W2kHistoryButton_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 4, 16),
    _W2kHistoryButton_Type()
)
w2kHistoryButton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kHistoryButton.setStatus("mandatory")
_W2kHistoryMaxEntries_Type = Integer32
_W2kHistoryMaxEntries_Object = MibScalar
w2kHistoryMaxEntries = _W2kHistoryMaxEntries_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 4, 17),
    _W2kHistoryMaxEntries_Type()
)
w2kHistoryMaxEntries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    w2kHistoryMaxEntries.setStatus("mandatory")
_W2kHistoryCount_Type = Integer32
_W2kHistoryCount_Object = MibScalar
w2kHistoryCount = _W2kHistoryCount_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 4, 18),
    _W2kHistoryCount_Type()
)
w2kHistoryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kHistoryCount.setStatus("mandatory")
_W2kHistoryTable_Object = MibTable
w2kHistoryTable = _W2kHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 4, 19)
)
if mibBuilder.loadTexts:
    w2kHistoryTable.setStatus("mandatory")
_W2kHistoryEntry_Object = MibTableRow
w2kHistoryEntry = _W2kHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 4, 19, 1)
)
if mibBuilder.loadTexts:
    w2kHistoryEntry.setStatus("mandatory")
_W2kHistoryTrapName_Type = DisplayString
_W2kHistoryTrapName_Object = MibTableColumn
w2kHistoryTrapName = _W2kHistoryTrapName_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 4, 19, 1, 1),
    _W2kHistoryTrapName_Type()
)
w2kHistoryTrapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kHistoryTrapName.setStatus("mandatory")
_W2kHistoryTrapNumber_Type = Integer32
_W2kHistoryTrapNumber_Object = MibTableColumn
w2kHistoryTrapNumber = _W2kHistoryTrapNumber_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 4, 19, 1, 2),
    _W2kHistoryTrapNumber_Type()
)
w2kHistoryTrapNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kHistoryTrapNumber.setStatus("mandatory")
_W2kHistoryTrapTime_Type = DisplayString
_W2kHistoryTrapTime_Object = MibTableColumn
w2kHistoryTrapTime = _W2kHistoryTrapTime_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 4, 19, 1, 3),
    _W2kHistoryTrapTime_Type()
)
w2kHistoryTrapTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kHistoryTrapTime.setStatus("mandatory")
_W2kHistoryTrapVarBind_Type = DisplayString
_W2kHistoryTrapVarBind_Object = MibTableColumn
w2kHistoryTrapVarBind = _W2kHistoryTrapVarBind_Object(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 4, 19, 1, 4),
    _W2kHistoryTrapVarBind_Type()
)
w2kHistoryTrapVarBind.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    w2kHistoryTrapVarBind.setStatus("mandatory")

# Managed Objects groups


# Notification objects

w2kCpuTotalUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 10000)
)
if mibBuilder.loadTexts:
    w2kCpuTotalUnknown.setStatus(
        ""
    )

w2kCpuTotalOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 10001)
)
if mibBuilder.loadTexts:
    w2kCpuTotalOk.setStatus(
        ""
    )

w2kCpuTotalWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 10002)
)
if mibBuilder.loadTexts:
    w2kCpuTotalWarning.setStatus(
        ""
    )

w2kCpuTotalCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 10003)
)
if mibBuilder.loadTexts:
    w2kCpuTotalCritical.setStatus(
        ""
    )

w2kCpuTotalModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 10009)
)
if mibBuilder.loadTexts:
    w2kCpuTotalModified.setStatus(
        ""
    )

w2kCpuUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 10990)
)
if mibBuilder.loadTexts:
    w2kCpuUnknown.setStatus(
        ""
    )

w2kCpuOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 10991)
)
if mibBuilder.loadTexts:
    w2kCpuOk.setStatus(
        ""
    )

w2kCpuWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 10992)
)
if mibBuilder.loadTexts:
    w2kCpuWarning.setStatus(
        ""
    )

w2kCpuCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 10993)
)
if mibBuilder.loadTexts:
    w2kCpuCritical.setStatus(
        ""
    )

w2kCpuAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 10996)
)
if mibBuilder.loadTexts:
    w2kCpuAdded.setStatus(
        ""
    )

w2kCpuDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 10997)
)
if mibBuilder.loadTexts:
    w2kCpuDeleted.setStatus(
        ""
    )

w2kCpuInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 10998)
)
if mibBuilder.loadTexts:
    w2kCpuInfo.setStatus(
        ""
    )

w2kCpuModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 10999)
)
if mibBuilder.loadTexts:
    w2kCpuModified.setStatus(
        ""
    )

w2kMemVirtUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 11010)
)
if mibBuilder.loadTexts:
    w2kMemVirtUnknown.setStatus(
        ""
    )

w2kMemVirtOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 11011)
)
if mibBuilder.loadTexts:
    w2kMemVirtOk.setStatus(
        ""
    )

w2kMemVirtWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 11012)
)
if mibBuilder.loadTexts:
    w2kMemVirtWarning.setStatus(
        ""
    )

w2kMemVirtCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 11013)
)
if mibBuilder.loadTexts:
    w2kMemVirtCritical.setStatus(
        ""
    )

w2kMemVirtModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 11019)
)
if mibBuilder.loadTexts:
    w2kMemVirtModified.setStatus(
        ""
    )

w2kMemPhysUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 11020)
)
if mibBuilder.loadTexts:
    w2kMemPhysUnknown.setStatus(
        ""
    )

w2kMemPhysOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 11021)
)
if mibBuilder.loadTexts:
    w2kMemPhysOk.setStatus(
        ""
    )

w2kMemPhysWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 11022)
)
if mibBuilder.loadTexts:
    w2kMemPhysWarning.setStatus(
        ""
    )

w2kMemPhysCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 11023)
)
if mibBuilder.loadTexts:
    w2kMemPhysCritical.setStatus(
        ""
    )

w2kMemPhysModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 11029)
)
if mibBuilder.loadTexts:
    w2kMemPhysModified.setStatus(
        ""
    )

w2kMemPageUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 11030)
)
if mibBuilder.loadTexts:
    w2kMemPageUnknown.setStatus(
        ""
    )

w2kMemPageOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 11031)
)
if mibBuilder.loadTexts:
    w2kMemPageOk.setStatus(
        ""
    )

w2kMemPageWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 11032)
)
if mibBuilder.loadTexts:
    w2kMemPageWarning.setStatus(
        ""
    )

w2kMemPageCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 11033)
)
if mibBuilder.loadTexts:
    w2kMemPageCritical.setStatus(
        ""
    )

w2kMemPageModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 11039)
)
if mibBuilder.loadTexts:
    w2kMemPageModified.setStatus(
        ""
    )

w2kLVolUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 12980)
)
if mibBuilder.loadTexts:
    w2kLVolUnknown.setStatus(
        ""
    )

w2kLVolOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 12981)
)
if mibBuilder.loadTexts:
    w2kLVolOk.setStatus(
        ""
    )

w2kLVolWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 12982)
)
if mibBuilder.loadTexts:
    w2kLVolWarning.setStatus(
        ""
    )

w2kLVolCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 12983)
)
if mibBuilder.loadTexts:
    w2kLVolCritical.setStatus(
        ""
    )

w2kLVolAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 12986)
)
if mibBuilder.loadTexts:
    w2kLVolAdded.setStatus(
        ""
    )

w2kLVolDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 12987)
)
if mibBuilder.loadTexts:
    w2kLVolDeleted.setStatus(
        ""
    )

w2kLVolInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 12988)
)
if mibBuilder.loadTexts:
    w2kLVolInfo.setStatus(
        ""
    )

w2kLVolModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 12989)
)
if mibBuilder.loadTexts:
    w2kLVolModified.setStatus(
        ""
    )

w2kMntUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 13980)
)
if mibBuilder.loadTexts:
    w2kMntUnknown.setStatus(
        ""
    )

w2kMntOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 13981)
)
if mibBuilder.loadTexts:
    w2kMntOk.setStatus(
        ""
    )

w2kMntWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 13982)
)
if mibBuilder.loadTexts:
    w2kMntWarning.setStatus(
        ""
    )

w2kMntCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 13983)
)
if mibBuilder.loadTexts:
    w2kMntCritical.setStatus(
        ""
    )

w2kMntAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 13986)
)
if mibBuilder.loadTexts:
    w2kMntAdded.setStatus(
        ""
    )

w2kMntDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 13987)
)
if mibBuilder.loadTexts:
    w2kMntDeleted.setStatus(
        ""
    )

w2kMntInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 13988)
)
if mibBuilder.loadTexts:
    w2kMntInfo.setStatus(
        ""
    )

w2kMntModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 13989)
)
if mibBuilder.loadTexts:
    w2kMntModified.setStatus(
        ""
    )

w2kDfsUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 14980)
)
if mibBuilder.loadTexts:
    w2kDfsUnknown.setStatus(
        ""
    )

w2kDfsOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 14981)
)
if mibBuilder.loadTexts:
    w2kDfsOk.setStatus(
        ""
    )

w2kDfsWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 14982)
)
if mibBuilder.loadTexts:
    w2kDfsWarning.setStatus(
        ""
    )

w2kDfsCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 14983)
)
if mibBuilder.loadTexts:
    w2kDfsCritical.setStatus(
        ""
    )

w2kDfsAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 14986)
)
if mibBuilder.loadTexts:
    w2kDfsAdded.setStatus(
        ""
    )

w2kDfsDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 14987)
)
if mibBuilder.loadTexts:
    w2kDfsDeleted.setStatus(
        ""
    )

w2kDfsInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 14988)
)
if mibBuilder.loadTexts:
    w2kDfsInfo.setStatus(
        ""
    )

w2kDfsModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 14989)
)
if mibBuilder.loadTexts:
    w2kDfsModified.setStatus(
        ""
    )

w2kQuotUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 15980)
)
if mibBuilder.loadTexts:
    w2kQuotUnknown.setStatus(
        ""
    )

w2kQuotOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 15981)
)
if mibBuilder.loadTexts:
    w2kQuotOk.setStatus(
        ""
    )

w2kQuotWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 15982)
)
if mibBuilder.loadTexts:
    w2kQuotWarning.setStatus(
        ""
    )

w2kQuotCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 15983)
)
if mibBuilder.loadTexts:
    w2kQuotCritical.setStatus(
        ""
    )

w2kQuotAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 15986)
)
if mibBuilder.loadTexts:
    w2kQuotAdded.setStatus(
        ""
    )

w2kQuotDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 15987)
)
if mibBuilder.loadTexts:
    w2kQuotDeleted.setStatus(
        ""
    )

w2kQuotInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 15988)
)
if mibBuilder.loadTexts:
    w2kQuotInfo.setStatus(
        ""
    )

w2kQuotModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 15989)
)
if mibBuilder.loadTexts:
    w2kQuotModified.setStatus(
        ""
    )

w2kDirUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 16980)
)
if mibBuilder.loadTexts:
    w2kDirUnknown.setStatus(
        ""
    )

w2kDirOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 16981)
)
if mibBuilder.loadTexts:
    w2kDirOk.setStatus(
        ""
    )

w2kDirWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 16982)
)
if mibBuilder.loadTexts:
    w2kDirWarning.setStatus(
        ""
    )

w2kDirCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 16983)
)
if mibBuilder.loadTexts:
    w2kDirCritical.setStatus(
        ""
    )

w2kDirAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 16986)
)
if mibBuilder.loadTexts:
    w2kDirAdded.setStatus(
        ""
    )

w2kDirDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 16987)
)
if mibBuilder.loadTexts:
    w2kDirDeleted.setStatus(
        ""
    )

w2kDirInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 16988)
)
if mibBuilder.loadTexts:
    w2kDirInfo.setStatus(
        ""
    )

w2kDirModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 16989)
)
if mibBuilder.loadTexts:
    w2kDirModified.setStatus(
        ""
    )

w2kFileUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 17980)
)
if mibBuilder.loadTexts:
    w2kFileUnknown.setStatus(
        ""
    )

w2kFileOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 17981)
)
if mibBuilder.loadTexts:
    w2kFileOk.setStatus(
        ""
    )

w2kFileWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 17982)
)
if mibBuilder.loadTexts:
    w2kFileWarning.setStatus(
        ""
    )

w2kFileCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 17983)
)
if mibBuilder.loadTexts:
    w2kFileCritical.setStatus(
        ""
    )

w2kFileAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 17986)
)
if mibBuilder.loadTexts:
    w2kFileAdded.setStatus(
        ""
    )

w2kFileDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 17987)
)
if mibBuilder.loadTexts:
    w2kFileDeleted.setStatus(
        ""
    )

w2kFileInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 17988)
)
if mibBuilder.loadTexts:
    w2kFileInfo.setStatus(
        ""
    )

w2kFileModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 17989)
)
if mibBuilder.loadTexts:
    w2kFileModified.setStatus(
        ""
    )

w2kProcUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 18980)
)
if mibBuilder.loadTexts:
    w2kProcUnknown.setStatus(
        ""
    )

w2kProcOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 18981)
)
if mibBuilder.loadTexts:
    w2kProcOk.setStatus(
        ""
    )

w2kProcWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 18982)
)
if mibBuilder.loadTexts:
    w2kProcWarning.setStatus(
        ""
    )

w2kProcCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 18983)
)
if mibBuilder.loadTexts:
    w2kProcCritical.setStatus(
        ""
    )

w2kProcAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 18986)
)
if mibBuilder.loadTexts:
    w2kProcAdded.setStatus(
        ""
    )

w2kProcDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 18987)
)
if mibBuilder.loadTexts:
    w2kProcDeleted.setStatus(
        ""
    )

w2kProcInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 18988)
)
if mibBuilder.loadTexts:
    w2kProcInfo.setStatus(
        ""
    )

w2kProcModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 18989)
)
if mibBuilder.loadTexts:
    w2kProcModified.setStatus(
        ""
    )

w2kSrvcUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 19980)
)
if mibBuilder.loadTexts:
    w2kSrvcUnknown.setStatus(
        ""
    )

w2kSrvcOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 19981)
)
if mibBuilder.loadTexts:
    w2kSrvcOk.setStatus(
        ""
    )

w2kSrvcWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 19982)
)
if mibBuilder.loadTexts:
    w2kSrvcWarning.setStatus(
        ""
    )

w2kSrvcCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 19983)
)
if mibBuilder.loadTexts:
    w2kSrvcCritical.setStatus(
        ""
    )

w2kSrvcAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 19986)
)
if mibBuilder.loadTexts:
    w2kSrvcAdded.setStatus(
        ""
    )

w2kSrvcDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 19987)
)
if mibBuilder.loadTexts:
    w2kSrvcDeleted.setStatus(
        ""
    )

w2kSrvcInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 19988)
)
if mibBuilder.loadTexts:
    w2kSrvcInfo.setStatus(
        ""
    )

w2kSrvcModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 19989)
)
if mibBuilder.loadTexts:
    w2kSrvcModified.setStatus(
        ""
    )

w2kJobUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 20980)
)
if mibBuilder.loadTexts:
    w2kJobUnknown.setStatus(
        ""
    )

w2kJobOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 20981)
)
if mibBuilder.loadTexts:
    w2kJobOk.setStatus(
        ""
    )

w2kJobWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 20982)
)
if mibBuilder.loadTexts:
    w2kJobWarning.setStatus(
        ""
    )

w2kJobCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 20983)
)
if mibBuilder.loadTexts:
    w2kJobCritical.setStatus(
        ""
    )

w2kJobAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 20986)
)
if mibBuilder.loadTexts:
    w2kJobAdded.setStatus(
        ""
    )

w2kJobDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 20987)
)
if mibBuilder.loadTexts:
    w2kJobDeleted.setStatus(
        ""
    )

w2kJobInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 20988)
)
if mibBuilder.loadTexts:
    w2kJobInfo.setStatus(
        ""
    )

w2kJobModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 20989)
)
if mibBuilder.loadTexts:
    w2kJobModified.setStatus(
        ""
    )

w2kSessUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 21980)
)
if mibBuilder.loadTexts:
    w2kSessUnknown.setStatus(
        ""
    )

w2kSessOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 21981)
)
if mibBuilder.loadTexts:
    w2kSessOk.setStatus(
        ""
    )

w2kSessWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 21982)
)
if mibBuilder.loadTexts:
    w2kSessWarning.setStatus(
        ""
    )

w2kSessCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 21983)
)
if mibBuilder.loadTexts:
    w2kSessCritical.setStatus(
        ""
    )

w2kSessAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 21986)
)
if mibBuilder.loadTexts:
    w2kSessAdded.setStatus(
        ""
    )

w2kSessDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 21987)
)
if mibBuilder.loadTexts:
    w2kSessDeleted.setStatus(
        ""
    )

w2kSessInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 21988)
)
if mibBuilder.loadTexts:
    w2kSessInfo.setStatus(
        ""
    )

w2kSessModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 21989)
)
if mibBuilder.loadTexts:
    w2kSessModified.setStatus(
        ""
    )

w2kPrnUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 22980)
)
if mibBuilder.loadTexts:
    w2kPrnUnknown.setStatus(
        ""
    )

w2kPrnOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 22981)
)
if mibBuilder.loadTexts:
    w2kPrnOk.setStatus(
        ""
    )

w2kPrnWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 22982)
)
if mibBuilder.loadTexts:
    w2kPrnWarning.setStatus(
        ""
    )

w2kPrnCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 22983)
)
if mibBuilder.loadTexts:
    w2kPrnCritical.setStatus(
        ""
    )

w2kPrnAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 22986)
)
if mibBuilder.loadTexts:
    w2kPrnAdded.setStatus(
        ""
    )

w2kPrnDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 22987)
)
if mibBuilder.loadTexts:
    w2kPrnDeleted.setStatus(
        ""
    )

w2kPrnInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 22988)
)
if mibBuilder.loadTexts:
    w2kPrnInfo.setStatus(
        ""
    )

w2kPrnModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 22989)
)
if mibBuilder.loadTexts:
    w2kPrnModified.setStatus(
        ""
    )

w2kNetTotalUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 23000)
)
if mibBuilder.loadTexts:
    w2kNetTotalUnknown.setStatus(
        ""
    )

w2kNetTotalOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 23001)
)
if mibBuilder.loadTexts:
    w2kNetTotalOk.setStatus(
        ""
    )

w2kNetTotalWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 23002)
)
if mibBuilder.loadTexts:
    w2kNetTotalWarning.setStatus(
        ""
    )

w2kNetTotalCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 23003)
)
if mibBuilder.loadTexts:
    w2kNetTotalCritical.setStatus(
        ""
    )

w2kNetTotalInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 23008)
)
if mibBuilder.loadTexts:
    w2kNetTotalInfo.setStatus(
        ""
    )

w2kNetTotalModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 23009)
)
if mibBuilder.loadTexts:
    w2kNetTotalModified.setStatus(
        ""
    )

w2kNetUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 23990)
)
if mibBuilder.loadTexts:
    w2kNetUnknown.setStatus(
        ""
    )

w2kNetOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 23991)
)
if mibBuilder.loadTexts:
    w2kNetOk.setStatus(
        ""
    )

w2kNetWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 23992)
)
if mibBuilder.loadTexts:
    w2kNetWarning.setStatus(
        ""
    )

w2kNetCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 23993)
)
if mibBuilder.loadTexts:
    w2kNetCritical.setStatus(
        ""
    )

w2kNetAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 23996)
)
if mibBuilder.loadTexts:
    w2kNetAdded.setStatus(
        ""
    )

w2kNetDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 23997)
)
if mibBuilder.loadTexts:
    w2kNetDeleted.setStatus(
        ""
    )

w2kNetInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 23998)
)
if mibBuilder.loadTexts:
    w2kNetInfo.setStatus(
        ""
    )

w2kNetModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 23999)
)
if mibBuilder.loadTexts:
    w2kNetModified.setStatus(
        ""
    )

w2kRegUnknown = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 24980)
)
if mibBuilder.loadTexts:
    w2kRegUnknown.setStatus(
        ""
    )

w2kRegOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 24981)
)
if mibBuilder.loadTexts:
    w2kRegOk.setStatus(
        ""
    )

w2kRegWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 24982)
)
if mibBuilder.loadTexts:
    w2kRegWarning.setStatus(
        ""
    )

w2kRegCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 24983)
)
if mibBuilder.loadTexts:
    w2kRegCritical.setStatus(
        ""
    )

w2kRegAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 24986)
)
if mibBuilder.loadTexts:
    w2kRegAdded.setStatus(
        ""
    )

w2kRegDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 24987)
)
if mibBuilder.loadTexts:
    w2kRegDeleted.setStatus(
        ""
    )

w2kRegInfo = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 24988)
)
if mibBuilder.loadTexts:
    w2kRegInfo.setStatus(
        ""
    )

w2kRegModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 791, 2, 10, 2, 43, 0, 24989)
)
if mibBuilder.loadTexts:
    w2kRegModified.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CA-W2KOS-MIB",
    **{"cai": cai,
       "caiSysMgr": caiSysMgr,
       "tng": tng,
       "agents": agents,
       "caiW2kOs": caiW2kOs,
       "w2kCpuTotalUnknown": w2kCpuTotalUnknown,
       "w2kCpuTotalOk": w2kCpuTotalOk,
       "w2kCpuTotalWarning": w2kCpuTotalWarning,
       "w2kCpuTotalCritical": w2kCpuTotalCritical,
       "w2kCpuTotalModified": w2kCpuTotalModified,
       "w2kCpuUnknown": w2kCpuUnknown,
       "w2kCpuOk": w2kCpuOk,
       "w2kCpuWarning": w2kCpuWarning,
       "w2kCpuCritical": w2kCpuCritical,
       "w2kCpuAdded": w2kCpuAdded,
       "w2kCpuDeleted": w2kCpuDeleted,
       "w2kCpuInfo": w2kCpuInfo,
       "w2kCpuModified": w2kCpuModified,
       "w2kMemVirtUnknown": w2kMemVirtUnknown,
       "w2kMemVirtOk": w2kMemVirtOk,
       "w2kMemVirtWarning": w2kMemVirtWarning,
       "w2kMemVirtCritical": w2kMemVirtCritical,
       "w2kMemVirtModified": w2kMemVirtModified,
       "w2kMemPhysUnknown": w2kMemPhysUnknown,
       "w2kMemPhysOk": w2kMemPhysOk,
       "w2kMemPhysWarning": w2kMemPhysWarning,
       "w2kMemPhysCritical": w2kMemPhysCritical,
       "w2kMemPhysModified": w2kMemPhysModified,
       "w2kMemPageUnknown": w2kMemPageUnknown,
       "w2kMemPageOk": w2kMemPageOk,
       "w2kMemPageWarning": w2kMemPageWarning,
       "w2kMemPageCritical": w2kMemPageCritical,
       "w2kMemPageModified": w2kMemPageModified,
       "w2kLVolUnknown": w2kLVolUnknown,
       "w2kLVolOk": w2kLVolOk,
       "w2kLVolWarning": w2kLVolWarning,
       "w2kLVolCritical": w2kLVolCritical,
       "w2kLVolAdded": w2kLVolAdded,
       "w2kLVolDeleted": w2kLVolDeleted,
       "w2kLVolInfo": w2kLVolInfo,
       "w2kLVolModified": w2kLVolModified,
       "w2kMntUnknown": w2kMntUnknown,
       "w2kMntOk": w2kMntOk,
       "w2kMntWarning": w2kMntWarning,
       "w2kMntCritical": w2kMntCritical,
       "w2kMntAdded": w2kMntAdded,
       "w2kMntDeleted": w2kMntDeleted,
       "w2kMntInfo": w2kMntInfo,
       "w2kMntModified": w2kMntModified,
       "w2kDfsUnknown": w2kDfsUnknown,
       "w2kDfsOk": w2kDfsOk,
       "w2kDfsWarning": w2kDfsWarning,
       "w2kDfsCritical": w2kDfsCritical,
       "w2kDfsAdded": w2kDfsAdded,
       "w2kDfsDeleted": w2kDfsDeleted,
       "w2kDfsInfo": w2kDfsInfo,
       "w2kDfsModified": w2kDfsModified,
       "w2kQuotUnknown": w2kQuotUnknown,
       "w2kQuotOk": w2kQuotOk,
       "w2kQuotWarning": w2kQuotWarning,
       "w2kQuotCritical": w2kQuotCritical,
       "w2kQuotAdded": w2kQuotAdded,
       "w2kQuotDeleted": w2kQuotDeleted,
       "w2kQuotInfo": w2kQuotInfo,
       "w2kQuotModified": w2kQuotModified,
       "w2kDirUnknown": w2kDirUnknown,
       "w2kDirOk": w2kDirOk,
       "w2kDirWarning": w2kDirWarning,
       "w2kDirCritical": w2kDirCritical,
       "w2kDirAdded": w2kDirAdded,
       "w2kDirDeleted": w2kDirDeleted,
       "w2kDirInfo": w2kDirInfo,
       "w2kDirModified": w2kDirModified,
       "w2kFileUnknown": w2kFileUnknown,
       "w2kFileOk": w2kFileOk,
       "w2kFileWarning": w2kFileWarning,
       "w2kFileCritical": w2kFileCritical,
       "w2kFileAdded": w2kFileAdded,
       "w2kFileDeleted": w2kFileDeleted,
       "w2kFileInfo": w2kFileInfo,
       "w2kFileModified": w2kFileModified,
       "w2kProcUnknown": w2kProcUnknown,
       "w2kProcOk": w2kProcOk,
       "w2kProcWarning": w2kProcWarning,
       "w2kProcCritical": w2kProcCritical,
       "w2kProcAdded": w2kProcAdded,
       "w2kProcDeleted": w2kProcDeleted,
       "w2kProcInfo": w2kProcInfo,
       "w2kProcModified": w2kProcModified,
       "w2kSrvcUnknown": w2kSrvcUnknown,
       "w2kSrvcOk": w2kSrvcOk,
       "w2kSrvcWarning": w2kSrvcWarning,
       "w2kSrvcCritical": w2kSrvcCritical,
       "w2kSrvcAdded": w2kSrvcAdded,
       "w2kSrvcDeleted": w2kSrvcDeleted,
       "w2kSrvcInfo": w2kSrvcInfo,
       "w2kSrvcModified": w2kSrvcModified,
       "w2kJobUnknown": w2kJobUnknown,
       "w2kJobOk": w2kJobOk,
       "w2kJobWarning": w2kJobWarning,
       "w2kJobCritical": w2kJobCritical,
       "w2kJobAdded": w2kJobAdded,
       "w2kJobDeleted": w2kJobDeleted,
       "w2kJobInfo": w2kJobInfo,
       "w2kJobModified": w2kJobModified,
       "w2kSessUnknown": w2kSessUnknown,
       "w2kSessOk": w2kSessOk,
       "w2kSessWarning": w2kSessWarning,
       "w2kSessCritical": w2kSessCritical,
       "w2kSessAdded": w2kSessAdded,
       "w2kSessDeleted": w2kSessDeleted,
       "w2kSessInfo": w2kSessInfo,
       "w2kSessModified": w2kSessModified,
       "w2kPrnUnknown": w2kPrnUnknown,
       "w2kPrnOk": w2kPrnOk,
       "w2kPrnWarning": w2kPrnWarning,
       "w2kPrnCritical": w2kPrnCritical,
       "w2kPrnAdded": w2kPrnAdded,
       "w2kPrnDeleted": w2kPrnDeleted,
       "w2kPrnInfo": w2kPrnInfo,
       "w2kPrnModified": w2kPrnModified,
       "w2kNetTotalUnknown": w2kNetTotalUnknown,
       "w2kNetTotalOk": w2kNetTotalOk,
       "w2kNetTotalWarning": w2kNetTotalWarning,
       "w2kNetTotalCritical": w2kNetTotalCritical,
       "w2kNetTotalInfo": w2kNetTotalInfo,
       "w2kNetTotalModified": w2kNetTotalModified,
       "w2kNetUnknown": w2kNetUnknown,
       "w2kNetOk": w2kNetOk,
       "w2kNetWarning": w2kNetWarning,
       "w2kNetCritical": w2kNetCritical,
       "w2kNetAdded": w2kNetAdded,
       "w2kNetDeleted": w2kNetDeleted,
       "w2kNetInfo": w2kNetInfo,
       "w2kNetModified": w2kNetModified,
       "w2kRegUnknown": w2kRegUnknown,
       "w2kRegOk": w2kRegOk,
       "w2kRegWarning": w2kRegWarning,
       "w2kRegCritical": w2kRegCritical,
       "w2kRegAdded": w2kRegAdded,
       "w2kRegDeleted": w2kRegDeleted,
       "w2kRegInfo": w2kRegInfo,
       "w2kRegModified": w2kRegModified,
       "w2kConfigGroup": w2kConfigGroup,
       "w2kConfigGeneralGroup": w2kConfigGeneralGroup,
       "w2kConfigGeneralAgentVersion": w2kConfigGeneralAgentVersion,
       "w2kConfigGeneralColdStartTime": w2kConfigGeneralColdStartTime,
       "w2kConfigGeneralWarmStartTime": w2kConfigGeneralWarmStartTime,
       "w2kConfigGeneralCpuPollTime": w2kConfigGeneralCpuPollTime,
       "w2kConfigGeneralMemPollTime": w2kConfigGeneralMemPollTime,
       "w2kConfigGeneralLVolPollTime": w2kConfigGeneralLVolPollTime,
       "w2kConfigGeneralMntPollTime": w2kConfigGeneralMntPollTime,
       "w2kConfigGeneralDfsPollTime": w2kConfigGeneralDfsPollTime,
       "w2kConfigGeneralQuotPollTime": w2kConfigGeneralQuotPollTime,
       "w2kConfigGeneralDirPollTime": w2kConfigGeneralDirPollTime,
       "w2kConfigGeneralFilePollTime": w2kConfigGeneralFilePollTime,
       "w2kConfigGeneralProcPollTime": w2kConfigGeneralProcPollTime,
       "w2kConfigGeneralSrvcPollTime": w2kConfigGeneralSrvcPollTime,
       "w2kConfigGeneralJobPollTime": w2kConfigGeneralJobPollTime,
       "w2kConfigGeneralSessPollTime": w2kConfigGeneralSessPollTime,
       "w2kConfigGeneralPrnPollTime": w2kConfigGeneralPrnPollTime,
       "w2kConfigGeneralNetPollTime": w2kConfigGeneralNetPollTime,
       "w2kConfigGeneralRegPollTime": w2kConfigGeneralRegPollTime,
       "w2kConfigSysGroup": w2kConfigSysGroup,
       "w2kConfigSysNodeName": w2kConfigSysNodeName,
       "w2kConfigSysVersion": w2kConfigSysVersion,
       "w2kConfigSysBios": w2kConfigSysBios,
       "w2kConfigSysColdStartTime": w2kConfigSysColdStartTime,
       "w2kConfigCpuGroup": w2kConfigCpuGroup,
       "w2kConfigCpuPollInterval": w2kConfigCpuPollInterval,
       "w2kConfigCpuPollMethod": w2kConfigCpuPollMethod,
       "w2kConfigCpuLoadLag": w2kConfigCpuLoadLag,
       "w2kConfigCpuLoadWarn": w2kConfigCpuLoadWarn,
       "w2kConfigCpuLoadCrit": w2kConfigCpuLoadCrit,
       "w2kConfigCpuLoadMonitor": w2kConfigCpuLoadMonitor,
       "w2kConfigCpuLossAction": w2kConfigCpuLossAction,
       "w2kConfigMemGroup": w2kConfigMemGroup,
       "w2kConfigMemPollInterval": w2kConfigMemPollInterval,
       "w2kConfigMemPollMethod": w2kConfigMemPollMethod,
       "w2kConfigLVolGroup": w2kConfigLVolGroup,
       "w2kConfigLVolPollInterval": w2kConfigLVolPollInterval,
       "w2kConfigLVolPollMethod": w2kConfigLVolPollMethod,
       "w2kConfigLVolAutoPollInterval": w2kConfigLVolAutoPollInterval,
       "w2kConfigLVolFragPollInterval": w2kConfigLVolFragPollInterval,
       "w2kConfigLVolName": w2kConfigLVolName,
       "w2kConfigLVolDescription": w2kConfigLVolDescription,
       "w2kConfigLVolAggLag": w2kConfigLVolAggLag,
       "w2kConfigLVolSizeWarn": w2kConfigLVolSizeWarn,
       "w2kConfigLVolSizeCrit": w2kConfigLVolSizeCrit,
       "w2kConfigLVolSizeMonitor": w2kConfigLVolSizeMonitor,
       "w2kConfigLVolSizeDWarn": w2kConfigLVolSizeDWarn,
       "w2kConfigLVolSizeDCrit": w2kConfigLVolSizeDCrit,
       "w2kConfigLVolSizeDMonitor": w2kConfigLVolSizeDMonitor,
       "w2kConfigLVolTPutWarn": w2kConfigLVolTPutWarn,
       "w2kConfigLVolTPutCrit": w2kConfigLVolTPutCrit,
       "w2kConfigLVolTPutMonitor": w2kConfigLVolTPutMonitor,
       "w2kConfigLVolFragWarn": w2kConfigLVolFragWarn,
       "w2kConfigLVolFragCrit": w2kConfigLVolFragCrit,
       "w2kConfigLVolFragMonitor": w2kConfigLVolFragMonitor,
       "w2kConfigLVolLossAction": w2kConfigLVolLossAction,
       "w2kConfigLVolAutoTableWatcherName": w2kConfigLVolAutoTableWatcherName,
       "w2kConfigLVolButton": w2kConfigLVolButton,
       "w2kConfigLVolAutoTable": w2kConfigLVolAutoTable,
       "w2kConfigLVolAutoEntry": w2kConfigLVolAutoEntry,
       "w2kConfigLVolAutoWatcherName": w2kConfigLVolAutoWatcherName,
       "w2kConfigLVolAutoName": w2kConfigLVolAutoName,
       "w2kConfigLVolAutoDescription": w2kConfigLVolAutoDescription,
       "w2kConfigLVolAutoAggLag": w2kConfigLVolAutoAggLag,
       "w2kConfigLVolAutoSizeWarn": w2kConfigLVolAutoSizeWarn,
       "w2kConfigLVolAutoSizeCrit": w2kConfigLVolAutoSizeCrit,
       "w2kConfigLVolAutoSizeMonitor": w2kConfigLVolAutoSizeMonitor,
       "w2kConfigLVolAutoSizeDWarn": w2kConfigLVolAutoSizeDWarn,
       "w2kConfigLVolAutoSizeDCrit": w2kConfigLVolAutoSizeDCrit,
       "w2kConfigLVolAutoSizeDMonitor": w2kConfigLVolAutoSizeDMonitor,
       "w2kConfigLVolAutoTPutWarn": w2kConfigLVolAutoTPutWarn,
       "w2kConfigLVolAutoTPutCrit": w2kConfigLVolAutoTPutCrit,
       "w2kConfigLVolAutoTPutMonitor": w2kConfigLVolAutoTPutMonitor,
       "w2kConfigLVolAutoFragWarn": w2kConfigLVolAutoFragWarn,
       "w2kConfigLVolAutoFragCrit": w2kConfigLVolAutoFragCrit,
       "w2kConfigLVolAutoFragMonitor": w2kConfigLVolAutoFragMonitor,
       "w2kConfigLVolAutoLossAction": w2kConfigLVolAutoLossAction,
       "w2kConfigLVolAutoButton": w2kConfigLVolAutoButton,
       "w2kConfigMntGroup": w2kConfigMntGroup,
       "w2kConfigMntPollInterval": w2kConfigMntPollInterval,
       "w2kConfigMntPollMethod": w2kConfigMntPollMethod,
       "w2kConfigMntAutoPollInterval": w2kConfigMntAutoPollInterval,
       "w2kConfigMntName": w2kConfigMntName,
       "w2kConfigMntDescription": w2kConfigMntDescription,
       "w2kConfigMntAggLag": w2kConfigMntAggLag,
       "w2kConfigMntRelToMonitor": w2kConfigMntRelToMonitor,
       "w2kConfigMntLossAction": w2kConfigMntLossAction,
       "w2kConfigMntAutoTableWatcherName": w2kConfigMntAutoTableWatcherName,
       "w2kConfigMntButton": w2kConfigMntButton,
       "w2kConfigMntAutoTable": w2kConfigMntAutoTable,
       "w2kConfigMntAutoEntry": w2kConfigMntAutoEntry,
       "w2kConfigMntAutoWatcherName": w2kConfigMntAutoWatcherName,
       "w2kConfigMntAutoName": w2kConfigMntAutoName,
       "w2kConfigMntAutoDescription": w2kConfigMntAutoDescription,
       "w2kConfigMntAutoAggLag": w2kConfigMntAutoAggLag,
       "w2kConfigMntAutoRelToMonitor": w2kConfigMntAutoRelToMonitor,
       "w2kConfigMntAutoLossAction": w2kConfigMntAutoLossAction,
       "w2kConfigMntAutoButton": w2kConfigMntAutoButton,
       "w2kConfigDfsGroup": w2kConfigDfsGroup,
       "w2kConfigDfsPollInterval": w2kConfigDfsPollInterval,
       "w2kConfigDfsPollMethod": w2kConfigDfsPollMethod,
       "w2kConfigDfsAutoPollInterval": w2kConfigDfsAutoPollInterval,
       "w2kConfigDfsName": w2kConfigDfsName,
       "w2kConfigDfsDescription": w2kConfigDfsDescription,
       "w2kConfigDfsAggLag": w2kConfigDfsAggLag,
       "w2kConfigDfsReplicaWarn": w2kConfigDfsReplicaWarn,
       "w2kConfigDfsReplicaCrit": w2kConfigDfsReplicaCrit,
       "w2kConfigDfsReplicaMonitor": w2kConfigDfsReplicaMonitor,
       "w2kConfigDfsLossAction": w2kConfigDfsLossAction,
       "w2kConfigDfsAutoTableWatcherName": w2kConfigDfsAutoTableWatcherName,
       "w2kConfigDfsButton": w2kConfigDfsButton,
       "w2kConfigDfsAutoTable": w2kConfigDfsAutoTable,
       "w2kConfigDfsAutoEntry": w2kConfigDfsAutoEntry,
       "w2kConfigDfsAutoWatcherName": w2kConfigDfsAutoWatcherName,
       "w2kConfigDfsAutoName": w2kConfigDfsAutoName,
       "w2kConfigDfsAutoDescription": w2kConfigDfsAutoDescription,
       "w2kConfigDfsAutoAggLag": w2kConfigDfsAutoAggLag,
       "w2kConfigDfsAutoReplicaWarn": w2kConfigDfsAutoReplicaWarn,
       "w2kConfigDfsAutoReplicaCrit": w2kConfigDfsAutoReplicaCrit,
       "w2kConfigDfsAutoReplicaMonitor": w2kConfigDfsAutoReplicaMonitor,
       "w2kConfigDfsAutoLossAction": w2kConfigDfsAutoLossAction,
       "w2kConfigDfsAutoButton": w2kConfigDfsAutoButton,
       "w2kConfigQuotGroup": w2kConfigQuotGroup,
       "w2kConfigQuotPollInterval": w2kConfigQuotPollInterval,
       "w2kConfigQuotPollMethod": w2kConfigQuotPollMethod,
       "w2kConfigQuotLVolName": w2kConfigQuotLVolName,
       "w2kConfigQuotUserName": w2kConfigQuotUserName,
       "w2kConfigQuotDescription": w2kConfigQuotDescription,
       "w2kConfigQuotAggLag": w2kConfigQuotAggLag,
       "w2kConfigQuotExist": w2kConfigQuotExist,
       "w2kConfigQuotExistMonitor": w2kConfigQuotExistMonitor,
       "w2kConfigQuotSizeWarn": w2kConfigQuotSizeWarn,
       "w2kConfigQuotSizeCrit": w2kConfigQuotSizeCrit,
       "w2kConfigQuotSizeMonitor": w2kConfigQuotSizeMonitor,
       "w2kConfigQuotButton": w2kConfigQuotButton,
       "w2kConfigDirGroup": w2kConfigDirGroup,
       "w2kConfigDirPollInterval": w2kConfigDirPollInterval,
       "w2kConfigDirPollMethod": w2kConfigDirPollMethod,
       "w2kConfigDirName": w2kConfigDirName,
       "w2kConfigDirDescription": w2kConfigDirDescription,
       "w2kConfigDirAggLag": w2kConfigDirAggLag,
       "w2kConfigDirExist": w2kConfigDirExist,
       "w2kConfigDirExistMonitor": w2kConfigDirExistMonitor,
       "w2kConfigDirTimeMonitor": w2kConfigDirTimeMonitor,
       "w2kConfigDirSizeWarn": w2kConfigDirSizeWarn,
       "w2kConfigDirSizeCrit": w2kConfigDirSizeCrit,
       "w2kConfigDirSizeMonitor": w2kConfigDirSizeMonitor,
       "w2kConfigDirSizeDWarn": w2kConfigDirSizeDWarn,
       "w2kConfigDirSizeDCrit": w2kConfigDirSizeDCrit,
       "w2kConfigDirSizeDMonitor": w2kConfigDirSizeDMonitor,
       "w2kConfigDirEntryWarn": w2kConfigDirEntryWarn,
       "w2kConfigDirEntryCrit": w2kConfigDirEntryCrit,
       "w2kConfigDirEntryMonitor": w2kConfigDirEntryMonitor,
       "w2kConfigDirButton": w2kConfigDirButton,
       "w2kConfigFileGroup": w2kConfigFileGroup,
       "w2kConfigFilePollInterval": w2kConfigFilePollInterval,
       "w2kConfigFilePollMethod": w2kConfigFilePollMethod,
       "w2kConfigFileName": w2kConfigFileName,
       "w2kConfigFileDescription": w2kConfigFileDescription,
       "w2kConfigFileAggLag": w2kConfigFileAggLag,
       "w2kConfigFileExist": w2kConfigFileExist,
       "w2kConfigFileExistMonitor": w2kConfigFileExistMonitor,
       "w2kConfigFileTimeMonitor": w2kConfigFileTimeMonitor,
       "w2kConfigFileSizeWarn": w2kConfigFileSizeWarn,
       "w2kConfigFileSizeCrit": w2kConfigFileSizeCrit,
       "w2kConfigFileSizeMonitor": w2kConfigFileSizeMonitor,
       "w2kConfigFileSizeDWarn": w2kConfigFileSizeDWarn,
       "w2kConfigFileSizeDCrit": w2kConfigFileSizeDCrit,
       "w2kConfigFileSizeDMonitor": w2kConfigFileSizeDMonitor,
       "w2kConfigFileButton": w2kConfigFileButton,
       "w2kConfigProcGroup": w2kConfigProcGroup,
       "w2kConfigProcPollInterval": w2kConfigProcPollInterval,
       "w2kConfigProcPollMethod": w2kConfigProcPollMethod,
       "w2kConfigProcProcName": w2kConfigProcProcName,
       "w2kConfigProcPathName": w2kConfigProcPathName,
       "w2kConfigProcUserName": w2kConfigProcUserName,
       "w2kConfigProcDescription": w2kConfigProcDescription,
       "w2kConfigProcAggLag": w2kConfigProcAggLag,
       "w2kConfigProcInstMin": w2kConfigProcInstMin,
       "w2kConfigProcInstMax": w2kConfigProcInstMax,
       "w2kConfigProcInstMonitor": w2kConfigProcInstMonitor,
       "w2kConfigProcChildMin": w2kConfigProcChildMin,
       "w2kConfigProcChildMax": w2kConfigProcChildMax,
       "w2kConfigProcChildMonitor": w2kConfigProcChildMonitor,
       "w2kConfigProcThreadMin": w2kConfigProcThreadMin,
       "w2kConfigProcThreadMax": w2kConfigProcThreadMax,
       "w2kConfigProcThreadMonitor": w2kConfigProcThreadMonitor,
       "w2kConfigProcMemoryWarn": w2kConfigProcMemoryWarn,
       "w2kConfigProcMemoryCrit": w2kConfigProcMemoryCrit,
       "w2kConfigProcMemoryMonitor": w2kConfigProcMemoryMonitor,
       "w2kConfigProcCpuWarn": w2kConfigProcCpuWarn,
       "w2kConfigProcCpuCrit": w2kConfigProcCpuCrit,
       "w2kConfigProcCpuMonitor": w2kConfigProcCpuMonitor,
       "w2kConfigProcButton": w2kConfigProcButton,
       "w2kConfigSrvcGroup": w2kConfigSrvcGroup,
       "w2kConfigSrvcPollInterval": w2kConfigSrvcPollInterval,
       "w2kConfigSrvcPollMethod": w2kConfigSrvcPollMethod,
       "w2kConfigSrvcAutoPollInterval": w2kConfigSrvcAutoPollInterval,
       "w2kConfigSrvcName": w2kConfigSrvcName,
       "w2kConfigSrvcDescription": w2kConfigSrvcDescription,
       "w2kConfigSrvcAggLag": w2kConfigSrvcAggLag,
       "w2kConfigSrvcExist": w2kConfigSrvcExist,
       "w2kConfigSrvcExistMonitor": w2kConfigSrvcExistMonitor,
       "w2kConfigSrvcActive": w2kConfigSrvcActive,
       "w2kConfigSrvcActiveMonitor": w2kConfigSrvcActiveMonitor,
       "w2kConfigSrvcAutoTableWatcherName": w2kConfigSrvcAutoTableWatcherName,
       "w2kConfigSrvcButton": w2kConfigSrvcButton,
       "w2kConfigSrvcAutoTable": w2kConfigSrvcAutoTable,
       "w2kConfigSrvcAutoEntry": w2kConfigSrvcAutoEntry,
       "w2kConfigSrvcAutoWatcherName": w2kConfigSrvcAutoWatcherName,
       "w2kConfigSrvcAutoName": w2kConfigSrvcAutoName,
       "w2kConfigSrvcAutoDescription": w2kConfigSrvcAutoDescription,
       "w2kConfigSrvcAutoAggLag": w2kConfigSrvcAutoAggLag,
       "w2kConfigSrvcAutoExist": w2kConfigSrvcAutoExist,
       "w2kConfigSrvcAutoExistMonitor": w2kConfigSrvcAutoExistMonitor,
       "w2kConfigSrvcAutoActive": w2kConfigSrvcAutoActive,
       "w2kConfigSrvcAutoActiveMonitor": w2kConfigSrvcAutoActiveMonitor,
       "w2kConfigSrvcAutoButton": w2kConfigSrvcAutoButton,
       "w2kConfigJobGroup": w2kConfigJobGroup,
       "w2kConfigJobPollInterval": w2kConfigJobPollInterval,
       "w2kConfigJobPollMethod": w2kConfigJobPollMethod,
       "w2kConfigJobName": w2kConfigJobName,
       "w2kConfigJobDescription": w2kConfigJobDescription,
       "w2kConfigJobAggLag": w2kConfigJobAggLag,
       "w2kConfigJobExist": w2kConfigJobExist,
       "w2kConfigJobExistMonitor": w2kConfigJobExistMonitor,
       "w2kConfigJobProcessMin": w2kConfigJobProcessMin,
       "w2kConfigJobProcessMax": w2kConfigJobProcessMax,
       "w2kConfigJobProcessMonitor": w2kConfigJobProcessMonitor,
       "w2kConfigJobCpuWarn": w2kConfigJobCpuWarn,
       "w2kConfigJobCpuCrit": w2kConfigJobCpuCrit,
       "w2kConfigJobCpuMonitor": w2kConfigJobCpuMonitor,
       "w2kConfigJobButton": w2kConfigJobButton,
       "w2kConfigSessGroup": w2kConfigSessGroup,
       "w2kConfigSessPollInterval": w2kConfigSessPollInterval,
       "w2kConfigSessPollMethod": w2kConfigSessPollMethod,
       "w2kConfigSessClientName": w2kConfigSessClientName,
       "w2kConfigSessUserName": w2kConfigSessUserName,
       "w2kConfigSessDescription": w2kConfigSessDescription,
       "w2kConfigSessAggLag": w2kConfigSessAggLag,
       "w2kConfigSessInstMin": w2kConfigSessInstMin,
       "w2kConfigSessInstMax": w2kConfigSessInstMax,
       "w2kConfigSessInstMonitor": w2kConfigSessInstMonitor,
       "w2kConfigSessMemoryWarn": w2kConfigSessMemoryWarn,
       "w2kConfigSessMemoryCrit": w2kConfigSessMemoryCrit,
       "w2kConfigSessMemoryMonitor": w2kConfigSessMemoryMonitor,
       "w2kConfigSessCpuWarn": w2kConfigSessCpuWarn,
       "w2kConfigSessCpuCrit": w2kConfigSessCpuCrit,
       "w2kConfigSessCpuMonitor": w2kConfigSessCpuMonitor,
       "w2kConfigSessButton": w2kConfigSessButton,
       "w2kConfigPrnGroup": w2kConfigPrnGroup,
       "w2kConfigPrnPollInterval": w2kConfigPrnPollInterval,
       "w2kConfigPrnPollMethod": w2kConfigPrnPollMethod,
       "w2kConfigPrnAutoPollInterval": w2kConfigPrnAutoPollInterval,
       "w2kConfigPrnName": w2kConfigPrnName,
       "w2kConfigPrnDescription": w2kConfigPrnDescription,
       "w2kConfigPrnAggLag": w2kConfigPrnAggLag,
       "w2kConfigPrnEventMonitor": w2kConfigPrnEventMonitor,
       "w2kConfigPrnQueueWarn": w2kConfigPrnQueueWarn,
       "w2kConfigPrnQueueCrit": w2kConfigPrnQueueCrit,
       "w2kConfigPrnQueueMonitor": w2kConfigPrnQueueMonitor,
       "w2kConfigPrnLossAction": w2kConfigPrnLossAction,
       "w2kConfigPrnAutoTableWatcherName": w2kConfigPrnAutoTableWatcherName,
       "w2kConfigPrnButton": w2kConfigPrnButton,
       "w2kConfigPrnAutoTable": w2kConfigPrnAutoTable,
       "w2kConfigPrnAutoEntry": w2kConfigPrnAutoEntry,
       "w2kConfigPrnAutoWatcherName": w2kConfigPrnAutoWatcherName,
       "w2kConfigPrnAutoName": w2kConfigPrnAutoName,
       "w2kConfigPrnAutoDescription": w2kConfigPrnAutoDescription,
       "w2kConfigPrnAutoAggLag": w2kConfigPrnAutoAggLag,
       "w2kConfigPrnAutoEventMonitor": w2kConfigPrnAutoEventMonitor,
       "w2kConfigPrnAutoQueueWarn": w2kConfigPrnAutoQueueWarn,
       "w2kConfigPrnAutoQueueCrit": w2kConfigPrnAutoQueueCrit,
       "w2kConfigPrnAutoQueueMonitor": w2kConfigPrnAutoQueueMonitor,
       "w2kConfigPrnAutoLossAction": w2kConfigPrnAutoLossAction,
       "w2kConfigPrnAutoButton": w2kConfigPrnAutoButton,
       "w2kConfigNetGroup": w2kConfigNetGroup,
       "w2kConfigNetPollInterval": w2kConfigNetPollInterval,
       "w2kConfigNetPollMethod": w2kConfigNetPollMethod,
       "w2kConfigNetAggLag": w2kConfigNetAggLag,
       "w2kConfigNetInPktWarn": w2kConfigNetInPktWarn,
       "w2kConfigNetInPktCrit": w2kConfigNetInPktCrit,
       "w2kConfigNetInPktMonitor": w2kConfigNetInPktMonitor,
       "w2kConfigNetOutPktWarn": w2kConfigNetOutPktWarn,
       "w2kConfigNetOutPktCrit": w2kConfigNetOutPktCrit,
       "w2kConfigNetOutPktMonitor": w2kConfigNetOutPktMonitor,
       "w2kConfigNetInErrDWarn": w2kConfigNetInErrDWarn,
       "w2kConfigNetInErrDCrit": w2kConfigNetInErrDCrit,
       "w2kConfigNetInErrDMonitor": w2kConfigNetInErrDMonitor,
       "w2kConfigNetOutErrDWarn": w2kConfigNetOutErrDWarn,
       "w2kConfigNetOutErrDCrit": w2kConfigNetOutErrDCrit,
       "w2kConfigNetOutErrDMonitor": w2kConfigNetOutErrDMonitor,
       "w2kConfigNetLossAction": w2kConfigNetLossAction,
       "w2kConfigRegGroup": w2kConfigRegGroup,
       "w2kConfigRegPollInterval": w2kConfigRegPollInterval,
       "w2kConfigRegPollMethod": w2kConfigRegPollMethod,
       "w2kConfigRegName": w2kConfigRegName,
       "w2kConfigRegDescription": w2kConfigRegDescription,
       "w2kConfigRegAggLag": w2kConfigRegAggLag,
       "w2kConfigRegExist": w2kConfigRegExist,
       "w2kConfigRegExistMonitor": w2kConfigRegExistMonitor,
       "w2kConfigRegValueRef": w2kConfigRegValueRef,
       "w2kConfigRegValueCond": w2kConfigRegValueCond,
       "w2kConfigRegValueMonitor": w2kConfigRegValueMonitor,
       "w2kConfigRegButton": w2kConfigRegButton,
       "w2kStatusGroup": w2kStatusGroup,
       "w2kStatusGeneralGroup": w2kStatusGeneralGroup,
       "w2kStatusGeneralTotalCount": w2kStatusGeneralTotalCount,
       "w2kStatusGeneralTotalWarn": w2kStatusGeneralTotalWarn,
       "w2kStatusGeneralTotalCrit": w2kStatusGeneralTotalCrit,
       "w2kStatusGeneralCpuCount": w2kStatusGeneralCpuCount,
       "w2kStatusGeneralCpuWarn": w2kStatusGeneralCpuWarn,
       "w2kStatusGeneralCpuCrit": w2kStatusGeneralCpuCrit,
       "w2kStatusGeneralMemCount": w2kStatusGeneralMemCount,
       "w2kStatusGeneralMemWarn": w2kStatusGeneralMemWarn,
       "w2kStatusGeneralMemCrit": w2kStatusGeneralMemCrit,
       "w2kStatusGeneralLVolCount": w2kStatusGeneralLVolCount,
       "w2kStatusGeneralLVolWarn": w2kStatusGeneralLVolWarn,
       "w2kStatusGeneralLVolCrit": w2kStatusGeneralLVolCrit,
       "w2kStatusGeneralMntCount": w2kStatusGeneralMntCount,
       "w2kStatusGeneralMntWarn": w2kStatusGeneralMntWarn,
       "w2kStatusGeneralMntCrit": w2kStatusGeneralMntCrit,
       "w2kStatusGeneralDfsCount": w2kStatusGeneralDfsCount,
       "w2kStatusGeneralDfsWarn": w2kStatusGeneralDfsWarn,
       "w2kStatusGeneralDfsCrit": w2kStatusGeneralDfsCrit,
       "w2kStatusGeneralQuotCount": w2kStatusGeneralQuotCount,
       "w2kStatusGeneralQuotWarn": w2kStatusGeneralQuotWarn,
       "w2kStatusGeneralQuotCrit": w2kStatusGeneralQuotCrit,
       "w2kStatusGeneralDirCount": w2kStatusGeneralDirCount,
       "w2kStatusGeneralDirWarn": w2kStatusGeneralDirWarn,
       "w2kStatusGeneralDirCrit": w2kStatusGeneralDirCrit,
       "w2kStatusGeneralFileCount": w2kStatusGeneralFileCount,
       "w2kStatusGeneralFileWarn": w2kStatusGeneralFileWarn,
       "w2kStatusGeneralFileCrit": w2kStatusGeneralFileCrit,
       "w2kStatusGeneralProcCount": w2kStatusGeneralProcCount,
       "w2kStatusGeneralProcWarn": w2kStatusGeneralProcWarn,
       "w2kStatusGeneralProcCrit": w2kStatusGeneralProcCrit,
       "w2kStatusGeneralSrvcCount": w2kStatusGeneralSrvcCount,
       "w2kStatusGeneralSrvcWarn": w2kStatusGeneralSrvcWarn,
       "w2kStatusGeneralSrvcCrit": w2kStatusGeneralSrvcCrit,
       "w2kStatusGeneralJobCount": w2kStatusGeneralJobCount,
       "w2kStatusGeneralJobWarn": w2kStatusGeneralJobWarn,
       "w2kStatusGeneralJobCrit": w2kStatusGeneralJobCrit,
       "w2kStatusGeneralSessCount": w2kStatusGeneralSessCount,
       "w2kStatusGeneralSessWarn": w2kStatusGeneralSessWarn,
       "w2kStatusGeneralSessCrit": w2kStatusGeneralSessCrit,
       "w2kStatusGeneralPrnCount": w2kStatusGeneralPrnCount,
       "w2kStatusGeneralPrnWarn": w2kStatusGeneralPrnWarn,
       "w2kStatusGeneralPrnCrit": w2kStatusGeneralPrnCrit,
       "w2kStatusGeneralNetCount": w2kStatusGeneralNetCount,
       "w2kStatusGeneralNetWarn": w2kStatusGeneralNetWarn,
       "w2kStatusGeneralNetCrit": w2kStatusGeneralNetCrit,
       "w2kStatusGeneralRegCount": w2kStatusGeneralRegCount,
       "w2kStatusGeneralRegWarn": w2kStatusGeneralRegWarn,
       "w2kStatusGeneralRegCrit": w2kStatusGeneralRegCrit,
       "w2kStatusCpuGroup": w2kStatusCpuGroup,
       "w2kStatusCpuTotalLoadValue": w2kStatusCpuTotalLoadValue,
       "w2kStatusCpuTotalLoadLagValue": w2kStatusCpuTotalLoadLagValue,
       "w2kStatusCpuTotalLoadLag": w2kStatusCpuTotalLoadLag,
       "w2kStatusCpuTotalLoadWarn": w2kStatusCpuTotalLoadWarn,
       "w2kStatusCpuTotalLoadCrit": w2kStatusCpuTotalLoadCrit,
       "w2kStatusCpuTotalLoadMonitor": w2kStatusCpuTotalLoadMonitor,
       "w2kStatusCpuTotalLoadStatus": w2kStatusCpuTotalLoadStatus,
       "w2kStatusCpuTotalCallBackRef": w2kStatusCpuTotalCallBackRef,
       "w2kStatusCpuCount": w2kStatusCpuCount,
       "w2kStatusCpuTable": w2kStatusCpuTable,
       "w2kStatusCpuEntry": w2kStatusCpuEntry,
       "w2kStatusCpuName": w2kStatusCpuName,
       "w2kStatusCpuType": w2kStatusCpuType,
       "w2kStatusCpuAggStatus": w2kStatusCpuAggStatus,
       "w2kStatusCpuLoadValue": w2kStatusCpuLoadValue,
       "w2kStatusCpuLoadLagValue": w2kStatusCpuLoadLagValue,
       "w2kStatusCpuLoadLag": w2kStatusCpuLoadLag,
       "w2kStatusCpuLoadWarn": w2kStatusCpuLoadWarn,
       "w2kStatusCpuLoadCrit": w2kStatusCpuLoadCrit,
       "w2kStatusCpuLoadMonitor": w2kStatusCpuLoadMonitor,
       "w2kStatusCpuLoadStatus": w2kStatusCpuLoadStatus,
       "w2kStatusCpuLossAction": w2kStatusCpuLossAction,
       "w2kStatusCpuLossStatus": w2kStatusCpuLossStatus,
       "w2kStatusCpuCallBackRef": w2kStatusCpuCallBackRef,
       "w2kStatusMemGroup": w2kStatusMemGroup,
       "w2kStatusMemVirtTotal": w2kStatusMemVirtTotal,
       "w2kStatusMemVirtValue": w2kStatusMemVirtValue,
       "w2kStatusMemVirtLagValue": w2kStatusMemVirtLagValue,
       "w2kStatusMemVirtLag": w2kStatusMemVirtLag,
       "w2kStatusMemVirtWarnValue": w2kStatusMemVirtWarnValue,
       "w2kStatusMemVirtCritValue": w2kStatusMemVirtCritValue,
       "w2kStatusMemVirtWarn": w2kStatusMemVirtWarn,
       "w2kStatusMemVirtCrit": w2kStatusMemVirtCrit,
       "w2kStatusMemVirtMonitor": w2kStatusMemVirtMonitor,
       "w2kStatusMemVirtStatus": w2kStatusMemVirtStatus,
       "w2kStatusMemPhysTotal": w2kStatusMemPhysTotal,
       "w2kStatusMemPhysValue": w2kStatusMemPhysValue,
       "w2kStatusMemPhysLagValue": w2kStatusMemPhysLagValue,
       "w2kStatusMemPhysLag": w2kStatusMemPhysLag,
       "w2kStatusMemPhysWarnValue": w2kStatusMemPhysWarnValue,
       "w2kStatusMemPhysCritValue": w2kStatusMemPhysCritValue,
       "w2kStatusMemPhysWarn": w2kStatusMemPhysWarn,
       "w2kStatusMemPhysCrit": w2kStatusMemPhysCrit,
       "w2kStatusMemPhysMonitor": w2kStatusMemPhysMonitor,
       "w2kStatusMemPhysStatus": w2kStatusMemPhysStatus,
       "w2kStatusMemPageTotal": w2kStatusMemPageTotal,
       "w2kStatusMemPageValue": w2kStatusMemPageValue,
       "w2kStatusMemPageLagValue": w2kStatusMemPageLagValue,
       "w2kStatusMemPageLag": w2kStatusMemPageLag,
       "w2kStatusMemPageWarnValue": w2kStatusMemPageWarnValue,
       "w2kStatusMemPageCritValue": w2kStatusMemPageCritValue,
       "w2kStatusMemPageWarn": w2kStatusMemPageWarn,
       "w2kStatusMemPageCrit": w2kStatusMemPageCrit,
       "w2kStatusMemPageMonitor": w2kStatusMemPageMonitor,
       "w2kStatusMemPageStatus": w2kStatusMemPageStatus,
       "w2kStatusMemCallBackRef": w2kStatusMemCallBackRef,
       "w2kStatusLVolGroup": w2kStatusLVolGroup,
       "w2kStatusLVolCount": w2kStatusLVolCount,
       "w2kStatusLVolTable": w2kStatusLVolTable,
       "w2kStatusLVolEntry": w2kStatusLVolEntry,
       "w2kStatusLVolName": w2kStatusLVolName,
       "w2kStatusLVolDescription": w2kStatusLVolDescription,
       "w2kStatusLVolMounts": w2kStatusLVolMounts,
       "w2kStatusLVolInfo": w2kStatusLVolInfo,
       "w2kStatusLVolAutoWatcherName": w2kStatusLVolAutoWatcherName,
       "w2kStatusLVolAggLagValue": w2kStatusLVolAggLagValue,
       "w2kStatusLVolAggLag": w2kStatusLVolAggLag,
       "w2kStatusLVolAggStatus": w2kStatusLVolAggStatus,
       "w2kStatusLVolSizeTotal": w2kStatusLVolSizeTotal,
       "w2kStatusLVolSizeValue": w2kStatusLVolSizeValue,
       "w2kStatusLVolSizeWarnValue": w2kStatusLVolSizeWarnValue,
       "w2kStatusLVolSizeCritValue": w2kStatusLVolSizeCritValue,
       "w2kStatusLVolSizeWarn": w2kStatusLVolSizeWarn,
       "w2kStatusLVolSizeCrit": w2kStatusLVolSizeCrit,
       "w2kStatusLVolSizeMonitor": w2kStatusLVolSizeMonitor,
       "w2kStatusLVolSizeStatus": w2kStatusLVolSizeStatus,
       "w2kStatusLVolSizeDValue": w2kStatusLVolSizeDValue,
       "w2kStatusLVolSizeDWarnValue": w2kStatusLVolSizeDWarnValue,
       "w2kStatusLVolSizeDCritValue": w2kStatusLVolSizeDCritValue,
       "w2kStatusLVolSizeDWarn": w2kStatusLVolSizeDWarn,
       "w2kStatusLVolSizeDCrit": w2kStatusLVolSizeDCrit,
       "w2kStatusLVolSizeDMonitor": w2kStatusLVolSizeDMonitor,
       "w2kStatusLVolSizeDStatus": w2kStatusLVolSizeDStatus,
       "w2kStatusLVolTPutValue": w2kStatusLVolTPutValue,
       "w2kStatusLVolTPutWarn": w2kStatusLVolTPutWarn,
       "w2kStatusLVolTPutCrit": w2kStatusLVolTPutCrit,
       "w2kStatusLVolTPutMonitor": w2kStatusLVolTPutMonitor,
       "w2kStatusLVolTPutStatus": w2kStatusLVolTPutStatus,
       "w2kStatusLVolFragValue": w2kStatusLVolFragValue,
       "w2kStatusLVolFragWarn": w2kStatusLVolFragWarn,
       "w2kStatusLVolFragCrit": w2kStatusLVolFragCrit,
       "w2kStatusLVolFragMonitor": w2kStatusLVolFragMonitor,
       "w2kStatusLVolFragStatus": w2kStatusLVolFragStatus,
       "w2kStatusLVolLossAction": w2kStatusLVolLossAction,
       "w2kStatusLVolLossStatus": w2kStatusLVolLossStatus,
       "w2kStatusLVolCallBackRef": w2kStatusLVolCallBackRef,
       "w2kStatusLVolButton": w2kStatusLVolButton,
       "w2kStatusMntGroup": w2kStatusMntGroup,
       "w2kStatusMntCount": w2kStatusMntCount,
       "w2kStatusMntTable": w2kStatusMntTable,
       "w2kStatusMntEntry": w2kStatusMntEntry,
       "w2kStatusMntName": w2kStatusMntName,
       "w2kStatusMntDescription": w2kStatusMntDescription,
       "w2kStatusMntAutoWatcherName": w2kStatusMntAutoWatcherName,
       "w2kStatusMntAggLagValue": w2kStatusMntAggLagValue,
       "w2kStatusMntAggLag": w2kStatusMntAggLag,
       "w2kStatusMntAggStatus": w2kStatusMntAggStatus,
       "w2kStatusMntRelToValue": w2kStatusMntRelToValue,
       "w2kStatusMntRelToRef": w2kStatusMntRelToRef,
       "w2kStatusMntRelToMonitor": w2kStatusMntRelToMonitor,
       "w2kStatusMntRelToStatus": w2kStatusMntRelToStatus,
       "w2kStatusMntLossAction": w2kStatusMntLossAction,
       "w2kStatusMntLossStatus": w2kStatusMntLossStatus,
       "w2kStatusMntCallBackRef": w2kStatusMntCallBackRef,
       "w2kStatusMntButton": w2kStatusMntButton,
       "w2kStatusDfsGroup": w2kStatusDfsGroup,
       "w2kStatusDfsCount": w2kStatusDfsCount,
       "w2kStatusDfsTable": w2kStatusDfsTable,
       "w2kStatusDfsEntry": w2kStatusDfsEntry,
       "w2kStatusDfsName": w2kStatusDfsName,
       "w2kStatusDfsDescription": w2kStatusDfsDescription,
       "w2kStatusDfsIds": w2kStatusDfsIds,
       "w2kStatusDfsAutoWatcherName": w2kStatusDfsAutoWatcherName,
       "w2kStatusDfsAggLagValue": w2kStatusDfsAggLagValue,
       "w2kStatusDfsAggLag": w2kStatusDfsAggLag,
       "w2kStatusDfsAggStatus": w2kStatusDfsAggStatus,
       "w2kStatusDfsReplicaTotal": w2kStatusDfsReplicaTotal,
       "w2kStatusDfsReplicaValue": w2kStatusDfsReplicaValue,
       "w2kStatusDfsReplicaWarn": w2kStatusDfsReplicaWarn,
       "w2kStatusDfsReplicaCrit": w2kStatusDfsReplicaCrit,
       "w2kStatusDfsReplicaMonitor": w2kStatusDfsReplicaMonitor,
       "w2kStatusDfsReplicaStatus": w2kStatusDfsReplicaStatus,
       "w2kStatusDfsLossAction": w2kStatusDfsLossAction,
       "w2kStatusDfsLossStatus": w2kStatusDfsLossStatus,
       "w2kStatusDfsCallBackRef": w2kStatusDfsCallBackRef,
       "w2kStatusDfsButton": w2kStatusDfsButton,
       "w2kStatusQuotGroup": w2kStatusQuotGroup,
       "w2kStatusQuotCount": w2kStatusQuotCount,
       "w2kStatusQuotTable": w2kStatusQuotTable,
       "w2kStatusQuotEntry": w2kStatusQuotEntry,
       "w2kStatusQuotLVolName": w2kStatusQuotLVolName,
       "w2kStatusQuotUserName": w2kStatusQuotUserName,
       "w2kStatusQuotDescription": w2kStatusQuotDescription,
       "w2kStatusQuotAggLagValue": w2kStatusQuotAggLagValue,
       "w2kStatusQuotAggLag": w2kStatusQuotAggLag,
       "w2kStatusQuotAggStatus": w2kStatusQuotAggStatus,
       "w2kStatusQuotExist": w2kStatusQuotExist,
       "w2kStatusQuotExistMonitor": w2kStatusQuotExistMonitor,
       "w2kStatusQuotExistStatus": w2kStatusQuotExistStatus,
       "w2kStatusQuotSizeValue": w2kStatusQuotSizeValue,
       "w2kStatusQuotSizeWarn": w2kStatusQuotSizeWarn,
       "w2kStatusQuotSizeCrit": w2kStatusQuotSizeCrit,
       "w2kStatusQuotSizeMonitor": w2kStatusQuotSizeMonitor,
       "w2kStatusQuotSizeStatus": w2kStatusQuotSizeStatus,
       "w2kStatusQuotCallBackRef": w2kStatusQuotCallBackRef,
       "w2kStatusQuotButton": w2kStatusQuotButton,
       "w2kStatusDirGroup": w2kStatusDirGroup,
       "w2kStatusDirCount": w2kStatusDirCount,
       "w2kStatusDirTable": w2kStatusDirTable,
       "w2kStatusDirEntry": w2kStatusDirEntry,
       "w2kStatusDirName": w2kStatusDirName,
       "w2kStatusDirDescription": w2kStatusDirDescription,
       "w2kStatusDirAggLagValue": w2kStatusDirAggLagValue,
       "w2kStatusDirAggLag": w2kStatusDirAggLag,
       "w2kStatusDirAggStatus": w2kStatusDirAggStatus,
       "w2kStatusDirExist": w2kStatusDirExist,
       "w2kStatusDirExistMonitor": w2kStatusDirExistMonitor,
       "w2kStatusDirExistStatus": w2kStatusDirExistStatus,
       "w2kStatusDirTimeValue": w2kStatusDirTimeValue,
       "w2kStatusDirTimeRef": w2kStatusDirTimeRef,
       "w2kStatusDirTimeMonitor": w2kStatusDirTimeMonitor,
       "w2kStatusDirTimeStatus": w2kStatusDirTimeStatus,
       "w2kStatusDirSizeRef": w2kStatusDirSizeRef,
       "w2kStatusDirSizeValue": w2kStatusDirSizeValue,
       "w2kStatusDirSizeWarnValue": w2kStatusDirSizeWarnValue,
       "w2kStatusDirSizeCritValue": w2kStatusDirSizeCritValue,
       "w2kStatusDirSizeWarn": w2kStatusDirSizeWarn,
       "w2kStatusDirSizeCrit": w2kStatusDirSizeCrit,
       "w2kStatusDirSizeMonitor": w2kStatusDirSizeMonitor,
       "w2kStatusDirSizeStatus": w2kStatusDirSizeStatus,
       "w2kStatusDirSizeDValue": w2kStatusDirSizeDValue,
       "w2kStatusDirSizeDWarnValue": w2kStatusDirSizeDWarnValue,
       "w2kStatusDirSizeDCritValue": w2kStatusDirSizeDCritValue,
       "w2kStatusDirSizeDWarn": w2kStatusDirSizeDWarn,
       "w2kStatusDirSizeDCrit": w2kStatusDirSizeDCrit,
       "w2kStatusDirSizeDMonitor": w2kStatusDirSizeDMonitor,
       "w2kStatusDirSizeDStatus": w2kStatusDirSizeDStatus,
       "w2kStatusDirEntryValue": w2kStatusDirEntryValue,
       "w2kStatusDirEntryWarn": w2kStatusDirEntryWarn,
       "w2kStatusDirEntryCrit": w2kStatusDirEntryCrit,
       "w2kStatusDirEntryMonitor": w2kStatusDirEntryMonitor,
       "w2kStatusDirEntryStatus": w2kStatusDirEntryStatus,
       "w2kStatusDirCallBackRef": w2kStatusDirCallBackRef,
       "w2kStatusDirButton": w2kStatusDirButton,
       "w2kStatusFileGroup": w2kStatusFileGroup,
       "w2kStatusFileCount": w2kStatusFileCount,
       "w2kStatusFileTable": w2kStatusFileTable,
       "w2kStatusFileEntry": w2kStatusFileEntry,
       "w2kStatusFileName": w2kStatusFileName,
       "w2kStatusFileDescription": w2kStatusFileDescription,
       "w2kStatusFileAggLagValue": w2kStatusFileAggLagValue,
       "w2kStatusFileAggLag": w2kStatusFileAggLag,
       "w2kStatusFileAggStatus": w2kStatusFileAggStatus,
       "w2kStatusFileExist": w2kStatusFileExist,
       "w2kStatusFileExistMonitor": w2kStatusFileExistMonitor,
       "w2kStatusFileExistStatus": w2kStatusFileExistStatus,
       "w2kStatusFileTimeValue": w2kStatusFileTimeValue,
       "w2kStatusFileTimeRef": w2kStatusFileTimeRef,
       "w2kStatusFileTimeMonitor": w2kStatusFileTimeMonitor,
       "w2kStatusFileTimeStatus": w2kStatusFileTimeStatus,
       "w2kStatusFileSizeRef": w2kStatusFileSizeRef,
       "w2kStatusFileSizeValue": w2kStatusFileSizeValue,
       "w2kStatusFileSizeWarnValue": w2kStatusFileSizeWarnValue,
       "w2kStatusFileSizeCritValue": w2kStatusFileSizeCritValue,
       "w2kStatusFileSizeWarn": w2kStatusFileSizeWarn,
       "w2kStatusFileSizeCrit": w2kStatusFileSizeCrit,
       "w2kStatusFileSizeMonitor": w2kStatusFileSizeMonitor,
       "w2kStatusFileSizeStatus": w2kStatusFileSizeStatus,
       "w2kStatusFileSizeDValue": w2kStatusFileSizeDValue,
       "w2kStatusFileSizeDWarnValue": w2kStatusFileSizeDWarnValue,
       "w2kStatusFileSizeDCritValue": w2kStatusFileSizeDCritValue,
       "w2kStatusFileSizeDWarn": w2kStatusFileSizeDWarn,
       "w2kStatusFileSizeDCrit": w2kStatusFileSizeDCrit,
       "w2kStatusFileSizeDMonitor": w2kStatusFileSizeDMonitor,
       "w2kStatusFileSizeDStatus": w2kStatusFileSizeDStatus,
       "w2kStatusFileCallBackRef": w2kStatusFileCallBackRef,
       "w2kStatusFileButton": w2kStatusFileButton,
       "w2kStatusProcGroup": w2kStatusProcGroup,
       "w2kStatusProcCount": w2kStatusProcCount,
       "w2kStatusProcTable": w2kStatusProcTable,
       "w2kStatusProcEntry": w2kStatusProcEntry,
       "w2kStatusProcProcName": w2kStatusProcProcName,
       "w2kStatusProcPathName": w2kStatusProcPathName,
       "w2kStatusProcUserName": w2kStatusProcUserName,
       "w2kStatusProcDescription": w2kStatusProcDescription,
       "w2kStatusProcIds": w2kStatusProcIds,
       "w2kStatusProcAggLagValue": w2kStatusProcAggLagValue,
       "w2kStatusProcAggLag": w2kStatusProcAggLag,
       "w2kStatusProcAggStatus": w2kStatusProcAggStatus,
       "w2kStatusProcInstValue": w2kStatusProcInstValue,
       "w2kStatusProcInstMin": w2kStatusProcInstMin,
       "w2kStatusProcInstMax": w2kStatusProcInstMax,
       "w2kStatusProcInstMonitor": w2kStatusProcInstMonitor,
       "w2kStatusProcInstStatus": w2kStatusProcInstStatus,
       "w2kStatusProcChildMinValue": w2kStatusProcChildMinValue,
       "w2kStatusProcChildMaxValue": w2kStatusProcChildMaxValue,
       "w2kStatusProcChildMin": w2kStatusProcChildMin,
       "w2kStatusProcChildMax": w2kStatusProcChildMax,
       "w2kStatusProcChildMonitor": w2kStatusProcChildMonitor,
       "w2kStatusProcChildStatus": w2kStatusProcChildStatus,
       "w2kStatusProcThreadMinValue": w2kStatusProcThreadMinValue,
       "w2kStatusProcThreadMaxValue": w2kStatusProcThreadMaxValue,
       "w2kStatusProcThreadMin": w2kStatusProcThreadMin,
       "w2kStatusProcThreadMax": w2kStatusProcThreadMax,
       "w2kStatusProcThreadMonitor": w2kStatusProcThreadMonitor,
       "w2kStatusProcThreadStatus": w2kStatusProcThreadStatus,
       "w2kStatusProcMemoryValue": w2kStatusProcMemoryValue,
       "w2kStatusProcMemoryWarn": w2kStatusProcMemoryWarn,
       "w2kStatusProcMemoryCrit": w2kStatusProcMemoryCrit,
       "w2kStatusProcMemoryMonitor": w2kStatusProcMemoryMonitor,
       "w2kStatusProcMemoryStatus": w2kStatusProcMemoryStatus,
       "w2kStatusProcCpuValue": w2kStatusProcCpuValue,
       "w2kStatusProcCpuWarn": w2kStatusProcCpuWarn,
       "w2kStatusProcCpuCrit": w2kStatusProcCpuCrit,
       "w2kStatusProcCpuMonitor": w2kStatusProcCpuMonitor,
       "w2kStatusProcCpuStatus": w2kStatusProcCpuStatus,
       "w2kStatusProcCallBackRef": w2kStatusProcCallBackRef,
       "w2kStatusProcButton": w2kStatusProcButton,
       "w2kStatusSrvcGroup": w2kStatusSrvcGroup,
       "w2kStatusSrvcCount": w2kStatusSrvcCount,
       "w2kStatusSrvcTable": w2kStatusSrvcTable,
       "w2kStatusSrvcEntry": w2kStatusSrvcEntry,
       "w2kStatusSrvcName": w2kStatusSrvcName,
       "w2kStatusSrvcDescription": w2kStatusSrvcDescription,
       "w2kStatusSrvcDescr": w2kStatusSrvcDescr,
       "w2kStatusSrvcAutoWatcherName": w2kStatusSrvcAutoWatcherName,
       "w2kStatusSrvcAggLagValue": w2kStatusSrvcAggLagValue,
       "w2kStatusSrvcAggLag": w2kStatusSrvcAggLag,
       "w2kStatusSrvcAggStatus": w2kStatusSrvcAggStatus,
       "w2kStatusSrvcExist": w2kStatusSrvcExist,
       "w2kStatusSrvcExistMonitor": w2kStatusSrvcExistMonitor,
       "w2kStatusSrvcExistStatus": w2kStatusSrvcExistStatus,
       "w2kStatusSrvcActiveValue": w2kStatusSrvcActiveValue,
       "w2kStatusSrvcActive": w2kStatusSrvcActive,
       "w2kStatusSrvcActiveMonitor": w2kStatusSrvcActiveMonitor,
       "w2kStatusSrvcActiveStatus": w2kStatusSrvcActiveStatus,
       "w2kStatusSrvcCallBackRef": w2kStatusSrvcCallBackRef,
       "w2kStatusSrvcButton": w2kStatusSrvcButton,
       "w2kStatusJobGroup": w2kStatusJobGroup,
       "w2kStatusJobCount": w2kStatusJobCount,
       "w2kStatusJobTable": w2kStatusJobTable,
       "w2kStatusJobEntry": w2kStatusJobEntry,
       "w2kStatusJobName": w2kStatusJobName,
       "w2kStatusJobDescription": w2kStatusJobDescription,
       "w2kStatusJobAggLagValue": w2kStatusJobAggLagValue,
       "w2kStatusJobAggLag": w2kStatusJobAggLag,
       "w2kStatusJobAggStatus": w2kStatusJobAggStatus,
       "w2kStatusJobExist": w2kStatusJobExist,
       "w2kStatusJobExistMonitor": w2kStatusJobExistMonitor,
       "w2kStatusJobExistStatus": w2kStatusJobExistStatus,
       "w2kStatusJobProcessValue": w2kStatusJobProcessValue,
       "w2kStatusJobProcessMin": w2kStatusJobProcessMin,
       "w2kStatusJobProcessMax": w2kStatusJobProcessMax,
       "w2kStatusJobProcessMonitor": w2kStatusJobProcessMonitor,
       "w2kStatusJobProcessStatus": w2kStatusJobProcessStatus,
       "w2kStatusJobCpuValue": w2kStatusJobCpuValue,
       "w2kStatusJobCpuWarn": w2kStatusJobCpuWarn,
       "w2kStatusJobCpuCrit": w2kStatusJobCpuCrit,
       "w2kStatusJobCpuMonitor": w2kStatusJobCpuMonitor,
       "w2kStatusJobCpuStatus": w2kStatusJobCpuStatus,
       "w2kStatusJobCallBackRef": w2kStatusJobCallBackRef,
       "w2kStatusJobButton": w2kStatusJobButton,
       "w2kStatusSessGroup": w2kStatusSessGroup,
       "w2kStatusSessCount": w2kStatusSessCount,
       "w2kStatusSessTable": w2kStatusSessTable,
       "w2kStatusSessEntry": w2kStatusSessEntry,
       "w2kStatusSessClientName": w2kStatusSessClientName,
       "w2kStatusSessUserName": w2kStatusSessUserName,
       "w2kStatusSessDescription": w2kStatusSessDescription,
       "w2kStatusSessIds": w2kStatusSessIds,
       "w2kStatusSessAggLagValue": w2kStatusSessAggLagValue,
       "w2kStatusSessAggLag": w2kStatusSessAggLag,
       "w2kStatusSessAggStatus": w2kStatusSessAggStatus,
       "w2kStatusSessInstValue": w2kStatusSessInstValue,
       "w2kStatusSessInstMin": w2kStatusSessInstMin,
       "w2kStatusSessInstMax": w2kStatusSessInstMax,
       "w2kStatusSessInstMonitor": w2kStatusSessInstMonitor,
       "w2kStatusSessInstStatus": w2kStatusSessInstStatus,
       "w2kStatusSessMemoryValue": w2kStatusSessMemoryValue,
       "w2kStatusSessMemoryWarn": w2kStatusSessMemoryWarn,
       "w2kStatusSessMemoryCrit": w2kStatusSessMemoryCrit,
       "w2kStatusSessMemoryMonitor": w2kStatusSessMemoryMonitor,
       "w2kStatusSessMemoryStatus": w2kStatusSessMemoryStatus,
       "w2kStatusSessCpuValue": w2kStatusSessCpuValue,
       "w2kStatusSessCpuWarn": w2kStatusSessCpuWarn,
       "w2kStatusSessCpuCrit": w2kStatusSessCpuCrit,
       "w2kStatusSessCpuMonitor": w2kStatusSessCpuMonitor,
       "w2kStatusSessCpuStatus": w2kStatusSessCpuStatus,
       "w2kStatusSessCallBackRef": w2kStatusSessCallBackRef,
       "w2kStatusSessButton": w2kStatusSessButton,
       "w2kStatusPrnGroup": w2kStatusPrnGroup,
       "w2kStatusPrnCount": w2kStatusPrnCount,
       "w2kStatusPrnTable": w2kStatusPrnTable,
       "w2kStatusPrnEntry": w2kStatusPrnEntry,
       "w2kStatusPrnName": w2kStatusPrnName,
       "w2kStatusPrnDescription": w2kStatusPrnDescription,
       "w2kStatusPrnAutoWatcherName": w2kStatusPrnAutoWatcherName,
       "w2kStatusPrnAggLagValue": w2kStatusPrnAggLagValue,
       "w2kStatusPrnAggLag": w2kStatusPrnAggLag,
       "w2kStatusPrnAggStatus": w2kStatusPrnAggStatus,
       "w2kStatusPrnEventDescr": w2kStatusPrnEventDescr,
       "w2kStatusPrnEventMonitor": w2kStatusPrnEventMonitor,
       "w2kStatusPrnEventStatus": w2kStatusPrnEventStatus,
       "w2kStatusPrnQueueValue": w2kStatusPrnQueueValue,
       "w2kStatusPrnQueueWarn": w2kStatusPrnQueueWarn,
       "w2kStatusPrnQueueCrit": w2kStatusPrnQueueCrit,
       "w2kStatusPrnQueueMonitor": w2kStatusPrnQueueMonitor,
       "w2kStatusPrnQueueStatus": w2kStatusPrnQueueStatus,
       "w2kStatusPrnLossAction": w2kStatusPrnLossAction,
       "w2kStatusPrnLossStatus": w2kStatusPrnLossStatus,
       "w2kStatusPrnCallBackRef": w2kStatusPrnCallBackRef,
       "w2kStatusPrnButton": w2kStatusPrnButton,
       "w2kStatusNetGroup": w2kStatusNetGroup,
       "w2kStatusNetTotalAggLagValue": w2kStatusNetTotalAggLagValue,
       "w2kStatusNetTotalAggLag": w2kStatusNetTotalAggLag,
       "w2kStatusNetTotalAggStatus": w2kStatusNetTotalAggStatus,
       "w2kStatusNetTotalInPktValue": w2kStatusNetTotalInPktValue,
       "w2kStatusNetTotalInPktWarn": w2kStatusNetTotalInPktWarn,
       "w2kStatusNetTotalInPktCrit": w2kStatusNetTotalInPktCrit,
       "w2kStatusNetTotalInPktMonitor": w2kStatusNetTotalInPktMonitor,
       "w2kStatusNetTotalInPktStatus": w2kStatusNetTotalInPktStatus,
       "w2kStatusNetTotalOutPktValue": w2kStatusNetTotalOutPktValue,
       "w2kStatusNetTotalOutPktWarn": w2kStatusNetTotalOutPktWarn,
       "w2kStatusNetTotalOutPktCrit": w2kStatusNetTotalOutPktCrit,
       "w2kStatusNetTotalOutPktMonitor": w2kStatusNetTotalOutPktMonitor,
       "w2kStatusNetTotalOutPktStatus": w2kStatusNetTotalOutPktStatus,
       "w2kStatusNetTotalInErrDValue": w2kStatusNetTotalInErrDValue,
       "w2kStatusNetTotalInErrDWarn": w2kStatusNetTotalInErrDWarn,
       "w2kStatusNetTotalInErrDCrit": w2kStatusNetTotalInErrDCrit,
       "w2kStatusNetTotalInErrDMonitor": w2kStatusNetTotalInErrDMonitor,
       "w2kStatusNetTotalInErrDStatus": w2kStatusNetTotalInErrDStatus,
       "w2kStatusNetTotalOutErrDValue": w2kStatusNetTotalOutErrDValue,
       "w2kStatusNetTotalOutErrDWarn": w2kStatusNetTotalOutErrDWarn,
       "w2kStatusNetTotalOutErrDCrit": w2kStatusNetTotalOutErrDCrit,
       "w2kStatusNetTotalOutErrDMonitor": w2kStatusNetTotalOutErrDMonitor,
       "w2kStatusNetTotalOutErrDStatus": w2kStatusNetTotalOutErrDStatus,
       "w2kStatusNetTotalCallBackRef": w2kStatusNetTotalCallBackRef,
       "w2kStatusNetCount": w2kStatusNetCount,
       "w2kStatusNetTable": w2kStatusNetTable,
       "w2kStatusNetEntry": w2kStatusNetEntry,
       "w2kStatusNetName": w2kStatusNetName,
       "w2kStatusNetAggLagValue": w2kStatusNetAggLagValue,
       "w2kStatusNetAggLag": w2kStatusNetAggLag,
       "w2kStatusNetAggStatus": w2kStatusNetAggStatus,
       "w2kStatusNetInPktValue": w2kStatusNetInPktValue,
       "w2kStatusNetInPktWarn": w2kStatusNetInPktWarn,
       "w2kStatusNetInPktCrit": w2kStatusNetInPktCrit,
       "w2kStatusNetInPktMonitor": w2kStatusNetInPktMonitor,
       "w2kStatusNetInPktStatus": w2kStatusNetInPktStatus,
       "w2kStatusNetOutPktValue": w2kStatusNetOutPktValue,
       "w2kStatusNetOutPktWarn": w2kStatusNetOutPktWarn,
       "w2kStatusNetOutPktCrit": w2kStatusNetOutPktCrit,
       "w2kStatusNetOutPktMonitor": w2kStatusNetOutPktMonitor,
       "w2kStatusNetOutPktStatus": w2kStatusNetOutPktStatus,
       "w2kStatusNetInErrDValue": w2kStatusNetInErrDValue,
       "w2kStatusNetInErrDWarn": w2kStatusNetInErrDWarn,
       "w2kStatusNetInErrDCrit": w2kStatusNetInErrDCrit,
       "w2kStatusNetInErrDMonitor": w2kStatusNetInErrDMonitor,
       "w2kStatusNetInErrDStatus": w2kStatusNetInErrDStatus,
       "w2kStatusNetOutErrDValue": w2kStatusNetOutErrDValue,
       "w2kStatusNetOutErrDWarn": w2kStatusNetOutErrDWarn,
       "w2kStatusNetOutErrDCrit": w2kStatusNetOutErrDCrit,
       "w2kStatusNetOutErrDMonitor": w2kStatusNetOutErrDMonitor,
       "w2kStatusNetOutErrDStatus": w2kStatusNetOutErrDStatus,
       "w2kStatusNetLossAction": w2kStatusNetLossAction,
       "w2kStatusNetLossStatus": w2kStatusNetLossStatus,
       "w2kStatusNetCallBackRef": w2kStatusNetCallBackRef,
       "w2kStatusRegGroup": w2kStatusRegGroup,
       "w2kStatusRegCount": w2kStatusRegCount,
       "w2kStatusRegTable": w2kStatusRegTable,
       "w2kStatusRegEntry": w2kStatusRegEntry,
       "w2kStatusRegName": w2kStatusRegName,
       "w2kStatusRegDescription": w2kStatusRegDescription,
       "w2kStatusRegAggLagValue": w2kStatusRegAggLagValue,
       "w2kStatusRegAggLag": w2kStatusRegAggLag,
       "w2kStatusRegAggStatus": w2kStatusRegAggStatus,
       "w2kStatusRegExist": w2kStatusRegExist,
       "w2kStatusRegExistMonitor": w2kStatusRegExistMonitor,
       "w2kStatusRegExistStatus": w2kStatusRegExistStatus,
       "w2kStatusRegValueValue": w2kStatusRegValueValue,
       "w2kStatusRegValueType": w2kStatusRegValueType,
       "w2kStatusRegValueRef": w2kStatusRegValueRef,
       "w2kStatusRegValueCond": w2kStatusRegValueCond,
       "w2kStatusRegValueMonitor": w2kStatusRegValueMonitor,
       "w2kStatusRegValueStatus": w2kStatusRegValueStatus,
       "w2kStatusRegCallBackRef": w2kStatusRegCallBackRef,
       "w2kStatusRegButton": w2kStatusRegButton,
       "w2kAvailableGroup": w2kAvailableGroup,
       "w2kAvailLVolGroup": w2kAvailLVolGroup,
       "w2kAvailLVolRefresh": w2kAvailLVolRefresh,
       "w2kAvailLVolCount": w2kAvailLVolCount,
       "w2kAvailLVolTable": w2kAvailLVolTable,
       "w2kAvailLVolEntry": w2kAvailLVolEntry,
       "w2kAvailLVolName": w2kAvailLVolName,
       "w2kAvailLVolMounts": w2kAvailLVolMounts,
       "w2kAvailLVolInfo": w2kAvailLVolInfo,
       "w2kAvailLVolTime": w2kAvailLVolTime,
       "w2kAvailMntGroup": w2kAvailMntGroup,
       "w2kAvailMntRefresh": w2kAvailMntRefresh,
       "w2kAvailMntCount": w2kAvailMntCount,
       "w2kAvailMntTable": w2kAvailMntTable,
       "w2kAvailMntEntry": w2kAvailMntEntry,
       "w2kAvailMntName": w2kAvailMntName,
       "w2kAvailMntRelTo": w2kAvailMntRelTo,
       "w2kAvailMntTime": w2kAvailMntTime,
       "w2kAvailDfsGroup": w2kAvailDfsGroup,
       "w2kAvailDfsRefresh": w2kAvailDfsRefresh,
       "w2kAvailDfsCount": w2kAvailDfsCount,
       "w2kAvailDfsTable": w2kAvailDfsTable,
       "w2kAvailDfsEntry": w2kAvailDfsEntry,
       "w2kAvailDfsName": w2kAvailDfsName,
       "w2kAvailDfsTime": w2kAvailDfsTime,
       "w2kAvailQuotGroup": w2kAvailQuotGroup,
       "w2kAvailQuotRefresh": w2kAvailQuotRefresh,
       "w2kAvailQuotCount": w2kAvailQuotCount,
       "w2kAvailQuotTable": w2kAvailQuotTable,
       "w2kAvailQuotEntry": w2kAvailQuotEntry,
       "w2kAvailQuotLVolName": w2kAvailQuotLVolName,
       "w2kAvailQuotUserName": w2kAvailQuotUserName,
       "w2kAvailQuotWarnLevel": w2kAvailQuotWarnLevel,
       "w2kAvailQuotLimit": w2kAvailQuotLimit,
       "w2kAvailQuotTime": w2kAvailQuotTime,
       "w2kAvailProcGroup": w2kAvailProcGroup,
       "w2kAvailProcRefresh": w2kAvailProcRefresh,
       "w2kAvailProcCount": w2kAvailProcCount,
       "w2kAvailProcTable": w2kAvailProcTable,
       "w2kAvailProcEntry": w2kAvailProcEntry,
       "w2kAvailProcProcName": w2kAvailProcProcName,
       "w2kAvailProcPathName": w2kAvailProcPathName,
       "w2kAvailProcUserName": w2kAvailProcUserName,
       "w2kAvailProcTime": w2kAvailProcTime,
       "w2kAvailSrvcGroup": w2kAvailSrvcGroup,
       "w2kAvailSrvcRefresh": w2kAvailSrvcRefresh,
       "w2kAvailSrvcCount": w2kAvailSrvcCount,
       "w2kAvailSrvcTable": w2kAvailSrvcTable,
       "w2kAvailSrvcEntry": w2kAvailSrvcEntry,
       "w2kAvailSrvcName": w2kAvailSrvcName,
       "w2kAvailSrvcDescr": w2kAvailSrvcDescr,
       "w2kAvailSrvcTime": w2kAvailSrvcTime,
       "w2kAvailJobGroup": w2kAvailJobGroup,
       "w2kAvailJobRefresh": w2kAvailJobRefresh,
       "w2kAvailJobCount": w2kAvailJobCount,
       "w2kAvailJobTable": w2kAvailJobTable,
       "w2kAvailJobEntry": w2kAvailJobEntry,
       "w2kAvailJobName": w2kAvailJobName,
       "w2kAvailJobTime": w2kAvailJobTime,
       "w2kAvailSessGroup": w2kAvailSessGroup,
       "w2kAvailSessRefresh": w2kAvailSessRefresh,
       "w2kAvailSessCount": w2kAvailSessCount,
       "w2kAvailSessTable": w2kAvailSessTable,
       "w2kAvailSessEntry": w2kAvailSessEntry,
       "w2kAvailSessClientName": w2kAvailSessClientName,
       "w2kAvailSessUserName": w2kAvailSessUserName,
       "w2kAvailSessTime": w2kAvailSessTime,
       "w2kAvailPrnGroup": w2kAvailPrnGroup,
       "w2kAvailPrnRefresh": w2kAvailPrnRefresh,
       "w2kAvailPrnCount": w2kAvailPrnCount,
       "w2kAvailPrnTable": w2kAvailPrnTable,
       "w2kAvailPrnEntry": w2kAvailPrnEntry,
       "w2kAvailPrnName": w2kAvailPrnName,
       "w2kAvailPrnTime": w2kAvailPrnTime,
       "w2kHistoryGroup": w2kHistoryGroup,
       "w2kHistoryCpuCollect": w2kHistoryCpuCollect,
       "w2kHistoryMemCollect": w2kHistoryMemCollect,
       "w2kHistoryLVolCollect": w2kHistoryLVolCollect,
       "w2kHistoryMntCollect": w2kHistoryMntCollect,
       "w2kHistoryDfsCollect": w2kHistoryDfsCollect,
       "w2kHistoryQuotCollect": w2kHistoryQuotCollect,
       "w2kHistoryDirCollect": w2kHistoryDirCollect,
       "w2kHistoryFileCollect": w2kHistoryFileCollect,
       "w2kHistoryProcCollect": w2kHistoryProcCollect,
       "w2kHistorySrvcCollect": w2kHistorySrvcCollect,
       "w2kHistoryJobCollect": w2kHistoryJobCollect,
       "w2kHistorySessCollect": w2kHistorySessCollect,
       "w2kHistoryPrnCollect": w2kHistoryPrnCollect,
       "w2kHistoryNetCollect": w2kHistoryNetCollect,
       "w2kHistoryRegCollect": w2kHistoryRegCollect,
       "w2kHistoryButton": w2kHistoryButton,
       "w2kHistoryMaxEntries": w2kHistoryMaxEntries,
       "w2kHistoryCount": w2kHistoryCount,
       "w2kHistoryTable": w2kHistoryTable,
       "w2kHistoryEntry": w2kHistoryEntry,
       "w2kHistoryTrapName": w2kHistoryTrapName,
       "w2kHistoryTrapNumber": w2kHistoryTrapNumber,
       "w2kHistoryTrapTime": w2kHistoryTrapTime,
       "w2kHistoryTrapVarBind": w2kHistoryTrapVarBind}
)
