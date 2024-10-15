# SNMP MIB module (ASANTE-SWITCH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASANTE-SWITCH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:40:50 2024
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



class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Asante_ObjectIdentity = ObjectIdentity
asante = _Asante_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 298)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 298, 1)
)
_SnmpAgent_ObjectIdentity = ObjectIdentity
snmpAgent = _SnmpAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 298, 1, 1)
)
_AgentSw_ObjectIdentity = ObjectIdentity
agentSw = _AgentSw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 298, 1, 1, 1)
)
_AgentRunTimeImageMajorVer_Type = Integer32
_AgentRunTimeImageMajorVer_Object = MibScalar
agentRunTimeImageMajorVer = _AgentRunTimeImageMajorVer_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 1, 1, 1),
    _AgentRunTimeImageMajorVer_Type()
)
agentRunTimeImageMajorVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentRunTimeImageMajorVer.setStatus("mandatory")
_AgentRunTimeImageMinorVer_Type = Integer32
_AgentRunTimeImageMinorVer_Object = MibScalar
agentRunTimeImageMinorVer = _AgentRunTimeImageMinorVer_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 1, 1, 2),
    _AgentRunTimeImageMinorVer_Type()
)
agentRunTimeImageMinorVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentRunTimeImageMinorVer.setStatus("mandatory")


class _AgentImageLoadMode_Type(Integer32):
    """Custom type agentImageLoadMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("localBoot", 2),
          ("netBoot", 3),
          ("other", 1))
    )


_AgentImageLoadMode_Type.__name__ = "Integer32"
_AgentImageLoadMode_Object = MibScalar
agentImageLoadMode = _AgentImageLoadMode_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 1, 1, 3),
    _AgentImageLoadMode_Type()
)
agentImageLoadMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentImageLoadMode.setStatus("mandatory")


class _AgentRemoteBootInfo_Type(Integer32):
    """Custom type agentRemoteBootInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eepromBootInfo", 2),
          ("other", 1))
    )


_AgentRemoteBootInfo_Type.__name__ = "Integer32"
_AgentRemoteBootInfo_Object = MibScalar
agentRemoteBootInfo = _AgentRemoteBootInfo_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 1, 1, 4),
    _AgentRemoteBootInfo_Type()
)
agentRemoteBootInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentRemoteBootInfo.setStatus("mandatory")


class _AgentRemoteBootProtocol_Type(Integer32):
    """Custom type agentRemoteBootProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bootp-tftp", 2),
          ("other", 1),
          ("tftp-only", 3))
    )


_AgentRemoteBootProtocol_Type.__name__ = "Integer32"
_AgentRemoteBootProtocol_Object = MibScalar
agentRemoteBootProtocol = _AgentRemoteBootProtocol_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 1, 1, 5),
    _AgentRemoteBootProtocol_Type()
)
agentRemoteBootProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRemoteBootProtocol.setStatus("mandatory")


class _AgentRemoteBootFile_Type(DisplayString):
    """Custom type agentRemoteBootFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AgentRemoteBootFile_Type.__name__ = "DisplayString"
_AgentRemoteBootFile_Object = MibScalar
agentRemoteBootFile = _AgentRemoteBootFile_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 1, 1, 6),
    _AgentRemoteBootFile_Type()
)
agentRemoteBootFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRemoteBootFile.setStatus("mandatory")


class _AgentOutBandDialString_Type(DisplayString):
    """Custom type agentOutBandDialString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AgentOutBandDialString_Type.__name__ = "DisplayString"
_AgentOutBandDialString_Object = MibScalar
agentOutBandDialString = _AgentOutBandDialString_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 1, 1, 7),
    _AgentOutBandDialString_Type()
)
agentOutBandDialString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentOutBandDialString.setStatus("mandatory")


class _AgentOutBandBaudRate_Type(Integer32):
    """Custom type agentOutBandBaudRate based on Integer32"""
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
        *(("b1200", 2),
          ("b19200", 6),
          ("b2400", 3),
          ("b4800", 4),
          ("b9600", 5),
          ("other", 1))
    )


_AgentOutBandBaudRate_Type.__name__ = "Integer32"
_AgentOutBandBaudRate_Object = MibScalar
agentOutBandBaudRate = _AgentOutBandBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 1, 1, 8),
    _AgentOutBandBaudRate_Type()
)
agentOutBandBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentOutBandBaudRate.setStatus("mandatory")


class _AgentReset_Type(Integer32):
    """Custom type agentReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("not-reset", 3),
          ("other", 1),
          ("reset", 2))
    )


_AgentReset_Type.__name__ = "Integer32"
_AgentReset_Object = MibScalar
agentReset = _AgentReset_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 1, 1, 9),
    _AgentReset_Type()
)
agentReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentReset.setStatus("mandatory")
_AgentFw_ObjectIdentity = ObjectIdentity
agentFw = _AgentFw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 298, 1, 1, 2)
)
_AgentFwMajorVer_Type = Integer32
_AgentFwMajorVer_Object = MibScalar
agentFwMajorVer = _AgentFwMajorVer_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 1, 2, 1),
    _AgentFwMajorVer_Type()
)
agentFwMajorVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentFwMajorVer.setStatus("mandatory")
_AgentFwMinorVer_Type = Integer32
_AgentFwMinorVer_Object = MibScalar
agentFwMinorVer = _AgentFwMinorVer_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 1, 2, 2),
    _AgentFwMinorVer_Type()
)
agentFwMinorVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentFwMinorVer.setStatus("mandatory")
_AgentHw_ObjectIdentity = ObjectIdentity
agentHw = _AgentHw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 298, 1, 1, 3)
)
_AgentHwReVer_Type = Integer32
_AgentHwReVer_Object = MibScalar
agentHwReVer = _AgentHwReVer_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 1, 3, 1),
    _AgentHwReVer_Type()
)
agentHwReVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentHwReVer.setStatus("mandatory")
_AgentHwVer_Type = Integer32
_AgentHwVer_Object = MibScalar
agentHwVer = _AgentHwVer_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 1, 3, 2),
    _AgentHwVer_Type()
)
agentHwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentHwVer.setStatus("mandatory")


class _AgentNetProtoStkCapMap_Type(OctetString):
    """Custom type agentNetProtoStkCapMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_AgentNetProtoStkCapMap_Type.__name__ = "OctetString"
_AgentNetProtoStkCapMap_Object = MibScalar
agentNetProtoStkCapMap = _AgentNetProtoStkCapMap_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 1, 4),
    _AgentNetProtoStkCapMap_Type()
)
agentNetProtoStkCapMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentNetProtoStkCapMap.setStatus("mandatory")
_AgentNetProtocol_ObjectIdentity = ObjectIdentity
agentNetProtocol = _AgentNetProtocol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 298, 1, 1, 5)
)
_IpagentProtocol_ObjectIdentity = ObjectIdentity
ipagentProtocol = _IpagentProtocol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 298, 1, 1, 5, 1)
)
_IpagentIpAddr_Type = IpAddress
_IpagentIpAddr_Object = MibScalar
ipagentIpAddr = _IpagentIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 1, 5, 1, 1),
    _IpagentIpAddr_Type()
)
ipagentIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipagentIpAddr.setStatus("mandatory")
_IpagentIpNetMask_Type = IpAddress
_IpagentIpNetMask_Object = MibScalar
ipagentIpNetMask = _IpagentIpNetMask_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 1, 5, 1, 2),
    _IpagentIpNetMask_Type()
)
ipagentIpNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipagentIpNetMask.setStatus("mandatory")
_IpagentDefaultGateway_Type = IpAddress
_IpagentDefaultGateway_Object = MibScalar
ipagentDefaultGateway = _IpagentDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 1, 5, 1, 3),
    _IpagentDefaultGateway_Type()
)
ipagentDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipagentDefaultGateway.setStatus("mandatory")
_IpagentBootServerAddr_Type = IpAddress
_IpagentBootServerAddr_Object = MibScalar
ipagentBootServerAddr = _IpagentBootServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 1, 5, 1, 4),
    _IpagentBootServerAddr_Type()
)
ipagentBootServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipagentBootServerAddr.setStatus("mandatory")
_IpagentUnAuthIP_Type = IpAddress
_IpagentUnAuthIP_Object = MibScalar
ipagentUnAuthIP = _IpagentUnAuthIP_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 1, 5, 1, 5),
    _IpagentUnAuthIP_Type()
)
ipagentUnAuthIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipagentUnAuthIP.setStatus("mandatory")
_IpagentUnAuthComm_Type = DisplayString
_IpagentUnAuthComm_Object = MibScalar
ipagentUnAuthComm = _IpagentUnAuthComm_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 1, 5, 1, 6),
    _IpagentUnAuthComm_Type()
)
ipagentUnAuthComm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipagentUnAuthComm.setStatus("mandatory")
_IpagentTrapRcvrTable_Object = MibTable
ipagentTrapRcvrTable = _IpagentTrapRcvrTable_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 1, 5, 2)
)
if mibBuilder.loadTexts:
    ipagentTrapRcvrTable.setStatus("mandatory")
_IpagentTrapRcvrEntry_Object = MibTableRow
ipagentTrapRcvrEntry = _IpagentTrapRcvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 1, 5, 2, 1)
)
ipagentTrapRcvrEntry.setIndexNames(
    (0, "ASANTE-SWITCH-MIB", "ipagentTrapRcvrIpAddr"),
)
if mibBuilder.loadTexts:
    ipagentTrapRcvrEntry.setStatus("mandatory")
_IpagentTrapRcvrIpAddr_Type = IpAddress
_IpagentTrapRcvrIpAddr_Object = MibTableColumn
ipagentTrapRcvrIpAddr = _IpagentTrapRcvrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 1, 5, 2, 1, 1),
    _IpagentTrapRcvrIpAddr_Type()
)
ipagentTrapRcvrIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipagentTrapRcvrIpAddr.setStatus("mandatory")


class _IpagentTrapRcvrStatus_Type(Integer32):
    """Custom type ipagentTrapRcvrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 3),
          ("other", 1),
          ("valid", 2))
    )


_IpagentTrapRcvrStatus_Type.__name__ = "Integer32"
_IpagentTrapRcvrStatus_Object = MibTableColumn
ipagentTrapRcvrStatus = _IpagentTrapRcvrStatus_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 1, 5, 2, 1, 2),
    _IpagentTrapRcvrStatus_Type()
)
ipagentTrapRcvrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipagentTrapRcvrStatus.setStatus("mandatory")
_IpagentTrapRcvrComm_Type = DisplayString
_IpagentTrapRcvrComm_Object = MibTableColumn
ipagentTrapRcvrComm = _IpagentTrapRcvrComm_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 1, 5, 2, 1, 3),
    _IpagentTrapRcvrComm_Type()
)
ipagentTrapRcvrComm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipagentTrapRcvrComm.setStatus("mandatory")
_Switch_ObjectIdentity = ObjectIdentity
switch = _Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 298, 1, 5)
)
_EAsntSwitch_ObjectIdentity = ObjectIdentity
eAsntSwitch = _EAsntSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1)
)
_ESWAgent_ObjectIdentity = ObjectIdentity
eSWAgent = _ESWAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 1)
)
_ESWAgentSW_ObjectIdentity = ObjectIdentity
eSWAgentSW = _ESWAgentSW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 1, 1)
)


class _ESWUpDownloadAction_Type(Integer32):
    """Custom type eSWUpDownloadAction based on Integer32"""
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
        *(("download", 3),
          ("off", 2),
          ("other", 1),
          ("upload", 4))
    )


_ESWUpDownloadAction_Type.__name__ = "Integer32"
_ESWUpDownloadAction_Object = MibScalar
eSWUpDownloadAction = _ESWUpDownloadAction_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 1, 1, 1),
    _ESWUpDownloadAction_Type()
)
eSWUpDownloadAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eSWUpDownloadAction.setStatus("mandatory")


class _ESWUpDownloadStatus_Type(Integer32):
    """Custom type eSWUpDownloadStatus based on Integer32"""
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
        *(("action-Failure", 3),
          ("action-Success", 2),
          ("configError", 6),
          ("in-Progress", 4),
          ("no-Action", 5),
          ("other", 1))
    )


_ESWUpDownloadStatus_Type.__name__ = "Integer32"
_ESWUpDownloadStatus_Object = MibScalar
eSWUpDownloadStatus = _ESWUpDownloadStatus_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 1, 1, 2),
    _ESWUpDownloadStatus_Type()
)
eSWUpDownloadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSWUpDownloadStatus.setStatus("mandatory")


