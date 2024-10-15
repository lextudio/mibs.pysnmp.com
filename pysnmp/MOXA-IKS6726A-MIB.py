# SNMP MIB module (MOXA-IKS6726A-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MOXA-IKS6726A-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:22:40 2024
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

(DateAndTime,
 DisplayString,
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

iks6726A = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116)
)
iks6726A.setRevisions(
        ("2015-06-30 00:00",
         "2014-08-07 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PortList(OctetString, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_Moxa_ObjectIdentity = ObjectIdentity
moxa = _Moxa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691)
)
_IndustrialEthernet_ObjectIdentity = ObjectIdentity
industrialEthernet = _IndustrialEthernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7)
)
_MibNotificationsPrefix_ObjectIdentity = ObjectIdentity
mibNotificationsPrefix = _MibNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 0)
)
_SwMgmt_ObjectIdentity = ObjectIdentity
swMgmt = _SwMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1)
)
_NumberOfPorts_Type = Integer32
_NumberOfPorts_Object = MibScalar
numberOfPorts = _NumberOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 1),
    _NumberOfPorts_Type()
)
numberOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOfPorts.setStatus("current")
_SwitchModel_Type = DisplayString
_SwitchModel_Object = MibScalar
switchModel = _SwitchModel_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 2),
    _SwitchModel_Type()
)
switchModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchModel.setStatus("current")
_FirmwareVersion_Type = DisplayString
_FirmwareVersion_Object = MibScalar
firmwareVersion = _FirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 4),
    _FirmwareVersion_Type()
)
firmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareVersion.setStatus("current")


class _EnableWebConfig_Type(Integer32):
    """Custom type enableWebConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("httpOrHttps", 1),
          ("httpsOnly", 2))
    )


_EnableWebConfig_Type.__name__ = "Integer32"
_EnableWebConfig_Object = MibScalar
enableWebConfig = _EnableWebConfig_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 5),
    _EnableWebConfig_Type()
)
enableWebConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableWebConfig.setStatus("current")


class _EnableTelnetConsole_Type(Integer32):
    """Custom type enableTelnetConsole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_EnableTelnetConsole_Type.__name__ = "Integer32"
_EnableTelnetConsole_Object = MibScalar
enableTelnetConsole = _EnableTelnetConsole_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 6),
    _EnableTelnetConsole_Type()
)
enableTelnetConsole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableTelnetConsole.setStatus("current")


class _LineSwapRecovery_Type(Integer32):
    """Custom type lineSwapRecovery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_LineSwapRecovery_Type.__name__ = "Integer32"
_LineSwapRecovery_Object = MibScalar
lineSwapRecovery = _LineSwapRecovery_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 7),
    _LineSwapRecovery_Type()
)
lineSwapRecovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineSwapRecovery.setStatus("current")
_NetworkSetting_ObjectIdentity = ObjectIdentity
networkSetting = _NetworkSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 8)
)
_SwitchIpAddr_Type = IpAddress
_SwitchIpAddr_Object = MibScalar
switchIpAddr = _SwitchIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 8, 1),
    _SwitchIpAddr_Type()
)
switchIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIpAddr.setStatus("current")
_SwitchIpMask_Type = IpAddress
_SwitchIpMask_Object = MibScalar
switchIpMask = _SwitchIpMask_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 8, 2),
    _SwitchIpMask_Type()
)
switchIpMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchIpMask.setStatus("current")
_DefaultGateway_Type = IpAddress
_DefaultGateway_Object = MibScalar
defaultGateway = _DefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 8, 3),
    _DefaultGateway_Type()
)
defaultGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    defaultGateway.setStatus("current")


class _EnableAutoIpConfig_Type(Integer32):
    """Custom type enableAutoIpConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enableBOOTP", 2),
          ("enableDHCP", 1))
    )


_EnableAutoIpConfig_Type.__name__ = "Integer32"
_EnableAutoIpConfig_Object = MibScalar
enableAutoIpConfig = _EnableAutoIpConfig_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 8, 4),
    _EnableAutoIpConfig_Type()
)
enableAutoIpConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableAutoIpConfig.setStatus("current")
_DnsServer1IpAddr_Type = IpAddress
_DnsServer1IpAddr_Object = MibScalar
dnsServer1IpAddr = _DnsServer1IpAddr_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 8, 5),
    _DnsServer1IpAddr_Type()
)
dnsServer1IpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsServer1IpAddr.setStatus("current")
_SnmpTrapCommunity_Type = DisplayString
_SnmpTrapCommunity_Object = MibScalar
snmpTrapCommunity = _SnmpTrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 8, 6),
    _SnmpTrapCommunity_Type()
)
snmpTrapCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapCommunity.setStatus("current")
_TrapServerAddr_Type = DisplayString
_TrapServerAddr_Object = MibScalar
trapServerAddr = _TrapServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 8, 7),
    _TrapServerAddr_Type()
)
trapServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapServerAddr.setStatus("current")
_DnsServer2IpAddr_Type = IpAddress
_DnsServer2IpAddr_Object = MibScalar
dnsServer2IpAddr = _DnsServer2IpAddr_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 8, 8),
    _DnsServer2IpAddr_Type()
)
dnsServer2IpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsServer2IpAddr.setStatus("current")
_SnmpReadCommunity_Type = DisplayString
_SnmpReadCommunity_Object = MibScalar
snmpReadCommunity = _SnmpReadCommunity_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 8, 9),
    _SnmpReadCommunity_Type()
)
snmpReadCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpReadCommunity.setStatus("current")
_SnmpTrap2Community_Type = DisplayString
_SnmpTrap2Community_Object = MibScalar
snmpTrap2Community = _SnmpTrap2Community_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 8, 11),
    _SnmpTrap2Community_Type()
)
snmpTrap2Community.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrap2Community.setStatus("current")
_Trap2ServerAddr_Type = DisplayString
_Trap2ServerAddr_Object = MibScalar
trap2ServerAddr = _Trap2ServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 8, 12),
    _Trap2ServerAddr_Type()
)
trap2ServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trap2ServerAddr.setStatus("current")


class _SnmpInformEnable_Type(Integer32):
    """Custom type snmpInformEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SnmpInformEnable_Type.__name__ = "Integer32"
_SnmpInformEnable_Object = MibScalar
snmpInformEnable = _SnmpInformEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 8, 13),
    _SnmpInformEnable_Type()
)
snmpInformEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpInformEnable.setStatus("current")


class _SnmpInformRetries_Type(Integer32):
    """Custom type snmpInformRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_SnmpInformRetries_Type.__name__ = "Integer32"
_SnmpInformRetries_Object = MibScalar
snmpInformRetries = _SnmpInformRetries_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 8, 14),
    _SnmpInformRetries_Type()
)
snmpInformRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpInformRetries.setStatus("current")


class _SnmpInformTimeout_Type(Integer32):
    """Custom type snmpInformTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_SnmpInformTimeout_Type.__name__ = "Integer32"
_SnmpInformTimeout_Object = MibScalar
snmpInformTimeout = _SnmpInformTimeout_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 8, 15),
    _SnmpInformTimeout_Type()
)
snmpInformTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpInformTimeout.setStatus("current")
_DhcpRetryPeriods_Type = Integer32
_DhcpRetryPeriods_Object = MibScalar
dhcpRetryPeriods = _DhcpRetryPeriods_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 8, 16),
    _DhcpRetryPeriods_Type()
)
dhcpRetryPeriods.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRetryPeriods.setStatus("current")
_DhcpRetryTimes_Type = Integer32
_DhcpRetryTimes_Object = MibScalar
dhcpRetryTimes = _DhcpRetryTimes_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 8, 17),
    _DhcpRetryTimes_Type()
)
dhcpRetryTimes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpRetryTimes.setStatus("current")


class _TrapVersion_Type(Integer32):
    """Custom type trapVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("snmpv1-Trap", 0),
          ("snmpv2-Inform", 2),
          ("snmpv2-Notification", 1))
    )


_TrapVersion_Type.__name__ = "Integer32"
_TrapVersion_Object = MibScalar
trapVersion = _TrapVersion_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 8, 18),
    _TrapVersion_Type()
)
trapVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapVersion.setStatus("current")
_PortSetting_ObjectIdentity = ObjectIdentity
portSetting = _PortSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 9)
)
_PortTable_Object = MibTable
portTable = _PortTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 9, 1)
)
if mibBuilder.loadTexts:
    portTable.setStatus("current")
_PortEntry_Object = MibTableRow
portEntry = _PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 9, 1, 1)
)
portEntry.setIndexNames(
    (0, "MOXA-IKS6726A-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    portEntry.setStatus("current")
_PortIndex_Type = Integer32
_PortIndex_Object = MibTableColumn
portIndex = _PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 9, 1, 1, 1),
    _PortIndex_Type()
)
portIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portIndex.setStatus("current")
_PortDesc_Type = DisplayString
_PortDesc_Object = MibTableColumn
portDesc = _PortDesc_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 9, 1, 1, 2),
    _PortDesc_Type()
)
portDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDesc.setStatus("current")


class _PortEnable_Type(Integer32):
    """Custom type portEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_PortEnable_Type.__name__ = "Integer32"
_PortEnable_Object = MibTableColumn
portEnable = _PortEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 9, 1, 1, 3),
    _PortEnable_Type()
)
portEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portEnable.setStatus("current")


class _PortSpeed_Type(Integer32):
    """Custom type portSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("speed1000M-Full", 5),
          ("speed100M-Full", 1),
          ("speed100M-Half", 2),
          ("speed10M-Full", 3),
          ("speed10M-Half", 4))
    )


_PortSpeed_Type.__name__ = "Integer32"
_PortSpeed_Object = MibTableColumn
portSpeed = _PortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 9, 1, 1, 4),
    _PortSpeed_Type()
)
portSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSpeed.setStatus("current")


class _PortMDI_Type(Integer32):
    """Custom type portMDI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("mdi", 2),
          ("mdiX", 3),
          ("na", 0))
    )


_PortMDI_Type.__name__ = "Integer32"
_PortMDI_Object = MibTableColumn
portMDI = _PortMDI_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 9, 1, 1, 5),
    _PortMDI_Type()
)
portMDI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portMDI.setStatus("current")


class _PortFDXFlowCtrl_Type(Integer32):
    """Custom type portFDXFlowCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_PortFDXFlowCtrl_Type.__name__ = "Integer32"
_PortFDXFlowCtrl_Object = MibTableColumn
portFDXFlowCtrl = _PortFDXFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 9, 1, 1, 6),
    _PortFDXFlowCtrl_Type()
)
portFDXFlowCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portFDXFlowCtrl.setStatus("current")
_PortName_Type = DisplayString
_PortName_Object = MibTableColumn
portName = _PortName_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 9, 1, 1, 7),
    _PortName_Type()
)
portName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portName.setStatus("current")
_Monitor_ObjectIdentity = ObjectIdentity
monitor = _Monitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 10)
)


class _Power1InputStatus_Type(Integer32):
    """Custom type power1InputStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not-present", 0),
          ("present", 1))
    )


_Power1InputStatus_Type.__name__ = "Integer32"
_Power1InputStatus_Object = MibScalar
power1InputStatus = _Power1InputStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 10, 1),
    _Power1InputStatus_Type()
)
power1InputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    power1InputStatus.setStatus("current")


class _Power2InputStatus_Type(Integer32):
    """Custom type power2InputStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not-present", 0),
          ("present", 1))
    )


_Power2InputStatus_Type.__name__ = "Integer32"
_Power2InputStatus_Object = MibScalar
power2InputStatus = _Power2InputStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 10, 2),
    _Power2InputStatus_Type()
)
power2InputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    power2InputStatus.setStatus("current")
_MonitorPortTable_Object = MibTable
monitorPortTable = _MonitorPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 10, 3)
)
if mibBuilder.loadTexts:
    monitorPortTable.setStatus("current")
_MonitorPortEntry_Object = MibTableRow
monitorPortEntry = _MonitorPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 10, 3, 1)
)
monitorPortEntry.setIndexNames(
    (0, "MOXA-IKS6726A-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    monitorPortEntry.setStatus("current")


class _MonitorLinkStatus_Type(Integer32):
    """Custom type monitorLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", -1),
          ("off", 0),
          ("on", 1))
    )


_MonitorLinkStatus_Type.__name__ = "Integer32"
_MonitorLinkStatus_Object = MibTableColumn
monitorLinkStatus = _MonitorLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 10, 3, 1, 2),
    _MonitorLinkStatus_Type()
)
monitorLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorLinkStatus.setStatus("current")


class _MonitorSpeed_Type(Integer32):
    """Custom type monitorSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("na", -1),
          ("speed1000M-Full", 5),
          ("speed1000M-Half", 4),
          ("speed100M-Full", 3),
          ("speed100M-Half", 2),
          ("speed10M-Full", 1),
          ("speed10M-Half", 0))
    )


_MonitorSpeed_Type.__name__ = "Integer32"
_MonitorSpeed_Object = MibTableColumn
monitorSpeed = _MonitorSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 10, 3, 1, 3),
    _MonitorSpeed_Type()
)
monitorSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorSpeed.setStatus("current")


class _MonitorAutoMDI_Type(Integer32):
    """Custom type monitorAutoMDI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("mdi", 0),
          ("mdiX", 1),
          ("na", -1))
    )


_MonitorAutoMDI_Type.__name__ = "Integer32"
_MonitorAutoMDI_Object = MibTableColumn
monitorAutoMDI = _MonitorAutoMDI_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 10, 3, 1, 4),
    _MonitorAutoMDI_Type()
)
monitorAutoMDI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorAutoMDI.setStatus("current")
_MonitorTraffic_Type = Integer32
_MonitorTraffic_Object = MibTableColumn
monitorTraffic = _MonitorTraffic_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 10, 3, 1, 5),
    _MonitorTraffic_Type()
)
monitorTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorTraffic.setStatus("current")


class _MonitorFDXFlowCtrl_Type(Integer32):
    """Custom type monitorFDXFlowCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_MonitorFDXFlowCtrl_Type.__name__ = "Integer32"
_MonitorFDXFlowCtrl_Object = MibTableColumn
monitorFDXFlowCtrl = _MonitorFDXFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 10, 3, 1, 6),
    _MonitorFDXFlowCtrl_Type()
)
monitorFDXFlowCtrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorFDXFlowCtrl.setStatus("current")
_MonitorTxTraffic_Type = Integer32
_MonitorTxTraffic_Object = MibTableColumn
monitorTxTraffic = _MonitorTxTraffic_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 10, 3, 1, 7),
    _MonitorTxTraffic_Type()
)
monitorTxTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorTxTraffic.setStatus("current")
_MonitorRxTraffic_Type = Integer32
_MonitorRxTraffic_Object = MibTableColumn
monitorRxTraffic = _MonitorRxTraffic_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 10, 3, 1, 8),
    _MonitorRxTraffic_Type()
)
monitorRxTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorRxTraffic.setStatus("current")
_MonitorDiTable_Object = MibTable
monitorDiTable = _MonitorDiTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 10, 4)
)
if mibBuilder.loadTexts:
    monitorDiTable.setStatus("current")
_MonitorDiEntry_Object = MibTableRow
monitorDiEntry = _MonitorDiEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 10, 4, 1)
)
monitorDiEntry.setIndexNames(
    (0, "MOXA-IKS6726A-MIB", "diIndex"),
)
if mibBuilder.loadTexts:
    monitorDiEntry.setStatus("current")


class _DiIndex_Type(Integer32):
    """Custom type diIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_DiIndex_Type.__name__ = "Integer32"
_DiIndex_Object = MibTableColumn
diIndex = _DiIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 10, 4, 1, 1),
    _DiIndex_Type()
)
diIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diIndex.setStatus("current")


class _DiInputStatus_Type(Integer32):
    """Custom type diInputStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_DiInputStatus_Type.__name__ = "Integer32"
_DiInputStatus_Object = MibTableColumn
diInputStatus = _DiInputStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 10, 4, 1, 2),
    _DiInputStatus_Type()
)
diInputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diInputStatus.setStatus("current")
_MonitorSFPTable_Object = MibTable
monitorSFPTable = _MonitorSFPTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 10, 7)
)
if mibBuilder.loadTexts:
    monitorSFPTable.setStatus("current")
_MonitorSFPEntry_Object = MibTableRow
monitorSFPEntry = _MonitorSFPEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 10, 7, 1)
)
monitorSFPEntry.setIndexNames(
    (0, "MOXA-IKS6726A-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    monitorSFPEntry.setStatus("current")
_SfpPort_Type = DisplayString
_SfpPort_Object = MibTableColumn
sfpPort = _SfpPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 10, 7, 1, 1),
    _SfpPort_Type()
)
sfpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpPort.setStatus("current")
_SfpModelName_Type = DisplayString
_SfpModelName_Object = MibTableColumn
sfpModelName = _SfpModelName_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 10, 7, 1, 2),
    _SfpModelName_Type()
)
sfpModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpModelName.setStatus("current")
_SfpTemperature_Type = DisplayString
_SfpTemperature_Object = MibTableColumn
sfpTemperature = _SfpTemperature_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 10, 7, 1, 3),
    _SfpTemperature_Type()
)
sfpTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpTemperature.setStatus("current")
_SfpVoltage_Type = DisplayString
_SfpVoltage_Object = MibTableColumn
sfpVoltage = _SfpVoltage_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 10, 7, 1, 4),
    _SfpVoltage_Type()
)
sfpVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpVoltage.setStatus("current")
_SfpTxPower_Type = DisplayString
_SfpTxPower_Object = MibTableColumn
sfpTxPower = _SfpTxPower_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 10, 7, 1, 5),
    _SfpTxPower_Type()
)
sfpTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpTxPower.setStatus("current")
_SfpRxPower_Type = DisplayString
_SfpRxPower_Object = MibTableColumn
sfpRxPower = _SfpRxPower_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 10, 7, 1, 6),
    _SfpRxPower_Type()
)
sfpRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sfpRxPower.setStatus("current")
_PowerConsumption_Type = DisplayString
_PowerConsumption_Object = MibScalar
powerConsumption = _PowerConsumption_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 10, 8),
    _PowerConsumption_Type()
)
powerConsumption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    powerConsumption.setStatus("current")
_EmailWarning_ObjectIdentity = ObjectIdentity
emailWarning = _EmailWarning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 11)
)
_EmailService_ObjectIdentity = ObjectIdentity
emailService = _EmailService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 11, 1)
)
_EmailWarningMailServer_Type = DisplayString
_EmailWarningMailServer_Object = MibScalar
emailWarningMailServer = _EmailWarningMailServer_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 11, 1, 1),
    _EmailWarningMailServer_Type()
)
emailWarningMailServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailWarningMailServer.setStatus("current")
_EmailWarningFirstEmailAddr_Type = DisplayString
_EmailWarningFirstEmailAddr_Object = MibScalar
emailWarningFirstEmailAddr = _EmailWarningFirstEmailAddr_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 11, 1, 2),
    _EmailWarningFirstEmailAddr_Type()
)
emailWarningFirstEmailAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailWarningFirstEmailAddr.setStatus("current")
_EmailWarningSecondEmailAddr_Type = DisplayString
_EmailWarningSecondEmailAddr_Object = MibScalar
emailWarningSecondEmailAddr = _EmailWarningSecondEmailAddr_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 11, 1, 3),
    _EmailWarningSecondEmailAddr_Type()
)
emailWarningSecondEmailAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailWarningSecondEmailAddr.setStatus("current")
_EmailWarningThirdEmailAddr_Type = DisplayString
_EmailWarningThirdEmailAddr_Object = MibScalar
emailWarningThirdEmailAddr = _EmailWarningThirdEmailAddr_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 11, 1, 4),
    _EmailWarningThirdEmailAddr_Type()
)
emailWarningThirdEmailAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailWarningThirdEmailAddr.setStatus("current")
_EmailWarningFourthEmailAddr_Type = DisplayString
_EmailWarningFourthEmailAddr_Object = MibScalar
emailWarningFourthEmailAddr = _EmailWarningFourthEmailAddr_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 11, 1, 5),
    _EmailWarningFourthEmailAddr_Type()
)
emailWarningFourthEmailAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailWarningFourthEmailAddr.setStatus("current")


class _EmailWarningSMTPPort_Type(Integer32):
    """Custom type emailWarningSMTPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_EmailWarningSMTPPort_Type.__name__ = "Integer32"
_EmailWarningSMTPPort_Object = MibScalar
emailWarningSMTPPort = _EmailWarningSMTPPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 11, 1, 6),
    _EmailWarningSMTPPort_Type()
)
emailWarningSMTPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailWarningSMTPPort.setStatus("current")
_SetDeviceIp_ObjectIdentity = ObjectIdentity
setDeviceIp = _SetDeviceIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 12)
)
_SetDevIpTable_Object = MibTable
setDevIpTable = _SetDevIpTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 12, 1)
)
if mibBuilder.loadTexts:
    setDevIpTable.setStatus("current")
_SetDevIpEntry_Object = MibTableRow
setDevIpEntry = _SetDevIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 12, 1, 1)
)
setDevIpEntry.setIndexNames(
    (0, "MOXA-IKS6726A-MIB", "setDevIpIndex"),
)
if mibBuilder.loadTexts:
    setDevIpEntry.setStatus("current")
_SetDevIpIndex_Type = Integer32
_SetDevIpIndex_Object = MibTableColumn
setDevIpIndex = _SetDevIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 12, 1, 1, 1),
    _SetDevIpIndex_Type()
)
setDevIpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setDevIpIndex.setStatus("current")
_SetDevIpCurrentIpofDevice_Type = DisplayString
_SetDevIpCurrentIpofDevice_Object = MibTableColumn
setDevIpCurrentIpofDevice = _SetDevIpCurrentIpofDevice_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 12, 1, 1, 2),
    _SetDevIpCurrentIpofDevice_Type()
)
setDevIpCurrentIpofDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setDevIpCurrentIpofDevice.setStatus("current")


class _SetDevIpPresentBy_Type(Integer32):
    """Custom type setDevIpPresentBy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("bootp", 4),
          ("dhcpClient", 1),
          ("no", 0),
          ("rarp", 2))
    )


_SetDevIpPresentBy_Type.__name__ = "Integer32"
_SetDevIpPresentBy_Object = MibTableColumn
setDevIpPresentBy = _SetDevIpPresentBy_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 12, 1, 1, 3),
    _SetDevIpPresentBy_Type()
)
setDevIpPresentBy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    setDevIpPresentBy.setStatus("current")
_SetDevIpDedicatedIp_Type = IpAddress
_SetDevIpDedicatedIp_Object = MibTableColumn
setDevIpDedicatedIp = _SetDevIpDedicatedIp_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 12, 1, 1, 4),
    _SetDevIpDedicatedIp_Type()
)
setDevIpDedicatedIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    setDevIpDedicatedIp.setStatus("current")
_Mirroring_ObjectIdentity = ObjectIdentity
mirroring = _Mirroring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 13)
)
_TargetPort_Type = Integer32
_TargetPort_Object = MibScalar
targetPort = _TargetPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 13, 1),
    _TargetPort_Type()
)
targetPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    targetPort.setStatus("current")
_MirroringPort_Type = Integer32
_MirroringPort_Object = MibScalar
mirroringPort = _MirroringPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 13, 2),
    _MirroringPort_Type()
)
mirroringPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mirroringPort.setStatus("current")


class _MonitorDirection_Type(Integer32):
    """Custom type monitorDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("biDirectional", 2),
          ("inputDataStream", 0),
          ("outputDataStream", 1))
    )


_MonitorDirection_Type.__name__ = "Integer32"
_MonitorDirection_Object = MibScalar
monitorDirection = _MonitorDirection_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 13, 3),
    _MonitorDirection_Type()
)
monitorDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    monitorDirection.setStatus("current")
_PortTrunking_ObjectIdentity = ObjectIdentity
portTrunking = _PortTrunking_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 14)
)
_TrunkSettingTable_Object = MibTable
trunkSettingTable = _TrunkSettingTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 14, 1)
)
if mibBuilder.loadTexts:
    trunkSettingTable.setStatus("current")
_TrunkSettingEntry_Object = MibTableRow
trunkSettingEntry = _TrunkSettingEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 14, 1, 1)
)
trunkSettingEntry.setIndexNames(
    (0, "MOXA-IKS6726A-MIB", "trunkSettingIndex"),
)
if mibBuilder.loadTexts:
    trunkSettingEntry.setStatus("current")
_TrunkSettingIndex_Type = Integer32
_TrunkSettingIndex_Object = MibTableColumn
trunkSettingIndex = _TrunkSettingIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 14, 1, 1, 1),
    _TrunkSettingIndex_Type()
)
trunkSettingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkSettingIndex.setStatus("current")


class _TrunkType_Type(Integer32):
    """Custom type trunkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lacp", 2),
          ("static", 1))
    )


