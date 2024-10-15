# SNMP MIB module (ASKEY-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ASKEY-SYSTEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:42:50 2024
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

(ipDslam,) = mibBuilder.importSymbols(
    "ASKEY-DSLAM-MIB",
    "ipDslam")

(aeAlarmPhysicalIndex,) = mibBuilder.importSymbols(
    "ASKEY-ENTITY-ALARM-MIB",
    "aeAlarmPhysicalIndex")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(InetAddress,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

askeySystemMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1)
)


# Types definitions



class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )




# TEXTUAL-CONVENTIONS



class IPSectionIndex(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )



class VLANList(OctetString, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_IpConfig_ObjectIdentity = ObjectIdentity
ipConfig = _IpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 1)
)
_NodeIP_ObjectIdentity = ObjectIdentity
nodeIP = _NodeIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 1, 1)
)
_NodeIPAddr_Type = IpAddress
_NodeIPAddr_Object = MibScalar
nodeIPAddr = _NodeIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 1, 1, 1),
    _NodeIPAddr_Type()
)
nodeIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeIPAddr.setStatus("current")
_NodeIPNetMask_Type = IpAddress
_NodeIPNetMask_Object = MibScalar
nodeIPNetMask = _NodeIPNetMask_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 1, 1, 2),
    _NodeIPNetMask_Type()
)
nodeIPNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nodeIPNetMask.setStatus("current")
_NodeMACAddr_Type = MacAddress
_NodeMACAddr_Object = MibScalar
nodeMACAddr = _NodeMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 1, 1, 3),
    _NodeMACAddr_Type()
)
nodeMACAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nodeMACAddr.setStatus("current")
_GatewayIPAddr_Type = IpAddress
_GatewayIPAddr_Object = MibScalar
gatewayIPAddr = _GatewayIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 1, 1, 4),
    _GatewayIPAddr_Type()
)
gatewayIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    gatewayIPAddr.setStatus("current")
_MgmtIP_ObjectIdentity = ObjectIdentity
mgmtIP = _MgmtIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 1, 2)
)
_MgmtIPAddr_Type = IpAddress
_MgmtIPAddr_Object = MibScalar
mgmtIPAddr = _MgmtIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 1, 2, 1),
    _MgmtIPAddr_Type()
)
mgmtIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtIPAddr.setStatus("current")
_MgmtIPNetMask_Type = IpAddress
_MgmtIPNetMask_Object = MibScalar
mgmtIPNetMask = _MgmtIPNetMask_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 1, 2, 2),
    _MgmtIPNetMask_Type()
)
mgmtIPNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgmtIPNetMask.setStatus("current")
_MgmtMACAddr_Type = MacAddress
_MgmtMACAddr_Object = MibScalar
mgmtMACAddr = _MgmtMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 1, 2, 3),
    _MgmtMACAddr_Type()
)
mgmtMACAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgmtMACAddr.setStatus("current")
_NodeTime_ObjectIdentity = ObjectIdentity
nodeTime = _NodeTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 2)
)


class _Time_Type(DisplayString):
    """Custom type time based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(14, 19),
    )


_Time_Type.__name__ = "DisplayString"
_Time_Object = MibScalar
time = _Time_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 2, 1),
    _Time_Type()
)
time.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    time.setStatus("current")


class _Zone_Type(Integer32):
    """Custom type zone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-12, 13),
    )


_Zone_Type.__name__ = "Integer32"
_Zone_Object = MibScalar
zone = _Zone_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 2, 2),
    _Zone_Type()
)
zone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zone.setStatus("current")
_SnmpTrapMib_ObjectIdentity = ObjectIdentity
snmpTrapMib = _SnmpTrapMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 6)
)
_SnmpTrapTable_Object = MibTable
snmpTrapTable = _SnmpTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 6, 1)
)
if mibBuilder.loadTexts:
    snmpTrapTable.setStatus("current")
_SnmpTrapEntry_Object = MibTableRow
snmpTrapEntry = _SnmpTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 6, 1, 1)
)
snmpTrapEntry.setIndexNames(
    (0, "ASKEY-SYSTEM-MIB", "snmpTrapStation"),
)
if mibBuilder.loadTexts:
    snmpTrapEntry.setStatus("current")
_SnmpTrapStation_Type = IpAddress
_SnmpTrapStation_Object = MibTableColumn
snmpTrapStation = _SnmpTrapStation_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 6, 1, 1, 1),
    _SnmpTrapStation_Type()
)
snmpTrapStation.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snmpTrapStation.setStatus("current")


class _SnmpTrapCommunity_Type(DisplayString):
    """Custom type snmpTrapCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_SnmpTrapCommunity_Type.__name__ = "DisplayString"
_SnmpTrapCommunity_Object = MibTableColumn
snmpTrapCommunity = _SnmpTrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 6, 1, 1, 2),
    _SnmpTrapCommunity_Type()
)
snmpTrapCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpTrapCommunity.setStatus("current")


class _SnmpTrapSNMPVersion_Type(Integer32):
    """Custom type snmpTrapSNMPVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("snmpv1", 1),
          ("snmpv2c", 2))
    )


_SnmpTrapSNMPVersion_Type.__name__ = "Integer32"
_SnmpTrapSNMPVersion_Object = MibTableColumn
snmpTrapSNMPVersion = _SnmpTrapSNMPVersion_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 6, 1, 1, 3),
    _SnmpTrapSNMPVersion_Type()
)
snmpTrapSNMPVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpTrapSNMPVersion.setStatus("current")
_SnmpTrapRowStatus_Type = RowStatus
_SnmpTrapRowStatus_Object = MibTableColumn
snmpTrapRowStatus = _SnmpTrapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 6, 1, 1, 4),
    _SnmpTrapRowStatus_Type()
)
snmpTrapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpTrapRowStatus.setStatus("current")
_SnmpCommunityMib_ObjectIdentity = ObjectIdentity
snmpCommunityMib = _SnmpCommunityMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 7)
)
_SnmpCommunityTable_Object = MibTable
snmpCommunityTable = _SnmpCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 7, 1)
)
if mibBuilder.loadTexts:
    snmpCommunityTable.setStatus("current")
_SnmpCommunityEntry_Object = MibTableRow
snmpCommunityEntry = _SnmpCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 7, 1, 1)
)
snmpCommunityEntry.setIndexNames(
    (1, "ASKEY-SYSTEM-MIB", "snmpCommunityName"),
)
if mibBuilder.loadTexts:
    snmpCommunityEntry.setStatus("current")


class _SnmpCommunityName_Type(DisplayString):
    """Custom type snmpCommunityName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_SnmpCommunityName_Type.__name__ = "DisplayString"
_SnmpCommunityName_Object = MibTableColumn
snmpCommunityName = _SnmpCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 7, 1, 1, 1),
    _SnmpCommunityName_Type()
)
snmpCommunityName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snmpCommunityName.setStatus("current")


class _SnmpCommunityPermission_Type(Integer32):
    """Custom type snmpCommunityPermission based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("readOnly", 1),
          ("readWrite", 2))
    )


