# SNMP MIB module (INTEL-ES400-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/INTEL-ES400-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:09:35 2024
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



class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )





class PortList(OctetString):
    """Custom type PortList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )





class VlanIndex(Integer32):
    """Custom type VlanIndex based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Intel_ObjectIdentity = ObjectIdentity
intel = _Intel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343)
)
_Mib2ext_ObjectIdentity = ObjectIdentity
mib2ext = _Mib2ext_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6)
)
_Es400_ObjectIdentity = ObjectIdentity
es400 = _Es400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 17)
)
_Es400Agent_ObjectIdentity = ObjectIdentity
es400Agent = _Es400Agent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 1)
)
_Es400AgentInfo_ObjectIdentity = ObjectIdentity
es400AgentInfo = _Es400AgentInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 1, 1)
)


class _Es400AgentRuntimeSwVersion_Type(DisplayString):
    """Custom type es400AgentRuntimeSwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_Es400AgentRuntimeSwVersion_Type.__name__ = "DisplayString"
_Es400AgentRuntimeSwVersion_Object = MibScalar
es400AgentRuntimeSwVersion = _Es400AgentRuntimeSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 1, 1, 1),
    _Es400AgentRuntimeSwVersion_Type()
)
es400AgentRuntimeSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400AgentRuntimeSwVersion.setStatus("mandatory")


class _Es400AgentPromFwVersion_Type(DisplayString):
    """Custom type es400AgentPromFwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_Es400AgentPromFwVersion_Type.__name__ = "DisplayString"
_Es400AgentPromFwVersion_Object = MibScalar
es400AgentPromFwVersion = _Es400AgentPromFwVersion_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 1, 1, 2),
    _Es400AgentPromFwVersion_Type()
)
es400AgentPromFwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400AgentPromFwVersion.setStatus("mandatory")
_Es400AgentHwRevision_Type = Integer32
_Es400AgentHwRevision_Object = MibScalar
es400AgentHwRevision = _Es400AgentHwRevision_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 1, 1, 3),
    _Es400AgentHwRevision_Type()
)
es400AgentHwRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400AgentHwRevision.setStatus("mandatory")


class _Es400AgentMgmtProtocolCapability_Type(Integer32):
    """Custom type es400AgentMgmtProtocolCapability based on Integer32"""
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


_Es400AgentMgmtProtocolCapability_Type.__name__ = "Integer32"
_Es400AgentMgmtProtocolCapability_Object = MibScalar
es400AgentMgmtProtocolCapability = _Es400AgentMgmtProtocolCapability_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 1, 1, 4),
    _Es400AgentMgmtProtocolCapability_Type()
)
es400AgentMgmtProtocolCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400AgentMgmtProtocolCapability.setStatus("mandatory")
_Es400AgentMibSupportTable_Object = MibTable
es400AgentMibSupportTable = _Es400AgentMibSupportTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 1, 1, 5)
)
if mibBuilder.loadTexts:
    es400AgentMibSupportTable.setStatus("mandatory")
_Es400AgentMibSupportEntry_Object = MibTableRow
es400AgentMibSupportEntry = _Es400AgentMibSupportEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 1, 1, 5, 1)
)
es400AgentMibSupportEntry.setIndexNames(
    (0, "INTEL-ES400-MIB", "es400AgentMibSupportIndex"),
)
if mibBuilder.loadTexts:
    es400AgentMibSupportEntry.setStatus("mandatory")
_Es400AgentMibSupportIndex_Type = Integer32
_Es400AgentMibSupportIndex_Object = MibTableColumn
es400AgentMibSupportIndex = _Es400AgentMibSupportIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 1, 1, 5, 1, 1),
    _Es400AgentMibSupportIndex_Type()
)
es400AgentMibSupportIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400AgentMibSupportIndex.setStatus("mandatory")


class _Es400AgentMibSupportDescr_Type(DisplayString):
    """Custom type es400AgentMibSupportDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Es400AgentMibSupportDescr_Type.__name__ = "DisplayString"
_Es400AgentMibSupportDescr_Object = MibTableColumn
es400AgentMibSupportDescr = _Es400AgentMibSupportDescr_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 1, 1, 5, 1, 2),
    _Es400AgentMibSupportDescr_Type()
)
es400AgentMibSupportDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400AgentMibSupportDescr.setStatus("mandatory")
_Es400AgentMibSupportVersion_Type = Integer32
_Es400AgentMibSupportVersion_Object = MibTableColumn
es400AgentMibSupportVersion = _Es400AgentMibSupportVersion_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 1, 1, 5, 1, 3),
    _Es400AgentMibSupportVersion_Type()
)
es400AgentMibSupportVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400AgentMibSupportVersion.setStatus("mandatory")


class _Es400AgentMibSupportType_Type(Integer32):
    """Custom type es400AgentMibSupportType based on Integer32"""
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


_Es400AgentMibSupportType_Type.__name__ = "Integer32"
_Es400AgentMibSupportType_Object = MibTableColumn
es400AgentMibSupportType = _Es400AgentMibSupportType_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 1, 1, 5, 1, 4),
    _Es400AgentMibSupportType_Type()
)
es400AgentMibSupportType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400AgentMibSupportType.setStatus("mandatory")
_Es400AgentConfig_ObjectIdentity = ObjectIdentity
es400AgentConfig = _Es400AgentConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 1, 2)
)


class _Es400AgentSwUpdateMode_Type(Integer32):
    """Custom type es400AgentSwUpdateMode based on Integer32"""
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


_Es400AgentSwUpdateMode_Type.__name__ = "Integer32"
_Es400AgentSwUpdateMode_Object = MibScalar
es400AgentSwUpdateMode = _Es400AgentSwUpdateMode_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 1, 2, 1),
    _Es400AgentSwUpdateMode_Type()
)
es400AgentSwUpdateMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es400AgentSwUpdateMode.setStatus("mandatory")


class _Es400AgentSwUpdateCtrl_Type(Integer32):
    """Custom type es400AgentSwUpdateCtrl based on Integer32"""
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


_Es400AgentSwUpdateCtrl_Type.__name__ = "Integer32"
_Es400AgentSwUpdateCtrl_Object = MibScalar
es400AgentSwUpdateCtrl = _Es400AgentSwUpdateCtrl_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 1, 2, 2),
    _Es400AgentSwUpdateCtrl_Type()
)
es400AgentSwUpdateCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es400AgentSwUpdateCtrl.setStatus("mandatory")


class _Es400AgentBootFile_Type(DisplayString):
    """Custom type es400AgentBootFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Es400AgentBootFile_Type.__name__ = "DisplayString"
_Es400AgentBootFile_Object = MibScalar
es400AgentBootFile = _Es400AgentBootFile_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 1, 2, 3),
    _Es400AgentBootFile_Type()
)
es400AgentBootFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es400AgentBootFile.setStatus("mandatory")


class _Es400AgentFirmwareUpdateCtrl_Type(Integer32):
    """Custom type es400AgentFirmwareUpdateCtrl based on Integer32"""
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


_Es400AgentFirmwareUpdateCtrl_Type.__name__ = "Integer32"
_Es400AgentFirmwareUpdateCtrl_Object = MibScalar
es400AgentFirmwareUpdateCtrl = _Es400AgentFirmwareUpdateCtrl_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 1, 2, 4),
    _Es400AgentFirmwareUpdateCtrl_Type()
)
es400AgentFirmwareUpdateCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es400AgentFirmwareUpdateCtrl.setStatus("mandatory")


class _Es400AgentFirmwareFile_Type(DisplayString):
    """Custom type es400AgentFirmwareFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Es400AgentFirmwareFile_Type.__name__ = "DisplayString"
_Es400AgentFirmwareFile_Object = MibScalar
es400AgentFirmwareFile = _Es400AgentFirmwareFile_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 1, 2, 5),
    _Es400AgentFirmwareFile_Type()
)
es400AgentFirmwareFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es400AgentFirmwareFile.setStatus("mandatory")


class _Es400AgentSystemReset_Type(Integer32):
    """Custom type es400AgentSystemReset based on Integer32"""
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


_Es400AgentSystemReset_Type.__name__ = "Integer32"
_Es400AgentSystemReset_Object = MibScalar
es400AgentSystemReset = _Es400AgentSystemReset_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 1, 2, 6),
    _Es400AgentSystemReset_Type()
)
es400AgentSystemReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es400AgentSystemReset.setStatus("mandatory")


class _Es400AgentRs232PortConfig_Type(Integer32):
    """Custom type es400AgentRs232PortConfig based on Integer32"""
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


_Es400AgentRs232PortConfig_Type.__name__ = "Integer32"
_Es400AgentRs232PortConfig_Object = MibScalar
es400AgentRs232PortConfig = _Es400AgentRs232PortConfig_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 1, 2, 7),
    _Es400AgentRs232PortConfig_Type()
)
es400AgentRs232PortConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es400AgentRs232PortConfig.setStatus("mandatory")


class _Es400AgentOutOfBandBaudRateConfig_Type(Integer32):
    """Custom type es400AgentOutOfBandBaudRateConfig based on Integer32"""
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


_Es400AgentOutOfBandBaudRateConfig_Type.__name__ = "Integer32"
_Es400AgentOutOfBandBaudRateConfig_Object = MibScalar
es400AgentOutOfBandBaudRateConfig = _Es400AgentOutOfBandBaudRateConfig_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 1, 2, 8),
    _Es400AgentOutOfBandBaudRateConfig_Type()
)
es400AgentOutOfBandBaudRateConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es400AgentOutOfBandBaudRateConfig.setStatus("mandatory")
_Es400AgentIpConfig_ObjectIdentity = ObjectIdentity
es400AgentIpConfig = _Es400AgentIpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 1, 3)
)
_Es400AgentIpNumOfIf_Type = Integer32
_Es400AgentIpNumOfIf_Object = MibScalar
es400AgentIpNumOfIf = _Es400AgentIpNumOfIf_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 1, 3, 1),
    _Es400AgentIpNumOfIf_Type()
)
es400AgentIpNumOfIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400AgentIpNumOfIf.setStatus("mandatory")
_Es400AgentIpIfTable_Object = MibTable
es400AgentIpIfTable = _Es400AgentIpIfTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 1, 3, 2)
)
if mibBuilder.loadTexts:
    es400AgentIpIfTable.setStatus("mandatory")
_Es400AgentIpIfEntry_Object = MibTableRow
es400AgentIpIfEntry = _Es400AgentIpIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 1, 3, 2, 1)
)
es400AgentIpIfEntry.setIndexNames(
    (0, "INTEL-ES400-MIB", "es400AgentIpIfIndex"),
)
if mibBuilder.loadTexts:
    es400AgentIpIfEntry.setStatus("mandatory")


class _Es400AgentIpIfIndex_Type(Integer32):
    """Custom type es400AgentIpIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Es400AgentIpIfIndex_Type.__name__ = "Integer32"
_Es400AgentIpIfIndex_Object = MibTableColumn
es400AgentIpIfIndex = _Es400AgentIpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 1, 3, 2, 1, 1),
    _Es400AgentIpIfIndex_Type()
)
es400AgentIpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400AgentIpIfIndex.setStatus("mandatory")
_Es400AgentIpIfAddress_Type = IpAddress
_Es400AgentIpIfAddress_Object = MibTableColumn
es400AgentIpIfAddress = _Es400AgentIpIfAddress_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 1, 3, 2, 1, 2),
    _Es400AgentIpIfAddress_Type()
)
es400AgentIpIfAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es400AgentIpIfAddress.setStatus("mandatory")
_Es400AgentIpIfNetMask_Type = IpAddress
_Es400AgentIpIfNetMask_Object = MibTableColumn
es400AgentIpIfNetMask = _Es400AgentIpIfNetMask_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 1, 3, 2, 1, 3),
    _Es400AgentIpIfNetMask_Type()
)
es400AgentIpIfNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es400AgentIpIfNetMask.setStatus("mandatory")
_Es400AgentIpIfDefaultRouter_Type = IpAddress
_Es400AgentIpIfDefaultRouter_Object = MibTableColumn
es400AgentIpIfDefaultRouter = _Es400AgentIpIfDefaultRouter_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 1, 3, 2, 1, 4),
    _Es400AgentIpIfDefaultRouter_Type()
)
es400AgentIpIfDefaultRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es400AgentIpIfDefaultRouter.setStatus("mandatory")
_Es400AgentIpIfMacAddr_Type = PhysAddress
_Es400AgentIpIfMacAddr_Object = MibTableColumn
es400AgentIpIfMacAddr = _Es400AgentIpIfMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 1, 3, 2, 1, 5),
    _Es400AgentIpIfMacAddr_Type()
)
es400AgentIpIfMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400AgentIpIfMacAddr.setStatus("mandatory")


