# SNMP MIB module (DES2218-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DES2218-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:24:48 2024
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

_Dlink_ObjectIdentity = ObjectIdentity
dlink = _Dlink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171)
)
_Dlink_products_ObjectIdentity = ObjectIdentity
dlink_products = _Dlink_products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10)
)
_Dlink_Des2218Prod_ObjectIdentity = ObjectIdentity
dlink_Des2218Prod = _Dlink_Des2218Prod_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 7)
)
_Dlink_Des2218ProdId_ObjectIdentity = ObjectIdentity
dlink_Des2218ProdId = _Dlink_Des2218ProdId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 7, 1)
)
_Des2218SwHub_ObjectIdentity = ObjectIdentity
des2218SwHub = _Des2218SwHub_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 7, 2)
)
_Dlink_mgmt_ObjectIdentity = ObjectIdentity
dlink_mgmt = _Dlink_mgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11)
)
_AgentConfigInfo_ObjectIdentity = ObjectIdentity
agentConfigInfo = _AgentConfigInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 1)
)
_AgentBasicInfo_ObjectIdentity = ObjectIdentity
agentBasicInfo = _AgentBasicInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 1, 1)
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
    (1, 3, 6, 1, 4, 1, 171, 11, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 1, 1, 2),
    _AgentPromFwVersion_Type()
)
agentPromFwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentPromFwVersion.setStatus("mandatory")


class _AgentHwRevision_Type(DisplayString):
    """Custom type agentHwRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_AgentHwRevision_Type.__name__ = "DisplayString"
_AgentHwRevision_Object = MibScalar
agentHwRevision = _AgentHwRevision_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 1, 1, 4),
    _AgentMgmtProtocolCapability_Type()
)
agentMgmtProtocolCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMgmtProtocolCapability.setStatus("mandatory")
_AgentMibCapabilityTable_Object = MibTable
agentMibCapabilityTable = _AgentMibCapabilityTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 1, 1, 5)
)
if mibBuilder.loadTexts:
    agentMibCapabilityTable.setStatus("mandatory")
_AgentMibCapabilityEntry_Object = MibTableRow
agentMibCapabilityEntry = _AgentMibCapabilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 1, 1, 5, 1)
)
agentMibCapabilityEntry.setIndexNames(
    (0, "DES2218-MIB", "agentMibCapabilityIndex"),
)
if mibBuilder.loadTexts:
    agentMibCapabilityEntry.setStatus("mandatory")
_AgentMibCapabilityIndex_Type = Integer32
_AgentMibCapabilityIndex_Object = MibTableColumn
agentMibCapabilityIndex = _AgentMibCapabilityIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 1, 1, 5, 1, 1),
    _AgentMibCapabilityIndex_Type()
)
agentMibCapabilityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMibCapabilityIndex.setStatus("mandatory")


class _AgentMibCapabilityDescr_Type(DisplayString):
    """Custom type agentMibCapabilityDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AgentMibCapabilityDescr_Type.__name__ = "DisplayString"
_AgentMibCapabilityDescr_Object = MibTableColumn
agentMibCapabilityDescr = _AgentMibCapabilityDescr_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 1, 1, 5, 1, 2),
    _AgentMibCapabilityDescr_Type()
)
agentMibCapabilityDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMibCapabilityDescr.setStatus("mandatory")
_AgentMibCapabilityVersion_Type = Integer32
_AgentMibCapabilityVersion_Object = MibTableColumn
agentMibCapabilityVersion = _AgentMibCapabilityVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 1, 1, 5, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 1, 1, 5, 1, 4),
    _AgentMibCapabilityType_Type()
)
agentMibCapabilityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentMibCapabilityType.setStatus("mandatory")
_AgentBasicConfig_ObjectIdentity = ObjectIdentity
agentBasicConfig = _AgentBasicConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 1, 2)
)


class _AgentSwUpdateMode_Type(Integer32):
    """Custom type agentSwUpdateMode based on Integer32"""
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


_AgentSwUpdateMode_Type.__name__ = "Integer32"
_AgentSwUpdateMode_Object = MibScalar
agentSwUpdateMode = _AgentSwUpdateMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 1, 2, 1),
    _AgentSwUpdateMode_Type()
)
agentSwUpdateMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwUpdateMode.setStatus("mandatory")


class _AgentSwUpdateCtrl_Type(Integer32):
    """Custom type agentSwUpdateCtrl based on Integer32"""
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


_AgentSwUpdateCtrl_Type.__name__ = "Integer32"
_AgentSwUpdateCtrl_Object = MibScalar
agentSwUpdateCtrl = _AgentSwUpdateCtrl_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 1, 2, 2),
    _AgentSwUpdateCtrl_Type()
)
agentSwUpdateCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSwUpdateCtrl.setStatus("mandatory")


class _AgentBootFile_Type(DisplayString):
    """Custom type agentBootFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AgentBootFile_Type.__name__ = "DisplayString"
_AgentBootFile_Object = MibScalar
agentBootFile = _AgentBootFile_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 1, 2, 3),
    _AgentBootFile_Type()
)
agentBootFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentBootFile.setStatus("mandatory")


class _AgentSystemReset_Type(Integer32):
    """Custom type agentSystemReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no-reset", 3),
          ("other", 1),
          ("reset", 2))
    )


_AgentSystemReset_Type.__name__ = "Integer32"
_AgentSystemReset_Object = MibScalar
agentSystemReset = _AgentSystemReset_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 1, 2, 4),
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
              3)
        )
    )
    namedValues = NamedValues(
        *(("console", 2),
          ("other", 1),
          ("out-of-band", 3))
    )


