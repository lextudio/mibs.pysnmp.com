# SNMP MIB module (COMMON-GOLF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/COMMON-GOLF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:16:43 2024
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
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Fore_ObjectIdentity = ObjectIdentity
fore = _Fore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326)
)
_Systems_ObjectIdentity = ObjectIdentity
systems = _Systems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2)
)
_Ethernet_ObjectIdentity = ObjectIdentity
ethernet = _Ethernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20)
)
_Edge_ObjectIdentity = ObjectIdentity
edge = _Edge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1)
)
_Edgecommon_ObjectIdentity = ObjectIdentity
edgecommon = _Edgecommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 1)
)
_Golf_ObjectIdentity = ObjectIdentity
golf = _Golf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2)
)
_Golfproducts_ObjectIdentity = ObjectIdentity
golfproducts = _Golfproducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 1)
)
_Golfcommon_ObjectIdentity = ObjectIdentity
golfcommon = _Golfcommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2)
)
_Fore_mgmt_ObjectIdentity = ObjectIdentity
fore_mgmt = _Fore_mgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2)
)
_AgentMgmt_ObjectIdentity = ObjectIdentity
agentMgmt = _AgentMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1)
)
_AgentBasicInfo_ObjectIdentity = ObjectIdentity
agentBasicInfo = _AgentBasicInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 1)
)


class _AgentRuntimeSwVersion_Type(DisplayString):
    """Custom type agentRuntimeSwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_AgentRuntimeSwVersion_Type.__name__ = "DisplayString"
_AgentRuntimeSwVersion_Object = MibScalar
agentRuntimeSwVersion = _AgentRuntimeSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 1, 1),
    _AgentRuntimeSwVersion_Type()
)
agentRuntimeSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentRuntimeSwVersion.setStatus("mandatory")


class _AgentPromFwVersion_Type(DisplayString):
    """Custom type agentPromFwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_AgentPromFwVersion_Type.__name__ = "DisplayString"
_AgentPromFwVersion_Object = MibScalar
agentPromFwVersion = _AgentPromFwVersion_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 1, 2),
    _AgentPromFwVersion_Type()
)
agentPromFwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPromFwVersion.setStatus("mandatory")
_AgentHwRevision_Type = Integer32
_AgentHwRevision_Object = MibScalar
agentHwRevision = _AgentHwRevision_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 1, 3),
    _AgentHwRevision_Type()
)
agentHwRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentHwRevision.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 1, 4),
    _AgentMgmtProtocolCapability_Type()
)
agentMgmtProtocolCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMgmtProtocolCapability.setStatus("mandatory")
_AgentMibCapabilityTable_Object = MibTable
agentMibCapabilityTable = _AgentMibCapabilityTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 1, 5)
)
if mibBuilder.loadTexts:
    agentMibCapabilityTable.setStatus("mandatory")
_AgentMibCapabilityEntry_Object = MibTableRow
agentMibCapabilityEntry = _AgentMibCapabilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 1, 5, 1)
)
agentMibCapabilityEntry.setIndexNames(
    (0, "COMMON-GOLF-MIB", "agentMibCapabilityIndex"),
)
if mibBuilder.loadTexts:
    agentMibCapabilityEntry.setStatus("mandatory")
_AgentMibCapabilityIndex_Type = Integer32
_AgentMibCapabilityIndex_Object = MibTableColumn
agentMibCapabilityIndex = _AgentMibCapabilityIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 1, 5, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 1, 5, 1, 2),
    _AgentMibCapabilityDescr_Type()
)
agentMibCapabilityDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMibCapabilityDescr.setStatus("mandatory")
_AgentMibCapabilityVersion_Type = Integer32
_AgentMibCapabilityVersion_Object = MibTableColumn
agentMibCapabilityVersion = _AgentMibCapabilityVersion_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 1, 5, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 1, 5, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 1, 7),
    _AgentStatusSaveCfg_Type()
)
agentStatusSaveCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentStatusSaveCfg.setStatus("mandatory")
_AgentBasicConfig_ObjectIdentity = ObjectIdentity
agentBasicConfig = _AgentBasicConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 2)
)


class _AgentUpdateSource_Type(Integer32):
    """Custom type agentUpdateSource based on Integer32"""
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


_AgentUpdateSource_Type.__name__ = "Integer32"
_AgentUpdateSource_Object = MibScalar
agentUpdateSource = _AgentUpdateSource_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 2, 1),
    _AgentUpdateSource_Type()
)
agentUpdateSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentUpdateSource.setStatus("mandatory")