class _Es400AgentIpIfType_Type(Integer32):
    """Custom type es400AgentIpIfType based on Integer32"""
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


_Es400AgentIpIfType_Type.__name__ = "Integer32"
_Es400AgentIpIfType_Object = MibTableColumn
es400AgentIpIfType = _Es400AgentIpIfType_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 1, 3, 2, 1, 6),
    _Es400AgentIpIfType_Type()
)
es400AgentIpIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400AgentIpIfType.setStatus("mandatory")
_Es400AgentIpBootServerAddr_Type = IpAddress
_Es400AgentIpBootServerAddr_Object = MibScalar
es400AgentIpBootServerAddr = _Es400AgentIpBootServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 1, 3, 3),
    _Es400AgentIpBootServerAddr_Type()
)
es400AgentIpBootServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es400AgentIpBootServerAddr.setStatus("mandatory")


class _Es400AgentIpGetIpFromBootpServer_Type(Integer32):
    """Custom type es400AgentIpGetIpFromBootpServer based on Integer32"""
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


_Es400AgentIpGetIpFromBootpServer_Type.__name__ = "Integer32"
_Es400AgentIpGetIpFromBootpServer_Object = MibScalar
es400AgentIpGetIpFromBootpServer = _Es400AgentIpGetIpFromBootpServer_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 1, 3, 4),
    _Es400AgentIpGetIpFromBootpServer_Type()
)
es400AgentIpGetIpFromBootpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es400AgentIpGetIpFromBootpServer.setStatus("mandatory")
_Es400AgentIpUnauthAddr_Type = IpAddress
_Es400AgentIpUnauthAddr_Object = MibScalar
es400AgentIpUnauthAddr = _Es400AgentIpUnauthAddr_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 1, 3, 5),
    _Es400AgentIpUnauthAddr_Type()
)
es400AgentIpUnauthAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400AgentIpUnauthAddr.setStatus("mandatory")


class _Es400AgentIpUnauthComm_Type(DisplayString):
    """Custom type es400AgentIpUnauthComm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_Es400AgentIpUnauthComm_Type.__name__ = "DisplayString"
_Es400AgentIpUnauthComm_Object = MibScalar
es400AgentIpUnauthComm = _Es400AgentIpUnauthComm_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 1, 3, 6),
    _Es400AgentIpUnauthComm_Type()
)
es400AgentIpUnauthComm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400AgentIpUnauthComm.setStatus("mandatory")
_Es400AgentIpLastBootServerAddr_Type = IpAddress
_Es400AgentIpLastBootServerAddr_Object = MibScalar
es400AgentIpLastBootServerAddr = _Es400AgentIpLastBootServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 1, 3, 7),
    _Es400AgentIpLastBootServerAddr_Type()
)
es400AgentIpLastBootServerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400AgentIpLastBootServerAddr.setStatus("mandatory")
_Es400AgentIpLastIpAddr_Type = IpAddress
_Es400AgentIpLastIpAddr_Object = MibScalar
es400AgentIpLastIpAddr = _Es400AgentIpLastIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 1, 3, 8),
    _Es400AgentIpLastIpAddr_Type()
)
es400AgentIpLastIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400AgentIpLastIpAddr.setStatus("mandatory")
_Es400AgentTrapAddressTable_Object = MibTable
es400AgentTrapAddressTable = _Es400AgentTrapAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 1, 4)
)
if mibBuilder.loadTexts:
    es400AgentTrapAddressTable.setStatus("mandatory")
_Es400AgentTrapAddressEntry_Object = MibTableRow
es400AgentTrapAddressEntry = _Es400AgentTrapAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 1, 4, 1)
)
es400AgentTrapAddressEntry.setIndexNames(
    (0, "INTEL-ES400-MIB", "es400AgentTrapIndex"),
)
if mibBuilder.loadTexts:
    es400AgentTrapAddressEntry.setStatus("mandatory")
_Es400AgentTrapIndex_Type = Integer32
_Es400AgentTrapIndex_Object = MibTableColumn
es400AgentTrapIndex = _Es400AgentTrapIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 1, 4, 1, 1),
    _Es400AgentTrapIndex_Type()
)
es400AgentTrapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400AgentTrapIndex.setStatus("mandatory")
_Es400AgentTrapAddressIp_Type = IpAddress
_Es400AgentTrapAddressIp_Object = MibTableColumn
es400AgentTrapAddressIp = _Es400AgentTrapAddressIp_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 1, 4, 1, 2),
    _Es400AgentTrapAddressIp_Type()
)
es400AgentTrapAddressIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es400AgentTrapAddressIp.setStatus("mandatory")


class _Es400AgentTrapAddressComm_Type(DisplayString):
    """Custom type es400AgentTrapAddressComm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_Es400AgentTrapAddressComm_Type.__name__ = "DisplayString"
_Es400AgentTrapAddressComm_Object = MibTableColumn
es400AgentTrapAddressComm = _Es400AgentTrapAddressComm_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 1, 4, 1, 3),
    _Es400AgentTrapAddressComm_Type()
)
es400AgentTrapAddressComm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es400AgentTrapAddressComm.setStatus("mandatory")


class _Es400AgentTrapAddressStatus_Type(Integer32):
    """Custom type es400AgentTrapAddressStatus based on Integer32"""
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


_Es400AgentTrapAddressStatus_Type.__name__ = "Integer32"
_Es400AgentTrapAddressStatus_Object = MibTableColumn
es400AgentTrapAddressStatus = _Es400AgentTrapAddressStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 1, 4, 1, 4),
    _Es400AgentTrapAddressStatus_Type()
)
es400AgentTrapAddressStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es400AgentTrapAddressStatus.setStatus("mandatory")
_Es400Chassis_ObjectIdentity = ObjectIdentity
es400Chassis = _Es400Chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 2)
)
_Es400ChassisInfo_ObjectIdentity = ObjectIdentity
es400ChassisInfo = _Es400ChassisInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 2, 1)
)
_Es400ChassisInfoSystemUpTime_Type = TimeTicks
_Es400ChassisInfoSystemUpTime_Object = MibScalar
es400ChassisInfoSystemUpTime = _Es400ChassisInfoSystemUpTime_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 2, 1, 1),
    _Es400ChassisInfoSystemUpTime_Type()
)
es400ChassisInfoSystemUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400ChassisInfoSystemUpTime.setStatus("mandatory")
_Es400ChassisInfoTotalNumOfPort_Type = Integer32
_Es400ChassisInfoTotalNumOfPort_Object = MibScalar
es400ChassisInfoTotalNumOfPort = _Es400ChassisInfoTotalNumOfPort_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 2, 1, 2),
    _Es400ChassisInfoTotalNumOfPort_Type()
)
es400ChassisInfoTotalNumOfPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400ChassisInfoTotalNumOfPort.setStatus("mandatory")
_Es400ChassisInfoNumOfPortInUse_Type = Integer32
_Es400ChassisInfoNumOfPortInUse_Object = MibScalar
es400ChassisInfoNumOfPortInUse = _Es400ChassisInfoNumOfPortInUse_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 2, 1, 3),
    _Es400ChassisInfoNumOfPortInUse_Type()
)
es400ChassisInfoNumOfPortInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400ChassisInfoNumOfPortInUse.setStatus("mandatory")


class _Es400ChassisInfoConsoleInUse_Type(Integer32):
    """Custom type es400ChassisInfoConsoleInUse based on Integer32"""
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


_Es400ChassisInfoConsoleInUse_Type.__name__ = "Integer32"
_Es400ChassisInfoConsoleInUse_Object = MibScalar
es400ChassisInfoConsoleInUse = _Es400ChassisInfoConsoleInUse_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 2, 1, 4),
    _Es400ChassisInfoConsoleInUse_Type()
)
es400ChassisInfoConsoleInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400ChassisInfoConsoleInUse.setStatus("mandatory")


class _Es400ChassisInfoFrontPanelLedStatus_Type(OctetString):
    """Custom type es400ChassisInfoFrontPanelLedStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Es400ChassisInfoFrontPanelLedStatus_Type.__name__ = "OctetString"
_Es400ChassisInfoFrontPanelLedStatus_Object = MibScalar
es400ChassisInfoFrontPanelLedStatus = _Es400ChassisInfoFrontPanelLedStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 2, 1, 5),
    _Es400ChassisInfoFrontPanelLedStatus_Type()
)
es400ChassisInfoFrontPanelLedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400ChassisInfoFrontPanelLedStatus.setStatus("mandatory")


class _Es400ChassisInfoSaveCfg_Type(Integer32):
    """Custom type es400ChassisInfoSaveCfg based on Integer32"""
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


_Es400ChassisInfoSaveCfg_Type.__name__ = "Integer32"
_Es400ChassisInfoSaveCfg_Object = MibScalar
es400ChassisInfoSaveCfg = _Es400ChassisInfoSaveCfg_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 2, 1, 6),
    _Es400ChassisInfoSaveCfg_Type()
)
es400ChassisInfoSaveCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400ChassisInfoSaveCfg.setStatus("mandatory")
_Es400ChassisConfig_ObjectIdentity = ObjectIdentity
es400ChassisConfig = _Es400ChassisConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 2, 2)
)


class _Es400ChassisConfigStpState_Type(Integer32):
    """Custom type es400ChassisConfigStpState based on Integer32"""
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


_Es400ChassisConfigStpState_Type.__name__ = "Integer32"
_Es400ChassisConfigStpState_Object = MibScalar
es400ChassisConfigStpState = _Es400ChassisConfigStpState_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 2, 2, 1),
    _Es400ChassisConfigStpState_Type()
)
es400ChassisConfigStpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es400ChassisConfigStpState.setStatus("mandatory")


class _Es400ChassisConfigIGMPCaptureState_Type(Integer32):
    """Custom type es400ChassisConfigIGMPCaptureState based on Integer32"""
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


_Es400ChassisConfigIGMPCaptureState_Type.__name__ = "Integer32"
_Es400ChassisConfigIGMPCaptureState_Object = MibScalar
es400ChassisConfigIGMPCaptureState = _Es400ChassisConfigIGMPCaptureState_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 2, 2, 2),
    _Es400ChassisConfigIGMPCaptureState_Type()
)
es400ChassisConfigIGMPCaptureState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es400ChassisConfigIGMPCaptureState.setStatus("mandatory")


class _Es400ChassisConfigPartitionModeState_Type(Integer32):
    """Custom type es400ChassisConfigPartitionModeState based on Integer32"""
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


_Es400ChassisConfigPartitionModeState_Type.__name__ = "Integer32"
_Es400ChassisConfigPartitionModeState_Object = MibScalar
es400ChassisConfigPartitionModeState = _Es400ChassisConfigPartitionModeState_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 2, 2, 3),
    _Es400ChassisConfigPartitionModeState_Type()
)
es400ChassisConfigPartitionModeState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es400ChassisConfigPartitionModeState.setStatus("mandatory")


class _Es400ChassisConfigTableLockState_Type(Integer32):
    """Custom type es400ChassisConfigTableLockState based on Integer32"""
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


_Es400ChassisConfigTableLockState_Type.__name__ = "Integer32"
_Es400ChassisConfigTableLockState_Object = MibScalar
es400ChassisConfigTableLockState = _Es400ChassisConfigTableLockState_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 2, 2, 4),
    _Es400ChassisConfigTableLockState_Type()
)
es400ChassisConfigTableLockState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es400ChassisConfigTableLockState.setStatus("mandatory")
_Es400ChassisConfigSaveCfg_Type = Integer32
_Es400ChassisConfigSaveCfg_Object = MibScalar
es400ChassisConfigSaveCfg = _Es400ChassisConfigSaveCfg_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 2, 2, 5),
    _Es400ChassisConfigSaveCfg_Type()
)
es400ChassisConfigSaveCfg.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    es400ChassisConfigSaveCfg.setStatus("mandatory")


class _Es400ChassisConfigHOLState_Type(Integer32):
    """Custom type es400ChassisConfigHOLState based on Integer32"""
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


_Es400ChassisConfigHOLState_Type.__name__ = "Integer32"
_Es400ChassisConfigHOLState_Object = MibScalar
es400ChassisConfigHOLState = _Es400ChassisConfigHOLState_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 2, 2, 6),
    _Es400ChassisConfigHOLState_Type()
)
es400ChassisConfigHOLState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es400ChassisConfigHOLState.setStatus("mandatory")


class _Es400ChassisConfigAddrLookupModes_Type(Integer32):
    """Custom type es400ChassisConfigAddrLookupModes based on Integer32"""
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
          ("random-mode", 3),
          ("sequential-mode", 2))
    )


_Es400ChassisConfigAddrLookupModes_Type.__name__ = "Integer32"
_Es400ChassisConfigAddrLookupModes_Object = MibScalar
es400ChassisConfigAddrLookupModes = _Es400ChassisConfigAddrLookupModes_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 2, 2, 7),
    _Es400ChassisConfigAddrLookupModes_Type()
)
es400ChassisConfigAddrLookupModes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es400ChassisConfigAddrLookupModes.setStatus("mandatory")


class _Es400ChassisConfigUploadImageFileName_Type(DisplayString):
    """Custom type es400ChassisConfigUploadImageFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Es400ChassisConfigUploadImageFileName_Type.__name__ = "DisplayString"