_AgentRs232PortConfig_Type.__name__ = "Integer32"
_AgentRs232PortConfig_Object = MibScalar
agentRs232PortConfig = _AgentRs232PortConfig_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 1, 2, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 1, 2, 6),
    _AgentOutOfBandBaudRateConfig_Type()
)
agentOutOfBandBaudRateConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentOutOfBandBaudRateConfig.setStatus("mandatory")


class _AgentOutOfBandDialNumber_Type(DisplayString):
    """Custom type agentOutOfBandDialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AgentOutOfBandDialNumber_Type.__name__ = "DisplayString"
_AgentOutOfBandDialNumber_Object = MibScalar
agentOutOfBandDialNumber = _AgentOutOfBandDialNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 1, 2, 7),
    _AgentOutOfBandDialNumber_Type()
)
agentOutOfBandDialNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentOutOfBandDialNumber.setStatus("mandatory")
_AgentIpProtoConfig_ObjectIdentity = ObjectIdentity
agentIpProtoConfig = _AgentIpProtoConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 1, 3)
)
_AgentIpNumOfIf_Type = Integer32
_AgentIpNumOfIf_Object = MibScalar
agentIpNumOfIf = _AgentIpNumOfIf_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 1, 3, 1),
    _AgentIpNumOfIf_Type()
)
agentIpNumOfIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIpNumOfIf.setStatus("mandatory")
_AgentIpIfTable_Object = MibTable
agentIpIfTable = _AgentIpIfTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 1, 3, 2)
)
if mibBuilder.loadTexts:
    agentIpIfTable.setStatus("mandatory")
_AgentIpIfEntry_Object = MibTableRow
agentIpIfEntry = _AgentIpIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 1, 3, 2, 1)
)
agentIpIfEntry.setIndexNames(
    (0, "DES2218-MIB", "agentIpIfIndex"),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 1, 3, 2, 1, 1),
    _AgentIpIfIndex_Type()
)
agentIpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIpIfIndex.setStatus("mandatory")
_AgentIpIfAddress_Type = IpAddress
_AgentIpIfAddress_Object = MibTableColumn
agentIpIfAddress = _AgentIpIfAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 1, 3, 2, 1, 2),
    _AgentIpIfAddress_Type()
)
agentIpIfAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIpIfAddress.setStatus("mandatory")
_AgentIpIfNetMask_Type = IpAddress
_AgentIpIfNetMask_Object = MibTableColumn
agentIpIfNetMask = _AgentIpIfNetMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 1, 3, 2, 1, 3),
    _AgentIpIfNetMask_Type()
)
agentIpIfNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIpIfNetMask.setStatus("mandatory")
_AgentIpIfDefaultRouter_Type = IpAddress
_AgentIpIfDefaultRouter_Object = MibTableColumn
agentIpIfDefaultRouter = _AgentIpIfDefaultRouter_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 1, 3, 2, 1, 4),
    _AgentIpIfDefaultRouter_Type()
)
agentIpIfDefaultRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIpIfDefaultRouter.setStatus("mandatory")
_AgentIpIfMacAddr_Type = PhysAddress
_AgentIpIfMacAddr_Object = MibTableColumn
agentIpIfMacAddr = _AgentIpIfMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 1, 3, 2, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 1, 3, 2, 1, 6),
    _AgentIpIfType_Type()
)
agentIpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIpIfType.setStatus("mandatory")
_AgentIpBootServerAddr_Type = IpAddress
_AgentIpBootServerAddr_Object = MibScalar
agentIpBootServerAddr = _AgentIpBootServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 1, 3, 3),
    _AgentIpBootServerAddr_Type()
)
agentIpBootServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIpBootServerAddr.setStatus("mandatory")


class _AgentIpBootProtocol_Type(Integer32):
    """Custom type agentIpBootProtocol based on Integer32"""
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
          ("tftp", 3))
    )


_AgentIpBootProtocol_Type.__name__ = "Integer32"
_AgentIpBootProtocol_Object = MibScalar
agentIpBootProtocol = _AgentIpBootProtocol_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 1, 3, 4),
    _AgentIpBootProtocol_Type()
)
agentIpBootProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIpBootProtocol.setStatus("mandatory")


class _AgentIpGetIpFromBootpServer_Type(Integer32):
    """Custom type agentIpGetIpFromBootpServer based on Integer32"""
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


_AgentIpGetIpFromBootpServer_Type.__name__ = "Integer32"
_AgentIpGetIpFromBootpServer_Object = MibScalar
agentIpGetIpFromBootpServer = _AgentIpGetIpFromBootpServer_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 1, 3, 5),
    _AgentIpGetIpFromBootpServer_Type()
)
agentIpGetIpFromBootpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIpGetIpFromBootpServer.setStatus("mandatory")
_AgentIpUnauthAddr_Type = IpAddress
_AgentIpUnauthAddr_Object = MibScalar
agentIpUnauthAddr = _AgentIpUnauthAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 1, 3, 6),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 1, 3, 7),
    _AgentIpUnauthComm_Type()
)
agentIpUnauthComm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIpUnauthComm.setStatus("mandatory")
_AgentIpLastBootServerAddr_Type = IpAddress
_AgentIpLastBootServerAddr_Object = MibScalar
agentIpLastBootServerAddr = _AgentIpLastBootServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 1, 3, 8),
    _AgentIpLastBootServerAddr_Type()
)
agentIpLastBootServerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIpLastBootServerAddr.setStatus("mandatory")
_AgentIpLastIpAddr_Type = IpAddress
_AgentIpLastIpAddr_Object = MibScalar
agentIpLastIpAddr = _AgentIpLastIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 1, 3, 9),
    _AgentIpLastIpAddr_Type()
)
agentIpLastIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentIpLastIpAddr.setStatus("mandatory")
_AgentIpTrapManagerTable_Object = MibTable
agentIpTrapManagerTable = _AgentIpTrapManagerTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 1, 3, 10)
)
if mibBuilder.loadTexts:
    agentIpTrapManagerTable.setStatus("mandatory")
_AgentIpTrapManagerEntry_Object = MibTableRow
agentIpTrapManagerEntry = _AgentIpTrapManagerEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 1, 3, 10, 1)
)
agentIpTrapManagerEntry.setIndexNames(
    (0, "DES2218-MIB", "agentIpTrapManagerIpAddr"),
)
if mibBuilder.loadTexts:
    agentIpTrapManagerEntry.setStatus("mandatory")
_AgentIpTrapManagerIpAddr_Type = IpAddress
_AgentIpTrapManagerIpAddr_Object = MibTableColumn
agentIpTrapManagerIpAddr = _AgentIpTrapManagerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 1, 3, 10, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 1, 3, 10, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 171, 11, 1, 3, 10, 1, 3),
    _AgentIpTrapManagerStatus_Type()
)
agentIpTrapManagerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentIpTrapManagerStatus.setStatus("mandatory")
_Des2218series_ObjectIdentity = ObjectIdentity
des2218series = _Des2218series_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 7)
)
_Des2218MIB_ObjectIdentity = ObjectIdentity
des2218MIB = _Des2218MIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 7, 1)
)
_SwDevicePackage_ObjectIdentity = ObjectIdentity
swDevicePackage = _SwDevicePackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 1)
)
_SwDeviceInfo_ObjectIdentity = ObjectIdentity
swDeviceInfo = _SwDeviceInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 1, 1)
)
_SwDevInfoTotalNumOfPort_Type = Integer32
_SwDevInfoTotalNumOfPort_Object = MibScalar
swDevInfoTotalNumOfPort = _SwDevInfoTotalNumOfPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 1, 1, 1),
    _SwDevInfoTotalNumOfPort_Type()
)
swDevInfoTotalNumOfPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDevInfoTotalNumOfPort.setStatus("mandatory")
_SwDevInfoNumOfPortOnUse_Type = Integer32
_SwDevInfoNumOfPortOnUse_Object = MibScalar
swDevInfoNumOfPortOnUse = _SwDevInfoNumOfPortOnUse_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 1, 1, 2),
    _SwDevInfoNumOfPortOnUse_Type()
)
swDevInfoNumOfPortOnUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDevInfoNumOfPortOnUse.setStatus("mandatory")


class _SwDevInfoDesc_Type(DisplayString):
    """Custom type swDevInfoDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SwDevInfoDesc_Type.__name__ = "DisplayString"