class _AgentCfgUpdateCtrl_Type(Integer32):
    """Custom type agentCfgUpdateCtrl based on Integer32"""
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


_AgentCfgUpdateCtrl_Type.__name__ = "Integer32"
_AgentCfgUpdateCtrl_Object = MibScalar
agentCfgUpdateCtrl = _AgentCfgUpdateCtrl_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 2, 2),
    _AgentCfgUpdateCtrl_Type()
)
agentCfgUpdateCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentCfgUpdateCtrl.setStatus("mandatory")


class _AgentCfgUpdateFile_Type(DisplayString):
    """Custom type agentCfgUpdateFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AgentCfgUpdateFile_Type.__name__ = "DisplayString"
_AgentCfgUpdateFile_Object = MibScalar
agentCfgUpdateFile = _AgentCfgUpdateFile_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 2, 3),
    _AgentCfgUpdateFile_Type()
)
agentCfgUpdateFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentCfgUpdateFile.setStatus("mandatory")


class _AgentSoftwareUpdateCtrl_Type(Integer32):
    """Custom type agentSoftwareUpdateCtrl based on Integer32"""
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


_AgentSoftwareUpdateCtrl_Type.__name__ = "Integer32"
_AgentSoftwareUpdateCtrl_Object = MibScalar
agentSoftwareUpdateCtrl = _AgentSoftwareUpdateCtrl_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 2, 4),
    _AgentSoftwareUpdateCtrl_Type()
)
agentSoftwareUpdateCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSoftwareUpdateCtrl.setStatus("mandatory")


class _AgentSoftwareUdateFile_Type(DisplayString):
    """Custom type agentSoftwareUdateFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AgentSoftwareUdateFile_Type.__name__ = "DisplayString"
_AgentSoftwareUdateFile_Object = MibScalar
agentSoftwareUdateFile = _AgentSoftwareUdateFile_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 2, 5),
    _AgentSoftwareUdateFile_Type()
)
agentSoftwareUdateFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSoftwareUdateFile.setStatus("mandatory")


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
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 2, 6),
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
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 2, 7),
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
              5)
        )
    )
    namedValues = NamedValues(
        *(("baudRate-19200", 4),
          ("baudRate-2400", 2),
          ("baudRate-38400", 5),
          ("baudRate-9600", 3),
          ("other", 1))
    )


_AgentOutOfBandBaudRateConfig_Type.__name__ = "Integer32"
_AgentOutOfBandBaudRateConfig_Object = MibScalar
agentOutOfBandBaudRateConfig = _AgentOutOfBandBaudRateConfig_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 2, 8),
    _AgentOutOfBandBaudRateConfig_Type()
)
agentOutOfBandBaudRateConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentOutOfBandBaudRateConfig.setStatus("mandatory")
_AgentSaveCfg_Type = Integer32
_AgentSaveCfg_Object = MibScalar
agentSaveCfg = _AgentSaveCfg_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 2, 9),
    _AgentSaveCfg_Type()
)
agentSaveCfg.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    agentSaveCfg.setStatus("mandatory")
_AgentIpProtoConfig_ObjectIdentity = ObjectIdentity
agentIpProtoConfig = _AgentIpProtoConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 3)
)
_AgentIpNumOfIf_Type = Integer32
_AgentIpNumOfIf_Object = MibScalar
agentIpNumOfIf = _AgentIpNumOfIf_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 3, 1),
    _AgentIpNumOfIf_Type()
)
agentIpNumOfIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIpNumOfIf.setStatus("mandatory")
_AgentIpIfTable_Object = MibTable
agentIpIfTable = _AgentIpIfTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    agentIpIfTable.setStatus("mandatory")
_AgentIpIfEntry_Object = MibTableRow
agentIpIfEntry = _AgentIpIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 3, 2, 1)
)
agentIpIfEntry.setIndexNames(
    (0, "COMMON-GOLF-MIB", "agentIpIfIndex"),
)
if mibBuilder.loadTexts:
    agentIpIfEntry.setStatus("mandatory")