_SnmpCommunityPermission_Type.__name__ = "Integer32"
_SnmpCommunityPermission_Object = MibTableColumn
snmpCommunityPermission = _SnmpCommunityPermission_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 7, 1, 1, 2),
    _SnmpCommunityPermission_Type()
)
snmpCommunityPermission.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpCommunityPermission.setStatus("current")
_SnmpCommunityRowStatus_Type = RowStatus
_SnmpCommunityRowStatus_Object = MibTableColumn
snmpCommunityRowStatus = _SnmpCommunityRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 7, 1, 1, 3),
    _SnmpCommunityRowStatus_Type()
)
snmpCommunityRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    snmpCommunityRowStatus.setStatus("current")
_AskeyDslamFdbTable_Object = MibTable
askeyDslamFdbTable = _AskeyDslamFdbTable_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 9)
)
if mibBuilder.loadTexts:
    askeyDslamFdbTable.setStatus("current")
_AskeyDslamFdbEntry_Object = MibTableRow
askeyDslamFdbEntry = _AskeyDslamFdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 9, 1)
)
askeyDslamFdbEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ASKEY-SYSTEM-MIB", "fdbMacIndex"),
)
if mibBuilder.loadTexts:
    askeyDslamFdbEntry.setStatus("current")


class _FdbMacIndex_Type(Integer32):
    """Custom type fdbMacIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_FdbMacIndex_Type.__name__ = "Integer32"
_FdbMacIndex_Object = MibTableColumn
fdbMacIndex = _FdbMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 9, 1, 1),
    _FdbMacIndex_Type()
)
fdbMacIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbMacIndex.setStatus("current")


class _FdbVpi_Type(Integer32):
    """Custom type fdbVpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FdbVpi_Type.__name__ = "Integer32"
_FdbVpi_Object = MibTableColumn
fdbVpi = _FdbVpi_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 9, 1, 2),
    _FdbVpi_Type()
)
fdbVpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbVpi.setStatus("current")


class _FdbVci_Type(Integer32):
    """Custom type fdbVci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FdbVci_Type.__name__ = "Integer32"
_FdbVci_Object = MibTableColumn
fdbVci = _FdbVci_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 9, 1, 3),
    _FdbVci_Type()
)
fdbVci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fdbVci.setStatus("current")
_MacAddress_Type = MacAddress
_MacAddress_Object = MibTableColumn
macAddress = _MacAddress_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 9, 1, 4),
    _MacAddress_Type()
)
macAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    macAddress.setStatus("current")


class _AskeyDslamFdbStatus_Type(Integer32):
    """Custom type askeyDslamFdbStatus based on Integer32"""
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
        *(("learned-routed", 6),
          ("learned-spoofed-active", 2),
          ("learned-spoofed-inactive", 3),
          ("learned-unique", 1),
          ("mgmt-forbid", 4),
          ("mgmt-permit", 5))
    )


_AskeyDslamFdbStatus_Type.__name__ = "Integer32"
_AskeyDslamFdbStatus_Object = MibTableColumn
askeyDslamFdbStatus = _AskeyDslamFdbStatus_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 9, 1, 5),
    _AskeyDslamFdbStatus_Type()
)
askeyDslamFdbStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    askeyDslamFdbStatus.setStatus("current")


class _ConfigDataMib_Type(Integer32):
    """Custom type configDataMib based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("restore", 2),
          ("save", 1))
    )


_ConfigDataMib_Type.__name__ = "Integer32"
_ConfigDataMib_Object = MibScalar
configDataMib = _ConfigDataMib_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 10),
    _ConfigDataMib_Type()
)
configDataMib.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configDataMib.setStatus("current")
_AskeyCardInfoTable_Object = MibTable
askeyCardInfoTable = _AskeyCardInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 11)
)
if mibBuilder.loadTexts:
    askeyCardInfoTable.setStatus("current")
_AskeyCardInfoEntry_Object = MibTableRow
askeyCardInfoEntry = _AskeyCardInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 11, 1)
)
askeyCardInfoEntry.setIndexNames(
    (0, "ASKEY-ENTITY-ALARM-MIB", "aeAlarmPhysicalIndex"),
)
if mibBuilder.loadTexts:
    askeyCardInfoEntry.setStatus("current")
_AskeyCardPlannedType_Type = Integer32
_AskeyCardPlannedType_Object = MibTableColumn
askeyCardPlannedType = _AskeyCardPlannedType_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 11, 1, 1),
    _AskeyCardPlannedType_Type()
)
askeyCardPlannedType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    askeyCardPlannedType.setStatus("current")
_AskeyCardType_Type = Integer32
_AskeyCardType_Object = MibTableColumn
askeyCardType = _AskeyCardType_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 11, 1, 2),
    _AskeyCardType_Type()
)
askeyCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    askeyCardType.setStatus("current")


class _AskeyCardHWVersion_Type(DisplayString):
    """Custom type askeyCardHWVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_AskeyCardHWVersion_Type.__name__ = "DisplayString"
_AskeyCardHWVersion_Object = MibTableColumn
askeyCardHWVersion = _AskeyCardHWVersion_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 11, 1, 3),
    _AskeyCardHWVersion_Type()
)
askeyCardHWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    askeyCardHWVersion.setStatus("current")


class _AskeyCardSWVersion_Type(DisplayString):
    """Custom type askeyCardSWVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_AskeyCardSWVersion_Type.__name__ = "DisplayString"
_AskeyCardSWVersion_Object = MibTableColumn
askeyCardSWVersion = _AskeyCardSWVersion_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 11, 1, 4),
    _AskeyCardSWVersion_Type()
)
askeyCardSWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    askeyCardSWVersion.setStatus("current")


class _AskeyCardImage_Type(DisplayString):
    """Custom type askeyCardImage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_AskeyCardImage_Type.__name__ = "DisplayString"
_AskeyCardImage_Object = MibTableColumn
askeyCardImage = _AskeyCardImage_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 11, 1, 5),
    _AskeyCardImage_Type()
)
askeyCardImage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    askeyCardImage.setStatus("current")
_AskeyCardUptime_Type = Integer32
_AskeyCardUptime_Object = MibTableColumn
askeyCardUptime = _AskeyCardUptime_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 11, 1, 6),
    _AskeyCardUptime_Type()
)
askeyCardUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    askeyCardUptime.setStatus("current")


class _AskeyCardRole_Type(Integer32):
    """Custom type askeyCardRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("standby", 2))
    )


_AskeyCardRole_Type.__name__ = "Integer32"
_AskeyCardRole_Object = MibTableColumn
askeyCardRole = _AskeyCardRole_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 11, 1, 7),
    _AskeyCardRole_Type()
)
askeyCardRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    askeyCardRole.setStatus("current")


class _AskeyCardSerialNumber_Type(DisplayString):
    """Custom type askeyCardSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_AskeyCardSerialNumber_Type.__name__ = "DisplayString"
_AskeyCardSerialNumber_Object = MibTableColumn
askeyCardSerialNumber = _AskeyCardSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 11, 1, 8),
    _AskeyCardSerialNumber_Type()
)
askeyCardSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    askeyCardSerialNumber.setStatus("current")


class _AskeyCardAdminStatus_Type(Integer32):
    """Custom type askeyCardAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_AskeyCardAdminStatus_Type.__name__ = "Integer32"