_SwDevInfoDesc_Object = MibScalar
swDevInfoDesc = _SwDevInfoDesc_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 1, 1, 3),
    _SwDevInfoDesc_Type()
)
swDevInfoDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDevInfoDesc.setStatus("mandatory")


class _SwDevInfoPortType_Type(Integer32):
    """Custom type swDevInfoPortType based on Integer32"""
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
        *(("other", 1),
          ("portType-AUI", 3),
          ("portType-BNC", 5),
          ("portType-Fiber", 4),
          ("portType-Option-module-100Bridge", 7),
          ("portType-Option-module-RAS", 6),
          ("portType-UTP", 2))
    )


_SwDevInfoPortType_Type.__name__ = "Integer32"
_SwDevInfoPortType_Object = MibScalar
swDevInfoPortType = _SwDevInfoPortType_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 1, 1, 4),
    _SwDevInfoPortType_Type()
)
swDevInfoPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDevInfoPortType.setStatus("mandatory")


class _SwDevInfoHwRev_Type(DisplayString):
    """Custom type swDevInfoHwRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_SwDevInfoHwRev_Type.__name__ = "DisplayString"
_SwDevInfoHwRev_Object = MibScalar
swDevInfoHwRev = _SwDevInfoHwRev_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 1, 1, 5),
    _SwDevInfoHwRev_Type()
)
swDevInfoHwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDevInfoHwRev.setStatus("mandatory")
_SwDevInfoSystemUpTime_Type = TimeTicks
_SwDevInfoSystemUpTime_Object = MibScalar
swDevInfoSystemUpTime = _SwDevInfoSystemUpTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 1, 1, 6),
    _SwDevInfoSystemUpTime_Type()
)
swDevInfoSystemUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDevInfoSystemUpTime.setStatus("mandatory")


class _SwDevInfoFrontPanelLedStatus_Type(OctetString):
    """Custom type swDevInfoFrontPanelLedStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_SwDevInfoFrontPanelLedStatus_Type.__name__ = "OctetString"
_SwDevInfoFrontPanelLedStatus_Object = MibScalar
swDevInfoFrontPanelLedStatus = _SwDevInfoFrontPanelLedStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 1, 1, 7),
    _SwDevInfoFrontPanelLedStatus_Type()
)
swDevInfoFrontPanelLedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDevInfoFrontPanelLedStatus.setStatus("mandatory")
_SwDevInfoDramSize_Type = Integer32
_SwDevInfoDramSize_Object = MibScalar
swDevInfoDramSize = _SwDevInfoDramSize_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 1, 1, 8),
    _SwDevInfoDramSize_Type()
)
swDevInfoDramSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swDevInfoDramSize.setStatus("mandatory")
_SwDeviceCtl_ObjectIdentity = ObjectIdentity
swDeviceCtl = _SwDeviceCtl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 1, 2)
)


