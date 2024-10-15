# SNMP MIB module (WG102-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WG102-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:13:49 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

version = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Netgear_ObjectIdentity = ObjectIdentity
netgear = _Netgear_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526)
)
_WirelessProducts_ObjectIdentity = ObjectIdentity
wirelessProducts = _WirelessProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4)
)
_Wg102_ObjectIdentity = ObjectIdentity
wg102 = _Wg102_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3)
)
_WirelessAPSystemGroup_ObjectIdentity = ObjectIdentity
wirelessAPSystemGroup = _WirelessAPSystemGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 1)
)
_ApMacAddress_Type = PhysAddress
_ApMacAddress_Object = MibScalar
apMacAddress = _ApMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 1, 1),
    _ApMacAddress_Type()
)
apMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apMacAddress.setStatus("mandatory")
_ApFirmwareVersion_Type = DisplayString
_ApFirmwareVersion_Object = MibScalar
apFirmwareVersion = _ApFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 1, 2),
    _ApFirmwareVersion_Type()
)
apFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apFirmwareVersion.setStatus("mandatory")
_ApIPaddress_Type = IpAddress
_ApIPaddress_Object = MibScalar
apIPaddress = _ApIPaddress_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 1, 6),
    _ApIPaddress_Type()
)
apIPaddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIPaddress.setStatus("mandatory")
_ApIPsubnetMask_Type = IpAddress
_ApIPsubnetMask_Object = MibScalar
apIPsubnetMask = _ApIPsubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 1, 7),
    _ApIPsubnetMask_Type()
)
apIPsubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apIPsubnetMask.setStatus("mandatory")
_ApGateway_Type = IpAddress
_ApGateway_Object = MibScalar
apGateway = _ApGateway_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 1, 8),
    _ApGateway_Type()
)
apGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apGateway.setStatus("mandatory")
_ApDNSServerIPAddress_Type = IpAddress
_ApDNSServerIPAddress_Object = MibScalar
apDNSServerIPAddress = _ApDNSServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 1, 9),
    _ApDNSServerIPAddress_Type()
)
apDNSServerIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apDNSServerIPAddress.setStatus("mandatory")


class _ApDHCPMode_Type(Integer32):
    """Custom type apDHCPMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dhcp-Client", 1),
          ("disable", 0))
    )


_ApDHCPMode_Type.__name__ = "Integer32"
_ApDHCPMode_Object = MibScalar
apDHCPMode = _ApDHCPMode_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 1, 10),
    _ApDHCPMode_Type()
)
apDHCPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apDHCPMode.setStatus("mandatory")


class _ApSystemName_Type(DisplayString):
    """Custom type apSystemName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ApSystemName_Type.__name__ = "DisplayString"
_ApSystemName_Object = MibScalar
apSystemName = _ApSystemName_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 1, 11),
    _ApSystemName_Type()
)
apSystemName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSystemName.setStatus("mandatory")


class _ApTimeZone_Type(DisplayString):
    """Custom type apTimeZone based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_ApTimeZone_Type.__name__ = "DisplayString"
_ApTimeZone_Object = MibScalar
apTimeZone = _ApTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 1, 13),
    _ApTimeZone_Type()
)
apTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apTimeZone.setStatus("mandatory")


class _ApDaylightSaving_Type(Integer32):
    """Custom type apDaylightSaving based on Integer32"""
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


_ApDaylightSaving_Type.__name__ = "Integer32"
_ApDaylightSaving_Object = MibScalar
apDaylightSaving = _ApDaylightSaving_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 1, 14),
    _ApDaylightSaving_Type()
)
apDaylightSaving.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apDaylightSaving.setStatus("mandatory")


class _ApCountryDomain_Type(Integer32):
    """Custom type apCountryDomain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(36,
              40,
              124,
              208,
              246,
              250,
              276,
              340,
              372,
              380,
              392,
              410,
              484,
              528,
              554,
              578,
              630,
              724,
              752,
              756,
              826,
              840)
        )
    )
    namedValues = NamedValues(
        *(("asia", 410),
          ("australia", 36),
          ("canada", 124),
          ("denmark", 208),
          ("europe", 40),
          ("finland", 246),
          ("france", 250),
          ("germany", 276),
          ("ireland", 372),
          ("italy", 380),
          ("japan", 392),
          ("mexico", 484),
          ("netherlands", 528),
          ("newZealand", 554),
          ("norway", 578),
          ("puertoRico", 630),
          ("southAmerica", 340),
          ("spain", 724),
          ("sweden", 752),
          ("switzerland", 756),
          ("unitedKingdom", 826),
          ("unitedStates", 840))
    )


_ApCountryDomain_Type.__name__ = "Integer32"
_ApCountryDomain_Object = MibScalar
apCountryDomain = _ApCountryDomain_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 1, 15),
    _ApCountryDomain_Type()
)
apCountryDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apCountryDomain.setStatus("mandatory")
_ApDateTime_Type = DisplayString
_ApDateTime_Object = MibScalar
apDateTime = _ApDateTime_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 1, 16),
    _ApDateTime_Type()
)
apDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apDateTime.setStatus("mandatory")
_ApConnectedStation_ObjectIdentity = ObjectIdentity
apConnectedStation = _ApConnectedStation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 1, 19)
)
_ApConnectedStationTable_Object = MibTable
apConnectedStationTable = _ApConnectedStationTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 1, 19, 1)
)
if mibBuilder.loadTexts:
    apConnectedStationTable.setStatus("mandatory")
_ApConnectedStationEntry_Object = MibTableRow
apConnectedStationEntry = _ApConnectedStationEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 1, 19, 1, 1)
)
apConnectedStationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    apConnectedStationEntry.setStatus("mandatory")
_ApConnectedStationMacAddr_Type = PhysAddress
_ApConnectedStationMacAddr_Object = MibTableColumn
apConnectedStationMacAddr = _ApConnectedStationMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 1, 19, 1, 1, 1),
    _ApConnectedStationMacAddr_Type()
)
apConnectedStationMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apConnectedStationMacAddr.setStatus("mandatory")


