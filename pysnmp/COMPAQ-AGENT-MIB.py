# SNMP MIB module (COMPAQ-AGENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/COMPAQ-AGENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:16:47 2024
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

(compaq_common_mgmt,) = mibBuilder.importSymbols(
    "COMPAQ-ID-REC-MIB",
    "compaq-common-mgmt")

(cpqRackAssetIndex,
 cpqRackCommonEnclosureIndex,
 cpqRackCommonEnclosureRack,
 cpqRackNetConnectorChassis,
 cpqRackNetConnectorIndex,
 cpqRackNetConnectorRack) = mibBuilder.importSymbols(
    "CPQRACK-MIB",
    "cpqRackAssetIndex",
    "cpqRackCommonEnclosureIndex",
    "cpqRackCommonEnclosureRack",
    "cpqRackNetConnectorChassis",
    "cpqRackNetConnectorIndex",
    "cpqRackNetConnectorRack")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AgentGeneralMgmt_ObjectIdentity = ObjectIdentity
agentGeneralMgmt = _AgentGeneralMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1)
)
_AgentBasicInfo_ObjectIdentity = ObjectIdentity
agentBasicInfo = _AgentBasicInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 1)
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
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 1, 1),
    _AgentMgmtProtocolCapability_Type()
)
agentMgmtProtocolCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMgmtProtocolCapability.setStatus("mandatory")
_AgentMibCapabilityTable_Object = MibTable
agentMibCapabilityTable = _AgentMibCapabilityTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 1, 2)
)
if mibBuilder.loadTexts:
    agentMibCapabilityTable.setStatus("mandatory")
_AgentMibCapabilityEntry_Object = MibTableRow
agentMibCapabilityEntry = _AgentMibCapabilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 1, 2, 1)
)
agentMibCapabilityEntry.setIndexNames(
    (0, "COMPAQ-AGENT-MIB", "agentMibCapabilityIndex"),
)
if mibBuilder.loadTexts:
    agentMibCapabilityEntry.setStatus("mandatory")
_AgentMibCapabilityIndex_Type = Integer32
_AgentMibCapabilityIndex_Object = MibTableColumn
agentMibCapabilityIndex = _AgentMibCapabilityIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 1, 2, 1, 1),
    _AgentMibCapabilityIndex_Type()
)
agentMibCapabilityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMibCapabilityIndex.setStatus("mandatory")


class _AgentMibCapabilityDescr_Type(DisplayString):
    """Custom type agentMibCapabilityDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 35),
    )


_AgentMibCapabilityDescr_Type.__name__ = "DisplayString"
_AgentMibCapabilityDescr_Object = MibTableColumn
agentMibCapabilityDescr = _AgentMibCapabilityDescr_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 1, 2, 1, 2),
    _AgentMibCapabilityDescr_Type()
)
agentMibCapabilityDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMibCapabilityDescr.setStatus("mandatory")
_AgentMibCapabilityVersion_Type = Integer32
_AgentMibCapabilityVersion_Object = MibTableColumn
agentMibCapabilityVersion = _AgentMibCapabilityVersion_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 1, 2, 1, 3),
    _AgentMibCapabilityVersion_Type()
)
agentMibCapabilityVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMibCapabilityVersion.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 1, 2, 1, 4),
    _AgentMibCapabilityType_Type()
)
agentMibCapabilityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMibCapabilityType.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 1, 3),
    _AgentStatusConsoleInUse_Type()
)
agentStatusConsoleInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStatusConsoleInUse.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 1, 4),
    _AgentStatusSaveCfg_Type()
)
agentStatusSaveCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStatusSaveCfg.setStatus("mandatory")


class _AgentSwitchMfgDate_Type(DisplayString):
    """Custom type agentSwitchMfgDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AgentSwitchMfgDate_Type.__name__ = "DisplayString"
_AgentSwitchMfgDate_Object = MibScalar
agentSwitchMfgDate = _AgentSwitchMfgDate_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 1, 5),
    _AgentSwitchMfgDate_Type()
)
agentSwitchMfgDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchMfgDate.setStatus("mandatory")


class _AgentSwitchFirmwareMfgDate_Type(DisplayString):
    """Custom type agentSwitchFirmwareMfgDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AgentSwitchFirmwareMfgDate_Type.__name__ = "DisplayString"
_AgentSwitchFirmwareMfgDate_Object = MibScalar
agentSwitchFirmwareMfgDate = _AgentSwitchFirmwareMfgDate_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 1, 6),
    _AgentSwitchFirmwareMfgDate_Type()
)
agentSwitchFirmwareMfgDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchFirmwareMfgDate.setStatus("mandatory")
_AgentBasicConfig_ObjectIdentity = ObjectIdentity
agentBasicConfig = _AgentBasicConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 2)
)
_AgentBscSwFileTable_Object = MibTable
agentBscSwFileTable = _AgentBscSwFileTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    agentBscSwFileTable.setStatus("mandatory")
_AgentBscSwFileEntry_Object = MibTableRow
agentBscSwFileEntry = _AgentBscSwFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 2, 1, 1)
)
agentBscSwFileEntry.setIndexNames(
    (0, "COMPAQ-AGENT-MIB", "agentBscSwFileIndex"),
)
if mibBuilder.loadTexts:
    agentBscSwFileEntry.setStatus("mandatory")
_AgentBscSwFileIndex_Type = Integer32
_AgentBscSwFileIndex_Object = MibTableColumn
agentBscSwFileIndex = _AgentBscSwFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 2, 1, 1, 1),
    _AgentBscSwFileIndex_Type()
)
agentBscSwFileIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentBscSwFileIndex.setStatus("mandatory")


class _AgentBscSwFileDscr_Type(DisplayString):
    """Custom type agentBscSwFileDscr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AgentBscSwFileDscr_Type.__name__ = "DisplayString"
_AgentBscSwFileDscr_Object = MibTableColumn
agentBscSwFileDscr = _AgentBscSwFileDscr_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 2, 1, 1, 2),
    _AgentBscSwFileDscr_Type()
)
agentBscSwFileDscr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentBscSwFileDscr.setStatus("mandatory")
_AgentBscSwFileAddr_Type = IpAddress
_AgentBscSwFileAddr_Object = MibTableColumn
agentBscSwFileAddr = _AgentBscSwFileAddr_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 2, 1, 1, 3),
    _AgentBscSwFileAddr_Type()
)
agentBscSwFileAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentBscSwFileAddr.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 2, 1, 1, 4),
    _AgentBscSwFileTransferType_Type()
)
agentBscSwFileTransferType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentBscSwFileTransferType.setStatus("mandatory")