_TrunkType_Type.__name__ = "Integer32"
_TrunkType_Object = MibTableColumn
trunkType = _TrunkType_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 14, 1, 1, 2),
    _TrunkType_Type()
)
trunkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trunkType.setStatus("current")
_TrunkMemberPorts_Type = PortList
_TrunkMemberPorts_Object = MibTableColumn
trunkMemberPorts = _TrunkMemberPorts_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 14, 1, 1, 3),
    _TrunkMemberPorts_Type()
)
trunkMemberPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trunkMemberPorts.setStatus("current")
_TrunkTable_Object = MibTable
trunkTable = _TrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 14, 2)
)
if mibBuilder.loadTexts:
    trunkTable.setStatus("current")
_TrunkEntry_Object = MibTableRow
trunkEntry = _TrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 14, 2, 1)
)
trunkEntry.setIndexNames(
    (0, "MOXA-IKS6726A-MIB", "trunkIndex"),
    (0, "MOXA-IKS6726A-MIB", "trunkPort"),
)
if mibBuilder.loadTexts:
    trunkEntry.setStatus("current")
_TrunkIndex_Type = Integer32
_TrunkIndex_Object = MibTableColumn
trunkIndex = _TrunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 14, 2, 1, 1),
    _TrunkIndex_Type()
)
trunkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkIndex.setStatus("current")
_TrunkPort_Type = Integer32
_TrunkPort_Object = MibTableColumn
trunkPort = _TrunkPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 14, 2, 1, 2),
    _TrunkPort_Type()
)
trunkPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkPort.setStatus("current")


class _TrunkStatus_Type(Integer32):
    """Custom type trunkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fail", 2),
          ("standby", 3),
          ("success", 1))
    )


_TrunkStatus_Type.__name__ = "Integer32"
_TrunkStatus_Object = MibTableColumn
trunkStatus = _TrunkStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 14, 2, 1, 3),
    _TrunkStatus_Type()
)
trunkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkStatus.setStatus("current")
_CommRedundancy_ObjectIdentity = ObjectIdentity
commRedundancy = _CommRedundancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 16)
)


class _ProtocolOfRedundancySetup_Type(Integer32):
    """Custom type protocolOfRedundancySetup based on Integer32"""
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
        *(("mstp", 5),
          ("spanningTree", 1),
          ("turboChain", 4),
          ("turboRing", 2),
          ("turboRingV2", 3))
    )


_ProtocolOfRedundancySetup_Type.__name__ = "Integer32"
_ProtocolOfRedundancySetup_Object = MibScalar
protocolOfRedundancySetup = _ProtocolOfRedundancySetup_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 16, 1),
    _ProtocolOfRedundancySetup_Type()
)
protocolOfRedundancySetup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    protocolOfRedundancySetup.setStatus("current")
_TurboRing_ObjectIdentity = ObjectIdentity
turboRing = _TurboRing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 16, 2)
)


class _TurboRingMaster_Type(Integer32):
    """Custom type turboRingMaster based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_TurboRingMaster_Type.__name__ = "Integer32"
_TurboRingMaster_Object = MibScalar
turboRingMaster = _TurboRingMaster_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 16, 2, 1),
    _TurboRingMaster_Type()
)
turboRingMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    turboRingMaster.setStatus("current")


class _TurboRingMasterSetup_Type(Integer32):
    """Custom type turboRingMasterSetup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_TurboRingMasterSetup_Type.__name__ = "Integer32"
_TurboRingMasterSetup_Object = MibScalar
turboRingMasterSetup = _TurboRingMasterSetup_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 16, 2, 2),
    _TurboRingMasterSetup_Type()
)
turboRingMasterSetup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRingMasterSetup.setStatus("current")
_TurboRingPortTable_Object = MibTable
turboRingPortTable = _TurboRingPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 16, 2, 3)
)
if mibBuilder.loadTexts:
    turboRingPortTable.setStatus("current")
_TurboRingPortEntry_Object = MibTableRow
turboRingPortEntry = _TurboRingPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 16, 2, 3, 1)
)
turboRingPortEntry.setIndexNames(
    (0, "MOXA-IKS6726A-MIB", "turboRingPortIndex"),
)
if mibBuilder.loadTexts:
    turboRingPortEntry.setStatus("current")
_TurboRingPortIndex_Type = Integer32
_TurboRingPortIndex_Object = MibTableColumn
turboRingPortIndex = _TurboRingPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 16, 2, 3, 1, 1),
    _TurboRingPortIndex_Type()
)
turboRingPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    turboRingPortIndex.setStatus("current")


class _TurboRingPortStatus_Type(Integer32):
    """Custom type turboRingPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("blocked", 3),
          ("forwarding", 5),
          ("learning", 4),
          ("linkDown", 2),
          ("notTurboRingPort", 1),
          ("portDisabled", 0))
    )


_TurboRingPortStatus_Type.__name__ = "Integer32"
_TurboRingPortStatus_Object = MibTableColumn
turboRingPortStatus = _TurboRingPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 16, 2, 3, 1, 2),
    _TurboRingPortStatus_Type()
)
turboRingPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    turboRingPortStatus.setStatus("current")
_TurboRingPortDesignatedBridge_Type = MacAddress
_TurboRingPortDesignatedBridge_Object = MibTableColumn
turboRingPortDesignatedBridge = _TurboRingPortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 16, 2, 3, 1, 3),
    _TurboRingPortDesignatedBridge_Type()
)
turboRingPortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    turboRingPortDesignatedBridge.setStatus("current")
_TurboRingPortDesignatedPort_Type = Integer32
_TurboRingPortDesignatedPort_Object = MibTableColumn
turboRingPortDesignatedPort = _TurboRingPortDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 16, 2, 3, 1, 4),
    _TurboRingPortDesignatedPort_Type()
)
turboRingPortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    turboRingPortDesignatedPort.setStatus("current")
_TurboRingDesignatedMaster_Type = MacAddress
_TurboRingDesignatedMaster_Object = MibScalar
turboRingDesignatedMaster = _TurboRingDesignatedMaster_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 16, 2, 6),
    _TurboRingDesignatedMaster_Type()
)
turboRingDesignatedMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    turboRingDesignatedMaster.setStatus("current")
_TurboRingRdntPort1_Type = Integer32
_TurboRingRdntPort1_Object = MibScalar
turboRingRdntPort1 = _TurboRingRdntPort1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 16, 2, 7),
    _TurboRingRdntPort1_Type()
)
turboRingRdntPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRingRdntPort1.setStatus("current")
_TurboRingRdntPort2_Type = Integer32
_TurboRingRdntPort2_Object = MibScalar
turboRingRdntPort2 = _TurboRingRdntPort2_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 16, 2, 8),
    _TurboRingRdntPort2_Type()
)
turboRingRdntPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRingRdntPort2.setStatus("current")


class _TurboRingEnableCoupling_Type(Integer32):
    """Custom type turboRingEnableCoupling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TurboRingEnableCoupling_Type.__name__ = "Integer32"
_TurboRingEnableCoupling_Object = MibScalar
turboRingEnableCoupling = _TurboRingEnableCoupling_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 16, 2, 9),
    _TurboRingEnableCoupling_Type()
)
turboRingEnableCoupling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRingEnableCoupling.setStatus("current")
_TurboRingCouplingPort_Type = Integer32
_TurboRingCouplingPort_Object = MibScalar
turboRingCouplingPort = _TurboRingCouplingPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 16, 2, 10),
    _TurboRingCouplingPort_Type()
)
turboRingCouplingPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRingCouplingPort.setStatus("current")


class _TurboRingCouplingPortStatus_Type(Integer32):
    """Custom type turboRingCouplingPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("blocked", 3),
          ("forwarding", 5),
          ("linkDown", 2),
          ("notCouplingPort", 1),
          ("portDisabled", 0))
    )


_TurboRingCouplingPortStatus_Type.__name__ = "Integer32"
_TurboRingCouplingPortStatus_Object = MibScalar
turboRingCouplingPortStatus = _TurboRingCouplingPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 16, 2, 11),
    _TurboRingCouplingPortStatus_Type()
)
turboRingCouplingPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    turboRingCouplingPortStatus.setStatus("current")
_TurboRingControlPort_Type = Integer32
_TurboRingControlPort_Object = MibScalar
turboRingControlPort = _TurboRingControlPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 16, 2, 12),
    _TurboRingControlPort_Type()
)
turboRingControlPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboRingControlPort.setStatus("current")


class _TurboRingControlPortStatus_Type(Integer32):
    """Custom type turboRingControlPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("active", 7),
          ("blocked", 3),
          ("forwarding", 5),
          ("inactive", 6),
          ("linkDown", 2),
          ("notControlPort", 1),
          ("portDisabled", 0))
    )


_TurboRingControlPortStatus_Type.__name__ = "Integer32"
_TurboRingControlPortStatus_Object = MibScalar
turboRingControlPortStatus = _TurboRingControlPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 16, 2, 13),
    _TurboRingControlPortStatus_Type()
)
turboRingControlPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    turboRingControlPortStatus.setStatus("current")


class _TurboRingBrokenStatus_Type(Integer32):
    """Custom type turboRingBrokenStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("broken", 2),
          ("na", 0),
          ("normal", 1))
    )


_TurboRingBrokenStatus_Type.__name__ = "Integer32"
_TurboRingBrokenStatus_Object = MibScalar
turboRingBrokenStatus = _TurboRingBrokenStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 16, 2, 14),
    _TurboRingBrokenStatus_Type()
)
turboRingBrokenStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    turboRingBrokenStatus.setStatus("current")
_SpanningTree_ObjectIdentity = ObjectIdentity
spanningTree = _SpanningTree_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 16, 3)
)


class _SpanningTreeRoot_Type(Integer32):
    """Custom type spanningTreeRoot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_SpanningTreeRoot_Type.__name__ = "Integer32"
_SpanningTreeRoot_Object = MibScalar
spanningTreeRoot = _SpanningTreeRoot_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 16, 3, 1),
    _SpanningTreeRoot_Type()
)
spanningTreeRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spanningTreeRoot.setStatus("current")


class _SpanningTreeBridgePriority_Type(Integer32):
    """Custom type spanningTreeBridgePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              4096,
              8192,
              12288,
              16384,
              20480,
              24576,
              28672,
              32768,
              36864,
              40960,
              45056,
              49152,
              53248,
              57344,
              61440)
        )
    )
    namedValues = NamedValues(
        *(("priority0", 0),
          ("priority12288", 12288),
          ("priority16384", 16384),
          ("priority20480", 20480),
          ("priority24576", 24576),
          ("priority28672", 28672),
          ("priority32768", 32768),
          ("priority36864", 36864),
          ("priority4096", 4096),
          ("priority40960", 40960),
          ("priority45056", 45056),
          ("priority49152", 49152),
          ("priority53248", 53248),
          ("priority57344", 57344),
          ("priority61440", 61440),
          ("priority8192", 8192))
    )


_SpanningTreeBridgePriority_Type.__name__ = "Integer32"
_SpanningTreeBridgePriority_Object = MibScalar
spanningTreeBridgePriority = _SpanningTreeBridgePriority_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 16, 3, 2),
    _SpanningTreeBridgePriority_Type()
)
spanningTreeBridgePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spanningTreeBridgePriority.setStatus("current")
_SpanningTreeHelloTime_Type = Integer32
_SpanningTreeHelloTime_Object = MibScalar
spanningTreeHelloTime = _SpanningTreeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 16, 3, 3),
    _SpanningTreeHelloTime_Type()
)
spanningTreeHelloTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spanningTreeHelloTime.setStatus("current")
_SpanningTreeMaxAge_Type = Integer32
_SpanningTreeMaxAge_Object = MibScalar
spanningTreeMaxAge = _SpanningTreeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 16, 3, 4),
    _SpanningTreeMaxAge_Type()
)
spanningTreeMaxAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spanningTreeMaxAge.setStatus("current")
_SpanningTreeForwardingDelay_Type = Integer32
_SpanningTreeForwardingDelay_Object = MibScalar
spanningTreeForwardingDelay = _SpanningTreeForwardingDelay_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 16, 3, 5),
    _SpanningTreeForwardingDelay_Type()
)
spanningTreeForwardingDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spanningTreeForwardingDelay.setStatus("current")
_SpanningTreeTable_Object = MibTable
spanningTreeTable = _SpanningTreeTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 16, 3, 6)
)
if mibBuilder.loadTexts:
    spanningTreeTable.setStatus("current")
_SpanningTreeEntry_Object = MibTableRow
spanningTreeEntry = _SpanningTreeEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 16, 3, 6, 1)
)
spanningTreeEntry.setIndexNames(
    (0, "MOXA-IKS6726A-MIB", "spanningTreeIndex"),
)
if mibBuilder.loadTexts:
    spanningTreeEntry.setStatus("current")
_SpanningTreeIndex_Type = Integer32
_SpanningTreeIndex_Object = MibTableColumn
spanningTreeIndex = _SpanningTreeIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 16, 3, 6, 1, 1),
    _SpanningTreeIndex_Type()
)
spanningTreeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spanningTreeIndex.setStatus("current")


class _EnableSpanningTree_Type(Integer32):
    """Custom type enableSpanningTree based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_EnableSpanningTree_Type.__name__ = "Integer32"
_EnableSpanningTree_Object = MibTableColumn
enableSpanningTree = _EnableSpanningTree_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 16, 3, 6, 1, 2),
    _EnableSpanningTree_Type()
)
enableSpanningTree.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableSpanningTree.setStatus("current")


class _SpanningTreePortPriority_Type(Integer32):
    """Custom type spanningTreePortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              16,
              32,
              48,
              64,
              80,
              96,
              112,
              128,
              144,
              160,
              176,
              192,
              208,
              224,
              240)
        )
    )
    namedValues = NamedValues(
        *(("priority0", 0),
          ("priority112", 112),
          ("priority128", 128),
          ("priority144", 144),
          ("priority16", 16),
          ("priority160", 160),
          ("priority176", 176),
          ("priority192", 192),
          ("priority208", 208),
          ("priority224", 224),
          ("priority240", 240),
          ("priority32", 32),
          ("priority48", 48),
          ("priority64", 64),
          ("priority80", 80),
          ("priority96", 96))
    )


_SpanningTreePortPriority_Type.__name__ = "Integer32"
_SpanningTreePortPriority_Object = MibTableColumn
spanningTreePortPriority = _SpanningTreePortPriority_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 16, 3, 6, 1, 3),
    _SpanningTreePortPriority_Type()
)
spanningTreePortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spanningTreePortPriority.setStatus("current")
_SpanningTreePortCost_Type = Integer32
_SpanningTreePortCost_Object = MibTableColumn
spanningTreePortCost = _SpanningTreePortCost_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 16, 3, 6, 1, 4),
    _SpanningTreePortCost_Type()
)
spanningTreePortCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spanningTreePortCost.setStatus("current")


class _SpanningTreePortStatus_Type(Integer32):
    """Custom type spanningTreePortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("blocked", 3),
          ("forwarding", 5),
          ("learning", 4),
          ("linkDown", 2),
          ("notSpanningTreePort", 1),
          ("portDisabled", 0))
    )


_SpanningTreePortStatus_Type.__name__ = "Integer32"
_SpanningTreePortStatus_Object = MibTableColumn
spanningTreePortStatus = _SpanningTreePortStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 16, 3, 6, 1, 5),
    _SpanningTreePortStatus_Type()
)
spanningTreePortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spanningTreePortStatus.setStatus("current")


class _SpanningTreePortEdge_Type(Integer32):
    """Custom type spanningTreePortEdge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("false", 2),
          ("forceEdge", 1))
    )


_SpanningTreePortEdge_Type.__name__ = "Integer32"
_SpanningTreePortEdge_Object = MibTableColumn
spanningTreePortEdge = _SpanningTreePortEdge_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 16, 3, 6, 1, 6),
    _SpanningTreePortEdge_Type()
)
spanningTreePortEdge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    spanningTreePortEdge.setStatus("current")


class _ActiveProtocolOfRedundancy_Type(Integer32):
    """Custom type activeProtocolOfRedundancy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("mstp", 5),
          ("none", 0),
          ("spanningTree", 1),
          ("turboChain", 4),
          ("turboRing", 2),
          ("turboRingV2", 3))
    )


_ActiveProtocolOfRedundancy_Type.__name__ = "Integer32"
_ActiveProtocolOfRedundancy_Object = MibScalar
activeProtocolOfRedundancy = _ActiveProtocolOfRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 16, 4),
    _ActiveProtocolOfRedundancy_Type()
)
activeProtocolOfRedundancy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    activeProtocolOfRedundancy.setStatus("current")
_TurboRingV2_ObjectIdentity = ObjectIdentity
turboRingV2 = _TurboRingV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 16, 5)
)
_TurboRingV2Ring1_ObjectIdentity = ObjectIdentity
turboRingV2Ring1 = _TurboRingV2Ring1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 16, 5, 1)
)


class _RingIndexRing1_Type(Integer32):
    """Custom type ringIndexRing1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_RingIndexRing1_Type.__name__ = "Integer32"
_RingIndexRing1_Object = MibScalar
ringIndexRing1 = _RingIndexRing1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 16, 5, 1, 1),
    _RingIndexRing1_Type()
)
ringIndexRing1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringIndexRing1.setStatus("current")


class _RingEnableRing1_Type(Integer32):
    """Custom type ringEnableRing1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RingEnableRing1_Type.__name__ = "Integer32"
_RingEnableRing1_Object = MibScalar
ringEnableRing1 = _RingEnableRing1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 16, 5, 1, 2),
    _RingEnableRing1_Type()
)
ringEnableRing1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringEnableRing1.setStatus("current")


class _MasterSetupRing1_Type(Integer32):
    """Custom type masterSetupRing1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_MasterSetupRing1_Type.__name__ = "Integer32"
_MasterSetupRing1_Object = MibScalar
masterSetupRing1 = _MasterSetupRing1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 16, 5, 1, 3),
    _MasterSetupRing1_Type()
)
masterSetupRing1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    masterSetupRing1.setStatus("current")


class _MasterStatusRing1_Type(Integer32):
    """Custom type masterStatusRing1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_MasterStatusRing1_Type.__name__ = "Integer32"
_MasterStatusRing1_Object = MibScalar
masterStatusRing1 = _MasterStatusRing1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 16, 5, 1, 4),
    _MasterStatusRing1_Type()
)
masterStatusRing1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    masterStatusRing1.setStatus("current")
_DesignatedMasterRing1_Type = MacAddress
_DesignatedMasterRing1_Object = MibScalar
designatedMasterRing1 = _DesignatedMasterRing1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 16, 5, 1, 5),
    _DesignatedMasterRing1_Type()
)
designatedMasterRing1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    designatedMasterRing1.setStatus("current")
_Rdnt1stPortRing1_Type = Integer32
_Rdnt1stPortRing1_Object = MibScalar
rdnt1stPortRing1 = _Rdnt1stPortRing1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 16, 5, 1, 6),
    _Rdnt1stPortRing1_Type()
)
rdnt1stPortRing1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdnt1stPortRing1.setStatus("current")


class _Rdnt1stPortStatusRing1_Type(Integer32):
    """Custom type rdnt1stPortStatusRing1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("blocking", 3),
          ("disabled", 0),
          ("forwarding", 5),
          ("learning", 4),
          ("linkdown", 2),
          ("notRedundant", 1))
    )


_Rdnt1stPortStatusRing1_Type.__name__ = "Integer32"
_Rdnt1stPortStatusRing1_Object = MibScalar
rdnt1stPortStatusRing1 = _Rdnt1stPortStatusRing1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 16, 5, 1, 7),
    _Rdnt1stPortStatusRing1_Type()
)
rdnt1stPortStatusRing1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnt1stPortStatusRing1.setStatus("current")
_Rdnt2ndPortRing1_Type = Integer32
_Rdnt2ndPortRing1_Object = MibScalar
rdnt2ndPortRing1 = _Rdnt2ndPortRing1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 16, 5, 1, 8),
    _Rdnt2ndPortRing1_Type()
)
rdnt2ndPortRing1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdnt2ndPortRing1.setStatus("current")


class _Rdnt2ndPortStatusRing1_Type(Integer32):
    """Custom type rdnt2ndPortStatusRing1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("blocking", 3),
          ("disabled", 0),
          ("forwarding", 5),
          ("learning", 4),
          ("linkdown", 2),
          ("notRedundant", 1))
    )


_Rdnt2ndPortStatusRing1_Type.__name__ = "Integer32"
_Rdnt2ndPortStatusRing1_Object = MibScalar
rdnt2ndPortStatusRing1 = _Rdnt2ndPortStatusRing1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 16, 5, 1, 9),
    _Rdnt2ndPortStatusRing1_Type()
)
rdnt2ndPortStatusRing1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnt2ndPortStatusRing1.setStatus("current")


class _BrokenStatusRing1_Type(Integer32):
    """Custom type brokenStatusRing1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("broken", 2),
          ("na", 0),
          ("normal", 1))
    )


_BrokenStatusRing1_Type.__name__ = "Integer32"
_BrokenStatusRing1_Object = MibScalar
brokenStatusRing1 = _BrokenStatusRing1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 16, 5, 1, 10),
    _BrokenStatusRing1_Type()
)
brokenStatusRing1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brokenStatusRing1.setStatus("current")
_TurboRingV2Ring2_ObjectIdentity = ObjectIdentity
turboRingV2Ring2 = _TurboRingV2Ring2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 16, 5, 2)
)


class _RingIndexRing2_Type(Integer32):
    """Custom type ringIndexRing2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_RingIndexRing2_Type.__name__ = "Integer32"
_RingIndexRing2_Object = MibScalar
ringIndexRing2 = _RingIndexRing2_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 16, 5, 2, 1),
    _RingIndexRing2_Type()
)
ringIndexRing2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ringIndexRing2.setStatus("current")


class _RingEnableRing2_Type(Integer32):
    """Custom type ringEnableRing2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RingEnableRing2_Type.__name__ = "Integer32"
_RingEnableRing2_Object = MibScalar
ringEnableRing2 = _RingEnableRing2_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 16, 5, 2, 2),
    _RingEnableRing2_Type()
)
ringEnableRing2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ringEnableRing2.setStatus("current")


class _MasterSetupRing2_Type(Integer32):
    """Custom type masterSetupRing2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_MasterSetupRing2_Type.__name__ = "Integer32"
_MasterSetupRing2_Object = MibScalar
masterSetupRing2 = _MasterSetupRing2_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 16, 5, 2, 3),
    _MasterSetupRing2_Type()
)
masterSetupRing2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    masterSetupRing2.setStatus("current")


class _MasterStatusRing2_Type(Integer32):
    """Custom type masterStatusRing2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_MasterStatusRing2_Type.__name__ = "Integer32"
_MasterStatusRing2_Object = MibScalar
masterStatusRing2 = _MasterStatusRing2_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 16, 5, 2, 4),
    _MasterStatusRing2_Type()
)
masterStatusRing2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    masterStatusRing2.setStatus("current")
_DesignatedMasterRing2_Type = MacAddress
_DesignatedMasterRing2_Object = MibScalar
designatedMasterRing2 = _DesignatedMasterRing2_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 16, 5, 2, 5),
    _DesignatedMasterRing2_Type()
)
designatedMasterRing2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    designatedMasterRing2.setStatus("current")
_Rdnt1stPortRing2_Type = Integer32
_Rdnt1stPortRing2_Object = MibScalar
rdnt1stPortRing2 = _Rdnt1stPortRing2_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 16, 5, 2, 6),
    _Rdnt1stPortRing2_Type()
)
rdnt1stPortRing2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdnt1stPortRing2.setStatus("current")


