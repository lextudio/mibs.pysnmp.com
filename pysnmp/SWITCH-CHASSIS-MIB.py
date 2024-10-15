# SNMP MIB module (SWITCH-CHASSIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DEFINITIONS
# Produced by pysmi-1.5.4 at Mon Oct 14 21:23:45 2024
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
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")

(switchChassis,) = mibBuilder.importSymbols(
    "TELESYN-ATI-TC",
    "switchChassis")


# MODULE-IDENTITY

switchChassisMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1)
)
switchChassisMib.setRevisions(
        ("1997-04-29 20:00",
         "1997-01-14 20:00",
         "1996-12-19 22:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HostNameOrIpAddr(DisplayString, TextualConvention):
    status = "current"


class HwIdentifier(OctetString, TextualConvention):
    status = "current"
    displayHint = "2d.2d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )



class SwVersionId(OctetString, TextualConvention):
    status = "current"
    displayHint = "2d.2d.2d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )



# MIB Managed Objects in the order of their OIDs

_ChassisParams_ObjectIdentity = ObjectIdentity
chassisParams = _ChassisParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 1)
)


class _ChassisSerialNumber_Type(DisplayString):
    """Custom type chassisSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ChassisSerialNumber_Type.__name__ = "DisplayString"
_ChassisSerialNumber_Object = MibScalar
chassisSerialNumber = _ChassisSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 1, 1),
    _ChassisSerialNumber_Type()
)
chassisSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisSerialNumber.setStatus("current")
_ChassisHwId_Type = HwIdentifier
_ChassisHwId_Object = MibScalar
chassisHwId = _ChassisHwId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 1, 2),
    _ChassisHwId_Type()
)
chassisHwId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisHwId.setStatus("current")


class _ChassisOSVersion_Type(DisplayString):
    """Custom type chassisOSVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ChassisOSVersion_Type.__name__ = "DisplayString"
_ChassisOSVersion_Object = MibScalar
chassisOSVersion = _ChassisOSVersion_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 1, 3),
    _ChassisOSVersion_Type()
)
chassisOSVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisOSVersion.setStatus("current")


class _ChassisFwVersion_Type(DisplayString):
    """Custom type chassisFwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_ChassisFwVersion_Type.__name__ = "DisplayString"
_ChassisFwVersion_Object = MibScalar
chassisFwVersion = _ChassisFwVersion_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 1, 4),
    _ChassisFwVersion_Type()
)
chassisFwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisFwVersion.setStatus("current")
_ChassisLastChanges_Type = Counter32
_ChassisLastChanges_Object = MibScalar
chassisLastChanges = _ChassisLastChanges_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 1, 5),
    _ChassisLastChanges_Type()
)
chassisLastChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisLastChanges.setStatus("current")
_ChassisBaseMacAddress_Type = MacAddress
_ChassisBaseMacAddress_Object = MibScalar
chassisBaseMacAddress = _ChassisBaseMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 1, 6),
    _ChassisBaseMacAddress_Type()
)
chassisBaseMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisBaseMacAddress.setStatus("current")


class _ChassisFanStatus_Type(Integer32):
    """Custom type chassisFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("slowOrStopped", 2))
    )


_ChassisFanStatus_Type.__name__ = "Integer32"
_ChassisFanStatus_Object = MibScalar
chassisFanStatus = _ChassisFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 1, 7),
    _ChassisFanStatus_Type()
)
chassisFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisFanStatus.setStatus("current")


class _ChassisBoardSerialNumber_Type(DisplayString):
    """Custom type chassisBoardSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_ChassisBoardSerialNumber_Type.__name__ = "DisplayString"
_ChassisBoardSerialNumber_Object = MibScalar
chassisBoardSerialNumber = _ChassisBoardSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 1, 8),
    _ChassisBoardSerialNumber_Type()
)
chassisBoardSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisBoardSerialNumber.setStatus("current")
_IpParams_ObjectIdentity = ObjectIdentity
ipParams = _IpParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 3)
)
_IpAddr_Type = IpAddress
_IpAddr_Object = MibScalar
ipAddr = _IpAddr_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 3, 1),
    _IpAddr_Type()
)
ipAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAddr.setStatus("obsolete")
_IpNetMask_Type = IpAddress
_IpNetMask_Object = MibScalar
ipNetMask = _IpNetMask_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 3, 2),
    _IpNetMask_Type()
)
ipNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNetMask.setStatus("obsolete")


class _IpBcastForm_Type(Integer32):
    """Custom type ipBcastForm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allOnes", 1),
          ("allZeros", 2))
    )