class _AgentBscSwFile_Type(DisplayString):
    """Custom type agentBscSwFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AgentBscSwFile_Type.__name__ = "DisplayString"
_AgentBscSwFile_Object = MibTableColumn
agentBscSwFile = _AgentBscSwFile_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 2, 1, 1, 5),
    _AgentBscSwFile_Type()
)
agentBscSwFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentBscSwFile.setStatus("mandatory")


class _AgentBscSwFileLocateId_Type(Integer32):
    """Custom type agentBscSwFileLocateId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AgentBscSwFileLocateId_Type.__name__ = "Integer32"
_AgentBscSwFileLocateId_Object = MibTableColumn
agentBscSwFileLocateId = _AgentBscSwFileLocateId_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 2, 1, 1, 6),
    _AgentBscSwFileLocateId_Type()
)
agentBscSwFileLocateId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentBscSwFileLocateId.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 2, 1, 1, 7),
    _AgentBscSwFileLoadType_Type()
)
agentBscSwFileLoadType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentBscSwFileLoadType.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 2, 1, 1, 8),
    _AgentBscSwFileCtrl_Type()
)
agentBscSwFileCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentBscSwFileCtrl.setStatus("mandatory")
_AgentBscFileServerTftpPort_Type = Integer32
_AgentBscFileServerTftpPort_Object = MibTableColumn
agentBscFileServerTftpPort = _AgentBscFileServerTftpPort_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 2, 1, 1, 9),
    _AgentBscFileServerTftpPort_Type()
)
agentBscFileServerTftpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentBscFileServerTftpPort.setStatus("mandatory")


class _AgentBscSwFileTime_Type(DisplayString):
    """Custom type agentBscSwFileTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AgentBscSwFileTime_Type.__name__ = "DisplayString"
_AgentBscSwFileTime_Object = MibTableColumn
agentBscSwFileTime = _AgentBscSwFileTime_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 2, 1, 1, 10),
    _AgentBscSwFileTime_Type()
)
agentBscSwFileTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentBscSwFileTime.setStatus("mandatory")


class _AgentBscSwFileStatus_Type(DisplayString):
    """Custom type agentBscSwFileStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_AgentBscSwFileStatus_Type.__name__ = "DisplayString"
_AgentBscSwFileStatus_Object = MibTableColumn
agentBscSwFileStatus = _AgentBscSwFileStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 2, 1, 1, 11),
    _AgentBscSwFileStatus_Type()
)
agentBscSwFileStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentBscSwFileStatus.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 2, 2),
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
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 2, 3),
    _AgentSystemReset_Type()
)
agentSystemReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSystemReset.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 2, 4),
    _AgentRs232PortConfig_Type()
)
agentRs232PortConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRs232PortConfig.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 2, 5),
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
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 2, 6),
    _AgentSaveCfg_Type()
)
agentSaveCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSaveCfg.setStatus("mandatory")
_AgentIpProtoConfig_ObjectIdentity = ObjectIdentity
agentIpProtoConfig = _AgentIpProtoConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 3)
)
_AgentIpNumOfIf_Type = Integer32
_AgentIpNumOfIf_Object = MibScalar
agentIpNumOfIf = _AgentIpNumOfIf_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 3, 1),
    _AgentIpNumOfIf_Type()
)
agentIpNumOfIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIpNumOfIf.setStatus("mandatory")
_AgentIpTftpServerAddr_Type = IpAddress
_AgentIpTftpServerAddr_Object = MibScalar
agentIpTftpServerAddr = _AgentIpTftpServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 3, 2),
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
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 3, 3),
    _AgentIpGetIpFrom_Type()
)
agentIpGetIpFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIpGetIpFrom.setStatus("mandatory")
_AgentIpTrapManager_ObjectIdentity = ObjectIdentity
agentIpTrapManager = _AgentIpTrapManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 4)
)
_AgentIpTrapManagerTable_Object = MibTable
agentIpTrapManagerTable = _AgentIpTrapManagerTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 4, 1)
)
if mibBuilder.loadTexts:
    agentIpTrapManagerTable.setStatus("mandatory")
_AgentIpTrapManagerEntry_Object = MibTableRow
agentIpTrapManagerEntry = _AgentIpTrapManagerEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 4, 1, 1)
)
agentIpTrapManagerEntry.setIndexNames(
    (0, "COMPAQ-AGENT-MIB", "agentIpTrapManagerIpAddr"),
)
if mibBuilder.loadTexts:
    agentIpTrapManagerEntry.setStatus("mandatory")
_AgentIpTrapManagerIpAddr_Type = IpAddress
_AgentIpTrapManagerIpAddr_Object = MibTableColumn
agentIpTrapManagerIpAddr = _AgentIpTrapManagerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 4, 1, 1, 1),
    _AgentIpTrapManagerIpAddr_Type()
)
agentIpTrapManagerIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIpTrapManagerIpAddr.setStatus("mandatory")


class _AgentIpTrapManagerComm_Type(DisplayString):
    """Custom type agentIpTrapManagerComm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AgentIpTrapManagerComm_Type.__name__ = "DisplayString"
_AgentIpTrapManagerComm_Object = MibTableColumn
agentIpTrapManagerComm = _AgentIpTrapManagerComm_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 4, 1, 1, 2),
    _AgentIpTrapManagerComm_Type()
)
agentIpTrapManagerComm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIpTrapManagerComm.setStatus("mandatory")


class _AgentIpTrapManagerStatus_Type(Integer32):
    """Custom type agentIpTrapManagerStatus based on Integer32"""
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


_AgentIpTrapManagerStatus_Type.__name__ = "Integer32"
_AgentIpTrapManagerStatus_Object = MibTableColumn
agentIpTrapManagerStatus = _AgentIpTrapManagerStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 4, 1, 1, 3),
    _AgentIpTrapManagerStatus_Type()
)
agentIpTrapManagerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIpTrapManagerStatus.setStatus("mandatory")
_AgentConsoleModeManager_ObjectIdentity = ObjectIdentity
agentConsoleModeManager = _AgentConsoleModeManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 5)
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
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 5, 1),
    _AgentConsoleModeManagerDataBits_Type()
)
agentConsoleModeManagerDataBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentConsoleModeManagerDataBits.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 5, 2),
    _AgentConsoleModeManagerStopBits_Type()
)
agentConsoleModeManagerStopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentConsoleModeManagerStopBits.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 5, 3),
    _AgentConsoleModeManagerParity_Type()
)
agentConsoleModeManagerParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentConsoleModeManagerParity.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 5, 4),
    _AgentConsoleModeManagerBaudRate_Type()
)
agentConsoleModeManagerBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentConsoleModeManagerBaudRate.setStatus("mandatory")
_AgentSlipModeManager_ObjectIdentity = ObjectIdentity
agentSlipModeManager = _AgentSlipModeManager_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 6)
)
_AgentSlipModeManagerLocalIP_Type = IpAddress
_AgentSlipModeManagerLocalIP_Object = MibScalar
agentSlipModeManagerLocalIP = _AgentSlipModeManagerLocalIP_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 6, 1),
    _AgentSlipModeManagerLocalIP_Type()
)
agentSlipModeManagerLocalIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSlipModeManagerLocalIP.setStatus("mandatory")
_AgentSlipModeManagerRemoteIP_Type = IpAddress
_AgentSlipModeManagerRemoteIP_Object = MibScalar
agentSlipModeManagerRemoteIP = _AgentSlipModeManagerRemoteIP_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 6, 2),
    _AgentSlipModeManagerRemoteIP_Type()
)
agentSlipModeManagerRemoteIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSlipModeManagerRemoteIP.setStatus("mandatory")


class _AgentSlipModeManagerMTU_Type(Integer32):
    """Custom type agentSlipModeManagerMTU based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mtu-1006", 2),
          ("mtu-1500", 3),
          ("other", 1))
    )


