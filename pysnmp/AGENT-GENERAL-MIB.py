# SNMP MIB module (AGENT-GENERAL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AGENT-GENERAL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:34:53 2024
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

(AgentNotifyLevel,
 dlink_common_mgmt) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "AgentNotifyLevel",
    "dlink-common-mgmt")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

agentGeneralMgmt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 1)
)


# Types definitions



class UnitList(OctetString):
    """Custom type UnitList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )




# TEXTUAL-CONVENTIONS



class Ipv6Address(OctetString, TextualConvention):
    status = "current"
    displayHint = "2x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )



# MIB Managed Objects in the order of their OIDs

_AgentBasicInfo_ObjectIdentity = ObjectIdentity
agentBasicInfo = _AgentBasicInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 1)
)


class _AgentMgmtProtocolCapability_Type(Integer32):
    """Custom type agentMgmtProtocolCapability based on Integer32"""
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
        *(("other", 1),
          ("snmp-ip", 2),
          ("snmp-ip-ipx", 4),
          ("snmp-ipx", 3))
    )


_AgentMgmtProtocolCapability_Type.__name__ = "Integer32"
_AgentMgmtProtocolCapability_Object = MibScalar
agentMgmtProtocolCapability = _AgentMgmtProtocolCapability_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 1, 1),
    _AgentMgmtProtocolCapability_Type()
)
agentMgmtProtocolCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMgmtProtocolCapability.setStatus("current")
_AgentMibCapabilityTable_Object = MibTable
agentMibCapabilityTable = _AgentMibCapabilityTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 1, 2)
)
if mibBuilder.loadTexts:
    agentMibCapabilityTable.setStatus("current")
_AgentMibCapabilityEntry_Object = MibTableRow
agentMibCapabilityEntry = _AgentMibCapabilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 1, 2, 1)
)
agentMibCapabilityEntry.setIndexNames(
    (0, "AGENT-GENERAL-MIB", "agentMibCapabilityIndex"),
)
if mibBuilder.loadTexts:
    agentMibCapabilityEntry.setStatus("current")
_AgentMibCapabilityIndex_Type = Integer32
_AgentMibCapabilityIndex_Object = MibTableColumn
agentMibCapabilityIndex = _AgentMibCapabilityIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 1, 2, 1, 1),
    _AgentMibCapabilityIndex_Type()
)
agentMibCapabilityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMibCapabilityIndex.setStatus("current")


class _AgentMibCapabilityDescr_Type(DisplayString):
    """Custom type agentMibCapabilityDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 35),
    )


_AgentMibCapabilityDescr_Type.__name__ = "DisplayString"
_AgentMibCapabilityDescr_Object = MibTableColumn
agentMibCapabilityDescr = _AgentMibCapabilityDescr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 1, 2, 1, 2),
    _AgentMibCapabilityDescr_Type()
)
agentMibCapabilityDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMibCapabilityDescr.setStatus("current")
_AgentMibCapabilityVersion_Type = Integer32
_AgentMibCapabilityVersion_Object = MibTableColumn
agentMibCapabilityVersion = _AgentMibCapabilityVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 1, 2, 1, 3),
    _AgentMibCapabilityVersion_Type()
)
agentMibCapabilityVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMibCapabilityVersion.setStatus("current")


class _AgentMibCapabilityType_Type(Integer32):
    """Custom type agentMibCapabilityType based on Integer32"""
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
        *(("experiment", 4),
          ("other", 1),
          ("proprietary", 3),
          ("standard", 2))
    )


_AgentMibCapabilityType_Type.__name__ = "Integer32"
_AgentMibCapabilityType_Object = MibTableColumn
agentMibCapabilityType = _AgentMibCapabilityType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 1, 2, 1, 4),
    _AgentMibCapabilityType_Type()
)
agentMibCapabilityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMibCapabilityType.setStatus("current")


class _AgentStatusConsoleInUse_Type(Integer32):
    """Custom type agentStatusConsoleInUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("in-use", 2),
          ("not-in-use", 3),
          ("other", 1))
    )


_AgentStatusConsoleInUse_Type.__name__ = "Integer32"
_AgentStatusConsoleInUse_Object = MibScalar
agentStatusConsoleInUse = _AgentStatusConsoleInUse_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 1, 3),
    _AgentStatusConsoleInUse_Type()
)
agentStatusConsoleInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStatusConsoleInUse.setStatus("current")


class _AgentStatusSaveCfg_Type(Integer32):
    """Custom type agentStatusSaveCfg based on Integer32"""
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
        *(("completed", 3),
          ("failed", 4),
          ("other", 1),
          ("proceeding", 2))
    )


_AgentStatusSaveCfg_Type.__name__ = "Integer32"
_AgentStatusSaveCfg_Object = MibScalar
agentStatusSaveCfg = _AgentStatusSaveCfg_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 1, 4),
    _AgentStatusSaveCfg_Type()
)
agentStatusSaveCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStatusSaveCfg.setStatus("current")


class _AgentStatusFileTransfer_Type(Integer32):
    """Custom type agentStatusFileTransfer based on Integer32"""
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
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("complete", 7),
          ("disk-full", 6),
          ("file-not-found", 5),
          ("in-process", 2),
          ("invalid-file", 3),
          ("memory-full", 10),
          ("not-format", 9),
          ("other", 1),
          ("time-out", 8),
          ("violation", 4))
    )


_AgentStatusFileTransfer_Type.__name__ = "Integer32"
_AgentStatusFileTransfer_Object = MibScalar
agentStatusFileTransfer = _AgentStatusFileTransfer_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 1, 5),
    _AgentStatusFileTransfer_Type()
)
agentStatusFileTransfer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStatusFileTransfer.setStatus("current")
_AgentCPUutilization_ObjectIdentity = ObjectIdentity
agentCPUutilization = _AgentCPUutilization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 1, 6)
)
_AgentCPUutilizationIn5sec_Type = Integer32
_AgentCPUutilizationIn5sec_Object = MibScalar
agentCPUutilizationIn5sec = _AgentCPUutilizationIn5sec_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 1, 6, 1),
    _AgentCPUutilizationIn5sec_Type()
)
agentCPUutilizationIn5sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentCPUutilizationIn5sec.setStatus("current")
_AgentCPUutilizationIn1min_Type = Integer32
_AgentCPUutilizationIn1min_Object = MibScalar
agentCPUutilizationIn1min = _AgentCPUutilizationIn1min_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 1, 6, 2),
    _AgentCPUutilizationIn1min_Type()
)
agentCPUutilizationIn1min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentCPUutilizationIn1min.setStatus("current")
_AgentCPUutilizationIn5min_Type = Integer32
_AgentCPUutilizationIn5min_Object = MibScalar
agentCPUutilizationIn5min = _AgentCPUutilizationIn5min_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 1, 6, 3),
    _AgentCPUutilizationIn5min_Type()
)
agentCPUutilizationIn5min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentCPUutilizationIn5min.setStatus("current")


class _AgentDualImageStatus_Type(Integer32):
    """Custom type agentDualImageStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not-supported", 0),
          ("supported", 1))
    )


_AgentDualImageStatus_Type.__name__ = "Integer32"
_AgentDualImageStatus_Object = MibScalar
agentDualImageStatus = _AgentDualImageStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 1, 7),
    _AgentDualImageStatus_Type()
)
agentDualImageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDualImageStatus.setStatus("current")
_AgentPORTutilizationTable_Object = MibTable
agentPORTutilizationTable = _AgentPORTutilizationTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 1, 8)
)
if mibBuilder.loadTexts:
    agentPORTutilizationTable.setStatus("current")
_AgentPORTutilizationEntry_Object = MibTableRow
agentPORTutilizationEntry = _AgentPORTutilizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 1, 8, 1)
)
agentPORTutilizationEntry.setIndexNames(
    (0, "AGENT-GENERAL-MIB", "agentPORTutilizationProtIndex"),
)
if mibBuilder.loadTexts:
    agentPORTutilizationEntry.setStatus("current")


class _AgentPORTutilizationProtIndex_Type(Integer32):
    """Custom type agentPORTutilizationProtIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AgentPORTutilizationProtIndex_Type.__name__ = "Integer32"
_AgentPORTutilizationProtIndex_Object = MibTableColumn
agentPORTutilizationProtIndex = _AgentPORTutilizationProtIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 1, 8, 1, 1),
    _AgentPORTutilizationProtIndex_Type()
)
agentPORTutilizationProtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPORTutilizationProtIndex.setStatus("current")
_AgentPORTutilizationTX_Type = Integer32
_AgentPORTutilizationTX_Object = MibTableColumn
agentPORTutilizationTX = _AgentPORTutilizationTX_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 1, 8, 1, 2),
    _AgentPORTutilizationTX_Type()
)
agentPORTutilizationTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPORTutilizationTX.setStatus("current")
_AgentPORTutilizationRX_Type = Integer32
_AgentPORTutilizationRX_Object = MibTableColumn
agentPORTutilizationRX = _AgentPORTutilizationRX_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 1, 8, 1, 3),
    _AgentPORTutilizationRX_Type()
)
agentPORTutilizationRX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPORTutilizationRX.setStatus("current")


class _AgentPORTutilizationUtil_Type(Integer32):
    """Custom type agentPORTutilizationUtil based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AgentPORTutilizationUtil_Type.__name__ = "Integer32"
_AgentPORTutilizationUtil_Object = MibTableColumn
agentPORTutilizationUtil = _AgentPORTutilizationUtil_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 1, 8, 1, 4),
    _AgentPORTutilizationUtil_Type()
)
agentPORTutilizationUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPORTutilizationUtil.setStatus("current")
if mibBuilder.loadTexts:
    agentPORTutilizationUtil.setUnits("%")
_AgentDRAMutilizationTable_Object = MibTable
agentDRAMutilizationTable = _AgentDRAMutilizationTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 1, 9)
)
if mibBuilder.loadTexts:
    agentDRAMutilizationTable.setStatus("current")
_AgentDRAMutilizationEntry_Object = MibTableRow
agentDRAMutilizationEntry = _AgentDRAMutilizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 1, 9, 1)
)
agentDRAMutilizationEntry.setIndexNames(
    (0, "AGENT-GENERAL-MIB", "agentDRAMutilizationUnitID"),
)
if mibBuilder.loadTexts:
    agentDRAMutilizationEntry.setStatus("current")
_AgentDRAMutilizationUnitID_Type = Integer32
_AgentDRAMutilizationUnitID_Object = MibTableColumn
agentDRAMutilizationUnitID = _AgentDRAMutilizationUnitID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 1, 9, 1, 1),
    _AgentDRAMutilizationUnitID_Type()
)
agentDRAMutilizationUnitID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDRAMutilizationUnitID.setStatus("current")
_AgentDRAMutilizationTotalDRAM_Type = Integer32
_AgentDRAMutilizationTotalDRAM_Object = MibTableColumn
agentDRAMutilizationTotalDRAM = _AgentDRAMutilizationTotalDRAM_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 1, 9, 1, 2),
    _AgentDRAMutilizationTotalDRAM_Type()
)
agentDRAMutilizationTotalDRAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDRAMutilizationTotalDRAM.setStatus("current")
if mibBuilder.loadTexts:
    agentDRAMutilizationTotalDRAM.setUnits("KB")
_AgentDRAMutilizationUsedDRAM_Type = Integer32
_AgentDRAMutilizationUsedDRAM_Object = MibTableColumn
agentDRAMutilizationUsedDRAM = _AgentDRAMutilizationUsedDRAM_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 1, 9, 1, 3),
    _AgentDRAMutilizationUsedDRAM_Type()
)
agentDRAMutilizationUsedDRAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDRAMutilizationUsedDRAM.setStatus("current")
if mibBuilder.loadTexts:
    agentDRAMutilizationUsedDRAM.setUnits("KB")
_AgentDRAMutilization_Type = Integer32
_AgentDRAMutilization_Object = MibTableColumn
agentDRAMutilization = _AgentDRAMutilization_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 1, 9, 1, 4),
    _AgentDRAMutilization_Type()
)
agentDRAMutilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDRAMutilization.setStatus("current")
_AgentFLASHutilizationTable_Object = MibTable
agentFLASHutilizationTable = _AgentFLASHutilizationTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 1, 10)
)
if mibBuilder.loadTexts:
    agentFLASHutilizationTable.setStatus("current")
_AgentFLASHutilizationEntry_Object = MibTableRow
agentFLASHutilizationEntry = _AgentFLASHutilizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 1, 10, 1)
)
agentFLASHutilizationEntry.setIndexNames(
    (0, "AGENT-GENERAL-MIB", "agentFLASHutilizationUnitID"),
)
if mibBuilder.loadTexts:
    agentFLASHutilizationEntry.setStatus("current")
_AgentFLASHutilizationUnitID_Type = Integer32
_AgentFLASHutilizationUnitID_Object = MibTableColumn
agentFLASHutilizationUnitID = _AgentFLASHutilizationUnitID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 1, 10, 1, 1),
    _AgentFLASHutilizationUnitID_Type()
)
agentFLASHutilizationUnitID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentFLASHutilizationUnitID.setStatus("current")
_AgentFLASHutilizationTotalFLASH_Type = Integer32
_AgentFLASHutilizationTotalFLASH_Object = MibTableColumn
agentFLASHutilizationTotalFLASH = _AgentFLASHutilizationTotalFLASH_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 1, 10, 1, 2),
    _AgentFLASHutilizationTotalFLASH_Type()
)
agentFLASHutilizationTotalFLASH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentFLASHutilizationTotalFLASH.setStatus("current")
if mibBuilder.loadTexts:
    agentFLASHutilizationTotalFLASH.setUnits("KB")
_AgentFLASHutilizationUsedFLASH_Type = Integer32
_AgentFLASHutilizationUsedFLASH_Object = MibTableColumn
agentFLASHutilizationUsedFLASH = _AgentFLASHutilizationUsedFLASH_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 1, 10, 1, 3),
    _AgentFLASHutilizationUsedFLASH_Type()
)
agentFLASHutilizationUsedFLASH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentFLASHutilizationUsedFLASH.setStatus("current")
if mibBuilder.loadTexts:
    agentFLASHutilizationUsedFLASH.setUnits("KB")
_AgentFLASHutilization_Type = Integer32
_AgentFLASHutilization_Object = MibTableColumn
agentFLASHutilization = _AgentFLASHutilization_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 1, 10, 1, 4),
    _AgentFLASHutilization_Type()
)
agentFLASHutilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentFLASHutilization.setStatus("current")


class _AgentStatusReset_Type(Integer32):
    """Custom type agentStatusReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("completed", 2),
          ("failed", 3),
          ("proceeding", 1))
    )


_AgentStatusReset_Type.__name__ = "Integer32"
_AgentStatusReset_Object = MibScalar
agentStatusReset = _AgentStatusReset_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 1, 11),
    _AgentStatusReset_Type()
)
agentStatusReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStatusReset.setStatus("current")
_AgentSerialNumber_Type = DisplayString
_AgentSerialNumber_Object = MibScalar
agentSerialNumber = _AgentSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 1, 12),
    _AgentSerialNumber_Type()
)
agentSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSerialNumber.setStatus("current")
_AgentFirmwareType_Type = DisplayString
_AgentFirmwareType_Object = MibScalar
agentFirmwareType = _AgentFirmwareType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 1, 13),
    _AgentFirmwareType_Type()
)
agentFirmwareType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentFirmwareType.setStatus("current")
_AgentBasicConfig_ObjectIdentity = ObjectIdentity
agentBasicConfig = _AgentBasicConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2)
)
_AgentBscSwFileTable_Object = MibTable
agentBscSwFileTable = _AgentBscSwFileTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 1)
)
if mibBuilder.loadTexts:
    agentBscSwFileTable.setStatus("current")
_AgentBscSwFileEntry_Object = MibTableRow
agentBscSwFileEntry = _AgentBscSwFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 1, 1)
)
agentBscSwFileEntry.setIndexNames(
    (0, "AGENT-GENERAL-MIB", "agentBscSwFileIndex"),
)
if mibBuilder.loadTexts:
    agentBscSwFileEntry.setStatus("current")
_AgentBscSwFileIndex_Type = Integer32
_AgentBscSwFileIndex_Object = MibTableColumn
agentBscSwFileIndex = _AgentBscSwFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 1, 1, 1),
    _AgentBscSwFileIndex_Type()
)
agentBscSwFileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentBscSwFileIndex.setStatus("current")


class _AgentBscSwFileDscr_Type(DisplayString):
    """Custom type agentBscSwFileDscr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AgentBscSwFileDscr_Type.__name__ = "DisplayString"
_AgentBscSwFileDscr_Object = MibTableColumn
agentBscSwFileDscr = _AgentBscSwFileDscr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 1, 1, 2),
    _AgentBscSwFileDscr_Type()
)
agentBscSwFileDscr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentBscSwFileDscr.setStatus("current")
_AgentBscSwFileAddr_Type = IpAddress
_AgentBscSwFileAddr_Object = MibTableColumn
agentBscSwFileAddr = _AgentBscSwFileAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 1, 1, 3),
    _AgentBscSwFileAddr_Type()
)
agentBscSwFileAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentBscSwFileAddr.setStatus("current")


