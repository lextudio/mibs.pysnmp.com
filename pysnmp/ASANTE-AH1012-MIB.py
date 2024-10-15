# SNMP MIB module (ASANTE-AH1012-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASANTE-AH1012-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:40:48 2024
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
 iso,
 private) = mibBuilder.importSymbols(
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
    "iso",
    "private")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""




class PhysAddress(OctetString):
    """Custom type PhysAddress based on OctetString"""



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


class _AgentRemoteBootFile_Type(OctetString):
    """Custom type agentRemoteBootFile based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AgentRemoteBootFile_Type.__name__ = "OctetString"
_AgentRemoteBootFile_Object = MibScalar
agentRemoteBootFile = _AgentRemoteBootFile_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 1, 1, 6),
    _AgentRemoteBootFile_Type()
)
agentRemoteBootFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRemoteBootFile.setStatus("mandatory")


class _AgentOutBandDialString_Type(OctetString):
    """Custom type agentOutBandDialString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AgentOutBandDialString_Type.__name__ = "OctetString"
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
              5)
        )
    )
    namedValues = NamedValues(
        *(("b1200", 2),
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
        ValueSizeConstraint(1, 4),
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
_IpagentUnAuthComm_Type = OctetString
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
    (0, "ASANTE-AH1012-MIB", "ipagentTrapRcvrIpAddr"),
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
_IpagentTrapRcvrComm_Type = OctetString
_IpagentTrapRcvrComm_Object = MibTableColumn
ipagentTrapRcvrComm = _IpagentTrapRcvrComm_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 1, 5, 2, 1, 3),
    _IpagentTrapRcvrComm_Type()
)
ipagentTrapRcvrComm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipagentTrapRcvrComm.setStatus("mandatory")
_AdaptCard_ObjectIdentity = ObjectIdentity
adaptCard = _AdaptCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 298, 1, 2)
)
_Concentrator_ObjectIdentity = ObjectIdentity
concentrator = _Concentrator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 298, 1, 3)
)
_ConcChassis_ObjectIdentity = ObjectIdentity
concChassis = _ConcChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 1)
)
_ConcBasicGrp_ObjectIdentity = ObjectIdentity
concBasicGrp = _ConcBasicGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 1, 1)
)


class _ConcChassisType_Type(Integer32):
    """Custom type concChassisType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aH1012", 2),
          ("other", 1))
    )


_ConcChassisType_Type.__name__ = "Integer32"
_ConcChassisType_Object = MibScalar
concChassisType = _ConcChassisType_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 1, 1, 1),
    _ConcChassisType_Type()
)
concChassisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concChassisType.setStatus("mandatory")


class _ConcChassisBkplType_Type(Integer32):
    """Custom type concChassisBkplType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no-backplane", 2),
          ("other", 1))
    )


_ConcChassisBkplType_Type.__name__ = "Integer32"
_ConcChassisBkplType_Object = MibScalar
concChassisBkplType = _ConcChassisBkplType_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 1, 1, 2),
    _ConcChassisBkplType_Type()
)
concChassisBkplType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concChassisBkplType.setStatus("mandatory")
_ConcChassisBkplRev_Type = Integer32
_ConcChassisBkplRev_Object = MibScalar
concChassisBkplRev = _ConcChassisBkplRev_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 1, 1, 3),
    _ConcChassisBkplRev_Type()
)
concChassisBkplRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concChassisBkplRev.setStatus("mandatory")
_ConcChassisPsTable_Object = MibTable
concChassisPsTable = _ConcChassisPsTable_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 1, 1, 4)
)
if mibBuilder.loadTexts:
    concChassisPsTable.setStatus("mandatory")
_ConcChassisPsEntry_Object = MibTableRow
concChassisPsEntry = _ConcChassisPsEntry_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 1, 1, 4, 1)
)
concChassisPsEntry.setIndexNames(
    (0, "ASANTE-AH1012-MIB", "concChassisPsIndex"),
)
if mibBuilder.loadTexts:
    concChassisPsEntry.setStatus("mandatory")
_ConcChassisPsIndex_Type = Integer32
_ConcChassisPsIndex_Object = MibTableColumn
concChassisPsIndex = _ConcChassisPsIndex_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 1, 1, 4, 1, 1),
    _ConcChassisPsIndex_Type()
)
concChassisPsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concChassisPsIndex.setStatus("mandatory")


class _ConcChassisPsModuleType_Type(Integer32):
    """Custom type concChassisPsModuleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("other", 1)
    )


_ConcChassisPsModuleType_Type.__name__ = "Integer32"
_ConcChassisPsModuleType_Object = MibTableColumn
concChassisPsModuleType = _ConcChassisPsModuleType_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 1, 1, 4, 1, 2),
    _ConcChassisPsModuleType_Type()
)
concChassisPsModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concChassisPsModuleType.setStatus("mandatory")


class _ConcChassisPsStatus_Type(Integer32):
    """Custom type concChassisPsStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bad", 3),
          ("good", 2),
          ("other", 1))
    )


_ConcChassisPsStatus_Type.__name__ = "Integer32"
_ConcChassisPsStatus_Object = MibTableColumn
concChassisPsStatus = _ConcChassisPsStatus_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 1, 1, 4, 1, 3),
    _ConcChassisPsStatus_Type()
)
concChassisPsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concChassisPsStatus.setStatus("mandatory")


class _ConcChassisFanStatus_Type(Integer32):
    """Custom type concChassisFanStatus based on Integer32"""
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
        *(("bad", 4),
          ("good", 3),
          ("no-fan", 2),
          ("other", 1))
    )


_ConcChassisFanStatus_Type.__name__ = "Integer32"
_ConcChassisFanStatus_Object = MibScalar
concChassisFanStatus = _ConcChassisFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 1, 1, 5),
    _ConcChassisFanStatus_Type()
)
concChassisFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concChassisFanStatus.setStatus("mandatory")
_ConcChassisGroupCapacity_Type = Integer32
_ConcChassisGroupCapacity_Object = MibScalar
concChassisGroupCapacity = _ConcChassisGroupCapacity_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 1, 1, 6),
    _ConcChassisGroupCapacity_Type()
)
concChassisGroupCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concChassisGroupCapacity.setStatus("mandatory")
_ConcChassisGroupMap_Type = OctetString
_ConcChassisGroupMap_Object = MibScalar
concChassisGroupMap = _ConcChassisGroupMap_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 1, 1, 7),
    _ConcChassisGroupMap_Type()
)
concChassisGroupMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concChassisGroupMap.setStatus("mandatory")
_ConcChassisGrpTable_Object = MibTable
concChassisGrpTable = _ConcChassisGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 1, 1, 8)
)
if mibBuilder.loadTexts:
    concChassisGrpTable.setStatus("mandatory")
_ConcChassisGrpEntry_Object = MibTableRow
concChassisGrpEntry = _ConcChassisGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 1, 1, 8, 1)
)
concChassisGrpEntry.setIndexNames(
    (0, "ASANTE-AH1012-MIB", "concChassisGrpIndex"),
)
if mibBuilder.loadTexts:
    concChassisGrpEntry.setStatus("mandatory")
_ConcChassisGrpIndex_Type = Integer32
_ConcChassisGrpIndex_Object = MibTableColumn
concChassisGrpIndex = _ConcChassisGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 1, 1, 8, 1, 1),
    _ConcChassisGrpIndex_Type()
)
concChassisGrpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concChassisGrpIndex.setStatus("mandatory")
_ConcChassisGrpNumberPort_Type = Integer32
_ConcChassisGrpNumberPort_Object = MibTableColumn
concChassisGrpNumberPort = _ConcChassisGrpNumberPort_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 1, 1, 8, 1, 2),
    _ConcChassisGrpNumberPort_Type()
)
concChassisGrpNumberPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concChassisGrpNumberPort.setStatus("mandatory")
_ConcChassisGrpType_Type = Integer32
_ConcChassisGrpType_Object = MibTableColumn
concChassisGrpType = _ConcChassisGrpType_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 1, 1, 8, 1, 3),
    _ConcChassisGrpType_Type()
)
concChassisGrpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concChassisGrpType.setStatus("mandatory")
_ConcChassisGrpDescr_Type = DisplayString
_ConcChassisGrpDescr_Object = MibTableColumn
concChassisGrpDescr = _ConcChassisGrpDescr_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 1, 1, 8, 1, 4),
    _ConcChassisGrpDescr_Type()
)
concChassisGrpDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concChassisGrpDescr.setStatus("mandatory")
_ConcChassisGrpHwRev_Type = Integer32
_ConcChassisGrpHwRev_Object = MibTableColumn
concChassisGrpHwRev = _ConcChassisGrpHwRev_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 1, 1, 8, 1, 5),
    _ConcChassisGrpHwRev_Type()
)
concChassisGrpHwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    concChassisGrpHwRev.setStatus("mandatory")
_ConcConfiguration_ObjectIdentity = ObjectIdentity
concConfiguration = _ConcConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 2)
)
_ESmartHubConfig_ObjectIdentity = ObjectIdentity
eSmartHubConfig = _ESmartHubConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 2, 1)
)
_ESmartHubId_Type = PhysAddress
_ESmartHubId_Object = MibScalar
eSmartHubId = _ESmartHubId_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 2, 1, 1),
    _ESmartHubId_Type()
)
eSmartHubId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSmartHubId.setStatus("mandatory")
_ESmartHubAssignedId_Type = Integer32
_ESmartHubAssignedId_Object = MibScalar
eSmartHubAssignedId = _ESmartHubAssignedId_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 2, 1, 2),
    _ESmartHubAssignedId_Type()
)
eSmartHubAssignedId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSmartHubAssignedId.setStatus("mandatory")


class _ESmartHubTerSwitch_Type(Integer32):
    """Custom type eSmartHubTerSwitch based on Integer32"""
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
          ("pc-modem", 3),
          ("terminal", 2))
    )