_AgentSlipModeManagerMTU_Type.__name__ = "Integer32"
_AgentSlipModeManagerMTU_Object = MibScalar
agentSlipModeManagerMTU = _AgentSlipModeManagerMTU_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 6, 3),
    _AgentSlipModeManagerMTU_Type()
)
agentSlipModeManagerMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSlipModeManagerMTU.setStatus("mandatory")


class _AgentSlipModeManagerBaudRate_Type(Integer32):
    """Custom type agentSlipModeManagerBaudRate based on Integer32"""
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


_AgentSlipModeManagerBaudRate_Type.__name__ = "Integer32"
_AgentSlipModeManagerBaudRate_Object = MibScalar
agentSlipModeManagerBaudRate = _AgentSlipModeManagerBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 6, 4),
    _AgentSlipModeManagerBaudRate_Type()
)
agentSlipModeManagerBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSlipModeManagerBaudRate.setStatus("mandatory")
_AgentSNTP_ObjectIdentity = ObjectIdentity
agentSNTP = _AgentSNTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 7)
)


class _AgentSNTPState_Type(Integer32):
    """Custom type agentSNTPState based on Integer32"""
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


_AgentSNTPState_Type.__name__ = "Integer32"
_AgentSNTPState_Object = MibScalar
agentSNTPState = _AgentSNTPState_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 7, 1),
    _AgentSNTPState_Type()
)
agentSNTPState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSNTPState.setStatus("mandatory")


class _AgentSNTPTimeSource_Type(Integer32):
    """Custom type agentSNTPTimeSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("server1", 1),
          ("server2", 2),
          ("system", 0))
    )


_AgentSNTPTimeSource_Type.__name__ = "Integer32"
_AgentSNTPTimeSource_Object = MibScalar
agentSNTPTimeSource = _AgentSNTPTimeSource_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 7, 2),
    _AgentSNTPTimeSource_Type()
)
agentSNTPTimeSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSNTPTimeSource.setStatus("mandatory")
_AgentSNTPServer1IPAddr_Type = IpAddress
_AgentSNTPServer1IPAddr_Object = MibScalar
agentSNTPServer1IPAddr = _AgentSNTPServer1IPAddr_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 7, 3),
    _AgentSNTPServer1IPAddr_Type()
)
agentSNTPServer1IPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSNTPServer1IPAddr.setStatus("mandatory")
_AgentSNTPServer2IPAddr_Type = IpAddress
_AgentSNTPServer2IPAddr_Object = MibScalar
agentSNTPServer2IPAddr = _AgentSNTPServer2IPAddr_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 7, 4),
    _AgentSNTPServer2IPAddr_Type()
)
agentSNTPServer2IPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSNTPServer2IPAddr.setStatus("mandatory")


class _AgentSNTPTimeZone_Type(Integer32):
    """Custom type agentSNTPTimeZone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-779, 839),
    )


_AgentSNTPTimeZone_Type.__name__ = "Integer32"
_AgentSNTPTimeZone_Object = MibScalar
agentSNTPTimeZone = _AgentSNTPTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 7, 5),
    _AgentSNTPTimeZone_Type()
)
agentSNTPTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSNTPTimeZone.setStatus("mandatory")


class _AgentSNTPPollInterval_Type(Integer32):
    """Custom type agentSNTPPollInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 99999),
    )


_AgentSNTPPollInterval_Type.__name__ = "Integer32"
_AgentSNTPPollInterval_Object = MibScalar
agentSNTPPollInterval = _AgentSNTPPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 7, 6),
    _AgentSNTPPollInterval_Type()
)
agentSNTPPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSNTPPollInterval.setStatus("mandatory")


class _AgentSNTPCurrentTime_Type(DisplayString):
    """Custom type agentSNTPCurrentTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AgentSNTPCurrentTime_Type.__name__ = "DisplayString"
_AgentSNTPCurrentTime_Object = MibScalar
agentSNTPCurrentTime = _AgentSNTPCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 7, 7),
    _AgentSNTPCurrentTime_Type()
)
agentSNTPCurrentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSNTPCurrentTime.setStatus("mandatory")
_AgentSNTPUpTime_Type = Integer32
_AgentSNTPUpTime_Object = MibScalar
agentSNTPUpTime = _AgentSNTPUpTime_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 7, 8),
    _AgentSNTPUpTime_Type()
)
agentSNTPUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSNTPUpTime.setStatus("mandatory")


class _AgentSNTPBootTime_Type(DisplayString):
    """Custom type agentSNTPBootTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AgentSNTPBootTime_Type.__name__ = "DisplayString"
_AgentSNTPBootTime_Object = MibScalar
agentSNTPBootTime = _AgentSNTPBootTime_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 7, 9),
    _AgentSNTPBootTime_Type()
)
agentSNTPBootTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSNTPBootTime.setStatus("mandatory")
_AgentDST_ObjectIdentity = ObjectIdentity
agentDST = _AgentDST_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 8)
)


class _AgentDSTStatus_Type(Integer32):
    """Custom type agentDSTStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("annual", 3),
          ("disable", 1),
          ("repeating", 2))
    )


_AgentDSTStatus_Type.__name__ = "Integer32"
_AgentDSTStatus_Object = MibScalar
agentDSTStatus = _AgentDSTStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 8, 1),
    _AgentDSTStatus_Type()
)
agentDSTStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDSTStatus.setStatus("mandatory")