class _AgentIpIfIndex_Type(Integer32):
    """Custom type agentIpIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AgentIpIfIndex_Type.__name__ = "Integer32"
_AgentIpIfIndex_Object = MibTableColumn
agentIpIfIndex = _AgentIpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 3, 2, 1, 1),
    _AgentIpIfIndex_Type()
)
agentIpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIpIfIndex.setStatus("mandatory")
_AgentIpIfAddress_Type = IpAddress
_AgentIpIfAddress_Object = MibTableColumn
agentIpIfAddress = _AgentIpIfAddress_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 3, 2, 1, 2),
    _AgentIpIfAddress_Type()
)
agentIpIfAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIpIfAddress.setStatus("mandatory")
_AgentIpIfNetMask_Type = IpAddress
_AgentIpIfNetMask_Object = MibTableColumn
agentIpIfNetMask = _AgentIpIfNetMask_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 3, 2, 1, 3),
    _AgentIpIfNetMask_Type()
)
agentIpIfNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIpIfNetMask.setStatus("mandatory")
_AgentIpIfDefaultRouter_Type = IpAddress
_AgentIpIfDefaultRouter_Object = MibTableColumn
agentIpIfDefaultRouter = _AgentIpIfDefaultRouter_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 3, 2, 1, 4),
    _AgentIpIfDefaultRouter_Type()
)
agentIpIfDefaultRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIpIfDefaultRouter.setStatus("mandatory")
_AgentIpIfMacAddr_Type = PhysAddress
_AgentIpIfMacAddr_Object = MibTableColumn
agentIpIfMacAddr = _AgentIpIfMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 3, 2, 1, 5),
    _AgentIpIfMacAddr_Type()
)
agentIpIfMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIpIfMacAddr.setStatus("mandatory")


class _AgentIpIfType_Type(Integer32):
    """Custom type agentIpIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              6,
              28)
        )
    )
    namedValues = NamedValues(
        *(("ethernet-csmacd", 6),
          ("other", 1),
          ("slip", 28))
    )


_AgentIpIfType_Type.__name__ = "Integer32"
_AgentIpIfType_Object = MibTableColumn
agentIpIfType = _AgentIpIfType_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 3, 2, 1, 6),
    _AgentIpIfType_Type()
)
agentIpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIpIfType.setStatus("mandatory")
_AgentIpBootServerAddr_Type = IpAddress
_AgentIpBootServerAddr_Object = MibScalar
agentIpBootServerAddr = _AgentIpBootServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 3, 3),
    _AgentIpBootServerAddr_Type()
)
agentIpBootServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIpBootServerAddr.setStatus("mandatory")


class _AgentIpGetIpFromBootpServer_Type(Integer32):
    """Custom type agentIpGetIpFromBootpServer based on Integer32"""
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
        *(("from-bootp", 3),
          ("from-dhcp", 4),
          ("manual", 2),
          ("other", 1))
    )


_AgentIpGetIpFromBootpServer_Type.__name__ = "Integer32"
_AgentIpGetIpFromBootpServer_Object = MibScalar
agentIpGetIpFromBootpServer = _AgentIpGetIpFromBootpServer_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 3, 4),
    _AgentIpGetIpFromBootpServer_Type()
)
agentIpGetIpFromBootpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIpGetIpFromBootpServer.setStatus("mandatory")
_AgentIpUnauthAddr_Type = IpAddress
_AgentIpUnauthAddr_Object = MibScalar
agentIpUnauthAddr = _AgentIpUnauthAddr_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 3, 5),
    _AgentIpUnauthAddr_Type()
)
agentIpUnauthAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIpUnauthAddr.setStatus("mandatory")