_Es400ChassisConfigUploadImageFileName_Object = MibScalar
es400ChassisConfigUploadImageFileName = _Es400ChassisConfigUploadImageFileName_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 2, 2, 8),
    _Es400ChassisConfigUploadImageFileName_Type()
)
es400ChassisConfigUploadImageFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es400ChassisConfigUploadImageFileName.setStatus("mandatory")
_Es400ChassisConfigUploadImage_Type = Integer32
_Es400ChassisConfigUploadImage_Object = MibScalar
es400ChassisConfigUploadImage = _Es400ChassisConfigUploadImage_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 2, 2, 9),
    _Es400ChassisConfigUploadImage_Type()
)
es400ChassisConfigUploadImage.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    es400ChassisConfigUploadImage.setStatus("mandatory")


class _Es400ChassisConfigHighPriorityServiceRatio_Type(Integer32):
    """Custom type es400ChassisConfigHighPriorityServiceRatio based on Integer32"""
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
        *(("all-high-before-low", 6),
          ("other", 1),
          ("pkt-12high-1low", 5),
          ("pkt-1high-1low", 2),
          ("pkt-4high-1low", 3),
          ("pkt-8high-1low", 4))
    )


_Es400ChassisConfigHighPriorityServiceRatio_Type.__name__ = "Integer32"
_Es400ChassisConfigHighPriorityServiceRatio_Object = MibScalar
es400ChassisConfigHighPriorityServiceRatio = _Es400ChassisConfigHighPriorityServiceRatio_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 2, 2, 10),
    _Es400ChassisConfigHighPriorityServiceRatio_Type()
)
es400ChassisConfigHighPriorityServiceRatio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es400ChassisConfigHighPriorityServiceRatio.setStatus("mandatory")
_Es400ChassisAlarm_ObjectIdentity = ObjectIdentity
es400ChassisAlarm = _Es400ChassisAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 2, 3)
)


class _Es400ChassisAlarmPartition_Type(Integer32):
    """Custom type es400ChassisAlarmPartition based on Integer32"""
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


_Es400ChassisAlarmPartition_Type.__name__ = "Integer32"
_Es400ChassisAlarmPartition_Object = MibScalar
es400ChassisAlarmPartition = _Es400ChassisAlarmPartition_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 2, 3, 1),
    _Es400ChassisAlarmPartition_Type()
)
es400ChassisAlarmPartition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es400ChassisAlarmPartition.setStatus("mandatory")


class _Es400ChassisAlarmNewRoot_Type(Integer32):
    """Custom type es400ChassisAlarmNewRoot based on Integer32"""
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


_Es400ChassisAlarmNewRoot_Type.__name__ = "Integer32"
_Es400ChassisAlarmNewRoot_Object = MibScalar
es400ChassisAlarmNewRoot = _Es400ChassisAlarmNewRoot_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 2, 3, 2),
    _Es400ChassisAlarmNewRoot_Type()
)
es400ChassisAlarmNewRoot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es400ChassisAlarmNewRoot.setStatus("mandatory")


class _Es400ChassisAlarmTopologyChange_Type(Integer32):
    """Custom type es400ChassisAlarmTopologyChange based on Integer32"""
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


_Es400ChassisAlarmTopologyChange_Type.__name__ = "Integer32"
_Es400ChassisAlarmTopologyChange_Object = MibScalar
es400ChassisAlarmTopologyChange = _Es400ChassisAlarmTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 2, 3, 3),
    _Es400ChassisAlarmTopologyChange_Type()
)
es400ChassisAlarmTopologyChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es400ChassisAlarmTopologyChange.setStatus("mandatory")


class _Es400ChassisAlarmLinkChange_Type(Integer32):
    """Custom type es400ChassisAlarmLinkChange based on Integer32"""
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


_Es400ChassisAlarmLinkChange_Type.__name__ = "Integer32"
_Es400ChassisAlarmLinkChange_Object = MibScalar
es400ChassisAlarmLinkChange = _Es400ChassisAlarmLinkChange_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 2, 3, 4),
    _Es400ChassisAlarmLinkChange_Type()
)
es400ChassisAlarmLinkChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es400ChassisAlarmLinkChange.setStatus("mandatory")
_Es400Port_ObjectIdentity = ObjectIdentity
es400Port = _Es400Port_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 3)
)
_Es400PortInfoTable_Object = MibTable
es400PortInfoTable = _Es400PortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 3, 1)
)
if mibBuilder.loadTexts:
    es400PortInfoTable.setStatus("mandatory")
_Es400PortInfoEntry_Object = MibTableRow
es400PortInfoEntry = _Es400PortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 3, 1, 1)
)
es400PortInfoEntry.setIndexNames(
    (0, "INTEL-ES400-MIB", "es400PortInfoIndex"),
)
if mibBuilder.loadTexts:
    es400PortInfoEntry.setStatus("mandatory")
_Es400PortInfoIndex_Type = Integer32
_Es400PortInfoIndex_Object = MibTableColumn
es400PortInfoIndex = _Es400PortInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 3, 1, 1, 1),
    _Es400PortInfoIndex_Type()
)
es400PortInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400PortInfoIndex.setStatus("mandatory")


class _Es400PortInfoType_Type(Integer32):
    """Custom type es400PortInfoType based on Integer32"""
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
        *(("other", 1),
          ("portType-AUI", 3),
          ("portType-BNC", 5),
          ("portType-Fiber", 4),
          ("portType-UTP", 2))
    )


_Es400PortInfoType_Type.__name__ = "Integer32"
_Es400PortInfoType_Object = MibTableColumn
es400PortInfoType = _Es400PortInfoType_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 3, 1, 1, 2),
    _Es400PortInfoType_Type()
)
es400PortInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400PortInfoType.setStatus("mandatory")


class _Es400PortInfoLinkStatus_Type(Integer32):
    """Custom type es400PortInfoLinkStatus based on Integer32"""
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


_Es400PortInfoLinkStatus_Type.__name__ = "Integer32"
_Es400PortInfoLinkStatus_Object = MibTableColumn
es400PortInfoLinkStatus = _Es400PortInfoLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 3, 1, 1, 3),
    _Es400PortInfoLinkStatus_Type()
)
es400PortInfoLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400PortInfoLinkStatus.setStatus("mandatory")


class _Es400PortInfoNwayStatus_Type(Integer32):
    """Custom type es400PortInfoNwayStatus based on Integer32"""
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
        *(("full-100Mbps", 5),
          ("full-10Mbps", 3),
          ("full-1Gigabps", 7),
          ("half-100Mbps", 4),
          ("half-10Mbps", 2),
          ("half-1Gigabps", 6),
          ("other", 1))
    )


_Es400PortInfoNwayStatus_Type.__name__ = "Integer32"
_Es400PortInfoNwayStatus_Object = MibTableColumn
es400PortInfoNwayStatus = _Es400PortInfoNwayStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 3, 1, 1, 4),
    _Es400PortInfoNwayStatus_Type()
)
es400PortInfoNwayStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400PortInfoNwayStatus.setStatus("mandatory")


class _Es400PortInfoFlowCtrlStatus_Type(Integer32):
    """Custom type es400PortInfoFlowCtrlStatus based on Integer32"""
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
        *(("backpressure-disabled", 4),
          ("backpressure-enabled", 5),
          ("flowctrl-disabled", 2),
          ("flowctrl-enabled", 3),
          ("other", 1))
    )


_Es400PortInfoFlowCtrlStatus_Type.__name__ = "Integer32"
_Es400PortInfoFlowCtrlStatus_Object = MibTableColumn
es400PortInfoFlowCtrlStatus = _Es400PortInfoFlowCtrlStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 3, 1, 1, 5),
    _Es400PortInfoFlowCtrlStatus_Type()
)
es400PortInfoFlowCtrlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400PortInfoFlowCtrlStatus.setStatus("mandatory")
_Es400PortConfigTable_Object = MibTable
es400PortConfigTable = _Es400PortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 3, 2)
)
if mibBuilder.loadTexts:
    es400PortConfigTable.setStatus("mandatory")
_Es400PortConfigEntry_Object = MibTableRow
es400PortConfigEntry = _Es400PortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 3, 2, 1)
)
es400PortConfigEntry.setIndexNames(
    (0, "INTEL-ES400-MIB", "es400PortConfigIndex"),
)
if mibBuilder.loadTexts:
    es400PortConfigEntry.setStatus("mandatory")
_Es400PortConfigIndex_Type = Integer32
_Es400PortConfigIndex_Object = MibTableColumn
es400PortConfigIndex = _Es400PortConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 3, 2, 1, 1),
    _Es400PortConfigIndex_Type()
)
es400PortConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400PortConfigIndex.setStatus("mandatory")


class _Es400PortConfigAdminState_Type(Integer32):
    """Custom type es400PortConfigAdminState based on Integer32"""
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


_Es400PortConfigAdminState_Type.__name__ = "Integer32"
_Es400PortConfigAdminState_Object = MibTableColumn
es400PortConfigAdminState = _Es400PortConfigAdminState_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 3, 2, 1, 2),
    _Es400PortConfigAdminState_Type()
)
es400PortConfigAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es400PortConfigAdminState.setStatus("mandatory")


class _Es400PortConfigLinkStatusAlarmState_Type(Integer32):
    """Custom type es400PortConfigLinkStatusAlarmState based on Integer32"""
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


_Es400PortConfigLinkStatusAlarmState_Type.__name__ = "Integer32"
_Es400PortConfigLinkStatusAlarmState_Object = MibTableColumn
es400PortConfigLinkStatusAlarmState = _Es400PortConfigLinkStatusAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 3, 2, 1, 3),
    _Es400PortConfigLinkStatusAlarmState_Type()
)
es400PortConfigLinkStatusAlarmState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es400PortConfigLinkStatusAlarmState.setStatus("mandatory")


class _Es400PortConfigNwayState_Type(Integer32):
    """Custom type es400PortConfigNwayState based on Integer32"""
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
        *(("nway-disabled-100Mbps-Full", 6),
          ("nway-disabled-100Mbps-Half", 5),
          ("nway-disabled-10Mbps-Full", 4),
          ("nway-disabled-10Mbps-Half", 3),
          ("nway-disabled-1Gigabps-Full", 8),
          ("nway-disabled-1Gigabps-Half", 7),
          ("nway-enabled", 2),
          ("other", 1))
    )


_Es400PortConfigNwayState_Type.__name__ = "Integer32"
_Es400PortConfigNwayState_Object = MibTableColumn
es400PortConfigNwayState = _Es400PortConfigNwayState_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 3, 2, 1, 4),
    _Es400PortConfigNwayState_Type()
)
es400PortConfigNwayState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es400PortConfigNwayState.setStatus("mandatory")


class _Es400PortConfigFlowCtrlState_Type(Integer32):
    """Custom type es400PortConfigFlowCtrlState based on Integer32"""
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


_Es400PortConfigFlowCtrlState_Type.__name__ = "Integer32"
_Es400PortConfigFlowCtrlState_Object = MibTableColumn
es400PortConfigFlowCtrlState = _Es400PortConfigFlowCtrlState_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 3, 2, 1, 5),
    _Es400PortConfigFlowCtrlState_Type()
)
es400PortConfigFlowCtrlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es400PortConfigFlowCtrlState.setStatus("mandatory")


class _Es400PortConfigBackPressState_Type(Integer32):
    """Custom type es400PortConfigBackPressState based on Integer32"""
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


_Es400PortConfigBackPressState_Type.__name__ = "Integer32"
_Es400PortConfigBackPressState_Object = MibTableColumn
es400PortConfigBackPressState = _Es400PortConfigBackPressState_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 3, 2, 1, 6),
    _Es400PortConfigBackPressState_Type()
)
es400PortConfigBackPressState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es400PortConfigBackPressState.setStatus("mandatory")