_ESmartHubTerSwitch_Type.__name__ = "Integer32"
_ESmartHubTerSwitch_Object = MibScalar
eSmartHubTerSwitch = _ESmartHubTerSwitch_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 2, 1, 3),
    _ESmartHubTerSwitch_Type()
)
eSmartHubTerSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSmartHubTerSwitch.setStatus("mandatory")
_ESmartHubHwLoadPatStatus_Type = Integer32
_ESmartHubHwLoadPatStatus_Object = MibScalar
eSmartHubHwLoadPatStatus = _ESmartHubHwLoadPatStatus_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 2, 1, 4),
    _ESmartHubHwLoadPatStatus_Type()
)
eSmartHubHwLoadPatStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eSmartHubHwLoadPatStatus.setStatus("mandatory")
_ESmartHubHwLoadPatCapacity_Type = OctetString
_ESmartHubHwLoadPatCapacity_Object = MibScalar
eSmartHubHwLoadPatCapacity = _ESmartHubHwLoadPatCapacity_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 2, 1, 5),
    _ESmartHubHwLoadPatCapacity_Type()
)
eSmartHubHwLoadPatCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSmartHubHwLoadPatCapacity.setStatus("mandatory")
_ESmartHubNodeAgeTimer_Type = Integer32
_ESmartHubNodeAgeTimer_Object = MibScalar
eSmartHubNodeAgeTimer = _ESmartHubNodeAgeTimer_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 2, 1, 6),
    _ESmartHubNodeAgeTimer_Type()
)
eSmartHubNodeAgeTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eSmartHubNodeAgeTimer.setStatus("mandatory")


class _ESmartHub3in1LnConStatus_Type(Integer32):
    """Custom type eSmartHub3in1LnConStatus based on Integer32"""
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
        *(("aUI", 3),
          ("other", 1),
          ("uTP", 2),
          ("uTP-and-AUI", 4))
    )


_ESmartHub3in1LnConStatus_Type.__name__ = "Integer32"
_ESmartHub3in1LnConStatus_Object = MibScalar
eSmartHub3in1LnConStatus = _ESmartHub3in1LnConStatus_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 2, 1, 7),
    _ESmartHub3in1LnConStatus_Type()
)
eSmartHub3in1LnConStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eSmartHub3in1LnConStatus.setStatus("mandatory")


class _ESmartHub3in1StateCtrl_Type(Integer32):
    """Custom type eSmartHub3in1StateCtrl based on Integer32"""
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
        *(("aUI", 4),
          ("auto", 5),
          ("bNC", 3),
          ("other", 1),
          ("uTP", 2))
    )


_ESmartHub3in1StateCtrl_Type.__name__ = "Integer32"
_ESmartHub3in1StateCtrl_Object = MibScalar
eSmartHub3in1StateCtrl = _ESmartHub3in1StateCtrl_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 2, 1, 8),
    _ESmartHub3in1StateCtrl_Type()
)
eSmartHub3in1StateCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eSmartHub3in1StateCtrl.setStatus("mandatory")
_ConcStatistics_ObjectIdentity = ObjectIdentity
concStatistics = _ConcStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3)
)
_EStatistics_ObjectIdentity = ObjectIdentity
eStatistics = _EStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1)
)
_EGlobalStatistics_ObjectIdentity = ObjectIdentity
eGlobalStatistics = _EGlobalStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 1)
)
_EGlobalHubReadableFrames_Type = Counter32
_EGlobalHubReadableFrames_Object = MibScalar
eGlobalHubReadableFrames = _EGlobalHubReadableFrames_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 1, 1),
    _EGlobalHubReadableFrames_Type()
)
eGlobalHubReadableFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eGlobalHubReadableFrames.setStatus("mandatory")
_EGlobalHubMcastFrames_Type = Counter32
_EGlobalHubMcastFrames_Object = MibScalar
eGlobalHubMcastFrames = _EGlobalHubMcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 1, 2),
    _EGlobalHubMcastFrames_Type()
)
eGlobalHubMcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eGlobalHubMcastFrames.setStatus("mandatory")
_EGlobalHubBcastFrames_Type = Counter32
_EGlobalHubBcastFrames_Object = MibScalar
eGlobalHubBcastFrames = _EGlobalHubBcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 1, 3),
    _EGlobalHubBcastFrames_Type()
)
eGlobalHubBcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eGlobalHubBcastFrames.setStatus("mandatory")
_EGlobalHubFrameTooLongs_Type = Counter32
_EGlobalHubFrameTooLongs_Object = MibScalar
eGlobalHubFrameTooLongs = _EGlobalHubFrameTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 1, 4),
    _EGlobalHubFrameTooLongs_Type()
)
eGlobalHubFrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eGlobalHubFrameTooLongs.setStatus("mandatory")
_EGlobalHubRunts_Type = Counter32
_EGlobalHubRunts_Object = MibScalar
eGlobalHubRunts = _EGlobalHubRunts_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 1, 5),
    _EGlobalHubRunts_Type()
)
eGlobalHubRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eGlobalHubRunts.setStatus("mandatory")
_EGlobalHubAlignmentErrors_Type = Counter32
_EGlobalHubAlignmentErrors_Object = MibScalar
eGlobalHubAlignmentErrors = _EGlobalHubAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 1, 6),
    _EGlobalHubAlignmentErrors_Type()
)
eGlobalHubAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eGlobalHubAlignmentErrors.setStatus("mandatory")
_EGlobalHubFragmentErrors_Type = Counter32
_EGlobalHubFragmentErrors_Object = MibScalar
eGlobalHubFragmentErrors = _EGlobalHubFragmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 1, 7),
    _EGlobalHubFragmentErrors_Type()
)
eGlobalHubFragmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eGlobalHubFragmentErrors.setStatus("mandatory")
_EGlobalHubFCSErrors_Type = Counter32
_EGlobalHubFCSErrors_Object = MibScalar
eGlobalHubFCSErrors = _EGlobalHubFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 1, 8),
    _EGlobalHubFCSErrors_Type()
)
eGlobalHubFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eGlobalHubFCSErrors.setStatus("mandatory")
_EGlobalHubIFGErrors_Type = Counter32
_EGlobalHubIFGErrors_Object = MibScalar
eGlobalHubIFGErrors = _EGlobalHubIFGErrors_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 1, 9),
    _EGlobalHubIFGErrors_Type()
)
eGlobalHubIFGErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eGlobalHubIFGErrors.setStatus("mandatory")
_EGlobalHubDataRateMismatchs_Type = Counter32
_EGlobalHubDataRateMismatchs_Object = MibScalar
eGlobalHubDataRateMismatchs = _EGlobalHubDataRateMismatchs_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 1, 10),
    _EGlobalHubDataRateMismatchs_Type()
)
eGlobalHubDataRateMismatchs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eGlobalHubDataRateMismatchs.setStatus("mandatory")
_EGlobalHubShortEvents_Type = Counter32
_EGlobalHubShortEvents_Object = MibScalar
eGlobalHubShortEvents = _EGlobalHubShortEvents_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 1, 11),
    _EGlobalHubShortEvents_Type()
)
eGlobalHubShortEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eGlobalHubShortEvents.setStatus("mandatory")
_EGlobalHubCollisions_Type = Counter32
_EGlobalHubCollisions_Object = MibScalar
eGlobalHubCollisions = _EGlobalHubCollisions_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 1, 12),
    _EGlobalHubCollisions_Type()
)
eGlobalHubCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eGlobalHubCollisions.setStatus("mandatory")
_EGlobalHubLateCollisions_Type = Counter32
_EGlobalHubLateCollisions_Object = MibScalar
eGlobalHubLateCollisions = _EGlobalHubLateCollisions_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 1, 13),
    _EGlobalHubLateCollisions_Type()
)
eGlobalHubLateCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eGlobalHubLateCollisions.setStatus("mandatory")
_EGlobalHubMJLPs_Type = Counter32
_EGlobalHubMJLPs_Object = MibScalar
eGlobalHubMJLPs = _EGlobalHubMJLPs_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 1, 14),
    _EGlobalHubMJLPs_Type()
)
eGlobalHubMJLPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eGlobalHubMJLPs.setStatus("mandatory")
_EGlobalHubAutoPartitions_Type = Counter32
_EGlobalHubAutoPartitions_Object = MibScalar
eGlobalHubAutoPartitions = _EGlobalHubAutoPartitions_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 1, 15),
    _EGlobalHubAutoPartitions_Type()
)
eGlobalHubAutoPartitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eGlobalHubAutoPartitions.setStatus("mandatory")
_EGlobalHubSFDMissings_Type = Counter32
_EGlobalHubSFDMissings_Object = MibScalar
eGlobalHubSFDMissings = _EGlobalHubSFDMissings_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 1, 16),
    _EGlobalHubSFDMissings_Type()
)
eGlobalHubSFDMissings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eGlobalHubSFDMissings.setStatus("mandatory")
_EGlobalHubBadFrames_Type = Counter32
_EGlobalHubBadFrames_Object = MibScalar
eGlobalHubBadFrames = _EGlobalHubBadFrames_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 1, 17),
    _EGlobalHubBadFrames_Type()
)
eGlobalHubBadFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eGlobalHubBadFrames.setStatus("mandatory")
_EGrpStatisticsTable_Object = MibTable
eGrpStatisticsTable = _EGrpStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 3)
)
if mibBuilder.loadTexts:
    eGrpStatisticsTable.setStatus("mandatory")
_EGrpStatisticsEntry_Object = MibTableRow
eGrpStatisticsEntry = _EGrpStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 3, 1)
)
eGrpStatisticsEntry.setIndexNames(
    (0, "ASANTE-AH1012-MIB", "eGrpStatIndex"),
)
if mibBuilder.loadTexts:
    eGrpStatisticsEntry.setStatus("mandatory")