_IpBcastForm_Type.__name__ = "Integer32"
_IpBcastForm_Object = MibScalar
ipBcastForm = _IpBcastForm_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 3, 3),
    _IpBcastForm_Type()
)
ipBcastForm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipBcastForm.setStatus("obsolete")


class _IpEncap_Type(Integer32):
    """Custom type ipEncap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 1),
          ("ieee8022", 2))
    )


_IpEncap_Type.__name__ = "Integer32"
_IpEncap_Object = MibScalar
ipEncap = _IpEncap_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 3, 4),
    _IpEncap_Type()
)
ipEncap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipEncap.setStatus("obsolete")
_IpDefaultGateway_Type = IpAddress
_IpDefaultGateway_Object = MibScalar
ipDefaultGateway = _IpDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 3, 5),
    _IpDefaultGateway_Type()
)
ipDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipDefaultGateway.setStatus("obsolete")


class _IpDomainName_Type(DisplayString):
    """Custom type ipDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_IpDomainName_Type.__name__ = "DisplayString"
_IpDomainName_Object = MibScalar
ipDomainName = _IpDomainName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 3, 6),
    _IpDomainName_Type()
)
ipDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipDomainName.setStatus("obsolete")
_SysConfigParams_ObjectIdentity = ObjectIdentity
sysConfigParams = _SysConfigParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 4)
)


class _BootFlag_Type(Integer32):
    """Custom type bootFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              8,
              16,
              32,
              48,
              64,
              128,
              192)
        )
    )
    namedValues = NamedValues(
        *(("bootDiag", 48),
          ("bootLoader", 16),
          ("bootNetwork", 32),
          ("bootSystem", 0),
          ("loopPost", 8),
          ("networkCom0", 192),
          ("networkEth0", 64),
          ("networkEth1", 128),
          ("runMonitor", 2),
          ("skipPost", 1),
          ("useBackupBoot", 4))
    )


_BootFlag_Type.__name__ = "Integer32"
_BootFlag_Object = MibScalar
bootFlag = _BootFlag_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 4, 1),
    _BootFlag_Type()
)
bootFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootFlag.setStatus("deprecated")
_DramSize_Type = Unsigned32
_DramSize_Object = MibScalar
dramSize = _DramSize_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 4, 2),
    _DramSize_Type()
)
dramSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dramSize.setStatus("current")
_CpuVer_Type = HwIdentifier
_CpuVer_Object = MibScalar
cpuVer = _CpuVer_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 4, 3),
    _CpuVer_Type()
)
cpuVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuVer.setStatus("current")
_IscVer_Type = HwIdentifier
_IscVer_Object = MibScalar
iscVer = _IscVer_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 4, 4),
    _IscVer_Type()
)
iscVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iscVer.setStatus("current")
_PigVer_Type = HwIdentifier
_PigVer_Object = MibScalar
pigVer = _PigVer_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 4, 5),
    _PigVer_Type()
)
pigVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pigVer.setStatus("current")
_PostVer_Type = SwVersionId
_PostVer_Object = MibScalar
postVer = _PostVer_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 4, 6),
    _PostVer_Type()
)
postVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    postVer.setStatus("current")
_IsdVer_Type = SwVersionId
_IsdVer_Object = MibScalar
isdVer = _IsdVer_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 4, 7),
    _IsdVer_Type()
)
isdVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isdVer.setStatus("current")
_BootVer_Type = SwVersionId
_BootVer_Object = MibScalar
bootVer = _BootVer_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 4, 8),
    _BootVer_Type()
)
bootVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootVer.setStatus("current")
_QmuMemSize_Type = Unsigned32
_QmuMemSize_Object = MibScalar
qmuMemSize = _QmuMemSize_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 4, 9),
    _QmuMemSize_Type()
)
qmuMemSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qmuMemSize.setStatus("current")
_SegBusTable_Object = MibTable
segBusTable = _SegBusTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 4, 10)
)
if mibBuilder.loadTexts:
    segBusTable.setStatus("current")
_SegBusEntry_Object = MibTableRow
segBusEntry = _SegBusEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 4, 10, 1)
)
segBusEntry.setIndexNames(
    (0, "SWITCH-CHASSIS-MIB", "segBusIndex"),
)
if mibBuilder.loadTexts:
    segBusEntry.setStatus("current")


class _SegBusIndex_Type(Integer32):
    """Custom type segBusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SegBusIndex_Type.__name__ = "Integer32"