class _Es400PortConfigLockState_Type(Integer32):
    """Custom type es400PortConfigLockState based on Integer32"""
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
          ("enable", 3),
          ("other", 1))
    )


_Es400PortConfigLockState_Type.__name__ = "Integer32"
_Es400PortConfigLockState_Object = MibTableColumn
es400PortConfigLockState = _Es400PortConfigLockState_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 3, 2, 1, 7),
    _Es400PortConfigLockState_Type()
)
es400PortConfigLockState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es400PortConfigLockState.setStatus("mandatory")


class _Es400PortConfigPriority_Type(Integer32):
    """Custom type es400PortConfigPriority based on Integer32"""
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
        *(("default", 2),
          ("force-high-priority", 4),
          ("force-low-priority", 3),
          ("other", 1))
    )


_Es400PortConfigPriority_Type.__name__ = "Integer32"
_Es400PortConfigPriority_Object = MibTableColumn
es400PortConfigPriority = _Es400PortConfigPriority_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 3, 2, 1, 8),
    _Es400PortConfigPriority_Type()
)
es400PortConfigPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es400PortConfigPriority.setStatus("mandatory")


class _Es400PortConfigStpState_Type(Integer32):
    """Custom type es400PortConfigStpState based on Integer32"""
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


_Es400PortConfigStpState_Type.__name__ = "Integer32"
_Es400PortConfigStpState_Object = MibTableColumn
es400PortConfigStpState = _Es400PortConfigStpState_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 3, 2, 1, 9),
    _Es400PortConfigStpState_Type()
)
es400PortConfigStpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es400PortConfigStpState.setStatus("mandatory")


class _Es400PortConfigHOLState_Type(Integer32):
    """Custom type es400PortConfigHOLState based on Integer32"""
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


_Es400PortConfigHOLState_Type.__name__ = "Integer32"
_Es400PortConfigHOLState_Object = MibTableColumn
es400PortConfigHOLState = _Es400PortConfigHOLState_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 3, 2, 1, 10),
    _Es400PortConfigHOLState_Type()
)
es400PortConfigHOLState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es400PortConfigHOLState.setStatus("mandatory")
_Es400PortConfigBroadcastStormThr_Type = Integer32
_Es400PortConfigBroadcastStormThr_Object = MibTableColumn
es400PortConfigBroadcastStormThr = _Es400PortConfigBroadcastStormThr_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 3, 2, 1, 11),
    _Es400PortConfigBroadcastStormThr_Type()
)
es400PortConfigBroadcastStormThr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es400PortConfigBroadcastStormThr.setStatus("mandatory")


class _Es400PortConfigBroadcastStormCtrl_Type(Integer32):
    """Custom type es400PortConfigBroadcastStormCtrl based on Integer32"""
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


_Es400PortConfigBroadcastStormCtrl_Type.__name__ = "Integer32"
_Es400PortConfigBroadcastStormCtrl_Object = MibTableColumn
es400PortConfigBroadcastStormCtrl = _Es400PortConfigBroadcastStormCtrl_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 3, 2, 1, 12),
    _Es400PortConfigBroadcastStormCtrl_Type()
)
es400PortConfigBroadcastStormCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es400PortConfigBroadcastStormCtrl.setStatus("mandatory")
_Es400PortConfigCleanAllStatisticCounter_Type = Integer32
_Es400PortConfigCleanAllStatisticCounter_Object = MibTableColumn
es400PortConfigCleanAllStatisticCounter = _Es400PortConfigCleanAllStatisticCounter_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 3, 2, 1, 13),
    _Es400PortConfigCleanAllStatisticCounter_Type()
)
es400PortConfigCleanAllStatisticCounter.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    es400PortConfigCleanAllStatisticCounter.setStatus("mandatory")
_Es400PortStatTable_Object = MibTable
es400PortStatTable = _Es400PortStatTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 3, 3)
)
if mibBuilder.loadTexts:
    es400PortStatTable.setStatus("mandatory")
_Es400PortStatEntry_Object = MibTableRow
es400PortStatEntry = _Es400PortStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 3, 3, 1)
)
es400PortStatEntry.setIndexNames(
    (0, "INTEL-ES400-MIB", "es400PortStatIndex"),
)
if mibBuilder.loadTexts:
    es400PortStatEntry.setStatus("mandatory")
_Es400PortStatIndex_Type = Integer32
_Es400PortStatIndex_Object = MibTableColumn
es400PortStatIndex = _Es400PortStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 3, 3, 1, 1),
    _Es400PortStatIndex_Type()
)
es400PortStatIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400PortStatIndex.setStatus("mandatory")
_Es400PortStatByteRx_Type = Counter32
_Es400PortStatByteRx_Object = MibTableColumn
es400PortStatByteRx = _Es400PortStatByteRx_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 3, 3, 1, 2),
    _Es400PortStatByteRx_Type()
)
es400PortStatByteRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400PortStatByteRx.setStatus("mandatory")
_Es400PortStatByteTx_Type = Counter32
_Es400PortStatByteTx_Object = MibTableColumn
es400PortStatByteTx = _Es400PortStatByteTx_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 3, 3, 1, 3),
    _Es400PortStatByteTx_Type()
)
es400PortStatByteTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400PortStatByteTx.setStatus("mandatory")
_Es400PortStatFrameRx_Type = Counter32
_Es400PortStatFrameRx_Object = MibTableColumn
es400PortStatFrameRx = _Es400PortStatFrameRx_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 3, 3, 1, 4),
    _Es400PortStatFrameRx_Type()
)
es400PortStatFrameRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400PortStatFrameRx.setStatus("mandatory")
_Es400PortStatFrameTx_Type = Counter32
_Es400PortStatFrameTx_Object = MibTableColumn
es400PortStatFrameTx = _Es400PortStatFrameTx_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 3, 3, 1, 5),
    _Es400PortStatFrameTx_Type()
)
es400PortStatFrameTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400PortStatFrameTx.setStatus("mandatory")
_Es400PortStatTotalBytesRx_Type = Counter32
_Es400PortStatTotalBytesRx_Object = MibTableColumn
es400PortStatTotalBytesRx = _Es400PortStatTotalBytesRx_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 3, 3, 1, 6),
    _Es400PortStatTotalBytesRx_Type()
)
es400PortStatTotalBytesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400PortStatTotalBytesRx.setStatus("mandatory")
_Es400PortStatTotalFramesRx_Type = Counter32
_Es400PortStatTotalFramesRx_Object = MibTableColumn
es400PortStatTotalFramesRx = _Es400PortStatTotalFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 3, 3, 1, 7),
    _Es400PortStatTotalFramesRx_Type()
)
es400PortStatTotalFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400PortStatTotalFramesRx.setStatus("mandatory")
_Es400PortStatBroadcastFramesRx_Type = Counter32
_Es400PortStatBroadcastFramesRx_Object = MibTableColumn
es400PortStatBroadcastFramesRx = _Es400PortStatBroadcastFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 3, 3, 1, 8),
    _Es400PortStatBroadcastFramesRx_Type()
)
es400PortStatBroadcastFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400PortStatBroadcastFramesRx.setStatus("mandatory")
_Es400PortStatMulticastFramesRx_Type = Counter32
_Es400PortStatMulticastFramesRx_Object = MibTableColumn
es400PortStatMulticastFramesRx = _Es400PortStatMulticastFramesRx_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 3, 3, 1, 9),
    _Es400PortStatMulticastFramesRx_Type()
)
es400PortStatMulticastFramesRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400PortStatMulticastFramesRx.setStatus("mandatory")
_Es400PortStatCRCError_Type = Counter32
_Es400PortStatCRCError_Object = MibTableColumn
es400PortStatCRCError = _Es400PortStatCRCError_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 3, 3, 1, 10),
    _Es400PortStatCRCError_Type()
)
es400PortStatCRCError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400PortStatCRCError.setStatus("mandatory")
_Es400PortStatOversizeFrames_Type = Counter32
_Es400PortStatOversizeFrames_Object = MibTableColumn
es400PortStatOversizeFrames = _Es400PortStatOversizeFrames_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 3, 3, 1, 11),
    _Es400PortStatOversizeFrames_Type()
)
es400PortStatOversizeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400PortStatOversizeFrames.setStatus("mandatory")
_Es400PortStatFragments_Type = Counter32
_Es400PortStatFragments_Object = MibTableColumn
es400PortStatFragments = _Es400PortStatFragments_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 3, 3, 1, 12),
    _Es400PortStatFragments_Type()
)
es400PortStatFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400PortStatFragments.setStatus("mandatory")
_Es400PortStatJabber_Type = Counter32
_Es400PortStatJabber_Object = MibTableColumn
es400PortStatJabber = _Es400PortStatJabber_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 3, 3, 1, 13),
    _Es400PortStatJabber_Type()
)
es400PortStatJabber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400PortStatJabber.setStatus("mandatory")
_Es400PortStatCollision_Type = Counter32
_Es400PortStatCollision_Object = MibTableColumn
es400PortStatCollision = _Es400PortStatCollision_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 3, 3, 1, 14),
    _Es400PortStatCollision_Type()
)
es400PortStatCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400PortStatCollision.setStatus("mandatory")
_Es400PortStatLateCollision_Type = Counter32
_Es400PortStatLateCollision_Object = MibTableColumn
es400PortStatLateCollision = _Es400PortStatLateCollision_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 3, 3, 1, 15),
    _Es400PortStatLateCollision_Type()
)
es400PortStatLateCollision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400PortStatLateCollision.setStatus("mandatory")
_Es400PortStatFrames_64_bytes_Type = Counter32
_Es400PortStatFrames_64_bytes_Object = MibScalar
es400PortStatFrames_64_bytes = _Es400PortStatFrames_64_bytes_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 3, 3, 1, 16),
    _Es400PortStatFrames_64_bytes_Type()
)
es400PortStatFrames_64_bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400PortStatFrames_64_bytes.setStatus("mandatory")
_Es400PortStatFrames_65_127_bytes_Type = Counter32
_Es400PortStatFrames_65_127_bytes_Object = MibScalar
es400PortStatFrames_65_127_bytes = _Es400PortStatFrames_65_127_bytes_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 3, 3, 1, 17),
    _Es400PortStatFrames_65_127_bytes_Type()
)
es400PortStatFrames_65_127_bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400PortStatFrames_65_127_bytes.setStatus("mandatory")
_Es400PortStatFrames_128_255_bytes_Type = Counter32
_Es400PortStatFrames_128_255_bytes_Object = MibScalar
es400PortStatFrames_128_255_bytes = _Es400PortStatFrames_128_255_bytes_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 3, 3, 1, 18),
    _Es400PortStatFrames_128_255_bytes_Type()
)
es400PortStatFrames_128_255_bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400PortStatFrames_128_255_bytes.setStatus("mandatory")
_Es400PortStatFrames_256_511_bytes_Type = Counter32
_Es400PortStatFrames_256_511_bytes_Object = MibScalar
es400PortStatFrames_256_511_bytes = _Es400PortStatFrames_256_511_bytes_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 3, 3, 1, 19),
    _Es400PortStatFrames_256_511_bytes_Type()
)
es400PortStatFrames_256_511_bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400PortStatFrames_256_511_bytes.setStatus("mandatory")
_Es400PortStatFrames_512_1023_bytes_Type = Counter32
_Es400PortStatFrames_512_1023_bytes_Object = MibScalar
es400PortStatFrames_512_1023_bytes = _Es400PortStatFrames_512_1023_bytes_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 3, 3, 1, 20),
    _Es400PortStatFrames_512_1023_bytes_Type()
)
es400PortStatFrames_512_1023_bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400PortStatFrames_512_1023_bytes.setStatus("mandatory")
_Es400PortStatFrames_1024_1536_bytes_Type = Counter32
_Es400PortStatFrames_1024_1536_bytes_Object = MibScalar
es400PortStatFrames_1024_1536_bytes = _Es400PortStatFrames_1024_1536_bytes_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 3, 3, 1, 21),
    _Es400PortStatFrames_1024_1536_bytes_Type()
)
es400PortStatFrames_1024_1536_bytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400PortStatFrames_1024_1536_bytes.setStatus("mandatory")
_Es400PortStatFramesDroppedFrames_Type = Counter32
_Es400PortStatFramesDroppedFrames_Object = MibTableColumn
es400PortStatFramesDroppedFrames = _Es400PortStatFramesDroppedFrames_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 3, 3, 1, 22),
    _Es400PortStatFramesDroppedFrames_Type()
)
es400PortStatFramesDroppedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400PortStatFramesDroppedFrames.setStatus("mandatory")
_Es400PortStatMulticastFramesTx_Type = Counter32
_Es400PortStatMulticastFramesTx_Object = MibTableColumn
es400PortStatMulticastFramesTx = _Es400PortStatMulticastFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 3, 3, 1, 23),
    _Es400PortStatMulticastFramesTx_Type()
)
es400PortStatMulticastFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400PortStatMulticastFramesTx.setStatus("mandatory")
_Es400PortStatBroadcastFramesTx_Type = Counter32
_Es400PortStatBroadcastFramesTx_Object = MibTableColumn
es400PortStatBroadcastFramesTx = _Es400PortStatBroadcastFramesTx_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 3, 3, 1, 24),
    _Es400PortStatBroadcastFramesTx_Type()
)
es400PortStatBroadcastFramesTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400PortStatBroadcastFramesTx.setStatus("mandatory")
_Es400PortStatUndersizeFrames_Type = Counter32
_Es400PortStatUndersizeFrames_Object = MibTableColumn
es400PortStatUndersizeFrames = _Es400PortStatUndersizeFrames_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 3, 3, 1, 25),
    _Es400PortStatUndersizeFrames_Type()
)
es400PortStatUndersizeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400PortStatUndersizeFrames.setStatus("mandatory")
_Es400FDb_ObjectIdentity = ObjectIdentity
es400FDb = _Es400FDb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 4)
)
_Es400FDbStaticTable_Object = MibTable
es400FDbStaticTable = _Es400FDbStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 4, 1)
)
if mibBuilder.loadTexts:
    es400FDbStaticTable.setStatus("mandatory")