class _AgentIpUnauthComm_Type(DisplayString):
    """Custom type agentIpUnauthComm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AgentIpUnauthComm_Type.__name__ = "DisplayString"
_AgentIpUnauthComm_Object = MibScalar
agentIpUnauthComm = _AgentIpUnauthComm_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 3, 6),
    _AgentIpUnauthComm_Type()
)
agentIpUnauthComm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIpUnauthComm.setStatus("mandatory")
_AgentIpLastBootServerAddr_Type = IpAddress
_AgentIpLastBootServerAddr_Object = MibScalar
agentIpLastBootServerAddr = _AgentIpLastBootServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 3, 7),
    _AgentIpLastBootServerAddr_Type()
)
agentIpLastBootServerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIpLastBootServerAddr.setStatus("mandatory")
_AgentIpLastIpAddr_Type = IpAddress
_AgentIpLastIpAddr_Object = MibScalar
agentIpLastIpAddr = _AgentIpLastIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 3, 8),
    _AgentIpLastIpAddr_Type()
)
agentIpLastIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIpLastIpAddr.setStatus("mandatory")
_AgentIpTrapManagerTable_Object = MibTable
agentIpTrapManagerTable = _AgentIpTrapManagerTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 3, 9)
)
if mibBuilder.loadTexts:
    agentIpTrapManagerTable.setStatus("mandatory")
_AgentIpTrapManagerEntry_Object = MibTableRow
agentIpTrapManagerEntry = _AgentIpTrapManagerEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 3, 9, 1)
)
agentIpTrapManagerEntry.setIndexNames(
    (0, "COMMON-GOLF-MIB", "agentIpTrapManagerIpAddr"),
)
if mibBuilder.loadTexts:
    agentIpTrapManagerEntry.setStatus("mandatory")
_AgentIpTrapManagerIpAddr_Type = IpAddress
_AgentIpTrapManagerIpAddr_Object = MibTableColumn
agentIpTrapManagerIpAddr = _AgentIpTrapManagerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 3, 9, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 3, 9, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 1, 3, 9, 1, 3),
    _AgentIpTrapManagerStatus_Type()
)
agentIpTrapManagerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIpTrapManagerStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "COMMON-GOLF-MIB",
    **{"fore": fore,
       "systems": systems,
       "ethernet": ethernet,
       "edge": edge,
       "edgecommon": edgecommon,
       "golf": golf,
       "golfproducts": golfproducts,
       "golfcommon": golfcommon,
       "fore-mgmt": fore_mgmt,
       "agentMgmt": agentMgmt,
       "agentBasicInfo": agentBasicInfo,
       "agentRuntimeSwVersion": agentRuntimeSwVersion,
       "agentPromFwVersion": agentPromFwVersion,
       "agentHwRevision": agentHwRevision,
       "agentMgmtProtocolCapability": agentMgmtProtocolCapability,
       "agentMibCapabilityTable": agentMibCapabilityTable,
       "agentMibCapabilityEntry": agentMibCapabilityEntry,
       "agentMibCapabilityIndex": agentMibCapabilityIndex,
       "agentMibCapabilityDescr": agentMibCapabilityDescr,
       "agentMibCapabilityVersion": agentMibCapabilityVersion,
       "agentMibCapabilityType": agentMibCapabilityType,
       "agentStatusConsoleInUse": agentStatusConsoleInUse,
       "agentStatusSaveCfg": agentStatusSaveCfg,
       "agentBasicConfig": agentBasicConfig,
       "agentUpdateSource": agentUpdateSource,
       "agentCfgUpdateCtrl": agentCfgUpdateCtrl,
       "agentCfgUpdateFile": agentCfgUpdateFile,
       "agentSoftwareUpdateCtrl": agentSoftwareUpdateCtrl,
       "agentSoftwareUdateFile": agentSoftwareUdateFile,
       "agentSystemReset": agentSystemReset,
       "agentRs232PortConfig": agentRs232PortConfig,
       "agentOutOfBandBaudRateConfig": agentOutOfBandBaudRateConfig,
       "agentSaveCfg": agentSaveCfg,
       "agentIpProtoConfig": agentIpProtoConfig,
       "agentIpNumOfIf": agentIpNumOfIf,
       "agentIpIfTable": agentIpIfTable,
       "agentIpIfEntry": agentIpIfEntry,
       "agentIpIfIndex": agentIpIfIndex,
       "agentIpIfAddress": agentIpIfAddress,
       "agentIpIfNetMask": agentIpIfNetMask,
       "agentIpIfDefaultRouter": agentIpIfDefaultRouter,
       "agentIpIfMacAddr": agentIpIfMacAddr,
       "agentIpIfType": agentIpIfType,
       "agentIpBootServerAddr": agentIpBootServerAddr,
       "agentIpGetIpFromBootpServer": agentIpGetIpFromBootpServer,
       "agentIpUnauthAddr": agentIpUnauthAddr,
       "agentIpUnauthComm": agentIpUnauthComm,
       "agentIpLastBootServerAddr": agentIpLastBootServerAddr,
       "agentIpLastIpAddr": agentIpLastIpAddr,
       "agentIpTrapManagerTable": agentIpTrapManagerTable,
       "agentIpTrapManagerEntry": agentIpTrapManagerEntry,
       "agentIpTrapManagerIpAddr": agentIpTrapManagerIpAddr,
       "agentIpTrapManagerComm": agentIpTrapManagerComm,
       "agentIpTrapManagerStatus": agentIpTrapManagerStatus}
)