class _ESWRemoteDownloadFile_Type(Integer32):
    """Custom type eSWRemoteDownloadFile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("config-File", 2),
          ("image-File", 3),
          ("other", 1))
    )


_ESWRemoteDownloadFile_Type.__name__ = "Integer32"
_ESWRemoteDownloadFile_Object = MibScalar
eSWRemoteDownloadFile = _ESWRemoteDownloadFile_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 1, 1, 3),
    _ESWRemoteDownloadFile_Type()
)
eSWRemoteDownloadFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eSWRemoteDownloadFile.setStatus("mandatory")
_ESWRemoteConfigServer_Type = IpAddress
_ESWRemoteConfigServer_Object = MibScalar
eSWRemoteConfigServer = _ESWRemoteConfigServer_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 1, 1, 4),
    _ESWRemoteConfigServer_Type()
)
eSWRemoteConfigServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eSWRemoteConfigServer.setStatus("mandatory")


class _ESWRemoteConfigFileName_Type(DisplayString):
    """Custom type eSWRemoteConfigFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ESWRemoteConfigFileName_Type.__name__ = "DisplayString"
_ESWRemoteConfigFileName_Object = MibScalar
eSWRemoteConfigFileName = _ESWRemoteConfigFileName_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 1, 1, 5),
    _ESWRemoteConfigFileName_Type()
)
eSWRemoteConfigFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eSWRemoteConfigFileName.setStatus("mandatory")


class _ESWConfigRetryCounter_Type(Integer32):
    """Custom type eSWConfigRetryCounter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_ESWConfigRetryCounter_Type.__name__ = "Integer32"
_ESWConfigRetryCounter_Object = MibScalar
eSWConfigRetryCounter = _ESWConfigRetryCounter_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 1, 1, 6),
    _ESWConfigRetryCounter_Type()
)
eSWConfigRetryCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eSWConfigRetryCounter.setStatus("mandatory")
_ESWRemoteImageServer_Type = IpAddress
_ESWRemoteImageServer_Object = MibScalar
eSWRemoteImageServer = _ESWRemoteImageServer_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 1, 1, 7),
    _ESWRemoteImageServer_Type()
)
eSWRemoteImageServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eSWRemoteImageServer.setStatus("mandatory")


class _ESWRemoteImageFileName_Type(DisplayString):
    """Custom type eSWRemoteImageFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_ESWRemoteImageFileName_Type.__name__ = "DisplayString"
_ESWRemoteImageFileName_Object = MibScalar
eSWRemoteImageFileName = _ESWRemoteImageFileName_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 1, 1, 8),
    _ESWRemoteImageFileName_Type()
)
eSWRemoteImageFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eSWRemoteImageFileName.setStatus("mandatory")


class _ESWImageRetryCounter_Type(Integer32):
    """Custom type eSWImageRetryCounter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_ESWImageRetryCounter_Type.__name__ = "Integer32"
_ESWImageRetryCounter_Object = MibScalar
eSWImageRetryCounter = _ESWImageRetryCounter_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 1, 1, 9),
    _ESWImageRetryCounter_Type()
)
eSWImageRetryCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eSWImageRetryCounter.setStatus("mandatory")


class _ESWActiveImageBank_Type(Integer32):
    """Custom type eSWActiveImageBank based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bank1", 2),
          ("bank2", 3),
          ("other", 1))
    )


_ESWActiveImageBank_Type.__name__ = "Integer32"
_ESWActiveImageBank_Object = MibScalar
eSWActiveImageBank = _ESWActiveImageBank_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 1, 1, 10),
    _ESWActiveImageBank_Type()
)
eSWActiveImageBank.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eSWActiveImageBank.setStatus("mandatory")


class _ESWRemoteDownloadImageBank_Type(Integer32):
    """Custom type eSWRemoteDownloadImageBank based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bank1", 2),
          ("bank2", 3),
          ("other", 1))
    )


_ESWRemoteDownloadImageBank_Type.__name__ = "Integer32"
_ESWRemoteDownloadImageBank_Object = MibScalar
eSWRemoteDownloadImageBank = _ESWRemoteDownloadImageBank_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 1, 1, 11),
    _ESWRemoteDownloadImageBank_Type()
)
eSWRemoteDownloadImageBank.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eSWRemoteDownloadImageBank.setStatus("mandatory")


class _ESWResetWaitTime_Type(Integer32):
    """Custom type eSWResetWaitTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400),
    )


_ESWResetWaitTime_Type.__name__ = "Integer32"
_ESWResetWaitTime_Object = MibScalar
eSWResetWaitTime = _ESWResetWaitTime_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 1, 1, 12),
    _ESWResetWaitTime_Type()
)
eSWResetWaitTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eSWResetWaitTime.setStatus("mandatory")
_ESWResetLeftTime_Type = Integer32
_ESWResetLeftTime_Object = MibScalar
eSWResetLeftTime = _ESWResetLeftTime_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 1, 1, 13),
    _ESWResetLeftTime_Type()
)
eSWResetLeftTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSWResetLeftTime.setStatus("mandatory")
_ESWBankImageInfoTable_Object = MibTable
eSWBankImageInfoTable = _ESWBankImageInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 1, 1, 14)
)
if mibBuilder.loadTexts:
    eSWBankImageInfoTable.setStatus("mandatory")
_ESWBankImageInfoEntry_Object = MibTableRow
eSWBankImageInfoEntry = _ESWBankImageInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 1, 1, 14, 1)
)
eSWBankImageInfoEntry.setIndexNames(
    (0, "ASANTE-SWITCH-MIB", "eSWBankIndex"),
)
if mibBuilder.loadTexts:
    eSWBankImageInfoEntry.setStatus("mandatory")


class _ESWBankIndex_Type(Integer32):
    """Custom type eSWBankIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_ESWBankIndex_Type.__name__ = "Integer32"
_ESWBankIndex_Object = MibTableColumn
eSWBankIndex = _ESWBankIndex_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 1, 1, 14, 1, 1),
    _ESWBankIndex_Type()
)
eSWBankIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSWBankIndex.setStatus("mandatory")
_ESWMajorVer_Type = Integer32
_ESWMajorVer_Object = MibTableColumn
eSWMajorVer = _ESWMajorVer_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 1, 1, 14, 1, 2),
    _ESWMajorVer_Type()
)
eSWMajorVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSWMajorVer.setStatus("mandatory")
_ESWMinorVer_Type = Integer32
_ESWMinorVer_Object = MibTableColumn
eSWMinorVer = _ESWMinorVer_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 1, 1, 14, 1, 3),
    _ESWMinorVer_Type()
)
eSWMinorVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSWMinorVer.setStatus("mandatory")
_ESWDateTime_Type = DisplayString
_ESWDateTime_Object = MibTableColumn
eSWDateTime = _ESWDateTime_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 1, 1, 14, 1, 4),
    _ESWDateTime_Type()
)
eSWDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSWDateTime.setStatus("mandatory")


class _ESWTelnetSessions_Type(Integer32):
    """Custom type eSWTelnetSessions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_ESWTelnetSessions_Type.__name__ = "Integer32"
_ESWTelnetSessions_Object = MibScalar
eSWTelnetSessions = _ESWTelnetSessions_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 1, 1, 15),
    _ESWTelnetSessions_Type()
)
eSWTelnetSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSWTelnetSessions.setStatus("mandatory")


class _ESWTelnetSessionActive_Type(Integer32):
    """Custom type eSWTelnetSessionActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_ESWTelnetSessionActive_Type.__name__ = "Integer32"
_ESWTelnetSessionActive_Object = MibScalar
eSWTelnetSessionActive = _ESWTelnetSessionActive_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 1, 1, 16),
    _ESWTelnetSessionActive_Type()
)
eSWTelnetSessionActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSWTelnetSessionActive.setStatus("mandatory")


class _ESWTelnetTimeOut_Type(Integer32):
    """Custom type eSWTelnetTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_ESWTelnetTimeOut_Type.__name__ = "Integer32"
_ESWTelnetTimeOut_Object = MibScalar
eSWTelnetTimeOut = _ESWTelnetTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 1, 1, 17),
    _ESWTelnetTimeOut_Type()
)
eSWTelnetTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eSWTelnetTimeOut.setStatus("mandatory")


class _ESWSTP_Type(Integer32):
    """Custom type eSWSTP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2),
          ("other", 1))
    )


_ESWSTP_Type.__name__ = "Integer32"
_ESWSTP_Object = MibScalar
eSWSTP = _ESWSTP_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 1, 1, 18),
    _ESWSTP_Type()
)
eSWSTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eSWSTP.setStatus("mandatory")


class _ESWUserInterfaceTimeOut_Type(Integer32):
    """Custom type eSWUserInterfaceTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_ESWUserInterfaceTimeOut_Type.__name__ = "Integer32"
_ESWUserInterfaceTimeOut_Object = MibScalar
eSWUserInterfaceTimeOut = _ESWUserInterfaceTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 1, 1, 19),
    _ESWUserInterfaceTimeOut_Type()
)
eSWUserInterfaceTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eSWUserInterfaceTimeOut.setStatus("mandatory")
_ESWBCastMcastThreshold_Type = Integer32
_ESWBCastMcastThreshold_Object = MibScalar
eSWBCastMcastThreshold = _ESWBCastMcastThreshold_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 1, 1, 20),
    _ESWBCastMcastThreshold_Type()
)
eSWBCastMcastThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eSWBCastMcastThreshold.setStatus("mandatory")
_ESWBCastMcastDuration_Type = Integer32
_ESWBCastMcastDuration_Object = MibScalar
eSWBCastMcastDuration = _ESWBCastMcastDuration_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 1, 1, 21),
    _ESWBCastMcastDuration_Type()
)
eSWBCastMcastDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eSWBCastMcastDuration.setStatus("mandatory")


class _ESWCfgFileErrStatus_Type(OctetString):
    """Custom type eSWCfgFileErrStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_ESWCfgFileErrStatus_Type.__name__ = "OctetString"
_ESWCfgFileErrStatus_Object = MibScalar
eSWCfgFileErrStatus = _ESWCfgFileErrStatus_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 1, 1, 22),
    _ESWCfgFileErrStatus_Type()
)
eSWCfgFileErrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSWCfgFileErrStatus.setStatus("mandatory")
_ESWAgentHW_ObjectIdentity = ObjectIdentity
eSWAgentHW = _ESWAgentHW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 1, 2)
)
_ESWDRAMSize_Type = Integer32
_ESWDRAMSize_Object = MibScalar
eSWDRAMSize = _ESWDRAMSize_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 1, 2, 1),
    _ESWDRAMSize_Type()
)
eSWDRAMSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSWDRAMSize.setStatus("mandatory")
_ESWFlashRAMSize_Type = Integer32
_ESWFlashRAMSize_Object = MibScalar
eSWFlashRAMSize = _ESWFlashRAMSize_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 1, 2, 2),
    _ESWFlashRAMSize_Type()
)
eSWFlashRAMSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSWFlashRAMSize.setStatus("mandatory")
_ESWEEPROMSize_Type = Integer32
_ESWEEPROMSize_Object = MibScalar
eSWEEPROMSize = _ESWEEPROMSize_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 1, 2, 3),
    _ESWEEPROMSize_Type()
)
eSWEEPROMSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSWEEPROMSize.setStatus("mandatory")
_ESWAgentFW_ObjectIdentity = ObjectIdentity
eSWAgentFW = _ESWAgentFW_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 1, 3)
)
_ESWBasic_ObjectIdentity = ObjectIdentity
eSWBasic = _ESWBasic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2)
)


class _ESWType_Type(Integer32):
    """Custom type eSWType based on Integer32"""
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
        *(("intraCore8000", 5),
          ("intraCore9000", 6),
          ("intraStack", 3),
          ("intraSwitch", 4),
          ("other", 1),
          ("thunderBird", 2))
    )


_ESWType_Type.__name__ = "Integer32"
_ESWType_Object = MibScalar
eSWType = _ESWType_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 1),
    _ESWType_Type()
)
eSWType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSWType.setStatus("mandatory")


class _ESWBkpType_Type(Integer32):
    """Custom type eSWBkpType based on Integer32"""
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
        *(("intraCore8000", 7),
          ("intraCore9000", 8),
          ("intraStack", 3),
          ("intraSwitch6216M", 4),
          ("intraSwitch6224", 5),
          ("intraSwitch6224M", 6),
          ("no-Bkp", 2),
          ("other", 1))
    )


_ESWBkpType_Type.__name__ = "Integer32"
_ESWBkpType_Object = MibScalar
eSWBkpType = _ESWBkpType_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 2),
    _ESWBkpType_Type()
)
eSWBkpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSWBkpType.setStatus("mandatory")
_ESWGroupCapacity_Type = Integer32
_ESWGroupCapacity_Object = MibScalar
eSWGroupCapacity = _ESWGroupCapacity_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 3),
    _ESWGroupCapacity_Type()
)
eSWGroupCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSWGroupCapacity.setStatus("mandatory")
_ESWStackLastChange_Type = TimeTicks
_ESWStackLastChange_Object = MibScalar
eSWStackLastChange = _ESWStackLastChange_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 4),
    _ESWStackLastChange_Type()
)
eSWStackLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSWStackLastChange.setStatus("mandatory")
_ESWGroupInfoTable_Object = MibTable
eSWGroupInfoTable = _ESWGroupInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 5)
)
if mibBuilder.loadTexts:
    eSWGroupInfoTable.setStatus("mandatory")
_ESWGroupInfoEntry_Object = MibTableRow
eSWGroupInfoEntry = _ESWGroupInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 5, 1)
)
eSWGroupInfoEntry.setIndexNames(
    (0, "ASANTE-SWITCH-MIB", "eSWGrpIndex"),
)
if mibBuilder.loadTexts:
    eSWGroupInfoEntry.setStatus("mandatory")
_ESWGrpIndex_Type = Integer32
_ESWGrpIndex_Object = MibTableColumn
eSWGrpIndex = _ESWGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 5, 1, 1),
    _ESWGrpIndex_Type()
)
eSWGrpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSWGrpIndex.setStatus("mandatory")
_ESWGrpID_Type = MacAddress
_ESWGrpID_Object = MibTableColumn
eSWGrpID = _ESWGrpID_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 5, 1, 2),
    _ESWGrpID_Type()
)
eSWGrpID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSWGrpID.setStatus("mandatory")


class _ESWGrpState_Type(Integer32):
    """Custom type eSWGrpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2),
          ("other", 1))
    )