_EGrpStatIndex_Type = Integer32
_EGrpStatIndex_Object = MibTableColumn
eGrpStatIndex = _EGrpStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 3, 1, 1),
    _EGrpStatIndex_Type()
)
eGrpStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eGrpStatIndex.setStatus("mandatory")
_EGrpStatReadableFrames_Type = Counter32
_EGrpStatReadableFrames_Object = MibTableColumn
eGrpStatReadableFrames = _EGrpStatReadableFrames_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 3, 1, 2),
    _EGrpStatReadableFrames_Type()
)
eGrpStatReadableFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eGrpStatReadableFrames.setStatus("mandatory")
_EGrpStatMcastFrames_Type = Counter32
_EGrpStatMcastFrames_Object = MibTableColumn
eGrpStatMcastFrames = _EGrpStatMcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 3, 1, 3),
    _EGrpStatMcastFrames_Type()
)
eGrpStatMcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eGrpStatMcastFrames.setStatus("mandatory")
_EGrpStatBcastFrames_Type = Counter32
_EGrpStatBcastFrames_Object = MibTableColumn
eGrpStatBcastFrames = _EGrpStatBcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 3, 1, 4),
    _EGrpStatBcastFrames_Type()
)
eGrpStatBcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eGrpStatBcastFrames.setStatus("mandatory")
_EGrpStatFrameTooLongs_Type = Counter32
_EGrpStatFrameTooLongs_Object = MibTableColumn
eGrpStatFrameTooLongs = _EGrpStatFrameTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 3, 1, 5),
    _EGrpStatFrameTooLongs_Type()
)
eGrpStatFrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eGrpStatFrameTooLongs.setStatus("mandatory")
_EGrpStatRunts_Type = Counter32
_EGrpStatRunts_Object = MibTableColumn
eGrpStatRunts = _EGrpStatRunts_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 3, 1, 6),
    _EGrpStatRunts_Type()
)
eGrpStatRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eGrpStatRunts.setStatus("mandatory")
_EGrpStatAlignmentErrors_Type = Counter32
_EGrpStatAlignmentErrors_Object = MibTableColumn
eGrpStatAlignmentErrors = _EGrpStatAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 3, 1, 7),
    _EGrpStatAlignmentErrors_Type()
)
eGrpStatAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eGrpStatAlignmentErrors.setStatus("mandatory")
_EGrpStatFragmentErrors_Type = Counter32
_EGrpStatFragmentErrors_Object = MibTableColumn
eGrpStatFragmentErrors = _EGrpStatFragmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 3, 1, 8),
    _EGrpStatFragmentErrors_Type()
)
eGrpStatFragmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eGrpStatFragmentErrors.setStatus("mandatory")
_EGrpStatFCSErrors_Type = Counter32
_EGrpStatFCSErrors_Object = MibTableColumn
eGrpStatFCSErrors = _EGrpStatFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 3, 1, 9),
    _EGrpStatFCSErrors_Type()
)
eGrpStatFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eGrpStatFCSErrors.setStatus("mandatory")
_EGrpStatIFGErrors_Type = Counter32
_EGrpStatIFGErrors_Object = MibTableColumn
eGrpStatIFGErrors = _EGrpStatIFGErrors_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 3, 1, 10),
    _EGrpStatIFGErrors_Type()
)
eGrpStatIFGErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eGrpStatIFGErrors.setStatus("mandatory")
_EGrpStatDataRateMismatchs_Type = Counter32
_EGrpStatDataRateMismatchs_Object = MibTableColumn
eGrpStatDataRateMismatchs = _EGrpStatDataRateMismatchs_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 3, 1, 11),
    _EGrpStatDataRateMismatchs_Type()
)
eGrpStatDataRateMismatchs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eGrpStatDataRateMismatchs.setStatus("mandatory")
_EGrpStatShortEvents_Type = Counter32
_EGrpStatShortEvents_Object = MibTableColumn
eGrpStatShortEvents = _EGrpStatShortEvents_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 3, 1, 12),
    _EGrpStatShortEvents_Type()
)
eGrpStatShortEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eGrpStatShortEvents.setStatus("mandatory")
_EGrpStatCollisions_Type = Counter32
_EGrpStatCollisions_Object = MibTableColumn
eGrpStatCollisions = _EGrpStatCollisions_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 3, 1, 13),
    _EGrpStatCollisions_Type()
)
eGrpStatCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eGrpStatCollisions.setStatus("mandatory")
_EGrpStatLateCollisions_Type = Counter32
_EGrpStatLateCollisions_Object = MibTableColumn
eGrpStatLateCollisions = _EGrpStatLateCollisions_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 3, 1, 14),
    _EGrpStatLateCollisions_Type()
)
eGrpStatLateCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eGrpStatLateCollisions.setStatus("mandatory")
_EGrpStatMJLPs_Type = Counter32
_EGrpStatMJLPs_Object = MibTableColumn
eGrpStatMJLPs = _EGrpStatMJLPs_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 3, 1, 15),
    _EGrpStatMJLPs_Type()
)
eGrpStatMJLPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eGrpStatMJLPs.setStatus("mandatory")
_EGrpStatAutoPartitions_Type = Counter32
_EGrpStatAutoPartitions_Object = MibTableColumn
eGrpStatAutoPartitions = _EGrpStatAutoPartitions_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 3, 1, 16),
    _EGrpStatAutoPartitions_Type()
)
eGrpStatAutoPartitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eGrpStatAutoPartitions.setStatus("mandatory")
_EGrpStatSFDMissings_Type = Counter32
_EGrpStatSFDMissings_Object = MibTableColumn
eGrpStatSFDMissings = _EGrpStatSFDMissings_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 3, 1, 17),
    _EGrpStatSFDMissings_Type()
)
eGrpStatSFDMissings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eGrpStatSFDMissings.setStatus("mandatory")
_EGrpStatBadFrames_Type = Counter32
_EGrpStatBadFrames_Object = MibTableColumn
eGrpStatBadFrames = _EGrpStatBadFrames_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 3, 1, 18),
    _EGrpStatBadFrames_Type()
)
eGrpStatBadFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eGrpStatBadFrames.setStatus("mandatory")
_EPortStatisticsTable_Object = MibTable
ePortStatisticsTable = _EPortStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 4)
)
if mibBuilder.loadTexts:
    ePortStatisticsTable.setStatus("mandatory")
_EPortStatisticsEntry_Object = MibTableRow
ePortStatisticsEntry = _EPortStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 4, 1)
)
ePortStatisticsEntry.setIndexNames(
    (0, "ASANTE-AH1012-MIB", "ePortGrpIndex"),
    (0, "ASANTE-AH1012-MIB", "ePortIndex"),
)
if mibBuilder.loadTexts:
    ePortStatisticsEntry.setStatus("mandatory")
