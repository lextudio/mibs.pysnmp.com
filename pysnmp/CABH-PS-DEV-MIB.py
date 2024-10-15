# SNMP MIB module (CABH-PS-DEV-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CABH-PS-DEV-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:52:08 2024
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

(cabhCdpLanTransCurCount,
 cabhCdpLanTransThreshold,
 cabhCdpServerDhcpAddress,
 cabhCdpWanDataAddrClientId) = mibBuilder.importSymbols(
    "CABH-CDP-MIB",
    "cabhCdpLanTransCurCount",
    "cabhCdpLanTransThreshold",
    "cabhCdpServerDhcpAddress",
    "cabhCdpWanDataAddrClientId")

(cabhQos2NumActivePolicyHolder,
 cabhQos2PolicyAdmissionControl,
 cabhQos2PolicyHolderEnabled) = mibBuilder.importSymbols(
    "CABH-QOS2-MIB",
    "cabhQos2NumActivePolicyHolder",
    "cabhQos2PolicyAdmissionControl",
    "cabhQos2PolicyHolderEnabled")

(clabProjCableHome,) = mibBuilder.importSymbols(
    "CLAB-DEF-MIB",
    "clabProjCableHome")

(docsDevEvId,
 docsDevEvLevel,
 docsDevEvText,
 docsDevSwCurrentVers,
 docsDevSwFilename,
 docsDevSwServer) = mibBuilder.importSymbols(
    "DOCS-CABLE-DEVICE-MIB",
    "docsDevEvId",
    "docsDevEvLevel",
    "docsDevEvText",
    "docsDevSwCurrentVers",
    "docsDevSwFilename",
    "docsDevSwServer")

(IANAifType,) = mibBuilder.importSymbols(
    "IANAifType-MIB",
    "IANAifType")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(ZeroBasedCounter32,) = mibBuilder.importSymbols(
    "RMON2-MIB",
    "ZeroBasedCounter32")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

cabhPsDevMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1)
)
cabhPsDevMib.setRevisions(
        ("2005-04-08 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CabhPsDevMibObjects_ObjectIdentity = ObjectIdentity
cabhPsDevMibObjects = _CabhPsDevMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1)
)
_CabhPsDevBase_ObjectIdentity = ObjectIdentity
cabhPsDevBase = _CabhPsDevBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 1)
)
_CabhPsDevDateTime_Type = DateAndTime
_CabhPsDevDateTime_Object = MibScalar
cabhPsDevDateTime = _CabhPsDevDateTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 1, 1),
    _CabhPsDevDateTime_Type()
)
cabhPsDevDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhPsDevDateTime.setStatus("current")
_CabhPsDevResetNow_Type = TruthValue
_CabhPsDevResetNow_Object = MibScalar
cabhPsDevResetNow = _CabhPsDevResetNow_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 1, 2),
    _CabhPsDevResetNow_Type()
)
cabhPsDevResetNow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhPsDevResetNow.setStatus("current")


class _CabhPsDevSerialNumber_Type(SnmpAdminString):
    """Custom type cabhPsDevSerialNumber based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CabhPsDevSerialNumber_Type.__name__ = "SnmpAdminString"
_CabhPsDevSerialNumber_Object = MibScalar
cabhPsDevSerialNumber = _CabhPsDevSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 1, 3),
    _CabhPsDevSerialNumber_Type()
)
cabhPsDevSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhPsDevSerialNumber.setStatus("current")


class _CabhPsDevHardwareVersion_Type(SnmpAdminString):
    """Custom type cabhPsDevHardwareVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_CabhPsDevHardwareVersion_Type.__name__ = "SnmpAdminString"
_CabhPsDevHardwareVersion_Object = MibScalar
cabhPsDevHardwareVersion = _CabhPsDevHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 1, 4),
    _CabhPsDevHardwareVersion_Type()
)
cabhPsDevHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhPsDevHardwareVersion.setStatus("current")


class _CabhPsDevWanManMacAddress_Type(PhysAddress):
    """Custom type cabhPsDevWanManMacAddress based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CabhPsDevWanManMacAddress_Type.__name__ = "PhysAddress"
_CabhPsDevWanManMacAddress_Object = MibScalar
cabhPsDevWanManMacAddress = _CabhPsDevWanManMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 1, 5),
    _CabhPsDevWanManMacAddress_Type()
)
cabhPsDevWanManMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhPsDevWanManMacAddress.setStatus("current")


class _CabhPsDevWanDataMacAddress_Type(PhysAddress):
    """Custom type cabhPsDevWanDataMacAddress based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CabhPsDevWanDataMacAddress_Type.__name__ = "PhysAddress"
_CabhPsDevWanDataMacAddress_Object = MibScalar
cabhPsDevWanDataMacAddress = _CabhPsDevWanDataMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 1, 6),
    _CabhPsDevWanDataMacAddress_Type()
)
cabhPsDevWanDataMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhPsDevWanDataMacAddress.setStatus("current")
_CabhPsDevTypeIdentifier_Type = SnmpAdminString
_CabhPsDevTypeIdentifier_Object = MibScalar
cabhPsDevTypeIdentifier = _CabhPsDevTypeIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 1, 7),
    _CabhPsDevTypeIdentifier_Type()
)
cabhPsDevTypeIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhPsDevTypeIdentifier.setStatus("current")
_CabhPsDevSetToFactory_Type = TruthValue
_CabhPsDevSetToFactory_Object = MibScalar
cabhPsDevSetToFactory = _CabhPsDevSetToFactory_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 1, 8),
    _CabhPsDevSetToFactory_Type()
)
cabhPsDevSetToFactory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhPsDevSetToFactory.setStatus("current")


class _CabhPsDevWanManClientId_Type(OctetString):
    """Custom type cabhPsDevWanManClientId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_CabhPsDevWanManClientId_Type.__name__ = "OctetString"
_CabhPsDevWanManClientId_Object = MibScalar
cabhPsDevWanManClientId = _CabhPsDevWanManClientId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 1, 9),
    _CabhPsDevWanManClientId_Type()
)
cabhPsDevWanManClientId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhPsDevWanManClientId.setStatus("deprecated")


class _CabhPsDevTodSyncStatus_Type(TruthValue):
    """Custom type cabhPsDevTodSyncStatus based on TruthValue"""


_CabhPsDevTodSyncStatus_Object = MibScalar
cabhPsDevTodSyncStatus = _CabhPsDevTodSyncStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 1, 10),
    _CabhPsDevTodSyncStatus_Type()
)
cabhPsDevTodSyncStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhPsDevTodSyncStatus.setStatus("current")


class _CabhPsDevProvMode_Type(Integer32):
    """Custom type cabhPsDevProvMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dhcpmode", 1),
          ("dormantCHmode", 3),
          ("snmpmode", 2))
    )


_CabhPsDevProvMode_Type.__name__ = "Integer32"
_CabhPsDevProvMode_Object = MibScalar
cabhPsDevProvMode = _CabhPsDevProvMode_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 1, 11),
    _CabhPsDevProvMode_Type()
)
cabhPsDevProvMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhPsDevProvMode.setStatus("current")
_CabhPsDevLastSetToFactory_Type = TimeStamp
_CabhPsDevLastSetToFactory_Object = MibScalar
cabhPsDevLastSetToFactory = _CabhPsDevLastSetToFactory_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 1, 12),
    _CabhPsDevLastSetToFactory_Type()
)
cabhPsDevLastSetToFactory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhPsDevLastSetToFactory.setStatus("current")


class _CabhPsDevTrapControl_Type(Bits):
    """Custom type cabhPsDevTrapControl based on Bits"""
    defaultHexValue = "0000"

    namedValues = NamedValues(
        *(("cabhPsDevCapTrap", 12),
          ("cabhPsDevCdpLanIpPoolTrap", 15),
          ("cabhPsDevCdpThresholdTrap", 10),
          ("cabhPsDevCdpWanDataIpTrap", 9),
          ("cabhPsDevCspTrap", 11),
          ("cabhPsDevCtpTrap", 13),
          ("cabhPsDevDHCPFailTrap", 3),
          ("cabhPsDevInitRetryTrap", 2),
          ("cabhPsDevInitTLVUnknownTrap", 0),
          ("cabhPsDevInitTrap", 1),
          ("cabhPsDevProvEnrollTrap", 14),
          ("cabhPsDevSwUpgradeCVCFailTrap", 7),
          ("cabhPsDevSwUpgradeFailTrap", 5),
          ("cabhPsDevSwUpgradeInitTrap", 4),
          ("cabhPsDevSwUpgradeSuccessTrap", 6),
          ("cabhPsDevTODFailTrap", 8),
          ("cabhPsDevUpnpMultiplePHTrap", 16))
    )

_CabhPsDevTrapControl_Type.__name__ = "Bits"
_CabhPsDevTrapControl_Object = MibScalar
cabhPsDevTrapControl = _CabhPsDevTrapControl_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 1, 13),
    _CabhPsDevTrapControl_Type()
)
cabhPsDevTrapControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhPsDevTrapControl.setStatus("current")
_CabhPsDevProv_ObjectIdentity = ObjectIdentity
cabhPsDevProv = _CabhPsDevProv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 2)
)


class _CabhPsDevProvisioningTimer_Type(Integer32):
    """Custom type cabhPsDevProvisioningTimer based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_CabhPsDevProvisioningTimer_Type.__name__ = "Integer32"
_CabhPsDevProvisioningTimer_Object = MibScalar
cabhPsDevProvisioningTimer = _CabhPsDevProvisioningTimer_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 2, 1),
    _CabhPsDevProvisioningTimer_Type()
)
cabhPsDevProvisioningTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhPsDevProvisioningTimer.setStatus("current")
if mibBuilder.loadTexts:
    cabhPsDevProvisioningTimer.setUnits("minutes")


class _CabhPsDevProvConfigFile_Type(SnmpAdminString):
    """Custom type cabhPsDevProvConfigFile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_CabhPsDevProvConfigFile_Type.__name__ = "SnmpAdminString"
_CabhPsDevProvConfigFile_Object = MibScalar
cabhPsDevProvConfigFile = _CabhPsDevProvConfigFile_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 2, 2),
    _CabhPsDevProvConfigFile_Type()
)
cabhPsDevProvConfigFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhPsDevProvConfigFile.setStatus("current")


class _CabhPsDevProvConfigHash_Type(OctetString):
    """Custom type cabhPsDevProvConfigHash based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(20, 20),
    )


_CabhPsDevProvConfigHash_Type.__name__ = "OctetString"
_CabhPsDevProvConfigHash_Object = MibScalar
cabhPsDevProvConfigHash = _CabhPsDevProvConfigHash_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 2, 3),
    _CabhPsDevProvConfigHash_Type()
)
cabhPsDevProvConfigHash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhPsDevProvConfigHash.setStatus("current")
_CabhPsDevProvConfigFileSize_Type = Integer32
_CabhPsDevProvConfigFileSize_Object = MibScalar
cabhPsDevProvConfigFileSize = _CabhPsDevProvConfigFileSize_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 2, 4),
    _CabhPsDevProvConfigFileSize_Type()
)
cabhPsDevProvConfigFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhPsDevProvConfigFileSize.setStatus("current")
if mibBuilder.loadTexts:
    cabhPsDevProvConfigFileSize.setUnits("bytes")


class _CabhPsDevProvConfigFileStatus_Type(Integer32):
    """Custom type cabhPsDevProvConfigFileStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("busy", 2),
          ("idle", 1))
    )