_SegBusIndex_Object = MibTableColumn
segBusIndex = _SegBusIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 4, 10, 1, 1),
    _SegBusIndex_Type()
)
segBusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    segBusIndex.setStatus("current")
_SegBusPmiuId_Type = HwIdentifier
_SegBusPmiuId_Object = MibTableColumn
segBusPmiuId = _SegBusPmiuId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 4, 10, 1, 2),
    _SegBusPmiuId_Type()
)
segBusPmiuId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    segBusPmiuId.setStatus("current")
_SegBusQmuId_Type = HwIdentifier
_SegBusQmuId_Object = MibTableColumn
segBusQmuId = _SegBusQmuId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 4, 10, 1, 3),
    _SegBusQmuId_Type()
)
segBusQmuId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    segBusQmuId.setStatus("current")
_SnmpParams_ObjectIdentity = ObjectIdentity
snmpParams = _SnmpParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 6)
)
_SnmpIpTrapRcvrTable_Object = MibTable
snmpIpTrapRcvrTable = _SnmpIpTrapRcvrTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 6, 1)
)
if mibBuilder.loadTexts:
    snmpIpTrapRcvrTable.setStatus("current")
_SnmpIpTrapRcvrEntry_Object = MibTableRow
snmpIpTrapRcvrEntry = _SnmpIpTrapRcvrEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 6, 1, 1)
)
snmpIpTrapRcvrEntry.setIndexNames(
    (0, "SWITCH-CHASSIS-MIB", "snmpIpTrapRcvrIpAddress"),
)
if mibBuilder.loadTexts:
    snmpIpTrapRcvrEntry.setStatus("current")
_SnmpIpTrapRcvrIpAddress_Type = IpAddress
_SnmpIpTrapRcvrIpAddress_Object = MibTableColumn
snmpIpTrapRcvrIpAddress = _SnmpIpTrapRcvrIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 6, 1, 1, 1),
    _SnmpIpTrapRcvrIpAddress_Type()
)
snmpIpTrapRcvrIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snmpIpTrapRcvrIpAddress.setStatus("current")


class _SnmpIpTrapRcvrPort_Type(Integer32):
    """Custom type snmpIpTrapRcvrPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SnmpIpTrapRcvrPort_Type.__name__ = "Integer32"
_SnmpIpTrapRcvrPort_Object = MibTableColumn
snmpIpTrapRcvrPort = _SnmpIpTrapRcvrPort_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 6, 1, 1, 2),
    _SnmpIpTrapRcvrPort_Type()
)
snmpIpTrapRcvrPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpIpTrapRcvrPort.setStatus("current")


class _SnmpIpTrapRcvrCommunity_Type(DisplayString):
    """Custom type snmpIpTrapRcvrCommunity based on DisplayString"""
    defaultValue = OctetString("public")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_SnmpIpTrapRcvrCommunity_Type.__name__ = "DisplayString"
_SnmpIpTrapRcvrCommunity_Object = MibTableColumn
snmpIpTrapRcvrCommunity = _SnmpIpTrapRcvrCommunity_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 6, 1, 1, 3),
    _SnmpIpTrapRcvrCommunity_Type()
)
snmpIpTrapRcvrCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpIpTrapRcvrCommunity.setStatus("current")
_SnmpIpTrapRcvrStatus_Type = RowStatus
_SnmpIpTrapRcvrStatus_Object = MibTableColumn
snmpIpTrapRcvrStatus = _SnmpIpTrapRcvrStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 6, 1, 1, 4),
    _SnmpIpTrapRcvrStatus_Type()
)
snmpIpTrapRcvrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpIpTrapRcvrStatus.setStatus("current")
_SnmpUnAuthIpAddr_Type = IpAddress
_SnmpUnAuthIpAddr_Object = MibScalar
snmpUnAuthIpAddr = _SnmpUnAuthIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 6, 2),
    _SnmpUnAuthIpAddr_Type()
)
snmpUnAuthIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpUnAuthIpAddr.setStatus("current")


class _SnmpUnAuthCommunity_Type(OctetString):
    """Custom type snmpUnAuthCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SnmpUnAuthCommunity_Type.__name__ = "OctetString"