_EPortGrpIndex_Type = Integer32
_EPortGrpIndex_Object = MibTableColumn
ePortGrpIndex = _EPortGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 4, 1, 1),
    _EPortGrpIndex_Type()
)
ePortGrpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePortGrpIndex.setStatus("mandatory")
_EPortIndex_Type = Integer32
_EPortIndex_Object = MibTableColumn
ePortIndex = _EPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 4, 1, 2),
    _EPortIndex_Type()
)
ePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePortIndex.setStatus("mandatory")
_EPortStatReadableFrames_Type = Counter32
_EPortStatReadableFrames_Object = MibTableColumn
ePortStatReadableFrames = _EPortStatReadableFrames_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 4, 1, 3),
    _EPortStatReadableFrames_Type()
)
ePortStatReadableFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePortStatReadableFrames.setStatus("mandatory")
_EPortStatMcastFrames_Type = Counter32
_EPortStatMcastFrames_Object = MibTableColumn
ePortStatMcastFrames = _EPortStatMcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 4, 1, 4),
    _EPortStatMcastFrames_Type()
)
ePortStatMcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePortStatMcastFrames.setStatus("mandatory")
_EPortStatBcastFrames_Type = Counter32
_EPortStatBcastFrames_Object = MibTableColumn
ePortStatBcastFrames = _EPortStatBcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 4, 1, 5),
    _EPortStatBcastFrames_Type()
)
ePortStatBcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePortStatBcastFrames.setStatus("mandatory")
_EPortStatFrameTooLongs_Type = Counter32
_EPortStatFrameTooLongs_Object = MibTableColumn
ePortStatFrameTooLongs = _EPortStatFrameTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 4, 1, 6),
    _EPortStatFrameTooLongs_Type()
)
ePortStatFrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePortStatFrameTooLongs.setStatus("mandatory")
_EPortStatRunts_Type = Counter32
_EPortStatRunts_Object = MibTableColumn
ePortStatRunts = _EPortStatRunts_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 4, 1, 7),
    _EPortStatRunts_Type()
)
ePortStatRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePortStatRunts.setStatus("mandatory")
_EPortStatAlignmentErrors_Type = Counter32
_EPortStatAlignmentErrors_Object = MibTableColumn
ePortStatAlignmentErrors = _EPortStatAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 4, 1, 8),
    _EPortStatAlignmentErrors_Type()
)
ePortStatAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePortStatAlignmentErrors.setStatus("mandatory")
_EPortStatFragmentErrors_Type = Counter32
_EPortStatFragmentErrors_Object = MibTableColumn
ePortStatFragmentErrors = _EPortStatFragmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 4, 1, 9),
    _EPortStatFragmentErrors_Type()
)
ePortStatFragmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePortStatFragmentErrors.setStatus("mandatory")
_EPortStatFCSErrors_Type = Counter32
_EPortStatFCSErrors_Object = MibTableColumn
ePortStatFCSErrors = _EPortStatFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 4, 1, 10),
    _EPortStatFCSErrors_Type()
)
ePortStatFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePortStatFCSErrors.setStatus("mandatory")
_EPortStatIFGErrors_Type = Counter32
_EPortStatIFGErrors_Object = MibTableColumn
ePortStatIFGErrors = _EPortStatIFGErrors_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 4, 1, 11),
    _EPortStatIFGErrors_Type()
)
ePortStatIFGErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePortStatIFGErrors.setStatus("mandatory")
_EPortStatDataRateMismatchs_Type = Counter32
_EPortStatDataRateMismatchs_Object = MibTableColumn
ePortStatDataRateMismatchs = _EPortStatDataRateMismatchs_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 4, 1, 12),
    _EPortStatDataRateMismatchs_Type()
)
ePortStatDataRateMismatchs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePortStatDataRateMismatchs.setStatus("mandatory")
_EPortStatShortEvents_Type = Counter32
_EPortStatShortEvents_Object = MibTableColumn
ePortStatShortEvents = _EPortStatShortEvents_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 4, 1, 13),
    _EPortStatShortEvents_Type()
)
ePortStatShortEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePortStatShortEvents.setStatus("mandatory")
_EPortStatCollisions_Type = Counter32
_EPortStatCollisions_Object = MibTableColumn
ePortStatCollisions = _EPortStatCollisions_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 4, 1, 14),
    _EPortStatCollisions_Type()
)
ePortStatCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePortStatCollisions.setStatus("mandatory")
_EPortStatLateCollisions_Type = Counter32
_EPortStatLateCollisions_Object = MibTableColumn
ePortStatLateCollisions = _EPortStatLateCollisions_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 4, 1, 15),
    _EPortStatLateCollisions_Type()
)
ePortStatLateCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePortStatLateCollisions.setStatus("mandatory")
_EPortStatMJLPs_Type = Counter32
_EPortStatMJLPs_Object = MibTableColumn
ePortStatMJLPs = _EPortStatMJLPs_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 4, 1, 16),
    _EPortStatMJLPs_Type()
)
ePortStatMJLPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePortStatMJLPs.setStatus("mandatory")
_EPortStatAutoPartitions_Type = Counter32
_EPortStatAutoPartitions_Object = MibTableColumn
ePortStatAutoPartitions = _EPortStatAutoPartitions_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 4, 1, 17),
    _EPortStatAutoPartitions_Type()
)
ePortStatAutoPartitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePortStatAutoPartitions.setStatus("mandatory")
_EPortStatSFDMissings_Type = Counter32
_EPortStatSFDMissings_Object = MibTableColumn
ePortStatSFDMissings = _EPortStatSFDMissings_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 4, 1, 18),
    _EPortStatSFDMissings_Type()
)
ePortStatSFDMissings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePortStatSFDMissings.setStatus("mandatory")
_EPortStatBadFrames_Type = Counter32
_EPortStatBadFrames_Object = MibTableColumn
ePortStatBadFrames = _EPortStatBadFrames_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 4, 1, 19),
    _EPortStatBadFrames_Type()
)
ePortStatBadFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePortStatBadFrames.setStatus("mandatory")
_ETrafficMatrixTable_Object = MibTable
eTrafficMatrixTable = _ETrafficMatrixTable_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 5)
)
if mibBuilder.loadTexts:
    eTrafficMatrixTable.setStatus("mandatory")
_ETrafficMatrixEntry_Object = MibTableRow
eTrafficMatrixEntry = _ETrafficMatrixEntry_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 5, 1)
)
eTrafficMatrixEntry.setIndexNames(
    (0, "ASANTE-AH1012-MIB", "eTrafficMatrixLength"),
)
if mibBuilder.loadTexts:
    eTrafficMatrixEntry.setStatus("mandatory")
_ETrafficMatrixLength_Type = Integer32
_ETrafficMatrixLength_Object = MibTableColumn
eTrafficMatrixLength = _ETrafficMatrixLength_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 5, 1, 1),
    _ETrafficMatrixLength_Type()
)
eTrafficMatrixLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eTrafficMatrixLength.setStatus("mandatory")


class _ETrafficMatrixRange_Type(Integer32):
    """Custom type eTrafficMatrixRange based on Integer32"""
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
        *(("exact-64-bytes", 11),
          ("from-1-to-63-bytes", 2),
          ("from-1024-to-1518-bytes", 8),
          ("from-128-to-255-bytes", 4),
          ("from-256-to-511-bytes", 5),
          ("from-512-to-1023-bytes", 9),
          ("from-512-to-767-bytes", 6),
          ("from-64-to-127-bytes", 3),
          ("from-65-to-511-bytes", 10),
          ("from-768-to-1023-bytes", 7),
          ("other", 1),
          ("over-1518-bytes", 12))
    )


_ETrafficMatrixRange_Type.__name__ = "Integer32"
_ETrafficMatrixRange_Object = MibTableColumn
eTrafficMatrixRange = _ETrafficMatrixRange_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 5, 1, 2),
    _ETrafficMatrixRange_Type()
)
eTrafficMatrixRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eTrafficMatrixRange.setStatus("mandatory")
_ETrafficMatrixFramesCounts_Type = Counter32
_ETrafficMatrixFramesCounts_Object = MibTableColumn
eTrafficMatrixFramesCounts = _ETrafficMatrixFramesCounts_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 5, 1, 3),
    _ETrafficMatrixFramesCounts_Type()
)
eTrafficMatrixFramesCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eTrafficMatrixFramesCounts.setStatus("mandatory")
_ESpecific_ObjectIdentity = ObjectIdentity
eSpecific = _ESpecific_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 6)
)
_ESmartHubSpec_ObjectIdentity = ObjectIdentity
eSmartHubSpec = _ESmartHubSpec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 6, 1)
)
_EColGraphBar_Type = Integer32
_EColGraphBar_Object = MibScalar
eColGraphBar = _EColGraphBar_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 6, 1, 1),
    _EColGraphBar_Type()
)
eColGraphBar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eColGraphBar.setStatus("mandatory")
_EUtilGraphBar_Type = Integer32
_EUtilGraphBar_Object = MibScalar
eUtilGraphBar = _EUtilGraphBar_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 6, 1, 2),
    _EUtilGraphBar_Type()
)
eUtilGraphBar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eUtilGraphBar.setStatus("mandatory")
_EPortRateTable_Object = MibTable
ePortRateTable = _EPortRateTable_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 6, 1, 6)
)
if mibBuilder.loadTexts:
    ePortRateTable.setStatus("optional")
_EPortRateEntry_Object = MibTableRow
ePortRateEntry = _EPortRateEntry_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 6, 1, 6, 1)
)
ePortRateEntry.setIndexNames(
    (0, "ASANTE-AH1012-MIB", "ePortRateGrpIndex"),
    (0, "ASANTE-AH1012-MIB", "ePortRatePortIndex"),
)
if mibBuilder.loadTexts:
    ePortRateEntry.setStatus("optional")