_AskeyCardAdminStatus_Object = MibTableColumn
askeyCardAdminStatus = _AskeyCardAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 11, 1, 9),
    _AskeyCardAdminStatus_Type()
)
askeyCardAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    askeyCardAdminStatus.setStatus("current")


class _AskeyCardOperStatus_Type(Integer32):
    """Custom type askeyCardOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notOperational", 2),
          ("notPresent", 3),
          ("operational", 1))
    )


_AskeyCardOperStatus_Type.__name__ = "Integer32"
_AskeyCardOperStatus_Object = MibTableColumn
askeyCardOperStatus = _AskeyCardOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 11, 1, 10),
    _AskeyCardOperStatus_Type()
)
askeyCardOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    askeyCardOperStatus.setStatus("current")


class _LineCardAdminVlanTagPassEnabled_Type(Integer32):
    """Custom type lineCardAdminVlanTagPassEnabled based on Integer32"""
    defaultValue = 2

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


_LineCardAdminVlanTagPassEnabled_Type.__name__ = "Integer32"
_LineCardAdminVlanTagPassEnabled_Object = MibTableColumn
lineCardAdminVlanTagPassEnabled = _LineCardAdminVlanTagPassEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 11, 1, 11),
    _LineCardAdminVlanTagPassEnabled_Type()
)
lineCardAdminVlanTagPassEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineCardAdminVlanTagPassEnabled.setStatus("current")


class _LineCardOperVlanTagPassEnabled_Type(Integer32):
    """Custom type lineCardOperVlanTagPassEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unknown", 0))
    )


_LineCardOperVlanTagPassEnabled_Type.__name__ = "Integer32"
_LineCardOperVlanTagPassEnabled_Object = MibTableColumn
lineCardOperVlanTagPassEnabled = _LineCardOperVlanTagPassEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 11, 1, 12),
    _LineCardOperVlanTagPassEnabled_Type()
)
lineCardOperVlanTagPassEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineCardOperVlanTagPassEnabled.setStatus("current")


class _LineCardAdminRfc2684Encap_Type(Integer32):
    """Custom type lineCardAdminRfc2684Encap based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("llc", 1),
          ("unknown", 0),
          ("vcMux", 2))
    )


_LineCardAdminRfc2684Encap_Type.__name__ = "Integer32"
_LineCardAdminRfc2684Encap_Object = MibTableColumn
lineCardAdminRfc2684Encap = _LineCardAdminRfc2684Encap_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 11, 1, 13),
    _LineCardAdminRfc2684Encap_Type()
)
lineCardAdminRfc2684Encap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineCardAdminRfc2684Encap.setStatus("current")


class _LineCardOperRfc2684Encap_Type(Integer32):
    """Custom type lineCardOperRfc2684Encap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("llc", 1),
          ("unknown", 0),
          ("vcMux", 2))
    )


_LineCardOperRfc2684Encap_Type.__name__ = "Integer32"
_LineCardOperRfc2684Encap_Object = MibTableColumn
lineCardOperRfc2684Encap = _LineCardOperRfc2684Encap_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 11, 1, 14),
    _LineCardOperRfc2684Encap_Type()
)
lineCardOperRfc2684Encap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineCardOperRfc2684Encap.setStatus("current")


class _LineCardServiceTypeControl_Type(Integer32):
    """Custom type lineCardServiceTypeControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unknown", 0))
    )


_LineCardServiceTypeControl_Type.__name__ = "Integer32"
_LineCardServiceTypeControl_Object = MibTableColumn
lineCardServiceTypeControl = _LineCardServiceTypeControl_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 11, 1, 15),
    _LineCardServiceTypeControl_Type()
)
lineCardServiceTypeControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineCardServiceTypeControl.setStatus("current")


class _ShdslFirmwareUpgrade_Type(Integer32):
    """Custom type shdslFirmwareUpgrade based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("upgrade", 0)
    )


_ShdslFirmwareUpgrade_Type.__name__ = "Integer32"
_ShdslFirmwareUpgrade_Object = MibTableColumn
shdslFirmwareUpgrade = _ShdslFirmwareUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 11, 1, 16),
    _ShdslFirmwareUpgrade_Type()
)
shdslFirmwareUpgrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    shdslFirmwareUpgrade.setStatus("current")


class _ShdslFirmwareUpgradeState_Type(Integer32):
    """Custom type shdslFirmwareUpgradeState based on Integer32"""
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
        *(("burning", 3),
          ("driverError", 6),
          ("failedToBurn", 5),
          ("failedToTransmitImage", 8),
          ("finished", 4),
          ("inital", 1),
          ("noFirmwareImage", 7),
          ("transmission", 2),
          ("unknown", 0))
    )


_ShdslFirmwareUpgradeState_Type.__name__ = "Integer32"
_ShdslFirmwareUpgradeState_Object = MibTableColumn
shdslFirmwareUpgradeState = _ShdslFirmwareUpgradeState_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 11, 1, 17),
    _ShdslFirmwareUpgradeState_Type()
)
shdslFirmwareUpgradeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    shdslFirmwareUpgradeState.setStatus("current")


class _TaggedModeAdminStatus_Type(Integer32):
    """Custom type taggedModeAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tagged-only", 1),
          ("untagged-only", 2))
    )


_TaggedModeAdminStatus_Type.__name__ = "Integer32"
_TaggedModeAdminStatus_Object = MibTableColumn
taggedModeAdminStatus = _TaggedModeAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 11, 1, 18),
    _TaggedModeAdminStatus_Type()
)
taggedModeAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    taggedModeAdminStatus.setStatus("current")


class _TaggedModeOperStatus_Type(Integer32):
    """Custom type taggedModeOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tagged-only", 1),
          ("untagged-only", 2))
    )


_TaggedModeOperStatus_Type.__name__ = "Integer32"
_TaggedModeOperStatus_Object = MibTableColumn
taggedModeOperStatus = _TaggedModeOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 11, 1, 19),
    _TaggedModeOperStatus_Type()
)
taggedModeOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taggedModeOperStatus.setStatus("current")
_LinePortInfo_ObjectIdentity = ObjectIdentity
linePortInfo = _LinePortInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 12)
)
_LinePortInfoTable_Object = MibTable
linePortInfoTable = _LinePortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 12, 1)
)
if mibBuilder.loadTexts:
    linePortInfoTable.setStatus("current")
_LinePortInfoEntry_Object = MibTableRow
linePortInfoEntry = _LinePortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 12, 1, 1)
)
linePortInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    linePortInfoEntry.setStatus("current")


class _LinePortAdminStatus_Type(Integer32):
    """Custom type linePortAdminStatus based on Integer32"""
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
        *(("disable", 2),
          ("enable", 1),
          ("reset", 4),
          ("testing", 3))
    )


_LinePortAdminStatus_Type.__name__ = "Integer32"
_LinePortAdminStatus_Object = MibTableColumn
linePortAdminStatus = _LinePortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 12, 1, 1, 1),
    _LinePortAdminStatus_Type()
)
linePortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    linePortAdminStatus.setStatus("current")