class _AgentDSTOffset_Type(Integer32):
    """Custom type agentDSTOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_AgentDSTOffset_Type.__name__ = "Integer32"
_AgentDSTOffset_Object = MibScalar
agentDSTOffset = _AgentDSTOffset_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 8, 2),
    _AgentDSTOffset_Type()
)
agentDSTOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDSTOffset.setStatus("mandatory")


class _AgentDSTRepeatingStartMonth_Type(Integer32):
    """Custom type agentDSTRepeatingStartMonth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_AgentDSTRepeatingStartMonth_Type.__name__ = "Integer32"
_AgentDSTRepeatingStartMonth_Object = MibScalar
agentDSTRepeatingStartMonth = _AgentDSTRepeatingStartMonth_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 8, 3),
    _AgentDSTRepeatingStartMonth_Type()
)
agentDSTRepeatingStartMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDSTRepeatingStartMonth.setStatus("mandatory")


class _AgentDSTRepeatingStartWhichDay_Type(Integer32):
    """Custom type agentDSTRepeatingStartWhichDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_AgentDSTRepeatingStartWhichDay_Type.__name__ = "Integer32"
_AgentDSTRepeatingStartWhichDay_Object = MibScalar
agentDSTRepeatingStartWhichDay = _AgentDSTRepeatingStartWhichDay_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 8, 4),
    _AgentDSTRepeatingStartWhichDay_Type()
)
agentDSTRepeatingStartWhichDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDSTRepeatingStartWhichDay.setStatus("mandatory")


class _AgentDSTRepeatingStartDayOfWeek_Type(Integer32):
    """Custom type agentDSTRepeatingStartDayOfWeek based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AgentDSTRepeatingStartDayOfWeek_Type.__name__ = "Integer32"
_AgentDSTRepeatingStartDayOfWeek_Object = MibScalar
agentDSTRepeatingStartDayOfWeek = _AgentDSTRepeatingStartDayOfWeek_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 8, 5),
    _AgentDSTRepeatingStartDayOfWeek_Type()
)
agentDSTRepeatingStartDayOfWeek.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDSTRepeatingStartDayOfWeek.setStatus("mandatory")


class _AgentDSTRepeatingStartHour_Type(Integer32):
    """Custom type agentDSTRepeatingStartHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_AgentDSTRepeatingStartHour_Type.__name__ = "Integer32"
_AgentDSTRepeatingStartHour_Object = MibScalar
agentDSTRepeatingStartHour = _AgentDSTRepeatingStartHour_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 8, 6),
    _AgentDSTRepeatingStartHour_Type()
)
agentDSTRepeatingStartHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDSTRepeatingStartHour.setStatus("mandatory")


class _AgentDSTRepeatingStartMinute_Type(Integer32):
    """Custom type agentDSTRepeatingStartMinute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_AgentDSTRepeatingStartMinute_Type.__name__ = "Integer32"
_AgentDSTRepeatingStartMinute_Object = MibScalar
agentDSTRepeatingStartMinute = _AgentDSTRepeatingStartMinute_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 8, 7),
    _AgentDSTRepeatingStartMinute_Type()
)
agentDSTRepeatingStartMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDSTRepeatingStartMinute.setStatus("mandatory")


class _AgentDSTRepeatingEndMonth_Type(Integer32):
    """Custom type agentDSTRepeatingEndMonth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_AgentDSTRepeatingEndMonth_Type.__name__ = "Integer32"
_AgentDSTRepeatingEndMonth_Object = MibScalar
agentDSTRepeatingEndMonth = _AgentDSTRepeatingEndMonth_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 8, 8),
    _AgentDSTRepeatingEndMonth_Type()
)
agentDSTRepeatingEndMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDSTRepeatingEndMonth.setStatus("mandatory")


class _AgentDSTRepeatingEndWhichDay_Type(Integer32):
    """Custom type agentDSTRepeatingEndWhichDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_AgentDSTRepeatingEndWhichDay_Type.__name__ = "Integer32"
_AgentDSTRepeatingEndWhichDay_Object = MibScalar
agentDSTRepeatingEndWhichDay = _AgentDSTRepeatingEndWhichDay_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 8, 9),
    _AgentDSTRepeatingEndWhichDay_Type()
)
agentDSTRepeatingEndWhichDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDSTRepeatingEndWhichDay.setStatus("mandatory")


class _AgentDSTRepeatingEndDayOfWeek_Type(Integer32):
    """Custom type agentDSTRepeatingEndDayOfWeek based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AgentDSTRepeatingEndDayOfWeek_Type.__name__ = "Integer32"
_AgentDSTRepeatingEndDayOfWeek_Object = MibScalar
agentDSTRepeatingEndDayOfWeek = _AgentDSTRepeatingEndDayOfWeek_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 8, 10),
    _AgentDSTRepeatingEndDayOfWeek_Type()
)
agentDSTRepeatingEndDayOfWeek.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDSTRepeatingEndDayOfWeek.setStatus("mandatory")


class _AgentDSTRepeatingEndHour_Type(Integer32):
    """Custom type agentDSTRepeatingEndHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_AgentDSTRepeatingEndHour_Type.__name__ = "Integer32"
_AgentDSTRepeatingEndHour_Object = MibScalar
agentDSTRepeatingEndHour = _AgentDSTRepeatingEndHour_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 8, 11),
    _AgentDSTRepeatingEndHour_Type()
)
agentDSTRepeatingEndHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDSTRepeatingEndHour.setStatus("mandatory")


class _AgentDSTRepeatingEndMinute_Type(Integer32):
    """Custom type agentDSTRepeatingEndMinute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_AgentDSTRepeatingEndMinute_Type.__name__ = "Integer32"
_AgentDSTRepeatingEndMinute_Object = MibScalar
agentDSTRepeatingEndMinute = _AgentDSTRepeatingEndMinute_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 8, 12),
    _AgentDSTRepeatingEndMinute_Type()
)
agentDSTRepeatingEndMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDSTRepeatingEndMinute.setStatus("mandatory")


class _AgentDSTAnnualStartMonth_Type(Integer32):
    """Custom type agentDSTAnnualStartMonth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_AgentDSTAnnualStartMonth_Type.__name__ = "Integer32"
_AgentDSTAnnualStartMonth_Object = MibScalar
agentDSTAnnualStartMonth = _AgentDSTAnnualStartMonth_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 8, 13),
    _AgentDSTAnnualStartMonth_Type()
)
agentDSTAnnualStartMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDSTAnnualStartMonth.setStatus("mandatory")