_EPortRateGrpIndex_Type = Integer32
_EPortRateGrpIndex_Object = MibTableColumn
ePortRateGrpIndex = _EPortRateGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 6, 1, 6, 1, 1),
    _EPortRateGrpIndex_Type()
)
ePortRateGrpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePortRateGrpIndex.setStatus("optional")
_EPortRatePortIndex_Type = Integer32
_EPortRatePortIndex_Object = MibTableColumn
ePortRatePortIndex = _EPortRatePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 6, 1, 6, 1, 2),
    _EPortRatePortIndex_Type()
)
ePortRatePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePortRatePortIndex.setStatus("optional")
_EPortRateReadableFrames_Type = Integer32
_EPortRateReadableFrames_Object = MibTableColumn
ePortRateReadableFrames = _EPortRateReadableFrames_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 6, 1, 6, 1, 3),
    _EPortRateReadableFrames_Type()
)
ePortRateReadableFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePortRateReadableFrames.setStatus("optional")
_EPortRateMcastFrames_Type = Integer32
_EPortRateMcastFrames_Object = MibTableColumn
ePortRateMcastFrames = _EPortRateMcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 6, 1, 6, 1, 4),
    _EPortRateMcastFrames_Type()
)
ePortRateMcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePortRateMcastFrames.setStatus("optional")
_EPortRateBcastFrames_Type = Integer32
_EPortRateBcastFrames_Object = MibTableColumn
ePortRateBcastFrames = _EPortRateBcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 6, 1, 6, 1, 5),
    _EPortRateBcastFrames_Type()
)
ePortRateBcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePortRateBcastFrames.setStatus("optional")
_EPortRateFrameTooLongs_Type = Integer32
_EPortRateFrameTooLongs_Object = MibTableColumn
ePortRateFrameTooLongs = _EPortRateFrameTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 6, 1, 6, 1, 6),
    _EPortRateFrameTooLongs_Type()
)
ePortRateFrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePortRateFrameTooLongs.setStatus("optional")
_EPortRateRunts_Type = Integer32
_EPortRateRunts_Object = MibTableColumn
ePortRateRunts = _EPortRateRunts_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 6, 1, 6, 1, 7),
    _EPortRateRunts_Type()
)
ePortRateRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePortRateRunts.setStatus("optional")
_EPortRateAlignmentErrors_Type = Integer32
_EPortRateAlignmentErrors_Object = MibTableColumn
ePortRateAlignmentErrors = _EPortRateAlignmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 6, 1, 6, 1, 8),
    _EPortRateAlignmentErrors_Type()
)
ePortRateAlignmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePortRateAlignmentErrors.setStatus("optional")
_EPortRateFragmentErrors_Type = Integer32
_EPortRateFragmentErrors_Object = MibTableColumn
ePortRateFragmentErrors = _EPortRateFragmentErrors_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 6, 1, 6, 1, 9),
    _EPortRateFragmentErrors_Type()
)
ePortRateFragmentErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePortRateFragmentErrors.setStatus("optional")
_EPortRateFCSErrors_Type = Integer32
_EPortRateFCSErrors_Object = MibTableColumn
ePortRateFCSErrors = _EPortRateFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 6, 1, 6, 1, 10),
    _EPortRateFCSErrors_Type()
)
ePortRateFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePortRateFCSErrors.setStatus("optional")
_EPortRateIFGErrors_Type = Integer32
_EPortRateIFGErrors_Object = MibTableColumn
ePortRateIFGErrors = _EPortRateIFGErrors_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 6, 1, 6, 1, 11),
    _EPortRateIFGErrors_Type()
)
ePortRateIFGErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePortRateIFGErrors.setStatus("optional")
_EPortRateDataRateMismatch_Type = Integer32
_EPortRateDataRateMismatch_Object = MibTableColumn
ePortRateDataRateMismatch = _EPortRateDataRateMismatch_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 6, 1, 6, 1, 12),
    _EPortRateDataRateMismatch_Type()
)
ePortRateDataRateMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePortRateDataRateMismatch.setStatus("optional")
_EPortRateShortEvents_Type = Integer32
_EPortRateShortEvents_Object = MibTableColumn
ePortRateShortEvents = _EPortRateShortEvents_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 6, 1, 6, 1, 13),
    _EPortRateShortEvents_Type()
)
ePortRateShortEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePortRateShortEvents.setStatus("optional")
_EPortRateCollisions_Type = Integer32
_EPortRateCollisions_Object = MibTableColumn
ePortRateCollisions = _EPortRateCollisions_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 6, 1, 6, 1, 14),
    _EPortRateCollisions_Type()
)
ePortRateCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePortRateCollisions.setStatus("optional")
_EPortRateLateCollisions_Type = Integer32
_EPortRateLateCollisions_Object = MibTableColumn
ePortRateLateCollisions = _EPortRateLateCollisions_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 6, 1, 6, 1, 15),
    _EPortRateLateCollisions_Type()
)
ePortRateLateCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePortRateLateCollisions.setStatus("optional")
_EPortRateMJLPs_Type = Integer32
_EPortRateMJLPs_Object = MibTableColumn
ePortRateMJLPs = _EPortRateMJLPs_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 6, 1, 6, 1, 16),
    _EPortRateMJLPs_Type()
)
ePortRateMJLPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePortRateMJLPs.setStatus("optional")
_EPortRateAutoPartitions_Type = Integer32
_EPortRateAutoPartitions_Object = MibTableColumn
ePortRateAutoPartitions = _EPortRateAutoPartitions_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 6, 1, 6, 1, 17),
    _EPortRateAutoPartitions_Type()
)
ePortRateAutoPartitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePortRateAutoPartitions.setStatus("optional")
_EPortRateSFDMissings_Type = Integer32
_EPortRateSFDMissings_Object = MibTableColumn
ePortRateSFDMissings = _EPortRateSFDMissings_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 6, 1, 6, 1, 18),
    _EPortRateSFDMissings_Type()
)
ePortRateSFDMissings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePortRateSFDMissings.setStatus("optional")
_EPortRateBadFrames_Type = Integer32
_EPortRateBadFrames_Object = MibTableColumn
ePortRateBadFrames = _EPortRateBadFrames_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 3, 1, 6, 1, 6, 1, 19),
    _EPortRateBadFrames_Type()
)
ePortRateBadFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePortRateBadFrames.setStatus("optional")
_ConcStateCtrl_ObjectIdentity = ObjectIdentity
concStateCtrl = _ConcStateCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 4)
)
_EStateCtrl_ObjectIdentity = ObjectIdentity
eStateCtrl = _EStateCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 4, 1)
)
_EPortStateCtrlTable_Object = MibTable
ePortStateCtrlTable = _EPortStateCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 4, 1, 1)
)
if mibBuilder.loadTexts:
    ePortStateCtrlTable.setStatus("mandatory")
_EPortStateCtrlEntry_Object = MibTableRow
ePortStateCtrlEntry = _EPortStateCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 4, 1, 1, 1)
)
ePortStateCtrlEntry.setIndexNames(
    (0, "ASANTE-AH1012-MIB", "ePortStateGrpIndex"),
    (0, "ASANTE-AH1012-MIB", "ePortStatePortIndex"),
)
if mibBuilder.loadTexts:
    ePortStateCtrlEntry.setStatus("mandatory")
_EPortStateGrpIndex_Type = Integer32
_EPortStateGrpIndex_Object = MibTableColumn
ePortStateGrpIndex = _EPortStateGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 4, 1, 1, 1, 1),
    _EPortStateGrpIndex_Type()
)
ePortStateGrpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePortStateGrpIndex.setStatus("mandatory")
_EPortStatePortIndex_Type = Integer32
_EPortStatePortIndex_Object = MibTableColumn
ePortStatePortIndex = _EPortStatePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 4, 1, 1, 1, 2),
    _EPortStatePortIndex_Type()
)
ePortStatePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePortStatePortIndex.setStatus("mandatory")


class _EPortStateType_Type(Integer32):
    """Custom type ePortStateType based on Integer32"""
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
        *(("aUI", 3),
          ("bNC", 2),
          ("foil", 5),
          ("other", 1),
          ("rJ45", 4),
          ("three-in-one", 6))
    )


_EPortStateType_Type.__name__ = "Integer32"
_EPortStateType_Object = MibTableColumn
ePortStateType = _EPortStateType_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 4, 1, 1, 1, 3),
    _EPortStateType_Type()
)
ePortStateType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePortStateType.setStatus("mandatory")


class _EPortStateLinkStatus_Type(Integer32):
    """Custom type ePortStateLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("linkoff", 3),
          ("linkon", 2),
          ("others", 1))
    )


_EPortStateLinkStatus_Type.__name__ = "Integer32"
_EPortStateLinkStatus_Object = MibTableColumn
ePortStateLinkStatus = _EPortStateLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 4, 1, 1, 1, 4),
    _EPortStateLinkStatus_Type()
)
ePortStateLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePortStateLinkStatus.setStatus("mandatory")


class _EPortStateLinkIntegTest_Type(Integer32):
    """Custom type ePortStateLinkIntegTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("linkTestDisable", 3),
          ("linkTestEnable", 2),
          ("others", 1))
    )


_EPortStateLinkIntegTest_Type.__name__ = "Integer32"
_EPortStateLinkIntegTest_Object = MibTableColumn
ePortStateLinkIntegTest = _EPortStateLinkIntegTest_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 4, 1, 1, 1, 5),
    _EPortStateLinkIntegTest_Type()
)
ePortStateLinkIntegTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ePortStateLinkIntegTest.setStatus("mandatory")


class _EPortStateAutoPartStatus_Type(Integer32):
    """Custom type ePortStateAutoPartStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autopartitioned", 2),
          ("notautopartitioned", 3),
          ("others", 1))
    )


_EPortStateAutoPartStatus_Type.__name__ = "Integer32"
_EPortStateAutoPartStatus_Object = MibTableColumn
ePortStateAutoPartStatus = _EPortStateAutoPartStatus_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 4, 1, 1, 1, 6),
    _EPortStateAutoPartStatus_Type()
)
ePortStateAutoPartStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePortStateAutoPartStatus.setStatus("mandatory")


class _EPortStateJabberStatus_Type(Integer32):
    """Custom type ePortStateJabberStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 3),
          ("on", 2),
          ("others", 1))
    )


_EPortStateJabberStatus_Type.__name__ = "Integer32"
_EPortStateJabberStatus_Object = MibTableColumn
ePortStateJabberStatus = _EPortStateJabberStatus_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 4, 1, 1, 1, 7),
    _EPortStateJabberStatus_Type()
)
ePortStateJabberStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePortStateJabberStatus.setStatus("mandatory")


class _EPortStateJabberState_Type(Integer32):
    """Custom type ePortStateJabberState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("others", 1))
    )


_EPortStateJabberState_Type.__name__ = "Integer32"
_EPortStateJabberState_Object = MibTableColumn
ePortStateJabberState = _EPortStateJabberState_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 4, 1, 1, 1, 8),
    _EPortStateJabberState_Type()
)
ePortStateJabberState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ePortStateJabberState.setStatus("mandatory")


class _EPortStateAdminState_Type(Integer32):
    """Custom type ePortStateAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("others", 1))
    )


_EPortStateAdminState_Type.__name__ = "Integer32"
_EPortStateAdminState_Object = MibTableColumn
ePortStateAdminState = _EPortStateAdminState_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 4, 1, 1, 1, 9),
    _EPortStateAdminState_Type()
)
ePortStateAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ePortStateAdminState.setStatus("mandatory")


class _EPortStateRDTState_Type(Integer32):
    """Custom type ePortStateRDTState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("others", 1),
          ("reduce", 3),
          ("unreduce", 2))
    )


_EPortStateRDTState_Type.__name__ = "Integer32"
_EPortStateRDTState_Object = MibTableColumn
ePortStateRDTState = _EPortStateRDTState_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 4, 1, 1, 1, 10),
    _EPortStateRDTState_Type()
)
ePortStateRDTState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ePortStateRDTState.setStatus("mandatory")


class _EPortStatePolarityStatus_Type(Integer32):
    """Custom type ePortStatePolarityStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 2),
          ("others", 1),
          ("reversed", 3))
    )


_EPortStatePolarityStatus_Type.__name__ = "Integer32"
_EPortStatePolarityStatus_Object = MibTableColumn
ePortStatePolarityStatus = _EPortStatePolarityStatus_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 4, 1, 1, 1, 11),
    _EPortStatePolarityStatus_Type()
)
ePortStatePolarityStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ePortStatePolarityStatus.setStatus("mandatory")