class _AgentBscSwFileTransferType_Type(Integer32):
    """Custom type agentBscSwFileTransferType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("network-load", 2),
          ("other", 1),
          ("out-of-band-load", 3))
    )


_AgentBscSwFileTransferType_Type.__name__ = "Integer32"
_AgentBscSwFileTransferType_Object = MibTableColumn
agentBscSwFileTransferType = _AgentBscSwFileTransferType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 1, 1, 4),
    _AgentBscSwFileTransferType_Type()
)
agentBscSwFileTransferType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentBscSwFileTransferType.setStatus("current")


class _AgentBscSwFile_Type(DisplayString):
    """Custom type agentBscSwFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AgentBscSwFile_Type.__name__ = "DisplayString"
_AgentBscSwFile_Object = MibTableColumn
agentBscSwFile = _AgentBscSwFile_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 1, 1, 5),
    _AgentBscSwFile_Type()
)
agentBscSwFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentBscSwFile.setStatus("current")


class _AgentBscSwFileLocateId_Type(Integer32):
    """Custom type agentBscSwFileLocateId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AgentBscSwFileLocateId_Type.__name__ = "Integer32"
_AgentBscSwFileLocateId_Object = MibTableColumn
agentBscSwFileLocateId = _AgentBscSwFileLocateId_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 1, 1, 6),
    _AgentBscSwFileLocateId_Type()
)
agentBscSwFileLocateId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentBscSwFileLocateId.setStatus("current")


class _AgentBscSwFileLoadType_Type(Integer32):
    """Custom type agentBscSwFileLoadType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("download", 3),
          ("other", 1),
          ("upload", 2))
    )


_AgentBscSwFileLoadType_Type.__name__ = "Integer32"
_AgentBscSwFileLoadType_Object = MibTableColumn
agentBscSwFileLoadType = _AgentBscSwFileLoadType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 1, 1, 7),
    _AgentBscSwFileLoadType_Type()
)
agentBscSwFileLoadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentBscSwFileLoadType.setStatus("current")


class _AgentBscSwFileCtrl_Type(Integer32):
    """Custom type agentBscSwFileCtrl based on Integer32"""
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
        *(("apply", 6),
          ("config-as-bootup", 5),
          ("delete", 4),
          ("inactive", 2),
          ("other", 1),
          ("start", 3))
    )


_AgentBscSwFileCtrl_Type.__name__ = "Integer32"
_AgentBscSwFileCtrl_Object = MibTableColumn
agentBscSwFileCtrl = _AgentBscSwFileCtrl_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 1, 1, 8),
    _AgentBscSwFileCtrl_Type()
)
agentBscSwFileCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentBscSwFileCtrl.setStatus("current")
_AgentBscSwFileBIncrement_Type = TruthValue
_AgentBscSwFileBIncrement_Object = MibTableColumn
agentBscSwFileBIncrement = _AgentBscSwFileBIncrement_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 1, 1, 9),
    _AgentBscSwFileBIncrement_Type()
)
agentBscSwFileBIncrement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentBscSwFileBIncrement.setStatus("current")
_AgentBscSwFileCtrlID_Type = Integer32
_AgentBscSwFileCtrlID_Object = MibTableColumn
agentBscSwFileCtrlID = _AgentBscSwFileCtrlID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 1, 1, 10),
    _AgentBscSwFileCtrlID_Type()
)
agentBscSwFileCtrlID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentBscSwFileCtrlID.setStatus("current")
_AgentBscSwFileCtrlUnitID_Type = UnitList
_AgentBscSwFileCtrlUnitID_Object = MibTableColumn
agentBscSwFileCtrlUnitID = _AgentBscSwFileCtrlUnitID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 1, 1, 11),
    _AgentBscSwFileCtrlUnitID_Type()
)
agentBscSwFileCtrlUnitID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentBscSwFileCtrlUnitID.setStatus("current")
_AgentBscSwFileIPv6Addr_Type = Ipv6Address
_AgentBscSwFileIPv6Addr_Object = MibTableColumn
agentBscSwFileIPv6Addr = _AgentBscSwFileIPv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 1, 1, 12),
    _AgentBscSwFileIPv6Addr_Type()
)
agentBscSwFileIPv6Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentBscSwFileIPv6Addr.setStatus("current")
_AgentBscSwFileBootUpImage_Type = TruthValue
_AgentBscSwFileBootUpImage_Object = MibTableColumn
agentBscSwFileBootUpImage = _AgentBscSwFileBootUpImage_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 1, 1, 13),
    _AgentBscSwFileBootUpImage_Type()
)
agentBscSwFileBootUpImage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentBscSwFileBootUpImage.setStatus("current")
_AgentBscSwFileForceAgree_Type = TruthValue
_AgentBscSwFileForceAgree_Object = MibTableColumn
agentBscSwFileForceAgree = _AgentBscSwFileForceAgree_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 1, 1, 14),
    _AgentBscSwFileForceAgree_Type()
)
agentBscSwFileForceAgree.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentBscSwFileForceAgree.setStatus("current")


class _AgentBscSwFileInterfaceName_Type(DisplayString):
    """Custom type agentBscSwFileInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_AgentBscSwFileInterfaceName_Type.__name__ = "DisplayString"
_AgentBscSwFileInterfaceName_Object = MibTableColumn
agentBscSwFileInterfaceName = _AgentBscSwFileInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 1, 1, 15),
    _AgentBscSwFileInterfaceName_Type()
)
agentBscSwFileInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentBscSwFileInterfaceName.setStatus("current")


class _AgentBscSwFileServerDomainName_Type(DisplayString):
    """Custom type agentBscSwFileServerDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AgentBscSwFileServerDomainName_Type.__name__ = "DisplayString"
_AgentBscSwFileServerDomainName_Object = MibTableColumn
agentBscSwFileServerDomainName = _AgentBscSwFileServerDomainName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 1, 1, 16),
    _AgentBscSwFileServerDomainName_Type()
)
agentBscSwFileServerDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentBscSwFileServerDomainName.setStatus("current")


class _AgentFileTransfer_Type(Integer32):
    """Custom type agentFileTransfer based on Integer32"""
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
        *(("noaction", 4),
          ("other", 1),
          ("start", 2),
          ("start-and-reset", 3))
    )


_AgentFileTransfer_Type.__name__ = "Integer32"
_AgentFileTransfer_Object = MibScalar
agentFileTransfer = _AgentFileTransfer_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 2),
    _AgentFileTransfer_Type()
)
agentFileTransfer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentFileTransfer.setStatus("obsolete")


class _AgentSystemReset_Type(Integer32):
    """Custom type agentSystemReset based on Integer32"""
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
        *(("cold-start", 2),
          ("no-reset", 4),
          ("other", 1),
          ("warm-start", 3))
    )


_AgentSystemReset_Type.__name__ = "Integer32"
_AgentSystemReset_Object = MibScalar
agentSystemReset = _AgentSystemReset_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 3),
    _AgentSystemReset_Type()
)
agentSystemReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSystemReset.setStatus("deprecated")


class _AgentRs232PortConfig_Type(Integer32):
    """Custom type agentRs232PortConfig based on Integer32"""
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
        *(("console", 2),
          ("notAvail", 4),
          ("other", 1),
          ("out-of-band", 3))
    )


_AgentRs232PortConfig_Type.__name__ = "Integer32"
_AgentRs232PortConfig_Object = MibScalar
agentRs232PortConfig = _AgentRs232PortConfig_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 4),
    _AgentRs232PortConfig_Type()
)
agentRs232PortConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRs232PortConfig.setStatus("current")


class _AgentOutOfBandBaudRateConfig_Type(Integer32):
    """Custom type agentOutOfBandBaudRateConfig based on Integer32"""
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
        *(("baudRate-115200", 6),
          ("baudRate-19200", 4),
          ("baudRate-2400", 2),
          ("baudRate-38400", 5),
          ("baudRate-9600", 3),
          ("other", 1))
    )


_AgentOutOfBandBaudRateConfig_Type.__name__ = "Integer32"
_AgentOutOfBandBaudRateConfig_Object = MibScalar
agentOutOfBandBaudRateConfig = _AgentOutOfBandBaudRateConfig_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 5),
    _AgentOutOfBandBaudRateConfig_Type()
)
agentOutOfBandBaudRateConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentOutOfBandBaudRateConfig.setStatus("obsolete")


class _AgentSaveCfg_Type(Integer32):
    """Custom type agentSaveCfg based on Integer32"""
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
        *(("all", 5),
          ("cfg-id1", 2),
          ("cfg-id2", 3),
          ("log", 4),
          ("other", 1))
    )


_AgentSaveCfg_Type.__name__ = "Integer32"
_AgentSaveCfg_Object = MibScalar
agentSaveCfg = _AgentSaveCfg_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 6),
    _AgentSaveCfg_Type()
)
agentSaveCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSaveCfg.setStatus("current")
_SwMultiImageInfoTable_Object = MibTable
swMultiImageInfoTable = _SwMultiImageInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 7)
)
if mibBuilder.loadTexts:
    swMultiImageInfoTable.setStatus("current")
_SwMultiImageInfoEntry_Object = MibTableRow
swMultiImageInfoEntry = _SwMultiImageInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 7, 1)
)
swMultiImageInfoEntry.setIndexNames(
    (0, "AGENT-GENERAL-MIB", "swMultiImageInfoID"),
)
if mibBuilder.loadTexts:
    swMultiImageInfoEntry.setStatus("current")
_SwMultiImageInfoID_Type = Integer32
_SwMultiImageInfoID_Object = MibTableColumn
swMultiImageInfoID = _SwMultiImageInfoID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 7, 1, 1),
    _SwMultiImageInfoID_Type()
)
swMultiImageInfoID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMultiImageInfoID.setStatus("current")


class _SwMultiImageVersion_Type(DisplayString):
    """Custom type swMultiImageVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SwMultiImageVersion_Type.__name__ = "DisplayString"
_SwMultiImageVersion_Object = MibTableColumn
swMultiImageVersion = _SwMultiImageVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 7, 1, 2),
    _SwMultiImageVersion_Type()
)
swMultiImageVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMultiImageVersion.setStatus("current")
_SwMultiImageSize_Type = Integer32
_SwMultiImageSize_Object = MibTableColumn
swMultiImageSize = _SwMultiImageSize_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 7, 1, 3),
    _SwMultiImageSize_Type()
)
swMultiImageSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMultiImageSize.setStatus("current")


class _SwMultiImageUpdateTime_Type(DisplayString):
    """Custom type swMultiImageUpdateTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SwMultiImageUpdateTime_Type.__name__ = "DisplayString"
_SwMultiImageUpdateTime_Object = MibTableColumn
swMultiImageUpdateTime = _SwMultiImageUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 7, 1, 4),
    _SwMultiImageUpdateTime_Type()
)
swMultiImageUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMultiImageUpdateTime.setStatus("current")


class _SwMultiImageFrom_Type(DisplayString):
    """Custom type swMultiImageFrom based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_SwMultiImageFrom_Type.__name__ = "DisplayString"
_SwMultiImageFrom_Object = MibTableColumn
swMultiImageFrom = _SwMultiImageFrom_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 7, 1, 5),
    _SwMultiImageFrom_Type()
)
swMultiImageFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMultiImageFrom.setStatus("current")


class _SwMultiImageSendUser_Type(DisplayString):
    """Custom type swMultiImageSendUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SwMultiImageSendUser_Type.__name__ = "DisplayString"
_SwMultiImageSendUser_Object = MibTableColumn
swMultiImageSendUser = _SwMultiImageSendUser_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 7, 1, 6),
    _SwMultiImageSendUser_Type()
)
swMultiImageSendUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMultiImageSendUser.setStatus("current")


class _SwMultiImageFileName_Type(DisplayString):
    """Custom type swMultiImageFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwMultiImageFileName_Type.__name__ = "DisplayString"
_SwMultiImageFileName_Object = MibTableColumn
swMultiImageFileName = _SwMultiImageFileName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 7, 1, 7),
    _SwMultiImageFileName_Type()
)
swMultiImageFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMultiImageFileName.setStatus("current")
_AgentMultiCfgMgmt_ObjectIdentity = ObjectIdentity
agentMultiCfgMgmt = _AgentMultiCfgMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 8)
)
_SwMultiCfgInfoTable_Object = MibTable
swMultiCfgInfoTable = _SwMultiCfgInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 8, 1)
)
if mibBuilder.loadTexts:
    swMultiCfgInfoTable.setStatus("current")
_SwMultiCfgInfoEntry_Object = MibTableRow
swMultiCfgInfoEntry = _SwMultiCfgInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 8, 1, 1)
)
swMultiCfgInfoEntry.setIndexNames(
    (0, "AGENT-GENERAL-MIB", "swMultiCfgInfoID"),
)
if mibBuilder.loadTexts:
    swMultiCfgInfoEntry.setStatus("current")
_SwMultiCfgInfoID_Type = Integer32
_SwMultiCfgInfoID_Object = MibTableColumn
swMultiCfgInfoID = _SwMultiCfgInfoID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 8, 1, 1, 1),
    _SwMultiCfgInfoID_Type()
)
swMultiCfgInfoID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMultiCfgInfoID.setStatus("current")


class _SwMultiCfgVersion_Type(DisplayString):
    """Custom type swMultiCfgVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SwMultiCfgVersion_Type.__name__ = "DisplayString"
_SwMultiCfgVersion_Object = MibTableColumn
swMultiCfgVersion = _SwMultiCfgVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 8, 1, 1, 2),
    _SwMultiCfgVersion_Type()
)
swMultiCfgVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMultiCfgVersion.setStatus("current")
_SwMultiCfgSize_Type = Integer32
_SwMultiCfgSize_Object = MibTableColumn
swMultiCfgSize = _SwMultiCfgSize_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 8, 1, 1, 3),
    _SwMultiCfgSize_Type()
)
swMultiCfgSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMultiCfgSize.setStatus("current")


class _SwMultiCFgUpdateTime_Type(DisplayString):
    """Custom type swMultiCFgUpdateTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SwMultiCFgUpdateTime_Type.__name__ = "DisplayString"
_SwMultiCFgUpdateTime_Object = MibTableColumn
swMultiCFgUpdateTime = _SwMultiCFgUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 8, 1, 1, 4),
    _SwMultiCFgUpdateTime_Type()
)
swMultiCFgUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMultiCFgUpdateTime.setStatus("current")


class _SwMultiCfgFrom_Type(DisplayString):
    """Custom type swMultiCfgFrom based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_SwMultiCfgFrom_Type.__name__ = "DisplayString"
_SwMultiCfgFrom_Object = MibTableColumn
swMultiCfgFrom = _SwMultiCfgFrom_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 8, 1, 1, 5),
    _SwMultiCfgFrom_Type()
)
swMultiCfgFrom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMultiCfgFrom.setStatus("current")


class _SwMultiCfgSendUser_Type(DisplayString):
    """Custom type swMultiCfgSendUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SwMultiCfgSendUser_Type.__name__ = "DisplayString"
_SwMultiCfgSendUser_Object = MibTableColumn
swMultiCfgSendUser = _SwMultiCfgSendUser_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 8, 1, 1, 6),
    _SwMultiCfgSendUser_Type()
)
swMultiCfgSendUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMultiCfgSendUser.setStatus("current")


class _SwMultiCfgFileName_Type(DisplayString):
    """Custom type swMultiCfgFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwMultiCfgFileName_Type.__name__ = "DisplayString"
_SwMultiCfgFileName_Object = MibTableColumn
swMultiCfgFileName = _SwMultiCfgFileName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 8, 1, 1, 7),
    _SwMultiCfgFileName_Type()
)
swMultiCfgFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMultiCfgFileName.setStatus("current")
_SwMultiCfgCurrentUsed_Type = Integer32
_SwMultiCfgCurrentUsed_Object = MibScalar
swMultiCfgCurrentUsed = _SwMultiCfgCurrentUsed_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 8, 2),
    _SwMultiCfgCurrentUsed_Type()
)
swMultiCfgCurrentUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMultiCfgCurrentUsed.setStatus("current")
_SwMultiCfgBootUp_Type = Integer32
_SwMultiCfgBootUp_Object = MibScalar
swMultiCfgBootUp = _SwMultiCfgBootUp_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 8, 3),
    _SwMultiCfgBootUp_Type()
)
swMultiCfgBootUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMultiCfgBootUp.setStatus("current")
_SwMultiCfgCtrlTable_Object = MibTable
swMultiCfgCtrlTable = _SwMultiCfgCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 8, 4)
)
if mibBuilder.loadTexts:
    swMultiCfgCtrlTable.setStatus("current")
_SwMultiCfgCtrlEntry_Object = MibTableRow
swMultiCfgCtrlEntry = _SwMultiCfgCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 8, 4, 1)
)
swMultiCfgCtrlEntry.setIndexNames(
    (0, "AGENT-GENERAL-MIB", "swMultiCfgCtrlID"),
)
if mibBuilder.loadTexts:
    swMultiCfgCtrlEntry.setStatus("current")