class _SwDevCtrlDisableLearningState_Type(Integer32):
    """Custom type swDevCtrlDisableLearningState based on Integer32"""
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


_SwDevCtrlDisableLearningState_Type.__name__ = "Integer32"
_SwDevCtrlDisableLearningState_Object = MibScalar
swDevCtrlDisableLearningState = _SwDevCtrlDisableLearningState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 1, 2, 1),
    _SwDevCtrlDisableLearningState_Type()
)
swDevCtrlDisableLearningState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDevCtrlDisableLearningState.setStatus("mandatory")


class _SwDevCtrlReset_Type(Integer32):
    """Custom type swDevCtrlReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no-reset", 3),
          ("other", 1),
          ("reset", 2))
    )


_SwDevCtrlReset_Type.__name__ = "Integer32"
_SwDevCtrlReset_Object = MibScalar
swDevCtrlReset = _SwDevCtrlReset_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 1, 2, 2),
    _SwDevCtrlReset_Type()
)
swDevCtrlReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDevCtrlReset.setStatus("mandatory")


class _SwDevCtrlSpanningTree_Type(Integer32):
    """Custom type swDevCtrlSpanningTree based on Integer32"""
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


_SwDevCtrlSpanningTree_Type.__name__ = "Integer32"
_SwDevCtrlSpanningTree_Object = MibScalar
swDevCtrlSpanningTree = _SwDevCtrlSpanningTree_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 1, 2, 3),
    _SwDevCtrlSpanningTree_Type()
)
swDevCtrlSpanningTree.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swDevCtrlSpanningTree.setStatus("mandatory")
_SwPortPackage_ObjectIdentity = ObjectIdentity
swPortPackage = _SwPortPackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2)
)
_SwPortInfoTable_Object = MibTable
swPortInfoTable = _SwPortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 1)
)
if mibBuilder.loadTexts:
    swPortInfoTable.setStatus("mandatory")
_SwPortInfoEntry_Object = MibTableRow
swPortInfoEntry = _SwPortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 1, 1)
)
swPortInfoEntry.setIndexNames(
    (0, "DES2218-MIB", "swPortInfoGroupIndex"),
    (0, "DES2218-MIB", "swPortInfoIndex"),
)
if mibBuilder.loadTexts:
    swPortInfoEntry.setStatus("mandatory")
_SwPortInfoGroupIndex_Type = Integer32
_SwPortInfoGroupIndex_Object = MibTableColumn
swPortInfoGroupIndex = _SwPortInfoGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 1, 1, 1),
    _SwPortInfoGroupIndex_Type()
)
swPortInfoGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortInfoGroupIndex.setStatus("mandatory")
_SwPortInfoIndex_Type = Integer32
_SwPortInfoIndex_Object = MibTableColumn
swPortInfoIndex = _SwPortInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 1, 1, 2),
    _SwPortInfoIndex_Type()
)
swPortInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortInfoIndex.setStatus("mandatory")


class _SwPortInfoType_Type(Integer32):
    """Custom type swPortInfoType based on Integer32"""
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
        *(("other", 1),
          ("portType-AUI", 3),
          ("portType-BNC", 5),
          ("portType-Fiber", 4),
          ("portType-Option-module-100Bridge", 7),
          ("portType-Option-module-RAS", 6),
          ("portType-UTP", 2))
    )


_SwPortInfoType_Type.__name__ = "Integer32"
_SwPortInfoType_Object = MibTableColumn
swPortInfoType = _SwPortInfoType_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 1, 1, 3),
    _SwPortInfoType_Type()
)
swPortInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortInfoType.setStatus("mandatory")


class _SwPortInfoPartitionStatus_Type(Integer32):
    """Custom type swPortInfoPartitionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no-partion", 2),
          ("other", 1),
          ("partion", 3))
    )


_SwPortInfoPartitionStatus_Type.__name__ = "Integer32"
_SwPortInfoPartitionStatus_Object = MibTableColumn
swPortInfoPartitionStatus = _SwPortInfoPartitionStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 1, 1, 4),
    _SwPortInfoPartitionStatus_Type()
)
swPortInfoPartitionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortInfoPartitionStatus.setStatus("mandatory")


class _SwPortInfoLinkStatus_Type(Integer32):
    """Custom type swPortInfoLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("link-fail", 3),
          ("link-pass", 2),
          ("other", 1))
    )


_SwPortInfoLinkStatus_Type.__name__ = "Integer32"
_SwPortInfoLinkStatus_Object = MibTableColumn
swPortInfoLinkStatus = _SwPortInfoLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 1, 1, 5),
    _SwPortInfoLinkStatus_Type()
)
swPortInfoLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortInfoLinkStatus.setStatus("mandatory")


class _SwPortInfoDuplexMode_Type(Integer32):
    """Custom type swPortInfoDuplexMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full", 3),
          ("half", 2),
          ("other", 1))
    )


_SwPortInfoDuplexMode_Type.__name__ = "Integer32"
_SwPortInfoDuplexMode_Object = MibTableColumn
swPortInfoDuplexMode = _SwPortInfoDuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 1, 1, 6),
    _SwPortInfoDuplexMode_Type()
)
swPortInfoDuplexMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortInfoDuplexMode.setStatus("mandatory")


class _SwPortInfoNegotiationStatus_Type(Integer32):
    """Custom type swPortInfoNegotiationStatus based on Integer32"""
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