class _EPortStatePolarityState_Type(Integer32):
    """Custom type ePortStatePolarityState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 3),
          ("enabled", 2),
          ("others", 1))
    )


_EPortStatePolarityState_Type.__name__ = "Integer32"
_EPortStatePolarityState_Object = MibTableColumn
ePortStatePolarityState = _EPortStatePolarityState_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 4, 1, 1, 1, 12),
    _EPortStatePolarityState_Type()
)
ePortStatePolarityState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ePortStatePolarityState.setStatus("mandatory")
_ConcNodeMgt_ObjectIdentity = ObjectIdentity
concNodeMgt = _ConcNodeMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 5)
)
_NodeSummaryTable_Object = MibTable
nodeSummaryTable = _NodeSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 5, 1)
)
if mibBuilder.loadTexts:
    nodeSummaryTable.setStatus("mandatory")
_NodeSummaryEntry_Object = MibTableRow
nodeSummaryEntry = _NodeSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 5, 1, 1)
)
nodeSummaryEntry.setIndexNames(
    (0, "ASANTE-AH1012-MIB", "nodeSummaryGrpIndex"),
    (0, "ASANTE-AH1012-MIB", "nodeSummaryPortIndex"),
    (0, "ASANTE-AH1012-MIB", "nodeSummarySrcMacAddr"),
    (0, "ASANTE-AH1012-MIB", "nodeSummaryDestMacAddr"),
)
if mibBuilder.loadTexts:
    nodeSummaryEntry.setStatus("mandatory")
_NodeSummaryGrpIndex_Type = Integer32
_NodeSummaryGrpIndex_Object = MibTableColumn
nodeSummaryGrpIndex = _NodeSummaryGrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 5, 1, 1, 1),
    _NodeSummaryGrpIndex_Type()
)
nodeSummaryGrpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeSummaryGrpIndex.setStatus("mandatory")
_NodeSummaryPortIndex_Type = Integer32
_NodeSummaryPortIndex_Object = MibTableColumn
nodeSummaryPortIndex = _NodeSummaryPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 5, 1, 1, 2),
    _NodeSummaryPortIndex_Type()
)
nodeSummaryPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeSummaryPortIndex.setStatus("mandatory")
_NodeSummarySrcMacAddr_Type = PhysAddress
_NodeSummarySrcMacAddr_Object = MibTableColumn
nodeSummarySrcMacAddr = _NodeSummarySrcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 5, 1, 1, 3),
    _NodeSummarySrcMacAddr_Type()
)
nodeSummarySrcMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeSummarySrcMacAddr.setStatus("mandatory")
_NodeSummaryDestMacAddr_Type = PhysAddress
_NodeSummaryDestMacAddr_Object = MibTableColumn
nodeSummaryDestMacAddr = _NodeSummaryDestMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 5, 1, 1, 4),
    _NodeSummaryDestMacAddr_Type()
)
nodeSummaryDestMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeSummaryDestMacAddr.setStatus("mandatory")
_NodeSummaryEtherType_Type = Integer32
_NodeSummaryEtherType_Object = MibTableColumn
nodeSummaryEtherType = _NodeSummaryEtherType_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 5, 1, 1, 5),
    _NodeSummaryEtherType_Type()
)
nodeSummaryEtherType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeSummaryEtherType.setStatus("mandatory")
_NodeSummaryIpAddrPair_Type = OctetString
_NodeSummaryIpAddrPair_Object = MibTableColumn
nodeSummaryIpAddrPair = _NodeSummaryIpAddrPair_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 5, 1, 1, 6),
    _NodeSummaryIpAddrPair_Type()
)
nodeSummaryIpAddrPair.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeSummaryIpAddrPair.setStatus("mandatory")
_NodeSummaryTimeStamp_Type = TimeTicks
_NodeSummaryTimeStamp_Object = MibTableColumn
nodeSummaryTimeStamp = _NodeSummaryTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 5, 1, 1, 7),
    _NodeSummaryTimeStamp_Type()
)
nodeSummaryTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeSummaryTimeStamp.setStatus("mandatory")
_NodeSecurity_ObjectIdentity = ObjectIdentity
nodeSecurity = _NodeSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 5, 2)
)
_NodeSecuLev1Table_Object = MibTable
nodeSecuLev1Table = _NodeSecuLev1Table_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 5, 2, 1)
)
if mibBuilder.loadTexts:
    nodeSecuLev1Table.setStatus("mandatory")
_NodeSecuLev1Entry_Object = MibTableRow
nodeSecuLev1Entry = _NodeSecuLev1Entry_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 5, 2, 1, 1)
)
nodeSecuLev1Entry.setIndexNames(
    (0, "ASANTE-AH1012-MIB", "nodeSecuLev1GrpIndex"),
    (0, "ASANTE-AH1012-MIB", "nodeSecuLev1PortIndex"),
)
if mibBuilder.loadTexts:
    nodeSecuLev1Entry.setStatus("mandatory")
_NodeSecuLev1GrpIndex_Type = Integer32
_NodeSecuLev1GrpIndex_Object = MibTableColumn
nodeSecuLev1GrpIndex = _NodeSecuLev1GrpIndex_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 5, 2, 1, 1, 1),
    _NodeSecuLev1GrpIndex_Type()
)
nodeSecuLev1GrpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeSecuLev1GrpIndex.setStatus("mandatory")
_NodeSecuLev1PortIndex_Type = Integer32
_NodeSecuLev1PortIndex_Object = MibTableColumn
nodeSecuLev1PortIndex = _NodeSecuLev1PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 5, 2, 1, 1, 2),
    _NodeSecuLev1PortIndex_Type()
)
nodeSecuLev1PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeSecuLev1PortIndex.setStatus("mandatory")


class _NodeSecuLev1Status_Type(Integer32):
    """Custom type nodeSecuLev1Status based on Integer32"""
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


_NodeSecuLev1Status_Type.__name__ = "Integer32"
_NodeSecuLev1Status_Object = MibTableColumn
nodeSecuLev1Status = _NodeSecuLev1Status_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 5, 2, 1, 1, 3),
    _NodeSecuLev1Status_Type()
)
nodeSecuLev1Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeSecuLev1Status.setStatus("mandatory")
_NodeSecuLev1AllowedAddr_Type = PhysAddress
_NodeSecuLev1AllowedAddr_Object = MibTableColumn
nodeSecuLev1AllowedAddr = _NodeSecuLev1AllowedAddr_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 5, 2, 1, 1, 4),
    _NodeSecuLev1AllowedAddr_Type()
)
nodeSecuLev1AllowedAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeSecuLev1AllowedAddr.setStatus("mandatory")


class _NodeSecuLev1Action_Type(Integer32):
    """Custom type nodeSecuLev1Action based on Integer32"""
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
        *(("other", 1),
          ("partition-port", 2),
          ("partition-port-and-send-trap", 4),
          ("partition-port-and-send-trap-and-request-page", 6),
          ("send-trap", 3),
          ("send-trap-and-request-page", 5))
    )


_NodeSecuLev1Action_Type.__name__ = "Integer32"
_NodeSecuLev1Action_Object = MibTableColumn
nodeSecuLev1Action = _NodeSecuLev1Action_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 5, 2, 1, 1, 5),
    _NodeSecuLev1Action_Type()
)
nodeSecuLev1Action.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeSecuLev1Action.setStatus("mandatory")
_ConcAlarmMgt_ObjectIdentity = ObjectIdentity
concAlarmMgt = _ConcAlarmMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 6)
)
_ThresholdAlarm_ObjectIdentity = ObjectIdentity
thresholdAlarm = _ThresholdAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 6, 1)
)
_ThresholdLev1Table_Object = MibTable
thresholdLev1Table = _ThresholdLev1Table_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 6, 1, 1)
)
if mibBuilder.loadTexts:
    thresholdLev1Table.setStatus("optional")
_ThresholdLev1Entry_Object = MibTableRow
thresholdLev1Entry = _ThresholdLev1Entry_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 6, 1, 1, 1)
)
thresholdLev1Entry.setIndexNames(
    (0, "ASANTE-AH1012-MIB", "thresholdLev1Index"),
)
if mibBuilder.loadTexts:
    thresholdLev1Entry.setStatus("optional")
_ThresholdLev1Index_Type = Integer32
_ThresholdLev1Index_Object = MibTableColumn
thresholdLev1Index = _ThresholdLev1Index_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 6, 1, 1, 1, 1),
    _ThresholdLev1Index_Type()
)
thresholdLev1Index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thresholdLev1Index.setStatus("optional")


class _ThresholdLev1Status_Type(Integer32):
    """Custom type thresholdLev1Status based on Integer32"""
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


_ThresholdLev1Status_Type.__name__ = "Integer32"
_ThresholdLev1Status_Object = MibTableColumn
thresholdLev1Status = _ThresholdLev1Status_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 6, 1, 1, 1, 2),
    _ThresholdLev1Status_Type()
)
thresholdLev1Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdLev1Status.setStatus("optional")


class _ThresholdLev1Target_Type(Integer32):
    """Custom type thresholdLev1Target based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hub", 2),
          ("other", 1),
          ("port", 3))
    )


_ThresholdLev1Target_Type.__name__ = "Integer32"
_ThresholdLev1Target_Object = MibTableColumn
thresholdLev1Target = _ThresholdLev1Target_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 6, 1, 1, 1, 3),
    _ThresholdLev1Target_Type()
)
thresholdLev1Target.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdLev1Target.setStatus("optional")
_ThresholdLev1GroupIndex_Type = Integer32
_ThresholdLev1GroupIndex_Object = MibTableColumn
thresholdLev1GroupIndex = _ThresholdLev1GroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 6, 1, 1, 1, 4),
    _ThresholdLev1GroupIndex_Type()
)
thresholdLev1GroupIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdLev1GroupIndex.setStatus("optional")
_ThresholdLev1PortIndex_Type = Integer32
_ThresholdLev1PortIndex_Object = MibTableColumn
thresholdLev1PortIndex = _ThresholdLev1PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 6, 1, 1, 1, 5),
    _ThresholdLev1PortIndex_Type()
)
thresholdLev1PortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdLev1PortIndex.setStatus("optional")