class _SwMultiCfgCtrlID_Type(Integer32):
    """Custom type swMultiCfgCtrlID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cfgId-1", 1),
          ("cfgId-2", 2))
    )


_SwMultiCfgCtrlID_Type.__name__ = "Integer32"
_SwMultiCfgCtrlID_Object = MibTableColumn
swMultiCfgCtrlID = _SwMultiCfgCtrlID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 8, 4, 1, 1),
    _SwMultiCfgCtrlID_Type()
)
swMultiCfgCtrlID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMultiCfgCtrlID.setStatus("current")


class _SwMultiCfgAction_Type(Integer32):
    """Custom type swMultiCfgAction based on Integer32"""
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
        *(("active", 1),
          ("apply", 3),
          ("config-as-bootup-cfg", 5),
          ("delete", 2),
          ("none", 4))
    )


_SwMultiCfgAction_Type.__name__ = "Integer32"
_SwMultiCfgAction_Object = MibTableColumn
swMultiCfgAction = _SwMultiCfgAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 8, 4, 1, 2),
    _SwMultiCfgAction_Type()
)
swMultiCfgAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMultiCfgAction.setStatus("current")
_SystemSeverityControlMgmt_ObjectIdentity = ObjectIdentity
systemSeverityControlMgmt = _SystemSeverityControlMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 9)
)
_SystemSeverityTrapControl_Type = AgentNotifyLevel
_SystemSeverityTrapControl_Object = MibScalar
systemSeverityTrapControl = _SystemSeverityTrapControl_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 9, 1),
    _SystemSeverityTrapControl_Type()
)
systemSeverityTrapControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSeverityTrapControl.setStatus("current")
_SystemSeverityLogControl_Type = AgentNotifyLevel
_SystemSeverityLogControl_Object = MibScalar
systemSeverityLogControl = _SystemSeverityLogControl_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 9, 2),
    _SystemSeverityLogControl_Type()
)
systemSeverityLogControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemSeverityLogControl.setStatus("current")
_AgentTrustedHostMgmt_ObjectIdentity = ObjectIdentity
agentTrustedHostMgmt = _AgentTrustedHostMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 10)
)
_AgentTrustedHostTable_Object = MibTable
agentTrustedHostTable = _AgentTrustedHostTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 10, 1)
)
if mibBuilder.loadTexts:
    agentTrustedHostTable.setStatus("current")
_AgentTrustedHostEntry_Object = MibTableRow
agentTrustedHostEntry = _AgentTrustedHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 10, 1, 1)
)
agentTrustedHostEntry.setIndexNames(
    (0, "AGENT-GENERAL-MIB", "agentTrustedHostIndex"),
)
if mibBuilder.loadTexts:
    agentTrustedHostEntry.setStatus("current")


class _AgentTrustedHostIndex_Type(Integer32):
    """Custom type agentTrustedHostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_AgentTrustedHostIndex_Type.__name__ = "Integer32"
_AgentTrustedHostIndex_Object = MibTableColumn
agentTrustedHostIndex = _AgentTrustedHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 10, 1, 1, 1),
    _AgentTrustedHostIndex_Type()
)
agentTrustedHostIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentTrustedHostIndex.setStatus("current")
_AgentTrustedHostIPAddress_Type = IpAddress
_AgentTrustedHostIPAddress_Object = MibTableColumn
agentTrustedHostIPAddress = _AgentTrustedHostIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 10, 1, 1, 2),
    _AgentTrustedHostIPAddress_Type()
)
agentTrustedHostIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentTrustedHostIPAddress.setStatus("current")
_AgentTrustedHostRowStatus_Type = RowStatus
_AgentTrustedHostRowStatus_Object = MibTableColumn
agentTrustedHostRowStatus = _AgentTrustedHostRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 10, 1, 1, 3),
    _AgentTrustedHostRowStatus_Type()
)
agentTrustedHostRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentTrustedHostRowStatus.setStatus("current")
_AgentTrustedHostIPSubnetMask_Type = IpAddress
_AgentTrustedHostIPSubnetMask_Object = MibTableColumn
agentTrustedHostIPSubnetMask = _AgentTrustedHostIPSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 10, 1, 1, 4),
    _AgentTrustedHostIPSubnetMask_Type()
)
agentTrustedHostIPSubnetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentTrustedHostIPSubnetMask.setStatus("current")


class _AgentTrustedHostForSNMP_Type(Integer32):
    """Custom type agentTrustedHostForSNMP based on Integer32"""
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


_AgentTrustedHostForSNMP_Type.__name__ = "Integer32"
_AgentTrustedHostForSNMP_Object = MibTableColumn
agentTrustedHostForSNMP = _AgentTrustedHostForSNMP_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 10, 1, 1, 5),
    _AgentTrustedHostForSNMP_Type()
)
agentTrustedHostForSNMP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentTrustedHostForSNMP.setStatus("current")


class _AgentTrustedHostForTELNET_Type(Integer32):
    """Custom type agentTrustedHostForTELNET based on Integer32"""
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


_AgentTrustedHostForTELNET_Type.__name__ = "Integer32"
_AgentTrustedHostForTELNET_Object = MibTableColumn
agentTrustedHostForTELNET = _AgentTrustedHostForTELNET_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 10, 1, 1, 6),
    _AgentTrustedHostForTELNET_Type()
)
agentTrustedHostForTELNET.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentTrustedHostForTELNET.setStatus("current")


class _AgentTrustedHostForSSH_Type(Integer32):
    """Custom type agentTrustedHostForSSH based on Integer32"""
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


_AgentTrustedHostForSSH_Type.__name__ = "Integer32"
_AgentTrustedHostForSSH_Object = MibTableColumn
agentTrustedHostForSSH = _AgentTrustedHostForSSH_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 10, 1, 1, 7),
    _AgentTrustedHostForSSH_Type()
)
agentTrustedHostForSSH.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentTrustedHostForSSH.setStatus("current")


class _AgentTrustedHostForHTTP_Type(Integer32):
    """Custom type agentTrustedHostForHTTP based on Integer32"""
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


_AgentTrustedHostForHTTP_Type.__name__ = "Integer32"
_AgentTrustedHostForHTTP_Object = MibTableColumn
agentTrustedHostForHTTP = _AgentTrustedHostForHTTP_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 10, 1, 1, 8),
    _AgentTrustedHostForHTTP_Type()
)
agentTrustedHostForHTTP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentTrustedHostForHTTP.setStatus("current")


class _AgentTrustedHostForHTTPS_Type(Integer32):
    """Custom type agentTrustedHostForHTTPS based on Integer32"""
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


_AgentTrustedHostForHTTPS_Type.__name__ = "Integer32"
_AgentTrustedHostForHTTPS_Object = MibTableColumn
agentTrustedHostForHTTPS = _AgentTrustedHostForHTTPS_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 10, 1, 1, 9),
    _AgentTrustedHostForHTTPS_Type()
)
agentTrustedHostForHTTPS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentTrustedHostForHTTPS.setStatus("current")


class _AgentTrustedHostForPING_Type(Integer32):
    """Custom type agentTrustedHostForPING based on Integer32"""
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


_AgentTrustedHostForPING_Type.__name__ = "Integer32"
_AgentTrustedHostForPING_Object = MibTableColumn
agentTrustedHostForPING = _AgentTrustedHostForPING_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 10, 1, 1, 10),
    _AgentTrustedHostForPING_Type()
)
agentTrustedHostForPING.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentTrustedHostForPING.setStatus("current")
_AgentTrustedHostAddrType_Type = InetAddressType
_AgentTrustedHostAddrType_Object = MibTableColumn
agentTrustedHostAddrType = _AgentTrustedHostAddrType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 10, 1, 1, 11),
    _AgentTrustedHostAddrType_Type()
)
agentTrustedHostAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentTrustedHostAddrType.setStatus("current")
_AgentTrustedHostAddr_Type = InetAddress
_AgentTrustedHostAddr_Object = MibTableColumn
agentTrustedHostAddr = _AgentTrustedHostAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 10, 1, 1, 12),
    _AgentTrustedHostAddr_Type()
)
agentTrustedHostAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentTrustedHostAddr.setStatus("current")


class _AgentTrustedHostIPv6PrefixLen_Type(Integer32):
    """Custom type agentTrustedHostIPv6PrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_AgentTrustedHostIPv6PrefixLen_Type.__name__ = "Integer32"
_AgentTrustedHostIPv6PrefixLen_Object = MibTableColumn
agentTrustedHostIPv6PrefixLen = _AgentTrustedHostIPv6PrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 10, 1, 1, 13),
    _AgentTrustedHostIPv6PrefixLen_Type()
)
agentTrustedHostIPv6PrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentTrustedHostIPv6PrefixLen.setStatus("current")


class _AgentTrustedHostDelAllState_Type(Integer32):
    """Custom type agentTrustedHostDelAllState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("start", 2))
    )


_AgentTrustedHostDelAllState_Type.__name__ = "Integer32"
_AgentTrustedHostDelAllState_Object = MibScalar
agentTrustedHostDelAllState = _AgentTrustedHostDelAllState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 10, 2),
    _AgentTrustedHostDelAllState_Type()
)
agentTrustedHostDelAllState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTrustedHostDelAllState.setStatus("current")
_AgentFDBMgmt_ObjectIdentity = ObjectIdentity
agentFDBMgmt = _AgentFDBMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 11)
)


class _AgentFDBClearAllState_Type(Integer32):
    """Custom type agentFDBClearAllState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("start", 2))
    )


_AgentFDBClearAllState_Type.__name__ = "Integer32"
_AgentFDBClearAllState_Object = MibScalar
agentFDBClearAllState = _AgentFDBClearAllState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 11, 1),
    _AgentFDBClearAllState_Type()
)
agentFDBClearAllState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentFDBClearAllState.setStatus("current")
_AgentFDBClearByPortTable_Object = MibTable
agentFDBClearByPortTable = _AgentFDBClearByPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 11, 2)
)
if mibBuilder.loadTexts:
    agentFDBClearByPortTable.setStatus("current")
_AgentFDBClearByPortEntry_Object = MibTableRow
agentFDBClearByPortEntry = _AgentFDBClearByPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 11, 2, 1)
)
agentFDBClearByPortEntry.setIndexNames(
    (0, "AGENT-GENERAL-MIB", "agentFDBClearPortIndex"),
)
if mibBuilder.loadTexts:
    agentFDBClearByPortEntry.setStatus("current")


class _AgentFDBClearPortIndex_Type(Integer32):
    """Custom type agentFDBClearPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AgentFDBClearPortIndex_Type.__name__ = "Integer32"
_AgentFDBClearPortIndex_Object = MibTableColumn
agentFDBClearPortIndex = _AgentFDBClearPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 11, 2, 1, 1),
    _AgentFDBClearPortIndex_Type()
)
agentFDBClearPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentFDBClearPortIndex.setStatus("current")


class _AgentFDBClearByPortAction_Type(Integer32):
    """Custom type agentFDBClearByPortAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("start", 2))
    )


_AgentFDBClearByPortAction_Type.__name__ = "Integer32"
_AgentFDBClearByPortAction_Object = MibTableColumn
agentFDBClearByPortAction = _AgentFDBClearByPortAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 11, 2, 1, 2),
    _AgentFDBClearByPortAction_Type()
)
agentFDBClearByPortAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentFDBClearByPortAction.setStatus("current")
_AgentFDBClearByVlanTable_Object = MibTable
agentFDBClearByVlanTable = _AgentFDBClearByVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 11, 3)
)
if mibBuilder.loadTexts:
    agentFDBClearByVlanTable.setStatus("current")
_AgentFDBClearByVlanEntry_Object = MibTableRow
agentFDBClearByVlanEntry = _AgentFDBClearByVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 11, 3, 1)
)
agentFDBClearByVlanEntry.setIndexNames(
    (0, "AGENT-GENERAL-MIB", "agentFDBClearVid"),
)
if mibBuilder.loadTexts:
    agentFDBClearByVlanEntry.setStatus("current")
_AgentFDBClearVid_Type = VlanId
_AgentFDBClearVid_Object = MibTableColumn
agentFDBClearVid = _AgentFDBClearVid_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 11, 3, 1, 1),
    _AgentFDBClearVid_Type()
)
agentFDBClearVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentFDBClearVid.setStatus("current")


class _AgentFDBClearByVlanAction_Type(Integer32):
    """Custom type agentFDBClearByVlanAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("start", 2))
    )


_AgentFDBClearByVlanAction_Type.__name__ = "Integer32"
_AgentFDBClearByVlanAction_Object = MibTableColumn
agentFDBClearByVlanAction = _AgentFDBClearByVlanAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 11, 3, 1, 2),
    _AgentFDBClearByVlanAction_Type()
)
agentFDBClearByVlanAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentFDBClearByVlanAction.setStatus("current")
_AgentFDBSecurityTable_Object = MibTable
agentFDBSecurityTable = _AgentFDBSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 11, 4)
)
if mibBuilder.loadTexts:
    agentFDBSecurityTable.setStatus("current")
_AgentFDBSecurityEntry_Object = MibTableRow
agentFDBSecurityEntry = _AgentFDBSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 11, 4, 1)
)
agentFDBSecurityEntry.setIndexNames(
    (0, "AGENT-GENERAL-MIB", "agentFDBVid"),
    (0, "AGENT-GENERAL-MIB", "agentFDBMacAddress"),
)
if mibBuilder.loadTexts:
    agentFDBSecurityEntry.setStatus("current")
_AgentFDBVid_Type = VlanId
_AgentFDBVid_Object = MibTableColumn
agentFDBVid = _AgentFDBVid_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 11, 4, 1, 1),
    _AgentFDBVid_Type()
)
agentFDBVid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentFDBVid.setStatus("current")
_AgentFDBMacAddress_Type = MacAddress
_AgentFDBMacAddress_Object = MibTableColumn
agentFDBMacAddress = _AgentFDBMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 11, 4, 1, 2),
    _AgentFDBMacAddress_Type()
)
agentFDBMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentFDBMacAddress.setStatus("current")


class _AgentFDBPort_Type(Integer32):
    """Custom type agentFDBPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AgentFDBPort_Type.__name__ = "Integer32"
_AgentFDBPort_Object = MibTableColumn
agentFDBPort = _AgentFDBPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 11, 4, 1, 3),
    _AgentFDBPort_Type()
)
agentFDBPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentFDBPort.setStatus("current")


class _AgentFDBType_Type(Integer32):
    """Custom type agentFDBType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("static", 2))
    )


_AgentFDBType_Type.__name__ = "Integer32"
_AgentFDBType_Object = MibTableColumn
agentFDBType = _AgentFDBType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 11, 4, 1, 4),
    _AgentFDBType_Type()
)
agentFDBType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentFDBType.setStatus("current")


class _AgentFDBStatus_Type(Integer32):
    """Custom type agentFDBStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("forward", 2))
    )


_AgentFDBStatus_Type.__name__ = "Integer32"
_AgentFDBStatus_Object = MibTableColumn
agentFDBStatus = _AgentFDBStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 11, 4, 1, 5),
    _AgentFDBStatus_Type()
)
agentFDBStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentFDBStatus.setStatus("current")


class _AgentFDBSecurityModule_Type(Integer32):
    """Custom type agentFDBSecurityModule based on Integer32"""
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
        *(("compound-authentication", 6),
          ("dot1x", 1),
          ("jwac", 3),
          ("mac-based-access-control", 5),
          ("port-security", 4),
          ("wac", 2))
    )


_AgentFDBSecurityModule_Type.__name__ = "Integer32"
_AgentFDBSecurityModule_Object = MibTableColumn
agentFDBSecurityModule = _AgentFDBSecurityModule_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 11, 4, 1, 6),
    _AgentFDBSecurityModule_Type()
)
agentFDBSecurityModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentFDBSecurityModule.setStatus("current")
_AgentARPMgmt_ObjectIdentity = ObjectIdentity
agentARPMgmt = _AgentARPMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 12)
)


class _AgentARPClearAllState_Type(Integer32):
    """Custom type agentARPClearAllState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("start", 2))
    )


_AgentARPClearAllState_Type.__name__ = "Integer32"
_AgentARPClearAllState_Object = MibScalar
agentARPClearAllState = _AgentARPClearAllState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 12, 1),
    _AgentARPClearAllState_Type()
)
agentARPClearAllState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentARPClearAllState.setStatus("current")
_AgentGratuitousARPMgmt_ObjectIdentity = ObjectIdentity
agentGratuitousARPMgmt = _AgentGratuitousARPMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 12, 2)
)


class _AgentGratuitousARPSendIpifStatusUpState_Type(Integer32):
    """Custom type agentGratuitousARPSendIpifStatusUpState based on Integer32"""
    defaultValue = 1

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


_AgentGratuitousARPSendIpifStatusUpState_Type.__name__ = "Integer32"
_AgentGratuitousARPSendIpifStatusUpState_Object = MibScalar
agentGratuitousARPSendIpifStatusUpState = _AgentGratuitousARPSendIpifStatusUpState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 12, 2, 1),
    _AgentGratuitousARPSendIpifStatusUpState_Type()
)
agentGratuitousARPSendIpifStatusUpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentGratuitousARPSendIpifStatusUpState.setStatus("current")


class _AgentGratuitousARPSendDupIpDetectedState_Type(Integer32):
    """Custom type agentGratuitousARPSendDupIpDetectedState based on Integer32"""
    defaultValue = 1

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


_AgentGratuitousARPSendDupIpDetectedState_Type.__name__ = "Integer32"
_AgentGratuitousARPSendDupIpDetectedState_Object = MibScalar
agentGratuitousARPSendDupIpDetectedState = _AgentGratuitousARPSendDupIpDetectedState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 12, 2, 2),
    _AgentGratuitousARPSendDupIpDetectedState_Type()
)
agentGratuitousARPSendDupIpDetectedState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentGratuitousARPSendDupIpDetectedState.setStatus("current")