_Es400FDbStaticEntry_Object = MibTableRow
es400FDbStaticEntry = _Es400FDbStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 4, 1, 1)
)
es400FDbStaticEntry.setIndexNames(
    (0, "INTEL-ES400-MIB", "es400FdbStaticVid"),
    (0, "INTEL-ES400-MIB", "es400FDbStaticAddressIndex"),
)
if mibBuilder.loadTexts:
    es400FDbStaticEntry.setStatus("mandatory")
_Es400FdbStaticVid_Type = Integer32
_Es400FdbStaticVid_Object = MibTableColumn
es400FdbStaticVid = _Es400FdbStaticVid_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 4, 1, 1, 1),
    _Es400FdbStaticVid_Type()
)
es400FdbStaticVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400FdbStaticVid.setStatus("mandatory")
_Es400FDbStaticAddressIndex_Type = MacAddress
_Es400FDbStaticAddressIndex_Object = MibTableColumn
es400FDbStaticAddressIndex = _Es400FDbStaticAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 4, 1, 1, 2),
    _Es400FDbStaticAddressIndex_Type()
)
es400FDbStaticAddressIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400FDbStaticAddressIndex.setStatus("mandatory")


class _Es400FDbStaticPortMap_Type(OctetString):
    """Custom type es400FDbStaticPortMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_Es400FDbStaticPortMap_Type.__name__ = "OctetString"
_Es400FDbStaticPortMap_Object = MibTableColumn
es400FDbStaticPortMap = _Es400FDbStaticPortMap_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 4, 1, 1, 3),
    _Es400FDbStaticPortMap_Type()
)
es400FDbStaticPortMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es400FDbStaticPortMap.setStatus("mandatory")


class _Es400FDbStaticState_Type(Integer32):
    """Custom type es400FDbStaticState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("other", 1),
          ("valid", 3))
    )


_Es400FDbStaticState_Type.__name__ = "Integer32"
_Es400FDbStaticState_Object = MibTableColumn
es400FDbStaticState = _Es400FDbStaticState_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 4, 1, 1, 4),
    _Es400FDbStaticState_Type()
)
es400FDbStaticState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es400FDbStaticState.setStatus("mandatory")


class _Es400FDbStaticStatus_Type(Integer32):
    """Custom type es400FDbStaticStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("apply", 2),
          ("not-apply", 3),
          ("other", 1))
    )


_Es400FDbStaticStatus_Type.__name__ = "Integer32"
_Es400FDbStaticStatus_Object = MibTableColumn
es400FDbStaticStatus = _Es400FDbStaticStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 4, 1, 1, 5),
    _Es400FDbStaticStatus_Type()
)
es400FDbStaticStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400FDbStaticStatus.setStatus("mandatory")
_Es400FDbFilterTable_Object = MibTable
es400FDbFilterTable = _Es400FDbFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 4, 2)
)
if mibBuilder.loadTexts:
    es400FDbFilterTable.setStatus("mandatory")
_Es400FDbFilterEntry_Object = MibTableRow
es400FDbFilterEntry = _Es400FDbFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 4, 2, 1)
)
es400FDbFilterEntry.setIndexNames(
    (0, "INTEL-ES400-MIB", "es400FdbFilterVid"),
    (0, "INTEL-ES400-MIB", "es400FDbFilterAddressIndex"),
)
if mibBuilder.loadTexts:
    es400FDbFilterEntry.setStatus("mandatory")
_Es400FdbFilterVid_Type = Integer32
_Es400FdbFilterVid_Object = MibTableColumn
es400FdbFilterVid = _Es400FdbFilterVid_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 4, 2, 1, 1),
    _Es400FdbFilterVid_Type()
)
es400FdbFilterVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400FdbFilterVid.setStatus("mandatory")
_Es400FDbFilterAddressIndex_Type = MacAddress
_Es400FDbFilterAddressIndex_Object = MibTableColumn
es400FDbFilterAddressIndex = _Es400FDbFilterAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 4, 2, 1, 2),
    _Es400FDbFilterAddressIndex_Type()
)
es400FDbFilterAddressIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400FDbFilterAddressIndex.setStatus("mandatory")


class _Es400FDbFilterState_Type(Integer32):
    """Custom type es400FDbFilterState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dst-src-addr", 2),
          ("invalid", 3),
          ("other", 1))
    )


_Es400FDbFilterState_Type.__name__ = "Integer32"
_Es400FDbFilterState_Object = MibTableColumn
es400FDbFilterState = _Es400FDbFilterState_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 4, 2, 1, 3),
    _Es400FDbFilterState_Type()
)
es400FDbFilterState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es400FDbFilterState.setStatus("mandatory")
_Es400LinkAggr_ObjectIdentity = ObjectIdentity
es400LinkAggr = _Es400LinkAggr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 5)
)
_Es400LinkAggrTable_Object = MibTable
es400LinkAggrTable = _Es400LinkAggrTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 5, 1)
)
if mibBuilder.loadTexts:
    es400LinkAggrTable.setStatus("mandatory")
_Es400LinkAggrEntry_Object = MibTableRow
es400LinkAggrEntry = _Es400LinkAggrEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 5, 1, 1)
)
es400LinkAggrEntry.setIndexNames(
    (0, "INTEL-ES400-MIB", "es400LinkAggrIndex"),
)
if mibBuilder.loadTexts:
    es400LinkAggrEntry.setStatus("mandatory")
_Es400LinkAggrIndex_Type = Integer32
_Es400LinkAggrIndex_Object = MibTableColumn
es400LinkAggrIndex = _Es400LinkAggrIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 5, 1, 1, 1),
    _Es400LinkAggrIndex_Type()
)
es400LinkAggrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400LinkAggrIndex.setStatus("mandatory")


class _Es400LinkAggrName_Type(DisplayString):
    """Custom type es400LinkAggrName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(30, 30),
    )


_Es400LinkAggrName_Type.__name__ = "DisplayString"
_Es400LinkAggrName_Object = MibTableColumn
es400LinkAggrName = _Es400LinkAggrName_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 5, 1, 1, 2),
    _Es400LinkAggrName_Type()
)
es400LinkAggrName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es400LinkAggrName.setStatus("mandatory")
_Es400LinkAggrMasterPort_Type = Integer32
_Es400LinkAggrMasterPort_Object = MibTableColumn
es400LinkAggrMasterPort = _Es400LinkAggrMasterPort_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 5, 1, 1, 3),
    _Es400LinkAggrMasterPort_Type()
)
es400LinkAggrMasterPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400LinkAggrMasterPort.setStatus("mandatory")
_Es400LinkAggrMemberNum_Type = Integer32
_Es400LinkAggrMemberNum_Object = MibTableColumn
es400LinkAggrMemberNum = _Es400LinkAggrMemberNum_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 5, 1, 1, 4),
    _Es400LinkAggrMemberNum_Type()
)
es400LinkAggrMemberNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es400LinkAggrMemberNum.setStatus("mandatory")


class _Es400LinkAggrState_Type(Integer32):
    """Custom type es400LinkAggrState based on Integer32"""
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


_Es400LinkAggrState_Type.__name__ = "Integer32"
_Es400LinkAggrState_Object = MibTableColumn
es400LinkAggrState = _Es400LinkAggrState_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 5, 1, 1, 5),
    _Es400LinkAggrState_Type()
)
es400LinkAggrState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es400LinkAggrState.setStatus("mandatory")
_Es400PortMirror_ObjectIdentity = ObjectIdentity
es400PortMirror = _Es400PortMirror_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 6)
)
_Es400PortMirrorCtrlTable_Object = MibTable
es400PortMirrorCtrlTable = _Es400PortMirrorCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 6, 1)
)
if mibBuilder.loadTexts:
    es400PortMirrorCtrlTable.setStatus("mandatory")
_Es400PortMirrorCtrlEntry_Object = MibTableRow
es400PortMirrorCtrlEntry = _Es400PortMirrorCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 6, 1, 1)
)
es400PortMirrorCtrlEntry.setIndexNames(
    (0, "INTEL-ES400-MIB", "es400PortMirrorCtrlIndex"),
)
if mibBuilder.loadTexts:
    es400PortMirrorCtrlEntry.setStatus("mandatory")
_Es400PortMirrorCtrlIndex_Type = Integer32
_Es400PortMirrorCtrlIndex_Object = MibTableColumn
es400PortMirrorCtrlIndex = _Es400PortMirrorCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 6, 1, 1, 1),
    _Es400PortMirrorCtrlIndex_Type()
)
es400PortMirrorCtrlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400PortMirrorCtrlIndex.setStatus("mandatory")


class _Es400PortMirrorCtrlSourcePort_Type(Integer32):
    """Custom type es400PortMirrorCtrlSourcePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_Es400PortMirrorCtrlSourcePort_Type.__name__ = "Integer32"
_Es400PortMirrorCtrlSourcePort_Object = MibTableColumn
es400PortMirrorCtrlSourcePort = _Es400PortMirrorCtrlSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 6, 1, 1, 2),
    _Es400PortMirrorCtrlSourcePort_Type()
)
es400PortMirrorCtrlSourcePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es400PortMirrorCtrlSourcePort.setStatus("mandatory")


class _Es400PortMirrorCtrlTargetPort_Type(Integer32):
    """Custom type es400PortMirrorCtrlTargetPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_Es400PortMirrorCtrlTargetPort_Type.__name__ = "Integer32"
_Es400PortMirrorCtrlTargetPort_Object = MibTableColumn
es400PortMirrorCtrlTargetPort = _Es400PortMirrorCtrlTargetPort_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 6, 1, 1, 3),
    _Es400PortMirrorCtrlTargetPort_Type()
)
es400PortMirrorCtrlTargetPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es400PortMirrorCtrlTargetPort.setStatus("mandatory")


class _Es400PortMirrorCtrlState_Type(Integer32):
    """Custom type es400PortMirrorCtrlState based on Integer32"""
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
          ("enable", 3),
          ("other", 1))
    )


_Es400PortMirrorCtrlState_Type.__name__ = "Integer32"
_Es400PortMirrorCtrlState_Object = MibTableColumn
es400PortMirrorCtrlState = _Es400PortMirrorCtrlState_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 6, 1, 1, 4),
    _Es400PortMirrorCtrlState_Type()
)
es400PortMirrorCtrlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es400PortMirrorCtrlState.setStatus("mandatory")
_Es400IgmpSnoop_ObjectIdentity = ObjectIdentity
es400IgmpSnoop = _Es400IgmpSnoop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 7)
)
_Es400IgmpSnoopConfigTable_Object = MibTable
es400IgmpSnoopConfigTable = _Es400IgmpSnoopConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 7, 1)
)
if mibBuilder.loadTexts:
    es400IgmpSnoopConfigTable.setStatus("mandatory")
_Es400IgmpSnoopConfigEntry_Object = MibTableRow
es400IgmpSnoopConfigEntry = _Es400IgmpSnoopConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 7, 1, 1)
)
es400IgmpSnoopConfigEntry.setIndexNames(
    (0, "INTEL-ES400-MIB", "es400IgmpSnoopConfigIndex"),
)
if mibBuilder.loadTexts:
    es400IgmpSnoopConfigEntry.setStatus("mandatory")


class _Es400IgmpSnoopConfigIndex_Type(Integer32):
    """Custom type es400IgmpSnoopConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_Es400IgmpSnoopConfigIndex_Type.__name__ = "Integer32"