class _Rdnt1stPortStatusRing2_Type(Integer32):
    """Custom type rdnt1stPortStatusRing2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("blocking", 3),
          ("disabled", 0),
          ("forwarding", 5),
          ("learning", 4),
          ("linkdown", 2),
          ("notRedundant", 1))
    )


_Rdnt1stPortStatusRing2_Type.__name__ = "Integer32"
_Rdnt1stPortStatusRing2_Object = MibScalar
rdnt1stPortStatusRing2 = _Rdnt1stPortStatusRing2_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 16, 5, 2, 7),
    _Rdnt1stPortStatusRing2_Type()
)
rdnt1stPortStatusRing2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnt1stPortStatusRing2.setStatus("current")
_Rdnt2ndPortRing2_Type = Integer32
_Rdnt2ndPortRing2_Object = MibScalar
rdnt2ndPortRing2 = _Rdnt2ndPortRing2_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 16, 5, 2, 8),
    _Rdnt2ndPortRing2_Type()
)
rdnt2ndPortRing2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rdnt2ndPortRing2.setStatus("current")


class _Rdnt2ndPortStatusRing2_Type(Integer32):
    """Custom type rdnt2ndPortStatusRing2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("blocking", 3),
          ("disabled", 0),
          ("forwarding", 5),
          ("learning", 4),
          ("linkdown", 2),
          ("notRedundant", 1))
    )


_Rdnt2ndPortStatusRing2_Type.__name__ = "Integer32"
_Rdnt2ndPortStatusRing2_Object = MibScalar
rdnt2ndPortStatusRing2 = _Rdnt2ndPortStatusRing2_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 16, 5, 2, 9),
    _Rdnt2ndPortStatusRing2_Type()
)
rdnt2ndPortStatusRing2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rdnt2ndPortStatusRing2.setStatus("current")


class _BrokenStatusRing2_Type(Integer32):
    """Custom type brokenStatusRing2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("broken", 2),
          ("na", 0),
          ("normal", 1))
    )


_BrokenStatusRing2_Type.__name__ = "Integer32"
_BrokenStatusRing2_Object = MibScalar
brokenStatusRing2 = _BrokenStatusRing2_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 16, 5, 2, 10),
    _BrokenStatusRing2_Type()
)
brokenStatusRing2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brokenStatusRing2.setStatus("current")
_TurboRingV2Coupling_ObjectIdentity = ObjectIdentity
turboRingV2Coupling = _TurboRingV2Coupling_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 16, 5, 3)
)


class _CouplingEnable_Type(Integer32):
    """Custom type couplingEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_CouplingEnable_Type.__name__ = "Integer32"
_CouplingEnable_Object = MibScalar
couplingEnable = _CouplingEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 16, 5, 3, 1),
    _CouplingEnable_Type()
)
couplingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    couplingEnable.setStatus("current")


class _CouplingMode_Type(Integer32):
    """Custom type couplingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("couplingBackup", 2),
          ("couplingPrimary", 3),
          ("dualHoming", 1))
    )


_CouplingMode_Type.__name__ = "Integer32"
_CouplingMode_Object = MibScalar
couplingMode = _CouplingMode_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 16, 5, 3, 2),
    _CouplingMode_Type()
)
couplingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    couplingMode.setStatus("current")
_Coupling1stPort_Type = Integer32
_Coupling1stPort_Object = MibScalar
coupling1stPort = _Coupling1stPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 16, 5, 3, 3),
    _Coupling1stPort_Type()
)
coupling1stPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coupling1stPort.setStatus("current")


class _Coupling1stPortStatus_Type(Integer32):
    """Custom type coupling1stPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("blocking", 3),
          ("disabled", 0),
          ("forwarding", 5),
          ("learning", 4),
          ("linkdown", 2),
          ("notRedundant", 1))
    )


_Coupling1stPortStatus_Type.__name__ = "Integer32"
_Coupling1stPortStatus_Object = MibScalar
coupling1stPortStatus = _Coupling1stPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 16, 5, 3, 4),
    _Coupling1stPortStatus_Type()
)
coupling1stPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coupling1stPortStatus.setStatus("current")
_Coupling2ndPort_Type = Integer32
_Coupling2ndPort_Object = MibScalar
coupling2ndPort = _Coupling2ndPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 16, 5, 3, 5),
    _Coupling2ndPort_Type()
)
coupling2ndPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    coupling2ndPort.setStatus("current")


class _Coupling2ndPortStatus_Type(Integer32):
    """Custom type coupling2ndPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("blocking", 3),
          ("disabled", 0),
          ("forwarding", 5),
          ("learning", 4),
          ("linkdown", 2),
          ("notRedundant", 1))
    )


_Coupling2ndPortStatus_Type.__name__ = "Integer32"
_Coupling2ndPortStatus_Object = MibScalar
coupling2ndPortStatus = _Coupling2ndPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 16, 5, 3, 6),
    _Coupling2ndPortStatus_Type()
)
coupling2ndPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    coupling2ndPortStatus.setStatus("current")
_TurboChain_ObjectIdentity = ObjectIdentity
turboChain = _TurboChain_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 16, 6)
)


class _TurboChainRole_Type(Integer32):
    """Custom type turboChainRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("head", 1),
          ("member", 2),
          ("tail", 3))
    )


_TurboChainRole_Type.__name__ = "Integer32"
_TurboChainRole_Object = MibScalar
turboChainRole = _TurboChainRole_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 16, 6, 1),
    _TurboChainRole_Type()
)
turboChainRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboChainRole.setStatus("current")
_TurboChainPort1_Type = Integer32
_TurboChainPort1_Object = MibScalar
turboChainPort1 = _TurboChainPort1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 16, 6, 2),
    _TurboChainPort1_Type()
)
turboChainPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboChainPort1.setStatus("current")
_TurboChainPort2_Type = Integer32
_TurboChainPort2_Object = MibScalar
turboChainPort2 = _TurboChainPort2_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 16, 6, 3),
    _TurboChainPort2_Type()
)
turboChainPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    turboChainPort2.setStatus("current")


class _TurboChainPort1Status_Type(Integer32):
    """Custom type turboChainPort1Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("blocked", 3),
          ("blocking", 2),
          ("forwarding", 4),
          ("linkDown", 1),
          ("na", 5),
          ("notTurboChainPort", 0))
    )


_TurboChainPort1Status_Type.__name__ = "Integer32"
_TurboChainPort1Status_Object = MibScalar
turboChainPort1Status = _TurboChainPort1Status_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 16, 6, 4),
    _TurboChainPort1Status_Type()
)
turboChainPort1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    turboChainPort1Status.setStatus("current")


class _TurboChainPort2Status_Type(Integer32):
    """Custom type turboChainPort2Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("blocked", 3),
          ("blocking", 2),
          ("forwarding", 4),
          ("linkDown", 1),
          ("na", 5),
          ("notTurboChainPort", 0))
    )


_TurboChainPort2Status_Type.__name__ = "Integer32"
_TurboChainPort2Status_Object = MibScalar
turboChainPort2Status = _TurboChainPort2Status_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 16, 6, 5),
    _TurboChainPort2Status_Type()
)
turboChainPort2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    turboChainPort2Status.setStatus("current")
_TurboChainPort1PartnerBridge_Type = MacAddress
_TurboChainPort1PartnerBridge_Object = MibScalar
turboChainPort1PartnerBridge = _TurboChainPort1PartnerBridge_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 16, 6, 6),
    _TurboChainPort1PartnerBridge_Type()
)
turboChainPort1PartnerBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    turboChainPort1PartnerBridge.setStatus("current")
_TurboChainPort2PartnerBridge_Type = MacAddress
_TurboChainPort2PartnerBridge_Object = MibScalar
turboChainPort2PartnerBridge = _TurboChainPort2PartnerBridge_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 16, 6, 7),
    _TurboChainPort2PartnerBridge_Type()
)
turboChainPort2PartnerBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    turboChainPort2PartnerBridge.setStatus("current")
_TrafficPrioritization_ObjectIdentity = ObjectIdentity
trafficPrioritization = _TrafficPrioritization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 18)
)
_QosClassification_ObjectIdentity = ObjectIdentity
qosClassification = _QosClassification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 18, 1)
)


class _QueuingMechanism_Type(Integer32):
    """Custom type queuingMechanism based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("schedstrict", 1),
          ("schedweightfair", 0))
    )


_QueuingMechanism_Type.__name__ = "Integer32"
_QueuingMechanism_Object = MibScalar
queuingMechanism = _QueuingMechanism_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 18, 1, 1),
    _QueuingMechanism_Type()
)
queuingMechanism.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    queuingMechanism.setStatus("current")
_QosPortTable_Object = MibTable
qosPortTable = _QosPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 18, 1, 2)
)
if mibBuilder.loadTexts:
    qosPortTable.setStatus("current")
_QosPortEntry_Object = MibTableRow
qosPortEntry = _QosPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 18, 1, 2, 1)
)
qosPortEntry.setIndexNames(
    (0, "MOXA-IKS6726A-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    qosPortEntry.setStatus("current")


class _InspectTos_Type(Integer32):
    """Custom type inspectTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_InspectTos_Type.__name__ = "Integer32"
_InspectTos_Object = MibTableColumn
inspectTos = _InspectTos_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 18, 1, 2, 1, 1),
    _InspectTos_Type()
)
inspectTos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inspectTos.setStatus("current")


class _InspectCos_Type(Integer32):
    """Custom type inspectCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_InspectCos_Type.__name__ = "Integer32"
_InspectCos_Object = MibTableColumn
inspectCos = _InspectCos_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 18, 1, 2, 1, 2),
    _InspectCos_Type()
)
inspectCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    inspectCos.setStatus("current")


class _PortPriority_Type(Integer32):
    """Custom type portPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("priority0", 0),
          ("priority1", 1),
          ("priority2", 2),
          ("priority3", 3),
          ("priority4", 4),
          ("priority5", 5),
          ("priority6", 6),
          ("priority7", 7))
    )


_PortPriority_Type.__name__ = "Integer32"
_PortPriority_Object = MibTableColumn
portPriority = _PortPriority_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 18, 1, 2, 1, 3),
    _PortPriority_Type()
)
portPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portPriority.setStatus("current")
_CosMapping_ObjectIdentity = ObjectIdentity
cosMapping = _CosMapping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 18, 2)
)
_CosMappingTable_Object = MibTable
cosMappingTable = _CosMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 18, 2, 1)
)
if mibBuilder.loadTexts:
    cosMappingTable.setStatus("current")
_CosMappingEntry_Object = MibTableRow
cosMappingEntry = _CosMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 18, 2, 1, 1)
)
cosMappingEntry.setIndexNames(
    (0, "MOXA-IKS6726A-MIB", "cosTag"),
)
if mibBuilder.loadTexts:
    cosMappingEntry.setStatus("current")


class _CosTag_Type(Integer32):
    """Custom type cosTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CosTag_Type.__name__ = "Integer32"
_CosTag_Object = MibTableColumn
cosTag = _CosTag_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 18, 2, 1, 1, 1),
    _CosTag_Type()
)
cosTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cosTag.setStatus("current")


class _CosMappedPriority_Type(Integer32):
    """Custom type cosMappedPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("TrafficClass0", 0),
          ("TrafficClass1", 1),
          ("TrafficClass2", 2),
          ("TrafficClass3", 3))
    )


_CosMappedPriority_Type.__name__ = "Integer32"
_CosMappedPriority_Object = MibTableColumn
cosMappedPriority = _CosMappedPriority_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 18, 2, 1, 1, 2),
    _CosMappedPriority_Type()
)
cosMappedPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cosMappedPriority.setStatus("current")
_TosMapping_ObjectIdentity = ObjectIdentity
tosMapping = _TosMapping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 18, 3)
)
_TosMappingTable_Object = MibTable
tosMappingTable = _TosMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 18, 3, 1)
)
if mibBuilder.loadTexts:
    tosMappingTable.setStatus("current")
_TosMappingEntry_Object = MibTableRow
tosMappingEntry = _TosMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 18, 3, 1, 1)
)
tosMappingEntry.setIndexNames(
    (0, "MOXA-IKS6726A-MIB", "tosClass"),
)
if mibBuilder.loadTexts:
    tosMappingEntry.setStatus("current")
_TosClass_Type = Integer32
_TosClass_Object = MibTableColumn
tosClass = _TosClass_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 18, 3, 1, 1, 1),
    _TosClass_Type()
)
tosClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tosClass.setStatus("current")


class _TosMappedPriority_Type(Integer32):
    """Custom type tosMappedPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("priority0", 0),
          ("priority1", 1),
          ("priority2", 2),
          ("priority3", 3),
          ("priority4", 4),
          ("priority5", 5),
          ("priority6", 6),
          ("priority7", 7))
    )


_TosMappedPriority_Type.__name__ = "Integer32"
_TosMappedPriority_Object = MibTableColumn
tosMappedPriority = _TosMappedPriority_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 18, 3, 1, 1, 2),
    _TosMappedPriority_Type()
)
tosMappedPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tosMappedPriority.setStatus("current")
_Vlan_ObjectIdentity = ObjectIdentity
vlan = _Vlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 19)
)
_VlanPortSettingTable_Object = MibTable
vlanPortSettingTable = _VlanPortSettingTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 19, 1)
)
if mibBuilder.loadTexts:
    vlanPortSettingTable.setStatus("current")
_VlanPortSettingEntry_Object = MibTableRow
vlanPortSettingEntry = _VlanPortSettingEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 19, 1, 1)
)
vlanPortSettingEntry.setIndexNames(
    (0, "MOXA-IKS6726A-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    vlanPortSettingEntry.setStatus("current")


class _PortVlanType_Type(Integer32):
    """Custom type portVlanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("access", 0),
          ("hybrid", 2),
          ("trunk", 1))
    )


_PortVlanType_Type.__name__ = "Integer32"
_PortVlanType_Object = MibTableColumn
portVlanType = _PortVlanType_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 19, 1, 1, 1),
    _PortVlanType_Type()
)
portVlanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portVlanType.setStatus("current")


class _PortDefaultVid_Type(Integer32):
    """Custom type portDefaultVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_PortDefaultVid_Type.__name__ = "Integer32"
_PortDefaultVid_Object = MibTableColumn
portDefaultVid = _PortDefaultVid_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 19, 1, 1, 2),
    _PortDefaultVid_Type()
)
portDefaultVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDefaultVid.setStatus("current")
_PortFixedVid_Type = DisplayString
_PortFixedVid_Object = MibTableColumn
portFixedVid = _PortFixedVid_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 19, 1, 1, 3),
    _PortFixedVid_Type()
)
portFixedVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portFixedVid.setStatus("current")
_PortForbiddenVid_Type = DisplayString
_PortForbiddenVid_Object = MibTableColumn
portForbiddenVid = _PortForbiddenVid_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 19, 1, 1, 4),
    _PortForbiddenVid_Type()
)
portForbiddenVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portForbiddenVid.setStatus("current")
_PortFixedVidUntag_Type = DisplayString
_PortFixedVidUntag_Object = MibTableColumn
portFixedVidUntag = _PortFixedVidUntag_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 19, 1, 1, 5),
    _PortFixedVidUntag_Type()
)
portFixedVidUntag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portFixedVidUntag.setStatus("current")
_VlanTable_Object = MibTable
vlanTable = _VlanTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 19, 2)
)
if mibBuilder.loadTexts:
    vlanTable.setStatus("current")
_VlanEntry_Object = MibTableRow
vlanEntry = _VlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 19, 2, 1)
)
vlanEntry.setIndexNames(
    (0, "MOXA-IKS6726A-MIB", "vlanId"),
)
if mibBuilder.loadTexts:
    vlanEntry.setStatus("current")


class _VlanId_Type(Integer32):
    """Custom type vlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_VlanId_Type.__name__ = "Integer32"
_VlanId_Object = MibTableColumn
vlanId = _VlanId_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 19, 2, 1, 1),
    _VlanId_Type()
)
vlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanId.setStatus("current")
_JoinedAccessPorts_Type = PortList
_JoinedAccessPorts_Object = MibTableColumn
joinedAccessPorts = _JoinedAccessPorts_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 19, 2, 1, 2),
    _JoinedAccessPorts_Type()
)
joinedAccessPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    joinedAccessPorts.setStatus("current")
_JoinedTrunkPorts_Type = PortList
_JoinedTrunkPorts_Object = MibTableColumn
joinedTrunkPorts = _JoinedTrunkPorts_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 19, 2, 1, 3),
    _JoinedTrunkPorts_Type()
)
joinedTrunkPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    joinedTrunkPorts.setStatus("current")
_JoinedHybridPorts_Type = PortList
_JoinedHybridPorts_Object = MibTableColumn
joinedHybridPorts = _JoinedHybridPorts_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 19, 2, 1, 4),
    _JoinedHybridPorts_Type()
)
joinedHybridPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    joinedHybridPorts.setStatus("current")
_ManagementVlanId_Type = Integer32
_ManagementVlanId_Object = MibScalar
managementVlanId = _ManagementVlanId_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 19, 3),
    _ManagementVlanId_Type()
)
managementVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    managementVlanId.setStatus("current")


class _VlanType_Type(Integer32):
    """Custom type vlanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("portBased", 1),
          ("tagBased", 0))
    )


_VlanType_Type.__name__ = "Integer32"
_VlanType_Object = MibScalar
vlanType = _VlanType_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 19, 4),
    _VlanType_Type()
)
vlanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanType.setStatus("current")
_PortbaseVlanSettingTable_Object = MibTable
portbaseVlanSettingTable = _PortbaseVlanSettingTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 19, 5)
)
if mibBuilder.loadTexts:
    portbaseVlanSettingTable.setStatus("current")
_PortbaseVlanSettingEntry_Object = MibTableRow
portbaseVlanSettingEntry = _PortbaseVlanSettingEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 19, 5, 1)
)
portbaseVlanSettingEntry.setIndexNames(
    (0, "MOXA-IKS6726A-MIB", "portbaseVlanSettingIndex"),
)
if mibBuilder.loadTexts:
    portbaseVlanSettingEntry.setStatus("current")
_PortbaseVlanSettingIndex_Type = Integer32
_PortbaseVlanSettingIndex_Object = MibTableColumn
portbaseVlanSettingIndex = _PortbaseVlanSettingIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 19, 5, 1, 1),
    _PortbaseVlanSettingIndex_Type()
)
portbaseVlanSettingIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portbaseVlanSettingIndex.setStatus("current")
_PortbaseVlanMemberPorts_Type = PortList
_PortbaseVlanMemberPorts_Object = MibTableColumn
portbaseVlanMemberPorts = _PortbaseVlanMemberPorts_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 19, 5, 1, 2),
    _PortbaseVlanMemberPorts_Type()
)
portbaseVlanMemberPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portbaseVlanMemberPorts.setStatus("current")


class _EnableGvrp_Type(Integer32):
    """Custom type enableGvrp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_EnableGvrp_Type.__name__ = "Integer32"
_EnableGvrp_Object = MibScalar
enableGvrp = _EnableGvrp_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 19, 6),
    _EnableGvrp_Type()
)
enableGvrp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableGvrp.setStatus("current")
_MulticastFiltering_ObjectIdentity = ObjectIdentity
multicastFiltering = _MulticastFiltering_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 20)
)
_IgmpSnooping_ObjectIdentity = ObjectIdentity
igmpSnooping = _IgmpSnooping_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 20, 1)
)


class _QuerierQueryInterval_Type(Integer32):
    """Custom type querierQueryInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 600),
    )


_QuerierQueryInterval_Type.__name__ = "Integer32"
_QuerierQueryInterval_Object = MibScalar
querierQueryInterval = _QuerierQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 20, 1, 1),
    _QuerierQueryInterval_Type()
)
querierQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    querierQueryInterval.setStatus("current")
_IgmpSnoopingSettingTable_Object = MibTable
igmpSnoopingSettingTable = _IgmpSnoopingSettingTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 20, 1, 2)
)
if mibBuilder.loadTexts:
    igmpSnoopingSettingTable.setStatus("current")
_IgmpSnoopingSettingEntry_Object = MibTableRow
igmpSnoopingSettingEntry = _IgmpSnoopingSettingEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 20, 1, 2, 1)
)
igmpSnoopingSettingEntry.setIndexNames(
    (0, "MOXA-IKS6726A-MIB", "vlanId"),
)
if mibBuilder.loadTexts:
    igmpSnoopingSettingEntry.setStatus("current")


class _EnableIgmpSnooping_Type(Integer32):
    """Custom type enableIgmpSnooping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_EnableIgmpSnooping_Type.__name__ = "Integer32"
_EnableIgmpSnooping_Object = MibTableColumn
enableIgmpSnooping = _EnableIgmpSnooping_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 20, 1, 2, 1, 1),
    _EnableIgmpSnooping_Type()
)
enableIgmpSnooping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableIgmpSnooping.setStatus("current")


class _EnableQuerier_Type(Integer32):
    """Custom type enableQuerier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("igmpv2", 1),
          ("igmpv3", 2))
    )


_EnableQuerier_Type.__name__ = "Integer32"
_EnableQuerier_Object = MibTableColumn
enableQuerier = _EnableQuerier_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 20, 1, 2, 1, 2),
    _EnableQuerier_Type()
)
enableQuerier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableQuerier.setStatus("current")
_FixedMulticastQuerierPorts_Type = PortList
_FixedMulticastQuerierPorts_Object = MibTableColumn
fixedMulticastQuerierPorts = _FixedMulticastQuerierPorts_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 20, 1, 2, 1, 3),
    _FixedMulticastQuerierPorts_Type()
)
fixedMulticastQuerierPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fixedMulticastQuerierPorts.setStatus("current")
_LearnedMulticastQuerierPorts_Type = PortList
_LearnedMulticastQuerierPorts_Object = MibTableColumn
learnedMulticastQuerierPorts = _LearnedMulticastQuerierPorts_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 20, 1, 2, 1, 4),
    _LearnedMulticastQuerierPorts_Type()
)
learnedMulticastQuerierPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    learnedMulticastQuerierPorts.setStatus("current")


class _EnableGlobalIgmpSnooping_Type(Integer32):
    """Custom type enableGlobalIgmpSnooping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_EnableGlobalIgmpSnooping_Type.__name__ = "Integer32"
_EnableGlobalIgmpSnooping_Object = MibScalar
enableGlobalIgmpSnooping = _EnableGlobalIgmpSnooping_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 20, 1, 4),
    _EnableGlobalIgmpSnooping_Type()
)
enableGlobalIgmpSnooping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableGlobalIgmpSnooping.setStatus("current")


class _MulticastFastForwarding_Type(Integer32):
    """Custom type multicastFastForwarding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_MulticastFastForwarding_Type.__name__ = "Integer32"
_MulticastFastForwarding_Object = MibScalar
multicastFastForwarding = _MulticastFastForwarding_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 20, 1, 7),
    _MulticastFastForwarding_Type()
)
multicastFastForwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    multicastFastForwarding.setStatus("current")
_StaticMulticast_ObjectIdentity = ObjectIdentity
staticMulticast = _StaticMulticast_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 20, 2)
)
_StaticMulticastTable_Object = MibTable
staticMulticastTable = _StaticMulticastTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 20, 2, 1)
)
if mibBuilder.loadTexts:
    staticMulticastTable.setStatus("current")
_StaticMulticastEntry_Object = MibTableRow
staticMulticastEntry = _StaticMulticastEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 20, 2, 1, 1)
)
staticMulticastEntry.setIndexNames(
    (0, "MOXA-IKS6726A-MIB", "staticMulticastAddress"),
)
if mibBuilder.loadTexts:
    staticMulticastEntry.setStatus("current")
_StaticMulticastAddress_Type = MacAddress
_StaticMulticastAddress_Object = MibTableColumn
staticMulticastAddress = _StaticMulticastAddress_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 20, 2, 1, 1, 1),
    _StaticMulticastAddress_Type()
)
staticMulticastAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    staticMulticastAddress.setStatus("current")
_StaticMulticastPorts_Type = PortList
_StaticMulticastPorts_Object = MibTableColumn
staticMulticastPorts = _StaticMulticastPorts_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 20, 2, 1, 1, 2),
    _StaticMulticastPorts_Type()
)
staticMulticastPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    staticMulticastPorts.setStatus("current")


class _StaticMulticastStatus_Type(Integer32):
    """Custom type staticMulticastStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6))
    )