_CabhPsDevProvConfigFileStatus_Type.__name__ = "Integer32"
_CabhPsDevProvConfigFileStatus_Object = MibScalar
cabhPsDevProvConfigFileStatus = _CabhPsDevProvConfigFileStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 2, 5),
    _CabhPsDevProvConfigFileStatus_Type()
)
cabhPsDevProvConfigFileStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhPsDevProvConfigFileStatus.setStatus("current")


class _CabhPsDevProvConfigTLVProcessed_Type(Integer32):
    """Custom type cabhPsDevProvConfigTLVProcessed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_CabhPsDevProvConfigTLVProcessed_Type.__name__ = "Integer32"
_CabhPsDevProvConfigTLVProcessed_Object = MibScalar
cabhPsDevProvConfigTLVProcessed = _CabhPsDevProvConfigTLVProcessed_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 2, 6),
    _CabhPsDevProvConfigTLVProcessed_Type()
)
cabhPsDevProvConfigTLVProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhPsDevProvConfigTLVProcessed.setStatus("current")


class _CabhPsDevProvConfigTLVRejected_Type(Integer32):
    """Custom type cabhPsDevProvConfigTLVRejected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_CabhPsDevProvConfigTLVRejected_Type.__name__ = "Integer32"
_CabhPsDevProvConfigTLVRejected_Object = MibScalar
cabhPsDevProvConfigTLVRejected = _CabhPsDevProvConfigTLVRejected_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 2, 7),
    _CabhPsDevProvConfigTLVRejected_Type()
)
cabhPsDevProvConfigTLVRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhPsDevProvConfigTLVRejected.setStatus("current")


class _CabhPsDevProvSolicitedKeyTimeout_Type(Integer32):
    """Custom type cabhPsDevProvSolicitedKeyTimeout based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 600),
    )


_CabhPsDevProvSolicitedKeyTimeout_Type.__name__ = "Integer32"
_CabhPsDevProvSolicitedKeyTimeout_Object = MibScalar
cabhPsDevProvSolicitedKeyTimeout = _CabhPsDevProvSolicitedKeyTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 2, 8),
    _CabhPsDevProvSolicitedKeyTimeout_Type()
)
cabhPsDevProvSolicitedKeyTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhPsDevProvSolicitedKeyTimeout.setStatus("current")
if mibBuilder.loadTexts:
    cabhPsDevProvSolicitedKeyTimeout.setUnits("seconds")


class _CabhPsDevProvState_Type(Integer32):
    """Custom type cabhPsDevProvState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fail", 3),
          ("inProgress", 2),
          ("pass", 1))
    )


_CabhPsDevProvState_Type.__name__ = "Integer32"
_CabhPsDevProvState_Object = MibScalar
cabhPsDevProvState = _CabhPsDevProvState_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 2, 9),
    _CabhPsDevProvState_Type()
)
cabhPsDevProvState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhPsDevProvState.setStatus("current")


class _CabhPsDevProvAuthState_Type(Integer32):
    """Custom type cabhPsDevProvAuthState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accepted", 1),
          ("rejected", 2))
    )


_CabhPsDevProvAuthState_Type.__name__ = "Integer32"
_CabhPsDevProvAuthState_Object = MibScalar
cabhPsDevProvAuthState = _CabhPsDevProvAuthState_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 2, 10),
    _CabhPsDevProvAuthState_Type()
)
cabhPsDevProvAuthState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhPsDevProvAuthState.setStatus("current")
_CabhPsDevProvCorrelationId_Type = Integer32
_CabhPsDevProvCorrelationId_Object = MibScalar
cabhPsDevProvCorrelationId = _CabhPsDevProvCorrelationId_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 2, 11),
    _CabhPsDevProvCorrelationId_Type()
)
cabhPsDevProvCorrelationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhPsDevProvCorrelationId.setStatus("deprecated")
_CabhPsDevTimeServerAddrType_Type = InetAddressType
_CabhPsDevTimeServerAddrType_Object = MibScalar
cabhPsDevTimeServerAddrType = _CabhPsDevTimeServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 2, 12),
    _CabhPsDevTimeServerAddrType_Type()
)
cabhPsDevTimeServerAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhPsDevTimeServerAddrType.setStatus("current")
_CabhPsDevTimeServerAddr_Type = InetAddress
_CabhPsDevTimeServerAddr_Object = MibScalar
cabhPsDevTimeServerAddr = _CabhPsDevTimeServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 2, 13),
    _CabhPsDevTimeServerAddr_Type()
)
cabhPsDevTimeServerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhPsDevTimeServerAddr.setStatus("current")
_CabhPsDevAttrib_ObjectIdentity = ObjectIdentity
cabhPsDevAttrib = _CabhPsDevAttrib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 3)
)
_CabhPsDevPsAttrib_ObjectIdentity = ObjectIdentity
cabhPsDevPsAttrib = _CabhPsDevPsAttrib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 3, 1)
)


class _CabhPsDevPsDeviceType_Type(SnmpAdminString):
    """Custom type cabhPsDevPsDeviceType based on SnmpAdminString"""
    defaultValue = OctetString("CableHome Residential Gateway")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CabhPsDevPsDeviceType_Type.__name__ = "SnmpAdminString"
_CabhPsDevPsDeviceType_Object = MibScalar
cabhPsDevPsDeviceType = _CabhPsDevPsDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 3, 1, 1),
    _CabhPsDevPsDeviceType_Type()
)
cabhPsDevPsDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhPsDevPsDeviceType.setStatus("current")


class _CabhPsDevPsManufacturerUrl_Type(SnmpAdminString):
    """Custom type cabhPsDevPsManufacturerUrl based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CabhPsDevPsManufacturerUrl_Type.__name__ = "SnmpAdminString"
_CabhPsDevPsManufacturerUrl_Object = MibScalar
cabhPsDevPsManufacturerUrl = _CabhPsDevPsManufacturerUrl_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 3, 1, 3),
    _CabhPsDevPsManufacturerUrl_Type()
)
cabhPsDevPsManufacturerUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhPsDevPsManufacturerUrl.setStatus("current")


class _CabhPsDevPsModelUrl_Type(SnmpAdminString):
    """Custom type cabhPsDevPsModelUrl based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CabhPsDevPsModelUrl_Type.__name__ = "SnmpAdminString"
_CabhPsDevPsModelUrl_Object = MibScalar
cabhPsDevPsModelUrl = _CabhPsDevPsModelUrl_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 3, 1, 7),
    _CabhPsDevPsModelUrl_Type()
)
cabhPsDevPsModelUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhPsDevPsModelUrl.setStatus("current")


class _CabhPsDevPsModelUpc_Type(SnmpAdminString):
    """Custom type cabhPsDevPsModelUpc based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CabhPsDevPsModelUpc_Type.__name__ = "SnmpAdminString"
_CabhPsDevPsModelUpc_Object = MibScalar
cabhPsDevPsModelUpc = _CabhPsDevPsModelUpc_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 3, 1, 8),
    _CabhPsDevPsModelUpc_Type()
)
cabhPsDevPsModelUpc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhPsDevPsModelUpc.setStatus("current")
_CabhPsDevBpAttrib_ObjectIdentity = ObjectIdentity
cabhPsDevBpAttrib = _CabhPsDevBpAttrib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 3, 2)
)
_CabhPsDevBpProfileTable_Object = MibTable
cabhPsDevBpProfileTable = _CabhPsDevBpProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    cabhPsDevBpProfileTable.setStatus("obsolete")
_CabhPsDevBpProfileEntry_Object = MibTableRow
cabhPsDevBpProfileEntry = _CabhPsDevBpProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 3, 2, 1, 1)
)
cabhPsDevBpProfileEntry.setIndexNames(
    (0, "CABH-PS-DEV-MIB", "cabhPsDevBpIndex"),
)
if mibBuilder.loadTexts:
    cabhPsDevBpProfileEntry.setStatus("obsolete")


class _CabhPsDevBpIndex_Type(Integer32):
    """Custom type cabhPsDevBpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CabhPsDevBpIndex_Type.__name__ = "Integer32"
_CabhPsDevBpIndex_Object = MibTableColumn
cabhPsDevBpIndex = _CabhPsDevBpIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 3, 2, 1, 1, 1),
    _CabhPsDevBpIndex_Type()
)
cabhPsDevBpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cabhPsDevBpIndex.setStatus("obsolete")


class _CabhPsDevBpDeviceType_Type(SnmpAdminString):
    """Custom type cabhPsDevBpDeviceType based on SnmpAdminString"""
    defaultValue = OctetString("CableHome Host")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CabhPsDevBpDeviceType_Type.__name__ = "SnmpAdminString"
_CabhPsDevBpDeviceType_Object = MibTableColumn
cabhPsDevBpDeviceType = _CabhPsDevBpDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 3, 2, 1, 1, 2),
    _CabhPsDevBpDeviceType_Type()
)
cabhPsDevBpDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhPsDevBpDeviceType.setStatus("obsolete")


class _CabhPsDevBpManufacturer_Type(SnmpAdminString):
    """Custom type cabhPsDevBpManufacturer based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CabhPsDevBpManufacturer_Type.__name__ = "SnmpAdminString"
_CabhPsDevBpManufacturer_Object = MibTableColumn
cabhPsDevBpManufacturer = _CabhPsDevBpManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 3, 2, 1, 1, 3),
    _CabhPsDevBpManufacturer_Type()
)
cabhPsDevBpManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhPsDevBpManufacturer.setStatus("obsolete")


class _CabhPsDevBpManufacturerUrl_Type(SnmpAdminString):
    """Custom type cabhPsDevBpManufacturerUrl based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CabhPsDevBpManufacturerUrl_Type.__name__ = "SnmpAdminString"
_CabhPsDevBpManufacturerUrl_Object = MibTableColumn
cabhPsDevBpManufacturerUrl = _CabhPsDevBpManufacturerUrl_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 3, 2, 1, 1, 4),
    _CabhPsDevBpManufacturerUrl_Type()
)
cabhPsDevBpManufacturerUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhPsDevBpManufacturerUrl.setStatus("obsolete")


class _CabhPsDevBpSerialNumber_Type(SnmpAdminString):
    """Custom type cabhPsDevBpSerialNumber based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CabhPsDevBpSerialNumber_Type.__name__ = "SnmpAdminString"
_CabhPsDevBpSerialNumber_Object = MibTableColumn
cabhPsDevBpSerialNumber = _CabhPsDevBpSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 3, 2, 1, 1, 5),
    _CabhPsDevBpSerialNumber_Type()
)
cabhPsDevBpSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhPsDevBpSerialNumber.setStatus("obsolete")


class _CabhPsDevBpHardwareVersion_Type(SnmpAdminString):
    """Custom type cabhPsDevBpHardwareVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CabhPsDevBpHardwareVersion_Type.__name__ = "SnmpAdminString"
_CabhPsDevBpHardwareVersion_Object = MibTableColumn
cabhPsDevBpHardwareVersion = _CabhPsDevBpHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 3, 2, 1, 1, 6),
    _CabhPsDevBpHardwareVersion_Type()
)
cabhPsDevBpHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhPsDevBpHardwareVersion.setStatus("obsolete")


class _CabhPsDevBpHardwareOptions_Type(SnmpAdminString):
    """Custom type cabhPsDevBpHardwareOptions based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CabhPsDevBpHardwareOptions_Type.__name__ = "SnmpAdminString"
_CabhPsDevBpHardwareOptions_Object = MibTableColumn
cabhPsDevBpHardwareOptions = _CabhPsDevBpHardwareOptions_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 3, 2, 1, 1, 7),
    _CabhPsDevBpHardwareOptions_Type()
)
cabhPsDevBpHardwareOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhPsDevBpHardwareOptions.setStatus("obsolete")