class _LinePortOperStatus_Type(Integer32):
    """Custom type linePortOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notOperational", 2),
          ("notPresent", 3),
          ("operational", 1))
    )


_LinePortOperStatus_Type.__name__ = "Integer32"
_LinePortOperStatus_Object = MibTableColumn
linePortOperStatus = _LinePortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 12, 1, 1, 2),
    _LinePortOperStatus_Type()
)
linePortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    linePortOperStatus.setStatus("current")
_CircuitID_Type = SnmpAdminString
_CircuitID_Object = MibTableColumn
circuitID = _CircuitID_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 12, 1, 1, 3),
    _CircuitID_Type()
)
circuitID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    circuitID.setStatus("current")


class _RemoteID_Type(SnmpAdminString):
    """Custom type remoteID based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_RemoteID_Type.__name__ = "SnmpAdminString"
_RemoteID_Object = MibTableColumn
remoteID = _RemoteID_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 12, 1, 1, 4),
    _RemoteID_Type()
)
remoteID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteID.setStatus("current")


class _Dot1TpMACAging_Type(Integer32):
    """Custom type dot1TpMACAging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aged", 1),
          ("nonaged", 2))
    )


_Dot1TpMACAging_Type.__name__ = "Integer32"
_Dot1TpMACAging_Object = MibScalar
dot1TpMACAging = _Dot1TpMACAging_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 13),
    _Dot1TpMACAging_Type()
)
dot1TpMACAging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1TpMACAging.setStatus("current")


class _AskeyRebootSystemAction_Type(Integer32):
    """Custom type askeyRebootSystemAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reboot", 1)
    )


_AskeyRebootSystemAction_Type.__name__ = "Integer32"
_AskeyRebootSystemAction_Object = MibScalar
askeyRebootSystemAction = _AskeyRebootSystemAction_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 14),
    _AskeyRebootSystemAction_Type()
)
askeyRebootSystemAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    askeyRebootSystemAction.setStatus("current")
_AskeyDslamOam_ObjectIdentity = ObjectIdentity
askeyDslamOam = _AskeyDslamOam_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 15)
)
_OamF5_ObjectIdentity = ObjectIdentity
oamF5 = _OamF5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 15, 1)
)
_OamF5IfIndex_Type = Integer32
_OamF5IfIndex_Object = MibScalar
oamF5IfIndex = _OamF5IfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 15, 1, 1),
    _OamF5IfIndex_Type()
)
oamF5IfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oamF5IfIndex.setStatus("current")


class _OamF5Vpi_Type(Integer32):
    """Custom type oamF5Vpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_OamF5Vpi_Type.__name__ = "Integer32"
_OamF5Vpi_Object = MibScalar
oamF5Vpi = _OamF5Vpi_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 15, 1, 2),
    _OamF5Vpi_Type()
)
oamF5Vpi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oamF5Vpi.setStatus("current")


class _OamF5Vci_Type(Integer32):
    """Custom type oamF5Vci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OamF5Vci_Type.__name__ = "Integer32"
_OamF5Vci_Object = MibScalar
oamF5Vci = _OamF5Vci_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 15, 1, 3),
    _OamF5Vci_Type()
)
oamF5Vci.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oamF5Vci.setStatus("current")


class _OamF5Scope_Type(Integer32):
    """Custom type oamF5Scope based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both-end2end-segment2segment", 3),
          ("end-to-end", 1),
          ("segment-to-segment", 2))
    )


_OamF5Scope_Type.__name__ = "Integer32"
_OamF5Scope_Object = MibScalar
oamF5Scope = _OamF5Scope_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 15, 1, 4),
    _OamF5Scope_Type()
)
oamF5Scope.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oamF5Scope.setStatus("current")
_AskeySystemManagementInfo_ObjectIdentity = ObjectIdentity
askeySystemManagementInfo = _AskeySystemManagementInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 16)
)


class _AskeyEmsVlanId_Type(Integer32):
    """Custom type askeyEmsVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AskeyEmsVlanId_Type.__name__ = "Integer32"
_AskeyEmsVlanId_Object = MibScalar
askeyEmsVlanId = _AskeyEmsVlanId_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 16, 1),
    _AskeyEmsVlanId_Type()
)
askeyEmsVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    askeyEmsVlanId.setStatus("current")
_AskeyBootDevice_ObjectIdentity = ObjectIdentity
askeyBootDevice = _AskeyBootDevice_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 16, 2)
)


class _AskeyNextBootDevice_Type(Integer32):
    """Custom type askeyNextBootDevice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("opCodeA", 1),
          ("opCodeB", 2))
    )


_AskeyNextBootDevice_Type.__name__ = "Integer32"
_AskeyNextBootDevice_Object = MibScalar
askeyNextBootDevice = _AskeyNextBootDevice_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 16, 2, 1),
    _AskeyNextBootDevice_Type()
)
askeyNextBootDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    askeyNextBootDevice.setStatus("current")


class _AskeyCurrentBootDevice_Type(Integer32):
    """Custom type askeyCurrentBootDevice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("network", 0),
          ("opCodeA", 1),
          ("opCodeB", 2))
    )


_AskeyCurrentBootDevice_Type.__name__ = "Integer32"
_AskeyCurrentBootDevice_Object = MibScalar
askeyCurrentBootDevice = _AskeyCurrentBootDevice_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 16, 2, 2),
    _AskeyCurrentBootDevice_Type()
)
askeyCurrentBootDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    askeyCurrentBootDevice.setStatus("current")


class _AskeySystemManagementIgmp_Type(Integer32):
    """Custom type askeySystemManagementIgmp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disableIgmp", 3),
          ("enableIgmpproxy", 2),
          ("enableIgmpsnoop", 1))
    )


_AskeySystemManagementIgmp_Type.__name__ = "Integer32"
_AskeySystemManagementIgmp_Object = MibScalar
askeySystemManagementIgmp = _AskeySystemManagementIgmp_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 16, 3),
    _AskeySystemManagementIgmp_Type()
)
askeySystemManagementIgmp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    askeySystemManagementIgmp.setStatus("current")
_AskeyRedundancy_ObjectIdentity = ObjectIdentity
askeyRedundancy = _AskeyRedundancy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 16, 4)
)


class _AskeyRedundancyAutoSyncEnabled_Type(Integer32):
    """Custom type askeyRedundancyAutoSyncEnabled based on Integer32"""
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


_AskeyRedundancyAutoSyncEnabled_Type.__name__ = "Integer32"
_AskeyRedundancyAutoSyncEnabled_Object = MibScalar
askeyRedundancyAutoSyncEnabled = _AskeyRedundancyAutoSyncEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 16, 4, 1),
    _AskeyRedundancyAutoSyncEnabled_Type()
)
askeyRedundancyAutoSyncEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    askeyRedundancyAutoSyncEnabled.setStatus("current")


class _AskeyRedundancyAutoSyncPeriod_Type(Integer32):
    """Custom type askeyRedundancyAutoSyncPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 3600),
    )


_AskeyRedundancyAutoSyncPeriod_Type.__name__ = "Integer32"
_AskeyRedundancyAutoSyncPeriod_Object = MibScalar
askeyRedundancyAutoSyncPeriod = _AskeyRedundancyAutoSyncPeriod_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 16, 4, 2),
    _AskeyRedundancyAutoSyncPeriod_Type()
)
askeyRedundancyAutoSyncPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    askeyRedundancyAutoSyncPeriod.setStatus("current")