_SwPortInfoNegotiationStatus_Type.__name__ = "Integer32"
_SwPortInfoNegotiationStatus_Object = MibTableColumn
swPortInfoNegotiationStatus = _SwPortInfoNegotiationStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 1, 1, 7),
    _SwPortInfoNegotiationStatus_Type()
)
swPortInfoNegotiationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortInfoNegotiationStatus.setStatus("mandatory")


class _SwPortInfoSpeedStatus_Type(Integer32):
    """Custom type swPortInfoSpeedStatus based on Integer32"""
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
          ("speed-100M", 3),
          ("speed-10M", 2))
    )


_SwPortInfoSpeedStatus_Type.__name__ = "Integer32"
_SwPortInfoSpeedStatus_Object = MibTableColumn
swPortInfoSpeedStatus = _SwPortInfoSpeedStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 1, 1, 8),
    _SwPortInfoSpeedStatus_Type()
)
swPortInfoSpeedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortInfoSpeedStatus.setStatus("mandatory")
_SwPortCtrlTable_Object = MibTable
swPortCtrlTable = _SwPortCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 2)
)
if mibBuilder.loadTexts:
    swPortCtrlTable.setStatus("mandatory")
_SwPortCtrlEntry_Object = MibTableRow
swPortCtrlEntry = _SwPortCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 2, 1)
)
swPortCtrlEntry.setIndexNames(
    (0, "DES2218-MIB", "swPortCtrlGroupIndex"),
    (0, "DES2218-MIB", "swPortCtrlIndex"),
)
if mibBuilder.loadTexts:
    swPortCtrlEntry.setStatus("mandatory")
_SwPortCtrlGroupIndex_Type = Integer32
_SwPortCtrlGroupIndex_Object = MibTableColumn
swPortCtrlGroupIndex = _SwPortCtrlGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 2, 1, 1),
    _SwPortCtrlGroupIndex_Type()
)
swPortCtrlGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortCtrlGroupIndex.setStatus("mandatory")
_SwPortCtrlIndex_Type = Integer32
_SwPortCtrlIndex_Object = MibTableColumn
swPortCtrlIndex = _SwPortCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 2, 1, 2),
    _SwPortCtrlIndex_Type()
)
swPortCtrlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortCtrlIndex.setStatus("mandatory")


class _SwPortCtrlAdminState_Type(Integer32):
    """Custom type swPortCtrlAdminState based on Integer32"""
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


_SwPortCtrlAdminState_Type.__name__ = "Integer32"
_SwPortCtrlAdminState_Object = MibTableColumn
swPortCtrlAdminState = _SwPortCtrlAdminState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 2, 1, 3),
    _SwPortCtrlAdminState_Type()
)
swPortCtrlAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortCtrlAdminState.setStatus("mandatory")


class _SwPortCtrlDuplexState_Type(Integer32):
    """Custom type swPortCtrlDuplexState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full", 3),
          ("half", 2),
          ("other", 1))
    )


_SwPortCtrlDuplexState_Type.__name__ = "Integer32"
_SwPortCtrlDuplexState_Object = MibTableColumn
swPortCtrlDuplexState = _SwPortCtrlDuplexState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 2, 1, 4),
    _SwPortCtrlDuplexState_Type()
)
swPortCtrlDuplexState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortCtrlDuplexState.setStatus("mandatory")


class _SwPortCtrlLinkStatusAlarmState_Type(Integer32):
    """Custom type swPortCtrlLinkStatusAlarmState based on Integer32"""
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


_SwPortCtrlLinkStatusAlarmState_Type.__name__ = "Integer32"
_SwPortCtrlLinkStatusAlarmState_Object = MibTableColumn
swPortCtrlLinkStatusAlarmState = _SwPortCtrlLinkStatusAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 2, 1, 5),
    _SwPortCtrlLinkStatusAlarmState_Type()
)
swPortCtrlLinkStatusAlarmState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortCtrlLinkStatusAlarmState.setStatus("mandatory")


class _SwPortCtrlFilterBcastState_Type(Integer32):
    """Custom type swPortCtrlFilterBcastState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("discard", 3),
          ("forward", 2),
          ("other", 1))
    )


_SwPortCtrlFilterBcastState_Type.__name__ = "Integer32"
_SwPortCtrlFilterBcastState_Object = MibTableColumn
swPortCtrlFilterBcastState = _SwPortCtrlFilterBcastState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 2, 1, 6),
    _SwPortCtrlFilterBcastState_Type()
)
swPortCtrlFilterBcastState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortCtrlFilterBcastState.setStatus("mandatory")


class _SwPortCtrlForwardUnknowState_Type(Integer32):
    """Custom type swPortCtrlForwardUnknowState based on Integer32"""
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


_SwPortCtrlForwardUnknowState_Type.__name__ = "Integer32"
_SwPortCtrlForwardUnknowState_Object = MibTableColumn
swPortCtrlForwardUnknowState = _SwPortCtrlForwardUnknowState_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 2, 1, 7),
    _SwPortCtrlForwardUnknowState_Type()
)
swPortCtrlForwardUnknowState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortCtrlForwardUnknowState.setStatus("mandatory")


class _SwPortCtrlPartitionStatus_Type(Integer32):
    """Custom type swPortCtrlPartitionStatus based on Integer32"""
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