class _ApConnectedStationStatus_Type(Integer32):
    """Custom type apConnectedStationStatus based on Integer32"""
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
        *(("allow", 3),
          ("authenticating", 2),
          ("blocked", 4),
          ("dot1xAuthenticated", 0),
          ("macAuthenticated", 1))
    )


_ApConnectedStationStatus_Type.__name__ = "Integer32"
_ApConnectedStationStatus_Object = MibTableColumn
apConnectedStationStatus = _ApConnectedStationStatus_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 1, 19, 1, 1, 2),
    _ApConnectedStationStatus_Type()
)
apConnectedStationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apConnectedStationStatus.setStatus("mandatory")
_WirelessAPManageGroup_ObjectIdentity = ObjectIdentity
wirelessAPManageGroup = _WirelessAPManageGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 2)
)


class _ApRebootNow_Type(Integer32):
    """Custom type apRebootNow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not-reboot", 0),
          ("reboot", 1))
    )


_ApRebootNow_Type.__name__ = "Integer32"
_ApRebootNow_Object = MibScalar
apRebootNow = _ApRebootNow_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 2, 1),
    _ApRebootNow_Type()
)
apRebootNow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRebootNow.setStatus("mandatory")


class _ApResetToFactoryDefault_Type(Integer32):
    """Custom type apResetToFactoryDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("not-reset", 0),
          ("reset", 1))
    )


_ApResetToFactoryDefault_Type.__name__ = "Integer32"
_ApResetToFactoryDefault_Object = MibScalar
apResetToFactoryDefault = _ApResetToFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 2, 2),
    _ApResetToFactoryDefault_Type()
)
apResetToFactoryDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apResetToFactoryDefault.setStatus("mandatory")
_ApTrapReceiveIpAddress_Type = IpAddress
_ApTrapReceiveIpAddress_Object = MibScalar
apTrapReceiveIpAddress = _ApTrapReceiveIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 2, 5),
    _ApTrapReceiveIpAddress_Type()
)
apTrapReceiveIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apTrapReceiveIpAddress.setStatus("mandatory")


class _ApSNMPEnable_Type(Integer32):
    """Custom type apSNMPEnable based on Integer32"""
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


_ApSNMPEnable_Type.__name__ = "Integer32"
_ApSNMPEnable_Object = MibScalar
apSNMPEnable = _ApSNMPEnable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 2, 6),
    _ApSNMPEnable_Type()
)
apSNMPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSNMPEnable.setStatus("mandatory")


class _ApSNMPReadCommunity_Type(DisplayString):
    """Custom type apSNMPReadCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ApSNMPReadCommunity_Type.__name__ = "DisplayString"
_ApSNMPReadCommunity_Object = MibScalar
apSNMPReadCommunity = _ApSNMPReadCommunity_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 2, 7),
    _ApSNMPReadCommunity_Type()
)
apSNMPReadCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSNMPReadCommunity.setStatus("mandatory")


class _ApSNMPWriteCommunity_Type(DisplayString):
    """Custom type apSNMPWriteCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ApSNMPWriteCommunity_Type.__name__ = "DisplayString"
_ApSNMPWriteCommunity_Object = MibScalar
apSNMPWriteCommunity = _ApSNMPWriteCommunity_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 2, 8),
    _ApSNMPWriteCommunity_Type()
)
apSNMPWriteCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSNMPWriteCommunity.setStatus("mandatory")


class _ApAccessControl_Type(Integer32):
    """Custom type apAccessControl based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loacl", 1),
          ("off", 0),
          ("radiusBased", 2))
    )


_ApAccessControl_Type.__name__ = "Integer32"
_ApAccessControl_Object = MibScalar
apAccessControl = _ApAccessControl_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 2, 12),
    _ApAccessControl_Type()
)
apAccessControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apAccessControl.setStatus("mandatory")
_ApAccessControlList_ObjectIdentity = ObjectIdentity
apAccessControlList = _ApAccessControlList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 2, 13)
)
_ApAccessControlListTable_Object = MibTable
apAccessControlListTable = _ApAccessControlListTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 2, 13, 1)
)
if mibBuilder.loadTexts:
    apAccessControlListTable.setStatus("mandatory")
_ApAccessControlListEntry_Object = MibTableRow
apAccessControlListEntry = _ApAccessControlListEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 2, 13, 1, 1)
)
apAccessControlListEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    apAccessControlListEntry.setStatus("mandatory")
_ApAccessControlListMacAddr_Type = PhysAddress
_ApAccessControlListMacAddr_Object = MibTableColumn
apAccessControlListMacAddr = _ApAccessControlListMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 2, 13, 1, 1, 1),
    _ApAccessControlListMacAddr_Type()
)
apAccessControlListMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apAccessControlListMacAddr.setStatus("mandatory")
_ApCtlOperate_ObjectIdentity = ObjectIdentity
apCtlOperate = _ApCtlOperate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 2, 14)
)
_ApAddACLMacAddr_Type = PhysAddress
_ApAddACLMacAddr_Object = MibScalar
apAddACLMacAddr = _ApAddACLMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 2, 14, 1),
    _ApAddACLMacAddr_Type()
)
apAddACLMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apAddACLMacAddr.setStatus("mandatory")
_ApDelACLMacAddr_Type = PhysAddress
_ApDelACLMacAddr_Object = MibScalar
apDelACLMacAddr = _ApDelACLMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 2, 14, 2),
    _ApDelACLMacAddr_Type()
)
apDelACLMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apDelACLMacAddr.setStatus("mandatory")


class _ApSyslog_Type(Integer32):
    """Custom type apSyslog based on Integer32"""
    defaultValue = 0

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


_ApSyslog_Type.__name__ = "Integer32"
_ApSyslog_Object = MibScalar
apSyslog = _ApSyslog_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 2, 25),
    _ApSyslog_Type()
)
apSyslog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSyslog.setStatus("mandatory")


class _ApSyslogPort_Type(Integer32):
    """Custom type apSyslogPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApSyslogPort_Type.__name__ = "Integer32"
