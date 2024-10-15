# SNMP MIB module (HUAWEI-SLOG-EUDM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-SLOG-EUDM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:05:55 2024
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

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hwSLOGEudm = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 16, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class FlowLogType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flowLogExport", 2),
          ("flowLogSysLog", 1))
    )



# MIB Managed Objects in the order of their OIDs

_HwSLOG_ObjectIdentity = ObjectIdentity
hwSLOG = _HwSLOG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 16)
)
_HwSLogEudmGlobalCfg_ObjectIdentity = ObjectIdentity
hwSLogEudmGlobalCfg = _HwSLogEudmGlobalCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 16, 2, 1)
)


class _HwSLogEudmAttackLogInterval_Type(Integer32):
    """Custom type hwSLogEudmAttackLogInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwSLogEudmAttackLogInterval_Type.__name__ = "Integer32"
_HwSLogEudmAttackLogInterval_Object = MibScalar
hwSLogEudmAttackLogInterval = _HwSLogEudmAttackLogInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 16, 2, 1, 1),
    _HwSLogEudmAttackLogInterval_Type()
)
hwSLogEudmAttackLogInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSLogEudmAttackLogInterval.setStatus("current")


class _HwSLogEudmFlowLogInterval_Type(Integer32):
    """Custom type hwSLogEudmFlowLogInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwSLogEudmFlowLogInterval_Type.__name__ = "Integer32"
_HwSLogEudmFlowLogInterval_Object = MibScalar
hwSLogEudmFlowLogInterval = _HwSLogEudmFlowLogInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 16, 2, 1, 2),
    _HwSLogEudmFlowLogInterval_Type()
)
hwSLogEudmFlowLogInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSLogEudmFlowLogInterval.setStatus("current")


class _HwSLogEudmStreamLogInterval_Type(Integer32):
    """Custom type hwSLogEudmStreamLogInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwSLogEudmStreamLogInterval_Type.__name__ = "Integer32"
_HwSLogEudmStreamLogInterval_Object = MibScalar
hwSLogEudmStreamLogInterval = _HwSLogEudmStreamLogInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 16, 2, 1, 3),
    _HwSLogEudmStreamLogInterval_Type()
)
hwSLogEudmStreamLogInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSLogEudmStreamLogInterval.setStatus("current")


class _HwSLogEudmFlowLogMode_Type(FlowLogType):
    """Custom type hwSLogEudmFlowLogMode based on FlowLogType"""


_HwSLogEudmFlowLogMode_Object = MibScalar
hwSLogEudmFlowLogMode = _HwSLogEudmFlowLogMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 16, 2, 1, 4),
    _HwSLogEudmFlowLogMode_Type()
)
hwSLogEudmFlowLogMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSLogEudmFlowLogMode.setStatus("current")


class _HwSLogEudmServerIP_Type(IpAddress):
    """Custom type hwSLogEudmServerIP based on IpAddress"""
    defaultValue = 0


_HwSLogEudmServerIP_Object = MibScalar
hwSLogEudmServerIP = _HwSLogEudmServerIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 16, 2, 1, 5),
    _HwSLogEudmServerIP_Type()
)
hwSLogEudmServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSLogEudmServerIP.setStatus("current")


class _HwSLogEudmServerPort_Type(Integer32):
    """Custom type hwSLogEudmServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwSLogEudmServerPort_Type.__name__ = "Integer32"
_HwSLogEudmServerPort_Object = MibScalar
hwSLogEudmServerPort = _HwSLogEudmServerPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 16, 2, 1, 6),
    _HwSLogEudmServerPort_Type()
)
hwSLogEudmServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSLogEudmServerPort.setStatus("current")
_HwSLogInterZoneEnableCfg_ObjectIdentity = ObjectIdentity
hwSLogInterZoneEnableCfg = _HwSLogInterZoneEnableCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 16, 2, 2)
)
_HwSLogEudmFlowLogEnableTable_Object = MibTable
hwSLogEudmFlowLogEnableTable = _HwSLogEudmFlowLogEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 16, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hwSLogEudmFlowLogEnableTable.setStatus("current")
_HwSLogEudmFlowLogEnableEntry_Object = MibTableRow
hwSLogEudmFlowLogEnableEntry = _HwSLogEudmFlowLogEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 16, 2, 2, 1, 1)
)
hwSLogEudmFlowLogEnableEntry.setIndexNames(
    (0, "HUAWEI-SLOG-EUDM-MIB", "hwSLogFlowEnableZoneID1"),
    (0, "HUAWEI-SLOG-EUDM-MIB", "hwSLogFlowEnableZoneID2"),
)
if mibBuilder.loadTexts:
    hwSLogEudmFlowLogEnableEntry.setStatus("current")


class _HwSLogFlowEnableZoneID1_Type(Integer32):
    """Custom type hwSLogFlowEnableZoneID1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HwSLogFlowEnableZoneID1_Type.__name__ = "Integer32"
_HwSLogFlowEnableZoneID1_Object = MibTableColumn
hwSLogFlowEnableZoneID1 = _HwSLogFlowEnableZoneID1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 16, 2, 2, 1, 1, 1),
    _HwSLogFlowEnableZoneID1_Type()
)
hwSLogFlowEnableZoneID1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwSLogFlowEnableZoneID1.setStatus("current")


class _HwSLogFlowEnableZoneID2_Type(Integer32):
    """Custom type hwSLogFlowEnableZoneID2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HwSLogFlowEnableZoneID2_Type.__name__ = "Integer32"