class _CabhPsDevBpModelName_Type(SnmpAdminString):
    """Custom type cabhPsDevBpModelName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CabhPsDevBpModelName_Type.__name__ = "SnmpAdminString"
_CabhPsDevBpModelName_Object = MibTableColumn
cabhPsDevBpModelName = _CabhPsDevBpModelName_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 3, 2, 1, 1, 8),
    _CabhPsDevBpModelName_Type()
)
cabhPsDevBpModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhPsDevBpModelName.setStatus("obsolete")


class _CabhPsDevBpModelNumber_Type(SnmpAdminString):
    """Custom type cabhPsDevBpModelNumber based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CabhPsDevBpModelNumber_Type.__name__ = "SnmpAdminString"
_CabhPsDevBpModelNumber_Object = MibTableColumn
cabhPsDevBpModelNumber = _CabhPsDevBpModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 3, 2, 1, 1, 9),
    _CabhPsDevBpModelNumber_Type()
)
cabhPsDevBpModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhPsDevBpModelNumber.setStatus("obsolete")


class _CabhPsDevBpModelUrl_Type(SnmpAdminString):
    """Custom type cabhPsDevBpModelUrl based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CabhPsDevBpModelUrl_Type.__name__ = "SnmpAdminString"
_CabhPsDevBpModelUrl_Object = MibTableColumn
cabhPsDevBpModelUrl = _CabhPsDevBpModelUrl_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 3, 2, 1, 1, 10),
    _CabhPsDevBpModelUrl_Type()
)
cabhPsDevBpModelUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhPsDevBpModelUrl.setStatus("obsolete")


class _CabhPsDevBpModelUpc_Type(SnmpAdminString):
    """Custom type cabhPsDevBpModelUpc based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CabhPsDevBpModelUpc_Type.__name__ = "SnmpAdminString"
_CabhPsDevBpModelUpc_Object = MibTableColumn
cabhPsDevBpModelUpc = _CabhPsDevBpModelUpc_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 3, 2, 1, 1, 11),
    _CabhPsDevBpModelUpc_Type()
)
cabhPsDevBpModelUpc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhPsDevBpModelUpc.setStatus("obsolete")


class _CabhPsDevBpModelSoftwareOs_Type(SnmpAdminString):
    """Custom type cabhPsDevBpModelSoftwareOs based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CabhPsDevBpModelSoftwareOs_Type.__name__ = "SnmpAdminString"
_CabhPsDevBpModelSoftwareOs_Object = MibTableColumn
cabhPsDevBpModelSoftwareOs = _CabhPsDevBpModelSoftwareOs_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 3, 2, 1, 1, 12),
    _CabhPsDevBpModelSoftwareOs_Type()
)
cabhPsDevBpModelSoftwareOs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhPsDevBpModelSoftwareOs.setStatus("obsolete")


class _CabhPsDevBpModelSoftwareVersion_Type(SnmpAdminString):
    """Custom type cabhPsDevBpModelSoftwareVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CabhPsDevBpModelSoftwareVersion_Type.__name__ = "SnmpAdminString"
_CabhPsDevBpModelSoftwareVersion_Object = MibTableColumn
cabhPsDevBpModelSoftwareVersion = _CabhPsDevBpModelSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 3, 2, 1, 1, 13),
    _CabhPsDevBpModelSoftwareVersion_Type()
)
cabhPsDevBpModelSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhPsDevBpModelSoftwareVersion.setStatus("obsolete")


class _CabhPsDevBpLanInterfaceType_Type(IANAifType):
    """Custom type cabhPsDevBpLanInterfaceType based on IANAifType"""


_CabhPsDevBpLanInterfaceType_Object = MibTableColumn
cabhPsDevBpLanInterfaceType = _CabhPsDevBpLanInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 3, 2, 1, 1, 14),
    _CabhPsDevBpLanInterfaceType_Type()
)
cabhPsDevBpLanInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhPsDevBpLanInterfaceType.setStatus("obsolete")


class _CabhPsDevBpNumberInterfacePriorities_Type(Integer32):
    """Custom type cabhPsDevBpNumberInterfacePriorities based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_CabhPsDevBpNumberInterfacePriorities_Type.__name__ = "Integer32"
_CabhPsDevBpNumberInterfacePriorities_Object = MibTableColumn
cabhPsDevBpNumberInterfacePriorities = _CabhPsDevBpNumberInterfacePriorities_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 3, 2, 1, 1, 15),
    _CabhPsDevBpNumberInterfacePriorities_Type()
)
cabhPsDevBpNumberInterfacePriorities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhPsDevBpNumberInterfacePriorities.setStatus("obsolete")


class _CabhPsDevBpPhysicalLocation_Type(SnmpAdminString):
    """Custom type cabhPsDevBpPhysicalLocation based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CabhPsDevBpPhysicalLocation_Type.__name__ = "SnmpAdminString"
_CabhPsDevBpPhysicalLocation_Object = MibTableColumn
cabhPsDevBpPhysicalLocation = _CabhPsDevBpPhysicalLocation_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 3, 2, 1, 1, 16),
    _CabhPsDevBpPhysicalLocation_Type()
)
cabhPsDevBpPhysicalLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhPsDevBpPhysicalLocation.setStatus("obsolete")


class _CabhPsDevBpPhysicalAddress_Type(PhysAddress):
    """Custom type cabhPsDevBpPhysicalAddress based on PhysAddress"""
    defaultHexValue = ""

    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_CabhPsDevBpPhysicalAddress_Type.__name__ = "PhysAddress"
_CabhPsDevBpPhysicalAddress_Object = MibTableColumn
cabhPsDevBpPhysicalAddress = _CabhPsDevBpPhysicalAddress_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 3, 2, 1, 1, 17),
    _CabhPsDevBpPhysicalAddress_Type()
)
cabhPsDevBpPhysicalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhPsDevBpPhysicalAddress.setStatus("obsolete")
_CabhPsDevStats_ObjectIdentity = ObjectIdentity
cabhPsDevStats = _CabhPsDevStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 4)
)


class _CabhPsDevLanIpTrafficCountersReset_Type(Integer32):
    """Custom type cabhPsDevLanIpTrafficCountersReset based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clearCounters", 1),
          ("clearTable", 2))
    )


_CabhPsDevLanIpTrafficCountersReset_Type.__name__ = "Integer32"
_CabhPsDevLanIpTrafficCountersReset_Object = MibScalar
cabhPsDevLanIpTrafficCountersReset = _CabhPsDevLanIpTrafficCountersReset_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 4, 1),
    _CabhPsDevLanIpTrafficCountersReset_Type()
)
cabhPsDevLanIpTrafficCountersReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhPsDevLanIpTrafficCountersReset.setStatus("current")
_CabhPsDevLanIpTrafficCountersLastReset_Type = TimeStamp
_CabhPsDevLanIpTrafficCountersLastReset_Object = MibScalar
cabhPsDevLanIpTrafficCountersLastReset = _CabhPsDevLanIpTrafficCountersLastReset_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 4, 2),
    _CabhPsDevLanIpTrafficCountersLastReset_Type()
)
cabhPsDevLanIpTrafficCountersLastReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhPsDevLanIpTrafficCountersLastReset.setStatus("current")


class _CabhPsDevLanIpTrafficEnabled_Type(TruthValue):
    """Custom type cabhPsDevLanIpTrafficEnabled based on TruthValue"""


_CabhPsDevLanIpTrafficEnabled_Object = MibScalar
cabhPsDevLanIpTrafficEnabled = _CabhPsDevLanIpTrafficEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 4, 3),
    _CabhPsDevLanIpTrafficEnabled_Type()
)
cabhPsDevLanIpTrafficEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhPsDevLanIpTrafficEnabled.setStatus("current")
_CabhPsDevLanIpTrafficTable_Object = MibTable
cabhPsDevLanIpTrafficTable = _CabhPsDevLanIpTrafficTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 4, 4)
)
if mibBuilder.loadTexts:
    cabhPsDevLanIpTrafficTable.setStatus("current")
_CabhPsDevLanIpTrafficEntry_Object = MibTableRow
cabhPsDevLanIpTrafficEntry = _CabhPsDevLanIpTrafficEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 4, 4, 1)
)
cabhPsDevLanIpTrafficEntry.setIndexNames(
    (0, "CABH-PS-DEV-MIB", "cabhPsDevLanIpTrafficIndex"),
)
if mibBuilder.loadTexts:
    cabhPsDevLanIpTrafficEntry.setStatus("current")


class _CabhPsDevLanIpTrafficIndex_Type(Integer32):
    """Custom type cabhPsDevLanIpTrafficIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CabhPsDevLanIpTrafficIndex_Type.__name__ = "Integer32"
_CabhPsDevLanIpTrafficIndex_Object = MibTableColumn
cabhPsDevLanIpTrafficIndex = _CabhPsDevLanIpTrafficIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 4, 4, 1, 1),
    _CabhPsDevLanIpTrafficIndex_Type()
)
cabhPsDevLanIpTrafficIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cabhPsDevLanIpTrafficIndex.setStatus("current")


class _CabhPsDevLanIpTrafficInetAddressType_Type(InetAddressType):
    """Custom type cabhPsDevLanIpTrafficInetAddressType based on InetAddressType"""


_CabhPsDevLanIpTrafficInetAddressType_Object = MibTableColumn
cabhPsDevLanIpTrafficInetAddressType = _CabhPsDevLanIpTrafficInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 4, 4, 1, 2),
    _CabhPsDevLanIpTrafficInetAddressType_Type()
)
cabhPsDevLanIpTrafficInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhPsDevLanIpTrafficInetAddressType.setStatus("current")
_CabhPsDevLanIpTrafficInetAddress_Type = InetAddress
_CabhPsDevLanIpTrafficInetAddress_Object = MibTableColumn
cabhPsDevLanIpTrafficInetAddress = _CabhPsDevLanIpTrafficInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 4, 4, 1, 3),
    _CabhPsDevLanIpTrafficInetAddress_Type()
)
cabhPsDevLanIpTrafficInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhPsDevLanIpTrafficInetAddress.setStatus("current")
_CabhPsDevLanIpTrafficInOctets_Type = ZeroBasedCounter32
_CabhPsDevLanIpTrafficInOctets_Object = MibTableColumn
cabhPsDevLanIpTrafficInOctets = _CabhPsDevLanIpTrafficInOctets_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 4, 4, 1, 4),
    _CabhPsDevLanIpTrafficInOctets_Type()
)
cabhPsDevLanIpTrafficInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhPsDevLanIpTrafficInOctets.setStatus("current")
_CabhPsDevLanIpTrafficOutOctets_Type = ZeroBasedCounter32
_CabhPsDevLanIpTrafficOutOctets_Object = MibTableColumn
cabhPsDevLanIpTrafficOutOctets = _CabhPsDevLanIpTrafficOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 4, 4, 1, 5),
    _CabhPsDevLanIpTrafficOutOctets_Type()
)
cabhPsDevLanIpTrafficOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhPsDevLanIpTrafficOutOctets.setStatus("current")
_CabhPsDevAccessControl_ObjectIdentity = ObjectIdentity
cabhPsDevAccessControl = _CabhPsDevAccessControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 5)
)


class _CabhPsDevAccessControlEnable_Type(Bits):
    """Custom type cabhPsDevAccessControlEnable based on Bits"""
    defaultHexValue = "00"

    namedValues = NamedValues(
        *(("homeplug", 3),
          ("hpna", 0),
          ("ieee1394", 5),
          ("ieee80211", 1),
          ("ieee8023", 2),
          ("other", 7),
          ("scsi", 6),
          ("usb", 4))
    )

