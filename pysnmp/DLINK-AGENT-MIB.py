# SNMP MIB module (DLINK-AGENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DLINK-AGENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:30:39 2024
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


# TEXTUAL-CONVENTIONS



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
    (0, "DLINK-AGENT-MIB", "agentMibCapabilityIndex"),
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
_AgentPORTutilizationTable_Object = MibTable
agentPORTutilizationTable = _AgentPORTutilizationTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 1, 7)
)
if mibBuilder.loadTexts:
    agentPORTutilizationTable.setStatus("current")
_AgentPORTutilizationEntry_Object = MibTableRow
agentPORTutilizationEntry = _AgentPORTutilizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 1, 7, 1)
)
agentPORTutilizationEntry.setIndexNames(
    (0, "DLINK-AGENT-MIB", "agentPORTutilizationProtIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 1, 7, 1, 1),
    _AgentPORTutilizationProtIndex_Type()
)
agentPORTutilizationProtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPORTutilizationProtIndex.setStatus("current")
_AgentPORTutilizationTX_Type = Integer32
_AgentPORTutilizationTX_Object = MibTableColumn
agentPORTutilizationTX = _AgentPORTutilizationTX_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 1, 7, 1, 2),
    _AgentPORTutilizationTX_Type()
)
agentPORTutilizationTX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPORTutilizationTX.setStatus("current")
_AgentPORTutilizationRX_Type = Integer32
_AgentPORTutilizationRX_Object = MibTableColumn
agentPORTutilizationRX = _AgentPORTutilizationRX_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 1, 7, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 1, 7, 1, 4),
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
    (0, "DLINK-AGENT-MIB", "agentDRAMutilizationUnitID"),
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
    (0, "DLINK-AGENT-MIB", "agentBscSwFileIndex"),
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
        ValueSizeConstraint(0, 64),
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
              5)
        )
    )
    namedValues = NamedValues(
        *(("config-as-bootup-fw", 5),
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
_AgentMultiImageCtrlID_Type = Integer32
_AgentMultiImageCtrlID_Object = MibTableColumn
agentMultiImageCtrlID = _AgentMultiImageCtrlID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 1, 1, 10),
    _AgentMultiImageCtrlID_Type()
)
agentMultiImageCtrlID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentMultiImageCtrlID.setStatus("current")


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
              3)
        )
    )
    namedValues = NamedValues(
        *(("idle", 2),
          ("other", 1),
          ("set", 3))
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
    (0, "DLINK-AGENT-MIB", "swMultiImageInfoID"),
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
        ValueSizeConstraint(0, 32),
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
_AgentTrustHostMgmt_ObjectIdentity = ObjectIdentity
agentTrustHostMgmt = _AgentTrustHostMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 10)
)
_AgentTrustHostTable_Object = MibTable
agentTrustHostTable = _AgentTrustHostTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 10, 1)
)
if mibBuilder.loadTexts:
    agentTrustHostTable.setStatus("current")
_AgentTrustHostEntry_Object = MibTableRow
agentTrustHostEntry = _AgentTrustHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 10, 1, 1)
)
agentTrustHostEntry.setIndexNames(
    (0, "DLINK-AGENT-MIB", "agentTrustHostIndex"),
)
if mibBuilder.loadTexts:
    agentTrustHostEntry.setStatus("current")