_ApSyslogPort_Object = MibScalar
apSyslogPort = _ApSyslogPort_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 2, 26),
    _ApSyslogPort_Type()
)
apSyslogPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSyslogPort.setStatus("mandatory")


class _ApSyslogServer_Type(DisplayString):
    """Custom type apSyslogServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_ApSyslogServer_Type.__name__ = "DisplayString"
_ApSyslogServer_Object = MibScalar
apSyslogServer = _ApSyslogServer_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 2, 27),
    _ApSyslogServer_Type()
)
apSyslogServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSyslogServer.setStatus("mandatory")
_WirelessAP24GGroup_ObjectIdentity = ObjectIdentity
wirelessAP24GGroup = _WirelessAP24GGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 3)
)
_ApWirelessSettingGroup_ObjectIdentity = ObjectIdentity
apWirelessSettingGroup = _ApWirelessSettingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 3, 1)
)


class _ApWirelessMode_Type(Integer32):
    """Custom type apWirelessMode based on Integer32"""
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
        *(("b", 2),
          ("b-and-g", 1),
          ("disable", 0),
          ("g", 3))
    )


_ApWirelessMode_Type.__name__ = "Integer32"
_ApWirelessMode_Object = MibScalar
apWirelessMode = _ApWirelessMode_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 3, 1, 1),
    _ApWirelessMode_Type()
)
apWirelessMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWirelessMode.setStatus("mandatory")


class _ApOperateMode_Type(Integer32):
    """Custom type apOperateMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("pointToMultiPoint", 3),
          ("pointToPoint", 2),
          ("repeaterAccessPoint", 4),
          ("wirelessAccessPoint", 0))
    )


_ApOperateMode_Type.__name__ = "Integer32"
_ApOperateMode_Object = MibScalar
apOperateMode = _ApOperateMode_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 3, 1, 2),
    _ApOperateMode_Type()
)
apOperateMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apOperateMode.setStatus("mandatory")


class _ApBridgeWlanClientAsoc_Type(Integer32):
    """Custom type apBridgeWlanClientAsoc based on Integer32"""
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


_ApBridgeWlanClientAsoc_Type.__name__ = "Integer32"
_ApBridgeWlanClientAsoc_Object = MibScalar
apBridgeWlanClientAsoc = _ApBridgeWlanClientAsoc_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 3, 1, 3),
    _ApBridgeWlanClientAsoc_Type()
)
apBridgeWlanClientAsoc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBridgeWlanClientAsoc.setStatus("mandatory")


class _ApSSID_Type(DisplayString):
    """Custom type apSSID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ApSSID_Type.__name__ = "DisplayString"
_ApSSID_Object = MibScalar
apSSID = _ApSSID_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 3, 1, 4),
    _ApSSID_Type()
)
apSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSSID.setStatus("mandatory")


class _ApChannelNo_Type(Integer32):
    """Custom type apChannelNo based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_ApChannelNo_Type.__name__ = "Integer32"
_ApChannelNo_Object = MibScalar
apChannelNo = _ApChannelNo_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 3, 1, 5),
    _ApChannelNo_Type()
)
apChannelNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apChannelNo.setStatus("mandatory")
_ApRemoteMacAddress_Type = PhysAddress
_ApRemoteMacAddress_Object = MibScalar
apRemoteMacAddress = _ApRemoteMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 3, 1, 6),
    _ApRemoteMacAddress_Type()
)
apRemoteMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRemoteMacAddress.setStatus("mandatory")
_ApChildMacAddress_Type = PhysAddress
_ApChildMacAddress_Object = MibScalar
apChildMacAddress = _ApChildMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 3, 1, 7),
    _ApChildMacAddress_Type()
)
apChildMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apChildMacAddress.setStatus("mandatory")


class _ApBroadcastSSID_Type(Integer32):
    """Custom type apBroadcastSSID based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ApBroadcastSSID_Type.__name__ = "Integer32"
_ApBroadcastSSID_Object = MibScalar
apBroadcastSSID = _ApBroadcastSSID_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 3, 1, 8),
    _ApBroadcastSSID_Type()
)
apBroadcastSSID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBroadcastSSID.setStatus("mandatory")


class _ApWirelessSeparation_Type(Integer32):
    """Custom type apWirelessSeparation based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ApWirelessSeparation_Type.__name__ = "Integer32"
_ApWirelessSeparation_Object = MibScalar
apWirelessSeparation = _ApWirelessSeparation_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 3, 1, 9),
    _ApWirelessSeparation_Type()
)
apWirelessSeparation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWirelessSeparation.setStatus("mandatory")


class _ApFragmentationLength_Type(Integer32):
    """Custom type apFragmentationLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 2346),
    )


_ApFragmentationLength_Type.__name__ = "Integer32"
_ApFragmentationLength_Object = MibScalar
apFragmentationLength = _ApFragmentationLength_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 3, 1, 10),
    _ApFragmentationLength_Type()
)
apFragmentationLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apFragmentationLength.setStatus("mandatory")


class _ApBeaconInterval_Type(Integer32):
    """Custom type apBeaconInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 3000),
    )


_ApBeaconInterval_Type.__name__ = "Integer32"
_ApBeaconInterval_Object = MibScalar
apBeaconInterval = _ApBeaconInterval_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 3, 1, 11),
    _ApBeaconInterval_Type()
)
apBeaconInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apBeaconInterval.setStatus("mandatory")