_CabhPsDevAccessControlEnable_Type.__name__ = "Bits"
_CabhPsDevAccessControlEnable_Object = MibScalar
cabhPsDevAccessControlEnable = _CabhPsDevAccessControlEnable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 5, 1),
    _CabhPsDevAccessControlEnable_Type()
)
cabhPsDevAccessControlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhPsDevAccessControlEnable.setStatus("current")
_CabhPsDevAccessControlTable_Object = MibTable
cabhPsDevAccessControlTable = _CabhPsDevAccessControlTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 5, 2)
)
if mibBuilder.loadTexts:
    cabhPsDevAccessControlTable.setStatus("current")
_CabhPsDevAccessControlEntry_Object = MibTableRow
cabhPsDevAccessControlEntry = _CabhPsDevAccessControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 5, 2, 1)
)
cabhPsDevAccessControlEntry.setIndexNames(
    (0, "CABH-PS-DEV-MIB", "cabhPsDevAccessControlIndex"),
)
if mibBuilder.loadTexts:
    cabhPsDevAccessControlEntry.setStatus("current")


class _CabhPsDevAccessControlIndex_Type(Integer32):
    """Custom type cabhPsDevAccessControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CabhPsDevAccessControlIndex_Type.__name__ = "Integer32"
_CabhPsDevAccessControlIndex_Object = MibTableColumn
cabhPsDevAccessControlIndex = _CabhPsDevAccessControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 5, 2, 1, 1),
    _CabhPsDevAccessControlIndex_Type()
)
cabhPsDevAccessControlIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cabhPsDevAccessControlIndex.setStatus("current")


class _CabhPsDevAccessControlPhysAddr_Type(PhysAddress):
    """Custom type cabhPsDevAccessControlPhysAddr based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CabhPsDevAccessControlPhysAddr_Type.__name__ = "PhysAddress"
_CabhPsDevAccessControlPhysAddr_Object = MibTableColumn
cabhPsDevAccessControlPhysAddr = _CabhPsDevAccessControlPhysAddr_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 5, 2, 1, 2),
    _CabhPsDevAccessControlPhysAddr_Type()
)
cabhPsDevAccessControlPhysAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cabhPsDevAccessControlPhysAddr.setStatus("current")
_CabhPsDevAccessControlRowStatus_Type = RowStatus
_CabhPsDevAccessControlRowStatus_Object = MibTableColumn
cabhPsDevAccessControlRowStatus = _CabhPsDevAccessControlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 5, 2, 1, 3),
    _CabhPsDevAccessControlRowStatus_Type()
)
cabhPsDevAccessControlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cabhPsDevAccessControlRowStatus.setStatus("current")
_CabhPsDevMisc_ObjectIdentity = ObjectIdentity
cabhPsDevMisc = _CabhPsDevMisc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 6)
)
_CabhPsDevUI_ObjectIdentity = ObjectIdentity
cabhPsDevUI = _CabhPsDevUI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 6, 1)
)


class _CabhPsDevUILogin_Type(OctetString):
    """Custom type cabhPsDevUILogin based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CabhPsDevUILogin_Type.__name__ = "OctetString"
_CabhPsDevUILogin_Object = MibScalar
cabhPsDevUILogin = _CabhPsDevUILogin_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 6, 1, 1),
    _CabhPsDevUILogin_Type()
)
cabhPsDevUILogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhPsDevUILogin.setStatus("current")


class _CabhPsDevUIPassword_Type(OctetString):
    """Custom type cabhPsDevUIPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 32),
    )


_CabhPsDevUIPassword_Type.__name__ = "OctetString"
_CabhPsDevUIPassword_Object = MibScalar
cabhPsDevUIPassword = _CabhPsDevUIPassword_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 6, 1, 2),
    _CabhPsDevUIPassword_Type()
)
cabhPsDevUIPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhPsDevUIPassword.setStatus("current")


class _CabhPsDevUISelection_Type(Integer32):
    """Custom type cabhPsDevUISelection based on Integer32"""
    defaultValue = 1

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
        *(("cableOperatorLocal", 2),
          ("cableOperatorServer", 3),
          ("disabledUI", 4),
          ("manufacturerLocal", 1))
    )


_CabhPsDevUISelection_Type.__name__ = "Integer32"
_CabhPsDevUISelection_Object = MibScalar
cabhPsDevUISelection = _CabhPsDevUISelection_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 6, 1, 3),
    _CabhPsDevUISelection_Type()
)
cabhPsDevUISelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhPsDevUISelection.setStatus("current")


class _CabhPsDevUIServerUrl_Type(SnmpAdminString):
    """Custom type cabhPsDevUIServerUrl based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CabhPsDevUIServerUrl_Type.__name__ = "SnmpAdminString"
_CabhPsDevUIServerUrl_Object = MibScalar
cabhPsDevUIServerUrl = _CabhPsDevUIServerUrl_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 6, 1, 4),
    _CabhPsDevUIServerUrl_Type()
)
cabhPsDevUIServerUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhPsDevUIServerUrl.setStatus("current")


class _CabhPsDevUISelectionDisabledBodyText_Type(SnmpAdminString):
    """Custom type cabhPsDevUISelectionDisabledBodyText based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CabhPsDevUISelectionDisabledBodyText_Type.__name__ = "SnmpAdminString"
_CabhPsDevUISelectionDisabledBodyText_Object = MibScalar
cabhPsDevUISelectionDisabledBodyText = _CabhPsDevUISelectionDisabledBodyText_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 6, 1, 5),
    _CabhPsDevUISelectionDisabledBodyText_Type()
)
cabhPsDevUISelectionDisabledBodyText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhPsDevUISelectionDisabledBodyText.setStatus("current")
_CabhPsDev802dot11_ObjectIdentity = ObjectIdentity
cabhPsDev802dot11 = _CabhPsDev802dot11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 6, 2)
)
_CabhPsDev802dot11BaseTable_Object = MibTable
cabhPsDev802dot11BaseTable = _CabhPsDev802dot11BaseTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 6, 2, 1)
)
if mibBuilder.loadTexts:
    cabhPsDev802dot11BaseTable.setStatus("current")
_CabhPsDev802dot11BaseEntry_Object = MibTableRow
cabhPsDev802dot11BaseEntry = _CabhPsDev802dot11BaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 6, 2, 1, 1)
)
cabhPsDev802dot11BaseEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cabhPsDev802dot11BaseEntry.setStatus("current")


class _CabhPsDev802dot11BaseSetToDefault_Type(TruthValue):
    """Custom type cabhPsDev802dot11BaseSetToDefault based on TruthValue"""


_CabhPsDev802dot11BaseSetToDefault_Object = MibTableColumn
cabhPsDev802dot11BaseSetToDefault = _CabhPsDev802dot11BaseSetToDefault_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 6, 2, 1, 1, 1),
    _CabhPsDev802dot11BaseSetToDefault_Type()
)
cabhPsDev802dot11BaseSetToDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhPsDev802dot11BaseSetToDefault.setStatus("current")
_CabhPsDev802dot11BaseLastSetToDefault_Type = TimeStamp
_CabhPsDev802dot11BaseLastSetToDefault_Object = MibTableColumn
cabhPsDev802dot11BaseLastSetToDefault = _CabhPsDev802dot11BaseLastSetToDefault_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 6, 2, 1, 1, 2),
    _CabhPsDev802dot11BaseLastSetToDefault_Type()
)
cabhPsDev802dot11BaseLastSetToDefault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhPsDev802dot11BaseLastSetToDefault.setStatus("current")


class _CabhPsDev802dot11BaseAdvertiseSSID_Type(TruthValue):
    """Custom type cabhPsDev802dot11BaseAdvertiseSSID based on TruthValue"""


_CabhPsDev802dot11BaseAdvertiseSSID_Object = MibTableColumn
cabhPsDev802dot11BaseAdvertiseSSID = _CabhPsDev802dot11BaseAdvertiseSSID_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 6, 2, 1, 1, 3),
    _CabhPsDev802dot11BaseAdvertiseSSID_Type()
)
cabhPsDev802dot11BaseAdvertiseSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhPsDev802dot11BaseAdvertiseSSID.setStatus("current")


class _CabhPsDev802dot11BasePhyCapabilities_Type(Bits):
    """Custom type cabhPsDev802dot11BasePhyCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("ieee80211a", 0),
          ("ieee80211b", 1),
          ("ieee80211g", 2))
    )

_CabhPsDev802dot11BasePhyCapabilities_Type.__name__ = "Bits"
_CabhPsDev802dot11BasePhyCapabilities_Object = MibTableColumn
cabhPsDev802dot11BasePhyCapabilities = _CabhPsDev802dot11BasePhyCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 6, 2, 1, 1, 4),
    _CabhPsDev802dot11BasePhyCapabilities_Type()
)
cabhPsDev802dot11BasePhyCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhPsDev802dot11BasePhyCapabilities.setStatus("current")


class _CabhPsDev802dot11BasePhyOperMode_Type(Integer32):
    """Custom type cabhPsDev802dot11BasePhyOperMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              24)
        )
    )
    namedValues = NamedValues(
        *(("ieee80211a", 1),
          ("ieee80211b", 2),
          ("ieee80211bg", 24),
          ("ieee80211g", 4))
    )


_CabhPsDev802dot11BasePhyOperMode_Type.__name__ = "Integer32"
_CabhPsDev802dot11BasePhyOperMode_Object = MibTableColumn
cabhPsDev802dot11BasePhyOperMode = _CabhPsDev802dot11BasePhyOperMode_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 6, 2, 1, 1, 5),
    _CabhPsDev802dot11BasePhyOperMode_Type()
)
cabhPsDev802dot11BasePhyOperMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhPsDev802dot11BasePhyOperMode.setStatus("current")
_CabhPsDev802dot11SecTable_Object = MibTable
cabhPsDev802dot11SecTable = _CabhPsDev802dot11SecTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 6, 2, 2)
)
if mibBuilder.loadTexts:
    cabhPsDev802dot11SecTable.setStatus("current")
_CabhPsDev802dot11SecEntry_Object = MibTableRow
cabhPsDev802dot11SecEntry = _CabhPsDev802dot11SecEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 6, 2, 2, 1)
)
cabhPsDev802dot11SecEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cabhPsDev802dot11SecEntry.setStatus("current")


class _CabhPsDev802dot11SecCapabilities_Type(Bits):
    """Custom type cabhPsDev802dot11SecCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("wep128", 1),
          ("wep64", 0),
          ("wpaPSK", 2))
    )

_CabhPsDev802dot11SecCapabilities_Type.__name__ = "Bits"
_CabhPsDev802dot11SecCapabilities_Object = MibTableColumn
cabhPsDev802dot11SecCapabilities = _CabhPsDev802dot11SecCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 6, 2, 2, 1, 1),
    _CabhPsDev802dot11SecCapabilities_Type()
)
cabhPsDev802dot11SecCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhPsDev802dot11SecCapabilities.setStatus("current")


class _CabhPsDev802dot11SecOperMode_Type(Bits):
    """Custom type cabhPsDev802dot11SecOperMode based on Bits"""
    namedValues = NamedValues(
        *(("wep128", 1),
          ("wep64", 0),
          ("wpaPSK", 2))
    )

_CabhPsDev802dot11SecOperMode_Type.__name__ = "Bits"
_CabhPsDev802dot11SecOperMode_Object = MibTableColumn
cabhPsDev802dot11SecOperMode = _CabhPsDev802dot11SecOperMode_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 6, 2, 2, 1, 2),
    _CabhPsDev802dot11SecOperMode_Type()
)
cabhPsDev802dot11SecOperMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhPsDev802dot11SecOperMode.setStatus("current")


class _CabhPsDev802dot11SecPassPhraseToWEPKey_Type(OctetString):
    """Custom type cabhPsDev802dot11SecPassPhraseToWEPKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(5, 63),
    )