class _AgentDSTAnnualStartDayOfMonth_Type(Integer32):
    """Custom type agentDSTAnnualStartDayOfMonth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_AgentDSTAnnualStartDayOfMonth_Type.__name__ = "Integer32"
_AgentDSTAnnualStartDayOfMonth_Object = MibScalar
agentDSTAnnualStartDayOfMonth = _AgentDSTAnnualStartDayOfMonth_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 8, 14),
    _AgentDSTAnnualStartDayOfMonth_Type()
)
agentDSTAnnualStartDayOfMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDSTAnnualStartDayOfMonth.setStatus("mandatory")


class _AgentDSTAnnualStartHour_Type(Integer32):
    """Custom type agentDSTAnnualStartHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_AgentDSTAnnualStartHour_Type.__name__ = "Integer32"
_AgentDSTAnnualStartHour_Object = MibScalar
agentDSTAnnualStartHour = _AgentDSTAnnualStartHour_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 8, 15),
    _AgentDSTAnnualStartHour_Type()
)
agentDSTAnnualStartHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDSTAnnualStartHour.setStatus("mandatory")


class _AgentDSTAnnualStartMinute_Type(Integer32):
    """Custom type agentDSTAnnualStartMinute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_AgentDSTAnnualStartMinute_Type.__name__ = "Integer32"
_AgentDSTAnnualStartMinute_Object = MibScalar
agentDSTAnnualStartMinute = _AgentDSTAnnualStartMinute_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 8, 16),
    _AgentDSTAnnualStartMinute_Type()
)
agentDSTAnnualStartMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDSTAnnualStartMinute.setStatus("mandatory")


class _AgentDSTAnnualEndMonth_Type(Integer32):
    """Custom type agentDSTAnnualEndMonth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_AgentDSTAnnualEndMonth_Type.__name__ = "Integer32"
_AgentDSTAnnualEndMonth_Object = MibScalar
agentDSTAnnualEndMonth = _AgentDSTAnnualEndMonth_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 8, 17),
    _AgentDSTAnnualEndMonth_Type()
)
agentDSTAnnualEndMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDSTAnnualEndMonth.setStatus("mandatory")


class _AgentDSTAnnualEndDayOfMonth_Type(Integer32):
    """Custom type agentDSTAnnualEndDayOfMonth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_AgentDSTAnnualEndDayOfMonth_Type.__name__ = "Integer32"
_AgentDSTAnnualEndDayOfMonth_Object = MibScalar
agentDSTAnnualEndDayOfMonth = _AgentDSTAnnualEndDayOfMonth_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 8, 18),
    _AgentDSTAnnualEndDayOfMonth_Type()
)
agentDSTAnnualEndDayOfMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDSTAnnualEndDayOfMonth.setStatus("mandatory")


class _AgentDSTAnnualEndHour_Type(Integer32):
    """Custom type agentDSTAnnualEndHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_AgentDSTAnnualEndHour_Type.__name__ = "Integer32"
_AgentDSTAnnualEndHour_Object = MibScalar
agentDSTAnnualEndHour = _AgentDSTAnnualEndHour_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 8, 19),
    _AgentDSTAnnualEndHour_Type()
)
agentDSTAnnualEndHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDSTAnnualEndHour.setStatus("mandatory")


class _AgentDSTAnnualEndMinute_Type(Integer32):
    """Custom type agentDSTAnnualEndMinute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_AgentDSTAnnualEndMinute_Type.__name__ = "Integer32"
_AgentDSTAnnualEndMinute_Object = MibScalar
agentDSTAnnualEndMinute = _AgentDSTAnnualEndMinute_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 1, 8, 20),
    _AgentDSTAnnualEndMinute_Type()
)
agentDSTAnnualEndMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDSTAnnualEndMinute.setStatus("mandatory")
_AgentSwitchCommonMgmt_ObjectIdentity = ObjectIdentity
agentSwitchCommonMgmt = _AgentSwitchCommonMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 3)
)
_AgentSwitchCube_ObjectIdentity = ObjectIdentity
agentSwitchCube = _AgentSwitchCube_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 3, 1)
)
_AgentSwitchCubeTable_Object = MibTable
agentSwitchCubeTable = _AgentSwitchCubeTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 3, 1, 1)
)
if mibBuilder.loadTexts:
    agentSwitchCubeTable.setStatus("mandatory")
_AgentSwitchCubeEntry_Object = MibTableRow
agentSwitchCubeEntry = _AgentSwitchCubeEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 3, 1, 1, 1)
)
agentSwitchCubeEntry.setIndexNames(
    (0, "CPQRACK-MIB", "cpqRackAssetIndex"),
    (0, "CPQRACK-MIB", "cpqRackCommonEnclosureRack"),
    (0, "CPQRACK-MIB", "cpqRackCommonEnclosureIndex"),
    (0, "CPQRACK-MIB", "cpqRackNetConnectorRack"),
    (0, "CPQRACK-MIB", "cpqRackNetConnectorChassis"),
    (0, "CPQRACK-MIB", "cpqRackNetConnectorIndex"),
    (0, "COMPAQ-AGENT-MIB", "agentSwitchCubeType"),
)
if mibBuilder.loadTexts:
    agentSwitchCubeEntry.setStatus("mandatory")


class _AgentSwitchCubeType_Type(Integer32):
    """Custom type agentSwitchCubeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dualTSX", 2),
          ("other", 1),
          ("quadT", 3))
    )


_AgentSwitchCubeType_Type.__name__ = "Integer32"
_AgentSwitchCubeType_Object = MibTableColumn
agentSwitchCubeType = _AgentSwitchCubeType_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 3, 1, 1, 1, 1),
    _AgentSwitchCubeType_Type()
)
agentSwitchCubeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchCubeType.setStatus("mandatory")


class _AgentSwitchCubeSpareName_Type(DisplayString):
    """Custom type agentSwitchCubeSpareName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AgentSwitchCubeSpareName_Type.__name__ = "DisplayString"
_AgentSwitchCubeSpareName_Object = MibTableColumn
agentSwitchCubeSpareName = _AgentSwitchCubeSpareName_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 3, 1, 1, 1, 2),
    _AgentSwitchCubeSpareName_Type()
)
agentSwitchCubeSpareName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchCubeSpareName.setStatus("mandatory")


class _AgentSwitchCubeSparePartNumber_Type(DisplayString):
    """Custom type agentSwitchCubeSparePartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AgentSwitchCubeSparePartNumber_Type.__name__ = "DisplayString"
_AgentSwitchCubeSparePartNumber_Object = MibTableColumn
agentSwitchCubeSparePartNumber = _AgentSwitchCubeSparePartNumber_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 3, 1, 1, 1, 3),
    _AgentSwitchCubeSparePartNumber_Type()
)
agentSwitchCubeSparePartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchCubeSparePartNumber.setStatus("mandatory")
_AgentSwitchPowerSupply_ObjectIdentity = ObjectIdentity
agentSwitchPowerSupply = _AgentSwitchPowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 3, 2)
)
_AgentSwitchPowerSupplyTable_Object = MibTable
agentSwitchPowerSupplyTable = _AgentSwitchPowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 3, 2, 1)
)
if mibBuilder.loadTexts:
    agentSwitchPowerSupplyTable.setStatus("mandatory")