_SwPortCtrlPartitionStatus_Type.__name__ = "Integer32"
_SwPortCtrlPartitionStatus_Object = MibTableColumn
swPortCtrlPartitionStatus = _SwPortCtrlPartitionStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 2, 1, 8),
    _SwPortCtrlPartitionStatus_Type()
)
swPortCtrlPartitionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortCtrlPartitionStatus.setStatus("mandatory")


class _SwPortCtrlNegotiationStatus_Type(Integer32):
    """Custom type swPortCtrlNegotiationStatus based on Integer32"""
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


_SwPortCtrlNegotiationStatus_Type.__name__ = "Integer32"
_SwPortCtrlNegotiationStatus_Object = MibTableColumn
swPortCtrlNegotiationStatus = _SwPortCtrlNegotiationStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 2, 1, 9),
    _SwPortCtrlNegotiationStatus_Type()
)
swPortCtrlNegotiationStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortCtrlNegotiationStatus.setStatus("mandatory")


class _SwPortCtrlSpeedStatus_Type(Integer32):
    """Custom type swPortCtrlSpeedStatus based on Integer32"""
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
          ("speed-100M", 3),
          ("speed-10M", 2))
    )


_SwPortCtrlSpeedStatus_Type.__name__ = "Integer32"
_SwPortCtrlSpeedStatus_Object = MibTableColumn
swPortCtrlSpeedStatus = _SwPortCtrlSpeedStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 2, 1, 10),
    _SwPortCtrlSpeedStatus_Type()
)
swPortCtrlSpeedStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortCtrlSpeedStatus.setStatus("mandatory")
_SwPortCounterTable_Object = MibTable
swPortCounterTable = _SwPortCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 3)
)
if mibBuilder.loadTexts:
    swPortCounterTable.setStatus("mandatory")
_SwPortCounterEntry_Object = MibTableRow
swPortCounterEntry = _SwPortCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 3, 1)
)
swPortCounterEntry.setIndexNames(
    (0, "DES2218-MIB", "swPortCounterGroupIndex"),
    (0, "DES2218-MIB", "swPortCounterIndex"),
)
if mibBuilder.loadTexts:
    swPortCounterEntry.setStatus("mandatory")