_SnmpUnAuthCommunity_Object = MibScalar
snmpUnAuthCommunity = _SnmpUnAuthCommunity_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 6, 3),
    _SnmpUnAuthCommunity_Type()
)
snmpUnAuthCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpUnAuthCommunity.setStatus("current")
_ConsoleParams_ObjectIdentity = ObjectIdentity
consoleParams = _ConsoleParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 7)
)
_ConsolePortSpeed_Type = Unsigned32
_ConsolePortSpeed_Object = MibScalar
consolePortSpeed = _ConsolePortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 7, 1),
    _ConsolePortSpeed_Type()
)
consolePortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consolePortSpeed.setStatus("deprecated")


class _ConsolePortDataBits_Type(Integer32):
    """Custom type consolePortDataBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(7, 8),
    )


_ConsolePortDataBits_Type.__name__ = "Integer32"
_ConsolePortDataBits_Object = MibScalar
consolePortDataBits = _ConsolePortDataBits_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 7, 2),
    _ConsolePortDataBits_Type()
)
consolePortDataBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consolePortDataBits.setStatus("deprecated")


class _ConsolePortStopBits_Type(Integer32):
    """Custom type consolePortStopBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("one", 1),
          ("onePointFive", 3),
          ("two", 2))
    )


_ConsolePortStopBits_Type.__name__ = "Integer32"
_ConsolePortStopBits_Object = MibScalar
consolePortStopBits = _ConsolePortStopBits_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 7, 3),
    _ConsolePortStopBits_Type()
)
consolePortStopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consolePortStopBits.setStatus("deprecated")


class _ConsolePortParity_Type(Integer32):
    """Custom type consolePortParity based on Integer32"""
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
        *(("even", 3),
          ("mark", 4),
          ("none", 1),
          ("odd", 2),
          ("space", 5))
    )


_ConsolePortParity_Type.__name__ = "Integer32"
_ConsolePortParity_Object = MibScalar
consolePortParity = _ConsolePortParity_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 7, 4),
    _ConsolePortParity_Type()
)
consolePortParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consolePortParity.setStatus("deprecated")
_LogParams_ObjectIdentity = ObjectIdentity
logParams = _LogParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 8)
)


class _EventLogEnable_Type(Integer32):
    """Custom type eventLogEnable based on Integer32"""
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


_EventLogEnable_Type.__name__ = "Integer32"
_EventLogEnable_Object = MibScalar
eventLogEnable = _EventLogEnable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 8, 1),
    _EventLogEnable_Type()
)
eventLogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventLogEnable.setStatus("current")
_EventLogSize_Type = Unsigned32
_EventLogSize_Object = MibScalar
eventLogSize = _EventLogSize_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 8, 2),
    _EventLogSize_Type()
)
eventLogSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogSize.setStatus("current")
_EventLogCount_Type = Unsigned32
_EventLogCount_Object = MibScalar
eventLogCount = _EventLogCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 8, 3),
    _EventLogCount_Type()
)
eventLogCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogCount.setStatus("current")
_EventLogTable_Object = MibTable
eventLogTable = _EventLogTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 8, 4)
)
if mibBuilder.loadTexts:
    eventLogTable.setStatus("current")
_EventLogEntry_Object = MibTableRow
eventLogEntry = _EventLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 8, 4, 1)
)
eventLogEntry.setIndexNames(
    (0, "SWITCH-CHASSIS-MIB", "eventLogIndex"),
)
if mibBuilder.loadTexts:
    eventLogEntry.setStatus("current")


class _EventLogIndex_Type(Integer32):
    """Custom type eventLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EventLogIndex_Type.__name__ = "Integer32"
_EventLogIndex_Object = MibTableColumn
eventLogIndex = _EventLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 8, 4, 1, 1),
    _EventLogIndex_Type()
)
eventLogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eventLogIndex.setStatus("current")
_EventLogTime_Type = DisplayString
_EventLogTime_Object = MibTableColumn
eventLogTime = _EventLogTime_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 8, 4, 1, 2),
    _EventLogTime_Type()
)
eventLogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogTime.setStatus("current")
_EventLogDescr_Type = DisplayString
_EventLogDescr_Object = MibTableColumn
eventLogDescr = _EventLogDescr_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 8, 4, 1, 3),
    _EventLogDescr_Type()
)
eventLogDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogDescr.setStatus("current")
_EventLogDetail_Type = DisplayString
_EventLogDetail_Object = MibTableColumn
eventLogDetail = _EventLogDetail_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 8, 4, 1, 4),
    _EventLogDetail_Type()
)
eventLogDetail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogDetail.setStatus("current")


class _EventLogRawEntry_Type(OctetString):
    """Custom type eventLogRawEntry based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EventLogRawEntry_Type.__name__ = "OctetString"