_Es400IgmpSnoopConfigIndex_Object = MibTableColumn
es400IgmpSnoopConfigIndex = _Es400IgmpSnoopConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 7, 1, 1, 1),
    _Es400IgmpSnoopConfigIndex_Type()
)
es400IgmpSnoopConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400IgmpSnoopConfigIndex.setStatus("mandatory")
_Es400IgmpSnoopConfigVid_Type = Integer32
_Es400IgmpSnoopConfigVid_Object = MibTableColumn
es400IgmpSnoopConfigVid = _Es400IgmpSnoopConfigVid_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 7, 1, 1, 2),
    _Es400IgmpSnoopConfigVid_Type()
)
es400IgmpSnoopConfigVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es400IgmpSnoopConfigVid.setStatus("mandatory")


class _Es400IgmpSnoopConfigTimer_Type(Integer32):
    """Custom type es400IgmpSnoopConfigTimer based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 9999),
    )


_Es400IgmpSnoopConfigTimer_Type.__name__ = "Integer32"
_Es400IgmpSnoopConfigTimer_Object = MibTableColumn
es400IgmpSnoopConfigTimer = _Es400IgmpSnoopConfigTimer_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 7, 1, 1, 3),
    _Es400IgmpSnoopConfigTimer_Type()
)
es400IgmpSnoopConfigTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es400IgmpSnoopConfigTimer.setStatus("mandatory")


class _Es400IgmpSnoopConfigState_Type(Integer32):
    """Custom type es400IgmpSnoopConfigState based on Integer32"""
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
          ("enable", 3),
          ("other", 1))
    )


_Es400IgmpSnoopConfigState_Type.__name__ = "Integer32"
_Es400IgmpSnoopConfigState_Object = MibTableColumn
es400IgmpSnoopConfigState = _Es400IgmpSnoopConfigState_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 7, 1, 1, 4),
    _Es400IgmpSnoopConfigState_Type()
)
es400IgmpSnoopConfigState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es400IgmpSnoopConfigState.setStatus("mandatory")
_Es400IgmpSnoopInfoTable_Object = MibTable
es400IgmpSnoopInfoTable = _Es400IgmpSnoopInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 7, 2)
)
if mibBuilder.loadTexts:
    es400IgmpSnoopInfoTable.setStatus("mandatory")
_Es400IgmpSnoopInfoEntry_Object = MibTableRow
es400IgmpSnoopInfoEntry = _Es400IgmpSnoopInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 7, 2, 1)
)
es400IgmpSnoopInfoEntry.setIndexNames(
    (0, "INTEL-ES400-MIB", "es400IgmpSnoopInfoIndex"),
)
if mibBuilder.loadTexts:
    es400IgmpSnoopInfoEntry.setStatus("mandatory")


class _Es400IgmpSnoopInfoIndex_Type(Integer32):
    """Custom type es400IgmpSnoopInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_Es400IgmpSnoopInfoIndex_Type.__name__ = "Integer32"
_Es400IgmpSnoopInfoIndex_Object = MibTableColumn
es400IgmpSnoopInfoIndex = _Es400IgmpSnoopInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 7, 2, 1, 1),
    _Es400IgmpSnoopInfoIndex_Type()
)
es400IgmpSnoopInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400IgmpSnoopInfoIndex.setStatus("mandatory")
_Es400IgmpSnoopInfoVid_Type = Integer32
_Es400IgmpSnoopInfoVid_Object = MibTableColumn
es400IgmpSnoopInfoVid = _Es400IgmpSnoopInfoVid_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 7, 2, 1, 2),
    _Es400IgmpSnoopInfoVid_Type()
)
es400IgmpSnoopInfoVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400IgmpSnoopInfoVid.setStatus("mandatory")
_Es400IgmpSnoopInfoQueryCount_Type = Integer32
_Es400IgmpSnoopInfoQueryCount_Object = MibTableColumn
es400IgmpSnoopInfoQueryCount = _Es400IgmpSnoopInfoQueryCount_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 7, 2, 1, 3),
    _Es400IgmpSnoopInfoQueryCount_Type()
)
es400IgmpSnoopInfoQueryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400IgmpSnoopInfoQueryCount.setStatus("mandatory")
_Es400IgmpSnoopInfoTxQueryCount_Type = Integer32
_Es400IgmpSnoopInfoTxQueryCount_Object = MibTableColumn
es400IgmpSnoopInfoTxQueryCount = _Es400IgmpSnoopInfoTxQueryCount_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 7, 2, 1, 4),
    _Es400IgmpSnoopInfoTxQueryCount_Type()
)
es400IgmpSnoopInfoTxQueryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400IgmpSnoopInfoTxQueryCount.setStatus("mandatory")
_Es400IgmpSnoopTable_Object = MibTable
es400IgmpSnoopTable = _Es400IgmpSnoopTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 7, 3)
)
if mibBuilder.loadTexts:
    es400IgmpSnoopTable.setStatus("mandatory")
_Es400IgmpSnoopEntry_Object = MibTableRow
es400IgmpSnoopEntry = _Es400IgmpSnoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 7, 3, 1)
)
es400IgmpSnoopEntry.setIndexNames(
    (0, "INTEL-ES400-MIB", "es400IgmpSnoopVid"),
    (0, "INTEL-ES400-MIB", "es400IgmpSnoopGroupIpAddr"),
)
if mibBuilder.loadTexts:
    es400IgmpSnoopEntry.setStatus("mandatory")
_Es400IgmpSnoopVid_Type = Integer32
_Es400IgmpSnoopVid_Object = MibTableColumn
es400IgmpSnoopVid = _Es400IgmpSnoopVid_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 7, 3, 1, 1),
    _Es400IgmpSnoopVid_Type()
)
es400IgmpSnoopVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400IgmpSnoopVid.setStatus("mandatory")
_Es400IgmpSnoopGroupIpAddr_Type = IpAddress
_Es400IgmpSnoopGroupIpAddr_Object = MibTableColumn
es400IgmpSnoopGroupIpAddr = _Es400IgmpSnoopGroupIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 7, 3, 1, 2),
    _Es400IgmpSnoopGroupIpAddr_Type()
)
es400IgmpSnoopGroupIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400IgmpSnoopGroupIpAddr.setStatus("mandatory")
_Es400IgmpSnoopMacAddr_Type = MacAddress
_Es400IgmpSnoopMacAddr_Object = MibTableColumn
es400IgmpSnoopMacAddr = _Es400IgmpSnoopMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 7, 3, 1, 3),
    _Es400IgmpSnoopMacAddr_Type()
)
es400IgmpSnoopMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400IgmpSnoopMacAddr.setStatus("mandatory")
_Es400IgmpSnoopPortMap_Type = PortList
_Es400IgmpSnoopPortMap_Object = MibTableColumn
es400IgmpSnoopPortMap = _Es400IgmpSnoopPortMap_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 7, 3, 1, 4),
    _Es400IgmpSnoopPortMap_Type()
)
es400IgmpSnoopPortMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400IgmpSnoopPortMap.setStatus("mandatory")
_Es400IgmpSnoopReportCount_Type = Integer32
_Es400IgmpSnoopReportCount_Object = MibTableColumn
es400IgmpSnoopReportCount = _Es400IgmpSnoopReportCount_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 7, 3, 1, 5),
    _Es400IgmpSnoopReportCount_Type()
)
es400IgmpSnoopReportCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400IgmpSnoopReportCount.setStatus("mandatory")
_Es400Vlan_ObjectIdentity = ObjectIdentity
es400Vlan = _Es400Vlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 8)
)


class _Es400VlanConfigMode_Type(Integer32):
    """Custom type es400VlanConfigMode based on Integer32"""
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
        *(("disabled", 2),
          ("ieee8021q", 5),
          ("mac-base", 3),
          ("other", 1),
          ("port-base", 4))
    )


_Es400VlanConfigMode_Type.__name__ = "Integer32"
_Es400VlanConfigMode_Object = MibScalar
es400VlanConfigMode = _Es400VlanConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 8, 1),
    _Es400VlanConfigMode_Type()
)
es400VlanConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es400VlanConfigMode.setStatus("mandatory")


class _Es400VlanInfoStatus_Type(Integer32):
    """Custom type es400VlanInfoStatus based on Integer32"""
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
        *(("disabled", 2),
          ("ieee8021q", 5),
          ("mac-base", 3),
          ("other", 1),
          ("port-base", 4))
    )


_Es400VlanInfoStatus_Type.__name__ = "Integer32"
_Es400VlanInfoStatus_Object = MibScalar
es400VlanInfoStatus = _Es400VlanInfoStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 8, 2),
    _Es400VlanInfoStatus_Type()
)
es400VlanInfoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400VlanInfoStatus.setStatus("mandatory")


class _Es400VlanSnmpPortInfo_Type(VlanIndex):
    """Custom type es400VlanSnmpPortInfo based on VlanIndex"""
    subtypeSpec = VlanIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Es400VlanSnmpPortInfo_Type.__name__ = "VlanIndex"
_Es400VlanSnmpPortInfo_Object = MibScalar
es400VlanSnmpPortInfo = _Es400VlanSnmpPortInfo_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 8, 3),
    _Es400VlanSnmpPortInfo_Type()
)
es400VlanSnmpPortInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es400VlanSnmpPortInfo.setStatus("mandatory")
_Es400MacVlan_ObjectIdentity = ObjectIdentity
es400MacVlan = _Es400MacVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 8, 4)
)
_Es400MacVlanTotalNum_Type = Integer32
_Es400MacVlanTotalNum_Object = MibScalar
es400MacVlanTotalNum = _Es400MacVlanTotalNum_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 8, 4, 1),
    _Es400MacVlanTotalNum_Type()
)
es400MacVlanTotalNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400MacVlanTotalNum.setStatus("mandatory")
_Es400MacVlanConfigTable_Object = MibTable
es400MacVlanConfigTable = _Es400MacVlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 8, 4, 2)
)
if mibBuilder.loadTexts:
    es400MacVlanConfigTable.setStatus("mandatory")
_Es400MacVlanConfigEntry_Object = MibTableRow
es400MacVlanConfigEntry = _Es400MacVlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 8, 4, 2, 1)
)
es400MacVlanConfigEntry.setIndexNames(
    (0, "INTEL-ES400-MIB", "es400MacVlanDesc"),
)
if mibBuilder.loadTexts:
    es400MacVlanConfigEntry.setStatus("mandatory")


class _Es400MacVlanDesc_Type(DisplayString):
    """Custom type es400MacVlanDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_Es400MacVlanDesc_Type.__name__ = "DisplayString"
_Es400MacVlanDesc_Object = MibTableColumn
es400MacVlanDesc = _Es400MacVlanDesc_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 8, 4, 2, 1, 1),
    _Es400MacVlanDesc_Type()
)
es400MacVlanDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400MacVlanDesc.setStatus("mandatory")
_Es400MacVlanMacMemberNum_Type = Integer32
_Es400MacVlanMacMemberNum_Object = MibTableColumn
es400MacVlanMacMemberNum = _Es400MacVlanMacMemberNum_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 8, 4, 2, 1, 2),
    _Es400MacVlanMacMemberNum_Type()
)
es400MacVlanMacMemberNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400MacVlanMacMemberNum.setStatus("mandatory")


class _Es400MacVlanCtrlState_Type(Integer32):
    """Custom type es400MacVlanCtrlState based on Integer32"""
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


_Es400MacVlanCtrlState_Type.__name__ = "Integer32"
_Es400MacVlanCtrlState_Object = MibTableColumn
es400MacVlanCtrlState = _Es400MacVlanCtrlState_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 8, 4, 2, 1, 3),
    _Es400MacVlanCtrlState_Type()
)
es400MacVlanCtrlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es400MacVlanCtrlState.setStatus("mandatory")
_Es400MacVlanAddrTotalNum_Type = Integer32
_Es400MacVlanAddrTotalNum_Object = MibScalar
es400MacVlanAddrTotalNum = _Es400MacVlanAddrTotalNum_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 8, 4, 3),
    _Es400MacVlanAddrTotalNum_Type()
)
es400MacVlanAddrTotalNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400MacVlanAddrTotalNum.setStatus("mandatory")
_Es400MacVlanAddrTable_Object = MibTable
es400MacVlanAddrTable = _Es400MacVlanAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 8, 4, 4)
)
if mibBuilder.loadTexts:
    es400MacVlanAddrTable.setStatus("mandatory")
_Es400MacVlanAddrEntry_Object = MibTableRow
es400MacVlanAddrEntry = _Es400MacVlanAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 8, 4, 4, 1)
)
es400MacVlanAddrEntry.setIndexNames(
    (0, "INTEL-ES400-MIB", "es400MacVlanAddress"),
)
if mibBuilder.loadTexts:
    es400MacVlanAddrEntry.setStatus("mandatory")
_Es400MacVlanAddress_Type = MacAddress
_Es400MacVlanAddress_Object = MibTableColumn
es400MacVlanAddress = _Es400MacVlanAddress_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 8, 4, 4, 1, 1),
    _Es400MacVlanAddress_Type()
)
es400MacVlanAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400MacVlanAddress.setStatus("mandatory")


class _Es400MacVlanAddrDesc_Type(DisplayString):
    """Custom type es400MacVlanAddrDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_Es400MacVlanAddrDesc_Type.__name__ = "DisplayString"