class _AgentGratuitousARPLearningState_Type(Integer32):
    """Custom type agentGratuitousARPLearningState based on Integer32"""
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


_AgentGratuitousARPLearningState_Type.__name__ = "Integer32"
_AgentGratuitousARPLearningState_Object = MibScalar
agentGratuitousARPLearningState = _AgentGratuitousARPLearningState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 12, 2, 3),
    _AgentGratuitousARPLearningState_Type()
)
agentGratuitousARPLearningState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentGratuitousARPLearningState.setStatus("current")
_AgentGratuitousARPTable_Object = MibTable
agentGratuitousARPTable = _AgentGratuitousARPTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 12, 2, 4)
)
if mibBuilder.loadTexts:
    agentGratuitousARPTable.setStatus("current")
_AgentGratuitousARPEntry_Object = MibTableRow
agentGratuitousARPEntry = _AgentGratuitousARPEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 12, 2, 4, 1)
)
agentGratuitousARPEntry.setIndexNames(
    (0, "AGENT-GENERAL-MIB", "agentGratuitousARPInterfaceName"),
)
if mibBuilder.loadTexts:
    agentGratuitousARPEntry.setStatus("current")
_AgentGratuitousARPInterfaceName_Type = DisplayString
_AgentGratuitousARPInterfaceName_Object = MibTableColumn
agentGratuitousARPInterfaceName = _AgentGratuitousARPInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 12, 2, 4, 1, 1),
    _AgentGratuitousARPInterfaceName_Type()
)
agentGratuitousARPInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentGratuitousARPInterfaceName.setStatus("current")


class _AgentGratuitousARPPeriodicalSendInterval_Type(Integer32):
    """Custom type agentGratuitousARPPeriodicalSendInterval based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AgentGratuitousARPPeriodicalSendInterval_Type.__name__ = "Integer32"
_AgentGratuitousARPPeriodicalSendInterval_Object = MibTableColumn
agentGratuitousARPPeriodicalSendInterval = _AgentGratuitousARPPeriodicalSendInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 12, 2, 4, 1, 2),
    _AgentGratuitousARPPeriodicalSendInterval_Type()
)
agentGratuitousARPPeriodicalSendInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentGratuitousARPPeriodicalSendInterval.setStatus("current")
if mibBuilder.loadTexts:
    agentGratuitousARPPeriodicalSendInterval.setUnits("seconds")


class _AgentGratuitousARPTrapState_Type(Integer32):
    """Custom type agentGratuitousARPTrapState based on Integer32"""
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


_AgentGratuitousARPTrapState_Type.__name__ = "Integer32"
_AgentGratuitousARPTrapState_Object = MibTableColumn
agentGratuitousARPTrapState = _AgentGratuitousARPTrapState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 12, 2, 4, 1, 3),
    _AgentGratuitousARPTrapState_Type()
)
agentGratuitousARPTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentGratuitousARPTrapState.setStatus("current")


class _AgentGratuitousARPLogState_Type(Integer32):
    """Custom type agentGratuitousARPLogState based on Integer32"""
    defaultValue = 1

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


_AgentGratuitousARPLogState_Type.__name__ = "Integer32"
_AgentGratuitousARPLogState_Object = MibTableColumn
agentGratuitousARPLogState = _AgentGratuitousARPLogState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 12, 2, 4, 1, 4),
    _AgentGratuitousARPLogState_Type()
)
agentGratuitousARPLogState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentGratuitousARPLogState.setStatus("current")
_AgentARPTotalARPEntries_Type = Integer32
_AgentARPTotalARPEntries_Object = MibScalar
agentARPTotalARPEntries = _AgentARPTotalARPEntries_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 12, 3),
    _AgentARPTotalARPEntries_Type()
)
agentARPTotalARPEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentARPTotalARPEntries.setStatus("current")
_AgentARPRetryTimes_Type = Integer32
_AgentARPRetryTimes_Object = MibScalar
agentARPRetryTimes = _AgentARPRetryTimes_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 12, 4),
    _AgentARPRetryTimes_Type()
)
agentARPRetryTimes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentARPRetryTimes.setStatus("current")
_SwMultiImageCtrlTable_Object = MibTable
swMultiImageCtrlTable = _SwMultiImageCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 13)
)
if mibBuilder.loadTexts:
    swMultiImageCtrlTable.setStatus("current")
_SwMultiImageCtrlEntry_Object = MibTableRow
swMultiImageCtrlEntry = _SwMultiImageCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 13, 1)
)
swMultiImageCtrlEntry.setIndexNames(
    (0, "AGENT-GENERAL-MIB", "swMultiImageCtrlID"),
)
if mibBuilder.loadTexts:
    swMultiImageCtrlEntry.setStatus("current")
_SwMultiImageCtrlID_Type = Integer32
_SwMultiImageCtrlID_Object = MibTableColumn
swMultiImageCtrlID = _SwMultiImageCtrlID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 13, 1, 1),
    _SwMultiImageCtrlID_Type()
)
swMultiImageCtrlID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMultiImageCtrlID.setStatus("current")


class _SwMultiImageCtrlAction_Type(Integer32):
    """Custom type swMultiImageCtrlAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("config-as-bootup-fw", 1),
          ("delete", 2),
          ("none", 3))
    )


_SwMultiImageCtrlAction_Type.__name__ = "Integer32"
_SwMultiImageCtrlAction_Object = MibTableColumn
swMultiImageCtrlAction = _SwMultiImageCtrlAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 13, 1, 2),
    _SwMultiImageCtrlAction_Type()
)
swMultiImageCtrlAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swMultiImageCtrlAction.setStatus("current")
_AgentOutOfBandDataBits_Type = Integer32
_AgentOutOfBandDataBits_Object = MibScalar
agentOutOfBandDataBits = _AgentOutOfBandDataBits_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 14),
    _AgentOutOfBandDataBits_Type()
)
agentOutOfBandDataBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOutOfBandDataBits.setStatus("current")
_AgentOutOfBandParityBits_Type = DisplayString
_AgentOutOfBandParityBits_Object = MibScalar
agentOutOfBandParityBits = _AgentOutOfBandParityBits_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 15),
    _AgentOutOfBandParityBits_Type()
)
agentOutOfBandParityBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOutOfBandParityBits.setStatus("current")
_AgentOutOfBandStopBits_Type = Integer32
_AgentOutOfBandStopBits_Object = MibScalar
agentOutOfBandStopBits = _AgentOutOfBandStopBits_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 16),
    _AgentOutOfBandStopBits_Type()
)
agentOutOfBandStopBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOutOfBandStopBits.setStatus("current")


class _AgentOutOfBandAutoLogoutConfig_Type(Integer32):
    """Custom type agentOutOfBandAutoLogoutConfig based on Integer32"""
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
        *(("minutes-10", 4),
          ("minutes-15", 5),
          ("minutes-2", 2),
          ("minutes-5", 3),
          ("never", 1))
    )


_AgentOutOfBandAutoLogoutConfig_Type.__name__ = "Integer32"
_AgentOutOfBandAutoLogoutConfig_Object = MibScalar
agentOutOfBandAutoLogoutConfig = _AgentOutOfBandAutoLogoutConfig_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 17),
    _AgentOutOfBandAutoLogoutConfig_Type()
)
agentOutOfBandAutoLogoutConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentOutOfBandAutoLogoutConfig.setStatus("current")
_AgentBscFileSystemMgmt_ObjectIdentity = ObjectIdentity
agentBscFileSystemMgmt = _AgentBscFileSystemMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 18)
)
_AgentBscFileSystemTable_Object = MibTable
agentBscFileSystemTable = _AgentBscFileSystemTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 18, 1)
)
if mibBuilder.loadTexts:
    agentBscFileSystemTable.setStatus("current")
_AgentBscFileSystemEntry_Object = MibTableRow
agentBscFileSystemEntry = _AgentBscFileSystemEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 18, 1, 1)
)
agentBscFileSystemEntry.setIndexNames(
    (0, "AGENT-GENERAL-MIB", "agentBscFileSystemIndex"),
)
if mibBuilder.loadTexts:
    agentBscFileSystemEntry.setStatus("current")
_AgentBscFileSystemIndex_Type = Integer32
_AgentBscFileSystemIndex_Object = MibTableColumn
agentBscFileSystemIndex = _AgentBscFileSystemIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 18, 1, 1, 1),
    _AgentBscFileSystemIndex_Type()
)
agentBscFileSystemIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentBscFileSystemIndex.setStatus("current")


class _AgentBscFileSystemDscr_Type(DisplayString):
    """Custom type agentBscFileSystemDscr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AgentBscFileSystemDscr_Type.__name__ = "DisplayString"
_AgentBscFileSystemDscr_Object = MibTableColumn
agentBscFileSystemDscr = _AgentBscFileSystemDscr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 18, 1, 1, 2),
    _AgentBscFileSystemDscr_Type()
)
agentBscFileSystemDscr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentBscFileSystemDscr.setStatus("current")
_AgentBscFileSystemServerAddr_Type = IpAddress
_AgentBscFileSystemServerAddr_Object = MibTableColumn
agentBscFileSystemServerAddr = _AgentBscFileSystemServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 18, 1, 1, 3),
    _AgentBscFileSystemServerAddr_Type()
)
agentBscFileSystemServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentBscFileSystemServerAddr.setStatus("current")
_AgentBscFileSystemServerIPv6Addr_Type = Ipv6Address
_AgentBscFileSystemServerIPv6Addr_Object = MibTableColumn
agentBscFileSystemServerIPv6Addr = _AgentBscFileSystemServerIPv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 18, 1, 1, 4),
    _AgentBscFileSystemServerIPv6Addr_Type()
)
agentBscFileSystemServerIPv6Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentBscFileSystemServerIPv6Addr.setStatus("current")


class _AgentBscFileSystemServerFileName_Type(DisplayString):
    """Custom type agentBscFileSystemServerFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AgentBscFileSystemServerFileName_Type.__name__ = "DisplayString"
_AgentBscFileSystemServerFileName_Object = MibTableColumn
agentBscFileSystemServerFileName = _AgentBscFileSystemServerFileName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 18, 1, 1, 5),
    _AgentBscFileSystemServerFileName_Type()
)
agentBscFileSystemServerFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentBscFileSystemServerFileName.setStatus("current")


class _AgentBscFileSystemDeviceDriverID_Type(Integer32):
    """Custom type agentBscFileSystemDeviceDriverID based on Integer32"""
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
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27)
        )
    )
    namedValues = NamedValues(
        *(("a", 2),
          ("b", 3),
          ("c", 4),
          ("d", 5),
          ("e", 6),
          ("f", 7),
          ("g", 8),
          ("h", 9),
          ("i", 10),
          ("j", 11),
          ("k", 12),
          ("l", 13),
          ("m", 14),
          ("n", 15),
          ("none", 1),
          ("o", 16),
          ("p", 17),
          ("q", 18),
          ("r", 19),
          ("s", 20),
          ("t", 21),
          ("u", 22),
          ("v", 23),
          ("w", 24),
          ("x", 25),
          ("y", 26),
          ("z", 27))
    )


_AgentBscFileSystemDeviceDriverID_Type.__name__ = "Integer32"
_AgentBscFileSystemDeviceDriverID_Object = MibTableColumn
agentBscFileSystemDeviceDriverID = _AgentBscFileSystemDeviceDriverID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 18, 1, 1, 6),
    _AgentBscFileSystemDeviceDriverID_Type()
)
agentBscFileSystemDeviceDriverID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentBscFileSystemDeviceDriverID.setStatus("current")


class _AgentBscFileSystemDeviceFileName_Type(DisplayString):
    """Custom type agentBscFileSystemDeviceFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AgentBscFileSystemDeviceFileName_Type.__name__ = "DisplayString"
_AgentBscFileSystemDeviceFileName_Object = MibTableColumn
agentBscFileSystemDeviceFileName = _AgentBscFileSystemDeviceFileName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 18, 1, 1, 7),
    _AgentBscFileSystemDeviceFileName_Type()
)
agentBscFileSystemDeviceFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentBscFileSystemDeviceFileName.setStatus("current")


class _AgentBscFileSystemLoadType_Type(Integer32):
    """Custom type agentBscFileSystemLoadType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("download", 3),
          ("other", 1),
          ("upload", 2))
    )


_AgentBscFileSystemLoadType_Type.__name__ = "Integer32"
_AgentBscFileSystemLoadType_Object = MibTableColumn
agentBscFileSystemLoadType = _AgentBscFileSystemLoadType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 18, 1, 1, 8),
    _AgentBscFileSystemLoadType_Type()
)
agentBscFileSystemLoadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentBscFileSystemLoadType.setStatus("current")
_AgentBscFileSystemCtrlUnitID_Type = UnitList
_AgentBscFileSystemCtrlUnitID_Object = MibTableColumn
agentBscFileSystemCtrlUnitID = _AgentBscFileSystemCtrlUnitID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 18, 1, 1, 9),
    _AgentBscFileSystemCtrlUnitID_Type()
)
agentBscFileSystemCtrlUnitID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentBscFileSystemCtrlUnitID.setStatus("current")
_AgentBscFileSystemBootUpImage_Type = TruthValue
_AgentBscFileSystemBootUpImage_Object = MibTableColumn
agentBscFileSystemBootUpImage = _AgentBscFileSystemBootUpImage_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 18, 1, 1, 10),
    _AgentBscFileSystemBootUpImage_Type()
)
agentBscFileSystemBootUpImage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentBscFileSystemBootUpImage.setStatus("current")
_AgentBscFileSystemForceAgree_Type = TruthValue
_AgentBscFileSystemForceAgree_Object = MibTableColumn
agentBscFileSystemForceAgree = _AgentBscFileSystemForceAgree_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 18, 1, 1, 11),
    _AgentBscFileSystemForceAgree_Type()
)
agentBscFileSystemForceAgree.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentBscFileSystemForceAgree.setStatus("current")


class _AgentBscFileSystemCtrl_Type(Integer32):
    """Custom type agentBscFileSystemCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 2),
          ("other", 1),
          ("start", 3))
    )


_AgentBscFileSystemCtrl_Type.__name__ = "Integer32"
_AgentBscFileSystemCtrl_Object = MibTableColumn
agentBscFileSystemCtrl = _AgentBscFileSystemCtrl_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 18, 1, 1, 12),
    _AgentBscFileSystemCtrl_Type()
)
agentBscFileSystemCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentBscFileSystemCtrl.setStatus("current")


class _AgentBscFileSystemInterfaceName_Type(DisplayString):
    """Custom type agentBscFileSystemInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_AgentBscFileSystemInterfaceName_Type.__name__ = "DisplayString"
_AgentBscFileSystemInterfaceName_Object = MibTableColumn
agentBscFileSystemInterfaceName = _AgentBscFileSystemInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 18, 1, 1, 13),
    _AgentBscFileSystemInterfaceName_Type()
)
agentBscFileSystemInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentBscFileSystemInterfaceName.setStatus("current")


class _AgentBscFileSystemServerDomainName_Type(DisplayString):
    """Custom type agentBscFileSystemServerDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AgentBscFileSystemServerDomainName_Type.__name__ = "DisplayString"
_AgentBscFileSystemServerDomainName_Object = MibTableColumn
agentBscFileSystemServerDomainName = _AgentBscFileSystemServerDomainName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 18, 1, 1, 14),
    _AgentBscFileSystemServerDomainName_Type()
)
agentBscFileSystemServerDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentBscFileSystemServerDomainName.setStatus("current")
_AgentBscFileSystemIncrement_Type = TruthValue
_AgentBscFileSystemIncrement_Object = MibTableColumn
agentBscFileSystemIncrement = _AgentBscFileSystemIncrement_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 18, 1, 1, 15),
    _AgentBscFileSystemIncrement_Type()
)
agentBscFileSystemIncrement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentBscFileSystemIncrement.setStatus("current")


class _AgentBscFileSystemSaveConfigDriverID_Type(Integer32):
    """Custom type agentBscFileSystemSaveConfigDriverID based on Integer32"""
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
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27)
        )
    )
    namedValues = NamedValues(
        *(("a", 2),
          ("b", 3),
          ("c", 4),
          ("d", 5),
          ("e", 6),
          ("f", 7),
          ("g", 8),
          ("h", 9),
          ("i", 10),
          ("j", 11),
          ("k", 12),
          ("l", 13),
          ("m", 14),
          ("n", 15),
          ("none", 1),
          ("o", 16),
          ("p", 17),
          ("q", 18),
          ("r", 19),
          ("s", 20),
          ("t", 21),
          ("u", 22),
          ("v", 23),
          ("w", 24),
          ("x", 25),
          ("y", 26),
          ("z", 27))
    )


_AgentBscFileSystemSaveConfigDriverID_Type.__name__ = "Integer32"
_AgentBscFileSystemSaveConfigDriverID_Object = MibScalar
agentBscFileSystemSaveConfigDriverID = _AgentBscFileSystemSaveConfigDriverID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 18, 2),
    _AgentBscFileSystemSaveConfigDriverID_Type()
)
agentBscFileSystemSaveConfigDriverID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentBscFileSystemSaveConfigDriverID.setStatus("current")


class _AgentBscFileSystemSaveConfigFileName_Type(DisplayString):
    """Custom type agentBscFileSystemSaveConfigFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AgentBscFileSystemSaveConfigFileName_Type.__name__ = "DisplayString"