_EventLogRawEntry_Object = MibTableColumn
eventLogRawEntry = _EventLogRawEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 8, 4, 1, 5),
    _EventLogRawEntry_Type()
)
eventLogRawEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventLogRawEntry.setStatus("current")
_BootParams_ObjectIdentity = ObjectIdentity
bootParams = _BootParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 9)
)


class _DeviceReset_Type(Integer32):
    """Custom type deviceReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 1),
          ("reset", 2))
    )


_DeviceReset_Type.__name__ = "Integer32"
_DeviceReset_Object = MibScalar
deviceReset = _DeviceReset_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 9, 1),
    _DeviceReset_Type()
)
deviceReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceReset.setStatus("current")
_TftpGroup_ObjectIdentity = ObjectIdentity
tftpGroup = _TftpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 9, 4)
)
_TftpServerName_Type = HostNameOrIpAddr
_TftpServerName_Object = MibScalar
tftpServerName = _TftpServerName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 9, 4, 1),
    _TftpServerName_Type()
)
tftpServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpServerName.setStatus("current")


class _TftpUserName_Type(OctetString):
    """Custom type tftpUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_TftpUserName_Type.__name__ = "OctetString"
_TftpUserName_Object = MibScalar
tftpUserName = _TftpUserName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 9, 4, 2),
    _TftpUserName_Type()
)
tftpUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpUserName.setStatus("current")


class _TftpRemoteFileName_Type(OctetString):
    """Custom type tftpRemoteFileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_TftpRemoteFileName_Type.__name__ = "OctetString"
_TftpRemoteFileName_Object = MibScalar
tftpRemoteFileName = _TftpRemoteFileName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 9, 4, 3),
    _TftpRemoteFileName_Type()
)
tftpRemoteFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpRemoteFileName.setStatus("current")


class _TftpLocalFileName_Type(OctetString):
    """Custom type tftpLocalFileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_TftpLocalFileName_Type.__name__ = "OctetString"
_TftpLocalFileName_Object = MibScalar
tftpLocalFileName = _TftpLocalFileName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 9, 4, 4),
    _TftpLocalFileName_Type()
)
tftpLocalFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpLocalFileName.setStatus("current")


class _TftpOperation_Type(Integer32):
    """Custom type tftpOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("getFile", 2),
          ("getFirmware", 3),
          ("putFile", 1))
    )


_TftpOperation_Type.__name__ = "Integer32"
_TftpOperation_Object = MibScalar
tftpOperation = _TftpOperation_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 9, 4, 5),
    _TftpOperation_Type()
)
tftpOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpOperation.setStatus("current")


class _TftpAdminState_Type(Integer32):
    """Custom type tftpAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("configure", 1),
          ("execute", 2))
    )


_TftpAdminState_Type.__name__ = "Integer32"
_TftpAdminState_Object = MibScalar
tftpAdminState = _TftpAdminState_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 9, 4, 6),
    _TftpAdminState_Type()
)
tftpAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpAdminState.setStatus("current")


class _TftpOperationState_Type(Integer32):
    """Custom type tftpOperationState based on Integer32"""
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
        *(("executing", 2),
          ("inactive", 1),
          ("localFileProblem", 4),
          ("otherFailure", 8),
          ("remoteFileProblem", 7),
          ("succeeded", 3),
          ("timedOut", 6),
          ("unknownHost", 5))
    )


_TftpOperationState_Type.__name__ = "Integer32"
_TftpOperationState_Object = MibScalar
tftpOperationState = _TftpOperationState_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 9, 4, 7),
    _TftpOperationState_Type()
)
tftpOperationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tftpOperationState.setStatus("current")
_TftpOperationStateChange_Type = TimeStamp
_TftpOperationStateChange_Object = MibScalar
tftpOperationStateChange = _TftpOperationStateChange_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 9, 4, 8),
    _TftpOperationStateChange_Type()
)
tftpOperationStateChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tftpOperationStateChange.setStatus("current")