_Es400MacVlanAddrDesc_Object = MibTableColumn
es400MacVlanAddrDesc = _Es400MacVlanAddrDesc_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 8, 4, 4, 1, 2),
    _Es400MacVlanAddrDesc_Type()
)
es400MacVlanAddrDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es400MacVlanAddrDesc.setStatus("mandatory")


class _Es400MacVlanAddrState_Type(Integer32):
    """Custom type es400MacVlanAddrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("other", 1),
          ("valid", 3))
    )


_Es400MacVlanAddrState_Type.__name__ = "Integer32"
_Es400MacVlanAddrState_Object = MibTableColumn
es400MacVlanAddrState = _Es400MacVlanAddrState_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 8, 4, 4, 1, 3),
    _Es400MacVlanAddrState_Type()
)
es400MacVlanAddrState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es400MacVlanAddrState.setStatus("mandatory")


class _Es400MacVlanAddrStatus_Type(Integer32):
    """Custom type es400MacVlanAddrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("apply", 2),
          ("not-apply", 3),
          ("other", 1))
    )


_Es400MacVlanAddrStatus_Type.__name__ = "Integer32"
_Es400MacVlanAddrStatus_Object = MibTableColumn
es400MacVlanAddrStatus = _Es400MacVlanAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 8, 4, 4, 1, 4),
    _Es400MacVlanAddrStatus_Type()
)
es400MacVlanAddrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400MacVlanAddrStatus.setStatus("mandatory")
_Es400PortVlan_ObjectIdentity = ObjectIdentity
es400PortVlan = _Es400PortVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 8, 5)
)
_Es400PortVlanTotalNum_Type = Integer32
_Es400PortVlanTotalNum_Object = MibScalar
es400PortVlanTotalNum = _Es400PortVlanTotalNum_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 8, 5, 1),
    _Es400PortVlanTotalNum_Type()
)
es400PortVlanTotalNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400PortVlanTotalNum.setStatus("mandatory")
_Es400PortVlanDefaultVlanTable_Object = MibTable
es400PortVlanDefaultVlanTable = _Es400PortVlanDefaultVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 8, 5, 2)
)
if mibBuilder.loadTexts:
    es400PortVlanDefaultVlanTable.setStatus("mandatory")
_Es400PortVlanDefaultVlanEntry_Object = MibTableRow
es400PortVlanDefaultVlanEntry = _Es400PortVlanDefaultVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 8, 5, 2, 1)
)
es400PortVlanDefaultVlanEntry.setIndexNames(
    (0, "INTEL-ES400-MIB", "es400PortVlanDefaultPvid"),
)
if mibBuilder.loadTexts:
    es400PortVlanDefaultVlanEntry.setStatus("mandatory")
_Es400PortVlanDefaultPvid_Type = Integer32
_Es400PortVlanDefaultPvid_Object = MibTableColumn
es400PortVlanDefaultPvid = _Es400PortVlanDefaultPvid_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 8, 5, 2, 1, 1),
    _Es400PortVlanDefaultPvid_Type()
)
es400PortVlanDefaultPvid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400PortVlanDefaultPvid.setStatus("mandatory")


class _Es400PortVlanDefaultDesc_Type(DisplayString):
    """Custom type es400PortVlanDefaultDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_Es400PortVlanDefaultDesc_Type.__name__ = "DisplayString"
_Es400PortVlanDefaultDesc_Object = MibTableColumn
es400PortVlanDefaultDesc = _Es400PortVlanDefaultDesc_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 8, 5, 2, 1, 2),
    _Es400PortVlanDefaultDesc_Type()
)
es400PortVlanDefaultDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400PortVlanDefaultDesc.setStatus("mandatory")
_Es400PortVlanDefaultPortList_Type = PortList
_Es400PortVlanDefaultPortList_Object = MibTableColumn
es400PortVlanDefaultPortList = _Es400PortVlanDefaultPortList_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 8, 5, 2, 1, 3),
    _Es400PortVlanDefaultPortList_Type()
)
es400PortVlanDefaultPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400PortVlanDefaultPortList.setStatus("mandatory")
_Es400PortVlanDefaultPortNumber_Type = Integer32
_Es400PortVlanDefaultPortNumber_Object = MibTableColumn
es400PortVlanDefaultPortNumber = _Es400PortVlanDefaultPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 8, 5, 2, 1, 4),
    _Es400PortVlanDefaultPortNumber_Type()
)
es400PortVlanDefaultPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400PortVlanDefaultPortNumber.setStatus("mandatory")
_Es400PortVlanConfigTable_Object = MibTable
es400PortVlanConfigTable = _Es400PortVlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 8, 5, 3)
)
if mibBuilder.loadTexts:
    es400PortVlanConfigTable.setStatus("mandatory")
_Es400PortVlanConfigEntry_Object = MibTableRow
es400PortVlanConfigEntry = _Es400PortVlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 8, 5, 3, 1)
)
es400PortVlanConfigEntry.setIndexNames(
    (0, "INTEL-ES400-MIB", "es400PortVlanConfigPvid"),
)
if mibBuilder.loadTexts:
    es400PortVlanConfigEntry.setStatus("mandatory")


class _Es400PortVlanConfigPvid_Type(Integer32):
    """Custom type es400PortVlanConfigPvid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 12),
    )


_Es400PortVlanConfigPvid_Type.__name__ = "Integer32"
_Es400PortVlanConfigPvid_Object = MibTableColumn
es400PortVlanConfigPvid = _Es400PortVlanConfigPvid_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 8, 5, 3, 1, 1),
    _Es400PortVlanConfigPvid_Type()
)
es400PortVlanConfigPvid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400PortVlanConfigPvid.setStatus("mandatory")