class _ApRTSThreshold_Type(Integer32):
    """Custom type apRTSThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 2346),
    )


_ApRTSThreshold_Type.__name__ = "Integer32"
_ApRTSThreshold_Object = MibScalar
apRTSThreshold = _ApRTSThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 3, 1, 12),
    _ApRTSThreshold_Type()
)
apRTSThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apRTSThreshold.setStatus("mandatory")


class _ApPreambleType_Type(Integer32):
    """Custom type apPreambleType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("long", 0))
    )


_ApPreambleType_Type.__name__ = "Integer32"
_ApPreambleType_Object = MibScalar
apPreambleType = _ApPreambleType_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 3, 1, 13),
    _ApPreambleType_Type()
)
apPreambleType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apPreambleType.setStatus("mandatory")


class _ApOutputPowerLevel_Type(Integer32):
    """Custom type apOutputPowerLevel based on Integer32"""
    defaultValue = 0

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
        *(("eighth", 3),
          ("full", 0),
          ("half", 1),
          ("minimum", 4),
          ("quarter", 2))
    )


_ApOutputPowerLevel_Type.__name__ = "Integer32"
_ApOutputPowerLevel_Object = MibScalar
apOutputPowerLevel = _ApOutputPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 3, 1, 14),
    _ApOutputPowerLevel_Type()
)
apOutputPowerLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apOutputPowerLevel.setStatus("mandatory")


class _ApDTIM_Type(Integer32):
    """Custom type apDTIM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ApDTIM_Type.__name__ = "Integer32"
_ApDTIM_Object = MibScalar
apDTIM = _ApDTIM_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 3, 1, 15),
    _ApDTIM_Type()
)
apDTIM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apDTIM.setStatus("mandatory")


class _ApSuperG_Type(Integer32):
    """Custom type apSuperG based on Integer32"""
    defaultValue = 0

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


_ApSuperG_Type.__name__ = "Integer32"
_ApSuperG_Object = MibScalar
apSuperG = _ApSuperG_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 3, 1, 16),
    _ApSuperG_Type()
)
apSuperG.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSuperG.setStatus("mandatory")


class _ApHTTPRedirect_Type(Integer32):
    """Custom type apHTTPRedirect based on Integer32"""
    defaultValue = 0

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


_ApHTTPRedirect_Type.__name__ = "Integer32"
_ApHTTPRedirect_Object = MibScalar
apHTTPRedirect = _ApHTTPRedirect_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 3, 1, 17),
    _ApHTTPRedirect_Type()
)
apHTTPRedirect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apHTTPRedirect.setStatus("mandatory")


class _ApHTTPRedirectURL_Type(DisplayString):
    """Custom type apHTTPRedirectURL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ApHTTPRedirectURL_Type.__name__ = "DisplayString"
_ApHTTPRedirectURL_Object = MibScalar
apHTTPRedirectURL = _ApHTTPRedirectURL_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 3, 1, 18),
    _ApHTTPRedirectURL_Type()
)
apHTTPRedirectURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apHTTPRedirectURL.setStatus("mandatory")


class _ApDataRate_Type(Integer32):
    """Custom type apDataRate based on Integer32"""
    defaultValue = 0

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
              13)
        )
    )
    namedValues = NamedValues(
        *(("auto-negotiate", 0),
          ("rate-108Mbps", 13),
          ("rate-11Mbps", 4),
          ("rate-12Mbps", 7),
          ("rate-18Mbps", 8),
          ("rate-1Mbps", 1),
          ("rate-24Mbps", 9),
          ("rate-2Mbps", 2),
          ("rate-36Mbps", 10),
          ("rate-48Mbps", 11),
          ("rate-54Mbps", 12),
          ("rate-5dot5Mbps", 3),
          ("rate-6Mbps", 5),
          ("rate-9Mbps", 6))
    )