class _AskeyRedundancySync_Type(Integer32):
    """Custom type askeyRedundancySync based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("syncNow", 1)
    )


_AskeyRedundancySync_Type.__name__ = "Integer32"
_AskeyRedundancySync_Object = MibScalar
askeyRedundancySync = _AskeyRedundancySync_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 16, 4, 3),
    _AskeyRedundancySync_Type()
)
askeyRedundancySync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    askeyRedundancySync.setStatus("current")
_AskeySystemManagementInfoVlan_ObjectIdentity = ObjectIdentity
askeySystemManagementInfoVlan = _AskeySystemManagementInfoVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 16, 5)
)
_AskeySystemManagementInfoVlanMacLimitTable_Object = MibTable
askeySystemManagementInfoVlanMacLimitTable = _AskeySystemManagementInfoVlanMacLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 16, 5, 1)
)
if mibBuilder.loadTexts:
    askeySystemManagementInfoVlanMacLimitTable.setStatus("current")
_AskeySystemManagementInfoVlanMacLimitEntry_Object = MibTableRow
askeySystemManagementInfoVlanMacLimitEntry = _AskeySystemManagementInfoVlanMacLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 16, 5, 1, 1)
)
askeySystemManagementInfoVlanMacLimitEntry.setIndexNames(
    (0, "ASKEY-SYSTEM-MIB", "askeySystemManagementInfoVlanID"),
)
if mibBuilder.loadTexts:
    askeySystemManagementInfoVlanMacLimitEntry.setStatus("current")


class _AskeySystemManagementInfoVlanID_Type(Integer32):
    """Custom type askeySystemManagementInfoVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AskeySystemManagementInfoVlanID_Type.__name__ = "Integer32"
_AskeySystemManagementInfoVlanID_Object = MibTableColumn
askeySystemManagementInfoVlanID = _AskeySystemManagementInfoVlanID_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 16, 5, 1, 1, 1),
    _AskeySystemManagementInfoVlanID_Type()
)
askeySystemManagementInfoVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    askeySystemManagementInfoVlanID.setStatus("current")


class _AskeySystemManagementInfoVlanMacLimit_Type(Integer32):
    """Custom type askeySystemManagementInfoVlanMacLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 50000),
    )


_AskeySystemManagementInfoVlanMacLimit_Type.__name__ = "Integer32"
_AskeySystemManagementInfoVlanMacLimit_Object = MibTableColumn
askeySystemManagementInfoVlanMacLimit = _AskeySystemManagementInfoVlanMacLimit_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 16, 5, 1, 1, 2),
    _AskeySystemManagementInfoVlanMacLimit_Type()
)
askeySystemManagementInfoVlanMacLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    askeySystemManagementInfoVlanMacLimit.setStatus("current")


class _AskeySystemManagementInfoVlanMacLimitEnabled_Type(Integer32):
    """Custom type askeySystemManagementInfoVlanMacLimitEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("unknown", 0))
    )


_AskeySystemManagementInfoVlanMacLimitEnabled_Type.__name__ = "Integer32"
_AskeySystemManagementInfoVlanMacLimitEnabled_Object = MibTableColumn
askeySystemManagementInfoVlanMacLimitEnabled = _AskeySystemManagementInfoVlanMacLimitEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 16, 5, 1, 1, 3),
    _AskeySystemManagementInfoVlanMacLimitEnabled_Type()
)
askeySystemManagementInfoVlanMacLimitEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    askeySystemManagementInfoVlanMacLimitEnabled.setStatus("current")
_AskeyCosQueue_ObjectIdentity = ObjectIdentity
askeyCosQueue = _AskeyCosQueue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 18)
)
_AskeyCosQueueMappingTable_Object = MibTable
askeyCosQueueMappingTable = _AskeyCosQueueMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 18, 1)
)
if mibBuilder.loadTexts:
    askeyCosQueueMappingTable.setStatus("current")
_AskeyCosQueueMappingEntry_Object = MibTableRow
askeyCosQueueMappingEntry = _AskeyCosQueueMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 18, 1, 1)
)
askeyCosQueueMappingEntry.setIndexNames(
    (0, "ASKEY-SYSTEM-MIB", "askeyCosQueueMapping8021p"),
)
if mibBuilder.loadTexts:
    askeyCosQueueMappingEntry.setStatus("current")


class _AskeyCosQueueMapping8021p_Type(Integer32):
    """Custom type askeyCosQueueMapping8021p based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AskeyCosQueueMapping8021p_Type.__name__ = "Integer32"
_AskeyCosQueueMapping8021p_Object = MibTableColumn
askeyCosQueueMapping8021p = _AskeyCosQueueMapping8021p_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 18, 1, 1, 1),
    _AskeyCosQueueMapping8021p_Type()
)
askeyCosQueueMapping8021p.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    askeyCosQueueMapping8021p.setStatus("current")


class _AskeyCosQueueIndex_Type(Integer32):
    """Custom type askeyCosQueueIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AskeyCosQueueIndex_Type.__name__ = "Integer32"
_AskeyCosQueueIndex_Object = MibTableColumn
askeyCosQueueIndex = _AskeyCosQueueIndex_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 18, 1, 1, 2),
    _AskeyCosQueueIndex_Type()
)
askeyCosQueueIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    askeyCosQueueIndex.setStatus("current")
_AskeySystemUserAccountTable_Object = MibTable
askeySystemUserAccountTable = _AskeySystemUserAccountTable_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 19)
)
if mibBuilder.loadTexts:
    askeySystemUserAccountTable.setStatus("current")
_AskeySystemUserAccountEntry_Object = MibTableRow
askeySystemUserAccountEntry = _AskeySystemUserAccountEntry_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 19, 1)
)
askeySystemUserAccountEntry.setIndexNames(
    (0, "ASKEY-SYSTEM-MIB", "askeySystemUserAccountUserName"),
)
if mibBuilder.loadTexts:
    askeySystemUserAccountEntry.setStatus("current")


class _AskeySystemUserAccountUserName_Type(SnmpAdminString):
    """Custom type askeySystemUserAccountUserName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_AskeySystemUserAccountUserName_Type.__name__ = "SnmpAdminString"
_AskeySystemUserAccountUserName_Object = MibTableColumn
askeySystemUserAccountUserName = _AskeySystemUserAccountUserName_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 19, 1, 1),
    _AskeySystemUserAccountUserName_Type()
)
askeySystemUserAccountUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    askeySystemUserAccountUserName.setStatus("current")


class _AskeySystemUserAccountPassword_Type(SnmpAdminString):
    """Custom type askeySystemUserAccountPassword based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_AskeySystemUserAccountPassword_Type.__name__ = "SnmpAdminString"
_AskeySystemUserAccountPassword_Object = MibTableColumn
askeySystemUserAccountPassword = _AskeySystemUserAccountPassword_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 19, 1, 2),
    _AskeySystemUserAccountPassword_Type()
)
askeySystemUserAccountPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    askeySystemUserAccountPassword.setStatus("current")