class _Es400PortVlanConfigDesc_Type(DisplayString):
    """Custom type es400PortVlanConfigDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_Es400PortVlanConfigDesc_Type.__name__ = "DisplayString"
_Es400PortVlanConfigDesc_Object = MibTableColumn
es400PortVlanConfigDesc = _Es400PortVlanConfigDesc_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 8, 5, 3, 1, 2),
    _Es400PortVlanConfigDesc_Type()
)
es400PortVlanConfigDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es400PortVlanConfigDesc.setStatus("mandatory")
_Es400PortVlanConfigPortList_Type = PortList
_Es400PortVlanConfigPortList_Object = MibTableColumn
es400PortVlanConfigPortList = _Es400PortVlanConfigPortList_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 8, 5, 3, 1, 3),
    _Es400PortVlanConfigPortList_Type()
)
es400PortVlanConfigPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es400PortVlanConfigPortList.setStatus("mandatory")
_Es400PortVlanConfigPortNumber_Type = Integer32
_Es400PortVlanConfigPortNumber_Object = MibTableColumn
es400PortVlanConfigPortNumber = _Es400PortVlanConfigPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 8, 5, 3, 1, 4),
    _Es400PortVlanConfigPortNumber_Type()
)
es400PortVlanConfigPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    es400PortVlanConfigPortNumber.setStatus("mandatory")


class _Es400PortVlanConfigState_Type(Integer32):
    """Custom type es400PortVlanConfigState based on Integer32"""
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


_Es400PortVlanConfigState_Type.__name__ = "Integer32"
_Es400PortVlanConfigState_Object = MibTableColumn
es400PortVlanConfigState = _Es400PortVlanConfigState_Object(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 8, 5, 3, 1, 5),
    _Es400PortVlanConfigState_Type()
)
es400PortVlanConfigState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    es400PortVlanConfigState.setStatus("mandatory")

# Managed Objects groups


# Notification objects

portPartition = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 0, 1)
)
portPartition.setObjects(
    ("INTEL-ES400-MIB", "es400PortInfoIndex")
)
if mibBuilder.loadTexts:
    portPartition.setStatus(
        ""
    )

linkChangeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 0, 2)
)
linkChangeEvent.setObjects(
    ("INTEL-ES400-MIB", "es400PortInfoIndex")
)
if mibBuilder.loadTexts:
    linkChangeEvent.setStatus(
        ""
    )

broadcastRisingStorm = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 0, 3)
)
broadcastRisingStorm.setObjects(
    ("INTEL-ES400-MIB", "es400PortInfoIndex")
)
if mibBuilder.loadTexts:
    broadcastRisingStorm.setStatus(
        ""
    )

broadcastFallingStorm = NotificationType(
    (1, 3, 6, 1, 4, 1, 343, 6, 17, 0, 4)
)
broadcastFallingStorm.setObjects(
    ("INTEL-ES400-MIB", "es400PortInfoIndex")
)
if mibBuilder.loadTexts:
    broadcastFallingStorm.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INTEL-ES400-MIB",
    **{"MacAddress": MacAddress,
       "PortList": PortList,
       "VlanIndex": VlanIndex,
       "intel": intel,
       "mib2ext": mib2ext,
       "es400": es400,
       "portPartition": portPartition,
       "linkChangeEvent": linkChangeEvent,
       "broadcastRisingStorm": broadcastRisingStorm,
       "broadcastFallingStorm": broadcastFallingStorm,
       "es400Agent": es400Agent,
       "es400AgentInfo": es400AgentInfo,
       "es400AgentRuntimeSwVersion": es400AgentRuntimeSwVersion,
       "es400AgentPromFwVersion": es400AgentPromFwVersion,
       "es400AgentHwRevision": es400AgentHwRevision,
       "es400AgentMgmtProtocolCapability": es400AgentMgmtProtocolCapability,
       "es400AgentMibSupportTable": es400AgentMibSupportTable,
       "es400AgentMibSupportEntry": es400AgentMibSupportEntry,
       "es400AgentMibSupportIndex": es400AgentMibSupportIndex,
       "es400AgentMibSupportDescr": es400AgentMibSupportDescr,
       "es400AgentMibSupportVersion": es400AgentMibSupportVersion,
       "es400AgentMibSupportType": es400AgentMibSupportType,
       "es400AgentConfig": es400AgentConfig,
       "es400AgentSwUpdateMode": es400AgentSwUpdateMode,
       "es400AgentSwUpdateCtrl": es400AgentSwUpdateCtrl,
       "es400AgentBootFile": es400AgentBootFile,
       "es400AgentFirmwareUpdateCtrl": es400AgentFirmwareUpdateCtrl,
       "es400AgentFirmwareFile": es400AgentFirmwareFile,
       "es400AgentSystemReset": es400AgentSystemReset,
       "es400AgentRs232PortConfig": es400AgentRs232PortConfig,
       "es400AgentOutOfBandBaudRateConfig": es400AgentOutOfBandBaudRateConfig,
       "es400AgentIpConfig": es400AgentIpConfig,
       "es400AgentIpNumOfIf": es400AgentIpNumOfIf,
       "es400AgentIpIfTable": es400AgentIpIfTable,
       "es400AgentIpIfEntry": es400AgentIpIfEntry,
       "es400AgentIpIfIndex": es400AgentIpIfIndex,
       "es400AgentIpIfAddress": es400AgentIpIfAddress,
       "es400AgentIpIfNetMask": es400AgentIpIfNetMask,
       "es400AgentIpIfDefaultRouter": es400AgentIpIfDefaultRouter,
       "es400AgentIpIfMacAddr": es400AgentIpIfMacAddr,
       "es400AgentIpIfType": es400AgentIpIfType,
       "es400AgentIpBootServerAddr": es400AgentIpBootServerAddr,
       "es400AgentIpGetIpFromBootpServer": es400AgentIpGetIpFromBootpServer,
       "es400AgentIpUnauthAddr": es400AgentIpUnauthAddr,
       "es400AgentIpUnauthComm": es400AgentIpUnauthComm,
       "es400AgentIpLastBootServerAddr": es400AgentIpLastBootServerAddr,
       "es400AgentIpLastIpAddr": es400AgentIpLastIpAddr,
       "es400AgentTrapAddressTable": es400AgentTrapAddressTable,
       "es400AgentTrapAddressEntry": es400AgentTrapAddressEntry,
       "es400AgentTrapIndex": es400AgentTrapIndex,
       "es400AgentTrapAddressIp": es400AgentTrapAddressIp,
       "es400AgentTrapAddressComm": es400AgentTrapAddressComm,
       "es400AgentTrapAddressStatus": es400AgentTrapAddressStatus,
       "es400Chassis": es400Chassis,
       "es400ChassisInfo": es400ChassisInfo,
       "es400ChassisInfoSystemUpTime": es400ChassisInfoSystemUpTime,
       "es400ChassisInfoTotalNumOfPort": es400ChassisInfoTotalNumOfPort,
       "es400ChassisInfoNumOfPortInUse": es400ChassisInfoNumOfPortInUse,
       "es400ChassisInfoConsoleInUse": es400ChassisInfoConsoleInUse,
       "es400ChassisInfoFrontPanelLedStatus": es400ChassisInfoFrontPanelLedStatus,
       "es400ChassisInfoSaveCfg": es400ChassisInfoSaveCfg,
       "es400ChassisConfig": es400ChassisConfig,
       "es400ChassisConfigStpState": es400ChassisConfigStpState,
       "es400ChassisConfigIGMPCaptureState": es400ChassisConfigIGMPCaptureState,
       "es400ChassisConfigPartitionModeState": es400ChassisConfigPartitionModeState,
       "es400ChassisConfigTableLockState": es400ChassisConfigTableLockState,
       "es400ChassisConfigSaveCfg": es400ChassisConfigSaveCfg,
       "es400ChassisConfigHOLState": es400ChassisConfigHOLState,
       "es400ChassisConfigAddrLookupModes": es400ChassisConfigAddrLookupModes,
       "es400ChassisConfigUploadImageFileName": es400ChassisConfigUploadImageFileName,
       "es400ChassisConfigUploadImage": es400ChassisConfigUploadImage,
       "es400ChassisConfigHighPriorityServiceRatio": es400ChassisConfigHighPriorityServiceRatio,
       "es400ChassisAlarm": es400ChassisAlarm,
       "es400ChassisAlarmPartition": es400ChassisAlarmPartition,
       "es400ChassisAlarmNewRoot": es400ChassisAlarmNewRoot,
       "es400ChassisAlarmTopologyChange": es400ChassisAlarmTopologyChange,
       "es400ChassisAlarmLinkChange": es400ChassisAlarmLinkChange,
       "es400Port": es400Port,
       "es400PortInfoTable": es400PortInfoTable,
       "es400PortInfoEntry": es400PortInfoEntry,
       "es400PortInfoIndex": es400PortInfoIndex,
       "es400PortInfoType": es400PortInfoType,
       "es400PortInfoLinkStatus": es400PortInfoLinkStatus,
       "es400PortInfoNwayStatus": es400PortInfoNwayStatus,
       "es400PortInfoFlowCtrlStatus": es400PortInfoFlowCtrlStatus,
       "es400PortConfigTable": es400PortConfigTable,
       "es400PortConfigEntry": es400PortConfigEntry,
       "es400PortConfigIndex": es400PortConfigIndex,
       "es400PortConfigAdminState": es400PortConfigAdminState,
       "es400PortConfigLinkStatusAlarmState": es400PortConfigLinkStatusAlarmState,
       "es400PortConfigNwayState": es400PortConfigNwayState,
       "es400PortConfigFlowCtrlState": es400PortConfigFlowCtrlState,
       "es400PortConfigBackPressState": es400PortConfigBackPressState,
       "es400PortConfigLockState": es400PortConfigLockState,
       "es400PortConfigPriority": es400PortConfigPriority,
       "es400PortConfigStpState": es400PortConfigStpState,
       "es400PortConfigHOLState": es400PortConfigHOLState,
       "es400PortConfigBroadcastStormThr": es400PortConfigBroadcastStormThr,
       "es400PortConfigBroadcastStormCtrl": es400PortConfigBroadcastStormCtrl,
       "es400PortConfigCleanAllStatisticCounter": es400PortConfigCleanAllStatisticCounter,
       "es400PortStatTable": es400PortStatTable,
       "es400PortStatEntry": es400PortStatEntry,
       "es400PortStatIndex": es400PortStatIndex,
       "es400PortStatByteRx": es400PortStatByteRx,
       "es400PortStatByteTx": es400PortStatByteTx,
       "es400PortStatFrameRx": es400PortStatFrameRx,
       "es400PortStatFrameTx": es400PortStatFrameTx,
       "es400PortStatTotalBytesRx": es400PortStatTotalBytesRx,
       "es400PortStatTotalFramesRx": es400PortStatTotalFramesRx,
       "es400PortStatBroadcastFramesRx": es400PortStatBroadcastFramesRx,
       "es400PortStatMulticastFramesRx": es400PortStatMulticastFramesRx,
       "es400PortStatCRCError": es400PortStatCRCError,
       "es400PortStatOversizeFrames": es400PortStatOversizeFrames,
       "es400PortStatFragments": es400PortStatFragments,
       "es400PortStatJabber": es400PortStatJabber,
       "es400PortStatCollision": es400PortStatCollision,
       "es400PortStatLateCollision": es400PortStatLateCollision,
       "es400PortStatFrames-64-bytes": es400PortStatFrames_64_bytes,
       "es400PortStatFrames-65-127-bytes": es400PortStatFrames_65_127_bytes,
       "es400PortStatFrames-128-255-bytes": es400PortStatFrames_128_255_bytes,
       "es400PortStatFrames-256-511-bytes": es400PortStatFrames_256_511_bytes,
       "es400PortStatFrames-512-1023-bytes": es400PortStatFrames_512_1023_bytes,
       "es400PortStatFrames-1024-1536-bytes": es400PortStatFrames_1024_1536_bytes,
       "es400PortStatFramesDroppedFrames": es400PortStatFramesDroppedFrames,
       "es400PortStatMulticastFramesTx": es400PortStatMulticastFramesTx,
       "es400PortStatBroadcastFramesTx": es400PortStatBroadcastFramesTx,
       "es400PortStatUndersizeFrames": es400PortStatUndersizeFrames,
       "es400FDb": es400FDb,
       "es400FDbStaticTable": es400FDbStaticTable,
       "es400FDbStaticEntry": es400FDbStaticEntry,
       "es400FdbStaticVid": es400FdbStaticVid,
       "es400FDbStaticAddressIndex": es400FDbStaticAddressIndex,
       "es400FDbStaticPortMap": es400FDbStaticPortMap,
       "es400FDbStaticState": es400FDbStaticState,
       "es400FDbStaticStatus": es400FDbStaticStatus,
       "es400FDbFilterTable": es400FDbFilterTable,
       "es400FDbFilterEntry": es400FDbFilterEntry,
       "es400FdbFilterVid": es400FdbFilterVid,
       "es400FDbFilterAddressIndex": es400FDbFilterAddressIndex,
       "es400FDbFilterState": es400FDbFilterState,
       "es400LinkAggr": es400LinkAggr,
       "es400LinkAggrTable": es400LinkAggrTable,
       "es400LinkAggrEntry": es400LinkAggrEntry,
       "es400LinkAggrIndex": es400LinkAggrIndex,
       "es400LinkAggrName": es400LinkAggrName,
       "es400LinkAggrMasterPort": es400LinkAggrMasterPort,
       "es400LinkAggrMemberNum": es400LinkAggrMemberNum,
       "es400LinkAggrState": es400LinkAggrState,
       "es400PortMirror": es400PortMirror,
       "es400PortMirrorCtrlTable": es400PortMirrorCtrlTable,
       "es400PortMirrorCtrlEntry": es400PortMirrorCtrlEntry,
       "es400PortMirrorCtrlIndex": es400PortMirrorCtrlIndex,
       "es400PortMirrorCtrlSourcePort": es400PortMirrorCtrlSourcePort,
       "es400PortMirrorCtrlTargetPort": es400PortMirrorCtrlTargetPort,
       "es400PortMirrorCtrlState": es400PortMirrorCtrlState,
       "es400IgmpSnoop": es400IgmpSnoop,
       "es400IgmpSnoopConfigTable": es400IgmpSnoopConfigTable,
       "es400IgmpSnoopConfigEntry": es400IgmpSnoopConfigEntry,
       "es400IgmpSnoopConfigIndex": es400IgmpSnoopConfigIndex,
       "es400IgmpSnoopConfigVid": es400IgmpSnoopConfigVid,
       "es400IgmpSnoopConfigTimer": es400IgmpSnoopConfigTimer,
       "es400IgmpSnoopConfigState": es400IgmpSnoopConfigState,
       "es400IgmpSnoopInfoTable": es400IgmpSnoopInfoTable,
       "es400IgmpSnoopInfoEntry": es400IgmpSnoopInfoEntry,
       "es400IgmpSnoopInfoIndex": es400IgmpSnoopInfoIndex,
       "es400IgmpSnoopInfoVid": es400IgmpSnoopInfoVid,
       "es400IgmpSnoopInfoQueryCount": es400IgmpSnoopInfoQueryCount,
       "es400IgmpSnoopInfoTxQueryCount": es400IgmpSnoopInfoTxQueryCount,
       "es400IgmpSnoopTable": es400IgmpSnoopTable,
       "es400IgmpSnoopEntry": es400IgmpSnoopEntry,
       "es400IgmpSnoopVid": es400IgmpSnoopVid,
       "es400IgmpSnoopGroupIpAddr": es400IgmpSnoopGroupIpAddr,
       "es400IgmpSnoopMacAddr": es400IgmpSnoopMacAddr,
       "es400IgmpSnoopPortMap": es400IgmpSnoopPortMap,
       "es400IgmpSnoopReportCount": es400IgmpSnoopReportCount,
       "es400Vlan": es400Vlan,
       "es400VlanConfigMode": es400VlanConfigMode,
       "es400VlanInfoStatus": es400VlanInfoStatus,
       "es400VlanSnmpPortInfo": es400VlanSnmpPortInfo,
       "es400MacVlan": es400MacVlan,
       "es400MacVlanTotalNum": es400MacVlanTotalNum,
       "es400MacVlanConfigTable": es400MacVlanConfigTable,
       "es400MacVlanConfigEntry": es400MacVlanConfigEntry,
       "es400MacVlanDesc": es400MacVlanDesc,
       "es400MacVlanMacMemberNum": es400MacVlanMacMemberNum,
       "es400MacVlanCtrlState": es400MacVlanCtrlState,
       "es400MacVlanAddrTotalNum": es400MacVlanAddrTotalNum,
       "es400MacVlanAddrTable": es400MacVlanAddrTable,
       "es400MacVlanAddrEntry": es400MacVlanAddrEntry,
       "es400MacVlanAddress": es400MacVlanAddress,
       "es400MacVlanAddrDesc": es400MacVlanAddrDesc,
       "es400MacVlanAddrState": es400MacVlanAddrState,
       "es400MacVlanAddrStatus": es400MacVlanAddrStatus,
       "es400PortVlan": es400PortVlan,
       "es400PortVlanTotalNum": es400PortVlanTotalNum,
       "es400PortVlanDefaultVlanTable": es400PortVlanDefaultVlanTable,
       "es400PortVlanDefaultVlanEntry": es400PortVlanDefaultVlanEntry,
       "es400PortVlanDefaultPvid": es400PortVlanDefaultPvid,
       "es400PortVlanDefaultDesc": es400PortVlanDefaultDesc,
       "es400PortVlanDefaultPortList": es400PortVlanDefaultPortList,
       "es400PortVlanDefaultPortNumber": es400PortVlanDefaultPortNumber,
       "es400PortVlanConfigTable": es400PortVlanConfigTable,
       "es400PortVlanConfigEntry": es400PortVlanConfigEntry,
       "es400PortVlanConfigPvid": es400PortVlanConfigPvid,
       "es400PortVlanConfigDesc": es400PortVlanConfigDesc,
       "es400PortVlanConfigPortList": es400PortVlanConfigPortList,
       "es400PortVlanConfigPortNumber": es400PortVlanConfigPortNumber,
       "es400PortVlanConfigState": es400PortVlanConfigState}
)