_AgentBscFileSystemSaveConfigFileName_Object = MibScalar
agentBscFileSystemSaveConfigFileName = _AgentBscFileSystemSaveConfigFileName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 18, 3),
    _AgentBscFileSystemSaveConfigFileName_Type()
)
agentBscFileSystemSaveConfigFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentBscFileSystemSaveConfigFileName.setStatus("current")


class _AgentBscFileSystemSaveCfg_Type(Integer32):
    """Custom type agentBscFileSystemSaveCfg based on Integer32"""
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
        *(("all", 4),
          ("cfg", 2),
          ("log", 3),
          ("other", 1))
    )


_AgentBscFileSystemSaveCfg_Type.__name__ = "Integer32"
_AgentBscFileSystemSaveCfg_Object = MibScalar
agentBscFileSystemSaveCfg = _AgentBscFileSystemSaveCfg_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 18, 4),
    _AgentBscFileSystemSaveCfg_Type()
)
agentBscFileSystemSaveCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentBscFileSystemSaveCfg.setStatus("current")
_AgentFileSystemConfigTable_Object = MibTable
agentFileSystemConfigTable = _AgentFileSystemConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 18, 5)
)
if mibBuilder.loadTexts:
    agentFileSystemConfigTable.setStatus("current")
_AgentFileSystemConfigEntry_Object = MibTableRow
agentFileSystemConfigEntry = _AgentFileSystemConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 18, 5, 1)
)
agentFileSystemConfigEntry.setIndexNames(
    (0, "AGENT-GENERAL-MIB", "agentFileSystemUnit"),
)
if mibBuilder.loadTexts:
    agentFileSystemConfigEntry.setStatus("current")
_AgentFileSystemUnit_Type = Integer32
_AgentFileSystemUnit_Object = MibTableColumn
agentFileSystemUnit = _AgentFileSystemUnit_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 18, 5, 1, 1),
    _AgentFileSystemUnit_Type()
)
agentFileSystemUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentFileSystemUnit.setStatus("current")


class _AgentFileSystemDriverID_Type(Integer32):
    """Custom type agentFileSystemDriverID based on Integer32"""
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
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27)
        )
    )
    namedValues = NamedValues(
        *(("a", 2),
          ("b", 3),
          ("c", 4),
          ("d", 5),
          ("e", 6),
          ("f", 7),
          ("g", 8),
          ("h", 9),
          ("i", 10),
          ("j", 11),
          ("k", 12),
          ("l", 13),
          ("m", 14),
          ("n", 15),
          ("none", 1),
          ("o", 16),
          ("p", 17),
          ("q", 18),
          ("r", 19),
          ("s", 20),
          ("t", 21),
          ("u", 22),
          ("v", 23),
          ("w", 24),
          ("x", 25),
          ("y", 26),
          ("z", 27))
    )


_AgentFileSystemDriverID_Type.__name__ = "Integer32"
_AgentFileSystemDriverID_Object = MibTableColumn
agentFileSystemDriverID = _AgentFileSystemDriverID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 18, 5, 1, 2),
    _AgentFileSystemDriverID_Type()
)
agentFileSystemDriverID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentFileSystemDriverID.setStatus("current")


class _AgentFileSystemBootImage_Type(DisplayString):
    """Custom type agentFileSystemBootImage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AgentFileSystemBootImage_Type.__name__ = "DisplayString"
_AgentFileSystemBootImage_Object = MibTableColumn
agentFileSystemBootImage = _AgentFileSystemBootImage_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 18, 5, 1, 3),
    _AgentFileSystemBootImage_Type()
)
agentFileSystemBootImage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentFileSystemBootImage.setStatus("current")


class _AgentFileSystemBootConfig_Type(DisplayString):
    """Custom type agentFileSystemBootConfig based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AgentFileSystemBootConfig_Type.__name__ = "DisplayString"
_AgentFileSystemBootConfig_Object = MibTableColumn
agentFileSystemBootConfig = _AgentFileSystemBootConfig_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 18, 5, 1, 4),
    _AgentFileSystemBootConfig_Type()
)
agentFileSystemBootConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentFileSystemBootConfig.setStatus("current")


class _AgentFileSystemActConfig_Type(DisplayString):
    """Custom type agentFileSystemActConfig based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AgentFileSystemActConfig_Type.__name__ = "DisplayString"
_AgentFileSystemActConfig_Object = MibTableColumn
agentFileSystemActConfig = _AgentFileSystemActConfig_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 18, 5, 1, 5),
    _AgentFileSystemActConfig_Type()
)
agentFileSystemActConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentFileSystemActConfig.setStatus("current")


class _AgentReboot_Type(Integer32):
    """Custom type agentReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("start", 2))
    )


_AgentReboot_Type.__name__ = "Integer32"
_AgentReboot_Object = MibScalar
agentReboot = _AgentReboot_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 19),
    _AgentReboot_Type()
)
agentReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentReboot.setStatus("current")


class _AgentReset_Type(Integer32):
    """Custom type agentReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("config", 2),
          ("none", 1),
          ("reset", 4),
          ("system", 3),
          ("system-exclude-ip", 6),
          ("system-exclude-vlan", 5),
          ("system-exclude-vlan-ip", 7))
    )


_AgentReset_Type.__name__ = "Integer32"
_AgentReset_Object = MibScalar
agentReset = _AgentReset_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 20),
    _AgentReset_Type()
)
agentReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentReset.setStatus("current")
_AgentFTPFileTable_Object = MibTable
agentFTPFileTable = _AgentFTPFileTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 21)
)
if mibBuilder.loadTexts:
    agentFTPFileTable.setStatus("current")
_AgentFTPFileEntry_Object = MibTableRow
agentFTPFileEntry = _AgentFTPFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 21, 1)
)
agentFTPFileEntry.setIndexNames(
    (0, "AGENT-GENERAL-MIB", "agentFTPFileIndex"),
)
if mibBuilder.loadTexts:
    agentFTPFileEntry.setStatus("current")
_AgentFTPFileIndex_Type = Integer32
_AgentFTPFileIndex_Object = MibTableColumn
agentFTPFileIndex = _AgentFTPFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 21, 1, 1),
    _AgentFTPFileIndex_Type()
)
agentFTPFileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentFTPFileIndex.setStatus("current")


class _AgentFTPFileDscr_Type(DisplayString):
    """Custom type agentFTPFileDscr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AgentFTPFileDscr_Type.__name__ = "DisplayString"
_AgentFTPFileDscr_Object = MibTableColumn
agentFTPFileDscr = _AgentFTPFileDscr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 21, 1, 2),
    _AgentFTPFileDscr_Type()
)
agentFTPFileDscr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentFTPFileDscr.setStatus("current")


class _AgentFTPFileLoadType_Type(Integer32):
    """Custom type agentFTPFileLoadType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("download", 3),
          ("other", 1),
          ("upload", 2))
    )


_AgentFTPFileLoadType_Type.__name__ = "Integer32"
_AgentFTPFileLoadType_Object = MibTableColumn
agentFTPFileLoadType = _AgentFTPFileLoadType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 21, 1, 3),
    _AgentFTPFileLoadType_Type()
)
agentFTPFileLoadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentFTPFileLoadType.setStatus("current")
_AgentFTPFileAddr_Type = IpAddress
_AgentFTPFileAddr_Object = MibTableColumn
agentFTPFileAddr = _AgentFTPFileAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 21, 1, 4),
    _AgentFTPFileAddr_Type()
)
agentFTPFileAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentFTPFileAddr.setStatus("current")
_AgentFTPTCPPort_Type = Integer32
_AgentFTPTCPPort_Object = MibTableColumn
agentFTPTCPPort = _AgentFTPTCPPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 21, 1, 5),
    _AgentFTPTCPPort_Type()
)
agentFTPTCPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentFTPTCPPort.setStatus("current")


class _AgentFTPFileName_Type(DisplayString):
    """Custom type agentFTPFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AgentFTPFileName_Type.__name__ = "DisplayString"
_AgentFTPFileName_Object = MibTableColumn
agentFTPFileName = _AgentFTPFileName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 21, 1, 6),
    _AgentFTPFileName_Type()
)
agentFTPFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentFTPFileName.setStatus("current")
_AgentFTPUserName_Type = DisplayString
_AgentFTPUserName_Object = MibTableColumn
agentFTPUserName = _AgentFTPUserName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 21, 1, 7),
    _AgentFTPUserName_Type()
)
agentFTPUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentFTPUserName.setStatus("current")
_AgentFTPPassword_Type = DisplayString
_AgentFTPPassword_Object = MibTableColumn
agentFTPPassword = _AgentFTPPassword_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 21, 1, 8),
    _AgentFTPPassword_Type()
)
agentFTPPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentFTPPassword.setStatus("current")
_AgentFTPFileCtrlID_Type = Integer32
_AgentFTPFileCtrlID_Object = MibTableColumn
agentFTPFileCtrlID = _AgentFTPFileCtrlID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 21, 1, 9),
    _AgentFTPFileCtrlID_Type()
)
agentFTPFileCtrlID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentFTPFileCtrlID.setStatus("current")
_AgentFTPFileBIncrement_Type = TruthValue
_AgentFTPFileBIncrement_Object = MibTableColumn
agentFTPFileBIncrement = _AgentFTPFileBIncrement_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 21, 1, 10),
    _AgentFTPFileBIncrement_Type()
)
agentFTPFileBIncrement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentFTPFileBIncrement.setStatus("current")


class _AgentFTPFileCtrl_Type(Integer32):
    """Custom type agentFTPFileCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("start", 2))
    )


_AgentFTPFileCtrl_Type.__name__ = "Integer32"
_AgentFTPFileCtrl_Object = MibTableColumn
agentFTPFileCtrl = _AgentFTPFileCtrl_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 21, 1, 11),
    _AgentFTPFileCtrl_Type()
)
agentFTPFileCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentFTPFileCtrl.setStatus("current")
_AgentFTPFileBootUpImage_Type = TruthValue
_AgentFTPFileBootUpImage_Object = MibTableColumn
agentFTPFileBootUpImage = _AgentFTPFileBootUpImage_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 21, 1, 12),
    _AgentFTPFileBootUpImage_Type()
)
agentFTPFileBootUpImage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentFTPFileBootUpImage.setStatus("current")
_AgentFTPFileForceAgree_Type = TruthValue
_AgentFTPFileForceAgree_Object = MibTableColumn
agentFTPFileForceAgree = _AgentFTPFileForceAgree_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 21, 1, 13),
    _AgentFTPFileForceAgree_Type()
)
agentFTPFileForceAgree.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentFTPFileForceAgree.setStatus("current")
_AgentFTPFileIPv6Addr_Type = DisplayString
_AgentFTPFileIPv6Addr_Object = MibTableColumn
agentFTPFileIPv6Addr = _AgentFTPFileIPv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 21, 1, 14),
    _AgentFTPFileIPv6Addr_Type()
)
agentFTPFileIPv6Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentFTPFileIPv6Addr.setStatus("current")
_AgentFTPFileInterfaceName_Type = DisplayString
_AgentFTPFileInterfaceName_Object = MibTableColumn
agentFTPFileInterfaceName = _AgentFTPFileInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 21, 1, 15),
    _AgentFTPFileInterfaceName_Type()
)
agentFTPFileInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentFTPFileInterfaceName.setStatus("current")
_AgentFTPFileUnitID_Type = UnitList
_AgentFTPFileUnitID_Object = MibTableColumn
agentFTPFileUnitID = _AgentFTPFileUnitID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 21, 1, 16),
    _AgentFTPFileUnitID_Type()
)
agentFTPFileUnitID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentFTPFileUnitID.setStatus("current")


class _AgentSnmpTrapState_Type(Integer32):
    """Custom type agentSnmpTrapState based on Integer32"""
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


_AgentSnmpTrapState_Type.__name__ = "Integer32"
_AgentSnmpTrapState_Object = MibScalar
agentSnmpTrapState = _AgentSnmpTrapState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 22),
    _AgentSnmpTrapState_Type()
)
agentSnmpTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSnmpTrapState.setStatus("current")
_AgentOutOfBandMgmt_ObjectIdentity = ObjectIdentity
agentOutOfBandMgmt = _AgentOutOfBandMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 23)
)


class _AgentOutOfBandMgmtState_Type(Integer32):
    """Custom type agentOutOfBandMgmtState based on Integer32"""
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


_AgentOutOfBandMgmtState_Type.__name__ = "Integer32"
_AgentOutOfBandMgmtState_Object = MibScalar
agentOutOfBandMgmtState = _AgentOutOfBandMgmtState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 23, 1),
    _AgentOutOfBandMgmtState_Type()
)
agentOutOfBandMgmtState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentOutOfBandMgmtState.setStatus("current")
_AgentOutOfBandMgmtIpAddr_Type = IpAddress
_AgentOutOfBandMgmtIpAddr_Object = MibScalar
agentOutOfBandMgmtIpAddr = _AgentOutOfBandMgmtIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 23, 2),
    _AgentOutOfBandMgmtIpAddr_Type()
)
agentOutOfBandMgmtIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentOutOfBandMgmtIpAddr.setStatus("current")
_AgentOutOfBandMgmtSubnetMask_Type = IpAddress
_AgentOutOfBandMgmtSubnetMask_Object = MibScalar
agentOutOfBandMgmtSubnetMask = _AgentOutOfBandMgmtSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 23, 3),
    _AgentOutOfBandMgmtSubnetMask_Type()
)
agentOutOfBandMgmtSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentOutOfBandMgmtSubnetMask.setStatus("current")
_AgentOutOfBandMgmtGateway_Type = IpAddress
_AgentOutOfBandMgmtGateway_Object = MibScalar
agentOutOfBandMgmtGateway = _AgentOutOfBandMgmtGateway_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 23, 4),
    _AgentOutOfBandMgmtGateway_Type()
)
agentOutOfBandMgmtGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentOutOfBandMgmtGateway.setStatus("current")


class _AgentOutOfBandMgmtLinkStatus_Type(Integer32):
    """Custom type agentOutOfBandMgmtLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("link-down", 2),
          ("link-up", 1))
    )


_AgentOutOfBandMgmtLinkStatus_Type.__name__ = "Integer32"
_AgentOutOfBandMgmtLinkStatus_Object = MibScalar
agentOutOfBandMgmtLinkStatus = _AgentOutOfBandMgmtLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 23, 5),
    _AgentOutOfBandMgmtLinkStatus_Type()
)
agentOutOfBandMgmtLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentOutOfBandMgmtLinkStatus.setStatus("current")
_AgentTrapMgmt_ObjectIdentity = ObjectIdentity
agentTrapMgmt = _AgentTrapMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 24)
)


class _AgentTrapColdStart_Type(Integer32):
    """Custom type agentTrapColdStart based on Integer32"""
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


_AgentTrapColdStart_Type.__name__ = "Integer32"
_AgentTrapColdStart_Object = MibScalar
agentTrapColdStart = _AgentTrapColdStart_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 24, 1),
    _AgentTrapColdStart_Type()
)
agentTrapColdStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTrapColdStart.setStatus("current")


class _AgentTrapWarmStart_Type(Integer32):
    """Custom type agentTrapWarmStart based on Integer32"""
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


_AgentTrapWarmStart_Type.__name__ = "Integer32"
_AgentTrapWarmStart_Object = MibScalar
agentTrapWarmStart = _AgentTrapWarmStart_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 24, 2),
    _AgentTrapWarmStart_Type()
)
agentTrapWarmStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTrapWarmStart.setStatus("current")


class _AgentTrapRmonRisingAlarm_Type(Integer32):
    """Custom type agentTrapRmonRisingAlarm based on Integer32"""
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


_AgentTrapRmonRisingAlarm_Type.__name__ = "Integer32"
_AgentTrapRmonRisingAlarm_Object = MibScalar
agentTrapRmonRisingAlarm = _AgentTrapRmonRisingAlarm_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 24, 3),
    _AgentTrapRmonRisingAlarm_Type()
)
agentTrapRmonRisingAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTrapRmonRisingAlarm.setStatus("current")


class _AgentTrapRmonFallingAlarm_Type(Integer32):
    """Custom type agentTrapRmonFallingAlarm based on Integer32"""
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


_AgentTrapRmonFallingAlarm_Type.__name__ = "Integer32"
_AgentTrapRmonFallingAlarm_Object = MibScalar
agentTrapRmonFallingAlarm = _AgentTrapRmonFallingAlarm_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 24, 4),
    _AgentTrapRmonFallingAlarm_Type()
)
agentTrapRmonFallingAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTrapRmonFallingAlarm.setStatus("current")


class _AgentTrapCfgSave_Type(Integer32):
    """Custom type agentTrapCfgSave based on Integer32"""
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


_AgentTrapCfgSave_Type.__name__ = "Integer32"
_AgentTrapCfgSave_Object = MibScalar
agentTrapCfgSave = _AgentTrapCfgSave_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 24, 5),
    _AgentTrapCfgSave_Type()
)
agentTrapCfgSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTrapCfgSave.setStatus("current")


class _AgentTrapCfgUpload_Type(Integer32):
    """Custom type agentTrapCfgUpload based on Integer32"""
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


_AgentTrapCfgUpload_Type.__name__ = "Integer32"
_AgentTrapCfgUpload_Object = MibScalar
agentTrapCfgUpload = _AgentTrapCfgUpload_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 24, 6),
    _AgentTrapCfgUpload_Type()
)
agentTrapCfgUpload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTrapCfgUpload.setStatus("current")