_AgentSwitchPowerSupplyEntry_Object = MibTableRow
agentSwitchPowerSupplyEntry = _AgentSwitchPowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 3, 2, 1, 1)
)
agentSwitchPowerSupplyEntry.setIndexNames(
    (0, "CPQRACK-MIB", "cpqRackAssetIndex"),
    (0, "CPQRACK-MIB", "cpqRackCommonEnclosureRack"),
    (0, "CPQRACK-MIB", "cpqRackCommonEnclosureIndex"),
    (0, "CPQRACK-MIB", "cpqRackNetConnectorRack"),
    (0, "CPQRACK-MIB", "cpqRackNetConnectorChassis"),
    (0, "CPQRACK-MIB", "cpqRackNetConnectorIndex"),
    (0, "COMPAQ-AGENT-MIB", "agentSwitchPowerSupplyIndex"),
)
if mibBuilder.loadTexts:
    agentSwitchPowerSupplyEntry.setStatus("mandatory")
_AgentSwitchPowerSupplyIndex_Type = Integer32
_AgentSwitchPowerSupplyIndex_Object = MibTableColumn
agentSwitchPowerSupplyIndex = _AgentSwitchPowerSupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 3, 2, 1, 1, 1),
    _AgentSwitchPowerSupplyIndex_Type()
)
agentSwitchPowerSupplyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchPowerSupplyIndex.setStatus("mandatory")
_AgentSwitchPowerSupplyMaxPwrOutput_Type = Integer32
_AgentSwitchPowerSupplyMaxPwrOutput_Object = MibTableColumn
agentSwitchPowerSupplyMaxPwrOutput = _AgentSwitchPowerSupplyMaxPwrOutput_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 3, 2, 1, 1, 2),
    _AgentSwitchPowerSupplyMaxPwrOutput_Type()
)
agentSwitchPowerSupplyMaxPwrOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchPowerSupplyMaxPwrOutput.setStatus("mandatory")
_AgentSwitchPowerSupplyCurPwrOutput_Type = Integer32
_AgentSwitchPowerSupplyCurPwrOutput_Object = MibTableColumn
agentSwitchPowerSupplyCurPwrOutput = _AgentSwitchPowerSupplyCurPwrOutput_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 3, 2, 1, 1, 3),
    _AgentSwitchPowerSupplyCurPwrOutput_Type()
)
agentSwitchPowerSupplyCurPwrOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchPowerSupplyCurPwrOutput.setStatus("mandatory")
_AgentSwitchPowerSupplyIntakeTemp_Type = Integer32
_AgentSwitchPowerSupplyIntakeTemp_Object = MibTableColumn
agentSwitchPowerSupplyIntakeTemp = _AgentSwitchPowerSupplyIntakeTemp_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 3, 2, 1, 1, 4),
    _AgentSwitchPowerSupplyIntakeTemp_Type()
)
agentSwitchPowerSupplyIntakeTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchPowerSupplyIntakeTemp.setStatus("mandatory")
_AgentSwitchPowerSupplyExhaustTemp_Type = Integer32
_AgentSwitchPowerSupplyExhaustTemp_Object = MibTableColumn
agentSwitchPowerSupplyExhaustTemp = _AgentSwitchPowerSupplyExhaustTemp_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 3, 2, 1, 1, 5),
    _AgentSwitchPowerSupplyExhaustTemp_Type()
)
agentSwitchPowerSupplyExhaustTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchPowerSupplyExhaustTemp.setStatus("mandatory")


class _AgentSwitchPowerSupplyStatus_Type(Integer32):
    """Custom type agentSwitchPowerSupplyStatus based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("bistFailure", 3),
          ("brownOut", 13),
          ("calibrationTableInvalid", 16),
          ("dacFailed", 9),
          ("epromFailed", 7),
          ("fanFailure", 4),
          ("generalFailure", 2),
          ("giveupOnStartup", 14),
          ("interlockOpen", 6),
          ("noError", 1),
          ("nvramInvalid", 15),
          ("orringdiodeFailed", 12),
          ("ramTestFailed", 10),
          ("tempFailure", 5),
          ("voltageChannelFailed", 11),
          ("vrefFailed", 8))
    )


_AgentSwitchPowerSupplyStatus_Type.__name__ = "Integer32"
_AgentSwitchPowerSupplyStatus_Object = MibTableColumn
agentSwitchPowerSupplyStatus = _AgentSwitchPowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 3, 2, 1, 1, 6),
    _AgentSwitchPowerSupplyStatus_Type()
)
agentSwitchPowerSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchPowerSupplyStatus.setStatus("mandatory")


class _AgentSwitchPowerSupplyInputLineStatus_Type(Integer32):
    """Custom type agentSwitchPowerSupplyInputLineStatus based on Integer32"""
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
        *(("brownOut", 5),
          ("lineHit", 4),
          ("lineOverVoltage", 2),
          ("linePowerLoss", 6),
          ("lineUnderVoltage", 3),
          ("noError", 1))
    )


_AgentSwitchPowerSupplyInputLineStatus_Type.__name__ = "Integer32"
_AgentSwitchPowerSupplyInputLineStatus_Object = MibTableColumn
agentSwitchPowerSupplyInputLineStatus = _AgentSwitchPowerSupplyInputLineStatus_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 3, 2, 1, 1, 7),
    _AgentSwitchPowerSupplyInputLineStatus_Type()
)
agentSwitchPowerSupplyInputLineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchPowerSupplyInputLineStatus.setStatus("mandatory")


class _AgentSwitchPowerSupplyCondition_Type(Integer32):
    """Custom type agentSwitchPowerSupplyCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_AgentSwitchPowerSupplyCondition_Type.__name__ = "Integer32"
_AgentSwitchPowerSupplyCondition_Object = MibTableColumn
agentSwitchPowerSupplyCondition = _AgentSwitchPowerSupplyCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 3, 2, 1, 1, 8),
    _AgentSwitchPowerSupplyCondition_Type()
)
agentSwitchPowerSupplyCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchPowerSupplyCondition.setStatus("mandatory")
_AgentSwitchFan_ObjectIdentity = ObjectIdentity
agentSwitchFan = _AgentSwitchFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 3, 3)
)
_AgentSwitchFanTable_Object = MibTable
agentSwitchFanTable = _AgentSwitchFanTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 3, 3, 1)
)
if mibBuilder.loadTexts:
    agentSwitchFanTable.setStatus("mandatory")