_SwPortCounterGroupIndex_Type = Integer32
_SwPortCounterGroupIndex_Object = MibTableColumn
swPortCounterGroupIndex = _SwPortCounterGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 3, 1, 1),
    _SwPortCounterGroupIndex_Type()
)
swPortCounterGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortCounterGroupIndex.setStatus("mandatory")
_SwPortCounterIndex_Type = Integer32
_SwPortCounterIndex_Object = MibTableColumn
swPortCounterIndex = _SwPortCounterIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 3, 1, 2),
    _SwPortCounterIndex_Type()
)
swPortCounterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortCounterIndex.setStatus("mandatory")
_SwPortBytesReceived_Type = Counter32
_SwPortBytesReceived_Object = MibTableColumn
swPortBytesReceived = _SwPortBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 3, 1, 3),
    _SwPortBytesReceived_Type()
)
swPortBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortBytesReceived.setStatus("mandatory")
_SwPortBytesSent_Type = Counter32
_SwPortBytesSent_Object = MibTableColumn
swPortBytesSent = _SwPortBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 3, 1, 4),
    _SwPortBytesSent_Type()
)
swPortBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortBytesSent.setStatus("mandatory")
_SwPortFramesReceived_Type = Counter32
_SwPortFramesReceived_Object = MibTableColumn
swPortFramesReceived = _SwPortFramesReceived_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 3, 1, 5),
    _SwPortFramesReceived_Type()
)
swPortFramesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortFramesReceived.setStatus("mandatory")
_SwPortFramesSent_Type = Counter32
_SwPortFramesSent_Object = MibTableColumn
swPortFramesSent = _SwPortFramesSent_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 3, 1, 6),
    _SwPortFramesSent_Type()
)
swPortFramesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortFramesSent.setStatus("mandatory")
_SwPortTotalBytesReceived_Type = Counter32
_SwPortTotalBytesReceived_Object = MibTableColumn
swPortTotalBytesReceived = _SwPortTotalBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 3, 1, 7),
    _SwPortTotalBytesReceived_Type()
)
swPortTotalBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortTotalBytesReceived.setStatus("mandatory")
_SwPortTotalFramesReceived_Type = Counter32
_SwPortTotalFramesReceived_Object = MibTableColumn
swPortTotalFramesReceived = _SwPortTotalFramesReceived_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 3, 1, 8),
    _SwPortTotalFramesReceived_Type()
)
swPortTotalFramesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortTotalFramesReceived.setStatus("mandatory")
_SwPortBroadcastFramesReceived_Type = Counter32
_SwPortBroadcastFramesReceived_Object = MibTableColumn
swPortBroadcastFramesReceived = _SwPortBroadcastFramesReceived_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 3, 1, 9),
    _SwPortBroadcastFramesReceived_Type()
)
swPortBroadcastFramesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortBroadcastFramesReceived.setStatus("mandatory")
_SwPortMulticastFramesReceived_Type = Counter32
_SwPortMulticastFramesReceived_Object = MibTableColumn
swPortMulticastFramesReceived = _SwPortMulticastFramesReceived_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 3, 1, 10),
    _SwPortMulticastFramesReceived_Type()
)
swPortMulticastFramesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortMulticastFramesReceived.setStatus("mandatory")
_SwPortCRCError_Type = Counter32
_SwPortCRCError_Object = MibTableColumn
swPortCRCError = _SwPortCRCError_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 3, 1, 11),
    _SwPortCRCError_Type()
)
swPortCRCError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortCRCError.setStatus("mandatory")
_SwPortOversizeFrames_Type = Counter32
_SwPortOversizeFrames_Object = MibTableColumn
swPortOversizeFrames = _SwPortOversizeFrames_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 3, 1, 12),
    _SwPortOversizeFrames_Type()
)
swPortOversizeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortOversizeFrames.setStatus("mandatory")
_SwPortFragments_Type = Counter32
_SwPortFragments_Object = MibTableColumn
swPortFragments = _SwPortFragments_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 3, 1, 13),
    _SwPortFragments_Type()
)
swPortFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortFragments.setStatus("mandatory")
_SwPortJabber_Type = Counter32
_SwPortJabber_Object = MibTableColumn
swPortJabber = _SwPortJabber_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 3, 1, 14),
    _SwPortJabber_Type()
)
swPortJabber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortJabber.setStatus("mandatory")
_SwPortCollision_Type = Counter32
_SwPortCollision_Object = MibTableColumn
swPortCollision = _SwPortCollision_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 3, 1, 15),
    _SwPortCollision_Type()
)
swPortCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortCollision.setStatus("mandatory")
_SwPortLateCollision_Type = Counter32
_SwPortLateCollision_Object = MibTableColumn
swPortLateCollision = _SwPortLateCollision_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 3, 1, 16),
    _SwPortLateCollision_Type()
)
swPortLateCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortLateCollision.setStatus("mandatory")
_SwPortFrames64Bytes_Type = Counter32
_SwPortFrames64Bytes_Object = MibTableColumn
swPortFrames64Bytes = _SwPortFrames64Bytes_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 3, 1, 17),
    _SwPortFrames64Bytes_Type()
)
swPortFrames64Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortFrames64Bytes.setStatus("mandatory")
_SwPortFrames65To127Bytes_Type = Counter32
_SwPortFrames65To127Bytes_Object = MibTableColumn
swPortFrames65To127Bytes = _SwPortFrames65To127Bytes_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 3, 1, 18),
    _SwPortFrames65To127Bytes_Type()
)
swPortFrames65To127Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortFrames65To127Bytes.setStatus("mandatory")
_SwPortFrames128To255Bytes_Type = Counter32
_SwPortFrames128To255Bytes_Object = MibTableColumn
swPortFrames128To255Bytes = _SwPortFrames128To255Bytes_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 3, 1, 19),
    _SwPortFrames128To255Bytes_Type()
)
swPortFrames128To255Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortFrames128To255Bytes.setStatus("mandatory")
_SwPortFrames256To511Bytes_Type = Counter32
_SwPortFrames256To511Bytes_Object = MibTableColumn
swPortFrames256To511Bytes = _SwPortFrames256To511Bytes_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 3, 1, 20),
    _SwPortFrames256To511Bytes_Type()
)
swPortFrames256To511Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortFrames256To511Bytes.setStatus("mandatory")
_SwPortFrames512To1023Bytes_Type = Counter32
_SwPortFrames512To1023Bytes_Object = MibTableColumn
swPortFrames512To1023Bytes = _SwPortFrames512To1023Bytes_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 3, 1, 21),
    _SwPortFrames512To1023Bytes_Type()
)
swPortFrames512To1023Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortFrames512To1023Bytes.setStatus("mandatory")
_SwPortFrames1024To1522Bytes_Type = Counter32
_SwPortFrames1024To1522Bytes_Object = MibTableColumn
swPortFrames1024To1522Bytes = _SwPortFrames1024To1522Bytes_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 3, 1, 22),
    _SwPortFrames1024To1522Bytes_Type()
)
swPortFrames1024To1522Bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortFrames1024To1522Bytes.setStatus("mandatory")
_SwPortMACRxError_Type = Counter32
_SwPortMACRxError_Object = MibTableColumn
swPortMACRxError = _SwPortMACRxError_Object(
    (1, 3, 6, 1, 4, 1, 171, 11, 7, 1, 2, 3, 1, 23),
    _SwPortMACRxError_Type()
)
swPortMACRxError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortMACRxError.setStatus("mandatory")

# Managed Objects groups


# Notification objects

linkChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 0, 1)
)
linkChangeEvent.setObjects(
      *(("DES2218-MIB", "swPortInfoIndex"),
        ("DES2218-MIB", "swPortInfoType"),
        ("DES2218-MIB", "swPortInfoPartitionStatus"),
        ("DES2218-MIB", "swPortInfoLinkStatus"),
        ("DES2218-MIB", "swPortInfoDuplexMode"))
)
if mibBuilder.loadTexts:
    linkChangeEvent.setStatus(
        ""
    )