class _AgentTrapCfgDownload_Type(Integer32):
    """Custom type agentTrapCfgDownload based on Integer32"""
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


_AgentTrapCfgDownload_Type.__name__ = "Integer32"
_AgentTrapCfgDownload_Object = MibScalar
agentTrapCfgDownload = _AgentTrapCfgDownload_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 24, 7),
    _AgentTrapCfgDownload_Type()
)
agentTrapCfgDownload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTrapCfgDownload.setStatus("current")
_AgentFTPFileSystemTable_Object = MibTable
agentFTPFileSystemTable = _AgentFTPFileSystemTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 25)
)
if mibBuilder.loadTexts:
    agentFTPFileSystemTable.setStatus("current")
_AgentFTPFileSystemEntry_Object = MibTableRow
agentFTPFileSystemEntry = _AgentFTPFileSystemEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 25, 1)
)
agentFTPFileSystemEntry.setIndexNames(
    (0, "AGENT-GENERAL-MIB", "agentFTPFileSystemIndex"),
)
if mibBuilder.loadTexts:
    agentFTPFileSystemEntry.setStatus("current")
_AgentFTPFileSystemIndex_Type = Integer32
_AgentFTPFileSystemIndex_Object = MibTableColumn
agentFTPFileSystemIndex = _AgentFTPFileSystemIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 25, 1, 1),
    _AgentFTPFileSystemIndex_Type()
)
agentFTPFileSystemIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentFTPFileSystemIndex.setStatus("current")
_AgentFTPFileSystemDscr_Type = DisplayString
_AgentFTPFileSystemDscr_Object = MibTableColumn
agentFTPFileSystemDscr = _AgentFTPFileSystemDscr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 25, 1, 2),
    _AgentFTPFileSystemDscr_Type()
)
agentFTPFileSystemDscr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentFTPFileSystemDscr.setStatus("current")


class _AgentFTPFileSystemLoadType_Type(Integer32):
    """Custom type agentFTPFileSystemLoadType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("download", 3),
          ("other", 1),
          ("upload", 2))
    )


_AgentFTPFileSystemLoadType_Type.__name__ = "Integer32"
_AgentFTPFileSystemLoadType_Object = MibTableColumn
agentFTPFileSystemLoadType = _AgentFTPFileSystemLoadType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 25, 1, 3),
    _AgentFTPFileSystemLoadType_Type()
)
agentFTPFileSystemLoadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentFTPFileSystemLoadType.setStatus("current")
_AgentFTPFileSystemAddressType_Type = InetAddressType
_AgentFTPFileSystemAddressType_Object = MibTableColumn
agentFTPFileSystemAddressType = _AgentFTPFileSystemAddressType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 25, 1, 4),
    _AgentFTPFileSystemAddressType_Type()
)
agentFTPFileSystemAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentFTPFileSystemAddressType.setStatus("current")
_AgentFTPFileSystemAddress_Type = InetAddress
_AgentFTPFileSystemAddress_Object = MibTableColumn
agentFTPFileSystemAddress = _AgentFTPFileSystemAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 25, 1, 5),
    _AgentFTPFileSystemAddress_Type()
)
agentFTPFileSystemAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentFTPFileSystemAddress.setStatus("current")
_AgentFTPFileSystemTCPPort_Type = Integer32
_AgentFTPFileSystemTCPPort_Object = MibTableColumn
agentFTPFileSystemTCPPort = _AgentFTPFileSystemTCPPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 25, 1, 6),
    _AgentFTPFileSystemTCPPort_Type()
)
agentFTPFileSystemTCPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentFTPFileSystemTCPPort.setStatus("current")


class _AgentFTPFileSystemServerFileName_Type(DisplayString):
    """Custom type agentFTPFileSystemServerFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AgentFTPFileSystemServerFileName_Type.__name__ = "DisplayString"
_AgentFTPFileSystemServerFileName_Object = MibTableColumn
agentFTPFileSystemServerFileName = _AgentFTPFileSystemServerFileName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 25, 1, 7),
    _AgentFTPFileSystemServerFileName_Type()
)
agentFTPFileSystemServerFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentFTPFileSystemServerFileName.setStatus("current")


class _AgentFTPFileSystemDeviceFileName_Type(DisplayString):
    """Custom type agentFTPFileSystemDeviceFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AgentFTPFileSystemDeviceFileName_Type.__name__ = "DisplayString"
_AgentFTPFileSystemDeviceFileName_Object = MibTableColumn
agentFTPFileSystemDeviceFileName = _AgentFTPFileSystemDeviceFileName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 25, 1, 8),
    _AgentFTPFileSystemDeviceFileName_Type()
)
agentFTPFileSystemDeviceFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentFTPFileSystemDeviceFileName.setStatus("current")
_AgentFTPFileSystemUserName_Type = DisplayString
_AgentFTPFileSystemUserName_Object = MibTableColumn
agentFTPFileSystemUserName = _AgentFTPFileSystemUserName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 25, 1, 9),
    _AgentFTPFileSystemUserName_Type()
)
agentFTPFileSystemUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentFTPFileSystemUserName.setStatus("current")
_AgentFTPFileSystemPassword_Type = DisplayString
_AgentFTPFileSystemPassword_Object = MibTableColumn
agentFTPFileSystemPassword = _AgentFTPFileSystemPassword_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 25, 1, 10),
    _AgentFTPFileSystemPassword_Type()
)
agentFTPFileSystemPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentFTPFileSystemPassword.setStatus("current")
_AgentFTPFileSystemCtrlUnitID_Type = UnitList
_AgentFTPFileSystemCtrlUnitID_Object = MibTableColumn
agentFTPFileSystemCtrlUnitID = _AgentFTPFileSystemCtrlUnitID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 25, 1, 11),
    _AgentFTPFileSystemCtrlUnitID_Type()
)
agentFTPFileSystemCtrlUnitID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentFTPFileSystemCtrlUnitID.setStatus("current")
_AgentFTPFileSystemBootUpImage_Type = TruthValue
_AgentFTPFileSystemBootUpImage_Object = MibTableColumn
agentFTPFileSystemBootUpImage = _AgentFTPFileSystemBootUpImage_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 25, 1, 12),
    _AgentFTPFileSystemBootUpImage_Type()
)
agentFTPFileSystemBootUpImage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentFTPFileSystemBootUpImage.setStatus("current")


class _AgentFTPFileSystemCtrl_Type(Integer32):
    """Custom type agentFTPFileSystemCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("start", 2))
    )


_AgentFTPFileSystemCtrl_Type.__name__ = "Integer32"
_AgentFTPFileSystemCtrl_Object = MibTableColumn
agentFTPFileSystemCtrl = _AgentFTPFileSystemCtrl_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 25, 1, 13),
    _AgentFTPFileSystemCtrl_Type()
)
agentFTPFileSystemCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentFTPFileSystemCtrl.setStatus("current")


class _AgentBscCMDLogState_Type(Integer32):
    """Custom type agentBscCMDLogState based on Integer32"""
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


_AgentBscCMDLogState_Type.__name__ = "Integer32"
_AgentBscCMDLogState_Object = MibScalar
agentBscCMDLogState = _AgentBscCMDLogState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 26),
    _AgentBscCMDLogState_Type()
)
agentBscCMDLogState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentBscCMDLogState.setStatus("current")


class _AgentBscBroadcastPingReplyState_Type(Integer32):
    """Custom type agentBscBroadcastPingReplyState based on Integer32"""
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


_AgentBscBroadcastPingReplyState_Type.__name__ = "Integer32"
_AgentBscBroadcastPingReplyState_Object = MibScalar
agentBscBroadcastPingReplyState = _AgentBscBroadcastPingReplyState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 27),
    _AgentBscBroadcastPingReplyState_Type()
)
agentBscBroadcastPingReplyState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentBscBroadcastPingReplyState.setStatus("current")
_AgentBscTftpConfigMgmt_ObjectIdentity = ObjectIdentity
agentBscTftpConfigMgmt = _AgentBscTftpConfigMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 28)
)


class _AgentBscTftpCfgFirmwareFile_Type(DisplayString):
    """Custom type agentBscTftpCfgFirmwareFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AgentBscTftpCfgFirmwareFile_Type.__name__ = "DisplayString"
_AgentBscTftpCfgFirmwareFile_Object = MibScalar
agentBscTftpCfgFirmwareFile = _AgentBscTftpCfgFirmwareFile_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 28, 1),
    _AgentBscTftpCfgFirmwareFile_Type()
)
agentBscTftpCfgFirmwareFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentBscTftpCfgFirmwareFile.setStatus("current")


class _AgentBscTftpCfgConfigFile_Type(DisplayString):
    """Custom type agentBscTftpCfgConfigFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AgentBscTftpCfgConfigFile_Type.__name__ = "DisplayString"
_AgentBscTftpCfgConfigFile_Object = MibScalar
agentBscTftpCfgConfigFile = _AgentBscTftpCfgConfigFile_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 28, 2),
    _AgentBscTftpCfgConfigFile_Type()
)
agentBscTftpCfgConfigFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentBscTftpCfgConfigFile.setStatus("current")


class _AgentBscTftpCfgLogFile_Type(DisplayString):
    """Custom type agentBscTftpCfgLogFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AgentBscTftpCfgLogFile_Type.__name__ = "DisplayString"
_AgentBscTftpCfgLogFile_Object = MibScalar
agentBscTftpCfgLogFile = _AgentBscTftpCfgLogFile_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 28, 3),
    _AgentBscTftpCfgLogFile_Type()
)
agentBscTftpCfgLogFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentBscTftpCfgLogFile.setStatus("current")


class _AgentBscTftpCfgAttackLogFile_Type(DisplayString):
    """Custom type agentBscTftpCfgAttackLogFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AgentBscTftpCfgAttackLogFile_Type.__name__ = "DisplayString"
_AgentBscTftpCfgAttackLogFile_Object = MibScalar
agentBscTftpCfgAttackLogFile = _AgentBscTftpCfgAttackLogFile_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 28, 4),
    _AgentBscTftpCfgAttackLogFile_Type()
)
agentBscTftpCfgAttackLogFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentBscTftpCfgAttackLogFile.setStatus("current")


class _AgentBscTftpCfgCertificateFile_Type(DisplayString):
    """Custom type agentBscTftpCfgCertificateFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AgentBscTftpCfgCertificateFile_Type.__name__ = "DisplayString"
_AgentBscTftpCfgCertificateFile_Object = MibScalar
agentBscTftpCfgCertificateFile = _AgentBscTftpCfgCertificateFile_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 28, 5),
    _AgentBscTftpCfgCertificateFile_Type()
)
agentBscTftpCfgCertificateFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentBscTftpCfgCertificateFile.setStatus("current")


class _AgentBscTftpCfgKeyFile_Type(DisplayString):
    """Custom type agentBscTftpCfgKeyFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AgentBscTftpCfgKeyFile_Type.__name__ = "DisplayString"
_AgentBscTftpCfgKeyFile_Object = MibScalar
agentBscTftpCfgKeyFile = _AgentBscTftpCfgKeyFile_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 28, 6),
    _AgentBscTftpCfgKeyFile_Type()
)
agentBscTftpCfgKeyFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentBscTftpCfgKeyFile.setStatus("current")


class _AgentBscTftpCfgTechSuooprtFile_Type(DisplayString):
    """Custom type agentBscTftpCfgTechSuooprtFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AgentBscTftpCfgTechSuooprtFile_Type.__name__ = "DisplayString"
_AgentBscTftpCfgTechSuooprtFile_Object = MibScalar
agentBscTftpCfgTechSuooprtFile = _AgentBscTftpCfgTechSuooprtFile_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 28, 7),
    _AgentBscTftpCfgTechSuooprtFile_Type()
)
agentBscTftpCfgTechSuooprtFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentBscTftpCfgTechSuooprtFile.setStatus("current")


class _AgentBscTftpCfgDebugLogFile_Type(DisplayString):
    """Custom type agentBscTftpCfgDebugLogFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AgentBscTftpCfgDebugLogFile_Type.__name__ = "DisplayString"
_AgentBscTftpCfgDebugLogFile_Object = MibScalar
agentBscTftpCfgDebugLogFile = _AgentBscTftpCfgDebugLogFile_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 28, 8),
    _AgentBscTftpCfgDebugLogFile_Type()
)
agentBscTftpCfgDebugLogFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentBscTftpCfgDebugLogFile.setStatus("current")


class _AgentBscTftpCfgSIMFirmwareFile_Type(DisplayString):
    """Custom type agentBscTftpCfgSIMFirmwareFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AgentBscTftpCfgSIMFirmwareFile_Type.__name__ = "DisplayString"
_AgentBscTftpCfgSIMFirmwareFile_Object = MibScalar
agentBscTftpCfgSIMFirmwareFile = _AgentBscTftpCfgSIMFirmwareFile_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 28, 9),
    _AgentBscTftpCfgSIMFirmwareFile_Type()
)
agentBscTftpCfgSIMFirmwareFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentBscTftpCfgSIMFirmwareFile.setStatus("current")


class _AgentBscTftpCfgSIMConfigFile_Type(DisplayString):
    """Custom type agentBscTftpCfgSIMConfigFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AgentBscTftpCfgSIMConfigFile_Type.__name__ = "DisplayString"
_AgentBscTftpCfgSIMConfigFile_Object = MibScalar
agentBscTftpCfgSIMConfigFile = _AgentBscTftpCfgSIMConfigFile_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 28, 10),
    _AgentBscTftpCfgSIMConfigFile_Type()
)
agentBscTftpCfgSIMConfigFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentBscTftpCfgSIMConfigFile.setStatus("current")


class _AgentBscTftpCfgSIMLogFile_Type(DisplayString):
    """Custom type agentBscTftpCfgSIMLogFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AgentBscTftpCfgSIMLogFile_Type.__name__ = "DisplayString"
_AgentBscTftpCfgSIMLogFile_Object = MibScalar
agentBscTftpCfgSIMLogFile = _AgentBscTftpCfgSIMLogFile_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 28, 11),
    _AgentBscTftpCfgSIMLogFile_Type()
)
agentBscTftpCfgSIMLogFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentBscTftpCfgSIMLogFile.setStatus("current")
_AgentBscTftpCfgServerIPAddr_Type = IpAddress
_AgentBscTftpCfgServerIPAddr_Object = MibScalar
agentBscTftpCfgServerIPAddr = _AgentBscTftpCfgServerIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 28, 12),
    _AgentBscTftpCfgServerIPAddr_Type()
)
agentBscTftpCfgServerIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentBscTftpCfgServerIPAddr.setStatus("current")
_AgentBscTftpCfgServerIPv6Addr_Type = Ipv6Address
_AgentBscTftpCfgServerIPv6Addr_Object = MibScalar
agentBscTftpCfgServerIPv6Addr = _AgentBscTftpCfgServerIPv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 28, 13),
    _AgentBscTftpCfgServerIPv6Addr_Type()
)
agentBscTftpCfgServerIPv6Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentBscTftpCfgServerIPv6Addr.setStatus("current")


class _AgentBscTftpCfgServerDomainName_Type(DisplayString):
    """Custom type agentBscTftpCfgServerDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AgentBscTftpCfgServerDomainName_Type.__name__ = "DisplayString"
_AgentBscTftpCfgServerDomainName_Object = MibScalar
agentBscTftpCfgServerDomainName = _AgentBscTftpCfgServerDomainName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 28, 14),
    _AgentBscTftpCfgServerDomainName_Type()
)
agentBscTftpCfgServerDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentBscTftpCfgServerDomainName.setStatus("current")


class _AgentBscCommunityEncryptionState_Type(Integer32):
    """Custom type agentBscCommunityEncryptionState based on Integer32"""
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


_AgentBscCommunityEncryptionState_Type.__name__ = "Integer32"
_AgentBscCommunityEncryptionState_Object = MibScalar
agentBscCommunityEncryptionState = _AgentBscCommunityEncryptionState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 29),
    _AgentBscCommunityEncryptionState_Type()
)
agentBscCommunityEncryptionState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentBscCommunityEncryptionState.setStatus("current")
_AgentIpProtoConfig_ObjectIdentity = ObjectIdentity
agentIpProtoConfig = _AgentIpProtoConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 3)
)
_AgentIpNumOfIf_Type = Integer32
_AgentIpNumOfIf_Object = MibScalar
agentIpNumOfIf = _AgentIpNumOfIf_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 3, 1),
    _AgentIpNumOfIf_Type()
)
agentIpNumOfIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIpNumOfIf.setStatus("current")
_AgentIpTftpServerAddr_Type = IpAddress
_AgentIpTftpServerAddr_Object = MibScalar
agentIpTftpServerAddr = _AgentIpTftpServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 3, 2),
    _AgentIpTftpServerAddr_Type()
)
agentIpTftpServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIpTftpServerAddr.setStatus("obsolete")


class _AgentIpGetIpFrom_Type(Integer32):
    """Custom type agentIpGetIpFrom based on Integer32"""
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
        *(("bootp", 3),
          ("dhcp", 4),
          ("disabled", 2),
          ("other", 1))
    )


_AgentIpGetIpFrom_Type.__name__ = "Integer32"
_AgentIpGetIpFrom_Object = MibScalar
agentIpGetIpFrom = _AgentIpGetIpFrom_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 3, 3),
    _AgentIpGetIpFrom_Type()
)
agentIpGetIpFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIpGetIpFrom.setStatus("current")