_ApDataRate_Type.__name__ = "Integer32"
_ApDataRate_Object = MibScalar
apDataRate = _ApDataRate_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 3, 1, 19),
    _ApDataRate_Type()
)
apDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apDataRate.setStatus("mandatory")
_ApStatistic_ObjectIdentity = ObjectIdentity
apStatistic = _ApStatistic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 3, 1, 20)
)
_ApWiredEthernetStat_ObjectIdentity = ObjectIdentity
apWiredEthernetStat = _ApWiredEthernetStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 3, 1, 20, 1)
)
_ApLanRecvPacket_Type = Unsigned32
_ApLanRecvPacket_Object = MibScalar
apLanRecvPacket = _ApLanRecvPacket_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 3, 1, 20, 1, 1),
    _ApLanRecvPacket_Type()
)
apLanRecvPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLanRecvPacket.setStatus("current")
_ApLanTransPacket_Type = Unsigned32
_ApLanTransPacket_Object = MibScalar
apLanTransPacket = _ApLanTransPacket_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 3, 1, 20, 1, 2),
    _ApLanTransPacket_Type()
)
apLanTransPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLanTransPacket.setStatus("current")
_ApLanRecvBytes_Type = Unsigned32
_ApLanRecvBytes_Object = MibScalar
apLanRecvBytes = _ApLanRecvBytes_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 3, 1, 20, 1, 3),
    _ApLanRecvBytes_Type()
)
apLanRecvBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLanRecvBytes.setStatus("current")
_ApLanTransBytes_Type = Unsigned32
_ApLanTransBytes_Object = MibScalar
apLanTransBytes = _ApLanTransBytes_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 3, 1, 20, 1, 4),
    _ApLanTransBytes_Type()
)
apLanTransBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apLanTransBytes.setStatus("current")
_ApWirelessStat_ObjectIdentity = ObjectIdentity
apWirelessStat = _ApWirelessStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 3, 1, 20, 2)
)
_ApWlanRecvUnicastPacket_Type = Unsigned32
_ApWlanRecvUnicastPacket_Object = MibScalar
apWlanRecvUnicastPacket = _ApWlanRecvUnicastPacket_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 3, 1, 20, 2, 1),
    _ApWlanRecvUnicastPacket_Type()
)
apWlanRecvUnicastPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWlanRecvUnicastPacket.setStatus("current")
_ApWlanTransUnicastPacket_Type = Unsigned32
_ApWlanTransUnicastPacket_Object = MibScalar
apWlanTransUnicastPacket = _ApWlanTransUnicastPacket_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 3, 1, 20, 2, 2),
    _ApWlanTransUnicastPacket_Type()
)
apWlanTransUnicastPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWlanTransUnicastPacket.setStatus("current")
_ApWlanRecvBroadcastPsacket_Type = Unsigned32
_ApWlanRecvBroadcastPsacket_Object = MibScalar
apWlanRecvBroadcastPsacket = _ApWlanRecvBroadcastPsacket_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 3, 1, 20, 2, 3),
    _ApWlanRecvBroadcastPsacket_Type()
)
apWlanRecvBroadcastPsacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWlanRecvBroadcastPsacket.setStatus("current")
_ApWlanTransBroadcastPacket_Type = Unsigned32
_ApWlanTransBroadcastPacket_Object = MibScalar
apWlanTransBroadcastPacket = _ApWlanTransBroadcastPacket_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 3, 1, 20, 2, 4),
    _ApWlanTransBroadcastPacket_Type()
)
apWlanTransBroadcastPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWlanTransBroadcastPacket.setStatus("current")
_ApWlanRecvMulticastPacket_Type = Unsigned32
_ApWlanRecvMulticastPacket_Object = MibScalar
apWlanRecvMulticastPacket = _ApWlanRecvMulticastPacket_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 3, 1, 20, 2, 5),
    _ApWlanRecvMulticastPacket_Type()
)
apWlanRecvMulticastPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWlanRecvMulticastPacket.setStatus("current")
_ApWlanTransMulticastPacket_Type = Unsigned32
_ApWlanTransMulticastPacket_Object = MibScalar
apWlanTransMulticastPacket = _ApWlanTransMulticastPacket_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 3, 1, 20, 2, 6),
    _ApWlanTransMulticastPacket_Type()
)
apWlanTransMulticastPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWlanTransMulticastPacket.setStatus("current")
_ApWlanRecvPacket_Type = Unsigned32
_ApWlanRecvPacket_Object = MibScalar
apWlanRecvPacket = _ApWlanRecvPacket_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 3, 1, 20, 2, 7),
    _ApWlanRecvPacket_Type()
)
apWlanRecvPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWlanRecvPacket.setStatus("current")
_ApWlanTransPacket_Type = Unsigned32
_ApWlanTransPacket_Object = MibScalar
apWlanTransPacket = _ApWlanTransPacket_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 3, 1, 20, 2, 8),
    _ApWlanTransPacket_Type()
)
apWlanTransPacket.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWlanTransPacket.setStatus("current")
_ApWlanRecvBytes_Type = Unsigned32
_ApWlanRecvBytes_Object = MibScalar
apWlanRecvBytes = _ApWlanRecvBytes_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 3, 1, 20, 2, 9),
    _ApWlanRecvBytes_Type()
)
apWlanRecvBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWlanRecvBytes.setStatus("current")
_ApWlanTransBytes_Type = Unsigned32
_ApWlanTransBytes_Object = MibScalar
apWlanTransBytes = _ApWlanTransBytes_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 3, 1, 20, 2, 10),
    _ApWlanTransBytes_Type()
)
apWlanTransBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apWlanTransBytes.setStatus("current")
_ApPTMPallowList_ObjectIdentity = ObjectIdentity
apPTMPallowList = _ApPTMPallowList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 3, 1, 27)
)
_Mac1_Type = PhysAddress
_Mac1_Object = MibScalar
mac1 = _Mac1_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 3, 1, 27, 1),
    _Mac1_Type()
)
mac1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mac1.setStatus("mandatory")
_Mac2_Type = PhysAddress
_Mac2_Object = MibScalar
mac2 = _Mac2_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 3, 1, 27, 2),
    _Mac2_Type()
)
mac2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mac2.setStatus("mandatory")
_Mac3_Type = PhysAddress
_Mac3_Object = MibScalar
mac3 = _Mac3_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 3, 1, 27, 3),
    _Mac3_Type()
)
mac3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mac3.setStatus("mandatory")
_Mac4_Type = PhysAddress
_Mac4_Object = MibScalar
mac4 = _Mac4_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 3, 1, 27, 4),
    _Mac4_Type()
)
mac4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mac4.setStatus("mandatory")
_ApWirelessSecurityGroup_ObjectIdentity = ObjectIdentity
apWirelessSecurityGroup = _ApWirelessSecurityGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 3, 2)
)


class _ApSecuritySystem_Type(Integer32):
    """Custom type apSecuritySystem based on Integer32"""
    defaultValue = 0

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
        *(("dot1x", 4),
          ("none", 0),
          ("wep", 1),
          ("wpa-802dot1x", 3),
          ("wpa-psk", 2))
    )


_ApSecuritySystem_Type.__name__ = "Integer32"
_ApSecuritySystem_Object = MibScalar
apSecuritySystem = _ApSecuritySystem_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 3, 2, 1),
    _ApSecuritySystem_Type()
)
apSecuritySystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSecuritySystem.setStatus("mandatory")


class _Ap802dot1xWEPKeySize_Type(Integer32):
    """Custom type ap802dot1xWEPKeySize based on Integer32"""
    defaultValue = 0

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
        *(("bit128", 2),
          ("bit152", 3),
          ("bit64", 1),
          ("none", 0))
    )


_Ap802dot1xWEPKeySize_Type.__name__ = "Integer32"
_Ap802dot1xWEPKeySize_Object = MibScalar
ap802dot1xWEPKeySize = _Ap802dot1xWEPKeySize_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 3, 2, 2),
    _Ap802dot1xWEPKeySize_Type()
)
ap802dot1xWEPKeySize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ap802dot1xWEPKeySize.setStatus("mandatory")