class _ThresholdLev1Subject_Type(Integer32):
    """Custom type thresholdLev1Subject based on Integer32"""
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
              17)
        )
    )
    namedValues = NamedValues(
        *(("alignment-errors", 7),
          ("auto-partitions", 15),
          ("bad-frames", 17),
          ("bcast-frames", 4),
          ("collisions", 13),
          ("data-rate-mismatch", 11),
          ("fCS-errors", 9),
          ("fragment-errors", 8),
          ("frame-too-longs", 5),
          ("iFG-errors", 10),
          ("late-collisions", 14),
          ("mcast-frames", 3),
          ("other", 1),
          ("readable-frames", 2),
          ("runts", 6),
          ("sfd-missing", 16),
          ("short-events", 12))
    )


_ThresholdLev1Subject_Type.__name__ = "Integer32"
_ThresholdLev1Subject_Object = MibTableColumn
thresholdLev1Subject = _ThresholdLev1Subject_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 6, 1, 1, 1, 6),
    _ThresholdLev1Subject_Type()
)
thresholdLev1Subject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdLev1Subject.setStatus("optional")


class _ThresholdLev1SampleType_Type(Integer32):
    """Custom type thresholdLev1SampleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("event-per-second", 2),
          ("other", 1))
    )


_ThresholdLev1SampleType_Type.__name__ = "Integer32"
_ThresholdLev1SampleType_Object = MibTableColumn
thresholdLev1SampleType = _ThresholdLev1SampleType_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 6, 1, 1, 1, 7),
    _ThresholdLev1SampleType_Type()
)
thresholdLev1SampleType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdLev1SampleType.setStatus("optional")


class _ThresholdLev1StartupAlarm_Type(Integer32):
    """Custom type thresholdLev1StartupAlarm based on Integer32"""
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
        *(("falling", 3),
          ("other", 1),
          ("rising", 2),
          ("rising-or-falling", 4))
    )


_ThresholdLev1StartupAlarm_Type.__name__ = "Integer32"
_ThresholdLev1StartupAlarm_Object = MibTableColumn
thresholdLev1StartupAlarm = _ThresholdLev1StartupAlarm_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 6, 1, 1, 1, 8),
    _ThresholdLev1StartupAlarm_Type()
)
thresholdLev1StartupAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdLev1StartupAlarm.setStatus("optional")
_ThresholdLev1WaterMark_Type = Integer32
_ThresholdLev1WaterMark_Object = MibTableColumn
thresholdLev1WaterMark = _ThresholdLev1WaterMark_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 6, 1, 1, 1, 9),
    _ThresholdLev1WaterMark_Type()
)
thresholdLev1WaterMark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdLev1WaterMark.setStatus("optional")
_ThresholdLev1DetectedValue_Type = Integer32
_ThresholdLev1DetectedValue_Object = MibTableColumn
thresholdLev1DetectedValue = _ThresholdLev1DetectedValue_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 6, 1, 1, 1, 10),
    _ThresholdLev1DetectedValue_Type()
)
thresholdLev1DetectedValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thresholdLev1DetectedValue.setStatus("optional")


class _ThresholdLev1RisingEvent_Type(Integer32):
    """Custom type thresholdLev1RisingEvent based on Integer32"""
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
        *(("other", 1),
          ("partition-port", 2),
          ("partition-port-and-send-trap", 4),
          ("partition-port-and-send-trap-and-request-page", 6),
          ("send-trap", 3),
          ("send-trap-and-request-page", 5))
    )


_ThresholdLev1RisingEvent_Type.__name__ = "Integer32"
_ThresholdLev1RisingEvent_Object = MibTableColumn
thresholdLev1RisingEvent = _ThresholdLev1RisingEvent_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 6, 1, 1, 1, 11),
    _ThresholdLev1RisingEvent_Type()
)
thresholdLev1RisingEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdLev1RisingEvent.setStatus("optional")


class _ThresholdLev1FallingEvent_Type(Integer32):
    """Custom type thresholdLev1FallingEvent based on Integer32"""
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
        *(("other", 1),
          ("partition-port", 2),
          ("partition-port-and-send-trap", 4),
          ("partition-port-and-send-trap-and-request-page", 6),
          ("send-trap", 3),
          ("send-trap-and-request-page", 5))
    )


_ThresholdLev1FallingEvent_Type.__name__ = "Integer32"
_ThresholdLev1FallingEvent_Object = MibTableColumn
thresholdLev1FallingEvent = _ThresholdLev1FallingEvent_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 6, 1, 1, 1, 12),
    _ThresholdLev1FallingEvent_Type()
)
thresholdLev1FallingEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdLev1FallingEvent.setStatus("optional")
_ThresholdLev1Interval_Type = Integer32
_ThresholdLev1Interval_Object = MibTableColumn
thresholdLev1Interval = _ThresholdLev1Interval_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 6, 1, 1, 1, 13),
    _ThresholdLev1Interval_Type()
)
thresholdLev1Interval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdLev1Interval.setStatus("optional")


class _ThresholdLev1OwnerString_Type(OctetString):
    """Custom type thresholdLev1OwnerString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ThresholdLev1OwnerString_Type.__name__ = "OctetString"
_ThresholdLev1OwnerString_Object = MibTableColumn
thresholdLev1OwnerString = _ThresholdLev1OwnerString_Object(
    (1, 3, 6, 1, 4, 1, 298, 1, 3, 6, 1, 1, 1, 14),
    _ThresholdLev1OwnerString_Type()
)
thresholdLev1OwnerString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thresholdLev1OwnerString.setStatus("optional")
_ProductId_ObjectIdentity = ObjectIdentity
productId = _ProductId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 298, 2)
)
_AdapterProductId_ObjectIdentity = ObjectIdentity
adapterProductId = _AdapterProductId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 298, 2, 1)
)
_ConcProductId_ObjectIdentity = ObjectIdentity
concProductId = _ConcProductId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 298, 2, 2)
)
_Hub1012_ObjectIdentity = ObjectIdentity
hub1012 = _Hub1012_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 298, 2, 2, 1)
)
_Hub1012_bridge_ObjectIdentity = ObjectIdentity
hub1012_bridge = _Hub1012_bridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 298, 2, 2, 2)
)

# Managed Objects groups


# Notification objects

thresholdLev1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 298, 2, 2, 1, 0, 1)
)
thresholdLev1.setObjects(
      *(("ASANTE-AH1012-MIB", "thresholdLev1Target"),
        ("ASANTE-AH1012-MIB", "thresholdLev1GroupIndex"),
        ("ASANTE-AH1012-MIB", "thresholdLev1PortIndex"),
        ("ASANTE-AH1012-MIB", "thresholdLev1Subject"),
        ("ASANTE-AH1012-MIB", "thresholdLev1SampleType"),
        ("ASANTE-AH1012-MIB", "thresholdLev1WaterMark"),
        ("ASANTE-AH1012-MIB", "thresholdLev1DetectedValue"),
        ("ASANTE-AH1012-MIB", "thresholdLev1OwnerString"),
        ("ASANTE-AH1012-MIB", "thresholdLev1RisingEvent"),
        ("ASANTE-AH1012-MIB", "thresholdLev1FallingEvent"))
)
if mibBuilder.loadTexts:
    thresholdLev1.setStatus(
        ""
    )