class _AgentIpAutoconfig_Type(Integer32):
    """Custom type agentIpAutoconfig based on Integer32"""
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


_AgentIpAutoconfig_Type.__name__ = "Integer32"
_AgentIpAutoconfig_Object = MibScalar
agentIpAutoconfig = _AgentIpAutoconfig_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 3, 4),
    _AgentIpAutoconfig_Type()
)
agentIpAutoconfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIpAutoconfig.setStatus("current")
_AgentIpAutoconfigTimeout_Type = Integer32
_AgentIpAutoconfigTimeout_Object = MibScalar
agentIpAutoconfigTimeout = _AgentIpAutoconfigTimeout_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 3, 5),
    _AgentIpAutoconfigTimeout_Type()
)
agentIpAutoconfigTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIpAutoconfigTimeout.setStatus("current")
_AgentIpTrapManager_ObjectIdentity = ObjectIdentity
agentIpTrapManager = _AgentIpTrapManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 4)
)
_AgentTrapManagerTable_Object = MibTable
agentTrapManagerTable = _AgentTrapManagerTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 4, 2)
)
if mibBuilder.loadTexts:
    agentTrapManagerTable.setStatus("current")
_AgentTrapManagerEntry_Object = MibTableRow
agentTrapManagerEntry = _AgentTrapManagerEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 4, 2, 1)
)
agentTrapManagerEntry.setIndexNames(
    (0, "AGENT-GENERAL-MIB", "agentTrapManagerIndex"),
)
if mibBuilder.loadTexts:
    agentTrapManagerEntry.setStatus("current")


class _AgentTrapManagerIndex_Type(Integer32):
    """Custom type agentTrapManagerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AgentTrapManagerIndex_Type.__name__ = "Integer32"
_AgentTrapManagerIndex_Object = MibTableColumn
agentTrapManagerIndex = _AgentTrapManagerIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 4, 2, 1, 1),
    _AgentTrapManagerIndex_Type()
)
agentTrapManagerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentTrapManagerIndex.setStatus("current")
_AgentTrapManagerIpAddr_Type = IpAddress
_AgentTrapManagerIpAddr_Object = MibTableColumn
agentTrapManagerIpAddr = _AgentTrapManagerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 4, 2, 1, 2),
    _AgentTrapManagerIpAddr_Type()
)
agentTrapManagerIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTrapManagerIpAddr.setStatus("current")


class _AgentTrapManagerComm_Type(DisplayString):
    """Custom type agentTrapManagerComm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AgentTrapManagerComm_Type.__name__ = "DisplayString"
_AgentTrapManagerComm_Object = MibTableColumn
agentTrapManagerComm = _AgentTrapManagerComm_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 4, 2, 1, 3),
    _AgentTrapManagerComm_Type()
)
agentTrapManagerComm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTrapManagerComm.setStatus("current")


class _AgentTrapManagerMsgVer_Type(Integer32):
    """Custom type agentTrapManagerMsgVer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("snmpAgentVersionDependent", 1),
          ("v1Trap", 2),
          ("v2Trap", 3))
    )


_AgentTrapManagerMsgVer_Type.__name__ = "Integer32"
_AgentTrapManagerMsgVer_Object = MibTableColumn
agentTrapManagerMsgVer = _AgentTrapManagerMsgVer_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 4, 2, 1, 4),
    _AgentTrapManagerMsgVer_Type()
)
agentTrapManagerMsgVer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTrapManagerMsgVer.setStatus("current")


class _AgentTrapManagerStatus_Type(Integer32):
    """Custom type agentTrapManagerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_AgentTrapManagerStatus_Type.__name__ = "Integer32"
_AgentTrapManagerStatus_Object = MibTableColumn
agentTrapManagerStatus = _AgentTrapManagerStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 4, 2, 1, 5),
    _AgentTrapManagerStatus_Type()
)
agentTrapManagerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTrapManagerStatus.setStatus("current")
_AgentNotify_ObjectIdentity = ObjectIdentity
agentNotify = _AgentNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 7)
)
_AgentNotifMgmt_ObjectIdentity = ObjectIdentity
agentNotifMgmt = _AgentNotifMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 7, 1)
)
_NotifFirmwareMgmt_ObjectIdentity = ObjectIdentity
notifFirmwareMgmt = _NotifFirmwareMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 7, 1, 2)
)
_AgentNotifFirmware_ObjectIdentity = ObjectIdentity
agentNotifFirmware = _AgentNotifFirmware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 7, 2)
)
_AgentNotifyPrefix_ObjectIdentity = ObjectIdentity
agentNotifyPrefix = _AgentNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 7, 2, 0)
)
_NotificationBindings_ObjectIdentity = ObjectIdentity
notificationBindings = _NotificationBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 7, 2, 1)
)
_UnitID_Type = Integer32
_UnitID_Object = MibScalar
unitID = _UnitID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 7, 2, 1, 1),
    _UnitID_Type()
)
unitID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    unitID.setStatus("current")


class _TrapInfosystemRestart_Type(DisplayString):
    """Custom type trapInfosystemRestart based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TrapInfosystemRestart_Type.__name__ = "DisplayString"
_TrapInfosystemRestart_Object = MibScalar
trapInfosystemRestart = _TrapInfosystemRestart_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 7, 2, 1, 2),
    _TrapInfosystemRestart_Type()
)
trapInfosystemRestart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapInfosystemRestart.setStatus("current")
_AgentGratuitousARPIpAddr_Type = IpAddress
_AgentGratuitousARPIpAddr_Object = MibScalar
agentGratuitousARPIpAddr = _AgentGratuitousARPIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 7, 2, 1, 3),
    _AgentGratuitousARPIpAddr_Type()
)
agentGratuitousARPIpAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    agentGratuitousARPIpAddr.setStatus("current")
_AgentGratuitousARPMacAddr_Type = MacAddress
_AgentGratuitousARPMacAddr_Object = MibScalar
agentGratuitousARPMacAddr = _AgentGratuitousARPMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 7, 2, 1, 4),
    _AgentGratuitousARPMacAddr_Type()
)
agentGratuitousARPMacAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    agentGratuitousARPMacAddr.setStatus("current")
_AgentGratuitousARPPortNumber_Type = DisplayString
_AgentGratuitousARPPortNumber_Object = MibScalar
agentGratuitousARPPortNumber = _AgentGratuitousARPPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 7, 2, 1, 5),
    _AgentGratuitousARPPortNumber_Type()
)
agentGratuitousARPPortNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    agentGratuitousARPPortNumber.setStatus("current")


class _AgentLoginType_Type(Integer32):
    """Custom type agentLoginType based on Integer32"""
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
        *(("console", 1),
          ("ssh", 5),
          ("ssl", 4),
          ("telnet", 2),
          ("web", 3))
    )


_AgentLoginType_Type.__name__ = "Integer32"
_AgentLoginType_Object = MibScalar
agentLoginType = _AgentLoginType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 7, 2, 1, 6),
    _AgentLoginType_Type()
)
agentLoginType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    agentLoginType.setStatus("current")


class _AgentLoginAAAMethod_Type(Integer32):
    """Custom type agentLoginAAAMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("local", 2),
          ("none", 1),
          ("server", 3))
    )


_AgentLoginAAAMethod_Type.__name__ = "Integer32"
_AgentLoginAAAMethod_Object = MibScalar
agentLoginAAAMethod = _AgentLoginAAAMethod_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 7, 2, 1, 7),
    _AgentLoginAAAMethod_Type()
)
agentLoginAAAMethod.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    agentLoginAAAMethod.setStatus("current")
_AgentLoginUserName_Type = DisplayString
_AgentLoginUserName_Object = MibScalar
agentLoginUserName = _AgentLoginUserName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 7, 2, 1, 8),
    _AgentLoginUserName_Type()
)
agentLoginUserName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    agentLoginUserName.setStatus("current")
_AgentLoginIpAddr_Type = IpAddress
_AgentLoginIpAddr_Object = MibScalar
agentLoginIpAddr = _AgentLoginIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 7, 2, 1, 9),
    _AgentLoginIpAddr_Type()
)
agentLoginIpAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    agentLoginIpAddr.setStatus("current")
_AgentLoginMacAddr_Type = MacAddress
_AgentLoginMacAddr_Object = MibScalar
agentLoginMacAddr = _AgentLoginMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 7, 2, 1, 10),
    _AgentLoginMacAddr_Type()
)
agentLoginMacAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    agentLoginMacAddr.setStatus("current")
_AgentLoginAAAServerAddr_Type = IpAddress
_AgentLoginAAAServerAddr_Object = MibScalar
agentLoginAAAServerAddr = _AgentLoginAAAServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 7, 2, 1, 11),
    _AgentLoginAAAServerAddr_Type()
)
agentLoginAAAServerAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    agentLoginAAAServerAddr.setStatus("current")


class _AgentLoginFailInfo_Type(Integer32):
    """Custom type agentLoginFailInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("authenticate-fail", 2),
          ("other", 1),
          ("server-timeout", 3))
    )


_AgentLoginFailInfo_Type.__name__ = "Integer32"
_AgentLoginFailInfo_Object = MibScalar
agentLoginFailInfo = _AgentLoginFailInfo_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 7, 2, 1, 12),
    _AgentLoginFailInfo_Type()
)
agentLoginFailInfo.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    agentLoginFailInfo.setStatus("current")


class _AgentAccessFlashOper_Type(DisplayString):
    """Custom type agentAccessFlashOper based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AgentAccessFlashOper_Type.__name__ = "DisplayString"
_AgentAccessFlashOper_Object = MibScalar
agentAccessFlashOper = _AgentAccessFlashOper_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 7, 2, 1, 13),
    _AgentAccessFlashOper_Type()
)
agentAccessFlashOper.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    agentAccessFlashOper.setStatus("current")
_AgentAccessFlashAddr_Type = Integer32
_AgentAccessFlashAddr_Object = MibScalar
agentAccessFlashAddr = _AgentAccessFlashAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 7, 2, 1, 14),
    _AgentAccessFlashAddr_Type()
)
agentAccessFlashAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    agentAccessFlashAddr.setStatus("current")