_StaticMulticastStatus_Type.__name__ = "Integer32"
_StaticMulticastStatus_Object = MibTableColumn
staticMulticastStatus = _StaticMulticastStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 20, 2, 1, 1, 3),
    _StaticMulticastStatus_Type()
)
staticMulticastStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    staticMulticastStatus.setStatus("current")
_Gmrp_ObjectIdentity = ObjectIdentity
gmrp = _Gmrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 20, 3)
)
_GmrpSettingTable_Object = MibTable
gmrpSettingTable = _GmrpSettingTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 20, 3, 1)
)
if mibBuilder.loadTexts:
    gmrpSettingTable.setStatus("current")
_GmrpSettingEntry_Object = MibTableRow
gmrpSettingEntry = _GmrpSettingEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 20, 3, 1, 1)
)
gmrpSettingEntry.setIndexNames(
    (0, "MOXA-IKS6726A-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    gmrpSettingEntry.setStatus("current")


class _EnableGMRP_Type(Integer32):
    """Custom type enableGMRP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_EnableGMRP_Type.__name__ = "Integer32"
_EnableGMRP_Object = MibTableColumn
enableGMRP = _EnableGMRP_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 20, 3, 1, 1, 1),
    _EnableGMRP_Type()
)
enableGMRP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableGMRP.setStatus("current")
_GmrpTable_Object = MibTable
gmrpTable = _GmrpTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 20, 3, 2)
)
if mibBuilder.loadTexts:
    gmrpTable.setStatus("current")
_GmrpEntry_Object = MibTableRow
gmrpEntry = _GmrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 20, 3, 2, 1)
)
gmrpEntry.setIndexNames(
    (0, "MOXA-IKS6726A-MIB", "gmrpMulticastGroup"),
)
if mibBuilder.loadTexts:
    gmrpEntry.setStatus("current")
_GmrpMulticastGroup_Type = MacAddress
_GmrpMulticastGroup_Object = MibTableColumn
gmrpMulticastGroup = _GmrpMulticastGroup_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 20, 3, 2, 1, 1),
    _GmrpMulticastGroup_Type()
)
gmrpMulticastGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmrpMulticastGroup.setStatus("current")
_GmrpFixedPorts_Type = PortList
_GmrpFixedPorts_Object = MibTableColumn
gmrpFixedPorts = _GmrpFixedPorts_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 20, 3, 2, 1, 2),
    _GmrpFixedPorts_Type()
)
gmrpFixedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmrpFixedPorts.setStatus("current")
_GmrpLearnedPorts_Type = PortList
_GmrpLearnedPorts_Object = MibTableColumn
gmrpLearnedPorts = _GmrpLearnedPorts_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 20, 3, 2, 1, 3),
    _GmrpLearnedPorts_Type()
)
gmrpLearnedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gmrpLearnedPorts.setStatus("current")
_Mfb_ObjectIdentity = ObjectIdentity
mfb = _Mfb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 20, 4)
)
_MfbSettingTable_Object = MibTable
mfbSettingTable = _MfbSettingTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 20, 4, 1)
)
if mibBuilder.loadTexts:
    mfbSettingTable.setStatus("current")
_MfbSettingEntry_Object = MibTableRow
mfbSettingEntry = _MfbSettingEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 20, 4, 1, 1)
)
mfbSettingEntry.setIndexNames(
    (0, "MOXA-IKS6726A-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    mfbSettingEntry.setStatus("current")


class _FilterBehavior_Type(Integer32):
    """Custom type filterBehavior based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("filterUnknown", 3),
          ("forwardUnknown", 2))
    )


_FilterBehavior_Type.__name__ = "Integer32"
_FilterBehavior_Object = MibTableColumn
filterBehavior = _FilterBehavior_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 20, 4, 1, 1, 1),
    _FilterBehavior_Type()
)
filterBehavior.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterBehavior.setStatus("current")
_RateLimiting_ObjectIdentity = ObjectIdentity
rateLimiting = _RateLimiting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 21)
)
_NormalModeRateLimitingTable_Object = MibTable
normalModeRateLimitingTable = _NormalModeRateLimitingTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 21, 1)
)
if mibBuilder.loadTexts:
    normalModeRateLimitingTable.setStatus("current")
_NormalModeRateLimitingEntry_Object = MibTableRow
normalModeRateLimitingEntry = _NormalModeRateLimitingEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 21, 1, 1)
)
normalModeRateLimitingEntry.setIndexNames(
    (0, "MOXA-IKS6726A-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    normalModeRateLimitingEntry.setStatus("current")


class _IngressLimitRate_Type(Integer32):
    """Custom type ingressLimitRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("notlimited", 0),
          ("percentage03", 1),
          ("percentage05", 2),
          ("percentage10", 3),
          ("percentage15", 4),
          ("percentage25", 5),
          ("percentage35", 6),
          ("percentage50", 7),
          ("percentage65", 8),
          ("percentage85", 9))
    )


_IngressLimitRate_Type.__name__ = "Integer32"
_IngressLimitRate_Object = MibTableColumn
ingressLimitRate = _IngressLimitRate_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 21, 1, 1, 1),
    _IngressLimitRate_Type()
)
ingressLimitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ingressLimitRate.setStatus("current")


class _EgressLimit_Type(Integer32):
    """Custom type egressLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("notlimited", 0),
          ("percentage03", 1),
          ("percentage05", 2),
          ("percentage10", 3),
          ("percentage15", 4),
          ("percentage25", 5),
          ("percentage35", 6),
          ("percentage50", 7),
          ("percentage65", 8),
          ("percentage85", 9))
    )


_EgressLimit_Type.__name__ = "Integer32"
_EgressLimit_Object = MibTableColumn
egressLimit = _EgressLimit_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 21, 1, 1, 2),
    _EgressLimit_Type()
)
egressLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    egressLimit.setStatus("current")
_BroadcastStormProtection_ObjectIdentity = ObjectIdentity
broadcastStormProtection = _BroadcastStormProtection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 21, 2)
)


class _EnableBcastStormProtection_Type(Integer32):
    """Custom type enableBcastStormProtection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_EnableBcastStormProtection_Type.__name__ = "Integer32"
_EnableBcastStormProtection_Object = MibScalar
enableBcastStormProtection = _EnableBcastStormProtection_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 21, 2, 1),
    _EnableBcastStormProtection_Type()
)
enableBcastStormProtection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableBcastStormProtection.setStatus("current")


class _BcastStormIncludeMcast_Type(Integer32):
    """Custom type bcastStormIncludeMcast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_BcastStormIncludeMcast_Type.__name__ = "Integer32"
_BcastStormIncludeMcast_Object = MibScalar
bcastStormIncludeMcast = _BcastStormIncludeMcast_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 21, 2, 2),
    _BcastStormIncludeMcast_Type()
)
bcastStormIncludeMcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcastStormIncludeMcast.setStatus("current")


class _BcastStormIncludeUnkonwnMcastUcast_Type(Integer32):
    """Custom type bcastStormIncludeUnkonwnMcastUcast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_BcastStormIncludeUnkonwnMcastUcast_Type.__name__ = "Integer32"
_BcastStormIncludeUnkonwnMcastUcast_Object = MibScalar
bcastStormIncludeUnkonwnMcastUcast = _BcastStormIncludeUnkonwnMcastUcast_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 21, 2, 3),
    _BcastStormIncludeUnkonwnMcastUcast_Type()
)
bcastStormIncludeUnkonwnMcastUcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcastStormIncludeUnkonwnMcastUcast.setStatus("current")
_UnicastFilterBehavior_ObjectIdentity = ObjectIdentity
unicastFilterBehavior = _UnicastFilterBehavior_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 21, 2, 4)
)


class _UfbIncludeUnkonwnUcast_Type(Integer32):
    """Custom type ufbIncludeUnkonwnUcast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_UfbIncludeUnkonwnUcast_Type.__name__ = "Integer32"
_UfbIncludeUnkonwnUcast_Object = MibScalar
ufbIncludeUnkonwnUcast = _UfbIncludeUnkonwnUcast_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 21, 2, 4, 1),
    _UfbIncludeUnkonwnUcast_Type()
)
ufbIncludeUnkonwnUcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ufbIncludeUnkonwnUcast.setStatus("current")
_PortDisableMode_ObjectIdentity = ObjectIdentity
portDisableMode = _PortDisableMode_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 21, 3)
)


class _PortDisableModePeriod_Type(Integer32):
    """Custom type portDisableModePeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PortDisableModePeriod_Type.__name__ = "Integer32"
_PortDisableModePeriod_Object = MibScalar
portDisableModePeriod = _PortDisableModePeriod_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 21, 3, 1),
    _PortDisableModePeriod_Type()
)
portDisableModePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDisableModePeriod.setStatus("current")
_PortDisableModeTable_Object = MibTable
portDisableModeTable = _PortDisableModeTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 21, 3, 2)
)
if mibBuilder.loadTexts:
    portDisableModeTable.setStatus("current")
_PortDisableModeEntry_Object = MibTableRow
portDisableModeEntry = _PortDisableModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 21, 3, 2, 1)
)
portDisableModeEntry.setIndexNames(
    (0, "MOXA-IKS6726A-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    portDisableModeEntry.setStatus("current")


class _IngressLimit_Type(Integer32):
    """Custom type ingressLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("notlimited", 0),
          ("rateGiga1Fps44640", 8),
          ("rateGiga2Fps74410", 9),
          ("rateGiga3Fps148810", 10),
          ("rateGiga4Fps223220", 11),
          ("rateGiga5Fps372030", 12),
          ("rateGiga6Fps520840", 13),
          ("rateGiga7Fps744050", 14),
          ("rateMega1Fps4464", 1),
          ("rateMega2Fps7441", 2),
          ("rateMega3Fps14881", 3),
          ("rateMega4Fps22322", 4),
          ("rateMega5Fps37203", 5),
          ("rateMega6Fps52084", 6),
          ("rateMega7Fps74405", 7))
    )


_IngressLimit_Type.__name__ = "Integer32"
_IngressLimit_Object = MibTableColumn
ingressLimit = _IngressLimit_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 21, 3, 2, 1, 1),
    _IngressLimit_Type()
)
ingressLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ingressLimit.setStatus("current")


class _RateLimitingMode_Type(Integer32):
    """Custom type rateLimitingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("portDisable", 1))
    )


_RateLimitingMode_Type.__name__ = "Integer32"
_RateLimitingMode_Object = MibScalar
rateLimitingMode = _RateLimitingMode_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 21, 4),
    _RateLimitingMode_Type()
)
rateLimitingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rateLimitingMode.setStatus("current")
_Security_ObjectIdentity = ObjectIdentity
security = _Security_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 22)
)
_UserLoginSetting_ObjectIdentity = ObjectIdentity
userLoginSetting = _UserLoginSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 22, 1)
)


class _UserLoginServer_Type(Integer32):
    """Custom type userLoginServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("radius", 2),
          ("tacacs", 1))
    )


_UserLoginServer_Type.__name__ = "Integer32"
_UserLoginServer_Object = MibScalar
userLoginServer = _UserLoginServer_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 22, 1, 1),
    _UserLoginServer_Type()
)
userLoginServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    userLoginServer.setStatus("current")
_TacacsServerSetting_ObjectIdentity = ObjectIdentity
tacacsServerSetting = _TacacsServerSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 22, 1, 2)
)
_TacacsLoginAuthServer_Type = DisplayString
_TacacsLoginAuthServer_Object = MibScalar
tacacsLoginAuthServer = _TacacsLoginAuthServer_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 22, 1, 2, 1),
    _TacacsLoginAuthServer_Type()
)
tacacsLoginAuthServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsLoginAuthServer.setStatus("current")


class _TacacsLoginAuthPort_Type(Integer32):
    """Custom type tacacsLoginAuthPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TacacsLoginAuthPort_Type.__name__ = "Integer32"
_TacacsLoginAuthPort_Object = MibScalar
tacacsLoginAuthPort = _TacacsLoginAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 22, 1, 2, 2),
    _TacacsLoginAuthPort_Type()
)
tacacsLoginAuthPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsLoginAuthPort.setStatus("current")
_TacacsLoginAuthSharedKey_Type = DisplayString
_TacacsLoginAuthSharedKey_Object = MibScalar
tacacsLoginAuthSharedKey = _TacacsLoginAuthSharedKey_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 22, 1, 2, 3),
    _TacacsLoginAuthSharedKey_Type()
)
tacacsLoginAuthSharedKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsLoginAuthSharedKey.setStatus("current")


class _TacacsLoginAuthAuthType_Type(Integer32):
    """Custom type tacacsLoginAuthAuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ascii", 0),
          ("chap", 2),
          ("mschap", 4),
          ("pap", 1))
    )


_TacacsLoginAuthAuthType_Type.__name__ = "Integer32"
_TacacsLoginAuthAuthType_Object = MibScalar
tacacsLoginAuthAuthType = _TacacsLoginAuthAuthType_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 22, 1, 2, 4),
    _TacacsLoginAuthAuthType_Type()
)
tacacsLoginAuthAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsLoginAuthAuthType.setStatus("current")


class _TacacsLoginAuthTimeout_Type(Integer32):
    """Custom type tacacsLoginAuthTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TacacsLoginAuthTimeout_Type.__name__ = "Integer32"
_TacacsLoginAuthTimeout_Object = MibScalar
tacacsLoginAuthTimeout = _TacacsLoginAuthTimeout_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 22, 1, 2, 5),
    _TacacsLoginAuthTimeout_Type()
)
tacacsLoginAuthTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsLoginAuthTimeout.setStatus("current")
_RadiusServerSetting_ObjectIdentity = ObjectIdentity
radiusServerSetting = _RadiusServerSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 22, 1, 3)
)
_RadiusLoginAuthServer_Type = DisplayString
_RadiusLoginAuthServer_Object = MibScalar
radiusLoginAuthServer = _RadiusLoginAuthServer_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 22, 1, 3, 1),
    _RadiusLoginAuthServer_Type()
)
radiusLoginAuthServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusLoginAuthServer.setStatus("current")


class _RadiusLoginAuthPort_Type(Integer32):
    """Custom type radiusLoginAuthPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RadiusLoginAuthPort_Type.__name__ = "Integer32"
_RadiusLoginAuthPort_Object = MibScalar
radiusLoginAuthPort = _RadiusLoginAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 22, 1, 3, 2),
    _RadiusLoginAuthPort_Type()
)
radiusLoginAuthPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusLoginAuthPort.setStatus("current")
_RadiusLoginAuthSharedKey_Type = DisplayString
_RadiusLoginAuthSharedKey_Object = MibScalar
radiusLoginAuthSharedKey = _RadiusLoginAuthSharedKey_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 22, 1, 3, 3),
    _RadiusLoginAuthSharedKey_Type()
)
radiusLoginAuthSharedKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusLoginAuthSharedKey.setStatus("current")


class _RadiusLoginAuthAuthType_Type(Integer32):
    """Custom type radiusLoginAuthAuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("eap-md5", 0)
    )


_RadiusLoginAuthAuthType_Type.__name__ = "Integer32"
_RadiusLoginAuthAuthType_Object = MibScalar
radiusLoginAuthAuthType = _RadiusLoginAuthAuthType_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 22, 1, 3, 4),
    _RadiusLoginAuthAuthType_Type()
)
radiusLoginAuthAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusLoginAuthAuthType.setStatus("current")


class _RadiusLoginAuthTimeout_Type(Integer32):
    """Custom type radiusLoginAuthTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RadiusLoginAuthTimeout_Type.__name__ = "Integer32"
_RadiusLoginAuthTimeout_Object = MibScalar
radiusLoginAuthTimeout = _RadiusLoginAuthTimeout_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 22, 1, 3, 5),
    _RadiusLoginAuthTimeout_Type()
)
radiusLoginAuthTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusLoginAuthTimeout.setStatus("current")
_PortAccessControl_ObjectIdentity = ObjectIdentity
portAccessControl = _PortAccessControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 22, 2)
)
_StaticPortLock_ObjectIdentity = ObjectIdentity
staticPortLock = _StaticPortLock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 22, 2, 1)
)
_StaticPortLockAddress_Type = MacAddress
_StaticPortLockAddress_Object = MibScalar
staticPortLockAddress = _StaticPortLockAddress_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 22, 2, 1, 1),
    _StaticPortLockAddress_Type()
)
staticPortLockAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    staticPortLockAddress.setStatus("current")
_StaticPortLockPort_Type = Integer32
_StaticPortLockPort_Object = MibScalar
staticPortLockPort = _StaticPortLockPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 22, 2, 1, 2),
    _StaticPortLockPort_Type()
)
staticPortLockPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    staticPortLockPort.setStatus("current")


class _StaticPortLockStatus_Type(Integer32):
    """Custom type staticPortLockStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4))
    )


_StaticPortLockStatus_Type.__name__ = "Integer32"
_StaticPortLockStatus_Object = MibScalar
staticPortLockStatus = _StaticPortLockStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 22, 2, 1, 3),
    _StaticPortLockStatus_Type()
)
staticPortLockStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    staticPortLockStatus.setStatus("current")
_Dot1x_ObjectIdentity = ObjectIdentity
dot1x = _Dot1x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 22, 2, 2)
)


class _DataBaseOption_Type(Integer32):
    """Custom type dataBaseOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("radius", 2),
          ("radiuslocal", 3))
    )


_DataBaseOption_Type.__name__ = "Integer32"
_DataBaseOption_Object = MibScalar
dataBaseOption = _DataBaseOption_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 22, 2, 2, 1),
    _DataBaseOption_Type()
)
dataBaseOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dataBaseOption.setStatus("current")


class _Dot1xReauthEnable_Type(Integer32):
    """Custom type dot1xReauthEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Dot1xReauthEnable_Type.__name__ = "Integer32"
_Dot1xReauthEnable_Object = MibScalar
dot1xReauthEnable = _Dot1xReauthEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 22, 2, 2, 5),
    _Dot1xReauthEnable_Type()
)
dot1xReauthEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xReauthEnable.setStatus("current")


class _Dot1xReauthPeriod_Type(Integer32):
    """Custom type dot1xReauthPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_Dot1xReauthPeriod_Type.__name__ = "Integer32"
_Dot1xReauthPeriod_Object = MibScalar
dot1xReauthPeriod = _Dot1xReauthPeriod_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 22, 2, 2, 6),
    _Dot1xReauthPeriod_Type()
)
dot1xReauthPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xReauthPeriod.setStatus("current")
_Dot1xSettingTable_Object = MibTable
dot1xSettingTable = _Dot1xSettingTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 22, 2, 2, 7)
)
if mibBuilder.loadTexts:
    dot1xSettingTable.setStatus("current")
_Dot1xSettingEntry_Object = MibTableRow
dot1xSettingEntry = _Dot1xSettingEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 22, 2, 2, 7, 1)
)
dot1xSettingEntry.setIndexNames(
    (0, "MOXA-IKS6726A-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    dot1xSettingEntry.setStatus("current")


class _EnableDot1X_Type(Integer32):
    """Custom type enableDot1X based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_EnableDot1X_Type.__name__ = "Integer32"
_EnableDot1X_Object = MibTableColumn
enableDot1X = _EnableDot1X_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 22, 2, 2, 7, 1, 1),
    _EnableDot1X_Type()
)
enableDot1X.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableDot1X.setStatus("current")
_Dot1xReauthTable_Object = MibTable
dot1xReauthTable = _Dot1xReauthTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 22, 2, 2, 8)
)
if mibBuilder.loadTexts:
    dot1xReauthTable.setStatus("current")
_Dot1xReauthEntry_Object = MibTableRow
dot1xReauthEntry = _Dot1xReauthEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 22, 2, 2, 8, 1)
)
dot1xReauthEntry.setIndexNames(
    (0, "MOXA-IKS6726A-MIB", "dot1xReauthPortIndex"),
)
if mibBuilder.loadTexts:
    dot1xReauthEntry.setStatus("current")
_Dot1xReauthPortIndex_Type = Integer32
_Dot1xReauthPortIndex_Object = MibTableColumn
dot1xReauthPortIndex = _Dot1xReauthPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 22, 2, 2, 8, 1, 1),
    _Dot1xReauthPortIndex_Type()
)
dot1xReauthPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dot1xReauthPortIndex.setStatus("current")


class _Dot1xReauth_Type(Integer32):
    """Custom type dot1xReauth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_Dot1xReauth_Type.__name__ = "Integer32"
_Dot1xReauth_Object = MibTableColumn
dot1xReauth = _Dot1xReauth_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 22, 2, 2, 8, 1, 2),
    _Dot1xReauth_Type()
)
dot1xReauth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xReauth.setStatus("current")
_Dot1xRadius_ObjectIdentity = ObjectIdentity
dot1xRadius = _Dot1xRadius_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 22, 2, 2, 9)
)


class _Dot1xSameAsAuthServer_Type(Integer32):
    """Custom type dot1xSameAsAuthServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notSame", 0),
          ("same", 1))
    )


_Dot1xSameAsAuthServer_Type.__name__ = "Integer32"
_Dot1xSameAsAuthServer_Object = MibScalar
dot1xSameAsAuthServer = _Dot1xSameAsAuthServer_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 22, 2, 2, 9, 1),
    _Dot1xSameAsAuthServer_Type()
)
dot1xSameAsAuthServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xSameAsAuthServer.setStatus("current")
_Dot1x1stRadiusServer_Type = DisplayString
_Dot1x1stRadiusServer_Object = MibScalar
dot1x1stRadiusServer = _Dot1x1stRadiusServer_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 22, 2, 2, 9, 2),
    _Dot1x1stRadiusServer_Type()
)
dot1x1stRadiusServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1x1stRadiusServer.setStatus("current")


class _Dot1x1stRadiusPort_Type(Integer32):
    """Custom type dot1x1stRadiusPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Dot1x1stRadiusPort_Type.__name__ = "Integer32"
_Dot1x1stRadiusPort_Object = MibScalar
dot1x1stRadiusPort = _Dot1x1stRadiusPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 22, 2, 2, 9, 3),
    _Dot1x1stRadiusPort_Type()
)
dot1x1stRadiusPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1x1stRadiusPort.setStatus("current")
_Dot1x1stRadiusSharedKey_Type = DisplayString
_Dot1x1stRadiusSharedKey_Object = MibScalar
dot1x1stRadiusSharedKey = _Dot1x1stRadiusSharedKey_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 22, 2, 2, 9, 4),
    _Dot1x1stRadiusSharedKey_Type()
)
dot1x1stRadiusSharedKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1x1stRadiusSharedKey.setStatus("current")
_Dot1x2ndRadiusServer_Type = DisplayString
_Dot1x2ndRadiusServer_Object = MibScalar
dot1x2ndRadiusServer = _Dot1x2ndRadiusServer_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 22, 2, 2, 9, 5),
    _Dot1x2ndRadiusServer_Type()
)
dot1x2ndRadiusServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1x2ndRadiusServer.setStatus("current")