_ESWGrpState_Type.__name__ = "Integer32"
_ESWGrpState_Object = MibTableColumn
eSWGrpState = _ESWGrpState_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 5, 1, 3),
    _ESWGrpState_Type()
)
eSWGrpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eSWGrpState.setStatus("mandatory")
_ESWGrpNumofPorts_Type = Integer32
_ESWGrpNumofPorts_Object = MibTableColumn
eSWGrpNumofPorts = _ESWGrpNumofPorts_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 5, 1, 4),
    _ESWGrpNumofPorts_Type()
)
eSWGrpNumofPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSWGrpNumofPorts.setStatus("mandatory")


class _ESWGrpType_Type(Integer32):
    """Custom type eSWGrpType based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("empty", 2),
          ("enterprise6216M-TX16", 7),
          ("enterprise6224M-TX24", 8),
          ("intraCore-GIGA", 12),
          ("intraCore-RJ21", 11),
          ("intraCore-RJ45", 10),
          ("intraCore8000", 9),
          ("intraStack-Base", 4),
          ("intraStack-FX8", 5),
          ("intraStack-TX16", 6),
          ("intraSwitch", 3),
          ("other", 1))
    )


_ESWGrpType_Type.__name__ = "Integer32"
_ESWGrpType_Object = MibTableColumn
eSWGrpType = _ESWGrpType_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 5, 1, 5),
    _ESWGrpType_Type()
)
eSWGrpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSWGrpType.setStatus("mandatory")
_ESWGrpDescrption_Type = DisplayString
_ESWGrpDescrption_Object = MibTableColumn
eSWGrpDescrption = _ESWGrpDescrption_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 5, 1, 6),
    _ESWGrpDescrption_Type()
)
eSWGrpDescrption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSWGrpDescrption.setStatus("mandatory")


class _ESWGrpLED_Type(OctetString):
    """Custom type eSWGrpLED based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )


_ESWGrpLED_Type.__name__ = "OctetString"
_ESWGrpLED_Object = MibTableColumn
eSWGrpLED = _ESWGrpLED_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 5, 1, 7),
    _ESWGrpLED_Type()
)
eSWGrpLED.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSWGrpLED.setStatus("mandatory")


class _ESWGrpFanStatus_Type(Integer32):
    """Custom type eSWGrpFanStatus based on Integer32"""
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
        *(("fail", 4),
          ("fan-1-2-bad", 7),
          ("fan-1-bad", 5),
          ("fan-2-bad", 6),
          ("no-fan", 2),
          ("normal", 3),
          ("other", 1))
    )


_ESWGrpFanStatus_Type.__name__ = "Integer32"
_ESWGrpFanStatus_Object = MibTableColumn
eSWGrpFanStatus = _ESWGrpFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 5, 1, 8),
    _ESWGrpFanStatus_Type()
)
eSWGrpFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSWGrpFanStatus.setStatus("mandatory")
_ESWGrpNumofExpPorts_Type = Integer32
_ESWGrpNumofExpPorts_Object = MibTableColumn
eSWGrpNumofExpPorts = _ESWGrpNumofExpPorts_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 5, 1, 9),
    _ESWGrpNumofExpPorts_Type()
)
eSWGrpNumofExpPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSWGrpNumofExpPorts.setStatus("mandatory")
_ESWGrpLastChange_Type = TimeTicks
_ESWGrpLastChange_Object = MibTableColumn
eSWGrpLastChange = _ESWGrpLastChange_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 5, 1, 10),
    _ESWGrpLastChange_Type()
)
eSWGrpLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSWGrpLastChange.setStatus("mandatory")


class _ESWGrpReset_Type(Integer32):
    """Custom type eSWGrpReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noReset", 2),
          ("other", 1),
          ("reset", 3))
    )


_ESWGrpReset_Type.__name__ = "Integer32"
_ESWGrpReset_Object = MibTableColumn
eSWGrpReset = _ESWGrpReset_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 5, 1, 11),
    _ESWGrpReset_Type()
)
eSWGrpReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSWGrpReset.setStatus("mandatory")
_ESWPortInfoTable_Object = MibTable
eSWPortInfoTable = _ESWPortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 6)
)
if mibBuilder.loadTexts:
    eSWPortInfoTable.setStatus("mandatory")
_ESWPortInfoEntry_Object = MibTableRow
eSWPortInfoEntry = _ESWPortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 6, 1)
)
eSWPortInfoEntry.setIndexNames(
    (0, "ASANTE-SWITCH-MIB", "eSWPortGrpIndex"),
    (0, "ASANTE-SWITCH-MIB", "eSWPortIndex"),
)
if mibBuilder.loadTexts:
    eSWPortInfoEntry.setStatus("mandatory")
_ESWPortGrpIndex_Type = Integer32
_ESWPortGrpIndex_Object = MibTableColumn
eSWPortGrpIndex = _ESWPortGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 6, 1, 1),
    _ESWPortGrpIndex_Type()
)
eSWPortGrpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSWPortGrpIndex.setStatus("mandatory")
_ESWPortIndex_Type = Integer32
_ESWPortIndex_Object = MibTableColumn
eSWPortIndex = _ESWPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 6, 1, 2),
    _ESWPortIndex_Type()
)
eSWPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSWPortIndex.setStatus("mandatory")


class _ESWPortType_Type(Integer32):
    """Custom type eSWPortType based on Integer32"""
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
        *(("foil", 7),
          ("mii-Empty", 2),
          ("mii-FL", 3),
          ("mii-FX", 5),
          ("mii-RJ45", 4),
          ("other", 1),
          ("rj45", 6))
    )


_ESWPortType_Type.__name__ = "Integer32"
_ESWPortType_Object = MibTableColumn
eSWPortType = _ESWPortType_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 6, 1, 3),
    _ESWPortType_Type()
)
eSWPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSWPortType.setStatus("mandatory")


class _ESWPortAutoNegAbility_Type(Integer32):
    """Custom type eSWPortAutoNegAbility based on Integer32"""
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
          ("with", 2),
          ("without", 3))
    )


_ESWPortAutoNegAbility_Type.__name__ = "Integer32"
_ESWPortAutoNegAbility_Object = MibTableColumn
eSWPortAutoNegAbility = _ESWPortAutoNegAbility_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 6, 1, 4),
    _ESWPortAutoNegAbility_Type()
)
eSWPortAutoNegAbility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSWPortAutoNegAbility.setStatus("mandatory")


class _ESWPortLink_Type(Integer32):
    """Custom type eSWPortLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 3),
          ("other", 1),
          ("up", 2))
    )


_ESWPortLink_Type.__name__ = "Integer32"
_ESWPortLink_Object = MibTableColumn
eSWPortLink = _ESWPortLink_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 6, 1, 5),
    _ESWPortLink_Type()
)
eSWPortLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSWPortLink.setStatus("mandatory")


class _ESWPortSpeed_Type(Integer32):
    """Custom type eSWPortSpeed based on Integer32"""
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
        *(("g1-Gbps", 4),
          ("m10-Mbps", 2),
          ("m100-Mbps", 3),
          ("other", 1))
    )


_ESWPortSpeed_Type.__name__ = "Integer32"
_ESWPortSpeed_Object = MibTableColumn
eSWPortSpeed = _ESWPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 6, 1, 6),
    _ESWPortSpeed_Type()
)
eSWPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSWPortSpeed.setStatus("mandatory")


class _ESWPortDuplex_Type(Integer32):
    """Custom type eSWPortDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full-Duplex", 3),
          ("half-Duplex", 2),
          ("other", 1))
    )


_ESWPortDuplex_Type.__name__ = "Integer32"
_ESWPortDuplex_Object = MibTableColumn
eSWPortDuplex = _ESWPortDuplex_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 6, 1, 7),
    _ESWPortDuplex_Type()
)
eSWPortDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSWPortDuplex.setStatus("mandatory")
_ESWGpPtInfoTable_Object = MibTable
eSWGpPtInfoTable = _ESWGpPtInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 7)
)
if mibBuilder.loadTexts:
    eSWGpPtInfoTable.setStatus("mandatory")
_ESWGpPtInfoEntry_Object = MibTableRow
eSWGpPtInfoEntry = _ESWGpPtInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 7, 1)
)
eSWGpPtInfoEntry.setIndexNames(
    (0, "ASANTE-SWITCH-MIB", "eSWGpPtInfoIndex"),
)
if mibBuilder.loadTexts:
    eSWGpPtInfoEntry.setStatus("mandatory")
_ESWGpPtInfoIndex_Type = Integer32
_ESWGpPtInfoIndex_Object = MibTableColumn
eSWGpPtInfoIndex = _ESWGpPtInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 7, 1, 1),
    _ESWGpPtInfoIndex_Type()
)
eSWGpPtInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSWGpPtInfoIndex.setStatus("mandatory")


class _ESWGpPtInfoType_Type(OctetString):
    """Custom type eSWGpPtInfoType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_ESWGpPtInfoType_Type.__name__ = "OctetString"
_ESWGpPtInfoType_Object = MibTableColumn
eSWGpPtInfoType = _ESWGpPtInfoType_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 7, 1, 2),
    _ESWGpPtInfoType_Type()
)
eSWGpPtInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSWGpPtInfoType.setStatus("mandatory")


class _ESWGpPtInfoAutoNegAbility_Type(OctetString):
    """Custom type eSWGpPtInfoAutoNegAbility based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_ESWGpPtInfoAutoNegAbility_Type.__name__ = "OctetString"
_ESWGpPtInfoAutoNegAbility_Object = MibTableColumn
eSWGpPtInfoAutoNegAbility = _ESWGpPtInfoAutoNegAbility_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 7, 1, 3),
    _ESWGpPtInfoAutoNegAbility_Type()
)
eSWGpPtInfoAutoNegAbility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSWGpPtInfoAutoNegAbility.setStatus("mandatory")


class _ESWGpPtInfoLink_Type(OctetString):
    """Custom type eSWGpPtInfoLink based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_ESWGpPtInfoLink_Type.__name__ = "OctetString"
_ESWGpPtInfoLink_Object = MibTableColumn
eSWGpPtInfoLink = _ESWGpPtInfoLink_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 7, 1, 4),
    _ESWGpPtInfoLink_Type()
)
eSWGpPtInfoLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSWGpPtInfoLink.setStatus("mandatory")


class _ESWGpPtInfoSpeed_Type(OctetString):
    """Custom type eSWGpPtInfoSpeed based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_ESWGpPtInfoSpeed_Type.__name__ = "OctetString"
_ESWGpPtInfoSpeed_Object = MibTableColumn
eSWGpPtInfoSpeed = _ESWGpPtInfoSpeed_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 7, 1, 5),
    _ESWGpPtInfoSpeed_Type()
)
eSWGpPtInfoSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSWGpPtInfoSpeed.setStatus("mandatory")


class _ESWGpPtInfoDuplex_Type(OctetString):
    """Custom type eSWGpPtInfoDuplex based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_ESWGpPtInfoDuplex_Type.__name__ = "OctetString"
_ESWGpPtInfoDuplex_Object = MibTableColumn
eSWGpPtInfoDuplex = _ESWGpPtInfoDuplex_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 7, 1, 6),
    _ESWGpPtInfoDuplex_Type()
)
eSWGpPtInfoDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSWGpPtInfoDuplex.setStatus("mandatory")
_ESWPtMacInfoTable_Object = MibTable
eSWPtMacInfoTable = _ESWPtMacInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 8)
)
if mibBuilder.loadTexts:
    eSWPtMacInfoTable.setStatus("mandatory")