_CabhPsDev802dot11SecPassPhraseToWEPKey_Type.__name__ = "OctetString"
_CabhPsDev802dot11SecPassPhraseToWEPKey_Object = MibTableColumn
cabhPsDev802dot11SecPassPhraseToWEPKey = _CabhPsDev802dot11SecPassPhraseToWEPKey_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 6, 2, 2, 1, 3),
    _CabhPsDev802dot11SecPassPhraseToWEPKey_Type()
)
cabhPsDev802dot11SecPassPhraseToWEPKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhPsDev802dot11SecPassPhraseToWEPKey.setStatus("current")


class _CabhPsDev802dot11SecUsePassPhraseToWEPKeyAlg_Type(TruthValue):
    """Custom type cabhPsDev802dot11SecUsePassPhraseToWEPKeyAlg based on TruthValue"""


_CabhPsDev802dot11SecUsePassPhraseToWEPKeyAlg_Object = MibTableColumn
cabhPsDev802dot11SecUsePassPhraseToWEPKeyAlg = _CabhPsDev802dot11SecUsePassPhraseToWEPKeyAlg_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 6, 2, 2, 1, 4),
    _CabhPsDev802dot11SecUsePassPhraseToWEPKeyAlg_Type()
)
cabhPsDev802dot11SecUsePassPhraseToWEPKeyAlg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhPsDev802dot11SecUsePassPhraseToWEPKeyAlg.setStatus("current")


class _CabhPsDev802dot11SecPSKPassPhraseToKey_Type(OctetString):
    """Custom type cabhPsDev802dot11SecPSKPassPhraseToKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 63),
    )


_CabhPsDev802dot11SecPSKPassPhraseToKey_Type.__name__ = "OctetString"
_CabhPsDev802dot11SecPSKPassPhraseToKey_Object = MibTableColumn
cabhPsDev802dot11SecPSKPassPhraseToKey = _CabhPsDev802dot11SecPSKPassPhraseToKey_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 6, 2, 2, 1, 5),
    _CabhPsDev802dot11SecPSKPassPhraseToKey_Type()
)
cabhPsDev802dot11SecPSKPassPhraseToKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhPsDev802dot11SecPSKPassPhraseToKey.setStatus("current")


class _CabhPsDev802dot11SecWPAPreSharedKey_Type(OctetString):
    """Custom type cabhPsDev802dot11SecWPAPreSharedKey based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(32, 32),
    )


_CabhPsDev802dot11SecWPAPreSharedKey_Type.__name__ = "OctetString"
_CabhPsDev802dot11SecWPAPreSharedKey_Object = MibTableColumn
cabhPsDev802dot11SecWPAPreSharedKey = _CabhPsDev802dot11SecWPAPreSharedKey_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 6, 2, 2, 1, 6),
    _CabhPsDev802dot11SecWPAPreSharedKey_Type()
)
cabhPsDev802dot11SecWPAPreSharedKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhPsDev802dot11SecWPAPreSharedKey.setStatus("current")


class _CabhPsDev802dot11SecWPARekeyTime_Type(Unsigned32):
    """Custom type cabhPsDev802dot11SecWPARekeyTime based on Unsigned32"""
    defaultValue = 86400

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CabhPsDev802dot11SecWPARekeyTime_Type.__name__ = "Unsigned32"
_CabhPsDev802dot11SecWPARekeyTime_Object = MibTableColumn
cabhPsDev802dot11SecWPARekeyTime = _CabhPsDev802dot11SecWPARekeyTime_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 6, 2, 2, 1, 7),
    _CabhPsDev802dot11SecWPARekeyTime_Type()
)
cabhPsDev802dot11SecWPARekeyTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhPsDev802dot11SecWPARekeyTime.setStatus("current")
if mibBuilder.loadTexts:
    cabhPsDev802dot11SecWPARekeyTime.setUnits("seconds")


class _CabhPsDev802dot11SecControl_Type(Integer32):
    """Custom type cabhPsDev802dot11SecControl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("commitConfig", 2),
          ("restoreConfig", 1))
    )


_CabhPsDev802dot11SecControl_Type.__name__ = "Integer32"
_CabhPsDev802dot11SecControl_Object = MibTableColumn
cabhPsDev802dot11SecControl = _CabhPsDev802dot11SecControl_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 6, 2, 2, 1, 8),
    _CabhPsDev802dot11SecControl_Type()
)
cabhPsDev802dot11SecControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhPsDev802dot11SecControl.setStatus("current")


class _CabhPsDev802dot11SecCommitStatus_Type(Integer32):
    """Custom type cabhPsDev802dot11SecCommitStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("commitFailed", 3),
          ("commitNeeded", 2),
          ("commitSucceeded", 1))
    )


_CabhPsDev802dot11SecCommitStatus_Type.__name__ = "Integer32"
_CabhPsDev802dot11SecCommitStatus_Object = MibTableColumn
cabhPsDev802dot11SecCommitStatus = _CabhPsDev802dot11SecCommitStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 6, 2, 2, 1, 9),
    _CabhPsDev802dot11SecCommitStatus_Type()
)
cabhPsDev802dot11SecCommitStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhPsDev802dot11SecCommitStatus.setStatus("current")
_CabhPsDevUpnp_ObjectIdentity = ObjectIdentity
cabhPsDevUpnp = _CabhPsDevUpnp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 6, 3)
)
_CabhPsDevUpnpBase_ObjectIdentity = ObjectIdentity
cabhPsDevUpnpBase = _CabhPsDevUpnpBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 6, 3, 1)
)


class _CabhPsDevUpnpEnabled_Type(TruthValue):
    """Custom type cabhPsDevUpnpEnabled based on TruthValue"""


_CabhPsDevUpnpEnabled_Object = MibScalar
cabhPsDevUpnpEnabled = _CabhPsDevUpnpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 6, 3, 1, 1),
    _CabhPsDevUpnpEnabled_Type()
)
cabhPsDevUpnpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhPsDevUpnpEnabled.setStatus("current")
_CabhPsDevUpnpCommands_ObjectIdentity = ObjectIdentity
cabhPsDevUpnpCommands = _CabhPsDevUpnpCommands_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 6, 3, 2)
)


class _CabhPsDevUpnpCommandIpType_Type(InetAddressType):
    """Custom type cabhPsDevUpnpCommandIpType based on InetAddressType"""


_CabhPsDevUpnpCommandIpType_Object = MibScalar
cabhPsDevUpnpCommandIpType = _CabhPsDevUpnpCommandIpType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 6, 3, 2, 1),
    _CabhPsDevUpnpCommandIpType_Type()
)
cabhPsDevUpnpCommandIpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhPsDevUpnpCommandIpType.setStatus("current")


class _CabhPsDevUpnpCommandIp_Type(InetAddress):
    """Custom type cabhPsDevUpnpCommandIp based on InetAddress"""
    defaultHexValue = "C0A80001"


_CabhPsDevUpnpCommandIp_Object = MibScalar
cabhPsDevUpnpCommandIp = _CabhPsDevUpnpCommandIp_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 6, 3, 2, 2),
    _CabhPsDevUpnpCommandIp_Type()
)
cabhPsDevUpnpCommandIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhPsDevUpnpCommandIp.setStatus("current")


class _CabhPsDevUpnpCommand_Type(Integer32):
    """Custom type cabhPsDevUpnpCommand based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("discoveryInfo", 1),
          ("qosDeviceCapabilities", 2),
          ("qosDeviceState", 3))
    )


_CabhPsDevUpnpCommand_Type.__name__ = "Integer32"
_CabhPsDevUpnpCommand_Object = MibScalar
cabhPsDevUpnpCommand = _CabhPsDevUpnpCommand_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 6, 3, 2, 3),
    _CabhPsDevUpnpCommand_Type()
)
cabhPsDevUpnpCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhPsDevUpnpCommand.setStatus("current")
_CabhPsDevUpnpCommandUpdate_Type = TruthValue
_CabhPsDevUpnpCommandUpdate_Object = MibScalar
cabhPsDevUpnpCommandUpdate = _CabhPsDevUpnpCommandUpdate_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 6, 3, 2, 4),
    _CabhPsDevUpnpCommandUpdate_Type()
)
cabhPsDevUpnpCommandUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cabhPsDevUpnpCommandUpdate.setStatus("current")
_CabhPsDevUpnpLastCommandUpdate_Type = TimeTicks
_CabhPsDevUpnpLastCommandUpdate_Object = MibScalar
cabhPsDevUpnpLastCommandUpdate = _CabhPsDevUpnpLastCommandUpdate_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 6, 3, 2, 5),
    _CabhPsDevUpnpLastCommandUpdate_Type()
)
cabhPsDevUpnpLastCommandUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhPsDevUpnpLastCommandUpdate.setStatus("current")


class _CabhPsDevUpnpCommandStatus_Type(Integer32):
    """Custom type cabhPsDevUpnpCommandStatus based on Integer32"""
    defaultValue = 1

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
        *(("complete", 3),
          ("failed", 4),
          ("inProgress", 2),
          ("none", 1))
    )


_CabhPsDevUpnpCommandStatus_Type.__name__ = "Integer32"
_CabhPsDevUpnpCommandStatus_Object = MibScalar
cabhPsDevUpnpCommandStatus = _CabhPsDevUpnpCommandStatus_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 6, 3, 2, 6),
    _CabhPsDevUpnpCommandStatus_Type()
)
cabhPsDevUpnpCommandStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhPsDevUpnpCommandStatus.setStatus("current")
_CabhPsDevUpnpInfoTable_Object = MibTable
cabhPsDevUpnpInfoTable = _CabhPsDevUpnpInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 6, 3, 2, 7)
)
if mibBuilder.loadTexts:
    cabhPsDevUpnpInfoTable.setStatus("current")
_CabhPsDevUpnpInfoEntry_Object = MibTableRow
cabhPsDevUpnpInfoEntry = _CabhPsDevUpnpInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 6, 3, 2, 7, 1)
)
cabhPsDevUpnpInfoEntry.setIndexNames(
    (0, "CABH-PS-DEV-MIB", "cabhPsDevUpnpInfoIpType"),
    (0, "CABH-PS-DEV-MIB", "cabhPsDevUpnpInfoIp"),
    (0, "CABH-PS-DEV-MIB", "cabhPsDevUpnpInfoXmlFragmentIndex"),
)
if mibBuilder.loadTexts:
    cabhPsDevUpnpInfoEntry.setStatus("current")
_CabhPsDevUpnpInfoIpType_Type = InetAddressType
_CabhPsDevUpnpInfoIpType_Object = MibTableColumn
cabhPsDevUpnpInfoIpType = _CabhPsDevUpnpInfoIpType_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 6, 3, 2, 7, 1, 1),
    _CabhPsDevUpnpInfoIpType_Type()
)
cabhPsDevUpnpInfoIpType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cabhPsDevUpnpInfoIpType.setStatus("current")
_CabhPsDevUpnpInfoIp_Type = InetAddress
_CabhPsDevUpnpInfoIp_Object = MibTableColumn
cabhPsDevUpnpInfoIp = _CabhPsDevUpnpInfoIp_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 6, 3, 2, 7, 1, 2),
    _CabhPsDevUpnpInfoIp_Type()
)
cabhPsDevUpnpInfoIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cabhPsDevUpnpInfoIp.setStatus("current")


class _CabhPsDevUpnpInfoXmlFragmentIndex_Type(Unsigned32):
    """Custom type cabhPsDevUpnpInfoXmlFragmentIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CabhPsDevUpnpInfoXmlFragmentIndex_Type.__name__ = "Unsigned32"