class _Dot1x2ndRadiusPort_Type(Integer32):
    """Custom type dot1x2ndRadiusPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Dot1x2ndRadiusPort_Type.__name__ = "Integer32"
_Dot1x2ndRadiusPort_Object = MibScalar
dot1x2ndRadiusPort = _Dot1x2ndRadiusPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 22, 2, 2, 9, 6),
    _Dot1x2ndRadiusPort_Type()
)
dot1x2ndRadiusPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1x2ndRadiusPort.setStatus("current")
_Dot1x2ndRadiusSharedKey_Type = DisplayString
_Dot1x2ndRadiusSharedKey_Object = MibScalar
dot1x2ndRadiusSharedKey = _Dot1x2ndRadiusSharedKey_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 22, 2, 2, 9, 7),
    _Dot1x2ndRadiusSharedKey_Type()
)
dot1x2ndRadiusSharedKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1x2ndRadiusSharedKey.setStatus("current")
_PortAccessControlTable_Object = MibTable
portAccessControlTable = _PortAccessControlTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 22, 2, 3)
)
if mibBuilder.loadTexts:
    portAccessControlTable.setStatus("current")
_PortAccessControlEntry_Object = MibTableRow
portAccessControlEntry = _PortAccessControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 22, 2, 3, 1)
)
portAccessControlEntry.setIndexNames(
    (0, "MOXA-IKS6726A-MIB", "portAccessControlAddress"),
)
if mibBuilder.loadTexts:
    portAccessControlEntry.setStatus("current")
_PortAccessControlAddress_Type = MacAddress
_PortAccessControlAddress_Object = MibTableColumn
portAccessControlAddress = _PortAccessControlAddress_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 22, 2, 3, 1, 1),
    _PortAccessControlAddress_Type()
)
portAccessControlAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portAccessControlAddress.setStatus("current")
_PortAccessControlPortNo_Type = Integer32
_PortAccessControlPortNo_Object = MibTableColumn
portAccessControlPortNo = _PortAccessControlPortNo_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 22, 2, 3, 1, 2),
    _PortAccessControlPortNo_Type()
)
portAccessControlPortNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portAccessControlPortNo.setStatus("current")


class _PortAccessControlAccessStatus_Type(Integer32):
    """Custom type portAccessControlAccessStatus based on Integer32"""
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
        *(("authorized", 2),
          ("authorizing", 4),
          ("staticLock", 1),
          ("unAuthorized", 3))
    )


_PortAccessControlAccessStatus_Type.__name__ = "Integer32"
_PortAccessControlAccessStatus_Object = MibTableColumn
portAccessControlAccessStatus = _PortAccessControlAccessStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 22, 2, 3, 1, 3),
    _PortAccessControlAccessStatus_Type()
)
portAccessControlAccessStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portAccessControlAccessStatus.setStatus("current")


class _PortAccessControlStatus_Type(Integer32):
    """Custom type portAccessControlStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6))
    )


_PortAccessControlStatus_Type.__name__ = "Integer32"
_PortAccessControlStatus_Object = MibTableColumn
portAccessControlStatus = _PortAccessControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 22, 2, 3, 1, 4),
    _PortAccessControlStatus_Type()
)
portAccessControlStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portAccessControlStatus.setStatus("current")
_AccessibleIP_ObjectIdentity = ObjectIdentity
accessibleIP = _AccessibleIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 30)
)


class _EnableAccessibleIP_Type(Integer32):
    """Custom type enableAccessibleIP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_EnableAccessibleIP_Type.__name__ = "Integer32"
_EnableAccessibleIP_Object = MibScalar
enableAccessibleIP = _EnableAccessibleIP_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 30, 1),
    _EnableAccessibleIP_Type()
)
enableAccessibleIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableAccessibleIP.setStatus("current")
_AccessibleIpTable_Object = MibTable
accessibleIpTable = _AccessibleIpTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 30, 2)
)
if mibBuilder.loadTexts:
    accessibleIpTable.setStatus("current")
_AccessibleIpEntry_Object = MibTableRow
accessibleIpEntry = _AccessibleIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 30, 2, 1)
)
accessibleIpEntry.setIndexNames(
    (0, "MOXA-IKS6726A-MIB", "accessibleIpAddress"),
)
if mibBuilder.loadTexts:
    accessibleIpEntry.setStatus("current")
_AccessibleIpAddress_Type = IpAddress
_AccessibleIpAddress_Object = MibTableColumn
accessibleIpAddress = _AccessibleIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 30, 2, 1, 1),
    _AccessibleIpAddress_Type()
)
accessibleIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    accessibleIpAddress.setStatus("current")
_AccessibleIpNetMask_Type = IpAddress
_AccessibleIpNetMask_Object = MibTableColumn
accessibleIpNetMask = _AccessibleIpNetMask_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 30, 2, 1, 2),
    _AccessibleIpNetMask_Type()
)
accessibleIpNetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    accessibleIpNetMask.setStatus("current")


class _AccessibleIpStatus_Type(Integer32):
    """Custom type accessibleIpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6))
    )


_AccessibleIpStatus_Type.__name__ = "Integer32"
_AccessibleIpStatus_Object = MibTableColumn
accessibleIpStatus = _AccessibleIpStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 30, 2, 1, 3),
    _AccessibleIpStatus_Type()
)
accessibleIpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    accessibleIpStatus.setStatus("current")
_SysFileUpdate_ObjectIdentity = ObjectIdentity
sysFileUpdate = _SysFileUpdate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 31)
)
_TftpServer_Type = DisplayString
_TftpServer_Object = MibScalar
tftpServer = _TftpServer_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 31, 1),
    _TftpServer_Type()
)
tftpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpServer.setStatus("current")
_FirmwarePathName_Type = DisplayString
_FirmwarePathName_Object = MibScalar
firmwarePathName = _FirmwarePathName_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 31, 2),
    _FirmwarePathName_Type()
)
firmwarePathName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firmwarePathName.setStatus("current")
_LogPathName_Type = DisplayString
_LogPathName_Object = MibScalar
logPathName = _LogPathName_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 31, 3),
    _LogPathName_Type()
)
logPathName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logPathName.setStatus("current")
_ConfPathName_Type = DisplayString
_ConfPathName_Object = MibScalar
confPathName = _ConfPathName_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 31, 4),
    _ConfPathName_Type()
)
confPathName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    confPathName.setStatus("current")


class _TftpUpdate_Type(Integer32):
    """Custom type tftpUpdate based on Integer32"""
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
        *(("exportConfig", 3),
          ("exportLog", 4),
          ("importConfig", 2),
          ("importFirmware", 1))
    )


_TftpUpdate_Type.__name__ = "Integer32"
_TftpUpdate_Object = MibScalar
tftpUpdate = _TftpUpdate_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 31, 5),
    _TftpUpdate_Type()
)
tftpUpdate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tftpUpdate.setStatus("current")
_TimeSetting_ObjectIdentity = ObjectIdentity
timeSetting = _TimeSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 32)
)
_SysDateTime_Type = DateAndTime
_SysDateTime_Object = MibScalar
sysDateTime = _SysDateTime_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 32, 1),
    _SysDateTime_Type()
)
sysDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysDateTime.setStatus("current")
_CalibratePeriod_Type = Integer32
_CalibratePeriod_Object = MibScalar
calibratePeriod = _CalibratePeriod_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 32, 2),
    _CalibratePeriod_Type()
)
calibratePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    calibratePeriod.setStatus("current")
_TimeServer1_Type = DisplayString
_TimeServer1_Object = MibScalar
timeServer1 = _TimeServer1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 32, 3),
    _TimeServer1_Type()
)
timeServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeServer1.setStatus("current")
_TimeServer2_Type = DisplayString
_TimeServer2_Object = MibScalar
timeServer2 = _TimeServer2_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 32, 4),
    _TimeServer2_Type()
)
timeServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeServer2.setStatus("current")
_DaylightSaving_ObjectIdentity = ObjectIdentity
daylightSaving = _DaylightSaving_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 32, 5)
)


class _StartMonth_Type(Integer32):
    """Custom type startMonth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("apr", 4),
          ("aug", 8),
          ("dec", 12),
          ("feb", 2),
          ("jan", 1),
          ("jul", 7),
          ("jun", 6),
          ("mar", 3),
          ("may", 5),
          ("na", 0),
          ("nov", 11),
          ("oct", 10),
          ("sep", 9))
    )


_StartMonth_Type.__name__ = "Integer32"
_StartMonth_Object = MibScalar
startMonth = _StartMonth_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 32, 5, 1),
    _StartMonth_Type()
)
startMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    startMonth.setStatus("current")


class _StartWeek_Type(Integer32):
    """Custom type startWeek based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("na", 0),
          ("week1", 1),
          ("week2", 2),
          ("week3", 3),
          ("week4", 4),
          ("weeklast", 6))
    )


_StartWeek_Type.__name__ = "Integer32"
_StartWeek_Object = MibScalar
startWeek = _StartWeek_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 32, 5, 2),
    _StartWeek_Type()
)
startWeek.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    startWeek.setStatus("current")


class _StartDay_Type(Integer32):
    """Custom type startDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("fri", 6),
          ("mon", 2),
          ("na", 0),
          ("sat", 7),
          ("sun", 1),
          ("thu", 5),
          ("tue", 3),
          ("wed", 4))
    )


_StartDay_Type.__name__ = "Integer32"
_StartDay_Object = MibScalar
startDay = _StartDay_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 32, 5, 3),
    _StartDay_Type()
)
startDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    startDay.setStatus("current")
_StartHour_Type = Integer32
_StartHour_Object = MibScalar
startHour = _StartHour_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 32, 5, 4),
    _StartHour_Type()
)
startHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    startHour.setStatus("current")


class _EndMonth_Type(Integer32):
    """Custom type endMonth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("apr", 4),
          ("aug", 8),
          ("dec", 12),
          ("feb", 2),
          ("jan", 1),
          ("jul", 7),
          ("jun", 6),
          ("mar", 3),
          ("may", 5),
          ("na", 0),
          ("nov", 11),
          ("oct", 10),
          ("sep", 9))
    )


_EndMonth_Type.__name__ = "Integer32"
_EndMonth_Object = MibScalar
endMonth = _EndMonth_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 32, 5, 5),
    _EndMonth_Type()
)
endMonth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    endMonth.setStatus("current")


class _EndWeek_Type(Integer32):
    """Custom type endWeek based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("na", 0),
          ("week1", 1),
          ("week2", 2),
          ("week3", 3),
          ("week4", 4),
          ("weeklast", 6))
    )


_EndWeek_Type.__name__ = "Integer32"
_EndWeek_Object = MibScalar
endWeek = _EndWeek_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 32, 5, 6),
    _EndWeek_Type()
)
endWeek.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    endWeek.setStatus("current")


class _EndDay_Type(Integer32):
    """Custom type endDay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("fri", 6),
          ("mon", 2),
          ("na", 0),
          ("sat", 7),
          ("sun", 1),
          ("thu", 5),
          ("tue", 3),
          ("wed", 4))
    )


_EndDay_Type.__name__ = "Integer32"
_EndDay_Object = MibScalar
endDay = _EndDay_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 32, 5, 7),
    _EndDay_Type()
)
endDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    endDay.setStatus("current")
_EndHour_Type = Integer32
_EndHour_Object = MibScalar
endHour = _EndHour_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 32, 5, 8),
    _EndHour_Type()
)
endHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    endHour.setStatus("current")
_OffsetHours_Type = Integer32
_OffsetHours_Object = MibScalar
offsetHours = _OffsetHours_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 32, 5, 9),
    _OffsetHours_Type()
)
offsetHours.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    offsetHours.setStatus("current")


class _EnableNTPServer_Type(Integer32):
    """Custom type enableNTPServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_EnableNTPServer_Type.__name__ = "Integer32"
_EnableNTPServer_Object = MibScalar
enableNTPServer = _EnableNTPServer_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 32, 6),
    _EnableNTPServer_Type()
)
enableNTPServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableNTPServer.setStatus("current")


class _ClockSource_Type(Integer32):
    """Custom type clockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 0),
          ("ntp", 2),
          ("sntp", 1))
    )


_ClockSource_Type.__name__ = "Integer32"
_ClockSource_Object = MibScalar
clockSource = _ClockSource_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 32, 7),
    _ClockSource_Type()
)
clockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clockSource.setStatus("current")
_BackupMediaSetting_ObjectIdentity = ObjectIdentity
backupMediaSetting = _BackupMediaSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 35)
)


class _Abc02Status_Type(Integer32):
    """Custom type abc02Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("detecting", 2),
          ("device-not-present", 0),
          ("ready-and-removable", 4),
          ("unauthorized-media", 1),
          ("working", 3))
    )


_Abc02Status_Type.__name__ = "Integer32"
_Abc02Status_Object = MibScalar
abc02Status = _Abc02Status_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 35, 2),
    _Abc02Status_Type()
)
abc02Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    abc02Status.setStatus("current")


class _Abc02AutoImportConfig_Type(Integer32):
    """Custom type abc02AutoImportConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Abc02AutoImportConfig_Type.__name__ = "Integer32"
_Abc02AutoImportConfig_Object = MibScalar
abc02AutoImportConfig = _Abc02AutoImportConfig_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 35, 3),
    _Abc02AutoImportConfig_Type()
)
abc02AutoImportConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    abc02AutoImportConfig.setStatus("current")


class _Abc02AutoExportConfig_Type(Integer32):
    """Custom type abc02AutoExportConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Abc02AutoExportConfig_Type.__name__ = "Integer32"
_Abc02AutoExportConfig_Object = MibScalar
abc02AutoExportConfig = _Abc02AutoExportConfig_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 35, 4),
    _Abc02AutoExportConfig_Type()
)
abc02AutoExportConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    abc02AutoExportConfig.setStatus("current")


class _Abc02AutoExportLog_Type(Integer32):
    """Custom type abc02AutoExportLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Abc02AutoExportLog_Type.__name__ = "Integer32"
_Abc02AutoExportLog_Object = MibScalar
abc02AutoExportLog = _Abc02AutoExportLog_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 35, 5),
    _Abc02AutoExportLog_Type()
)
abc02AutoExportLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    abc02AutoExportLog.setStatus("current")


class _EnableWarmStart_Type(Integer32):
    """Custom type enableWarmStart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_EnableWarmStart_Type.__name__ = "Integer32"
_EnableWarmStart_Object = MibScalar
enableWarmStart = _EnableWarmStart_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 36),
    _EnableWarmStart_Type()
)
enableWarmStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableWarmStart.setStatus("current")
_SyslogSetting_ObjectIdentity = ObjectIdentity
syslogSetting = _SyslogSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 37)
)
_SyslogServer1_Type = DisplayString
_SyslogServer1_Object = MibScalar
syslogServer1 = _SyslogServer1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 37, 1),
    _SyslogServer1_Type()
)
syslogServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogServer1.setStatus("current")
_SyslogServer1port_Type = Integer32
_SyslogServer1port_Object = MibScalar
syslogServer1port = _SyslogServer1port_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 37, 2),
    _SyslogServer1port_Type()
)
syslogServer1port.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogServer1port.setStatus("current")
_SyslogServer2_Type = DisplayString
_SyslogServer2_Object = MibScalar
syslogServer2 = _SyslogServer2_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 37, 3),
    _SyslogServer2_Type()
)
syslogServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogServer2.setStatus("current")
_SyslogServer2port_Type = Integer32
_SyslogServer2port_Object = MibScalar
syslogServer2port = _SyslogServer2port_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 37, 4),
    _SyslogServer2port_Type()
)
syslogServer2port.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogServer2port.setStatus("current")
_SyslogServer3_Type = DisplayString
_SyslogServer3_Object = MibScalar
syslogServer3 = _SyslogServer3_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 37, 5),
    _SyslogServer3_Type()
)
syslogServer3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogServer3.setStatus("current")
_SyslogServer3port_Type = Integer32
_SyslogServer3port_Object = MibScalar
syslogServer3port = _SyslogServer3port_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 37, 6),
    _SyslogServer3port_Type()
)
syslogServer3port.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogServer3port.setStatus("current")
_DhcpRelayAgentSetting_ObjectIdentity = ObjectIdentity
dhcpRelayAgentSetting = _DhcpRelayAgentSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 39)
)
_DhcpServer1_Type = DisplayString
_DhcpServer1_Object = MibScalar
dhcpServer1 = _DhcpServer1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 39, 1),
    _DhcpServer1_Type()
)
dhcpServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServer1.setStatus("current")
_DhcpServer2_Type = DisplayString
_DhcpServer2_Object = MibScalar
dhcpServer2 = _DhcpServer2_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 39, 2),
    _DhcpServer2_Type()
)
dhcpServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServer2.setStatus("current")
_DhcpServer3_Type = DisplayString
_DhcpServer3_Object = MibScalar
dhcpServer3 = _DhcpServer3_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 39, 3),
    _DhcpServer3_Type()
)
dhcpServer3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServer3.setStatus("current")
_DhcpServer4_Type = DisplayString
_DhcpServer4_Object = MibScalar
dhcpServer4 = _DhcpServer4_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 39, 4),
    _DhcpServer4_Type()
)
dhcpServer4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpServer4.setStatus("current")
_Option82Setting_ObjectIdentity = ObjectIdentity
option82Setting = _Option82Setting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 39, 5)
)


class _EnableOption82_Type(Integer32):
    """Custom type enableOption82 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_EnableOption82_Type.__name__ = "Integer32"
_EnableOption82_Object = MibScalar
enableOption82 = _EnableOption82_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 39, 5, 1),
    _EnableOption82_Type()
)
enableOption82.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableOption82.setStatus("current")


class _Option82Type_Type(Integer32):
    """Custom type option82Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("client-id", 2),
          ("ip", 0),
          ("mac", 1),
          ("other", 3))
    )


_Option82Type_Type.__name__ = "Integer32"
_Option82Type_Object = MibScalar
option82Type = _Option82Type_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 39, 5, 2),
    _Option82Type_Type()
)
option82Type.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    option82Type.setStatus("current")
_Option82Value_Type = DisplayString
_Option82Value_Object = MibScalar
option82Value = _Option82Value_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 39, 5, 3),
    _Option82Value_Type()
)
option82Value.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    option82Value.setStatus("current")
_Option82ValueDisplay_Type = DisplayString
_Option82ValueDisplay_Object = MibScalar
option82ValueDisplay = _Option82ValueDisplay_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 39, 5, 4),
    _Option82ValueDisplay_Type()
)
option82ValueDisplay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    option82ValueDisplay.setStatus("current")
_DhcpFunctionTable_Object = MibTable
dhcpFunctionTable = _DhcpFunctionTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 39, 6)
)
if mibBuilder.loadTexts:
    dhcpFunctionTable.setStatus("current")
_DhcpFunctionTableEntry_Object = MibTableRow
dhcpFunctionTableEntry = _DhcpFunctionTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 39, 6, 1)
)
dhcpFunctionTableEntry.setIndexNames(
    (0, "MOXA-IKS6726A-MIB", "dhcpPortIndex"),
)
if mibBuilder.loadTexts:
    dhcpFunctionTableEntry.setStatus("current")
_DhcpPortIndex_Type = Integer32
_DhcpPortIndex_Object = MibTableColumn
dhcpPortIndex = _DhcpPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 39, 6, 1, 1),
    _DhcpPortIndex_Type()
)
dhcpPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpPortIndex.setStatus("current")
_CircuitID_Type = DisplayString
_CircuitID_Object = MibTableColumn
circuitID = _CircuitID_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 39, 6, 1, 2),
    _CircuitID_Type()
)
circuitID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitID.setStatus("current")


class _Option82Enable_Type(Integer32):
    """Custom type option82Enable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_Option82Enable_Type.__name__ = "Integer32"
_Option82Enable_Object = MibTableColumn
option82Enable = _Option82Enable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 39, 6, 1, 3),
    _Option82Enable_Type()
)
option82Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    option82Enable.setStatus("current")
_Ieee1588Setting_ObjectIdentity = ObjectIdentity
ieee1588Setting = _Ieee1588Setting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 41)
)
_Ptpv1Setting_ObjectIdentity = ObjectIdentity
ptpv1Setting = _Ptpv1Setting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 41, 1)
)


class _EnablePtpv1_Type(Integer32):
    """Custom type enablePtpv1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_EnablePtpv1_Type.__name__ = "Integer32"
_EnablePtpv1_Object = MibScalar
enablePtpv1 = _EnablePtpv1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 41, 1, 1),
    _EnablePtpv1_Type()
)
enablePtpv1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enablePtpv1.setStatus("current")


class _ClockModev1_Type(Integer32):
    """Custom type clockModev1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("v1BC", 0),
          ("v2E2E2stepTC", 1),
          ("v2E2EBC", 4),
          ("v2P2PBC", 5),
          ("v2P2PTC", 3))
    )


_ClockModev1_Type.__name__ = "Integer32"
_ClockModev1_Object = MibScalar
clockModev1 = _ClockModev1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 41, 1, 2),
    _ClockModev1_Type()
)
clockModev1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clockModev1.setStatus("current")


class _SyncIntervalv1_Type(Integer32):
    """Custom type syncIntervalv1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("eightSec", 3),
          ("fourSec", 2),
          ("oneSec", 0),
          ("sixteenSec", 4),
          ("twoSec", 1))
    )


_SyncIntervalv1_Type.__name__ = "Integer32"
_SyncIntervalv1_Object = MibScalar
syncIntervalv1 = _SyncIntervalv1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 41, 1, 3),
    _SyncIntervalv1_Type()
)
syncIntervalv1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syncIntervalv1.setStatus("current")


class _SubDomainNamev1_Type(Integer32):
    """Custom type subDomainNamev1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alt1", 1),
          ("alt2", 2),
          ("alt3", 3),
          ("dflt", 0))
    )


_SubDomainNamev1_Type.__name__ = "Integer32"
_SubDomainNamev1_Object = MibScalar
subDomainNamev1 = _SubDomainNamev1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 41, 1, 4),
    _SubDomainNamev1_Type()
)
subDomainNamev1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subDomainNamev1.setStatus("current")


class _PreferMasterv1_Type(Integer32):
    """Custom type preferMasterv1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_PreferMasterv1_Type.__name__ = "Integer32"
_PreferMasterv1_Object = MibScalar
preferMasterv1 = _PreferMasterv1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 41, 1, 5),
    _PreferMasterv1_Type()
)
preferMasterv1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    preferMasterv1.setStatus("current")
_Ptpv2Setting_ObjectIdentity = ObjectIdentity
ptpv2Setting = _Ptpv2Setting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 41, 2)
)


class _EnablePtp_Type(Integer32):
    """Custom type enablePtp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_EnablePtp_Type.__name__ = "Integer32"
_EnablePtp_Object = MibScalar
enablePtp = _EnablePtp_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 41, 2, 1),
    _EnablePtp_Type()
)
enablePtp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enablePtp.setStatus("current")


class _ClockMode_Type(Integer32):
    """Custom type clockMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("v1BC", 0),
          ("v2E2E2stepTC", 1),
          ("v2E2EBC", 4),
          ("v2P2PBC", 5),
          ("v2P2PTC", 3))
    )


_ClockMode_Type.__name__ = "Integer32"
_ClockMode_Object = MibScalar
clockMode = _ClockMode_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 41, 2, 2),
    _ClockMode_Type()
)
clockMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clockMode.setStatus("current")


class _Transport_Type(Integer32):
    """Custom type transport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ieee802dot3", 0),
          ("ipv4", 1))
    )


_Transport_Type.__name__ = "Integer32"
_Transport_Object = MibScalar
transport = _Transport_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 41, 2, 3),
    _Transport_Type()
)
transport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transport.setStatus("current")


class _SyncInterval_Type(Integer32):
    """Custom type syncInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-3,
              -2,
              -1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("t128msec", -3),
          ("t1sec", 0),
          ("t256msec", -2),
          ("t2sec", 1),
          ("t512msec", -1))
    )


_SyncInterval_Type.__name__ = "Integer32"
_SyncInterval_Object = MibScalar
syncInterval = _SyncInterval_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 41, 2, 4),
    _SyncInterval_Type()
)
syncInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syncInterval.setStatus("current")


class _LogMinDelayReqInterval_Type(Integer32):
    """Custom type logMinDelayReqInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("t16sec", 4),
          ("t1sec", 0),
          ("t2sec", 1),
          ("t32sec", 5),
          ("t4sec", 2),
          ("t8sec", 3))
    )


_LogMinDelayReqInterval_Type.__name__ = "Integer32"
_LogMinDelayReqInterval_Object = MibScalar
logMinDelayReqInterval = _LogMinDelayReqInterval_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 41, 2, 5),
    _LogMinDelayReqInterval_Type()
)
logMinDelayReqInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logMinDelayReqInterval.setStatus("current")