_ESWPtMacInfoEntry_Object = MibTableRow
eSWPtMacInfoEntry = _ESWPtMacInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 8, 1)
)
eSWPtMacInfoEntry.setIndexNames(
    (0, "ASANTE-SWITCH-MIB", "eSWPtMacPort"),
    (0, "ASANTE-SWITCH-MIB", "eSWPtMacMACADDR"),
)
if mibBuilder.loadTexts:
    eSWPtMacInfoEntry.setStatus("mandatory")
_ESWPtMacPort_Type = Integer32
_ESWPtMacPort_Object = MibTableColumn
eSWPtMacPort = _ESWPtMacPort_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 8, 1, 1),
    _ESWPtMacPort_Type()
)
eSWPtMacPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSWPtMacPort.setStatus("mandatory")
_ESWPtMacMACADDR_Type = MacAddress
_ESWPtMacMACADDR_Object = MibTableColumn
eSWPtMacMACADDR = _ESWPtMacMACADDR_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 8, 1, 2),
    _ESWPtMacMACADDR_Type()
)
eSWPtMacMACADDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSWPtMacMACADDR.setStatus("mandatory")
_ESWVlanInfo_ObjectIdentity = ObjectIdentity
eSWVlanInfo = _ESWVlanInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 9)
)
_ESWVlanVersion_Type = Integer32
_ESWVlanVersion_Object = MibScalar
eSWVlanVersion = _ESWVlanVersion_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 9, 1),
    _ESWVlanVersion_Type()
)
eSWVlanVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSWVlanVersion.setStatus("mandatory")
_ESWVlanMaxCapacity_Type = Integer32
_ESWVlanMaxCapacity_Object = MibScalar
eSWVlanMaxCapacity = _ESWVlanMaxCapacity_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 9, 2),
    _ESWVlanMaxCapacity_Type()
)
eSWVlanMaxCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSWVlanMaxCapacity.setStatus("mandatory")
_ESWVlanTypesSupported_Type = Integer32
_ESWVlanTypesSupported_Object = MibScalar
eSWVlanTypesSupported = _ESWVlanTypesSupported_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 9, 3),
    _ESWVlanTypesSupported_Type()
)
eSWVlanTypesSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSWVlanTypesSupported.setStatus("mandatory")
_ESWVlanTable_Object = MibTable
eSWVlanTable = _ESWVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 9, 4)
)
if mibBuilder.loadTexts:
    eSWVlanTable.setStatus("mandatory")
_ESWVlanEntry_Object = MibTableRow
eSWVlanEntry = _ESWVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 9, 4, 1)
)
eSWVlanEntry.setIndexNames(
    (0, "ASANTE-SWITCH-MIB", "eSWVLANIndex"),
)
if mibBuilder.loadTexts:
    eSWVlanEntry.setStatus("mandatory")
_ESWVLANIndex_Type = Integer32
_ESWVLANIndex_Object = MibTableColumn
eSWVLANIndex = _ESWVLANIndex_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 9, 4, 1, 1),
    _ESWVLANIndex_Type()
)
eSWVLANIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSWVLANIndex.setStatus("mandatory")


class _ESWVlanName_Type(DisplayString):
    """Custom type eSWVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ESWVlanName_Type.__name__ = "DisplayString"
_ESWVlanName_Object = MibTableColumn
eSWVlanName = _ESWVlanName_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 9, 4, 1, 2),
    _ESWVlanName_Type()
)
eSWVlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eSWVlanName.setStatus("mandatory")
_ESWVlanID_Type = Integer32
_ESWVlanID_Object = MibTableColumn
eSWVlanID = _ESWVlanID_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 9, 4, 1, 3),
    _ESWVlanID_Type()
)
eSWVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eSWVlanID.setStatus("mandatory")
_ESWVlanMemberSet_Type = OctetString
_ESWVlanMemberSet_Object = MibTableColumn
eSWVlanMemberSet = _ESWVlanMemberSet_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 9, 4, 1, 4),
    _ESWVlanMemberSet_Type()
)
eSWVlanMemberSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSWVlanMemberSet.setStatus("mandatory")


class _ESWVlanMgmAccess_Type(Integer32):
    """Custom type eSWVlanMgmAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_ESWVlanMgmAccess_Type.__name__ = "Integer32"
_ESWVlanMgmAccess_Object = MibTableColumn
eSWVlanMgmAccess = _ESWVlanMgmAccess_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 9, 4, 1, 5),
    _ESWVlanMgmAccess_Type()
)
eSWVlanMgmAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eSWVlanMgmAccess.setStatus("mandatory")
_ESWTrunkBundleCapacity_Type = Integer32
_ESWTrunkBundleCapacity_Object = MibScalar
eSWTrunkBundleCapacity = _ESWTrunkBundleCapacity_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 10),
    _ESWTrunkBundleCapacity_Type()
)
eSWTrunkBundleCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSWTrunkBundleCapacity.setStatus("mandatory")
_ESWTrunkBundleTable_Object = MibTable
eSWTrunkBundleTable = _ESWTrunkBundleTable_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 11)
)
if mibBuilder.loadTexts:
    eSWTrunkBundleTable.setStatus("mandatory")
_ESWTrunkBundleEntry_Object = MibTableRow
eSWTrunkBundleEntry = _ESWTrunkBundleEntry_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 11, 1)
)
eSWTrunkBundleEntry.setIndexNames(
    (0, "ASANTE-SWITCH-MIB", "eSWTrunkBundleIndex"),
)
if mibBuilder.loadTexts:
    eSWTrunkBundleEntry.setStatus("mandatory")
_ESWTrunkBundleIndex_Type = Integer32
_ESWTrunkBundleIndex_Object = MibTableColumn
eSWTrunkBundleIndex = _ESWTrunkBundleIndex_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 11, 1, 1),
    _ESWTrunkBundleIndex_Type()
)
eSWTrunkBundleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSWTrunkBundleIndex.setStatus("mandatory")
_ESWTrunkBundlePortA_Type = Integer32
_ESWTrunkBundlePortA_Object = MibTableColumn
eSWTrunkBundlePortA = _ESWTrunkBundlePortA_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 11, 1, 2),
    _ESWTrunkBundlePortA_Type()
)
eSWTrunkBundlePortA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSWTrunkBundlePortA.setStatus("mandatory")
_ESWTrunkBundlePortB_Type = Integer32
_ESWTrunkBundlePortB_Object = MibTableColumn
eSWTrunkBundlePortB = _ESWTrunkBundlePortB_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 11, 1, 3),
    _ESWTrunkBundlePortB_Type()
)
eSWTrunkBundlePortB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSWTrunkBundlePortB.setStatus("mandatory")


class _ESWTrunkBundleState_Type(Integer32):
    """Custom type eSWTrunkBundleState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2),
          ("other", 1))
    )


_ESWTrunkBundleState_Type.__name__ = "Integer32"
_ESWTrunkBundleState_Object = MibTableColumn
eSWTrunkBundleState = _ESWTrunkBundleState_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 11, 1, 4),
    _ESWTrunkBundleState_Type()
)
eSWTrunkBundleState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eSWTrunkBundleState.setStatus("mandatory")
_ESWNetSecurityInfo_ObjectIdentity = ObjectIdentity
eSWNetSecurityInfo = _ESWNetSecurityInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 13)
)
_ESWNetworkSecurityVersion_Type = Integer32
_ESWNetworkSecurityVersion_Object = MibScalar
eSWNetworkSecurityVersion = _ESWNetworkSecurityVersion_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 13, 1),
    _ESWNetworkSecurityVersion_Type()
)
eSWNetworkSecurityVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSWNetworkSecurityVersion.setStatus("mandatory")
_ESWNetworkSecurityMAXLevels_Type = Integer32
_ESWNetworkSecurityMAXLevels_Object = MibScalar
eSWNetworkSecurityMAXLevels = _ESWNetworkSecurityMAXLevels_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 13, 2),
    _ESWNetworkSecurityMAXLevels_Type()
)
eSWNetworkSecurityMAXLevels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSWNetworkSecurityMAXLevels.setStatus("mandatory")
_ESWSecurityTypesSupported_Type = Integer32
_ESWSecurityTypesSupported_Object = MibScalar
eSWSecurityTypesSupported = _ESWSecurityTypesSupported_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 13, 3),
    _ESWSecurityTypesSupported_Type()
)
eSWSecurityTypesSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSWSecurityTypesSupported.setStatus("mandatory")
_ESWSecConfigTable_Object = MibTable
eSWSecConfigTable = _ESWSecConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 13, 4)
)
if mibBuilder.loadTexts:
    eSWSecConfigTable.setStatus("mandatory")
_ESWSecConfigEntry_Object = MibTableRow
eSWSecConfigEntry = _ESWSecConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 13, 4, 1)
)
eSWSecConfigEntry.setIndexNames(
    (0, "ASANTE-SWITCH-MIB", "eSWSecPortIndex"),
)
if mibBuilder.loadTexts:
    eSWSecConfigEntry.setStatus("mandatory")
_ESWSecPortIndex_Type = Integer32
_ESWSecPortIndex_Object = MibTableColumn
eSWSecPortIndex = _ESWSecPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 13, 4, 1, 1),
    _ESWSecPortIndex_Type()
)
eSWSecPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSWSecPortIndex.setStatus("mandatory")


class _ESWSecurityLevel_Type(Integer32):
    """Custom type eSWSecurityLevel based on Integer32"""
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
        *(("knownMACAddressForwarding", 2),
          ("knownMACAddressForwardingWithIntruderLock", 4),
          ("newNodeDetection", 1),
          ("normalPort", 5),
          ("other", 6),
          ("restrictedKnownMACAddressForwarding", 3))
    )


_ESWSecurityLevel_Type.__name__ = "Integer32"
_ESWSecurityLevel_Object = MibTableColumn
eSWSecurityLevel = _ESWSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 13, 4, 1, 2),
    _ESWSecurityLevel_Type()
)
eSWSecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eSWSecurityLevel.setStatus("mandatory")
_ESWSecMonitorPort_Type = Integer32
_ESWSecMonitorPort_Object = MibScalar
eSWSecMonitorPort = _ESWSecMonitorPort_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 13, 5),
    _ESWSecMonitorPort_Type()
)
eSWSecMonitorPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eSWSecMonitorPort.setStatus("mandatory")


class _ESWSecurityTrapEnable_Type(Integer32):
    """Custom type eSWSecurityTrapEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("other", 3))
    )


_ESWSecurityTrapEnable_Type.__name__ = "Integer32"
_ESWSecurityTrapEnable_Object = MibScalar
eSWSecurityTrapEnable = _ESWSecurityTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 13, 6),
    _ESWSecurityTrapEnable_Type()
)
eSWSecurityTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eSWSecurityTrapEnable.setStatus("mandatory")
_ESWSecIncSetConfigTable_Object = MibTable
eSWSecIncSetConfigTable = _ESWSecIncSetConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 13, 7)
)
if mibBuilder.loadTexts:
    eSWSecIncSetConfigTable.setStatus("mandatory")
_ESWSecIncSetConfigEntry_Object = MibTableRow
eSWSecIncSetConfigEntry = _ESWSecIncSetConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 13, 7, 1)
)
eSWSecIncSetConfigEntry.setIndexNames(
    (0, "ASANTE-SWITCH-MIB", "eSWIncSetPort"),
    (0, "ASANTE-SWITCH-MIB", "eSWIncSetMACAddr"),
)
if mibBuilder.loadTexts:
    eSWSecIncSetConfigEntry.setStatus("mandatory")
_ESWIncSetPort_Type = Integer32
_ESWIncSetPort_Object = MibTableColumn
eSWIncSetPort = _ESWIncSetPort_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 13, 7, 1, 1),
    _ESWIncSetPort_Type()
)
eSWIncSetPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSWIncSetPort.setStatus("mandatory")
_ESWIncSetMACAddr_Type = MacAddress
_ESWIncSetMACAddr_Object = MibTableColumn
eSWIncSetMACAddr = _ESWIncSetMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 13, 7, 1, 2),
    _ESWIncSetMACAddr_Type()
)
eSWIncSetMACAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSWIncSetMACAddr.setStatus("mandatory")