portPartition = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 0, 2)
)
portPartition.setObjects(
      *(("DES2218-MIB", "swPortInfoIndex"),
        ("DES2218-MIB", "swPortInfoType"),
        ("DES2218-MIB", "swPortInfoPartitionStatus"),
        ("DES2218-MIB", "swPortInfoLinkStatus"),
        ("DES2218-MIB", "swPortInfoDuplexMode"))
)
if mibBuilder.loadTexts:
    portPartition.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DES2218-MIB",
    **{"dlink": dlink,
       "linkChangeEvent": linkChangeEvent,
       "portPartition": portPartition,
       "dlink-products": dlink_products,
       "dlink-Des2218Prod": dlink_Des2218Prod,
       "dlink-Des2218ProdId": dlink_Des2218ProdId,
       "des2218SwHub": des2218SwHub,
       "dlink-mgmt": dlink_mgmt,
       "agentConfigInfo": agentConfigInfo,
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
       "agentBasicConfig": agentBasicConfig,
       "agentSwUpdateMode": agentSwUpdateMode,
       "agentSwUpdateCtrl": agentSwUpdateCtrl,
       "agentBootFile": agentBootFile,
       "agentSystemReset": agentSystemReset,
       "agentRs232PortConfig": agentRs232PortConfig,
       "agentOutOfBandBaudRateConfig": agentOutOfBandBaudRateConfig,
       "agentOutOfBandDialNumber": agentOutOfBandDialNumber,
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
       "agentIpBootProtocol": agentIpBootProtocol,
       "agentIpGetIpFromBootpServer": agentIpGetIpFromBootpServer,
       "agentIpUnauthAddr": agentIpUnauthAddr,
       "agentIpUnauthComm": agentIpUnauthComm,
       "agentIpLastBootServerAddr": agentIpLastBootServerAddr,
       "agentIpLastIpAddr": agentIpLastIpAddr,
       "agentIpTrapManagerTable": agentIpTrapManagerTable,
       "agentIpTrapManagerEntry": agentIpTrapManagerEntry,
       "agentIpTrapManagerIpAddr": agentIpTrapManagerIpAddr,
       "agentIpTrapManagerComm": agentIpTrapManagerComm,
       "agentIpTrapManagerStatus": agentIpTrapManagerStatus,
       "des2218series": des2218series,
       "des2218MIB": des2218MIB,
       "swDevicePackage": swDevicePackage,
       "swDeviceInfo": swDeviceInfo,
       "swDevInfoTotalNumOfPort": swDevInfoTotalNumOfPort,
       "swDevInfoNumOfPortOnUse": swDevInfoNumOfPortOnUse,
       "swDevInfoDesc": swDevInfoDesc,
       "swDevInfoPortType": swDevInfoPortType,
       "swDevInfoHwRev": swDevInfoHwRev,
       "swDevInfoSystemUpTime": swDevInfoSystemUpTime,
       "swDevInfoFrontPanelLedStatus": swDevInfoFrontPanelLedStatus,
       "swDevInfoDramSize": swDevInfoDramSize,
       "swDeviceCtl": swDeviceCtl,
       "swDevCtrlDisableLearningState": swDevCtrlDisableLearningState,
       "swDevCtrlReset": swDevCtrlReset,
       "swDevCtrlSpanningTree": swDevCtrlSpanningTree,
       "swPortPackage": swPortPackage,
       "swPortInfoTable": swPortInfoTable,
       "swPortInfoEntry": swPortInfoEntry,
       "swPortInfoGroupIndex": swPortInfoGroupIndex,
       "swPortInfoIndex": swPortInfoIndex,
       "swPortInfoType": swPortInfoType,
       "swPortInfoPartitionStatus": swPortInfoPartitionStatus,
       "swPortInfoLinkStatus": swPortInfoLinkStatus,
       "swPortInfoDuplexMode": swPortInfoDuplexMode,
       "swPortInfoNegotiationStatus": swPortInfoNegotiationStatus,
       "swPortInfoSpeedStatus": swPortInfoSpeedStatus,
       "swPortCtrlTable": swPortCtrlTable,
       "swPortCtrlEntry": swPortCtrlEntry,
       "swPortCtrlGroupIndex": swPortCtrlGroupIndex,
       "swPortCtrlIndex": swPortCtrlIndex,
       "swPortCtrlAdminState": swPortCtrlAdminState,
       "swPortCtrlDuplexState": swPortCtrlDuplexState,
       "swPortCtrlLinkStatusAlarmState": swPortCtrlLinkStatusAlarmState,
       "swPortCtrlFilterBcastState": swPortCtrlFilterBcastState,
       "swPortCtrlForwardUnknowState": swPortCtrlForwardUnknowState,
       "swPortCtrlPartitionStatus": swPortCtrlPartitionStatus,
       "swPortCtrlNegotiationStatus": swPortCtrlNegotiationStatus,
       "swPortCtrlSpeedStatus": swPortCtrlSpeedStatus,
       "swPortCounterTable": swPortCounterTable,
       "swPortCounterEntry": swPortCounterEntry,
       "swPortCounterGroupIndex": swPortCounterGroupIndex,
       "swPortCounterIndex": swPortCounterIndex,
       "swPortBytesReceived": swPortBytesReceived,
       "swPortBytesSent": swPortBytesSent,
       "swPortFramesReceived": swPortFramesReceived,
       "swPortFramesSent": swPortFramesSent,
       "swPortTotalBytesReceived": swPortTotalBytesReceived,
       "swPortTotalFramesReceived": swPortTotalFramesReceived,
       "swPortBroadcastFramesReceived": swPortBroadcastFramesReceived,
       "swPortMulticastFramesReceived": swPortMulticastFramesReceived,
       "swPortCRCError": swPortCRCError,
       "swPortOversizeFrames": swPortOversizeFrames,
       "swPortFragments": swPortFragments,
       "swPortJabber": swPortJabber,
       "swPortCollision": swPortCollision,
       "swPortLateCollision": swPortLateCollision,
       "swPortFrames64Bytes": swPortFrames64Bytes,
       "swPortFrames65To127Bytes": swPortFrames65To127Bytes,
       "swPortFrames128To255Bytes": swPortFrames128To255Bytes,
       "swPortFrames256To511Bytes": swPortFrames256To511Bytes,
       "swPortFrames512To1023Bytes": swPortFrames512To1023Bytes,
       "swPortFrames1024To1522Bytes": swPortFrames1024To1522Bytes,
       "swPortMACRxError": swPortMACRxError}
)