_AgentSwitchFanEntry_Object = MibTableRow
agentSwitchFanEntry = _AgentSwitchFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 3, 3, 1, 1)
)
agentSwitchFanEntry.setIndexNames(
    (0, "CPQRACK-MIB", "cpqRackAssetIndex"),
    (0, "CPQRACK-MIB", "cpqRackCommonEnclosureRack"),
    (0, "CPQRACK-MIB", "cpqRackCommonEnclosureIndex"),
    (0, "CPQRACK-MIB", "cpqRackNetConnectorRack"),
    (0, "CPQRACK-MIB", "cpqRackNetConnectorChassis"),
    (0, "CPQRACK-MIB", "cpqRackNetConnectorIndex"),
    (0, "COMPAQ-AGENT-MIB", "agentSwitchFanIndex"),
)
if mibBuilder.loadTexts:
    agentSwitchFanEntry.setStatus("mandatory")
_AgentSwitchFanIndex_Type = Integer32
_AgentSwitchFanIndex_Object = MibTableColumn
agentSwitchFanIndex = _AgentSwitchFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 3, 3, 1, 1, 1),
    _AgentSwitchFanIndex_Type()
)
agentSwitchFanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchFanIndex.setStatus("mandatory")


class _AgentSwitchFanCondition_Type(Integer32):
    """Custom type agentSwitchFanCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_AgentSwitchFanCondition_Type.__name__ = "Integer32"
_AgentSwitchFanCondition_Object = MibTableColumn
agentSwitchFanCondition = _AgentSwitchFanCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 3, 3, 1, 1, 2),
    _AgentSwitchFanCondition_Type()
)
agentSwitchFanCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchFanCondition.setStatus("mandatory")
_AgentSwitchTempSensor_ObjectIdentity = ObjectIdentity
agentSwitchTempSensor = _AgentSwitchTempSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 3, 4)
)
_AgentSwitchTempSensorTable_Object = MibTable
agentSwitchTempSensorTable = _AgentSwitchTempSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 3, 4, 1)
)
if mibBuilder.loadTexts:
    agentSwitchTempSensorTable.setStatus("mandatory")
_AgentSwitchTempSensorEntry_Object = MibTableRow
agentSwitchTempSensorEntry = _AgentSwitchTempSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 3, 4, 1, 1)
)
agentSwitchTempSensorEntry.setIndexNames(
    (0, "CPQRACK-MIB", "cpqRackAssetIndex"),
    (0, "CPQRACK-MIB", "cpqRackCommonEnclosureRack"),
    (0, "CPQRACK-MIB", "cpqRackCommonEnclosureIndex"),
    (0, "CPQRACK-MIB", "cpqRackNetConnectorRack"),
    (0, "CPQRACK-MIB", "cpqRackNetConnectorChassis"),
    (0, "CPQRACK-MIB", "cpqRackNetConnectorIndex"),
    (0, "COMPAQ-AGENT-MIB", "agentSwitchTempSensorIndex"),
)
if mibBuilder.loadTexts:
    agentSwitchTempSensorEntry.setStatus("mandatory")
_AgentSwitchTempSensorIndex_Type = Integer32
_AgentSwitchTempSensorIndex_Object = MibTableColumn
agentSwitchTempSensorIndex = _AgentSwitchTempSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 3, 4, 1, 1, 1),
    _AgentSwitchTempSensorIndex_Type()
)
agentSwitchTempSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchTempSensorIndex.setStatus("mandatory")
_AgentSwitchTempSensorCurrent_Type = Integer32
_AgentSwitchTempSensorCurrent_Object = MibTableColumn
agentSwitchTempSensorCurrent = _AgentSwitchTempSensorCurrent_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 3, 4, 1, 1, 2),
    _AgentSwitchTempSensorCurrent_Type()
)
agentSwitchTempSensorCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchTempSensorCurrent.setStatus("mandatory")
_AgentSwitchTempSensorThreshold_Type = Integer32
_AgentSwitchTempSensorThreshold_Object = MibTableColumn
agentSwitchTempSensorThreshold = _AgentSwitchTempSensorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 3, 4, 1, 1, 3),
    _AgentSwitchTempSensorThreshold_Type()
)
agentSwitchTempSensorThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchTempSensorThreshold.setStatus("mandatory")


class _AgentSwitchTempSensorCondition_Type(Integer32):
    """Custom type agentSwitchTempSensorCondition based on Integer32"""
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
        *(("degraded", 3),
          ("failed", 4),
          ("ok", 2),
          ("other", 1))
    )


_AgentSwitchTempSensorCondition_Type.__name__ = "Integer32"
_AgentSwitchTempSensorCondition_Object = MibTableColumn
agentSwitchTempSensorCondition = _AgentSwitchTempSensorCondition_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 3, 4, 1, 1, 4),
    _AgentSwitchTempSensorCondition_Type()
)
agentSwitchTempSensorCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchTempSensorCondition.setStatus("mandatory")


class _AgentSwitchTempSensorTempType_Type(Integer32):
    """Custom type agentSwitchTempSensorTempType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              5,
              9,
              15)
        )
    )
    namedValues = NamedValues(
        *(("blowout", 5),
          ("caution", 9),
          ("critical", 15),
          ("other", 1))
    )