class _LogMinPdelayReqInterval_Type(Integer32):
    """Custom type logMinPdelayReqInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("t16sec", 4),
          ("t1sec", 0),
          ("t2sec", 1),
          ("t32sec", 5),
          ("t4sec", 2),
          ("t512msec", -1),
          ("t8sec", 3))
    )


_LogMinPdelayReqInterval_Type.__name__ = "Integer32"
_LogMinPdelayReqInterval_Object = MibScalar
logMinPdelayReqInterval = _LogMinPdelayReqInterval_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 41, 2, 6),
    _LogMinPdelayReqInterval_Type()
)
logMinPdelayReqInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logMinPdelayReqInterval.setStatus("current")


class _LogAnnounceInterval_Type(Integer32):
    """Custom type logAnnounceInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("t16sec", 4),
          ("t1sec", 0),
          ("t2sec", 1),
          ("t4sec", 2),
          ("t8sec", 3))
    )


_LogAnnounceInterval_Type.__name__ = "Integer32"
_LogAnnounceInterval_Object = MibScalar
logAnnounceInterval = _LogAnnounceInterval_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 41, 2, 7),
    _LogAnnounceInterval_Type()
)
logAnnounceInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logAnnounceInterval.setStatus("current")


class _AnnounceReceiptTimeout_Type(Integer32):
    """Custom type announceReceiptTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_AnnounceReceiptTimeout_Type.__name__ = "Integer32"
_AnnounceReceiptTimeout_Object = MibScalar
announceReceiptTimeout = _AnnounceReceiptTimeout_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 41, 2, 8),
    _AnnounceReceiptTimeout_Type()
)
announceReceiptTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    announceReceiptTimeout.setStatus("current")
_Priority1_Type = Integer32
_Priority1_Object = MibScalar
priority1 = _Priority1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 41, 2, 9),
    _Priority1_Type()
)
priority1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    priority1.setStatus("current")
_Priority2_Type = Integer32
_Priority2_Object = MibScalar
priority2 = _Priority2_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 41, 2, 10),
    _Priority2_Type()
)
priority2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    priority2.setStatus("current")
_ClockClass_Type = Integer32
_ClockClass_Object = MibScalar
clockClass = _ClockClass_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 41, 2, 11),
    _ClockClass_Type()
)
clockClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clockClass.setStatus("current")


class _DomainNumber_Type(Integer32):
    """Custom type domainNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alt1", 1),
          ("alt2", 2),
          ("alt3", 3),
          ("dflt", 0))
    )


_DomainNumber_Type.__name__ = "Integer32"
_DomainNumber_Object = MibScalar
domainNumber = _DomainNumber_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 41, 2, 12),
    _DomainNumber_Type()
)
domainNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    domainNumber.setStatus("current")
_LocalUtcOffset_Type = Integer32
_LocalUtcOffset_Object = MibScalar
localUtcOffset = _LocalUtcOffset_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 41, 2, 13),
    _LocalUtcOffset_Type()
)
localUtcOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localUtcOffset.setStatus("current")


class _LocalUtcOffsetValid_Type(Integer32):
    """Custom type localUtcOffsetValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_LocalUtcOffsetValid_Type.__name__ = "Integer32"
_LocalUtcOffsetValid_Object = MibScalar
localUtcOffsetValid = _LocalUtcOffsetValid_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 41, 2, 14),
    _LocalUtcOffsetValid_Type()
)
localUtcOffsetValid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localUtcOffsetValid.setStatus("current")


class _LocalLeap59_Type(Integer32):
    """Custom type localLeap59 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_LocalLeap59_Type.__name__ = "Integer32"
_LocalLeap59_Object = MibScalar
localLeap59 = _LocalLeap59_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 41, 2, 15),
    _LocalLeap59_Type()
)
localLeap59.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localLeap59.setStatus("current")


class _LocalLeap61_Type(Integer32):
    """Custom type localLeap61 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_LocalLeap61_Type.__name__ = "Integer32"
_LocalLeap61_Object = MibScalar
localLeap61 = _LocalLeap61_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 41, 2, 16),
    _LocalLeap61_Type()
)
localLeap61.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localLeap61.setStatus("current")


class _LocalPtpTimescale_Type(Integer32):
    """Custom type localPtpTimescale based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("arb", 0),
          ("ptp", 1))
    )


_LocalPtpTimescale_Type.__name__ = "Integer32"
_LocalPtpTimescale_Object = MibScalar
localPtpTimescale = _LocalPtpTimescale_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 41, 2, 17),
    _LocalPtpTimescale_Type()
)
localPtpTimescale.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localPtpTimescale.setStatus("current")
_LocalArbTime_Type = Integer32
_LocalArbTime_Object = MibScalar
localArbTime = _LocalArbTime_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 41, 2, 18),
    _LocalArbTime_Type()
)
localArbTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    localArbTime.setStatus("current")
_Ptpv1Status_ObjectIdentity = ObjectIdentity
ptpv1Status = _Ptpv1Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 41, 3)
)
_OffsetToMasterv1_Type = Integer32
_OffsetToMasterv1_Object = MibScalar
offsetToMasterv1 = _OffsetToMasterv1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 41, 3, 1),
    _OffsetToMasterv1_Type()
)
offsetToMasterv1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    offsetToMasterv1.setStatus("current")
_MeanPathDelayv1_Type = Integer32
_MeanPathDelayv1_Object = MibScalar
meanPathDelayv1 = _MeanPathDelayv1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 41, 3, 2),
    _MeanPathDelayv1_Type()
)
meanPathDelayv1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meanPathDelayv1.setStatus("current")
_GrandMasterUuidv1_Type = MacAddress
_GrandMasterUuidv1_Object = MibScalar
grandMasterUuidv1 = _GrandMasterUuidv1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 41, 3, 3),
    _GrandMasterUuidv1_Type()
)
grandMasterUuidv1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grandMasterUuidv1.setStatus("current")
_ParentUuidv1_Type = MacAddress
_ParentUuidv1_Object = MibScalar
parentUuidv1 = _ParentUuidv1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 41, 3, 4),
    _ParentUuidv1_Type()
)
parentUuidv1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parentUuidv1.setStatus("current")
_ClockStratumv1_Type = Integer32
_ClockStratumv1_Object = MibScalar
clockStratumv1 = _ClockStratumv1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 41, 3, 5),
    _ClockStratumv1_Type()
)
clockStratumv1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clockStratumv1.setStatus("current")
_ClockIdentifierv1_Type = DisplayString
_ClockIdentifierv1_Object = MibScalar
clockIdentifierv1 = _ClockIdentifierv1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 41, 3, 6),
    _ClockIdentifierv1_Type()
)
clockIdentifierv1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clockIdentifierv1.setStatus("current")
_Ptpv2Status_ObjectIdentity = ObjectIdentity
ptpv2Status = _Ptpv2Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 41, 4)
)
_OffsetToMaster_Type = Integer32
_OffsetToMaster_Object = MibScalar
offsetToMaster = _OffsetToMaster_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 41, 4, 1),
    _OffsetToMaster_Type()
)
offsetToMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    offsetToMaster.setStatus("current")
_MeanPathDelay_Type = Integer32
_MeanPathDelay_Object = MibScalar
meanPathDelay = _MeanPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 41, 4, 2),
    _MeanPathDelay_Type()
)
meanPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    meanPathDelay.setStatus("current")
_ParentIdentity_Type = DisplayString
_ParentIdentity_Object = MibScalar
parentIdentity = _ParentIdentity_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 41, 4, 3),
    _ParentIdentity_Type()
)
parentIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parentIdentity.setStatus("current")
_GrandmasterIdentity_Type = DisplayString
_GrandmasterIdentity_Object = MibScalar
grandmasterIdentity = _GrandmasterIdentity_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 41, 4, 4),
    _GrandmasterIdentity_Type()
)
grandmasterIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grandmasterIdentity.setStatus("current")
_GrandmasterClockClass_Type = Integer32
_GrandmasterClockClass_Object = MibScalar
grandmasterClockClass = _GrandmasterClockClass_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 41, 4, 5),
    _GrandmasterClockClass_Type()
)
grandmasterClockClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grandmasterClockClass.setStatus("current")
_GrandmasterClockAccuracy_Type = Integer32
_GrandmasterClockAccuracy_Object = MibScalar
grandmasterClockAccuracy = _GrandmasterClockAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 41, 4, 6),
    _GrandmasterClockAccuracy_Type()
)
grandmasterClockAccuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grandmasterClockAccuracy.setStatus("current")
_GrandmasterPriority1_Type = Integer32
_GrandmasterPriority1_Object = MibScalar
grandmasterPriority1 = _GrandmasterPriority1_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 41, 4, 7),
    _GrandmasterPriority1_Type()
)
grandmasterPriority1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grandmasterPriority1.setStatus("current")
_GrandmasterPriority2_Type = Integer32
_GrandmasterPriority2_Object = MibScalar
grandmasterPriority2 = _GrandmasterPriority2_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 41, 4, 8),
    _GrandmasterPriority2_Type()
)
grandmasterPriority2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    grandmasterPriority2.setStatus("current")
_StepsRemoved_Type = Integer32
_StepsRemoved_Object = MibScalar
stepsRemoved = _StepsRemoved_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 41, 4, 9),
    _StepsRemoved_Type()
)
stepsRemoved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stepsRemoved.setStatus("current")
_CurrentUtcOffset_Type = Integer32
_CurrentUtcOffset_Object = MibScalar
currentUtcOffset = _CurrentUtcOffset_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 41, 4, 10),
    _CurrentUtcOffset_Type()
)
currentUtcOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentUtcOffset.setStatus("current")
_CurrentUtcOffsetValid_Type = DisplayString
_CurrentUtcOffsetValid_Object = MibScalar
currentUtcOffsetValid = _CurrentUtcOffsetValid_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 41, 4, 11),
    _CurrentUtcOffsetValid_Type()
)
currentUtcOffsetValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentUtcOffsetValid.setStatus("current")
_Leap59_Type = DisplayString
_Leap59_Object = MibScalar
leap59 = _Leap59_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 41, 4, 12),
    _Leap59_Type()
)
leap59.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    leap59.setStatus("current")
_Leap61_Type = DisplayString
_Leap61_Object = MibScalar
leap61 = _Leap61_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 41, 4, 13),
    _Leap61_Type()
)
leap61.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    leap61.setStatus("current")
_PtpTimescale_Type = DisplayString
_PtpTimescale_Object = MibScalar
ptpTimescale = _PtpTimescale_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 41, 4, 14),
    _PtpTimescale_Type()
)
ptpTimescale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpTimescale.setStatus("current")
_Timesource_Type = DisplayString
_Timesource_Object = MibScalar
timesource = _Timesource_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 41, 4, 15),
    _Timesource_Type()
)
timesource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timesource.setStatus("current")
_PtpPortTable_Object = MibTable
ptpPortTable = _PtpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 41, 5)
)
if mibBuilder.loadTexts:
    ptpPortTable.setStatus("current")
_PtpPortEntry_Object = MibTableRow
ptpPortEntry = _PtpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 41, 5, 1)
)
ptpPortEntry.setIndexNames(
    (0, "MOXA-IKS6726A-MIB", "ptpPortIndex"),
)
if mibBuilder.loadTexts:
    ptpPortEntry.setStatus("current")
_PtpPortIndex_Type = Integer32
_PtpPortIndex_Object = MibTableColumn
ptpPortIndex = _PtpPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 41, 5, 1, 1),
    _PtpPortIndex_Type()
)
ptpPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpPortIndex.setStatus("current")


class _PtpPortEnable_Type(Integer32):
    """Custom type ptpPortEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_PtpPortEnable_Type.__name__ = "Integer32"
_PtpPortEnable_Object = MibTableColumn
ptpPortEnable = _PtpPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 41, 5, 1, 2),
    _PtpPortEnable_Type()
)
ptpPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptpPortEnable.setStatus("current")


class _PtpPortStatus_Type(Integer32):
    """Custom type ptpPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
        *(("ptpDisabled", 2),
          ("ptpFaulty", 1),
          ("ptpInitializing", 0),
          ("ptpListening", 3),
          ("ptpMaster", 5),
          ("ptpPassive", 6),
          ("ptpPreMaster", 4),
          ("ptpSlave", 8),
          ("ptpUncalibrated", 7))
    )


_PtpPortStatus_Type.__name__ = "Integer32"
_PtpPortStatus_Object = MibTableColumn
ptpPortStatus = _PtpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 41, 5, 1, 3),
    _PtpPortStatus_Type()
)
ptpPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpPortStatus.setStatus("current")
_Diagnosis_ObjectIdentity = ObjectIdentity
diagnosis = _Diagnosis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 42)
)
_LldpSetting_ObjectIdentity = ObjectIdentity
lldpSetting = _LldpSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 42, 1)
)


class _EnableLLDP_Type(Integer32):
    """Custom type enableLLDP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_EnableLLDP_Type.__name__ = "Integer32"
_EnableLLDP_Object = MibScalar
enableLLDP = _EnableLLDP_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 42, 1, 1),
    _EnableLLDP_Type()
)
enableLLDP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableLLDP.setStatus("current")
_LldpMSGInterval_Type = Integer32
_LldpMSGInterval_Object = MibScalar
lldpMSGInterval = _LldpMSGInterval_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 42, 1, 2),
    _LldpMSGInterval_Type()
)
lldpMSGInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpMSGInterval.setStatus("current")
_AgeTime_Type = Integer32
_AgeTime_Object = MibScalar
ageTime = _AgeTime_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 44),
    _AgeTime_Type()
)
ageTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ageTime.setStatus("current")
_GarpSetting_ObjectIdentity = ObjectIdentity
garpSetting = _GarpSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 45)
)
_JoinTime_Type = Integer32
_JoinTime_Object = MibScalar
joinTime = _JoinTime_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 45, 1),
    _JoinTime_Type()
)
joinTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    joinTime.setStatus("current")
_LeaveTime_Type = Integer32
_LeaveTime_Object = MibScalar
leaveTime = _LeaveTime_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 45, 2),
    _LeaveTime_Type()
)
leaveTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    leaveTime.setStatus("current")
_LeaveAllTime_Type = Integer32
_LeaveAllTime_Object = MibScalar
leaveAllTime = _LeaveAllTime_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 45, 3),
    _LeaveAllTime_Type()
)
leaveAllTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    leaveAllTime.setStatus("current")
_Eventlog_ObjectIdentity = ObjectIdentity
eventlog = _Eventlog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 46)
)
_EventlogTable_Object = MibTable
eventlogTable = _EventlogTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 46, 1)
)
if mibBuilder.loadTexts:
    eventlogTable.setStatus("current")
_EventlogEntry_Object = MibTableRow
eventlogEntry = _EventlogEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 46, 1, 1)
)
eventlogEntry.setIndexNames(
    (0, "MOXA-IKS6726A-MIB", "eventlogIndex"),
)
if mibBuilder.loadTexts:
    eventlogEntry.setStatus("current")
_EventlogIndex_Type = Integer32
_EventlogIndex_Object = MibTableColumn
eventlogIndex = _EventlogIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 46, 1, 1, 1),
    _EventlogIndex_Type()
)
eventlogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventlogIndex.setStatus("current")
_EventlogBootup_Type = Integer32
_EventlogBootup_Object = MibTableColumn
eventlogBootup = _EventlogBootup_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 46, 1, 1, 2),
    _EventlogBootup_Type()
)
eventlogBootup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventlogBootup.setStatus("current")
_EventlogDate_Type = DisplayString
_EventlogDate_Object = MibTableColumn
eventlogDate = _EventlogDate_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 46, 1, 1, 3),
    _EventlogDate_Type()
)
eventlogDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventlogDate.setStatus("current")
_EventlogTime_Type = DisplayString
_EventlogTime_Object = MibTableColumn
eventlogTime = _EventlogTime_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 46, 1, 1, 4),
    _EventlogTime_Type()
)
eventlogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventlogTime.setStatus("current")
_EventlogUptime_Type = DisplayString
_EventlogUptime_Object = MibTableColumn
eventlogUptime = _EventlogUptime_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 46, 1, 1, 5),
    _EventlogUptime_Type()
)
eventlogUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventlogUptime.setStatus("current")
_EventlogEvent_Type = DisplayString
_EventlogEvent_Object = MibTableColumn
eventlogEvent = _EventlogEvent_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 46, 1, 1, 6),
    _EventlogEvent_Type()
)
eventlogEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eventlogEvent.setStatus("current")


class _EventlogClear_Type(Integer32):
    """Custom type eventlogClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("noop", 0))
    )


_EventlogClear_Type.__name__ = "Integer32"
_EventlogClear_Object = MibScalar
eventlogClear = _EventlogClear_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 46, 2),
    _EventlogClear_Type()
)
eventlogClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eventlogClear.setStatus("current")
_IndustrialProtocol_ObjectIdentity = ObjectIdentity
industrialProtocol = _IndustrialProtocol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 47)
)
_EipSetting_ObjectIdentity = ObjectIdentity
eipSetting = _EipSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 47, 1)
)


class _EnableEtherNetIP_Type(Integer32):
    """Custom type enableEtherNetIP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_EnableEtherNetIP_Type.__name__ = "Integer32"
_EnableEtherNetIP_Object = MibScalar
enableEtherNetIP = _EnableEtherNetIP_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 47, 1, 1),
    _EnableEtherNetIP_Type()
)
enableEtherNetIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableEtherNetIP.setStatus("current")
_ModbusTCPSetting_ObjectIdentity = ObjectIdentity
modbusTCPSetting = _ModbusTCPSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 47, 2)
)


class _EnableModbusTCP_Type(Integer32):
    """Custom type enableModbusTCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_EnableModbusTCP_Type.__name__ = "Integer32"
_EnableModbusTCP_Object = MibScalar
enableModbusTCP = _EnableModbusTCP_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 47, 2, 1),
    _EnableModbusTCP_Type()
)
enableModbusTCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableModbusTCP.setStatus("current")
_ProfinetioSetting_ObjectIdentity = ObjectIdentity
profinetioSetting = _ProfinetioSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 47, 3)
)


class _EnableProfinetIO_Type(Integer32):
    """Custom type enableProfinetIO based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_EnableProfinetIO_Type.__name__ = "Integer32"
_EnableProfinetIO_Object = MibScalar
enableProfinetIO = _EnableProfinetIO_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 47, 3, 1),
    _EnableProfinetIO_Type()
)
enableProfinetIO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableProfinetIO.setStatus("current")


class _EnableFactoryDefault_Type(Integer32):
    """Custom type enableFactoryDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("activate", 1)
    )


_EnableFactoryDefault_Type.__name__ = "Integer32"
_EnableFactoryDefault_Object = MibScalar
enableFactoryDefault = _EnableFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 48),
    _EnableFactoryDefault_Type()
)
enableFactoryDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    enableFactoryDefault.setStatus("current")


class _ConsoleLoginMode_Type(Integer32):
    """Custom type consoleLoginMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cli", 1),
          ("menu", 0))
    )


_ConsoleLoginMode_Type.__name__ = "Integer32"
_ConsoleLoginMode_Object = MibScalar
consoleLoginMode = _ConsoleLoginMode_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 51),
    _ConsoleLoginMode_Type()
)
consoleLoginMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consoleLoginMode.setStatus("current")
_CpuLoading5s_Type = Integer32
_CpuLoading5s_Object = MibScalar
cpuLoading5s = _CpuLoading5s_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 53),
    _CpuLoading5s_Type()
)
cpuLoading5s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuLoading5s.setStatus("current")
_CpuLoading30s_Type = Integer32
_CpuLoading30s_Object = MibScalar
cpuLoading30s = _CpuLoading30s_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 54),
    _CpuLoading30s_Type()
)
cpuLoading30s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuLoading30s.setStatus("current")
_CpuLoading300s_Type = Integer32
_CpuLoading300s_Object = MibScalar
cpuLoading300s = _CpuLoading300s_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 55),
    _CpuLoading300s_Type()
)
cpuLoading300s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuLoading300s.setStatus("current")
_TotalMemory_Type = Integer32
_TotalMemory_Object = MibScalar
totalMemory = _TotalMemory_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 56),
    _TotalMemory_Type()
)
totalMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalMemory.setStatus("current")
_FreeMemory_Type = Integer32
_FreeMemory_Object = MibScalar
freeMemory = _FreeMemory_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 57),
    _FreeMemory_Type()
)
freeMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    freeMemory.setStatus("current")
_UsedMemory_Type = Integer32
_UsedMemory_Object = MibScalar
usedMemory = _UsedMemory_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 58),
    _UsedMemory_Type()
)
usedMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usedMemory.setStatus("current")
_MemoryUsage_Type = Integer32
_MemoryUsage_Object = MibScalar
memoryUsage = _MemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 59),
    _MemoryUsage_Type()
)
memoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryUsage.setStatus("current")


class _LoopProtection_Type(Integer32):
    """Custom type loopProtection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_LoopProtection_Type.__name__ = "Integer32"
_LoopProtection_Object = MibScalar
loopProtection = _LoopProtection_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 61),
    _LoopProtection_Type()
)
loopProtection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    loopProtection.setStatus("current")
_EventSettings_ObjectIdentity = ObjectIdentity
eventSettings = _EventSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 62)
)
_SystemEventSettingsTable_Object = MibTable
systemEventSettingsTable = _SystemEventSettingsTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 62, 1)
)
if mibBuilder.loadTexts:
    systemEventSettingsTable.setStatus("current")
_SystemEventSettingsEntry_Object = MibTableRow
systemEventSettingsEntry = _SystemEventSettingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 62, 1, 1)
)
systemEventSettingsEntry.setIndexNames(
    (0, "MOXA-IKS6726A-MIB", "systemEventIndex"),
)
if mibBuilder.loadTexts:
    systemEventSettingsEntry.setStatus("current")
_SystemEventIndex_Type = Integer32
_SystemEventIndex_Object = MibTableColumn
systemEventIndex = _SystemEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 62, 1, 1, 1),
    _SystemEventIndex_Type()
)
systemEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemEventIndex.setStatus("current")


class _SystemEventActive_Type(Integer32):
    """Custom type systemEventActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0))
    )


_SystemEventActive_Type.__name__ = "Integer32"
_SystemEventActive_Object = MibTableColumn
systemEventActive = _SystemEventActive_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 62, 1, 1, 2),
    _SystemEventActive_Type()
)
systemEventActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemEventActive.setStatus("current")
_SystemEventName_Type = DisplayString
_SystemEventName_Object = MibTableColumn
systemEventName = _SystemEventName_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 62, 1, 1, 3),
    _SystemEventName_Type()
)
systemEventName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemEventName.setStatus("current")


class _SystemEventSupport_Type(Integer32):
    """Custom type systemEventSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              28,
              30,
              31)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("support-Email-Relay1", 10),
          ("support-Email-Relay2", 18),
          ("support-Email-Syslog", 6),
          ("support-Email-Syslog-Relay1", 14),
          ("support-Email-Syslog-Relay1-Relay2", 30),
          ("support-Email-Syslog-Relay2", 22),
          ("support-Email-only", 2),
          ("support-Relay1-Relay2", 24),
          ("support-Relay1-only", 8),
          ("support-Relay2-only", 16),
          ("support-SNMP-Trap-Email", 3),
          ("support-SNMPTrap-Email-Relay1", 11),
          ("support-SNMPTrap-Email-Relay2", 19),
          ("support-SNMPTrap-Email-Syslog", 7),
          ("support-SNMPTrap-Email-Syslog-Relay1", 15),
          ("support-SNMPTrap-Email-Syslog-Relay2", 23),
          ("support-SNMPTrap-Relay1", 9),
          ("support-SNMPTrap-Relay1-Relay2", 25),
          ("support-SNMPTrap-Relay2", 17),
          ("support-SNMPTrap-Syslog", 5),
          ("support-SNMPTrap-Syslog-Relay1", 13),
          ("support-SNMPTrap-Syslog-Relay2", 21),
          ("support-SNMPTrap-only", 1),
          ("support-Syslog-Relay1", 12),
          ("support-Syslog-Relay1-Relay2", 28),
          ("support-Syslog-Relay2", 20),
          ("support-Syslog-only", 4),
          ("support-all-SNMPTrap-Email-Syslog-Relay1-Relay2", 31))
    )


_SystemEventSupport_Type.__name__ = "Integer32"
_SystemEventSupport_Object = MibTableColumn
systemEventSupport = _SystemEventSupport_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 62, 1, 1, 4),
    _SystemEventSupport_Type()
)
systemEventSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemEventSupport.setStatus("current")