class _ESWIncSetMACStatus_Type(Integer32):
    """Custom type eSWIncSetMACStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_ESWIncSetMACStatus_Type.__name__ = "Integer32"
_ESWIncSetMACStatus_Object = MibTableColumn
eSWIncSetMACStatus = _ESWIncSetMACStatus_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 13, 7, 1, 3),
    _ESWIncSetMACStatus_Type()
)
eSWIncSetMACStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eSWIncSetMACStatus.setStatus("mandatory")
_ESWSecIntMACAddrTable_Object = MibTable
eSWSecIntMACAddrTable = _ESWSecIntMACAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 13, 8)
)
if mibBuilder.loadTexts:
    eSWSecIntMACAddrTable.setStatus("mandatory")
_ESWSecIntMACAddrEntry_Object = MibTableRow
eSWSecIntMACAddrEntry = _ESWSecIntMACAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 13, 8, 1)
)
eSWSecIntMACAddrEntry.setIndexNames(
    (0, "ASANTE-SWITCH-MIB", "eSWIntMACAddrPort"),
    (0, "ASANTE-SWITCH-MIB", "eSWIntMACAddr"),
)
if mibBuilder.loadTexts:
    eSWSecIntMACAddrEntry.setStatus("mandatory")
_ESWIntMACAddrPort_Type = Integer32
_ESWIntMACAddrPort_Object = MibTableColumn
eSWIntMACAddrPort = _ESWIntMACAddrPort_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 13, 8, 1, 1),
    _ESWIntMACAddrPort_Type()
)
eSWIntMACAddrPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSWIntMACAddrPort.setStatus("mandatory")
_ESWIntMACAddr_Type = MacAddress
_ESWIntMACAddr_Object = MibTableColumn
eSWIntMACAddr = _ESWIntMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 13, 8, 1, 2),
    _ESWIntMACAddr_Type()
)
eSWIntMACAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSWIntMACAddr.setStatus("mandatory")
_ESWFilteringInfo_ObjectIdentity = ObjectIdentity
eSWFilteringInfo = _ESWFilteringInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 14)
)
_ESWFilteringTypesSupported_Type = Integer32
_ESWFilteringTypesSupported_Object = MibScalar
eSWFilteringTypesSupported = _ESWFilteringTypesSupported_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 14, 1),
    _ESWFilteringTypesSupported_Type()
)
eSWFilteringTypesSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSWFilteringTypesSupported.setStatus("mandatory")
_ESWFiltMACVLANBasedConfigTable_Object = MibTable
eSWFiltMACVLANBasedConfigTable = _ESWFiltMACVLANBasedConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 14, 2)
)
if mibBuilder.loadTexts:
    eSWFiltMACVLANBasedConfigTable.setStatus("mandatory")
_ESWFiltMACVLANBasedConfigEntry_Object = MibTableRow
eSWFiltMACVLANBasedConfigEntry = _ESWFiltMACVLANBasedConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 14, 2, 1)
)
eSWFiltMACVLANBasedConfigEntry.setIndexNames(
    (0, "ASANTE-SWITCH-MIB", "eSWVLANIndex"),
    (0, "ASANTE-SWITCH-MIB", "eSWFiltMACAddr"),
)
if mibBuilder.loadTexts:
    eSWFiltMACVLANBasedConfigEntry.setStatus("mandatory")
_ESWVIDIndex_Type = Integer32
_ESWVIDIndex_Object = MibTableColumn
eSWVIDIndex = _ESWVIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 14, 2, 1, 1),
    _ESWVIDIndex_Type()
)
eSWVIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSWVIDIndex.setStatus("mandatory")
_ESWFiltMACAddr_Type = MacAddress
_ESWFiltMACAddr_Object = MibTableColumn
eSWFiltMACAddr = _ESWFiltMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 14, 2, 1, 2),
    _ESWFiltMACAddr_Type()
)
eSWFiltMACAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSWFiltMACAddr.setStatus("mandatory")


class _ESWFiltMACSts_Type(Integer32):
    """Custom type eSWFiltMACSts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_ESWFiltMACSts_Type.__name__ = "Integer32"
_ESWFiltMACSts_Object = MibTableColumn
eSWFiltMACSts = _ESWFiltMACSts_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 14, 2, 1, 3),
    _ESWFiltMACSts_Type()
)
eSWFiltMACSts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eSWFiltMACSts.setStatus("mandatory")
_ESWFiltMACPortBasedConfigTable_Object = MibTable
eSWFiltMACPortBasedConfigTable = _ESWFiltMACPortBasedConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 14, 3)
)
if mibBuilder.loadTexts:
    eSWFiltMACPortBasedConfigTable.setStatus("mandatory")
_ESWFiltMACPortBasedConfigEntry_Object = MibTableRow
eSWFiltMACPortBasedConfigEntry = _ESWFiltMACPortBasedConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 14, 3, 1)
)
eSWFiltMACPortBasedConfigEntry.setIndexNames(
    (0, "ASANTE-SWITCH-MIB", "eSWFiltPortIndex"),
    (0, "ASANTE-SWITCH-MIB", "eSWFiltPMACAddr"),
)
if mibBuilder.loadTexts:
    eSWFiltMACPortBasedConfigEntry.setStatus("mandatory")
_ESWFiltPortIndex_Type = Integer32
_ESWFiltPortIndex_Object = MibTableColumn
eSWFiltPortIndex = _ESWFiltPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 14, 3, 1, 1),
    _ESWFiltPortIndex_Type()
)
eSWFiltPortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eSWFiltPortIndex.setStatus("mandatory")
_ESWFiltPMACAddr_Type = MacAddress
_ESWFiltPMACAddr_Object = MibTableColumn
eSWFiltPMACAddr = _ESWFiltPMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 14, 3, 1, 2),
    _ESWFiltPMACAddr_Type()
)
eSWFiltPMACAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eSWFiltPMACAddr.setStatus("mandatory")


class _ESWFiltPMACStatus_Type(Integer32):
    """Custom type eSWFiltPMACStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_ESWFiltPMACStatus_Type.__name__ = "Integer32"
_ESWFiltPMACStatus_Object = MibTableColumn
eSWFiltPMACStatus = _ESWFiltPMACStatus_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 14, 3, 1, 3),
    _ESWFiltPMACStatus_Type()
)
eSWFiltPMACStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eSWFiltPMACStatus.setStatus("mandatory")
_ESWFiltProtVLANBasedCFGTable_Object = MibTable
eSWFiltProtVLANBasedCFGTable = _ESWFiltProtVLANBasedCFGTable_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 14, 4)
)
if mibBuilder.loadTexts:
    eSWFiltProtVLANBasedCFGTable.setStatus("mandatory")
_ESWFiltProtVLANBasedCFGEntry_Object = MibTableRow
eSWFiltProtVLANBasedCFGEntry = _ESWFiltProtVLANBasedCFGEntry_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 14, 4, 1)
)
eSWFiltProtVLANBasedCFGEntry.setIndexNames(
    (0, "ASANTE-SWITCH-MIB", "eSWVLANIndex"),
)
if mibBuilder.loadTexts:
    eSWFiltProtVLANBasedCFGEntry.setStatus("mandatory")
_ESWFiltProtocolVID_Type = Integer32
_ESWFiltProtocolVID_Object = MibTableColumn
eSWFiltProtocolVID = _ESWFiltProtocolVID_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 14, 4, 1, 1),
    _ESWFiltProtocolVID_Type()
)
eSWFiltProtocolVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eSWFiltProtocolVID.setStatus("mandatory")


class _ESWFiltVLANProtocolType_Type(OctetString):
    """Custom type eSWFiltVLANProtocolType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_ESWFiltVLANProtocolType_Type.__name__ = "OctetString"
_ESWFiltVLANProtocolType_Object = MibTableColumn
eSWFiltVLANProtocolType = _ESWFiltVLANProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 14, 4, 1, 2),
    _ESWFiltVLANProtocolType_Type()
)
eSWFiltVLANProtocolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eSWFiltVLANProtocolType.setStatus("mandatory")
_ESWFiltProtPortBasedCFGTable_Object = MibTable
eSWFiltProtPortBasedCFGTable = _ESWFiltProtPortBasedCFGTable_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 14, 5)
)
if mibBuilder.loadTexts:
    eSWFiltProtPortBasedCFGTable.setStatus("mandatory")
_ESWFiltProtPortBasedCFGEntry_Object = MibTableRow
eSWFiltProtPortBasedCFGEntry = _ESWFiltProtPortBasedCFGEntry_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 14, 5, 1)
)
eSWFiltProtPortBasedCFGEntry.setIndexNames(
    (0, "ASANTE-SWITCH-MIB", "eSWPortIndex"),
)
if mibBuilder.loadTexts:
    eSWFiltProtPortBasedCFGEntry.setStatus("mandatory")
_ESWFiltProtPort_Type = Integer32
_ESWFiltProtPort_Object = MibTableColumn
eSWFiltProtPort = _ESWFiltProtPort_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 14, 5, 1, 1),
    _ESWFiltProtPort_Type()
)
eSWFiltProtPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eSWFiltProtPort.setStatus("mandatory")


class _ESWFiltProtcolType_Type(OctetString):
    """Custom type eSWFiltProtcolType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_ESWFiltProtcolType_Type.__name__ = "OctetString"
_ESWFiltProtcolType_Object = MibTableColumn
eSWFiltProtcolType = _ESWFiltProtcolType_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 2, 14, 5, 1, 2),
    _ESWFiltProtcolType_Type()
)
eSWFiltProtcolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eSWFiltProtcolType.setStatus("mandatory")
_ESWCtrl_ObjectIdentity = ObjectIdentity
eSWCtrl = _ESWCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 3)
)
_ESWPortCtrlTable_Object = MibTable
eSWPortCtrlTable = _ESWPortCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 3, 1)
)
if mibBuilder.loadTexts:
    eSWPortCtrlTable.setStatus("mandatory")
_ESWPortCtrlEntry_Object = MibTableRow
eSWPortCtrlEntry = _ESWPortCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 3, 1, 1)
)
eSWPortCtrlEntry.setIndexNames(
    (0, "ASANTE-SWITCH-MIB", "eSWGrpPtCtrlIndex"),
    (0, "ASANTE-SWITCH-MIB", "eSWPortCtrlIndex"),
)
if mibBuilder.loadTexts:
    eSWPortCtrlEntry.setStatus("mandatory")
_ESWGrpPtCtrlIndex_Type = Integer32
_ESWGrpPtCtrlIndex_Object = MibTableColumn
eSWGrpPtCtrlIndex = _ESWGrpPtCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 3, 1, 1, 1),
    _ESWGrpPtCtrlIndex_Type()
)
eSWGrpPtCtrlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSWGrpPtCtrlIndex.setStatus("mandatory")
_ESWPortCtrlIndex_Type = Integer32
_ESWPortCtrlIndex_Object = MibTableColumn
eSWPortCtrlIndex = _ESWPortCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 3, 1, 1, 2),
    _ESWPortCtrlIndex_Type()
)
eSWPortCtrlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSWPortCtrlIndex.setStatus("mandatory")


class _ESWPortCtrlState_Type(Integer32):
    """Custom type eSWPortCtrlState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2),
          ("other", 1))
    )


_ESWPortCtrlState_Type.__name__ = "Integer32"
_ESWPortCtrlState_Object = MibTableColumn
eSWPortCtrlState = _ESWPortCtrlState_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 3, 1, 1, 3),
    _ESWPortCtrlState_Type()
)
eSWPortCtrlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eSWPortCtrlState.setStatus("mandatory")


class _ESWPortCtrlBcastFilter_Type(Integer32):
    """Custom type eSWPortCtrlBcastFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2),
          ("other", 1))
    )


_ESWPortCtrlBcastFilter_Type.__name__ = "Integer32"
_ESWPortCtrlBcastFilter_Object = MibTableColumn
eSWPortCtrlBcastFilter = _ESWPortCtrlBcastFilter_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 3, 1, 1, 4),
    _ESWPortCtrlBcastFilter_Type()
)
eSWPortCtrlBcastFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eSWPortCtrlBcastFilter.setStatus("mandatory")


class _ESWPortCtrlStNFw_Type(Integer32):
    """Custom type eSWPortCtrlStNFw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2),
          ("other", 1))
    )


_ESWPortCtrlStNFw_Type.__name__ = "Integer32"
_ESWPortCtrlStNFw_Object = MibTableColumn
eSWPortCtrlStNFw = _ESWPortCtrlStNFw_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 3, 1, 1, 5),
    _ESWPortCtrlStNFw_Type()
)
eSWPortCtrlStNFw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eSWPortCtrlStNFw.setStatus("mandatory")


class _ESWPortCtrlSTP_Type(Integer32):
    """Custom type eSWPortCtrlSTP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 2),
          ("other", 1))
    )


_ESWPortCtrlSTP_Type.__name__ = "Integer32"
_ESWPortCtrlSTP_Object = MibTableColumn
eSWPortCtrlSTP = _ESWPortCtrlSTP_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 3, 1, 1, 6),
    _ESWPortCtrlSTP_Type()
)
eSWPortCtrlSTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSWPortCtrlSTP.setStatus("mandatory")
_ESWPortCtrlVlanID_Type = Integer32
_ESWPortCtrlVlanID_Object = MibTableColumn
eSWPortCtrlVlanID = _ESWPortCtrlVlanID_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 3, 1, 1, 7),
    _ESWPortCtrlVlanID_Type()
)
eSWPortCtrlVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eSWPortCtrlVlanID.setStatus("mandatory")


class _ESWPortCtrlVlanTagging_Type(Integer32):
    """Custom type eSWPortCtrlVlanTagging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 1),
          ("enable8021Q", 2))
    )