_CabhPsDevUpnpInfoXmlFragmentIndex_Object = MibTableColumn
cabhPsDevUpnpInfoXmlFragmentIndex = _CabhPsDevUpnpInfoXmlFragmentIndex_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 6, 3, 2, 7, 1, 3),
    _CabhPsDevUpnpInfoXmlFragmentIndex_Type()
)
cabhPsDevUpnpInfoXmlFragmentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cabhPsDevUpnpInfoXmlFragmentIndex.setStatus("current")


class _CabhPsDevUpnpInfoXmlFragment_Type(OctetString):
    """Custom type cabhPsDevUpnpInfoXmlFragment based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 400),
    )


_CabhPsDevUpnpInfoXmlFragment_Type.__name__ = "OctetString"
_CabhPsDevUpnpInfoXmlFragment_Object = MibTableColumn
cabhPsDevUpnpInfoXmlFragment = _CabhPsDevUpnpInfoXmlFragment_Object(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 1, 6, 3, 2, 7, 1, 4),
    _CabhPsDevUpnpInfoXmlFragment_Type()
)
cabhPsDevUpnpInfoXmlFragment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cabhPsDevUpnpInfoXmlFragment.setStatus("current")
_CabhPsNotification_ObjectIdentity = ObjectIdentity
cabhPsNotification = _CabhPsNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 2)
)
_CabhPsDevNotifications_ObjectIdentity = ObjectIdentity
cabhPsDevNotifications = _CabhPsDevNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 2, 0)
)
_CabhPsConformance_ObjectIdentity = ObjectIdentity
cabhPsConformance = _CabhPsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 3)
)
_CabhPsCompliances_ObjectIdentity = ObjectIdentity
cabhPsCompliances = _CabhPsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 3, 1)
)
_CabhPsGroups_ObjectIdentity = ObjectIdentity
cabhPsGroups = _CabhPsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 3, 2)
)

# Managed Objects groups

cabhPsDevBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 3, 2, 1)
)
cabhPsDevBaseGroup.setObjects(
      *(("CABH-PS-DEV-MIB", "cabhPsDevDateTime"),
        ("CABH-PS-DEV-MIB", "cabhPsDevResetNow"),
        ("CABH-PS-DEV-MIB", "cabhPsDevSerialNumber"),
        ("CABH-PS-DEV-MIB", "cabhPsDevHardwareVersion"),
        ("CABH-PS-DEV-MIB", "cabhPsDevWanManMacAddress"),
        ("CABH-PS-DEV-MIB", "cabhPsDevWanDataMacAddress"),
        ("CABH-PS-DEV-MIB", "cabhPsDevTypeIdentifier"),
        ("CABH-PS-DEV-MIB", "cabhPsDevSetToFactory"),
        ("CABH-PS-DEV-MIB", "cabhPsDevTodSyncStatus"),
        ("CABH-PS-DEV-MIB", "cabhPsDevProvMode"),
        ("CABH-PS-DEV-MIB", "cabhPsDevLastSetToFactory"),
        ("CABH-PS-DEV-MIB", "cabhPsDevTrapControl"))
)
if mibBuilder.loadTexts:
    cabhPsDevBaseGroup.setStatus("current")

cabhPsDevProvGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 3, 2, 2)
)
cabhPsDevProvGroup.setObjects(
      *(("CABH-PS-DEV-MIB", "cabhPsDevProvisioningTimer"),
        ("CABH-PS-DEV-MIB", "cabhPsDevProvConfigFile"),
        ("CABH-PS-DEV-MIB", "cabhPsDevProvConfigHash"),
        ("CABH-PS-DEV-MIB", "cabhPsDevProvConfigFileSize"),
        ("CABH-PS-DEV-MIB", "cabhPsDevProvConfigFileStatus"),
        ("CABH-PS-DEV-MIB", "cabhPsDevProvConfigTLVProcessed"),
        ("CABH-PS-DEV-MIB", "cabhPsDevProvConfigTLVRejected"),
        ("CABH-PS-DEV-MIB", "cabhPsDevProvSolicitedKeyTimeout"),
        ("CABH-PS-DEV-MIB", "cabhPsDevProvState"),
        ("CABH-PS-DEV-MIB", "cabhPsDevProvAuthState"),
        ("CABH-PS-DEV-MIB", "cabhPsDevTimeServerAddrType"),
        ("CABH-PS-DEV-MIB", "cabhPsDevTimeServerAddr"))
)
if mibBuilder.loadTexts:
    cabhPsDevProvGroup.setStatus("current")

cabhPsDevAttribGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 3, 2, 3)
)
cabhPsDevAttribGroup.setObjects(
      *(("CABH-PS-DEV-MIB", "cabhPsDevPsDeviceType"),
        ("CABH-PS-DEV-MIB", "cabhPsDevPsManufacturerUrl"),
        ("CABH-PS-DEV-MIB", "cabhPsDevPsModelUrl"),
        ("CABH-PS-DEV-MIB", "cabhPsDevPsModelUpc"))
)
if mibBuilder.loadTexts:
    cabhPsDevAttribGroup.setStatus("current")

cabhPsDevStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 3, 2, 4)
)
cabhPsDevStatsGroup.setObjects(
      *(("CABH-PS-DEV-MIB", "cabhPsDevLanIpTrafficCountersReset"),
        ("CABH-PS-DEV-MIB", "cabhPsDevLanIpTrafficCountersLastReset"),
        ("CABH-PS-DEV-MIB", "cabhPsDevLanIpTrafficEnabled"),
        ("CABH-PS-DEV-MIB", "cabhPsDevLanIpTrafficInetAddressType"),
        ("CABH-PS-DEV-MIB", "cabhPsDevLanIpTrafficInetAddress"),
        ("CABH-PS-DEV-MIB", "cabhPsDevLanIpTrafficInOctets"),
        ("CABH-PS-DEV-MIB", "cabhPsDevLanIpTrafficOutOctets"))
)
if mibBuilder.loadTexts:
    cabhPsDevStatsGroup.setStatus("current")

cabhPsDevDeprecatedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 3, 2, 5)
)
cabhPsDevDeprecatedGroup.setObjects(
      *(("CABH-PS-DEV-MIB", "cabhPsDevWanManClientId"),
        ("CABH-PS-DEV-MIB", "cabhPsDevProvCorrelationId"))
)
if mibBuilder.loadTexts:
    cabhPsDevDeprecatedGroup.setStatus("deprecated")

cabhPsDevAccessControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 3, 2, 7)
)
cabhPsDevAccessControlGroup.setObjects(
      *(("CABH-PS-DEV-MIB", "cabhPsDevAccessControlEnable"),
        ("CABH-PS-DEV-MIB", "cabhPsDevAccessControlPhysAddr"),
        ("CABH-PS-DEV-MIB", "cabhPsDevAccessControlRowStatus"))
)
if mibBuilder.loadTexts:
    cabhPsDevAccessControlGroup.setStatus("current")

cabhPsDevUIGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 3, 2, 8)
)
cabhPsDevUIGroup.setObjects(
      *(("CABH-PS-DEV-MIB", "cabhPsDevUILogin"),
        ("CABH-PS-DEV-MIB", "cabhPsDevUIPassword"),
        ("CABH-PS-DEV-MIB", "cabhPsDevUISelection"),
        ("CABH-PS-DEV-MIB", "cabhPsDevUIServerUrl"),
        ("CABH-PS-DEV-MIB", "cabhPsDevUISelectionDisabledBodyText"))
)
if mibBuilder.loadTexts:
    cabhPsDevUIGroup.setStatus("current")

cabhPsDev802dot11Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 3, 2, 9)
)
cabhPsDev802dot11Group.setObjects(
      *(("CABH-PS-DEV-MIB", "cabhPsDev802dot11BaseSetToDefault"),
        ("CABH-PS-DEV-MIB", "cabhPsDev802dot11BaseLastSetToDefault"),
        ("CABH-PS-DEV-MIB", "cabhPsDev802dot11BaseAdvertiseSSID"),
        ("CABH-PS-DEV-MIB", "cabhPsDev802dot11BasePhyCapabilities"),
        ("CABH-PS-DEV-MIB", "cabhPsDev802dot11BasePhyOperMode"),
        ("CABH-PS-DEV-MIB", "cabhPsDev802dot11SecCapabilities"),
        ("CABH-PS-DEV-MIB", "cabhPsDev802dot11SecOperMode"),
        ("CABH-PS-DEV-MIB", "cabhPsDev802dot11SecPassPhraseToWEPKey"),
        ("CABH-PS-DEV-MIB", "cabhPsDev802dot11SecUsePassPhraseToWEPKeyAlg"),
        ("CABH-PS-DEV-MIB", "cabhPsDev802dot11SecPSKPassPhraseToKey"),
        ("CABH-PS-DEV-MIB", "cabhPsDev802dot11SecWPAPreSharedKey"),
        ("CABH-PS-DEV-MIB", "cabhPsDev802dot11SecWPARekeyTime"),
        ("CABH-PS-DEV-MIB", "cabhPsDev802dot11SecControl"),
        ("CABH-PS-DEV-MIB", "cabhPsDev802dot11SecCommitStatus"))
)
if mibBuilder.loadTexts:
    cabhPsDev802dot11Group.setStatus("current")

cabhPsDevUpnpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 3, 2, 10)
)
cabhPsDevUpnpGroup.setObjects(
      *(("CABH-PS-DEV-MIB", "cabhPsDevUpnpEnabled"),
        ("CABH-PS-DEV-MIB", "cabhPsDevUpnpCommandIpType"),
        ("CABH-PS-DEV-MIB", "cabhPsDevUpnpCommandIp"),
        ("CABH-PS-DEV-MIB", "cabhPsDevUpnpCommand"),
        ("CABH-PS-DEV-MIB", "cabhPsDevUpnpCommandUpdate"),
        ("CABH-PS-DEV-MIB", "cabhPsDevUpnpLastCommandUpdate"),
        ("CABH-PS-DEV-MIB", "cabhPsDevUpnpCommandStatus"),
        ("CABH-PS-DEV-MIB", "cabhPsDevUpnpInfoXmlFragment"))
)
if mibBuilder.loadTexts:
    cabhPsDevUpnpGroup.setStatus("current")

cabhPsDevObsoleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 3, 2, 11)
)
cabhPsDevObsoleteGroup.setObjects(
      *(("CABH-PS-DEV-MIB", "cabhPsDevBpDeviceType"),
        ("CABH-PS-DEV-MIB", "cabhPsDevBpManufacturer"),
        ("CABH-PS-DEV-MIB", "cabhPsDevBpManufacturerUrl"),
        ("CABH-PS-DEV-MIB", "cabhPsDevBpSerialNumber"),
        ("CABH-PS-DEV-MIB", "cabhPsDevBpHardwareVersion"),
        ("CABH-PS-DEV-MIB", "cabhPsDevBpHardwareOptions"),
        ("CABH-PS-DEV-MIB", "cabhPsDevBpModelName"),
        ("CABH-PS-DEV-MIB", "cabhPsDevBpModelNumber"),
        ("CABH-PS-DEV-MIB", "cabhPsDevBpModelUrl"),
        ("CABH-PS-DEV-MIB", "cabhPsDevBpModelUpc"),
        ("CABH-PS-DEV-MIB", "cabhPsDevBpModelSoftwareOs"),
        ("CABH-PS-DEV-MIB", "cabhPsDevBpModelSoftwareVersion"),
        ("CABH-PS-DEV-MIB", "cabhPsDevBpLanInterfaceType"),
        ("CABH-PS-DEV-MIB", "cabhPsDevBpNumberInterfacePriorities"),
        ("CABH-PS-DEV-MIB", "cabhPsDevBpPhysicalLocation"),
        ("CABH-PS-DEV-MIB", "cabhPsDevBpPhysicalAddress"))
)
if mibBuilder.loadTexts:
    cabhPsDevObsoleteGroup.setStatus("obsolete")


# Notification objects

cabhPsDevInitTLVUnknownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 2, 0, 1)
)
cabhPsDevInitTLVUnknownTrap.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("CABH-PS-DEV-MIB", "cabhPsDevWanManMacAddress"))
)
if mibBuilder.loadTexts:
    cabhPsDevInitTLVUnknownTrap.setStatus(
        "current"
    )

cabhPsDevInitTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 2, 0, 2)
)
cabhPsDevInitTrap.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("CABH-PS-DEV-MIB", "cabhPsDevWanManMacAddress"),
        ("CABH-PS-DEV-MIB", "cabhPsDevProvConfigFile"),
        ("CABH-PS-DEV-MIB", "cabhPsDevProvConfigTLVProcessed"),
        ("CABH-PS-DEV-MIB", "cabhPsDevProvConfigTLVRejected"))
)
if mibBuilder.loadTexts:
    cabhPsDevInitTrap.setStatus(
        "current"
    )

cabhPsDevInitRetryTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 2, 0, 3)
)
cabhPsDevInitRetryTrap.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("CABH-PS-DEV-MIB", "cabhPsDevWanManMacAddress"))
)
if mibBuilder.loadTexts:
    cabhPsDevInitRetryTrap.setStatus(
        "current"
    )

cabhPsDevDHCPFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 2, 0, 4)
)
cabhPsDevDHCPFailTrap.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("CABH-PS-DEV-MIB", "cabhPsDevWanManMacAddress"),
        ("CABH-CDP-MIB", "cabhCdpServerDhcpAddress"))
)
if mibBuilder.loadTexts:
    cabhPsDevDHCPFailTrap.setStatus(
        "current"
    )

cabhPsDevSwUpgradeInitTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 2, 0, 5)
)
cabhPsDevSwUpgradeInitTrap.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("CABH-PS-DEV-MIB", "cabhPsDevWanManMacAddress"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevSwFilename"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevSwServer"))
)
if mibBuilder.loadTexts:
    cabhPsDevSwUpgradeInitTrap.setStatus(
        "current"
    )

cabhPsDevSwUpgradeFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 2, 0, 6)
)
cabhPsDevSwUpgradeFailTrap.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("CABH-PS-DEV-MIB", "cabhPsDevWanManMacAddress"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevSwFilename"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevSwServer"))
)
if mibBuilder.loadTexts:
    cabhPsDevSwUpgradeFailTrap.setStatus(
        "current"
    )

cabhPsDevSwUpgradeSuccessTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 2, 0, 7)
)
cabhPsDevSwUpgradeSuccessTrap.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("CABH-PS-DEV-MIB", "cabhPsDevWanManMacAddress"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevSwFilename"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevSwServer"))
)
if mibBuilder.loadTexts:
    cabhPsDevSwUpgradeSuccessTrap.setStatus(
        "current"
    )

cabhPsDevSwUpgradeCVCFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 2, 0, 8)
)
cabhPsDevSwUpgradeCVCFailTrap.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("CABH-PS-DEV-MIB", "cabhPsDevWanManMacAddress"))
)
if mibBuilder.loadTexts:
    cabhPsDevSwUpgradeCVCFailTrap.setStatus(
        "current"
    )

cabhPsDevTODFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 2, 0, 9)
)
cabhPsDevTODFailTrap.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("CABH-PS-DEV-MIB", "cabhPsDevTimeServerAddr"),
        ("CABH-PS-DEV-MIB", "cabhPsDevWanManMacAddress"))
)
if mibBuilder.loadTexts:
    cabhPsDevTODFailTrap.setStatus(
        "current"
    )

cabhPsDevCdpWanDataIpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 2, 0, 10)
)
cabhPsDevCdpWanDataIpTrap.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("CABH-CDP-MIB", "cabhCdpWanDataAddrClientId"),
        ("CABH-PS-DEV-MIB", "cabhPsDevWanManMacAddress"))
)
if mibBuilder.loadTexts:
    cabhPsDevCdpWanDataIpTrap.setStatus(
        "current"
    )

cabhPsDevCdpThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 2, 0, 11)
)
cabhPsDevCdpThresholdTrap.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("CABH-PS-DEV-MIB", "cabhPsDevWanManMacAddress"),
        ("CABH-CDP-MIB", "cabhCdpLanTransThreshold"))
)
if mibBuilder.loadTexts:
    cabhPsDevCdpThresholdTrap.setStatus(
        "current"
    )

cabhPsDevCspTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 2, 0, 12)
)
cabhPsDevCspTrap.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("CABH-PS-DEV-MIB", "cabhPsDevWanManMacAddress"))
)
if mibBuilder.loadTexts:
    cabhPsDevCspTrap.setStatus(
        "current"
    )

cabhPsDevCapTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 2, 0, 13)
)
cabhPsDevCapTrap.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("CABH-PS-DEV-MIB", "cabhPsDevWanManMacAddress"))
)
if mibBuilder.loadTexts:
    cabhPsDevCapTrap.setStatus(
        "current"
    )

cabhPsDevCtpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 2, 0, 14)
)
cabhPsDevCtpTrap.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("CABH-PS-DEV-MIB", "cabhPsDevWanManMacAddress"))
)
if mibBuilder.loadTexts:
    cabhPsDevCtpTrap.setStatus(
        "current"
    )

cabhPsDevProvEnrollTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 2, 0, 15)
)
cabhPsDevProvEnrollTrap.setObjects(
      *(("CABH-PS-DEV-MIB", "cabhPsDevHardwareVersion"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevSwCurrentVers"),
        ("CABH-PS-DEV-MIB", "cabhPsDevTypeIdentifier"),
        ("CABH-PS-DEV-MIB", "cabhPsDevWanManMacAddress"))
)
if mibBuilder.loadTexts:
    cabhPsDevProvEnrollTrap.setStatus(
        "current"
    )

cabhPsDevCdpLanIpPoolTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 2, 0, 16)
)
cabhPsDevCdpLanIpPoolTrap.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("CABH-PS-DEV-MIB", "cabhPsDevWanManMacAddress"),
        ("CABH-CDP-MIB", "cabhCdpLanTransCurCount"))
)
if mibBuilder.loadTexts:
    cabhPsDevCdpLanIpPoolTrap.setStatus(
        "current"
    )

cabhPsDevUpnpMultiplePHTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 2, 0, 17)
)
cabhPsDevUpnpMultiplePHTrap.setObjects(
      *(("DOCS-CABLE-DEVICE-MIB", "docsDevEvLevel"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvId"),
        ("DOCS-CABLE-DEVICE-MIB", "docsDevEvText"),
        ("CABH-QOS2-MIB", "cabhQos2NumActivePolicyHolder"),
        ("CABH-QOS2-MIB", "cabhQos2PolicyHolderEnabled"),
        ("CABH-QOS2-MIB", "cabhQos2PolicyAdmissionControl"))
)
if mibBuilder.loadTexts:
    cabhPsDevUpnpMultiplePHTrap.setStatus(
        "current"
    )


# Notifications groups

cabhPsNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 3, 2, 6)
)
cabhPsNotificationGroup.setObjects(
      *(("CABH-PS-DEV-MIB", "cabhPsDevInitTLVUnknownTrap"),
        ("CABH-PS-DEV-MIB", "cabhPsDevInitTrap"),
        ("CABH-PS-DEV-MIB", "cabhPsDevInitRetryTrap"),
        ("CABH-PS-DEV-MIB", "cabhPsDevDHCPFailTrap"),
        ("CABH-PS-DEV-MIB", "cabhPsDevSwUpgradeInitTrap"),
        ("CABH-PS-DEV-MIB", "cabhPsDevSwUpgradeFailTrap"),
        ("CABH-PS-DEV-MIB", "cabhPsDevSwUpgradeSuccessTrap"),
        ("CABH-PS-DEV-MIB", "cabhPsDevSwUpgradeCVCFailTrap"),
        ("CABH-PS-DEV-MIB", "cabhPsDevTODFailTrap"),
        ("CABH-PS-DEV-MIB", "cabhPsDevCdpWanDataIpTrap"),
        ("CABH-PS-DEV-MIB", "cabhPsDevCdpThresholdTrap"),
        ("CABH-PS-DEV-MIB", "cabhPsDevCspTrap"),
        ("CABH-PS-DEV-MIB", "cabhPsDevCapTrap"),
        ("CABH-PS-DEV-MIB", "cabhPsDevCtpTrap"),
        ("CABH-PS-DEV-MIB", "cabhPsDevProvEnrollTrap"),
        ("CABH-PS-DEV-MIB", "cabhPsDevCdpLanIpPoolTrap"),
        ("CABH-PS-DEV-MIB", "cabhPsDevUpnpMultiplePHTrap"))
)
if mibBuilder.loadTexts:
    cabhPsNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cabhPsBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cabhPsBasicCompliance.setStatus(
        "current"
    )

cabhPsDeprecatedCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    cabhPsDeprecatedCompliance.setStatus(
        "deprecated"
    )

cabhPsObsoleteCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4491, 2, 4, 1, 3, 1, 3)
)
if mibBuilder.loadTexts:
    cabhPsObsoleteCompliance.setStatus(
        "obsolete"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CABH-PS-DEV-MIB",
    **{"cabhPsDevMib": cabhPsDevMib,
       "cabhPsDevMibObjects": cabhPsDevMibObjects,
       "cabhPsDevBase": cabhPsDevBase,
       "cabhPsDevDateTime": cabhPsDevDateTime,
       "cabhPsDevResetNow": cabhPsDevResetNow,
       "cabhPsDevSerialNumber": cabhPsDevSerialNumber,
       "cabhPsDevHardwareVersion": cabhPsDevHardwareVersion,
       "cabhPsDevWanManMacAddress": cabhPsDevWanManMacAddress,
       "cabhPsDevWanDataMacAddress": cabhPsDevWanDataMacAddress,
       "cabhPsDevTypeIdentifier": cabhPsDevTypeIdentifier,
       "cabhPsDevSetToFactory": cabhPsDevSetToFactory,
       "cabhPsDevWanManClientId": cabhPsDevWanManClientId,
       "cabhPsDevTodSyncStatus": cabhPsDevTodSyncStatus,
       "cabhPsDevProvMode": cabhPsDevProvMode,
       "cabhPsDevLastSetToFactory": cabhPsDevLastSetToFactory,
       "cabhPsDevTrapControl": cabhPsDevTrapControl,
       "cabhPsDevProv": cabhPsDevProv,
       "cabhPsDevProvisioningTimer": cabhPsDevProvisioningTimer,
       "cabhPsDevProvConfigFile": cabhPsDevProvConfigFile,
       "cabhPsDevProvConfigHash": cabhPsDevProvConfigHash,
       "cabhPsDevProvConfigFileSize": cabhPsDevProvConfigFileSize,
       "cabhPsDevProvConfigFileStatus": cabhPsDevProvConfigFileStatus,
       "cabhPsDevProvConfigTLVProcessed": cabhPsDevProvConfigTLVProcessed,
       "cabhPsDevProvConfigTLVRejected": cabhPsDevProvConfigTLVRejected,
       "cabhPsDevProvSolicitedKeyTimeout": cabhPsDevProvSolicitedKeyTimeout,
       "cabhPsDevProvState": cabhPsDevProvState,
       "cabhPsDevProvAuthState": cabhPsDevProvAuthState,
       "cabhPsDevProvCorrelationId": cabhPsDevProvCorrelationId,
       "cabhPsDevTimeServerAddrType": cabhPsDevTimeServerAddrType,
       "cabhPsDevTimeServerAddr": cabhPsDevTimeServerAddr,
       "cabhPsDevAttrib": cabhPsDevAttrib,
       "cabhPsDevPsAttrib": cabhPsDevPsAttrib,
       "cabhPsDevPsDeviceType": cabhPsDevPsDeviceType,
       "cabhPsDevPsManufacturerUrl": cabhPsDevPsManufacturerUrl,
       "cabhPsDevPsModelUrl": cabhPsDevPsModelUrl,
       "cabhPsDevPsModelUpc": cabhPsDevPsModelUpc,
       "cabhPsDevBpAttrib": cabhPsDevBpAttrib,
       "cabhPsDevBpProfileTable": cabhPsDevBpProfileTable,
       "cabhPsDevBpProfileEntry": cabhPsDevBpProfileEntry,
       "cabhPsDevBpIndex": cabhPsDevBpIndex,
       "cabhPsDevBpDeviceType": cabhPsDevBpDeviceType,
       "cabhPsDevBpManufacturer": cabhPsDevBpManufacturer,
       "cabhPsDevBpManufacturerUrl": cabhPsDevBpManufacturerUrl,
       "cabhPsDevBpSerialNumber": cabhPsDevBpSerialNumber,
       "cabhPsDevBpHardwareVersion": cabhPsDevBpHardwareVersion,
       "cabhPsDevBpHardwareOptions": cabhPsDevBpHardwareOptions,
       "cabhPsDevBpModelName": cabhPsDevBpModelName,
       "cabhPsDevBpModelNumber": cabhPsDevBpModelNumber,
       "cabhPsDevBpModelUrl": cabhPsDevBpModelUrl,
       "cabhPsDevBpModelUpc": cabhPsDevBpModelUpc,
       "cabhPsDevBpModelSoftwareOs": cabhPsDevBpModelSoftwareOs,
       "cabhPsDevBpModelSoftwareVersion": cabhPsDevBpModelSoftwareVersion,
       "cabhPsDevBpLanInterfaceType": cabhPsDevBpLanInterfaceType,
       "cabhPsDevBpNumberInterfacePriorities": cabhPsDevBpNumberInterfacePriorities,
       "cabhPsDevBpPhysicalLocation": cabhPsDevBpPhysicalLocation,
       "cabhPsDevBpPhysicalAddress": cabhPsDevBpPhysicalAddress,
       "cabhPsDevStats": cabhPsDevStats,
       "cabhPsDevLanIpTrafficCountersReset": cabhPsDevLanIpTrafficCountersReset,
       "cabhPsDevLanIpTrafficCountersLastReset": cabhPsDevLanIpTrafficCountersLastReset,
       "cabhPsDevLanIpTrafficEnabled": cabhPsDevLanIpTrafficEnabled,
       "cabhPsDevLanIpTrafficTable": cabhPsDevLanIpTrafficTable,
       "cabhPsDevLanIpTrafficEntry": cabhPsDevLanIpTrafficEntry,
       "cabhPsDevLanIpTrafficIndex": cabhPsDevLanIpTrafficIndex,
       "cabhPsDevLanIpTrafficInetAddressType": cabhPsDevLanIpTrafficInetAddressType,
       "cabhPsDevLanIpTrafficInetAddress": cabhPsDevLanIpTrafficInetAddress,
       "cabhPsDevLanIpTrafficInOctets": cabhPsDevLanIpTrafficInOctets,
       "cabhPsDevLanIpTrafficOutOctets": cabhPsDevLanIpTrafficOutOctets,
       "cabhPsDevAccessControl": cabhPsDevAccessControl,
       "cabhPsDevAccessControlEnable": cabhPsDevAccessControlEnable,
       "cabhPsDevAccessControlTable": cabhPsDevAccessControlTable,
       "cabhPsDevAccessControlEntry": cabhPsDevAccessControlEntry,
       "cabhPsDevAccessControlIndex": cabhPsDevAccessControlIndex,
       "cabhPsDevAccessControlPhysAddr": cabhPsDevAccessControlPhysAddr,
       "cabhPsDevAccessControlRowStatus": cabhPsDevAccessControlRowStatus,
       "cabhPsDevMisc": cabhPsDevMisc,
       "cabhPsDevUI": cabhPsDevUI,
       "cabhPsDevUILogin": cabhPsDevUILogin,
       "cabhPsDevUIPassword": cabhPsDevUIPassword,
       "cabhPsDevUISelection": cabhPsDevUISelection,
       "cabhPsDevUIServerUrl": cabhPsDevUIServerUrl,
       "cabhPsDevUISelectionDisabledBodyText": cabhPsDevUISelectionDisabledBodyText,
       "cabhPsDev802dot11": cabhPsDev802dot11,
       "cabhPsDev802dot11BaseTable": cabhPsDev802dot11BaseTable,
       "cabhPsDev802dot11BaseEntry": cabhPsDev802dot11BaseEntry,
       "cabhPsDev802dot11BaseSetToDefault": cabhPsDev802dot11BaseSetToDefault,
       "cabhPsDev802dot11BaseLastSetToDefault": cabhPsDev802dot11BaseLastSetToDefault,
       "cabhPsDev802dot11BaseAdvertiseSSID": cabhPsDev802dot11BaseAdvertiseSSID,
       "cabhPsDev802dot11BasePhyCapabilities": cabhPsDev802dot11BasePhyCapabilities,
       "cabhPsDev802dot11BasePhyOperMode": cabhPsDev802dot11BasePhyOperMode,
       "cabhPsDev802dot11SecTable": cabhPsDev802dot11SecTable,
       "cabhPsDev802dot11SecEntry": cabhPsDev802dot11SecEntry,
       "cabhPsDev802dot11SecCapabilities": cabhPsDev802dot11SecCapabilities,
       "cabhPsDev802dot11SecOperMode": cabhPsDev802dot11SecOperMode,
       "cabhPsDev802dot11SecPassPhraseToWEPKey": cabhPsDev802dot11SecPassPhraseToWEPKey,
       "cabhPsDev802dot11SecUsePassPhraseToWEPKeyAlg": cabhPsDev802dot11SecUsePassPhraseToWEPKeyAlg,
       "cabhPsDev802dot11SecPSKPassPhraseToKey": cabhPsDev802dot11SecPSKPassPhraseToKey,
       "cabhPsDev802dot11SecWPAPreSharedKey": cabhPsDev802dot11SecWPAPreSharedKey,
       "cabhPsDev802dot11SecWPARekeyTime": cabhPsDev802dot11SecWPARekeyTime,
       "cabhPsDev802dot11SecControl": cabhPsDev802dot11SecControl,
       "cabhPsDev802dot11SecCommitStatus": cabhPsDev802dot11SecCommitStatus,
       "cabhPsDevUpnp": cabhPsDevUpnp,
       "cabhPsDevUpnpBase": cabhPsDevUpnpBase,
       "cabhPsDevUpnpEnabled": cabhPsDevUpnpEnabled,
       "cabhPsDevUpnpCommands": cabhPsDevUpnpCommands,
       "cabhPsDevUpnpCommandIpType": cabhPsDevUpnpCommandIpType,
       "cabhPsDevUpnpCommandIp": cabhPsDevUpnpCommandIp,
       "cabhPsDevUpnpCommand": cabhPsDevUpnpCommand,
       "cabhPsDevUpnpCommandUpdate": cabhPsDevUpnpCommandUpdate,
       "cabhPsDevUpnpLastCommandUpdate": cabhPsDevUpnpLastCommandUpdate,
       "cabhPsDevUpnpCommandStatus": cabhPsDevUpnpCommandStatus,
       "cabhPsDevUpnpInfoTable": cabhPsDevUpnpInfoTable,
       "cabhPsDevUpnpInfoEntry": cabhPsDevUpnpInfoEntry,
       "cabhPsDevUpnpInfoIpType": cabhPsDevUpnpInfoIpType,
       "cabhPsDevUpnpInfoIp": cabhPsDevUpnpInfoIp,
       "cabhPsDevUpnpInfoXmlFragmentIndex": cabhPsDevUpnpInfoXmlFragmentIndex,
       "cabhPsDevUpnpInfoXmlFragment": cabhPsDevUpnpInfoXmlFragment,
       "cabhPsNotification": cabhPsNotification,
       "cabhPsDevNotifications": cabhPsDevNotifications,
       "cabhPsDevInitTLVUnknownTrap": cabhPsDevInitTLVUnknownTrap,
       "cabhPsDevInitTrap": cabhPsDevInitTrap,
       "cabhPsDevInitRetryTrap": cabhPsDevInitRetryTrap,
       "cabhPsDevDHCPFailTrap": cabhPsDevDHCPFailTrap,
       "cabhPsDevSwUpgradeInitTrap": cabhPsDevSwUpgradeInitTrap,
       "cabhPsDevSwUpgradeFailTrap": cabhPsDevSwUpgradeFailTrap,
       "cabhPsDevSwUpgradeSuccessTrap": cabhPsDevSwUpgradeSuccessTrap,
       "cabhPsDevSwUpgradeCVCFailTrap": cabhPsDevSwUpgradeCVCFailTrap,
       "cabhPsDevTODFailTrap": cabhPsDevTODFailTrap,
       "cabhPsDevCdpWanDataIpTrap": cabhPsDevCdpWanDataIpTrap,
       "cabhPsDevCdpThresholdTrap": cabhPsDevCdpThresholdTrap,
       "cabhPsDevCspTrap": cabhPsDevCspTrap,
       "cabhPsDevCapTrap": cabhPsDevCapTrap,
       "cabhPsDevCtpTrap": cabhPsDevCtpTrap,
       "cabhPsDevProvEnrollTrap": cabhPsDevProvEnrollTrap,
       "cabhPsDevCdpLanIpPoolTrap": cabhPsDevCdpLanIpPoolTrap,
       "cabhPsDevUpnpMultiplePHTrap": cabhPsDevUpnpMultiplePHTrap,
       "cabhPsConformance": cabhPsConformance,
       "cabhPsCompliances": cabhPsCompliances,
       "cabhPsBasicCompliance": cabhPsBasicCompliance,
       "cabhPsDeprecatedCompliance": cabhPsDeprecatedCompliance,
       "cabhPsObsoleteCompliance": cabhPsObsoleteCompliance,
       "cabhPsGroups": cabhPsGroups,
       "cabhPsDevBaseGroup": cabhPsDevBaseGroup,
       "cabhPsDevProvGroup": cabhPsDevProvGroup,
       "cabhPsDevAttribGroup": cabhPsDevAttribGroup,
       "cabhPsDevStatsGroup": cabhPsDevStatsGroup,
       "cabhPsDevDeprecatedGroup": cabhPsDevDeprecatedGroup,
       "cabhPsNotificationGroup": cabhPsNotificationGroup,
       "cabhPsDevAccessControlGroup": cabhPsDevAccessControlGroup,
       "cabhPsDevUIGroup": cabhPsDevUIGroup,
       "cabhPsDev802dot11Group": cabhPsDev802dot11Group,
       "cabhPsDevUpnpGroup": cabhPsDevUpnpGroup,
       "cabhPsDevObsoleteGroup": cabhPsDevObsoleteGroup}
)