class _TftpErrorMessage_Type(DisplayString):
    """Custom type tftpErrorMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_TftpErrorMessage_Type.__name__ = "DisplayString"
_TftpErrorMessage_Object = MibScalar
tftpErrorMessage = _TftpErrorMessage_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 9, 1, 1, 9, 4, 9),
    _TftpErrorMessage_Type()
)
tftpErrorMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tftpErrorMessage.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SWITCH-CHASSIS-MIB",
    **{"HostNameOrIpAddr": HostNameOrIpAddr,
       "HwIdentifier": HwIdentifier,
       "SwVersionId": SwVersionId,
       "switchChassisMib": switchChassisMib,
       "chassisParams": chassisParams,
       "chassisSerialNumber": chassisSerialNumber,
       "chassisHwId": chassisHwId,
       "chassisOSVersion": chassisOSVersion,
       "chassisFwVersion": chassisFwVersion,
       "chassisLastChanges": chassisLastChanges,
       "chassisBaseMacAddress": chassisBaseMacAddress,
       "chassisFanStatus": chassisFanStatus,
       "chassisBoardSerialNumber": chassisBoardSerialNumber,
       "ipParams": ipParams,
       "ipAddr": ipAddr,
       "ipNetMask": ipNetMask,
       "ipBcastForm": ipBcastForm,
       "ipEncap": ipEncap,
       "ipDefaultGateway": ipDefaultGateway,
       "ipDomainName": ipDomainName,
       "sysConfigParams": sysConfigParams,
       "bootFlag": bootFlag,
       "dramSize": dramSize,
       "cpuVer": cpuVer,
       "iscVer": iscVer,
       "pigVer": pigVer,
       "postVer": postVer,
       "isdVer": isdVer,
       "bootVer": bootVer,
       "qmuMemSize": qmuMemSize,
       "segBusTable": segBusTable,
       "segBusEntry": segBusEntry,
       "segBusIndex": segBusIndex,
       "segBusPmiuId": segBusPmiuId,
       "segBusQmuId": segBusQmuId,
       "snmpParams": snmpParams,
       "snmpIpTrapRcvrTable": snmpIpTrapRcvrTable,
       "snmpIpTrapRcvrEntry": snmpIpTrapRcvrEntry,
       "snmpIpTrapRcvrIpAddress": snmpIpTrapRcvrIpAddress,
       "snmpIpTrapRcvrPort": snmpIpTrapRcvrPort,
       "snmpIpTrapRcvrCommunity": snmpIpTrapRcvrCommunity,
       "snmpIpTrapRcvrStatus": snmpIpTrapRcvrStatus,
       "snmpUnAuthIpAddr": snmpUnAuthIpAddr,
       "snmpUnAuthCommunity": snmpUnAuthCommunity,
       "consoleParams": consoleParams,
       "consolePortSpeed": consolePortSpeed,
       "consolePortDataBits": consolePortDataBits,
       "consolePortStopBits": consolePortStopBits,
       "consolePortParity": consolePortParity,
       "logParams": logParams,
       "eventLogEnable": eventLogEnable,
       "eventLogSize": eventLogSize,
       "eventLogCount": eventLogCount,
       "eventLogTable": eventLogTable,
       "eventLogEntry": eventLogEntry,
       "eventLogIndex": eventLogIndex,
       "eventLogTime": eventLogTime,
       "eventLogDescr": eventLogDescr,
       "eventLogDetail": eventLogDetail,
       "eventLogRawEntry": eventLogRawEntry,
       "bootParams": bootParams,
       "deviceReset": deviceReset,
       "tftpGroup": tftpGroup,
       "tftpServerName": tftpServerName,
       "tftpUserName": tftpUserName,
       "tftpRemoteFileName": tftpRemoteFileName,
       "tftpLocalFileName": tftpLocalFileName,
       "tftpOperation": tftpOperation,
       "tftpAdminState": tftpAdminState,
       "tftpOperationState": tftpOperationState,
       "tftpOperationStateChange": tftpOperationStateChange,
       "tftpErrorMessage": tftpErrorMessage}
)