_ESWPortCtrlVlanTagging_Type.__name__ = "Integer32"
_ESWPortCtrlVlanTagging_Object = MibTableColumn
eSWPortCtrlVlanTagging = _ESWPortCtrlVlanTagging_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 3, 1, 1, 8),
    _ESWPortCtrlVlanTagging_Type()
)
eSWPortCtrlVlanTagging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eSWPortCtrlVlanTagging.setStatus("mandatory")


class _ESWPortCtrlVlanGroups_Type(OctetString):
    """Custom type eSWPortCtrlVlanGroups based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_ESWPortCtrlVlanGroups_Type.__name__ = "OctetString"
_ESWPortCtrlVlanGroups_Object = MibTableColumn
eSWPortCtrlVlanGroups = _ESWPortCtrlVlanGroups_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 3, 1, 1, 9),
    _ESWPortCtrlVlanGroups_Type()
)
eSWPortCtrlVlanGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eSWPortCtrlVlanGroups.setStatus("mandatory")
_ESWPortCtrlTrunkBundleIndex_Type = Integer32
_ESWPortCtrlTrunkBundleIndex_Object = MibTableColumn
eSWPortCtrlTrunkBundleIndex = _ESWPortCtrlTrunkBundleIndex_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 3, 1, 1, 10),
    _ESWPortCtrlTrunkBundleIndex_Type()
)
eSWPortCtrlTrunkBundleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSWPortCtrlTrunkBundleIndex.setStatus("mandatory")


class _ESWPortCtrlGVRPEnable_Type(Integer32):
    """Custom type eSWPortCtrlGVRPEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_ESWPortCtrlGVRPEnable_Type.__name__ = "Integer32"
_ESWPortCtrlGVRPEnable_Object = MibTableColumn
eSWPortCtrlGVRPEnable = _ESWPortCtrlGVRPEnable_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 3, 1, 1, 11),
    _ESWPortCtrlGVRPEnable_Type()
)
eSWPortCtrlGVRPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eSWPortCtrlGVRPEnable.setStatus("mandatory")


class _ESWPortCtrlSecurityLevel_Type(Integer32):
    """Custom type eSWPortCtrlSecurityLevel based on Integer32"""
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
        *(("knownMACAddressForwarding", 2),
          ("knownMACAddressForwardingWithIntruderLock", 4),
          ("newNodeDetection", 1),
          ("normalPort", 5),
          ("other", 6),
          ("restrictedKnownMACAddressForwarding", 3))
    )


_ESWPortCtrlSecurityLevel_Type.__name__ = "Integer32"
_ESWPortCtrlSecurityLevel_Object = MibTableColumn
eSWPortCtrlSecurityLevel = _ESWPortCtrlSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 3, 1, 1, 12),
    _ESWPortCtrlSecurityLevel_Type()
)
eSWPortCtrlSecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eSWPortCtrlSecurityLevel.setStatus("mandatory")


class _ESWPortProtocolFilter_Type(OctetString):
    """Custom type eSWPortProtocolFilter based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_ESWPortProtocolFilter_Type.__name__ = "OctetString"
_ESWPortProtocolFilter_Object = MibTableColumn
eSWPortProtocolFilter = _ESWPortProtocolFilter_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 3, 1, 1, 13),
    _ESWPortProtocolFilter_Type()
)
eSWPortProtocolFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eSWPortProtocolFilter.setStatus("mandatory")
_ESWGpPtCtrlTable_Object = MibTable
eSWGpPtCtrlTable = _ESWGpPtCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 3, 2)
)
if mibBuilder.loadTexts:
    eSWGpPtCtrlTable.setStatus("mandatory")
_ESWGpPtCtrlEntry_Object = MibTableRow
eSWGpPtCtrlEntry = _ESWGpPtCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 3, 2, 1)
)
eSWGpPtCtrlEntry.setIndexNames(
    (0, "ASANTE-SWITCH-MIB", "eSWGpPtCtrlIndex"),
)
if mibBuilder.loadTexts:
    eSWGpPtCtrlEntry.setStatus("mandatory")
_ESWGpPtCtrlIndex_Type = Integer32
_ESWGpPtCtrlIndex_Object = MibTableColumn
eSWGpPtCtrlIndex = _ESWGpPtCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 3, 2, 1, 1),
    _ESWGpPtCtrlIndex_Type()
)
eSWGpPtCtrlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSWGpPtCtrlIndex.setStatus("mandatory")


class _ESWGpPtCtrlState_Type(OctetString):
    """Custom type eSWGpPtCtrlState based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_ESWGpPtCtrlState_Type.__name__ = "OctetString"
_ESWGpPtCtrlState_Object = MibTableColumn
eSWGpPtCtrlState = _ESWGpPtCtrlState_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 3, 2, 1, 2),
    _ESWGpPtCtrlState_Type()
)
eSWGpPtCtrlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eSWGpPtCtrlState.setStatus("mandatory")


class _ESWGpPtCtrlBcastFilter_Type(OctetString):
    """Custom type eSWGpPtCtrlBcastFilter based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_ESWGpPtCtrlBcastFilter_Type.__name__ = "OctetString"
_ESWGpPtCtrlBcastFilter_Object = MibTableColumn
eSWGpPtCtrlBcastFilter = _ESWGpPtCtrlBcastFilter_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 3, 2, 1, 3),
    _ESWGpPtCtrlBcastFilter_Type()
)
eSWGpPtCtrlBcastFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eSWGpPtCtrlBcastFilter.setStatus("mandatory")


class _ESWGpPtCtrlStNFw_Type(OctetString):
    """Custom type eSWGpPtCtrlStNFw based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_ESWGpPtCtrlStNFw_Type.__name__ = "OctetString"
_ESWGpPtCtrlStNFw_Object = MibTableColumn
eSWGpPtCtrlStNFw = _ESWGpPtCtrlStNFw_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 3, 2, 1, 4),
    _ESWGpPtCtrlStNFw_Type()
)
eSWGpPtCtrlStNFw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSWGpPtCtrlStNFw.setStatus("mandatory")


class _ESWGpPtCtrlSTP_Type(OctetString):
    """Custom type eSWGpPtCtrlSTP based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_ESWGpPtCtrlSTP_Type.__name__ = "OctetString"
_ESWGpPtCtrlSTP_Object = MibTableColumn
eSWGpPtCtrlSTP = _ESWGpPtCtrlSTP_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 3, 2, 1, 5),
    _ESWGpPtCtrlSTP_Type()
)
eSWGpPtCtrlSTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSWGpPtCtrlSTP.setStatus("mandatory")


class _ESWGpPtCtrlSecurityLevel_Type(OctetString):
    """Custom type eSWGpPtCtrlSecurityLevel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_ESWGpPtCtrlSecurityLevel_Type.__name__ = "OctetString"
_ESWGpPtCtrlSecurityLevel_Object = MibTableColumn
eSWGpPtCtrlSecurityLevel = _ESWGpPtCtrlSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 3, 2, 1, 6),
    _ESWGpPtCtrlSecurityLevel_Type()
)
eSWGpPtCtrlSecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eSWGpPtCtrlSecurityLevel.setStatus("mandatory")


class _ESWGpPtProtocolFilter_Type(OctetString):
    """Custom type eSWGpPtProtocolFilter based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_ESWGpPtProtocolFilter_Type.__name__ = "OctetString"
_ESWGpPtProtocolFilter_Object = MibTableColumn
eSWGpPtProtocolFilter = _ESWGpPtProtocolFilter_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 3, 2, 1, 7),
    _ESWGpPtProtocolFilter_Type()
)
eSWGpPtProtocolFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eSWGpPtProtocolFilter.setStatus("mandatory")
_ESWAutoPortCtrlTable_Object = MibTable
eSWAutoPortCtrlTable = _ESWAutoPortCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 3, 3)
)
if mibBuilder.loadTexts:
    eSWAutoPortCtrlTable.setStatus("mandatory")
_ESWAutoPortCtrlEntry_Object = MibTableRow
eSWAutoPortCtrlEntry = _ESWAutoPortCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 3, 3, 1)
)
eSWAutoPortCtrlEntry.setIndexNames(
    (0, "ASANTE-SWITCH-MIB", "eSWAutoNegGrpIndex"),
    (0, "ASANTE-SWITCH-MIB", "eSWAutoNegPortIndex"),
)
if mibBuilder.loadTexts:
    eSWAutoPortCtrlEntry.setStatus("mandatory")
_ESWAutoNegGrpIndex_Type = Integer32
_ESWAutoNegGrpIndex_Object = MibTableColumn
eSWAutoNegGrpIndex = _ESWAutoNegGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 3, 3, 1, 1),
    _ESWAutoNegGrpIndex_Type()
)
eSWAutoNegGrpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSWAutoNegGrpIndex.setStatus("mandatory")
_ESWAutoNegPortIndex_Type = Integer32
_ESWAutoNegPortIndex_Object = MibTableColumn
eSWAutoNegPortIndex = _ESWAutoNegPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 3, 3, 1, 2),
    _ESWAutoNegPortIndex_Type()
)
eSWAutoNegPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSWAutoNegPortIndex.setStatus("mandatory")


class _ESWAutoNegAdminState_Type(Integer32):
    """Custom type eSWAutoNegAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enabled", 2),
          ("other", 1))
    )


_ESWAutoNegAdminState_Type.__name__ = "Integer32"
_ESWAutoNegAdminState_Object = MibTableColumn
eSWAutoNegAdminState = _ESWAutoNegAdminState_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 3, 3, 1, 3),
    _ESWAutoNegAdminState_Type()
)
eSWAutoNegAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eSWAutoNegAdminState.setStatus("mandatory")


class _ESWAutoNegRemoteAble_Type(Integer32):
    """Custom type eSWAutoNegRemoteAble based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("able", 2),
          ("not-able", 3),
          ("other", 1))
    )


_ESWAutoNegRemoteAble_Type.__name__ = "Integer32"
_ESWAutoNegRemoteAble_Object = MibTableColumn
eSWAutoNegRemoteAble = _ESWAutoNegRemoteAble_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 3, 3, 1, 4),
    _ESWAutoNegRemoteAble_Type()
)
eSWAutoNegRemoteAble.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSWAutoNegRemoteAble.setStatus("mandatory")


class _ESWAutoNegAutoConfig_Type(Integer32):
    """Custom type eSWAutoNegAutoConfig based on Integer32"""
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
        *(("complete", 3),
          ("configuring", 2),
          ("disable", 4),
          ("other", 1),
          ("parallel-detect-fail", 5),
          ("remote-fault", 6))
    )


_ESWAutoNegAutoConfig_Type.__name__ = "Integer32"
_ESWAutoNegAutoConfig_Object = MibTableColumn
eSWAutoNegAutoConfig = _ESWAutoNegAutoConfig_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 3, 3, 1, 5),
    _ESWAutoNegAutoConfig_Type()
)
eSWAutoNegAutoConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSWAutoNegAutoConfig.setStatus("mandatory")


class _ESWAutoNegLocalAbility_Type(OctetString):
    """Custom type eSWAutoNegLocalAbility based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_ESWAutoNegLocalAbility_Type.__name__ = "OctetString"
_ESWAutoNegLocalAbility_Object = MibTableColumn
eSWAutoNegLocalAbility = _ESWAutoNegLocalAbility_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 3, 3, 1, 6),
    _ESWAutoNegLocalAbility_Type()
)
eSWAutoNegLocalAbility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSWAutoNegLocalAbility.setStatus("mandatory")


class _ESWAutoNegAdvertisedAbility_Type(OctetString):
    """Custom type eSWAutoNegAdvertisedAbility based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_ESWAutoNegAdvertisedAbility_Type.__name__ = "OctetString"
_ESWAutoNegAdvertisedAbility_Object = MibTableColumn
eSWAutoNegAdvertisedAbility = _ESWAutoNegAdvertisedAbility_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 3, 3, 1, 7),
    _ESWAutoNegAdvertisedAbility_Type()
)
eSWAutoNegAdvertisedAbility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eSWAutoNegAdvertisedAbility.setStatus("mandatory")


class _ESWAutoNegReceivedAbility_Type(OctetString):
    """Custom type eSWAutoNegReceivedAbility based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_ESWAutoNegReceivedAbility_Type.__name__ = "OctetString"
_ESWAutoNegReceivedAbility_Object = MibTableColumn
eSWAutoNegReceivedAbility = _ESWAutoNegReceivedAbility_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 3, 3, 1, 8),
    _ESWAutoNegReceivedAbility_Type()
)
eSWAutoNegReceivedAbility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSWAutoNegReceivedAbility.setStatus("mandatory")