class _SystemEventModuleEnable_Type(Integer32):
    """Custom type systemEventModuleEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              28,
              30,
              31)
        )
    )
    namedValues = NamedValues(
        *(("enable-All-SNMPTrap-Email-Syslog-Relay1-Relay2", 31),
          ("enable-Email-Relay1", 10),
          ("enable-Email-Relay2", 18),
          ("enable-Email-Syslog", 6),
          ("enable-Email-Syslog-Relay1", 14),
          ("enable-Email-Syslog-Relay1-Relay2", 30),
          ("enable-Email-Syslog-Relay2", 22),
          ("enable-Email-only", 2),
          ("enable-Relay1-Relay2", 24),
          ("enable-Relay1-only", 8),
          ("enable-Relay2-only", 16),
          ("enable-SNMPTrap-Email", 3),
          ("enable-SNMPTrap-Email-Relay1", 11),
          ("enable-SNMPTrap-Email-Relay2", 19),
          ("enable-SNMPTrap-Email-Syslog", 7),
          ("enable-SNMPTrap-Email-Syslog-Relay1", 15),
          ("enable-SNMPTrap-Email-Syslog-Relay2", 23),
          ("enable-SNMPTrap-Relay1", 9),
          ("enable-SNMPTrap-Relay1-Relay2", 25),
          ("enable-SNMPTrap-Relay2", 17),
          ("enable-SNMPTrap-Syslog", 5),
          ("enable-SNMPTrap-Syslog-Relay1", 13),
          ("enable-SNMPTrap-Syslog-Relay2", 21),
          ("enable-SNMPTrap-only", 1),
          ("enable-Syslog-Relay1", 12),
          ("enable-Syslog-Relay1-Relay2", 28),
          ("enable-Syslog-Relay2", 20),
          ("enable-Syslog-only", 4),
          ("none", 0))
    )


_SystemEventModuleEnable_Type.__name__ = "Integer32"
_SystemEventModuleEnable_Object = MibTableColumn
systemEventModuleEnable = _SystemEventModuleEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 62, 1, 1, 5),
    _SystemEventModuleEnable_Type()
)
systemEventModuleEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemEventModuleEnable.setStatus("current")


class _SystemEventSeverity_Type(Integer32):
    """Custom type systemEventSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("alert", 1),
          ("critical", 2),
          ("debug", 7),
          ("emergency", 0),
          ("error", 3),
          ("information", 6),
          ("notice", 5),
          ("warning", 4))
    )


_SystemEventSeverity_Type.__name__ = "Integer32"
_SystemEventSeverity_Object = MibTableColumn
systemEventSeverity = _SystemEventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 62, 1, 1, 6),
    _SystemEventSeverity_Type()
)
systemEventSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systemEventSeverity.setStatus("current")
_PortEventSettingsTable_Object = MibTable
portEventSettingsTable = _PortEventSettingsTable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 62, 2)
)
if mibBuilder.loadTexts:
    portEventSettingsTable.setStatus("current")
_PortEventSettingsEntry_Object = MibTableRow
portEventSettingsEntry = _PortEventSettingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 62, 2, 1)
)
portEventSettingsEntry.setIndexNames(
    (0, "MOXA-IKS6726A-MIB", "portEventIndex"),
)
if mibBuilder.loadTexts:
    portEventSettingsEntry.setStatus("current")
_PortEventIndex_Type = Integer32
_PortEventIndex_Object = MibTableColumn
portEventIndex = _PortEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 62, 2, 1, 1),
    _PortEventIndex_Type()
)
portEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portEventIndex.setStatus("current")
_PortEventLabel_Type = DisplayString
_PortEventLabel_Object = MibTableColumn
portEventLabel = _PortEventLabel_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 62, 2, 1, 2),
    _PortEventLabel_Type()
)
portEventLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portEventLabel.setStatus("current")


class _PortEventActive_Type(Integer32):
    """Custom type portEventActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0))
    )


_PortEventActive_Type.__name__ = "Integer32"
_PortEventActive_Object = MibTableColumn
portEventActive = _PortEventActive_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 62, 2, 1, 3),
    _PortEventActive_Type()
)
portEventActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portEventActive.setStatus("current")


class _PortEventEnable_Type(Integer32):
    """Custom type portEventEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("enable-All-LinkOn-LinkOff-TrafficOverload", 7),
          ("enable-LinkOff-TrafficOverload", 6),
          ("enable-LinkOff-only", 2),
          ("enable-LinkOn-LinkOff", 3),
          ("enable-LinkOn-TrafficOverload", 5),
          ("enable-LinkOn-only", 1),
          ("enable-TrafficOverload-only", 4),
          ("none", 0))
    )


_PortEventEnable_Type.__name__ = "Integer32"
_PortEventEnable_Object = MibTableColumn
portEventEnable = _PortEventEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 62, 2, 1, 4),
    _PortEventEnable_Type()
)
portEventEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portEventEnable.setStatus("current")


class _PortEventTrafficThreshold_Type(Integer32):
    """Custom type portEventTrafficThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PortEventTrafficThreshold_Type.__name__ = "Integer32"
_PortEventTrafficThreshold_Object = MibTableColumn
portEventTrafficThreshold = _PortEventTrafficThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 62, 2, 1, 5),
    _PortEventTrafficThreshold_Type()
)
portEventTrafficThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portEventTrafficThreshold.setStatus("current")


class _PortEventTrafficDuration_Type(Integer32):
    """Custom type portEventTrafficDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_PortEventTrafficDuration_Type.__name__ = "Integer32"
_PortEventTrafficDuration_Object = MibTableColumn
portEventTrafficDuration = _PortEventTrafficDuration_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 62, 2, 1, 6),
    _PortEventTrafficDuration_Type()
)
portEventTrafficDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portEventTrafficDuration.setStatus("current")


class _PortEventModuleEnable_Type(Integer32):
    """Custom type portEventModuleEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              28,
              30,
              31)
        )
    )
    namedValues = NamedValues(
        *(("enable-All-SNMPTrap-Email-Syslog-Relay1-Relay2", 31),
          ("enable-Email-Relay1", 10),
          ("enable-Email-Relay2", 18),
          ("enable-Email-Syslog", 6),
          ("enable-Email-Syslog-Relay1", 14),
          ("enable-Email-Syslog-Relay1-Relay2", 30),
          ("enable-Email-Syslog-Relay2", 22),
          ("enable-Email-only", 2),
          ("enable-Relay1-Relay2", 24),
          ("enable-Relay1-only", 8),
          ("enable-Relay2-only", 16),
          ("enable-SNMPTrap-Email", 3),
          ("enable-SNMPTrap-Email-Relay1", 11),
          ("enable-SNMPTrap-Email-Relay2", 19),
          ("enable-SNMPTrap-Email-Syslog", 7),
          ("enable-SNMPTrap-Email-Syslog-Relay1", 15),
          ("enable-SNMPTrap-Email-Syslog-Relay2", 23),
          ("enable-SNMPTrap-Relay1", 9),
          ("enable-SNMPTrap-Relay1-Relay2", 25),
          ("enable-SNMPTrap-Relay2", 17),
          ("enable-SNMPTrap-Syslog", 5),
          ("enable-SNMPTrap-Syslog-Relay1", 13),
          ("enable-SNMPTrap-Syslog-Relay2", 21),
          ("enable-SNMPTrap-only", 1),
          ("enable-Syslog-Relay1", 12),
          ("enable-Syslog-Relay1-Relay2", 28),
          ("enable-Syslog-Relay2", 20),
          ("enable-Syslog-only", 4),
          ("none", 0))
    )


_PortEventModuleEnable_Type.__name__ = "Integer32"
_PortEventModuleEnable_Object = MibTableColumn
portEventModuleEnable = _PortEventModuleEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 62, 2, 1, 7),
    _PortEventModuleEnable_Type()
)
portEventModuleEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portEventModuleEnable.setStatus("current")


class _PortEventSeverity_Type(Integer32):
    """Custom type portEventSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("alert", 1),
          ("critical", 2),
          ("debug", 7),
          ("emergency", 0),
          ("error", 3),
          ("information", 6),
          ("notice", 5),
          ("warning", 4))
    )


_PortEventSeverity_Type.__name__ = "Integer32"
_PortEventSeverity_Object = MibTableColumn
portEventSeverity = _PortEventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 62, 2, 1, 8),
    _PortEventSeverity_Type()
)
portEventSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portEventSeverity.setStatus("current")
_ManagementInterface_ObjectIdentity = ObjectIdentity
managementInterface = _ManagementInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 63)
)


class _HttpEnable_Type(Integer32):
    """Custom type httpEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_HttpEnable_Type.__name__ = "Integer32"
_HttpEnable_Object = MibScalar
httpEnable = _HttpEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 63, 1),
    _HttpEnable_Type()
)
httpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpEnable.setStatus("current")


class _HttpPort_Type(Integer32):
    """Custom type httpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HttpPort_Type.__name__ = "Integer32"
_HttpPort_Object = MibScalar
httpPort = _HttpPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 63, 2),
    _HttpPort_Type()
)
httpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    httpPort.setStatus("current")


class _SslEnable_Type(Integer32):
    """Custom type sslEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SslEnable_Type.__name__ = "Integer32"
_SslEnable_Object = MibScalar
sslEnable = _SslEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 63, 3),
    _SslEnable_Type()
)
sslEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sslEnable.setStatus("current")


class _SslPort_Type(Integer32):
    """Custom type sslPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SslPort_Type.__name__ = "Integer32"
_SslPort_Object = MibScalar
sslPort = _SslPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 63, 4),
    _SslPort_Type()
)
sslPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sslPort.setStatus("current")


class _TelnetEnable_Type(Integer32):
    """Custom type telnetEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_TelnetEnable_Type.__name__ = "Integer32"
_TelnetEnable_Object = MibScalar
telnetEnable = _TelnetEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 63, 5),
    _TelnetEnable_Type()
)
telnetEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetEnable.setStatus("current")


class _TelnetPort_Type(Integer32):
    """Custom type telnetPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TelnetPort_Type.__name__ = "Integer32"
_TelnetPort_Object = MibScalar
telnetPort = _TelnetPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 63, 6),
    _TelnetPort_Type()
)
telnetPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetPort.setStatus("current")


class _SshEnable_Type(Integer32):
    """Custom type sshEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SshEnable_Type.__name__ = "Integer32"
_SshEnable_Object = MibScalar
sshEnable = _SshEnable_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 63, 7),
    _SshEnable_Type()
)
sshEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshEnable.setStatus("current")


class _SshPort_Type(Integer32):
    """Custom type sshPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SshPort_Type.__name__ = "Integer32"
_SshPort_Object = MibScalar
sshPort = _SshPort_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 63, 8),
    _SshPort_Type()
)
sshPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshPort.setStatus("current")


class _WebTimeout_Type(Integer32):
    """Custom type webTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_WebTimeout_Type.__name__ = "Integer32"
_WebTimeout_Object = MibScalar
webTimeout = _WebTimeout_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 63, 9),
    _WebTimeout_Type()
)
webTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    webTimeout.setStatus("current")
_SwitchLocator_ObjectIdentity = ObjectIdentity
switchLocator = _SwitchLocator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 64)
)


class _BlinkingLocatorLED_Type(Integer32):
    """Custom type blinkingLocatorLED based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_BlinkingLocatorLED_Type.__name__ = "Integer32"
_BlinkingLocatorLED_Object = MibScalar
blinkingLocatorLED = _BlinkingLocatorLED_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 64, 1),
    _BlinkingLocatorLED_Type()
)
blinkingLocatorLED.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blinkingLocatorLED.setStatus("current")
_DisableLocatorLEDTime_Type = Integer32
_DisableLocatorLEDTime_Object = MibScalar
disableLocatorLEDTime = _DisableLocatorLEDTime_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 64, 2),
    _DisableLocatorLEDTime_Type()
)
disableLocatorLEDTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    disableLocatorLEDTime.setStatus("current")
_UiVersion_Type = Integer32
_UiVersion_Object = MibScalar
uiVersion = _UiVersion_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 1, 65),
    _UiVersion_Type()
)
uiVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uiVersion.setStatus("current")
_SwTraps_ObjectIdentity = ObjectIdentity
swTraps = _SwTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 2)
)


class _VarconfigChangeTrap_Type(Integer32):
    """Custom type varconfigChangeTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("configChanged", 2),
          ("none", 1))
    )


_VarconfigChangeTrap_Type.__name__ = "Integer32"
_VarconfigChangeTrap_Object = MibScalar
varconfigChangeTrap = _VarconfigChangeTrap_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 2, 1),
    _VarconfigChangeTrap_Type()
)
varconfigChangeTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    varconfigChangeTrap.setStatus("current")


class _Varpower1Trap_Type(Integer32):
    """Custom type varpower1Trap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("off2on", 3),
          ("on2off", 2))
    )


_Varpower1Trap_Type.__name__ = "Integer32"
_Varpower1Trap_Object = MibScalar
varpower1Trap = _Varpower1Trap_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 2, 2),
    _Varpower1Trap_Type()
)
varpower1Trap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    varpower1Trap.setStatus("current")


class _Varpower2Trap_Type(Integer32):
    """Custom type varpower2Trap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("off2on", 3),
          ("on2off", 2))
    )


_Varpower2Trap_Type.__name__ = "Integer32"
_Varpower2Trap_Object = MibScalar
varpower2Trap = _Varpower2Trap_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 2, 3),
    _Varpower2Trap_Type()
)
varpower2Trap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    varpower2Trap.setStatus("current")
_VartrafficOverloadTrap_Type = Integer32
_VartrafficOverloadTrap_Object = MibScalar
vartrafficOverloadTrap = _VartrafficOverloadTrap_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 2, 4),
    _VartrafficOverloadTrap_Type()
)
vartrafficOverloadTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vartrafficOverloadTrap.setStatus("current")


class _VarredundancyTopologyChangedTrap_Type(Integer32):
    """Custom type varredundancyTopologyChangedTrap based on Integer32"""
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
        *(("none", 1),
          ("topologyChanged", 2),
          ("topologyChangedTurboChainHead", 3),
          ("topologyChangedTurboChainTail", 4))
    )


_VarredundancyTopologyChangedTrap_Type.__name__ = "Integer32"
_VarredundancyTopologyChangedTrap_Object = MibScalar
varredundancyTopologyChangedTrap = _VarredundancyTopologyChangedTrap_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 2, 5),
    _VarredundancyTopologyChangedTrap_Type()
)
varredundancyTopologyChangedTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    varredundancyTopologyChangedTrap.setStatus("current")


class _VarturboRingCouplingPortChangedTrap_Type(Integer32):
    """Custom type varturboRingCouplingPortChangedTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("couplingPortChanged", 2),
          ("none", 1))
    )


_VarturboRingCouplingPortChangedTrap_Type.__name__ = "Integer32"
_VarturboRingCouplingPortChangedTrap_Object = MibScalar
varturboRingCouplingPortChangedTrap = _VarturboRingCouplingPortChangedTrap_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 2, 6),
    _VarturboRingCouplingPortChangedTrap_Type()
)
varturboRingCouplingPortChangedTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    varturboRingCouplingPortChangedTrap.setStatus("current")


class _VarturboRingMasterChangedTrap_Type(Integer32):
    """Custom type varturboRingMasterChangedTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("ringMasterChanged", 2))
    )


_VarturboRingMasterChangedTrap_Type.__name__ = "Integer32"
_VarturboRingMasterChangedTrap_Object = MibScalar
varturboRingMasterChangedTrap = _VarturboRingMasterChangedTrap_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 2, 7),
    _VarturboRingMasterChangedTrap_Type()
)
varturboRingMasterChangedTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    varturboRingMasterChangedTrap.setStatus("current")


class _VarPoEWarningTrap_Type(Integer32):
    """Custom type varPoEWarningTrap based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("exceedSystemPowerBudget", 9),
          ("exceedSystemThreshold", 5),
          ("pdCheckFail", 2),
          ("pdOverCurrent", 1),
          ("pdPowerOff", 4),
          ("pdPowerOn", 3),
          ("pseFetBad", 6),
          ("pseOverTemperature", 7),
          ("pseVeeUvlo", 8))
    )


_VarPoEWarningTrap_Type.__name__ = "Integer32"
_VarPoEWarningTrap_Object = MibScalar
varPoEWarningTrap = _VarPoEWarningTrap_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 2, 16),
    _VarPoEWarningTrap_Type()
)
varPoEWarningTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    varPoEWarningTrap.setStatus("current")
_VarPortLoopDetectedTrap_Type = Integer32
_VarPortLoopDetectedTrap_Object = MibScalar
varPortLoopDetectedTrap = _VarPortLoopDetectedTrap_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 2, 17),
    _VarPortLoopDetectedTrap_Type()
)
varPortLoopDetectedTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    varPortLoopDetectedTrap.setStatus("current")


class _VarRateLimitedOnTrap_Type(Integer32):
    """Custom type varRateLimitedOnTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("rateLimitOFF", 3),
          ("rateLimitON", 2))
    )


_VarRateLimitedOnTrap_Type.__name__ = "Integer32"
_VarRateLimitedOnTrap_Object = MibScalar
varRateLimitedOnTrap = _VarRateLimitedOnTrap_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 2, 18),
    _VarRateLimitedOnTrap_Type()
)
varRateLimitedOnTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    varRateLimitedOnTrap.setStatus("current")
_VarLLDPChgTrap_Type = Integer32
_VarLLDPChgTrap_Object = MibScalar
varLLDPChgTrap = _VarLLDPChgTrap_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 2, 19),
    _VarLLDPChgTrap_Type()
)
varLLDPChgTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    varLLDPChgTrap.setStatus("current")


class _VarusbWarningTrap_Type(Integer32):
    """Custom type varusbWarningTrap based on Integer32"""
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
        *(("autoImportFail", 5),
          ("exportConfigFail", 3),
          ("exportLogFail", 4),
          ("isAttached", 6),
          ("isDetached", 7),
          ("noEnoughSpace", 1),
          ("unauthDevice", 2))
    )


_VarusbWarningTrap_Type.__name__ = "Integer32"
_VarusbWarningTrap_Object = MibScalar
varusbWarningTrap = _VarusbWarningTrap_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 2, 20),
    _VarusbWarningTrap_Type()
)
varusbWarningTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    varusbWarningTrap.setStatus("current")


class _VarturboRingMasterMismatchTrap_Type(Integer32):
    """Custom type varturboRingMasterMismatchTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("ringMasterMismatch", 2))
    )


_VarturboRingMasterMismatchTrap_Type.__name__ = "Integer32"
_VarturboRingMasterMismatchTrap_Object = MibScalar
varturboRingMasterMismatchTrap = _VarturboRingMasterMismatchTrap_Object(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 2, 22),
    _VarturboRingMasterMismatchTrap_Type()
)
varturboRingMasterMismatchTrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    varturboRingMasterMismatchTrap.setStatus("current")

# Managed Objects groups


# Notification objects

configChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 0, 1)
)
configChangeTrap.setObjects(
    ("MOXA-IKS6726A-MIB", "varconfigChangeTrap")
)
if mibBuilder.loadTexts:
    configChangeTrap.setStatus(
        "current"
    )

power1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 0, 2)
)
power1Trap.setObjects(
    ("MOXA-IKS6726A-MIB", "varpower1Trap")
)
if mibBuilder.loadTexts:
    power1Trap.setStatus(
        "current"
    )

power2Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 0, 3)
)
power2Trap.setObjects(
    ("MOXA-IKS6726A-MIB", "varpower2Trap")
)
if mibBuilder.loadTexts:
    power2Trap.setStatus(
        "current"
    )

trafficOverloadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 0, 4)
)
trafficOverloadTrap.setObjects(
    ("MOXA-IKS6726A-MIB", "vartrafficOverloadTrap")
)
if mibBuilder.loadTexts:
    trafficOverloadTrap.setStatus(
        "current"
    )

redundancyTopologyChangedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 0, 5)
)
redundancyTopologyChangedTrap.setObjects(
    ("MOXA-IKS6726A-MIB", "varredundancyTopologyChangedTrap")
)
if mibBuilder.loadTexts:
    redundancyTopologyChangedTrap.setStatus(
        "current"
    )

turboRingCouplingPortChangedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 0, 6)
)
turboRingCouplingPortChangedTrap.setObjects(
    ("MOXA-IKS6726A-MIB", "varturboRingCouplingPortChangedTrap")
)
if mibBuilder.loadTexts:
    turboRingCouplingPortChangedTrap.setStatus(
        "current"
    )

turboRingMasterChangedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 0, 7)
)
turboRingMasterChangedTrap.setObjects(
    ("MOXA-IKS6726A-MIB", "varturboRingMasterChangedTrap")
)
if mibBuilder.loadTexts:
    turboRingMasterChangedTrap.setStatus(
        "current"
    )

poeWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 0, 16)
)
poeWarningTrap.setObjects(
    ("MOXA-IKS6726A-MIB", "varPoEWarningTrap")
)
if mibBuilder.loadTexts:
    poeWarningTrap.setStatus(
        "current"
    )

portLoopDetectedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 0, 17)
)
portLoopDetectedTrap.setObjects(
    ("MOXA-IKS6726A-MIB", "varPortLoopDetectedTrap")
)
if mibBuilder.loadTexts:
    portLoopDetectedTrap.setStatus(
        "current"
    )

rateLimitedOnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 0, 18)
)
rateLimitedOnTrap.setObjects(
    ("MOXA-IKS6726A-MIB", "varRateLimitedOnTrap")
)
if mibBuilder.loadTexts:
    rateLimitedOnTrap.setStatus(
        "current"
    )

lldpChgTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 0, 19)
)
lldpChgTrap.setObjects(
    ("MOXA-IKS6726A-MIB", "varLLDPChgTrap")
)
if mibBuilder.loadTexts:
    lldpChgTrap.setStatus(
        "current"
    )

usbWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 0, 20)
)
usbWarningTrap.setObjects(
    ("MOXA-IKS6726A-MIB", "varusbWarningTrap")
)
if mibBuilder.loadTexts:
    usbWarningTrap.setStatus(
        "current"
    )

turboRingMasterMismatchTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8691, 7, 116, 0, 22)
)
turboRingMasterMismatchTrap.setObjects(
    ("MOXA-IKS6726A-MIB", "varturboRingMasterChangedTrap")
)
if mibBuilder.loadTexts:
    turboRingMasterMismatchTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MOXA-IKS6726A-MIB",
    **{"PortList": PortList,
       "moxa": moxa,
       "industrialEthernet": industrialEthernet,
       "iks6726A": iks6726A,
       "mibNotificationsPrefix": mibNotificationsPrefix,
       "configChangeTrap": configChangeTrap,
       "power1Trap": power1Trap,
       "power2Trap": power2Trap,
       "trafficOverloadTrap": trafficOverloadTrap,
       "redundancyTopologyChangedTrap": redundancyTopologyChangedTrap,
       "turboRingCouplingPortChangedTrap": turboRingCouplingPortChangedTrap,
       "turboRingMasterChangedTrap": turboRingMasterChangedTrap,
       "poeWarningTrap": poeWarningTrap,
       "portLoopDetectedTrap": portLoopDetectedTrap,
       "rateLimitedOnTrap": rateLimitedOnTrap,
       "lldpChgTrap": lldpChgTrap,
       "usbWarningTrap": usbWarningTrap,
       "turboRingMasterMismatchTrap": turboRingMasterMismatchTrap,
       "swMgmt": swMgmt,
       "numberOfPorts": numberOfPorts,
       "switchModel": switchModel,
       "firmwareVersion": firmwareVersion,
       "enableWebConfig": enableWebConfig,
       "enableTelnetConsole": enableTelnetConsole,
       "lineSwapRecovery": lineSwapRecovery,
       "networkSetting": networkSetting,
       "switchIpAddr": switchIpAddr,
       "switchIpMask": switchIpMask,
       "defaultGateway": defaultGateway,
       "enableAutoIpConfig": enableAutoIpConfig,
       "dnsServer1IpAddr": dnsServer1IpAddr,
       "snmpTrapCommunity": snmpTrapCommunity,
       "trapServerAddr": trapServerAddr,
       "dnsServer2IpAddr": dnsServer2IpAddr,
       "snmpReadCommunity": snmpReadCommunity,
       "snmpTrap2Community": snmpTrap2Community,
       "trap2ServerAddr": trap2ServerAddr,
       "snmpInformEnable": snmpInformEnable,
       "snmpInformRetries": snmpInformRetries,
       "snmpInformTimeout": snmpInformTimeout,
       "dhcpRetryPeriods": dhcpRetryPeriods,
       "dhcpRetryTimes": dhcpRetryTimes,
       "trapVersion": trapVersion,
       "portSetting": portSetting,
       "portTable": portTable,
       "portEntry": portEntry,
       "portIndex": portIndex,
       "portDesc": portDesc,
       "portEnable": portEnable,
       "portSpeed": portSpeed,
       "portMDI": portMDI,
       "portFDXFlowCtrl": portFDXFlowCtrl,
       "portName": portName,
       "monitor": monitor,
       "power1InputStatus": power1InputStatus,
       "power2InputStatus": power2InputStatus,
       "monitorPortTable": monitorPortTable,
       "monitorPortEntry": monitorPortEntry,
       "monitorLinkStatus": monitorLinkStatus,
       "monitorSpeed": monitorSpeed,
       "monitorAutoMDI": monitorAutoMDI,
       "monitorTraffic": monitorTraffic,
       "monitorFDXFlowCtrl": monitorFDXFlowCtrl,
       "monitorTxTraffic": monitorTxTraffic,
       "monitorRxTraffic": monitorRxTraffic,
       "monitorDiTable": monitorDiTable,
       "monitorDiEntry": monitorDiEntry,
       "diIndex": diIndex,
       "diInputStatus": diInputStatus,
       "monitorSFPTable": monitorSFPTable,
       "monitorSFPEntry": monitorSFPEntry,
       "sfpPort": sfpPort,
       "sfpModelName": sfpModelName,
       "sfpTemperature": sfpTemperature,
       "sfpVoltage": sfpVoltage,
       "sfpTxPower": sfpTxPower,
       "sfpRxPower": sfpRxPower,
       "powerConsumption": powerConsumption,
       "emailWarning": emailWarning,
       "emailService": emailService,
       "emailWarningMailServer": emailWarningMailServer,
       "emailWarningFirstEmailAddr": emailWarningFirstEmailAddr,
       "emailWarningSecondEmailAddr": emailWarningSecondEmailAddr,
       "emailWarningThirdEmailAddr": emailWarningThirdEmailAddr,
       "emailWarningFourthEmailAddr": emailWarningFourthEmailAddr,
       "emailWarningSMTPPort": emailWarningSMTPPort,
       "setDeviceIp": setDeviceIp,
       "setDevIpTable": setDevIpTable,
       "setDevIpEntry": setDevIpEntry,
       "setDevIpIndex": setDevIpIndex,
       "setDevIpCurrentIpofDevice": setDevIpCurrentIpofDevice,
       "setDevIpPresentBy": setDevIpPresentBy,
       "setDevIpDedicatedIp": setDevIpDedicatedIp,
       "mirroring": mirroring,
       "targetPort": targetPort,
       "mirroringPort": mirroringPort,
       "monitorDirection": monitorDirection,
       "portTrunking": portTrunking,
       "trunkSettingTable": trunkSettingTable,
       "trunkSettingEntry": trunkSettingEntry,
       "trunkSettingIndex": trunkSettingIndex,
       "trunkType": trunkType,
       "trunkMemberPorts": trunkMemberPorts,
       "trunkTable": trunkTable,
       "trunkEntry": trunkEntry,
       "trunkIndex": trunkIndex,
       "trunkPort": trunkPort,
       "trunkStatus": trunkStatus,
       "commRedundancy": commRedundancy,
       "protocolOfRedundancySetup": protocolOfRedundancySetup,
       "turboRing": turboRing,
       "turboRingMaster": turboRingMaster,
       "turboRingMasterSetup": turboRingMasterSetup,
       "turboRingPortTable": turboRingPortTable,
       "turboRingPortEntry": turboRingPortEntry,
       "turboRingPortIndex": turboRingPortIndex,
       "turboRingPortStatus": turboRingPortStatus,
       "turboRingPortDesignatedBridge": turboRingPortDesignatedBridge,
       "turboRingPortDesignatedPort": turboRingPortDesignatedPort,
       "turboRingDesignatedMaster": turboRingDesignatedMaster,
       "turboRingRdntPort1": turboRingRdntPort1,
       "turboRingRdntPort2": turboRingRdntPort2,
       "turboRingEnableCoupling": turboRingEnableCoupling,
       "turboRingCouplingPort": turboRingCouplingPort,
       "turboRingCouplingPortStatus": turboRingCouplingPortStatus,
       "turboRingControlPort": turboRingControlPort,
       "turboRingControlPortStatus": turboRingControlPortStatus,
       "turboRingBrokenStatus": turboRingBrokenStatus,
       "spanningTree": spanningTree,
       "spanningTreeRoot": spanningTreeRoot,
       "spanningTreeBridgePriority": spanningTreeBridgePriority,
       "spanningTreeHelloTime": spanningTreeHelloTime,
       "spanningTreeMaxAge": spanningTreeMaxAge,
       "spanningTreeForwardingDelay": spanningTreeForwardingDelay,
       "spanningTreeTable": spanningTreeTable,
       "spanningTreeEntry": spanningTreeEntry,
       "spanningTreeIndex": spanningTreeIndex,
       "enableSpanningTree": enableSpanningTree,
       "spanningTreePortPriority": spanningTreePortPriority,
       "spanningTreePortCost": spanningTreePortCost,
       "spanningTreePortStatus": spanningTreePortStatus,
       "spanningTreePortEdge": spanningTreePortEdge,
       "activeProtocolOfRedundancy": activeProtocolOfRedundancy,
       "turboRingV2": turboRingV2,
       "turboRingV2Ring1": turboRingV2Ring1,
       "ringIndexRing1": ringIndexRing1,
       "ringEnableRing1": ringEnableRing1,
       "masterSetupRing1": masterSetupRing1,
       "masterStatusRing1": masterStatusRing1,
       "designatedMasterRing1": designatedMasterRing1,
       "rdnt1stPortRing1": rdnt1stPortRing1,
       "rdnt1stPortStatusRing1": rdnt1stPortStatusRing1,
       "rdnt2ndPortRing1": rdnt2ndPortRing1,
       "rdnt2ndPortStatusRing1": rdnt2ndPortStatusRing1,
       "brokenStatusRing1": brokenStatusRing1,
       "turboRingV2Ring2": turboRingV2Ring2,
       "ringIndexRing2": ringIndexRing2,
       "ringEnableRing2": ringEnableRing2,
       "masterSetupRing2": masterSetupRing2,
       "masterStatusRing2": masterStatusRing2,
       "designatedMasterRing2": designatedMasterRing2,
       "rdnt1stPortRing2": rdnt1stPortRing2,
       "rdnt1stPortStatusRing2": rdnt1stPortStatusRing2,
       "rdnt2ndPortRing2": rdnt2ndPortRing2,
       "rdnt2ndPortStatusRing2": rdnt2ndPortStatusRing2,
       "brokenStatusRing2": brokenStatusRing2,
       "turboRingV2Coupling": turboRingV2Coupling,
       "couplingEnable": couplingEnable,
       "couplingMode": couplingMode,
       "coupling1stPort": coupling1stPort,
       "coupling1stPortStatus": coupling1stPortStatus,
       "coupling2ndPort": coupling2ndPort,
       "coupling2ndPortStatus": coupling2ndPortStatus,
       "turboChain": turboChain,
       "turboChainRole": turboChainRole,
       "turboChainPort1": turboChainPort1,
       "turboChainPort2": turboChainPort2,
       "turboChainPort1Status": turboChainPort1Status,
       "turboChainPort2Status": turboChainPort2Status,
       "turboChainPort1PartnerBridge": turboChainPort1PartnerBridge,
       "turboChainPort2PartnerBridge": turboChainPort2PartnerBridge,
       "trafficPrioritization": trafficPrioritization,
       "qosClassification": qosClassification,
       "queuingMechanism": queuingMechanism,
       "qosPortTable": qosPortTable,
       "qosPortEntry": qosPortEntry,
       "inspectTos": inspectTos,
       "inspectCos": inspectCos,
       "portPriority": portPriority,
       "cosMapping": cosMapping,
       "cosMappingTable": cosMappingTable,
       "cosMappingEntry": cosMappingEntry,
       "cosTag": cosTag,
       "cosMappedPriority": cosMappedPriority,
       "tosMapping": tosMapping,
       "tosMappingTable": tosMappingTable,
       "tosMappingEntry": tosMappingEntry,
       "tosClass": tosClass,
       "tosMappedPriority": tosMappedPriority,
       "vlan": vlan,
       "vlanPortSettingTable": vlanPortSettingTable,
       "vlanPortSettingEntry": vlanPortSettingEntry,
       "portVlanType": portVlanType,
       "portDefaultVid": portDefaultVid,
       "portFixedVid": portFixedVid,
       "portForbiddenVid": portForbiddenVid,
       "portFixedVidUntag": portFixedVidUntag,
       "vlanTable": vlanTable,
       "vlanEntry": vlanEntry,
       "vlanId": vlanId,
       "joinedAccessPorts": joinedAccessPorts,
       "joinedTrunkPorts": joinedTrunkPorts,
       "joinedHybridPorts": joinedHybridPorts,
       "managementVlanId": managementVlanId,
       "vlanType": vlanType,
       "portbaseVlanSettingTable": portbaseVlanSettingTable,
       "portbaseVlanSettingEntry": portbaseVlanSettingEntry,
       "portbaseVlanSettingIndex": portbaseVlanSettingIndex,
       "portbaseVlanMemberPorts": portbaseVlanMemberPorts,
       "enableGvrp": enableGvrp,
       "multicastFiltering": multicastFiltering,
       "igmpSnooping": igmpSnooping,
       "querierQueryInterval": querierQueryInterval,
       "igmpSnoopingSettingTable": igmpSnoopingSettingTable,
       "igmpSnoopingSettingEntry": igmpSnoopingSettingEntry,
       "enableIgmpSnooping": enableIgmpSnooping,
       "enableQuerier": enableQuerier,
       "fixedMulticastQuerierPorts": fixedMulticastQuerierPorts,
       "learnedMulticastQuerierPorts": learnedMulticastQuerierPorts,
       "enableGlobalIgmpSnooping": enableGlobalIgmpSnooping,
       "multicastFastForwarding": multicastFastForwarding,
       "staticMulticast": staticMulticast,
       "staticMulticastTable": staticMulticastTable,
       "staticMulticastEntry": staticMulticastEntry,
       "staticMulticastAddress": staticMulticastAddress,
       "staticMulticastPorts": staticMulticastPorts,
       "staticMulticastStatus": staticMulticastStatus,
       "gmrp": gmrp,
       "gmrpSettingTable": gmrpSettingTable,
       "gmrpSettingEntry": gmrpSettingEntry,
       "enableGMRP": enableGMRP,
       "gmrpTable": gmrpTable,
       "gmrpEntry": gmrpEntry,
       "gmrpMulticastGroup": gmrpMulticastGroup,
       "gmrpFixedPorts": gmrpFixedPorts,
       "gmrpLearnedPorts": gmrpLearnedPorts,
       "mfb": mfb,
       "mfbSettingTable": mfbSettingTable,
       "mfbSettingEntry": mfbSettingEntry,
       "filterBehavior": filterBehavior,
       "rateLimiting": rateLimiting,
       "normalModeRateLimitingTable": normalModeRateLimitingTable,
       "normalModeRateLimitingEntry": normalModeRateLimitingEntry,
       "ingressLimitRate": ingressLimitRate,
       "egressLimit": egressLimit,
       "broadcastStormProtection": broadcastStormProtection,
       "enableBcastStormProtection": enableBcastStormProtection,
       "bcastStormIncludeMcast": bcastStormIncludeMcast,
       "bcastStormIncludeUnkonwnMcastUcast": bcastStormIncludeUnkonwnMcastUcast,
       "unicastFilterBehavior": unicastFilterBehavior,
       "ufbIncludeUnkonwnUcast": ufbIncludeUnkonwnUcast,
       "portDisableMode": portDisableMode,
       "portDisableModePeriod": portDisableModePeriod,
       "portDisableModeTable": portDisableModeTable,
       "portDisableModeEntry": portDisableModeEntry,
       "ingressLimit": ingressLimit,
       "rateLimitingMode": rateLimitingMode,
       "security": security,
       "userLoginSetting": userLoginSetting,
       "userLoginServer": userLoginServer,
       "tacacsServerSetting": tacacsServerSetting,
       "tacacsLoginAuthServer": tacacsLoginAuthServer,
       "tacacsLoginAuthPort": tacacsLoginAuthPort,
       "tacacsLoginAuthSharedKey": tacacsLoginAuthSharedKey,
       "tacacsLoginAuthAuthType": tacacsLoginAuthAuthType,
       "tacacsLoginAuthTimeout": tacacsLoginAuthTimeout,
       "radiusServerSetting": radiusServerSetting,
       "radiusLoginAuthServer": radiusLoginAuthServer,
       "radiusLoginAuthPort": radiusLoginAuthPort,
       "radiusLoginAuthSharedKey": radiusLoginAuthSharedKey,
       "radiusLoginAuthAuthType": radiusLoginAuthAuthType,
       "radiusLoginAuthTimeout": radiusLoginAuthTimeout,
       "portAccessControl": portAccessControl,
       "staticPortLock": staticPortLock,
       "staticPortLockAddress": staticPortLockAddress,
       "staticPortLockPort": staticPortLockPort,
       "staticPortLockStatus": staticPortLockStatus,
       "dot1x": dot1x,
       "dataBaseOption": dataBaseOption,
       "dot1xReauthEnable": dot1xReauthEnable,
       "dot1xReauthPeriod": dot1xReauthPeriod,
       "dot1xSettingTable": dot1xSettingTable,
       "dot1xSettingEntry": dot1xSettingEntry,
       "enableDot1X": enableDot1X,
       "dot1xReauthTable": dot1xReauthTable,
       "dot1xReauthEntry": dot1xReauthEntry,
       "dot1xReauthPortIndex": dot1xReauthPortIndex,
       "dot1xReauth": dot1xReauth,
       "dot1xRadius": dot1xRadius,
       "dot1xSameAsAuthServer": dot1xSameAsAuthServer,
       "dot1x1stRadiusServer": dot1x1stRadiusServer,
       "dot1x1stRadiusPort": dot1x1stRadiusPort,
       "dot1x1stRadiusSharedKey": dot1x1stRadiusSharedKey,
       "dot1x2ndRadiusServer": dot1x2ndRadiusServer,
       "dot1x2ndRadiusPort": dot1x2ndRadiusPort,
       "dot1x2ndRadiusSharedKey": dot1x2ndRadiusSharedKey,
       "portAccessControlTable": portAccessControlTable,
       "portAccessControlEntry": portAccessControlEntry,
       "portAccessControlAddress": portAccessControlAddress,
       "portAccessControlPortNo": portAccessControlPortNo,
       "portAccessControlAccessStatus": portAccessControlAccessStatus,
       "portAccessControlStatus": portAccessControlStatus,
       "accessibleIP": accessibleIP,
       "enableAccessibleIP": enableAccessibleIP,
       "accessibleIpTable": accessibleIpTable,
       "accessibleIpEntry": accessibleIpEntry,
       "accessibleIpAddress": accessibleIpAddress,
       "accessibleIpNetMask": accessibleIpNetMask,
       "accessibleIpStatus": accessibleIpStatus,
       "sysFileUpdate": sysFileUpdate,
       "tftpServer": tftpServer,
       "firmwarePathName": firmwarePathName,
       "logPathName": logPathName,
       "confPathName": confPathName,
       "tftpUpdate": tftpUpdate,
       "timeSetting": timeSetting,
       "sysDateTime": sysDateTime,
       "calibratePeriod": calibratePeriod,
       "timeServer1": timeServer1,
       "timeServer2": timeServer2,
       "daylightSaving": daylightSaving,
       "startMonth": startMonth,
       "startWeek": startWeek,
       "startDay": startDay,
       "startHour": startHour,
       "endMonth": endMonth,
       "endWeek": endWeek,
       "endDay": endDay,
       "endHour": endHour,
       "offsetHours": offsetHours,
       "enableNTPServer": enableNTPServer,
       "clockSource": clockSource,
       "backupMediaSetting": backupMediaSetting,
       "abc02Status": abc02Status,
       "abc02AutoImportConfig": abc02AutoImportConfig,
       "abc02AutoExportConfig": abc02AutoExportConfig,
       "abc02AutoExportLog": abc02AutoExportLog,
       "enableWarmStart": enableWarmStart,
       "syslogSetting": syslogSetting,
       "syslogServer1": syslogServer1,
       "syslogServer1port": syslogServer1port,
       "syslogServer2": syslogServer2,
       "syslogServer2port": syslogServer2port,
       "syslogServer3": syslogServer3,
       "syslogServer3port": syslogServer3port,
       "dhcpRelayAgentSetting": dhcpRelayAgentSetting,
       "dhcpServer1": dhcpServer1,
       "dhcpServer2": dhcpServer2,
       "dhcpServer3": dhcpServer3,
       "dhcpServer4": dhcpServer4,
       "option82Setting": option82Setting,
       "enableOption82": enableOption82,
       "option82Type": option82Type,
       "option82Value": option82Value,
       "option82ValueDisplay": option82ValueDisplay,
       "dhcpFunctionTable": dhcpFunctionTable,
       "dhcpFunctionTableEntry": dhcpFunctionTableEntry,
       "dhcpPortIndex": dhcpPortIndex,
       "circuitID": circuitID,
       "option82Enable": option82Enable,
       "ieee1588Setting": ieee1588Setting,
       "ptpv1Setting": ptpv1Setting,
       "enablePtpv1": enablePtpv1,
       "clockModev1": clockModev1,
       "syncIntervalv1": syncIntervalv1,
       "subDomainNamev1": subDomainNamev1,
       "preferMasterv1": preferMasterv1,
       "ptpv2Setting": ptpv2Setting,
       "enablePtp": enablePtp,
       "clockMode": clockMode,
       "transport": transport,
       "syncInterval": syncInterval,
       "logMinDelayReqInterval": logMinDelayReqInterval,
       "logMinPdelayReqInterval": logMinPdelayReqInterval,
       "logAnnounceInterval": logAnnounceInterval,
       "announceReceiptTimeout": announceReceiptTimeout,
       "priority1": priority1,
       "priority2": priority2,
       "clockClass": clockClass,
       "domainNumber": domainNumber,
       "localUtcOffset": localUtcOffset,
       "localUtcOffsetValid": localUtcOffsetValid,
       "localLeap59": localLeap59,
       "localLeap61": localLeap61,
       "localPtpTimescale": localPtpTimescale,
       "localArbTime": localArbTime,
       "ptpv1Status": ptpv1Status,
       "offsetToMasterv1": offsetToMasterv1,
       "meanPathDelayv1": meanPathDelayv1,
       "grandMasterUuidv1": grandMasterUuidv1,
       "parentUuidv1": parentUuidv1,
       "clockStratumv1": clockStratumv1,
       "clockIdentifierv1": clockIdentifierv1,
       "ptpv2Status": ptpv2Status,
       "offsetToMaster": offsetToMaster,
       "meanPathDelay": meanPathDelay,
       "parentIdentity": parentIdentity,
       "grandmasterIdentity": grandmasterIdentity,
       "grandmasterClockClass": grandmasterClockClass,
       "grandmasterClockAccuracy": grandmasterClockAccuracy,
       "grandmasterPriority1": grandmasterPriority1,
       "grandmasterPriority2": grandmasterPriority2,
       "stepsRemoved": stepsRemoved,
       "currentUtcOffset": currentUtcOffset,
       "currentUtcOffsetValid": currentUtcOffsetValid,
       "leap59": leap59,
       "leap61": leap61,
       "ptpTimescale": ptpTimescale,
       "timesource": timesource,
       "ptpPortTable": ptpPortTable,
       "ptpPortEntry": ptpPortEntry,
       "ptpPortIndex": ptpPortIndex,
       "ptpPortEnable": ptpPortEnable,
       "ptpPortStatus": ptpPortStatus,
       "diagnosis": diagnosis,
       "lldpSetting": lldpSetting,
       "enableLLDP": enableLLDP,
       "lldpMSGInterval": lldpMSGInterval,
       "ageTime": ageTime,
       "garpSetting": garpSetting,
       "joinTime": joinTime,
       "leaveTime": leaveTime,
       "leaveAllTime": leaveAllTime,
       "eventlog": eventlog,
       "eventlogTable": eventlogTable,
       "eventlogEntry": eventlogEntry,
       "eventlogIndex": eventlogIndex,
       "eventlogBootup": eventlogBootup,
       "eventlogDate": eventlogDate,
       "eventlogTime": eventlogTime,
       "eventlogUptime": eventlogUptime,
       "eventlogEvent": eventlogEvent,
       "eventlogClear": eventlogClear,
       "industrialProtocol": industrialProtocol,
       "eipSetting": eipSetting,
       "enableEtherNetIP": enableEtherNetIP,
       "modbusTCPSetting": modbusTCPSetting,
       "enableModbusTCP": enableModbusTCP,
       "profinetioSetting": profinetioSetting,
       "enableProfinetIO": enableProfinetIO,
       "enableFactoryDefault": enableFactoryDefault,
       "consoleLoginMode": consoleLoginMode,
       "cpuLoading5s": cpuLoading5s,
       "cpuLoading30s": cpuLoading30s,
       "cpuLoading300s": cpuLoading300s,
       "totalMemory": totalMemory,
       "freeMemory": freeMemory,
       "usedMemory": usedMemory,
       "memoryUsage": memoryUsage,
       "loopProtection": loopProtection,
       "eventSettings": eventSettings,
       "systemEventSettingsTable": systemEventSettingsTable,
       "systemEventSettingsEntry": systemEventSettingsEntry,
       "systemEventIndex": systemEventIndex,
       "systemEventActive": systemEventActive,
       "systemEventName": systemEventName,
       "systemEventSupport": systemEventSupport,
       "systemEventModuleEnable": systemEventModuleEnable,
       "systemEventSeverity": systemEventSeverity,
       "portEventSettingsTable": portEventSettingsTable,
       "portEventSettingsEntry": portEventSettingsEntry,
       "portEventIndex": portEventIndex,
       "portEventLabel": portEventLabel,
       "portEventActive": portEventActive,
       "portEventEnable": portEventEnable,
       "portEventTrafficThreshold": portEventTrafficThreshold,
       "portEventTrafficDuration": portEventTrafficDuration,
       "portEventModuleEnable": portEventModuleEnable,
       "portEventSeverity": portEventSeverity,
       "managementInterface": managementInterface,
       "httpEnable": httpEnable,
       "httpPort": httpPort,
       "sslEnable": sslEnable,
       "sslPort": sslPort,
       "telnetEnable": telnetEnable,
       "telnetPort": telnetPort,
       "sshEnable": sshEnable,
       "sshPort": sshPort,
       "webTimeout": webTimeout,
       "switchLocator": switchLocator,
       "blinkingLocatorLED": blinkingLocatorLED,
       "disableLocatorLEDTime": disableLocatorLEDTime,
       "uiVersion": uiVersion,
       "swTraps": swTraps,
       "varconfigChangeTrap": varconfigChangeTrap,
       "varpower1Trap": varpower1Trap,
       "varpower2Trap": varpower2Trap,
       "vartrafficOverloadTrap": vartrafficOverloadTrap,
       "varredundancyTopologyChangedTrap": varredundancyTopologyChangedTrap,
       "varturboRingCouplingPortChangedTrap": varturboRingCouplingPortChangedTrap,
       "varturboRingMasterChangedTrap": varturboRingMasterChangedTrap,
       "varPoEWarningTrap": varPoEWarningTrap,
       "varPortLoopDetectedTrap": varPortLoopDetectedTrap,
       "varRateLimitedOnTrap": varRateLimitedOnTrap,
       "varLLDPChgTrap": varLLDPChgTrap,
       "varusbWarningTrap": varusbWarningTrap,
       "varturboRingMasterMismatchTrap": varturboRingMasterMismatchTrap}
)