class _AskeySystemUserAccountGroup_Type(Integer32):
    """Custom type askeySystemUserAccountGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("admin", 2),
          ("guest", 1))
    )


_AskeySystemUserAccountGroup_Type.__name__ = "Integer32"
_AskeySystemUserAccountGroup_Object = MibTableColumn
askeySystemUserAccountGroup = _AskeySystemUserAccountGroup_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 19, 1, 3),
    _AskeySystemUserAccountGroup_Type()
)
askeySystemUserAccountGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    askeySystemUserAccountGroup.setStatus("current")
_AskeySystemUserAccountRowStatus_Type = RowStatus
_AskeySystemUserAccountRowStatus_Object = MibTableColumn
askeySystemUserAccountRowStatus = _AskeySystemUserAccountRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 19, 1, 4),
    _AskeySystemUserAccountRowStatus_Type()
)
askeySystemUserAccountRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    askeySystemUserAccountRowStatus.setStatus("current")
_AskeyPPPoE_ObjectIdentity = ObjectIdentity
askeyPPPoE = _AskeyPPPoE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 20)
)


class _Suboption_Type(Integer32):
    """Custom type suboption based on Integer32"""
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


_Suboption_Type.__name__ = "Integer32"
_Suboption_Object = MibScalar
suboption = _Suboption_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 20, 1),
    _Suboption_Type()
)
suboption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    suboption.setStatus("current")
_DnsService_ObjectIdentity = ObjectIdentity
dnsService = _DnsService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 21)
)
_DnsServer1IPAddress_Type = IpAddress
_DnsServer1IPAddress_Object = MibScalar
dnsServer1IPAddress = _DnsServer1IPAddress_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 21, 1),
    _DnsServer1IPAddress_Type()
)
dnsServer1IPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsServer1IPAddress.setStatus("current")
_DnsServer2IPAddress_Type = IpAddress
_DnsServer2IPAddress_Object = MibScalar
dnsServer2IPAddress = _DnsServer2IPAddress_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 21, 2),
    _DnsServer2IPAddress_Type()
)
dnsServer2IPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsServer2IPAddress.setStatus("current")
_DnsServer3IPAddress_Type = IpAddress
_DnsServer3IPAddress_Object = MibScalar
dnsServer3IPAddress = _DnsServer3IPAddress_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 21, 3),
    _DnsServer3IPAddress_Type()
)
dnsServer3IPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsServer3IPAddress.setStatus("current")
_TimeService_ObjectIdentity = ObjectIdentity
timeService = _TimeService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 22)
)


class _Protocol_Type(Integer32):
    """Custom type protocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("sntp", 1))
    )


_Protocol_Type.__name__ = "Integer32"
_Protocol_Object = MibScalar
protocol = _Protocol_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 22, 1),
    _Protocol_Type()
)
protocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    protocol.setStatus("current")


class _UpdatePeriod_Type(Unsigned32):
    """Custom type updatePeriod based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_UpdatePeriod_Type.__name__ = "Unsigned32"
_UpdatePeriod_Object = MibScalar
updatePeriod = _UpdatePeriod_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 22, 2),
    _UpdatePeriod_Type()
)
updatePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    updatePeriod.setStatus("current")


class _TimeServer1InetAddress_Type(InetAddress):
    """Custom type timeServer1InetAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_TimeServer1InetAddress_Type.__name__ = "InetAddress"
_TimeServer1InetAddress_Object = MibScalar
timeServer1InetAddress = _TimeServer1InetAddress_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 22, 3),
    _TimeServer1InetAddress_Type()
)
timeServer1InetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeServer1InetAddress.setStatus("current")


class _TimeServer2InetAddress_Type(InetAddress):
    """Custom type timeServer2InetAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_TimeServer2InetAddress_Type.__name__ = "InetAddress"
_TimeServer2InetAddress_Object = MibScalar
timeServer2InetAddress = _TimeServer2InetAddress_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 22, 4),
    _TimeServer2InetAddress_Type()
)
timeServer2InetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeServer2InetAddress.setStatus("current")


class _TimeServer3InetAddress_Type(InetAddress):
    """Custom type timeServer3InetAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_TimeServer3InetAddress_Type.__name__ = "InetAddress"
_TimeServer3InetAddress_Object = MibScalar
timeServer3InetAddress = _TimeServer3InetAddress_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 22, 5),
    _TimeServer3InetAddress_Type()
)
timeServer3InetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeServer3InetAddress.setStatus("current")


class _TimeServer1Status_Type(Integer32):
    """Custom type timeServer1Status based on Integer32"""
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
        *(("backupMode", 2),
          ("failToResolveDomainName", 3),
          ("networkTimeSource", 1),
          ("notSet", 0),
          ("serverNoResponse", 4))
    )


_TimeServer1Status_Type.__name__ = "Integer32"
_TimeServer1Status_Object = MibScalar
timeServer1Status = _TimeServer1Status_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 22, 6),
    _TimeServer1Status_Type()
)
timeServer1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeServer1Status.setStatus("current")


class _TimeServer2Status_Type(Integer32):
    """Custom type timeServer2Status based on Integer32"""
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
        *(("backupMode", 2),
          ("failToResolveDomainName", 3),
          ("networkTimeSource", 1),
          ("notSet", 0),
          ("serverNoResponse", 4))
    )


_TimeServer2Status_Type.__name__ = "Integer32"
_TimeServer2Status_Object = MibScalar
timeServer2Status = _TimeServer2Status_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 22, 7),
    _TimeServer2Status_Type()
)
timeServer2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeServer2Status.setStatus("current")


class _TimeServer3Status_Type(Integer32):
    """Custom type timeServer3Status based on Integer32"""
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
        *(("backupMode", 2),
          ("failToResolveDomainName", 3),
          ("networkTimeSource", 1),
          ("notSet", 0),
          ("serverNoResponse", 4))
    )


_TimeServer3Status_Type.__name__ = "Integer32"
_TimeServer3Status_Object = MibScalar
timeServer3Status = _TimeServer3Status_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 22, 8),
    _TimeServer3Status_Type()
)
timeServer3Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    timeServer3Status.setStatus("current")