class _ESWAutoNegRestartAutoConfig_Type(Integer32):
    """Custom type eSWAutoNegRestartAutoConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noRestart", 3),
          ("other", 1),
          ("reStart", 2))
    )


_ESWAutoNegRestartAutoConfig_Type.__name__ = "Integer32"
_ESWAutoNegRestartAutoConfig_Object = MibTableColumn
eSWAutoNegRestartAutoConfig = _ESWAutoNegRestartAutoConfig_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 3, 3, 1, 9),
    _ESWAutoNegRestartAutoConfig_Type()
)
eSWAutoNegRestartAutoConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eSWAutoNegRestartAutoConfig.setStatus("mandatory")
_ESWMonitor_ObjectIdentity = ObjectIdentity
eSWMonitor = _ESWMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 4)
)
_ESWMonIPTable_Object = MibTable
eSWMonIPTable = _ESWMonIPTable_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 4, 1)
)
if mibBuilder.loadTexts:
    eSWMonIPTable.setStatus("mandatory")
_ESWMonIPEntry_Object = MibTableRow
eSWMonIPEntry = _ESWMonIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 4, 1, 1)
)
eSWMonIPEntry.setIndexNames(
    (0, "ASANTE-SWITCH-MIB", "eSWMonIP"),
)
if mibBuilder.loadTexts:
    eSWMonIPEntry.setStatus("mandatory")
_ESWMonIP_Type = IpAddress
_ESWMonIP_Object = MibTableColumn
eSWMonIP = _ESWMonIP_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 4, 1, 1, 1),
    _ESWMonIP_Type()
)
eSWMonIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSWMonIP.setStatus("mandatory")
_ESWMonMAC_Type = MacAddress
_ESWMonMAC_Object = MibTableColumn
eSWMonMAC = _ESWMonMAC_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 4, 1, 1, 2),
    _ESWMonMAC_Type()
)
eSWMonMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSWMonMAC.setStatus("mandatory")
_ESWMonVLANID_Type = Integer32
_ESWMonVLANID_Object = MibTableColumn
eSWMonVLANID = _ESWMonVLANID_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 4, 1, 1, 3),
    _ESWMonVLANID_Type()
)
eSWMonVLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSWMonVLANID.setStatus("mandatory")
_ESWMonGrp_Type = Integer32
_ESWMonGrp_Object = MibTableColumn
eSWMonGrp = _ESWMonGrp_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 4, 1, 1, 4),
    _ESWMonGrp_Type()
)
eSWMonGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSWMonGrp.setStatus("mandatory")
_ESWMonPort_Type = Integer32
_ESWMonPort_Object = MibTableColumn
eSWMonPort = _ESWMonPort_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 5, 1, 4, 1, 1, 5),
    _ESWMonPort_Type()
)
eSWMonPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSWMonPort.setStatus("mandatory")
_ProductId_ObjectIdentity = ObjectIdentity
productId = _ProductId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 298, 2)
)
_ConcProductId_ObjectIdentity = ObjectIdentity
concProductId = _ConcProductId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 298, 2, 2)
)
_Intraswitch_ObjectIdentity = ObjectIdentity
intraswitch = _Intraswitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 298, 2, 2, 11)
)
_Intrastack_ObjectIdentity = ObjectIdentity
intrastack = _Intrastack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 298, 2, 2, 12)
)
_Friendlyswitch_ObjectIdentity = ObjectIdentity
friendlyswitch = _Friendlyswitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 298, 2, 2, 13)
)
_IntraSwitch6216M_ObjectIdentity = ObjectIdentity
intraSwitch6216M = _IntraSwitch6216M_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 298, 2, 2, 16)
)
_IntraSwitch6224_ObjectIdentity = ObjectIdentity
intraSwitch6224 = _IntraSwitch6224_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 298, 2, 2, 17)
)
_IntraCore8000_ObjectIdentity = ObjectIdentity
intraCore8000 = _IntraCore8000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 298, 2, 2, 22)
)
_IntraCore9000_ObjectIdentity = ObjectIdentity
intraCore9000 = _IntraCore9000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 298, 2, 2, 23)
)

# Managed Objects groups


# Notification objects

eSWFanFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 298, 0, 3)
)
eSWFanFail.setObjects(
    ("ASANTE-SWITCH-MIB", "eSWGrpIndex")
)
if mibBuilder.loadTexts:
    eSWFanFail.setStatus(
        ""
    )

eSWExpPortConnectStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 298, 0, 4)
)
eSWExpPortConnectStateChange.setObjects(
      *(("ASANTE-SWITCH-MIB", "eSWGrpIndex"),
        ("ASANTE-SWITCH-MIB", "eSWPortIndex"))
)
if mibBuilder.loadTexts:
    eSWExpPortConnectStateChange.setStatus(
        ""
    )

eSWIPSpoofing = NotificationType(
    (1, 3, 6, 1, 4, 1, 298, 0, 5)
)
eSWIPSpoofing.setObjects(
      *(("ASANTE-SWITCH-MIB", "eSWMonIP"),
        ("ASANTE-SWITCH-MIB", "eSWMonMAC"),
        ("ASANTE-SWITCH-MIB", "eSWMonPort"),
        ("ASANTE-SWITCH-MIB", "eSWMonIP"),
        ("ASANTE-SWITCH-MIB", "eSWMonMAC"),
        ("ASANTE-SWITCH-MIB", "eSWMonPort"))
)
if mibBuilder.loadTexts:
    eSWIPSpoofing.setStatus(
        ""
    )

eSWStationMove = NotificationType(
    (1, 3, 6, 1, 4, 1, 298, 0, 6)
)
eSWStationMove.setObjects(
      *(("ASANTE-SWITCH-MIB", "eSWMonIP"),
        ("ASANTE-SWITCH-MIB", "eSWMonMAC"),
        ("ASANTE-SWITCH-MIB", "eSWMonPort"))
)
if mibBuilder.loadTexts:
    eSWStationMove.setStatus(
        ""
    )

eSWNewNodeDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 298, 0, 7)
)
eSWNewNodeDetected.setObjects(
      *(("ASANTE-SWITCH-MIB", "eSWMonPort"),
        ("ASANTE-SWITCH-MIB", "eSWMonMAC"),
        ("ASANTE-SWITCH-MIB", "eSWMonIP"))
)
if mibBuilder.loadTexts:
    eSWNewNodeDetected.setStatus(
        ""
    )

eSWIntruderDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 298, 0, 8)
)
eSWIntruderDetected.setObjects(
      *(("ASANTE-SWITCH-MIB", "eSWMonPort"),
        ("ASANTE-SWITCH-MIB", "eSWMonMAC"),
        ("ASANTE-SWITCH-MIB", "eSWMonIP"),
        ("ASANTE-SWITCH-MIB", "eSWSecurityLevel"))
)
if mibBuilder.loadTexts:
    eSWIntruderDetected.setStatus(
        ""
    )

eSWIntruderPortDisable = NotificationType(
    (1, 3, 6, 1, 4, 1, 298, 0, 9)
)
eSWIntruderPortDisable.setObjects(
      *(("ASANTE-SWITCH-MIB", "eSWMonPort"),
        ("ASANTE-SWITCH-MIB", "eSWMonMAC"),
        ("ASANTE-SWITCH-MIB", "eSWMonIP"))
)
if mibBuilder.loadTexts:
    eSWIntruderPortDisable.setStatus(
        ""
    )

eSWEnhIPSpoofing = NotificationType(
    (1, 3, 6, 1, 4, 1, 298, 0, 10)
)
eSWEnhIPSpoofing.setObjects(
      *(("ASANTE-SWITCH-MIB", "eSWMonIP"),
        ("ASANTE-SWITCH-MIB", "eSWMonMAC"),
        ("ASANTE-SWITCH-MIB", "eSWMonVLANID"),
        ("ASANTE-SWITCH-MIB", "eSWMonGrp"),
        ("ASANTE-SWITCH-MIB", "eSWMonPort"),
        ("ASANTE-SWITCH-MIB", "eSWMonMAC"),
        ("ASANTE-SWITCH-MIB", "eSWMonVLANID"),
        ("ASANTE-SWITCH-MIB", "eSWMonGrp"),
        ("ASANTE-SWITCH-MIB", "eSWMonPort"))
)
if mibBuilder.loadTexts:
    eSWEnhIPSpoofing.setStatus(
        ""
    )

eSWEnhStationMove = NotificationType(
    (1, 3, 6, 1, 4, 1, 298, 0, 11)
)
eSWEnhStationMove.setObjects(
      *(("ASANTE-SWITCH-MIB", "eSWMonIP"),
        ("ASANTE-SWITCH-MIB", "eSWMonMAC"),
        ("ASANTE-SWITCH-MIB", "eSWMonVLANID"),
        ("ASANTE-SWITCH-MIB", "eSWMonGrp"),
        ("ASANTE-SWITCH-MIB", "eSWMonPort"),
        ("ASANTE-SWITCH-MIB", "eSWMonGrp"),
        ("ASANTE-SWITCH-MIB", "eSWMonPort"))
)
if mibBuilder.loadTexts:
    eSWEnhStationMove.setStatus(
        ""
    )

eSWEnhNewNodeDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 298, 0, 12)
)
eSWEnhNewNodeDetected.setObjects(
      *(("ASANTE-SWITCH-MIB", "eSWMonGrp"),
        ("ASANTE-SWITCH-MIB", "eSWMonPort"),
        ("ASANTE-SWITCH-MIB", "eSWMonMAC"),
        ("ASANTE-SWITCH-MIB", "eSWMonVLANID"),
        ("ASANTE-SWITCH-MIB", "eSWMonIP"))
)
if mibBuilder.loadTexts:
    eSWEnhNewNodeDetected.setStatus(
        ""
    )

eSWEnhIntruderDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 298, 0, 13)
)
eSWEnhIntruderDetected.setObjects(
      *(("ASANTE-SWITCH-MIB", "eSWMonGrp"),
        ("ASANTE-SWITCH-MIB", "eSWMonPort"),
        ("ASANTE-SWITCH-MIB", "eSWMonMAC"),
        ("ASANTE-SWITCH-MIB", "eSWMonVLANID"),
        ("ASANTE-SWITCH-MIB", "eSWMonIP"))
)
if mibBuilder.loadTexts:
    eSWEnhIntruderDetected.setStatus(
        ""
    )

eSWEnhIntruderPortDisable = NotificationType(
    (1, 3, 6, 1, 4, 1, 298, 0, 14)
)
eSWEnhIntruderPortDisable.setObjects(
      *(("ASANTE-SWITCH-MIB", "eSWMonGrp"),
        ("ASANTE-SWITCH-MIB", "eSWMonPort"),
        ("ASANTE-SWITCH-MIB", "eSWMonMAC"),
        ("ASANTE-SWITCH-MIB", "eSWMonVLANID"),
        ("ASANTE-SWITCH-MIB", "eSWMonIP"))
)
if mibBuilder.loadTexts:
    eSWEnhIntruderPortDisable.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASANTE-SWITCH-MIB",
    **{"MacAddress": MacAddress,
       "asante": asante,
       "eSWFanFail": eSWFanFail,
       "eSWExpPortConnectStateChange": eSWExpPortConnectStateChange,
       "eSWIPSpoofing": eSWIPSpoofing,
       "eSWStationMove": eSWStationMove,
       "eSWNewNodeDetected": eSWNewNodeDetected,
       "eSWIntruderDetected": eSWIntruderDetected,
       "eSWIntruderPortDisable": eSWIntruderPortDisable,
       "eSWEnhIPSpoofing": eSWEnhIPSpoofing,
       "eSWEnhStationMove": eSWEnhStationMove,
       "eSWEnhNewNodeDetected": eSWEnhNewNodeDetected,
       "eSWEnhIntruderDetected": eSWEnhIntruderDetected,
       "eSWEnhIntruderPortDisable": eSWEnhIntruderPortDisable,
       "products": products,
       "snmpAgent": snmpAgent,
       "agentSw": agentSw,
       "agentRunTimeImageMajorVer": agentRunTimeImageMajorVer,
       "agentRunTimeImageMinorVer": agentRunTimeImageMinorVer,
       "agentImageLoadMode": agentImageLoadMode,
       "agentRemoteBootInfo": agentRemoteBootInfo,
       "agentRemoteBootProtocol": agentRemoteBootProtocol,
       "agentRemoteBootFile": agentRemoteBootFile,
       "agentOutBandDialString": agentOutBandDialString,
       "agentOutBandBaudRate": agentOutBandBaudRate,
       "agentReset": agentReset,
       "agentFw": agentFw,
       "agentFwMajorVer": agentFwMajorVer,
       "agentFwMinorVer": agentFwMinorVer,
       "agentHw": agentHw,
       "agentHwReVer": agentHwReVer,
       "agentHwVer": agentHwVer,
       "agentNetProtoStkCapMap": agentNetProtoStkCapMap,
       "agentNetProtocol": agentNetProtocol,
       "ipagentProtocol": ipagentProtocol,
       "ipagentIpAddr": ipagentIpAddr,
       "ipagentIpNetMask": ipagentIpNetMask,
       "ipagentDefaultGateway": ipagentDefaultGateway,
       "ipagentBootServerAddr": ipagentBootServerAddr,
       "ipagentUnAuthIP": ipagentUnAuthIP,
       "ipagentUnAuthComm": ipagentUnAuthComm,
       "ipagentTrapRcvrTable": ipagentTrapRcvrTable,
       "ipagentTrapRcvrEntry": ipagentTrapRcvrEntry,
       "ipagentTrapRcvrIpAddr": ipagentTrapRcvrIpAddr,
       "ipagentTrapRcvrStatus": ipagentTrapRcvrStatus,
       "ipagentTrapRcvrComm": ipagentTrapRcvrComm,
       "switch": switch,
       "eAsntSwitch": eAsntSwitch,
       "eSWAgent": eSWAgent,
       "eSWAgentSW": eSWAgentSW,
       "eSWUpDownloadAction": eSWUpDownloadAction,
       "eSWUpDownloadStatus": eSWUpDownloadStatus,
       "eSWRemoteDownloadFile": eSWRemoteDownloadFile,
       "eSWRemoteConfigServer": eSWRemoteConfigServer,
       "eSWRemoteConfigFileName": eSWRemoteConfigFileName,
       "eSWConfigRetryCounter": eSWConfigRetryCounter,
       "eSWRemoteImageServer": eSWRemoteImageServer,
       "eSWRemoteImageFileName": eSWRemoteImageFileName,
       "eSWImageRetryCounter": eSWImageRetryCounter,
       "eSWActiveImageBank": eSWActiveImageBank,
       "eSWRemoteDownloadImageBank": eSWRemoteDownloadImageBank,
       "eSWResetWaitTime": eSWResetWaitTime,
       "eSWResetLeftTime": eSWResetLeftTime,
       "eSWBankImageInfoTable": eSWBankImageInfoTable,
       "eSWBankImageInfoEntry": eSWBankImageInfoEntry,
       "eSWBankIndex": eSWBankIndex,
       "eSWMajorVer": eSWMajorVer,
       "eSWMinorVer": eSWMinorVer,
       "eSWDateTime": eSWDateTime,
       "eSWTelnetSessions": eSWTelnetSessions,
       "eSWTelnetSessionActive": eSWTelnetSessionActive,
       "eSWTelnetTimeOut": eSWTelnetTimeOut,
       "eSWSTP": eSWSTP,
       "eSWUserInterfaceTimeOut": eSWUserInterfaceTimeOut,
       "eSWBCastMcastThreshold": eSWBCastMcastThreshold,
       "eSWBCastMcastDuration": eSWBCastMcastDuration,
       "eSWCfgFileErrStatus": eSWCfgFileErrStatus,
       "eSWAgentHW": eSWAgentHW,
       "eSWDRAMSize": eSWDRAMSize,
       "eSWFlashRAMSize": eSWFlashRAMSize,
       "eSWEEPROMSize": eSWEEPROMSize,
       "eSWAgentFW": eSWAgentFW,
       "eSWBasic": eSWBasic,
       "eSWType": eSWType,
       "eSWBkpType": eSWBkpType,
       "eSWGroupCapacity": eSWGroupCapacity,
       "eSWStackLastChange": eSWStackLastChange,
       "eSWGroupInfoTable": eSWGroupInfoTable,
       "eSWGroupInfoEntry": eSWGroupInfoEntry,
       "eSWGrpIndex": eSWGrpIndex,
       "eSWGrpID": eSWGrpID,
       "eSWGrpState": eSWGrpState,
       "eSWGrpNumofPorts": eSWGrpNumofPorts,
       "eSWGrpType": eSWGrpType,
       "eSWGrpDescrption": eSWGrpDescrption,
       "eSWGrpLED": eSWGrpLED,
       "eSWGrpFanStatus": eSWGrpFanStatus,
       "eSWGrpNumofExpPorts": eSWGrpNumofExpPorts,
       "eSWGrpLastChange": eSWGrpLastChange,
       "eSWGrpReset": eSWGrpReset,
       "eSWPortInfoTable": eSWPortInfoTable,
       "eSWPortInfoEntry": eSWPortInfoEntry,
       "eSWPortGrpIndex": eSWPortGrpIndex,
       "eSWPortIndex": eSWPortIndex,
       "eSWPortType": eSWPortType,
       "eSWPortAutoNegAbility": eSWPortAutoNegAbility,
       "eSWPortLink": eSWPortLink,
       "eSWPortSpeed": eSWPortSpeed,
       "eSWPortDuplex": eSWPortDuplex,
       "eSWGpPtInfoTable": eSWGpPtInfoTable,
       "eSWGpPtInfoEntry": eSWGpPtInfoEntry,
       "eSWGpPtInfoIndex": eSWGpPtInfoIndex,
       "eSWGpPtInfoType": eSWGpPtInfoType,
       "eSWGpPtInfoAutoNegAbility": eSWGpPtInfoAutoNegAbility,
       "eSWGpPtInfoLink": eSWGpPtInfoLink,
       "eSWGpPtInfoSpeed": eSWGpPtInfoSpeed,
       "eSWGpPtInfoDuplex": eSWGpPtInfoDuplex,
       "eSWPtMacInfoTable": eSWPtMacInfoTable,
       "eSWPtMacInfoEntry": eSWPtMacInfoEntry,
       "eSWPtMacPort": eSWPtMacPort,
       "eSWPtMacMACADDR": eSWPtMacMACADDR,
       "eSWVlanInfo": eSWVlanInfo,
       "eSWVlanVersion": eSWVlanVersion,
       "eSWVlanMaxCapacity": eSWVlanMaxCapacity,
       "eSWVlanTypesSupported": eSWVlanTypesSupported,
       "eSWVlanTable": eSWVlanTable,
       "eSWVlanEntry": eSWVlanEntry,
       "eSWVLANIndex": eSWVLANIndex,
       "eSWVlanName": eSWVlanName,
       "eSWVlanID": eSWVlanID,
       "eSWVlanMemberSet": eSWVlanMemberSet,
       "eSWVlanMgmAccess": eSWVlanMgmAccess,
       "eSWTrunkBundleCapacity": eSWTrunkBundleCapacity,
       "eSWTrunkBundleTable": eSWTrunkBundleTable,
       "eSWTrunkBundleEntry": eSWTrunkBundleEntry,
       "eSWTrunkBundleIndex": eSWTrunkBundleIndex,
       "eSWTrunkBundlePortA": eSWTrunkBundlePortA,
       "eSWTrunkBundlePortB": eSWTrunkBundlePortB,
       "eSWTrunkBundleState": eSWTrunkBundleState,
       "eSWNetSecurityInfo": eSWNetSecurityInfo,
       "eSWNetworkSecurityVersion": eSWNetworkSecurityVersion,
       "eSWNetworkSecurityMAXLevels": eSWNetworkSecurityMAXLevels,
       "eSWSecurityTypesSupported": eSWSecurityTypesSupported,
       "eSWSecConfigTable": eSWSecConfigTable,
       "eSWSecConfigEntry": eSWSecConfigEntry,
       "eSWSecPortIndex": eSWSecPortIndex,
       "eSWSecurityLevel": eSWSecurityLevel,
       "eSWSecMonitorPort": eSWSecMonitorPort,
       "eSWSecurityTrapEnable": eSWSecurityTrapEnable,
       "eSWSecIncSetConfigTable": eSWSecIncSetConfigTable,
       "eSWSecIncSetConfigEntry": eSWSecIncSetConfigEntry,
       "eSWIncSetPort": eSWIncSetPort,
       "eSWIncSetMACAddr": eSWIncSetMACAddr,
       "eSWIncSetMACStatus": eSWIncSetMACStatus,
       "eSWSecIntMACAddrTable": eSWSecIntMACAddrTable,
       "eSWSecIntMACAddrEntry": eSWSecIntMACAddrEntry,
       "eSWIntMACAddrPort": eSWIntMACAddrPort,
       "eSWIntMACAddr": eSWIntMACAddr,
       "eSWFilteringInfo": eSWFilteringInfo,
       "eSWFilteringTypesSupported": eSWFilteringTypesSupported,
       "eSWFiltMACVLANBasedConfigTable": eSWFiltMACVLANBasedConfigTable,
       "eSWFiltMACVLANBasedConfigEntry": eSWFiltMACVLANBasedConfigEntry,
       "eSWVIDIndex": eSWVIDIndex,
       "eSWFiltMACAddr": eSWFiltMACAddr,
       "eSWFiltMACSts": eSWFiltMACSts,
       "eSWFiltMACPortBasedConfigTable": eSWFiltMACPortBasedConfigTable,
       "eSWFiltMACPortBasedConfigEntry": eSWFiltMACPortBasedConfigEntry,
       "eSWFiltPortIndex": eSWFiltPortIndex,
       "eSWFiltPMACAddr": eSWFiltPMACAddr,
       "eSWFiltPMACStatus": eSWFiltPMACStatus,
       "eSWFiltProtVLANBasedCFGTable": eSWFiltProtVLANBasedCFGTable,
       "eSWFiltProtVLANBasedCFGEntry": eSWFiltProtVLANBasedCFGEntry,
       "eSWFiltProtocolVID": eSWFiltProtocolVID,
       "eSWFiltVLANProtocolType": eSWFiltVLANProtocolType,
       "eSWFiltProtPortBasedCFGTable": eSWFiltProtPortBasedCFGTable,
       "eSWFiltProtPortBasedCFGEntry": eSWFiltProtPortBasedCFGEntry,
       "eSWFiltProtPort": eSWFiltProtPort,
       "eSWFiltProtcolType": eSWFiltProtcolType,
       "eSWCtrl": eSWCtrl,
       "eSWPortCtrlTable": eSWPortCtrlTable,
       "eSWPortCtrlEntry": eSWPortCtrlEntry,
       "eSWGrpPtCtrlIndex": eSWGrpPtCtrlIndex,
       "eSWPortCtrlIndex": eSWPortCtrlIndex,
       "eSWPortCtrlState": eSWPortCtrlState,
       "eSWPortCtrlBcastFilter": eSWPortCtrlBcastFilter,
       "eSWPortCtrlStNFw": eSWPortCtrlStNFw,
       "eSWPortCtrlSTP": eSWPortCtrlSTP,
       "eSWPortCtrlVlanID": eSWPortCtrlVlanID,
       "eSWPortCtrlVlanTagging": eSWPortCtrlVlanTagging,
       "eSWPortCtrlVlanGroups": eSWPortCtrlVlanGroups,
       "eSWPortCtrlTrunkBundleIndex": eSWPortCtrlTrunkBundleIndex,
       "eSWPortCtrlGVRPEnable": eSWPortCtrlGVRPEnable,
       "eSWPortCtrlSecurityLevel": eSWPortCtrlSecurityLevel,
       "eSWPortProtocolFilter": eSWPortProtocolFilter,
       "eSWGpPtCtrlTable": eSWGpPtCtrlTable,
       "eSWGpPtCtrlEntry": eSWGpPtCtrlEntry,
       "eSWGpPtCtrlIndex": eSWGpPtCtrlIndex,
       "eSWGpPtCtrlState": eSWGpPtCtrlState,
       "eSWGpPtCtrlBcastFilter": eSWGpPtCtrlBcastFilter,
       "eSWGpPtCtrlStNFw": eSWGpPtCtrlStNFw,
       "eSWGpPtCtrlSTP": eSWGpPtCtrlSTP,
       "eSWGpPtCtrlSecurityLevel": eSWGpPtCtrlSecurityLevel,
       "eSWGpPtProtocolFilter": eSWGpPtProtocolFilter,
       "eSWAutoPortCtrlTable": eSWAutoPortCtrlTable,
       "eSWAutoPortCtrlEntry": eSWAutoPortCtrlEntry,
       "eSWAutoNegGrpIndex": eSWAutoNegGrpIndex,
       "eSWAutoNegPortIndex": eSWAutoNegPortIndex,
       "eSWAutoNegAdminState": eSWAutoNegAdminState,
       "eSWAutoNegRemoteAble": eSWAutoNegRemoteAble,
       "eSWAutoNegAutoConfig": eSWAutoNegAutoConfig,
       "eSWAutoNegLocalAbility": eSWAutoNegLocalAbility,
       "eSWAutoNegAdvertisedAbility": eSWAutoNegAdvertisedAbility,
       "eSWAutoNegReceivedAbility": eSWAutoNegReceivedAbility,
       "eSWAutoNegRestartAutoConfig": eSWAutoNegRestartAutoConfig,
       "eSWMonitor": eSWMonitor,
       "eSWMonIPTable": eSWMonIPTable,
       "eSWMonIPEntry": eSWMonIPEntry,
       "eSWMonIP": eSWMonIP,
       "eSWMonMAC": eSWMonMAC,
       "eSWMonVLANID": eSWMonVLANID,
       "eSWMonGrp": eSWMonGrp,
       "eSWMonPort": eSWMonPort,
       "productId": productId,
       "concProductId": concProductId,
       "intraswitch": intraswitch,
       "intrastack": intrastack,
       "friendlyswitch": friendlyswitch,
       "intraSwitch6216M": intraSwitch6216M,
       "intraSwitch6224": intraSwitch6224,
       "intraCore8000": intraCore8000,
       "intraCore9000": intraCore9000}
)