class _ApWEPMode_Type(Integer32):
    """Custom type apWEPMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("open-128WEP-MODE", 1),
          ("open-152WEP-MODE", 6),
          ("open-64WEP-MODE", 0),
          ("share-128WEP-MODE", 3),
          ("share-152WEP-MODE", 7),
          ("share-64WEP-MODE", 2))
    )


_ApWEPMode_Type.__name__ = "Integer32"
_ApWEPMode_Object = MibScalar
apWEPMode = _ApWEPMode_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 3, 2, 3),
    _ApWEPMode_Type()
)
apWEPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWEPMode.setStatus("mandatory")
_ApWEPKeysSet_ObjectIdentity = ObjectIdentity
apWEPKeysSet = _ApWEPKeysSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 3, 2, 4)
)
_ApKeys24GSetTable_Object = MibTable
apKeys24GSetTable = _ApKeys24GSetTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 3, 2, 4, 1)
)
if mibBuilder.loadTexts:
    apKeys24GSetTable.setStatus("mandatory")
_ApKeys24GSetEntry_Object = MibTableRow
apKeys24GSetEntry = _ApKeys24GSetEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 3, 2, 4, 1, 1)
)
apKeys24GSetEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    apKeys24GSetEntry.setStatus("mandatory")


class _ApKeysSetEnabled_Type(Integer32):
    """Custom type apKeysSetEnabled based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ApKeysSetEnabled_Type.__name__ = "Integer32"
_ApKeysSetEnabled_Object = MibTableColumn
apKeysSetEnabled = _ApKeysSetEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 3, 2, 4, 1, 1, 1),
    _ApKeysSetEnabled_Type()
)
apKeysSetEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apKeysSetEnabled.setStatus("mandatory")


class _ApKeys_Type(OctetString):
    """Custom type apKeys based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 13),
    )


_ApKeys_Type.__name__ = "OctetString"
_ApKeys_Object = MibTableColumn
apKeys = _ApKeys_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 3, 2, 4, 1, 1, 2),
    _ApKeys_Type()
)
apKeys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apKeys.setStatus("mandatory")


class _ApWPANetworkKey_Type(DisplayString):
    """Custom type apWPANetworkKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ApWPANetworkKey_Type.__name__ = "DisplayString"
_ApWPANetworkKey_Object = MibScalar
apWPANetworkKey = _ApWPANetworkKey_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 3, 2, 6),
    _ApWPANetworkKey_Type()
)
apWPANetworkKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWPANetworkKey.setStatus("mandatory")


class _ApWPAEncryption_Type(Integer32):
    """Custom type apWPAEncryption based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aes-ccmp", 3),
          ("tkip", 0))
    )


_ApWPAEncryption_Type.__name__ = "Integer32"
_ApWPAEncryption_Object = MibScalar
apWPAEncryption = _ApWPAEncryption_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 3, 2, 7),
    _ApWPAEncryption_Type()
)
apWPAEncryption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWPAEncryption.setStatus("mandatory")


class _ApWPAGroupKeyUpdate_Type(Integer32):
    """Custom type apWPAGroupKeyUpdate based on Integer32"""
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


_ApWPAGroupKeyUpdate_Type.__name__ = "Integer32"
_ApWPAGroupKeyUpdate_Object = MibScalar
apWPAGroupKeyUpdate = _ApWPAGroupKeyUpdate_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 3, 2, 10),
    _ApWPAGroupKeyUpdate_Type()
)
apWPAGroupKeyUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWPAGroupKeyUpdate.setStatus("mandatory")


class _ApWPAGroupKeyLifetime_Type(Integer32):
    """Custom type apWPAGroupKeyLifetime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 200),
    )


_ApWPAGroupKeyLifetime_Type.__name__ = "Integer32"
_ApWPAGroupKeyLifetime_Object = MibScalar
apWPAGroupKeyLifetime = _ApWPAGroupKeyLifetime_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 3, 2, 11),
    _ApWPAGroupKeyLifetime_Type()
)
apWPAGroupKeyLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWPAGroupKeyLifetime.setStatus("mandatory")


class _ApWPAMembershipTerminatedGroupKeyUpdate_Type(Integer32):
    """Custom type apWPAMembershipTerminatedGroupKeyUpdate based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ApWPAMembershipTerminatedGroupKeyUpdate_Type.__name__ = "Integer32"
_ApWPAMembershipTerminatedGroupKeyUpdate_Object = MibScalar
apWPAMembershipTerminatedGroupKeyUpdate = _ApWPAMembershipTerminatedGroupKeyUpdate_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 3, 2, 12),
    _ApWPAMembershipTerminatedGroupKeyUpdate_Type()
)
apWPAMembershipTerminatedGroupKeyUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apWPAMembershipTerminatedGroupKeyUpdate.setStatus("mandatory")
_ApPrimaryRadiusServer_Type = DisplayString
_ApPrimaryRadiusServer_Object = MibScalar
apPrimaryRadiusServer = _ApPrimaryRadiusServer_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 3, 2, 13),
    _ApPrimaryRadiusServer_Type()
)
apPrimaryRadiusServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apPrimaryRadiusServer.setStatus("mandatory")


class _ApPrimaryRadiusPort_Type(Integer32):
    """Custom type apPrimaryRadiusPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApPrimaryRadiusPort_Type.__name__ = "Integer32"
_ApPrimaryRadiusPort_Object = MibScalar
apPrimaryRadiusPort = _ApPrimaryRadiusPort_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 3, 2, 14),
    _ApPrimaryRadiusPort_Type()
)
apPrimaryRadiusPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apPrimaryRadiusPort.setStatus("mandatory")