nodeSecuLevel1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 298, 2, 2, 1, 0, 2)
)
if mibBuilder.loadTexts:
    nodeSecuLevel1.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASANTE-AH1012-MIB",
    **{"DisplayString": DisplayString,
       "PhysAddress": PhysAddress,
       "asante": asante,
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
       "adaptCard": adaptCard,
       "concentrator": concentrator,
       "concChassis": concChassis,
       "concBasicGrp": concBasicGrp,
       "concChassisType": concChassisType,
       "concChassisBkplType": concChassisBkplType,
       "concChassisBkplRev": concChassisBkplRev,
       "concChassisPsTable": concChassisPsTable,
       "concChassisPsEntry": concChassisPsEntry,
       "concChassisPsIndex": concChassisPsIndex,
       "concChassisPsModuleType": concChassisPsModuleType,
       "concChassisPsStatus": concChassisPsStatus,
       "concChassisFanStatus": concChassisFanStatus,
       "concChassisGroupCapacity": concChassisGroupCapacity,
       "concChassisGroupMap": concChassisGroupMap,
       "concChassisGrpTable": concChassisGrpTable,
       "concChassisGrpEntry": concChassisGrpEntry,
       "concChassisGrpIndex": concChassisGrpIndex,
       "concChassisGrpNumberPort": concChassisGrpNumberPort,
       "concChassisGrpType": concChassisGrpType,
       "concChassisGrpDescr": concChassisGrpDescr,
       "concChassisGrpHwRev": concChassisGrpHwRev,
       "concConfiguration": concConfiguration,
       "eSmartHubConfig": eSmartHubConfig,
       "eSmartHubId": eSmartHubId,
       "eSmartHubAssignedId": eSmartHubAssignedId,
       "eSmartHubTerSwitch": eSmartHubTerSwitch,
       "eSmartHubHwLoadPatStatus": eSmartHubHwLoadPatStatus,
       "eSmartHubHwLoadPatCapacity": eSmartHubHwLoadPatCapacity,
       "eSmartHubNodeAgeTimer": eSmartHubNodeAgeTimer,
       "eSmartHub3in1LnConStatus": eSmartHub3in1LnConStatus,
       "eSmartHub3in1StateCtrl": eSmartHub3in1StateCtrl,
       "concStatistics": concStatistics,
       "eStatistics": eStatistics,
       "eGlobalStatistics": eGlobalStatistics,
       "eGlobalHubReadableFrames": eGlobalHubReadableFrames,
       "eGlobalHubMcastFrames": eGlobalHubMcastFrames,
       "eGlobalHubBcastFrames": eGlobalHubBcastFrames,
       "eGlobalHubFrameTooLongs": eGlobalHubFrameTooLongs,
       "eGlobalHubRunts": eGlobalHubRunts,
       "eGlobalHubAlignmentErrors": eGlobalHubAlignmentErrors,
       "eGlobalHubFragmentErrors": eGlobalHubFragmentErrors,
       "eGlobalHubFCSErrors": eGlobalHubFCSErrors,
       "eGlobalHubIFGErrors": eGlobalHubIFGErrors,
       "eGlobalHubDataRateMismatchs": eGlobalHubDataRateMismatchs,
       "eGlobalHubShortEvents": eGlobalHubShortEvents,
       "eGlobalHubCollisions": eGlobalHubCollisions,
       "eGlobalHubLateCollisions": eGlobalHubLateCollisions,
       "eGlobalHubMJLPs": eGlobalHubMJLPs,
       "eGlobalHubAutoPartitions": eGlobalHubAutoPartitions,
       "eGlobalHubSFDMissings": eGlobalHubSFDMissings,
       "eGlobalHubBadFrames": eGlobalHubBadFrames,
       "eGrpStatisticsTable": eGrpStatisticsTable,
       "eGrpStatisticsEntry": eGrpStatisticsEntry,
       "eGrpStatIndex": eGrpStatIndex,
       "eGrpStatReadableFrames": eGrpStatReadableFrames,
       "eGrpStatMcastFrames": eGrpStatMcastFrames,
       "eGrpStatBcastFrames": eGrpStatBcastFrames,
       "eGrpStatFrameTooLongs": eGrpStatFrameTooLongs,
       "eGrpStatRunts": eGrpStatRunts,
       "eGrpStatAlignmentErrors": eGrpStatAlignmentErrors,
       "eGrpStatFragmentErrors": eGrpStatFragmentErrors,
       "eGrpStatFCSErrors": eGrpStatFCSErrors,
       "eGrpStatIFGErrors": eGrpStatIFGErrors,
       "eGrpStatDataRateMismatchs": eGrpStatDataRateMismatchs,
       "eGrpStatShortEvents": eGrpStatShortEvents,
       "eGrpStatCollisions": eGrpStatCollisions,
       "eGrpStatLateCollisions": eGrpStatLateCollisions,
       "eGrpStatMJLPs": eGrpStatMJLPs,
       "eGrpStatAutoPartitions": eGrpStatAutoPartitions,
       "eGrpStatSFDMissings": eGrpStatSFDMissings,
       "eGrpStatBadFrames": eGrpStatBadFrames,
       "ePortStatisticsTable": ePortStatisticsTable,
       "ePortStatisticsEntry": ePortStatisticsEntry,
       "ePortGrpIndex": ePortGrpIndex,
       "ePortIndex": ePortIndex,
       "ePortStatReadableFrames": ePortStatReadableFrames,
       "ePortStatMcastFrames": ePortStatMcastFrames,
       "ePortStatBcastFrames": ePortStatBcastFrames,
       "ePortStatFrameTooLongs": ePortStatFrameTooLongs,
       "ePortStatRunts": ePortStatRunts,
       "ePortStatAlignmentErrors": ePortStatAlignmentErrors,
       "ePortStatFragmentErrors": ePortStatFragmentErrors,
       "ePortStatFCSErrors": ePortStatFCSErrors,
       "ePortStatIFGErrors": ePortStatIFGErrors,
       "ePortStatDataRateMismatchs": ePortStatDataRateMismatchs,
       "ePortStatShortEvents": ePortStatShortEvents,
       "ePortStatCollisions": ePortStatCollisions,
       "ePortStatLateCollisions": ePortStatLateCollisions,
       "ePortStatMJLPs": ePortStatMJLPs,
       "ePortStatAutoPartitions": ePortStatAutoPartitions,
       "ePortStatSFDMissings": ePortStatSFDMissings,
       "ePortStatBadFrames": ePortStatBadFrames,
       "eTrafficMatrixTable": eTrafficMatrixTable,
       "eTrafficMatrixEntry": eTrafficMatrixEntry,
       "eTrafficMatrixLength": eTrafficMatrixLength,
       "eTrafficMatrixRange": eTrafficMatrixRange,
       "eTrafficMatrixFramesCounts": eTrafficMatrixFramesCounts,
       "eSpecific": eSpecific,
       "eSmartHubSpec": eSmartHubSpec,
       "eColGraphBar": eColGraphBar,
       "eUtilGraphBar": eUtilGraphBar,
       "ePortRateTable": ePortRateTable,
       "ePortRateEntry": ePortRateEntry,
       "ePortRateGrpIndex": ePortRateGrpIndex,
       "ePortRatePortIndex": ePortRatePortIndex,
       "ePortRateReadableFrames": ePortRateReadableFrames,
       "ePortRateMcastFrames": ePortRateMcastFrames,
       "ePortRateBcastFrames": ePortRateBcastFrames,
       "ePortRateFrameTooLongs": ePortRateFrameTooLongs,
       "ePortRateRunts": ePortRateRunts,
       "ePortRateAlignmentErrors": ePortRateAlignmentErrors,
       "ePortRateFragmentErrors": ePortRateFragmentErrors,
       "ePortRateFCSErrors": ePortRateFCSErrors,
       "ePortRateIFGErrors": ePortRateIFGErrors,
       "ePortRateDataRateMismatch": ePortRateDataRateMismatch,
       "ePortRateShortEvents": ePortRateShortEvents,
       "ePortRateCollisions": ePortRateCollisions,
       "ePortRateLateCollisions": ePortRateLateCollisions,
       "ePortRateMJLPs": ePortRateMJLPs,
       "ePortRateAutoPartitions": ePortRateAutoPartitions,
       "ePortRateSFDMissings": ePortRateSFDMissings,
       "ePortRateBadFrames": ePortRateBadFrames,
       "concStateCtrl": concStateCtrl,
       "eStateCtrl": eStateCtrl,
       "ePortStateCtrlTable": ePortStateCtrlTable,
       "ePortStateCtrlEntry": ePortStateCtrlEntry,
       "ePortStateGrpIndex": ePortStateGrpIndex,
       "ePortStatePortIndex": ePortStatePortIndex,
       "ePortStateType": ePortStateType,
       "ePortStateLinkStatus": ePortStateLinkStatus,
       "ePortStateLinkIntegTest": ePortStateLinkIntegTest,
       "ePortStateAutoPartStatus": ePortStateAutoPartStatus,
       "ePortStateJabberStatus": ePortStateJabberStatus,
       "ePortStateJabberState": ePortStateJabberState,
       "ePortStateAdminState": ePortStateAdminState,
       "ePortStateRDTState": ePortStateRDTState,
       "ePortStatePolarityStatus": ePortStatePolarityStatus,
       "ePortStatePolarityState": ePortStatePolarityState,
       "concNodeMgt": concNodeMgt,
       "nodeSummaryTable": nodeSummaryTable,
       "nodeSummaryEntry": nodeSummaryEntry,
       "nodeSummaryGrpIndex": nodeSummaryGrpIndex,
       "nodeSummaryPortIndex": nodeSummaryPortIndex,
       "nodeSummarySrcMacAddr": nodeSummarySrcMacAddr,
       "nodeSummaryDestMacAddr": nodeSummaryDestMacAddr,
       "nodeSummaryEtherType": nodeSummaryEtherType,
       "nodeSummaryIpAddrPair": nodeSummaryIpAddrPair,
       "nodeSummaryTimeStamp": nodeSummaryTimeStamp,
       "nodeSecurity": nodeSecurity,
       "nodeSecuLev1Table": nodeSecuLev1Table,
       "nodeSecuLev1Entry": nodeSecuLev1Entry,
       "nodeSecuLev1GrpIndex": nodeSecuLev1GrpIndex,
       "nodeSecuLev1PortIndex": nodeSecuLev1PortIndex,
       "nodeSecuLev1Status": nodeSecuLev1Status,
       "nodeSecuLev1AllowedAddr": nodeSecuLev1AllowedAddr,
       "nodeSecuLev1Action": nodeSecuLev1Action,
       "concAlarmMgt": concAlarmMgt,
       "thresholdAlarm": thresholdAlarm,
       "thresholdLev1Table": thresholdLev1Table,
       "thresholdLev1Entry": thresholdLev1Entry,
       "thresholdLev1Index": thresholdLev1Index,
       "thresholdLev1Status": thresholdLev1Status,
       "thresholdLev1Target": thresholdLev1Target,
       "thresholdLev1GroupIndex": thresholdLev1GroupIndex,
       "thresholdLev1PortIndex": thresholdLev1PortIndex,
       "thresholdLev1Subject": thresholdLev1Subject,
       "thresholdLev1SampleType": thresholdLev1SampleType,
       "thresholdLev1StartupAlarm": thresholdLev1StartupAlarm,
       "thresholdLev1WaterMark": thresholdLev1WaterMark,
       "thresholdLev1DetectedValue": thresholdLev1DetectedValue,
       "thresholdLev1RisingEvent": thresholdLev1RisingEvent,
       "thresholdLev1FallingEvent": thresholdLev1FallingEvent,
       "thresholdLev1Interval": thresholdLev1Interval,
       "thresholdLev1OwnerString": thresholdLev1OwnerString,
       "productId": productId,
       "adapterProductId": adapterProductId,
       "concProductId": concProductId,
       "hub1012": hub1012,
       "thresholdLev1": thresholdLev1,
       "nodeSecuLevel1": nodeSecuLevel1,
       "hub1012-bridge": hub1012_bridge}
)
