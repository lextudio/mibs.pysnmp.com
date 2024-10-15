# SNMP MIB module (AGENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AGENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:34:54 2024
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

(dlink_common_mgmt,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


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
    (0, "AGENT-MIB", "agentMibCapabilityIndex"),
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
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("changed-not-save", 4),
          ("completed", 3),
          ("failed", 5),
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
    (0, "AGENT-MIB", "agentPORTutilizationProtIndex"),
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
    (0, "AGENT-MIB", "agentBscSwFileIndex"),
)
if mibBuilder.loadTexts:
    agentBscSwFileEntry.setStatus("current")
_AgentBscSwFileIndex_Type = Integer32
_AgentBscSwFileIndex_Object = MibTableColumn
agentBscSwFileIndex = _AgentBscSwFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 2, 1, 1, 1),
    _AgentBscSwFileIndex_Type()
)
agentBscSwFileIndex.setMaxAccess("read-write")
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
              5)
        )
    )
    namedValues = NamedValues(
        *(("create-and-go", 5),
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
    agentSystemReset.setStatus("current")


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
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("all", 5),
          ("cfg", 3),
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
    (0, "AGENT-MIB", "agentTrustHostIndex"),
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
_AgentConsoleModeManager_ObjectIdentity = ObjectIdentity
agentConsoleModeManager = _AgentConsoleModeManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 5)
)


class _AgentConsoleModeManagerDataBits_Type(Integer32):
    """Custom type agentConsoleModeManagerDataBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bits-7", 2),
          ("bits-8", 3),
          ("other", 1))
    )


_AgentConsoleModeManagerDataBits_Type.__name__ = "Integer32"
_AgentConsoleModeManagerDataBits_Object = MibScalar
agentConsoleModeManagerDataBits = _AgentConsoleModeManagerDataBits_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 5, 1),
    _AgentConsoleModeManagerDataBits_Type()
)
agentConsoleModeManagerDataBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentConsoleModeManagerDataBits.setStatus("current")


class _AgentConsoleModeManagerStopBits_Type(Integer32):
    """Custom type agentConsoleModeManagerStopBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("stopbits-1", 2),
          ("stopbits-2", 3))
    )


_AgentConsoleModeManagerStopBits_Type.__name__ = "Integer32"
_AgentConsoleModeManagerStopBits_Object = MibScalar
agentConsoleModeManagerStopBits = _AgentConsoleModeManagerStopBits_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 5, 2),
    _AgentConsoleModeManagerStopBits_Type()
)
agentConsoleModeManagerStopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentConsoleModeManagerStopBits.setStatus("current")


class _AgentConsoleModeManagerParity_Type(Integer32):
    """Custom type agentConsoleModeManagerParity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("even", 3),
          ("none", 1),
          ("odd", 2))
    )


_AgentConsoleModeManagerParity_Type.__name__ = "Integer32"
_AgentConsoleModeManagerParity_Object = MibScalar
agentConsoleModeManagerParity = _AgentConsoleModeManagerParity_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 5, 3),
    _AgentConsoleModeManagerParity_Type()
)
agentConsoleModeManagerParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentConsoleModeManagerParity.setStatus("current")


class _AgentConsoleModeManagerBaudRate_Type(Integer32):
    """Custom type agentConsoleModeManagerBaudRate based on Integer32"""
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
        *(("baudRate-115200", 7),
          ("baudRate-19200", 4),
          ("baudRate-2400", 2),
          ("baudRate-38400", 5),
          ("baudRate-57200", 6),
          ("baudRate-9600", 3),
          ("other", 1))
    )


_AgentConsoleModeManagerBaudRate_Type.__name__ = "Integer32"
_AgentConsoleModeManagerBaudRate_Object = MibScalar
agentConsoleModeManagerBaudRate = _AgentConsoleModeManagerBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 5, 4),
    _AgentConsoleModeManagerBaudRate_Type()
)
agentConsoleModeManagerBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentConsoleModeManagerBaudRate.setStatus("current")


class _AgentConsoleModeManagerLogoutTime_Type(Integer32):
    """Custom type agentConsoleModeManagerLogoutTime based on Integer32"""
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
        *(("fifteen-minutes", 5),
          ("five-minutes", 3),
          ("never", 1),
          ("ten-minutes", 4),
          ("two-minutes", 2))
    )


_AgentConsoleModeManagerLogoutTime_Type.__name__ = "Integer32"
_AgentConsoleModeManagerLogoutTime_Object = MibScalar
agentConsoleModeManagerLogoutTime = _AgentConsoleModeManagerLogoutTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 1, 5, 5),
    _AgentConsoleModeManagerLogoutTime_Type()
)
agentConsoleModeManagerLogoutTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentConsoleModeManagerLogoutTime.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AGENT-MIB",
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
       "agentPORTutilizationTable": agentPORTutilizationTable,
       "agentPORTutilizationEntry": agentPORTutilizationEntry,
       "agentPORTutilizationProtIndex": agentPORTutilizationProtIndex,
       "agentPORTutilizationTX": agentPORTutilizationTX,
       "agentPORTutilizationRX": agentPORTutilizationRX,
       "agentPORTutilizationUtil": agentPORTutilizationUtil,
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
       "agentFileTransfer": agentFileTransfer,
       "agentSystemReset": agentSystemReset,
       "agentRs232PortConfig": agentRs232PortConfig,
       "agentOutOfBandBaudRateConfig": agentOutOfBandBaudRateConfig,
       "agentSaveCfg": agentSaveCfg,
       "agentTrustHostMgmt": agentTrustHostMgmt,
       "agentTrustHostTable": agentTrustHostTable,
       "agentTrustHostEntry": agentTrustHostEntry,
       "agentTrustHostIndex": agentTrustHostIndex,
       "agentTrustHostIPAddress": agentTrustHostIPAddress,
       "agentTrustHostRowStatus": agentTrustHostRowStatus,
       "agentTrustHostIPSubnetMask": agentTrustHostIPSubnetMask,
       "agentTrustHostDelAllState": agentTrustHostDelAllState,
       "agentFDBMgmt": agentFDBMgmt,
       "agentFDBClearAllState": agentFDBClearAllState,
       "agentARPMgmt": agentARPMgmt,
       "agentARPClearAllState": agentARPClearAllState,
       "agentIpProtoConfig": agentIpProtoConfig,
       "agentIpNumOfIf": agentIpNumOfIf,
       "agentIpTftpServerAddr": agentIpTftpServerAddr,
       "agentIpGetIpFrom": agentIpGetIpFrom,
       "agentConsoleModeManager": agentConsoleModeManager,
       "agentConsoleModeManagerDataBits": agentConsoleModeManagerDataBits,
       "agentConsoleModeManagerStopBits": agentConsoleModeManagerStopBits,
       "agentConsoleModeManagerParity": agentConsoleModeManagerParity,
       "agentConsoleModeManagerBaudRate": agentConsoleModeManagerBaudRate,
       "agentConsoleModeManagerLogoutTime": agentConsoleModeManagerLogoutTime}
)