class _ApPrimaryRadiusSharedKey_Type(DisplayString):
    """Custom type apPrimaryRadiusSharedKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ApPrimaryRadiusSharedKey_Type.__name__ = "DisplayString"
_ApPrimaryRadiusSharedKey_Object = MibScalar
apPrimaryRadiusSharedKey = _ApPrimaryRadiusSharedKey_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 3, 2, 15),
    _ApPrimaryRadiusSharedKey_Type()
)
apPrimaryRadiusSharedKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apPrimaryRadiusSharedKey.setStatus("mandatory")
_ApPrimaryRadiusAccountServer_Type = DisplayString
_ApPrimaryRadiusAccountServer_Object = MibScalar
apPrimaryRadiusAccountServer = _ApPrimaryRadiusAccountServer_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 3, 2, 16),
    _ApPrimaryRadiusAccountServer_Type()
)
apPrimaryRadiusAccountServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apPrimaryRadiusAccountServer.setStatus("mandatory")


class _ApPrimaryRadiusAccountPort_Type(Integer32):
    """Custom type apPrimaryRadiusAccountPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApPrimaryRadiusAccountPort_Type.__name__ = "Integer32"
_ApPrimaryRadiusAccountPort_Object = MibScalar
apPrimaryRadiusAccountPort = _ApPrimaryRadiusAccountPort_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 3, 2, 17),
    _ApPrimaryRadiusAccountPort_Type()
)
apPrimaryRadiusAccountPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apPrimaryRadiusAccountPort.setStatus("mandatory")


class _ApPrimaryRadiusAccountSharedKey_Type(DisplayString):
    """Custom type apPrimaryRadiusAccountSharedKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ApPrimaryRadiusAccountSharedKey_Type.__name__ = "DisplayString"
_ApPrimaryRadiusAccountSharedKey_Object = MibScalar
apPrimaryRadiusAccountSharedKey = _ApPrimaryRadiusAccountSharedKey_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 3, 2, 18),
    _ApPrimaryRadiusAccountSharedKey_Type()
)
apPrimaryRadiusAccountSharedKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apPrimaryRadiusAccountSharedKey.setStatus("mandatory")
_ApSecondaryRadiusServer_Type = DisplayString
_ApSecondaryRadiusServer_Object = MibScalar
apSecondaryRadiusServer = _ApSecondaryRadiusServer_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 3, 2, 19),
    _ApSecondaryRadiusServer_Type()
)
apSecondaryRadiusServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSecondaryRadiusServer.setStatus("mandatory")


class _ApSecondaryRadiusPort_Type(Integer32):
    """Custom type apSecondaryRadiusPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApSecondaryRadiusPort_Type.__name__ = "Integer32"
_ApSecondaryRadiusPort_Object = MibScalar
apSecondaryRadiusPort = _ApSecondaryRadiusPort_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 3, 2, 20),
    _ApSecondaryRadiusPort_Type()
)
apSecondaryRadiusPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSecondaryRadiusPort.setStatus("mandatory")


class _ApSecondaryRadiusSharedKey_Type(DisplayString):
    """Custom type apSecondaryRadiusSharedKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ApSecondaryRadiusSharedKey_Type.__name__ = "DisplayString"
_ApSecondaryRadiusSharedKey_Object = MibScalar
apSecondaryRadiusSharedKey = _ApSecondaryRadiusSharedKey_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 3, 2, 21),
    _ApSecondaryRadiusSharedKey_Type()
)
apSecondaryRadiusSharedKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSecondaryRadiusSharedKey.setStatus("mandatory")
_ApSecondaryRadiusAccountServer_Type = DisplayString
_ApSecondaryRadiusAccountServer_Object = MibScalar
apSecondaryRadiusAccountServer = _ApSecondaryRadiusAccountServer_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 3, 2, 22),
    _ApSecondaryRadiusAccountServer_Type()
)
apSecondaryRadiusAccountServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSecondaryRadiusAccountServer.setStatus("mandatory")


class _ApSecondaryRadiusAccountPort_Type(Integer32):
    """Custom type apSecondaryRadiusAccountPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApSecondaryRadiusAccountPort_Type.__name__ = "Integer32"
_ApSecondaryRadiusAccountPort_Object = MibScalar
apSecondaryRadiusAccountPort = _ApSecondaryRadiusAccountPort_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 3, 2, 23),
    _ApSecondaryRadiusAccountPort_Type()
)
apSecondaryRadiusAccountPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSecondaryRadiusAccountPort.setStatus("mandatory")


class _ApSecondaryRadiusAccountSharedKey_Type(DisplayString):
    """Custom type apSecondaryRadiusAccountSharedKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ApSecondaryRadiusAccountSharedKey_Type.__name__ = "DisplayString"
_ApSecondaryRadiusAccountSharedKey_Object = MibScalar
apSecondaryRadiusAccountSharedKey = _ApSecondaryRadiusAccountSharedKey_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 3, 2, 24),
    _ApSecondaryRadiusAccountSharedKey_Type()
)
apSecondaryRadiusAccountSharedKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apSecondaryRadiusAccountSharedKey.setStatus("mandatory")


class _ApReauthenticationTime_Type(Integer32):
    """Custom type apReauthenticationTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1800, 36000),
    )