class _AgentTrustHostIndex_Type(Integer32):
    """Custom type agentTrustHostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AgentTrustHostIndex_Type.__name__ = "Integer32"
_AgentTrustHostIndex_Object = MibTableColumn
agentTrustHostIndex = _AgentTrustHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 10, 1, 1, 1),
    _AgentTrustHostIndex_Type()
)
agentTrustHostIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentTrustHostIndex.setStatus("current")
_AgentTrustHostIPAddress_Type = IpAddress
_AgentTrustHostIPAddress_Object = MibTableColumn
agentTrustHostIPAddress = _AgentTrustHostIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 10, 1, 1, 2),
    _AgentTrustHostIPAddress_Type()
)
agentTrustHostIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentTrustHostIPAddress.setStatus("current")
_AgentTrustHostRowStatus_Type = RowStatus
_AgentTrustHostRowStatus_Object = MibTableColumn
agentTrustHostRowStatus = _AgentTrustHostRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 10, 1, 1, 3),
    _AgentTrustHostRowStatus_Type()
)
agentTrustHostRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentTrustHostRowStatus.setStatus("current")
_AgentTrustHostIPSubnetMask_Type = IpAddress
_AgentTrustHostIPSubnetMask_Object = MibTableColumn
agentTrustHostIPSubnetMask = _AgentTrustHostIPSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 10, 1, 1, 4),
    _AgentTrustHostIPSubnetMask_Type()
)
agentTrustHostIPSubnetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentTrustHostIPSubnetMask.setStatus("current")


class _AgentTrustHostForSNMP_Type(Integer32):
    """Custom type agentTrustHostForSNMP based on Integer32"""
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


_AgentTrustHostForSNMP_Type.__name__ = "Integer32"
_AgentTrustHostForSNMP_Object = MibTableColumn
agentTrustHostForSNMP = _AgentTrustHostForSNMP_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 10, 1, 1, 5),
    _AgentTrustHostForSNMP_Type()
)
agentTrustHostForSNMP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentTrustHostForSNMP.setStatus("current")


class _AgentTrustHostForTELNET_Type(Integer32):
    """Custom type agentTrustHostForTELNET based on Integer32"""
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


_AgentTrustHostForTELNET_Type.__name__ = "Integer32"
_AgentTrustHostForTELNET_Object = MibTableColumn
agentTrustHostForTELNET = _AgentTrustHostForTELNET_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 10, 1, 1, 6),
    _AgentTrustHostForTELNET_Type()
)
agentTrustHostForTELNET.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentTrustHostForTELNET.setStatus("current")


class _AgentTrustHostForSSH_Type(Integer32):
    """Custom type agentTrustHostForSSH based on Integer32"""
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


_AgentTrustHostForSSH_Type.__name__ = "Integer32"
_AgentTrustHostForSSH_Object = MibTableColumn
agentTrustHostForSSH = _AgentTrustHostForSSH_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 10, 1, 1, 7),
    _AgentTrustHostForSSH_Type()
)
agentTrustHostForSSH.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentTrustHostForSSH.setStatus("current")


class _AgentTrustHostForHTTP_Type(Integer32):
    """Custom type agentTrustHostForHTTP based on Integer32"""
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


_AgentTrustHostForHTTP_Type.__name__ = "Integer32"
_AgentTrustHostForHTTP_Object = MibTableColumn
agentTrustHostForHTTP = _AgentTrustHostForHTTP_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 10, 1, 1, 8),
    _AgentTrustHostForHTTP_Type()
)
agentTrustHostForHTTP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentTrustHostForHTTP.setStatus("current")


class _AgentTrustHostForHTTPS_Type(Integer32):
    """Custom type agentTrustHostForHTTPS based on Integer32"""
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


_AgentTrustHostForHTTPS_Type.__name__ = "Integer32"
_AgentTrustHostForHTTPS_Object = MibTableColumn
agentTrustHostForHTTPS = _AgentTrustHostForHTTPS_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 10, 1, 1, 9),
    _AgentTrustHostForHTTPS_Type()
)
agentTrustHostForHTTPS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentTrustHostForHTTPS.setStatus("current")


class _AgentTrustHostDelAllState_Type(Integer32):
    """Custom type agentTrustHostDelAllState based on Integer32"""
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


_AgentTrustHostDelAllState_Type.__name__ = "Integer32"
_AgentTrustHostDelAllState_Object = MibScalar
agentTrustHostDelAllState = _AgentTrustHostDelAllState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 10, 2),
    _AgentTrustHostDelAllState_Type()
)
agentTrustHostDelAllState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentTrustHostDelAllState.setStatus("current")
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
    (0, "DLINK-AGENT-MIB", "agentGratuitousARPInterfaceName"),
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
_AgentNotify_ObjectIdentity = ObjectIdentity
agentNotify = _AgentNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 4)
)
_AgentNotifMgmt_ObjectIdentity = ObjectIdentity
agentNotifMgmt = _AgentNotifMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 4, 1)
)
_SystemTrapsSeverity_Type = AgentNotifyLevel
_SystemTrapsSeverity_Object = MibScalar
systemTrapsSeverity = _SystemTrapsSeverity_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 4, 1, 1),
    _SystemTrapsSeverity_Type()
)
systemTrapsSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemTrapsSeverity.setStatus("current")
_SystemLogsSeverity_Type = AgentNotifyLevel
_SystemLogsSeverity_Object = MibScalar
systemLogsSeverity = _SystemLogsSeverity_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 4, 1, 2),
    _SystemLogsSeverity_Type()
)
systemLogsSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemLogsSeverity.setStatus("current")
_AgentNotifFirmware_ObjectIdentity = ObjectIdentity
agentNotifFirmware = _AgentNotifFirmware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 4, 2)
)
_AgentNotifyPrefix_ObjectIdentity = ObjectIdentity
agentNotifyPrefix = _AgentNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 4, 2, 0)
)
_NotificationBidings_ObjectIdentity = ObjectIdentity
notificationBidings = _NotificationBidings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 4, 2, 1)
)
_AgentGratuitousARPIpAddr_Type = IpAddress
_AgentGratuitousARPIpAddr_Object = MibScalar
agentGratuitousARPIpAddr = _AgentGratuitousARPIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 4, 2, 1, 3),
    _AgentGratuitousARPIpAddr_Type()
)
agentGratuitousARPIpAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    agentGratuitousARPIpAddr.setStatus("current")
_AgentGratuitousARPMacAddr_Type = MacAddress
_AgentGratuitousARPMacAddr_Object = MibScalar
agentGratuitousARPMacAddr = _AgentGratuitousARPMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 4, 2, 1, 4),
    _AgentGratuitousARPMacAddr_Type()
)
agentGratuitousARPMacAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    agentGratuitousARPMacAddr.setStatus("current")
_AgentGratuitousARPPortNumber_Type = DisplayString
_AgentGratuitousARPPortNumber_Object = MibScalar
agentGratuitousARPPortNumber = _AgentGratuitousARPPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 4, 2, 1, 5),
    _AgentGratuitousARPPortNumber_Type()
)
agentGratuitousARPPortNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    agentGratuitousARPPortNumber.setStatus("current")

# Managed Objects groups


# Notification objects

agentGratuitousARPTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 4, 2, 0, 5)
)
agentGratuitousARPTrap.setObjects(
      *(("DLINK-AGENT-MIB", "agentGratuitousARPIpAddr"),
        ("DLINK-AGENT-MIB", "agentGratuitousARPMacAddr"),
        ("DLINK-AGENT-MIB", "agentGratuitousARPPortNumber"),
        ("DLINK-AGENT-MIB", "agentGratuitousARPInterfaceName"))
)
if mibBuilder.loadTexts:
    agentGratuitousARPTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINK-AGENT-MIB",
    **{"agentGeneralMgmt": agentGeneralMgmt,
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
       "agentStatusReset": agentStatusReset,
       "agentSerialNumber": agentSerialNumber,
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
       "agentMultiImageCtrlID": agentMultiImageCtrlID,
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
       "agentTrustHostMgmt": agentTrustHostMgmt,
       "agentTrustHostTable": agentTrustHostTable,
       "agentTrustHostEntry": agentTrustHostEntry,
       "agentTrustHostIndex": agentTrustHostIndex,
       "agentTrustHostIPAddress": agentTrustHostIPAddress,
       "agentTrustHostRowStatus": agentTrustHostRowStatus,
       "agentTrustHostIPSubnetMask": agentTrustHostIPSubnetMask,
       "agentTrustHostForSNMP": agentTrustHostForSNMP,
       "agentTrustHostForTELNET": agentTrustHostForTELNET,
       "agentTrustHostForSSH": agentTrustHostForSSH,
       "agentTrustHostForHTTP": agentTrustHostForHTTP,
       "agentTrustHostForHTTPS": agentTrustHostForHTTPS,
       "agentTrustHostDelAllState": agentTrustHostDelAllState,
       "agentFDBMgmt": agentFDBMgmt,
       "agentFDBClearAllState": agentFDBClearAllState,
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
       "agentReboot": agentReboot,
       "agentReset": agentReset,
       "agentSnmpTrapState": agentSnmpTrapState,
       "agentIpProtoConfig": agentIpProtoConfig,
       "agentIpNumOfIf": agentIpNumOfIf,
       "agentIpTftpServerAddr": agentIpTftpServerAddr,
       "agentIpGetIpFrom": agentIpGetIpFrom,
       "agentIpAutoconfig": agentIpAutoconfig,
       "agentNotify": agentNotify,
       "agentNotifMgmt": agentNotifMgmt,
       "systemTrapsSeverity": systemTrapsSeverity,
       "systemLogsSeverity": systemLogsSeverity,
       "agentNotifFirmware": agentNotifFirmware,
       "agentNotifyPrefix": agentNotifyPrefix,
       "agentGratuitousARPTrap": agentGratuitousARPTrap,
       "notificationBidings": notificationBidings,
       "agentGratuitousARPIpAddr": agentGratuitousARPIpAddr,
       "agentGratuitousARPMacAddr": agentGratuitousARPMacAddr,
       "agentGratuitousARPPortNumber": agentGratuitousARPPortNumber}
)