_AgentSwitchTempSensorTempType_Type.__name__ = "Integer32"
_AgentSwitchTempSensorTempType_Object = MibTableColumn
agentSwitchTempSensorTempType = _AgentSwitchTempSensorTempType_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 3, 4, 1, 1, 5),
    _AgentSwitchTempSensorTempType_Type()
)
agentSwitchTempSensorTempType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSwitchTempSensorTempType.setStatus("mandatory")
_EndOfMIB_Type = Integer32
_EndOfMIB_Object = MibScalar
endOfMIB = _EndOfMIB_Object(
    (1, 3, 6, 1, 4, 1, 232, 161, 3, 3, 9999),
    _EndOfMIB_Type()
)
endOfMIB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfMIB.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "COMPAQ-AGENT-MIB",
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
       "agentSwitchMfgDate": agentSwitchMfgDate,
       "agentSwitchFirmwareMfgDate": agentSwitchFirmwareMfgDate,
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
       "agentBscFileServerTftpPort": agentBscFileServerTftpPort,
       "agentBscSwFileTime": agentBscSwFileTime,
       "agentBscSwFileStatus": agentBscSwFileStatus,
       "agentFileTransfer": agentFileTransfer,
       "agentSystemReset": agentSystemReset,
       "agentRs232PortConfig": agentRs232PortConfig,
       "agentOutOfBandBaudRateConfig": agentOutOfBandBaudRateConfig,
       "agentSaveCfg": agentSaveCfg,
       "agentIpProtoConfig": agentIpProtoConfig,
       "agentIpNumOfIf": agentIpNumOfIf,
       "agentIpTftpServerAddr": agentIpTftpServerAddr,
       "agentIpGetIpFrom": agentIpGetIpFrom,
       "agentIpTrapManager": agentIpTrapManager,
       "agentIpTrapManagerTable": agentIpTrapManagerTable,
       "agentIpTrapManagerEntry": agentIpTrapManagerEntry,
       "agentIpTrapManagerIpAddr": agentIpTrapManagerIpAddr,
       "agentIpTrapManagerComm": agentIpTrapManagerComm,
       "agentIpTrapManagerStatus": agentIpTrapManagerStatus,
       "agentConsoleModeManager": agentConsoleModeManager,
       "agentConsoleModeManagerDataBits": agentConsoleModeManagerDataBits,
       "agentConsoleModeManagerStopBits": agentConsoleModeManagerStopBits,
       "agentConsoleModeManagerParity": agentConsoleModeManagerParity,
       "agentConsoleModeManagerBaudRate": agentConsoleModeManagerBaudRate,
       "agentSlipModeManager": agentSlipModeManager,
       "agentSlipModeManagerLocalIP": agentSlipModeManagerLocalIP,
       "agentSlipModeManagerRemoteIP": agentSlipModeManagerRemoteIP,
       "agentSlipModeManagerMTU": agentSlipModeManagerMTU,
       "agentSlipModeManagerBaudRate": agentSlipModeManagerBaudRate,
       "agentSNTP": agentSNTP,
       "agentSNTPState": agentSNTPState,
       "agentSNTPTimeSource": agentSNTPTimeSource,
       "agentSNTPServer1IPAddr": agentSNTPServer1IPAddr,
       "agentSNTPServer2IPAddr": agentSNTPServer2IPAddr,
       "agentSNTPTimeZone": agentSNTPTimeZone,
       "agentSNTPPollInterval": agentSNTPPollInterval,
       "agentSNTPCurrentTime": agentSNTPCurrentTime,
       "agentSNTPUpTime": agentSNTPUpTime,
       "agentSNTPBootTime": agentSNTPBootTime,
       "agentDST": agentDST,
       "agentDSTStatus": agentDSTStatus,
       "agentDSTOffset": agentDSTOffset,
       "agentDSTRepeatingStartMonth": agentDSTRepeatingStartMonth,
       "agentDSTRepeatingStartWhichDay": agentDSTRepeatingStartWhichDay,
       "agentDSTRepeatingStartDayOfWeek": agentDSTRepeatingStartDayOfWeek,
       "agentDSTRepeatingStartHour": agentDSTRepeatingStartHour,
       "agentDSTRepeatingStartMinute": agentDSTRepeatingStartMinute,
       "agentDSTRepeatingEndMonth": agentDSTRepeatingEndMonth,
       "agentDSTRepeatingEndWhichDay": agentDSTRepeatingEndWhichDay,
       "agentDSTRepeatingEndDayOfWeek": agentDSTRepeatingEndDayOfWeek,
       "agentDSTRepeatingEndHour": agentDSTRepeatingEndHour,
       "agentDSTRepeatingEndMinute": agentDSTRepeatingEndMinute,
       "agentDSTAnnualStartMonth": agentDSTAnnualStartMonth,
       "agentDSTAnnualStartDayOfMonth": agentDSTAnnualStartDayOfMonth,
       "agentDSTAnnualStartHour": agentDSTAnnualStartHour,
       "agentDSTAnnualStartMinute": agentDSTAnnualStartMinute,
       "agentDSTAnnualEndMonth": agentDSTAnnualEndMonth,
       "agentDSTAnnualEndDayOfMonth": agentDSTAnnualEndDayOfMonth,
       "agentDSTAnnualEndHour": agentDSTAnnualEndHour,
       "agentDSTAnnualEndMinute": agentDSTAnnualEndMinute,
       "agentSwitchCommonMgmt": agentSwitchCommonMgmt,
       "agentSwitchCube": agentSwitchCube,
       "agentSwitchCubeTable": agentSwitchCubeTable,
       "agentSwitchCubeEntry": agentSwitchCubeEntry,
       "agentSwitchCubeType": agentSwitchCubeType,
       "agentSwitchCubeSpareName": agentSwitchCubeSpareName,
       "agentSwitchCubeSparePartNumber": agentSwitchCubeSparePartNumber,
       "agentSwitchPowerSupply": agentSwitchPowerSupply,
       "agentSwitchPowerSupplyTable": agentSwitchPowerSupplyTable,
       "agentSwitchPowerSupplyEntry": agentSwitchPowerSupplyEntry,
       "agentSwitchPowerSupplyIndex": agentSwitchPowerSupplyIndex,
       "agentSwitchPowerSupplyMaxPwrOutput": agentSwitchPowerSupplyMaxPwrOutput,
       "agentSwitchPowerSupplyCurPwrOutput": agentSwitchPowerSupplyCurPwrOutput,
       "agentSwitchPowerSupplyIntakeTemp": agentSwitchPowerSupplyIntakeTemp,
       "agentSwitchPowerSupplyExhaustTemp": agentSwitchPowerSupplyExhaustTemp,
       "agentSwitchPowerSupplyStatus": agentSwitchPowerSupplyStatus,
       "agentSwitchPowerSupplyInputLineStatus": agentSwitchPowerSupplyInputLineStatus,
       "agentSwitchPowerSupplyCondition": agentSwitchPowerSupplyCondition,
       "agentSwitchFan": agentSwitchFan,
       "agentSwitchFanTable": agentSwitchFanTable,
       "agentSwitchFanEntry": agentSwitchFanEntry,
       "agentSwitchFanIndex": agentSwitchFanIndex,
       "agentSwitchFanCondition": agentSwitchFanCondition,
       "agentSwitchTempSensor": agentSwitchTempSensor,
       "agentSwitchTempSensorTable": agentSwitchTempSensorTable,
       "agentSwitchTempSensorEntry": agentSwitchTempSensorEntry,
       "agentSwitchTempSensorIndex": agentSwitchTempSensorIndex,
       "agentSwitchTempSensorCurrent": agentSwitchTempSensorCurrent,
       "agentSwitchTempSensorThreshold": agentSwitchTempSensorThreshold,
       "agentSwitchTempSensorCondition": agentSwitchTempSensorCondition,
       "agentSwitchTempSensorTempType": agentSwitchTempSensorTempType,
       "endOfMIB": endOfMIB}
)