_HwSLogFlowEnableZoneID2_Object = MibTableColumn
hwSLogFlowEnableZoneID2 = _HwSLogFlowEnableZoneID2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 16, 2, 2, 1, 1, 2),
    _HwSLogFlowEnableZoneID2_Type()
)
hwSLogFlowEnableZoneID2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwSLogFlowEnableZoneID2.setStatus("current")
_HwSLogEudmFlowEnableFlag_Type = TruthValue
_HwSLogEudmFlowEnableFlag_Object = MibTableColumn
hwSLogEudmFlowEnableFlag = _HwSLogEudmFlowEnableFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 16, 2, 2, 1, 1, 3),
    _HwSLogEudmFlowEnableFlag_Type()
)
hwSLogEudmFlowEnableFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSLogEudmFlowEnableFlag.setStatus("current")


class _HwSLogEudmEnableHostAcl_Type(Integer32):
    """Custom type hwSLogEudmEnableHostAcl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(2000, 3999),
    )


_HwSLogEudmEnableHostAcl_Type.__name__ = "Integer32"
_HwSLogEudmEnableHostAcl_Object = MibTableColumn
hwSLogEudmEnableHostAcl = _HwSLogEudmEnableHostAcl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 16, 2, 2, 1, 1, 4),
    _HwSLogEudmEnableHostAcl_Type()
)
hwSLogEudmEnableHostAcl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSLogEudmEnableHostAcl.setStatus("current")
_HwSLOGEudmConformance_ObjectIdentity = ObjectIdentity
hwSLOGEudmConformance = _HwSLOGEudmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 16, 2, 3)
)
_HwSLOGEudmCompliance_ObjectIdentity = ObjectIdentity
hwSLOGEudmCompliance = _HwSLOGEudmCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 16, 2, 3, 1)
)
_HwSLOGEudmMibGroups_ObjectIdentity = ObjectIdentity
hwSLOGEudmMibGroups = _HwSLOGEudmMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 16, 2, 3, 2)
)

# Managed Objects groups

hwSLOGEudmGlobalCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 16, 2, 3, 2, 1)
)
hwSLOGEudmGlobalCfgGroup.setObjects(
      *(("HUAWEI-SLOG-EUDM-MIB", "hwSLogEudmAttackLogInterval"),
        ("HUAWEI-SLOG-EUDM-MIB", "hwSLogEudmStreamLogInterval"),
        ("HUAWEI-SLOG-EUDM-MIB", "hwSLogEudmFlowLogMode"),
        ("HUAWEI-SLOG-EUDM-MIB", "hwSLogEudmFlowLogInterval"),
        ("HUAWEI-SLOG-EUDM-MIB", "hwSLogEudmServerIP"),
        ("HUAWEI-SLOG-EUDM-MIB", "hwSLogEudmServerPort"))
)
if mibBuilder.loadTexts:
    hwSLOGEudmGlobalCfgGroup.setStatus("current")

hwSLOGEudmFlowLogEnableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 16, 2, 3, 2, 2)
)
hwSLOGEudmFlowLogEnableGroup.setObjects(
      *(("HUAWEI-SLOG-EUDM-MIB", "hwSLogEudmFlowEnableFlag"),
        ("HUAWEI-SLOG-EUDM-MIB", "hwSLogEudmEnableHostAcl"))
)
if mibBuilder.loadTexts:
    hwSLOGEudmFlowLogEnableGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-SLOG-EUDM-MIB",
    **{"FlowLogType": FlowLogType,
       "hwSLOG": hwSLOG,
       "hwSLOGEudm": hwSLOGEudm,
       "hwSLogEudmGlobalCfg": hwSLogEudmGlobalCfg,
       "hwSLogEudmAttackLogInterval": hwSLogEudmAttackLogInterval,
       "hwSLogEudmFlowLogInterval": hwSLogEudmFlowLogInterval,
       "hwSLogEudmStreamLogInterval": hwSLogEudmStreamLogInterval,
       "hwSLogEudmFlowLogMode": hwSLogEudmFlowLogMode,
       "hwSLogEudmServerIP": hwSLogEudmServerIP,
       "hwSLogEudmServerPort": hwSLogEudmServerPort,
       "hwSLogInterZoneEnableCfg": hwSLogInterZoneEnableCfg,
       "hwSLogEudmFlowLogEnableTable": hwSLogEudmFlowLogEnableTable,
       "hwSLogEudmFlowLogEnableEntry": hwSLogEudmFlowLogEnableEntry,
       "hwSLogFlowEnableZoneID1": hwSLogFlowEnableZoneID1,
       "hwSLogFlowEnableZoneID2": hwSLogFlowEnableZoneID2,
       "hwSLogEudmFlowEnableFlag": hwSLogEudmFlowEnableFlag,
       "hwSLogEudmEnableHostAcl": hwSLogEudmEnableHostAcl,
       "hwSLOGEudmConformance": hwSLOGEudmConformance,
       "hwSLOGEudmCompliance": hwSLOGEudmCompliance,
       "hwSLOGEudmMibGroups": hwSLOGEudmMibGroups,
       "hwSLOGEudmGlobalCfgGroup": hwSLOGEudmGlobalCfgGroup,
       "hwSLOGEudmFlowLogEnableGroup": hwSLOGEudmFlowLogEnableGroup}
)