class _AgentCfgOperate_Type(Integer32):
    """Custom type agentCfgOperate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("download", 3),
          ("save", 1),
          ("upload", 2))
    )


_AgentCfgOperate_Type.__name__ = "Integer32"
_AgentCfgOperate_Object = MibScalar
agentCfgOperate = _AgentCfgOperate_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 7, 2, 1, 15),
    _AgentCfgOperate_Type()
)
agentCfgOperate.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    agentCfgOperate.setStatus("current")

# Managed Objects groups


# Notification objects

agentsystemRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 7, 2, 0, 1)
)
agentsystemRestart.setObjects(
    ("AGENT-GENERAL-MIB", "trapInfosystemRestart")
)
if mibBuilder.loadTexts:
    agentsystemRestart.setStatus(
        "current"
    )

agentSaveToNVRAM = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 7, 2, 0, 2)
)
agentSaveToNVRAM.setObjects(
    ("AGENT-GENERAL-MIB", "unitID")
)
if mibBuilder.loadTexts:
    agentSaveToNVRAM.setStatus(
        "current"
    )

agentFileTransferStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 7, 2, 0, 3)
)
agentFileTransferStatusChange.setObjects(
      *(("AGENT-GENERAL-MIB", "unitID"),
        ("AGENT-GENERAL-MIB", "agentStatusFileTransfer"))
)
if mibBuilder.loadTexts:
    agentFileTransferStatusChange.setStatus(
        "current"
    )

agentSetToFactoryDefault = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 7, 2, 0, 4)
)
agentSetToFactoryDefault.setObjects(
    ("AGENT-GENERAL-MIB", "unitID")
)
if mibBuilder.loadTexts:
    agentSetToFactoryDefault.setStatus(
        "current"
    )

agentGratuitousARPTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 7, 2, 0, 5)
)
agentGratuitousARPTrap.setObjects(
      *(("AGENT-GENERAL-MIB", "agentGratuitousARPIpAddr"),
        ("AGENT-GENERAL-MIB", "agentGratuitousARPMacAddr"),
        ("AGENT-GENERAL-MIB", "agentGratuitousARPPortNumber"),
        ("AGENT-GENERAL-MIB", "agentGratuitousARPInterfaceName"))
)
if mibBuilder.loadTexts:
    agentGratuitousARPTrap.setStatus(
        "current"
    )

agentLoginFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 7, 2, 0, 6)
)
agentLoginFailTrap.setObjects(
      *(("AGENT-GENERAL-MIB", "agentLoginType"),
        ("AGENT-GENERAL-MIB", "agentLoginAAAMethod"),
        ("AGENT-GENERAL-MIB", "agentLoginUserName"),
        ("AGENT-GENERAL-MIB", "agentLoginIpAddr"),
        ("AGENT-GENERAL-MIB", "agentLoginMacAddr"),
        ("AGENT-GENERAL-MIB", "agentLoginAAAServerAddr"),
        ("AGENT-GENERAL-MIB", "agentLoginFailInfo"))
)
if mibBuilder.loadTexts:
    agentLoginFailTrap.setStatus(
        "current"
    )

agentFirmwareUpgrade = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 7, 2, 0, 7)
)
agentFirmwareUpgrade.setObjects(
    ("AGENT-GENERAL-MIB", "swMultiImageVersion")
)
if mibBuilder.loadTexts:
    agentFirmwareUpgrade.setStatus(
        "current"
    )

agentAccessFlashFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 7, 2, 0, 8)
)
agentAccessFlashFailed.setObjects(
      *(("AGENT-GENERAL-MIB", "agentAccessFlashOper"),
        ("AGENT-GENERAL-MIB", "agentAccessFlashAddr"))
)
if mibBuilder.loadTexts:
    agentAccessFlashFailed.setStatus(
        "current"
    )

agentCfgOperCompleteTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 7, 2, 0, 9)
)
agentCfgOperCompleteTrap.setObjects(
      *(("AGENT-GENERAL-MIB", "unitID"),
        ("AGENT-GENERAL-MIB", "agentCfgOperate"),
        ("AGENT-GENERAL-MIB", "agentLoginUserName"))
)
if mibBuilder.loadTexts:
    agentCfgOperCompleteTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AGENT-GENERAL-MIB",
    **{"Ipv6Address": Ipv6Address,
       "UnitList": UnitList,
       "agentGeneralMgmt": agentGeneralMgmt,
       "agentBasicInfo": agentBasicInfo,
       "agentMgmtProtocolCapability": agentMgmtProtocolCapability,
       "agentMibCapabilityTable": agentMibCapabilityTable,
       "agentMibCapabilityEntry": agentMibCapabilityEntry,
       "agentMibCapabilityIndex": agentMibCapabilityIndex,
       "agentMibCapabilityDescr": agentMibCapabilityDescr,
       "agentMibCapabilityVersion": agentMibCapabilityVersion,
       "agentMibCapabilityType": agentMibCapabilityType,
       "agentStatusConsoleInUse": agentStatusConsoleInUse,
       "agentStatusSaveCfg": agentStatusSaveCfg,
       "agentStatusFileTransfer": agentStatusFileTransfer,
       "agentCPUutilization": agentCPUutilization,
       "agentCPUutilizationIn5sec": agentCPUutilizationIn5sec,
       "agentCPUutilizationIn1min": agentCPUutilizationIn1min,
       "agentCPUutilizationIn5min": agentCPUutilizationIn5min,
       "agentDualImageStatus": agentDualImageStatus,
       "agentPORTutilizationTable": agentPORTutilizationTable,
       "agentPORTutilizationEntry": agentPORTutilizationEntry,
       "agentPORTutilizationProtIndex": agentPORTutilizationProtIndex,
       "agentPORTutilizationTX": agentPORTutilizationTX,
       "agentPORTutilizationRX": agentPORTutilizationRX,
       "agentPORTutilizationUtil": agentPORTutilizationUtil,
       "agentDRAMutilizationTable": agentDRAMutilizationTable,
       "agentDRAMutilizationEntry": agentDRAMutilizationEntry,
       "agentDRAMutilizationUnitID": agentDRAMutilizationUnitID,
       "agentDRAMutilizationTotalDRAM": agentDRAMutilizationTotalDRAM,
       "agentDRAMutilizationUsedDRAM": agentDRAMutilizationUsedDRAM,
       "agentDRAMutilization": agentDRAMutilization,
       "agentFLASHutilizationTable": agentFLASHutilizationTable,
       "agentFLASHutilizationEntry": agentFLASHutilizationEntry,
       "agentFLASHutilizationUnitID": agentFLASHutilizationUnitID,
       "agentFLASHutilizationTotalFLASH": agentFLASHutilizationTotalFLASH,
       "agentFLASHutilizationUsedFLASH": agentFLASHutilizationUsedFLASH,
       "agentFLASHutilization": agentFLASHutilization,
       "agentStatusReset": agentStatusReset,
       "agentSerialNumber": agentSerialNumber,
       "agentFirmwareType": agentFirmwareType,
       "agentBasicConfig": agentBasicConfig,
       "agentBscSwFileTable": agentBscSwFileTable,
       "agentBscSwFileEntry": agentBscSwFileEntry,
       "agentBscSwFileIndex": agentBscSwFileIndex,
       "agentBscSwFileDscr": agentBscSwFileDscr,
       "agentBscSwFileAddr": agentBscSwFileAddr,
       "agentBscSwFileTransferType": agentBscSwFileTransferType,
       "agentBscSwFile": agentBscSwFile,
       "agentBscSwFileLocateId": agentBscSwFileLocateId,
       "agentBscSwFileLoadType": agentBscSwFileLoadType,
       "agentBscSwFileCtrl": agentBscSwFileCtrl,
       "agentBscSwFileBIncrement": agentBscSwFileBIncrement,
       "agentBscSwFileCtrlID": agentBscSwFileCtrlID,
       "agentBscSwFileCtrlUnitID": agentBscSwFileCtrlUnitID,
       "agentBscSwFileIPv6Addr": agentBscSwFileIPv6Addr,
       "agentBscSwFileBootUpImage": agentBscSwFileBootUpImage,
       "agentBscSwFileForceAgree": agentBscSwFileForceAgree,
       "agentBscSwFileInterfaceName": agentBscSwFileInterfaceName,
       "agentBscSwFileServerDomainName": agentBscSwFileServerDomainName,
       "agentFileTransfer": agentFileTransfer,
       "agentSystemReset": agentSystemReset,
       "agentRs232PortConfig": agentRs232PortConfig,
       "agentOutOfBandBaudRateConfig": agentOutOfBandBaudRateConfig,
       "agentSaveCfg": agentSaveCfg,
       "swMultiImageInfoTable": swMultiImageInfoTable,
       "swMultiImageInfoEntry": swMultiImageInfoEntry,
       "swMultiImageInfoID": swMultiImageInfoID,
       "swMultiImageVersion": swMultiImageVersion,
       "swMultiImageSize": swMultiImageSize,
       "swMultiImageUpdateTime": swMultiImageUpdateTime,
       "swMultiImageFrom": swMultiImageFrom,
       "swMultiImageSendUser": swMultiImageSendUser,
       "swMultiImageFileName": swMultiImageFileName,
       "agentMultiCfgMgmt": agentMultiCfgMgmt,
       "swMultiCfgInfoTable": swMultiCfgInfoTable,
       "swMultiCfgInfoEntry": swMultiCfgInfoEntry,
       "swMultiCfgInfoID": swMultiCfgInfoID,
       "swMultiCfgVersion": swMultiCfgVersion,
       "swMultiCfgSize": swMultiCfgSize,
       "swMultiCFgUpdateTime": swMultiCFgUpdateTime,
       "swMultiCfgFrom": swMultiCfgFrom,
       "swMultiCfgSendUser": swMultiCfgSendUser,
       "swMultiCfgFileName": swMultiCfgFileName,
       "swMultiCfgCurrentUsed": swMultiCfgCurrentUsed,
       "swMultiCfgBootUp": swMultiCfgBootUp,
       "swMultiCfgCtrlTable": swMultiCfgCtrlTable,
       "swMultiCfgCtrlEntry": swMultiCfgCtrlEntry,
       "swMultiCfgCtrlID": swMultiCfgCtrlID,
       "swMultiCfgAction": swMultiCfgAction,
       "systemSeverityControlMgmt": systemSeverityControlMgmt,
       "systemSeverityTrapControl": systemSeverityTrapControl,
       "systemSeverityLogControl": systemSeverityLogControl,
       "agentTrustedHostMgmt": agentTrustedHostMgmt,
       "agentTrustedHostTable": agentTrustedHostTable,
       "agentTrustedHostEntry": agentTrustedHostEntry,
       "agentTrustedHostIndex": agentTrustedHostIndex,
       "agentTrustedHostIPAddress": agentTrustedHostIPAddress,
       "agentTrustedHostRowStatus": agentTrustedHostRowStatus,
       "agentTrustedHostIPSubnetMask": agentTrustedHostIPSubnetMask,
       "agentTrustedHostForSNMP": agentTrustedHostForSNMP,
       "agentTrustedHostForTELNET": agentTrustedHostForTELNET,
       "agentTrustedHostForSSH": agentTrustedHostForSSH,
       "agentTrustedHostForHTTP": agentTrustedHostForHTTP,
       "agentTrustedHostForHTTPS": agentTrustedHostForHTTPS,
       "agentTrustedHostForPING": agentTrustedHostForPING,
       "agentTrustedHostAddrType": agentTrustedHostAddrType,
       "agentTrustedHostAddr": agentTrustedHostAddr,
       "agentTrustedHostIPv6PrefixLen": agentTrustedHostIPv6PrefixLen,
       "agentTrustedHostDelAllState": agentTrustedHostDelAllState,
       "agentFDBMgmt": agentFDBMgmt,
       "agentFDBClearAllState": agentFDBClearAllState,
       "agentFDBClearByPortTable": agentFDBClearByPortTable,
       "agentFDBClearByPortEntry": agentFDBClearByPortEntry,
       "agentFDBClearPortIndex": agentFDBClearPortIndex,
       "agentFDBClearByPortAction": agentFDBClearByPortAction,
       "agentFDBClearByVlanTable": agentFDBClearByVlanTable,
       "agentFDBClearByVlanEntry": agentFDBClearByVlanEntry,
       "agentFDBClearVid": agentFDBClearVid,
       "agentFDBClearByVlanAction": agentFDBClearByVlanAction,
       "agentFDBSecurityTable": agentFDBSecurityTable,
       "agentFDBSecurityEntry": agentFDBSecurityEntry,
       "agentFDBVid": agentFDBVid,
       "agentFDBMacAddress": agentFDBMacAddress,
       "agentFDBPort": agentFDBPort,
       "agentFDBType": agentFDBType,
       "agentFDBStatus": agentFDBStatus,
       "agentFDBSecurityModule": agentFDBSecurityModule,
       "agentARPMgmt": agentARPMgmt,
       "agentARPClearAllState": agentARPClearAllState,
       "agentGratuitousARPMgmt": agentGratuitousARPMgmt,
       "agentGratuitousARPSendIpifStatusUpState": agentGratuitousARPSendIpifStatusUpState,
       "agentGratuitousARPSendDupIpDetectedState": agentGratuitousARPSendDupIpDetectedState,
       "agentGratuitousARPLearningState": agentGratuitousARPLearningState,
       "agentGratuitousARPTable": agentGratuitousARPTable,
       "agentGratuitousARPEntry": agentGratuitousARPEntry,
       "agentGratuitousARPInterfaceName": agentGratuitousARPInterfaceName,
       "agentGratuitousARPPeriodicalSendInterval": agentGratuitousARPPeriodicalSendInterval,
       "agentGratuitousARPTrapState": agentGratuitousARPTrapState,
       "agentGratuitousARPLogState": agentGratuitousARPLogState,
       "agentARPTotalARPEntries": agentARPTotalARPEntries,
       "agentARPRetryTimes": agentARPRetryTimes,
       "swMultiImageCtrlTable": swMultiImageCtrlTable,
       "swMultiImageCtrlEntry": swMultiImageCtrlEntry,
       "swMultiImageCtrlID": swMultiImageCtrlID,
       "swMultiImageCtrlAction": swMultiImageCtrlAction,
       "agentOutOfBandDataBits": agentOutOfBandDataBits,
       "agentOutOfBandParityBits": agentOutOfBandParityBits,
       "agentOutOfBandStopBits": agentOutOfBandStopBits,
       "agentOutOfBandAutoLogoutConfig": agentOutOfBandAutoLogoutConfig,
       "agentBscFileSystemMgmt": agentBscFileSystemMgmt,
       "agentBscFileSystemTable": agentBscFileSystemTable,
       "agentBscFileSystemEntry": agentBscFileSystemEntry,
       "agentBscFileSystemIndex": agentBscFileSystemIndex,
       "agentBscFileSystemDscr": agentBscFileSystemDscr,
       "agentBscFileSystemServerAddr": agentBscFileSystemServerAddr,
       "agentBscFileSystemServerIPv6Addr": agentBscFileSystemServerIPv6Addr,
       "agentBscFileSystemServerFileName": agentBscFileSystemServerFileName,
       "agentBscFileSystemDeviceDriverID": agentBscFileSystemDeviceDriverID,
       "agentBscFileSystemDeviceFileName": agentBscFileSystemDeviceFileName,
       "agentBscFileSystemLoadType": agentBscFileSystemLoadType,
       "agentBscFileSystemCtrlUnitID": agentBscFileSystemCtrlUnitID,
       "agentBscFileSystemBootUpImage": agentBscFileSystemBootUpImage,
       "agentBscFileSystemForceAgree": agentBscFileSystemForceAgree,
       "agentBscFileSystemCtrl": agentBscFileSystemCtrl,
       "agentBscFileSystemInterfaceName": agentBscFileSystemInterfaceName,
       "agentBscFileSystemServerDomainName": agentBscFileSystemServerDomainName,
       "agentBscFileSystemIncrement": agentBscFileSystemIncrement,
       "agentBscFileSystemSaveConfigDriverID": agentBscFileSystemSaveConfigDriverID,
       "agentBscFileSystemSaveConfigFileName": agentBscFileSystemSaveConfigFileName,
       "agentBscFileSystemSaveCfg": agentBscFileSystemSaveCfg,
       "agentFileSystemConfigTable": agentFileSystemConfigTable,
       "agentFileSystemConfigEntry": agentFileSystemConfigEntry,
       "agentFileSystemUnit": agentFileSystemUnit,
       "agentFileSystemDriverID": agentFileSystemDriverID,
       "agentFileSystemBootImage": agentFileSystemBootImage,
       "agentFileSystemBootConfig": agentFileSystemBootConfig,
       "agentFileSystemActConfig": agentFileSystemActConfig,
       "agentReboot": agentReboot,
       "agentReset": agentReset,
       "agentFTPFileTable": agentFTPFileTable,
       "agentFTPFileEntry": agentFTPFileEntry,
       "agentFTPFileIndex": agentFTPFileIndex,
       "agentFTPFileDscr": agentFTPFileDscr,
       "agentFTPFileLoadType": agentFTPFileLoadType,
       "agentFTPFileAddr": agentFTPFileAddr,
       "agentFTPTCPPort": agentFTPTCPPort,
       "agentFTPFileName": agentFTPFileName,
       "agentFTPUserName": agentFTPUserName,
       "agentFTPPassword": agentFTPPassword,
       "agentFTPFileCtrlID": agentFTPFileCtrlID,
       "agentFTPFileBIncrement": agentFTPFileBIncrement,
       "agentFTPFileCtrl": agentFTPFileCtrl,
       "agentFTPFileBootUpImage": agentFTPFileBootUpImage,
       "agentFTPFileForceAgree": agentFTPFileForceAgree,
       "agentFTPFileIPv6Addr": agentFTPFileIPv6Addr,
       "agentFTPFileInterfaceName": agentFTPFileInterfaceName,
       "agentFTPFileUnitID": agentFTPFileUnitID,
       "agentSnmpTrapState": agentSnmpTrapState,
       "agentOutOfBandMgmt": agentOutOfBandMgmt,
       "agentOutOfBandMgmtState": agentOutOfBandMgmtState,
       "agentOutOfBandMgmtIpAddr": agentOutOfBandMgmtIpAddr,
       "agentOutOfBandMgmtSubnetMask": agentOutOfBandMgmtSubnetMask,
       "agentOutOfBandMgmtGateway": agentOutOfBandMgmtGateway,
       "agentOutOfBandMgmtLinkStatus": agentOutOfBandMgmtLinkStatus,
       "agentTrapMgmt": agentTrapMgmt,
       "agentTrapColdStart": agentTrapColdStart,
       "agentTrapWarmStart": agentTrapWarmStart,
       "agentTrapRmonRisingAlarm": agentTrapRmonRisingAlarm,
       "agentTrapRmonFallingAlarm": agentTrapRmonFallingAlarm,
       "agentTrapCfgSave": agentTrapCfgSave,
       "agentTrapCfgUpload": agentTrapCfgUpload,
       "agentTrapCfgDownload": agentTrapCfgDownload,
       "agentFTPFileSystemTable": agentFTPFileSystemTable,
       "agentFTPFileSystemEntry": agentFTPFileSystemEntry,
       "agentFTPFileSystemIndex": agentFTPFileSystemIndex,
       "agentFTPFileSystemDscr": agentFTPFileSystemDscr,
       "agentFTPFileSystemLoadType": agentFTPFileSystemLoadType,
       "agentFTPFileSystemAddressType": agentFTPFileSystemAddressType,
       "agentFTPFileSystemAddress": agentFTPFileSystemAddress,
       "agentFTPFileSystemTCPPort": agentFTPFileSystemTCPPort,
       "agentFTPFileSystemServerFileName": agentFTPFileSystemServerFileName,
       "agentFTPFileSystemDeviceFileName": agentFTPFileSystemDeviceFileName,
       "agentFTPFileSystemUserName": agentFTPFileSystemUserName,
       "agentFTPFileSystemPassword": agentFTPFileSystemPassword,
       "agentFTPFileSystemCtrlUnitID": agentFTPFileSystemCtrlUnitID,
       "agentFTPFileSystemBootUpImage": agentFTPFileSystemBootUpImage,
       "agentFTPFileSystemCtrl": agentFTPFileSystemCtrl,
       "agentBscCMDLogState": agentBscCMDLogState,
       "agentBscBroadcastPingReplyState": agentBscBroadcastPingReplyState,
       "agentBscTftpConfigMgmt": agentBscTftpConfigMgmt,
       "agentBscTftpCfgFirmwareFile": agentBscTftpCfgFirmwareFile,
       "agentBscTftpCfgConfigFile": agentBscTftpCfgConfigFile,
       "agentBscTftpCfgLogFile": agentBscTftpCfgLogFile,
       "agentBscTftpCfgAttackLogFile": agentBscTftpCfgAttackLogFile,
       "agentBscTftpCfgCertificateFile": agentBscTftpCfgCertificateFile,
       "agentBscTftpCfgKeyFile": agentBscTftpCfgKeyFile,
       "agentBscTftpCfgTechSuooprtFile": agentBscTftpCfgTechSuooprtFile,
       "agentBscTftpCfgDebugLogFile": agentBscTftpCfgDebugLogFile,
       "agentBscTftpCfgSIMFirmwareFile": agentBscTftpCfgSIMFirmwareFile,
       "agentBscTftpCfgSIMConfigFile": agentBscTftpCfgSIMConfigFile,
       "agentBscTftpCfgSIMLogFile": agentBscTftpCfgSIMLogFile,
       "agentBscTftpCfgServerIPAddr": agentBscTftpCfgServerIPAddr,
       "agentBscTftpCfgServerIPv6Addr": agentBscTftpCfgServerIPv6Addr,
       "agentBscTftpCfgServerDomainName": agentBscTftpCfgServerDomainName,
       "agentBscCommunityEncryptionState": agentBscCommunityEncryptionState,
       "agentIpProtoConfig": agentIpProtoConfig,
       "agentIpNumOfIf": agentIpNumOfIf,
       "agentIpTftpServerAddr": agentIpTftpServerAddr,
       "agentIpGetIpFrom": agentIpGetIpFrom,
       "agentIpAutoconfig": agentIpAutoconfig,
       "agentIpAutoconfigTimeout": agentIpAutoconfigTimeout,
       "agentIpTrapManager": agentIpTrapManager,
       "agentTrapManagerTable": agentTrapManagerTable,
       "agentTrapManagerEntry": agentTrapManagerEntry,
       "agentTrapManagerIndex": agentTrapManagerIndex,
       "agentTrapManagerIpAddr": agentTrapManagerIpAddr,
       "agentTrapManagerComm": agentTrapManagerComm,
       "agentTrapManagerMsgVer": agentTrapManagerMsgVer,
       "agentTrapManagerStatus": agentTrapManagerStatus,
       "agentNotify": agentNotify,
       "agentNotifMgmt": agentNotifMgmt,
       "notifFirmwareMgmt": notifFirmwareMgmt,
       "agentNotifFirmware": agentNotifFirmware,
       "agentNotifyPrefix": agentNotifyPrefix,
       "agentsystemRestart": agentsystemRestart,
       "agentSaveToNVRAM": agentSaveToNVRAM,
       "agentFileTransferStatusChange": agentFileTransferStatusChange,
       "agentSetToFactoryDefault": agentSetToFactoryDefault,
       "agentGratuitousARPTrap": agentGratuitousARPTrap,
       "agentLoginFailTrap": agentLoginFailTrap,
       "agentFirmwareUpgrade": agentFirmwareUpgrade,
       "agentAccessFlashFailed": agentAccessFlashFailed,
       "agentCfgOperCompleteTrap": agentCfgOperCompleteTrap,
       "notificationBindings": notificationBindings,
       "unitID": unitID,
       "trapInfosystemRestart": trapInfosystemRestart,
       "agentGratuitousARPIpAddr": agentGratuitousARPIpAddr,
       "agentGratuitousARPMacAddr": agentGratuitousARPMacAddr,
       "agentGratuitousARPPortNumber": agentGratuitousARPPortNumber,
       "agentLoginType": agentLoginType,
       "agentLoginAAAMethod": agentLoginAAAMethod,
       "agentLoginUserName": agentLoginUserName,
       "agentLoginIpAddr": agentLoginIpAddr,
       "agentLoginMacAddr": agentLoginMacAddr,
       "agentLoginAAAServerAddr": agentLoginAAAServerAddr,
       "agentLoginFailInfo": agentLoginFailInfo,
       "agentAccessFlashOper": agentAccessFlashOper,
       "agentAccessFlashAddr": agentAccessFlashAddr,
       "agentCfgOperate": agentCfgOperate}
)