_ApReauthenticationTime_Type.__name__ = "Integer32"
_ApReauthenticationTime_Object = MibScalar
apReauthenticationTime = _ApReauthenticationTime_Object(
    (1, 3, 6, 1, 4, 1, 4526, 4, 3, 1000, 3, 2, 27),
    _ApReauthenticationTime_Type()
)
apReauthenticationTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apReauthenticationTime.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WG102-MIB",
    **{"netgear": netgear,
       "wirelessProducts": wirelessProducts,
       "wg102": wg102,
       "version": version,
       "wirelessAPSystemGroup": wirelessAPSystemGroup,
       "apMacAddress": apMacAddress,
       "apFirmwareVersion": apFirmwareVersion,
       "apIPaddress": apIPaddress,
       "apIPsubnetMask": apIPsubnetMask,
       "apGateway": apGateway,
       "apDNSServerIPAddress": apDNSServerIPAddress,
       "apDHCPMode": apDHCPMode,
       "apSystemName": apSystemName,
       "apTimeZone": apTimeZone,
       "apDaylightSaving": apDaylightSaving,
       "apCountryDomain": apCountryDomain,
       "apDateTime": apDateTime,
       "apConnectedStation": apConnectedStation,
       "apConnectedStationTable": apConnectedStationTable,
       "apConnectedStationEntry": apConnectedStationEntry,
       "apConnectedStationMacAddr": apConnectedStationMacAddr,
       "apConnectedStationStatus": apConnectedStationStatus,
       "wirelessAPManageGroup": wirelessAPManageGroup,
       "apRebootNow": apRebootNow,
       "apResetToFactoryDefault": apResetToFactoryDefault,
       "apTrapReceiveIpAddress": apTrapReceiveIpAddress,
       "apSNMPEnable": apSNMPEnable,
       "apSNMPReadCommunity": apSNMPReadCommunity,
       "apSNMPWriteCommunity": apSNMPWriteCommunity,
       "apAccessControl": apAccessControl,
       "apAccessControlList": apAccessControlList,
       "apAccessControlListTable": apAccessControlListTable,
       "apAccessControlListEntry": apAccessControlListEntry,
       "apAccessControlListMacAddr": apAccessControlListMacAddr,
       "apCtlOperate": apCtlOperate,
       "apAddACLMacAddr": apAddACLMacAddr,
       "apDelACLMacAddr": apDelACLMacAddr,
       "apSyslog": apSyslog,
       "apSyslogPort": apSyslogPort,
       "apSyslogServer": apSyslogServer,
       "wirelessAP24GGroup": wirelessAP24GGroup,
       "apWirelessSettingGroup": apWirelessSettingGroup,
       "apWirelessMode": apWirelessMode,
       "apOperateMode": apOperateMode,
       "apBridgeWlanClientAsoc": apBridgeWlanClientAsoc,
       "apSSID": apSSID,
       "apChannelNo": apChannelNo,
       "apRemoteMacAddress": apRemoteMacAddress,
       "apChildMacAddress": apChildMacAddress,
       "apBroadcastSSID": apBroadcastSSID,
       "apWirelessSeparation": apWirelessSeparation,
       "apFragmentationLength": apFragmentationLength,
       "apBeaconInterval": apBeaconInterval,
       "apRTSThreshold": apRTSThreshold,
       "apPreambleType": apPreambleType,
       "apOutputPowerLevel": apOutputPowerLevel,
       "apDTIM": apDTIM,
       "apSuperG": apSuperG,
       "apHTTPRedirect": apHTTPRedirect,
       "apHTTPRedirectURL": apHTTPRedirectURL,
       "apDataRate": apDataRate,
       "apStatistic": apStatistic,
       "apWiredEthernetStat": apWiredEthernetStat,
       "apLanRecvPacket": apLanRecvPacket,
       "apLanTransPacket": apLanTransPacket,
       "apLanRecvBytes": apLanRecvBytes,
       "apLanTransBytes": apLanTransBytes,
       "apWirelessStat": apWirelessStat,
       "apWlanRecvUnicastPacket": apWlanRecvUnicastPacket,
       "apWlanTransUnicastPacket": apWlanTransUnicastPacket,
       "apWlanRecvBroadcastPsacket": apWlanRecvBroadcastPsacket,
       "apWlanTransBroadcastPacket": apWlanTransBroadcastPacket,
       "apWlanRecvMulticastPacket": apWlanRecvMulticastPacket,
       "apWlanTransMulticastPacket": apWlanTransMulticastPacket,
       "apWlanRecvPacket": apWlanRecvPacket,
       "apWlanTransPacket": apWlanTransPacket,
       "apWlanRecvBytes": apWlanRecvBytes,
       "apWlanTransBytes": apWlanTransBytes,
       "apPTMPallowList": apPTMPallowList,
       "mac1": mac1,
       "mac2": mac2,
       "mac3": mac3,
       "mac4": mac4,
       "apWirelessSecurityGroup": apWirelessSecurityGroup,
       "apSecuritySystem": apSecuritySystem,
       "ap802dot1xWEPKeySize": ap802dot1xWEPKeySize,
       "apWEPMode": apWEPMode,
       "apWEPKeysSet": apWEPKeysSet,
       "apKeys24GSetTable": apKeys24GSetTable,
       "apKeys24GSetEntry": apKeys24GSetEntry,
       "apKeysSetEnabled": apKeysSetEnabled,
       "apKeys": apKeys,
       "apWPANetworkKey": apWPANetworkKey,
       "apWPAEncryption": apWPAEncryption,
       "apWPAGroupKeyUpdate": apWPAGroupKeyUpdate,
       "apWPAGroupKeyLifetime": apWPAGroupKeyLifetime,
       "apWPAMembershipTerminatedGroupKeyUpdate": apWPAMembershipTerminatedGroupKeyUpdate,
       "apPrimaryRadiusServer": apPrimaryRadiusServer,
       "apPrimaryRadiusPort": apPrimaryRadiusPort,
       "apPrimaryRadiusSharedKey": apPrimaryRadiusSharedKey,
       "apPrimaryRadiusAccountServer": apPrimaryRadiusAccountServer,
       "apPrimaryRadiusAccountPort": apPrimaryRadiusAccountPort,
       "apPrimaryRadiusAccountSharedKey": apPrimaryRadiusAccountSharedKey,
       "apSecondaryRadiusServer": apSecondaryRadiusServer,
       "apSecondaryRadiusPort": apSecondaryRadiusPort,
       "apSecondaryRadiusSharedKey": apSecondaryRadiusSharedKey,
       "apSecondaryRadiusAccountServer": apSecondaryRadiusAccountServer,
       "apSecondaryRadiusAccountPort": apSecondaryRadiusAccountPort,
       "apSecondaryRadiusAccountSharedKey": apSecondaryRadiusAccountSharedKey,
       "apReauthenticationTime": apReauthenticationTime}
)