class _TimeZone_Type(Integer32):
    """Custom type timeZone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-12, 13),
    )


_TimeZone_Type.__name__ = "Integer32"
_TimeZone_Object = MibScalar
timeZone = _TimeZone_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 22, 9),
    _TimeZone_Type()
)
timeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    timeZone.setStatus("current")
_UgeMIBObjects_ObjectIdentity = ObjectIdentity
ugeMIBObjects = _UgeMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 23)
)
_UgeAutoNegotiationTable_Object = MibTable
ugeAutoNegotiationTable = _UgeAutoNegotiationTable_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 23, 2)
)
if mibBuilder.loadTexts:
    ugeAutoNegotiationTable.setStatus("current")
_UgeAutoNegotionEntry_Object = MibTableRow
ugeAutoNegotionEntry = _UgeAutoNegotionEntry_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 23, 2, 1)
)
ugeAutoNegotionEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ugeAutoNegotionEntry.setStatus("current")


class _AutoNegotiationState_Type(Integer32):
    """Custom type autoNegotiationState based on Integer32"""
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


_AutoNegotiationState_Type.__name__ = "Integer32"
_AutoNegotiationState_Object = MibTableColumn
autoNegotiationState = _AutoNegotiationState_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 23, 2, 1, 1),
    _AutoNegotiationState_Type()
)
autoNegotiationState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autoNegotiationState.setStatus("current")
_UgePauseFrameStatisticTable_Object = MibTable
ugePauseFrameStatisticTable = _UgePauseFrameStatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 23, 3)
)
if mibBuilder.loadTexts:
    ugePauseFrameStatisticTable.setStatus("current")
_UgePauseFrameStatisticEntry_Object = MibTableRow
ugePauseFrameStatisticEntry = _UgePauseFrameStatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 23, 3, 1)
)
ugePauseFrameStatisticEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ugePauseFrameStatisticEntry.setStatus("current")
_RxPausePackets_Type = Unsigned32
_RxPausePackets_Object = MibTableColumn
rxPausePackets = _RxPausePackets_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 23, 3, 1, 1),
    _RxPausePackets_Type()
)
rxPausePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rxPausePackets.setStatus("current")
_TxPausePackets_Type = Unsigned32
_TxPausePackets_Object = MibTableColumn
txPausePackets = _TxPausePackets_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 23, 3, 1, 2),
    _TxPausePackets_Type()
)
txPausePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    txPausePackets.setStatus("current")
_SubtendVLANTable_Object = MibTable
subtendVLANTable = _SubtendVLANTable_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 23, 4)
)
if mibBuilder.loadTexts:
    subtendVLANTable.setStatus("current")
_SubtendVLANEntry_Object = MibTableRow
subtendVLANEntry = _SubtendVLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 23, 4, 1)
)
subtendVLANEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    subtendVLANEntry.setStatus("current")


class _SubtendState_Type(Integer32):
    """Custom type subtendState based on Integer32"""
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


_SubtendState_Type.__name__ = "Integer32"
_SubtendState_Object = MibTableColumn
subtendState = _SubtendState_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 23, 4, 1, 1),
    _SubtendState_Type()
)
subtendState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subtendState.setStatus("current")
_SubtendVLAN_Type = VLANList
_SubtendVLAN_Object = MibTableColumn
subtendVLAN = _SubtendVLAN_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 23, 4, 1, 2),
    _SubtendVLAN_Type()
)
subtendVLAN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subtendVLAN.setStatus("current")
_UgeVLANTable_Object = MibTable
ugeVLANTable = _UgeVLANTable_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 23, 5)
)
if mibBuilder.loadTexts:
    ugeVLANTable.setStatus("current")
_UgeVLANEntry_Object = MibTableRow
ugeVLANEntry = _UgeVLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 23, 5, 1)
)
ugeVLANEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ugeVLANEntry.setStatus("current")
_UgeVLAN_Type = VLANList
_UgeVLAN_Object = MibTableColumn
ugeVLAN = _UgeVLAN_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 23, 5, 1, 1),
    _UgeVLAN_Type()
)
ugeVLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ugeVLAN.setStatus("current")
_SecuredHosts_ObjectIdentity = ObjectIdentity
securedHosts = _SecuredHosts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 24)
)


class _SecuredHostAdminStatus_Type(Integer32):
    """Custom type securedHostAdminStatus based on Integer32"""
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


_SecuredHostAdminStatus_Type.__name__ = "Integer32"
_SecuredHostAdminStatus_Object = MibScalar
securedHostAdminStatus = _SecuredHostAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 24, 1),
    _SecuredHostAdminStatus_Type()
)
securedHostAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securedHostAdminStatus.setStatus("current")
_SecuredHostTable_Object = MibTable
securedHostTable = _SecuredHostTable_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 24, 2)
)
if mibBuilder.loadTexts:
    securedHostTable.setStatus("current")
_SecuredHostEntry_Object = MibTableRow
securedHostEntry = _SecuredHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 24, 2, 1)
)
securedHostEntry.setIndexNames(
    (0, "ASKEY-SYSTEM-MIB", "securedIPSectorIndex"),
)
if mibBuilder.loadTexts:
    securedHostEntry.setStatus("current")
_SecuredIPSectorIndex_Type = IPSectionIndex
_SecuredIPSectorIndex_Object = MibTableColumn
securedIPSectorIndex = _SecuredIPSectorIndex_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 24, 2, 1, 1),
    _SecuredIPSectorIndex_Type()
)
securedIPSectorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    securedIPSectorIndex.setStatus("current")
_SecuredIPSectorStartIP_Type = IpAddress
_SecuredIPSectorStartIP_Object = MibTableColumn
securedIPSectorStartIP = _SecuredIPSectorStartIP_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 24, 2, 1, 2),
    _SecuredIPSectorStartIP_Type()
)
securedIPSectorStartIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securedIPSectorStartIP.setStatus("current")
_SecuredIPSectorEndIP_Type = IpAddress
_SecuredIPSectorEndIP_Object = MibTableColumn
securedIPSectorEndIP = _SecuredIPSectorEndIP_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 24, 2, 1, 3),
    _SecuredIPSectorEndIP_Type()
)
securedIPSectorEndIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securedIPSectorEndIP.setStatus("current")


class _AllowedServiceType_Type(Bits):
    """Custom type allowedServiceType based on Bits"""
    namedValues = NamedValues(
        *(("ftp", 2),
          ("snmp", 0),
          ("telnet", 1),
          ("tftp", 3))
    )

_AllowedServiceType_Type.__name__ = "Bits"
_AllowedServiceType_Object = MibTableColumn
allowedServiceType = _AllowedServiceType_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 24, 2, 1, 4),
    _AllowedServiceType_Type()
)
allowedServiceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    allowedServiceType.setStatus("current")
_NetBIOSFilter_ObjectIdentity = ObjectIdentity
netBIOSFilter = _NetBIOSFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 25)
)


class _NetBIOSFilterAction_Type(Integer32):
    """Custom type netBIOSFilterAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dropping", 1),
          ("forwarding", 2))
    )


_NetBIOSFilterAction_Type.__name__ = "Integer32"
_NetBIOSFilterAction_Object = MibScalar
netBIOSFilterAction = _NetBIOSFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 3646, 1300, 2, 1, 25, 1),
    _NetBIOSFilterAction_Type()
)
netBIOSFilterAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netBIOSFilterAction.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ASKEY-SYSTEM-MIB",
    **{"MacAddress": MacAddress,
       "IPSectionIndex": IPSectionIndex,
       "VLANList": VLANList,
       "askeySystemMib": askeySystemMib,
       "ipConfig": ipConfig,
       "nodeIP": nodeIP,
       "nodeIPAddr": nodeIPAddr,
       "nodeIPNetMask": nodeIPNetMask,
       "nodeMACAddr": nodeMACAddr,
       "gatewayIPAddr": gatewayIPAddr,
       "mgmtIP": mgmtIP,
       "mgmtIPAddr": mgmtIPAddr,
       "mgmtIPNetMask": mgmtIPNetMask,
       "mgmtMACAddr": mgmtMACAddr,
       "nodeTime": nodeTime,
       "time": time,
       "zone": zone,
       "snmpTrapMib": snmpTrapMib,
       "snmpTrapTable": snmpTrapTable,
       "snmpTrapEntry": snmpTrapEntry,
       "snmpTrapStation": snmpTrapStation,
       "snmpTrapCommunity": snmpTrapCommunity,
       "snmpTrapSNMPVersion": snmpTrapSNMPVersion,
       "snmpTrapRowStatus": snmpTrapRowStatus,
       "snmpCommunityMib": snmpCommunityMib,
       "snmpCommunityTable": snmpCommunityTable,
       "snmpCommunityEntry": snmpCommunityEntry,
       "snmpCommunityName": snmpCommunityName,
       "snmpCommunityPermission": snmpCommunityPermission,
       "snmpCommunityRowStatus": snmpCommunityRowStatus,
       "askeyDslamFdbTable": askeyDslamFdbTable,
       "askeyDslamFdbEntry": askeyDslamFdbEntry,
       "fdbMacIndex": fdbMacIndex,
       "fdbVpi": fdbVpi,
       "fdbVci": fdbVci,
       "macAddress": macAddress,
       "askeyDslamFdbStatus": askeyDslamFdbStatus,
       "configDataMib": configDataMib,
       "askeyCardInfoTable": askeyCardInfoTable,
       "askeyCardInfoEntry": askeyCardInfoEntry,
       "askeyCardPlannedType": askeyCardPlannedType,
       "askeyCardType": askeyCardType,
       "askeyCardHWVersion": askeyCardHWVersion,
       "askeyCardSWVersion": askeyCardSWVersion,
       "askeyCardImage": askeyCardImage,
       "askeyCardUptime": askeyCardUptime,
       "askeyCardRole": askeyCardRole,
       "askeyCardSerialNumber": askeyCardSerialNumber,
       "askeyCardAdminStatus": askeyCardAdminStatus,
       "askeyCardOperStatus": askeyCardOperStatus,
       "lineCardAdminVlanTagPassEnabled": lineCardAdminVlanTagPassEnabled,
       "lineCardOperVlanTagPassEnabled": lineCardOperVlanTagPassEnabled,
       "lineCardAdminRfc2684Encap": lineCardAdminRfc2684Encap,
       "lineCardOperRfc2684Encap": lineCardOperRfc2684Encap,
       "lineCardServiceTypeControl": lineCardServiceTypeControl,
       "shdslFirmwareUpgrade": shdslFirmwareUpgrade,
       "shdslFirmwareUpgradeState": shdslFirmwareUpgradeState,
       "taggedModeAdminStatus": taggedModeAdminStatus,
       "taggedModeOperStatus": taggedModeOperStatus,
       "linePortInfo": linePortInfo,
       "linePortInfoTable": linePortInfoTable,
       "linePortInfoEntry": linePortInfoEntry,
       "linePortAdminStatus": linePortAdminStatus,
       "linePortOperStatus": linePortOperStatus,
       "circuitID": circuitID,
       "remoteID": remoteID,
       "dot1TpMACAging": dot1TpMACAging,
       "askeyRebootSystemAction": askeyRebootSystemAction,
       "askeyDslamOam": askeyDslamOam,
       "oamF5": oamF5,
       "oamF5IfIndex": oamF5IfIndex,
       "oamF5Vpi": oamF5Vpi,
       "oamF5Vci": oamF5Vci,
       "oamF5Scope": oamF5Scope,
       "askeySystemManagementInfo": askeySystemManagementInfo,
       "askeyEmsVlanId": askeyEmsVlanId,
       "askeyBootDevice": askeyBootDevice,
       "askeyNextBootDevice": askeyNextBootDevice,
       "askeyCurrentBootDevice": askeyCurrentBootDevice,
       "askeySystemManagementIgmp": askeySystemManagementIgmp,
       "askeyRedundancy": askeyRedundancy,
       "askeyRedundancyAutoSyncEnabled": askeyRedundancyAutoSyncEnabled,
       "askeyRedundancyAutoSyncPeriod": askeyRedundancyAutoSyncPeriod,
       "askeyRedundancySync": askeyRedundancySync,
       "askeySystemManagementInfoVlan": askeySystemManagementInfoVlan,
       "askeySystemManagementInfoVlanMacLimitTable": askeySystemManagementInfoVlanMacLimitTable,
       "askeySystemManagementInfoVlanMacLimitEntry": askeySystemManagementInfoVlanMacLimitEntry,
       "askeySystemManagementInfoVlanID": askeySystemManagementInfoVlanID,
       "askeySystemManagementInfoVlanMacLimit": askeySystemManagementInfoVlanMacLimit,
       "askeySystemManagementInfoVlanMacLimitEnabled": askeySystemManagementInfoVlanMacLimitEnabled,
       "askeyCosQueue": askeyCosQueue,
       "askeyCosQueueMappingTable": askeyCosQueueMappingTable,
       "askeyCosQueueMappingEntry": askeyCosQueueMappingEntry,
       "askeyCosQueueMapping8021p": askeyCosQueueMapping8021p,
       "askeyCosQueueIndex": askeyCosQueueIndex,
       "askeySystemUserAccountTable": askeySystemUserAccountTable,
       "askeySystemUserAccountEntry": askeySystemUserAccountEntry,
       "askeySystemUserAccountUserName": askeySystemUserAccountUserName,
       "askeySystemUserAccountPassword": askeySystemUserAccountPassword,
       "askeySystemUserAccountGroup": askeySystemUserAccountGroup,
       "askeySystemUserAccountRowStatus": askeySystemUserAccountRowStatus,
       "askeyPPPoE": askeyPPPoE,
       "suboption": suboption,
       "dnsService": dnsService,
       "dnsServer1IPAddress": dnsServer1IPAddress,
       "dnsServer2IPAddress": dnsServer2IPAddress,
       "dnsServer3IPAddress": dnsServer3IPAddress,
       "timeService": timeService,
       "protocol": protocol,
       "updatePeriod": updatePeriod,
       "timeServer1InetAddress": timeServer1InetAddress,
       "timeServer2InetAddress": timeServer2InetAddress,
       "timeServer3InetAddress": timeServer3InetAddress,
       "timeServer1Status": timeServer1Status,
       "timeServer2Status": timeServer2Status,
       "timeServer3Status": timeServer3Status,
       "timeZone": timeZone,
       "ugeMIBObjects": ugeMIBObjects,
       "ugeAutoNegotiationTable": ugeAutoNegotiationTable,
       "ugeAutoNegotionEntry": ugeAutoNegotionEntry,
       "autoNegotiationState": autoNegotiationState,
       "ugePauseFrameStatisticTable": ugePauseFrameStatisticTable,
       "ugePauseFrameStatisticEntry": ugePauseFrameStatisticEntry,
       "rxPausePackets": rxPausePackets,
       "txPausePackets": txPausePackets,
       "subtendVLANTable": subtendVLANTable,
       "subtendVLANEntry": subtendVLANEntry,
       "subtendState": subtendState,
       "subtendVLAN": subtendVLAN,
       "ugeVLANTable": ugeVLANTable,
       "ugeVLANEntry": ugeVLANEntry,
       "ugeVLAN": ugeVLAN,
       "securedHosts": securedHosts,
       "securedHostAdminStatus": securedHostAdminStatus,
       "securedHostTable": securedHostTable,
       "securedHostEntry": securedHostEntry,
       "securedIPSectorIndex": securedIPSectorIndex,
       "securedIPSectorStartIP": securedIPSectorStartIP,
       "securedIPSectorEndIP": securedIPSectorEndIP,
       "allowedServiceType": allowedServiceType,
       "netBIOSFilter": netBIOSFilter,
       "netBIOSFilterAction": netBIOSFilterAction}
)
